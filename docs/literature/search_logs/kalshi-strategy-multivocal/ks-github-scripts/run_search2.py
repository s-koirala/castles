"""Stage 2: GitLab, PyPI, npm, notebook hosts, and the GitHub code-search attempt."""
import os, sys, json, time, hashlib, gzip, datetime, urllib.parse, urllib.request, urllib.error

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# OUT/PAY are derived from run_search.py's own file location; no absolute home path is inherited.
from run_search import fetch, record, log, OUT, PAY, CAP, now  # noqa

results = {"gitlab": {}, "pypi": {}, "npm": {}, "nb": {}}

# ------------------------------------------------- GitHub code search (auth-gated; logged as attempted)
for qid, q in [("ks-ghcode-01", "kalshi arbitrage"), ("ks-ghcode-02", "kalshi market maker")]:
    url = f"https://api.github.com/search/code?q={urllib.parse.quote(q)}&per_page={CAP}"
    st, raw = fetch(url)
    record(qid, q, "GitHub REST v3 /search/code", url, st, raw, 0, None,
           fields="code content; endpoint requires authentication")

# ------------------------------------------------- GitLab
gl = [("ks-gl-01", "kalshi trading"), ("ks-gl-02", "kalshi bot"), ("ks-gl-03", "kalshi arbitrage"),
      ("ks-gl-04", "kalshi client"), ("ks-gl-05", "polymarket arbitrage"),
      ("ks-gl-06", "polymarket bot"), ("ks-gl-07", "prediction market arbitrage"),
      ("ks-gl-08", "prediction market backtest"), ("ks-gl-09", "event contract trading"),
      ("ks-gl-10", "betfair arbitrage")]
for qid, q in gl:
    url = (f"https://gitlab.com/api/v4/projects?search={urllib.parse.quote(q)}"
           f"&per_page={CAP}&order_by=id&sort=desc")
    st, raw = fetch(url, accept="application/json")
    n, tot = 0, None
    if st == 200:
        try:
            d = json.loads(raw)
            n = len(d)
            for p in d:
                results["gitlab"].setdefault(p.get("path_with_namespace"), p)["_q"] = qid
        except Exception:
            pass
    record(qid, q, "GitLab REST v4 /api/v4/projects?search=", url, st, raw, n, tot,
           fields="project name, path, description")
    time.sleep(1.2)

# ------------------------------------------------- PyPI (package-name field only, per §3.2)
pypi_names = ["kalshi", "kalshi-python", "kalshi-api", "kalshi-client", "kalshi-trading",
              "kalshi-sdk", "kalshiclient", "kalshi-arbitrage", "kalshi-bot",
              "py-clob-client", "polymarket", "polymarket-sdk", "predictit",
              "prediction-market", "manifoldpy", "betfairlightweight"]
for i, name in enumerate(pypi_names):
    qid = f"ks-pypi-{i+1:02d}"
    url = f"https://pypi.org/pypi/{urllib.parse.quote(name)}/json"
    st, raw = fetch(url, accept="application/json")
    n = 0
    if st == 200:
        try:
            d = json.loads(raw)
            n = 1
            results["pypi"][name] = {"info": d.get("info", {}),
                                     "urls": [{k: u.get(k) for k in ("filename", "digests", "upload_time_iso_8601")} for u in d.get("urls", [])]}
        except Exception:
            pass
    record(qid, name, "PyPI JSON API /pypi/{name}/json", url, st, raw, n, n,
           fields="package-name field only")
    time.sleep(0.5)

# ------------------------------------------------- npm registry search (name/description/keywords)
npm = [("ks-npm-01", "kalshi client"), ("ks-npm-02", "kalshi trading"), ("ks-npm-03", "kalshi sdk"),
       ("ks-npm-04", "kalshi bot"), ("ks-npm-05", "polymarket sdk"),
       ("ks-npm-06", "polymarket trading"), ("ks-npm-07", "prediction market trading"),
       ("ks-npm-08", "event contract client")]
for qid, q in npm:
    url = f"https://registry.npmjs.org/-/v1/search?text={urllib.parse.quote(q)}&size={CAP}"
    st, raw = fetch(url, accept="application/json")
    n, tot = 0, None
    if st == 200:
        try:
            d = json.loads(raw)
            n = len(d.get("objects", []))
            tot = d.get("total")
            for o in d["objects"]:
                pk = o.get("package", {})
                results["npm"].setdefault(pk.get("name"), {"pkg": pk, "_q": qid})
        except Exception:
            pass
    record(qid, q, "npm registry REST /-/v1/search", url, st, raw, n, tot,
           fields="package name, description, keywords")
    time.sleep(0.8)

# ------------------------------------------------- public notebook hosts
nb = [("ks-nb-01", "kalshi trading", "https://www.kaggle.com/api/v1/kernels/list?search=kalshi+trading&pageSize=50"),
      ("ks-nb-02", "kalshi arbitrage", "https://www.kaggle.com/api/v1/kernels/list?search=kalshi+arbitrage&pageSize=50"),
      ("ks-nb-03", "prediction market backtest", "https://www.kaggle.com/api/v1/kernels/list?search=prediction+market+backtest&pageSize=50")]
for qid, q, url in nb:
    st, raw = fetch(url, accept="application/json")
    n = 0
    if st == 200:
        try:
            d = json.loads(raw)
            n = len(d)
            results["nb"][qid] = d
        except Exception:
            pass
    record(qid, q, "Kaggle public API /api/v1/kernels/list", url, st, raw, n, None,
           fields="kernel title and subtitle")
    time.sleep(1.0)

with open(os.path.join(OUT, "_stage2.json"), "w", encoding="utf-8") as f:
    json.dump({"log": log, "results": results}, f, indent=1, default=str)
print("gitlab", len(results["gitlab"]), "pypi", len(results["pypi"]), "npm", len(results["npm"]))
