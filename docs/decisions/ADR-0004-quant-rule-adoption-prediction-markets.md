# ADR-0004 — quant-project rules adopted, by explicit reference, for the prediction-market branch

- **Status:** Accepted
- **Date:** 2026-09-02
- **Deciders:** Sajan Koirala
- **Supersedes:** none. Exercises the adoption mechanism reserved in
  [ADR-0001](ADR-0001-project-kind-and-scope.md) §Decision; bounded by
  [ADR-0003](ADR-0003-specification-not-execution.md).

## Context

This session opens a new research branch on arbitrage and market-making in
binary event markets, with Kalshi as the venue of interest.

`CLAUDE.md` §Scope records that this path matches no cwd glob in
`rules/quant-project.md`, so those rules do not auto-activate here, and that they
are "adopted **by explicit reference** where a given analysis justifies it, and
each adoption is documented at its site." `REVIEW.md` carries the same
restriction in stronger terms after audit finding M-9: its directives "are
time-series/markets-specific and bind only work that is actually time-indexed
financial analysis," and it names, as the harm to avoid, handing a reviewer of a
non-markets artifact blocking directives about corporate-action adjustment and
Sharpe bootstrap CIs.

The new branch is time-indexed financial analysis. It is the first thread in this
repository for which that is true. Nothing in the repository yet records which
directives bind it, and the two failure modes are symmetric: leaving the branch
ungoverned would let unattributed folklore factors into a corpus synthesis, while
adopting the rule set wholesale would apply seven directives about backtest
mechanics to a literature review that computes nothing.

## Decision

**`rules/quant-project.md` and `REVIEW.md` are adopted for the prediction-market
branch, and for that branch only.** The adoption is scoped by branch, not by
repository and not by file extension.

The branch is delimited as: `docs/methodology/protocol_kalshi-arbitrage-review_*`,
`docs/literature/lit_review_kalshi-arbitrage_*`,
`docs/literature/references_kalshi-arbitrage.json`,
`docs/literature/search_logs/kalshi-arbitrage/`,
`docs/research_notes/research_agenda_prediction-market-microstructure_*`, and any
successor artifact that names this branch in its front matter.

### Which directives bind at the present stage

The branch is at a literature-only stage. It compiles and synthesizes published
work; it acquires no market data and computes no estimate.

**Binding now — `REVIEW.md` blocking directive 8 (citation or derivation).**
Every factor, signal, or trading rule appearing in branch artifacts carries a
citation to published research or an in-repo derivation. Unattributed folklore
factors are a blocking defect. This directive binds because it constrains what
may be *written*, and writing is what this stage does. It is the directive the
branch is most exposed to: a survey of arbitrage strategies is exactly the genre
in which folklore travels uncited.

Also binding now, from `rules/quant-project.md` §Published research and
§Reporting, in their documentary sense: any operating characteristic quoted from
a source is attributed to that source, and any reported backtest result quoted
from the literature carries the universe, cost model, and sample window the
source itself declared — a quoted Sharpe with no stated cost model is reported as
such, not laundered into a bare number.

**Not binding now — `REVIEW.md` blocking directives 1 through 7.** No-look-ahead,
split integrity, corporate-action adjustment, return-convention declaration, HAC
standard errors, Sharpe confidence intervals, and multiple-testing control across
strategies all presuppose an executed analysis. There is none. Invoking them
against a literature corpus is the precise error `REVIEW.md`'s own scope
correction forbids.

**These seven bind the branch's first empirical stage, wherever it occurs.**
Under [ADR-0003](ADR-0003-specification-not-execution.md) that stage does not
occur in this repository: castles specifies and does not execute. The obligation
therefore attaches to the branch's *specifications* — a test specified here must
be specifiable *under* directives 1-7, and any specification that could not
satisfy them is defective at the point of writing even though nothing here will
run it.

### Boundary against ADR-0003

This ADR adopts a review standard. It does not license execution. No branch
artifact acquires Kalshi market data, calls an exchange API, fits a model,
backtests, or states a tradeable rule. Where the corpus exposes a testable
proposition, the branch specifies the test — null, statistic, surrogate,
aggregation rule, refutation condition — and the value of any parameter is left
`TO COMPUTE` for an executing project, per ADR-0003 §Decision.

### Boundary against the other threads

The adoption does not extend to the explosive-regime review, the charter, the
context-portability thread, or the architecture agenda. The explosive-regime
thread is the nearest neighbour and the most tempting to sweep in — it is about
financial time series — but it is a methodological survey of date-stamping
econometrics, not an analysis of a return series, and `REVIEW.md` binds "work
that is actually time-indexed financial analysis." It stays out.

## Consequences

**Positive**

- The branch has a stated review standard before its first artifact exists,
  rather than one applied retroactively at audit.
- The directive-8 requirement is enforceable at the corpus stage, where an
  unattributed claim is cheap to catch, instead of after it has been carried
  into an agenda and cited onward.
- The literature/empirical split is written down, so a future session cannot
  reach directives 1-7 by drift, and cannot avoid them by claiming the branch
  was never a markets branch.

**Negative**

- The repository now has two governance regimes and a branch boundary to
  maintain. A misfiled artifact is governed wrongly, and nothing mechanical
  detects that — the branch delimitation above is prose, checked by reviewers.
- "Time-indexed financial analysis" is a judgement, not a predicate. This ADR
  decides one case; the next borderline thread will need its own.

**Neutral**

- No existing artifact changes status. The adoption is prospective.

## Alternatives considered

- **Adopt repository-wide.** Rejected: contradicts `CLAUDE.md` §Scope, ADR-0001
  §Decision, and the M-9 scope correction in `REVIEW.md`, all three of which
  record that no cwd-scoped rule file auto-activates at this path.
- **Adopt nothing; rely on the general evidence hierarchy in `~/.claude/CLAUDE.md`.**
  Rejected: the general hierarchy requires citations for factual claims but
  states no rule about unattributed *factors*, which is the branch's
  characteristic failure mode and the thing directive 8 exists to stop.
- **Adopt all eight blocking directives and mark 1-7 vacuously satisfied.**
  Rejected: a vacuously-satisfied directive is indistinguishable at audit from a
  genuinely-satisfied one, and would let a future empirical stage inherit seven
  green checks it never earned.

## References

- `CLAUDE.md` §Scope — adoption-by-explicit-reference mechanism.
- [ADR-0001](ADR-0001-project-kind-and-scope.md) §Decision — kind selection and
  the non-activation of cwd-scoped rule files at this path.
- [ADR-0003](ADR-0003-specification-not-execution.md) — specification, not
  execution.
- `REVIEW.md` §"Scope correction (2026-08-21, audit finding M-9)" and
  §"Blocking directives".
- `rules/quant-project.md` §Published research, §Reporting, §Inference.
