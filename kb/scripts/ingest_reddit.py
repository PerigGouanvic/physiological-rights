"""Ingest Reddit posts and comments from kb/reddit/*.jsonl.zst into the KB.

Streams each .zst frame-by-frame (no full decompression), filters by minimum
body length and score, chunks with the same markdown chunker used for the
Jekyll corpus, embeds via Voyage in batches, and writes to the same `chunks`
+ `chunk_vec` tables with `source_type = 'reddit'`.

Filters (defaults, all tunable):
- body must be >= 300 characters after strip
- score >= 3
- selftext/body not in {'', '[deleted]', '[removed]'}
- item.removed_by_category must be null

Idempotence: source_path is `reddit/<sub>/<id>`. If any chunk with that
source_path already exists, the item is skipped. Use --force to re-ingest.

Usage:
    python ingest_reddit.py --stats                      # dry-run + cost estimate
    python ingest_reddit.py                              # ingest everything
    python ingest_reddit.py --subs Magnesium,B12_Deficiency
    python ingest_reddit.py --kinds posts                # skip comments
    python ingest_reddit.py --min-len 500 --min-score 10 # tighter filter
    python ingest_reddit.py --force                      # re-ingest all
"""

from __future__ import annotations

import argparse
import io
import json
import sqlite3
import struct
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import voyageai
import zstandard as zstd

from chunker import Chunk, chunk_markdown, estimate_tokens
from config import (
    EMBED_MODEL,
    INGEST_BATCH_SIZE,
    KB_ROOT,
    LOGS_DIR,
    require_voyage_key,
)
from schema import init_db

REDDIT_DIR = KB_ROOT / "reddit"

DEFAULT_MIN_LEN = 300
DEFAULT_MIN_SCORE = 3
DEFAULT_AUTHORITY = 0.3

VOYAGE_PRICE_PER_MTOKENS = {
    "voyage-3": 0.06,
    "voyage-3-large": 0.18,
    "voyage-3-lite": 0.02,
    "voyage-3.5": 0.06,
    "voyage-3.5-lite": 0.02,
}

DELETED_MARKERS = {"", "[deleted]", "[removed]"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _hash_text(text: str) -> str:
    import hashlib
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _serialize_vector(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def _log(msg: str, log_path: Path) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    line = f"[{_now()}] {msg}"
    print(line, flush=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def iter_items(path: Path):
    """Yield JSON objects from a .zst NDJSON file, tolerating decode errors."""
    dctx = zstd.ZstdDecompressor()
    with path.open("rb") as f, dctx.stream_reader(f) as r:
        buf = io.BufferedReader(r, 1024 * 1024)
        for line in buf:
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def item_passes_filter(item: dict, kind: str, min_len: int, min_score: int) -> bool:
    if item.get("removed_by_category"):
        return False
    body = (item.get("selftext") if kind == "posts" else item.get("body")) or ""
    body = body.strip()
    if body in DELETED_MARKERS or len(body) < min_len:
        return False
    try:
        score = int(item.get("score", 0))
    except (TypeError, ValueError):
        score = 0
    if score < min_score:
        return False
    return True


def build_document(item: dict, kind: str, sub: str) -> tuple[str, str, str, dict]:
    """Return (source_path, title, content, meta)."""
    rid = item.get("id", "")
    source_path = f"reddit/{sub}/{rid}"
    if kind == "posts":
        title = (item.get("title") or "").strip() or f"r/{sub} post {rid}"
        body = (item.get("selftext") or "").strip()
        content = f"{title}\n\n{body}" if body else title
    else:
        body = (item.get("body") or "").strip()
        snippet = body[:80].replace("\n", " ")
        title = f"r/{sub} comment: {snippet}"
        content = body

    permalink = item.get("permalink") or ""
    meta = {
        "sub": sub,
        "kind": kind,
        "id": rid,
        "permalink": f"https://reddit.com{permalink}" if permalink else "",
        "score": int(item.get("score") or 0),
        "num_comments": int(item.get("num_comments") or 0),
        "created_utc": int(item.get("created_utc") or 0),
        "author": item.get("author") or "",
    }
    return source_path, title, content, meta


def paths_for(subs: set[str] | None, kinds: tuple[str, ...]) -> list[Path]:
    all_paths = sorted(REDDIT_DIR.glob("*.jsonl.zst"))
    out = []
    for p in all_paths:
        stem = p.name[: -len(".jsonl.zst")]
        parts = stem.rsplit("_", 1)
        if len(parts) != 2:
            continue
        sub, kind = parts
        if kind not in kinds:
            continue
        if subs and sub not in subs:
            continue
        out.append(p)
    return out


def existing_source_paths(conn: sqlite3.Connection) -> set[str]:
    """Load the set of Reddit source_paths already ingested (for idempotence)."""
    rows = conn.execute(
        "SELECT DISTINCT source_path FROM chunks WHERE source_type = 'reddit'"
    ).fetchall()
    return {r["source_path"] for r in rows}


def _embed_batch(client: voyageai.Client, texts: list[str]) -> list[list[float]]:
    result = client.embed(texts=texts, model=EMBED_MODEL, input_type="document")
    return result.embeddings


def _flush(
    conn: sqlite3.Connection,
    client: voyageai.Client | None,
    pending: list[dict],
    log_path: Path,
    dry_run: bool,
) -> int:
    if not pending:
        return 0
    texts = [p["content"] for p in pending]
    if dry_run:
        return 0

    backoff = 2.0
    for attempt in range(6):
        try:
            vectors = _embed_batch(client, texts)
            break
        except Exception as exc:
            _log(f"  embed error (attempt {attempt+1}): {exc}, retry in {backoff:.0f}s", log_path)
            time.sleep(backoff)
            backoff = min(backoff * 2, 60.0)
    else:
        _log(f"  gave up on batch of {len(texts)}", log_path)
        return 0

    now = _now()
    written = 0
    for record, vector in zip(pending, vectors):
        cur = conn.execute(
            """
            INSERT INTO chunks (
                source_path, source_type, title, section, authority_score,
                source_category, frontmatter_json, content, token_count,
                content_hash, ingested_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record["source_path"],
                "reddit",
                record["title"],
                record["section"],
                record["authority_score"],
                record["source_category"],
                record["frontmatter_json"],
                record["content"],
                record["token_count"],
                record["content_hash"],
                now,
            ),
        )
        chunk_id = cur.lastrowid
        conn.execute(
            "INSERT INTO chunk_vec (chunk_id, embedding) VALUES (?, ?)",
            (chunk_id, _serialize_vector(vector)),
        )
        written += 1
    conn.commit()
    return written


def ingest_reddit(
    *,
    subs: set[str] | None,
    kinds: tuple[str, ...],
    min_len: int,
    min_score: int,
    authority: float,
    stats_only: bool,
    force: bool,
) -> None:
    log_path = LOGS_DIR / f"ingest-reddit-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
    conn = init_db()

    client: voyageai.Client | None = None
    if not stats_only:
        require_voyage_key()
        client = voyageai.Client()

    paths = paths_for(subs, kinds)
    if not paths:
        _log("No matching .jsonl.zst files.", log_path)
        return

    _log(
        f"Scanning {len(paths)} files (kinds={list(kinds)}, "
        f"min_len={min_len}, min_score={min_score}, authority={authority}, "
        f"stats_only={stats_only}, force={force})",
        log_path,
    )

    seen = set() if force else existing_source_paths(conn)
    _log(f"  {len(seen)} Reddit source_paths already in KB", log_path)

    pending: list[dict] = []
    total_scanned = 0
    total_kept = 0
    total_skipped_existing = 0
    total_chunks = 0
    total_tokens = 0
    total_written = 0

    for path in paths:
        stem = path.name[: -len(".jsonl.zst")]
        sub, kind = stem.rsplit("_", 1)
        file_kept = 0
        file_scanned = 0

        for item in iter_items(path):
            file_scanned += 1
            total_scanned += 1
            if not item_passes_filter(item, kind, min_len, min_score):
                continue

            source_path, title, content, meta = build_document(item, kind, sub)
            if source_path in seen:
                total_skipped_existing += 1
                continue

            chunks = chunk_markdown(content)
            if not chunks:
                continue

            file_kept += 1
            total_kept += 1
            frontmatter_json = json.dumps(meta, ensure_ascii=False, sort_keys=True)

            for c in chunks:
                total_chunks += 1
                total_tokens += c.token_count
                if stats_only:
                    continue
                pending.append({
                    "source_path": source_path,
                    "title": title,
                    "section": c.section,
                    "authority_score": authority,
                    "source_category": sub,
                    "frontmatter_json": frontmatter_json,
                    "content": c.content,
                    "token_count": c.token_count,
                    "content_hash": _hash_text(c.content),
                })

            seen.add(source_path)

            if not stats_only and len(pending) >= INGEST_BATCH_SIZE:
                batch = pending[:INGEST_BATCH_SIZE]
                pending = pending[INGEST_BATCH_SIZE:]
                total_written += _flush(conn, client, batch, log_path, dry_run=False)

        _log(
            f"  {path.name}: scanned={file_scanned}, kept={file_kept}",
            log_path,
        )

    if not stats_only:
        total_written += _flush(conn, client, pending, log_path, dry_run=False)

    price = VOYAGE_PRICE_PER_MTOKENS.get(EMBED_MODEL, 0.06)
    est_cost = total_tokens / 1_000_000 * price

    _log(
        f"DONE — scanned={total_scanned}, kept={total_kept}, "
        f"skipped_existing={total_skipped_existing}, chunks={total_chunks}, "
        f"tokens≈{total_tokens} (est {EMBED_MODEL} cost ${est_cost:.2f}), "
        f"written={total_written}",
        log_path,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--subs", help="comma-separated subreddit names to restrict")
    ap.add_argument("--kinds", default="posts,comments",
                    help="comma-separated: posts,comments (default: both)")
    ap.add_argument("--min-len", type=int, default=DEFAULT_MIN_LEN,
                    help=f"minimum body chars (default {DEFAULT_MIN_LEN})")
    ap.add_argument("--min-score", type=int, default=DEFAULT_MIN_SCORE,
                    help=f"minimum item score (default {DEFAULT_MIN_SCORE})")
    ap.add_argument("--authority", type=float, default=DEFAULT_AUTHORITY,
                    help=f"authority_score for Reddit chunks (default {DEFAULT_AUTHORITY})")
    ap.add_argument("--stats", action="store_true",
                    help="dry-run: scan, filter, chunk, count tokens; no embedding, no writes")
    ap.add_argument("--force", action="store_true",
                    help="re-ingest even items already present (does NOT delete existing)")
    args = ap.parse_args()

    subs = {s.strip() for s in args.subs.split(",")} if args.subs else None
    kinds = tuple(k.strip() for k in args.kinds.split(",") if k.strip())

    ingest_reddit(
        subs=subs,
        kinds=kinds,
        min_len=args.min_len,
        min_score=args.min_score,
        authority=args.authority,
        stats_only=args.stats,
        force=args.force,
    )


if __name__ == "__main__":
    main()
