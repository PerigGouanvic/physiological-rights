#!/usr/bin/env python3
"""Match each footnote use in a page to the best supporting passage of its source.

Usage: scripts/auto_cite.py _rights/omega-3.md [--fetch]

1. Reads kramdown footnotes ([^n] uses, [^n]: URL definitions).
2. Maps each URL to an identifier (PubMed, PMC, DOI, or plain web/PDF) and,
   with --fetch, deposits the text via fetch_source.py (skips ones already there).
3. For each use, takes the claim (the sentence ending at the marker), scores every
   paragraph of the source by shared numbers (weighted) and content words, and
   reports the best paragraph and best sentence.

Writes _audit/verification/<page>-matches.md, a review table: claim, source,
score, best sentence. Nothing in the page is changed. Low scores flag claims
the source may not support; every row is to be read by a human or by Claude.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TXT = ROOT / "kb/sources/texts"
sys.path.insert(0, str(ROOT / "scripts"))
import make_source as ms  # noqa: E402

STOP = set("""a an the and or of to in on for with by from at as is are was were be been being this that these those it its
their there which who whom what when where than then so such not no but also into over under about after before between
more most less many much can could may might will would should has have had do does did per each other only very
""".split())


def ident_for(url):
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url) or re.search(r"pubmed\.gov/(\d+)", url)
    if m:
        return f"pmid:{m.group(1)}"
    m = re.search(r"(PMC\d+)", url)
    if m:
        return f"pmc:{m.group(1)}"
    m = re.search(r"doi\.org/(10\.[^\s?#]+)", url) or re.search(r"/doi/(?:full/|abs/|pdf/)?(10\.[^\s?#]+)", url)
    if m:
        return f"doi:{m.group(1).rstrip('/')}"
    m = re.search(r"sciencedirect\.com/science/article/(?:abs/)?pii/(\w+)", url)
    if m:
        return f"pii:{m.group(1)}"
    if url.lower().endswith(".pdf"):
        return f"pdf:{url}"
    return f"url:{url}"


def resolve_pii(pii):
    import urllib.request
    try:
        q = f"https://api.crossref.org/works?filter=alternative-id:{pii}&rows=1"
        with urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": "pr-autocite"}), timeout=30) as r:
            items = json.loads(r.read())["message"]["items"]
        return f"doi:{items[0]['DOI']}" if items else None
    except Exception:
        return None


def words(s):
    return {w for w in re.findall(r"[a-z][a-z\-]{2,}", s.lower()) if w not in STOP}


def numbers(s):
    return {n.replace(",", "").replace(" ", "") for n in re.findall(r"\d[\d,\s]*(?:\.\d+)?", s) if len(n.strip()) > 0}


def sentences(p):
    return re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", p)


def score(claim, text):
    cn, tn = numbers(claim) - {"1", "2", "3"}, numbers(text)
    cw, tw = words(claim), words(text)
    return 3 * len(cn & tn) + len(cw & tw) / (1 + 0.15 * len(cw))


def main():
    page = Path(sys.argv[1])
    fetch = "--fetch" in sys.argv
    src = page.read_text()
    defs = dict(re.findall(r"^\[\^(\w+)\]:\s*(\S+)", src, re.M))
    body = re.sub(r"^\[\^\w+\]:.*$", "", src, flags=re.M)
    slug = page.stem
    sids = {}
    for n, url in defs.items():
        ident = ident_for(url)
        if ident.startswith("pii:"):
            ident = resolve_pii(ident[4:]) or f"url:{url}"
        sid = f"{slug}-ref{n}"
        sids[n] = (sid, ident, url)
        if fetch and not (TXT / f"{sid}.txt").exists():
            r = subprocess.run([sys.executable, str(ROOT / "scripts/fetch_source.py"), sid, ident], capture_output=True, text=True, timeout=180)
            (ROOT / "_sources" / f"{sid}.md").unlink(missing_ok=True)
            print(f"[^{n}] {ident[:70]} -> {(r.stdout or r.stderr).strip().splitlines()[0][:110] if (r.stdout or r.stderr).strip() else 'no output'}")
    rows = []
    for m in re.finditer(r"\[\^(\w+)\]", body):
        n = m.group(1)
        if n not in sids:
            continue
        before = body[:m.start()]
        before = re.sub(r"(\[\^\w+\])+$", "", before)
        cl = re.split(r"(?<=[.!?:])\s+|\n\n|\n[-|>#]", before)[-1][-400:]
        if len(cl) < 40:
            cl = before[-400:]
        sid, ident, url = sids[n]
        f = TXT / f"{sid}.txt"
        text = f.read_text() if f.exists() else ""
        ps = [p for p in ms.paragraphs(text) if len(p) > 80] if text else []
        best = max(((score(cl, p), i) for i, p in enumerate(ps)), default=(0, -1))
        bsent = ""
        if best[1] >= 0:
            bsent = max(sentences(ps[best[1]]), key=lambda s_: score(cl, s_))
        rows.append({"n": n, "sid": sid, "ident": ident, "claim": cl.strip(), "score": round(best[0], 2),
                     "para": best[1], "sentence": bsent, "chars": len(text)})
    out = ROOT / "_audit/verification" / f"{slug}-matches.md"
    lines = [f"# Appariements automatiques : {page}", "", "Score = 3 x chiffres partagés + recouvrement lexical. À relire ligne par ligne.", ""]
    for r in rows:
        lines += [f"## [^{r['n']}] {r['sid']} ({r['ident'][:60]}) score {r['score']} texte {r['chars']} c.",
                  f"- **Affirmation :** {r['claim']}", f"- **Meilleure phrase (¶{r['para']}) :** {r['sentence'][:600]}", ""]
    out.write_text("\n".join(lines))
    json.dump(rows, open(ROOT / "_audit/verification" / f"{slug}-matches.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(rows)} uses -> {out}")


if __name__ == "__main__":
    main()
