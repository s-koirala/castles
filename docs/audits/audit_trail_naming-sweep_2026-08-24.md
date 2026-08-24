---
schema_version: "WI-3/2"
conforms_to:
  - "PROV-DM / PROV-O"
  - "RO-Crate 1.1"
  - "ISO 19011:2018"
  - "FAIR (Wilkinson et al. 2016, doi:10.1038/sdata.2016.18)"
  - "Sandve et al. 2013 (doi:10.1371/journal.pcbi.1003285)"
  - "21 CFR 11.10(e)"
  - "ICMJE §V.A"
title: "Audit trail — Naming sweep, round 1"
type: audit_trail
date: "2026-08-24"
started_at: "2026-08-24T09:27:09-05:00"
ended_at: "2026-08-24T09:34:40-05:00"
artifacts:
  - {path: "docs/literature/vocabulary_regime-synonyms_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "56b54aaa8ffbc512669cb13dd1c6d95077b93e76baad9d698d5df293664a78ba"}
  - {path: "docs/literature/lit_review_regime-naming_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "0bf877a832a67403ae5150d8c18d66a8cf7ab13ee26bbb2a164053b3e96acb9f"}
  - {path: "docs/literature/lit_review_regime-naming-a_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "fd23e6d38b229fc2139eda72a6e9f15247e0157ad00f1c590870adf14a2a7cfe"}
  - {path: "docs/literature/lit_review_regime-naming-b_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "015e95509b388cf9071e730f42a2e4447ea95f09751561885722abaa4bfe7564"}
  - {path: "docs/literature/lit_review_regime-definitions_2026-08-21.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "ac64dcebfea3f548cb839fcc27ea9dc5889ff0644fb453bfba5a899a299c3bb4"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "7032ba091976204ecced698b1721b14fda83829a1a406d7cf521c38263d93cfe"}
repo_head: "0845acbf5d464cd330c93941c3af1bf000f3791d"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    Round 1 audit of the naming-sweep session (deliverable_spec_naming-sweep_2026-08-24.md). Three research-librarian stages produced: (1) the term registry vocabulary_regime-synonyms_2026-08-24.md (137 head terms, 8 traditions, ~540 morphological variants, homonym-collision ledger; harvest provenance only, never evidence; methodology citations PRESS/McGowan 2016, pearl growing/Schlosser 2006, Hausner 2012 — all handle-verified); (2) two tradition-clustered sweep part-records — lit_review_regime-naming-a (practitioner clusters, 22 records, NA-01..NA-20, 67 synonym-graph rows) and lit_review_regime-naming-b (academic clusters, 31 records, NB-01..NB-31, 45 rows) — each with logged queries, first-class zero-record negatives, and declared coverage gaps. The lead session then (3) merged the part stores into references_regime-naming.json (53 entries, zero id/DOI collisions, deterministic check PASS), wrote the umbrella record lit_review_regime-naming_2026-08-24.md (combined flow 1059/990/53, synonym-graph summary, saturation adjudication: NOT reached — 6 flagged families swept in-line, 6 tier-5 ICT/Wyckoff-adjacent residuals logged open with expected-yield rationale), (4) appended an append-only supplement addendum to lit_review_regime-definitions_2026-08-21.md (pre-addendum SHA-256 b561340781d8bc3de3ce0b7aa18b7d1f75414428fe111c4abaff574e8e2e4464 recorded in the addendum; single addendum marker verified) superseding its time-t-null universal, and (5) revised the agenda to revision 3: Definitional-basis item (d) struck and restated as refuted-by-vocabulary-expansion (Phillips-Wu-Yu 2011 doi:10.1111/j.1468-2354.2010.00625.x; Phillips-Shi-Yu 2015 doi:10.1111/iere.12132 — real-time date-stamping of an explosive state with stated limit theory), with the bounded survivor stated; item (b) range claim bounded (spatial operationalizations prior-covered; temporal-state definition unlocated); compression negative upgraded to two-sweep-stable; branch 3 gains the SADF/GSADF date-stamping comparator note and DC additions (NB-25..29); Verification status records Rev 3 with the abstract-depth caveat on the Phillips records. AUDIT FOCUS: (a) claim fidelity — does each integration accurately carry what its part-record establishes; ESPECIALLY the Phillips date-stamping characterization (real-time, stated critical values — verify against the actual records at abstract level; the agenda itself flags full-text as pending, so audit the claim AS BOUNDED); (b) the supersession chain: definitions-survey addendum, umbrella §3, and agenda (d) must tell the same story with the same bounded survivor; (c) registry honesty — harvest-provenance-only discipline (nothing in the registry cited as evidence anywhere); (d) saturation adjudication honesty — residuals logged open, not claimed saturated; (e) synonym-graph spot fidelity — sample rows against their cited sources; (f) no regression of prior-spec remediations in the re-edited files (agenda Rev 2 fixes intact; F005 addendum untouched). The G16 publisher-403 class is closed (handle-API responseCode 1 is the test; both sweeps carry per-DOI logs and dispositions; the part records' gate 'block' verdicts are G16-only and dispositioned — do not re-raise). The lowercase filename deviation (regime-naming-a/-b vs the spec's part-file naming) is declared in the part records — assess whether it needs more than the declaration.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_naming-sweep_2026-08-24.md", sha256: "06362dc88247cbe9db93eda9dfb434c2413fddfa7798eebbb005e90392142533"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill)."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-fable-5", effort: "medium", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-fable-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Fable 5, claude-fable-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, literature-check) → adversarial refuter → trail-assembly agent (this document)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. All six artifacts are markdown prose (a term registry, three literature scoping records, the amended definitions survey, and the research agenda — no code, no executed statistics), so quant-auditor and epi-auditor were not routed. critical-reviewer (claim fidelity, supersession-chain consistency, saturation honesty) and scope-auditor (deliverable coverage against deliverable_spec_naming-sweep_2026-08-24.md, including the declared filename deviation) are unconditional; literature-check routed on the citation-fidelity focus of the taskSpec (Phillips date-stamping characterization, synonym-graph spot fidelity, registry harvest-provenance discipline). Efforts: critical-reviewer high, scope-auditor medium, literature-check high."
rounds_completed: 1
rounds_cap: 3
cap_reached: false
verdict: "proceed-with-remediation"
counts: {raw_critical: 0, raw_major: 5, raw_minor: 14, refuted: 0, retained_conservative: 0, to_remediate: 5, minors_logged: 14}
sidecar: {path: "docs/audits/audit_trail_naming-sweep_2026-08-24.json", sha256: "fffba9ee9cb8130ffd1ae7889d91090324f905b79006958af08cec698af69b48"}
---

# Audit trail — Naming sweep, round 1

Round 1 of the fresh 3-round cap opened by
[deliverable_spec_naming-sweep_2026-08-24.md](../deliverables/deliverable_spec_naming-sweep_2026-08-24.md).
Audited artifacts: the term registry, the two tradition-clustered sweep
part-records, the umbrella record, the amended definitions survey, and the
Rev 3 regime-classification agenda (worktree versions at HEAD `0845acb`,
uncommitted — `worktree_clean: false`; artifact digests in the front matter
and the JSON sidecar). Branch verdicts: critical-reviewer
proceed-with-remediation, scope-auditor proceed-with-remediation,
literature-check proceed-with-remediation. Round verdict:
**proceed-with-remediation** (0 critical, 5 major to remediate, 14 minors
logged, 0 refuted). Full finding payloads, refute-gate dispositions, and
per-branch residual-risk statements are held verbatim in the JSON sidecar
([audit_trail_naming-sweep_2026-08-24.json](audit_trail_naming-sweep_2026-08-24.json));
the sections below carry the required record.

## findings-table

One row per finding. All eight schema fields (id, severity, category,
location, issue, evidence, fix, reference) plus branch and disposition;
issue/evidence/fix are compressed for tabular legibility — the full verbatim
text of every finding is in the JSON sidecar, and every major's claim is
reproduced verbatim and unabridged in the refute-gate section below.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-1-1 | major | consistency | agenda:94-96 | Supersession-chain divergence: agenda (d) appends an exclusivity clause ("outside the explosive family no other located state vocabulary carries one") absent from addendum and umbrella §3 and unadjudicated by the part records (NB-13, NB-02 carry stated nulls at F causality); bounded-universal overreach recurring in the sentence memorializing the prior instance | "within the 59 surveyed definitions, none attaches a time-t assignment null, and outside the explosive family no other located state vocabulary carries one" | Strike the clause or bound it to what the sweeps adjudicated, flagging NB-02/NB-13 as unadjudicated pending full text | CHAMP item 30; prior-round disposition REV-1-1 | critical-reviewer | retained → remediate |
| REV-1-2 | major | consistency | umbrella:128 | Saturation adjudication says the six residual families "remain in the registry as open rows" — the registry contains no such rows; the open-residual state is honestly declared but mislocated | "They remain in the registry as open rows." | Correct the sentence to the true carrier (part A §8.4 / part B §8.7 flags), or append a registry addendum adding the 12 flagged families and leave the sentence true | CHAMP item 21; register convention | critical-reviewer | retained → remediate |
| SCOPE-1-1 | major | changed | agenda:93-96, :440-442 | Supersession-chain asymmetry: agenda carries a stronger survivor than the other two chain sites; branch 3 restates it as "the one located detector whose time-t assignment carries its own null"; other "stated" null rows (NB-02/NB-08/NB-13/NB-23/NB-29) never established as non-time-t | Agenda extension clause vs addendum "The bounded form survives..." and umbrella "The narrower claim survives..." | Strike the extension from agenda (d) and branch 3, or add it identically at all three sites with its warrant (episode-level vs time-t distinction) | S-3/S-4; task audit focus (b) | scope-auditor | retained → remediate |
| LITERATURE-1-1 | major | misattributed-citation | naming-a:481 (NA-09) | arXiv:2403.18839 cited in prose as "Ige (2024)"; sole author is Jai Pal (export API + abs page); store carries correct "Pal, Jai" under the wrong-name id ige2024arxiv240318839; contradicts prisma-s-7 author-verification claim | Part A line 481 vs arxiv.org/abs/2403.18839 (author Jai Pal, v1 only) | Correct prose to Pal (2024); regenerate the store id (updating recorded SHA-256s) or note the id predates the correction; record the correction event per strike-don't-delete | https://arxiv.org/abs/2403.18839 | literature-check | retained → remediate |
| LITERATURE-1-2 | major | claim-fidelity / supersession-chain divergence | agenda:93-96 (item d, Rev 3) | Restated bounded survivor adds a clause absent from both other chain links; NB-13 and NB-02/NB-08 are unadjudicated counter-candidates at abstract depth; fresh universal-from-bounded-coverage of the session's own named hazard class | Agenda clause vs addendum/umbrella bounded forms; part B §8.9 "stated" null rows | Strike the added clause, or bound it explicitly with the nearest candidates flagged for the full-text pass | naming-b:610-611,832,844; definitions:1253-1260 | literature-check | retained → remediate |
| REV-1-3 | minor | consistency | naming-a:428-429; umbrella:44,130 | "45 bibliographic query executions" vs 47 table rows; only 47 reproduces 756; umbrella propagates 45 and 104 | prisma-s-15 sentence | Recount against the table; correct to 47/106 or state the exclusion rule yielding 45 | SAMPL; PRISMA-S item 15 | critical-reviewer | logged |
| REV-1-4 | minor | consistency | naming-b:137-139,204-205 | "Four informative arXiv zeros" claimed twice; table shows three zero-record rows | "arXiv 7 across 8 queries (four zeros)" | Change to "three zeros" or state the screened-to-zero counting rule explicitly | SAMPL; CHAMP item 20 | critical-reviewer | logged |
| REV-1-5 | minor | reporting | definitions:1256-1258; umbrella:79-86; naming-b:601-602 vs 834 | "Derived critical values" exceeds the quoted abstract evidence; inference from the sup-ADF family; caveat-free in the permanent addendum | "real-time date-stamping with derived critical values" | Replace with quote-supported wording or append the inference/full-text-pending caveat | CHAMP item 24 / SAMPL; evidence hierarchy item 5 | critical-reviewer | logged |
| REV-1-6 | minor | consistency | definitions:1253-1260 vs 1213-1215 | Addendum names only §8.8 as superseded site; §10.5 restates the universal in near-unbounded form under "All other findings stand" | §10.5 "the missing object the corpus-wide search confirms absent" | Extend the addendum's supersession sentence to enumerate §10.5 | Register convention; CHAMP item 30 | critical-reviewer | logged |
| REV-1-7 | minor | interpretation | agenda:96-98; umbrella:73-86 | Methodological moral overstates the registry's role: the refuting family was itself a registry gap reached via dispatch known-item queries | "...is why the term registry now precedes any evidence query" | Add one clause noting registry-first narrows but does not close the F005 class | CHAMP items 27/29 | critical-reviewer | logged |
| REV-1-8 | minor | interpretation | agenda:76-78 | Rev 3 bounding of item (b) is ambiguous where it needs to be exact ("bounded" modifying definition vs hedged "unlocated") | "a bounded operational definition of range as a *temporal state* remains unlocated at any tier" | Rephrase with "with stated price bounds" and the HSMM prior-coverage boundary | CHAMP item 30; SAMPL | critical-reviewer | logged |
| SCOPE-1-2 | minor | partial | agenda:75-78 | Item (b) does not carry the near-miss boundaries: prior tier-1 temporal-state coverage (sideways/HSMM "Sidewalk"; range-bound arXiv:1304.6846) in the same synonym family | Part A lines 586, 593 vs agenda phrasing | Add the boundary and define "bounded operational definition" as a computable price-bound assignment rule | S-4; task audit focus (a) | scope-auditor | logged |
| SCOPE-1-3 | minor | documented-drift | naming-a:61 (and NB namespace) | Spec says definitions numbered continuing the D-series; delivery opens NA-/NB-namespaces, documented as design rule but not flagged as spec deviation | Spec lines 30-31 vs part A §1.2 | One-line umbrella note recording the deliberate deviation with rationale; no renumbering | S-2 | scope-auditor | logged |
| SCOPE-1-4 | minor | documented-drift | naming-a:727-732; naming-b:893-895 | Filename-case deviation, assessed per the task's explicit question: declared at both part-record sites with the G1 lowercase-slug rationale; all cross-references resolve | Part A limitation 7; part B §9 | None required; recorded here so the disposition is on the trail | S-2; task audit focus | scope-auditor | logged (no action) |
| SCOPE-1-5 | minor | omitted | docs/audits/; git HEAD | Attested trail and provenance commit not yet present — sequenced after this round by design; pending, not a delivery failure | Spec lines 56-63; glob/status at audit time | Write and attest this trail, then /commit-with-provenance role=multi before ticking the spec | S-5, S-6 | scope-auditor | logged (partially discharged by this document) |
| LITERATURE-1-3 | minor | count-integrity | naming-a:652; propagates to umbrella, definitions:1251, agenda | Part A §8.3 says "Row count: 67" but the table holds 66 body rows; combined total 111, not the propagated 112 | Table body lines 585-650 = 66 rows | Recount programmatically; correct 67→66 and 112→111 in all four documents, or restore and document the dropped row | naming-a:585-652 | literature-check | logged |
| LITERATURE-1-4 | minor | count-integrity | naming-a:428; umbrella §1, §4 | "45 bibliographic query executions" vs 47 table rows; umbrella's "104 queries" reconciles with no combination of the part tables | Part A table lines 87-133 = 47; part B subtotals = 59 | Recompute from the tables, state the counting rule, correct 45 and 104 consistently | naming-a:85-136; naming-b:140-205 | literature-check | logged |
| LITERATURE-1-5 | minor | claim-fidelity (bounding phrasing) | agenda:76-79 (item b, Rev 3) | "Unlocated at any tier" defensible only under an unstated reading of "bounded"; part A records a tier-1 prior temporal operationalization (sideways/HSMM) | Part A line 593 vs agenda lines 76-78 | Restrict the claim explicitly to price-bound state definitions | naming-a:593 | literature-check | logged |
| LITERATURE-1-6 | minor | unpinned-citation | registry:96 (§1.5) | "cf. Cochrane Handbook ch. 4" cited without version, authors, or locator — the registry's only unresolved methods citation | Registry lines 93-99 vs DOI-pinned lines 49-74 | Pin to Lefebvre et al., Chapter 4, with version and URL, or drop the aside | https://training.cochrane.org/handbook | literature-check | logged |

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Five dispositions,
all **retained** after failed refutation attempts; zero findings were dropped
(refuted: 0). No entry carries `reproduction_required: true`, so no
`reproduction: {command, observed}` blocks are owed. There are no
retained-conservative entries this round (retained_conservative: 0). Claims
are given verbatim, unabridged.

### REV-1-1 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:94-96
> **issue:** Supersession-chain divergence: the agenda's restated item (d) appends an exclusivity clause absent from both the definitions-survey addendum and the umbrella §3, and the clause is not adjudicated by the part records. Part B's synonym graph marks other families with F-causality AND a stated null — NB-13 flight-to-quality ('a definition and a test', causality F, null 'stated (definition and test together)') and NB-02 drawdown episodes (causality F, null 'stated (stretched-exponential + surrogate)'). Whether those constitute time-t assignment nulls under the survey's §8.8 standard was never assessed at abstract depth; the agenda asserts the negative anyway. This is the session's own named hazard (bounded-universal overreach, REV-1-1 of the prior spec) recurring in the sentence that memorializes the previous instance of it.
> **evidence:** within the 59 surveyed definitions, none attaches a time-t assignment null, and outside the explosive family no other located state vocabulary carries one
> **fix:** Either strike the clause after 'assignment null,' or bound it to what the part records adjudicated, e.g.: 'no other located vocabulary was classified as carrying a time-t assignment null in the sweeps' synonym graphs; NB-02 (drawdown episodes) and NB-13 (flight-to-quality) attach stated nulls at F causality and are unadjudicated against the assignment-null standard pending full text.'
> **reference:** CHAMP item 30 (conclusions limited to what the analysis supports); prior-round disposition REV-1-1 (bounded-universal phrasing discipline)

Refutation evidence:

> Attempted refutation failed; every element of the finding reproduces. (1) The exclusivity clause exists verbatim at agenda lines 94-96: "...none attaches a time-t assignment null, and outside the explosive family no other located state vocabulary carries one." (2) It is absent from both supersession sources: umbrella §3 ends at "within the 59 originally surveyed definitions, none attaches a time-t assignment null" (lines 84-86), and the definitions-survey addendum ends at the same bounded claim plus "All other findings stand" (lines 1258-1260). (3) Part B §8.0 marks NB-13 (Baur & Lucey flight-to-quality) causality F (day-level observables) with null "stated (test accompanies the definition)" and NB-02 (Johansen & Sornette drawdowns) causality F with null "stated (stretched-exponential + surrogate)", repeated in the §8.9 synonym graph. (4) No part record adjudicates either against the time-t assignment-null standard: §8.3 calls NB-13's definition-plus-null pairing "rare in this corpus" (implying non-uniqueness), §8.1 calls NB-02 unique only within the bull/bear family, and §10.1 confirms extraction never exceeded abstract depth. The only counter-argument found (NB-02's boundary "confirmed one move later" arguably fails strict time-t) is itself an adjudication absent from the records and does not cover NB-13. The bounded-universal overreach claim is confirmed.

### REV-1-2 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_regime-naming_2026-08-24.md:128
> **issue:** The saturation adjudication states the six unswept residual families 'remain in the registry as open rows.' They do not: the registry (vocabulary_regime-synonyms_2026-08-24.md) contains no row for absorption, liquidity void, Judas swing, inversion FVG, midnight opening gap, or technical range — grep confirms only 'absorption ratio' as a tradition annotation on the fragile row and 'drawdown' as a retracement variant. Part A §8.4 itself says these terms are 'in NEITHER the registry NOR the seed list (flagged for the registry's next revision)', and the registry file carries no revision or addendum. A future round steered by the umbrella to 'open rows' in the registry finds nothing; the open-residual state — otherwise honestly declared — is mislocated.
> **evidence:** They remain in the registry as open rows.
> **fix:** Correct the sentence to the true carrier: 'They are flagged for the registry's next revision in part A §8.4 and part B §8.7; the registry itself has not yet been revised to carry them.' Alternatively, append an addendum to the registry adding the 12 flagged families as open rows (per the register/living-doc convention) and leave the umbrella sentence true.
> **reference:** CHAMP item 21 (no selective/inaccurate reporting of what exists where); project register convention (append-only addenda)

Refutation evidence:

> Attempted refutation failed; the finding reproduces fully. (1) Line 128 of docs/literature/lit_review_regime-naming_2026-08-24.md contains the exact sentence "They remain in the registry as open rows." applied to the six residual families. (2) Grep of docs/literature/vocabulary_regime-synonyms_2026-08-24.md for absorption|liquidity void|Judas|inversion FVG|midnight opening gap|technical range returns only line 205, where "absorption ratio" is a parenthetical tradition annotation on the fragile row — no open rows for any of the six. (3) Part A §8.4 (lit_review_regime-naming-a_2026-08-24.md lines 656-657) confirms the terms are "in NEITHER the registry NOR the seed list (flagged for the registry's next revision, per dispatch)". (4) The registry file contains no revision or addendum section (grep for addendum/revision hits only an unrelated 2012 citation). The umbrella sentence is therefore factually wrong about where the open-residual state is carried.

### SCOPE-1-1 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** changed
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:93-96 and :440-442
> **issue:** Supersession-chain asymmetry: the agenda carries a stronger survivor than the other two chain sites. The addendum (lit_review_regime-definitions_2026-08-21.md:1258-1260) and umbrella §3 both bound the survivor to 'within the 59 originally surveyed definitions, none attaches a time-t assignment null.' The agenda (d) appends an additional universal — 'and outside the explosive family no other located state vocabulary carries one' — and branch 3 restates it as 'the one located detector whose time-t assignment carries its own null.' That extension is asserted at one of the three sites only and is not marked as going beyond what the addendum/umbrella claim; part B's synonym graph carries other 'stated' null statuses (NB-02/NB-08 drawdown, NB-13 flight-to-quality, NB-23 runs, NB-29 DC overshoot) whose non-time-t character the agenda nowhere establishes. The task spec requires all three sites to tell the same story with the same bounded survivor.
> **evidence:** Agenda: 'within the 59 surveyed definitions, none attaches a time-t assignment null, and outside the explosive family no other located state vocabulary carries one.' Addendum: 'The bounded form survives: within the 59 definitions surveyed here, none attaches a time-t assignment null. All other findings stand.' Umbrella §3: 'The narrower claim survives: within the 59 originally surveyed definitions, none attaches a time-t assignment null.' Part B §8.9 rows with null-status 'stated' outside the explosive family: drawdown/drawup (NB-02, NB-08), flight to quality (NB-13, 'definition and test together'), runs (NB-23), overshoot (NB-29).
> **fix:** Either strike the extension clause from agenda (d) and branch 3 so all three sites carry the identical bounded survivor, or (if the extension is intended) add it identically to the addendum and umbrella §3 with its warrant — an explicit statement of why the other 'stated' null rows in part B §8.9 are not time-t assignment nulls (episode-level vs time-t distinction).
> **reference:** S-3/S-4; task audit focus (b)

Refutation evidence:

> Attempted refutation failed; all evidence reproduces. Agenda lines 93-96 carry the extension clause "and outside the explosive family no other located state vocabulary carries one" and branch 3 (line 442) restates it as "the one located detector whose time-t assignment carries its own null", while the addendum (lit_review_regime-definitions_2026-08-21.md:1258-1260) and umbrella §3 (lit_review_regime-naming_2026-08-24.md:84-86) carry only the bounded survivor with no extension. Part B §8.9 (lines 830-861) confirms "stated" null statuses outside the explosive family (NB-02/NB-08 drawdown, NB-13 flight-to-quality with day-level observables, NB-23 runs, NB-29 DC overshoot). Grep of the agenda for episode/drawdown/flight/runs/overshoot terms returns only explosive-family lines — the agenda nowhere establishes the non-time-t character of those rows. "time-t" appears in neither part-file, so the extension also has no stated warrant in the sweep corpus. The extension's possible substantive defensibility (episode-level vs time-t) does not counter the claimed defect, which is unmarked cross-site asymmetry.

### LITERATURE-1-1 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** misattributed-citation
> **location:** docs/literature/lit_review_regime-naming-a_2026-08-24.md:481 (included-corpus row NA-09; id ige2024arxiv240318839)
> **issue:** Author misattribution in the review prose: the included record arXiv:2403.18839, 'Long Short-Term Memory Pattern Recognition in Currency Trading' (2024, q-fin.TR), is cited as 'Ige (2024)'. The sole author on arXiv (single version, v1, 2024-02-23, confirmed via both the export API and the abs page) is Jai Pal. The merged store references_regime-naming.json:373-377 carries the correct 'Pal, Jai' (fetched from export.arxiv.org), so the prose citation and the store contradict each other, and the store id 'ige2024arxiv240318839' perpetuates the wrong name. This also contradicts the review's own prisma-s-7 claim that every candidate's authors were verified against the arXiv export API before inclusion. Content characterization of the record (algorithmic Wyckoff accumulation/secondary-test labeling via CNN/LSTM) is accurate — only the attribution is wrong.
> **evidence:** Part A line 481: 'Ige (2024). Long Short-Term Memory Pattern Recognition in Currency Trading. arXiv:2403.18839 [q-fin.TR].' vs arxiv.org/abs/2403.18839: author Jai Pal, one version only. Store (references_regime-naming.json lines 373-379) has family 'Pal', given 'Jai' under id 'ige2024arxiv240318839'.
> **fix:** Correct the prose citation in part A section 7 (and anywhere NA-09 is expanded) to Pal (2024). Either regenerate the entry id to pal2024arxiv240318839 in both part-A and merged stores (updating the recorded SHA-256s and the umbrella's bibliography_sha256) or, if id stability is preferred, add an explicit note in part A that the id string predates the correction. Record the correction event rather than silently editing, per the project's strike-don't-delete convention.
> **reference:** https://arxiv.org/abs/2403.18839

Refutation evidence:

> Refutation attempt failed; the finding is independently confirmed. (1) Part A line 481 reproduced verbatim: 'ige2024arxiv240318839 | Ige (2024). Long Short-Term Memory Pattern Recognition in Currency Trading. arXiv:2403.18839 [q-fin.TR]'. (2) references_regime-naming.json lines 373-379 (and references_regime-naming-A.json lines 371-379) carry author family 'Pal', given 'Jai' under the id 'ige2024arxiv240318839'. (3) Fresh fetch of https://export.arxiv.org/api/query?id_list=2403.18839 returns sole author Jai Pal, single version v1, submitted 2024-02-23 — no author 'Ige'. Additional corroboration: the misattribution originates in search log swA-doicheck-02.json line 21, which records the verification result as 'Ige (arXiv q-fin.TR 2024)', contradicting the review's prisma-s-7 author-verification claim exactly as the finding states.

### LITERATURE-1-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** claim-fidelity / supersession-chain divergence
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:93-96 (Definitional basis item d, Rev 3)
> **issue:** The agenda's restated bounded survivor adds a clause absent from both other links of the supersession chain: '...and outside the explosive family no other located state vocabulary carries one [a time-t assignment null].' The definitions-survey addendum (lines 1253-1260) and the umbrella section 3 both bound the survivor strictly to 'within the 59 surveyed definitions'. Neither part record states the agenda's wider universal, and part B's own synonym graph contains located vocabulary that are at minimum unadjudicated counter-candidates at abstract depth: NB-13 flight-to-quality ('a definition and a test' arriving together, day-level observables, causality F, null 'stated') and NB-02/NB-08 drawdown/drawup episodes (causality F, null 'stated'). This is a fresh universal-from-bounded-coverage of exactly the class the session's own hazard note (agenda lines 96-98) and the Rev 2 REV-1-1 disposition name as the required phrasing discipline.
> **evidence:** Agenda: 'within the 59 surveyed definitions, none attaches a time-t assignment null, and outside the explosive family no other located state vocabulary carries one.' Addendum: 'The bounded form survives: within the 59 definitions surveyed here, none attaches a time-t assignment null.' Umbrella section 3: 'The narrower claim survives: within the 59 originally surveyed definitions...'. Part B 8.9 rows 'flight to quality': null-distribution status 'stated (definition and test together)'; 'drawdown / drawup': 'stated (NB-02, NB-08)' with causality F in 8.0.
> **fix:** Either strike the added clause so all three links carry the identical bounded survivor, or bound it explicitly: e.g. 'no other located vocabulary was classified by the sweep as attaching its null to the assignment procedure itself; nearest candidates (flight-to-quality NB-13, drawdown episodes NB-02/NB-08) are unadjudicated at abstract depth and flagged for the full-text pass.'
> **reference:** docs/literature/lit_review_regime-naming-b_2026-08-24.md:610-611,832,844; docs/literature/lit_review_regime-definitions_2026-08-21.md:1253-1260

Refutation evidence:

> Attempted refutation failed; every evidence element reproduces. (1) Agenda lines 93-96 contain the added clause "and outside the explosive family no other located state vocabulary carries one" verbatim. (2) The definitions-survey addendum (lit_review_regime-definitions_2026-08-21.md:1258-1259) and umbrella section (lit_review_regime-naming_2026-08-24.md:84-86) both bound the survivor strictly to the 59 surveyed definitions with no wider clause. (3) Grep across docs/literature for "outside the explosive"/"no other located"/"explosive family" and "assignment null|time-t assignment" confirms no part record states the agenda's wider universal or adjudicates non-explosive vocabulary against the criterion. (4) The cited counter-candidates exist as described: NB-13 (naming-b:610) null "stated (test accompanies the definition)", causality F; 8.9 row (line 844) "stated (definition and test together)"; NB-02 (line 599) causality F, null "stated"; NB-08 (line 605) "stated"; 8.9 row (line 832) "stated (NB-02, NB-08)". The corpus contains no adjudication that these fail the time-t assignment-null criterion, so the agenda clause is an unsupported universal unique to that link of the supersession chain. Finding stands.

## deferred-logged-minors

Fourteen minors logged, not remediated this round (full payloads in the JSON
sidecar; compressed rows in the findings table above):

- **REV-1-3 / LITERATURE-1-4** (consistency / count-integrity, convergent):
  part A's "45 bibliographic query executions" vs 47 prisma-s-1 table rows,
  and the umbrella's non-reconciling "104 queries" — recount from the tables
  and state the counting rule.
- **REV-1-4** (consistency): part B's "four arXiv zeros" vs three zero-record
  table rows.
- **REV-1-5** (reporting): "derived critical values" caveat-free in the
  permanent addendum exceeds the quoted abstract evidence.
- **REV-1-6** (consistency): the addendum enumerates §8.8 but not §10.5's
  restatement of the superseded universal.
- **REV-1-7** (interpretation): the registry-first moral overstates the
  registry's role in the refutation (the refuting family was a registry gap).
- **REV-1-8 / SCOPE-1-2 / LITERATURE-1-5** (interpretation / partial /
  claim-fidelity, convergent): agenda item (b)'s "bounded operational
  definition of range as a temporal state remains unlocated" is ambiguous
  against part A's tier-1 prior sideways/HSMM coverage — define "bounded"
  as an explicit price-bound assignment rule.
- **SCOPE-1-3** (documented-drift): NA-/NB-namespaces vs the spec's
  D-series-continuation wording — note as a deliberate deviation.
- **SCOPE-1-4** (documented-drift): filename-case deviation — assessed per
  the taskSpec's explicit question; declaration sufficient, **no action**.
- **SCOPE-1-5** (omitted): trail and provenance commit pending by design —
  the trail half is discharged by this document.
- **LITERATURE-1-3** (count-integrity): part A synonym-graph "67" vs 66
  counted body rows; propagated 112 vs 111.
- **LITERATURE-1-6** (unpinned-citation): bare "Cochrane Handbook ch. 4"
  citation in the registry methods.

Per project policy, logged minors are carried on the trail and addressed
opportunistically or in a later spec; they do not gate the round verdict.
The 19+4 logged minors from the phase1-sweep spec remain open by policy and
were not re-raised.

## verification-of-remediations

**Prior-spec remediations, verified this round (audit focus f).**
literature-check confirms the agenda's Rev 2 fixes (Benhamou/Codling,
Hall & York, Cheng & Hall, Garzarelli bounded claims) are intact in Rev 3,
and the definitions-survey addendum is append-only with a single addendum
marker and the pre-addendum SHA-256
(b561340781d8bc3de3ce0b7aa18b7d1f75414428fe111c4abaff574e8e2e4464) recorded;
the F005 addendum is untouched. All three branches adopted the standing G16
publisher-403 disposition (handle-API responseCode 1 is the test; per-DOI
logs in both part records) and re-raised no publisher-page fetchability
finding. Registry harvest-provenance discipline verified clean by two
branches independently: no registry entry is cited as evidence in any
downstream artifact. Saturation adjudication verified honest (12 flags
reconcile to 6 swept in-line + 6 logged open with expected-yield rationale) —
the sole defect is the mislocation of the open rows (REV-1-2). The
filename-case deviation was assessed per the taskSpec's explicit question and
needs nothing beyond the existing declarations (SCOPE-1-4).

**This round's remediations (REV-1-1, REV-1-2, SCOPE-1-1, LITERATURE-1-1,
LITERATURE-1-2): pending at trail-writing time.** The round verdict is
proceed-with-remediation; remediation follows this trail. Three of the five
majors (REV-1-1, SCOPE-1-1, LITERATURE-1-2) converge on one defect — the
unwarranted exclusivity clause in agenda item (d) and its branch-3
restatement — and are remediable by a single bounded rewrite applied
consistently across the supersession chain. Verification evidence for the
majors (post-fix artifact digests and, if a round 2 runs, the round-2 branch
confirmations) is to be appended as the next round section of this file —
prior entries are never edited. The /commit-with-provenance step
(SCOPE-1-5's second half) lands after remediation; its trailer-bearing
commit hash is to be recorded here as a dated addendum.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Three specialist branches read six artifacts against the
naming-sweep spec, the standing dispositions, and the cited primary sources;
they did not exhaustively verify every sentence, every citation-claim
pairing, every synonym-graph row, or every cross-artifact dependency.
Absence of a finding is not evidence of absence of a defect — the same
asymmetry the charter enforces for statistical nulls applies to this audit's
coverage.

Per-branch residual-risk statements, verbatim:

**critical-reviewer:** Residual risks after remediation of the above. (1) The entire Phillips date-stamping characterization — and hence the supersession event — rests on abstract-depth verification; the agenda's full-text-pending flag is the correct control, but until that pass runs, the refutation's 'critical values' component is inference (REV-1-5) and branch 3 must not consume the family quantitatively. (2) The registry has not been revised with the 12 flagged families, so the next sweep's instrument still lacks the refuting vocabulary and the six open residuals; the open state is honest in the part records but currently mislocated by the umbrella (REV-1-2). (3) Single-screener, single-harvester throughout — all NONE/zero verdicts are one model's screening judgments over capped retrieval sets, correctly declared as query-conditional but unfalsified by any second reader; Semantic Scholar recall is untested both sweeps. (4) The lowercase filename deviation (regime-naming-a/-b) needs nothing beyond the existing declarations: it is documented at both part-record sites with a concrete gate-grammar rationale, the stores retain the dispatch spelling, and the umbrella frontmatter links resolve — no further action recommended. (5) Checks that passed and are not re-raised: registry tallies (137 head terms, tradition sums), combined flow arithmetic, 112-row graph count, saturation ledger 7+5=12 with 6/6 disposition, harvest-provenance-only discipline (nothing in the registry cited as evidence downstream), predecessor-diff discipline, and the G16 publisher-403 class (closed, dispositioned with per-DOI handle-API logs in both part records). RQI coverage: importance covered (recall correction motivated by two documented in-project failures); originality covered (diff-against-288-identifiers discipline; the refutation and the runs-lineage false-positive correction are genuinely new to the corpus); method, presentation, interpretation covered by findings above.

**scope-auditor:** Bounds on this round's assurance: (1) the append-only claim on the definitions survey rests on the recorded pre-addendum SHA-256 (b5613407...) — this branch has no hashing tool, so byte-identity above the addendum rule was not independently recomputed; a deterministic re-hash before commit closes it. (2) Synonym-graph fidelity was spot-sampled (Wyckoff NA-10a provenance vs registry harvest source, Phillips NB-04/NB-05 abstract quotes, range/sideways rows), not exhaustively verified against all 112 rows' cited sources. (3) The Phillips date-stamping characterization was audited as bounded to abstract depth, per the agenda's own declared caveat — full-text confirmation of the critical-value machinery remains an open verification item the artifacts themselves flag. (4) Coverage is declared-incomplete by design: ~540 registry surface forms vs 104 executed queries, Semantic Scholar unavailable both sweeps, six tier-5 residual families open — all honestly logged, so the omission risk is documented rather than silent, but recall against the unexecuted variants is untested. (5) Registry-honesty verification was grep/spot-based; a systematic cross-check that no vh-harvest-only source id appears in either bibliography store would make finding-category (c) deterministic.

**literature-check:** Verified against primary sources (Crossref works route, arXiv export API/abs pages, OpenAlex abstract reconstruction): ~35 of the 53 included records plus all methodology citations, both Phillips records (venue/volume/pages exact; PSY 2015 abstract confirms 'real-time date-stamping'; PWY 2011 abstract confirms recursive date-stamping but the words 'real time' and 'critical values' are not verbatim in its abstract — the artifacts' abstract-depth caveat and full-text-pending flag cover this, so it is not raised as a finding, but the flagged full-text pass is load-bearing before branch 3 cites critical values quantitatively). Not independently verified: the remaining Wiley chapter DOIs and dedup-ledger twin identifiers (all spot-checks clean; per-DOI handle logs exist), the SHA-256 digests (bibliography stores, pre-addendum survey hash — no hashing tool in this branch; quant-auditor scope), the search-log JSONs' query-by-query contents, and the 2026 SSRN/IEEE Access records' venue quality (declared as unrefereed/weak-venue in the artifacts themselves). G16 publisher-403 class not re-raised per standing disposition. Registry harvest-provenance discipline checked and clean: no registry entry is cited as evidence in any downstream artifact. Saturation adjudication verified honest (12 flags reconcile to 6 swept in-line + 6 logged open with rationale). Filename-case deviation is declared in both part records and needs nothing beyond the declaration. Rev 2 remediations (Benhamou/Codling, Hall & York, Cheng & Hall, Garzarelli bounded claims) are intact in the agenda; the definitions-survey addendum is append-only with a single addendum marker and the pre-addendum hash recorded.

**Prior dispositions carried into this round** (verbatim from the round
payload): Fresh cap for naming-sweep spec. Standing project dispositions: G16 DOI publisher-403 false-positive class closed — handle-API responseCode 1 is the resolution test (five predecessor reviews carry identical dispositions with logs). F-5: aggregate-only verification inadmissible — per-site/per-cluster checks required. Register/living-doc convention: strike-don't-delete, append-only addenda, revision notes. Prior naming-relevant history: the regime-definitions survey (predecessor) failed on recall for vocabulary reasons — the F005 headline fell the same way — so unbounded universals from bounded coverage are the session's named hazard; the agenda Rev 2 REV-1-1 finding (bounded-universal overreach) documents the required phrasing discipline. 19+4 logged minors from the phase1-sweep spec remain open by policy, not re-raised.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Fable 5 (model id `claude-fable-5`, Anthropic) — all
  branches: three specialist audit agents (critical-reviewer at high effort,
  scope-auditor at medium effort, literature-check at high effort, each with
  `model: inherit` in its agent definition), the adversarial refuter (high
  effort), and the trail-assembly agent that authored this document.
- Roles: audit (findings, refutations, verification of the naming-sweep
  integrations, the supersession chain, and the registry discipline) and
  prose (assembly of this trail). No authored research content; the audited
  artifacts were not modified by this round's agents.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the verdict and remediations proceed.
- Reproducibility log: ReproLog emission is sequenced with the
  /commit-with-provenance step (SCOPE-1-5); the log lands at
  `logs/reproducibility/repro_log_{run_id}.json` (gitignored), and its
  clone-durable digest is carried by the commit's `Repro-Log-Path:` /
  `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility contract. The
  commit hash is to be recorded here as a dated addendum when it lands.

## immutability-and-retention

This trail and its JSON sidecar
([audit_trail_naming-sweep_2026-08-24.json](audit_trail_naming-sweep_2026-08-24.json),
SHA-256 `fffba9ee9cb8130ffd1ae7889d91090324f905b79006958af08cec698af69b48`,
holding the round-1 payload verbatim per FAIR I1) are committed to the
repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. Later rounds of this loop append
new round sections to this file; corrections to any recorded entry are
appended as a dated addendum that identifies what it corrects — prior entries
are never edited, overwritten, or deleted. Retention follows the repository's
git history; the tracked file is the durable record, and the front-matter
digests bind it to the exact artifact states audited.

---

# Audit trail — Naming sweep, round 2

Appended round section per 21 CFR 11.10(e): the round-1 entries above are
unmodified. Round 2 is a verify-only round over the five round-1 retained
majors (REV-1-1, REV-1-2, SCOPE-1-1, LITERATURE-1-1, LITERATURE-1-2 — three
of which name one defect, the agenda's exclusivity clause). All three branch
verdicts: **accept**. Union verdict: **accept**. Zero critical/major findings
raised; five new minors logged; the refute gate had nothing to gate.

The file-level YAML front matter at the top of this document is the round-1
record and is not edited; the round-2 front matter is carried verbatim in the
fenced block below (and, as JSON, in the round-2 sidecar).

```yaml
schema_version: "WI-3/2"
conforms_to:
  - "PROV-DM / PROV-O"
  - "RO-Crate 1.1"
  - "ISO 19011:2018"
  - "FAIR (Wilkinson et al. 2016, doi:10.1038/sdata.2016.18)"
  - "Sandve et al. 2013 (doi:10.1371/journal.pcbi.1003285)"
  - "21 CFR 11.10(e)"
  - "ICMJE §V.A"
title: "Audit trail — Naming sweep, round 2"
type: audit_trail
date: "2026-08-24"
started_at: "2026-08-24T09:42:39-05:00"
ended_at: "2026-08-24T09:44:49-05:00"
artifacts:
  - {path: "docs/literature/vocabulary_regime-synonyms_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "3989b61e7f0b7d04b2f860860da329ea5a14e62ffc1dc3cd3ba6ec0f50ba7c25"}
  - {path: "docs/literature/lit_review_regime-naming_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "c1320a718de05745f2bc2842f6483577db9aaff3447a877ce95c445b3d7fbf1a"}
  - {path: "docs/literature/lit_review_regime-naming-a_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "54498e736beb718a1aee305296398adebc37bcf90ccd0056e1e61eada867e111"}
  - {path: "docs/literature/lit_review_regime-naming-b_2026-08-24.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "015e95509b388cf9071e730f42a2e4447ea95f09751561885722abaa4bfe7564"}
  - {path: "docs/literature/lit_review_regime-definitions_2026-08-21.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "ac64dcebfea3f548cb839fcc27ea9dc5889ff0644fb453bfba5a899a299c3bb4"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "0845acbf5d464cd330c93941c3af1bf000f3791d", sha256: "07a6646ff9ec994cada89b416cf1268536acddd7fe4e2cd287738174e8f56507"}
repo_head: "0845acbf5d464cd330c93941c3af1bf000f3791d"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    Round 2 (verify-only) of the naming-sweep loop (deliverable_spec_naming-sweep_2026-08-24.md). Round 1 retained five majors, all now remediated: REV-1-1 / SCOPE-1-1 / LITERATURE-1-2 (one defect, three findings — the agenda's unbounded exclusivity clause) — agenda item (d) now reads: bounded survivor for the 59 surveyed definitions, then 'Outside the explosive family, no other located vocabulary was classified by the sweeps as carrying a time-t assignment null — but the nearest candidates are unadjudicated, not absent: drawdown/drawup episodes (NB-02/NB-08) and flight-to-quality (NB-13) attach stated nulls at filtered causality and were screened only at abstract depth; whether their nulls attach to the assignment procedure itself awaits the full-text pass'; branch 3's restatement now reads 'the only detector the sweeps classified as carrying its own time-t assignment null (nearest unadjudicated candidates at abstract depth: NB-02/NB-08 drawdown episodes, NB-13 flight-to-quality)'. REV-1-2 — the term registry now carries a 2026-08-24 post-sweep append-only addendum registering all 12 flagged families as rows (6 swept-in-line with record pointers, 6 open with the tier-5 zero-yield rationale; variant generation explicitly deferred to the sweeping round), and the umbrella's saturation sentence was corrected to point at that addendum and the part-record flags. LITERATURE-1-1 — part A line 481 prose corrected from 'Ige (2024)' to 'Pal (2024)' with a bracketed dated correction note citing the audit finding, the arXiv export API, and the id-stability decision (store id ige2024arxiv240318839 retained, store entry was already correct). VERIFY ONLY: (a) each remediation present and adequate against its fix specification; (b) the supersession chain is now consistent — addendum, umbrella §3, and agenda (d) carry compatible bounded survivors (the agenda's additional sentence is bounded to what the sweeps classified and names its unadjudicated candidates, which the fix specifications permitted as option two); (c) no new defect in the edit vicinities; (d) the registry addendum is append-only (nothing above its rule edited) and its 12 rows reconcile with part A §8.4 + part B §8.7. DO NOT re-raise: the 14 round-1 logged minors (deferred per invitesPolish=false); the G16 class; the abstract-depth caveat on the Phillips records (already the artifacts' own declared control); terminal bookkeeping (spec ticks, ReproLog, commit — sequenced after accept).
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_naming-sweep_2026-08-24.md", sha256: "06362dc88247cbe9db93eda9dfb434c2413fddfa7798eebbb005e90392142533"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill). Round 2 is a verify-only round; zero critical/major findings, so the refute gate was not exercised."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-fable-5", effort: "medium", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Fable 5, claude-fable-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, literature-check) → trail-assembly agent (this round section)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js; identical branch set to round 1 for continuity of verification (all six artifacts remain markdown prose — quant-auditor and epi-auditor not routed). critical-reviewer (adequacy of the five remediations against their fix specifications, supersession-chain consistency, no-new-defect vicinity check, registry-addendum reconciliation) high; scope-auditor (remediation-vs-fix-specification fidelity, append-only structural check, spec traceability) medium; literature-check (primary-source re-verification of the corrected and load-bearing citations: Pal/arXiv:2403.18839, Phillips-Wu-Yu 2011, Phillips-Shi-Yu 2015; supersession-chain and addendum-row reconciliation) high."
rounds_completed: 2
rounds_cap: 3
cap_reached: false
verdict: "accept"
counts: {raw_critical: 0, raw_major: 0, raw_minor: 5, refuted: 0, retained_conservative: 0, to_remediate: 0, minors_logged: 5}
sidecar: {path: "docs/audits/audit_trail_naming-sweep_2026-08-24.round2.json", sha256: "1ca94bbf4685ffc09b97b2ffbec23286b6a491b80842a6bf20722ad25acef64a"}
```

Notes on the round-2 record: `started_at`/`ended_at` are the trail-assembly
interval for this round section. Part B and the definitions survey digests
are unchanged from round 1 (`015e9550…`, `ac64dceb…`); the four artifacts
touched by the five remediations moved — the registry from `56b54aaa…` to
`3989b61e…` (post-sweep addendum), the umbrella from `0bf877a8…` to
`c1320a71…` (saturation-sentence correction), part A from `fd23e6d3…` to
`54498e73…` (Ige→Pal correction note), and the agenda from `7032ba09…` to
`07a6646f…` (bounded exclusivity clause and branch-3 restatement). The
round-2 sidecar is a separate sibling file so that the round-1 sidecar
(whose SHA-256 is bound into the round-1 front matter above) remains
byte-identical, per append-only retention.

## findings-table

Round 2 raised zero critical and zero major findings and five minors, all
logged not remediated. The counts object, verbatim from the round payload:
raw_critical 0, raw_major 0, raw_minor 5, refuted 0, retained_conservative 0,
to_remediate 0, minors_logged 5. One row per finding; all eight schema fields
plus branch and disposition (the sidecar carries the identical payload in
JSON, including the exact multi-line text that table cells flatten). Two
convergent pairs: REV-2-1/LITERATURE-2-1 name one defect (the umbrella §4
rationale clause vs the new addendum row for "technical range"), and
REV-2-2/LITERATURE-2-3 name one defect (no pre-addendum digest pinned in the
registry addendum).

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-2-1 | minor | consistency | umbrella:122-127 vs registry:467 | Umbrella §4's open-families bullet characterizes all six open families — including "technical range" — as tier-5 ICT/Wyckoff-adjacent zero-yield vocabulary; the new registry addendum row (correctly) classifies "technical range" as an academic near-miss on a single-source flag (E1, an OMICS-venue exclusion) — a characterization mismatch created by the remediation's pointer | Umbrella: '…"technical range" — all tier-5 ICT/Wyckoff-adjacent micro-vocabulary…yield was zero' vs addendum row 'academic near-miss…open — not swept (single-source flag, part A)' | Qualify the umbrella §4 rationale clause: five tier-5 zero-yield families plus "technical range" as an academic near-miss on E1; one-line edit, addendum unchanged | CHAMP item 19; SAMPL (a quantity appearing twice must agree) | critical-reviewer | deferred — logged minor |
| REV-2-2 | minor | verification-gap | registry:446-452 | Registry addendum asserts append-only ('no entry above this rule edited') but, unlike the definitions-survey addendum precedent, pins no pre-addendum SHA-256, so the claim is not mechanically verifiable from the artifact alone; criterion (d) verified by internal corroboration (unchanged §5 tallies of 137 head terms; none of the 12 families in the §2 body; drawdown still spatial-only in §2.4), not a digest check | Registry addendum preamble vs definitions addendum's pinned pre-addendum SHA-256 b5613407… (definitions:1241-1242) | Add the pre-addendum SHA-256 to the addendum header, recoverable from the registry blob at the last pre-addendum commit | Project reproducibility contract; CHAMP item 22 | critical-reviewer | deferred — logged minor |
| LITERATURE-2-1 | minor | misattributed-rationale | umbrella:121-128 (§4, open-families bullet) | The sentence immediately preceding the REV-1-2 remediation lumps "technical range" into the tier-5 ICT/Wyckoff zero-yield rationale; the remediated addendum row and part A both give the accurate rationale: academic near-miss, single-source flag (E1, in the range cluster where academic yield was not zero) | Umbrella §4 bullet vs addendum row vs part A E1 and §8.4 item 7; possible overlap with the 14 round-1 logged minors, flagged for sitting in the direct edit vicinity | Carve "technical range" out of the tier-5 rationale in umbrella §4, holding it open on the single-source flag (part A, E1) | registry addendum table; naming-a §6 E1, §8.4 | literature-check | deferred — logged minor |
| LITERATURE-2-2 | minor | residual-misattribution-in-audit-trail | search_logs/regime-naming/swA-doicheck-02.json:21 | The doicheck log entry for 10.48550/arXiv.2403.18839 still annotates the record as "Ige (arXiv q-fin.TR 2024) via export.arxiv.org" — the misattribution corrected by LITERATURE-1-1 — in the very log cited as the DOI-verification trail; the export API returns sole author Jai Pal (re-verified this round) | swA-doicheck-02.json line 21 vs arXiv export API id_list=2403.18839 (author Jai Pal) | Do not edit the log line (immutable-record convention); add an append-only annotation or sibling note pointing at the part A line 481 correction | https://export.arxiv.org/api/query?id_list=2403.18839 | literature-check | deferred — logged minor |
| LITERATURE-2-3 | minor | verification-gap | registry:446-452 (addendum preamble) | Registry addendum asserts append-only but, unlike the sibling addendum in the definitions survey, records no pre-addendum SHA-256; the assertion rests on git history. Content-level spot checks clean: §5 tallies still match table row counts (§2.1 = 11 rows, §2.2 = 12 rows); addendum rows correctly excluded from §5 tallies | Registry addendum preamble carries no digest vs definitions addendum pinning b5613407… | Record the pre-addendum SHA-256 (or pre-addendum git blob hash) in the addendum preamble to make the claim self-verifying | definitions:1241-1242 | literature-check | deferred — logged minor |

## refute-gate

No critical or major findings were raised in round 2, so no disposition
reached the adversarial refute gate (`refute_gate_dispositions: []`). There
are no dropped, retained, or retained-conservative entries, and no entry with
`reproduction_required: true`, so no `reproduction: {command, observed}`
blocks are owed. The gate's standing rule is unchanged: drop requires concrete
counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)).

## deferred-logged-minors

Five new minors logged in round 2 (`minors_logged: 5`), none remediated this
round (full schema fields in the findings table above and the round-2
sidecar):

- REV-2-1 / LITERATURE-2-1 (critical-reviewer / literature-check, convergent;
  umbrella §4 vs registry addendum) — the pre-existing umbrella rationale
  clause lumps "technical range" into the tier-5 ICT/Wyckoff zero-yield
  stratum, conflicting with the (correct) academic-near-miss classification
  in the addendum row the remediated sentence now points at.
- REV-2-2 / LITERATURE-2-3 (critical-reviewer / literature-check, convergent;
  registry addendum preamble) — the addendum's append-only assertion pins no
  pre-addendum SHA-256, unlike the definitions-survey precedent, so it is not
  self-verifying from the artifact alone.
- LITERATURE-2-2 (literature-check; swA-doicheck-02.json:21) — the "Ige"
  misattribution persists in one tracked search-log annotation; fix is an
  append-only annotation, never an edit of the log line.

The fourteen round-1 minors remain open in this trail per
`invitesPolish=false` — deferred by protocol, not missed — and were excluded
from re-raising by the round-2 task spec, as were the G16 class, the
abstract-depth caveat on the Phillips records (the artifacts' own declared
control), and the terminal bookkeeping items (sequenced after accept).
SCOPE-1-5's trail half stands discharged by this round section; its
provenance-commit half remains sequenced with the terminal bookkeeping phase.

## verification-of-remediations

All five round-1 retained majors are verified remediated, per branch and
against each finding's fix specification:

- **REV-1-1 / SCOPE-1-1 / LITERATURE-1-2 — remediated (one defect, option
  two of the fix specifications).** Agenda item (d) now carries the bounded
  survivor for the 59 surveyed definitions followed by the explicitly bounded
  exclusivity sentence ("no other located vocabulary was classified by the
  sweeps as carrying a time-t assignment null") naming its unadjudicated
  candidates (NB-02/NB-08 drawdown/drawup episodes, NB-13 flight-to-quality,
  stated nulls at filtered causality, abstract-depth screening, adjudication
  deferred to the full-text pass); branch 3's restatement carries the
  matching parenthetical. critical-reviewer confirms the sentence is accurate
  against part B's own extraction table; literature-check confirms the chain
  (definitions addendum, umbrella §3, agenda (d)) now carries compatible
  bounded survivors matching part B's inventory (only NB-04/NB-05 described
  as a null attached to the assignment procedure itself); scope-auditor
  confirms the delivered sentence matches the round-1 fix specification
  verbatim, noting only that the plural "attach stated nulls at filtered
  causality" is exact for NB-02 and NB-13 while NB-08 is a pure
  null-apparatus record with causality n/a — spec-conformant, not drift, and
  self-correcting via the same sentence's full-text deferral.
- **REV-1-2 — remediated (registry-addendum option).** The registry carries
  a 2026-08-24 post-sweep append-only addendum registering all 12 flagged
  families as rows — 6 swept-in-line with record pointers, 6 open with
  rationale, variant generation explicitly deferred to the sweeping round —
  reconciling exactly with part A §8.4 items 1-7 plus part B §8.7 items 1-5
  (verified independently by critical-reviewer and literature-check); the
  umbrella's saturation sentence now points at the addendum and the
  part-record flags. Append-only status verified structurally and
  content-level (unchanged §5 tallies, no family present in the §2 body);
  the absence of a pinned pre-addendum digest is logged as
  REV-2-2/LITERATURE-2-3 (minors).
- **LITERATURE-1-1 — remediated (id-stability option).** Part A line 481
  prose corrected from "Ige (2024)" to "Pal (2024)" with a bracketed dated
  correction note citing the audit finding, the arXiv export API, and the
  id-stability decision (store id ige2024arxiv240318839 retained; both CSL
  stores were already correct). literature-check re-verified against the
  export API (sole author Jai Pal). Residual "Ige" strings survive only in
  the immutable audit trail and harvest log where they belong; the one
  tracked search-log annotation still carrying the misattribution is logged
  as LITERATURE-2-2 (minor, append-only annotation owed, never an edit).
- **No new critical/major defect in the edit vicinities; no regression
  elsewhere.** The two vicinity findings (REV-2-1/LITERATURE-2-1 and
  REV-2-2/LITERATURE-2-3) are presentation- and verification-level and touch
  no conclusion. literature-check additionally re-verified the two
  load-bearing Phillips citations against Crossref (PWY 2011, Int Econ Rev
  52(1):201-226, doi:10.1111/j.1468-2354.2010.00625.x; PSY 2015, Int Econ
  Rev 56(4):1043-1078, doi:10.1111/iere.12132) exactly as cited in the
  agenda (d) and umbrella §3 edits.

Branch verdicts, verbatim from the round payload: critical-reviewer accept,
scope-auditor accept, literature-check accept. Union verdict: **accept**, at
rounds_completed 2 of rounds_cap 3 (`cap_reached: false`).

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Round 2 was a verify-only round focused on the five
remediated passages, their vicinity, the supersession chain, and the
registry-addendum reconciliation; it did not exhaustively re-audit every
sentence, citation-claim pairing, store record, or cross-artifact
dependency. Absence of a finding is not evidence of absence of a defect —
the same asymmetry the charter enforces for statistical nulls applies to
this audit's coverage.

Per-branch residual-risk statements, verbatim:

**critical-reviewer:** All five round-1 majors are verified remediated to their fix specifications: the agenda's exclusivity clause is now a bounded survivor whose unadjudicated-candidate sentence is accurate against part B's own extraction table (NB-02/NB-08 and NB-13 carry stated nulls at F-class causality, screened at abstract depth, assignment-attachment genuinely open); the branch-3 restatement carries the matching parenthetical; the registry addendum registers all 12 flagged families (7 from part A §8.4, 5 from part B §8.7 — exact reconciliation) with correct record pointers and a preserved variant-provenance discipline; the umbrella saturation paragraph points at the addendum; and the Ige-to-Pal correction is present with all three required citations, residual 'Ige' strings surviving only in the immutable audit trail and harvest log where they belong. The supersession chain (survey addendum, umbrella §3, agenda (d)) is consistent. Residual risks, none blocking: (1) the two minors above; (2) part A §8.4 item 8's collision-ledger additions (Climax granite homonym; OpenAlex hyphen failure on 'one-time framing') are flagged in the part record but not yet appended to the registry's §3 homonym ledger — the fix specification did not require this and the next sweeping round will consult the part records, but the registry-as-instrument is one step behind its flags on collisions as it no longer is on families; (3) the whole classification distinction the bounded survivor now rests on ('null attaches to the assignment procedure' vs 'null attaches at filtered causality') is adjudicable only at the full-text pass the artifacts themselves schedule — until that pass runs, the explosive family's uniqueness claim is a classification of abstract-depth evidence, which the artifacts state plainly; (4) append-only status of the registry addendum was corroborated internally, not digest-verified (REV-2-2). Terminal bookkeeping (spec ticks, ReproLog, provenance commit) remains sequenced after accept per the task spec.

**scope-auditor:** Two limits on this verify-only pass. (1) Append-only verification of the registry addendum was structural, not byte-level: this branch has no shell access, so "no entry above the rule edited" was checked by placement and content consistency (family counts, tradition tallies at lines 440-442 still summing as before) rather than a git diff against the pre-remediation blob; the terminal bookkeeping stage should let the deterministic append-only check (already listed under Self-executed in the spec) confirm byte-identity. (2) The agenda's plural phrasing "attach stated nulls at filtered causality" is exactly precise for NB-02 and NB-13 but NB-08 is a pure null-apparatus record with causality n/a per part B's own table; the delivered sentence matches the round-1 fix specification verbatim, so this is not drift, and the imprecision is self-correcting because the same sentence defers adjudication to the full-text pass. The open items the artifacts themselves declare (6 unswept families, S2 outage recall gap, abstract-depth screening) are documented drift within the spec's own saturation-adjudication clause, not findings.

**literature-check:** All five round-1 majors are verified remediated, with the two load-bearing external citations re-verified against primary sources this round: arXiv export API confirms sole author Jai Pal for 2403.18839 (LITERATURE-1-1 correction factually right; both CSL stores already correct), and Crossref confirms Phillips, Wu & Yu 2011 (Int Econ Rev 52(1):201-226, doi:10.1111/j.1468-2354.2010.00625.x) and Phillips, Shi & Yu 2015 (Int Econ Rev 56(4):1043-1078, doi:10.1111/iere.12132) exactly as cited in the agenda (d) and umbrella section 3 edits. The supersession chain (regime-definitions addendum, umbrella section 3, agenda (d)) carries compatible bounded survivors, and the agenda's exclusivity sentence is now bounded to what the sweeps classified, matching part B's own inventory (only NB-04/NB-05 described as a null attached to the assignment procedure; NB-02/NB-08 and NB-13 correctly held as unadjudicated at abstract depth). The addendum's 12 rows reconcile exactly with part A section 8.4 items 1-7 plus part B section 8.7 items 1-5. Remaining risks, all declared in the artifacts or deferred by design: Phillips content claims rest on abstract-level verification pending the flagged full-text pass before branch-3 quantitative use; whether NB-02/NB-08/NB-13 nulls attach to the assignment procedure awaits that same pass; append-only status of the registry addendum is verified content-level and by git history only (no pinned pre-addendum digest, LITERATURE-2-3); the misattribution persists in one tracked search-log annotation (LITERATURE-2-2). None of the three new minors blocks acceptance; per invitesPolish=false they can be logged alongside the 14 deferred round-1 minors.

**Prior dispositions carried into this round** (verbatim from the round
payload): Round 1 (this spec): 3 branches, all proceed-with-remediation; 5 majors retained through the refute gate — REV-1-1/SCOPE-1-1/LITERATURE-1-2 (agenda exclusivity clause, one defect thrice-found), REV-1-2 (umbrella misdescribed registry state), LITERATURE-1-1 (Ige→Pal author misattribution) — all remediated per taskSpec; 14 minors logged not remediated per invitesPolish=false. Standing: G16 closed on handle-API evidence; F-5 aggregate-only verification inadmissible; append-only/strike-don't-delete conventions; bounded-universal phrasing discipline is the session's named hazard, now enforced twice.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Fable 5 (model id `claude-fable-5`, Anthropic) — three
  specialist audit agents (critical-reviewer at high effort, scope-auditor at
  medium effort, literature-check at high effort, each with `model: inherit`
  in its agent definition) and the trail-assembly agent that authored this
  round section. No refuter was invoked this round (zero critical/major
  findings).
- Roles: audit (verification of the five round-1 remediations against their
  fix specifications, supersession-chain and registry-addendum checks,
  vicinity and regression checks) and prose (assembly of this round section).
  No authored research content; the audited artifacts were not modified by
  this round's agents.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the accept verdict proceeds.
- Reproducibility log: ReproLog emission is sequenced with the
  /commit-with-provenance step (terminal bookkeeping after accept); the log
  lands at `logs/reproducibility/repro_log_{run_id}.json` (gitignored), and
  its clone-durable digest is carried by the commit's `Repro-Log-Path:` /
  `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility contract. The
  commit hash is to be recorded here as a dated addendum when it lands.

## immutability-and-retention

This round section and its JSON sidecar
([audit_trail_naming-sweep_2026-08-24.round2.json](audit_trail_naming-sweep_2026-08-24.round2.json),
SHA-256 `1ca94bbf4685ffc09b97b2ffbec23286b6a491b80842a6bf20722ad25acef64a`,
holding the round-2 payload verbatim per FAIR I1) are committed to the
repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. This round-2 section was
appended without editing, overwriting, or deleting any round-1 entry; the
round-1 sidecar is likewise untouched, preserving the SHA-256 bound into the
round-1 front matter. Corrections to any recorded entry are appended as a
dated addendum that identifies what it corrects. Retention follows the
repository's git history; the tracked file is the durable record, and the
round-2 artifact digests above bind this record to the exact artifact states
verified.

---

# Addendum — provenance commit landed (2026-08-24)

Appended per 21 CFR 11.10(e); no prior entry edited. Completes the terminal
bookkeeping phase sequenced after the round-2 accept.

- Commit: `5671a86538f6516b11fae0c494cefc3bc077515f` on `main`
  ("docs(naming): vocabulary-first naming re-sweep; agenda rev 3; time-t-null
  universal superseded") — 154 files: term registry with post-sweep addendum,
  umbrella + two part records, three stores (53 merged entries), 141 search
  logs, the definitions-survey supplement addendum, agenda rev 3, the
  deliverable spec, and this trail with both sidecars.
- Trailers, verbatim from `git log -1`:
  - `Repro-Log-Path: logs/reproducibility/repro_log_8584befb1b0646f18e68fbce3b25eb9e.json`
  - `Repro-Log-SHA256: bdb5a8bc07636af5ac4bab4de58ff6077dea975fc407dc2ebb332fa695973c14`
  - `AI-Assistance: claude-fable-5 (role=multi)`
- Deterministic pre-commit checks recorded: store counts 22/31/53 with zero
  id/DOI collisions; every merged id resolves in a part record; the
  definitions-survey addendum verified append-only at BYTE level (prefix
  hashes to the recorded pre-addendum SHA-256 `b5613407…`) — closing the
  structural-only limitation both round-2 read-only branches declared.
- Open items handed forward: 19 round-1 + 5 round-2 logged minors (deferred
  per invitesPolish=false), including the registry addendum's missing
  pre-addendum digest (unrecoverable — the registry was never committed
  pre-addendum; its first committed state includes the addendum, so git
  history is the integrity carrier from here), the technical-range rationale
  mismatch in umbrella §4, and the swA-doicheck-02 log's residual "Ige"
  annotation (immutable log; corrected in part A prose). The full-text pass
  on the Phillips records remains the load-bearing precondition before
  branch 3 uses their critical values quantitatively. Six registry families
  remain open/unswept.
- This addendum and the spec's commit-box tick are committed separately as
  closure bookkeeping.
