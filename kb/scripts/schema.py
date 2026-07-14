"""SQLite schema for the KB.

Two stores:
- `chunks` (regular table) — text + metadata for every chunk.
- `chunk_vec` (sqlite-vec virtual table) — embeddings, keyed by chunk id.
- `source_files` — file-level hashes to enable incremental re-ingestion.

Also builds an FTS5 index on chunk content for the BM25 half of hybrid search.
"""

from __future__ import annotations

import sqlite3

import sqlite_vec

from config import DB_DIR, DB_PATH, EMBED_DIM


CHUNK_SCHEMA = """
CREATE TABLE IF NOT EXISTS chunks (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    source_path       TEXT    NOT NULL,
    source_type       TEXT    NOT NULL,
    title             TEXT,
    section           TEXT,
    authority_score   REAL    NOT NULL DEFAULT 1.0,
    source_category   TEXT,
    frontmatter_json  TEXT,
    content           TEXT    NOT NULL,
    token_count       INTEGER,
    content_hash      TEXT    NOT NULL,
    ingested_at       TEXT    NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_path);
CREATE INDEX IF NOT EXISTS idx_chunks_type   ON chunks(source_type);
CREATE INDEX IF NOT EXISTS idx_chunks_hash   ON chunks(content_hash);

CREATE TABLE IF NOT EXISTS source_files (
    source_path      TEXT PRIMARY KEY,
    file_hash        TEXT NOT NULL,
    source_type      TEXT NOT NULL,
    authority_score  REAL NOT NULL DEFAULT 1.0,
    source_category  TEXT,
    ingested_at      TEXT NOT NULL
);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    content,
    title,
    content='chunks',
    content_rowid='id',
    tokenize='unicode61 remove_diacritics 2'
);

CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
    INSERT INTO chunks_fts(rowid, content, title) VALUES (new.id, new.content, new.title);
END;

CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, content, title) VALUES('delete', old.id, old.content, old.title);
END;

CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, content, title) VALUES('delete', old.id, old.content, old.title);
    INSERT INTO chunks_fts(rowid, content, title) VALUES (new.id, new.content, new.title);
END;
"""


def vec_schema(dim: int) -> str:
    return f"""
    CREATE VIRTUAL TABLE IF NOT EXISTS chunk_vec USING vec0(
        chunk_id INTEGER PRIMARY KEY,
        embedding FLOAT[{dim}]
    );
    """


def get_conn() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> sqlite3.Connection:
    conn = get_conn()
    conn.executescript(CHUNK_SCHEMA)
    conn.executescript(vec_schema(EMBED_DIM))
    conn.commit()
    return conn


if __name__ == "__main__":
    conn = init_db()
    print(f"Initialized {DB_PATH}")
    print("Tables:")
    for row in conn.execute("SELECT name FROM sqlite_master WHERE type IN ('table','virtual') ORDER BY name"):
        print(f"  - {row['name']}")
