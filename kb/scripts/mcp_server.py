"""MCP server exposing the physiological-rights KB to Claude Code.

Registered via `.mcp.json` at the repo root. When Claude Code starts in this
project it will (after user approval) launch this server over stdio and gain
four tools:

- `kb_query`         — hybrid retrieval over the indexed corpus (Jekyll + sources)
- `kb_list_sources`  — inventory of what's currently indexed
- `kb_reddit_search` — grep-like regex search over the Reddit dumps (streaming, no index, no embedding cost)
- `kb_reddit_sources` — inventory of downloaded Reddit dumps
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
from reddit_search import list_reddit_sources, search_reddit  # noqa: E402
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
    editorials, resources) and — as ingestion grows — external
    scientific sources.

    Retrieval is hybrid: dense embeddings + BM25 over FTS5, reranked by
    the manually-assigned authority_score, then MMR to enforce source
    diversity.

    Args:
        query: the natural-language question or search phrase.
        k: number of results to return. Default 6. Up to ~12 is comfortable.
        types: optional filter by source_type — subset of
            ["definitions", "reports", "critique", "editorials",
             "resources", "inbox"].
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


@mcp.tool()
def kb_reddit_search(
    pattern: str,
    subs: list[str] | None = None,
    kinds: list[str] | None = None,
    limit: int = 20,
    min_len: int = 200,
    min_score: int = 0,
    context: int = 120,
    case_sensitive: bool = False,
    sort_by: str = "date",
) -> list[dict[str, Any]]:
    """Regex-search the raw Reddit corpus in kb/reddit/ (streaming, no index).

    Use this to find lived-experience testimony from patients and
    self-experimenters — reports of what a nutrient did or did not do, how
    a symptom presented, what a doctor said, what a lab test showed. Reddit
    is anecdotal by nature; treat hits as leads and testimony, not evidence.

    The Reddit corpus is NOT in the vector KB. This tool streams the
    compressed dumps and matches a Python regex against the post title
    and body (or comment body). No API cost, no embedding.

    Cost note: a scan without `subs` walks the entire ~3 GB corpus and
    can take minutes. Always pass `subs` when you can name the relevant
    subreddits.

    Args:
        pattern: Python regex, case-insensitive by default.
            Examples: "K2 arrhythmia", "\\bTSH\\b", "normal.{0,20}test".
        subs: subreddit names to restrict the scan (highly recommended).
            Example: ["MTHFR", "B12_Deficiency", "POTS"].
        kinds: "posts" and/or "comments". Default ["posts"]. Comments
            are only available for a few subs (see `kb_reddit_sources`).
        limit: maximum hits to return. Default 20.
        min_len: skip posts/comments shorter than this (chars). Default 200.
        min_score: skip items with Reddit score below this. Default 0.
        context: characters around each match in the snippet. Default 120.
        case_sensitive: default False.
        sort_by: "date" (newest first), "score", or "num_comments". Default "date".

    Returns:
        List of hit dicts: sub, kind, date, score, num_comments, title,
        body_len, snippet, permalink.
    """
    kinds_tuple = tuple(kinds) if kinds else ("posts",)
    return search_reddit(
        pattern,
        subs=subs,
        kinds=kinds_tuple,
        limit=limit,
        min_len=min_len,
        min_score=min_score,
        context=context,
        case_sensitive=case_sensitive,
        sort_by=sort_by,
    )


@mcp.tool()
def kb_reddit_sources() -> list[dict[str, Any]]:
    """Inventory of the Reddit dumps available for `kb_reddit_search`.

    Returns one entry per (subreddit, kind) file with size in MB and last
    modification date. Use this to know which subs are downloaded and how
    much material each one holds before choosing `subs` for a search.

    Returns:
        List of dicts: sub, kind, size_mb, modified.
    """
    return list_reddit_sources()


if __name__ == "__main__":
    mcp.run()
