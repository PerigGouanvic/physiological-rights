#!/usr/bin/env python3
"""Build _sources/<sid>.md from a spec + the text deposited by fetch_source.py.

Usage: scripts/make_source.py _audit/source-specs/<sid>.json [...]

Spec keys: sid, short, url (best reading link, optional), container (override),
license (override), note (commentary, optional),
excerpts: [{key, where, anchor | "abstract", until (optional anchor of last paragraph)}].

Every excerpt is copied verbatim from the deposited text, located by an anchor
phrase; the script fails if an anchor is not found, so nothing is typed by hand.
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TXT = ROOT / "kb/sources/texts"
OUT = ROOT / "_sources"

SPACES = {c: " " for c in (0xa0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200a, 0x202f, 0x205f)}
META_RE = re.compile(r"^(\d+\. |Collaborators|Author information|DOI:|PMID:|PMCID:|Comment in|Erratum in|Copyright|©|\(\d+\)|Conflict of interest)")


def paragraphs(text):
    return [html.unescape(re.sub(r"\s*\n\s*", " ", p)).translate(SPACES).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def pubmed_abstract(text):
    ps = paragraphs(text)
    # PubMed text layout: citation, title, authors, affiliations, abstract..., DOI/PMID
    body = [p for p in ps[3:] if not META_RE.match(p)]
    return [p for p in body if len(p) > 200 or re.match(r"^[A-Z /]+:", p)]


def find(ps, anchor):
    norm = lambda s: re.sub(r"\s+", " ", s)
    for i, p in enumerate(ps):
        if norm(anchor) in norm(p):
            return i
    raise SystemExit(f"anchor not found: {anchor!r}")


def q(v):
    return json.dumps(v, ensure_ascii=False)


def build(spec_path):
    spec = json.loads(Path(spec_path).read_text())
    sid = spec["sid"]
    meta = json.loads((TXT / f"{sid}.json").read_text())
    text = (TXT / f"{sid}.txt").read_text()
    full = "BODY" in text[:20000] or meta.get("access", "").startswith("full")
    ps = paragraphs(text)
    lines = ["---", f"sid: {q(sid)}", f"title: {q(spec.get('title') or meta['title'])}", f"short: {q(spec['short'])}", "authors:"]
    lines += [f"  - {q(a)}" for a in (spec.get("authors") or meta["authors"])]
    for k in ("container", "year", "volume", "issue", "pages", "doi", "pmid", "pmcid"):
        v = spec.get(k, meta.get(k))
        if v:
            lines.append(f"{k}: {q(str(v))}")
    for k in ("url", "license", "note"):
        v = spec.get(k, meta.get(k))
        if v:
            lines.append(f"{k}: {q(v)}")
    lines += [f"access: {q(spec.get('access') or meta['access'])}", f"status: {q(meta['status'])}", f"verified: {q(meta['fetched'])}", "excerpts:"]
    for ex in spec.get("excerpts") or []:
        if ex.get("anchor") == "abstract":
            chunk = pubmed_abstract(text) if not full else ps[1:find(ps, "BODY")]
        else:
            i = find(ps, ex["anchor"])
            j = find(ps, ex["until"]) if ex.get("until") else i
            chunk = ps[i:j + 1]
            if ex.get("from"):
                chunk[0] = chunk[0][chunk[0].index(ex["from"]):]
            if ex.get("to"):
                chunk[-1] = chunk[-1][:chunk[-1].index(ex["to"]) + len(ex["to"])]
        for m in ex.get("marks", []):
            if not any(m in p for p in chunk):
                raise SystemExit(f"mark not in excerpt {ex['key']}: {m!r}")
        lines += [f"  - key: {q(ex['key'])}", f"    where: {q(ex['where'])}"]
        if ex.get("marks"):
            lines += ["    marks:"] + [f"      - {q(m)}" for m in ex["marks"]]
        lines += ["    paras:"]
        lines += [f"      - {q(p)}" for p in chunk]
    lines += ["---", ""]
    OUT.mkdir(exist_ok=True)
    (OUT / f"{sid}.md").write_text("\n".join(lines), encoding="utf-8")
    n = sum(1 for l in lines if l.startswith("      - "))
    print(f"{sid}: {len(spec.get('excerpts') or [])} excerpts, {n} paragraphs")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        build(p)
