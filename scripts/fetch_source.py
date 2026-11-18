#!/usr/bin/env python3
"""Fetch a publication's metadata and text for the source library.

Usage: scripts/fetch_source.py <slug> pmid:<n> | pmc:<PMCn> | doi:<doi>

Writes:
  kb/sources/texts/<slug>.txt   full text (Europe PMC JATS) or abstract (PubMed), gitignored
  kb/sources/texts/<slug>.json  metadata + access log
  _sources/<slug>.md            skeleton front matter (only if absent)

Access status (Crossref 'updated-by', PubMed publication types) is recorded,
so a retracted or corrected paper is never cited silently.
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
TXT = ROOT / "kb/sources/texts"
SRC = ROOT / "_sources"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
UA = {"User-Agent": "physiological-rights-source-fetcher/0.1"}
log = []


def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
                log.append({"url": url, "status": r.status, "bytes": len(data)})
                return data if binary else data.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            log.append({"url": url, "error": str(e)})
            time.sleep(1.5 * (attempt + 1))
    return None


def strip(x):
    x = re.sub(r"<(table-wrap|fig)\b.*?</\1>", "", x, flags=re.S)
    x = re.sub(r"</(p|title|sec)>", "\n\n", x)
    x = re.sub(r"<[^>]+>", "", x)
    x = re.sub(r"[ \t]+", " ", x)
    return re.sub(r"\n\s*\n+", "\n\n", x).strip()


def epmc_search(q):
    d = get(f"{EPMC}/search?query={urllib.parse.quote(q)}&format=json&resultType=core")
    if not d:
        return None
    res = json.loads(d)["resultList"]["result"]
    return res[0] if res else None


def main():
    slug, ident = sys.argv[1], sys.argv[2]
    kind, val = ident.split(":", 1)
    if kind in ("url", "pdf"):
        return fetch_web(slug, ident.split(":", 1)[1], kind)
    q = {"pmid": f"EXT_ID:{val} AND SRC:MED", "pmc": f"PMCID:{val}", "doi": f'DOI:"{val}"'}[kind]
    rec = epmc_search(q) or {}
    pmid = rec.get("pmid") or (val if kind == "pmid" else None)
    pmcid = rec.get("pmcid") or (val if kind == "pmc" else None)
    doi = rec.get("doi") or (val if kind == "doi" else None)

    authors = [
        " ".join(filter(None, [a.get("firstName"), a.get("lastName")])) or a.get("collectiveName", "")
        for a in rec.get("authorList", {}).get("author", [])
    ]
    ji = rec.get("journalInfo", {})
    meta = {
        "slug": slug,
        "title": (rec.get("title") or "").rstrip("."),
        "authors": authors,
        "container": ji.get("journal", {}).get("title"),
        "year": rec.get("pubYear"),
        "volume": ji.get("volume"),
        "issue": ji.get("issue"),
        "pages": rec.get("pageInfo"),
        "doi": doi, "pmid": pmid, "pmcid": pmcid,
        "pub_types": rec.get("pubTypeList", {}).get("pubType", []),
        "open_access": rec.get("isOpenAccess"),
        "license": rec.get("license"),
        "fetched": date.today().isoformat(),
    }

    text, access = None, None
    if pmcid:
        x = get(f"{EPMC}/{pmcid}/fullTextXML")
        if not x or len(x) < 1500 or "<body>" not in x:
            x = get(f"{EU}/efetch.fcgi?db=pmc&id={pmcid.replace('PMC', '')}&retmode=xml")
        if x and len(x) > 1500 and "<body>" in x:
            body = re.search(r"<body>(.*)</body>", x, re.S)
            abst = re.search(r"<abstract[^>]*>(.*?)</abstract>", x, re.S)
            text = "ABSTRACT\n\n" + strip(abst.group(1) if abst else "") + "\n\nBODY\n\n" + strip(body.group(1) if body else x)
            access = "full text (PMC)"
    if not text and pmid:
        a = get(f"{EU}/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract&retmode=text")
        if a:
            text, access = a.strip(), "abstract (PubMed)"
    if not text and rec.get("abstractText"):
        text, access = strip(rec["abstractText"]), "abstract (Europe PMC)"
    meta["access"] = access

    status = []
    if doi:
        c = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
        if c:
            m = json.loads(c)["message"]
            for u in m.get("updated-by", []) or []:
                status.append(f"{u.get('type')} ({u.get('DOI')})")
            if not meta["pages"]:
                meta["pages"] = m.get("page") or m.get("article-number")
    for t in meta["pub_types"]:
        if re.search(r"retract|correct|erratum|expression of concern", t, re.I):
            status.append(t)
    meta["status"] = "; ".join(status) or f"no retraction or correction found (Crossref, Europe PMC, {meta['fetched']})"
    meta["log"] = log

    TXT.mkdir(parents=True, exist_ok=True)
    (TXT / f"{slug}.txt").write_text(text or "", encoding="utf-8")
    (TXT / f"{slug}.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    SRC.mkdir(exist_ok=True)
    md = SRC / f"{slug}.md"
    if not md.exists():
        def y(v):
            return json.dumps(v, ensure_ascii=False) if v is not None else '""'
        lines = ["---", f"title: {y(meta['title'])}", "authors:"]
        lines += [f"  - {y(a)}" for a in authors] or ["  []"]
        for k in ("container", "year", "volume", "issue", "pages", "doi", "pmid", "pmcid"):
            lines.append(f"{k}: {y(meta[k])}")
        lines += [f"access: {y(access)}", f"status: {y(meta['status'])}", f"verified: {meta['fetched']}",
                  "excerpts:", "  - key: main", '    where: ""', "    text: |", "      TODO", "---", ""]
        md.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: meta[k] for k in ("title", "container", "year", "access", "status")}, ensure_ascii=False))
    print(f"text: {len(text or '')} chars -> {TXT / (slug + '.txt')}")


def fetch_web(slug, url, kind):
    import subprocess, tempfile
    data = get(url, binary=True)
    if data is None:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=40).read()
    if kind == "pdf" or data[:4] == b"%PDF":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(data); f.flush()
            text = subprocess.run(["pdftotext", "-layout", f.name, "-"], capture_output=True, text=True).stdout
        text = re.sub(r"[ \t]+", " ", text)
        access = "full text (PDF)"
    else:
        h = data.decode("utf-8", "replace")
        h = re.sub(r"<(script|style|noscript|svg|nav|header|footer)\b.*?</\1>", "", h, flags=re.S | re.I)
        m = re.search(r"<(article|main)\b.*?</\1>", h, re.S | re.I)
        text = strip(m.group(0) if m else h)
        access = "full text (web page)"
    t = re.search(r"<title>(.*?)</title>", data.decode("utf-8", "replace"), re.S | re.I) if kind == "url" else None
    meta = {"slug": slug, "title": strip(t.group(1)) if t else "", "authors": [], "url": url, "access": access,
            "fetched": date.today().isoformat(), "status": "web source; no retraction registry applies", "log": log}
    for k in ("container", "year", "volume", "issue", "pages", "doi", "pmid", "pmcid"):
        meta.setdefault(k, None)
    TXT.mkdir(parents=True, exist_ok=True)
    (TXT / f"{slug}.txt").write_text(text, encoding="utf-8")
    (TXT / f"{slug}.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"title": meta["title"], "access": access}, ensure_ascii=False))
    print(f"text: {len(text)} chars")


if __name__ == "__main__":
    main()
