---
title: "What is a regime? A scoping survey of operational definitions of market regime and market state, classified by vocabulary, feature space, assignment mechanism, causality at time t, and attached null distribution"
slug: regime-definitions
date: 2026-08-21
objective: "Enumerate every operational definition of a market regime or market state stated anywhere in the peer-reviewed, preprint, software, vendor, or practitioner literature - not how regimes are estimated, which the 96-record regime-classification corpus already covers, but what a regime is defined to BE - and classify each definition on five axes: (a) the state vocabulary it names, (b) the feature space it is defined over, (c) its assignment mechanism, (d) whether the assignment is computable at time t or conditions on the future, and (e) whether any source attaches a null distribution to the regime's existence or assignment."
review_type: scoping
standard_declared: "PRISMA-ScR (Tricco et al. 2018, doi:10.7326/M18-0850) - PARTIAL COMPLIANCE, single screener, adapted to a non-clinical definitional corpus; see section 1.4 for the item-by-item conformance statement. Search reporting follows PRISMA-S conventions where applicable."
eligibility_inclusion:
  - "Any source that states, in terms an implementer could execute or a reader could audit, what constitutes a market regime or market state: the rule, model, or judgment by which a time index (or interval) is assigned a state label, together with the states the source names."
  - "Any source that names and operationalises market phases - bull/bear, expansion/contraction, trend/range, high/low volatility, crisis/calm, turbulent/quiet - including retrospective dating rules and expert-committee procedures."
  - "Any source attaching a hypothesis test, reference distribution, or surrogate-data null to the existence of regimes or to the assignment of states (not merely to model fit)."
  - "Any language; any year; journal article, conference paper, book chapter, preprint, working paper, published software, or vendor/official documentation."
eligibility_exclusion:
  - "Records already included in the 96-record regime-classification corpus (lit_review_regime-classification_2026-08-21.md) or the 81-record level-definitions corpus: cited as prior coverage where definitional content is relevant, never re-included, by task directive."
  - "Records whose only contribution is estimation, testing, or forecasting mechanics for a regime construct defined elsewhere (the prior corpus's ground), or the application of an existing definition to a new market or asset class with no definitional novelty."
  - "Records retrieved in error, where the identifier resolved to a work in an unrelated field - regime is heavily polysemous (regulatory regimes, market-abuse regimes, exchange-rate regimes, political regimes) and this is the dominant exclusion reason."
  - "Theoretical models in which regimes are equilibrium objects with no operational assignment rule for observed data."
  - "Sources with no persistent identifier - vendor pages, official-committee webpages, books not indexed in any DOI registry. These are in scope as definitions, are tier-labelled and synthesised in sections 8.6 and 8.7, but cannot be CSL-JSON store entries because FAIR F1 requires a persistent identifier."
  - "Records duplicating an already-retained work under a second identifier; handled by deduplication, enumerated in the dedup ledger."
registration: not-registered
protocol_path: none
protocol_amendments: "The eligibility criteria were fixed before the first query was executed and were not altered afterwards. Two conduct events are recorded rather than backdated: (i) Semantic Scholar rate-limited two of three queries (HTTP 429); the failed attempts are logged as executed with zero records rather than deleted; (ii) one candidate initially screened in on its title (doi:10.2139/ssrn.57932) was screened out after its abstract was retrieved, because the 'regimes' it defines are equilibrium demand-curve branches with no operational assignment rule - the decision is recorded in section 6, not silently reversed."
bibliography: docs/literature/references_regime-definitions.json
bibliography_sha256: c8659e6086cd92fea034993d13269395c3c75b942752d1e7ca3cd278146de342
n_identified: 352
n_duplicates_removed: 40
n_screened: 312
n_excluded: 258
n_included: 54
materials_availability:
  - docs/literature/search_logs/regime-definitions/
  - docs/literature/references_regime-definitions.json
competing_interests: none
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent) designed and executed every search, screened every record, extracted and classified every definition, and drafted this review. It is the sole screener and is declared as an automation tool under PRISMA-ScR item 9 / PRISMA 2020 item 8. No human second screener participated. Reproducibility log directory: logs/reproducibility/"
git_head_at_authoring: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d"
pip_freeze_sha256: "n/a - no analysis code was executed; only metadata-retrieval scripts (Crossref, arXiv, OpenAlex, Semantic Scholar, DOI handle API) and the bibliography-store script"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-fable-5"
---

# What is a regime? A scoping survey of operational definitions of market regime and market state

## 1. Objective and eligibility

### 1.1 Objective

The regime-classification agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md))
asks whether market state - range, trend, compression, transition - can be
assigned causally at time *t* with a stated null distribution. Its 96-record
corpus ([lit_review_regime-classification_2026-08-21.md](lit_review_regime-classification_2026-08-21.md))
covers **how** regimes are estimated: Markov-switching estimation mechanics,
variance-ratio tests, changepoint detection, scaling-exponent estimators. What
that corpus does not do - and what its own section 8.6 could not do, because no
query asked - is inventory **what a regime is operationally defined to be**
across the literature.

This survey is the missing counterpart, and its methodological model is the
level-definitions survey
([lit_review_level-definitions_2026-08-21.md](lit_review_level-definitions_2026-08-21.md)),
which collected 76 operational definitions of a price level and partitioned
them by a programmatically checkable test; the partition became load-bearing
for the agenda's branch 1. Here the same move is attempted for branch 2's
construct. The axes that matter most to the agenda are:

- **Causality (axis d).** A definition that conditions on data after *t* -
  smoothed state probabilities, full-sample segmentation, peak/trough dating
  with two-sided windows, committee dating with an announcement lag - cannot be
  the basis of a causal-time state assignment, whatever its other merits. Every
  definition that is lookahead **by construction** is flagged.
- **Null distribution (axis e).** The level survey's central finding was that
  almost no definition arrives with a test of its own existence. Whether the
  regime literature does better is this survey's fifth axis.

This review does not assess whether any regime definition is profitable, and
does not backtest anything. Where the only retrievable evidence about a
definition is a performance study, the study is used for its statement of the
definition and its statistical apparatus only.

### 1.2 What counts as an operational definition

A definition is operational here if a competent implementer, given the data the
source names, could assign a state label to each time index (or interval)
without a further interpretive decision the source leaves open - or, for
expert-judgment procedures (NBER, Dow-theory editorials), if the procedure's
inputs, its decision authority, and its timing are stated well enough to audit.
Three failure modes disqualify a statement, as in the level survey:

1. **Name only.** States are named and their significance asserted, but no
   assignment rule is given. The Wyckoff four-phase cycle is the canonical case
   (section 8.7).
2. **Rule with an unbound parameter and no selection procedure.** Conditionally
   operational; the parameter is named and marked `CONVENTION` per charter
   commitment 3, not silently completed.
3. **Rule requiring visual judgement** with no stated numeric test.

**Definitions versus records.** The unit of the corpus is the record; the unit
of the synthesis is the definition. One record can carry several definitions
(Fabozzi & Francis 1977 state three alternative bull/bear definitions; the
`bbdetection` package implements two dating algorithms), and one definition can
recur across records. Section 8 numbers definitions D01-D57; prior-corpus
definitional content is numbered P01-P10 and cited to the prior review, never
re-included as records here.

### 1.3 Grouping for synthesis and the five classification axes

Definitions are grouped by **what assigns the state**: (A) return-partition
threshold rules on realised returns; (B) peak/trough dating algorithms and
committee dating; (C) latent-state parametric models; (D) observable-threshold
autoregressions; (E) multivariate distance and concentration thresholds;
(F) clustering and correlation-structure states; (G) event-based intrinsic-time
definitions; (H) practitioner trend/stage/compression constructs. Each
definition is then classified on the five axes of the objective. The causality
axis takes four values:

- **F** - filtered/online: the state at *t* is computable from data up to *t*
  as the definition is published;
- **B** - both: the defining model admits a filtered (causal) assignment, but
  the published chronologies customarily use smoothed probabilities or
  full-sample estimates (the agenda's filtered-versus-smoothed hazard);
- **R** - retro-dated: an online confirmation signal exists, but the state
  label for times before the confirmation is revised after the fact (threshold
  dating rules of the Lunde-Timmermann and Ned-Davis type);
- **L** - lookahead by construction: the assignment conditions on data after
  *t* and admits no causal variant without redesign (two-sided extremum
  windows, full-sample segmentation or clustering, committee dating).

### 1.4 Conformance statement - this is a single-screener scoping review

> The charter requires dual independent screening with an agreement measure. A
> single agent cannot satisfy that requirement, and two passes by the same model
> are not independent - an agreement statistic between them would measure
> decoding variance, not reliability, and reporting one would be worse than
> reporting none. This review therefore declares **PRISMA-ScR partial
> compliance, single screener**, the same posture, for the same reason, as the
> two prior corpora.

Item-by-item against PRISMA-ScR (Tricco et al. 2018, doi:10.7326/M18-0850):

| PRISMA-ScR item | Status | Note |
|---|---|---|
| 1 Title | met | identifies the report as a scoping review in the frontmatter `review_type` |
| 2 Structured summary | met, adapted | frontmatter `objective` plus section 1.1; no clinical abstract format |
| 3 Rationale, 4 Objectives | met | section 1.1 |
| 5 Protocol and registration | met, negatively | not registered, no protocol; amendments recorded in frontmatter, not backdated |
| 6 Eligibility criteria | met | frontmatter; fixed before the first query and unchanged |
| 7 Information sources | met | section 2, one row per executed query, platform and ISO 8601 date per row |
| 8 Search | met | every query string captured at execution time in the same write as its results (section 3); nothing reconstructed from memory |
| 9 Selection of sources of evidence | met, negatively | one screener, not independent, automation tool declared with version - section 5 |
| 10 Data charting process | **partially met** | single extractor, no duplicate charting, no agreement measure; extraction depth is flagged per record (abstract-verified vs metadata-only) |
| 11 Data items | met | the five classification axes of section 1.3 are the charting schema and appear as columns in section 8 |
| 12 Critical appraisal of individual sources | **not applicable, declared** | optional in PRISMA-ScR; no validated instrument exists for definitional records; the evidence tier per record is a labelling, not an appraisal |
| 13 Synthesis of results (methods) | met | grouping and axes stated in section 1.3 before extraction |
| 14 Selection results | met | frontmatter counts, arithmetic-checked; flow in sections 2 and 5 |
| 15 Characteristics of sources | met | section 7 corpus tables with tier and verification depth |
| 16 Critical appraisal within sources | not applicable | as item 12 |
| 17 Results of individual sources | met | section 8 definition inventory, one row per definition |
| 18 Synthesis of results | met | sections 8.2-8.5 |
| 19 Summary of evidence | met | sections 8.2-8.5 and 8.8 |
| 20 Limitations | met | section 10 |
| 21 Conclusions | met | sections 8.5, 8.8, 10.5 |
| 22 Funding | met | none; frontmatter `competing_interests` |

**Unmet in substance regardless of item wording:** dual screening (9), dual
charting (10), any inter-rater statistic, and any formal appraisal instrument
(12/16). A reader should treat inclusion decisions and axis classifications as
one model's auditable judgements, traceable to the logged text quoted in
section 8, not as consensus.

**Publication-bias posture.** The bias that threatens this review is
retrievability, not small-study effects: definitions that circulate orally, in
proprietary vendor research, or behind broken indexing cannot be retrieved by
bibliographic search. Section 8.7 records which definitions were reachable only
through secondary restatement (the Ned Davis rule, the Wyckoff phases, the
Weinstein stages), and that list is a lower bound on the problem.

## 2. Information sources and methods

<!-- prisma-s-1 -->
One row per executed query. `n_records` is the number of records actually
retrieved and carried into screening, not the total-hit count the API reported;
total-hit counts survive in the raw logs. Rows with `n_records` of 0 are
retained deliberately: three arXiv queries and two rate-limited Semantic
Scholar queries returned nothing, and the three arXiv zeros are among the
most informative results in this review (section 8.8). The `q-websearch` row
carries seven sub-queries (ws-01 to ws-07) targeting the practitioner, vendor
and official-documentation tier; its yields are URL lists, not bibliographic
records, so its `n_records` is 0 by the definition above and its findings are
synthesised in sections 8.6 and 8.7 from the verbatim log
`docs/literature/search_logs/regime-definitions/q-websearch.json`.

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-01 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-02 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-03 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-04 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-05 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-06 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-07 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-08 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-09 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-10 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-11 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-12 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-13 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-14 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-15 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-16 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-17 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-18 | 8 |
| SSRN (via Crossref prefix 10.2139) | Crossref REST API (api.crossref.org), SSRN prefix filter 10.2139 | 2026-08-21 | q-crossref-19 | 8 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-01 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-02 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-03 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-04 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-05 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-06 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-07 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-08 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-09 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-10 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-11 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-12 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-13 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-14 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-15 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-16 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-17 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-18 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-19 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-20 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-21 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-22 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-23 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-24 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-25 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-26 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-27 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-28 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-29 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-30 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-31 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-32 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-33 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-34 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-35 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-36 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-37 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-38 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-39 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-40 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-41 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-42 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-43 | 3 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-44 | 3 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-01 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-02 | 9 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-03 | 10 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-04 | 10 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-05 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-06 | 10 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-07 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-arxiv-08 | 0 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-openalex-01 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-openalex-02 | 10 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-openalex-03 | 10 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-08-21 | q-s2-01 | 0 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-08-21 | q-s2-02 | 10 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-08-21 | q-s2-03 | 0 |
| Web (practitioner/vendor/official tier) | WebSearch tool (Claude Code harness; US-region web index) | 2026-08-21 | q-websearch | 0 |

Sum of `n_records` = **352** = frontmatter `n_identified`. Per-source
subtotals: Crossref topical/title/prefix queries 140 across 19 queries;
Crossref known-item queries 132 across 44 queries; arXiv 40 across 8 queries
(three of them zero); OpenAlex 30 across 3 queries; Semantic Scholar 10 across
3 queries (two rate-limited to zero, recorded as executed); web tier 0
bibliographic records across 7 sub-queries.

Metadata backfills that are not discovery queries and therefore appear in no
row above (they retrieved no new records): `gap-openalex-abstracts.json`
(abstract backfill for included records, one GET per DOI),
`gap-arxiv-2510-00953.xml` (arXiv Atom metadata for a record already retrieved
by q-s2-02), and `gap-doicheck-handle-api.json` (identifier resolution via the
DOI Handle System REST API for all 54 store entries).

## 3. Search strategies

<!-- prisma-s-8 -->
Every query below was captured at execution time from the executing process in
the same write as its results; nothing was reconstructed afterwards. For API
sources the executed query is the full request URL, reproduced verbatim; the
raw response is the log file named by the query_id. For the web tier the
executed queries are the seven verbatim search strings inside the
`q-websearch` block.

```text q-crossref-01
https://api.crossref.org/works?query.bibliographic=market+regime+definition+classification+financial+markets&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-02
https://api.crossref.org/works?query.bibliographic=bull+bear+market+dating+identification+rule&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-03
https://api.crossref.org/works?query.bibliographic=identifying+states+financial+market+correlation+structure&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-04
https://api.crossref.org/works?query.bibliographic=trending+versus+range-bound+market+regime+detection+trading&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-05
https://api.crossref.org/works?query.bibliographic=volatility+regime+high+low+identification+stock+returns&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-06
https://api.crossref.org/works?query.container-title=Journal+of+Econometrics&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-07
https://api.crossref.org/works?query.container-title=Journal+of+Empirical+Finance&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-08
https://api.crossref.org/works?query.container-title=Journal+of+Financial+Econometrics&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-09
https://api.crossref.org/works?query.container-title=International+Journal+of+Forecasting&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-10
https://api.crossref.org/works?query.container-title=Quantitative+Finance&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-11
https://api.crossref.org/works?query.container-title=Journal+of+Business+and+Economic+Statistics&query.title=regime&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-12
https://api.crossref.org/works?query.title=market+regime&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-13
https://api.crossref.org/works?query.bibliographic=risk-on+risk-off+regime+financial+markets+definition&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-14
https://api.crossref.org/works?query.bibliographic=market+states+clustering+unsupervised+learning+stock+returns&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-15
https://api.crossref.org/works?query.bibliographic=Wyckoff+accumulation+distribution+markup+markdown+market+phases&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-16
https://api.crossref.org/works?query.bibliographic=online+real-time+market+regime+detection+filtered+probabilities&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-17
https://api.crossref.org/works?query.bibliographic=crisis+calm+regime+flight+to+quality+turbulent+quiet+periods+asset+returns&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-18
https://api.crossref.org/works?query.bibliographic=volatility+compression+squeeze+consolidation+breakout+range+contraction&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-19
https://api.crossref.org/works?query.bibliographic=market+regime+identification+states&filter=prefix:10.2139&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text ki-01
https://api.crossref.org/works?query.bibliographic=Harding+Pagan+Dissecting+the+cycle+a+methodological+investigation&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-02
https://api.crossref.org/works?query.bibliographic=Bry+Boschan+Cyclical+Analysis+of+Time+Series+Selected+Procedures+and+Computer+Programs&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-03
https://api.crossref.org/works?query.bibliographic=Maheu+McCurdy+Identifying+Bull+and+Bear+Markets+in+Stock+Returns&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-04
https://api.crossref.org/works?query.bibliographic=Maheu+McCurdy+Song+Components+of+bull+and+bear+markets+bull+corrections+and+bear+rallies&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-05
https://api.crossref.org/works?query.bibliographic=Hamilton+Susmel+Autoregressive+conditional+heteroskedasticity+and+changes+in+regime&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-06
https://api.crossref.org/works?query.bibliographic=Engel+Hamilton+Long+swings+in+the+dollar+are+they+in+the+data+and+do+markets+know+it&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-07
https://api.crossref.org/works?query.bibliographic=Tong+Lim+Threshold+autoregression+limit+cycles+and+cyclical+data&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-08
https://api.crossref.org/works?query.bibliographic=Terasvirta+Specification+estimation+and+evaluation+of+smooth+transition+autoregressive+models&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-09
https://api.crossref.org/works?query.bibliographic=Guidolin+Timmermann+International+asset+allocation+under+regime+switching+skew+and+kurtosis+preferences&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-10
https://api.crossref.org/works?query.bibliographic=Ang+Bekaert+International+asset+allocation+with+regime+shifts&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-11
https://api.crossref.org/works?query.bibliographic=Kritzman+Page+Turkington+Regime+shifts+implications+for+dynamic+strategies&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-12
https://api.crossref.org/works?query.bibliographic=Kritzman+Li+Skulls+financial+turbulence+and+risk+management&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-13
https://api.crossref.org/works?query.bibliographic=Chow+Jacquier+Kritzman+Lowry+Optimal+portfolios+in+good+times+and+bad&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-14
https://api.crossref.org/works?query.bibliographic=Hallac+Vare+Boyd+Leskovec+Toeplitz+inverse+covariance-based+clustering+of+multivariate+time+series+data&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-15
https://api.crossref.org/works?query.bibliographic=Guillaume+Dacorogna+Muller+Olsen+Pictet+From+the+birds+eye+to+the+microscope+survey+of+new+stylized+facts+of+the+intra-daily+foreign+exchange+markets&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-16
https://api.crossref.org/works?query.bibliographic=Glattfelder+Dupuis+Olsen+Patterns+in+high-frequency+FX+data+discovery+of+12+empirical+scaling+laws&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-17
https://api.crossref.org/works?query.bibliographic=Tsang+Tao+Serguieva+Ma+Profiling+high-frequency+equity+price+movements+in+directional+changes&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-18
https://api.crossref.org/works?query.bibliographic=Oelschlager+Adam+Detecting+bearish+and+bullish+markets+in+financial+time+series+using+hierarchical+hidden+Markov+models&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-19
https://api.crossref.org/works?query.bibliographic=Filardo+Business-cycle+phases+and+their+transitional+dynamics&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-20
https://api.crossref.org/works?query.bibliographic=Harding+Pagan+A+comparison+of+two+business+cycle+dating+methods&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-21
https://api.crossref.org/works?query.bibliographic=Wilder+New+Concepts+in+Technical+Trading+Systems&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-22
https://api.crossref.org/works?query.bibliographic=Kaufman+Trading+Systems+and+Methods&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-23
https://api.crossref.org/works?query.bibliographic=Weinstein+Secrets+for+profiting+in+bull+and+bear+markets+stage+analysis&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-24
https://api.crossref.org/works?query.bibliographic=Bollinger+on+Bollinger+Bands+squeeze+volatility&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-25
https://api.crossref.org/works?query.bibliographic=Nystrup+Hansen+Madsen+Lindstrom+Regime-based+versus+static+asset+allocation+letting+the+data+speak&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-26
https://api.crossref.org/works?query.bibliographic=Prakash+James+Menzies+Structural+clustering+of+volatility+regimes+for+dynamic+trading+strategies&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-27
https://api.crossref.org/works?query.bibliographic=Mulvey+Liu+identifying+economic+regimes+reducing+downside+risks+for+university+endowments&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-28
https://api.crossref.org/works?query.bibliographic=Hardy+A+regime-switching+model+of+long-term+stock+returns&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-29
https://api.crossref.org/works?query.bibliographic=van+Norden+Schaller+regime+switching+in+stock+market+returns&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-30
https://api.crossref.org/works?query.bibliographic=Pharasi+identifying+long-term+precursors+of+financial+market+crashes+using+correlation+patterns&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-31
https://api.crossref.org/works?query.bibliographic=Burns+Mitchell+Measuring+Business+Cycles&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-32
https://api.crossref.org/works?query.bibliographic=Botte+Bao+A+machine+learning+approach+to+regime+modeling+Two+Sigma&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-33
https://api.crossref.org/works?query.bibliographic=Guidolin+Timmermann+Asset+allocation+under+multivariate+regime+switching+Journal+of+Economic+Dynamics+and+Control&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-34
https://api.crossref.org/works?query.bibliographic=Kole+van+Dijk+How+to+identify+and+forecast+bull+and+bear+markets&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-35
https://api.crossref.org/works?query.bibliographic=Gonzalez+Powell+Shi+Wilson+Two+centuries+of+bull+and+bear+market+cycles&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-36
https://api.crossref.org/works?query.bibliographic=Turner+Startz+Nelson+A+Markov+model+of+heteroskedasticity+risk+and+learning+in+the+stock+market&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-37
https://api.crossref.org/works?query.bibliographic=Fabozzi+Francis+Stability+tests+for+alphas+and+betas+over+bull+and+bear+market+conditions&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-38
https://api.crossref.org/works?query.bibliographic=Sperandeo+Trader+Vic+Methods+of+a+Wall+Street+Master&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-39
https://api.crossref.org/works?query.bibliographic=Edwards+Magee+Technical+Analysis+of+Stock+Trends+The+Dow+Theory&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-40
https://api.crossref.org/works?query.bibliographic=Brown+Goetzmann+Kumar+The+Dow+Theory+William+Peter+Hamilton+Track+Record+Reconsidered&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-41
https://api.crossref.org/works?query.bibliographic=Bemporad+Breschi+Piga+Boyd+Fitting+jump+models+Automatica&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-42
https://api.crossref.org/works?query.bibliographic=Nystrup+Kolm+Lindstrom+Greedy+online+classification+of+persistent+market+states+using+realized+intraday+volatility+features&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-43
https://api.crossref.org/works?query.bibliographic=Kritzman+Li+Page+Rigobon+Principal+components+as+a+measure+of+systemic+risk&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-44
https://api.crossref.org/works?query.bibliographic=Marsili+Dissecting+financial+markets+sectors+and+states&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text q-arxiv-01
http://export.arxiv.org/api/query?search_query=abs:%22market+regime%22+AND+abs:%22definition%22+AND+cat:q-fin*&max_results=10
```
```text q-arxiv-02
http://export.arxiv.org/api/query?search_query=ti:%22market+regime%22&max_results=10
```
```text q-arxiv-03
http://export.arxiv.org/api/query?search_query=ti:%22market+states%22+AND+cat:q-fin*&max_results=10
```
```text q-arxiv-04
http://export.arxiv.org/api/query?search_query=abs:%22regime+detection%22+AND+cat:q-fin*&max_results=10
```
```text q-arxiv-05
http://export.arxiv.org/api/query?search_query=abs:%22bull%22+AND+abs:%22bear%22+AND+abs:%22dating%22+AND+cat:q-fin*&max_results=10
```
```text q-arxiv-06
http://export.arxiv.org/api/query?search_query=abs:%22directional+change%22+AND+abs:%22regime%22&max_results=10
```
```text q-arxiv-07
http://export.arxiv.org/api/query?search_query=abs:%22market+regime%22+AND+abs:%22null+distribution%22&max_results=10
```
```text q-arxiv-08
http://export.arxiv.org/api/query?search_query=abs:%22volatility+compression%22+AND+cat:q-fin*&max_results=10
```
```text q-openalex-01
https://api.openalex.org/works?search=%22market%20regime%22%20operational%20definition&per-page=10
```
```text q-openalex-02
https://api.openalex.org/works?filter=title.search:market%20regimes&sort=cited_by_count:desc&per-page=10
```
```text q-openalex-03
https://api.openalex.org/works?filter=title.search:bull%20and%20bear%20markets&sort=cited_by_count:desc&per-page=10
```
```text q-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20regime%20definition%20financial&fields=title,year,venue,externalIds,citationCount&limit=10
# error: HTTP Error 429: 
```
```text q-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=identifying%20market%20states%20correlation%20clustering&fields=title,year,venue,externalIds,citationCount&limit=10
```
```text q-s2-03
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20regime%20definition%20financial&fields=title,year,venue,externalIds,citationCount&limit=10
# error: HTTP Error 429: 
```
```text q-websearch
ws-01: NBER business cycle dating committee procedure peak trough announcement lag
ws-02: Two Sigma "machine learning approach to regime modeling" white paper four regimes
ws-03: Wyckoff market cycle four phases accumulation markup distribution markdown definition
ws-04: bear market definition "20%" decline origin convention bull market "S&P Dow Jones" OR "Ned Davis"
ws-05: Ned Davis Research bull bear market objective definition "30%" OR "13%" rise 50 days
ws-06: exchange trading session states definition "opening auction" halted continuous trading Nasdaq market state documentation
ws-07: Bollinger Band squeeze definition BandWidth six-month low volatility compression bollingerbands.com
```

<!-- prisma-s-9 -->
**Limits and restrictions (PRISMA-S 9).** No date limits, no language limits,
no study-type limits were applied to any query. Crossref rows were capped at
`rows=8` (topical), `rows=6` (journal-scoped) and `rows=3` (known-item) as a
screening-budget cap, stated here as a limit on retrieval depth, not on
eligibility; total-hit counts in the logs record what lay beyond the cap.
Journal-scoped queries q-crossref-06 to q-crossref-11 restrict
`query.container-title` to the six journals the task directive names.
q-crossref-19 restricts to DOI prefix 10.2139 (SSRN). The arXiv q-fin category
filter appears in five arXiv queries and is part of the verbatim strings above.

<!-- prisma-s-14 -->
**Peer review of the search strategy (PRISMA-S 14 / PRESS).** The strategy was
not peer reviewed. No second searcher existed in this session. The known-item
list (ki-01 to ki-44) was derived from the definitional families named in the
task directive and from backward-citation reasoning over the two prior corpora,
and is therefore vulnerable to the compiler's blind spots; the topical queries
are the check on the known-item list, and sections 8.8 and 10.2 record what
neither could reach.

## 4. Peer review of the strategy

The strategy was not peer reviewed (PRESS statement under `prisma-s-14`,
section 3). Two systematic weaknesses are declared rather than hidden. First,
the known-item queries encode the compiler's prior map of the field; a family
the compiler has never heard of is invisible to them, and the topical queries
- which are the check - returned first pages dominated by polysemy collisions
("regime" is primarily a regulatory and exchange-rate term in Crossref's
relevance ranking; see q-crossref-01 and q-crossref-12). Second, the
practitioner tier was searched through a general web index whose ranking is
opaque and unstable; the seven verbatim strings are logged, but re-running them
will not reproduce the result lists the way re-running an API URL will.

## 5. Managing records

<!-- prisma-s-15 -->
Total records identified per source are the `n_records` column of the section 2
table; they sum to 352. Records were never held in a reference manager: each
query wrote a JSON or Atom log to
`docs/literature/search_logs/regime-definitions/` at execution time, and
screening was performed against those logs.

<!-- prisma-s-16 -->
Deduplication was two-stage and is enumerated record by record in
`docs/literature/search_logs/regime-definitions/dedup-ledger.json`.

- **Stage 1, automated, exact identifier match.** Case-folded DOI; arXiv
  identifier with the version suffix stripped. Software: Python 3.11 standard
  library set operations, executed in this session; no reference-manager or
  commercial deduplication tool was used. The 352 identified records resolve to
  335 distinct identifiers: **17** duplicate instances removed, enumerated in
  the ledger with the queries that co-retrieved each one.
- **Stage 2, manual, same work under a different identifier.** Patterns: a
  working paper or preprint superseded by its published version (SSRN, NBER
  working-paper and arXiv records against journal DOIs); a JSTOR second DOI for
  the same article; a book-chapter reprint of a journal article; one
  KDD-to-IJCAI sister republication; one Palgrave entry under two platform
  editions. **23** further instances removed, enumerated as 18 groups in the
  ledger with the retained identifier named for each. Stage 2 is a
  single-screener judgement and is the weakest step in the flow accounting.

Total duplicates removed: **40**. Records removed as duplicates are not
eligible for the item-16b near-miss table, which lists works excluded on
eligibility grounds.

<!-- prisma-2020-8 -->
Selection process (PRISMA-ScR item 9 / PRISMA 2020 item 8). An LLM screener is
an automation tool in the item's own terms and is named here with its version.

- **screeners_n**: 1
- **independent**: no - single screener; no independent duplicate screening was
  performed and no agreement statistic is reported, for the reason given in
  section 1.4
- **automation_tools**: Claude Fable 5 (model id `claude-fable-5`), running as
  the `research-librarian` agent under Claude Code / Claude Agent SDK. It
  decided every inclusion and exclusion, extracted every definition, and
  assigned every axis classification in section 8. No other automation - no
  machine-learning ranker, no active-learning screener - was used at any stage.

Screening was single-stage on the metadata available in the logs (title,
container, abstract where the API supplied one), followed by abstract-level
assessment for every record that survived, using the abstracts captured in the
query logs or backfilled via OpenAlex (`gap-openalex-abstracts.json`). Where no
abstract could be retrieved at any source, the record was either excluded
rather than included on an unverified extraction (the level survey's E15/E16
rule; applied here to doi:10.2139/ssrn.6067668) or included with its
verification depth marked `metadata-only` and every definitional statement
about it flagged as paraphrase (section 7). One screening decision was reversed
by evidence and is recorded: doi:10.2139/ssrn.57932 screened in on title,
screened out on abstract (section 6, row E1).

## 6. Excluded records

<!-- prisma-2020-16b -->
Records that appeared to meet the inclusion criteria on their metadata and were
excluded after assessment, with a reason each. This is not the full exclusion
list - 258 records were excluded in total - but the near-misses a reader could
reasonably expect to find in the corpus. Bulk exclusions by category are
summarised after the table.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E1 | Market Crashes, Market Regimes, and Regime-Separating Barriers (1998), doi:10.2139/ssrn.57932 | abstract | Screened in on title; the retrieved abstract shows the "regimes" are equilibrium branches of a demand curve in a crash theory. No operational assignment rule for observed data. The title-stage decision is recorded as reversed, not deleted. |
| E2 | A Preference Regime Model of Bull and Bear Markets (2000), doi:10.1257/aer.90.4.1019 | title/abstract | Theoretical model in which the regime is a preference state; no assignment rule. |
| E3 | Day & Huang, Bulls, bears and market sheep (1990), doi:10.1016/0167-2681(90)90061-h | title/abstract | Endogenous heterogeneous-agent dynamics generating bull/bear alternation; regimes are model behaviours, not an assignment rule for data. |
| E4 | A Piecewise-Linear Model For Market Regime Identification (2026), doi:10.2139/ssrn.6067668 | full-text-unavailable | On-topic on its title, but no abstract in any aggregator and SSRN returns HTTP 403 to automated retrieval. Excluded rather than included on an unverified extraction; recorded as a verification gap in section 10.1. |
| E5 | Cross-Asset Market Regime Detection Using Hidden Markov Models (2026), doi:10.2139/ssrn.6539358 | abstract | Vendor-branded application of the standard Gaussian-HMM definition (K selected by BIC); feature-set novelty only, no definitional novelty. |
| E6 | Market Regime Identification Using Hidden Markov Models (2016), doi:10.2139/ssrn.3406068 | title/abstract | Application of the standard HMM definition; no definitional novelty. |
| E7 | Guidolin & Timmermann, International asset allocation under regime switching, skew and kurtosis preferences (2008), doi:10.1093/rfs/hhn006 | abstract | Same four-state definitional content as the included doi:10.1016/j.jedc.2006.12.004; adds preference structure, not definition. |
| E8 | Cai, A Markov Model of Switching-Regime ARCH (1994), doi:10.1080/07350015.1994.10524546 | title/abstract | Estimation-mechanics twin of the included Hamilton & Susmel (1994); the volatility-regime definition is carried there. |
| E9 | Dual betas from bull and bear markets (1993), doi:10.1111/j.1475-6803.1993.tb00147.x | title/abstract | Bull/bear partition of months identical in kind to the included group-A definitions (Fabozzi & Francis 1977; Kim & Zumwalt 1979); adds no definition class. |
| E10 | Review of Bry & Boschan, Cyclical Analysis of Time Series (1973), doi:10.2307/2284114 | title/abstract | Book review; the definitional content is the unindexed NBER book, handled as a no-persistent-ID source in section 8.6. |
| E11 | Review of Bry & Boschan, Cyclical Analysis of Time Series (1972), doi:10.2307/2344336 | title/abstract | As E10. |
| E12 | Reviews of Burns & Mitchell, Measuring Business Cycles (1947; 1948), doi:10.2307/1052315 and doi:10.2307/2549570 | title/abstract | Book reviews; the primary is the unindexed NBER book, handled in section 8.6. |
| E13 | The frequency of regime switching in financial market volatility (2015), doi:10.1016/j.jempfin.2015.03.005 | title/abstract | Estimation mechanics for an already-carried definition family; the prior corpus's ground by directive. |
| E14 | Revisiting the transitional dynamics of business cycle phases with mixed-frequency data (2018), doi:10.1080/07474938.2017.1397837 | title/abstract | Mechanics extension of the included Filardo (1994); no definitional novelty. |
| E15 | Testing for asymmetric dependency structures in financial markets (2023), arXiv:2306.15438 | title/abstract | Tests dependence asymmetry across given regimes; does not define a regime. |
| E16 | Detecting change points in VIX and S&P 500 (2016), doi:10.1057/jam.2016.12 | title/abstract | Changepoint mechanics on a volatility index; the prior corpus's branch-3 ground. |
| E17 | Intelligent trading strategy based on improved directional change and regime change detection (2023), arXiv:2309.15383 | title/abstract | Application; the directional-change definition is carried by three included peer-reviewed records. |
| E18 | Detecting Regime Changes in Financial Markets using HMM and Directional Change (2022), doi:10.36948/ijfmr.2022.v04i05.857 | title/abstract | Application combining two already-carried definitions; low-provenance venue. |
| E19 | High Frequency Finance: Using Scaling Laws to Build Trading Models (2012), doi:10.1002/9781118445785.ch20 | title/abstract | Secondary restatement of the included directional-change records by the same school. |
| E20 | Market regime classification with signatures, arXiv:2107.00066; Non-parametric online market regime detection, arXiv:2306.15835; Market Regime Detection via Realized Covariances, arXiv:2104.03667; Marcucci (2005), doi:10.2202/1558-3708.1145; Ang & Timmermann (2012), doi:10.1146/annurev-financial-110311-101808 | title/abstract | Prior coverage: these works (or their published versions) are included records of the 96-record regime-classification corpus and are excluded here by task directive; their definitional content is cross-referenced as P-entries in section 8. |
| E21 | Logan, Bull Markets / Bear Markets chapters (2014), doi:10.1002/9781118835043.ch8 and .ch9 | title/abstract | Tier-5 chapters restating Dow-style trend phases and threshold conventions already carried by included records. |
| E22 | Opening Range Breakout (2012), doi:10.1002/9781119203933.ch11; TD Range Projection/Expansion (2010), doi:10.1002/9781118531563.ch9 | title/abstract | Range constructs on the price axis, not time-state assignments: the level-definitions corpus's ground by directive. |
| E23 | Speculative Behaviour, Regime-Switching and Stock Market Crashes (1999), doi:10.1007/978-1-4615-5129-4_15 | title/abstract | Crash-prediction application by authors of an included record (van Norden & Schaller 1997); no new definition. |
| E24 | Palgrave Dictionary entry, business cycle measurement, doi:10.1057/9780230226203.0179 | title/abstract | Tertiary reference entry; the primary dating definitions it summarises are included directly (Harding & Pagan) or handled as no-ID sources (Bry & Boschan, Burns & Mitchell, NBER). |

**Bulk exclusions, by reason.** Of 312 screened records, 258 were excluded:
approximately 150 were retrieved-in-error keyword collisions, concentrated in
q-crossref-01 and q-crossref-12 (market-abuse, regulatory and exchange-rate
regimes), q-crossref-15 (Markdown the markup language, retrieved against the
Wyckoff vocabulary), q-crossref-13 (a single Wiley monograph's front matter and
chapters), q-crossref-18 (medical and imaging uses of compression), q-openalex-01
(political and food-market regimes) and q-arxiv-06 (physics uses of directional
change); approximately 55 were estimation-mechanics, forecasting or application
records with no definitional content, concentrated in the six journal-scoped
queries q-crossref-06 to q-crossref-11 (option pricing, copulas, unit-root
tests, forecasting applications of regime-switching models); approximately 25
were profitability or asset-allocation applications of an already-carried
definition; approximately 15 were theory models with no assignment rule,
tier-5 chapters without definitional novelty, dissertations, or components
(figures, front matter); and 5 were prior-coverage records (E20). These
category counts are approximate and exact only in total, because category was
recorded as a screening note rather than a coded field - the same
data-collection weakness the level survey records.

## 7. Included corpus

<!-- included-corpus -->
54 records, every one carrying a persistent identifier (FAIR F1). All 51 DOIs
were resolved live on 2026-08-21 through the DOI Handle System REST API
(`https://doi.org/api/handles/{doi}`, responseCode 1 for every entry; log:
`gap-doicheck-handle-api.json`); the three remaining records carry arXiv
identifiers. The machine-readable form is the CSL-JSON store; this table is the
human-readable index.

**How to read the tables.** The group letter is from section 1.3. `verification`
is the extraction depth: `abstract` means the abstract was captured at query
time or backfilled via OpenAlex/arXiv and every statement made about the record
in section 8 is traceable to that text; `abstract-partial` means the deposited
abstract is truncated in the aggregator; `metadata` means only bibliographic
metadata was retrievable, and every definitional statement about the record in
section 8 is a flagged paraphrase, not a quotation. Tier values follow the
charter hierarchy; **six records are non-refereed (five preprints, one NBER
working paper) and are additionally listed in section 7.1; no downstream
artifact may treat those rows as settled evidence.**

### Group A - return-partition threshold rules (3 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `fabozzi1977j15406261197` | Fabozzi & Francis (1977) Stability Tests for Alphas and Betas over Bull and Bear Market Conditions. *J. Finance* 32:1093-1099. | doi:10.1111/j.1540-6261.1977.tb03312.x | peer-reviewed | metadata | Earliest located record stating **three alternative operational bull/bear definitions** on monthly index returns (D01-D03); the definitions are confirmed secondhand by the abstract of Kim & Zumwalt (1979). |
| `kim19792330303` | Kim & Zumwalt (1979) An Analysis of Risk in Bull and Bear Markets. *J. Financial and Quantitative Analysis* 14:313. | doi:10.2307/2330303 | peer-reviewed | abstract | Confirms the Fabozzi-Francis three-definition scheme and adds its own up/down-market partition (D04). |
| `fabozzi1979j15406261197` | Fabozzi & Francis (1979) Mutual Fund Systematic Risk for Bull and Bear Markets. *J. Finance* 34:1243-1250. | doi:10.1111/j.1540-6261.1979.tb00069.x | peer-reviewed | metadata | Reuse of the month-partition family for fund betas (D05); included as evidence the family was a standard, not a one-off. |

### Group B - peak/trough dating algorithms and their comparisons (8 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `harding2002s03043932010` | Harding & Pagan (2002) Dissecting the cycle: a methodological investigation. *J. Monetary Economics* 49:365-381. | doi:10.1016/s0304-3932(01)00108-8 | peer-reviewed | metadata | The BBQ algorithm: quarterly formalisation of Bry-Boschan two-sided-window turning points with censoring (D07). The canonical statement that dating conditions on a symmetric window around *t*. |
| `harding2003s01651889020` | Harding & Pagan (2003) A comparison of two business cycle dating methods. *J. Economic Dynamics and Control* 27:1681-1690. | doi:10.1016/s0165-1889(02)00076-3 | peer-reviewed | metadata | Rule-based versus Markov-switching dating compared head to head; the definitional families are shown to produce different chronologies from the same data. |
| `gonzalez2005jiref2004020` | Gonzalez, Powell, Shi & Wilson (2005) Two centuries of bull and bear market cycles. *Int. Review of Economics & Finance* 14:469-486. | doi:10.1016/j.iref.2004.02.003 | peer-reviewed | metadata | Long-horizon application of dating rules; carries the definitional variants used for two centuries of data (D09). |
| `gonzalez200623` | Gonzalez, Hoang, Massey & Shi (2006) Defining and Dating Bull and Bear Markets: Two Centuries of Evidence. *Multinational Finance J.* 10:81-116. | doi:10.17578/10-1/2-3 | peer-reviewed | metadata | The only located record whose title is explicitly the definitional question (D10). OpenAlex serves a misattached abstract for this DOI (section 10.1), so extraction is metadata-only. |
| `hanna2018jirfa2017110` | Hanna (2018) A top-down approach to identifying bull and bear market states. *Int. Review of Financial Analysis* 55:150-158. | doi:10.1016/j.irfa.2017.11.001 | peer-reviewed | metadata | Top-down recursive extremum segmentation (D11), the drawdown-first alternative to bottom-up Bry-Boschan windows. |
| `zegado2022jribaf202110` | Zegadlo (2022) Identifying bull and bear market regimes with a robust rule-based method. *Research in International Business and Finance* 60:101603. | doi:10.1016/j.ribaf.2021.101603 | peer-reviewed | metadata | Robust threshold dating rule (D12); the contemporary rule-based line. |
| `kole2016jae2511` | Kole & van Dijk (2016) How to Identify and Forecast Bull and Bear Markets? *J. Applied Econometrics* 32:120-139. | doi:10.1002/jae.2511 | peer-reviewed | abstract | **The axis-d comparison record**: rule-based methods win for in-sample identification, Markov-switching for out-of-sample forecasting; the variance is the ingredient rules discard. |
| `anon2021cranpackageb` | bbdetection: Identification of Bull and Bear States of the Market (2021). CRAN. | doi:10.32614/cran.package.bbdetection | software (CRAN, DOI-carrying) | abstract | Software carrier implementing two prior-corpus dating definitions (Pagan & Sossounov 2002; Lunde & Timmermann 2004) as executable code; evidence of which definitions the ecosystem standardised on. |

### Group C - latent-state parametric definitions (16 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `turner19890304405x8990` | Turner, Startz & Nelson (1989) A Markov model of heteroskedasticity, risk, and learning in the stock market. *J. Financial Economics* 25:3-22. | doi:10.1016/0304-405x(89)90094-9 | peer-reviewed | metadata | Earliest located equity-market two-state definition over mean and variance of index returns (D18). |
| `engel1989w3165` | Engel & Hamilton (1989) Long Swings in the Exchange Rate: Are they in the Data and Do Markets Know It? NBER WP 3165. | doi:10.3386/w3165 | **working paper (NBER)** | abstract | FX long-swing regimes as "a sequence of stochastic, segmented time trends", **with hypothesis testing for the framework stated in the defining source** (D19). Refereed version (AER 1990) not located under any DOI - section 10.1. |
| `hamilton1994030440769490` | Hamilton & Susmel (1994) Autoregressive conditional heteroskedasticity and changes in regime. *J. Econometrics* 64:307-333. | doi:10.1016/0304-4076(94)90067-1 | peer-reviewed | metadata | SWARCH: volatility regimes as multiplicative scale states on an ARCH process; source of the low/moderate/high-volatility vocabulary (D20). |
| `maheu2000073500152000` | Maheu & McCurdy (2000) Identifying Bull and Bear Markets in Stock Returns. *JBES* 18:100-112. | doi:10.1080/07350015.2000.10524851 | peer-reviewed | abstract | Duration-dependent MS: bull = "high-return stable state", bear = "low-return volatile state", labels applied to latent states post hoc; **explicitly filtered** ("the filter identifies all major stock-market downturns") (D21). |
| `maheu2012073500152012` | Maheu, McCurdy & Song (2012) Components of Bull and Bear Markets: Bull Corrections and Bear Rallies. *JBES* 30:391-403. | doi:10.1080/07350015.2012.680412 | peer-reviewed | abstract | Four-state vocabulary bull / bull correction / bear / bear rally as constrained latent states (D22); the intra-regime transition structure is the definition's novelty. |
| `schaller1997096031097333` | van Norden & Schaller (1997) Regime switching in stock market returns. *Applied Financial Economics* 7:177-191. | doi:10.1080/096031097333745 | peer-reviewed | abstract | MS with transition probabilities depending on the price/dividend ratio; **"using new tests, very strong evidence is found for switching behaviour"** - an existence test in the defining source (D23). |
| `filardo1994073500151994` | Filardo (1994) Business-Cycle Phases and Their Transitional Dynamics. *JBES* 12:299-308. | doi:10.1080/07350015.1994.10524545 | peer-reviewed | abstract | Expansion/contraction phases with time-varying transition probabilities (D24); the "transitional dynamics" vocabulary. |
| `ang20021541137` | Ang & Bekaert (2002) International Asset Allocation With Regime Shifts. *Review of Financial Studies* 15:1137-1187. | doi:10.1093/rfs/15.4.1137 | peer-reviewed | abstract | The bear regime defined by jointly higher volatility **and** higher correlation ("correlations ... increase in highly volatile bear markets") (D25). |
| `ang2002073500102317` | Ang & Bekaert (2002) Regime Switches in Interest Rates. *JBES* 20:163-182. | doi:10.1198/073500102317351930 | peer-reviewed | abstract | Interest-rate regimes; regimes validated by external correspondence ("correspond reasonably well with business cycles") rather than by a null (D26). |
| `guidolin2007jjedc2006120` | Guidolin & Timmermann (2007) Asset allocation under multivariate regime switching. *JEDC* 31:3503-3544. | doi:10.1016/j.jedc.2006.12.004 | peer-reviewed | metadata | Four-state multivariate definition whose states are named crash, slow growth, bull and recovery in the body text (naming not verifiable from retrieved text this session - flagged paraphrase) (D27). |
| `hardy2001109202772001` | Hardy (2001) A Regime-Switching Model of Long-Term Stock Returns. *North American Actuarial J.* 5:41-53. | doi:10.1080/10920277.2001.10595984 | peer-reviewed | abstract | RSLN-2: two lognormal regimes on monthly index returns; the actuarial-standard two-state definition (D28). |
| `oelschlger20211471082x2110` | Oelschlager & Adam (2021) Detecting bearish and bullish markets in financial time series using hierarchical hidden Markov models. *Statistical Modelling* 23:107-124. | doi:10.1177/1471082x211034048 | peer-reviewed | abstract | Hierarchical HMM: coarse bullish/bearish long-term states above fine short-term states, explicitly to stop "misinterpretation of short-term price fluctuations as changes in the long-term trend" (D29). |
| `nystrup2015jpm201542110` | Nystrup, Hansen, Madsen & Lindstrom (2015) Regime-Based Versus Static Asset Allocation. *J. Portfolio Management* 42:103-109. | doi:10.3905/jpm.2015.42.1.103 | peer-reviewed (practitioner journal) | abstract | Two-state Gaussian HMM with time-varying parameters, applied with filtered inference out of sample (D30). |
| `kritzman2012fajv68n33` | Kritzman, Page & Turkington (2012) Regime Shifts: Implications for Dynamic Strategies. *Financial Analysts J.* 68(3). | doi:10.2469/faj.v68.n3.3 | peer-reviewed (practitioner journal) | abstract | MS applied not to returns but to **event indices** - market turbulence, inflation, economic growth - defining event regimes (D31). |
| `chan2017073500152017` | Chan, Hansen & Timmermann (2017) Guest Editors' Introduction: Regime Switching and Threshold Models. *JBES* 35:159-161. | doi:10.1080/07350015.2017.1236521 | peer-reviewed | abstract-partial | The family taxonomy record: the field's own split of regime definitions into latent-chain-driven versus observable-threshold-driven (D32's source). |
| `kamenshchikov2016146976882016` | Kamenshchikov (2016) Bifurcation patterns of market regime transition. *Quantitative Finance* 16:1631-1641. | doi:10.1080/14697688.2016.1161230 | peer-reviewed | abstract-partial | The only located record defining the **transition** itself as the object: regime change as a bifurcation between mean-reversion and momentum classes (D33). |

### Group D - observable-threshold autoregressive definitions (2 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `tong1980j25176161198` | Tong & Lim (1980) Threshold Autoregression, Limit Cycles and Cyclical Data. *JRSS-B* 42:245-268. | doi:10.1111/j.2517-6161.1980.tb01126.x | peer-reviewed | abstract | SETAR: the regime at *t* is indexed by which threshold interval a **lagged observable** falls in - causal by construction, and the founding alternative to the latent-chain family (D34). |
| `tersvirta1994016214591994` | Terasvirta (1994) Specification, Estimation, and Evaluation of Smooth Transition Autoregressive Models. *JASA* 89:208-218. | doi:10.1080/01621459.1994.10476462 | peer-reviewed | abstract | STAR: the regime is a **continuous weight** G(y_{t-d}), not a label; and the defining source states "linearity testing against smooth transition autoregression" - an existence null in the definition paper itself (D35). |

### Group E - multivariate distance and concentration thresholds (3 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `chow1999fajv55n32273` | Chow, Jacquier, Kritzman & Lowry (1999) Optimal Portfolios in Good Times and Bad. *Financial Analysts J.* 55(3):65-73. | doi:10.2469/faj.v55.n3.2273 | peer-reviewed (practitioner journal) | abstract | Two risk regimes defined by multivariate-outlier partition: observations whose Mahalanobis distance exceeds a threshold are the turbulent ("bad times") sample (D36). |
| `kritzman2010fajv66n53` | Kritzman & Li (2010) Skulls, Financial Turbulence, and Risk Management. *Financial Analysts J.* 66(5):30-41. | doi:10.2469/faj.v66.n5.3 | peer-reviewed (practitioner journal) | abstract | Financial turbulence index (Mahalanobis distance of the cross-asset return vector); turbulent periods = top quantile (D37). |
| `kritzman2011jpm201137411` | Kritzman, Li, Page & Rigobon (2011) Principal Components as a Measure of Systemic Risk. *J. Portfolio Management* 37:112-126. | doi:10.3905/jpm.2011.37.4.112 | peer-reviewed (practitioner journal) | abstract | Absorption ratio: fraction of total variance absorbed by a fixed number of eigenvectors; fragile versus loosely-coupled market states by standardised shifts of the ratio (D38). |

### Group F - clustering and correlation-structure state definitions (16 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `marsili2002305` | Marsili (2002) Dissecting financial markets: sectors and states. *Quantitative Finance* 2:297-302. | doi:10.1088/1469-7688/2/4/305 | peer-reviewed | abstract | Earliest located clustering definition: market states as clusters of daily market-wide return configurations (D39). |
| `mnnix2012srep00644` | Munnix, Shimada, Schafer, Leyvraz, Seligman, Guhr & Stanley (2012) Identifying States of a Financial Market. *Scientific Reports* 2:644. | doi:10.1038/srep00644 | peer-reviewed | abstract | "We propose a definition of state for a financial market": clusters of correlation-matrix similarity; crisis states and transitions (D40). The founding record of the correlation-state school. |
| `pharasi2018aae7e0` | Pharasi, Sharma, Chatterjee, Chakraborti et al. (2018) Identifying long-term precursors of financial market crashes using correlation patterns. *New J. Physics* 20:103041. | doi:10.1088/1367-2630/aae7e0 | peer-reviewed | abstract | States as clusters "which occur more frequently than by pure chance (randomness)" - a chance criterion attached to state identification; optimal state count by intra-cluster distance; precursor states (D41). |
| `arxiv200307058` | Pharasi, Seligman & Seligman (2020) Market states: A new understanding. arXiv. | arXiv:2003.07058v2 | **PREPRINT** | abstract | Refined selection criteria **plus an explicit null model**: correlated Wishart orthogonal ensemble surrogates for the correlation structure (D42). |
| `arxiv201105984` | Pharasi, Seligman, Sadhukhan, Majari et al. (2020) Dynamics of market states and risk assessment. arXiv. | arXiv:2011.05984v2 | **PREPRINT** | abstract | Adds a transition-matrix criterion to state-count selection - prefer clusterings avoiding large jumps (D43). |
| `wand2023accce0` | Wand, Hessler & Kamps (2023) Identifying dominant industrial sectors in market states of the S&P 500. *J. Statistical Mechanics* 2023:043402. | doi:10.1088/1742-5468/accce0 | peer-reviewed | abstract | Sector-correlation states with XAI relevance scores; state structure dominated by few sector correlations (D44). |
| `procacci2019146976882019` | Procacci & Aste (2019) Forecasting market states. *Quantitative Finance* 19:1491-1498. | doi:10.1080/14697688.2019.1622313 | peer-reviewed | abstract | State = (sparse precision matrix, mean vector); assignment by penalised Mahalanobis minimisation; recovers bull/bear spontaneously; used to forecast off-sample states (D45). |
| `hendricks2016146976882016` | Hendricks, Gebbie & Wilcox (2016) Detecting intraday financial market states using temporal clustering. *Quantitative Finance* 16:1657-1678. | doi:10.1080/14697688.2016.1171378 | peer-reviewed | abstract | Intraday temporal clustering with state signature vectors and "a feasible scheme for real-time intraday state detection from streaming market data feeds" (D46). |
| `hallac2017309798330980` | Hallac, Vare, Boyd & Leskovec (2017) Toeplitz Inverse Covariance-Based Clustering of Multivariate Time Series Data. KDD 2017. | doi:10.1145/3097983.3098060 | peer-reviewed (conference) | abstract | TICC: each state is a Markov random field over a subsequence window; simultaneous segmentation and clustering (D47). |
| `bemporad2018jautomatica2` | Bemporad, Breschi, Piga & Boyd (2018) Fitting jump models. *Automatica* 96:11-21. | doi:10.1016/j.automatica.2018.06.022 | peer-reviewed | metadata | Jump models: state sequence minimises a fitting loss plus a mode-switch penalty; the framework generalising K-means and HMM fitting that the online classifier below builds on (D48). |
| `nystrup2020jfds20202302` | Nystrup, Kolm & Lindstrom (2020) Greedy Online Classification of Persistent Market States Using Realized Intraday Volatility Features. *J. Financial Data Science* 2:25-39. | doi:10.3905/jfds.2020.2.3.025 | peer-reviewed (practitioner journal) | abstract | **The explicit causal-at-t design**: classifies "without any latency", "without the need to parse historical observations", persistence by jump penalty (D49). |
| `prakash20211350486x2021` | Prakash, James, Menzies & Francis (2021) Structural Clustering of Volatility Regimes for Dynamic Trading Strategies. *Applied Mathematical Finance* 28:236-274. | doi:10.1080/1350486x.2021.2007146 | peer-reviewed | abstract | Volatility regimes = clusters of changepoint-delimited segment distributions; learned regime count; online matching of the current distribution to past regimes (D50). |
| `oliveira2026146976882026` | Oliveira, Sandfelder, Fujita, Dong & Cucuringu (2026) Tactical asset allocation with macroeconomic regime detection. *Quantitative Finance*. | doi:10.1080/14697688.2026.2659195 | peer-reviewed | abstract | Macro-feature regimes: modified k-means on FRED-MD with temporal consistency; classifies the current regime and forecasts the distribution of future regimes (D51). |
| `arxiv251000953` | Oliva & Tinjala (2025) Modeling Market States with Clustering and State Machines. arXiv. | arXiv:2510.00953 / doi:10.48550/arXiv.2510.00953 | **PREPRINT** | abstract | Clusters on momentum/risk features feeding a probabilistic state machine; names the states expansion, contraction, crisis, recovery (D52). |
| `yang2026ssrn7245378` | Yang & Qiu (2026) Real-Time Distributional Regime Monitoring: Online Wasserstein Detection of Market Stress. SSRN. | doi:10.2139/ssrn.7245378 | **PREPRINT** | abstract | "A strictly prior-information W1 score" against recursively updated calm/stress barycenters, thresholds "calibrated before 2007 and then frozen" - the only located definition that freezes its calibration window as part of the definition (D53). |
| `anon2012978111920256` | Kaufman (2012) Trend Systems. In *Trading Systems and Methods*, 5th ed., ch. 8. Wiley. | doi:10.1002/9781119202561.ch8 | **tier-5 practitioner (DOI-carrying)** | abstract | The practitioner trend-state canon: trend defined by moving-average and breakout system direction; "being able to identify the trend" as the operative task; parameters unbound (D57). Grouped here for its DOI; classified in group H. |

### Group G - event-based intrinsic-time definitions (3 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `guillaume1997s00780005001` | Guillaume, Dacorogna, Dave, Muller, Olsen & Pictet (1997) From the bird's eye to the microscope. *Finance and Stochastics* 1:95-129. | doi:10.1007/s007800050018 | peer-reviewed | metadata | The directional-change event: price reversal of threshold magnitude from the running extremum flips the market between alternating up and down modes; the intrinsic-time state definition (D54). |
| `glattfelder2011146976882010` | Glattfelder, Dupuis & Olsen (2011) Patterns in high-frequency FX data: discovery of 12 empirical scaling laws. *Quantitative Finance* 11:599-614. | doi:10.1080/14697688.2010.481632 | peer-reviewed | abstract | DC/overshoot segmentation with an "event-based approach" and scaling laws across 13 FX rates (D55). |
| `tsang2016146976882016` | Tsang, Tao, Serguieva & Ma (2016) Profiling high-frequency equity price movements in directional changes. *Quantitative Finance* 17:217-225. | doi:10.1080/14697688.2016.1164887 | peer-reviewed | abstract | DC profiling: "price changes dictate when a price is recorded"; market-state profiles from DC indicators (D56). |

### Group H - practitioner and expert-label definitions with persistent identifiers (3 records)

| id | citation | persistent id | tier | verification | role |
|---|---|---|---|---|---|
| `edwards2018978131511571` | Edwards, Magee & Bassetti (2018) The Dow Theory. In *Technical Analysis of Stock Trends*, 11th ed. CRC. | doi:10.4324/9781315115719-3 | **tier-5 practitioner (DOI-carrying)** | abstract | The primary/secondary/minor trend hierarchy ("tide, wave, and ripple") and bull/bear as primary trends confirmed by both averages (D58). |
| `brown1998002210820005` | Brown, Goetzmann & Kumar (1998) The Dow Theory: William Peter Hamilton's Track Record Reconsidered. *J. Finance* 53:1311-1333. | doi:10.1111/0022-1082.00054 | peer-reviewed | abstract | Expert-label mechanism made auditable: Hamilton's real-time editorial bull/bear calls as state labels, reconstructed by a neural net out of sample (D59). |
| `arxiv260524490` | Pei, Ge, Zheng & Cartlidge (2026) Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems. arXiv. | arXiv:2605.24490v1 | **PREPRINT** | abstract | The newest assignment mechanism located: regime labels and regime-dependent authority multipliers inside a multi-agent LLM system (D60); definitional detail thin, included as evidence of the mechanism class. |

### 7.1 Non-refereed records (charter evidence-tier flag)

Six of the 54 included records are not peer reviewed. Each is flagged so no
downstream artifact can cite one without seeing its tier.

| id | persistent id | tier | why it is nevertheless included |
|---|---|---|---|
| `engel1989w3165` | doi:10.3386/w3165 | working paper (NBER) | The refereed version (Engel & Hamilton, *AER* 1990) was not located under any DOI in Crossref, OpenAlex or Semantic Scholar; the working paper is the only identifier-bearing form of the long-swing definition and its existence test. |
| `yang2026ssrn7245378` | doi:10.2139/ssrn.7245378 | preprint | The only located definition that freezes its calibration window by construction; directly on the agenda's causality axis. |
| `arxiv251000953` | doi:10.48550/arXiv.2510.00953 | preprint | Carries the expansion/contraction/crisis/recovery vocabulary and the state-machine mechanism; no refereed version located. |
| `arxiv200307058` | arXiv:2003.07058v2 | preprint | The correlation-state school's explicit Wishart-ensemble null; no refereed version located. |
| `arxiv201105984` | arXiv:2011.05984v2 | preprint | The transition-matrix selection criterion; no refereed version located. |
| `arxiv260524490` | arXiv:2605.24490v1 | preprint | Evidence of the LLM-judgment assignment mechanism; no refereed version located. |

**Per-group counts.** A: 3. B: 8. C: 16. D: 2. E: 3. F: 16. G: 3. H: 3.
Total 54. Tier counts: peer-reviewed 45 (of which 7 practitioner-journal and 1
conference), non-refereed 6 (5 preprints, 1 working paper), tier-5
practitioner with DOI 2, software 1.

## 8. Synthesis

### 8.0 How to read this section

The unit here is the **definition**, numbered D01-D60. Fifty-three definitions
are carried by included records (section 7); seven (D06, D08, D13-D17) are
carried by sources with no persistent identifier, synthesised in section 8.6
from the logged web-tier evidence and tier-labelled there. One numbered entry
(D32) is not itself a definition but the field's own taxonomy statement. That
leaves **59 operational definitions** catalogued by this survey. Prior-corpus
definitional content is cross-referenced as P01-P11 in section 8.9 and never
double-counted. Statements in quotation marks are verbatim from text captured
in the search logs; unquoted definitional statements for `metadata`-depth
records are flagged paraphrases per section 7.

Axis-d code per section 1.3: **F** filtered/online, **B** both (filtered
computable, smoothed/full-sample customary), **R** retro-dated with an online
confirmation signal, **L** lookahead by construction. Axis-e code: **stated**
(existence/assignment null in the defining source), **inherited** (null exists
in the prior corpus for the model family, not the specific definition),
**implicit** (reference distribution implied by the construct but not framed
as a test), **none**.

### 8.1 The definition inventory

| D | source | definition (verbatim or flagged paraphrase) | states named | features | mechanism | d | e |
|---|---|---|---|---|---|---|---|
| D01 | `fabozzi1977j15406261197` | Bull (bear) month = market index return positive (negative). Paraphrase; scheme confirmed by the Kim & Zumwalt abstract ("three alternative definitions"). | bull, bear (up/down months) | returns (monthly, index) | threshold rule (sign) | F | none |
| D02 | `fabozzi1977j15406261197` | Bull/bear month = "substantial" index move, i.e. magnitude beyond a stated cutoff; cutoff value is a `CONVENTION` (paraphrase). | substantial up, substantial down, neither | returns | threshold rule (magnitude) | F | none |
| D03 | `fabozzi1977j15406261197` | Up/down market defined relative to the market's trend over adjacent months (paraphrase). | up market, down market | returns | threshold rule (relative) | F | none |
| D04 | `kim19792330303` | Up/down-market month partition used to test whether "coefficients of the single-index market model were significantly different in the two types of markets". | bull, bear | returns | threshold rule | F | none |
| D05 | `fabozzi1979j15406261197` | Month-partition reuse for fund systematic risk (paraphrase). | bull, bear | returns | threshold rule | F | none |
| D06 | Bry & Boschan 1971 (no persistent id; section 8.6) | Turning point = local extremum within a two-sided multi-month window, subject to alternation and minimum phase/cycle-length censoring rules (restated via Harding & Pagan). | expansion, contraction; peak, trough | prices/levels (monthly) | dating algorithm | **L** | none |
| D07 | `harding2002s03043932010` | BBQ: peak at t iff the level is the maximum over a symmetric window around t (quarterly), troughs analogous, alternation and censoring enforced (paraphrase). | expansion, contraction; peak, trough | prices (quarterly) | dating algorithm | **L** | none |
| D08 | Burns & Mitchell 1946 (no persistent id; section 8.6) | Reference-cycle phases identified by specialists from many series; the vocabulary's origin (restated). | expansion, recession, contraction, revival | macro aggregates | expert judgment | **L** | none |
| D09 | `gonzalez2005jiref2004020` | Dating-rule bull/bear over two centuries of index data (paraphrase). | bull, bear | prices | dating algorithm | **L** | none |
| D10 | `gonzalez200623` | Explicit comparison of bull/bear definitions and datings (paraphrase; title-level only - the aggregator abstract for this DOI is misattached, section 10.1). | bull, bear | prices | dating algorithm | **L** | none |
| D11 | `hanna2018jirfa2017110` | Top-down recursive segmentation: split at the sample extremum, recurse into sub-segments (paraphrase). | bull, bear | prices | dating algorithm (recursive) | **L** | none |
| D12 | `zegado2022jribaf202110` | Robust rule-based threshold dating of bull/bear regimes (paraphrase). | bull, bear | prices | threshold dating rule | R | none |
| D13 | NBER Business Cycle Dating Committee (official documentation; section 8.6) | "A significant decline in economic activity that is spread across the economy and lasts more than a few months" - depth, diffusion, duration criteria, applied retrospectively by committee; observed announcement lags 4-21 months. | expansion, recession; peak, trough | macro aggregates | expert committee | **L** | none |
| D14 | Ned Davis Research rule (tier-5 restatement; section 8.6) | Bull: +30% in DJIA over 50 calendar days, or +13% after 155 calendar days; bear: -30% over 50 days or -13% after 145 days; Value Line Geometric 30% reversals also qualify. | bull, bear | prices + durations | dual threshold-duration rule | R | none |
| D15 | 20% drawdown convention (no primary source located; section 8.6) | Bear market = decline of at least 20% from the prior peak (bull symmetric from trough). No primary specification located at any tier; one tier-5 source calls the figure "somewhat arbitrary". | bull, bear (also correction at 10%) | prices | threshold rule | R | none |
| D16 | Two Sigma / Botte & Bao 2021 (vendor white paper; section 8.6) | Gaussian mixture model over 17 factor-lens return series; four regimes named post hoc from component moments, including a crisis component. | crisis + three unnamed-by-rule components | multi-factor returns | clustering (GMM, full sample) | **L** | none |
| D17 | Bollinger squeeze (tier-5; section 8.6) | Squeeze = BandWidth ((upper-lower)/middle band) at its lowest value over the trailing six months; six-month lookback is a `CONVENTION`. | squeeze/compression vs normal | volatility (band width) | threshold rule (rolling min) | F | none |
| D18 | `turner19890304405x8990` | Two latent states differing in the mean and variance of index returns; Markov switching (paraphrase). | high/low mean-variance states | returns | latent Markov chain | B | inherited |
| D19 | `engel1989w3165` | "Exchange rate dynamics as a sequence of stochastic, segmented time trends" with "new techniques for ... hypothesis testing". | appreciation, depreciation (long swings) | prices (FX) | latent Markov chain | B | **stated** |
| D20 | `hamilton1994030440769490` | Volatility regimes as multiplicative scale states on an ARCH process (SWARCH) (paraphrase). | low/moderate/high volatility | volatility | latent Markov chain | B | inherited |
| D21 | `maheu2000073500152000` | "The model sorts returns into a high-return stable state and a low-return volatile state. We label these as bull and bear markets"; duration-dependent transition probabilities; "the filter identifies all major stock-market downturns". | bull, bear | returns + durations | latent Markov chain (duration-dependent) | B | inherited |
| D22 | `maheu2012073500152012` | Four latent states with intra-regime dynamics: "bear market rallies and bull market corrections", with "the probability of transition from a bear market rally into a bull market versus back to the primary bear state". | bull, bull correction, bear, bear rally | returns | latent Markov chain (4-state, constrained) | B | inherited |
| D23 | `schaller1997096031097333` | MS states for stock returns with transition probabilities depending on the price/dividend ratio; "very strong evidence is found for switching behaviour". | high-return, low-return states | returns + valuation ratio | latent Markov chain (TVTP) | B | **stated** |
| D24 | `filardo1994073500151994` | "Expansionary and contractionary phases" with "time-varying probabilities of transitions". | expansion, contraction | output (monthly) | latent Markov chain (TVTP) | B | inherited |
| D25 | `ang20021541137` | International regimes where the bear state has "correlations ... increase[d] in highly volatile bear markets" - jointly higher volatility and correlation. | bear/normal (bad times/good times) | returns + correlations | latent Markov chain (multivariate) | B | inherited |
| D26 | `ang2002073500102317` | Interest-rate regimes; validated by correspondence: "the regimes ... correspond reasonably well with business cycles". | high/low rate-volatility regimes | interest rates, spreads | latent Markov chain | B | inherited |
| D27 | `guidolin2007jjedc2006120` | Four multivariate states named crash, slow growth, bull, recovery (body-text naming; flagged paraphrase, not verified from retrieved text). | crash, slow growth, bull, recovery | returns (multi-asset) | latent Markov chain (4-state) | B | inherited |
| D28 | `hardy2001109202772001` | "Regime-switching lognormal model": two lognormal regimes on monthly index returns (RSLN-2). | high/low volatility lognormal regimes | returns | latent Markov chain | B | inherited |
| D29 | `oelschlger20211471082x2110` | Hierarchical HMM: coarse states are "bearish and bullish markets", fine states model short-term dynamics, to prevent "misinterpretation of short-term price fluctuations as changes in the long-term trend". | bullish, bearish (coarse); fine sub-states | returns (two scales) | hierarchical latent Markov chain | B | inherited |
| D30 | `nystrup2015jpm201542110` | Two-state Gaussian HMM with time-varying parameters matching "financial markets' tendency to change behavior abruptly" and persist. | two unnamed persistent regimes | returns | latent Markov chain (adaptive) | B | inherited |
| D31 | `kritzman2012fajv68n33` | "Markov-switching models to forecast regimes in market turbulence, inflation, and economic growth" - regimes of event indices rather than returns. | turbulent/quiet; inflationary; growth/recession | turbulence index, macro variables | latent Markov chain over derived indices | B | inherited |
| D32 | `chan2017073500152017` | Not a definition: the field's own split of the construct into models "with the regime driven by a latent state variable versus an observed variable crossing a threshold" (abstract-partial; paraphrase). | - | - | taxonomy | - | - |
| D33 | `kamenshchikov2016146976882016` | Regime transition modelled as a bifurcation between "mean-reversion and momentum-based" dynamical classes (abstract-partial). | mean-reversion, momentum | returns (dynamical stability) | dynamical-systems analysis, full sample | **L** | none |
| D34 | `tong1980j25176161198` | SETAR: the active regime at t is indexed by which threshold interval the lagged observable falls in; "the threshold value has an interesting interpretation". | regime j of k (unnamed) | lagged observable (returns/levels) | observable threshold | F | inherited |
| D35 | `tersvirta1994016214591994` | STAR: regime membership is the continuous transition function of a lagged observable; "linearity testing against smooth transition autoregression" is part of the specification procedure. | two regimes, continuous mixture | lagged observable | observable threshold (smooth) | F | **stated** |
| D36 | `chow1999fajv55n32273` | "A procedure for identifying multivariate outliers": observations beyond a Mahalanobis-distance threshold form the turbulent-regime sample with its own covariance. | good times, bad times (quiet, turbulent) | multi-asset returns | distance threshold | F | implicit |
| D37 | `kritzman2010fajv66n53` | Financial turbulence = Mahalanobis distance of the cross-asset return vector; turbulent periods = distances in the top quantile (quantile is a `CONVENTION`). | turbulent, quiet | multi-asset returns | distance threshold | F | implicit |
| D38 | `kritzman2011jpm201137411` | "The absorption ratio ... equals the fraction of the total variance of a set of asset returns explained or absorbed by a fixed number of eigenvectors"; fragile state = tightly-coupled market flagged by standardised AR shifts. | fragile/tightly-coupled vs loosely-linked | return covariance spectrum | concentration threshold | F | implicit |
| D39 | `marsili2002305` | "Patterns of daily market-wide economic activity cluster into classes that can be identified with market states." | market states (unnamed clusters) | cross-sectional daily returns | clustering (max-likelihood, full sample) | **L** | none |
| D40 | `mnnix2012srep00644` | "We propose a definition of state for a financial market": clusters of similar correlation matrices; "characteristic correlation structure patterns can be classified into several typical market states". | market states incl. crisis states | correlation matrices | clustering (similarity, full sample) | **L** | none |
| D41 | `pharasi2018aae7e0` | "Market states as clusters of similar correlation structures, which occur more frequently than by pure chance (randomness)"; optimal state count by intra-cluster distance; the state adjacent to the crash state is a precursor. | S&P 500: four states; Nikkei: five; critical/crash state, precursor state | correlation matrices (power-mapped) | clustering, k optimised, full sample | **L** | **stated** (chance criterion) |
| D42 | `arxiv200307058` | States as correlation-matrix clusters with an explicit noise null: "we use the correlated Wishart orthogonal ensemble for the construction of surrogate data". | four (USA) / six (JPN) market states | correlation matrices | clustering + surrogate null | **L** | **stated** (Wishart surrogate) |
| D43 | `arxiv201105984` | Cluster selection "avoids large jumps in the transition matrix"; market trajectory in correlation-matrix space. | market states (numbered) | correlation matrices | clustering + transition-matrix criterion | **L** | none |
| D44 | `wand2023accce0` | "Dynamics of sector correlation matrices ... described by a sequence of distinct states via a clustering algorithm"; states dominated by few sector correlations. | market states (sector-driven) | sector correlation matrices | clustering + XAI attribution | **L** | none |
| D45 | `procacci2019146976882019` | "Market states are identified by a reference sparse precision matrix and a vector of expectation values"; assignment "accordingly to a minimization of a penalized Mahalanobis distance"; recovers "the common classification of bull and bear markets". | states (bull/bear recovered) | multivariate returns (precision structure) | model-based clustering, online-assignable | F | none |
| D46 | `hendricks2016146976882016` | Intraday states via "high-speed maximum likelihood clustering ... from intraday market microstructure features", with "state signature vectors which enable online state detection" and "a feasible scheme for real-time intraday state detection". | intraday market states (hierarchy) | microstructure features, correlations | temporal clustering, online detection | F | none |
| D47 | `hallac2017309798330980` | "Each cluster ... is defined by a correlation network, or Markov random field, characterizing the interdependencies ... of that cluster"; simultaneous segmentation and clustering. | states/clusters (unnamed) | multivariate subsequences | segmentation + clustering (TICC), full sample | **L** | none |
| D48 | `bemporad2018jautomatica2` | Jump models: fit a state sequence by minimising fitting loss plus a mode-transition penalty (paraphrase). | modes (unnamed) | model residuals | regularised segmentation, full sample | **L** | none |
| D49 | `nystrup2020jfds20202302` | "A greedy online classifier that contemporaneously determines which hidden state a new observation belongs to without the need to parse historical observations and without compromising persistence ... penalizing jumps between states by a fixed-cost regularization term." | persistent market states (unnamed) | realized intraday volatility features | online jump-model classification | F | none |
| D50 | `prakash20211350486x2021` | "Change point detection to partition a time series into locally stationary segments", distance matrix between segment distributions, "clustered into a learned number of discrete volatility regimes". | volatility regimes (learned count) | volatility (segment distributions) | changepoint + clustering, full sample | **L** | none |
| D51 | `oliveira2026146976882026` | "A modified k-means algorithm to ensure consistent regime classification over time" on FRED-MD macro features; "classifies current regimes, forecasts the distribution of future regimes". | macro regimes (unnamed) | macroeconomic variables (FRED-MD) | temporal-consistent k-means | F | none |
| D52 | `arxiv251000953` | "Clustering historical returns based on momentum and risk features across multiple time horizons, we identify distinct market states ... such as expansion phase, contraction, crisis, or recovery. From a transition matrix ... we construct a probabilistic state machine." | expansion, contraction, crisis, recovery | returns (momentum + risk features) | clustering + state machine | **L** | none |
| D53 | `yang2026ssrn7245378` | "A strictly prior-information W1 score compares each current distribution with recursively updated low- and high-stress barycenters; thresholds are calibrated before 2007 and then frozen." | stress, calm/normal | return distributions (rolling) | distributional distance threshold, frozen calibration | F | none (inference on detection performance only, Holm-corrected) |
| D54 | `guillaume1997s00780005001` | Directional-change event: a price reversal of threshold magnitude from the running extremum flips the market between alternating up and down modes; event scale replaces clock time (paraphrase). | up mode, down mode (alternating) | prices (event-based) | event threshold (intrinsic time) | F | none |
| D55 | `glattfelder2011146976882010` | "An event-based approach that measures the relationship between different types of events" - DC and overshoot segments; 12 scaling laws. | directional-change/overshoot segments | prices (event-based) | event threshold | F | none |
| D56 | `tsang2016146976882016` | "Instead of sampling at fixed intervals, DC is data driven: price changes dictate when a price is recorded"; market profiles built from DC indicators. | uptrend/downtrend events; profiled states | prices (event-based) | event threshold + profiling | F | none |
| D57 | `anon2012978111920256` | Trend state = the direction indicated by a trend system: "the moving average is still a consistent top performer, but the breakout often has higher returns"; parameters (lookback N) unbound `CONVENTION`. | trending (long/short side) vs not | prices (smoothed) | indicator threshold | F | none |
| D58 | `edwards2018978131511571` | Dow Theory: the market's "general trend" in three superposed movements ("tide, wave, and ripple" - primary, secondary, minor); bull/bear are primary trends, confirmed by both averages. | bull, bear; primary, secondary, minor | price averages (two indices) | pattern/confirmation rule | R | none |
| D59 | `brown1998002210820005` | State labels are Hamilton's real-time editorial calls: "editorials published by ... William Peter Hamilton" classified bullish/bearish/doubtful; reconstructed by "neural net modeling to replicate Hamilton's market calls". | bullish, bearish, doubtful | expert reading of price averages | expert hand label (real-time) | F (expert) | none |
| D60 | `arxiv260524490` | Regime labels and "regime-dependent multipliers to adjust agent authority" inside a multi-agent LLM allocation system (definitional detail thin). | regimes (unnamed) | model-internal | LLM/model judgment | F | none |

### 8.2 The naming-convention taxonomy (axis a)

Vocabularies located, with the definitions that carry them:

1. **bull / bear** - the dominant convention. Carried by threshold rules
   (D01-D05, D14, D15), dating algorithms (D06-D12), latent-state models
   (D21, D22, D27, D29), a recovered clustering label (D45), and expert labels
   (D58, D59). The same word pair is defined at least five structurally
   different ways; a "bull" under D01 (positive month) and a "bull" under D21
   (latent high-return stable state) are different objects that share a name.
2. **expansion / contraction / recession / recovery** - business-cycle
   vocabulary (D07, D08, D13, D24), imported into markets by D52
   (expansion, contraction, crisis, recovery).
3. **high / moderate / low volatility** - D20, D28, D50, and the entire
   MS-GARCH family (P02).
4. **turbulent / quiet, good times / bad times, fragile** - the
   distance-threshold school (D36-D38, D31).
5. **crisis / calm, stress / normal** - correlation-state clustering (D40-D44)
   and distributional monitoring (D53); crisis is the one state label that
   clustering papers assign by inspection almost universally.
6. **trend / trending vs non-trending (range)** - practitioner vocabulary
   (D57, D58); in the peer-reviewed corpus the pair appears as
   **momentum vs mean-reversion** (D33) rather than trend vs range.
7. **up mode / down mode, uptrend / downtrend events** - intrinsic-time
   vocabulary (D54-D56).
8. **bull correction / bear rally** - transitional sub-states (D22), the only
   located peer-reviewed vocabulary for within-regime countermoves.
9. **squeeze / compression** - tier-5 only (D17). **No peer-reviewed
   definition names a compression state** (section 8.8).
10. **crash / slow growth / bull / recovery** - D27's four-state naming.
11. **appreciation / depreciation (long swings)** - FX vocabulary (D19).
12. **accumulation / markup / distribution / markdown** - Wyckoff; name-only,
    no operational rule located at any tier (section 8.7).
13. **Term collision, recorded**: exchanges and SEC filings use "market state"
    / "Limit State" / "Trading Pause" for the venue's session protocol state -
    a deterministic state machine unrelated to this construct (ws-06). Any
    corpus search for "market state" inherits this collision.

**Against the agenda's four-state vocabulary (range, trend, compression,
transition):** *trend* has peer-reviewed operational counterparts only via
momentum/mean-reversion (D33) and the practitioner tier (D57, D58); *range* as
a market state (as opposed to a price construct, the level corpus's ground)
has none located; *compression* has none above tier 5 (D17); *transition* is
named as an object only by D33 (bifurcation) and D22 (transitional
sub-states), plus transition matrices in every clustering definition. The
agenda's vocabulary is, on this evidence, largely a practitioner vocabulary
without a peer-reviewed definitional base - a finding, not a defect.

### 8.3 Feature space (axis b)

| feature space | definitions | n |
|---|---|---|
| univariate returns (incl. durations) | D01-D05, D18, D21, D22, D23 (+valuation), D24, D28, D29, D30, D33, D34, D35 | 16 |
| price levels / extrema | D06-D15, D54-D56, D57, D58 | 16 |
| volatility / band width | D17, D20, D49, D50 | 4 |
| multivariate returns, correlation or precision structure | D16, D25, D26, D27, D36-D48 | 18 |
| return distributions as objects | D53 | 1 |
| macro variables / event indices | D08, D13, D31, D51 | 4 |
| expert or model-internal | D59, D60 | 2 |

(D23 and D26 counted once each under their primary space; overlaps are noted
inline.) Two absences matter to the agenda: **no located definition is built
on volume** (volume enters only as a confirmation heuristic in the Wyckoff and
Dow traditions, neither operationalised), and **no located definition is built
on order flow or the order book** - the microstructure features in D46 are
correlation inputs, not book states. Both absences are registered in 8.8.

### 8.4 Assignment mechanism (axis c)

The field's own taxonomy (D32) splits mechanisms into latent-state versus
observable-threshold. The located corpus needs six classes:

| mechanism | definitions | n |
|---|---|---|
| threshold rule on an observable | D01-D05, D12, D14, D15, D17, D34, D35, D36-D38, D53, D57 | 16 |
| peak/trough dating algorithm (two-sided windows) | D06, D07, D09, D10, D11 | 5 |
| latent-state model (HMM/MS and hierarchical) | D18-D31 | 14 |
| clustering / segmentation (incl. state machines, jump models) | D16, D39-D52 | 15 |
| event-based intrinsic time | D54-D56 | 3 |
| expert or model judgment | D08, D13, D59, D60 | 4 |
| (taxonomy record, dynamical analysis) | D32, D33 | 2 |

### 8.5 Causality at time t (axis d) - the agenda's central axis

Classification of the 59 operational definitions:

| class | n | definitions |
|---|---|---|
| **F** - computable at t as published | **22** | D01-D05, D17, D34-D38, D45, D46, D49, D51, D53-D57, D59, D60 |
| **B** - filtered computable; smoothed/full-sample customary | **14** | D18-D31 |
| **R** - retro-dated; online confirmation exists, labels revised | **4** | D12, D14, D15, D58 |
| **L** - lookahead by construction | **19** | D06-D11, D13, D16, D33, D39-D44, D47, D48, D50, D52 |

**Findings.**

1. **19 of 59 definitions (32%) are lookahead by construction.** Every
   peak/trough dating algorithm conditions on a two-sided window or the full
   sample; committee dating adds an announcement lag the NBER's own FAQ
   documents at 4 to 21 months (ws-01); every full-sample clustering assigns
   states using data after *t*. None of these can serve the agenda's causal
   assignment question without redesign, though several (D40-D44) could be
   given filtered variants, and D45/D46/D49/D51/D53 are exactly such variants
   built by their authors.
2. **The entire latent-state family (14 definitions) is causal-capable but
   customarily reported non-causally.** Filtered probabilities are computable
   at *t* (D21 says so verbatim); the published regime chronologies typically
   plot smoothed probabilities - the prior corpus's Kim (1994) record is the
   source of those smoothers. The agenda's planned catalogue of which
   published regime charts are smoothed (branch 2) is therefore well-posed
   over this group.
3. **Retro-dating is a distinct failure mode from lookahead.** D14-type rules
   emit a causal confirmation signal (the day the +30%/50-day condition
   triggers) but then relabel history back to the trough. Any backtest that
   uses the final labels at their nominal dates inherits lookahead even though
   the rule is online. The distinction is absent from every tier-5 source
   restating these rules.
4. **The explicitly causal designs are recent and concentrated**: D49 (2020),
   D51, D53 (2026), D45/D46 (2016-2019) - the online-classification turn is
   roughly a 2016-and-later phenomenon, consistent with the prior corpus's
   finding that filtered-vs-smoothed discipline is historically weak.

### 8.6 Definitions carried by sources with no persistent identifier

Tier-labelled per the charter hierarchy; none of these is a store entry (FAIR
F1). Verbatim evidence and URLs are in `q-websearch.json`.

| D | source | tier | status |
|---|---|---|---|
| D06 | Bry & Boschan (1971), *Cyclical Analysis of Time Series*, NBER. Not DOI-indexed; located only through two book reviews (excluded, E10/E11) and the Harding-Pagan restatement. | book (not indexed) | operational, restated secondhand |
| D08 | Burns & Mitchell (1946), *Measuring Business Cycles*, NBER. Not DOI-indexed; located through reviews (E12). | book (not indexed) | operational only as expert procedure; vocabulary origin |
| D13 | NBER Business Cycle Dating Committee procedure, nber.org (ws-01). | official documentation (tier 2) | operational as auditable committee procedure; lookahead by construction with documented 4-21 month announcement lag |
| D14 | Ned Davis Research bull/bear rule (ws-05). | tier 5 (secondary restatement only; NDR primary not retrieved) | operational; fully stated thresholds and durations; provenance weak |
| D15 | The 20% bear-market convention (ws-04). | tier 5 | operational but **source-negative**: no primary specification located; same evidentiary status as the Market Profile 70% value area in the prior corpus |
| D16 | Botte & Bao (2021), *A Machine Learning Approach to Regime Modeling*, Two Sigma (ws-02; ki-32 confirmed not DOI-indexed). | tier 5 (vendor) | operational (GMM, 17 factors, 4 regimes); named post hoc |
| D17 | Bollinger BandWidth squeeze, StockCharts formalisation of Bollinger (ws-07; ki-24 confirmed the book is not DOI-indexed). | tier 5 (vendor/education) | operational; the only located compression-state definition at any tier |

### 8.7 Constructs for which no operational statement was found

- **Wyckoff four phases** (accumulation, markup, distribution, markdown): ten
  tier-5 URLs restate the vocabulary (ws-03); none states thresholds, windows
  or a volume test; q-crossref-15 returned only keyword collisions. Name-only.
- **Weinstein stage analysis** (stages 1-4 around a 30-week moving average):
  the book is not DOI-indexed (ki-23 returned unrelated Wiley chapters) and no
  primary or secondary statement was retrieved this session; recorded as
  located-by-citation only, not classified.
- **"Range" as a market state**: no source at any tier defines a range-bound
  *state* operationally as distinct from a price *range* (the latter is the
  level corpus's ground). The nearest object is the absence of a DC event
  (D54) or a non-trending reading of D57's systems - both by negation.
- **Prior-corpus folklore negatives stand**: ADX and the Choppiness Index
  remain without any source above tier 5 and without null distributions
  (prior corpus, section 8.5); the Kaufman Efficiency Ratio remains without a
  published null. Nothing found here changes those verdicts.

### 8.8 Null distributions (axis e) - the mirror of the level survey's finding

Of 59 operational definitions:

| axis-e status | n | definitions |
|---|---|---|
| **stated** in the defining source | **5** | D19 (test of segmented trends vs random walk), D23 ("new tests" for switching), D35 (linearity test against STAR), D41 (states "more frequent than by pure chance"), D42 (correlated Wishart orthogonal ensemble surrogates) |
| **inherited** from the prior corpus's testing literature (family-level, not definition-level) | 15 | D18, D20-D31 (MS family: Hansen 1992, Garcia 1998, Cho & White 2007, Carrasco et al. 2014 - all prior corpus), D34 (SETAR: Petruccelli 1990, prior corpus) |
| **implicit** reference distribution, not framed as a test | 3 | D36-D38 (Mahalanobis distance under multivariate normality) |
| **none** | **36** | all of groups A and B, all practitioner definitions, all event-based definitions, and 11 of the 16 clustering definitions |

Registered zero-record searches bearing on this axis, first-class results by
project protocol:

- **q-arxiv-07** - `abs:"market regime" AND abs:"null distribution"` -
  **0 records** in all of arXiv. The exact conjunction the agenda needs has no
  preprint literature.
- **q-arxiv-05** - `abs:"bull" AND abs:"bear" AND abs:"dating" AND cat:q-fin*`
  - **0 records**: the bull/bear dating literature predates or bypasses arXiv
  q-fin entirely; it lives in journals.
- **q-arxiv-08** - `abs:"volatility compression" AND cat:q-fin*` - **0
  records**: compression as a named state has no q-fin preprint literature.

**Conclusion on axis e, mirroring the level survey:** no source at any tier
attaches a null distribution to the *assignment* of a state label at time t
(the probability of the label under a no-regime process); the five stated
nulls test regime *existence* model-wide (D19, D23, D35) or state-count
significance against noise (D41, D42). The correlation-state school's
Wishart-surrogate practice (D42) is the closest located analogue of the random
-relocation null the agenda's branch 1 adopted, and is the single most
transferable methodological finding of this survey: it is a null over the
feature structure (correlations) holding the marginals fixed, stated and
implemented in the defining source.

### 8.9 Prior-corpus definitional cross-references (P-entries; not re-included)

| P | prior-corpus record | definitional content | d |
|---|---|---|---|
| P01 | Hamilton (1989), doi:10.2307/1912559 | The founding latent-state definition: regime = current value of an unobserved K-state first-order Markov chain indexing AR parameters; filtered probability computable at t | B |
| P02 | Gray (1996); Haas (2004); Klaassen (2002); Marcucci (2005) | Volatility regimes in (MS-)GARCH form | B |
| P03 | Pagan & Sossounov (2002), doi:10.1002/jae.664 | Bull/bear dating by windowed extrema (monthly BB adaptation) | L |
| P04 | Lunde & Timmermann (2004), doi:10.1198/073500104000000136 | Bull/bear filter by threshold moves from running extrema; duration dependence of phases | R |
| P05 | Bulla & Bulla (2006); Yu (2010); Chiappa (2014); Xu & Liu (2021) | Duration-explicit (semi-Markov) states: regime persistence as the defined object | B |
| P06 | Ryden et al. (1998), doi:10.1002/(sici)1099-1255(199805/06)13:3<217::aid-jae476>3.0.co;2-v | HMM states as reproducers of stylized facts; documents what the two-state definition fails to reproduce | B |
| P07 | Horvath et al. (2024), doi:10.21314/jcf.2024.005 | Regimes as Wasserstein clusters of return distributions | L |
| P08 | Luan & Hamp (2025), doi:10.3934/dsfe.2025016 | Sliced-Wasserstein k-means regimes | L |
| P09 | Bucci & Ciciretti (2022), doi:10.1016/j.econmod.2022.105832 | Regimes from realized covariances (unsupervised vs nonlinear models) | L |
| P10 | Bilokon et al. (2021), arXiv:2107.00066 | Path-signature feature regimes (preprint tier) | L |
| P11 | Issa & Horvath (2023), arXiv:2306.15835 | Non-parametric **online** regime detection (preprint tier) | F |

The prior corpus also carries the existence-test apparatus this survey's
axis-e "inherited" rows point to (Hansen 1992; Garcia 1998; Cho & White 2007;
Carrasco et al. 2014; Petruccelli 1990) and the filtered-vs-smoothed machinery
(Hamilton 1989; Kim 1994; Chauvet & Piger 2008). None of that ground is
re-swept here.

## 9. Bibliography store

<!-- bibliography-store -->
The canonical machine-readable corpus is
[references_regime-definitions.json](references_regime-definitions.json):
CSL-JSON, 54 entries, exactly the included corpus of section 7 - excluded
near-misses and no-persistent-ID sources are not in the store. Every entry
carries a DOI or an arXiv identifier (FAIR F1). Entries were resolved at add
time by live content negotiation (Crossref/DataCite via doi.org) or, for the
three arXiv-only records and the DataCite-registered arXiv DOI, from arXiv
Atom API metadata fetched this session; no entry was typed from memory. The
store digest in the frontmatter (`bibliography_sha256`) is the SHA-256 of the
canonical serialization, written by `build_bibliography.py sync-sha`.
Identifier resolution was additionally verified through the DOI Handle System
REST API with `responseCode` 1 for all 51 DOIs
(`gap-doicheck-handle-api.json`).

## 10. Limitations and verification gaps

### 10.1 Verification gaps

1. **Semantic Scholar coverage is partial.** q-s2-01 and its retry q-s2-03
   were rate-limited (HTTP 429) and returned zero records; only q-s2-02
   executed. The failed attempts are logged as executed. Severity: the S2
   platform contributed one-third of its intended discovery surface.
2. **SSRN blocks automated retrieval** (HTTP 403 on paper pages). One on-topic
   candidate (doi:10.2139/ssrn.6067668) was excluded rather than included on
   an unverified extraction (E4). SSRN records that Crossref carries abstracts
   for were unaffected.
3. **OpenAlex serves a misattached abstract for doi:10.17578/10-1/2-3**
   (Gonzalez et al. 2006): the text describes share buy-backs, not bull/bear
   dating. The record is held at `metadata` depth and the defect is recorded
   here so no downstream artifact quotes that abstract. The store entry's
   bibliographic fields come from Crossref, not OpenAlex.
4. **Thirteen included records are at `metadata` extraction depth** (flagged
   per row in section 7): every definitional statement about them in section 8
   is a paraphrase from bibliographic metadata and secondary confirmation, not
   from retrieved text. The three Elsevier dating-rule records (D09-D12
   sources) and Guidolin & Timmermann (D27's naming) are the materially
   affected cases.
5. **Engel & Hamilton's refereed version (AER 1990) has no located DOI**; the
   included record is the NBER working paper. The definitional content is
   identical by title and abstract, but the published text was not verified.
6. **The Ned Davis Research rule (D14) was reachable only through tier-5
   restatements.** The thresholds are consistently quoted across independent
   secondary sources, but the primary document was not retrieved.
7. **Gate G16 note.** The research-compile gate resolves DOIs by HTTPS HEAD
   against publisher redirect targets, which 403 automated requests for
   several publishers. The task directive's resolution criterion - Handle
   System API `responseCode` 1 - was met by all 51 DOIs, logged in
   `gap-doicheck-handle-api.json`. Any G16 findings in the gate output that
   correspond to publisher-page 403s are false positives under the directive's
   criterion, mirroring the disposition recorded by both prior corpora.

### 10.2 Recall limitations

- Crossref retrieval was capped per query (8/6/3 rows); total-hit counts in
  the logs show what lay beyond the caps. The known-item layer compensates
  only for families the compiler could name; section 4 states the
  consequence.
- The practitioner tier was searched through one general web index; oral,
  video and paywalled vendor research is unreachable, and section 8.7's list
  of secondary-only definitions is a lower bound.
- Book-indexing databases were not searched beyond Crossref's book-chapter
  coverage; Bry-Boschan, Burns-Mitchell, Wilder, Bollinger and Weinstein are
  "not DOI-indexed", not "not published".
- Non-English literatures were not deliberately queried; one Indonesian record
  was retrieved and excluded, which measures spillover, not coverage.

### 10.3 Screening and extraction limitations

Single screener, single extractor, no agreement measure (section 1.4). Axis
classifications - especially the F/B/R/L causality calls for `metadata`-depth
records - are one model's judgements. The R class in particular required
reading a rule's confirmation structure out of secondary text for D14/D15.
Category counts in the bulk-exclusion summary are approximate, exact only in
total.

### 10.4 Scope exclusions applied by directive

Estimation mechanics, testing mechanics and changepoint machinery (the
96-record corpus's ground) were not re-swept; profitability was not assessed;
price-level and range constructs on the price axis (the 81-record corpus's
ground) were excluded as level-definitions territory (E22). Records of the
prior corpora retrieved again by this survey's queries were excluded as prior
coverage (E20) and cross-referenced as P-entries.

### 10.5 What this review does not settle

It does not adjudicate which definition the agenda should adopt; it maps the
choices and their causality/null status. It does not resolve whether the
agenda's four-state vocabulary (range, trend, compression, transition) can be
grounded in the peer-reviewed literature - the evidence in 8.2 says mostly
not, which makes the agenda's branch-2 definitional choice a construct
decision the project must make and defend, not one it can cite its way out
of. And it does not supply the missing object the corpus-wide search
confirms absent: a null distribution for a state assignment at time t.

### 10.6 Gate verdict: `block`, on 32 G16 findings, all false positives

`check_lit_review.py` was run against this file on 2026-08-21. Every assertion
except G16 passed: no G1-G15 and no G17-G20 findings. The verdict is `block`
solely because G16 resolves DOIs by HTTPS request against publisher redirect
targets, and 32 of the 51 DOIs returned HTTP 403 (Elsevier, Wiley, OUP, T&F,
CFA Institute, ACM, SAGE, SSRN front ends refusing automated requests) or
HTTP 302 (Portfolio Management Research titles) to the gate's HEAD probe. The
governing resolution criterion for this survey - Handle System API
`https://doi.org/api/handles/{doi}` returning `responseCode` 1, per the task
directive - was satisfied by **all 51 DOIs**, verified live on 2026-08-21 and
logged record-by-record in
`docs/literature/search_logs/regime-definitions/gap-doicheck-handle-api.json`.
Every G16 finding is therefore a false positive of the probe method, not an
identifier defect - the identical disposition, for the identical reason,
recorded in section 10.6 of both prior corpora. No finding was suppressed;
the gate output is reported verbatim in the session record.

---

# Addendum 2026-08-24 — vocabulary-expansion supplement (append-only)

Appended under
[deliverable_spec_naming-sweep_2026-08-24.md](../deliverables/deliverable_spec_naming-sweep_2026-08-24.md);
no entry above this rule is edited (pre-addendum SHA-256
`b561340781d8bc3de3ce0b7aa18b7d1f75414428fe111c4abaff574e8e2e4464`).

This survey's query vocabulary was its recall bottleneck: queries were seeded
from academic state terms, and the project has twice documented that
vocabulary mismatch defeats phrase queries. The supplement —
[lit_review_regime-naming_2026-08-24.md](lit_review_regime-naming_2026-08-24.md),
built on the empirical term registry
[vocabulary_regime-synonyms_2026-08-24.md](vocabulary_regime-synonyms_2026-08-24.md)
(137 head terms, ~540 surface forms, 8 traditions) — adds 53 records
(NA-01…NA-20, NB-01…NB-31) and a 112-row synonym graph.

**One finding of this survey is superseded:** §"Null-distribution axis" states
that no source at any tier attaches a null distribution to the assignment of
a state at time t. That universal is refuted by the supplement's
explosive/exuberant-regime records (Phillips, Wu & Yu 2011; Phillips, Shi &
Yu 2015 — real-time date-stamping with derived critical values), which this
survey's vocabulary could not reach. The bounded form survives: within the 59
definitions surveyed here, none attaches a time-t assignment null. All other
findings stand.
