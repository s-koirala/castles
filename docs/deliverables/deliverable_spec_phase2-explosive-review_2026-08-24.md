---
type: deliverable_spec
slug: phase2-explosive-review
date: 2026-08-24
session_objective: Phase 2 stage 1 — PRISMA 2020 systematic review of real-time explosive-regime date-stamping (SADF/GSADF/PSY family and direct competitors), with protocol registered before searching, dual independent screening with an agreement measure, per-study appraisal, and full-text adjudication of the standing preconditions (Phillips records; NB-02/NB-08/NB-13).
scope_note: Stages 2 (branch-1 test-specification methods note) and 3 (branch-2 assigner review) of the recommended Phase 2 order are OUT OF SCOPE — successor sessions, declared here so their absence is a decision, not an omission.
---

# Deliverables

- [ ] `docs/methodology/protocol_explosive-regime-review_2026-08-24.md`
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

- [ ] Registration commit (mid-session, BEFORE search execution)
  - state: The frozen protocol committed via /commit-with-provenance with its
    SHA-256 recorded in the commit body; search stages begin only after this
    commit exists.
  - check: `git log` shows the protocol commit with trailers timestamped
    before the search logs' recorded execution; protocol SHA in commit body.

- [ ] `docs/literature/search_logs/explosive-regime/` + `docs/literature/references_explosive-regime-dating.json`
  - state: Search executed per the protocol's verbatim queries (deviations
    logged as protocol amendments, never silent); per-query logs; CSL-JSON
    store for all records advanced to screening.
  - check: logs exist with verbatim queries + dates + counts; store parses;
    every query in the protocol has a log or a logged amendment.

- [ ] Dual-screening records + agreement statistic + adjudication log
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
