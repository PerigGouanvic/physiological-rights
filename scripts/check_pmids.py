#!/usr/bin/env python3
"""Site-wide check: does each PubMed link point to the paper the text describes?

Usage: scripts/check_pmids.py [files...]   (default: all published collections)

For each pubmed.ncbi.nlm.nih.gov/<PMID> link, takes the surrounding text (the
reference line or the 250 characters before the link), fetches the real title
from NCBI, and scores word overlap. Prints suspicious links (low overlap) first.
"""
import glob, json, re, sys, time, urllib.request

STOP = set("the of and in a an for to with on by from at as is are vs its their into".split())


def words(s):
    return {w for w in re.findall(r"[a-z][a-z\-]{3,}", s.lower()) if w not in STOP}


def main():
    files = sys.argv[1:] or [f for c in ("_rights", "_critique", "_editorials", "_definitions", "_did-you-know", "_currents", "_reports", "_resources") for f in glob.glob(f"{c}/*.md")]
    uses = []
    for f in files:
        t = open(f).read()
        for m in re.finditer(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", t):
            line_start = t.rfind("\n", 0, m.start()) + 1
            ctx = t[line_start:m.start()]
            if len(ctx) < 40:
                ctx = t[max(0, m.start() - 250):m.start()]
            uses.append((f, m.group(1), ctx))
    ids = sorted({u[1] for u in uses})
    titles = {}
    for i in range(0, len(ids), 150):
        chunk = ids[i:i + 150]
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(chunk)
        res = json.loads(urllib.request.urlopen(url, timeout=60).read())["result"]
        for u in chunk:
            x = res.get(u, {})
            titles[u] = (x.get("title", ""), x.get("sortfirstauthor", ""), (x.get("pubdate") or "")[:4])
        time.sleep(0.4)
    rows = []
    for f, pid, ctx in uses:
        title, au, yr = titles.get(pid, ("", "", ""))
        tw, cw = words(title), words(ctx)
        ov = len(tw & cw) / max(1, len(tw))
        au_hit = au.split(" ")[0].lower() in ctx.lower() if au else False
        rows.append((ov + (0.3 if au_hit else 0), f, pid, au, yr, title, ctx.strip()[-160:]))
    rows.sort()
    for sc, f, pid, au, yr, title, ctx in rows:
        flag = "SUSPECT" if sc < 0.25 else "ok"
        print(f"{flag:7} {sc:.2f} {f} PMID {pid}\n        real: {au} {yr} | {title[:110]}\n        text: …{ctx}")


if __name__ == "__main__":
    main()
