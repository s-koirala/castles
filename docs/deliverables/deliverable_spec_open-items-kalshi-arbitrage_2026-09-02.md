---
type: deliverable_spec
slug: open-items-kalshi-arbitrage
date: 2026-09-02
session_objective: Close every open item carried by this project — the four unchecked Phase 2 explosive-regime deliverables and the two standing round-3 audit failures — and open a new prediction-market branch with a registered literature search on arbitrage and market-making in binary event markets (Kalshi-specific where the literature supports it).
scope_note: |
  Objective wording "all open items, expanding literature search to arbitrage opportunities in market making in KALSHI" is read as two threads, stated explicitly because the reading is load-bearing:
  (a) open items = the four unchecked boxes in deliverable_spec_phase2-explosive-review_2026-08-24.md. The two round-3 audit failures described as open in gate_waiver_65148ad5-9c9.md were checked at the start of this session and found ALREADY DISCHARGED at commit a150e74; Thread B below records that check and carries no remediation work. The declaration retains Thread B rather than deleting it, because the objective named those items and their absence would otherwise be unexplained.
  (b) the Kalshi thread is a REGISTERED LITERATURE SEARCH producing a compiled corpus (research-compile), NOT a dual-screened PRISMA 2020 systematic review. A dual-screened review of this corpus, any empirical microstructure analysis, any data acquisition from the Kalshi API, and any backtest or trading rule are OUT OF SCOPE — successor sessions, declared here so their absence is a decision, not an omission.
  Rule-adoption note: the Kalshi branch IS time-indexed financial analysis, so rules/quant-project.md and REVIEW.md bind it by explicit adoption per CLAUDE.md §Scope. ADR-0004 records that adoption; it does not extend to the explosive-regime or charter threads.
---

# Deliverables

## Thread A — Phase 2 explosive-regime review close-out

- [ ] `docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`
  - state: PRISMA 2020 review over the frozen 72-record included corpus: flow
    accounting (identified/screened/excluded-with-reasons/included) reconciling
    with the search logs and kappa records; one appraisal row per included study
    using the protocol's declared instrument; synthesis of operating
    characteristics and validity conditions; full-text extraction for BOTH
    Phillips records discharging the branch-3 precondition; explicit adjudication
    of NB-02, NB-08 and NB-13 against the time-t assignment-null standard;
    publication-bias posture per protocol; limitations mapping residual PRISMA
    gaps.
  - check: flow numbers reconcile against
    `docs/literature/search_logs/explosive-regime/se-included-set.json` and
    `se-kappa-computation.json`; appraisal row count equals 72; both Phillips
    full-text sections present; three NB verdicts explicit.

- [ ] `docs/research_notes/research_agenda_regime-classification_2026-08-21.md` (rev 4)
  - state: Branch 3 integrates the review's verdicts; every "full-text pass
    pending" caveat is discharged or corrected at each site it appears
    (Definitional basis (d), branch 3, Verification status); supersession markers
    added wherever a Rev 3 claim falls.
  - check: grep for "pending full-text" returns no hit that refers to an
    adjudicated record; rev header reads 4.

- [ ] `docs/audits/audit_trail_phase2-explosive-review_2026-08-24.md`
  - state: WI-3 §2 trail for the audit round covering the Thread A artifacts;
    22 required front-matter keys; 7 required body sections; attested.
  - check: file exists, written this session, all 22 keys present, sidecar SHA
    recorded.

## Thread B — standing round-3 audit failures

**Thread B was already discharged before this session opened.** Check run
2026-09-02: `deliverable_spec_think-tank-charter_2026-08-21.md` carries zero
unchecked boxes. Both items were remediated and ticked under
`deliverable_spec_round3-remediation_2026-08-21.md` at commit `a150e74`
("remediate round-3 failures; charter Rev 3 citations, agenda branch-1
attributions"), each with per-section check output recorded inline and the
round-3 failure record retained unedited beneath the tick, confirmed by audit
rounds 1-2 in `docs/audits/audit_trail_round3-remediation_2026-08-21.md`.

`gate_waiver_65148ad5-9c9.md` (2026-08-21) describes these two items as open.
That waiver states the position at the moment it was written; the remediation
commit postdates it. The waiver is an audit record and is not edited — this
note supersedes its Thread B description. No remediation work is carried out
under this spec for Thread B, and the boxes below are ticked on the check
having been run, not on work performed this session.

- [x] `docs/methodology/charter_castles_2026-08-21.md` — round-3 failure disposition
  - state: The recorded round-3 failure is either remediated on its per-section
    evidence (spec lines 10-19 of
    `deliverable_spec_think-tank-charter_2026-08-21.md`) and re-audited to a
    passing verdict, OR explicitly accepted by a dated acceptance note naming
    each unremediated finding. One of the two, never silence.
  - check: PASSED 2026-09-02 — `deliverable_spec_think-tank-charter_2026-08-21.md`
    item 1 is ticked and cites the disposition path
    `deliverable_spec_round3-remediation_2026-08-21.md`, with per-section
    evidence (Standing commitments 4/1, Admissible output types 4/0, Evidence
    standard 1/1, Publication-bias posture 3/0, Negative-result protocol 1/2,
    Failure taxonomy 0/1, Prior art posture 7/0, Falsification of commitment 1
    1/0 — all eight claim-bearing H2 spans PASS individually).

- [x] `docs/research_notes/research_agenda_architecture_2026-08-21.md` — round-3 failure disposition
  - state: As above against spec lines 25-32.
  - check: PASSED 2026-09-02 — item 2 is ticked and cites the same disposition
    path, with per-branch evidence (1. Platform selection 9 citations /
    Falsification Y; 2. Prior art 6/Y; 3. Human-in-the-loop frame 7/Y — all
    three branches PASS individually; branch 1 was 0 before remediation).
    Branch-1 attributions verified against Crossref.

## Thread C — Kalshi / binary-event-market arbitrage branch

- [ ] `docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md`
  - state: ADR recording that rules/quant-project.md and REVIEW.md are adopted
    by explicit reference for the prediction-market branch and for that branch
    only; states which blocking directives bind a literature-only stage
    (directive 8: citation-or-derivation) versus which bind only a future
    empirical stage (directives 1-7); states the boundary against ADR-0003
    (specification, not execution).
  - check: file exists; ADR template sections present; adoption scope names the
    branch, not the repository.

- [ ] `docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md`
  - state: Registered search protocol: review question; eligibility criteria
    fixed in advance; named databases with verbatim query templates; inclusion
    and exclusion rules; the CONVENTION label on every element whose source is
    convention rather than a cited standard; explicit statement that this is a
    registered search producing a corpus, NOT a dual-screened systematic review,
    with the PRISMA items thereby unmet enumerated.
  - check: file exists; SHA-256 computed and recorded; every DOI cited in the
    protocol handle-resolves.

- [ ] Registration commit for the Thread C protocol
  - state: The frozen protocol committed via /commit-with-provenance with its
    SHA-256 in the commit body; no Thread C search executes before this commit.
  - check: `git log` shows the protocol commit with Repro-Log trailers,
    timestamped before the earliest execution date in the Thread C search logs.

- [ ] `docs/literature/search_logs/kalshi-arbitrage/` + `docs/literature/references_kalshi-arbitrage.json`
  - state: Every protocol query executed verbatim post-registration, one log per
    query recording database, platform, verbatim query string, execution date
    and result count; deviations recorded as numbered append-only protocol
    amendments, never silently; CSL-JSON store parses and covers every record
    advanced past identification.
  - check: the store parses as JSON under the project venv; every protocol query
    has a log file or a logged amendment.

- [ ] `docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md`
  - state: Compiled corpus record per the research-compile skill: search
    provenance, per-source counts, inclusion/exclusion with reasons, and a
    synthesis of what the literature establishes about arbitrage and
    market-making in binary event markets — at minimum the no-arbitrage and
    coherence conditions for binary contracts, longshot bias, inventory-risk
    market-making models and their applicability to bounded [0,1] payoffs, and
    cross-venue price-discrepancy evidence. Every claim carries a citation; each
    Kalshi-specific claim is separated from claims generalized from other venues,
    and each generalization states the assumption that carries it.
  - check: every claim line carries a resolvable citation; a Kalshi-specific vs
    generalized separation is present as a column or a section boundary; zero
    unattributed factors per REVIEW.md blocking directive 8.

- [ ] `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md`
  - state: New branch agenda: numbered research branches derived from the gaps
    the corpus exposes, each with a falsification test that is a genuine
    branch-level test (the defect repaired in the 2026-08-21 agendas), and each
    with its evidence tier.
  - check: one falsification test per branch; no test that is a design-resolution
    study, precondition, or adoption policy mislabelled as a test.

## Thread D — session close

- [ ] `docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md`
  - state: WI-3 §2 trail for this session's audit round(s) over Threads B and C;
    22 front-matter keys; 7 body sections; refute-gate dispositions verbatim for
    every gated finding; attested.
  - check: file exists, written this session, 22 keys present, sidecar SHA
    recorded, refute-gate section non-empty or explicitly stating zero gated
    findings.

- [ ] Final commit via /commit-with-provenance --role=multi
  - state: All Thread A-D artifacts committed with Repro-Log-Path,
    Repro-Log-SHA256 and AI-Assistance trailers.
  - check: `git log -1` shows the three trailers; `git status --short` shows no
    untracked tracked-class artifact.

# Delegation

- agent: research-librarian
  objective: Write the Thread A review — full-text extraction, per-study
    appraisal, synthesis, PRISMA 2020 flow accounting, and the three NB
    adjudications — over the already-frozen 72-record included corpus.
  output: `docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`,
    plus a returned summary giving the flow numbers at every PRISMA stage and
    the three NB verdicts.
  sources: `docs/methodology/protocol_explosive-regime-review_2026-08-24.md`,
    `docs/literature/search_logs/explosive-regime/` (se-included-set.json,
    se-kappa-computation.json, adjudication logs),
    `docs/literature/references_explosive-regime-dating.json`, full texts via
    WebFetch, Crossref.
  excluded: MUST NOT add, drop or re-screen any record outside the adjudicated
    72-record included set; MUST NOT alter the frozen protocol or its
    eligibility criteria; runs no simulations (ADR-0003 boundary).

- agent: research-librarian
  objective: Draft the Thread C search protocol — review question, fixed
    eligibility criteria, verbatim query set across the named databases,
    inclusion/exclusion rules, and the enumerated list of PRISMA items a
    corpus-only stage does not meet.
  output: `docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md`,
    plus a returned summary of the protocol's key design decisions and the
    query count.
  sources: WebSearch/WebFetch, Crossref, OpenAlex for template and standard
    citations; PRISMA-P 2015 checklist; the existing
    `protocol_explosive-regime-review_2026-08-24.md` as a structural precedent
    only.
  excluded: MUST run NO evidence searches — query design only; MUST NOT screen
    records; MUST NOT assert any substantive claim about prediction-market
    microstructure.

- agent: research-librarian
  objective: Execute the frozen Thread C protocol's queries verbatim after the
    registration commit exists, build the CSL-JSON candidate store, apply the
    protocol's inclusion/exclusion rules with recorded reasons, and write the
    compiled corpus record.
  output: `docs/literature/search_logs/kalshi-arbitrage/` (one log per query),
    `docs/literature/references_kalshi-arbitrage.json`, and
    `docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md`; returned
    summary gives per-query counts and the final included count.
  sources: Crossref, OpenAlex, Semantic Scholar, arXiv, SSRN, NBER, and the CFTC
    public record for venue-structural facts; full texts via WebFetch.
  excluded: MUST NOT modify the frozen eligibility criteria — any deviation is a
    numbered append-only amendment; MUST NOT acquire Kalshi market data, call
    any exchange API, or state a tradeable rule; MUST NOT present a claim
    generalized from another venue as a Kalshi-specific finding.

- agent: literature-check
  objective: Verify every citation and every attributed method claim in the two
    Thread C artifacts and in the Thread A review against primary sources.
  output: Structured findings JSON per the audit-remediate-loop 8-field schema.
  sources: The artifact files; Crossref, WebFetch of primary sources.
  excluded: Returns findings only; MUST NOT edit any file; MUST NOT re-raise
    the G16 publisher-403 class closed in the prior spec.

- agent: audit-remediate-loop (7-branch specialist round, 3-round cap)
  objective: Audit Threads A, B and C — protocol-vs-execution fidelity for
    Thread C (registration precedes search, verbatim queries, no criteria
    drift), REVIEW.md directive-8 compliance on the corpus synthesis, the
    Kalshi-specific-vs-generalized separation, Thread A appraisal honesty and
    Phillips full-text claims, agenda falsification-test genuineness, and
    whether the Thread B round-3 findings are actually discharged.
  output: Attested findings with refute-gate dispositions, and the two audit
    trail files under `docs/audits/`.
  sources: All session artifacts, the frozen protocols, CLAUDE.md,
    rules/quant-project.md, REVIEW.md, and primary sources.
  excluded: MUST NOT re-raise minors logged in prior specs; MUST NOT drop any
    critical/major finding without concrete enumerated counter-evidence per the
    refute-gate triage rule.

# Self-executed

- Thread B remediation edits to `charter_castles_2026-08-21.md` and
  `research_agenda_architecture_2026-08-21.md`  (reason: remediation is the lead
  session's step 5 of the loop by construction — the skill assigns "Remediate.
  Apply fixes" to the lead, and the fixes are then re-audited by the delegated
  round, so this is not self-audit)
- Thread A agenda rev 4 integration edits  (reason: transcription of delegated
  results into an existing file, carrying no authored research content of its
  own — recorded Rule 1 deviation, routed through the delegated audit round)
- `ADR-0004-quant-rule-adoption-prediction-markets.md`  (reason: a decision
  record of the author's own scope choice, not an analysis deliverable; it
  asserts no research claim — routed through the delegated audit round for
  scope-consistency against ADR-0001/ADR-0003 rather than claiming an exclusion)
- Protocol freeze SHA-256, registration commit, spec ticks, ReproLog emission,
  trail `git add`, final commit  (reason: gate-mandated deterministic
  bookkeeping and hashing, no authored research content)
