# ADR-0003 — castles specifies; it does not execute

- **Status:** Accepted
- **Date:** 2026-08-21
- **Deciders:** Sajan Koirala
- **Supersedes:** none. Narrows the scope stated in ADR-0001 §Decision.

## Context

The charter describes castles as a think tank producing "systematic reviews and
methodology documentation." Rounds 1–3 of the audit loop, and the agendas written
in them, drifted past that: branch falsification tests were specified with
parameter lines, MDES gates, and multiplicity registers as though this repository
would *run* them. A round-3 recommendation went further and proposed enforcing the
multiple-testing convention through a gate that blocks inference runs — of which
this repository has none and will have none.

The author has stated the boundary explicitly: **this directory's purpose is
knowledge and literature review, not coding and testing.**

That boundary was never written down, so nothing caught the drift.

## Decision

**castles produces specifications, surveys, and methodology. It does not produce
results.**

Concretely:

- **In scope:** literature corpora, definitional surveys, methods notes, failure
  autopsies, research agendas, decision records, and the *specification* of tests —
  their null, statistic, surrogate, aggregation rule, and refutation condition.
- **Out of scope:** running those tests, fitting models, backtesting, and producing
  any performance or inference result.
- **Executing projects consume this repository's output.** Where an agenda states
  a parameter as `TO COMPUTE`, computing it is the executing project's work, and the
  value is recorded *there* with its provenance, not backfilled here.
- **Conventions are authored here and enforced there.** The multiple-testing
  aggregation rule is a good example: castles decides that existence claims need
  family-wise control and absence claims are intersection-union tests needing none,
  and writes that down. The gate that blocks a non-compliant run lives in the
  project that runs things.

## Consequences

**Positive**

- The audit branches' most valuable finding is reframed correctly. quant-auditor
  demonstrated that a specification in this repository would have rejected
  unimodality on pure noise at 35–90%, rising with sample size. Under this ADR that
  is not an abstract methodological note — it is **a defect caught in the product
  before anyone built on it**, which is the entire value proposition of a
  specification shop.
- Falsification tests stop being aspirational. An agenda branch is *complete* when
  its test is fully specified, not when it has been run. That is an achievable
  definition of done, and the current one was not.
- The scope boundary is now checkable: an artifact reporting a *result* is out of
  scope and should be produced elsewhere.

**Negative**

- Parts of the `--kind=quant` scaffold are now definitively inert:
  `config/instruments/`, `logs/promotions/`, and the `promoted` status in
  `hypothesis_backlog.md` all presuppose an execution pipeline. Retained rather than
  removed, per ADR-0002's frozen-record decision, but they should not be populated.
- The reproducibility contract in `CLAUDE.md` — ReproLog per artifact-producing run,
  dataset checksums, RNG seeds — has no trigger here, since no run produces an
  artifact. It remains correct for the executing project and dormant for this one.
- A specification cannot be validated by its own results. This repository's quality
  control is therefore entirely adversarial review, which the audit trail already
  records as having a weak verification layer. That is now a structural feature, not
  a temporary gap.

**Neutral**

- ADR-0001's `--kind=quant` decision is unaffected. The layout was chosen for its
  literature-review and register structure, and those remain the right structures.

## Consequence for the multiple-testing convention

The convention is still owed and is still authored here. Its statement:

- **Existence claims** ("at least one of these works") are union alternatives and
  require family-wise error control across the registered family — White's Reality
  Check or Hansen's SPA, which respect the dependence among members.
- **Absence claims** ("none of these works") are intersection nulls tested by
  intersection-union: each member at level alpha, **no adjustment**, and each member
  must be an *equivalence* test against a pre-registered bound rather than a failed
  difference test.
- **Cross-instrument structure must be declared before data is examined.** Four
  instruments are either four members of one family (correct across them) or a
  replication design (each pre-registered separately, with the claim being about
  consistency). These are different tests and the choice is not recoverable after
  the fact.

Where the register and the gate live is the executing project's decision, not this
one's.
