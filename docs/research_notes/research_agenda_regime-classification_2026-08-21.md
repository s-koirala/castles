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
an overnight session is a clock, not a classifier.

Three corrections to the first draft of this hazard (quant-auditor F-3-11):

1. **Leakage.** The time-of-day profile MUST be estimated on a strictly prior,
   disjoint window and never re-estimated using data at or after *t*. A
   full-sample profile is a full-sample statistic entering a feature required to
   be computable at *t*, violating charter commitment 4 directly, and every
   downstream causal-time claim inherits it. State the profile-estimation window
   with the split.
2. **Form.** Andersen & Bollerslev's periodicity is a **multiplicative** scale
   factor estimated by a flexible Fourier form on log absolute returns. The first
   draft specified **additive** mean subtraction, which does not remove
   multiplicative diurnal heteroskedasticity and leaves the U-shape substantially
   intact. It did not implement the method it cited.
3. **Scope.** Deseasonalization applies to scale- and intensity-valued features
   (volatility, volume, duration) — **not to price levels**. Subtracting a
   time-varying constant from price shifts the price axis within the session and
   destroys the absolute-price-anchored structure branch 1 exists to detect,
   round-number clustering above all. Branch 1 operates on raw price and handles
   diurnality by conditioning, not by transformation. The first draft's universal
   quantifier was unsatisfiable for branch 1.

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

> ### PARTIALLY UNBLOCKED 2026-08-21 — resolved by definition class
>
> The definitional survey
> ([lit_review_level-definitions_2026-08-21.md](../literature/lit_review_level-definitions_2026-08-21.md))
> found **76 distinct definitions** of "level" and partitioned them by an affine
> test that is programmatically checkable rather than a judgment call: a
> definition is independent of both confounds iff `L(a·p+b) = a·L(p)+b`.
>
> | Class | n | Surrogate admissibility |
> |---|---|---|
> | **N** — independent of both | **53 (70%)** | Random-relocation null **admissible as written** |
> | **T** — requires the tick/exchange grid | 12 (16%) | Admissible **only if relocation is constrained to the lattice**; off-lattice relocation makes surrogate levels *uncomputable*, not merely wrong |
> | **R** — requires round numbers | 7 (9%) | **No relocation or return-resampling null is admissible.** Relocating destroys roundness, so rejection is guaranteed and uninformative. The only identifying design located in the corpus is a redenomination natural experiment |
> | unclassified | 4 (5%) | No rule obtainable from any source |
>
> **The premise that blocked this branch — that "level" cannot be separated from
> round-number clustering and tick discreteness — is false for 53 of 76
> definitions.** The block is lifted for Class N, conditioned for Class T, and
> replaced by a *different and harder* block for Class R.
>
> **Consequence for every downstream artifact: a branch-1 claim must name its
> definition class.** A `construct-negative` verdict on Class N says nothing
> whatever about R or T. A failure_log row without a class is not localised.
>
> Three definitions are jointly R and T, and one separates the confounds
> empirically: a tenfold tick-size reduction on an FX platform left limit orders
> clustered at the **old** permitted prices — round-number behaviour surviving the
> removal of the grid that produced it. That is the natural experiment this branch
> needed and did not know existed.
>
> Eight Class-N definitions are **affine-defective**: scale- but not
> translation-equivariant, because their tolerance is a percentage *of price*. One
> is worse — its cluster-count selection compares a squared-price objective against
> an absolute constant, so it is not even scale-equivariant. Screen these out
> before any cross-instrument work: ES at ~7,700 and SI at ~30 are not comparable
> under a percentage tolerance.
>
> ### The statistic remains invalid regardless of class (quant-auditor F-3-1/F-3-3)
>
> **The statistic is invalid on this data.** The dip test's null is derived for
> i.i.d. sampling from a unimodal density. Price levels are integrated: over a
> fixed window the empirical distribution converges not to a density but to the
> occupation measure of the realized path (Brownian local time), which is
> generically multimodal. Demonstrated, not argued — Monte Carlo M=2000,
> α=0.05, seed 20260821, rejection rate of unimodality:
>
> | n | i.i.d. N(0,1) | AR(1) ρ=.9 | AR(1) ρ=.99 | random walk |
> |---|---|---|---|---|
> | 250 | 0.000 | 0.002 | 0.225 | **0.352** |
> | 1000 | 0.000 | 0.001 | 0.178 | **0.622** |
> | 5000 | 0.000 | 0.000 | 0.032 | **0.903** |
>
> The nominal critical value shrinks as n^-1/2 while the true one is flat in n, so
> the mis-calibration is **unbounded in n**: at n=5000 the ratio is 7.9x. Sampling
> more finely inside a fixed window buys spurious significance and zero
> information. The earlier note exempting the dip test from calibration concerns
> ("the dip test does not depend on it") was **wrong and is withdrawn**.
>
> Mirror-image defect: against a Gaussian unimodal alternative actual size is
> ~0.000 because the uniform is least-favourable. The test is simultaneously
> anticonservative on levels and near-powerless on interior-mode densities, which
> makes the positive control load-bearing rather than a formality.
>
> **The information unit is the number of independent sessions/excursions, not the
> number of ticks.** Step 2's MDES is computed on the session count.
>
> **Every return-resampling surrogate is also inadmissible**, on a ground beyond
> the IAAFT objection: the hypothesis is about *levels*, which are anchored in
> absolute price space, and every return-resampling scheme is invariant in
> distribution to the path's arbitrary starting location. No such surrogate can
> preserve round-number clustering — listed below as a property requiring
> preservation. IAAFT additionally preserves only *linear* dependence (destroying
> volatility clustering and jumps by construction) and requires stationarity, which
> an integrated series does not have.
>
> **Also unresolved and prior to all of the above:** "level" is never defined
> disjointly from round-number clustering and tick discreteness, so it cannot be
> decided whether those are construct or non-construct properties — which means no
> null-generating process can be specified at all until the construct is. Osler
> 2003 gives round-number clustering an order-book mechanism, which argues it is
> *part of* the construct rather than a nuisance.

- *Surrogate — REPLACED.* Use a **random-relocation null**: hold the observed path
  fixed and randomize the *locations* of the estimated levels within the observed
  price range. This preserves every property of the data exactly — all six listed
  below, and every unknown one — and breaks only the level-location
  correspondence, which is the construct. It is the spatial-statistics
  random-shift design, and it is the only null in this class that gate condition
  (i) can actually satisfy. The endpoint becomes out-of-sample: does a level
  estimated on [0,t] predict behaviour on (t, t+h]?
  The alternative is a model-based null fitted under an explicit no-level
  restriction (tick-grid jump-diffusion with an Andersen–Bollerslev intraday
  volatility factor), per the Brock, Lakonishok & LeBaron 1992 design
  ([doi:10.1111/j.1540-6261.1992.tb04681.x](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)),
  which is already in the corpus. If a block bootstrap is used anywhere else,
  block length by Politis & White (2004) **as corrected by Patton, Politis & White
  (2009)** ([doi:10.1080/07474930802459016](https://doi.org/10.1080/07474930802459016))
  — the corpus carries the annotation "the uncorrected formula is wrong" and the
  first draft of this agenda stripped it.
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

  **The dip statistic and the excess-mass statistic coincide up to a known
  constant for the k=1 vs k=2 null.** Registering both as family members misstates
  the effective dimension and invites the appearance of two-of-three agreement
  where one statistic is reported twice. Pick one; use excess mass only if k>2 is
  genuinely being tested, where the count-vs-location separation it offers is
  real. The dip test's own calibration paper — Cheng & Hall 1998,
  [doi:10.1111/1467-9868.00141](https://doi.org/10.1111/1467-9868.00141) — is
  **absent from the corpus**, the identical structural gap already flagged for
  Silverman. It addresses the i.i.d. case only and does not repair the defect
  above.
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
against out-of-sample predictive log-likelihood at all.

> **Instrument corrected (F-3-10).** The first draft refuted on "the selected
> parameter's bootstrap interval spans the search grid". The selected parameter is
> an **argmax** — a non-smooth functional — and the n-out-of-n bootstrap is
> *inconsistent* for argmax-type estimators (cube-root asymptotics, Kim & Pollard
> 1990). The interval whose width was the entire refutation criterion has no
> established coverage. Replaced by the **Model Confidence Set** (Hansen, Lunde &
> Nason 2011, [doi:10.3982/ECTA5771](https://doi.org/10.3982/ECTA5771)) — already
> in this project's corpus, annotated there as "the right object when the goal is
> state-model selection rather than a single winner", and unused until now.

Refuted if the **Model Confidence Set** spans the search grid across every
candidate objective — that is not a parameter selection, and branch 4 closes with the
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
