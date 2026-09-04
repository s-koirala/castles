"""Emit the G1/G2 capacity ledger required by protocol section 4.4 / 4.5.

RE-RUNNER NOTE. Consumes _drawn.json, _stage1_gh.json and _stage2.json, none of which was
retained. All three are re-derivable offline from the archived payloads under ../payloads/;
see ../README.md for the verified reconstruction and its checked counts.
"""
import os, json, datetime
from pathlib import Path

assert os.environ.get("PYTHONHASHSEED") == "0", \
    "PYTHONHASHSEED=0 must be asserted at entry (protocol section 3.0); set it in the environment before launching python"

# The arm's search-log directory, derived from this file's own location; no absolute
# home-directory path is stored — such paths are brittle across machines (CLAUDE.md).
OUT = Path(__file__).resolve().parent.parent
d = json.load(open(os.path.join(OUT, "_drawn.json"), encoding="utf-8"))
s1 = json.load(open(os.path.join(OUT, "_stage1_gh.json"), encoding="utf-8"))
s2 = json.load(open(os.path.join(OUT, "_stage2.json"), encoding="utf-8"))
recs = [json.loads(l) for l in open(os.path.join(OUT, "ks-github-records.jsonl"), encoding="utf-8")][1:]

assessed = {r["platform_metadata"]["full_name"] for r in recs}
n_identified = (len(s1["repos"]) + len(s2["results"]["gitlab"])
                + len(s2["results"]["pypi"]) + len(s2["results"]["npm"]))

g1 = {}
for k, names in d["universe"].items():
    g1[k] = [n for n in names if n not in assessed]
n_g1_in_strata = sum(len(v) for v in g1.values())
n_outside = n_identified - sum(len(v) for v in d["universe"].values())

led = {
 "_header": {
  "arm": "software-repository", "registration_commit": "4821611c1c93b5f929a76f3ba6207e900440cee5",
  "protocol_sha256": "32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac",
  "protocol_section": "4.4 (capacity gaps are not eligibility determinations), 4.5 (arithmetic identities)",
  "subset_rule": "ks-github-subset-rule.md, fixed before any record in the subset was assessed (section 4.4 rule 4)",
  "written_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
  "WHAT_G1_MEANS": ("G1 — identified, eligibility not assessed. The record entered the universe and NO "
                    "eligibility determination under N1-N6 was ever made for it. It is NOT eligible and "
                    "NOT ineligible: it is UNDECIDED. Nothing about its merits was determined. G1 is a "
                    "CAPACITY GAP, NOT A CRITERION FAILURE (section 4.4 rule 1), and no G1 row may be "
                    "converted to a Y-code without the assessment a Y-code asserts (rule 3)."),
  "WHAT_G2_MEANS": ("G2 — eligible, extraction not performed. No record in this arm carries G2: every "
                    "record that passed section 2 in this session was also extracted."),
  "REPORTING_OBLIGATION": ("The corpus record must report G1 and G2 counts SEPARATELY from every Y-code "
                           "count. A corpus record that folds G-rows into the Y totals is defective "
                           "(section 4.4 rule 2)."),
  "HOW_A_LATER_SESSION_DECIDES_THESE": ("Section 4.4 rule 4: a later session may decide a G1 row, and does "
                                        "so as a numbered amendment stating the subset rule it applied and "
                                        "fixing that rule BEFORE any record in the subset is assessed."),
 },
 "counts": {
  "n_identified_this_arm": n_identified,
  "n_identified_by_host": {"github.com": len(s1["repos"]), "gitlab.com": len(s2["results"]["gitlab"]),
                           "pypi.org": len(s2["results"]["pypi"]),
                           "registry.npmjs.org": len(s2["results"]["npm"])},
  "n_deduplicated_within_arm": ("distinct full_name / package name per host; the harvest keyed on that "
                                "identifier, so intra-arm duplicates were collapsed at harvest and the "
                                "per-host counts above are already deduplicated. Cross-arm and cross-class "
                                "deduplication is the lead session's, per section 4.1."),
  "n_assessed_and_recorded": len(recs),
  "n_included": sum(1 for r in recs if r["disposition"] == "include"),
  "n_excluded_Y2": sum(1 for r in recs if r.get("primary_exclusion_code") == "Y2"),
  "n_excluded_Y4": sum(1 for r in recs if r.get("primary_exclusion_code") == "Y4"),
  "n_G1_identified_eligibility_not_assessed": n_identified - len(recs),
  "n_G2_eligible_extraction_not_performed": 0,
  "identity_check": (f"{n_identified} identified = {len(recs)} assessed + "
                     f"{n_identified - len(recs)} G1"),
 },
 "stratum_sizes_under_the_subset_rule": d["stratum_sizes"],
 "note_on_records_outside_every_stratum": {
  "n": n_outside,
  "meaning": ("Records returned by the frozen query grid whose platform metadata matched no venue token, "
              "or matched a venue token but no artifact-intent token, under the SR-1/SR-2/SR-3 screen. "
              "They are G1 — UNDECIDED — exactly like the in-stratum remainder. They are NOT Y1 and NOT "
              "Y2: no eligibility determination was made for any of them (section 4.4 rules 1 and 3)."),
 },
 "G1_rows_within_the_strata": {k: sorted(v) for k, v in g1.items()},
}
json.dump(led, open(os.path.join(OUT, "ks-github-capacity-ledger.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
print("identified", n_identified, "| assessed", len(recs), "| G1", n_identified - len(recs),
      "| G1 in-strata", n_g1_in_strata, "| outside strata", n_outside)
