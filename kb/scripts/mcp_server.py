"""MCP server exposing the physiological-rights KB to Claude Code.

Registered via `.mcp.json` at the repo root. When Claude Code starts in this
project it will (after user approval) launch this server over stdio and gain
two tools:

- `kb_query`      — hybrid retrieval (dense + BM25 + MMR + authority weight)
- `kb_list_sources` — inventory of what's currently indexed
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import voyageai  # noqa: E402
from mcp.server.fastmcp import FastMCP  # noqa: E402

from config import require_voyage_key  # noqa: E402
from query import (  # noqa: E402
    _bm25_search,
    _dense_search,
    _embed_query,
    _fetch_embeddings,
    _hybrid_rerank,
    _mmr_select,
)
from schema import init_db  # noqa: E402


mcp = FastMCP("physiological-rights-kb")

_client: voyageai.Client | None = None
_conn = None


def _get_client() -> voyageai.Client:
    global _client
    if _client is None:
        require_voyage_key()
        _client = voyageai.Client()
    return _client


def _get_conn():
    global _conn
    if _conn is None:
        _conn = init_db()
    return _conn


@mcp.tool()
def kb_query(
    query: str,
    k: int = 6,
    types: list[str] | None = None,
    mmr_lambda: float = 0.7,
) -> list[dict[str, Any]]:
    """Search the physiological-rights personal knowledge base.

    Use this whenever Perig asks about nutrients, vitamins, minerals,
    conditionally essential compounds, physiological rights, or any
    biological or clinical topic that may be documented in the corpus.
    The KB contains site content (definitions, reports, critique,
    editorials, resources), personal notes (_private/), and — as ingestion
    grows — external scientific sources.

    Retrieval is hybrid: dense embeddings + BM25 over FTS5, reranked by
    the manually-assigned authority_score, then MMR to enforce source
    diversity.

    Args:
        query: the natural-language question or search phrase.
        k: number of results to return. Default 6. Up to ~12 is comfortable.
        types: optional filter by source_type — subset of
            ["definitions", "reports", "critique", "editorials",
             "resources", "inbox", "private"].
        mmr_lambda: relevance/diversity trade-off, in [0, 1].
            1.0 = pure relevance (may return near-duplicates from long sources);
            0.5 = strong diversity (surfaces distinct sources);
            default 0.7.

    Returns:
        List of chunk records, each carrying source_path, source_type,
        section, title, source_category, authority_score, relevance_score,
        dense_score, bm25_score, and the full chunk content.
    """
    client = _get_client()
    conn = _get_conn()
    embedding = _embed_query(client, query)

    pool_size = max(k * 4, 20)
    dense = _dense_search(conn, embedding, k=pool_size, types=types)
    sparse = _bm25_search(conn, query, k=pool_size, types=types)
    ranked = _hybrid_rerank(dense, sparse)

    if len(ranked) > k:
        candidate_ids = [r["id"] for r in ranked[:pool_size]]
        embeddings_ = _fetch_embeddings(conn, candidate_ids)
        results = _mmr_select(ranked[:pool_size], embeddings_, k=k, lambda_=mmr_lambda)
    else:
        results = ranked[:k]

    return [
        {
            "source_path": r["source_path"],
            "source_type": r["source_type"],
            "title": r["title"],
            "section": r["section"],
            "source_category": r["source_category"],
            "authority_score": r["authority_score"],
            "relevance_score": round(r["score"], 3),
            "dense_score": round(r["dense_score"], 3),
            "bm25_score": round(r["bm25_score"], 3),
            "content": r["content"],
        }
        for r in results
    ]


@mcp.tool()
def kb_list_sources() -> dict[str, Any]:
    """Return an inventory of what's currently in the KB.

    Use this when you want to know what's available before deciding whether
    a `kb_query` will be useful, or when Perig asks about the state of the
    corpus.

    Returns:
        A dict with total_chunks, per-type counts (chunks + files), and the
        list of source files with their type, chunk count, and authority_score.
    """
    conn = _get_conn()

    total = conn.execute("SELECT COUNT(*) AS c FROM chunks").fetchone()["c"]

    by_type_rows = conn.execute(
        """
        SELECT source_type,
               COUNT(*) AS chunks,
               COUNT(DISTINCT source_path) AS files
        FROM chunks
        GROUP BY source_type
        ORDER BY source_type
        """
    ).fetchall()

    sources_rows = conn.execute(
        """
        SELECT source_path,
               source_type,
               COUNT(*) AS chunks,
               MAX(authority_score) AS authority_score,
               MAX(source_category) AS source_category
        FROM chunks
        GROUP BY source_path
        ORDER BY source_type, source_path
        """
    ).fetchall()

    return {
        "total_chunks": total,
        "by_type": [
            {"source_type": r["source_type"], "chunks": r["chunks"], "files": r["files"]}
            for r in by_type_rows
        ],
        "sources": [
            {
                "path": r["source_path"],
                "type": r["source_type"],
                "chunks": r["chunks"],
                "authority_score": r["authority_score"],
                "source_category": r["source_category"],
            }
            for r in sources_rows
        ],
    }


if __name__ == "__main__":
    mcp.run()
