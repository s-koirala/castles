---
type: lit_review
subtype: vocabulary-expansion scoping sweep (umbrella record)
slug: regime-naming
date: 2026-08-24
reporting_standard: PRISMA-ScR partial (single screener; per-item conformance notes in the two part records)
spec: docs/deliverables/deliverable_spec_naming-sweep_2026-08-24.md
instrument: docs/literature/vocabulary_regime-synonyms_2026-08-24.md
part_records:
  - docs/literature/lit_review_regime-naming-a_2026-08-24.md   # practitioner clusters, 22 records
  - docs/literature/lit_review_regime-naming-b_2026-08-24.md   # academic clusters, 31 records
bibliography: docs/literature/references_regime-naming.json    # 53 entries, merged from the two part stores, zero id/DOI collisions
bibliography_sha256: ffe4294e991db08f105735e5c45d675c869e99ec4b68dd976b63f9600a2ce6f8
---

# Regime/state naming conventions — vocabulary-expansion sweep (umbrella)

Corrects the recall bottleneck of
[lit_review_regime-definitions_2026-08-21.md](lit_review_regime-definitions_2026-08-21.md):
that survey's queries were seeded from academic state vocabulary, and vocabulary
mismatch is this project's twice-documented failure class (F005; the
"supports and resistances" phrase-query miss). This sweep made the vocabulary
itself an empirical instrument before any evidence query ran.

## 1. Design (three stages, all delegated, all logged)

1. **Term harvest** — [vocabulary_regime-synonyms_2026-08-24.md](vocabulary_regime-synonyms_2026-08-24.md):
   137 head terms across 8 traditions, ~540 morphological surface forms
   (plural/hyphenation/word-order/POS axes), 12-entry homonym-collision ledger.
   Harvested from included-record keywords, practitioner taxonomies
   (Edwards & Magee, Murphy, Kaufman, Wyckoff, Market Profile), Wikipedia
   redirect graphs, and OpenAlex concepts — harvest provenance only, never
   evidence. Methodology: PRESS
   ([McGowan et al. 2016](https://doi.org/10.1016/j.jclinepi.2016.01.021),
   *Journal of Clinical Epidemiology* 75:40–46), pearl growing
   ([Schlosser et al. 2006](https://doi.org/10.1080/13682820600742190)),
   term-harvesting for search development
   ([Hausner et al. 2012](https://doi.org/10.1186/2046-4053-1-19)).
   Informative negative: OpenAlex carries **no controlled vocabulary** for any
   practitioner state term — free-text variants are the only instrument.
2. **Sweep A (practitioner clusters)** —
   [part record A](lit_review_regime-naming-a_2026-08-24.md): TA-spatial /
   range-consolidation, Wyckoff, auction/Market-Profile, retail smart-money,
   chart-pattern events, sentiment. 45 queries, 756 identified / 724 screened /
   22 included; entries NA-01…NA-20; 67 synonym-graph rows.
3. **Sweep B (academic clusters)** —
   [part record B](lit_review_regime-naming-b_2026-08-24.md): bull/bear
   extensions, business-cycle-on-markets, crisis/stress, volatility states,
   trend events, runs, directional change, regime-noun probes. 303 identified /
   266 screened / 31 included; entries NB-01…NB-31; 45 synonym-graph rows.

Combined flow: **1,059 identified → 69 duplicates removed → 990 screened →
937 excluded → 53 included.** All 53 records diffed against the five
predecessor stores (288 records) before inclusion; prior coverage cited, never
re-included. DOI verification per project rule: doi.org handle API
responseCode 1; the part records carry the G16 publisher-403 dispositions with
per-DOI logs (`swA-doicheck-01.json`, `swB-doicheck-01.json`,
`swA-g16-disposition.json`).

## 2. Synonym graph

112 rows total (§8.3 of part A; §8.9 of part B): term → construct → tradition
→ operational definition located (NA-/NB-/D-/level-survey id, or NONE) →
null-distribution status → evidence tier. The spatial/temporal boundary is
handled by cross-mapping: spatial structures (channel, band, zone, rectangle,
value area) map to the level survey's definition classes; temporal states
(accumulation, climax, risk-off episode) receive new entries. That the
practitioner vocabulary does not separate the spatial and temporal constructs
is recorded as a finding, not fought.

## 3. Findings that bind downstream artifacts

- **The time-t-null universal falls.** The regime-definitions survey's claim
  that "no source at any tier attaches a null distribution to the assignment
  of a state at time t" is **refuted by vocabulary expansion**: the
  explosive/exuberant-regime literature
  ([Phillips, Wu & Yu 2011](https://doi.org/10.1111/j.1468-2354.2010.00625.x),
  *International Economic Review* 52:201–226;
  [Phillips, Shi & Yu 2015](https://doi.org/10.1111/iere.12132),
  *International Economic Review* 56:1043–1078; NB-04/NB-05) date-stamps an
  explosive state in real time against derived critical values — a time-t
  assignment with stated limit theory. Neither record was in any predecessor
  store; the vocabulary that finds them ("explosive", "exuberance",
  "date-stamping") was outside the original query set. The narrower claim
  survives: within the 59 originally surveyed definitions, none attaches a
  time-t assignment null.
- **Chart-pattern events are the strong practitioner cluster**: definitions
  and nulls both exist at tier 1 (Savin/Weller/Zvingelis — venue corrected to
  *Journal of Financial Econometrics*; Dawson & Steeley; Caginalp & Laurent;
  Marshall et al. bootstrap null; Plastun gap tests). The rest of the
  practitioner vocabulary is definitions-without-nulls or names-without-
  definitions (Market Profile day types, one-time framing, value-area
  migration: zero records above tier 5 — three first-class zero-yield
  queries).
- **Runs is the mirror image**: a null apparatus without named states
  (Wald–Wolfowitz 1940 lineage → Cowles & Jones 1937 → Fama 1965,
  [doi:10.1086/294743](https://doi.org/10.1086/294743) verified →
  Niederhoffer & Osborne 1966), including a documented false-positive
  correction (Cowles 1960, averaging artifact) directly relevant to the
  charter's nulls-as-objects remit.
- **Crisis/stress vocabulary is operationalized in the academic literature**
  (risk-off episodes, flight-to-quality with definition-and-test together,
  FTS days, stress continua; NB-12…NB-16), with explicit synonym evidence
  linking stress↔crisis.
- **Two-sweep-stable negatives**: volatility squeeze/compression remains
  tier-5-only under every variant tried ("volatility squeeze" = 0 records in
  all of arXiv); secular bull/bear has no academic operationalization;
  momentum burst none at any tier; "smart money concepts" on arXiv = 0.
- **"Market phase" is the one regime-synonym with independent recall value**
  (it alone surfaced two records the "regime" vocabulary missed); mode/
  environment/condition/episode are collision-dominated.

## 4. Saturation adjudication (lead session)

**Saturation NOT reached, stated plainly.** The round surfaced 12 candidate
new families. Disposition per family:

- **Swept in-line by the flagging agent** (records included this round):
  bubble/explosive/exuberance; boom/bust; drawdown/drawup episodes;
  metastability; sequences-and-reversals; failed auction.
- **Logged open, not swept** (residuals for a future round, with expected-
  yield rationale): absorption, liquidity void, Judas swing, inversion FVG,
  midnight opening gap, "technical range" — all tier-5 ICT/Wyckoff-adjacent
  micro-vocabulary in clusters where this round's academic-platform yield was
  zero across every executed variant (ICT arXiv = 0; Wyckoff event acronyms =
  0). A supplementary round over these terms has an evidenced near-zero
  expected academic yield; running it now would spend the session's budget on
  the least-promising stratum. All 12 flagged families are carried as rows in
  the registry's 2026-08-24 post-sweep addendum (6 marked swept-in-line, 6
  open — variant generation deferred to the round that sweeps them), per
  audit finding REV-1-2; the flags originate in part A §8.4 and part B §8.7.
- **Declared unexecuted variants** are listed in part A §10.4 and part B
  §8.10 (~540 surface forms, 104 queries executed across both sweeps plus
  known-item batches; per-cluster prioritization recorded).

## 5. Limits

Single screener throughout; abstract-depth screening (no full texts except
where the part records say otherwise); Semantic Scholar effectively
unavailable both sweeps (HTTP 429 — S2-unique recall untested, logged);
non-English vocabulary unexplored; in-text thresholds of NB-01/NB-11/NB-12
not extracted (abstract-depth; flagged for a full-text pass). Every count
above is recomputable from the logs under
`docs/literature/search_logs/regime-naming/` (25 vh-, 52 swA-, 64 swB-
files).
