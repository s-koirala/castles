"""F4 verification: every quote must be reproducible from the retrieved bytes.

RE-RUNNER NOTE. This script needs three inputs. The README bytes ARE archived (see RM below).
The two stage files it reads for the platform-description half of each source string
(_stage1_gh.json, _stage2.json) were NOT retained; both are re-derivable offline from the
archived payloads under ../payloads/ by re-running run_search.py's harvest_gh() and
run_search2.py's per-platform harvest over those bytes. See ../README.md.
"""
import os, json, sys
from pathlib import Path

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

# The arm's search-log directory, derived from this file's own location; no absolute
# home-directory path is stored — such paths are brittle across machines (CLAUDE.md).
OUT = Path(__file__).resolve().parent.parent
# The run wrote README bytes to <OUT>/_readmes/; they are archived under the name below.
RM = os.path.join(OUT, "ks-github-readme-evidence")
EX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "extractions.json"), encoding="utf-8"))
s1 = json.load(open(os.path.join(OUT, "_stage1_gh.json"), encoding="utf-8"))["repos"]
s2 = json.load(open(os.path.join(OUT, "_stage2.json"), encoding="utf-8"))["results"]

bad = []
for e in EX:
    h, k = e["_host"], e["_key"]
    if h == "github":
        p = os.path.join(RM, k.replace("/", "__") + ".md")
        src = open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""
        src += "\n<<META>>\n" + (s1[k].get("description") or "")
    elif h == "gitlab":
        p = os.path.join(RM, "gitlab__" + k.replace("/", "__") + ".md")
        src = open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""
        src += "\n<<META>>\n" + (s2["gitlab"][k].get("description") or "")
    elif h == "pypi":
        i = s2["pypi"][k]["info"]
        src = json.dumps(i, ensure_ascii=False) + "\n" + (i.get("summary") or "") + "\n" + str(i.get("license_expression"))
    else:
        pk = s2["npm"][k]["pkg"]
        src = json.dumps(pk, ensure_ascii=False) + "\n" + (pk.get("description") or "")
    allq = [(q["quote"], "F4/" + q.get("class", "")) for q in e["F4_evidence_quotes"] if q.get("quote")]
    allq += [(q["quote"], "F9") for q in e.get("F9_preconditions_stated", []) if q.get("quote")]
    inj = e.get("injection_observed")
    if inj and inj.get("verbatim"):
        allq.append((inj["verbatim"], "injection"))
    o = e.get("F10_outcome_reported", {})
    if o.get("verbatim"):
        allq.append((o["verbatim"], "F10"))
    for q, tag in allq:
        if q not in src:
            bad.append((e["id"], k, tag, q[:90]))

if bad:
    print("QUOTE VERIFICATION FAILURES:", len(bad))
    for b in bad:
        print("  ", b[0], "|", b[2], "|", b[1], "\n     >>", b[3])
    sys.exit(1)
print("ALL QUOTES VERIFIED reproducible from retrieved bytes:", sum(
    len([q for q in e["F4_evidence_quotes"] if q.get("quote")]) for e in EX), "F4 quotes across", len(EX), "records")
