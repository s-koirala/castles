---
type: research_agenda
slug: architecture
date: 2026-08-21
status: open
corpus: none  # no corpus commissioned for this thread yet
---

# Research agenda — architecture

**Question.** What is the correct shape for a research environment that ingests
a live stream, runs models against it, and presents results to a human — such
that the research remains reproducible, the components remain independently
testable, and no layer's failure silently corrupts another's?

**Framing.** This agenda is about the *carrier*, not the signal. It is scoped so
that its conclusions survive whatever the regime-classification agenda finds.
An environment whose value depends on a particular model working is
mis-designed.

> **Test-design requirement (charter step 2).** Every test below states its
> alpha, its target detection probability, and the MDES that follows, before it
> is run. A test with no stated MDES is not runnable. Where a quantity is not
> yet computable it is marked `TO COMPUTE` rather than omitted — an omitted
> parameter becomes an unlabelled constant chosen after seeing the data.
> On failure, each test names the disposition and the
> [failure_log.md](../../failure_log.md) row it produces.

## 1. Platform selection

Open questions:

- Scripting-host capability matrix: sandboxing, external assembly references,
  I/O permissions, threading model. The binding constraint is not charting
  quality but whether the host can hold arbitrary code and do network I/O.
- Shared computation kernel: a single `netstandard2.0` assembly targeting both
  NinjaTrader 8 and MultiCharts .NET, with adapters carrying no logic. Whether
  the runtime compatibility claim holds in practice is testable and untested.
- Sidecar inter-process patterns: named pipes, ZeroMQ, shared memory. Staleness
  semantics, and how a display degrades rather than lies when inference is late.
- Thread discipline: what blocks a chart calculation thread, what cascades into
  an execution thread, and how to prove a component does neither.
- Market data licensing: the display versus non-display / derived-data
  distinction, and whether feeding an external model reclassifies a
  non-professional subscription. This is a compliance question with a factual
  answer in a specific subscriber agreement, not a judgement call.
- Vendor comparison: Databento, Rithmic, IQFeed, CQG, dxFeed — latency, history
  depth, API surface, cost, and the terms above.
- Bar construction: time versus tick versus volume versus dollar bars
  ([López de Prado 2018](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086),
  *Advances in Financial Machine Learning*, Wiley, ch. 2), grounded in the
  trading-time result that returns normalize under an activity-subordinated
  clock ([Clark 1973](https://doi.org/10.2307/1913889), *Econometrica*
  41:135–155; [Ané & Geman 2000](https://doi.org/10.1111/0022-1082.00286),
  *The Journal of Finance* 55:2259–2284;
  [Easley, López de Prado & O'Hara 2012](https://doi.org/10.3905/jpm.2012.39.1.019),
  *The Journal of Portfolio Management* 39(1):19–29), and how bar choice
  interacts with the deseasonalization requirement from the regime agenda.
  Roll conventions for continuous futures as an experimental variable rather
  than a default — noting the null on record:
  [Carchano & Pardo 2009](https://doi.org/10.1002/fut.20373) (*Journal of
  Futures Markets* 29(7):684–694) find **no significant differences** among
  five roll criteria for stock index futures. Whether that null transports to
  physically-settled or less liquid contracts is open; cite it for "studied
  choice, no detected difference where tested — indecisive about magnitude
  absent an equivalence bound", never for material sensitivity. Failure to
  reject is not evidence of absence (charter, construct gate (ii)).
- Reproducibility of a stream-fed system: what a dataset checksum means when the
  input is a live feed, and what the durable record of a live run should be.
  Existing practice assumes a batch run over fixed inputs
  ([Peng 2011](https://doi.org/10.1126/science.1213847), *Science*
  334:1226–1227;
  [Sandve, Nekrutenko, Taylor & Hovig 2013](https://doi.org/10.1371/journal.pcbi.1003285),
  *PLOS Computational Biology* 9(10):e1003285), which is exactly the assumption
  a live feed violates.

**Falsification.** Build the shared kernel and load the identical assembly into
both hosts. If outputs differ beyond the stated tolerance, the shared-kernel
premise is false and the cross-platform design collapses to per-platform
reimplementation. One-day test gating a large design commitment.

Two controls the first draft lacked:

- *Tolerance.* "Different" is undefined. Differing JIT behaviour, floating-point
  contraction, and target architecture guarantee **some** bit-level difference, so
  without a stated tolerance the test either always fails or gets adjudicated
  after the fact — and an after-the-fact threshold is an unlabelled constant under
  charter commitment 3. State it in ULPs or relative error — the attributed
  units of floating-point comparison, defined and interconverted in
  [Goldberg 1991](https://doi.org/10.1145/103162.103163) (*ACM Computing
  Surveys* 23(1):5–48), with format and rounding semantics fixed by
  [IEEE 754-2019](https://doi.org/10.1109/IEEESTD.2019.8766229) — with
  provenance, before running. `TO COMPUTE`.
- *Input path.* "The same inputs" is not controlled if each host supplies its own
  bars: a difference is then far more likely to come from bar construction or roll
  handling than from the kernel, and the test cannot attribute. Feed both hosts a
  **byte-identical serialized bar array** and verify its SHA-256 on both sides.

## 2. Prior art

Open questions:

- Time-series foundation model landscape:
  [Kronos](https://arxiv.org/abs/2508.02739) (reported accepted to AAAI 2026 —
  self-reported in the authors' repository; no proceedings record yet),
  [Chronos-2](https://arxiv.org/abs/2510.15821), TimesFM, Moirai,
  TiRex, FlowState, TimeGPT. Architecture, covariate support, context length,
  input dimensionality constraints, and license.
- Benchmark infrastructure: GIFT-Eval, [fev-bench](https://arxiv.org/abs/2509.26468),
  [FinTSB](https://arxiv.org/abs/2502.18834). What each measures,
  what none measures, and the domain composition that determines whether a
  ranking transfers.
- Open-source stacks: OpenBB, lightweight-charts, OpenCharts, NautilusTrader.
  Maintenance status, license obligations, and the honest build-versus-adopt
  boundary.
- LLM-to-platform bridges: the MCP server ecosystem for market data and
  execution. Security posture, and execution authority as a distinct hazard
  class from data access.
- Commercial AI-overlay vendors: what they claim, what they disclose, and the
  systematic absence of calibration reporting across the category.
- **Failure autopsy** — the branch's distinctive contribution. Why LLM
  components contributed nothing to time-series forecasters
  ([Tan et al. 2024](https://arxiv.org/abs/2406.16964), NeurIPS), and why
  pretrained TSFMs fail on returns (Noguer i Alonso & Pereira Franklin,
  [arXiv 2606.27100](https://arxiv.org/abs/2606.27100) — **unrefereed preprint**;
  the tier matters because this is the most load-bearing negative result in the
  project). Both are registered in
  [failure_log.md](../../failure_log.md) — as F002 and F001 respectively — and
  warrant full five-step autopsies under the charter protocol. Whether the
  reported failures hold is open at their evidence tiers — F001's source is an
  unrefereed preprint, and the charter's tier rule forbids treating it as
  settled. The autopsies' object is what the failures, *if they hold*, identify
  about the data.

**Adoption policy** (not a falsification — relabelled per audit). For each adopted
component, state the specific claim relied on and the test that would refute it.
A dependency adopted on reputation rather than on a stated, tested claim is
recorded as unverified. A policy is complied with or not; it has no failure state.

The leaderboard-transfer case was withdrawn as a falsification: the charter
already declares it false as a standing commitment ("a model's position on a
leaderboard is a statement about that leaderboard's datasets"), so testing it is
a demonstration, not a test, and nothing in this branch depends on it.

**Falsification** (branch-level, on a claim the branch actually relies on). The
branch presumes a sidecar staleness contract **degrades rather than lies**.
Refuted by injecting inference latency beyond the contract bound and observing
whether the display shows its stated degraded state or a stale value presented as
current. A single instance of the latter refutes the contract and the sidecar
pattern is redesigned or abandoned. This is cheap, pre-committed, and decisive.

*Parameters:* contract bound `TO COMPUTE`; injected latencies swept from below to
well above it; n trials `TO COMPUTE` for the false-negative rate on a rare stale
display.

## 3. Human-in-the-loop frame

Open questions:

- Human–AI complementarity: the meta-analytic finding that combinations
  underperform the better component on average, and the moderator that
  determines when they do not
  ([Vaccaro, Almaatouq & Malone 2024](https://www.nature.com/articles/s41562-024-02024-1),
  *Nature Human Behaviour* 8:2293–2303; F003 in
  [failure_log.md](../../failure_log.md)).
- Judgmental adjustment of statistical forecasts: the large-versus-small
  adjustment asymmetry and the directional optimism bias
  ([Fildes, Goodwin, Lawrence & Nikolopoulos 2009](https://doi.org/10.1016/j.ijforecast.2008.11.010),
  *International Journal of Forecasting* 25(1):3–23). The closest empirical
  analogue to a trader overriding a model, and one of the few places where
  human-in-the-loop is net positive.
- Clinical versus actuarial judgment: the mechanical-combination result (Meehl
  1954, *Clinical versus Statistical Prediction*, University of Minnesota Press;
  [Dawes, Faust & Meehl 1989](https://doi.org/10.1126/science.2648573),
  "Clinical versus actuarial judgment", *Science* 243(4899):1668–1674), and the
  broken-leg exception that licenses override on information the model provably
  cannot see. Formalizing what counts as a broken leg is an open problem.
- Algorithm aversion
  ([Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033),
  *Journal of Experimental Psychology: General* 144(1):114–126) versus
  appreciation ([Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005),
  *Organizational Behavior and Human Decision Processes* 151:90–103), and
  accuracy disclosure as a reliance-calibration intervention.
- Uncertainty visualization — two distinct results, often conflated:
  (a) the cone boundary is read as a categorical danger zone and cone growth is
  misread as storm growth
  ([Ruginski et al. 2016](https://doi.org/10.1080/13875868.2015.1137577),
  *Spatial Cognition and Computation* 16(2):154–172); (b) individual ensemble
  members are over-weighted — a rig lying on an ensemble track was judged more
  damaged in 99.68% of trials even when a closer off-track location existed
  ([Padilla, Ruginski & Creem-Regehr 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5626802/),
  *Cognitive Research: Principles and Implications* 2:40). Quantile dotplots and
  hypothetical outcome plots as candidate mitigations; deterministic construal
  error as the proposed mechanism.
  **Open question, not a finding:** whether instruction reduces these biases is
  *untested* in both papers — the 2017 paper raises supplemental instruction only
  as a suggestion. Locating a study that actually tested it is a corpus task.
- Anchoring and insufficient adjustment when a numeric forecast is displayed.
- Experimental design for a single-operator decision aid: N-of-1 protocols,
  block randomization, endpoint selection under low signal-to-noise, and
  minimum detectable effect rather than retrospective power.

**Falsification.** Any decision-aid design is a human-factors claim, not a
statistical one, and cannot be backtested. It is refuted or supported only by a
block-randomized on/off protocol with a pre-registered endpoint on the operator.

*The escape hatch is withdrawn.* The first draft ended "a design shipped without
that protocol is recorded as an untested hypothesis, not as a deliverable" — which
converted the test into an optional labelling step with no outcome that forces
abandonment. Replaced with a consequence: **an untested design may not be cited
by any other artifact in this project, and expires 180 days after authoring**
(`CONVENTION`; interval chosen to force revisit within a plausible research cycle,
no empirical basis, revise when one exists).

*Gate before any design work.* Compute the MDES for the proposed N-of-1 design
under a stated target power and a **sourced** plausible aid effect — before the
branch produces any design. The branch's own open-question list already flags
that its endpoint may be under-resolved at achievable n. If the MDES exceeds any
plausible aid effect, say so plainly, close the measurement branch, and downgrade
this branch's outputs from *findings* to *design rationale*. That is an honest and
useful position, and it is the expected outcome.

*Parameters:* alpha `TO COMPUTE`, target power `TO COMPUTE`, sourced plausible
effect `TO COMPUTE`, achievable n `TO COMPUTE`. Shares its design with
[context-portability](research_agenda_context-portability_2026-08-21.md) branch 4 —
solve once, reuse.

## Cross-branch open questions

- Does the sidecar pattern generalize? The same shape — fast deterministic
  display layer, slow probabilistic inference layer, explicit staleness contract
  — appears in clinical decision support and in operations dashboards. Whether
  the staleness-contract design transfers is worth a separate note.
- What is the reproducibility unit for an interactive system? Existing
  reproducibility practice assumes a batch run with fixed inputs. A
  human-in-the-loop environment has neither, and the field has no settled
  answer.

## Verification status

Citations and factual platform claims in this document are queued for
verification by the `literature-check` branch declared in
[deliverable_spec_think-tank-charter_2026-08-21.md](../deliverables/deliverable_spec_think-tank-charter_2026-08-21.md).
Platform capability claims in particular are version-dependent and are dated to
2026-08-21.

Branch-1 method attributions (bar construction, floating-point tolerance, roll
conventions, reproducibility) were added 2026-08-21 under
[deliverable_spec_round3-remediation_2026-08-21.md](../deliverables/deliverable_spec_round3-remediation_2026-08-21.md);
each was verified against its Crossref record and the doi.org handle API before
insertion.
