"""Ingest Markdown files from the repo into the KB.

Sources covered:
- Jekyll collections listed in config.JEKYLL_COLLECTIONS
- `_private/` (personal notes, not versioned)

Behavior:
- Idempotent: files are hashed; unchanged files are skipped.
- If a file changed, its previous chunks are deleted and re-ingested.
- Frontmatter fields recognized: `title`, `authority_score`, `source_category`.
- Embeddings are batched to Voyage; failures on a batch are logged and skipped.

Usage:
    python ingest.py                    # ingest everything (skips unchanged)
    python ingest.py --force            # re-ingest everything
    python ingest.py --path _private    # ingest just one folder
    python ingest.py --dry-run          # parse + chunk, no API calls, no writes
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

import frontmatter
import voyageai

from chunker import Chunk, chunk_markdown
from config import (
    EMBED_MODEL,
    INGEST_BATCH_SIZE,
    JEKYLL_COLLECTIONS,
    LOGS_DIR,
    PRIVATE_DIR,
    REPO_ROOT,
    require_voyage_key,
)
from schema import init_db


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _iter_source_files(only: Path | None = None) -> list[tuple[Path, str]]:
    """Yield (absolute_path, source_type) for every markdown file to consider."""
    files: list[tuple[Path, str]] = []
    roots: list[tuple[Path, str]] = []

    if only is not None:
        target = (REPO_ROOT / only).resolve()
        roots.append((target, target.name.lstrip("_")))
    else:
        for name in JEKYLL_COLLECTIONS:
            roots.append((REPO_ROOT / name, name.lstrip("_")))
        roots.append((PRIVATE_DIR, "private"))

    for root, source_type in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path.is_file():
                files.append((path, source_type))
    return files


def _read_markdown(path: Path) -> tuple[dict, str]:
    with path.open("r", encoding="utf-8") as f:
        post = frontmatter.load(f)
    return post.metadata, post.content


def _serialize_vector(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def _delete_existing(conn: sqlite3.Connection, source_path: str) -> None:
    ids = [row["id"] for row in conn.execute("SELECT id FROM chunks WHERE source_path = ?", (source_path,))]
    if not ids:
        return
    q_marks = ",".join("?" * len(ids))
    conn.execute(f"DELETE FROM chunk_vec WHERE chunk_id IN ({q_marks})", ids)
    conn.execute(f"DELETE FROM chunks WHERE id IN ({q_marks})", ids)
    conn.execute("DELETE FROM source_files WHERE source_path = ?", (source_path,))


def _log(msg: str, log_path: Path) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    line = f"[{_now()}] {msg}"
    print(line)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def _embed_batch(client: voyageai.Client, texts: list[str]) -> list[list[float]]:
    result = client.embed(texts=texts, model=EMBED_MODEL, input_type="document")
    return result.embeddings


def _flush_pending(
    conn: sqlite3.Connection,
    client: voyageai.Client,
    pending: list[dict],
    log_path: Path,
    dry_run: bool,
) -> int:
    """Embed and persist a batch of pending chunk records. Returns count written."""
    if not pending:
        return 0
    texts = [p["content"] for p in pending]
    if dry_run:
        _log(f"DRY: would embed {len(texts)} chunks", log_path)
        return 0
    try:
        vectors = _embed_batch(client, texts)
    except Exception as exc:
        _log(f"ERROR embedding batch of {len(texts)}: {exc}", log_path)
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
                record["source_type"],
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


def ingest(only: Path | None = None, force: bool = False, dry_run: bool = False) -> None:
    log_path = LOGS_DIR / f"ingest-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
    conn = init_db()

    client: voyageai.Client | None = None
    if not dry_run:
        require_voyage_key()
        client = voyageai.Client()

    files = _iter_source_files(only=only)
    _log(f"Discovered {len(files)} markdown files", log_path)

    pending: list[dict] = []
    total_chunks_written = 0
    files_ingested = 0
    files_skipped = 0

    for path, source_type in files:
        rel = str(path.relative_to(REPO_ROOT))
        try:
            metadata, body = _read_markdown(path)
        except Exception as exc:
            _log(f"SKIP (read error) {rel}: {exc}", log_path)
            continue

        file_hash = _hash_text(body + json.dumps(metadata, sort_keys=True, default=str))

        existing = conn.execute(
            "SELECT file_hash FROM source_files WHERE source_path = ?", (rel,)
        ).fetchone()
        if existing and existing["file_hash"] == file_hash and not force:
            files_skipped += 1
            continue

        _delete_existing(conn, rel)

        title = metadata.get("title") or path.stem
        authority_score = float(metadata.get("authority_score", 1.0))
        source_category = metadata.get("source_category")

        chunks: list[Chunk] = chunk_markdown(body)
        if not chunks:
            _log(f"SKIP (empty) {rel}", log_path)
            continue

        conn.execute(
            """
            INSERT INTO source_files (source_path, file_hash, source_type,
                authority_score, source_category, ingested_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (rel, file_hash, source_type, authority_score, source_category, _now()),
        )

        frontmatter_json = json.dumps(metadata, sort_keys=True, default=str, ensure_ascii=False)
        for c in chunks:
            pending.append({
                "source_path": rel,
                "source_type": source_type,
                "title": title,
                "section": c.section,
                "authority_score": authority_score,
                "source_category": source_category,
                "frontmatter_json": frontmatter_json,
                "content": c.content,
                "token_count": c.token_count,
                "content_hash": _hash_text(c.content),
            })

        files_ingested += 1
        _log(f"CHUNKED {rel} → {len(chunks)} chunks (type={source_type})", log_path)

        while len(pending) >= INGEST_BATCH_SIZE:
            batch = pending[:INGEST_BATCH_SIZE]
            pending = pending[INGEST_BATCH_SIZE:]
            total_chunks_written += _flush_pending(conn, client, batch, log_path, dry_run)

    total_chunks_written += _flush_pending(conn, client, pending, log_path, dry_run)

    _log(
        f"DONE — files_ingested={files_ingested} files_skipped={files_skipped} "
        f"chunks_written={total_chunks_written}",
        log_path,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--force", action="store_true", help="re-ingest all files")
    parser.add_argument("--path", type=Path, help="ingest a single folder (relative to repo root)")
    parser.add_argument("--dry-run", action="store_true", help="parse and chunk without embedding or writing")
    args = parser.parse_args()
    ingest(only=args.path, force=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
