"""S-C (software-repository) arm executor for protocol_kalshi-strategy-multivocal_2026-09-04.md
Registration commit 4821611c1c93b5f929a76f3ba6207e900440cee5.
Query construction rule (frozen §3.2): venue/instrument token AND artifact-intent token.
Logs EVERY query including zero-yield (§3.0). Does not clone, build, or execute anything.
"""
import os, sys, json, time, hashlib, gzip, datetime, urllib.parse, urllib.request, urllib.error
from pathlib import Path

# os.environ.setdefault() here would be a no-op: hash randomisation is fixed at interpreter
# start-up, so setting the variable from inside the running process changes nothing. Assert
# the caller set it, exactly as the ACADEMIC-arm scripts do.
assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

# The arm's search-log directory, derived from this file's own location: this script lives in
# <search-log-dir>/ks-github-scripts/, so the parent of its parent is that directory. No absolute
# home-directory path is stored — such paths are brittle across machines (CLAUDE.md).
OUT = Path(__file__).resolve().parent.parent
PAY = os.path.join(OUT, "payloads")
os.makedirs(PAY, exist_ok=True)

UA = "castles-research-protocol-ks-multivocal (+https://github.com/s-koirala/castles)"
CAP = 50  # per-response retrieval cap, CONVENTION carried from predecessor protocol §3.1 (limit=50)

log = []


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def fetch(url, accept="application/vnd.github+json"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return None, str(e).encode()


def record(qid, verbatim, endpoint, url, status, raw, n_ret, n_tot, retry_of=None,
           trunc=None, fields=None, store=True):
    sha = hashlib.sha256(raw).hexdigest()
    ppath = None
    if store and status == 200:
        fn = f"{qid}.json.gz"
        with gzip.open(os.path.join(PAY, fn), "wb") as f:
            f.write(raw)
        ppath = f"docs/literature/search_logs/kalshi-strategy-multivocal/payloads/{fn}"
    e = {
        "query_id": qid,
        "query_verbatim": verbatim,
        "endpoint": endpoint,
        "request_url": url,
        "executed_at": now(),
        "http_status": status,
        "n_returned": n_ret,
        "n_total_reported": n_tot,
        "payload_sha256": sha,
        "payload_path": ppath,
        "retry_of": retry_of,
        "retrieval_cap": CAP,
        "truncated": trunc,
        "search_fields": fields,
    }
    log.append(e)
    print(f"{qid:16s} {str(status):5s} n={n_ret} tot={n_tot} :: {verbatim}", flush=True)
    return e


# ---------------------------------------------------------------- GitHub repo search
GH_REPO = "https://api.github.com/search/repositories"
gh_queries = [
    ("ks-gh-01", "kalshi trading"),
    ("ks-gh-02", "kalshi bot"),
    ("ks-gh-03", "kalshi arbitrage"),
    ("ks-gh-04", "kalshi market maker"),
    ("ks-gh-05", "kalshi backtest"),
    ("ks-gh-06", "kalshi client"),
    ("ks-gh-07", "kalshi sdk"),
    ("ks-gh-08", "kalshi data capture"),
    ("ks-gh-09", "kalshi scanner"),
    ("ks-gh-10", "kalshi api trading"),
    ("ks-gh-11", "polymarket arbitrage"),
    ("ks-gh-12", "polymarket bot"),
    ("ks-gh-13", "polymarket market maker"),
    ("ks-gh-14", "predictit trading"),
    ("ks-gh-15", "prediction market arbitrage"),
    ("ks-gh-16", "prediction market backtest"),
    ("ks-gh-17", "event contract trading"),
    ("ks-gh-18", "manifold markets bot"),
    ("ks-gh-19", "betfair arbitrage"),
    ("ks-gh-20", "prediction market market maker"),
]

repos = {}


def harvest_gh(raw, qid):
    try:
        d = json.loads(raw)
    except Exception:
        return 0, None
    items = d.get("items", [])
    for it in items:
        fn = it.get("full_name")
        if fn and fn not in repos:
            it["_first_seen_query"] = qid
            repos[fn] = it
        elif fn:
            repos[fn].setdefault("_also_query", []).append(qid)
    return len(items), d.get("total_count")


def run_github():
    for i, (qid, q) in enumerate(gh_queries):
        url = f"{GH_REPO}?q={urllib.parse.quote(q)}&per_page={CAP}"
        st, raw = fetch(url)
        if st == 403 or st == 429:
            time.sleep(65)
            st, raw = fetch(url)
            n, tot = harvest_gh(raw, qid + "-b") if st == 200 else (0, None)
            record(qid + "-b", q, "GitHub REST v3 /search/repositories", url, st, raw, n, tot,
                   retry_of=qid, trunc=(tot is not None and tot > CAP),
                   fields="platform default for repository search")
            continue
        n, tot = harvest_gh(raw, qid) if st == 200 else (0, None)
        record(qid, q, "GitHub REST v3 /search/repositories", url, st, raw, n, tot,
               trunc=(tot is not None and tot > CAP),
               fields="platform default for repository search")
        time.sleep(6.5)  # unauthenticated search limit is 10 req/min


if __name__ == "__main__":
    run_github()
    with open(os.path.join(OUT, "_stage1_gh.json"), "w", encoding="utf-8") as f:
        json.dump({"log": log, "repos": repos}, f, indent=1)
    print("distinct repos:", len(repos))
