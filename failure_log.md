# Failure log

Append-only register of nulls, non-replications, and negative results.
Governed by the negative-result protocol in
[docs/methodology/charter_castles_2026-08-21.md](docs/methodology/charter_castles_2026-08-21.md).
Referenced by [hypothesis_backlog.md](hypothesis_backlog.md) under `archived`.

Nothing is deleted from this file. A null later overturned gains a
`superseded_by` note; its row stays.

**Layer definitions live in the charter, not here** — §"Localize the failure".
Duplicating them created two sources of truth against a living document.

**Revision 2 (2026-08-21).** Rev 1 was audited before any row was acted on.
Three of four rows carried layer assignments that did not follow from what their
sources could establish, and four of four reported a transferable positive with
no row reporting absence — which made the project's distinctive column
uninformative on its first use. Rev 2 re-localizes F001, F003, and F004,
records two "none found" transfers, adds the evidence tier, and records that
protocol steps 1–2 were **not executed** for any row. The original assignments
are shown struck rather than deleted.

**Revision 3 (2026-09-04).** Appends four rows — **F006, F007, F008, F009** —
registered from the 2026-09-04 multivocal corpus record
[lit_review_kalshi-strategy-multivocal_2026-09-04.md](docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md)
§10. Nothing above this line is altered, reworded, or withdrawn. Three things
about the new rows, stated here because the rev-2 header's defect is exactly the
one a reader will look for:

- **Protocol steps 1–2 were NOT executed for any of F006–F009 either**, and each
  row says so in the charter's own words rather than leaving it to be discovered.
  The rev-2 header's blanket sentence is therefore still true of every row in the
  file, and rev 3 does not repeat it silently.
- **Two of the four rows register nulls REPORTED BY SOURCES, not nulls this
  project established** (F008, F009). Each says which, records the source's
  outcome verbatim and attributed, and adopts nothing.
- **One row is `undetermined` because the observation was never made** (F007), and
  the charter's rule — a layer with no discriminating observation is
  `undetermined`, not a guess — is the whole reason it is filed that way. A
  capacity gap is not an absence.

## Schema

Each row records: the precise null, the source and its evidence tier, the
localization layer **with the alternatives considered and the discriminating
observation**, the transferable positive **or "none found"**, verification
status, and a pointer to the full autopsy. A layer with no discriminating
observation is `undetermined`, not a guess.

**Steps 1–2 not executed for any row below.** No row states an alpha, an n, a
target power, or an MDES. Until an autopsy supplies them, every layer here is
provisional by the charter's own standard.

---

## F001 — Pretrained TSFMs vs. random walk on equity return forecasting

- **Result as reported:** across five liquid US equities, a one-sided
  Diebold–Mariano test rejects equal-or-inferior predictive accuracy for only
  two of ten model–asset task comparisons.
- **Source:** Noguer i Alonso & Pereira Franklin,
  [arXiv 2606.27100](https://arxiv.org/abs/2606.27100). **Tier: `preprint`**
  (unrefereed). Load-bearing, so the tier matters.
- **Layer:** `undetermined` — ~~`question`~~ (Rev 1, withdrawn).
  - *Alternatives considered:* `precision` (SNR too low relative to n),
    `construct` (no predictable conditional mean at this horizon — the
    efficient-markets reading), `method` (restricted univariate conditioning
    set), `question` (non-identification).
  - *Why `question` was wrong:* E[r_{t+1} | history] is a well-defined
    functional of the joint distribution and **is** identified by an infinite
    sample. The source establishes that it is approximately zero or
    noise-swamped — a statement about magnitude and signal-to-noise, not
    identifiability. Conflating "not predictable from a restricted information
    set" with "not identified" was a category error.
  - *Discriminating observation:* an irreducible-error or oracle-bound estimate
    for the target at this horizon. **Not available from the source**; obtainable
    only by re-analysis with a stronger conditioning set.
  - *Step 2b (source validity) - SUSPECTED DEFECT, unconfirmed.* A random walk IS
    nested in a forecasting model that includes it as a coefficient restriction.
    Under nesting the population loss differential is identically zero and its
    long-run variance degenerates, so DM is not asymptotically standard normal - and
    the direction is signable and adverse to the source's conclusion: the larger
    model's MSPE is inflated by estimation noise even when the extra parameters have
    zero population value, so a one-sided DM test against normal critical values is
    severely **undersized**. "2 of 10 rejections" is exactly the output a
    correctly-functioning-but-mis-sized nested DM test produces even when the models
    carry genuine predictive content. If plain DM was used, the source's null is not
    weak - it is **uninformative, because the statistic was biased toward the null by
    construction**.
  - *Three discriminating observations, ALL obtainable from the source without
    re-analysis* (this is the cheapest available action on the project's
    highest-priority row):
    1. Which statistic was used - plain DM, Clark-West-adjusted, or
       Clark-McCracken bootstrap?
    2. Zero-shot evaluation, or fine-tuned on the evaluation assets?
    3. Expanding-recursive or fixed-rolling forecast origin?
    Item 1 determines whether the defect is present; items 2-3 determine whether the
    nesting degeneracy binds at all. Strictly zero-shot with no fitting, or a fixed
    finite rolling window, means the differential need not be degenerate and
    Giacomini-White conditional predictive-ability inference is valid for nested
    models.
  - *Corpus gap, four records, on the most load-bearing row in the project:*
    Clark & West 2006 ([doi:10.1016/j.jeconom.2005.07.014](https://doi.org/10.1016/j.jeconom.2005.07.014)),
    Clark & West 2007 ([doi:10.1016/j.jeconom.2006.05.023](https://doi.org/10.1016/j.jeconom.2006.05.023)),
    Clark & McCracken 2001 ([doi:10.1016/S0304-4076(01)00071-9](https://doi.org/10.1016/S0304-4076(01)00071-9)),
    Giacomini & White 2006 ([doi:10.1111/j.1468-0262.2006.00718.x](https://doi.org/10.1111/j.1468-0262.2006.00718.x)).
    None is in the corpus.
  - *Unresolved:* the source's DM count, alpha, and multiplicity family are
    unrecorded, and DM applied to a nested comparison (a random walk is nested
    in a forecasting model) is degenerate — whether a Clark–West-type correction
    was used is load-bearing and unknown.
- **Transferable positive:** **none found.** ~~"volatility remains a live
  target"~~ (Rev 1, withdrawn) — four independent grounds: (a) "not tested" was
  upgraded to "not implicated"; (b) if the deficit is component-level, which is
  exactly what F002 asserts, the defect is shared by mean and variance heads, so
  **F001's Rev-1 transfer contradicted F002's premise**; (c) the mean comparator
  was a random walk, the variance comparator would be HAR-RV — losing to the
  weak baseline makes beating the strong one less likely a priori, not neutral;
  (d) "volatility is forecastable" is settled, not live.
- **Verified:** CONFIRMED verbatim by literature-check — model list, asset list,
  8-of-10 task-level wins, and the DM sentence all match the source.
- **Status — ELEVATED 2026-08-21.** The author has designated this source a
  **foundational paper** for the project. That raises rather than lowers the bar
  on the three discriminating observations above, and the direction of the risk
  is the one that matters:
  - The paper's finding is **negative** (TSFMs fail to beat a random walk).
  - The suspected nested-DM defect biases a test **toward finding nothing**.
  - So a defect here means the paper **understates** TSFM performance, and a
    foundation built on it would rest on a result weaker than it appears, in the
    direction that undermines it.
  - **The conclusion it is being used to support is over-determined and survives
    regardless**: F002 (ablations, the strongest row here), F003, and F004 reach a
    compatible position by independent routes and do not share this defect. What
    is at stake is whether *this paper specifically* can carry foundational
    weight — a narrower question than whether the position is sound.
  - Resolving the three observations is therefore a **prerequisite for citing it
    as foundational**, not an optional tidy-up.
- **Scope note.** Per [ADR-0003](docs/decisions/ADR-0003-specification-not-execution.md),
  the paper's conditions (daily US equities, five names) are not the conditions
  this project is interested in (5-minute ES/NQ/GC/SI). Transporting a null across
  that gap is itself a claim requiring justification, and the transport direction
  is unfavourable: intraday futures have higher sampling frequency, different
  microstructure, and a different signal-to-noise profile than daily equities.
  Record the transport assumption explicitly wherever this row is cited.
- **Autopsy:** not yet written. Highest priority of the four, now with a stated
  prerequisite role.

## F002 — Removing the LLM component from LLM-based time-series forecasters

- **Result as reported:** ablations replacing the language model with a single
  randomly-initialized attention layer or transformer block outperform the full
  method in 26/26 (Time-LLM), 22/26 (LLaTA, renamed CALF in v2), and 19/26
  (OneFitsAll) cases.
- **Source:** Tan et al., [arXiv 2406.16964](https://arxiv.org/abs/2406.16964).
  **Tier: `accepted-preprint`** — NeurIPS 2024 Spotlight.
- **Layer:** `method`. **Settled, not provisional.**
  - *Alternatives considered:* `implementation`, `data`, `estimand`.
  - *Why `method` holds:* an ablation is the one design that licenses
    component-level attribution. The discriminating observation is internal to
    the design and was obtained.
- **Transferable positive:** the gains were **not attributable to the LLM
  component**. Note the correction: an ablation shows the removed component is
  not *necessary*; it does not show the remainder is *sufficient*, nor that
  gains are attributable to the remainder — both may be beating a weak baseline.
  Rev 1 overstated this as positive attribution to the surrounding architecture.
- **Verified:** CONFIRMED. Counts exact. Cite v2's framing (13 datasets × 2
  metrics = 26); v1's "8 datasets" is internally inconsistent.
- **Autopsy:** not yet written. This row is the model the other three are held
  against.

## F003 — Human–AI combinations vs. the better component alone

- **Result as reported:** across 106 experimental studies and 370 effect sizes,
  human–AI combinations performed significantly worse on average than the best
  of human-alone or AI-alone; losses in decision tasks, gains in content
  creation.
- **Source:** Vaccaro, Almaatouq & Malone 2024,
  [*Nature Human Behaviour* 8:2293–2303](https://doi.org/10.1038/s41562-024-02024-1).
  **Tier: `peer-reviewed`** — the only row at the top tier.
- **Layer:** `estimand` — ~~`method`~~ (Rev 1, withdrawn).
  - *Why `method` was wrong:* a meta-analytic average over a heterogeneous
    population of combination designs and tasks does not establish that any
    particular combination method was wrong. It establishes that a **marginal
    average across a heterogeneous population** is negative. The row's own next
    column said so — the effect is moderated — while the layer said otherwise.
  - *Discriminating observation:* the moderator analysis, which is available
    from the source and points to `estimand`.
- **Transferable positive:** a **pre-specified-or-exploratory moderator
  consistent with, but not established by, a between-study contrast**: the
  combination effect is positive where humans outperformed AI alone. This does
  **not** license a within-design intervention rule. Rev 1's "gives a design
  rule" read a study-level observational contrast causally — it is confounded by
  task type, domain, and whatever determined AI strength in the same studies.
  Whether the moderator was pre-specified in the preregistration is decisive and
  is **not yet recorded**.
- **Verified:** CONFIRMED, all sub-facts, against the journal version. Cite the
  journal, not the arXiv preprint — the preprint says only "over 100 studies /
  over 300 effect sizes".
- **Autopsy:** not yet written.

## F004 — Deep learning vs. traditional strategies on financial time series

- **Result as reported:** verbatim, "modern deep learning techniques do not
  universally outperform traditional quantitative strategies or tree-based
  models."
- **Source:** FinTSB, [arXiv 2502.18834](https://arxiv.org/abs/2502.18834);
  also in ICAIF proceedings — cite the proceedings version.
  **Tier: `preprint`** for the arXiv record.
- **Layer:** `no-stated-test` → `undetermined` — ~~`data`~~ (Rev 1, withdrawn).
  - *Why `data` was wrong:* a benchmark comparison of models on fixed data
    produces the identical observation whether the cause is low SNR or limited
    model capacity. Attributing to `data` requires an irreducible-error or
    oracle-bound estimate, which a leaderboard does not provide. Rev 1's
    parenthetical asserted a discriminating conclusion with no discriminating
    test.
  - *This row is a leaderboard with no hypothesis test*, so under charter step 1
    it does not qualify as a null at all until a test is reconstructed from the
    reported quantities.
  - *Straw-man warning:* "does not **universally** outperform" is refuted by a
    single counterexample and asserts nothing anyone claimed. The informative
    registration is the effect size and its interval on the specific benchmark.
- **Transferable positive:** **none found — the result is intra-domain.**
  "Establishes the baseline" is the ordinary output of any benchmark study, not
  a cross-domain transfer.
- **Verified:** conclusion CONFIRMED verbatim; dataset structure (20 datasets,
  300 stocks × 250 trading days, 40+ methods, six backbone families) CONFIRMED.
  **One sub-fact failed:** the "Chinese A-shares" attribution is **not stated**
  in retrievable paper text. Data is distributed via Eastmoney and the transfer
  evaluation uses CSI 300; write it that way rather than asserting the market.
- **Autopsy:** not yet written.

---

## F005 — The most-used definitions of "level" have never been tested for existence

- **Result as reported:** across 76 operational definitions of support/resistance
  recovered from peer-reviewed literature, arXiv, GitHub, TradingView and
  practitioner sources, only 16 have ever had statistical apparatus attached. Of
  those, the 7 that tested the level's own **existence or location** are all Class R
  (requires round numbers), Class T (requires the tick grid), or N-X (anchored to an
  exogenous institutional grid). **Not one Class N definition — independent of both
  confounds, and 70% of the corpus — has ever had its existence tested.** That
  includes every pivot formula, every extremum detector, every clustering rule and
  all eight candle-geometry constructions. No source reports a confidence interval
  on a level location.
- **Source:** [lit_review_level-definitions_2026-08-21.md](docs/literature/lit_review_level-definitions_2026-08-21.md),
  81 included records from 390 screened. **Tier: mixed** — the review is a
  single-screener, PRISMA-partial survey; its own declared gaps include that no full
  text was read for any record and no forward-citation search was run, so the count
  of definitions-with-a-test is a **lower bound**.
- **Layer:** `data` — ~~`undetermined`~~ (original assignment, superseded by
  the obtained discriminating observation; see the 2026-08-21 addendum below).
  - *Alternatives considered:* `source-artifact` (the literature tested what was
    testable and the gap reflects publication practice), `question` (Class N
    existence may not be identified without an exogenous anchor — which is precisely
    what R, T and N-X definitions supply and N lacks), `data` (the tests exist but
    are unindexed and the survey missed them).
  - *Discriminating observation:* a forward-citation search from the seven tested
    definitions, plus a targeted search for any Class N existence test. **Obtainable**
    — the survey explicitly did not run one.
  - *Why this is not yet a null:* no hypothesis has been tested and failed. This is
    an **absence of testing**, not a negative result about levels. Registering it
    here is a deliberate widening of the register's scope, flagged as such.
- **Transferable positive:** the asymmetry is itself informative. The definitions
  that *have* been tested are exactly those with an exogenous anchor — a round
  number, a lattice, a strike — against which "the level is here and not there" is a
  statable hypothesis. Class N definitions derive the level from the path itself,
  which is what makes them convenient and also what makes an existence test require
  a surrogate. **The testability gap tracks the identification problem, not neglect.**
  That is a claim about why the literature looks the way it does, and it is checkable.
- **Verified:** counts and taxonomy are the survey's own, verified programmatically
  by it as exact and disjoint over all 76. Not independently re-verified.
- **Autopsy:** not written. This row and F001 are the two that would most repay one.
- **ADDENDUM 2026-08-21 — discriminating observation OBTAINED; layer promoted
  `undetermined` → `data` under the charter's promotion rule.** The recorded
  observation (forward-citation search from the seven tested definitions plus a
  targeted Class-N existence-test search) was executed under
  [deliverable_spec_phase1-sweep_2026-08-21.md](docs/deliverables/deliverable_spec_phase1-sweep_2026-08-21.md);
  full record at
  [lit_review_f005-class-n-tests_2026-08-21.md](docs/literature/lit_review_f005-class-n-tests_2026-08-21.md)
  (3,769 identified / 1,948 screened / 7 included; 1,825 distinct citing works
  across the seven seeds).
  - **The headline claim "not one Class N definition has ever had its existence
    tested" is refuted as stated.**
    [Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero 2014](https://doi.org/10.1038/srep04487)
    (*Scientific Reports* 4:4487, peer-reviewed, read in full via
    arXiv:1110.5197 v1 — whose author list lacks Pompa; the published version
    carries five authors) tests a path-derived trailing-extremum level — fully
    affine-equivariant, Class N — via conditional bounce probability against a
    shuffled-return null: deflection significantly above chance, increasing in
    prior bounces, at 45–90 s timescales (not 180 s), LSE tick data.
    Peer-reviewed boundary evidence: Driessen, Lin & Van Hemert 2013; Huddart,
    Lang & Yetman 2009; Mizrach & Weerts 2009.
  - *Why `data`:* the tests exist and the survey missed them. Sharpening:
    Garzarelli was **retrieved by the survey (q-arxiv-01) but bulk-excluded
    without a coded reason**, and the 52-week-high family was never retrieved
    (vocabulary: "supports and resistances" defeats the phrase query "support
    and resistance"). The alternative layers (`source-artifact`, `question`)
    are not supported: the gap was recall, not publication practice or
    identification.
  - **Two narrower negatives survive:** (a) no located Class N existence test
    uses a charter-admissible null — Garzarelli's shuffled-return surrogate is
    exactly the return-resampling class branch 1 rules inadmissible; (b) no
    **located** source reports a confidence interval on a level location —
    coverage-bounded, not universal (~1,354 of 1,948 screened titles matched
    neither keyword net and were not individually read; f005 review §10). The
    unbounded form of exactly this claim is what this addendum refutes.
  - **Transferable positive — WEAKENED.** The original claim ("the testability
    gap tracks the identification problem, not neglect") is contradicted in
    part: at least one Class N existence test was published and simply missed,
    so neglect-of-retrieval explains part of the gap. What survives: no Class N
    test with an *admissible* null exists, and that narrower gap does still
    track the identification problem (a path-derived level needs a surrogate;
    every published attempt reached for the inadmissible resampling class).
  - *Unadjudicable candidate flagged:* SSRN 3021585 ("Faulty Anchors",
    52-week-high family) — no abstract retrievable at any API, SSRN 403;
    potentially a further included record.

## Column health check

Standing check mandated by charter step 4: **the transfer column must not be
uniformly populated.** Current state — 2 transfers found, 2 "none found". Rev 1
was 4-for-4, which is the signature this project would flag in someone else's
work. Re-audit the criterion if the rate returns to 100% over any window.

## Open autopsies

All four. None has executed protocol steps 1–2. F001 is highest priority: it is
the most load-bearing negative result in the project, it rests on an unrefereed
preprint, and its layer is `undetermined` pending an observation the source does
not supply.

---

# Revision 3 rows (2026-09-04) — the Kalshi multivocal branch

All four rows below are registered from
[lit_review_kalshi-strategy-multivocal_2026-09-04.md](docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md)
§10 (negative results), §11 (data-integrity defects) and §12 (named gaps), and
from the arm logs under
`docs/literature/search_logs/kalshi-strategy-multivocal/`. **No citation is
introduced here that is not already carried by that corpus record, its arm logs,
or `ks-instrument-verification.json`.**

**Standing tier statement for all four rows.** The multivocal corpus contains
**zero peer-reviewed and zero preprint records** — its academic arm assigned no
eligibility verdict to any of its 528 identified records, all of which are `G1`,
undecided (corpus gap **G-5**). Every row below therefore rests on tier 2
(official documentation, the venue and regulator filings) or tier 5 (everything
else). **No row below is at the top of the evidence hierarchy and none may be
cited as if it were.**

**Bare numbers.** Every figure quoted below is quoted verbatim from its source
with its locator and is **NOT ADOPTABLE** as a parameter anywhere in this
project (corpus gap **G-23**; `~/.claude/CLAUDE.md` §"Parameter & Prompt
Selection"; charter commitment 3). None is re-derived, re-scaled, rounded or
annualised here.

---

## F006 — The post-print latency race on a scheduled-release ladder is FORECLOSED on the one series for which a source states the timing, not merely unprofitable

- **Result as reported.** Two components, and they are different kinds of thing,
  so they are kept apart:
  - *(a) An absence.* The multivocal corpus's lateral arm executed **seed 5**
    specifically for the post-release latency class. **No retrieved source states
    it as an executable class for the series examined.** The candidate class is
    dispositioned **Y3 (unsourced)** as `ks-y3-5` and enters **no** taxonomy row
    (corpus §6, §10 N-1). An unsourced strategy is never recorded as a finding by
    that corpus, and it is not recorded as one here.
  - *(b) A sourced statement running the other way.* `KSL-C18`, full text of the
    retrieved bytes, Kalshi-specific, attributed verbatim to OddsShopper,
    2026-08-19: *"on Kalshi's KXPAYROLLS ladder, trading closes at 8:29 AM ET and
    the report lands at 8:30, so whatever you hold going in is what gets graded."*
    The same source states the close is tied to the expected release rather than
    to a fixed clock — each monthly market carries a close set, in the exchange's
    own wording as that source quotes it, *"at 8:29 AM ET on the expected date of
    the data release."* The corpus records this as a **constraint** (contribution
    code K3), not as a trade.
  - **The null this row registers, stated precisely:** *on the KXPAYROLLS ladder,
    there exists no instant between the release of the payrolls print and the
    grading of the contract at which an order can be placed, because the venue's
    stated close precedes the release.* That is a statement about the admissible
    **action set**, not about the profitability of acting.
- **Established here, or reported by a source?** **Reported by a source**, and by
  exactly one. This project established nothing about the venue's timing; it
  transcribed a practitioner page's quotation of the exchange's wording.
- **Source and tier.** `KSL-C18`, lateral arm
  (`ks-lateral-records.json`), source class **S-E**, extraction depth full text of
  the retrieved page, retrieved 2026-09-04. **Tier 5.** The venue-primary
  confirmation — the KXPAYROLLS series' own filed terms and conditions — was
  **not retrieved**: the venue arm specified **one** of roughly ninety contract
  series at terms-and-conditions depth (corpus limitation 3), and the rulebook in
  force on the retrieval date **was not located** (gap **G-1**).
- **Steps 1–2 executed?** **NO.** *This row states no alpha, no n, no target
  detection probability and no MDES.* None was computed by this project and none
  is stated by the source. Under the charter's step-1 branch for test-free
  sources, component (b) reports **no hypothesis test at all**; it reports a rule.
  The row is registered because a rule that empties the action set is the strongest
  possible form of a null about that action set, not because a test was run.
- **Layer:** `question` **for the named series (KXPAYROLLS)**; `undetermined`
  **for the class in general**. Both assignments are stated because they are
  genuinely different, and collapsing them would be the error the corpus's own
  scope note warns against.
  - *Alternatives considered, for the series:* `precision` (the race exists and
    the edge sits inside cost and noise), `data` (the window exists and no capture
    resolves it), `temporal-validity` (the window existed and a rule change closed
    it), `question` (the target quantity is not identified by **any** design
    because no observation of a post-print order on that series can exist),
    `construct` (rejected outright — the charter's five-condition gate is not met
    and is not close to being met).
  - *Why `question` and not `precision`:* the two make different predictions about
    what more data would do. Under `precision` the estimate of a post-print return
    exists and its interval narrows with n. Under the stated close, **no
    observation is generable at any n**, because there is no instant at which an
    order is admissible. The layer definition — "the target quantity is not
    identified by the design, regardless of n" — is met by the venue rule rather
    than by the analyst's design, which is a widening of the layer's ordinary use
    and is flagged as such.
  - *Why `temporal-validity` cannot be excluded:* the venue's terms are amendable
    on **ten** business days' notice for a rule change (`d22-c1`) and **one**
    business day for a product listing (`d22-c3`), and the rulebook in force is not
    located (**G-1**). The close time is therefore a dated fact with no
    point-in-time archive behind it. Whether the window ever existed and was closed
    is **not determinable from the retrieved record**.
  - *Discriminating observation:* **the KXPAYROLLS series' own filed terms and
    conditions, stating the trading close relative to the scheduled release.**
    Status: **obtainable in principle, NOT OBTAINED.** It is not in the retrieved
    document set (limitation 3, **G-1**), and what stands in its place is a tier-5
    page's quotation of it.
  - *Why `undetermined` for the class:* the absence in component (a) is an absence
    **over the endpoints the lateral arm reached**. Forum and community archives,
    podcast and conference transcripts and paywalled trade press were **not reached
    as distinct endpoints** (**G-21**); no code-level and no notebook search was
    executed at all, both endpoints returning HTTP 401 unauthenticated (**G-22**).
    An absence over unreached endpoints is not evidence of absence. The class-level
    statement is bounded to **one series, one source**, exactly as the corpus's own
    scope note for N-1 states.
- **Transferable positive:** **found.** A venue-imposed trading close that
  **precedes** the settlement observation converts a latency question into a
  **documentary** question, answerable per series from filed terms before any
  market data is acquired, any API is called, or any capture is built. That is a
  constraint identified by the null and live elsewhere: it applies to every
  scheduled-release event contract on any venue, and it reorders the work — read
  the close time first, and the entire latency design either has a subject or does
  not. **It is not a licence to assume the same close on any other series**; the
  corpus states the scope in terms, and any transfer must re-read the terms.
- **Verified:** the `KSL-C18` quotations are reproduced from corpus §10 N-1, which
  carries them verbatim from the lateral arm's stored retrieval. **They were not
  re-retrieved from the source in this session, and the venue-primary term was not
  obtained.** Verification status: **single-source, tier 5, unconfirmed against the
  filed contract terms.**
- **Autopsy:** **warranted, not written.** Its whole content would be the
  discriminating observation above — the filed KXPAYROLLS terms — so it should not
  be written until that document is retrieved. Path when written:
  `docs/research_notes/autopsy_{slug}_{YYYY-MM-DD}.md`, per the charter's
  admissible output types.

## F007 — The weather / temperature-settlement stratum is near-empty in the academic record, and that emptiness carries NO information

- **Result as reported.** The multivocal corpus's academic arm reports near-zero
  yield in its weather-and-climate stratum (`S3`). The corpus's own limitation 9
  and §10 **N-5** state that this is **not a clean absence** and must not be read
  as one. This row registers the non-result and refuses the inference.
- **What was actually executed, checked against the arm logs in this session and
  NOT taken from the corpus record's summary:**
  - **`ks-s2-03` never executed.** The one query aimed squarely at temperature
    settlement — verbatim
    `https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50`
    — was attempted **eleven** times (`ks-s2-03`, `-03-b` … `-03-k`; eleven log
    files exist on disk) and **every attempt returned HTTP 429**. Across the whole
    academic arm, **53 of 56** Semantic Scholar attempts returned HTTP 429 and one
    returned HTTP 500 (gap **G-9**).
  - **The RePEc rows are not searches.** `ks-repec-04.json` records
    `http_status: 200`, `n_returned: 0`, and its own field
    `platform_interface_failure` states verbatim: *"PLATFORM INTERFACE FAILURE, NOT
    A ZERO-YIELD RESULT. The endpoint answered HTTP 200 but the body is the
    IDEAS/RePEc search FORM, not a result set … The query therefore never executed
    … n_returned=0 here means NO SEARCH WAS RUN and must not be read as 'RePEc
    contains no such record'."* Its `n_returned_semantics` field reads *"no search
    executed; not an observed zero-yield."*
  - **A discrepancy between the corpus record's summary and the arm log, resolved
    in favour of the arm log, and NOT repaired in either document.** Corpus §10
    N-5 states that **four** academic queries in that stratum *executed* and
    returned zero, naming `ks-arxiv-04`, `ks-openalex-04`, `ks-repec-04` and
    `ks-repec-04-b`. By `ks-repec-04.json`'s own field, the two RePEc rows **did
    not execute**. The executed-and-zero count in that stratum is therefore **two**
    (`ks-arxiv-04`, `ks-openalex-04`), not four. The arm-log field is preferred
    because it is the statement derived from the retrieved bytes. Neither the
    corpus record nor the arm log is edited by this row; the discrepancy is
    recorded here and belongs to the corpus record's own gap register (**G-9**
    and §11's defect class).
  - **One further check, recorded because it is a correction in the strict
    direction.** The arm log states the page *"carries the banner 'IDEAS is
    struggling with massive bot traffic, please be patient.'"* That string **is**
    present in the retrieved payload `payloads/ks-repec-04.html`, but it sits
    **inside an HTML comment** and therefore does not render. The load-bearing
    fact is unaffected and is independently checkable in the same bytes: the
    document's `<title>` and `<h1>` are both *"IDEAS/RePEc search"* and the body is
    the search form, **not a result set**. The verdict stands; one clause of its
    stated evidence is weaker than the log implies, and saying so is cheaper than
    letting a later reader find it.
- **The null this row registers, stated precisely — and it is a NON-null.** *No
  proposition about the weather/temperature-settlement literature is established
  by this stratum's yield.* A capacity gap is not an absence.
- **Established here, or reported by a source?** Neither. This is a property of
  **this project's own search**, registered because the charter makes nulls objects
  of study and because the reading a hurried successor would take — "there is no
  literature on temperature settlement" — is unsupported.
- **Source and tier.** `ks-repec-04.json`, `ks-repec-04-b.json`, the eleven
  `ks-s2-03*` log files, and corpus §10 N-5 / limitation 9 / gap **G-9**. **Tier:
  n/a** — these are this project's own execution records, not evidence about the
  world.
- **Steps 1–2 executed?** **NO.** *This row states no alpha, no n, no target
  detection probability and no MDES.* Under the charter's step-1 branch this row
  is not a null at all: **no hypothesis was tested, and one of the searches that
  would have supplied the observation never ran.**
- **Layer:** `undetermined`, **and the reason is that the observation was never
  made.** The charter's rule is used here as written — a layer with no
  discriminating observation is `undetermined`, not a guess — and **no layer is
  manufactured**.
  - *Alternatives considered:* `data` (the literature exists and the reached
    indexes do not cover it), `source-artifact` (the literature genuinely lacks a
    temperature-settlement strategy record, and the emptiness reflects publication
    practice), `precision` (inapplicable — there is no estimate), `question`
    (inapplicable — nothing was being identified).
  - *Why neither `data` nor `source-artifact` may be asserted:* the two make
    identical predictions about **the record actually in hand**, because the query
    that would separate them never ran. Choosing between them on the evidence held
    would be a guess dressed as a localization, which is the defect rev 2 of this
    file was written to stop.
  - *Discriminating observation:* execution of `ks-s2-03` **verbatim as frozen**,
    plus a RePEc/EconPapers route that returns a result set rather than the search
    form. Status: **OBTAINABLE.** It requires a retry window that survives the rate
    limiter, or an alternative index, and it belongs to a later session **as a
    numbered amendment stating the rule it applied before it applies it** (the
    corpus's protocol §4.4 rule 4 precedent, and handoff **TC-13** for the same
    discipline over the undecided rows).
- **Transferable positive:** **none found.** An absence produced by a rate limiter
  and a bot-mitigation interstitial carries no information about any literature, so
  there is nothing here to transfer. The methodological rule this project applies —
  "a capacity gap is not an absence" — is a **house rule already in force** (the
  corpus's `G1` capacity code exists precisely to keep such rows out of the Y-code
  counts), not a positive extracted from this null, and recording it as a transfer
  would inflate the transfer column with something the row did not produce.
- **Verified:** the eleven `ks-s2-03*` log files were confirmed present on disk in
  this session; `ks-repec-04.json`'s two disposition fields were read verbatim; the
  banner's comment status and the form-page identity were checked in
  `payloads/ks-repec-04.html`. The HTTP-429 status of each of the eleven attempts
  was **not** individually re-read in this session and rests on the corpus record's
  §10 N-5 statement.
- **Autopsy:** **not warranted.** There is nothing to autopsy. The remedy is a
  search re-execution under a numbered amendment, not a forensic reading of a
  result that does not exist.
- **ADDENDUM 2026-09-04 — the corpus record HAS since been corrected; the row
  above is left standing verbatim and is superseded on ONE sentence only.** The
  sentence *"Neither the corpus record nor the arm log is edited by this row"*
  described the state of those two documents at the moment this row was written,
  and it stays legible as written. **As of 2026-09-04, in the same audit round
  that produced this addendum, the corpus record
  [lit_review_kalshi-strategy-multivocal_2026-09-04.md](docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md)
  has been corrected at its §10 N-5 and N-8 loci, under audit findings
  REV-1-1 / SCOPE-1-1 / QUANT-1-1 / LITERATURE-1-1 / REPRODUCIBILITY-1-1 /
  FORMAT-1-1, and now carries a data-integrity entry cross-referencing this row.**
  Three consequences, stated so that no reader has to reconcile the two documents
  by hand:
  - **The arm logs remain deliberately UNEDITED, and that is the point.** They are
    the primary record — the statement derived from the retrieved bytes — so the
    only admissible direction of repair is summary-corrected-against-log, never
    log-corrected-against-summary. `ks-repec-04.json` and `ks-repec-04-b.json` are
    untouched by this row, by that correction, and by this addendum.
  - **The executed-and-zero count of TWO now appears in BOTH documents** — in this
    row, and in the corrected corpus record — so the discrepancy this row recorded
    is no longer live between them. The two are `ks-arxiv-04` and `ks-openalex-04`;
    the two RePEc rows are interface failures and are not searches.
  - **What is UNCHANGED by the correction:** the null this row registers, its
    `undetermined` layer, its discriminating observation (verbatim re-execution of
    `ks-s2-03` plus a RePEc route that returns a result set), and its **none
    found** transfer entry. The correction is to the state of a cited document, not
    to this row's finding, and this row is not promoted, demoted or withdrawn by it.

## F008 — A repository's best candidate strategy is statistically indistinguishable from an always-NO baseline (null REPORTED BY A SOURCE)

- **Result as reported, verbatim and attributed.** `ks-sc-001` —
  `github.com/sudo-ai-git/kalshi-backtest` at commit
  `c32b700111a321db16a8cfae5eceaab0ea167dd8`, README-and-metadata depth, dated
  2026-08-27, accessed 2026-09-04 — states in its README, over *"~92,000
  settled/closed Kalshi markets"*: *"Best candidate strategy (BUY_NO @
  high-NO-prob) | +1.37% ROI, CI [1.13, 1.61], n=23"*, and states in the same
  README that the candidate is **"statistically indistinguishable"** from the
  always-NO baseline, that *"The correct null for any strategy is the **always-NO
  baseline**, and every candidate must beat it"*, and that the favourite–longshot
  bias *"is already priced in and eaten by fees/spread."*
- **Established here, or reported by a source?** **REPORTED BY THE SOURCE.** This
  project ran nothing, fitted nothing and acquired no market data
  ([ADR-0003](docs/decisions/ADR-0003-specification-not-execution.md)). The
  figures above are transcribed verbatim and attributed. **They are NOT ADOPTED,
  NOT re-derived, NOT re-scaled and NOT annualised**, and `+1.37%`, `[1.13,
  1.61]` and `n=23` are **NOT ADOPTABLE** as parameters anywhere in this project
  (**G-23**). The corpus additionally records that **the ROI figure's own cost
  treatment is not stated in the README**.
- **Source and tier.** `ks-sc-001`, software-repository arm
  (`ks-github-records.jsonl`), source class **S-C**, contribution codes K1/K2/K4,
  taxonomy classes T4 and T8, **no persistent identifier** (ADR-0006 design;
  **G-15**), README digest
  `50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118`. **Tier 5.**
  Not peer-reviewed, not a preprint, not refereed by anyone.
- **Steps 1–2 executed?** **NO, by this project.** *This row states no alpha, no
  target detection probability and no MDES computed by this project.* The
  **source** states an n (23), a point ROI and an interval, and states no alpha,
  no target detection probability and no MDES of its own. Under the charter, an
  interval on a point estimate is not an MDES and does not substitute for one; the
  handoff that names the lawful substitute is **TC-12** — minimum detectable effect
  size, **never** retrospective power.
- **Layer:** `undetermined`.
  - *Alternatives considered:* `precision` (n=23 candidate events cannot resolve
    an effect of the size at issue), `data` (the universe is wrong — see below),
    `method` (the indistinguishability verdict rests on an unstated statistic),
    `estimand` (a marginal average over a heterogeneous market population masking a
    moderator), `construct` (**rejected outright**; the charter's five-condition
    gate is not met and a README cannot meet it).
  - *Why no layer can be settled:* the README states **which** conclusion it
    reached and **not** how. Three things are unstated at the depth the record was
    assessed — the test used to declare indistinguishability, the cost treatment
    behind the ROI figure, and the procedure by which the candidate's NO-probability
    threshold was chosen. Any of the four candidate layers reproduces the reported
    output under some filling-in of those three, so the observation in hand
    discriminates none of them.
  - *Discriminating observations, all three OBTAINABLE and none obtained:* (i) the
    statistic and its alpha for the baseline comparison; (ii) the cost treatment of
    the ROI figure; (iii) the candidate-threshold selection procedure — which is
    exactly the corpus's handoff **TC-11** ("the NO-probability threshold defining
    `ks-sc-001`'s candidate — grid or cross-validated search with a bootstrap CI").
    All three sit in the repository at full depth; the record was assessed at
    **README-and-metadata depth only**, which is a stated warrant label and not an
    oversight.
  - *A `data` alternative that the corpus itself supplies, and that a successor
    must not skip:* `KSL-C30` states that the venue's raw markets feed is **flooded
    with auto-generated combination markets**, so a scanner's market count is not a
    count of tradeable markets, and **TC-8** records that the universe-construction
    filter separating single-outcome markets from combinations **is uncomputed and
    no source states a rule for it**. Independently, `ks-sc-002` states that *"79%
    of the 54,380 contracts observed never showed a two-sided book."* Whether
    "~92,000 settled/closed markets" is a census of tradeable objects is therefore
    **open**, and it is open in a direction that bears on the null.
  - *Step 2b — source-design validity: a CONDITIONAL, not a finding.*
    **[corpus-inference]** — the marker the predecessor branch uses for a step from
    what an author **states** to what the author does **not** state (corpus record
    §8.4 legend). **Rewritten 2026-09-04, audit finding REV-1-5; the superseded
    wording is kept below rather than deleted.**
    - *Superseded wording, left legible and struck:* ~~"The candidate was selected
      **and** evaluated on the same market set, with no stated family-wise control
      (**TC-14** names the control that is absent). A post-selection interval is
      biased **toward finding an effect**. So the source's negative verdict is
      reached **despite** a bias running the other way, which makes the null
      **more** informative than its provenance would otherwise suggest — the
      opposite of F001's situation."~~
    - *Why it was wrong: the premise is not in the record.* **The README does not
      state whether the candidate was selected and evaluated on the same market
      set.** What `ks-github-records.jsonl` does state is that the **two figures
      the record reports rest on spans that DIFFER**: the headline finding is
      located in a README section titled *"The headline finding (from ~92,000 real
      settled markets)"*, while the record's own `data_span` field reads *"~92,000
      settled/closed Kalshi markets; NO-tilt measured across a 30k settled
      sample"*, and the reported candidate carries `n=23`. Whether the selection
      set and the evaluation set coincide is therefore **undetermined at the depth
      assessed**, and the original wording asserted as fact something the record
      does not carry.
    - *The conditional that survives, and it is all that survives.* **IF** the
      candidate was selected **and** evaluated on the same market set — an
      antecedent this record does not settle — **THEN** the reported interval is a
      post-selection interval whose bias runs **toward finding an effect**, and the
      source states **no** family-wise control (**TC-14** names the control that is
      absent: White 2000 reality check or Hansen 2005 SPA, adopted for this branch
      by explicit reference under
      [ADR-0004](docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md)).
      **ONLY under that antecedent** is the source's negative verdict reached
      despite a bias running the other way.
    - *Status of the informativeness upgrade: **CONTINGENT, not established.*** The
      claim that this null is **more** informative than its provenance suggests is
      **conditional on the discriminating observation below and is not asserted by
      this row**. Until that observation is made, this row asserts **no** direction
      of bias, and the contrast with **F001** — which was the whole reason the
      superseded wording was written — is **not available and must not be cited**.
    - *A FOURTH discriminating observation, added by this correction, **OBTAINABLE**
      and not obtained:* whether the market set over which the candidate's
      NO-probability threshold was chosen is the same set over which the `+1.37%`
      figure and its interval were computed, and which of the two stated spans each
      figure rests on. It sits in the repository at full depth, alongside the other
      three, and it is what converts the conditional above into a finding or
      discharges it.
- **Transferable positive:** **found.** The **always-NO baseline as the mandatory
  comparator** — the source's own sentence, *"The correct null for any strategy is
  the always-NO baseline, and every candidate must beat it"* — is a design
  constraint, not a number, and it transfers: on any binary event-contract market
  where the NO leg resolves true in most listed contracts, a candidate's absolute
  hit rate is uninformative and any evaluation that omits the constant-NO
  comparator has not stated a null. It binds this project's own specifications
  directly — it is the same obligation as `research/01_hypothesis_register/H001/design.md`
  §1.6 ("What it must beat"), reached independently by a practitioner. **Adopted as
  a constraint on test design; the source's numbers are adopted as nothing.**
- **Verified:** the quotations are reproduced from corpus §10 N-2, which carries
  them from the README at the pinned commit with a byte digest. **They were not
  independently re-retrieved from GitHub in this session.** The record's identifiers
  (commit, digest, dates, depth) were read in this session from
  `docs/literature/references_kalshi-strategy-multivocal.json`. **Added 2026-09-04
  (REV-1-5):** the two reported spans were read in this session from
  `ks-github-records.jsonl` / the software arm's extraction record, field
  `F10_outcome_reported.data_span`.
- **Autopsy:** **warranted, not written**, and it is the highest-value autopsy in
  this branch: it is the only record in the corpus, other than F009's, that states a
  data span **and** a cost treatment at all, all three discriminating observations
  are obtainable at full-repository depth, and the layer is settleable by reading
  rather than by re-running anything. Path when written:
  `docs/research_notes/autopsy_{slug}_{YYYY-MM-DD}.md`. *(Read with the Step-2b
  correction above: the autopsy now has **four** discriminating observations to
  obtain, not three, and the fourth decides whether the informativeness upgrade
  stands at all.)*

## F009 — A repository derives a taker round-trip break-even, in cents, at a stated price band, and reports the market as well calibrated (null REPORTED BY A SOURCE)

- **Result as reported, verbatim and attributed.** `ks-sc-002` —
  `github.com/himagna16/kalshi-microstructure` at commit `817fe37c…`,
  README-and-metadata depth, accessed 2026-09-04 — states, over *"July 30 to
  August 17, 2026; 8.06M snapshots across 54,380 contracts"*:
  - *"A contract trading at 40–50¢ must move **10.7¢** (≈ 11 percentage points of
    implied probability) before a taker round trip breaks even."*
  - *"**Prices are extremely well calibrated.** Brier score 0.009 at close, 0.062
    even 24h out (vs ~0.24 for guessing the base rate). The market knows."*
  - *"**Most listed contracts are never tradable.** 79% of the 54,380 contracts
    observed never showed a two-sided book."*
- **Established here, or reported by a source?** **REPORTED BY THE SOURCE.** No
  price was computed and no data acquired by this project (ADR-0003). **`10.7¢`,
  the `40–50¢` band, the Brier values and `79%` are quoted, attributed, and NOT
  ADOPTABLE** as parameters (**G-23**). The corpus records that **the Brier scores
  are point values with no interval stated**. The handoff that names the lawful
  route to an adoptable break-even is **TC-10**: *derived from the stated fee
  function and a **measured** spread distribution, not chosen by hand* — and the
  per-series multiplier that any such derivation needs is **blocked** by defect
  **DI-3**, the fee-schedule tables being present in the retrieved bytes and not
  extractable (**TC-2**).
- **Source and tier.** `ks-sc-002`, software-repository arm, source class
  **S-C**, taxonomy classes T4/T6/T8, **no persistent identifier** (**G-15**).
  **Tier 5.** Not peer-reviewed, not a preprint.
- **Steps 1–2 executed?** **NO.** *This row states no alpha, no target detection
  probability and no MDES.* The **source** states a data span, a snapshot count
  and a contract count, and states no alpha, no target detection probability and
  no MDES; its calibration claim is carried by **point values with no interval**.
- **Layer:** `no-stated-test` → `undetermined`, following F004's disposition for
  the same reason: **no hypothesis test is stated**, and under charter step 1 a
  row with no reconstructed test does not license a layer at all.
  - *Alternatives considered:* `data` (the universe is listings rather than
    tradeable objects), `method` (a Brier score with no interval and no reference
    class cannot support "the market knows"), `estimand` (an average over a
    heterogeneous contract population), `precision` (inapplicable — nothing is
    being resolved against a stated alternative), `construct` (**rejected
    outright**; gate not met).
  - *One observation IS in hand and it points at `data` for any DERIVED claim, but
    it does not promote this row.* The source's own third statement — 79% of
    observed contracts never showed a two-sided book — means a calibration
    statistic computed over the full listed universe is a statement about
    **listings**, not about **tradeable prices**. Whether the Brier figures were
    computed over the full 54,380 or over the roughly one-in-five with a two-sided
    book **is not stated at README depth**, and the two readings support opposite
    conclusions about the same numbers.
  - *Discriminating observation:* the universe over which the calibration statistic
    was computed, and whether the break-even derivation uses the venue's stated fee
    function with the **per-series** multiplier or a single flat rate. Status:
    **OBTAINABLE** from the repository at full depth; **not obtained** — the record
    was assessed at README-and-metadata depth.
  - *A second, external limit on any promotion:* the per-series multiplier that
    the break-even figure depends on is **not extractable from the venue's own
    published fee schedule** (**DI-3**), so even a full read of the repository
    cannot settle whether its cost treatment matches the venue's, until that table
    is recovered.
- **Transferable positive:** **none found.** All three statements are bounded to
  one venue, one nineteen-day window, and a universe the corpus separately records
  as contaminated by auto-generated combination markets whose filter is uncomputed
  (`KSL-C30`, **TC-8**). Naming an adjacent target the record did not examine and
  inferring it is unaffected is the category error the charter's step 4 forbids —
  "not tested" is not "not implicated" — and the honest column entry is the empty
  one. **The general proposition that a cost floor can exceed any plausible edge is
  not this record's contribution**; it is arithmetic, and quoting `10.7¢` as
  evidence for it would be adopting the number this row refuses to adopt.
- **Verified:** quotations reproduced from corpus §10 N-3, which carries them from
  the README at the stated commit. **Not independently re-retrieved in this
  session.** The commit is recorded in the corpus record as `817fe37c…`, truncated
  there and reproduced truncated here rather than completed from elsewhere.
- **Autopsy:** **warranted, not written**, at lower priority than F008: the
  universe question is answerable by reading the repository, but the fee half is
  blocked behind **DI-3**, so an autopsy written now would close one half and
  register the other as blocked. Path when written:
  `docs/research_notes/autopsy_{slug}_{YYYY-MM-DD}.md`.

---

## Candidate nulls considered at revision 3 and NOT registered

Recorded because a rejected candidate is cheaper to re-reject than to
re-adjudicate, and because two of them are readings a successor is likely to
reach for.

- **"RePEc contains no weather-settlement literature."** Rejected. **No search
  ran** (F007). The rows that would support it are interface failures.
- **"The academic literature on binary event-contract strategy does not exist,
  because the corpus contains no peer-reviewed record."** Rejected. The academic
  arm identified 528 records and assigned **no eligibility verdict to any of
  them**; all are `G1`, *undecided* — not eligible and not ineligible (**G-5**).
  An absence of verdicts is not an absence of records, and the corpus says so in
  its first limitation.
- **"The eight-class taxonomy is correct, because no class needed amendment."**
  Rejected as a row. The corpus's own **N-7** states this is evidence the buckets
  absorbed what the arms located and **not** evidence the partition is correct: a
  search that finds only what its partition anticipates always returns this
  result. It is a fact about the search, not about the world.
- **"The post-print latency race is unprofitable."** Rejected **in that form** and
  registered in the foreclosure form instead (**F006**). Unprofitability is a
  claim about magnitudes this project has not measured and will not measure
  (ADR-0003); the sourced statement is about the action set.

## Column health check — restated at revision 3

Charter step 4's standing check, recomputed over all nine rows. **Transfers
found: F002, F003, F005 (weakened), F006, F008 — five. "None found": F001, F004,
F007, F009 — four.** The column is not uniformly populated and the rate over the
revision-3 window alone is two found of four, so the re-audit trigger in the
rev-2 check is not met. The rev-2 statement of the check ("2 found, 2 none
found") described the file as it then stood and is left standing.

## Open autopsies — restated at revision 3

Nine rows, **zero autopsies written**, and **no row in the file has executed
protocol steps 1–2**. Priority order among the revision-3 rows: **F008** first
(three discriminating observations, all obtainable by reading a repository at
full depth, and it carries the branch's only mandatory-comparator transfer);
**F006** second, but **blocked** until the KXPAYROLLS filed terms are retrieved,
which is gated on **G-1**; **F009** third and half-blocked behind **DI-3**;
**F007** not warranted at all until its query executes. F001 remains the highest
priority in the file overall.

**Addendum 2026-09-04 (REV-1-5), append-only.** F008's discriminating-observation
count in the paragraph above reads **three** and is left standing as written; the
Step-2b correction in that row adds a **fourth** — whether selection and
evaluation used the same market set — which does not change F008's first place in
the priority order and does change what its autopsy must obtain.
