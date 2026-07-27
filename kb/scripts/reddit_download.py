"""Download a subreddit's full history (posts + comments) via the Arctic Shift API.

Writes NDJSON to kb/reddit/<subreddit>_<kind>.jsonl.zst as a sequence of
self-contained zstd frames (one frame per page). This makes the file resumable
even after a hard kill mid-write: any trailing corrupted bytes are truncated
on resume and the last known-good cursor is used to continue.

Usage:
    python reddit_download.py <subreddit>
    python reddit_download.py <subreddit> --kinds posts
    python reddit_download.py <subreddit> --resume

Design choices:
- Ascending time sort with `after=<created_utc>` cursor — resumable, deterministic.
- One self-contained zstd frame per API page (100 items) — hard-kill-safe.
- Retries on 429/5xx and on the Arctic Shift 422 "slow down" rate-limit signal.
- Throttle between pages to stay under the API's tolerance.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import zstandard as zstd

from config import KB_ROOT

REDDIT_DIR = KB_ROOT / "reddit"
API_BASE = "https://arctic-shift.photon-reddit.com/api"
USER_AGENT = "physiological-rights-kb/1.0 (research)"
PAGE_LIMIT = 100
BACKOFF_INITIAL = 2.0
BACKOFF_MAX = 60.0
THROTTLE_S = 0.5
EPOCH_ORIGIN = "2005-01-01"


def api_url(kind: str, subreddit: str, after: int) -> str:
    endpoint = "posts/search" if kind == "posts" else "comments/search"
    after_param: str | int = after if after > 0 else EPOCH_ORIGIN
    qs = urllib.parse.urlencode({
        "subreddit": subreddit,
        "limit": PAGE_LIMIT,
        "sort": "asc",
        "after": after_param,
    })
    return f"{API_BASE}/{endpoint}?{qs}"


def fetch_page(url: str) -> list[dict]:
    backoff = BACKOFF_INITIAL
    for attempt in range(12):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                payload = json.load(resp)
                return payload.get("data", [])
        except json.JSONDecodeError as e:
            # Server sometimes returns truncated JSON under load — treat as retriable.
            sys.stderr.write(f"  JSON decode error ({e}), retrying in {backoff:.0f}s...\n")
            time.sleep(backoff)
            backoff = min(backoff * 2, BACKOFF_MAX)
            continue
        except urllib.error.HTTPError as e:
            body = e.read()[:400].decode("utf-8", errors="replace")
            retriable = e.code in (429, 500, 502, 503, 504)
            # Arctic Shift returns 422 with "slow down" body as its rate-limit signal.
            if e.code == 422 and "slow down" in body.lower():
                retriable = True
            if retriable:
                sys.stderr.write(f"  HTTP {e.code} ({body[:80]}), retrying in {backoff:.0f}s...\n")
                time.sleep(backoff)
                backoff = min(backoff * 2, BACKOFF_MAX)
                continue
            sys.stderr.write(f"  HTTP {e.code} on {url}\n  body: {body}\n")
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            sys.stderr.write(f"  network error ({e}), retrying in {backoff:.0f}s...\n")
            time.sleep(backoff)
            backoff = min(backoff * 2, BACKOFF_MAX)
    raise SystemExit(f"gave up after retries: {url}")


def scan_and_truncate(path: Path) -> int:
    """Walk zstd frames from the start; on the first bad/incomplete frame,
    truncate the file to the previous good frame boundary. Return the last
    `created_utc` seen in the surviving prefix, or 0 if the file is empty.
    """
    if not path.exists() or path.stat().st_size == 0:
        return 0

    dctx = zstd.ZstdDecompressor()
    valid_end = 0
    last_cursor = 0
    with path.open("rb") as f:
        remaining = f.read()

    while remaining:
        try:
            dobj = dctx.decompressobj()
            decompressed = dobj.decompress(remaining)
            if not dobj.eof:
                break  # last frame is incomplete
        except zstd.ZstdError:
            break

        for line in decompressed.splitlines():
            if not line.strip():
                continue
            try:
                c = json.loads(line).get("created_utc")
                if c is not None:
                    last_cursor = int(c)
            except (json.JSONDecodeError, ValueError):
                pass

        unused = dobj.unused_data
        valid_end += len(remaining) - len(unused)
        remaining = unused

    if valid_end < path.stat().st_size:
        with path.open("r+b") as f:
            f.truncate(valid_end)
        sys.stderr.write(
            f"  (resume) truncated {path.name} to last complete frame at byte {valid_end}\n"
        )
    return last_cursor


def download_kind(subreddit: str, kind: str, resume: bool) -> tuple[int, int]:
    path = REDDIT_DIR / f"{subreddit}_{kind}.jsonl.zst"
    REDDIT_DIR.mkdir(parents=True, exist_ok=True)

    if resume:
        after = scan_and_truncate(path)
    else:
        after = 0
        if path.exists():
            path.unlink()

    mode = "ab" if (resume and after > 0) else "wb"
    cctx = zstd.ZstdCompressor(level=10)
    items_total = 0
    pages = 0
    started = time.time()

    with path.open(mode) as f:
        while True:
            url = api_url(kind, subreddit, after)
            items = fetch_page(url)
            if not items:
                break
            payload = "".join(
                json.dumps(item, separators=(",", ":")) + "\n" for item in items
            ).encode("utf-8")
            # One self-contained zstd frame per page — resumable on kill.
            f.write(cctx.compress(payload))
            f.flush()
            pages += 1
            items_total += len(items)
            last = items[-1]
            new_after = int(last.get("created_utc", after))
            if new_after <= after:
                # No forward progress — stop to avoid infinite loop.
                break
            after = new_after
            time.sleep(THROTTLE_S)
            if pages % 10 == 0:
                elapsed = time.time() - started
                rate = items_total / elapsed if elapsed else 0
                sys.stderr.write(
                    f"  [{kind}] {items_total:>7} items, "
                    f"{pages:>4} pages, {rate:.0f}/s, "
                    f"cursor={after}\n"
                )
            if len(items) < PAGE_LIMIT:
                break

    size = path.stat().st_size if path.exists() else 0
    return items_total, size


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("subreddit", help="subreddit name (without r/)")
    ap.add_argument(
        "--kinds",
        default="posts,comments",
        help="comma-separated: posts,comments (default: both)",
    )
    ap.add_argument("--resume", action="store_true", help="resume from last cursor")
    args = ap.parse_args()

    kinds = [k.strip() for k in args.kinds.split(",") if k.strip()]
    total_size = 0
    total_items = 0
    for kind in kinds:
        sys.stderr.write(f"=== r/{args.subreddit} {kind} ===\n")
        items, size = download_kind(args.subreddit, kind, args.resume)
        sys.stderr.write(f"  done: {items} items, {size / 1_000_000:.1f} MB\n")
        total_items += items
        total_size += size

    sys.stderr.write(
        f"\nTotal r/{args.subreddit}: {total_items} items, "
        f"{total_size / 1_000_000:.1f} MB compressed\n"
    )


if __name__ == "__main__":
    main()
