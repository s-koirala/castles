---
type: methods_memo
slug: refute-gate-calibration
date: 2026-09-03
status: open
spec: docs/deliverables/deliverable_spec_s4-reexecution-and-repo-gaps_2026-09-03.md
thread: D
subject: the audit-remediate-loop refute gate, not the deliverables it gated
repo_head_at_analysis: 2ba291f9922547e1848d7d505cedafb2979e2433
---

# Memo — refute-gate calibration, 2026-09-02 session

## 1. Question

The 2026-09-02 session ran five audit rounds. **151 critical/major findings
passed the adversarial refute gate; 11 were dropped. A 7.3% kill rate.** The
[audit-remediate-loop](https://github.com/s-koirala/dotfiles/tree/main/claude/skills/audit-remediate-loop)
skill records, as directional support for the gate's existence, that adversarial
verification killed ~79–83% of candidate findings as false positives in
LLM-assisted defect discovery ([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)).

Two hypotheses were left open in the session trail
[docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md](../audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md)
§2:

- **H1** — the auditors were unusually accurate, because documentary and prose
  artifacts admit checkable claims (a page number is right or wrong) in a way
  that C/C++ defect candidates do not.
- **H2** — the refuters were insufficiently adversarial: going through the
  motions and returning "not refuted" without genuinely attempting the
  counter-test the gate's rule demands.

**This memo does not treat ~79–83% as a benchmark this session failed.** §3.4
sets out why the comparison does not license that inference. The memo analyses
the gate. It does not re-adjudicate any finding's substance, and no statement
below should be read as agreeing or disagreeing with any auditor's claim.

## 2. Data

### 2.1 Sources

All five rounds' recorded refute-gate dispositions, read at repository HEAD
`2ba291f9922547e1848d7d505cedafb2979e2433`. Digests pin the exact bytes read
(these files are tracked, so the digests resolve in a fresh clone). SHA-256
truncated to its leading 16 hex characters for width:

| file | sha256 (leading 16) |
|---|---|
| [docs/audits/audit_trail_phase2-explosive-review_2026-08-24.md](../audits/audit_trail_phase2-explosive-review_2026-08-24.md) | `b61f8596d3ffc9de` |
| `…phase2-explosive-review_2026-08-24.json` (Thread A round 1) | `221d4f241b04bba9` |
| `…phase2-explosive-review_2026-08-24.round2.json` | `b62e57f063baf5f4` |
| `…phase2-explosive-review_2026-08-24.round3.json` | `92e803db1464b1db` |
| [docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md](../audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md) | `34e6aca60f3867b9` |
| `…kalshi-arbitrage-review_2026-09-02.json` (Thread C round 1) | `fcad5133001899a7` |
| `…kalshi-arbitrage-review_2026-09-02.round2.json` | `2eb62d0a716b19ac` |
| [docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md](../audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md) | `3efb13b79b2c60fc` |
| `…open-items-kalshi-arbitrage_2026-09-02.json` (session level) | `4a8520439ca9de0e` |

All nine live in [docs/audits/](../audits/).

Gate rule and schema: `~/.claude/skills/audit-remediate-loop/SKILL.md`
(sha256 `491dc002bf8d7ca7bb5474a75f1a4b5a9c63813236743e9b6040e229f8a7ec1e`),
§"Refute-gate triage rule" and §"Refute-gate dispositions". Eval suite:
`~/.claude/skills/audit-remediate-loop/evals/` — `evals.json`
(`2ea384902b57721c…`), `README.md` (`c3331eb6542d78c8…`), 8 fixtures.

The eight `~/.claude` paths are outside this repository and outside its history;
they are named as untracked locators and pinned by digest, per the CLAUDE.md
reproducibility contract.

### 2.2 The stated counts reconcile

Every per-round figure supplied in the Thread D brief was re-derived from the
sidecars rather than accepted. All five reconcile, and so do the session totals.

| round | thread | raw critical | raw major | gated | dropped | retained | minors logged |
|---|---|---|---|---|---|---|---|
| 1 | A | 0 | 27 | 27 | 3 | 24 | 21 |
| 2 | A | 0 | 30 | 30 | **0** | 30 | 15 |
| 3 | A | 0 | 17 | 17 | 1 | 16 | 16 |
| 1 | C | 3 | 38 | 41 | 4 | 37 | 24 |
| 2 | C | 2 | 34 | 36 | 3 | 33 | 19 |
| **total** | | **5** | **146** | **151** | **11** | **140** | **95** |

11/151 = 7.28%. The `refute_gate_dispositions` array length equals the gated
count in every round (27, 30, 17, 41, 36), and equals `len(remediate) +
len(refuted)` in every round. `retained_conservative` is 0 in all five rounds,
so there are no refuter-unavailable fallbacks to account for. The
agent-count field also closes: 184 agents = (4+5+5+4+5 branches) + (one refuter
per gated finding, 151) + 2 per round (trail writer and independent attestor).
That reconciliation is the only evidence in the record that one refuter agent
ran per finding; nothing else in the trail asserts it directly.

### 2.3 Discrepancy register

Reported, not adjusted. None of these changes any count in §2.2; all bear on
whether the gate's record can be checked after the fact.

**D1 — `evidence_type: none` is outside the enumeration.** The schema enumerates
`reproduced-check | source-quote | counter-test | logical-proof` and calls the
field "mandatory and enumerated … it *is* the drop rule". 136 of the 151 rows
carry `none`. Every one of those 136 is a retained finding. The enumeration has
no member for "a refutation was attempted and failed", so the sentinel is the
only available value — but the consequence is that the single field that would
distinguish H1 from H2 is, by construction, blank on 97% of the retained
population.

**D2 — `evidence_type` is used with two different meanings.** 136 retained rows
carry `none`; 4 retained rows carry `reproduced-check` — LITERATURE-1-2 (Thread
C, round 1), REV-2-5, REV-2-6 and LITERATURE-2-1 (all Thread C, round 2). Those
four refuters recorded the evidence type of the work they performed; the other
136 recorded the evidence type that carried a drop, and since there was no drop
they recorded `none`. Both readings are defensible against the schema text. The
field is therefore not comparable across rows.

**D3 — `refuted_by` never carries `model_id`.** The schema specifies
`{role: refuter, model_id: "<model@version>", effort: high}`. All 151 sidecar
rows carry `{"role": "refuter", "effort": "high"}` and no `model_id`. The trail
front matter does declare the refuter branch model (`claude-opus-5`, effort
high) in `agents[]`, so the fact is recoverable at round level but not at row
level.

**D4 — `decided_at` is absent from all 151 sidecar rows.** The schema lists it
in the per-entry block.

**D5 — the `reproduction` block is present on 3 of the 9 rows that require
one.** Nine rows carry `reproduction_required: true` (the 4 `reproduced-check`
drops, the 1 `counter-test` drop, and the 4 `reproduced-check` retentions). A
`reproduction: {command, observed}` block exists for LITERATURE-1-3 (Thread A,
round 1, dropped), SCOPE-1-3 (Thread C, round 1, dropped) and LITERATURE-1-2
(Thread C, round 1, retained) — in the Markdown trails only; the JSON sidecars
carry the boolean flag but never the block. The six round-2 rows that require
one — REV-2-7, SCOPE-2-1, LITERATURE-2-2 (dropped) and REV-2-5, REV-2-6,
LITERATURE-2-1 (retained), all Thread C round 2 — carry none in either
representation. On the schema's own stated rationale ("without the command, a
'counter-test' is indistinguishable from the bare doubt the gate exists to
reject"), **3 of the 11 drops are under-evidenced as recorded**, even though all
three carry long, artifact-anchored prose.

**D6 — 13 of 17 distinct pinned `(path, digest)` pairs are not recoverable from
git.** Each round's front matter pins its artifacts as `{path, git_head,
sha256}`. Reconstructing every content state of each path across
`git rev-list --all` and hashing it shows that only 4 of the 17 pinned digests
exist anywhere in history. Concretely: round 2 Thread C pins
`docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md` at
`acfc6a57a4ecdaa5…`; that path has exactly one content state in the entire
repository history, `4ee8ef348fbd5c19…`, the post-remediation version. The
pinned bytes were an uncommitted working-tree state and no longer exist. The
same holds for the Thread A artifacts at rounds 1 and 2. **No refutation from
rounds A1, A2, C1 or C2 can be re-run against the artifact version it examined.**

**D7 — a spot-check of a refuter's arithmetic could not be scored, for the D6
reason.** The refutation that dropped LITERATURE-2-2 (Thread C, round 2) records
a verbatim counter-count command and its result: 86 fenced blocks in review lines
292–602, 45 after removing the forward-citation and known-item arms. Re-running
that exact command against the committed file returns 85 and 44. That is not
evidence for or against the refuter: the file it ran on is the `acfc6a57…`
state, which is unrecoverable. Reported so the attempt is on record and is not
mistaken for a scoring.

By contrast, a claim in the refutation of LITERATURE-2-1 (Thread A, round 2)
that touches a file the remediation did not modify does score: the refuter
states `screen-verdicts-R1.jsonl` "has exactly 1996 lines … and line 209 is
eru-0209". Both are exactly true of the committed file. One verified claim is
not a validation of 151 refutations; it is recorded because it is the only
refuter arithmetic in the corpus that this memo could independently score.

**D8 — finding ids are not session-unique, and 8 of the 11 drops share an id
with a retained finding.** The schema says "ids are load-bearing: refutations
key on it". Ids are unique within a round but are re-issued per thread: 53 of
the 98 distinct ids appear twice, covering 106 of the 151 dispositions. **Eight
of the eleven drops have a same-id twin in the sibling thread that was
retained**: REV-1-1 and SCOPE-1-3 (dropped in C1, retained in A1); REV-2-7,
SCOPE-2-1 and LITERATURE-2-2 (dropped in C2, retained in A2); LITERATURE-1-1,
LITERATURE-1-3 and LITERATURE-1-5 (dropped in A1, retained in C1). Only
C/1/QUANT-1-9, C/1/LITERATURE-1-13 and A/3/QUANT-3-2 carry ids used once in the
session. A bare id does not identify a disposition. Every finding reference in
this memo is therefore qualified as `thread/round/id`.

**D9 — absolute home-directory paths appear inside recorded refutation
evidence** in the tracked trails. Not a numerical discrepancy; noted because
CLAUDE.md makes repo-relative paths the convention in tracked prose and this
repository is public. This memo quotes only passages that do not contain them.

## 3. Analysis

### 3.1 `evidence_type` across the 11 drops

| evidence type | drops | retentions | reproduction block required | block present |
|---|---|---|---|---|
| `source-quote` | 6 | 0 | no | n/a |
| `reproduced-check` | 4 | 4 | yes | 3 of 8 |
| `counter-test` | 1 | 0 | yes | 0 of 1 |
| `logical-proof` | 0 | 0 | no | n/a |
| `none` (outside enum, D1) | 0 | 136 | no | n/a |
| **total** | **11** | **140** | **9 rows** | **3 rows** |

The eleven drops, each with the raiser and the type that carried it:

| disposition | raiser | severity | evidence type | reproduction block |
|---|---|---|---|---|
| A/1/LITERATURE-1-1 | literature-check | major | `source-quote` | not required |
| A/1/LITERATURE-1-3 | literature-check | major | `reproduced-check` | **present** |
| A/1/LITERATURE-1-5 | literature-check | major | `source-quote` | not required |
| A/3/QUANT-3-2 | quant-auditor | major | `source-quote` | not required |
| C/1/REV-1-1 | critical-reviewer | **critical** | `source-quote` | not required |
| C/1/SCOPE-1-3 | scope-auditor | major | `reproduced-check` | **present** |
| C/1/QUANT-1-9 | quant-auditor | major | `source-quote` | not required |
| C/1/LITERATURE-1-13 | literature-check | major | `source-quote` | not required |
| C/2/REV-2-7 | critical-reviewer | major | `counter-test` | **absent** |
| C/2/SCOPE-2-1 | scope-auditor | major | `reproduced-check` | **absent** |
| C/2/LITERATURE-2-2 | literature-check | major | `reproduced-check` | **absent** |

Three readings follow.

**Only two types ever killed anything, and they are the two that require an
external retrieval or a mechanical re-derivation.** Six drops turned on going to
a source the auditor had characterised and finding that it said something else
(`source-quote`); four on re-deriving a count or a join the auditor had computed
(`reproduced-check`); one on constructing a test the auditor had not run
(`counter-test`). `logical-proof` — the one type that requires no contact with
an artifact or a source — killed nothing. That is the shape a functioning
evidence rule should have.

**Reproduction evidence is present on 3 of the 9 rows that require it (D5).**
The three that carry it are all round-1 rows; all six round-2 rows omit it. This
is a recording regression between rounds, not a difference in the work: the
round-2 refutation prose contains the commands (C/2/REV-2-6's refutation, for
instance, records a full pipeline rebuild with control and treatment runs and
their divergent counts), but they are embedded in narrative rather than lifted
into the structured field the schema defines for them. The distinction matters
exactly as the schema says it does: prose can be read, a `{command, observed}`
pair can be re-run.

**Every drop is anchored to something outside the finding.** All eleven
refutation-evidence strings name a retrieved document, a URL, a digest, a
line-numbered read, or a command. The shortest is 1,881 characters; the longest
3,957. None of the eleven is a plausibility argument or a severity quibble. On
the substance of the drops this memo takes no position; on their *form*, none is
a bare-doubt drop.

### 3.2 Retained findings: genuine failed counter-tests, or no attempt?

This is the discriminating evidence the brief identifies, and it is where the
answer is clearest.

**Structural facts over all 140 retained dispositions.** No refutation-evidence
field is empty. Lengths: minimum 1,244 characters, median 2,259, maximum 4,446.
Under a four-marker lexical screen (CONVENTION-2, §8), 138 of 140 quote artifact
text verbatim, 121 assert in terms that the refutation failed, 99 name an
executed operation (a shell command, a script re-run, a fetch, a digest), 77
name a candidate defence of the artifact that the refuter constructed and
rejected. 110 of 140 carry three or more of the four markers.

**Every case the screen flagged as a possible non-attempt was read in full and
is the opposite.** Four rows carry one marker or fewer: A/2/LITERATURE-2-1,
C/1/QUANT-1-3, C/1/QUANT-1-6, C/1/LITERATURE-1-14. All four are among the most
thorough refutations in the corpus, and the screen missed them only because each
opens with idiosyncratic phrasing. A/2/LITERATURE-2-1 opens "Refutation attempted
on four independent angles; all failed" and works through universe membership,
same-work identity resolved against three bibliographic APIs, screening history
across four verdict files, and a wording-escape test. C/1/LITERATURE-1-14 opens
"Attempted refutation on three fronts" and names each. C/1/QUANT-1-3 records
"every counter-avenue tested failed" and enumerates three closed avenues (a), (b),
(c). C/1/QUANT-1-6 ran the archived pipeline five times — three unseeded, two
under `PYTHONHASHSEED=0` — and reports three distinct output digests for the
unseeded runs against one for the seeded pair. The screen has a demonstrated
false-negative rate of 4 in 4 on the cases it flagged; it should be read as a
lower bound on attempt quality, not a measurement of it.

**Seventeen retained dispositions were read in full** — nine from the zero-kill
round (A/2/REV-2-1 through A/2/REV-2-7, A/2/REV-2-12, A/2/SCOPE-2-1), the four
screen-flagged rows above, and the four retentions carrying a non-sentinel
`evidence_type` (C/1/LITERATURE-1-2, C/2/REV-2-5, C/2/REV-2-6,
C/2/LITERATURE-2-1). The selection is purposive, not random: it targets the
round the brief calls the sharpest datapoint, the cases most likely to be
non-attempts, and the cases whose recording is anomalous. **None records bare
doubt. None records an absent attempt.**
Each names the artifact locations it read, the operations it ran, and where
available the counter-reading it constructed and why that counter-reading
failed. Representative, quoted verbatim:

- A/2/REV-2-12 — "The only available defense — reading 'answered' loosely to
  include n/a — is foreclosed by the review's own legend at line 987".
- A/2/REV-2-6 — "The only counter-line I could construct … attacks only the
  strength of the er-bc-1 example, does not settle it … That is a plausibility
  argument, not counter-evidence." The refuter explicitly declines to drop on
  the strength of an argument it recognises as insufficient under the gate's own
  rule.
- A/2/SCOPE-2-1 — "The only angle that yielded any tension is that A11's phrase
  … names a successor review pass rather than the agenda by name; but that bears
  on where the fix should land, not on whether the defect exists."
- A/2/REV-2-3 — a five-part re-derivation ending "Only defect in the finding is
  a wording imprecision that does not affect the claim".

**The refuters also corrected the auditors' own claims, against the auditors'
interest, while retaining the findings — in at least seven dispositions.**
The set below is the one §4 item 1 cites; the two lists were not identical
before, and the enumeration here is now the single reference set for the claim
in both places *(finding FORMAT-1-2, 2026-09-03)*. Each is quoted from the
`refutation_evidence` field of the round's own sidecar:

| disposition | the correction the refuter made to the finding |
|---|---|
| A/1/QUANT-1-2 | *"Only defect I could find in the finding is a count-boundary quibble, not a refutation: under the protocol's literal wording ('no' or 'unclear' only) the count is 22, not 31, and D4 would be 17 low / 47 high"* — then explains why the auditor's wider reading is the one the document's own §2.8 ordering supports, so the correction is raised against the finding and then withdrawn on the document's own convention |
| A/2/REV-2-3 | "Only defect in the finding is a wording imprecision that does not affect the claim" — two of the four §4 dimensions the finding named do *not* inherit their codes from the carriers |
| A/2/REV-2-12 | "That is five occurrences, one more than the finding's stated 'four times' — an understatement in the finding, not a defect in it" |
| A/2/QUANT-2-6 | "My count differs from the auditor's 22 only by scope of the table window and by including the non-DOI record eru-1770" — 23 divergent year fields against the finding's 22 |
| C/1/REV-1-4 | "Only defect located in the finding is a section locator slip" — the Berkowitz et al. 2017 line is at §8.1.2, not the §8.3.2 the finding cited |
| C/1/QUANT-1-6 | "Two secondary inaccuracies in the finding do not touch the claim" — and both are identified by line; separately, "My count differs from the auditor's 4,415 only because each unseeded run draws a fresh hash seed" |
| C/2/REV-2-8 | "The only defect I found in the finding is its flip clause" — E6's category list does not make a quote-driven venue license the transfer automatically |

**Seven is a lower bound, not a census.** It is what a lexical scan of all 151
`refutation_evidence` strings for correction language (CONVENTION-6, §8) turned
up *and* a full read confirmed. The scan flagged further candidates that were
not read to a verdict here, so the true count is ≥ 7.

**The reading base for this table is wider than the seventeen above.** Three of
the seven (A/2/REV-2-3, A/2/REV-2-12, C/1/QUANT-1-6) are inside the seventeen
dispositions the memo's original purposive selection read. The other four
(A/1/QUANT-1-2, A/2/QUANT-2-6, C/1/REV-1-4, C/2/REV-2-8) and the withdrawal
evidence for C/2/QUANT-2-9 were read on **2026-09-03**, during remediation of
FORMAT-1-2, and are not part of the seventeen. The seventeen-row claim above is
unchanged and still describes the original selection; nothing in §3.3, §3.4 or
§4's other items depends on the wider reading.

**Two claims this paragraph previously made are withdrawn as misattributions,
both found by the 2026-09-03 audit round and both verified against the
sidecars.** (i) The phrase "overstated by one" was attributed to C/2/REV-2-6.
It belongs to **C/2/QUANT-2-9**, whose refutation records that the artifact's
claim that bare patterns "would have wrongly moved three genuine DeFi records
out of X5" is "overstated by one" — and that sub-claim *was* raised by the
finding (its fix reads "name only the two records the bare patterns would have
moved and drop the third"), so it is a confirmation of the auditor, not a
correction against the auditor. C/2/REV-2-6's own refutation corrects nothing in
its finding: it re-derives the K ∩ SSRN intersection as 15 and enumerates the
15 record ids, which is confirmation. (ii) C/2/REV-2-5 likewise corrects
nothing: it reproduces the finding's three arithmetic errors from a stated
`sed`/`awk` count and separately confirms the subsidiary Oliven & Rietz claim
that the finding had asserted without a count. **Supplying evidence an auditor
did not supply is not the same act as correcting an auditor**, and running the
two together is what produced two non-identical reference sets for one claim.

Both behaviours — correcting the auditor and evidencing beyond the auditor — are
calibrated and non-deferential. Neither is what sycophantic agreement looks like
— the failure mode [arXiv 2509.05396](https://arxiv.org/abs/2509.05396)
documents and the round cap exists to bound.

**Conclusion for §3.2.** On the evidence available, H2 in its strong form — the
refuters went through the motions and returned "not refuted" without attempting
the counter-test — is not supported anywhere in the record examined. Every one
of the 17 retained dispositions read in full, including all 4 that the screen
singled out, records concrete artifact-anchored work; 77 of 140 name a
constructed and rejected defence. §4 states what this does and does not settle.

### 3.3 The round-2 Thread A zero

Three separate questions are tangled here: whether the zero is anomalous,
whether it has a structural cause, and whether it is diagnostic of the gate.

**It is not anomalous.** Under the session's own pooled rate (11/151 = 0.0728),
P(0 kills in 30) = 0.103. Against the pooled rate of the other four rounds
(11/121 = 0.0909), which is the cleaner comparison because it excludes the round
being tested, P(0 in 30) = 0.057. A Monte Carlo permutation test of homogeneity
across the five rounds (CONVENTION-4, §8: B = 20,000, seed 20260903) gives observed
χ² = 3.421, p = 0.506; the asymptotic χ²(4) agrees at p = 0.490 but its expected
cell counts are small enough that the permutation value is the one to use.
**There is no evidence the five rounds' kill rates differ from each other.**
Exact one-sided 95% upper bound on the round's true rate given 0 of 30:
9.50%. Clopper-Pearson two-sided 95% intervals per round overlap heavily
(A1 2.35–29.2%, A2 0–11.6%, A3 0.15–28.7%, C1 2.72–23.1%, C2 1.75–22.5%).

The sharpest datapoint in the session trail is therefore sharp in one direction
only: 0 of 30 is decisively incompatible with a true kill rate near 0.79–0.83
(P = 4.6 × 10⁻²¹ at 0.79), and entirely compatible with the rate the other four
rounds ran at. It discriminates between populations, not between H1 and H2.

**A structural explanation exists but does not isolate this round.** The round-2
Thread A brief is a verification brief: its `taskSpec` reads "ROUND 2 — VERIFY
THE ROUND-1 REMEDIATIONS AND HUNT WHAT THEY INTRODUCED" and enumerates twelve
specific claims to check, most of them mechanically checkable (does amendment
A4–A11 exist and is it dated and stage-named; is the I3 count seven everywhere;
is the D-rule column correctly derived for all 72 rows; are the assessable
denominators 65 and 53 applied at every site). Findings raised against that
brief are largely internal-consistency defects — the artifact contradicting
itself, or an arithmetic identity failing — and the round's category tally bears
that out: consistency 3, reporting 4, interpretation 3, partial 3, numerical 2,
plus five reproducibility-branch categories, against a handful of
external-source categories. **But Thread C round 2 carried an identical
instruction** (verbatim "ROUND 2 — VERIFY THE ROUND-1 REMEDIATIONS AND HUNT WHAT
THEY INTRODUCED", with ten enumerated claims) **and killed 3 of 36.** Being a
verification round does not by itself produce a zero.

**What does covary with the kill rate is whether the finding turns on a fact
outside the artifact.** Classifying each of the 151 findings by whether its own
`evidence` / `reference` / `location` / `category` / `issue` text names an
external source (CONVENTION-3, §8):

| finding class | dropped | gated | kill rate |
|---|---|---|---|
| names an external source | 9 | 66 | 13.6% |
| artifact-internal only | 2 | 85 | 2.4% |

Fisher exact two-sided p = 0.011. **This is exploratory and must not be read as
a test.** The partition was chosen after reading the eleven drops, so the p-value
has no error-rate interpretation; and the partition is confounded with branch —
`literature-check` findings are 71% externally anchored and account for 5 of the
11 drops, while `reproducibility-verifier` is 36% external and killed 0 of 14.
Restricting to the four non-`literature-check` branches leaves the direction
intact but the evidence weak: 4/39 = 10.3% external against 2/74 = 2.7%
internal, Fisher p = 0.18. Per-branch kill rates for completeness:
`literature-check` 5/38, `scope-auditor` 2/20, `quant-auditor` 2/36,
`critical-reviewer` 2/43, `reproducibility-verifier` 0/14.

**Reading.** The mechanism H1 proposes is visible in the data — a refuter can
beat a finding only when there is a fact outside the artifact the auditor might
have got wrong, and it cannot beat "line 113 states three counts that sum to 63
and calls the total 72" (A/2/REV-2-2) because the artifact is its own ground
truth there. Round 2 Thread A was disproportionately made of that second class.
But the association is directional, confounded, and post hoc, and the round
itself is statistically unremarkable. **The zero is not a signal. It is what a
7% process does one round in ten.**

### 3.4 Is ~79–83% the right comparator?

No, and four independent reasons say so. Any one of them would be enough.

**(a) The skill does not offer it as one.** The text reads "C/C++ security
libraries, compilers, and standards targets — directional, not a calibration
target". The source's own scope is source-code defect discovery. This session
gated findings against multi-thousand-line PRISMA-style prose reviews, a
bibliography store, a frozen protocol and an ADR.

**(b) The denominators are different objects, and the difference is large
enough to swamp the comparison.** The cited rate is over *raw candidate
findings*. This gate never sees raw candidates: §"Loop structure" step 3 triages
first, and `minor` findings are dropped before step 4's refuter is spawned. 95
minors were triaged out across the five rounds and never reached the gate. The
gate's 7.3% is therefore a rate conditional on having survived triage. Computed
instead over the raw finding population the way the cited study computes its
own — all 246 findings raised, of which 106 were not remediated (11 gate drops
plus 95 triaged minors) — the same session's same work yields **43.1%**. That
figure is offered as a demonstration, not as an equivalent statistic: it is
*also* not commensurable, because triage and refutation are different filters
with different rules. The point is that the denominator choice alone moves the
number by a factor of about six, and neither document states the denominator
precisely enough for the two to be aligned.

**(c) The producers differ.** The cited candidates come from LLM defect
discovery over source code. These come from seven role-specialised auditors,
each briefed with the task spec, the artifact digests, `CLAUDE.md` and the
applicable rules files, running after a triage step, against artifacts whose
claims are in large part checkable within the artifact itself. §3.3's
internal/external split is direct evidence that this population's checkability
profile differs from a code-defect population's.

**(d) The inference would have to run backwards.** To read 7.3% as gate failure
requires assuming the two populations share a true false-positive rate — the
very thing the comparison is being used to establish. The zero-kill round shows
how far apart they are: P(0 of 30 | p = 0.79) = 4.6 × 10⁻²¹. The honest
conclusion from that number is that the populations are not the same, not that
the gate underperformed.

Recording "7.3% — an order of magnitude lower" beside the cited figure, as the
session trail does, is a true statement about two numbers. Treating the gap as a
defect signal, or tuning the refuter until the gap closes, would be an
unattributed threshold imported from another domain — the error `CLAUDE.md`
§"Parameter & Prompt Selection" forbids, and the failure mode
[arXiv 2606.19544](https://arxiv.org/abs/2606.19544) describes when a judge's
consistency is mistaken for its validity.

## 4. Verdict

**The evidence supports H1 over H2 in its strong form, disconfirms neither
completely, and cannot separate them at the level that matters, for a reason
that is itself the memo's most actionable finding.**

Stated precisely:

1. **H2-strong ("no genuine attempt") is not supported.** Zero of the 17 retained
   dispositions read in full — including all 4 the lexical screen flagged as
   possible non-attempts — record bare doubt or an absent attempt. 77 of 140
   name a defence of the artifact the refuter constructed and rejected; 99 name
   an executed operation. **At least seven** refutations correct the auditor's
   own claim against the auditor's interest while retaining the finding
   (A/1/QUANT-1-2, A/2/REV-2-3, A/2/REV-2-12, A/2/QUANT-2-6, C/1/REV-1-4,
   C/1/QUANT-1-6, C/2/REV-2-8) — the set §3.2 enumerates and quotes, and a
   lower bound rather than a census (CONVENTION-6, §8). Corrected 2026-09-03
   under finding FORMAT-1-2: this item previously said "four" and named a set
   that §3.2 did not evidence.

2. **H2-weak ("attempted, but stopped short") is untested and untestable from
   this record.** Nothing in the schema measures refuter effort against a
   standard. There is no field that says how many counter-hypotheses were
   constructed, or whether the refuter looked beyond the finding's own cited
   lines. §3.2's 77-of-140 count is recovered from prose that happened to
   volunteer it, not from a field that required it. A refuter that read the
   cited lines, confirmed them, and stopped would produce a record
   indistinguishable in structure from one that exhausted the alternatives.

3. **H1 is consistent with the mechanism visible in the data but is not
   established.** The internal/external gradient (§3.3) is the mechanism H1
   predicts, and it is present at 13.6% against 2.4%. But it is post hoc,
   confounded with branch, and weak within branches. More fundamentally: a
   *false* internal-consistency finding and a *true* one that the refuter
   correctly failed to kill leave identical traces in this record.

4. **The binding obstacle is the absence of ground truth, not the absence of
   analysis.** No amount of further reading of these trails can establish what
   fraction of the 140 retained findings were false, and without that, no kill
   rate can be scored as too low or too high. This is why §7 proposes an
   instrument rather than a further pass over the data.

5. **A third reading is established by the counts and is not exclusive of either
   hypothesis. Call it H3: the population reaching the gate is not the raw
   population.** Triage removed 95 minors before any refuter was spawned. The
   7.3% is a conditional rate over a pre-filtered, higher-prior set, and any
   comparison against a raw-candidate rate is a category error before any
   question of auditor accuracy or refuter effort arises (§3.4b). H3 is
   demonstrable from the trail alone; H1 and H2 are not.

**One thing the record does establish about the gate, independent of H1/H2:
its own auditability is degraded.** The `reproduction` block is present on 3 of
9 required rows (D5), `evidence_type` is blank-by-sentinel on 97% of retentions
(D1) and inconsistently applied on the rest (D2), `model_id` and `decided_at`
are absent from all 151 rows (D3, D4), 8 of 11 drops share an id with a retained
finding in the sibling thread (D8), and 13 of 17 pinned artifact digests name
bytes that exist nowhere in the repository (D6). The gate's record is the only
surviving trace of a dropped finding — the skill says so — and on the schema's
own terms it is currently a self-report that cannot be re-run.

## 5. Threats to this analysis

**T1 — the trail is the refuter's self-report.** Central and unresolved. Every
statement in §3.2 about what a refuter did is a statement about what a refuter
*wrote that it did*. Independent verification requires re-running the recorded
operations, which D6 makes impossible for four of five rounds. The one
independently scored claim (D7, second paragraph) verified; that is one claim
of 151.

**T2 — version drift.** The digests the refutations ran against are unrecoverable
for 13 of 17 pinned pairs (D6). The one spot-check attempted against a
remediated file returned 44/85 where the refuter recorded 45/86, and cannot be
attributed to either party (D7).

**T3 — sampling.** 17 of 140 retained dispositions (12%) were read in full. The
remaining 123 are characterised by a lexical screen with a demonstrated 4-of-4
false-negative rate on the cases it flagged and an unmeasured false-positive
rate. Reading all 140 would settle the classification. It would not settle
ground truth (verdict item 4).

**T4 — post-hoc partition.** The internal/external split (§3.3) was constructed
after reading the eleven drops and applied to the whole population. Its p-value
has no error-rate interpretation and it is reported for direction only. It is
also confounded with branch, and within non-`literature-check` branches falls to
p = 0.18.

**T5 — independence.** The binomial and permutation calculations in §3.3 treat
the 151 findings as exchangeable within and across rounds. They are not: findings
within a round share an artifact, a lead session and a refuter configuration, and
Thread A's three rounds share an artifact lineage. The figures are descriptive
summaries of the observed dispersion, not inferences about a population.

**T6 — n.** One session, two artifact lineages, one project, one refuter model at
one effort setting (`claude-opus-5`, high). Nothing here generalises to other
artifact classes, and §3.4 is precisely an argument that such generalisation is
what went wrong with the ~79–83% comparison in the first place.

**T7 — my own analysis is not independently audited at the time of writing.**
Per the spec's standing correction, this memo is delegated output and is reported
complete only if the session's audit round verifies it.

## 6. Proposed change to the refuter brief

**The memo proposes; the author applies.** Nothing under `~/.claude` was modified
in producing this memo (SKILL.md digest re-checked after drafting:
`491dc002bf8d7ca7bb5474a75f1a4b5a9c63813236743e9b6040e229f8a7ec1e`, unchanged).
The diff below was generated against a scratchpad copy and verified to apply
cleanly to an unmodified `SKILL.md` with `git apply --check`.

Five changes, each traced to a defect this memo established rather than to a
guess about refuter behaviour:

| change | fixes | rationale |
|---|---|---|
| `attempted-and-failed` added to the `evidence_type` enumeration; `none` forbidden on retentions | D1, D2 | the field that would separate H1 from H2 is currently blank by construction on 97% of retentions |
| `counter_hypotheses` made mandatory and non-empty | verdict 2 | promotes to a requirement what the best 77 of 140 refutations already volunteered; makes "stopped short" visible in the record |
| `reproduction` required on retentions that ran a command, not only on drops | D5 | the schema's own argument ("without the command, a counter-test is indistinguishable from bare doubt") is symmetric; exempting retentions is what makes effort unmeasurable |
| `reproduction.artifact_state` carries a `git hash-object` blob id or `uncommitted` | D6 | a `{path, git_head, sha256}` triple over uncommitted bytes is not a durable pin |
| `disposition_key: {thread}/{round}/{id}`; gate metrics recorded with `gated_population` and `triaged_out_before_gate` named | D8, §3.4b | ids collide across threads; and a post-triage kill rate must never again be tabled next to a raw-candidate rate without its denominator |

````diff
diff --git a/skills/audit-remediate-loop/SKILL.md b/skills/audit-remediate-loop/SKILL.md
--- a/skills/audit-remediate-loop/SKILL.md
+++ b/skills/audit-remediate-loop/SKILL.md
@@ -78,27 +78,37 @@ The trail is the only surviving record of a *dropped* finding, so it is the load
 One entry per gated finding — dropped, retained, and retained-conservative alike:
 
 ```yaml
-- finding_id: LITERATURE-1-1        # the raiser's id; ids are load-bearing
+- finding_id: LITERATURE-1-1        # the raiser's id; unique within a round ONLY
+  disposition_key: A/1/LITERATURE-1-1  # {thread}/{round}/{id} — the session-unique key
   raised_by: literature-check        # PROV wasAttributedTo
   severity_claimed: major
   finding_verbatim:                  # NOT an abridgement — the claim as filed
     location: "...", issue: "...", evidence: "...", reference: "..."
   refuted_by: {role: refuter, model_id: "<model@version>", effort: high}
-  evidence_type: source-quote        # reproduced-check | source-quote | counter-test | logical-proof
+  evidence_type: source-quote        # reproduced-check | source-quote | counter-test |
+                                     # logical-proof | attempted-and-failed
   refutation_evidence: "<verbatim counter-evidence>"
-  reproduction:                      # REQUIRED for reproduced-check and counter-test
+  counter_hypotheses:                # REQUIRED on EVERY entry, minimum one item
+    - claim: "<a defence of the artifact the refuter constructed against the finding>"
+      test: "<how it was tested — command, fetch, or the passage read>"
+      result: failed                 # refuted-the-finding | failed | not-testable
+  reproduction:                      # REQUIRED for reproduced-check and counter-test,
+                                     # and for ANY entry whose refutation ran a command
     command: "<exact command or fetched URL>"
     observed: "<output or quoted passage>"
+    artifact_state: "<git hash-object blob id of the file examined, or `uncommitted`>"
   outcome: dropped                   # dropped | retained | retained-conservative
   decided_at: 2026-07-30T14:02:11-05:00
 ```
 
 - **Verbatim, not abridged.** A summary of a dropped claim cannot be re-adjudicated; abridgement is acceptable only for remediated findings, whose fix is visible in the artifact.
-- **`evidence_type` is mandatory and enumerated** — it *is* the drop rule, so recording only the prose would make the rule unverifiable after the fact.
-- **`reproduction` is mandatory for `reproduced-check` and `counter-test`** (Sandve rule 1). Without the command, a "counter-test" is indistinguishable from the bare doubt the gate exists to reject.
+- **`evidence_type` is mandatory and enumerated** — it *is* the drop rule, so recording only the prose would make the rule unverifiable after the fact. `attempted-and-failed` is the value for a retained finding whose refutation ran a real counter-test that did not succeed; it exists so that "tried and failed" is distinguishable in the record from "did nothing". A retained entry may not carry `none`, an empty value, or any type outside the enumeration.
+- **`reproduction` is mandatory for `reproduced-check` and `counter-test`** (Sandve rule 1). Without the command, a "counter-test" is indistinguishable from the bare doubt the gate exists to reject. **The same requirement binds a retained entry whose refutation ran a command or fetched a URL** — exempting retentions from it makes the gate's own effort unmeasurable after the fact, which is the one thing the trail exists to preserve.
+- **`counter_hypotheses` is mandatory and non-empty.** The refuter states, per finding, at least one defence of the artifact it constructed and how that defence failed. A refuter that can construct none records `not-testable` with the reason. This field is what distinguishes an adversarial pass from a confirmatory re-read.
+- **Pin the artifact state the refutation ran against.** `reproduction.artifact_state` carries a `git hash-object` blob id so the examined bytes stay retrievable, or the literal `uncommitted`. A `{path, git_head, sha256}` triple whose content was never committed is not a durable pin — the digest names bytes that no longer exist anywhere.
 - **Retained-conservative cases are recorded**, including the refuter-unavailable fallback. ISO 19011 requires unresolved diverging opinions in the report; PRISMA 2020 item 8 requires stating how reviewers worked and how conflicts were resolved — this system's reviewers are automation tools, so both clauses bind.
 - **Do not collapse to a verdict.** Per-branch divergence is what makes a single-branch minority finding recoverable ([arXiv 2602.09341](https://arxiv.org/abs/2602.09341) — preprint, directional).
-- **Keep the gate metrics** (raw critical/major, killed count, seeded-defect kills) in the same file; per-run kill rates are the only empirical input to the gate-recall calibration in [evals/](evals/).
+- **Keep the gate metrics** (raw critical/major, killed count, seeded-defect kills) in the same file; per-run kill rates are the only empirical input to the gate-recall calibration in [evals/](evals/). Record them with the denominator named — `gated_population: post-triage critical+major` and `triaged_out_before_gate: <n minors>`. A kill rate over the post-triage population is a conditional rate and is not commensurable with a rate over raw candidate findings.
 
 ### Enforcement
 
@@ -109,7 +119,7 @@ Two layers, because the first is not sufficient:
 
 ## Refute-gate triage rule
 
-Every `critical`/`major` finding passes an adversarial refuter before remediation. The refuter's single job is to disprove the finding: reproduce the claimed evidence, check the cited source, run the counter-test. A finding is dropped only on `refuted: true` with a concrete evidence type (`reproduced-check | source-quote | counter-test | logical-proof`) — bare doubt, plausibility arguments, or severity quibbles never drop a finding, guarding against systematic reviewer overcorrection ([AUSE 2026, doi 10.1007/s10515-026-00638-5](https://doi.org/10.1007/s10515-026-00638-5); judge consistency ≠ validity, [arXiv 2606.19544](https://arxiv.org/abs/2606.19544)). Empirical basis for the gate: adversarial verification killed ~79–83% of candidate findings as false positives in LLM-assisted defect discovery ([arXiv 2604.19049](https://arxiv.org/abs/2604.19049); C/C++ security libraries, compilers, and standards targets — directional, not a calibration target). Refuted findings are logged, never silently discarded. Gate recall is measured by the seeded-defect suite in [evals/](evals/) — a gate that kills seeded true defects fails the eval.
+Every `critical`/`major` finding passes an adversarial refuter before remediation. The refuter's single job is to disprove the finding: reproduce the claimed evidence, check the cited source, run the counter-test. **Construct the strongest defence of the artifact you can before deciding, record it in `counter_hypotheses`, and state how it failed** — a pass that only re-reads the finding's own cited lines and confirms them is a verification, not a refutation attempt, and must not be recorded as one. A finding is dropped only on `refuted: true` with a concrete evidence type (`reproduced-check | source-quote | counter-test | logical-proof`) — bare doubt, plausibility arguments, or severity quibbles never drop a finding, guarding against systematic reviewer overcorrection ([AUSE 2026, doi 10.1007/s10515-026-00638-5](https://doi.org/10.1007/s10515-026-00638-5); judge consistency ≠ validity, [arXiv 2606.19544](https://arxiv.org/abs/2606.19544)). Empirical basis for the gate: adversarial verification killed ~79–83% of candidate findings as false positives in LLM-assisted defect discovery ([arXiv 2604.19049](https://arxiv.org/abs/2604.19049); C/C++ security libraries, compilers, and standards targets — directional, not a calibration target). **That rate is over a raw candidate population on source-code targets; this gate runs on a post-triage `critical`/`major` population over whatever artifact class is routed, so the two are not commensurable and no per-run kill rate is to be read against it as a target.** Refuted findings are logged, never silently discarded. Gate recall is measured by the seeded-defect suite in [evals/](evals/) — a gate that kills seeded true defects fails the eval; gate *precision* is measured by the seeded-false-finding arm of the same suite — a gate that retains seeded false findings fails it too.
 
 ## Auditor selection — 7 parallel specialist branches
 
````

**What this diff deliberately does not do.** It does not instruct the refuter to
be more aggressive, does not set a target kill rate, and does not add a
threshold of any kind. §3 gives no evidence that the refuters were insufficiently
aggressive, and §3.4 gives four reasons why a target rate would be unjustifiable.
Every change makes the gate's own behaviour *recordable*; none changes what the
gate is supposed to decide.

## 7. The eval that would test it

### 7.1 The existing suite does not answer this question

`~/.claude/skills/audit-remediate-loop/evals/` holds a case registry of 8 cases
(E1–E6 defects, C1–C2 clean controls) and 8 fixtures. Read in full. It does not
answer the H1/H2 question, for four reasons:

1. **It measures gate recall, not gate precision.** Its headline metric is the
   fraction of E1–E6 whose seeded defect *survives* the gate; the README states
   "a refute gate that kills a seeded true defect fails the eval". That detects
   an over-aggressive gate. H2 alleges an under-aggressive one, which the suite
   has no case designed to detect.
2. **There is no seeded *false* finding anywhere in the registry.** The nearest
   thing is C1/C2, whose pass condition is zero post-gate findings on a clean
   fixture. But the findings the gate would have to kill there are whatever the
   auditors spontaneously raise — an uncontrolled stimulus that varies run to
   run and can legitimately be empty. A run in which the auditors raise nothing
   on C1 scores a pass while testing the gate not at all.
3. **The fixture population is the wrong class.** All 8 fixtures are ≤ 40 lines
   of Python or short Markdown. The artifacts gated on 2026-09-02 were
   multi-thousand-line prose reviews, a 149-entry CSL-JSON store and a frozen
   protocol. §3.4(a) objects to reasoning from C/C++ targets to prose artifacts;
   reasoning from 40-line fixtures to the same prose artifacts is the same
   objection at a shorter distance.
4. **No baseline run exists.** The directory contains the registry, the README
   and the 8 fixtures, and no results file. The README's own GEPA section is
   marked "deferred until ≥ 1 full baseline run of this suite exists". The
   session trail's referral of the 7.3% figure to `evals/` as "an input to the
   gate-recall calibration" refers to a calibration that has not been run and, as
   constituted, would not test this.

### 7.2 The arm that would test it

A **seeded-false-finding arm**, run at the gate rather than at the auditors.

**Design.** Cases `F1…Fn`, each a `{fixture, injected_finding, ground_truth}`
triple. The injected finding is a fully-formed 8-field findings-schema object
handed directly to the refuter; the auditor branches do not run. Half the
injected findings are **true** (drawn from the E1–E6 ground truth, restated as
an auditor would file them); half are **false by construction** — each misreads
its fixture in a way recorded in the registry, so that the correct disposition is
known before the run. Defect classes for the false half should mirror the classes
this session actually produced: a page locator that is in fact correct
(the A/1/LITERATURE-1-1 shape), an arithmetic recount that is in fact wrong (the
A/2/REV-2-2 shape inverted), a scope objection to a claim the artifact does
qualify (the C/1/REV-1-1 shape), a source characterised as inaccessible that is
in fact reachable (the A/1/LITERATURE-1-5 shape).

**Metrics.** *Gate precision*: fraction of seeded-false findings dropped. *Gate
recall*: fraction of seeded-true findings retained — the existing metric,
preserved so a change cannot buy precision with recall. Both reported per run
with the raw counts.

**Why this and not more trail analysis.** It supplies the one thing verdict item
4 says is missing: ground truth about whether a retained finding was true. With
it, H1 and H2 separate directly — a gate that drops seeded-false findings at a
high rate while this session's rate stayed at 7.3% supports H1 (the findings
were mostly right); a gate that retains seeded-false findings supports H2.

**Sizing, stated as MDE rather than retrospective power** (charter rule; retro
power is never computed here). Conventions in §8.

- *Single-arm, current brief only.* Testing H₀: gate precision ≤ 0.30 at
  one-sided α = 0.05, the smallest n of seeded-false cases with detection
  probability ≥ 0.80 at a true precision of 0.80 is **n = 7** (reject on ≥ 5
  kills). At n = 20 the MDE is a true precision of 0.57; at n = 24, 0.56; at
  n = 30, 0.53. Below n ≈ 10 the test can only distinguish near-total success
  from near-total failure.
- *Paired, current brief against the §6 brief on the same cases* (exact
  conditional sign test, one-sided α = 0.05, discordance model p₀₁ = 0.05):
  detecting a marginal precision gain of 0.30 → 0.65 with probability ≥ 0.80
  needs **n = 24**; a gain of 0.30 → 0.55 needs n = 37; a gain of 0.30 → 0.45 is
  not detectable at n ≤ 80. At a fixed n = 24 the MDE is a net improvement of
  +0.35 in marginal precision.

**Recommended minimum: 24 seeded-false cases plus the 6 existing seeded-true
cases restated as injected findings.** That sizing is chosen so the paired
comparison in §6 is decidable at the smallest effect worth acting on; it is not
a threshold on the gate itself.

**Two conditions on running it.**

- *Hold-out.* The README's hold-out discipline binds: expand the suite and
  reserve a subset never shown to any optimizer before any GEPA run, and report
  optimized-versus-baseline figures on the held-out cases only.
- *At least one long-prose fixture.* Objection 3 above is not fixed by adding
  more 40-line fixtures. At minimum one fixture in the several-hundred-line
  documentary class, with its seeded false finding of the internal-consistency
  type that §3.3 shows is near-unkillable — otherwise the arm measures the gate
  on a population as distant from this session's as the C/C++ one is.

**What the arm still will not settle.** It measures the gate on seeded findings
whose falsity was constructed. It does not measure the gate on the naturally
occurring false findings of a real round, and it cannot, because those are
exactly what has no ground truth. The arm bounds the gate's behaviour on a known
population; it does not license reading a per-run kill rate as a quality score.

## 8. Conventions used

Zero of these is a threshold on any decision in this memo. Each is named per
`CLAUDE.md` §"Parameter & Prompt Selection".

- **CONVENTION-1 — α = 0.05.** Two-sided for the descriptive intervals in §3.3,
  one-sided for the eval sizing in §7.2. The conventional level; no
  project-specific justification exists and none is claimed. No conclusion in
  §4 turns on any interval crossing it — the intervals are reported so the
  dispersion is visible, and the verdict is argued from the disposition texts
  and the schema, not from a p-value.
- **CONVENTION-2 — the four-marker lexical screen** applied to the 140 retained
  refutations (§3.2): verbatim-quotation, attempt-failed phrasing, executed
  operation, named-and-rejected defence. Hand-built regexes, not validated
  against a labelled set. Demonstrated 4-of-4 false-negative rate on the cases
  it flagged. Used only to *select* cases for full reading, and every case it
  flagged was read; its counts are reported as a lower bound.
- **CONVENTION-3 — the internal/external partition** (§3.3): a finding is
  "external" if its own `evidence`/`reference`/`location`/`category`/`issue`
  text names a DOI resolver, a bibliographic API, a preprint or repository host,
  a URL, or the phrase "full text"/"primary source". Post hoc, chosen after
  reading the eleven drops. Reported for direction only (T4).
- **CONVENTION-4 — permutation test parameters:** B = 20,000 replicates,
  RNG seed 20260903, Pearson χ² as the statistic on the 5 × 2 round-by-outcome
  table. Seed recorded so the p = 0.506 figure is reproducible.
- **CONVENTION-5 — the eval alternatives** in §7.2 (precision 0.30 under the
  current brief, 0.65 under the revised one, discordance p₀₁ = 0.05, detection
  probability 0.80). These are stipulated to make the design's MDE computable
  before any data exist. They are not estimates — no prior run supports them —
  and the sizing should be recomputed against the first baseline run's observed
  precision.
- **CONVENTION-6 — the correction-language scan** used to enumerate the
  against-interest corrections in §3.2 and §4. Added 2026-09-03 under finding
  FORMAT-1-2. A case-insensitive scan of the `refutation_evidence` string of all
  151 gated dispositions for `only defect`, `defect .{0,25}in the finding`,
  `inaccurac*`, `imprecision`, `understatement`, `overstat*`, `misstat*`,
  `differs from the auditor`, `the finding's stated`, `the auditor's <digit>`,
  `slip`, `quibble`, `not a defect in it`. Hand-built, not validated against a
  labelled set, and *over*-inclusive by construction — `overstat*` and `quibble`
  fire on refutations that correct the artifact rather than the auditor, which
  is precisely the conflation that produced FORMAT-1-2. Every disposition
  enumerated in §3.2's table was therefore read in full and admitted only on a
  quotable correction of the *finding's own* claim. Candidates the scan flagged
  and this pass did not read to a verdict are neither admitted nor excluded, so
  the enumerated seven is a **lower bound**, not a census.

## 9. Scope of this memo

Analyses the gate. Does not re-adjudicate any finding's substance: no statement
above endorses or disputes any auditor's claim or any refuter's counter-evidence,
and the §3.1 assessment of the eleven drops is about the *form* of their
evidence, never its correctness. Modifies nothing under `~/.claude` — §6 is a
proposal for the author to apply. Does not commit and ticks no specification box.

**AI-assistance statement** (ICMJE 2026, per `CLAUDE.md`): analysis, statistics
and prose produced with `claude-opus-5` (role: idea, code, prose) as the Thread D
delegate of the session declared at
[docs/deliverables/deliverable_spec_s4-reexecution-and-repo-gaps_2026-09-03.md](../deliverables/deliverable_spec_s4-reexecution-and-repo-gaps_2026-09-03.md).
All source digests are named in §2.1. Per the spec's Self-executed list, ReproLog
and sidecar emission for this artifact are the lead session's; the clone-durable
digests of every input this memo read are given in §2.1 so the analysis is
re-derivable without them.
