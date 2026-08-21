---
title: "Regime-method gaps: null distributions for state assigners, changepoint operating characteristics, and purged cross-validation methodology"
slug: regime-method-gaps
date: 2026-08-21
objective: "For three recorded corpus gaps in the regime-classification agenda, locate what published literature exists: (A) null/reference distributions for the Kaufman Efficiency Ratio, bounded-oscillator transformations, and hidden semi-Markov regime-duration models; (B) evaluation of online changepoint detectors by detection delay versus average run length to false alarm, including financial applications; (C) formal methodological sources for purged/embargoed cross-validation above practitioner tier."
review_type: scoping
standard_declared: "PRISMA-ScR (adapted, non-clinical) - PARTIAL COMPLIANCE, targeted scoping sweep, single screener; see section 1.3 for the item-by-item conformance statement"
eligibility_inclusion:
  - "Study deriving, simulating, or characterizing the sampling distribution of a price-path efficiency/signal-to-noise statistic (Kaufman Efficiency Ratio or a mathematical analogue under any name, e.g. straightness index, tortuosity, net-to-gross displacement ratio) under a null stochastic process."
  - "Study deriving or simulating the reference distribution of a bounded technical-indicator transformation (ADX-class, RSI-class) of price under a null model, or establishing the model-based-null simulation tradition for technical-rule statistics."
  - "Peer-reviewed application of hidden semi-Markov / explicit-duration / duration-dependent Markov-switching models to financial state assignment, or methodological source for duration-distribution inference in such models."
  - "Source in the sequential-analysis / statistical-process-control tradition establishing or evaluating detection delay versus average run length to false alarm (ARL0) as detector operating characteristics, including minimax and Bayesian optimality theory, modern evaluations of BOCPD-class detectors, and applications of this evaluation frame to financial data."
  - "Formally published methodological source bearing on purged/embargoed or combinatorial purged cross-validation for dependent data, or the adjacent rigorous literature on dependent-data cross-validation and out-of-sample split selection (h-block, hv-block, time-series CV validity, forecast-evaluation sample-splitting theory)."
  - "Any language; any year; journal article, conference paper, monograph chapter, or preprint carrying a persistent identifier (DOI or arXiv)."
  - "Preprints are admissible only where no peer-reviewed record covers the same sub-question; where a published version of a preprint exists, the published version is included and the preprint is recorded as a duplicate or near-miss."
eligibility_exclusion:
  - "Records whose only contribution is the profitability of a trading rule or strategy, with no distributional, operating-characteristic, or estimator-theoretic content."
  - "Records retrieved in error, where the identifier resolved to a work outside every target (metallurgy, fire safety, medicine, and similar false-positive matches on query terms)."
  - "Trade, vendor, blog, or encyclopedia sources with no persistent identifier; these are recorded as provenance for negative findings but are never corpus entries."
  - "Software artifacts (CRAN/Zenodo packages) with no methodological derivation."
  - "Records already serving the same role in the main regime-classification corpus are re-included here only where they carry a target-specific role; the two stores are independent."
registration: not-registered
protocol_path: none
protocol_amendments: "None. Targets, inclusion and exclusion criteria were fixed by the dispatching task before the first query was executed and were not altered afterwards. Semantic Scholar rate-limiting forced retries of four planned queries; two (q-s2-03, q-s2-04) never executed successfully and are recorded as verification gaps in section 10, not as zero-hit results."
bibliography: docs/literature/references_regime-method-gaps.json
bibliography_sha256: f7cac833cfbce1e7ffc730d80038497bde1ba57f2700393e1963a382fe8f6c38
n_identified: 667
n_duplicates_removed: 22
n_screened: 645
n_excluded: 595
n_included: 50
materials_availability:
  - docs/literature/search_logs/regime-method-gaps/
  - docs/literature/references_regime-method-gaps.json
competing_interests: none
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent) executed the searches, the screening, the metadata resolution, and the drafting of this review. It is the sole screener and is declared as an automation tool under PRISMA 2020 item 8. No human second screener participated. Reproducibility log directory: logs/reproducibility/"
git_head_at_authoring: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d"
pip_freeze_sha256: "n/a - no analysis code executed; only metadata-retrieval and bibliography-store scripts"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-fable-5"
---

# Regime-method gaps: null distributions for state assigners, changepoint operating characteristics, and purged cross-validation methodology

## 1. Objective and eligibility

### 1.1 Objective

The regime-classification agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md))
carries three recorded corpus gaps left open by the 96-record main review
([lit_review_regime-classification_2026-08-21.md](lit_review_regime-classification_2026-08-21.md)).
This sweep addresses precisely those three holes and nothing else:

- **Target A - null/reference distributions for state assigners.**
  (A.1) Any published derivation, simulation study, or reference distribution of
  the Kaufman Efficiency Ratio (ER) under a null process - extending the earlier
  zero-record arXiv/Crossref search to OpenAlex, Semantic Scholar, SSRN,
  web search, and analogue literatures where the same statistic exists under
  other names ("fractal efficiency"; the straightness index of movement
  ecology). (A.2) Sampling distributions of ADX-class/RSI-class bounded
  transformations of price under a null model. (A.3) Hidden semi-Markov /
  explicit-duration models for financial regime duration, and who has addressed
  the geometric-duration misfit of standard HMMs.
- **Target B - changepoint detector operating characteristics.** The
  detection-delay-versus-ARL0 evaluation tradition (Page, Lorden, Pollak,
  Shiryaev-Roberts, Lai's minimax theory), modern evaluations of BOCPD-class
  detectors on these criteria, and applications of this frame to financial
  regime detection - testing the agenda's assertion that the framing is
  "largely absent from the trading literature".
- **Target C - purge/embargo methodology above practitioner tier.** Formally
  published sources for purged/embargoed and combinatorial purged
  cross-validation, and the adjacent rigorous dependent-data CV and
  sample-splitting literature that could ground purge/embargo choices.

The main corpus is **not** re-swept. Two records from it (Brock, Lakonishok &
LeBaron 1992; the Model Confidence Set family is untouched) reappear here only
because they carry a target-specific role; the stores are independent.

### 1.2 Grouping for synthesis

Records are grouped by target (A.1, A.2, A.3, B, C). Each numbered sub-question
receives an explicit **FOUND** (with records) or **NONE FOUND** (with the
queries that establish it) verdict in section 8.

### 1.3 Conformance statement - targeted scoping sweep, single screener

> This is a **targeted scoping sweep**, declared PRISMA-ScR partial compliance.
> It is not a full systematic review: no protocol was registered (ScR item 5,
> not met beyond the frozen task specification), no critical appraisal of
> individual sources was performed (ScR item 16, not met - an evidence tier is
> recorded per record instead, which is not equivalent), and screening was
> performed by a single automated screener with no second screener and no
> agreement measure (ScR item 9, met negatively). Search provenance (items
> 6-8), flow counts (item 14), exclusion reasons, and per-record identifiers
> are reported in full. Two screening passes by the same model would not be
> independent, so no kappa is reported; reporting one would look like evidence
> and be none.

## 2. Information sources and methods

<!-- prisma-s-1 -->
PRISMA-S 1/2/13: one row per executed query. All searches executed 2026-08-21.
`n_records` is the number of records retrieved and screened for that query, not
the platform's total-hit estimate (relevance-ranked APIs report totals in the
millions for bibliographic queries; the retrieved set is the screened set).
Rows q-s2-03 and q-s2-04 record queries that failed with HTTP 429 on every
attempt; their `n_records` is 0 and the failure is a verification gap
(section 10), not a zero-hit result.

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-01 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-02 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-03 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-04 | 20 |
| Crossref (SSRN subset) | Crossref REST API, filter prefix 10.2139 | 2026-08-21 | q-cr-05 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-06 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-07 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-08 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-09 | 25 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-10 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-11 | 25 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-12 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-13 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-14 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-15 | 15 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-16 | 25 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-17 | 20 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-cr-18 | 20 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-01 | 0 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-02 | 25 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-03 | 25 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-04 | 25 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-05 | 25 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-06 | 25 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | q-oa-07 | 25 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-01 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-02 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-03 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-04 | 2 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-05 | 1 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-06 | 0 |
| arXiv | arXiv API (export.arxiv.org) | 2026-08-21 | q-ax-07 | 0 |
| Semantic Scholar | Semantic Scholar Graph API | 2026-08-21 | q-s2-01 | 20 |
| Semantic Scholar | Semantic Scholar Graph API | 2026-08-21 | q-s2-02 | 20 |
| Semantic Scholar | Semantic Scholar Graph API | 2026-08-21 | q-s2-03 | 0 |
| Semantic Scholar | Semantic Scholar Graph API | 2026-08-21 | q-s2-04 | 0 |
| Crossref (known-item batch, Target A) | Crossref REST API (api.crossref.org) | 2026-08-21 | ki-a | 18 |
| Crossref (known-item batch 2, Target A) | Crossref REST API (api.crossref.org) | 2026-08-21 | ki-a2 | 6 |
| arXiv (known-item, id_list) | arXiv API (export.arxiv.org) | 2026-08-21 | ki-a3 | 1 |
| Crossref (known-item batch, Target B) | Crossref REST API (api.crossref.org) | 2026-08-21 | ki-b | 33 |
| OpenAlex (known-item title search) | OpenAlex REST API (api.openalex.org) | 2026-08-21 | ki-b2 | 1 |
| arXiv (known-item title/author search) | arXiv API (export.arxiv.org) | 2026-08-21 | ki-b3 | 0 |
| Crossref (known-item batch, Target C) | Crossref REST API (api.crossref.org) | 2026-08-21 | ki-c | 18 |
| Crossref (known-item batch 2, Target C) | Crossref REST API (api.crossref.org) | 2026-08-21 | ki-c2 | 6 |
| Web (general) | Anthropic WebSearch tool (Claude Code) | 2026-08-21 | q-ws-01 | 10 |
| Web (general) | Anthropic WebSearch tool (Claude Code) | 2026-08-21 | q-ws-02 | 9 |

<!-- prisma-s-2 -->
No multi-database platform search was used. Each API above indexes a single
bibliographic source; the Crossref SSRN-subset query (q-cr-05) restricts
Crossref to the SSRN DOI prefix 10.2139 and is a filter, not a platform union.

<!-- prisma-s-3 -->
No study registries were searched; the targets are statistical-methodology
literatures with no registry coverage.

<!-- prisma-s-4 -->
Two general web searches (q-ws-01, q-ws-02) were purposefully run to cover the
non-DOI-indexed practitioner space for Target A.1, because the Kaufman
Efficiency Ratio originates in trade books and vendor documentation. Their full
result lists with per-result tier assessments are in
`search_logs/regime-method-gaps/q-websearch-01.json`.

<!-- prisma-s-5 -->
Limited backward citation searching: known-item queries (ki-a, ki-a2, ki-b,
ki-c, ki-c2) resolved identifiers for works cited by records retrieved in the
topical queries (e.g. the Pollak 1987 ARL paper surfaced as a secondary hit of
the Pollak 1985 lookup and was screened in). No systematic forward citation
chasing was performed; this is a stated limitation (section 10).

<!-- prisma-s-6 -->
No contacts with authors, experts, or manufacturers were made.

<!-- prisma-s-7 -->
No other information sources were used.

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S 8: each query is reproduced exactly as executed, at execution time. For
API queries the executed artifact is the request URL (shown verbatim); the raw
response is stored under `search_logs/regime-method-gaps/` in the file named by
the query id. For known-item batches the fence lists every `query.bibliographic`
string submitted through the same URL template. For WebSearch the fence is the
query text submitted to the tool.

```text q-cr-01
https://api.crossref.org/works?query.bibliographic=Kaufman+efficiency+ratio+trading&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-02
https://api.crossref.org/works?query.bibliographic=Kaufman+adaptive+moving+average&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-03
https://api.crossref.org/works?query.bibliographic=fractal+efficiency+ratio+price+noise&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-04
https://api.crossref.org/works?query.bibliographic=straightness+index+random+walk+tortuosity+path&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-05
https://api.crossref.org/works?query.bibliographic=Kaufman+efficiency+ratio+adaptive+moving+average&filter=prefix:10.2139&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-06
https://api.crossref.org/works?query.bibliographic=relative+strength+index+statistical+properties+distribution&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-07
https://api.crossref.org/works?query.bibliographic=technical+trading+rules+bootstrap+null+model+distribution&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-08
https://api.crossref.org/works?query.bibliographic=average+directional+index+Wilder+distribution&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-09
https://api.crossref.org/works?query.bibliographic=hidden+semi-Markov+model+financial+time+series&rows=25&select=DOI,title,author,issued,container-title,type
```

```text q-cr-10
https://api.crossref.org/works?query.bibliographic=duration+dependent+Markov+switching+bull+bear+markets&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-11
https://api.crossref.org/works?query.bibliographic=average+run+length+false+alarm+detection+delay+change+point&rows=25&select=DOI,title,author,issued,container-title,type
```

```text q-cr-12
https://api.crossref.org/works?query.bibliographic=quickest+change+detection+minimax+sequential&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-13
https://api.crossref.org/works?query.bibliographic=statistical+surveillance+financial+monitoring+optimality&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-14
https://api.crossref.org/works?query.bibliographic=purged+cross-validation+embargo+financial+machine+learning&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-15
https://api.crossref.org/works?query.bibliographic=hv-block+cross-validation+dependent+data&rows=15&select=DOI,title,author,issued,container-title,type
```

```text q-cr-16
https://api.crossref.org/works?query.bibliographic=cross-validation+time+series+autoregressive+validity+evaluation&rows=25&select=DOI,title,author,issued,container-title,type
```

```text q-cr-17
https://api.crossref.org/works?query.bibliographic=out-of-sample+forecast+evaluation+sample+split+choice&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-cr-18
https://api.crossref.org/works?query.bibliographic=sequential+monitoring+volatility+CUSUM+GARCH+financial+time+series&rows=20&select=DOI,title,author,issued,container-title,type
```

```text q-oa-01
https://api.openalex.org/works?search=%22Kaufman%20efficiency%20ratio%22&per-page=25
```

```text q-oa-02
https://api.openalex.org/works?search=%22Kaufman%20adaptive%20moving%20average%22&per-page=25
```

```text q-oa-03
https://api.openalex.org/works?search=%22relative%20strength%20index%22%20%22sampling%20distribution%22&per-page=25
```

```text q-oa-04
https://api.openalex.org/works?search=%22hidden%20semi-Markov%22%20financial%20regime&per-page=25
```

```text q-oa-05
https://api.openalex.org/works?search=%22run%20length%22%20%22detection%20delay%22%20changepoint%20financial&per-page=25
```

```text q-oa-06
https://api.openalex.org/works?search=%22purged%20cross-validation%22&per-page=25
```

```text q-oa-07
https://api.openalex.org/works?search=%22relative%20strength%20index%22%20%22random%20walk%22&per-page=25
```

```text q-ax-01
https://export.arxiv.org/api/query?search_query=all:%22Kaufman+adaptive+moving+average%22+OR+all:%22Kaufman+efficiency+ratio%22&max_results=20
```

```text q-ax-02
https://export.arxiv.org/api/query?search_query=abs:%22relative+strength+index%22+AND+abs:distribution&max_results=20
```

```text q-ax-03
https://export.arxiv.org/api/query?search_query=abs:%22hidden+semi-Markov%22+AND+cat:q-fin*&max_results=25
```

```text q-ax-04
https://export.arxiv.org/api/query?search_query=abs:%22Bayesian+online+changepoint+detection%22+AND+abs:%22false+alarm%22&max_results=25
```

```text q-ax-05
https://export.arxiv.org/api/query?search_query=abs:%22purged+cross-validation%22+OR+abs:%22combinatorial+purged%22&max_results=25
```

```text q-ax-06
https://export.arxiv.org/api/query?search_query=ti:%22Restarted+Bayesian+Online+Change-point+Detector%22&max_results=5
```

```text q-ax-07
https://export.arxiv.org/api/query?search_query=abs:%22change+point%22+AND+abs:%22average+run+length%22+AND+cat:q-fin*&max_results=25
```

```text q-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=Kaufman%20efficiency%20ratio%20null%20distribution&limit=20&fields=title,externalIds,year,venue,publicationTypes
```

```text q-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=Kaufman%20adaptive%20moving%20average%20efficiency%20ratio&limit=20&fields=title,externalIds,year,venue,publicationTypes
```

```text q-s2-03
https://api.semanticscholar.org/graph/v1/paper/search?query=Bayesian%20online%20changepoint%20detection%20average%20run%20length%20false%20alarm&limit=20&fields=title,externalIds,year,venue,publicationTypes
```

```text q-s2-04
https://api.semanticscholar.org/graph/v1/paper/search?query=combinatorial%20purged%20cross-validation&limit=20&fields=title,externalIds,year,venue,publicationTypes
```

```text ki-a
URL template: https://api.crossref.org/works?query.bibliographic={query}&rows=3&select=DOI,title,author,issued,container-title,type
1. How to reliably estimate the tortuosity of an animal's path straightness sinuosity fractal dimension Benhamou
2. Random walk models in biology Codling Plank Benhamou
3. Data-snooping technical trading rule performance bootstrap Sullivan Timmermann White
4. Estimating hidden semi-Markov chains from discrete sequences Guedon
5. Hidden semi-Markov models Yu survey artificial intelligence
6. Hidden Markov models with arbitrary state dwell-time distributions Langrock Zucchini
7. Duration-dependent transitions in a Markov model of US GNP growth Durland McCurdy
8. Identifying bull and bear markets in stock returns Maheu McCurdy
(queries 6 and 8 returned HTTP 429 in this batch and were re-executed as ki-a2)
```

```text ki-a2
URL template: https://api.crossref.org/works?query.bibliographic={query}&rows=3&select=DOI,title,author,issued,container-title,type
1. Hidden Markov models with arbitrary state dwell-time distributions Langrock Zucchini computational statistics
2. Identifying bull and bear markets in stock returns Maheu McCurdy journal of business economic statistics
```

```text ki-a3
https://export.arxiv.org/api/query?id_list=1710.02175
```

```text ki-b
URL template: https://api.crossref.org/works?query.bibliographic={query}&rows=3&select=DOI,title,author,issued,container-title,type
1. Continuous inspection schemes Page Biometrika 1954
2. Procedures for reacting to a change in distribution Lorden
3. Optimal detection of a change in distribution Pollak
4. Optimal stopping times for detecting changes in distributions Moustakides
5. On optimum methods in quickest detection problems Shiryaev
6. Information bounds and quick detection of parameter changes in stochastic systems Lai
7. A comparison of some control chart procedures Roberts Technometrics
8. State-of-the-art in sequential change-point detection Polunchenko Tartakovsky
9. A numerical approach to performance analysis of quickest change-point detection procedures Moustakides Polunchenko Tartakovsky
10. Restarted Bayesian online change-point detector achieves optimal detection delay Alami Maillard Feraud
11. An evaluation of change point detection algorithms van den Burg Williams
```

```text ki-b2
https://api.openalex.org/works?filter=title.search:restarted%20bayesian%20online%20change-point%20detector&per-page=10
```

```text ki-b3
https://export.arxiv.org/api/query?search_query=ti:%22Optimal+Detection+Delay%22+AND+au:Alami&max_results=10
```

```text ki-c
URL template: https://api.crossref.org/works?query.bibliographic={query}&rows=3&select=DOI,title,author,issued,container-title,type
1. A cross-validatory method for dependent data Burman Chow Nolan
2. Evaluating time series forecasting models empirical study performance estimation methods Cerqueira Torgo
3. Asymptotic inference about predictive ability West Econometrica
4. Advances in financial machine learning Lopez de Prado notes on backtesting
5. The deflated Sharpe ratio correcting for selection bias backtest overfitting Bailey Lopez de Prado
6. Automated kernel smoothing of dependent data by using time series cross-validation Hart
```

```text ki-c2
URL template: https://api.crossref.org/works?query.bibliographic={query}&rows=3&select=DOI,title,author,issued,container-title,type
1. The probability of backtest overfitting Bailey Borwein Lopez de Prado Zhu journal of computational finance
2. Time series cross validation theoretical properties and empirical performance
```

```text q-ws-01
"Kaufman efficiency ratio" distribution random walk null simulation
```

```text q-ws-02
"efficiency ratio" OR "fractal efficiency" indicator sampling distribution derivation academic paper Kaufman KAMA
```

<!-- prisma-s-9 -->
No limits were used on year, language, or document type at query time. Result
counts per query were capped at the `rows`/`limit`/`max_results` values shown
in each URL (15-25), a retrieval-depth cap on relevance-ranked APIs, not an
eligibility limit; the cap is why `n_records` reports retrieved-and-screened
counts rather than platform totals.

<!-- prisma-s-10 -->
No published search filters were used.

<!-- prisma-s-11 -->
The overall strategy (Crossref topical + known-item batches + arXiv + OpenAlex
+ targeted web search, raw responses logged per query) is reused from the main
regime-classification review
([lit_review_regime-classification_2026-08-21.md](lit_review_regime-classification_2026-08-21.md)),
this project, 2026-08-21. No query string was reused.

<!-- prisma-s-12 -->
No updates are scheduled. The sweep is a point-in-time gap assessment; the
agenda will trigger a re-run if a target is re-opened.

<!-- prisma-s-13 -->
All strategies were last executed 2026-08-21, in agreement with the
`date_searched` column in section 2.

## 4. Peer review of the strategy

<!-- prisma-s-14 -->
Not peer reviewed. No PRESS review by an information specialist and no
adversarial re-derivation by a second agent took place. Single-agent sweep.

## 5. Managing records

<!-- prisma-s-15 -->
667 records were identified in total, distributed per query as in the section 2
table (`n_records` column). No source outside that table contributed records.
The two failed Semantic Scholar queries contributed zero records and are
reported as verification gaps, not as searches with zero hits.

<!-- prisma-s-16 -->
Deduplication: exact DOI match (case-insensitive) across all sources; records
without a DOI matched on normalized title (lowercased, non-word characters
collapsed); arXiv and web records without DOIs matched on URL. Software: Python
3.11 standard-library script (json/re), run inline on 2026-08-21; the script
text is preserved in the session audit trail. 22 duplicates were removed
(667 identified, 645 screened).

<!-- prisma-2020-8 -->
PRISMA 2020 item 8, selection process.

- **screeners_n**: 1
- **independent**: no - single screener
- **automation_tools**: Claude Fable 5 (model id claude-fable-5), Claude Code /
  Claude Agent SDK research-librarian agent; it executed every query, screened
  every record on title/venue/abstract against the frozen criteria, and
  resolved all metadata. No human screener participated.

## 6. Excluded records

<!-- prisma-2020-16b -->
Records that appeared to meet the inclusion criteria but were excluded, with
reasons. The remaining bulk of the 595 exclusions were topical false positives
on query vocabulary (metallurgy, fire-safety, soil-mechanics, medical, and
IoT/SPC-hardware records; vendor book chapters; profitability-only trading
studies) excluded at the title/venue stage.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E1 | Alami, Maillard & Feraud (2020) Restarted Bayesian Online Change-point Detector achieves Optimal Detection Delay. ICML/PMLR. OpenAlex W3035594853 | full-record | Directly on-target for B (BOCPD-class detector with delay/false-alarm guarantees) but carries no persistent identifier admissible to the store: no DOI, no arXiv record locatable (queries ki-b, ki-b2, ki-b3). Recorded as a verification gap in section 10 and discussed in section 8.4. |
| E2 | Anonymous authorship per SSRN record (2025) Analysis of an Algo Trading Strategy Based on the Kaufman Adaptive Moving Average, doi:10.2139/ssrn.5694583 | title-abstract | Profitability-only KAMA strategy study; no distributional content; preprint tier. |
| E3 | Zakamulin (2020, with coauthorship as listed on SSRN) Not All Bull and Bear Markets Are Alike, doi:10.2139/ssrn.3678004 | full-record | Preprint version of an included published record (doi:10.1057/s41283-022-00112-y); published version included per eligibility rule. |
| E4 | Bulla (2006) Application of Hidden Markov and Hidden Semi-Markov Models to Financial Time Series, doi:10.53846/goediss-3687 | full-record | Dissertation superseded by the included peer-reviewed article (doi:10.1016/j.csda.2006.07.021) covering the same material. |
| E5 | (2024) Simplicity versus Complexity: A Comparative Analysis of HMM and HSMM for Regime-Based Asset Allocation, doi:10.2139/ssrn.4796238 | title-abstract | Preprint with no located published version; peer-reviewed HMM-vs-HSMM comparisons already cover the sub-question (eligibility rule on preprints). |
| E6 | Frisen ed. (2007) Statistical Models in Finance, ch. 2 of Financial Surveillance, doi:10.1002/9780470987179.ch2 | full-record | Contextual model-catalogue chapter; no operating-characteristic content; ch. 3 of the same volume included instead. |
| E7 | purgedcv: scikit-learn-compatible purged and combinatorial cross-validation (2026), doi:10.5281/zenodo.20312979 (and 12 sibling version DOIs) | full-record | Software artifact, no methodological derivation; tier-5 for the purposes of Target C. Noted in section 8.5 as evidence the practitioner method is being packaged, not formalized. |
| E8 | (2020) Evaluation of Change Point Detection Algorithms for Application in Big Data Mini-terms, doi:10.5220/0009594001170124 | title-abstract | Manufacturing-domain CPD evaluation; no delay-vs-ARL0 operating-characteristic content evident at screening stage. |
| E9 | (2024) Bayesian Autoregressive Online Change-Point Detection with Time-Varying Parameters, doi:10.2139/ssrn.4902550 | title-abstract | Preprint; no published version located; delay/ARL0 content not established from the available record. |
| E10 | (2022) Time Series Cross Validation: Theoretical Properties and Empirical Performance, doi:10.2139/ssrn.3996529 | full-record | Preprint version of the included published record (doi:10.1016/j.econlet.2023.111369). |
| E11 | (2016) Optimizing the Performance of the Fractal Adaptive Moving Average Strategy: The Case of EUR/USD, doi:10.5539/IJEF.V8N2P171 | title-abstract | FRAMA (KAMA-family) profitability optimization; no reference-distribution content. |
| E12 | (2022) Robust Testing for Bollinger Band, Moving Average and Relative Strength Index, doi:10.58886/jfi.v20i1.3218 | title-abstract | Rule-profitability robustness testing; no indication of a derived indicator sampling distribution at screening stage; full text not assessed (section 10). |
| E13 | (2013) Representation of trading signals: SSRN duplicate cluster of q-cr-05 (moving-average trading-rule studies, 18 records) | title-abstract | Profitability-only moving-average studies retrieved by the SSRN-prefix query; none carries distributional content for A.1. Representative DOIs in the q-cr-05 log. |

## 7. Included corpus

<!-- included-corpus -->
Every included record carries a persistent identifier (FAIR F1). The
machine-readable form is the CSL-JSON store; this table is the human-readable
index. Tier abbreviations: PR = peer-reviewed; PR-mono = peer-reviewed
monograph/survey series; BC = edited-book chapter; PP = preprint.

| id | citation | persistent id | role in the argument |
|---|---|---|---|
| benhamou2004jjtbi2004030 | Benhamou (2004) How to reliably estimate the tortuosity of an animal's path. J Theor Biol. | 10.1016/j.jtbi.2004.03.016 | A.1 analogue [PR]: the straightness index (net displacement / path length) is the Kaufman ER computed on a spatial path; derives its expectation behaviour under random-walk nulls and shows it is an unreliable tortuosity estimator whose value depends on path length. |
| codling2008rsif20080014 | Codling, Plank & Benhamou (2008) Random walk models in biology. J R Soc Interface. | 10.1098/rsif.2008.0014 | A.1 analogue [PR]: survey of random-walk theory giving the distributional machinery (net-displacement moments under CRW/BRW) from which an ER-class null can be derived. |
| anon2013cmse130408 | (2013) Representation of trading signals based on Kaufman adaptive moving average as a system of linear inequalities. Bull. South Ural State Univ. | 10.14529/cmse130408 | A.1 evidence-of-absence [PR]: the only peer-reviewed KAMA-specific methodological record located; formalizes KAMA signals, states no null distribution. |
| brock1992j15406261199 | Brock, Lakonishok & LeBaron (1992) Simple Technical Trading Rules and the Stochastic Properties of Stock Returns. J Finance. | 10.1111/j.1540-6261.1992.tb04681.x | A.2 [PR]: canonical model-based-null bootstrap design - simulate RW/AR(1)/GARCH-M/EGARCH nulls and read off the indicator statistic's reference distribution; the located substitute for closed-form oscillator distributions. |
| sullivan1999002210820016 | Sullivan, Timmermann & White (1999) Data-Snooping, Technical Trading Rule Performance, and the Bootstrap. J Finance. | 10.1111/0022-1082.00163 | A.2 [PR]: extends the BLL null-model program with data-snooping-adjusted p-values over a rule universe; reference-distribution inference for rule families rather than single indicators. |
| deford2017e19110615 | DeFord & Moore (2017) Random Walk Null Models for Time Series Data. Entropy. | 10.3390/e19110615 | A.2 [PR]: the closest located example of the exact program Target A asks for - derives the distribution of a bounded ordinal-pattern statistic of a price-like series analytically under explicit random-walk nulls, with a validation statistic. |
| gurrib2018bbs133201806 | Gurrib (2018) Performance of the Average Directional Index as a market timing tool. Banks and Bank Systems. | 10.21511/bbs.13(3).2018.06 | A.2 evidence-of-absence [PR]: peer-reviewed ADX application; uses the conventional threshold, states no reference distribution - the ADX-null gap persists in the applied literature. |
| bulla2006jcsda2006070 | Bulla & Bulla (2006) Stylized facts of financial time series and hidden semi-Markov models. Comput Stat Data Anal. | 10.1016/j.csda.2006.07.021 | A.3 [PR]: the direct answer to "who has addressed the geometric-duration misfit" - fits HSMMs with non-geometric dwell times to daily returns and shows they reproduce stylized facts standard HMMs miss. |
| gudon2003106186003203 | Guedon (2003) Estimating Hidden Semi-Markov Chains From Discrete Sequences. J Comput Graph Stat. | 10.1198/1061860032030 | A.3 [PR]: estimation machinery for explicit-duration chains, including duration-distribution inference. |
| yu2010jartint20091 | Yu (2010) Hidden semi-Markov models. Artificial Intelligence. | 10.1016/j.artint.2009.11.011 | A.3 [PR]: the standard survey of HSMM inference, complexity, and duration-model families. |
| langrock2011jcsda2010060 | Langrock & Zucchini (2011) Hidden Markov models with arbitrary state dwell-time distributions. Comput Stat Data Anal. | 10.1016/j.csda.2010.06.015 | A.3 [PR]: embeds arbitrary dwell-time distributions in an expanded-state HMM, making HSMM-class duration inference computable with standard HMM tools. |
| durland1994073500151994 | Durland & McCurdy (1994) Duration-Dependent Transitions in a Markov Model of U.S. GNP Growth. J Bus Econ Stat. | 10.1080/07350015.1994.10524543 | A.3 [PR]: earliest located econometric treatment of duration dependence in regime transitions - the semi-Markov idea inside a Markov-switching framework. |
| maheu2000073500152000 | Maheu & McCurdy (2000) Identifying Bull and Bear Markets in Stock Returns. J Bus Econ Stat. | 10.1080/07350015.2000.10524851 | A.3 [PR]: duration-dependent Markov switching applied to financial state assignment; transition probabilities are functions of state age. |
| chiappa20142200000054 | Chiappa (2014) Explicit-Duration Markov Switching Models. Found Trends Mach Learn. | 10.1561/2200000054 | A.3 [PR-mono]: unifying treatment of explicit-duration switching models and their inference algorithms. |
| zakamulin2022s41283022001 | Zakamulin (2022) Not all bull and bear markets are alike: five-state hidden semi-Markov model. Risk Management. | 10.1057/s41283-022-00112-y | A.3 [PR]: modern financial HSMM state assignment with explicit duration distributions per state. |
| wang2021jfrl20211019 | Wang, Gupta & Zhang (2021) Bear, Bull, Sidewalk, and Crash: HSMM on over a century of US stock data. Finance Research Letters. | 10.1016/j.frl.2021.101998 | A.3 [PR]: four-state HSMM regime assignment on long-horizon data; duration-distribution estimates by state. |
| qin2024s10479024059 | Qin et al. (2024) On robust estimation of hidden semi-Markov regime-switching models. Ann Oper Res. | 10.1007/s10479-024-05989-4 | A.3 [PR]: robust estimation for financial HSMM regime models; addresses outlier sensitivity of duration inference. |
| suda2019info10100322 | Suda & Spiteri (2019) Analysis and Comparison of Bitcoin and S&P 500 Market Features Using HMMs and HSMMs. Information. | 10.3390/info10100322 | A.3 [PR]: head-to-head HMM vs HSMM comparison on financial series, including duration-fit differences. |
| page19544112100 | Page (1954) Continuous Inspection Schemes. Biometrika. | 10.1093/biomet/41.1-2.100 | B [PR]: origin of CUSUM and of run-length-based evaluation. |
| lorden19711177693055 | Lorden (1971) Procedures for Reacting to a Change in Distribution. Ann Math Stat. | 10.1214/aoms/1177693055 | B [PR]: minimax worst-case delay criterion subject to an ARL0 constraint; first asymptotic optimality of CUSUM. |
| roberts1966004017061966 | Roberts (1966) A Comparison of Some Control Chart Procedures. Technometrics. | 10.1080/00401706.1966.10490374 | B [PR]: Shiryaev-Roberts procedure in SPC form and the first systematic delay-vs-ARL0 comparison across chart procedures. |
| shiryaev19631108002 | Shiryaev (1963) On Optimum Methods in Quickest Detection Problems. Theory Probab Appl. | 10.1137/1108002 | B [PR]: Bayesian quickest-detection optimality; the Shiryaev procedure. |
| pollak19851176346587 | Pollak (1985) Optimal Detection of a Change in Distribution. Ann Stat. | 10.1214/aos/1176346587 | B [PR]: Pollak's supremum-conditional-delay criterion and near-optimality of Shiryaev-Roberts. |
| pollak19871176350373 | Pollak (1987) Average Run Lengths of an Optimal Method of Detecting a Change in Distribution. Ann Stat. | 10.1214/aos/1176350373 | B [PR]: explicit ARL analysis of the optimal procedure - the delay-vs-ARL0 operating characteristic itself. |
| moustakides19861176350164 | Moustakides (1986) Optimal Stopping Times for Detecting Changes in Distributions. Ann Stat. | 10.1214/aos/1176350164 | B [PR]: exact minimax optimality of CUSUM under Lorden's criterion. |
| tzeleunglai199818737522 | Lai (1998) Information bounds and quick detection of parameter changes in stochastic systems. IEEE Trans Inf Theory. | 10.1109/18.737522 | B [PR]: information-theoretic lower bounds on detection delay at fixed false-alarm rate; the minimax theory named in the agenda. |
| polunchenko2011s11009011925 | Polunchenko & Tartakovsky (2012) State-of-the-Art in Sequential Change-Point Detection. Methodol Comput Appl Probab. | 10.1007/s11009-011-9256-5 | B [PR]: survey organizing the field around the delay-vs-ARL0 tradeoff across minimax, Bayesian, and multi-cyclic formulations. |
| moustakides2011ss2011026a | Moustakides, Polunchenko & Tartakovsky (2011) A numerical approach to performance analysis of quickest change-point detection procedures. Statistica Sinica. | 10.5705/ss.2011.026a | B [PR]: numerical machinery for computing delay and ARL0 operating characteristics of CUSUM/SR-class detectors - the practical template for a design-resolution study. |
| mei2008074749408024 | Mei (2008) Is Average Run Length to False Alarm Always an Informative Criterion? Sequential Analysis. | 10.1080/07474940802445790 | B [PR]: the internal critique - ARL0 can be uninformative for some procedures; a false-alarm criterion must be chosen, not assumed. Discussion pieces in the same issue. |
| kuhn2018s11009018963 | Kuhn, Mandjes & Taimre (2018) Practical Aspects of False Alarm Control for Change Point Detection: Beyond Average Run Length. Methodol Comput Appl Probab. | 10.1007/s11009-018-9636-1 | B [PR]: modern false-alarm-control alternatives to raw ARL0 and their practical calibration. |
| johnson2017rsta20160298 | Johnson, Moriarty & Peskir (2017) Detecting changes in real-time data: a user's guide to optimal detection. Phil Trans R Soc A. | 10.1098/rsta.2016.0298 | B [PR]: applied bridge from quickest-detection optimality theory to real-time practice; states criteria a practitioner must fix (incl. false-alarm frequency) before choosing a detector. |
| vandenburg2020evalcpd | van den Burg & Williams (2020) An Evaluation of Change Point Detection Algorithms. arXiv. | 10.48550/arXiv.2003.06222 | B [PP]: the standard modern CPD benchmark - notably evaluates BOCPD-class detectors by F1/cover on annotated series, not by delay-vs-ARL0; direct evidence for the agenda's absence claim in the ML evaluation culture. |
| frisn2003j17515823200 | Frisen (2003) Statistical Surveillance. Optimality and Methods. Int Stat Rev. | 10.1111/j.1751-5823.2003.tb00205.x | B [PR]: systematizes surveillance evaluation metrics (ARL, expected delay, predictive value) and their relations - the evaluation-frame taxonomy for target B. |
| bock2007978047098717 | Bock, Andersson & Frisen (2007) The Relation between Statistical Surveillance and Technical Analysis in Finance. In: Financial Surveillance (Wiley). | 10.1002/9780470987179.ch3 | B [BC]: explicitly maps trading indicators onto surveillance stopping rules and evaluates them by delay/false-alarm criteria - the located bridge between target B's framing and the trading literature. |
| yeganeh2023journalpone0 | Yeganeh & Shongwe (2023) A novel application of statistical process control charts in financial market surveillance with an ARL-based evaluation. PLOS ONE. | 10.1371/journal.pone.0288627 | B [PR]: recent direct application of ARL-evaluated control charts to financial market data. |
| horvth2025jtsa12824 | Horvath, Trapani & Wang (2025) Sequential Monitoring for Changes in GARCH(1,1) Models Without Assuming Stationarity. J Time Ser Anal. | 10.1111/jtsa.12824 | B [PR]: financial sequential monitoring with controlled false-alarm behaviour under volatility dynamics - the econometric wing of delay-vs-false-alarm evaluation. |
| astill2021nbab009 | Astill et al. (2021) CUSUM-Based Monitoring for Explosive Episodes in Financial Data in the Presence of Time-Varying Volatility. J Financ Econom. | 10.1093/jjfinec/nbab009 | B [PR]: CUSUM monitoring of financial episodes with false-alarm control under heteroskedasticity; nearest financial cousin of the ARL0 tradition. |
| burman1994812351 | Burman, Chow & Nolan (1994) A cross-validatory method for dependent data. Biometrika. | 10.1093/biomet/81.2.351 | C [PR]: h-block CV - the earliest formal purge analogue: delete a block of h observations around the test point to break dependence. |
| hart1994j25176161199 | Hart (1994) Automated Kernel Smoothing of Dependent Data by Using Time Series Cross-Validation. JRSS-B. | 10.1111/j.2517-6161.1994.tb01998.x | C [PR]: time-series cross-validation with dependence-aware risk estimation; formal antecedent of leave-future-out schemes. |
| racine2000s03044076000 | Racine (2000) Consistent cross-validatory model-selection for dependent data: hv-block cross-validation. J Econometrics. | 10.1016/s0304-4076(00)00030-0 | C [PR]: hv-block CV - h-block plus a validation block; proves consistency for dependent data and gives the formal criterion an embargo length could be selected against. |
| bergmeir2012jins20111202 | Bergmeir & Benitez (2012) On the use of cross-validation for time series predictor evaluation. Information Sciences. | 10.1016/j.ins.2011.12.028 | C [PR]: empirical comparison of blocked/modified CV schemes for time series. |
| bergmeir2018jcsda2017110 | Bergmeir, Hyndman & Koo (2018) A note on the validity of cross-validation for evaluating autoregressive time series prediction. Comput Stat Data Anal. | 10.1016/j.csda.2017.11.003 | C [PR]: shows standard K-fold CV can be valid for purely autoregressive fits with uncorrelated errors - the boundary of when purging is even necessary. |
| cerqueira2020s10994020059 | Cerqueira, Torgo & Mozetic (2020) Evaluating time series forecasting models: an empirical study on performance estimation methods. Machine Learning. | 10.1007/s10994-020-05910-7 | C [PR]: large-scale empirical comparison of performance-estimation schemes (incl. blocked CV and out-of-sample variants) for dependent data. |
| deng2023jeconlet2023 | Deng (2023) Time series cross validation: A theoretical result and finite sample performance. Economics Letters. | 10.1016/j.econlet.2023.111369 | C [PR]: recent theoretical result for time-series CV; the published version of the sole located theory paper on leave-future-out CV properties. |
| bailey2016jcf2016322 | Bailey, Borwein, Lopez de Prado & Zhu (2016) The probability of backtest overfitting. J Comput Finance. | 10.21314/jcf.2016.322 | C [PR]: combinatorially symmetric cross-validation (CSCV) with formal PBO estimator - the peer-reviewed formal core nearest to combinatorial purged CV; note it analyzes overfitting probability, not CPCV variance. |
| west19962171956 | West (1996) Asymptotic Inference about Predictive Ability. Econometrica. | 10.2307/2171956 | C [PR]: asymptotic theory of out-of-sample predictive inference under estimated parameters; the sample-splitting inference foundation. |
| rossi2012073500152012 | Rossi & Inoue (2012) Out-of-Sample Forecast Tests Robust to the Choice of Window Size. J Bus Econ Stat. | 10.1080/07350015.2012.693850 | C [PR]: removes the researcher degree of freedom in split/window choice by robustifying over it - the formal treatment of a tunable the practitioner catalogue leaves free. |
| hansen2015ecta10581 | Hansen & Timmermann (2015) Equivalence Between Out-of-Sample Forecast Comparisons and Wald Statistics. Econometrica. | 10.3982/ecta10581 | C [PR]: shows split-sample forecast comparisons are Wald statistics; sample-split choice affects power in a characterizable way. |
| kolev2017jjbankfin201 | Kolev & Karapandza (2017) Out-of-sample equity premium predictability and sample split-invariant inference. J Banking & Finance. | 10.1016/j.jbankfin.2016.07.017 | C [PR]: demonstrates result sensitivity to sample-split choice in finance and constructs split-invariant inference. |
| stank2023for3013 | Stanek (2023) Optimal out-of-sample forecast evaluation under stationarity. J Forecasting. | 10.1002/for.3013 | C [PR]: optimality theory for out-of-sample evaluation design under stationarity, with an R implementation (ACV). |

## 8. Synthesis

Evidence tiers follow the project hierarchy; every record's tier is in the
section 7 table. Verdicts are stated per numbered sub-question of the
dispatching task.

### 8.1 Target A.1 - Kaufman Efficiency Ratio null distribution

**Verdict: NONE FOUND** for any published derivation, simulation study, or
reference distribution of the Kaufman ER under any null, in any of Crossref,
OpenAlex, Semantic Scholar, arXiv, the SSRN subset, or the open web.
Establishing queries: q-cr-01, q-cr-02, q-cr-03, q-cr-05, q-oa-01 (**zero
records** for the exact phrase "Kaufman efficiency ratio" in OpenAlex full-text
search - a second-platform replication of the agenda's arXiv zero), q-oa-02,
q-ax-01, q-s2-01, q-s2-02, q-ws-01, q-ws-02. Everything ER-specific above
tier 5 either applies KAMA without a null (10.14529/cmse130408, included as
evidence of absence) or is a profitability study (E2, E11). All 19 web-search
results bearing on ER itself were tier-5 vendor/blog material (logged with
per-result tier assessments in `q-websearch-01.json`).

**Analogue literature: FOUND, and directly usable.** The ER statistic - net
displacement over path length in a window - is, term for term, the
**straightness index** of movement ecology. Benhamou (2004)
[10.1016/j.jtbi.2004.03.016] analyzes exactly this ratio for random-walk paths:
its expectation decays with path length under a correlated random walk (for an
uncorrelated walk the 2-D mean net displacement grows as the square root of
step count while path length grows linearly), so the "efficiency" of a null
path is a *function of the window length n*, not a constant - any fixed ER
threshold therefore encodes an implicit window-dependent false-positive rate.
Codling, Plank & Benhamou (2008) [10.1098/rsif.2008.0014] supply the
net-displacement moment machinery from which an ER null for a specified
increment process can be derived or simulated. The agenda's conclusion
("deriving or simulating it is unavoidable") stands, and the derivation now has
a peer-reviewed starting point: treat ER as a straightness index of a 1-D walk
with the deseasonalized increment distribution, and obtain its null law by the
methods of these two records.

### 8.2 Target A.2 - bounded-oscillator reference distributions

**Verdict: NONE FOUND** for a closed-form or simulated *sampling distribution
of ADX-class or RSI-class bounded transformations* published as such.
Establishing queries: q-cr-06, q-cr-08, q-oa-03, q-oa-07, q-ax-02 (zero
records). The RSI/ADX applied literature retrieved by these queries applies
conventional thresholds (30/70; ADX>25) with no reference distribution;
Gurrib (2018) [10.21511/bbs.13(3).2018.06] is included as the peer-reviewed
witness of that practice.

**The located tradition is model-based null simulation, not derivation.**
Brock, Lakonishok & LeBaron (1992) [10.1111/j.1540-6261.1992.tb04681.x]
established the design: fit null models (random walk, AR(1), GARCH-M, EGARCH),
simulate, and read the indicator statistic's reference distribution off the
simulations; Sullivan, Timmermann & White (1999) [10.1111/0022-1082.00163]
extended it with data-snooping-adjusted inference over a rule universe. Both
target trading-rule *returns* rather than the indicator's own sampling
distribution, but the machinery transfers unchanged to ADX/RSI values
themselves. One record executes precisely the "derive the bounded statistic's
distribution under a random-walk null" program, for a different bounded
statistic: DeFord & Moore (2017) [10.3390/e19110615] derive ordinal-pattern
distributions of random-walk series analytically and use them as null models
for time-series statistics. It is the existence proof that the program Target
A.2 asks about is feasible and publishable - and that nobody has done it for
ADX or RSI.

### 8.3 Target A.3 - hidden semi-Markov models for financial regime duration

**Verdict: FOUND - a substantial peer-reviewed literature (11 records).** The
geometric-duration misfit of standard HMMs the agenda flags has been addressed
along two lines. **Econometric duration dependence:** Durland & McCurdy (1994)
[10.1080/07350015.1994.10524543] made transition probabilities functions of
state age; Maheu & McCurdy (2000) [10.1080/07350015.2000.10524851] applied
duration-dependent switching to bull/bear identification. **Explicit-duration
HSMMs:** Bulla & Bulla (2006) [10.1016/j.csda.2006.07.021] is the direct
answer - HSMMs with negative-binomial dwell times reproduce the slow decay of
squared-return autocorrelation that geometric-duration HMMs cannot. Inference
machinery: Guedon (2003) [10.1198/1061860032030], Yu (2010)
[10.1016/j.artint.2009.11.011], Langrock & Zucchini (2011)
[10.1016/j.csda.2010.06.015] (arbitrary dwell-time distributions inside an
expanded-state HMM - the practical route for this project), and Chiappa (2014)
[10.1561/2200000054]. Modern financial state assignment with explicit
durations: Zakamulin (2022) [10.1057/s41283-022-00112-y], Wang et
al. (2021) [10.1016/j.frl.2021.101998], Qin et al. (2024)
[10.1007/s10479-024-05989-4], Suda & Spiteri (2019) [10.3390/info10100322].
Consequence for the agenda: branch 2's remaining-duration endpoint has an
established model class with peer-reviewed duration-distribution inference; the
HSMM row of the assigner sweep can cite primary methodology rather than
folklore.

### 8.4 Target B - detection delay versus ARL0

**Verdict on the tradition: FOUND, deep and canonical (11 records).** Page
(1954), Shiryaev (1963), Roberts (1966), Lorden (1971), Pollak (1985, 1987),
Moustakides (1986), Lai (1998), surveyed in Polunchenko & Tartakovsky (2012),
with computable operating characteristics in Moustakides, Polunchenko &
Tartakovsky (2011) [10.5705/ss.2011.026a] - the last is the practical template
for the agenda's design-resolution study (smallest recoverable shift at stated
ARL0). Two records qualify the criterion itself: Mei (2008)
[10.1080/07474940802445790] shows ARL0 can be uninformative for some detector
classes, and Kuhn, Mandjes & Taimre (2018) [10.1007/s11009-018-9636-1] give
modern alternatives; the agenda's `TO COMPUTE` ARL0 parameter should be chosen
in awareness of both.

**Verdict on BOCPD-class evaluation by these criteria: PARTIALLY FOUND.** The
standard modern benchmark - van den Burg & Williams (2020)
[10.48550/arXiv.2003.06222, preprint] - evaluates BOCPD-class detectors by
F1/covering against annotated changepoints, *not* by delay-vs-ARL0; the ML
evaluation culture and the sequential-analysis culture have not merged. The one
located work giving a BOCPD-class detector delay/false-alarm guarantees -
Alami, Maillard & Feraud (2020), Restarted BOCPD - could not be included: no
DOI and no arXiv record exists (queries ki-b, ki-b2, ki-b3; OpenAlex
W3035594853). This is recorded as near-miss E1 and verification gap V3.

**Verdict on financial application: FOUND, but in the statistics literature,
not the trading literature - the agenda's assertion is sustained in refined
form.** A "financial surveillance" school evaluates financial monitoring by
surveillance operating characteristics: Frisen (2003)
[10.1111/j.1751-5823.2003.tb00205.x] taxonomizes the criteria; Bock, Andersson
& Frisen (2007) [10.1002/9780470987179.ch3] explicitly recast technical-analysis
indicators as surveillance stopping rules and evaluate them by delay and
false-alarm properties - the single located record that does to trading
indicators what Target B asks for; Yeganeh & Shongwe (2023)
[10.1371/journal.pone.0288627] apply ARL-evaluated control charts to market
data; Horvath et al. (2025) [10.1111/jtsa.12824] and Astill et al. (2021)
[10.1093/jjfinec/nbab009] carry the false-alarm-controlled monitoring program
into financial econometrics. Zero records were found applying delay-vs-ARL0
inside the trading/technical-analysis literature proper (q-ax-07: zero records
for the ARL vocabulary within q-fin), so the corrected claim is: the framing
exists, imported from statistical process control, and the trading literature
has not adopted it.

### 8.5 Target C - purged/embargoed cross-validation above practitioner tier

**Verdict on purge/embargo-specific formal analysis: NONE FOUND.** No
peer-reviewed record analyzing combinatorial purged CV's variance properties,
and no formal analysis of purge or embargo length selection, exists in any
searched source. Establishing queries: q-cr-14, q-oa-06, q-ax-05 (one record,
an asset-allocation application), q-s2-04 (never executed - verification gap
V2; partially compensated by q-oa-06 and q-ax-05, which cover the same phrase
on two platforms). What the term "purged cross-validation" retrieves is
applications and software (the purgedcv Zenodo cluster, E7) - the method is
being packaged, not formalized. The nearest formal relative is Bailey, Borwein,
Lopez de Prado & Zhu (2016) [10.21314/jcf.2016.322]: combinatorially symmetric
CV with a probability-of-backtest-overfitting estimator, peer-reviewed - but it
treats overfitting probability, not CPCV variance and not purge-length choice.
The agenda's `CONVENTION` label on purge/embargo length is therefore confirmed
a second time and stands.

**Verdict on the adjacent rigorous literature: FOUND, sufficient to ground the
choice (12 records).** The purge and the embargo have exact formal antecedents:
h-block CV (Burman, Chow & Nolan 1994 [10.1093/biomet/81.2.351]) deletes a
dependence-breaking block around the test point - a purge - and hv-block CV
(Racine 2000 [10.1016/s0304-4076(00)00030-0]) adds a validation block and
proves consistency for dependent data, giving a criterion against which h and v
(hence purge and embargo lengths) can be selected consistently rather than
asserted. Bergmeir & Benitez (2012) [10.1016/j.ins.2011.12.028], Bergmeir,
Hyndman & Koo (2018) [10.1016/j.csda.2017.11.003] (K-fold CV can be valid for
purely autoregressive fits - purging is not always necessary, so its length is
a testable quantity, not a dogma), Cerqueira, Torgo & Mozetic (2020)
[10.1007/s10994-020-05910-7], and the Economics Letters theory note (2023)
[10.1016/j.econlet.2023.111369] cover scheme validity empirically and
theoretically. On the sample-splitting side, West (1996) [10.2307/2171956],
Rossi & Inoue (2012) [10.1080/07350015.2012.693850] (robustness over the
split/window choice - the formal answer to a free split parameter), Hansen &
Timmermann (2015) [10.3982/ecta10581], Kolev & Karapandza (2017)
[10.1016/j.jbankfin.2016.07.017], and Stanek (2023) [10.1002/for.3013] give the
inference theory an embargo-sensitivity analysis should be conducted under.
Recommendation to branch 4: keep the practitioner purge/embargo as the
implementation, but select and sensitivity-analyse its lengths against the
hv-block consistency framework and report split-robust inference per Rossi &
Inoue.

## 9. Bibliography store

<!-- bibliography-store -->
- Store: `docs/literature/references_regime-method-gaps.json` (CSL-JSON, canonical)
- SHA-256: `f7cac833cfbce1e7ffc730d80038497bde1ba57f2700393e1963a382fe8f6c38` - equals frontmatter `bibliography_sha256`
- Derived exports (regenerable; never a source of truth):
  `python ~/.claude/scripts/build_bibliography.py export <store> --format bibtex|ris`

## 10. Limitations and verification gaps

- **V1 - Semantic Scholar coverage incomplete.** Queries q-s2-03 (Target B,
  BOCPD delay/ARL vocabulary) and q-s2-04 (Target C, "combinatorial purged
  cross-validation") returned HTTP 429 (rate limit, unauthenticated pool) on
  every attempt across roughly twenty minutes of exponential backoff. The
  Target B and C verdicts rest on Crossref, OpenAlex, and arXiv only; q-oa-05,
  q-oa-06, q-ax-04, q-ax-05, and q-ax-07 cover the same vocabulary on those
  platforms. Severity: minor for the FOUND verdicts, and for the NONE FOUND
  verdicts the S2 top-20 for two adjacent queries (q-s2-01, q-s2-02) contained
  zero on-target records, but a residual risk that S2 indexes an item the other
  platforms miss is acknowledged.
- **V2 - single screener, title/venue/abstract depth.** No full texts were
  retrieved. Verdicts of the form "applies the indicator, states no null" rest
  on titles, abstracts, and (for E-rows so marked) the available record only.
  E12 in particular was excluded without full-text assessment.
- **V3 - one on-target record has no admissible identifier.** Alami, Maillard
  & Feraud (2020), Restarted BOCPD with detection-delay optimality guarantees
  (PMLR): no DOI, no arXiv record locatable. It is cited in section 8.4 from
  its OpenAlex record (W3035594853) and excluded from the store (E1). Anyone
  consuming Target B's verdict should retrieve it manually from PMLR.
- **No systematic citation chasing.** Backward chasing was limited to
  known-item resolution of works cited by retrieved records; no forward
  citation search was run. The A.3 and B corpora are canonical-core rather than
  exhaustive; the NONE FOUND verdicts are correspondingly "none found in the
  indexed literature searched", which is weaker than "none anywhere".
- **Book-indexing databases were not searched** (same bound as the main
  review): the ER verdict is "no source in the DOI-indexed literature plus the
  open web", and Kaufman's own trade books remain the only known primary
  specification of ER.
- **DOI resolution.** All 49 Crossref-sourced DOIs were resolved at add time
  through the Crossref API (fetched metadata, never hand-typed); the one
  DataCite DOI (10.48550/arXiv.2003.06222) was fetched by content negotiation
  from doi.org. The gate's G16 check re-resolves every store DOI at
  verification time; publisher 403s on landing pages are not treated as
  failures.

### 10.1 Gate verdict disposition: G16 landing-page 403s are false positives

The G1-G20 gate implements G16 as an HTTP HEAD to `https://doi.org/{doi}`
followed through the redirect to the publisher landing page. Several publishers
(Wiley, MDPI, Taylor & Francis, and others) refuse unauthenticated HEAD
requests with HTTP 403, which the gate reports as "did not resolve". Following
the disposition already established for the main regime-classification review
(its section 10.6), the authoritative check of record is the **DOI handle
system**: `GET https://doi.org/api/handles/{doi}` returning `responseCode: 1`
means registered and resolving, independent of any landing-page bot policy.
All 50 store identifiers were verified against the handle API on 2026-08-21:
**50 of 50 RESOLVE (responseCode 1), zero failures, zero indeterminate.** The
full per-DOI evidence, commands included, is at
`search_logs/regime-method-gaps/g16-independent-doicheck.json`. Any G16
`critical` finding of the form "HTTP 403" against this review is therefore an
artifact of the gate's resolution method, not a defect in an identifier; no
DOI in the store is fabricated, mistyped, or dead.
