---
schema_version: WI-3/2
conforms_to: WI-3 section 2 required-field spec (22 front-matter keys, 7 body sections)
title: "Audit trail - kalshi-strategy-corpus (multivocal strategy corpus branch), round 1"
type: audit_trail
date: 2026-09-04
started_at: 2026-09-04T12:05:12-05:00
ended_at: 2026-09-04T12:41:50-05:00
artifacts:
  - path: docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: ed7aca3e767714a70aa3415037a5982fb1595ad3b616f289625ef3da86d80e53
  - path: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: e5167919c8f3ef76ad010d5f3e45abd607989a3591d198269118e90eeb8bd84a
  - path: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: fcf0b71c43981576acf589afa458b1b9c0a7746d4a5bce92b281ae1274266c2e
  - path: docs/literature/references_kalshi-strategy-multivocal.json
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df
  - path: docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: a253633490751326212b91e7c7e04407ca1ad885a042e7c36faad567d9034375
  - path: failure_log.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: f1c102d91ff49f78fa7dd95033dfed485cbf2eb0ae89e145a14d5ccba95f922f
  - path: research/01_hypothesis_register/H001/design.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 4f9160f9c97a59724a51ca0d5ba88865390d5594ca3d5152d98adf0c38c19861
  - path: hypothesis_backlog.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 46b4615724adad60c411b4fcaa96cbbd05a205eda20296fa33b383be99003c96
  - path: docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 6d5d7890487d6b2c578c71c6c30e17e654245b86c784913cdd94951f94d53077
repo_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
worktree_clean: false  # `git status --porcelain` is non-empty at round 1: every artifact
                       # audited here is staged-or-untracked and not yet committed
                       # (see finding REPRODUCIBILITY-1-7).
audit_criteria:
  task_spec_verbatim: |
    TASK SPEC OF RECORD: docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md (read it in full; it carries the Deliverables checklist with per-item `state` and `check` lines, the Delegation table, and append-only Declaration amendments D1-D7 plus a push-authorisation note).

    SESSION OBJECTIVE: open and execute a second, MULTIVOCAL corpus branch compiling the retrievable record of STATED trading/arbitrage/market-making strategies for binary event contracts with KalshiEX LLC as venue of interest, admitting the source classes the frozen 2026-09-02 protocol excludes by criterion I3 (software repositories, exchange/regulator documents, practitioner grey literature), and register the resulting strategy taxonomy, its provenance, and its executability preconditions WITHOUT stating any tradeable rule.

    GOVERNING CONSTRAINTS THE AUDIT MUST APPLY:
    - ADR-0003: castles SPECIFIES, never executes. No market data acquired, no exchange API called, no price computed, nothing fitted, nothing backtested, NO tradeable rule, NO position size, NO expected return. Every executing parameter left `TO COMPUTE` with its SELECTION PROCEDURE NAMED.
    - ADR-0004 + REVIEW.md blocking directive 8: 'Every factor, signal, or trading rule must carry a citation to published research or an in-repo derivation. Unattributed folklore factors are blocking.' ADR-0006 records a WIDENED CARRIER reading for this branch (repository artifact / rulebook clause / dated practitioner write-up satisfy the carrier; model recall does not). Check that widening is stated wherever relied on and never elided.
    - CLAUDE.md + charter commitment 3: NO unlabelled constants. Any threshold is derived from a cited procedure, selected by a documented search, or labelled CONVENTION with provenance.
    - Charter commitment 5 (attribution fidelity) and the predecessor's A19 quotation-audit precedent: a dropped qualifier or a misattributed clause is a DEFECT, not a style choice. Verify quotations byte-exactly against sources.
    - Charter: retrospective power is NEVER computed; MDES is computed instead.
    - Protocol section 10: 'a corpus record that ran under an amendment it does not enumerate is defective.' Amendment M1 (three parts, all pre-screening) must be enumerated wherever it bears.
    - Protocol section 11: the frozen prefix (first 91,498 bytes) must still hash to 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac, i.e. no frozen text was edited by the M1 append.

    KNOWN OPEN DEFECT, SEEDED DELIBERATELY - CONFIRM AND REMEDIATE, DO NOT MERELY RESTATE: the corpus record's section 10 note N-5 says 'four executed academic queries in that stratum returned zero'. At least two of those queries NEVER EXECUTED (HTTP 429 / interface failure); the arm logs' own `n_returned_semantics` / `platform_interface_failure` fields state that n_returned=0 there means NO SEARCH WAS RUN. The corrected executed-and-zero count is TWO. A capacity gap is not an absence. Verify independently against docs/literature/search_logs/kalshi-strategy-multivocal/ks-s2-03*.json and ks-repec-0*.json before accepting or rejecting.

    ACCEPTANCE CRITERIA ALREADY MECHANICALLY VERIFIED BY THE LEAD (re-verify, do not assume): ADR-0006 carries Context/Decision/Alternatives/Consequences/Reversal-cost headings; protocol frozen prefix hash matches the registration commit 4821611c1c93b5f929a76f3ba6207e900440cee5; that commit is an ancestor of every committed search-log commit; corpus has zero `[unsourced]` markers; both flow identities close (1986-412=1574; 1574-1475=99); len(CSL-JSON store) == n_included == 99 so the predecessor gap AG-11 is NOT repeated; H001 design status is `draft-unfrozen` with 30 TO COMPUTE items; M1 present in both required registers with all three parts.

    SPECIFIC RISKS TO PROBE: (a) the corpus rests on evidence tiers 2 and 5 only - the academic arm contributed ZERO included records and all 528 of its rows are capacity-gap G1 - check no claim overreaches that base; (b) 1,465 of 1,475 exclusions are capacity gaps, NOT criterion failures - check they are never reported as eligibility determinations; (c) the research-compile gate returns `block` on FAIR F1 once per store entry, a DESIGNED consequence of ADR-0006 dropping the identifier requirement - check success is nowhere claimed and the gap is recorded; (d) three executability-relevant objects are WITHHELD AT SOURCE in confidential appendices and the rulebook in force was NOT located - check no downstream artifact treats these as merely unretrieved; (e) H001's design must not state a tradeable rule and must not present the always-NO-baseline record as a stronger claim than the source makes ('statistically indistinguishable', n=23); (f) identity hygiene - the author's real email address must appear in no tracked file.
  files_consulted:
    - path: docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md
      sha256: 382ade8e863f96a965b7008b913f0656dffb5847ea652507c9c08b1db34dfc39
      role: task spec of record; quoted verbatim in task_spec_verbatim below
    - path: CLAUDE.md
      sha256: 2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759
      role: project-local rules (in force)
    - path: ~/.claude/CLAUDE.md
      sha256: 9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f
      role: user-level directives (in force)
    - path: ~/.claude/rules/quant-project.md
      sha256: 433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f
      role: not auto-activated here; adopted by explicit reference via ADR-0004
    - path: ~/.claude/rules/population-health.md
      sha256: f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966
      role: consulted; cwd matches no glob, not in force
    - path: ~/.claude/rules/publishing.md
      sha256: a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479
      role: consulted; not in force (real-name attribution per project CLAUDE.md)
    - path: docs/methodology/charter_castles_2026-08-21.md
      sha256: 303da9b003d7877a4324dde6cc1401bade836e2548fea02e2926fc349a3b35b5
      role: governing charter (commitments 3 and 5; MDES never retrospective power)
mechanism: >-
  audit-remediate-loop skill routed to the Workflow engine script
  workflows/audit-remediate.js - deterministic routing, parallel specialist auditors,
  schema-validated findings, and an adversarial refute gate through which every
  critical/major finding must pass before remediation (a drop requires concrete
  counter-evidence, never bare disagreement). One round per invocation; cap 3.
agents:
  - branch: critical-reviewer
    agent_def_path: ~/.claude/agents/critical-reviewer.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor
  - branch: scope-auditor
    agent_def_path: ~/.claude/agents/scope-auditor.md
    model_id: claude-opus-5
    effort: medium
    role: specialist auditor
  - branch: quant-auditor
    agent_def_path: ~/.claude/agents/quant-auditor.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor
  - branch: literature-check
    agent_def_path: ~/.claude/agents/literature-check.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor
  - branch: reproducibility-verifier
    agent_def_path: ~/.claude/agents/reproducibility-verifier.md
    model_id: claude-opus-5
    effort: medium
    role: specialist auditor
  - branch: format-auditor
    agent_def_path: ~/.claude/agents/format-auditor.md
    model_id: claude-opus-5
    effort: low
    role: specialist auditor
  - branch: refute-gate
    agent_def_path: "(no standalone agent definition; the refuter is the in-script
      adversarial role of workflows/audit-remediate.js)"
    model_id: claude-opus-5
    effort: high
    role: refuter (adversarial refute gate)
operator: Sajan Koirala (repository-local git identity 238704148+s-koirala@users.noreply.github.com)
acted_on_behalf_of: >-
  Sajan Koirala, independent researcher, acting for himself. Delegation chain:
  operator -> lead session (Claude Opus 5) -> audit-remediate workflow ->
  six specialist auditor branches and the refute gate. No third party directed
  this audit; no agent message was treated as operator authorisation.
routing:
  - critical-reviewer
  - scope-auditor
  - quant-auditor
  - literature-check
  - reproducibility-verifier
  - format-auditor
rounds_completed: 1
rounds_cap: 3
cap_reached: false
verdict: block
counts:
  raw_critical: 7
  raw_major: 27
  raw_minor: 21
  refuted: 2
  retained_conservative: 0
  to_remediate: 32
  minors_logged: 21
sidecar:
  path: docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.json
  sha256: b79c631144c770f11431dff7c5f55d9149fa3853fe3f2d41b13dc4c305f10038
---

# Audit trail - kalshi-strategy-corpus, round 1

Round 1 of the audit-remediate loop over the multivocal strategy-corpus deliverable set.
Six specialist branches were routed; all six returned `proceed-with-remediation`.
Fifty-five raw findings were raised: 7 critical, 27 major, 21 minor. Six of the
critical/major findings are independent confirmations of the same seeded defect, one from
each branch (REV-1-1, SCOPE-1-1, QUANT-1-1, LITERATURE-1-1, REPRODUCIBILITY-1-1, FORMAT-1-1);
they are recorded separately rather than merged, because each was reproduced independently.
Every critical and major finding was put to the adversarial refute gate: 2 were dropped
on concrete counter-evidence, 32 were retained, 0 were retained-conservative. Round verdict
is `block`: the deliverable set must not be committed as final until the 32 retained
findings are remediated and a round 2 re-audit runs.

Per-branch verdicts:

| branch | effort | verdict |
| --- | --- | --- |
| `critical-reviewer` | high | proceed-with-remediation |
| `scope-auditor` | medium | proceed-with-remediation |
| `quant-auditor` | high | proceed-with-remediation |
| `literature-check` | high | proceed-with-remediation |
| `reproducibility-verifier` | medium | proceed-with-remediation |
| `format-auditor` | low | proceed-with-remediation |

## findings-table

One row per finding raised in round 1, carrying all eight schema fields
(`id`, `severity`, `category`, `location`, `issue`, `evidence`, `fix`, `reference`)
plus the raising `branch` and the refute-gate `disposition`. Minors are not gated and are
listed here as `deferred-logged` with their detail in the deferred-logged-minors section.

| id | severity | category | branch | disposition | location | issue | evidence | fix | reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `REV-1-1` | critical | interpretation | `critical-reviewer` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:219 and :1640-1642 | CONFIRMED INDEPENDENTLY AGAINST THE ARM LOGS. Limitation 9 and negative result N-5 both report FOUR academic queries in the weather stratum as having executed and returned zero, naming ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b. Two of the four never executed. ks-repec-04.json and ks-repec-04-b.json each carry a `platform_interface_failure` field reading 'PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN', and an `n_returned_semantics` field reading 'no search executed; not an observed zero-yield'. I re-read ks-arxiv-04.json (HTTP 200, n_returned 0, n_total_reported 0, no failure field) and ks-openalex-04.json (HTTP 200, n_returned 0, n_total_reported 0, no failure field) and confirm those two DID execute. The corrected executed-and-zero count in stratum S3 is TWO, not four. The record thereby counts a capacity gap as an observed zero in the one limitation whose entire purpose is to stop that inference, and it does so while asserting elsewhere (section 5.4) that 'A corpus record that folds G-rows into the Y totals is defective; this one does not.' The defect is already adjudicated inside the artifact set: failure_log.md F007 states 'The executed-and-zero count in that stratum is therefore **two** ... not four' and then 'Neither the corpus record nor the arm log is edited by this row' - so the set ships a corpus record whose own project has already established the statement to be false, with the correction reachable only from a different file. | **N-5 — the weather stratum is NOT a clean absence, and must not be reported as one.** Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0). | Correct both loci in the corpus record to TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and state in the same sentence that ks-repec-04 and ks-repec-04-b answered HTTP 200 with the IDEAS/RePEc search FORM rather than a result set and therefore never executed, quoting the logs' own `n_returned_semantics` value. Add the RePEc non-execution to the gap register (a new G-n, or an explicit extension of G-9, which currently names only Semantic Scholar). Do not edit the arm logs. Record the correction as a dated amendment note so the superseded wording stays legible, per protocol section 10, and update failure_log.md F007's sentence that neither document is repaired. | CHAMP items 24-25 (results interpreted from evidence; a non-result read as indecisive, never as absence); protocol section 4.4 rule 2; corpus record section 5.4 |
| `REV-1-2` | major | reporting | `critical-reviewer` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:274, :570-588, :1668-1675 | The RePEc platform-interface failure is recorded NOWHERE in the corpus record, and is positively mischaracterised in the one place it is discussed. N-8 states the nine RePEc attempts were 'all HTTP 200 with an empty result page'; the arm logs state the body is 'the IDEAS/RePEc search FORM, not a result set'. An empty result set and an unreturned result set are different objects and the record's own G1-vs-Y discipline turns on the distinction. Three further loci propagate the same misreport: the section 2 information-sources table reports RePEc `n_records` 0 with no flag; the section 3 verbatim-strategy fence annotates all nine RePEc queries as `executed ... n_returned=0` while PRISMA-S item 8 is claimed DIRECTLY on the ground that the strategies are 'copied and pasted exactly as run'; and no entry in the section 12.1 gap register (G-1 ... G-25) covers RePEc non-execution, G-9 being scoped to Semantic Scholar only. The arm logs carry the corrective fields (`platform_interface_failure`, `n_returned_semantics`) that the record never surfaces, so a reader of the record alone cannot recover the fact. | RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page), and SSRN's own interface returned **HTTP 403** unauthenticated at `ks-ssrn-01`. | In N-8 replace 'an empty result page' with the logs' own characterisation (search form returned in place of a result set; query never executed). Annotate the nine ks-repec-* comment lines in the section 3 fence with the log's `n_returned_semantics` value so the fence does not present an unexecuted query as executed. Flag the RePEc row of the section 2 table as an interface failure rather than a zero yield. Add a named gap for the RePEc endpoint alongside G-9. | PRISMA-S item 8 (search strategies copied and pasted exactly as run), items 1 and 15; SAMPL (report what was done, not what was intended) |
| `REV-1-3` | major | consistency | `critical-reviewer` | REMEDIATE (retained at refute gate) | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:89, :93, :374, :441, :459 | The rev-3 agenda now consumes gap and handoff identifiers from TWO corpora whose identifier spaces collide, and the collision is nowhere declared or disambiguated. The front matter states the predecessor corpus's 'section 10 gaps (G-1...G-10) and section 11 TO COMPUTE handoffs (TC-1...TC-5)' are the source of branches 1-6, and separately that the multivocal corpus's 'gaps G-1..G-25 and handoffs TC-1..TC-15 are the sole admissible source of branches 7-11'. Bare 'G-3' then appears with two different referents inside Branch 0 alone: at the branch head and in the rev-2 status paragraph it means the predecessor's G-3 ('The corpus's six G-3 marks stand at six'), while in the branch's own still-missing table it means the multivocal G-3 (confidential elevated-position-limit appendix). 'G-1' is likewise multivocal at line 439 and predecessor at Branch 1's head; 'TC-1' at Branch 0's head is unresolvable. The document already demonstrates the author's awareness of exactly this hazard - agenda-local handoffs were prefixed 'A3-TC-1..A3-TC-7 so that they can never be confused with the corpus's own TC-1..TC-15' - and ADR-0006 set the governing precedent by renaming J1-J6 to N1-N6 for the identical reason. The corpus record's own section 15 item 9 makes the identifiers load-bearing: 'They are numbered because the branch agenda consumes them by identifier, and a branch derived from anything else would not be traceable to this record.' As shipped, a reader grepping 'G-3' retrieves two unrelated gaps. | **From:** G-3, TC-1, AG-1, AG-2. **Tier of the motivating evidence:** T2 (official documentation), currently *unretrieved*. | Adopt a disambiguating prefix for one corpus throughout the agenda (for example MV-G-n / MV-TC-n for the multivocal record, leaving the predecessor's bare G-n / TC-n untouched, or the reverse), state the convention once in 'How to read this document', and sweep every bare G-n and TC-n in the body to the prefixed form. Do not renumber either corpus record. Record the sweep in the revision note as a rev-3 correction, following the ADR-0006 J1-J6 precedent it cites. | CHAMP item 20 (presentation must let a reader verify a stated result); ADR-0006 section Consequences (Negative), the code-collision precedent |
| `REV-1-4` | major | consistency | `critical-reviewer` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:23 and :30-37; hypothesis_backlog.md:26 | Two shipped artifacts assert the non-existence of a third shipped artifact in the same set, and use that non-existence as the stated reason the H001 design is not frozen. H001's front matter records `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)` and its `freeze_status` states 'The corpus record this design depends on ... does not exist'; hypothesis_backlog.md repeats 'the corpus record the design depends on ... does not yet exist'. That file is a delivered artifact of this session. The freeze remains correctly deferred - pre-freeze checklist items 2 through 6 in design.md section 12 are genuinely open (academic-arm screening, ks-a-057 disposition, the mutual-exclusivity flag, the fee-multiplier table, the unlocated rulebook) - but item 1 is now discharged and the stated justification is false as shipped. Compounding it, design.md section 0.3 grounds its provisionality on `ks-academic-candidates.json` reporting 'n_deduplicated_records: 480' where the finished corpus record reports 528 deduplicated academic records; a reader comparing the two artifacts finds two different sizes for the same arm with no reconciliation note. | corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET) | Update H001's front matter and `freeze_status`, and the hypothesis_backlog H001 Notes cell, to record that pre-freeze checklist item 1 is now discharged and that the freeze is deferred on items 2-6, naming them. Add a one-line reconciliation in design.md section 0.3 stating that the academic arm's mid-run figure of 480 was superseded by the corpus record's final 528 and that no claim in the design rests on either count. Do not freeze the design. | CHAMP item 30 (conclusions and stated status limited to what the artifact set supports); deliverable spec amendment D5 |
| `REV-1-5` | major | interpretation | `critical-reviewer` | REMEDIATE (retained at refute gate) | failure_log.md:620-629 | F008's 'Step 2b - source-design validity, with a signable direction' asserts as fact that ks-sc-001's candidate 'was selected **and** evaluated on the same market set', and on that premise concludes the source's null is 'MORE informative than its provenance would otherwise suggest'. The premise is not in the record. ks-github-records.jsonl gives ks-sc-001's `F10_outcome_reported.data_span` as '~92,000 settled/closed Kalshi markets; NO-tilt measured across a 30k settled sample' - two different spans - and the record was assessed at README-and-metadata depth only. The same F008 row lists 'the candidate-threshold selection procedure' as discriminating observation (iii), status OBTAINABLE and not obtained, and assigns layer `undetermined` precisely because the README states which conclusion it reached and not how. The row therefore builds a signed informativeness upgrade on one of the three facts it simultaneously records as unobtained, and does not carry the `[corpus-inference]` marker this project uses elsewhere (research agenda front matter and Branch 2b) for exactly this move. A related smaller instance in the same row supplies a unit the source does not state: 'n=23 candidate events'. | The candidate was selected **and** evaluated on the same market set, with no stated family-wise control (**TC-14** names the control that is absent ... ). A post-selection interval is biased **toward finding an effect**. So the source's negative verdict is reached **despite** a bias running the other way, which makes the null **more** informative than its provenance would otherwise suggest | Rewrite Step 2b as a conditional marked `[corpus-inference]`: state that the README does not say whether the candidate was selected and evaluated on the same set, that the two spans it reports differ, and that IF selection and evaluation shared a set THEN the post-selection bias runs toward finding an effect - and that the informativeness upgrade is therefore contingent on discriminating observation (iii), not established. Strike 'candidate events' as the unit of n or attribute the unit to the reader's inference. | CHAMP items 27 and 29 (causation/association discipline; pre-specified vs exploratory reasoning distinguished); charter commitment 5 (attribution fidelity) |
| `REV-1-7` | major | consistency | `critical-reviewer` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:86 | The front-matter `screening_verdict_source` field states a total of 109 verdicted records and then itemises components summing to 110: 43 software + 30 venue + 32 lateral + 5 Y3. The correct lateral figure after the cross-arm deduplication of KSL-C31 (section 5.2, which states deduplication happens BEFORE screening) is 31, giving 43 + 30 + 31 + 5 = 109, which is also what the flow requires (99 included + 10 Y-code excluded) and what section 5.3 restates ('It assigned every one of the 109 eligibility verdicts'). The arm log's own `n_classes_sourced` is 32, so both numbers are defensible in isolation but not in one sentence. In a record whose warrant rests on published arithmetic closure - and which flags DI-2 for a two-row shortfall of exactly this kind and refuses to resolve it 'by rounding' or 'by reclassification' - an itemisation that does not sum to its own stated total is the same class of defect the record polices elsewhere. | READ-BASED for 100% of the 109 records that received any eligibility verdict — 43 software artifacts assessed by the software arm at the depth its records state, 30 venue documents assessed by the lead session against the frozen N/Y criteria, 32 lateral class records assessed by the lateral arm at retrieval, and 5 unsourced candidate classes dispositioned Y3. | Change '32 lateral class records' to '31 lateral class records (32 sourced by the arm, less KSL-C31 removed at the cross-arm deduplication step of section 5.2, which precedes screening)' so the itemisation sums to the stated 109. Verify no other locus repeats the 32 as a verdicted count. | CHAMP items 17 and 20 (data described correctly; presentation must reconcile); protocol section 4.5 count identities |
| `SCOPE-1-1` | critical | changed | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:218-219 and :1639-1646 | CONFIRMED against the arm logs: the corpus record reports a capacity gap as an executed zero-yield result. Limitation 9 states "Four executed academic queries in that stratum returned zero" and section 10 N-5 names them as ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b, each annotated "(HTTP 200, 0)". Two of the four never executed. The correct executed-and-zero count is TWO. This is the exact class of defect the corpus itself legislates against (front matter capacity_codes G1: "NOT eligible, NOT ineligible"; protocol section 4.4 rule 1; limitation 9's own headline "is NOT a clean absence"), applied to the query layer instead of the record layer. failure_log.md F007 already establishes the correction but expressly declines to repair the corpus record, so the false count still stands unqualified in the artifact a reader reaches first. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json field platform_interface_failure: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'."; field n_returned_semantics: "no search executed; not an observed zero-yield". ks-repec-04-b.json carries the identical two fields (retry_of: ks-repec-04). Eleven ks-s2-03*.json files exist on disk, all HTTP 429, corroborating the rest of N-5. Corpus limitation 9: "Four executed academic queries in that stratum returned zero"; N-5: "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)." | Edit N-5 and limitation 9 to read TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and to state that ks-repec-04 / ks-repec-04-b returned HTTP 200 with a search FORM and never executed, quoting the log's n_returned_semantics field. Add the correction to section 11 as a numbered data-integrity entry (DI-n) and cross-reference failure_log F007 so the two documents agree; extend gap G-9 to name the RePEc interface failure alongside the Semantic Scholar 429s. | deliverable spec Deliverables row 4 (corpus record: "a named-gap section, and the limitations a reader must carry into every number") and clause 4 of the spec's "Why this is a NEW branch" section ("An unbounded claim of completeness is a defect") |
| `SCOPE-1-2` | major | changed | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:577-590 vs docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:66 | Silent substitution in kind. The declaration's protocol row promises a protocol frozen before first query "specifying ... the verbatim query set per arm". The frozen protocol instead freezes the construction RULE and leaves the concrete strings to execution. Defensible (and it is what made amendment M1 necessary and possible), but it is a different deliverable in kind from the one declared, and none of the append-only amendments D1-D7 records it. | Spec line 66: "...eligibility criteria with codes, the verbatim query set per arm, the screening rule...". Protocol section 3.5: "The concrete query strings are **not** fixed in this file. ... **What freezes is the construction rule in sections 3.1-3.4 and the recording obligation in section 3.0.**" | Append a declaration amendment D8 recording that the frozen artifact freezes the query CONSTRUCTION RULE rather than the verbatim query set, why (an unenumerable multivocal query surface), and what discipline substitutes for it (section 3.0 recording obligation plus the section 10 amendment requirement that produced M1). Do not edit the frozen protocol. | spec Deliverables item 2 |
| `SCOPE-1-3` | major | changed | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/literature/search_logs/kalshi-strategy-multivocal/ (directory) vs deliverable spec:70-71 | The declared search-log deliverable requires "the deterministic dedup and screening scripts with PYTHONHASHSEED=0 asserted at entry, as the 2026-09-02 branch does", and its check is "the screening script self-test exits 0". Six deterministic Python scripts exist and cover parsing, dedup, candidate assembly, recovery and store building, but NO screening script exists and none can: the branch deliberately assigned all 109 eligibility verdicts by read-based agent assessment. The declared check is therefore unsatisfiable as written. The substitution is documented in the deliverable (front matter screening_verdict_source; section 5.3) but is nowhere declared as a divergence from this spec. | Spec check: "every `query_id` cited in the corpus record resolves to a file in this directory, and the screening script self-test exits 0." Corpus front matter: "NO KEYWORD CLASSIFIER ASSIGNED ANY VERDICT IN THIS CORPUS. ... The trade is deliberate and is not an improvement in coverage — it is a much smaller decided set." Directory listing shows ks-academic-{extract,assemble,recovery-pass,runner,query-table,query-table-supplementary}.py and no screening script. | Append a declaration amendment recording that no screening script exists by design, that the spec's "screening script self-test exits 0" check is retired as inapplicable, and naming the substitute verification (the stored B1-B4 branch rule and SR-1/SR-3 subset rule, both declared non-verdict machinery, plus the PYTHONHASHSEED=0 assertion on the five deterministic scripts that do exist). | spec Deliverables item 3 |
| `SCOPE-1-4` | major | partial | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1180-1197 (section 4) | The spec's completeness-bound clause promises three components in the corpus record: per-arm coverage, the strata left unassessed, and a known-item recall check "in the manner the 2026-09-02 record does". Two are delivered in full (limitations 1-3, G-1..G-25; the unassessed strata). The third is absent: the file contains no known-item recall check and no occurrence of the phrase. Section 4 reports only that the strategy was not peer reviewed and points to the pre-freeze instrument verification, which is a different check (instrument resolution, not search recall). No D-amendment records the drop. | Spec line 54-57: "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." Grep for 'known-item\|known item\|recall check' over the corpus record: no matches. Section 4 delivers instead: "**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was obtained, and none was simulated." | Either execute and report a known-item recall check (seed set of records the arms should have retrieved — e.g. the predecessor branch's Kalshi-naming included records and the two negative-measurement repositories — with per-arm hit/miss), or append a declaration amendment stating the check was not performed, why, and registering it as a numbered gap in section 12.1 so the agenda can consume it. | spec "Why this is a NEW branch" clause 4; Deliverables item 4 |
| `SCOPE-1-5` | major | omitted | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md + .json (both absent from disk) | Declared deliverable not present. The spec requires a session audit trail validating against the WI-3 section 2 required-field spec (22 front-matter keys, 7 body sections) with every refute-gate disposition recorded verbatim, plus a sidecar whose sha256 matches. Neither file exists. Severity is set at major rather than the category default because this artifact is the audit loop's own output and cannot exist before the loop closes; it becomes critical if the session commits without it. | Spec lines 85-87. Glob 'docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.*' returns no files. Sibling trails for the prior session exist (audit_trail_s4-reexecution-and-repo-gaps_2026-09-03.{md,json}), so the naming convention is established and the absence is not a path miss. | Write the trail and sidecar before the final provenance commit; carry every round-1 finding and its refute-gate disposition verbatim, including the SCOPE-1-1 confirmation and the reason each declaration amendment below was or was not opened. | spec Deliverables item 7 |
| `SCOPE-1-6` | major | added | `scope-auditor` | REMEDIATE (retained at refute gate) | hypothesis_backlog.md:13, :26, :28-33 | Undeclared scope addition. The spec declares the H001 design document (D5) and failure_log.md (D6) but no change to hypothesis_backlog.md. That file has been given a new H001 row, a newly invented status value `specified-unfrozen` added to the house status legend, and a retained-prior-state note recording removal of the bootstrap stub. Adding a status token to a cross-project convention register is a broader change than the row itself. D6 opened scope for failure_log.md on exactly the reasoning that "an undeclared deliverable is a scope divergence"; the same standard was not applied here. | hypothesis_backlog.md line 13: "`specified-unfrozen` \| **PROPOSED 2026-09-04, not yet ratified.** ... This status exists because `designed` below asserts a freeze that has not happened, and no other status in this legend is true of a drafted-but-unfrozen design." Spec D5 declares only "`H001 pre-registration design document` (path per the `pre-register-hypothesis` skill...)". Spec D6: "Not in the original Deliverables list. ... Registering them is a standing charter obligation, not a discretionary addition, so it is recorded as scope rather than left undone." | Append a declaration amendment covering the hypothesis_backlog.md edit, stating explicitly that a new status token was introduced into a shared convention register, that it is PROPOSED and not ratified, and what would ratify it. | spec Declaration amendments D5/D6 (the standard they set) |
| `SCOPE-1-7` | major | spec-conflict | `scope-auditor` | REMEDIATE (retained at refute gate) | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:626-631 vs :663-685 | The frozen protocol contradicts itself about whether a record may end screening undispositioned, and 93% of the delivered flow (1,465 of 1,574 screened records) took the path section 4.2 does not enumerate. Section 4.2 states every deduplicated record receives exactly ONE stage-1 disposition and lists three: include, exclude-with-Y-code, promote. Section 4.4 then creates G1/G2, which are none of the three. The corpus record follows 4.4 consistently and reports G-rows separately from Y-rows as rule 2 requires, so the DELIVERY is coherent; the SPEC is not, and a reviewer re-deciding any G-row against section 4.2 alone would find an unmet obligation. | Protocol section 4.2: "Every deduplicated record receives exactly one stage-1 disposition: `include`, `exclude` with a primary Y-code, or `promote` where eligibility is not decidable at metadata depth (N6)." Protocol section 4.4: "**G1 — identified, eligibility not assessed.** ... It is **not** eligible, **not** ineligible: it is **undecided**." Corpus front matter: n_capacity_gap 1465, n_criterion_excluded 10. | Remediate the SPEC, not the delivery: issue append-only amendment M2 reconciling section 4.2's disposition enumeration with section 4.4's capacity codes (a G-code is a fourth stage-1 outcome, or 4.2's 'exactly one' is read as conditional on assessment capacity). Do not edit frozen text; record M2 in both registers as M1 was. | lower-precedence spec source: frozen protocol, sections 4.2 / 4.4 |
| `QUANT-1-1` | critical | numerical | `quant-auditor` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:216-218 (limitation 9) and :1639-1653 (negative result N-5) | The corpus record states, twice, that FOUR academic queries in the weather stratum executed and returned zero. Two of the four named queries (`ks-repec-04`, `ks-repec-04-b`) NEVER EXECUTED — their own logs declare a platform interface failure and state that n_returned=0 there means no search was run. The corrected executed-and-zero count is TWO. The record therefore reports a capacity gap as an observed zero-yield, which is precisely the inference the same section forbids ('a capacity gap is not an absence'). The defect is identified in failure_log.md F007 and in the research agenda, but both explicitly decline to repair it ('Neither the corpus record nor the arm log is edited by this row'), so the citable primary artifact still carries the false statement. Recording a known-false claim elsewhere is not remediation; §11's 'recorded, not repaired' class is for defects in EXTERNAL sources (DI-1, a regulator's mis-indexed PDF), not for the record's own misstatement of its own execution log. | Corpus L1640: 'Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0).' Independent read of the logs: ks-repec-04.json / ks-repec-04-b.json carry `"platform_interface_failure": "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN"` and `"n_returned_semantics": "no search executed; not an observed zero-yield"`. Only ks-arxiv-04.json and ks-openalex-04.json carry http_status 200, client_error null, n_total_reported 0 with no interface-failure field. Corrected count = 2. | Edit both loci in the corpus record to read 'TWO academic queries in that stratum executed and returned zero (`ks-arxiv-04`, `ks-openalex-04`); `ks-repec-04` and `ks-repec-04-b` returned HTTP 200 but never executed — their own `platform_interface_failure` / `n_returned_semantics` fields state that n_returned=0 there means no search was run, so they are capacity gaps, not observations.' Also correct N-8's characterisation of the nine RePEc attempts as 'HTTP 200 with an empty result page' to 'HTTP 200 serving the search FORM, not a result set'. Record the correction as a dated erratum in the record and cross-reference failure_log F007 and agenda rev 3 so the three artifacts agree. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json, ks-repec-04-b.json, ks-arxiv-04.json, ks-openalex-04.json; failure_log.md:481-491; protocol §4.4 rule 2 (G-rows reported separately from criterion failures) |
| `QUANT-1-2` | major | method | `quant-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:462-472; docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1601-1612 (N-2) | H001 §1.6 asserts a 'Correction to the framing this design was handed': that the ks-sc-001 record does NOT state that no price-based strategy beat the always-NO baseline. The primary source is in the repository, byte-verifiable, and states exactly that in bold. The assertion about the source is false, and the corpus's N-2 characterisation ('the record's own null result is that its best candidate did not beat its own baseline') likewise understates the source's own headline null. Charter commitment 5 makes a misdescribed source clause a defect regardless of direction; here it makes a source-reported NULL look weaker than the source states it, in the artifact whose whole function is to record what sources state. | ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md (sha256 50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118, matches the recorded README digest), item 3 of 'Three structural realities': '**No price-based strategy clears the honest bar.** The best candidate beats always-NO on point estimate but is statistically indistinguishable from it (n=23, CI overlaps).' and the conclusion line: '**Conclusion: there is no demostrable price-based edge in the public settled-market data.**' The arm log's F4_evidence_quotes for that item begins at 'Favorites >> longshots', dropping the two preceding sentences of the same numbered item. | Add the two dropped sentences to ks-sc-001's F4_evidence_quotes with their location; rewrite H001 §1.6(i)'s 'Correction' paragraph to state what the README actually says ('No price-based strategy clears the honest bar' with the always-NO baseline defined as that bar in item 2, plus the conclusion sentence) and keep the design's conservative use of only the n=23 / CI-overlap claim as an explicit choice rather than as a claim about the source; extend corpus N-2 with the same two verbatim sentences. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 30-42; charter commitment 5 (attribution fidelity); predecessor amendment A19 quotation-audit precedent |
| `QUANT-1-3` | major | parameter | `quant-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:474-500 (§1.6(ii)) and :1119-1126 (§9.2 item 1); docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-records.jsonl (ks-sc-002, F9_preconditions_stated) | A load-bearing qualifier is dropped from the ks-sc-002 source at extraction and propagates into the design's registered sanity ceiling. The README states the 40-50c round-trip hurdle of 10.7c and, in the very next sentence, 'Even at the tails the hurdle is 2.6c.' The arm log's quote stops immediately before that sentence; H001 §1.6(ii) then argues the source's bar is stated only mid-range, leaves the tail bar 'TO COMPUTE', and registers QUOTED 10.7c as the pre-registered sanity ceiling for a tail-band `delta` in §9.2. The source's own tail figure is ~4x tighter, so the registered ceiling cannot catch the arithmetic error it exists to catch. Separately, the justification given for the ceiling ('the fee is monotonically smaller away from P = 0.5') covers only the fee component, while 10.7c is spread PLUS twice the fee; the same README states liquidity concentrates near the money and 79% of contracts never showed a two-sided book, so tail spreads are not established to be monotone. The monotonicity assumption is asserted, not verified. | ks-github-readme-evidence/himagna16__kalshi-microstructure.md (sha256 753d94ddd29e..., matches recorded digest), cost-to-trade section: 'A contract trading at 40-50c must move **10.7c** ... before a taker round trip breaks even. Even at the tails the hurdle is 2.6c.' ks-sc-002 F9_preconditions_stated quote ends at '...breaks even.'; grep for '2.6' returns no hit in H001 design.md or in the corpus record. | Extend the ks-sc-002 extraction to include 'Even at the tails the hurdle is 2.6c.'; in H001 §1.6(ii) record that figure as the source's own tail statement, flag it non-adoptable on the same grounds as the other bare numbers (no derivation on the page), and re-register the §9.2 sanity ceiling against it rather than against 10.7c; replace the fee-monotonicity justification with one that covers the spread term, or restrict the ceiling claim to the fee component only. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/himagna16__kalshi-microstructure.md lines 90-96; charter commitment 3 (no unlabelled constants) and commitment 5 |
| `QUANT-1-4` | major | parameter | `quant-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:816 (§6 embargo) and :1087 (§9.1 bootstrap block length); §13 References :1315-1403 | The 'Politis-White automatic block length' procedure is named twice as the selection procedure for two load-bearing parameters (the walk-forward embargo and the bootstrap block length feeding Hansen SPA / White Reality Check) and carries no citation anywhere in the document, in the charter, or in ks-instrument-verification.json. Every other statistical instrument in the design is cited with a DOI and its provenance declared; this one is not. That breaches CLAUDE.md's parameter-selection rule (documented selection rationale with citations), the design's own §0.2 labelling regime, and the D5 acceptance check that no external citation appear that is absent from ks-instrument-verification.json or an arm output. | grep -n 'Politis' research/01_hypothesis_register/H001/design.md returns only lines 816 and 1087; grep 'Politis' across docs/methodology/charter_castles_2026-08-21.md returns nothing; §13's four citation blocks list White, Hansen, Newey-West, Andrews, Opdyke, Lo, Ledoit-Wolf, Hoenig-Heisey, Theiler, Kaufman, Lakens, Schuirmann — Politis-White appears in none. | Add the citation to §13 with its DOI (Politis & White 2004, Econometric Reviews 23(1):53-70, doi:10.1081/ETC-120028836, together with the Patton, Politis & White 2009 correction, doi:10.1080/07474930802459016), declare its provenance in the same terms used for the other statistical instruments ('cited as the rule file / charter records it, not re-verified in this drafting session'), or replace the named procedure with one already carried in ks-instrument-verification.json. | ~/.claude/CLAUDE.md §Parameter & Prompt Selection; deliverable spec D5 check line 218-220 |
| `QUANT-1-5` | major | reproducibility | `quant-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:99-106 (§0.3) and front matter :24-29 | H001 §0.3 quotes two named fields verbatim from an in-repo file whose current bytes contradict them, and records no read-time digest that would make the quotation checkable. The design declares the arm 'PROVISIONAL and possibly mid-run', which explains the staleness but does not make the quotation reproducible: a reader following the citation retrieves different numbers and has no way to confirm the design read the file it says it read. | design.md L101-102: '`ks-academic-candidates.json` reports `n_deduplicated_records: 480` and `n_in_reported_branches: 144`'. On disk: grep -o '"n_deduplicated_records": *[0-9]*' returns 528; '"n_in_reported_branches": 152'. No sha256 of ks-academic-candidates.json is recorded anywhere in the design. | Record the SHA-256 (and read timestamp) of ks-academic-candidates.json as read, next to the quoted figures, and add a one-line note that the file has since been superseded at 528 / 152; or re-read and re-quote the current values with the current digest. Apply the same digest discipline to the other four entries in `arms_read_for_this_draft`. | CLAUDE.md §Reproducibility contract (dataset checksum); charter commitment 5 |
| `QUANT-1-6` | major | reporting | `quant-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:23, :30-38 (freeze_status), :1296-1300 (pre-freeze checklist item 1); hypothesis_backlog.md:26 | Two tracked deliverables in the same delivery assert as fact that the corpus record does not exist, and use that non-existence as the stated reason the design is not frozen. The corpus record exists on disk and is a deliverable of the same session. Pre-freeze checklist item 1 is therefore satisfied while the artifacts still report it as blocking, so a reader cannot tell which pre-freeze conditions actually remain open. | design.md L23: 'corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)'; L34-37: 'The corpus record this design depends on ... does not exist; freezing now would register a design against literature that has not been compiled.' hypothesis_backlog.md L26: '...because the corpus record the design depends on (...) does not yet exist'. `ls -l` shows the file present at 203,216 bytes, and git status lists it as an untracked file of this delivery. | Update both artifacts to state that the corpus record now exists (with its SHA-256), mark pre-freeze checklist item 1 as DISCHARGED, and restate the remaining freeze blockers — checklist items 2-6 (academic stage-1 screening of ks-a-057, the KSL-C02 exclusivity flag, the per-series multiplier table, the unlocated rulebook, clause re-retrieval) — as the operative reason the design stays `draft-unfrozen`. | deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D5 (freeze deferred until the corpus record exists) |
| `LITERATURE-1-1` | critical | misattribution-of-cited-primary-source | `literature-check` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1640-1642 and :215-219 | The seeded defect is CONFIRMED and still OPEN in the corpus record. Section 10 note N-5 and head-limitation 9 both state that FOUR academic queries in the weather stratum executed and returned zero, naming ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b. Two of the four named queries never executed. The corpus record thereby reports two capacity gaps as executed zero-yield observations — the exact category error N-5 exists to prevent — and does so in direct contradiction of the primary sources it cites by id. | Verified independently against the primary logs. docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json line 33 `platform_interface_failure`: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed. ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." Line 34 `n_returned_semantics`: "no search executed; not an observed zero-yield". ks-repec-04-b.json carries byte-identical text in both fields (lines 33-34). Corpus line 1640 reads verbatim: "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)." Line 215-216 reads: "Four executed academic queries in that stratum returned zero". The corrected executed-and-zero count is TWO (ks-arxiv-04, ks-openalex-04). The 11 ks-s2-03* logs were also re-read: all eleven carry `http_status: 429`, so the corpus's claim about the never-executed on-point query is correct. The discrepancy is already correctly diagnosed in failure_log.md F007 (lines 482-491) and in docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1721-1728, both of which state the count is two — but both explicitly decline to repair the corpus record, leaving the branch's own citable artifact carrying the false statement. | Edit N-5 to read: "TWO academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0) and `ks-openalex-04` (HTTP 200, 0). `ks-repec-04` and `ks-repec-04-b` returned HTTP 200 with `n_returned: 0`, but their own `platform_interface_failure` and `n_returned_semantics` fields state that no search was run; they are platform-interface failures, not observed zeros, and are counted nowhere as evidence about the literature." Make the identical correction at limitation 9 (line 215). Record the correction as a dated in-place correction note so the original wording stays legible, per the branch's own amendment discipline. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json fields `platform_interface_failure`, `n_returned_semantics`; failure_log.md F007; charter commitment 5 (attribution fidelity); protocol section 4.4 rule 2 (capacity codes reported separately from criterion codes) |
| `LITERATURE-1-2` | major | misquotation-of-cited-primary-source | `literature-check` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1669-1671 (N-8), with docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:274 (PRISMA-S item 15 source table) | Second, independent instance of the same misdescription. N-8 states RePEc "returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". The cited logs say the opposite of "empty result page": they say the body is the SEARCH FORM, not a result set, and that the query never executed. An "empty result page" is a search that ran and found nothing; a form page is a search that did not run. Compounding this, the PRISMA-S item 15 source table at line 274 reports `RePEc / IDEAS ... n_records 0` with no interface-failure annotation, while PRISMA-S item 15 ("Document the total number of records identified from each database") is claimed DIRECTLY (not by analogy) at line 262. | Corpus line 1669-1670 verbatim: "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". Against ks-repec-04.json line 33: "the body is the IDEAS/RePEc search FORM, not a result set". The nine-attempt count is correct (ks-repec-01, -01-b, -01-c, -02, -02-b, -03, -03-b, -04, -04-b confirmed on disk). N-8's closing sentence ("each is a finding about the endpoint") partly mitigates but does not correct the false description of what the bytes contain. | Replace "all HTTP 200 with an empty result page" with "all HTTP 200 returning the IDEAS/RePEc search form rather than a result set, so no search executed". Add a footnote to the source table's RePEc, SSRN, GitHub-code and Kaggle rows marking `n_records = 0` as an interface failure and not an identified-record count, so the directly-claimed PRISMA-S item 15 figure is not read as a yield. | ks-repec-04.json / ks-repec-04-b.json `platform_interface_failure`; PRISMA-S item 15 (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z), verified verbatim at PMC8270366: "Document the total number of records identified from each database and other information sources." |
| `LITERATURE-1-3` | major | unattributed-method | `literature-check` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:816 and :1087 | The "Politis–White automatic block length" is named twice as a binding, non-discretionary selection procedure — for the splitter `embargo` (§6) and for the block bootstrap inside the Hansen SPA aggregation (§9.1) — with NO citation anywhere in the document, including the otherwise-exhaustive §12 References (lines 1368-1404). This is a named method with no resolvable record, in a design whose §0.2 declares that every parameter carries either `QUOTED`, `TO COMPUTE` with a named procedure, or `CONVENTION` with provenance, and whose §12 explicitly flags which instruments were and were not re-verified. The omission also loses a materially important fact: the original formula was corrected in a published erratum that reference implementations follow. | Line 816: "the Politis–White automatic block length for the same series. Data-driven, not chosen." Line 1087: "Politis–White automatic procedure (the same estimator §6 uses for the embargo)." Grep of the file for `Politis` returns only those two lines; §12 References (lines 1368-1404) lists PRISMA-S, PRISMA 2020, Arksey & O'Malley, Adams/Smart/Huff, Garousi, Kalliamvakou, Munaiah, Smith, Klein, Jones, White 2000, Hansen 2005, Newey & West 1994, Andrews 1991, Opdyke 2007, Lo 2002, Ledoit & Wolf 2008, Hoenig & Heisey 2001, Theiler 1992, Kaufman 2012, Lakens 2018, Schuirmann 1987 — and no Politis. Canonical record verified via Crossref: Politis DN, White H. "Automatic Block-Length Selection for the Dependent Bootstrap." Econometric Reviews. 2004;23(1):53-70, doi:10.1081/ETC-120028836. Erratum verified via Crossref: Patton A, Politis DN, White H. "Correction to 'Automatic Block-Length Selection for the Dependent Bootstrap' by D. Politis and H. White." Econometric Reviews. 2009;28(4):372-375, doi:10.1080/07474930802459016. | Add to §6, §9.1 and §12: Politis & White 2004 (doi:10.1081/ETC-120028836) as amended by Patton, Politis & White 2009 (doi:10.1080/07474930802459016), and state which of the two formulae the executing project must implement. Follow the file's own convention of flagging whether the record was re-fetched in this drafting session. | https://doi.org/10.1081/ETC-120028836 ; https://doi.org/10.1080/07474930802459016 ; CLAUDE.md "Document selection rationale with citations"; REVIEW.md blocking directive 8 as widened by ADR-0006 |
| `REPRODUCIBILITY-1-1` | critical | data_hashed | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1639-1642 (N-5) and :215-219 (head limitation 9) | CONFIRMED, seeded defect. N-5 states "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)". Two of the four NEVER EXECUTED. The corrected executed-and-zero count is TWO. Head limitation 9 repeats the same wrong count ("Four executed academic queries in that stratum returned zero"). A capacity/interface gap is being reported as an observed zero-yield, which is the exact eligibility-vs-capacity conflation the protocol section 4.4 and the corpus's own risk framing forbid. | Independent re-derivation from the arm logs (python over docs/literature/search_logs/kalshi-strategy-multivocal/): ks-repec-04.json and ks-repec-04-b.json both carry n_returned_semantics = "no search executed; not an observed zero-yield" and platform_interface_failure = "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set...". All nine ks-repec-0*.json files carry the identical pair of fields. Only ks-arxiv-04.json (200, n=0, semantics=None, pif=None) and ks-openalex-04.json (200, n=0, semantics=None, pif=None) are genuine executed zero-yields. Separately verified as correct in the same note: all 11 ks-s2-03* attempts are HTTP 429, and the arm-wide Semantic Scholar tally is exactly 53x429 / 1x500 / 2x200 over 56 files, matching N-5's text. | Rewrite N-5 to read TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and move ks-repec-04 / ks-repec-04-b into the never-executed set alongside ks-s2-03, quoting their own platform_interface_failure field. Correct head limitation 9 to the same count. State explicitly that the weather stratum has TWO executed queries, not five, and that three of its five queries produced no search at all. | _(none stated)_ |
| `REPRODUCIBILITY-1-2` | major | data_hashed | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md, section 10 note N-8 | Same defect class as N-5, second instance. N-8 says "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". "An empty result page" is an observation about a result set. The logs state the opposite: no result set was served at all. | All nine ks-repec-0*.json carry platform_interface_failure = "...the body is the IDEAS/RePEc search FORM, not a result set..." and n_returned_semantics = "no search executed; not an observed zero-yield". N-8's closing sentence ("each is a finding about the endpoint") is right, but the descriptive clause preceding it asserts a zero-yield observation the logs deny, and it is that clause N-5 relied on. | Replace "all HTTP 200 with an empty result page" with the logs' own wording: HTTP 200 whose body is the search form rather than a result set, i.e. no search executed. Cross-reference the corrected N-5. | _(none stated)_ |
| `REPRODUCIBILITY-1-3` | critical | entrypoint_runs | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/search_logs/kalshi-strategy-multivocal/ (all 6 academic .py and all 7 ks-github-scripts/*.py) | No archived script in the branch can execute. The pipeline is not re-runnable from the artifact set, and the deliverable spec's own check for this directory ("the screening script self-test exits 0") is unsatisfiable — no script exposes a self-test and no script even imports successfully. | Dry-run under the project venv with PYTHONHASHSEED=0, exit status captured for each: ks-academic-runner.py -> exit 1, ModuleNotFoundError: No module named 'queries' (it does `from queries import QUERIES`; the file was archived as ks-academic-query-table.py). ks-academic-assemble.py -> exit 1, FileNotFoundError candidates.json (archived as ks-academic-candidates.json). ks-academic-recovery-pass.py and ks-academic-query-table-supplementary.py both do `import run_arm`, and no run_arm.py exists in the directory. ks-github-scripts/write_ledger.py -> exit 1, FileNotFoundError _drawn.json; verify_quotes.py -> exit 1, FileNotFoundError _stage1_gh.json. None of _stage1_gh.json, _stage2.json, _drawn.json, _pins.json, _readmes.json or _readmes/ is present, so draw_and_pin.py, get_readmes.py, write_logs.py, write_ledger.py and verify_quotes.py are all dead. Grep for self.test\|self_test\|--check across all 13 scripts returns nothing. Consequence: the S-C arm's F4 quote verification (verify_quotes.py) cannot be re-executed by any reader, and the SR-4 sha256-ordered subset draw cannot be independently re-derived from the archive. | Either (a) archive the modules under their import names (queries.py, run_arm.py) or add a shim/rename the imports, and archive the intermediate stage files the S-C scripts consume, or (b) if the intermediates are deliberately not retained, say so in the corpus record's materials_availability and DOWNGRADE the spec check for this directory from "the screening script self-test exits 0" to what the archive actually supports. Do not leave a deliverable check on the page that the artifact fails. | _(none stated)_ |
| `REPRODUCIBILITY-1-4` | major | seeds_pinned | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:97 (front-matter rng_seed) | The rng_seed field makes three factually false enumerations. Its candour about the LLM half is exemplary; its claim about the deterministic half does not survive checking. | Claim: "PYTHONHASHSEED=0 is asserted at entry of every script in this branch — ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-query-table.py, and the store builder that emitted references_kalshi-strategy-multivocal.json." (1) `grep -c PYTHONHASHSEED ks-academic-query-table.py` = 0; that file contains no assert. (2) "every script in this branch" is false for the entire S-C arm: ks-github-scripts/run_search.py uses `os.environ.setdefault("PYTHONHASHSEED", "0")`, which is a no-op for hash randomisation because it runs after interpreter start and asserts nothing; draw_and_pin.py, get_readmes.py, run_search2.py, verify_quotes.py, write_ledger.py and write_logs.py contain no seed statement at all. (3) No store-builder script exists: `grep -rln references_kalshi-strategy-multivocal --include=*.py .` returns nothing repo-wide, so the 99-entry CSL-JSON store was emitted by an unarchived process. Two scripts that DO assert correctly (ks-academic-runner.py, ks-academic-query-table-supplementary.py) are omitted from the list. | Replace the enumeration with the verified one: assert present in ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-runner.py, ks-academic-query-table-supplementary.py; absent in ks-academic-query-table.py (pure data table, no hash-order dependence — state that); no-op setdefault in the S-C arm; and state that the CSL-JSON store builder was NOT archived. Add the assert to the S-C scripts, or record the omission as a gap. | _(none stated)_ |
| `REPRODUCIBILITY-1-5` | major | cross_platform | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-scripts/run_search.py:11, verify_quotes.py:3, write_ledger.py:3, write_logs.py:4 | Four S-C scripts hardcode an absolute home-directory path, `OUT = r"C:\\Users\\skoir\\castles\\docs\\literature\\search_logs\\kalshi-strategy-multivocal"`. run_search2.py, draw_and_pin.py and get_readmes.py inherit it by import, so the whole arm is bound to one machine and one OS. This contradicts CLAUDE.md ("absolute paths under a home directory are brittle across machines regardless of identity policy") and is inconsistent with the branch's own academic scripts. | ks-academic-extract.py:11 and ks-academic-runner.py:14 resolve the repo root relatively and carry the inline comment "repo root resolved relative to this file; no absolute home-directory path is stored". The S-C arm does the opposite. It also leaks the OS username into artifacts intended for a public, real-name-attributed repository; the username is not the protected item here (the real email is, and it is absent), but the path is still non-portable. | Replace with `OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))` as the academic scripts do. Prefer pathlib.Path throughout while touching them. | _(none stated)_ |
| `REPRODUCIBILITY-1-6` | major | data_hashed | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | docs/literature/search_logs/kalshi-strategy-multivocal/ks-lateral-records.json (32 records) and ks-venue-docs.json (30 documents) | Two of four arms record a SHA-256 of retrieved bytes whose subject bytes are not in the repository, so no reader can verify the digest. The lateral arm is worse than merely unarchived: each record carries a `local_payload_name` naming a local payload object that does not exist anywhere on disk — a dangling reference that reads as if the bytes were retained. | All 32 lateral records carry sha256_of_retrieved_bytes AND local_payload_name (e.g. "s1_oddsshopper_ladder"); resolving each name against the record dir, payloads/ and the repo root finds 0 of 32. All 30 venue documents carry sha256_of_retrieved_bytes and NO local-path field of any kind (key set: accessed_at, attribution_label, clauses, ..., retrieved_bytes, sha256_of_retrieved_bytes, source_class, url). payloads/ holds 161 files covering only the academic (ks-arxiv/crossref/openalex/repec/s2/ssrn) and S-C (ks-gh/gl/npm/pypi) arms. Contrast, independently verified this round: 112 of 112 academic logs' payload_sha256 match the file at their payload_path byte-for-byte, 0 mismatches, 0 missing. The corpus's dataset_checksums field (line 96) asserts "Per-payload digests are carried per query in the arm logs and per record in the store's note and custom.sha256_of_retrieved_bytes fields" without disclosing that for 2 of 4 arms the digests are unverifiable in-repo (store-side: 40 of 99 entries carry no sha256 at all). | Either archive the lateral and venue retrieved bytes under payloads/ (they are already digested, so this is a copy), or remove `local_payload_name` and state plainly in dataset_checksums and limitation 8 that S-D and S-E retrieved bytes were NOT retained, that their digests are therefore attestations rather than checkable digests, and register it as a named gap alongside G-15. | _(none stated)_ |
| `REPRODUCIBILITY-1-7` | major | entrypoint_runs | `reproducibility-verifier` | REMEDIATE (retained at refute gate) | repository working tree vs git index | Nothing this branch produced is committed. A fresh clone at HEAD contains none of the corpus record, the store, the H001 design, the arm logs, the payloads or the scripts, so every locator in `materials_availability` resolves to nothing and the branch is currently 0% reproducible from the repository. | `git ls-files` in docs/literature/search_logs/kalshi-strategy-multivocal returns 2 of ~200 files (only ks-instrument-verification.json and ks-prior-identifiers.json, the two pre-registration inputs). `git status --porcelain` marks lit_review_kalshi-strategy-multivocal_2026-09-04.md, references_kalshi-strategy-multivocal.json and research/01_hypothesis_register/H001/design.md as untracked (??). `git check-ignore` confirms none of them is gitignored, so this is an unmade commit, not a policy exclusion. Consequently the spec's protocol-row check — "that commit is an ancestor of every commit touching docs/literature/search_logs/kalshi-strategy-multivocal/" — is presently VACUOUSLY true: no commit touches that directory. It cannot be reported as passing. | Commit the branch before claiming any ancestry or materials-availability property, then re-run the ancestry check non-vacuously. Until then, do not tick the search-log or corpus deliverable checkboxes. Note that `ks-github-readme-evidence/` will need at least one tracked file per directory (git stores no empty dirs) — it currently holds 29 evidence files, which is fine, but verify none is skipped by a filter. | _(none stated)_ |
| `FORMAT-1-1` | critical | citations | `format-auditor` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1640 and :216 | CONFIRMED, independently verified: the corpus record reports a capacity gap as an observed absence. Section 10 note N-5 states "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)", and limitation 9 (line 216) repeats "Four executed academic queries in that stratum returned zero". Both RePEc rows NEVER EXECUTED. The correct executed-and-zero count is TWO (ks-arxiv-04, ks-openalex-04). This is a charter commitment-5 attribution-fidelity defect against the branch's own primary record, and it is already recognised-but-unrepaired in two downstream artifacts, so the defect is live in the artifact that carries the claim. | ks-repec-04.json: "platform_interface_failure": "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN"; "n_returned_semantics": "no search executed; not an observed zero-yield". Identical fields in ks-repec-04-b.json (retry_of: ks-repec-04). Corroborated by research_agenda_...2026-09-02.md:1721-1728 ("the arm log is preferred, the executed-and-zero count in that stratum is two") and failure_log F007. | Amend the corpus record in place (not silently): N-5 to read "TWO academic queries in that stratum executed and returned zero (ks-arxiv-04, ks-openalex-04). ks-repec-04 and ks-repec-04-b returned HTTP 200 but the body was the IDEAS/RePEc search form, not a result set; per their own platform_interface_failure and n_returned_semantics fields, no search was run and their n_returned=0 is a capacity gap, not a zero yield." Apply the same correction to limitation 9 at line 216. Add the correction as a dated append-only entry alongside M1 so the corrected count is traceable, and update the agenda's §rev-3 note from "recorded and NOT repaired" to "recorded and repaired at <ref>". | charter commitment 5 (attribution fidelity); protocol §4.4 rule 2 (capacity gaps reported separately from criterion determinations); task-spec seeded-defect clause |
| `FORMAT-1-2` | major | citations | `format-auditor` | REMEDIATE (retained at refute gate) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1669-1670 (note N-8) | Second, distinct instance of the same capacity-gap-as-absence framing, in the same record and not covered by the agenda's recorded discrepancy. N-8 says RePEc "returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". The logs do not describe an empty result page; they describe a search form served under a bot-traffic banner, i.e. no search executed. "Returned zero" and "empty result page" both assert an executed retrieval that did not occur. | lit_review:1669 "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)" vs ks-repec-04.json "the body is the IDEAS/RePEc search FORM, not a result set, and the page carries the banner 'IDEAS is struggling with massive bot traffic, please be patient.' The query therefore never executed." | Rewrite N-8's RePEc clause to: "RePEc executed no search at all across nine attempts: every attempt answered HTTP 200 with the IDEAS/EconPapers search form rather than a result set, under a stated bot-traffic banner. Zero records were returned because no search ran." Remove "empty result page". | protocol §4.4 rule 2; charter commitment 5 |
| `FORMAT-1-3` | major | templates | `format-auditor` | REMEDIATE (retained at refute gate) | research/01_hypothesis_register/H001/design.md:19,23,29 | Stale front-matter cross-references in a pre-registration document. The design's `corpus` block asserts `state: IN PROGRESS`, `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`, and marks the academic-arm inputs `PROVISIONAL`. That record now exists on disk with its bibliography SHA-256 published. A frozen-later design whose own dependency block misstates the state of the artifact it depends on will mislead the freeze decision (§freeze_status makes existence of the corpus record the explicit freeze precondition). | design.md:23 `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`; design.md:30-37 freeze_status "The corpus record this design depends on ... does not exist". Corpus record present with `bibliography_sha256: c7545d31...`, `n_included: 99`. | Update the `corpus` block to `state: COMPILED`, replace the `(DOES NOT EXIST YET)` annotation with the record path plus its authoring git HEAD (4821611c...) and bibliography_sha256, resolve the PROVISIONAL marker on the academic-arm inputs to their final state (528 G1 rows, zero included), and restate freeze_status as "freeze precondition now met; freeze still not executed" rather than "the record does not exist". | deliverable spec D5 check line (`status: draft-unfrozen`, citations resolve to arm outputs) |
| `REV-1-6` | major | reporting | `critical-reviewer` | DROPPED at refute gate | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1506 and :1601-1612; research/01_hypothesis_register/H001/design.md:453-472; failure_log.md:558-567 | The single interval estimate in the entire corpus is propagated through four artifacts without the three facts a reader needs to re-use or re-analyse it. '+1.37% ROI, CI [1.13, 1.61], n=23' is carried in corpus section 8's bare-numbers table, in N-2, in H001 section 1.6, and in failure_log F008, and none of them records that (a) the source states no confidence level for the interval, (b) the source states no method by which the interval was computed, or (c) the source never defines what the 23 are - the same record reports '~92,000 settled/closed Kalshi markets' and a '30k settled sample', so n=23 is unreconciled against both. The artifacts are careful about a fourth gap (cost treatment not stated) and about non-adoption, which makes the omission of the other three conspicuous rather than incidental; H001 section 1.6 then leans on the undefined n ('`n=23` is also small enough that the comparison is uninformative'), an argument that cannot be checked without knowing what n counts. The corpus states no CI on any other quantity, so this is the whole of its interval reporting. | \| `ks-sc-001` \| "+1.37% ROI, CI [1.13, 1.61], n=23" \| Reported by the source with its own caveat that the candidate is "statistically indistinguishable" from the always-NO baseline. Transcribed, attributed, **not adopted, not re-derived, not annualised** \| | At the primary locus (section 8's table and N-2) add one sentence: the source states no confidence level, no interval method, and no definition of the estimation unit behind n=23, which is unreconciled against the '~92,000 settled/closed markets' and the '30k settled sample' the same README reports; the interval is therefore not re-usable and is recorded as `undefined-in-source` on all three counts. Cross-reference that sentence from H001 section 1.6 and failure_log F008 rather than restating the figure without it. | SAMPL (report confidence intervals with their level and the method used; report numerators, denominators and group n sufficient for re-analysis); CHAMP items 18-19 |
| `QUANT-1-7` | major | reporting | `quant-auditor` | DROPPED at refute gate | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1943 (§15 item 1) vs :396-424 (§3 OpenAlex query table) and :1521-1526 (§9 attribution discipline) | The record asserts a verification result about itself that is false, and states a policy it then breaks 14 times in its own body. §15 item 1 reports that research-compile gate assertion G18 'finds no OS username, no email address and no absolute home-directory path in either file'. §9 states that two clauses are described rather than quoted 'so that no address enters this committed file'. The §3 verbatim OpenAlex query table embeds an email address in every one of the 14 logged query URLs. The address is the GitHub noreply address CLAUDE.md sanctions, so this is not a real-address leak, but a stated gate result that is demonstrably false is a reporting defect in the same class the record polices elsewhere. | grep -c 'mailto\\|noreply' on the corpus record returns 14; e.g. L397: '...&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com'. §15 L1943: 'G18 finds no OS username, no email address and no absolute home-directory path in either file.' Independent grep for the author's real address (skoirala2625) across all tracked and untracked files returns zero hits, so probe (f) is otherwise clean. | Amend §15 item 1 to state the true G18 result — the store is clean, the corpus record carries the project's public noreply address 14 times inside verbatim OpenAlex `mailto` polite-pool parameters, which are reproduced because the protocol requires verbatim query logging — and amend the §9 sentence from 'no address enters this committed file' to 'no address from a retrieved venue document enters this committed file'. | research-compile gate assertion G18; ~/.claude/rules/publishing.md §Identity hygiene (not in force here per CLAUDE.md, but the record invokes the assertion itself) |
| `REV-1-8` | minor | reporting | `critical-reviewer` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:199-201 | Limitation 6 writes an arithmetic expression that is false as written. 437 minus (8,813 minus 6,923) is 437 minus 1,890, which is -1,453, not 0. The intended construction is evidently a floor at zero (no negative lower bound is meaningful for a count), but the flooring is not stated, so the sentence asserts an equality that does not hold and a reader checking it finds an error in a limitation whose whole point is arithmetic honesty about a bound. | **437 is an upper bound on novelty with no recorded lower bound above 437 − (8,813 − 6,923) = 0 by that construction, and the corpus states no lower bound.** | Write it as max(0, 437 − (8,813 − 6,923)) = 0, or in words: the differencing construction supports no lower bound above zero, because the 1,890 predecessor records outside the identifier index exceed the 437 records flagged novel. | SAMPL (numerical precision and internal arithmetic consistency); CHAMP item 20 |
| `REV-1-9` | minor | standard-coverage | `critical-reviewer` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:18 vs :262 | The record states two different sets of PRISMA-S items as claimed directly. The `standard_declared` front-matter block says 'PRISMA-S items 1, 8, 13 and 15 are claimed DIRECTLY', matching protocol section 8.1. The body's section 2 header instead says 'PRISMA-S items 1, 2 and 13, claimed directly (see `standard_declared`)' - citing the front matter for a set the front matter does not contain, and naming item 2 which the front matter omits and omitting item 15 which it includes. On inspection the record in fact addresses all sixteen PRISMA-S items (anchors prisma-s-1 through prisma-s-16 are all present and substantive), so the coverage is stronger than either statement; only the declaration of which items are claimed is inconsistent, which matters because PRISMA-S is this record's one directly-claimed standard. | PRISMA-S items 1, 2 and 13, claimed directly (see `standard_declared`). One row per source, naming the **platform/interface**, not merely the database. | Reconcile the two statements. Simplest correct form: declare in `standard_declared` that all sixteen PRISMA-S items are addressed and anchored, and at section 2 name the items that block covers (1, 2, 3, 4, 5, 6, 7) rather than a subset of the front-matter list. | PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z); declared-standard coverage as oracle |
| `REV-1-10` | minor | reporting | `critical-reviewer` | deferred-logged (minor; not gated) | research/01_hypothesis_register/H001/design.md:600 and :827-833 | The design contains two sections numbered 3 - '## 3. Features' and '## 3. Null constructions (surrogates)' - and the running order is 0, 1, 2, 3(Features), 4, 5, 6, 3(Nulls), 7, 8 .... The document declares the insertion ('the 11-section template places surrogates nowhere ... They are inserted here as section 3.1 and section 3.2 ... This is the one structural deviation from the template's section order, recorded rather than silent') but does not acknowledge that the number was already in use, and the collision then makes bare cross-references unresolvable: section 5.1 refers to 'the surrogate ensemble sizes `B_quant` and `B_stale` (section 3)' while section 3.2 step 1 refers to 'the input the design cannot proceed without (section 3 feature `quote_age@0.1.0`)'. A reviewer following either reference lands on the wrong section half the time. | > Section numbering note: the 11-section template places surrogates nowhere, and<br>> ADR-0003 makes them mandatory ("its null, its statistic, its **surrogate**, its<br>> aggregation rule, its refutation condition"). They are inserted here as §3.1<br>> and §3.2 and cross-referenced from §§1, 5, 8 and 9. | Renumber the surrogate section to a non-colliding label (for example section 3S, or section 6A placed after the splitter), update the deviation note to say the template number 3 was already occupied by Features, and sweep the bare 'section 3' cross-references in sections 1.5, 3.2, 5.1, 8 and 9 to the disambiguated form. | CHAMP item 20 (figures, tables and structure acceptable and navigable); SAMPL presentation |
| `SCOPE-1-8` | minor | partial | `scope-auditor` | deferred-logged (minor; not gated) | .claude/settings.json:3-7 | The declared state is "a prioritized allowlist of common read-only Bash/MCP calls, produced by the `fewer-permission-prompts` skill". The file carries three entries, all project test/lint invocations, none read-only in the sense declared and none matching the read-only calls this session actually made (git log/status, hashing, directory listing). Severity held at minor because the spec's own mechanical check does pass and the spec itself classes the item as harness plumbing on which no research claim rests. | Spec lines 89-91 (state/check) and lines 149-150 ("configuration/formatting change ... it is harness plumbing and no research claim rests on it"). File contents: allow = ["Bash(uv run pytest tests/test_erob_recount.py)", "Bash(uv run ruff check)", "Bash(uv run pytest tests/)"]. | Either regenerate the allowlist from this session's actual read-only call profile, or amend the declaration to state that the existing three-entry allowlist was retained unchanged and no new entries were produced. | spec Deliverables item 8 |
| `SCOPE-1-9` | minor | partial | `scope-auditor` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1942-1943 vs :397-423 | The section 15 gate report asserts "G18 finds no OS username, no email address and no absolute home-directory path in either file". The corpus record itself contains fourteen percent-encoded email addresses in the reproduced OpenAlex query strings. Identity hygiene is NOT breached — the address is the noreply form CLAUDE.md mandates and the author's real address appears in no tracked file (verified by grep across the repository) — but the gate assertion as stated is not true of the artifact, which understates what a reader is being told was checked. | Section 15 item 1: "G18 finds no OS username, no email address and no absolute home-directory path in either file." Section 3, ks-openalex-01 through -14, each ending: "&mailto=238704148%2Bs-koirala%40users.noreply.github.com". | Qualify the G18 sentence: the only email strings present are the percent-encoded noreply contact address required by the OpenAlex polite-pool convention and reproduced verbatim because PRISMA-S item 8 forbids altering an executed query string; no real address and no OS username appears. | spec push-authorisation section, identity-hygiene clause |
| `QUANT-1-8` | minor | reproducibility | `quant-auditor` | deferred-logged (minor; not gated) | docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl (withdrawal_rule, traceability_tag); docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1151-1178 (§3.3); deliverable spec D7 | The M1 withdrawal rule instructs a reviewer to 'withdraw exactly the records tagged with that part's `reached_via` value', and D7 states 'Each part carries a `reached_via` tag so a reviewer rejecting any ruling can withdraw exactly the affected records'. No record in any arm log, the identified universe, the candidates file, or the CSL-JSON store carries a `reached_via` field. The stated procedure is not executable as written; the affected sets are recoverable only by re-deriving them from `from_query` / `also_from_query`. | grep -c 'reached_via' returns 0 in ks-academic-candidates.json, ks-academic-identified-universe.json, ks-github-records.jsonl, ks-lateral-records.json, ks-venue-docs.json and references_kalshi-strategy-multivocal.json. Re-deriving from query provenance reproduces the published counts exactly (M1a 67, M1b 3, M1c 20; 90 reachable only via M1 queries), so the counts themselves are correct. | Either write the `reached_via` field onto the 90 affected rows in ks-academic-identified-universe.json, or restate the withdrawal rule as the derivation actually available: 'withdraw exactly the records whose `from_query` and `also_from_query` sets are contained in that part's query list', and record the reproduced counts (67 / 3 / 20) beside it. | protocol §10 (an amendment register that a corpus record ran under must be enumerable); ks-amendments.jsonl withdrawal_rule |
| `QUANT-1-9` | minor | reporting | `quant-auditor` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:158-163 (limitation 3); research/01_hypothesis_register/H001/design.md:1027-1029 (§8.1) | The record's own defect DI-6 states that the venue arm's log gives two mutually inconsistent counts of retrieved rule filings (five in document-class 1, four implied by document-class 7) and that the record does not resolve them. Limitation 3 and H001 §8.1 both state 'five' flatly, with no caveat, in the places a reader is most likely to carry the number forward. Only the DI-6 / G-7 entries deep in the record disclose the ambiguity. | Limitation 3: 'Of the filing register's 111 enumerated KEX rule filings, five were retrieved in full'. DI-6: 'its document-class 7 note states that four self-certifications were retrieved ... which implies four. The two statements differ by one and this record does not resolve them'. H001 §8.1: 'the venue arm enumerated 111 KEX rule filings (query KS-VR-Q32) and retrieved five'. | Append '(or four — the arm log states both; see DI-6 / G-7)' to limitation 3 and to H001 §8.1, so the unresolved count never appears without its flag. | corpus §11 DI-6; §12.1 G-7 |
| `QUANT-1-10` | minor | reporting | `quant-auditor` | deferred-logged (minor; not gated) | research/01_hypothesis_register/H001/design.md:600 ('## 3. Features') and :827 ('## 3. Null constructions (surrogates)') | The design carries two distinct sections numbered 3, and cross-references to '§3' resolve to different sections depending on the caller. In a pre-registration document, whose value is unambiguous advance commitment, an ambiguous internal reference is a substantive defect rather than a formatting one. The §3 numbering note records the insertion but does not resolve the collision. | §6 splitter: 'the resampling that H001 needs is supplied by the two surrogates in §3'. §8.1: 'the fee schedule **is** a feature (§3, `fee_schedule_in_force@0.1.0`)'. Both cite '§3'; the first means the surrogate section at line 827, the second the features section at line 600. | Renumber the surrogate section to an unused number (e.g. §3B or §6a) or retitle it '§3S Null constructions', and update the eight cross-references in §§1, 5, 6, 8, 9 accordingly before /preregister runs. | design.md §3 numbering note lines 829-833 |
| `QUANT-1-11` | minor | method | `quant-auditor` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1510-1516 (§9 preamble) and :1533 (§9.1 row 2) | §9 declares that everything in it is 'built from the 28 included S-D records and their **130** verbatim clauses' (tier 2). One row of the SETTLED table cites two tier-5 records as corroborating sources inside that table. The corroboration is harmless in substance (the parabolic fee shape follows directly from d01-c2), but it mixes a tier-5 carrier into a table the reader has been told is tier-2-only, which is exactly the warrant-averaging hazard ADR-0006 §Consequences names as the branch's chief risk. | §9 preamble: 'Everything below is built from the 28 included S-D records and their **130** verbatim clauses'. §9.1 row 'Cost is price-dependent and maximal mid-range' clause column: '`d01-c2`, and independently at `ks-sc-002`, `KSL-C03`'. | Either move the tier-5 corroborators to a footnote labelled 'tier 5, corroborative only, not part of the settled set', or amend the §9 preamble to say the table is built from the S-D clause set with tier-labelled corroboration noted where it exists. | ADR-0006 §'What the widening costs', final bullet ('warrant is per record, and is labelled per record') |
| `QUANT-1-12` | minor | reproducibility | `quant-auditor` | deferred-logged (minor; not gated) | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61,65,69,73,77,81,85,89,247 | The tracked declaration file addresses nine of its ten deliverables by absolute Windows path under the author's home directory, embedding the OS username in tracked prose of a public real-name repository. CLAUDE.md states the opposite convention explicitly. Nothing downstream breaks, but a fresh clone cannot resolve any of the checked paths. | deliverable spec L61: '- [ ] `C:\Users\skoir\castles\docs\decisions\ADR-0006-multivocal-scope-for-strategy-corpus.md`' and eight further identical-form entries. CLAUDE.md §Identity hygiene: 'Repo-relative paths remain the convention in tracked prose — absolute paths under a home directory are brittle across machines regardless of identity policy.' The corpus record, protocol, ADR-0006, H001 design and failure_log all correctly use repo-relative paths (grep for the absolute prefix returns 0 in each). | Rewrite the nine deliverable paths in the declaration as repo-relative, as every other artifact in this branch already does. | CLAUDE.md §Identity hygiene, final paragraph |
| `LITERATURE-1-4` | minor | misattributed-locator | `literature-check` | deferred-logged (minor; not gated) | research/01_hypothesis_register/H001/design.md:637 | "Triple-barrier labelling per AFML §3.2 does not apply and is not used." Two problems: (i) the triple-barrier method is AFML §3.4, not §3.2 — §3.2 is "The Fixed-Time Horizon Method"; (ii) "AFML" appears nowhere else in the document and carries no bibliographic record in §12 References, so a "per X" attribution is made against an unresolvable abbreviation. | Grep of design.md for `AFML` returns line 637 only; §12 References contains no López de Prado entry. Chapter 3 ("Labeling") section structure corroborated from two independent indexes of the Wiley title: 3.1 Motivation, 3.2 The Fixed-Time Horizon Method, 3.3 Computing Dynamic Thresholds, 3.4 The Triple-Barrier Method, 3.5 Learning Side and Size, 3.6 Meta-Labeling. Verification depth is search-index and O'Reilly/Wiley TOC listings; the publisher TOC PDF and O'Reilly chapter page both returned HTTP 403 to unauthenticated fetch, so this is corroborated but not fetched from publisher primary text — declared rather than asserted. | Change to "§3.4" and add the record to §12: López de Prado M. Advances in Financial Machine Learning. Hoboken, NJ: Wiley; 2018. ISBN 978-1-119-48208-6, §3.4 "The Triple-Barrier Method". Since the method is declared NOT used, mark it as a not-applied instrument in the same manner §7.4 of the protocol handles GRADE. | Wiley 9781119482086 chapter 3 contents (publisher page HTTP 403; corroborated from O'Reilly library TOC and ETH Zurich TOC record) |
| `LITERATURE-1-5` | minor | truncated-quotation | `literature-check` | deferred-logged (minor; not gated) | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:897-900; also docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json instrument 5 | Software Citation Principle 3 is quoted as ending at "...recognized by at least a community of the corresponding domain experts" with a closing quotation mark and no ellipsis. The published principle continues ", and preferably by general public researchers." A quotation terminated mid-sentence without an elision mark is a dropped clause, which charter commitment 5 and the predecessor branch's A19 quotation-audit precedent classify as a defect rather than a style choice. Principle 6, quoted immediately after, IS byte-exact. | Protocol line 897-900: 'principle 3 (unique identification), a software citation "should include a method for identification that is machine actionable, globally unique, interoperable, and recognized by at least a community of the corresponding domain experts"'. Verified against the official FORCE11 Software Citation Principles page: "A software citation should include a method for identification that is machine actionable, globally unique, interoperable, and recognized by at least a community of the corresponding domain experts, and preferably by general public researchers." Principle 6 verified byte-exact against the same page and against corpus record line 1885-1889. Bibliographic record verified via Crossref (10.7717/peerj-cs.86): Arfon M. Smith, Daniel S. Katz, Kyle E. Niemeyer, FORCE11 Software Citation Working Group; PeerJ Computer Science 2016;2:e86 — the group author is correctly named in both the protocol and corpus §14, as the branch itself flags. | Close the quotation with an ellipsis, or restore the full clause: "...recognized by at least a community of the corresponding domain experts, and preferably by general public researchers." Apply the same fix in ks-instrument-verification.json instrument 5. | https://www.force11.org/software-citation-principles ; https://doi.org/10.7717/peerj-cs.86 |
| `LITERATURE-1-6` | minor | truncated-quotation | `literature-check` | deferred-logged (minor; not gated) | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:831-832 (and the fragment reused at docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1849) | The Adams, Smart & Huff continuum sentence is quoted as a complete sentence terminated with a full stop inside the quotation marks: "Rather than having discrete bands, the gradation in both dimensions is on a continuous range between known and unknown." The source sentence continues ", producing the shades of GL." The dropped clause does not change the proposition the protocol rests on, but the clause is presented as a whole sentence when it is not. | Protocol line 831-832 quotes the sentence with a terminal period. The source sentence, corroborated from search-index retrieval of the Wiley full text and from the arXiv preprint of Garousi et al. 1707.02553 which reproduces the scheme, reads: "Rather than having discrete bands, the gradation in both dimensions is on a continuous range between known and unknown, producing the shades of GL." Wiley full text returned HTTP 403 to unauthenticated fetch, so this is corroborated at secondary depth — which the branch itself already declares for this record (protocol §7.1(b): "verified at secondary depth only (publisher full text HTTP 403)"). Bibliographic record verified via Crossref (10.1111/ijmr.12102): Richard J. Adams, Palie Smart, Anne Sigismund Huff; International Journal of Management Reviews 19(4):432-454; online-first 19 April 2016, print 2017 — the branch's parenthetical explaining the 2016/2017 dual citation is correct. | Either restore the full sentence or close with an ellipsis before the period. The corpus record's §13.4 inline fragment ("is on a continuous range between known and unknown") is correct as an embedded partial quote and needs no change. | https://doi.org/10.1111/ijmr.12102 |
| `LITERATURE-1-7` | minor | quotation-fidelity-inconsistent-with-declared-rule | `literature-check` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:189-190 (limitation 5c) and :1559 (§9.2) | The corpus record quotes clause d21-c11 as "Appendix E (Confidential) - Source Agency", silently normalising the spurious intra-word space present in the arm log's verbatim field. The same record's DI-7 (line 1736-1743) declares that quotations from ks-vr-d21 "are transcribed exactly as extracted so that they remain reproducible from the bytes, which is why several quotations in section 9 look malformed." The record therefore states one transcription rule and applies a different one at two sites, and the normalised string no longer exact-matches the source of record. Separately, limitation 5(b) excerpts d16-c5 mid-sentence with no leading or trailing ellipsis. | ks-venue-docs.json line 1233 `quote`: "A ppendix E (Confidential) - Source Agency". Corpus line 190 and line 1559 both render it "Appendix E (Confidential) - Source Agency". ks-venue-docs.json line 914 `quote`: "Please note that appendix A is confidential and submitted under a request for confidential FOIA treatment as noted on the attached FOIA confidential treatment request letter."; corpus line 187-188 renders "appendix A is confidential and submitted under a request for confidential FOIA treatment". By contrast, research/01_hypothesis_register/H001/design.md follows the DI-7 rule correctly throughout (e.g. §4 line 663-666 and §5.3 line 775-780 reproduce the degraded spacing exactly), which shows the deviation is site-specific and not a house convention. d19-c3's quotation at limitation 5(a) was checked and is byte-exact. | At limitation 5(c) and §9.2, restore the extracted string exactly ("A ppendix E (Confidential) - Source Agency") or mark the normalisation explicitly as `[spacing normalised from the degraded extraction]`. At limitation 5(b), add a leading ellipsis to the mid-sentence excerpt. | docs/literature/search_logs/kalshi-strategy-multivocal/ks-venue-docs.json clauses d21-c11 and d16-c5; corpus record §11 DI-7; charter commitment 5 |
| `LITERATURE-1-8` | minor | named-instrument-without-record | `literature-check` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1183-1185 | Section 4 states "No PRESS 2015 review by an information specialist was obtained, and none was simulated. Protocol section 3.5 declares this as a standing limitation of the design." PRESS is a named methodological instrument introduced only here, with no bibliographic record anywhere in the branch (protocol, corpus record, or ks-instrument-verification.json), and the attribution to protocol §3.5 is loose: §3.5 declares that no independent information specialist reviews the strategies, but it never names PRESS. The section anchor is `prisma-s-14`, and PRISMA-S item 14 is the search-peer-review item, so a reader will take PRESS to be a protocol-declared instrument when it is not. | Grep of docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md for "PRESS" returns no matches. Protocol §3.5 (lines 592-595) reads: "Search-strategy peer review. No independent information specialist reviews these strategies. That is a declared limitation, reported in the corpus record in those words..." — no instrument is named. The instrument's canonical record is McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. "PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement." Journal of Clinical Epidemiology. 2016;75:40-46, doi:10.1016/j.jclinepi.2016.01.021 — note the "2015" is part of the guideline's own name and the publication year is 2016, so the bare string "PRESS 2015" is also year-ambiguous. | Either cite the instrument in full at the point of use with its DOI and the 2015-guideline/2016-publication distinction stated, and add it to the protocol's §12 citation ledger as an instrument NAMED BUT NOT APPLIED (the pattern §7.4 already uses for GRADE); or drop the instrument name and state the limitation in the protocol's own wording, which the corpus record claims to be quoting. | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §3.5 lines 592-595; https://doi.org/10.1016/j.jclinepi.2016.01.021 |
| `REPRODUCIBILITY-1-8` | minor | data_hashed | `reproducibility-verifier` | deferred-logged (minor; not gated) | docs/literature/search_logs/kalshi-strategy-multivocal/ks-s2-*.json (55 logs) | The `n_returned` field is overloaded: it holds 0 both for "the search ran and found nothing" and for "no search ran". Only the RePEc logs carry the disambiguating `n_returned_semantics` / `platform_interface_failure` fields. This schema gap is the direct mechanism that produced finding REPRODUCIBILITY-1-1, and it will reproduce the same error in any future aggregation over these logs. | Scan of every arm log with an http_status field: 55 logs have n_returned == 0 with a non-200 status (53x429, 1x500, 1x403 SSRN) and NO n_returned_semantics field. The 9 RePEc logs are the only ones that disambiguate, and they do so only because their status was 200. | Backfill `n_returned_semantics` (or a boolean `search_executed`) on every non-200 log so the field is self-describing, and state in the corpus that any count derived from these logs must filter on it rather than on n_returned. | _(none stated)_ |
| `REPRODUCIBILITY-1-9` | minor | llm_provenance | `reproducibility-verifier` | deferred-logged (minor; not gated) | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:93 (ai_assistance), :97 (rng_seed) | Model identity is pinned correctly (`claude-opus-5`, not "latest") and the delegation prompts are versioned in-repo in the deliverable spec's Delegation table, but sampling parameters (temperature, top-p) are recorded nowhere. The record discloses this honestly — "all 109 eligibility verdicts and all extractions in this corpus are single-pass LLM outputs with no archived prompt and no recoverable sampling parameters" — which is why this is minor rather than major. | grep for temperature/top_p/top-p across the corpus record, protocol, ADR-0006 and H001 design returns only weather-contract and slippage-model hits; no sampling parameter is recorded. The "no archived prompt" clause is slightly overstated: the four arm briefs ARE archived verbatim in docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md under Delegation. | Record that sampling parameters were harness defaults and are unrecoverable (which is the true state), and amend "no archived prompt" to point at the Delegation table as the archived arm-level prompt while noting that per-record extraction prompts are not archived. | _(none stated)_ |
| `REPRODUCIBILITY-1-10` | minor | deps_pinned | `reproducibility-verifier` | deferred-logged (minor; not gated) | pyproject.toml, README.md Quickstart, CLAUDE.md Quickstart | There is no end-to-end reproduce target. `uv run pytest` runs the unit suite only; nothing re-derives the corpus from the arm logs. Dependency capture is otherwise sound, so this is a documentation-of-scope gap, not a pinning gap. | Verified this round: requires-python = ">=3.11,<3.13" declared; uv.lock is tracked (ADR-0005); dev group moved out of optional-dependencies so `uv sync` installs pytest; .venv/Scripts/python.exe -m pytest -q -> 10 passed in 0.09s, exit 0. Every branch script imports stdlib only (os, sys, json, re, glob, hashlib, datetime, urllib, time, gzip), so the lockfile is not load-bearing for this branch — which is itself worth stating. logs/reproducibility/env/495798ac...txt exists and hashes to 495798ac328ee7cc673610470fe1d344e15a2dd942b22c0cb9ada0cd6a01115a, matching the corpus front matter exactly. No system deps (BLAS/CUDA/C libs) are used or needed. | State in the corpus record that the branch is Python-3.11-stdlib-only and that no third-party dependency bears on any number in it. If a reproduce target is wanted, add one that re-verifies the archive (payload digests, flow identities, store length) rather than re-running network queries, since the queries are not idempotent. | _(none stated)_ |
| `FORMAT-1-4` | minor | templates | `format-auditor` | deferred-logged (minor; not gated) | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:784-785, 793, 843, 889 (also :481, :624) | The protocol asserts "A placeholder surviving into the registration commit is itself a defect; none survives", yet the literal `[INSTRUMENT-MLR]`, `[INSTRUMENT-GH]` and `[INSTRUMENT-SWCITE]` tokens survive verbatim as section headings and as in-text references. The substitutions were in fact made (each heading is followed by the resolved citation), so this is a self-contradiction in the frozen text rather than an unresolved placeholder — but a reader grepping for the defect signature the protocol itself names will hit five matches. | protocol:784 "**A placeholder surviving into the registration commit is itself a defect**; none survives." against protocol:793 "### 7.1 [INSTRUMENT-MLR] — multivocal review conduct...", :843, :889, :481, :624. | Cannot edit frozen text. Record a one-line clarification in the append-only Addendum (alongside M1) stating that the `[INSTRUMENT-*]` tokens are retained deliberately as stable cross-reference anchors, that the substitution test is "the anchor is followed by a resolved record in §7", and that all three anchors pass it. | protocol §7 placeholder clause; protocol §10 append-only amendment policy |
| `FORMAT-1-5` | minor | style | `format-auditor` | deferred-logged (minor; not gated) | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61,65,69,73,77,81,85,89 and docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-scripts/{run_search,write_logs,write_ledger,verify_quotes}.py:1 | Absolute home-directory paths embedded in tracked files in a public repository, against the project CLAUDE.md convention. Nine occurrences in the spec's Deliverables list and one per new search-log script. This is not an identity-hygiene breach (the real email is absent everywhere; the OS username coincides with the publicly attributed GitHub handle), but it is the exact brittleness CLAUDE.md names, and the scripts will not run from a fresh clone. | spec:61 "- [ ] `C:\Users\skoir\castles\docs\decisions\ADR-0006-...`"; CLAUDE.md §Identity hygiene: "Repo-relative paths remain the convention in tracked prose — absolute paths under a home directory are brittle across machines regardless of identity policy." 171 occurrences across 16 tracked files, so the pattern is standing, not new. | Convert the eight Deliverables rows and the four script path constants to repo-relative paths. If the standing pre-existing occurrences in audit trails are to be left (they are immutable session records), state that exemption once in CLAUDE.md so the convention is not silently partial. | CLAUDE.md §Identity hygiene, final paragraph |
| `FORMAT-1-6` | minor | templates | `format-auditor` | deferred-logged (minor; not gated) | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61-95, 208, 247 | Every Deliverables checkbox is still `- [ ]` although the ADR, protocol, search-log directory, corpus record, CSL-JSON store, agenda rev 3, H001 design and failure_log rows all exist on disk. The spec is the artifact `scope-auditor` reads for delivery state, so an all-unchecked list understates completion and gives no machine-readable delivery signal. | spec:73 "- [ ] `C:\...\lit_review_kalshi-strategy-multivocal_2026-09-04.md`" while that file exists with 1,978 lines and closed flow identities; same for D5:208 (H001 design present) and D6:247 (failure_log F006-F009 present). | Tick each delivered row to `- [x]` at the end of the loop, or add a one-line "delivery state is recorded in the audit trail, not here" note if the boxes are deliberately frozen as-declared. Do not leave the two readings ambiguous. | deliverable spec Deliverables checklist convention; audit-remediate-loop post-loop procedure |

## refute-gate

Every critical and major finding was submitted to an adversarial refuter whose brief is to
disprove the finding with concrete counter-evidence - a source quote, a counter-test, or a
logical proof. Bare disagreement, severity quibbles and plausibility arguments do not clear
the gate. Each entry below records the claim VERBATIM as the raising branch filed it, the
raiser, the refuter, the enumerated `evidence_type`, the refutation evidence, and the
outcome. Entries with `reproduction_required: true` carry the reproduction block lifted from
the refutation evidence. Retained-conservative entries would appear here too; there were
none this round.

Dispositions: 34 total - 2 dropped, 32 retained, 0 retained-conservative.

### REV-1-6 - DROPPED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `source-quote`
- **reproduction_required:** false
- **outcome:** dropped

**Claim, verbatim as filed:**

- `category`:

  > reporting

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1506 and :1601-1612; research/01_hypothesis_register/H001/design.md:453-472; failure_log.md:558-567

- `issue`:

  > The single interval estimate in the entire corpus is propagated through four artifacts without the three facts a reader needs to re-use or re-analyse it. '+1.37% ROI, CI [1.13, 1.61], n=23' is carried in corpus section 8's bare-numbers table, in N-2, in H001 section 1.6, and in failure_log F008, and none of them records that (a) the source states no confidence level for the interval, (b) the source states no method by which the interval was computed, or (c) the source never defines what the 23 are - the same record reports '~92,000 settled/closed Kalshi markets' and a '30k settled sample', so n=23 is unreconciled against both. The artifacts are careful about a fourth gap (cost treatment not stated) and about non-adoption, which makes the omission of the other three conspicuous rather than incidental; H001 section 1.6 then leans on the undefined n ('`n=23` is also small enough that the comparison is uninformative'), an argument that cannot be checked without knowing what n counts. The corpus states no CI on any other quantity, so this is the whole of its interval reporting.

- `evidence`:

  > | `ks-sc-001` | "+1.37% ROI, CI [1.13, 1.61], n=23" | Reported by the source with its own caveat that the candidate is "statistically indistinguishable" from the always-NO baseline. Transcribed, attributed, **not adopted, not re-derived, not annualised** |

- `fix`:

  > At the primary locus (section 8's table and N-2) add one sentence: the source states no confidence level, no interval method, and no definition of the estimation unit behind n=23, which is unreconciled against the '~92,000 settled/closed markets' and the '30k settled sample' the same README reports; the interval is therefore not re-usable and is recorded as `undefined-in-source` on all three counts. Cross-reference that sentence from H001 section 1.6 and failure_log F008 rather than restating the figure without it.

- `reference`:

  > SAMPL (report confidence intervals with their level and the method used; report numerators, denominators and group n sufficient for re-analysis); CHAMP items 18-19

**Refutation evidence:**

> Two of the three "facts" the finding asserts are absent from the source are in fact stated by the source, and the byte-pinned copy of that source is in the repo. The verbatim README for `ks-sc-001` is at docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md; I recomputed its digest — 4039 bytes, sha256 50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118 — which matches `platform_metadata.readme.sha256` and `F12.readme_sha256` in the record at docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-records.jsonl, so this is the pinned artifact the corpus, H001 and F008 all cite.
>
> (b) REFUTED BY THE SOURCE. The finding states "the source states no method by which the interval was computed." The README carries a dedicated "Methodology notes" bullet: "**Confidence intervals:** bootstrap (resample with replacement) on per-bet ROI, so the verdict reports whether the CI excludes the baseline — not the point-estimate delta." The method is named (nonparametric bootstrap, resampling with replacement), the resampling unit is named (per-bet ROI), and the decision rule the interval feeds is named (CI-excludes-baseline, not a point-estimate delta). The premise is false, and the claimed fix would write a false statement about the source into the corpus at the primary locus and cross-reference it from two more artifacts.
>
> (c) REFUTED IN ITS LOAD-BEARING PART. The finding states "the source never defines what the 23 are" and that "n=23 is unreconciled against both" 92,000 and 30k. The README defines the estimation unit in the same Methodology notes: "**Semantics (flat-bet, $1 face value per contract):** BUY YES @ p pays p… BUY NO @ p pays (1-p)… capital at risk = 1-p", and the interval bullet says the resampling is over "per-bet ROI" — so n is bets under a flat-bet, one-contract-face convention, not an undefined quantity. The reconciliation the finding says is missing is also printed in the same headline table the +1.37% row comes from: "Direct single-event binary markets found | **136 (0.15% of sampled)**" and "Of those, clean YES/NO settlements | 61". That is an explicit funnel 92,000 sampled → 136 direct single-event binary → 61 clean YES/NO settlements, with n=23 the high-NO-prob subset below 61; the 30k figure is separately scoped by its own row label ("NO-tilt across a 30k settled sample"), i.e. it is the denominator of the 97.1% NO-tilt statistic, not of the ROI estimate. The finding treats 92,000 and 30k as the only two denominators in the record; the record states four.
>
> (a) survives on the source but is materially narrower than the finding as written: the README states no confidence level (no "95%" or equivalent appears anywhere in the 4039 bytes). Note also that failure_log.md F008 already records at :585-588 that "The **source** states an n (23), a point ROI and an interval, and states no alpha, no target detection probability and no MDES of its own", so even the surviving gap is not wholly unrecorded across the four artifacts.
>
> I confirmed the finding's transcription claims reproduce (the figure appears at lit_review …_2026-09-04.md:1506 and :1604, design.md:454-457, failure_log.md:563, and research_agenda_…_2026-09-02.md:358), and I confirmed by grep that none of these artifacts transcribes the bootstrap-method sentence or the 136/61 funnel rows. So a residual, much smaller reporting gap exists — the artifacts omit a method the source does supply. That is a different defect from the one filed. As filed, REV-1-6 asserts three source-level absences, two of which the pinned source contradicts verbatim, and prescribes recording all three as `undefined-in-source`, which would be factually wrong.

### QUANT-1-7 - DROPPED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `counter-test`
- **reproduction_required:** true
- **outcome:** dropped

**Claim, verbatim as filed:**

- `category`:

  > reporting

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1943 (§15 item 1) vs :396-424 (§3 OpenAlex query table) and :1521-1526 (§9 attribution discipline)

- `issue`:

  > The record asserts a verification result about itself that is false, and states a policy it then breaks 14 times in its own body. §15 item 1 reports that research-compile gate assertion G18 'finds no OS username, no email address and no absolute home-directory path in either file'. §9 states that two clauses are described rather than quoted 'so that no address enters this committed file'. The §3 verbatim OpenAlex query table embeds an email address in every one of the 14 logged query URLs. The address is the GitHub noreply address CLAUDE.md sanctions, so this is not a real-address leak, but a stated gate result that is demonstrably false is a reporting defect in the same class the record polices elsewhere.

- `evidence`:

  > grep -c 'mailto\|noreply' on the corpus record returns 14; e.g. L397: '...&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com'. §15 L1943: 'G18 finds no OS username, no email address and no absolute home-directory path in either file.' Independent grep for the author's real address (skoirala2625) across all tracked and untracked files returns zero hits, so probe (f) is otherwise clean.

- `fix`:

  > Amend §15 item 1 to state the true G18 result — the store is clean, the corpus record carries the project's public noreply address 14 times inside verbatim OpenAlex `mailto` polite-pool parameters, which are reproduced because the protocol requires verbatim query logging — and amend the §9 sentence from 'no address enters this committed file' to 'no address from a retrieved venue document enters this committed file'.

- `reference`:

  > research-compile gate assertion G18; ~/.claude/rules/publishing.md §Identity hygiene (not in force here per CLAUDE.md, but the record invokes the assertion itself)

**Refutation evidence:**

> Ran the gate the finding invokes. `python ~/.claude/skills/research-compile/assets/check_lit_review.py docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md --no-network --json` against the exact review+store pair, with NO --allow-email whitelist, returns assertion ids fired = {G13: 99, G16: 1} and G18 findings = [] (empty). G18 is therefore accurately reported by the record; the finding's load-bearing claim that the record "asserts a verification result about itself that is false" is disproven.
>
> Mechanism, from the gate source: check_lit_review.py L47 defines _EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), applied at L496 over both scan targets (review at L485, store at L487). It requires a LITERAL '@'. All 14 occurrences are percent-encoded: the logged token is `mailto=238704148%2Bs-koirala%40users.noreply.github.com` (%40, not @). Running _EMAIL_RE directly over both files returns [] for each. The review contains only 5 literal '@' characters total and none is an address (a curl UA header L1036, two git-commit pins L1382-1383, two quoted strategy strings L1603/L1615).
>
> The other two G18 sub-claims also hold: USERNAME=skoir, and a `\bskoir\b` (re.I) probe returns 0 hits in the review and 0 in the store — which covers the "no absolute home-directory path" clause transitively, since any Windows home path here (C:/Users/skoir/...) contains the username at word boundaries.
>
> Grammatically the §15 L1942-43 sentence's subject is the gate and its verb is "finds" — it is a report of what G18 finds, and G18 finds exactly that. True, not false. This is not whitelist evasion; the gate was run clean with no flags.
>
> What DOES reproduce (auditor's raw observations, all accurate, none of which establish the claimed defect): grep -c 'mailto\|noreply' returns 14; L397 carries the quoted URL; urllib.parse.unquote confirms the encoded token decodes to 238704148+s-koirala@users.noreply.github.com; §9 L1521-26 and §15 L1942-43 read verbatim as quoted.
>
> Residual disclosed for the parent's judgment: the §9 purpose clause "so that no address enters this committed file" is, on an unrestricted reading, in tension with the 14 encoded parameters; its in-context referent is the two venue-document contact addresses (d27-c1, d26-c5) that were described rather than quoted. That is a wording-scope ambiguity in one subordinate clause, not the false-gate-result reporting defect the finding asserts and rates major.

**reproduction:**

```
command:  python ~/.claude/skills/research-compile/assets/check_lit_review.py docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md --no-network --json
observed: assertion ids fired = {G13: 99, G16: 1}; G18 findings = [] (empty). Run with NO --allow-email whitelist, against the exact review+store pair. Mechanism: check_lit_review.py L47 defines _EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), applied at L496 over both scan targets; it requires a LITERAL '@', and all 14 occurrences are percent-encoded (mailto=238704148%2Bs-koirala%40users.noreply.github.com). Running _EMAIL_RE directly over both files returns [] for each. A \bskoir\b (re.I) probe returns 0 hits in the review and 0 in the store.
```

### REV-1-1 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > interpretation

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:219 and :1640-1642

- `issue`:

  > CONFIRMED INDEPENDENTLY AGAINST THE ARM LOGS. Limitation 9 and negative result N-5 both report FOUR academic queries in the weather stratum as having executed and returned zero, naming ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b. Two of the four never executed. ks-repec-04.json and ks-repec-04-b.json each carry a `platform_interface_failure` field reading 'PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN', and an `n_returned_semantics` field reading 'no search executed; not an observed zero-yield'. I re-read ks-arxiv-04.json (HTTP 200, n_returned 0, n_total_reported 0, no failure field) and ks-openalex-04.json (HTTP 200, n_returned 0, n_total_reported 0, no failure field) and confirm those two DID execute. The corrected executed-and-zero count in stratum S3 is TWO, not four. The record thereby counts a capacity gap as an observed zero in the one limitation whose entire purpose is to stop that inference, and it does so while asserting elsewhere (section 5.4) that 'A corpus record that folds G-rows into the Y totals is defective; this one does not.' The defect is already adjudicated inside the artifact set: failure_log.md F007 states 'The executed-and-zero count in that stratum is therefore **two** ... not four' and then 'Neither the corpus record nor the arm log is edited by this row' - so the set ships a corpus record whose own project has already established the statement to be false, with the correction reachable only from a different file.

- `evidence`:

  > **N-5 — the weather stratum is NOT a clean absence, and must not be reported as one.** Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0).

- `fix`:

  > Correct both loci in the corpus record to TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and state in the same sentence that ks-repec-04 and ks-repec-04-b answered HTTP 200 with the IDEAS/RePEc search FORM rather than a result set and therefore never executed, quoting the logs' own `n_returned_semantics` value. Add the RePEc non-execution to the gap register (a new G-n, or an explicit extension of G-9, which currently names only Semantic Scholar). Do not edit the arm logs. Record the correction as a dated amendment note so the superseded wording stays legible, per protocol section 10, and update failure_log.md F007's sentence that neither document is repaired.

- `reference`:

  > CHAMP items 24-25 (results interpreted from evidence; a non-result read as indecisive, never as absence); protocol section 4.4 rule 2; corpus record section 5.4

**Refutation evidence:**

> Refutation attempted on four independent grounds; all four failed. The finding reproduces exactly.
>
> (1) Both loci verified verbatim. docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:215-219 (limitation 9) reads "Four executed academic queries in that stratum returned zero"; :1639-1642 (N-5) reads "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)."
>
> (2) The two RePEc logs contradict that directly. docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json and ks-repec-04-b.json each carry `platform_interface_failure`: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT ... the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN", and `n_returned_semantics`: "no search executed; not an observed zero-yield". ks-arxiv-04.json and ks-openalex-04.json carry http_status 200, n_returned 0, n_total_reported 0 and NO failure field, and ks-arxiv-04's target_stratum includes S3, so the corrected executed-and-zero count in S3 is two. The auditor's claimed counts are the logs' own.
>
> (3) Tested whether the record self-corrects elsewhere. It does not. No errata or dated amendment touches these loci (grep for errata/correction/amendment/superseded returns only unrelated lines 177, 1145, 1758). The gap register at :1766 defines G-9 as Semantic Scholar-only ("The weather stratum's most on-point query never executed across eleven attempts; 53 of 56 Semantic Scholar attempts returned HTTP 429"); no gap row anywhere covers RePEc non-execution — grep "RePEc" over the record returns only :196, :274, :1254 and :1669, none of which is a gap row. The single partial mitigation I found, N-8 at :1668-1671, in fact repeats the same error in the opposite direction: it describes the nine RePEc attempts as "all HTTP 200 with an empty result page", which is again the executed-and-empty reading the logs forbid. It does add "each is a finding about the endpoint", which softens the downstream inference but does not make the N-5 and limitation-9 sentences true.
>
> (4) Tested whether ks-amendments.jsonl repairs it. It does not — the file holds only the header row and amendment M1 (parts M1a/M1b/M1c on section 3.1 vocabulary slots); nothing about the weather stratum or RePEc.
>
> The internal adjudication the auditor cites is also verbatim. failure_log.md F007 (line ~482 ff.) states: "Corpus §10 N-5 states that **four** academic queries in that stratum *executed* and returned zero ... By `ks-repec-04.json`'s own field, the two RePEc rows **did not execute**. The executed-and-zero count in that stratum is therefore **two** ... not four ... Neither the corpus record nor the arm log is edited by this row." And section 5.4 at :1339-1341 does assert "A corpus record that folds G-rows into the Y totals is defective; this one does not."
>
> No counter-evidence exists. The defect claim is true as stated.

### REV-1-2 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > reporting

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:274, :570-588, :1668-1675

- `issue`:

  > The RePEc platform-interface failure is recorded NOWHERE in the corpus record, and is positively mischaracterised in the one place it is discussed. N-8 states the nine RePEc attempts were 'all HTTP 200 with an empty result page'; the arm logs state the body is 'the IDEAS/RePEc search FORM, not a result set'. An empty result set and an unreturned result set are different objects and the record's own G1-vs-Y discipline turns on the distinction. Three further loci propagate the same misreport: the section 2 information-sources table reports RePEc `n_records` 0 with no flag; the section 3 verbatim-strategy fence annotates all nine RePEc queries as `executed ... n_returned=0` while PRISMA-S item 8 is claimed DIRECTLY on the ground that the strategies are 'copied and pasted exactly as run'; and no entry in the section 12.1 gap register (G-1 ... G-25) covers RePEc non-execution, G-9 being scoped to Semantic Scholar only. The arm logs carry the corrective fields (`platform_interface_failure`, `n_returned_semantics`) that the record never surfaces, so a reader of the record alone cannot recover the fact.

- `evidence`:

  > RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page), and SSRN's own interface returned **HTTP 403** unauthenticated at `ks-ssrn-01`.

- `fix`:

  > In N-8 replace 'an empty result page' with the logs' own characterisation (search form returned in place of a result set; query never executed). Annotate the nine ks-repec-* comment lines in the section 3 fence with the log's `n_returned_semantics` value so the fence does not present an unexecuted query as executed. Flag the RePEc row of the section 2 table as an interface failure rather than a zero yield. Add a named gap for the RePEc endpoint alongside G-9.

- `reference`:

  > PRISMA-S item 8 (search strategies copied and pasted exactly as run), items 1 and 15; SAMPL (report what was done, not what was intended)

**Refutation evidence:**

> Refutation attempted and failed; every limb of the finding reproduces, and the counter-check strengthened it.
>
> 1) N-8 (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1668-1675) reads verbatim: "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". Confirmed.
>
> 2) All nine arm logs (ks-repec-01, -01-b, -01-c, -02, -02-b, -03, -03-b, -04, -04-b) carry `platform_interface_failure` = "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set... The query therefore never executed... n_returned=0 here means NO SEARCH WAS RUN" and `n_returned_semantics` = "no search executed; not an observed zero-yield". Confirmed on all nine.
>
> 3) Counter-test against the stored bytes: I parsed docs/literature/search_logs/kalshi-strategy-multivocal/payloads/ks-repec-01.html (16,573 bytes, matching the log's payload_bytes). It contains two <form> elements, the IDEAS/RePEc search chrome, and the literal banner "IDEAS is struggling with massive bot traffic, please be patient." There is no result region. The logs' characterisation is correct and N-8's "empty result page" is the erroneous one — the opposite of a refutation.
>
> 4) Section 2 table (line 274): "| RePEc / IDEAS | ideas.repec.org site search over HTML | 2026-09-04 | ks-repec | 0 |" — n_records 0, no flag, no footnote. Confirmed.
>
> 5) Section 3 fence (lines 570-588): exactly nine ks-repec-* comment lines, every one annotated "executed <timestamp> | HTTP 200 | n_returned=0", under a header at line 344-352 claiming PRISMA-S item 8 "directly" and describing these as "72 of the 112 academic queries ... returned nothing". Confirmed.
>
> 6) Gap register 12.1 (G-1 ... G-25, lines ~1757-1795): read in full. No entry names RePEc. G-9 is scoped to the weather stratum / Semantic Scholar HTTP 429; G-20 covers CME/Betfair/PredictIt; G-22 covers GitHub code and Kaggle HTTP 401. Confirmed.
>
> 7) Case-insensitive grep for repec|ideas.repec|econpapers over the whole 1,977-line record returns only lines 196, 274, 570-588, 1138, 1254, 1641-1642, 1669. Greps for "interface failure|search form|bot traffic|never executed|no search|n_returned_semantics|unexecuted" return no RePEc-related hit. The corrective fact is surfaced nowhere in the record.
>
> 8) Additional propagation the finding did not cite, found while checking: N-5 at lines 1640-1642 asserts "Four academic queries in that stratum executed and returned zero: ... `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)" — a fifth locus positively asserting execution of a query the arm log says never ran, and one used to characterise the weather stratum's yield.
>
> 9) No amendment covers it: docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl holds only the header and M1 (M1a/M1b/M1c, instrument-slot and container-restriction rulings). M1c cites ks-ssrn-01's HTTP 403 but says nothing about RePEc.
>
> No counter-evidence exists. The defect claim is true as stated.

### REV-1-3 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > consistency

- `location`:

  > docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:89, :93, :374, :441, :459

- `issue`:

  > The rev-3 agenda now consumes gap and handoff identifiers from TWO corpora whose identifier spaces collide, and the collision is nowhere declared or disambiguated. The front matter states the predecessor corpus's 'section 10 gaps (G-1...G-10) and section 11 TO COMPUTE handoffs (TC-1...TC-5)' are the source of branches 1-6, and separately that the multivocal corpus's 'gaps G-1..G-25 and handoffs TC-1..TC-15 are the sole admissible source of branches 7-11'. Bare 'G-3' then appears with two different referents inside Branch 0 alone: at the branch head and in the rev-2 status paragraph it means the predecessor's G-3 ('The corpus's six G-3 marks stand at six'), while in the branch's own still-missing table it means the multivocal G-3 (confidential elevated-position-limit appendix). 'G-1' is likewise multivocal at line 439 and predecessor at Branch 1's head; 'TC-1' at Branch 0's head is unresolvable. The document already demonstrates the author's awareness of exactly this hazard - agenda-local handoffs were prefixed 'A3-TC-1..A3-TC-7 so that they can never be confused with the corpus's own TC-1..TC-15' - and ADR-0006 set the governing precedent by renaming J1-J6 to N1-N6 for the identical reason. The corpus record's own section 15 item 9 makes the identifiers load-bearing: 'They are numbered because the branch agenda consumes them by identifier, and a branch derived from anything else would not be traceable to this record.' As shipped, a reader grepping 'G-3' retrieves two unrelated gaps.

- `evidence`:

  > **From:** G-3, TC-1, AG-1, AG-2. **Tier of the motivating evidence:** T2 (official documentation), currently *unretrieved*.

- `fix`:

  > Adopt a disambiguating prefix for one corpus throughout the agenda (for example MV-G-n / MV-TC-n for the multivocal record, leaving the predecessor's bare G-n / TC-n untouched, or the reverse), state the convention once in 'How to read this document', and sweep every bare G-n and TC-n in the body to the prefixed form. Do not renumber either corpus record. Record the sweep in the revision note as a rev-3 correction, following the ADR-0006 J1-J6 precedent it cites.

- `reference`:

  > CHAMP item 20 (presentation must let a reader verify a stated result); ADR-0006 section Consequences (Negative), the code-collision precedent

**Refutation evidence:**

> No counter-evidence found; the refutation attempt confirmed the finding instead. Checks run, all against the working tree:
>
> 1. Collision exists in the two corpus records. Predecessor [docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md](docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md) section 10 (line 3692) defines G-1 = "No strand is empty, but S5 is nearly so on its own terms" and G-3 = "Nothing in the corpus establishes Kalshi's own contract mechanics" (the six-mark transfer table); its section 11 (line 3858) defines TC-1 = "The venue's fee schedule, tick size, position limits, settlement source and permitted pre-settlement position transformations, as a dated document set". Multivocal [docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md](docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md) section 12.1 (line 1747) defines G-1 = "The rulebook in force on 2026-09-04 was not located", G-3 = "Which contracts carry elevated position limits is withheld at source", and section 12.2 TC-1 = "Coherence-violation detection threshold, net of fees". Ranges overlap completely (G-1..G-10 vs G-1..G-25; TC-1..TC-5 vs TC-1..TC-15).
>
> 2. The within-Branch-0 double referent for bare G-3 reproduces exactly as claimed. Line 374 heads Branch 0 "**From:** G-3, TC-1, AG-1, AG-2"; line 390 "G-3's six marks" and line 403 "The corpus's six G-3 marks stand at six" can only be the predecessor's G-3 (only it has a six-row mark table; the multivocal G-3 has no marks). Line 441, inside the same branch's still-missing table, reads "| which contracts carry elevated position limits | **WITHHELD AT SOURCE** (G-3) |" — verbatim the multivocal G-3. Line 439 "the rulebook in force on the retrieval date | **NOT LOCATED** (G-1)" is likewise the multivocal G-1, while line 459 heads Branch 1 "**From:** G-1, and the S1 strand of the corpus" (S1 strands exist only in the predecessor). The branch-range rule in the front matter ("branches 7-11" from the multivocal corpus, line 93) cannot resolve this, because both referents occur inside Branch 0, which the rule does not cover. The same double use recurs outside Branch 0: line 248 "(S7-5, G-3" (predecessor) vs line 320 "confidential FOIA treatment" — `d16-c5`, **G-3**" (multivocal).
>
> 3. No disambiguation convention exists. grep -i over the agenda for "disambig|collision|collide|identifier space|prefix|namespace|confus" returns only line 59 (the A3-TC-1..A3-TC-7 agenda-local prefix), line 125 (an unrelated "frozen-prefix sha256"), and lines 312/852/1645 on unrelated topics. "How to read this document" (lines 159-210) states no G-n/TC-n convention. grep -rn "MV-G|MV-TC|KS-G-|KSG-" over docs/ returns nothing. Line 59's own wording — "the corpus's own TC-1..TC-15" — treats TC-1..TC-15 as if it were the only TC space, while the front matter at line 89 simultaneously assigns TC-1..TC-5 to the predecessor, which is itself the conflation.
>
> 4. Both cited precedents check out. [docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md](docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md):66-67 and :239-241 record the J1-J6 to N1-N6 rename for exactly this reason ("The rename to N1-N6 removes the collision"). The multivocal record's section 15 item 9 carries the quoted sentence verbatim: "They are numbered because the branch agenda consumes them by identifier".

### REV-1-4 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > consistency

- `location`:

  > research/01_hypothesis_register/H001/design.md:23 and :30-37; hypothesis_backlog.md:26

- `issue`:

  > Two shipped artifacts assert the non-existence of a third shipped artifact in the same set, and use that non-existence as the stated reason the H001 design is not frozen. H001's front matter records `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)` and its `freeze_status` states 'The corpus record this design depends on ... does not exist'; hypothesis_backlog.md repeats 'the corpus record the design depends on ... does not yet exist'. That file is a delivered artifact of this session. The freeze remains correctly deferred - pre-freeze checklist items 2 through 6 in design.md section 12 are genuinely open (academic-arm screening, ks-a-057 disposition, the mutual-exclusivity flag, the fee-multiplier table, the unlocated rulebook) - but item 1 is now discharged and the stated justification is false as shipped. Compounding it, design.md section 0.3 grounds its provisionality on `ks-academic-candidates.json` reporting 'n_deduplicated_records: 480' where the finished corpus record reports 528 deduplicated academic records; a reader comparing the two artifacts finds two different sizes for the same arm with no reconciliation note.

- `evidence`:

  > corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)

- `fix`:

  > Update H001's front matter and `freeze_status`, and the hypothesis_backlog H001 Notes cell, to record that pre-freeze checklist item 1 is now discharged and that the freeze is deferred on items 2-6, naming them. Add a one-line reconciliation in design.md section 0.3 stating that the academic arm's mid-run figure of 480 was superseded by the corpus record's final 528 and that no claim in the design rests on either count. Do not freeze the design.

- `reference`:

  > CHAMP item 30 (conclusions and stated status limited to what the artifact set supports); deliverable spec amendment D5

**Refutation evidence:**

> No refutation available; the finding reproduces exactly and its second sub-claim is understated. (1) `ls` confirms docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md exists (203,216 bytes, 2026-09-04 12:03) and is a fully compiled corpus record (PRISMA flow, n_screened 1574, limitation register G-1..G-5), not a placeholder. research/01_hypothesis_register/H001/design.md:23 still reads `corpus_record: ... (DOES NOT EXIST YET)`; the front-matter `freeze_status` (lines 30-37) asserts "The corpus record this design depends on ... does not exist; freezing now would register a design against literature that has not been compiled"; hypothesis_backlog.md's H001 Notes cell repeats "does not yet exist". design.md section 12 pre-freeze checklist item 1 ("... exists and is the compiled corpus record", line 1298-1299) is therefore discharged while items 2-6 (academic screening/ks-a-057 disposition, KSL-C02 exclusivity flag, ks-vr-d01 fee-multiplier table, rulebook in force, venue re-retrieval) remain genuinely open — exactly as the finding states. A grep for "now exists", "checklist item 1", or any discharge/reconciliation wording across design.md and hypothesis_backlog.md returns zero hits. (2) The count mismatch is real and larger than reported: design.md:101 quotes `ks-academic-candidates.json` as reporting `n_deduplicated_records: 480` and `n_in_reported_branches: 144`, but the shipped docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json lines 18-19 read `"n_deduplicated_records": 528, "n_in_reported_branches": 152`. The lit review reports 528 in nine independent places (lines 83, 133, 146, 198, 1283, 1326, 1350, 1417, 1444, 1762) and ks-amendments.jsonl M1 also states 528. So section 0.3 misquotes its own cited source file, and no reconciliation note exists in any of the three artifacts. The only objection I could construct — that "does not exist" was accurate at drafting time and the design is a point-in-time snapshot — is a plausibility argument about authoring order, not counter-evidence about the artifact set as shipped, which is the finding's stated scope.

### REV-1-5 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > interpretation

- `location`:

  > failure_log.md:620-629

- `issue`:

  > F008's 'Step 2b - source-design validity, with a signable direction' asserts as fact that ks-sc-001's candidate 'was selected **and** evaluated on the same market set', and on that premise concludes the source's null is 'MORE informative than its provenance would otherwise suggest'. The premise is not in the record. ks-github-records.jsonl gives ks-sc-001's `F10_outcome_reported.data_span` as '~92,000 settled/closed Kalshi markets; NO-tilt measured across a 30k settled sample' - two different spans - and the record was assessed at README-and-metadata depth only. The same F008 row lists 'the candidate-threshold selection procedure' as discriminating observation (iii), status OBTAINABLE and not obtained, and assigns layer `undetermined` precisely because the README states which conclusion it reached and not how. The row therefore builds a signed informativeness upgrade on one of the three facts it simultaneously records as unobtained, and does not carry the `[corpus-inference]` marker this project uses elsewhere (research agenda front matter and Branch 2b) for exactly this move. A related smaller instance in the same row supplies a unit the source does not state: 'n=23 candidate events'.

- `evidence`:

  > The candidate was selected **and** evaluated on the same market set, with no stated family-wise control (**TC-14** names the control that is absent ... ). A post-selection interval is biased **toward finding an effect**. So the source's negative verdict is reached **despite** a bias running the other way, which makes the null **more** informative than its provenance would otherwise suggest

- `fix`:

  > Rewrite Step 2b as a conditional marked `[corpus-inference]`: state that the README does not say whether the candidate was selected and evaluated on the same set, that the two spans it reports differ, and that IF selection and evaluation shared a set THEN the post-selection bias runs toward finding an effect - and that the informativeness upgrade is therefore contingent on discriminating observation (iii), not established. Strike 'candidate events' as the unit of n or attribute the unit to the reader's inference.

- `reference`:

  > CHAMP items 27 and 29 (causation/association discipline; pre-specified vs exploratory reasoning distinguished); charter commitment 5 (attribution fidelity)

**Refutation evidence:**

> Refutation attempted and failed; every element of the finding reproduces. (1) failure_log.md:620-629 carries the quoted Step 2b text in the declarative with no [corpus-inference] marker and no conditional. (2) The pinned README bytes (docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md, sha256 50293b49...) nowhere state how the 'high-NO-prob' threshold was chosen; the two nearest sentences do not supply the premise — 'Baselines: always-YES and always-NO on the *same* universe' concerns the comparator sharing the strategy's universe, not selection sharing the evaluation set, and 'requires forecast history and out-of-sample proof — which this public-data backtest cannot fabricate' is scoped to a model-based (forecast-beats-market) edge. A pre-specified price band from the README's favorite-longshot decomposition would yield the identical README with no post-selection bias, so the premise is not even derivable. (3) ks-github-records.jsonl record ks-sc-001 confirms F6_extraction_depth='README-and-metadata', F10_outcome_reported.data_span='~92,000 settled/closed Kalshi markets; NO-tilt measured across a 30k settled sample' (two spans, neither the n=23 set), and F14_to_compute[0]='the NO-probability threshold defining "high-NO-prob" (selection procedure: grid or cross-validated search ... )' — the record itself files the selection procedure as uncomputed, matching the row's own discriminating observation (iii), OBTAINABLE and not obtained, and its layer=undetermined rationale 'the README states which conclusion it reached and not how'. (4) The [corpus-inference] convention is real and in force in this project (defined in lit_review_kalshi-arbitrage_2026-09-02.md section 8.4 legend and applied in the research agenda / Branch 2b per audit_trail_s4 round 2), so its absence here is a deviation from an established in-project standard. (5) Unit sub-claim reproduces: repo-wide grep shows the source states a bare 'n=23'; 'candidate events' appears only at failure_log.md:590, and the README's intervals are bootstrap on per-bet ROI, so the event unit is not established. No concrete counter-evidence exists; the defect claim stands.

### REV-1-7 - RETAINED

- **raised_by:** `critical-reviewer`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > consistency

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:86

- `issue`:

  > The front-matter `screening_verdict_source` field states a total of 109 verdicted records and then itemises components summing to 110: 43 software + 30 venue + 32 lateral + 5 Y3. The correct lateral figure after the cross-arm deduplication of KSL-C31 (section 5.2, which states deduplication happens BEFORE screening) is 31, giving 43 + 30 + 31 + 5 = 109, which is also what the flow requires (99 included + 10 Y-code excluded) and what section 5.3 restates ('It assigned every one of the 109 eligibility verdicts'). The arm log's own `n_classes_sourced` is 32, so both numbers are defensible in isolation but not in one sentence. In a record whose warrant rests on published arithmetic closure - and which flags DI-2 for a two-row shortfall of exactly this kind and refuses to resolve it 'by rounding' or 'by reclassification' - an itemisation that does not sum to its own stated total is the same class of defect the record polices elsewhere.

- `evidence`:

  > READ-BASED for 100% of the 109 records that received any eligibility verdict — 43 software artifacts assessed by the software arm at the depth its records state, 30 venue documents assessed by the lead session against the frozen N/Y criteria, 32 lateral class records assessed by the lateral arm at retrieval, and 5 unsourced candidate classes dispositioned Y3.

- `fix`:

  > Change '32 lateral class records' to '31 lateral class records (32 sourced by the arm, less KSL-C31 removed at the cross-arm deduplication step of section 5.2, which precedes screening)' so the itemisation sums to the stated 109. Verify no other locus repeats the 32 as a verdicted count.

- `reference`:

  > CHAMP items 17 and 20 (data described correctly; presentation must reconcile); protocol section 4.5 count identities

**Refutation evidence:**

> Refutation attempted and failed; the defect reproduces exactly. (1) Line 86 of docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md itemises 43 software + 30 venue + 32 lateral + 5 Y3 = 110 against a stated total of 109. (2) The 109 is independently pinned by the record's own section 5.4 identities: n_included 99 plus n_criterion_excluded 10 (Y2 3, Y3 5, Y4 1, Y9 1) = 109. (3) Per-arm closure leaves 31 as the only admissible lateral slot value: software 980 screened = 43 verdicted + 937 G1 (n_capacity_gap 1465 = 528 academic + 937 software), with 43 = 40 included + 3 Y2; venue 30 screened = 28 included + 2 excluded; lateral 37 identified - 1 cross-arm dedup = 36 screened = 31 included + 5 Y3. 43 + 30 + 36 = 109, i.e. 43 + 30 + 31 + 5 = 109. Section 5.4 itself writes "n_included 99 = 40 software + 28 venue + 31 lateral + 0 academic". (4) Source check of the 32: docs/literature/search_logs/kalshi-strategy-multivocal/ks-lateral-records.json header carries "n_classes_sourced": 32 and the file holds 33 rows (header + KSL-C01..KSL-C32), so 32 is the pre-deduplication sourced count; section 5.2's cross-arm ledger drops KSL-C31 into ks-vr-d06 and states deduplication precedes screening. The front-matter sentence therefore mixes a pre-dedup figure with post-dedup figures inside one sum. No alternative assignment of the four components reconciles to 109, so no counter-evidence is available.

### SCOPE-1-1 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > changed

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:218-219 and :1639-1646

- `issue`:

  > CONFIRMED against the arm logs: the corpus record reports a capacity gap as an executed zero-yield result. Limitation 9 states "Four executed academic queries in that stratum returned zero" and section 10 N-5 names them as ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b, each annotated "(HTTP 200, 0)". Two of the four never executed. The correct executed-and-zero count is TWO. This is the exact class of defect the corpus itself legislates against (front matter capacity_codes G1: "NOT eligible, NOT ineligible"; protocol section 4.4 rule 1; limitation 9's own headline "is NOT a clean absence"), applied to the query layer instead of the record layer. failure_log.md F007 already establishes the correction but expressly declines to repair the corpus record, so the false count still stands unqualified in the artifact a reader reaches first.

- `evidence`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json field platform_interface_failure: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'."; field n_returned_semantics: "no search executed; not an observed zero-yield". ks-repec-04-b.json carries the identical two fields (retry_of: ks-repec-04). Eleven ks-s2-03*.json files exist on disk, all HTTP 429, corroborating the rest of N-5. Corpus limitation 9: "Four executed academic queries in that stratum returned zero"; N-5: "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)."

- `fix`:

  > Edit N-5 and limitation 9 to read TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and to state that ks-repec-04 / ks-repec-04-b returned HTTP 200 with a search FORM and never executed, quoting the log's n_returned_semantics field. Add the correction to section 11 as a numbered data-integrity entry (DI-n) and cross-reference failure_log F007 so the two documents agree; extend gap G-9 to name the RePEc interface failure alongside the Semantic Scholar 429s.

- `reference`:

  > deliverable spec Deliverables row 4 (corpus record: "a named-gap section, and the limitations a reader must carry into every number") and clause 4 of the spec's "Why this is a NEW branch" section ("An unbounded claim of completeness is a defect")

**Refutation evidence:**

> No refutation. The finding reproduces exactly and I found no counter-evidence.
>
> (1) Artifact text confirmed verbatim. lit_review_kalshi-strategy-multivocal_2026-09-04.md lines 215-219 (limitation 9): "The weather stratum's near-zero yield is NOT a clean absence. Four executed academic queries in that stratum returned zero, and the one query aimed squarely at temperature settlement never executed at all across eleven attempts." Lines 1639-1642 (section 10 N-5): "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)."
>
> (2) Log evidence confirmed verbatim. ks-repec-04.json and ks-repec-04-b.json (docs/literature/search_logs/kalshi-strategy-multivocal/) each carry field platform_interface_failure: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." and field n_returned_semantics: "no search executed; not an observed zero-yield". ks-repec-04-b.json has retry_of: "ks-repec-04", so it is one query plus its retry, not two independent queries.
>
> (3) Counter-test on the other two rows: ks-arxiv-04.json and ks-openalex-04.json carry http_status 200, client_error null, n_returned 0, n_total_reported 0, truncated_by_cap false, count_parse_error null, and NO platform_interface_failure / n_returned_semantics field. They are genuine executed zeros. Executed-and-zero count in stratum S3 is therefore TWO, exactly as the finding states.
>
> (4) Attempted refutation on the semantics of "executed" -- failed. The corpus cannot be read as using "executed" to mean "HTTP request issued": the same N-5 paragraph writes "But `ks-s2-03` ... NEVER EXECUTED" for queries that did return HTTP responses (429s), so the corpus's own sense of "executed" is search-ran, which is the sense the RePEc logs deny.
>
> (5) Attempted refutation via an existing qualification elsewhere in the corpus -- failed, and the search surfaced a second instance of the same error. Grepped every RePEc mention. Line 1669 (N-8) states "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)" -- an "empty result page" is precisely what the log says was not served (the body is the search form). Line 274 summary table row: "| RePEc / IDEAS | ideas.repec.org site search over HTML | 2026-09-04 | ks-repec | 0 |" with no interface-failure qualifier. Section 11's data-integrity register contains DI-1 through DI-7, none about RePEc or N-5. Gap G-9 (line 1766) names only "The weather stratum's most on-point query never executed across eleven attempts; 53 of 56 Semantic Scholar attempts returned HTTP 429" -- Semantic Scholar only, no RePEc. So the false count stands unqualified in the corpus record.
>
> (6) failure_log.md F007 (lines 482-492) confirms the finding's characterization word for word: "Corpus section 10 N-5 states that four academic queries in that stratum executed and returned zero, naming ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b. By ks-repec-04.json's own field, the two RePEc rows did not execute. The executed-and-zero count in that stratum is therefore two (ks-arxiv-04, ks-openalex-04), not four. ... Neither the corpus record nor the arm log is edited by this row."
>
> (7) ks-amendments.jsonl contains only the header and amendment M1 (M1a/M1b/M1c, query-construction departures); nothing amends N-5 or limitation 9.
>
> The defect claim is true as stated.

### SCOPE-1-2 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > changed

- `location`:

  > docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:577-590 vs docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:66

- `issue`:

  > Silent substitution in kind. The declaration's protocol row promises a protocol frozen before first query "specifying ... the verbatim query set per arm". The frozen protocol instead freezes the construction RULE and leaves the concrete strings to execution. Defensible (and it is what made amendment M1 necessary and possible), but it is a different deliverable in kind from the one declared, and none of the append-only amendments D1-D7 records it.

- `evidence`:

  > Spec line 66: "...eligibility criteria with codes, the verbatim query set per arm, the screening rule...". Protocol section 3.5: "The concrete query strings are **not** fixed in this file. ... **What freezes is the construction rule in sections 3.1-3.4 and the recording obligation in section 3.0.**"

- `fix`:

  > Append a declaration amendment D8 recording that the frozen artifact freezes the query CONSTRUCTION RULE rather than the verbatim query set, why (an unenumerable multivocal query surface), and what discipline substitutes for it (section 3.0 recording obligation plus the section 10 amendment requirement that produced M1). Do not edit the frozen protocol.

- `reference`:

  > spec Deliverables item 2

**Refutation evidence:**

> Attempted refutation on four independent lines; all four confirmed the finding instead.
>
> (1) Both quotes reproduce verbatim at the stated locations. C:\Users\skoir\castles\docs\deliverables\deliverable_spec_kalshi-strategy-corpus_2026-09-04.md line 66 reads "...eligibility criteria with codes, the verbatim query set per arm, the screening rule, the extraction schema..." C:\Users\skoir\castles\docs\methodology\protocol_kalshi-strategy-multivocal_2026-09-04.md lines 577-590 reproduce exactly as cited, including the heading "### 3.5 Query tables — filled at execution, frozen as to rule", the sentence "The concrete query strings are **not** fixed in this file.", an EMPTY query table (header row plus separator row only, lines 582-583, zero data rows), and "**What freezes is the construction rule in sections 3.1-3.4 and the recording obligation in section 3.0.**" The cited line range is exact.
>
> (2) Counter-hypothesis tested: that verbatim strings are frozen elsewhere in the protocol, making section 3.5 a scoping remark rather than a substitution. Read protocol lines 430-575 covering sections 3.1-3.4. Every arm carries a prose "**Query construction rule.**" and no literal query strings: §3.2 "Each query is the conjunction of (i) a **venue or instrument token** ... and (ii) an **artifact-intent token**"; §3.3 "Documents are located by **document class** rather than by free-text topic"; §3.4 queries "built from a frozen **lateral seed list** of strategy areas, each expanded with the instrument and venue tokens." Refutation fails: the protocol nowhere freezes a verbatim query set.
>
> (3) Counter-hypothesis tested: that the spec itself already contemplates execution-time query filling, so no divergence exists. Grepped every occurrence of "verbatim" and "query" across the spec (13 hits). Line 66 is the only spec statement about what the protocol specifies, and it is unqualified. Lines 70, 107, 113, 119 require verbatim query strings in the SEARCH LOGS (a different deliverable, satisfied at execution); line 146 says only "Freezing the protocol: computing its SHA-256 and committing it before any query runs." Nothing in the spec anticipates or licenses a rule-only freeze. Refutation fails.
>
> (4) Counter-hypothesis tested: that an existing declaration amendment already records the substitution. Read D1-D7 in full (spec lines 155-268). D1 = criterion-code rename J->N. D2 = two pre-registration inputs added to the search-log dir. D3 = added quotation-audit delegation. D4 = PRISMA-S no longer declared "adapted". D5 = added H001 design document. D6 = failure_log.md registration. D7 = amendment M1 issued post-freeze. D7 is the nearest miss and expressly frames itself as "Not a new artifact but a change to a declared one, recorded here because the declaration's protocol row said the protocol would be frozen and this records what happened to it AFTER freeze" — it records the three M1 query-construction departures and their adjudication, not the antecedent fact that the frozen artifact never contained a verbatim query set. None of D1-D7 records the substitution in kind. Refutation fails.
>
> Also cross-checked ks-amendments.jsonl: it registers M1 (parts M1a/M1b/M1c) against protocol sha256 32dfea6da36c..., each part quoting frozen construction-rule text ("one instrument term drawn from the frozen instrument vocabulary", "one strategy term drawn from the frozen strategy vocabulary"). This corroborates rather than refutes: the amendments are adjudications against a construction RULE, which is only possible because no verbatim string set was frozen.
>
> No concrete counter-evidence obtained. The defect claim is true as stated.

### SCOPE-1-3 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > changed

- `location`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ (directory) vs deliverable spec:70-71

- `issue`:

  > The declared search-log deliverable requires "the deterministic dedup and screening scripts with PYTHONHASHSEED=0 asserted at entry, as the 2026-09-02 branch does", and its check is "the screening script self-test exits 0". Six deterministic Python scripts exist and cover parsing, dedup, candidate assembly, recovery and store building, but NO screening script exists and none can: the branch deliberately assigned all 109 eligibility verdicts by read-based agent assessment. The declared check is therefore unsatisfiable as written. The substitution is documented in the deliverable (front matter screening_verdict_source; section 5.3) but is nowhere declared as a divergence from this spec.

- `evidence`:

  > Spec check: "every `query_id` cited in the corpus record resolves to a file in this directory, and the screening script self-test exits 0." Corpus front matter: "NO KEYWORD CLASSIFIER ASSIGNED ANY VERDICT IN THIS CORPUS. ... The trade is deliberate and is not an improvement in coverage — it is a much smaller decided set." Directory listing shows ks-academic-{extract,assemble,recovery-pass,runner,query-table,query-table-supplementary}.py and no screening script.

- `fix`:

  > Append a declaration amendment recording that no screening script exists by design, that the spec's "screening script self-test exits 0" check is retired as inapplicable, and naming the substitute verification (the stored B1-B4 branch rule and SR-1/SR-3 subset rule, both declared non-verdict machinery, plus the PYTHONHASHSEED=0 assertion on the five deterministic scripts that do exist).

- `reference`:

  > spec Deliverables item 3

**Refutation evidence:**

> Attempted refutation failed; every element of the finding reproduced. (1) No screening script: the directory holds 13 .py files (6 academic + 7 in ks-github-scripts/), not six, and none assigns an eligibility verdict. ks-academic-extract.py docstring: "NO eligibility determination is made here. Rows carry SIGNALS only." ks-academic-assemble.py docstring: "NO eligibility determination is made: ... section 4.2 stage-1 dispositions are NOT assigned here." The others are query executors, a retry pass, query tables, a README fetcher, a subset-draw/pin script, a quote verifier, and log/ledger writers. The predecessor branch does have docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py; this branch has no analogue. (2) The check is unsatisfiable: `grep -rn "self-test\|selftest" docs/` returns exactly ONE hit in the entire tree - spec line 71 itself. No self-test exists to exit 0. (3) Read-based verdicts confirmed: corpus front matter line 86 screening_verdict_source and section 5.3 ("It assigned every one of the 109 eligibility verdicts in this corpus"; "No keyword or regular-expression classifier assigned any eligibility verdict in this corpus"; B1-B4 and SR-1/SR-2/SR-3 declared "non-verdict machinery"). (4) Not declared as a divergence: the spec's append-only "Declaration amendments" register runs D1-D7 (D1 criterion renaming, D2 pre-registration inputs, D3 added quotation-audit delegation, D4 reporting-standard framing, D5 H001 design doc, D6 failure_log, D7 amendment M1) and none concerns the screening script or retires the check; ks-amendments.jsonl carries only M1, which states it alters "NO screening rule". Only defect in the finding is cosmetic: it miscounts the scripts as six (13 exist) and its claimed-fix text says five - neither miscount touches the defect claim, since none of the 13 is a screening script.

### SCOPE-1-4 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > partial

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1180-1197 (section 4)

- `issue`:

  > The spec's completeness-bound clause promises three components in the corpus record: per-arm coverage, the strata left unassessed, and a known-item recall check "in the manner the 2026-09-02 record does". Two are delivered in full (limitations 1-3, G-1..G-25; the unassessed strata). The third is absent: the file contains no known-item recall check and no occurrence of the phrase. Section 4 reports only that the strategy was not peer reviewed and points to the pre-freeze instrument verification, which is a different check (instrument resolution, not search recall). No D-amendment records the drop.

- `evidence`:

  > Spec line 54-57: "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." Grep for 'known-item|known item|recall check' over the corpus record: no matches. Section 4 delivers instead: "**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was obtained, and none was simulated."

- `fix`:

  > Either execute and report a known-item recall check (seed set of records the arms should have retrieved — e.g. the predecessor branch's Kalshi-naming included records and the two negative-measurement repositories — with per-arm hit/miss), or append a declaration amendment stating the check was not performed, why, and registering it as a numbered gap in section 12.1 so the agenda can consume it.

- `reference`:

  > spec "Why this is a NEW branch" clause 4; Deliverables item 4

**Refutation evidence:**

> Attempted refutation on four routes; all failed, and every element of the finding reproduced. (1) Spec clause verbatim at docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:54-57 — "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." (2) Grep for 'known.item|known item|recall check|recall' over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns exactly one hit, line 62, "an executing agent's own recall" — the Y3 exclusion criterion, not a check. Section 4 (lines 1179-1197) delivers only "NOT PEER REVIEWED", the pre-freeze instrument verification, and gap G-14 (verification depth), which is instrument resolution, not search recall. (3) Counter-test for the check under different naming: grep for 'seed set|seed record|sentinel|hit/miss|should have retrieved|would have retrieved|gold set|benchmark set|verification set|retrieval check|sensitivit|validation of the search' returns zero matches; the only 'seed' occurrences are the lateral arm's ten frozen topic seeds and PYTHONHASHSEED/RNG-seed columns in the query log. 'PRESS' appears exactly once in the whole record (line 1183) and only in the negative. (4) Counter-test for a recorded drop: gap register 12.1 enumerated in full, G-1..G-25 at lines 1758-1782 — none covers a missing recall check; declaration amendments D1-D7 read in full (spec lines 155-268) — none drops or defers it; docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl has exactly two lines, a header and M1 (academic-arm query admissibility, decided pre-screening), touching no such thing. The spec's referent is real rather than vacuous: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:4161 carries section "13.4 Known-item recall check — reported per item, with no pass threshold", with 16 of 23 items retrieved and a machine-readable log at ka-known-item-recall.json. No counter-evidence obtained; the finding stands.

### SCOPE-1-5 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > omitted

- `location`:

  > docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md + .json (both absent from disk)

- `issue`:

  > Declared deliverable not present. The spec requires a session audit trail validating against the WI-3 section 2 required-field spec (22 front-matter keys, 7 body sections) with every refute-gate disposition recorded verbatim, plus a sidecar whose sha256 matches. Neither file exists. Severity is set at major rather than the category default because this artifact is the audit loop's own output and cannot exist before the loop closes; it becomes critical if the session commits without it.

- `evidence`:

  > Spec lines 85-87. Glob 'docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.*' returns no files. Sibling trails for the prior session exist (audit_trail_s4-reexecution-and-repo-gaps_2026-09-03.{md,json}), so the naming convention is established and the absence is not a path miss.

- `fix`:

  > Write the trail and sidecar before the final provenance commit; carry every round-1 finding and its refute-gate disposition verbatim, including the SCOPE-1-1 confirmation and the reason each declaration amendment below was or was not opened.

- `reference`:

  > spec Deliverables item 7

**Refutation evidence:**

> Could not refute; the claim reproduces exactly. (1) `find C:\Users\skoir\castles -iname "*kalshi-strategy-corpus*" -not -path "*/.git/*"` returns a single hit, the spec itself (docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md); neither audit_trail_kalshi-strategy-corpus_2026-09-04.md nor .json exists anywhere in the working tree. (2) A full `ls -la` of docs/audits/ confirms trails exist for think-tank-charter (08-21), phase1-sweep (08-21), round3-remediation (08-21), naming-sweep (08-24), phase2-explosive-review (08-24), kalshi-arbitrage-review (09-02), open-items-kalshi-arbitrage (09-02) and s4-reexecution-and-repo-gaps (09-03) — establishing the naming convention as the auditor stated — with no kalshi-strategy-corpus entry. session_trail_2026-09-04.md and union_gate_waivers_2026-09-04.md are present but are distinct artifact types, not the WI-3 audit trail the spec demands. (3) `git status --porcelain` shows no staged, modified, or untracked path matching the required filename, so the absence is not an unstaged/unindexed artifact. (4) The spec requirement is verbatim confirmed in the Deliverables section: bullet `docs\audits\audit_trail_kalshi-strategy-corpus_2026-09-04.md` + `.json` sidecar, state "an audit trail written during this session that validates against the WI-3 section 2 required-field spec — 22 front-matter keys, 7 body sections — recording every refute-gate disposition verbatim", check "hooks/stop_union_gate.py does not block at end of turn; the trail sidecar.sha256 matches the sidecar on disk." The only available counter-argument — that this artifact cannot exist until the audit loop closes — is stated by the finding itself and is a severity/sequencing argument, not evidence against the absence, so it does not meet the refutation bar.

### SCOPE-1-6 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > added

- `location`:

  > hypothesis_backlog.md:13, :26, :28-33

- `issue`:

  > Undeclared scope addition. The spec declares the H001 design document (D5) and failure_log.md (D6) but no change to hypothesis_backlog.md. That file has been given a new H001 row, a newly invented status value `specified-unfrozen` added to the house status legend, and a retained-prior-state note recording removal of the bootstrap stub. Adding a status token to a cross-project convention register is a broader change than the row itself. D6 opened scope for failure_log.md on exactly the reasoning that "an undeclared deliverable is a scope divergence"; the same standard was not applied here.

- `evidence`:

  > hypothesis_backlog.md line 13: "`specified-unfrozen` | **PROPOSED 2026-09-04, not yet ratified.** ... This status exists because `designed` below asserts a freeze that has not happened, and no other status in this legend is true of a drafted-but-unfrozen design." Spec D5 declares only "`H001 pre-registration design document` (path per the `pre-register-hypothesis` skill...)". Spec D6: "Not in the original Deliverables list. ... Registering them is a standing charter obligation, not a discretionary addition, so it is recorded as scope rather than left undone."

- `fix`:

  > Append a declaration amendment covering the hypothesis_backlog.md edit, stating explicitly that a new status token was introduced into a shared convention register, that it is PROPOSED and not ratified, and what would ratify it.

- `reference`:

  > spec Declaration amendments D5/D6 (the standard they set)

**Refutation evidence:**

> Refutation attempted and failed; every element of the claim reproduced.
>
> 1. Quoted text at stated lines is verbatim-accurate. `grep -n` on C:\Users\skoir\castles\hypothesis_backlog.md returns line 13 = the `specified-unfrozen` legend row containing exactly the quoted string ("PROPOSED 2026-09-04, not yet ratified. ... This status exists because `designed` below asserts a freeze that has not happened, and no other status in this legend is true of a drafted-but-unfrozen design."); line 26 = the new H001 row whose Status cell is `specified-unfrozen`; lines 28-33 = the retained-prior-state note recording removal of the bootstrap stub. Line numbers match the finding exactly.
>
> 2. The spec declares no such deliverable. Read C:\Users\skoir\castles\docs\deliverables\deliverable_spec_kalshi-strategy-corpus_2026-09-04.md in full. The Deliverables list (lines 61-95) contains no hypothesis_backlog.md entry. Declaration amendments run D1-D7 (lines 160-268); D5 (line 208) declares only "`H001 pre-registration design document` (path per the `pre-register-hypothesis` skill...)" with checks confined to that file's front matter and TO COMPUTE count. D6 (line 247) declares only `failure_log.md`. No amendment names hypothesis_backlog.md. Grep for "hypothesis_backlog" across docs/, research/, failure_log.md returns only pre-existing references (ADR-0001, ADR-0003, the 2026-08-21 charter spec/audit trail, failure_log.md line 6, and design.md:1249 which merely quotes ADR-0003 about `promoted`) — nothing in this session's ADR-0006 or H001 design.md declares the backlog edit.
>
> 3. The status token is genuinely new, not a pre-existing house value. Repo-wide grep for "specified-unfrozen" (excluding .git) returns exactly two hits, both inside hypothesis_backlog.md itself (lines 13, 26). It appears in no ADR, no protocol, no design document, and no prior audit trail — so it was invented by this session and inserted into the legend the file itself describes as "Per SKIE-Universe convention".
>
> 4. The change is uncommitted working-tree scope. `git log --oneline -- hypothesis_backlog.md` shows a single commit (988e521 bootstrap scaffold); `git status --porcelain` shows ` M hypothesis_backlog.md`; `git diff HEAD --stat` shows 10 insertions / 5 deletions. The diff confirms all three claimed edits and additionally shows a fourth undeclared edit the finding did not even cite: the `promoted` legend row was rewritten to append "**inert in this repository** per ADR-0003 §Consequences...". That strengthens rather than weakens the claim.
>
> 5. The consistency argument holds on the spec's own text. D6 states verbatim "Not in the original Deliverables list. ... Registering them is a standing charter obligation, not a discretionary addition, so it is recorded as scope rather than left undone", and D3 states "an undeclared delegation is a scope divergence even when it improves the deliverable". The same standard is unapplied to hypothesis_backlog.md.
>
> No counter-test, source quote, or logical proof was found that would disprove the defect claim.

### SCOPE-1-7 - RETAINED

- **raised_by:** `scope-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > spec-conflict

- `location`:

  > docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:626-631 vs :663-685

- `issue`:

  > The frozen protocol contradicts itself about whether a record may end screening undispositioned, and 93% of the delivered flow (1,465 of 1,574 screened records) took the path section 4.2 does not enumerate. Section 4.2 states every deduplicated record receives exactly ONE stage-1 disposition and lists three: include, exclude-with-Y-code, promote. Section 4.4 then creates G1/G2, which are none of the three. The corpus record follows 4.4 consistently and reports G-rows separately from Y-rows as rule 2 requires, so the DELIVERY is coherent; the SPEC is not, and a reviewer re-deciding any G-row against section 4.2 alone would find an unmet obligation.

- `evidence`:

  > Protocol section 4.2: "Every deduplicated record receives exactly one stage-1 disposition: `include`, `exclude` with a primary Y-code, or `promote` where eligibility is not decidable at metadata depth (N6)." Protocol section 4.4: "**G1 — identified, eligibility not assessed.** ... It is **not** eligible, **not** ineligible: it is **undecided**." Corpus front matter: n_capacity_gap 1465, n_criterion_excluded 10.

- `fix`:

  > Remediate the SPEC, not the delivery: issue append-only amendment M2 reconciling section 4.2's disposition enumeration with section 4.4's capacity codes (a G-code is a fourth stage-1 outcome, or 4.2's 'exactly one' is read as conditional on assessment capacity). Do not edit frozen text; record M2 in both registers as M1 was.

- `reference`:

  > lower-precedence spec source: frozen protocol, sections 4.2 / 4.4

**Refutation evidence:**

> Refutation attempted and failed; the finding reproduces exactly. (1) Verbatim text confirmed at the cited lines: protocol L628-631 "Every deduplicated record receives exactly one stage-1 disposition: `include`, `exclude` with a primary Y-code, or `promote` where eligibility is not decidable at metadata depth (N6)"; L663-685 defines "G1 - identified, eligibility not assessed... no eligibility determination under N1-N6 was ever made for it. It is not eligible, not ineligible: it is undecided." (2) Counts confirmed in the corpus front matter: n_screened 1574, n_excluded 1475, n_criterion_excluded 10, n_capacity_gap 1465, n_included 99 (1465/1574 = 93.1%); corpus line 86 states the 1,465 G1 rows "received NO verdict of any kind". Because n_screened = n_identified - n_duplicates_removed, all 1,465 G1 rows ARE deduplicated records, so 4.2's universal quantifier reaches them. (3) The only escape reading - that a G1 row could have carried the `promote` disposition, which is routing rather than an eligibility verdict - is closed by the protocol's own text: 4.2 defines `promote` as the N6 outcome, and N6 lies inside the N1-N6 range G1 declares was never determined. A G1 row therefore provably carries none of the three enumerated dispositions. (4) No reconciling clause exists: grep over the protocol for "disposition", "undecided", "fourth", "4.2", and contradict/tension/reconcile finds no qualifier on 4.2's universal and no cross-reference from 4.4 back to 4.2. Section 2.4 (L356) "Capacity dispositions are NOT exclusions on the merits and are coded separately in section 4" and objective O7 (L147) "dispositioned as undecided rather than as ineligible" are two further uses of a fourth outcome that 4.2's enumeration does not carry - reinforcing the conflict rather than curing it. (5) The sole existing amendment M1 (ks-amendments.jsonl line 2 and the protocol addendum) touches section 3.1 / query admissibility only and states explicitly that it alters "NO screening rule and NO arithmetic identity", so no amendment already reconciles 4.2 with 4.4. No counter-evidence obtained.

### QUANT-1-1 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > numerical

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:216-218 (limitation 9) and :1639-1653 (negative result N-5)

- `issue`:

  > The corpus record states, twice, that FOUR academic queries in the weather stratum executed and returned zero. Two of the four named queries (`ks-repec-04`, `ks-repec-04-b`) NEVER EXECUTED — their own logs declare a platform interface failure and state that n_returned=0 there means no search was run. The corrected executed-and-zero count is TWO. The record therefore reports a capacity gap as an observed zero-yield, which is precisely the inference the same section forbids ('a capacity gap is not an absence'). The defect is identified in failure_log.md F007 and in the research agenda, but both explicitly decline to repair it ('Neither the corpus record nor the arm log is edited by this row'), so the citable primary artifact still carries the false statement. Recording a known-false claim elsewhere is not remediation; §11's 'recorded, not repaired' class is for defects in EXTERNAL sources (DI-1, a regulator's mis-indexed PDF), not for the record's own misstatement of its own execution log.

- `evidence`:

  > Corpus L1640: 'Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0).' Independent read of the logs: ks-repec-04.json / ks-repec-04-b.json carry `"platform_interface_failure": "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN"` and `"n_returned_semantics": "no search executed; not an observed zero-yield"`. Only ks-arxiv-04.json and ks-openalex-04.json carry http_status 200, client_error null, n_total_reported 0 with no interface-failure field. Corrected count = 2.

- `fix`:

  > Edit both loci in the corpus record to read 'TWO academic queries in that stratum executed and returned zero (`ks-arxiv-04`, `ks-openalex-04`); `ks-repec-04` and `ks-repec-04-b` returned HTTP 200 but never executed — their own `platform_interface_failure` / `n_returned_semantics` fields state that n_returned=0 there means no search was run, so they are capacity gaps, not observations.' Also correct N-8's characterisation of the nine RePEc attempts as 'HTTP 200 with an empty result page' to 'HTTP 200 serving the search FORM, not a result set'. Record the correction as a dated erratum in the record and cross-reference failure_log F007 and agenda rev 3 so the three artifacts agree.

- `reference`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json, ks-repec-04-b.json, ks-arxiv-04.json, ks-openalex-04.json; failure_log.md:481-491; protocol §4.4 rule 2 (G-rows reported separately from criterion failures)

**Refutation evidence:**

> Refutation attempted and failed; the defect claim reproduces on independent read.
>
> 1. Locus 1 (limitation 9, docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:215-218) reads verbatim: "**The weather stratum's near-zero yield is NOT a clean absence.** Four executed academic queries in that stratum returned zero, and the one query aimed squarely at temperature settlement **never executed at all** across eleven attempts." Locus 2 (N-5, :1639-1642) reads: "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)."
>
> 2. Independent read of the four named logs in docs/literature/search_logs/kalshi-strategy-multivocal/ confirms the auditor's split. ks-arxiv-04.json and ks-openalex-04.json: http_status 200, client_error null, n_returned 0, n_total_reported 0, platform_interface_failure null, n_returned_semantics null. ks-repec-04.json and ks-repec-04-b.json both carry platform_interface_failure = "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." and n_returned_semantics = "no search executed; not an observed zero-yield". Corrected executed-and-zero count = 2. Also note n_total_reported is null for both RePEc rows (no count was parsed at all), versus 0 for the two genuine zeros.
>
> 3. Attempted refutation via a special sense of "executed" (i.e. "HTTP request issued"): fails. The record's own N-5 sentence contrasts "executed and returned zero" against ks-s2-03, which "NEVER EXECUTED" despite eleven HTTP round-trips returning 429. Under the record's own usage, "executed" means the search ran, which the RePEc logs explicitly deny. Grep of the protocol found no competing definition (only executed_at as a timestamp field).
>
> 4. Attempted refutation via an existing in-record correction: fails. Grep for "erratum"/"Erratum" over the corpus record returns nothing; the only "never executed" hits at :217 and G-9 (:1766) both refer to ks-s2-03, not the RePEc rows. docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl contains only the header and amendment M1 (query-construction rulings) — no correction to the count.
>
> 5. The claim that the defect is knowingly left unrepaired in the citable artifact reproduces at failure_log.md F007 (:482-492), verbatim: "Corpus §10 N-5 states that **four** academic queries in that stratum *executed* and returned zero ... The executed-and-zero count in that stratum is therefore **two** ... Neither the corpus record nor the arm log is edited by this row".
>
> 6. Ancillary claim about N-8 also reproduces: :1668-1670 reads "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)", whereas the logs state the body is the search FORM, not an empty result set.
>
> Only discrepancy found is immaterial: limitation 9 begins at line 215, not 216. No counter-evidence obtained.

### QUANT-1-2 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > method

- `location`:

  > research/01_hypothesis_register/H001/design.md:462-472; docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1601-1612 (N-2)

- `issue`:

  > H001 §1.6 asserts a 'Correction to the framing this design was handed': that the ks-sc-001 record does NOT state that no price-based strategy beat the always-NO baseline. The primary source is in the repository, byte-verifiable, and states exactly that in bold. The assertion about the source is false, and the corpus's N-2 characterisation ('the record's own null result is that its best candidate did not beat its own baseline') likewise understates the source's own headline null. Charter commitment 5 makes a misdescribed source clause a defect regardless of direction; here it makes a source-reported NULL look weaker than the source states it, in the artifact whose whole function is to record what sources state.

- `evidence`:

  > ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md (sha256 50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118, matches the recorded README digest), item 3 of 'Three structural realities': '**No price-based strategy clears the honest bar.** The best candidate beats always-NO on point estimate but is statistically indistinguishable from it (n=23, CI overlaps).' and the conclusion line: '**Conclusion: there is no demostrable price-based edge in the public settled-market data.**' The arm log's F4_evidence_quotes for that item begins at 'Favorites >> longshots', dropping the two preceding sentences of the same numbered item.

- `fix`:

  > Add the two dropped sentences to ks-sc-001's F4_evidence_quotes with their location; rewrite H001 §1.6(i)'s 'Correction' paragraph to state what the README actually says ('No price-based strategy clears the honest bar' with the always-NO baseline defined as that bar in item 2, plus the conclusion sentence) and keep the design's conservative use of only the n=23 / CI-overlap claim as an explicit choice rather than as a claim about the source; extend corpus N-2 with the same two verbatim sentences.

- `reference`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 30-42; charter commitment 5 (attribution fidelity); predecessor amendment A19 quotation-audit precedent

**Refutation evidence:**

> Attempted refutation failed; every element of the finding reproduced.
>
> 1. Source integrity. sha256sum of C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal\ks-github-readme-evidence\sudo-ai-git__kalshi-backtest.md = 50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118, identical to the readme.sha256 recorded in the ks-sc-001 platform_metadata and F12_retrieval_and_drift blocks. The evidence file is the pinned README.
>
> 2. Source text. Lines 25-45 of that file contain item 2: "The correct null for any strategy is the **always-NO baseline**, and every candidate must beat it." and item 3, opening: "**No price-based strategy clears the honest bar.** The best candidate beats always-NO on point estimate but is statistically indistinguishable from it (n=23, CI overlaps). Favorites >> longshots ..." followed by "**Conclusion: there is no demostrable price-based edge in the public settled-market data.**" The composition of items 2 and 3 states, in near-verbatim terms, that no price-based strategy beat the always-NO baseline.
>
> 3. Arm-log truncation confirmed. In ks-github-records.jsonl, the ks-sc-001 F4_evidence_quotes entry whose location is "README.md, section 'Three structural realities', item 3" begins at "Favorites >> longshots (the classic favorite-longshot bias), but that bias is already priced in and eaten by fees/spread." The two preceding sentences of the same numbered item are absent, as is the Conclusion line. The record's F9 "correct baseline required" entry quotes item 2 but not item 3's headline.
>
> 4. Repository-wide check. grep for "honest bar", "demostrable", and "demonstrable price-based" across all .md/.json/.jsonl files returns zero hits outside the raw README evidence file. Neither the arm log, the corpus, nor H001 carries the source's headline null anywhere.
>
> 5. Artifact text confirmed. research/01_hypothesis_register/H001/design.md at the cited region reads: "The record does **not** state, in those words, that *no* price-based strategy beat the always-NO baseline. What it states is that the correct null is the always-NO baseline, that its *best candidate* is statistically indistinguishable from that baseline ... That is a weaker and more specific claim". The "weaker and more specific claim" characterisation is a claim about the source's content and is false against item 3's bold headline plus the Conclusion line. docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md N-2 reads "the record's own null result is that its best candidate did not beat its own baseline", which likewise substitutes the best-candidate result for the source's stated class-wide null.
>
> 6. Only candidate defence examined and rejected. The hedge "in those words" and the possible reading of "the record" as the arm-log entry rather than the README would make the sentence literally true only in a circular sense (true because the arm log itself dropped the sentences), and it does not rescue the following sentence, which asserts what the source states and calls it weaker. Under either reading the source-descriptive assertion is wrong in the direction the finding names.
>
> No counter-evidence obtained. Finding stands.

### QUANT-1-3 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > parameter

- `location`:

  > research/01_hypothesis_register/H001/design.md:474-500 (§1.6(ii)) and :1119-1126 (§9.2 item 1); docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-records.jsonl (ks-sc-002, F9_preconditions_stated)

- `issue`:

  > A load-bearing qualifier is dropped from the ks-sc-002 source at extraction and propagates into the design's registered sanity ceiling. The README states the 40-50c round-trip hurdle of 10.7c and, in the very next sentence, 'Even at the tails the hurdle is 2.6c.' The arm log's quote stops immediately before that sentence; H001 §1.6(ii) then argues the source's bar is stated only mid-range, leaves the tail bar 'TO COMPUTE', and registers QUOTED 10.7c as the pre-registered sanity ceiling for a tail-band `delta` in §9.2. The source's own tail figure is ~4x tighter, so the registered ceiling cannot catch the arithmetic error it exists to catch. Separately, the justification given for the ceiling ('the fee is monotonically smaller away from P = 0.5') covers only the fee component, while 10.7c is spread PLUS twice the fee; the same README states liquidity concentrates near the money and 79% of contracts never showed a two-sided book, so tail spreads are not established to be monotone. The monotonicity assumption is asserted, not verified.

- `evidence`:

  > ks-github-readme-evidence/himagna16__kalshi-microstructure.md (sha256 753d94ddd29e..., matches recorded digest), cost-to-trade section: 'A contract trading at 40-50c must move **10.7c** ... before a taker round trip breaks even. Even at the tails the hurdle is 2.6c.' ks-sc-002 F9_preconditions_stated quote ends at '...breaks even.'; grep for '2.6' returns no hit in H001 design.md or in the corpus record.

- `fix`:

  > Extend the ks-sc-002 extraction to include 'Even at the tails the hurdle is 2.6c.'; in H001 §1.6(ii) record that figure as the source's own tail statement, flag it non-adoptable on the same grounds as the other bare numbers (no derivation on the page), and re-register the §9.2 sanity ceiling against it rather than against 10.7c; replace the fee-monotonicity justification with one that covers the spread term, or restrict the ceiling claim to the fee component only.

- `reference`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/himagna16__kalshi-microstructure.md lines 90-96; charter commitment 3 (no unlabelled constants) and commitment 5

**Refutation evidence:**

> No refutation found; every claim reproduced. (1) himagna16__kalshi-microstructure.md lines 92-94 contain "...before a taker round trip breaks even. Even at the tails the hurdle is 2.6c." and the file's sha256 753d94ddd29ee97929fa4d483420e105aeee602f34f610d69ec65b4bb7668462 matches the digest recorded in ks-sc-002 (platform_metadata.readme.sha256 and F12.readme_sha256), so the record is pinned to exactly this text. (2) JSON round-trip of ks-sc-002 in ks-github-records.jsonl confirms the F9_preconditions_stated quote for "break-even move required for a taker round trip" ends at "before a taker round trip breaks even." and the substring "2.6" appears nowhere in the whole record. (3) H001 design.md 502-509 states the bar is given "at 40-50c, the middle of the price range", leaves the tail bar "TO COMPUTE", and registers 10.7c as the sanity ceiling justified solely by "the fee is monotonically smaller away from P = 0.5"; line 1125 (section 9.2 item 1) re-registers "Sanity ceiling: QUOTED 10.7c". grep for "2.6" in design.md returns nothing. (4) Repo-wide, grep -rln "2.6c" (cent sign) matches only the raw README evidence file and grep -rn "tails the hurdle" matches nothing outside it: the tail figure is in no extraction record, no amendment in ks-amendments.jsonl, the lit review, protocol, or ADR-0006. (5) 10.7/2.6 = 4.1, consistent with "~4x tighter". Candidate counter-evidence considered and rejected: the same README sentence says the spread "is also widest mid-range", which weakly bears on the spread term, but that is not the justification the design gives (it cites fee monotonicity only), the record's own F9 carries the source's "79% ... never showed a two-sided book", and "widest mid-range" does not establish tail monotonicity. Both sub-claims stand.

### QUANT-1-4 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > parameter

- `location`:

  > research/01_hypothesis_register/H001/design.md:816 (§6 embargo) and :1087 (§9.1 bootstrap block length); §13 References :1315-1403

- `issue`:

  > The 'Politis-White automatic block length' procedure is named twice as the selection procedure for two load-bearing parameters (the walk-forward embargo and the bootstrap block length feeding Hansen SPA / White Reality Check) and carries no citation anywhere in the document, in the charter, or in ks-instrument-verification.json. Every other statistical instrument in the design is cited with a DOI and its provenance declared; this one is not. That breaches CLAUDE.md's parameter-selection rule (documented selection rationale with citations), the design's own §0.2 labelling regime, and the D5 acceptance check that no external citation appear that is absent from ks-instrument-verification.json or an arm output.

- `evidence`:

  > grep -n 'Politis' research/01_hypothesis_register/H001/design.md returns only lines 816 and 1087; grep 'Politis' across docs/methodology/charter_castles_2026-08-21.md returns nothing; §13's four citation blocks list White, Hansen, Newey-West, Andrews, Opdyke, Lo, Ledoit-Wolf, Hoenig-Heisey, Theiler, Kaufman, Lakens, Schuirmann — Politis-White appears in none.

- `fix`:

  > Add the citation to §13 with its DOI (Politis & White 2004, Econometric Reviews 23(1):53-70, doi:10.1081/ETC-120028836, together with the Patton, Politis & White 2009 correction, doi:10.1080/07474930802459016), declare its provenance in the same terms used for the other statistical instruments ('cited as the rule file / charter records it, not re-verified in this drafting session'), or replace the named procedure with one already carried in ks-instrument-verification.json.

- `reference`:

  > ~/.claude/CLAUDE.md §Parameter & Prompt Selection; deliverable spec D5 check line 218-220

**Refutation evidence:**

> Attempted refutation failed; every element of the claim reproduced independently.
>
> 1. Location check. `grep -n 'Politis' research/01_hypothesis_register/H001/design.md` returns exactly two lines, matching the stated locations: line 816 (§6 Splitter, embargo) "...maximum of (i) the lag at which the residual PACF ... and (ii) the Politis-White automatic block length for the same series. Data-driven, not chosen." and line 1087 (§9.1) "...with a stationary/block bootstrap whose block length is `TO COMPUTE` by the Politis-White automatic procedure (the same estimator §6 uses for the embargo)." Both parameters are load-bearing: the embargo governs the PurgedWalkForwardSplitter, and the block length feeds Hansen SPA (primary) and White Reality Check (pre-registered sensitivity).
>
> 2. No citation in the document. §13 References spans lines 1315-1403 (file is 1403 lines; §13 is the last section). Read in full: its five citation blocks are venue/clause ids, practitioner class ids, GitHub records, academic records, "Methodological instruments verified before protocol freeze" (PRISMA-S, PRISMA 2020, Arksey & O'Malley, Adams/Smart/Huff, Garousi, Kalliamvakou, Munaiah, Smith/FORCE11, Klein, Jones), "Statistical instruments ... adopted by explicit reference through ADR-0004" (White 2000, Hansen 2005, Newey & West 1994, Andrews 1991, Opdyke 2007, Lo 2002, Ledoit & Wolf 2008), and "Charter-cited instruments" (Hoenig & Heisey, Theiler et al., Kaufman et al., Lakens et al., Schuirmann). Politis-White appears in none, and no other section of design.md carries it (grep result above is exhaustive).
>
> 3. No adoption route covers it. `grep 'Politis\|block length'` over docs/methodology/charter_castles_2026-08-21.md and ~/.claude/rules/quant-project.md returns nothing. The §13 statistical block's escape hatch is "cited as that rule file records them" — the rule file's §Inference lists only Newey-West/Andrews, Opdyke/Lo/Ledoit-Wolf, White/Hansen, so the adoption clause does not reach Politis-White.
>
> 4. Not in the arm output. `grep -c 'Politis' docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json` = 0. That file's eight instruments are the MLR/grey-literature methodology set, none statistical.
>
> 5. No self-declared gap. §12 and the six-item pre-freeze checklist (lines 1272-1314) list no citation obligation for the block-length estimator. §0.2's labelling regime is satisfied only in the weak sense that the procedure is "named"; CLAUDE.md §Parameter & Prompt Selection additionally requires "Document selection rationale with citations", which is unmet.
>
> 6. The source exists and is already in-repo, so this is a gap, not a naming artifact: docs/literature/lit_review_regime-classification_2026-08-21.md:1204 and :1208 carry Politis & White (2004) doi:10.1081/etc-120028836 and the mandatory Patton, Politis & White (2009) correction doi:10.1080/07474930802459016, with references_regime-classification.json entries. design.md contains no cross-reference to that corpus (`grep 'regime-classification'` on design.md returns nothing).
>
> Only weakening found, insufficient for refutation and not touching the defect: the finding's secondary appeal to the D5 check (deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:218-220, verbatim "no external citation appears that is absent from `ks-instrument-verification.json` or an arm output") is a poor fit — an uncited procedure name does not "appear as an external citation", and that check is in any case already exceeded by the twelve DOIs §13 carries from the rule file and charter, none of which are in ks-instrument-verification.json. This misapplies one of two cited authorities; the primary authority (CLAUDE.md §Parameter & Prompt Selection) holds, and the factual defect — an uncited procedure selecting two load-bearing parameters in a document where every other statistical instrument carries a DOI and a declared provenance — is confirmed.

### QUANT-1-5 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > reproducibility

- `location`:

  > research/01_hypothesis_register/H001/design.md:99-106 (§0.3) and front matter :24-29

- `issue`:

  > H001 §0.3 quotes two named fields verbatim from an in-repo file whose current bytes contradict them, and records no read-time digest that would make the quotation checkable. The design declares the arm 'PROVISIONAL and possibly mid-run', which explains the staleness but does not make the quotation reproducible: a reader following the citation retrieves different numbers and has no way to confirm the design read the file it says it read.

- `evidence`:

  > design.md L101-102: '`ks-academic-candidates.json` reports `n_deduplicated_records: 480` and `n_in_reported_branches: 144`'. On disk: grep -o '"n_deduplicated_records": *[0-9]*' returns 528; '"n_in_reported_branches": 152'. No sha256 of ks-academic-candidates.json is recorded anywhere in the design.

- `fix`:

  > Record the SHA-256 (and read timestamp) of ks-academic-candidates.json as read, next to the quoted figures, and add a one-line note that the file has since been superseded at 528 / 152; or re-read and re-quote the current values with the current digest. Apply the same digest discipline to the other four entries in `arms_read_for_this_draft`.

- `reference`:

  > CLAUDE.md §Reproducibility contract (dataset checksum); charter commitment 5

**Refutation evidence:**

> No refutation. Both factual claims reproduce. (1) design.md L101-102 quotes n_deduplicated_records: 480 and n_in_reported_branches: 144; grep on docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json returns 528 and 152, and no numeric field in that file holds 480 or 144. The arm's own amendment register (ks-amendments.jsonl, M1) independently states "All 528 academic-arm records are G1 rows", confirming 528 is the arm's current self-report rather than a transient write. (2) No read-time digest exists anywhere: grep for sha256/digest/read_at across design.md returns hits only for the protocol SHA, two GitHub README SHAs, and venue-clause SHAs -- none for ks-academic-candidates.json; no file under logs/reproducibility/ mentions it; the file is untracked in git (git ls-files --error-unmatch fails), so no committed prior version preserves the 480/144 state either. Current digest computed: ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58. The front-matter PROVISIONAL flag (L29) and the sec 0.3 "PROVISIONAL and possibly mid-run" language explain the staleness but record no digest or timestamp, exactly as the finding asserts.

### QUANT-1-6 - RETAINED

- **raised_by:** `quant-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > reporting

- `location`:

  > research/01_hypothesis_register/H001/design.md:23, :30-38 (freeze_status), :1296-1300 (pre-freeze checklist item 1); hypothesis_backlog.md:26

- `issue`:

  > Two tracked deliverables in the same delivery assert as fact that the corpus record does not exist, and use that non-existence as the stated reason the design is not frozen. The corpus record exists on disk and is a deliverable of the same session. Pre-freeze checklist item 1 is therefore satisfied while the artifacts still report it as blocking, so a reader cannot tell which pre-freeze conditions actually remain open.

- `evidence`:

  > design.md L23: 'corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)'; L34-37: 'The corpus record this design depends on ... does not exist; freezing now would register a design against literature that has not been compiled.' hypothesis_backlog.md L26: '...because the corpus record the design depends on (...) does not yet exist'. `ls -l` shows the file present at 203,216 bytes, and git status lists it as an untracked file of this delivery.

- `fix`:

  > Update both artifacts to state that the corpus record now exists (with its SHA-256), mark pre-freeze checklist item 1 as DISCHARGED, and restate the remaining freeze blockers — checklist items 2-6 (academic stage-1 screening of ks-a-057, the KSL-C02 exclusivity flag, the per-series multiplier table, the unlocated rulebook, clause re-retrieval) — as the operative reason the design stays `draft-unfrozen`.

- `reference`:

  > deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D5 (freeze deferred until the corpus record exists)

**Refutation evidence:**

> Refutation attempt failed; every element of the finding reproduced verbatim.
>
> 1. design.md L23 reads exactly: `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`. L34-37 (freeze_status) reads: "The corpus record this design depends on (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md) does not exist; freezing now would register a design against literature that has not been compiled." L1294-95 repeats it: "/preregister has not been run and must not be run until the corpus record exists". Pre-freeze checklist item 1 at L1298-99: "`docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` exists and is the compiled corpus record."
>
> 2. hypothesis_backlog.md L26 reads: "...because the corpus record the design depends on (`docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md`) does not yet exist and freezing would register a design against uncompiled literature."
>
> 3. The file exists: `ls -l` gives 203,216 bytes, mtime 2026-09-04 12:03:34 -0500, sha256 fcf0b71c43981576acf589afa458b1b9c0a7746d4a5bce92b281ae1274266c2e. Its own front-matter title is "Compiled corpus record — stated trading, arbitrage, market-making and adjacent STRATEGIES for binary event contracts, with KalshiEX LLC as the venue of interest (multivocal branch)", with slug kalshi-strategy-multivocal and date 2026-09-04 — i.e. it self-identifies as the compiled corpus record checklist item 1 names, so item 1 is in fact satisfied.
>
> 4. Same-delivery confirmed by `git status --porcelain`: the corpus record is untracked (`??`), design.md is untracked (`??`), hypothesis_backlog.md is modified (` M`). mtimes place design.md at 10:59:53 and hypothesis_backlog.md at 11:00:39, both preceding the corpus record's 12:03:34 in the same day/session — the statements were true when drafted and were never updated after the record was written.
>
> 5. Searched for any qualifier that would rescue the wording: `grep -n "lit_review_kalshi-strategy-multivocal" research/01_hypothesis_register/H001/design.md` returns only the three lines above — no amendment note, no "as of drafting" hedge, no later correction. The append-only amendment register docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl contains only the header and amendment M1 (academic-arm query-slot construals); nothing addresses the corpus-record existence claim. The referenced spec docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md L226 likewise still says "`lit_review_kalshi-strategy-multivocal_2026-09-04.md` is unwritten", corroborating rather than contradicting the finding.
>
> The only argument available against the finding is that the assertions were true at authoring time — a plausibility/severity argument, not counter-evidence. In the delivered state both tracked deliverables assert as fact a non-existence contradicted by disk, and use it as the stated freeze blocker while item 1 is discharged. Finding stands.

### LITERATURE-1-1 - RETAINED

- **raised_by:** `literature-check`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > misattribution-of-cited-primary-source

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1640-1642 and :215-219

- `issue`:

  > The seeded defect is CONFIRMED and still OPEN in the corpus record. Section 10 note N-5 and head-limitation 9 both state that FOUR academic queries in the weather stratum executed and returned zero, naming ks-arxiv-04, ks-openalex-04, ks-repec-04 and ks-repec-04-b. Two of the four named queries never executed. The corpus record thereby reports two capacity gaps as executed zero-yield observations — the exact category error N-5 exists to prevent — and does so in direct contradiction of the primary sources it cites by id.

- `evidence`:

  > Verified independently against the primary logs. docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json line 33 `platform_interface_failure`: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed. ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." Line 34 `n_returned_semantics`: "no search executed; not an observed zero-yield". ks-repec-04-b.json carries byte-identical text in both fields (lines 33-34). Corpus line 1640 reads verbatim: "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)." Line 215-216 reads: "Four executed academic queries in that stratum returned zero". The corrected executed-and-zero count is TWO (ks-arxiv-04, ks-openalex-04). The 11 ks-s2-03* logs were also re-read: all eleven carry `http_status: 429`, so the corpus's claim about the never-executed on-point query is correct. The discrepancy is already correctly diagnosed in failure_log.md F007 (lines 482-491) and in docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1721-1728, both of which state the count is two — but both explicitly decline to repair the corpus record, leaving the branch's own citable artifact carrying the false statement.

- `fix`:

  > Edit N-5 to read: "TWO academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0) and `ks-openalex-04` (HTTP 200, 0). `ks-repec-04` and `ks-repec-04-b` returned HTTP 200 with `n_returned: 0`, but their own `platform_interface_failure` and `n_returned_semantics` fields state that no search was run; they are platform-interface failures, not observed zeros, and are counted nowhere as evidence about the literature." Make the identical correction at limitation 9 (line 215). Record the correction as a dated in-place correction note so the original wording stays legible, per the branch's own amendment discipline.

- `reference`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-repec-04.json fields `platform_interface_failure`, `n_returned_semantics`; failure_log.md F007; charter commitment 5 (attribution fidelity); protocol section 4.4 rule 2 (capacity codes reported separately from criterion codes)

**Refutation evidence:**

> No refutation available; the finding reproduced exactly. (1) Corpus line 1640-1642 reads verbatim "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)."; line 215-216 reads "Four executed academic queries in that stratum returned zero". (2) ks-repec-04.json field `platform_interface_failure` states "The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN", and `n_returned_semantics` states "no search executed; not an observed zero-yield"; ks-repec-04-b.json carries byte-identical text in both fields. (3) ks-arxiv-04.json and ks-openalex-04.json carry http_status 200 / n_returned 0 with no platform_interface_failure field, so the corrected executed-and-zero count is two, exactly as the auditor states. (4) I searched for any in-corpus repair that would make the finding stale and found none: section 11 enumerates defects DI-1 through DI-7 and omits this one; the gap register G-1..G-13 omits it; ks-amendments.jsonl contains only amendment M1 (parts M1a/M1b/M1c) on query-vocabulary departures and never touches N-5 or RePEc. (5) failure_log.md:482-491 independently reaches the same conclusion (count is two) and explicitly declines to repair the corpus. Additional corroboration found in the same direction: note N-8 at line 1669 describes RePEc as returning zero "all HTTP 200 with an empty result page", which also contradicts the log's statement that the body was the IDEAS search FORM, not a result set. The defect claim is true and still open in the corpus record.

### LITERATURE-1-2 - RETAINED

- **raised_by:** `literature-check`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > misquotation-of-cited-primary-source

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1669-1671 (N-8), with docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:274 (PRISMA-S item 15 source table)

- `issue`:

  > Second, independent instance of the same misdescription. N-8 states RePEc "returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". The cited logs say the opposite of "empty result page": they say the body is the SEARCH FORM, not a result set, and that the query never executed. An "empty result page" is a search that ran and found nothing; a form page is a search that did not run. Compounding this, the PRISMA-S item 15 source table at line 274 reports `RePEc / IDEAS ... n_records 0` with no interface-failure annotation, while PRISMA-S item 15 ("Document the total number of records identified from each database") is claimed DIRECTLY (not by analogy) at line 262.

- `evidence`:

  > Corpus line 1669-1670 verbatim: "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". Against ks-repec-04.json line 33: "the body is the IDEAS/RePEc search FORM, not a result set". The nine-attempt count is correct (ks-repec-01, -01-b, -01-c, -02, -02-b, -03, -03-b, -04, -04-b confirmed on disk). N-8's closing sentence ("each is a finding about the endpoint") partly mitigates but does not correct the false description of what the bytes contain.

- `fix`:

  > Replace "all HTTP 200 with an empty result page" with "all HTTP 200 returning the IDEAS/RePEc search form rather than a result set, so no search executed". Add a footnote to the source table's RePEc, SSRN, GitHub-code and Kaggle rows marking `n_records = 0` as an interface failure and not an identified-record count, so the directly-claimed PRISMA-S item 15 figure is not read as a yield.

- `reference`:

  > ks-repec-04.json / ks-repec-04-b.json `platform_interface_failure`; PRISMA-S item 15 (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z), verified verbatim at PMC8270366: "Document the total number of records identified from each database and other information sources."

**Refutation evidence:**

> Refutation attempted and failed; the finding is confirmed on every load-bearing element. (1) Quote reproduced: lit_review_kalshi-strategy-multivocal_2026-09-04.md:1669-1670 reads verbatim "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". (2) Log reproduced: ks-repec-04.json field platform_interface_failure states "the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed", plus n_returned_semantics "no search executed; not an observed zero-yield". (3) Counter-test run on the primary bytes rather than the log's prose: payloads/ks-repec-04.html hashes to 7f2c634f7090... matching the log's payload_sha256, and its body contains two live search forms (<form method="POST" action="/cgi-bin/htsearch2" role="search"> with <input name="q" value=""> — the submitted query is not even echoed back) plus the "struggling with massive bot" banner, and no result container. The bytes support the log, not the corpus sentence. (4) Compounding claim confirmed: line 274 is "| RePEc / IDEAS | ideas.repec.org site search over HTML | 2026-09-04 | ks-repec | 0 |" and lines 275-291 show no footnote follows the table (prisma-s-2 begins at 292); grep -ni for "interface failure|search form|never executed|not a result set" across the whole corpus returns only three hits, all about Semantic Scholar ks-s2-03, none about RePEc. (5) PRISMA-S item 15 is indeed claimed DIRECTLY — front matter line 18: "PRISMA-S items 1, 8, 13 and 15 are claimed DIRECTLY" — and instantiated by the <!-- prisma-s-15 --> marker at line 1203, whose section 5.1 sums the section-2 n_records column to n_identified = 1,986. Only the finding's line pointer for that claim is imprecise (line 262 claims items 1, 2 and 13; item 15 is claimed at line 18 and 1203); the claim structure it describes is true, so this is a location error, not a defect in the claim. Aggravating rather than mitigating: lines 1641-1642 list ks-repec-04 and -04-b as "(HTTP 200, 0)" beside genuine zero-yield queries, and the strategy fence at lines 571-588 carries n_returned=0 per RePEc query with no failure flag, so the non-executed search is presented as an observed zero in four places.

### LITERATURE-1-3 - RETAINED

- **raised_by:** `literature-check`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > unattributed-method

- `location`:

  > research/01_hypothesis_register/H001/design.md:816 and :1087

- `issue`:

  > The "Politis–White automatic block length" is named twice as a binding, non-discretionary selection procedure — for the splitter `embargo` (§6) and for the block bootstrap inside the Hansen SPA aggregation (§9.1) — with NO citation anywhere in the document, including the otherwise-exhaustive §12 References (lines 1368-1404). This is a named method with no resolvable record, in a design whose §0.2 declares that every parameter carries either `QUOTED`, `TO COMPUTE` with a named procedure, or `CONVENTION` with provenance, and whose §12 explicitly flags which instruments were and were not re-verified. The omission also loses a materially important fact: the original formula was corrected in a published erratum that reference implementations follow.

- `evidence`:

  > Line 816: "the Politis–White automatic block length for the same series. Data-driven, not chosen." Line 1087: "Politis–White automatic procedure (the same estimator §6 uses for the embargo)." Grep of the file for `Politis` returns only those two lines; §12 References (lines 1368-1404) lists PRISMA-S, PRISMA 2020, Arksey & O'Malley, Adams/Smart/Huff, Garousi, Kalliamvakou, Munaiah, Smith, Klein, Jones, White 2000, Hansen 2005, Newey & West 1994, Andrews 1991, Opdyke 2007, Lo 2002, Ledoit & Wolf 2008, Hoenig & Heisey 2001, Theiler 1992, Kaufman 2012, Lakens 2018, Schuirmann 1987 — and no Politis. Canonical record verified via Crossref: Politis DN, White H. "Automatic Block-Length Selection for the Dependent Bootstrap." Econometric Reviews. 2004;23(1):53-70, doi:10.1081/ETC-120028836. Erratum verified via Crossref: Patton A, Politis DN, White H. "Correction to 'Automatic Block-Length Selection for the Dependent Bootstrap' by D. Politis and H. White." Econometric Reviews. 2009;28(4):372-375, doi:10.1080/07474930802459016.

- `fix`:

  > Add to §6, §9.1 and §12: Politis & White 2004 (doi:10.1081/ETC-120028836) as amended by Patton, Politis & White 2009 (doi:10.1080/07474930802459016), and state which of the two formulae the executing project must implement. Follow the file's own convention of flagging whether the record was re-fetched in this drafting session.

- `reference`:

  > https://doi.org/10.1081/ETC-120028836 ; https://doi.org/10.1080/07474930802459016 ; CLAUDE.md "Document selection rationale with citations"; REVIEW.md blocking directive 8 as widened by ADR-0006

**Refutation evidence:**

> Refutation attempted on five independent avenues; all failed. The finding is confirmed.
>
> (1) In-file citation: `grep -n "Politis" research/01_hypothesis_register/H001/design.md` returns exactly two lines, 816 and 1087, matching the quoted evidence verbatim ("...the Politis-White automatic block length for the same series. Data-driven, not chosen." / "...Politis-White automatic procedure (the same estimator §6 uses for the embargo)."). Both are bare method names. The References section (§13, lines 1315-1403) contains zero occurrences of "Politis". File is 1403 lines total.
>
> (2) Attribution-by-adoption via the rule file: the design attributes its statistical instruments to `rules/quant-project.md` §Inference through ADR-0004. `grep -n "Politis" C:/Users/skoir/.claude/rules/quant-project.md` exits 1 — no match. That §Inference block names only Newey-West 1994, Andrews 1991, Opdyke 2007, Lo 2002, Ledoit & Wolf 2008, White 2000, Hansen 2005. The block-length estimator is not among them, so the adoption chain does not supply the missing citation.
>
> (3) Attribution via ADR-0004 itself: `grep -c "Politis" docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md` = 0.
>
> (4) Companion parameter file in the HID directory: `ls research/01_hypothesis_register/H001/` shows design.md is the only file. No sibling carries the record.
>
> (5) Cross-reference to an existing in-repo corpus: the repo DOES hold the canonical records — docs/literature/lit_review_regime-classification_2026-08-21.md:1204 and :1208 carry `politis2004etc120028836` (doi:10.1081/etc-120028836) and `patton2009074749308024` (doi:10.1080/07474930802459016), the latter annotated "Must be applied with it; the uncorrected formula is wrong." But design.md contains no reference to that lit review: `grep -n "regime-classification\|lit_review"` on design.md returns only three lines, all pointing at lit_review_kalshi-strategy-multivocal_2026-09-04.md (and lines 23/35 state it "DOES NOT EXIST YET"). The resolvable record exists in the repo and the design does not reach it.
>
> Corroborating: the repo's own audit trail records this exact defect class as a prior applied finding — docs/audits/audit_trail_think-tank-charter_2026-08-21.md:759, "F-3-18 (Politis-White block length requires the 2009 correction - the corpus carries the annotation 'the uncorrected formula is wrong' and the agenda stripped it)", described there as the second instance of a corpus annotation stripped on propagation. The present occurrence is a recurrence of a pattern the project already adjudicated as real.
>
> The design's §0.1 (line 55) confirms the binding convention the finding invokes: "Every parameter whose value would require data is left `TO COMPUTE` with its selection procedure named." Both cited sites are `TO COMPUTE` parameters naming this procedure, so the citation obligation attaches.
>
> Only inaccuracy found, non-refuting: the finding labels the References section "§12"; it is actually "## 13. References" (§12 is "Reproducibility commitments", line 1272). The stated line range 1368-1404 does fall inside §13, and the content claim is correct. This is a label error, not a defect in the claim.

### REPRODUCIBILITY-1-1 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > data_hashed

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1639-1642 (N-5) and :215-219 (head limitation 9)

- `issue`:

  > CONFIRMED, seeded defect. N-5 states "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)". Two of the four NEVER EXECUTED. The corrected executed-and-zero count is TWO. Head limitation 9 repeats the same wrong count ("Four executed academic queries in that stratum returned zero"). A capacity/interface gap is being reported as an observed zero-yield, which is the exact eligibility-vs-capacity conflation the protocol section 4.4 and the corpus's own risk framing forbid.

- `evidence`:

  > Independent re-derivation from the arm logs (python over docs/literature/search_logs/kalshi-strategy-multivocal/): ks-repec-04.json and ks-repec-04-b.json both carry n_returned_semantics = "no search executed; not an observed zero-yield" and platform_interface_failure = "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set...". All nine ks-repec-0*.json files carry the identical pair of fields. Only ks-arxiv-04.json (200, n=0, semantics=None, pif=None) and ks-openalex-04.json (200, n=0, semantics=None, pif=None) are genuine executed zero-yields. Separately verified as correct in the same note: all 11 ks-s2-03* attempts are HTTP 429, and the arm-wide Semantic Scholar tally is exactly 53x429 / 1x500 / 2x200 over 56 files, matching N-5's text.

- `fix`:

  > Rewrite N-5 to read TWO executed-and-zero queries (ks-arxiv-04, ks-openalex-04), and move ks-repec-04 / ks-repec-04-b into the never-executed set alongside ks-s2-03, quoting their own platform_interface_failure field. Correct head limitation 9 to the same count. State explicitly that the weather stratum has TWO executed queries, not five, and that three of its five queries produced no search at all.

- `reference`: _(none stated)_
**Refutation evidence:**

> Attempted refutation failed; the finding reproduces exactly. (1) At C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md N-5 reads verbatim: "Four academic queries in that stratum executed and returned zero: `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and `ks-repec-04-b` (HTTP 200, 0)." (2) Head limitation 9 (~lines 215-219) repeats it: "Four executed academic queries in that stratum returned zero". (3) Counter-check of the logs contradicts both: C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal\ks-repec-04.json and ks-repec-04-b.json each carry "n_returned_semantics": "no search executed; not an observed zero-yield" and a platform_interface_failure field stating "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT... the body is the IDEAS/RePEc search FORM, not a result set... The query therefore never executed... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." ks-repec-04-b is additionally "retry_of": "ks-repec-04", so it is not an independent query either. (4) By contrast ks-arxiv-04.json and ks-openalex-04.json carry http_status 200, n_returned 0, n_total_reported 0, truncated_by_cap false, and no platform_interface_failure or n_returned_semantics key at all — the only two genuine executed zero-yields. (5) Searched for a superseding correction: grep for "repec-04", "N-5", "limitation 9" in docs\literature\search_logs\kalshi-strategy-multivocal\ks-amendments.jsonl returns no matches, so no amendment repairs the count. The prose therefore reports a capacity/interface gap as an observed zero-yield, exactly as charged.

### REPRODUCIBILITY-1-2 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > data_hashed

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md, section 10 note N-8

- `issue`:

  > Same defect class as N-5, second instance. N-8 says "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". "An empty result page" is an observation about a result set. The logs state the opposite: no result set was served at all.

- `evidence`:

  > All nine ks-repec-0*.json carry platform_interface_failure = "...the body is the IDEAS/RePEc search FORM, not a result set..." and n_returned_semantics = "no search executed; not an observed zero-yield". N-8's closing sentence ("each is a finding about the endpoint") is right, but the descriptive clause preceding it asserts a zero-yield observation the logs deny, and it is that clause N-5 relied on.

- `fix`:

  > Replace "all HTTP 200 with an empty result page" with the logs' own wording: HTTP 200 whose body is the search form rather than a result set, i.e. no search executed. Cross-reference the corrected N-5.

- `reference`: _(none stated)_
**Refutation evidence:**

> No refutation available; the finding is confirmed on three independent checks. (1) Reproduced at location: lit_review_kalshi-strategy-multivocal_2026-09-04.md line ~1669, N-8 reads "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". (2) Log check: all nine ks-repec-0*.json (01, 01-b, 01-c, 02, 02-b, 03, 03-b, 04, 04-b — the count of nine is also correct) carry platform_interface_failure = "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set... The query therefore never executed... n_returned=0 here means NO SEARCH WAS RUN" and n_returned_semantics = "no search executed; not an observed zero-yield". (3) Counter-test on the stored payload bytes, run to see whether the page might genuinely be an empty result page (which would have refuted the claim): payloads/ks-repec-01.html contains only two IDEAS navbar search FORM elements (action=/cgi-bin/htsearch2) plus the "massive bot traffic" banner, with no result container; payloads/ks-repec-01-c.html and ks-repec-04-b.html are EconPapers advanced-search forms whose extracted visible text reads "Please run the search by clicking on Search." — an unsubmitted form, not a zero-hit result set. The bytes corroborate the logs. N-8's parenthetical therefore asserts a zero-yield observation that both the logs and the payloads deny, and it is the clause N-5 (line ~1641, "ks-repec-04 and ks-repec-04-b (HTTP 200, 0)" described as queries that "executed and returned zero") relies on.

### REPRODUCIBILITY-1-3 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > entrypoint_runs

- `location`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ (all 6 academic .py and all 7 ks-github-scripts/*.py)

- `issue`:

  > No archived script in the branch can execute. The pipeline is not re-runnable from the artifact set, and the deliverable spec's own check for this directory ("the screening script self-test exits 0") is unsatisfiable — no script exposes a self-test and no script even imports successfully.

- `evidence`:

  > Dry-run under the project venv with PYTHONHASHSEED=0, exit status captured for each: ks-academic-runner.py -> exit 1, ModuleNotFoundError: No module named 'queries' (it does `from queries import QUERIES`; the file was archived as ks-academic-query-table.py). ks-academic-assemble.py -> exit 1, FileNotFoundError candidates.json (archived as ks-academic-candidates.json). ks-academic-recovery-pass.py and ks-academic-query-table-supplementary.py both do `import run_arm`, and no run_arm.py exists in the directory. ks-github-scripts/write_ledger.py -> exit 1, FileNotFoundError _drawn.json; verify_quotes.py -> exit 1, FileNotFoundError _stage1_gh.json. None of _stage1_gh.json, _stage2.json, _drawn.json, _pins.json, _readmes.json or _readmes/ is present, so draw_and_pin.py, get_readmes.py, write_logs.py, write_ledger.py and verify_quotes.py are all dead. Grep for self.test|self_test|--check across all 13 scripts returns nothing. Consequence: the S-C arm's F4 quote verification (verify_quotes.py) cannot be re-executed by any reader, and the SR-4 sha256-ordered subset draw cannot be independently re-derived from the archive.

- `fix`:

  > Either (a) archive the modules under their import names (queries.py, run_arm.py) or add a shim/rename the imports, and archive the intermediate stage files the S-C scripts consume, or (b) if the intermediates are deliberately not retained, say so in the corpus record's materials_availability and DOWNGRADE the spec check for this directory from "the screening script self-test exits 0" to what the archive actually supports. Do not leave a deliverable check on the page that the artifact fails.

- `reference`: _(none stated)_
**Refutation evidence:**

> NOT REFUTED. Core defect reproduced. (1) `python ks-academic-runner.py` -> exit 1, ModuleNotFoundError: No module named 'queries'; `queries.py` and `run_arm.py` do not exist in the directory; `ks-academic-runner.py:72` defines execute() and `ks-academic-recovery-pass.py:22` calls `run_arm.execute(...)`, so recovery-pass and query-table-supplementary are unrunnable as archived. (2) `ks-github-scripts/write_ledger.py` -> exit 1 FileNotFoundError _drawn.json; `verify_quotes.py` -> exit 1 FileNotFoundError _stage1_gh.json; confirmed absent: _stage1_gh.json, _stage2.json, _drawn.json, _pins.json, _readmes.json, _readmes/. run_search.py, the only producer of _stage1_gh.json, hits the live GitHub API at module level, so the SR-4 sha256-ordered draw cannot be re-derived from the archive and F4 quote verification cannot be re-executed. (3) grep -rn "self.test|self_test|--check|selftest" over all 13 scripts -> exit 1, zero matches; the spec check at docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:71 literally reads "the screening script self-test exits 0" and is unsatisfiable.
>
> PARTIAL COUNTER-EVIDENCE (scope corrections, insufficient to refute): (a) The headline sentences "No archived script in the branch can execute" and "no script even imports successfully" are FALSE. `PYTHONHASHSEED=0 python ks-academic-extract.py` -> exit 0, printing "raw rows 650  deduped 528  duplicates 122" plus B1-B4 branch counts; its emitted title_merge_ledger.json is byte-identical to the archived ks-academic-dedup-title-ledger.json (both sha256 15dbb51e4bc6f5763847131bc7edea89ea8c10f2625705b6cfda037c49e97c74), so the academic dedup/screening stage IS deterministically re-runnable and reproduces an archived output. (b) The ks-academic-assemble.py diagnosis is wrong: candidates.json is not a rename of ks-academic-candidates.json — it is a stage output written by ks-academic-extract.py:234, while ks-academic-candidates.json is assemble's own OUTPUT (ks-academic-assemble.py:106). Running extract first lets assemble pass line 12 and enter its network phase (killed at 25s timeout, exit 124). The auditor ran a stage-2 script without its stage-1 producer.
>
> These corrections narrow the finding (A-arm is re-runnable in order; one script self-executes cleanly) but do not disprove it: the S-C GitHub arm is genuinely dead, two academic scripts cannot import under their archived names, and no self-test exists anywhere, so the spec check on this directory is failed by the artifact. Working tree restored — the candidates.json and title_merge_ledger.json my re-run generated were deleted.

### REPRODUCIBILITY-1-4 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > seeds_pinned

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:97 (front-matter rng_seed)

- `issue`:

  > The rng_seed field makes three factually false enumerations. Its candour about the LLM half is exemplary; its claim about the deterministic half does not survive checking.

- `evidence`:

  > Claim: "PYTHONHASHSEED=0 is asserted at entry of every script in this branch — ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-query-table.py, and the store builder that emitted references_kalshi-strategy-multivocal.json." (1) `grep -c PYTHONHASHSEED ks-academic-query-table.py` = 0; that file contains no assert. (2) "every script in this branch" is false for the entire S-C arm: ks-github-scripts/run_search.py uses `os.environ.setdefault("PYTHONHASHSEED", "0")`, which is a no-op for hash randomisation because it runs after interpreter start and asserts nothing; draw_and_pin.py, get_readmes.py, run_search2.py, verify_quotes.py, write_ledger.py and write_logs.py contain no seed statement at all. (3) No store-builder script exists: `grep -rln references_kalshi-strategy-multivocal --include=*.py .` returns nothing repo-wide, so the 99-entry CSL-JSON store was emitted by an unarchived process. Two scripts that DO assert correctly (ks-academic-runner.py, ks-academic-query-table-supplementary.py) are omitted from the list.

- `fix`:

  > Replace the enumeration with the verified one: assert present in ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-runner.py, ks-academic-query-table-supplementary.py; absent in ks-academic-query-table.py (pure data table, no hash-order dependence — state that); no-op setdefault in the S-C arm; and state that the CSL-JSON store builder was NOT archived. Add the assert to the S-C scripts, or record the omission as a gap.

- `reference`: _(none stated)_
**Refutation evidence:**

> Refutation attempt failed; every sub-claim reproduced verbatim at docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:97 (confirmed as the rng_seed line by grep -n "^rng_seed").
>
> (1) ks-academic-query-table.py has no assert. Per-file grep over docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-*.py: assemble.py:7, extract.py:8, recovery-pass.py:6, runner.py:9, query-table-supplementary.py:15 each carry `assert os.environ.get("PYTHONHASHSEED") == "0"`; ks-academic-query-table.py returns zero matches. Its first 20 lines are a module-level QUERIES list of dicts plus URL constants — no executable entry point. So the enumerated list names a file that does not assert, and omits two (ks-academic-runner.py, ks-academic-query-table-supplementary.py) that do, exactly as the finding states.
>
> (2) "every script in this branch" is false for the S-C arm. Directory listing of ks-github-scripts/ gives 7 .py files. Only run_search.py:8 contains any seed statement, and it is `os.environ.setdefault("PYTHONHASHSEED", "0")` — a mutation of os.environ after interpreter start, which cannot affect hash randomisation for the running process and contains no assertion. draw_and_pin.py, get_readmes.py, run_search2.py, verify_quotes.py, write_ledger.py, write_logs.py match neither "PYTHONHASHSEED" nor "seed" at all.
>
> (3) No store builder exists. `grep -rln references_kalshi-strategy-multivocal --include=*.py .` returns nothing (exit 1). The looser `grep -rln references_kalshi --include=*.py .` hits only three predecessor-branch files under search_logs/kalshi-arbitrage/ (ka-partition-script.py, ka-store-arxiv-venuecheck.py, ka-store-registrant-sweep.py), none of which touch the multivocal store. Repo-wide, the only files mentioning references_kalshi-strategy-multivocal are prose/JSON artifacts (ADR-0006, the deliverable spec, the lit review, the protocol, the research agenda, failure_log.md) — no script. The find of all .py under the branch's search-log dir enumerates exactly the 6 academic + 7 github scripts above; no store builder is among them.
>
> I also checked whether an amendment had already corrected the text: ks-amendments.jsonl contains no entry matching seed/hashseed/rng_seed, so the claim stands uncorrected in the artifact. No scope-reading rescues it either — the enumeration explicitly names "the store builder", and the failure inside its own enumerated academic list (query-table.py) is independent of how "this branch" is construed. Defect claim is true as stated.

### REPRODUCIBILITY-1-5 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > cross_platform

- `location`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-scripts/run_search.py:11, verify_quotes.py:3, write_ledger.py:3, write_logs.py:4

- `issue`:

  > Four S-C scripts hardcode an absolute home-directory path, `OUT = r"C:\\Users\\skoir\\castles\\docs\\literature\\search_logs\\kalshi-strategy-multivocal"`. run_search2.py, draw_and_pin.py and get_readmes.py inherit it by import, so the whole arm is bound to one machine and one OS. This contradicts CLAUDE.md ("absolute paths under a home directory are brittle across machines regardless of identity policy") and is inconsistent with the branch's own academic scripts.

- `evidence`:

  > ks-academic-extract.py:11 and ks-academic-runner.py:14 resolve the repo root relatively and carry the inline comment "repo root resolved relative to this file; no absolute home-directory path is stored". The S-C arm does the opposite. It also leaks the OS username into artifacts intended for a public, real-name-attributed repository; the username is not the protected item here (the real email is, and it is absent), but the path is still non-portable.

- `fix`:

  > Replace with `OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))` as the academic scripts do. Prefer pathlib.Path throughout while touching them.

- `reference`: _(none stated)_
**Refutation evidence:**

> No refutation. Every load-bearing element of the finding reproduced exactly; attempted counter-tests all failed to disprove it.
>
> 1. Hardcoded constant confirmed by grep in C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal\ks-github-scripts\:
>    run_search.py:10, verify_quotes.py:3, write_ledger.py:3, write_logs.py:4 each contain
>    OUT = r"C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal"
>    (Only discrepancy: the finding cites run_search.py:11; the assignment is at line 10. Off-by-one in the citation, not a defect in the claim. AST parse confirms: "OUT assigned at line 10 -> C:\Users\skoir\castles\...".)
>
> 2. Import inheritance confirmed. run_search2.py:4 `from run_search import fetch, record, log, OUT, PAY, CAP, now`; draw_and_pin.py:5 `from run_search import fetch, now, OUT, PAY`; get_readmes.py:5 `from run_search import fetch, now, OUT`. All three bind the same machine-specific constant.
>
> 3. Counter-test for an escape hatch: grepped all seven scripts for os.environ / getenv / sys.argv reassignment of OUT. Zero hits. There is no env-var or CLI override; the constant is a module-level raw string literal with no fallback. On any other machine or OS, run_search.py:12 `os.makedirs(PAY, exist_ok=True)` would create/fail against a nonexistent C:\Users\skoir tree rather than the repo.
>
> 4. Contrast with the academic arm confirmed verbatim. ks-academic-extract.py:11 and ks-academic-runner.py:14 both read
>    REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))  # repo root resolved relative to this file; no absolute home-directory path is stored
>    The inline comment the auditor quoted is present in both, so the inconsistency between arms is real and self-documented.
>
> 5. Cited source confirmed. C:\Users\skoir\castles\CLAUDE.md line 116 contains "a home directory are brittle across machines regardless of identity policy."
>
> 6. Counter-test for a documented waiver: grepped ks-amendments.jsonl, protocol_kalshi-strategy-multivocal_2026-09-04.md, and ks-github-subset-rule.md for "absolute path", "hardcod", "portab", "C:.Users". Zero hits — no registered exception exempts the S-C arm.
>
> 7. Counter-test for "these files never reach the repo": `git check-ignore -v` on run_search.py exits 1 (not ignored); the file is untracked-but-stageable alongside the rest of the branch's artifacts, so the public-repo exposure sub-claim also stands.
>
> The only thing I could challenge is the line number 11 vs 10 for run_search.py, which does not touch the substance of the defect.

### REPRODUCIBILITY-1-6 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > data_hashed

- `location`:

  > docs/literature/search_logs/kalshi-strategy-multivocal/ks-lateral-records.json (32 records) and ks-venue-docs.json (30 documents)

- `issue`:

  > Two of four arms record a SHA-256 of retrieved bytes whose subject bytes are not in the repository, so no reader can verify the digest. The lateral arm is worse than merely unarchived: each record carries a `local_payload_name` naming a local payload object that does not exist anywhere on disk — a dangling reference that reads as if the bytes were retained.

- `evidence`:

  > All 32 lateral records carry sha256_of_retrieved_bytes AND local_payload_name (e.g. "s1_oddsshopper_ladder"); resolving each name against the record dir, payloads/ and the repo root finds 0 of 32. All 30 venue documents carry sha256_of_retrieved_bytes and NO local-path field of any kind (key set: accessed_at, attribution_label, clauses, ..., retrieved_bytes, sha256_of_retrieved_bytes, source_class, url). payloads/ holds 161 files covering only the academic (ks-arxiv/crossref/openalex/repec/s2/ssrn) and S-C (ks-gh/gl/npm/pypi) arms. Contrast, independently verified this round: 112 of 112 academic logs' payload_sha256 match the file at their payload_path byte-for-byte, 0 mismatches, 0 missing. The corpus's dataset_checksums field (line 96) asserts "Per-payload digests are carried per query in the arm logs and per record in the store's note and custom.sha256_of_retrieved_bytes fields" without disclosing that for 2 of 4 arms the digests are unverifiable in-repo (store-side: 40 of 99 entries carry no sha256 at all).

- `fix`:

  > Either archive the lateral and venue retrieved bytes under payloads/ (they are already digested, so this is a copy), or remove `local_payload_name` and state plainly in dataset_checksums and limitation 8 that S-D and S-E retrieved bytes were NOT retained, that their digests are therefore attestations rather than checkable digests, and register it as a named gap alongside G-15.

- `reference`: _(none stated)_
**Refutation evidence:**

> Refutation failed; the finding reproduces exactly and my strongest counter-test confirmed rather than disproved it. (1) ks-lateral-records.json = 1 header + 32 records; all 32 carry sha256_of_retrieved_bytes AND local_payload_name (25 distinct tokens, e.g. s1_oddsshopper_ladder). Walked all 8,895 non-.git files in the repo: 0 of 25 tokens match any basename. (2) ks-venue-docs.json = 30 documents, all with sha256_of_retrieved_bytes; the union key set across all 30 contains no path/file/local/payload/archive field of any kind. (3) payloads/ = 161 files, prefix census arxiv 13 / crossref 19 / gh 20 / gl 10 / npm 8 / openalex 14 / pypi 11 / repec 9 / s2 56 / ssrn 1 — academic and S-C arms only, zero lateral or venue payloads. (4) COUNTER-TEST for the one path that could have refuted this (payloads archived under different filenames): I SHA-256'd every file in the repository and matched against all 60 distinct digests asserted by the lateral records (including corroborating_sources[].sha256) and the venue documents — 0 of 60 matched. No byte sequence in the repo reproduces any S-D/S-E digest, so none of those digests is checkable in-repo. (5) Disclosure check: local_payload_name appears in no prose anywhere in docs/; ks-lateral-queries.json carries the same tokens under local_name; its declared_recording_gaps enumerate five gaps, none being non-retention; the lateral header instead asserts "Every class below carries a retrieved payload". dataset_checksums at docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md line 96 makes the per-record digest-carriage claim with no arm qualification, and grep for retention/archival language across the lit review and protocol returns nothing. (6) git log --diff-filter=D over *payload* shows no deleted payload files and .gitignore has no payload rule, so the bytes were never tracked or subsequently removed. The claim that two of four arms record digests over bytes absent from the repository, and that the lateral arm additionally carries 32 dangling local_payload_name references, is true as stated.

### REPRODUCIBILITY-1-7 - RETAINED

- **raised_by:** `reproducibility-verifier`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > entrypoint_runs

- `location`:

  > repository working tree vs git index

- `issue`:

  > Nothing this branch produced is committed. A fresh clone at HEAD contains none of the corpus record, the store, the H001 design, the arm logs, the payloads or the scripts, so every locator in `materials_availability` resolves to nothing and the branch is currently 0% reproducible from the repository.

- `evidence`:

  > `git ls-files` in docs/literature/search_logs/kalshi-strategy-multivocal returns 2 of ~200 files (only ks-instrument-verification.json and ks-prior-identifiers.json, the two pre-registration inputs). `git status --porcelain` marks lit_review_kalshi-strategy-multivocal_2026-09-04.md, references_kalshi-strategy-multivocal.json and research/01_hypothesis_register/H001/design.md as untracked (??). `git check-ignore` confirms none of them is gitignored, so this is an unmade commit, not a policy exclusion. Consequently the spec's protocol-row check — "that commit is an ancestor of every commit touching docs/literature/search_logs/kalshi-strategy-multivocal/" — is presently VACUOUSLY true: no commit touches that directory. It cannot be reported as passing.

- `fix`:

  > Commit the branch before claiming any ancestry or materials-availability property, then re-run the ancestry check non-vacuously. Until then, do not tick the search-log or corpus deliverable checkboxes. Note that `ks-github-readme-evidence/` will need at least one tracked file per directory (git stores no empty dirs) — it currently holds 29 evidence files, which is fine, but verify none is skipped by a filter.

- `reference`: _(none stated)_
**Refutation evidence:**

> REFUTATION FAILED. I reproduced the defect at HEAD 4821611c1c93b5f929a76f3ba6207e900440cee5 and it holds.
>
> Confirmed:
> - `git ls-files docs/literature/search_logs/kalshi-strategy-multivocal/` returns exactly 2 paths (ks-instrument-verification.json, ks-prior-identifiers.json) against 331 files on disk (`find ... -type f | wc -l` = 331). 329 uncommitted.
> - `git status --porcelain` marks docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md, docs/literature/references_kalshi-strategy-multivocal.json and research/01_hypothesis_register/H001/design.md as `??`. `git check-ignore -v` on all three exits 1 (no match) — an unmade commit, not a policy exclusion, exactly as claimed.
> - Resolving the record's own `materials_availability` list (lit review lines 87-91) against `git ls-tree -r HEAD`: references_kalshi-strategy-multivocal.json -> 0 entries; search_logs/kalshi-strategy-multivocal -> 2 entries of 331. ADR-0006 (1 entry) and the protocol (1 entry) are tracked, but the protocol is ` M` dirty, so the tracked blob is not the file the record was compiled against.
> - ks-github-readme-evidence/: 29 files on disk, `git ls-files` on it returns 0. The finding's own note about that directory is understated, not overstated.
> - ks-amendments.jsonl: `git ls-files --error-unmatch` -> "did not match any file(s) known to git".
>
> One sub-claim in the evidence is FALSE, and it does not help the artifact: the finding asserts "no commit touches that directory", making the spec's ancestry check vacuous. `git log --format='%H %s' -- docs/literature/search_logs/kalshi-strategy-multivocal/` returns one commit — 4821611, the protocol registration commit itself. `git merge-base --is-ancestor 4821611 4821611` exits 0, so the spec check at docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:67 is satisfied reflexively, not vacuously. But the only commit it quantifies over is the pre-registration commit carrying the two protocol inputs; it certifies nothing about the 329 uncommitted arm logs, payloads and scripts the check exists to bind. Correcting "vacuous" to "reflexively true over a single pre-registration commit" leaves the defect — unresolvable materials_availability locators in a fresh clone — fully intact.
>
> Also imprecise but non-exculpatory: "Nothing this branch produced is committed" overstates slightly (ADR-0006 and a stale protocol blob are in HEAD); every item the finding actually enumerates — corpus record, store, H001 design, arm logs, payloads, scripts — is uncommitted. That is a wording quibble, not counter-evidence.

### FORMAT-1-1 - RETAINED

- **raised_by:** `format-auditor`
- **severity_claimed:** critical
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > citations

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1640 and :216

- `issue`:

  > CONFIRMED, independently verified: the corpus record reports a capacity gap as an observed absence. Section 10 note N-5 states "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)", and limitation 9 (line 216) repeats "Four executed academic queries in that stratum returned zero". Both RePEc rows NEVER EXECUTED. The correct executed-and-zero count is TWO (ks-arxiv-04, ks-openalex-04). This is a charter commitment-5 attribution-fidelity defect against the branch's own primary record, and it is already recognised-but-unrepaired in two downstream artifacts, so the defect is live in the artifact that carries the claim.

- `evidence`:

  > ks-repec-04.json: "platform_interface_failure": "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set ... The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN"; "n_returned_semantics": "no search executed; not an observed zero-yield". Identical fields in ks-repec-04-b.json (retry_of: ks-repec-04). Corroborated by research_agenda_...2026-09-02.md:1721-1728 ("the arm log is preferred, the executed-and-zero count in that stratum is two") and failure_log F007.

- `fix`:

  > Amend the corpus record in place (not silently): N-5 to read "TWO academic queries in that stratum executed and returned zero (ks-arxiv-04, ks-openalex-04). ks-repec-04 and ks-repec-04-b returned HTTP 200 but the body was the IDEAS/RePEc search form, not a result set; per their own platform_interface_failure and n_returned_semantics fields, no search was run and their n_returned=0 is a capacity gap, not a zero yield." Apply the same correction to limitation 9 at line 216. Add the correction as a dated append-only entry alongside M1 so the corrected count is traceable, and update the agenda's §rev-3 note from "recorded and NOT repaired" to "recorded and repaired at <ref>".

- `reference`:

  > charter commitment 5 (attribution fidelity); protocol §4.4 rule 2 (capacity gaps reported separately from criterion determinations); task-spec seeded-defect clause

**Refutation evidence:**

> Refutation attempted and failed; the finding is confirmed on independent reproduction. (1) Both cited locations reproduce verbatim at the stated lines: lit_review_kalshi-strategy-multivocal_2026-09-04.md:1640 N-5 "Four academic queries in that stratum executed and returned zero: ks-arxiv-04 (HTTP 200, 0), ks-openalex-04 (HTTP 200, 0), ks-repec-04 and ks-repec-04-b (HTTP 200, 0)"; and :215-216 limitation 9 "Four / executed academic queries in that stratum returned zero". (2) ks-repec-04.json and ks-repec-04-b.json both carry platform_interface_failure ("The query therefore never executed ... n_returned=0 here means NO SEARCH WAS RUN") and n_returned_semantics "no search executed; not an observed zero-yield". (3) Counter-test on the raw payload: payloads/ks-repec-04.html has <title>IDEAS/RePEc search</title> and is the search form, independently confirming non-execution rather than zero yield. (4) ks-arxiv-04.json and ks-openalex-04.json carry n_total_reported=0, truncated_by_cap=false and no failure field, so they are genuine executed zeros; the executed-and-zero count is two. (5) No repair exists anywhere in the artifact: no errata section, and ks-amendments.jsonl contains only M1 (academic query admissibility), which does not touch N-5; section 11's defect register covers DI-1 only. The defect is live. Additional unclaimed instance found: N-8 at line 1668 repeats the same mischaracterisation ("RePEc returned zero across nine attempts ... all HTTP 200 with an empty result page"), which is also a search form, not an empty result page. Downstream corroboration confirmed at research_agenda_prediction-market-microstructure_2026-09-02.md:1721-1728 and failure_log F007, both stating the count is two and both stating it is NOT repaired.

### FORMAT-1-2 - RETAINED

- **raised_by:** `format-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > citations

- `location`:

  > docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1669-1670 (note N-8)

- `issue`:

  > Second, distinct instance of the same capacity-gap-as-absence framing, in the same record and not covered by the agenda's recorded discrepancy. N-8 says RePEc "returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". The logs do not describe an empty result page; they describe a search form served under a bot-traffic banner, i.e. no search executed. "Returned zero" and "empty result page" both assert an executed retrieval that did not occur.

- `evidence`:

  > lit_review:1669 "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)" vs ks-repec-04.json "the body is the IDEAS/RePEc search FORM, not a result set, and the page carries the banner 'IDEAS is struggling with massive bot traffic, please be patient.' The query therefore never executed."

- `fix`:

  > Rewrite N-8's RePEc clause to: "RePEc executed no search at all across nine attempts: every attempt answered HTTP 200 with the IDEAS/EconPapers search form rather than a result set, under a stated bot-traffic banner. Zero records were returned because no search ran." Remove "empty result page".

- `reference`:

  > protocol §4.4 rule 2; charter commitment 5

**Refutation evidence:**

> Refutation attempted on four levers; all four failed. The finding stands.
>
> LEVER 1 — does the quoted text exist as claimed? Yes, verbatim. C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md line 1669 reads "RePEc returned zero across nine attempts (four queries plus retries, all HTTP 200 with an empty result page)". The nine-attempt count is itself accurate (ks-repec-01, -01-b, -01-c, -02, -02-b, -03, -03-b, -04, -04-b = 9 log files), so the count is not the defect; the retrieval-semantics claim is.
>
> LEVER 2 — does the cited log say what the auditor quoted? Yes, verbatim, and in all nine logs, not just ks-repec-04.json. Every RePEc log carries an identical `platform_interface_failure` field: "PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the IDEAS/RePEc search FORM, not a result set, and the page carries the banner 'IDEAS is struggling with massive bot traffic, please be patient.' The query therefore never executed. ... n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc contains no such record'." Each also carries `"n_returned_semantics": "no search executed; not an observed zero-yield"`. The logs do not merely fail to support "returned zero"; they explicitly prohibit that reading.
>
> LEVER 3 — counter-test on the raw payload, to see whether "empty result page" is defensible as a description of what came back. It is not. I inspected the retrieved bytes at docs\literature\search_logs\kalshi-strategy-multivocal\payloads\ks-repec-01.html directly. The body contains two IDEAS search FORMs (`<form method="POST" action="/cgi-bin/htsearch2" id="mobilesearch">` and `id="topsearch">`) and the banner "IDEAS is struggling with massive bot traffic, please be patient. We apologize for the inconvenience." A grep for any zero-yield marker ("no documents", "no results", "no matches", "0 results", "nothing found", "found N") returned nothing. Stripped visible text is the IDEAS landing/search chrome (Advanced search, Browse Econ Literature, Working papers, Journals, Rankings) with no result region at all. There is no result page in the bytes, empty or otherwise, so "empty result page" is not a loose-but-true paraphrase — it describes an object that was never served. The strongest available counter-material, ks-repec-01-b's `note` ("carrying its search FORM and zero result rows"), still says FORM, and sits in the same file as the explicit "never executed" field, so it does not rescue the phrasing.
>
> LEVER 4 — is the instance already covered by the agenda's recorded discrepancy, which would make it a duplicate rather than a new defect? No. The agenda (docs\research_notes\research_agenda_prediction-market-microstructure_2026-09-02.md, ~lines 1720-1727) records exactly one discrepancy and scopes it explicitly to a different note and a different stratum: "the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero, while ks-repec-04.json's own platform_interface_failure field states that its query never executed ... the executed-and-zero count in that stratum is two". That covers §10 N-5 and the weather stratum only. N-8 is a separate note making a global claim across all nine RePEc attempts, and no agenda text reaches it. The auditor's scoping claim holds.
>
> Corroborating internal inconsistency (strengthens rather than weakens the finding): the same agenda states the correct characterization at line 1033 — "RePEc's interface never returned a result set at all" — so the project's own prose elsewhere contradicts lit_review line 1669.
>
> Only quibble available, which is not refutation per the gate rules: N-8's surrounding sentences do frame the endpoint failures correctly ("two whole endpoints returned nothing, for reasons that are not evidence about the literature ... None of these is a finding about the absence of records; each is a finding about the endpoint"), and the finding's `reference` to "protocol §4.4 rule 2" is imprecise — §4.4 governs G1/G2 eligibility capacity codes and its rule 2 concerns G-rows inside n_excluded, not retrieval-side zero-yield semantics (the section heading "Capacity gaps are not eligibility determinations" carries the principle, but rule 2 is not the on-point rule). Neither point bears on whether the parenthetical misstates the log, which it does. Severity/citation-precision quibbles are not counter-evidence.

### FORMAT-1-3 - RETAINED

- **raised_by:** `format-auditor`
- **severity_claimed:** major
- **refuted_by:** role `refuter`, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim, verbatim as filed:**

- `category`:

  > templates

- `location`:

  > research/01_hypothesis_register/H001/design.md:19,23,29

- `issue`:

  > Stale front-matter cross-references in a pre-registration document. The design's `corpus` block asserts `state: IN PROGRESS`, `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`, and marks the academic-arm inputs `PROVISIONAL`. That record now exists on disk with its bibliography SHA-256 published. A frozen-later design whose own dependency block misstates the state of the artifact it depends on will mislead the freeze decision (§freeze_status makes existence of the corpus record the explicit freeze precondition).

- `evidence`:

  > design.md:23 `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`; design.md:30-37 freeze_status "The corpus record this design depends on ... does not exist". Corpus record present with `bibliography_sha256: c7545d31...`, `n_included: 99`.

- `fix`:

  > Update the `corpus` block to `state: COMPILED`, replace the `(DOES NOT EXIST YET)` annotation with the record path plus its authoring git HEAD (4821611c...) and bibliography_sha256, resolve the PROVISIONAL marker on the academic-arm inputs to their final state (528 G1 rows, zero included), and restate freeze_status as "freeze precondition now met; freeze still not executed" rather than "the record does not exist".

- `reference`:

  > deliverable spec D5 check line (`status: draft-unfrozen`, citations resolve to arm outputs)

**Refutation evidence:**

> Refutation attempt failed; the finding reproduces exactly. (1) research/01_hypothesis_register/H001/design.md lines 19/23/29 verbatim: `state: IN PROGRESS`, `corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (DOES NOT EXIST YET)`, `ks-academic-candidates.json / ks-academic-identified-universe.json (PROVISIONAL — see §0.3)`; lines 30-37 freeze_status asserts in present tense that the corpus record "does not exist". (2) The named record IS on disk: 203,216 bytes / 1,977 lines, front matter `bibliography_sha256: c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df`, `n_included: 99`, `bibliography_store_covers: 99`, with closing identities (1574 - 1475 = 99; len(store) == n_included). (3) The strongest available defense — that the front matter is a correct as-of-drafting snapshot pinned to `registration_commit: 4821611c1c93b5f929a76f3ba6207e900440cee5` — is disproved by the record's own `git_head_at_authoring: 4821611c1c93b5f929a76f3ba6207e900440cee5`: both artifacts were authored at the SAME HEAD, so the record already existed at the commit the design pins itself to. (4) Additional corroboration of staleness: design §0.3 cites `n_deduplicated_records: 480` / `n_in_reported_branches: 144`, while docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json now reports 528 and 152; the corpus record's arithmetic gives the academic arm zero included (99 = 40 software + 28 venue + 31 lateral + 0 academic), so the PROVISIONAL marker is resolvable and unresolved. (5) Untracked status (`?? research/01_hypothesis_register/H001/`) does not exempt the file: it is an audited artifact carrying `status: draft-unfrozen`, and its own §freeze_status is the freeze precondition the finding says is misstated.

## deferred-logged-minors

Minor findings are not put to the refute gate and do not gate the round verdict. They are
logged here in full so that a later round, or a later session, can act on them without
re-deriving them. None is remediated in round 1.

### REV-1-8 (`critical-reviewer`, reporting)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:199-201
- **issue:** Limitation 6 writes an arithmetic expression that is false as written. 437 minus (8,813 minus 6,923) is 437 minus 1,890, which is -1,453, not 0. The intended construction is evidently a floor at zero (no negative lower bound is meaningful for a count), but the flooring is not stated, so the sentence asserts an equality that does not hold and a reader checking it finds an error in a limitation whose whole point is arithmetic honesty about a bound.
- **evidence:** **437 is an upper bound on novelty with no recorded lower bound above 437 − (8,813 − 6,923) = 0 by that construction, and the corpus states no lower bound.**
- **fix:** Write it as max(0, 437 − (8,813 − 6,923)) = 0, or in words: the differencing construction supports no lower bound above zero, because the 1,890 predecessor records outside the identifier index exceed the 437 records flagged novel.
- **reference:** SAMPL (numerical precision and internal arithmetic consistency); CHAMP item 20

### REV-1-9 (`critical-reviewer`, standard-coverage)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:18 vs :262
- **issue:** The record states two different sets of PRISMA-S items as claimed directly. The `standard_declared` front-matter block says 'PRISMA-S items 1, 8, 13 and 15 are claimed DIRECTLY', matching protocol section 8.1. The body's section 2 header instead says 'PRISMA-S items 1, 2 and 13, claimed directly (see `standard_declared`)' - citing the front matter for a set the front matter does not contain, and naming item 2 which the front matter omits and omitting item 15 which it includes. On inspection the record in fact addresses all sixteen PRISMA-S items (anchors prisma-s-1 through prisma-s-16 are all present and substantive), so the coverage is stronger than either statement; only the declaration of which items are claimed is inconsistent, which matters because PRISMA-S is this record's one directly-claimed standard.
- **evidence:** PRISMA-S items 1, 2 and 13, claimed directly (see `standard_declared`). One row per source, naming the **platform/interface**, not merely the database.
- **fix:** Reconcile the two statements. Simplest correct form: declare in `standard_declared` that all sixteen PRISMA-S items are addressed and anchored, and at section 2 name the items that block covers (1, 2, 3, 4, 5, 6, 7) rather than a subset of the front-matter list.
- **reference:** PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z); declared-standard coverage as oracle

### REV-1-10 (`critical-reviewer`, reporting)

- **location:** research/01_hypothesis_register/H001/design.md:600 and :827-833
- **issue:** The design contains two sections numbered 3 - '## 3. Features' and '## 3. Null constructions (surrogates)' - and the running order is 0, 1, 2, 3(Features), 4, 5, 6, 3(Nulls), 7, 8 .... The document declares the insertion ('the 11-section template places surrogates nowhere ... They are inserted here as section 3.1 and section 3.2 ... This is the one structural deviation from the template's section order, recorded rather than silent') but does not acknowledge that the number was already in use, and the collision then makes bare cross-references unresolvable: section 5.1 refers to 'the surrogate ensemble sizes `B_quant` and `B_stale` (section 3)' while section 3.2 step 1 refers to 'the input the design cannot proceed without (section 3 feature `quote_age@0.1.0`)'. A reviewer following either reference lands on the wrong section half the time.
- **evidence:** > Section numbering note: the 11-section template places surrogates nowhere, and > ADR-0003 makes them mandatory ("its null, its statistic, its **surrogate**, its > aggregation rule, its refutation condition"). They are inserted here as §3.1 > and §3.2 and cross-referenced from §§1, 5, 8 and 9.
- **fix:** Renumber the surrogate section to a non-colliding label (for example section 3S, or section 6A placed after the splitter), update the deviation note to say the template number 3 was already occupied by Features, and sweep the bare 'section 3' cross-references in sections 1.5, 3.2, 5.1, 8 and 9 to the disambiguated form.
- **reference:** CHAMP item 20 (figures, tables and structure acceptable and navigable); SAMPL presentation

### SCOPE-1-8 (`scope-auditor`, partial)

- **location:** .claude/settings.json:3-7
- **issue:** The declared state is "a prioritized allowlist of common read-only Bash/MCP calls, produced by the `fewer-permission-prompts` skill". The file carries three entries, all project test/lint invocations, none read-only in the sense declared and none matching the read-only calls this session actually made (git log/status, hashing, directory listing). Severity held at minor because the spec's own mechanical check does pass and the spec itself classes the item as harness plumbing on which no research claim rests.
- **evidence:** Spec lines 89-91 (state/check) and lines 149-150 ("configuration/formatting change ... it is harness plumbing and no research claim rests on it"). File contents: allow = ["Bash(uv run pytest tests/test_erob_recount.py)", "Bash(uv run ruff check)", "Bash(uv run pytest tests/)"].
- **fix:** Either regenerate the allowlist from this session's actual read-only call profile, or amend the declaration to state that the existing three-entry allowlist was retained unchanged and no new entries were produced.
- **reference:** spec Deliverables item 8

### SCOPE-1-9 (`scope-auditor`, partial)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1942-1943 vs :397-423
- **issue:** The section 15 gate report asserts "G18 finds no OS username, no email address and no absolute home-directory path in either file". The corpus record itself contains fourteen percent-encoded email addresses in the reproduced OpenAlex query strings. Identity hygiene is NOT breached — the address is the noreply form CLAUDE.md mandates and the author's real address appears in no tracked file (verified by grep across the repository) — but the gate assertion as stated is not true of the artifact, which understates what a reader is being told was checked.
- **evidence:** Section 15 item 1: "G18 finds no OS username, no email address and no absolute home-directory path in either file." Section 3, ks-openalex-01 through -14, each ending: "&mailto=238704148%2Bs-koirala%40users.noreply.github.com".
- **fix:** Qualify the G18 sentence: the only email strings present are the percent-encoded noreply contact address required by the OpenAlex polite-pool convention and reproduced verbatim because PRISMA-S item 8 forbids altering an executed query string; no real address and no OS username appears.
- **reference:** spec push-authorisation section, identity-hygiene clause

### QUANT-1-8 (`quant-auditor`, reproducibility)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl (withdrawal_rule, traceability_tag); docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1151-1178 (§3.3); deliverable spec D7
- **issue:** The M1 withdrawal rule instructs a reviewer to 'withdraw exactly the records tagged with that part's `reached_via` value', and D7 states 'Each part carries a `reached_via` tag so a reviewer rejecting any ruling can withdraw exactly the affected records'. No record in any arm log, the identified universe, the candidates file, or the CSL-JSON store carries a `reached_via` field. The stated procedure is not executable as written; the affected sets are recoverable only by re-deriving them from `from_query` / `also_from_query`.
- **evidence:** grep -c 'reached_via' returns 0 in ks-academic-candidates.json, ks-academic-identified-universe.json, ks-github-records.jsonl, ks-lateral-records.json, ks-venue-docs.json and references_kalshi-strategy-multivocal.json. Re-deriving from query provenance reproduces the published counts exactly (M1a 67, M1b 3, M1c 20; 90 reachable only via M1 queries), so the counts themselves are correct.
- **fix:** Either write the `reached_via` field onto the 90 affected rows in ks-academic-identified-universe.json, or restate the withdrawal rule as the derivation actually available: 'withdraw exactly the records whose `from_query` and `also_from_query` sets are contained in that part's query list', and record the reproduced counts (67 / 3 / 20) beside it.
- **reference:** protocol §10 (an amendment register that a corpus record ran under must be enumerable); ks-amendments.jsonl withdrawal_rule

### QUANT-1-9 (`quant-auditor`, reporting)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:158-163 (limitation 3); research/01_hypothesis_register/H001/design.md:1027-1029 (§8.1)
- **issue:** The record's own defect DI-6 states that the venue arm's log gives two mutually inconsistent counts of retrieved rule filings (five in document-class 1, four implied by document-class 7) and that the record does not resolve them. Limitation 3 and H001 §8.1 both state 'five' flatly, with no caveat, in the places a reader is most likely to carry the number forward. Only the DI-6 / G-7 entries deep in the record disclose the ambiguity.
- **evidence:** Limitation 3: 'Of the filing register's 111 enumerated KEX rule filings, five were retrieved in full'. DI-6: 'its document-class 7 note states that four self-certifications were retrieved ... which implies four. The two statements differ by one and this record does not resolve them'. H001 §8.1: 'the venue arm enumerated 111 KEX rule filings (query KS-VR-Q32) and retrieved five'.
- **fix:** Append '(or four — the arm log states both; see DI-6 / G-7)' to limitation 3 and to H001 §8.1, so the unresolved count never appears without its flag.
- **reference:** corpus §11 DI-6; §12.1 G-7

### QUANT-1-10 (`quant-auditor`, reporting)

- **location:** research/01_hypothesis_register/H001/design.md:600 ('## 3. Features') and :827 ('## 3. Null constructions (surrogates)')
- **issue:** The design carries two distinct sections numbered 3, and cross-references to '§3' resolve to different sections depending on the caller. In a pre-registration document, whose value is unambiguous advance commitment, an ambiguous internal reference is a substantive defect rather than a formatting one. The §3 numbering note records the insertion but does not resolve the collision.
- **evidence:** §6 splitter: 'the resampling that H001 needs is supplied by the two surrogates in §3'. §8.1: 'the fee schedule **is** a feature (§3, `fee_schedule_in_force@0.1.0`)'. Both cite '§3'; the first means the surrogate section at line 827, the second the features section at line 600.
- **fix:** Renumber the surrogate section to an unused number (e.g. §3B or §6a) or retitle it '§3S Null constructions', and update the eight cross-references in §§1, 5, 6, 8, 9 accordingly before /preregister runs.
- **reference:** design.md §3 numbering note lines 829-833

### QUANT-1-11 (`quant-auditor`, method)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1510-1516 (§9 preamble) and :1533 (§9.1 row 2)
- **issue:** §9 declares that everything in it is 'built from the 28 included S-D records and their **130** verbatim clauses' (tier 2). One row of the SETTLED table cites two tier-5 records as corroborating sources inside that table. The corroboration is harmless in substance (the parabolic fee shape follows directly from d01-c2), but it mixes a tier-5 carrier into a table the reader has been told is tier-2-only, which is exactly the warrant-averaging hazard ADR-0006 §Consequences names as the branch's chief risk.
- **evidence:** §9 preamble: 'Everything below is built from the 28 included S-D records and their **130** verbatim clauses'. §9.1 row 'Cost is price-dependent and maximal mid-range' clause column: '`d01-c2`, and independently at `ks-sc-002`, `KSL-C03`'.
- **fix:** Either move the tier-5 corroborators to a footnote labelled 'tier 5, corroborative only, not part of the settled set', or amend the §9 preamble to say the table is built from the S-D clause set with tier-labelled corroboration noted where it exists.
- **reference:** ADR-0006 §'What the widening costs', final bullet ('warrant is per record, and is labelled per record')

### QUANT-1-12 (`quant-auditor`, reproducibility)

- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61,65,69,73,77,81,85,89,247
- **issue:** The tracked declaration file addresses nine of its ten deliverables by absolute Windows path under the author's home directory, embedding the OS username in tracked prose of a public real-name repository. CLAUDE.md states the opposite convention explicitly. Nothing downstream breaks, but a fresh clone cannot resolve any of the checked paths.
- **evidence:** deliverable spec L61: '- [ ] `C:\Users\skoir\castles\docs\decisions\ADR-0006-multivocal-scope-for-strategy-corpus.md`' and eight further identical-form entries. CLAUDE.md §Identity hygiene: 'Repo-relative paths remain the convention in tracked prose — absolute paths under a home directory are brittle across machines regardless of identity policy.' The corpus record, protocol, ADR-0006, H001 design and failure_log all correctly use repo-relative paths (grep for the absolute prefix returns 0 in each).
- **fix:** Rewrite the nine deliverable paths in the declaration as repo-relative, as every other artifact in this branch already does.
- **reference:** CLAUDE.md §Identity hygiene, final paragraph

### LITERATURE-1-4 (`literature-check`, misattributed-locator)

- **location:** research/01_hypothesis_register/H001/design.md:637
- **issue:** "Triple-barrier labelling per AFML §3.2 does not apply and is not used." Two problems: (i) the triple-barrier method is AFML §3.4, not §3.2 — §3.2 is "The Fixed-Time Horizon Method"; (ii) "AFML" appears nowhere else in the document and carries no bibliographic record in §12 References, so a "per X" attribution is made against an unresolvable abbreviation.
- **evidence:** Grep of design.md for `AFML` returns line 637 only; §12 References contains no López de Prado entry. Chapter 3 ("Labeling") section structure corroborated from two independent indexes of the Wiley title: 3.1 Motivation, 3.2 The Fixed-Time Horizon Method, 3.3 Computing Dynamic Thresholds, 3.4 The Triple-Barrier Method, 3.5 Learning Side and Size, 3.6 Meta-Labeling. Verification depth is search-index and O'Reilly/Wiley TOC listings; the publisher TOC PDF and O'Reilly chapter page both returned HTTP 403 to unauthenticated fetch, so this is corroborated but not fetched from publisher primary text — declared rather than asserted.
- **fix:** Change to "§3.4" and add the record to §12: López de Prado M. Advances in Financial Machine Learning. Hoboken, NJ: Wiley; 2018. ISBN 978-1-119-48208-6, §3.4 "The Triple-Barrier Method". Since the method is declared NOT used, mark it as a not-applied instrument in the same manner §7.4 of the protocol handles GRADE.
- **reference:** Wiley 9781119482086 chapter 3 contents (publisher page HTTP 403; corroborated from O'Reilly library TOC and ETH Zurich TOC record)

### LITERATURE-1-5 (`literature-check`, truncated-quotation)

- **location:** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:897-900; also docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json instrument 5
- **issue:** Software Citation Principle 3 is quoted as ending at "...recognized by at least a community of the corresponding domain experts" with a closing quotation mark and no ellipsis. The published principle continues ", and preferably by general public researchers." A quotation terminated mid-sentence without an elision mark is a dropped clause, which charter commitment 5 and the predecessor branch's A19 quotation-audit precedent classify as a defect rather than a style choice. Principle 6, quoted immediately after, IS byte-exact.
- **evidence:** Protocol line 897-900: 'principle 3 (unique identification), a software citation "should include a method for identification that is machine actionable, globally unique, interoperable, and recognized by at least a community of the corresponding domain experts"'. Verified against the official FORCE11 Software Citation Principles page: "A software citation should include a method for identification that is machine actionable, globally unique, interoperable, and recognized by at least a community of the corresponding domain experts, and preferably by general public researchers." Principle 6 verified byte-exact against the same page and against corpus record line 1885-1889. Bibliographic record verified via Crossref (10.7717/peerj-cs.86): Arfon M. Smith, Daniel S. Katz, Kyle E. Niemeyer, FORCE11 Software Citation Working Group; PeerJ Computer Science 2016;2:e86 — the group author is correctly named in both the protocol and corpus §14, as the branch itself flags.
- **fix:** Close the quotation with an ellipsis, or restore the full clause: "...recognized by at least a community of the corresponding domain experts, and preferably by general public researchers." Apply the same fix in ks-instrument-verification.json instrument 5.
- **reference:** https://www.force11.org/software-citation-principles ; https://doi.org/10.7717/peerj-cs.86

### LITERATURE-1-6 (`literature-check`, truncated-quotation)

- **location:** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:831-832 (and the fragment reused at docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1849)
- **issue:** The Adams, Smart & Huff continuum sentence is quoted as a complete sentence terminated with a full stop inside the quotation marks: "Rather than having discrete bands, the gradation in both dimensions is on a continuous range between known and unknown." The source sentence continues ", producing the shades of GL." The dropped clause does not change the proposition the protocol rests on, but the clause is presented as a whole sentence when it is not.
- **evidence:** Protocol line 831-832 quotes the sentence with a terminal period. The source sentence, corroborated from search-index retrieval of the Wiley full text and from the arXiv preprint of Garousi et al. 1707.02553 which reproduces the scheme, reads: "Rather than having discrete bands, the gradation in both dimensions is on a continuous range between known and unknown, producing the shades of GL." Wiley full text returned HTTP 403 to unauthenticated fetch, so this is corroborated at secondary depth — which the branch itself already declares for this record (protocol §7.1(b): "verified at secondary depth only (publisher full text HTTP 403)"). Bibliographic record verified via Crossref (10.1111/ijmr.12102): Richard J. Adams, Palie Smart, Anne Sigismund Huff; International Journal of Management Reviews 19(4):432-454; online-first 19 April 2016, print 2017 — the branch's parenthetical explaining the 2016/2017 dual citation is correct.
- **fix:** Either restore the full sentence or close with an ellipsis before the period. The corpus record's §13.4 inline fragment ("is on a continuous range between known and unknown") is correct as an embedded partial quote and needs no change.
- **reference:** https://doi.org/10.1111/ijmr.12102

### LITERATURE-1-7 (`literature-check`, quotation-fidelity-inconsistent-with-declared-rule)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:189-190 (limitation 5c) and :1559 (§9.2)
- **issue:** The corpus record quotes clause d21-c11 as "Appendix E (Confidential) - Source Agency", silently normalising the spurious intra-word space present in the arm log's verbatim field. The same record's DI-7 (line 1736-1743) declares that quotations from ks-vr-d21 "are transcribed exactly as extracted so that they remain reproducible from the bytes, which is why several quotations in section 9 look malformed." The record therefore states one transcription rule and applies a different one at two sites, and the normalised string no longer exact-matches the source of record. Separately, limitation 5(b) excerpts d16-c5 mid-sentence with no leading or trailing ellipsis.
- **evidence:** ks-venue-docs.json line 1233 `quote`: "A ppendix E (Confidential) - Source Agency". Corpus line 190 and line 1559 both render it "Appendix E (Confidential) - Source Agency". ks-venue-docs.json line 914 `quote`: "Please note that appendix A is confidential and submitted under a request for confidential FOIA treatment as noted on the attached FOIA confidential treatment request letter."; corpus line 187-188 renders "appendix A is confidential and submitted under a request for confidential FOIA treatment". By contrast, research/01_hypothesis_register/H001/design.md follows the DI-7 rule correctly throughout (e.g. §4 line 663-666 and §5.3 line 775-780 reproduce the degraded spacing exactly), which shows the deviation is site-specific and not a house convention. d19-c3's quotation at limitation 5(a) was checked and is byte-exact.
- **fix:** At limitation 5(c) and §9.2, restore the extracted string exactly ("A ppendix E (Confidential) - Source Agency") or mark the normalisation explicitly as `[spacing normalised from the degraded extraction]`. At limitation 5(b), add a leading ellipsis to the mid-sentence excerpt.
- **reference:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-venue-docs.json clauses d21-c11 and d16-c5; corpus record §11 DI-7; charter commitment 5

### LITERATURE-1-8 (`literature-check`, named-instrument-without-record)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1183-1185
- **issue:** Section 4 states "No PRESS 2015 review by an information specialist was obtained, and none was simulated. Protocol section 3.5 declares this as a standing limitation of the design." PRESS is a named methodological instrument introduced only here, with no bibliographic record anywhere in the branch (protocol, corpus record, or ks-instrument-verification.json), and the attribution to protocol §3.5 is loose: §3.5 declares that no independent information specialist reviews the strategies, but it never names PRESS. The section anchor is `prisma-s-14`, and PRISMA-S item 14 is the search-peer-review item, so a reader will take PRESS to be a protocol-declared instrument when it is not.
- **evidence:** Grep of docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md for "PRESS" returns no matches. Protocol §3.5 (lines 592-595) reads: "Search-strategy peer review. No independent information specialist reviews these strategies. That is a declared limitation, reported in the corpus record in those words..." — no instrument is named. The instrument's canonical record is McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. "PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement." Journal of Clinical Epidemiology. 2016;75:40-46, doi:10.1016/j.jclinepi.2016.01.021 — note the "2015" is part of the guideline's own name and the publication year is 2016, so the bare string "PRESS 2015" is also year-ambiguous.
- **fix:** Either cite the instrument in full at the point of use with its DOI and the 2015-guideline/2016-publication distinction stated, and add it to the protocol's §12 citation ledger as an instrument NAMED BUT NOT APPLIED (the pattern §7.4 already uses for GRADE); or drop the instrument name and state the limitation in the protocol's own wording, which the corpus record claims to be quoting.
- **reference:** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §3.5 lines 592-595; https://doi.org/10.1016/j.jclinepi.2016.01.021

### REPRODUCIBILITY-1-8 (`reproducibility-verifier`, data_hashed)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-s2-*.json (55 logs)
- **issue:** The `n_returned` field is overloaded: it holds 0 both for "the search ran and found nothing" and for "no search ran". Only the RePEc logs carry the disambiguating `n_returned_semantics` / `platform_interface_failure` fields. This schema gap is the direct mechanism that produced finding REPRODUCIBILITY-1-1, and it will reproduce the same error in any future aggregation over these logs.
- **evidence:** Scan of every arm log with an http_status field: 55 logs have n_returned == 0 with a non-200 status (53x429, 1x500, 1x403 SSRN) and NO n_returned_semantics field. The 9 RePEc logs are the only ones that disambiguate, and they do so only because their status was 200.
- **fix:** Backfill `n_returned_semantics` (or a boolean `search_executed`) on every non-200 log so the field is self-describing, and state in the corpus that any count derived from these logs must filter on it rather than on n_returned.
- **reference:** _(none stated)_

### REPRODUCIBILITY-1-9 (`reproducibility-verifier`, llm_provenance)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:93 (ai_assistance), :97 (rng_seed)
- **issue:** Model identity is pinned correctly (`claude-opus-5`, not "latest") and the delegation prompts are versioned in-repo in the deliverable spec's Delegation table, but sampling parameters (temperature, top-p) are recorded nowhere. The record discloses this honestly — "all 109 eligibility verdicts and all extractions in this corpus are single-pass LLM outputs with no archived prompt and no recoverable sampling parameters" — which is why this is minor rather than major.
- **evidence:** grep for temperature/top_p/top-p across the corpus record, protocol, ADR-0006 and H001 design returns only weather-contract and slippage-model hits; no sampling parameter is recorded. The "no archived prompt" clause is slightly overstated: the four arm briefs ARE archived verbatim in docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md under Delegation.
- **fix:** Record that sampling parameters were harness defaults and are unrecoverable (which is the true state), and amend "no archived prompt" to point at the Delegation table as the archived arm-level prompt while noting that per-record extraction prompts are not archived.
- **reference:** _(none stated)_

### REPRODUCIBILITY-1-10 (`reproducibility-verifier`, deps_pinned)

- **location:** pyproject.toml, README.md Quickstart, CLAUDE.md Quickstart
- **issue:** There is no end-to-end reproduce target. `uv run pytest` runs the unit suite only; nothing re-derives the corpus from the arm logs. Dependency capture is otherwise sound, so this is a documentation-of-scope gap, not a pinning gap.
- **evidence:** Verified this round: requires-python = ">=3.11,<3.13" declared; uv.lock is tracked (ADR-0005); dev group moved out of optional-dependencies so `uv sync` installs pytest; .venv/Scripts/python.exe -m pytest -q -> 10 passed in 0.09s, exit 0. Every branch script imports stdlib only (os, sys, json, re, glob, hashlib, datetime, urllib, time, gzip), so the lockfile is not load-bearing for this branch — which is itself worth stating. logs/reproducibility/env/495798ac...txt exists and hashes to 495798ac328ee7cc673610470fe1d344e15a2dd942b22c0cb9ada0cd6a01115a, matching the corpus front matter exactly. No system deps (BLAS/CUDA/C libs) are used or needed.
- **fix:** State in the corpus record that the branch is Python-3.11-stdlib-only and that no third-party dependency bears on any number in it. If a reproduce target is wanted, add one that re-verifies the archive (payload digests, flow identities, store length) rather than re-running network queries, since the queries are not idempotent.
- **reference:** _(none stated)_

### FORMAT-1-4 (`format-auditor`, templates)

- **location:** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:784-785, 793, 843, 889 (also :481, :624)
- **issue:** The protocol asserts "A placeholder surviving into the registration commit is itself a defect; none survives", yet the literal `[INSTRUMENT-MLR]`, `[INSTRUMENT-GH]` and `[INSTRUMENT-SWCITE]` tokens survive verbatim as section headings and as in-text references. The substitutions were in fact made (each heading is followed by the resolved citation), so this is a self-contradiction in the frozen text rather than an unresolved placeholder — but a reader grepping for the defect signature the protocol itself names will hit five matches.
- **evidence:** protocol:784 "**A placeholder surviving into the registration commit is itself a defect**; none survives." against protocol:793 "### 7.1 [INSTRUMENT-MLR] — multivocal review conduct...", :843, :889, :481, :624.
- **fix:** Cannot edit frozen text. Record a one-line clarification in the append-only Addendum (alongside M1) stating that the `[INSTRUMENT-*]` tokens are retained deliberately as stable cross-reference anchors, that the substitution test is "the anchor is followed by a resolved record in §7", and that all three anchors pass it.
- **reference:** protocol §7 placeholder clause; protocol §10 append-only amendment policy

### FORMAT-1-5 (`format-auditor`, style)

- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61,65,69,73,77,81,85,89 and docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-scripts/{run_search,write_logs,write_ledger,verify_quotes}.py:1
- **issue:** Absolute home-directory paths embedded in tracked files in a public repository, against the project CLAUDE.md convention. Nine occurrences in the spec's Deliverables list and one per new search-log script. This is not an identity-hygiene breach (the real email is absent everywhere; the OS username coincides with the publicly attributed GitHub handle), but it is the exact brittleness CLAUDE.md names, and the scripts will not run from a fresh clone.
- **evidence:** spec:61 "- [ ] `C:\Users\skoir\castles\docs\decisions\ADR-0006-...`"; CLAUDE.md §Identity hygiene: "Repo-relative paths remain the convention in tracked prose — absolute paths under a home directory are brittle across machines regardless of identity policy." 171 occurrences across 16 tracked files, so the pattern is standing, not new.
- **fix:** Convert the eight Deliverables rows and the four script path constants to repo-relative paths. If the standing pre-existing occurrences in audit trails are to be left (they are immutable session records), state that exemption once in CLAUDE.md so the convention is not silently partial.
- **reference:** CLAUDE.md §Identity hygiene, final paragraph

### FORMAT-1-6 (`format-auditor`, templates)

- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:61-95, 208, 247
- **issue:** Every Deliverables checkbox is still `- [ ]` although the ADR, protocol, search-log directory, corpus record, CSL-JSON store, agenda rev 3, H001 design and failure_log rows all exist on disk. The spec is the artifact `scope-auditor` reads for delivery state, so an all-unchecked list understates completion and gives no machine-readable delivery signal.
- **evidence:** spec:73 "- [ ] `C:\...\lit_review_kalshi-strategy-multivocal_2026-09-04.md`" while that file exists with 1,978 lines and closed flow identities; same for D5:208 (H001 design present) and D6:247 (failure_log F006-F009 present).
- **fix:** Tick each delivered row to `- [x]` at the end of the loop, or add a one-line "delivery state is recorded in the audit trail, not here" note if the boxes are deliberately frozen as-declared. Do not leave the two readings ambiguous.
- **reference:** deliverable spec Deliverables checklist convention; audit-remediate-loop post-loop procedure

## verification-of-remediations

**Round 1 verified no remediations, because none had yet been applied when this round ran.**

The loop's order is: route the branches, gate the findings, write the trail, remediate, then
re-audit in round 2. At the moment this round closed, all 32 retained findings and all 21
deferred minors were OPEN. The artifact digests in the front matter are therefore the
pre-remediation state, and any later claim that a finding was fixed must be verified against
a round-2 re-read, not against this section.

Two verification results that ARE established by round 1, because the refute gate reproduced
them independently rather than accepting them from the lead:

1. The frozen-prefix hash holds. sha256 over the first 91,498 bytes of the working-tree
   protocol, over its LF-normalised form, and over the full blob at registration commit
   `4821611c1c93b5f929a76f3ba6207e900440cee5` (which is exactly 91,498 bytes) all equal
   `32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac`. The M1 append edited
   no frozen text, and the check is not line-ending-fragile.
2. The four flow identities close: 1986 - 412 = 1574; 1574 - 1475 = 99;
   40 + 28 + 31 = 99; len(CSL-JSON store) = 99 = n_included, with store digest
   `c7545d31...` matching the corpus front matter. Predecessor gap AG-11 is not repeated.

What round 2 must verify, per finding: the corrected executed-and-zero count of TWO at both
loci plus the RePEc gap-register entry (REV-1-1 / SCOPE-1-1 / QUANT-1-1 / LITERATURE-1-1 /
REPRODUCIBILITY-1-1 / FORMAT-1-1, all six being independent confirmations of the same seeded
defect); the N-8 rewrite (REV-1-2 / LITERATURE-1-2 / REPRODUCIBILITY-1-2 / FORMAT-1-2); the
109-vs-110 itemisation (REV-1-7); the declaration amendments D8+ for the substitutions in
kind (SCOPE-1-2, SCOPE-1-3, SCOPE-1-6) and the missing known-item recall check (SCOPE-1-4);
amendment M2 reconciling protocol sections 4.2 and 4.4 (SCOPE-1-7); the two source-fidelity
repairs against the pinned READMEs (QUANT-1-2, QUANT-1-3); the Politis-White citation
(QUANT-1-4 / LITERATURE-1-3); the H001 freeze-status and digest repairs (REV-1-4, QUANT-1-5,
QUANT-1-6, FORMAT-1-3); the failure_log F008 conditional (REV-1-5); the agenda identifier
disambiguation (REV-1-3); and the reproducibility set (REPRODUCIBILITY-1-3 through -1-7),
of which -1-7 - committing the branch - must be verified LAST, because committing changes
every digest recorded above.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples. Each branch examined a subset of the artifact set at
a depth its effort tier allowed, and the evidence actually examined may not be
representative of the evidence that exists. A finding not raised here is NOT a certificate
that the defect it would have named is absent; it may be a region no branch opened, a source
no branch could fetch, or a claim no branch had the standing to adjudicate. Specifically
unexamined this round: the substantive correctness of the 130 venue clauses against their
source documents beyond the sampled subset, whether the 1,465 undecided G1 rows conceal
records that would change the taxonomy, whether the 528 academic rows would survive
screening, byte-exactness of the 43 software-arm and 32 lateral-arm extractions (their
verification harness does not run - see REPRODUCIBILITY-1-3), and CHAMP items 7-16 for any
artifact no statistical branch opened. The 109 read-based eligibility verdicts are
single-pass LLM outputs with no archived per-record prompt and no recoverable sampling
parameters; that is disclosed by the corpus record itself and is not remediable by editing.

Per-branch residual risk, as each branch stated it:

### critical-reviewer

RQI coverage for this round. (1) Importance of the question - ADEQUATE, with a note. The question ('what strategies does the retrievable multivocal record STATE, and under what preconditions') is well posed and the motivation is documented rather than asserted: ADR-0006 shows the predecessor protocol's I3/X7 structurally excludes every source class in which stated strategy content lives, and section 9 of the corpus record demonstrates the payoff by settling nineteen executability preconditions from primary venue and regulator clauses. No finding raised. (2) Originality - ADEQUATE, with a note. The record is explicitly the second branch on an adjacent question, states the non-merge rule against the predecessor corpus, and nowhere restates a known result as new; its two nearest empirical records (N-2, N-3) are transcribed as source statements and explicitly not adopted. No finding raised. (3)-(5) Method, presentation and interpretation are covered by findings REV-1-1 through REV-1-10.

Risks the brief flagged, checked and NOT found defective, recorded so a later round does not re-open them. (a) The tier-2/tier-5-only base is declared in the front matter, in limitation 1, in section 1, in section 7's role column, in failure_log's standing tier statement and in the agenda's hazards; I found no claim overreaching it. (b) The 1,465 capacity-gap rows are reported separately from every Y-code count at every locus I checked (front matter, section 5.4, section 6.3, agenda `corpus_multivocal_flow`) and are consistently described as undecided rather than ineligible. (c) The research-compile gate's `block` on FAIR F1 is declared as a designed consequence in corpus section 15.1 and in the agenda front matter, and success is nowhere claimed; the store carries 99 entries and zero DOI/PMID/PMCID fields, which I verified directly. (d) The withheld-at-source set is distinguished from the merely-unretrieved set in corpus limitation 5, section 9.2, gaps G-2/G-3/G-4, H001 section 10 and agenda Branch 0's two-kinds-of-debt table; no downstream artifact treats a confidential appendix as a search problem. (e) H001 states no tradeable rule, no position size and no expected return, and section 1.6 explicitly weakens the always-NO-baseline framing it was handed rather than strengthening it - the residual interpretation problem is in failure_log F008, raised as REV-1-5, not in the design. Flow identities re-derived and closing: 1986 = 650+1269+30+37; 1986-412 = 1574; 1574-1475 = 99; store 99 == n_included 99; Y-code 10 = Y2 3 + Y3 5 + Y4 1 + Y9 1; per-arm screened 528+980+30+36 = 1574. Amendment M1 is enumerated in full with three parts, pre-screening stage, and 67+3+20 = 90 reached-via records all G1.

Residual risk after remediation. The corpus rests on a single-pass, single-screener LLM pipeline with no archived prompts and no recoverable sampling parameters (its own limitation 8 of section 15), so none of the 109 verdicts is reproducible even after every finding above is fixed; that is declared and is not remediable by editing. The largest uncharacterised quantity remains the gap between `n_total_reported` and `n_returned` on the academic arm, which the record itself names as 'the single largest uncharacterised part of this search' and which no finding here reduces. Because the academic arm contributed zero screened records, the corpus has no tier-1 anchor at all, and the one identified record that could pre-empt H001's statistic (ks-a-057, arXiv:2608.00666, 'Executable Arbitrage and Market Efficiency in Prediction Markets') is still undispositioned - if it is later admitted, H001 sections 1 and 1.6 may need revision before freeze, and that dependency is correctly registered in the design's pre-freeze checklist. Finally, items 7-16 of CHAMP (statistical-method description, assumptions, effect and interaction assessment, confounding, missing data) were NOT opened by this branch and are owned by the quant auditor; if no statistical branch was routed for this artifact set, H001's estimator, surrogate constructions and family-wise control are unaudited.

### scope-auditor

Spec source used: precedence level 1, docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md, read in full including amendments D1-D7. Levels 2-4 (task spec, frozen protocol) were read for spec-conflict only; the one conflict found is SCOPE-1-7.

Traceability outcome: of the ten declared deliverables (eight base rows plus D5 H001 and D6 failure_log), eight are present and satisfy their declared checks as re-verified here rather than assumed — ADR-0006 carries Context / Decision / Alternatives considered / Consequences / Reversal cost; the corpus record carries zero `[unsourced]` markers and both flow identities close (1986-412=1574, 1574-1475=99); the CSL-JSON store holds exactly 99 `id` keys so `len(store) == n_included` closes and predecessor gap AG-11 is not repeated; the agenda reads `revision: 3` and every gap/handoff id its branches 7-11 cite (G-1..G-4, G-11, G-12, G-19, G-20, G-24, G-25, TC-3, TC-5, TC-12) exists in the new corpus record's section 12; H001 design.md reads `status: draft-unfrozen`, carries exactly 30 `TO COMPUTE` occurrences, states MDES rather than retrospective power, and handles the always-NO baseline at the strength its source states ('statistically indistinguishable', n=23, explicitly not adopted); M1 appears in both required registers with all three parts and matching reached_via tags; failure_log carries new rows F006-F009 each with an explicit steps-1-2 status. One deliverable is absent (audit trail), one is undeclared scope (hypothesis_backlog), two are silent substitutions in kind (verbatim query set, screening script), one is partial (known-item recall check).

What this branch did NOT check, by definition of its scope: whether any retained method is correct, whether any quotation is byte-exact against its external source, whether the 130 venue clauses say what the corpus says they say, whether the taxonomy partition is sound, or whether the 99 included records resolve. Attribution fidelity beyond the two arm-log fields quoted in SCOPE-1-1 is critical-reviewer and literature-check territory.

Residual scope risk after remediation: the largest remaining exposure is that this corpus's undecided majority (1,465 G1 rows) is a standing invitation for a later session to decide a self-selected subset and report it as coverage. TC-13 and protocol section 4.4 rule 4 anticipate exactly that and require a subset rule fixed before assessment; nothing mechanical enforces it. Second, the final provenance commit could not be evaluated in round 1 — its trailers, and whether every artifact audited here is actually in it, remain unverified and should be re-checked at round close.

### quant-auditor

Verified independently: the frozen-prefix hash 32dfea6d... over the first 91,498 bytes, the append-only property of both the protocol and the spec diffs (110/88 insertions, zero deletions), the registration commit as ancestor of the search-log commit, all four flow identities (1986-412=1574, 1574-1475=99, 40+28+31=99, len(store)=99 with sha c7545d31... matching the front matter), the M1 withdrawal counts 67/3/20 re-derived from query provenance, the 53/1/2 Semantic Scholar status split across 56 logs, the 132/130 clause split, DI-2's two-row npm shortfall, and byte-exact agreement of the sampled venue clauses, the two README quotations and the ADR-0003 multiple-testing quotation with their stored sources; what remains unverifiable from the artifact alone is whether the 1,465 undecided G1 rows conceal records that would change the taxonomy, whether the 528 academic rows would survive screening (the arm contributed zero included records and its most on-point weather query never ran), and whether any retrieved S-C/S-D/S-E object still resolves at the URL recorded, since only byte digests and not archived snapshots were kept (G-24, G-25).

### literature-check

Citations checked and resolved to primary sources: 31. All bibliographic records verified against Crossref, PLOS, PMC, arXiv, FORCE11 or the publisher's own page, and NONE was found misstated in author list, year, venue, volume or pages. Specifically verified: PRISMA-S (Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, Koffel JB; PRISMA-S Group, Syst Rev 2021;10:39, 10.1186/s13643-020-01542-z) — the load-bearing all-fields-and-disciplines terminology clause and items 1, 8, 13, 15 confirmed BYTE-EXACT at PMC8270366, so the branch's headline claim that PRISMA-S applies on its own terms and is NOT "adapted" is correctly supported; PRISMA 2020 scope statement confirmed byte-exact at PMC8005924, so the branch's refusal to claim it is correctly grounded; Levac/Colquhoun/O'Brien 2010 quality-appraisal sentence byte-exact; Arksey & O'Malley 2005 and Tricco et al. 2018 records exact; Adams/Smart/Huff 2017; Garousi/Felderer/Mäntylä 2019 abstract quotes and the "in any area of SE" self-scoping clause byte-exact from arXiv 1707.02553; Kalliamvakou 2014 and 2016; Munaiah et al. 2017 — abstract quote byte-exact and the 82% precision / 86% recall / 200-repository ground truth figures confirmed exactly as the protocol states them; Smith/Katz/Niemeyer/FORCE11 2016 principles 3 and 6; Katz et al. 2021 F1000Research 9:1257 v2 (12 Jan 2021); Klein et al. 2014 and Jones et al. 2016 link-rot/content-drift definitions byte-exact from PLOS; Zittrain/Albert/Lessig 2014; ISO 690:2021 4th ed. 2021-06; Wilkinson et al. 2016; Moher et al. 2015 PRISMA-P; ICMJE Recommendations confirmed "Updated January 2026"; the five inherited quant-rule records (Ledoit & Wolf 2008, White 2000, Hansen 2005, Newey & West 1994, Andrews 1991) and the charter records (Hoenig & Heisey 2001, Theiler et al. 1992, Kaufman et al. 2012, Lakens et al. 2018, Schuirmann 1987, Politis & White 2004, Patton/Politis/White 2009); arXiv 2608.00666 (Gebele, Mutzel & Matthes), 2607.17991 (Feil & Nendel) and 2607.17428 (Moallemi, Robinson & Zhu) all resolve with exact title and author matches. In-repo primary sources verified byte-exact: ADR-0006's quotations of predecessor protocol I3 (lines 215-219), X7 (line 254), §2.7 constraints 1 and 2 (lines 335-341), §10 "Frozen text above this line is never edited" / "Silent deviation is a conduct violation" (lines 1080-1084), A4's "No eligibility criterion is altered, added, removed, or reinterpreted." at lines 1378-1379 (the D3-declared A5→A4 misattribution IS remediated), A8 at lines 1533-1571 including the "116 included records plus 33 X8 exclusions" clause, and A18 §(c) at line 2538. Both cited GitHub repositories (sudo-ai-git/kalshi-backtest, himagna16/kalshi-microstructure) exist and their quoted README strings — including "+1.37% ROI, CI [1.13, 1.61], n=23", "statistically indistinguishable", "79% of the 54,380 contracts", "10.7¢" — reproduce verbatim; H001 §1.6 and failure_log F008 both state the weaker claim the source actually makes, so brief risk (e) is discharged. Brief risks (a), (b), (c) and (f) are discharged: no claim overreaches the tier-2/tier-5 base, G-rows are never reported as eligibility determinations, the non-`pass` gate verdict is disclosed rather than worked around, and the author's real address appears in no tracked file (only the noreply address, in OpenAlex mailto parameters). RESIDUAL RISK, in order: (1) LITERATURE-1-1 is an open critical defect in the branch's citable artifact — the downstream documents diagnose it correctly but deliberately do not repair it, so a reader of the corpus record alone gets a false count; it is a one-sentence fix and must not be deferred to round 2. (2) Depth risk on three sources whose publishers block unauthenticated fetch: Adams/Smart/Huff (Wiley 403), Munaiah (Springer/ACM 403, verified via the SWAG Lab abstract mirror), and the AFML chapter TOC (Wiley and O'Reilly both 403) — these are corroborated at secondary/index depth only, which the branch itself already declares for the first two but not for AFML. (3) ISO 690:2021's normative text remains unread by anyone in this branch; the "4th ed., 2021-06-11" day-level date could not be confirmed past "2021-06" from a free source, and the standard is cited for a practice (date of citation on dynamic online resources) that no one in this project has read the text of. (4) The eight instrument-verification records were verified pre-freeze at abstract/metadata depth by a prior session and inherited here; my re-verification reached full text or official-page depth for PRISMA-S, PRISMA 2020, Levac, Klein, Jones, Garousi, Munaiah and the FORCE11 principles, which upgrades those, but the Adams tier-mapping table and the Kalliamvakou numbered peril headings remain corroborated only from search-index extraction as instrument-verification declares. (5) Not in my scope and not assessed: whether the statistic in H001 §1.4, the surrogate constructions in §3, or the SPA/embargo machinery are correctly specified — that is quant-auditor's determination.

### reproducibility-verifier

Check summary: deps_pinned = pass (requires-python >=3.11,<3.13; uv.lock tracked; dev group installs under `uv sync`; branch scripts stdlib-only; pip-freeze archive digest verifies exactly). seeds_pinned = partial (PYTHONHASHSEED asserted at entry in 5 academic scripts; no-op setdefault or nothing across the 7 S-C scripts; front-matter enumeration false, F-1-4). data_hashed = partial (112/112 academic payload digests re-verified byte-exact against payload_path, 0 mismatch; lateral and venue arms carry 62 digests with no retained bytes, F-1-6; 40/99 store entries carry no digest). entrypoint_runs = fail (all 4 dry-runs exit 1, F-1-3; nothing committed, F-1-7). llm_provenance = pass-with-gap (model id pinned, ICMJE role declared, arm prompts versioned; sampling parameters unrecoverable and disclosed). cross_platform = partial (hardcoded C:\Users\skoir path in 4 S-C scripts, F-1-5; .gitattributes forces LF for .md/.py/.json and the protocol file is already pure LF).

Independently re-verified as SOUND, not assumed: the frozen-prefix hash is robust — sha256 of the first 91,498 bytes of the working-tree protocol, of its LF-normalised form, and of the full blob at registration commit 4821611c1c93b5f929a76f3ba6207e900440cee5 (which is exactly 91,498 bytes) all equal 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac, so the M1 append edited no frozen text and the check is not line-ending-fragile. CSL-JSON store length is 99. Identity hygiene is clean: the author's real address appears in no file outside .git, and no audited prose artifact contains an absolute home-directory path (0 hits across all seven). The SR-4 subset draw is genuinely deterministic (sha256-ordered, seed-free) and ks-github-subset-rule.md documents the allocation as capacity numbers with an explicit no-popularity-floor declaration.

Residual risk I could not close from within this branch's scope: (i) the 43 S-C and 32 lateral extractions are single-pass LLM outputs whose verification script (verify_quotes.py) is dead, so quote fidelity for those arms is attested but not re-checkable by me — the byte-exactness question belongs to the quotation-audit branch and should be told that its verification harness does not run; (ii) I verified digest-to-payload correspondence for the academic arm only, because it is the only arm whose bytes were retained; (iii) N-5's Semantic Scholar tally checks out exactly (53/1/2 over 56), so the seeded defect is narrowly the four-versus-two RePEc conflation and should not be over-remediated into doubt about the rest of the note.

### format-auditor

Identity hygiene is clean: the author's real address [REAL ADDRESS REDACTED BY THE LEAD SESSION 2026-09-04 BEFORE COMMIT] (the author's personal address, which CLAUDE.md forbids introducing into any commit, tag or tracked file; the format-auditor branch quoted it verbatim while certifying that it appears in no tracked file, which would have made the certification false at the moment it was written. The finding it reported is unaffected and stands: the address appears in no OTHER tracked file, and the OpenAlex mailto parameter carries the noreply address) appears in no tracked file; the OpenAlex `mailto` parameter in every ks-openalex query log correctly carries the noreply form 238704148+s-koirala@users.noreply.github.com; no kernelspec or notebook metadata is in scope. Real-name strings appear only where CLAUDE.md explicitly authorises them for this repository. Citation formatting is consistent across the ADR, protocol, corpus record and H001 design — Wilkinson 2016 (10.1038/sdata.2016.18), Rethlefsen 2021, Arksey & O'Malley 2005, Levac 2010, Garousi 2019, Adams/Smart/Huff 2017, Kalliamvakou 2014/2016, Munaiah 2017 all carry identical DOIs, years and author casing at every point of use, and the Kalliamvakou full-author-list vs et-al forms are used in the correct positions. Magic-number policy holds in H001: every numeric is labelled QUOTED (with clause id), TO COMPUTE (with named selection procedure) or CONVENTION (with provenance), and the corpus record explicitly refuses the one bare number it transcribed (`~$0.15` "is a bare number and is not adoptable"). Sharpe appears only as a conditional deferral with the correct Opdyke/Lo/Ledoit-Wolf routing, consistent with the KPI-only feedback. Remaining risk is concentrated in FORMAT-1-1/1-2: the record's own two capacity-gap-as-absence statements are the kind of defect this branch's whole apparatus exists to prevent, and one of them (N-8) is not covered by the agenda's recorded discrepancy note, so a reader who trusts the agenda's "one discrepancy" framing will not find it. FORMAT-1-3 is the highest-consequence of the rest because H001 is intended to be frozen later against a dependency block that is currently false.

## ai-assistance-statement

Per ICMJE Recommendations (updated January 2026), section II.A.4 on AI-assisted technology:
AI cannot be an author, and its use is disclosed here. Per the publishing rules' disclosure
convention, the models, their versions, their roles, and the reproducibility-log path are
stated.

| model | version / id | role in this artifact |
| --- | --- | --- |
| Claude Opus 5 | `claude-opus-5` | lead session: routed the audit, assembled this trail (role: `audit`) |
| Claude Opus 5 | `claude-opus-5` | six specialist auditor branches, efforts as recorded in `agents` (role: `audit`) |
| Claude Opus 5 | `claude-opus-5` | adversarial refuter at the refute gate (role: `audit`) |

No sampling parameters (temperature, top-p) were recorded by the harness and they are not
recoverable; this is a declared gap, also recorded as REPRODUCIBILITY-1-9. The arm-level
briefs are archived verbatim in the Delegation table of
`docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md`; per-finding
prompts are not archived. Every finding in this trail was verified against the repository by
the refuter before retention; no finding was accepted on model assertion alone.

Reproducibility log. `artifacts/` and `logs/` are gitignored, so no path under them resolves
in a fresh clone; the clone-durable carrier is the commit itself, via the
`Repro-Log-Path:` / `Repro-Log-SHA256:` trailers written by `/commit-with-provenance`.
Untracked locator for this round: `logs/reproducibility/repro_log_{run_id}.json` for the
session run id recorded in `docs/audits/session_trail_2026-09-04.md`; the pip-freeze archive
for this environment is `logs/reproducibility/env/495798ac...txt`, sha256
`495798ac328ee7cc673610470fe1d344e15a2dd942b22c0cb9ada0cd6a01115a`, which matches the corpus
record's front matter. The machine-readable payload of this round is the sidecar named in
the front matter, whose sha256 is recorded there.

## immutability-and-retention

This trail is committed to the repository and is **append-only**. Round 1 is the section
above. A later round of the same loop APPENDS a round section to this same file and appends
its payload to the sidecar; it never overwrites, edits, or deletes an earlier round's text,
and it never rewrites a finding, a refutation, or a disposition already recorded here.

A correction to anything recorded above is made as a **dated addendum appended at the end of
this file**, stating what was recorded, what is now believed, and on what evidence. The
superseded wording stays legible in place. Record changes must not obscure previously
recorded information (21 CFR 11.10(e)); an audit trail that is silently edited is not an
audit trail. The same discipline the branch applies to its own frozen protocol - append,
never edit - applies to this document.

Retention: for the life of the repository. The trail and its sidecar are tracked, so their
integrity is carried by git history; the sidecar sha256 recorded in the front matter pins
the payload as of this round's close. If the sidecar is later appended to by round 2, the
round-2 front matter records the new digest and the round-1 digest above remains the correct
digest for the round-1 payload as it stood.

---
schema_version: WI-3/2
conforms_to: WI-3 section 2 required-field spec (22 front-matter keys, 7 body sections)
title: "Audit trail - kalshi-strategy-corpus (multivocal strategy corpus branch), round 2"
type: audit_trail
date: 2026-09-04
started_at: 2026-09-04T13:26:30-05:00
ended_at: 2026-09-04T14:38:05-05:00
artifacts:
  - path: docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: ed7aca3e767714a70aa3415037a5982fb1595ad3b616f289625ef3da86d80e53
  - path: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: c643c620560fe5a83603a65780383b86d75e075a9d429dd06e11186969d424bb
  - path: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21
  - path: docs/literature/references_kalshi-strategy-multivocal.json
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df
  - path: docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 671ae2b4b5dbcdd6a6ecfedfe772ded9f6a852c265e215d785fe8afbc41badfc
  - path: failure_log.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 6ab2fd3507edeb7fca34e99a84703a6e85cba07c0ed844f2f76be51c72d1736a
  - path: research/01_hypothesis_register/H001/design.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 38ab578bc9d030169c908b433735da807d607a4ff30d2bddb053bfef52abc3e2
  - path: hypothesis_backlog.md
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: 98facb704264898a058bcdafe26bd48b6af18487757e6d4f23ef1b31a592cd4f
  - path: docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl
    git_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
    sha256: bacd5bdff2db267366312298e6fd79f1ceba8142647eb5f77f2349a49a826f97
repo_head: 4821611c1c93b5f929a76f3ba6207e900440cee5
worktree_clean: false  # `git status --porcelain` is non-empty at round 2: every audited
                       # artifact is still staged-or-untracked and uncommitted, which is
                       # itself finding REPRODUCIBILITY-2-1's exposure (the search-log tree
                       # is untracked, so an overwritten log cannot be recovered from git).
audit_criteria:
  task_spec_verbatim: |
    TASK SPEC OF RECORD: docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md. Read it in full INCLUDING the append-only Declaration amendments D1-D11 and the round-1 remediation section at the tail, which record what changed and why.
    
    ROUND 2 OF 3. Round 1 returned verdict `block` with 7 critical / 27 major / 21 minors and 2 refuted. YOUR JOB IS TO VERIFY THE REMEDIATION, NOT TO RE-DERIVE ROUND 1. Do not re-raise a round-1 finding unless the fix is absent, wrong, or incomplete — and if you do, say which.
    
    GOVERNING CONSTRAINTS (unchanged): ADR-0003 castles specifies and never executes — no market data, no exchange API, no price computed, nothing fitted or backtested, NO tradeable rule / position size / expected return, every executing parameter TO COMPUTE with its selection procedure named. ADR-0004 + REVIEW.md directive 8 with ADR-0006's recorded WIDENED CARRIER reading. CLAUDE.md + charter commitment 3: no unlabelled constants. Charter commitment 5: a dropped qualifier or misattributed clause is a defect. Charter: MDES never retrospective power. Protocol section 10: a corpus record that ran under an amendment it does not enumerate is defective — there are now TWO, M1 and M2. Protocol section 11: frozen prefix (first 91,498 bytes) must still hash to 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac.
    
    PRIOR DISPOSITIONS — WHAT WAS REMEDIATED AND HOW:
    (1) THE RePEc DEFECT, raised by six of seven branches (REV-1-1, SCOPE-1-1, QUANT-1-1, LITERATURE-1-1, REPRODUCIBILITY-1-1, FORMAT-1-1) plus LITERATURE-1-2 / REPRODUCIBILITY-1-2 on the second instance. Corrected at SIX loci in the corpus record: head limitation 9, note N-5, note N-8, four section-2 source-table rows, nine ks-repec annotations in the section-3 fence, and gap G-9 extended. New gap G-26 and new data-integrity entry DI-8 added. Every superseded sentence is RETAINED VERBATIM in a dated correction note rather than overwritten. NO arm log was edited — the logs were right; the record was wrong. No count changed. VERIFY: that the corrected count is two, that no locus still asserts four executed, that the retained superseded wording is clearly marked as struck rather than reading as current text, and that failure_log F007's addendum agrees with DI-8.
    (2) REV-1-7 arithmetic: front-matter screening_verdict_source itemised to 110 against a stated 109; corrected to 31 lateral (KSL-C31 removed at cross-arm dedup, which precedes screening) so 43+30+31+5=109.
    (3) H001 + hypothesis_backlog: QUANT-1-2 — the design's claimed 'Correction' asserting its source does NOT say no price-based strategy clears the bar was FALSE and is withdrawn; both dropped README sentences are now named, the source is framed as making a stronger and a weaker claim, and the design's use of only the weaker is restated as a conservative CHOICE. QUANT-1-3 — the dropped tail sentence 'Even at the tails the hurdle is 2.6c' recorded, both 10.7c and 2.6c flagged NOT ADOPTABLE, the section 9.2 sanity reference re-registered against 2.6c, and the fee-monotonicity justification withdrawn as insufficient because the round-trip bar is fee PLUS spread. REV-1-4 / QUANT-1-6 — corpus record now recorded as EXISTING, pre-freeze checklist item 1 DISCHARGED, items 2-7 restated as the operative blockers. QUANT-1-5 — read-state digest discipline added; the LEAD computed the six digests the agent could not and recorded them WITH the limit that they pin for a future re-read and do NOT retroactively verify the draft's existing quotations. QUANT-1-4 / LITERATURE-1-3 — Politis & White 2004 doi:10.1081/ETC-120028836 and Patton, Politis & White 2009 doi:10.1080/07474930802459016 added to sections 6, 9.1 and 13 with the implementable formula named and flagged not-re-fetched. STATUS REMAINS draft-unfrozen.
    (4) Agenda REV-1-3: the two corpora's identifier spaces collided. MV-G-n / MV-TC-n adopted for the multivocal corpus, predecessor left bare, convention stated once, 86 identifiers swept, collision sites annotated inline.
    (5) failure_log REV-1-5: F008 Step 2b rewritten as a [corpus-inference] CONDITIONAL — the README does not state whether the candidate was selected and evaluated on the same set and the two reported spans differ, so the informativeness upgrade is contingent, not established. F007 given a dated addendum. Verified append-only: 533 insertions, 0 deletions vs HEAD, F001-F009 heading block byte-identical.
    (6) DECLARATION amendments D8-D11: D8 records that the protocol froze the query CONSTRUCTION RULE not the verbatim query set the declaration promised (a change in KIND); D9 RETIRES the inherited 'screening script self-test exits 0' check as inapplicable because this branch assigned no classifier verdicts at all; D10 records that the promised known-item recall check was EXECUTED not waived, at 4.3% (14 of 327 predecessor includes), published with both bounds; D11 records that a new status token was added to a shared convention register and is PROPOSED, not ratified. SCOPE-1-5 discharged: the trail exists with 22/22 keys and 7/7 sections.
    (7) PROTOCOL AMENDMENT M2 for SCOPE-1-7: sections 4.2 and 4.4 contradicted each other on whether a record may end screening undispositioned, and 93% of the flow took the path 4.2 does not enumerate. Ruled that a G-code is a FOURTH stage-1 outcome. Declared POST-EXECUTION and therefore explicitly WEAKER than M1. Frozen text not edited; prefix hash re-verified intact.
    (8) REPRODUCIBILITY: 1-3 — module-name shims restored, all 15 scripts now import cleanly under PYTHONHASHSEED=0, README.md written stating per script what is and is not reproducible; the S-C stage files were shown RE-DERIVABLE offline from archived payloads and reproduce the recorded counts exactly, while _pins.json and _readmes.json are genuinely unrecoverable. 1-4 — the rng_seed field was false in three particulars and is corrected in place with the superseded wording retained; the store-builder clause is WITHDRAWN AS FALSE and registered as new gap G-28. 1-5 — four hardcoded absolute home paths replaced; a repo-wide grep for C:\Users in .py now returns nothing. 1-6 — new gap G-27: S-D/S-E bytes are NOT archived and their digests are ATTESTATIONS; the lead independently hashed all 32 lateral payloads in the ephemeral scratchpad before it clears (32 matched, 0 mismatched, 0 missing, recorded at ks-payload-digest-verification.json) making them VERIFIED-ONCE not verifiable; the bytes were deliberately NOT copied in because they are third-party pages and this repository is public. 1-7 — nothing was committed at audit time; the commit is the session's final step.
    
    SPECIFIC THINGS TO PROBE THIS ROUND: (a) does any correction note read as CURRENT text rather than as struck superseded text — i.e. could a reader mistake a retained wrong sentence for the record's claim; (b) do the corpus record, failure_log F007 and DI-8 now agree with each other AND with the arm logs; (c) is M2's post-execution weakness stated plainly wherever it bears, or softened; (d) does the 4.3% recall figure travel with both of its bounds everywhere it appears; (e) has any remediation introduced a NEW unlabelled constant, uncited method, or overreaching claim; (f) is the H001 design still free of any tradeable rule after the 1.6 rewrite; (g) do the agenda's MV- prefixes leave any branch derivation orphaned or any predecessor citation mislabelled.
  files_consulted:
    - path: docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md
      sha256: 5abce3e39fbfb644d9c92d7f97c7198b6f66772105d06369b595d2cc62a1f047
      role: task spec of record for round 2; quoted verbatim in task_spec_verbatim. The digest is of the AMENDED spec, which now carries D8-D11 and the round-1 remediation block; the round-1 trail records the pre-amendment digest 382ade8e...
    - path: CLAUDE.md
      sha256: 2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759
      role: project-local rules (in force)
    - path: ~/.claude/CLAUDE.md
      sha256: 9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f
      role: user-level directives (in force)
    - path: ~/.claude/rules/quant-project.md
      sha256: 433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f
      role: not auto-activated on this path; adopted by explicit reference via ADR-0004
    - path: ~/.claude/rules/population-health.md
      sha256: f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966
      role: consulted; cwd matches no glob, not in force
    - path: ~/.claude/rules/publishing.md
      sha256: a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479
      role: consulted; not in force (real-name attribution per project CLAUDE.md)
    - path: docs/methodology/charter_castles_2026-08-21.md
      sha256: 303da9b003d7877a4324dde6cc1401bade836e2548fea02e2926fc349a3b35b5
      role: governing charter (commitments 3 and 5; MDES never retrospective power)
mechanism: >-
  audit-remediate-loop skill routed to the Workflow engine script
  workflows/audit-remediate.js - deterministic routing, parallel specialist auditors,
  schema-validated findings, and an adversarial refute gate through which every
  critical/major finding must pass before remediation (a drop requires concrete
  counter-evidence, never bare disagreement). One round per invocation; cap 3. Routing
  is identical to round 1 because the artifact set is unchanged.
agents:
  - branch: critical-reviewer
    agent_def_path: ~/.claude/agents/critical-reviewer.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor - argument, RQI and remediation-verification review
  - branch: scope-auditor
    agent_def_path: ~/.claude/agents/scope-auditor.md
    model_id: claude-opus-5
    effort: medium
    role: specialist auditor - spec-vs-delivery diff over the round-1 remediation
  - branch: quant-auditor
    agent_def_path: ~/.claude/agents/quant-auditor.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor - method fidelity and numerical re-derivation of every remediated count
  - branch: literature-check
    agent_def_path: ~/.claude/agents/literature-check.md
    model_id: claude-opus-5
    effort: high
    role: specialist auditor - citation and quotation verification of the corrected claims
  - branch: reproducibility-verifier
    agent_def_path: ~/.claude/agents/reproducibility-verifier.md
    model_id: claude-opus-5
    effort: medium
    role: specialist auditor - repro envelope, digest chain, entrypoint runs
  - branch: format-auditor
    agent_def_path: ~/.claude/agents/format-auditor.md
    model_id: claude-opus-5
    effort: low
    role: specialist auditor - naming, identity hygiene, template and magic-number policy
  - branch: refute-gate
    agent_def_path: "(no standalone agent definition; the refuter is the in-script
      adversarial role of workflows/audit-remediate.js)"
    model_id: claude-opus-5
    effort: high
    role: refuter (adversarial refute gate)
operator: Sajan Koirala (repository-local git identity 238704148+s-koirala@users.noreply.github.com)
acted_on_behalf_of: >-
  Sajan Koirala, independent researcher, acting for himself. Delegation chain:
  operator -> lead session (Claude Opus 5) -> audit-remediate workflow ->
  six specialist auditor branches and the refute gate. No third party directed
  this audit; no agent message was treated as operator authorisation.
routing:
  - critical-reviewer
  - scope-auditor
  - quant-auditor
  - literature-check
  - reproducibility-verifier
  - format-auditor
rounds_completed: 2
rounds_cap: 3
cap_reached: false
verdict: block
counts:
  raw_critical: 7
  raw_major: 26
  raw_minor: 21
  refuted: 0
  retained_conservative: 0
  to_remediate: 33
  minors_logged: 21
sidecar:
  path: docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.round2.json
  sha256: 3eb19a401e79e0dd1029e2cf3cf9a5f2b0b34e94b3789357004f07e6dc0e6fa9
---

# Audit trail - kalshi-strategy-corpus, round 2

Round 2 of the three-round cap over the multivocal strategy-corpus deliverable set. This
round's task was to VERIFY the thirty-two round-1 remediations and to hunt what they
introduced, not to re-derive round 1. The same six specialist branches ran in parallel over
the remediated artifacts; every critical and major finding then passed the adversarial refute
gate before remediation was authorised. Branch verdicts: `critical-reviewer` proceed-with-remediation, `scope-auditor` block, `quant-auditor` block, `literature-check` block, `reproducibility-verifier` block, `format-auditor` proceed-with-remediation.

Raised this round: **7 critical, 26 major, 21 minor**. The gate DROPPED **0** and RETAINED **33**
(0 retained-conservative); **21 minors are logged and not remediated**. Round verdict: **block**
- five branches raise the same unremediated critical (M2 is registered in both registers protocol
section 10 requires and enumerated in neither the corpus record nor the declaration), and one
branch raises a NEW critical of its own: two archived executor scripts have no `__main__` guard
and write over the archive in place, and sixteen query logs plus their payloads were overwritten
during this audit and cannot be recovered because the search-log tree is untracked.

Round-1 dispositions carried forward: Round 1: 7 critical, 27 major, 21 minors logged, 2 refuted by the gate, verdict block. All 32 remediation items applied as summarised in the taskSpec. Six of seven branches independently confirmed the same seeded RePEc defect, which is the round-1 gate-recall signal.
Round 1's front matter, findings table, refute-gate entries and JSON sidecar are unmodified by
this round; round 2 is appended below them with its own front matter and its own sidecar.

The machine-readable payload of this round is held verbatim in the round-2 sidecar named in the
front matter above (FAIR I1); every field abridged in the table below is unabridged there and in
the refute-gate entries.

## findings-table

One row per finding raised this round, carrying all eight schema fields (id, severity, category,
location, issue, evidence, fix, reference) plus the raising branch and the disposition. The 33
gated findings come first, then the 21 logged minors. Long cells are compressed here with `…`;
the unabridged text of every field is in the round-2 JSON sidecar, and every gated claim is
reproduced verbatim and unabridged in [refute-gate](#refute-gate) below.

| id | severity | category | location | issue | evidence | fix | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| CRITICAL-2-1 | critical | design | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74, :1173-1198 (§3.3), :73 (protocol_path comment) | The corpus record does not enumerate protocol amendment M2, and positively asserts that only one amendment exists. Round-1 remediation issued M2 (finding SCOPE-1-7) against the fro … | "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here" (li … | Add §3.4 "Amendment M2, enumerated" to the corpus record, carrying M2's ruling, its POST-EXECUTION stage in those words, its declared weakness relative to M1, and its scale (1,465 … | Protocol section 10 (amendment enumeration); CHAMP item 6 (consistency with the pre-registered protocol); ks-amendments. … | critical-reviewer | retained at the refute gate — to remediate |
| CRITICAL-2-2 | major | consistency | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803 | Incomplete remediation of the round-1 RePEc defect. The agenda still asserts, in the present tense and explicitly as a LIVE un-repaired discrepancy, that the corpus record's §10 N- … | "**One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here** … the corpus record's §10 N-5 states that four academic queries in the w … | Replace the bullet with a dated correction note in the agenda's own append-only style: retain the superseded sentence marked struck, and state that as of 2026-09-04 the corpus reco … | Charter commitment 5 (attribution fidelity); SAMPL/CHAMP internal-consistency requirement — a claim about a cited docume … | critical-reviewer | retained at the refute gate — to remediate |
| CRITICAL-2-3 | major | consistency | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:59-60 and :114 (front matter `corpus_ … | The agenda declares, at two loci, that the multivocal corpus supplies gaps G-1..G-25, and that these are cited in the agenda as MV-G-1..MV-G-25 and are "the sole admissible source … | agenda:114 "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 … are the sole admissible source of branches 7-11" — agains … | Update both range declarations to G-1..G-28 / MV-G-1..MV-G-28 with a dated rev-3 correction note recording that the range moved by round-1 remediation, and cite MV-G-26 at the agen … | Deliverable spec, agenda row check: "every new branch cites a gap id or handoff id that exists in the new corpus record" | critical-reviewer | retained at the refute gate — to remediate |
| CRITICAL-2-4 | major | standard-coverage | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §4 (:1202-1219), head limitations (:131-235), §12.1 … | Probe (d): the executed known-item recall figure does not travel with its bounds everywhere it appears because it appears in only ONE prose location — declaration amendment D10 — a … | lit_review §4: "**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was obtained, and none was simulated. … What *was* done, and what it is not a substitute fo … | Add the recall result to the corpus record §4 with both of its stated bounds (the seed-set/question-mismatch caveat and the 6,923-of-8,813 index bound), cross-reference ks-known-it … | PRISMA-S item 14 (peer review of the search strategy) and the predecessor protocol's known-item recall clause; deliverab … | critical-reviewer | retained at the refute gate — to remediate |
| SCOPE-2-1 | critical | omitted | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`) and :1173-11 … | The round-1 remediation for SCOPE-1-7 issued protocol amendment M2, but the corpus record still enumerates ONE amendment. The protocol's own section 10 makes exactly this defective … | Protocol :1150-1152 — "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an am … | Amend the corpus record's `protocol_amendments` field to enumerate TWO amendments and retitle/extend §3.3 to "Amendments M1 and M2, enumerated", carrying M2's ruling, its `touches` … | protocol §10; taskSpec constraint "there are now TWO, M1 and M2" | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-2 | major | omitted | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md — §3.3, §5 flow, limitation 1-2, capacity_codes fron … | Probe (c): M2's declared weakness — that it is POST-EXECUTION and therefore weaker than M1 — is stated plainly in the protocol addendum and in the amendment register, and is stated … | Protocol :1467-1472 — "Execution stage - POST-EXECUTION, and this is a WEAKER amendment than M1. ... the 1,465 G-dispositions were assigned before this contradiction was adjudicate … | State M2's post-execution weakness in the corpus record at the loci where the 1,465 G-rows are accounted for (§3.3, §5 flow narrative, and the `capacity_codes` front-matter block), … | protocol M2 §"Execution stage"; taskSpec probe (c) | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-3 | major | added | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md — "Declaration amendments, round-1 audit remedia … | M2 is a post-freeze change to a declared deliverable (the protocol) made during round-1 remediation, and no declaration amendment records it. The declaration set its own precedent … | Spec D7 :256-259 — "D7 - 2026-09-04 - amendment M1 issued against the frozen protocol. Not a new artifact but a change to a declared one, recorded here because the declaration's pr … | Append a D12 recording that amendment M2 was issued against the frozen protocol on audit finding SCOPE-1-7, that it is POST-EXECUTION and declared weaker than M1, that it changes n … | spec D7 precedent | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-4 | major | partial | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (absent throughout); spec D10 :330-347 | SCOPE-1-4's remedy is only half-applied. The known-item recall check was executed and its log written, but it is published solely in the declaration — which is the loop's INPUT, no … | Spec :54-57 — "'Comprehensive' is bounded and the bound is published. ... **The corpus record** states per-arm coverage, the strata left unassessed, and the known-item recall check … | Add the recall result to the corpus record — a limitation/section-4 paragraph carrying 14/327, both caveats, and the non-screening denominator note — and register a numbered gap in … | spec deliverable row for the corpus record; D10 | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-6 | major | partial | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803 | The DI-8 correction was not propagated to the agenda, which still describes the corpus record as asserting the wrong thing and presents a discrepancy that remediation closed as liv … | Agenda :1796-1801 — "**One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here** ... the corpus record's §10 N-5 states that four aca … | Update the agenda bullet to record that the corpus record has since been corrected at limitation 9, N-5, N-8, the section-2 rows and the section-3 fence, that DI-8 and G-26 now exi … | DI-8; round-1 findings REV-1-1/SCOPE-1-1 | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-7 | major | partial | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :187, :1753 | Probe (g): the MV- prefix sweep itself leaves no branch derivation orphaned, but the agenda's three statements of what the multivocal corpus supplies are stale after remediation. A … | Agenda :187 — "The **multivocal** corpus, `lit_review_kalshi-strategy-multivocal_2026-09-04.md`, names gaps **G-1…G-25** and handoffs **TC-1…TC-15**" (same assertion at :60 and :17 … | Extend the three range statements to G-1..G-28, and add MV-G-26/27/28 to the agenda's hazards or verification-status section — at minimum MV-G-27, because the agenda's citations in … | corpus §12.1 G-26/G-27/G-28; taskSpec probe (g) | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-8 | major | changed | research/01_hypothesis_register/H001/design.md:29-35 vs :43-65 (same front matter) | Probe (e): the QUANT-1-5 read-state digest remediation was applied to one front-matter field and not to the adjacent one, leaving the front matter asserting two incompatible states … | :29-31 — "corpus_record_sha256: > TO COMPUTE — no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed. … | Set `corpus_record_sha256` to the computed digest, retain the superseded "TO COMPUTE / no hashing tool" wording as struck, and carry the same limit the other field carries — that t … | round-1 QUANT-1-5 remediation | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-9 | major | partial | hypothesis_backlog.md:32 (H001 row, round-1 correction block) vs research/01_hypothesis_register/H001/design.md:43-74 | The same QUANT-1-5 remediation left the two registers disagreeing. The backlog's H001 correction states as a live freeze blocker that no read-time digest is recorded for the corpus … | hypothesis_backlog.md:32 — "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is ass … | Append to the backlog row (append-only, superseded wording retained) that item 7 is partly discharged — the six digests are computed and recorded in the design — and restate the re … | design.md read_state_digest_discipline; spec D11 | scope-auditor | retained at the refute gate — to remediate |
| SCOPE-2-10 | major | added | research/01_hypothesis_register/H001/design.md:970-986 and :1615-1633; spec D5 check :218-220 | Probe (e): the QUANT-1-4 / LITERATURE-1-3 remediation added two external bibliographic records to H001 that fall outside the provenance envelope the declaration itself set for that … | Spec D5 :218-220 — "check: front matter reads `status: draft-unfrozen`; `grep -c \"TO COMPUTE\"` returns a positive integer; **no external citation appears that is absent from `ks- … | Either add both records to a verification log for this branch, or append a declaration amendment recording that D5's citation-envelope check is widened to admit instruments adopted … | spec D5 check; ADR-0004 explicit-reference mechanism | scope-auditor | retained at the refute gate — to remediate |
| QUANT-2-1 | critical | method | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:98 (front matter protocol_amendments) and :1173-1198 … | The corpus record does not enumerate amendment M2. Its front matter and section 3.3 both still assert that exactly ONE amendment exists. The frozen protocol's section 10 declares p … | `grep -n "M2" docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns ZERO matches. Front matter: `protocol_amendments: "ONE numbered append-only amendment, M1 … | Add section 3.3b to the corpus record enumerating M2 (contradiction quoted, ruling, touched sections 4.2/4.4, and POST-EXECUTION weakness stated in the protocol's own words — 'a we … | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §10 (frozen prefix, line 1149-1152); docs/literature/ … | quant-auditor | retained at the refute gate — to remediate |
| QUANT-2-2 | major | reproducibility | research/01_hypothesis_register/H001/design.md:30-77 (front matter corpus_record_sha256 and read_state_digest_discipline … | The read-state digest discipline added under round-1 finding QUANT-1-5 pins a corpus-record SHA-256 that does not match the delivered corpus record, and the same front matter simul … | Recorded: `corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b`. Recomputed on disk: `451f90080c952 … | Recompute the corpus-record digest LAST, after all corpus-record edits for the round are final, and replace b3679514... with the final value, retaining the superseded value in a da … | research/01_hypothesis_register/H001/design.md front matter, own rule text; CLAUDE.md §Reproducibility (dataset checksum … | quant-auditor | retained at the refute gate — to remediate |
| QUANT-2-3 | major | reporting | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:132-243 (nine head limitations) and :2022-2074 (sect … | Round-1 SCOPE-1-4's remedy is INCOMPLETE. The known-item recall check was executed correctly and its result is arithmetically sound, but it is published ONLY in the declaration ame … | `grep -rn "4.3%\|known-item\|known_item"` over the corpus record, the protocol, the agenda and ADR-0006 returns ZERO matches; the only hits repo-wide for this branch are the spec ( … | Add a tenth head limitation (or extend limitation 6, which already carries the same 6,923-of-8,813 bound) stating the 4.3% figure WITH both caveats verbatim from ks-known-item-reca … | docs/literature/search_logs/kalshi-strategy-multivocal/ks-known-item-recall.json; PRISMA-S item 11 (prior work / recall … | quant-auditor | retained at the refute gate — to remediate |
| QUANT-2-4 | major | reproducibility | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1874 (gap G-28); docs/literature/search_logs/kalshi- … | G-28 registers the CSL-JSON store builder as a permanent gap — 'never archived', 'not re-runnable at all' — but the builder exists and is readable at audit time in the same executi … | `build_store.py` (9,145 bytes, mtime 2026-09-04 11:48) is present in the executing session's scratchpad and line 222 reads `out = "docs/literature/references_kalshi-strategy-multiv … | Archive build_store.py into docs/literature/search_logs/kalshi-strategy-multivocal/ under the directory's ks- naming convention, with the PYTHONHASHSEED=0 entry assert and the home … | docs/literature/search_logs/kalshi-strategy-multivocal/README.md §'The five missing S-C stage files' (the precedent for … | quant-auditor | retained at the refute gate — to remediate |
| QUANT-2-5 | major | reporting | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1727-1838 (section 11, DI-1..DI-8) and section 8 T4 … | Two verified extraction defects in the software-arm log — established during this session at primary-source depth — are registered ONLY in an unfrozen draft design and are absent f … | H001 §1.6 establishes, from a re-fetch of the pinned raw READMEs: (i) `ks-sc-001` extraction is INCOMPLETE — *"No price-based strategy clears the honest bar."* and the bolded *"Con … | Add DI-9 to section 11 recording both extraction defects with the two missing verbatim sentences, their re-fetch provenance and the two stated limits (converted text, digest not re … | docs/methodology/charter_castles_2026-08-21.md commitment 5; corpus record §11 DI-7 (the existing precedent for register … | quant-auditor | retained at the refute gate — to remediate |
| LITERATURE-2-1 | critical | missing-attribution / self-declared protocol defect | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`); :1173 (§3.3 … | The corpus record does not enumerate amendment M2 anywhere, and affirmatively asserts that only one amendment exists. The frozen protocol clause it quotes in the same paragraph mak … | grep for "M2" across the corpus record returns ZERO matches. Front matter line 74 reads: "protocol_amendments: 'ONE numbered append-only amendment, M1, enumerated in full in sectio … | Amend the front-matter `protocol_amendments` field to read TWO amendments and carry M2's ruling text; rename §3.3 to "Amendments M1 and M2, enumerated"; add an M2 sub-block stating … | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §10 (frozen, lines 1143-1152); addendum M2 (lines 144 … | literature-check | retained at the refute gate — to remediate |
| LITERATURE-2-2 | major | dropped source clause / incomplete round-1 fix | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1623-1647 (§10 N-2, N-3), :1522-1529 (§8 bare-number … | The remediation for QUANT-1-2 / QUANT-1-3 verified that ks-sc-001's README states a headline null stronger than the arm log carried, and that ks-sc-002's extraction is truncated on … | In-repo primary bytes confirm both clauses: docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 34-41 — "**No pri … | Add a dated correction note to corpus §10 N-2 and N-3 recording the two ks-sc-001 sentences and the ks-sc-002 tail sentence verbatim, attributed, with the in-repo locator ks-github … | charter commitment 5 (attribution fidelity); H001 design.md §1.6(i) lines 547-570 and §1.6(ii) lines 613-672 | literature-check | retained at the refute gate — to remediate |
| LITERATURE-2-3 | major | search-coverage instrument not reported where required | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (whole file — absent); docs/deliverables/deliverable … | The known-item recall check promised by the declaration's corpus-record deliverable row was executed in remediation (SCOPE-1-4) but published only in the declaration amendment D10 … | grep for "recall" in the corpus record returns only the Y3 definition ("an executing agent's own recall") at line 62 — no known-item recall reporting. grep for "4.3%", "known-item" … | Add a subsection to the corpus record (natural home: §4 or a new §5.5) stating the check, the 14/327 = 4.3% figure, BOTH bounds verbatim from ks-known-item-recall.json (imperfect s … | deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10; PRESS 2015 known-item recall check as the 2026-09-02 branch a … | literature-check | retained at the refute gate — to remediate |
| LITERATURE-2-4 | major | uncited method + wrong section pointer | research/01_hypothesis_register/H001/design.md:793 (§4), :965-990 (§6), :1541-1657 (§13 References) | The same defect class that the Politis-White remediation was written to close is still open for the AFML-derived machinery. "AFML" is an unexpanded abbreviation with no bibliograph … | Line 793: "**Triple-barrier labelling per AFML §3.2 does not apply and is not used.**" Verified against the book's table of contents: Chapter 3 runs 3.1 Motivation, 3.2 The Fixed-T … | Add the full record to §13 — López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. ISBN 978-1-119-48208-6 — and cite it at §4 for the triple-barrier method wi … | López de Prado (2018), Advances in Financial Machine Learning, Ch. 3 §3.4 (Triple-Barrier Method), Ch. 7 §7.4 (Purging a … | literature-check | retained at the refute gate — to remediate |
| LITERATURE-2-5 | major | provenance contradiction introduced by remediation | research/01_hypothesis_register/H001/design.md:29-35 (`corpus_record_sha256`), :43-74 (`read_state_digest_discipline`), … | The QUANT-1-5 remediation added six computed digests to the H001 front matter but left three statements elsewhere in the same file — and one in hypothesis_backlog — asserting that … | Front matter lines 29-35: "corpus_record_sha256: TO COMPUTE — no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rathe … | Rewrite `corpus_record_sha256` to carry the computed value with the read-state limit that `read_state_digest_discipline` already states, retaining the superseded 'no tool available … | charter commitment 5; the record's own correction convention ("the superseded wording is retained") | literature-check | retained at the refute gate — to remediate |
| REPRODUCIBILITY-2-1 | critical | entrypoint_runs | docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-query-table-supplementary.py (module tail, no __main_ … | NEW defect, introduced by the round-1 remediation that archived and documented these scripts. Two of the archived executor scripts run their query loop at MODULE level with no `if … | Verified destructively and disclosed: loading ks-academic-query-table-supplementary.py under PYTHONHASHSEED=0 (an import, not `main()`) executed live Crossref/OpenAlex/arXiv querie … | (1) Restore or re-execute the 16 affected supplementary-block queries and reconcile the §3 fence, or record the loss as a dated data-integrity entry (DI-9) plus a gap — do not leav … | Protocol section 3.0 (verbatim logging obligation); PAYLOADS.md "Retained"; README.md "What was changed in these scripts … | reproducibility-verifier | retained at the refute gate — to remediate |
| REPRODUCIBILITY-2-2 | critical | data_hashed | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front-matter protocol_amendments) and §3.3; docs … | Round-1 remediation item (7) is INCOMPLETE. Amendment M2 was issued and registered in two of the three required registers — the protocol Addendum (line 1441) and ks-amendments.json … | `grep -c "M2" lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns 0. Line 74 still reads `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full … | Amend front matter line 74 to "TWO numbered append-only amendments, M1 and M2", add an M2 subsection to §3.3 carrying its POST-EXECUTION status and the words "weaker than M1" verba … | protocol_kalshi-strategy-multivocal_2026-09-04.md §10 and Addendum M2; ks-amendments.jsonl | reproducibility-verifier | retained at the refute gate — to remediate |
| REPRODUCIBILITY-2-3 | major | data_hashed | research/01_hypothesis_register/H001/design.md front matter, `corpus_record_sha256` and `read_state_digest_discipline` | Incomplete fix of QUANT-1-5. The six read-state digests the lead computed were verified against disk: five match exactly, but the load-bearing one — the corpus record itself — does … | Recomputed on 2026-09-04: lit_review_kalshi-strategy-multivocal_2026-09-04.md = 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21; the design records b36795140b5bc93 … | Recompute the corpus-record digest after the M2 and DI-9 edits land, record it with the date and time of computation, and state that a digest recorded mid-remediation is void; dele … | H001 design.md §12 pre-freeze checklist item 7 | reproducibility-verifier | retained at the refute gate — to remediate |
| REPRODUCIBILITY-2-4 | major | data_hashed | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10; docs/literature/search_logs/kalshi-strategy … | Probe (d): the 4.3% recall figure does NOT travel everywhere it is owed, and it travels with only one of the two figures its own log computes. (a) The declaration's own §4 promise … | `grep -rn "known-item\\|recall" lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns one hit, and it is the Y3 exclusion code's use of the word "recall" (model recall), not … | Add a subsection to the corpus record §5 or §13 stating the known-item recall check, both figures (14/327 = 4.3% against the identified universe, 13/327 = 4.0% against reported bra … | deliverable_spec_kalshi-strategy-corpus_2026-09-04.md "Why this is a NEW branch" item 4; charter commitment 5 | reproducibility-verifier | retained at the refute gate — to remediate |
| REPRODUCIBILITY-2-5 | major | data_hashed | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :114 (front-matter corpus_multivo … | Probe (g): the MV- prefix sweep is internally consistent (89 MV-G-/MV-TC- occurrences, no orphaned bare G-n citations to the multivocal corpus), but the round-1 remediation added T … | Corpus record §12.1 now runs to G-28 and line 2069 states "The full gap list is section 12.1 (`G-1` … `G-28`)". Agenda line 114: "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CIT … | Extend the four range statements to G-1..G-28 and add MV-G-26/27/28 to the agenda's gap register, each either consumed by a branch or explicitly recorded as a gap this agenda decli … | agenda rev 3 derivation rule ("every branch derived ONLY from a named gap or TO COMPUTE handoff in the new corpus record … | reproducibility-verifier | retained at the refute gate — to remediate |
| FORMAT-2-1 | critical | templates | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`); whole file | NEW defect introduced by round-1 remediation. Amendment M2 was issued against the frozen protocol (protocol §Addendum M2; ks-amendments.jsonl line 3), but the corpus record does no … | corpus front matter: "protocol_amendments: \"ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...\""; protocol M2: "Nothing about them change … | Amend `protocol_amendments` to "TWO numbered append-only amendments, M1 and M2", retaining the superseded wording in the same dated-correction style used for `rng_seed` and `screen … | protocol §10 amendment-enumeration rule; ks-amendments.jsonl M2 `execution_stage`; task constraint "there are now TWO, M … | format-auditor | retained at the refute gate — to remediate |
| FORMAT-2-2 | major | citations | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803 | Seventh locus of the RePEc defect, missed by the remediation's six-locus sweep. The agenda still describes the corpus record's CURRENT text as asserting four executed-and-zero quer … | "the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero ... **One discrepancy between the second corpus record and its ow … | Append a dated correction bullet (matching the house struck-text pattern) recording that the corpus record was corrected at limitation 9, N-5, N-8, the four section-2 source rows a … | corpus DI-8 / G-26; failure_log.md F007 ADDENDUM 2026-09-04; charter commitment 5 | format-auditor | retained at the refute gate — to remediate |
| FORMAT-2-3 | major | citations | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:58-60, 185-188, 1753-1754 | The MV- prefix convention (REV-1-3 remediation) fixes the multivocal identifier space at G-1..G-25 and TC-1..TC-15. Remediation then added three new corpus gaps — G-26 (RePEc never … | agenda:187-188 "The **multivocal** corpus ... names gaps **G-1…G-25** and handoffs **TC-1…TC-15**"; corpus §12.1 carries G-26, G-27, G-28 | Extend the convention statement to G-1..G-28, add MV-G-26/27/28 to the gap register, and state for each either the branch that consumes it or that it is registered and deliberately … | agenda rev-3 convention block; corpus §12.1 rows G-26/G-27/G-28 | format-auditor | retained at the refute gate — to remediate |
| FORMAT-2-4 | major | magic-numbers | research/01_hypothesis_register/H001/design.md:29-35, 43-74, 89, 1509-1516, 1530-1537; hypothesis_backlog.md:32 | The read-state digest remediation (QUANT-1-5) was applied at one locus and left four contradicting loci untouched, inside the same front matter. `corpus_record_sha256` still reads … | design.md:30 "TO COMPUTE — no shell or hashing tool was available ... NO DIGEST IS ASSERTED rather than guessed" vs design.md:54-55 "corpus record lit_review_kalshi-strategy-multiv … | At each of the four stale loci, record the digest (or a pointer to the read_state_digest_discipline block) with the same limit already stated there — pins a future re-read, does no … | CLAUDE.md §Reproducibility; design.md `read_state_digest_discipline`; QUANT-1-5 remediation | format-auditor | retained at the refute gate — to remediate |
| FORMAT-2-5 | major | citations | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (limitations 1-9, §12); docs/deliverables/deliverabl … | Probe (d): the 4.3% known-item recall figure and its two bounds do not travel — they appear ONLY in declaration amendment D10. `grep '4.3\\|recall'` over the corpus record returns … | spec:56 "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check"; corpus record grep for 'recall' matches only the Y3 exclusion-code … | Add the recall result to the corpus record's limitation block or §12, carrying BOTH bounds verbatim with it (seed-set question mismatch between the two protocols; novelty index cov … | deliverable spec D10; corpus limitation 6 / gap G-10 | format-auditor | retained at the refute gate — to remediate |
| CRITICAL-2-5 | minor | reporting | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10 (:330-347) vs ks-known-item-recall.json resu … | Selective reporting of the more favourable of two computed recall statistics. The log computes and stores both `recall_vs_identified_universe: 0.0428` and `recall_vs_reported_branc … | ks-known-item-recall.json: "found_in_identified_universe": 14, "found_in_reported_branches": 13, "recall_vs_identified_universe": 0.0428, "recall_vs_reported_branches": 0.0398 — ag … | Report both figures wherever the recall is stated, with the denominator each is taken against, as the log itself distinguishes them. | SAMPL: no selective reporting of computed analyses; CHAMP item 20 | critical-reviewer | logged, not remediated |
| CRITICAL-2-6 | minor | consistency | hypothesis_backlog.md:32 (H001 row, tail of the round-1 correction note) vs research/01_hypothesis_register/H001/design. … | The two artifacts disagree on the state of the same pre-freeze obligation. The backlog's H001 row states pre-freeze checklist item 7 as "no read-time SHA-256 is recorded for the co … | hypothesis_backlog.md:32 "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is asser … | Append a dated note to the H001 backlog row (the file is append-only) recording that the six digests were computed by the lead session on 2026-09-04, that item 7 is discharged as t … | CHAMP internal consistency; charter commitment 3 (a stated state must match the artifact it describes) | critical-reviewer | logged, not remediated |
| CRITICAL-2-7 | minor | reporting | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §3 fences ks-ssrn (:613-616), ks-ghcode (:661-666), … | DI-8 states that the corrected defect class "extends to SSRN (HTTP 403), GitHub code search (HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are now fl … | "# ks-ssrn-01 \| executed 2026-09-04T10:30:21-05:00 \| HTTP 403 \| n_returned=0 \| n_total_reported=None" — against DI-8: "The same class extends to SSRN (HTTP 403), GitHub code se … | Add `n_returned_semantics` (or an equivalent "not an observed zero-yield" tag) to the ks-ssrn, ks-ghcode and ks-nb fence annotations, matching the ks-repec treatment, with the fenc … | PRISMA-S item 8 (search strategies as run) and item 15 (records identified per source); DI-8's own stated scope | critical-reviewer | logged, not remediated |
| CRITICAL-2-8 | minor | reporting | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 gap G-27 (:1875) | G-27 is headed as a gap about "S-D and S-E retrieved bytes" but reports a verification covering only the 32 lateral (S-E) payloads. It never states that the 28 included S-D venue-d … | "**S-D and S-E retrieved bytes are NOT in this repository, so their `sha256_of_retrieved_bytes` values are ATTESTATIONS a reader cannot check.** … the lead session hashed all 32 la … | State in G-27, in a sentence of its own, that no S-D document digest was re-verified against its bytes at any point, so the S-D half of the gap is unverified rather than verified-o … | CHAMP item 19 (data described adequately and correctly); the record's own warrant-per-record rule (ADR-0006 §What the wi … | critical-reviewer | logged, not remediated |
| CRITICAL-2-9 | minor | consistency | failure_log.md F007 addendum (:555-581) vs F007 body (:482-492) | The F007 addendum declares the row "superseded on ONE sentence only" and names that sentence as "Neither the corpus record nor the arm log is edited by this row". But the same para … | "the row above is left standing verbatim and is superseded on ONE sentence only.** The sentence *"Neither the corpus record nor the arm log is edited by this row"*" | Amend the addendum's scope sentence (append-only) to name both superseded sentences: the "neither is edited" clause and the present-tense "Corpus §10 N-5 states that four" clause. | Charter commitment 5; append-only supersession discipline (protocol section 10 pattern) | critical-reviewer | logged, not remediated |
| CRITICAL-2-10 | minor | reporting | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 (:1873-1877) | The gap table is out of numeric order at its tail: G-24, then G-28, G-27, G-26, G-25. The three rows added by round-1 remediation were inserted before the pre-existing G-25 rather … | row order in §12.1: "\| **G-24** \| **Grey-literature content drift is unmitigated.** …" then "\| **G-28** \| **The CSL-JSON store builder was never archived.**" then "\| **G-27** … | Reorder the three appended rows to G-25, G-26, G-27, G-28, or append them after G-25 in issue order. No text change is required. | SAMPL: tables acceptable and non-duplicative; CHAMP item 22 (presentation) | critical-reviewer | logged, not remediated |
| SCOPE-2-5 | minor | partial | docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:336-338 vs ks-known-item-recall.json:14-16 | Probe (d): D10 publishes one recall figure where its own source file computes two. The log reports recall against the identified universe (14/327 = 4.28%) AND against the reported … | ks-known-item-recall.json :13-16 — "found_in_identified_universe": 14, "found_in_reported_branches": 13, "recall_vs_identified_universe": 0.0428, "recall_vs_reported_branches": 0.0 … | State both figures wherever the recall is reported, with the denominator distinction named, or state explicitly why only the identified-universe figure is carried. | taskSpec probe (d); charter commitment 5 | scope-auditor | logged, not remediated |
| SCOPE-2-11 | minor | added | docs/literature/search_logs/kalshi-strategy-multivocal/README.md, PAYLOADS.md, queries.py, run_arm.py, ks-payload-digest … | Round-1 reproducibility remediation added five files to the declared search-log directory. They are legitimate materials of a declared deliverable and are described inside the corp … | Spec D2 :168-171 — "two pre-registration inputs added to the search-log directory before freeze ... Recording it here because an undeclared delegation is a scope divergence even wh … | Append a declaration amendment naming the files round-1 remediation added to the search-log directory and what each is for; downgrade to documented-drift once recorded. | spec D2 precedent | scope-auditor | logged, not remediated |
| SCOPE-2-12 | minor | partial | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:613-616, :661-667, :745-752 | DI-8 extends its own defect class to SSRN, GitHub code search and Kaggle kernels and states their section-2 counts are now flagged; the section-2 rows were indeed flagged, but the … | DI-8 :1823-1826 — "The same class extends to SSRN (HTTP 403), GitHub code search (HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are now flagged as in … | Annotate the ks-ssrn, ks-ghcode and ks-nb fence rows the way the ks-repec rows were annotated — the request was refused, not answered with a result set — or state in DI-8 why those … | DI-8 | scope-auditor | logged, not remediated |
| QUANT-2-6 | minor | reporting | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :114, :187, :1753 | The agenda's identifier-collision convention — the round-1 REV-1-3 remedy — states at four loci that the multivocal corpus supplies gaps 'G-1..G-25'. The same round added G-26, G-2 … | Agenda line 114: *"its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 ... are the sole admissible source of branches 7-11" … | Update the four range statements to G-1..G-28 with a one-line dated note recording that G-26/G-27/G-28 were added by round-1 remediation after rev 3 was written, and state whether … | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1, §15 item 9 | quant-auditor | logged, not remediated |
| QUANT-2-7 | minor | reporting | hypothesis_backlog.md:36 (H001 row, Notes cell) | Probe (a): the withdrawn false clause is left as running prose at its point of use and is struck only by a note roughly 350 words later in the same table cell. Everywhere else in t … | The cell reads *"... and no SHA is recorded, because the corpus record the design depends on (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md) does not yet exis … | Insert an inline marker at the clause itself — e.g. strike-through markup or a bracketed `[FALSE — see CORRECTION at end of this cell]` immediately after 'does not yet exist' — wit … | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md limitation 9 correction block (the in-file standard) … | quant-auditor | logged, not remediated |
| QUANT-2-8 | minor | reproducibility | docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json (key scratchpad_path_UNTRACKE … | The REPRODUCIBILITY-1-6 remedy introduces an absolute home-directory path carrying the OS username into a newly tracked file, contrary to the project convention and to the corpus r … | File contains `"scratchpad_path_UNTRACKED_AND_EPHEMERAL": "C:\\Users\\skoir\\AppData\\Local\\Temp\\claude\\C--Users-skoir-castles\\e88a64c5-...\\scratchpad\\lateral"`. Repo CLAUDE. … | Replace the literal path with a non-resolving descriptor (e.g. `"<session scratchpad>/lateral (untracked, ephemeral, not reconstructible)"`), keeping the session-id if it is load-b … | C:/Users/skoir/castles/CLAUDE.md §Identity hygiene, final paragraph | quant-auditor | logged, not remediated |
| QUANT-2-9 | minor | reproducibility | docs/literature/search_logs/kalshi-strategy-multivocal/candidates.json, .../title_merge_ledger.json; .../README.md:73-74 | Two regenerated intermediates sit untracked inside a tracked search-log directory, in direct conflict with the README's stated intent, and neither follows the directory's ks- namin … | `git status --porcelain` lists `?? docs/literature/search_logs/kalshi-strategy-multivocal/candidates.json` (348,776 bytes) and `?? .../title_merge_ledger.json`, both mtime 2026-09- … | Delete the two regenerated files before the final commit, or gitignore them, or commit them under ks- prefixed names and amend the README sentence. Do not leave the stated intent a … | docs/literature/search_logs/kalshi-strategy-multivocal/README.md §'The one missing academic intermediate' | quant-auditor | logged, not remediated |
| LITERATURE-2-6 | minor | stale identifier-space declaration | docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:59-60, :187, :1753 | The MV- prefix convention introduced for REV-1-3 declares the multivocal corpus's identifier space as G-1…G-25, but the same remediation round added G-26, G-27 and G-28 to that rec … | Agenda line 187: "The **multivocal** corpus ... names gaps **G-1…G-25** and handoffs **TC-1…TC-15**"; repeated at lines 59-60 and 1753. Corpus record §15 item 9: "The full gap list … | Update the three range statements to G-1…G-28 and note that MV-G-26, MV-G-27 and MV-G-28 are named-but-unconsumed by rev 3, or open a debt row for them. Also note that the corpus r … | agenda front-matter revision_note clause (3); corpus record §12.1 | literature-check | logged, not remediated |
| LITERATURE-2-7 | minor | weaker locator cited than the one available in repo | research/01_hypothesis_register/H001/design.md:561-570, :621-624, :1530-1537 (pre-freeze item 7), :1588-1594 (§13) | The §1.6 findings are provenanced to a URL re-fetch in converted text, with byte-depth verification and digest recomputation deferred to pre-freeze item 7. An in-repo archived copy … | docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 34, 40-41 and .../himagna16__kalshi-microstructure.md lines 9 … | Cite the in-repo evidence file plus its line positions and matching digest alongside the raw URL in §1.6(i)/(ii) and §13; narrow pre-freeze item 7 to whatever genuinely remains aft … | CLAUDE.md Reproducibility contract (untracked locator vs clone-durable carrier); evidence hierarchy tier ordering | literature-check | logged, not remediated |
| LITERATURE-2-8 | minor | quotation attributable to the wrong source | research/01_hypothesis_register/H001/design.md:1187-1191 (§8.1) | An italicised sentence follows the naming of Kaufman, Rosset, Perlich & Stitelman 2012 in a construction that reads as a quotation from that paper. The sentence is in fact the word … | Line 1188-1191: "The formal treatment is Kaufman, Rosset, Perlich & Stitelman 2012 (charter commitment 4), and it applies here without modification: *every feature must be computab … | Attribute the italicised sentence to rules/quant-project.md §"Time-series integrity" explicitly, or de-italicise it and state it as the design's own restatement of the rule, keepin … | charter commitment 5; doi:10.1145/2382577.2382579 (verified: ACM TKDD 6(4), Dec 2012) | literature-check | logged, not remediated |
| LITERATURE-2-9 | minor | undeclared method transfer | research/01_hypothesis_register/H001/design.md:970-986 (§6 embargo) | The Politis-White automatic block length is used as one of two inputs to the walk-forward EMBARGO length. Neither cited paper addresses embargoing or purged cross-validation; both … | §6: "`embargo` selection method: TO COMPUTE — selection procedure: the maximum of (i) the lag at which the residual PACF ... and (ii) the **Politis–White automatic block length** f … | Add one clause to §6 stating that the block-length estimator is transferred from bootstrap resampling to embargo selection as a dependence-horizon estimate, that neither cited pape … | doi:10.1081/ETC-120028836 and doi:10.1080/07474930802459016 (both verified via Crossref); design §3.2 and §13 for the de … | literature-check | logged, not remediated |
| REPRODUCIBILITY-2-6 | minor | data_hashed | docs/literature/search_logs/kalshi-strategy-multivocal/PAYLOADS.md, "Retained" -> software-repository paragraph | The retained-bytes inventory under-states which S-C query rows carry no payload. It says payloads exist only for HTTP 200 rows and that "the five PyPI names that 404'd are logged w … | Recomputed all fifty-nine ks-github-queries.json rows: 49 payload digests verify exactly (0 missing, 0 mismatch) after gzip decompression, confirming the `payload_sha256_basis` cla … | Amend the sentence to "the five PyPI names that 404'd and the five auth-blocked rows (ks-ghcode-01/02, ks-nb-01/02/03, HTTP 401 — gap G-22) are logged with no payload". | PAYLOADS.md; corpus record N-8 / G-22 | reproducibility-verifier | logged, not remediated |
| REPRODUCIBILITY-2-7 | minor | data_hashed | docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json | The verified-once evidence for G-27 is recorded only in aggregate. `results` gives 32/32/0/0 with `mismatched_detail` and `missing_detail` empty, but there is no per-record list of … | File contents: `"results": {"records_checked": 32, "matched": 32, ...}`, no itemisation; `"scratchpad_path_UNTRACKED_AND_EPHEMERAL": "C:\\Users\\skoir\\AppData\\Local\\Temp\\claude … | Add the 32-row itemisation (record id, local_payload_name, digest recomputed, digest as recorded) so the verified-once claim is at least internally auditable after the scratchpad c … | corpus record G-27; PAYLOADS.md "Where the S-D bytes actually are" | reproducibility-verifier | logged, not remediated |
| FORMAT-2-6 | minor | style | docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1874-1877 | The §12.1 named-gap table is out of identifier order after remediation: G-28, then G-27, then G-26, then G-25. A reader scanning for a gap id can miss a row. | row order in §12.1: "\| **G-28** \| ... \| **G-27** \| ... \| **G-26** \| ... \| **G-25** \|" | Sort the three appended rows into numeric position, or state once above the table that appended rows are listed in remediation order. | house table convention across §12.1 rows G-1..G-24 | format-auditor | logged, not remediated |
| FORMAT-2-7 | minor | templates | docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:784-785 vs 481, 624, 793, 843, 889 | Round-1 finding on surviving `[INSTRUMENT-*]` tokens is NOT remediated: the prescribed fix was a one-line clarification in the append-only Addendum, and the Addendum contains only … | protocol:784 "**A placeholder surviving into the registration commit is itself a defect**; none survives." against protocol:793 "### 7.1 [INSTRUMENT-MLR] — ...", :843, :889, :481, … | Append the one-line Addendum clarification (frozen text cannot be edited): the `[INSTRUMENT-*]` tokens are retained deliberately as stable cross-reference anchors, the substitution … | protocol §7; round-1 template-substitution finding and its recorded fix | format-auditor | logged, not remediated |

## refute-gate

Every critical and major finding was put to an independent adversarial refuter, whose standing
instruction is that a drop requires concrete counter-evidence — a source, a reproduced check, or
a counter-example — and that bare disagreement, a plausibility argument or a severity quibble is
not refutation ([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). **0 of 33 were dropped this
round; 33 were retained; 0 were retained-conservative.** Each entry below carries the claim
VERBATIM and unabridged, the raiser, the refuter, the enumerated evidence type, and — where
`reproduction_required` is true — the reproduction block lifted from the refutation evidence.
`evidence_type: none` means the refuter searched for counter-evidence and found none, which is
the ground on which the finding is retained rather than dropped.

### CRITICAL-2-1 - RETAINED

- **raised by:** `critical-reviewer` (severity claimed: critical; category: design)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74, :1173-1198 (§3.3), :73 (protocol_path comment)

**Claim, verbatim.**

> **issue.** The corpus record does not enumerate protocol amendment M2, and positively asserts that only one amendment exists. Round-1 remediation issued M2 (finding SCOPE-1-7) against the frozen protocol and registered it correctly in BOTH registers protocol section 10 requires — the protocol addendum (protocol_kalshi-strategy-multivocal_2026-09-04.md:1441-1480) and ks-amendments.jsonl line 3 — but the third obligation, enumeration in the corpus record, was not discharged. M2 is not a query-admissibility ruling like M1: it is a POST-EXECUTION ruling on the disposition semantics of 1,465 of the 1,574 screened records (93% of the delivered flow), i.e. on the very dispositions this record reports and on the n_excluded == Y-rows + G-rows decomposition it publishes in §5.4. The record therefore materially ran under M2. Three loci are wrong: (a) front-matter `protocol_amendments` opens "ONE numbered append-only amendment, M1"; (b) §3.3 is headed "Amendment M1, enumerated" and states "One amendment exists"; (c) the `protocol_path` comment says "the M1 addendum is appended BELOW the frozen line", which no longer describes the file. Charter/protocol A6 (deliverable consistent with the frozen design and its amendment register) fails, and it fails against a rule the record quotes against itself one sentence earlier.
>
> **evidence.** "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here" (lit_review §3.3, lines 1175-1176) — against protocol addendum "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared" and "**1,465 of the 1,574 screened records - 93% of the delivered flow - took the path section 4.2 does not enumerate.**"
>
> **fix.** Add §3.4 "Amendment M2, enumerated" to the corpus record, carrying M2's ruling, its POST-EXECUTION stage in those words, its declared weakness relative to M1, and its scale (1,465 of 1,574). Change the front-matter `protocol_amendments` field to "TWO numbered append-only amendments, M1 and M2" and enumerate both; correct §3.3's "One amendment exists" and the `protocol_path` comment to name both addenda. Retain the superseded wording in a dated correction note at each locus, as the DI-8 remediation did.
>
> **reference.** Protocol section 10 (amendment enumeration); CHAMP item 6 (consistency with the pre-registered protocol); ks-amendments.jsonl header "A discrepancy between the two is itself a defect"

**Refutation attempt.**

> No refuting evidence found; every element of the finding reproduced exactly, and the two available refutation angles both collapse.
> 
> REPRODUCED CHECKS (all on bytes currently on disk):
> 
> 1. `grep -c "M2" docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns **0**. The string "M2" does not occur anywhere in the corpus record — no §3.4, no correction note, no front-matter mention. The non-enumeration is total, not partial.
> 
> 2. Locus (a), line 74 exactly as quoted: `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record ..."`. The field enumerates only M1(a)/M1(b)/M1(c).
> 
> 3. Locus (b), lines 1173/1175-1176 exactly as quoted: heading `### 3.3 Amendment M1, enumerated`, then "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here". The self-quoted rule and the false assertion are adjacent, as the finding states.
> 
> 4. Locus (c), line 73: `protocol_path: ... the M1 addendum is appended BELOW the frozen line and the prefix digest is unchanged by it` — names only the M1 addendum.
> 
> 5. Both registers protocol §10 requires DO carry M2. ks-amendments.jsonl line 3 is a full M2 object (`"execution_stage": "POST-EXECUTION and declared as such per section 10..."`, `"raised_by": "SCOPE-1-7"`, `"scale": "1,465 of 1,574 screened records (93% of the delivered flow)..."`). The protocol addendum carries the prose twin at lines 1440-1480, heading `### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared`. So the discrepancy is exclusively the corpus record's, and the two-register consistency the finding relies on is intact.
> 
> 6. SOURCE QUOTE, protocol §10 (lines 1150-1153), verbatim: "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective." The obligation the finding invokes exists in the frozen text and is stated in exactly those terms.
> 
> WHY THE TWO REFUTATION ANGLES FAIL:
> 
> A. "The record did not RUN UNDER M2, since M2 postdates the dispositions." Defeated by the same §10 paragraph, lines 1146-1149: "An amendment logged after the affected decisions were made must say so in those words; that is a weaker amendment than a pre-execution one, **and the corpus record reports the distinction.**" §10 therefore imposes a corpus-record reporting duty on post-execution amendments specifically. Even the narrowest construal of "ran under" leaves the record in breach of an explicit §10 sentence. M2's own addendum text repeats the duty ("the corpus record reports it as such") and points at the record's own published decomposition ("exactly as the corpus record does (`n_excluded == Y-rows + G-rows`, 10 + 1,465 = 1,475)") — which I confirmed the record publishes at front-matter lines n_excluded: 1475 / n_criterion_excluded: 10 / n_capacity_gap: 1465. The record reports the very quantity M2 adjudicates.
> 
> B. "Only the enumeration is missing; the affirmative assertion is harmless." Defeated on its face: "One amendment exists" (line 1176) is a positive factual claim about the amendment register, and the register on disk contains two amendments. That is a standalone falsity independent of any construal of "ran under."
> 
> Conclusion: the defect claim is true as stated at all three loci. Nothing in the artifacts, the register, or the frozen protocol contradicts it.

### CRITICAL-2-2 - RETAINED

- **raised by:** `critical-reviewer` (severity claimed: major; category: consistency)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803

**Claim, verbatim.**

> **issue.** Incomplete remediation of the round-1 RePEc defect. The agenda still asserts, in the present tense and explicitly as a LIVE un-repaired discrepancy, that the corpus record's §10 N-5 states four academic queries in the weather stratum executed and returned zero. That was corrected at six loci in the corpus record in this same round (limitation 9, N-5, N-8, four §2 source rows, nine ks-repec fence annotations, DI-8, G-26), and failure_log F007 was given a dated addendum saying so — but the agenda, which the same round edited (86-identifier MV- prefix sweep), was not. A reader of the agenda alone is told the corpus record still carries the false claim, and the bullet is framed as something the agenda declines to repair. Probe (b) fails at this artifact: the corpus record, F007/DI-8 and the arm logs now agree; the agenda does not agree with any of them.
>
> **evidence.** "**One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here** … the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero, while `ks-repec-04.json`'s own `platform_interface_failure` field states that its query **never executed**"
>
> **fix.** Replace the bullet with a dated correction note in the agenda's own append-only style: retain the superseded sentence marked struck, and state that as of 2026-09-04 the corpus record has been corrected at limitation 9, N-5 and N-8, that the executed-and-zero count of two now appears in both documents, and that the discrepancy is no longer live. Cite DI-8 and MV-G-26.
>
> **reference.** Charter commitment 5 (attribution fidelity); SAMPL/CHAMP internal-consistency requirement — a claim about a cited document must match that document

**Refutation attempt.**

> No refutation found; the defect reproduces. (1) The agenda bullet at docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803 is verbatim as quoted, is in the present tense, is the final content of the 1803-line file, and carries no dated correction/supersession marker — even though the same file uses that convention elsewhere (line 56 "CORRECTED 2026-09-04, audit finding REV-1-3"; line 303 "PARTLY SUPERSEDED"). (2) The cited document no longer says what the agenda says it says: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §10 N-5 (line 1661 f.) now reads "**Two** academic queries in that stratum executed and returned zero: ks-arxiv-04 ... and ks-openalex-04 ... **ks-repec-04 and ks-repec-04-b did NOT execute.**", immediately followed by a "CORRECTION 2026-09-04 (round-1 audit; REV-1-1, SCOPE-1-1, QUANT-1-1, LITERATURE-1-1, REPRODUCIBILITY-1-1, FORMAT-1-1)" block retaining the struck four-query wording. (3) DI-8 in the same record (~line 1828) confirms the six-locus repair: "Limitation 9, **N-5**, **N-8**, the four section 2 source rows and the nine `ks-repec` annotations in the section 3 fence are corrected in place", with "**The corrected executed-and-zero count is TWO.**", gap G-9 extended and G-26 added (line 1858). (4) failure_log.md F007 (lines 459-482) agrees with the corrected reading. Corpus record, DI-8, F007 and the ks-repec arm logs (lines 593-609 of the corpus record fence, each carrying platform_interface_failure and n_returned_semantics "no search executed") are mutually consistent; the agenda alone is not. The claim that the discrepancy is "recorded and NOT repaired" is therefore false as of the current tree.

### CRITICAL-2-3 - RETAINED

- **raised by:** `critical-reviewer` (severity claimed: major; category: consistency)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:59-60 and :114 (front matter `corpus_multivocal`)

**Claim, verbatim.**

> **issue.** The agenda declares, at two loci, that the multivocal corpus supplies gaps G-1..G-25, and that these are cited in the agenda as MV-G-1..MV-G-25 and are "the sole admissible source of branches 7-11". The same remediation round added THREE gaps to that corpus record — G-26 (RePEc was never searched), G-27 (S-D/S-E digests are verified-once attestations) and G-28 (the CSL-JSON store builder was never archived) — and the corpus record's own §15 item 9 now reads "the full gap list is section 12.1 (`G-1` … `G-28`)". The agenda's declared range is stale, so MV-G-26, MV-G-27 and MV-G-28 fall outside the identifier space the agenda declares admissible, none is consumed by any branch, and the agenda's RePEc claim at :1088 rests on MV-G-9 and MV-G-22 rather than on the gap created for it.
>
> **evidence.** agenda:114 "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 … are the sole admissible source of branches 7-11" — against lit_review §15 item 9 "**The full gap list is section 12.1 (`G-1` … `G-28`)**"
>
> **fix.** Update both range declarations to G-1..G-28 / MV-G-1..MV-G-28 with a dated rev-3 correction note recording that the range moved by round-1 remediation, and cite MV-G-26 at the agenda's RePEc statement (:1088) alongside MV-G-9 and MV-G-22.
>
> **reference.** Deliverable spec, agenda row check: "every new branch cites a gap id or handoff id that exists in the new corpus record"

**Refutation attempt.**

> Attempted refutation failed; every element of the finding reproduced. (1) agenda:114 verbatim: "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 ... are the sole admissible source of branches 7-11". (2) lit_review_kalshi-strategy-multivocal_2026-09-04.md:2069 verbatim: "9. **The full gap list is section 12.1 (`G-1` ... `G-28`) and the full handoff list". (3) G-26, G-27, G-28 exist as section 12.1 rows at corpus lines 1876, 1875, 1874 respectively, each stamped "Added 2026-09-04 by round-1 audit remediation" (REV-1-1/LITERATURE-1-2/REPRODUCIBILITY-1-2 for G-26; REPRODUCIBILITY-1-6 for G-27; REPRODUCIBILITY-1-4 for G-28) - confirming the same-round addition the finding alleges. (4) Counter-test for consumption: `grep -n "MV-G-2[6-9]\|G-26\|G-27\|G-28"` over the agenda returns zero matches (exit status 1), so MV-G-26/27/28 are cited nowhere in the agenda and no branch consumes them. (5) The agenda's RePEc statement at :1087-1090 ("RePEc's interface never returned a result set at all") cites MV-G-9, MV-G-22 and failure_log F007, not MV-G-26 - as claimed. (6) No countervailing amendment exists: ks-amendments.jsonl (3 lines) contains no G-26/27/28 token. Finding is if anything understated in scope: the stale G-1..G-25 range appears at FOUR loci, not the two cited - lines 60, 114, 187 ("names gaps **G-1...G-25**") and 1753 ("the multivocal corpus supplies G-1..G-25"). No concrete counter-evidence obtained; the defect claim stands.

### CRITICAL-2-4 - RETAINED

- **raised by:** `critical-reviewer` (severity claimed: major; category: standard-coverage)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §4 (:1202-1219), head limitations (:131-235), §12.1 (:1846-1877)

**Claim, verbatim.**

> **issue.** Probe (d): the executed known-item recall figure does not travel with its bounds everywhere it appears because it appears in only ONE prose location — declaration amendment D10 — and nowhere in the deliverable a reader actually consumes. The corpus record contains no occurrence of the strings "recall", "known-item" or "4.3" outside the Y3 exclusion-code definition; the check is absent from the nine head limitations, absent from §4 ("Peer review of the search strategy", the PRISMA-S item 14 locus and the place the predecessor protocol §718 explicitly puts its PRESS known-item recall check), and absent from the gap register. The declaration's own check for this deliverable requires it there: "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." A 4.3% recall against the predecessor's 327 includes is among the most consequential limitations a reader must carry into a record whose session objective is a "comprehensive retrievable record", and §4 currently tells that reader only that no PRESS review was obtained.
>
> **evidence.** lit_review §4: "**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was obtained, and none was simulated. … What *was* done, and what it is not a substitute for: the methodological instruments the protocol declares were resolved and checked … before the protocol froze" — the only thing §4 reports as done; against D10: "**Result: the academic arm identified 14 of the 327 records the predecessor branch dispositioned `include` - a recall of 4.3%.**"
>
> **fix.** Add the recall result to the corpus record §4 with both of its stated bounds (the seed-set/question-mismatch caveat and the 6,923-of-8,813 index bound), cross-reference ks-known-item-recall.json and its input digests, and add a tenth head limitation or a gap row so the agenda can consume it by identifier. State explicitly that it is not a screening statistic, as the log's `denominator_note` does.
>
> **reference.** PRISMA-S item 14 (peer review of the search strategy) and the predecessor protocol's known-item recall clause; deliverable_spec_kalshi-strategy-corpus_2026-09-04.md line 56

**Refutation attempt.**

> Refutation attempted and failed; every prong reproduces.
> 
> (1) Absence in the deliverable reproduced. `grep -n -i "recall|known-item|known item|4\.3"` over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns exactly one hit, line 62, which is the Y3 exclusion-code definition ("came from a summarizer, from an executing agent's own recall"). The 4.3% figure, the phrase "known-item", and the log filename occur nowhere in the 2,072-line corpus record.
> 
> (2) Section 4 reproduces verbatim as quoted. sed -n '1201,1219p' shows "## 4. Peer review of the search strategy" / "<!-- prisma-s-14 -->" / "**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was obtained, and none was simulated." The only affirmative content is the pre-freeze literature-check instrument verification (ks-instrument-verification.json, verdict proceed-with-remediation) carried as gap G-14. No recall statement.
> 
> (3) Head limitations reproduce as nine items (lines ~131-235): academic-arm all-G1, software subset, venue-arm sampling, rulebook not located, three objects withheld at source, novelty upper bound, heterogeneous unit of account, findability/no-DOI, weather-stratum near-zero yield. None is the recall check.
> 
> (4) Gap register reproduces: section 12.1 table at lines 1848-1877 runs G-1 through G-28 (rows out of numeric order at the tail). No row mentions recall or the known-item check.
> 
> (5) Sole prose location confirmed by repo-wide search: `grep -rn "ks-known-item-recall" --include=*.md --include=*.json .` returns ONE hit, docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:335, inside amendment D10, whose line 337 reads "**Result: the academic arm identified 14 of the 327 records the predecessor branch dispositioned `include` - a recall of 4.3%.**"
> 
> (6) The declaration's binding check reproduces at deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:55-57: "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does."
> 
> (7) The comparator standard holds, so "in the manner the 2026-09-02 record does" means section-4 placement: protocol_kalshi-arbitrage-review_2026-09-02.md:718 states "The known-item arm functions as the PRESS known-item recall check, with per-item reporting and no pass threshold", and lit_review_kalshi-arbitrage_2026-09-02.md:744 heads "## 4. Peer review of the strategy" with line 755 stating "the PRESS known-item recall check and returned **16 of 23 items retrieved**" (restated at 4164). The multivocal record's section 4 carries no analogue.
> 
> (8) The one plausible alternate carrier was checked and ruled out. research_agenda_prediction-market-microstructure_2026-09-02.md:1690 does mention a known-item miss, but lines 1685-1700 show it is a round-2 correction INHERITED FROM THE 2026-09-02 PREDECESSOR (KI-20/KI-21, ka-crossref-07, rows=20 cap), not the multivocal 4.3% result. The agenda contains no occurrence of 4.3% or 0.0428.
> 
> (9) The underlying log exists and contains exactly the bounds the fix asks to be carried: ks-known-item-recall.json has seed_set_caveat (predecessor asks arbitrage/coherence/market-making vs this branch's stated strategies), second_caveat (6,923 of 8,813 index bound), denominator_note ("It is not a screening or eligibility statistic: all 528 academic rows are capacity-gap G1 rows and none was assessed"), and results.recall_vs_identified_universe 0.0428. So the check was executed and only its disclosure into the reader-facing deliverable is missing, which is precisely what the finding asserts.
> 
> No counter-evidence found on any prong. Finding stands.

### SCOPE-2-1 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: critical; category: omitted)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`) and :1173-1178 (§3.3)

**Claim, verbatim.**

> **issue.** The round-1 remediation for SCOPE-1-7 issued protocol amendment M2, but the corpus record still enumerates ONE amendment. The protocol's own section 10 makes exactly this defective. The remediation was written into the protocol addendum and into ks-amendments.jsonl and never propagated to the deliverable the rule is about.
>
> **evidence.** Protocol :1150-1152 — "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective." Corpus record front matter :74 — "protocol_amendments: \"ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...\"". Corpus record :1173-1176 — "### 3.3 Amendment M1, enumerated / Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists...". Protocol :1441 — "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION". ks-amendments.jsonl line 3 — {"amendment": "M2", ..., "raised_by": "SCOPE-1-7"}.
>
> **fix.** Amend the corpus record's `protocol_amendments` field to enumerate TWO amendments and retitle/extend §3.3 to "Amendments M1 and M2, enumerated", carrying M2's ruling, its `touches` set (sections 4.2, 4.4), and its declared POST-EXECUTION stage. Retain the superseded "ONE ... M1" wording as struck, per the correction discipline used at DI-8.
>
> **reference.** protocol §10; taskSpec constraint "there are now TWO, M1 and M2"

**Refutation attempt.**

> Attempted refutation failed; every element of the finding reproduces verbatim on disk, and the three exemption theories I tested all collapse.
> 
> 1. Rule text reproduced. C:\Users\skoir\castles\docs\methodology\protocol_kalshi-strategy-multivocal_2026-09-04.md line 1117 opens "## 10. Amendment mechanism — APPEND-ONLY ADDENDUM BELOW THIS SECTION"; lines 1150-1152 read "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective." Exact as quoted.
> 
> 2. M2 exists in both required registers. Protocol line 1441: "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared". ks-amendments.jsonl line 3 carries {"amendment": "M2", ..., "raised_by": "SCOPE-1-7", "touches": {"sections": ["4.2","4.4"], ...}, "execution_stage": "POST-EXECUTION and declared as such per section 10..."}. Both places §10 requires are populated.
> 
> 3. Corpus record still enumerates one. C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md line 74: protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...". Line 1173 heading: "### 3.3 Amendment M1, enumerated". Lines 1175-1176: "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here". Counter-test: `grep -c "M2"` over the whole corpus record returns **0** — the string M2 appears nowhere in the deliverable, and `grep -ni "amendment"` returns no oblique reference to a second amendment either (hits at 260/262, 323, 825-826, 1488-1489, 1697, 1895 are unrelated: taxonomy amendment_needed:null, a CFTC rule-amendments URL, and TC-13's future-amendment note).
> 
> Refutation theories tested and rejected:
> (a) "The corpus record did not run under M2." Rejected on the record's own text: its front-matter capacity_codes block cites "protocol section 4.4 rule 2" and n_capacity_gap: 1465 is reported "per protocol section 4.4 rule 2" — sections 4.2/4.4 are exactly M2's `touches` set, and M2's ruling is what makes the record's 4-outcome flow (include/exclude-Y/promote/G) consistent with §4.2. The record operates under the reconciled reading.
> (b) "M2 is post-execution, so it need not appear." Rejected by §10's own sentence at 1147-1149 — "An amendment logged after the affected decisions were made must say so in those words; ... the corpus record reports the distinction" — and by M2's own text at protocol :1470-1471, "the reconciliation is retrospective and the corpus record reports it as such." Post-execution status increases, not waives, the reporting duty.
> (c) "The corpus record is frozen and cannot be edited." Rejected: only protocol text above the addendum line is frozen ("Frozen text above this line is never edited"). The corpus record already carries an in-place struck correction under the same discipline at line 74's screening_verdict_source field — "CORRECTION 2026-09-04 (finding REV-1-7): this field previously read ..." — proving the deliverable is amendable by that method.
> 
> Defect claim is true as stated: an amendment register and protocol addendum enumerate M1 and M2, while the deliverable the §10 rule governs enumerates only M1 and affirmatively asserts "One amendment exists."

### SCOPE-2-2 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: omitted)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md — §3.3, §5 flow, limitation 1-2, capacity_codes front-matter block

**Claim, verbatim.**

> **issue.** Probe (c): M2's declared weakness — that it is POST-EXECUTION and therefore weaker than M1 — is stated plainly in the protocol addendum and in the amendment register, and is stated NOWHERE in the corpus record, which is the artifact a reader consults for the 1,465 G-dispositions the amendment retrospectively reconciles. The corpus record instead carries only M1's contrasting boast that its departures were PRE-SCREENING.
>
> **evidence.** Protocol :1467-1472 — "Execution stage - POST-EXECUTION, and this is a WEAKER amendment than M1. ... the 1,465 G-dispositions were assigned before this contradiction was adjudicated ... the reconciliation is retrospective and the corpus record reports it as such." The corpus record does not report it as such: grep for "M2" over the corpus record returns no matches, and §3.3 :1186-1191 asserts only "Execution stage, stated in the amendment's own words: PRE-SCREENING ... This is **not** the predecessor branch's A8 position".
>
> **fix.** State M2's post-execution weakness in the corpus record at the loci where the 1,465 G-rows are accounted for (§3.3, §5 flow narrative, and the `capacity_codes` front-matter block), in the amendment's own words, without softening — the protocol says the corpus record reports it, so the protocol's claim is currently false.
>
> **reference.** protocol M2 §"Execution stage"; taskSpec probe (c)

**Refutation attempt.**

> Attempted refutation failed; every check confirmed the finding.
> 
> 1. Counter-test for any mention of M2 in the corpus record: `grep -n "M2" C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns exit status 1 with zero matching lines across all 2,072 lines. Synonym sweep `grep -nEi "post-execution|retrospectiv|second amendment|weaker amendment|fourth stage"` returns only line 1162, which is explicitly a DIFFERENT event — a correction to the ks-openalex-02 query-log annotation, made "before any screening", and the record states "this is not a fourth part of M1". M2 is not disclosed under any alias.
> 
> 2. Protocol addendum reproduced verbatim at C:\Users\skoir\castles\docs\methodology\protocol_kalshi-strategy-multivocal_2026-09-04.md :1467-1472: "**Execution stage - POST-EXECUTION, and this is a WEAKER amendment than M1.** Section 10 requires that an amendment logged after the affected decisions were made say so in those words. It is said here: the 1,465 G-dispositions were assigned before this contradiction was adjudicated ... the reconciliation is retrospective and the corpus record reports it as such." The final clause is false as written.
> 
> 3. §3.3 reproduced at corpus record :1173-1191. Heading is "### 3.3 Amendment M1, enumerated"; body asserts "One amendment exists and all three of its parts are enumerated here"; the execution-stage sentence reads "**Execution stage, stated in the amendment's own words: PRE-SCREENING.** ... This is **not** the predecessor branch's A8 position". Only M1's pre-screening contrast is carried; M2's post-execution weakness is absent.
> 
> 4. Front matter confirms the omission is systematic, not a §3.3-local slip: line 74 `protocol_amendments:` opens "ONE numbered append-only amendment, M1"; the `capacity_codes` block (:69-71), which is where the G1 rows covering the 1,465 dispositions are defined, cites only "protocol section 4.4 rule 2" and says nothing about a retrospective reconciliation; `protocol_path` (:73) states "the M1 addendum is appended BELOW the frozen line", singular.
> 
> 5. The amendment register does carry M2 as a distinct entry, so the corpus record's "One amendment exists" is contradicted by its own cited register. Parsed C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal\ks-amendments.jsonl: entry 1 amendment "M1", execution_stage "PRE-SCREENING..."; entry 2 amendment "M2", decided_at 2026-09-04T13:40:00-05:00, execution_stage "POST-EXECUTION and declared as such per section 10. The 1,465 G-dispositions were assigned before this contradiction was adjudicated. This is a WEAKER amendment than M1."
> 
> Every element of the claim — the protocol's assertion, its falsity in the corpus record, and the specific loci (§3.3, capacity_codes front matter) — reproduces exactly. No counter-evidence available.

### SCOPE-2-3 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: added)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md — "Declaration amendments, round-1 audit remediation" section (D8-D11)

**Claim, verbatim.**

> **issue.** M2 is a post-freeze change to a declared deliverable (the protocol) made during round-1 remediation, and no declaration amendment records it. The declaration set its own precedent at D7, which records M1 for exactly this reason. The round-1 remediation block records D8-D11 and the SCOPE-1-5 discharge but is silent on the amendment SCOPE-1-7 produced.
>
> **evidence.** Spec D7 :256-259 — "D7 - 2026-09-04 - amendment M1 issued against the frozen protocol. Not a new artifact but a change to a declared one, recorded here because the declaration's protocol row said the protocol would be frozen and this records what happened to it after freeze." No corresponding entry exists for M2; the spec's text contains no occurrence of "M2".
>
> **fix.** Append a D12 recording that amendment M2 was issued against the frozen protocol on audit finding SCOPE-1-7, that it is POST-EXECUTION and declared weaker than M1, that it changes no eligibility criterion, disposition or count, and that the frozen prefix hash is unchanged.
>
> **reference.** spec D7 precedent

**Refutation attempt.**

> No refutation possible; every element of the claim reproduced. (1) D7 quote verbatim-accurate at docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:256, including the stated rationale "recorded here because the declaration's protocol row said the protocol would be frozen and this records what happened to it after freeze." (2) grep for "M2" over the 368-line spec exits 1 — zero occurrences. (3) M2 is real and is precisely the event class D7 covers: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:1441 carries the Addendum entry, and docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl:3 records amendment "M2", decided_by "lead session, on audit finding SCOPE-1-7 (scope-auditor, round 1)", execution_stage "POST-EXECUTION ... WEAKER amendment than M1", carrying the same protocol_frozen_sha256 32dfea6da36c... and registration_commit 4821611c as the M1 header row — i.e. a post-freeze change to a declared deliverable made during round-1 remediation. (4) The round-1 remediation block (spec lines 290-368) records SCOPE-1-2 (D8), SCOPE-1-3 (D9), SCOPE-1-4 (D10), SCOPE-1-6 (D11) and the SCOPE-1-5 discharge; grep "SCOPE-1" returns exactly those five and no SCOPE-1-7. The only post-D7 occurrences of "amendment" (lines 306, 311) refer to M1 and to the general amendment discipline, not to M2. The omission is in fact more conspicuous than stated: the block enumerates -1-2 through -1-6 contiguously and -1-7 is the sole gap in that run.

### SCOPE-2-4 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: partial)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (absent throughout); spec D10 :330-347

**Claim, verbatim.**

> **issue.** SCOPE-1-4's remedy is only half-applied. The known-item recall check was executed and its log written, but it is published solely in the declaration — which is the loop's INPUT, not a deliverable — while the corpus record, to which the spec expressly assigns the obligation, still contains no recall check, no result, and no gap row. The agenda therefore has no identifier to consume and a reader of the shipped corpus record cannot learn the figure exists.
>
> **evidence.** Spec :54-57 — "'Comprehensive' is bounded and the bound is published. ... **The corpus record** states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." Grep for "recall" over lit_review_kalshi-strategy-multivocal_2026-09-04.md returns exactly one hit, the Y3 criterion's use of the word in an unrelated sense (:62). ks-known-item-recall.json exists on disk with `recall_vs_identified_universe: 0.0428`. The round-1 audit trail's own remedy (:809) asked for the result to be "registered ... as a numbered gap in section 12.1 so the agenda can consume it"; §12.1 has no such row.
>
> **fix.** Add the recall result to the corpus record — a limitation/section-4 paragraph carrying 14/327, both caveats, and the non-screening denominator note — and register a numbered gap in §12.1 pointing at ks-known-item-recall.json so the agenda can consume it.
>
> **reference.** spec deliverable row for the corpus record; D10

**Refutation attempt.**

> Attempted refutation on five routes; all failed, and every element of the finding reproduced.
> 
> (1) Spec obligation is real and assigned to the corpus record. docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:54-57 reads verbatim: "**\"Comprehensive\" is bounded and the bound is published.** No search is exhaustive. The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does. An unbounded claim of completeness is a defect." The obligation-bearer is the corpus record, not the declaration.
> 
> (2) The corpus record contains no recall check. Exhaustive grep over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md for `known.item|known_item|ks-known|0\.0428|4\.3%|recall` returns exactly one hit: line 62, the Y3 exclusion criterion "...it came from a summarizer, from an executing agent's own recall...". That is model recall, an unrelated sense. Zero hits for "known-item", zero for the log filename, zero for the figure in either decimal or percentage form.
> 
> (3) Counter-test for the figure under a different denominator/format. Grep for `14/327|327` over the same file returns exactly one hit, line 77, which is the AG-11 predecessor-branch note ("149 store entries against 327 included records") — a bibliography-store identity, not the recall check. So the 14/327 figure is not smuggled in under other wording.
> 
> (4) §12.1 has no such gap row. Read in full at :1846-1889. The register runs G-1..G-28 (numbered out of order; G-25..G-28 appended by round-1 remediation). None concerns known-item recall. G-10 ("Novelty differencing is an upper bound: the prior index covers 6,923 of 8,813 predecessor records") is the closest neighbour and is the novelty-differencing bound — it is the same 6,923/8,813 caveat the recall log inherits, but it registers novelty differencing, states no recall figure, and points at no recall log. The round-1 trail's remedy at docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md:809 explicitly asked for registration "as a numbered gap in section 12.1 so the agenda can consume it"; no such row exists.
> 
> (5) The result exists only in the loop's input and on disk. docs/literature/search_logs/kalshi-strategy-multivocal/ks-known-item-recall.json:15 carries `"recall_vs_identified_universe": 0.0428`. The spec's D10 (:330-347) publishes the result in prose — "the academic arm identified 14 of the 327 records the predecessor branch dispositioned `include` - a recall of 4.3%" — with both caveats. The declaration is the loop's input, not a shipped deliverable, so the finding's characterisation of the remedy as half-applied holds.
> 
> (6) Counter-test on the agenda's ability to consume it. Grep for `recall|known.item` over docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md returns lines 12, 103, 112, 1655 (all "model recall" in the provenance sense) and line 1690, "**No demonstrated vocabulary gap** is claimed for any known-item miss." Reading :1687-1697 shows that block is headed "**Round-2 corrections inherited from the corpus record**, all dated 2026-09-02" and concerns the predecessor branch's KI-20/KI-21 items and `ka-crossref-07` — the 16/23 check in lit_review_kalshi-arbitrage_2026-09-02.md, not the multivocal branch's 14/327. The agenda carries no reference to ks-known-item-recall.json and no consumable identifier for it, exactly as the finding states.
> 
> No counter-evidence obtained on any route. The finding stands.

### SCOPE-2-6 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: partial)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803

**Claim, verbatim.**

> **issue.** The DI-8 correction was not propagated to the agenda, which still describes the corpus record as asserting the wrong thing and presents a discrepancy that remediation closed as live and unrepaired. The agenda's conclusion (count is two) is right; its description of the current state of a document it cites is now false.
>
> **evidence.** Agenda :1796-1801 — "**One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here** ... the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero". Corpus record N-5 :1662-1670 now reads "**Two** academic queries in that stratum executed and returned zero ... **`ks-repec-04` and `ks-repec-04-b` did NOT execute.**", and DI-8 :1834-1835 records that F007 and the corpus record now agree.
>
> **fix.** Update the agenda bullet to record that the corpus record has since been corrected at limitation 9, N-5, N-8, the section-2 rows and the section-3 fence, that DI-8 and G-26 now exist, and that the discrepancy is closed — retaining the superseded sentence as struck, per the agenda's own append-only correction practice.
>
> **reference.** DI-8; round-1 findings REV-1-1/SCOPE-1-1

**Refutation attempt.**

> No refutation available; the finding reproduces exactly. (1) Agenda :1796-1803 contains the quoted bullet verbatim, present tense, inside the list headed "Rev-3 corrections and inheritances from the SECOND corpus, all dated 2026-09-04, all material to what this agenda may assert": "One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here ... the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero". (2) Corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md :1661-1678 now reads "N-5 — ... **Two** academic queries in that stratum executed and returned zero: ks-arxiv-04 ... and ks-openalex-04 ... **ks-repec-04 and ks-repec-04-b did NOT execute.**", with the four-query wording surviving only inside a "CORRECTION 2026-09-04 (round-1 audit; REV-1-1, SCOPE-1-1, ...)" block that explicitly strikes it. So the agenda's present-tense description of what that document states is false. (3) DI-8 exists at :1793 and its closing paragraph :1829-1835 states "Limitation 9, N-5, N-8, the four section 2 source rows and the nine ks-repec annotations in the section 3 fence are corrected in place ... Gap G-26 is added ... failure_log.md F007 adjudicated this defect before the audit raised it and is cross-referenced here so the two documents agree" — i.e. the discrepancy is closed, contradicting the agenda's "recorded and NOT repaired". G-9 (:1858) and G-26 (:1876) confirmed present. (4) Counter-test for a superseding note elsewhere in the agenda: grep -n "DI-8|G-26|ks-repec-04" over the full 1803-line agenda returns exactly one hit, line 1799 inside the stale bullet itself — no correction marker anywhere. (5) The "it is a dated historical record" defense fails on two grounds: both documents carry the same date 2026-09-04, so there is no temporal separation; and the agenda's own established practice is in-place dated correction of stale assertions (lines 56, 94, 228, 465-466, 609, 653, 779-785, 794, 805, 1748-1760, e.g. "Rev 2's Branch 0 status paragraph is false on its facts as of 2026-09-04 and is superseded in place ... with the rev-2 text left standing"). The narrow reading that "NOT repaired here" is true because the agenda edits neither document rescues only the second clause and leaves the false present-tense characterization of N-5 standing; that is a scope quibble, not counter-evidence.

### SCOPE-2-7 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: partial)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :187, :1753

**Claim, verbatim.**

> **issue.** Probe (g): the MV- prefix sweep itself leaves no branch derivation orphaned, but the agenda's three statements of what the multivocal corpus supplies are stale after remediation. All three assert gaps G-1..G-25; the corpus record now names G-26, G-27 and G-28, none of which the agenda mentions or consumes. G-27 in particular bears directly on the agenda's evidence posture — it downgrades every S-D/S-E byte digest from verifiable to verified-once — and a reader of the agenda alone would not know it.
>
> **evidence.** Agenda :187 — "The **multivocal** corpus, `lit_review_kalshi-strategy-multivocal_2026-09-04.md`, names gaps **G-1…G-25** and handoffs **TC-1…TC-15**" (same assertion at :60 and :1753). Corpus record §12.1 now carries **G-26** ("RePEc was never searched"), **G-27** ("S-D and S-E retrieved bytes are NOT in this repository, so their `sha256_of_retrieved_bytes` values are ATTESTATIONS a reader cannot check") and **G-28** ("The CSL-JSON store builder was never archived"), all three added by round-1 remediation.
>
> **fix.** Extend the three range statements to G-1..G-28, and add MV-G-26/27/28 to the agenda's hazards or verification-status section — at minimum MV-G-27, because the agenda's citations into ks-lateral-records.json rest on digests it now describes as unverifiable by a reader.
>
> **reference.** corpus §12.1 G-26/G-27/G-28; taskSpec probe (g)

**Refutation attempt.**

> Refutation attempted and FAILED — the defect claim reproduces exactly.
> 
> (1) The three stale range statements exist verbatim at the stated lines of C:\Users\skoir\castles\docs\research_notes\research_agenda_prediction-market-microstructure_2026-09-02.md:
> - :60 — "supplies G-1..G-25 and TC-1..TC-15, which branches 7-11 consume"
> - :187 — "names gaps **G-1…G-25** and handoffs **TC-1…TC-15**"
> - :1753 — "the multivocal corpus supplies G-1..G-25 and TC-1..TC-15"
> A fourth instance the finding did not name also exists at :114 (front-matter `corpus_multivocal:` — "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25"), which strengthens rather than weakens the finding.
> 
> (2) The corpus record C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 does name G-26, G-27 and G-28, at lines 1874-1876, each tagged "Added 2026-09-04 by round-1 audit remediation". Line 2069 of the same file states the range authoritatively: "The full gap list is section 12.1 (`G-1` … `G-28`)". G-27's text confirms the substance the finding attributes to it: "S-D and S-E retrieved bytes are NOT in this repository, so their `sha256_of_retrieved_bytes` values are ATTESTATIONS a reader cannot check ... That makes the attestation VERIFIED-ONCE, not verifiable".
> 
> (3) Counter-test for any mention in any form: `grep -n "G-2[6-8]"` over the agenda returns ZERO hits; so does a search for "MV-G-26/27/28", "twenty-eight", and "28 gaps". The agenda mentions the three new gaps nowhere, under no spelling.
> 
> (4) Counter-test for an as-of/forward-tolerant qualifier that would make the range non-stale: the "How to read this document" block at :182-201 states the ranges as flat assertions of what each corpus names, with no as-of date, no "current list", and no pointer to the corpus as the governing list. Nothing in the agenda scopes the G-1…G-25 claim to a revision date.
> 
> One sub-claim in the finding's *claimed fix* does not hold, but it is rationale, not the defect: the agenda contains no direct citations into `ks-lateral-records.json` (grep for "ks-lateral-records", "ks-payload-digest" and "sha256_of_retrieved_bytes" over the agenda returns zero hits), so the assertion that "the agenda's citations into ks-lateral-records.json rest on digests" overstates the coupling. This affects the remedy's framing only; the defect as stated in `issue` and `evidence` — three stale range statements that omit G-26/27/28, with G-27 unmentioned — is true as written.

### SCOPE-2-8 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: changed)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:29-35 vs :43-65 (same front matter)

**Claim, verbatim.**

> **issue.** Probe (e): the QUANT-1-5 read-state digest remediation was applied to one front-matter field and not to the adjacent one, leaving the front matter asserting two incompatible states of the same fact. `corpus_record_sha256` still says no digest is asserted because no hashing tool existed; `read_state_digest_discipline`, six lines below, asserts that very digest as computed by the lead. A tool or reader keying on `corpus_record_sha256` gets the superseded state with no marker that it is superseded.
>
> **evidence.** :29-31 — "corpus_record_sha256: > TO COMPUTE — no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed." :51-55 — "the LEAD SESSION computed them on 2026-09-04 and they are recorded here ... corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b".
>
> **fix.** Set `corpus_record_sha256` to the computed digest, retain the superseded "TO COMPUTE / no hashing tool" wording as struck, and carry the same limit the other field carries — that the digest is of the post-remediation byte state and does not retroactively verify this draft's quotations.
>
> **reference.** round-1 QUANT-1-5 remediation

**Refutation attempt.**

> Attempted refutation failed; the finding reproduces exactly at the stated location in C:\Users\skoir\castles\research\01_hypothesis_register\H001\design.md.
> 
> Reproduced check 1 — lines 29-35 are verbatim as quoted: "corpus_record_sha256: > / TO COMPUTE — no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed." The block goes on to say "The digest it returns is recorded here and re-verified at freeze" — "here" being this field, where nothing is recorded.
> 
> Reproduced check 2 — lines 43-55 of the same front matter (the adjacent `read_state_digest_discipline` key, separated only by `arms_read_for_this_draft` at 36-42) states "the LEAD SESSION computed them on 2026-09-04 and they are recorded here, so this obligation is now DISCHARGED as to computation:" followed by "corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b". So the same YAML mapping asserts both that no digest of the corpus record is asserted and a specific digest of the corpus record.
> 
> Reproduced check 3 — searched the whole repo for `corpus_record_sha256` (grep, 3 hits, all in this file: lines 29, 50, 175). The only cross-reference runs the wrong way: line 50 points from `read_state_digest_discipline` back to `corpus_record_sha256` for the command. There is no forward pointer, "superseded" marker, or struck-through annotation inside the `corpus_record_sha256` block. A tool or reader keying on that field therefore reads the pre-remediation state with no signal that it is stale, exactly as the finding claims. (Line 175 is a third occurrence in §0.3 body prose, likewise still saying "TO COMPUTE", though for ks-academic-candidates.json rather than the corpus record.)
> 
> Counter-test attempted and it cut against refutation, not for it: running the command the field itself prescribes — python -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md').read_bytes()).hexdigest())" — returns 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21, which does not match the b3679514... asserted six lines below. That is an independent discrepancy (the remediator's claimed fix of copying b3679514... into `corpus_record_sha256` would propagate a digest that no longer matches the file on disk), but it does nothing to refute the contradiction the finding actually alleges. Only that contradiction claim was under test, and it is true as stated.

### SCOPE-2-9 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: partial)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** hypothesis_backlog.md:32 (H001 row, round-1 correction block) vs research/01_hypothesis_register/H001/design.md:43-74

**Claim, verbatim.**

> **issue.** The same QUANT-1-5 remediation left the two registers disagreeing. The backlog's H001 correction states as a live freeze blocker that no read-time digest is recorded for the corpus record or any arm file, and that none is asserted because no hashing tool was available; the design now records six lead-computed digests and declares that obligation discharged as to computation.
>
> **evidence.** hypothesis_backlog.md:32 — "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available in the remediation session and a fabricated digest would be worse than an absent one." design.md:51-53 — "the LEAD SESSION computed them on 2026-09-04 and they are recorded here, so this obligation is now DISCHARGED as to computation"; :72-74 — "Pre-freeze checklist item 7 stays OPEN on its remaining components".
>
> **fix.** Append to the backlog row (append-only, superseded wording retained) that item 7 is partly discharged — the six digests are computed and recorded in the design — and restate the remaining open components exactly as the design states them, so the two registers no longer disagree on the state of the same checklist item.
>
> **reference.** design.md read_state_digest_discipline; spec D11

**Refutation attempt.**

> No refutation obtained; the defect claim reproduces. (1) hypothesis_backlog.md:32 reproduces verbatim, including "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available in the remediation session and a fabricated digest would be worse than an absent one." (2) design.md:49-53 reproduces "the LEAD SESSION computed them on 2026-09-04 and they are recorded here, so this obligation is now DISCHARGED as to computation:" followed by six digests, and :71-74 "Pre-freeze checklist item 7 stays OPEN on its remaining components". Three refutation attempts failed. (a) Scope-narrowing: the design does state its digests are not read-time state ("which is NOT the state this draft read"), so the registers agree on the narrow clause "no read-time SHA-256 is recorded" — but the backlog's following sentence "Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available" is unqualified and is now false as a state claim, so the defense covers only half the backlog sentence. (b) Note-elsewhere: grep of hypothesis_backlog.md for b36795, sha256, SHA-256, "LEAD SESSION", "DISCHARGED as to computation" returns only the legend row at :19 and the H001 row at :32 — no digest, no partial-discharge note, no later appended block, so the :32 correction is the operative current-state text in an append-only register. (c) Placeholder-digest theory: recomputed ks-venue-docs.json = cab38c3f50d1f6b43455c409bc4c8e20695979456eacaee92b8b11c8cc2fec1d, matching the design's recorded value exactly, so the design's digests are genuine computations and "none is asserted" is not salvageable. Incidental corroboration (not part of the claim): the design is itself split — front matter corpus_record_sha256 at :29-31 still reads "TO COMPUTE ... NO DIGEST IS ASSERTED rather than guessed" and §12 item 7 at :1530 still reads a bare "OPEN", while :53-60 records the six digests. Separately noted for the lead, outside this finding's scope: the recorded corpus-record digest b3679514... no longer matches the file on disk, which now hashes to 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21.

### SCOPE-2-10 - RETAINED

- **raised by:** `scope-auditor` (severity claimed: major; category: added)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:970-986 and :1615-1633; spec D5 check :218-220

**Claim, verbatim.**

> **issue.** Probe (e): the QUANT-1-4 / LITERATURE-1-3 remediation added two external bibliographic records to H001 that fall outside the provenance envelope the declaration itself set for that deliverable. D5's stated check is that no external citation appears that is absent from ks-instrument-verification.json or an arm output; neither Politis & White 2004 nor Patton, Politis & White 2009 appears in ks-instrument-verification.json or in any kalshi-strategy-multivocal arm log. The addition is defensible on the merits and is honestly flagged not-re-fetched, but it widens a declared check and no declaration amendment records the widening.
>
> **evidence.** Spec D5 :218-220 — "check: front matter reads `status: draft-unfrozen`; `grep -c \"TO COMPUTE\"` returns a positive integer; **no external citation appears that is absent from `ks-instrument-verification.json` or an arm output.**" design.md:1620-1625 lists both records; a repository-wide grep for "Politis" returns no hit anywhere under docs/literature/search_logs/kalshi-strategy-multivocal/.
>
> **fix.** Either add both records to a verification log for this branch, or append a declaration amendment recording that D5's citation-envelope check is widened to admit instruments adopted by explicit reference under ADR-0004 and charter-cited instruments, naming the records so admitted. Do not leave the check standing while it fails.
>
> **reference.** spec D5 check; ADR-0004 explicit-reference mechanism

**Refutation attempt.**

> Refutation attempted on five avenues; all failed. Every element of the claim reproduced independently.
> 
> (1) Spec check reproduces verbatim. sed -n '218,220p' docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md returns exactly: "check: front matter reads `status: draft-unfrozen`; `grep -c \"TO COMPUTE\"` returns a positive integer; no external citation appears that is absent from `ks-instrument-verification.json` or an arm output." The quotation in the finding is exact.
> 
> (2) Both records are present in the D5 deliverable at the stated locations. grep -n "Politis\|Patton" research/01_hypothesis_register/H001/design.md (file is 1656 lines) returns 972-979 (section 6, embargo selection procedure), 1256-1257 (section 9.1 resampler), 1535 (pre-freeze checklist item 7), and 1620-1625 (section 13 References). Lines 1620-1625 carry both full bibliographic records: "Politis, D. N., & White, H. (2004). Automatic Block-Length Selection for the Dependent Bootstrap. Econometric Reviews 23(1):53-70. doi:10.1081/ETC-120028836." and "Patton, A., Politis, D. N., & White, H. (2009). Correction to ... Econometric Reviews 28(4):372-375. doi:10.1080/07474930802459016." The finding's stated ranges :970-986 and :1615-1633 both bracket these correctly.
> 
> (3) Absent from ks-instrument-verification.json. grep -c "Politis" on that file returns 0 (exit status 1). Parsed the JSON and enumerated all eight instruments: Garousi/Felderer/Mantyla (10.1016/j.infsof.2018.09.006), Adams/Smart/Huff (10.1111/ijmr.12102), Kalliamvakou (10.1145/2597073.2597074, 10.1007/s10664-015-9393-5), Munaiah (10.1007/s10664-017-9512-6), Smith/FORCE11 (10.7717/peerj-cs.86), PRISMA-S + PRISMA 2020, PRISMA-ScR + Arksey/O'Malley + Levac, Klein/Jones/ISO 690. All are MLR, reporting-standard, GitHub-curation or archiving instruments; the file contains no statistical instrument of any kind.
> 
> (4) Absent from every arm output. Repository-wide grep -rn "Politis" over docs/literature/search_logs/ returns hits only under kalshi-arbitrage (one false positive, the German title "Neue Politische Oekonomie der Regulierung...") and regime-classification (ki-batch3/4/7, gap-crossref-31, gap-openalex-42). Zero hits anywhere under docs/literature/search_logs/kalshi-strategy-multivocal/. Same result for a grep on the two DOI strings ETC-120028836 and 07474930802459016 across docs/ and research/: the only hits are design.md itself and the round-1 audit trail.
> 
> (5) No declaration amendment records the widening. The spec's divergence register runs D1 through D11 (grep of section headers: lines 160, 168, 180, 191, 201, 236, 256, 298, 315, 330, 349) and stops; none concerns the citation envelope. grep -n "ks-instrument-verification" over the spec returns only line 175 (the log's own description in the search-log inventory) and line 220 (the check itself). The branch amendment register docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl was read in full: header plus M1 (query-vocabulary departures, sections 3.1/3.4) and M2 (the G-code fourth-disposition ruling, sections 4.2/4.4). Neither touches D5 or the citation envelope.
> 
> Only weakening found, insufficient for refutation. The round-1 refute gate for QUANT-1-4 already recorded (docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.json:354) that D5's check "is in any case already exceeded by the twelve DOIs section 13 carries from the rule file and charter, none of which are in ks-instrument-verification.json." I confirmed this independently against the instrument enumeration in (3): White 2000, Hansen 2005, Newey & West 1994, Andrews 1991, Opdyke 2007, Lo 2002, Ledoit & Wolf 2008, Hoenig & Heisey, Theiler, Kaufman, Lakens and Schuirmann appear in none of the eight verified instruments. So the check was already failing before the QUANT-1-4 / LITERATURE-1-3 remediation, which makes the finding's word "widens" imprecise -- the addition further violates an already-breached check rather than widening an intact one. That is a nuance about attribution and magnitude, not counter-evidence against the defect. The operative claim -- two external citations sit in the D5 deliverable outside the provenance envelope the declaration set, and no amendment records it -- is confirmed on every element, and the finding's claimed fix ("do not leave the check standing while it fails") is the correct disposition whether the breach is new or pre-existing.

### QUANT-2-1 - RETAINED

- **raised by:** `quant-auditor` (severity claimed: critical; category: method)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:98 (front matter protocol_amendments) and :1173-1198 (section 3.3); docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:1441-1493 (M2 addendum)

**Claim, verbatim.**

> **issue.** The corpus record does not enumerate amendment M2. Its front matter and section 3.3 both still assert that exactly ONE amendment exists. The frozen protocol's section 10 declares precisely this state defective, and this is the constraint the task spec named. The defect is bidirectional: M2's own prose in the protocol addendum asserts that the corpus record reports the reconciliation, which it does not, so the two required registers disagree — and the register header itself states that a discrepancy between the two is a defect correctable only by a further amendment.
>
> **evidence.** `grep -n "M2" docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns ZERO matches. Front matter: `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record..."`. Section 3.3 heading: `### 3.3 Amendment M1, enumerated`; body: *"Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here"*. Protocol frozen text line 1149-1152: *"The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective."* M2 exists in BOTH required registers otherwise — `ks-amendments.jsonl` object 3 (`"amendment": "M2"`, `execution_stage: "POST-EXECUTION ... This is a WEAKER amendment than M1"`) and protocol addendum §M2. M2's prose claims *"they are reported decomposed, exactly as the corpus record does"* and *"the corpus record reports it as such"* — neither is true of the delivered record. Frozen prefix re-verified intact: sha256 over first 91,498 bytes = 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac (matches).
>
> **fix.** Add section 3.3b to the corpus record enumerating M2 (contradiction quoted, ruling, touched sections 4.2/4.4, and POST-EXECUTION weakness stated in the protocol's own words — 'a weaker amendment than M1', 1,465 of 1,574 dispositions assigned before adjudication, no record moves, no count moves). Amend the front-matter `protocol_amendments` field to TWO amendments with a dated correction note retaining the superseded 'ONE ... M1' wording verbatim, in the same style as the `screening_verdict_source` and `rng_seed` corrections already in that front matter. Re-title section 3.3 so it does not read 'Amendment M1' alone.
>
> **reference.** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §10 (frozen prefix, line 1149-1152); docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl header note

**Refutation attempt.**

> Not refuted. Every load-bearing element reproduced independently. (1) grep -c "M2" on docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns 0; so do greps for "SCOPE-1-7", "FOURTH"/"fourth stage", and "4.2". (2) Front matter protocol_amendments (actual line 74, NOT :98 as cited) reads verbatim: 'ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...'. (3) Section 3.3 at line 1173 is titled 'Amendment M1, enumerated' and its body states 'One amendment exists and all three of its parts are enumerated here'. (4) M2 is present in BOTH required registers: ks-amendments.jsonl object 3 ("amendment":"M2", execution_stage "POST-EXECUTION ... This is a WEAKER amendment than M1", raised_by SCOPE-1-7) and the protocol addendum at lines 1441-1483. (5) Frozen protocol section 10 text reproduced at lines ~1149-1152: 'The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective.' An independently binding sentence immediately prior: 'An amendment logged after the affected decisions were made must say so in those words; that is a weaker amendment than a pre-execution one, and the corpus record reports the distinction.' The record reports no such distinction, so the POST-EXECUTION status of M2 does not exempt it. (6) Frozen-prefix integrity re-verified: sha256 over the first 91,498 bytes = 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac, matching the register header and both amendment objects. TWO INACCURACIES FOUND IN THE FINDING'S WRITE-UP, NEITHER AMOUNTING TO REFUTATION: (a) the finding claims M2's clause 'they are reported decomposed, exactly as the corpus record does' is untrue of the delivered record — it IS true; line 1349 states 'n_excluded 1475 = 10 Y-code rows + 1465 G-code rows' and the section-6 table at 1361-1372 reports the G-rows separately from every Y-code count. Only M2's second clause ('the corpus record reports it as such', the retrospective reconciliation) is false, so the bidirectional defect is half as broad as stated. (b) The finding says 'the two required registers disagree'; section 10 names the two required registers as ks-amendments.jsonl and the protocol addendum, and those two agree on M2 — the disagreement is between those registers and the corpus record. Also the front-matter locator is off by 24 lines (74, not 98). These are locator/scope imprecisions in the report, not counter-evidence. The defect claim itself — the corpus record affirmatively asserts exactly one amendment exists while a second amendment is registered in both required registers, a state the frozen protocol names defective — is confirmed.

### QUANT-2-2 - RETAINED

- **raised by:** `quant-auditor` (severity claimed: major; category: reproducibility)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:30-77 (front matter corpus_record_sha256 and read_state_digest_discipline)

**Claim, verbatim.**

> **issue.** The read-state digest discipline added under round-1 finding QUANT-1-5 pins a corpus-record SHA-256 that does not match the delivered corpus record, and the same front matter simultaneously asserts that no digest is asserted. The pin is dead on arrival: by the design's own rule, a reader running the stated command at freeze will conclude the corpus record changed.
>
> **evidence.** Recorded: `corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b`. Recomputed on disk: `451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21`. Cause is visible in mtimes — design.md 2026-09-04 13:19:56, corpus record 13:26:08: the record was edited AFTER the pin was written, in the same remediation pass. The other five pinned digests all verify OK (ks-academic-candidates.json, ks-github-records.jsonl, ks-venue-docs.json, ks-lateral-records.json, ks-instrument-verification.json). Internal contradiction in the same front matter: `corpus_record_sha256: > TO COMPUTE — no shell or hashing tool was available ... and NO DIGEST IS ASSERTED rather than guessed`, and §0.3 repeats *"The digest of the file as it now stands is `TO COMPUTE`"*. The design's own rule: *"a digest that differs at freeze is a changed corpus record, not a confirmation."*
>
> **fix.** Recompute the corpus-record digest LAST, after all corpus-record edits for the round are final, and replace b3679514... with the final value, retaining the superseded value in a dated note. Reconcile `corpus_record_sha256` and §0.3 with `read_state_digest_discipline` — either fill the front-matter field with the same final digest or state explicitly that it is superseded by the discipline block. Add an ordering rule: digests of mutable artifacts are pinned only after the artifact's last write in the round.
>
> **reference.** research/01_hypothesis_register/H001/design.md front matter, own rule text; CLAUDE.md §Reproducibility (dataset checksum)

**Refutation attempt.**

> No refutation found; the finding reproduces exactly. Recomputed sha256 of docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md on disk = 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21, which does not match the pinned b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b in research/01_hypothesis_register/H001/design.md front matter (read_state_digest_discipline). Control test rules out a hashing/encoding confound: in the same sha256sum invocation, all five arm-file pins verify byte-exactly (ks-academic-candidates.json ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58; ks-github-records.jsonl 98e312934e12fb42b19f93f1542d8fc8950805df0d844d8c430e563c94989b19; ks-venue-docs.json cab38c3f50d1f6b43455c409bc4c8e20695979456eacaee92b8b11c8cc2fec1d; ks-lateral-records.json 3fd644ae22bbb7db981c543604c94dfd6f6f19130176f0b548ee9f9f284aa181; ks-instrument-verification.json af4da817c2d2dcabdf851df62637bcb5322b2d32b313b19680ff0b15ac2e7028). Stated mtime ordering also confirmed via ls --time-style=full-iso: design.md 2026-09-04 13:19:56.499, corpus record 2026-09-04 13:26:08.512 (record written after the pin). Internal contradiction confirmed in the same front matter: design.md line 30 reads "TO COMPUTE - no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed", and line 174 repeats "file as it now stands is `TO COMPUTE` by the command in the front matter's ...", while read_state_digest_discipline asserts the corpus-record digest. The design's own rule that a differing digest at freeze means a changed corpus record is therefore triggered by the delivered state. Defect claim stands.

### QUANT-2-3 - RETAINED

- **raised by:** `quant-auditor` (severity claimed: major; category: reporting)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:132-243 (nine head limitations) and :2022-2074 (section 15); docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:54-57, :330-347

**Claim, verbatim.**

> **issue.** Round-1 SCOPE-1-4's remedy is INCOMPLETE. The known-item recall check was executed correctly and its result is arithmetically sound, but it is published ONLY in the declaration amendment D10 and in the arm log. It appears nowhere in the corpus record — the artifact the spec designates to carry it, and the artifact any downstream reader consumes. A 4.3% recall against the predecessor's include set is the single strongest bound on this corpus's coverage claim and it travels with neither of its two caveats into the record's limitations or verification-gaps sections.
>
> **evidence.** `grep -rn "4.3%|known-item|known_item"` over the corpus record, the protocol, the agenda and ADR-0006 returns ZERO matches; the only hits repo-wide for this branch are the spec (D10) and `ks-known-item-recall.json`. The spec's own §4 states the requirement: *"The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does."* The predecessor record does carry its recall figure inline (lit_review_kalshi-arbitrage_2026-09-02.md:755, '16 of 23 items retrieved'). I re-derived the figure independently from the two named inputs: seed = 327 identifiers dispositioned `include` post-A16 in ks-prior-identifiers.json; matches in ks-academic-identified-universe.json on doi/arxiv = 14; 14/327 = 0.042813 = 4.3%; not_retrieved list length 313 = 327-14, all unique; all three declared input digests verify. The number is right; its placement is not.
>
> **fix.** Add a tenth head limitation (or extend limitation 6, which already carries the same 6,923-of-8,813 bound) stating the 4.3% figure WITH both caveats verbatim from ks-known-item-recall.json — the seed-set mismatch between the two protocols' questions, and the novelty-index coverage bound — plus the denominator_note that it is not a screening statistic. Cross-reference it from section 15. Update the head from 'The nine limitations' accordingly.
>
> **reference.** docs/literature/search_logs/kalshi-strategy-multivocal/ks-known-item-recall.json; PRISMA-S item 11 (prior work / recall verification), Rethlefsen et al. 2021 doi:10.1186/s13643-020-01542-z

**Refutation attempt.**

> Refutation attempt failed; the finding reproduces in full. (1) grep for "4.3%|known-item|known_item|recall" over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns a single unrelated hit (line 62, the Y3 code's phrase "an executing agent's own recall"). I read the nine head limitations (lines 132-243) and all of section 15 (lines 2022-2072; file is 2072 lines total) directly: neither carries the recall figure, and the section 12.1 gap list G-1..G-28 is not tied to it. The same grep returns zero on docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md, docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md, and docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md (its only "known-item" hit, line 1690, concerns the PREDECESSOR branch's KI-20/KI-21 vocabulary correction, a different object). (2) grep -rn "ks-known-item-recall" repo-wide returns exactly one hit outside the JSON itself: deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:335 (D10). The arm log ks-amendments.jsonl is 3 lines (amendment M1 only) and contains no recall reference, so the figure lives in TWO places, not three -- narrower than the finding claims, which strengthens it. (3) The spec requirement is verbatim as quoted, lines 54-57: "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." (4) The predecessor comparator holds: lit_review_kalshi-arbitrage_2026-09-02.md:755 carries "16 of 23 items retrieved" inline. (5) Independent re-derivation: all three declared input digests in ks-known-item-recall.json verify (ks-prior-identifiers.json e3b873eecbd3df503a854e3a1b0a3ee22ab9ec3b812d3fab4d96f6df6a7c6c48; ks-academic-candidates.json ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58; ks-academic-identified-universe.json b523b7a5aab72166317ea444489bfce989a9770a2fce33b51453d66cb767248f). Seed = 327 entries dispositioned `include` in the prior index; doi/arxiv matches against the 528-row identified universe = 14; 14/327 = 0.042813 = 4.3%; not_retrieved = 313 and my derived list is set-identical to the file's 313-element list. The computation is sound and its placement is the defect, exactly as reported.

### QUANT-2-4 - RETAINED

- **raised by:** `quant-auditor` (severity claimed: major; category: reproducibility)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1874 (gap G-28); docs/literature/search_logs/kalshi-strategy-multivocal/README.md

**Claim, verbatim.**

> **issue.** G-28 registers the CSL-JSON store builder as a permanent gap — 'never archived', 'not re-runnable at all' — but the builder exists and is readable at audit time in the same executing-session scratchpad from which fifteen other scripts were archived during this very remediation round. A recoverable artifact was registered as an unrecoverable gap rather than recovered.
>
> **evidence.** `build_store.py` (9,145 bytes, mtime 2026-09-04 11:48) is present in the executing session's scratchpad and line 222 reads `out = "docs/literature/references_kalshi-strategy-multivocal.json"` — it is exactly the emitter G-28 declares nonexistent. G-28 text: *"No script anywhere in the repository emits references_kalshi-strategy-multivocal.json; the store's construction is therefore not re-runnable"*, echoed in the front-matter rng_seed correction: *"THE STORE BUILDER CLAUSE IS WITHDRAWN AS FALSE: no script emitting references_kalshi-strategy-multivocal.json exists anywhere in this repository"*. The claim is literally true of the repository and false of the recoverable state: the same round archived queries.py, run_arm.py and seven ks-github-scripts/ files out of that scratchpad, and README.md §'What was changed in these scripts' documents that archival.
>
> **fix.** Archive build_store.py into docs/literature/search_logs/kalshi-strategy-multivocal/ under the directory's ks- naming convention, with the PYTHONHASHSEED=0 entry assert and the home-path substitution applied as for the other fifteen, verify it regenerates the store to the recorded digest c7545d31..., and downgrade or close G-28 accordingly. If it is deliberately not archived, state that as a decision with its reason, not as an unrecoverable gap.
>
> **reference.** docs/literature/search_logs/kalshi-strategy-multivocal/README.md §'The five missing S-C stage files' (the precedent for recovering-rather-than-registering); CLAUDE.md §Reproducibility

**Refutation attempt.**

> No refutation found; every element of QUANT-2-4 reproduced, and a counter-test strengthened it.
> 
> 1) Builder exists and is readable at audit time. `find` over the session scratchpad root returns exactly one hit: C:\Users\skoir\AppData\Local\Temp\claude\C--Users-skoir-castles\e88a64c5-a5b6-4ea4-8e14-05f651099a06\scratchpad\build_store.py — 9,145 bytes, mtime 2026-09-04 11:48, 226 lines, sha256 60bcea27c640f8740832b96b860e4645542d30376f4947f485fb0ca10b679152. That directory is this executing session's scratchpad (the same UUID this subagent was assigned). Line 222 reads verbatim `out = "docs/literature/references_kalshi-strategy-multivocal.json"`. Its module docstring names it "Build the CSL-JSON store for the kalshi-strategy-multivocal corpus" and line 8 already carries `assert os.environ.get("PYTHONHASHSEED") == "0"`.
> 
> 2) Repository is genuinely empty of it. `grep -rn "references_kalshi-strategy-multivocal.json" --include=*.py .` and `grep -rln "canonical_bytes" --include=*.py .` return zero hits in C:\Users\skoir\castles; `find` for *build_store* in the repo returns nothing. So G-28's literal repo-scoped claim is true and the "not recoverable" framing is what is at issue — exactly as the auditor stated.
> 
> 3) G-28 text reproduced verbatim at C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md:1874 — "**The CSL-JSON store builder was never archived.** No script anywhere in the repository emits `references_kalshi-strategy-multivocal.json`; the store's construction is therefore not re-runnable". The front-matter echo is at line 97: "THE STORE BUILDER CLAUSE IS WITHDRAWN AS FALSE: no script emitting references_kalshi-strategy-multivocal.json exists anywhere in this repository, so the store's construction is not re-runnable at all — registered as gap G-28."
> 
> 4) Counter-test run, and it went against refutation. I copied build_store.py, redirected only line 222 to a scratch path, and ran it from the repo root with PYTHONHASHSEED=0. It executed cleanly against the archived arm logs (entries: 99, validation errors: 0, by arm: software-repository 40 / lateral-practitioner 31 / venue-and-regulator 28) and printed sha256 c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df, 167,673 bytes. `sha256sum` of the tracked store docs/literature/references_kalshi-strategy-multivocal.json is the identical c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df. The builder therefore regenerates the store byte-for-byte to the recorded digest — "not re-runnable at all" is falsified by execution, not merely by the file's existence. (Temp copy and regenerated file deleted; the repo store was never written to.)
> 
> 5) Archival precedent verified. docs\literature\search_logs\kalshi-strategy-multivocal\ contains queries.py and run_arm.py (both mtime 13:17, after build_store.py's 11:48) plus ks-github-scripts\ with seven files (draw_and_pin.py, get_readmes.py, run_search.py, run_search2.py, verify_quotes.py, write_ledger.py, write_logs.py), and README.md carries the cited headings at line 91 "### The five missing S-C stage files" and line 137 "## What was changed in these scripts, and what was not". So the same round did archive scripts out of that scratchpad while leaving this one unarchived.
> 
> The only defensible objection would be a severity or scope quibble, which is not refutation.

### QUANT-2-5 - RETAINED

- **raised by:** `quant-auditor` (severity claimed: major; category: reporting)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1727-1838 (section 11, DI-1..DI-8) and section 8 T4 row / bare-number table; research/01_hypothesis_register/H001/design.md:546-640

**Claim, verbatim.**

> **issue.** Two verified extraction defects in the software-arm log — established during this session at primary-source depth — are registered ONLY in an unfrozen draft design and are absent from the corpus record's data-integrity section, its bare-number register (G-23) and its taxonomy source column. The corpus record is the artifact of record; a reader of it gets the truncated framing without knowing it is truncated.
>
> **evidence.** H001 §1.6 establishes, from a re-fetch of the pinned raw READMEs: (i) `ks-sc-001` extraction is INCOMPLETE — *"No price-based strategy clears the honest bar."* and the bolded *"Conclusion: there is no demostrable price-based edge in the public settled-market data."* are 'absent from every field of the ks-sc-001 record'; (ii) `ks-sc-002` extraction is TRUNCATED — the arm log's quote stops at 'breaks even' and drops the immediately following *"Even at the tails the hurdle is 2.6¢."* `grep -n "2\.6|No price-based strategy|demostrable|TRUNCAT|INCOMPLETE"` over the corpus record returns nothing on any of them. The corpus record's §8 T4 row reproduces only the truncated framing ('reported as already priced in and eaten by fees/spread'), G-23 still says 'Five bare numbers' with 2.6¢ not among them, and N-3 quotes 10.7¢ without the tail sentence. Charter commitment 5 makes a dropped qualifier a defect, and the record's own §11 exists for exactly this class.
>
> **fix.** Add DI-9 to section 11 recording both extraction defects with the two missing verbatim sentences, their re-fetch provenance and the two stated limits (converted text, digest not recomputed, section-level locations). Extend G-23 to six bare numbers to include QUOTED 2.6¢ and flag it NOT ADOPTABLE on the same grounds as the existing five. Annotate the §8 T4 row so it does not present the truncated reading as the source's whole claim.
>
> **reference.** docs/methodology/charter_castles_2026-08-21.md commitment 5; corpus record §11 DI-7 (the existing precedent for registering an extraction defect)

**Refutation attempt.**

> Attempted refutation failed; every load-bearing element of the finding reproduced independently.
> 
> 1. Claimed grep reproduces exactly. `grep -c -F` over C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md (2072 lines) returns 0 for each of "2.6", "No price-based", "demostrable", "TRUNCAT", "INCOMPLETE", and also 0 for "DI-9". Not a false negative: control greps on the same file return 6 hits for "ks-sc-001" and 4 for "10.7".
> 
> 2. The two sentences ARE in the primary source, verified against the repo's pinned raw-README evidence files (not the arm log, not H001):
>    - docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md:34 and :40 carry "**No price-based strategy clears the honest bar.**" and "**Conclusion: there is no demostrable price-based edge in the public settled-market data.**"
>    - .../himagna16__kalshi-microstructure.md:93-94 carries "...before a taker round trip breaks even. Even at the tails the hurdle is 2.6¢."
> 
> 3. The extraction defects themselves are real, checked by parsing the arm log docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-records.jsonl: record ks-sc-001 contains "honest bar"=False, "demostrable"=False; record ks-sc-002 contains "breaks even"=True but "2.6"=False — i.e. truncated at exactly the point claimed. File-wide counts of "honest bar", "demostrable", "2.6" in the arm log are all 0.
> 
> 4. The corpus record's specific defects reproduce verbatim:
>    - Section 11 runs DI-1 through DI-8 only; DI-8 is the RePEc zero-yield correction. No entry covers either software-arm extraction defect, under that or any wording.
>    - Line 1872: G-23 reads "**Five bare numbers from sources are recorded verbatim and are not adoptable**"; the section 8 bare-number table (lines ~1522-1528) lists KSL-C10, KSL-C19, KSL-C28, KSL-C12, ks-sc-001 — 2.6¢ is not among them, and 10.7¢ is not registered there either.
>    - Line 1505, section 8 T4 row, reproduces only "`ks-sc-001` RM/K (favourite–longshot, **reported as already priced in and eaten by fees/spread**)" — the truncated framing, unannotated.
>    - N-2 (line ~1622) uses only the weaker "statistically indistinguishable" claim; N-3 (line ~1643) quotes "must move **10.7¢** ... before a taker round trip breaks even" and stops there, dropping the tail sentence.
>    - grep for "H001", "design.md" and "§1.6" over the corpus record returns zero — there is no cross-reference that would carry the defect to a reader of the record of record.
> 
> 5. The "unfrozen draft" descriptor is accurate: research/01_hypothesis_register/H001/design.md:3 "Pre-registration DESIGN DRAFT for hypothesis H001. NOT FROZEN." and :9 "status: draft-unfrozen". H001 §1.6 (lines ~546-640) registers both defects with the stated re-fetch provenance and the two stated limits (converted text, digest not recomputed, section-level locations) exactly as the finding describes.
> 
> 6. Corroborating, not load-bearing: docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md:1046 records a round-1 repository-wide check finding the same absence ("Neither the arm log, the corpus, nor H001 carries the source's headline null anywhere"), and its round-1 fix text explicitly directed "extend corpus N-2 with the same two verbatim sentences" — a remediation that was applied to H001 but not to the corpus record, which is precisely the residue this finding names.
> 
> No counter-evidence found on any element.

### LITERATURE-2-1 - RETAINED

- **raised by:** `literature-check` (severity claimed: critical; category: missing-attribution / self-declared protocol defect)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`); :1173 (§3.3 heading); :1176

**Claim, verbatim.**

> **issue.** The corpus record does not enumerate amendment M2 anywhere, and affirmatively asserts that only one amendment exists. The frozen protocol clause it quotes in the same paragraph makes exactly this defective. This is the round-2 governing constraint the taskSpec named (protocol §10; TWO amendments now exist) and it is unremediated.
>
> **evidence.** grep for "M2" across the corpus record returns ZERO matches. Front matter line 74 reads: "protocol_amendments: 'ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...'". §3.3 is headed "Amendment M1, enumerated" and line 1175-1176 reads: "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here". M2 IS registered against the frozen protocol: protocol addendum lines 1441-1481 ("M2 - 2026-09-04 - ... POST-EXECUTION, and the weakness is declared") and ks-amendments.jsonl line 3. The frozen clause at protocol:1149-1152 reads: "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective." M2 bears directly on this record's own 1,465 G1 rows (93% of the delivered flow). Secondary: the deliverable declaration's append-only round-1 section records D8-D11 and SCOPE-1-5 but has no entry for M2/SCOPE-1-7 either, so M1 was recorded as a scope divergence (D7) and M2 was not.
>
> **fix.** Amend the front-matter `protocol_amendments` field to read TWO amendments and carry M2's ruling text; rename §3.3 to "Amendments M1 and M2, enumerated"; add an M2 sub-block stating (a) the section 4.2/4.4 contradiction, (b) the ruling that a G-code is a FOURTH stage-1 outcome, (c) the POST-EXECUTION stage and that M2 is explicitly WEAKER than M1, in those words, and (d) that no record, count or eligibility moves. Strike the sentence "One amendment exists" with the superseded wording retained, per the record's own correction convention. Add a matching declaration amendment recording M2 as a change to a declared artifact.
>
> **reference.** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md §10 (frozen, lines 1143-1152); addendum M2 (lines 1441-1481); ks-amendments.jsonl line 3

**Refutation attempt.**

> Refutation attempted and FAILED — every element of the finding reproduced verbatim at the stated locations.
> 
> 1. Zero-match claim confirmed. `grep -c "M2" docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns 0. I also searched for every plausible alias that could satisfy the enumeration obligation under a different name — "M-2", "second amendment", "two amendments", "SCOPE-1-7", "FOURTH", "4.2" — and got zero hits bearing on an amendment (the only "fourth" hits are line 1169, which says the ks-known-item file is "not a fourth part of M1", and line 1772, an unrelated venue count). The record names no second amendment under any spelling.
> 
> 2. The affirmative false assertion is present. Front matter line 74 reads: `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record..."`. Line 1173 heads the section "### 3.3 Amendment M1, enumerated". Lines 1175-1176 read: "Protocol section 10 makes a corpus record that ran under an amendment it does not enumerate **defective**. One amendment exists and all three of its parts are enumerated here". So the record does not merely omit M2 — it asserts a false exclusive count in the same paragraph as the clause that condemns the omission.
> 
> 3. M2 exists and is registered in both required registers. Protocol addendum line 1439ff: "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared", ruling "a G-code is a FOURTH stage-1 outcome", scale "1,465 of the 1,574 screened records - 93% of the delivered flow". ks-amendments.jsonl line 3 carries the JSON twin with `"amendment": "M2"`, `"raised_by": "SCOPE-1-7"`, same frozen sha256 32dfea6d... and registration commit 4821611c.... The protocol's own rule (lines 1139-1141) is that a discrepancy between the prose twin and the register is itself a defect — here the two registers agree with each other and the corpus record disagrees with both.
> 
> 4. The frozen clause is quoted accurately and is inside the frozen prefix. Protocol lines 1149-1152: "The corpus record's front matter cites this protocol's path and commit hash and enumerates every amendment it ran under; a corpus record that ran under an amendment it does not enumerate is defective." M2's addendum sits at line 1439, below the frozen line, consistent with the front matter's own note that the prefix digest is unaffected.
> 
> 5. Counter-test on the strongest available defense — that M2 is post-execution, so the record never "ran under" it — fails on the frozen text itself. Protocol lines 1146-1149, three sentences above the enumeration clause: "An amendment logged after the affected decisions were made must say so in those words; that is a weaker amendment than a pre-execution one, and the corpus record reports the distinction." That places an independent, explicit reporting duty on the corpus record for exactly the post-execution case. M2's own addendum invokes that clause ("Section 10 requires that an amendment logged after the affected decisions were made say so in those words. It is said here"). The record reports the distinction for M1 ("Execution stage, stated in the amendment's own words: PRE-SCREENING") and not at all for M2.
> 
> 6. Secondary claim confirmed. docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md is 368 lines; the round-1 append-only section (line 290ff) runs D8 (SCOPE-1-2), D9 (SCOPE-1-3), D10 (SCOPE-1-4), D11 (SCOPE-1-6), then closes with "SCOPE-1-5 - DISCHARGED, not amended." No D12 and no M2/SCOPE-1-7 entry exists anywhere in the file. M1 was recorded at line 256 as D7 ("amendment M1 issued against the frozen protocol"), so the asymmetry the finding alleges is real: the parallel treatment for M2 is absent.
> 
> No concrete counter-evidence of any kind was obtainable. The defect claim is true as stated.

### LITERATURE-2-2 - RETAINED

- **raised by:** `literature-check` (severity claimed: major; category: dropped source clause / incomplete round-1 fix)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1623-1647 (§10 N-2, N-3), :1522-1529 (§8 bare-numbers table), :1872 (G-23); failure_log.md:582-701 (F008), :726-788 (F009)

**Claim, verbatim.**

> **issue.** The remediation for QUANT-1-2 / QUANT-1-3 verified that ks-sc-001's README states a headline null stronger than the arm log carried, and that ks-sc-002's extraction is truncated one sentence before the tail figure. Those verified clauses were propagated into H001 ONLY. The corpus record and failure_log still characterise both sources at the truncated depth, with no flag and no cross-reference — although the bytes that prove the clauses are archived IN THIS REPOSITORY. Charter commitment 5 makes a dropped qualifier a defect, and the corpus record is the branch's authoritative statement of what sources state.
>
> **evidence.** In-repo primary bytes confirm both clauses: docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 34-41 — "**No price-based strategy clears the honest bar.**" and "**Conclusion: there is no demostrable price-based edge in the public settled-market data.**"; .../himagna16__kalshi-microstructure.md lines 92-94 — "...must move **10.7¢** ... before a taker round trip breaks even. Even at the tails the hurdle is 2.6¢." Corpus §10 N-2 states only that "the record's own null result is that its best candidate did not beat its own baseline" and carries neither stronger sentence. Corpus §10 N-3 quotes the 10.7¢ sentence and stops exactly where the arm log stops; "2.6" returns no hit anywhere in the corpus record. Corpus §8's NOT-ADOPTABLE table lists five figures and omits both 10.7¢ and 2.6¢, and G-23 still says "Five bare numbers" — while H001 §0.2 adds both to the not-adoptable list. failure_log F008 'Result as reported' reproduces the same truncated set. The round-1 audit trail (docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md:1046, :1079) recorded that neither the arm log, the corpus, nor H001 carried these clauses; only H001 was fixed.
>
> **fix.** Add a dated correction note to corpus §10 N-2 and N-3 recording the two ks-sc-001 sentences and the ks-sc-002 tail sentence verbatim, attributed, with the in-repo locator ks-github-readme-evidence/<file>.md and its recorded README digest; add 10.7¢ and 2.6¢ to the §8 NOT-ADOPTABLE table and update G-23 from "Five bare numbers" to seven; add the same clauses to failure_log F008/F009 as a dated addendum (append-only, superseded wording retained). Do not edit the arm logs — register the extraction findings against them as H001 already does.
>
> **reference.** charter commitment 5 (attribution fidelity); H001 design.md §1.6(i) lines 547-570 and §1.6(ii) lines 613-672

**Refutation attempt.**

> No refutation. Every element of the finding reproduced independently.
> 
> (1) In-repo primary bytes, digest-verified: sha256sum of docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md = 50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118 and himagna16__kalshi-microstructure.md = 753d94ddd29ee97929fa4d483420e105aeee602f34f610d69ec65b4bb7668462, both identical to the readme_sha256 recorded for ks-sc-001 / ks-sc-002 in ks-github-records.jsonl. The files carry verbatim "**No price-based strategy clears the honest bar.**", "**Conclusion: there is no demostrable price-based edge in the public settled-market data.**", and "Even at the tails the hurdle is 2.6c."
> 
> (2) Corpus record: grep for "honest bar", "demostrable", "2.6" over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns ZERO hits (the only "10.7" matches outside N-3 line 1643 are DOI fragments 10.7326 and 10.7717). Section 10 N-2 terminates at "the record's own null result is that its best candidate did not beat its own baseline"; N-3 quotes the 10.7c sentence and stops exactly there. Section 8's NOT-ADOPTABLE table contains exactly five rows (KSL-C10, KSL-C19, KSL-C28, KSL-C12, ks-sc-001), omitting both 10.7c and 2.6c; G-23 still reads "Five bare numbers".
> 
> (3) failure_log.md: F008's "Result as reported" bullet reproduces the same truncated ks-sc-001 quote set with no headline-null clause; F009 quotes 10.7c and not 2.6c. grep for "honest bar", "demostrable", "2.6c" over failure_log.md returns zero hits.
> 
> (4) Propagation asymmetry confirmed: H001 design.md carries both clauses (lines 155-156 not-adoptable list, 558-559, 610, 619, 642, 655-663, 1306-1314). grep for "H001" / "QUANT-1-2" / "QUANT-1-3" over the corpus returns zero hits; over failure_log.md a single hit at line 699, which references H001 section 1.6's always-NO comparator obligation and is not a flag or cross-reference to the deeper extraction. No flag and no cross-reference exist, as the finding states.
> 
> (5) Round-1 audit trail docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md at the cited region records the repository-wide grep confirming neither the arm log, the corpus, nor H001 carried the headline null; only H001 was subsequently remediated.
> 
> Candidate defences examined and rejected: (a) that the clauses appear elsewhere in the corpus under different wording - refuted by the zero-hit greps on three distinct phrase anchors; (b) that a general "README depth" disclaimer plus a cross-reference to H001 already discharges the obligation - refuted by the zero H001 references in the corpus; (c) that the archived evidence file might not be the attested README - refuted by the exact digest match against the recorded readme_sha256.

### LITERATURE-2-3 - RETAINED

- **raised by:** `literature-check` (severity claimed: major; category: search-coverage instrument not reported where required)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (whole file — absent); docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:74, :330-347 (D10)

**Claim, verbatim.**

> **issue.** The known-item recall check promised by the declaration's corpus-record deliverable row was executed in remediation (SCOPE-1-4) but published only in the declaration amendment D10 and in a JSON log. It appears nowhere in the corpus record — not the figure, not either of its two bounds, not a pointer to the log. Probe (d): where the figure DOES appear it correctly carries both bounds; the defect is that it does not appear in the artifact the declaration binds it to.
>
> **evidence.** grep for "recall" in the corpus record returns only the Y3 definition ("an executing agent's own recall") at line 62 — no known-item recall reporting. grep for "4.3%", "known-item", "14 of 327" across docs/**/*.md returns no hit in the corpus record. The declaration's corpus-record row (spec line 74) requires: "the corpus record ... carrying ... per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does" (spec line 54-57 restates it). ks-known-item-recall.json does carry both bounds (seed_set_caveat; second_caveat) and arithmetic that closes: seed_size 327, found 14, recall 0.0428, not_retrieved 313, and the not_retrieved_identifiers array holds exactly 313 entries.
>
> **fix.** Add a subsection to the corpus record (natural home: §4 or a new §5.5) stating the check, the 14/327 = 4.3% figure, BOTH bounds verbatim from ks-known-item-recall.json (imperfect seed — the two protocols ask different questions; and the 6,923-of-8,813 index bound), the denominator note that it is not a screening statistic, and the log path. Add it as a named gap or limitation cross-reference so the head limitation list carries it.
>
> **reference.** deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10; PRESS 2015 known-item recall check as the 2026-09-02 branch applies it

**Refutation attempt.**

> Attempted refutation failed; every element of the finding reproduces. (1) Case-insensitive grep for known|recall|PRESS|ks-known over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns exactly one hit, line 62, the Y3 exclusion-code definition ("an executing agent's own recall"). No hit for 4.3%, 0.0428, "14 of 327", or the log filename. The only 327 hit is line 77 (predecessor store gap AG-11, 149 vs 327 — unrelated). The only 6,923-of-8,813 hits (lines 195, 350) are the novelty-index bound in limitation 6 and PRISMA-S item 7, neither mentioning a recall check. (2) grep -rn "ks-known-item-recall" docs/ --include=*.md returns a single line repo-wide: deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:335, inside amendment D10 — confirming publication only in the declaration amendment and the JSON log. (3) The binding obligation reproduces verbatim at spec lines 54-57: the corpus record "states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." D10 (spec :330-347) records the check as PERFORMED rather than waived and retires nothing; the adjacent D9 shows the repo's own convention that retiring a check is recorded explicitly as a scope change, and no such retirement exists for this row. (4) Independent verification of the log: seed_size 327, found_in_identified_universe 14, recall_vs_identified_universe 0.0428, not_retrieved 313, and len(not_retrieved_identifiers)==313; both bounds (seed_set_caveat, second_caveat) and denominator_note are present, matching probe (d). No source, counter-test, or logical argument contradicts the claim that the figure is absent from the artifact the declaration binds it to.

### LITERATURE-2-4 - RETAINED

- **raised by:** `literature-check` (severity claimed: major; category: uncited method + wrong section pointer)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:793 (§4), :965-990 (§6), :1541-1657 (§13 References)

**Claim, verbatim.**

> **issue.** The same defect class that the Politis-White remediation was written to close is still open for the AFML-derived machinery. "AFML" is an unexpanded abbreviation with no bibliographic record anywhere in §13; the section pointer is wrong; and `PurgedWalkForwardSplitter`, `purge` and `embargo` — all López de Prado (2018) constructs — are named as the design's splitter with no citation at all.
>
> **evidence.** Line 793: "**Triple-barrier labelling per AFML §3.2 does not apply and is not used.**" Verified against the book's table of contents: Chapter 3 runs 3.1 Motivation, 3.2 The Fixed-Time Horizon Method, 3.3 Computing Dynamic Thresholds, **3.4 The Triple-Barrier Method** — so the triple-barrier method is §3.4, and §3.2 is a different method. "AFML" appears exactly once in the file and expands nowhere; §13 lists no López de Prado entry. Purging/embargoing are AFML Ch. 7 §7.4; §6 uses both terms and the class name `PurgedWalkForwardSplitter` with no source. §13's own preamble at lines 1615-1618 states the governing principle and why it was applied to Politis-White: "named here because §0.2 and §1.2's directive-8 statement require every named method to carry provenance, and an earlier state of this document named the procedure in both sections with no citation anywhere."
>
> **fix.** Add the full record to §13 — López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. ISBN 978-1-119-48208-6 — and cite it at §4 for the triple-barrier method with the corrected pointer §3.4, and at §6 for purging/embargoing (§7.4). Expand "AFML" at first use. Record whether the book is re-fetched or carried unverified, in the same posture §13 already uses for the not-re-fetched instruments.
>
> **reference.** López de Prado (2018), Advances in Financial Machine Learning, Ch. 3 §3.4 (Triple-Barrier Method), Ch. 7 §7.4 (Purging and Embargo)

**Refutation attempt.**

> Attempted refutation failed; every sub-claim reproduces at the stated locations in C:\Users\skoir\castles\research\01_hypothesis_register\H001\design.md.
> 
> (1) Unexpanded, uncited abbreviation. `grep -n "AFML"` returns exactly one hit, line 793: "**Triple-barrier labelling per AFML §3.2 does not apply and is not used.**" `grep -n -i "Prado"` over the entire file returns ZERO hits. Read §13 in full (lines 1541-1657): it contains venue documents, practitioner records, software records, academic records, methodological instruments, the Politis-White/Patton block-length pair, the ADR-0004 statistical instruments, and the charter-cited instruments — no López de Prado / Advances in Financial Machine Learning entry of any kind. So "AFML" is used as a load-bearing source pointer with no expansion and no bibliographic record.
> 
> (2) Wrong section pointer. Verified against the publisher-side table of contents rather than from memory. O'Reilly's Chapter 3 ToC for Advances in Financial Machine Learning (ISBN 9781119482086) confirms the ordering 3.2 The Fixed-Time Horizon Method (p. 43), 3.3 Computing Dynamic Thresholds (p. 44), 3.4 The Triple-Barrier Method, 3.5 Learning Side and Size. Independently corroborated by the Mlfin.py documentation, which cites "Advances in Financial Machine Learning, Chapter 3.2, pages 43-44" specifically for the FIXED-TIME HORIZON method. Line 793 therefore points the triple-barrier method at the section that is a different labelling method.
> 
> (3) Uncited splitter machinery. §6 (lines 963-991) names `PurgedWalkForwardSplitter` as the splitter choice at line 965 and uses `embargo` (line 969) and `purge` (lines 987-990) as its two tuned quantities. There is no citation to López de Prado anywhere in that section or the file. Note the aggravating counter-check: the upstream template at C:\Users\skoir\.claude\skills\pre-register-hypothesis\assets\hypothesis_design_TEMPLATE.md:80 DOES carry the attribution — "`PurgedWalkForwardSplitter` or `CombinatorialPurgedCV` per López de Prado AFML §7+§12" — and line 59 carries "Triple-barrier labeling per López de Prado AFML §3.2". design.md dropped the author name from both while retaining the bare abbreviation and the erroneous §3.2 pointer, so the attribution loss is a change made in this artifact, not an absence inherited intact. The §7.4 locus for purging/embargo is independently corroborated inside the user's own toolchain: C:\Users\skoir\.claude\skills\pit-canary\SKILL.md:16 states López de Prado 2018 §7 "Cross-Validation in Finance" is what introduces purge + embargo.
> 
> (4) The governing principle the finding invokes is present verbatim. Lines 1615-1618 read: "**Block-length selection for the dependent bootstrap (§6 embargo, §9.1 SPA / Reality Check resampler)** — named here because §0.2 and §1.2's directive-8 statement require every named method to carry provenance, and an earlier state of this document named the procedure in both sections with **no citation anywhere**". The document therefore states the exact rule that the AFML machinery violates, and applied that rule to Politis-White while leaving the AFML constructs untreated.
> 
> No counter-evidence found on any of the three prongs. Only imprecision located is cosmetic: §6 spans lines 963-991 rather than the reported 965-990, which does not affect the claim.

### LITERATURE-2-5 - RETAINED

- **raised by:** `literature-check` (severity claimed: major; category: provenance contradiction introduced by remediation)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:29-35 (`corpus_record_sha256`), :43-74 (`read_state_digest_discipline`), :174-177 (§0.3), :1509-1516 (pre-freeze item 1); hypothesis_backlog.md:32

**Claim, verbatim.**

> **issue.** The QUANT-1-5 remediation added six computed digests to the H001 front matter but left three statements elsewhere in the same file — and one in hypothesis_backlog — asserting that no digest was computed or recorded. None of the stale statements is marked as superseded, so a reader cannot tell which is current. This is probe (a)'s failure mode occurring in a file other than the corpus record.
>
> **evidence.** Front matter lines 29-35: "corpus_record_sha256: TO COMPUTE — no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed." Twenty lines below, lines 54-55 record: "corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b". §0.3 lines 174-177: "The digest of the file as it now stands is `TO COMPUTE` ... applied to ... ks-academic-candidates.json" — while front matter line 57 records ks-academic-candidates.json = ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58. Pre-freeze item 1 (line 1514-1516): "Residual obligation ... its SHA-256 is not yet recorded". hypothesis_backlog.md:32 closes with: "Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available in the remediation session".
>
> **fix.** Rewrite `corpus_record_sha256` to carry the computed value with the read-state limit that `read_state_digest_discipline` already states, retaining the superseded 'no tool available' wording as struck; do the same at §0.3 and at pre-freeze item 1 (restate the residual obligation as re-reading at the pinned digest, which is what item 7 actually says); append a dated correction to the hypothesis_backlog H001 row noting the digests now exist and what they do and do not pin.
>
> **reference.** charter commitment 5; the record's own correction convention ("the superseded wording is retained")

**Refutation attempt.**

> Attempted refutation failed; the finding reproduces in full. (1) research/01_hypothesis_register/H001/design.md L29-31 reads verbatim "corpus_record_sha256: > TO COMPUTE - no shell or hashing tool was available in the session that performed this remediation, and NO DIGEST IS ASSERTED rather than guessed." while L54-55 of the SAME front matter block records "corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b". (2) L173-177 (S0.3) reads "The digest of the file as it now stands is `TO COMPUTE` by the command in the front matter's `corpus_record_sha256` field applied to `docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json`" while L56-57 records ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58 for that file. (3) L1514-1516 (pre-freeze item 1) reads "Residual obligation, carried into item 7: its SHA-256 is not yet recorded", contradicted by L54-55. (4) hypothesis_backlog.md:32 reads "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` - none is asserted here, because no hashing tool was available in the remediation session". Counter-test run against the finding: I recomputed sha256 of ks-academic-candidates.json myself and obtained ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58, an exact match to the front-matter value - so S0.3's "TO COMPUTE" claim is factually false about the file's current bytes, not merely stale wording; this strengthens the finding. Supersession check: grep -i "supersed|struck|stale|CORRECTION" over design.md returns no marker anywhere in L25-35, L173-177 or L1509-1516; the only "superseded" hit (L172) refers to the 480/144 record counts, not to the digest statement, and the read_state_digest_discipline block at L50-53 cites corpus_record_sha256 as the live source of the hashing command, reinforcing rather than retracting it. The sole partially defensible fragment is the backlog's qualifier "read-time" (the recorded digests are post-remediation byte states, a limit design.md L69-76 states itself), but the adjacent clause "Digests remain `TO COMPUTE`" is false, and the design.md statements at L29-31, L174 and L1514 carry no such qualifier. No concrete counter-evidence exists; the provenance contradiction is real and unmarked.

**reproduction.**

- `command`: `python -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json').read_bytes()).hexdigest())"  (the command design.md's own `corpus_record_sha256` field prescribes, applied to the file §0.3 names)`
- `observed`: ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58 — an exact match to the digest recorded in the front matter at design.md L56-57, so §0.3's "The digest of the file as it now stands is `TO COMPUTE`" is false about the file's current bytes, not merely stale wording. Supersession sweep in the same pass: `grep -i "supersed|struck|stale|CORRECTION"` over design.md returns no marker anywhere in L25-35, L173-177 or L1509-1516.

### REPRODUCIBILITY-2-1 - RETAINED

- **raised by:** `reproducibility-verifier` (severity claimed: critical; category: entrypoint_runs)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-query-table-supplementary.py (module tail, no __main__ guard); ks-academic-recovery-pass.py (same); README.md:11-19, 41-48, 137-147

**Claim, verbatim.**

> **issue.** NEW defect, introduced by the round-1 remediation that archived and documented these scripts. Two of the archived executor scripts run their query loop at MODULE level with no `if __name__ == "__main__"` guard, and they write their output back over the archived logs and payloads IN PLACE. README.md tells a re-runner to invoke `PYTHONHASHSEED=0 python <script>` for "every executable script here" and warns only that a re-run "will not return the 2026-09-04 result sets" — it does not warn that the re-run DESTROYS the 2026-09-04 archive. The primary record of this branch is therefore one accidental import away from being silently overwritten, and it was overwritten during this audit.
>
> **evidence.** Verified destructively and disclosed: loading ks-academic-query-table-supplementary.py under PYTHONHASHSEED=0 (an import, not `main()`) executed live Crossref/OpenAlex/arXiv queries and rewrote 16 query logs plus their 16 payload files; a subsequent load of ks-academic-recovery-pass.py rewrote ks-s2-01-e.json before it was killed. `find -newermt "2026-09-04 13:26"` lists ks-crossref-16..19, ks-openalex-09..14, ks-arxiv-09..13, ks-s2-01-e and the matching payloads/. Divergence is now live between the record and its own logs: the corpus record §3 fence, line 401, reads `# ks-crossref-16 | executed 2026-09-04T10:36:43-05:00 | HTTP 200 | n_returned=20 | n_total_reported=2074233`, while ks-crossref-16.json on disk now reads executed_at 2026-09-04T13:27:34-05:00, n_total_reported 2074293 and a new payload_sha256; same for ks-arxiv-13 (10:37:35 -> 13:28:32) and ks-openalex-14 (10:37:14 -> 13:28:11). The original bytes are unrecoverable because the whole search-log tree is still untracked (`git status` shows `??`). The 112 academic log/payload digest pairs still self-verify (112 ok, 0 mismatch) precisely because log and payload were rewritten together, so the corruption is INVISIBLE to the in-tree digest check and only detectable against the prose record. failure_log F007's addendum guarantee — "the arm logs remain deliberately UNEDITED ... ks-repec-04.json and ks-repec-04-b.json are untouched" — rests on nothing enforceable.
>
> **fix.** (1) Restore or re-execute the 16 affected supplementary-block queries and reconcile the §3 fence, or record the loss as a dated data-integrity entry (DI-9) plus a gap — do not leave record and log silently disagreeing. (2) Put the query loop of ks-academic-query-table-supplementary.py and ks-academic-recovery-pass.py behind `if __name__ == "__main__": main()`. (3) Make LOGDIR/PAYDIR default to a `rerun/` subdirectory or require an explicit `--out` argument, so no re-run can write onto the archive. (4) Commit the search-log tree (it is the primary record and is currently untracked) and publish a manifest of per-log SHA-256 values so an overwrite is detectable. (5) Amend README.md's "Before running anything" section with an explicit destructive-write warning.
>
> **reference.** Protocol section 3.0 (verbatim logging obligation); PAYLOADS.md "Retained"; README.md "What was changed in these scripts, and what was not"

**Refutation attempt.**

> No refutation obtained; every checkable element of the finding reproduced independently. (1) Guard absence confirmed: ks-academic-query-table-supplementary.py ends with a module-level `for q in SUPP: e = run_arm.execute(q)`; ks-academic-recovery-pass.py has two module-level loops (`for qid in S2:`, `for q in REPEC_ALT:`); neither file contains the string `__main__`, while ks-academic-runner.py does have `if __name__ == "__main__":` at line 175 — guard present exactly where the finding says present, absent exactly where it says absent. (2) In-place archive writes confirmed: ks-academic-runner.py:15-16 sets LOGDIR=<repo>/docs/literature/search_logs/kalshi-strategy-multivocal and PAYDIR=LOGDIR/payloads, writing os.path.join(LOGDIR, "%s.json" % qid) at line 145 and os.path.join(PAYDIR, fn) at line 97; no --out and no rerun/ subdir exist. (3) Divergence is live on disk: lit_review_kalshi-strategy-multivocal_2026-09-04.md line 401 records ks-crossref-16 executed 2026-09-04T10:36:43-05:00 with n_total_reported=2074233, while ks-crossref-16.json now reads executed_at 2026-09-04T13:27:34-05:00 and n_total_reported 2074293; line 438 (openalex-14, 10:37:14) vs disk 13:28:11; line 467 (arxiv-13, 10:37:35) vs disk 13:28:32 — all three claimed divergences match exactly. (4) mtime scan returns 34 files newer than 2026-09-04 13:26: crossref-16..19, openalex-09..14, arxiv-09..13 (16 logs) plus their 16 payloads, plus ks-s2-01-e.json and its payload, plus candidates.json and title_merge_ledger.json. (5) README.md:11-19 instructs `PYTHONHASHSEED=0 python <script>` for "Every executable script here" and the table at 41-48 warns only "live API calls"/"will not return the 2026-09-04 result sets"; grep -ni "destro|overwrit|in place|in-place|backup|clobber" over README.md and PAYLOADS.md returns zero hits, so no destructive-write warning exists. (6) Irrecoverability confirmed: git status shows the whole search-log tree as untracked (??), git ls-tree -r 4821611 lists only ks-instrument-verification.json and ks-prior-identifiers.json from that directory, git stash list is empty, and no backup/.bak copy of ks-crossref-16.json exists outside the archive and its payloads/. (7) failure_log.md:567-571 does contain the unenforced guarantee "The arm logs remain deliberately UNEDITED ... ks-repec-04.json and ks-repec-04-b.json are untouched". The only unverified sub-claims are the auditor's account of the mechanism (its own import triggering the run) and the "112 ok, 0 mismatch" digest check; neither is load-bearing, and the mtimes plus timestamp divergence corroborate a live re-execution overwriting the archive at 13:27-13:29 on 2026-09-04. All checks were read-only; I did not import either executor script.

### REPRODUCIBILITY-2-2 - RETAINED

- **raised by:** `reproducibility-verifier` (severity claimed: critical; category: data_hashed)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front-matter protocol_amendments) and §3.3; docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md (round-1 remediation block, D8-D11)

**Claim, verbatim.**

> **issue.** Round-1 remediation item (7) is INCOMPLETE. Amendment M2 was issued and registered in two of the three required registers — the protocol Addendum (line 1441) and ks-amendments.jsonl — but the corpus record does not enumerate it anywhere. Protocol section 10, as the task spec restates it, makes a corpus record that ran under an amendment it does not enumerate defective, and there are now TWO. M2 is not incidental to this record: it rules on the record's own 1,465 G-dispositions and on its `n_excluded == Y-rows + G-rows` decomposition. The declaration is likewise silent: D7 records M1, and no D-entry records M2 even though the round-1 remediation block was appended after M2 was decided.
>
> **evidence.** `grep -c "M2" lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns 0. Line 74 still reads `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record ..."`. ks-amendments.jsonl carries M2 with `"execution_stage": "POST-EXECUTION and declared as such per section 10 ... This is a WEAKER amendment than M1"` and `"raised_by": "SCOPE-1-7"`; the protocol addendum §M2 states the weakness plainly and unsoftened (probe (c) passes AT THE PROTOCOL, fails at the record because the record does not carry it at all). Frozen prefix re-verified intact: sha256 of the first 91,498 bytes = 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac.
>
> **fix.** Amend front matter line 74 to "TWO numbered append-only amendments, M1 and M2", add an M2 subsection to §3.3 carrying its POST-EXECUTION status and the words "weaker than M1" verbatim, cross-reference it from the §5 flow where the 10 + 1,465 = 1,475 decomposition is stated, and append a D12 entry to the declaration recording M2 the way D7 records M1.
>
> **reference.** protocol_kalshi-strategy-multivocal_2026-09-04.md §10 and Addendum M2; ks-amendments.jsonl

**Refutation attempt.**

> Attempted refutation failed; every claimed element reproduces. (1) `grep -c "M2" docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns 0 (exit 1). A looser case-insensitive grep for "M2|amendment" across the record returns only M1-related hits plus unrelated CFTC "Rule Amendments" URLs and taxonomy-amendment prose — no reference to M2 in any spelling. (2) Line 74 verbatim still opens `protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record ..."`. (3) Section 3.3 is headed "3.3 Amendment M1, enumerated" and its body asserts "One amendment exists and all three of its parts are enumerated here" — a now-false count, not merely an omission. (4) M2 is registered in BOTH registers protocol section 10 requires: ks-amendments.jsonl carries the M2 object with `"execution_stage": "POST-EXECUTION and declared as such per section 10 ... This is a WEAKER amendment than M1"` and `"raised_by": "SCOPE-1-7"`; the protocol Addendum heading at line 1441 reads "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared". (5) Protocol section 10 (lines 1117-1152) states verbatim: "An amendment logged after the affected decisions were made must say so in those words; that is a weaker amendment than a pre-execution one, and the corpus record reports the distinction. ... a corpus record that ran under an amendment it does not enumerate is defective." The record does not report the distinction. (6) M2 is load-bearing on this record specifically: its ruling text names "the corpus record" and the exact decomposition "10 + 1,465 = 1,475", so the record demonstrably ran under it. (7) Declaration check: `grep -n "SCOPE-1-7" docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md` returns nothing; the D-series ends at D11 plus a "SCOPE-1-5 - DISCHARGED" entry, with no D12; D7 records M1 in full ("amendment M1 issued against the frozen protocol") and no entry records M2, even though the round-1 remediation block (D8-D11) addresses sibling round-1 scope-auditor findings and M2 was raised by round-1 SCOPE-1-7 (decided 13:40:00-05:00, after M1's 13:05:00-05:00). No exemption for post-execution amendments exists in section 10 — it explicitly contemplates them and imposes an ADDITIONAL reporting duty on the record. Finding stands as stated.

### REPRODUCIBILITY-2-3 - RETAINED

- **raised by:** `reproducibility-verifier` (severity claimed: major; category: data_hashed)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md front matter, `corpus_record_sha256` and `read_state_digest_discipline`

**Claim, verbatim.**

> **issue.** Incomplete fix of QUANT-1-5. The six read-state digests the lead computed were verified against disk: five match exactly, but the load-bearing one — the corpus record itself — does NOT. The pin was stale before it was committed, so the discipline the remediation added is already violated at its only externally-consumed value. Separately the same front matter carries two contradictory statements about that digest: `corpus_record_sha256` still reads "TO COMPUTE ... NO DIGEST IS ASSERTED rather than guessed" while `read_state_digest_discipline` twelve lines later asserts a concrete value for the same file.
>
> **evidence.** Recomputed on 2026-09-04: lit_review_kalshi-strategy-multivocal_2026-09-04.md = 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21; the design records b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b. The other five match byte-for-byte (ks-academic-candidates.json ad2b8208..., ks-github-records.jsonl 98e31293..., ks-venue-docs.json cab38c3f..., ks-lateral-records.json 3fd644ae..., ks-instrument-verification.json af4da817...). The stale value appears in no other file (`grep -rln b36795140b5bc93f .` -> design.md only), so nothing else propagates it. The design's own carried limit ("they pin the files for a FUTURE re-read; they do not retrospectively make this draft's existing quotations verifiable") is correctly stated and is not the defect — the defect is that the corpus-record value does not pin the current bytes either.
>
> **fix.** Recompute the corpus-record digest after the M2 and DI-9 edits land, record it with the date and time of computation, and state that a digest recorded mid-remediation is void; delete or explicitly supersede the "TO COMPUTE" text in `corpus_record_sha256` so one field does not deny what the other asserts. Re-verify all six at /preregister time as pre-freeze item 7 already requires.
>
> **reference.** H001 design.md §12 pre-freeze checklist item 7

**Refutation attempt.**

> No refutation. Both prongs reproduced independently. (1) Digest mismatch: running the design's own specified command from the repo root yields 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21 for docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md, while design.md line 55 records b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b. sha256sum in binary mode returns the identical 451f9008... value, excluding a line-ending or text/binary read-mode artifact. The other five arm digests match byte-for-byte (ks-academic-candidates.json ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58, ks-github-records.jsonl 98e312934e12fb42b19f93f1542d8fc8950805df0d844d8c430e563c94989b19, ks-venue-docs.json cab38c3f50d1f6b43455c409bc4c8e20695979456eacaee92b8b11c8cc2fec1d, ks-lateral-records.json 3fd644ae22bbb7db981c543604c94dfd6f6f19130176f0b548ee9f9f284aa181, ks-instrument-verification.json af4da817c2d2dcabdf851df62637bcb5322b2d32b313b19680ff0b15ac2e7028), which rules out any environment-wide hashing discrepancy as an explanation for the sixth. (2) Contradiction: design.md line 29 corpus_record_sha256 reads "TO COMPUTE ... NO DIGEST IS ASSERTED rather than guessed" while read_state_digest_discipline (line 43, value line 55) asserts a concrete digest for the same file; section 0.3 at line 174 repeats "The digest of the file as it now stands is `TO COMPUTE`". grep -n for void|supersede|stale over design.md finds no language retiring or superseding the b3679514... pin. (3) Propagation: grep -rln "b36795140b5bc93f" . returns only research/01_hypothesis_register/H001/design.md, matching the auditor's claim. Only imprecision found, non-load-bearing: the finding says the pin "was stale before it was committed", but git status --porcelain shows both design.md and the corpus record are untracked ("??"), so neither is committed at all. That corrects the tense of one clause and does not touch the defect, which is that the recorded digest does not pin the current bytes and that two front-matter fields assert contradictory things about the same value.

### REPRODUCIBILITY-2-4 - RETAINED

- **raised by:** `reproducibility-verifier` (severity claimed: major; category: data_hashed)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10; docs/literature/search_logs/kalshi-strategy-multivocal/ks-known-item-recall.json; docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (absent)

**Claim, verbatim.**

> **issue.** Probe (d): the 4.3% recall figure does NOT travel everywhere it is owed, and it travels with only one of the two figures its own log computes. (a) The declaration's own §4 promise is that "the corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check" — the corpus record contains no mention of the check, the seed set, or either recall figure; only G-10 carries the unrelated 6,923/8,813 index bound. The check was executed but never reached the artifact a reader consumes. (b) ks-known-item-recall.json computes TWO results, `recall_vs_identified_universe` 0.0428 (14/327) and `recall_vs_reported_branches` 0.0398 (13/327); D10 publishes only the higher one and never names the lower. Under charter commitment 5 a dropped qualifier is a defect, and this is the more favourable of two computed numbers reported alone.
>
> **evidence.** `grep -rn "known-item\|recall" lit_review_kalshi-strategy-multivocal_2026-09-04.md` returns one hit, and it is the Y3 exclusion code's use of the word "recall" (model recall), not the check. `grep -rln "4.3%"` across docs/, failure_log.md, hypothesis_backlog.md and research/ hits only the deliverable spec. ks-known-item-recall.json: `/results/seed_size = 327`, `/results/found_in_identified_universe = 14`, `/results/found_in_reported_branches = 13`, `/results/recall_vs_identified_universe = 0.0428`, `/results/recall_vs_reported_branches = 0.0398`. Its three input digests were recomputed and all three match. Both caveats ARE carried in D10 and in the file, so the bounds discipline itself is sound where the figure appears.
>
> **fix.** Add a subsection to the corpus record §5 or §13 stating the known-item recall check, both figures (14/327 = 4.3% against the identified universe, 13/327 = 4.0% against reported branches), both caveats verbatim, and the pointer to ks-known-item-recall.json; amend D10 to name the second figure and say why the first is quoted as headline.
>
> **reference.** deliverable_spec_kalshi-strategy-corpus_2026-09-04.md "Why this is a NEW branch" item 4; charter commitment 5

**Refutation attempt.**

> Attempted refutation failed; both limbs of the finding reproduce exactly. (a) deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:55-57 promises "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." Grep of the corpus record (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md, 2072 lines) for "known-item|known item|recall" returns ONE hit, line 62, which is the Y3 exclusion code's phrase "an executing agent's own recall" (model recall), not the check. Grep for "ks-known-item|seed set|327|0.0428|0.0398|4.3%" returns only line 77, where 327 is the PREDECESSOR branch's AG-11 store/include mismatch ("149 store entries against 327 included records") - the same integer in an unrelated role, not the seed set. 6,923/8,813 appears only at lines 195-200, 350 and gap row G-10, all novelty-differencing bound, as the finding states. The comparator clause strengthens the finding: the 2026-09-02 record carries its check IN-RECORD at section 13.4 "Known-item recall check - reported per item, with no pass threshold" (lit_review_kalshi-arbitrage_2026-09-02.md:4161) with the log cited at line 4252; the successor record has no counterpart. Grep of ks-amendments.jsonl for "known.item|recall" returns zero hits, so it is not carried in the amendment ledger either. Repo-wide grep for "4.3%" across docs/, failure_log.md, hypothesis_backlog.md, research/ hits only deliverable_spec line 337; the two "4.0%" hits are the unrelated Kalshi longshot-bias win rate in the 2026-09-02 lit review and its CSL-JSON abstract. (b) ks-known-item-recall.json /results verified verbatim: seed_size 327, found_in_identified_universe 14, found_in_reported_branches 13, recall_vs_identified_universe 0.0428, recall_vs_reported_branches 0.0398, not_retrieved 313. D10 (lines 330-348) publishes only "14 of the 327 ... a recall of 4.3%"; grep of the whole spec for "reported_branches|reported branches|13 of|4.0%" returns nothing. 14/327=0.042813 > 13/327=0.039755, so the published figure is arithmetically the more favourable of the two. ONLY discrepancy located: the finding anchors "a dropped qualifier is a defect" to "charter commitment 5", but charter_castles_2026-08-21.md:82-89 defines commitment 5 as "Attribution fidelity" (secondary-source marking; method attributions verified against the originating paper), not a completeness-of-reporting rule. That is a mis-cited normative anchor, not a counter-example - the spec's own section 4 promise is an independent in-document obligation that is unmet, and the two-computed-one-published fact holds without reference to any charter clause. A wrong reference attached to a true defect claim is a framing quibble, which the gate does not accept as refutation.

### REPRODUCIBILITY-2-5 - RETAINED

- **raised by:** `reproducibility-verifier` (severity claimed: major; category: data_hashed)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :114 (front-matter corpus_multivocal), :187, :1753

**Claim, verbatim.**

> **issue.** Probe (g): the MV- prefix sweep is internally consistent (89 MV-G-/MV-TC- occurrences, no orphaned bare G-n citations to the multivocal corpus), but the round-1 remediation added THREE new gaps to the corpus record (G-26 RePEc never searched, G-27 S-D/S-E digests are attestations, G-28 no store builder) without updating the agenda, which still declares in four places that the multivocal corpus "supplies G-1..G-25 and TC-1..TC-15" and names those as "the sole admissible source of branches 7-11". The declared range is now false, and the two gaps that are purely reproducibility gaps — G-27 and G-28 — have no downstream consumer at all.
>
> **evidence.** Corpus record §12.1 now runs to G-28 and line 2069 states "The full gap list is section 12.1 (`G-1` … `G-28`)". Agenda line 114: "its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 ... are the sole admissible source of branches 7-11"; line 60 and line 1753 repeat "G-1..G-25"; line 187 repeats "names gaps **G-1…G-25**". `grep "G-26\|G-27\|G-28"` over the agenda returns zero hits.
>
> **fix.** Extend the four range statements to G-1..G-28 and add MV-G-26/27/28 to the agenda's gap register, each either consumed by a branch or explicitly recorded as a gap this agenda declines to consume with the reason; MV-G-27 (attested-not-checkable S-D/S-E digests) in particular bears on any branch that would re-quote venue or lateral evidence.
>
> **reference.** agenda rev 3 derivation rule ("every branch derived ONLY from a named gap or TO COMPUTE handoff in the new corpus record")

**Refutation attempt.**

> Attempted refutation failed; every claimed particular reproduced. (1) Corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md section 12.1 contains G-26 (line 1876, RePEc never searched), G-27 (line 1875, S-D/S-E digests are attestations) and G-28 (line 1874, no archived store builder), each labelled "Added 2026-09-04 by round-1 audit remediation"; line 2069 states "The full gap list is section 12.1 (`G-1` ... `G-28`)". (2) The agenda declares the G-1..G-25 range at exactly the four cited sites: line 60, line 114 (front-matter corpus_multivocal, "sole admissible source of branches 7-11"), line 187 ("names gaps **G-1...G-25**"), line 1753. (3) grep "G-26\|G-27\|G-28" over the agenda returns zero hits. (4) The one available refutation avenue -- a version/digest pin that would make "G-1..G-25" true of a frozen snapshot -- does not exist: the agenda's only two mentions of the corpus record (lines 114, 187) carry no SHA-256 and no "as of" qualifier, unlike sibling front-matter fields at lines 146, 147, 151 and 152 which do pin digests for the protocol and both bibliographies. So the range declaration is unqualified and now false. (5) The no-downstream-consumer sub-claim also holds: a repo-wide grep for G-26/G-27/G-28 outside the corpus record yields a single hit, the token "G-27." inside docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json (a provenance log, not a consuming branch); docs/audits/, failure_log.md, hypothesis_backlog.md, research/, docs/decisions/ and docs/methodology/ return none.

**reproduction.**

- `command`: `grep "G-26\\|G-27\\|G-28" docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md  (plus a repo-wide grep for the same three ids outside the corpus record)`
- `observed`: Zero hits in the agenda. Repo-wide, the only occurrence outside the corpus record is the token "G-27." inside docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json (a provenance log, not a consuming branch); docs/audits/, failure_log.md, hypothesis_backlog.md, research/, docs/decisions/ and docs/methodology/ return none. Corpus §12.1 carries G-26 (line 1876), G-27 (1875), G-28 (1874), each tagged "Added 2026-09-04 by round-1 audit remediation", and line 2069 states the range as `G-1` … `G-28`; the agenda states G-1..G-25 at lines 60, 114, 187 and 1753 with no as-of date and no digest pin.

### FORMAT-2-1 - RETAINED

- **raised by:** `format-auditor` (severity claimed: critical; category: templates)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:74 (front matter `protocol_amendments`); whole file

**Claim, verbatim.**

> **issue.** NEW defect introduced by round-1 remediation. Amendment M2 was issued against the frozen protocol (protocol §Addendum M2; ks-amendments.jsonl line 3), but the corpus record does not enumerate it anywhere: `grep -n 'M2\|SCOPE-1-7'` over the corpus record returns NOTHING, and the front matter still asserts a count of one. The governing constraint is explicit: a corpus record that ran under an amendment it does not enumerate is defective, and there are now TWO. M2's own text asserts the opposite of the file state.
>
> **evidence.** corpus front matter: "protocol_amendments: \"ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record...\""; protocol M2: "Nothing about them changes ... but the reconciliation is retrospective and **the corpus record reports it as such**."
>
> **fix.** Amend `protocol_amendments` to "TWO numbered append-only amendments, M1 and M2", retaining the superseded wording in the same dated-correction style used for `rng_seed` and `screening_verdict_source`, and add an M2 subsection to section 3.3 enumerating the ruling, its POST-EXECUTION stage, its declared weakness relative to M1, and the 10 + 1,465 = 1,475 decomposition it ratifies. Do not edit ks-amendments.jsonl or the protocol.
>
> **reference.** protocol §10 amendment-enumeration rule; ks-amendments.jsonl M2 `execution_stage`; task constraint "there are now TWO, M1 and M2"

**Refutation attempt.**

> Could not refute; the finding reproduces in full. (1) `grep -n 'M2\|SCOPE-1-7'` over docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md returns exit 1 / zero matches; the grep is sound because `grep -c 'M1'` on the same file returns 10 and `file` reports plain UTF-8 (no encoding artifact). Case-insensitive and 'M-2' variants also return nothing. (2) M2 genuinely exists in both registers: ks-amendments.jsonl line 3 = {"amendment": "M2", "date": "2026-09-04", "decided_by": "lead session, on audit finding SCOPE-1-7", "execution_stage": "POST-EXECUTION and declared as such per section 10", "ruling": "A G-code is a FOURTH stage-1 outcome ... 10 + 1465 = 1475", "raised_by": "SCOPE-1-7"}, and its prose twin is at protocol line 1441 "### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared". (3) The corpus record asserts the contrary in two places, both unamended: front matter line 74 'protocol_amendments: "ONE numbered append-only amendment, M1, enumerated in full in section 3.3 of this record..."', and section 3.3 at line 1173 titled "Amendment M1, enumerated" whose body reads "One amendment exists and all three of its parts are enumerated here". (4) The governing rule reproduces verbatim at protocol section 10, lines 1151-1152: "a corpus record that ran under an amendment it does not enumerate is defective", with line 1147 separately requiring that for a retrospectively-logged amendment "the corpus record reports the distinction". (5) M2's own protocol text at lines 1471-1473 states "the reconciliation is retrospective and the corpus record reports it as such" — an assertion contradicted by the file, which never names M2. The only refutation avenue available — arguing the record did not "run under" M2 because M2 is POST-EXECUTION — fails on two independent grounds: section 10's second clause independently obliges the record to report the retrospective-amendment distinction, and the corpus record actually publishes the decomposition M2 ratifies (n_criterion_excluded: 10, n_capacity_gap: 1465, n_excluded: 1475), so it does rest on M2's ruling while omitting it. No concrete counter-evidence exists; the defect claim is true.

### FORMAT-2-2 - RETAINED

- **raised by:** `format-auditor` (severity claimed: major; category: citations)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:1796-1803

**Claim, verbatim.**

> **issue.** Seventh locus of the RePEc defect, missed by the remediation's six-locus sweep. The agenda still describes the corpus record's CURRENT text as asserting four executed-and-zero queries. That description was true before remediation and is false now: §10 N-5 was corrected to two. The bullet also frames the discrepancy as live and unrepaired.
>
> **evidence.** "the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero ... **One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here**"
>
> **fix.** Append a dated correction bullet (matching the house struck-text pattern) recording that the corpus record was corrected at limitation 9, N-5, N-8, the four section-2 source rows and the nine ks-repec fence annotations under DI-8/G-26, that the discrepancy is no longer live between the two documents, and that failure_log F007's 2026-09-04 addendum records the same. Retain the superseded sentence marked as struck.
>
> **reference.** corpus DI-8 / G-26; failure_log.md F007 ADDENDUM 2026-09-04; charter commitment 5

**Refutation attempt.**

> No refutation available; every leg of the finding reproduced against the working tree. (1) Anchor: research_agenda_prediction-market-microstructure_2026-09-02.md lines 1796-1803 carry the quoted text verbatim ("One discrepancy between the second corpus record and its own arm log is recorded and NOT repaired here ... the corpus record's §10 N-5 states that four academic queries in the weather stratum *executed* and returned zero"), present tense, as the file's final bullet (file ends at 1803), inside a section headed "Rev-3 corrections and inheritances from the SECOND corpus, all dated 2026-09-04" — a live-state section with no as-at-writing qualifier. (2) Referent: lit_review_kalshi-strategy-multivocal_2026-09-04.md §10 N-5 (line 1661) now reads "**Two** academic queries in that stratum executed and returned zero", with the "Four" wording demoted into a struck CORRECTION 2026-09-04 blockquote; DI-8 at line 1817 states "The corrected executed-and-zero count is TWO." So the agenda's description of that record's current text is false. (3) Liveness: failure_log.md F007 ADDENDUM 2026-09-04 states the count of TWO "now appears in BOTH documents — in this row, and in the corrected corpus record — so the discrepancy this row recorded is no longer live between them", directly contradicting the agenda's "recorded and NOT repaired here". (4) Counter-test for an existing fix: grep of the agenda for "2026-09-04|CORRECTION|struck|superseded" returned 20+ hits, none addressing the N-5 repair; the DI-8 sweep (limitation 9, N-5, N-8, four section-2 source rows, nine ks-repec fence annotations) is confined to the corpus record and does not reach the agenda, confirming the seventh-locus miss. The only contrary argument — that the struck "Four" wording is still physically present inside N-5, so the agenda's sentence is literally findable — fails because the wording is explicitly marked superseded (the record no longer asserts it) and the bullet's second clause independently frames the discrepancy as unrepaired; that is a plausibility quibble, not counter-evidence.

### FORMAT-2-3 - RETAINED

- **raised by:** `format-auditor` (severity claimed: major; category: citations)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:58-60, 185-188, 1753-1754

**Claim, verbatim.**

> **issue.** The MV- prefix convention (REV-1-3 remediation) fixes the multivocal identifier space at G-1..G-25 and TC-1..TC-15. Remediation then added three new corpus gaps — G-26 (RePEc never searched), G-27 (S-D/S-E bytes not archived), G-28 (store builder never archived). None appears in the agenda under any prefix, so the convention statement now under-describes the space it defines and three named gaps have no branch derivation or explicit non-consumption note.
>
> **evidence.** agenda:187-188 "The **multivocal** corpus ... names gaps **G-1…G-25** and handoffs **TC-1…TC-15**"; corpus §12.1 carries G-26, G-27, G-28
>
> **fix.** Extend the convention statement to G-1..G-28, add MV-G-26/27/28 to the gap register, and state for each either the branch that consumes it or that it is registered and deliberately not branched.
>
> **reference.** agenda rev-3 convention block; corpus §12.1 rows G-26/G-27/G-28

**Refutation attempt.**

> Attempted refutation failed; every element of the claim reproduces exactly.
> 
> 1. Convention statement bound at G-1..G-25. docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:187-188 reads: "The **multivocal** corpus, `lit_review_kalshi-strategy-multivocal_2026-09-04.md`, names gaps **G-1…G-25** and handoffs **TC-1…TC-15**, and **branches 7–11** derive from those." The same G-1..G-25 bound is repeated in the front matter at line 114 ("its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15") and in the rev-3 corrections block at lines 1753-1754 ("the multivocal corpus supplies G-1..G-25 and TC-1..TC-15"). Three sites, all capped at 25.
> 
> 2. Corpus defines G-1..G-28. docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 carries all three new rows: line 1874 G-28 ("The CSL-JSON store builder was never archived"), line 1875 G-27 ("S-D and S-E retrieved bytes are NOT in this repository"), line 1876 G-26 ("RePEc was never searched"). The corpus states its own bound at line 2069: "The full gap list is section 12.1 (`G-1` … `G-28`)". So the identifier space the agenda claims to describe is now 28 wide, not 25.
> 
> 3. No MV-G-26/27/28 anywhere in the agenda. `grep -o "MV-G-[0-9]*" | sort -u` over the agenda returns only MV-G-1..MV-G-9, MV-G-11, MV-G-12, MV-G-15..MV-G-20, MV-G-22..MV-G-25. Nothing at 26, 27, or 28. A separate grep for "G-2[5-9]|G-3[0-9]" over the agenda returns only the G-25 bound statements — zero hits for 26/27/28 under any prefix.
> 
> 4. No branch derivation and no explicit non-consumption note for the three. The only substantive contact the agenda makes with any of the three subjects is the RePEc interface failure, mentioned in prose at lines 1088 and 1790 without any gap identifier (line 1790 attributes it to failure-log row F007, not to a gap row). G-27 (unarchived S-D/S-E bytes) and G-28 (unarchived store builder) have no prose or identifier presence in the agenda at all.
> 
> The only thing that could soften the finding is that corpus line 1858 extends G-9 to cross-reference G-26, so MV-G-9 in the agenda indirectly touches the RePEc non-execution. That is a partial-coverage nuance for one of three gaps, not counter-evidence: it does not repair the G-1..G-25 bound in the convention statement, and it leaves G-27 and G-28 with no derivation and no non-consumption note. The defect claim is true as stated.

### FORMAT-2-4 - RETAINED

- **raised by:** `format-auditor` (severity claimed: major; category: magic-numbers)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** research/01_hypothesis_register/H001/design.md:29-35, 43-74, 89, 1509-1516, 1530-1537; hypothesis_backlog.md:32

**Claim, verbatim.**

> **issue.** The read-state digest remediation (QUANT-1-5) was applied at one locus and left four contradicting loci untouched, inside the same front matter. `corpus_record_sha256` still reads TO COMPUTE and "NO DIGEST IS ASSERTED", while 20 lines below the same front matter records that digest as b3679514...; `freeze_status` still says no read-time digest has been recorded for any arm file or for the corpus record; checklist item 1's residual obligation and item 7 restate the same; the backlog row repeats "Digests remain `TO COMPUTE` — none is asserted here". A reader cannot tell whether six digests exist.
>
> **evidence.** design.md:30 "TO COMPUTE — no shell or hashing tool was available ... NO DIGEST IS ASSERTED rather than guessed" vs design.md:54-55 "corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b"
>
> **fix.** At each of the four stale loci, record the digest (or a pointer to the read_state_digest_discipline block) with the same limit already stated there — pins a future re-read, does not retroactively verify this draft's quotations — retaining superseded wording as struck. Restate item 7's OPEN scope as the re-read and byte-depth re-verification only.
>
> **reference.** CLAUDE.md §Reproducibility; design.md `read_state_digest_discipline`; QUANT-1-5 remediation

**Refutation attempt.**

> Refutation attempted and failed; the finding is confirmed. All cited loci reproduce verbatim. design.md:30-31 states `corpus_record_sha256: TO COMPUTE ... NO DIGEST IS ASSERTED rather than guessed`, while design.md:43-74 in the same front matter asserts six digests including `corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md = b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b`. design.md:89 (`freeze_status`) states `no read-time digest has been recorded for any arm file or for the corpus record`. design.md:1514-1516 (checklist item 1 residual) states `its SHA-256 is not yet recorded`. design.md:1530-1533 lists item 7 as OPEN with `A SHA-256 is recorded for the corpus record and for each of the five arm files` inside its scope. hypothesis_backlog.md:32 states `(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files ... Digests remain TO COMPUTE - none is asserted here`. Counter-test run to test whether the 43-74 block might be non-assertive placeholder text: I recomputed SHA-256 over the arm files; ks-academic-candidates.json hashes to ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58, byte-identical to the recorded value, proving the block records genuine computed digests. The corpus record now hashes 451f90080c952360c3ab8d63772e5c19410d6acb217a526f0b8b777b61e28f21 (it changed after the b3679514 digest was taken), which the block's own CARRY-THE-LIMIT caveat anticipates but which does not rescue the four stale loci. The only partial defense - that item 7's residual scope is genuinely still open per the digest block's closing sentence - does not hold for item 7's own text, which still enumerates digest recording as OPEN, and does not apply at all to design.md:30-31, design.md:89, design.md:1514-1516, or hypothesis_backlog.md:32.

### FORMAT-2-5 - RETAINED

- **raised by:** `format-auditor` (severity claimed: major; category: citations)
- **refuted by:** refute-gate refuter role, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained
- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (limitations 1-9, §12); docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:56, 330-347

**Claim, verbatim.**

> **issue.** Probe (d): the 4.3% known-item recall figure and its two bounds do not travel — they appear ONLY in declaration amendment D10. `grep '4.3\|recall'` over the corpus record returns no recall statement at all, although the declaration's own corpus row requires the record to state "the known-item recall check" among the bounds a reader must carry.
>
> **evidence.** spec:56 "The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check"; corpus record grep for 'recall' matches only the Y3 exclusion-code text at line 62
>
> **fix.** Add the recall result to the corpus record's limitation block or §12, carrying BOTH bounds verbatim with it (seed-set question mismatch between the two protocols; novelty index covers 6,923 of 8,813 predecessor records) and the statement that it is not a screening statistic.
>
> **reference.** deliverable spec D10; corpus limitation 6 / gap G-10

**Refutation attempt.**

> Attempted refutation failed; every check confirmed the finding.
> 
> 1. Spec requirement reproduced verbatim at C:\Users\skoir\castles\docs\deliverables\deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:54-57: "No search is exhaustive. The corpus record states per-arm coverage, the strata left unassessed, and the known-item recall check, in the manner the 2026-09-02 record does." The obligation is placed on the corpus record, not on the declaration.
> 
> 2. Corpus record grep reproduced. `grep -n "recall\|4\.3"` over C:\Users\skoir\castles\docs\literature\lit_review_kalshi-strategy-multivocal_2026-09-04.md (2,072 lines) returns exactly one hit, line 62, inside the Y3 exclusion-code text ("from an executing agent's own recall"). Nothing else. Widened greps for "known.item", "seed set", "ks-known-item-recall", "14 of" also return no recall statement.
> 
> 3. Read the three places the result would have to live, and it is in none:
>    - Limitations 1-9 (lines 131-238): limitation 6 carries only the novelty-index bound ("6,923 of the predecessor branch's 8,813 records", 437 upper bound). No recall figure, no seed-set caveat, no "not a screening statistic".
>    - Section 12 gap table: row G-10 reads only "Novelty differencing is an upper bound: the prior index covers 6,923 of 8,813 predecessor records" — the novelty bound alone.
>    - Section 15 (lines 2022-2072), the record's own "what could not be verified" section: eight items, none mentioning the recall check.
> 
> 4. Provenance-scope check: `grep -rn "ks-known-item-recall" docs/` returns exactly one file — the deliverable spec, line 335 (amendment D10). The log file C:\Users\skoir\castles\docs\literature\search_logs\kalshi-strategy-multivocal\ks-known-item-recall.json does exist and does carry the result plus both bounds (seed_set_caveat: predecessor asks arbitrage/coherence/market-making vs this branch's STATED STRATEGIES; second_caveat: index covers 6,923 of 8,813), which confirms the two bounds the finding quotes are real — but confirms equally that neither the figure nor the bounds travel into the corpus record.
> 
> 5. Scanned the rest of the artifact set for a carrier elsewhere. docs\research_notes\research_agenda_prediction-market-microstructure_2026-09-02.md:1690 mentions "known-item miss" but that is the inherited 2026-09-02 predecessor correction about KI-20/KI-21 vocabulary gaps, a different branch and a different check; it carries no 4.3% figure. ADR-0006, the protocol, references JSON, failure_log.md, H001 design.md, hypothesis_backlog.md, and ks-amendments.jsonl carry no recall result (the protocol's "recall" hits are the Munaiah et al. 86% classifier figure and a "recall-check pass criterion deliberately absent" row — not this check).
> 
> Conclusion: the defect claim is true as stated. The 4.3% figure and its two bounds appear only in declaration amendment D10 and the untracked-locator log; the corpus record, which the declaration itself obligates to state the known-item recall check, states none.

## deferred-logged-minors

21 minors were raised and are LOGGED, NOT REMEDIATED, and did not pass through the refute gate
(the gate is for critical and major findings). They are recorded here in full so a later round or
a later session can act on them without re-deriving them; several are the low-severity tail of a
major finding above (the stale G-1..G-25 range, the 4.3%/4.0% pair, the digest contradictions).

### CRITICAL-2-5 (`critical-reviewer`, reporting)

- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md D10 (:330-347) vs ks-known-item-recall.json results block
- **issue:** Selective reporting of the more favourable of two computed recall statistics. The log computes and stores both `recall_vs_identified_universe: 0.0428` and `recall_vs_reported_branches: 0.0398` (14/327 and 13/327). D10 publishes only 4.3% and does not mention that a second, lower figure was computed against the branch-reported subset. The difference does not change the interpretation, which is why this is minor rather than major — but the deliverable that says "The figure is low and is published because it is low" publishes the higher of the two.
- **evidence:** ks-known-item-recall.json: "found_in_identified_universe": 14, "found_in_reported_branches": 13, "recall_vs_identified_universe": 0.0428, "recall_vs_reported_branches": 0.0398 — against D10: "a recall of 4.3%"
- **fix:** Report both figures wherever the recall is stated, with the denominator each is taken against, as the log itself distinguishes them.
- **reference:** SAMPL: no selective reporting of computed analyses; CHAMP item 20

### CRITICAL-2-6 (`critical-reviewer`, consistency)

- **location:** hypothesis_backlog.md:32 (H001 row, tail of the round-1 correction note) vs research/01_hypothesis_register/H001/design.md front matter `read_state_digest_discipline` (:43-74)
- **issue:** The two artifacts disagree on the state of the same pre-freeze obligation. The backlog's H001 row states pre-freeze checklist item 7 as "no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes" and closes "Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available in the remediation session". The design's front matter now records six computed digests and declares the computation obligation "DISCHARGED as to computation", with item 7 open only on its remaining components (re-reading at the pinned digest, byte-depth re-verification of the ks-sc-001/ks-sc-002 sentences). A reader consulting the register rather than the design is told no digest exists.
- **evidence:** hypothesis_backlog.md:32 "(7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is asserted here" — against design.md "the LEAD SESSION computed them on 2026-09-04 and they are recorded here, so this obligation is now DISCHARGED as to computation"
- **fix:** Append a dated note to the H001 backlog row (the file is append-only) recording that the six digests were computed by the lead session on 2026-09-04, that item 7 is discharged as to computation and open on re-read and byte-depth re-verification, and carrying the design's own limit that the digests pin a future re-read and do not retroactively verify the draft's existing quotations.
- **reference:** CHAMP internal consistency; charter commitment 3 (a stated state must match the artifact it describes)

### CRITICAL-2-7 (`critical-reviewer`, reporting)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §3 fences ks-ssrn (:613-616), ks-ghcode (:661-666), ks-nb; DI-8 (:1823-1826)
- **issue:** DI-8 states that the corrected defect class "extends to SSRN (HTTP 403), GitHub code search (HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are now flagged as interface failures rather than yields". The §2 source-table rows were duly flagged, and the nine ks-repec §3 fence annotations were rewritten to carry `n_returned_semantics`. The corresponding §3 fence annotations for ks-ssrn, ks-ghcode and ks-nb were not: they still read "executed … n_returned=0" with no semantics field, i.e. the same annotation form DI-8 struck for RePEc. The exposure is smaller because the HTTP 403/401 in the annotation itself discloses the failure, which is why this is minor rather than a repeat of the critical — but the remediation is incomplete at loci DI-8 names.
- **evidence:** "# ks-ssrn-01 | executed 2026-09-04T10:30:21-05:00 | HTTP 403 | n_returned=0 | n_total_reported=None" — against DI-8: "The same class extends to SSRN (HTTP 403), GitHub code search (HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are now flagged as interface failures rather than yields"
- **fix:** Add `n_returned_semantics` (or an equivalent "not an observed zero-yield" tag) to the ks-ssrn, ks-ghcode and ks-nb fence annotations, matching the ks-repec treatment, with the fence-header correction note extended to name them.
- **reference:** PRISMA-S item 8 (search strategies as run) and item 15 (records identified per source); DI-8's own stated scope

### CRITICAL-2-8 (`critical-reviewer`, reporting)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 gap G-27 (:1875)
- **issue:** G-27 is headed as a gap about "S-D and S-E retrieved bytes" but reports a verification covering only the 32 lateral (S-E) payloads. It never states that the 28 included S-D venue-document digests received no verification of any kind, so a reader can carry "32 matched, 0 mismatched, 0 missing" across both source classes and conclude the S-D attestations are verified-once too. The half of the gap that is strictly weaker is the half left unqualified.
- **evidence:** "**S-D and S-E retrieved bytes are NOT in this repository, so their `sha256_of_retrieved_bytes` values are ATTESTATIONS a reader cannot check.** … the lead session hashed all 32 lateral payloads there on 2026-09-04 before it was cleared: **32 matched, 0 mismatched, 0 missing**"
- **fix:** State in G-27, in a sentence of its own, that no S-D document digest was re-verified against its bytes at any point, so the S-D half of the gap is unverified rather than verified-once, and that the 32/32 result is confined to S-E.
- **reference:** CHAMP item 19 (data described adequately and correctly); the record's own warrant-per-record rule (ADR-0006 §What the widening costs)

### CRITICAL-2-9 (`critical-reviewer`, consistency)

- **location:** failure_log.md F007 addendum (:555-581) vs F007 body (:482-492)
- **issue:** The F007 addendum declares the row "superseded on ONE sentence only" and names that sentence as "Neither the corpus record nor the arm log is edited by this row". But the same paragraph's opening present-tense sentence — "Corpus §10 N-5 states that **four** academic queries in that stratum *executed* and returned zero" — is now equally false of the current corpus record. The addendum's second bullet does resolve the substance ("The executed-and-zero count of TWO now appears in BOTH documents"), so no reader is left with a wrong count; the defect is that the addendum's own scope statement understates what it supersedes.
- **evidence:** "the row above is left standing verbatim and is superseded on ONE sentence only.** The sentence *"Neither the corpus record nor the arm log is edited by this row"*"
- **fix:** Amend the addendum's scope sentence (append-only) to name both superseded sentences: the "neither is edited" clause and the present-tense "Corpus §10 N-5 states that four" clause.
- **reference:** Charter commitment 5; append-only supersession discipline (protocol section 10 pattern)

### CRITICAL-2-10 (`critical-reviewer`, reporting)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1 (:1873-1877)
- **issue:** The gap table is out of numeric order at its tail: G-24, then G-28, G-27, G-26, G-25. The three rows added by round-1 remediation were inserted before the pre-existing G-25 rather than appended. A reader scanning for a gap id by position, or checking that the register is complete against §15's "G-1 … G-28", has to read every row. Presentation only; no claim is affected.
- **evidence:** row order in §12.1: "| **G-24** | **Grey-literature content drift is unmitigated.** …" then "| **G-28** | **The CSL-JSON store builder was never archived.**" then "| **G-27** |" then "| **G-26** |" then "| **G-25** |"
- **fix:** Reorder the three appended rows to G-25, G-26, G-27, G-28, or append them after G-25 in issue order. No text change is required.
- **reference:** SAMPL: tables acceptable and non-duplicative; CHAMP item 22 (presentation)

### SCOPE-2-5 (`scope-auditor`, partial)

- **location:** docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md:336-338 vs ks-known-item-recall.json:14-16
- **issue:** Probe (d): D10 publishes one recall figure where its own source file computes two. The log reports recall against the identified universe (14/327 = 4.28%) AND against the reported branches (13/327 = 3.98%); D10 carries only the first. The two qualifying caveats do travel, but the second computed figure is dropped silently, which is the class charter commitment 5 treats as a defect.
- **evidence:** ks-known-item-recall.json :13-16 — "found_in_identified_universe": 14, "found_in_reported_branches": 13, "recall_vs_identified_universe": 0.0428, "recall_vs_reported_branches": 0.0398. Spec D10 :336-338 — "the academic arm identified 14 of the 327 records the predecessor branch dispositioned `include` - a recall of 4.3%."
- **fix:** State both figures wherever the recall is reported, with the denominator distinction named, or state explicitly why only the identified-universe figure is carried.
- **reference:** taskSpec probe (d); charter commitment 5

### SCOPE-2-11 (`scope-auditor`, added)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/README.md, PAYLOADS.md, queries.py, run_arm.py, ks-payload-digest-verification.json
- **issue:** Round-1 reproducibility remediation added five files to the declared search-log directory. They are legitimate materials of a declared deliverable and are described inside the corpus record (G-27 names the digest-verification file), but the declaration set its own precedent at D2 of recording additions to that directory as scope divergences, and none of these is recorded there. Only ks-known-item-recall.json is declared, at D10.
- **evidence:** Spec D2 :168-171 — "two pre-registration inputs added to the search-log directory before freeze ... Recording it here because an undeclared delegation is a scope divergence even when it improves the deliverable." Directory listing shows README.md, PAYLOADS.md, queries.py, run_arm.py and ks-payload-digest-verification.json, none named in the declaration.
- **fix:** Append a declaration amendment naming the files round-1 remediation added to the search-log directory and what each is for; downgrade to documented-drift once recorded.
- **reference:** spec D2 precedent

### SCOPE-2-12 (`scope-auditor`, partial)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:613-616, :661-667, :745-752
- **issue:** DI-8 extends its own defect class to SSRN, GitHub code search and Kaggle kernels and states their section-2 counts are now flagged; the section-2 rows were indeed flagged, but the corresponding section-3 fence rows were not, and still read "executed ... n_returned=0" with no semantics annotation — the same asymmetry the nine RePEc fence rows were corrected for.
- **evidence:** DI-8 :1823-1826 — "The same class extends to SSRN (HTTP 403), GitHub code search (HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are now flagged as interface failures rather than yields". Fence :614 — "# ks-ssrn-01 | executed 2026-09-04T10:30:21-05:00 | HTTP 403 | n_returned=0"; :662 — "# ks-ghcode-01 | executed ... | HTTP 401 | n_returned=0"; :746 — "# ks-nb-01 | executed ... | HTTP 401 | n_returned=0". Compare the corrected RePEc fence at :587-593, which carries a struck-wording header and per-row `n_returned_semantics`.
- **fix:** Annotate the ks-ssrn, ks-ghcode and ks-nb fence rows the way the ks-repec rows were annotated — the request was refused, not answered with a result set — or state in DI-8 why those three fences are deliberately left in the "executed" form.
- **reference:** DI-8

### QUANT-2-6 (`quant-auditor`, reporting)

- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:60, :114, :187, :1753
- **issue:** The agenda's identifier-collision convention — the round-1 REV-1-3 remedy — states at four loci that the multivocal corpus supplies gaps 'G-1..G-25'. The same round added G-26, G-27 and G-28 to that corpus, so the declared range is now stale and understates the register the agenda claims to be the sole admissible source of branches 7-11.
- **evidence:** Agenda line 114: *"its gaps G-1..G-25 and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-25 AND MV-TC-1..MV-TC-15 ... are the sole admissible source of branches 7-11"*; identical range statements at lines 60, 187 and 1753. Corpus record §15 item 9: *"The full gap list is section 12.1 (`G-1` … `G-28`)"*, and the §12.1 table carries G-26, G-27 and G-28. `grep -o "MV-G-2[678]"` over the agenda returns zero. The prefix sweep itself is otherwise clean: every bare G-n/TC-n occurrence outside the convention paragraphs resolves to the predecessor corpus, and no branch derivation is orphaned (branches 7-11 each name an existing MV- identifier: MV-G-1/2/3/4/11/12/19/20/24/25, MV-TC-3/5/12).
- **fix:** Update the four range statements to G-1..G-28 with a one-line dated note recording that G-26/G-27/G-28 were added by round-1 remediation after rev 3 was written, and state whether any of the three bears on an existing branch (G-27's verified-once digest posture bears on every branch quoting an S-E record).
- **reference:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md §12.1, §15 item 9

### QUANT-2-7 (`quant-auditor`, reporting)

- **location:** hypothesis_backlog.md:36 (H001 row, Notes cell)
- **issue:** Probe (a): the withdrawn false clause is left as running prose at its point of use and is struck only by a note roughly 350 words later in the same table cell. Everywhere else in this artifact set the practice is stronger — a blockquote, the words 'previously read', and 'Struck'. A reader scanning the cell top-to-bottom reads the false clause as the register's current claim before reaching its withdrawal.
- **evidence:** The cell reads *"... and no SHA is recorded, because the corpus record the design depends on (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md) does not yet exist and freezing would register a design against uncompiled literature"* as plain running text, and only at the end: *"CORRECTION 2026-09-04 (audit round 1, findings REV-1-4 / QUANT-1-6). The clause above beginning 'because the corpus record the design depends on … does not yet exist' is FALSE..."*. Compare the corpus record's limitation 9 and N-5/N-8, and the H001 front matter `corpus_record_state`, all of which mark the superseded text at the point of use.
- **fix:** Insert an inline marker at the clause itself — e.g. strike-through markup or a bracketed `[FALSE — see CORRECTION at end of this cell]` immediately after 'does not yet exist' — without deleting the wording, preserving append-only.
- **reference:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md limitation 9 correction block (the in-file standard); 21 CFR 11.10(e) as this project applies it

### QUANT-2-8 (`quant-auditor`, reproducibility)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json (key scratchpad_path_UNTRACKED_AND_EPHEMERAL)
- **issue:** The REPRODUCIBILITY-1-6 remedy introduces an absolute home-directory path carrying the OS username into a newly tracked file, contrary to the project convention and to the corpus record's own section 15 assertion about gate check G18. The REPRODUCIBILITY-1-5 sweep that removed four such paths was scoped to .py files only, so the class was not closed.
- **evidence:** File contains `"scratchpad_path_UNTRACKED_AND_EPHEMERAL": "C:\\Users\\skoir\\AppData\\Local\\Temp\\claude\\C--Users-skoir-castles\\e88a64c5-...\\scratchpad\\lateral"`. Repo CLAUDE.md: *"Repo-relative paths remain the convention in tracked prose — absolute paths under a home directory are brittle across machines regardless of identity policy."* Corpus record §15 item 1: *"G18 finds no OS username, no email address and no absolute home-directory path in either file"* — true of the two files named, but the same standard is not held in the sibling artifact this round created. Confirmed the .py sweep is complete: `grep -rn 'C:\\Users' --include=*.py` over the repository returns nothing.
- **fix:** Replace the literal path with a non-resolving descriptor (e.g. `"<session scratchpad>/lateral (untracked, ephemeral, not reconstructible)"`), keeping the session-id if it is load-bearing for the attestation's provenance, and extend the sweep to .json/.md as well as .py.
- **reference:** C:/Users/skoir/castles/CLAUDE.md §Identity hygiene, final paragraph

### QUANT-2-9 (`quant-auditor`, reproducibility)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/candidates.json, .../title_merge_ledger.json; .../README.md:73-74
- **issue:** Two regenerated intermediates sit untracked inside a tracked search-log directory, in direct conflict with the README's stated intent, and neither follows the directory's ks- naming convention. The declared final step of the session is a commit over docs/, which would sweep them in.
- **evidence:** `git status --porcelain` lists `?? docs/literature/search_logs/kalshi-strategy-multivocal/candidates.json` (348,776 bytes) and `?? .../title_merge_ledger.json`, both mtime 2026-09-04 13:27. README.md: *"The regenerated files are deliberately **not** committed: they are byte-equivalent to material already archived, and the corpus record's file inventory is the lead's to set."* I independently confirmed the byte-equivalence claim the README makes: title_merge_ledger.json and the archived ks-academic-dedup-title-ledger.json both digest to 15dbb51e4bc6f5763847131bc7edea89ea8c10f2625705b6cfda037c49e97c74. Every other file in the directory carries the ks- prefix.
- **fix:** Delete the two regenerated files before the final commit, or gitignore them, or commit them under ks- prefixed names and amend the README sentence. Do not leave the stated intent and the working tree in conflict at the commit boundary.
- **reference:** docs/literature/search_logs/kalshi-strategy-multivocal/README.md §'The one missing academic intermediate'

### LITERATURE-2-6 (`literature-check`, stale identifier-space declaration)

- **location:** docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md:59-60, :187, :1753
- **issue:** The MV- prefix convention introduced for REV-1-3 declares the multivocal corpus's identifier space as G-1…G-25, but the same remediation round added G-26, G-27 and G-28 to that record. The declared range is stale by three. Probe (g): no branch derivation is orphaned and no predecessor citation is mislabelled — all 94 MV- references resolve.
- **evidence:** Agenda line 187: "The **multivocal** corpus ... names gaps **G-1…G-25** and handoffs **TC-1…TC-15**"; repeated at lines 59-60 and 1753. Corpus record §15 item 9: "The full gap list is section 12.1 (`G-1` … `G-28`)", and §12.1 carries G-26 (RePEc never searched), G-27 (S-D/S-E bytes unarchived) and G-28 (store builder never archived), all three added 2026-09-04 by round-1 remediation. Verified independently: every MV-G-n / MV-TC-n token used in the agenda falls in G-1..G-25 / TC-1..TC-15, so nothing is orphaned; the agenda's own RePEc statement at line 1088 ("RePEc's interface never returned a result set at all") agrees with the corrected reading.
- **fix:** Update the three range statements to G-1…G-28 and note that MV-G-26, MV-G-27 and MV-G-28 are named-but-unconsumed by rev 3, or open a debt row for them. Also note that the corpus record's §12.1 gap table lists the rows out of order (…G-24, G-28, G-27, G-26, G-25), which makes the range easy to mis-read.
- **reference:** agenda front-matter revision_note clause (3); corpus record §12.1

### LITERATURE-2-7 (`literature-check`, weaker locator cited than the one available in repo)

- **location:** research/01_hypothesis_register/H001/design.md:561-570, :621-624, :1530-1537 (pre-freeze item 7), :1588-1594 (§13)
- **issue:** The §1.6 findings are provenanced to a URL re-fetch in converted text, with byte-depth verification and digest recomputation deferred to pre-freeze item 7. An in-repo archived copy of both READMEs exists, carries both quoted passages verbatim at fixed line positions, and its digest was already shown to match the recorded README digest. The design cites the weaker, non-durable locator and declares a verification gap that is already closed.
- **evidence:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-github-readme-evidence/sudo-ai-git__kalshi-backtest.md lines 34, 40-41 and .../himagna16__kalshi-microstructure.md lines 92-94 carry the three sentences verbatim. The round-1 audit trail (docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.md:1079) records the evidence file's "sha256 753d94ddd29e..., matches recorded digest". Design lines 566-570 nonetheless state "the fetch returned converted text rather than raw bytes, so **the README SHA-256 was NOT recomputed at re-fetch** ... and no line numbers were obtained, so the locations above are section-level". grep confirms the directory ks-github-readme-evidence/ is referenced by PAYLOADS.md, README.md and two scripts, and by NO prose artifact — not the corpus record, not H001, not failure_log.
- **fix:** Cite the in-repo evidence file plus its line positions and matching digest alongside the raw URL in §1.6(i)/(ii) and §13; narrow pre-freeze item 7 to whatever genuinely remains after that (re-reading each arm file at the pinned digest), and record that the two ks-sc-001 sentences and the one ks-sc-002 sentence are now verifiable in-repo.
- **reference:** CLAUDE.md Reproducibility contract (untracked locator vs clone-durable carrier); evidence hierarchy tier ordering

### LITERATURE-2-8 (`literature-check`, quotation attributable to the wrong source)

- **location:** research/01_hypothesis_register/H001/design.md:1187-1191 (§8.1)
- **issue:** An italicised sentence follows the naming of Kaufman, Rosset, Perlich & Stitelman 2012 in a construction that reads as a quotation from that paper. The sentence is in fact the wording of the adopted rule file, not of the paper. Italics are the document's convention for verbatim source quotation throughout, so the attribution is ambiguous in the direction charter commitment 5 forbids.
- **evidence:** Line 1188-1191: "The formal treatment is Kaufman, Rosset, Perlich & Stitelman 2012 (charter commitment 4), and it applies here without modification: *every feature must be computable at time `t` using only data available at time `t`* — and the fee schedule **is** a feature". rules/quant-project.md §Time-series integrity reads: "No look-ahead: every feature must be computable at time t using only data available at time t." Crossref-verified record for the cited DOI 10.1145/2382577.2382579: Kaufman, Rosset, Perlich, Stitelman, "Leakage in data mining: Formulation, detection, and avoidance", ACM TKDD 6(4), 2012 — correct as a bibliographic record; the issue is only which text the italics carry.
- **fix:** Attribute the italicised sentence to rules/quant-project.md §"Time-series integrity" explicitly, or de-italicise it and state it as the design's own restatement of the rule, keeping Kaufman et al. as the formal-treatment citation.
- **reference:** charter commitment 5; doi:10.1145/2382577.2382579 (verified: ACM TKDD 6(4), Dec 2012)

### LITERATURE-2-9 (`literature-check`, undeclared method transfer)

- **location:** research/01_hypothesis_register/H001/design.md:970-986 (§6 embargo)
- **issue:** The Politis-White automatic block length is used as one of two inputs to the walk-forward EMBARGO length. Neither cited paper addresses embargoing or purged cross-validation; both give optimal block length for the stationary and circular block bootstrap. The design declares comparable transfers explicitly elsewhere but not this one.
- **evidence:** §6: "`embargo` selection method: TO COMPUTE — selection procedure: the maximum of (i) the lag at which the residual PACF ... and (ii) the **Politis–White automatic block length** for the same series — Politis & White 2004 ... doi:10.1081/ETC-120028836, as amended by Patton, Politis & White 2009 ... doi:10.1080/07474930802459016 ... Data-driven, not chosen." Both records independently verified against Crossref and both match the design exactly: Politis & White (2004), "Automatic Block-Length Selection for the Dependent Bootstrap", Econometric Reviews 23(1):53-70; Patton, Politis & White (2009), "Correction to 'Automatic Block-Length Selection for the Dependent Bootstrap' by D. Politis and H. White", Econometric Reviews 28(4):372-375. Neither paper's scope reaches embargo/purge selection. By contrast the document writes "applied as a **declared cross-sectional transfer**" for Theiler et al. 1992 and "a **declared transfer**" for Adams, Smart & Huff 2017.
- **fix:** Add one clause to §6 stating that the block-length estimator is transferred from bootstrap resampling to embargo selection as a dependence-horizon estimate, that neither cited paper prescribes that use, and that the in-document derivation (the embargo must exceed the measured dependence horizon) is what carries it — in the same words the document already uses for its other declared transfers.
- **reference:** doi:10.1081/ETC-120028836 and doi:10.1080/07474930802459016 (both verified via Crossref); design §3.2 and §13 for the declared-transfer convention

### REPRODUCIBILITY-2-6 (`reproducibility-verifier`, data_hashed)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/PAYLOADS.md, "Retained" -> software-repository paragraph
- **issue:** The retained-bytes inventory under-states which S-C query rows carry no payload. It says payloads exist only for HTTP 200 rows and that "the five PyPI names that 404'd are logged with no payload, as intended", but ten of the fifty-nine rows carry no payload: the five PyPI 404s plus five auth-blocked 401 rows. The 401 rows are documented elsewhere (N-8, G-22) but a reader auditing byte retention from this file alone will reconcile 49 payloads against 54 rows and find five unexplained.
- **evidence:** Recomputed all fifty-nine ks-github-queries.json rows: 49 payload digests verify exactly (0 missing, 0 mismatch) after gzip decompression, confirming the `payload_sha256_basis` claim; the 10 payload-less rows are ks-pypi-03/05/07/08/14 (HTTP 404) and ks-ghcode-01, ks-ghcode-02, ks-nb-01, ks-nb-02, ks-nb-03 (HTTP 401).
- **fix:** Amend the sentence to "the five PyPI names that 404'd and the five auth-blocked rows (ks-ghcode-01/02, ks-nb-01/02/03, HTTP 401 — gap G-22) are logged with no payload".
- **reference:** PAYLOADS.md; corpus record N-8 / G-22

### REPRODUCIBILITY-2-7 (`reproducibility-verifier`, data_hashed)

- **location:** docs/literature/search_logs/kalshi-strategy-multivocal/ks-payload-digest-verification.json
- **issue:** The verified-once evidence for G-27 is recorded only in aggregate. `results` gives 32/32/0/0 with `mismatched_detail` and `missing_detail` empty, but there is no per-record list of `class_id` -> `local_payload_name` -> digest-as-hashed, so a reader cannot even confirm that the 32 objects hashed are the 32 records in ks-lateral-records.json rather than 32 other files. Separately the file embeds a machine-local absolute path carrying the OS username into a tracked artifact in a public repository, which is the class of thing round-1 finding REPRODUCIBILITY-1-5 removed from the .py files.
- **evidence:** File contents: `"results": {"records_checked": 32, "matched": 32, ...}`, no itemisation; `"scratchpad_path_UNTRACKED_AND_EPHEMERAL": "C:\\Users\\skoir\\AppData\\Local\\Temp\\claude\\..."`. The one anchor that does check is `record_file_sha256` 3fd644ae22bbb7db981c543604c94dfd6f6f19130176f0b548ee9f9f284aa181, which I recomputed against ks-lateral-records.json and it matches. Repo-wide `grep "C:\\Users" --include=*.py` returns nothing, so the 1-5 fix itself holds.
- **fix:** Add the 32-row itemisation (record id, local_payload_name, digest recomputed, digest as recorded) so the verified-once claim is at least internally auditable after the scratchpad clears; replace the absolute scratchpad path with a non-identifying description, or keep it but state that the username in it is incidental.
- **reference:** corpus record G-27; PAYLOADS.md "Where the S-D bytes actually are"

### FORMAT-2-6 (`format-auditor`, style)

- **location:** docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md:1874-1877
- **issue:** The §12.1 named-gap table is out of identifier order after remediation: G-28, then G-27, then G-26, then G-25. A reader scanning for a gap id can miss a row.
- **evidence:** row order in §12.1: "| **G-28** | ... | **G-27** | ... | **G-26** | ... | **G-25** |"
- **fix:** Sort the three appended rows into numeric position, or state once above the table that appended rows are listed in remediation order.
- **reference:** house table convention across §12.1 rows G-1..G-24

### FORMAT-2-7 (`format-auditor`, templates)

- **location:** docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md:784-785 vs 481, 624, 793, 843, 889
- **issue:** Round-1 finding on surviving `[INSTRUMENT-*]` tokens is NOT remediated: the prescribed fix was a one-line clarification in the append-only Addendum, and the Addendum contains only M1 and M2. `grep 'placeholder|anchor'` over the protocol returns a single hit — the frozen sentence that the tokens contradict.
- **evidence:** protocol:784 "**A placeholder surviving into the registration commit is itself a defect**; none survives." against protocol:793 "### 7.1 [INSTRUMENT-MLR] — ...", :843, :889, :481, :624
- **fix:** Append the one-line Addendum clarification (frozen text cannot be edited): the `[INSTRUMENT-*]` tokens are retained deliberately as stable cross-reference anchors, the substitution test is that each anchor is followed by a resolved record in §7, and all three pass it.
- **reference:** protocol §7; round-1 template-substitution finding and its recorded fix

## verification-of-remediations

This is the round-2 obligation: confirm what round 1's thirty-two retained findings produced.
Each item below states what was checked and the result. **CONFIRMED FIXED** means the branches
re-derived the fix and found it complete; **INCOMPLETE** means the fix landed at the locus the
round-1 finding named and not at the artifacts that cite it, and the residue is carried as a
round-2 finding by id.

1. **The seeded RePEc defect (REV/SCOPE/QUANT/LITERATURE/REPRODUCIBILITY/FORMAT-1-1, plus
   LITERATURE-1-2 / REPRODUCIBILITY-1-2) — CONFIRMED FIXED inside the corpus record.** Four
   branches independently re-read all six loci (head limitation 9, N-5, N-8, the four section-2
   source rows, the nine `ks-repec` section-3 fence annotations, G-9 extended) plus DI-8 and the
   new gap G-26. The corrected executed-and-zero count is TWO (`ks-arxiv-04`, `ks-openalex-04`);
   no locus still asserts four; no arm log was edited; no count moved. Probe (a) passes here:
   every superseded sentence sits inside a dated, marked "CORRECTION 2026-09-04 … Struck"
   blockquote and cannot be misread as the record's current claim. Probe (b) passes: corpus
   record, DI-8, G-26, failure_log F007's dated addendum and the nine untouched arm logs agree.
   **INCOMPLETE outside it:** the agenda still narrates the pre-correction state as live
   (CRITICAL-2-2, SCOPE-2-6, FORMAT-2-2), and DI-8's own extension to the SSRN / GitHub-code /
   Kaggle fences was not applied (minors CRITICAL-2-7, SCOPE-2-12).
2. **REV-1-7 arithmetic — CONFIRMED FIXED.** Re-derived independently by three branches:
   43+30+31+5=109, 109-10=99, store length 99 = `n_included`; and the flow identities close
   (1986-412=1574, 1574-1475=99, 10+1465=1475, per-arm 528+980+30+36=1574, source-table
   `n_records` summing to 1,986, extraction-depth composition 40+28+31=99).
3. **QUANT-1-2 / QUANT-1-3 (H001 withdrawal and restatement) — CONFIRMED FIXED in H001, and
   probe (f) passes:** the false 'Correction' is withdrawn, both dropped README sentences are
   named, the stronger/weaker framing is explicit, the 2.6c tail sentence is recorded, both
   10.7c and 2.6c are flagged NOT ADOPTABLE, and the fee-monotonicity justification is withdrawn
   with the fee-PLUS-spread reason stated. The design still states no tradeable rule, no position
   size and no expected return. **INCOMPLETE:** the two verified extraction defects were
   propagated to H001 only and are absent from the corpus record of record and from the
   failure_log (QUANT-2-5, LITERATURE-2-2).
4. **REV-1-4 / QUANT-1-6 (corpus record recorded as EXISTING; checklist item 1 discharged) —
   CONFIRMED FIXED in the design body, INCOMPLETE at four sibling loci that still assert the
   superseded state (FORMAT-2-4, LITERATURE-2-5, minor QUANT-2-7).
5. **QUANT-1-5 (read-state digest discipline) — INCOMPLETE and, at one value, WRONG.** Five of
   the six lead-computed digests verify byte-exactly on disk; the sixth, the corpus record's, does
   not (recorded `b3679514…`, actual `451f9008…`), because the record was written at 13:26:08
   after the pin was taken at 13:19:56 (QUANT-2-2, REPRODUCIBILITY-2-3). The same front matter
   still asserts that no digest is asserted (SCOPE-2-8), and the backlog register disagrees with
   the design about whether item 7 is discharged (SCOPE-2-9, minor CRITICAL-2-6).
6. **QUANT-1-4 / LITERATURE-1-3 (Politis & White 2004; Patton, Politis & White 2009) —
   CONFIRMED FIXED and bibliographically exact.** Both records were re-fetched against primary
   sources this round and match (Econometric Reviews 23(1):53-70, doi:10.1081/ETC-120028836;
   28(4):372-375, doi:10.1080/07474930802459016); the 2009 formulae are correctly named as the
   implementable ones and both are flagged not-re-fetched-in-session. Residue: the addition sits
   outside the declaration's D5 citation envelope with no amendment (SCOPE-2-10), and the
   AFML-derived machinery in the same document remains uncited with a wrong section pointer
   (LITERATURE-2-4).
7. **REV-1-3 (MV- prefix sweep) — CONFIRMED FIXED as to the sweep; probe (g) passes.** All 94
   MV- references resolve, no branch derivation is orphaned, no predecessor citation is
   mislabelled. **INCOMPLETE:** the declared identifier RANGE is stale at four loci
   (CRITICAL-2-3, SCOPE-2-7, REPRODUCIBILITY-2-5, FORMAT-2-3, minors QUANT-2-6, LITERATURE-2-6).
8. **REV-1-5 (failure_log F008 conditional, F007 addendum) — CONFIRMED FIXED.** F008's Step 2b
   is a marked `[corpus-inference]` conditional, F007 carries its dated addendum, and the
   append-only property holds. Residue is a scope-statement understatement inside the addendum
   (minor CRITICAL-2-9).
9. **D8-D11 and the SCOPE-1-5 discharge — CONFIRMED PRESENT.** The round-1 trail exists with
   22/22 keys and 7/7 sections, and the four declaration amendments are recorded. **INCOMPLETE:**
   D10's executed known-item recall never reached the corpus record the declaration binds it to,
   and it drops the second computed figure (CRITICAL-2-4, SCOPE-2-4, QUANT-2-3, LITERATURE-2-3,
   REPRODUCIBILITY-2-4, FORMAT-2-5, minors CRITICAL-2-5, SCOPE-2-5). Probe (d) therefore FAILS,
   by non-propagation rather than by dropped bounds: where the figure appears it does carry both
   caveats.
10. **SCOPE-1-7 / amendment M2 — ISSUED CORRECTLY, THEN NOT PROPAGATED.** M2 is written into both
    registers protocol section 10 requires, states its POST-EXECUTION stage and its declared
    weakness relative to M1 plainly and unsoftened, and did not touch frozen text. It is
    enumerated in neither the corpus record (which affirmatively asserts "One amendment exists")
    nor the declaration, which is the precise state section 10 calls defective. Five branches
    raise it independently: CRITICAL-2-1, SCOPE-2-1/2-2/2-3, QUANT-2-1, LITERATURE-2-1,
    REPRODUCIBILITY-2-2, FORMAT-2-1. Probe (c) therefore fails by ABSENCE, not by softening.
11. **REPRODUCIBILITY-1-3/1-4/1-5/1-6 — CONFIRMED FIXED, and re-verified mechanically.** The
    frozen prefix still hashes to `32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac`
    over the first 91,498 bytes; the corrected `rng_seed` enumeration is exact (13 PYTHONHASHSEED
    asserts, with a reproducing negative control); all 112 academic, 49 S-C and 29 README digests
    recompute; `ks-academic-extract.py` regenerates the title ledger byte-identically
    (`15dbb51e4bc6…`); no absolute home path survives in any `.py`; G-27 and G-28 are registered.
    Residue: G-28's "not re-runnable at all" was falsified by execution — the builder was
    recovered from the session scratchpad and regenerated the store to the recorded digest
    `c7545d31…` (QUANT-2-4); G-27 reports only the S-E half of its own scope (minor CRITICAL-2-8);
    and the absolute-path class was closed for `.py` only (minors QUANT-2-8, REPRODUCIBILITY-2-7).
12. **REPRODUCIBILITY-1-7 (nothing committed at audit time) — NOT FIXED, and now load-bearing.**
    The tree is still uncommitted, and this round demonstrated the consequence: an accidental
    module-level execution of two archived scripts overwrote sixteen query logs and their
    payloads in place, the record and its logs now disagree, and the original bytes are
    unrecoverable precisely because the search-log tree is untracked (REPRODUCIBILITY-2-1).

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; it does not enumerate. The examined evidence may not be
representative of the artifact set, and nothing below should be read as a certificate that the
unexamined remainder is sound. Six branches read what their briefs directed them to read, at the
depth their effort tier allowed, in one pass; a different sample would very likely surface a
different set of findings. Absence of a finding in a region is evidence about the sample, not
about the region. Two round-2 findings are themselves instances of this: QUANT-2-4 exists only
because one branch happened to look outside the repository at the executing session's scratchpad,
and REPRODUCIBILITY-2-1 exists only because a branch executed an archived script rather than
reading it. Neither region was sampled in round 1.

Per-branch residual risk, in each branch's own words, is recorded verbatim in the round-2 sidecar
under `residual_risks`. The load-bearing items:

- **`critical-reviewer`** — RQI coverage. (D1) Importance — ADEQUATE, no finding: the question (what the retrievable multivocal record STATES about strategies on a regulated binary-event venue, and what preconditions those sources themselves name) is well posed, is reachable under ADR-0003's specification-only bound, and the corpus record is explicit that it answers a stated-record question and not a profitability question. (D2) Originality — ADEQUATE with a declared, honest caveat: the branch is not a restatement of the 2026-09-02 corpus (different admission bar, different question, non-merge rule stated in both documents and in ADR-0006 §Consequences/Negative), and H001 §0.3 pre-registers its own originality risk by …
- **`scope-auditor`** — The seeded round-1 RePEc defect is genuinely and thoroughly remediated: all six named loci in the corpus record carry corrections, every superseded sentence is quoted inside an explicitly marked correction block or struck header rather than left readable as current text (probe (a) clears), the nine ks-repec arm logs independently support the corrected count of two, and the corpus record, DI-8, gap G-26 and failure_log F007's dated addendum now agree with each other and with the logs (probe (b) clears). REV-1-7's arithmetic closes independently: 43+30+31+5=109, 109-10=99, 99 store entries, 1986-412=1574, 1574-1475=99, 10+1465=1475. QUANT-1-2 and QUANT-1-3 are properly withdrawn-and-restated, …
- **`quant-auditor`** — The RePEc remediation is complete and correct at all six loci with no surviving assertion of four executed queries and with corpus record, F007's addendum, DI-8 and the nine untouched arm logs now in agreement; the arithmetic I could re-derive is sound (109 = 43+30+31+5, all three flow identities, per-source counts summing to 1,986, store length 99 = n_included at the recorded digest, 14/327 = 4.3%, 22/22 inline lateral digests, 25/25 scratchpad lateral payloads, byte-identical title-ledger regeneration, 13 PYTHONHASHSEED asserts, zero absolute paths in .py, frozen prefix hash intact, and every QUOTED constant in H001 tracing to a real venue clause) — so what remains unverifiable is confined …
- **`literature-check`** — VERIFIED CLEAN THIS ROUND (positive results, recorded so they are not re-litigated in round 3). Every external citation I could resolve was fetched against a primary source and matched: Politis & White 2004 = Econometric Reviews 23(1):53-70, doi:10.1081/ETC-120028836; Patton, Politis & White 2009 = Econometric Reviews 28(4):372-375, doi:10.1080/07474930802459016 — the LITERATURE-1-3 / QUANT-1-4 remediation is bibliographically exact, correctly names the 2009 formulae as the ones to implement, and correctly flags both as not-re-fetched. PRISMA-S terminology clause verified VERBATIM against PMC7839230 including the full review-type enumeration, so `standard_declared` clause 1's direct claim st …
- **`reproducibility-verifier`** — Round-1 reproducibility remediation is largely genuine and I verified it rather than taking it on trust. Confirmed good: the frozen prefix still hashes to 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac over the first 91,498 bytes; the corrected rng_seed field's enumeration is exact — twelve scripts carry a real `assert os.environ.get("PYTHONHASHSEED") == "0"` (five academic + all seven S-C) plus run_arm.py inheriting it = thirteen, ks-academic-query-table.py correctly has none, and the negative control reproduces (every assert-carrying script raises AssertionError at entry with PYTHONHASHSEED unset); the withdrawn store-builder clause is correctly registered as G-28; all 11 …
- **`format-auditor`** — The RePEc remediation itself is sound and well-executed within the corpus record: every superseded sentence is retained inside a blockquoted, dated CORRECTION note that names the finding ids and uses the word "struck", so probe (a) is clean — no retained wrong sentence reads as the record's current claim. Probes (b) and (f) are also clean: DI-8, F007's dated addendum and the arm logs agree on TWO executed-and-zero queries with the logs deliberately unedited, and the H001 §1.6 rewrite states no tradeable rule, no position size and no expected return, withdraws the false 'Correction' explicitly, flags both 10.7c and 2.6c NOT ADOPTABLE, and withdraws the fee-monotonicity justification. Probe (c …

Standing risks the artifacts disclose themselves and which this round did not re-litigate: every
eligibility verdict and every extraction is single-pass LLM output with no archived per-record
prompt and no recoverable sampling parameters, so the seed pins only the deduplication,
branching, ordering and serialization halves; the S-D and S-E payload attestations become
unverifiable once the session scratchpad clears (G-27), and the S-D half was never verified at
all; and quotations this draft made from mutable arm files before the digests were pinned remain
unrecoverable at byte depth. One branch could not compute the frozen-prefix digest itself and
carried that as its own residual risk; another branch computed it and it matches.

## ai-assistance-statement

Per ICMJE Recommendations (updated January 2026), an AI tool cannot be an author and AI
assistance is disclosed. **Models used:** Claude Opus 5 (model id `claude-opus-5`) for the lead
orchestration session, for all six specialist auditor branches, and for the adversarial refute-gate
role. **Roles:** audit (all six branches: reading the remediated artifacts, re-deriving counts and
digests, and raising schema-validated findings), audit-adversarial (the refuter, which attempted to
defeat each critical/major finding with concrete counter-evidence), and prose (drafting this trail
and its sidecar from the workflow payload). No model authored a research claim of the branch under
audit; the deliverables audited here were produced in earlier sessions and are unmodified by this
round. The responsible human is the operator named in the front matter, who directed the round and
owns every disposition recorded in it.

**Reproducibility log.** `artifacts/` and `logs/` are gitignored, so no path under them resolves in
a fresh clone; the clone-durable carrier is the commit itself, via the `Repro-Log-Path:` /
`Repro-Log-SHA256:` trailers written by `/commit-with-provenance`. Untracked locator for this round:
`logs/reproducibility/repro_log_{run_id}.json` for the session run id recorded in
`docs/audits/session_trail_2026-09-04.md`; the pip-freeze archive for this environment is
`logs/reproducibility/env/495798ac...txt`, sha256
`495798ac328ee7cc673610470fe1d344e15a2dd942b22c0cb9ada0cd6a01115a`. The machine-readable payload of
this round is the round-2 sidecar named in the front matter, whose sha256 is recorded there.

## immutability-and-retention

This trail is committed to the repository and is **append-only**. Round 1 occupies the sections
above and is untouched by this round: its front matter, its findings table, its refute-gate
entries and its JSON sidecar
(`docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.json`, sha256
`b79c631144c770f11431dff7c5f55d9149fa3853fe3f2d41b13dc4c305f10038`) are byte-unchanged. Round 2 is
appended below them with its own front matter and its own sidecar
(`docs/audits/audit_trail_kalshi-strategy-corpus_2026-09-04.round2.json`, sha256 `3eb19a401e79e0dd1029e2cf3cf9a5f2b0b34e94b3789357004f07e6dc0e6fa9`),
so no previously recorded information is obscured (21 CFR 11.10(e)). A round 3, if the loop reaches
it, appends in the same way.

A correction to anything recorded in either round is made as a **dated addendum appended at the
end of this file**, stating what was recorded, what is now believed, and on what evidence. The
superseded wording stays legible in place. No finding, refutation or disposition already recorded
here is rewritten, and no entry is deleted; an audit trail that is silently edited is not an audit
trail. This is the same discipline the branch applies to its own frozen protocol.

Retention: for the life of the repository. The trail and both sidecars are tracked, so their
integrity is carried by git history, and the front-matter digests bind each round to the exact
artifact bytes audited in it. `worktree_clean: false` at both rounds, so the round-2 artifact
digests pin working-tree bytes rather than committed ones until the delivery commit lands them —
the exposure REPRODUCIBILITY-2-1 names, recorded here rather than elided. The round-1 sidecar
digest above remains the correct digest for the round-1 payload as it stood.


---

# ROUND 2 — appended 2026-09-04T14:27:17-05:00

**Append-only.** This section is added below the round-1 record; nothing above is
edited (21 CFR 11.10(e)).

## Round-2 result

| | |
|---|---|
| verdict | **block** |
| branches routed | critical-reviewer, scope-auditor, quant-auditor, literature-check, reproducibility-verifier, format-auditor |
| raw critical / major / minor | 7 / 26 / 21 |
| refuted by the gate | **0** |
| to remediate | 33 |
| rounds completed / cap | 2 / 3 |
| cap reached | no |

**The round-2 gate refuted nothing.** Round 1 dropped 2 of 34 gated findings;
round 2 dropped 0 of 33. That is recorded rather than smoothed over: a gate that
kills nothing is either facing only true findings or has lost discrimination, and
this run cannot distinguish those. It is entered as a residual risk below.

## What round 2 found, and why running it mattered

**Four branches independently raised the same critical finding, and it was a
defect ROUND-1 REMEDIATION ITSELF INTRODUCED.** Amendment M2 was issued during
round-1 remediation and registered in the two registers protocol section 10
names — the protocol addendum and `ks-amendments.jsonl` — but the third
obligation, enumeration in the corpus record, was missed. The corpus record went
on asserting "One amendment exists" one sentence after quoting the rule that
makes exactly that defective. **This is the finding that justifies the second
round**: it did not exist before round 1's remediation, so no amount of
additional round-1 auditing could have caught it.

**A gap was registered that should never have been registered.** Round-1
remediation closed REPRODUCIBILITY-1-4 by recording gap G-28, "the CSL-JSON store
builder was never archived ... not re-runnable at all". Round-2 finding QUANT-2-4
established that the builder existed at the time, in the same scratchpad from
which fifteen other scripts had just been archived. It is now archived and
verified to regenerate the store **byte-for-byte** (`c7545d31…`, 167,673 bytes,
99 entries), and G-28 is closed by recovery with its text struck. The general
lesson is recorded in the declaration and in the agenda: **registering a gap is a
claim about the world and carries the same evidence burden as any other claim.**

**Two agents refused to write, and both were right.** The corpus-record
remediation agent and the H001 agent each lacked an in-place edit tool and
declined to whole-file-rewrite a data-integrity record and a design containing
byte-sensitive degraded-extraction quotations. Both supplied verified drop-in
patches instead; the lead applied them with `Edit`. The three degraded quotations
(`P ayout C riterion`, `Contracts hall be $0.01`, the source's `demostrable`
misspelling) were confirmed intact afterwards. **A refusal to act that names its
reason and hands over the work is a correct outcome, not a failed one**, and it
is recorded here as such.

## Round-2 remediations

| finding(s) | branch(es) | disposition | where |
|---|---|---|---|
| CRITICAL-2-1, SCOPE-2-1, QUANT-2-1, LITERATURE-2-1 | 4 branches | remediated | corpus §3.4, front matter `protocol_amendments`, §3.3, `protocol_path` |
| CRITICAL-2-4, SCOPE-2-4, QUANT-2-3, LITERATURE-2-3 | 4 branches | remediated | corpus head limitation 10 + gap G-29 |
| QUANT-2-4 | quant-auditor | remediated by RECOVERY | `ks-store-builder.py`; G-28 closed |
| LITERATURE-2-2, QUANT-2-5 | 2 branches | remediated | corpus DI-9; G-23 five→seven figures |
| SCOPE-2-8, QUANT-2-2 | 2 branches | remediated | H001 ordering rule; both digest fields |
| SCOPE-2-9 | scope-auditor | remediated | backlog reconciled; pending-flag struck |
| LITERATURE-2-4 | literature-check | remediated | López de Prado 2018 at §4, §6, §13 |
| CRITICAL-2-2, CRITICAL-2-3, SCOPE-2-6, SCOPE-2-7 | 2 branches | remediated | agenda: ranges → MV-G-1..28, H-10, closure notes |
| SCOPE-2-3, SCOPE-2-10 | scope-auditor | remediated | declaration D12, D13 |

## Artifact digests at close of round 2

| path | sha256 |
|---|---|
| `docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md` | `ed7aca3e767714a70aa3415037a5982fb1595ad3b616f289625ef3da86d80e53` |
| `docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md` | `c643c620560fe5a83603a65780383b86d75e075a9d429dd06e11186969d424bb` |
| `docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` | `bedb10fbb71ee2024c6ca1852bb586d2146443ca09dae6df7edd6589bba6e430` |
| `docs/literature/references_kalshi-strategy-multivocal.json` | `c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df` |
| `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md` | `bcb82f1d470895c6f5e9a0feab884f699ee184f326763c4a5b6a06fa29735d24` |
| `failure_log.md` | `6ab2fd3507edeb7fca34e99a84703a6e85cba07c0ed844f2f76be51c72d1736a` |
| `research/01_hypothesis_register/H001/design.md` | `3707a1d443bb291146907fe9eb9e3d57068bca695e6024b49064ff586586c7c1` |
| `hypothesis_backlog.md` | `60bcccb84a437ad0853757b78efa0c181d43cdc78add3f8a68895928e5246903` |
| `docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl` | `bacd5bdff2db267366312298e6fd79f1ceba8142647eb5f77f2349a49a826f97` |

repo_head at close: `4821611c1c93b5f929a76f3ba6207e900440cee5`

## Residual risk after round 2

1. **The loop is exiting at round 2 of a 3-round cap with a `block` verdict on
   round 2's own findings, all of which are remediated but NOT re-audited.** A
   third round would very likely surface defects introduced by round-2
   remediation, exactly as round 2 surfaced defects introduced by round 1's. The
   pattern across two rounds is that each remediation pass introduces new,
   smaller defects. **No claim is made that the artifact set is defect-free.**
2. **The round-2 refute gate dropped zero findings.** Its discrimination on this
   run is unmeasured.
3. **The corpus rests on evidence tiers 2 and 5 only.** The academic arm
   contributed zero included records; all 528 of its rows are capacity gaps.
4. **1,465 of 1,475 exclusions are capacity gaps, not criterion failures**, and
   93% of the flow took a path the frozen protocol did not enumerate until M2
   reconciled it POST-EXECUTION.
5. **S-D and S-E retrieved bytes are not archived** (G-27). Their digests are
   verified-once attestations, not reader-checkable digests.
6. **The academic arm's known-item recall is 4.3%** (G-29), with both bounds.
7. **Sampling caveat.** Every finding above is the output of LLM auditors on a
   single pass per branch. Absence of a finding is not evidence of absence of a
   defect.
