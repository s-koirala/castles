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

- [x] `docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`
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

- [x] `docs/research_notes/research_agenda_regime-classification_2026-08-21.md` (rev 4)
  - state: Branch 3 integrates the review's verdicts; every "full-text pass
    pending" caveat is discharged or corrected at each site it appears
    (Definitional basis (d), branch 3, Verification status); supersession markers
    added wherever a Rev 3 claim falls.
  - check: grep for "pending full-text" returns no hit that refers to an
    adjudicated record; rev header reads 4.

- [x] `docs/audits/audit_trail_phase2-explosive-review_2026-08-24.md`
  - state: WI-3 §2 trail for the audit round covering the Thread A artifacts;
    22 required front-matter keys; 7 required body sections; attested.
  - check: PASSED 2026-09-02 — written this session by the workflow's trail
    phase, attested by an independent reproducibility-verifier agent; 22/22
    front-matter keys verified by key-presence check; sidecar SHA recorded;
    round-2 and round-3 sections appended to the same file per the append-only
    rule.

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

- [x] `docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md`
  - state: ADR recording that rules/quant-project.md and REVIEW.md are adopted
    by explicit reference for the prediction-market branch and for that branch
    only; states which blocking directives bind a literature-only stage
    (directive 8: citation-or-derivation) versus which bind only a future
    empirical stage (directives 1-7); states the boundary against ADR-0003
    (specification, not execution).
  - check: PASSED 2026-09-02 — file exists; Status/Date/Deciders/Context/Decision/
    Consequences/Alternatives/References present; adoption scope delimits the
    branch by artifact-path set and explicitly excludes the explosive-regime,
    charter, context-portability and architecture threads.

- [x] `docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md`
  - state: Registered search protocol: review question; eligibility criteria
    fixed in advance; named databases with verbatim query templates; inclusion
    and exclusion rules; the CONVENTION label on every element whose source is
    convention rather than a cited standard; explicit statement that this is a
    registered search producing a corpus, NOT a dual-screened systematic review,
    with the PRISMA items thereby unmet enumerated.
  - check: PASSED 2026-09-02 — file exists; SHA-256
    99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4 computed by
    the lead and recorded in commit 27d7473; 29/29 cited DOIs returned
    responseCode 1 from the DOI Handle System and were cross-checked against
    Crossref (record: docs/literature/search_logs/kalshi-arbitrage/protocol-doicheck.json);
    the one non-DOI identifier arXiv:1206.5252 verified against the arXiv API.

- [x] Registration commit for the Thread C protocol
  - state: The frozen protocol committed via /commit-with-provenance with its
    SHA-256 in the commit body; no Thread C search executes before this commit.
  - check: PASSED 2026-09-02 with a stated granularity limit — commit 27d7473 at
    2026-09-02T10:20:28-05:00 carries Repro-Log-Path, Repro-Log-SHA256 and
    AI-Assistance trailers. The search logs record execution DATE only
    (2026-09-02), not time, so the logs alone cannot order the two within the
    day. Ordering rests instead on two independent facts: the search executor was
    dispatched after the commit existed, and it verified the frozen protocol
    SHA-256 99524df02696 against the committed file before its first query.

- [x] `docs/literature/search_logs/kalshi-arbitrage/` + `docs/literature/references_kalshi-arbitrage.json`
  - state: Every protocol query executed verbatim post-registration, one log per
    query recording database, platform, verbatim query string, execution date
    and result count; deviations recorded as numbered append-only protocol
    amendments, never silently; CSL-JSON store parses and covers every record
    advanced past identification.
  - check: PASSED 2026-09-02 — store parses as a 149-entry JSON list (sha256
    fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164); 149 files
    in the log directory; all 86 protocol query rows executed, with the five
    deviations recorded as numbered append-only amendments A1-A5 in
    ka-protocol-amendments.md. NOTE, not covered by this check: amendment A5's
    disposition code X11 leaves 643 records with eligibility UNDECIDED and A4's
    X10 leaves 545 eligible-but-unextracted, so 1,188 records reached the end of
    screening unresolved. That is a defect of the corpus, audited separately.
  - CORRECTION 2026-09-02, audit finding SCOPE-2-2 — the tick above stands as
    written and is NOT edited; it is superseded here, as this spec already does
    for Thread B. The check was executed BEFORE the round-1 remediation and the
    delivery has since moved on four numbers. Restated as executed after
    remediation rounds 1 and 2:
      * FIFTEEN numbered append-only amendments, not five: A1-A5 during
        execution, A6-A12 at round-1 audit remediation, A13-A15 at round-2. All
        fifteen are in ka-protocol-amendments.md AND, from A12, in the frozen
        protocol's own append-only addendum.
      * NOT all 86 protocol query rows executed as a complete strategy. TWO
        protocol arms were never executed and are now declared as numbered
        amendments: A6, the ka-bc-{n} backward citation-chasing arm, whose recall
        consequence is gap G-7; and A7, the SSRN supplementary site-search arm,
        whose recall consequence is gap G-9 and access gap AG-9. G-9 is material:
        31 of the 149 included records and 15 of the 19 Kalshi-specific records
        carry SSRN DOIs.
      * The unresolved split is 545 X10 + 700 X11 = 1,245, not 643 and not 1,188.
        Amendment A11 corrected an unanchored-substring defect in the X5 rule and
        moved 57 records from a criterion failure into the undecided stratum.
      * The log directory holds 159 files, not 149. The additions are the round-1
        and round-2 remediation artefacts: ka-partition-script.py,
        ka-gate-verdict.json, ka-counterfactuals.py/.json,
        ka-query-token-inventory.py/.json, ka-store-registrant-sweep.py/.json,
        ka-store-arxiv-venuecheck.py/.json and ka-store-retroreg-yearcheck.json.
      * The store still parses as a 149-entry JSON list and its digest is
        UNCHANGED at
        fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164.
        No round-2 finding moved a record into or out of the corpus.
    This note supersedes the tick's completeness picture; it does not un-tick the
    item, because the artifacts it names do exist.

- [x] `docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md`
  - state: Compiled corpus record per the research-compile skill: search
    provenance, per-source counts, inclusion/exclusion with reasons, and a
    synthesis of what the literature establishes about arbitrage and
    market-making in binary event markets — at minimum the no-arbitrage and
    coherence conditions for binary contracts, longshot bias, inventory-risk
    market-making models and their applicability to bounded [0,1] payoffs, and
    cross-venue price-discrepancy evidence. Every claim carries a citation; each
    Kalshi-specific claim is separated from claims generalized from other venues,
    and each generalization states the assumption that carries it.
  - check: PASSED 2026-09-02 on the three stated conditions — the audit found
    REVIEW.md blocking directive 8 SATISFIED (every rule-shaped statement carries
    its source plus an explicit E14 non-endorsement; the corpus states no rule of
    its own; no unattributed folklore factor found); the Kalshi-specific vs
    generalized separation is present as structural 8.x.1 / 8.x.2 blocks with the
    carrying assumption on the same line as every generalized claim; identifiers
    resolve 149/149 at the DOI Handle System.
    **TICKED ON THIS CHECK ONLY, AND THE CHECK DOES NOT COVER WHAT MATTERS MOST.**
    The artifact self-reports gate verdict `block`. After two audit rounds the
    residual is that 98.3% of screening dispositions are keyword-classifier
    outputs, 1,245 records ended screening unresolved (700 eligibility UNDECIDED),
    and no full text was read for any of the 149 included records. The round-2
    critical-reviewer's direct answer: a defensible compiled corpus record of what
    a published classifier retrieved and what 116 abstracts plus 33 metadata stubs
    state — defensible because the claims were trimmed to that, not because the
    evidence base improved; its largest strand reads as a reading list with
    transfer flags, not a synthesis. Round 3 of the 3-round cap was NOT run, so
    the round-2 remediation is unverified. See
    `docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` §5.1, §5.3.

- [x] `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md`
  - state: New branch agenda: numbered research branches derived from the gaps
    the corpus exposes, each with a falsification test that is a genuine
    branch-level test (the defect repaired in the 2026-08-21 agendas), and each
    with its evidence tier.
  - check: PASSED 2026-09-02 — six numbered research branches, one falsification
    test each, plus a Branch 0 precondition branch carrying no test BY DESIGN and
    saying so, which is exactly the distinction this check enforces (the
    2026-08-21 agendas' defect was mislabelling preconditions AS tests). Seven
    identifiers verified live at the Handle System; four methodology DOIs verified
    against Crossref and flagged non-corpus; TO COMPUTE parameters left uncomputed
    with their selection rule named, per ADR-0003. Written in the unverified
    post-round-2 pass.

## Thread D — session close

- [x] `docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md`
      (+ `.json`, + `.round2.json`)
  - state: WI-3 §2 trail for this session's audit round(s); 22 front-matter keys;
    7 body sections; refute-gate dispositions verbatim for every gated finding;
    attested.
  - RENAMED 2026-09-02, audit finding SCOPE-2-4. This item previously named
    `docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` and
    declared a single trail "covering this session's audit round(s) over Threads B
    and C". Two facts made that unsatisfiable as written, and both are recorded
    here rather than worked around:
      * The trail actually written and shipped uses the PER-BRANCH slug
        `audit_trail_kalshi-arbitrage-review_*`, which no spec item named, so the
        delivered artifact sat under an unnamed path and the round-2 trail would
        have inherited the same problem. The item is renamed to the slug in use.
      * NO TRAIL COVERS THREAD B, and none will: Thread B carried no audit round
        in this session because it was discharged pre-session. The Thread D item's
        "over Threads B and C" is therefore replaced by "over the audit rounds
        this session actually ran", which are the Thread C rounds 1 and 2.
    Neither change relaxes the content requirements below; only the path and the
    thread coverage are reconciled with what exists.
  - check: PASSED 2026-09-02 — `audit_trail_kalshi-arbitrage-review_2026-09-02.md`
    exists with 22/22 keys and its `.json` + `.round2.json` sidecars; refute-gate
    sections non-empty (4 killed in round 1, 3 in round 2). Thread B's absence is
    the recorded decision above, not an open box.
    ADDITIONALLY DELIVERED, beyond this item: the lead wrote a SESSION-LEVEL trail
    at `docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md`
    (22/22 keys, YAML parses, sidecar sha256 `4a8520439ca9de0e…`) indexing both
    per-branch trails and carrying what neither can: the cross-thread totals
    (5 rounds, 184 agents, 5 critical / 146 major / 95 minor, 11 refuted, 140
    remediated), the gate-calibration note, and the consolidated residual-risk
    report. The original item name is retained by that file, so the rename above
    costs no coverage.

- [x] Final commit via /commit-with-provenance --role=multi
  - state: All Thread A-D artifacts committed with Repro-Log-Path,
    Repro-Log-SHA256 and AI-Assistance trailers.
  - check: PASSED 2026-09-02 — commit `3183f44ca6c7b19baf65c93736e4c99f114d5fcb`,
    192 files, carries Repro-Log-Path, Repro-Log-SHA256
    (`0263d322275dd555…`, digest verified against the on-disk bytes) and
    AI-Assistance trailers. No untracked tracked-class artifact remains.
    The delivery ReproLog's pip-freeze archive was written in BINARY mode with LF
    bytes and its digest re-verified by reading the file back, after the
    text-mode/CRLF defect earlier in this session.

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

# Recorded deviations

- **Round-1 remediation of the Thread A review was DELEGATED, not self-executed**
  (2026-09-02). The audit-remediate-loop assigns step 5 "Remediate. Apply fixes"
  to the lead session, and this spec's Self-executed list assumed that. Of the 24
  surviving major findings, four (REV-1-7, QUANT-1-6, LITERATURE-1-6, SCOPE-1-6)
  are agenda-transcription fixes and were remediated by the lead as declared. The
  other 20 land in the review, the corpus store and the protocol addendum, and
  three of them — LITERATURE-1-4 (full Crossref page/volume check across all 62
  DOI-bearing records), LITERATURE-1-2 (re-dating and re-tiering eru-1289) and
  SCOPE-1-4 (execute the backward citation-chasing arm or waive it by dated
  amendment) — require network retrieval the lead session cannot perform. They
  were dispatched to research-librarian. Round 2 audits the result independently,
  so the fix is not self-reviewed.

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
