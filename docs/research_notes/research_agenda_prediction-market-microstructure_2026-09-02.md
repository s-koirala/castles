---
type: research_agenda
slug: prediction-market-microstructure
branch: kalshi-arbitrage / prediction-market microstructure
date: 2026-09-02
status: open
revision: 1
revision_note: >
  Rev 1 (2026-09-02) opens the branch agenda declared by
  deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C item 6.
  Written under audit finding SCOPE-2-3, which recorded that the spec-declared
  agenda did not exist anywhere in the repository although the corpus record's
  section 10 gaps (G-1…G-10) and section 11 TO COMPUTE handoffs (TC-1…TC-5) had
  been written as its input. Every branch below is derived from a named gap or
  handoff; nothing here is derived from model recall.
corpus: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md  # 149 records; compiled corpus record, NOT a systematic review
protocol: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md  # frozen prefix sha256 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4 (first 82,677 bytes); with addendum A1-A15 sha256 21a77d10841ba7f15ea58d5a58a1bca57818b2ed1a0f3bf53a1dbce6a8dcc53b
bibliography: docs/literature/references_kalshi-arbitrage.json  # sha256 fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164
governing_decisions:
  - docs/decisions/ADR-0003-specification-not-execution.md   # castles specifies; it does not execute
  - docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md  # rules/quant-project.md + REVIEW.md adopted for this branch only
scope_boundary: >
  This document SPECIFIES tests. It runs none of them. No branch below acquires
  Kalshi market data, calls an exchange API, fits a model, backtests, or states a
  tradeable rule (ADR-0003, ADR-0004 §Boundary). Every parameter that an executing
  project would have to choose is left `TO COMPUTE` with the selection procedure
  named, never a bare number (CLAUDE.md §Parameter & Prompt Selection).
---

# Research agenda — prediction-market microstructure (Kalshi branch)

**Question.** For a regulated binary event-contract venue, which of the
no-arbitrage/coherence conditions, systematic mispricings, and market-making
results established on *other* venues and for *unbounded* payoffs actually transfer
— and under which stated, checkable preconditions?

## How to read this document

Each branch states: the **gap or handoff it comes from**, the **claim at issue**,
one **falsification test** (H0, statistic, comparison/surrogate, refutation
condition, unit of analysis), the **evidence tier** the branch currently stands on,
and its **preconditions**. A branch is *complete* when its test is fully specified,
not when it has been run (ADR-0003 §Consequences).

**What counts as a falsification test here, stated because the 2026-08-21 agendas
got this wrong and the spec names the defect explicitly.** A falsification test
must be a statement about the *world* that the branch's own claim forbids, with a
statistic and a refutation condition attached. **These do not count and are not
written as tests below:** a *design-resolution study* (choosing between two
implementations), a *precondition* (retrieving a document the test needs), and an
*adoption policy* (deciding to use a convention). Where a branch needs one of
those, it is listed under **Preconditions**, never under **Falsification test**.
Branch 0 is a retrieval task and is therefore stated as a precondition branch with
**no** falsification test, and says so.

**Branch count, stated so the spec check is unambiguous.** **Six numbered research
branches, 1 through 6, each carrying exactly one falsification test**, plus **one
precondition branch, Branch 0, carrying none by design**. Branch 0 is numbered
because four other branches are blocked on it and a reader needs a name for the
blocker; it is not counted as a research branch and no test is claimed for it.

**Evidence tiers** are CLAUDE.md's: T1 peer-reviewed, T2 official documentation,
T3 professional standard, T4 vetted technical forum, T5 other. A branch's tier is
the tier of the *weakest* record its motivating claim rests on.

## Standing hazards — read before any branch

**H-1. The corpus behind this agenda is a compiled corpus record, not a review.**
98.3% of its 8,813 dispositions are keyword-classifier outputs; 150 records carry a
read-based verdict; **no full text was read for any of the 149 included records**;
33 of the 149 are metadata-depth only. Gap **G-10**. Consequence for this agenda:
**an absence in the corpus is not evidence of absence in the literature**, and no
branch below may take "the corpus contains no record that does X" as a finding. Where
a branch rests on such an absence it is marked **absence-of-evidence** and its first
precondition is a targeted retrieval.

**H-2. 1,245 records ended screening unresolved and they are concentrated in this
agenda's largest strand.** 700 X11 records are transfer-clause model records —
exactly the class branches 2 and 3 are about — and 545 X10 records are candidate
records whose eligibility was never assessed. Gap **G-5**. Any branch that claims
novelty must first check its claim against those strata, which are in
`ka-screening-verdicts.jsonl` and *not* in the corpus.

**H-3. The venue's own mechanics are unretrieved.** The filer-published rulebook
returned HTTP 429 on nine attempts (AG-1) and 17 CFR 40.11 returned an access
interstitial (AG-2). Six transfers in the corpus are marked
`not-transferable-as-stated` for want of facts in those documents (G-3). **Branch 0
is a hard precondition for branches 1, 3, 4 and 5**, and a branch that proceeds
without it is discharging a carrying assumption against a fact nobody has.

**H-4. Venue mechanism is not established, in either direction.** The corpus can
say neither that the venue is order-driven nor that it is quote-driven (S7-5, G-3
mark 6). No branch may assume either. Where a test's design depends on the answer,
both arms are specified.

**H-5. The Kalshi evidence base is thin and not independent.** 17 of 19
Kalshi-specific records are T5; exactly one peer-reviewed record contributes a
stated finding; 7 of 19 come from two author groups; 15 of 19 are SSRN DOIs sitting
on top of an arm that was never run (G-6, G-9). **No branch may treat the Kalshi
block as a replicated literature.**

---

## Branch 0 — Venue mechanics as a dated document set (precondition branch)

**From:** G-3, TC-1, AG-1, AG-2. **Tier of the motivating evidence:** T2 (official
documentation), currently *unretrieved*.

**What is needed.** The filer-published rulebook plus the CFTC filing record, as a
**dated document set**, yielding: fee schedule; tick size; settlement source and
settlement rule per contract family; position limits; membership and market-maker
programme terms; permitted pre-settlement position transformations; and **the
trading mechanism** (order-driven book vs quote-driven dealer vs hybrid).

**No falsification test is stated for this branch, and that is deliberate.** It is a
retrieval task, not a claim about the world. Writing a "test" here would be exactly
the design-resolution-mislabelled-as-test defect this agenda is written against.

**Refutation condition for the branch's *own* premise, which is testable:** the
branch assumes the documents exist and are publicly reachable. If a session with a
working route to the filer's document establishes that the rulebook is not
publicly published, the premise is refuted and G-3's six marks become permanent
rather than pending.

**Preconditions.** A retrieval route that survives the venue's rate limiting; a
dated snapshot with its retrieval log, per this project's provenance rule.

**Blocks:** branches 1, 3, 4, 5.

---

## Branch 1 — Does the coherence condition bind on a live binary event book?

**From:** G-1, and the S1 strand of the corpus. **Tier:** T1 (the coherence
condition is stated in peer-reviewed sources in the corpus); the venue-side premise
is T2-*unretrieved*.

**Claim at issue.** That for a set of mutually exclusive and exhaustive contracts on
one event, quoted prices imply probabilities summing to one up to a bound set by the
fee, spread and collateral structure — and that observed violations are therefore
informative about frictions rather than about mispricing.

**Falsification test.**
- **Unit of analysis:** one (event, timestamp) pair over a mutually exclusive and
  exhaustive contract family.
- **H0:** the distribution of the coherence residual — the signed excess of the
  summed best-executable implied probabilities over one — is centred at the value
  predicted by the venue's own fee and spread structure (Branch 0 output), against
  the alternative that it is displaced from it.
- **Statistic:** the location of the residual distribution, estimated with a
  HAC-consistent standard error; bandwidth by the
  [Newey & West 1994](https://doi.org/10.2307/2297912) data-dependent rule or the
  [Andrews 1991](https://doi.org/10.2307/2938229) plug-in, **selection rule named,
  value `TO COMPUTE`**. Serial dependence within an event is the reason a HAC
  estimator rather than an i.i.d. one is specified.
- **Comparison:** the *predicted* residual location computed from Branch 0's fee and
  tick schedule, not zero. A test against zero would reject on the fee alone and
  would be uninformative, which is the failure mode this specification exists to
  avoid.
- **Refutation condition:** the branch's claim is refuted if the residual location
  is statistically distinguishable from the friction-predicted value **and** the
  displacement does not shrink as the executable-depth constraint is tightened. If
  it shrinks with depth, the residual is a liquidity artefact and the claim
  survives.
- **Multiplicity:** the test is run over many contract families. This is an
  **existence** claim ("there exist families where coherence fails beyond
  frictions"), so it needs family-wise control —
  [White 2000](https://doi.org/10.1111/1468-0262.00152) reality check or
  [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA. Family definition
  and α `TO COMPUTE`.

**Preconditions.** Branch 0 (fee, tick, collateral); a book snapshot at executable
depth, which is out of scope here (ADR-0003) and belongs to an executing project.

**Absence-of-evidence flag.** The corpus contains no record that nets a measured
event-exchange discrepancy against a fully specified friction set on an order book
(G-1). Under H-1 that is not evidence that none exists; a targeted retrieval
against the 545 X10 and 700 X11 strata is the first step.

---

## Branch 2 — Do inventory-risk market makers survive the bounded-payoff restriction?

**From:** G-5, TC-4, and the corpus's S4 strand. **Tier:** T1 for the lineage; the
transfer itself is **asserted by transfer, not by the lineage** — four of five
named-lineage anchors are at metadata depth and the one whose model is stated
assumes a Brownian reference price, which is explicitly excluded for a probability
bounded in [0,1]
([Guéant, Lehalle & Fernandez-Tapia 2012](https://doi.org/10.1007/s11579-012-0087-0)).

**Claim at issue.** That the inventory-control lineage's central qualitative
prediction — a maker's reservation price moves monotonically against accumulated
inventory — holds when the underlying is a probability bounded in [0,1] and settling
at an endpoint, rather than an unbounded diffusion.

**Falsification test.**
- **Unit of analysis:** the model, not the market. This is a **derivation** test and
  it is specifiable without any data, which is why it sits before branch 3.
- **H0:** for each named-lineage model, the monotone inventory-reservation-price
  result is derivable when the reference-price process is replaced by a process with
  support in [0,1] and an absorbing endpoint at settlement, with all other
  assumptions unchanged.
- **Statistic / procedure:** re-derive each model's first-order condition under the
  substituted process and record, per model, one of `holds`, `holds under an added
  condition C` (with C stated), or `fails`.
- **Refutation condition:** the branch's claim — that the lineage transfers — is
  refuted for any model whose result requires unbounded support, and the refutation
  is **per model**, not per lineage. A single failure does not refute the lineage; a
  failure in the model a downstream stage intends to fit refutes the transfer *for
  that stage*.
- **Independent check the corpus already supplies:** the corpus records an
  **unresolved internal disagreement** on the sign of this very effect — the lineage
  predicts a negative inventory-to-reservation-price relation, while futures
  transaction data show a positive one as a strong and consistent regularity
  ([Manaster & Mann 1996](https://doi.org/10.1093/rfs/9.3.953)). A derivation that
  reproduces the negative sign without addressing that evidence has not completed
  the test.

**Preconditions.** None from Branch 0 — this branch is venue-independent by
construction, which is why it is the one branch that can proceed while AG-1 stands.
Full texts of the five named-lineage anchors, which the corpus does **not** have
(AG-5): four are at metadata depth. **Retrieving them is the branch's first task and
is a precondition, not a test.**

---

## Branch 3 — Is the favourite-longshot bias present on the venue, and is it the same object?

**From:** G-3 marks 3 and 4, G-4, G-6, and the S3 strand. **Tier:** T1 for the FLB
literature; **T5** for every Kalshi-specific record that would motivate expecting it
here, and one author group supplies five of them (H-5).

**Claim at issue.** That the favourite-longshot bias measured on sportsbooks,
racetracks and parimutuel pools is the same phenomenon as any price-probability
curvature observed on a regulated event-contract exchange — and therefore that its
explanations transfer.

**Falsification test.**
- **Unit of analysis:** the (contract, resolution) pair, binned by quoted implied
  probability.
- **H0:** the calibration curve of quoted implied probability against realised
  frequency is flat in the deviation sense — the deviation from the 45° line does
  not vary monotonically with the quoted probability — against the alternative that
  it is monotone in the direction the sportsbook literature reports.
- **Statistic:** a monotone-trend statistic on the binned deviations with a
  distribution-free null (permutation of the resolution labels within event date),
  and a bootstrap CI on the deviation at each bin. Bin edges `TO COMPUTE` by a
  stated rule — equal-count bins with count chosen by cross-validation of the
  calibration estimator, **not** a round number.
- **Comparison:** the *same* estimator applied to a bookmaker or parimutuel dataset
  from the corpus's own T1 sources, so that a difference in the estimator's
  behaviour cannot be confused with a difference in the venue.
- **Refutation condition, and this is the branch's substantive content:** the "same
  object" claim is refuted if the venue curve and the comparison-venue curve differ
  in **sign or monotonicity direction**, not merely in magnitude. A magnitude
  difference is consistent with the same phenomenon under different frictions; a
  sign difference is not.
- **Mechanism confound that must be handled, not assumed away (H-4).** Every leading
  explanation in the corpus is mechanism-dependent — bookmaker price setting under
  information asymmetry, insider-driven odds movement, risk-love preferences. If
  Branch 0 shows the venue is order-driven, the bookmaker-conduct explanations are
  **not** available and the test is a test of the preference-side explanations only;
  if quote-driven, both classes are live. The branch specification is therefore
  **two-armed** and the arm is selected by Branch 0's output, never assumed.

**Preconditions.** Branch 0 (mechanism, settlement rule); resolution outcomes;
composition control across the 2025 asset-class boundary (TC-5) — a re-estimate that
pools across a composition break measures the break.

**Absence-of-evidence flag.** G-4: no abstract this corpus read states a
market-making model fitted to this venue. Bounded to the 116 abstract-depth records.

---

## Branch 4 — Is a stated cross-venue discrepancy executable after the full friction set?

**From:** G-2, TC-3, the S2 and S5 strands. **Tier:** T1 for the cross-venue
arbitrage literature; **the friction side is unevidenced** — G-2 records that no
retrieved abstract among the 116 read at abstract depth states a measurement or a
model of the cost of capital locked in an event-contract position until settlement.

**Claim at issue.** That a price discrepancy between two venues on the same event
constitutes an arbitrage opportunity once fees, spread, collateral and capital
lockup to settlement are netted.

**Falsification test.**
- **Unit of analysis:** the (event, venue-pair, timestamp) triple.
- **H0:** the net-of-friction discrepancy, computed at **executable** depth on both
  legs and charged the full lockup cost to settlement, has a distribution whose
  upper tail is not distinguishable from what the friction model alone generates.
- **Statistic:** the frequency and size of net-positive discrepancies, with a
  bootstrap CI; the surrogate is the **same computation with the two legs' event
  identities permuted**, which preserves each venue's marginal price process and
  friction structure while destroying the same-event correspondence that an
  arbitrage requires. A returns-resampling surrogate is **not** admissible here: it
  destroys the settlement-endpoint structure the claim depends on.
- **Refutation condition:** the claim is refuted if the net-of-friction upper tail
  is indistinguishable from the permuted surrogate. It is *not* refuted by a small
  effect; it is refuted by an effect that the surrogate reproduces.
- **Capital lockup is the parameter that decides this test and it has no source.**
  It is `TO COMPUTE` as a function of contract duration against a funding-cost
  series (TC-3), and until it is computed the test **cannot be run** and no
  executability claim may be stated. This is the branch's binding constraint and it
  is stated here rather than discovered later.

**Preconditions.** Branch 0 (fees, collateral, settlement); a funding-cost series;
synchronised quotes at executable depth on both venues — all out of scope here.

---

## Branch 5 — Does the protocol-executable / payoff-space distinction have a venue counterpart?

**From:** TC-2, TC-1, G-3 mark 1. **Tier:** T5 (the distinction is stated in a
preprint the corpus carries at abstract depth,
[Gebele, Mutzel & Matthes 2026](https://arxiv.org/abs/2608.00666)); the venue side
is T2-*unretrieved*.

**Claim at issue.** That an arbitrage which exists in payoff space is realisable
only if the venue's rules permit the specific pre-settlement position
transformations the strategy requires — so that "arbitrage exists" and "arbitrage is
executable" are different claims with different evidence.

**Falsification test.**
- **Unit of analysis:** the (payoff-space arbitrage, venue rule set) pair.
- **H0:** the set of payoff-space arbitrages on this venue's contract families is
  **equal** to the set realisable under the venue's stated pre-settlement
  transformation rules, against the alternative that the realisable set is a proper
  subset.
- **Statistic:** the cardinality ratio realisable / payoff-space, enumerated over a
  stated contract-family census rather than sampled.
- **Refutation condition:** H0 is refuted by the exhibition of **one** payoff-space
  arbitrage that the rule set forbids. This is a single-counterexample test and
  needs no multiplicity control — which is why it is worth stating separately from
  branch 1 rather than folding into it.
- **Symmetry the branch must not lose:** the converse is also informative. A
  transformation the rules permit that creates a realisable position with no
  payoff-space counterpart would refute the *framing*, not just H0.

**Preconditions.** Branch 0 (permitted transformations — TC-1); the contract-family
census. Marked `not-transferable-as-stated` in the corpus until Branch 0 returns.

---

## Branch 6 — Are the corpus's own unresolved strata hiding the answer?

**From:** G-5, G-7, G-10, H-1, H-2. **Tier:** n/a — this is a branch about the
corpus, and it is the only branch whose object is the evidence base rather than the
market.

**Claim at issue.** That the corpus's declared gaps are gaps in the *literature*
rather than gaps in this *search*.

**Falsification test.**
- **Unit of analysis:** the gap statement.
- **H0:** for each of G-1, G-2, G-4 and G-5, no record in the 700 X11 stratum, the
  545 X10 stratum or the 3,090 title-only DEFAULT-X1 stratum states the thing the
  gap says is absent.
- **Statistic:** a targeted screen of those strata, read rather than classified,
  against the gap's own predicate. The strata are enumerated in
  `ka-screening-verdicts.jsonl`, so the sampling frame is fixed and published.
- **Refutation condition:** H0 is refuted for a gap by **one** record in those
  strata that states what the gap says is absent. Each such record also converts a
  corpus-record gap statement into a corpus-record error, which goes to
  [failure_log.md](../../failure_log.md) under the charter's null protocol.
- **Why this is a genuine test and not a chore:** the corpus itself declares its
  absences bounded to what it read (G-2, G-4, "Qualified under finding REV-1-10"),
  so the branch has a real chance of failing, and failing would change what
  branches 1, 2 and 4 may claim as novel.
- **Precondition, not part of the test:** the backward citation-chasing arm never
  ran (G-7, amendment A6) because it needs full texts. Running it is a retrieval
  task and belongs under preconditions.

**Minimum detectable effect, not retrospective power** (charter). Before screening,
state the smallest number of hits in the stratum that would be treated as refuting
each gap. That number is `TO COMPUTE` from the stratum size and the screening
budget; it must be fixed **before** the screen, or the test is unfalsifiable.

---

## Cross-branch open questions

- **Is "the venue" a single object across time?** The 2025 asset-class boundary
  (TC-5) means a statistic estimated across it may be measuring a composition
  change. Every branch that pools across it inherits this.
- **Does the bounded-payoff restriction change the *question* or only the model?**
  Branch 2 tests whether the lineage's results survive. It does not ask whether the
  right maker for a [0,1] payoff belongs to that lineage at all — the corpus's
  market-scoring-rule and cost-function families are written natively for bounded
  payoffs and may make the transfer question moot rather than answer it.
- **What does this branch owe the other threads?** The coherence-residual statistic
  in branch 1 and the calibration-deviation statistic in branch 3 are both
  time-indexed and both would inherit `rules/quant-project.md` directives 1-7 at
  their first empirical stage (ADR-0004). Any successor specification that could not
  satisfy no-look-ahead and time-ordered splits is defective **at the point of
  writing**, even though nothing here will run it.

## Verification status

**Every substantive citation in this document is drawn from the compiled corpus
record named in the frontmatter and carries the identifier that record carries.**
Nothing here was written from model recall.

**Four methodology citations are NOT corpus records and are marked as such.** They
are the inference conventions adopted for this branch by
[ADR-0004](../decisions/ADR-0004-quant-rule-adoption-prediction-markets.md) from
`rules/quant-project.md`, and they bind the branch's first empirical stage wherever
it occurs. Each was verified against Crossref on 2026-09-02 (author, year,
container) and each resolves at the DOI Handle System with `responseCode` 1:
Newey & West 1994, *Automatic Lag Selection in Covariance Matrix Estimation*,
*Review of Economic Studies* (`10.2307/2297912`); Andrews 1991, *Heteroskedasticity
and Autocorrelation Consistent Covariance Matrix Estimation*, *Econometrica*
(`10.2307/2938229`); White 2000, *A Reality Check for Data Snooping*, *Econometrica*
(`10.1111/1468-0262.00152`); Hansen 2005, *A Test for Superior Predictive Ability*,
*JBES* (`10.1198/073500105000000063`). They are cited for their **procedure**, not
for a result, and no operating characteristic is quoted from any of them.

**What that inherits, stated because it bounds every branch above.** The corpus is a
compiled corpus record, not a systematic review: 98.3% of its dispositions are
keyword-classifier outputs, no full text was read for any included record, 33 of 149
included records are metadata-depth only, and 1,245 records ended screening
unresolved. The corpus's own gate returns `block` on 83 G16 identifier findings, 81
dispositioned as the standing publisher-403 class and two dispositioned
individually; the DOI Handle System resolves 149 of 149. **A branch that needs a
claim to be true, rather than to be *stated by a retrieved record*, must retrieve
the full text itself.**

**Round-2 corrections inherited from the corpus record**, all dated 2026-09-02, all
material to what this agenda may assert:

- **No demonstrated vocabulary gap** is claimed for any known-item miss. The corpus
  briefly asserted that `dealer` and `limit order` appear in none of its topical
  queries and that KI-20 and KI-21 were therefore demonstrated vocabulary gaps.
  `limit order` **is** carried, by `ka-crossref-07`. The cause of the four genuine
  misses is undetermined between vocabulary and the retrieval cap. **Consequence for
  this agenda:** a successor must not "fix" the search by adding vocabulary
  `ka-crossref-07` already carries; the live constraint for KI-21 is the `rows=20`
  cap against a platform-reported 79,887.
- **The arXiv `cat:q-fin*` narrowing is offset in weakened form, not unoffset.**
  Three of the four offsetting queries executed and returned records; one returned
  zero (G-8).
- **15, not 13, of the 19 Kalshi-specific records are SSRN DOIs** (G-9), so H-5 is
  worse than the corpus first reported.
- **Six transfers, not five, are `not-transferable-as-stated`** for want of the
  venue's mechanism (G-3), which is why Branch 0 is a precondition for four of the
  six branches rather than three.
