#!/usr/bin/env python3
"""Resolve a page's reference list against Europe PMC and report mismatches.

Usage: scripts/check_refs.py _rights/potassium.md

For each numbered reference under '## References', searches Europe PMC by title
words, then compares first author, year, journal, volume and first page with the
best match. Prints one line per reference: OK / MISMATCH (fields) / NOT FOUND,
plus the identifiers found (PMID, PMCID, DOI), to feed fetch_source.py.
"""
import json, re, sys, time, urllib.parse, urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def search(q):
    url = f"{EPMC}?query={urllib.parse.quote(q)}&format=json&resultType=core&pageSize=5"
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pr-refcheck"}), timeout=30) as r:
                return json.loads(r.read())["resultList"]["result"]
        except Exception:
            time.sleep(1 + a)
    return []


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower())


def refs(md):
    t = open(md).read()
    m = re.search(r"\n## References\s*\n(.*)", t, re.S)
    out = []
    for line in (m.group(1) if m else "").splitlines():
        mm = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if mm:
            out.append((int(mm.group(1)), mm.group(2)))
    return out


def parse(ref):
    first = re.match(r"([A-Z][A-Za-z'\- ]+?)\s+[A-Z]{1,3}\b", ref)
    year = re.search(r"\b(19|20)\d{2}\b", ref)
    vol = re.search(r"\b(19|20)\d{2};\s*(\d+)", ref)
    page = re.search(r":\s*e?(\d+)", ref)
    parts = re.split(r"\.\s+", ref)
    title = max(parts[1:3] if len(parts) > 2 else parts, key=len) if parts else ref
    return {"first": first.group(1) if first else None, "year": year.group(0) if year else None,
            "vol": vol.group(2) if vol else None, "page": page.group(1) if page else None,
            "title": re.sub(r"[*\[\]]", "", title)}


def main():
    for n, ref in refs(sys.argv[1]):
        p = parse(ref)
        words = " ".join(w for w in re.findall(r"[A-Za-z]{4,}", p["title"])[:10])
        res = search(f'TITLE:({words})') if words else []
        if not res:
            print(f"{n:>3} NOT FOUND   | {ref[:110]}")
            continue
        r = res[0]
        issues = []
        if p["first"] and norm(p["first"]) not in norm(r.get("authorString", "")):
            issues.append(f"author {p['first']} vs {r.get('authorString','')[:40]}")
        if p["year"] and p["year"] != r.get("pubYear"):
            issues.append(f"year {p['year']} vs {r.get('pubYear')}")
        ji = r.get("journalInfo", {})
        if p["vol"] and p["vol"] != str(ji.get("volume", "")):
            issues.append(f"vol {p['vol']} vs {ji.get('volume')}")
        pg = (r.get("pageInfo") or "").split("-")[0].lstrip("e")
        if p["page"] and pg and p["page"] != pg:
            issues.append(f"page {p['page']} vs {r.get('pageInfo')}")
        ids = f"pmid:{r.get('pmid')} pmc:{r.get('pmcid')} doi:{r.get('doi')}"
        status = "OK" if not issues else "CHECK " + "; ".join(issues)
        print(f"{n:>3} {status}\n    found: {r.get('title','')[:100]} | {ji.get('journal',{}).get('isoabbreviation')} {r.get('pubYear')}\n    {ids}")
        time.sleep(0.3)


if __name__ == "__main__":
    main()
