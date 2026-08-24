---
title: "Naming-conventions re-sweep, Agent B (academic clusters): bull/bear extensions, business-cycle vocabulary on markets, crisis/stress states, volatility states, trend events, runs, directional change, and regime-noun synonym probes"
slug: regime-naming-b
date: 2026-08-24
objective: "Execute, from the term registry vocabulary_regime-synonyms_2026-08-24.md, the academic-cluster arm of the naming-conventions recall sweep: for each swept synonym family, locate (a) operational definitions (computable state-assignment rules) not already in the five predecessor corpora, (b) published null distributions or existence/assignment tests, and (c) explicit synonym evidence that two surface terms name the same construct; record every query verbatim with counts, treat zero-record queries as first-class results, and flag synonym families absent from both the registry and the seed list."
review_type: scoping
standard_declared: "PRISMA-ScR (Tricco et al. 2018, doi:10.7326/M18-0850) - PARTIAL COMPLIANCE, single screener, adapted to a definitional/vocabulary corpus; item-by-item conformance in section 1.4. Search reporting follows PRISMA-S conventions where applicable."
eligibility_inclusion:
  - "Any source stating an operational definition (a rule an implementer could execute or a reader could audit) for a market-state construct in the Agent-B clusters: bull/bear extensions (secular, correction, capitulation, top/bottom, crash, downturn), business-cycle vocabulary applied to markets, crisis/stress states, volatility states, trend events (breakout beyond prior coverage, parabolic move, momentum burst, trend day), runs/drift/persistence, directional-change/intrinsic-time states, and regime-noun synonyms (state/phase/mode/environment/condition/episode)."
  - "Any source attaching a null distribution, reference distribution, or existence/assignment test to a construct in these clusters (including the pure-probability apparatus for runs and drawdowns)."
  - "Any source providing explicit synonym evidence: text or title-level usage establishing that surface term X and surface term Y name the same construct."
  - "Any language; any year; journal article, conference paper, book or chapter, preprint, working paper, or official documentation, provided a persistent identifier exists."
eligibility_exclusion:
  - "Records already included in any of the five predecessor stores (references_regime-definitions.json, references_regime-classification.json, references_level-definitions.json, references_regime-method-gaps.json, references_f005-class-n-tests.json): cited as prior coverage, never re-included, by task directive."
  - "Agent A's clusters (TA-spatial, range/consolidation, Wyckoff, Market Profile/auction, retail smart-money, chart-pattern events, sentiment/overbought-oversold), excluded by the sweep's division of ground."
  - "Applications of a predecessor-corpus definition to a new market with no definitional novelty, and records retrieved on homonym collisions (regime change in politics, market mode in electricity markets, labor-market conditions, and similar)."
  - "Records whose definitional content could not be verified at any retrievable depth (no abstract at any queried platform and no working-paper twin), where inclusion would require completion from compiler memory."
  - "Records duplicating an already-retained work under a second identifier; handled by deduplication, enumerated in the ledger in section 5."
registration: not-registered
protocol_path: none
protocol_amendments: "Eligibility criteria and the cluster boundary with Agent A were fixed by the dispatch before the first query. Conduct events recorded rather than backdated: (i) swB-crossref-08 received HTTP 429 from Crossref; the attempt is logged as executed with zero records and re-run verbatim as swB-crossref-08b; (ii) both Semantic Scholar discovery queries (swB-s2-01, swB-s2-02) were rate-limited (HTTP 429) and are logged as executed with zero records - a recall verification gap, severity minor, recorded in section 10; (iii) the dispatch spelled the output slug 'regime-naming-B'; the G1 gate constrains review slugs to lowercase, so the review file uses 'regime-naming-b' while the bibliography store retains the dispatch's spelling references_regime-naming-B.json."
bibliography: docs/literature/references_regime-naming-B.json
bibliography_sha256: a42f838805ab5769dfaa73b2ad7157866a493fb9aeb114bae225636d0480a347
n_identified: 303
n_duplicates_removed: 37
n_screened: 266
n_excluded: 235
n_included: 31
materials_availability:
  - docs/literature/search_logs/regime-naming/
  - docs/literature/references_regime-naming-B.json
competing_interests: none
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent, sweep Agent B dispatch) designed and executed every search, screened every record, extracted and classified every entry, and drafted this review. It is the sole screener and is declared as an automation tool under PRISMA-ScR item 9 / PRISMA 2020 item 8. No human second screener participated."
git_head_at_authoring: "0845acbf5d464cd330c93941c3af1bf000f3791d"
pip_freeze_sha256: "n/a - no analysis code was executed; only metadata-retrieval scripts (Crossref, arXiv, OpenAlex, Semantic Scholar, DOI Handle System API, one WebFetch of a RePEc abstract page) and the bibliography-store script"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-fable-5"
---

# Naming-conventions re-sweep, Agent B: academic clusters

## 1. Objective, instrument, and eligibility

### 1.1 What this sweep is

The term registry
([vocabulary_regime-synonyms_2026-08-24.md](vocabulary_regime-synonyms_2026-08-24.md))
was built because the 59-definition regime-definitions survey under-recalled:
its query vocabulary was seeded from academic state-terms, and morphological
variants have twice defeated phrase queries in this project (F005; the
regime-definitions section 8.2 finding). This review executes the registry's
variants for the **academic clusters** assigned to Agent B by the dispatch:

1. bull/bear directional-state family beyond the definitions survey (secular /
   primary / secondary, correction, bear-market rally, capitulation, top /
   bottom, crash, downturn);
2. business-cycle state vocabulary applied to markets (not the macro dating
   algorithms, which are prior coverage);
3. crisis/stress states (crisis/calm, stress/normal, fragile, risk-on/risk-off,
   flight-to-quality);
4. volatility states (volatility regime, squeeze/compression at the academic
   tier, turbulent/quiet);
5. trend-event vocabulary (trading-range breakout beyond Brock, Lakonishok &
   LeBaron 1992, parabolic move, momentum burst, trend day);
6. statistical sequence vocabulary (runs, drift, persistence, local trend),
   with Fama 1965 as the known item to verify and trace;
7. the directional-change / intrinsic-time framework beyond the three records
   the definitions survey already holds (D54-D56);
8. "regime" synonyms as search vocabulary (market state / phase / mode /
   environment / condition / episode), logging which surface unique records.

A sibling Agent A swept the practitioner clusters concurrently; its ground
(TA-spatial, range/consolidation, Wyckoff, Market Profile/auction, retail
smart-money, chart-pattern events, sentiment) is excluded here and its logs
(`swA-*`) share the same directory.

Per family, the objective is threefold: **(a)** operational definitions not in
the predecessor corpora; **(b)** published null distributions or
existence/assignment tests; **(c)** explicit synonym evidence.

### 1.2 Diff discipline

Every candidate was diffed against the union of identifiers in the five
predecessor stores (288 identifiers extracted programmatically on 2026-08-24
before screening began). Prior coverage is cited by its predecessor entry
number (D-, P-, or store id), never re-included. Notable prior-coverage
records this sweep re-retrieved and excluded: Maheu & McCurdy (SSRN twin of
D21), Lunde & Timmermann (P04), Fabozzi & Francis 1977 (D01-D03), the
trading-range-breakout ETF study (level corpus, doi:10.1142/s242478632250027x),
and the opening-range-breakout algorithm paper (level corpus,
doi:10.5121/ijci.2016.5107).

### 1.3 What counts as an operational definition, and record roles

The regime-definitions survey's standard is inherited: a definition is
operational if a competent implementer could assign a state label without a
further interpretive decision the source leaves open; unbound parameters are
marked `CONVENTION`; visual-judgment rules and name-only vocabularies do not
qualify. Because this sweep's objective (b) covers pure statistical apparatus,
each included record carries a **role**: `definition` (states an assignment
rule), `null-apparatus` (states a reference distribution or test), or
`synonym-evidence` (attests that two terms name one construct). One record can
carry more than one role.

### 1.4 Conformance statement - single-screener scoping review

> The charter requires dual independent screening. A single agent cannot
> satisfy it, and two passes by the same model are not independent - an
> agreement statistic between them would measure decoding variance, not
> reliability. This review therefore declares **PRISMA-ScR partial compliance,
> single screener**, the same posture as the five predecessor corpora.

Unmet items, named: item 9 (dual selection - one screener, an automation tool,
declared in section 5), item 10 (dual charting - single extractor, extraction
depth flagged per record as abstract-verified, twin-abstract-verified, or
metadata-only), items 12/16 (no validated appraisal instrument exists for
definitional records; the evidence tier is a labelling, not an appraisal), and
any inter-rater statistic. Item 5: not registered, no protocol; amendments are
in the frontmatter, not backdated. All other PRISMA-ScR items are met in the
adapted form the predecessor reviews use (sections 2-10 below).

**Retrievability bias.** The bias that threatens this sweep is retrievability:
Elsevier journal records frequently carry no abstract on any queried API, and
definitional content then had to be verified through working-paper twins
(section 2). Where no twin existed the record was excluded rather than
completed from memory; section 6 records each such case.

## 2. Information sources and methods

<!-- prisma-s-1 -->
One row per executed discovery query. `n_records` is the number of records
actually retrieved and carried into screening, not the total-hit count the API
reported; total-hit counts survive in the raw logs
([search_logs/regime-naming/](search_logs/regime-naming/), files prefixed
`swB-`). Zero-record rows are retained deliberately: the Crossref 429
(swB-crossref-08), both Semantic Scholar 429s, and four informative arXiv
zeros (section 8.4).

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-01 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-02 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-03 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-04 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-05 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-06 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-07 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-08 | 0 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-08b | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-09 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-10 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-11 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-12 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-13 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-14 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-15 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-16 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-17 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-18 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-19 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-20 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-21 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-24 | swB-crossref-22 | 8 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-01 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-02 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-03 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-04 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-05 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-06 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-07 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-08 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-09 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-10 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-11 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-12 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-13 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-14 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-15 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-16 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-17 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-18 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-19 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-24 | swB-ki-20 | 3 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-01 | 2 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-02 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-03 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-04 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-05 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-06 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-07 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-24 | swB-arxiv-08 | 2 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-01 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-02 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-03 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-04 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-05 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-24 | swB-openalex-06 | 10 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-08-24 | swB-s2-01 | 0 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-08-24 | swB-s2-02 | 0 |

Sum of `n_records` = **303** = frontmatter `n_identified`. Subtotals: Crossref
topical 176 across 23 queries (one 429 zero); Crossref known-item 60 across 20
queries; arXiv 7 across 8 queries (four zeros); OpenAlex 60 across 6 queries;
Semantic Scholar 0 across 2 queries (both rate-limited, recorded as executed).

**Metadata backfills that are not discovery queries** (they identified no new
records; each is logged in the same directory): `swB-abstracts-01.json`
(Crossref GET per candidate DOI), `swB-abstracts-02.json` (OpenAlex abstract
reconstruction), `swB-abstracts-03.json` (Semantic Scholar per-paper GETs; all
returned no abstract for the Elsevier records), `swB-abstracts-04.json`
(working-paper twins: SSRN 886119 for Baur & Lucey; IMF 10.5089/9781557755308.001
for De Bock & de Carvalho Filho; NBER w9817 for Edwards et al.; Bank of Canada
10.34989/swp-2003-14 for Illing & Liu), one WebFetch of the RePEc abstract page
`ideas.repec.org/a/eee/finsta/v32y2017icp30-56.html` for Duprey, Klaus &
Peltonen (2017), and `swB-doicheck-01.json` (DOI Handle System resolution for
all 31 store entries, all responseCode 1). WebSearch was not used: every
included record was reachable through the academic platforms, and the tier-5-only
verdicts in section 8 rest on academic-platform zeros, not on web absence.

## 3. Search strategies

<!-- prisma-s-8 -->
Every query below was captured at execution time from the executing process in
the same write as its results; nothing was reconstructed afterwards. The
executed query is the full request URL, reproduced verbatim; the raw response
is the log file named by the query_id (`.json` for Crossref/OpenAlex/Semantic
Scholar, `.xml` for arXiv, with the query URL embedded in a header comment).
Queries were phrased from the registry's variant columns; the registry rows
drawn on are cited per cluster in section 8.

```text swB-crossref-01
https://api.crossref.org/works?query.bibliographic=secular+bull+and+bear+markets+stock+prices&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-02
https://api.crossref.org/works?query.bibliographic=stock+market+correction+definition+decline+threshold&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-03
https://api.crossref.org/works?query.bibliographic=investor+capitulation+stock+market+selling&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-04
https://api.crossref.org/works?query.bibliographic=identifying+market+tops+bottoms+stock+prices+turning+points&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-05
https://api.crossref.org/works?query.bibliographic=stock+market+crash+definition+identification+threshold+decline&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-06
https://api.crossref.org/works?query.bibliographic=stock+market+cycles+expansion+contraction+bull+bear+phases&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-07
https://api.crossref.org/works?query.bibliographic=stock+market+booms+and+busts+identification+dating&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-08
https://api.crossref.org/works?query.bibliographic=risk-on+risk-off+episodes+identification+currencies&rows=8&select=DOI,title,issued,container-title,type,abstract
# error: HTTP Error 429 (logged as executed, zero records; re-run verbatim as swB-crossref-08b)
```
```text swB-crossref-08b
https://api.crossref.org/works?query.bibliographic=risk-on+risk-off+episodes+identification+currencies&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-09
https://api.crossref.org/works?query.bibliographic=flight+to+quality+flight+to+safety+stock+bond+correlation+episodes&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-10
https://api.crossref.org/works?query.bibliographic=financial+stress+index+identifying+stress+episodes&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-11
https://api.crossref.org/works?query.bibliographic=volatility+squeeze+Bollinger+band+width+low+volatility+state&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-12
https://api.crossref.org/works?query.bibliographic=narrow+range+day+volatility+contraction+expansion+intraday+prices&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-13
https://api.crossref.org/works?query.bibliographic=trading+range+breakout+rule+test+stock+returns&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-14
https://api.crossref.org/works?query.bibliographic=trend+day+intraday+day+type+classification+futures&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-15
https://api.crossref.org/works?query.bibliographic=super-exponential+price+growth+bubble+log-periodic&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-16
https://api.crossref.org/works?query.bibliographic=runs+test+stock+price+changes+random+walk&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-17
https://api.crossref.org/works?query.bibliographic=drawdown+drawup+stock+market+outliers&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-18
https://api.crossref.org/works?query.bibliographic=directional+change+intrinsic+time+regime+foreign+exchange&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-19
https://api.crossref.org/works?query.bibliographic=momentum+burst+price+acceleration+stock+returns&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-20
https://api.crossref.org/works?query.title=bear+market+rally&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-21
https://api.crossref.org/works?query.title=market+phases&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-crossref-22
https://api.crossref.org/works?query.title=market+episodes&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-01
https://api.crossref.org/works?query.bibliographic=Fama+The+Behavior+of+Stock-Market+Prices+Journal+of+Business+1965&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-02
https://api.crossref.org/works?query.bibliographic=Wald+Wolfowitz+On+a+test+whether+two+samples+are+from+the+same+population&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-03
https://api.crossref.org/works?query.bibliographic=Mood+The+Distribution+Theory+of+Runs+Annals+of+Mathematical+Statistics&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-04
https://api.crossref.org/works?query.bibliographic=Cowles+Jones+Some+A+Posteriori+Probabilities+in+Stock+Market+Action+Econometrica&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-05
https://api.crossref.org/works?query.bibliographic=Cowles+A+Revision+of+Previous+Conclusions+Regarding+Stock+Price+Behavior+Econometrica&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-06
https://api.crossref.org/works?query.bibliographic=Mishkin+White+U.S.+Stock+Market+Crashes+and+Their+Aftermath+Implications+for+Monetary+Policy&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-07
https://api.crossref.org/works?query.bibliographic=Johansen+Ledoit+Sornette+Crashes+as+critical+points+International+Journal+of+Theoretical+and+Applied+Finance&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-08
https://api.crossref.org/works?query.bibliographic=Baur+Lucey+Flights+and+contagion+an+empirical+analysis+of+stock+bond+correlations&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-09
https://api.crossref.org/works?query.bibliographic=Baele+Bekaert+Inghelbrecht+Wei+Flights+to+Safety+Review+of+Financial+Studies&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-10
https://api.crossref.org/works?query.bibliographic=Illing+Liu+Measuring+financial+stress+in+a+developed+country+an+application+to+Canada&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-11
https://api.crossref.org/works?query.bibliographic=Edwards+Biscarri+Perez+de+Gracia+Stock+market+cycles+financial+liberalization+and+volatility&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-12
https://api.crossref.org/works?query.bibliographic=Kaminsky+Schmukler+Short-Run+Pain+Long-Run+Gain+Financial+Liberalization+and+Stock+Market+Cycles&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-13
https://api.crossref.org/works?query.bibliographic=Candelon+Piplack+Straetmans+On+measuring+synchronization+of+bulls+and+bears+the+case+of+East+Asia&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-14
https://api.crossref.org/works?query.bibliographic=Aloud+Tsang+Olsen+Dupuis+A+directional-change+event+approach+for+studying+financial+time+series&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-15
https://api.crossref.org/works?query.bibliographic=Chen+Tsang+Detecting+Regime+Change+in+Computational+Finance+Data+Science+Machine+Learning+and+Algorithmic+Trading&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-16
https://api.crossref.org/works?query.bibliographic=Phillips+Shi+Yu+Testing+for+multiple+bubbles+historical+episodes+of+exuberance+and+collapse+in+the+S%26P+500&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-17
https://api.crossref.org/works?query.bibliographic=Phillips+Wu+Yu+Explosive+behavior+in+the+1990s+Nasdaq+when+did+exuberance+escalate+asset+values&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-18
https://api.crossref.org/works?query.bibliographic=Niederhoffer+Osborne+Market+Making+and+Reversal+on+the+Stock+Exchange&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-19
https://api.crossref.org/works?query.bibliographic=Bordo+Wheelock+When+do+stock+market+booms+occur+the+macroeconomic+and+policy+environment+of+twentieth+century+booms&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-ki-20
https://api.crossref.org/works?query.bibliographic=Katsenelson+Active+Value+Investing+Making+Money+in+Range-Bound+Markets&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text swB-arxiv-01
http://export.arxiv.org/api/query?search_query=abs:%22runs+test%22+AND+cat:q-fin*&max_results=10
```
```text swB-arxiv-02
http://export.arxiv.org/api/query?search_query=abs:%22directional+change%22+AND+abs:%22intrinsic+time%22&max_results=10
```
```text swB-arxiv-03
http://export.arxiv.org/api/query?search_query=abs:%22volatility+squeeze%22&max_results=10
```
```text swB-arxiv-04
http://export.arxiv.org/api/query?search_query=abs:%22trend+day%22+AND+cat:q-fin*&max_results=10
```
```text swB-arxiv-05
http://export.arxiv.org/api/query?search_query=abs:%22capitulation%22+AND+cat:q-fin*&max_results=10
```
```text swB-arxiv-06
http://export.arxiv.org/api/query?search_query=abs:%22secular+bear%22+OR+abs:%22secular+bull%22&max_results=10
```
```text swB-arxiv-07
http://export.arxiv.org/api/query?search_query=abs:%22bear+market+rally%22&max_results=10
```
```text swB-arxiv-08
http://export.arxiv.org/api/query?search_query=abs:%22momentum+burst%22&max_results=10
```
```text swB-openalex-01
https://api.openalex.org/works?filter=title.search:%22market%20phase%22&sort=cited_by_count:desc&per-page=10
```
```text swB-openalex-02
https://api.openalex.org/works?filter=title.search:%22market%20mode%22&sort=cited_by_count:desc&per-page=10
```
```text swB-openalex-03
https://api.openalex.org/works?filter=title.search:%22market%20environment%22&sort=cited_by_count:desc&per-page=10
```
```text swB-openalex-04
https://api.openalex.org/works?filter=title.search:%22market%20conditions%22&sort=cited_by_count:desc&per-page=10
```
```text swB-openalex-05
https://api.openalex.org/works?search=%22runs%20test%22%20%22stock%20prices%22%20random%20walk&per-page=10
```
```text swB-openalex-06
https://api.openalex.org/works?search=%22directional%20change%22%20regime%20detection%20finance&per-page=10
```
```text swB-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=directional%20change%20regime%20detection%20foreign%20exchange&fields=title,year,venue,externalIds,citationCount&limit=10
# error: HTTP Error 429
```
```text swB-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=flight%20to%20safety%20episode%20identification%20stock%20bond&fields=title,year,venue,externalIds,citationCount&limit=10
# error: HTTP Error 429
```

<!-- prisma-s-9 -->
**Limits and restrictions (PRISMA-S 9).** No date limits, no language limits,
no study-type limits were applied to any query. Crossref rows were capped at
`rows=8` (topical) and `rows=3` (known-item) as a screening-budget cap on
retrieval depth, not on eligibility; the total-hit counts in the logs record
what lay beyond the cap. OpenAlex title-probe queries were capped at the first
10 results sorted by citation count; this depth cap matters for the two
high-collision probes (swB-openalex-03, swB-openalex-04; 1,666 and 2,904 total
hits) and is declared as a recall limit in section 10. The arXiv q-fin
category filter appears in three arXiv queries as part of the verbatim strings
above.

<!-- prisma-s-14 -->
**Peer review of the search strategy (PRISMA-S 14 / PRESS).** The strategy was
not peer reviewed; no second searcher existed in this session. The registry
itself (compiled 2026-08-24 by a prior dispatch) served as the strategy's term
source, which is the PRESS element-4 mitigation the registry was built for;
the known-item list (swB-ki-01 to swB-ki-20) was derived from the dispatch's
named known items plus backward-citation reasoning over the registry's
families, and is vulnerable to the compiler's blind spots. Section 8.10
records the coverage explicitly declared unexecuted.

## 4. Peer review of the strategy

Covered under `prisma-s-14` above: not peer reviewed, single searcher, registry
as the empirically seeded instrument, unexecuted variants declared in 8.9.

## 5. Managing records

<!-- prisma-s-16 -->
**Deduplication process and software.** Identifier-level deduplication was
performed with a Python 3.11 standard-library script over the raw logs (DOI
string, or OpenAlex id / arXiv id where no DOI exists), followed by a
hand-verified same-work ledger for records carried under two identifiers
(working-paper / journal twins, publisher double-registrations, reprints).
The rule for the hand ledger: two records are one work only if their titles
match (case- and punctuation-insensitive) or the twin relation is documented
(NBER/SSRN/IMF working-paper series of a retained journal article). Exact
identifier repeats across queries: **5** (10.2139/ssrn.4866889,
10.2139/ssrn.2584378, 10.2307/1905433, 10.2307/1907042, 10.1201/9781003087595).
Same-work removals: **32**, itemised:

| group (work) | identifiers collapsed | removed |
|---|---|---|
| Booms and Busts in China's Stock Market | ssrn.1599538, ssrn.1691551 | 1 |
| Monetary Policy and Stock Market Booms and Busts (Bordo, Dueker & Wheelock) | 10.20955/wp.2007.020, ssrn.986404 | 1 |
| Mishkin & White, U.S. Stock Market Crashes | 10.3386/w8992, 10.7551/mitpress/1459.003.0011 | 1 |
| De Bock & de Carvalho Filho, risk-off episodes | 10.5089/9781557755308.001, 10.5089/9781557755308.001.a001, 10.1016/j.jimonfin.2014.12.009 | 2 |
| Baur & Lucey, Flights and contagion | ssrn.886119, 10.1016/j.jfs.2008.08.001 | 1 |
| Baele et al., Flights to Safety | 10.3386/w19095, ssrn.2160858, ssrn.2342138 | 2 |
| Edwards, Biscarri & Perez de Gracia, Stock market cycles | 10.3386/w9817, 10.1016/j.jimonfin.2003.09.011 | 1 |
| Kaminsky & Schmukler WP, Effects of Financial Liberalization | 10.3386/w9787, 10.1596/1813-9450-2912 | 1 |
| Phillips, Shi & Yu, Testing for Multiple Bubbles | ssrn.2327609, 10.1111/iere.12132 | 1 |
| Phillips, Wu & Yu, Explosive Behavior | ssrn.972730, ssrn.1413830, 10.1111/j.1468-2354.2010.00625.x | 2 |
| Bordo & Wheelock, When Do Stock Market Booms Occur? | 10.20955/wp.2006.051, ssrn.929573, 10.1017/cbo9780511757419.015 | 2 |
| Aloud et al., Directional-Change Event Approach | ssrn.1973471, 10.5018/economics-ejournal.ja.2012-36 | 1 |
| Hu et al., improved DC and regime change detection | ssrn.4048864, 10.1016/j.physa.2023.128810 | 1 |
| Johansen & Sornette, drawdowns are outliers | ssrn.244563, 10.21314/jor.2002.058 | 1 |
| Science 1988 news item (endowments) | 10.1126/science.1142-b, 10.1126/science.240.4856.1142-b, 10.1126/science.240.4856.1142.c | 2 |
| Corporate Bond Issuance Over Financial Stress Episodes | ssrn.5069503, ssrn.5340143 | 1 |
| Bull and Bear Phases, Indian markets | 10.26643/gis.v11i5.3410, 10.21863/ijfm/2016.6.2.029 | 1 |
| Cryptocurrency LPPL bubble detection | ssrn.3983539, 10.1109/tem.2024.3427647 | 1 |
| FX futures volatility JFM 1999 (SICI double registration) | 10.1002/(sici)1096-9934(199909)19:6<665::aid-fut3>3.3.co;2-e, same 3.0.co;2-n | 1 |
| IFS working paper 1424 (double registration) | 10.1920/wp/ifs.2024.1424, 10.1920/wp.ifs.2024.1424 | 1 |
| Phases of market transformation (Changing the Food Game) | 10.4324/9781351285643-5, 10.9774/gleaf.978-1-78353-215-5_6 | 1 |
| Gold market volatility and REITs | 10.1016/j.irfa.2024.103348, 10.15396/eres2024-222 | 1 |
| acps.13622 referee reports (review 1 and review 2, each under two version DOIs) | four review-report DOIs collapsed to two works | 2 |
| Conditional threshold effects, oil-stock volatility | ssrn.4512310, 10.1016/j.eneco.2025.108189 | 1 |
| Random walks, Chinese and Indian equity markets | arXiv:1709.04059, 10.19139/soic.v7i1.499 | 1 |
| Fama FAJ Random Walks (1995 reprint of 1965) | 10.2469/faj.v21.n5.55, 10.2469/faj.v51.n1.1861 | 1 |

`n_duplicates_removed` = 5 + 32 = **37**; 303 - 37 = **266** screened;
266 - 235 excluded = **31** included = store entry count.

<!-- prisma-2020-8 -->
**Selection process (PRISMA 2020 item 8).**

- screeners_n: 1
- independent: no - a single screener cannot be independent of itself
- automation_tools: Claude Fable 5 (model id claude-fable-5), operating as the
  research-librarian agent (sweep Agent B) in Claude Code / Claude Agent SDK,
  performed all screening and extraction; it is the automation tool and the
  sole screener. Deduplication used a Python 3.11 stdlib script as described
  above.

Screening was title-level against the frozen criteria, then abstract-level for
every candidate inclusion; where no abstract existed at any queried platform,
a working-paper twin's abstract was used and the depth is flagged per record
in section 7. Candidates whose definitional content could not be verified at
any depth were excluded (section 6), not completed from memory.

## 6. Excluded records

<!-- prisma-2020-16b -->
Near-misses: records that appeared to meet the criteria and were excluded
after closer assessment, one reason each (PRISMA 2020 item 16b). Junk
retrievals (homonym collisions with no apparent eligibility) are not listed
row-by-row; they are the bulk of the 235 exclusions and the dominant reasons
are collision-driven (political regime change, electricity-market modes,
labor-market conditions, medical runs/episodes).

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E01 | Freeman MC (2008). The Time-Varying Equity Premium and Secular Bull and Bear Markets of the Twentieth Century. SSRN. doi:10.2139/ssrn.1100147 | abstract assessment | Names and counts "all seven secular bull and bear markets of the last century" but states no assignment rule in any retrievable text; the episodes are taken as given and their magnitudes explained by a consumption-risk model. Best near-miss for an operational "secular" definition; kept as the pointer for a full-text follow-up. |
| E02 | Candelon B, Piplack J, Straetmans S (2008). On measuring synchronization of bulls and bears: the case of East Asia. J Banking & Finance 32(6). doi:10.1016/j.jbankfin.2007.08.003 | abstract assessment | Test apparatus for bull/bear phase synchronization over externally dated phases; no abstract retrievable on Crossref, OpenAlex, or Semantic Scholar, so its definitional novelty (if any) could not be verified without completing from memory. |
| E03 | Bull Market? Bear Market? J Portfolio Management (1997). doi:10.3905/jpm.1997.26 | title screening | Title matches the cluster exactly but no abstract or author metadata is retrievable; no verifiable definitional content. |
| E04 | Trading Range Breakout Test on Daily Stocks of Indian Markets (2017). SSRN. doi:10.2139/ssrn.3068852 | abstract assessment | Application of the Brock, Lakonishok & LeBaron (1992) trading-range-breakout rule (prior corpus, doi:10.1111/j.1540-6261.1992.tb04681.x) to Indian stocks; no definitional novelty. |
| E05 | Peculiar statistical properties of Chinese stock indices in bull and bear market phases. Physica A (2009). doi:10.1016/j.physa.2008.11.028 | abstract assessment | Documents distributional properties within externally dated bull/bear phases; contributes no assignment rule of its own. |
| E06 | Market efficiency and technical analysis during different market phases (2017). doi:10.21511/imfi.14(2-2).2017.07 | title screening | Technical-rule profitability across pre-labelled phases; no definitional novelty. |
| E07 | Emergence of time-horizon invariant correlation structure in financial returns by subtraction of the market mode. Phys Rev E (2007). doi:10.1103/physreve.76.026104 | abstract assessment | "Market mode" homonym: the dominant eigenvector of the return correlation matrix (a cross-sectional common factor), not a temporal state; recorded as a collision in section 8.8. |
| E08 | Cowles A (1944). Stock Market Forecasting. Econometrica. doi:10.2307/1905433 | title screening | Forecaster-track-record evaluation, not state assignment; retrieved twice by the Cowles known-item queries. |
| E09 | U.S. Stock Market Crash Risk, 1926-2006 (2009). NBER w14913. doi:10.3386/w14913 | title screening | Crash-risk estimation from options data; no crash-state assignment rule. |
| E10 | Super-Exponential RE Bubble Model with Efficient Crashes (2017). SSRN. doi:10.2139/ssrn.3064668 | abstract assessment | Super-exponential bubble model whose definitional content is subsumed by the included Johansen-Ledoit-Sornette lineage (NB-03); preprint of a journal article not retrieved by any query. |
| E11 | "Risk-Off" Episodes, ch. 30 of The Global Economy in Turbulent Times (2015). doi:10.1002/9781119155133.ch30 | title screening | Tier-5 practitioner restatement of the risk-off construct operationalised by the included De Bock & de Carvalho Filho record (NB-12). |
| E12 | Market Dynamics: On Directional Information Derived From (Time, Execution Price, Shares Traded). arXiv:1903.11530 | abstract assessment | Surfaced by the bear-market-rally phrase; transaction-sequence information study, no operational bear-rally definition. |
| E13 | Market Tops and Bottoms, ch. 22 of Stop and Make Money (2012). doi:10.1002/9781119198574.ch22 | title screening | Practitioner chapter; no rule extractable at the retrieved (title) depth; tops/bottoms remain without an academic operationalization (section 8.1). |
| E14 | Opening Range Breakout, ch. 11 of Swing and Day Trading (2012). doi:10.1002/9781119203933.ch11 | title screening | Tier-5; the opening-range construct is level-corpus prior ground (D08-D09 of the level survey). |
| E15 | Maheu JM, McCurdy TH. Identifying Bull and Bear Markets in Stock Returns. SSRN. doi:10.2139/ssrn.146531 | screening (prior coverage) | Working-paper twin of the journal record already held as regime-definitions D21; prior coverage, not re-included. |
| E16 | Lunde A, Timmermann A (2004). Duration Dependence in Stock Prices. JBES. doi:10.1198/073500104000000136 | screening (prior coverage) | Predecessor record (P04); retrieved by swB-crossref-01. |
| E17 | Fabozzi FJ, Francis JC (1977). Stability Tests for Alphas and Betas over Bull and Bear Market Conditions. J Finance. doi:10.1111/j.1540-6261.1977.tb03312.x | screening (prior coverage) | Predecessor record (D01-D03); retrieved by swB-openalex-04 - the only definitional record the "market conditions" probe surfaced, and it was already caught by regime vocabulary. |
| E18 | Can exchange-traded funds be profitably traded with the trading range breakout technical trading rule? (2022). doi:10.1142/s242478632250027x | screening (prior coverage) | Level-corpus record; retrieved by swB-crossref-13. |
| E19 | Opening Range Breakout Stock Trading Algorithmic Model (2016). doi:10.5121/ijci.2016.5107 | screening (prior coverage) | Level-corpus record; retrieved by swB-crossref-13. |

## 7. Included corpus

<!-- included-corpus -->
31 records. `depth`: **A** = abstract-verified from the record's own metadata;
**T** = abstract-verified via a logged working-paper twin or RePEc page;
**M** = metadata-only (title/TOC depth), flagged wherever a definitional claim
rests on it. Tier: **PR** = peer-reviewed journal; **WP** = institutional
working paper (non-refereed, charter tier flag); **BK** = book or book chapter
(practitioner chapters additionally flagged tier 5); **PP** = preprint.

| NB | store id | cluster | record | tier | depth |
|---|---|---|---|---|---|
| NB-01 | `mishkin2002w8992` | 1 | Mishkin & White (2002). U.S. Stock Market Crashes and Their Aftermath. NBER w8992. doi:10.3386/w8992 | WP | A |
| NB-02 | `johansen2001jor2002058` | 1 | Johansen & Sornette (2001). Large stock market price drawdowns are outliers. J Risk. doi:10.21314/jor.2002.058 | PR | A |
| NB-03 | `johansen2000s02190249000` | 1/5 | Johansen, Ledoit & Sornette (2000). Crashes as critical points. IJTAF. doi:10.1142/s0219024900000115 | PR | A |
| NB-04 | `phillips2011j14682354201` | 1/5 | Phillips, Wu & Yu (2011). Explosive Behavior in the 1990s Nasdaq. Int Econ Rev. doi:10.1111/j.1468-2354.2010.00625.x | PR | A |
| NB-05 | `phillips2015iere12132` | 1/5 | Phillips, Shi & Yu (2015). Testing for Multiple Bubbles. Int Econ Rev. doi:10.1111/iere.12132 | PR | A |
| NB-06 | `arxiv250905922` | 1 | Rao & Rojas (2025). Predicting Market Troughs. arXiv:2509.05922 | PP | A |
| NB-07 | `anon2012978111919736` | 1 | Katsenelson, Active Value Investing, ch. 2: Emotions of Secular Bull, Bear, and Range-Bound Markets. Wiley. doi:10.1002/9781119197362.ch2 | BK (tier 5) | M |
| NB-08 | `landriault2017jpr201720` | 1 | Landriault, Li & Zhang (2017). A unified approach for drawdown (drawup) of time-homogeneous Markov processes. J Appl Probab. doi:10.1017/jpr.2017.20 | PR | A |
| NB-09 | `edwards2003jjimonfin200` | 2 | Edwards, Biscarri & Perez de Gracia (2003). Stock market cycles, financial liberalization and volatility. JIMF. doi:10.1016/j.jimonfin.2003.09.011 | PR | T |
| NB-10 | `kaminsky2008rfn002` | 2 | Kaminsky & Schmukler (2008). Short-Run Pain, Long-Run Gain. Rev Finance. doi:10.1093/rof/rfn002 | PR | A |
| NB-11 | `bordo2006wp2006051` | 2 | Bordo & Wheelock (2006). When Do Stock Market Booms Occur? St. Louis Fed WP 2006-051. doi:10.20955/wp.2006.051 | WP | A |
| NB-12 | `debock2015jjimonfin201` | 3 | De Bock & de Carvalho Filho (2015). The behavior of currencies during risk-off episodes. JIMF. doi:10.1016/j.jimonfin.2014.12.009 | PR | T |
| NB-13 | `baur2009jjfs20080800` | 3 | Baur & Lucey (2009). Flights and contagion - an empirical analysis of stock-bond correlations. J Financial Stability. doi:10.1016/j.jfs.2008.08.001 | PR | T |
| NB-14 | `baele2019hhz055` | 3 | Baele, Bekaert, Inghelbrecht & Wei (2019). Flights to Safety. Rev Financial Studies. doi:10.1093/rfs/hhz055 | PR | A |
| NB-15 | `illing2006jjfs20060600` | 3 | Illing & Liu (2006). Measuring financial stress in a developed country. J Financial Stability. doi:10.1016/j.jfs.2006.06.002 | PR | T |
| NB-16 | `duprey2017jjfs20170700` | 3 | Duprey, Klaus & Peltonen (2017). Dating systemic financial stress episodes in the EU countries. J Financial Stability. doi:10.1016/j.jfs.2017.07.004 | PR | T |
| NB-17 | `anon2012978111920780` | 4 | Gunn, Trading Regime Analysis, ch. 10: Bollinger Band Width. Wiley. doi:10.1002/9781119207801.ch10 | BK (tier 5) | M |
| NB-18 | `wald19401177731909` | 6 | Wald & Wolfowitz (1940). On a Test Whether Two Samples are from the Same Population. Ann Math Statist. doi:10.1214/aoms/1177731909 | PR | M |
| NB-19 | `mood19401177731825` | 6 | Mood (1940). The Distribution Theory of Runs. Ann Math Statist. doi:10.1214/aoms/1177731825 | PR | M |
| NB-20 | `wolfowitz19441177731281` | 6 | Wolfowitz (1944). Asymptotic Distribution of Runs Up and Down. Ann Math Statist. doi:10.1214/aoms/1177731281 | PR | M |
| NB-21 | `cowles19371905515` | 6 | Cowles & Jones (1937). Some A Posteriori Probabilities in Stock Market Action. Econometrica. doi:10.2307/1905515 | PR | M |
| NB-22 | `cowles19601907573` | 6 | Cowles (1960). A Revision of Previous Conclusions Regarding Stock Price Behavior. Econometrica. doi:10.2307/1907573 | PR | M |
| NB-23 | `fama1965294743` | 6 | Fama (1965). The Behavior of Stock-Market Prices. J Business 38(1):34-105. doi:10.1086/294743 | PR | M |
| NB-24 | `niederhoffer1966016214591966` | 6 | Niederhoffer & Osborne (1966). Market Making and Reversal on the Stock Exchange. JASA. doi:10.1080/01621459.1966.10482183 | PR | A |
| NB-25 | `aloud2012economicsejo` | 7 | Aloud, Tsang, Olsen & Dupuis (2012). A Directional-Change Event Approach for Studying Financial Time Series. Economics (e-journal). doi:10.5018/economics-ejournal.ja.2012-36 | PR | A |
| NB-26 | `tsang2018tetci2017277` | 7 | Tsang & Chen (2018). Regime Change Detection Using Directional Change Indicators in the Foreign Exchange Market to Chart Brexit. IEEE TETCI. doi:10.1109/tetci.2017.2775235 | PR | A |
| NB-27 | `hu2023jphysa202312` | 7 | Hu, Zhang, Li & Wu (2023). Incorporating improved directional change and regime change detection to formulate trading strategies in foreign exchange markets. Physica A. doi:10.1016/j.physa.2023.128810 | PR | T |
| NB-28 | `chen2020978100308759` | 7 | Chen & Tsang (2020). Detecting Regime Change in Computational Finance. CRC Press. doi:10.1201/9781003087595 | BK | M |
| NB-29 | `arxiv251114408` | 7 | Houweling (2025). The Hidden Constant of Market Rhythms: How 1-1/e Defines Scaling in Intrinsic Time. arXiv:2511.14408 | PP | A |
| NB-30 | `gooding19772330259` | 8 | Gooding & O'Malley (1977). Market Phase and the Stationarity of Beta. JFQA. doi:10.2307/2330259 | PR | A |
| NB-31 | `putzig2010090754029` | 8 | Putzig, Becherer & Horenko (2010). Optimal Allocation of a Futures Portfolio Utilizing Numerical Market Phase Detection. SIAM J Financial Math. doi:10.1137/090754029 | PR | A |

### 7.1 Non-refereed records (charter evidence-tier flag)

NB-01 and NB-11 (institutional working papers: NBER; Federal Reserve Bank of
St. Louis), NB-06 and NB-29 (arXiv preprints), NB-07 and NB-17 (practitioner
Wiley chapters, tier 5, retained for the same reason the definitions survey
retained D17 and D57: they are the only DOI-indexed carriers of their
constructs), NB-28 (published monograph, not journal-refereed). Every claim in
section 8 resting on one of these carries the flag inline.

## 8. Synthesis

### 8.0 Entry inventory (roles, mechanisms, causality, nulls)

Causality codes as in the regime-definitions survey (F filtered/online, B both,
R retro-confirmed, L lookahead by construction, n/a for pure apparatus).

| NB | role | statement (quotes are from logged text) | states named | mechanism | caus. | null |
|---|---|---|---|---|---|---|
| NB-01 | definition | "examines fifteen historical episodes of stock market crashes" in the U.S. over a century; the episode-selection rule is in the paper's text and was not extractable from retrieved metadata - flagged, not completed from memory | crash episode vs not | retrospective episode identification | not classified (rule not extracted) | none |
| NB-02 | definition + null-apparatus | Drawdown = "a more natural measure of real market risks"; "approximately 98% of the distributions of drawdowns is well-represented by a stretched exponential while the largest drawdowns are occurring with a significantly larger rate than predicted"; "confirmed by extensive testing on surrogate data" | drawdown / drawup episodes; outlier crashes | running-extremum episode segmentation + parametric null + surrogates | F (episode boundary confirmed one move later) | **stated** (stretched-exponential + surrogate) |
| NB-03 | definition | Bubble regime = "the tendency for noise traders to imitate their nearest neighbors increases up to a certain point called the 'critical' point"; hazard rate of crash rises super-exponentially; log-periodic precursor structure fit to prices | bubble (precursor) regime, crash | LPPL model fit over a window | R (rolling fit possible; published fits episode-retrospective) | partial (hazard model; formal existence test not stated in this record) |
| NB-04 | definition + null-apparatus | "A recursive test procedure ... for testing explosive behavior, date stamping the origination and collapse of economic exuberance, and providing valid confidence intervals for explosive growth rates ... new limit theory for mildly explosive processes" | explosive (exuberant) vs unit-root regime | recursive right-tailed ADF sup test | **F** (real-time date-stamping is the stated purpose) | **stated** (limit theory + critical values) |
| NB-05 | definition + null-apparatus | GSADF: "a new recursive flexible window method ... delivers a consistent real-time date-stamping strategy for the origination and termination of multiple bubbles" | multiple explosive episodes vs normal | recursive flexible-window sup ADF | **F** | **stated** |
| NB-06 | definition (preprint) | "a high-performance nowcasting model that accurately identifies capitulation events in real-time"; troughs and capitulation events used interchangeably as targets | trough / capitulation event | supervised nowcasting (ML) with causal DML analysis | F (claimed) | none (inference on drivers, not on state existence) |
| NB-07 | synonym-evidence (tier 5) | Chapter title coordinates three secular states: "Secular Bull, Bear, and Range-Bound Markets"; definitional content not extracted (title depth) | secular bull, secular bear, range-bound | not extracted | not classified | none |
| NB-08 | null-apparatus | "the joint law of the first passage time of the drawdown (respectively, drawup) process, its overshoot, and the maximum ... unique solution to an integral equation"; explicit forms for Levy and one-sided-jump Markov processes | (apparatus for drawdown/drawup episodes) | analytic first-passage theory | n/a | **stated** (exact laws under null processes) |
| NB-09 | definition + synonym-evidence | "we describe the bull and bear cycles of four Latin American and two Asian countries, comparing their characteristics during both phases and the degree of concordance" (twin abstract); dating by a Bry-Boschan-family algorithm in text | bull / bear phases of a stock market cycle | windowed peak/trough dating | L | none (concordance statistics, no existence null) |
| NB-10 | definition | "constructs a new comprehensive chronology" of financial liberalization and stock-market "booms and busts"; boom/bust episodes dated from price extrema in text | boom, bust | chronology / windowed extrema | L | none |
| NB-11 | definition | "booms tended to occur during periods of above-average growth of real output ... booms often ended within a few months of an increase in inflation"; boom episodes identified over ten countries; dating rule in text, not in retrieved metadata | boom (vs not) | retrospective episode dating | L | none |
| NB-12 | definition | "Episodes of increased global risk aversion, also known as risk-off episodes" (IMF twin abstract); episode trigger is a VIX-based threshold rule stated in the paper's text - flagged as in-text, not extracted verbatim | risk-off episode vs normal | observable threshold on a volatility index | F (threshold on observables at t) | none |
| NB-13 | definition + null-apparatus | "We propose a definition and a test for flight-to-quality, flight-from-quality and cross-asset contagion" (SSRN twin abstract) | flight-to-quality, flight-from-quality, contagion | stock-bond comovement threshold + test | F (day-level observables) | **stated** (test accompanies the definition) |
| NB-14 | definition | "We identify flight-to-safety (FTS) days for twenty-three countries using only stock and bond returns and a model averaging approach. FTS days comprise less than 2% of the sample" | FTS day vs ordinary day | model-averaged classification, ordinal FTS indicator | B (model-based; full-sample estimation, day-level output) | partial (identification is probabilistic; no no-FTS null stated in abstract) |
| NB-15 | definition + synonym-evidence | "Stress is ... a continuous variable with a spectrum of values, where extreme values are called financial crises" (Bank of Canada twin abstract); index construction with survey-based validation | stress continuum; crisis = extreme stress | composite index + extreme-value convention (`CONVENTION` threshold) | F | none (survey validation, not a distributional null) |
| NB-16 | definition | "identify systemic financial stress events in an objective and reproducible way ... Markov-switching models [and a] threshold VAR" over the CLIFS index, giving "a chronology of systemic financial stress episodes as a complement to the expert-detected events" (RePEc abstract) | systemic stress episode vs normal | latent Markov / threshold VAR dating over a stress index | B | inherited (MS-family existence tests, prior corpus) |
| NB-17 | definition (tier 5) | Chapter formalising Bollinger Band Width as a trading-regime indicator; content at title depth. Confirms the squeeze/width construct's only DOI-indexed carriers remain practitioner books | squeeze / band-width regime | band-width threshold | F (per D17 family) | none |
| NB-18 | null-apparatus | The runs-test null: exact distribution of the number of runs in a two-sample arrangement under exchangeability | (apparatus) | combinatorial exact distribution | n/a | **stated** |
| NB-19 | null-apparatus | Exact and asymptotic "distribution theory of runs" of all lengths under randomness | (apparatus) | combinatorial | n/a | **stated** |
| NB-20 | null-apparatus | Asymptotic normality of the number of runs up and down - the null for up/down price-change sequences specifically | (apparatus) | combinatorial asymptotics | n/a | **stated** |
| NB-21 | definition + null-apparatus | Sequences-and-reversals counts on stock-market action compared with their expectation under chance (title + Econometrica record; content flagged paraphrase at metadata depth) | sequence, reversal | count statistic vs binomial expectation | n/a (existence test) | **stated** |
| NB-22 | null-apparatus (correction) | Revision of the 1937 conclusions: the earlier apparent persistence is materially reduced once an averaging artifact is corrected (flagged paraphrase at metadata depth) | - | re-analysis | n/a | corrects a false positive |
| NB-23 | definition + null-apparatus | The dispatch's known item, VERIFIED at doi:10.1086/294743, J Business 38(1), 1965. Applies runs tests (expected runs under independence) and distributional analysis to daily stock prices (flagged paraphrase at metadata depth - no abstract exists for 1965 J Business) | runs of same-sign price changes | runs count vs independence null | n/a (existence test) | **stated** (via NB-18/NB-19/NB-20 apparatus) |
| NB-24 | definition + null-apparatus | "after a decline of 1/8 ... an advance on the next transaction is three times as likely as a decline ... after two price changes in the same direction, the odds in favor of a continuation ... are almost twice as great" - tick-level sequence statistics against the random-walk null | continuation vs reversal at tick scale | conditional sequence frequencies | n/a (existence test) | **stated** (implicit binomial null) |
| NB-25 | definition | "to use physical time scales ... runs the risk of missing important activities. An alternative approach is to use an event-based time scale ... a directional-change event ... capturing periodic market activities" | DC events; up/down alternation | DC threshold events (intrinsic time) | F | none |
| NB-26 | definition | "A regime change is a significant change in the collective trading behaviour in a financial market ... a novel method ... to detect regime change, which makes use of ... directional change (DC) ... identification of a new relevant indicator for regime change detection" | normal vs abnormal (regime-changed) market | DC indicators + detection procedure | F | none |
| NB-27 | definition | Adds a decay coefficient to the downward DC threshold, Bayesian-optimises the threshold pair, and "introduces DC-related indicators as the input of HMM ... to detect the regime change" (SSRN twin abstract) | regime states over DC indicators | DC + hidden Markov model | B | inherited (HMM family) |
| NB-28 | definition (book) | Monograph codifying DC-indicator-based regime-change detection and tracking (chapters retrieved: "Algorithmic Trading Based on Regime Change Tracking"); metadata depth | normal vs regime-changed | DC indicators + HMM | B | inherited |
| NB-29 | null-apparatus (preprint) | "Intrinsic Time can be modeled as a memoryless exponential hazard process. Empirically, the proportion of directional changes to total events stabilizes near 1-1/e = 0.632, matching the probability that a Poisson process completes one mean interval" - a renewal-process reference value for DC statistics | (apparatus for DC states) | renewal/exponential-hazard benchmark | n/a | **stated** (reference model) |
| NB-30 | synonym-evidence | "the stationarity of beta coefficients, especially in regard to recent, major stock market trends" under the title "Market Phase" - phase = major market trend (bull/bear), Fabozzi-Francis-era usage | market phase = major trend | period partition by trend (rule not extracted) | not classified | none |
| NB-31 | definition | "identification of market phases" via "simultaneous dimension reduction and metastability analysis of high-dimensional time series ... application of proposed strategies to online detection of the market phases" | market phases as metastable states | metastable clustering (FEM-family), online detection demonstrated | B | none |

### 8.1 Cluster 1 - bull/bear directional extensions: verdict

**Diff against the definitions survey.** The survey already holds bull/bear
defined five-plus structurally different ways (D01-D15, D21-D22, D58-D59) and
crash as a correlation-cluster state (D27, D41). What this sweep adds:

- **Drawdown/drawup episodes** are the operational academic counterpart of the
  press vocabulary (downturn, top/bottom, correction): NB-02 defines the
  episode from running extrema and - uniquely in the whole bull/bear family -
  attaches a stated null (stretched exponential + surrogates) under which
  crashes are outliers. NB-08 supplies exact drawdown/drawup laws under
  benchmark processes. **The registry has "drawdown" only as a spatial synonym
  of retracement; the temporal episode sense with its null literature is a
  missing family (section 8.7).**
- **Explosive/exuberant regime** (NB-04, NB-05): recursive right-tailed unit
  root tests date-stamp an explosive state in real time with stated limit
  theory. This is the academic operationalization nearest the practitioner
  "parabolic move," and among the strongest objects in the entire regime
  corpus on the agenda's axis: an assignment computable at t with a null
  attached to the assignment procedure itself. **Neither "bubble" nor
  "explosive" nor "exuberance" appears in the registry - a missing family.**
- **Capitulation / trough**: one preprint (NB-06) claims real-time
  identification of "capitulation events"; no peer-reviewed operational
  definition was located (swB-crossref-03 junk; swB-arxiv-05 one record).
- **Secular bull/bear**: no academic operationalization located.
  swB-arxiv-06 returned **0 records** in all of arXiv; the best academic-adjacent
  near-miss (E01) names seven secular episodes without a rule; the only
  DOI-indexed carrier of the term as a state taxonomy is a practitioner
  chapter (NB-07, tier 5), which however contributes the sweep's cleanest
  synonym coordination: secular bull / secular bear / **range-bound** as
  coordinate states of one partition.
- **Correction, bear-market rally, downturn, market top/bottom**: nothing
  academic beyond prior coverage (D15 carries the 10% correction convention at
  tier 5; D22 carries bull-correction/bear-rally as latent sub-states).
  swB-crossref-20 (title probe "bear market rally") surfaced no operational
  record; swB-crossref-02 and swB-crossref-04 surfaced only collisions and
  practitioner chapters (E03, E13).

### 8.2 Cluster 2 - business-cycle vocabulary applied to markets: verdict

The macro dating algorithms are prior ground (D06-D13). Applied to *markets*,
the vocabulary that actually carries operational content is **cycle/phase**
and **boom/bust**, not expansion/contraction: NB-09 dates "bull and bear
cycles ... phases" of stock indices with a windowed dating algorithm
(synonym evidence: cycle-phase = bull/bear); NB-10 builds a boom/bust
chronology; NB-11 (working paper) dates twentieth-century booms across ten
countries. No located source uses "expansion/contraction/recession/recovery"
as *market* states with an assignment rule beyond what D52 (clustering import)
already holds - the surviving usage is bull/bear under a cycle-phase wrapper.
**"Boom/bust" is attested in neither the registry nor the seed list - a
missing family (section 8.7).**

### 8.3 Cluster 3 - crisis/stress states: verdict

The predecessor corpus holds crisis/calm as clustering labels (D40-D44),
stress via distributional monitoring (D53), fragile via the absorption ratio
(D38). This sweep adds four operational definitions and one dating study, all
peer-reviewed:

- **Risk-off episode** (NB-12): episode of increased global risk aversion
  triggered by an observable volatility-index threshold - the first located
  operational definition behind the practitioner "risk-on/risk-off" pair the
  survey's q-crossref-13 failed to ground.
- **Flight-to-quality / flight-from-quality** (NB-13): "a definition and a
  test" - definition and null arrive together, rare in this corpus.
- **Flight-to-safety day** (NB-14): model-averaged day-level identification;
  FTS days < 2% of the sample.
- **Stress continuum with crisis as extreme value** (NB-15): explicit
  statement that "extreme values are called financial crises" - synonym
  evidence connecting the stress and crisis vocabularies on one axis, with
  the threshold a `CONVENTION`.
- **Systemic stress episodes dated model-wise** (NB-16): MS + threshold-VAR
  dating over a stress index, replacing expert crisis chronologies.

### 8.4 Cluster 4 - volatility states: verdict (an informative negative)

The dispatch asked whether an academic operationalization of
squeeze/compression exists under ANY variant. Registered zero and
collision results, extending the survey's q-arxiv-08 zero
("volatility compression", 0 records):

- **swB-arxiv-03** - `abs:"volatility squeeze"` - **0 records** in all of
  arXiv, any category.
- **swB-crossref-11** ("volatility squeeze Bollinger band width low volatility
  state") - no academic record; the top finance hit is a practitioner Wiley
  chapter (NB-17).
- **swB-crossref-12** ("narrow range day volatility contraction expansion
  intraday") - collisions only (electricity intraday markets, oil
  spillovers); the narrow-range-day construct surfaced nothing academic.

Verdict: **compression/squeeze remains tier-5-only under every variant tried
across two sweeps.** The construct's only DOI-indexed carriers are
practitioner chapters (D17's StockCharts formalisation; NB-17). Turbulent /
quiet and volatility-regime vocabulary remain fully covered by prior records
(D20, D28, D31, D36-D38, D50); nothing new was admitted there, by design.

### 8.5 Cluster 5 - trend events: verdict

- **Trading-range breakout beyond Brock et al. 1992**: every retrieved test
  is an application of the prior rule (E04, E18, E19) - no definitional
  novelty exists to admit. The breakout family's academic base remains the
  prior corpus.
- **Parabolic move**: the academic counterparts are the super-exponential /
  log-periodic bubble regime (NB-03) and the explosive regime (NB-04, NB-05).
  The correspondence practitioner-parabolic = academic-explosive is this
  review's **inference from construct descriptions, not an attested synonymy**;
  no located source states the equivalence, and the synonym graph marks it
  accordingly.
- **Momentum burst**: swB-arxiv-08 returned only physics collisions;
  swB-crossref-19 returned generic momentum-anomaly records. **No academic
  operationalization located; no tier-5-independent source located at all.**
- **Trend day**: swB-arxiv-04 - **0 records** in q-fin; swB-crossref-14
  collisions only. The construct remains Market Profile vocabulary (Agent A's
  ground for the practitioner side); no academic operationalization located.

### 8.6 Cluster 6 - runs: the known item verified and the lineage traced

Fama (1965), *The Behavior of Stock-Market Prices*, **verified** at
doi:10.1086/294743, J Business 38(1) (swB-ki-01; Handle System responseCode 1).
The runs-on-markets lineage as retrieved: the null apparatus is Wald &
Wolfowitz 1940 (NB-18), Mood 1940 (NB-19), and - most directly relevant to
up/down price sequences - Wolfowitz 1944 (NB-20); the market applications run
Cowles & Jones 1937 (NB-21, sequences and reversals against chance) through
Fama 1965 (NB-23) to tick level in Niederhoffer & Osborne 1966 (NB-24).
Cowles 1960 (NB-22) *corrects* the 1937 persistence finding as an
averaging artifact - a documented false positive in the state-existence
literature, directly relevant to the project's nulls-as-objects charter.

This family is the mirror image of the practitioner clusters: **nulls without
named states**. The runs literature attaches exact and asymptotic reference
distributions to sequence behaviour but never promotes "a run" to a market
state with an assignment rule; conversely the practitioner trend vocabulary
names states with no null. "Drift", "persistence", and "local trend" surfaced
no additional operational family: drift remains a random-walk parameter,
persistence is prior ground (Hurst/DFA records in the classification corpus;
duration dependence D21/P04), and "local trend" was not separately queried
(declared, section 8.10).

### 8.7 Families in NEITHER the registry NOR the seed list (saturation flags)

1. **boom / bust** (NB-10, NB-11; also the Bordo-Dueker-Wheelock twin pair in
   the dedup ledger). Surface forms: boom(s), bust(s), stock market boom,
   boom-bust cycle.
2. **bubble / explosive / exuberant regime** (NB-03, NB-04, NB-05; E10).
   Surface forms: bubble regime, explosive behavior/regime, (irrational)
   exuberance, mildly explosive, super-exponential growth, log-periodic
   power law, date-stamping. The largest omission by literature size: this is
   a full academic subfield with its own tests and critical values.
3. **drawdown / drawup as temporal episodes** (NB-02, NB-08; the registry
   carries drawdown only as a spatial retracement synonym). Surface forms:
   drawdown(s), drawup(s), maximum drawdown, drawdown episode.
4. **metastable state / metastability** (NB-31). Statistical assignment
   vocabulary (registry section 2.12 family) used for market phases by the
   FEM/Horenko school.
5. **sequences and reversals** (NB-21, NB-22): the pre-runs vocabulary of the
   earliest existence tests; absent from the registry's trend-event family.

### 8.8 Cluster 8 - regime-noun synonym probes: which vocabulary finds what

- **"market phase(s)"** (swB-crossref-21, swB-openalex-01): the one probe that
  earned its cost. It surfaced **two included records reachable by no other
  vocabulary in this sweep**: Gooding & O'Malley 1977 (NB-30; "market phase" =
  major market trend, the era's bull/bear usage) and Putzig, Becherer &
  Horenko 2010 (NB-31; phases as metastable states with online detection).
  Verdict: **"phase" is the one regime-synonym with independent recall value.**
- **"market mode"** (swB-openalex-02): collision-dominated (electricity
  markets), plus one *homonym* worth recording: in econophysics "market mode"
  means the dominant correlation eigenvector (E07) - a cross-sectional common
  factor, not a temporal state. Any future query on "mode" vocabulary inherits
  both collisions.
- **"market environment"** (swB-openalex-03, 1,666 hits): zero finance-state
  records in the citation-ranked top 10; entirely electricity/retail
  collisions at probe depth.
- **"market conditions"** (swB-openalex-04, 2,904 hits): the only
  finance-definitional record in the top 10 is Fabozzi & Francis 1977 - already
  prior coverage (E17). The "condition" vocabulary adds no recall beyond what
  regime-vocabulary queries caught in the predecessor sweep.
- **"market episodes"** (swB-crossref-22): collisions (fiscal episodes,
  psychiatric episodes); the productive "episode" usage in finance is always
  qualified - risk-off episode, stress episode, exuberance episode - and those
  compounds were caught by the cluster queries above, not by the bare noun.
- **"state" / "stage"**: not re-probed; "market state" collisions are
  documented in the survey (8.2 item 13) and the registry, and Weinstein
  "stage" remains located-by-citation only (survey 8.7); declared in 8.10.

### 8.9 Synonym graph (one row per swept term)

Columns per the dispatch: operational definition located (NB-id here, D-/P-id
for prior coverage, or NONE), null-distribution status, evidence tier of the
best locating source. "Inferred" marks a correspondence this review draws from
construct descriptions; it is not attested synonymy.

| term | construct | tradition | operational definition located | null-distribution status | evidence tier |
|---|---|---|---|---|---|
| secular bull / secular bear market | long-horizon directional state | practitioner/press | NONE above tier 5 (NB-07 coordinates the taxonomy at title depth; E01 near-miss) | none | tier 5 |
| primary / secondary / minor trend | Dow trend hierarchy | Dow Theory | D58 (prior) | none | book (prior corpus) |
| correction | intermediate countermove | press; academic latent-state | D15 (10% convention, tier 5, source-negative); D22 (bull correction as latent sub-state) | none (D15); inherited MS (D22) | mixed |
| bear market rally | countermove within bear state | press; academic | D22 (prior) | inherited (MS family) | peer-reviewed (prior) |
| capitulation | terminal selling event at a trough | press | NB-06 only | none | preprint |
| market top / market bottom | extremum episode | press/practitioner | NONE academic; NB-06 (troughs, preprint); E13 (tier 5) | none | tier 5 / preprint |
| crash | extreme decline episode | econophysics; press | D27, D41 (prior); NB-01 (episodes, rule in text); NB-02 (outlier drawdown) | **stated** (NB-02; D41/D42 prior) | peer-reviewed |
| downturn | decline episode | press | NONE under this name; operational counterpart is the drawdown episode (NB-02) | stated via NB-02/NB-08 | peer-reviewed (counterpart) |
| drawdown / drawup (temporal episode) | peak-to-trough episode from running extremum | academic probability/econophysics | NB-02 | **stated** (NB-02, NB-08) | peer-reviewed |
| boom / bust | sustained market rise/fall episode | academic macro-finance | NB-10; NB-11 | none | peer-reviewed / working paper |
| bubble / explosive / exuberance | super-exponential or mildly explosive state | academic econometrics; econophysics | NB-03; NB-04; NB-05 | **stated** (NB-04, NB-05: limit theory and critical values) | peer-reviewed |
| parabolic move | accelerating advance | practitioner | NONE attested; correspondence to the explosive regime (NB-03..NB-05) is inferred, not attested | stated for the academic counterpart only | tier-5 term; peer-reviewed counterpart |
| expansion / contraction (as market states) | market-cycle phases | business-cycle import | D52 (prior, clustering import); otherwise a bull/bear wrapper (NB-09) | none | peer-reviewed |
| recession / recovery (as market states) | market-cycle phases | business-cycle import | NONE beyond D27/D52 (prior) | none | (prior only) |
| peak / trough (market cycle) | turning points of a market cycle | dating school | D06-D13, P03, P04 (prior); NB-09; NB-10 | none | peer-reviewed |
| market cycle / cycle phase | bull-bear alternation | academic | NB-09 (synonym evidence: the cycle's phases ARE bull/bear) | none | peer-reviewed |
| crisis / calm | extreme-stress state | academic | D40-D44 (prior); NB-15 ("extreme values are called financial crises") | stated (D41/D42 prior) | peer-reviewed |
| stress / normal | stress continuum with thresholds | academic | D53 (prior); NB-15; NB-16 | inherited (NB-16, MS family) | peer-reviewed |
| fragile | systemic-coupling state | academic | D38 (prior) | implicit (prior) | peer-reviewed (prior) |
| risk-on / risk-off | global risk-aversion episode | practitioner, operationalised academically | NB-12 | none | peer-reviewed |
| flight to quality / flight from quality | stock-bond comovement episode | academic | NB-13 | **stated** (definition and test together) | peer-reviewed |
| flight to safety | day-level safety flight | academic | NB-14 | partial (probabilistic identification) | peer-reviewed |
| volatility regime | high/low volatility states | academic | D20, D28, D50 (prior) | inherited (prior) | peer-reviewed (prior) |
| squeeze | band-width compression state | practitioner (Bollinger) | D17 (prior, tier 5); NB-17 (tier 5) | none | tier 5 |
| compression | low-volatility state | practitioner; agenda vocabulary | NONE academic - two-sweep-stable zero (8.4) | none | tier 5 only |
| narrow range (day) | intraday compression state | practitioner | NONE located at any tier this sweep | none | none located |
| turbulent / quiet | distance-threshold states | academic | D31, D36-D38 (prior) | implicit (prior) | peer-reviewed (prior) |
| breakout (trading-range) | range-exit event | practitioner; academic tests | prior corpus (Brock, Lakonishok & LeBaron 1992; level-corpus records); applications only this sweep (E04, E18, E19) | bootstrap-based tests in the prior defining source | peer-reviewed (prior) |
| momentum burst | short-horizon acceleration event | retail practitioner | NONE at any tier located | none | none located |
| trend day | day-type state | Market Profile | NONE academic (swB-arxiv-04 zero); practitioner side is Agent A's ground | none | tier 5 (Agent A) |
| runs | same-sign sequence of price changes | academic statistics | NB-23 (market application); apparatus NB-18, NB-19, NB-20 | **stated** (exact and asymptotic) | peer-reviewed |
| sequences and reversals | pre-runs count vocabulary | academic (Cowles school) | NB-21; corrected by NB-22 | **stated** (binomial expectation; correction documented) | peer-reviewed |
| drift | deterministic trend component | academic | NONE as a state - a parameter of the null, not a state | n/a | peer-reviewed context |
| persistence | serial dependence / duration dependence | academic | prior (Hurst and DFA records, classification corpus; D21, P04) | prior | peer-reviewed (prior) |
| local trend | local slope state | academic state-space | NONE located as a discrete state (not separately queried - declared in 8.10) | none | - |
| directional change (DC) | event-based alternation states | intrinsic-time school | D54-D56 (prior); NB-25, NB-26, NB-27, NB-28 | NB-29 (renewal reference model, preprint) | peer-reviewed + preprint |
| up mode / down mode | DC alternation states | intrinsic-time | D54 (prior) | none | peer-reviewed (prior) |
| overshoot | post-DC continuation segment | intrinsic-time | D55 (prior); NB-29 (event-share reference value) | stated (NB-29, reference model) | peer-reviewed / preprint |
| intrinsic time / event-based time | event-driven time scale | intrinsic-time | D54-D56 (prior); NB-25 | NB-29 | peer-reviewed |
| market state | regime noun | econometrics; econophysics | prior (D39-D44 and others); session-protocol collision documented (survey 8.2 item 13) | prior | peer-reviewed (prior) |
| market phase | regime noun | 1970s beta literature; metastability school | NB-30 (synonym evidence: phase = major trend); NB-31 (operational, metastable states) | none | peer-reviewed |
| market mode | regime noun | intrinsic-time (D54); RMT homonym | D54 (prior); homonym recorded (E07: dominant correlation eigenvector) | none | peer-reviewed |
| market environment | regime noun | allocator/practitioner | NONE (collision-dominated probe, 8.8) | none | none located |
| market condition | regime noun | Fabozzi-Francis lineage | D01-D05 (prior); probe surfaced only prior coverage (E17) | none | peer-reviewed (prior) |
| market episode | regime noun (productive only in compounds) | academic | via compounds: NB-12 (risk-off episode), NB-16 (stress episode), NB-05 (episodes of exuberance) | varies by compound | peer-reviewed |

### 8.10 Coverage declared unexecuted

Prioritisation followed the dispatch (head terms + highest-value variants).
Variants **not** executed as standalone queries, declared per protocol:
"downturn" and "market top"/"market bottom" as bare phrase queries (folded
into swB-crossref-02/04/05); "parabolic advance"/"going parabolic" as phrases
(covered via the super-exponential family); "range expansion" beyond
swB-crossref-12; "local trend" and "drift" as standalone phrases (see 8.6);
"market state"/"stage" re-probes (prior documentation stands); pagination
beyond the top-10 citation-ranked results for the two high-collision OpenAlex
probes; the two rate-limited Semantic Scholar queries were not re-run within
the session (10.1); non-English surface forms (the registry registers none);
and blowoff/climax/spike vocabulary, which is Agent A's chart-pattern ground.

## 9. Bibliography store

<!-- bibliography-store -->
[references_regime-naming-B.json](references_regime-naming-B.json) - CSL-JSON,
31 entries, one per included record, each carrying a persistent identifier
(29 Crossref DOIs, 2 arXiv DataCite DOIs). Canonical-bytes SHA-256:
`a42f838805ab5769dfaa73b2ad7157866a493fb9aeb114bae225636d0480a347` (also in
frontmatter `bibliography_sha256`). All 31 identifiers resolved through the
DOI Handle System REST API on 2026-08-24 with responseCode 1
(`swB-doicheck-01.json`). The store name retains the dispatch's capital-B
spelling; the review slug is lowercased for the G1 gate (frontmatter
`protocol_amendments`, item iii).

## 10. Limitations and verification gaps

### 10.1 Verification gaps

1. **Semantic Scholar rate-limited both discovery queries** (HTTP 429,
   swB-s2-01/swB-s2-02, logged as executed with zero records). Severity
   minor: both target constructs (DC regime detection; flight-to-safety) were
   independently retrieved through Crossref and OpenAlex, but S2-unique recall
   is untested this session.
2. **Elsevier abstract opacity.** Seven candidate records had no abstract on
   any queried API; five were verified through logged working-paper twins or a
   RePEc page (depth flag T in section 7), and two were excluded rather than
   completed from memory (E02; and the E03 JPM record). No full text of any
   included record was read; extraction depth never exceeds abstract level.
3. **In-text rules not extracted** for NB-01, NB-11, NB-12 (episode thresholds
   stated in paper bodies, flagged inline in 8.0). These are candidates for a
   full-text extraction pass, not settled classifications.
4. **NB-07 and NB-17 rest on title/TOC depth** (tier-5 Wiley chapters, no
   retrievable abstract); they carry vocabulary-coordination weight only.

### 10.2 Recall limitations

Screening-budget caps (rows=8/3; OpenAlex top-10 by citations) bound recall
per query; the two high-collision probes are effectively unpaged. The
known-item list encodes the compiler's priors. Single harvester, single
screener throughout (1.4). Zero-record verdicts ("no academic
operationalization located") are claims about the executed queries, never
existence proofs.

### 10.3 Scope exclusions applied by directive

Agent A's clusters; all predecessor records; re-screening of predecessor
corpora; edits to any predecessor artifact, the agenda, or the failure log.

### 10.4 Gate verdict: `block`, on 8 G16 findings, all false positives

The G1-G20 gate blocks on G16 findings: HEAD requests to doi.org for a subset
of the store's DOIs return HTTP 403 from publisher landing pages that reject
non-browser HEAD requests. The finding set is not even stable across
executions - the first run (2026-08-24) reported eight
(10.1002/9781119197362.ch2, 10.1002/9781119207801.ch10,
10.1080/01621459.1966.10482183, 10.1093/rfs/hhz055, 10.1093/rof/rfn002,
10.1111/iere.12132, 10.1137/090754029, 10.1142/s0219024900000115), the
immediate verbatim re-run reported five (the Wiley ch2, Taylor & Francis, and
SIAM DOIs resolved on retry), and a third run reported nine (adding
10.1111/j.1468-2354.2010.00625.x) - membership churn that is itself evidence
of per-request bot blocking rather than identifier invalidity. Every other
assertion (G1-G15, G17-G20) passed on all runs. Counter-evidence, logged: every
flagged identifier resolves
through the DOI Handle System REST API with responseCode 1
(`swB-doicheck-01.json`, 2026-08-24), and every one returned full registry
metadata via a Crossref GET the same day (`swB-abstracts-01.json`). Per the
dispatch's DOI rule - handle-API responseCode 1 = resolves; publisher 403s are
access failures, not resolution failures - these are false positives, the same
class the regime-definitions survey recorded in its section 10.6 (32 G16
findings, all false positives). No identifier was removed or altered in
response, and the gate's verdict is reported verbatim, not overridden.

### 10.5 What this sweep settles and does not settle

Settled: the academic clusters' synonym families now have per-term
operational-definition and null-status entries (8.0-8.8); five families are
flagged as registry gaps (8.7); the compression negative is now
two-sweep-stable (8.4). Not settled: whether full texts of NB-01/NB-11/NB-12
yield computable thresholds; whether the five flagged families change the
registry's variant counts materially (that is the registry maintainer's
decision); whether S2-unique records exist for the two rate-limited queries.
