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
  - **DELIVERED WITH A DECLARED DEFECT — recorded 2026-09-04 under audit finding
    SCOPE-2-1, and the box is deliberately NOT ticked.** The artifact satisfies
    every clause of the mechanical **check** above: the verdict file parses, it
    carries 197 verdict-bearing rows against an S4 subset size of 197,
    197 + 503 = 700, every row cites a criterion, the residual `undecided` count
    is stated, the amendment (A16, with A18 and A19 correcting it) exists, and
    the frozen prefix was re-verified against the bytes on disk after every
    append. What it does **not** satisfy is the **state** clause, and the
    delivery says so itself: the admission bar actually applied was the
    **negation of X6** — a disjunction, admitted unless the record states
    *neither* a payoff support *nor* an applicability condition — and not the
    §2.2 transfer clause's **conjunction**, which is the criterion this item
    names. The include verdicts are therefore not the assessment this item
    describes. **The set the transfer clause admits lies in [0, 178]**, no lower
    bound above zero is recorded for it, and the include count is conditioned at
    **[149, 327]** (protocol amendment **A18** §§(c)–(d); corpus record §8.4.4).
    The defect is declared at every governing site — §8.4.4, A18 §§(c)–(d), the
    corpus record's front matter, its "Read this first" block, its §5 identity
    table, §8.4, §8.8, §13.2 and the gap register — rather than papered over,
    and **no claim line in §8 rests on any of the 178**, so the corpus record's
    claims are unaffected and the 178 can only weaken §8.4's universal
    negatives, which is the conservative direction. **Carried forward as an open
    item to the next session's spec:** re-screen the 178 against the transfer
    clause's **positive conjunct**, recording per record a mandatory
    `admitting_statement` that quotes the record's own sentence with its source
    named, and re-adjudicating to `undecided` wherever none can be quoted. **No
    re-screen was performed in this session and no count, verdict or record was
    changed by its declaration.**

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

# Recorded deviation — Thread A item 2 scope

**2026-09-03.** Thread A item 2 as declared requires full-text extraction for
the named lineage anchors "plus every S4 record newly included by the completion
screen". That was written expecting the completion screen to admit a modest
number. It admitted **178** (197 assessed: 178 include, 12 exclude X5, 7
undecided), taking the corpus from 149 to **327**. Full-text reading of 178
records is not achievable in this session, and pretending otherwise would
reproduce the exact defect this thread exists to correct — an extraction stage
claiming a depth it did not reach.

**The deviation:** full-text depth is required for (a) the named inventory-risk
and market-scoring-rule lineage anchors, and (b) every record §8.4 actually
cites after the rewrite. Newly included records that §8.4 does not cite are
carried at the depth already reached, **labelled as such per record**, and
counted. The rewrite's rule is unchanged and is what matters: no §8.4 claim may
assert an applicability condition at abstract depth without saying so.

This narrows the deliverable. It is recorded here rather than absorbed silently,
and the residual — the count of included-but-not-full-text-read S4 records — is
reported in the session's residual risk.

# Findings recorded during execution, not repaired here

Two defects surfaced mid-session that are outside this spec's deliverables. Both
are recorded rather than fixed, with the reason.

**F-1 — amendment A8's wording misdescribes what its own count is against.**
A8 says the 31 lenient divergences are counted against "the primary extractor's
own judgments". They are counted against the review's §2.8-**resolved** domain
column, i.e. after the `†` raises. Recount against the raw `domain_concerns`
field in `se-extraction-primary.jsonl` gives **42** (D1 4, D2 1, D3 21, D4 9,
D5 6, D6 1); the strict count is 13 either way. Established mechanically by
`tests/test_erob_recount.py`, which reproduces A8's published 31/13 exactly
against the resolved column. The review's §6 legend is precise about this; A8's
prose is not. **Not repaired:** correcting a published amendment in an
append-only addendum is a substantive act on a frozen protocol, and the lead
session should not do it on its own reading. Routed to the audit round.
**REPAIRED 2026-09-03 by the audit round (findings QUANT-1-6 and REV-1-6, both
major, neither refuted).** The stated reason above conflated *editing* an
amendment with *appending a correcting one*; the second was available — A12(a)
already corrects A7's denominator by append — and has now been used. Protocol
amendment **A15** records the correction in the governing document, and the
review's §6 legend mirrors it. Nothing above this note is edited, and no spec box
is ticked by it. Frozen prefix re-verified after the append: the first 51,478
bytes still hash to `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`;
the protocol-with-addendum digest moves to
`eed7db745ff7fe241f85246c37f8f244890fb23712bf7c712093f3a40f9df9e0` (91,329
bytes), superseding `9d400eb5…`.

**F-2 — absolute home-directory paths carrying the OS username are in tracked,
public files.** Raised as D9 by the refute-gate memo. Present in 16 files:
6 audit-trail `.md`, 9 audit-trail `.json` sidecars, 4
`union_gate_waivers_*.md`, and `er-screening-prompt.txt`. This contravenes
`CLAUDE.md` §Identity hygiene's closing convention ("repo-relative paths remain
the convention in tracked prose — absolute paths under a home directory are
brittle across machines regardless of identity policy") in a repository that is
public by explicit choice.

**Not repaired, and the reason is a genuine conflict, not reluctance.** The
`.json` sidecars are digest-pinned by `sidecar: {path, sha256}` in their own
`.md` trails and now also by the calibration memo; rewriting them silently
breaks the pin chain, which is a worse defect than the leak. The trails are
also append-only immutable records under 21 CFR 11.10(e). And the
`union_gate_waivers_*.md` files are written by
`~/.claude/hooks/stop_union_gate.py`, so the durable fix is in the hook, which
this spec places out of scope.

The author's decision is needed on which of three to take: (a) leave history and
fix the hook so no new file carries an absolute path; (b) normalise history and
re-pin every affected digest in the same commit, recording the normalisation as
a dated addendum in each trail; (c) accept it, on the ground that the repository
already carries the author's real name by choice and the OS username adds
little. This session took none of them; new files it wrote use repo-relative
paths.

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
