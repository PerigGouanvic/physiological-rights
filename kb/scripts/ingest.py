"""Ingest Markdown and PDF files from the repo into the KB.

Sources covered:
- Jekyll collections listed in config.JEKYLL_COLLECTIONS (markdown, frontmatter)
- `kb/sources/` (external PDFs, sidecar YAML for metadata)

Behavior:
- Idempotent: files are hashed; unchanged files are skipped.
- If a file changed, its previous chunks are deleted and re-ingested.
- Markdown metadata: `title`, `authority_score`, `source_category` in frontmatter.
- PDF metadata: optional sidecar `<name>.meta.yaml` with the same fields (plus
  free-form `authors`, `year`, `url`, ...); if absent, defaults are used.
- Embeddings are batched to Voyage; failures on a batch are logged and skipped.

Usage:
    python ingest.py                    # ingest everything (skips unchanged)
    python ingest.py --force            # re-ingest everything
    python ingest.py --path _reports    # ingest just one folder
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
import pdfplumber
import voyageai
import yaml

from chunker import Chunk, chunk_markdown
from config import (
    EMBED_MODEL,
    INGEST_BATCH_SIZE,
    JEKYLL_COLLECTIONS,
    LOGS_DIR,
    REPO_ROOT,
    SOURCES_DIR,
    require_voyage_key,
)
from schema import init_db


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _iter_source_files(only: Path | None = None) -> list[tuple[Path, str, str]]:
    """Yield (absolute_path, source_type, kind) tuples.

    kind is either "markdown" or "pdf" and dictates which reader is used.
    """
    files: list[tuple[Path, str, str]] = []

    def _scan(root: Path, source_type: str) -> None:
        if not root.exists():
            return
        for path in root.rglob("*.md"):
            if path.is_file():
                files.append((path, source_type, "markdown"))
        for path in root.rglob("*.pdf"):
            if path.is_file():
                files.append((path, source_type, "pdf"))

    if only is not None:
        target = (REPO_ROOT / only).resolve()
        _scan(target, target.name.lstrip("_"))
    else:
        for name in JEKYLL_COLLECTIONS:
            _scan(REPO_ROOT / name, name.lstrip("_"))
        _scan(SOURCES_DIR, "sources-external")

    return files


def _read_markdown(path: Path) -> tuple[dict, str]:
    with path.open("r", encoding="utf-8") as f:
        post = frontmatter.load(f)
    return post.metadata, post.content


def _read_pdf(path: Path) -> tuple[dict, str]:
    """Extract text and metadata from a PDF.

    Metadata precedence: sidecar `<name>.meta.yaml` > embedded PDF metadata >
    filename-derived defaults. Page breaks are marked in the body as
    `[page N]` on their own line so the downstream chunker can split cleanly
    and human readers can locate a snippet.
    """
    sidecar = path.with_suffix(".meta.yaml")
    metadata: dict = {}
    if sidecar.exists():
        with sidecar.open("r", encoding="utf-8") as f:
            loaded = yaml.safe_load(f) or {}
        if isinstance(loaded, dict):
            metadata = loaded

    pages: list[str] = []
    with pdfplumber.open(path) as pdf:
        pdf_info = pdf.metadata or {}
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text = text.strip()
            if text:
                pages.append(f"[page {i}]\n\n{text}")

    if "title" not in metadata:
        metadata["title"] = pdf_info.get("Title") or path.stem
    body = "\n\n".join(pages)
    return metadata, body


def _read_source(path: Path, kind: str) -> tuple[dict, str]:
    if kind == "pdf":
        return _read_pdf(path)
    return _read_markdown(path)


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
    _log(f"Discovered {len(files)} source files (markdown + pdf)", log_path)

    pending: list[dict] = []
    total_chunks_written = 0
    files_ingested = 0
    files_skipped = 0

    for path, source_type, kind in files:
        rel = str(path.relative_to(REPO_ROOT))
        try:
            metadata, body = _read_source(path, kind)
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
