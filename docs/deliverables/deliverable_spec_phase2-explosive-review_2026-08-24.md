---
type: deliverable_spec
slug: phase2-explosive-review
date: 2026-08-24
session_objective: Phase 2 stage 1 — PRISMA 2020 systematic review of real-time explosive-regime date-stamping (SADF/GSADF/PSY family and direct competitors), with protocol registered before searching, dual independent screening with an agreement measure, per-study appraisal, and full-text adjudication of the standing preconditions (Phillips records; NB-02/NB-08/NB-13).
scope_note: Stages 2 (branch-1 test-specification methods note) and 3 (branch-2 assigner review) of the recommended Phase 2 order are OUT OF SCOPE — successor sessions, declared here so their absence is a decision, not an omission.
---

# Deliverables

- [x] `docs/methodology/protocol_explosive-regime-review_2026-08-24.md` —
  PRISMA-P structure with item coverage; frozen SHA-256
  `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`
  (verified by lead recomputation); 25/25 protocol DOIs handle-resolve
  (Evans 1991 FAIR gap declared)
  - state: Review protocol structured per PRISMA-P 2015 (Moher et al.,
    doi:10.1186/2046-4053-4-1): review question; eligibility criteria fixed in
    advance; named databases with verbatim query templates; dual-independent-
    screening design with the agreement statistic and its adjudication rule
    stated; a per-study appraisal instrument selected and justified (no
    standard RoB tool fits econometric method studies — the chosen instrument
    is protocol-declared, `CONVENTION`-labelled, with design templates cited);
    synthesis plan; PRISMA-2020-item conformance map declaring which items are
    met, partially met (e.g. LLM-agent dual screening is not two humans), or
    inapplicable, each with rationale. ADR-0003 boundary stated: synthesis of
    published operating characteristics only, no simulations run.
  - check: file exists; PRISMA-P item coverage explicit; SHA-256 computed.

- [x] Registration commit — `9deee0ccdee8` at 2026-08-24 10:15:17 -0500,
  subject carries the frozen SHA prefix; full protocol SHA bound as
  `config_resolved_sha256` in pre-commit ReproLog
  `repro_log_35329773772a4e0eac2cb5792d7d3be8.json` (sha256 `656a2369…`);
  all search execution postdates this commit
  - state: The frozen protocol committed via /commit-with-provenance with its
    SHA-256 recorded in the commit body; search stages begin only after this
    commit exists.
  - check: `git log` shows the protocol commit with trailers timestamped
    before the search logs' recorded execution; protocol SHA in commit body.

- [x] `docs/literature/search_logs/explosive-regime/` + `docs/literature/references_explosive-regime-dating.json` —
  62 se- logs on disk incl. dedup ledger and KI recall check; store parses at
  1,996 entries (SHA-256 `2e8d5fc7…`); all 24 topical queries + 4 uncapped
  forward-citation arms + 14 KIs executed post-registration; deviations
  recorded as protocol amendments A1/A2 (append-only); PRESS recall check
  fired on the three pre-seed antecedents (KI-05/13/14), captured via the
  known-item arm
  - state: Search executed per the protocol's verbatim queries (deviations
    logged as protocol amendments, never silent); per-query logs; CSL-JSON
    store for all records advanced to screening.
  - check: logs exist with verbatim queries + dates + counts; store parses;
    every query in the protocol has a log or a logged amendment.

- [x] Dual-screening records + agreement statistic + adjudication log —
  stage-1: R1/R2 verdict files (1,996 each, self-checked), κ=0.433 with raw
  agreement 0.807 and the 2×2 table (se-kappa-computation.json), 386
  disagreements blind-adjudicated (attribution withheld; se-adjudication-input
  carries ids only); stage-2: dual full-text verdicts (586 each), 16
  substantive conflicts blind-adjudicated, 153 access asymmetries resolved
  under amendment A3; frozen screening prompts archived
  (er-screening-prompt.txt); final corpus 72 (flow reconciles at every stage,
  se-included-set.json)
  - state: Two agents screen the identical record set independently against
    the frozen criteria (no shared reasoning); verdict sets preserved
    verbatim; Cohen's kappa computed deterministically by the lead; every
    disagreement adjudicated by the protocol's stated rule with recorded
    rationale.
  - check: two verdict files + kappa computation script output + adjudication
    log under docs/literature/search_logs/explosive-regime/.

- [ ] `docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`
  - state: PRISMA 2020 review: flow accounting (identified/screened/excluded
    with reasons/included); per-study appraisal table using the protocol's
    instrument; synthesis of operating characteristics and validity
    conditions; full-text extraction for included records including BOTH
    Phillips records (discharging the branch-3 precondition — critical-value
    machinery confirmed or corrected from full text); explicit adjudication
    of NB-02, NB-08, NB-13 against the time-t assignment-null standard;
    publication-bias/small-study posture addressed as the protocol declares;
    limitations section maps residual PRISMA gaps.
  - check: flow numbers reconcile with logs and kappa records; appraisal row
    per included study; Phillips full-text sections present; three
    adjudication verdicts explicit.

- [ ] `docs/research_notes/research_agenda_regime-classification_2026-08-21.md` (rev 4)
  - state: Branch 3 integrates the review's verdicts; the "full-text pass
    pending" caveats are discharged or corrected wherever they appear
    (Definitional basis (d), branch 3, Verification status); supersession
    markers added if any Rev 3 claim falls.
  - check: per-site inspection; no stale "pending full-text" caveat remains
    for adjudicated records.

- [ ] `docs/audits/audit_trail_phase2-explosive-review_2026-08-24.md`
  - state: WI-3 §2 trail for this session's audit round(s), attested.
  - check: file exists, written this session, attested.

- [ ] Final commit via /commit-with-provenance
  - state: All deliverables committed with Repro-Log trailers, role=multi.
  - check: `git log -1` shows the three trailers.

# Delegation

- agent: research-librarian (protocol drafter)
  objective: Draft the PRISMA-P protocol — review question, fixed eligibility
    criteria, verbatim query set, screening/adjudication design, appraisal-
    instrument selection with verified design-template citations
    (QUADAS-2/PROBAST as adaptation sources), synthesis plan, conformance map.
  output: The protocol file; return summary of key protocol decisions.
  sources: The naming-sweep corpus records (NB-04/NB-05 and family), prior
    corpora for known coverage, WebSearch/WebFetch + Crossref for template
    citations; PRISMA-P checklist.
  excluded: Runs NO evidence searches — query design only. Does not screen.
  check: deliverable 1's check.

- agent: research-librarian (search executor)
  objective: Execute the frozen protocol's queries verbatim post-registration;
    build the candidate store; log any necessary deviation as an amendment.
  output: Search logs + store; return counts per query.
  sources: Crossref, OpenAlex, Semantic Scholar, arXiv, SSRN per protocol.
  excluded: Does not screen; does not alter eligibility criteria.
  check: deliverable 3's check.

- agent: general-purpose ×2 (independent screeners)
  objective: Each independently applies the frozen eligibility criteria to
    the identical candidate set (title/abstract stage, then full-text stage
    for survivors); no access to the other's verdicts.
  output: Per-record verdict files (include/exclude + criterion cited).
  sources: The candidate store; record abstracts/full texts via WebFetch.
  excluded: No communication with the sibling screener; no criterion
    modification.
  check: two verdict files exist, same record universe.

- agent: general-purpose (disagreement adjudicator)
  objective: Adjudicate only the disagreement set per the protocol's rule,
    blind to which screener gave which verdict.
  output: Adjudication log with per-record rationale.
  sources: Frozen criteria + the disputed records.
  excluded: Cannot revisit agreed records.
  check: adjudication log covers exactly the disagreement set.

- agent: research-librarian (extraction + synthesis)
  objective: Full-text extraction on included records (dual-extraction
    partial-compliance declared per protocol), appraisal-instrument
    application per study, synthesis, and the three NB adjudications; writes
    the review.
  output: The review file; return summary with flow numbers and verdicts.
  sources: Included full texts, protocol, appraisal instrument.
  excluded: Cannot add records outside the adjudicated included set.
  check: deliverable 5's check.

- agent: audit-remediate round(s) (post-integration)
  objective: Specialist audit — protocol-vs-execution fidelity (registration
    before search; verbatim queries; criteria drift), kappa computation
    correctness, appraisal honesty, Phillips full-text claims, agenda
    integration, PRISMA conformance-map truthfulness.
  output: Attested findings + trail.
  sources: All session artifacts + primary sources.
  excluded: G16 publisher-403 class closed; prior specs' logged minors not
    re-raised.
  check: round report; attested trail.

# Self-executed

- Protocol freeze (SHA-256), registration commit, kappa computation script,
  adjudication-set assembly  (reason: deterministic bookkeeping and
  computation, no authored research content)
- Agenda rev 4 integration edits  (reason: transcription integrating
  delegated results — recorded Rule 1 deviation, routed through the audit
  round)
- Spec ticks, trail addenda, ReproLog, commits  (reason: gate-mandated
  bookkeeping)
