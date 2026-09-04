# -*- coding: utf-8 -*-
"""ACADEMIC arm executor for protocol_kalshi-strategy-multivocal_2026-09-04.md.

Executes the frozen-rule query table, stores raw response bytes, and writes one
section-3.0 log entry per query INCLUDING zero-yield and failed queries.
"""
import os, sys, json, time, hashlib, datetime, urllib.request, urllib.error

assert os.environ.get("PYTHONHASHSEED") == "0", "PYTHONHASHSEED=0 must be asserted at entry (section 3.0)"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from queries import QUERIES

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))  # repo root resolved relative to this file; no absolute home-directory path is stored
LOGDIR = os.path.join(REPO, "docs", "literature", "search_logs", "kalshi-strategy-multivocal")
PAYDIR = os.path.join(LOGDIR, "payloads")
RELLOG = "docs/literature/search_logs/kalshi-strategy-multivocal"
UA = "castles-research/1.0 (+https://github.com/s-koirala; mailto:238704148+s-koirala@users.noreply.github.com)"

REGISTRATION_COMMIT = "4821611c1c93b5f929a76f3ba6207e900440cee5"
PROTOCOL_SHA256 = "32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac"

PAUSE = {"crossref": 1.5, "openalex": 3.0, "arxiv": 3.5, "semanticscholar": 4.0, "repec": 2.5, "ssrn": 1.0}
RETRY_WAITS = {"openalex": [45, 60, 90], "semanticscholar": [20, 40, 75], "crossref": [10, 20],
               "arxiv": [10, 20], "repec": [10, 20], "ssrn": []}


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def ext_for(platform):
    return {"arxiv": "xml", "repec": "html", "ssrn": "html"}.get(platform, "json")


def count_records(platform, raw):
    """(n_returned, n_total_reported, truncated_flag). Never guesses."""
    try:
        if platform == "crossref":
            d = json.loads(raw)
            m = d.get("message", {})
            return len(m.get("items", [])), m.get("total-results"), None
        if platform == "openalex":
            d = json.loads(raw)
            return len(d.get("results", [])), d.get("meta", {}).get("count"), None
        if platform == "semanticscholar":
            d = json.loads(raw)
            return len(d.get("data", [])), d.get("total"), None
        if platform == "arxiv":
            import re
            txt = raw.decode("utf-8", "replace")
            n = len(re.findall(r"<entry>", txt))
            tot = re.search(r"opensearch:totalResults[^>]*>(\d+)<", txt)
            return n, int(tot.group(1)) if tot else None, None
        if platform == "repec":
            import re
            txt = raw.decode("utf-8", "replace")
            n = len(re.findall(r'href="https?://(?:ideas|econpapers)\.repec\.org/[aphrb]/', txt))
            tot = re.search(r"([\d,]+)\s+(?:results|papers|matches)", txt, re.I)
            return n, int(tot.group(1).replace(",", "")) if tot else None, None
    except Exception as e:
        return None, None, "count-parse-failure: %s" % type(e).__name__
    return None, None, None


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    r = urllib.request.urlopen(req, timeout=90)
    return r.status, r.read(), dict(r.headers)


def execute(q, attempt=0, retry_of=None):
    qid = q["qid"] if attempt == 0 else "%s-%s" % (q["qid"], "bcd"[attempt - 1])
    plat = q["platform"]
    executed_at = now()
    raw, status, err = b"", None, None
    try:
        status, raw, _ = fetch(q["url"])
    except urllib.error.HTTPError as e:
        status = e.code
        try:
            raw = e.read()
        except Exception:
            raw = b""
        err = "HTTPError %s" % e.code
    except Exception as e:
        status = "client-error"
        err = "%s: %s" % (type(e).__name__, str(e)[:300])

    n_ret, n_tot, cerr = count_records(plat, raw) if raw and status == 200 else (0 if status == 200 else None, None, None)
    if status != 200:
        n_ret = 0

    paypath = None
    if raw:
        fn = "%s.%s" % (qid, ext_for(plat))
        with open(os.path.join(PAYDIR, fn), "wb") as f:
            f.write(raw)
        paypath = "%s/payloads/%s" % (RELLOG, fn)

    truncated = None
    if isinstance(n_tot, int) and isinstance(n_ret, int):
        truncated = n_tot > n_ret

    entry = {
        "query_id": qid,
        "arm": "academic",
        "protocol": "docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md",
        "protocol_sha256": PROTOCOL_SHA256,
        "registration_commit": REGISTRATION_COMMIT,
        "query_verbatim": q["url"],
        "endpoint": q["url"].split("?")[0],
        "platform": plat,
        "executed_at": executed_at,
        "http_status": status,
        "client_error": err,
        "n_returned": n_ret,
        "n_total_reported": n_tot,
        "truncated_by_cap": truncated,
        "retrieval_cap_in_force": q["cap"],
        "payload_sha256": hashlib.sha256(raw).hexdigest() if raw else None,
        "payload_bytes": len(raw),
        "payload_path": paypath,
        "retry_of": retry_of,
        "construction_section_3_1": {
            "instrument_term": q["instrument"],
            "strategy_term": q["strategy"],
            "venue_narrowing": q.get("venue"),
            "date_restriction": "none",
            "language_restriction": "none",
            "field_restriction": {
                "crossref": "query.bibliographic (bibliographic metadata field; Crossref exposes no combined title-and-abstract field)",
                "openalex": "filter=title_and_abstract.search",
                "arxiv": "abs: (abstract field; arXiv's title-and-abstract-equivalent restriction)",
                "semanticscholar": "relevance search over title and abstract; the platform offers no explicit field-restriction parameter",
                "repec": "IDEAS htsearch default index; the platform offers no field-restriction parameter",
                "ssrn": "keyword field",
            }[plat],
            "subject_or_category_narrowing": "none",
        },
        "target_stratum": q["stratum"],
        "note": q.get("note"),
        "count_parse_error": cerr,
    }
    with open(os.path.join(LOGDIR, "%s.json" % qid), "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return entry


def main():
    results = []
    for q in QUERIES:
        e = execute(q)
        results.append(e)
        print("%-22s %-16s status=%-14s n=%-5s total=%s" % (e["query_id"], q["platform"], e["http_status"], e["n_returned"], e["n_total_reported"]))
        sys.stdout.flush()
        # retry chain on transient failure (429/5xx/client error), per predecessor -b/-c convention
        if e["http_status"] != 200:
            for i, w in enumerate(RETRY_WAITS.get(q["platform"], [])):
                time.sleep(w)
                r = execute(q, attempt=i + 1, retry_of=results[-1]["query_id"])
                results.append(r)
                print("  retry %-18s status=%-14s n=%-5s total=%s" % (r["query_id"], r["http_status"], r["n_returned"], r["n_total_reported"]))
                sys.stdout.flush()
                if r["http_status"] == 200:
                    break
        time.sleep(PAUSE.get(q["platform"], 2.0))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_summary.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    ok = [r for r in results if r["http_status"] == 200]
    print("\nexecuted=%d ok=%d records=%d" % (len(results), len(ok), sum(r["n_returned"] or 0 for r in ok)))


if __name__ == "__main__":
    main()
