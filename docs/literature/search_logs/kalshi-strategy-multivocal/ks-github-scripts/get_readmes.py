"""Fetch README content for drawn records at the PINNED commit SHA.
Read-only via the platform web view. Nothing is cloned, built, or executed."""
import os, sys, json, time, hashlib, urllib.parse

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# OUT is derived from run_search.py's own file location; no absolute home path is inherited.
from run_search import fetch, now, OUT  # noqa

# The run wrote README bytes to <OUT>/_readmes/; that directory is archived under the name
# below, so a re-run writes back into the archived evidence directory rather than a new one.
RM = os.path.join(OUT, "ks-github-readme-evidence")
os.makedirs(RM, exist_ok=True)

drawn = json.load(open(os.path.join(OUT, "_drawn.json"), encoding="utf-8"))["drawn"]
pins = json.load(open(os.path.join(OUT, "_pins.json"), encoding="utf-8"))

CAND = ["README.md", "readme.md", "README.MD", "Readme.md", "README.rst", "README.txt", "README"]
out = {}

for k in ("gh_sr1", "gh_sr2"):
    for fn in drawn[k]:
        p = pins.get(f"github.com/{fn}", {})
        sha = p.get("commit_sha")
        if not sha:
            out[fn] = {"ok": False, "why": f"no commit identifier (HTTP {p.get('http_status')})"}
            continue
        got = None
        for c in CAND:
            url = f"https://raw.githubusercontent.com/{fn}/{sha}/{c}"
            st, raw = fetch(url, accept="text/plain")
            if st == 200 and raw.strip():
                got = (c, url, raw)
                break
            time.sleep(0.15)
        if got:
            c, url, raw = got
            fnsafe = fn.replace("/", "__") + ".md"
            open(os.path.join(RM, fnsafe), "wb").write(raw)
            out[fn] = {"ok": True, "path": c, "url": url, "bytes": len(raw),
                       "sha256": hashlib.sha256(raw).hexdigest(), "accessed_at": now(),
                       "file": fnsafe}
        else:
            out[fn] = {"ok": False, "why": "no README at pinned SHA among " + ",".join(CAND)}
        print(fn, out[fn].get("ok"), out[fn].get("bytes", out[fn].get("why", "")))
        time.sleep(0.2)

for fn in drawn["gitlab"]:
    p = pins.get(f"gitlab.com/{fn}", {})
    sha = p.get("commit_sha")
    if not sha:
        out["gitlab:" + fn] = {"ok": False, "why": "no commit identifier"}
        continue
    got = None
    for c in CAND:
        url = f"https://gitlab.com/{fn}/-/raw/{sha}/{c}"
        st, raw = fetch(url, accept="text/plain")
        if st == 200 and raw.strip() and b"<!DOCTYPE" not in raw[:200]:
            got = (c, url, raw)
            break
        time.sleep(0.2)
    if got:
        c, url, raw = got
        fnsafe = "gitlab__" + fn.replace("/", "__") + ".md"
        open(os.path.join(RM, fnsafe), "wb").write(raw)
        out["gitlab:" + fn] = {"ok": True, "path": c, "url": url, "bytes": len(raw),
                               "sha256": hashlib.sha256(raw).hexdigest(), "accessed_at": now(), "file": fnsafe}
    else:
        out["gitlab:" + fn] = {"ok": False, "why": "no README at pinned SHA"}
    print("gitlab", fn, out["gitlab:" + fn].get("ok"), out["gitlab:" + fn].get("bytes", ""))
    time.sleep(0.3)

json.dump(out, open(os.path.join(OUT, "_readmes.json"), "w", encoding="utf-8"), indent=1)
print("READMEs retrieved:", sum(1 for v in out.values() if v.get("ok")), "of", len(out))
