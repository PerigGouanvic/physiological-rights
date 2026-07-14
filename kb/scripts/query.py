"""Query the KB.

v1: hybrid retrieval (dense + BM25 via FTS5), simple authority-weighted rerank.
MMR (diversity) and true cross-encoder reranking will land in a later iteration.

Usage:
    python query.py "quels nutriments cofacteurs pour la thyroïde"
    python query.py "..." --k 8 --type reports,critique
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import struct
import sys

import voyageai

from config import EMBED_MODEL, require_voyage_key
from schema import get_conn


def _serialize_vector(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def _embed_query(client: voyageai.Client, query: str) -> list[float]:
    result = client.embed(texts=[query], model=EMBED_MODEL, input_type="query")
    return result.embeddings[0]


def _dense_search(
    conn: sqlite3.Connection,
    embedding: list[float],
    k: int,
    types: list[str] | None,
) -> dict[int, dict]:
    """Return {chunk_id: {row + 'dense_score'}} where score is 1/(1+distance)."""
    type_filter = ""
    params: list = [_serialize_vector(embedding), k * 4]  # over-fetch for filtering
    if types:
        placeholders = ",".join("?" * len(types))
        type_filter = f"AND c.source_type IN ({placeholders})"
        params = [_serialize_vector(embedding), k * 4, *types]

    rows = conn.execute(
        f"""
        SELECT c.id, c.source_path, c.source_type, c.title, c.section,
               c.authority_score, c.source_category, c.content,
               v.distance
        FROM chunk_vec v
        JOIN chunks c ON c.id = v.chunk_id
        WHERE v.embedding MATCH ?
          AND v.k = ?
          {type_filter}
        ORDER BY v.distance
        """,
        params,
    ).fetchall()

    out: dict[int, dict] = {}
    for row in rows[:k]:
        d = dict(row)
        d["dense_score"] = 1.0 / (1.0 + row["distance"])
        out[row["id"]] = d
    return out


def _fts_query_from(query: str) -> str:
    """Turn a user query into an FTS5 MATCH expression tolerant of noise."""
    tokens = re.findall(r"\w+", query, flags=re.UNICODE)
    tokens = [t for t in tokens if len(t) > 2]
    if not tokens:
        return query
    return " OR ".join(f'"{t}"' for t in tokens)


def _bm25_search(
    conn: sqlite3.Connection,
    query: str,
    k: int,
    types: list[str] | None,
) -> dict[int, dict]:
    match = _fts_query_from(query)
    type_filter = ""
    params: list = [match, k * 4]
    if types:
        placeholders = ",".join("?" * len(types))
        type_filter = f"AND c.source_type IN ({placeholders})"
        params = [match, k * 4, *types]

    try:
        rows = conn.execute(
            f"""
            SELECT c.id, c.source_path, c.source_type, c.title, c.section,
                   c.authority_score, c.source_category, c.content,
                   bm25(chunks_fts) AS bm25_raw
            FROM chunks_fts
            JOIN chunks c ON c.id = chunks_fts.rowid
            WHERE chunks_fts MATCH ?
              {type_filter}
            ORDER BY bm25_raw
            LIMIT ?
            """,
            [match, *(types or []), k * 4],
        ).fetchall()
    except sqlite3.OperationalError:
        return {}

    if not rows:
        return {}

    raw_scores = [-row["bm25_raw"] for row in rows]
    max_raw = max(raw_scores) if raw_scores else 1.0
    min_raw = min(raw_scores) if raw_scores else 0.0
    span = max_raw - min_raw or 1.0

    out: dict[int, dict] = {}
    for row, raw in zip(rows[:k], raw_scores[:k]):
        d = dict(row)
        d["bm25_score"] = (raw - min_raw) / span
        out[row["id"]] = d
    return out


def _hybrid_rerank(
    dense: dict[int, dict],
    sparse: dict[int, dict],
    *,
    alpha: float = 0.6,
) -> list[dict]:
    """Combine dense + sparse scores, weight by authority, sort."""
    ids = set(dense) | set(sparse)
    merged: list[dict] = []
    for cid in ids:
        base = dense.get(cid) or sparse.get(cid)
        dense_s = dense.get(cid, {}).get("dense_score", 0.0)
        sparse_s = sparse.get(cid, {}).get("bm25_score", 0.0)
        combined = alpha * dense_s + (1 - alpha) * sparse_s
        weighted = combined * base["authority_score"]
        merged.append({**base, "dense_score": dense_s, "bm25_score": sparse_s, "score": weighted})
    merged.sort(key=lambda r: r["score"], reverse=True)
    return merged


def query(text: str, k: int = 6, types: list[str] | None = None, as_json: bool = False) -> None:
    require_voyage_key()
    client = voyageai.Client()
    embedding = _embed_query(client, text)

    conn = get_conn()
    dense = _dense_search(conn, embedding, k=k * 2, types=types)
    sparse = _bm25_search(conn, text, k=k * 2, types=types)
    results = _hybrid_rerank(dense, sparse)[:k]

    if as_json:
        print(json.dumps(
            [{k_: v for k_, v in r.items() if k_ != "content"} | {"content": r["content"]} for r in results],
            ensure_ascii=False, indent=2, default=str,
        ))
        return

    if not results:
        print("Aucun résultat.")
        return

    for i, r in enumerate(results, 1):
        header = f"[{i}] score={r['score']:.3f} (dense={r['dense_score']:.2f} bm25={r['bm25_score']:.2f} authority={r['authority_score']:.2f})"
        print(header)
        print(f"    source : {r['source_path']}  ({r['source_type']})")
        if r["section"]:
            print(f"    section: {r['section']}")
        if r["source_category"]:
            print(f"    catégorie: {r['source_category']}")
        excerpt = r["content"].strip().replace("\n", " ")
        if len(excerpt) > 400:
            excerpt = excerpt[:400] + "…"
        print(f"    {excerpt}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("query", nargs="+", help="the query text")
    parser.add_argument("--k", type=int, default=6, help="number of results (default 6)")
    parser.add_argument("--type", type=str, help="comma-separated source_types to filter (e.g. reports,critique)")
    parser.add_argument("--json", action="store_true", help="emit structured JSON")
    args = parser.parse_args()
    types = [t.strip() for t in args.type.split(",")] if args.type else None
    query(" ".join(args.query), k=args.k, types=types, as_json=args.json)


if __name__ == "__main__":
    main()
