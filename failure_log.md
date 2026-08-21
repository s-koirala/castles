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
