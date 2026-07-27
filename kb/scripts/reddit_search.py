"""Grep-like search across the Reddit dumps in kb/reddit/.

Streams each .zst frame-by-frame — no full decompression, no in-memory load.
Matches a regex against title + selftext, returns structured results.
Exposed both as a CLI and as a callable used by the MCP server.

Usage:
    python reddit_search.py "<regex>"
    python reddit_search.py "normal.{0,20}test" --subs MTHFR,B12_Deficiency
    python reddit_search.py "\\bTSH\\b" --min-len 500 --limit 20
    python reddit_search.py "my doctor" --context 120 --sort-by score
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import re
import sys
from pathlib import Path

import zstandard as zstd

from config import KB_ROOT

REDDIT_DIR = KB_ROOT / "reddit"


def iter_items(path: Path):
    """Yield JSON objects from a .zst NDJSON file, skipping decode errors."""
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


def make_snippet(text: str, m: re.Match, ctx: int) -> str:
    start = max(0, m.start() - ctx)
    end = min(len(text), m.end() + ctx)
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(text) else ""
    return prefix + text[start:end].replace("\n", " ") + suffix


def find_paths(subs: set[str] | None, kinds: tuple[str, ...]) -> list[Path]:
    all_paths = sorted(REDDIT_DIR.glob("*.jsonl.zst"))
    out: list[Path] = []
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


def search_reddit(
    pattern: str,
    *,
    subs: list[str] | None = None,
    kinds: tuple[str, ...] = ("posts",),
    limit: int = 30,
    min_len: int = 200,
    min_score: int = 0,
    context: int = 120,
    case_sensitive: bool = False,
    sort_by: str = "date",
) -> list[dict]:
    """Run a regex search over Reddit .zst dumps and return structured hits.

    Returns:
        List of dicts with keys: sub, kind, created_utc, date, score,
        num_comments, title, body_len, snippet, permalink.
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    rx = re.compile(pattern, flags)
    subs_set = set(subs) if subs else None
    paths = find_paths(subs_set, kinds)
    if not paths:
        return []

    results: list[dict] = []
    for path in paths:
        stem = path.name[: -len(".jsonl.zst")]
        sub, kind = stem.rsplit("_", 1)
        for item in iter_items(path):
            title = item.get("title") or ""
            body = item.get("selftext") if kind == "posts" else item.get("body")
            body = body or ""
            if len(body) < min_len:
                continue
            try:
                score = int(item.get("score", 0))
            except (TypeError, ValueError):
                score = 0
            if score < min_score:
                continue
            text = f"{title}\n\n{body}" if kind == "posts" else body
            m = rx.search(text)
            if not m:
                continue
            permalink = item.get("permalink") or ""
            created = int(item.get("created_utc") or 0)
            results.append({
                "sub": sub,
                "kind": kind,
                "created_utc": created,
                "date": dt.datetime.fromtimestamp(created, dt.UTC).date().isoformat() if created else "",
                "score": score,
                "num_comments": int(item.get("num_comments") or 0),
                "title": title,
                "body_len": len(body),
                "snippet": make_snippet(text, m, context),
                "permalink": f"https://reddit.com{permalink}" if permalink else "",
            })

    if sort_by == "date":
        results.sort(key=lambda r: r["created_utc"], reverse=True)
    elif sort_by in ("score", "num_comments"):
        results.sort(key=lambda r: r[sort_by], reverse=True)

    return results[:limit]


def list_reddit_sources() -> list[dict]:
    """Inventory of Reddit dumps: sub, kind, file size, last-modified date."""
    out: list[dict] = []
    for p in sorted(REDDIT_DIR.glob("*.jsonl.zst")):
        stem = p.name[: -len(".jsonl.zst")]
        parts = stem.rsplit("_", 1)
        if len(parts) != 2:
            continue
        sub, kind = parts
        st = p.stat()
        out.append({
            "sub": sub,
            "kind": kind,
            "size_mb": round(st.st_size / 1_000_000, 2),
            "modified": dt.datetime.fromtimestamp(st.st_mtime, dt.UTC).date().isoformat(),
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", help="Python regex, case-insensitive by default")
    ap.add_argument("--subs", help="comma-separated subreddit names to restrict")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--min-len", type=int, default=200)
    ap.add_argument("--min-score", type=int, default=0)
    ap.add_argument("--context", type=int, default=120)
    ap.add_argument("--case-sensitive", action="store_true")
    ap.add_argument("--sort-by", choices=["date", "score", "num_comments"], default="date")
    ap.add_argument("--kinds", default="posts", help="posts,comments")
    args = ap.parse_args()

    subs = [s.strip() for s in args.subs.split(",")] if args.subs else None
    kinds = tuple(k.strip() for k in args.kinds.split(",") if k.strip())

    results = search_reddit(
        args.pattern,
        subs=subs,
        kinds=kinds,
        limit=args.limit,
        min_len=args.min_len,
        min_score=args.min_score,
        context=args.context,
        case_sensitive=args.case_sensitive,
        sort_by=args.sort_by,
    )

    sys.stderr.write(f"{len(results)} results shown\n\n")
    for r in results:
        print(f"[{r['date']}] r/{r['sub']} — {r['title'][:100]}")
        print(f"  score={r['score']} comments={r['num_comments']} bodylen={r['body_len']} kind={r['kind']}")
        print(f"  {r['permalink']}")
        print(f"  >> {r['snippet']}")
        print()


if __name__ == "__main__":
    main()
