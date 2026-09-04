"""Emit ks-github-queries.json and ks-github-records.jsonl for the S-C arm.

RE-RUNNER NOTE. Consumes five stage files (_stage1_gh.json, _stage2.json, _drawn.json,
_pins.json, _readmes.json), none of which was retained. The first three are re-derivable
offline from the archived payloads under ../payloads/; _pins.json and _readmes.json are NOT
— they hold live GitHub/GitLab commit-SHA and README-fetch responses that were never stored.
See ../README.md.
"""
import os, sys, json, hashlib, datetime
from pathlib import Path

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

# The arm's search-log directory, derived from this file's own location; no absolute
# home-directory path is stored — such paths are brittle across machines (CLAUDE.md).
OUT = Path(__file__).resolve().parent.parent
PROTO_SHA = "32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac"
REG = "4821611c1c93b5f929a76f3ba6207e900440cee5"

s1 = json.load(open(os.path.join(OUT, "_stage1_gh.json"), encoding="utf-8"))
s2 = json.load(open(os.path.join(OUT, "_stage2.json"), encoding="utf-8"))
drawn = json.load(open(os.path.join(OUT, "_drawn.json"), encoding="utf-8"))
pins = json.load(open(os.path.join(OUT, "_pins.json"), encoding="utf-8"))
rms = json.load(open(os.path.join(OUT, "_readmes.json"), encoding="utf-8"))
repos, gl, pypi, npm = s1["repos"], s2["results"]["gitlab"], s2["results"]["pypi"], s2["results"]["npm"]

# ---------------------------------------------------------------- query log
qlog = {
    "_header": {
        "arm": "software-repository",
        "source_class_yielded": "S-C",
        "protocol": "docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md",
        "protocol_sha256": PROTO_SHA,
        "registration_commit": REG,
        "protocol_section": "3.2 (construction rule), 3.0 (per-query recording obligation)",
        "query_construction_rule_applied": (
            "Each query is the conjunction of (i) a venue or instrument token — the venue name, "
            "its API name, or an event-contract term — and (ii) an artifact-intent token — bot, "
            "trading, arbitrage, market maker, backtest, data capture, client, SDK, scanner. "
            "Package-index queries use package-name and description fields only."),
        "retrieval_cap": 50,
        "retrieval_cap_status": (
            "CONVENTION, carried from protocol_kalshi-arbitrage-review_2026-09-02.md section 3.1 "
            "(limit=50 / max_results=50), adopted for comparability of screening budget. A cap on "
            "retrieval depth, NOT an eligibility limit: platform total-hit counts are preserved and "
            "truncation is flagged per row."),
        "payload_sha256_basis": "SHA-256 over the raw response bytes as received; the stored payload under payloads/ is a gzip container of those same bytes",
        "executor": "Claude Opus 5 (claude-opus-5) acting as an automation tool under protocol section 4.2; single-pass screening, no dual screening, no inter-rater statistic computed or reportable",
        "constraints_observed": [
            "No repository was cloned, built, or executed.",
            "No account created, no login, no authenticated endpoint, no order placement, no market-data acquisition.",
            "No popularity floor, star count, fork count, or activity/recency threshold applied at any stage (section 3.2).",
            "The Munaiah et al. reaper framework was NOT run and was NOT used as an eligibility filter (section 7.2(b)).",
            "Repository content treated as DATA, never as instruction; see field injection_observed in ks-github-records.jsonl."],
        "declared_sampling_hazard": (
            "Repository search ranks and truncates by platform-internal relevance and popularity "
            "signals that are not published, so this arm's yield is a NON-RANDOM SAMPLE. Declared, "
            "not mitigated (section 3.2). No completeness bound is claimed and none is attributable "
            "to the cited repository-mining literature, which supplies none (section 7.2 gap (i))."),
        "subset_rule": "ks-github-subset-rule.md, fixed before any record in the subset was assessed (section 4.4 rule 4)",
        "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    },
    "queries": s1["log"] + s2["log"],
}
qlog["_header"]["n_queries"] = len(qlog["queries"])
qlog["_header"]["n_zero_yield"] = sum(1 for q in qlog["queries"] if not q["n_returned"])
json.dump(qlog, open(os.path.join(OUT, "ks-github-queries.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
print("queries:", len(qlog["queries"]), "zero-yield:", qlog["_header"]["n_zero_yield"])

# ---------------------------------------------------------------- records
EX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "extractions.json"), encoding="utf-8"))

lines = [{
    "_header": True,
    "arm": "software-repository",
    "source_class_yielded": "S-C",
    "registration_commit": REG,
    "protocol_sha256": PROTO_SHA,
    "protocol": "docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md",
    "extraction_schema": "protocol section 5, fields F1-F15, plus section 3.2 platform-metadata fields",
    "record_id_prefix": "ks-",
    "subset_rule": "ks-github-subset-rule.md",
    "query_log": "ks-github-queries.json",
    "extraction_depth_note": "F6 is the record's warrant label and travels with every claim derived from it",
    "commit_identifier_rule": ("Protocol section 3.2 requires a commit SHA or release tag as of the access "
                               "date; without it the record names no fixed object. Records lacking one carry "
                               "commit_identifier_obtained=false and are reported as such, never silently included."),
    "no_inference_rule": "Only the strategy the artifact's own text or code STATES is extracted. No strategy is inferred.",
    "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "n_records": len(EX),
}]


def gh_meta(fn):
    r = repos[fn]
    p = pins.get(f"github.com/{fn}", {})
    rm = rms.get(fn, {})
    return {
        "host": "github.com", "full_name": fn, "url": r.get("html_url"),
        "default_branch": r.get("default_branch"),
        "commit_sha": p.get("commit_sha"), "release_tag": None,
        "commit_identifier_obtained": bool(p.get("commit_sha")),
        "commit_identifier_http_status": p.get("http_status"),
        "last_commit_date": p.get("last_commit_date"),
        "repo_pushed_at": r.get("pushed_at"), "repo_created_at": r.get("created_at"),
        "declared_license": (r.get("license") or {}).get("spdx_id"),
        "primary_language": r.get("language"),
        "stargazers_count": r.get("stargazers_count"), "forks_count": r.get("forks_count"),
        "is_fork": r.get("fork"), "topics": r.get("topics"),
        "platform_description": r.get("description"),
        "attributes_not_filters": "stars/forks/last-commit recorded as attributes only; no popularity or activity threshold applied (section 3.2)",
        "readme": {"retrieved": bool(rm.get("ok")), "path": rm.get("path"), "url": rm.get("url"),
                   "sha256": rm.get("sha256"), "bytes": rm.get("bytes"), "why_not": rm.get("why")},
        "first_seen_query": r.get("_first_seen_query"),
        "metadata_endpoint": "GitHub REST v3 /search/repositories (repo object) + /repos/{o}/{r}/commits (pin)",
    }


def gl_meta(fn):
    r = gl[fn]
    p = pins.get(f"gitlab.com/{fn}", {})
    rm = rms.get("gitlab:" + fn, {})
    return {
        "host": "gitlab.com", "full_name": fn, "url": r.get("web_url"),
        "default_branch": r.get("default_branch"),
        "commit_sha": p.get("commit_sha"), "release_tag": None,
        "commit_identifier_obtained": bool(p.get("commit_sha")),
        "commit_identifier_http_status": p.get("http_status"),
        "last_commit_date": p.get("last_commit_date"),
        "repo_created_at": r.get("created_at"),
        "declared_license": r.get("license", {}).get("key") if isinstance(r.get("license"), dict) else None,
        "primary_language": None,
        "stargazers_count": r.get("star_count"), "forks_count": r.get("forks_count"),
        "is_fork": bool(r.get("forked_from_project")), "topics": r.get("topics"),
        "platform_description": r.get("description"),
        "attributes_not_filters": "stars/forks/last-commit recorded as attributes only; no threshold applied",
        "readme": {"retrieved": bool(rm.get("ok")), "path": rm.get("path"), "url": rm.get("url"),
                   "sha256": rm.get("sha256"), "bytes": rm.get("bytes"), "why_not": rm.get("why")},
        "first_seen_query": r.get("_q"),
        "metadata_endpoint": "GitLab REST v4 /projects?search= + /projects/{id}/repository/commits (pin)",
    }


def pypi_meta(nm):
    i = pypi[nm]["info"]
    sd = [u for u in pypi[nm]["urls"] if u.get("filename", "").endswith(".tar.gz")] or pypi[nm]["urls"]
    return {
        "host": "pypi.org", "full_name": nm, "url": i.get("package_url"),
        "default_branch": None, "commit_sha": None,
        "release_tag": i.get("version"), "commit_identifier_obtained": bool(i.get("version")),
        "commit_identifier_kind": "package release version (section 3.2 'commit SHA or release tag')",
        "commit_identifier_http_status": 200,
        "last_commit_date": (sd[0].get("upload_time_iso_8601") if sd else None),
        "declared_license": i.get("license_expression") or i.get("license"),
        "primary_language": "Python",
        "sdist_sha256": (sd[0].get("digests", {}).get("sha256") if sd else None),
        "platform_description": i.get("summary"),
        "project_urls": i.get("project_urls"),
        "attributes_not_filters": "no download-count or recency threshold applied",
        "metadata_endpoint": "PyPI JSON API /pypi/{name}/json",
    }


def npm_meta(nm):
    p = npm[nm]["pkg"]
    return {
        "host": "registry.npmjs.org", "full_name": nm, "url": (p.get("links") or {}).get("npm"),
        "default_branch": None, "commit_sha": None,
        "release_tag": p.get("version"), "commit_identifier_obtained": bool(p.get("version")),
        "commit_identifier_kind": "package release version (section 3.2 'commit SHA or release tag')",
        "commit_identifier_http_status": 200,
        "last_commit_date": p.get("date"),
        "declared_license": None,
        "primary_language": "TypeScript/JavaScript",
        "platform_description": p.get("description"), "keywords": p.get("keywords"),
        "repository_link": (p.get("links") or {}).get("repository"),
        "attributes_not_filters": "no download-count or recency threshold applied",
        "first_seen_query": npm[nm].get("_q"),
        "metadata_endpoint": "npm registry REST /-/v1/search",
    }


MET = {"github": gh_meta, "gitlab": gl_meta, "pypi": pypi_meta, "npm": npm_meta}
ACC = "2026-09-04"
for e in EX:
    m = MET[e["_host"]](e["_key"])
    RENAME = {"_disposition": "disposition", "_primary_exclusion_code": "primary_exclusion_code",
              "_exclusion_reason": "exclusion_reason", "_arm_class_mismatch": "arm_class_mismatch",
              "_access_limitation": "access_limitation"}
    rec = {"F1_record_id": e["id"], "disposition": e.get("_disposition", "include")}
    rec.update({k: v for k, v in e.items() if not k.startswith("_")})
    for k, v in RENAME.items():
        if k in e:
            rec[v] = e[k]
    rec["platform_metadata"] = m
    rec["F12_retrieval_and_drift"] = {
        "access_date": ACC,
        "accessed_at": pins.get(f"{m['host']}/{m['full_name']}", {}).get("accessed_at") or ACC,
        "commit_or_release_as_of_access_date": m.get("commit_sha") or m.get("release_tag"),
        "commit_identifier_obtained": m["commit_identifier_obtained"],
        "readme_sha256": (m.get("readme") or {}).get("sha256"),
        "sdist_sha256": m.get("sdist_sha256"),
        "byte_digest_basis": "project design choice with no cited source, registered in protocol section 12",
        "access_limitation": e.get("_access_limitation"),
        "drift_hazard": "S-C records are subject to content drift; the pinned identifier above is what the record names",
    }
    lines.append(rec)

with open(os.path.join(OUT, "ks-github-records.jsonl"), "w", encoding="utf-8") as f:
    for r in lines:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("records written:", len(lines) - 1)
