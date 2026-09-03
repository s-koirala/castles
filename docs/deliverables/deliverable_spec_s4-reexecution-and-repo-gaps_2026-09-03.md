---
type: deliverable_spec
slug: s4-reexecution-and-repo-gaps
date: 2026-09-03
session_objective: Re-execute the Kalshi corpus narrowly on the S4 inventory-risk strand — finish the screening that was never finished and read full texts for the strand's core records — then close the repository reproducibility gaps, verify the load-bearing explosive-regime locators, and produce the refute-gate calibration memo.
scope_note: |
  Objective wording "the re-execution, then the rest of the tasks you proposed" is read against the four recommendations made at the close of the 2026-09-02 session:
  (1) re-execute narrowly rather than run a third Kalshi audit round, scoped to the S4 inventory-risk strand — ACCEPTED, Thread A;
  (2) fix the repository reproducibility gaps VG-14 and VG-16 — Thread B;
  (3) targeted locator verification on load-bearing explosive-regime claims, NOT a full 60-record sweep — Thread C;
  (4) examine the refute-gate kill rate — Thread D, delivered as a memo.
  Ordering is as the objective states: Thread A first; B, C, D follow.

  WHAT THE RE-EXECUTION IS, AND IS NOT. The 700 X11 records carry eligibility UNDECIDED — they were promoted under the transfer clause and never assessed at stage 2. Deciding them is COMPLETING a screen that was never completed, not re-screening a settled one. It will change the corpus composition, and that is the point: the 149-record corpus was never legitimately frozen, because its eligible set was undetermined at ~4.7x its included set. The 545 X10 records (eligible, extraction not performed) are NOT re-opened here.

  OUT OF SCOPE, declared so the absence is a decision: a third Kalshi audit round on the 2026-09-02 prose; re-screening the 8,663 classifier-verdicted records; any Kalshi market data, API call, backtest or tradeable rule (ADR-0003, ADR-0004); any edit to `~/.claude` — Thread D produces a memo and a proposed diff, and applying it is the author's call in a separate action.
---

# Deliverables

## Thread A — S4 inventory-risk re-execution

- [ ] `docs/literature/search_logs/kalshi-arbitrage/ka-s4-completion-screen.jsonl` + its amendment entry
  - state: Every X11 record whose transfer clause bears on strand S4 is assessed
    at stage 2 against the FROZEN eligibility criteria and given a terminal
    verdict with the criterion cited; every X11 record NOT in that subset keeps
    `undecided` and is counted. The stage is declared by a numbered append-only
    amendment in the Kalshi protocol addendum stating that this completes a
    screen left incomplete, names the S4 subset rule fixed BEFORE assessment,
    and states that assessment was by reading, not by the classifier.
  - check: the verdict file parses; its record count equals the S4 subset size;
    every row cites a criterion; the residual `undecided` count is stated and
    the two counts sum to 700; the amendment exists and the protocol's frozen
    prefix still hashes to
    `99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`
    over its first 82,677 bytes.

- [ ] `docs/literature/search_logs/kalshi-arbitrage/ka-s4-fulltext-extraction.jsonl`
  - state: Full-text extraction for the S4 core set — at minimum the named
    inventory-risk and market-scoring-rule lineage anchors, four of five of
    which stood at metadata depth: Glosten & Milgrom 1985, Kyle 1985, Ho & Stoll
    1981, Avellaneda & Stoikov 2008, Guéant/Lehalle/Fernandez-Tapia 2013, Hanson
    LMSR, Chen & Pennock, Othman et al. 2013, Abernethy/Chen/Vaughan 2013, Kroer
    et al. 2016 — plus every S4 record newly included by the completion screen.
    Each record records extraction DEPTH reached and, per protocol field E10,
    the applicability conditions the authors themselves state for a payoff
    bounded in [0,1] settling at an endpoint. Where a full text could not be
    obtained, the record says so and says what could not be extracted; no
    abstract content is presented as full-text extraction.
  - check: one row per core-set record; every row carries a depth field; the
    count of rows at `fulltext` depth is stated explicitly against the count
    attempted; every inaccessible record is named with its failure mode.

- [ ] `docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md` (revised in place)
  - state: Revision note at the head recording this re-execution; flow
    accounting restated with the new include count and the residual undecided
    count; §8.4 (S4) rewritten on the full-text evidence, replacing statements
    that rested on abstracts with statements that rest on what the authors
    state, and marking every claim that still rests on an abstract; the
    "read this as a reading list, not a synthesis" caveat either discharged for
    S4 with its evidence or retained with the reason it survives.
  - check: the revision note names this spec; the flow numbers reconcile with
    the two new log files; no §8.4 claim line asserts an applicability condition
    at abstract depth without saying so.

- [ ] `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-03.md` (rev 2, or an in-place revision of the 2026-09-02 file)
  - state: The S4-derived branches are re-grounded on the full-text evidence;
    any branch whose premise the full texts contradict is corrected or withdrawn
    with a supersession marker; Branch 0's precondition status is restated
    against whatever venue-structural facts remain unretrieved.
  - check: every S4-derived branch cites a full-text-depth record or is marked
    as resting on abstract depth; no withdrawn premise remains unmarked.

## Thread B — repository reproducibility gaps

- [ ] `uv.lock` tracked, and the pinning decision recorded
  - state: `uv.lock` is committed, closing VG-14's clone-durability half. The
    `pyproject.toml` unpinned-dependency question is decided one way and the
    decision recorded with its reason — either dependencies are pinned, or the
    lockfile is declared the pinning mechanism and `pyproject` stays a range
    specification.
  - check: `git ls-files uv.lock` returns the path; the decision appears in a
    tracked file with its rationale.

- [ ] `tests/test_erob_recount.py`
  - state: A test that re-derives the ER-RoB appraisal table's domain-concern
    column from the extraction JSONLs under the frozen protocol's Q→D rule and
    asserts it against the table shipped in the review, so the review's central
    appraisal claim has a runnable reproduce target. The test states which
    divergences are EXPECTED (the 31 lenient-direction and 13 opposite-direction
    cells recorded under amendment A8) and fails on any divergence outside that
    recorded set.
  - check: `uv run pytest tests/test_erob_recount.py` exits 0; the test reads
    the JSONLs rather than hardcoding the expected table; deleting a row from
    the input makes it fail.

## Thread C — targeted locator verification, explosive-regime review

- [ ] `docs/literature/search_logs/explosive-regime/se-verify-loadbearing-01.json`
  - state: Every page locator and quoted string carrying a §7 synthesis claim or
    cited by `research_agenda_regime-classification_2026-08-21.md` is verified
    against the retrieved full text. Records outside that load-bearing set are
    NOT swept, and the boundary is stated. Each verification records the
    retrieval route, the content digest, and verified / corrected / unverifiable.
  - check: the log lists every load-bearing locator with a verdict; corrections
    are applied at every site in the review AND the agenda; the count of records
    verified is stated against the 72-record corpus so the residual is visible.

## Thread D — refute-gate calibration

- [ ] `docs/research_notes/memo_refute-gate-calibration_2026-09-03.md`
  - state: Memo establishing whether the 2026-09-02 session's 7.3% refute-gate
    kill rate (11 of 151 gated) indicates accurate auditors or insufficiently
    adversarial refuters. Uses the five rounds' recorded refute-gate
    dispositions as its data: the distribution of `evidence_type` across the 11
    drops, whether retained findings carried refutation attempts with concrete
    counter-evidence or bare doubt, and whether the round-2 zero-kill result has
    a structural explanation. States which of the two hypotheses the evidence
    supports, or that it does not separate them. Ends with a concrete proposed
    change to the refuter brief, as a diff, and the eval that would test it.
  - check: the memo's numbers reconcile with the three audit trails' recorded
    dispositions; every claim about a finding cites that finding's id; the
    proposed diff is concrete enough to apply.

## Thread E — session close

- [ ] `docs/audits/audit_trail_s4-reexecution-and-repo-gaps_2026-09-03.md`
  - state: WI-3 §2 trail for this session's audit round(s); 22 front-matter
    keys; 7 body sections; refute-gate dispositions verbatim for every gated
    finding; attested.
  - check: file exists, written this session, 22 keys present and the front
    matter parses as YAML, sidecar SHA recorded, refute-gate section non-empty
    or explicitly stating zero gated findings.

- [ ] Final commit via /commit-with-provenance --role=multi
  - state: All Thread A–E artifacts committed with Repro-Log-Path,
    Repro-Log-SHA256 and AI-Assistance trailers.
  - check: `git log -1` shows the three trailers; `git status --short` shows no
    untracked tracked-class artifact.

# Delegation

- agent: research-librarian
  objective: Fix the S4 subset rule BEFORE assessing anything, then assess every
    X11 record in that subset at stage 2 against the frozen eligibility criteria
    by reading the record, and give each a terminal verdict with its criterion.
  output: `ka-s4-completion-screen.jsonl` (one row per assessed record: id,
    verdict, criterion cited, depth read, rationale), the numbered protocol
    amendment declaring the stage, and a returned summary giving the subset
    rule, the subset size, the include/exclude split, and the residual undecided
    count.
  sources: `ka-screening-verdicts.jsonl`, `references_kalshi-arbitrage.json`,
    the frozen protocol's §2 criteria, record abstracts and full texts via
    WebFetch, Crossref/OpenAlex for metadata.
  excluded: MUST NOT alter any frozen eligibility criterion; MUST NOT re-open
    the 545 X10 records; MUST NOT use the keyword classifier to produce any
    verdict in this stage — every verdict is from reading; MUST NOT touch the
    8,663 records already terminally verdicted.

- agent: research-librarian
  objective: Extract at full-text depth for the S4 core set and rewrite §8.4 of
    the corpus record on that evidence.
  output: `ka-s4-fulltext-extraction.jsonl`, the revised
    `lit_review_kalshi-arbitrage_2026-09-02.md`, and a returned summary giving
    the count reached at full-text depth against the count attempted, the E10
    applicability conditions found, and every claim that still rests on an
    abstract.
  sources: The S4 core set and the completion screen's new includes; publisher
    full texts, arXiv, SSRN, institutional repositories via WebFetch.
  excluded: MUST NOT present abstract content as full-text extraction; MUST NOT
    state a tradeable rule or an applicability condition the authors do not
    state; MUST NOT admit records the completion screen excluded.

- agent: research-librarian
  objective: Verify every load-bearing locator and quoted string in the
    explosive-regime review — those carrying a §7 synthesis claim or cited by
    the regime-classification agenda — against the retrieved full texts, and
    correct every site of every error found.
  output: `se-verify-loadbearing-01.json` plus the corrections applied in the
    review; returned summary giving the load-bearing set size, verified /
    corrected / unverifiable counts, and every correction the LEAD must apply to
    the agenda.
  sources: The retrieved reprints and their recorded routes in review §9.5, the
    review's §7 and the agenda's citation sites.
  excluded: MUST NOT sweep records outside the load-bearing set — the boundary
    is the deliverable; MUST NOT re-screen the corpus; MUST NOT edit the agenda,
    which the lead owns.

- agent: general-purpose
  objective: Determine, from the three audit trails' recorded refute-gate
    dispositions, whether the 7.3% kill rate indicates accurate auditors or
    insufficiently adversarial refuters, and propose a concrete refuter-brief
    change with the eval that would test it.
  output: `memo_refute-gate-calibration_2026-09-03.md`; returned summary giving
    the evidence_type distribution, the verdict on the two hypotheses, and the
    proposed diff.
  sources: `docs/audits/audit_trail_phase2-explosive-review_2026-08-24.md` and
    its round sidecars, `audit_trail_kalshi-arbitrage-review_2026-09-02.md` and
    sidecars, `audit_trail_open-items-kalshi-arbitrage_2026-09-02.md`,
    `~/.claude/skills/audit-remediate-loop/SKILL.md` §"Refute-gate triage rule".
  excluded: MUST NOT edit anything under `~/.claude` — the memo proposes, the
    author applies; MUST NOT assert a kill-rate benchmark the cited literature
    does not support (the ~79-83% figure is directional, from a different
    domain); MUST NOT re-adjudicate any finding's substance.

- agent: general-purpose
  objective: Write a test that re-derives the ER-RoB appraisal table's
    domain-concern column from the extraction JSONLs under the frozen protocol's
    Q-to-D rule and asserts it against the table shipped in the review, giving
    that appraisal claim a runnable reproduce target.
  output: `tests/test_erob_recount.py`, plus a returned summary giving the
    assertion the test makes, the recorded-divergence set it treats as expected,
    and the mutation it was checked against.
  sources: `docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl`
    and `se-extraction-recheck.jsonl`, the appraisal table in section 6 of
    `docs/literature/lit_review_explosive-regime-dating_2026-08-24.md`, the
    frozen Q-to-D rule in section 6 of
    `docs/methodology/protocol_explosive-regime-review_2026-08-24.md`, and
    amendment A8 for the recorded divergences.
  excluded: MUST NOT hardcode the expected table — a test that restates the
    shipped values rather than re-deriving them from the JSONLs is the failure
    mode this deliverable exists to avoid; MUST NOT edit the review, the
    protocol, or any extraction log; MUST NOT widen the expected-divergence set
    to make the test pass.

- agent: audit-remediate-loop (7-branch specialist round, 3-round cap)
  objective: Audit Threads A–D — whether the completion screen genuinely read
    rather than classified, whether the S4 rewrite's claims match the extraction
    depth actually reached, whether the test re-derives rather than restates,
    whether the locator verification's boundary is honestly drawn, and whether
    the calibration memo's numbers reconcile with the trails.
  output: Attested findings with refute-gate dispositions and the audit trail.
  sources: All session artifacts, the frozen protocols, CLAUDE.md,
    rules/quant-project.md, REVIEW.md, primary sources.
  excluded: MUST NOT re-raise minors logged in the 2026-09-02 specs; MUST NOT
    drop a critical/major finding without concrete enumerated counter-evidence.

# Self-executed

- Agenda corrections in `research_agenda_regime-classification_2026-08-21.md`
  arising from Thread C  (reason: transcription of delegated results into an
  existing file, no authored research content — recorded Rule 1 deviation,
  routed through the delegated audit round)
- `uv.lock` tracking and the pinning decision, recorded as ADR-0005  (reason:
  repository configuration bookkeeping and a decision record of the author's own
  scope choice, asserting no research claim; routed through the delegated audit
  round for consistency against ADR-0001/0003/0004 rather than claiming an
  exclusion)

**Rule 1 correction, 2026-09-03.** `tests/test_erob_recount.py` appeared under
Deliverables but in neither Delegation nor Self-executed when this spec was first
written — a Rule 1 violation in the declaration itself. It is now delegated (the
`general-purpose` entry above). Recorded rather than silently repaired: the
declaration is the artifact that makes delegation auditable, so a gap in it is
worth more as a recorded defect than as a quiet fix.
- Protocol amendment SHA recomputation, spec ticks, ReproLog and sidecar
  emission, trail `git add`, commits  (reason: gate-mandated deterministic
  bookkeeping and hashing, no authored research content)

# Standing correction from the 2026-09-02 session

Remediation introduced false claims at a steady rate across all five audit
rounds of that session — three inside round 1's fixes, four inside round 2's,
each caught by the following round, and nothing checked the last pass on either
thread. Two consequences bind this session:

1. Every delegated brief in this spec carries an explicit instruction to write
   uncertainty into the artifact rather than assert past the evidence.
2. No deliverable here is reported complete on a remediating agent's own account
   of its work. Either an audit round verified it, or the tick records that it
   did not.
