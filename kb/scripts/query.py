"""Query the KB.

Hybrid retrieval (dense + BM25 via FTS5), authority-weighted rerank, and
MMR (Maximal Marginal Relevance) for diversity. Prevents any single long
source from dominating the top-K results.

Usage:
    python query.py "quels nutriments cofacteurs pour la thyroïde"
    python query.py "..." --k 8 --type reports,critique
    python query.py "..." --mmr-lambda 0.5    # more diverse (default 0.7)
    python query.py "..." --no-mmr            # disable MMR entirely
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
import struct
import sys

import voyageai

from config import EMBED_DIM, EMBED_MODEL, require_voyage_key
from schema import get_conn


def _serialize_vector(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def _deserialize_vector(blob: bytes) -> list[float]:
    return list(struct.unpack(f"{EMBED_DIM}f", blob))


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


def _fetch_embeddings(conn: sqlite3.Connection, chunk_ids: list[int]) -> dict[int, list[float]]:
    if not chunk_ids:
        return {}
    q_marks = ",".join("?" * len(chunk_ids))
    rows = conn.execute(
        f"SELECT chunk_id, embedding FROM chunk_vec WHERE chunk_id IN ({q_marks})",
        chunk_ids,
    ).fetchall()
    return {row["chunk_id"]: _deserialize_vector(row["embedding"]) for row in rows}


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def _mmr_select(
    candidates: list[dict],
    embeddings: dict[int, list[float]],
    k: int,
    lambda_: float,
) -> list[dict]:
    """Greedy MMR selection.

    Relevance is taken from `candidate['score']` (already authority-weighted).
    Similarity between candidates is cosine sim of their embeddings.
    Both are normalized to [0, 1] so lambda has meaningful semantics.
    """
    if not candidates:
        return []

    max_rel = max(c["score"] for c in candidates) or 1.0
    for c in candidates:
        c["_norm_rel"] = c["score"] / max_rel

    selected: list[dict] = [candidates[0]]
    remaining: list[dict] = list(candidates[1:])

    while len(selected) < k and remaining:
        best_score = -math.inf
        best_idx = -1
        for i, cand in enumerate(remaining):
            cand_emb = embeddings.get(cand["id"])
            if cand_emb is None:
                sim_to_selected = 0.0
            else:
                sim_to_selected = max(
                    max(0.0, _cosine(cand_emb, embeddings[s["id"]]))
                    for s in selected
                    if s["id"] in embeddings
                ) if any(s["id"] in embeddings for s in selected) else 0.0
            mmr = lambda_ * cand["_norm_rel"] - (1.0 - lambda_) * sim_to_selected
            if mmr > best_score:
                best_score = mmr
                best_idx = i
        if best_idx < 0:
            break
        selected.append(remaining.pop(best_idx))

    for c in selected:
        c.pop("_norm_rel", None)
    return selected


def query(
    text: str,
    k: int = 6,
    types: list[str] | None = None,
    as_json: bool = False,
    mmr_lambda: float = 0.7,
    use_mmr: bool = True,
) -> None:
    require_voyage_key()
    client = voyageai.Client()
    embedding = _embed_query(client, text)

    conn = get_conn()
    pool_size = max(k * 4, 20)
    dense = _dense_search(conn, embedding, k=pool_size, types=types)
    sparse = _bm25_search(conn, text, k=pool_size, types=types)
    ranked = _hybrid_rerank(dense, sparse)

    if use_mmr and len(ranked) > k:
        candidate_ids = [r["id"] for r in ranked[:pool_size]]
        embeddings = _fetch_embeddings(conn, candidate_ids)
        results = _mmr_select(ranked[:pool_size], embeddings, k=k, lambda_=mmr_lambda)
    else:
        results = ranked[:k]

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
    parser.add_argument("--mmr-lambda", type=float, default=0.7,
                        help="MMR relevance/diversity trade-off (1.0 = pure relevance, 0.0 = pure diversity, default 0.7)")
    parser.add_argument("--no-mmr", action="store_true", help="disable MMR diversity selection")
    args = parser.parse_args()
    types = [t.strip() for t in args.type.split(",")] if args.type else None
    query(
        " ".join(args.query),
        k=args.k,
        types=types,
        as_json=args.json,
        mmr_lambda=args.mmr_lambda,
        use_mmr=not args.no_mmr,
    )


if __name__ == "__main__":
    main()
