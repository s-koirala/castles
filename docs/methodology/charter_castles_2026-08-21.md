---
type: charter
slug: castles
date: 2026-08-21
status: living
revision: 2
revision_note: >
  Rev 2 (2026-08-21) applies critical-reviewer round-1 findings REV-1-1 through
  REV-1-6, REV-1-16, REV-1-18, REV-1-19. Rev 1 specified a vocabulary for
  negative-result forensics without the decision procedures that make it
  discriminating; the layer set did not cover this document's own taxonomy
  terms, step 3 demanded unique attribution the evidence cannot support,
  `construct-negative` had no gate, and MDES was under-determined. Amended in
  place per the append-only rule below.
---

# castles — Research Charter

## What this is

A standing think tank. Its output is systematic reviews and methodology
documentation: durable, citable records of what is known about a question, how
that knowledge was established, and where it breaks.

The domain is deliberately unbounded and expected to grow. There is no terminal
goal state and no fixed deliverable set. What is fixed is the method.

## What this is not

**This repository specifies; it does not execute.** See
[ADR-0003](../decisions/ADR-0003-specification-not-execution.md).

In scope: corpora, definitional surveys, methods notes, failure autopsies,
agendas, decision records, and the *specification* of a test — its null, its
statistic, its surrogate, its aggregation rule, its refutation condition.

Out of scope: running the test, fitting anything, backtesting, and any artifact
reporting a result. Executing projects consume this output; a `TO COMPUTE` marker
is a handoff, not a debt this repository pays.

A branch is **complete when its test is fully specified**, not when it has been
run. This boundary was unwritten through rounds 1–3 and the agendas drifted past
it unchallenged, which is why it is stated here rather than assumed.

## Standing commitments

1. **Unbounded domain, bounded method.** Any question may enter. Every question
   is worked the same way: locate the primary sources, reproduce the reasoning,
   state what would falsify the conclusion.

   > **This commitment is an untested claim in this charter's own terms.** Every
   > agenda branch must carry a falsification test; until Rev 2 this commitment
   > carried none, while being stated as settled. Its falsification is now
   > stated in §"Falsification of commitment 1" below and is open.

2. **Negative-result forensics.** A published null is an object of study, not a
   dead end. See §"Negative-result protocol". This is the house specialty and
   the reason the project exists — see §"Prior art posture" for what is
   genuinely novel here, which is less than the phrase implies.

3. **No unlabelled constants.** Every numeric threshold in every artifact is
   either derived from a cited procedure, selected by a documented search over a
   stated objective, or explicitly labelled `CONVENTION` with its provenance.
   Inherited from `~/.claude/CLAUDE.md` §"Parameter & Prompt Selection".

4. **Causal-time discipline.** For any time-indexed claim, state what
   information was available at the decision point. Applies beyond finance:
   an epidemiological exposure window, a citation-count snapshot, and a
   backtest feature are the same problem.

5. **Attribution fidelity.** A claim traced to a secondary source is marked as
   such. Method attributions are verified against the originating paper, not
   against the field's habit of citing a review.

## Admissible output types

| Type | Path | What it is |
|---|---|---|
| Charter | `docs/methodology/charter_{slug}_{date}.md` | This document; governs method, not topic |
| Deliverable spec | `docs/deliverables/deliverable_spec_{slug}_{date}.md` | Per-session declaration of what will be produced and how it is checked |
| Systematic review | `docs/literature/lit_review_{slug}_{date}.md` | Conducted and reported to **PRISMA 2020**. See §"Systematic review standard" |
| Methods note | `docs/methodology/{type}_{slug}_{date}.md` | How a technique works, its assumptions, its failure modes |
| Failure autopsy | `docs/research_notes/autopsy_{slug}_{date}.md` | Forensic reading of a published null — see protocol below |
| Research agenda | `docs/research_notes/research_agenda_{slug}_{date}.md` | Subtopic tree with per-branch falsification tests |
| Decision record | `docs/decisions/ADR-NNNN-{slug}.md` | A choice, its rationale, its alternatives, and its reversal cost |
| Replication report | `reports/` | An attempt to reproduce a published result, with its outcome either way |

Register of nulls encountered: [failure_log.md](../../failure_log.md).

### Systematic review standard

A systematic review here is conducted and reported to **PRISMA 2020**, not to a
lighter project-local standard. At minimum: a protocol registered before
searching, eligibility criteria fixed in advance, the search strategy recorded
verbatim per database with dates, dual independent screening and extraction with
an agreement measure, a risk-of-bias instrument applied per included study, a
flow accounting of records screened and excluded with reasons, and a
small-study/publication-bias assessment. Search provenance and a CSL-JSON store
are necessary but nowhere near sufficient; a corpus with a query log is a
narrative review and must be labelled as one.

## Evidence standard

Inherits the hierarchy in `~/.claude/CLAUDE.md`: peer-reviewed literature →
official documentation → professional standards → vetted technical forums →
reproduction of the referenced method. No paraphrase without verification.

Three project-local additions:

- **Numeric claims require the primary source.** A number taken from a blog
  summary of a paper is recorded as unverified until the paper is read.
- **Benchmark rankings are recorded with their measurement scope.** A model's
  position on a leaderboard is a statement about that leaderboard's datasets,
  not about the model. Rankings are never carried across domains without saying
  so.
- **Evidence tier travels with the claim.** Every failure_log row and every
  load-bearing citation carries its tier: `peer-reviewed`,
  `accepted-preprint`, or `preprint`. **No artifact may treat a `pending` or
  `preprint`-tier row as settled.** Phrasing that forecloses a question the
  register holds open ("the question is not whether they failed") is a defect.

## Publication-bias posture

The project's input stream is published nulls, which are a non-random sample:
selected on surprise, on contrarian framing, or on having refuted a
high-profile positive. Nothing in the protocol below distinguishes "this null is
informative" from "this null is what survived the file drawer" unless the
following are recorded per source:

- Was the study preregistered, and is there a registry or registered-report
  record?
- Does a matched positive literature exist on the same question?
- Is the null the study's primary declared outcome, or a secondary result
  reframed?

An unrecorded answer is recorded as unknown, not skipped.

## Negative-result protocol

Applied to any result reported as a null, a failure, or a non-replication.

> `CONVENTION` — provenance. The step sequence and the localization layers below
> are **this project's own construction**, not an established protocol. Only
> step 2's prohibition on retrospective power is externally grounded. See
> §"Prior art posture" — substantial existing methodology covers much of this,
> and the survey locating this protocol against it has **not yet been done**.

**1. Restate the null precisely.** What specific hypothesis failed to be
rejected, at what alpha, against what alternative? "It didn't work" is not a
null; it is an absence of a stated test.

> **Branch for test-free sources.** Benchmark leaderboards and many ML papers
> report no hypothesis test at all, and will be a large share of this project's
> input. For these: either reconstruct a test from the reported quantities and
> record the reconstruction, or classify the row `no-stated-test` and record
> that localization is therefore **unavailable**. Do not assign a layer anyway.

**2. Interrogate the design's resolution.** Compute the **minimum detectable
effect size** given n, variance, alpha, **and a stated target detection
probability**. MDES is undefined without the power target; the target is itself
a `CONVENTION` requiring provenance under commitment 3.

Do **not** compute retrospective power — post-hoc power is a monotone transform
of the observed p-value and carries no information beyond it
([Hoenig & Heisey 2001](https://doi.org/10.1198/000313001300339897),
*The American Statistician* 55:19–24).

The comparator must be **sourced**, not judged: a prior meta-analytic estimate,
a decision-relevant threshold, or a declared smallest effect size of interest
(SESOI). "Implausibly large" without a source is the judgment call commitment 3
forbids.

> **Directionality caveat.** A wide MDES makes a null uninformative about the
> effect. The converse does **not** hold automatically: a tight MDES licenses an
> informative-null reading **only where the target is identified by the design**.
> MDES is a variance quantity; observational work is usually bias-dominated, and
> confounding can displace an estimate far beyond a tight MDES. Where the target
> is not identified, record the layer as `question` and do not read the MDES as
> evidence about the effect.

**2b. Assess the source design's validity, not only its resolution.** A null
produced by a design biased toward the null shows a tight MDES and is still
uninformative. Record explicitly whether any of these are present:
non-differential misclassification, contamination between arms, low adherence,
differential attrition, an inappropriate active comparator, or a nested-model
comparison tested with a statistic that is degenerate under nesting.

**3. Localize the failure — with a discriminating observation.** A single null
refutes only the *conjunction* of the substantive hypothesis and its auxiliaries.
Taken alone it cannot discriminate among layers. Therefore every layer
assignment must record:

  (i) the alternative layers explicitly considered;
  (ii) the observation that would distinguish the asserted layer from each
       alternative;
  (iii) whether that observation is available from the source, obtainable by
        re-analysis, or unobtainable.

**A layer with no discriminating observation is recorded `undetermined`** — not
as a provisional guess. Promotion from `undetermined` to settled requires that
the discriminating observation was actually obtained and pointed the stated way.

Layers:

| Layer | Meaning |
|---|---|
| `method` | The estimator or model was wrong for the structure |
| `implementation` | Right estimator, wrong code. The dominant cause of computational non-replication, and has the opposite disposition to `method` |
| `data` | The measurement lacked resolution, coverage, or provenance |
| `precision` | n and variance were insufficient; the design could not resolve the effect. Distinct from `data` — the remedy is more of the same, not different measurement |
| `estimand` | The effect exists but the reported quantity is a marginal average masking a moderator |
| `question` | The target quantity is not identified by the design, regardless of n |
| `construct` | The measured entity does not appear to exist as posited. Gated — see below |
| `temporal-validity` | The construct existed and stopped: decay, regime shift, distribution shift |
| `attribution` | The result is real; the mechanism claimed for it is not supported |
| `source-artifact` | The "null" is a non-replication of an original Type I error inflated by selective reporting. The failure is in the prior literature |
| `undetermined` | No discriminating observation available. The default |

Every term in §"Failure taxonomy" must resolve to a layer in this table. That
mapping is a lint condition on new failure_log rows.

**Gate on `construct`.** Concluding a construct does not exist requires ruling
out every method that could have detected it — an unbounded quantifier. The
layer may be asserted only with **all four** of:

  (i) a named surrogate or null-generating process preserving every *known*
      non-construct property of the data — not a straw-man surrogate;
  (ii) an **equivalence test against a pre-registered bound**, not a failed
       difference test. Failure to reject is not evidence of absence;
  (iii) a **positive control** — an injected instance of the construct at the
        smallest interesting magnitude must be recovered by the same statistic,
        demonstrating the test could have found it;
  (iv) an explicit scope: instrument, timescale, feature set, measurement, **and
       — where the construct has competing operational definitions — the
       definition class the verdict applies to**. A `construct-negative` on one
       class is silent about the others. The level survey is the worked case: 76
       definitions partition into three classes with different admissible nulls,
       and a verdict naming no class is not localised;
  (v) a **negative control on the surrogate itself** — the surrogate must be shown,
      by the same statistic, *not* to exhibit the construct.

Absent any of the five, the layer is `undetermined`.

> **Why (v) exists (quant-auditor F-3-2).** Condition (i) pushes the surrogate
> toward the real data as the preserved-property list grows. Gate (ii)'s
> equivalence test protects only one end of that gradient. A *low-power* surrogate
> is caught — TOST fails to reject and correctly withholds `construct`. A surrogate
> that **absorbs the construct** is not: it shrinks the real-vs-surrogate point
> estimate toward zero *without* inflating its standard error, so TOST rejects and
> licenses `construct-negative` precisely when the null was mis-specified. Step 2b
> already names "an inappropriate active comparator" as a null-biasing defect but
> applied that scrutiny only to *external* sources, never to this project's own
> surrogates. Without (v) the gate contains an unmanaged gradient toward the
> project's own highest-status conclusion — the negative-results analogue of the
> p-hacking pressure the gate exists to prevent.
>
> The standing tradeoff, stated so it is chosen rather than inherited: a
> straw-man null inflates Type I error toward a false `construct`-positive; an
> alternative-absorbing null produces a false `construct-negative` by equivalence.
> The resolution is a **model-based null of stated form**, not a maximally-matched
> resample of the series whose construct status is the question. Step 2b's list is
> extended reflexively with: *"a surrogate estimated from the data under test,
> which inherits the alternative."* Note the standing hazard:
`construct` is the project's highest-status finding and, without this gate, its
cheapest to claim. That is the negative-results analogue of p-hacking pressure.

**4. Look for the transferable positive.** A null in domain A sometimes
identifies a constraint that is a live result in domain B. **Record "none found"
when none exists** — this is required, not optional. A transfer column that is
uniformly populated carries no information; a 100% transfer rate over any window
is itself a signal to re-audit the column's criterion.

An untested adjacent target is not a transfer. Naming a target the source did
not examine, and inferring it is unaffected, is a category error — "not tested"
is not "not implicated."

**5. Register the disposition.** Append to [failure_log.md](../../failure_log.md)
with the fields the schema requires **and a pointer to the autopsy document**.
Nulls are never deleted and never silently dropped.

## Failure taxonomy

`CONVENTION` — project-local vocabulary, not drawn from a published taxonomy.
Each term maps to a layer in step 3; the mapping is asserted here and linted.

| Term | Meaning | Layer |
|---|---|---|
| `null` | A stated hypothesis was tested and not rejected | (any) |
| `underpowered` | The design's MDES exceeded any sourced plausible effect | `precision` |
| `unidentified` | The design cannot recover the target quantity regardless of n | `question` |
| `misattributed` | The result is real but the claimed mechanism is not supported | `attribution` |
| `non-replication` | A prior positive did not reproduce under a stated protocol | `implementation` or `source-artifact` |
| `construct-negative` | The measured entity does not appear to exist as posited | `construct` (gated) |
| `no-stated-test` | The source reported no hypothesis test; localization unavailable | `undetermined` |

## Prior art posture

**The survey locating this protocol against existing practice has not been
done.** Stating that plainly, rather than presenting the protocol as unsituated,
is the honest position — and it is the project's first scheduled systematic
review.

Bodies of practice that already cover much of what the five steps do:
equivalence testing and TOST for making nulls informative; SESOI specification,
which is exactly the comparator step 2 needs; registered reports and
results-blind review as the structural fix for the file drawer; severity and
design-sensitivity analysis as the formal treatment of "could this design have
found it"; and the existing negative-results and replication-study literature.

Until that review is written, no claim of novelty is made for anything in
§"Negative-result protocol".

## Falsification of commitment 1

Commitment 1 asserts the method is domain-general. It is currently supported by
zero artifacts: both seeded agendas are finance and software, and the only
operational procedure anywhere in the protocol — surrogate-data testing — is a
time-series technique with no cross-sectional analogue.

**Test.** Work one epidemiological null and one engineering/reliability null
through all five steps.

**Refutation condition, stated in advance:** if steps 2 and 3 cannot be executed
on a case-control null without importing design-specific machinery not in this
charter — a study-design taxonomy, a per-design reporting standard, DAG-based
adjustment-set selection, unmeasured-confounding sensitivity analysis, a
missingness assumption and imputation policy — then commitment 1 is falsified
and the domain is rescoped to time-indexed questions.

A §Design-family annex mapping each design family to its reporting standard, its
identification requirement, and its version of steps 2 and 3 is the remedy if
the test fails. It has not been written.

## What this charter does not do

It does not set priorities, deadlines, or a topic roadmap. Topic selection is
driven by curiosity and by what the open questions in existing artifacts
surface. The charter constrains *how* a question is worked, never *which*.

## Status

Living document. Amendments are made in place with a `revision` bump and a
changelog entry, not by superseding files. Superseded text is not silently
overwritten where a reader could be misled — the `revision_note` records what
changed and why.
