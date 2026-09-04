# -*- coding: utf-8 -*-
"""Build the CSL-JSON store for the kalshi-strategy-multivocal corpus.

Every entry is derived from an arm log on disk. No record is introduced that
appears in no arm log. PYTHONHASHSEED=0 asserted at entry (protocol section 3.0).
"""
import os, sys, json, io, re
assert os.environ.get("PYTHONHASHSEED") == "0", "PYTHONHASHSEED=0 asserted at entry"

LOG = "docs/literature/search_logs/kalshi-strategy-multivocal"


def L(p):
    return json.load(io.open(os.path.join(LOG, p), encoding="utf-8"))


gh = [json.loads(x) for x in io.open(os.path.join(LOG, "ks-github-records.jsonl"),
                                     encoding="utf-8") if x.strip()]
gh = [r for r in gh if not r.get("_header")]
vd = [r for r in L("ks-venue-docs.json") if not r.get("_header")]
lr = [r for r in L("ks-lateral-records.json") if not r.get("_header")]

DUP_LATERAL = {"KSL-C31"}                       # deduped into ks-vr-d06 (same document)
EXCL_VENUE = {"ks-vr-d05": "Y9", "ks-vr-d12": "Y2"}


def iso_date(s):
    if not s:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s))
    if m:
        return [int(m.group(1)), int(m.group(2)), int(m.group(3))]
    m = re.match(r"(\d{4})-(\d{2})$", str(s))
    if m:
        return [int(m.group(1)), int(m.group(2))]
    return None


entries = []

# ------------------------------------------------------------ S-C, software arm
for r in gh:
    if r.get("disposition") != "include":
        continue
    pm = r.get("platform_metadata") or {}
    f12 = r.get("F12_retrieval_and_drift") or {}
    host = pm.get("host")
    full = pm.get("full_name")
    ver = pm.get("commit_sha") or pm.get("release_tag")
    owner = None
    if host in ("github.com", "gitlab.com") and "/" in (full or ""):
        owner = full.split("/")[0]
    digest = f12.get("readme_sha256") or f12.get("sdist_sha256") or "none recorded"
    e = {
        "id": r["F1_record_id"],
        "type": "software",
        "title": full,
        "URL": pm.get("url"),
        "version": ver,
        "publisher": host,
        "accessed": {"date-parts": [iso_date(f12.get("access_date"))]},
        "abstract": pm.get("platform_description") or None,
        "note": (
            "S-C. persistent identifier: none (ADR-0006). "
            "commit-or-release as of access date: {v}. "
            "retrieved-bytes digest (README or sdist; project design choice, protocol "
            "section 12): {d}. extraction depth: {x}. arm log: ks-github-records.jsonl."
        ).format(v=ver, d=digest, x=r.get("F6_extraction_depth")),
        "custom": {
            "record_id": r["F1_record_id"],
            "source_class": "S-C",
            "arm": "software-repository",
            "strategy_class": r.get("F3_strategy_class"),
            "contribution_codes": r.get("F3_contribution_codes"),
            "extraction_depth": r.get("F6_extraction_depth"),
            "venue_of_establishment": r.get("F7_venue_of_establishment"),
            "kalshi_specific": r.get("F8_kalshi_specific"),
            "persistent_identifier": "none",
            "arm_log": LOG + "/ks-github-records.jsonl",
        },
    }
    if owner:
        e["author"] = [{"literal": owner}]
    if pm.get("declared_license"):
        e["custom"]["declared_license"] = pm["declared_license"]
    lc = iso_date(pm.get("last_commit_date"))
    if lc:
        e["issued"] = {"date-parts": [lc]}
    entries.append(e)

# ------------------------------------------------------------ S-D, venue arm
VENUE_TYPE = {"ks-vr-d22": "regulation"}
for r in vd:
    if r["id"] in EXCL_VENUE:
        continue
    url = r.get("url") or ""
    if r["id"] in VENUE_TYPE:
        ctype = VENUE_TYPE[r["id"]]
    elif ".pdf" in url.lower() or "/filings/" in url.lower() or "PressRoom" in url:
        ctype = "report"
    else:
        ctype = "webpage"
    issued = iso_date(r.get("document_date")) or iso_date(r.get("effective_date"))
    e = {
        "id": r["id"],
        "type": ctype,
        "title": r.get("title"),
        "URL": url,
        "publisher": r.get("publisher"),
        "accessed": {"date-parts": [iso_date(r.get("retrieval_date"))]},
        "note": (
            "S-D. persistent identifier: none (ADR-0006). "
            "SHA-256 of retrieved bytes (project design choice, protocol section 12): {s}. "
            "retrieved {rd}, HTTP {st}, {b} bytes. document class: {dc}. "
            "clauses extracted: {nc}. attribution label: {al}. "
            "arm log: ks-venue-docs.json (query {q})."
        ).format(s=r.get("sha256_of_retrieved_bytes"), rd=r.get("retrieval_date"),
                 st=r.get("http_status_at_retrieval"), b=r.get("retrieved_bytes"),
                 dc=r.get("document_class"), nc=r.get("n_clauses"),
                 al=r.get("attribution_label"), q=r.get("query_id")),
        "custom": {
            "record_id": r["id"],
            "source_class": "S-D",
            "arm": "venue-and-regulator",
            "contribution_codes": r.get("contribution_codes"),
            "extraction_depth": r.get("extraction_depth"),
            "clause_ids": [c["clause_id"] for c in (r.get("clauses") or [])],
            "sha256_of_retrieved_bytes": r.get("sha256_of_retrieved_bytes"),
            "effective_date": r.get("effective_date"),
            "extraction_defect": r.get("extraction_defect"),
            "persistent_identifier": "none",
            "arm_log": LOG + "/ks-venue-docs.json",
        },
    }
    if issued:
        e["issued"] = {"date-parts": [issued]}
    else:
        e["custom"]["date_basis"] = (
            "the document states no publication date; the recordable date under N4 is "
            "the access date"
        )
    entries.append(e)

# ------------------------------------------------------------ lateral arm
LTYPE = {"S-C": "software", "S-D": "webpage", "S-E": "post-weblog"}
for r in lr:
    if r["class_id"] in DUP_LATERAL:
        continue
    st = r.get("source_type")
    url = r.get("source_url_or_identifier") or ""
    ctype = LTYPE.get(st, "webpage")
    if st == "S-D" and url.endswith(".pdf"):
        ctype = "report"
    e = {
        "id": r["class_id"],
        "type": ctype,
        "title": r.get("class_name"),
        "URL": url,
        "author": [{"literal": r.get("publisher_or_author")}],
        "accessed": {"date-parts": [iso_date(r.get("accessed_at"))]},
        "abstract": r.get("one_line"),
        "note": (
            "{sc}. persistent identifier: none (ADR-0006). "
            "SHA-256 of retrieved bytes (project design choice, protocol section 12): {s}. "
            "HTTP {h}, {b} bytes, retrieved {rd}. extraction depth: {x}. "
            "TITLE BASIS: the arm log records no document title for this source; the title "
            "field carries this corpus's strategy-class name and the URL is the locator. "
            "arm log: ks-lateral-records.json (query {q})."
        ).format(sc=st, s=r.get("sha256_of_retrieved_bytes"), h=r.get("http_status"),
                 b=r.get("retrieved_bytes"), rd=(r.get("accessed_at") or "")[:10],
                 x=r.get("extraction_depth"), q=r.get("query_log_id")),
        "custom": {
            "record_id": r["class_id"],
            "source_class": st,
            "arm": "lateral-practitioner",
            "strategy_class": [r.get("taxonomy_class")],
            "contribution_codes": r.get("strategy_contribution_codes"),
            "extraction_depth": r.get("extraction_depth"),
            "kalshi_specific": r.get("kalshi_specific_or_transferred"),
            "ordinary_or_lateral": r.get("ordinary_or_lateral"),
            "sha256_of_retrieved_bytes": r.get("sha256_of_retrieved_bytes"),
            "persistent_identifier": "none",
            "arm_log": LOG + "/ks-lateral-records.json",
        },
    }
    d = iso_date(r.get("source_date"))
    if d:
        e["issued"] = {"date-parts": [d]}
    else:
        e["custom"]["date_basis"] = (
            "the source states no date; the recordable date under N4 is the access date"
        )
    entries.append(e)


def prune(o):
    if isinstance(o, dict):
        return {k: prune(v) for k, v in o.items() if v not in (None, "", [], {})}
    if isinstance(o, list):
        return [prune(x) for x in o if x is not None]
    return o


entries = [prune(e) for e in entries]
entries.sort(key=lambda e: e["id"])

sys.path.insert(0, os.path.expanduser("~/.claude/scripts"))
from build_bibliography import (canonical_bytes, sha256_bytes, validate_store,
                                has_persistent_id)

errs = validate_store(entries)
print("entries:", len(entries))
print("validation errors:", len(errs))
for x in errs[:20]:
    print("   ", x)
print("without persistent id:", sum(1 for e in entries if not has_persistent_id(e)))
import collections
print("by arm:", collections.Counter(e["custom"]["arm"] for e in entries))
print("by type:", collections.Counter(e["type"] for e in entries))

data = canonical_bytes(entries)
out = "docs/literature/references_kalshi-strategy-multivocal.json"
with open(out, "wb") as fh:
    fh.write(data)
print("sha256:", sha256_bytes(data))
print("bytes:", len(data))
