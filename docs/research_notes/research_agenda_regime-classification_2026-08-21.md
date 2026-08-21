---
type: research_agenda
slug: regime-classification
date: 2026-08-21
status: open
corpus: docs/literature/lit_review_regime-classification_2026-08-21.md  # delivered 2026-08-21; 96 records, PRISMA 2020 partial (single screener)
---

# Research agenda — regime classification

**Question.** Can market state — range, trend, compression, transition — be
assigned causally at time *t* using only information available at *t*, with a
stated null distribution, such that the assigned state carries predictive
content about *t+1* onward?

**Standing hazard — periodicity.** Intraday volatility and volume follow a
strong deterministic time-of-day profile
([Andersen & Bollerslev 1997](https://doi.org/10.1016/S0927-5398(97)00004-2),
*Journal of Empirical Finance* 4:115–158). An unnormalized state classifier applied to
an overnight session is a clock, not a classifier. Every feature in every branch
below is deseasonalized by its time-of-day mean before use. This is a
precondition, not a refinement.

**Standing hazard — labeling.** State is latent and only observable after it
ends. Any hand-labeled training set built by inspecting charts encodes
lookahead. No branch below may use eye-labeled segments as ground truth.

> **Test-design requirement (charter step 2).** Every test below states its
> alpha, its target detection probability, and the MDES that follows, before it
> is run. A test with no stated MDES is not runnable. Where a quantity is not
> yet computable it is marked `TO COMPUTE` rather than omitted — an omitted
> parameter becomes an unlabelled constant chosen after seeing the data.
> On failure, each test names the disposition and the
> [failure_log.md](../../failure_log.md) row it produces.

## 1. Level estimation — defining [L, U] without eyeballing it

Open questions:

- Kernel density estimation on price: bandwidth by Silverman rule (Silverman
  1986, *Density Estimation for Statistics and Data Analysis*) vs
  cross-validation vs the Sheather–Jones plug-in (Sheather & Jones 1991,
  *JRSS-B*) — DOIs pending verification — and whether the choice materially
  moves mode locations. Mode *prominence* as a level-strength measure.
- Volume-at-price: point of control and value area. The 70% value-area
  definition is inherited from Market Profile / TPO and is labelled `CONVENTION`.
  **Corpus search 2026-08-21 found no primary specification** — 17 URLs returned,
  none above vendor-help tier, including a search aimed at CME/CBOT
  documentation. The label stands and is now backed by a logged search rather
  than by assumption.
- Levels as clustering: agglomerative clustering or DBSCAN (Ester, Kriegel,
  Sander & Xu 1996, KDD — DOI pending verification) over swing extrema and
  pivot points; how cluster count is chosen without a magic number.
- Level persistence: the survival function of an estimated level. Half-life, and
  whether it exceeds the estimation window.
- Book-derived levels (resting size, depth imbalance at price) versus
  price-derived levels — do they agree, and does disagreement predict anything?
- Confidence intervals on mode locations via bootstrap (Efron 1979, *Annals of
  Statistics* — DOI pending verification). A level without an interval is a
  drawing.

**Falsification.** Runs before any other work in the branch.

A bounded random walk calibrated on deseasonalized volatility alone is a **straw
man**: real series also differ from it by volatility clustering, fat tails,
jumps, intraday autocorrelation, tick discreteness, and round-number clustering.
Any of those moves the level statistics, so that surrogate would find a
difference essentially always and attribute it to levels existing. Instead:

- *Surrogate:* the **strongest** null preserving all known non-level properties —
  IAAFT / phase-randomized surrogates, or a stationary block bootstrap preserving
  the marginal distribution and dependence structure. Block length by
  Politis–White automatic selection, not chosen by hand.
- *Statistic:* **one** pre-specified discriminating statistic. **This does not
  need to be invented — three published tests for the significance of a mode
  already exist**, established by the corpus search:
  - Silverman's critical bandwidth (1981,
    [doi:10.1111/j.2517-6161.1981.tb01155.x](https://doi.org/10.1111/j.2517-6161.1981.tb01155.x))
    with bootstrap calibration (1983).
  - The **dip test** (Hartigan & Hartigan 1985,
    [doi:10.1214/aos/1176346577](https://doi.org/10.1214/aos/1176346577)) —
    bandwidth-free, with the uniform as the asymptotically least-favourable
    unimodal null.
  - **Excess mass** (Müller & Sawitzki 1991,
    [doi:10.1080/01621459.1991.10475103](https://doi.org/10.1080/01621459.1991.10475103)),
    which explicitly separates *how many* modes from *where* they are — the exact
    split this branch needs.

  Asymptotics: Mammen, Marron & Fisher 1992. Finite-sample comparison: Fischer,
  Mammen & Marron 1994. Family comparison: Ameijeiras-Alonso et al. 2018.

  > **Blocker before implementation.** Hall & York (2001), "On the calibration of
  > Silverman's test for multimodality", *Statistica Sinica* 11:515–536, is the
  > principal published calibration correction and **has no DOI in any
  > aggregator**, so it is not in the corpus. The direction of the Silverman
  > test's size distortion is therefore unstated. Obtain this paper before
  > implementing the Silverman route; the dip test does not depend on it.

  If more than one statistic is used, they are registered as a single
  multiplicity family, as branch 4 does for its parameter grid.
- *Direction:* an **equivalence test against a pre-registered bound**, not a
  failed difference test. Failure to reject is not evidence of absence, and the
  charter's `construct` gate requires this explicitly.
- *Positive control:* inject levels of known strength at the smallest interesting
  magnitude and confirm the statistic recovers them. Without this, a low-powered
  statistic delivers `construct-negative` for free.
- *Parameters:* alpha `TO COMPUTE`, target power `TO COMPUTE`, equivalence bound
  `TO COMPUTE` — each labelled `CONVENTION` with provenance when set.

*Disposition on failure:* branch 1 closes as `construct` — but only with all four
gate conditions met. Otherwise `undetermined`. Either way a failure_log row is
opened with the scope (instrument, timescale, feature set) stated.

## 2. State assignment

Open questions:

- Kaufman Efficiency Ratio (attribution to Perry J. Kaufman confirmed; the
  origin is *The New Commodity Trading Systems and Methods* 1987 / *Smarter
  Trading* 1995, **not** a bare "Trading Systems and Methods" — a specific
  edition and page still needs verifying from a licensed copy). **Corpus search
  confirms the negative:** the targeted arXiv query was the only query in the
  entire review to return **zero records**, and no Crossref source was found. No
  null distribution is published. Deriving or simulating it is unavoidable, not
  optional.
- Variance ratio test ([Lo & MacKinlay 1988](https://doi.org/10.1093/rfs/1.1.41),
  *Review of Financial Studies* 1(1):41–66), homoskedastic and
  heteroskedasticity-robust statistics (dual-statistic structure verified via
  official EViews documentation, not the paper text — publisher full text was
  not retrievable); the Chow–Denning joint multi-horizon
  extension and its size properties in short intraday windows.
- Hurst / fractal dimension: R/S versus DFA versus wavelet estimators, and the
  small-sample bias that makes short-window Hurst unreliable. Quantifying the
  window length below which the estimator is uninformative.
- Markov-switching ([Hamilton 1989](https://doi.org/10.2307/1912559), "A New
  Approach to the Economic Analysis of Nonstationary Time Series and the Business
  Cycle", *Econometrica* 57(2):357–384) and MS-GARCH.
  State count by AIC/BIC/ICL, and the documented inconsistency of BIC for hidden
  Markov models.
- Hidden semi-Markov models: standard HMMs impose geometric state durations,
  which is a poor model of regime persistence — and regime duration is precisely
  the quantity of interest.
- Filtered versus smoothed state probabilities. Published regime charts commonly
  plot smoothed probabilities, which condition on the full sample and are
  therefore lookahead. Cataloguing which published results are affected is a
  discrete, tractable corpus task.
- **Folklore audit — RESOLVED 2026-08-21 by corpus search. Both fail.**
  - **ADX:** Wilder (1978) is not indexed in Crossref, OpenAlex, arXiv, or
    Semantic Scholar. A web search returned nine URLs, **all tier-5** (broker
    marketing, charting vendors, Wikipedia). The single peer-reviewed indexed
    record touching ADX *applies* it and states no null. ADX is an unattributed
    transformation producing a number with no reference distribution.
  - **Choppiness Index:** worse — no source at **any** tier above 5. Attribution
    to E. W. Dreiss exists only on a trade blog. No book, paper, working paper,
    patent, or standard located.
  - **Bounding:** no book-indexing database was searched, so these are "no source
    in the DOI-indexed literature", not "no source anywhere".
  - *Consequence:* neither may be used as a state assigner in this project
    without first deriving or simulating its null distribution. Under charter
    commitment 5 they are unattributed folklore.

**Falsification.**

*Endpoint correction:* conditional dispersion is **tautological** for any
assigner that defines states by dispersion — Markov-switching variance models,
MS-GARCH, HMMs on volatility features. For those it is true by construction
in-sample and cannot fail. **Conditional remaining-duration is the informative
endpoint** and does not have this defect. Dispersion may be used only as a
strictly out-of-sample endpoint, with the split stated in advance.

*Multiplicity:* the sweep is roughly seven assigners × two endpoints × parameter
settings. This is a larger garden of forking paths than the parameter grid branch
4 already guards, and is **registered as one multiplicity family** alongside it.

*Branch-level disposition:* if **no** assigner in the pre-registered set yields an
out-of-sample remaining-duration difference exceeding the pre-stated MDES at the
pre-stated target power, branch 2 closes and is logged. Failure of a single
assigner implicates that assigner only.

*Parameters:* alpha `TO COMPUTE`, target power `TO COMPUTE`, MDES `TO COMPUTE`.

## 3. The transition event

Open questions:

- Bayesian online changepoint detection
  ([Adams & MacKay 2007](https://arxiv.org/abs/0710.3742) — unrefereed preprint,
  still the canonical reference). **Tier hazard:** the corpus flags this branch's
  canonical method *and* its known-failure literature as both preprint-tier.
  Fearnhead & Liu (2007, *JRSS-B*) is the peer-reviewed contemporary and is run
  alongside BOCPD so that no result in this branch rests on a preprint alone.
  Specification questions:
  hazard function specification and its sensitivity; the run-length posterior as
  a continuous breakout signal rather than a binary trigger.
- Frequentist counterparts — CUSUM, Page–Hinkley, SPRT — and Bai–Perron as the
  retrospective comparator establishing an upper bound on what an online
  detector could achieve.
- Detector operating characteristics: detection delay against average run length
  to false alarm. This is the honest way to compare detectors and is largely
  absent from the trading literature.
- Confirmation displacement expressed in deseasonalized sigma rather than fixed
  points. A fixed offset is a magic number; the multiplier is a fitted parameter
  with an interval.
- Failed-transition base rate: the fraction of detected transitions that revert
  within *h* bars. Estimable with no strategy attached, and the single number
  determining whether the setup class is worth anything.
- Volume-on-breakout folklore, tested against a time-of-day baseline rather than
  a moving average that lags the session profile.
- Distinguishing a mean shift from a variance shift — a breakout and a
  volatility expansion are different events that look alike on a chart.

**Design-resolution study** (not a falsification — relabelled per audit). Run each
detector on synthetic series with known injected changepoints, sweeping effect
size, and report the smallest recoverable shift at a stated ARL₀. This measures a
detector's resolution; it implicates a detector, never the branch's premise.

**Falsification** (branch-level). The branch presumes detectable transitions
exist as events distinct from continuous variation. Refuted if, on real
deseasonalized data, the best-resolving detector's run-length posterior is
indistinguishable — by equivalence test against a pre-registered bound — from its
behaviour on a surrogate with no injected changepoints but matched marginal and
dependence structure. If transitions are not separable from the null process,
branch 3 closes and the failed-transition base rate is undefined rather than
merely unknown.

*Parameters:* alpha `TO COMPUTE`, target power `TO COMPUTE`, ARL₀ `TO COMPUTE`,
equivalence bound `TO COMPUTE`. "Realistic effect sizes" was an unlabelled
constant and is withdrawn.

## 4. Parameter selection

Open questions:

- Objective function. Predictive log-likelihood of the state model is
  self-contained and needs no labels; an economic objective reintroduces
  alpha-mining; labeled accuracy requires labels that cannot be produced without
  lookahead. The tradeoffs among these three are this branch's central question.
- Walk-forward design: anchored versus rolling origin; purging and embargo;
  combinatorial purged cross-validation and its variance properties.
  > **`CONVENTION` — new negative, found by corpus search 2026-08-21.** The
  > *length* of the purge and embargo has **no peer-reviewed methodological
  > source**. Its only corpus source is a practitioner catalogue (López de Prado
  > 2018, *Journal of Portfolio Management*). Any value used here is a labelled
  > convention with no empirical backing, in the same class as the Market Profile
  > 70% value area — and must be sensitivity-analysed rather than fixed.
- Stationary bootstrap (Politis & Romano 1994, *Journal of the American
  Statistical Association* — DOI pending verification) for confidence intervals
  under dependence, and block-length selection for it.
- Multiple testing over the parameter grid:
  [White 2000](https://doi.org/10.1111/1468-0262.00152) reality check,
  [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA, and the deflated
  Sharpe ratio (Bailey & Lopez de Prado 2014 — DOI pending verification). A
  five-parameter grid is thousands of comparisons and is registered as one family.
- Plateau analysis versus point optima. A parameter whose bootstrap interval
  spans the search grid was not selected.
- The point-in-time leakage canary as a standing pipeline test rather than a
  one-time check.

**Pipeline precondition** (not a falsification — relabelled per audit). It
implicates the harness, never the branch's premise, and it runs before any
selected parameter is reported. Its result is recorded whether it passes or fails.

*Graded form.* A single next-bar oracle detects leakage only when leakage is
severe enough for honest features to rival an oracle. The realistic failure — an
embargo one bar too short — leaves the oracle dominant and the canary silent.
Instead, shift the injected feature by *k* bars and report the *k* at which
dominance disappears. That *k* is the MDES of the canary itself.

*Necessary, not sufficient.* Non-dominance is ambiguous among three causes:
the pipeline leaks, the model class cannot exploit the feature, or the target is
too noisy for one oracle feature to dominate. The test cannot distinguish them
and does not claim to.

**Falsification** (branch-level). The branch presumes parameters are selectable
against out-of-sample predictive log-likelihood at all. Refuted if the selected
parameter's bootstrap interval spans the search grid across every candidate
objective — that is not a parameter selection, and branch 4 closes with the
state model reported as unidentified at this sample size.

## Cross-branch open questions

- Is regime a property of the market or of the observer's timescale? A state
  assignment that inverts under a change of bar size is describing the sampling
  scheme.
- Does any of this transfer outside markets? The same structure — latent state,
  causal-time constraint, no ground-truth labels, deseasonalization requirement
  — appears in epidemiological phase detection and in systems telemetry. Whether
  the methods transfer is an open question this project is positioned to ask.

## Verification status

Citations in this document are queued for verification against primary sources
by the `literature-check` branch declared in
[deliverable_spec_think-tank-charter_2026-08-21.md](../deliverables/deliverable_spec_think-tank-charter_2026-08-21.md).
Treat DOIs and volume/page numbers here as unconfirmed until that check returns.
