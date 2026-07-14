"""Central configuration for the KB pipeline.

All paths are anchored to the repo root so scripts can be run from anywhere.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
KB_ROOT = REPO_ROOT / "kb"
DB_DIR = KB_ROOT / "db"
DB_PATH = DB_DIR / "kb.sqlite"
SOURCES_DIR = KB_ROOT / "sources"
LOGS_DIR = KB_ROOT / "logs"
PRIVATE_DIR = REPO_ROOT / "_private"

load_dotenv(REPO_ROOT / ".env")

VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY")

EMBED_MODEL = os.environ.get("KB_EMBED_MODEL", "voyage-3")
EMBED_DIM = int(os.environ.get("KB_EMBED_DIM", "1024"))

CHUNK_TARGET_TOKENS = 500
CHUNK_MAX_TOKENS = 900
CHUNK_MIN_TOKENS = 60

INGEST_BATCH_SIZE = 32

JEKYLL_COLLECTIONS = [
    "_definitions",
    "_reports",
    "_critique",
    "_editorials",
    "_resources",
    "_inbox",
]


def require_voyage_key() -> str:
    if not VOYAGE_API_KEY:
        raise SystemExit(
            "VOYAGE_API_KEY is not set. Copy .env.example to .env at the "
            "repo root and add your key, or export the variable in your shell."
        )
    return VOYAGE_API_KEY
