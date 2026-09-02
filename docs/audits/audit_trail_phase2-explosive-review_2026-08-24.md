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
title: "Audit trail — Phase 2 explosive-regime review close-out, round 1"
type: audit_trail
date: "2026-08-24"
started_at: "2026-09-02T09:41:12-05:00"
ended_at: "2026-09-02T10:58:44-05:00"
artifacts:
  - {path: "docs/literature/lit_review_explosive-regime-dating_2026-08-24.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "4dd5a3f65057a8b84f90dd8b7ca86013bb355ea555f0f476e8caa3a607b1d364"}
  - {path: "docs/literature/references_explosive-regime.json", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "1abbb9d8b253ff2d10c5f021205101ab4bd610812ffd75d8f6bdcde024bbb7dc"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "7e29fcdea2087d9852f4080320881688ba654fa2ded90f6cc3f88f8c6f99bcc6"}
repo_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A — Phase 2 explosive-regime review close-out. Item 1: PRISMA 2020 review over the frozen 72-record included corpus: flow accounting (identified/screened/excluded-with-reasons/included) reconciling with the search logs and kappa records; one appraisal row per included study using the protocol's declared instrument; synthesis of operating characteristics and validity conditions; full-text extraction for BOTH Phillips records discharging the branch-3 precondition; explicit adjudication of NB-02, NB-08 and NB-13 against the time-t assignment-null standard; publication-bias posture per protocol; limitations mapping residual PRISMA gaps. Item 2: agenda rev 4 — branch 3 integrates the review's verdicts; every 'full-text pass pending' caveat discharged or corrected at each site (Definitional basis (d), branch 3, Verification status); supersession markers added wherever a Rev 3 claim falls. FOCUS FOR THIS ROUND: (a) protocol-vs-execution fidelity against the frozen protocol docs/methodology/protocol_explosive-regime-review_2026-08-24.md sha256 33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54, registration commit 9deee0c; (b) whether the review's flow numbers actually reconcile against the primitive verdict files in docs/literature/search_logs/explosive-regime/ rather than being copied from se-included-set.json; (c) appraisal honesty — 72 ER-RoB rows, the dagger/double-dagger conservative-resolution convention, and whether single-pass rows are marked as such; (d) the Phillips confirm-or-correct verdict (review section 8.3): is 'in real time' correctly restricted to ADF_r/BSADF and denied to SADF/GSADF, and is 'against derived critical values' correctly denied on the ground that operating critical values are Monte Carlo simulated; (e) the three NB adjudications (section 9) — NB-02 Johansen & Sornette, NB-08 Landriault/Li/Zhang, NB-13 Baur & Lucey, all returned episode-statistic-null; NB-13's verdict rests on a working paper plus abstract after the journal version proved unobtainable; (f) the review's OWN self-reported defects — backward citation-chasing arm er-bc-* never executed, protocol section 4.3 dual-extraction reconciliation never ran with 90/357 divergent cells resolved by a post-hoc conservative rule, five included records failing eligibility criterion I3 as written, three same-work twin pairs surviving deduplication, and post-hoc amendments A4/A5/A6 — are these disclosed with the right severity and are the review's conclusions correctly bounded by them, or does the review state conclusions its recall-limited corpus cannot carry; (g) whether the agenda Rev 4 transcription faithfully carries the review's verdicts without overstating them, in particular that universal (d) remains refuted while the Rev 3 sentence's strength falls, and that the corpus recall limitation is carried into the agenda rather than dropped.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md", sha256: "f3160c5eba1e7bbd2f8a19156eb1f36218b94ff5ac89b7cdae338461d9ea691b"}
    - {path: "docs/methodology/protocol_explosive-regime-review_2026-08-24.md", sha256: "c5a4be8d84241f0ea34dfc0f6e08a0c88ee5d4f81d05a6edd934e5db7fb72721"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill)."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "quant-auditor", agent_def_path: "~/.claude/agents/quant-auditor.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-opus-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Opus 5, claude-opus-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, quant-auditor, literature-check) → adversarial refuter → trail-assembly agent (this document)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. Four branches routed. critical-reviewer (design, conduct, interpretation, RQI dimensions) and scope-auditor (declared-spec coverage against deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A, and protocol-vs-execution presence) are unconditional. quant-auditor routed on focus items (b) and (c) — the flow identities, the kappa computation, the 72-row ER-RoB table and the dagger convention are arithmetic reconciliations against primitive verdict files, not prose checks. literature-check routed on focus items (d) and (e) — the Phillips confirm-or-correct verdict and the three NB adjudications are citation- and source-fidelity claims. epi-auditor was not routed (no population-health artifact, no human-subjects data). Efforts: critical-reviewer high, scope-auditor medium, quant-auditor high, literature-check high."
rounds_completed: 1
rounds_cap: 3
cap_reached: false
verdict: "proceed-with-remediation"
counts: {raw_critical: 0, raw_major: 27, raw_minor: 21, refuted: 3, retained_conservative: 0, to_remediate: 24, minors_logged: 21}
sidecar: {path: "docs/audits/audit_trail_phase2-explosive-review_2026-08-24.json", sha256: "221d4f241b04bba99af67097508e221eba9cc26207add417bd7bdb6bfd8d96ca"}
---

# Audit trail — Phase 2 explosive-regime review close-out, round 1

Round 1 of a fresh 3-round cap opened by
[deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md](../deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md)
Thread A. Audited artifacts: the PRISMA 2020 explosive-regime-dating review, its
72-record CSL-JSON included-corpus store, and the Rev 4 regime-classification
agenda (worktree versions at HEAD `27d7473`, all three uncommitted or modified —
`worktree_clean: false`; artifact digests in the front matter and the JSON
sidecar). The frozen protocol
[protocol_explosive-regime-review_2026-08-24.md](../methodology/protocol_explosive-regime-review_2026-08-24.md)
(registration digest `33c01c522521…`, commit `9deee0c`; on-disk A1–A3 addendum
digest `c5a4be8d…`) was the primary conformance criterion.

Branch verdicts: critical-reviewer proceed-with-remediation, scope-auditor
proceed-with-remediation, quant-auditor proceed-with-remediation,
literature-check proceed-with-remediation. Round verdict:
**proceed-with-remediation** (0 critical, 27 majors raised, 3 refuted at the
gate, 24 majors retained for remediation, 21 minors logged, 0 retained-conservative).
Full finding payloads, refute-gate dispositions, and per-branch residual-risk
statements are held verbatim in the JSON sidecar
([audit_trail_phase2-explosive-review_2026-08-24.json](audit_trail_phase2-explosive-review_2026-08-24.json),
SHA-256 `221d4f24…`); the sections below carry the required record.

Two focus items verified clean and produced no finding: focus (b) — the flow
identities, all eight JSONL row counts, the stage-1/stage-2 verdict marginals
and the kappa 2×2 (κ = 0.433012, p₀ = 0.806613, pₑ = 0.658923) reconcile exactly
against the primitive verdict files, independently in two branches — and the
dagger half of focus (c) — exactly 90 Q-cell daggers with the stated per-question
distribution (Q1 6 / Q2 7 / Q3 3 / Q4 23 / Q5 14 / Q6 12 / Q7 25). Focus (d) also
held on the merits: the restriction of "in real time" to ADF_r/BSADF and its
denial to SADF/GSADF is grounded in verbatim authorial statements from both
Phillips papers, and the denial of "against derived critical values" on
Monte-Carlo provenance is sound — the attempt to overturn it (LITERATURE-1-3) was
refuted at the gate.

## findings-table

One row per finding. All eight schema fields (id, severity, category, location,
issue, evidence, fix, reference) plus branch and disposition; issue/evidence/fix
are compressed for tabular legibility — the full verbatim text of every finding
is in the JSON sidecar, and every major's claim is reproduced verbatim and
unabridged in the refute-gate section below.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-1-1 | major | design | review:2007-2029 (§12.5); protocol:748-767 (§10) | A4/A5/A6 described in the review but never appended to the frozen protocol's append-only addendum, which still ends at A3; deferral to a "consumer session" leaves the registration carrier inconsistent with executed conduct at ship time | "the consumer session should append them" | Append A4-A6 dated, with stage and PRISMA-P item, in the shipping commit; update protocol_sha256_with_addendum; else declare the record incomplete and log a VG | Protocol §10; PRISMA 2020 item 24c; CHAMP item 6 | critical-reviewer | retained → remediate |
| REV-1-2 | major | consistency | review:667-691 (§5.1), 1864-1870 (L-6), 1958 (VG-8); references_explosive-regime.json | I3-failure count is seven, not five: 62 DOIs + 2 arXiv + 1 Handle = 65 of 72 identified; twins eru-0154 and eru-0904 omitted; undercount propagates to the conformance map and the agenda | "**Five included records have no DOI, no arXiv ID and no Handle**" | Correct to seven at all five sites; add I3 GAP notes and best locators to the two twin entries; state that a carrier's DOI is not the twin's identifier | Protocol §2.2 I3; PRISMA 2020 items 5, 27; SAMPL | critical-reviewer | retained → remediate |
| REV-1-3 | major | reporting | review:788-793, 796-869, 876-925 (§6/§6.1); protocol:526-529 (§6) | Domain-concern column not derived by the frozen Q→D rule; deviation described as "a few cells" while affecting a large minority (13 D3 rows, 6 D4 rows); feeds §6.1 distributions and three abstract claims | "a few cells are consequently less concerning than a mechanical map would give" | Add a rule-derived domain column, give exact per-domain divergence counts, restate §6.1 and abstract on the rule-derived column; else amend under §10 | Protocol §6; PRISMA 2020 item 18; CHAMP item 19 | critical-reviewer | retained → remediate |
| REV-1-4 | major | reporting | review:84-91, 916-919, 994-996, 1049, 1110 | Headline coverage fractions use 72 as denominator although 3 twins and up to 16 n/a records cannot contribute a numerator; assessable denominators are 65 (Q1-Q7) and 53 (Q8/Q9); the one attempt says "56 assessable" where its own row gives 53 | "**D7 is the weakest domain overall (46 high, 5 low, out of 56 assessable).**" | State each fraction over its assessable denominator with the excluded classes named; correct 56→53; carry corrections into abstract and §7.2-§7.4 | SAMPL; PRISMA 2020 items 2, 20; CHAMP item 18 | critical-reviewer | retained → remediate |
| REV-1-5 | major | reporting | review:95-103 (abstract), 194-199 (§2.2), 1951-1958 (§12.3) | Abstract Limitations omits two equally-rated defects: the never-executed backward-chase arm (VG-4 major) and the I3/X7 eligibility violations; Design paragraph asserts the design without the non-executed arm | Abstract Limitations paragraph, four defects only | Add the unexecuted arm and the eligibility violations to the abstract Limitations; state the non-execution in the Design sentence | PRISMA 2020 item 2; CHAMP items 20-23 | critical-reviewer | retained → remediate |
| REV-1-6 | major | interpretation | review:1595-1674 (§9.3, §9.4); agenda:124-138, 501-505 | NB-13 given an unqualified `episode-statistic-null` on the DP 122 working-paper twin after the journal text was never obtained; `indeterminate-from-full-text` existed in the frozen vocabulary and was not used; propagates as "adjudicated-and-negative" | "**The journal full text was NOT obtained** after four attempts" | Relabel `indeterminate-from-full-text`, or retain the label explicitly as provisional; correct §9.4 and the agenda's unqualified sites | Protocol §9.1 vocabulary; CHAMP items 24, 30; PRISMA 2020 item 23b | critical-reviewer | retained → remediate |
| REV-1-7 | major | consistency | agenda:479-511, 678-710; review:2299-2318 (§14 items 2, 5) | Agenda Rev 4 drops three branch-3 inputs: the surveillance comparator recommendation with its nine record ids, the measured FWER 0.55-0.93, and TC-4's prohibition on adopting r0 / the duration constant | "should enter the comparator set on that ground alone" | Extend branch 3 with the surveillance line + reason, the FWER measurement and the missing delay/ARL0 metric, and TC-4; attach the multiplicity qualification to Definitional basis (d) | Review §7.4, §7.8, §11, §14; CHAMP items 24, 30; spec Thread A item 2 | critical-reviewer | retained → remediate |
| REV-1-13 | major | interpretation | review:1152-1162 (§7.4) | The self-declared sharpest claim is an unscoped universal negative about a literature while every neighbouring claim is corpus-scoped; the supporting corpus lost 47.8% of full-text-stage records and never ran the backward arm | "the recursive family is the one that does not" | Rewrite the O4 claim corpus-scoped; attach the L-4/L-5 recall bound at the claim; apply the same scoping test to O5 | CHAMP items 24, 29, 30; PRISMA 2020 item 23b/23d | critical-reviewer | retained → remediate |
| SCOPE-1-1 | major | changed | review:1459-1486 (§9.0); search_logs/explosive-regime/ | Protocol §9.1 force-screening of NB-02/NB-08/NB-13 into the 1,996-record universe never happened; the review discloses out-of-corpus status but not non-entry, while §3.2 claims the flow reconciles exactly | Grep of the log directory matches only se-nb-adjudications.json and protocol-doicheck.json | Disclose in §3.1/§9.0 plus a VG row that the three targets were adjudicated without entering the screened universe; log as a numbered amendment | protocol §9.1 final paragraph | scope-auditor | retained → remediate |
| SCOPE-1-2 | major | omitted | protocol:765-821 (Addendum); review §12.5 | A4/A5/A6 exist only inside the review, which delegates the append to a consumer session; the protocol addendum ends at A3, so three declared deviations have no entry in the frozen carrier | "amendments_run_under: [A1, A2, A3]" vs "amendments_this_document_requests: [A4, A5, A6]" | Append A4-A6 verbatim with dates, stage and PRISMA-P items; update the review frontmatter to cite them as appended | protocol §10; review §12.5 | scope-auditor | retained → remediate |
| SCOPE-1-3 | major | changed | review:302-336 (§2.8), §6, §12.1 L-2 | Protocol §4.3 source-text reconciliation replaced by a post-hoc conservative ordering rule over 90 of 357 divergent cells with no source reopened; §6 is direction-safe, not adjudicated | "The rule is chosen to be direction-safe, not to be right." | Run the reconciliation and write the artifact, or state in §6's header and every downstream use that the profile is convention-resolved; propagate to the agenda | protocol §4.3; review §2.8, L-2, A6 | scope-auditor | retained → remediate |
| SCOPE-1-4 | major | omitted | review:194-199 (§2.2), §12.3 VG-4 | Protocol §3.3 backward citation-chasing arm never executed and no se-bc-* log exists; compounded by three known-item recall failures on the pre-2011 antecedent layer | "Backward citation-chasing (er-bc-*): not run. … MAJOR protocol-vs-execution gap" | Execute the arm over I2b records and log additions, or record a dated §10 waiver freezing the corpus as recall-limited; do not tick Thread A first | protocol §3.3; review VG-4 | scope-auditor | retained → remediate |
| SCOPE-1-5 | major | changed | review:1864-1878 (§12.1 L-6, L-7) | Frozen I3 and X7 applied differently from their written form: five records without any PID inside the 72, and three same-work twins surviving deduplication (72 records = 69 works) | Protocol I3 "excluded and logged … not silently dropped" vs L-6/L-7 | Record both as numbered §10 amendments; state 72 records / 69 distinct works in the §5 and §6 headers | protocol §2.2 I3, §2.3 X7; review L-6, L-7 | scope-auditor | retained → remediate |
| SCOPE-1-6 | major | partial | agenda:701-710 | Rev 4 residual paragraph carries a subset of the bounding defects and omits the largest (280 X6 exclusions, 47.8%, direction unknown) and A6's consequence for the appraisal | Review L-4 vs agenda residual paragraph | Add one sentence carrying L-4 and one clause noting the appraisal is convention-resolved, not source-adjudicated | review §12.1 L-2, L-4; VG-2 | scope-auditor | retained → remediate |
| QUANT-1-1 | major | method | review:279-300, 776-870; protocol:526-544 | ER-RoB v1's three-level response scale was executed as four levels by adding `partial` in 50 cells, with no amendment, while §2.7 asserts the instrument was unaltered; the frozen concern rule is undefined for the added level | Protocol §6 "yes / no / unclear" vs review legend "yes / partial / unclear / no" | Add an amendment A7 recording the scale extension and where `partial` sits in the concern rule; correct §2.7 to except the response scale | protocol §6; PRISMA 2020 item 11 | quant-auditor | retained → remediate |
| QUANT-1-2 | major | assumption | review:788-793, 871-920, 81-93 | 31 domain cells recorded `low` although a mapped question answered other than `yes`; D4 would be 48 high / 16 low under the frozen rule, not 41/23; departures run toward lower concern against §2.8's stated posture | Recomputation over the 72 rows: D3 21, D4 7, D5 2, D6 1 | Replace "a few cells" with the count broken out per domain; report both distributions; say which underlies §6.1 reading 2 and abstract point (3) | protocol §6; QUADAS-2 convention | quant-auditor | retained → remediate |
| QUANT-1-3 | major | reproducibility | review:34-41, 262-268, 1819-1827, 2354-2364 | The review declares claude-opus-5 as the screening/extraction automation tool; the commit trailers on 8aeebfe and 9deee0c and the protocol frontmatter declare claude-fable-5, and the cited ReproLog has no model field | Frontmatter vs `AI-Assistance: claude-fable-5 (role=multi)` | State per stage which model id produced the artifact, matching the trailers; if stages differ, say so and re-state what κ measures | PRISMA 2020 item 8; CLAUDE.md §Reproducibility contract | quant-auditor | retained → remediate |
| QUANT-1-4 | major | reproducibility | review:2320-2334 (§15), 1999 (§12.4 item 27) | §15 omits the ReproLog path/SHA-256, the sidecar SHA-256 and the git HEAD the project contract requires; item 27 asserts "all tracked" while three cited artifacts are untracked | CLAUDE.md contract clause vs §15 rows and `git status --short` | Add ReproLog/sidecar/HEAD rows labelled as untracked locators; re-word item 27 to state status as of the delivering commit | CLAUDE.md §Reproducibility contract; emit-repro-log; PRISMA item 27 | quant-auditor | retained → remediate |
| QUANT-1-5 | major | numerical | review:975-983 vs 969 (§7.1) | The O1 claim says size distortion is "always upward" while the same section's table carries a counterexample where size tends to 1 **or 0** by break sign — a power failure, not a false-alarm failure | "size tends to 1 or 0 depending on break sign" (eru-0348) | Replace "always upward" with the bounded form naming the drift-break exception; carry the exception into the TC-1 handoff rationale | doi:10.1515/jtse-2013-0004 (Sollis 2016) | quant-auditor | retained → remediate |
| QUANT-1-6 | major | reporting | agenda:479-511 vs review:1122-1170, 2299-2305 | Branch 3 admits BSADF as an online comparator with no multiplicity caveat and omits the surveillance line the review says publishes branch 3's own declared metric | Agenda grep returns no FWER/0.55/0.93/eru- hit | Add the FWER 0.55-0.93 measurement with the 7.56→12.20-month delay cost as a binding condition, and the surveillance record set with its admission ground | review §7.4, §14; doi:10.1017/9781108910095.003 Table 1 | quant-auditor | retained → remediate |
| QUANT-1-7 | major | verification-gap | review:1332-1458 (§8), 1488-1666 (§9) | The Phillips verdict and the three NB adjudications rest on quotations and page locations from primary texts with no archived copy, retrieval route or digest in the repository; fidelity is asserted, not verifiable | Extraction JSONL is a transcription, not the source | Record retrieval route and content digest (or archived copy) for each of the six primary texts, or mark §8/§9 as single-session transcription and add the gap to §12.3 | charter "numeric claims require the primary source"; PRISMA item 19 | quant-auditor | retained → remediate |
| LITERATURE-1-2 | major | misattributed-source | review:661, 1126-1135; references_explosive-regime.json:2359-2379 | eru-1289 is dated 2022 and tiered "peer-reviewed chapter" on a DOI that resolves to a 2025 CUP chapter, while the extracted text is the Cowles DP 2331 working paper; absent from L-10 and VG-6 | Crossref: chapter issued 2025-04-30, pp. 30-59 | Re-date and re-extract from the chapter, or tier the FWER claim working-paper and add eru-1289 to L-10/VG-6 as a fourth case | https://doi.org/10.1017/9781108910095.003 | literature-check | retained → remediate |
| LITERATURE-1-4 | major | verification-claim-overstated | review:1916-1923 (L-13) | L-13 claims exactly two metadata discrepancies surfaced at verification; independent Crossref checks find at least two more (eru-1580 issue and both page bounds; eru-1852 page bounds) | Crossref jtsa.12784 = 46(5):846-866 vs review 46(1):102-132 | Run the full Crossref page/volume/issue check over all 62 DOI-bearing records and restate L-13, or declare it a spot check | https://api.crossref.org/works/10.1111/jtsa.12784 | literature-check | retained → remediate |
| LITERATURE-1-6 | major | consumer-transcription-omission | agenda:701-710 | Agenda residual paragraph drops the 280 X6 unobtainable-full-text exclusions and names A6 without its content, so an agenda-only reader cannot tell the appraisal profiles are unadjudicated | Zero agenda hits for 280 / 47.8 / X6 / 357 | Add the 280 X6 exclusions as a corpus-wide recall bound and one clause stating what A6 is | review L-4, VG-2, L-2 | literature-check | retained → remediate |
| LITERATURE-1-1 | major | unverifiable-quotation | review:1341, 1352-1363; agenda:109-114 | Claimed that every PWY 2011 quotation resolves to no independently accessible copy | Targeted phrase searches "return zero hits on all three" | Archive the retrieved text with a checksum, or mark the three quotations as single-retrieval | https://doi.org/10.1111/j.1468-2354.2010.00625.x | literature-check | **refuted → dropped** |
| LITERATURE-1-3 | major | method-attribution-overstated | review:1425-1430 (§8.3 clause 2) | Claimed the clause flattens numerical evaluation of the derived limit functional into finite-sample Monte Carlo, and that the agenda inherits the over-broad ground | "it does not deliver the numbers" | Restate clause 2 splitting the two provenances; keep PARTIAL and TC-5 | https://doi.org/10.1111/iere.12132 | literature-check | **refuted → dropped** |
| LITERATURE-1-5 | major | unverifiable-numeric-claim | review:1124-1133, 89 | Claimed the FWER triple 0.55/0.78/0.93 could not be confirmed in any accessible copy of Cowles DP 2331 | "PDF text extraction was unavailable for all three" | Cite the table and page of the version read, archive the cell, bound the synthesis to its design | https://elischolar.library.yale.edu/cowles-discussion-paper-series/2688/ | literature-check | **refuted → dropped** |
| REV-1-8 | minor | consistency | review:1246-1252, 1217-1224 (§7.6) | "Fewer than one in three" is false on the sentence's own denominator: 22/65 = 33.8% | O6 synthesis sentence | Give the count and denominator, or fix the denominator and state the excluded classes | SAMPL; CHAMP item 22 | critical-reviewer | logged |
| REV-1-9 | minor | reporting | review:157-171, 1978, 1999, 2328 | "42 executed query logs" is a query-id count, not a file count (60 files); "six verdict/extraction JSONL files" where eight exist; item 27's tracked claim false for se-extraction-recheck.jsonl | "one file per query id" | State both numbers; correct six→eight; commit the recheck log before the availability claim | PRISMA-S items 7-9; PRISMA 2020 item 27 | critical-reviewer | logged |
| REV-1-10 | minor | reporting | review:425-455 (§3.3); frontmatter 30-32 | κ reported to six decimals with no interval, on counts giving ~5e-4 granularity; same over-precision on p₀ and pₑ | "κ = … **0.433012**" | Report κ = 0.43 with a CI (asymptotic or bootstrap) and round p₀/pₑ; or state why no interval is computed | SAMPL; CHAMP item 18 | critical-reviewer | logged |
| REV-1-11 | minor | consistency | review:1488-1495, 1947-1958; agenda:126-128 | NB-02 adjudicated on a preprint twin — the same defect logged as VG-3 for NB-13 — but recorded only inline; year inconsistent (2001 vs 2002) across protocol, review and agenda | "Version adjudicated: arXiv:cond-mat/0010050v2" | Add a parallel VG row with the equivalence argument; fix the year to one form or state the WP/journal split | PRISMA 2020 item 23; review §12.3 | critical-reviewer | logged |
| REV-1-12 | minor | reporting | review:105-112 (§1), 1682-1795 (§10), 2289-2318 (§14) | No statement of how the synthesis relates to published surveys of the same literature, several inside its own corpus; originality of the conclusions is not locatable | §1 rationale carried in force from protocol §0 | Add a subsection naming the in-corpus surveys and which findings are new relative to them | PRISMA 2020 items 3, 23b; RQI originality | critical-reviewer | logged |
| SCOPE-1-7 | minor | documented-drift | review:768-869 (§6) | 72 rows but seven carry no appraisal content (4 unread, 3 twins); effective coverage 65, of which 14 single-pass — disclosed, but "one row per included study" is met at row level only | §6 legend and §6.1 | State the effective denominator (65 appraised; 51 dual, 14 single-pass) in the §6 header and wherever an "of 72" domain count is quoted | spec Thread A item 1; review §6, L-9 | scope-auditor | logged |
| SCOPE-1-8 | minor | spec-conflict | spec:17 vs protocol:24-27 | Spec names the delivered review path; the frozen protocol's planned_outputs names a different filename pattern and date component; declared as A4, which is unappended | protocol planned_outputs vs §12.5 A4 | Append A4 so the frozen record names the delivered path, or rename | spec Thread A item 1; protocol planned_outputs; A4 | scope-auditor | logged |
| SCOPE-1-9 | minor | documented-drift | spec:40-44 | Thread A item 3 — this audit trail — did not exist at audit time; declared unchecked in the spec | Glob `docs/audits/audit_trail_phase2*` → no files | Write the trail with the 22 keys, 7 sections, gate dispositions and sidecar SHA before ticking Thread A | spec Thread A item 3 | scope-auditor | logged (discharged by this document) |
| SCOPE-1-10 | minor | documented-drift | review:1691-1695 (§10.1), L-8, I-2 | Protocol §8 item 1's citation-uptake check is unrunnable because X1 excludes plain applications; replaced by an in-corpus uptake observation, declared as L-8/I-2 and flagged ▲ | L-8 and conformance item 14 | No further work on this artifact; carry I-2 into the successor protocol | protocol §8 item 1; review §10.1, L-8, I-2 | scope-auditor | logged |
| QUANT-1-8 | minor | numerical | review:1246-1252 (§7.6) | O6 fraction wrong in the direction that overstates the finding and its denominator inconsistent with the review's own coding (66, not 65) | RT 22, CS 19, FS 22, SPLIT 3, NS 2, NE 4 = 72 | State the denominator's derivation; "22 of 66 (one in three)"; handle SPLIT explicitly | review §4.1, §5, §7.6 | quant-auditor | logged |
| QUANT-1-9 | minor | reporting | review:1130-1135 (§7.4) | Concern profile beside the sharpest claim says D4 low; the appraisal row and the extraction record both say D4 high | §6 row 68; se-extraction-primary.jsonl | Correct to "D6 low, D4 high, D7 high" | review §6 row 68; se-extraction-primary.jsonl | quant-auditor | logged |
| QUANT-1-10 | minor | reporting | review:680-692, 1864-1870, 1958 | I3 gap reported as five where seven store entries carry no PID; twin-identifier crediting applied inconsistently (eru-0622 got its own DOI) and never stated | 62 DOIs; 10 without; 2 arXiv, 1 Handle | State the twin-identifier rule and report seven with two discharged by inheritance, or list all seven | protocol §2.2 I3, §4.1; FAIR F1 | quant-auditor | logged |
| QUANT-1-11 | minor | reporting | review:745-766 (§5.4), 1893-1899 (L-10), 1956 (VG-6) | The version/chain caveat list omits eru-1289, the source of the headline O4 quantity; disclosed only inline in §7.4 | §5.4 "Three further records carry version or chain caveats" | Add eru-1289 to §5.4 and VG-6; attach the caveat to the abstract's FWER sentence and §7.8's BSADF row | review §5.4, §7.4, §12.3 | quant-auditor | logged |
| QUANT-1-12 | minor | reporting | agenda:701-710 | Residual paragraph omits L-1 (single-model screening) and L-4 (280 X6), the two limitations the review ranks first and fourth by capacity to change a conclusion | "recall-limited on the antecedent layer" | Name both and widen the bounding sentence to the review's own framing | review L-1, L-4; VG-2 | quant-auditor | logged |
| QUANT-1-13 | minor | reporting | review:1693-1698 (§10.1) | A non-suppression conclusion drawn from a proportion over an availability-selected subset (53 of 72); the existence half is robust, the proportion half is not | §10.1 two-thirds sentence vs L-4 | Split the sentence; re-state the proportion as "over the 53 records whose full text was obtained", flagged as availability-selected | PRISMA 2020 items 14/21; protocol §8 | quant-auditor | logged |
| QUANT-1-14 | minor | reporting | review:171, 367, 1978, 2328 | "42 executed query logs" repeated four times as a file count; 58 files carry a `retrieved_count`, summing to 4,898 exactly | Recount over the log directory | Re-word to "42 protocol queries executed, archived across 58 response files plus 2 seed-resolve logs" | PRISMA-S items 8-9; protocol §3.1, A1 | quant-auditor | logged |
| LITERATURE-1-7 | minor | internal-attribution-inconsistency | review:1134 vs 865 | The concern profile on the most consequential O4 claim contradicts the appraisal row for the same record, in the direction of confidence | §7.4 "D6 low, D4 low, D7 high" vs row 68 D4 high | Correct §7.4 and re-sweep the other per-claim concern-profile sentences in §7 against §6 | review §6 row 68 | literature-check | logged |
| LITERATURE-1-8 | minor | imprecise-attribution | review:126-128, 2344 | The O4 evaluation-criteria taxonomy is attributed to Frisén 2003, whose declared subject is optimality and methods; the canonical source for the criteria set is Frisén 1992 | Frisén 2003 ISR 71(2):403-434 verified; Frisén 1992 Stat Med 11(11):1489-1502 verified | Cite Frisén 1992 alongside 2003 where the taxonomy is invoked, or reword | https://doi.org/10.1002/sim.4780111107 | literature-check | logged |
| LITERATURE-1-9 | minor | citation-year-inconsistency | agenda:127 vs review:1490-1494 | NB-02 dated 2002 in the agenda, 2001 in protocol and review, same DOI, no reconciling note | arXiv v2 25 Jul 2001; journal-ref Journal of Risk 4(2), Winter 2001/02 | Fix one form across the three artifacts and state the adjudicated text at the agenda site | https://arxiv.org/abs/cond-mat/0010050 | literature-check | logged |
| LITERATURE-1-10 | minor | search-reporting-accuracy | review:171, 1978, 2328 | "42 executed query logs" labels arms as logs (60 files exist), and §12.4's "all 42 logs including the four zero-yield 429s" is not consistent with the arithmetic producing 42 | Directory enumeration = 60 files | Report both numbers explicitly and update §2.2's total row, §12.4 item 7 and §15 | docs/literature/search_logs/explosive-regime/ | literature-check | logged |
| LITERATURE-1-11 | minor | canonical-form-mismatch | review:1340-1341 | The PWY null limit is written with undemeaned W and no window fraction, contradicting the demeaned regression the same cell describes | E4/E5 cell, §8.1 | Reproduce the limit as in the source with demeaned Wiener functionals and subsample normalisation, or keep the prose statement only | https://doi.org/10.1111/j.1468-2354.2010.00625.x | literature-check | logged |

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; a drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Twenty-seven
dispositions: **3 dropped** (LITERATURE-1-1, LITERATURE-1-3, LITERATURE-1-5 —
each defeated by an independent retrieval or a line-anchored re-read that
contradicted the claim's own evidentiary premise) and **24 retained** after
failed refutation attempts. There are no retained-conservative entries this
round (`retained_conservative: 0`); the three drops carry concrete
counter-evidence of the enumerated types (`source-quote`, `reproduced-check`),
so none is a bare-disagreement drop. Exactly one entry carries
`reproduction_required: true` (LITERATURE-1-3); its
`reproduction: {command, observed}` block is lifted from the refutation
evidence and given below. Claims are reproduced verbatim and unabridged.

### LITERATURE-1-1 — dropped (refuted)

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false; outcome: **dropped**

Claim verbatim:

> **category:** unverifiable-quotation
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1341,1352-1363; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:109-114
> **issue:** Every verbatim quotation attributed to PWY 2011 — the half of the §8.3 confirm-or-correct verdict that discharges the branch-3 precondition — resolves to no independently accessible copy. The PSY 2015a counterparts verify; the PWY ones do not.
> **evidence:** Review §8.1 quotes, as from IER 52: 'However, sup_{r∈[r₀,1]} ADF_r cannot reveal the location of the exuberance' (p.215); 'The setting employed is cv_adf_n(s) = log(log(ns))/100 … leads to critical values around the 4% significance level' (p.208); 'The critical values … are obtained by Monte Carlo simulation with 10,000 replications' (Table 1 note, p.214). Targeted phrase searches over the indexed Yale/Cowles/HKIMR copies return zero hits on all three, while the same method returned exact hits for the PSY 2015a analogues ('…the GSADF test is an ex post statistic used for analyzing a given data set for bubble behavior'; r₀ = 0.01 + 1.8/√T; 'asymptotic critical values … obtained by numerical simulations with 2,000 replications'). The review's own §8 retrieval note records that four in-cap attempts failed and the texts were secured only by an out-of-cap deviation (requested amendment A5); no quote-level archive of the retrieved text exists in docs/literature/search_logs/explosive-regime/. The first quote is transcribed into agenda Rev 4 line 109 as load-bearing evidence.

Refutation (counter-evidence, `source-quote`): the refuter independently
retrieved Cowles Foundation Paper 1349 (the IER 52(1):201-226 reprint) at
`http://korora.econ.yale.edu/phillips/pubs/art/p1349.pdf` (258,681 bytes,
sha256 `a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4`) and
matched all three disputed quotations verbatim — page 214 ("However,
sup_{r∈[r0,1]} ADF_r cannot reveal the location of the exuberance."), page 207
(the log(log(ns))/100 "around the 4% significance level" sentence), and the
page 213 Table 1 note ("obtained by Monte Carlo simulation with 10,000
replications") — plus a second independent copy (HKIMR WP 22/2007) carrying the
load-bearing first quotation. The host serves HTTP only and refuses HTTPS,
which explains the auditor's null probe. The claim's evidentiary premise ("zero
hits on all three") is therefore false. The missing local quote-archive
observation is accurate but is a different defect; the page-locator off-by-one
the refuter found incidentally is carried by QUANT-1-7, which was retained.

### LITERATURE-1-3 — dropped (refuted)

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **reproduced-check**; reproduction_required: **true**; outcome: **dropped**

Claim verbatim:

> **category:** method-attribution-overstated
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1425-1430
> **issue:** §8.3 clause 2 denies 'against derived critical values' with the blanket rationale that the derived limit theory 'delivers the distributional form and the consistency rate conditions; it does not deliver the numbers'. That flattens two distinct provenances the review's own §8.2 extraction keeps apart: numerical evaluation of the derived limit functional (which is how a derived asymptotic distribution is tabulated, as in Dickey–Fuller) versus finite-sample Monte Carlo quantiles.
> **evidence:** Review §8.2 E5 records for PSY 2015a: 'asymptotic distributions derived (Theorem 1); asymptotic CVs by numerical simulation of the limit functional (2,000 replications, 2,000-step Wiener approximation); finite-sample CVs by Monte Carlo, 2,000 replications'. PSY 2015a's own Table 1 note, verified verbatim in the indexed Cowles/Yale text, states the asymptotic critical values are obtained by numerical simulation in which the Wiener process is approximated by partial sums of 2,000 N(0,1) variates. The protocol §9.1(i) PARTIAL trigger is 'the operational critical values are simulated finite-sample values', not 'the asymptotic values were computed numerically'. The PARTIAL verdict survives on the operational dating rule (finite-sample MC at each r₂, p.1067; PWY's log-log convention), but the stated ground is broader than the sources support and is what the agenda inherits.

```yaml
reproduction:
  command: >-
    line-numbered read of docs/literature/lit_review_explosive-regime-dating_2026-08-24.md
    at lines 1425-1430 (clause 2), 1395-1401 (the criterion-(b) adjudication it
    summarises) and 1442-1448 (the prescribed Rev 4 text), then of
    docs/research_notes/research_agenda_regime-classification_2026-08-21.md at
    lines 110-114 (the inherited wording); cross-read of
    docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl
    record ADJUDICATION-i, field criterion_b_derived_cvs
  observed: >-
    Line 1425 opens clause 2 and reads: '**"against derived critical values" — NOT
    SUPPORTED as an operational description.** In both papers the critical values
    actually used are Monte Carlo simulated (asymptotic-functional or
    finite-sample) or, in PWY's dating rule, a stated divergence convention
    log(log(ns))/100 at "around the 4% significance level". The derived limit
    theory delivers the distributional *form* and the consistency *rate
    conditions*; it does not deliver the numbers.' The parenthetical
    '(asymptotic-functional or finite-sample)' is the very distinction the finding
    says is flattened, and the header is scoped 'as an operational description'.
    Lines 1395-1401 state 'Criterion (b) **FAILS as the operational source.** Limit
    distributions are derived (Theorem 1 eq. (5); the companion's Theorems 1-9),
    but every operational quantile is simulated', quoting the IER 56:1051 Table 1
    note. Agenda lines 110-114 read 'The operational critical values are
    **simulated from a derived null limit theory** … not derived values', i.e.
    substantively the finding's own claimed fix, so no over-broad ground
    propagates.
```

The defect claim fails on the artifact text at the cited lines and on the cited
sources. PARTIAL and TC-5 stand unchanged.

### LITERATURE-1-5 — dropped (refuted)

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false; outcome: **dropped**

Claim verbatim:

> **category:** unverifiable-numeric-claim
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1124-1133,89
> **issue:** The FWER 0.55 / 0.78 / 0.93 values — the review's self-described sharpest synthesis claim and abstract principal finding (4), and the ground on which branch 3 is told the recursive family 'does not publish the quantity branch 3 declares as its comparison metric' — could not be confirmed in any accessible copy of the cited source, and rest on a single record with no replication.
> **evidence:** Review §7.4 attributes 'FWER of the PSY dating recursion over a 10-year span … 0.55 (T = 40, quarterly)', '0.78, rising to 0.93 in the worst configuration' and 'origination delay 7.56 → 12.20 months' to eru-1289 Table 1. Targeted searches of the indexed Cowles DP 2331 (d2331_0.pdf), the EliScholar deposit and the Macquarie accepted manuscript return no occurrence of these values; PDF text extraction was unavailable for all three. The review itself notes this is an originator-team paper and, per §2.9, counts in the review may not function as inference — yet the §7.4 synthesis sentence generalises one Monte Carlo design (T = 40, quarterly, 10-year span) into a property of 'the recursive right-tailed family … as conventionally applied'.

Refutation (counter-evidence, `source-quote`): the refuter retrieved exactly the
file the finding names (`https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf`,
31 pages) and extracted its text with pypdf 6.13.1. Table 1 on printed p.20
("The family wise error rates of the PSY procedure") gives PSY (standard) 0.55 /
0.78 / 0.93 across Quarterly T = 40, Monthly T = 120, Weekly T = 520, with body
text "still badly distorted at 55% … rises rapidly to 93%"; Table 2 on printed
p.21 gives 7.56 and 12.20 months, with the 10-year-span and Type-I-over-the-
period framing stated in-source. The values are therefore verifiable and now
verified at the cited table, matching the repo's own extraction records. The
residual scope point about "as conventionally applied" is a wording quibble
outside the filed numeric-verifiability defect; the source itself frames the
result across three sampling frequencies rather than one configuration.

### REV-1-1 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** design
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2007-2029 (§12.5); docs/methodology/protocol_explosive-regime-review_2026-08-24.md:748-767 (§10)
> **issue:** Three declared protocol deviations (A4 output naming, A5 retrieval-cap deviation for the §9.1(i) carriers, A6 unexecuted dual-extraction reconciliation) are described in the review but NOT appended to the frozen protocol's append-only addendum, which still ends at A3. Protocol §10 assigns amendment entries to the executing session and states that any deviation 'is recorded as a dated amendment entry in the addendum section below'. The review is the executing session for all three: A4's naming was fixed at dispatch, A5 occurred during §8 extraction, A6 during the extraction stage. Deferring to a 'consumer session' leaves the registration carrier — the artefact that makes protocol-vs-execution fidelity auditable — inconsistent with executed conduct at ship time, and makes the frontmatter field protocol_sha256_with_addendum (A1-A3 only) an incomplete record of the conduct the review describes.
> **evidence:** This review does **not** edit the frozen protocol. Protocol §10 makes the addendum append-only and assigns amendment entries to the executing session; the three deviations below are recorded here in full so that none is silent, and the consumer session should append them:

Refutation attempt failed with no counter-evidence of any enumerated type. The
addendum grep returns A1/A2/A3 only; A1–A3 were themselves appended after the
`9deee0c` freeze, so no structural bar excuses A4–A6; the two counter-candidates
tested (the §12.4 24a/b/c disclosure row; the "A4 is pre-execution" argument,
defeated by A1 being an identically-classed pre-execution naming deviation that
was appended) both fail.

### REV-1-2 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:667-691 (§5.1), 1864-1870 (L-6), 1958 (VG-8); docs/literature/references_explosive-regime.json
> **issue:** The count of included records failing eligibility criterion I3 is wrong: it is seven, not five. The review's own identifier tally proves it — 62 DOIs + 2 arXiv IDs + 1 Handle = 65 identified records out of 72, leaving seven without any protocol-accepted persistent identifier, while §5.1, L-6 and VG-8 name only five (eru-0100, eru-0112, eru-0268, eru-0427, eru-1310). The two omitted records are the twins eru-0154 and eru-0904: the corpus store carries no DOI/arXiv/Handle field for either, and neither carries the 'I3 GAP' note that the other five carry (the store has exactly five such notes). §5.3 itself states eru-0154 has 'no independent identifier'. The undercount propagates into the PRISMA conformance map's item-5 caveat and into the agenda's Rev 4 residual paragraph, which repeats 'Five included records fail eligibility criterion I3 as written'.
> **evidence:** **Five included records have no DOI, no arXiv ID and no Handle** — `eru-0100`, `eru-0112`, `eru-0268`, `eru-0427`, `eru-1310`.

Refutation failed: a parse of the 72-entry store confirms exactly seven records
with no DOI, arXiv ID or Handle, and the only candidate defense — twin
inheritance of a carrier's DOI — is contradicted by the record-level wording of
protocol §2.2 I3 and by the review's own §5.3.

### REV-1-3 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:788-793 (§6 legend), 796-869 (appraisal table), 876-925 (§6.1); docs/methodology/protocol_explosive-regime-review_2026-08-24.md:526-529 (§6)
> **issue:** The domain-concern column is not derived by the rule the frozen protocol states for ER-RoB v1 ('no' or 'unclear' on any question in a domain raises that domain's concern), and the deviation is described as affecting 'a few cells' when it affects a large minority. For domain D3 alone, at least 13 of the ~41 records answering Q4 'no' carry D3 = low: eru-0503 (row 9), eru-0748 (17), eru-0889 (19), eru-1394 (29), eru-1716 (33), plus rows 23, 28, 31, 41, 59, 60, 61, 69. D4 shows the same pattern (eru-1604 row 32, eru-1155 row 56, eru-1770 row 71 all have Q5 = no with D4 = low). Because §6.1's domain distributions are computed from these cells and feed four headline 'readings' and three abstract claims (D4 high in 41, D6 high in 33, D7 high in 46), the corpus-level concern profile is systematically more lenient than the declared instrument produces, and a reader cannot tell which cells were rule-derived and which were the extractor's free judgment. §2.7 simultaneously asserts 'no domain or question was added, dropped or reworded' while the domain-scoring rule was in effect dropped.
> **evidence:** A domain cell **without** `†` is the primary extractor's own recorded judgment, reproduced verbatim and not re-derived mechanically from the Q cells; the instrument does not fix a deterministic Q→D map, and a few cells are consequently less concerning than a mechanical map would give.

Refutation failed: an independent parse of the 72 rows reproduces the enumerated
13 D3 rows exactly and finds 6 such D4 rows; the legend disclaimer cited as
counter-evidence is the artifact's own acknowledgment of the deviation, not a
rebuttal. The only imprecision found (~41 vs 39 Q4 "no" records) is hedged in the
claim and does not affect it.

### REV-1-4 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:84-91 (abstract), 916-919 (§6.1 reading 4), 994-996 (§7.2), 1049 (§7.3), 1110 (§7.4)
> **issue:** Every headline coverage fraction uses 72 as the denominator, but 3 of the 72 are twins appraised '—' and up to 16 more are 'n/a' (4 with no full text, 12 recheck-only where Q8/Q9 are unanswerable), so they cannot contribute a numerator by construction. The correct assessable denominators are 65 for Q1-Q7 and 53 for Q8/Q9. The effect is systematic and one-directional: 8/72 = 11% becomes 8/53 = 15% for code availability; 23/72 = 32% becomes 23/65 = 35% for dating; 19/72 = 26% becomes 19/65 = 29% for multiplicity. Each mis-stated fraction understates the literature's coverage, i.e. biases in the direction of the review's own critical conclusions. The single place an assessable denominator is attempted gives the wrong number: §6.1 reading 4 says 'out of 56 assessable' where its own table row is 5 + 2 + 46 = 53.
> **evidence:** **D7 is the weakest domain overall (46 high, 5 low, out of 56 assessable).**

Refutation failed: the row sums reproduce the assessable denominators 53 and 65
exactly, no site declares a deliberate 72-denominator convention, and the §6.1
table header's gloss ("n/a = the four records with no full text") is itself false
for the D7/D8 rows where n/a = 16.

### REV-1-5 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:95-103 (abstract Limitations), 194-199 (§2.2), 1951-1958 (§12.3)
> **issue:** The abstract's Limitations paragraph reports four defects (single-model screening, 280 X6 exclusions, 4 unread includes, unreconciled dual extraction) but omits two of the review's own equally-rated defects: the backward citation-chasing arm that the body labels a MAJOR protocol-vs-execution gap and rates VG-4 major, and the eligibility violations (records failing I3, twins surviving X7). A reader of the abstract alone learns that recall was limited by access failure but not that a prescribed search arm was never executed and that the included set contains records failing the frozen inclusion criteria. The abstract's Design paragraph also asserts the protocol design ('Five platforms, 24 topical queries, four forward-citation arms over the two seed papers, and a 14-item known-item arm') without noting that the supplementary arm the protocol prescribes did not run.
> **evidence:** **Limitations.** Screening was two context-independent sessions of one base model, not two humans; κ therefore measures decoding-and-context variance, not inter-rater reliability. 280 records (47.8% of those reaching full text) were excluded because full text could not be obtained, which is a recall-side risk of unknown direction. 4 included records were never read at full text.

Refutation failed: the abstract carries exactly the four named defects and no
trace of the backward arm, I3 or X7; VG-4 sits in the same "major" band as the
two access-side limitations that are in the abstract. Only partial mitigation
exists (the twin count is visible in the Results paragraph), insufficient to
refute.

### REV-1-6 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1595-1674 (§9.3, §9.4); docs/research_notes/research_agenda_regime-classification_2026-08-21.md:124-138, 501-505
> **issue:** NB-13 is given an unqualified substantive verdict on a version that is not the version whose claim is being adjudicated. The journal full text was never obtained; the adjudicated text is the 2006 IIIS DP 122 working paper; and the review itself records that the sentence the agenda quotes appears in the journal abstract but NOT in DP 122, and that the journal version reorganises the analysis around the definition-and-test framing with a different country set. The protocol's own pre-fixed verdict vocabulary contains `indeterminate-from-full-text` for exactly this situation, and it was not used. The definite verdict then propagates: §9.4 says the agenda's bounded claim 'strengthens', and the agenda records 'Rev 4 strengthens that claim from "nearest candidates unadjudicated" to adjudicated-and-negative'. The review's own reasoning for extending the DP 122 finding to the journal version is an absence-of-evidence inference ('No accessible trace of the journal version suggests a day-t-computable statistic ... was added'), which cannot carry a definite adjudication.
> **evidence:** **The journal full text was NOT obtained** after four attempts: (1) SSRN 886119 delivery — Cloudflare challenge; (2) OpenAlex and Semantic Scholar OA lookup — status CLOSED, no OA location; (3) web search for a mirrored PDF — none; (4) search for a cached SSRN PDF — none.

Refutation failed: protocol §9.1(iv) fixes the adjudication target by journal
DOI, the frozen vocabulary contains `indeterminate-from-full-text`, no amendment
authorises twin substitution, and the definite label propagates unqualified to
§9.4, the abstract and agenda branch 3. The scope inaccuracies found in the
claimed fix do not touch the defect claim.

### REV-1-7 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:479-511 (branch 3), 678-710 (Verification status); docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2299-2318 (§14 items 2 and 5)
> **issue:** The agenda Rev 4 transcribes the review's Phillips correction and the three NB verdicts faithfully, but drops three of the review's substantive branch-3 inputs. (i) §14 item 2's positive recommendation — that the surveillance/monitoring line publishes a closed-form false-alarm rate over a stated horizon and 'should enter the comparator set on that ground alone' — is nowhere in branch 3; the nine record ids the review names are absent from the agenda. (ii) The review's sharpest synthesis claim, that the recursive family's PSY dating recursion carries a measured family-wise false-detection probability of 0.55-0.93 as conventionally applied, is absent — yet branch 3's declared comparison metric is delay against ARL0, and the agenda's Definitional-basis (d) now asserts 'This is still a time-t assignment with a stated null' with no multiplicity qualification. (iii) §14 item 5 flags TC-4 (r0 and the minimum-duration constant are CONVENTION in the family's own words) as 'the one that blocks a parameter choice'; only TC-5 and TC-6 reach the agenda, so a branch-3 specification reading the agenda alone could adopt r0 = 0.10 or delta*log(T) as an unlabelled constant — the exact failure the project's parameter rule forbids.
> **evidence:** The surveillance / monitoring line (`eru-0735`, `eru-1117`, `eru-1519`, `eru-1844`, `eru-1845`, `eru-0889`, `eru-1038`, `eru-1921`, `eru-1852`) does publish a false-alarm rate over a stated horizon in closed form and should enter the comparator set on that ground alone.

Refutation failed on all three sub-claims: zero agenda hits for the nine record
ids, for the FWER figures, and for TC-4; the pre-existing Rev 2 Frisén/Bock
bullet is not a comparator-set admission and carries none of the records.

### REV-1-13 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1152-1162 (§7.4 synthesis claim)
> **issue:** The review's self-declared sharpest claim is stated as an unscoped universal negative about a literature, not about the corpus. Every neighbouring claim is correctly corpus-scoped ('no record in the corpus reports ARL0 under that name', 'The corpus contains **no** published operating characteristic ... at intraday frequency'), but this one asserts that the recursive family does not publish the required quantity, full stop. The corpus that supports it excluded 47.8% of full-text-stage records as unobtainable (L-4), never ran the backward citation-chasing arm that the protocol prescribes precisely to recover detectors the seeds do not cite (L-5/VG-4), and failed the known-item recall check on three antecedents. This is structurally the F005-class failure the consumer agenda itself catalogues — an unbounded universal drawn from bounded search coverage — and the review's own reading rule ('a count of records is a fact about the literature's coverage, never a fact about a detector') is not applied to it.
> **evidence:** For a consumer whose comparison metric is detection delay against a stated ARL₀ — which is branch 3's declared metric — the surveillance line is the one that publishes the required quantity, and the recursive family is the one that does not.

Refutation failed: O1, O2, O3, O5 and the adjacent TC-3 note are all
corpus-scoped and only the O4 closing sentence is not; no document-level scoping
convention exists that would implicitly scope a negative existential coverage
claim; and the unscoped form propagates to §14 item 2.

### SCOPE-1-1 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** changed
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1459-1486 (§9.0); docs/literature/search_logs/explosive-regime/
> **issue:** Protocol §9.1 requires NB-02/NB-08/NB-13 to be FORCE-SCREENED into the record universe ('regardless of query recall'). They were not: none of the three DOIs appears in screen-verdicts-R1.jsonl, screen-verdicts-R2.jsonl or the candidate store references_explosive-regime-dating.json; they appear only in se-nb-adjudications.json and protocol-doicheck.json. The review discloses that they are out-of-corpus and 'None of them is in the 72', but nowhere discloses that they never entered the 1,996-record universe, so the §3.1 identification/screening flow silently omits three protocol-mandated records and the §3.2 claim 'the flow reconciles exactly with the logs at every stage' is stated without noting this exception.
> **evidence:** Protocol §9.1: 'Records (ii)–(iv) are force-screened into the record universe regardless of query recall (they are already identified; their adjudication is a stated deliverable). Their inclusion in the CORPUS still requires passing §2'. Grep of the search-log directory for '10.21314/jor.2002.058|10.1017/jpr.2017.20|10.1016/j.jfs.2008.08.001' returns matches only in se-nb-adjudications.json and protocol-doicheck.json — not in either screening-verdict file (each 1,996 rows) nor in the candidate store.

Refutation failed: the DOI-grep weakness was tested by parsing the 1,996-record
candidate store directly, which contains none of the three by DOI, arXiv id,
title or author; protocol-doicheck.json self-describes as protocol-drafting
verification carrying no records into any corpus; and no disclosure or VG row
covers the non-entry.

### SCOPE-1-2 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** omitted
> **location:** docs/methodology/protocol_explosive-regime-review_2026-08-24.md:765-821 (Addendum); lit_review §12.5
> **issue:** Protocol §10 requires every deviation to be recorded as a dated amendment entry in the protocol's append-only addendum. Amendments A4 (output naming), A5 (retrieval-cap deviation for the §9.1(i) carriers) and A6 (dual-extraction reconciliation not executed) are enumerated only inside the review, which explicitly delegates the append to 'the consumer session'. The protocol addendum still ends at A3, so three declared deviations have no entry in the frozen-protocol carrier, and the review's frontmatter simultaneously carries 'amendments_run_under: [A1, A2, A3]' and 'amendments_this_document_requests: [A4, A5, A6]' — a deliverable whose own amendment record is incomplete.
> **evidence:** Protocol §10: 'ANY deviation … is recorded as a dated amendment entry in the addendum section below'. Protocol addendum contains A1, A2, A3 only. Review §12.5: 'This review does not edit the frozen protocol … the three deviations below are recorded here in full so that none is silent, and the consumer session should append them.'

Refutation failed: a repo-wide search finds no alternate carrier for A4–A6, and
the review's own `protocol_sha256_with_addendum` is byte-identical to the on-disk
protocol whose addendum ends at A3, so no later-appended version can be argued to
be operative.

### SCOPE-1-3 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** changed
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:302-336 (§2.8), §6, §12.1 L-2
> **issue:** Protocol §4.3 specifies dual re-extraction with mismatches 'resolved against the source text and the mismatch count reported'. The delivered appraisal substitutes a post-hoc conservative ordering rule (no > unclear > partial > yes, marked †) applied to 90 of 357 divergent cells without reopening a single source. This is a substitution in kind of a load-bearing protocol step: the appraisal table in §6 is a direction-safe construction, not a source-adjudicated one, and 25.2% of comparable cells were decided by convention. The review declares the substitution fully (§2.8, L-2, A6, conformance item 9 marked weaker than anticipated), so the drift is documented rather than hidden — but the delivered artifact does not satisfy the protocol item as written.
> **evidence:** Protocol §4.3: 'mismatches are resolved against the source text and the mismatch count reported'. Review §2.8: '90 divergent cells out of 357 (25.2%) … No reconciliation record exists in the search-log directory and the mismatch count had never been reported. Re-opening 51 full texts to adjudicate 90 cells was not undertaken in this pass. … The rule is chosen to be direction-safe, not to be right.' No reconciliation artifact exists in docs/literature/search_logs/explosive-regime/.

Refutation failed: protocol §4.3 and §6 both state the source-adjudication
obligation, the review concedes non-performance in its own words, and the only
"adjudication" artifacts in the log directory are screening-stage files, not an
extraction reconciliation record.

### SCOPE-1-4 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** omitted
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:194-199 (§2.2), §12.3 VG-4
> **issue:** Protocol §3.3's backward citation-chasing arm (er-bc-*) — the one supplementary method that recovers detectors the seeds do not cite — was never executed. No se-bc-* log exists in the search-log directory. The review self-reports this as a MAJOR protocol-vs-execution gap and compounds it with three known-item recall failures on the pre-2011 antecedent layer (KI-05, KI-13, KI-14), so the corpus's coverage of methodological antecedents rests entirely on the known-item list. The omission is disclosed with correct severity and the conclusions are bounded to 'what the included corpus establishes' — recorded here as documented drift against the frozen search protocol, not as concealment.
> **evidence:** Protocol §3.3: 'Backward citation-chasing: the reference lists of INCLUDED comparison and simulation studies (I2b records) are hand-checked for in-scope detectors not yet retrieved; each such addition is logged with its carrier record (er-bc-{n}).' Review §2.2: 'Backward citation-chasing (er-bc-*): not run. … This is a MAJOR protocol-vs-execution gap'. Directory listing of docs/literature/search_logs/explosive-regime/ contains no se-bc-* or er-bc-* file.

Refutation failed: the 82-file log directory holds no backward-chase log, no
amendment or gate waiver covers the arm, and the three known-item recall failures
reproduce in §2.3. The only discrepancy found is a path label in the
orchestrator's artifact list, outside the defect claim.

### SCOPE-1-5 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** changed
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1864-1878 (§12.1 L-6, L-7)
> **issue:** Two frozen eligibility/deduplication rules were applied differently from their written form: five included records (eru-0100, eru-0112, eru-0268, eru-0427, eru-1310) have no DOI, arXiv ID or Handle and therefore fail I3, which mandates exclusion-with-logging, yet they are inside the frozen 72; and three same-work twins (eru-0622, eru-0154, eru-0904) survive X7 deduplication, so '72 records' is 69 distinct works. Both are disclosed with their consequences (each twin extracted once under its carrier; 69 stated alongside 72 in frontmatter and abstract), and the review declines to re-screen a frozen corpus — documented drift against protocol §2.2 I3 and §2.3 X7, but drift that changes the corpus composition and every record-level count.
> **evidence:** Protocol §2.2 I3: 'A persistent identifier exists (DOI, arXiv ID, or Handle-System handle). A record failing I3 is excluded and logged with its best locator (FAIR F1 gap), not silently dropped.' Review L-6: 'Five included records fail criterion I3 as written … they were included instead. The corpus is frozen and this review does not re-screen it, so the discrepancy is recorded, not repaired.' L-7: 'Three same-work twins survive in the frozen included set … Under X7 they should have been merged.'

Refutation failed: the store's own I3-GAP and twin notes confirm both deviations
machine-readably, no exemption clause exists in protocol §2.2–2.4, and neither
deviation appears in the addendum (A1–A3) or in the review's requested set
(A4–A6).

### SCOPE-1-6 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** partial
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:701-710 ('Residual, carried openly')
> **issue:** The Rev 4 transcription of the review's verdicts is faithful and does not overstate them (universal (d) explicitly remains refuted; the Rev 3 sentence's strength is recorded as falling; SADF/GSADF are barred from the comparator set as online detectors; the NB-13 weakness and its re-openability are carried). But the residual paragraph carries only a subset of the review's own bounding defects: the backward-chase gap, the three known-item recall failures, I3 and X7. It omits the review's LARGEST self-reported completeness threat — 280 records (47.8% of those reaching full text) excluded solely because full text was unobtainable, L-4, VG-2 — and states A4/A5/A6 are 'post-hoc' without carrying what A6 means for the appraisal (L-2: the ER-RoB profile is convention-resolved, not source-adjudicated). A consumer reading the agenda alone would under-bound the corpus.
> **evidence:** Review §12.1 L-4: '280 records (47.8% of those reaching full text) were excluded because full text could not be obtained. This is the largest single threat to completeness and its direction is unknown'. Agenda lines 701-710 name only the er-bc-* arm, the three known-item antecedents, I3 and X7, plus 'Amendments A4, A5 and A6 are post-hoc and labelled as such.'

Refutation failed and produced an aggravating counter-finding: the omission is
document-wide (zero agenda hits for 280 / 47.8 / X6 / 357), and the bound the
agenda does state ("recall-limited on the antecedent layer") is narrower than
L-4 permits.

### QUANT-1-1 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** method
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:279-300, 776-870 (appraisal table); cf. docs/methodology/protocol_explosive-regime-review_2026-08-24.md:526-544
> **issue:** The frozen appraisal instrument ER-RoB v1 declares a three-level response scale; the execution used a four-level scale by adding `partial`, in 50 cells, with no amendment requested. Section 2.7 simultaneously asserts that the instrument was not altered. The frozen concern rule is undefined for the added level, so the domain judgments for those cells rest on an undeclared convention.
> **evidence:** Protocol §6: "ER-RoB v1 — domains and signalling questions (answered yes / no / unclear per included study; \"no\" or \"unclear\" on any question in a domain raises that domain's concern)". Review §2.7: "No other instrument was substituted; no domain or question was added, dropped or reworded." Review §6 legend: "Q-cell values are `yes` / `partial` / `unclear` / `no`". Recount over the 72 parsed appraisal rows: 50 cells carry `partial` (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29). The deviation is absent from I-1..I-6 (§12.2), VG-1..VG-8 (§12.3) and the requested amendments A4-A6 (§12.5).

Refutation failed: an independent recount (handling the escaped `I2a\|I2b` cells
that break a naive parse) reproduces 50 `partial` cells with the stated
per-question distribution, and the only ordering that places `partial` anywhere
is the §2.8 divergence-resolution convention, not the frozen concern rule.

### QUANT-1-2 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** assumption
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:788-793 (legend), 871-920 (§6.1), 81-93 (abstract point 3)
> **issue:** 31 domain cells are recorded `low` although a signalling question in that domain answered other than `yes`, contradicting the frozen instrument's concern rule. The review discloses this as "a few cells". The departure is material to the review's own headline appraisal finding: D4 would be 48 high / 16 low under the frozen rule, not the reported 41 / 23, and the departures run toward LOWER concern, the opposite of the direction-safe posture the review adopts everywhere else (§2.8).
> **evidence:** Protocol §6: "'no' or 'unclear' on any question in a domain raises that domain's concern." Recomputation over the 72 appraisal rows with the protocol's domain-to-question map (D1←Q1, D2←Q2, D3←Q3,Q4, D4←Q5, D5←Q6, D6←Q7, D7←Q8, D8←Q9): 31 violations — D3 21, D4 7 (eru-0238, eru-0604, eru-1044, eru-1604, eru-1155, eru-0198, eru-1770, all with Q5 `no` or `partial` but D4 `low`), D5 2, D6 1. Review §6 legend concedes only "a few cells are consequently less concerning than a mechanical map would give"; §6.1 reading 2 and the abstract both use the 41/23 split.

Refutation failed: the refuter's parse reproduces the published §6.1
distributions exactly and then reproduces the 31 violations with the same
per-domain split and the same D4 record list. Under the protocol's strictly
literal wording the count is 22 rather than 31 — a boundary quibble the claim
itself discloses — and the departure exceeds "a few cells" under either reading.

### QUANT-1-3 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reproducibility
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:34-41 (frontmatter ai_assistance), 262-268 (§2.5), 1819-1827 (L-1), 2354-2364 (AI-assistance statement)
> **issue:** The review declares one base model as the automation tool for screening, adjudication and extraction; the repository's own provenance record for the commit that produced those verdict files declares a different model. PRISMA 2020 item 8 requires the automation tool to be declared with its version, and the review's kappa interpretation ("two context-independent sessions of the same base model") is stated relative to that identity.
> **evidence:** Review frontmatter: "Claude Opus 5 (model id claude-opus-5 …). Screeners A and B, the blind adjudicator, the primary extractor and the independent re-extractor were separately spawned sessions of this same base model." `git log 8aeebfe` ("docs(review): execute registered search + dual screening; explosive-regime corpus fixed at 72", the commit carrying screen-verdicts-R1/R2/ADJ.jsonl and screen2-verdicts-*.jsonl) records trailer `AI-Assistance: claude-fable-5 (role=multi)`; the protocol registration commit 9deee0c carries the same trailer, and protocol frontmatter `ai_assistance` names "Claude Fable 5 (model id claude-fable-5)". `logs/reproducibility/repro_log_f5419aa650e249378ff40828424696bb.json` (the ReproLog cited by 8aeebfe) records no model field, so the conflict cannot be resolved from the logs.

Refutation failed: no alias or equivalence documentation exists anywhere in
`docs/`, the review never mentions the trailer, and the repository's own trails
record spawned branches under the lead session's model id — so the
"subagent-vs-committer" defense does not hold.

### QUANT-1-4 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reproducibility
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2320-2334 (§15 Provenance), 1999 (§12.4 item 27)
> **issue:** The provenance table omits the ReproLog path and SHA-256, the sidecar SHA-256, and the git HEAD that the project reproducibility contract requires of every tracked deliverable; and the conformance map asserts item 27 "met" on the ground that all materials are tracked, which is false for three of the artifacts at the time of writing.
> **evidence:** Project CLAUDE.md: "A tracked deliverable therefore cites the SHA-256 of the ReproLog and the sidecar plus the git HEAD, and labels the path as an untracked locator — never the path alone." §15 lists protocol SHA-256, store SHA-256 and identifier checks but no ReproLog/sidecar digest and no git HEAD. Precedent in the same directory: lit_review_f005-class-n-tests_2026-08-21.md frontmatter carries "Reproducibility log: logs/reproducibility/repro_log_4471f7f2…json (untracked locator; sha256 1b8da281…)". `git status --short` at review time: `?? docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`, `?? docs/literature/references_explosive-regime.json`, `?? docs/literature/search_logs/explosive-regime/se-extraction-recheck.jsonl` — all untracked, against §12.4 item 27 "CSL-JSON stores, 42 raw query logs, six verdict/extraction JSONL files, the protocol and this review, all tracked".

Refutation failed: both halves reproduce at HEAD `27d7473`, and the only
available counter-argument (that the tracked-deliverable clause has not yet
bound) is self-defeating, since the same untracked state falsifies item 27's
present-tense claim.

### QUANT-1-5 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** numerical
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:975-983 (§7.1 synthesis claim) vs 969 (same section's evidence table)
> **issue:** The O1 synthesis claim asserts that every documented departure from the stated null distorts size upward, i.e. toward spurious bubble detection. The review's own evidence table two paragraphs above contains a counterexample in which size collapses toward zero. A downward distortion is a power failure, not a false-alarm failure, and the consumer would draw the opposite operational conclusion.
> **evidence:** §7.1 claim: "Every departure from `iid errors + constant unconditional variance + asymptotically negligible drift + no deterministic trend + no jumps` that the corpus tests produces size distortion, in most cases severe and always upward — i.e. toward spurious bubble detection." §7.1 table row: "| deterministic drift break under the null | DF_μ diverges; size tends to 1 or 0 depending on break sign | `eru-0348` Theorem 1 and Table 2, Sollis 2016 |".

Refutation failed on three angles (scope exclusion, an errata/qualifier search,
and a source check). The corpus's own extraction record for eru-0348 confirms the
downward branch is genuine, and the contradiction is restated at line 1189. The
imprecise locus citation the refuter found is a separate issue.

### QUANT-1-6 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:479-511 (branch 3) vs docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1122-1170 (§7.4), 2299-2305 (§14 item 2)
> **issue:** The Rev 4 transcription into branch 3 carries the statistic-attribution correction and the critical-value non-transferability, but drops the review's two other branch-3-directed verdicts: the measured family-wise false-detection probability of the standard PSY dating recursion, and the recommendation that the surveillance/monitoring line enter the comparator set. Branch 3 therefore admits BSADF as an online comparator with no multiplicity caveat attached, and does not admit the line the review says publishes branch 3's own declared comparison metric.
> **evidence:** Review §7.4: "used as conventionally applied, the PSY date-stamping recursion has a family-wise false-detection probability between roughly one-half and nine-tenths over a decade of data" (FWER 0.55/0.78/0.93, `eru-1289` Table 1) and "the surveillance line is the one that publishes the required quantity, and the recursive family is the one that does not". Review §14 item 2: "The surveillance / monitoring line (`eru-0735`, `eru-1117`, `eru-1519`, `eru-1844`, `eru-1845`, `eru-0889`, `eru-1038`, `eru-1921`, `eru-1852`) does publish a false-alarm rate over a stated horizon in closed form and should enter the comparator set on that ground alone." `grep -n "FWER\|0.55\|0.93\|Astill\|Whitehouse\|multiplicity"` over the agenda returns no hit in branch 3 or Definitional basis (d); the only "multiplicity" hit (line 455) is unrelated (branch 4).

Refutation failed: both review-side quotes reproduce verbatim and are explicitly
branch-3-directed, the agenda-side absence reproduces (zero `eru-` identifiers
anywhere in the agenda), and the candidate counter-reading — the Rev 2
sequential-analysis bullet — is not a comparator admission. Convergent with
REV-1-7.

### QUANT-1-7 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** verification-gap
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1332-1458 (§8), 1488-1666 (§9)
> **issue:** The two deliverables that carry the whole branch-3 precondition — the Phillips confirm-or-correct verdict and the three NB adjudications — rest entirely on verbatim quotations and table/page locations from primary texts that cannot be re-opened in this audit environment (no network, no PDFs in the repository). Method fidelity to the cited sources is therefore asserted, not verified, at the decisive points.
> **evidence:** Load-bearing unverifiable strings include: PWY eq. (8) "r̂ₑ = inf_{s≥r₀} {s : ADF_s > cv_adf(s)}" (IER 52:208); "cv_adf_n(s) = log(log(ns))/100 … around the 4% significance level" (p.208); PSY "the new date-stamping strategy may be used as an ex ante real-time dating procedure, whereas the GSADF test is an ex post statistic" (IER 56:1054); the `eru-1289` FWER triple 0.55/0.78/0.93 (Table 1, Cowles DP 2331 p.21); Johansen & Sornette "we shall take the stretched exponential law as our null hypothesis"; Landriault et al. Theorem 3.1; Baur & Lucey DP 122 pp.4-6. The repository holds no cached full texts for these; the extraction JSONL is a transcription, not the source.

Refutation failed and corroborated the finding. One premise is wrong — network
access exists — but re-opening the sources confirmed the substantive claim and
surfaced the errors it predicts: every §8 page locator the refuter re-checked is
one page high (PWY printed 207/213/214 vs cited 208/214/215; PSY printed
1050/1053/1066 vs cited 1051/1054/1067), and PWY footnote 6 is quoted as verbatim
where the source text is a paraphrase. No route or digest existed by which a
successor could have caught this without repeating the retrieval; §12.3 registers
no such gap. **Retained with its scope corrected**: the defect is the absent
retrieval-provenance record and the resulting unverifiability at the decisive
points, not an absence of network access.

### LITERATURE-1-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** misattributed-source
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:661,1126-1135; docs/literature/references_explosive-regime.json:2359-2379
> **issue:** eru-1289 is cited as 'Shi S, Phillips PCB (2022) … chapter doi:10.1017/9781108910095.003' and tiered 'peer-reviewed chapter', but the DOI resolves to a 2025 Cambridge book chapter while the text actually extracted is the 2022 Cowles DP 2331 working paper. The record is omitted from the version-caveat limitation (L-10) and verification gap (VG-6) that record the two comparable cases.
> **evidence:** Cambridge Core (identifier 9781108910095#c2) gives the chapter in 'Financial Econometrics: Theory and Applications', CUP, 2025, pp. 30–59. Review §5 row 68 dates the record 2022 and tiers it 'peer-reviewed chapter'; §7.4 states 'tier: peer-reviewed chapter, with the Cowles DP 2331 working-paper twin as the extraction source' — i.e. the tier is taken from a version that was not read. L-10 lists exactly three version-caveat records (eru-0150, eru-0259, eru-1715) and VG-6 exactly two; eru-1289 appears in neither, although it carries the review's self-declared 'sharpest' O4 claim and abstract principal finding (4). Protocol §2.4 fixes 'tier RECORDED per record … tier-blind admission with tier-labelled use' and the charter rule that tier travels with the claim.

Refutation failed: an independent CrossRef call (2026-09-02) returns the chapter
issued 2025-04-30, pp. 30-59, edition 1, created 2025-02-20 — so no earlier
edition reconciles the 2022/chapter-DOI pairing — and the version caveat is
registered nowhere else in the review.

### LITERATURE-1-4 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** verification-claim-overstated
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1916-1923
> **issue:** L-13 asserts that exactly 'two metadata discrepancies surfaced at verification'. Independent Crossref checks find at least two further discrepancies in the §5 study-characteristics table (PRISMA item 17), one of them substantial. The positive claim of a completed metadata verification is therefore not supported.
> **evidence:** Crossref 10.1111/jtsa.12784 (eru-1580, Harvey, Leybourne, Taylor & Zu, 'A new heteroskedasticity-robust test for explosive bubbles') = J. Time Series Analysis 46(5):846–866; review §5 row 60 gives 46(1):102–132. Crossref 10.1111/jtsa.12845 (eru-1852, Breitung & Diegel) = 46(5):829–845; review §5 row 37 gives 46(5):828–847. Neither appears in L-13, which names only eru-1384 and eru-1761. Spot checks of 10.1111/obes.12540 (eru-1519) and 10.1016/j.ijforecast.2024.12.005 (eru-1844) matched exactly, so the error is not systematic — it is an incomplete check reported as a complete one. The CSL store carries no page field for these records, so §5's page ranges rest solely on the extraction stage's E1 strings.

Refutation failed: the refuter's own Crossref calls reproduce both discrepancies
and both non-discrepant controls, so no systematic-offset explanation is
available; the only verification the review documents is DOI Handle resolution,
which does not license a bare count of two metadata discrepancies.

### LITERATURE-1-6 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consumer-transcription-omission
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:701-710
> **issue:** The agenda Rev 4 'Residual, carried openly' paragraph carries the backward-chase gap, the three known-item antecedent recall failures, the I3 failures, the twins and the post-hoc amendments — but drops the review's own largest declared threat to completeness: 280 records (47.8% of those reaching full text) excluded because full text was unobtainable, direction unknown.
> **evidence:** Review L-4 / VG-2: '280 records (47.8% of those reaching full text) were excluded because full text could not be obtained. This is the largest single threat to completeness and its direction is unknown … Nothing in this review can bound the number of eligible studies lost this way.' The agenda's residual paragraph instead bounds the corpus only 'on the antecedent layer'. Amendment A6 is named at line 710 without its content (90 of 357 comparable appraisal cells diverged between extraction passes and were resolved by a post-hoc conservative rule, review §2.8 / L-2), so a reader of the agenda alone cannot tell that the appraisal profiles it relies on are direction-safe but unadjudicated.

Refutation failed: zero agenda matches for 280 / 47.8 / X6 / 357 / reconcil, and
the single "A6" occurrence carries no content. Convergent with SCOPE-1-6 and
QUANT-1-12.

## deferred-logged-minors

Twenty-one minors logged, not remediated this round (full payloads in the JSON
sidecar; compressed rows in the findings table above). Convergent clusters are
grouped so remediation can address them once:

- **REV-1-9 / QUANT-1-14 / LITERATURE-1-10** (reporting / search-reporting
  accuracy, three-way convergent): "42 executed query logs" is a protocol-query-id
  count reported as a file count (58 files carry a `retrieved_count`; 60 query-log
  files exist), and "six verdict/extraction JSONL files" undercounts the eight
  that exist. State both numbers explicitly at §2.2, §3.1, §12.4 item 7 and §15.
- **REV-1-8 / QUANT-1-8** (consistency / numerical, convergent): the O6 fraction
  "fewer than one in three" is false on its own denominator (22/65 = 33.8%) and
  the denominator itself is inconsistent with the review's causality coding
  (66 records carry an extracted status). Give the count and its derivation.
- **QUANT-1-9 / LITERATURE-1-7** (reporting / internal-attribution
  inconsistency, convergent): §7.4's concern profile for `eru-1289` says D4 low
  where the §6 row and the extraction record both say D4 high — a misreport in
  the direction of confidence on the review's most consequential claim. Correct
  it and re-sweep the other per-claim concern-profile sentences in §7.
- **QUANT-1-12** (reporting): the agenda residual paragraph omits L-1
  (single-model screening) as well as L-4; convergent with SCOPE-1-6 and
  LITERATURE-1-6, which are majors and are being remediated.
- **QUANT-1-11 / LITERATURE-1-2 overlap** (reporting): `eru-1289` is missing
  from the §5.4 version-caveat list and VG-6; the major LITERATURE-1-2 covers
  the year/tier pairing, this minor covers the enumeration and the abstract's
  unqualified FWER sentence.
- **REV-1-10** (reporting): κ reported to six decimals with no interval.
- **REV-1-11 / LITERATURE-1-9** (consistency / citation-year, convergent):
  NB-02's preprint-twin adjudication is recorded only inline while the identical
  NB-13 defect is VG-3, and the record's year is 2001 in protocol and review but
  2002 in the agenda.
- **REV-1-12** (reporting): no statement of the synthesis's relation to
  published surveys of the same literature, several of which sit inside the
  corpus.
- **SCOPE-1-7** (documented-drift): "one appraisal row per included study" is met
  at row level (72) but not at appraisal level (65 appraised, 14 single-pass).
- **SCOPE-1-8** (spec-conflict): delivered review filename vs the frozen
  protocol's `planned_outputs` pattern; declared as A4, unappended.
- **SCOPE-1-9** (documented-drift): the Thread A audit trail did not exist at
  audit time — **discharged by this document**; the sidecar SHA is recorded in
  the front matter.
- **SCOPE-1-10** (documented-drift): protocol §8 item 1's citation-uptake check
  is unrunnable against a corpus X1 constructs; substitution declared as L-8/I-2.
  **No action on this artifact**; carry I-2 into the successor protocol.
- **QUANT-1-10** (reporting): the twin-identifier crediting rule for I3 is
  applied inconsistently and never stated; convergent with the major REV-1-2.
- **QUANT-1-13** (reporting): the non-suppression conclusion's proportion half is
  computed over an availability-selected subset (53 of 72) and is not hedged at
  §10.1.
- **LITERATURE-1-8** (imprecise-attribution): the O4 evaluation-criteria taxonomy
  is attributed to Frisén 2003 rather than Frisén 1992; both citations verified
  correct in themselves.
- **LITERATURE-1-11** (canonical-form-mismatch): the PWY null limit is written
  with undemeaned W and no window fraction, contradicting the demeaned regression
  described in the same cell.

Per project policy, logged minors are carried on the trail and addressed
opportunistically or in a later spec; they do not gate the round verdict. The
open minors from the phase1-sweep, round3-remediation and naming-sweep specs
remain open by policy and were not re-raised.

## verification-of-remediations

**Nothing to verify from a prior round of this loop.** This is round 1 of a fresh
3-round cap (`rounds_completed: 1`, `cap_reached: false`, `prior_dispositions:
null`); no round-0 remediation exists to confirm, and this file has no prior
round section.

**Positive verifications performed this round** (checks that closed rather than
opened items):

- *Flow accounting (focus b).* The PRISMA identification/screening/inclusion
  identities were recomputed independently by two branches from the primitive
  verdict files, not from `se-included-set.json`: all eight JSONL row counts
  (1,996 / 1,996 / 386 stage-1; 586 / 586 / 16 stage-2; 73 primary extraction
  rows including the adjudication row; 65 recheck rows), every stage-1 and
  stage-2 verdict marginal, the stage-2 crosstable's consistency with the R1/R2
  marginals (INCLUDE 119, EXCLUDE 340, X6 713), the kappa 2×2 and κ itself
  (κ = 0.433012, p₀ = 0.806613, pₑ = 0.658923), the 90/357 dual-pass divergence
  split, all 234 §13 exclusions and every record-to-DOI pairing reconcile with
  zero mismatches. No finding was raised against the flow.
- *Dagger convention (focus c, first half).* Exactly 90 Q-cell daggers, with the
  declared per-question distribution Q1 6 / Q2 7 / Q3 3 / Q4 23 / Q5 14 / Q6 12 /
  Q7 25; single-pass rows are marked `‡` and no-full-text rows are marked, as
  declared. The appraisal table carries exactly 72 rows and
  `references_explosive-regime.json` exactly 72 ids. The defects found in the
  appraisal layer (REV-1-3, QUANT-1-1, QUANT-1-2, SCOPE-1-7) concern the domain
  column, the response scale and the effective denominator — not the dagger
  bookkeeping.
- *Phillips verdict on the merits (focus d).* Confirmed sound by two branches:
  the restriction of "in real time" to ADF_r/BSADF and its denial to SADF/GSADF
  rests on verbatim authorial statements in both papers (PSY 2015a's ex-ante /
  ex-post split verified against indexed source text), and the denial of "against
  derived critical values" on Monte-Carlo provenance is correct and correctly
  distinguished from PWY's log(log(ns))/100 divergence convention. The attempt to
  widen this into a defect (LITERATURE-1-3) was **refuted** at the gate with a
  line-anchored reproduction, and the agenda's inherited wording was verified to
  match the review's prescribed Rev 4 text.
- *Standards and NB citations (focus e).* All eight standards/method citations in
  §15 (PRISMA 2020, PRISMA-P, PRISMA-S, Cohen 1960, QUADAS-2, PROBAST, Egger
  1997, Frisén 2003) verified correct in title, journal, year, volume and pages.
  All three NB records verified in title, authors, journal, volume, issue and
  pages. The §9.3 NB-13 version caveat is factually accurate — the defect
  (REV-1-6) is the unqualified verdict *label* and its propagation, not the
  caveat's content.
- *Agenda transcription, positive half (focus g).* Verified faithful and not
  overstated on the points the spec names: universal (d) remains explicitly
  refuted, the Rev 3 sentence's strength is recorded as falling, SADF/GSADF are
  barred from the comparator set as online detectors, and the NB-13 weakness and
  its re-openability are carried at the Definitional-basis and Verification-status
  sites. The transcription defects found (REV-1-7, SCOPE-1-6, QUANT-1-6,
  LITERATURE-1-6, QUANT-1-12) are omissions and under-bounding, not overstatement.

**This round's remediations (24 retained majors): pending at trail-writing
time.** The round verdict is proceed-with-remediation; remediation follows this
trail. Three clusters carry most of the work and are each remediable as a unit:
the **amendment-register cluster** (REV-1-1, SCOPE-1-2, SCOPE-1-5, SCOPE-1-1,
QUANT-1-1, plus minor SCOPE-1-8 — append A4–A6 and the newly required entries to
the frozen addendum and re-digest); the **denominator-and-instrument cluster**
(REV-1-2, REV-1-3, REV-1-4, QUANT-1-2, plus minors QUANT-1-10 and SCOPE-1-7); and
the **agenda-transcription cluster** (REV-1-7, SCOPE-1-6, QUANT-1-6,
LITERATURE-1-6, plus minor QUANT-1-12 — one rewrite of branch 3 and the residual
paragraph discharges all five). Verification evidence for the majors (post-fix
artifact digests and, if a round 2 runs, the round-2 branch confirmations) is to
be appended as the next round section of this file — prior entries are never
edited. The `/commit-with-provenance` step lands after remediation; its
trailer-bearing commit hash is to be recorded here as a dated addendum.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Four specialist branches read three artifacts against the frozen
protocol, the deliverable spec, the primitive search logs and a subset of the
cited primary sources; they did not exhaustively verify every sentence, every
citation-claim pairing, every extracted numeral, every appraisal cell against its
source text, or every cross-artifact dependency. Absence of a finding is not
evidence of absence of a defect — the same asymmetry the charter enforces for
statistical nulls applies to this audit's own coverage. Two concrete
demonstrations of that asymmetry arose this round: a page-locator off-by-one
running through §8 was found only because a refutation attempt happened to
re-open the sources, and 2 of 6 Crossref spot checks on the §5 table failed,
implying an unknown error rate across the ~56 unchecked rows.

**Per-branch residual risk** (full statements verbatim in the sidecar):

- *critical-reviewer.* Design and conduct are the strongest part of the
  deliverable and carry no critical defect: the protocol was frozen and committed
  before execution, eligibility criteria were not reinterpreted, the pooling
  condition was pre-specified and its failure documented per characteristic, no
  vote counting is presented as inference, and the §9.1 adjudication criteria were
  fixed in advance. Residual risk concentrates in three places — the appraisal
  layer (the domain column is not rule-derived and the 90 divergent cells were
  never adjudicated against source text, so the corpus-level concern profile is an
  artefact of two undocumented decisions layered on each other, and no reader can
  reconstruct which); the recall bound (with the backward arm unexecuted and 47.8%
  of full-text-stage records unobtainable, no negative statement about what this
  literature contains is safe); and transcription loss into the consumer agenda.
  One item could not be settled from the artefacts: whether the twin records
  eru-0154 and eru-0904 were counted as separate records in any §7 numerator.
- *scope-auditor.* Presence-side coverage of the declared spec is high — every
  Thread A state clause has a located artifact section. The residual risk is not
  omission of promised sections but that several protocol-mandated *procedures*
  behind those sections did not run (backward-chase arm, dual-extraction
  reconciliation, NB force-screening), and that three declared amendments live
  only in the review. This branch checks presence, not correctness: no arithmetic
  identity, extracted numeral, page citation or substantive verdict was verified
  here. Highest remaining scope risk: a reader taking the agenda's Rev 4 residual
  paragraph as the full bounding of the corpus would miss the 280-record X6
  exclusion class.
- *quant-auditor.* The bookkeeping is verifiably exact, so residual risk is
  concentrated where the logs cannot adjudicate: whether the quotations and table
  values transcribed from the six primary texts in §8–§9 (and the FWER triple)
  faithfully reflect those sources, and whether the 280 unobtainable full texts
  and the never-executed backward arm conceal a detector line or a matched-design
  pair that would change the O1/O4 verdicts.
- *literature-check.* 24 citations resolved and checked. Residual risk in three
  places: no PDF could be text-extracted in that branch's environment, so PWY
  2011's quotations and `eru-1289`'s FWER values were unconfirmed there by a
  second retrieval (both were subsequently retrieved and confirmed by the
  refuter, dropping LITERATURE-1-1 and LITERATURE-1-5); the §5 citation strings
  are extraction-stage transcriptions with no Crossref cross-check in the CSL
  store and 2 of 6 spot checks failed, so an unknown number of the remaining ~56
  rows carry page/issue errors; and the per-claim certainty apparatus (tier +
  concern profile) is mis-stated in at least one high-consequence instance
  (`eru-1289`), so the tier-travels-with-the-claim rule should be re-swept, not
  spot-fixed. None of the findings overturns the PARTIAL verdict on the agenda
  sentence, the three episode-statistic-null adjudications, or the agenda's
  retention of universal (d) as refuted with reduced sentence strength.

**Cross-branch residual.** The audit did not itself re-derive any of the six
primary texts' substantive results, did not re-run the search, and did not
adjudicate any of the 90 divergent appraisal cells against source text. The
review's central verdicts (the Phillips confirm-or-correct and the three NB
adjudications) survive this round, but their evidentiary base is a single
retrieval session whose provenance record is the defect QUANT-1-7 names.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Opus 5 (model id `claude-opus-5`, Anthropic, via Claude
  Code / Claude Agent SDK) — all branches: four specialist audit agents
  (critical-reviewer at high effort, scope-auditor at medium effort,
  quant-auditor at high effort, literature-check at high effort, each with
  `model: inherit` in its agent definition), the adversarial refuter (high
  effort), and the trail-assembly agent that authored this document.
- Roles: audit (findings, refutations, independent recomputation of the PRISMA
  flow and κ, independent retrieval and re-reading of primary sources) and prose
  (assembly of this trail). No authored research content; the audited artifacts
  were not modified by this round's agents.
- Note recorded rather than resolved: QUANT-1-3 (retained) concerns a model-id
  conflict between the audited review's own declaration (`claude-opus-5`) and the
  provenance trailers on the commits that produced its verdict files
  (`claude-fable-5`). That conflict is a property of the audited artifacts, not
  of this audit; the model id declared here is this audit's own.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the verdict and remediations proceed.
- Reproducibility log: ReproLog emission is sequenced with the
  `/commit-with-provenance` step; the log lands at
  `logs/reproducibility/repro_log_{run_id}.json` (gitignored, an untracked
  locator), and its clone-durable digest is carried by the commit's
  `Repro-Log-Path:` / `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility
  contract. The commit hash is to be recorded here as a dated addendum when it
  lands.

## immutability-and-retention

This trail and its JSON sidecar
([audit_trail_phase2-explosive-review_2026-08-24.json](audit_trail_phase2-explosive-review_2026-08-24.json),
SHA-256 `221d4f241b04bba99af67097508e221eba9cc26207add417bd7bdb6bfd8d96ca`,
holding the round-1 payload verbatim per FAIR I1) are committed to the repository
and are **append-only**, per 21 CFR 11.10(e): record changes must not obscure
previously recorded information. Later rounds of this loop append new round
sections to this file; corrections to any recorded entry are appended as a dated
addendum that identifies what it corrects — prior entries are never edited,
overwritten, or deleted. Retention follows the repository's git history; the
tracked file is the durable record, and the front-matter digests bind it to the
exact artifact states audited (HEAD `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`,
`worktree_clean: false`).

---

# Audit trail — Phase 2 explosive-regime review close-out, round 2

Appended round section per 21 CFR 11.10(e): the round-1 entries above are
unmodified. Round 2 is a verify-and-hunt round over the 24 round-1 retained
majors — all 24 remediated by the lead between rounds — and over what those
remediations introduced. Five branches routed (`reproducibility-verifier` added
to the round-1 four). All five branch verdicts: **proceed-with-remediation**.
Round verdict: **proceed-with-remediation** (0 critical, 30 majors raised, 0
refuted at the gate, 30 majors retained for remediation, 15 minors logged, 0
retained-conservative).

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
title: "Audit trail — Phase 2 explosive-regime review close-out, round 2"
type: audit_trail
date: "2026-08-24"
started_at: "2026-09-02T12:41:07-05:00"
ended_at: "2026-09-02T13:12:55-05:00"
artifacts:
  - {path: "docs/literature/lit_review_explosive-regime-dating_2026-08-24.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "40bc4ae30a4c731a6fa33dabf835b6c197d8486100976efd7efe5a65e52460ef"}
  - {path: "docs/literature/references_explosive-regime.json", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "2ad84ee0374cf6d2924852a640006e086d3d9e51205eeba65c7253766f0007a3"}
  - {path: "docs/methodology/protocol_explosive-regime-review_2026-08-24.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b"}
repo_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A — Phase 2 explosive-regime review close-out. Item 1: PRISMA 2020 review over the frozen 72-record included corpus with flow accounting reconciling against the search logs and kappa records, one appraisal row per included study using the protocol's declared instrument, synthesis of operating characteristics and validity conditions, full-text extraction for BOTH Phillips records, explicit adjudication of NB-02/NB-08/NB-13 against the time-t assignment-null standard, publication-bias posture per protocol, limitations mapping residual PRISMA gaps. Item 2: agenda rev 4 carrying the review's verdicts without overstating them. ROUND 2 — VERIFY THE ROUND-1 REMEDIATIONS AND HUNT WHAT THEY INTRODUCED. Round 1 raised 27 major findings, refuted 3, retained 24, and all 24 have now been remediated. Do NOT re-raise a round-1 finding that is genuinely fixed; DO verify each fix actually holds, and DO raise anything the remediation itself broke or overstated. Specific claims to verify: (1) protocol amendments A4-A11 appended to the addendum with the frozen prefix byte-identical — the lead has independently confirmed the first 51478 bytes still hash to 33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54 and the full file now hashes to 0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b; check the amendment CONTENT is accurate, dated, stage-named, PRISMA-P-itemised and post-hoc-flagged, not merely present. (2) The I3 count is now seven everywhere with the twin-does-not-inherit rule stated; store carries 7 I3 GAP notes (lead confirmed). (3) The new D-rule column in section 6: verify it is correctly derived from the Q cells for all 72 rows, that the 31 lenient-direction markers and 13 opposite-direction markers are right, and that section 6.1 and the abstract now rest on the rule-derived column with the recorded column as sensitivity. The remediation claims the audit only named the lenient direction and it found 13 running the other way — check that claim. (4) Assessable denominators 65 and 53 applied at every coverage-fraction site with excluded classes named. (5) The backward citation-chasing arm was EXECUTED post-freeze under amendment A11 via Crossref reference arrays and OpenAlex referenced_works rather than the hand-checked PDFs section 3.3 specifies — a declared route deviation. 27 I2b carriers targeted, 22 covered, 392 unique referenced DOIs, 177 absent from the universe, 2 candidate additions found (er-bc-1 Hall/Psaradakis/Sola 1999; er-bc-2 Banerjee/Chevillon/Kratz 2013) and NEITHER admitted because the corpus is frozen. Assess: is the route deviation adequately declared, is refusing to admit a probable eligible miss the right call or does it need its own disclosure, and is the claim that the gap is now bounded-and-named rather than closed accurate. (6) NB-13 retained episode-statistic-null as provisional-on-the-twin rather than relabelled indeterminate-from-full-text, with the justification that a full text WAS read and DID decide under section 9.1(iv) and the ambiguity is about which version the label attaches to. Adjudicate that reasoning. (7) The O4 claim rewritten corpus-scoped. (8) Model-identity conflict QUANT-1-3 stated as UNRESOLVABLE from the logs rather than resolved, with kappa restated as surviving within the screening stage only. Check the honesty and completeness of that treatment. (9) LITERATURE-1-4: a full Crossref check across 62 of 62 DOI-bearing records now reports 13 metadata discrepancies plus 3 pagination updates, 1 version misattribution, 1 unverifiable and a year-of-record CONVENTION covering 7 online-first/print divergences. Spot-verify a sample of these against Crossref and check L-13 now states the check's completeness accurately. (10) eru-1289 re-tiered working-paper with the FWER claim's tier travelling with it. (11) The agenda: the lead remediated REV-1-7, QUANT-1-6, LITERATURE-1-6 and SCOPE-1-6 plus propagated the seven-not-five correction and the NB-13 provisional status; verify branch 3 now carries the FWER 0.55-0.93 condition, the surveillance-line comparators, and TC-4, and that the residual paragraph carries the 280-record 47.8 percent completeness threat and the A6 convention-resolved appraisal caveat. (12) Sections 9.5 and 16 are new — verify the retrieval-route and traceability records are accurate and that the four unre-fetchable primary texts are correctly marked as single-session transcription.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md", sha256: "6425f053ce0e3dfd0554d7a103f3f65b76fdd46b95f4c4df6b5147eafd30e17d"}
    - {path: "docs/methodology/protocol_explosive-regime-review_2026-08-24.md", sha256: "0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b"}
mechanism: "Workflow engine \u2014 workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill). Round 2 is a verify-and-hunt round: each round-1 remediation was re-derived independently where mechanically checkable, and every new critical/major finding passed the refute gate."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "quant-auditor", agent_def_path: "~/.claude/agents/quant-auditor.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "reproducibility-verifier", agent_def_path: "~/.claude/agents/reproducibility-verifier.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-opus-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala \u2192 lead orchestrator session (Claude Opus 5, claude-opus-5) \u2192 workflows/audit-remediate.js \u2192 routed specialist branches (critical-reviewer, scope-auditor, quant-auditor, literature-check, reproducibility-verifier) \u2192 adversarial refuter \u2192 trail-assembly agent (this round section)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. Five branches routed. The round-1 four are re-routed for continuity of verification over the same three artifacts plus the now-amended protocol: critical-reviewer (adequacy of the 24 remediations, interpretation and RQI dimensions) high; scope-auditor (declared-spec coverage and consumer-artifact fidelity) medium; quant-auditor (independent re-derivation of the D-rule column, the assessable denominators, the partial-cell and divergence counts, and live Crossref re-checks) high; literature-check (primary-source and identifier re-verification, the NB adjudications, the backward-chase candidates) high. reproducibility-verifier is added this round because the remediation introduced digest-, ReproLog- and retrieval-route claims (\u00a79.5, \u00a715, A11, se-bc-01.json) that are re-derivable and were not part of round 1's routing; medium effort. epi-auditor was not routed (no population-health artifact, no human-subjects data)."
rounds_completed: 2
rounds_cap: 3
cap_reached: false
verdict: "proceed-with-remediation"
counts: {raw_critical: 0, raw_major: 30, raw_minor: 15, refuted: 0, retained_conservative: 0, to_remediate: 30, minors_logged: 15}
sidecar: {path: "docs/audits/audit_trail_phase2-explosive-review_2026-08-24.round2.json", sha256: "b62e57f063baf5f4c4a1a5d23c2d38ed246114ef8ecc912e53df3df50c26edba"}
```

Notes on the round-2 record: `started_at`/`ended_at` are the trail-assembly
interval for this round section. Three of the four audited artifacts moved
between rounds — the review from `4dd5a3f6…` to `40bc4ae3…`, the included-corpus
store from `1abbb9d8…` to `8ed6f9ca…`, the agenda from `7e29fcde…` to
`2ad84ee0…` — and the frozen protocol is added to the artifact set this round
because the remediation appended amendments A4–A11 to its addendum, moving it
from the registered digest `33c01c5225…` (still the digest of the first 51,478
bytes) to `0c961d3089…`. The deliverable spec also moved (`f3160c5e…` →
`6425f053…`) and is recorded at its round-2 digest. `repo_head` is unchanged at
`27d74738…`: the remediation is in the worktree and not yet committed, so
`worktree_clean: false`. The round-2 sidecar is a separate sibling file so that
the round-1 sidecar (whose SHA-256 is bound into the round-1 front matter above)
remains byte-identical, per append-only retention.

## findings-table

Round 2 raised zero critical findings, 30 majors and 15 minors. The counts
object, verbatim from the round payload: raw_critical 0, raw_major 30,
raw_minor 15, refuted 0, retained_conservative 0, to_remediate 30,
minors_logged 15. One row per finding — all eight schema fields (id, severity,
category, location, issue, evidence, fix, reference) plus branch and disposition;
issue, evidence and fix are compressed for tabular legibility, and the full
unabridged text of every finding, every refutation and every per-branch
residual-risk statement is held in the JSON sidecar. Convergent clusters (one
defect, several branches) are noted after the table.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-2-1 | major | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:364 | The QUANT-1-3 remediation reconciled the automation-tool identity per stage in the frontmatter, L-15, VG-11 and the §15 AI-assistance statement (screening declared `claude-fable-5`), but §2.5's "Honest compliance statement, as executed" was not updated and sti … | **Honest compliance statement, as executed.** Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5). | Replace `(claude-opus-5)` at §2.5 with the per-stage declaration (`claude-fable-5` per the `8aeebfe` trailer, with the conflict pointer to L-15/VG-11), or drop the model name and cross-reference §15. … | PRISMA 2020 item 8; CHAMP item 19 (reporting consistency); round-1 finding QUANT-1-3 | critical-reviewer | retained — remediate |
| REV-2-2 | major | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:113-116, 1608-1609 | The REV-1-4 assessable-denominator remediation was applied inconsistently to O6. The abstract defends 72 as "the right denominator" for three counts that sum to 63, not 72 (the remaining 9 records are SPLIT 3, NS 2, NE 4), while §7.6 uses 65 and asserts "fewer … | (2) 22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the record set, so 72 is … | Fix one denominator for O6 and use it at both sites. If 65 (assessable, excluding 4 NE and 3 twins) is chosen, state 22 of 65 (34%) and delete "fewer than one in three"; also note that 2 of those 65 a … | CHAMP items 17, 19; SAMPL §Basic statistical reporting (denominators and numerators for every proportion); round-1 finding REV-1-4 | critical-reviewer | retained — remediate |
| REV-2-3 | major | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:899-900, 691-697, 1579-1586, 2228-2230 | §5.3, L-7 and amendment A10(b) all assure the reader that the three same-work twins cause no double-counting, and §6.1 excludes them from every assessable denominator. But the record-level distributions in §4 (O6, evidence tier, authorship lineage, extraction … | Each twin is extracted once, under its carrier, so no operating characteristic is double-counted in the synthesis. … Authorship lineage across the 72 records: **21** carry a PSY-lineage author (Philli … | Narrow the §5.3/L-7/A10(b) assurance to "no operating characteristic in the §7 evidence tables is double-counted" and add the distinct-work counts alongside the record counts in §4, §7.6 and §10.2 (O6 … | CHAMP items 17, 19; PRISMA 2020 item 17; round-1 finding SCOPE-1-5 | critical-reviewer | retained — remediate |
| REV-2-4 | major | design | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2018, 2029-2032; docs/methodology/protocol_explosive-regime-review_2026-08-24.md:598- … | The REV-1-6 remediation ships NB-13's verdict as `episode-statistic-null` carrying a new scope qualifier, "PROVISIONAL ON THE WORKING-PAPER TWIN", which the frozen §9.1 verdict vocabulary (assignment-null / episode-statistic-null / mixed / indeterminate-from-f … | **Verdict: `episode-statistic-null` — PROVISIONAL ON THE WORKING-PAPER TWIN.** … The verdict token therefore stays inside the frozen vocabulary and unaltered; **"provisional on the working-paper twin" … | Append amendment A12 to the protocol addendum recording the §9.1 verdict-vocabulary scope qualifier: what it is, why `indeterminate-from-full-text` was not used, that it attaches to the adjudicated ob … | Protocol §9.1 frozen verdict vocabulary; protocol §10 amendments policy; CHAMP item 5 (design violations declared); precedent set by amendme … | critical-reviewer | retained — remediate |
| REV-2-5 | major | interpretation | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1223-1225, 1513-1515 | The reading rule that governs every count in §7 — and that the REV-1-13 remediation quotes verbatim as its authority for corpus-scoping the O4 claim — itself states the wrong scope: it says a count of records is a fact about "the literature's coverage". Over a … | Reading rule, stated once and applied throughout: a count of records is a fact about the literature's coverage, never a fact about a detector. … The review's own reading rule applies to this claim as … | Restate the reading rule as "a count of records is a fact about *this corpus's* coverage, never about the literature and never about a detector", and propagate the corrected wording to both quotation … | CHAMP item 30 (conclusions limited to what the analysis supports); SAMPL §Basic statistical reporting (report a measure of precision with an … | critical-reviewer | retained — remediate |
| REV-2-6 | major | interpretation | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1631-1635 | The REV-1-13 remediation attached the L-4/L-5 recall bound at the point of claim in §7.4 and §7.8, and states that the O5 template is the standard to follow. §7.7 was not brought to that standard: its outcome is generalised from the corpus to "the state of the … | **Outcome: structured no-meta-analysis**, exactly as the protocol anticipated. The failure is systematic rather than incidental — this literature's Monte Carlo designs are chosen to display each new m … | Rewrite §7.7's closing sentence corpus-scoped on the O5/§7.4 template; label the outcome as the pre-registered expectation confirmed rather than as a finding; and attach the A11 bound at the point of … | CHAMP items 28, 30; protocol §7 15c (pre-registered expectation); round-1 finding REV-1-13 | critical-reviewer | retained — remediate |
| REV-2-7 | major | interpretation | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:529-530 | The REV-1-13 corpus-scoping did not propagate to the consumer artifact. The agenda's branch-3 Rev 4 text carries the O4 claim as an unscoped universal negative about the recursive family, which is the exact defect the review remediated in §7.4 ("A delay-versus … | **No BSADF comparator specification in this branch may be written without stating which of the two it uses and carrying the corresponding cost.** The recursive family does *not* publish this branch's … | Rewrite as "No record in the 72-record explosive-regime corpus publishes this branch's own declared comparison metric (delay against ARL₀) for the recursive family; the corpus lost 47.8% of its full-t … | CHAMP item 30; review §7.4 "Recall bound attached at the point of the claim, not deferred to §12.1"; round-1 findings REV-1-13, REV-1-7 | critical-reviewer | retained — remediate |
| REV-2-12 | major | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:394-395, 975-976, 2646; docs/methodology/protocol_explosive-regime-review_2026-08-24. … | The `partial`-cell denominator 585 contradicts the review's own assessable denominators. 585 is 65 records × 9 questions, but the review states that Q8 and Q9 are unanswerable for 12 recheck-only records, so the number of answered Q-cells is 65×7 + 53×2 = 561. … | Execution used a **four-level** scale by adding `partial`, in **50 of the 585 answered Q-cells** (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29). | Correct the denominator to 561 at §2.7, §6, and §12.4 item 11, showing the arithmetic (65×7 for Q1–Q7 plus 53×2 for Q8/Q9). Because A7 is inside an append-only addendum, do not edit it; append a short … | SAMPL §Basic statistical reporting (numerator and denominator for every reported proportion); CHAMP item 19; round-1 findings QUANT-1-1, REV … | critical-reviewer | retained — remediate |
| SCOPE-2-1 | major | partial | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:751-755 | The agenda's Rev 4 residual paragraph — itself rewritten in this remediation round for SCOPE-1-6 — still asserts that the backward citation-chasing arm 'never executed', which the SCOPE-1-4 remediation superseded on the same day, and it carries neither of the … | Agenda l.751-755: '**Antecedent layer specifically.** The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed, and three known-item antecedents ... were recovered by the … | Replace 'never executed' with the executed-post-freeze status under A11 (22 of 27 carriers, deposited reference lists, single-agent, not a screening stage) and name `er-bc-1` Hall/Psaradakis/Sola 1999 … | deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A item 2 ('Branch 3 integrates the review's verdicts'); review §14, A11 | scope-auditor | retained — remediate |
| SCOPE-2-2 | major | omitted | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:730-735, 769 | The review's §14 item 3 — the transcription contract for the agenda — directs the agenda to record that none of NB-02/NB-08/NB-13 ever entered the screened universe as protocol §9.1 required (amendment A9, VG-9). The agenda records the three verdicts and NB-13 … | Review §14 item 3 (l.3003-3006): 'Record also the NB-08 derivability note ... and the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9).' Agenda l.730 … | Add the A9/VG-9 disclosure to the NB bullet, and replace the A4-A6 sentence with the full A4-A11 post-hoc set, naming A9 (force-screening not executed), A10 (I3/X7 violations inside the frozen set) an … | review §14 item 3; protocol addendum A4-A11 | scope-auditor | retained — remediate |
| SCOPE-2-3 | major | partial | C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:938-943 vs 883-914; protocol A10(b) | The X7 drift declared by the round-1 remediation (amendment A10(b), §5.3, and the '72 records / 69 distinct works' figure repeated in the abstract, §6, §12.5 and the agenda) enumerates exactly three same-work twin pairs. §5.4 of the same document documents a f … | §5.4 l.938-943: '`eru-0259` Franses (2016) ... extraction was performed on the working-paper twin `eru-0198` (Econometric Institute Report 2013-12). Twin status was verified against the published arti … | Either extend A10(b), §5.3, the store notes and the distinct-works count to the `eru-0198`/`eru-0259` pair (72 records / 68 distinct works, one appraisal row voided or marked `—`), or state explicitly … | protocol §2.3 X7; amendment A10(b); round-1 finding SCOPE-1-5 | scope-auditor | retained — remediate |
| SCOPE-2-4 | major | partial | C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:113-116, 1579-1586, 1608-1609, 694 | The REV-1-4 remediation requires every coverage fraction to be stated over a named assessable denominator with the excluded classes named. The O6 site fails on both counts and now contradicts itself in three places: the abstract asserts the partition is over 7 … | Abstract l.114-116: '22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the rec … | State the O6 denominator once and consistently — 68 records with an extracted causality status (72 minus the 4 NE), or 72 for the full partition — and name the excluded classes (SPLIT, NS, NE) at the … | round-1 finding REV-1-4; §6.1 denominator rule | scope-auditor | retained — remediate |
| QUANT-2-1 | major | numerical | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:394,976,2697,3110 and C:/Users/skoir/castles/docs/methodology/ … | The remediation's own denominator for the response-scale deviation is wrong and contradicts the assessable-denominator rule the same remediation installed. 'partial in 50 of the 585 answered Q-cells' uses 65x9=585, i.e. it counts the 24 Q8/Q9 cells of the 12 r … | Recount over the §6 table (parser handling escaped pipes): total answered Q cells = 561; 585 - 561 = 24 = 12 recheck-only records x {Q8,Q9}. Per-question partial counts (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, … | Append a new addendum entry A12 correcting A7's denominator to 561 (50/561 = 8.9%) with the exclusion classes named (4 no-full-text, 3 twins, 12 recheck-only x Q8/Q9); A7 itself cannot be edited under … | protocol §10 (append-only addendum); PRISMA 2020 item 13a/18, doi:10.1136/bmj.n71 | quant-auditor | retained — remediate |
| QUANT-2-2 | major | reporting | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1608-1613 (§7.6 synthesis claim O6) | The O6 synthesis claim — the domain the consumer agenda's standing hazard turns on — rests on a denominator that is not derivable from the review's own O6 distribution, and the directional statement is false at that denominator. §7.6 says 'Of the 65 records wi … | Recount of the §5 table's O6 column: Counter({'FS': 22, 'RT': 22, 'CS': 19, 'NE': 4, 'SPLIT': 3, 'NS': 2}) = 72; the three twins carry O6 codes (eru-0154 CS, eru-0622 FS, eru-0904 CS), so the 65 used … | State the O6 fraction as 22/66 records with an extracted status (or 22/72 over the full partition), name the excluded classes (4 NE, 2 NS), and replace 'fewer than one in three' with the arithmeticall … | PRISMA 2020 item 20b (synthesis results with denominators), doi:10.1136/bmj.n71 | quant-auditor | retained — remediate |
| QUANT-2-3 | major | numerical | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1237,1430,1592,1743,1825,2148-2149; C:/Users/skoir/castles/doc … | The page locators for the review's most load-bearing quotations are wrong in 3 of 5 spot-checks against the published texts, and the errors propagate into the consumer agenda. §9.5 exists precisely so a successor auditor can 're-open the quoted page', so wrong … | Retrieved Cowles Foundation Papers 1349/1498 (journal pagination in the running heads) and located each item: PWY Table 3 Panel A (ADF1 size 0.049 at g=0.00) is on IER p.219, review says 'Table 3 Pane … | Correct the four locators to p.207, p.214, p.219 and p.1053 in §7.1, §7.4, §7.6, §8.2, §8.3 and the §9.5 table, propagate the p.1053 correction to agenda lines 110 and 499, and record in §9.5 that the … | Phillips, Wu & Yu 2011 IER 52(1):201-226, doi:10.1111/j.1468-2354.2010.00625.x (Cowles Paper 1349, korora.econ.yale.edu/phillips/pubs/art/p1 … | quant-auditor | retained — remediate |
| QUANT-2-4 | major | reproducibility | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2148-2175 (§9.5), 2560-2575 (L-16), 2616 (VG-10) | The remediation of QUANT-1-7 rests on an un-refetchability claim that does not hold. §9.5 marks all three Phillips texts 'FAILED — host korora.econ.yale.edu did not accept a connection' with digest 'none', and L-16/VG-10 assert the four texts 'cannot presently … | HTTP 200 application/pdf from http://korora.econ.yale.edu/phillips/pubs/art/p{1349,1498,1499}.pdf: p1349.pdf 258,681 B sha256 a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4 (page 1: … | Re-fetch the three reprints, record their SHA-256 digests in the §9.5 table, mark the quote/page re-verification as performed, and narrow L-16/VG-10 to eru-1289 (Cowles DP 2331) alone; state that the … | project reproducibility contract (CLAUDE.md §Reproducibility contract); §9.5 as delivered | quant-auditor | retained — remediate |
| QUANT-2-5 | major | reporting | C:/Users/skoir/castles/docs/research_notes/research_agenda_regime-classification_2026-08-21.md:743-772 (Verification status, Residual) | The consumer agenda's residual paragraph is stale against the review it now cites and under-discloses in three ways the review explicitly asks it to carry. (a) It states the backward-chase arm 'never executed' and that pre-2011 antecedent coverage rests on the … | Agenda line 752: 'The protocol\'s backward citation-chasing arm (er-bc-*, protocol §3.3) never executed'; line 769: 'Amendments A4, A5 and A6 are post-hoc and labelled as such.' Review §14 item 3 (lin … | Rewrite the residual bullets: state that the er-bc-* arm ran post-freeze under A11 through publisher-deposited reference lists over 22 of 27 carriers and named two unadmitted candidates (er-bc-1 Hall/ … | review §14 items 2-3, amendments A9 and A11; PRISMA 2020 item 24c (protocol deviations) | quant-auditor | retained — remediate |
| QUANT-2-6 | major | reporting | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2448-2515 (L-13, especially (e)) | L-13 is the fix for 'a partial metadata check reported as a complete one', and it reintroduces the same defect on the year field. It claims a check 'field by field on container title, volume, issue, page range and year' over 62 of 62 records, then discloses on … | Live Crossref pull for all 62 DOI-bearing records: 19 with online-year != print-year (eru-0150, 0238, 0348, 0559, 0597, 0689, 0748, 0891, 1044, 1112, 1117, 1260, 1384, 1509, 1580, 1604, 1715, 1845, 06 … | Either enumerate all 19 online/print year divergences under the CONVENTION and reconcile the 22 label-vs-store year mismatches, or narrow L-13's completeness claim to the fields actually reconciled (c … | api.crossref.org/works/{doi} retrieved 2026-09-02; PRISMA 2020 item 27 / L-13's own completeness assertion | quant-auditor | retained — remediate |
| LITERATURE-2-1 | major | misattributed-source / false recall claim | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:148-149 (abstract), :278-283 (§2.2), :294-295, :2367-2378 (L-5), :2610 (VG-4); docs/m … | The A11 backward-chase diagnostic reports `er-bc-2` (Banerjee, Chevillon & Kratz 2013, SSRN 2322360) as one of two "candidate additions" absent from the 1,996-record universe and "a record the frozen corpus does not contain", with eligibility "indeterminate at … | (1) references_explosive-regime-dating.json:4436-4452 carries `eru-0209`, "Detecting and Forecasting Large Deviations and Bubbles WITH a Near-Explosive Random Coefficient Model", 2013 — the same 2013 … | Correct §2.2, L-5, VG-4, the abstract and protocol amendment A11 to state that er-bc-2's work was already in the universe as `eru-0209`/`eru-1027`, was screened at both stages, and was excluded S-c-fa … | https://doi.org/10.1093/ectj/utaa004 ; https://doi.org/10.2139/ssrn.2322360 ; docs/literature/search_logs/explosive-regime/screen2-verdicts- … | literature-check | retained — remediate |
| LITERATURE-2-2 | major | unverifiable-claim contradicted by primary source | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2151 (§9.5 row for eru-1289), :2560-2569 (L-16), :2616 (VG-10) | §9.5 (new, created by the QUANT-1-7 remediation) records the re-fetch of Cowles DP 2331 as "FAILED — cowles.yale.edu and elischolar.library.yale.edu returned HTML", and L-16/VG-10 conclude that §7.4's FWER triple "rest[s] on single-session transcription that c … | Fetched this round: https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf returned a 578 KB application/pdf (saved to the session tool-results directory). The Cowles listing and EliScholar m … | Re-fetch d2331_0.pdf at the direct file path, record its SHA-256 in the §9.5 table, mark the row OK, and downgrade VG-10/L-16 so they no longer assert that the FWER triple cannot be re-opened. If the … | https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf | literature-check | retained — remediate |
| LITERATURE-2-4 | major | incomplete check reported as complete | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2449-2458 (L-13 preamble), :2500-2508 (L-13(e)), :2620-2626 (§12.3 summary) | L-13 (the LITERATURE-1-4 remediation) asserts a complete 62/62 Crossref comparison "field by field on container title, volume, issue, page range AND YEAR", and closes the year dimension with a CONVENTION covering exactly seven records. Spot-verification defeat … | (1) `eru-1117`: L-13(e) states of all seven that "Crossref's published-print year is one later". Crossref 10.1093/jjfinec/nbab009 gives published-online [2021,5,5] and published-print [2023,1,19] — tw … | Either enumerate every year divergence in both directions across the 62 records, or restate L-13's scope as "container title, volume, issue and page range, plus the seven online-first/print year diver … | https://api.crossref.org/works/10.1093/jjfinec/nbab009 ; https://api.crossref.org/works/10.1111/jtsa.12768 ; https://api.crossref.org/works/ … | literature-check | retained — remediate |
| LITERATURE-2-5 | major | tool/method attribution contradicted within the artifact | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:362-368 (§2.5 "Honest compliance statement, as executed") | The QUANT-1-3 remediation reconciled the automation-tool identity per stage in the frontmatter, L-15, VG-11 and the §15 AI-assistance statement, and states the conflict is UNRESOLVABLE from the logs. §2.5 — the PRISMA 2020 item-8 compliance statement itself, i … | §2.5:363-364 reads: "Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5)." Against this: frontmatter `ai_assistance` (:41-51) declares … | Replace §2.5's parenthetical with the per-stage trailer declaration and a pointer to L-15/VG-11, so PRISMA item 8 is discharged on the same record as the rest of the document. | PRISMA 2020 item 8 (Page et al. 2021, doi:10.1136/bmj.n71) | literature-check | retained — remediate |
| LITERATURE-2-6 | major | claim attributed to the frozen protocol that the protocol does not make | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2020-2032 (§9.3, "Why this label and not `indeterminate-from-full-text`") | The REV-1-6 remediation's justification for keeping the definite `episode-statistic-null` token turns on a definition it attributes to the frozen protocol: "The protocol's verdict vocabulary contains `indeterminate-from-full-text` for the case where a full tex … | protocol_explosive-regime-review_2026-08-24.md:598-603 verbatim: "`assignment-null` — the stated null attaches to the state-assignment decision at time t (…); `episode-statistic-null` — the null gover … | Label the `indeterminate-from-full-text` gloss explicitly as a CONVENTION of this document (or append it as a numbered amendment), and state that the frozen protocol decides neither the version-mismat … | docs/methodology/protocol_explosive-regime-review_2026-08-24.md §9.1 lines 598-603, 650-662 | literature-check | retained — remediate |
| LITERATURE-2-7 | major | consumer document contradicts the source it transcribes; required disclosure omitted | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:751-755, :769 | The Rev 4 residual paragraph — explicitly rewritten 2026-09-02 "after the Thread A audit round" — still states that the backward citation-chasing arm "never executed", which the SCOPE-1-4 remediation superseded on the same date, and carries no mention of er-bc … | Agenda:751-755 "The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed…" versus review §2.2:255-289 and A11 (protocol:969-1016), which record the arm as executed 2026-0 … | Rewrite the antecedent-layer bullet: the arm ran post-freeze under A11 through publisher-deposited reference lists over 22 of 27 carriers; it named Hall, Psaradakis & Sola (1999) as a probable eligibl … | https://doi.org/10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X | literature-check | retained — remediate |
| LITERATURE-2-8 | major | required transcription omitted from consumer | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:730-735, :133-147, :513-521 | Review §14 item 3 instructs the consumer, in terms, to "Record also … the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)". Rev 4 records the three NB verdicts and NB-13's provisional status at three sites bu … | Review §14:3005-3006 (the instruction); review §9.0:1873-1898, L-17:2571-2578, VG-9:2615 (the defect). Agenda:730-735 discharges the NB caveats and carries only the NB-13 version caveat; agenda:513-52 … | Add to the NB bullet: all three adjudications rest on §9's full-text reading alone; protocol §9.1 required the three to be force-screened into the record universe and they never entered it, so no crit … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §14 item 3, §9.0, L-17, VG-9 | literature-check | retained — remediate |
| REPRODUCIBILITY-2-1 | major | deps_pinned | C:\Users\skoir\castles\pyproject.toml:10-40; repo root uv.lock (untracked) | No clone-durable environment specification exists for the runs that produced and remediated this review. pyproject declares every dependency unpinned (ruff, pytest, pandas, numpy, scipy, pandera, matplotlib ...) with no `==` and no version floors, and the only … | pyproject.toml dev/data/viz extras contain no version specifier except `jsonschema>=4.18`; `git ls-files uv.lock` empty; .gitignore lines 49/56 exclude artifacts/ and logs/ with only .gitkeep exceptio … | Commit uv.lock (it is already generated), and state in the review's §15 provenance row that the environment is fixed by uv.lock at the delivering commit rather than by the gitignored pip-freeze archiv … | — | reproducibility-verifier | retained — remediate |
| REPRODUCIBILITY-2-2 | major | deps_pinned | C:\Users\skoir\castles\logs\reproducibility\repro_log_f5419aa650e249378ff40828424696bb.json; review §15 row 'earlier-stage ReproLog' | The ReproLog for the stage that PRODUCED the frozen corpus (search, screening, extraction; commit 8aeebfe) has a vacuous environment and data record, and §15 cites it as an environment record while disclosing only its missing model field. Its pip_freeze_sha256 … | repro_log_f5419aa6...json: {"config_resolved_sha256": null, "dataset_checksums": {}, "pip_freeze_sha256": "e3b0c442...b855"}; `ls -la logs/reproducibility/env/` shows e3b0c442...txt at 0 bytes; review … | Add one sentence to the §15 earlier-stage ReproLog row and to VG-11: the 8aeebfe ReproLog carries an empty pip-freeze (digest = SHA-256 of the empty string), a null config digest and no dataset checks … | — | reproducibility-verifier | retained — remediate |
| REPRODUCIBILITY-2-3 | major | llm_provenance | C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md §15 (AI-assistance statement, 'what κ then measures'); logs\re … | The round-1 remediation of QUANT-1-3 is honest about model IDENTITY but silently leaves model CONFIGURATION unrecorded, and then leans on it. §15 now asserts κ = 0.433 'measures decoding-and-context variance of the screening model'. No temperature, top_p, max_ … | grep -ril 'temperature\|top_p\|top-p' over docs/literature/search_logs/explosive-regime/ matches only records whose abstracts discuss physical temperature (se-crossref-07.json: 'temperature of long-li … | Either (a) record the decoding configuration of the screening sessions if it is recoverable from the dispatch record and add it to er-screening-prompt.txt's archival note, or (b) weaken the §15 senten … | — | reproducibility-verifier | retained — remediate |
| REPRODUCIBILITY-2-4 | major | data_hashed | C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md §12.1 L-13 (lines ~2449-2490), §15 'identifier verification' r … | The LITERATURE-1-4 remediation replaced a partial check with a complete one but archived no evidence for it. The 62/62 Crossref cross-check, the 62/62 DOI Handle re-resolution, the 2 arXiv and 1 Handle resolutions, and the §9.5 retrieval attempts produced NO m … | `ls docs/literature/search_logs/explosive-regime/` (81 files) contains se-bc-01.json but no crossref-recheck or doicheck-2026-09-02 artifact; protocol-doicheck.json is the 2026-08-24 protocol-time fil … | Write the per-DOI check results (DOI, queried date, retrieved container-title/volume/issue/page/issued, verdict) to a tracked log, e.g. docs/literature/search_logs/explosive-regime/se-crossref-recheck … | — | reproducibility-verifier | retained — remediate |
| REPRODUCIBILITY-2-5 | major | entrypoint_runs | C:\Users\skoir\castles\tests\ (empty), src\ (empty), CLAUDE.md Quickstart | No entrypoint re-derives any reported number. The Quickstart advertises `uv venv && uv sync; uv run pytest`, but tests/ and src/ contain no files (git ls-files returns nothing under either) and .venv/Lib/site-packages holds 3 entries, i.e. the project venv was … | `ls -d tests src` shows both exist and are empty; `git ls-files data` returns only data/metadata/.gitkeep; logs/reproducibility/env/51760dc9....txt line 4 is `alpaca-py==0.43.2`, a package in no pypro … | Commit the recount as a test or script under tests/ or src/ (e.g. tests/test_erob_recount.py) that reads se-extraction-primary.jsonl + se-extraction-recheck.jsonl and the §6 table and asserts the publ … | — | reproducibility-verifier | retained — remediate |
| REV-2-8 | minor | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:128-130, 1902-1906 | The abstract's remediated NB sentence asserts that NB-02 was adjudicated "on the full text of the version at issue", but §9.1 records the adjudicated text as arXiv:cond-mat/0010050v2, the preprint twin of the Journal of Risk article the DOI identifies. The ext … | (7) NB-02, NB-08 and NB-13 are all adjudicated **episode-statistic-null** — NB-02 and NB-08 on the full text of the version at issue, **NB-13 provisionally, on the 2006 working-paper twin, the 2009 jo … | Reword the abstract to "NB-08 on the published article, NB-02 on the arXiv v2 preprint the protocol names as the target version, NB-13 provisionally on the 2006 working-paper twin", and add one senten … | CHAMP item 19 (internal consistency of the abstract with the results); round-1 finding REV-1-6 | critical-reviewer | deferred — logged minor |
| REV-2-9 | minor | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3093-3095 | The new §16 change note misstates the round-1 audit's own configuration: it says "seven-branch" and then names four branches in the immediately following parenthesis, which matches the recorded round-1 routing (four branches, 33 agents). A provenance section t … | A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check) with an adversarial refute gate raised 27 major findings against this review; 3 were refuted and dro … | Change "seven-branch" to "four-branch" (or state "four specialist branches, 33 agents" if the agent count is what was intended). Confirm the 27 / 3 / 24 / 20+4 arithmetic against the round-1 dispositi … | CHAMP item 19; PRISMA 2020 item 24c (amendments and their provenance) | critical-reviewer | deferred — logged minor |
| REV-2-10 | minor | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:128-149 | The REV-1-6 propagation into Definitional basis (d) leads with a bolded, unqualified universal — all three candidates "adjudicated on full text" — and qualifies NB-13 only four lines later; a reader lifting the bolded sentence gets the unqualified form the fin … | **Rev 4: the three unadjudicated candidates are now adjudicated on full text and none of them carries one** — drawdown/drawup episodes NB-02 … **Two of the three are adjudicated on full text; NB-13 is … | Qualify the lead sentence in place ("…are now adjudicated at full-text depth — two definitively, NB-13 provisionally on a working-paper twin — and none of them carries one") and delete the duplicated … | CHAMP items 19, 29; round-1 finding REV-1-6 | critical-reviewer | deferred — logged minor |
| REV-2-11 | minor | interpretation | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:531-536, 550-574 | Originality note. The Rev 4 remediation adds a branch-3 bullet presenting "admission of the surveillance/monitoring line" as a new consequence of the review, but the same branch already carries a Rev 2 bullet establishing the Frisén financial-surveillance scho … | **Rev 4, admission of the surveillance/monitoring line (audit REV-1-7, QUANT-1-6; review §14 item 2).** That line *does* publish a false-alarm rate over a stated horizon in closed form, which is the q … | Cross-reference the Rev 2 bullet from the Rev 4 bullet and state precisely what Rev 4 adds — nine named in-corpus bubble-monitoring records with closed-form FPR, as against Rev 2's location of the gen … | RQI dimension 2 (originality); CHAMP item 28 | critical-reviewer | deferred — logged minor |
| SCOPE-2-5 | minor | untraceable | C:\Users\skoir\castles\docs\deliverables\deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:17-38 | Thread A items 1 and 2 are ticked `[x]` but their `check:` lines are left as the original prospective check text, with no recorded check output. Every other ticked item in the same spec (Thread B items, Thread C ADR, protocol, registration commit, search logs) … | Spec l.27-30: '- check: flow numbers reconcile against `se-included-set.json` and `se-kappa-computation.json`; appraisal row count equals 72; both Phillips full-text sections present; three NB verdict … | Record the executed check output under Thread A items 1 and 2 in the same form as Threads B and C — appraisal row count, the reconciliation result including the A9 exception, the Phillips section anch … | ISO/IEC/IEEE 29148:2018 verifiability/traceability; spec item Thread A checks | scope-auditor | deferred — logged minor |
| SCOPE-2-6 | minor | changed | C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:3093-3095 | The change note describes the round-1 audit as 'A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check)', naming four branches while asserting seven. Seven is the loop's configured branch count, not the number routed … | §16 l.3093-3095: 'A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check) with an adversarial refute gate raised 27 major findings against this review'. Spe … | Reword to 'a seven-branch specialist loop of which four branches routed (critical-reviewer, scope-auditor, quant-auditor, literature-check)'. | deliverable spec Delegation, round-1 disposition record | scope-auditor | deferred — logged minor |
| QUANT-2-7 | minor | reporting | C:/Users/skoir/castles/docs/research_notes/research_agenda_regime-classification_2026-08-21.md:764-766 | The agenda describes the store as 'five carrying the I3 GAP note plus the twins eru-0154 and eru-0904'. That describes the pre-remediation store: all seven entries now carry an I3 GAP note, and the two twin notes additionally carry the twin-does-not-inherit ru … | references_explosive-regime.json contains exactly 7 occurrences of 'I3 GAP', on eru-0100, eru-0112, eru-0154, eru-0268, eru-0427, eru-0904, eru-1310; the eru-0154 and eru-0904 notes read 'A twin does … | Replace 'five carrying the I3 GAP note plus the twins' with 'all seven carrying an I3 GAP note in the included-corpus store, the two twin entries additionally recording that a twin does not inherit it … | docs/literature/references_explosive-regime.json (sha256 8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124) | quant-auditor | deferred — logged minor |
| QUANT-2-8 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3092-3096 (§16 change note) | The change note misstates the audit it is responding to: 'A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check)' names four branches in its own parenthetical, and the round-1 record is four branches / 33 agents. Th … | §16 line 3093 as quoted; round-1 disposition record: '4 branches routed (critical-reviewer, scope-auditor, quant-auditor, literature-check), 33 agents'. | Change 'seven-branch' to 'four-branch (33 agents)'. | round-1 audit disposition record | quant-auditor | deferred — logged minor |
| QUANT-2-9 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1296-1300 (§7.2 coverage) | The §7.2 coverage sentence does not exhaust its own denominator: 'reported in 15 of 65 (23%), partially in 8, and not at all in 41' accounts for 64 of 65 assessable records, silently dropping the one Q4 'unclear' cell. §7.3 and §7.4 enumerate all four response … | Recount of the §6 table Q4 column: yes 15, partial 8, unclear 1, no 41 (total 65). §7.4 by contrast writes 'addressed in 19 of 65 ... partially in 1, unclear in 6, not addressed in 39' (= 65). | Add 'unclear in 1' to the §7.2 sentence so the four levels sum to the assessable denominator. | review §6 appraisal table; PRISMA 2020 item 20b | quant-auditor | deferred — logged minor |
| LITERATURE-2-3 | minor | overstated verification gap | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2146-2151 (§9.5 rows for eru-0131/0393/0395), :2560-2569 (L-16), :2616 (VG-10) | §9.5 records only three hosts (korora.econ.yale.edu, cowles.yale.edu, elischolar) for the three Phillips texts and then concludes the §8.3 verdict "cannot presently be re-opened". Independently accessible full texts of the same work exist and were not attempte … | korora.econ.yale.edu confirmed dead (ECONNREFUSED). But HKIMR Working Paper No. 22/2007 of PWY 2011 was retrieved this round from https://www.aof.org.hk/uploads/publication/175/ub_full_0_2_164_hkimr-n … | Reword §9.5/L-16/VG-10 to the checkable claim: "the specific Cowles reprint file that was transcribed is unre-fetchable and no extraction-time digest exists; other versions of the same works are acces … | https://doi.org/10.1111/j.1468-2354.2010.00625.x ; https://www.aof.org.hk/uploads/publication/175/ub_full_0_2_164_hkimr-no22_bw.pdf | literature-check | deferred — logged minor |
| LITERATURE-2-9 | minor | stale figure after remediation | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:763-766 | The agenda states seven I3 failures as "five carrying the I3 GAP note plus the twins `eru-0154` and `eru-0904`". The REV-1-2 remediation added `I3 GAP` notes to the two twins as well, so all seven now carry the note; the agenda describes the pre-remediation st … | references_explosive-regime.json carries seven `I3 GAP` notes (lines 1582, 1603, 1624, 1645, 1667, 1910, 2042), the two twin entries (1624, 1910) explicitly stating "A twin does not inherit its carrie … | Reword to "seven included records fail I3 as written and all seven now carry an `I3 GAP` note in the store, including the twins `eru-0154` and `eru-0904`, for which a carrier's DOI is not the twin's i … | docs/literature/references_explosive-regime.json | literature-check | deferred — logged minor |
| LITERATURE-2-10 | minor | unresolvable citations / inconsistent claim about the corpus table | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:735-808 (§5 corpus table), :2453-2456 (L-13) | L-13 says the Crossref check compared "the extraction stage's E1 citation string (which §5 reproduces verbatim)". §5 does not reproduce E1 verbatim — it truncates the citation column mid-string, cutting DOIs, so the table's own identifiers do not resolve. §5.2 … | §5 row 1 ends "…International Economic Review 52(1):201-226. doi:10.1111..."; row 2 "…doi:10.10..."; row 27 (`eru-1117`) is cut at "…Time-Varying Volatility. Jour..." so neither its volume/issue/pages … | Either restore the full E1 strings in §5 (the machine-readable store is already the fallback), or correct L-13's and §5.2's wording to state that §5 shows a truncated citation column and that the full … | docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl | literature-check | deferred — logged minor |
| REPRODUCIBILITY-2-6 | minor | cross_platform | C:\Users\skoir\castles\docs\literature\search_logs\explosive-regime\er-screening-prompt.txt:11,77 | The archived, frozen screening instrument hardcodes a machine-specific absolute Windows path: 'the registered systematic review at C:/Users/skoir/castles (working directory)' (both the stage-1 and stage-2 prompts). Re-running the screening instrument on any ot … | grep -n 'C:/Users' er-screening-prompt.txt → lines 11 and 77. | Do not edit the frozen prompt text. Add one line to the file's existing archival note stating that `C:/Users/skoir/castles` is the execution-time working directory and that a re-execution substitutes … | — | reproducibility-verifier | deferred — logged minor |
| REPRODUCIBILITY-2-7 | minor | data_hashed | C:\Users\skoir\castles\docs\literature\search_logs\explosive-regime\se-bc-01.json (all_referenced_dois_not_in_universe entries sourced from Crossref u … | The new backward-chase log stores lossily transcoded reference strings: U+FFFD replacement characters appear where the source had typographic quotes, e.g. the eru-1509 entry reads 'Blackburn, K., and M. Sola. 1996. �Market Fundamentals versus Speculative Bubbl … | json.load of se-bc-01.json with encoding='utf-8' yields '�' inside carrier reference titles; universe check: 1996 records loaded, both candidate DOIs and normalised titles absent. | Note in se-bc-01.json (a `notes` entry) that unstructured Crossref reference strings were stored after a lossy transcode and that the title-normalisation match is therefore approximate for those entri … | — | reproducibility-verifier | deferred — logged minor |
| REPRODUCIBILITY-2-8 | minor | data_hashed | C:\Users\skoir\castles\data\_manifest.json (absent); CLAUDE.md §Reproducibility contract | The project contract names data/_manifest.json as the dataset-provenance carrier with a CI `--check` drift mode; the file does not exist. The review's four datasets — the 1,996-record candidate store, the 72-record included store, the 81 files under search_log … | `cat data/_manifest.json` → No such file; §15 gives SHA-256 for references_explosive-regime.json and the protocol only; sidecar artifact_digests lists 3 files, none of which is the candidate store, an … | Add the candidate store's SHA-256 to §15's provenance table (and to the sidecar's artifact_digests) alongside the included-corpus digest, and either build data/_manifest.json over these paths or recor … | — | reproducibility-verifier | deferred — logged minor |

Convergent clusters, so remediation can address each defect once:

- **The O6 denominator** — REV-2-2, SCOPE-2-4 and QUANT-2-2 (three branches, one
  defect): the same quantity (RT = 22) is stated over 72 in the abstract and over
  65 in §7.6, the excluded classes are unnamed at the abstract site, and "fewer
  than one in three" is arithmetically false at every denominator the document's
  own definitions support except 72.
- **The `partial`-cell denominator 585** — REV-2-12 and QUANT-2-1: 65 × 9 counts
  24 `n/a` cells as answered; the correct figure is 65 × 7 + 53 × 2 = 561, and the
  wrong one is embedded in append-only amendment A7.
- **The §2.5 model-identity residue** — REV-2-1 and LITERATURE-2-5: the PRISMA
  item-8 site still names `claude-opus-5` as the screening base model after the
  QUANT-1-3 remediation declared the identity unresolvable and the trailers
  declare `claude-fable-5`.
- **The consumer agenda lagging the review** — SCOPE-2-1, SCOPE-2-2, QUANT-2-5,
  LITERATURE-2-7, LITERATURE-2-8 and REV-2-7 (four branches): "never executed"
  for the backward-chase arm, the two named unadmitted candidates absent, the
  A4–A6 post-hoc roll-up stale against A4–A11, the A9/VG-9 disclosure the review
  explicitly instructs absent, and the O4 claim carried unscoped.
- **The §9.5 un-refetchability claim** — QUANT-2-4, LITERATURE-2-2 and (minor)
  LITERATURE-2-3: all four "cannot presently be re-opened" texts were re-fetched
  and re-collated this round, three from the exact URL §9.5 records over HTTP and
  the fourth from the direct `cowles.yale.edu` file path.
- **L-13's completeness on the year field** — QUANT-2-6 and LITERATURE-2-4: a
  check declared complete over `container title, volume, issue, page range and
  year` discloses 7 of 19 online/print year divergences and misstates the class
  ("one later") for `eru-1117`.
- **The stale seven-branch change note** — REV-2-9, SCOPE-2-6 and QUANT-2-8
  (minors): §16 says "seven-branch" and names four.
- **The stale I3-store description in the agenda** — QUANT-2-7 and
  LITERATURE-2-9 (minors).

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; a drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Thirty dispositions,
one per major finding: **0 dropped** and **30 retained** after failed refutation
attempts (`refuted: []`, `counts.refuted: 0`). There are no retained-conservative
entries this round (`retained_conservative: 0`), so no entry is retained on
uncertainty rather than on a failed refutation. No entry carries
`reproduction_required: true` — every refutation attempt was resolved by direct
re-reading, live retrieval or independent recomputation reported inside the
refutation evidence itself — so **no `reproduction: {command, observed}` block is
owed on any entry**; where a refuter ran a command, the command and its observed
result are stated verbatim inside the refutation evidence quoted below. Claims
are reproduced verbatim and unabridged, as is each refutation's evidence.

`evidence_type` is enumerated per entry. All thirty are `none`: in every case the
refuter searched for counter-evidence of the permitted types (`source-quote`,
`reproduced-check`, `counter-test`, `logical-proof`) and obtained none, so the
gate could not drop the finding. Several refutation attempts strengthened the
finding instead (QUANT-2-3, QUANT-2-4, LITERATURE-2-1, LITERATURE-2-2,
REV-2-12, SCOPE-2-4), and those additions are recorded in the evidence text.

### REV-2-1 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:364
> **issue:** The QUANT-1-3 remediation reconciled the automation-tool identity per stage in the frontmatter, L-15, VG-11 and the §15 AI-assistance statement (screening declared `claude-fable-5`), but §2.5's "Honest compliance statement, as executed" was not updated and still names `claude-opus-5` as the screening base model. The document therefore contradicts itself on the single fact the remediation exists to state honestly, and §2.5 is the site a PRISMA item-8 reader reaches first.
> **evidence:** **Honest compliance statement, as executed.** Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5).
> **fix:** Replace `(claude-opus-5)` at §2.5 with the per-stage declaration (`claude-fable-5` per the `8aeebfe` trailer, with the conflict pointer to L-15/VG-11), or drop the model name and cross-reference §15. Grep the artifact for every remaining bare model name and confirm each matches the per-stage table.
> **reference:** PRISMA 2020 item 8; CHAMP item 19 (reporting consistency); round-1 finding QUANT-1-3

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No counter-evidence found; the defect reproduces exactly as stated. At docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:362-369 (inside §2.5 "Selection process (item 8)", which runs from the header at L344 to the §2.6 header at L371) the text reads verbatim: "**Honest compliance statement, as executed.** Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5)." The name appears bare, in the present tense, describing execution — not flagged as the superseded "as first delivered" declaration, and with no pointer to L-15, VG-11 or §15.
>
> Every other site the QUANT-1-3 remediation touched declares the screening stage as claude-fable-5: frontmatter ai_assistance L38-44 ("stage-1 and stage-2 screening, both blind adjudications ... (commit 8aeebfe): claude-fable-5"); L-15 prose at L2315-2317 ("declared by the commit that carries their verdict files as `claude-fable-5`"); the L-15 per-stage table row at L2530 ("stage-1 and stage-2 screening, both blind adjudications | ... | `8aeebfe` | `claude-fable-5 (role=multi)`"); VG-11 at L2617; and the §15 AI-assistance table row at L3071-3072 (`claude-fable-5`). L2521 and L3060 both explicitly characterise `claude-opus-5`-for-every-stage as the superseded original declaration.
>
> A full grep of the artifact for `opus-5`/`fable-5` (hits at L41, L44, L48, L364, L2317, L2521, L2528-2533, L2617, L3060, L3069-3076) confirms L364 is the only remaining occurrence of `claude-opus-5` attached to a screening/adjudication stage; every other `claude-opus-5` hit is correctly scoped to synthesis, write-up, or round-1 remediation, or is explicitly labelled as the superseded declaration. The contradiction is therefore real, is internal to a single document, and sits at the PRISMA item-8 selection-process section.

### REV-2-2 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:113-116, 1608-1609
> **issue:** The REV-1-4 assessable-denominator remediation was applied inconsistently to O6. The abstract defends 72 as "the right denominator" for three counts that sum to 63, not 72 (the remaining 9 records are SPLIT 3, NS 2, NE 4), while §7.6 uses 65 and asserts "fewer than one in three" — which is arithmetically false: 22/65 = 33.85%, above one in three. The same quantity is therefore given two denominators, one of which yields a false quantitative statement.
> **evidence:** (2) 22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the record set, so 72 is the right denominator here). … **Synthesis claim (O6).** Of the 65 records with an extracted causality status, fewer than one in three publishes a characteristic measured on a genuinely real-time procedure
> **fix:** Fix one denominator for O6 and use it at both sites. If 65 (assessable, excluding 4 NE and 3 twins) is chosen, state 22 of 65 (34%) and delete "fewer than one in three"; also note that 2 of those 65 are NS, so the base for "extracted causality status" is 63, not 65. If 72 is retained, list all six code counts so the partition is visible and drop the abstract's "fewer than one in three" analogue.
> **reference:** CHAMP items 17, 19; SAMPL §Basic statistical reporting (denominators and numerators for every proportion); round-1 finding REV-1-4

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; the finding reproduces exactly. (1) Independent recount of the §5 study-characteristics table (rows 737-808 of docs/literature/lit_review_explosive-regime-dating_2026-08-24.md, O6 column parsed programmatically) yields RT 22, FS 22, CS 19, SPLIT 3, NS 2, NE 4 = 72, matching the §4 tally at line 694 and the §7.6 code table at lines 1580-1587. The finding's characterization of the residual 9 (SPLIT 3, NS 2, NE 4) is correct. (2) Abstract, lines 113-116, verbatim: "22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the record set, so 72 is the right denominator here)" — the three listed counts sum to 63; the parenthetical asserts a partition without exhibiting the remaining three codes, so 72 cannot be verified from the abstract. (3) §7.6, lines 1608-1609, verbatim: "Of the 65 records with an extracted causality status, fewer than one in three publishes a characteristic measured on a genuinely real-time procedure". The numerator is unambiguously RT = 22, fixed two paragraphs above by the §7.6 table row "**RT** | 22 | the reported characteristic is measured on a genuinely real-time procedure". 22/65 = 33.85% > 33.33%, so "fewer than one in three" is arithmetically false on the stated denominator. It is false on every base consistent with the document's own definitions: 22/63 = 34.9% (65 minus 2 NS, the actual base for "extracted causality status"), 22/65 = 33.85%, 22/66 = 33.33% (exactly one in three, not fewer). It holds only on 68 or 72, neither of which the sentence states. (4) Checked whether the 22 RT records could shrink inside the 65 assessable set: the 3 twins are eru-0154 (CS), eru-0622 (FS), eru-0904 (CS) and the 4 NE are eru-0112, eru-0749, eru-1310, eru-1890 — none is RT, so RT remains 22 within the 65. (5) Same-quantity/two-denominator claim confirmed: RT = 22 is reported over 72 in the abstract and over 65 in §7.6. (6) grep across docs/ found no errata, amendment, or later correction touching either site; the round-1 trail docs/audits/audit_trail_phase2-explosive-review_2026-08-24.json already logged the identical arithmetic (lines 516-517, 616-617) and the sentence still stands unmodified, so the defect is live, not stale.

### REV-2-3 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:899-900, 691-697, 1579-1586, 2228-2230
> **issue:** §5.3, L-7 and amendment A10(b) all assure the reader that the three same-work twins cause no double-counting, and §6.1 excludes them from every assessable denominator. But the record-level distributions in §4 (O6, evidence tier, authorship lineage, extraction depth), §7.6 and §10.2 count all 72 records, so `eru-0154` (CS), `eru-0904` (CS) and `eru-0622` (FS) are each counted a second time under codes inherited from their carriers. On distinct works the O6 split is RT 22 / FS 21 / CS 17, not 22/22/19, and the PSY-lineage count is 19, not 21. The assurance as written is false for these tables.
> **evidence:** Each twin is extracted once, under its carrier, so no operating characteristic is double-counted in the synthesis. … Authorship lineage across the 72 records: **21** carry a PSY-lineage author (Phillips, Shi, Yu, Wu); **16** carry a Harvey–Leybourne–Taylor–Astill-line author; **35** are neither.
> **fix:** Narrow the §5.3/L-7/A10(b) assurance to "no operating characteristic in the §7 evidence tables is double-counted" and add the distinct-work counts alongside the record counts in §4, §7.6 and §10.2 (O6: RT 22 / FS 21 / CS 17 / SPLIT 3 / NS 2 / NE 4 over 69; lineage 19/16/34), consistent with §6.1's own twin rule.
> **reference:** CHAMP items 17, 19; PRISMA 2020 item 17; round-1 finding SCOPE-1-5

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; the finding reproduces exactly. (1) The assurance exists verbatim at L899-900 (§5.3), L2398-2399 (L-7: "so no operating characteristic is double-counted"), with L-7 further claiming the twins "are excluded from every assessable denominator in §6.1 and §7", and A10(b) at L2700. (2) §5.1 rows assign the twins O6 codes identical to their carriers: eru-0154 CS (L780) vs carrier eru-0126 CS (L799); eru-0904 CS (L790) vs carrier eru-1526 CS (L767); eru-0622 FS (L785) vs carrier eru-0675 FS (L786). (3) The §4 dimension table (L~697) and §7.6 (L1579-1586) both report RT 22 / CS 19 / FS 22 / SPLIT 3 / NS 2 / NE 4, summing to 72, with no work-level column; deleting the three twins gives RT 22 / CS 17 / FS 21 / SPLIT 3 / NS 2 / NE 4 = 69, matching the finding's 22/21/17. (4) §10.2 (L2228-2230) reports lineage 21 PSY / 16 HLTA / 35 other over 72; eru-0154 (Phillips, Yu) and eru-0904 (Lui with Phillips, Yu) are PSY-lineage, eru-0622 (Pavlidis, Martinez-Garcia, Grossman) is "neither", so distinct-work lineage is 19/16/34, again matching. (5) Counter-test for an already-present dual count: grep for "distinct" over the whole file returns only L31, 94-95, 151, 511, 896, 954, 2400, 3115 (frontmatter, abstract, flow diagram, §5.3, §5.1 header, L-7, ledger) — no distinct-work figure appears anywhere in §4, §7.6 or §10.2, so §5.3's own promise that a materially differing count over works "is given both ways" is unmet at these sites. (6) §6.1 (L1157-1197) does exclude the twins (assessable n = 65 = 72 - 4 NE - 3 twins; D7 denominator 53 with the text "and 3 are twins"), confirming the internal inconsistency the finding alleges, and showing L-7's "and §7" clause is false of §7.6. Only defect in the finding is a wording imprecision that does not affect the claim: of the four §4 dimensions named, extraction depth gives twins their own category ("twin extracted under its carrier 3") and evidence tier codes them working-paper against peer-reviewed carriers, so those two are not "codes inherited from their carriers" — they still count the same work twice at record level. Claim stands.

### REV-2-4 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** design
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2018, 2029-2032; docs/methodology/protocol_explosive-regime-review_2026-08-24.md:598-603, 822-1017
> **issue:** The REV-1-6 remediation ships NB-13's verdict as `episode-statistic-null` carrying a new scope qualifier, "PROVISIONAL ON THE WORKING-PAPER TWIN", which the frozen §9.1 verdict vocabulary (assignment-null / episode-statistic-null / mixed / indeterminate-from-full-text) does not define. No numbered amendment records the extension. This is the same class of deviation as A7 — a qualifier the frozen instrument is silent about — and the review itself set the precedent that such an extension must be recorded as an amendment with a labelled CONVENTION. A8–A11 were appended for lesser departures; this one was not. The reasoning for preferring the qualified label over `indeterminate-from-full-text` is sound and disclosed, but the protocol-fidelity bookkeeping the review applies everywhere else was skipped here.
> **evidence:** **Verdict: `episode-statistic-null` — PROVISIONAL ON THE WORKING-PAPER TWIN.** … The verdict token therefore stays inside the frozen vocabulary and unaltered; **"provisional on the working-paper twin" is a scope label on the adjudicated object, not a fifth verdict**
> **fix:** Append amendment A12 to the protocol addendum recording the §9.1 verdict-vocabulary scope qualifier: what it is, why `indeterminate-from-full-text` was not used, that it attaches to the adjudicated object rather than the verdict token, that it is post-hoc, and the PRISMA-P item it touches (11c). Cross-reference it from §9.3, §9.4, §14 item 3 and VG-3, exactly as A7 is cross-referenced from §2.7 and §6.
> **reference:** Protocol §9.1 frozen verdict vocabulary; protocol §10 amendments policy; CHAMP item 5 (design violations declared); precedent set by amendment A7

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; every element of the finding reproduced. (1) lit_review line 2018 contains verbatim "Verdict: `episode-statistic-null` — PROVISIONAL ON THE WORKING-PAPER TWIN." and lines 2029-2032 contain the quoted scope-label defense. (2) Protocol §9.1 lines 598-603 freeze exactly four tokens (assignment-null / episode-statistic-null / mixed / indeterminate-from-full-text) with no scope-qualifier provision; a case-insensitive grep for version|working.paper|twin|preprint across the protocol returns only §2.4 tier handling, §4.1 twin ledger and §5 E1 — none authorizing substitution of the adjudicated object, and §9.1(iv) names the target by journal DOI 10.1016/j.jfs.2008.08.001. (3) The append-only addendum runs A1..A11 and ends at file line 1016; grep -rn "A12" docs/ matches only unrelated substrings inside search-log JSON; the review's own amendment register (lines 2660, 2697-2701) and frontmatter line 13 (amendments_appended_by_this_document: [A4..A11]) also stop at A11 — so no numbered amendment records the extension. (4) The precedent argument holds against refutation: A7 (protocol line 859) is the same shape (undefined level added to a frozen instrument, fixed retrospectively with a labelled CONVENTION) and A9 (line 913) shows a §9.1 departure already treated as amendment-worthy; §10 (lines 750-761) scopes amendments to "ANY deviation", and adjudicating IIIS DP 122 in place of the §9.1(iv) DOI-named target is a deviation in the adjudicated object regardless of the token being unaltered. (5) Disclosure elsewhere (§9.3, §14 item 3 line 3002, VG-3 line 2609, REV-1-6 row line 3118) does not constitute an addendum entry, and the finding already concedes the disclosure.

### REV-2-5 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1223-1225, 1513-1515
> **issue:** The reading rule that governs every count in §7 — and that the REV-1-13 remediation quotes verbatim as its authority for corpus-scoping the O4 claim — itself states the wrong scope: it says a count of records is a fact about "the literature's coverage". Over a corpus that lost 47.8% of its full-text-stage records, failed three of fourteen known-item recall checks and ran its backward-chase arm only post-freeze, a record count is a fact about *this corpus's* coverage and nothing more. The rule as written licenses precisely the generalisation the remediation was meant to close, and no coverage fraction anywhere in §6.1, §7 or §10.4 carries an uncertainty measure to support a literature-level reading.
> **evidence:** Reading rule, stated once and applied throughout: a count of records is a fact about the literature's coverage, never a fact about a detector. … The review's own reading rule applies to this claim as to every other: **a count of records is a fact about the literature's coverage, never a fact about a detector.**
> **fix:** Restate the reading rule as "a count of records is a fact about *this corpus's* coverage, never about the literature and never about a detector", and propagate the corrected wording to both quotation sites. If any coverage fraction is intended to estimate a literature-level proportion, attach a binomial interval and name the sampling frame; otherwise say explicitly that the fractions are census statistics of the frozen 72-record set.
> **reference:** CHAMP item 30 (conclusions limited to what the analysis supports); SAMPL §Basic statistical reporting (report a measure of precision with an estimated proportion); round-1 finding REV-1-13

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; the defect reproduces at every point. (1) Both quoted strings are verbatim at the stated lines of docs/literature/lit_review_explosive-regime-dating_2026-08-24.md (1223-1225 and 1513-1515), plus a third unlisted instance at line 468 in section 2.9 ("descriptions of the *literature's coverage*"). (2) No corpus-scoping definition exists: grep "the literature" returns 7 hits and none redefines the term as the frozen 72-record set; L-4 at line 2351 states the opposite, that unobtainable records "are not a random sample of the literature", and names "every coverage statement in 6.1 and 7" as affected. (3) The document contradicts itself inside one paragraph: line 1507-1508 says the O4 claim "is a statement about *this corpus's coverage*, not a universal negative about the literature", then line 1513-1515 invokes the rule in its literature-scoped wording. (4) No uncertainty measure exists on any coverage fraction: grep -E "\bCI\b|interval|precision|standard error|+/-|binomial|Wilson|confidence" over the whole file yields only lines 2179-2180 (no common effect estimate with a standard error to plot), 2586-2587 (the corpus reports almost no Monte Carlo standard errors) and 2950 (an excluded source paper's own CI construction) - none attaches precision to a review-computed proportion. The 6.1 fractions (58/65, 39/65, 13/65, 23/65, 27/65, 19/65, 5/53, 1/53) and 10.4 fractions (52/65, 39/65, 23/65, 19/65, 8/53) are bare census counts, yet 10.4 concludes at literature level: "the published record over-represents the characteristics on which these detectors do well." (5) Every corpus limitation the finding cites reproduces: 47.8% / 280 full-text-stage records lost with unknown direction (lines 136-137, 668-670, 2348), three of fourteen known-item recall failures (lines 145-146, 301-319, 627), backward-chase arm run only post-freeze under A11 over 22 of 27 carriers (lines 2354-2369). The single imprecision in the finding - characterising the rule as the remediation's "authority for corpus-scoping" when the adjacent sentence carries that scoping and the rule is invoked for the record-count-vs-detector-fact half - is a framing nuance, not concrete counter-evidence against the defect claim.

### REV-2-6 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1631-1635
> **issue:** The REV-1-13 remediation attached the L-4/L-5 recall bound at the point of claim in §7.4 and §7.8, and states that the O5 template is the standard to follow. §7.7 was not brought to that standard: its outcome is generalised from the corpus to "the state of the evidence" without any bound, and it is described as a "finding" although protocol §7 15c pre-registered exactly this outcome as the expectation. §7.7 is also the claim most sensitive to the one named backward-chase miss: `er-bc-1` (Hall, Psaradakis & Sola 1999) is a simulation study on periodically collapsing bubbles by a team non-overlapping with `eru-0150` and `eru-0131`, i.e. potentially the second arm of the pair whose absence §7.7 rests on. L-4 explicitly concedes the pooling condition "could in principle be met by a pair inside the X6 set"; L-5 makes no equivalent concession for the two named A11 candidates.
> **evidence:** **Outcome: structured no-meta-analysis**, exactly as the protocol anticipated. The failure is systematic rather than incidental — this literature's Monte Carlo designs are chosen to display each new method's contribution, not to be commensurable with predecessors — and it is itself the review's most transferable finding about the state of the evidence.
> **fix:** Rewrite §7.7's closing sentence corpus-scoped on the O5/§7.4 template; label the outcome as the pre-registered expectation confirmed rather than as a finding; and attach the A11 bound at the point of claim, naming `er-bc-1` as a record whose admission could in principle supply the non-overlapping second arm on the Evans-collapse power characteristic. Add the same one-line bound to §7.2's synthesis claim.
> **reference:** CHAMP items 28, 30; protocol §7 15c (pre-registered expectation); round-1 finding REV-1-13

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; the finding reproduces exactly. (1) The quoted closing sentence is verbatim at lit_review_explosive-regime-dating_2026-08-24.md:1631-1635, including the corpus-transcending phrases "this literature's Monte Carlo designs" and "the state of the evidence". (2) Section 7.7 (1616-1635) carries no L-4/L-5/A11 recall bound, while section 7.4 (1505-1519) carries one under an explicit heading "Recall bound attached at the point of the claim, not deferred to 12.1 (finding REV-1-13)" that names the O5 claim as "the template this claim now follows", and section 7.8 (1645-1649) carries the same bound; the asymmetry is measured against a standard the document itself declares. (3) No section-level bound covers 7.7: the section 7 header's only global caveat (1223-1225) is the counts-vs-detectors reading rule, and the L-4/L-5 caveat at 1209-1213 is explicitly scoped to section 6's numbers. (4) L-4 at 2354-2355 does concede "the meta-analysis condition in 7.7 could in principle be met by a pair inside the X6 set", but only in 12.1 - precisely the deferral REV-1-13 ruled insufficient; L-5 (2357-2379) names 7.4 and 7.8 as affected and makes no equivalent concession for er-bc-1/er-bc-2. (5) Protocol section 7 15c (protocol_explosive-regime-review_2026-08-24.md:554-562) pre-registers both the outcome ("the anticipated outcome is a structured no-meta-analysis") and the mechanism ("Monte Carlo designs in this literature differ in DGP, T, and r0"), so labelling it "the review's most transferable finding" does label a confirmed pre-registered expectation as a finding; the review's own "exactly as the protocol anticipated" mitigates but does not remove the label. (6) er-bc-1 is recorded at 273-279 as Hall, Psaradakis and Sola (1999), a simulation study on periodically collapsing bubbles with carriers eru-0463/eru-0526/eru-1509 - a team non-overlapping with eru-0150 (Homm and Breitung) and eru-0131 (PWY), so the modal claim that it could in principle supply a non-overlapping second arm on the Evans-collapse power row is not contradicted by the record. The only counter-line I could construct - that a 1999 paper cannot report power for supDF/supDFC/supBT/supB, which postdate it - attacks only the strength of the er-bc-1 example, does not settle it (a matched "power of the standard ADF under Evans-type collapse" cell against eru-0131 remains conceivable), and leaves the core defect (missing point-of-claim bound plus unbounded generalisation) untouched. That is a plausibility argument, not counter-evidence.

### REV-2-7 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:529-530
> **issue:** The REV-1-13 corpus-scoping did not propagate to the consumer artifact. The agenda's branch-3 Rev 4 text carries the O4 claim as an unscoped universal negative about the recursive family, which is the exact defect the review remediated in §7.4 ("A delay-versus-ARL₀ result for the recursive family may exist outside this corpus; nothing here bounds that possibility"). The blanket caveat at the foot of Verification status defers the bound to the end of the document — the pattern the review explicitly rejected when it wrote "Recall bound attached at the point of the claim, not deferred to §12.1". The agenda is the artifact a branch-3 specification will read.
> **evidence:** **No BSADF comparator specification in this branch may be written without stating which of the two it uses and carrying the corresponding cost.** The recursive family does *not* publish this branch's own declared comparison metric (delay against ARL₀).
> **fix:** Rewrite as "No record in the 72-record explosive-regime corpus publishes this branch's own declared comparison metric (delay against ARL₀) for the recursive family; the corpus lost 47.8% of its full-text-stage records and its backward-chase arm ran only post-freeze, so this bounds the corpus, not the literature (review §7.4)." Apply the same point-of-claim bound to the surveillance-line bullet.
> **reference:** CHAMP item 30; review §7.4 "Recall bound attached at the point of the claim, not deferred to §12.1"; round-1 findings REV-1-13, REV-1-7

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted and failed; the finding reproduces exactly.
>
> 1. Location check. C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md lines 529-530 read verbatim: "it uses and carrying the corresponding cost.** The recursive family does *not* / publish this branch's own declared comparison metric (delay against ARL₀)." No corpus qualifier, no recall bound, no "in this corpus" scope on that sentence or in the sentence preceding it (which scopes only tier: "extraction source Cowles DP 2331, 2022, working-paper tier").
>
> 2. Searched for any point-of-claim scoping I might have missed. grep -n -i "corpus|72-record|47.8" over the whole agenda returns nothing between lines 481 and 614 — i.e. nothing anywhere in the branch-3 block that would scope the O4 negative. The only scoping statements are at line 718 ("72-record included corpus") and lines 744-772 (Residual + the closing "Consequently the Rev 4 claims above state what the *included corpus* establishes"), both inside Verification status at the foot of the document, exactly as the finding describes.
>
> 3. Source check confirms the drift rather than refuting it. Review §7.4 (lit_review_explosive-regime-dating_2026-08-24.md:1417 ff.) states the O4 claim in scoped form — "**No record in this corpus reports a detection-delay-versus-ARL₀ characterisation for the recursive right-tailed family**" — and then, under the heading "Recall bound attached at the point of the claim, not deferred to §12.1 (finding REV-1-13)", writes "A delay-versus-ARL₀ result for the recursive family may exist outside this corpus; nothing here bounds that possibility." Both quoted strings in the finding are verbatim from the artifact.
>
> 4. The review's own consumer handoff makes the propagation obligation explicit, so the agenda's rendering is a real deviation, not a permitted paraphrase. §14 item 2 (line ~2980): "**no record in this corpus** publishes the quantity branch 3 declares as its comparison metric for that family… Both halves are corpus-scoped statements bounded by L-4 (280 unobtainable full texts) and L-5 (the backward-chase arm ran only as a post-freeze diagnostic); neither is a universal claim about the literature (§7.4, finding REV-1-13)."
>
> 5. The second half of the finding also holds: the surveillance-line bullet at lines 531-537 says "That line *does* publish a false-alarm rate over a stated horizon in closed form" with no corpus scope, where §14 item 2 marks it as one of the two corpus-scoped halves.
>
> The only candidate counter-evidence — the blanket caveat at line 771 — is the exact deferral pattern the finding names and REV-1-13 rejected, so it is not a refutation. No counter-test, source quote, or logical proof available that contradicts the defect claim.

### REV-2-12 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:394-395, 975-976, 2646; docs/methodology/protocol_explosive-regime-review_2026-08-24.md:863-865
> **issue:** The `partial`-cell denominator 585 contradicts the review's own assessable denominators. 585 is 65 records × 9 questions, but the review states that Q8 and Q9 are unanswerable for 12 recheck-only records, so the number of answered Q-cells is 65×7 + 53×2 = 561. The 50 `partial` cells are correct and match the §6.1 distributions exactly, but the denominator counts 24 `n/a` cells as answered. The wrong figure appears four times, including inside append-only amendment A7 in the frozen protocol addendum, where it is now difficult to correct cleanly. This is the REV-1-4 denominator discipline not being propagated to the QUANT-1-1 site.
> **evidence:** Execution used a **four-level** scale by adding `partial`, in **50 of the 585 answered Q-cells** (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29).
> **fix:** Correct the denominator to 561 at §2.7, §6, and §12.4 item 11, showing the arithmetic (65×7 for Q1–Q7 plus 53×2 for Q8/Q9). Because A7 is inside an append-only addendum, do not edit it; append a short correcting amendment (or an A7 erratum entry) stating the corrected denominator and that the 50-cell numerator and its per-question split are unchanged.
> **reference:** SAMPL §Basic statistical reporting (numerator and denominator for every reported proportion); CHAMP item 19; round-1 findings QUANT-1-1, REV-1-4

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; the finding is confirmed. (1) Summing the nine §6.1 per-question rows reproduces the stated assessable n exactly (Q1-Q7 = 65 each, Q8 = 53, Q9 = 53) and the partial column sums to 50. Total answered cells = 65*7 + 53*2 = 561, not 585. (2) 585 = 65*9 = (72 - 3 twins - 4 no-full-text) * 9, i.e. it excludes twins and no-full-text records but counts the 12 recheck-only records' 24 n/a Q8/Q9 cells as answered — exactly the defect alleged. (3) Direct grep confirms 12 rows tagged "single-pass (recheck only)" and 4 rows tagged "no full text; ER-RoB v1 not applied"; §6.1 line 1110 states the assessable denominators as "65 for Q1-Q7 and D1-D6, and 53 for Q8/Q9 and D7/D8", and line 1194 gives the 16 = 4 + 12 breakdown. (4) The only available defense — reading "answered" loosely to include n/a — is foreclosed by the review's own legend at line 987: "`n/a` = the question could not be answered because the underlying field was not extracted." (5) All cited sites reproduce: review lines 394, 976, 2697 (A7 amendment-table row), 3110 (QUANT-1-1 disposition row), and protocol line 864 inside the append-only A7 addendum entry. That is five occurrences, one more than the finding's stated "four times" — an understatement in the finding, not a defect in it. No counter-evidence obtained.

### SCOPE-2-1 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** partial
> **location:** C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:751-755
> **issue:** The agenda's Rev 4 residual paragraph — itself rewritten in this remediation round for SCOPE-1-6 — still asserts that the backward citation-chasing arm 'never executed', which the SCOPE-1-4 remediation superseded on the same day, and it carries neither of the two named candidate records the executed arm surfaced. The review explicitly designates the consumer/successor as the inheritor of those two named gaps, so the agenda is the site where they must land.
> **evidence:** Agenda l.751-755: '**Antecedent layer specifically.** The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed, and three known-item antecedents ... were recovered by the known-item arm alone.' Review amendment A11 (protocol l.969-1013): 'Executed 2026-09-02 over the 27 I2b-bearing included records ... The two candidates are therefore carried as **named, bounded recall gaps** ... and a successor pass that unfreezes the corpus inherits them.' Review §2.2 l.291-299: 'The gap changes character but does not close ... has named **two** specific records the frozen corpus does not contain, at least one of which looks eligible.' Grep of the agenda for `er-bc`, 'backward', 'near-miss' returns no hit carrying the candidates.
> **fix:** Replace 'never executed' with the executed-post-freeze status under A11 (22 of 27 carriers, deposited reference lists, single-agent, not a screening stage) and name `er-bc-1` Hall/Psaradakis/Sola 1999 and `er-bc-2` Banerjee/Chevillon/Kratz 2013 as inherited bounded recall gaps.
> **reference:** deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A item 2 ('Branch 3 integrates the review's verdicts'); review §14, A11

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; every element of the finding reproduced independently.
>
> 1. Agenda text at the stated location. C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md lines 751-755 read verbatim: "**Antecedent layer specifically.** The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed, and three known-item antecedents (Phillips & Magdalinos, Busetti & Taylor, Evans) were recovered by the known-item arm alone. Pre-2011 antecedent coverage therefore rests on the known-item list." The paragraph heading at l.742-744 confirms it was itself rewritten this round: "Corrected and extended 2026-09-02 after the Thread A audit round (findings LITERATURE-1-6, SCOPE-1-6, REV-1-2)".
>
> 2. The superseding record exists and is dated the same day. Protocol l.969 opens "### A11 — 2026-09-02 — supplementary search, executed AFTER corpus freeze"; l.985-987 state "Executed 2026-09-02 over the 27 I2b-bearing included records ... logged at docs/literature/search_logs/explosive-regime/se-bc-01.json"; l.994-995 "Carrier coverage 22 of 27"; l.998-1006 name `er-bc-1` Hall, Psaradakis & Sola (1999) and `er-bc-2` Banerjee, Chevillon & Kratz (2013); l.1011-1013 "carried as **named, bounded recall gaps** ... and a successor pass that unfreezes the corpus inherits them." Review §2.2 l.291-299 corroborates: "The gap changes character but does not close ... has named **two** specific records the frozen corpus does not contain, at least one of which looks eligible." Review l.2610 (VG-4), l.2701 (A11 row), l.3030 and l.3117 (SCOPE-1-4 disposition) all carry the executed status.
>
> 3. The candidates are absent from the agenda. `grep -n -i "er-bc|backward|near-miss|Psaradakis|Banerjee|Chevillon|Kratz"` over the agenda returns only lines 751-752 (the "never executed" sentence itself) — zero hits for either candidate. A second grep for "A11|recall gap|se-bc|post-freeze|frozen at 72" returns a single hit at l.348, which is an unrelated URL fragment (`.../oldpdf/A11n28.pdf`), not a reference to amendment A11.
>
> 4. Both files are uncommitted working-tree modifications (`git status --porcelain` shows ` M` on the agenda and the protocol), so the contradiction is live in the current round's output, not an artifact of a stale committed revision.
>
> The only angle that yielded any tension is that A11's phrase "a successor pass that unfreezes the corpus" names a successor review pass rather than the agenda by name; but that bears on where the fix should land, not on whether the defect exists. The core claim — the agenda asserts "never executed" for an arm the same-day A11 records as executed, and carries neither named candidate — is confirmed, so this is a severity/scoping quibble and not refutation.

### SCOPE-2-2 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** omitted
> **location:** C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:730-735, 769
> **issue:** The review's §14 item 3 — the transcription contract for the agenda — directs the agenda to record that none of NB-02/NB-08/NB-13 ever entered the screened universe as protocol §9.1 required (amendment A9, VG-9). The agenda records the three verdicts and NB-13's provisional status but omits the A9 disclosure entirely, so the agenda presents three adjudications whose prescribed screening audit trail does not exist as if they were normally screened records. The same paragraph's amendment roll-up is stale: it names only A4, A5 and A6 as post-hoc, whereas A4-A11 are all post-hoc entries and A9/A10/A11 are the substantive ones.
> **evidence:** Review §14 item 3 (l.3003-3006): 'Record also the NB-08 derivability note ... and the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9).' Agenda l.730-735 carries the verdicts and the NB-13 caveat only; grep for 'A9', 'force-screen', 'screened universe' over the agenda returns zero hits. Agenda l.769: 'Amendments A4, A5 and A6 are post-hoc and labelled as such.' Protocol addendum now runs A4-A11, each headed 'entry POST-HOC'.
> **fix:** Add the A9/VG-9 disclosure to the NB bullet, and replace the A4-A6 sentence with the full A4-A11 post-hoc set, naming A9 (force-screening not executed), A10 (I3/X7 violations inside the frozen set) and A11 (post-freeze backward-chase).
> **reference:** review §14 item 3; protocol addendum A4-A11

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; every claimed element reproduced exactly.
>
> 1. Review §14 item 3 verified at docs/literature/lit_review_explosive-regime-dating_2026-08-24.md (lines ~3003-3006): "Record also the NB-08 derivability note, which is the only route in that group to an online drawdown monitor and is TC-6, and the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)." The transcription contract is real and explicitly names the A9/VG-9 disclosure.
>
> 2. Agenda lines 730-735 verified: they carry only the discharge of the caveats ("all three adjudicated episode-statistic-null (review §9). Two on full text; NB-13 provisional — journal version unobtainable after four attempts ... re-openable under review protocol §10 (audit REV-1-6)"). No screening-audit-trail disclosure.
>
> 3. Counter-search for an equivalently-worded disclosure elsewhere in the agenda came back empty. grep -nE "A9|force-screen|screened universe|§9\.1|VG-9" over docs/research_notes/research_agenda_regime-classification_2026-08-21.md exits 1 (zero hits); grep for "\bA(7|8|9|10|11)\b" also exits 1. A broader grep for NB-02|NB-08|NB-13|audit trail|screen returns lines 14-15, 130-147, 514-518, 730-731, 768 only — none mentions force-screening or non-entry into the screened universe. Line 768's "the corpus was not re-screened" refers to the I3/X7 eligibility deviations, not to §9.1 force-screening.
>
> 4. Agenda line 769 verified verbatim: "- Amendments A4, A5 and A6 are post-hoc and labelled as such."
>
> 5. Protocol addendum verified stale-making: docs/methodology/protocol_explosive-regime-review_2026-08-24.md headers at lines 822, 834, 844, 859, 885, 913, 938, 969 run A4 through A11, every one marked "entry POST-HOC" (A11: "execution and entry both POST-HOC"). A9 (l.913) is headed "§9.1's force-screening requirement was not executed" and states "the audit trail §9.1 requires does not exist and cannot be manufactured after the fact."
>
> Both halves of the defect claim are true as stated: the A9/VG-9 disclosure is absent from the agenda, and the A4-A6 post-hoc roll-up is stale against an A4-A11 addendum.

### SCOPE-2-3 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** partial
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:938-943 vs 883-914; protocol A10(b)
> **issue:** The X7 drift declared by the round-1 remediation (amendment A10(b), §5.3, and the '72 records / 69 distinct works' figure repeated in the abstract, §6, §12.5 and the agenda) enumerates exactly three same-work twin pairs. §5.4 of the same document documents a fourth: `eru-0198` is described as the working-paper twin of `eru-0259`, with `eru-0259`'s extraction performed on `eru-0198`'s text. Unlike the three declared twins, both records carry independent appraisal rows in §6 with divergent Q cells, both count in the 65 assessable denominator, and neither store entry carries a twin note. The declared drift therefore does not cover all instances of itself, and §5.3's guarantee that 'each twin is extracted once, under its carrier, so no operating characteristic is double-counted' does not hold for this pair.
> **evidence:** §5.4 l.938-943: '`eru-0259` Franses (2016) ... extraction was performed on the working-paper twin `eru-0198` (Econometric Institute Report 2013-12). Twin status was verified against the published article's indexed abstract.' §5.3 l.888: 'Three pairs survived into the frozen included set'. §6 row 4 (`eru-0259`, 'single-pass (recheck only)', Q4 `no`, Q7 `yes`, D-rule `LLRRLL··`) and row 64 (`eru-0198`, 'single-pass (primary only)', Q4 `partial`, Q7 `no`, D-rule `LLRRLRRR`) are two independent appraisals of what §5.4 says is one text. Grep of references_explosive-regime.json for `eru-0198`/`eru-0259` shows no twin note on either entry.
> **fix:** Either extend A10(b), §5.3, the store notes and the distinct-works count to the `eru-0198`/`eru-0259` pair (72 records / 68 distinct works, one appraisal row voided or marked `—`), or state explicitly in §5.4 why this pair is not an X7 twin despite the extraction substitution, and reconcile the two divergent appraisal rows.
> **reference:** protocol §2.3 X7; amendment A10(b); round-1 finding SCOPE-1-5

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; every element of the finding reproduces at the stated locations, and no text in any of the four artifacts distinguishes the eru-0198/eru-0259 pair from the three declared X7 twins.
>
> (1) Scope of the declared drift. lit_review l.888: "Three pairs survived into the frozen included set and were identified at extraction:" followed by a three-row table (l.892-894) naming only eru-0622/eru-0675, eru-0154/eru-0126, eru-0904/eru-1526. Protocol A10(b) at docs/methodology/protocol_explosive-regime-review_2026-08-24.md:956-961 enumerates the identical three and states "the included set is **72 records / 69 distinct works**". The 72/69 figure recurs at lit_review l.94, 151, 896, 954, 2400, 2700 and research_agenda l.767. No fourth pair anywhere.
>
> (2) §5.4 does call this pair a twin. l.938-942 verbatim: "`eru-0259` Franses (2016) ... the journal PDF was unobtainable (publisher paywall, no OA deposit located); extraction was performed on the working-paper twin `eru-0198` (Econometric Institute Report 2013-12). Twin status was verified against the published article's indexed abstract. Numbers attributed to `eru-0259` are the working-paper's numbers." Corroborated a second time by L-10 at l.2422: "`eru-0259`'s journal version was unobtainable and its working-paper twin was extracted".
>
> (3) Asymmetric treatment vs the declared twins is confirmed, not explained. In §5.2 the three declared twins carry extraction status "twin (extracted under eru-0126/0675/1526)" (l.780, 785, 790) and in §6 their rows are all-`—` with D-rule `········` (l.1074, 1079, 1084). By contrast §5.2 l.740 gives eru-0259 "full text at recheck only, single pass" and l.800 gives eru-0198 "full text, single pass", and §6 carries two full independent appraisals: row 4 (eru-0259) Q4 `no‡`, Q7 `yes‡`, D-rule `LLRRLL··`; row 64 (eru-0198) Q4 `partial‡`, Q7 `no‡`, D-rule `LLRRLRRR`. Two divergent appraisals of what §5.4 says is one extracted text.
>
> (4) Both sit inside the assessable denominator. §6.1 l.1106-1110 derives 65 as 72 minus "3 ... twins appraised `—`" minus "4 ... no full text"; neither eru-0198 nor eru-0259 is in either excluded class, so both count. 72−3−4=65 checks out.
>
> (5) Store. Parsing docs/literature/references_explosive-regime.json (72 entries): eru-0259 has no `note` field at all; eru-0198's only note is "I3 satisfied by Handle 1765/39598 (Handle System responseCode 1, checked 2026-09-02); no DOI registered." Neither carries a twin note, and neither appears in the X7 dedup ledger (the ledger's X7 rows at l.2753-2754 concern eru-0106/eru-0127 against eru-0154 only).
>
> (6) Counter-test for an exculpatory statement: grep of all four artifacts for every occurrence of `eru-0198`/`eru-0259` returns lit_review l.740, 800, 816, 938-942, 1034, 1094, 2422, 2612 and nothing in the protocol or agenda. The nearest candidate defense, VG-6 (l.2612), groups eru-0259 with eru-0150 and eru-1289 as "extracted from working-paper versions, not from the published versions their DOIs resolve to" — but that class is not exculpatory here, because eru-0150's and eru-1289's working papers are not themselves corpus records, whereas eru-0198 is record 64 of 72 with its own appraisal row. VG-6 therefore does not state, and no other passage states, why this pair is not an X7 twin.
>
> Consequently §5.3's guarantee at l.899-900 ("Each twin is extracted once, under its carrier, so no operating characteristic is double-counted") and the identical sentence in A10(b) are contradicted for this pair by the document's own §5.2/§6 rows. The defect claim holds; only severity or fix choice could be argued, which is not refutation.

### SCOPE-2-4 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** partial
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:113-116, 1579-1586, 1608-1609, 694
> **issue:** The REV-1-4 remediation requires every coverage fraction to be stated over a named assessable denominator with the excluded classes named. The O6 site fails on both counts and now contradicts itself in three places: the abstract asserts the partition is over 72 but names only 63 records (22+22+19), leaving SPLIT 3, NS 2 and NE 4 unnamed at that site; §7.6's table sums to 72; and §7.6's synthesis sentence states 'Of the 65 records with an extracted causality status', a denominator that matches neither its own table (68 records carry an extracted status once NE 4 is removed) nor §4's 72-record partition. The 65 appears to have been imported from the Q1-Q7 assessable denominator, where it does not apply.
> **evidence:** Abstract l.114-116: '22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the record set, so 72 is the right denominator here)'. §7.6 table l.1581-1586: RT 22, CS 19, FS 22, SPLIT 3, NS 2, NE 4 = 72. §7.6 l.1608: 'Of the 65 records with an extracted causality status, fewer than one in three publishes a characteristic measured on a genuinely real-time procedure'. §4 l.694 gives the same six-class partition over 72.
> **fix:** State the O6 denominator once and consistently — 68 records with an extracted causality status (72 minus the 4 NE), or 72 for the full partition — and name the excluded classes (SPLIT, NS, NE) at the abstract site as the REV-1-4 remediation requires elsewhere.
> **reference:** round-1 finding REV-1-4; §6.1 denominator rule

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; the defect reproduced in full and additional confirming evidence emerged. (1) Abstract l.113-116 reads verbatim "22 of the 72 records evaluate a detector in genuinely real-time form; 22 are full-sample only; 19 use a causal statistic but report only ex-post evaluation (a partition of the record set, so 72 is the right denominator here)" — 22+22+19=63 named of 72, with SPLIT 3, NS 2, NE 4 unnamed, contrary to REV-1-4's requirement at l.3112 that denominators be stated "with the excluded classes named at each site". (2) The §7.6 table l.1581-1586 sums RT 22 + CS 19 + FS 22 + SPLIT 3 + NS 2 + NE 4 = 72, matching §4 l.694. (3) §7.6 l.1608 reads verbatim "Of the 65 records with an extracted causality status, fewer than one in three publishes a characteristic measured on a genuinely real-time procedure." Counter-test on the arithmetic: no reading of the table yields 65. Records with an extracted status = 72 - 4 NE - 2 NS = 66; RT+CS+FS+SPLIT = 66; the auditor's alternative (72 - 4 NE) = 68. The only arithmetic route to 65 is 72 - 4 NE - 3 twins, but §4's extraction-depth row lists "twin extracted under its carrier 3" and "no full text at any stage 4" as disjoint classes, the twins are already counted inside RT/CS/FS, and that route still wrongly retains the 2 NS records that by definition have no extracted status. 65 is exactly the Q1-Q7/D1-D6 assessable denominator declared at l.102 ("65 records for Q1-Q7 and D1-D6, 53 for Q8/Q9 and D7/D8") and l.1110, corroborating the alleged import. (4) Independent confirmation the auditor did not raise: the sentence is self-falsifying on its own denominator — 22/65 = 33.85%, which is more than one in three, so "fewer than one in three" is false at 65 (and at 66 = 33.33%); it holds only at 68 (32.4%) or 72 (30.6%). The claim of a three-way denominator inconsistency at the O6 site is true as stated.

### QUANT-2-1 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** numerical
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:394,976,2697,3110 and C:/Users/skoir/castles/docs/methodology/protocol_explosive-regime-review_2026-08-24.md:864 (amendment A7)
> **issue:** The remediation's own denominator for the response-scale deviation is wrong and contradicts the assessable-denominator rule the same remediation installed. 'partial in 50 of the 585 answered Q-cells' uses 65x9=585, i.e. it counts the 24 Q8/Q9 cells of the 12 recheck-only records as answered although the §6 table shows them as n/a and §6.1 fixes the Q8/Q9 denominator at 53. The correct count of answered (non-n/a, non-twin) Q-cells is 65x7 + 53x2 = 561. The error is now embedded in the append-only protocol addendum (A7), which is the auditable registration carrier.
> **evidence:** Recount over the §6 table (parser handling escaped pipes): total answered Q cells = 561; 585 - 561 = 24 = 12 recheck-only records x {Q8,Q9}. Per-question partial counts (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29 = 50) all reproduce exactly, so only the denominator is wrong. §6.1 states the same cells as 'assessable denominators are therefore 65 for Q1-Q7 and D1-D6, and 53 for Q8/Q9 and D7/D8'.
> **fix:** Append a new addendum entry A12 correcting A7's denominator to 561 (50/561 = 8.9%) with the exclusion classes named (4 no-full-text, 3 twins, 12 recheck-only x Q8/Q9); A7 itself cannot be edited under §10's append-only rule. Restate the figure at review lines 394, 976, 2697 and 3110.
> **reference:** protocol §10 (append-only addendum); PRISMA 2020 item 13a/18, doi:10.1136/bmj.n71

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Could not refute; the finding reproduces exactly. Independent parse of the §6 table in docs/literature/lit_review_explosive-regime-dating_2026-08-24.md (lines 952-1103; 72 rows, 24 columns, escaped-pipe-aware split, dagger/section/pilcrow markers stripped) yields: total answered (non-n/a, non-twin-dash) Q-cells = 561, with per-question answered counts Q1-Q7 = 65 each and Q8 = Q9 = 53. Value tally: yes 239, no 245, partial 50, unclear 27, n/a 60, twin em-dash 27. Per-question `partial` counts reproduce the review's stated list exactly (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29; sum 50), so only the denominator is wrong. Pass-column classification confirms the exclusion classes: 12 'single-pass (recheck only)', 4 'no full text', 3 'twin of ...', 2 'single-pass (primary only)'; 585 - 561 = 24 = 12 recheck-only records x {Q8,Q9}. The same document's §6.1 (lines 1109-1112) states 'The assessable denominators are therefore **65 for Q1-Q7 and D1-D6**, and **53 for Q8/Q9 and D7/D8**', and its signalling-question table lists assessable n = 65 x7 then 53, 53 — so 585 (65x9) contradicts the review's own installed rule and the literal `n/a` entries in those 24 cells. The string 'in 50 of the 585 answered Q-cells' / '50 of 585 answered Q-cells' is present at review lines 394, 976, 2697, 3110 and at protocol_explosive-regime-review_2026-08-24.md line 864 within amendment A7; protocol §10 'Addendum (append-only; empty at freeze)' exists at line 765, confirming the append-only carrier claim. No alternative reading of 'answered' survives, since the disputed 24 cells are recorded as n/a in the source table.

### QUANT-2-2 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1608-1613 (§7.6 synthesis claim O6)
> **issue:** The O6 synthesis claim — the domain the consumer agenda's standing hazard turns on — rests on a denominator that is not derivable from the review's own O6 distribution, and the directional statement is false at that denominator. §7.6 says 'Of the 65 records with an extracted causality status, fewer than one in three publishes a characteristic measured on a genuinely real-time procedure'. The O6 table gives RT 22, CS 19, FS 22, SPLIT 3, NS 2, NE 4 (=72), so records with an extracted status are 66 (72 minus 4 NE minus 2 NS), not 65; and 22/66 = 33.3% is exactly one in three while 22/65 = 33.8% is MORE than one in three. Only the abstract's denominator of 72 (22/72 = 30.6%) supports 'fewer than one in three', and the abstract and §7.6 therefore state the same quantity over two different denominators.
> **evidence:** Recount of the §5 table's O6 column: Counter({'FS': 22, 'RT': 22, 'CS': 19, 'NE': 4, 'SPLIT': 3, 'NS': 2}) = 72; the three twins carry O6 codes (eru-0154 CS, eru-0622 FS, eru-0904 CS), so the 65 used for Q1-Q7 (which excludes twins) is not the O6 assessable set. Abstract line 113: '22 of the 72 records evaluate a detector in genuinely real-time form ... a partition of the record set, so 72 is the right denominator here.'
> **fix:** State the O6 fraction as 22/66 records with an extracted status (or 22/72 over the full partition), name the excluded classes (4 NE, 2 NS), and replace 'fewer than one in three' with the arithmetically true form ('about one in three' at 66; 'fewer than one in three' only if 72 is used).
> **reference:** PRISMA 2020 item 20b (synthesis results with denominators), doi:10.1136/bmj.n71

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted and failed; the finding is confirmed on independent reproduction. (1) The §7.6 text at lit_review_explosive-regime-dating_2026-08-24.md:1608-1613 reproduces verbatim ("Of the 65 records with an extracted causality status, fewer than one in three ..."). (2) An independent parse of all 72 rows of the §5 table (line 735 onward), correcting for 3 rows whose escaped "I2a\|I2b" cell adds a column, yields Counter({FS:22, RT:22, CS:19, NE:4, SPLIT:3, NS:2}) = 72, matching the §7.6 table at lines 1579-1587 and the summary line 694. (3) §4.1 (lines 708-722) defines NE as "not extracted - no full text obtained at any stage" and NS as "causality status not stated in the extracted text", so the set with an extracted status is 72-4-2 = 66, not 65. (4) The 65 is the Q1-Q7/D1-D6 denominator defined in the abstract (lines 101-103) as 72 minus 3 twins minus 4 no-full-text; the three twins are eru-0154 (line 780, CS), eru-0622 (785, FS), eru-0904 (790, CS) - all carry O6 codes and none is RT/NS/NE - so 65 still contains the 2 NS records and is not the O6-assessable set. (5) Arithmetic across every candidate denominator: 22/63=34.92%, 22/65=33.85% (GREATER than one in three), 22/66=33.33% (exactly one in three), 22/68=32.35%, 22/69=31.88%, 22/72=30.56%. "Fewer than one in three" is false at 65 and at 66 and true only at 68+, i.e. only on the abstract's 72, which line 113 justifies separately as a partition denominator. (6) grep over the document for "one in three", "extracted causality", "22 of" finds no reconciling note; the other "22 of" hits are the unrelated 22-of-27-carriers citation-chasing diagnostic. Alternative readings also fail: counting SPLIT into the numerator gives 25/65=38.5%; reading 65 as 72-4 NE-3 SPLIT is arithmetically coincident but still 22/65=33.85% > 1/3. No reading of the review's own O6 distribution makes the denominator 65 and the direction "fewer than one in three" simultaneously true.

### QUANT-2-3 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** numerical
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1237,1430,1592,1743,1825,2148-2149; C:/Users/skoir/castles/docs/research_notes/research_agenda_regime-classification_2026-08-21.md:110,499
> **issue:** The page locators for the review's most load-bearing quotations are wrong in 3 of 5 spot-checks against the published texts, and the errors propagate into the consumer agenda. §9.5 exists precisely so a successor auditor can 're-open the quoted page', so wrong locators defeat the remediation's stated purpose. The quoted strings and the extracted numbers themselves verify verbatim; only the page attributions fail, and not by a uniform offset (Table 4 at p.221 is correct), so this is sporadic transcription error rather than a systematic pagination convention.
> **evidence:** Retrieved Cowles Foundation Papers 1349/1498 (journal pagination in the running heads) and located each item: PWY Table 3 Panel A (ADF1 size 0.049 at g=0.00) is on IER p.219, review says 'Table 3 Panel A p.220' (line 1237, 2148); 'sup_r ADF_r cannot reveal the location of the exuberance' is on p.214, review says 'IER 52:215' (lines 1592, 1743); 'cvadf(s) = log(log(ns))/100 ... leads to critical values around the 4% significance level' is on p.207 (and repeated p.214), review says 'p.208, p.211' and p.211 carries neither (lines 1430, 2148); PSY 2015a's 'may be used as an ex ante real-time dating procedure, whereas the GSADF test is an ex post statistic' is on p.1053, review and agenda say p.1054 (lines 2149, 1825; agenda 110, 499). PWY Table 4 on p.221 is correctly cited. The underlying source of the error is the extraction record itself (se-extraction-primary.jsonl eru-0131 rob: 'Q2 ... [Table 3, p.220]', 'Q1 ... [pp.208, 214]').
> **fix:** Correct the four locators to p.207, p.214, p.219 and p.1053 in §7.1, §7.4, §7.6, §8.2, §8.3 and the §9.5 table, propagate the p.1053 correction to agenda lines 110 and 499, and record in §9.5 that the locators were re-verified against the retrieved reprints on this pass.
> **reference:** Phillips, Wu & Yu 2011 IER 52(1):201-226, doi:10.1111/j.1468-2354.2010.00625.x (Cowles Paper 1349, korora.econ.yale.edu/phillips/pubs/art/p1349.pdf); Phillips, Shi & Yu 2015a IER 56(4):1043-1078, doi:10.1111/iere.12132 (Cowles Paper 1498)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt FAILED — the finding is confirmed on all four locators. I independently retrieved the two Cowles reprints over plain HTTP (the review's §9.5 recorded a FAILED fetch because it used https; http://korora.econ.yale.edu/phillips/pubs/art/p1349.pdf returns 200, 258,681 bytes, sha256 a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4; p1498.pdf 1,204,657 bytes, sha256 dfd19565775d1c9814ac1d33128223f585f201a0e740020f13e3254ed83a8c81), extracted per-page text with pypdf, and anchored the PDF-page→journal-page map on the running heads (p1349: PDF p.3 head "202 PHILLIPS, WU, AND YU" through PDF p.22 head "EXPLOSIVE BEHAVIOR IN THE 1990S NASDAQ 221", i.e. journal = PDF+199; p1498: PDF p.3 "1044 PHILLIPS, SHI, AND YU", PDF p.12 "TESTING FOR MULTIPLE BUBBLES 1053", i.e. journal = PDF+1041).
>
> (1) PWY Table 3 Panel A: the page whose running head reads "…NASDAQ 219" carries "TABLE 3 POWER OF THE ADF1 TEST Panel A … g = 0.00 (size) … 0.049". Journal p.220 contains no Table 3 body, only the narrative "Table 4 reports the empirical power…". Review lines 1237 and 2148 say "Table 3 Panel A p.220" — wrong; correct is p.219.
>
> (2) "However, sup_{r∈[r0,1]} ADF_r cannot reveal the location of the exuberance" appears on the page headed "214 PHILLIPS, WU, AND YU"; it occurs nowhere on p.215. Review lines 1592 and 1743 cite "IER 52:215" — wrong; correct is p.214.
>
> (3) "The setting employed is cvadf_βn(s) = log(log(ns))/100. For the sample sizes considered in our empirical application, this setting leads to critical values around the 4% significance level" is on the page headed "…NASDAQ 207". A per-page scan shows the token "cvadf" on journal pp. 207, 210, 211, 212, 214 and the string "4% signi" only on pp. 207 and 214. Journal p.208 contains neither "cvadf" nor the rule (it runs from "has some good properties…" into §3.1 and eq. (9)); p.211 carries eq. (14), not eq. (13) nor the log-log rule. Review lines 1430 and 2148 cite "p.208, p.211" — wrong; correct is p.207 (restated p.214).
>
> (4) PSY 2015a: "Importantly, the new date-stamping strategy may be used as an ex ante real-time dating procedure, whereas the GSADF test is an ex post statistic used for analyzing a given data set for bubble behavior" is on the page headed "TESTING FOR MULTIPLE BUBBLES 1053". Review lines 1825 and 2149 and agenda lines 110 and 499 say p.1054 — wrong; correct is p.1053.
>
> (5) The auditor's control case verifies: "TABLE 4 POWER OF THE ADF1 AND sup_r ADF_r TESTS UNDER THE EVANS (1991) MODEL" is on the page headed "…NASDAQ 221", so the p.221 citation is correct and the errors are not a uniform offset.
>
> (6) The upstream cause verifies too: docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl record eru-0131 rob carries "Q1 … [pp.208, 214]" and "Q2 … empirical size 0.049 at nominal 5%, T=120 [Table 3, p.220]".
>
> Quoted strings and extracted numbers verify verbatim, as the finding states; only the page attributions fail. No counter-evidence found.

### QUANT-2-4 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reproducibility
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2148-2175 (§9.5), 2560-2575 (L-16), 2616 (VG-10)
> **issue:** The remediation of QUANT-1-7 rests on an un-refetchability claim that does not hold. §9.5 marks all three Phillips texts 'FAILED — host korora.econ.yale.edu did not accept a connection' with digest 'none', and L-16/VG-10 assert the four texts 'cannot presently be re-opened from this environment'. The host serves all three PDFs on demand from the exact URLs the review records, so digests and quote re-verification were available and VG-10 is overstated for three of its four texts. This matters because VG-10 is the gap the review asks the consumer to carry over §8.3's statistic-attribution correction.
> **evidence:** HTTP 200 application/pdf from http://korora.econ.yale.edu/phillips/pubs/art/p{1349,1498,1499}.pdf: p1349.pdf 258,681 B sha256 a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4 (page 1: 'EXPLOSIVE BEHAVIOR IN THE 1990S NASDAQ ... COWLES FOUNDATION PAPER NO. 1349'); p1498.pdf 1,204,657 B sha256 dfd19565775d1c9814ac1d33128223f585f201a0e740020f13e3254ed83a8c81; p1499.pdf 470,694 B sha256 85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012. Quote re-verification against these files succeeded verbatim for 'cannot reveal the location of the exuberance', the cvadf/4% gloss, the PSY ex-ante/ex-post sentence, the PSY Table 2 size vector 0.041/0.049/0.042/0.054/0.060 and 0.061/0.058/0.055/0.069/0.070 with r0 = 0.01+1.8/sqrt(T), and PSY 2015b Theorems 2, 3 and 8's rate conditions. Only Cowles DP 2331 (eru-1289) remains genuinely unobtainable (elischolar viewcontent returns 403 HTML), so the FWER triple's single-session status stands.
> **fix:** Re-fetch the three reprints, record their SHA-256 digests in the §9.5 table, mark the quote/page re-verification as performed, and narrow L-16/VG-10 to eru-1289 (Cowles DP 2331) alone; state that the earlier 'host did not respond' entry was a transient retrieval failure, not an access barrier.
> **reference:** project reproducibility contract (CLAUDE.md §Reproducibility contract); §9.5 as delivered

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation available — the counter-test I ran confirms the finding rather than disproving it.
>
> Direct re-fetch from the exact URLs §9.5 records, run from this environment on this machine:
> - http://korora.econ.yale.edu/phillips/pubs/art/p1349.pdf -> HTTP 200, content_type application/pdf, 258,681 B, sha256 a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4
> - .../p1498.pdf -> HTTP 200, application/pdf, 1,204,657 B, sha256 dfd19565775d1c9814ac1d33128223f585f201a0e740020f13e3254ed83a8c81
> - .../p1499.pdf -> HTTP 200, application/pdf, 470,694 B, sha256 85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012
>
> All three byte counts and all three digests match the auditor's claimed values exactly. Files are valid PDF 1.6; first pages read "EXPLOSIVE BEHAVIOR IN THE 1990S NASDAQ ... Phillips, Wu and Yu", "TESTING FOR MULTIPLE BUBBLES: HISTORICAL EPISODES ...", and "TESTING FOR MULTIPLE BUBBLES: LIMIT THEORY OF REAL TIME DETECTORS ... COWLES ...", i.e. bound to eru-0131, eru-0393, eru-0395 respectively.
>
> Quote re-verification against the fetched files (pypdf text extraction, NFKD-normalized): p1349 contains "cannot reveal the location of the exuberance" verbatim and the cvadf gloss verbatim — "cvadf βn (s) = log(log(ns))/100. For the sample sizes considered in our empirical application, this setting leads to critical values around the 4% significance level" (an initial literal match on "4% significance level" failed only because of the fi ligature U+FB01, not absence). p1498 contains "ex ante real-time dating procedure". p1499 (57 pp.) carries the theorem statements.
>
> Therefore §9.5's "FAILED — host korora.econ.yale.edu did not accept a connection" / digest "none" entries for eru-0131, eru-0393, eru-0395, and the L-16/VG-10 claim that those texts "cannot presently be re-opened from this environment", are false as written: the host serves them on demand and both digesting and quote re-verification were achievable. The only element I could not disturb is the auditor's own concession that eru-1289 (Cowles DP 2331) remains unobtainable, which is not part of the defect claim. The defect claim stands.

### QUANT-2-5 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** C:/Users/skoir/castles/docs/research_notes/research_agenda_regime-classification_2026-08-21.md:743-772 (Verification status, Residual)
> **issue:** The consumer agenda's residual paragraph is stale against the review it now cites and under-discloses in three ways the review explicitly asks it to carry. (a) It states the backward-chase arm 'never executed' and that pre-2011 antecedent coverage rests on the known-item list, omitting amendment A11's post-freeze execution and, more importantly, the two named unadmitted candidates — er-bc-1 Hall, Psaradakis & Sola (1999) is exactly a pre-2011 antecedent that the diagnostic found and the corpus does not contain, so the agenda still reports an unbounded gap where the review reports a named bounded one. (b) It says 'Amendments A4, A5 and A6 are post-hoc' when A4-A11 are all post-hoc entries, including A7/A8 (instrument deviations qualifying every concern-profile claim the agenda leans on) and A9/A10. (c) It omits A9 entirely, although §14 item 3 instructs the agenda to record 'the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)' — the NB-02/NB-08/NB-13 bullet presents the caveats as discharged with no mention that the three carry no screening verdict.
> **evidence:** Agenda line 752: 'The protocol\'s backward citation-chasing arm (er-bc-*, protocol §3.3) never executed'; line 769: 'Amendments A4, A5 and A6 are post-hoc and labelled as such.' Review §14 item 3 (line ~3005): 'Record also ... the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9).' Independent check of the 1,996-record candidate store confirms er-bc-1 is genuinely absent (no DOI or normalised-title match; the Markov-switching descendants eru-0125/eru-0180 are present but were lost to X6).
> **fix:** Rewrite the residual bullets: state that the er-bc-* arm ran post-freeze under A11 through publisher-deposited reference lists over 22 of 27 carriers and named two unadmitted candidates (er-bc-1 Hall/Psaradakis/Sola 1999, er-bc-2 Banerjee/Chevillon/Kratz 2013), that the gap is bounded-and-named but not closed; change 'A4, A5 and A6' to 'A4-A11'; and add the A9/VG-9 disclosure to the NB-02/NB-08/NB-13 bullet.
> **reference:** review §14 items 2-3, amendments A9 and A11; PRISMA 2020 item 24c (protocol deviations)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Could not refute; all three sub-claims reproduced and independently corroborated. (a) Agenda line 752 reads verbatim "The protocol's backward citation-chasing arm (er-bc-*, protocol §3.3) never executed ... Pre-2011 antecedent coverage therefore rests on the known-item list", while review VG-4 (line 2610), amendment A11 (line 2701) and §16 SCOPE-1-4 (line 3117) record the arm as executed post-freeze over 22/27 I2b carriers with two named unadmitted candidates (er-bc-1 Hall/Psaradakis/Sola 1999, er-bc-2 Banerjee/Chevillon/Kratz 2013) and state the gap is "bounded and named rather than unbounded, but it is not closed". A grep of the entire agenda for A11|A9|VG-9|er-bc-1|er-bc-2|Psaradakis|Chevillon returns only line 348, an unrelated URL fragment (A11n28.pdf). (b) Agenda line 769 reads "Amendments A4, A5 and A6 are post-hoc and labelled as such"; review PRISMA row 24a/b/c (line 2660) states "A4-A11 are appended to the protocol addendum by this document (§12.5), all eight labelled post-hoc", and A7/A8 (lines 2697-2698) are the instrument deviations qualifying the concern-profile claims the same residual paragraph leans on. (c) Review §14 item 3 (line 3006) verbatim: "Record also ... the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)"; the agenda's NB-02/NB-08/NB-13 bullet (lines 730-735) carries only the NB-13 provisional caveat with no A9/VG-9 mention anywhere in the file. Independent counter-test on the falsifiable assertion: references_explosive-regime.json contains exactly one Psaradakis author literal (line 2405, eru-1509 Morita/Psaradakis/Sola/Yunis 2023), confirming er-bc-1 Hall/Psaradakis/Sola 1999 is absent from the frozen 72 — so the named bounded gap is real. The only available counter-argument (a residual paragraph need not enumerate every amendment) is a plausibility argument, not counter-evidence, and fails because A7/A8 govern the appraisal caveat the paragraph already states and A9 disclosure is explicitly instructed by the review.

### QUANT-2-6 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2448-2515 (L-13, especially (e))
> **issue:** L-13 is the fix for 'a partial metadata check reported as a complete one', and it reintroduces the same defect on the year field. It claims a check 'field by field on container title, volume, issue, page range and year' over 62 of 62 records, then discloses only 'seven further records' where the online year and the print year diverge. A full recomputation over all 62 Crossref records finds 19 records with a published-online/published-print year divergence and 22 records whose §5/§6 display-label year differs from the store's issued year. Two specific statements are also wrong: eru-1117's print year is two years later, not 'one later' (online 2021-05-05, print 2023-01-19), and eru-1155's label year 2018 matches neither the store (2021), nor Crossref online (2021), nor the issue implied by the DOI slug 201707 — it is flagged in (a) for volume only. Finally the CONVENTION as declared ('the review dates a record by first publication (online-first or working paper), not by issue year') is contradicted by the review's own labels in most divergent cases: Homm & Breitung labelled 2012 (online 2011, store 2011), Phillips/Shi/Yu labelled 2014 (online 2013, store 2013), Sollis labelled 2016 (online 2015), Phillips & Shi labelled 2018 (online 2017).
> **evidence:** Live Crossref pull for all 62 DOI-bearing records: 19 with online-year != print-year (eru-0150, 0238, 0348, 0559, 0597, 0689, 0748, 0891, 1044, 1112, 1117, 1260, 1384, 1509, 1580, 1604, 1715, 1845, 0691); 22 records where the §6 label year != store issued year. eru-1117 10.1093/jjfinec/nbab009: published-online [[2021,5,5]], published-print [[2023,1,19]]. eru-1155 10.6339/jds.201707_15(3).0007: Crossref online [[2021,3,8]], vol 15 iss 3 pp.495-508; store issued 2021; review label 'Harsha & Ismail 2018'. The 13 volume/issue/page rows in L-13(a) and the 3 pagination updates in (b) all reproduce exactly, so the failure is confined to the year field.
> **fix:** Either enumerate all 19 online/print year divergences under the CONVENTION and reconcile the 22 label-vs-store year mismatches, or narrow L-13's completeness claim to the fields actually reconciled (container title, volume, issue, page range) and state that the year field was checked only for the seven listed records. Correct eru-1117's 'one later' to two, and add eru-1155's year to (a).
> **reference:** api.crossref.org/works/{doi} retrieved 2026-09-02; PRISMA 2020 item 27 / L-13's own completeness assertion

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; every checkable component of QUANT-2-6 reproduced independently.
>
> 1. Online/print year divergence count. I pulled all 62 DOI-bearing records from api.crossref.org myself (2026-09-02, 62/62 retrieved). Exactly 19 have published-online year != published-print year: eru-0150, 0238, 0348, 0559, 0597, 0689, 0691, 0748, 0891, 1044, 1112, 1117, 1260, 1384, 1509, 1580, 1604, 1715, 1845 — identical to the auditor's list. L-13(e) at lit_review_explosive-regime-dating_2026-08-24.md:2504-2511 discloses only seven (eru-0691, 1112, 1117, 1384, 1509, 1580, 1845), while L-13's preamble (L2448-2458) asserts the check was run "field by field on container title, volume, issue, page range and year" over "all 62 DOI-bearing included records". Twelve divergences are undisclosed. The completeness claim is therefore false on the year field, exactly as alleged.
>
> 2. eru-1117 "one later" is wrong. Crossref 10.1093/jjfinec/nbab009: published-online [[2021,5,5]], published-print [[2023,1,19]] — two years later, not the "one later" L-13(e) asserts for the whole seven-record set.
>
> 3. eru-1155 year error is real and uncorrected. Crossref 10.6339/jds.201707_15(3).0007: published-online [[2021,3,8]], no published-print, vol 15 iss 3 pp.495-508. Store issued 2021. Review §5 (L792) and §6 (L1086) label it "Harsha S, Ismail B (2018)" / "Harsha & Ismail 2018". L-13(a) row at L2470 corrects only the volume (16(3) -> 15(3)) and is silent on the year. 2018 matches neither the store, nor Crossref, nor the 201707 DOI slug.
>
> 4. Label-vs-store year mismatches are widespread. Parsing the §5 corpus table and §6 RoB table against the CSL store's issued year, I find 23 records whose display-label year differs from the store's issued year (eru-0150 2012/2011, 0238 2014/2013, 0259 2016/2014, 0348 2016/2015, 0463, 0513, 0559, 0597, 0604, 0689, 0748, 0749 2020/2018, 0889, 0891, 1044, 1112, 1155, 1260, 1394, 1526, 1604, 1715, 1770). My count differs from the auditor's 22 only by scope of the table window and by including the non-DOI record eru-1770; the substantive claim — that the divergence set is an order of magnitude larger than the seven disclosed — holds.
>
> 5. CONVENTION contradiction confirmed. L-13(e) declares "the review dates a record by first publication (online-first or working paper), not by issue year", yet eru-0150 (Homm & Breitung) is labelled 2012 with online 2011-12-28 and store 2011, and eru-0348 (Sollis) is labelled 2016 with online 2015-05-28 and store 2015 — both labelled by issue year, contradicting the stated convention. Separately, eru-1112's store year (2021) is not the Crossref published-online year (2022), so L-13(e)'s premise that "the citation year is the Crossref published-online year" fails there too.
>
> 6. Auditor's own caveat verified: the 13 volume/issue/page rows in L-13(a) and the 3 pagination updates in (b) reproduce against my Crossref pull, so the defect is correctly scoped to the year field rather than overstated.
>
> No counter-evidence found. The defect claim stands.

### LITERATURE-2-1 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** misattributed-source / false recall claim
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:148-149 (abstract), :278-283 (§2.2), :294-295, :2367-2378 (L-5), :2610 (VG-4); docs/methodology/protocol_explosive-regime-review_2026-08-24.md:1003-1013 (A11); docs/literature/search_logs/explosive-regime/se-bc-01.json:79-92
> **issue:** The A11 backward-chase diagnostic reports `er-bc-2` (Banerjee, Chevillon & Kratz 2013, SSRN 2322360) as one of two "candidate additions" absent from the 1,996-record universe and "a record the frozen corpus does not contain", with eligibility "indeterminate at retrievable depth — no abstract is deposited at either platform". That is false. The same work is already in the universe, was dual-screened, and was excluded on a substantive criterion. The diagnostic's true yield is ONE candidate addition, not two, and the chase's DOI-or-normalised-title dedup rule failed against a same-work twin whose twin relation is recorded in the project's own stage-2 verdict log.
> **evidence:** (1) references_explosive-regime-dating.json:4436-4452 carries `eru-0209`, "Detecting and Forecasting Large Deviations and Bubbles WITH a Near-Explosive Random Coefficient Model", 2013 — the same 2013 work as er-bc-2 ("...IN a Near-Explosive Random Coefficient Model"); the one-word title difference is exactly why the normalised-title match missed it. (2) screen2-verdicts-R1.jsonl:73 — `{"id":"eru-0209","verdict":"EXCLUDE","criterion":"X7","note":"working-paper twin of eru-1027 (near-explosive random coefficient forecasting)"}`. (3) The published version is `eru-1027`, doi:10.1093/ectj/utaa004, Banerjee/Chevillon/Kratz, Econometrics Journal 2020 (store line 28029-28062) WITH a full deposited abstract describing the NERC model — screened INCLUDE-track at stage 1 by both screeners (screen-verdicts-R1.jsonl:1027, R2:1027) and excluded at stage 2 (screen2-verdicts-R1.jsonl:364, criterion S-c-fail, "NERC predictive-probability model (ESSEC WP twin); no null-referenced time-t decision"). (4) Crossref 10.2139/ssrn.2322360 confirms the 2013 preprint's authors/title; the EJ 2020 abstract (Crossref/OpenAlex) proposes the identical NERC model with the same three authors; corroborating source: academic.oup.com/ectj/article-abstract/23/2/297/5736054.
> **fix:** Correct §2.2, L-5, VG-4, the abstract and protocol amendment A11 to state that er-bc-2's work was already in the universe as `eru-0209`/`eru-1027`, was screened at both stages, and was excluded S-c-fail/X7 — so it is not a recall gap. Restate the diagnostic yield as one candidate addition (er-bc-1). Record as an A11 sub-note that the chase's DOI-or-normalised-title match is defeated by one-word title variants, which also bounds the reliability of the "177 referenced DOIs absent from the universe" figure.
> **reference:** https://doi.org/10.1093/ectj/utaa004 ; https://doi.org/10.2139/ssrn.2322360 ; docs/literature/search_logs/explosive-regime/screen2-verdicts-R1.jsonl

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted on four independent angles; all failed — the finding reproduces exactly.
>
> (1) Universe membership. docs/literature/search_logs/explosive-regime/screen-verdicts-R1.jsonl has exactly 1996 lines (the screened universe), and line 209 is eru-0209. The store record (docs/literature/references_explosive-regime-dating.json, block beginning "id": "eru-0209") is titled "Detecting and Forecasting Large Deviations and Bubbles WITH a Near-Explosive Random Coefficient Model", issued 2013, no DOI, s2_paper_id 0b2057876edebb2a0bc64d9983e9491436579fc7. So the work is in the 1,996-record universe.
>
> (2) Same-work identity — the angle most likely to break the finding, since eru-0209 carries no author list locally. Resolved the recorded S2 id against the live Semantic Scholar Graph API: paperId 0b2057876edebb2a0bc64d9983e9491436579fc7, title "...WITH a Near-Explosive Random Coefficient Model", year 2013, authors Anurag Banerjee and Guillaume Chevillon, full text at faculty.baruch.cuny.edu/jwang/seminarpapers/BCK_Bubbles.pdf ("BCK" = Banerjee/Chevillon/Kratz). Crossref 10.2139/ssrn.2322360 returns title "...IN a Near-Explosive Random Coefficient Model", posted 2013, first author "Anurag Narayan Banerjee". OpenAlex title.search over "Detecting and Forecasting Large Deviations and Bubbles" returns only three works — W3124094309 (doi 10.2139/ssrn.2322360), W1542349816 (doi 10.2139/ssrn.2337438), W4298243649 — all 2013, all authored Banerjee/Chevillon/Kratz, and no distinct "with a" work exists to which eru-0209 could instead belong. Same work, one-word title variant, confirmed.
>
> (3) Screening history. Reproduced verbatim: screen-verdicts-R1.jsonl:209 PROMOTE, screen-verdicts-R2.jsonl:209 PROMOTE (dual stage-1); screen2-verdicts-R1.jsonl:73 {"verdict":"EXCLUDE","criterion":"X7","note":"working-paper twin of eru-1027 (near-explosive random coefficient forecasting)"}; screen2-verdicts-R2.jsonl:201 X6. eru-1027 is in the store at line 28030 as Banerjee/Chevillon/Kratz, Econometrics Journal 2020, DOI 10.1093/ectj/utaa004, with a full deposited abstract proposing the NERC model, and screen2-verdicts-R1.jsonl:364 excludes it S-c-fail "NERC predictive-probability model (ESSEC WP twin); no null-referenced time-t decision". So the work was screened at both stages and excluded on substantive criteria, not missed.
>
> (4) Wording escape — could the artifacts be read as saying only "not in the frozen 72-record included set", which would be true? No. se-bc-01.json:60 declares "universe_compared_against: docs/literature/references_explosive-regime-dating.json (1,996 deduplicated candidate records); match on normalised DOI OR normalised title" and files er-bc-2 under "candidate_additions". lit_review ... :2366-2368 states "392 unique referenced DOIs, 177 absent from the 1,996-record universe, and 2 candidate additions surfaced". The absence claim is pinned to the 1,996-record universe, not the 72-record corpus, and is therefore false. Protocol A11 (protocol_explosive-regime-review_2026-08-24.md:999-1013) and VG-4 repeat "2 candidate additions" without qualification, and §2.2/L-5 label er-bc-2 a "named recall gap" with eligibility "indeterminate at retrievable depth".
>
> Dedup-failure mechanism confirmed: er-bc-2 carries DOI 10.2139/ssrn.2322360 while eru-0209 has no DOI, and the normalised titles differ solely by "in a" vs "with a", so the DOI-or-normalised-title rule could not match.
>
> Incidental (strengthens rather than refutes): se-bc-01.json's stated evidence for er-bc-2, "no abstract deposited at Crossref or OpenAlex", is also contradicted — Crossref 10.2139/ssrn.2322360 returns a full jats:p abstract describing the Near Explosive Random-Coefficient autoregressive model and the Case-Shiller application.
>
> No concrete counter-evidence obtained; the defect claim stands.

### LITERATURE-2-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** unverifiable-claim contradicted by primary source
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2151 (§9.5 row for eru-1289), :2560-2569 (L-16), :2616 (VG-10)
> **issue:** §9.5 (new, created by the QUANT-1-7 remediation) records the re-fetch of Cowles DP 2331 as "FAILED — cowles.yale.edu and elischolar.library.yale.edu returned HTML", and L-16/VG-10 conclude that §7.4's FWER triple "rest[s] on single-session transcription that cannot presently be re-opened". That conclusion is false: the DP 2331 PDF is served and downloadable from a stable cowles.yale.edu path. This matters because the FWER 0.55/0.78/0.93 triple is the single review datum the Rev 4 agenda now carries as a binding branch-3 condition.
> **evidence:** Fetched this round: https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf returned a 578 KB application/pdf (saved to the session tool-results directory). The Cowles listing and EliScholar mirror (elischolar.library.yale.edu/cgi/viewcontent.cgi?article=3690&context=cowles-discussion-paper-series) both resolve. Authorship independently confirmed: CFDP 2331, "Econometric Analysis of Asset Price Bubbles", Shuping Shi & Peter C. B. Phillips, 2022 (econpapers.repec.org/paper/cwlcwldpp/2331.htm). Contrast: korora.econ.yale.edu genuinely refuses connections (ECONNREFUSED 128.36.64.198:443), so the Phillips-reprint rows of §9.5 are corroborated — the eru-1289 row is not.
> **fix:** Re-fetch d2331_0.pdf at the direct file path, record its SHA-256 in the §9.5 table, mark the row OK, and downgrade VG-10/L-16 so they no longer assert that the FWER triple cannot be re-opened. If the numerals cannot be re-read this session, say "not re-collated", not "cannot presently be re-opened".
> **reference:** https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; the finding is corroborated on every checkable point.
>
> 1. Direct fetch reproduces. `curl -sSL https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf` returned http=200, content_type=application/pdf, size_download=591865 bytes (578 KB), no redirect (url_effective unchanged). File magic is %PDF-1.7. SHA-256 of the retrieved file: 309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e (saved to the session scratchpad as d2331_0.pdf). So the §9.5 eru-1289 cell "FAILED — cowles.yale.edu ... returned HTML" is contradicted at the direct file path.
>
> 2. Document identity confirmed from the file itself, not from a third party. Decompressing the first content stream yields the title page text: "Econometric Analysis of Asset Price Bubbles* Shuping Shi and Peter C. B. Phillips ... Macquarie University ... Yale University, University of Auckland, University of Southampton, Singapore Management University". This is CFDP 2331.
>
> 3. The load-bearing datum is not merely re-fetchable, it is re-collatable in this environment. Text extraction of the same PDF locates the source table verbatim: "Table 1: The familywise error rates of the PSY procedure  FWER/Sample Size  Quarterly Monthly Weekly  T=40 T=120 T=520  PSY(standard) 0.55 0.78 0.93  PSY(multiple) 0.04 0.06 0.05". The 0.55/0.78/0.93 triple that VG-10 and L-16 declare "cannot presently be re-opened" was re-opened and matched exactly, including its sample-size column headers.
>
> 4. The finding's own contrast claims also hold, so it is not a blanket-network artifact. korora.econ.yale.edu genuinely refuses: `curl https://korora.econ.yale.edu/phillips/pubs/art/p1349.pdf` → "curl: (7) Failed to connect to korora.econ.yale.edu port 443". The Phillips-reprint rows of §9.5 are therefore correct and only the eru-1289 row is wrong.
>
> The single partially-exculpatory observation is not a refutation: the EliScholar mirror path in the finding's evidence returns http=403 text/html (5486 bytes), so §9.5's clause about elischolar returning HTML is defensible for that route. That does not rescue the row's verdict or VG-10/L-16, because the primary cowles.yale.edu file path serves the PDF and the quoted numerals re-read correctly from it. The defect claim stands as stated: the conclusion that §7.4's FWER triple rests on transcription "that cannot presently be re-opened" is false.

### LITERATURE-2-4 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** incomplete check reported as complete
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2449-2458 (L-13 preamble), :2500-2508 (L-13(e)), :2620-2626 (§12.3 summary)
> **issue:** L-13 (the LITERATURE-1-4 remediation) asserts a complete 62/62 Crossref comparison "field by field on container title, volume, issue, page range AND YEAR", and closes the year dimension with a CONVENTION covering exactly seven records. Spot-verification defeats the completeness claim on the year field in two records and defeats the class statement in a third. The finding LITERATURE-1-4 was 'a partial check reported as complete'; the remediation reproduces it in narrower form.
> **evidence:** (1) `eru-1117`: L-13(e) states of all seven that "Crossref's published-print year is one later". Crossref 10.1093/jjfinec/nbab009 gives published-online [2021,5,5] and published-print [2023,1,19] — two years later, not one. (2) `eru-1715`: E1 citation (se-extraction-primary.jsonl:42) reads "Kurozumi E, Nishi M (2025)"; Crossref 10.1111/jtsa.12768 gives published-online 2024-09-27, published-print 2025-09. The record is dated by ISSUE year, contradicting the stated CONVENTION ("the review dates a record by first publication (online-first or working paper), not by issue year"), and the divergence is reported nowhere. (3) `eru-0150`: E1 (se-extraction-primary.jsonl:14) reads "Homm U, Breitung J (2012)"; Crossref 10.1093/jjfinec/nbr009 issues 2011 (online 2011-12-28), and the review's own §5.4 says the text extracted was the June 2009 Bonn working paper — a divergence in both directions, reported nowhere. Verified-correct rows (spot check): eru-0675, eru-0855, eru-1509, eru-1580, eru-0749, eru-1289, eru-1813, eru-1921, eru-0691, eru-1384, eru-1845, eru-1890 all match L-13 exactly against Crossref.
> **fix:** Either enumerate every year divergence in both directions across the 62 records, or restate L-13's scope as "container title, volume, issue and page range, plus the seven online-first/print year divergences listed", and drop the claim that the year field was checked completely. Correct the eru-1117 'one later' wording, and either re-date eru-1715 and eru-0150 to first publication or narrow the CONVENTION to what is actually applied.
> **reference:** https://api.crossref.org/works/10.1093/jjfinec/nbab009 ; https://api.crossref.org/works/10.1111/jtsa.12768 ; https://api.crossref.org/works/10.1093/jjfinec/nbr009

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; all three sub-claims reproduced independently against live Crossref and the repository's own extraction log.
>
> (1) eru-1117: se-extraction-primary.jsonl gives citation "Astill S, Harvey DI, Leybourne SJ, Taylor AMR, Zu Y (2021) ... doi:10.1093/jjfinec/nbab009". api.crossref.org/works/10.1093/jjfinec/nbab009 returns published-online date-parts [2021,5,5] and published-print [2023,1,19]. The print year is TWO later than the cited online year, so L-13(e)'s class statement at lit_review_explosive-regime-dating_2026-08-24.md:2500-2508 ("the citation year is the Crossref published-online year and Crossref's published-print year is one later", asserted over all seven of eru-0691, eru-1112, eru-1117, eru-1384, eru-1509, eru-1580, eru-1845) is false for eru-1117.
>
> (2) eru-1715: se-extraction-primary.jsonl line 42 and the review's own Section 5 corpus row 61 (line 797) both read "Kurozumi E, Nishi M (2025)". api.crossref.org/works/10.1111/jtsa.12768 returns published-online 2024-09-27, published-print [2025,9]. The record is dated by print/issue year, contradicting the CONVENTION stated in L-13(e) ("the review dates a record by first publication (online-first or working paper), not by issue year"). eru-1715 appears in L-13 table (a) at line 2474 for volume/issue/page only; the year divergence is reported nowhere, and eru-1715 is not among (e)'s seven.
>
> (3) eru-0150: se-extraction-primary.jsonl line 14 and Section 5 corpus row 2 (line 738) read "Homm U, Breitung J (2012)". api.crossref.org/works/10.1093/jjfinec/nbr009 returns published-online 2011-12-28, published-print [2012,1,1]. Dated by print year against the convention. Further, the review's own Section 5.4 (line 946) states "extraction was performed on the June 2009 University of Bonn working paper", so under the convention's own "online-first or working paper" clause the date should be 2009. Divergence in both directions; eru-0150 is not in (e)'s seven and no year note exists for it anywhere in L-13.
>
> Consequently the completeness assertion at lines 2449-2458 ("comparing ... field by field on container title, volume, issue, page range and year" over all 62 DOI-bearing records) and the restatement in Section 12.3 (lines 2620-2626, "a COMPLETE Crossref metadata cross-check ... surfaced 13 volume/issue/page discrepancies, 3 pagination updates and 1 version misattribution") are not supported on the year dimension: at least two year divergences (eru-1715, eru-0150) are unenumerated and one class statement (eru-1117) is factually wrong. The finding stands as stated, at the stated severity.

### LITERATURE-2-5 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** tool/method attribution contradicted within the artifact
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:362-368 (§2.5 "Honest compliance statement, as executed")
> **issue:** The QUANT-1-3 remediation reconciled the automation-tool identity per stage in the frontmatter, L-15, VG-11 and the §15 AI-assistance statement, and states the conflict is UNRESOLVABLE from the logs. §2.5 — the PRISMA 2020 item-8 compliance statement itself, i.e. the site where the automation tool is formally declared — was not updated and still asserts the identity as settled fact, and asserts the model the remediation concluded is NOT what the record carries.
> **evidence:** §2.5:363-364 reads: "Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5)." Against this: frontmatter `ai_assistance` (:41-51) declares screening as claude-fable-5; L-15 table (:2530) assigns screening to commit 8aeebfe trailer `claude-fable-5`; L-1 (:2315-2317) says "declared by the commit that carries their verdict files as `claude-fable-5`"; §15 table (:3071-3072) declares claude-fable-5; VG-11 (:2617) says the conflict "cannot be resolved from the logs".
> **fix:** Replace §2.5's parenthetical with the per-stage trailer declaration and a pointer to L-15/VG-11, so PRISMA item 8 is discharged on the same record as the rest of the document.
> **reference:** PRISMA 2020 item 8 (Page et al. 2021, doi:10.1136/bmj.n71)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; the defect claim reproduces exactly and is corroborated by the document's own remediation ledger.
>
> 1. Cited text reproduced verbatim. docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:362-364 reads: "**Honest compliance statement, as executed.** Screener A, screener B and the adjudicator are context-independent sessions of the *same* base model (claude-opus-5). Under PRISMA 2020 item 8 the model is the declared automation tool and the sole effective screener class." Stated as settled fact, with no hedge and no cross-reference.
>
> 2. Every contradicting site reproduces. Frontmatter ai_assistance (:40, :44-46) declares "the conflict cannot be resolved from the logs (12.1 L-15, 12.3 VG-11)" and assigns "stage-1 and stage-2 screening, both blind adjudications ... claude-fable-5". L-1 (:2315-2317) says the screening sessions are "declared by the commit that carries their verdict files as `claude-fable-5`". L-15 stage table (:2530) assigns screening/adjudication to commit 8aeebfe trailer `claude-fable-5 (role=multi)`. VG-11 (:2617) states the conflict "cannot be resolved from the logs". §15 table (:3071-3072) declares `claude-fable-5` for both screening rows.
>
> 3. §2.5 is the PRISMA item-8 site. Its own heading is "### 2.5 Selection process (item 8)" (line 344). It is ordinary authored prose, not a quoted, frozen, or as-of-registration block — I checked lines 300-362 for blockquote, fence, or frozen-text markers and found none. So the "preserved historical text" defense does not apply.
>
> 4. The document itself labels claude-opus-5 as the superseded declaration. L-15 (:2521): "This review as first delivered declared `claude-opus-5` as the base model for every stage. The repository's provenance trailers say otherwise for the stages that produced the verdict and extraction files." §15 (:3060) repeats it. §2.5:364 is therefore a residual instance of the exact statement the remediation retracted.
>
> 5. The remediation ledger confirms the omission by enumeration. §12.6 entry for QUANT-1-3 (:3121) lists the sites updated: "the frontmatter `ai_assistance` block, in new limitation L-15 (with the stage table) and in the §15 AI-assistance statement". §2.5 is absent from that list. Counter-check on sibling sites shows the reconciliation was propagated elsewhere — the abstract-level text at :136 carries "a conflict the logs cannot resolve (L-15, VG-11)", and the §12.4 conformance map item-8 row (:2643) carries the same pointer — which makes §2.5 the sole unreconciled occurrence rather than a stylistic choice.
>
> 6. No document-wide superseding disclaimer exists that would defuse §2.5. Grep for supersede/superseded returns only the protocol SHA-256 supersession (:11, :3023), unrelated to model identity.
>
> The only two remaining mentions of claude-opus-5 outside the explicitly-scoped synthesis rows are :48 and :364; :48 is correctly scoped to synthesis/remediation, :364 is not. Claim stands as stated.

### LITERATURE-2-6 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** claim attributed to the frozen protocol that the protocol does not make
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2020-2032 (§9.3, "Why this label and not `indeterminate-from-full-text`")
> **issue:** The REV-1-6 remediation's justification for keeping the definite `episode-statistic-null` token turns on a definition it attributes to the frozen protocol: "The protocol's verdict vocabulary contains `indeterminate-from-full-text` for the case where a full text was read and did not decide." The protocol states no such definition. It defines `assignment-null` and `episode-statistic-null` at length and then lists `mixed` and `indeterminate-from-full-text` as bare tokens. The load-bearing premise of the adjudication is therefore this document's own gloss presented as frozen text — and it is the gloss that excludes the version-mismatch case from the token.
> **evidence:** protocol_explosive-regime-review_2026-08-24.md:598-603 verbatim: "`assignment-null` — the stated null attaches to the state-assignment decision at time t (…); `episode-statistic-null` — the null governs statistics of completed/ex-post episodes; `mixed`; `indeterminate-from-full-text`." No gloss for the last two. Compounding: protocol §9.1(iv) (:650-651) names the adjudication target by DOI as "NB-13 — Baur & Lucey 2009 (doi:10.1016/j.jfs.2008.08.001)", and the review adjudicated IIIS DP 122 (2006) instead, extending by absence-of-evidence. The version difference is real and confirmed: the journal abstract verbatim reads "We propose a definition and a test for flight-to-quality, flight-from-quality and cross-asset contagion … eight developed countries including the US, the UK, Germany and Japan" (RePEc eee/finsta/v5y2009i4p339-352), which the review correctly reports is absent from DP 122.
> **fix:** Label the `indeterminate-from-full-text` gloss explicitly as a CONVENTION of this document (or append it as a numbered amendment), and state that the frozen protocol decides neither the version-mismatch case nor the meaning of the two undefined tokens. Keep the verdict if desired, but rest it on a disclosed convention rather than on attributed protocol text.
> **reference:** docs/methodology/protocol_explosive-regime-review_2026-08-24.md §9.1 lines 598-603, 650-662

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; the finding was corroborated on every checkable point.
>
> (1) Protocol text reproduced. docs/methodology/protocol_explosive-regime-review_2026-08-24.md:598-603 matches the auditor's quote verbatim: only `assignment-null` and `episode-statistic-null` are glossed; `mixed` and `indeterminate-from-full-text` are bare tokens. `grep -n "indeterminate"` over the entire protocol returns exactly ONE hit — line 603 — so there is no definition of the token anywhere else in the frozen document, and no protocol treatment of the version-mismatch case (grep for version/working-paper/twin/preprint returns only tier-admissibility and dedup-ledger material at lines 136-185, 427-430, 493, 949-956, none of which decides which version an adjudication attaches to).
>
> (2) Attribution reproduced. lit_review_explosive-regime-dating_2026-08-24.md:2020-2022 reads verbatim: "The protocol's verdict vocabulary contains `indeterminate-from-full-text` for the case where a full text was read and did not decide." The protocol makes no such statement.
>
> (3) Additional corroboration not cited by the auditor: the review's OWN §9.0 (lines 1856-1865), under the heading "Verdict vocabulary, fixed in protocol §9.1 before any of the three full texts was read", reproduces the last two entries as bare tokens with no gloss, exactly matching the protocol. The document thus shows at §9.0 that the protocol supplies no definition and then at §9.3 attributes one to it.
>
> (4) Load-bearing confirmed. The §9.3 rejection of the alternative token is "That is not this case: a full text **was** read and **did** decide" — a direct application of the invented gloss; removing the gloss leaves the adjudication without a premise. The gloss also performs the exclusion the auditor names: it narrows the token to "read but undecided", excluding "the DOI-named version was never read".
>
> (5) Compounding claim confirmed. Protocol §9.1(iv) (:650-651) names the target by DOI as "NB-13 — Baur & Lucey 2009 (doi:10.1016/j.jfs.2008.08.001)"; the review (:2005-2009) records "Version adjudicated: IIIS Discussion Paper No. 122 (March 2006)" and "The journal full text was NOT obtained". The RePEc abstract quote was not independently checked because the version difference is asserted by the review itself (:2033-2037) and is not a premise the finding requires.
>
> (6) No mitigating label exists. The review does mark conventions explicitly elsewhere ("CONVENTION (this document, §2.8)" at :429; amendment A7 at :397-402) and maintains an amendment register A4-A11, so the unlabelled gloss at §9.3 is a genuine gap in a document that otherwise marks such moves, not a formatting nicety.

### LITERATURE-2-7 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consumer document contradicts the source it transcribes; required disclosure omitted
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:751-755, :769
> **issue:** The Rev 4 residual paragraph — explicitly rewritten 2026-09-02 "after the Thread A audit round" — still states that the backward citation-chasing arm "never executed", which the SCOPE-1-4 remediation superseded on the same date, and carries no mention of er-bc-1 (Hall, Psaradakis & Sola 1999), the probable eligible miss the arm named and the corpus refused to admit. The spec's question (5) — whether refusing to admit a probable eligible miss needs its own disclosure — is answered in the negative by omission at the only site a downstream consumer reads. The same paragraph's amendment enumeration is stale.
> **evidence:** Agenda:751-755 "The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed…" versus review §2.2:255-289 and A11 (protocol:969-1016), which record the arm as executed 2026-09-02 with two named candidates and neither admitted. Agenda:769 "Amendments A4, A5 and A6 are post-hoc and labelled as such" versus the eight amendments A4–A11, all flagged post-hoc (protocol:822-1016; review §12.5:2694-2701). er-bc-1's identity independently verified: Hall, Psaradakis & Sola, "Detecting periodically collapsing bubbles: a Markov-switching unit root test", J. Applied Econometrics 14(2):143-154, 1999 (Crossref), OpenAlex abstract supports the S-a/S-b/S-c pass and the simulation claim the log asserts; it is genuinely absent from the 1,996-record universe.
> **fix:** Rewrite the antecedent-layer bullet: the arm ran post-freeze under A11 through publisher-deposited reference lists over 22 of 27 carriers; it named Hall, Psaradakis & Sola (1999) as a probable eligible pre-2011 antecedent that the frozen corpus does not contain and that was NOT admitted; pre-2011 coverage therefore rests on the known-item list plus one bounded, weakly-routed pass with a known, named miss. Correct "A4, A5 and A6" to A4–A11.
> **reference:** https://doi.org/10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted and failed; every claimed element reproduces verbatim in the working tree, and all three artifacts are co-present (agenda and protocol " M", review untracked-new), so the contradiction is live within one audit set.
>
> (1) Agenda:752 (bullet spanning 751-755) reads "The protocol's backward citation-chasing arm (`er-bc-*`, protocol §3.3) never executed, and three known-item antecedents ... were recovered by the known-item arm alone. Pre-2011 antecedent coverage therefore rests on the known-item list." The immediately preceding sentence at agenda:742-744 self-dates the paragraph: "Corrected and extended 2026-09-02 after the Thread A audit round (findings LITERATURE-1-6, SCOPE-1-6, REV-1-2); the Rev 4 text as first written under-bounded the corpus and is superseded here." The claim of staleness-despite-revision therefore holds on the document's own terms.
>
> (2) The superseding record exists in both consumer sources. Review §2.2 (lines ~245-289): "The arm has now been executed, after the corpus was frozen, and logged at ... se-bc-01.json under amendment A11", with "Carrier coverage 22 of 27", "Result: 2 candidate additions, 6 named near-misses", "`er-bc-1` Hall, Psaradakis & Sola (1999) ... which passes S-a/S-b/S-c on its deposited abstract and reports simulation evidence", and "Neither candidate is admitted, and the corpus stays at 72." Protocol A11 (lines 969-1016) records the same, including the DOI 10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X and the carriers eru-0463 / eru-0526 / eru-1509.
>
> (3) The omission claim holds. `grep -n "Psaradakis|er-bc|A11|A7|A8|A9|A10"` over the agenda returns exactly one hit, agenda:348, an unrelated URL fragment "A11n28.pdf". No mention of the arm's execution, of er-bc-1, or of the refusal to admit it appears anywhere in the agenda.
>
> (4) The stale enumeration reproduces. Agenda:769 "Amendments A4, A5 and A6 are post-hoc and labelled as such." Protocol headings show eight amendments, each carrying an explicit POST-HOC label: A4 (:822), A5 (:834), A6 (:844), A7 (:859), A8 (:885), A9 (:913), A10 (:938), A11 (:969). Review §12.5 (:2694-2701) tabulates the same A4-A11 with a post-hoc column set for all eight and states "three of the eight amendments record things that cannot be repaired by bookkeeping".
>
> The only counter-line I could construct — that the agenda paragraph names only LITERATURE-1-6 / SCOPE-1-6 / REV-1-2 and so was never scoped to SCOPE-1-4 — is a scoping quibble, not counter-evidence: the paragraph still asserts as of its own stated 2026-09-02 revision date a proposition the same-date remediation falsified, and agenda:769 is independently wrong regardless of which finding prompted the rewrite.

### LITERATURE-2-8 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** required transcription omitted from consumer
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:730-735, :133-147, :513-521
> **issue:** Review §14 item 3 instructs the consumer, in terms, to "Record also … the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)". Rev 4 records the three NB verdicts and NB-13's provisional status at three sites but records the A9/VG-9 audit-trail failure at none of them. The agenda therefore presents three adjudications as protocol-conformant when the review states that no dual-screening verdict citing a criterion identifier exists for any of them.
> **evidence:** Review §14:3005-3006 (the instruction); review §9.0:1873-1898, L-17:2571-2578, VG-9:2615 (the defect). Agenda:730-735 discharges the NB caveats and carries only the NB-13 version caveat; agenda:513-521 and :133-147 likewise. No occurrence of A9, VG-9, "force-screen" or "never entered" anywhere in the agenda.
> **fix:** Add to the NB bullet: all three adjudications rest on §9's full-text reading alone; protocol §9.1 required the three to be force-screened into the record universe and they never entered it, so no criterion-citing screening verdict exists for them (review A9, L-17, VG-9).
> **reference:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §14 item 3, §9.0, L-17, VG-9

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; the claim reproduces exactly. (1) Instruction verified: lit_review_explosive-regime-dating_2026-08-24.md §14 item 3 at lines 3005-3006 reads "Record also the NB-08 derivability note ... and the fact that none of the three ever entered the screened universe as protocol §9.1 required (A9, VG-9)." (2) Underlying defect verified in the review: §9.0 lines 1873-1898 state the three "are also not in the 1,996, and §9.1 required them to be (finding SCOPE-1-1)" and that "no screening verdict citing a criterion identifier exists for any of them, so the eligibility failures below rest on this section's full-text reading alone rather than on two screeners plus an adjudicator", recorded as amendment A9 and gap VG-9; L-17 at 2571-2578 repeats it ("the dual-screening audit trail the protocol requires for them does not exist"); the VG table row VG-9 at line 2615 lists it as major. Protocol protocol_explosive-regime-review_2026-08-24.md line 664 carries the force-screen clause and lines 915-917 confirm it was not executed. (3) Omission from the consumer verified by exhaustive grep of docs/research_notes/research_agenda_regime-classification_2026-08-21.md: zero occurrences of A9, VG-9, L-17, SCOPE-1-1, "force-screen", "never entered", "screened universe", "dual-screen", "screening verdict", "criterion identifier", "1,996", "4,898". (4) All NB sites enumerated by grep for NB-02|NB-08|NB-13: lines 14-15, 130-147, 513-521, 730-735 — each records the episode-statistic-null verdicts and the NB-13 provisional/REV-1-6 caveat only. (5) Checked the one plausible alternative location, the "Residual, carried openly" limitations block at lines 745-772: it cites VG-2/L-4, A6/L-2, REV-1-2 and A4/A5, but not A9/VG-9/L-17, so the audit-trail failure is absent from the agenda entirely.

### REPRODUCIBILITY-2-1 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** deps_pinned
> **location:** C:\Users\skoir\castles\pyproject.toml:10-40; repo root uv.lock (untracked)
> **issue:** No clone-durable environment specification exists for the runs that produced and remediated this review. pyproject declares every dependency unpinned (ruff, pytest, pandas, numpy, scipy, pandera, matplotlib ...) with no `==` and no version floors, and the only lock artifact, uv.lock, is UNTRACKED (it appears as `?? uv.lock` in git status and `git ls-files uv.lock` returns nothing). The pip-freeze archives that would substitute live under logs/reproducibility/env/, which .gitignore excludes (.gitignore:56). A fresh clone therefore resolves an arbitrary dependency set. Python version is correctly declared (requires-python >=3.11,<3.13) and matches the ReproLog host record (3.11.9), so the gap is package-level only.
> **evidence:** pyproject.toml dev/data/viz extras contain no version specifier except `jsonschema>=4.18`; `git ls-files uv.lock` empty; .gitignore lines 49/56 exclude artifacts/ and logs/ with only .gitkeep exceptions; logs/reproducibility/env/51760dc9....txt (172 pinned lines) exists locally but is not clone-visible.
> **fix:** Commit uv.lock (it is already generated), and state in the review's §15 provenance row that the environment is fixed by uv.lock at the delivering commit rather than by the gitignored pip-freeze archive. If uv.lock must stay untracked, copy the 172-line pinned freeze into a tracked path (e.g. docs/literature/search_logs/explosive-regime/se-env-freeze.txt) and cite its SHA-256.
> **reference:** none recorded

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; every factual claim reproduced exactly at the stated locations.
>
> 1. pyproject.toml (C:\Users\skoir\castles\pyproject.toml), lines 10-40: all three extras are unpinned. dev = ruff, pytest, pre-commit, nbstripout, nbqa, pyyaml, jsonschema>=4.18; data = pandas, numpy, scipy, pandera, pyarrow; viz = matplotlib, seaborn, great_tables. `jsonschema>=4.18` (line 20) is the sole version specifier in the entire file. No `==` anywhere.
>
> 2. `git ls-files uv.lock` returns empty; `git status --porcelain uv.lock` returns `?? uv.lock`. The file exists locally (208,360 bytes, mtime Aug 21 14:34) but is untracked. `git check-ignore -v uv.lock` exits rc=1 (not ignored — merely never added), which does not change the clone-durability conclusion.
>
> 3. `git ls-files | grep -Ei 'uv\.lock|requirements|freeze|env.*\.txt|constraints'` returns nothing: there is no tracked lock file, requirements file, constraints file, or freeze archive anywhere in the repository.
>
> 4. .gitignore line 49 = `artifacts/`, line 56 = `logs/`, with only `!logs/reproducibility/.gitkeep` (57) and `!logs/reproducibility/env/.gitkeep` (58) as exceptions. `git check-ignore -v logs/reproducibility/env/` confirms `.gitignore:56:logs/`. The freeze archive logs/reproducibility/env/51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e.txt exists locally and is exactly 172 lines, all `==`-pinned (aiohappyeyeballs==2.6.1, aiohttp==3.13.2, aiosignal==1.4.0, ...) — matching the finding's stated line count — and is not clone-visible.
>
> 5. requires-python = ">=3.11,<3.13" is present (line 5), so the finding's own carve-out that the Python-version declaration is correct also holds; the gap is package-level only, as claimed.
>
> 6. Counter-test for an alternative clone-durable carrier: the review's §15 provenance table (lit_review_explosive-regime-dating_2026-08-24.md, ~lines 3020-3040) enumerates protocol digest, search logs, candidate/included stores and their SHA-256, backward-chase log, ReproLog and sidecar (both explicitly labeled "untracked locator — logs/ is gitignored and does not resolve in a fresh clone"), git HEAD, and model identity. It contains NO row for the environment, no pip-freeze SHA-256, and no uv.lock reference. Commit trailers carry only Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance — the ReproLog itself is gitignored, so its env digest is unrecoverable from a clone. No substitute carrier exists.
>
> The only available counter-arguments are relevance/severity ones — e.g. that §15 declares "No simulation, no fitting, no critical value," so package versions may be inconsequential — which are explicitly excluded as refutation, and are in any case weakened by the review's own record of Python-executed work (SHA-256 digests, kappa recomputation, 62/62 Crossref cross-check, DOI/arXiv resolution). No concrete counter-evidence obtained.

### REPRODUCIBILITY-2-2 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** deps_pinned
> **location:** C:\Users\skoir\castles\logs\reproducibility\repro_log_f5419aa650e249378ff40828424696bb.json; review §15 row 'earlier-stage ReproLog'
> **issue:** The ReproLog for the stage that PRODUCED the frozen corpus (search, screening, extraction; commit 8aeebfe) has a vacuous environment and data record, and §15 cites it as an environment record while disclosing only its missing model field. Its pip_freeze_sha256 is e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 — the SHA-256 of the EMPTY STRING — and the referenced env file logs/reproducibility/env/e3b0c...txt is 0 bytes. Its config_resolved_sha256 is null and dataset_checksums is {}, so neither the protocol version nor the 1,996-record candidate store nor any verdict file is checksummed at the point of the run that created them. The corpus-producing stage is thus unpinned in environment and in data, and §15 names only the model-field defect (L-15/VG-11), not this one. The remediation-stage ReproLog (a0f236b3) is by contrast complete: 13 fields, non-empty freeze, dataset checksums that I verified byte-for-byte.
> **evidence:** repro_log_f5419aa6...json: {"config_resolved_sha256": null, "dataset_checksums": {}, "pip_freeze_sha256": "e3b0c442...b855"}; `ls -la logs/reproducibility/env/` shows e3b0c442...txt at 0 bytes; review §15 describes this log only as recording 'no model field'.
> **fix:** Add one sentence to the §15 earlier-stage ReproLog row and to VG-11: the 8aeebfe ReproLog carries an empty pip-freeze (digest = SHA-256 of the empty string), a null config digest and no dataset checksums, so the screening/extraction stage has no environment or input-state record; the corpus's input state is instead fixed retrospectively by the digests recorded in the 2026-09-02 sidecar and by commit 8aeebfe's tree.
> **reference:** none recorded

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted and failed — every component of the claim reproduces at the stated locations.
>
> 1. Log contents (C:\Users\skoir\castles\logs\reproducibility\repro_log_f5419aa650e249378ff40828424696bb.json): "config_resolved_sha256": null, "dataset_checksums": {}, "pip_freeze_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "model_hash": null, git_head 9deee0c (the parent of 8aeebfe, i.e. the pre-delivery HEAD).
>
> 2. Empty-string identity confirmed: `printf '' | sha256sum` returns e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 — identical to the recorded pip_freeze_sha256. `ls -la logs/reproducibility/env/` shows e3b0c44298fc...b855.txt at 0 bytes (the only other env file, 51760dc9....txt, is 3405 bytes and belongs to the 2026-09-02 runs).
>
> 3. Attribution to the corpus-producing commit confirmed: `git log 8aeebfe` carries `Repro-Log-Path: logs/reproducibility/repro_log_f5419aa650e249378ff40828424696bb.json` and `Repro-Log-SHA256: 7716edd8e6cdc0e81d84f624eda853f7474d096fe2c4c3598ffcd8d4e37bac7f`; `sha256sum` of the file returns that same digest. So this log is unambiguously the environment record for the search/screening/extraction stage.
>
> 4. Disclosure gap confirmed: line 3034 of docs/literature/lit_review_explosive-regime-dating_2026-08-24.md (the §15 'earlier-stage ReproLog' row) states only that "It records **no model field**, which is why the automation-tool identity cannot be resolved from the logs (L-15, VG-11)". A grep across the review, the protocol and the agenda for "freeze"/"pip freeze"/"env_id"/"dataset_checksum"/"config_resolved"/"unpinned" returns no mention anywhere of the empty pip-freeze, the null config digest, or the absent dataset checksums. VG-11 (line 2617) and L-15 (line 2519) likewise name only the model-identity conflict.
>
> 5. Counter-test for an alternative complete record for the same stage: I dumped every ReproLog in logs/reproducibility/. All four Aug-24 logs (35329773, 8584befb, 85f57228, 49510cf1) carry the same empty-string pip freeze and empty dataset_checksums; the only non-empty freeze (51760dc9) appears solely in the 2026-09-02 logs (28961af5, 8f5b02d3, a0f236b3). No log covering the corpus-producing stage pins environment or input state. The remediation log a0f236b3 does carry a 3405-byte freeze plus dataset checksums (references_explosive-regime.json = 8ed6f9ca..., se-bc-01.json = 3ea52681...), matching the finding's comparative claim.
>
> No plausible counter-reading survives: the defect claim is true as stated.

### REPRODUCIBILITY-2-3 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** llm_provenance
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md §15 (AI-assistance statement, 'what κ then measures'); logs\reproducibility\repro_log_a0f236b34b25417cb697df683198b3ef.json
> **issue:** The round-1 remediation of QUANT-1-3 is honest about model IDENTITY but silently leaves model CONFIGURATION unrecorded, and then leans on it. §15 now asserts κ = 0.433 'measures decoding-and-context variance of the screening model'. No temperature, top_p, max_tokens, thinking budget or session seed is recorded anywhere — not in er-screening-prompt.txt, not in any verdict JSONL, not in either ReproLog (grep over the whole search_logs tree returns only the word 'temperature' inside paper abstracts). A decoding-variance interpretation is unfalsifiable and the screening stage is not re-runnable to a comparable κ without those settings. Separately, the remediation run's own ReproLog still carries "model_hash": null, so the exact defect L-15/VG-11 names for the 2026-08 stages is reproduced for the 2026-09-02 stage; only the untracked sidecar carries ai_assistance = claude-opus-5, and sidecars are gitignored.
> **evidence:** grep -ril 'temperature|top_p|top-p' over docs/literature/search_logs/explosive-regime/ matches only records whose abstracts discuss physical temperature (se-crossref-07.json: 'temperature of long-lived ball lightning'); repro_log_a0f236b3...json line "model_hash": null; §15: 'κ = 0.433 compares two context-independent sessions ... so it measures decoding-and-context variance of the screening model'.
> **fix:** Either (a) record the decoding configuration of the screening sessions if it is recoverable from the dispatch record and add it to er-screening-prompt.txt's archival note, or (b) weaken the §15 sentence to 'measures between-session variance under an UNRECORDED decoding configuration' and add the missing sampling parameters to VG-11 as a named, unclosable gap. In both cases populate model_hash (or an equivalent model-id field) in the remediation ReproLog rather than leaving it null while the review criticises the same omission upstream.
> **reference:** none recorded

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; every claimed element reproduced. (1) §15 text confirmed verbatim at C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md lines 3081-3084: "**What κ then measures:** κ = 0.433 compares two context-independent sessions that sit in the same stage under the same trailer, so it measures decoding-and-context variance of the *screening* model." (2) Repo-wide search for a decoding configuration returns nothing. `grep -rilE 'temperature|top_p|max_tokens' --include=*.json --include=*.yaml --include=*.txt --include=*.md --include=*.toml` outside search_logs matched only docs/literature/references_explosive-regime-dating.json, whose hits are paper abstracts about physical temperature ("the fluid temperature effect might be misinterpreted as a kick migration"; "global temperatures ... forecasting"). Inside docs/literature/search_logs/explosive-regime/, the only hits are screen-verdicts-R1/R2.jsonl line 1464 ("explosive tests on temperatures; I2c unverifiable") and the word "seed" at er-screening-prompt.txt line 50, which refers to seed papers ("The forward-citation arms retrieved everything citing the two seed papers") and at verdict lines 131/393 ("KI-01 seed"). No temperature, top_p, top_k, max_tokens, thinking budget or session seed exists in er-screening-prompt.txt, any verdict JSONL, the frozen protocol docs/methodology/protocol_explosive-regime-review_2026-08-24.md, any ReproLog, or the sidecar. (3) C:\Users\skoir\castles\logs\reproducibility\repro_log_a0f236b34b25417cb697df683198b3ef.json contains "model_hash": null — reproduced verbatim; the same file's git_head is 27d74738aa35ec1cdf1ec6915b50532e3620ea6f. This is the identical defect the review criticises upstream: L-15 (line ~2537) states of repro_log_f5419aa650e2...json that "the 13-field ReproLog schema has `model_hash`, which is `null`, and no model-id field at all". (4) Only artifacts/runs/explosive-regime-dating/a0f236b34b25417cb697df683198b3ef/sidecar.json line 159 carries "ai_assistance": "claude-opus-5 (Claude Code / Claude Agent SDK), role=multi", and .gitignore line 49 is `artifacts/`, so that carrier is untracked, exactly as the finding states. VG-11 (line 2617) names only the model-identity conflict; it does not name missing sampling parameters, so the disclosure does not already cover the gap. The only remaining objection to the finding would be a plausibility argument about whether "decoding-and-context variance" is truly unfalsifiable, which is severity quibbling, not counter-evidence.

### REPRODUCIBILITY-2-4 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** data_hashed
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md §12.1 L-13 (lines ~2449-2490), §15 'identifier verification' row; docs\literature\search_logs\explosive-regime\ (no corresponding log)
> **issue:** The LITERATURE-1-4 remediation replaced a partial check with a complete one but archived no evidence for it. The 62/62 Crossref cross-check, the 62/62 DOI Handle re-resolution, the 2 arXiv and 1 Handle resolutions, and the §9.5 retrieval attempts produced NO machine-readable log, while the analogous post-freeze backward-chase arm executed the same day did get a full log (se-bc-01.json, with endpoints, per-carrier counts and all 177 referenced DOIs). The retrieved Crossref payloads were not retained, so the 13 discrepancies, 3 pagination updates, the version misattribution, the 1 unverifiable record and the 7 year-of-record CONVENTION cases are re-openable only by re-querying a mutable API — and Crossref records mutate, which is precisely why 13 of them diverged from the extraction citations in the first place. Protocol §4.1 and PRISMA-S treat retrieved metadata as logged evidence. Accuracy is not in question: I re-queried api.crossref.org for eru-0675 (10.1016/j.econmod.2018.07.021 → Economic Modelling 80:87-102, issued 2019), eru-1155 (10.6339/JDS.201707_15(3).0007 → 15(3):495-508) and eru-1580 (10.1111/jtsa.12784 → 46(5):846-866) and all three matched L-13's reported Crossref values exactly. The defect is provenance form, not content.
> **evidence:** `ls docs/literature/search_logs/explosive-regime/` (81 files) contains se-bc-01.json but no crossref-recheck or doicheck-2026-09-02 artifact; protocol-doicheck.json is the 2026-08-24 protocol-time file (25 DOIs). Sidecar records only aggregate counts: {"retrieved": 62, "failed": 0, "volume_issue_page_discrepancies": 13, ...}, and the sidecar is gitignored.
> **fix:** Write the per-DOI check results (DOI, queried date, retrieved container-title/volume/issue/page/issued, verdict) to a tracked log, e.g. docs/literature/search_logs/explosive-regime/se-crossref-recheck-01.json, add its SHA-256 to the sidecar's artifact_digests and cite it from L-13 and from §15's 'identifier verification' row, exactly as A11 does for se-bc-01.json.
> **reference:** none recorded

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted and failed; every claimed element reproduces exactly.
>
> 1. Directory census. `ls docs/literature/search_logs/explosive-regime/` returns 81 entries. `se-bc-01.json` is present; there is no crossref-recheck, doicheck-2026-09-02, or any equivalent artifact. The only *-doicheck* file is `protocol-doicheck.json`, whose header I read directly: `"date_executed": "2026-08-24"`, `"n_checked": 25`, `"executed_by": "Claude Fable 5"` — the protocol-time file, exactly as the finding states, covering 25 protocol-cited DOIs, not the 62 corpus DOIs.
>
> 2. No 2026-09-02 artifact other than se-bc-01.json. `grep -l "2026-09-02" .../explosive-regime/*.json*` matches se-bc-01.json ONLY. `ls --time-style=long-iso` shows se-bc-01.json as the sole file with a 2026-09-02 mtime. The twelve `se-crossref-*.json` files do hit api.crossref.org but are 2026-08-24 discovery queries (`se-crossref-01`: `date_executed: 2026-08-24`, `url=...works?query.bibliographic=sup+ADF+test...&rows=20`), not per-DOI `works/{DOI}` retrievals.
>
> 3. Nothing hidden in gitignored trees. `find artifacts -type f` returns exactly two sidecars plus two .gitkeep files; `ls -R logs/` shows only repro_log_*.json and env/*.txt. No per-DOI payload store exists anywhere in the repo.
>
> 4. Sidecar confirmed aggregate-only. Read `artifacts/runs/explosive-regime-dating/a0f236b34b25417cb697df683198b3ef/sidecar.json` (5111 bytes) in full. `computations.crossref_metadata_crosscheck` = {scope, endpoint, date, retrieved: 62, failed: 0, volume_issue_page_discrepancies: 13, pagination_updates: 3, version_misattribution: 1, inconclusive_no_crossref_pagination: 1, year_of_record_convention_divergences: 7} — nine scalars, zero per-DOI rows. There is no key at all for the 62/62 DOI Handle re-resolution, the 2 arXiv resolutions or the 1 Handle resolution. `artifact_digests` has three entries (store, protocol, se-bc-01.json) and no recheck log. The sidecar is under gitignored `artifacts/`.
>
> 5. Asymmetry with the peer arm confirmed. The sidecar's sibling computation `backward_citation_chase_er_bc` carries `"log": "docs/literature/search_logs/explosive-regime/se-bc-01.json"` and that file exists (43,545 bytes) and is cited from the review at lines 256, 2363, 2610, 2618, 2642, 2663, 3030, 3037, 3076, 3117, 3131 and from the protocol at line 984. The Crossref cross-check has no `log` key and no cited log anywhere.
>
> 6. Citation sites confirmed. §15's identifier-verification row (line 3036) reads in full: `| identifier verification | 62/62 DOIs responseCode 1 against the DOI Handle System; 2 arXiv IDs resolved against the arXiv API; 1 Handle responseCode 1 — all 2026-09-02 |` — no log path. §12.1 L-13 (lines ~2449-2515) narrates the check and tabulates 13 + 3 + 1 + 1 + 7 = 25 records in prose, citing no log; the remaining 37 clean records are not itemized anywhere, so for those there is no record of the retrieved values at all.
>
> 7. Protocol text checked, not misrepresented. Protocol §4.1 (Data management, 11a) opens "Raw responses per query_id under docs/literature/search_logs/explosive-regime/." Reading this as covering the recheck is a mild interpretive extension (a metadata recheck is not a "query_id" arm), but that affects only the finding's supporting rationale, not the defect: the review itself lists the 62/62 cross-check alongside the backward chase in §15 "computations performed by this review", and the backward chase got a full log while the cross-check got none.
>
> No basis for refutation was found. The defect claim — a reported complete check with no archived machine-readable evidence — is factually true as stated.

### REPRODUCIBILITY-2-5 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** entrypoint_runs
> **location:** C:\Users\skoir\castles\tests\ (empty), src\ (empty), CLAUDE.md Quickstart
> **issue:** No entrypoint re-derives any reported number. The Quickstart advertises `uv venv && uv sync; uv run pytest`, but tests/ and src/ contain no files (git ls-files returns nothing under either) and .venv/Lib/site-packages holds 3 entries, i.e. the project venv was never populated — the 172-package freeze recorded for the remediation run is the user's GLOBAL interpreter (it contains alpaca-py, astroid, asgiref and other packages absent from pyproject), not the project venv the reproducibility contract calls for. Every headline count in the round-1 remediation (31/13 D-cell divergences, 50 partial cells, 90/357 inter-pass divergence, 65/53 assessable denominators, I3 = 7, 62 DOI-bearing) was produced by throwaway code. I could re-derive all of them from the tracked logs — the D-rule column matches its Q cells in 576/576 domain cells across all 72 rows, § markers = 31 and ¶ markers = 13 exactly, partial cells = 50 with the exact per-question breakdown (Q1 2, Q2 3, Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29), divergence = 90 of 357, I3 failures = 7 with exactly 7 `I3 GAP` store notes — but only by writing that code from scratch, and a successor auditor gets no guarantee of the same parse (the §6 table uses escaped pipes inside I2 cells, which silently breaks naive column splitting).
> **evidence:** `ls -d tests src` shows both exist and are empty; `git ls-files data` returns only data/metadata/.gitkeep; logs/reproducibility/env/51760dc9....txt line 4 is `alpaca-py==0.43.2`, a package in no pyproject extra; my independent recount script reproduced 576/576 D-rule cells and the 90/357 and 50-cell counts.
> **fix:** Commit the recount as a test or script under tests/ or src/ (e.g. tests/test_erob_recount.py) that reads se-extraction-primary.jsonl + se-extraction-recheck.jsonl and the §6 table and asserts the published 31/13/50/90/357/65/53/7 figures, so `uv run pytest` becomes the review's reproduce target; and record the pip freeze from the project venv (uv run python -m pip freeze) rather than the global interpreter in the next ReproLog.
> **reference:** none recorded

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation on all four sub-claims; every one reproduced, so the defect stands.
>
> 1. No entrypoint exists. `ls -la tests/ src/` shows each contains only `.gitkeep` (0 bytes). `git ls-files tests src` returns exactly `src/.gitkeep` and `tests/.gitkeep`. I widened the search beyond the two stated dirs to look for any re-derivation code anywhere in the repo: `git ls-files | grep -iE '\.(py|sh|R|jl|ipynb)$'` returns ZERO tracked files of any executable type across the whole project, and the untracked `scripts/` dir contains only `scripts/.gitkeep`. With `[tool.pytest.ini_options] testpaths = ["tests"]` in pyproject.toml, the advertised `uv run pytest` collects nothing. The finding's phrasing "git ls-files returns nothing under either" is imprecise (it returns the two .gitkeep placeholders), but that is a wording nit, not a counter-fact — there is no code.
>
> 2. Project venv never populated. `ls .venv/Lib/site-packages` returns exactly 3 entries: `__pycache__`, `_virtualenv.pth`, `_virtualenv.py`. No pip, no pytest, no project deps.
>
> 3. The recorded freeze is not the project venv. `logs/reproducibility/env/51760dc96e6e....txt` is 172 lines; line 4 is `alpaca-py==0.43.2`, line 8 `asgiref==3.11.0`, line 9 `astroid==4.0.2`. I read pyproject.toml in full — its only extras are `dev` (ruff, pytest, pre-commit, nbstripout, nbqa, pyyaml, jsonschema), `data` (pandas, numpy, scipy, pandera, pyarrow), `viz` (matplotlib, seaborn, great_tables). None of alpaca-py / asgiref / astroid appears in any extra or in a transitive path plausible for them. A 172-package freeze is logically impossible from a 3-entry site-packages, so the freeze is demonstrably from a different (global) interpreter.
>
> 4. That freeze is the one bound to the remediation run. `logs/reproducibility/repro_log_a0f236b34b25417cb697df683198b3ef.json` carries `pip_freeze_path` and `pip_freeze_sha256` both equal to `51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e`, confirming the ReproLog for the round-1 remediation points at the global-interpreter freeze, not the project venv the CLAUDE.md reproducibility contract requires.
>
> No counter-evidence found. refuted=false.

## deferred-logged-minors

Fifteen minors logged, not remediated this round (`minors_logged: 15`); full
schema fields in the findings table above and verbatim in the JSON sidecar. The
twenty-one round-1 minors also remain open: none was shown by a round-2 finding
to be actually major, so they stay logged under the loop's standing rule, except
that round-1's REV-1-8 / QUANT-1-8 (the O6 denominator, logged minor in round 1)
is superseded by REV-2-2 / SCOPE-2-4 / QUANT-2-2, which are majors this round
because the REV-1-4 remediation was supposed to close that class and did not.

- **REV-2-8** (critical-reviewer; docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:128-130, 1902-1906) — The abstract's remediated NB sentence asserts that NB-02 was adjudicated "on the full text of the version at issue", but §9.1 records the adjudicated text as arXiv:cond-mat/0010050v2, the preprint twin of the Journal of Risk article the DOI identifies. The extension from preprint to journal version rests on a title/author/abstract/structure/table match — an absence-of-difference inference of the s …
- **REV-2-9** (critical-reviewer; docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3093-3095) — The new §16 change note misstates the round-1 audit's own configuration: it says "seven-branch" and then names four branches in the immediately following parenthesis, which matches the recorded round-1 routing (four branches, 33 agents). A provenance section that misdescribes the audit it documents undercuts the record it exists to create.
- **REV-2-10** (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:128-149) — The REV-1-6 propagation into Definitional basis (d) leads with a bolded, unqualified universal — all three candidates "adjudicated on full text" — and qualifies NB-13 only four lines later; a reader lifting the bolded sentence gets the unqualified form the finding was raised against. The NB-13 caveat is then stated twice in the same paragraph in near-identical terms, which obscures rather than rei …
- **REV-2-11** (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:531-536, 550-574) — Originality note. The Rev 4 remediation adds a branch-3 bullet presenting "admission of the surveillance/monitoring line" as a new consequence of the review, but the same branch already carries a Rev 2 bullet establishing the Frisén financial-surveillance school as the delay/ARL₀ canon and as the evaluation template for this branch. The nine records the review contributes are genuinely new; the st …
- **SCOPE-2-5** (scope-auditor; C:\Users\skoir\castles\docs\deliverables\deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:17-38) — Thread A items 1 and 2 are ticked `[x]` but their `check:` lines are left as the original prospective check text, with no recorded check output. Every other ticked item in the same spec (Thread B items, Thread C ADR, protocol, registration commit, search logs) records a dated 'PASSED 2026-09-02 —' line with per-item evidence. Satisfaction of the two Thread A deliverables is therefore asserted rath …
- **SCOPE-2-6** (scope-auditor; C:\Users\skoir\castles\docs\literature\lit_review_explosive-regime-dating_2026-08-24.md:3093-3095) — The change note describes the round-1 audit as 'A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check)', naming four branches while asserting seven. Seven is the loop's configured branch count, not the number routed; the round-1 record shows four branches routed. As written the sentence overstates the breadth of independent scrutiny the remediation rest …
- **QUANT-2-7** (quant-auditor; C:/Users/skoir/castles/docs/research_notes/research_agenda_regime-classification_2026-08-21.md:764-766) — The agenda describes the store as 'five carrying the I3 GAP note plus the twins eru-0154 and eru-0904'. That describes the pre-remediation store: all seven entries now carry an I3 GAP note, and the two twin notes additionally carry the twin-does-not-inherit rule. The count of seven is right; the description of the artifact is stale.
- **QUANT-2-8** (quant-auditor; C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3092-3096 (§16 change note)) — The change note misstates the audit it is responding to: 'A seven-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor, literature-check)' names four branches in its own parenthetical, and the round-1 record is four branches / 33 agents. The finding accounting in the same paragraph (27 raised, 3 refuted, 24 retained, 20 remediated here, 4 on the agenda) is correct and the remed …
- **QUANT-2-9** (quant-auditor; C:/Users/skoir/castles/docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1296-1300 (§7.2 coverage)) — The §7.2 coverage sentence does not exhaust its own denominator: 'reported in 15 of 65 (23%), partially in 8, and not at all in 41' accounts for 64 of 65 assessable records, silently dropping the one Q4 'unclear' cell. §7.3 and §7.4 enumerate all four response levels, so the omission is inconsistent within the review and slightly understates the not-clearly-reported class.
- **LITERATURE-2-3** (literature-check; docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2146-2151 (§9.5 rows for eru-0131/0393/0395), :2560-256 …) — §9.5 records only three hosts (korora.econ.yale.edu, cowles.yale.edu, elischolar) for the three Phillips texts and then concludes the §8.3 verdict "cannot presently be re-opened". Independently accessible full texts of the same work exist and were not attempted; round 1's refute gate already dropped LITERATURE-1-1 on precisely that ground, so the remediation re-introduces, in §9.5, the position th …
- **LITERATURE-2-9** (literature-check; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:763-766) — The agenda states seven I3 failures as "five carrying the I3 GAP note plus the twins `eru-0154` and `eru-0904`". The REV-1-2 remediation added `I3 GAP` notes to the two twins as well, so all seven now carry the note; the agenda describes the pre-remediation store.
- **LITERATURE-2-10** (literature-check; docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:735-808 (§5 corpus table), :2453-2456 (L-13)) — L-13 says the Crossref check compared "the extraction stage's E1 citation string (which §5 reproduces verbatim)". §5 does not reproduce E1 verbatim — it truncates the citation column mid-string, cutting DOIs, so the table's own identifiers do not resolve. §5.2 then declines to give a reference list on the ground that §5 "enumerate[s] them with full citations".
- **REPRODUCIBILITY-2-6** (reproducibility-verifier; C:\Users\skoir\castles\docs\literature\search_logs\explosive-regime\er-screening-prompt.txt:11,77) — The archived, frozen screening instrument hardcodes a machine-specific absolute Windows path: 'the registered systematic review at C:/Users/skoir/castles (working directory)' (both the stage-1 and stage-2 prompts). Re-running the screening instrument on any other machine requires editing the frozen prompt, which changes the instrument — the archived prompt is therefore not re-executable as archive …
- **REPRODUCIBILITY-2-7** (reproducibility-verifier; C:\Users\skoir\castles\docs\literature\search_logs\explosive-regime\se-bc-01.json (all_referenced_dois_not_in_universe e …) — The new backward-chase log stores lossily transcoded reference strings: U+FFFD replacement characters appear where the source had typographic quotes, e.g. the eru-1509 entry reads 'Blackburn, K., and M. Sola. 1996. �Market Fundamentals versus Speculative Bubbles...� International Journal of Finance & Economics 1: 303�17.' Since the 177-record 'not in universe' determination used normalised-title m …
- **REPRODUCIBILITY-2-8** (reproducibility-verifier; C:\Users\skoir\castles\data\_manifest.json (absent); CLAUDE.md §Reproducibility contract) — The project contract names data/_manifest.json as the dataset-provenance carrier with a CI `--check` drift mode; the file does not exist. The review's four datasets — the 1,996-record candidate store, the 72-record included store, the 81 files under search_logs/, and the four §9.5 primary texts — are hashed only inside the gitignored ReproLog and sidecar plus two prose rows in §15, so no tracked m …

These minors are deferred by protocol, not missed. Three of them (REV-2-9,
SCOPE-2-6, QUANT-2-8) name one defect — the §16 "seven-branch" description — and
two more (QUANT-2-7, LITERATURE-2-9) name a second, the agenda's stale
description of the I3 store; both are one-line edits that a remediation pass for
the majors can absorb at no extra cost.

## verification-of-remediations

This round exists to verify the 24 round-1 retained majors, all remediated by
the lead between rounds, and to hunt what those remediations introduced. **No
round-1 finding is re-raised as unremediated.** Every round-1 fix was located and
checked; where a fix holds, it is recorded as holding and produced no finding.
The round-2 majors are of two kinds: incomplete propagation of a fix to a site it
should have reached, and a new defect the fix itself created.

**Verified holding, no finding raised:**

- *REV-1-1 / SCOPE-1-2 (amendments not appended).* Amendments A4–A11 are present
  in the protocol addendum, each dated, stage-named, PRISMA-P-itemised and
  explicitly POST-HOC-flagged, and substantively accurate against the executed
  conduct. The frozen prefix is byte-identical: the first 51,478 bytes still hash
  to `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54` and the
  67,112-byte file to `0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b`,
  both re-derived independently by the reproducibility branch.
- *REV-1-3 / QUANT-1-2 (the Q-to-D rule).* The new rule-derived D column is
  mechanically correct in **576 of 576** domain cells over all 72 rows; the 31 `§`
  markers and 13 `¶` markers are each correctly placed with the legend's
  per-domain splits (D3 21 / D4 7 / D5 2 / D6 1 and D3 1 / D4 7 / D5 5) exact; the
  50 `partial` cells reproduce with the exact per-question breakdown and the
  90/357 inter-pass divergence. The remediation's claim that the round-1 audit
  named only the lenient direction, and that 13 cells run the other way, is
  accurate — three branches confirmed it independently.
- *REV-1-2 (I3 = seven, not five).* The count reconciles with the identifier
  tally (62 DOIs + 2 arXiv + 1 Handle = 65 of 72); the store carries exactly seven
  `I3 GAP` notes on the named ids, with the twin-does-not-inherit rule stated in
  the note text. Only the consumer agenda's *description* of the store is stale
  (minors QUANT-2-7, LITERATURE-2-9).
- *QUANT-1-4 (provenance).* The §15 ReproLog and sidecar digests reproduce
  byte-for-byte, git HEAD `27d74738` exists and is the pre-delivery commit, and
  both gitignored paths are correctly labelled untracked locators.
- *QUANT-1-5, LITERATURE-1-2, REV-1-5, SCOPE-1-1, SCOPE-1-3.* Each fix was located
  at every site its round-1 fix specification named and no branch raised against
  it: the "always upward" claim is corrected against the drift-break row; the
  `eru-1289` tier is re-tiered working-paper with the FWER claim's tier travelling
  with it; the abstract's limitations now carry the unexecuted-arm and eligibility
  disclosures; the three force-screen targets' non-entry is recorded as A9/VG-9 in
  the review; and the dual-extraction substitution is disclosed as a post-hoc
  conservative rule under A8.
- *The three round-1 refutations were not re-raised.* LITERATURE-1-1,
  LITERATURE-1-3 and LITERATURE-1-5 stand dropped; no branch produced new evidence
  defeating those refutations. LITERATURE-2-3 (minor) observes only that §9.5's
  new wording drifts back toward the position LITERATURE-1-1's refutation
  defeated, which is a statement about the new text, not a re-raise.

**Verified as fixed at the raised site but incompletely propagated** (each now a
round-2 major, against the propagation gap, not the original defect):

- *REV-1-4 (assessable denominators 65/53).* Correctly derived and correctly
  applied at §6.1, §7.2, §7.3, §7.4, §10.4 and the abstract. Two sites were
  missed — §7.6/O6 (REV-2-2, SCOPE-2-4, QUANT-2-2) and the 585 `partial`-cell
  denominator (REV-2-12, QUANT-2-1) — and at the first of them the missed
  propagation produces an arithmetically false sentence.
- *QUANT-1-3 (model identity).* The treatment in the frontmatter, L-15, VG-11 and
  §15 is honest and complete, and correctly refuses to resolve what the logs
  cannot. §2.5 — the PRISMA item-8 site — was not updated (REV-2-1,
  LITERATURE-2-5). The reproducibility branch adds that model *configuration*
  remains unrecorded while §15 now leans on it (REPRODUCIBILITY-2-3).
- *REV-1-13 (O4 corpus-scoping).* Correctly done at §7.4 and §7.8 on the O5
  template. The reading rule that governs §7 still says "the literature's
  coverage" (REV-2-5), §7.7 was not brought to the same standard (REV-2-6), and
  the scoping did not reach the consumer agenda (REV-2-7).
- *SCOPE-1-4 (backward-chase arm).* The arm was executed post-freeze under A11,
  the route deviation is declared at five sites, the coverage arithmetic
  reconciles (18 Crossref + 4 OpenAlex = 22 of 27), and refusing to admit
  `er-bc-1` into a frozen corpus is the right call — but one of the two named
  candidates was already in the universe and dual-screened (LITERATURE-2-1), the
  consequence of the bound is not attached at §7.7 (REV-2-6), and the agenda still
  says the arm "never executed" (SCOPE-2-1, QUANT-2-5, LITERATURE-2-7).
- *SCOPE-1-5 (I3/X7 as amendments).* A10(a)/(b) now record both deviations, but
  the twin assurance is false for the record-level tables (REV-2-3) and a fourth
  same-work pair, `eru-0198`/`eru-0259`, is documented in §5.4 and excluded from
  the declared drift (SCOPE-2-3).
- *QUANT-1-7 (unverifiable transcription).* §9.5 and §16 are new, accurate in
  structure, and correctly mark single-session transcription — but the
  un-refetchability claim itself does not hold for any of the four texts
  (QUANT-2-4, LITERATURE-2-2), and the page locators §9.5 exists to make
  re-openable are wrong in three of five spot checks (QUANT-2-3).
- *LITERATURE-1-4 (partial check reported as complete).* The 62/62 volume/issue/
  page reconciliation is real and was spot-verified live by three branches; the
  completeness claim fails on the year field (QUANT-2-6, LITERATURE-2-4) and the
  check archived no machine-readable evidence (REPRODUCIBILITY-2-4).
- *REV-1-6 (NB-13 provisional).* The reasoning is substantively correct — a full
  text was read and did decide under the pre-specified §9.1(iv) criterion, and the
  ambiguity is genuinely about which version the label attaches to — but the scope
  qualifier extends a frozen vocabulary with no amendment (REV-2-4) and its
  supporting gloss is attributed to protocol text that does not exist
  (LITERATURE-2-6).
- *REV-1-7 / QUANT-1-6 / LITERATURE-1-6 / SCOPE-1-6 (the agenda).* Rev 4 does now
  carry the FWER 0.55–0.93 condition, the surveillance-line comparators, TC-4, the
  280-record/47.8% completeness threat and the A6 convention-resolved appraisal
  caveat — all five confirmed present. What it does not carry is the disclosure
  set the review's §14 hands it: A9/VG-9, A7–A11 as post-hoc, the executed
  backward chase and its two named candidates, and point-of-claim corpus scoping
  (SCOPE-2-1, SCOPE-2-2, QUANT-2-5, LITERATURE-2-7, LITERATURE-2-8, REV-2-7).

**New this round, not traceable to a round-1 finding:** the five
reproducibility-verifier findings (REPRODUCIBILITY-2-1 through 2-5) address the
environment, data and entrypoint layer that round 1 did not route a branch to.
None touches a substantive verdict; all five are disclosure or archival repairs
that can be made without unfreezing the corpus.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Five specialist branches read four artifacts against the frozen
protocol, the deliverable spec, the primitive search logs and a subset of the
cited primary sources; they did not exhaustively verify every sentence, every
citation-claim pairing, every extracted numeral, every appraisal cell against its
source text, or every cross-artifact dependency. Absence of a finding is not
evidence of absence of a defect — the same asymmetry the charter enforces for
statistical nulls applies to this audit's own coverage. This round supplies its
own demonstrations: the page locators were wrong in **3 of 5** spot checks
(QUANT-2-3) and the year field failed in **12 of 19** unchecked divergences
(QUANT-2-6), both classes discovered only because a branch happened to re-open
the sources; the 62/62 Crossref check was re-sampled at 12 records, not re-run in
full; and one branch (scope-auditor) had no network or shell tool at all, so its
verification was documentary and it took the lead's hash claims as asserted.
Coverage of the *unexamined* remainder — roughly 56 unchecked §5 citation rows,
the 37 Crossref records L-13 does not itemise, and every quotation in §8 that no
branch could re-collate — is unknown.

**Per-branch residual risk** (full statements verbatim in the JSON sidecar):

- *critical-reviewer.* Round-1 remediations verified as holding, with the exceptions above. I independently recomputed the D-rule column for all 72 appraisal rows from the Q cells under protocol §6's domain-to-question map with A7's `partial` CONVENTION: all 72 eight-character strings are correct, all 31 `§` markers and all 13 `¶` markers are correctly placed, the per-domain splits in the legend (D3 21/D4 7/D5 2/D6 1 for `§`; D3 1/D4 7/D5 5 for `¶`) and the 22-no/unclear vs 9-partial breakdown are exact, and §6.1 tables (a) and (b) and the Q-distribution table reconcile cell-for-cell with the appraisal grid. The remediation's claim that the round-1 audit named only the lenient direction and that 13 cells run the other way is accurate. The seven-I3 count reconciles with the identifier tally (62 DOIs + 2 arXiv + 1 Handle = 65 of 72) and the store carries exactly 7 `I3 GAP` notes with the twin-does-not-inherit rule stated at all six sites. The 65/53 assessable denominators are correctly derived (72 − 3 twins − 4 no-full-text; − 12 recheck-only) and correctly applied at §6.1, §7.2, §7.3, §7.4, §10.4 and the abstract — but not at §7.6 (REV-2-2) or at the 585 `partial`-cell denominator (REV-2-12), which are the two propagation misses. I spot-verified four of the thirteen L-13 Crossref discrepancies against api.crossref.org (10.1111/sjpe.12179 → 66(1):139–153; 10.1111/jtsa.12784 → 46(5):846–866; 10.1093/jjfinec/nbab027 → 21(4):989–1063; 10.1111/jtsa.12845 → 46(5):829–845): all four match the L-13 Crossref column exactly, the online-first/print divergences match the (e) convention list, and the store carries 17 L-13 notes (13 + 3 + 1) as claimed. Amendments A4–A11 are dated, stage-named, PRISMA-P-itemised, post-hoc-flagged and substantively accurate against the executed conduct; §13 carries exactly 234 exclusion rows. On item (5): the backward-chase route deviation is adequately declared at five sites (§2.2, A11, L-5, VG-4, VG-12), refusing to admit `er-bc-1` post-freeze is the right call because admission would require re-screening a changed universe, and "bounded and named rather than closed" is accurate for the covered subset — but the bound's consequence is attached only at §7.4 and §7.8, not at §7.7, which is the claim most exposed to it (REV-2-6). On item (6): the NB-13 reasoning is substantively correct — a full text was read and did decide under §9.1(iv)'s pre-specified criterion, and the ambiguity is genuinely about which version the label attaches to — but the qualifier extends a frozen vocabulary without the amendment the review's own A7 precedent requires (REV-2-4). On item (8): the model-identity treatment is honest and complete in L-15/VG-11/§15, and correctly refuses to resolve what the logs cannot; it simply missed §2.5 (REV-2-1). On item (12): §9.5 and §16 are accurate, the three re-fetched digests are bound to first-page content checks, and the four unre-fetchable texts are correctly marked as single-session transcription with the load-bearing quotations named. RQI dimension 1 (importance): adequate — the review discharges a named, dated precondition of branch 3 and the question is worth asking. RQI dimension 2 (originality): covered by REV-2-11 and REV-2-6; the corpus enumeration and the ER-RoB profile are new, the O4 structural claim partly restates this project's own Rev 2 record. Residual risk not addressable by any edit: the whole appraisal remains convention-resolved rather than source-adjudicated (A6/L-2), the corpus remains frozen with two named probable misses outside it, 47.8% of full-text-stage records were never obtained, and the §8/§9 verdicts that carry the entire branch-3 precondition rest on single-session transcription from four texts that cannot presently be re-opened. Those are correctly disclosed and correctly refused repair; a consumer that carries them forward is the remaining exposure.

- *scope-auditor.* Verification here was documentary only: no network or shell tool was available to this branch, so the lead's hash claims (protocol frozen-prefix 33c01c5225…, full-file 0c961d3089…, store 8ed6f9ca…, ReproLog/sidecar digests, the three §9.5 content digests), the 62/62 Crossref cross-check underlying L-13, and the contents of se-bc-01.json, se-included-set.json and the verdict JSONLs were taken as asserted and not independently re-computed or spot-checked against Crossref. What was verified directly: the D-rule column derives correctly from the Q cells on a 12-row sample spanning dual, recheck-only, primary-only, no-full-text and twin rows; the § markers total 31 with the stated per-domain split (D3 21, D4 7, D5 2, D6 1) and the ¶ markers total 13 (D3 1, D4 7, D5 5), so the A8 claim about both directions holds as written; the 65/53 assessable denominators are applied consistently at §6.1, §7.2, §7.3, §7.4 and the abstract, the O6 site excepted (SCOPE-2-4); the included store holds 72 entries with exactly 7 `I3 GAP` notes; and the A4-A11 addendum entries are dated, stage-named, PRISMA-P-itemised and post-hoc-flagged in content, not merely present. The NB-13 'provisional-on-the-twin' reasoning and the A11 route-deviation disclosure are, on the documents, adequate and honest: the label stays inside the frozen vocabulary, the extension to the 2009 journal version is explicitly an absence-of-evidence inference, the refusal to admit er-bc-1/er-bc-2 is stated with its reason at the amendment, §2.2, L-5 and the abstract, and §2.2 correctly says the gap 'changes character but does not close'. The A11 entry's own phrase 'bounded recall gaps' is marginally stronger than the qualified §2.2 statement (22 of 27 carriers, deposited lists only) but is bounded in the body and was not raised. The residual exposure concentrated in the four findings above is that the agenda — the consumer artifact — is one remediation cycle behind the review it transcribes.

- *quant-auditor.* The round-1 remediations that could be mechanically verified all hold exactly — the D-rule column is correct on every one of the 72 rows with all 44 divergence markers correctly placed, the 31/13 and 22/9 splits, the 90/357 divergence and its per-question distribution, kappa and every §3.2 flow identity, the 7 I3 GAP notes, the 13/3/1/1 Crossref note classes (spot-checked live), the protocol prefix and full-file hashes, and the ReproLog, sidecar, store and NB-text digests all reproduce; what remains at risk is that the review's page-level citations and year metadata are demonstrably unreliable at a ~50% error rate in the spot-checks performed (quotes and numbers themselves verify verbatim), that the eru-1289 FWER triple is still the one genuinely unre-openable transcription, and that the consumer agenda lags the review's disclosure set so a downstream reader of the agenda alone would under-bound the corpus.

- *literature-check.* Citations checked this round: 30 distinct identifiers resolved against Crossref, OpenAlex, arXiv, RePEc or the publisher, plus 4 primary-text retrieval attempts. Everything I could pin held except where flagged. Specifically CONFIRMED accurate and not re-raised: PWY 2011 / PSY 2015a / PSY 2015b metadata (10.1111/j.1468-2354.2010.00625.x 52(1):201-226; 10.1111/iere.12132 56(4):1043-1078; 10.1111/iere.12131 56(4):1079-1134); NB-02 (10.21314/jor.2002.058, J. Risk 4(2):69-110, arXiv cond-mat/0010050v2 dated 25 Jul 2001, journal-ref matches); NB-08 (10.1017/jpr.2017.20, JAP 54(2):603-626); NB-13 (10.1016/j.jfs.2008.08.001, JFS 5(4):339-352, 2009) including the verbatim abstract sentence and the eight-country/Japan version caveat; all eight standards citations in §15 (PRISMA 2020, PRISMA-S, PRISMA-P 2015, Cohen 1960, QUADAS-2, PROBAST, Egger 1997, Frisen 2003); the eru-1289 authorship chain (CFDP 2331, Shi & Phillips 2022) and its DOI's 2025 CUP chapter pp.30-59; 12 of the L-13 discrepancy rows spot-verified exactly; the nine surveillance-line comparators' author/year/venue attributions; Bock-Andersson-Frisen 2007 and Moustakides-Polunchenko-Tartakovsky 2011 in the agenda; er-bc-1's identity and its OpenAlex abstract supporting the log's S-a/S-b/S-c reasoning; amendments A4-A11 are dated, stage-named, PRISMA-P-itemised and post-hoc-flagged as claimed. NOT verifiable this round and still open: every verbatim quotation, equation number and page locator in §8 (PWY/PSY) and §7.4's FWER numerals — the environment has no PDF text extraction, so although I retrieved the CFDP 2331 and HKIMR PDFs as binaries I could not read Table 1 or eq. (8). The review's own VG-10 covers this; LITERATURE-2-2 and 2-3 concern the accuracy of that gap's statement, not its existence. Also unverified: the completeness of the backward chase's 392/177 DOI counts (LITERATURE-2-1 shows the normalisation rule is defeated by one-word title variants, so 177 is an upper bound of unknown tightness); the 62/62 Crossref check was sampled at 12 records, not re-run in full. Round-1 refutations LITERATURE-1-1/1-3/1-5 were not re-raised; LITERATURE-2-3 notes only that §9.5's new wording drifts back toward the position 1-1's refutation defeated.

- *reproducibility-verifier.* Verified and NOT re-raised (round-1 fixes hold under independent re-derivation): (1) protocol prefix and full hashes reproduce exactly — first 51,478 bytes hash to 33c01c522521... and the 67,112-byte file to 0c961d3089..., and A4-A11 each carry an ISO date, an execution stage, PRISMA-P item numbers and an explicit POST-HOC flag, with A6/A7/A8/A9/A10 stating that the affected entries/decisions predate the entry; (2) I3 = 7 with exactly seven `I3 GAP` store notes on the named ids and the twin-does-not-inherit rule stated in the note text; the residual 3 non-DOI records (eru-1716, eru-1770 arXiv; eru-0198 Handle) are correctly counted as identified, giving 65; (3) the D-rule column is mechanically correct in 576 of 576 domain cells over all 72 rows, § markers total exactly 31 and ¶ markers exactly 13, and the 50 partial cells reproduce with the exact per-question breakdown and the 90/357 divergence; the round-1 audit's lenient-direction-only framing is defeated by the artifact itself; (5) route deviation is declared in both A11 and se-bc-01.json, coverage arithmetic reconciles (18 Crossref + 4 OpenAlex = 22 of 27, 5 named uncovered), and both candidates are genuinely absent from the 1,996-record universe by DOI and title — the non-admission is disclosed at the point of claim; (9) three sampled Crossref discrepancies re-verified live and matched L-13 exactly; ReproLog and sidecar digests cited in §15 reproduce byte-for-byte, git HEAD 27d74738 exists and is the pre-delivery commit. Residual risk concentrates in three places my findings name: nothing in a fresh clone pins the environment (unpinned pyproject + untracked uv.lock + gitignored freeze, and the corpus-producing stage's freeze is the empty string), the completeness claim that closed LITERATURE-1-4 has no archived evidence to re-open, and the decoding configuration behind the κ interpretation is unrecorded and now unrecoverable. None of these touches a substantive verdict; all three are disclosure/archival repairs that can be made without unfreezing the corpus. Unassessed by this branch: the substantive correctness of the NB-13 provisional-label reasoning, the coverage-fraction denominators' application site by site, and the agenda's non-overstatement, which fall to the critical-reviewer, quant and scope branches (I confirmed only that the agenda's Rev 4 text does carry the FWER 0.55-0.93 condition, the surveillance line, TC-4, the 280-record/47.8% threat and the A6 convention-resolved caveat).

**Residual risk not addressable by any edit**, and therefore carried forward
rather than remediated: the whole appraisal remains convention-resolved rather
than source-adjudicated (A6 / L-2); the corpus stays frozen at 72 with at least
one named probable-eligible record outside it (`er-bc-1`); 47.8% of
full-text-stage records — 280 of 586 — were never obtained and are not a random
sample of the literature; the §9.1 force-screening audit trail for NB-02/NB-08/
NB-13 does not exist and cannot be manufactured after the fact (A9); the
screening stage's decoding configuration is unrecorded and now unrecoverable, so
the κ = 0.433 interpretation is not falsifiable; and the corpus-producing stage
has no environment or input-state record (empty pip-freeze, null config digest,
no dataset checksums). These are correctly disclosed in the review and correctly
refused repair. The remaining exposure is a consumer that carries the review's
conclusions forward without them — which is precisely what the six
agenda-lagging findings above describe, and why they are majors rather than
minors.

## ai-assistance-statement

Per ICMJE Recommendations (updated January 2026) §V.A: AI cannot be an
author; AI assistance is disclosed here with the models used, their versions and
their roles.

- Models used: Claude Opus 5 (model id `claude-opus-5`, Anthropic, via Claude
  Code / Claude Agent SDK) — all branches: five specialist audit agents
  (critical-reviewer at high effort, scope-auditor at medium effort,
  quant-auditor at high effort, literature-check at high effort,
  reproducibility-verifier at medium effort, each with `model: inherit` in its
  agent definition), the adversarial refuter (high effort), and the
  trail-assembly agent that authored this round section.
- Roles: **audit** (findings; refutations; independent re-derivation of the
  D-rule column over 576 domain cells, the 31/13 divergence markers, the 50
  `partial` cells, the 90/357 inter-pass divergence, the assessable denominators,
  the seven `I3 GAP` notes, the protocol prefix and full-file digests, the
  ReproLog and sidecar digests; live retrieval and re-reading of primary sources
  and of api.crossref.org, OpenAlex, arXiv, the DOI Handle System and the
  Semantic Scholar Graph API) and **prose** (assembly of this trail). No authored
  research content; the audited artifacts were not modified by this round's
  agents.
- Note recorded rather than resolved, carried from round 1: QUANT-1-3 concerned a
  model-id conflict between the audited review's own declaration and the
  provenance trailers on the commits that produced its verdict files
  (`claude-fable-5`). Round 2 finds that conflict honestly stated in the review's
  L-15/VG-11/§15 and residually contradicted at §2.5 (REV-2-1, LITERATURE-2-5).
  That conflict is a property of the audited artifacts, not of this audit; the
  model id declared here is this audit's own.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the verdict and remediations proceed.
- Reproducibility log: ReproLog emission is sequenced with the
  `/commit-with-provenance` step; the log lands at
  `logs/reproducibility/repro_log_{run_id}.json` (gitignored, an untracked
  locator), and its clone-durable digest is carried by the commit's
  `Repro-Log-Path:` / `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility
  contract. The commit hash is to be recorded here as a dated addendum when it
  lands. REPRODUCIBILITY-2-1 and 2-2 note that this carrier does not pin the
  environment for a fresh clone; that finding is against the audited project's
  contract implementation, and it applies to this trail's own ReproLog too.

## immutability-and-retention

This round section and its JSON sidecar
([audit_trail_phase2-explosive-review_2026-08-24.round2.json](audit_trail_phase2-explosive-review_2026-08-24.round2.json),
SHA-256 `b62e57f063baf5f4c4a1a5d23c2d38ed246114ef8ecc912e53df3df50c26edba`, holding the round-2 payload verbatim per FAIR I1) are committed to
the repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. The round-1 front matter, findings
table, refute-gate dispositions, minors, verification section, residual-risk
statements, AI-assistance statement and retention note above this divider are
unmodified by this round; nothing in them was edited, overwritten or deleted, and
the round-1 sidecar remains byte-identical at its recorded digest
`221d4f241b04bba99af67097508e221eba9cc26207add417bd7bdb6bfd8d96ca`. A round 3, if
the lead opens one within the 3-round cap (`rounds_completed: 2`, `rounds_cap: 3`,
`cap_reached: false`), appends a further section below this one in the same form.
Corrections to any recorded entry — in either round — are appended as a dated
addendum that identifies what it corrects; prior entries are never edited.
Retention follows the repository's git history; the tracked file is the durable
record, and the round-2 front-matter digests bind this section to the exact
artifact states audited (HEAD `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`,
`worktree_clean: false`, the four artifact SHA-256 values listed above).

---

# Audit trail — Phase 2 explosive-regime review close-out, round 3 (cap)

Appended round section per 21 CFR 11.10(e): the round-1 and round-2 entries above
are unmodified. Round 3 is the **cap round** of this loop (`rounds_cap: 3`,
`cap_reached: true`); no round 4 exists, so everything retained here is surfaced
to the author as residual risk rather than routed to a further audit. It is a
verify-and-hunt round over the 30 round-2 retained majors — all 30 remediated
between rounds, 24 by the librarian in the review, store and protocol and 6 by
the lead in the agenda — and over what those remediations introduced. The same
five branches were routed as in round 2. All five branch verdicts:
**proceed-with-remediation**. Round verdict: **proceed-with-remediation**
(0 critical, 17 majors raised, **1 refuted and dropped at the gate**, 16 majors
retained for remediation, 16 minors logged, 0 retained-conservative).

The file-level YAML front matter at the top of this document is the round-1
record and is not edited; the round-3 front matter is carried verbatim in the
fenced block below (and, as JSON, in the round-3 sidecar).

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
title: "Audit trail — Phase 2 explosive-regime review close-out, round 3 (cap)"
type: audit_trail
date: "2026-08-24"
started_at: "2026-09-02T13:59:41-05:00"
ended_at: "2026-09-02T14:22:02-05:00"
artifacts:
  - {path: "docs/literature/lit_review_explosive-regime-dating_2026-08-24.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "86340644775039bd36bf1437c905fa467340da76abedc41345c5613a446f142a"}
  - {path: "docs/literature/references_explosive-regime.json", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "90979e895edce3d09d8757f6dfb2435cff99d74369d382c79df86aa2d58ca081"}
  - {path: "docs/methodology/protocol_explosive-regime-review_2026-08-24.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2"}
repo_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A. Item 1: the PRISMA 2020 review over the frozen 72-record corpus. Item 2: agenda rev 4 carrying the review's verdicts without overstating them. ROUND 3 — THIS IS THE CAP. No round 4 exists; whatever survives this round is surfaced to the author as residual risk, so calibrate severity accordingly and do not inflate. VERIFY THE ROUND-2 REMEDIATIONS AND HUNT WHAT THEY INTRODUCED. Round 2 raised 30 major findings and the refute gate dropped NONE. All 30 are now remediated — 24 by the librarian in the review/store/protocol, 6 by the lead in the agenda. Do NOT re-raise a round-1 or round-2 finding that is genuinely fixed. Claims to verify: (1) LITERATURE-2-1 was CONFIRMED against the remediation's own earlier claim — er-bc-2 IS in the universe as eru-0209 (stage-2 X7, twin of eru-1027, DOI 10.1093/ectj/utaa004); the A11 dedup test missed it because the SSRN DOI is absent from the store and the normalised titles differ by one word ('in a' versus 'with a'). Backward-chase yield restated from two candidates to ONE (er-bc-1 Hall/Psaradakis/Sola 1999), and the '177 absent from the universe' figure rebounded as an upper bound. Verify the correction propagated everywhere and that the upper-bound framing is right. (2) LITERATURE-2-2/QUANT-2-4: the round-1 un-refetchability claim was FALSE — korora.econ.yale.edu refuses TCP on 443 but serves all three Phillips Cowles reprints over plain HTTP on 80, and Cowles DP 2331 fetched fine from cowles.yale.edu. All four now have content digests. L-16 narrowed and VG-10 downgraded major to minor. Verify the digests and that the two residues kept are correctly stated: no extraction-time digest exists so version identity between the 2026-08 extraction and the 2026-09 refetch is unprovable, and the three NB texts were refetched but NOT re-read so their locators remain unverified. That second residue matters because re-reading section 8 found 14 locator errors — assess whether leaving the section 9 NB locators unverified is now an acceptable residual or a live defect. (3) QUANT-2-3: 14 page locators corrected across PWY 2011, PSY 2015a, PSY 2015b and eru-1289, recorded in new limitation L-18, and NOT a uniform offset (several locators were already correct). Spot-verify a sample against the retrieved reprints. The lead has separately corrected five locators in the agenda: PSY 56:1053 (was 1054) at three sites, PWY 52:214 (was 215), PWY Table 1 note p.213 (was 214), PSY Table 1 note p.1050 (was 1051), PWY divergence convention p.207 (was 208). Verify those five agenda corrections are right and complete. (4) Three defects the re-read found that no auditor had raised: section 8.1 quotation-marked a paraphrase; section 7.4's FWER table row 2 was labelled 'longer span' when DP 2331 section 5.2 fixes a 10-year span for all three cells with only frequency varying (T = 40/120/520); section 8.2's E9 paired two unrelated Table 2 cells and omitted the maximum GSADF 0.787 at k=6, T=100. Verify all three corrections against the sources. (5) The O6 denominator was set to 63 distinct works (69 minus 4 NE minus 2 NS), giving 22/63 = 35% 'just over one in three', with the false 'fewer than one in three' deleted. Verify the arithmetic and that both sites now agree. (6) QUANT-2-6/LITERATURE-2-4: the year check found 19 online/print divergences not 7, and found the declared date-by-first-publication CONVENTION contradicted by the review's own labels in 12 of the 19; L-13's completeness claim narrowed to container title, volume, issue and page range. Verify. (7) SCOPE-2-3: a FOURTH probable twin pair (eru-0198/eru-0259) is disclosed as unresolved with both distinct-work counts given (69-or-68) rather than adjudicated either way, on the ground that the journal text was never obtained. Adjudicate whether that refusal is right or whether it dodges a decision. (8) Amendments A12 and A13 appended; frozen prefix must still hash to 33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54 over the first 51478 bytes and the full file to 92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2. (9) The agenda: verify the lead's six round-2 fixes hold — the backward-chase arm's post-freeze A11 status with er-bc-1 named as an unadmitted probable eligible miss, the A9/VG-9 disclosure that none of the three NB records ever entered the screened universe, A4-A6 corrected to A4-A11, the O4 claim corpus-scoped at the point of claim, and the surveillance-line bullet bounded the same way. (10) Three REPOSITORY-LEVEL gaps are recorded as VG-14/15/16 and deliberately NOT repaired: unpinned pyproject with untracked uv.lock, a vacuous corpus-producing ReproLog, and no entrypoint that re-derives any reported number. Confirm they are correctly scoped as repository-level rather than review-level, and do not raise them as review defects.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md", sha256: "6425f053ce0e3dfd0554d7a103f3f65b76fdd46b95f4c4df6b5147eafd30e17d"}
    - {path: "docs/methodology/protocol_explosive-regime-review_2026-08-24.md", sha256: "92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill). Round 3 is the cap round: each round-2 remediation was re-derived independently where mechanically checkable, every new critical/major finding passed the refute gate, and severity was calibrated against the fact that survivors are surfaced to the author rather than re-audited."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "quant-auditor", agent_def_path: "~/.claude/agents/quant-auditor.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "reproducibility-verifier", agent_def_path: "~/.claude/agents/reproducibility-verifier.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-opus-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Opus 5, claude-opus-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, quant-auditor, literature-check, reproducibility-verifier) → adversarial refuter → trail-assembly agent (this round section)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. Five branches routed, the same set as round 2, over the same four artifacts: critical-reviewer (adequacy of the 30 remediations, interpretation and RQI dimensions) high; scope-auditor (declared-spec coverage and consumer-artifact fidelity, plus adjudication of the two judgement calls the brief put to it) medium; quant-auditor (independent re-derivation of the flow identities, denominators, D-rule split, content digests and the corrected page locators against retrieved primary texts) high; literature-check (primary-source and identifier re-verification, the fourth twin pair's work identity, the L-18 correction record) high; reproducibility-verifier (protocol frozen-prefix and full-file digests, store and search-log digests, ReproLog and sidecar currency, and the repository-level VG-14/15/16 claims) medium. epi-auditor was not routed (no population-health artifact, no human-subjects data)."
rounds_completed: 3
rounds_cap: 3
cap_reached: true
verdict: "proceed-with-remediation"
counts: {raw_critical: 0, raw_major: 17, raw_minor: 16, refuted: 1, retained_conservative: 0, to_remediate: 16, minors_logged: 16}
sidecar: {path: "docs/audits/audit_trail_phase2-explosive-review_2026-08-24.round3.json", sha256: "92e803db1464b1dbac990f125007d524c0f721dbbe46a1664ab8edadb90ecd00"}
```

Notes on the round-3 record. `started_at`/`ended_at` are the trail-assembly
interval for this round section. All four audited artifacts moved between rounds
— the review from `40bc4ae3…` to `86340644…`, the included-corpus store from
`8ed6f9ca…` to `13c76d8f…`, the agenda from `2ad84ee0…` to `90979e89…`, and the
frozen protocol from `0c961d30…` to `92fff3f2…` because the round-2 remediation
appended amendments A12 and A13 to its append-only addendum. The two protocol
digest claims the brief asked to be checked were **independently recomputed for
this trail and both reproduce exactly**: `head -c 51478` of the protocol hashes
to `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54` (the
registration digest at commit `9deee0c`), and the whole file hashes to
`92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2` — so the
frozen text above the addendum is byte-identical to the registered protocol.
The deliverable spec is unchanged from its round-2 state (`6425f053…`).
`repo_head` is unchanged at `27d74738…`: the remediation and the audited
artifacts are in the worktree and not yet committed, so `worktree_clean: false`
(`git status --porcelain` is non-empty). The round-3 sidecar is a separate
sibling file so that the round-1 and round-2 sidecars, whose digests are bound
into the front matter above, remain byte-identical, per append-only retention.
Following this round's own finding REPRODUCIBILITY-3-2, the sidecar was written
with LF line endings so that its recorded SHA-256 survives `git add` under
`.gitattributes`' `*.json text eol=lf` rule and is reproducible from a clone.

## findings-table

Round 3 raised zero critical findings, 17 majors and 16 minors. The counts
object, verbatim from the round payload: raw_critical 0, raw_major 17,
raw_minor 16, refuted 1, retained_conservative 0, to_remediate 16,
minors_logged 16. One row per finding — all eight schema fields (id, severity,
category, location, issue, evidence, fix, reference) plus branch and disposition;
issue, evidence, fix, location and reference are compressed for tabular
legibility, and the full unabridged text of every finding, every refutation and
every per-branch residual-risk statement is held in the JSON sidecar. Majors
appear first in disposition order, then the 16 logged minors. Convergent clusters
(one defect, several branches) are noted after the table.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-3-1 | major | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787 | The round-2 withdrawal of `er-bc-2` (LITERATURE-2-1 / protocol A12(b)) did NOT propagate to the consumer agenda. The agenda's Verification-status residual still reports the post-freeze backward-chase arm as naming TWO records the frozen corpus does not contain, and still describes `er-bc-2` as having indeterminate eligibility. T … | It named **two candidates the frozen corpus does not contain, neither admitted**: - `er-bc-1` **Hall, Psaradakis & Sola 1999**, … - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indetermina … | Replace the bullet pair with the corrected single-record form from review §14 item 7: the A11 diagnostic named ONE record the corpus does not contain (`er-bc-1`, a probable eligible miss on the pre-20 … | CHAMP item 30 (conclusions limited to what the analysis supports); PRISMA 2020 item 24c (amendments); review §2.2, §14 item 7, pro … | critical-reviewer | retained — remediate |
| REV-3-2 | major | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-814 | The agenda's amendment enumeration was corrected in round 2 from 'A4-A6' to 'A4-A11', but the same round-2 pass appended A12 and A13 to the protocol addendum. The agenda's list is therefore stale again, and the two omitted entries are precisely the ones that correct claims the agenda repeats verbatim: A12(b) withdraws `er-bc-2` … | three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works. Recorded as findings; the corpus was **not** re-screened. - **Amendments A4–A11 are all post-hoc** (corrected … | Restate as 'Amendments A4-A13 are all post-hoc' and add A12 and A13 to the substantive list with one clause each: A12 — corrections to A7's `partial` denominator (585 -> 561) and A11's yield (2 candid … | PRISMA 2020 item 24c; CHAMP item 6 (consistency with the frozen protocol); protocol amendments A12, A13 | critical-reviewer | retained — remediate |
| REV-3-3 | major | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1569,1571,1577 (§7.3); :1899 (§7.8); :2636 (§ … | The round-2 re-read established that DP 2331's 7.56 and 12.20 are the MEAN BIAS in the estimated origination date at successful-detection rates 0.84 and 0.75, reported in Table 2 p.21 — and corrected §7.4, §9.5, §14 and L-18 accordingly. Four other sites were left on the uncorrected label. §7.3 calls them 'PSY origination delay' … | \| PSY origination delay, standard per-observation CVs \| 7.56 months (4.99) \| monthly, 10-year span, M = 2,000 \| `eru-1289` Table 1, [Shi & Phillips 2022] … controlling the family-wise error rate of th … | Propagate the L-18 correction to all four sites. In §7.3 relabel the two rows 'PSY mean origination-date bias' with 'at successful-detection rate 0.84' / '0.75' in the design column, and change the so … | CHAMP items 17, 19 (data described adequately and correctly; individual results with their source); SAMPL general principles (nume … | critical-reviewer | retained — remediate |
| REV-3-4 | major | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1601-1605 (§7.3) | The round-1 tier correction (LITERATURE-1-2, L-10) re-tiered `eru-1289` to WORKING-PAPER and stated that the tier 'travels with the claim … wherever it is used', then enumerated the sites: 'here, in the abstract's principal finding (4), in §7.8, and in §14's inputs'. §7.3 is not in that enumeration, and §7.3 is the section that … | **The single most consumer-relevant number in the corpus** is the `eru-1289` pair … Evidence tier: peer-reviewed throughout. | Change §7.3's tier line to 'Evidence tier: peer-reviewed except the four `eru-1289` rows, which are WORKING-PAPER tier — the 2025 CUP chapter carrying that record's DOI was never obtained and the extr … | CHAMP items 19, 22 (individual results and certainty reported with their evidence status); charter rule that evidence tier travels … | critical-reviewer | retained — remediate |
| REV-3-5 | major | verification-gap | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3174 (VG-10); :2472-2478, :2494-2500 (§9.5) | VG-10 was downgraded major -> minor on the strength of the Phillips re-read, then had a second, unlike residue folded into it: the three §9 NB texts were re-fetched but NOT re-read, so §9.1-§9.3's QUOTATIONS as well as their page locators remain single-session transcriptions. The review states in its own words that this is 'exac … | \| **VG-10** \| **minor** (downgraded from major, and re-scoped to §9's NB texts) \| … **The three §9 NB texts were re-fetched but not re-read**, so their quotations and locators are still single-session … | Split the gap. Keep VG-10 at `minor` for the version-identity residue alone (no extraction-time digest, so 2026-08 and 2026-09 files cannot be proved identical). Open a separate `major` gap — the §9 N … | CHAMP item 29 (methodological limitations discussed appropriately); CHAMP response scale — Unclear maps to major, never to accept; … | critical-reviewer | retained — remediate |
| REV-3-6 | major | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1420-1428, :1450-1460 (§7.1); :1898 (§7.8) | The round-2 re-read of PSY 2015a Table 2 established that the table's maximum size is GSADF 0.787 at fixed lag k = 6, T = 100 — under the stated null DGP, with only the fitted lag order changed. That number was recorded at §8.2's E9 cell and in L-18, and nowhere else. §7.1, the section that IS the O1 synthesis, reports from the … | **Synthesis claim (O1).** *The recursive right-tailed family's near-nominal size is a property of its stated null, not of the family.* Every departure from `iid errors + constant unconditional varianc … | Add a row to §7.1's first table: 'GSADF, lag overspecification \| up to 0.787 at 5% (fixed k = 6, T = 100); 0.697 under significance-test kmax = 6, with SADF 0.145 \| same null DGP, lag order varied \| ` … | CHAMP item 20 (no selective reporting of analyses); SAMPL — report the analysis as performed, including the least favourable cells … | critical-reviewer | retained — remediate |
| SCOPE-3-1 | major | partial | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787 | The round-2 er-bc-2 retraction was remediated in the review but NOT propagated to the agenda, and the review explicitly handed that propagation to the lead. The agenda's residual still states the A11 backward-chase arm "named two candidates the frozen corpus does not contain, neither admitted" and lists `er-bc-2` Banerjee, Chevi … | Agenda l.779-787: "It named **two candidates the frozen corpus does not contain, neither admitted**: - `er-bc-1` **Hall, Psaradakis & Sola 1999** … - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligi … | Rewrite the agenda bullet to "It named ONE record the frozen corpus does not contain, not admitted: er-bc-1 …", delete the er-bc-2 sub-bullet or restate it as a withdrawn false positive present in the … | deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A item 2 ("Branch 3 integrates the review's verdicts"); review § … | scope-auditor | retained — remediate |
| QUANT-3-1 | major | reporting | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:777-787 | The withdrawn er-bc-2 claim survives in the consumer agenda. The review withdrew it as FALSE (LITERATURE-2-1, A12(b), VG-4) and §14 item 7 says explicitly it "must not be transcribed as a recall gap"; the lead's round-2 agenda pass rewrote the surrounding bullet (post-freeze A11 status, er-bc-1 as a probable eligible miss) but l … | Agenda: "It named **two candidates the frozen corpus does not contain, neither admitted**: … - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited." Verified … | Replace the bullet's lead with "It named ONE candidate the frozen corpus does not contain"; delete the er-bc-2 sub-bullet and replace it with the withdrawal plus the instrument bound ("absent by DOI o … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §2.2, §14 item 7; docs/methodology/protocol_explosive-regime-revi … | quant-auditor | retained — remediate |
| QUANT-3-3 | major | numerical | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1573-1578 (§7.3 evidence table, eru-1289 rows … | §7.3 attributes the 7.56 / 0.79 / 12.20 / 0.77-month figures to `eru-1289` **Table 1**. They are in Table 2 (DP 2331, p.21); Table 1 is the FWER table (0.55/0.78/0.93, p.20). §7.4 and §14 item 2 cite Table 2 correctly, so the review contradicts itself, and the wrong attribution sits on what §7.3 itself calls "the single most con … | Retrieved d2331_0.pdf (sha256 309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e, matches §9.5). Printed p.20 carries "Table 1: The family wise error rates of the PSY procedure … PSY (st … | Change the four `eru-1289` source cells in §7.3 from "Table 1" to "Table 2 p.21", and add §7.3 to the site list in §9.5 and L-18. | Shi & Phillips, Cowles Foundation Discussion Paper 2331 (2022), Tables 1–2, pp.20–21 | quant-auditor | retained — remediate |
| QUANT-3-4 | major | verification-gap | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2147-2185 (§9.1); §9.5 "What is still not est … | VG-10's retained residue — "the three NB texts were re-fetched but NOT re-read, so their locators remain unverified" — is not a neutral residual: on re-read NB-02's locators are demonstrably wrong. I re-read all three. NB-08 and NB-13 verify exactly; NB-02 has three wrong page attributions in the section that carries the branch- … | Retrieved nb02.pdf (sha256 d8ae7e69dce54dc97a3b014f4865ad263a0cf4d2d6a75fa8476214d3bc12973f, matches §9.5). Printed folios: pdf p3=1, p4=2, p11=9, p12=10. (a) "we shall take the stretched exponential … | Correct the three NB-02 locators in §9.1 (p.1→p.2; p.8→p.9 twice), add them to L-18's table, and narrow VG-10 to record that the NB re-read has now been done with NB-02 failing and NB-08/NB-13 passing … | arXiv:cond-mat/0010050v2 (Johansen & Sornette); doi:10.1017/jpr.2017.20; IIIS DP 122 (2006) | quant-auditor | retained — remediate |
| QUANT-3-5 | major | method | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1069-1110 (§5.4 eru-0259 bullet) | The §5.4 bullet asserts and denies the same fact in adjacent sentences: "Twin status was verified against the published article's indexed abstract" and, four paragraphs later, "Same-work identity cannot be settled at the depth available, and this review will assert neither it nor its negation." The refusal to adjudicate (SCOPE-2 … | Both sentences are in the same bullet. The affirmative claim is unsupported by anything retained: references_explosive-regime.json carries no `abstract` field for eru-0259 (eru-0198 has one); Crossref … | Delete or source the sentence "Twin status was verified against the published article's indexed abstract." If the abstract text was seen at extraction, retain it verbatim on the eru-0259 store entry a … | docs/literature/references_explosive-regime.json (eru-0259, eru-0198); api.crossref.org/works/10.1016/j.csda.2014.06.006; api.open … | quant-auditor | retained — remediate |
| LITERATURE-3-1 | major | misattributed-claim / withdrawn-claim not propagated | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787 | The agenda still carries the round-2-withdrawn er-bc-2 recall-gap claim. It states the backward-chase arm "named **two candidates** the frozen corpus does not contain, neither admitted" and lists "`er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited". The review withdrew exactly this clai … | Verified independently, not merely against the review: (a) `docs/literature/search_logs/explosive-regime/screen-verdicts-R1.jsonl:209` and `-R2.jsonl:209` record eru-0209 PROMOTE/PROMOTE; `screen2-ver … | Rewrite the agenda bullet to name ONE unadmitted candidate (er-bc-1 Hall, Psaradakis & Sola 1999, DOI 10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X — verified in Crossref as *Journ … | https://doi.org/10.1093/ectj/utaa004 ; https://doi.org/10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X | literature-check | retained — remediate |
| LITERATURE-3-2 | major | work-identity attribution / internal contradiction | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1069-1112 and :3175 (VG-13); docs/methodology … | The round-2 SCOPE-2-3 disclosure of the fourth twin pair (eru-0198 / eru-0259) is self-contradictory and applies a standard inconsistent with the three adjudicated pairs. Within the SAME bullet, line 1072-73 asserts "Twin status was verified against the published article's indexed abstract", while the appended blockquote and VG- … | (a) Review lines 1069-1074 vs lines 1101-1109 and VG-13 (line 3175) — direct contradiction on whether twin status was verified. (b) Protocol A13(b) quotes the project's own primary extraction log: "PR … | Reconcile the two sentences. Either (i) withdraw "Twin status was verified against the published article's indexed abstract" as an overstatement, or (ii) adjudicate the pair at the same depth used for … | https://doi.org/10.1016/j.csda.2014.06.006 ; https://ideas.repec.org/p/ems/eureir/39598.html | literature-check | retained — remediate |
| LITERATURE-3-3 | major | misstated correction record | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3064-3095 (L-18); repeated at :165? no — at : … | L-18's headline count is inconsistent with L-18's own table. The claim "Fourteen page locators in §7, §8 and §9 were wrong" is repeated at seven sites in the review and once in the agenda, but the old→new table carries NINETEEN corrected locators (PWY 9: 208→207, 209→208, 211→210, 213→212, 214→213, 215→214, 216→215, 220→219, 221 … | L-18 table, review lines 3074-3095 (20 rows, 19 with an old→new change). Count claim at lines 1957, 2476, 2490, 3058, 3061, 3064, 3639 and §17 line 3830; agenda line 756 ("corrected 14 locators in the … | Recount and restate at all eight sites (19 corrected locators plus one added, or state the counting rule that yields 14 and mark the rows it excludes), and reconcile the "already correct" sentence wit … | (none) | literature-check | retained — remediate |
| REPRODUCIBILITY-3-1 | major | data_hashed / entrypoint provenance | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3680-3681 (§15 ReproLog + sidecar rows), :319 … | The round-2 remediation emitted no ReproLog or sidecar of its own. §15 still cites the round-1 remediation records (`repro_log_a0f236b34b25417cb697df683198b3ef.json`, sidecar `a0f236b3…`) as the provenance record for a document whose content is now the round-2 remediation, and every input those records checksum is a superseded s … | ReproLog `a0f236b3…` (mtime 2026-09-02 12:25:21) records `config_resolved_sha256` = `0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b`, which §15:3670 itself labels "protocol SHA-256 w … | Emit a round-2 ReproLog and sidecar with `config_resolved_sha256` = `92fff3f2…`, `dataset_checksums` covering the current `references_explosive-regime.json` (`13c76d8f…`), `se-bc-01.json` (`1b8727dc…` … | (none) | reproducibility-verifier | retained — remediate |
| REPRODUCIBILITY-3-2 | major | data_hashed / cross_platform | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2432, :3215, :3218, :3678, :3679; .gitattribu … | The two evidence logs created by the round-2 remediation are cited by SHA-256 as the clone-durable carriers of that remediation's findings, but the digests were taken over CRLF working-tree bytes while `.gitattributes` forces `*.json text eol=lf`. Git normalises these files to LF on add, so no consumer of the committed repositor … | Byte counts: `se-crossref-recheck-01.json` CRLF 2609 / LF 2609 (all-CRLF); `se-fetch-recheck-01.json` CRLF 108 / LF 108; `se-bc-01.json` CRLF 1479 / LF 1479. `.gitattributes` line `*.json text eol=lf` … | Rewrite the two logs with LF endings before committing and republish the digests as `9457d3de…` and `f93061d1…`, or state at each citation site that the digest is over LF-normalised bytes and publish … | (none) | reproducibility-verifier | retained — remediate |
| QUANT-3-2 | major | numerical | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3094 (L-18 row); applied at §8.2 E11 (line 20 … | L-18 turned a CORRECT locator into a wrong one. Row "delay 0.05→0.03 and 0.04→0.06 \| pp.1090–1091 \| **p.1090**" collapses a two-page range onto one page, but the two figure pairs sit on different pages: the δ_T-varying delays (0.05→0.03) are Table 1, IER 56:1090; the duration-varying delays (0.04→0.06) are Table 2, IER 56:1091. … | Retrieved Cowles reprint p1499.pdf (sha256 85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012, verified against §9.5). p.1090 TABLE 1 "…DIFFERENT BUBBLE EXPANSION RATES": PSY r̂e 0.45 (0 … | Restore the L-18 row to "p.1090 (Table 1, expansion-rate delays 0.05→0.03) and p.1091 (Table 2, duration delays 0.04→0.06)" and split the citation at §8.2's E11 cell accordingly; correct L-18's "alrea … | doi:10.1111/iere.12131, IER 56(4):1079–1134, Tables 1–2, pp.1090–1091 | quant-auditor | dropped — refuted at the gate |
| REV-3-7 | minor | consistency | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1793-1802 (§7.6); :109-133 (abstract principa … | §7.6 declares the O6 assessable denominator 'fixed here and used at every site' and derives it as 69 - 4 NE - 2 NS = 63. But the same document makes 69 conditional: VG-13 / A13(b) / frontmatter all say 69-or-68 depending on the unadjudicated `eru-0198`/`eru-0259` pair. Both of those records are coded O6 = RT (§5 rows 4 and 64), … | **The O6 assessable denominator, fixed here and used at every site.** Coverage fractions on O6 are stated over **63 distinct works** = 69 distinct works − 4 NE (no full text at any stage, so no status … | Add one clause at §7.6, at §4's column header and at the abstract's principal finding (2): 'conditional on the fourth pair being two works; if `eru-0198`/`eru-0259` is one work (VG-13, A13(b)) the den … | CHAMP item 17 (data described adequately and correctly); PRISMA 2020 item 20 (synthesis results); review §5.4, VG-13, A13(b) | critical-reviewer | logged, not remediated |
| REV-3-8 | minor | standard-coverage | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:137-149 (Definitional basis (d)); :745 … | Review §14 item 3 issues an explicit consumer instruction that the agenda does not discharge: 'Carry the provenance of the qualifier too: "provisional on the working-paper twin" is not in protocol §9.1's frozen verdict vocabulary and is registered as amendment A13(c), and the reason for preferring it over `indeterminate-from-ful … | NB-13's `episode-statistic-null` stands as provisional-on-the-working-paper-twin and is re-openable under review protocol §10. | Append one sentence at the Definitional-basis (d) NB-13 site: 'The qualifier "provisional on the working-paper twin" is a post-hoc CONVENTION of the review (protocol amendment A13(c)), not a token of … | PRISMA 2020 item 24c (amendments to the registered protocol); CHAMP item 6; review §14 item 3, §9.4, VG-3, protocol amendment A13( … | critical-reviewer | logged, not remediated |
| SCOPE-3-2 | minor | partial | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-814 | Second propagation gap opened by the round-2 remediation: the agenda's residual section names the post-hoc amendment set as "A4–A11" and asserts flatly that "72 records are 69 distinct works", while the review as remediated carries A4–A13 and now gives the distinct-work count as 69-or-68 because a fourth, probable, unadjudicated … | Agenda l.806-807: "and three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works." Agenda l.808: "**Amendments A4–A11 are all post-hoc** (corrected 2026-09-02; the first … | In the agenda residual, replace "A4–A11" with "A4–A13" and add the two round-2 correcting entries in one clause (A12: partial-cell denominator 561 and backward-chase yield 1; A13: twin no-double-count … | deliverable_spec Thread A item 2; review VG-13, amendments A12/A13, §12.5 | scope-auditor | logged, not remediated |
| SCOPE-3-3 | minor | partial | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:750-756 vs 109-118, 500 | The agenda's own record of the locator remediation under-declares it and exceeds its warrant. The Verification-status bullet says only "The two Phillips quotation locators this agenda carries were wrong and are fixed", but five distinct locators were changed in the body (PWY quotation 52:214, PWY Table 1 note p.213, PWY divergen … | Agenda l.750-753: "**Page locators corrected 2026-09-02** (audit QUANT-2-3, review L-18). The two Phillips quotation locators this agenda carries were wrong and are fixed…" Agenda l.110 and l.500: "BS … | Restate the agenda bullet as five corrected locators, listing each old→new value against its L-18 row; and either cite the BSADF_r2 definition page from a checked L-18 row or drop the page from those … | review §12.1 L-18; review §14 item 6 ("If the agenda carries any further locator taken from §7, §8 or §9, it should be checked aga … | scope-auditor | logged, not remediated |
| SCOPE-3-4 | minor | documented-drift | docs/methodology/protocol_explosive-regime-review_2026-08-24.md (addendum) vs deliverable_spec_open-items-kals … | The declared spec's delegation forbids the review agent to "alter the frozen protocol or its eligibility criteria", while the frozen protocol's own §10 assigns amendment entries to the executing session. Ten amendments (A4–A13) were consequently appended to the protocol file during this session. The conflict is real but resolved … | Spec l.194: "MUST NOT alter the frozen protocol or its eligibility criteria". Review §12.5 l.3266-3268: "Protocol §10 makes the addendum append-only and **assigns amendment entries to the executing se … | Add one clause to the spec's delegation exclusion — "MUST NOT alter the frozen protocol text above its append-only addendum; amendments are appended under protocol §10 by the executing session" — so t … | ISO/IEC/IEEE 29148:2018 (requirements must be correct and conforming); protocol §10; review §12.5 | scope-auditor | logged, not remediated |
| QUANT-3-6 | minor | reporting | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-813 | Two agenda statements went stale again during round 2. (a) "Amendments A4–A11 are all post-hoc" — A12 and A13 were appended in the same round and are not named, although A12(b) is the correction QUANT-3-1 turns on and A13(b) is the fourth twin. (b) "three same-work twin pairs survive X7 deduplication, so 72 records are 69 distin … | Agenda line 807: "…so 72 records are 69 distinct works. Recorded as findings; the corpus was **not** re-screened." Line 808: "**Amendments A4–A11 are all post-hoc** (corrected 2026-09-02; the first Re … | Change "A4–A11" to "A4–A13" and add one clause naming A12 (er-bc-2 withdrawal, 561 denominator) and A13 (narrowed no-double-counting assurance, fourth probable twin); append "— 68 if the probable unad … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §12.5, VG-13 | quant-auditor | logged, not remediated |
| QUANT-3-7 | minor | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:783-795 (§4 header/table), 1783-1836 (§7.6) | The 68-or-69 conditional is disclosed in the frontmatter, abstract, §5.3, §5.4, VG-13, A13(b) and §12.4 item 5, but not at the two sites where distinct-work counts are actually computed and consumed. §4's header states "72 records but 69 distinct works" flatly and §7.6 explains the two columns as differing "because three records … | Both eru-0198 (row 64) and eru-0259 (row 4) are coded RT in §5. If the pair is one work: distinct works 68, denominator 62, numerator 21 → 21/62 = 33.87%, versus the reported 22/63 = 34.92% ("35%, jus … | Add one sentence to §4's header and to §7.6's synthesis claim: "Under the unresolved eru-0198/eru-0259 pair (VG-13, A13(b)) the distinct-work counts fall by one — O6 becomes RT 21 of 62 = 33.9%, which … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §5.3, §5.4, VG-13 | quant-auditor | logged, not remediated |
| QUANT-3-8 | minor | numerical | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3081 (L-18, PWY Table 4 row) | L-18's own parenthetical "(Appendix pp.222–225)" is wrong at the upper end. The PWY appendix runs pp.222–224; the reference list begins on p.224 and continues to p.226. | Retrieved p1349.pdf (sha256 a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4, matches §9.5; journal page = pdf page + 199). "APPENDIX" heading appears on p.222; "REFERENCES" appears on … | Change "(Appendix pp.222–225)" to "(Appendix pp.222–224; references pp.224–226)". | doi:10.1111/j.1468-2354.2010.00625.x, IER 52(1):201–226 | quant-auditor | logged, not remediated |
| QUANT-3-9 | minor | reporting | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1578-1585 (§7.3 prose); docs/research_notes/r … | L-18's third non-locator correction — relabelling the DP 2331 Table 2 quantities from "origination delay" to "mean bias in the estimated bubble origination date … at successful-detection rates 0.84 and 0.75" — was applied at §7.4 and §14 item 2 but not at §7.3 or in the agenda, so the same numbers carry two different labels insi … | §7.3: "controlling the family-wise error rate of the PSY dating recursion **increases origination delay from 7.56 to 12.20 months** while leaving collapse delay essentially unchanged (0.79 → 0.77)" — … | Use one label at all four sites and append "at SDR 0.84 vs 0.75, so the two means are conditioned on different event sets" to §7.3's prose and to the agenda's branch-3 FWER bullet. | Cowles DP 2331 (2022) §5.2–5.3 and Table 2, p.21 | quant-auditor | logged, not remediated |
| QUANT-3-10 | minor | reproducibility | docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl; L-18 | The 14 corrected locators live only in the review. The extraction log — which the review elsewhere treats as the primitive record and which VG-16 names as the successor's re-derivation source — still carries the superseded page attributions with no pointer to L-18. The frozen-artifact discipline ("no extraction file was touched" … | se-extraction-primary.jsonl, eru-0131 rob.Q1: "…cv provenance explicit (derived limit + MC-simulated operational CVs + declared log-log convention) [pp.208, 214]" (L-18: p.208 → p.207); rob.Q2: "empir … | Add one sentence to L-18: "The extraction logs are append-only and are not edited; se-extraction-primary.jsonl still carries the superseded locators, and any locator taken from it must be checked agai … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md L-18, VG-16; §17 "Artifacts changed by this pass" | quant-auditor | logged, not remediated |
| LITERATURE-3-4 | minor | version-mixed citation / locator not resolvable from the cit … | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1634-1636 (§7.4 table), :3603-3605 (§14 item … | The FWER triple and origination-bias figures are cited as "`eru-1289` Table 1 p.20, [Shi & Phillips 2022](https://doi.org/10.1017/9781108910095.003)". Those page locators belong to Cowles DP 2331 (31 pages), not to the DOI's target, which Crossref records as a 2025 Cambridge University Press chapter paginated 30-59. A reader fol … | Crossref 10.1017/9781108910095.003 → "Econometric Analysis of Asset Price Bubbles", *Financial Econometrics*, CUP, pp. 30-59, 2025-04-30. Review §9.5 line 2452 records the DP retrieved at https://cowl … | At each locator site cite the version actually read — Shi & Phillips (2022), Cowles Foundation DP 2331, Table 1 p.20 / Table 2 p.21, with the §9.5 URL and digest — and give the 2025 chapter DOI as the … | https://api.crossref.org/works/10.1017/9781108910095.003 ; https://elischolar.library.yale.edu/cowles-discussion-paper-series/2688 … | literature-check | logged, not remediated |
| LITERATURE-3-5 | minor | incomplete disclosure at a section preamble | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1956-1959 | §8's preamble says "**Two things did not survive** that re-read" and names the locators and the quotation-marked paraphrase. Three non-locator corrections are recorded elsewhere: the paraphrase, the mis-summarised E9 number ("0.697/0.401", which pairs two unrelated Table 2 cells and omits the maximum GSADF 0.787 at k = 6, T = 10 … | Preamble line 1956-1959 vs §9.5 lines 2485-2489, L-18 lines 3103-3110, and §17 line 3830 ("one paraphrase quotation-marked as verbatim, one mis-summarised number …, and one mislabelled row"). Independ … | Change "Two things" to three and name the E9 mis-summary in the preamble alongside the locators and the paraphrase. | (none) | literature-check | logged, not remediated |
| LITERATURE-3-6 | minor | count not propagated | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:174-175 (abstract Limitations); docs/research … | The 69-or-68 distinct-work conditionality created by VG-13/A13(b) is carried in §5.3, §5.4, §7.6 and VG-13 but not in the abstract's Limitations ("three same-work twins survive X7, so 72 records are 69 distinct works") or in the agenda's residual bullet ("three same-work twin pairs survive X7 deduplication, so 72 records are 69 … | Review lines 174-175 and agenda lines 806-807 state 69 flatly; review lines 1011-1012 and VG-13 (line 3175) state "69 if the pair is two works and 68 if it is one". | Append the conditional at both sites ("69 distinct works under the three adjudicated pairs; 68 if the probable fourth pair eru-0198/eru-0259 is one work — VG-13"), or resolve it per LITERATURE-3-2 and … | (none) | literature-check | logged, not remediated |
| LITERATURE-3-7 | minor | claim falsified by the same pass that made it | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1080-1081 | §5.4's fourth-twin blockquote states "neither store entry carries a twin note". The same round-2 pass added exactly such a note to both store entries, and §17 records that edit ("`references_explosive-regime.json`, **notes only** on `eru-0198` and `eru-0259`"). The eru-0259 note now opens "PROBABLE UNADJUDICATED SAME-WORK TWIN o … | references_explosive-regime.json:147 (eru-0259 note) and the parallel note on eru-0198 (:2271); review §17 line 3872-3873. | Restate as "neither store entry carried a twin note before this pass; both now carry a probable-twin note", or delete the sentence. | (none) | literature-check | logged, not remediated |
| LITERATURE-3-8 | minor | quantity mis-described in the consumer document | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:526-527 | The agenda says "The FWER-controlled variant buys that back at a delay cost of 7.56 → 12.20 months." L-18 corrected precisely this description in the review: DP 2331 Table 2 reports these as the MEAN BIAS in the estimated bubble origination date, in months, at successful-detection rates falling 0.84 → 0.75. Review §14 item 2 sup … | Agenda lines 522-527 vs review L-18 lines 3116-3119 and §14 item 2 lines 3603-3605. | Restate as "mean bias in the estimated bubble origination date of 7.56 → 12.20 months, at successful-detection rate 0.84 → 0.75 (DP 2331 Table 2 p.21)". | (none) | literature-check | logged, not remediated |
| REPRODUCIBILITY-3-3 | minor | entrypoint_runs | docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3193 (VG-16), :3685 (§15 reproduce-target row … | VG-16 is correctly scoped as repository-level and its core claims verify, but it understates the failure mode: the advertised Quickstart command does not merely find nothing to run, it aborts before pytest is reached. VG-16 also omits that `uv.lock` already resolves the environment locally, which makes the VG-14 remedy a one-com … | `uv run pytest --collect-only -q` terminates with a pyproject parse error: `[build-system]` … `missing field \`requires\`` — the table is present at pyproject.toml:41 with every key commented out, so … | In VG-16, add that `uv run pytest` currently fails at pyproject parse because `[build-system]` is declared with no `requires` key, so the Quickstart is broken independently of the missing tests; in VG … | (none) | reproducibility-verifier | logged, not remediated |

**Convergent clusters.** Four branches independently raised the same defect —
the round-2 withdrawal of `er-bc-2` never propagated to the consumer agenda —
as REV-3-1 (critical-reviewer), SCOPE-3-1 (scope-auditor), QUANT-3-1
(quant-auditor) and LITERATURE-3-1 (literature-check); all four are recorded
separately because each carries independent evidence (the review's §14 item 7
instruction, the protocol A12(b) entry, the primitive screening verdict files,
and a live Crossref check respectively), and all four passed the gate. A second
cluster covers the stale amendment enumeration and the unconditional
distinct-work count in the agenda (REV-3-2 major; SCOPE-3-2, QUANT-3-6,
LITERATURE-3-6 minors). A third covers the un-propagated relabelling of the
DP 2331 Table 2 quantities (REV-3-3 major, QUANT-3-3 major on the Table 1/Table 2
attribution, QUANT-3-9 and LITERATURE-3-8 minors). A fourth covers the fourth
twin pair's contradictory adjudication status (QUANT-3-5 and LITERATURE-3-2
majors; REV-3-7, QUANT-3-7 minors).

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; a drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Seventeen dispositions,
one per major finding: **1 dropped** (QUANT-3-2) and **16 retained** after failed
refutation attempts (`counts.refuted: 1`, `counts.to_remediate: 16`). There are
no retained-conservative entries this round (`retained_conservative: 0`), so no
entry is retained on uncertainty rather than on a failed refutation; the
retained-conservative class is nonetheless within scope of this section and
would be reported here if any entry fell into it. No entry carries
`reproduction_required: true` — every refutation attempt was resolved by direct
re-reading, live retrieval or independent recomputation reported inside the
refutation evidence itself — so **no `reproduction: {command, observed}` block is
owed on any entry**; where a refuter ran a command, fetched a file or recomputed
a digest, the command and its observed result are stated verbatim inside the
refutation evidence quoted below. Claims are reproduced verbatim and unabridged,
as is each refutation's evidence.

`evidence_type` is enumerated per entry. One entry is `source-quote` — QUANT-3-2,
the single drop, where the refuter retrieved the Cowles reprint `p1499.pdf`
(SHA-256 `85a984e9…`, matching §9.5), located the running head for IER 56:1090
and quoted the authors' own summary sentence carrying both delay pairs on that
one page, disproving the finding's load-bearing premise that the two pairs sit on
different pages. The other sixteen are `none`: in every case the refuter searched
for counter-evidence of the permitted types (`source-quote`, `reproduced-check`,
`counter-test`, `logical-proof`) and obtained none, so the gate could not drop
the finding. Several refutation attempts strengthened the finding instead
(REV-3-4, where L-10's own scope line was found to assert the flag §7.3 does not
carry; LITERATURE-3-2, where a project screening verdict recording a same-work
X7 determination on the disputed pair was found; LITERATURE-3-3, where an eighth
repetition site was found; QUANT-3-5, where one limb of the auditor's evidence
was corrected without disturbing the defect), and those additions are recorded in
the evidence text.

### QUANT-3-2 — dropped (refuted)

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false (no `reproduction` block owed); outcome: **dropped**

Claim verbatim:

> **category:** numerical
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3094 (L-18 row); applied at §8.2 E11 (line 2011)
>
> **issue:** L-18 turned a CORRECT locator into a wrong one. Row "delay 0.05→0.03 and 0.04→0.06 | pp.1090–1091 | **p.1090**" collapses a two-page range onto one page, but the two figure pairs sit on different pages: the δ_T-varying delays (0.05→0.03) are Table 1, IER 56:1090; the duration-varying delays (0.04→0.06) are Table 2, IER 56:1091. The old range was right; the new single page is not. This is a regression inside the table whose purpose is to fix locators, and L-18 additionally declares "all of PSY 2015b's simulation-section locators (pp.1090, 1092, 1093 …) were already correct".
>
> **evidence:** Retrieved Cowles reprint p1499.pdf (sha256 85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012, verified against §9.5). p.1090 TABLE 1 "…DIFFERENT BUBBLE EXPANSION RATES": PSY r̂e 0.45 (0.03), 0.44 (0.03), 0.43 (0.03) at δ_T 1.06/1.08/1.10, r_e=0.40 → delay 0.05→0.03. p.1091 TABLE 2 "…DIFFERENT BUBBLE DURATIONS": PSY r̂e 0.44 (0.02), 0.45 (0.03), 0.46 (0.04) at f−e = 0.10T/0.15T/0.20T → delay 0.04→0.06.
>
> **fix:** Restore the L-18 row to "p.1090 (Table 1, expansion-rate delays 0.05→0.03) and p.1091 (Table 2, duration delays 0.04→0.06)" and split the citation at §8.2's E11 cell accordingly; correct L-18's "already correct" sentence to include p.1091.
>
> **reference:** doi:10.1111/iere.12131, IER 56(4):1079–1134, Tables 1–2, pp.1090–1091

Refutation succeeded (`evidence_type: source-quote`); evidence verbatim:

> REFUTED. The finding's load-bearing premise — "the two figure pairs sit on different pages" — is false. Both delay pairs are asserted in a SINGLE sentence that lies wholly on IER 56:1090, so the L-18 correction to "p.1090" is right and the old range pp.1090–1091 was the looser locator, not the correct one.
>
> Source verified myself. Cowles reprint p1499.pdf, cached at C:\Users\skoir\AppData\Local\Temp\claude\C--Users-skoir-castles\0dd6aec6-5e05-434f-b42c-7cc8e9f01065\scratchpad\p1499.pdf, sha256 85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012 — byte-identical to the digest recorded in §9.5 (line 2451 of the lit review) and to the auditor's own stated digest. 57 pages; running heads give the mapping pdfidx = journal page − 1078 (pdfidx 12 head "1090 PHILLIPS, SHI, AND YU"; pdfidx 13 head "TESTING FOR MULTIPLE BUBBLES 1091").
>
> Verbatim, from §4.1 body text on p.1090 (pdfidx 12), pypdf extraction, NFKD-normalized:
> "For instance, the delay in the PSY estimate reduces from 0.05 to 0.03 when δT increases from 1.06 to 1.10 and the delay increases from 0.04 to 0.06 when the bubble duration extends from ⌊0.10T⌋ to ⌊0.20T⌋."
>
> The sentence is complete on p.1090 (it terminates before footnote 7 and before the page break); it is not split across the 1090/1091 boundary. A document-wide scan for the substrings "reduces from 0.05" and "0.04 to 0.06" returns exactly one page — pdfidx 12 = p.1090. p.1091 (pdfidx 13) contains neither substring.
>
> That is precisely what the L-18 row and the §8.2 E11 cell cite. E11 reads "delay 0.05 falling to 0.03 as δ_T rises 1.06→1.10; delay grows 0.04→0.06 as duration goes 0.10T→0.20T (p.1090)" — a paraphrase of the p.1090 sentence, cited to the page on which the paper makes that exact claim. The locator is correct as it stands; no split is warranted.
>
> The auditor's table readings are individually accurate but do not support the defect claim. Confirmed from the same file: p.1090 Table 1 ("…DIFFERENT BUBBLE EXPANSION RATES"), PSY column r_e = 0.40 → 0.45 (0.03), 0.44 (0.03), 0.43 (0.03) at δ_T 1.06/1.08/1.10; p.1091 Table 2 ("…DIFFERENT BUBBLE DURATIONS"), PSY column → 0.44 (0.02), 0.45 (0.03), 0.46 (0.04) at τ_f−τ_e = 0.10T/0.15T/0.20T. So the underlying tabulated values for the second pair do sit on p.1091 — but the review does not cite Table 2 or its cells; it cites the authors' summary sentence, which the authors placed on p.1090 while discussing "Tables 1 and 2" together. Citing where a claim is stated is not a wrong locator.
>
> The subsidiary complaint also fails: L-18's sentence "all of PSY 2015b's simulation-section locators (pp.1090, 1092, 1093, Table 4 p.1092) were already correct" enumerates the locators the review actually uses. p.1091 is not among them precisely because no §8/§9 claim is attributed to it, so there is nothing to add.
>
> The only residue is a stylistic preference for citing the source tables instead of the source sentence. That is not the reported defect, which was that "the new single page is not" right — and that is disproven by the page-1090 running head plus the verbatim sentence above.

### REV-3-1 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
>
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787
>
> **issue:** The round-2 withdrawal of `er-bc-2` (LITERATURE-2-1 / protocol A12(b)) did NOT propagate to the consumer agenda. The agenda's Verification-status residual still reports the post-freeze backward-chase arm as naming TWO records the frozen corpus does not contain, and still describes `er-bc-2` as having indeterminate eligibility. The review proves the opposite: the work is in the 1,996-record universe twice (`eru-0209` X7, `eru-1027` S-c-fail), was PROMOTE/PROMOTE at stage 1 and excluded at stage 2. The review's own §14 item 7 instructs the consumer in terms — 'must not be transcribed as a recall gap' — and the transcription happened anyway. This is the round-2 remediation's headline correction failing at the one downstream site it was written for, and it inflates the named recall gap from one record to two in the artifact a successor session will actually read.
>
> **evidence:** It named **two candidates the frozen corpus does not contain, neither admitted**:
>   - `er-bc-1` **Hall, Psaradakis & Sola 1999**, … 
>   - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited.
>
> **fix:** Replace the bullet pair with the corrected single-record form from review §14 item 7: the A11 diagnostic named ONE record the corpus does not contain (`er-bc-1`, a probable eligible miss on the pre-2011 antecedent layer); `er-bc-2` was a false positive, present in the universe as `eru-0209`/`eru-1027` and dual-screened and excluded (X7 / S-c-fail), and is not a recall gap. Add the A12(c) consequence the agenda inherits: the arm's DOI-or-exact-normalised-title absence test is defeated by one-word title variants, so its '177 absent' figure is an upper bound of unquantified looseness.
>
> **reference:** CHAMP item 30 (conclusions limited to what the analysis supports); PRISMA 2020 item 24c (amendments); review §2.2, §14 item 7, protocol amendment A12(b)-(c)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation. The claim reproduces exactly. Agenda lines 779-787 still read "It named **two candidates the frozen corpus does not contain, neither admitted**" with the er-bc-1 / er-bc-2 bullet pair, er-bc-2 marked "eligibility indeterminate, no abstract deposited". A grep of the entire agenda for er-bc, eru-0209, eru-1027 and A12 returns hits only at lines 775, 781, 786, 793 — the round-2 withdrawal appears nowhere in the consumer document, so there is no offsetting correction elsewhere in the file. The review contradicts the agenda directly: §14 item 7 (review lines 3653-3661) says er-bc-1 is "the only record the A11 diagnostic named that the corpus does not contain" and that er-bc-2 "was a false positive — that work is in the universe as eru-0209/eru-1027 and was dual-screened and excluded (X7 / S-c-fail) — and must not be transcribed as a recall gap"; the same correction is carried at VG-4 (line 3168), the amendment table rows A11 and A12 (lines 3300-3301), and finding row LITERATURE-2-1 (line 3828). Protocol amendment A12(b)-(c) (protocol_explosive-regime-review_2026-08-24.md lines 1044-1073) states "the set of records the corpus does not contain is **er-bc-1 alone**" and records the DOI-or-exact-normalised-title absence test being defeated by a one-word title variant. The only potentially exculpatory check I ran — whether eru-0209/eru-1027 exist in references_explosive-regime.json (grep count 0) — is not counter-evidence: that store holds the 72 included records, not universe-stage excluded ones, so their absence there is expected and consistent with the review's account.

### REV-3-2 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
>
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-814
>
> **issue:** The agenda's amendment enumeration was corrected in round 2 from 'A4-A6' to 'A4-A11', but the same round-2 pass appended A12 and A13 to the protocol addendum. The agenda's list is therefore stale again, and the two omitted entries are precisely the ones that correct claims the agenda repeats verbatim: A12(b) withdraws `er-bc-2` (see REV-3-1) and A13(b) makes the distinct-work count conditional (69 if the fourth pair is two works, 68 if one). The agenda states '72 records are 69 distinct works' flatly and 'three same-work twin pairs survive X7' as if the enumeration were closed, which is exactly the over-broad form review §5.3 and VG-13 narrowed.
>
> **evidence:** three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works. Recorded as findings; the corpus was **not** re-screened.
> - **Amendments A4–A11 are all post-hoc** (corrected 2026-09-02; the first Rev 4 text named only A4–A6).
>
> **fix:** Restate as 'Amendments A4-A13 are all post-hoc' and add A12 and A13 to the substantive list with one clause each: A12 — corrections to A7's `partial` denominator (585 -> 561) and A11's yield (2 candidates -> 1); A13 — the no-double-counting assurance narrowed to §7's evidence tables, a fourth PROBABLE unadjudicated twin pair (`eru-0198`/`eru-0259`) disclosed, and the NB-13 scope qualifier registered as a review CONVENTION. Change the twin sentence to '72 records are 69 distinct works under the three adjudicated pairs, and 68 if the fourth, unadjudicated pair is one work (review VG-13, A13(b)).'
>
> **reference:** PRISMA 2020 item 24c; CHAMP item 6 (consistency with the frozen protocol); protocol amendments A12, A13

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempt failed; the finding reproduces exactly on all four sub-claims. (1) Agenda line 808 reads verbatim "**Amendments A4-A11 are all post-hoc** (corrected 2026-09-02; the first Rev 4 text named only A4-A6)"; grep for "A12|A13" across the whole of docs/research_notes/research_agenda_regime-classification_2026-08-21.md returns 0 matches. (2) The protocol addendum does contain both later entries: docs/methodology/protocol_explosive-regime-review_2026-08-24.md:1018 "### A12 - 2026-09-02 (round-2 correcting entry)" and :1097 "### A13 - 2026-09-02 (round-2 correcting entry)". The agenda's enumeration is therefore stale. (3) A12(b) (protocol :1044) is headed "A11's yield: 1 candidate addition, not 2. `er-bc-2` is in the universe." and states of A11's description of er-bc-2 "**That is false.** ... It is **not** a recall gap and is withdrawn from A11's candidate list. The arm's yield of records the corpus does not contain is **`er-bc-1` alone**." (it documents er-bc-2 as present twice in the 1,996-record universe as eru-0209 and eru-1027, dual-screened and excluded on X7/S-c-fail). The agenda at :786 still lists "`er-bc-2` Banerjee, Chevillon & Kratz 2013 - eligibility indeterminate, no abstract deposited" under a bullet whose header is "...the frozen corpus does not contain, neither admitted" - i.e. it repeats the withdrawn claim. (4) A13(b) states "**72 records are 69 distinct works if this pair is two works, and 68 if it is one**, and the pair's two appraisal rows are not independent evidence whichever it is. Carried as a verification gap in the review's §12.3 (VG-13)", disclosing the fourth PROBABLE unadjudicated pair eru-0198/eru-0259. The agenda at :806-807 states flatly "three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works", with no conditional and no mention of eru-0198/eru-0259 or VG-13. No counter-evidence obtained; the consistency defect is confirmed.

### REV-3-3 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** consistency
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1569,1571,1577 (§7.3); :1899 (§7.8); :2636 (§11 TC-2); docs/research_notes/research_agenda_regime-classification_2026-08-21.md:526-527
>
> **issue:** The round-2 re-read established that DP 2331's 7.56 and 12.20 are the MEAN BIAS in the estimated origination date at successful-detection rates 0.84 and 0.75, reported in Table 2 p.21 — and corrected §7.4, §9.5, §14 and L-18 accordingly. Four other sites were left on the uncorrected label. §7.3 calls them 'PSY origination delay' in two table rows and again in prose, AND attributes them to `eru-1289` Table 1 (Table 1 is the FWER triple, p.20 — the review's own §9.5 and §14 say Table 2 p.21). §7.8 and §11 TC-2 repeat 'origination delay'. The agenda calls it 'a delay cost of 7.56 -> 12.20 months'. The successful-detection-rate cost (0.84 -> 0.75) that the corrected form carries is absent from all four. §17's assurance that 'No number was changed at one site only … were grepped across the document' does not hold for this correction, and §17's own QUANT-2-3 row lists the sites touched as §7.1/§7.4/§7.5/§7.6/§8.1/§8.2/§8.3/§9.5 — §7.3, §7.8 and §11 are not among them.
>
> **evidence:** | PSY origination delay, standard per-observation CVs | 7.56 months (4.99) | monthly, 10-year span, M = 2,000 | `eru-1289` Table 1, [Shi & Phillips 2022] … controlling the family-wise error rate of the PSY dating recursion **increases origination delay from 7.56 to 12.20 months**
>
> **fix:** Propagate the L-18 correction to all four sites. In §7.3 relabel the two rows 'PSY mean origination-date bias' with 'at successful-detection rate 0.84' / '0.75' in the design column, and change the source cell from `eru-1289` Table 1 to `eru-1289` Table 2 p.21; rewrite the prose sentence as 'increases mean origination-date bias from 7.56 to 12.20 months while the successful-detection rate falls 0.84 -> 0.75'. Apply the same relabel in §7.8's BSADF row and §11 TC-2. In the agenda, replace 'a delay cost of 7.56 -> 12.20 months' with 'mean origination-date bias 7.56 -> 12.20 months at successful-detection rate 0.84 -> 0.75'. Then update §17's claim, or delete it.
>
> **reference:** CHAMP items 17, 19 (data described adequately and correctly; individual results with their source); SAMPL general principles (numerical detail sufficient for re-use); review §12.1 L-18, §14 item 2

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; every element of the finding reproduces. (1) Uncorrected label present at all four sites: lit_review:1569 "PSY origination delay, standard per-observation CVs | 7.56 months (4.99) | ... | `eru-1289` Table 1"; :1571 "PSY origination delay, FWER-controlled ... | 12.20 months (5.33)"; :1577 "increases origination delay from 7.56 to 12.20 months"; :1899 (§7.8 BSADF row) "origination delay 7.56 months (standard CVs) or 12.20 (FWER-controlled)"; :2636 (§11 TC-2) "or 7.56-12.20 months"; agenda:527 "buys that back at a delay cost of 7.56 -> 12.20 months". (2) `grep -n "successful-detection"` over the review returns exactly three hits — :1636 (§7.4), :3119 (L-18), :3605 (§14) — confirming the corrected form ("mean bias in the estimated bubble origination date ... at successful-detection rates 0.84 and 0.75", "Table 2 p.21") is absent from all four flagged sites. (3) Table-number conflict verified internally: :2452 (§9.5 retrieval digest, SHA-256 309a38ae13210f56...) states "Table 1 FWER triple 0.55 / 0.78 / 0.93 (**p.20**); Table 2 origination bias 7.56 -> 12.20 months (**p.21**)", so §7.3:1569's attribution to `eru-1289` Table 1 contradicts the review's own verified re-read. (4) §17 claims verified: :3830 QUANT-2-3 row lists sites as "§7.1, §7.4, §7.5, §7.6, §8.1, §8.2, §8.3 and §9.5" (no §7.3/§7.8/§11); :3855-3857 carries "No number was changed at one site only: the denominators 561 and 63, the candidate count 1, and every corrected page locator were grepped across the document." Only nuance found, insufficient to refute: that sentence's enumerated scope covers denominators, a candidate count and page locators, and 7.56/12.20 were relabelled rather than renumbered — but the leading clause is unqualified and §7.3 still carries an uncorrected source locator ("Table 1"), so the assurance overstates either way. No local copy of Cowles DP 2331 exists in the repo (find for *2331* and data/external listing both empty), so no external counter-test of the Table 1/Table 2 assignment was possible; the only in-repo authority supports the finding.

### REV-3-4 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1601-1605 (§7.3)
>
> **issue:** The round-1 tier correction (LITERATURE-1-2, L-10) re-tiered `eru-1289` to WORKING-PAPER and stated that the tier 'travels with the claim … wherever it is used', then enumerated the sites: 'here, in the abstract's principal finding (4), in §7.8, and in §14's inputs'. §7.3 is not in that enumeration, and §7.3 is the section that calls the `eru-1289` pair 'the single most consumer-relevant number in the corpus'. Four of the thirteen rows of §7.3's dating table are `eru-1289`, and §7.3's tier line affirmatively asserts the opposite of the correction. §11 TC-2 does carry the tier flag for the same numbers, which makes §7.3 the one unguarded site.
>
> **evidence:** **The single most consumer-relevant number in the corpus** is the `eru-1289` pair … Evidence tier: peer-reviewed throughout.
>
> **fix:** Change §7.3's tier line to 'Evidence tier: peer-reviewed except the four `eru-1289` rows, which are WORKING-PAPER tier — the 2025 CUP chapter carrying that record's DOI was never obtained and the extracted text is Cowles DP 2331 (2022); §7.4 tier correction, L-10, VG-6.' Add `eru-1289` = working-paper tier inline in the four table rows, as §7.4 and §7.8 already do. Extend L-10's enumeration of sites to include §7.3 and §11 TC-2.
>
> **reference:** CHAMP items 19, 22 (individual results and certainty reported with their evidence status); charter rule that evidence tier travels with the claim; review §7.4 tier correction, L-10

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Attempted refutation failed; the defect claim reproduces exactly.
>
> 1. Verbatim reproduction at docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1601-1605 (§7.3, Synthesis claim O3): "termination is dated more accurately than origination in every design in the corpus that reports both (`eru-0395`, `eru-0559`, `eru-1289`). … Evidence tier: peer-reviewed throughout." The sentence that carries the tier assertion names `eru-1289` itself, so no narrowing reading rescues it.
>
> 2. Four unflagged `eru-1289` rows confirmed in §7.3's dating table (file lines 1569-1572): origination delay 7.56, collapse delay 0.79, FWER-controlled 12.20, FWER-controlled collapse 0.77. None carries a tier annotation, unlike §7.4's rows (1634-1636) which sit under an explicit tier-correction blockquote, and unlike the §7.3 third-party row for `eru-0150` which is flagged inline "Homm & Breitung WP" (line 1588). §7.3's own table therefore does flag WP tier where the review chose to — just not for `eru-1289`.
>
> 3. Tier status independently confirmed outside the review prose: docs/literature/references_explosive-regime.json, record `eru-1289`, `note` field — "The record is therefore tiered WORKING-PAPER, not peer-reviewed chapter, and every claim resting on it - including the FWER triple 0.55/0.78/0.93 - carries that tier". Also §5 store row 68 (line 909) and the §4 tier tally (line 796) both record the corrected working-paper tier.
>
> 4. The enumeration sub-claim is accurate. §7.4's tier-correction blockquote (lines 1653-1656) reads "wherever it is used — here, in the abstract's principal finding (4), in §7.8, and in §14's inputs to the consumer agenda." §7.3 is absent from that list, as stated.
>
> 5. The one candidate counter-fact found actually aggravates the finding rather than refuting it. L-10 in §12.1 (lines 2787-2797) does name §7.3 in its scope line: "*Affects:* §7.1, §7.2, §7.3 and §7.4 wherever those records are cited, each flagged at the point of use." That is an affirmative claim that §7.3 carries a point-of-use flag, and §7.3 instead asserts the opposite ("peer-reviewed throughout"). L-10's own tier-travel sentence, one line earlier, again omits §7.3: "carries that tier wherever it is used (§7.4, abstract finding (4), §7.8, §14)."
>
> 6. The corroborating detail in the finding also checks out: §11 TC-2 (line 2636) does carry the flag — "7.56-12.20 months (`eru-1289`, **working-paper tier**, §7.4)" — leaving §7.3 as the unguarded site.
>
> 7. §7's own preamble (lines 1389-1393) states the governing convention the §7.3 line violates: "Where a value is single-pass or intermediary-mediated the row says so. Where a value is preprint-tier the row says so."
>
> No counter-test, source quote, or logical argument available that defeats the claim.

### REV-3-5 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** verification-gap
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3174 (VG-10); :2472-2478, :2494-2500 (§9.5)
>
> **issue:** VG-10 was downgraded major -> minor on the strength of the Phillips re-read, then had a second, unlike residue folded into it: the three §9 NB texts were re-fetched but NOT re-read, so §9.1-§9.3's QUOTATIONS as well as their page locators remain single-session transcriptions. The review states in its own words that this is 'exactly the class that produced 14 errors in §8'. That residue is the same kind as VG-1 (four included records never read, major) and VG-3 (NB-13 journal version never obtained, major), and it sits under the three adjudications that discharge the consumer agenda's 'nearest unadjudicated candidates' claim — a branch-3 precondition. Carrying it at `minor` inside a gap whose stated reason for downgrade is a re-read that did not cover it understates a live risk in the last round available, and a reader scanning the severity column will read the §9 residue as minor. Note this is a severity/scoping objection, not a re-raise: the substance is disclosed.
>
> **evidence:** | **VG-10** | **minor** (downgraded from major, and re-scoped to §9's NB texts) | … **The three §9 NB texts were re-fetched but not re-read**, so their quotations and locators are still single-session transcriptions of exactly the class that produced those fourteen errors; VG-10 now carries that residue.
>
> **fix:** Split the gap. Keep VG-10 at `minor` for the version-identity residue alone (no extraction-time digest, so 2026-08 and 2026-09 files cannot be proved identical). Open a separate `major` gap — the §9 NB quotations and locators are unverified single-session transcriptions of the class that produced 14 errors in §8, and they carry the three out-of-corpus adjudications the consumer relies on. Either re-read the three digested files (bounded: the digests are already recorded in the §9.5 table) and close it, or carry the major gap into §14 item 3 so the agenda inherits it. The agenda currently inherits neither.
>
> **reference:** CHAMP item 29 (methodological limitations discussed appropriately); CHAMP response scale — Unclear maps to major, never to accept; review §9.5, L-16, VG-10

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; every factual premise reproduced. (1) VG-10 at lit_review_explosive-regime-dating_2026-08-24.md:3174 reproduces verbatim, severity cell "minor (downgraded from major, and re-scoped to §9's NB texts)", with the §9 residue folded into the same gap whose stated downgrade ground is the Phillips re-read. (2) §9.5:2472-2474 and L-16:3059-3061 state in the review's own words that the three NB texts were re-fetched but NOT re-read, that §9.1-§9.3's quotations and page locators remain single-session transcriptions "of exactly the class that produced those fourteen errors", and that the NB locators "should be treated as unverified". (3) Counter-test on L-18's old->new locator table (:3064-3105), the sole record of what the re-read actually verified: all 14 corrected locators belong to eru-0131 (PWY 2011), eru-0393 (PSY 2015a), eru-0395 (PSY 2015b) and eru-1289 (Cowles DP 2331); zero entries touch NB-02, NB-08 or NB-13, confirming no pass covered the §9 NB quotations or locators despite L-18's "§7, §8 and §9" heading. (4) grep for single-session|unverified|not re-read|VG-10|L-16 inside §9.1-§9.3 (:2147-2380) returns no hits, so no inline caveat sits under the three adjudications themselves. (5) Inheritance: §14 item 3 (:3611-3630) carries NB-13 provisional status, A13(c), the NB-08 derivability note and A9/VG-9 but never the unverified-transcription residue; §14 item 6 propagates only the two already-corrected Phillips locators; research_agenda_regime-classification_2026-08-21.md lines 14-15, 129-147, 512-518, 739-745 inherit episode-statistic-null, NB-13-provisional and VG-9 and nothing about unverified §9 quotations — so "the agenda currently inherits neither" is accurate. The finding is a severity/scoping objection resting on facts that all hold; per the gate's rules this is refuted=false with no counter-evidence.

### REV-3-6 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1420-1428, :1450-1460 (§7.1); :1898 (§7.8)
>
> **issue:** The round-2 re-read of PSY 2015a Table 2 established that the table's maximum size is GSADF 0.787 at fixed lag k = 6, T = 100 — under the stated null DGP, with only the fitted lag order changed. That number was recorded at §8.2's E9 cell and in L-18, and nowhere else. §7.1, the section that IS the O1 synthesis, reports from the same table only the k = 0 column (SADF 0.041-0.060, GSADF 0.055-0.070) and puts every size failure in a second table of 'departures from the stated null'. §7.8's GSADF row likewise carries 'size 0.055-0.070 at 5%' with no lag caveat. The consequence is a synthesis claim that reads as if the originators' own null-case size were near-nominal and all failures third-party: lag overspecification is a specification choice, not a departure from the null, and 0.787 is nearly sixteen times nominal. §17 asserts the round-2 corrections were 'applied at every site in §7.1, §7.4, …' — §7.1 does not carry this one.
>
> **evidence:** **Synthesis claim (O1).** *The recursive right-tailed family's near-nominal size is a property of its stated null, not of the family.* Every departure from `iid errors + constant unconditional variance + asymptotically negligible drift + no deterministic trend + no jumps` that the corpus tests produces size distortion
>
> **fix:** Add a row to §7.1's first table: 'GSADF, lag overspecification | up to 0.787 at 5% (fixed k = 6, T = 100); 0.697 under significance-test kmax = 6, with SADF 0.145 | same null DGP, lag order varied | `eru-0393` Table 2 p.1058'. Add 'severe distortion under lag overspecification (up to 0.787)' to §7.8's GSADF row. Qualify the O1 synthesis sentence so it does not imply the stated null is safe irrespective of lag choice, and record lag-order selection as a TC-1 input.
>
> **reference:** CHAMP item 20 (no selective reporting of analyses); SAMPL — report the analysis as performed, including the least favourable cells of a cited table; review §8.2 E9, L-18

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation found; the finding reproduces exactly at every stated location and is corroborated by the document's own text.
>
> (1) docs/literature/lit_review_explosive-regime-dating_2026-08-24.md lines 1414-1479 constitute the whole of §7.1 (next header "### 7.2" at line 1480). Its first table's PSY 2015a rows are "SADF | 0.041 / 0.049 / 0.042 / 0.054 / 0.060 at 5% | T = 100/200/400/800/1600, asymptotic CVs, lag k = 0" (line 1422) and "GSADF | 0.061 / 0.058 / 0.055 / 0.069 / 0.070 at 5% | same design" (line 1423). No k = 6 or kmax = 6 cell of the same Table 2 appears anywhere in §7.1. The second table (lines 1434-1448) is headed "departure from the stated null"; its only lag-related row is third-party (`eru-1604`, Pavlidis 2025, "heavy tails and lag-length misspecification | GSADF up to 0.67"), confirming the asymmetry the finding names.
>
> (2) §7.8 line 1898 GSADF row reads "size 0.055-0.070 at 5%" with validity conditions "as SADF, plus r0 = 0.01+1.8/sqrt(T) (convention)" - no lag caveat. The SADF row (line 1897) carries none either.
>
> (3) grep for "0.787" over the file returns exactly four sites, none in §7.1 or §7.8: line 2010 (§8.2 E9 cell), lines 2486-2489 (§9.5 bullet: "Restated at its site and recorded in L-18"), lines 3104-3109 (§12.1 L-18), line 3830 (§17 QUANT-2-3 row). grep over docs/methodology/protocol_explosive-regime-review_2026-08-24.md, docs/research_notes/research_agenda_regime-classification_2026-08-21.md and docs/literature/references_explosive-regime.json returns nothing.
>
> (4) The review states the defect itself. L-18 line 3109: "Restated at its site. The ten k = 0 figures §7.1 reports from the same table verify cell for cell." That is an explicit record that §7.1 carries only the k = 0 column and that the maximum-cell correction was applied at a single site (§8.2).
>
> (5) The "same null DGP, lag order varied" premise is confirmed by the review's own placement: §8.2's E9 cell is the *size* cell, and it reads "severe distortion under lag overspecification, **worst cell GSADF 0.787** (fixed lag k = 6, T = 100), and the authors' own highlighted case 'when T = 100, r0 = 0.190, and kmax = 6, the size of SADF and GSADF is 0.145 and 0.697'". Lag overspecification is therefore recorded by the review as a fitted-specification change under the null, not a DGP departure - so §7.1's exclusion of it from the null-case table is the reporting defect alleged. 0.787 / 0.05 = 15.7x nominal, matching the finding's arithmetic.
>
> (6) The §17 sub-claim survives as worded. Line 3830 reads "...applied at every site in §7.1, §7.4, §7.5, §7.6, §8.1, §8.2, §8.3 and §9.5". §7.1 does carry one L-18 locator correction (`eru-0131` Table 3 Panel A, p.220 -> p.219, line 1424), so the sentence is not globally false; but the finding is scoped to "this one" (the 0.787 correction), and that correction is absent from §7.1. Partial mitigation at most, not refutation.
>
> No later remediation has been applied: the working-tree file is the current state and lacks the row. The only candidate counter-arguments available are severity/scoping quibbles, which do not meet the refutation bar.

### SCOPE-3-1 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** partial
>
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787
>
> **issue:** The round-2 er-bc-2 retraction was remediated in the review but NOT propagated to the agenda, and the review explicitly handed that propagation to the lead. The agenda's residual still states the A11 backward-chase arm "named two candidates the frozen corpus does not contain, neither admitted" and lists `er-bc-2` Banerjee, Chevillon & Kratz 2013 as one of them with "eligibility indeterminate, no abstract deposited". Review §14 item 7, written in the same remediation pass, says the opposite and names the transcription as forbidden. A consumer reading only the agenda inherits a withdrawn false claim that overstates the corpus's recall gap by one record, and the two Thread A deliverables now contradict each other on a point an audit round already adjudicated. Spec item Thread A/2 requires branch 3 to integrate the review's verdicts; this verdict was not integrated.
>
> **evidence:** Agenda l.779-787: "It named **two candidates the frozen corpus does not contain, neither admitted**: - `er-bc-1` **Hall, Psaradakis & Sola 1999** … - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited." Review §14 item 7 (l.3653-3661): "**The backward-chase gap the agenda inherits is ONE named record, not two (finding LITERATURE-2-1).** … `er-bc-2` … was a false positive — that work is in the universe as `eru-0209`/`eru-1027` and was dual-screened and excluded (X7 / S-c-fail) — and **must not be transcribed as a recall gap**." Review §17 (l.3876-3881): "§14 carries the inputs, including the two page locators (item 6) and the corrected backward-chase gap (item 7) that this round's findings add to that list."
>
> **fix:** Rewrite the agenda bullet to "It named ONE record the frozen corpus does not contain, not admitted: er-bc-1 …", delete the er-bc-2 sub-bullet or restate it as a withdrawn false positive present in the universe as eru-0209/eru-1027 (screened, excluded X7 / S-c-fail), and carry A12(c)'s bound that the arm's DOI-or-normalised-title absence test makes "177 absent" an upper bound with unquantified looseness.
>
> **reference:** deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread A item 2 ("Branch 3 integrates the review's verdicts"); review §14 item 7; A12(b)-(c); VG-4/VG-12

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Could not refute; the finding reproduces exactly at every cited location and is corroborated by three independent artifacts.
>
> (1) Agenda text verbatim, lines 779-787 of docs/research_notes/research_agenda_regime-classification_2026-08-21.md: "It named **two candidates the frozen corpus does not contain, neither admitted**:" followed by the er-bc-1 bullet and "- `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited." Line numbers match the finding's 779-787 precisely.
>
> (2) A grep of the entire agenda for `er-bc-2|Banerjee|eru-0209|eru-1027` returns exactly one hit (line 786, the stale bullet). There is no correction, withdrawal note, or superseding paragraph anywhere else in the agenda, so the "propagation was done elsewhere in the file" escape is closed.
>
> (3) Review §14 item 7 reproduces verbatim at lit_review_explosive-regime-dating_2026-08-24.md:3653-3661: "**The backward-chase gap the agenda inherits is ONE named record, not two (finding LITERATURE-2-1).** ... `er-bc-2` ... was a false positive — that work is in the universe as `eru-0209`/`eru-1027` and was dual-screened and excluded (X7 / S-c-fail) — and must not be transcribed as a recall gap." The contradiction between the two Thread A deliverables is therefore direct and textual.
>
> (4) The withdrawal is not a review-only assertion; it is carried in three further places: protocol amendment A12(b) (protocol_explosive-regime-review_2026-08-24.md:1044, "A11's yield: 1 candidate addition, not 2. `er-bc-2` is in the universe."), review VG-4 (l.3168) and the A11/A12 addendum rows (l.3300-3301), and a `corrections_2026-09-02` block I read directly out of docs/literature/search_logs/explosive-regime/se-bc-01.json, which states for `candidate_additions[1] (er-bc-2)`: "WITHDRAWN. The work is in the universe twice: eru-0209 ... and eru-1027 ... Both PROMOTE/PROMOTE at stage 1; at stage 2 eru-0209 EXCLUDE/X7 ... and eru-1027 EXCLUDE/S-c-fail ... It is not a recall gap.", and restates the result summary as "1 candidate addition (er-bc-1), 6 named near-misses". So the agenda contradicts the review, the protocol addendum, and the primary search log simultaneously.
>
> (5) The only counter-line I could construct is a wording escape: "the frozen corpus does not contain" is, read narrowly against the 72-record included set, literally true of er-bc-2's work, since eru-0209/eru-1027 were excluded rather than absent. That escape fails on two independent grounds. First, the sub-bullet's substantive predicate — "eligibility indeterminate, no abstract deposited" — is independently false on the record: eligibility was determined (dual-screened, excluded X7 / S-c-fail, terminal under A3), and the round-2 audit's Crossref check on 10.2139/ssrn.2322360 returned a full deposited jats:p abstract (audit_trail_phase2-explosive-review_2026-08-24.md:1560). Second, the bullet sits inside the residual/completeness paragraph as an unadmitted recall candidate, which is precisely the transcription review §14 item 7 forbids. That is a plausibility argument about phrasing, not counter-evidence, and it does not survive the two falsified clauses.
>
> The defect claim — round-2 er-bc-2 retraction remediated in the review but not propagated to the agenda, leaving the two Thread A deliverables in contradiction on an adjudicated point — is true as stated.

### QUANT-3-1 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** reporting
>
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:777-787
>
> **issue:** The withdrawn er-bc-2 claim survives in the consumer agenda. The review withdrew it as FALSE (LITERATURE-2-1, A12(b), VG-4) and §14 item 7 says explicitly it "must not be transcribed as a recall gap"; the lead's round-2 agenda pass rewrote the surrounding bullet (post-freeze A11 status, er-bc-1 as a probable eligible miss) but left the two-candidate framing and er-bc-2 itself in place. Rev 4 therefore ships a factual falsehood the review had already retracted.
>
> **evidence:** Agenda: "It named **two candidates the frozen corpus does not contain, neither admitted**: … - `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited." Verified against the logs: screen-verdicts-R1/R2.jsonl give eru-0209 PROMOTE/PROMOTE and eru-1027 PROMOTE/PROMOTE at stage 1; screen2-verdicts-R1.jsonl gives eru-0209 EXCLUDE/X7 ("working-paper twin of eru-1027") and eru-1027 EXCLUDE/S-c-fail, X6 from the second screener in both cases. The candidate store carries eru-0209 ("…Bubbles with a Near-Explosive Random Coefficient Model", no DOI) and eru-1027 (10.1093/ectj/utaa004). The work is in the universe and was dual-screened.
>
> **fix:** Replace the bullet's lead with "It named ONE candidate the frozen corpus does not contain"; delete the er-bc-2 sub-bullet and replace it with the withdrawal plus the instrument bound ("absent by DOI or exact normalised title only; 177 is an upper bound of unquantified looseness"), citing review §2.2, A12(b)-(c), VG-4/VG-12.
>
> **reference:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §2.2, §14 item 7; docs/methodology/protocol_explosive-regime-review_2026-08-24.md A12(b); docs/literature/search_logs/explosive-regime/se-bc-01.json corrections_2026-09-02

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation. Every element reproduced. (1) docs/research_notes/research_agenda_regime-classification_2026-08-21.md lines 775-787 still carry "It named **two candidates the frozen corpus does not contain, neither admitted**" plus the sub-bullet "- `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited."; grep across the whole agenda for er-bc/Banerjee/LITERATURE-2-1/A12 returns only lines 775, 781, 786, 793, so no later passage corrects it. (2) Review docs/literature/lit_review_explosive-regime-dating_2026-08-24.md §2.2 lines 305-330: "**`er-bc-2` was NOT a recall gap and the claim that it was is withdrawn.**" and "**That is false.**", and it records eru-1027 as carrying "a full deposited abstract of the same NERC model", directly contradicting the agenda's "no abstract deposited"/"eligibility indeterminate". (3) Review §14 item 7 lines 3653-3661 is an explicit consumer-side directive: the gap is "ONE named record, not two" and er-bc-2 "must not be transcribed as a recall gap". (4) Protocol docs/methodology/protocol_explosive-regime-review_2026-08-24.md line 1044, amendment A12(b): "A11's yield: 1 candidate addition, not 2. `er-bc-2` is in the universe." (5) Logs confirm the underlying fact: screen-verdicts-R1.jsonl:209 and -R2.jsonl:209 PROMOTE/PROMOTE (eru-0209); -R1.jsonl:1027 and -R2.jsonl:1027 PROMOTE/PROMOTE (eru-1027); screen2-verdicts-R1.jsonl:73 EXCLUDE/X7 "working-paper twin of eru-1027"; screen2-verdicts-R1.jsonl:364 EXCLUDE/S-c-fail. The only available defense — that "the frozen corpus does not contain er-bc-2" is literally true because eru-1027 was excluded rather than absent — fails, because the agenda additionally asserts "eligibility indeterminate, no abstract deposited", which the review adjudicated false on a deposited abstract and a substantive S-c-fail exclusion, and because §14 item 7 bars the recall-gap framing itself. Finding stands.

### QUANT-3-3 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** numerical
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1573-1578 (§7.3 evidence table, eru-1289 rows)
>
> **issue:** §7.3 attributes the 7.56 / 0.79 / 12.20 / 0.77-month figures to `eru-1289` **Table 1**. They are in Table 2 (DP 2331, p.21); Table 1 is the FWER table (0.55/0.78/0.93, p.20). §7.4 and §14 item 2 cite Table 2 correctly, so the review contradicts itself, and the wrong attribution sits on what §7.3 itself calls "the single most consumer-relevant number in the corpus". Round 2's claim that "every headline number verified" against the retrieved text did not cover §7.3 — §9.5 lists the sites re-applied as §7.1, §7.4, §7.5, §7.6, §8.1, §8.2, §8.3, §9.5, omitting §7.3.
>
> **evidence:** Retrieved d2331_0.pdf (sha256 309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e, matches §9.5). Printed p.20 carries "Table 1: The family wise error rates of the PSY procedure … PSY (standard) 0.55 0.78 0.93". Printed p.21 carries "Table 2: The successful detection rates and the biases of the estimated bubble origination and collasping dates … PSY (standard) 0.84 … 7.56 (4.99) 0.79 (1.72); PSY (multiple) 0.75 … 12.20 (5.33) 0.77 (1.71)".
>
> **fix:** Change the four `eru-1289` source cells in §7.3 from "Table 1" to "Table 2 p.21", and add §7.3 to the site list in §9.5 and L-18.
>
> **reference:** Shi & Phillips, Cowles Foundation Discussion Paper 2331 (2022), Tables 1–2, pp.20–21

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No counter-evidence found; the finding reproduces exactly and is independently confirmed against the primary source.
>
> 1. Artifact reproduced. docs/literature/lit_review_explosive-regime-dating_2026-08-24.md lines 1569-1572 read: "| PSY origination delay, standard per-observation CVs | 7.56 months (4.99) | monthly, 10-year span, M = 2,000 | `eru-1289` Table 1, [Shi & Phillips 2022](https://doi.org/10.1017/9781108910095.003) |" with the following three rows ("same") inheriting that source cell. Line 1577 is the "single most consumer-relevant number" sentence.
>
> 2. Source independently retrieved and read. I fetched https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf myself: HTTP 200, 591,865 bytes, sha256 309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e (byte-identical to the digest §9.5 records), 31 pages. Text extraction via pypdf:
>    - PDF page 21 (printed p.20): "Table 1: The family wise error rates of the PSY procedure ... PSY (standard) 0.55 0.78 0.93 / PSY (multiple) 0.04 0.06 0.05". No delay or SDR figures anywhere on it.
>    - PDF page 22 (printed p.21): "Table 2: The successful detection rates and the biases of the estimated bubble origination and collasping dates ... T = 120 SDR ... PSY (standard) 0.84 7.56 (4.99) 0.79 (1.72) / PSY (multiple) 0.75 12.20 (5.33) 0.77 (1.71)".
>    All four disputed values (7.56/4.99, 0.79/1.72, 12.20/5.33, 0.77/1.71) are in Table 2 and none is in Table 1. The auditor's page and table attributions are exact.
>
> 3. Internal contradiction reproduced. The same review cites the same numbers to Table 2 at line 1636 ("`eru-1289` Table 2 p.21"), line 2452 ("Table 1 FWER triple 0.55 / 0.78 / 0.93 (**p.20**); Table 2 origination bias 7.56 -> 12.20 months (**p.21**)"), line 3049, line 3117 and line 3605 ("Table 2 p.21"). Only §7.3 says Table 1.
>
> 4. Coverage-gap sub-claim reproduced. Line 3830 (QUANT-2-3 row) lists the round-2 re-application sites as "§7.1, §7.4, §7.5, §7.6, §8.1, §8.2, §8.3 and §9.5" — §7.3 is absent, so round 2's "every headline number verified" bullet (line 2483, which itself pins the figures to Table 2 p.21) never touched the §7.3 cells.
>
> 5. The project's own extraction log agrees with the source, not with §7.3: docs/literature/search_logs/explosive-regime/se-extraction-recheck.jsonl record eru-1289 places the FWER triple at "Table 1 p.20 (PDF p.21)" and the SDR/delay figures under E10_power at "Table 2 (T=120, bubble DGP (25))"; screen2-verdicts-ADJ.jsonl likewise describes "Tables 1-3 report family-wise size, detection rates, dating bias/delay".
>
> The only conceivable escape — that "Table 1" refers to the CUP chapter (DOI 10.1017/9781108910095.003) whose numbering might differ — fails: §14/§9.5 of the review state the chapter "is still not obtained", so no chapter numbering was ever consulted, and the row's design cell ("monthly, 10-year span, M = 2,000") is verbatim the DP 2331 §5.2 setup that feeds its Table 2.

### QUANT-3-4 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** verification-gap
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2147-2185 (§9.1); §9.5 "What is still not established"; VG-10
>
> **issue:** VG-10's retained residue — "the three NB texts were re-fetched but NOT re-read, so their locators remain unverified" — is not a neutral residual: on re-read NB-02's locators are demonstrably wrong. I re-read all three. NB-08 and NB-13 verify exactly; NB-02 has three wrong page attributions in the section that carries the branch-3 definitional adjudication. Leaving this open when the file is already in hand and the review itself calls it "a bounded task" is a live defect, not an acceptable residual.
>
> **evidence:** Retrieved nb02.pdf (sha256 d8ae7e69dce54dc97a3b014f4865ad263a0cf4d2d6a75fa8476214d3bc12973f, matches §9.5). Printed folios: pdf p3=1, p4=2, p11=9, p12=10. (a) "we shall take the stretched exponential law as our null hypothesis" cited (§1, p.1) — is on p.2. (b) "for each financial time series, we have reshuffled the daily returns 1000 times…" cited (§5, p.8) — is on p.9. (c) "The third column gives the number of drawdowns above the threshold in the true data…" cited (§5, p.8) — is on p.9; §5 itself begins on p.9. Control checks that PASS: NB-08 abstract p.603, "our main result reduces the drawdown problem…" p.605, "Drawdowns are also closely related…" and the τ_a passage p.604 (nb08.pdf sha256 87277984ef7ecf4c61509577257de911b40ed18331d32013ac7249b3ebe13413); NB-13 §1 p.2 definitions, §2 p.6 CACC sentence, §4.1 p.14 one-standard-deviation threshold (nb13.pdf sha256 9e38c95673c9880aa2d8db353c06b020be49e86b78b9280bbeea44d8c476379a).
>
> **fix:** Correct the three NB-02 locators in §9.1 (p.1→p.2; p.8→p.9 twice), add them to L-18's table, and narrow VG-10 to record that the NB re-read has now been done with NB-02 failing and NB-08/NB-13 passing.
>
> **reference:** arXiv:cond-mat/0010050v2 (Johansen & Sornette); doi:10.1017/jpr.2017.20; IIIS DP 122 (2006)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; the defect claim reproduces exactly. I independently downloaded arXiv:cond-mat/0010050v2 (sha256 d8ae7e69dce54dc97a3b014f4865ad263a0cf4d2d6a75fa8476214d3bc12973f, 1,205,388 bytes, 55 pages — digest matches the §9.5 row) and extracted per-page text with pypdf. Printed folios confirm the finding's offset: pdf p3 ends "1", p4 ends "2", p11 ends "9", p12 ends "10". Quote locations: (a) "we shall take the stretched exponential law as our null hypothesis" occurs only on pdf p4 = folio 2, while lit_review §9.1 item 2 cites "(§1, p.1)" — wrong; (b) "for each financial time series, we have reshuffled the daily returns 1000 times and hence generated 1000 synthetic data sets for each" occurs only on pdf p11 = folio 9, cited as "(§5, p.8)" — wrong; (c) "The third column gives the number of drawdowns above the threshold in the true data..." occurs on pdf p11 = folio 9 (and again in the p.48 table appendix), cited as "(§5, p.8)" — wrong. The §5 heading "5 Synthetic tests and statistical significance" is itself on pdf p11 = folio 9, so §5 does not start on p.8. The one §9.1 locator the finding does not challenge is correct: the drawdown definition ("A drawdown is thus the cumulative loss from the last maximum to the next minimum") is on pdf p3 = folio 1, matching "(§1, p.1)". Two alternative-convention defences were tested and both fail: under PDF-page numbering the three quotes would be pp.4, 11, 11 — matching none of the cited p.1/p.8 values; and journal pagination (J. Risk 4(2):69-110) is excluded both because §9.1 states the adjudicated version is the arXiv v2 preprint with quotes "verbatim from the adjudicated text" and because 69-110 contains neither p.1 nor p.8. The review's own adjacent citation "(§6, item 6, pp.9-10)" — §6 begins on folio 9, item 6 sits at the top of folio 10 — establishes that folio numbering is the convention actually in use, so the three cited locators are inconsistent with the review's own scheme as well as factually wrong. Finding stands as stated (major/verification-gap).

### QUANT-3-5 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** method
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1069-1110 (§5.4 eru-0259 bullet)
>
> **issue:** The §5.4 bullet asserts and denies the same fact in adjacent sentences: "Twin status was verified against the published article's indexed abstract" and, four paragraphs later, "Same-work identity cannot be settled at the depth available, and this review will assert neither it nor its negation." The refusal to adjudicate (SCOPE-2-3 / A13(b) / VG-13) is the right posture on the evidence that survives, but it is not tenable while the affirmative sentence stands — if twin status was verified, the pair is adjudicated and the distinct-work count is 68, row 4 is a duplicate appraisal row, and the 65 assessable denominator is inflated by one.
>
> **evidence:** Both sentences are in the same bullet. The affirmative claim is unsupported by anything retained: references_explosive-regime.json carries no `abstract` field for eru-0259 (eru-0198 has one); Crossref for 10.1016/j.csda.2014.06.006 returns no abstract; the OpenAlex record for the same DOI has no abstract_inverted_index. se-extraction-primary.jsonl's note says only "abstracts near-identical", with no retained abstract text for the journal version.
>
> **fix:** Delete or source the sentence "Twin status was verified against the published article's indexed abstract." If the abstract text was seen at extraction, retain it verbatim on the eru-0259 store entry and adjudicate the pair; if it cannot be reproduced, withdraw the sentence and leave the VG-13 refusal as the sole statement.
>
> **reference:** docs/literature/references_explosive-regime.json (eru-0259, eru-0198); api.crossref.org/works/10.1016/j.csda.2014.06.006; api.openalex.org/works/doi:10.1016/j.csda.2014.06.006

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Not refuted; the defect reproduces at the stated location. Line 1072-1073 of docs/literature/lit_review_explosive-regime-dating_2026-08-24.md reads "Twin status was verified against the published article's indexed abstract." and lines 1105-1107 of the same bullet read "Same-work identity cannot be settled at the depth available, and this review will assert neither it nor its negation." The document's own vocabulary makes these mutually exclusive: section 5.3 is titled "Three same-work twins", line 999 describes the twin ledger as "review-stage hand-verified", and lines 980 and 1011 call this pair "probable but unadjudicated", so "verified twin status" is the very adjudication the later paragraph refuses. The affirmative sentence carries no hedge limiting it to abstract depth, and the indexed abstract is inside "the depth available", so the compatibility reading fails. External checks reproduce the auditor's evidence: Crossref works/10.1016/j.csda.2014.06.006 returns no abstract key; OpenAlex W2007843530 has abstract_inverted_index null; Semantic Scholar paper 8e1952a9a70acd1ee1e22f7db73d993eddada950 returns "abstract": null with a publisher-elision disclaimer; references_explosive-regime.json has no abstract field on eru-0259 while eru-0198 has one. ONE SUB-CLAIM OF THE AUDITOR'S EVIDENCE IS INCORRECT but does not disprove the defect: the sentence is not unsourced. se-extraction-recheck.jsonl, record eru-0259, field "doc", states verbatim "Twin status verified against the published article's indexed abstract (same author, same growth-vs-acceleration imbalance test on (1-L^2)y via recursive residuals, same Monte Carlo claim of high power)", and se-extraction-primary.jsonl retains abstract-derived content ("Journal version per its abstract replaces one-step-ahead forecast errors with recursive residuals - a refinement not verifiable at full-text depth this run"). That corrects the sourcing limb only; the contradiction between the two adjacent assertions stands, and the retained provenance itself both claims verification and flags the refinement as unverifiable.

### LITERATURE-3-1 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** misattributed-claim / withdrawn-claim not propagated
>
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-787
>
> **issue:** The agenda still carries the round-2-withdrawn er-bc-2 recall-gap claim. It states the backward-chase arm "named **two candidates** the frozen corpus does not contain, neither admitted" and lists "`er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited". The review withdrew exactly this claim (LITERATURE-2-1) and its §14 item 7 instructs the consumer that er-bc-2 "must not be transcribed as a recall gap". The agenda also adds a detail the review contradicts: eru-1027 carries "a full deposited abstract of the same NERC model" (review §2.2), so "no abstract deposited" is false as well. The lead's round-2 agenda pass fixed the SCOPE-2-1 staleness ("arm never executed") in the same bullet but did not propagate the er-bc-2 withdrawal, so the agenda now overstates the corpus's named recall gap by 100% (two records instead of one) and asserts a work is missing from the corpus that was in the universe twice and dual-screened out.
>
> **evidence:** Verified independently, not merely against the review: (a) `docs/literature/search_logs/explosive-regime/screen-verdicts-R1.jsonl:209` and `-R2.jsonl:209` record eru-0209 PROMOTE/PROMOTE; `screen2-verdicts-R1.jsonl:73` records EXCLUDE/X7 "working-paper twin of eru-1027"; `screen2-verdicts-R2.jsonl:201` records X6. (b) `screen-verdicts-R1/R2.jsonl:1027` PROMOTE/PROMOTE and `screen2-verdicts-R1.jsonl:364` EXCLUDE/S-c-fail for eru-1027. (c) `references_explosive-regime-dating.json:4436-4438` holds eru-0209 with the title variant "…Bubbles **with** a Near-Explosive Random Coefficient Model", confirming the one-word dedup failure. (d) Crossref for 10.1093/ectj/utaa004 returns Banerjee, Chevillon & Kratz, *The Econometrics Journal* 23(2):297-315, online 2020-02-14 / print 2020-05-01 — the published twin, as the review states. (e) Review §14 item 7 (lines 3653-3661) and protocol amendment A12(b) (protocol lines 1044-1069) both instruct the correction. The review-side correction is propagated at every site checked (abstract lines 167-172, §2.2 lines 296-338, VG-4, VG-12, se-bc-01.json corrections block); only the agenda is stale.
>
> **fix:** Rewrite the agenda bullet to name ONE unadmitted candidate (er-bc-1 Hall, Psaradakis & Sola 1999, DOI 10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X — verified in Crossref as *Journal of Applied Econometrics* 14(2):143-154, and verified absent from `references_explosive-regime-dating.json` by both title and author search), delete the er-bc-2 sub-bullet, and state in its place that er-bc-2 was a false positive dual-screened out as eru-0209/eru-1027 and that the arm's absence test (DOI or exact normalised title) makes "177 absent" an upper bound, per review §14 item 7 and A12(b)-(c).
>
> **reference:** https://doi.org/10.1093/ectj/utaa004 ; https://doi.org/10.1002/(SICI)1099-1255(199903/04)14:2<143::AID-JAE500>3.0.CO;2-X

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted on four independent angles; all failed. Every element of the finding reproduces.
>
> (1) Stale text present, verbatim, at the stated location. `docs/research_notes/research_agenda_regime-classification_2026-08-21.md:779-780` reads "It named **two candidates the frozen corpus does not contain, neither admitted**:" and lines 786-787 read "- `er-bc-2` Banerjee, Chevillon & Kratz 2013 — eligibility indeterminate, no abstract deposited."
>
> (2) Counter-test for a downstream correction elsewhere in the agenda: NEGATIVE. `grep -n "er-bc-2\|Banerjee\|eru-0209\|eru-1027"` over the whole agenda returns exactly one hit — line 786. `grep -n "LITERATURE-2-1"` over the agenda returns zero hits. There is no superseding note, no later revision block, nothing that walks the claim back. The bullet is the agenda's only and final statement on er-bc-2.
>
> (3) Attempted semantic defence — that "frozen corpus" might mean the 72-record included set (which genuinely excludes the work), making the agenda literally true — collapses against the review's own wording. The review uses the identical phrase with the opposite count: abstract lines 166-168, "it named **one** record the corpus does not contain (`er-bc-1`)"; §2.2, "**This is the diagnostic's entire yield of records the corpus does not contain.**" Same phrase, same referent, count one. §14 item 7 (lines 3653-3661) is categorical: "The backward-chase gap the agenda inherits is ONE named record, not two (finding LITERATURE-2-1)" and er-bc-2 "must not be transcribed as a recall gap" — and the agenda bullet sits inside the §Residual completeness-threat paragraph, i.e. exactly a recall-gap transcription. The defence is foreclosed by the source the agenda is supposed to inherit from.
>
> (4) Attempted defence of the "no abstract deposited" detail: also fails. Review §2.2 states eru-1027 (`10.1093/ectj/utaa004`) is "the published version, with a full deposited abstract of the same NERC model." The original diagnostic's own wording was "indeterminate at retrievable depth", not "no abstract deposited", so the agenda additionally hardens a claim the source never made.
>
> Underlying screening evidence reproduced first-hand, not taken on the review's word: `screen-verdicts-R1.jsonl:209` = {"id":"eru-0209","verdict":"PROMOTE"}; `-R2.jsonl:209` = PROMOTE; `screen2-verdicts-R1.jsonl:73` = EXCLUDE / X7 / "working-paper twin of eru-1027"; `screen2-verdicts-R2.jsonl:201` = X6. `screen-verdicts-R1.jsonl:1027` = eru-1027 PROMOTE; `screen2-verdicts-R1.jsonl:364` = EXCLUDE / S-c-fail / "NERC predictive-probability model (ESSEC WP twin); no null-referenced time-t decision". The one-word dedup failure is confirmed at `docs/literature/references_explosive-regime-dating.json:4438`: "Detecting and Forecasting Large Deviations and Bubbles **with** a Near-Explosive Random Coefficient Model". So the work was in the 1,996-record universe twice and dual-screened out on substantive criteria — not missed.
>
> The defect claim is true as stated: the agenda overstates the named backward-chase recall gap as two records where the corrected review says one, and asserts "no abstract deposited" for a work whose published twin carries a full deposited abstract.

### LITERATURE-3-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** work-identity attribution / internal contradiction
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1069-1112 and :3175 (VG-13); docs/methodology/protocol_explosive-regime-review_2026-08-24.md:1122-1147 (A13(b))
>
> **issue:** The round-2 SCOPE-2-3 disclosure of the fourth twin pair (eru-0198 / eru-0259) is self-contradictory and applies a standard inconsistent with the three adjudicated pairs. Within the SAME bullet, line 1072-73 asserts "Twin status was verified against the published article's indexed abstract", while the appended blockquote and VG-13 assert "Same-work identity cannot be settled at the depth available" / "cannot be settled because the journal text was never obtained", and the review "will assert neither it nor its negation". The stated reason for refusing does not distinguish this pair from the ADJUDICATED pair eru-0622/eru-0675, whose journal text was likewise never read (§5.3: "extraction performed once on the WP text, which is the version the journal article derives from"). The review also relies operationally on the identity it declines to assert — eru-0259's numbers are the working paper's numbers, and its ER-RoB row is a pass over eru-0198's document. This is a refusal that dodges a decision its own evidence supports, not a principled abstention.
>
> **evidence:** (a) Review lines 1069-1074 vs lines 1101-1109 and VG-13 (line 3175) — direct contradiction on whether twin status was verified. (b) Protocol A13(b) quotes the project's own primary extraction log: "PROBABLE SAME-WORK TWIN PAIR (eru-0198 WP, eru-0259 journal): **abstracts near-identical** …; titles differ so the section-4.1 title rule does not fire", and `se-extraction-recheck.jsonl` records eru-0198 as `{"twin_of":"eru-0259"}`. (c) Independent check this round: Crossref 10.1016/j.csda.2014.06.006 = Franses (sole author), *Computational Statistics & Data Analysis* 100:160-169, "A simple test for a bubble based on growth and acceleration"; RePEc ems/eureir/39598 = Franses, EI 2013-12, "Are we in a bubble? A simple time-series-based diagnostic", whose abstract is the same construct (imbalance between growth and acceleration; positive first AND second differences; one-step-ahead forecast-error diagnostic; housing/Nikkei applications; Monte Carlo power). Same sole author, same construct, WP 2013-03 → Crossref `created` 2014-06 → print 2016. (d) §5.3's declared twin pair 1 was adjudicated on strictly weaker access (journal text never read either).
>
> **fix:** Reconcile the two sentences. Either (i) withdraw "Twin status was verified against the published article's indexed abstract" as an overstatement, or (ii) adjudicate the pair at the same depth used for the three declared pairs — near-identical abstracts + sole author + WP-to-journal chain — record 68 distinct works with the depth of adjudication stated, and add the twin flag to §5.3's ledger. State explicitly which evidentiary standard governs a twin declaration, since VG-13's stated reason (journal text unobtained) does not distinguish this pair from eru-0622/eru-0675.
>
> **reference:** https://doi.org/10.1016/j.csda.2014.06.006 ; https://ideas.repec.org/p/ems/eureir/39598.html

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Refutation attempted on four fronts; all failed. (1) The internal contradiction reproduces verbatim at the stated location. docs/literature/lit_review_explosive-regime-dating_2026-08-24.md lines 1072-74 read "Twin status was verified against the published article's indexed abstract. Numbers attributed to `eru-0259` are the working-paper's numbers." Lines 1105-07, inside the blockquote appended to that same bullet, read "Same-work identity cannot be settled at the depth available, and this review will assert neither it nor its negation." Line 3175 (VG-13) reads "Same-work identity cannot be settled because the journal text was never obtained (L-10, VG-6)." Nothing in the intervening text withdraws, qualifies, or supersedes the line-1072 sentence; the blockquote opens by calling the pair a "twin candidate that the review never adjudicated" but never retracts the earlier assertion that twin status was verified. A charitable reading that "twin status" means something weaker than same-work identity fails: §5.3 is titled "Three same-work twins inside the frozen included set", so "twin" is that document's term for same-work identity. (2) Protocol A13(b) quotation checks out: docs/methodology/protocol_explosive-regime-review_2026-08-24.md:1126-1137 quotes the primary log's "PROBABLE SAME-WORK TWIN PAIR (eru-0198 WP, eru-0259 journal): abstracts near-identical …; titles differ so the section-4.1 title rule does not fire" and records `se-extraction-recheck.jsonl` `{"twin_of":"eru-0259"}`. I confirmed the underlying logs independently and found evidence the finding did not cite that further supports it: docs/literature/search_logs/explosive-regime/screen2-verdicts-R2.jsonl:11 is a dual-screening verdict `{"id": "eru-0198", "verdict": "EXCLUDE", "criterion": "X7", ... "note": "EI-report WP twin of eru-0259 (CSDA 2014, Franses); same work"}` — one of the project's own screeners already recorded a same-work X7 determination on this pair. (3) The external identity check confirms rather than contradicts the finding. Crossref 10.1016/j.csda.2014.06.006 returns title "A simple test for a bubble based on growth and acceleration", sole author Philip Hans Franses, Computational Statistics & Data Analysis vol. 100, pp. 160-169, issued 2016-08, created 2014-06-11. RePEc ems/eureir/39598 returns "Are we in a bubble? A simple time-series-based diagnostic", Philip Hans Franses, Econometric Institute Research Papers EI 2013-12, 2013, abstract describing the identical construct (unbalance between growth and acceleration, both first and second differences positive before collapse, one-step-ahead forecast-error monitoring test, housing and Nikkei applications, Monte Carlo power). Same sole author, same construct, WP 2013 to Crossref-created 2014-06 to print 2016. (4) The comparability claim to the adjudicated pair holds on the document's own words: §5.3 line 1005 describes the eru-0622/eru-0675 relation as "working-paper twin; extraction performed once on the WP text, which is the version the journal article derives from", i.e. that pair was declared a twin without the journal text having been the extracted document either, so VG-13's stated reason ("the journal text was never obtained") does not distinguish the two cases. The only tension I could find against sub-claim (d) is §5 row 50 (line 891), which labels eru-0675 "full text, dual numeric pass"; that is itself in tension with §5.3's own relation column and does not disturb the finding's primary defect claim. No concrete counter-evidence obtained; the defect claim is true as stated.

### LITERATURE-3-3 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** misstated correction record
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3064-3095 (L-18); repeated at :165? no — at :1957, :2476, :2490, :3058, :3061, :3639, :3830; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:756
>
> **issue:** L-18's headline count is inconsistent with L-18's own table. The claim "Fourteen page locators in §7, §8 and §9 were wrong" is repeated at seven sites in the review and once in the agenda, but the old→new table carries NINETEEN corrected locators (PWY 9: 208→207, 209→208, 211→210, 213→212, 214→213, 215→214, 216→215, 220→219, 221-222→221; PSY 2015a 7: 1048→1047, 1051→1050, 1053→1052, 1054→1053, 1057→1056-1057, 1063→1062, 1067→1066; PSY 2015b 3: 1082→1081, 1083→1082, 1090-1091→1090) plus one row adding locators where none existed (eru-1289 → p.20, p.21). Separately, L-18's prose names "PWY's Table 4 (p.221)" and "all of PSY 2015b's simulation-section locators (pp.1090, …)" as ALREADY CORRECT while the table lists both as changed rows. A remediation whose own defect count is wrong in the under-reporting direction reproduces the round-2 failure mode ("a false claim inside a fix"). All nineteen new locators are in fact applied in the body text (spot-checked at §8.1 lines 1972-1979, §8.2 lines 2006-2013, §7.6 line 1808-1811), so the corrections themselves were made; only the count is wrong.
>
> **evidence:** L-18 table, review lines 3074-3095 (20 rows, 19 with an old→new change). Count claim at lines 1957, 2476, 2490, 3058, 3061, 3064, 3639 and §17 line 3830; agenda line 756 ("corrected 14 locators in the review"). Prose-vs-table conflict at lines 3070-3072 against table rows 3084 and 3094.
>
> **fix:** Recount and restate at all eight sites (19 corrected locators plus one added, or state the counting rule that yields 14 and mark the rows it excludes), and reconcile the "already correct" sentence with rows 3084 and 3094 — a range narrowed to a single page is a correction, not a locator that was already correct.
>
> **reference:** (none stated)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> Could not refute; the defect reproduces exactly.
>
> (1) Table row count. Machine-extracted the old→new columns of the L-18 table at docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3074-3095: 20 data rows, 19 carrying an old→new locator change (PWY 9: 208→207, 209→208, 211→210, 213→212, 214→213, 215→214, 216→215, 220→219, pp.221–222→221; PSY 2015a 7: 1048→1047, 1051→1050, 1053→1052, 1054→1053, 1057→pp.1056–1057, 1063→1062, 1067→1066; PSY 2015b 3: 1082→1081, 1083→1082, pp.1090–1091→1090) plus one row changing "(no locator given)" → p.20, p.21 (eru-1289). The headline "Fourteen" at :3064 does not match 19.
>
> (2) No counting rule rescues 14. Searched the review and docs/methodology/protocol_explosive-regime-review_2026-08-24.md for any stated counting rule ("counting rule", "count excludes", "these fourteen", "nineteen", "twenty") — no hits defining the tally. Tested the only defensible exclusion rules myself: excluding the three range rows whose true page was already inside the cited range (221–222→221, 1057→1056–1057, 1090–1091→1090) yields 16; counting only pure one-page shifts yields 16; counting distinct old page locators yields 19. None yields 14, so the mismatch is not a definitional artifact.
>
> (3) Prose-vs-table conflict confirmed. Lines 3070-3072 state "PWY's Table 4 (p.221) ... and all of PSY 2015b's simulation-section locators (pp.1090, 1092, 1093, Table 4 p.1092) were already correct", while table rows at 3084 (pp.221–222 → p.221) and 3094 (pp.1090–1091 → p.1090) list both as changed.
>
> (4) Repetition sites confirmed by grep: :1957, :2476, :2490, :3058, :3061, :3064, :3639, :3830 (and :3174 in the VG-10 row, "14 wrong page locators" / "14 errors", an eighth review site not listed in the finding), plus docs/research_notes/research_agenda_regime-classification_2026-08-21.md:756 ("corrected 14 locators in the review"). The finding therefore understates the number of affected sites rather than overstating it.
>
> The finding's own concession is also accurate: the corrected locators are applied in the body (e.g. §8.1 line 1974 carries p.213/p.215/p.212, the new values). Only the count and the "already correct" sentence are wrong.

### REPRODUCIBILITY-3-1 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** data_hashed / entrypoint provenance
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3680-3681 (§15 ReproLog + sidecar rows), :3192 (VG-15)
>
> **issue:** The round-2 remediation emitted no ReproLog or sidecar of its own. §15 still cites the round-1 remediation records (`repro_log_a0f236b34b25417cb697df683198b3ef.json`, sidecar `a0f236b3…`) as the provenance record for a document whose content is now the round-2 remediation, and every input those records checksum is a superseded state. VG-15's assertion that this ReproLog is "complete on 13 fields with verified dataset checksums" is, as of the round-2 edits, false. This is a defect introduced by round 2, not a re-raise: round-2's REPRODUCIBILITY-2-2 concerned the earlier-stage log `f5419aa6…`, and the review discloses no staleness in `a0f236b3…`.
>
> **evidence:** ReproLog `a0f236b3…` (mtime 2026-09-02 12:25:21) records `config_resolved_sha256` = `0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b`, which §15:3670 itself labels "protocol SHA-256 with addendum A1–A11 — superseded 2026-09-02 by the round-2 append"; the current protocol hashes to `92fff3f2…`. Its `dataset_checksums` gives `references_explosive-regime.json` = `8ed6f9ca…`, which §15:3676 labels the round-1 state; the current file hashes to `13c76d8f…`. It gives `se-bc-01.json` = `3ea52681…`; the current file (carrying the A12(b) `corrections_2026-09-02` block) hashes to `1b8727dc13e1a16a3a0e239b6115b62e365c0237357be2ea6ea4ba84d17fa3c0`. The sidecar's `stage` field reads "round-1 audit remediation…" and its crossref block still records `year_of_record_convention_divergences: 7`, the figure L-13(e) corrects to 19. Artifact mtimes are 13:39–13:59 on 2026-09-02, i.e. 74–94 minutes after the ReproLog was written, and `ls logs/reproducibility/*.json` shows no later explosive-regime log (the only newer log, `8f5b02d3…` 12:37, is the kalshi-arbitrage run). Both cited digests (`20acd0bc…`, `d2835f07…`) do verify against the files, so the rows are internally consistent and externally stale.
>
> **fix:** Emit a round-2 ReproLog and sidecar with `config_resolved_sha256` = `92fff3f2…`, `dataset_checksums` covering the current `references_explosive-regime.json` (`13c76d8f…`), `se-bc-01.json` (`1b8727dc…`), `se-crossref-recheck-01.json` and `se-fetch-recheck-01.json`, and a `stage` naming the round-2 remediation; repoint §15's two rows at it and retain the round-1 pair as a superseded row. In VG-15, replace "complete on 13 fields with verified dataset checksums" with the accurate statement that the round-1 remediation log is complete on 13 fields but pins pre-round-2 input states.
>
> **reference:** (none stated)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation obtained; every claim in the finding reproduced exactly. (1) logs/reproducibility/repro_log_a0f236b34b25417cb697df683198b3ef.json (mtime 2026-09-02 12:25:21 -0500) records config_resolved_sha256 = 0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b, which the review's own §15:3670 labels "superseded 2026-09-02 by the round-2 append"; sha256sum of the current docs/methodology/protocol_explosive-regime-review_2026-08-24.md = 92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2. (2) Its dataset_checksums pin references_explosive-regime.json = 8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124 (the round-1 state per §15:3676) against a current hash of 13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521, and se-bc-01.json = 3ea526817b3068ab6fbe8f6e38cfb38aa0f1252430ce270ea0cd0b67458c7d0c against a current hash of 1b8727dc13e1a16a3a0e239b6115b62e365c0237357be2ea6ea4ba84d17fa3c0 — byte-identical to the digest the finding asserts. The round-2 logs se-crossref-recheck-01.json and se-fetch-recheck-01.json appear nowhere in dataset_checksums. (3) The sidecar's stage field reads "round-1 audit remediation of lit_review_explosive-regime-dating_2026-08-24" and its crossref block records year_of_record_convention_divergences: 7, while the document's own round-2 entry at line 3845 states L-13(e) is "replaced by a full report: 19 online/print year divergences (not 7)". (4) Artifact mtimes are 13:39:10 (protocol), 13:39:41 (se-bc-01), 13:53:53 (references), 13:57:02 (lit review), 13:59:03 (research agenda) — 74 to 94 minutes after the ReproLog; ls logs/reproducibility/*.json shows exactly one newer log, repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json (12:37), whose dataset_checksums names only references_kalshi-arbitrage.json, so no round-2 explosive-regime ReproLog exists. (5) Both digests cited at §15:3680-3681 verify against the files (20acd0bc95084d4f096e5c2f22922ecf1cb3594e2bd7547cefa2c10c6fe51df7 and d2835f07146e0d4ff1de55891d894ac347e587b271d9301b06c363b9b7004ff9), confirming the rows are internally consistent and externally stale. (6) VG-15 at :3192 does assert the log is "complete on 13 fields with verified dataset checksums", which no longer holds. (7) The finding is not a re-raise and the staleness is undisclosed: grep for "a0f236b3" returns only lines 3176, 3192, 3680, 3754, of which 3176 and 3754 disclose only model_hash: null, while REPRODUCIBILITY-2-2/VG-15 concerns the distinct earlier log f5419aa650e249378ff40828424696bb.json. The one available refutation angle — whether re-emission is required — cuts against refutation: CLAUDE.md's reproducibility contract requires a 13-field ReproLog for every artifact-producing run, and round 2 rewrote five tracked files.

### REPRODUCIBILITY-3-2 — retained

- raised_by: reproducibility-verifier; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false (no `reproduction` block owed); outcome: **retained**

Claim verbatim:

> **category:** data_hashed / cross_platform
>
> **location:** docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:2432, :3215, :3218, :3678, :3679; .gitattributes
>
> **issue:** The two evidence logs created by the round-2 remediation are cited by SHA-256 as the clone-durable carriers of that remediation's findings, but the digests were taken over CRLF working-tree bytes while `.gitattributes` forces `*.json text eol=lf`. Git normalises these files to LF on add, so no consumer of the committed repository — on any platform — can reproduce the published digests. `se-fetch-recheck-01.json` is the sole archived evidence for the LITERATURE-2-2 / QUANT-2-4 correction (the false un-refetchability claim), and `se-crossref-recheck-01.json` is the sole evidence for L-13(e)'s 19 year divergences, so the failure lands on exactly the two claims round 2 was created to substantiate.
>
> **evidence:** Byte counts: `se-crossref-recheck-01.json` CRLF 2609 / LF 2609 (all-CRLF); `se-fetch-recheck-01.json` CRLF 108 / LF 108; `se-bc-01.json` CRLF 1479 / LF 1479. `.gitattributes` line `*.json text eol=lf`; `git check-attr` returns `eol: lf`. `git hash-object -- se-crossref-recheck-01.json` returns `4f69beadf3946f947c33801cc4ae829bce211405`, which equals the SHA-1 of the LF-normalised content and not of the raw CRLF content (`79185c47…`), empirically confirming index normalisation. Recomputed SHA-256 after LF normalisation: `se-crossref-recheck-01.json` → `9457d3de7e3e3e60cc2b5832785b0b8b6da462153a627ddc69e29f72cd77ac9d` (cited: `cb9b0c26…`); `se-fetch-recheck-01.json` → `f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9` (cited: `30b69960…`). By contrast `references_explosive-regime.json` and the protocol are already LF, so §15's store digest and the frozen-prefix check (first 51,478 bytes → `33c01c52…`; full file → `92fff3f2…`, both verified here) are clone-durable.
>
> **fix:** Rewrite the two logs with LF endings before committing and republish the digests as `9457d3de…` and `f93061d1…`, or state at each citation site that the digest is over LF-normalised bytes and publish the LF value. Apply the same normalisation to `se-bc-01.json` and `se-extraction-recheck.jsonl` (the latter is `text: auto`, `eol: unspecified`, so its checkout form is platform-dependent) before any future digest is cited for them.
>
> **reference:** (none stated)

Refutation attempted and failed (`evidence_type: none`); evidence verbatim:

> No refutation. Every claimed fact reproduced independently. (1) .gitattributes contains `*.json text eol=lf`; `git check-attr text eol` returns `text: set` / `eol: lf` for se-crossref-recheck-01.json, se-fetch-recheck-01.json and se-bc-01.json, and `text: auto` / `eol: unspecified` for se-extraction-recheck.jsonl. (2) All three JSON logs are all-CRLF (CR count == LF count: 2609 / 108 / 1479; true byte sizes 65577 / 4675 / 45618 — the finding mislabels the CR/LF counts as "byte counts", a cosmetic slip that does not affect the claim). (3) Digest arithmetic confirmed both ways: se-crossref-recheck-01.json raw-CRLF SHA-256 = cb9b0c26428ee8fc7d7f6b23150e3b8b3c8fc81b90602080b5fa990479172bf2 (the digest published at lines 2847, 3215, 3678) and LF-normalised = 9457d3de7e3e3e60cc2b5832785b0b8b6da462153a627ddc69e29f72cd77ac9d; se-fetch-recheck-01.json raw = 30b6996084d83293f6bebfb4072021e6c60f650880b2d58ab543037465d99253 (published at 2432, 3218, 3679) and LF = f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9. Both recomputations match the auditor exactly. (4) Index normalisation empirically confirmed: `git hash-object` returns 4f69beadf3946f947c33801cc4ae829bce211405 / 394977c5c08327502bc951f58be26ee5be1671fb, `git hash-object --no-filters` returns 79185c47305a97fb5d9218e898fa33101f8d0d75 / 3e02067d9ca33a77937dc61fa76ae491f139af0d, and piping LF-stripped content to `git hash-object --stdin` reproduces the filtered values — so the stored blob is the LF form, not the bytes the published digests cover. Repo core.autocrlf=true, but the eol=lf attribute overrides it on checkout, so no platform recovers the CRLF form. (5) Grep for crlf|line.ending|eol=lf|LF-normal|normalis across all four artifacts returns zero line-ending caveats (all hits concern title/DOI normalisation), so no citation site qualifies the digest. Line 3256 affirmatively presents these logs as tracked by the delivering commit, unlike the ReproLog/sidecar rows which are labelled untracked locators. (6) Scope is correct: references_explosive-regime.json and the protocol are already LF, so the §15 store digest and the frozen-prefix check are unaffected. (7) All three JSON logs are currently absent from `git ls-files`, so normalisation will occur on the delivering `git add`, exactly as predicted. A clone-under-each-core.autocrlf-setting counter-test was attempted but denied by the permission system; the hash-object comparison independently settles the storage form. Nothing found that contradicts the defect claim.

## deferred-logged-minors

Sixteen minors were raised this round and are **logged, not remediated**, per
the loop's standing rule that minors are carried forward unless one is
demonstrably major. They join the 36 minors logged and not remediated across
rounds 1 and 2, giving 52 logged minors over the loop. Because this is the cap
round, none of the sixteen will be re-audited: each is surfaced to the author
here as a standing, disclosed item. Two of them (REV-3-7 and QUANT-3-7) quantify
the sensitivity of the headline O6 figure to the unresolved fourth twin pair and
should be read alongside majors QUANT-3-5 and LITERATURE-3-2; SCOPE-3-4 is a
recorded spec-vs-protocol conflict resolved in the safe direction and is
explicitly not a defect in the delivery. Full unabridged text of each is in the
JSON sidecar under `minors_logged`.

- **REV-3-7** (critical-reviewer, consistency) — §7.6 declares the O6 assessable denominator 'fixed here and used at every site' and derives it as 69 - 4 NE - 2 NS = 63. But the same document makes 69 conditional: VG-13 / A13(b) / frontmatter all say 69-or-68 depending on the unadjudicated `eru-0198`/`eru-0259` pair. Both of those records are coded O6 = RT (§5 rows 4 and 64), so under the 68-work reading the O6 statement becomes 21/62 = 34%, not 22/63 = 35%. The ab …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1793-1802 (§7.6); :109-133 (abstract principal finding 2); :794-802 (§4)  
  *Fix as proposed:* Add one clause at §7.6, at §4's column header and at the abstract's principal finding (2): 'conditional on the fourth pair being two works; if `eru-0198`/`eru-0259` is one work (VG-13, A13(b)) the denominator is 62 and, both records being RT, the figure is 21/ …
- **REV-3-8** (critical-reviewer, standard-coverage) — Review §14 item 3 issues an explicit consumer instruction that the agenda does not discharge: 'Carry the provenance of the qualifier too: "provisional on the working-paper twin" is not in protocol §9.1's frozen verdict vocabulary and is registered as amendment A13(c), and the reason for preferring it over `indeterminate-from-full-text` rests on a declared CONVENTION of §9.3.' The agenda carries the provisional status …  
  *Location:* docs/research_notes/research_agenda_regime-classification_2026-08-21.md:137-149 (Definitional basis (d)); :745-749  
  *Fix as proposed:* Append one sentence at the Definitional-basis (d) NB-13 site: 'The qualifier "provisional on the working-paper twin" is a post-hoc CONVENTION of the review (protocol amendment A13(c)), not a token of protocol §9.1's frozen verdict vocabulary, which leaves `ind …
- **SCOPE-3-2** (scope-auditor, partial) — Second propagation gap opened by the round-2 remediation: the agenda's residual section names the post-hoc amendment set as "A4–A11" and asserts flatly that "72 records are 69 distinct works", while the review as remediated carries A4–A13 and now gives the distinct-work count as 69-or-68 because a fourth, probable, unadjudicated twin pair (eru-0198/eru-0259) is disclosed at VG-13/A13(b). The agenda therefore ships th …  
  *Location:* docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-814  
  *Fix as proposed:* In the agenda residual, replace "A4–A11" with "A4–A13" and add the two round-2 correcting entries in one clause (A12: partial-cell denominator 561 and backward-chase yield 1; A13: twin no-double-counting assurance narrowed, fourth probable twin pair disclosed, …
- **SCOPE-3-3** (scope-auditor, partial) — The agenda's own record of the locator remediation under-declares it and exceeds its warrant. The Verification-status bullet says only "The two Phillips quotation locators this agenda carries were wrong and are fixed", but five distinct locators were changed in the body (PWY quotation 52:214, PWY Table 1 note p.213, PWY divergence convention p.207, PSY quotation 56:1053, PSY Table 1 note p.1050), and the value 1053 i …  
  *Location:* docs/research_notes/research_agenda_regime-classification_2026-08-21.md:750-756 vs 109-118, 500  
  *Fix as proposed:* Restate the agenda bullet as five corrected locators, listing each old→new value against its L-18 row; and either cite the BSADF_r2 definition page from a checked L-18 row or drop the page from those two sites and cite the equation/section instead until the pa …
- **SCOPE-3-4** (scope-auditor, documented-drift) — The declared spec's delegation forbids the review agent to "alter the frozen protocol or its eligibility criteria", while the frozen protocol's own §10 assigns amendment entries to the executing session. Ten amendments (A4–A13) were consequently appended to the protocol file during this session. The conflict is real but resolved in the safe direction and disclosed in detail: §12.5 states that the frozen text above th …  
  *Location:* docs/methodology/protocol_explosive-regime-review_2026-08-24.md (addendum) vs deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:194  
  *Fix as proposed:* Add one clause to the spec's delegation exclusion — "MUST NOT alter the frozen protocol text above its append-only addendum; amendments are appended under protocol §10 by the executing session" — so the constraint and the protocol agree in writing. No change t …
- **QUANT-3-6** (quant-auditor, reporting) — Two agenda statements went stale again during round 2. (a) "Amendments A4–A11 are all post-hoc" — A12 and A13 were appended in the same round and are not named, although A12(b) is the correction QUANT-3-1 turns on and A13(b) is the fourth twin. (b) "three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works" is stated unconditionally, while the review's own abstract, §5.3, §5.4, VG-13 an …  
  *Location:* docs/research_notes/research_agenda_regime-classification_2026-08-21.md:806-813  
  *Fix as proposed:* Change "A4–A11" to "A4–A13" and add one clause naming A12 (er-bc-2 withdrawal, 561 denominator) and A13 (narrowed no-double-counting assurance, fourth probable twin); append "— 68 if the probable unadjudicated eru-0198/eru-0259 pair is one work (VG-13, A13(b)) …
- **QUANT-3-7** (quant-auditor, reporting) — The 68-or-69 conditional is disclosed in the frontmatter, abstract, §5.3, §5.4, VG-13, A13(b) and §12.4 item 5, but not at the two sites where distinct-work counts are actually computed and consumed. §4's header states "72 records but 69 distinct works" flatly and §7.6 explains the two columns as differing "because three records are the same works as three others" with no mention of the fourth pair. The O6 assessable …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:783-795 (§4 header/table), 1783-1836 (§7.6)  
  *Fix as proposed:* Add one sentence to §4's header and to §7.6's synthesis claim: "Under the unresolved eru-0198/eru-0259 pair (VG-13, A13(b)) the distinct-work counts fall by one — O6 becomes RT 21 of 62 = 33.9%, which is still above one in three but by 0.5pp rather than 1.6pp. …
- **QUANT-3-8** (quant-auditor, numerical) — L-18's own parenthetical "(Appendix pp.222–225)" is wrong at the upper end. The PWY appendix runs pp.222–224; the reference list begins on p.224 and continues to p.226.  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3081 (L-18, PWY Table 4 row)  
  *Fix as proposed:* Change "(Appendix pp.222–225)" to "(Appendix pp.222–224; references pp.224–226)".
- **QUANT-3-9** (quant-auditor, reporting) — L-18's third non-locator correction — relabelling the DP 2331 Table 2 quantities from "origination delay" to "mean bias in the estimated bubble origination date … at successful-detection rates 0.84 and 0.75" — was applied at §7.4 and §14 item 2 but not at §7.3 or in the agenda, so the same numbers carry two different labels inside one document. More substantively, both §7.3 and the agenda drop the successful-detectio …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1578-1585 (§7.3 prose); docs/research_notes/research_agenda_regime-classification_2026-08-21.md …  
  *Fix as proposed:* Use one label at all four sites and append "at SDR 0.84 vs 0.75, so the two means are conditioned on different event sets" to §7.3's prose and to the agenda's branch-3 FWER bullet.
- **QUANT-3-10** (quant-auditor, reproducibility) — The 14 corrected locators live only in the review. The extraction log — which the review elsewhere treats as the primitive record and which VG-16 names as the successor's re-derivation source — still carries the superseded page attributions with no pointer to L-18. The frozen-artifact discipline ("no extraction file was touched") is correct, but the round-2 pass did amend the CSL store by note for eru-0198/eru-0259, …  
  *Location:* docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl; L-18  
  *Fix as proposed:* Add one sentence to L-18: "The extraction logs are append-only and are not edited; se-extraction-primary.jsonl still carries the superseded locators, and any locator taken from it must be checked against this table." Optionally mirror the pointer as a note on …
- **LITERATURE-3-4** (literature-check, version-mixed citation / locator not resolvable from the cited identifier) — The FWER triple and origination-bias figures are cited as "`eru-1289` Table 1 p.20, [Shi & Phillips 2022](https://doi.org/10.1017/9781108910095.003)". Those page locators belong to Cowles DP 2331 (31 pages), not to the DOI's target, which Crossref records as a 2025 Cambridge University Press chapter paginated 30-59. A reader following the citation cannot reach p.20, and the year in the link text (2022) is not the DOI …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1634-1636 (§7.4 table), :3603-3605 (§14 item 2)  
  *Fix as proposed:* At each locator site cite the version actually read — Shi & Phillips (2022), Cowles Foundation DP 2331, Table 1 p.20 / Table 2 p.21, with the §9.5 URL and digest — and give the 2025 chapter DOI as the related published version rather than as the locator's targ …
- **LITERATURE-3-5** (literature-check, incomplete disclosure at a section preamble) — §8's preamble says "**Two things did not survive** that re-read" and names the locators and the quotation-marked paraphrase. Three non-locator corrections are recorded elsewhere: the paraphrase, the mis-summarised E9 number ("0.697/0.401", which pairs two unrelated Table 2 cells and omits the maximum GSADF 0.787 at k = 6, T = 100), and the §7.4 FWER row mislabel. The mis-summarised number lives in §8.2 — inside the s …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1956-1959  
  *Fix as proposed:* Change "Two things" to three and name the E9 mis-summary in the preamble alongside the locators and the paraphrase.
- **LITERATURE-3-6** (literature-check, count not propagated) — The 69-or-68 distinct-work conditionality created by VG-13/A13(b) is carried in §5.3, §5.4, §7.6 and VG-13 but not in the abstract's Limitations ("three same-work twins survive X7, so 72 records are 69 distinct works") or in the agenda's residual bullet ("three same-work twin pairs survive X7 deduplication, so 72 records are 69 distinct works"). §17 claims "No number was changed at one site only … grepped across the …  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:174-175 (abstract Limitations); docs/research_notes/research_agenda_regime-classification_2026- …  
  *Fix as proposed:* Append the conditional at both sites ("69 distinct works under the three adjudicated pairs; 68 if the probable fourth pair eru-0198/eru-0259 is one work — VG-13"), or resolve it per LITERATURE-3-2 and state a single number.
- **LITERATURE-3-7** (literature-check, claim falsified by the same pass that made it) — §5.4's fourth-twin blockquote states "neither store entry carries a twin note". The same round-2 pass added exactly such a note to both store entries, and §17 records that edit ("`references_explosive-regime.json`, **notes only** on `eru-0198` and `eru-0259`"). The eru-0259 note now opens "PROBABLE UNADJUDICATED SAME-WORK TWIN of eru-0198".  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:1080-1081  
  *Fix as proposed:* Restate as "neither store entry carried a twin note before this pass; both now carry a probable-twin note", or delete the sentence.
- **LITERATURE-3-8** (literature-check, quantity mis-described in the consumer document) — The agenda says "The FWER-controlled variant buys that back at a delay cost of 7.56 → 12.20 months." L-18 corrected precisely this description in the review: DP 2331 Table 2 reports these as the MEAN BIAS in the estimated bubble origination date, in months, at successful-detection rates falling 0.84 → 0.75. Review §14 item 2 supplied the corrected wording as an explicit agenda input. The agenda took §14 item 6's two …  
  *Location:* docs/research_notes/research_agenda_regime-classification_2026-08-21.md:526-527  
  *Fix as proposed:* Restate as "mean bias in the estimated bubble origination date of 7.56 → 12.20 months, at successful-detection rate 0.84 → 0.75 (DP 2331 Table 2 p.21)".
- **REPRODUCIBILITY-3-3** (reproducibility-verifier, entrypoint_runs) — VG-16 is correctly scoped as repository-level and its core claims verify, but it understates the failure mode: the advertised Quickstart command does not merely find nothing to run, it aborts before pytest is reached. VG-16 also omits that `uv.lock` already resolves the environment locally, which makes the VG-14 remedy a one-command fix rather than an open task.  
  *Location:* docs/literature/lit_review_explosive-regime-dating_2026-08-24.md:3193 (VG-16), :3685 (§15 reproduce-target row)  
  *Fix as proposed:* In VG-16, add that `uv run pytest` currently fails at pyproject parse because `[build-system]` is declared with no `requires` key, so the Quickstart is broken independently of the missing tests; in VG-14, add that `uv.lock` exists and resolves 86 packages, so …

## verification-of-remediations

Round 2's 30 retained majors were all remediated between rounds — 24 by the
librarian in the review, the CSL-JSON store and the protocol addendum, 6 by the
lead in the consumer agenda. This round verified each, and the standing rule was
observed: **no round-1 or round-2 finding that is genuinely fixed was
re-raised.** What the branches confirmed, by the ten claims the brief put to
them:

1. **LITERATURE-2-1 (`er-bc-2` withdrawal).** The correction is right and is
   propagated at every *review-side* site checked — abstract, §2.2, VG-4, VG-12,
   the A11/A12 amendment rows, and a `corrections_2026-09-02` block in
   `se-bc-01.json` restating the arm's yield as one candidate addition. The
   underlying fact was re-derived from primitives, not taken on the review's
   word: `screen-verdicts-R1/R2.jsonl` give `eru-0209` and `eru-1027`
   PROMOTE/PROMOTE at stage 1; `screen2-verdicts-R1.jsonl` gives `eru-0209`
   EXCLUDE/X7 ("working-paper twin of eru-1027") and `eru-1027` EXCLUDE/S-c-fail.
   The one-word title variant that defeated the A11 dedup test was confirmed in
   the universe store. The upper-bound framing of "177 absent" is right, since
   the absence test is DOI-or-exact-normalised-title only. **The single failure
   is downstream:** the withdrawal did not reach the agenda, which is why four
   branches raised it (REV-3-1, SCOPE-3-1, QUANT-3-1, LITERATURE-3-1).
2. **LITERATURE-2-2 / QUANT-2-4 (refetchability and the four content digests).**
   Confirmed. Cowles DP 2331 was re-retrieved this round at the URL §9.5 records,
   591,865 bytes, SHA-256 `309a38ae…` — byte-identical to the recorded digest;
   `p1499.pdf` (`85a984e9…`), `p1349.pdf` (`a35fac94…`) and the three NB texts
   (`d8ae7e69…`, `87277984…`, `9e38c956…`) likewise matched where re-fetched.
   The port diagnosis was independently corroborated (an HTTPS-forcing fetcher
   observed `ECONNREFUSED 128.36.64.198:443` on `korora.econ.yale.edu`). Both
   retained residues are correctly stated in both directions. On the second
   residue the brief asked for an adjudication and the branches split by scope:
   scope-auditor and literature-check judge the un-re-read §9 NB locators an
   **acceptable disclosed residual** (the verdicts turn on what the texts say,
   every quoted string and headline number verified, and the digests reduce the
   remainder to a bounded task); critical-reviewer objects to its **severity**
   (REV-3-5, a scoping objection, not a re-raise); and quant-auditor settled it
   empirically by re-reading all three — NB-08 and NB-13 verify exactly, NB-02's
   three page attributions are wrong (QUANT-3-4). The residual is therefore not
   neutral, and the trail records it as a live, bounded defect.
3. **QUANT-2-3 (14 corrected page locators, L-18).** The corrections themselves
   are applied in the body and spot-verified where a primary text could be
   opened; the non-uniformity of the offset is real. Two defects survive: L-18's
   headline count of "fourteen" does not match its own table of nineteen
   corrected locators plus one added (LITERATURE-3-3), and one L-18 parenthetical
   is wrong at the upper end (QUANT-3-8, minor). The **five agenda locator
   corrections were checked one by one and all five are right** — 52:215→214,
   56:1054→1053 at three sites, PWY Table 1 note 214→213, PSY Table 1 note
   1051→1050, PWY divergence convention 208→207 — each matching L-18's old→new
   row. They are not *complete*: the agenda's own change record declares only two
   of the five, and a sixth locator (PSY 2015a p.1053 for BSADF_r2) is applied at
   two further sites that L-18's table does not cover (SCOPE-3-3, minor).
4. **The three self-found defects.** All three corrections verify against the
   sources. PWY fn. 6 was confirmed verbatim, so §8.1's paraphrase repair is
   right; DP 2331 §5.2 was confirmed verbatim ("over a 10-year period with
   sampling frequencies of quarterly, monthly, and weekly (i.e., T = {40, 120,
   520})"), so the §7.4 FWER row-2 relabel is right and "longer span" was indeed
   wrong; the E9 diagnosis is right, the two paired cells being unrelated. The
   maximum GSADF 0.787 at k = 6, T = 100 could not be independently confirmed
   from an accessible source and remains single-session — and, separately, it was
   recorded at §8.2 and L-18 only and never reached the §7.1 synthesis it bears
   on (REV-3-6).
5. **The O6 denominator.** Arithmetic verifies at both sites: 63 = 69 − 4 NE − 2
   NS, 22/63 = 34.9% → "35%, just over one in three"; the abstract and §7.6 agree
   and the false "fewer than one in three" is gone. The residual is that 63 is
   advertised as fixed while 69 is conditional on the fourth twin pair
   (REV-3-7, QUANT-3-7, minors; the reading survives both branches).
6. **QUANT-2-6 / LITERATURE-2-4 (year divergences).** Verified: 19 online/print
   divergences, the convention contradicted by the review's own labels in 12 of
   them, L-13 narrowed to container title, volume, issue and page range. An
   external Crossref check on `eru-1117` (JFE 21(1):187-227, online 2021-05-05 /
   print 2023-01-19) confirms L-13(e1)'s two-year claim exactly.
7. **SCOPE-2-3 (fourth twin pair) — adjudication requested.** Two branches
   adjudicate the *refusal to decide* as **right, not a dodge**: the criterion is
   decidable, the evidence that would settle it is named, its unavailability is
   recorded, neither identity nor its negation is asserted, and both counts are
   published with their consequence — the honest form of CHAMP's `Unclear`. What
   does not survive is the execution: the same bullet asserts twin status *was*
   verified against the published article's indexed abstract (QUANT-3-5,
   LITERATURE-3-2), the stated ground for refusing does not distinguish this pair
   from the adjudicated pair `eru-0622`/`eru-0675`, and the conditionality does
   not reach the abstract, §4, §7.6 or the agenda.
8. **A12/A13 and the frozen prefix.** Both digest claims were **recomputed
   independently for this trail and both reproduce exactly** (see the front-matter
   notes above). A12 and A13 exist in the append-only addendum, are dated,
   stage-named and post-hoc-flagged, and edit no frozen text.
9. **The lead's six agenda fixes.** Four hold: the arm's post-freeze A11 status
   with `er-bc-1` named as an unadmitted probable eligible miss, the A9/VG-9
   disclosure that none of the three NB records ever entered the screened
   universe, the corpus-scoped O4 claim at the point of claim, and the
   surveillance-line bullet bounded the same way. Two do not: the "A4–A6 → A4–A11"
   correction was itself overtaken by A12/A13 in the same round (REV-3-2), and
   the same bullet retains the withdrawn `er-bc-2` claim (item 1 above).
10. **VG-14/15/16.** All five branches that examined them agree they are
    **correctly scoped as repository-level, not review-level** — each names a
    repository artefact (`pyproject.toml`/`uv.lock`, a prior-stage ReproLog,
    absent `tests/` and `src/`), states that this document does not repair it,
    and gives an author-side remedy. **None is raised as a review defect.** Their
    factual claims were re-derived and hold. One minor refines rather than
    contradicts them (REPRODUCIBILITY-3-3: the Quickstart aborts at a
    `[build-system]` table with no `requires` key before `pytest` is reached, and
    `uv.lock` already resolves 86 packages, so the VG-14 remedy is smaller than
    stated).

Two defects **introduced by the round-2 remediation itself** were found by the
reproducibility branch and are not re-raises: the round-2 pass emitted no
ReproLog or sidecar of its own, so §15 still cites round-1 records that checksum
superseded inputs (REPRODUCIBILITY-3-1), and the two new evidence logs are cited
by digests taken over CRLF working-tree bytes that `git add` normalises to LF,
making them unreproducible from a clone (REPRODUCIBILITY-3-2). The latter's
arithmetic was verified both ways and its index-normalisation claim confirmed by
`git hash-object` with and without filters.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; it does not enumerate. The examined
evidence may not be representative of the artifacts as a whole, and nothing in
this section should be read as assurance about material no branch opened. Every
branch stated the boundary of its own verification, verbatim in the sidecar under
`residual_risks`, and those boundaries are load-bearing here. In particular:
critical-reviewer and literature-check had **no shell**, so neither could compute
any SHA-256 and neither could open a PDF (literature-check's PDF path required an
uninstalled `pdftoppm`); consequently **none of L-18's nineteen page locators was
confirmed at page level by those branches**, only checked for internal
consistency and propagation. Quant-auditor, which could retrieve and parse the
reprints, states that because the same class of error was found in three places
the round-2 re-read had declared clean (§7.3's table attribution, §9.1's NB-02
locators, and L-18's own two entries), **any locator in §7.2, §7.5, §7.8,
§9.2–§9.3 or §10 that it did not sample should be assumed unverified rather than
correct.** The asserted maximum GSADF 0.787 at k = 6, T = 100 remains a
single-session transcription that no branch could independently confirm.
CHAMP items 7–16 were not opened by critical-reviewer (they fall in
quant-auditor's lane, and a statistical branch was routed, so no
`unrouted-analysis` finding arises).

**Residual risk after the cap.** This is the last round; the sixteen retained
majors and sixteen logged minors are surfaced to the author rather than routed
onward. Four residues dominate.

- *Propagation, not error.* Nine of the seventeen majors are propagation
  failures — a correction made correctly at its primary site and not carried to
  every secondary site or to the consumer artifact. This is the third consecutive
  round in which that failure mode produced the largest share of findings, and
  the review's §17 assurance that corrected numbers "were grepped across the
  document" is falsified by REV-3-3, REV-3-6 and LITERATURE-3-6. **A successor
  session must not treat that assurance as evidence.** The single most
  consequential instance is the consumer agenda, which a successor reads in place
  of the review: as it stands it asserts a backward-chase recall gap of two
  records that the review has withdrawn to one, understates the amendment set,
  states the distinct-work count unconditionally, and carries two page locators
  not traceable to L-18's verified table.
- *Substantive conclusions appear unaffected.* Nothing in this round touches the
  review's design (CHAMP 1–6 adequate: the question is answerable by the design,
  the corpus is frozen, the protocol was pre-registered with a provenance commit
  predating execution, and declared departures are amended rather than absorbed).
  On internal evidence the PWY/PSY PARTIAL verdict, the three
  episode-statistic-null adjudications, the O6 distribution, the corpus-scoped O4
  and O5 claims and the failed pooling condition are unmoved by every finding
  here. The O6 headline is nonetheless knife-edge under the unresolved fourth
  twin pair: 22/63 = 34.9% becomes 21/62 = 33.9% against a "one in three"
  threshold of 33.3%.
- *Unverified transcription under the §9 adjudications.* §9's three out-of-corpus
  adjudications rest on single-session transcriptions, one of them additionally
  on a working-paper twin (VG-3). QUANT-3-4 shows this is not hypothetical:
  NB-02 carries three wrong page attributions. If a successor unfreezes anything,
  this is the first thing to re-read, and it is now a bounded task because the
  content digests exist.
- *Evidence tier and reproducibility.* The working-paper tier on the FWER triple
  and the mean-bias figures is the corpus's single most consequential evidential
  weakness for branch 3, and REV-3-4 shows the tier label does not travel
  reliably even inside the review that made the correction. On reproducibility:
  if REPRODUCIBILITY-3-1 is not fixed the delivered review's only provenance
  record checksums a superseded protocol, store and search log and reports a
  crossref count (7) the review itself now gives as 19; if REPRODUCIBILITY-3-2 is
  not fixed, both digests underwriting the round-2 corrections fail for every
  clone consumer — the precise failure digest citation exists to prevent. LLM
  provenance (`model_hash: null`, no temperature, top-p or sampling seed) remains
  open **by design**, is accurately disclosed as VG-11, and is unclosable
  retrospectively, so the screening κ is not re-derivable; that is residual, not
  a defect. Repository-level and outside the review's scope: CLAUDE.md's
  reproducibility contract names `data/_manifest.json` as the dataset-provenance
  carrier and that file does not exist, though the literature stores sit outside
  `data/` and are digest-covered in §15, so nothing this review reports depends
  on it.

## ai-assistance-statement

Per ICMJE Recommendations (updated January 2026) §V.A — AI cannot be an author,
and AI assistance is disclosed. This round section, its findings, refutations and
sidecar were produced with AI assistance under human responsibility:

| stage | model (version) | role | effort |
|---|---|---|---|
| audit — critical-reviewer branch | Claude Opus 5 (`claude-opus-5`) | audit | high |
| audit — scope-auditor branch | Claude Opus 5 (`claude-opus-5`) | audit | medium |
| audit — quant-auditor branch | Claude Opus 5 (`claude-opus-5`) | audit | high |
| audit — literature-check branch | Claude Opus 5 (`claude-opus-5`) | audit | high |
| audit — reproducibility-verifier branch | Claude Opus 5 (`claude-opus-5`) | audit | medium |
| adversarial refute gate | Claude Opus 5 (`claude-opus-5`) | audit | high |
| trail assembly (this section + sidecar) | Claude Opus 5 (`claude-opus-5`) | prose, audit | — |

Orchestration mechanism: `workflows/audit-remediate.js`. Responsible human and
operator: Sajan Koirala; delegation chain as recorded in `acted_on_behalf_of`
above. No AI system is credited as an author of any audited artifact.

**Reproducibility log path.** Per CLAUDE.md §Reproducibility contract, the
ReproLog for this round is written to `logs/reproducibility/repro_log_{run_id}.json`
with the per-run scientific payload at
`artifacts/runs/{HID}/{run_id}/sidecar.json`. Both paths are **gitignored and are
therefore untracked locators, not clone-resolvable paths**; the clone-durable
carriers of their digests are the delivering commit's `Repro-Log-Path:` and
`Repro-Log-SHA256:` trailers, written by `/commit-with-provenance` with
`--role=audit`. The commit hash is to be recorded here as a dated addendum when
it lands. This round's own finding REPRODUCIBILITY-3-1 concerns exactly this
discipline as applied to the audited review, and the note is repeated here so the
trail is not read as exempt from it.

## immutability-and-retention

This round section and its JSON sidecar
([audit_trail_phase2-explosive-review_2026-08-24.round3.json](audit_trail_phase2-explosive-review_2026-08-24.round3.json),
SHA-256 `92e803db1464b1dbac990f125007d524c0f721dbbe46a1664ab8edadb90ecd00`,
holding the round-3 payload verbatim per FAIR I1) are committed to the repository
and are **append-only**, per 21 CFR 11.10(e): record changes must not obscure
previously recorded information. The round-1 and round-2 sections above are
unmodified by this append, and their sidecars are byte-identical, which is why
each round writes a separate sibling sidecar rather than editing an existing one.
This is the cap round, so no further round section will be appended to this file;
**corrections to any recorded entry — including any correction arising from the
sixteen retained majors — are appended as a dated addendum that identifies what
it corrects.** Prior entries are never edited, overwritten, or deleted. Retention
follows the repository's git history; the tracked file is the durable record, and
the front-matter digests bind this section to the exact artifact states audited
(HEAD `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`, `worktree_clean: false`,
per-artifact SHA-256 in the fenced front-matter block above).
