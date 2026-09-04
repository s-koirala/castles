# -*- coding: utf-8 -*-
"""Assemble the ACADEMIC-arm candidate table and write it, with its branching rule,
into the arm's own log directory. NO eligibility determination is made: every field
whose name ends in _signal is a keyword signal over retrieved metadata, and section
4.2 stage-1 dispositions are NOT assigned here."""
import os, sys, json, re, time, urllib.request, urllib.error, hashlib, datetime
assert os.environ.get("PYTHONHASHSEED") == "0"

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
LOGDIR = os.path.join(REPO, "docs", "literature", "search_logs", "kalshi-strategy-multivocal")
ROWS = json.load(open(os.path.join(HERE, "candidates.json"), encoding="utf-8"))

K2 = [r"return", r"profit", r"backtest", r"fill rate", r"violation", r"realized", r"realised",
      r"sharpe", r"pnl", r"p&l", r"simulat", r"empirical"]
K3 = [r"\bfee", r"\btick\b", r"collateral", r"margin", r"position limit", r"rate limit",
      r"settlement", r"resolution rule", r"latency", r"capital", r"lock-?up", r"maker", r"taker"]
K4 = [r"dataset", r"\bapi\b", r"framework", r"harness", r"toolkit", r"benchmark", r"database", r"pipeline"]

CLASS = [
    ("arbitrage-coherence", [r"arbitrage", r"coherence", r"mispric"]),
    ("market-making-quoting-inventory", [r"market ?mak", r"quoting", r"quote", r"inventory", r"liquidity provision"]),
    ("execution-and-timing", [r"execution", r"order book", r"latency", r"taker", r"maker"]),
    ("hedging-and-basis", [r"hedg", r"basis"]),
    ("forecasting-driven-trading", [r"forecast", r"trading strateg", r"backtest"]),
]

def hits(pats, t):
    return [p for p in pats if re.search(p, t)]

out = []
for r in ROWS:
    t = ((r["title"] or "") + " " + " ".join(r["strategy_hits"]) + " " + " ".join(r["instrument_hits"])).lower()
    # the abstract is not re-stored on the row; use the signal lists already computed plus title
    codes = []
    if r["strategy_hits"] and (r["instrument_hits"] or r["venue_hits"]):
        codes.append("K1?")
    if hits(K2, t):
        codes.append("K2?")
    if hits(K3, t):
        codes.append("K3?")
    if hits(K4, t):
        codes.append("K4?")
    cls = [name for name, pats in CLASS if any(re.search(p, " ".join(r["strategy_hits"])) for p in pats)]
    r["contribution_code_signals"] = codes
    r["strategy_class_signal"] = cls
    out.append(r)

REPORT = [r for r in out if r["branch"] in ("B1-instrument-and-strategy", "B2-instrument-only")]
REPORT.sort(key=lambda r: (not r["venue_hits"], -(int(r["year"]) if str(r.get("year") or "").isdigit() else 0)))

# ---- DOI / arXiv resolution check on the reported set -------------------------
UA = "castles-research/1.0 (+https://github.com/s-koirala; mailto:238704148+s-koirala@users.noreply.github.com)"
res_cache = {}
def resolve(doi):
    if doi in res_cache:
        return res_cache[doi]
    u = "https://doi.org/api/handles/" + urllib.parse.quote(doi)
    try:
        rq = urllib.request.Request(u, headers={"User-Agent": UA})
        d = json.loads(urllib.request.urlopen(rq, timeout=45).read())
        v = d.get("responseCode")
    except urllib.error.HTTPError as e:
        v = "http-%s" % e.code
    except Exception as e:
        v = "error-%s" % type(e).__name__
    res_cache[doi] = v
    time.sleep(0.4)
    return v

import urllib.parse
checked = 0
for r in REPORT:
    if r["doi"]:
        r["doi_handle_responseCode"] = resolve(r["doi"])
        checked += 1
    else:
        r["doi_handle_responseCode"] = None
print("DOIs resolution-checked:", checked,
      "responseCode==1:", sum(1 for r in REPORT if r.get("doi_handle_responseCode") == 1),
      "failures:", sorted({str(r.get("doi_handle_responseCode")) for r in REPORT if r["doi"] and r.get("doi_handle_responseCode") != 1}))

payload = {
    "_header": True,
    "artifact": "ACADEMIC-arm candidate table",
    "arm": "academic",
    "protocol": "docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md",
    "protocol_sha256": "32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac",
    "registration_commit": "4821611c1c93b5f929a76f3ba6207e900440cee5",
    "built_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    "pythonhashseed": "0",
    "automation_tool": "Claude Opus 5 (model id claude-opus-5), acting as the single executing agent",
    "what_this_is_NOT": [
        "No section 4.2 stage-1 disposition is assigned in this file. No record here is included, excluded, or promoted.",
        "Every field ending in _signal, and every contribution code suffixed '?', is a keyword signal over retrieved metadata, not a determination under N1-N6 or K1-K4.",
        "Under section 4.4 every row is therefore a G1 row until a screening session decides it: identified, eligibility not assessed, nothing about its merits determined.",
    ],
    "counts": {
        "n_rows_returned_by_platforms": len(ROWS) if False else None,
        "n_deduplicated_records": len(out),
        "n_in_reported_branches": len(REPORT),
    },
    "branching_rule_file": "docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-stage1-branch-rule.md",
    "records": REPORT,
}
json.dump(payload, open(os.path.join(LOGDIR, "ks-academic-candidates.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
json.dump(out, open(os.path.join(LOGDIR, "ks-academic-identified-universe.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
print("wrote candidate table:", len(REPORT), "of", len(out))
