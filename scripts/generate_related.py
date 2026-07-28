#!/usr/bin/env python3
"""Compute the top-4 related pages for every published article by TF-IDF cosine
similarity, and write the result into each article's frontmatter as a `related:`
list of `{title, url}` entries. Rendered by `_layouts/default.html` as the
"Related" aside block. Re-run whenever new articles are added or existing
articles are substantially revised. Manual overrides in a page's `related:`
block will be overwritten by the next run; move them elsewhere if you want
them preserved."""

import math
import re
import sys
from collections import Counter
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = ["_rights", "_definitions", "_editorials", "_critique", "_reports"]
TOP_N = 4
MIN_CHARS = 400

STOPWORDS = set("""
a an the and or but if while of in on at to for with by from as is are was were be been being
this that these those it its it's their they them there here what which who whom whose when where
why how not no nor so than then too very can could may might must shall should will would do does
did done have has had having about above after again against all also although among any because
become becomes been before behind between both do down during each even ever every few first from
further had have he her here hers herself him himself his how i in into is it its itself just
like more most much must my myself never new no not now of off on once only other our ours over
own same she should so some such than that the their theirs them themselves then there they this
those through thus to too under until up upon us used using very was way we well were what when
where whether which while who whom will with within without would you your yours yourself yourselves
one two three four five six seven eight nine ten also however therefore thus hence indeed rather
often already still yet still even ever much many some any all none within between across through
into onto upon toward towards among amongst per via off out up down here there where such kind sort
type case cases sense form forms level levels point points thing things something anything nothing
everything someone anyone everyone way ways time times year years day days moment moments word
words page pages line lines text texts note notes see also cf compare
""".split())

TOKEN_RE = re.compile(r"[a-zà-ÿ][a-zà-ÿ']{2,}")


def tokens(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return [t for t in TOKEN_RE.findall(text) if t not in STOPWORDS and len(t) >= 3]


def url_for(collection: str, path: Path) -> str:
    return f"/{collection.lstrip('_')}/{path.stem}/"


def load_docs() -> list[dict]:
    docs = []
    for coll in COLLECTIONS:
        coll_dir = ROOT / coll
        if not coll_dir.is_dir():
            continue
        for md in sorted(coll_dir.glob("*.md")):
            post = frontmatter.load(md)
            if len(post.content) < MIN_CHARS:
                continue
            if post.get("hidden") or post.get("search_exclude"):
                continue
            docs.append({
                "path": md,
                "title": post.get("title") or md.stem,
                "url": url_for(coll, md),
                "tokens": tokens(post.content),
                "post": post,
            })
    return docs


def tfidf_vectors(docs: list[dict]) -> None:
    n = len(docs)
    df = Counter()
    for d in docs:
        df.update(set(d["tokens"]))
    for d in docs:
        tf = Counter(d["tokens"])
        total = sum(tf.values()) or 1
        vec = {}
        for term, count in tf.items():
            idf = math.log((1 + n) / (1 + df[term])) + 1.0
            vec[term] = (count / total) * idf
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        d["vec"] = {t: v / norm for t, v in vec.items()}


def cosine(a: dict, b: dict) -> float:
    if len(a) > len(b):
        a, b = b, a
    return sum(v * b.get(t, 0.0) for t, v in a.items())


def assign_related(docs: list[dict]) -> None:
    for d in docs:
        scores = []
        for other in docs:
            if other is d:
                continue
            scores.append((cosine(d["vec"], other["vec"]), other))
        scores.sort(key=lambda x: x[0], reverse=True)
        d["post"]["related"] = [
            {"title": o["title"], "url": o["url"]} for _, o in scores[:TOP_N]
        ]
        frontmatter.dump(d["post"], d["path"])


def main() -> int:
    docs = load_docs()
    print(f"Loaded {len(docs)} documents.", file=sys.stderr)
    tfidf_vectors(docs)
    assign_related(docs)
    print(f"Wrote related: on {len(docs)} files.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
