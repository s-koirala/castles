"""Draw the SR-1..SR-5 subset and pin each record to a commit SHA / release tag.
Reads only. Does not clone, build, or execute anything."""
import os, sys, json, re, time, hashlib, gzip, datetime, urllib.parse, urllib.request, urllib.error

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# OUT/PAY are derived from run_search.py's own file location; no absolute home path is inherited.
from run_search import fetch, now, OUT, PAY  # noqa

KAL = re.compile(r'kalshi', re.I)
OTH = re.compile(r'polymarket|predictit|manifold|betfair|smarkets|prediction[ -]?market|event[ -]contract|betting exchange', re.I)
INT = re.compile(r'\bbot\b|trading|trader|arbitrage|\barb\b|market[ -]?mak|backtest|data capture|capture|\bclient\b|\bsdk\b|scanner|\bscan\b|quant|strateg', re.I)


def key(host, fn):
    return hashlib.sha256(f"{host}/{fn}".encode()).hexdigest()


gh = json.load(open(os.path.join(OUT, "_stage1_gh.json"), encoding="utf-8"))["repos"]
s2 = json.load(open(os.path.join(OUT, "_stage2.json"), encoding="utf-8"))["results"]

strat = {"gh_sr1": [], "gh_sr2": [], "gitlab": [], "pypi": [], "npm": []}

for fn, r in gh.items():
    txt = ' '.join([fn, r.get('description') or '', ' '.join(r.get('topics') or [])])
    if not INT.search(txt):
        continue
    if KAL.search(txt):
        strat["gh_sr1"].append((key("github.com", fn), fn, r))
    elif OTH.search(txt):
        strat["gh_sr2"].append((key("github.com", fn), fn, r))

for fn, r in s2["gitlab"].items():
    txt = ' '.join([fn, r.get('description') or ''])
    if (KAL.search(txt) or OTH.search(txt)) and INT.search(txt):
        strat["gitlab"].append((key("gitlab.com", fn), fn, r))

for nm, r in s2["pypi"].items():
    txt = ' '.join([nm, r['info'].get('summary') or ''])
    if KAL.search(txt) or OTH.search(txt):
        strat["pypi"].append((key("pypi.org", nm), nm, r))

for nm, r in s2["npm"].items():
    p = r['pkg']
    txt = ' '.join([nm, p.get('description') or '', ' '.join(p.get('keywords') or [])])
    if (KAL.search(txt) or OTH.search(txt)) and INT.search(txt):
        strat["npm"].append((key("registry.npmjs.org", nm), nm, r))

ALLOC = {"gh_sr1": 24, "gh_sr2": 5, "gitlab": 3, "pypi": 6, "npm": 5}
drawn, gone = {}, {}
for k, v in strat.items():
    v.sort(key=lambda x: x[0])
    drawn[k] = v[:ALLOC[k]]
    gone[k] = len(v)
    print(f"{k:8s} stratum={len(v):4d} drawn={len(drawn[k])}")

json.dump({"stratum_sizes": gone,
           "drawn": {k: [x[1] for x in v] for k, v in drawn.items()},
           "sr4_keys": {k: {x[1]: x[0] for x in v} for k, v in drawn.items()},
           "universe": {k: [x[1] for x in strat[k]] for k in strat}},
          open(os.path.join(OUT, "_drawn.json"), "w", encoding="utf-8"), indent=1)

# ---------- pin GitHub / GitLab drawn records to a commit SHA ----------
pins = {}
for k in ("gh_sr1", "gh_sr2"):
    for _, fn, r in drawn[k]:
        br = r.get("default_branch") or "main"
        url = f"https://api.github.com/repos/{fn}/commits?sha={urllib.parse.quote(br)}&per_page=1"
        st, raw = fetch(url)
        sha = date = None
        if st == 200:
            try:
                c = json.loads(raw)[0]
                sha = c["sha"]
                date = c["commit"]["committer"]["date"]
            except Exception:
                pass
        pins[f"github.com/{fn}"] = {"http_status": st, "endpoint": "GitHub REST v3 /repos/{o}/{r}/commits",
                                    "request_url": url, "commit_sha": sha, "last_commit_date": date,
                                    "accessed_at": now(), "payload_sha256": hashlib.sha256(raw).hexdigest()}
        print("pin", fn, st, (sha or "")[:12], date)
        time.sleep(0.4)

for _, fn, r in drawn["gitlab"]:
    pid = r.get("id")
    url = f"https://gitlab.com/api/v4/projects/{pid}/repository/commits?per_page=1"
    st, raw = fetch(url, accept="application/json")
    sha = date = None
    if st == 200:
        try:
            c = json.loads(raw)[0]
            sha = c["id"]
            date = c["committed_date"]
        except Exception:
            pass
    pins[f"gitlab.com/{fn}"] = {"http_status": st, "endpoint": "GitLab REST v4 /projects/{id}/repository/commits",
                                "request_url": url, "commit_sha": sha, "last_commit_date": date,
                                "accessed_at": now(), "payload_sha256": hashlib.sha256(raw).hexdigest()}
    print("pin", fn, st, (sha or "")[:12], date)
    time.sleep(0.6)

json.dump(pins, open(os.path.join(OUT, "_pins.json"), "w", encoding="utf-8"), indent=1)
print("pinned:", sum(1 for v in pins.values() if v["commit_sha"]), "of", len(pins))
