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
title: "Audit trail — Phase 1 gap-targeted sweep, round 1"
type: audit_trail
date: "2026-08-21"
started_at: "2026-08-21T16:02:17-05:00"
ended_at: "2026-08-21T16:07:50-05:00"
artifacts:
  - {path: "docs/literature/lit_review_regime-definitions_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "b561340781d8bc3de3ce0b7aa18b7d1f75414428fe111c4abaff574e8e2e4464"}
  - {path: "docs/literature/lit_review_regime-method-gaps_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "ea0fc5a0ec75a873b626a04545271a5c1938bde2d3f52a970bc5eeebcd97aa66"}
  - {path: "docs/literature/lit_review_f005-class-n-tests_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "c8bcea3a54f46e13cb4cf66615f0db2c7eb0ddba3d4b26c42eba4914f5158e60"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "6e3847e2c5204f4ee8c2bb9869ae01c4826f82b4c46190faab5fd9219e1aa582"}
  - {path: "failure_log.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "c36a4e6eeccf9edef53b8363637201a31b7c46ddb216ced78030d6fa242ae048"}
repo_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    Round 1 audit of the Phase 1 gap-targeted sweep (deliverable_spec_phase1-sweep_2026-08-21.md). Three research-librarian agents produced three scoping records with CSL-JSON stores and search logs: (1) lit_review_regime-definitions (54 records, 59 operational definitions of market regime, PRISMA-ScR partial declared); (2) lit_review_regime-method-gaps (50 records, three targets: assigner null distributions, detector delay/ARL0 operating characteristics, purge/embargo methodology); (3) lit_review_f005-class-n-tests (7 records; Hall & York 2001 and Cheng & Hall 1998 retrieved and read in full; F005 forward-citation search — 3769 identified / 1948 screened — with verdict FOUND: Garzarelli et al. 2014, doi:10.1038/srep04487, is a Class N level existence test, refuting F005's headline claim). The lead session then (4) revised the regime-classification agenda to revision 2, integrating results at five gap sites (Definitional basis paragraph; ER/Benhamou straightness-index analogue; HSMM/Bulla citations; detector-OC canon with refined absence claim; purge/embargo second confirmation + h-block/hv-block grounding; branch-1 calibration blocker resolved with Hall & York's conservative-direction finding; branch-1 prior-art note with the two surviving negatives), and (5) appended the F005 addendum to failure_log.md promoting the layer undetermined -> data under the charter's promotion rule, with the original text retained struck and the transferable positive explicitly weakened. AUDIT FOCUS: (a) citation and claim fidelity of the integrations — does each Rev 2 insertion in the agenda accurately represent what its sweep record establishes (especially: Hall & York conservatism figures 0.000/0.010/0.032/0.102 at nominal 0.01/0.05/0.10/0.20; the Garzarelli test description; the Benhamou straightness-index equivalence; the refined not-absent-but-in-statistics-literature ARL claim); (b) F005 promotion-rule compliance — layer change only on an obtained observation pointing a stated way, original text retained, transferable positive honestly re-argued; (c) PRISMA-ScR declarations honest (single screener, unmet items named); (d) the three gate 'block' verdicts: all are G16 publisher-403 false positives (independently dispositioned with handle-API logs at docs/literature/search_logs/*/g16-*.json — all DOIs responseCode 1) plus one irreducible G13 (Hall & York has no DOI anywhere; carried with archival URL as locator) — verify the dispositions are recorded in the reviews and adopt them; do NOT re-raise publisher-page fetchability findings; (e) internal consistency of the agenda after five insertions (no contradiction between the Definitional basis paragraph and existing branch text; no regression of Rev 1 audit fixes).
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_phase1-sweep_2026-08-21.md", sha256: "cbb67afdfcfdef654fe9ce3c44b8e912f466e0f1d836bf936b0b18771b1747f7"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill)."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-fable-5", effort: "medium", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-fable-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Fable 5, claude-fable-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, literature-check) → adversarial refuter → trail-assembly agent (this document)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. All five artifacts are markdown prose (literature scoping records, a research agenda, and the failure register — no code, no executed statistics), so quant-auditor and epi-auditor were not routed. critical-reviewer (claim fidelity, interpretation, internal consistency) and scope-auditor (deliverable coverage against deliverable_spec_phase1-sweep_2026-08-21.md) are unconditional; literature-check routed on the citation-integration focus of the taskSpec. Efforts: critical-reviewer high, scope-auditor medium, literature-check high."
rounds_completed: 1
rounds_cap: 3
cap_reached: false
verdict: "proceed-with-remediation"
counts: {raw_critical: 0, raw_major: 4, raw_minor: 15, refuted: 0, retained_conservative: 0, to_remediate: 4, minors_logged: 15}
sidecar: {path: "docs/audits/audit_trail_phase1-sweep_2026-08-21.json", sha256: "b2573d31d552e53f6481a9cfd5edb02003d666b2909831ef0a1c3c9b95c9f2c9"}
---

# Audit trail — Phase 1 gap-targeted sweep

Round 1 of the fresh 3-round cap opened by
[deliverable_spec_phase1-sweep_2026-08-21.md](../deliverables/deliverable_spec_phase1-sweep_2026-08-21.md).
Audited artifacts: the three sweep scoping records, the Rev 2
regime-classification agenda, and the failure register (worktree versions at
HEAD `6f16cd55`, uncommitted — `worktree_clean: false`; artifact digests in
the front matter and the JSON sidecar). Branch verdicts: critical-reviewer
proceed-with-remediation, scope-auditor proceed-with-remediation,
literature-check proceed-with-remediation. Union verdict:
**proceed-with-remediation**.

## findings-table

One row per finding; all eight schema fields plus branch and disposition. Text
is verbatim from the branch reports (the sidecar carries the identical payload
in JSON).

| id | severity | category | location | issue | evidence | fix | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-1-1 | major | interpretation | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:160-163; failure_log.md:283-284 | Both Rev 2 integration sites state the surviving CI negative as an unbounded universal — 'no source anywhere reports a confidence interval on a level location' — and rest the branch-1 novelty claim ('first interval on location') on it. The f005 review states this finding in bounded form ('No confidence interval on a level location was found', §9.4 limit 2) and explicitly disclaims the coverage a universal would need: ~1,354 of 1,948 screened titles matched neither keyword net and were not individually read, and 'A NONE-FOUND verdict could not have been asserted on this coverage' (§10 item 2). This reinstates the exact overreach form whose refutation is the subject of the same addendum: F005's headline 'not one Class N definition has ever had its existence tested' was an unbounded universal from bounded search coverage, and it fell to one missed record. | Agenda: '(b) **no source anywhere reports a confidence interval on a level location.** The branch's novelty claim is therefore not "first existence test" but "first existence test under an admissible null, and first interval on location."' — versus f005 review §10.2: 'A NONE-FOUND verdict could not have been asserted on this coverage; the FOUND verdict does not depend on it.' | Rewrite both sites in the bounded form the review itself uses: 'no located source reports a confidence interval on a level location (coverage bound: §10 of the f005 review)', and condition the novelty claim accordingly ('first located interval on location in the searched literature'). Apply the same bounding discipline the addendum applies to negative (a), which correctly says 'no located Class N existence test'. | CHAMP item 30 (conclusions limited to what the analysis supports) / checklist C7; internal precedent: the F005 refutation itself | critical-reviewer | retained → remediate |
| REV-1-2 | major | reporting | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:425-429 | The Rev 2 detector-OC insertion claims BOCPD's delay/ARL0 operating characteristics 'remain substantially uncharacterized — a live gap, not settled ground' while omitting the one directly on-target counter-record the sweep located: Alami, Maillard & Feraud (2020), Restarted BOCPD with detection-delay/false-alarm optimality guarantees (sweep near-miss E1, verification gap V3, OpenAlex W3035594853). The sweep excluded it from the store only for lacking a persistent identifier and explicitly instructed: 'Anyone consuming Target B's verdict should retrieve it manually from PMLR.' The agenda is a consumer of Target B's verdict and does not carry the record or the caveat. An agenda claiming a gap while dropping the nearest located prior art is the same failure pattern the F005 addendum in the same revision documents. | Agenda: 'so BOCPD's operating characteristics on these criteria remain substantially uncharacterized — a live gap, not settled ground.' — versus method-gaps review §8.4: 'The one located work giving a BOCPD-class detector delay/false-alarm guarantees - Alami, Maillard & Feraud (2020), Restarted BOCPD - could not be included: no DOI and no arXiv record exists' and §10 V3: 'Anyone consuming Target B's verdict should retrieve it manually from PMLR.' | Add one sentence to the insertion: theoretical delay/false-alarm optimality guarantees for a restarted BOCPD variant exist (Alami, Maillard & Feraud 2020, PMLR; no persistent identifier — cite by venue and OpenAlex id, tier-flagged), so the residual gap is the empirical delay-vs-ARL0 characterization of BOCPD-class detectors on financial data, not the absence of any characterization. | CHAMP item 21 / SAMPL selective-reporting principle (checklist B4); method-gaps review §8.4, §10 V3 | critical-reviewer | retained → remediate |
| LITERATURE-1-1 | major | citation-metadata / author-list error | C:\Users\skoir\castles\docs\literature\lit_review_f005-class-n-tests_2026-08-21.md:329,446,545; C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:149; C:\Users\skoir\castles\failure_log.md:266 | The decisive F005-refuting record is cited in prose as 'Garzarelli, Cristelli, Zaccaria & Pietronero (2014)' (four authors), but the published version cited by DOI has five authors: Crossref for 10.1038/srep04487 lists Federico Garzarelli, Matthieu Cristelli, Gabriele Pompa, Andrea Zaccaria, Luciano Pietronero. The four-name list is the arXiv:1110.5197 v1 author list (full text was read from arXiv), carried onto the 2014 journal citation. The project's own CSL store (references_f005-class-n-tests.json) correctly includes Pompa, so the prose contradicts the canonical store in all three artifacts. | Crossref works/10.1038/srep04487: authors = Garzarelli, Cristelli, Pompa, Zaccaria, Pietronero (5). arXiv abs/1110.5197: authors = Garzarelli, Cristelli, Zaccaria, Pietronero (4). references_f005-class-n-tests.json lines 43-55 contain family names Garzarelli, ..., Pompa, Zaccaria. All content claims (level definition, 9 LSE stocks/251 days of 2002, timescales 45/60/90/180 s, shuffled-return null ~0.5, chi-squared alpha=0.05 significant at 45-90 s not 180 s) verified correct against the arXiv full text. | Correct the prose author list to Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014) at all cited sites in the f005 review (sections 7, 9.1, 9.4), the agenda branch-1 prior-art note, and the failure_log F005 addendum; where the arXiv version is the read text, note the version/author-list difference explicitly. | https://api.crossref.org/works/10.1038/srep04487; https://arxiv.org/abs/1110.5197 | literature-check | retained → remediate |
| LITERATURE-1-2 | major | misattribution | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:417-420 | The Rev 2 detector-OC insertion attributes to Frisén 2003 the claim that it 'explicitly recasts trading indicators as surveillance stopping rules'. Per the method-gaps sweep itself (section 8.4), that recasting is Bock, Andersson & Frisén (2007), 'The Relation between Statistical Surveillance and Technical Analysis in Finance' (doi:10.1002/9780470987179.ch3) — 'the single located record that does to trading indicators what Target B asks for'. Frisén 2003 (ISR 71:403-434) is the surveillance-optimality taxonomy; its abstract contains no trading-indicator content. | lit_review_regime-method-gaps_2026-08-21.md lines 671-676: 'Frisen (2003) ... taxonomizes the criteria; Bock, Andersson & Frisen (2007) ... explicitly recast technical-analysis indicators as surveillance stopping rules'. Crossref abstract for 10.1111/j.1751-5823.2003.tb00205.x: optimality criteria, likelihood-ratio methods — no recasting of trading indicators. | Reattach the relative clause: cite Frisén 2003 for the evaluation-criteria taxonomy and add Bock, Andersson & Frisén 2007 (doi:10.1002/9780470987179.ch3) as the record that recasts trading indicators as surveillance stopping rules. The refined absence claim itself (framing exists in the statistics literature, q-fin ARL query zero) is faithfully carried and needs no change. | https://api.crossref.org/works/10.1111/j.1751-5823.2003.tb00205.x; lit_review_regime-method-gaps_2026-08-21.md §8.4 | literature-check | retained → remediate |
| REV-1-3 | minor | reporting | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:476-477 | The purge/embargo insertion states 'no purge/embargo-length formal analysis exists', stripping the coverage bound the sweep attaches to its own verdict. The sweep's limitations section states its NONE FOUND verdicts are 'none found in the indexed literature searched', which is weaker than 'none anywhere' — and the sweep additionally records that one platform (Semantic Scholar, q-s2-04) never executed for exactly this target (verification gap V1/V2). | Agenda: '**Rev 2: negative confirmed a second time by the targeted sweep** — no purge/embargo-length formal analysis exists' — versus method-gaps review §10: 'the NONE FOUND verdicts are correspondingly "none found in the indexed literature searched", which is weaker than "none anywhere".' | Change to 'no purge/embargo-length formal analysis was located (second confirmation; coverage bounds and one failed-platform gap in the sweep's §10)'. | Checklist C7 / method-gaps review §10 (V1, V2) | critical-reviewer | deferred — logged minor |
| REV-1-4 | minor | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:417-421 | Misattribution within the ARL insertion: the agenda credits Frisén 2003 as the record 'which explicitly recasts trading indicators as surveillance stopping rules'. Per the sweep, Frisén 2003 'systematizes surveillance evaluation metrics ... the evaluation-frame taxonomy'; the record that 'explicitly recast technical-analysis indicators as surveillance stopping rules and evaluate them by delay and false-alarm properties' is Bock, Andersson & Frisén 2007 (doi:10.1002/9780470987179.ch3), described by the sweep as 'the single located record that does to trading indicators what Target B asks for'. A reader citing Frisén 2003 for the recasting claim cites the wrong source. | Agenda: '(the Frisén "financial surveillance" school, [Frisén 2003](https://doi.org/10.1111/j.1751-5823.2003.tb00205.x), which explicitly recasts trading indicators as surveillance stopping rules)' — versus method-gaps §8.4: 'Bock, Andersson & Frisen (2007) [10.1002/9780470987179.ch3] explicitly recast technical-analysis indicators as surveillance stopping rules'. | Attach the recasting clause to Bock, Andersson & Frisén 2007 (book chapter, tier-flagged BC) and keep Frisén 2003 as the criteria taxonomy, matching the sweep's role assignments. | CHAMP item 22 (reporting fidelity); method-gaps review §7 role column, §8.4 | critical-reviewer | deferred — logged minor |
| REV-1-5 | minor | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:486-487 | Second misattribution: 'Bergmeir & Benítez's evaluations (sweep store) show purging is not always necessary'. Per the sweep, the purging-not-always-necessary result (K-fold CV valid for purely autoregressive fits with uncorrelated errors) belongs to Bergmeir, Hyndman & Koo 2018 (doi:10.1016/j.csda.2017.11.003); Bergmeir & Benítez 2012 is the empirical comparison of blocked/modified CV schemes and does not carry that boundary result. | Agenda: 'Bergmeir & Benítez's evaluations (sweep store) show purging is not always necessary' — versus method-gaps §7: 'Bergmeir, Hyndman & Koo (2018) ... shows standard K-fold CV can be valid for purely autoregressive fits with uncorrelated errors - the boundary of when purging is even necessary.' | Cite Bergmeir, Hyndman & Koo 2018 for the not-always-necessary claim; cite Bergmeir & Benítez 2012 separately (or as 'the Bergmeir line of evaluations, sweep store') for the scheme comparisons. | CHAMP item 22; method-gaps review §7, §8.5 | critical-reviewer | deferred — logged minor |
| REV-1-6 | minor | consistency | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:150-153; failure_log.md:269-271 | Both integration sites describe Garzarelli et al. 2014's construct as a 'path-derived trailing-extremum level'. The f005 review defines it as a 'previous local minimum or maximum of the price series subsampled at timescale tau' with a dispersion-scaled stripe — a Group B path-local-extremum rule — and reserves 'trailing extremum' for the 52-week-high/Donchian D59 family (§9.2), whose admissibility as Class N existence evidence it explicitly leaves as an open taxonomy call for the lead session. The label merges the decisive record with the supporting family and blurs the distinction the review took care to preserve ('only Garzarelli tests the latter'). | failure_log: 'tests a path-derived trailing-extremum level — fully affine-equivariant, Class N' — versus f005 review §9.1: 'A support or resistance is a previous local minimum or maximum of the price series subsampled at timescale tau' and §9.2 heading: 'The 52-week-high family: approach/breach designs at a trailing extremum'. | In both sites, describe Garzarelli's construct as a 'path-derived local-extremum level (previous local min/max at timescale tau, dispersion-scaled stripe)' and keep 'trailing-extremum' for the Driessen/Huddart/Mizrach 52-week-high family only. | f005 review §9.1 vs §9.2 ('Classification honesty' paragraph) | critical-reviewer | deferred — logged minor |
| REV-1-7 | minor | consistency | docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:273-277 and 615-618 | Screening-coverage arithmetic does not reconcile against its stated denominator. Section 4: net 1 matched 396 titles, net 2 a further 75, 471 read individually, 'about 1,354' matched neither net. Section 10 item 2: '~1,354 of 1,948 distinct titles matched neither keyword net'. But 471 + 1,354 = 1,825 — the distinct citing-work count — not 1,948 (the full screened set). Either the nets were applied only to the 1,825 citing titles (making 'of 1,948' the wrong denominator, and leaving the screening depth of the ~123 direct-query records unstated), or the neither-net count over 1,948 should be ~1,477. A number that appears twice must reconcile, and this one bounds the coverage claim behind the surviving negatives. | §4: 'net 1 matched 396 titles, net 2 matched a further 75, and all 471 were read individually ... Titles matching neither net (about 1,354) were screened by the nets only' — §10: '~1,354 of 1,948 distinct titles matched neither keyword net and were not individually read.' 471 + 1,354 = 1,825 ≠ 1,948. | State the actual net-application population (presumably the 1,825 deduplicated citing titles), correct the §10 denominator, and add one sentence on how the ~123 direct-query records were screened. | CHAMP item 19 / PRISMA 2020 16a flow-count consistency | critical-reviewer | deferred — logged minor |
| REV-1-8 | minor | reporting | docs/research_notes/research_agenda_regime-classification_2026-08-21.md:76-78 | Definitional-basis item (f) calls the correlated-Wishart surrogate 'the nearest published analogue to branch 1's random-relocation design' without tier-flagging that the record carrying the explicit Wishart null (D42, arXiv:2003.07058v2) is an unrefereed preprint with 'no refereed version located' per the survey. The agenda applies tier discipline to preprints elsewhere in the same document (Adams & MacKay 'unrefereed preprint'; van den Burg & Williams 'preprint'), so the omission is internally inconsistent; 'published' also overstates 'located'. | Agenda: 'the correlation-state school's correlated-Wishart surrogate is a stated, implemented feature-structure null — the nearest published analogue to branch 1's random-relocation design.' — versus definitions review: 'arXiv:2003.07058v2 \| preprint \| The correlation-state school's explicit Wishart-ensemble null; no refereed version located.' | Add the tier flag: '...a stated, implemented feature-structure null (stated explicitly only in an unrefereed preprint, arXiv:2003.07058; the school's founding record, Münnix et al. 2012, Sci Rep, is peer-reviewed) — the nearest located analogue...'. | CLAUDE.md evidence hierarchy; definitions review §7 tier table and §8.8; agenda's own tier-hazard convention (branch 3) | critical-reviewer | deferred — logged minor |
| REV-1-9 | minor | consistency | failure_log.md:245-252 vs 285-291 | F005's transferable-positive text — 'The testability gap tracks the identification problem, not neglect.' — is contradicted in part by the addendum but retained unstruck in its original position; the weakening lives only in an addendum bullet ~40 lines below. This deviates from the register's own inline-strike convention, applied in the same file at F001 (withdrawn positive shown struck inline) and at F005's own layer line (~~undetermined~~ struck). A reader of the row's top takes a contradicted claim as live. (The unstruck 'Result as reported' headline is acceptable as a historical report of the survey's claim, since the addendum refutes it in the same row.) | F005: '**The testability gap tracks the identification problem, not neglect.**' (unstruck) — versus the F001 precedent in the same file: '**Transferable positive:** **none found.** ~~"volatility remains a live target"~~ (Rev 1, withdrawn)'. | Strike the contradicted sentence inline (retain it, per append-only) and append '(weakened 2026-08-21 — see addendum)'; the addendum's re-argued narrower positive then stands as the live claim. | failure_log Rev 2 convention ('original assignments are shown struck rather than deleted'); prior-disposition register convention | critical-reviewer | deferred — logged minor |
| REV-1-10 | minor | standard-coverage | docs/literature/lit_review_regime-method-gaps_2026-08-21.md:90-95 | PRISMA-ScR item-number slip in the conformance statement: 'no critical appraisal of individual sources was performed (ScR item 16, not met...)'. Critical appraisal of individual sources is item 12 (methods); item 16 is the results-section counterpart ('critical appraisal within sources'). The sibling definitions review's own item table (its §1.4) maps 12 = 'Critical appraisal of individual sources' and 16 = 'Critical appraisal within sources', so the two artifacts disagree on numbering for the same declaration. The declaration itself is honest; only the item citation is off. | method-gaps §1.3: 'no critical appraisal of individual sources was performed (ScR item 16, not met - an evidence tier is recorded per record instead...)' — versus definitions review §1.4 table: '12 Critical appraisal of individual sources \| not applicable, declared ... 16 Critical appraisal within sources \| not applicable'. | Cite 'ScR items 12/16' in the method-gaps conformance statement, matching the definitions review's mapping. | PRISMA-ScR (Tricco et al. 2018, doi:10.7326/M18-0850) item list; declared-standard coverage check | critical-reviewer | deferred — logged minor |
| SCOPE-1-1 | minor | partial | docs/literature/lit_review_regime-definitions_2026-08-21.md:102 | Stale internal definition count: section 1.2 states 'Section 8 numbers definitions D01-D57', but the section 8 synthesis enumerates through D59, and both the agenda frontmatter (line 16, '59 definitions') and the task handoff state 59 definitions. The delivered enumeration does not match its own declared extent. | Line 102: 'Section 8 numbers definitions D01-D57; prior-corpus definitional content is numbered P01-P10' — versus D58 and D59 present at lines 798-799, 905-906, 916, and elsewhere in the synthesis table; agenda supplementary_corpora line 16: '54 records, 59 definitions'. | Correct line 102 to 'D01-D59' (one-line edit in the review). | S-1 | scope-auditor | deferred — logged minor |
| SCOPE-1-2 | minor | partial | docs/audits/ (docs/audits/audit_trail_phase1-sweep_2026-08-21.md absent) | Spec deliverable 6 (WI-3 §2 audit trail for this session, attested) does not yet exist. This is expected sequencing — the trail is produced by the audit round now running — but it is an open spec item that must exist and be attested before the spec can be ticked complete. | deliverable_spec_phase1-sweep_2026-08-21.md lines 57-59: 'docs/audits/audit_trail_phase1-sweep_2026-08-21.md ... check: file exists, written this session, attested.' Glob of docs/audits/ returns only think-tank-charter, round3-remediation, and session_trail files. | Write and attest the phase1-sweep audit trail before closing the session; verify at spec-tick time. | S-6 | scope-auditor | deferred — logged minor (satisfied by this document; see verification section) |
| SCOPE-1-3 | minor | partial | git HEAD (spec deliverable 7) | Spec deliverable 7 (commit via /commit-with-provenance with Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance trailers, role=multi) has not yet been made — the sweep artifacts are uncommitted at audit time. Expected sequencing (commit is the spec's final step) but an open item. | deliverable_spec_phase1-sweep_2026-08-21.md lines 61-64; git status at session start shows the most recent commit is 57b409c (pre-sweep) and the new literature/agenda artifacts are not in a provenance commit. | Complete the /commit-with-provenance step after remediation and trail attestation; verify trailers with git log -1. | S-7 | scope-auditor | deferred — logged minor |
| LITERATURE-1-3 | minor | construct misdescription | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:150-151; C:\Users\skoir\castles\failure_log.md:268-270 | Garzarelli's tested construct is described as 'a path-derived trailing-extremum level'. The sweep record defines it as previous local minima/maxima of the price subsampled at timescale tau with a dispersion-scaled stripe (Group B path-extremum rule), and reserves 'trailing-window path extremum' for the Donchian/52-week-high D59 family (Driessen, Huddart, Mizrach). The descriptor conflates the two designs and dilutes the sweep's explicit 'classification honesty' distinction (only Garzarelli tests bounce-vs-cross deflection; the 52-week-high family tests behaviour at a defined location). Class N membership — the load-bearing claim — is correct for both. | lit_review_f005-class-n-tests_2026-08-21.md §9.1: 'a previous local minimum or maximum of the price series subsampled at timescale tau... not identical to any of the survey's 76 numbered definitions'; §9.2: 'The 52-week high/low is the trailing-window path extremum — the Donchian-type construct the survey files as D59'; §9.2 closing: 'only Garzarelli tests the latter'. arXiv:1110.5197 confirms the local-extremum definition. | In the agenda and failure_log addendum, replace 'trailing-extremum level' with 'local-extremum level (previous local minima/maxima at timescale tau with dispersion-scaled stripe)' for Garzarelli, and keep 'trailing-extremum' for the Driessen/Huddart/Mizrach boundary records; optionally restate the deflection-vs-behaviour distinction in one clause. | lit_review_f005-class-n-tests_2026-08-21.md §9.1-9.2 | literature-check | deferred — logged minor |
| LITERATURE-1-4 | minor | misattribution (within author cluster) | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:486-487 | The purge/embargo insertion states 'Bergmeir & Benítez's evaluations (sweep store) show purging is not always necessary — its length is a testable quantity'. The sweep attributes that specific result (standard K-fold CV can be valid for purely autoregressive fits with uncorrelated errors) to Bergmeir, Hyndman & Koo 2018 (doi:10.1016/j.csda.2017.11.003); Bergmeir & Benítez 2012 (doi:10.1016/j.ins.2011.12.028) is the blocked/modified-CV empirical comparison. | lit_review_regime-method-gaps_2026-08-21.md lines 710-712 and store row bergmeir2018jcsda2017110: 'K-fold CV can be valid for purely autoregressive fits - purging is not always necessary, so its length is a testable quantity, not a dogma' attached to Bergmeir, Hyndman & Koo (2018). | Cite 'Bergmeir, Hyndman & Koo 2018 (with Bergmeir & Benítez 2012 as the empirical comparison)' or rephrase to 'the Bergmeir-line evaluations' with both DOIs. | lit_review_regime-method-gaps_2026-08-21.md §8.5 | literature-check | deferred — logged minor |
| LITERATURE-1-5 | minor | evidence-tier omission | C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:76-78 | Definitional-basis item (f) calls the correlated-Wishart surrogate 'the nearest published analogue to branch 1's random-relocation design' with no tier label. The defining source of that null (D42) is arXiv:2003.07058v2, a preprint with 'no refereed version located' per the survey's own tier table. The agenda flags preprint tier elsewhere (Adams & MacKay BOCPD 'Tier hazard'), so the omission is inconsistent with its own practice and 'published' overstates the tier. | lit_review_regime-definitions_2026-08-21.md line 772 and 812: 'arXiv:2003.07058v2 \| **PREPRINT** ... no refereed version located'; §8.8 conclusion names D42 as the stated-and-implemented Wishart null. | Append a tier qualifier: '(stated and implemented in a preprint-tier source, arXiv:2003.07058; no refereed version located)'. | lit_review_regime-definitions_2026-08-21.md §7/§8.8 | literature-check | deferred — logged minor |
| LITERATURE-1-6 | minor | internal consistency (register) | C:\Users\skoir\castles\failure_log.md:297-301 | The 'Column health check' still reads 'Current state — 2 transfers found, 2 "none found"', which counts only F001-F004. After the F005 addendum the register has five rows and F005 carries a weakened-but-surviving transferable positive, so the standing check mandated by charter step 4 is stale in the same file that was edited this session. | failure_log.md line 300 vs the F005 'Transferable positive — WEAKENED' block at lines 285-291 added by the same revision. | Update the tally to include F005 (e.g. '3 transfers found, of which 1 weakened by its discriminating observation; 2 none found') or scope the check explicitly to a stated window. | charter step 4 standing check, failure_log.md | literature-check | deferred — logged minor |

Counts (verbatim from the round payload): raw_critical 0, raw_major 4,
raw_minor 15, refuted 0, retained_conservative 0, to_remediate 4,
minors_logged 15.

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Four dispositions,
all **retained** after failed refutation attempts; zero findings were dropped
(refuted: 0). No entry carries `reproduction_required: true`, so no
`reproduction: {command, observed}` blocks are owed. There are no
retained-conservative entries this round (retained_conservative: 0). Claims
are given verbatim, unabridged.

### REV-1-1 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:160-163; failure_log.md:283-284
> **issue:** Both Rev 2 integration sites state the surviving CI negative as an unbounded universal — 'no source anywhere reports a confidence interval on a level location' — and rest the branch-1 novelty claim ('first interval on location') on it. The f005 review states this finding in bounded form ('No confidence interval on a level location was found', §9.4 limit 2) and explicitly disclaims the coverage a universal would need: ~1,354 of 1,948 screened titles matched neither keyword net and were not individually read, and 'A NONE-FOUND verdict could not have been asserted on this coverage' (§10 item 2). This reinstates the exact overreach form whose refutation is the subject of the same addendum: F005's headline 'not one Class N definition has ever had its existence tested' was an unbounded universal from bounded search coverage, and it fell to one missed record.
> **evidence:** Agenda: '(b) **no source anywhere reports a confidence interval on a level location.** The branch's novelty claim is therefore not "first existence test" but "first existence test under an admissible null, and first interval on location."' — versus f005 review §10.2: 'A NONE-FOUND verdict could not have been asserted on this coverage; the FOUND verdict does not depend on it.'
> **fix:** Rewrite both sites in the bounded form the review itself uses: 'no located source reports a confidence interval on a level location (coverage bound: §10 of the f005 review)', and condition the novelty claim accordingly ('first located interval on location in the searched literature'). Apply the same bounding discipline the addendum applies to negative (a), which correctly says 'no located Class N existence test'.
> **reference:** CHAMP item 30 (conclusions limited to what the analysis supports) / checklist C7; internal precedent: the F005 refutation itself

Refutation evidence:

> Refutation attempt failed; every quoted element reproduces exactly. Agenda lines 160-163 and failure_log lines 283-284 both state the universal "no source anywhere reports a confidence interval on a level location." The f005 review states the same negative only in bounded form (section 9.4 limit 2: "No confidence interval on a level location was found... survives this search") and section 10 item 2 explicitly disclaims the coverage a universal would need ("~1,354 of 1,948 distinct titles matched neither keyword net and were not individually read. A NONE-FOUND verdict could not have been asserted on this coverage"). The adjacent negative (a) at both sites is correctly bounded ("no located Class N existence test"), showing the universal phrasing of (b) is a genuine overreach, not a paraphrase convention. Finding stands.

### REV-1-2 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/research_notes/research_agenda_regime-classification_2026-08-21.md:425-429
> **issue:** The Rev 2 detector-OC insertion claims BOCPD's delay/ARL0 operating characteristics 'remain substantially uncharacterized — a live gap, not settled ground' while omitting the one directly on-target counter-record the sweep located: Alami, Maillard & Feraud (2020), Restarted BOCPD with detection-delay/false-alarm optimality guarantees (sweep near-miss E1, verification gap V3, OpenAlex W3035594853). The sweep excluded it from the store only for lacking a persistent identifier and explicitly instructed: 'Anyone consuming Target B's verdict should retrieve it manually from PMLR.' The agenda is a consumer of Target B's verdict and does not carry the record or the caveat. An agenda claiming a gap while dropping the nearest located prior art is the same failure pattern the F005 addendum in the same revision documents.
> **evidence:** Agenda: 'so BOCPD's operating characteristics on these criteria remain substantially uncharacterized — a live gap, not settled ground.' — versus method-gaps review §8.4: 'The one located work giving a BOCPD-class detector delay/false-alarm guarantees - Alami, Maillard & Feraud (2020), Restarted BOCPD - could not be included: no DOI and no arXiv record exists' and §10 V3: 'Anyone consuming Target B's verdict should retrieve it manually from PMLR.'
> **fix:** Add one sentence to the insertion: theoretical delay/false-alarm optimality guarantees for a restarted BOCPD variant exist (Alami, Maillard & Feraud 2020, PMLR; no persistent identifier — cite by venue and OpenAlex id, tier-flagged), so the residual gap is the empirical delay-vs-ARL0 characterization of BOCPD-class detectors on financial data, not the absence of any characterization.
> **reference:** CHAMP item 21 / SAMPL selective-reporting principle (checklist B4); method-gaps review §8.4, §10 V3

Refutation evidence:

> Evidence reproduced, not refuted. (1) Agenda lines 425-429 contain the quoted 'remain substantially uncharacterized — a live gap, not settled ground' claim. (2) Grep of the agenda for 'Alami|W3035594853|Restarted' returns zero matches — the counter-record and V3 caveat are absent. (3) Method-gaps review lines 662-666 (§8.4) and 751-754 (V3) contain the cited counter-record text verbatim, including 'Anyone consuming Target B's verdict should retrieve it manually', and the E1 exclusion row (line 482) marks Alami, Maillard & Feraud (2020) as 'Directly on-target for B'. The sweep's own Target B verdict is 'PARTIALLY FOUND', which the agenda's unqualified gap framing omits. The defect claim stands.

### LITERATURE-1-1 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** citation-metadata / author-list error
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_f005-class-n-tests_2026-08-21.md:329,446,545; C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:149; C:\Users\skoir\castles\failure_log.md:266
> **issue:** The decisive F005-refuting record is cited in prose as 'Garzarelli, Cristelli, Zaccaria & Pietronero (2014)' (four authors), but the published version cited by DOI has five authors: Crossref for 10.1038/srep04487 lists Federico Garzarelli, Matthieu Cristelli, Gabriele Pompa, Andrea Zaccaria, Luciano Pietronero. The four-name list is the arXiv:1110.5197 v1 author list (full text was read from arXiv), carried onto the 2014 journal citation. The project's own CSL store (references_f005-class-n-tests.json) correctly includes Pompa, so the prose contradicts the canonical store in all three artifacts.
> **evidence:** Crossref works/10.1038/srep04487: authors = Garzarelli, Cristelli, Pompa, Zaccaria, Pietronero (5). arXiv abs/1110.5197: authors = Garzarelli, Cristelli, Zaccaria, Pietronero (4). references_f005-class-n-tests.json lines 43-55 contain family names Garzarelli, ..., Pompa, Zaccaria. All content claims (level definition, 9 LSE stocks/251 days of 2002, timescales 45/60/90/180 s, shuffled-return null ~0.5, chi-squared alpha=0.05 significant at 45-90 s not 180 s) verified correct against the arXiv full text.
> **fix:** Correct the prose author list to Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014) at all cited sites in the f005 review (sections 7, 9.1, 9.4), the agenda branch-1 prior-art note, and the failure_log F005 addendum; where the arXiv version is the read text, note the version/author-list difference explicitly.
> **reference:** https://api.crossref.org/works/10.1038/srep04487; https://arxiv.org/abs/1110.5197

Refutation evidence:

> Refutation attempt failed; every element of the finding independently reproduced. (1) grep confirms the four-name list 'Garzarelli, Cristelli, Zaccaria & Pietronero' at lit_review_f005-class-n-tests_2026-08-21.md:329,446,545, research_agenda_regime-classification_2026-08-21.md:149, and failure_log.md:266. (2) Crossref works/10.1038/srep04487 returns five authors: Federico Garzarelli, Matthieu Cristelli, Gabriele Pompa, Andrea Zaccaria, Luciano Pietronero. (3) arXiv abs/1110.5197 is v1-only (24 Oct 2011) with exactly the four-name list, consistent with the auditor's provenance account. (4) docs/literature/references_f005-class-n-tests.json lines 41-62 (id garzarelli2014srep04487) contains all five authors including Pompa, so the prose contradicts the project's canonical CSL store. The finding stands.

### LITERATURE-1-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: none; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** misattribution
> **location:** C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:417-420
> **issue:** The Rev 2 detector-OC insertion attributes to Frisén 2003 the claim that it 'explicitly recasts trading indicators as surveillance stopping rules'. Per the method-gaps sweep itself (section 8.4), that recasting is Bock, Andersson & Frisén (2007), 'The Relation between Statistical Surveillance and Technical Analysis in Finance' (doi:10.1002/9780470987179.ch3) — 'the single located record that does to trading indicators what Target B asks for'. Frisén 2003 (ISR 71:403-434) is the surveillance-optimality taxonomy; its abstract contains no trading-indicator content.
> **evidence:** lit_review_regime-method-gaps_2026-08-21.md lines 671-676: 'Frisen (2003) ... taxonomizes the criteria; Bock, Andersson & Frisen (2007) ... explicitly recast technical-analysis indicators as surveillance stopping rules'. Crossref abstract for 10.1111/j.1751-5823.2003.tb00205.x: optimality criteria, likelihood-ratio methods — no recasting of trading indicators.
> **fix:** Reattach the relative clause: cite Frisén 2003 for the evaluation-criteria taxonomy and add Bock, Andersson & Frisén 2007 (doi:10.1002/9780470987179.ch3) as the record that recasts trading indicators as surveillance stopping rules. The refined absence claim itself (framing exists in the statistics literature, q-fin ARL query zero) is faithfully carried and needs no change.
> **reference:** https://api.crossref.org/works/10.1111/j.1751-5823.2003.tb00205.x; lit_review_regime-method-gaps_2026-08-21.md §8.4

Refutation evidence:

> Refutation attempt failed; finding confirmed by primary sources. (1) Agenda lines 418-420 attach "which explicitly recasts trading indicators as surveillance stopping rules" solely to the Frisen 2003 citation. (2) Crossref record for 10.1111/j.1751-5823.2003.tb00205.x confirms Frisen 2003 is "Statistical Surveillance. Optimality and Methods" (ISR); its abstract covers optimality criteria and likelihood-ratio methods only — no trading-indicator content. (3) Crossref record for 10.1002/9780470987179.ch3 confirms Bock, Andersson & Frisen 2007, "The Relation between Statistical Surveillance and Technical Analysis in Finance", is the recasting work, matching method-gaps sweep section 8.4 (lines 671-676). The only counter-reading (relative clause attaching to "the Frisen school" rather than the citation) still leaves Frisen 2003 as the sole cited support for the recasting claim, so it does not overturn the misattribution.

## deferred-logged-minors

Fifteen minors deferred to the remediation backlog, logged here (full schema
fields in the findings table and the sidecar):

- REV-1-3 (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:476-477) — The purge/embargo insertion states 'no purge/embargo-length formal analysis exists', stripping the coverage bound the sweep attaches to its own verdict.
- REV-1-4 (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:417-421) — Misattribution within the ARL insertion: the agenda credits Frisén 2003 as the record 'which explicitly recasts trading indicators as surveillance stopping rules'.
- REV-1-5 (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:486-487) — Second misattribution: 'Bergmeir & Benítez's evaluations (sweep store) show purging is not always necessary'.
- REV-1-6 (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:150-153; failure_log.md:269-271) — Both integration sites describe Garzarelli et al.
- REV-1-7 (critical-reviewer; docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:273-277 and 615-618) — Screening-coverage arithmetic does not reconcile against its stated denominator.
- REV-1-8 (critical-reviewer; docs/research_notes/research_agenda_regime-classification_2026-08-21.md:76-78) — Definitional-basis item (f) calls the correlated-Wishart surrogate 'the nearest published analogue to branch 1's random-relocation design' without tier-flagging that the record carrying the explicit Wishart null (D42, arXiv:2003.07058v2) is an unrefereed preprint with 'no refereed version located' per the survey.
- REV-1-9 (critical-reviewer; failure_log.md:245-252 vs 285-291) — F005's transferable-positive text — 'The testability gap tracks the identification problem, not neglect.' — is contradicted in part by the addendum but retained unstruck in its original position; the weakening lives only in an addendum bullet ~40 lines below.
- REV-1-10 (critical-reviewer; docs/literature/lit_review_regime-method-gaps_2026-08-21.md:90-95) — PRISMA-ScR item-number slip in the conformance statement: 'no critical appraisal of individual sources was performed (ScR item 16, not met...)'.
- SCOPE-1-1 (scope-auditor; docs/literature/lit_review_regime-definitions_2026-08-21.md:102) — Stale internal definition count: section 1.2 states 'Section 8 numbers definitions D01-D57', but the section 8 synthesis enumerates through D59, and both the agenda frontmatter (line 16, '59 definitions') and the task handoff state 59 definitions.
- SCOPE-1-2 (scope-auditor; docs/audits/ (docs/audits/audit_trail_phase1-sweep_2026-08-21.md absent)) — Spec deliverable 6 (WI-3 §2 audit trail for this session, attested) does not yet exist.
- SCOPE-1-3 (scope-auditor; git HEAD (spec deliverable 7)) — Spec deliverable 7 (commit via /commit-with-provenance with Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance trailers, role=multi) has not yet been made — the sweep artifacts are uncommitted at audit time.
- LITERATURE-1-3 (literature-check; C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:150-151; C:\Users\skoir\castles\failure_log.md:268-270) — Garzarelli's tested construct is described as 'a path-derived trailing-extremum level'.
- LITERATURE-1-4 (literature-check; C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:486-487) — The purge/embargo insertion states 'Bergmeir & Benítez's evaluations (sweep store) show purging is not always necessary — its length is a testable quantity'.
- LITERATURE-1-5 (literature-check; C:\Users\skoir\castles\docs\research_notes\research_agenda_regime-classification_2026-08-21.md:76-78) — Definitional-basis item (f) calls the correlated-Wishart surrogate 'the nearest published analogue to branch 1's random-relocation design' with no tier label.
- LITERATURE-1-6 (literature-check; C:\Users\skoir\castles\failure_log.md:297-301) — The 'Column health check' still reads 'Current state — 2 transfers found, 2 "none found"', which counts only F001-F004.

## verification-of-remediations

**Predecessor-round fixes, verified this round.** literature-check confirms no
Rev 1 audit fix (F-3-1/3/10/11) regressed in Rev 2; critical-reviewer confirms
the sweep's design validly discharges F005's discriminating observation, the
charter promotion rule was followed with honest sharpening (layer change on an
obtained observation pointing the stated way; original text retained struck;
transferable positive re-argued against interest), and every quantitative
figure checked (Hall & York table values, flow counts, definition counts)
reconciles except the REV-1-7 arithmetic defect. All three branches adopted
the recorded G16 publisher-403 dispositions (handle-API logs at
docs/literature/search_logs/*/g16-*.json, all DOIs responseCode 1) and the one
irreducible G13 (Hall & York, no DOI anywhere, archival URL as locator); no
publisher-page fetchability finding was re-raised. PRISMA-ScR
partial-compliance declarations in all three sweep records were verified
honest: single screener, unmet items named per item, keyword-net coverage
limit stated.

**This round's remediations (REV-1-1, REV-1-2, LITERATURE-1-1,
LITERATURE-1-2): pending at trail-writing time.** The round verdict is
proceed-with-remediation; remediation follows this trail. SCOPE-1-2 (minor) is
discharged by the existence of this document
(`docs/audits/audit_trail_phase1-sweep_2026-08-21.md`, written this session
per the skill's post-loop field spec). SCOPE-1-3 (minor) is discharged when
the /commit-with-provenance step lands; its trailer-bearing commit hash is to
be recorded here as a dated addendum. Verification evidence for the four
majors (post-fix artifact digests and, if a round 2 runs, the round-2 branch
confirmations) is to be appended as the next round section of this file —
prior entries are never edited.

**Undeclared-edit note (per scope-auditor).** failure_log.md's "Column health
check" paragraph (lines 296-301) was updated this session as a consequence of
the F005 transferable-positive weakening, while the spec scopes the
failure_log deliverable to "F005 row update" only. The edit is
charter-mandated maintenance consistent with the addendum — recorded here as
scope-auditor requested, not raised as scope creep; its staleness relative to
the five-row register is separately logged as LITERATURE-1-6.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Three specialist branches read five artifacts against the
phase1-sweep spec, the standing dispositions, and the cited primary sources;
they did not exhaustively verify every sentence, every citation-claim pairing,
every store record, or every cross-artifact dependency. Absence of a finding
is not evidence of absence of a defect — the same asymmetry the charter
enforces for statistical nulls applies to this audit's coverage.

Per-branch residual-risk statements, verbatim:

**critical-reviewer:** RQI coverage: importance covered (the sweep answers three recorded gaps plus a registered discriminating observation — adequate); originality covered (the F005 refutation narrows the novelty claim honestly, but the surviving novelty claim inherits REV-1-1's unbounded form); method, presentation, and interpretation covered by the findings above. Residual risks after remediation: (1) The level-definitions survey — outside this artifact set — still asserts the refuted headline and the '16 tested, 60 untested' §8.6.6 tally with no supersession marker; the f005 review's recommendation (iv) explicitly assigned the erratum decision to the lead session and no decision is recorded anywhere in the shipped set. This is promised-vs-shipped ground (scope-auditor) but it leaves a tracked document contradicting the register until routed. (2) Three of the four Class-N prior-art records (Driessen, Huddart, Mizrach) and the Li-Luo-Xiao working paper were adjudicated on abstracts only — declared, but the agenda's 'supporting peer-reviewed evidence' sentence inherits abstract-depth confidence; literature-check should prioritize these. (3) N6 'Faulty Anchors' (ssrn.3021585) remains unadjudicable and could add a further Class-N record, which would touch the 52-week-high boundary discussion but not the FOUND verdict. (4) All NONE-FOUND verdicts across the three sweeps are coverage-bounded (failed S2 queries, net-bounded citing-title screening, no book-index search); any downstream deliverable quoting them must carry the bound — REV-1-1 and REV-1-3 are the two places Rev 2 dropped it. (5) The method-gaps and definitions reviews cite only a reproducibility-log directory rather than the ReproLog SHA-256 the project contract requires; deferred to reproducibility-verifier. No critical finding: the design of the sweep validly discharges F005's discriminating observation, the promotion rule was followed with honest sharpening, and every quantitative figure checked (Hall & York table values, flow counts, definition counts) reconciles except the one arithmetic defect in REV-1-7.

**scope-auditor:** Spec source used: docs/deliverables/deliverable_spec_phase1-sweep_2026-08-21.md (precedence 1); no conflict found between it and the task spec passed by the loop. Three risks remain unverified within this branch's read-only means. (1) The S-4 check 'no existing citation removed' from the agenda could not be independently verified without a git diff of Rev 1 vs Rev 2; the revision note asserts additive-only integration but a silent deletion would be invisible to file inspection alone — a diff-based confirmation at commit time would close this. (2) The S-1 check 'every included record resolves to a store entry' was verified at the aggregate level only (54 store ids == n_included 54, matching counts for the other two stores at 50 and 7); per-record resolution of all 111 entries was not enumerated, which sits in tension with the standing F-5 disposition against aggregate-only verification — a deterministic script check at spec-tick time is the cheap closure. (3) failure_log.md's 'Column health check' paragraph (lines 296-301, '2 transfers found, 2 none found... Rev 1 was 4-for-4') appears to have been updated this session as a consequence of the F005 transferable-positive weakening; the spec scopes the failure_log deliverable to 'F005 row update' only. The edit is charter-mandated maintenance and consistent with the addendum, so it is not raised as a scope-creep finding, but it is undeclared in the spec and should be mentioned in the trail. Correctness of the integrated claims (Hall & York figures, Garzarelli test description, Benhamou equivalence, ARL claim refinement) is outside this branch's scope and is left to the sibling auditors.

**literature-check:** Verified 17 external citations against primary sources (Crossref, arXiv full text, publisher pages) plus the three sweep records as internal sources; all year/venue/volume/page metadata exact except the Garzarelli author list (finding 1-1). Residual gaps, none blocking: (1) Hall & York 2001 Table 1's exact quadruple 0.000/0.010/0.032/0.102 could not be independently re-extracted — both open PDFs (Statistica Sinica A11n28.pdf, 275.9KB matching the review's 282,488-byte record, and the Cheng & Hall self-archive) downloaded but this environment lacks PDF text extraction (pdftoppm unavailable); the direction (conservative), the lambda(alpha) polynomial+Monte-Carlo calibration form, the j=1-only scope, and the Cheng-Hall d=|f''(x0)|/f(x0)^3 constant were independently corroborated via the publisher abstract page and the Ameijeiras-Alonso et al. survey (arXiv:1609.05188), so the figures rest on two concordant in-project full-text readings of a pinned open source. (2) Driessen/Huddart/Mizrach remain abstract-verified and Li-Luo-Xiao abstract-only tier-5, exactly as the f005 review itself declares — carried, not new. (3) SSRN 3021585 ('Faulty Anchors') remains unadjudicable, flagged by the review. (4) Kaufman ER book attribution (1987/1995 editions) remains unverifiable in DOI-indexed sources; the agenda already labels it as needing a licensed copy. G16 publisher-403 and G13 Hall-&-York-no-DOI dispositions were checked (handle-API log shows responseCode 1 for all 6 store DOIs) and adopted per standing disposition; not re-raised. PRISMA-ScR partial-compliance declarations in all three sweep records are honest: single screener, unmet items named per item, keyword-net coverage limit stated. F005 promotion complies with the charter rule: observation obtained, points to the enumerated 'data' alternative, original layer retained struck, transferable positive re-argued against interest. No Rev 1 audit fix (F-3-1/3/10/11) regressed in Rev 2.

**Prior dispositions carried into this round** (verbatim from the round
payload): This is round 1 for the phase1-sweep spec (fresh cap). Standing project dispositions that bind: G16 DOI-resolution false-positive class is closed — the test is handle-API resolution (https://doi.org/api/handles/{doi} responseCode 1), never publisher-page fetchability (established for the level-definitions review, commit b4e82e8, and re-confirmed with per-DOI logs by all three sweep agents this session). F-5 (predecessor charter spec): whole-file/aggregate verification counts are inadmissible — verify per-section/per-site. Charter promotion rule: a failure_log layer changes only when the discriminating observation was actually obtained and pointed the stated way. Register convention: original rows retained with strikethrough, never deleted.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Fable 5 (model id `claude-fable-5`, Anthropic) — all
  branches: three specialist audit agents (critical-reviewer at high effort,
  scope-auditor at medium effort, literature-check at high effort, each with
  `model: inherit` in its agent definition), the adversarial refuter (high
  effort), and the trail-assembly agent that authored this document.
- Roles: audit (findings, refutations, verification of the Phase 1 sweep
  integrations and the F005 promotion) and prose (assembly of this trail). No
  authored research content; the audited artifacts were not modified by this
  round's agents.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the verdict and remediations proceed.
- Reproducibility log: ReproLog emission is sequenced with the
  /commit-with-provenance step (spec deliverable 7 / SCOPE-1-3); the log lands
  at `logs/reproducibility/repro_log_{run_id}.json` (gitignored), and its
  clone-durable digest is carried by the commit's `Repro-Log-Path:` /
  `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility contract. The
  commit hash is to be recorded here as a dated addendum when it lands.

## immutability-and-retention

This trail and its JSON sidecar
([audit_trail_phase1-sweep_2026-08-21.json](audit_trail_phase1-sweep_2026-08-21.json),
SHA-256 `b2573d31d552e53f6481a9cfd5edb02003d666b2909831ef0a1c3c9b95c9f2c9`,
holding the round-1 payload verbatim per FAIR I1) are committed to the
repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. Later rounds of this loop append
new round sections to this file; corrections to any recorded entry are
appended as a dated addendum that identifies what it corrects — prior entries
are never edited, overwritten, or deleted. Retention follows the repository's
git history; the tracked file is the durable record, and the front-matter
digests bind it to the exact artifact states audited.

---

# Audit trail — Phase 1 gap-targeted sweep, round 2

Appended round section per 21 CFR 11.10(e): the round-1 entries above are
unmodified. Round 2 is a verify-only round over the four round-1 retained
majors (REV-1-1, REV-1-2, LITERATURE-1-1, LITERATURE-1-2). All three branch
verdicts: **accept**. Union verdict: **accept**. Zero critical/major findings
raised; four new minors logged; the refute gate had nothing to gate.

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
title: "Audit trail — Phase 1 gap-targeted sweep, round 2"
type: audit_trail
date: "2026-08-21"
started_at: "2026-08-21T16:14:05-05:00"
ended_at: "2026-08-21T16:15:10-05:00"
artifacts:
  - {path: "docs/literature/lit_review_regime-definitions_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "b561340781d8bc3de3ce0b7aa18b7d1f75414428fe111c4abaff574e8e2e4464"}
  - {path: "docs/literature/lit_review_regime-method-gaps_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "ea0fc5a0ec75a873b626a04545271a5c1938bde2d3f52a970bc5eeebcd97aa66"}
  - {path: "docs/literature/lit_review_f005-class-n-tests_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "56a50c8db61645c1d2eed5e33d797f21ac04ec8b67006e028cdf6851fcd2d478"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "c71e781904013dc4a6ab99fab5d3ba2014a82aa49ebf27317c8c5e55f6524085"}
  - {path: "failure_log.md", git_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d", sha256: "5d4c3514ffe11aa3ce436ab387819a3269c9f29632fa16936ea0ed131309a8ba"}
repo_head: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    Round 2 (verify-only) of the phase1-sweep loop (deliverable_spec_phase1-sweep_2026-08-21.md). Round 1 retained four majors, all now remediated: REV-1-1 — the unbounded universal 'no source anywhere reports a confidence interval on a level location' was rewritten in bounded form at both sites (agenda branch-1 prior-art note and failure_log F005 addendum): 'no located source... coverage-bounded, not universal (~1,354 of 1,948 screened titles matched neither keyword net...; f005 review §10)', and the novelty claim conditioned to 'first located interval on location in the searched literature'. REV-1-2 — the agenda's detector-OC insertion now carries Alami, Maillard & Féraud 2020 (PMLR, no DOI/arXiv, OpenAlex W3035594853, retrieve-manually caveat) and states the residual gap as the EMPIRICAL delay-vs-ARL0 characterization on financial data, not absence of any characterization. LITERATURE-1-1 — the Garzarelli prose author list was corrected to five authors (adding Pompa) at all five sites (f005 review store table + §9.1 + §9.4 quote; agenda prior-art note; failure_log addendum), each noting the read text is arXiv:1110.5197 v1 whose author list lacks Pompa. LITERATURE-1-2 — the recasting clause was reattached: Frisén 2003 now cited for the evaluation-criteria taxonomy and Bock, Andersson & Frisén 2007 (doi:10.1002/9780470987179.ch3) added as the record that recasts trading indicators as surveillance stopping rules. VERIFY ONLY: (a) each remediation present and adequate against its fix specification; (b) no new defect introduced in the vicinity of the edits; (c) no regression elsewhere. DO NOT re-raise the 15 round-1 logged minors (deferred per invitesPolish=false), the G16 publisher-403 class (closed on handle-API evidence), the G13 Hall-&-York-no-DOI fact (irreducible, carried with archival URL), or the terminal bookkeeping items (spec ticks, ReproLog, provenance commit — sequenced after this round returns accept).
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_phase1-sweep_2026-08-21.md", sha256: "cbb67afdfcfdef654fe9ce3c44b8e912f466e0f1d836bf936b0b18771b1747f7"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill). Round 2 is a verify-only round; zero critical/major findings, so the refute gate was not exercised."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-fable-5", effort: "medium", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-fable-5", effort: "high", role: "audit"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Fable 5, claude-fable-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, literature-check) → trail-assembly agent (this round section)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js; identical branch set to round 1 for continuity of verification (all five artifacts remain markdown prose — quant-auditor and epi-auditor not routed). critical-reviewer (adequacy of the four remediations against their fix specifications, no-new-defect vicinity check, internal consistency) high; scope-auditor (spec traceability, remediation-vs-description fidelity) medium; literature-check (primary-source re-verification of the corrected citations: Garzarelli author lists, Frisén/Bock attribution, Alami record) high."
rounds_completed: 2
rounds_cap: 3
cap_reached: false
verdict: "accept"
counts: {raw_critical: 0, raw_major: 0, raw_minor: 4, refuted: 0, retained_conservative: 0, to_remediate: 0, minors_logged: 4}
sidecar: {path: "docs/audits/audit_trail_phase1-sweep_2026-08-21.round2.json", sha256: "de709e50d48307d203f3d08d6189506932462f99241c5c3163adbc76cecfb840"}
```

Notes on the round-2 record: `started_at`/`ended_at` are the trail-assembly
interval for this round section. The definitions and method-gaps review
digests are unchanged from round 1 (`b5613407…`, `ea0fc5a0…`); the three
artifacts touched by the four remediations moved — the f005 review from
`c8bcea3a…` to `56a50c8d…`, the agenda from `6e3847e2…` to `c71e7819…`, and
failure_log.md from `c36a4e6e…` to `5d4c3514…`. The round-2 sidecar is a
separate sibling file so that the round-1 sidecar (whose SHA-256 is bound
into the round-1 front matter above) remains byte-identical, per append-only
retention.

## findings-table

Round 2 raised zero critical and zero major findings and four minors, all
logged not remediated. The counts object, verbatim from the round payload:
raw_critical 0, raw_major 0, raw_minor 4, refuted 0, retained_conservative 0,
to_remediate 0, minors_logged 4. One row per finding; all eight schema fields
plus branch and disposition (the sidecar carries the identical payload in
JSON, including the exact multi-line evidence text that table cells flatten).

| id | severity | category | location | issue | evidence | fix | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-2-1 | minor | consistency | failure_log.md:288 | New sentence introduced by the REV-1-1 remediation has a wrong or ambiguous referent: grammatically it says the addendum refutes the unbounded form of negative (b) (the confidence-interval claim), but the addendum refutes the row's headline existence-test claim; no CI-reporting source was found, and the f005 review §9.4 explicitly states that part of the gap 'is intact'. Under the natural reading the sentence contradicts both the immediately preceding 'Two narrower negatives survive' and the f005 review. | (b) no **located** source reports a confidence interval on a level location — coverage-bounded, not universal (~1,354 of 1,948 screened titles matched neither keyword net and were not individually read; f005 review §10). The unbounded form of exactly this claim is what this addendum refutes. | Re-anchor the referent so the refuted object is the headline, e.g.: 'An unbounded universal of exactly this form — the row's headline — is what this addendum refutes; hence the coverage bound here.' (mirrors the agenda's clearer phrasing 'the same bounding discipline whose absence let F005's own headline fall to one missed record'). | CHAMP item 27 (conclusions consistent with results); internal consistency vs docs/literature/lit_review_f005-class-n-tests_2026-08-21.md §9.4 limit 2 | critical-reviewer | deferred — logged minor |
| REV-2-2 | minor | reporting | docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:546 | LITERATURE-1-1 fix specification says each of the five Garzarelli sites notes that the read full text is arXiv:1110.5197 v1 whose author list lacks Pompa. The §9.4 verdict blockquote carries the corrected five-author list but omits the provenance caveat (present at the other four sites: store table line 329, §9.1 lines 446-449, agenda lines 149-151, failure_log lines 266-269). No factual error propagates — the published version cited by DOI does carry five authors — so this is a spec-fidelity gap only, relevant because the blockquote is the quotable verdict most likely to be lifted standalone. | > Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014), *Scientific Reports* 4:4487, doi:10.1038/srep04487, tests the Class N construct ... | Append the caveat to the blockquote citation: '(read text: arXiv:1110.5197 v1, whose author list lacks Pompa)' — or record in the round log that the §9.4 omission is accepted because the caveat is stated twice earlier in the same document including at the canonical store entry. | SAMPL general principles (source attribution precision); round-1 LITERATURE-1-1 fix specification | critical-reviewer | deferred — logged minor |
| SCOPE-2-1 | minor | partial | docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:546-547 | The LITERATURE-1-1 remediation is described in the round-2 task spec as applied at five sites 'each noting the read text is arXiv:1110.5197 v1'. The author-list correction (Pompa added) is present at all five sites, but the arXiv-v1/author-list caveat accompanies only four of them; the §9.4 verdict block-quote carries the corrected five-author list without the read-text caveat. | §9.4: 'Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014), *Scientific Reports* 4:4487, doi:10.1038/srep04487, tests the Class N construct...' — no version/read-text note, versus §9.1 (lines 448-449) and the store row (line 329) in the same document, which both carry 'read in full via arXiv:1110.5197 v1, whose author list lacks Pompa'. | Either append the read-text caveat to the §9.4 quote or record that the caveat is carried at document level (store + §9.1) rather than at every citation site. Substantively remediated; this is a delivery-vs-remediation-description discrepancy only. | LITERATURE-1-1 | scope-auditor | deferred — logged minor |
| LITERATURE-2-1 | minor | misattributed-citation | docs/literature/lit_review_regime-method-gaps_2026-08-21.md:487 (near-miss row E6) | Chapter 2 of Financial Surveillance is cited under the book editor's name ('Frisen ed. (2007) Statistical Models in Finance, ch. 2 of Financial Surveillance, doi:10.1002/9780470987179.ch2'); the chapter's author per Crossref is Helgi Tomasson, with Frisen as volume editor. The row sits in the vicinity of the LITERATURE-1-2 remediation (it references the ch. 3 inclusion) so it is reported rather than deferred, but it is non-load-bearing (an exclusion-table row) and the 'ed.' marker partially signals the editor role. | Crossref record for 10.1002/9780470987179.ch2: chapter title 'Statistical Models in Finance', author Helgi Tomasson, book 'Financial Surveillance', 2007 (fetched 2026-08-21). | Rewrite E6 citation as 'Tomasson (2007) Statistical Models in Finance, ch. 2 of Frisen (ed.) Financial Surveillance, doi:10.1002/9780470987179.ch2'. | https://doi.org/10.1002/9780470987179.ch2 | literature-check | deferred — logged minor |

## refute-gate

No critical or major findings were raised in round 2, so no disposition
reached the adversarial refute gate (`refute_gate_dispositions: []`). There
are no dropped, retained, or retained-conservative entries, and no entry with
`reproduction_required: true`, so no `reproduction: {command, observed}`
blocks are owed. The gate's standing rule is unchanged: drop requires concrete
counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)).

## deferred-logged-minors

Four new minors logged in round 2 (`minors_logged: 4`), none remediated this
round (full schema fields in the findings table above and the round-2
sidecar):

- REV-2-1 (critical-reviewer; failure_log.md:288) — the sentence added by the
  REV-1-1 remediation has a wrong or ambiguous referent: it reads as saying
  the addendum refutes the unbounded form of the confidence-interval negative
  (b), whereas the addendum refutes the row's headline existence-test claim.
- REV-2-2 (critical-reviewer; docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:546)
  — the §9.4 verdict blockquote carries the corrected five-author Garzarelli
  list but omits the arXiv-v1 read-text caveat present at the other four
  sites.
- SCOPE-2-1 (scope-auditor; docs/literature/lit_review_f005-class-n-tests_2026-08-21.md:546-547)
  — same site, scope framing: the LITERATURE-1-1 caveat placement is 4-of-5
  versus the task spec's 'each noting' description; a
  delivery-vs-remediation-description discrepancy only.
- LITERATURE-2-1 (literature-check; docs/literature/lit_review_regime-method-gaps_2026-08-21.md:487,
  near-miss row E6) — ch. 2 of Financial Surveillance cited under the volume
  editor's name (Frisén) rather than the chapter author (Tomasson) per
  Crossref for 10.1002/9780470987179.ch2.

The fifteen round-1 minors (REV-1-3 through REV-1-10, SCOPE-1-1 through
SCOPE-1-3, LITERATURE-1-3 through LITERATURE-1-6) remain open in this trail
per `invitesPolish=false` — deferred by protocol, not missed — and were
excluded from re-raising by the round-2 task spec. SCOPE-1-2 stands
discharged by this trail; SCOPE-1-3 remains sequenced with the terminal
bookkeeping phase.

## verification-of-remediations

All four round-1 retained majors are verified remediated, per branch and
against each finding's fix specification:

- **REV-1-1 — remediated (fix as specified).** The unbounded universal 'no
  source anywhere reports a confidence interval on a level location' was
  rewritten in bounded form at both sites (agenda branch-1 prior-art note and
  failure_log F005 addendum): 'no located source... coverage-bounded, not
  universal (~1,354 of 1,948 screened titles matched neither keyword net...;
  f005 review §10)', with the novelty claim conditioned to 'first located
  interval on location in the searched literature'. literature-check confirms
  the bounded claim and conditioned novelty claim are present at both
  required sites with counts matching f005 review §10; critical-reviewer
  confirms the coverage-bound figure is internally consistent (1,825 citing
  works − 471 net-read = 1,354). One presentation-level referent ambiguity in
  the new failure_log sentence is logged as REV-2-1 (minor); it does not
  touch the remediation's substance.
- **REV-1-2 — remediated (fix as specified).** The agenda's detector-OC
  insertion now carries Alami, Maillard & Féraud 2020 (PMLR, no DOI/arXiv,
  OpenAlex W3035594853, retrieve-manually caveat) and states the residual gap
  as the empirical delay-vs-ARL0 characterization on financial data, not
  absence of any characterization. literature-check verifies the record
  against PMLR v119 (alami20a) and OpenAlex, and confirms the no-DOI/no-arXiv
  negative (arXiv 2304.00232 is the distinct 2023 Alami–Mahfoud–Moulines MDP
  paper).
- **LITERATURE-1-1 — remediated (author-list correction complete; caveat
  4-of-5).** The Garzarelli prose author list is corrected to five authors
  (adding Pompa) at all five sites (f005 review store table, §9.1, §9.4
  quote; agenda prior-art note; failure_log addendum), verified against
  Crossref for 10.1038/srep04487 (five authors) and arXiv:1110.5197 v1 (four
  authors). The arXiv-v1 read-text caveat accompanies four of the five sites;
  its omission from the §9.4 blockquote is logged as REV-2-2/SCOPE-2-1
  (minors) — a spec-fidelity gap with no factual error, the caveat being
  carried twice in the same document including at the canonical store entry.
- **LITERATURE-1-2 — remediated (fix as specified).** The recasting clause
  was reattached: Frisén 2003 (ISR 71(2):403-434) is now cited for the
  evaluation-criteria taxonomy and Bock, Andersson & Frisén 2007
  (doi:10.1002/9780470987179.ch3, 'The Relation between Statistical
  Surveillance and Technical Analysis in Finance') added as the record that
  recasts trading indicators as surveillance stopping rules; both records
  verify exactly against Crossref.
- **No new defect of critical/major severity in vicinity; no regression
  elsewhere.** critical-reviewer confirms the two new findings in the edit
  vicinity are presentation-level and touch no conclusion; scope-auditor
  confirms the spec-to-delivery traceability matrix remains fully satisfied
  with no omission, undocumented substitution, or scope creep;
  literature-check detects no regression in the definitions-review scope and
  confirms the deferred round-1 minors were left untouched per
  `invitesPolish=false`.

Branch verdicts, verbatim from the round payload: critical-reviewer accept,
scope-auditor accept, literature-check accept. Union verdict: **accept**, at
rounds_completed 2 of rounds_cap 3 (`cap_reached: false`).

Round-1 bookkeeping items SCOPE-1-2 (this trail) and SCOPE-1-3 (provenance
commit) are the documented terminal bookkeeping phase executed after this
round returns accept: SCOPE-1-2 is discharged by this round section and its
sidecar; SCOPE-1-3 is discharged when the /commit-with-provenance step lands,
its trailer-bearing commit hash to be recorded here as a dated addendum.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Round 2 was a verify-only round focused on the four
remediated passages, their vicinity, and regression spot-checks; it did not
exhaustively re-audit every sentence, citation-claim pairing, store record,
or cross-artifact dependency. Absence of a finding is not evidence of absence
of a defect — the same asymmetry the charter enforces for statistical nulls
applies to this audit's coverage.

Per-branch residual-risk statements, verbatim:

**critical-reviewer:** All four round-1 majors are remediated adequately in substance; the two new findings are presentation-level and do not touch any conclusion. Residual risks: (1) I did not independently re-verify the published Scientific Reports author list, the Alami OpenAlex ID (W3035594853), or the handle-API DOI logs — those rest on round-1 literature-check and the sweeps' logged evidence, per branch scoping. (2) A pre-existing cross-reference mislabel was observed outside the edit vicinity and is not raised as a finding because it plausibly sits among the 15 deferred round-1 minors: method-gaps review §8.5 (line 693) labels the q-s2-04 failure 'verification gap V2' while §10 numbers the S2 rate-limit gap V1 (V2 there is the single-screener gap). (3) The coverage-bound figure (~1,354 of 1,948) is internally consistent (1,825 citing works − 471 net-read = 1,354; remainder are the ~123 direct-query records screened individually), but the failure_log/agenda phrasing 'of 1,948 screened titles' silently spans two retrieval arms; a reader recomputing 1,948 − 471 = 1,477 will not reconcile it without the f005 review §2/§4 — acceptable given the §10 pointer is cited at both sites. (4) CHAMP items 7–16 remain with the quant-auditor branch, which was routed in round 1 (F-3-x findings are cited in the agenda), so no unrouted-analysis finding is warranted. RQI coverage: importance and method adequacy were established in round 1 and re-confirmed unchanged; originality is now correctly conditioned by the remediated novelty claim; presentation and interpretation are covered by the two findings above.

**scope-auditor:** All four round-1 majors (REV-1-1, REV-1-2, LITERATURE-1-1, LITERATURE-1-2) are present and match their fix specifications; the spec-to-delivery traceability matrix for deliverable_spec_phase1-sweep_2026-08-21.md remains fully satisfied for the five artifact deliverables and the audit trail, with the commit/ReproLog items correctly sequenced after this round per the task spec. Residual scope risk is confined to: (1) the one minor above — a 4-of-5 caveat placement versus the task spec's 'each noting' claim, which cannot bias the record since the caveat is carried twice in the same document; (2) the 15 deferred round-1 minors, which remain logged-not-remediated by explicit policy (invitesPolish=false) and are outside this round's mandate; (3) correctness of the remediated claims themselves (e.g., whether the Alami 2020 optimality characterization is accurately summarized), which is method-auditor and literature-check ground, not scope. No omission, undocumented substitution, or scope creep detected in this round.

**literature-check:** All four round-1 majors verified remediated with primary-source confirmation: (1) Garzarelli et al. 2014 published author list (Crossref, 10.1038/srep04487) is five authors including Pompa and arXiv:1110.5197 v1 is four authors lacking Pompa, matching the corrected prose and caveat at all five sites; (2) Frisen 2003 (ISR 71(2):403-434) and Bock, Andersson & Frisen 2007 (10.1002/9780470987179.ch3, 'The Relation between Statistical Surveillance and Technical Analysis in Finance') both verify exactly, with the recasting claim attached to the correct record; (3) the Alami, Maillard & Feraud 2020 record verifies — PMLR v119 (alami20a), OpenAlex W3035594853, no DOI, and no arXiv record (arXiv 2304.00232 is the distinct 2023 Alami-Mahfoud-Moulines MDP paper, confirming the negative); (4) the bounded CI-on-location claim and conditioned novelty claim are present at both required sites with counts matching f005 review section 10. Residual risks: the Alami paper's methodological detail is carried from abstract/OpenAlex-level verification, not full text, consistent with the artifact's own retrieve-manually caveat (an open HAL locator, hal-03021712, exists and could be added as a supplementary access route); the bounded negative 'no located CI on a level location' remains contingent on the ~1,354 individually unread titles, as the artifact now correctly states; Hall & York 2001 no-DOI status carried per prior disposition; the f005 review section 9.4 limit 2 quotes F005's original unbounded phrasing inside a search-scoped sentence ('survives this search'), which is internally bounded and was outside the fix specification's two named sites. No regression detected in the definitions review scope; deferred round-1 minors untouched per invitesPolish=false.

**Prior dispositions carried into this round** (verbatim from the round
payload): Round 1 (this spec): 3 branches, all proceed-with-remediation; 4 majors retained through the refute gate (REV-1-1 bounded-universal overreach, REV-1-2 omitted Alami counter-record, LITERATURE-1-1 Garzarelli author list missing Pompa, LITERATURE-1-2 Frisén/Bock misattribution) — all four now remediated per taskSpec; 15 minors logged not remediated per invitesPolish=false (incl. stale D01-D57 count in definitions review §1.2, ReproLog-SHA citation gaps, level-definitions survey erratum routing left to lead). Standing: G16 closed on handle-API evidence; F-5 aggregate-only verification inadmissible; charter promotion rule honored for F005 (verified by all three branches in round 1); register strike-don't-delete convention.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Fable 5 (model id `claude-fable-5`, Anthropic) — three
  specialist audit agents (critical-reviewer at high effort, scope-auditor at
  medium effort, literature-check at high effort, each with `model: inherit`
  in its agent definition) and the trail-assembly agent that authored this
  round section. No refuter was invoked this round (zero critical/major
  findings).
- Roles: audit (verification of the four round-1 remediations against their
  fix specifications, vicinity and regression checks) and prose (assembly of
  this round section). No authored research content; the audited artifacts
  were not modified by this round's agents.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the accept verdict proceeds.
- Reproducibility log: ReproLog emission is sequenced with the
  /commit-with-provenance step (spec deliverable 7 / SCOPE-1-3); the log
  lands at `logs/reproducibility/repro_log_{run_id}.json` (gitignored), and
  its clone-durable digest is carried by the commit's `Repro-Log-Path:` /
  `Repro-Log-SHA256:` trailers per CLAUDE.md §Reproducibility contract. The
  commit hash is to be recorded here as a dated addendum when it lands.

## immutability-and-retention

This round section and its JSON sidecar
([audit_trail_phase1-sweep_2026-08-21.round2.json](audit_trail_phase1-sweep_2026-08-21.round2.json),
SHA-256 `de709e50d48307d203f3d08d6189506932462f99241c5c3163adbc76cecfb840`,
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

# Addendum — provenance commit landed (2026-08-21)

Appended per 21 CFR 11.10(e); no prior entry edited. Completes the terminal
bookkeeping phase sequenced after the round-2 accept.

- Commit: `2dc418763be6cbe2b6c2809e67f98ff2626dcdad` on `main`
  ("docs(sweep): phase 1 gap-targeted corpus sweep; agenda rev 2; F005 layer
  promoted to data") — 173 files: the three sweep records with CSL-JSON stores
  and 161 search logs, the agenda at revision 2, the failure_log F005 addendum,
  the deliverable spec, and this trail with both sidecars.
- Trailers, verbatim from `git log -1`:
  - `Repro-Log-Path: logs/reproducibility/repro_log_67058aa0d29d479c9a969a7ce3889b24.json`
  - `Repro-Log-SHA256: 4db4997d5ec5bbeaf313e9a4c0976a1562aaeed4b1a397dfc82185ef2aa4aad3`
  - `AI-Assistance: claude-fable-5 (role=multi)`
- Deterministic pre-commit checks recorded: store counts 54/50/7 as declared,
  zero store ids uncited in their reviews, PRISMA declarations present
  (integration check PASS on all five gap sites; `revision: 2` confirmed).
- Sweep-agent ReproLogs (gitignored; digests are the durable anchors):
  `repro_log_4471f7f2091348dd901d083fdf8bc908.json` (sha256
  `1b8da281d63eee4dc9428b3a64751c57a994643e8b1595c5d9a7c88818284be9`, f005
  sweep). The lead-session commit ReproLog is carried by the trailers above.
- Open items handed forward, not closed here: 15 round-1 + 4 round-2 logged
  minors (deferred per invitesPolish=false); the level-definitions survey
  erratum routing (the survey's headline claim is refuted by the F005 addendum
  and the tracked survey does not yet carry a supersession marker) — assigned
  to the lead session by f005 review recommendation (iv), decision not yet
  taken; SSRN 3021585 remains unadjudicable.
- This addendum and the spec's commit-box tick are committed separately as
  closure bookkeeping; that commit's own trailers carry its provenance.
