# -*- coding: utf-8 -*-
"""Parse ACADEMIC-arm payloads into candidate rows, dedupe per section 4.1, and
difference against the 2026-09-02 branch's disposition index (section 3.1).

NO eligibility determination is made here. Rows carry SIGNALS only.
"""
import os, sys, json, re, glob, hashlib, datetime
assert os.environ.get("PYTHONHASHSEED") == "0", "PYTHONHASHSEED=0 asserted at entry (section 3.0)"

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))  # repo root resolved relative to this file; no absolute home-directory path is stored
LOGDIR = os.path.join(REPO, "docs", "literature", "search_logs", "kalshi-strategy-multivocal")
PAYDIR = os.path.join(LOGDIR, "payloads")

PRIOR = json.load(open(os.path.join(LOGDIR, "ks-prior-identifiers.json"), encoding="utf-8"))["identifiers"]

# ---- frozen vocabularies, section 3.1 -----------------------------------------
INSTRUMENT = [r"event contract", r"event derivative", r"prediction market", r"binary contract",
              r"binary option", r"betting exchange", r"betting market", r"sports ?book",
              r"parimutuel", r"pari-mutuel", r"designated contract market", r"event market"]
VENUE = [r"kalshi", r"polymarket", r"predictit", r"betfair", r"iowa electronic market",
         r"intrade", r"tradesports", r"manifold market", r"metaculus", r"hollywood stock exchange"]
STRATEGY = [r"arbitrage", r"coherence", r"mispric", r"market ?making", r"market maker", r"quoting",
            r"quote", r"inventory", r"spread", r"execution", r"hedg", r"forecast", r"trading strateg",
            r"backtest", r"order book", r"liquidity provision"]

CONTRACT_FAMILY = {
    "sports": [r"sports?", r"nfl", r"nba", r"soccer", r"football", r"baseball", r"tennis", r"horse ?rac"],
    "weather": [r"weather", r"temperature", r"precipitation", r"climate", r"hurricane", r"rainfall"],
    "macro": [r"\bcpi\b", r"inflation", r"federal reserve", r"\bfed\b", r"fomc", r"payroll",
              r"\bgdp\b", r"shutdown", r"macroeconomic", r"interest rate", r"unemployment"],
    "election": [r"election", r"political", r"presidential", r"vote"],
    "llm-agent": [r"large language model", r"\bllm\b", r"language model", r"\bagent", r"neural", r"machine learning"],
}


def hit(pats, text):
    return sorted({p for p in pats if re.search(p, text)})


def norm_doi(d):
    if not d:
        return None
    d = d.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d if d.startswith("10.") else None


def canon(doi, arx):
    """DataCite mints 10.48550/arXiv.<id> for arXiv deposits; the same work therefore
    reaches this arm under two locators. Section 4.1 orders DOI before arXiv id, so the
    two must be reduced to one key before that ordering is applied."""
    if doi and doi.startswith("10.48550/arxiv."):
        arx = arx or ("arxiv:" + doi[len("10.48550/arxiv."):])
        doi = None
    return doi, arx


def norm_arxiv(a):
    if not a:
        return None
    a = a.strip().lower()
    a = re.sub(r"^https?://arxiv\.org/abs/", "", a)
    a = re.sub(r"^arxiv[:/]", "", a)
    a = re.sub(r"v\d+$", "", a)
    return "arxiv:" + a if a else None


def prior_of(doi, arx):
    for k in (doi, arx):
        if k and k in PRIOR:
            return PRIOR[k]
    return None


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()


ROWS = []


def add(qid, title, doi, arx, year, venue, abstract, src_class, extra=None):
    title = strip_tags(title) or ""
    abstract = strip_tags(abstract) or ""
    text = (title + " " + abstract).lower()
    doi = norm_doi(doi)
    arx = norm_arxiv(arx)
    ROWS.append({
        "from_query": qid,
        "title": title,
        "doi": doi,
        "arxiv": arx,
        "year": year,
        "venue_container": venue,
        "source_class_signal": src_class,
        "instrument_hits": hit(INSTRUMENT, text),
        "venue_hits": hit(VENUE, text),
        "strategy_hits": hit(STRATEGY, text),
        "family_hits": {k: hit(v, text) for k, v in CONTRACT_FAMILY.items() if hit(v, text)},
        "has_abstract": bool(abstract),
        "extra": extra or {},
    })


def logs():
    out = []
    for f in sorted(glob.glob(os.path.join(LOGDIR, "ks-*.json"))):
        b = os.path.basename(f)
        if not re.match(r"^ks-(crossref|openalex|arxiv|s2|repec|ssrn)-", b):
            continue  # sibling arms write into the same directory; ACADEMIC arm owns these prefixes only
        out.append(json.load(open(f, encoding="utf-8")))
    return out


for L in logs():
    if L["http_status"] != 200 or not L.get("payload_path"):
        continue
    p = os.path.join(PAYDIR, os.path.basename(L["payload_path"]))
    raw = open(p, "rb").read()
    qid, plat = L["query_id"], L["platform"]
    if plat == "crossref":
        for it in json.loads(raw).get("message", {}).get("items", []):
            ct = (it.get("container-title") or [None])[0]
            ty = it.get("type", "")
            sc = "S-B" if (ty in ("posted-content", "report") or (ct or "").upper().startswith("SSRN")) else "S-A"
            yr = None
            try:
                yr = it["issued"]["date-parts"][0][0]
            except Exception:
                pass
            add(qid, (it.get("title") or [""])[0], it.get("DOI"), None, yr, ct, it.get("abstract"), sc,
                {"crossref_type": ty})
    elif plat == "openalex":
        for it in json.loads(raw).get("results", []):
            inv = it.get("abstract_inverted_index")
            ab = ""
            if inv:
                w = sorted(((i, k) for k, v in inv.items() for i in v))
                ab = " ".join(k for _, k in w)
            loc = (it.get("primary_location") or {}).get("source") or {}
            ty = it.get("type", "")
            sc = "S-B" if ty in ("preprint", "report", "dissertation") else "S-A"
            add(qid, it.get("title") or it.get("display_name"), (it.get("doi") or ""),
                (it.get("ids") or {}).get("arxiv"), it.get("publication_year"), loc.get("display_name"),
                ab, sc, {"openalex_id": it.get("id"), "openalex_type": ty, "cited_by": it.get("cited_by_count")})
    elif plat == "semanticscholar":
        for it in json.loads(raw).get("data", []):
            ex = it.get("externalIds") or {}
            pt = it.get("publicationTypes") or []
            sc = "S-B" if ("JournalArticle" not in pt and (ex.get("ArXiv") or "Preprint" in pt)) else "S-A"
            add(qid, it.get("title"), ex.get("DOI"), ex.get("ArXiv"), it.get("year"), it.get("venue"),
                it.get("abstract"), sc, {"s2_paperId": it.get("paperId"), "citationCount": it.get("citationCount"),
                                         "publicationTypes": pt})
    elif plat == "arxiv":
        txt = raw.decode("utf-8", "replace")
        for m in re.finditer(r"<entry>(.*?)</entry>", txt, re.S):
            e = m.group(1)
            def g(tag):
                mm = re.search(r"<%s>(.*?)</%s>" % (tag, tag), e, re.S)
                return mm.group(1).strip() if mm else None
            aid = g("id") or ""
            arx = re.sub(r"^https?://arxiv\.org/abs/", "", aid)
            doi = g("arxiv:doi") or None
            pub = g("published") or ""
            jr = g("arxiv:journal_ref")
            add(qid, g("title"), doi, arx, pub[:4] if pub else None, jr or "arXiv", g("summary"),
                "S-A" if jr else "S-B", {"arxiv_id": arx, "journal_ref": jr,
                                          "primary_category": (re.search(r'term="([^"]+)"', e).group(1) if re.search(r'term="([^"]+)"', e) else None)})

# ---- deduplication, section 4.1 (DOI -> arXiv -> normalised title) -------------
seen, dedup, dupes = {}, [], 0
TITLE_LEDGER = []
for r in ROWS:
    r["doi"], r["arxiv"] = canon(r["doi"], r["arxiv"])
    key = r["arxiv"] or r["doi"] or ("t:" + re.sub(r"[^a-z0-9]", "", (r["title"] or "").lower()))
    if key in seen:
        dupes += 1
        seen[key]["also_from_query"] = sorted(set(seen[key].get("also_from_query", []) + [r["from_query"]]))
        if not seen[key]["doi"] and r["doi"]:
            seen[key]["doi"] = r["doi"]
        if not seen[key]["arxiv"] and r["arxiv"]:
            seen[key]["arxiv"] = r["arxiv"]
        continue
    seen[key] = r
    dedup.append(r)

# second pass: same-work twins with non-matching identifiers, merged on a
# case- and punctuation-insensitive title match (section 4.1). Every merge is
# itemized in TITLE_LEDGER for hand verification, as that section requires.
by_title, merged = {}, []
for r in dedup:
    t = re.sub(r"[^a-z0-9]", "", (r["title"] or "").lower())
    if len(t) < 25:            # too short to identify a work; never merged on title alone
        merged.append(r)
        continue
    if t in by_title:
        keep = by_title[t]
        TITLE_LEDGER.append({"retained": keep.get("id_tmp"), "retained_title": keep["title"],
                             "retained_locator": keep["doi"] or keep["arxiv"],
                             "dropped_locator": r["doi"] or r["arxiv"],
                             "dropped_from_query": r["from_query"]})
        keep.setdefault("alt_locators", []).append(r["doi"] or r["arxiv"] or "none")
        keep["also_from_query"] = sorted(set(keep.get("also_from_query", []) + [r["from_query"]]))
        if not keep["doi"] and r["doi"]:
            keep["doi"] = r["doi"]
        if not keep["arxiv"] and r["arxiv"]:
            keep["arxiv"] = r["arxiv"]
        dupes += 1
        continue
    by_title[t] = r
    merged.append(r)
dedup = merged

for i, r in enumerate(dedup, 1):
    r["id"] = "ks-a-%03d" % i
    pd = prior_of(r["doi"], r["arxiv"])
    r["prior_disposition"] = pd
    r["novel_vs_2026_09_02"] = pd is None
    # section 4.2 branching rule, stored with the logs and named on every row
    inst = bool(r["instrument_hits"] or r["venue_hits"])
    strat = bool(r["strategy_hits"])
    r["branch"] = "B1-instrument-and-strategy" if (inst and strat) else (
        "B2-instrument-only" if inst else ("B3-strategy-only" if strat else "B4-neither"))

print("raw rows %d  deduped %d  duplicates %d" % (len(ROWS), len(dedup), dupes))
import collections
print("branch:", collections.Counter(r["branch"] for r in dedup).most_common())
print("novel:", sum(1 for r in dedup if r["novel_vs_2026_09_02"]), "prior-dispositioned:", sum(1 for r in dedup if not r["novel_vs_2026_09_02"]))
print("prior codes:", collections.Counter(r["prior_disposition"] for r in dedup if r["prior_disposition"]).most_common())
b1 = [r for r in dedup if r["branch"] == "B1-instrument-and-strategy"]
print("B1 with venue hit:", sum(1 for r in b1 if r["venue_hits"]))

json.dump(TITLE_LEDGER, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "title_merge_ledger.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(dedup, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "candidates.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
