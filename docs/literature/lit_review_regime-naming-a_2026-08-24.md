---
title: "Practitioner market-state vocabulary, sweep A: operational definitions, null distributions, and academic operationalizations for the range/consolidation, Wyckoff, auction/Market-Profile, retail smart-money, chart-pattern-event, and sentiment-state clusters of the regime-naming registry"
slug: regime-naming-a
date: 2026-08-24
objective: "For each practitioner term family assigned to sweep agent A by the regime-naming registry (vocabulary_regime-synonyms_2026-08-24.md), locate (a) operational definitions - computable rules assigning the state or structure, at any evidence tier; (b) any published null distribution or statistical test attached to the concept's existence or assignment; and (c) academic studies that operationalized the practitioner concept algorithmically - diffed against the five predecessor corpora so that no prior record is re-included."
review_type: scoping
standard_declared: "PRISMA-ScR (Tricco et al. 2018, doi:10.7326/M18-0850) - PARTIAL COMPLIANCE, single screener, adapted to a non-clinical definitional corpus; unmet items named in section 1.3. Search reporting follows PRISMA-S conventions where applicable."
eligibility_inclusion:
  - "Any source stating a computable rule that assigns one of the swept practitioner states or structures (trading range, consolidation, rectangle, Wyckoff phase or event, auction/Market-Profile state, ICT structure, chart-pattern event, overbought/oversold or contrary-opinion state) to a time index, interval, or price region - any tier, any language, any year."
  - "Any source attaching a null distribution, reference distribution, bootstrap, or hypothesis test to the existence, occurrence frequency, or return effect of one of the swept constructs."
  - "Any academic study (journal, conference, preprint) that operationalizes a practitioner concept from the swept clusters algorithmically, whether or not it finds the construct informative."
eligibility_exclusion:
  - "Records already present in any of the five predecessor stores (references_regime-definitions.json 54, references_regime-classification.json 96, references_level-definitions.json 81, references_regime-method-gaps.json 50, references_f005-class-n-tests.json 7): cited as prior coverage, never re-included, by dispatch directive."
  - "Agent B's clusters: bull/bear directional states, business-cycle dating, crisis/stress/risk-on-risk-off, volatility regimes, momentum/mean-reversion classes, latent-state statistical vocabulary, runs/drift, directional-change/intrinsic-time, and bare regime-noun synonyms."
  - "Spatial structures already carrying a level-survey definition class (D-series of lit_review_level-definitions_2026-08-21.md): cross-mapped in the synonym graph, not re-defined; a new record is included only if it adds a definition, test, or peer-reviewed operationalization the D-series lacks."
  - "Strategy-tuning papers that consume an existing definition without adding a rule or test; automated content-mill records (the Zenodo E8 Intelligence Research family); records whose authorship cannot be attributed."
registration: not-registered
protocol_path: none
protocol_amendments: "Eligibility was fixed before the first query. Three conduct events are recorded rather than backdated: (i) Semantic Scholar rate-limited the sweep - one query executed (swA-s2-01), one failed with persistent HTTP 429 after six retries (swA-s2-02, logged as an access failure); (ii) the swA-s2-01 log records the second of two query strings run under that id - the first ('Wyckoff method trading accumulation distribution detection', 6200 total hits, same top-20 relevance profile) was overwritten by the retained run and is declared here rather than reconstructed; (iii) three OpenAlex queries (swA-openalex-07, -15, -16) mis-parsed their OR/phrase syntax and retrieved generic corpora - they are retained in the source table as executed, screened to zero, and re-run in corrected form (swA-openalex-09/-10, -17, -18)."
bibliography: references_regime-naming-A.json
bibliography_sha256: a83bf3e887192a1f30667c8df1ff768abb2b368d2d06d07f56cebbc6b27223d2
n_identified: 756
n_duplicates_removed: 32
n_screened: 724
n_excluded: 702
n_included: 22
materials_availability:
  - search_logs/regime-naming/
competing_interests: none
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent, sweep-A dispatch) designed and executed every search, screened every record, and drafted this review. Sole screener, declared as an automation tool under PRISMA 2020 item 8. No human second screener. Reproducibility log directory: logs/reproducibility/"
git_head_at_authoring: "0845acbf5d464cd330c93941c3af1bf000f3791d"
pip_freeze_sha256: "n/a - no analysis code was executed; only stdlib metadata-retrieval scripts (Crossref, OpenAlex, arXiv, Semantic Scholar, DOI handle API) and build_bibliography.py"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-fable-5"
---

# Practitioner market-state vocabulary, sweep A

## 1. Objective and eligibility

This is one of two concurrent recall sweeps executed against the term registry
[vocabulary_regime-synonyms_2026-08-24.md](vocabulary_regime-synonyms_2026-08-24.md).
Agent A holds the practitioner clusters: (1) TA-spatial and range/consolidation,
(2) Wyckoff cycle and event vocabulary, (3) auction/Market-Profile, (4) retail
smart-money (ICT), (5) chart-pattern events, (6) sentiment/press states.
Agent B holds the academic clusters and its output is a separate artifact.

Records were screened on title, abstract (where retrievable), and verified
metadata against the frozen criteria in the frontmatter. Synthesis groups
records by cluster and expresses every swept term as a synonym-graph row
(section 8.3) whose operational-definition column resolves to a new NA-series
entry, a predecessor D-series entry or level-survey class, or NONE.

### 1.2 Spatial-vs-temporal boundary rule

Spatial structures (channel, band, zone, rectangle as places on the price axis)
receive synonym-graph rows cross-mapped to the level survey's definition
classes; no new level-definition entries are built here. Temporal states
(accumulation as a phase, climax as an event) receive new NA-series definition
entries. The NA namespace does not reuse or extend the predecessor D-series.

### 1.3 PRISMA-ScR partial-conformance statement

Single automated screener (this model); no independent duplicate screening
(ScR item 9's calibration expectation unmet); no critical appraisal of included
sources (item 12, not applicable to a definitional corpus but formally unmet);
not registered (item 24a); data charting performed by the same single agent that
screened (item 10 met only in its single-reviewer degenerate form). Items 1-8,
13-18, 20-22, 25-27 are addressed by the structure of this document and its logs.

## 2. Information sources and methods

<!-- prisma-s-1 -->
One row per executed query, per the regime-definitions convention: `n_records`
is the count actually retrieved and carried into screening, not the platform's
total-hit estimate (Crossref `query.bibliographic` totals are whole-index match
counts and are meaningless as yields; they survive in the raw logs). Zero-yield
rows are retained deliberately - the zeros for one-time framing, value-area
migration, trend-day, and arXiv smart-money-concepts are first-class results
(section 8.2). Verification rows (DOI handle checks, record-level metadata
verification) and the tier-5 WebSearch locator carry `n_records` 0 because
their yields are not bibliographic records.

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-01 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-02 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-03 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-04 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-05 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-06 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-07 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-08 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-09 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-10 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-11 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-12 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-13 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-14 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-15 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-16 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-17 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-18 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-19 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-20 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-21 | 20 |
| Crossref | Crossref REST API (api.crossref.org, query.bibliographic) | 2026-08-24 | swA-crossref-22 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-01 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-02 | 16 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-03 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-04 | 13 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-05 | 9 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-06 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-07 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-08 | 0 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-09 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-10 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-11 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-12 | 13 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-13 | 5 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-14 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-15 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-16 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-17 | 4 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-18 | 0 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-19 | 0 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-20 | 8 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swA-openalex-21 | 4 |
| arXiv | arXiv export API (export.arxiv.org/api/query) | 2026-08-24 | swA-arxiv-01 | 20 |
| arXiv | arXiv export API (export.arxiv.org/api/query) | 2026-08-24 | swA-arxiv-02 | 0 |
| arXiv | arXiv export API (export.arxiv.org/api/query) | 2026-08-24 | swA-arxiv-03 | 4 |
| Semantic Scholar | Semantic Scholar Graph API v1 | 2026-08-24 | swA-s2-01 | 20 |
| Web (tier-5 locator) | Claude Code WebSearch tool | 2026-08-24 | swA-websearch-01 | 0 |
| DOI Handle System | doi.org/api/handles | 2026-08-24 | n/a | 0 |
| Crossref (record-level verification) | api.crossref.org/works/{doi} + export.arxiv.org | 2026-08-24 | n/a | 0 |

<!-- prisma-s-2 -->
No multi-database platform search was used. Each API was queried directly.

<!-- prisma-s-3 -->
No study registries were searched; the constructs under review are not
clinical interventions.

<!-- prisma-s-4 -->
One purposive tier-5 web locator query (swA-websearch-01) targeted the Market
Profile day-type and one-time-framing vocabulary to establish whether any
operational rule circulates above tier 5; its URL yield is logged verbatim.

<!-- prisma-s-5 -->
No systematic citation searching. Known-item verification was performed for the
five dispatch-named candidates (Lo/Mamaysky/Wang 2000; Chang & Osler 1999;
Savin/Weller/Zvingelis; Dawson & Steeley 2003; Caginalp & Laurent 1998) by
direct Crossref bibliographic query rather than by citation chasing.

<!-- prisma-s-6 -->
No contacts made.

<!-- prisma-s-7 -->
Record-level verification: every candidate's DOI was resolved through the DOI
Handle System API (swA-doicheck-01, all 22 responseCode 1) and its
title/venue/year/authors verified against the Crossref works route or the arXiv
export API before inclusion (swA-doicheck-02). Nothing was passed through from
the dispatch or from model memory; the dispatch's venue guess for
Savin/Weller/Zvingelis (Review of Financial Studies) was corrected to the
Journal of Financial Econometrics by this verification.

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S 8: each query exactly as executed, one fence per `query_id`. Bracketed
lines record execution parameters carried in the request URL, not query text.
Raw request URLs and full top-k hit lists are in
[search_logs/regime-naming/](search_logs/regime-naming/), one JSON log per id.

```text swA-crossref-01
trading range technical analysis stock market
```

```text swA-crossref-02
range-bound market
```

```text swA-crossref-03
sideways market
```

```text swA-crossref-04
congestion area price chart technical analysis
```

```text swA-crossref-05
consolidation pattern stock price technical analysis
```

```text swA-crossref-06
rectangle chart pattern stock
```

```text swA-crossref-07
Wyckoff method accumulation distribution trading
```

```text swA-crossref-08
Market Profile Steidlmayer auction value area futures
```

```text swA-crossref-09
Savin Weller Zvingelis head-and-shoulders pattern
```

```text swA-crossref-10
Dawson Steeley visual technical patterns UK stock
```

```text swA-crossref-11
Caginalp Laurent predictive power candlestick patterns
```

```text swA-crossref-12
Marshall Young Rose candlestick technical trading strategies bootstrap
```

```text swA-crossref-13
price gaps stock returns technical analysis opening gap
```

```text swA-crossref-14
selling climax buying climax stock market
```

```text swA-crossref-15
Plastun price gap anomaly stock market
```

```text swA-crossref-16
Bulkowski Encyclopedia of Chart Patterns throwback pullback
```

```text swA-crossref-17
overbought oversold relative strength index stock returns test
```

```text swA-crossref-18
contrary opinion sentiment futures markets test
```

```text swA-crossref-19
Wyckoff accumulation distribution trading
[executed with URL parameter filter=prefix:10.2139 — SSRN-only]
```

```text swA-crossref-20
market profile value area initial balance
[executed with URL parameter filter=prefix:10.2139 — SSRN-only]
```

```text swA-crossref-21
order block fair value gap smart money
[executed with URL parameter filter=prefix:10.2139 — SSRN-only]
```

```text swA-crossref-22
Wong Manzur Chew technical analysis Singapore stock market moving average RSI
```

```text swA-openalex-01
Wyckoff accumulation distribution stock market
[executed in relevance-search mode (?search=), not title_and_abstract.search]
```

```text swA-openalex-02
"Wyckoff method"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-03
"trading range" AND "breakout"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-04
"market profile" AND "value area"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-05
"auction market theory"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-06
"smart money concepts" OR "inner circle trader"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-07
"fair value gap" OR "order block"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-08
"one-time framing" OR "initial balance" AND "market profile"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-09
"fair value gap"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-10
"order block" trading
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-11
"one-time framing"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-12
"selling climax" OR "buying climax"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-13
"key reversal" trading
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-14
"measured move"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-15
"break of structure" OR "change of character" market
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-16
"value area migration" OR "value migration" futures
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-17
"change of character" "smart money"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-18
"value area migration"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-19
"trend day" futures intraday
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-20
"demand zone" "supply zone"
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-openalex-21
"base formation" stock price basing
[executed as filter=title_and_abstract.search, sort=cited_by_count:desc]
```

```text swA-arxiv-01
all:"Wyckoff"
```

```text swA-arxiv-02
all:"smart money concepts"
```

```text swA-arxiv-03
all:"trading range" AND cat:q-fin*
```

```text swA-s2-01
Wyckoff method trading phases detection deep learning
```

```text swA-websearch-01
"one-time framing" market profile definition rule "trend day" "day type" classification
```

<!-- prisma-s-9 -->
No limits were used on language, year, or document type. The SSRN-only queries
(swA-crossref-19/20/21) restricted the Crossref prefix to 10.2139 by design, to
reach the working-paper tier the dispatch names as a platform; this is a scope
extension, not a restriction on the other queries. Retrieval depth was capped
at the top 20 records per query by relevance rank - a pragmatic cap identical
to the predecessor reviews' practice, declared as a coverage limit in section 10.

<!-- prisma-s-10 -->
No published search filters were used; none exist for this vocabulary
(registry section 1.5: no controlled vocabulary covers these terms).

<!-- prisma-s-11 -->
The query vocabulary is drawn verbatim from the registry's variant columns
(vocabulary_regime-synonyms_2026-08-24.md), which is the instrument this sweep
executes; the per-source design follows the predecessor regime-definitions
review's platform conventions.

<!-- prisma-s-12 -->
No updates scheduled; a re-run belongs to a future registry revision.

<!-- prisma-s-13 -->
All queries executed 2026-08-24, in agreement with every `date_searched` cell.

## 4. Peer review of the strategy

<!-- prisma-s-14 -->
Not peer reviewed. No PRESS review of these strategies occurred before
execution; the registry itself (per its section 4, limit 1) is the reviewable
instrument, and this sweep is one of two independent executions against it.
Agent B's concurrent sweep provides no cross-check of these clusters, by the
non-overlap design of the dispatch.

## 5. Managing records

<!-- prisma-s-15 -->
756 records retrieved across 45 bibliographic query executions (see the
prisma-s-1 table; verification and locator rows contribute 0 by definition).
Per-source totals as reported by each platform survive in the JSON logs.

<!-- prisma-s-16 -->
Deduplication: exact-match on DOI, or arXiv id, or lower-cased title where no
identifier was returned, across all retrieval sets, computed by a Python 3.11
stdlib script over the JSON logs (collections.Counter; the logs are the input
of record). 32 cross-query duplicates removed. Predecessor-store overlap is
handled as an eligibility exclusion (criterion 1), not as deduplication.

<!-- prisma-2020-8 -->
- **screeners_n**: 1
- **independent**: no - single screener
- **automation_tools**: Claude Fable 5 (model id claude-fable-5), Claude Code / Claude Agent SDK research-librarian agent, sweep-A dispatch; it decided every screening inclusion and exclusion; no human review of individual decisions

## 6. Excluded records

<!-- prisma-2020-16b -->
Near-misses: records that appeared to meet the criteria and were excluded at
the stated stage, with reasons. The Zenodo content-mill family is recorded once
as a class.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E1 | Anon. (2012). Theoretical Properties of Technical Range and Its Applications. J Stock Forex Trading, doi:10.4172/2168-9458.1000103 | metadata review | OMICS-group venue; peer review unverifiable and full text not retrievable this session; the only located candidate for a formal "technical range" theory, so its exclusion is a recall loss, declared |
| E2 | Anon. (2014). Quantum Tunneling of Stock Price in Range Bound Market Conditions, doi:10.2139/ssrn.2519103 (journal twin doi:10.12785/qpl/030201) | full-record review | range-bound state as a potential-well model: the construct is already covered by prior-corpus arXiv:1304.6846 (level survey); venue of the journal twin weak; adds no assignment rule |
| E3 | Anonymous (2026). Auction Market Theory as an Emergent Property of Inventory Dynamics, doi:10.2139/ssrn.6616280 | metadata review | authorship anonymous in the deposited metadata ("anon M"); provenance unverifiable, per the exclusion criterion on unattributable records |
| E4 | Anon. (2026). Stop Distance, Exit Methodology, and Signal Preservation in Intraday Value Area Breakouts, doi:10.2139/ssrn.6350238 | abstract review | strategy tuning atop the prior value-area class (level-survey D33); no new definition or null |
| E5 | Anon. (2026). Multi-Asset A/A+ Momentum Fair Value Gap Strategy, doi:10.2139/ssrn.6725880 | abstract review | consumes the D68 FVG rule inside a momentum strategy; the included Barot record already carries the FVG statistical evaluation |
| E6 | Anon. (2024). Price Gap Anomaly: Empirical Study of Opening Price Gaps and Price Disparities in Chinese Stock Markets, doi:10.1007/s10690-024-09461-y | abstract review | duplicative of the included Plastun et al. (2020) gap operationalization; same construct, narrower market scope |
| E7 | Zenodo "E8 Intelligence Research" record family (multiple DOIs, e.g. doi:10.5281/zenodo.21912647) | screening | automated LLM content mill mass-depositing video-scout summaries as records; not research output at any tier; excluded as a class |
| E8 | Dalton et al. (2012). Profiting from Market-Generated Information. Markets in Profile ch. 9, doi:10.1002/9781119196709.ch9 | full-record review | the book is already the prior corpus's Market Profile source (level survey, .app1); this chapter adds no operational rule the D32-D36 classes lack |
| E9 | Anon. (2022). Predicting key reversal points through Fibonacci retracements, doi:10.31580/jmi.v9i3.2638 | abstract review | "key reversal" here means retracement targets, not the key-reversal-day event; off-construct homonym |

## 7. Included corpus

<!-- included-corpus -->
Tier codes per the CLAUDE.md evidence hierarchy: T1 peer-reviewed, T5
practitioner/preprint/working-paper (recorded per record; nothing silent).
SSRN 2026 records are unrefereed working papers: T5 despite academic form.

| id | citation | persistent id | role in the argument |
|---|---|---|---|
| savin2006nbl012 | Savin, Weller & Zvingelis (2007). The Predictive Power of "Head-and-Shoulders" Price Patterns in the U.S. Stock Market. J Financial Econometrics 5(2). | 10.1093/jjfinec/nbl012 | T1. NA-01: kernel-regression head-and-shoulders definition (modified Lo-Mamaysky-Wang) with bootstrap inference on excess returns; the dispatch's venue guess corrected |
| dawson2003146859570049 | Dawson & Steeley (2003). On the Existence of Visual Technical Patterns in the UK Stock Market. J Bus Finance Accounting 30(1-2). | 10.1111/1468-5957.00492 | T1. NA-02: LMW pattern definitions re-executed on UK data; pattern-conditioned return distributions tested against unconditional ones - a null-distribution record |
| caginalp1998135048698334 | Caginalp & Laurent (1998). The predictive power of price patterns. Applied Mathematical Finance 5(3-4). | 10.1080/135048698334637 | T1. NA-03: candlestick reversal patterns as computable OHLC-sequence predicates with out-of-sample tests |
| marshall2006jjbankfin200 | Marshall, Young & Rose (2006). Candlestick technical trading strategies: Can they create value for investors? J Banking & Finance 30(8). | 10.1016/j.jbankfin.2005.08.001 | T1. NA-04: candlestick pattern returns tested against a bootstrap null - the null-distribution machinery for pattern-event vocabulary |
| plastun2020jnajef202010 | Plastun, Sibande, Gupta & Wohar (2020). Price gap anomaly in the US stock market: The whole story. NAJEF 52. | 10.1016/j.najef.2020.101177 | T1. NA-05: operational price-gap definition (threshold on open-to-prior-close displacement) with statistical tests and trading-simulation checks; the gap family's academic operationalization |
| simon2001fut4 | Simon & Wiggins (2001). S&P futures returns and contrary sentiment indicators. J Futures Markets 21(5). | 10.1002/fut.4 | T1. NA-07a: contrary-opinion states operationalized as extremes of sentiment indicators with predictive regressions |
| wang2001fut2003 | Wang (2001). Investor Sentiment and Return Predictability in Agricultural Futures Markets. J Futures Markets 21(10). | 10.1002/fut.2003 | T1. NA-07b: contrary-opinion state via trader-position sentiment extremes; tests of the contrarian hypothesis in futures |
| wong2003096031002200 | Wong, Manzur & Chew (2003). How rewarding is technical analysis? Evidence from Singapore stock market. Applied Financial Economics 13(7). | 10.1080/0960310022000020906 | T1. NA-06: RSI overbought/oversold rules stated as computable signals and tested; the oscillator-state family's academic operationalization |
| ha2016290881229088 | Ha, Lee & Moon (2016). A Genetic Algorithm for Rule-based Chart Pattern Search in Stock Market Prices. GECCO 2016. | 10.1145/2908812.2908828 | T1 (refereed conference). NA-08: chart patterns as conjunctions of predicates over price extrema, searched by GA - generic operationalization machinery for the rectangle/range pattern grammar |
| ige2024arxiv240318839 | Pal (2024). Long Short-Term Memory Pattern Recognition in Currency Trading. arXiv:2403.18839 [q-fin.TR]. **[CORRECTION 2026-08-24, audit finding LITERATURE-1-1: sole author is Jai Pal per the arXiv export API; the original prose "Ige (2024)" was a misattribution. The store entry was already correct; the id string `ige2024arxiv240318839` predates this correction and is retained for store stability.]** | 10.48550/arXiv.2403.18839 | T5 (preprint). NA-09: the only located algorithmic Wyckoff-phase assignment - accumulation trading range and secondary test labeled via swing points, classified by CNN/LSTM |
| friday2026access202636 | Friday, Pati, Mishra & Mishra (2026). A Meta-Adaptive Framework Combining Gated Attention Mechanisms and Feature-Wise Modulation for Multi-Horizon Stock Price Movement Prediction. IEEE Access. | 10.1109/access.2026.3663386 | T1 (weak venue, declared). NA-14: peer-reviewed statement of the FVG "deterministic three-bar imbalance rule" plus order-block features - academic confirmation of the level survey's code-derived D68/D66 rules |
| barot2026ssrn7148099 | Barot (2026). Fair Value Gaps Work - Until You Try to Trade Them. SSRN. | 10.2139/ssrn.7148099 | T5 (working paper). NA-15: statistical evaluation of FVG fill behavior versus tradability - the closest located thing to a null-distribution treatment of an ICT construct |
| subedi2024sudurpaschim | Subedi, Shahi & Bhatt (2024). Efficacy of Technical Analysis to Assess Fair Value Gap: Evidence from Nepalese Commercial Banks. Sudurpaschim Spectrum 2(2). | 10.3126/sudurpaschim.v2i2.80419 | T1 (venue quality unverifiable, declared). NA-16: the only located journal-published direct FVG efficacy test |
| tolusic2026ssrn7135258 | Tolusic (2026). Initiative and Responsive: Auction Market Theory at the Signed Tape. SSRN. | 10.2139/ssrn.7135258 | T5 (working paper). NA-17: initiative/responsive activity operationalized on signed trades - the first located computable rule for this auction-state pair |
| perry2026ssrn7106618 | Perry (2026). Beyond the Boundary: Structure, Signal, and Robustness in Failed Auction Reversion at Daily Value Area Extremes. SSRN. | 10.2139/ssrn.7106618 | T5 (working paper). NA-18: value-area edge events ("failed auction") given an operational rule with robustness analysis; also the saturation flag for the unregistered term "failed auction" |
| lamanna2026ssrn6974102 | La Manna (2026). Reframing TPO as an Estimator of Moments and Entropy of Equity Markets. SSRN. | 10.2139/ssrn.6974102 | T5 (working paper). NA-19: the TPO/profile construct restated as a statistical estimator - the only located formalization of the TPO beyond vendor documentation |
| moustafa2026ssrn6854685 | Moustafa, Neagu & Kalita (2026). ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading. SSRN. | 10.2139/ssrn.6854685 | T5 (working paper). NA-20: auction-market-theory states encoded as order-flow features for RL - algorithmic operationalization of balance/imbalance vocabulary |
| anon2012978111919682 | Pruden (2007; online 2012). The Wyckoff Method of Technical Analysis and Speculation. In The Three Skills of Top Trading. Wiley. | 10.1002/9781119196822.ch6 | T5 (practitioner). NA-10a: canonical narrative-operational statement of the Wyckoff phases and events; no numeric bounds |
| weis2013978111865638 | Weis (2013). Trades About to Happen: A Modern Adaptation of the Wyckoff Method. Wiley. | 10.1002/9781118656389 | T5 (practitioner). NA-10b: chapter-level treatment of springs, upthrusts, absorption - the event vocabulary's most explicit practitioner statement; also the saturation flag for "absorption" |
| anon2012978047042841 | Schannep (2008; online 2012). Capitulation: The Selling Climax. In Dow Theory for the 21st Century. Wiley. | 10.1002/9780470428412.ch8 | T5 (practitioner). NA-11: the one located source that quantifies a selling-climax/capitulation event rule |
| anon2012978111920353 | Bulkowski (2012). Visual Guide to Chart Patterns. Wiley (Bloomberg Financial). | 10.1002/9781119203537 | T5 (practitioner). NA-12: throwback/pullback and measured-move rules with empirical frequency statistics - the only located quantified treatment of those events |
| anon2007978142001314 | Edwards & Magee (2007, 9th ed.). Consolidation Formations. In Technical Analysis of Stock Trends. CRC. | 10.1201/9781420013146.ch11 | T5 (practitioner). NA-13: the canonical rectangle/consolidation/Dow-line chapter - the definitional root the academic operationalizations point back to |

## 8. Synthesis

### 8.1 Per-cluster verdicts

**Cluster 1 - range/consolidation (trading range, range-bound, consolidation,
rectangle, Dow line, congestion, base, sideways, tight range).** Operational
definitions exist at two poles and almost nothing between: the practitioner
canon (NA-13) defines the shapes without numeric bounds, and the academic pole
operationalizes only two members - the rectangle (via the prior-corpus
Lo-Mamaysky-Wang kernel definitions, level-survey coverage) and the trading
range implicitly via the trading-range-break rule (prior corpus: Brock et al.
1992, level-survey D76). NA-08 supplies generic rule-grammar machinery. No
null distribution attaches to "the market is range-bound" as a state
assignment anywhere located; the sideways-state exceptions (arXiv options
papers; the five-state HSMM "Sidewalk" paper) are all prior coverage. Verdict:
definitions partial, nulls NONE (new), academic operationalizations
prior-covered.

**Cluster 2 - Wyckoff.** Phase and event vocabulary is defined narratively at
tier 5 (NA-10a/b); exactly one algorithmic operationalization located (NA-09,
preprint, accumulation phases only). No null distribution or statistical test
of Wyckoff phase existence or assignment exists at any tier located this
session. The UTAD/SOS/SOW/LPS/PSY event acronyms have no academic literature
at all. Verdict: definitions tier-5 plus one preprint; nulls NONE; academic
operationalization one preprint.

**Cluster 3 - auction/Market Profile.** The spatial constructs (value area,
POC, initial balance, TPO, volume nodes) are prior-covered by level-survey
classes D32-D36/D08-D09. The temporal state vocabulary was the gap, and it is
now partially filled only at working-paper tier: initiative/responsive (NA-17),
balance/imbalance via order-flow features (NA-20), value-area edge events
(NA-18), TPO formalization (NA-19). Day types, one-time framing, and value-area
migration have zero records above tier 5 - three deliberate zero-yield queries
plus the tier-5 locator log document this. Verdict: definitions tier-5 and
working-paper only; nulls NONE; peer-reviewed operationalizations NONE.

**Cluster 4 - ICT/smart-money.** The level survey's code-derived D65-D72 rules
remain the operational core. New this sweep: a peer-reviewed venue now states
the FVG three-bar rule and order-block features (NA-14), one journal test of
FVG efficacy exists at an unverifiable-quality venue (NA-16), and one working
paper statistically evaluates FVG fill behavior (NA-15). Premium/discount/
equilibrium: nothing beyond prior D62 at any tier. arXiv carries zero records
for "smart money concepts". Verdict: definitions prior-covered (code) plus one
peer-reviewed confirmation; nulls approaching existence at working-paper tier;
academic operationalizations beginning to appear (2024-2026).

**Cluster 5 - chart-pattern events.** The strongest cluster. Known-items
verified and included: NA-01 (head-and-shoulders with bootstrap inference),
NA-02 (UK patterns against unconditional-distribution nulls), NA-03/NA-04
(candlestick predicates; bootstrap null), NA-05 (gap operationalization with
tests). Prior coverage: Lo-Mamaysky-Wang 2000 and Chang & Osler 1999 (both in
the level-definitions store). Key reversal day: NONE above tier 5 (one
off-construct homonym excluded, E9). Climax/blowoff: one quantified
practitioner rule (NA-11), no academic test; the bare phrase is untestable in
query form (Crossref drowns it in the geology of Nevada's Climax granite
stock - a new homonym-collision for the registry ledger). Throwback and
measured move: tier-5 quantification only (NA-12). BOS/CHoCH: prior D72;
nothing new above tier 5. Verdict: definitions and nulls FOUND (this is where
the null-distribution tradition lives); events outside the classic patterns
remain tier-5 only.

**Cluster 6 - sentiment/press states.** Overbought/oversold: operational RSI
rules tested in a peer-reviewed venue (NA-06); the 70/30 thresholds themselves
remain folklore constants with no derivation - consistent with the project's
zero-arbitrary-thresholds finding pattern. Contrary opinion: two peer-reviewed
operationalizations with predictive tests (NA-07a/b). Verdict: definitions
FOUND (T1); nulls partial (regression-based tests, no explicit null-model
construction); academic operationalizations FOUND.

### 8.2 Zero-yield results (first-class)

| query | term family | result |
|---|---|---|
| swA-openalex-11 / -19 and swA-websearch-01 | one-time framing, trend day, day types | no records above tier 5; operational rules exist only in vendor/trader glossaries |
| swA-openalex-18 | value area migration | zero records on any platform |
| swA-arxiv-02 | smart money concepts | zero arXiv records |
| swA-openalex-12 (screened) | selling/buying climax | no academic operationalization; one practitioner quantification (NA-11) |
| swA-openalex-13 (screened) | key reversal | no on-construct records above tier 5 |
| swA-openalex-20 / -21 (screened) | supply/demand zone, base/basing | no financial-market records at all - both terms resolve to NONE |

### 8.3 Synonym graph

Columns per dispatch: the operational definition resolves to an NA-id, a
level-survey class (LS-D series of lit_review_level-definitions_2026-08-21.md),
or NONE. Null-distribution status: FOUND (a test exists), PARTIAL (tests of
return effects but not of construct existence), NONE. Tier is the best tier at
which any operational definition of the term was located.

| term | construct it names | tradition | operational definition located | null-distribution status | evidence tier |
|---|---|---|---|---|---|
| trading range | bounded lateral price interval (state and place) | classical TA / Wyckoff | LS-D76 (bounds as n-period extrema, prior); NA-13 (shape); NA-09 (Wyckoff TR labeling) | PARTIAL - Brock et al. bootstrap on the break rule (prior), none on the state itself | 1 (prior) |
| range-bound (market) | the same interval as a temporal state | practitioner | NONE new; prior arXiv:1304.6846 models it (level survey) | NONE | 5 |
| range trading / ranging market | trading within the state | practitioner | NONE | NONE | 5 |
| consolidation | pause/lateral formation in a trend | classical TA | NA-13 (non-numeric); NA-08 (rule-grammar machinery) | NONE | 5 |
| rectangle | parallel-bound consolidation shape | classical TA | prior LMW RTOP/RBOT kernel definitions (level survey); NA-13 | FOUND (prior LMW conditional-distribution tests; NA-02 UK re-test) | 1 (prior) |
| line (Dow Theory) | narrow multi-week range in the averages | Dow Theory | NA-13 restates; bare term unqueryable (homonym); no dedicated record | NONE | 5 |
| congestion area / congestion zone | traded-over region | classical TA | NONE (query drowned by traffic/power-grid homonyms; nothing on-construct retrieved) | NONE | 5 |
| base / basing | post-decline consolidation | practitioner | NONE | NONE | 5 |
| sideways market | directionless temporal state | classical TA | prior: arXiv:2006.14121 and the FRL "Sidewalk" HSMM state (method-gaps store) | PARTIAL (prior HSMM model comparison) | 1 (prior) |
| tight trading range / narrow range | compressed range | practitioner | prior LS-D64: the source explicitly declines to bound it | NONE | 5 |
| non-trending / trendless | state by negation | practitioner | NONE (defined only as complement) | NONE | 5 |
| channel | sloped parallel-bound region | classical TA | prior LS-D59 (Donchian) and kernel channels (level survey) - cross-map only | PARTIAL (prior) | 1 (prior) |
| band / trading band | volatility-scaled envelope | volatility trading | prior LS-D56-D58 - cross-map only | NONE | 1 (prior) |
| corridor | synonym of channel/band | thin | NONE anywhere; no financial record retrieved | NONE | none located |
| zone | tolerance region around a level | retail TA | prior LS-D62 (premium/discount) et al. - cross-map only | NONE | 5 |
| supply zone / demand zone | origin regions of impulsive moves | retail TA / Wyckoff root | NONE at any tier this sweep | NONE | 5 (existence only) |
| accumulation (phase) | smart-money buying range before markup | Wyckoff | NA-09 (algorithmic, preprint); NA-10a/b (narrative) | NONE | 5 / preprint |
| distribution (phase) | selling range before markdown | Wyckoff | NA-10a (narrative only; bare phrase query unusable - probability collision confirmed) | NONE | 5 |
| markup / markdown | trending phases between ranges | Wyckoff | NA-10a (narrative) | NONE | 5 |
| spring / shakeout | terminal sub-range false breakdown | Wyckoff | NA-10b (Weis ch. 5, narrative-operational) | NONE | 5 |
| upthrust / UTAD | terminal false breakout above range | Wyckoff | NA-10b (Weis ch. 6) | NONE | 5 |
| test / secondary test (ST) | return toward a prior extreme on lower volume | Wyckoff | NA-09 (labeled explicitly in the preprint); NA-10a | NONE | preprint |
| sign of strength / sign of weakness (SOS/SOW) | impulsive confirmation moves | Wyckoff | NA-10a (narrative) | NONE | 5 |
| last point of support / supply (LPS/LPSY) | last pullback before trend | Wyckoff | NA-10a (narrative) | NONE | 5 |
| preliminary support / supply (PS/PSY) | first counter-pressure in a trend | Wyckoff | NA-10a (narrative) | NONE | 5 |
| automatic rally / automatic reaction | first bounce after climax | Wyckoff | NA-10a (narrative) | NONE | 5 |
| phases A-E | ordered sub-stages of a Wyckoff range | Wyckoff | NA-10a; NA-09 operationalizes a subset | NONE | 5 / preprint |
| bull trap / bear trap | failed breakout that reverses | Wyckoff / general TA | NONE beyond narrative | NONE | 5 |
| line of least resistance | direction of pending breakout | Wyckoff/Livermore | NONE | NONE | 5 |
| balance / balanced market | two-sided rotational auction state | auction-MP | NA-20 (order-flow features, working paper); vendor rules otherwise | NONE | 5 |
| imbalance (auction sense) | one-sided directional auction state | auction-MP | NA-20; collision ledger confirmed (order-flow imbalance is prior LS-D43-D44 ground) | NONE | 5 |
| rotation / rotational market | alternating directional auctions | auction-MP | NA-17 partially (responsive/initiative alternation) | NONE | 5 |
| price discovery (market-state sense) | directional exploration for value | auction-MP | NONE distinct from the microstructure-efficiency homonym; no record defines it as a STATE above tier 5 | NONE | 5 |
| initiative (buying/selling) | activity away from value | auction-MP | NA-17 (signed-tape rule, working paper) | NONE | 5 |
| responsive (buying/selling) | activity back toward value | auction-MP | NA-17 | NONE | 5 |
| day type (trend/neutral/normal/non-trend day) | daily auction taxonomy | Market Profile | NONE above tier 5 (zero-yield queries + tier-5 locator log) | NONE | 5 |
| one-time framing (OTF) | directional bar-sequence condition | Market Profile | NONE above tier 5; tier-5 rule: consecutive higher lows (up) / lower highs (down) | NONE | 5 |
| value area migration | day-over-day drift of the value area | Market Profile | NONE at any tier (zero records) | NONE | none located |
| value area / VAH / VAL | central 70% traded region | Market Profile | prior LS-D33 - cross-map; NA-19 reframes statistically | NONE | 5 (prior) |
| point of control / POC | modal TPO/volume price | Market Profile | prior LS-D32 - cross-map | NONE | 5 (prior) |
| initial balance | first-hour range | Market Profile | prior LS-D08-D09 - cross-map | PARTIAL (prior opening-range-breakout tests) | 1 (prior) |
| range extension | auction beyond the initial balance | Market Profile | NONE new; vendor rules only | NONE | 5 |
| single prints / excess / buying tail / selling tail | rejection structures in the profile | Market Profile | NONE above tier 5 | NONE | 5 |
| failed auction | rejected probe of a value-area extreme | Market Profile (UNREGISTERED TERM) | NA-18 (working paper) | PARTIAL (robustness analysis, working paper) | 5 |
| TPO | time-price opportunity cell | Market Profile | prior LS-D34 - cross-map; NA-19 | NONE | 5 (prior) |
| volume node (HVN/LVN) | high/low volume prices | volume profile | prior LS-D35 - cross-map | NONE | 5 (prior) |
| long liquidation / short covering | positioning-unwind day types | Market Profile | NONE above tier 5 | NONE | 5 |
| open types (open-drive, open test-drive, open rejection-reverse, open auction) | opening auction taxonomy | Market Profile | NONE above tier 5 | NONE | 5 |
| spike (Market Profile sense) | late impulsive move left unvalidated | Market Profile / E&M | NONE above tier 5 | NONE | 5 |
| auction / two-way auction | the market process the states describe | Steidlmayer/Dalton | NA-20/NA-17 operationalize derived states; the process itself defined narratively | NONE | 5 |
| order block | last opposing candle before impulse | ICT | prior LS-D65-D67 (code) - cross-map; NA-14 uses as features (peer-reviewed) | NONE | 1 (as features) |
| fair value gap / FVG / imbalance (ICT) / inefficiency | three-bar displacement void | ICT | prior LS-D68-D69 (code); NA-14 (peer-reviewed three-bar rule); NA-16 | PARTIAL - NA-15 fill-rate evaluation (working paper) | 1 |
| premium / discount / equilibrium | halves of a dealing range | ICT | prior LS-D62 (code) - cross-map only; nothing new at any tier | NONE | 5 (prior) |
| break of structure / BOS | continuation break of a swing extreme | retail smart-money | prior LS-D72 (code) - cross-map | NONE | 5 (prior) |
| change of character / CHoCH | first counter-trend structure break | retail smart-money | prior LS-D72 - cross-map; only content-mill records new | NONE | 5 (prior) |
| selling climax / buying climax / blowoff | terminal panic/euphoria volume event | E&M / Wyckoff | NA-11 (quantified, practitioner) | NONE | 5 |
| capitulation | press synonym of selling climax | press | NA-11 | NONE | 5 |
| key reversal (day) / one-day reversal | single-bar reversal event | classical TA | NONE above tier 5 | NONE | 5 |
| measured move | projected repeat of a prior swing | classical TA | NA-12 (rule + frequencies, practitioner) | NONE | 5 |
| throwback / pullback (pattern sense) | post-breakout return to the boundary | classical TA | NA-12 (rule + frequencies) | NONE | 5 |
| gap (taxonomy: breakaway/runaway/exhaustion/common/area) | open beyond the prior bar's range | classical TA | NA-05 (threshold operationalization + tests) | FOUND (NA-05 statistical tests) | 1 |
| island reversal | gapped-off price cluster | classical TA | NONE academic; narrative in E&M (prior chapter DOIs) | NONE | 5 |
| head-and-shoulders | three-peak reversal pattern | classical TA | NA-01 (kernel definition); prior Chang & Osler (level survey) | FOUND (NA-01 bootstrap; prior C&O simulated null) | 1 |
| candlestick reversal patterns | OHLC-sequence events | Japanese charting | NA-03 (predicates); NA-04 | FOUND (NA-04 bootstrap null) | 1 |
| overbought / oversold | oscillator-extreme state | oscillator tradition | NA-06 (RSI rules, tested) | PARTIAL (profitability tests; the 70/30 constants underived) | 1 |
| contrary opinion | fade-the-consensus sentiment state | futures tradition | NA-07a/b (indicator extremes + regressions) | PARTIAL | 1 |

Row count: 67.

### 8.4 New families flagged for the saturation check

Terms encountered this sweep that are in NEITHER the registry NOR the seed
list (flagged for the registry's next revision, per dispatch):

1. **failed auction** (Market Profile event; NA-18's core construct).
2. **absorption** (Wyckoff-adjacent event; a chapter title in Weis 2013).
3. **liquidity void** (ICT; used in the NA-14 abstract as the FVG's referent).
4. **Judas swing** (ICT session-open false move; attested only in content-mill
   titles, hence provenance-weak, but absent from the registry).
5. **inversion fair value gap / IFVG** (ICT; an FVG acting with reversed
   polarity after being traded through - structurally parallel to the
   registry's breaker-block row but unregistered).
6. **midnight opening gap (MNOG)** (ICT session construct; one Zenodo
   feasibility deposit).
7. **technical range** (as a theorized construct; E1's title term - excluded
   record, but the term itself is not a registry surface form).
8. Registry collision-ledger addition: "selling climax" collides with the
   geological literature of the Climax stock (granite, Nevada) on
   bibliographic platforms; "one-time framing" fails hyphen-sensitive phrase
   matching on OpenAlex.

### 8.5 Method observation for the registry

The OpenAlex `title_and_abstract.search` OR-syntax silently degrades with
quoted phrases (three malformed executions, retained and re-run); phrase
queries there should be issued one phrase per query. Hyphenated registry
variants ("one-time framing") failed to phrase-match at all - the sweep's
morphological-variant warrant (F005) extends to hyphen handling on OpenAlex.

## 9. Bibliography store

<!-- bibliography-store -->
- Store: `references_regime-naming-A.json` (CSL-JSON, canonical; 22 entries)
- SHA-256: `a83bf3e887192a1f30667c8df1ff768abb2b368d2d06d07f56cebbc6b27223d2` - equals frontmatter `bibliography_sha256`
- Derived exports (regenerable; never a source of truth):
  `python ~/.claude/scripts/build_bibliography.py export <store> --format bibtex|ris`

## 10. Limitations and verification gaps

1. **Semantic Scholar effectively unavailable.** One query executed
   (swA-s2-01, poor phrase relevance), one blocked by persistent HTTP 429
   (swA-s2-02, logged); the platform contributed nothing screenable.
   Severity minor for coverage (Crossref/OpenAlex overlap) but declared.
2. **Screening was title/abstract/metadata-level.** No full texts were
   retrieved; practitioner-book records are included on verified chapter
   metadata plus the registry's TOC harvest, and their operational content is
   characterized only to the depth those sources state. E1's exclusion
   (unretrievable full text, unverifiable venue) is a declared recall loss.
3. **SSRN 2026 working papers are unrefereed** and of unestablished
   provenance; all five included ones have named authors and resolving DOIs,
   but none has a citation record. They are load-bearing only for the claim
   that operationalizations exist at working-paper tier, never for their
   findings' correctness.
4. **Coverage declared, not complete.** Of the registry's ~540 surface forms,
   this sweep executed 45 bibliographic queries prioritizing head terms and
   the variants most likely to differ. Not executed as standalone queries:
   the individual Wyckoff event acronyms (UTAD, SOS, SOW, LPS, LPSY, PS, PSY,
   AR) beyond their parent-term queries; the Market Profile open types and
   long-liquidation/short-covering forms; "island reversal", "blowoff",
   "runaway day" and most gap-subtype names; "premium zone"/"discount zone"
   as standalone phrases; "ranging market", "range trading", "congested
   market" word-order variants; the Dow-Theory "line" (unqueryable bare -
   homonym); non-English forms (none registered). Each unexecuted variant is
   a potential recall gap of exactly the F005 class this session exists to
   fix; the declaration here is the mitigation.
5. **Homonym drowning.** Two queries (swA-crossref-04, -14) were dominated by
   out-of-domain homonyms despite conjunctive context terms; their zero
   on-construct yield is evidence of absence only in the weak,
   query-conditional sense.
6. **Single screener, no PRESS review** (sections 1.3, 4). The synonym graph's
   NONE verdicts are one model's screening judgments over top-20 retrieval
   sets and are falsifiable by deeper retrieval.
7. **Filename-case deviation from the dispatch.** The dispatch named the
   deliverables with a capital A (regime-naming-A); the G1 gate's slug grammar
   is lowercase-only, so the review file and slug use `regime-naming-a` while
   the bibliography store keeps the dispatch's exact
   `references_regime-naming-A.json` name. Declared here so neither name
   appears unexplained.
8. **No new records for Agent B's clusters** were screened in, per the
   non-overlap design; boundary terms (sideways as a temporal state, spike)
   are cross-mapped here only where the registry assigns them to a sweep-A
   family.

### 10.9 Gate verdict: `block`, on G16 findings only, all in the closed publisher-403 class

The research-compile G1-G20 gate was executed against this file twice on
2026-08-24. Every assertion except G16 passed in both runs: no G1-G15 and no
G17-G20 findings. The verdict is `block` solely on G16 identifier-resolution
findings: run 1 reported 12 (11 `HTTP 403`, one `network unavailable` on
10.1201/9781420013146.ch11); run 2, after this section was added, reported 11 -
the Schannep chapter DOI (10.1002/9780470428412.ch8) that was `HTTP 403` in
run 1 resolved cleanly in run 2. That run-to-run flip is itself direct evidence
that the failing component is the probe, not the identifiers.

All are false positives of the probe method, per the identical dispositions
in section 10 of every predecessor review and the closed-class ruling in
[deliverable_spec_naming-sweep_2026-08-24.md](../deliverables/deliverable_spec_naming-sweep_2026-08-24.md)
(line: "G16 publisher-403 class stays closed (handle-API test); logged").
Independent evidence, logged in
[search_logs/regime-naming/swA-g16-disposition.json](search_logs/regime-naming/swA-g16-disposition.json)
and [swA-doicheck-01.json](search_logs/regime-naming/swA-doicheck-01.json):

- **DOI Handle System API** (`https://doi.org/api/handles/{doi}`), the
  authoritative resolution test per the dispatch's DOI rule: all 12 return
  `responseCode: 1` (handle exists and resolves).
- **Browser-user-agent GET** to `https://doi.org/{doi}`: 11 of 12 return
  HTTP 403 **from the publisher host after doi.org had already redirected
  there** (Wiley x7, Taylor & Francis x2, OUP x1, ACM x1) - possible only if
  resolution succeeded; the 403 is the publisher's landing-page bot policy.
  The twelfth (CRC/Taylor & Francis, 10.1201/9781420013146.ch11) timed out at
  the publisher host on this network while its handle record resolves with
  `responseCode: 1`.

No identifier in the store is altered on the basis of these findings. The gate
verdict is reported verbatim; the class is disposed, not waived silently.
