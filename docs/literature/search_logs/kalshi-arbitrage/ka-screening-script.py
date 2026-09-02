# Archived screening tooling for the kalshi-arbitrage registered search.
# Absolute scratch paths present at execution time were replaced by <WORKDIR> so that no
# OS account name appears in a committed file (CLAUDE.md, identity hygiene).
#
# REMEDIATION 2026-09-02 (round-1 audit). Three findings are discharged in this file and
# each edit is tagged with its finding id:
#
#   QUANT-1-1 [critical] -- this script, not a reading screener, is what produced every
#     disposition except the 149 includes. The rule set R0-R9 below and the five token
#     lists EVENT / CONTRIB / MODEL / DEFI / ELICIT are therefore declared, in the emitted
#     header and in protocol amendment A10, as THE automation tool of record for all
#     8,664 non-include dispositions. The previous header note claimed the rules "encode"
#     a screener's reading; that claim was unfalsifiable and is struck.
#   QUANT-1-2 [major] -- the DEFI list matched unanchored substrings: "dex" fired inside
#     "index" (51 hits), "amm" inside "programming" (9), "defi" inside "defined" (7).
#     The four affected tokens are now matched with word boundaries. See BOUNDED below.
#   QUANT-1-4 [major] -- the X10 / X11 reason strings described eligibility determinations
#     ("ELIGIBLE", "promoted") that no human or model ever made for those records. They
#     are restated as what they are: keyword-identified strata.
#
# Run with PYTHONHASHSEED=0 (QUANT-1-6); inputs are produced by ka-universe-script.py,
# ka-dedup-script.py and ka-partition-script.py, all in this directory.
import json, io, os, re, pathlib, collections

if os.environ.get("PYTHONHASHSEED") != "0":
    raise SystemExit("QUANT-1-6: run with PYTHONHASHSEED=0.")
SP = os.environ.get("KA_WORKDIR", r"<WORKDIR>")
LOG = pathlib.Path("docs/literature/search_logs/kalshi-arbitrage")
works = json.load(io.open(SP + "/works.json", encoding="utf-8"))
byuid = {w["uid"]: w for w in works}
part = json.load(io.open(SP + "/partition.json", encoding="utf-8"))
inc = json.load(io.open(SP + "/inc.json", encoding="utf-8"))
INCLUDE = {o["uid"]: o for o in inc["include"]}
X7SET = set(inc["x7"])
DEFAULT_X1 = set(part["default_x1"])
# J6 hand-verified same-work twin found at extraction time: the SSRN 2001 working-paper
# version (10.2139/ssrn.294306) is the same work as the European Financial Management 2005
# version (10.1111/j.1354-7798.2005.00274.x). The titles differ by a trailing word so the
# normalized-title merge did not catch it. J6 retains the journal version; the twin is
# excluded X9 and pointed at its retained partner. This is the ONE non-include verdict in
# the whole file that a human hand-verified rather than the classifier assigning it.
# QUANT-1-6: keyed by DOI, not by run-generated uid, which is not stable across runs.
_TWIN_DOI, _KEEP_DOI = "10.2139/ssrn.294306", "10.1111/j.1354-7798.2005.00274.x"
_by_doi = {d.lower(): w["uid"] for w in works for d in w["dois"]}
X9 = {_by_doi[_TWIN_DOI]: _by_doi[_KEEP_DOI]}

EVENT = ["prediction market", "prediction-market", "event contract", "event-contract", "event derivative",
         "event market", "information market", "decision market", "betting", "bettor", "wager", "gambl",
         "bookmak", "bookie", "sportsbook", "sports book", "parimutuel", "pari-mutuel", "pari mutuel",
         "racetrack", "horse rac", "point spread", "pointspread", "moneyline", "money line", "longshot",
         "long shot", "long-shot", "overround", "lottery", "lotteries", "kalshi", "polymarket", "predictit",
         "tradesports", "intrade", "betfair", "iowa electronic", "binary option", "binary contract",
         "binary prediction", "state contingent", "state-contingent", "contingent claim", "arrow security",
         "boolean securit", "combinatorial market", "combinatorial predict", "odds", "spread betting",
         "wagering"]
CONTRIB = ["arbitrage", "no-arbitrage", "law of one price", "coheren", "mispric", "misalign",
           "price discrepanc", "efficien", "calibrat", "bias", "transaction cost", "commission", "fee",
           "collateral", "margin", "execut", "liquidit", "market maker", "market-maker", "market making",
           "market-making", "scoring rule", "microstructure", "spread", "probabilit", "overround",
           "forecast accuracy", "return", "profit", "manipulat", "informed trad", "adverse selection"]
MODEL = ["market maker", "market-maker", "market making", "market-making", "marketmaking", "scoring rule",
         "lmsr", "automated market", "constant function market", "constant product market", "cfmm",
         "inventory risk", "inventory cost", "inventory control", "inventory effect", "dealer pricing",
         "optimal quot", "glosten", "milgrom", "kyle model", "avellaneda", "stoikov", "ho-stoll",
         "liquidity provision", "liquidity provider", "specialist", "dealership", "immediacy"]
DEFI = ["defi", "decentralized finance", "decentralised finance", "uniswap", "sushiswap",
        "impermanent loss", "liquidity pool", "token pair", "blockchain", "cryptocurrency", "stablecoin",
        "dex", "on-chain", "smart contract", "amm", "constant product", "yield farming", "crypto"]
ELICIT = ["elicit", "proper scoring rule", "forecast tournament", "expert judgment", "expert judgement",
          "delphi", "crowdsourc", "wisdom of crowd", "peer prediction", "belief elicitation", "survey"]

# QUANT-1-2. Four DEFI tokens are short enough to occur inside unrelated words. They are
# matched with word boundaries instead of as bare substrings. The inflected forms admitted
# are exactly those attested in this record universe, so no form is invented:
#   dexe?s?  -- "DEX", "DEXs", "DEXes" (e.g. "Funding-Aware Optimal Market Making for
#               Perpetual DEXs"); excludes "index", "indexed", "sensex-index", "stockindex"
#   amms?    -- "AMM", "AMMs"; excludes "programming", "programmable", "hammer",
#               "notamment", "constamment", "independamment"
#   defi     -- "DeFi"; excludes "defined", "definition", "predefined", "indefinite"
#   crypto   -- prefix-anchored: "crypto", "cryptocurrency", "cryptoeconomic", "crypto-asset"
# Every other DEFI token is >= 8 characters or contains a space and is left as a substring
# test, which is the frozen behaviour.
BOUNDED = {"dex": r"\bdexe?s?\b", "amm": r"\bamms?\b", "defi": r"\bdefi\b", "crypto": r"\bcrypto"}
BOUNDED_RE = {k: re.compile(v) for k, v in BOUNDED.items()}
# Audit toggle. KA_DEFI_MATCH=substring reproduces the pre-remediation (defective) behaviour
# byte for byte, so the before/after deltas reported in the corpus record section 6 can be
# re-derived by a third party without editing this file. Default is the corrected behaviour.
if os.environ.get("KA_DEFI_MATCH") == "substring":
    BOUNDED_RE = {}


def blob(w):
    return ((w.get("title") or "") + " || " + " || ".join(w.get("titles_all") or []) + " || " +
            (w.get("abstract") or "")).lower()


def any_in(b, toks):
    return any(t in b for t in toks)


def any_defi(b):
    """QUANT-1-2: DEFI membership with word boundaries on the four short tokens."""
    for t in DEFI:
        if t in BOUNDED_RE:
            if BOUNDED_RE[t].search(b):
                return True
        elif t in b:
            return True
    return False


def has_pid(w):
    return bool(w["dois"] or w["arxiv"] or w["repec"])


RULES = {
    "R0": "uid is in the extracted included set -> include",
    "R1": "record would otherwise pass 2.1/2.2 (R3 or R6 branch) but carries no DOI, arXiv id or RePEc handle -> X7 (fails I3). Applied AFTER X1/X2/X5 per the section 2.4 first-code-that-applies ordering",
    "R2": "DEFAULT-X1 stratum of amendment A3 (no in-scope vocabulary token in title or abstract) -> X1",
    "R3": "event-claim token AND contribution token present -> X10 (keyword-identified candidate stratum; no eligibility determination was made for these records -- QUANT-1-4, amendment A10)",
    "R4": "event-claim token present, no contribution token -> X2 (satisfies 2.1 but makes none of C1-C4)",
    "R5": "no event-claim token, model token present, word-boundary DeFi/token-pair token present -> X5 (keyword determination that the traded object is a token pair, not an event claim; QUANT-1-2 corrected the token match from substring to word boundary)",
    "R6": "no event-claim token, model token present, no DeFi token -> X11 (keyword-identified model-record stratum; neither a stage-1 nor a stage-2 assessment was performed for these records -- QUANT-1-4, amendment A10)",
    "R7": "no event-claim token, no model token, elicitation token present -> X3 (elicitation without a transferable traded claim; fails B-d)",
    "R8": "otherwise -> X1 (not an in-scope instrument under 2.1 and not a C3 transfer-clause record)",
    "R9": "hand-verified same-work twin under J6 -> X9, pointing at the retained journal version",
}
REASON = {
    "include": "eligible under I1-I5; extracted per section 5",
    "X7": "fails I3: no DOI, arXiv identifier or RePEc handle in any retrieved metadata record (FAIR F1 gap, recorded not dropped)",
    "X1": "fails 2.1 (B-a/B-b/B-c/B-d): title and abstract identify no traded event claim, and the record is not a C3 transfer-clause model record",
    "X2": "satisfies 2.1 but makes none of C1-C4: no condition stated, no quantity measured, no model specified, no microstructure result",
    "X3": "probability elicitation / forecasting or scoring-rule evaluation with no transferable traded claim; fails B-d",
    "X5": "traded object is a token pair or liquidity pool rather than an event claim; fails B-a",
    "X10": "AMENDMENT A4, as restated by amendment A10 -- KEYWORD-IDENTIFIED CANDIDATE STRATUM, NOT a criterion failure and NOT an eligibility determination. Title/abstract carry both an event-claim token and a contribution token, which is the A4 extraction-selection rule's keyword proxy for a record serving only secondary objectives O2/O3. No screener read these records; eligibility under I1-I5 was never assessed and section-5 extraction was not performed (capacity gap)",
    "X9": "X9 duplicate: same work as the retained European Financial Management (2005) record doi:10.1111/j.1354-7798.2005.00274.x; J6 retains the journal version and records the working-paper twin here. Hand-verified at extraction time; the only non-include verdict in this file that the keyword classifier did not assign",
    "X11": "AMENDMENT A5, as restated by amendment A10 -- KEYWORD-IDENTIFIED MODEL-RECORD STRATUM, NOT a criterion failure and NOT an eligibility determination. Title/abstract carry a market-making/inventory-model token and no event-claim token, which is the keyword proxy for a section 2.2 transfer-clause candidate. No screener read these records; neither the stage-1 promotion condition of section 4.2 nor any stage-2 full-text assessment was evaluated for any of them, so eligibility is UNDECIDED (capacity gap)",
}
CRIT = {"R0": "I1-I5", "R1": "I3", "R2": "2.1 B-a/B-b/B-c/B-d", "R3": "I1,I2 (A4)", "R4": "C1-C4",
        "R5": "B-a / X5", "R6": "2.2 transfer clause (A5)", "R7": "B-d / X3", "R8": "2.1", "R9": "X9 / J6"}

rows = []
counts = collections.Counter()
rule_counts = collections.Counter()      # QUANT-1-1 / REV-1-6: publish the per-rule split
verdict_source = {}
for uid in sorted(byuid):
    w = byuid[uid]
    b = blob(w)
    if uid in X9:
        v, code, rule = "exclude", "X9", "R9"
    elif uid in INCLUDE:
        v, code, rule = "include", None, "R0"
    elif uid in DEFAULT_X1:
        v, code, rule = "exclude", "X1", "R2"
    else:
        ev, co = any_in(b, EVENT), any_in(b, CONTRIB)
        mo, de, el = any_in(b, MODEL), any_defi(b), any_in(b, ELICIT)   # QUANT-1-2
        if ev and co:
            if has_pid(w) and uid not in X7SET:
                v, code, rule = "exclude", "X10", "R3"
            else:
                v, code, rule = "exclude", "X7", "R1"
        elif ev:
            v, code, rule = "exclude", "X2", "R4"
        elif mo and de:
            v, code, rule = "exclude", "X5", "R5"
        elif mo:
            if has_pid(w) and uid not in X7SET:
                v, code, rule = "exclude", "X11", "R6"
            else:
                v, code, rule = "exclude", "X7", "R1"
        elif el:
            v, code, rule = "exclude", "X3", "R7"
        else:
            v, code, rule = "exclude", "X1", "R8"
    counts[code or "include"] += 1
    rule_counts[rule] += 1
    verdict_source[rule] = ("hand-verified by the screener" if rule == "R9"
                            else "screener read + extracted" if rule == "R0"
                            else "keyword classifier (this script); no record read")
    if w["dois"]:
        ident = w["dois"][0]
    elif w["arxiv"]:
        ident = "arXiv:" + w["arxiv"][0]
    elif w["repec"]:
        ident = "RePEc:" + w["repec"][0]
    else:
        ident = ""
    rows.append({
        "id": uid,
        "citation": "%s (%s). %s." % ((w.get("title") or "[no title]")[:150],
                                      w.get("year") or "n.d.", w.get("venue") or "n.v."),
        "identifier": ident,
        "stage_excluded": ("n/a (included)" if v == "include"
                           else ("identification" if code == "X7" else "title-abstract")),
        "verdict": v,
        "primary_code": code,
        "secondary_codes": [],
        "criterion_cited": CRIT[rule],
        "rule": rule,
        "reason": REASON[code or "include"],
        "arms": w["arms"],
    })

hdr = {
    "_header": True,
    "protocol": "docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md",
    "protocol_sha256": "99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4",
    "protocol_sha256_note": ("registration hash of the frozen protocol; it is the hash of the first "
                             "82,677 bytes of the file, which are unaltered. Amendments A1-A15 are "
                             "appended to that file's append-only addendum (A1-A12 on 2026-09-02 under "
                             "amendment A12; A13-A15 at round-2 audit remediation the same day), so the "
                             "whole-file digest is now "
                             "21a77d10841ba7f15ea58d5a58a1bca57818b2ed1a0f3bf53a1dbce6a8dcc53b "
                             "(132,488 bytes), superseding 42bc6116ee554ee5cc80743d14d2f3d834f4feb389b5"
                             "3b5eaf2820c27322a762"),
    "registration_commit": "27d74738aa35ec1cdf1ec6915b50532e3620ea6f",
    "date": "2026-09-02",
    "n_records": len(rows),
    "screeners_n": 1,
    "independent": "no",
    "automation_tools": [
        "Claude Opus 5 (model id claude-opus-5), LLM screener, PRISMA 2020 item 8 automation tool. "
        "Scope of its READ-BASED verdicts, corrected 2026-09-02 under amendment A10: the 149 included "
        "records (extracted at abstract or metadata depth) and the single hand-verified J6 same-work "
        "twin excluded X9. NO other record in the universe carries a read-based verdict.",
        "This script -- the deterministic five-list keyword classifier below (token lists EVENT, CONTRIB, "
        "MODEL, DEFI, ELICIT; rules R0-R9) -- is THE automation tool of record for all 8,664 non-include "
        "dispositions. Declared under protocol amendment A10 (finding QUANT-1-1). It supersedes the "
        "narrower declaration made under amendment A3, which named only the DEFAULT-X1 partition.",
        "amendment A3 deterministic vocabulary pre-sorter (ka-screening-vocabulary.json) -- the R2 branch "
        "of the classifier above; retained as a separate declaration because its token list and partition "
        "counts are published separately"],
    "note": ("PRISMA 2020 item 8, corrected. Every verdict in this file except the 149 includes and the "
             "single X9 twin was assigned by the keyword classifier in this script, not by a screener "
             "reading the record. That is true of the 5,249-record amendment-A3 DEFAULT-X1 stratum (rule "
             "R2), of the 2,905-record A3 REVIEW stratum, and of the 659 topical / known-item / "
             "supplementary records alike: all three were routed through rules R3-R8. The previous "
             "wording of this field said the rule set 'encodes' a screener's reading of the REVIEW and "
             "topical strata; that claim was not falsifiable from any artefact and is withdrawn. "
             "Consequence for every count in this file: a code is a statement about which tokens the "
             "record's title and abstract contain, and about nothing else."),
    "remediation": {
        "date": "2026-09-02",
        "round": "audit rounds 1 and 2",
        "amendments": ["A10 (classifier declared as the automation tool of record; QUANT-1-1)",
                       "A11 (word-boundary DeFi matching + deterministic uid assignment; QUANT-1-2, QUANT-1-6)",
                       "A13 (A10's strike of the individual-reading claims completed; REV-2-1, SCOPE-2-5, REPRODUCIBILITY-2-7)",
                       "A14 (evidence corrections to A11; both declared departures upheld; QUANT-2-2, QUANT-2-6, QUANT-2-9, REPRODUCIBILITY-2-3/4/5)"],
        "row_ids": ("The row identifier emitted by this script is the field named `id` (NOT `uid`; the "
                    "header said `uid` until 2026-09-02, finding QUANT-2-6). `id` values are regenerated "
                    "under PYTHONHASHSEED=0 with total dedup tie-breaks and DO NOT correspond to the "
                    "values published on 2026-09-02 before round-1 remediation."),
        "row_ids_migration_key": ("Join on the `identifier` field, not on `id` -- but the join is DEFINED "
                                  "ONLY for the 6,923 rows carrying a persistent identifier, on which "
                                  "`identifier` values are unique. It is NULL (the empty string) for the "
                                  "other 1,890 rows (21.4%): every work with no DOI, no arXiv id and no "
                                  "RePEc handle gets ident = \"\" below, so those 1,890 collapse to a "
                                  "single join value and CANNOT be reconciled against any earlier file. "
                                  "For them the `citation` string is the only available fallback and it "
                                  "is not a key. Finding QUANT-2-6, amendment A14."),
        "pre_remediation_file": ("NOT ARCHIVED and NOT RECOVERABLE. The pre-remediation verdicts file was "
                                 "overwritten in place by the round-1 re-emission and had never been "
                                 "committed, so it is not in git history either. CONSEQUENCE, stated "
                                 "rather than papered over: the round-1 figures '2,630 of 8,813 uid "
                                 "mappings agreed' and '6,183 published row identifiers were not "
                                 "reproducible' CANNOT BE VERIFIED BY ANYONE from the shipped artefacts. "
                                 "They are an unverifiable assertion of the round-1 remediation session, "
                                 "not a measurement. The determinism defect itself is independently "
                                 "established by the seed guard and by the tie-break argument in A11(b) "
                                 "and A14(a). Findings QUANT-2-6, REPRODUCIBILITY-2-5, amendment A14."),
    },
    "rules": RULES,
    "reasons": REASON,
    "counts": dict(counts),
    "counts_by_rule": dict(sorted(rule_counts.items())),
    "verdict_source_by_rule": dict(sorted(verdict_source.items())),
    "n_read_based_verdicts": counts["include"] + counts["X9"],
    "n_classifier_verdicts": len(rows) - counts["include"] - counts["X9"],
}
with io.open(LOG / "ka-screening-verdicts.jsonl", "w", encoding="utf-8") as f:
    f.write(json.dumps(hdr, ensure_ascii=False) + "\n")
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(json.dumps(dict(counts), indent=1))
print("total", len(rows))
