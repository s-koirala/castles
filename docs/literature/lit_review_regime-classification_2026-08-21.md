---
title: "Regime classification: level estimation, state assignment, transition detection, and label-free validation"
slug: regime-classification
date: 2026-08-21
objective: "Locate, for each method proposed in the regime-classification research agenda, its primary source, whether it carries a derivation or a null distribution, and its documented failure modes and small-sample behaviour."
review_type: systematic
standard_declared: "PRISMA 2020 + PRISMA-S (adapted, non-clinical) - PARTIAL COMPLIANCE, single screener; see section 1.3 for the item-by-item conformance statement"
eligibility_inclusion:
  - "Primary methodological source for a named estimator, test, detector, or model class appearing in one of the four agenda branches (level estimation, state assignment, transition detection, label-free validation)."
  - "Study reporting the null distribution, size, power, small-sample bias, or documented failure mode of such a method."
  - "Study supplying empirical evidence about the existence or persistence of price levels, market states, or regime transitions in financial time series."
  - "Methodological source establishing the deseasonalization or causal-time preconditions the agenda declares as standing hazards."
  - "Any language; any year; journal article, conference paper, book chapter, or preprint carrying a persistent identifier."
eligibility_exclusion:
  - "Records whose only contribution is the profitability of a trading rule, with no distributional or estimator-theoretic content (out of scope by task directive)."
  - "Records retrieved in error, where the identifier resolved to a work outside every branch."
  - "Trade, vendor, blog, or encyclopedia sources with no persistent identifier; these are recorded as provenance for negative findings but are never corpus entries."
  - "Applications of a method to an unrelated substantive domain that add no estimator-theoretic or failure-mode content."
  - "Records concerning the project's architecture or context-portability agendas."
registration: not-registered
protocol_path: none
protocol_amendments: "Search executed 2026-08-21 in a prior session that terminated on an API error before the review was written. This session reconstructed provenance from the on-disk search logs and executed sixteen additional gap queries (gap-crossref-26, gap-s2-27, gap-openalex-28, gap-crossref-29 through gap-crossref-40, gap-webfetch-41) whose targets were identified during screening. No eligibility criterion was altered after the first search."
bibliography: docs/literature/references_regime-classification.json
bibliography_sha256: 80980318c0c67b2bac95c3c0cd24a908ac54fb7bdd8a23f4081f9bd7c2612e8d
n_identified: 518
n_duplicates_removed: 56
n_screened: 462
n_excluded: 366
n_included: 96
materials_availability:
  - docs/literature/search_logs/regime-classification/
  - docs/literature/references_regime-classification.json
competing_interests: none
ai_assistance: "Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK, research-librarian agent) executed the searches, the screening, the metadata resolution, and the drafting of this review. It is the sole screener and is declared as an automation tool under PRISMA 2020 item 8. No human second screener participated. Reproducibility log directory: logs/reproducibility/"
git_head_at_authoring: "n/a - project directory is not a git repository at authoring time (git rev-parse HEAD returns: fatal: ambiguous argument HEAD)"
pip_freeze_sha256: "n/a - no analysis code executed; only metadata-retrieval and bibliography-store scripts"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-opus-5"
---

# Regime classification: level estimation, state assignment, transition detection, and label-free validation

## 1. Objective and eligibility

### 1.1 Objective

The regime-classification agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md))
asks whether market state can be assigned causally at time *t*, with a stated
null distribution, such that the assignment carries predictive content about
*t+1* onward. This review supplies the corpus that question needs. For every
method named in the agenda's four branches it records three things and only
three things:

- **(a) Null or derivation.** Does the method have a stated null distribution, a
  derivation, or an asymptotic theory - or is it folklore asserted without one?
- **(b) Primary source**, resolved to a persistent identifier.
- **(c) Documented failure modes and small-sample behaviour.**

The review does not assess whether any method is profitable. A profitability
study is eligible only where it is the sole peer-reviewed evidence bearing on
whether a method has a derivation, and its performance claims are not evaluated
here.

### 1.2 Grouping for synthesis

Records are grouped by the agenda branch they serve: (1) level estimation,
(2) state assignment, (3) transition detection, (4) label-free validation. A
record serving two branches is listed under its primary branch and
cross-referenced. Within a branch, records are ordered method-family first, then
the failure-mode evidence for that family.

### 1.3 Conformance statement - this is a single-screener review

> The project charter
> ([charter_castles_2026-08-21.md](../methodology/charter_castles_2026-08-21.md),
> section "Systematic review standard") requires conduct and reporting to PRISMA
> 2020, including **dual independent screening and extraction with an agreement
> measure**. **A single agent cannot satisfy that requirement.** Two screening
> passes by the same model are not independent: they share training data,
> parameters, and systematic bias, so any agreement statistic computed between
> them measures decoding variance, not reliability. Reporting a kappa from such a
> pair would be worse than reporting none, because it would look like evidence.
> This review therefore declares itself **PRISMA 2020 partial compliance, single
> screener**, and states below exactly which items are met and which are not.
> Per the charter, an honest limitation is a first-class result; a compliance
> claim that cannot be delivered is a defect.

| PRISMA 2020 item | Status | Note |
|---|---|---|
| 3 Rationale, 4 Objectives | met | section 1.1 |
| 5 Eligibility criteria | met | frontmatter; fixed before the gap searches and inherited unchanged from the first search session |
| 6 Information sources | met | section 2 table, one row per executed query, with platform and ISO 8601 date |
| 7 Search strategy | **partially met** | verbatim capture holds for arXiv, for the sixteen gap queries, and for WebSearch; it **fails for the twenty-five original Crossref topical queries**, whose query strings were not written to the logs at execution time and are not reconstructable. See section 3 and section 10.1. |
| 8 Selection process | met, negatively | one screener, not independent, automation tool declared with version - section 5 |
| 9 Data collection process | **partially met** | single extractor, no duplicate extraction, no agreement measure |
| 10 Data items | met | the three fields (a)/(b)/(c) in section 1.1 are the extraction schema |
| 11 Risk of bias in studies | **not met** | no risk-of-bias instrument was applied. No validated instrument exists for methodological and econometric primary sources of this kind; ROBIS, RoB 2 and QUADAS-2 target clinical designs this corpus does not contain. Rather than misapply one, the review records an evidence tier per record (section 7) and a derivation-status verdict per method (section 8). That substitution is **not** equivalent to a risk-of-bias assessment and must not be reported as one. |
| 12-15 Effect measures, synthesis methods, reporting-bias, certainty | **not applicable / not met** | no effect sizes are pooled; this is a methodological corpus, not an intervention synthesis. No GRADE assessment. |
| 16a Flow of records | met | frontmatter counts, arithmetic-checked |
| 16b Exclusions with reasons | met | section 6 |
| 17-22 Study characteristics, RoB results, results of syntheses | partially met | sections 7 and 8 carry characteristics and narrative synthesis; no risk-of-bias results |
| 23 Certainty of evidence | **not met** | no formal certainty rating |
| 24a/b/c Registration and protocol | met, negatively | not registered, no protocol, amendments recorded in frontmatter |
| 25 Support | met | none |
| 26 Competing interests | met | none |
| 27 Availability of data, code, materials | met | search logs and CSL-JSON store committed |

**Publication-bias posture** (charter section "Publication-bias posture"). No
small-study or publication-bias assessment was performed, and none is meaningful
here: the units are methods, not effect estimates, so there is no funnel to
inspect. The relevant bias in this corpus is different and is stated plainly -
**a method with no primary source cannot be retrieved by a bibliographic
search.** The negative findings in section 8.5 are therefore evidence of absence
*in the indexed literature*, which is weaker than evidence of absence, and are
labelled as such throughout.

## 2. Information sources and methods

<!-- prisma-s-1 -->
One row per executed query. `n_records` is the number of records actually
retrieved and carried into screening, not the total-hit count the API reported;
total-hit counts survive in the raw logs and, for the rows whose query string was
lost, are the only remaining quantitative trace (section 10.1).

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-01 | 13 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-02 | 15 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-03 | 15 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-04 | 6 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-05 | 11 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-06 | 11 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-07 | 7 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-08 | 5 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-09 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-10 | 10 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-ki | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-01 | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-02 | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-03 | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-04 | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-05 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-06 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-07 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-08 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-09 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-10 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-11 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-12 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-13 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-14 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-15 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-16 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-17 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-18 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-19 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-20 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-21 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-22 | 5 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-23 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-24 | 10 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | q-crossref-25 | 10 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch1 | 12 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch2 | 16 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch3 | 16 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch4 | 13 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch5 | 13 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch6 | 9 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch7 | 8 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | ki-batch8 | 5 |
| Crossref | Crossref REST API (api.crossref.org), known-item DOI lookup | 2026-08-21 | gap-crossref-26 | 1 |
| Semantic Scholar | Semantic Scholar Graph API v1 (api.semanticscholar.org) | 2026-08-21 | gap-s2-27 | 5 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | gap-openalex-28 | 1 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-29 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-30 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-31 | 8 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-32 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-33 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-34 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-35 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-36 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-37 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-38 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-39 | 6 |
| Crossref | Crossref REST API (api.crossref.org) | 2026-08-21 | gap-crossref-40 | 6 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | openalex-ecta5771 | 1 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | openalex-ecta8609 | 1 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-08-21 | openalex-mcs-search | 3 |
| Semantic Scholar | Semantic Scholar Graph API v1 (api.semanticscholar.org) | 2026-08-21 | s2-ecta5771 | 0 |
| Semantic Scholar | Semantic Scholar Graph API v1 (api.semanticscholar.org) | 2026-08-21 | s2-mcs-search | 0 |
| Web search (grey and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-01 | 9 |
| Web search (grey and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-02 | 10 |
| Web search (grey and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-03 | 8 |
| Web search (grey and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-04 | 10 |
| Web search (grey and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-05 | 9 |
| Publisher website | Wiley Online Library (onlinelibrary.wiley.com) via WebFetch | 2026-08-21 | gap-webfetch-41 | 1 |

**Total records identified: 518** (equals frontmatter `n_identified`).

<!-- prisma-s-2 -->
No multi-database platform search was used. Crossref, OpenAlex, Semantic Scholar
and arXiv were each queried directly through their own public REST or Atom API.
No Ovid, EBSCOhost, ProQuest or Web of Science interface was available to this
project, and no clinical database (MEDLINE, Embase, CINAHL) was searched, because
the corpus is econometric and statistical rather than clinical.

<!-- prisma-s-3 -->
No study registries were searched. PROSPERO, ClinicalTrials.gov, ICTRP and OSF
Registries index prospective clinical and behavioural protocols; none indexes the
econometric and statistical methodology this review covers, and no registry of
quantitative-finance method studies was located.

<!-- prisma-s-4 -->
Five purposeful web searches (`q-websearch-01` through `q-websearch-05`) were run
against trade, vendor and encyclopedia sources for four methods with no indexed
primary source: the Average Directional Index, the Choppiness Index, the Market
Profile value-area convention, and the Kaufman Efficiency Ratio. Those 46 returned
URLs are recorded as provenance for the negative findings in section 8.5. **None
became a corpus entry**; none carries a persistent identifier and all fail the
eligibility criteria.

<!-- prisma-s-5 -->
No systematic backward or forward citation searching was performed, and no
citation-chasing tool (Scopus, Web of Science, Connected Papers, citationchaser)
was used. The known-item DOI batches (`ki-batch1` to `ki-batch8`) were assembled
from references named in the research agenda and from reference lists encountered
while reading retrieved abstracts, which is opportunistic snowballing rather than
systematic citation searching. This is a recall limitation and is recorded in
section 10.2.

<!-- prisma-s-6 -->
No contacts were made with authors, experts, manufacturers, or information
specialists.

<!-- prisma-s-7 -->
One publisher-website retrieval (`gap-webfetch-41`) was used to resolve author
metadata that was absent from both Crossref and OpenAlex for
doi:10.3982/ECTA5771. No other information source or search method was used.

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S item 8 requires each strategy copied and pasted exactly as run. Each
fence below ends its info string with the `query_id` from the section 2 table.
Fences whose content begins `QUERY STRING NOT CAPTURED` record an explicit
reporting failure, not a paraphrase: the string was never written to the log and
is deliberately not reconstructed. Twenty-five of the sixty-nine rows are in that
state; see section 10.1.

*q-arxiv-01 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-01
search_query=all:"Bayesian online changepoint detection"&id_list=&start=0&max_results=15
```

*q-arxiv-02 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-02
search_query=abs:"Hurst exponent" AND (abs:"finite sample" OR abs:"bias" OR abs:"estimator")&id_list=&start=0&max_results=15
```

*q-arxiv-03 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-03
search_query=abs:"market regime" AND (abs:"clustering" OR abs:"Wasserstein" OR abs:"detection")&id_list=&start=0&max_results=15
```

*q-arxiv-04 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-04
search_query=all:"hidden semi-Markov" AND (all:"financial" OR all:"stock" OR all:"regime")&id_list=&start=0&max_results=15
```

*q-arxiv-05 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-05
search_query=abs:"number of states" AND abs:"hidden Markov" AND (abs:"BIC" OR abs:"model selection" OR abs:"order")&id_list=&start=0&max_results=15
```

*q-arxiv-06 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-06
search_query=abs:"backtest overfitting" OR abs:"purged cross-validation" OR (abs:"cross-validation" AND abs:"financial machine learning")&id_list=&start=0&max_results=15
```

*q-arxiv-07 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-07
search_query=abs:"support and resistance" AND (abs:"price" OR abs:"market")&id_list=&start=0&max_results=15
```

*q-arxiv-08 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-08
search_query=abs:"regime" AND abs:"efficiency ratio" OR abs:"trend strength" AND abs:"indicator"&id_list=&start=0&max_results=12
```

*q-arxiv-09 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-09
search_query=all:"efficiency ratio" AND all:"Kaufman"&id_list=&start=0&max_results=10
```

*q-arxiv-10 - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-10
search_query=all:"average directional" OR all:"choppiness index"&id_list=&start=0&max_results=10
```

*q-arxiv-ki - server echo of the query as executed, taken from the feed title element*

```text q-arxiv-ki
search_query=&id_list=0710.3742,2302.04759,2306.15835,2101.07410,1201.4786,1909.05800,1804.10308,2310.01285,2104.03667,2107.00066&start=0&max_results=20
```

*q-crossref-01 - see section 10.1*

```text q-crossref-01
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 821805
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-02 - see section 10.1*

```text q-crossref-02
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 897812
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-03 - see section 10.1*

```text q-crossref-03
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 5655748
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-04 - see section 10.1*

```text q-crossref-04
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 568378
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-05 - see section 10.1*

```text q-crossref-05
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 2819990
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-06 - see section 10.1*

```text q-crossref-06
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 7511547
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-07 - see section 10.1*

```text q-crossref-07
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 5014281
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-08 - see section 10.1*

```text q-crossref-08
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 1394501
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-09 - see section 10.1*

```text q-crossref-09
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 4525601
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-10 - see section 10.1*

```text q-crossref-10
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 1071820
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-11 - see section 10.1*

```text q-crossref-11
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 2855341
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-12 - see section 10.1*

```text q-crossref-12
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 67303
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-13 - see section 10.1*

```text q-crossref-13
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 251095
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-14 - see section 10.1*

```text q-crossref-14
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 242975
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-15 - see section 10.1*

```text q-crossref-15
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 9539421
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-16 - see section 10.1*

```text q-crossref-16
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 15431351
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-17 - see section 10.1*

```text q-crossref-17
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 1147362
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-18 - see section 10.1*

```text q-crossref-18
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 72556
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-19 - see section 10.1*

```text q-crossref-19
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 168201
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-20 - see section 10.1*

```text q-crossref-20
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 2495092
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-21 - see section 10.1*

```text q-crossref-21
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 93301
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-22 - see section 10.1*

```text q-crossref-22
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 4143225
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-23 - see section 10.1*

```text q-crossref-23
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 6186904
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-24 - see section 10.1*

```text q-crossref-24
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 95887
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*q-crossref-25 - see section 10.1*

```text q-crossref-25
QUERY STRING NOT CAPTURED AT EXECUTION TIME.
PRISMA-S item 8 is NOT satisfied for this row.
Endpoint used (from the response envelope): https://api.crossref.org/works?query.bibliographic=<string>&rows=<n>
total-results returned by the API for the uncaptured string: 1871025
The string is NOT reconstructed here. Reconstructing a query after the fact
is prohibited by PRISMA-S item 8 and would misrepresent provenance.
```

*ki-batch1 - the DOI list is the query*

```text ki-batch1
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/jae.3950070506
10.1016/0304-4076(93)90051-6
10.1016/0304-4076(94)90036-1
10.1016/S0378-4371(02)01383-3
10.1029/WR005i002p00321
10.1080/07350015.2000.10524842
10.1093/rfs/1.1.41
10.1103/PhysRevE.49.1685
10.1111/j.1468-0262.2007.00809.x
10.2307/1912559
10.2307/2938368
10.3982/ECTA8609
```

*ki-batch2 - the DOI list is the query*

```text ki-batch2
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/(SICI)1099-131X(199901)18:1<1::AID-FOR685>3.0.CO;2-B
10.1002/jae.664
10.1007/s13253-017-0283-8
10.1016/0304-4076(89)90083-3
10.1016/S0378-4371(02)00961-5
10.1016/j.artint.2009.11.011
10.1016/j.csda.2006.07.021
10.1016/j.ijforecast.2017.11.002
10.1093/jjfinec/nbh020
10.1109/18.650984
10.1109/34.865189
10.1111/1467-9892.00305
10.1146/annurev-financial-110311-101808
10.1198/073500104000000136
10.1198/073500107000000296
10.2307/2527399
```

*ki-batch3 - the DOI list is the query*

```text ki-batch3
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/jae.659
10.1080/01621459.1994.10476870
10.1080/01621459.2012.737745
10.1080/07474930802459016
10.1081/ETC-120028836
10.1090/noti1105
10.1093/biomet/41.1-2.100
10.1093/biomet/58.3.509
10.1111/0022-1082.00163
10.1111/j.1467-9868.2007.00601.x
10.1111/j.1468-0262.2005.00615.x
10.1198/073500105000000063
10.1214/aoms/1177693055
10.1214/aoms/1177731118
10.1214/aos/1176350164
10.3905/jpm.2014.40.5.094
```

*ki-batch4 - the DOI list is the query*

```text ki-batch4
GET https://api.crossref.org/works/{DOI} for each of:
10.1016/S0927-5398(97)00022-4
10.1016/j.ijforecast.2018.05.004
10.1016/j.jempfin.2008.03.002
10.1080/01621459.1999.10474186
10.1109/18.720549
10.1111/1540-6261.00583
10.1111/j.1540-6261.1992.tb04681.x
10.1111/j.2517-6161.1981.tb01155.x
10.1111/j.2517-6161.1991.tb01857.x
10.1214/aos/1176346577
10.1214/aos/1176350951
10.2307/2331058
10.2469/faj.v58.n4.2453
```

*ki-batch5 - the DOI list is the query*

```text ki-batch5
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/for.3980090104
10.1007/BF00053066
10.1016/j.euroecorev.2005.01.002
10.1016/j.frl.2006.01.001
10.1016/j.jempfin.2010.11.009
10.1016/j.sigpro.2019.107299
10.1061/TACEAT.0006518
10.1109/18.737522
10.1111/1540-6261.00588
10.1214/aoms/1177730197
10.21314/JCF.2016.322
10.2307/2331416
10.3905/jpm.2018.44.6.120
```

*ki-batch6 - the DOI list is the query*

```text ki-batch6
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/for.2447
10.1007/s001810100100
10.1016/0304-4076(90)90093-9
10.1016/j.euroecorev.2005.09.001
10.1016/j.frl.2009.04.003
10.1016/j.jempfin.2010.11.005
10.1198/073500104000000073
10.1287/opre.13.2.258
10.3982/ECTA5771
```

*ki-batch7 - the DOI list is the query*

```text ki-batch7
GET https://api.crossref.org/works/{DOI} for each of:
10.1002/(sici)1099-1255(199805/06)13:3<217::aid-jae476>3.0.co;2-v
10.1007/s13571-024-00322-2
10.1016/0304-405x(96)00875-6
10.1016/j.jempfin.2010.01.001
10.21314/jcf.2024.005
10.21511/bbs.13(3).2018.06
10.2202/1558-3708.1145
10.2307/2998540
```

*ki-batch8 - the DOI list is the query*

```text ki-batch8
GET https://api.crossref.org/works/{DOI} for each of:
10.1016/j.econmod.2022.105832
10.1016/j.physa.2010.05.025
10.1561/2200000054
10.32473/flairs.v34i1.128424
10.3934/DSFE.2025016
```

*gap-crossref-26 - verbatim, executed by this session*

```text gap-crossref-26
GET https://api.crossref.org/works/10.3982/ECTA5771
```

*gap-s2-27 - verbatim, executed by this session*

```text gap-s2-27
GET https://api.semanticscholar.org/graph/v1/paper/search?query=The%20Model%20Confidence%20Set%20Econometrica&fields=title,year,venue,authors,externalIds&limit=5
```

*gap-openalex-28 - verbatim, executed by this session; contact address redacted per identity-hygiene rule*

```text gap-openalex-28
GET https://api.openalex.org/works/https://doi.org/10.3982/ecta5771?mailto=<contact>
```

*gap-crossref-29 - verbatim, executed by this session*

```text gap-crossref-29
GET https://api.crossref.org/works
  query.bibliographic = calibration of Silverman test for multimodality critical bandwidth
  rows = 8
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-30 - verbatim, executed by this session*

```text gap-crossref-30
GET https://api.crossref.org/works
  query.bibliographic = excess mass test number of modes significance
  rows = 8
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-31 - verbatim, executed by this session*

```text gap-crossref-31
GET https://api.crossref.org/works
  query.bibliographic = cross-validation for evaluating autoregressive time series prediction validity
  rows = 8
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-32 - verbatim, executed by this session*

```text gap-crossref-32
GET https://api.crossref.org/works
  query.bibliographic = Hall York bandwidth choice Silverman test unimodality calibration
  rows = 6
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-33 - verbatim, executed by this session*

```text gap-crossref-33
GET https://api.crossref.org/works
  query.bibliographic = Muller Sawitzki excess mass estimates tests for multimodality
  rows = 6
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-34 - verbatim, executed by this session*

```text gap-crossref-34
GET https://api.crossref.org/works
  query.bibliographic = Mammen Marron Fisher asymptotics multimodality tests kernel density estimates
  rows = 6
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-35 - verbatim, executed by this session*

```text gap-crossref-35
GET https://api.crossref.org/works
  query.bibliographic = on the use of cross-validation for time series predictor evaluation
  rows = 6
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-36 - verbatim, executed by this session*

```text gap-crossref-36
GET https://api.crossref.org/works
  query.bibliographic = purged combinatorial cross-validation financial machine learning backtest leakage
  rows = 6
  select = DOI,title,author,issued,container-title,type,volume,page
```

*gap-crossref-37 - verbatim, executed by this session*

```text gap-crossref-37
GET https://api.crossref.org/works
  query.bibliographic = On the calibration of Silverman's test for multimodality
  rows = 6
  select = DOI,title,author,issued,container-title,type
```

*gap-crossref-38 - verbatim, executed by this session*

```text gap-crossref-38
GET https://api.crossref.org/works
  query.bibliographic = Wilder new concepts in technical trading systems average directional movement index
  rows = 6
  select = DOI,title,author,issued,container-title,type
```

*gap-crossref-39 - verbatim, executed by this session*

```text gap-crossref-39
GET https://api.crossref.org/works
  query.bibliographic = Choppiness Index Dreiss fractal dimension trading range indicator
  rows = 6
  select = DOI,title,author,issued,container-title,type
```

*gap-crossref-40 - verbatim, executed by this session*

```text gap-crossref-40
GET https://api.crossref.org/works
  query.bibliographic = Kaufman efficiency ratio adaptive moving average trend noise
  rows = 6
  select = DOI,title,author,issued,container-title,type
```

*openalex-ecta5771 - RECONSTRUCTED from the log filename and the returned work id; NOT a verbatim capture*

```text openalex-ecta5771
GET https://api.openalex.org/works/https://doi.org/10.3982/ecta5771
```

*openalex-ecta8609 - RECONSTRUCTED from the log filename and the returned work id; NOT a verbatim capture*

```text openalex-ecta8609
GET https://api.openalex.org/works/https://doi.org/10.3982/ecta8609
```

*openalex-mcs-search - server echo of the executed query, from meta.x_query.url*

```text openalex-mcs-search
GET /works?filter=display_name.search:The Model Confidence Set&per_page=3
```

*s2-ecta5771 - 0 records retrieved; see section 10.1*

```text s2-ecta5771
DOI lookup for 10.3982/ECTA5771. FULL REQUEST URL NOT CAPTURED.
API response, verbatim: {"error":"Paper with id DOI:10.3982/ECTA5771 not found"}
```

*s2-mcs-search - 0 records retrieved; rate-limited, retried as gap-s2-27*

```text s2-mcs-search
Title search for The Model Confidence Set. FULL REQUEST URL NOT CAPTURED.
API response, verbatim: {"message": "Too Many Requests. Please wait and try again or apply for a key for higher rate limits. https://www.semanticscholar.org/product/api#api-key-form", "code": "429"}
```

*q-websearch-01 - verbatim as issued to the tool*

```text q-websearch-01
"Average Directional Index" ADX Wilder 1978 statistical evaluation null distribution peer-reviewed
```

*q-websearch-02 - verbatim as issued to the tool*

```text q-websearch-02
"Choppiness Index" Dreiss original publication derivation technical indicator
```

*q-websearch-03 - verbatim as issued to the tool*

```text q-websearch-03
Market Profile "value area" 70 percent convention Steidlmayer CBOT origin one standard deviation empirical basis
```

*q-websearch-04 - verbatim as issued to the tool*

```text q-websearch-04
Osler "Support for Resistance" technical analysis intraday exchange rates Federal Reserve Bank of New York Economic Policy Review 2000
```

*q-websearch-05 - verbatim as issued to the tool*

```text q-websearch-05
CME Group official documentation Market Profile "value area" definition 70% of volume TPO handbook
```

*gap-webfetch-41 - author metadata absent from both Crossref and OpenAlex; resolved from the publisher record*

```text gap-webfetch-41
GET https://onlinelibrary.wiley.com/doi/10.3982/ECTA5771
```

<!-- prisma-s-9 -->
**Limits and restrictions.** No date limit, no language limit, no publication-type
limit and no subject limit were applied to any query. Two mechanical restrictions
did apply and both are recall-limiting: (i) each arXiv query was capped at
`max_results` between 10 and 20, and each Crossref query at `rows` between 5 and
10, so broad queries returned only the platform-ranked head of the result set -
`q-arxiv-02` returned 15 of 137 hits and `q-arxiv-10` returned 10 of 92; (ii) no
result set was paged beyond the first page. These caps were not justified by any
empirical criterion and are recorded as a limitation, not as a design choice
(section 10.2).

<!-- prisma-s-10 -->
No published search filters or hedges were used. No validated filter exists for
econometric or statistical-methodology retrieval; the clinical filter literature
(for example the Cochrane RCT hedges) is not transferable to this corpus.

<!-- prisma-s-11 -->
No search strategy was adapted or reused from a prior published review. The
strategies were constructed de novo from the four branches of the research agenda.

<!-- prisma-s-12 -->
No update is scheduled and no email alerts or saved searches were created. If the
review is refreshed, the arXiv and gap-Crossref strategies in this section are
re-runnable verbatim; the twenty-five original Crossref topical strategies are
**not** re-runnable and would have to be redesigned from scratch, which would make
the refreshed search a different search.

<!-- prisma-s-13 -->
Date of the last search, per strategy: **2026-08-21** for every strategy in the
section 2 table, matching every `date_searched` value in that column. The original
session executed `q-arxiv-*`, `q-crossref-*`, `ki-batch*`, `openalex-*`, `s2-*`
and `q-websearch-*` between 14:43 and 14:58 UTC; this session executed
`gap-crossref-26`, `gap-s2-27`, `gap-openalex-28`, `gap-crossref-29` through
`gap-crossref-40` and `gap-webfetch-41` later the same day.

## 4. Peer review of the strategy

<!-- prisma-s-14 -->
**Not peer reviewed.** No PRESS 2015 review by an information specialist was
obtained, and no second agent re-derived the strategy adversarially. The strategy
therefore carries no external check on its Boolean logic, its line-by-line
spelling, or its subject coverage - the four PRESS domains. The concrete
consequence is visible in the corpus itself: `q-arxiv-08` uses an unparenthesised
mixed AND/OR expression whose precedence almost certainly did not express the
intended concept, and it returned 5 records. A PRESS review would have caught
that before execution.

## 5. Managing records

<!-- prisma-s-15 -->
**Records identified per source.** The `n_records` column of the section 2 table
is the complete accounting; it sums to **518**, equal to frontmatter
`n_identified`. Aggregated by platform:

| platform | queries | records identified |
|---|---|---|
| arXiv API v1 (topical) | 10 | 93 |
| arXiv API v1 (known-item id_list) | 1 | 10 |
| Crossref REST API (topical, original session) | 25 | 186 |
| Crossref REST API (topical, gap session) | 12 | 78 |
| Crossref REST API (known-item DOI lookup) | 9 | 93 |
| OpenAlex REST API | 4 | 6 |
| Semantic Scholar Graph API | 3 | 5 |
| Claude Code WebSearch | 5 | 46 |
| Wiley Online Library (WebFetch) | 1 | 1 |
| **total** | **70** | **518** |

No source is represented outside that table. No records were obtained by hand
searching, by contacting authors, or from any unlogged source.

<!-- prisma-s-16 -->
**Deduplication process and software.** Deduplication was mechanical, not manual.
A Python 3.11 script (`classify.py` / `dedup.py`, run 2026-08-21; scratch
artifacts, so the logic is reproduced here in full rather than referenced)
assigned each of the 518 retrieved records one collision key, in this priority
order:

1. `doi:` + DOI, lowercased, as returned by the source. For arXiv Atom entries
   this is the `<arxiv:doi>` element, present when the preprint has a published
   DOI.
2. `arxiv:` + the arXiv identifier with any trailing version suffix stripped by
   the regex `v\d+$`, for arXiv entries with no published DOI.
3. `url:` + the result URL, lowercased with any trailing slash removed, for
   WebSearch results, which carry no bibliographic identifier at all.
4. `ti:` + title lowercased with all non-alphanumeric characters removed, for the
   single Semantic Scholar record lacking a DOI.

Records sharing a key were collapsed to one. **518 retrieved, 462 distinct keys,
56 duplicates removed.** No fuzzy or probabilistic matching was used; no
reference-manager deduplication (EndNote, Zotero, Rayyan, Deduklick) was applied.

The consequence of exact-key matching is stated rather than hidden. A work
indexed under two different DOIs - a journal article and its NBER, SSRN or
book-chapter reissue - is **not** collapsed, and is counted twice at
identification. That pattern is present and quantified: a post-hoc exact-title
match between the 366 excluded records and the 96 included ones finds **11
excluded records that are alternate versions of an included work**, among them
`doi:10.3386/w2168` and `arxiv:2203.13820`. These were resolved by hand at
screening, so only one version of each work entered the store and the
**included** count is free of version duplication; but `n_duplicates_removed = 56`
understates the true duplication rate by at least 11. Reported this way rather
than adjusted, because adjusting it would require a fuzzy-match threshold with no
empirical justification (CLAUDE.md, no arbitrary thresholds).

<!-- prisma-2020-8 -->
PRISMA 2020 item 8, selection process. An LLM screener is an automation tool in
the item's own terms and is named here with its version.

- **screeners_n**: 1
- **independent**: no - single screener. No second screener, human or machine,
  examined any record. No inter-rater agreement statistic is reported and none
  could be; see section 1.3.
- **automation_tools**: Claude Opus 5 (model id `claude-opus-5`), running as the
  `research-librarian` agent under the Claude Agent SDK / Claude Code harness.
  It decided **every** inclusion and exclusion, executed the sixteen gap queries,
  extracted the (a)/(b)/(c) fields, and assigned the branch and evidence tier of
  every included record. Screening used title, venue, year, author and - where
  Crossref supplied one - abstract. It did **not** use full text; see section 10.3.

**Screening procedure.** Records were screened in one pass against the frozen
eligibility criteria in the frontmatter. There was no separate title/abstract and
full-text stage, because full texts were not retrieved; the single stage is
recorded as `title-abstract` in section 6. The 92 known-item DOI lookups plus the
gap-session lookup constitute a second, deeper assessment for records that
survived topical screening: each was resolved to complete Crossref metadata
before a final decision, and the thirteen that were resolved and then not stored
are the item-16b near-misses below.

## 6. Excluded records

<!-- prisma-2020-16b -->
Records that appeared to meet the inclusion criteria and were nevertheless
excluded, with a reason for each. **366 records were excluded.** Ten near-misses
that reached full-metadata assessment are named individually; the remainder are
accounted for by mechanically derived category in the second table. Three of the
thirteen records that were resolved to full Crossref metadata in the first
session and then not stored (Kantelhardt et al. 2002, Petruccelli 1990,
Gurrib 2018) were re-screened this session against the same frozen criteria and
**included**; their inclusion is recorded in section 7.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E1 | Gencay R (1998) The predictability of security returns with simple technical trading rules. *J Empir Finance* 5:347-359. doi:10.1016/S0927-5398(97)00022-4 | full-metadata | Contribution is the out-of-sample profitability of moving-average trading rules. No null distribution, no estimator theory, no state-assignment construct. Excluded by the profitability criterion, which the task directive makes explicit. |
| E2 | Muller DW, Sawitzki G (1995) Corrections: Excess Mass Estimates and Tests for Multimodality. doi:10.2307/2291192 | title-abstract | Corrigendum record whose corrected article (doi:10.1080/01621459.1991.10475103) is included. Adds no method and no null distribution. Its existence is nevertheless flagged as a caution in section 8.1. |
| E3 | Lee C, Jang W (2018) Kernel excess mass test for multimodality. *Aust N Z J Stat*. doi:10.1111/anzs.12214 | title-abstract | Later variant within the excess-mass family, whose primary source (Muller & Sawitzki 1991) and comparative evaluation (Ameijeiras-Alonso et al. 2018) are both included. Supplies no additional null derivation for branch 1. **A second screener might reasonably have included this record**; the decision is recorded as marginal. |
| E4 | Sawitzki G (1996) The Excess Mass Approach and the Analysis of Multi-Modality. doi:10.1007/978-3-642-79999-0_20 | title-abstract | Expository chapter restating the 1991 method. Not a primary source, not a small-sample study. |
| E5 | Snijders TAB (1988) On Cross-Validation for Predictor Evaluation in Time Series. doi:10.1007/978-3-642-61564-1_4 | title-abstract | Directly on branch 4's question, but superseded for this corpus by two included sources (Bergmeir & Benitez 2012; Bergmeir, Hyndman & Koo 2018) that carry explicit finite-sample simulation evidence. Recorded as a recall gap in section 10.2 rather than as a settled rejection. |
| E6 | Deng Y (2022; 2023) Time Series Cross Validation: Theoretical Properties and Empirical Performance; A Note on Time Series Cross Validation. doi:10.2139/ssrn.3996529; doi:10.2139/ssrn.4366573 | title-abstract | SSRN working papers, no peer-review status, no journal version located. Excluded to keep branch 4's validation theory at peer-reviewed tier, where included alternatives exist. |
| E7 | Mir A, Shrestha S (2026) Quantifying Backtest Overfitting from Information Leakage: A Walk-Forward and Embargo-Based Framework. doi:10.2139/ssrn.7029819 | title-abstract | On-topic for branch 4's purge/embargo question but an unrefereed 2026 SSRN posting with no independent replication. The charter forbids treating a preprint-tier row as settled; admitting it as the *only* source for purged walk-forward would do precisely that. Recorded instead as the branch-4 negative in section 8.4.2. |
| E8 | Mariani F et al. (2025) Analysis of an Algo Trading Strategy Based on the Kaufman Adaptive Moving Average (KAMA) and Stochastic. doi:10.2139/ssrn.5694583 | full-metadata | The only indexed record naming Kaufman's adaptive moving average. An SSRN strategy backtest: no derivation of the Efficiency Ratio, no null distribution, no citation to a primary Kaufman source carrying an identifier. Excluded on both the profitability criterion and the preprint-tier rule - but its content is itself the evidence for the negative finding in section 8.5.1. |
| E9 | Siffer A (2018) Rfolding: The Folding Test of Unimodality. doi:10.32614/cran.package.rfolding; Maechler M (2003) diptest: Hartigan's Dip Test Statistic for Unimodality - Corrected. doi:10.32614/cran.package.diptest | title-abstract | CRAN software-distribution records. They carry DOIs but are implementations, not method sources; the corresponding method source (Hartigan & Hartigan 1985) is included. |
| E10 | Gray RJ (1988) A Class of K-Sample Tests for Comparing the Cumulative Incidence of a Competing Risk. doi:10.1214/aos/1176350951; and eight further records retrieved by known-item DOI lookup whose identifiers resolved to unrelated works (doi:10.1016/j.ijforecast.2017.11.002 book review; doi:10.1109/18.720549 coding-theory survey; doi:10.1111/1540-6261.00583 annual meeting minutes; doi:10.2307/2331058 beta stationarity; doi:10.1016/j.jempfin.2010.11.009 news analytics; doi:10.1016/j.euroecorev.2005.01.002 trade credit; doi:10.1016/j.frl.2006.01.001 asset trading volume; doi:10.1198/073500104000000073 employment decisions) | full-metadata | Retrieved in error: the DOI submitted to the known-item lookup was mistyped or misremembered and resolved to a work outside every branch. Excluded by the retrieved-in-error criterion. The count of nine such records is itself a finding about known-item lookup by recalled DOI and is discussed in section 10.4. |

**Remaining exclusions by mechanically derived category** (356 records; buckets
assigned from the record's Crossref `type` field or key prefix, not by judgment,
so the counts are reproducible from the logs):

| category | n | reason |
|---|---|---|
| Web pages with no persistent identifier (`url:` keys) | 44 | All distinct WebSearch results (46 retrieved, 44 distinct). Vendor documentation, broker marketing, charting-platform help pages, Wikipedia, Grokipedia. Retained as provenance for the negative findings in section 8.5; ineligible as corpus entries under the persistent-identifier exclusion criterion. |
| Preprint-server records with no DOI (`posted-content`) | 111 | arXiv records retrieved by the ten topical arXiv queries. Excluded on topic (deforestation monitoring, radar spectrum sharing, soil drydown, metro ridership, intrusion detection, sunspots, network traffic - all returned by the Hurst and changepoint queries), on being an alternate version of an included work, or on being an application that adds no estimator theory. Five arXiv records survived and are in the corpus. |
| Non-article Crossref objects | 48 | `component` 19, `dataset` 10, `other` 10, `standard` 5, `report` 2, `edited-book` 1, `reference-entry` 1. Figure and table objects, book front matter, indexes, BSI calibration standards, dataset DOIs. Not works that could state a null distribution. |
| Article-like records excluded on topic or scope | 163 | `journal-article` 91, `book-chapter` 32, arXiv-with-published-DOI 23, `proceedings-article` 13, `dissertation` 4. Grounds, in descending frequency as recorded during screening: wrong substantive domain returned by a broad query (medicine, hydrology, materials science, coding theory, labour-market indicator tables); application of an already-included method to an unrelated domain; profitability-only trading study; alternate version of an included work. Per-ground counts were **not** tallied at screening time and are deliberately not reconstructed here. |
| **total** | **366** | |

Arithmetic: 462 screened - 366 excluded = **96 included**, matching frontmatter
`n_included` and the 96-entry bibliography store.

## 7. Included corpus

<!-- included-corpus -->
All 96 included records carry a persistent identifier (FAIR F1). The machine-readable form is the CSL-JSON store; this table is the human-readable
index. The `tier` column is the charter evidence tier and travels with the record. **Five records are `PREPRINT` tier and are marked in bold; per the
charter, no artifact may treat a preprint-tier row as settled.** They are listed together in section 7.5.


### 7.1 Branch 1 - level estimation (15 records)

| id | citation | persistent id | tier | role in the argument |
|---|---|---|---|---|
| `niederhoffer1965opre132258` | Niederhoffer (1965) Clustering of Stock Prices. *Operations Research* 13:258-265. | doi:10.1287/opre.13.2.258 | peer-reviewed | Earliest located empirical documentation of price clustering at round numbers; the observational basis for treating levels as a real phenomenon. |
| `silverman1981j25176161198` | Silverman (1981) Using Kernel Density Estimates to Investigate Multimodality. *Journal of the Royal Statistical Society Series B: Statistical Methodology* 43:97-99. | doi:10.1111/j.2517-6161.1981.tb01155.x | peer-reviewed | Critical-bandwidth approach: the number of modes of a KDE is monotone in bandwidth, giving a test statistic for "at least k modes". The founding source for branch 1 level estimation. |
| `silverman1983cbo978051166` | Silverman (1983) Some properties of a test for multimodality based on kernel density estimates. *Probability, Statistics and Analysis*:248-259. | doi:10.1017/cbo9780511662430.015 | peer-reviewed (edited-volume chapter) | The significance test itself: bootstrap calibration of the critical bandwidth, i.e. a p-value for a mode. This is the record the agenda branch-1 falsification asks for. |
| `hartigan19851176346577` | Hartigan & Hartigan (1985) The Dip Test of Unimodality. *The Annals of Statistics* 13. | doi:10.1214/aos/1176346577 | peer-reviewed | Dip statistic and its null distribution against the least-favourable unimodal (uniform) null. A significance test for unimodality that needs no bandwidth. |
| `romano1988bf00053066` | Romano (1988) Bootstrapping the mode. *Annals of the Institute of Statistical Mathematics* 40:565-586. | doi:10.1007/bf00053066 | peer-reviewed | Bootstrap for the mode location, including where the naive bootstrap fails; supplies the confidence interval the agenda demands before a level is called a level. |
| `mller1991016214591991` | Müller & Sawitzki (1991) Excess Mass Estimates and Tests for Multimodality. *Journal of the American Statistical Association* 86:738-746. | doi:10.1080/01621459.1991.10475103 | peer-reviewed | Excess-mass functional and test for k modes; the second independent significance-test family for modes. |
| `sheather1991j25176161199` | Sheather & Jones (1991) A Reliable Data-Based Bandwidth Selection Method for Kernel Density Estimation. *Journal of the Royal Statistical Society Series B: Statistical Methodology* 53:683-690. | doi:10.1111/j.2517-6161.1991.tb01857.x | peer-reviewed | Solve-the-equation plug-in bandwidth selector, the alternative to the Silverman rule of thumb named in agenda branch 1. |
| `mammen1992bf01194493` | Mammen et al. (1992) Some asymptotics for multimodality tests based on kernel density estimates. *Probability Theory and Related Fields* 91:115-132. | doi:10.1007/bf01194493 | peer-reviewed | Asymptotic theory for critical-bandwidth and excess-mass multimodality tests: consistency, and the rates that govern their small-sample behaviour. |
| `donaldson19932331416` | Donaldson & Kim (1993) Price Barriers in the Dow Jones Industrial Average. *The Journal of Financial and Quantitative Analysis* 28:313. | doi:10.2307/2331416 | peer-reviewed | Formal test for price barriers in the DJIA with a stated null on the uniformity of digit frequencies. |
| `fischer1994016794739490` | Fischer et al. (1994) Testing for multimodality. *Computational Statistics & Data Analysis* 18:499-512. | doi:10.1016/0167-9473(94)90080-9 | peer-reviewed | Finite-sample comparison of multimodality tests; direct evidence on which test to use in a short window. |
| `chaudhuri1999016214591999` | Chaudhuri & Marron (1999) SiZer for Exploration of Structures in Curves. *Journal of the American Statistical Association* 94:807-823. | doi:10.1080/01621459.1999.10474186 | peer-reviewed | SiZer: scale-space inference for features of a curve with simultaneous confidence limits across bandwidths; sidesteps the single-bandwidth choice for mode identification. |
| `osler2003154062610058` | Osler (2003) Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis. *The Journal of Finance* 58:1791-1819. | doi:10.1111/1540-6261.00588 | peer-reviewed | Order-book mechanism for support/resistance: take-profit orders cluster at round numbers, stop-loss orders just beyond. Links a price-derived level to a book-derived one, which is agenda branch 1s book-versus-price question. |
| `sonnemans2006jeuroecorev2` | Sonnemans (2006) Price clustering and natural resistance points in the Dutch stock market: A natural experiment. *European Economic Review* 50:1937-1950. | doi:10.1016/j.euroecorev.2005.09.001 | peer-reviewed | Natural experiment (euro redenomination) separating price clustering from a nominal-scale artefact. |
| `ameijeirasalonso2018s11749018061` | Ameijeiras-Alonso et al. (2018) Mode testing, critical bandwidth and excess mass. *TEST* 28:900-919. | doi:10.1007/s11749-018-0611-5 | peer-reviewed | Comparative evaluation of the critical-bandwidth and excess-mass families and their calibrations; the entry point for choosing a mode test with a stated size. |
| `arxiv210107410` | Chung & Bellotti (2021) Evidence and Behaviour of Support and Resistance Levels in Financial Time Series. *arXiv*. | arXiv:2101.07410v1 | PREPRINT | Support/resistance level extraction and persistence testing on financial series. **Preprint tier - not settled evidence.** |

### 7.2 Branch 2 - state assignment (47 records)

| id | citation | persistent id | tier | role in the argument |
|---|---|---|---|---|
| `hurst1951taceat000651` | Hurst (1951) Long-Term Storage Capacity of Reservoirs. *Transactions of the American Society of Civil Engineers* 116:770-799. | doi:10.1061/taceat.0006518 | peer-reviewed | Original rescaled-range statistic. Primary source for the Hurst exponent. |
| `mandelbrot1969wr005i002p00` | Mandelbrot & Wallis (1969) Some long‐run properties of geophysical records. *Water Resources Research* 5:321-340. | doi:10.1029/wr005i002p00321 | peer-reviewed | R/S analysis for long-run dependence and its properties; the statistical formalisation of Hurst. |
| `lo19881141` | Lo & MacKinlay (1988) Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test. *Review of Financial Studies* 1:41-66. | doi:10.1093/rfs/1.1.41 | peer-reviewed | Variance-ratio statistic with homoskedastic and heteroskedasticity-robust standard errors; the reference null-distribution test for random walk versus trend/mean reversion. |
| `hamilton19891912559` | Hamilton (1989) A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle. *Econometrica* 57:357. | doi:10.2307/1912559 | peer-reviewed | Markov-switching autoregression: the canonical latent-state model with filtered state probabilities computable at time t. |
| `lo1989030440768990` | Lo & MacKinlay (1989) The size and power of the variance ratio test in finite samples. *Journal of Econometrics* 40:203-238. | doi:10.1016/0304-4076(89)90083-3 | peer-reviewed | Monte Carlo size and power of the variance-ratio test in finite samples - the small-sample evidence branch 2 requires before applying VR to an intraday window. |
| `hamilton1990030440769090` | Hamilton (1990) Analysis of time series subject to changes in regime. *Journal of Econometrics* 45:39-70. | doi:10.1016/0304-4076(90)90093-9 | peer-reviewed | EM estimation for regime-switching models; the algorithm behind every applied fit. |
| `petruccelli1990for398009010` | Petruccelli (1990) A comparison of tests for setar‐type non‐linearity in time series. *Journal of Forecasting* 9:25-36. | doi:10.1002/for.3980090104 | peer-reviewed | Relative small-sample performance of tests for SETAR-type nonlinearity - the threshold-model counterpart to the Markov-switching LR test problem. Admitted on re-screening this session. |
| `lo19912938368` | Lo (1991) Long-Term Memory in Stock Market Prices. *Econometrica* 59:1279. | doi:10.2307/2938368 | peer-reviewed | Modified R/S with a null distribution robust to short-range dependence; shows classical R/S rejects too often when short memory is present. |
| `hansen1992jae395007050` | Hansen (1992) The likelihood ratio test under nonstandard conditions: Testing the markov switching model of gnp. *Journal of Applied Econometrics* 7:S61-S82. | doi:10.1002/jae.3950070506 | peer-reviewed | The likelihood ratio test for the number of regimes under nonstandard conditions - nuisance parameters unidentified under the null, so the LR statistic is not chi-squared. The core inference obstacle for branch 2. |
| `chow1993030440769390` | Chow & Denning (1993) A simple multiple variance ratio test. *Journal of Econometrics* 58:385-401. | doi:10.1016/0304-4076(93)90051-6 | peer-reviewed | Multiple-horizon joint variance-ratio test controlling the family-wise error the single-horizon test ignores. |
| `kim1994030440769490` | Kim (1994) Dynamic linear models with Markov-switching. *Journal of Econometrics* 60:1-22. | doi:10.1016/0304-4076(94)90036-1 | peer-reviewed | The smoothing algorithm for state-space models with Markov switching. **Directly relevant to the agendas filtered-vs-smoothed lookahead concern: this paper is the source of the smoothed probabilities that published regime charts plot.** |
| `peng1994physreve4916` | Peng et al. (1994) Mosaic organization of DNA nucleotides. *Physical Review E* 49:1685-1689. | doi:10.1103/physreve.49.1685 | peer-reviewed | Detrended fluctuation analysis, the estimator family alternative to R/S named in branch 2. |
| `gray19960304405x9600` | Gray (1996) Modeling the conditional distribution of interest rates as a regime-switching process. *Journal of Financial Economics* 42:27-62. | doi:10.1016/0304-405x(96)00875-6 | peer-reviewed | Regime-switching conditional distribution with path-dependence collapsed; the first practical RS-GARCH. |
| `abry199818650984` | Abry & Veitch (1998) Wavelet analysis of long-range-dependent traffic. *IEEE Transactions on Information Theory* 44:2-15. | doi:10.1109/18.650984 | peer-reviewed | Wavelet-based estimator of the scaling exponent with an explicit variance and a goodness-of-fit test; the third estimator family in branch 2. |
| `garcia19982527399` | Garcia (1998) Asymptotic Null Distribution of the Likelihood Ratio Test in Markov Switching Models. *International Economic Review* 39:763. | doi:10.2307/2527399 | peer-reviewed | Asymptotic null distribution for the LR test in Markov-switching models; a usable critical-value source. |
| `rydn199806133217aidj` | Rydén et al. (1998) Stylized facts of daily return series and the hidden Markov model. *Journal of Applied Econometrics* 13:217-244. | doi:10.1002/(sici)1099-1255(199805/06)13:3<217::aid-jae476>3.0.co;2-v | peer-reviewed | Which stylized facts of daily returns an HMM does and does not reproduce. **Documents a specific failure: the HMM does not reproduce the slow decay of autocorrelation in absolute returns.** |
| `dacco1999sici1099131x` | Dacco & Satchell (1999) Why do regime-switching models forecast so badly?. *Journal of Forecasting* 18:1-16. | doi:10.1002/(sici)1099-131x(199901)18:1<1::aid-for685>3.0.co;2-b | peer-reviewed | **The branch-2 null.** Regime-switching models forecast poorly out of sample despite good in-sample fit; the failure autopsy the agenda needs before adopting the family. |
| `biernacki200034865189` | Biernacki et al. (2000) Assessing a mixture model for clustering with the integrated completed likelihood. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 22:719-725. | doi:10.1109/34.865189 | peer-reviewed | Integrated completed likelihood (ICL) - the entropy-penalised alternative to BIC for latent-class count selection. |
| `wright2000073500152000` | Wright (2000) Alternative Variance-Ratio Tests Using Ranks and Signs. *Journal of Business & Economic Statistics* 18:1-9. | doi:10.1080/07350015.2000.10524842 | peer-reviewed | Rank- and sign-based variance ratios with exact finite-sample distributions; removes the asymptotic approximation in short samples. |
| `kantelhardt2002s03784371020` | Kantelhardt et al. (2002) Multifractal detrended fluctuation analysis of nonstationary time series. *Physica A: Statistical Mechanics and its Applications* 316:87-114. | doi:10.1016/s0378-4371(02)01383-3 | peer-reviewed | Multifractal DFA - generalisation of DFA to a spectrum of scaling exponents. Admitted on re-screening this session. |
| `klaassen2002s00181010010` | Klaassen (2002) Improving GARCH volatility forecasts with regime-switching GARCH. *Empirical Economics* 27:363-394. | doi:10.1007/s001810100100 | peer-reviewed | Regime-switching GARCH with improved conditional-variance recursion. |
| `pagan2002jae664` | Pagan & Sossounov (2002) A simple framework for analysing bull and bear markets. *Journal of Applied Econometrics* 18:23-46. | doi:10.1002/jae.664 | peer-reviewed | Bull/bear dating algorithm with the DGP dependence of the resulting cycle characteristics analysed rather than assumed. The rule-based comparator to a fitted latent-state model. |
| `weron2002s03784371020` | Weron (2002) Estimating long-range dependence: finite sample properties and confidence intervals. *Physica A: Statistical Mechanics and its Applications* 312:285-299. | doi:10.1016/s0378-4371(02)00961-5 | peer-reviewed | Finite-sample properties and confidence intervals for R/S, DFA and periodogram estimators - the quantitative answer to branch 2s "below what window length is Hurst uninformative". |
| `psaradakis2003146798920030` | Psaradakis & Spagnolo (2003) ON THE DETERMINATION OF THE NUMBER OF REGIMES IN MARKOV‐SWITCHING AUTOREGRESSIVE MODELS. *Journal of Time Series Analysis* 24:237-252. | doi:10.1111/1467-9892.00305 | peer-reviewed | Properties of alternative procedures for determining the state dimension of a Markov-switching autoregression. |
| `haas2004nbh020` | Haas (2004) A New Approach to Markov-Switching GARCH Models. *Journal of Financial Econometrics* 2:493-530. | doi:10.1093/jjfinec/nbh020 | peer-reviewed | MS-GARCH formulation with tractable stationarity conditions and moment structure. |
| `lunde2004073500104000` | Lunde & Timmermann (2004) Duration Dependence in Stock Prices. *Journal of Business & Economic Statistics* 22:253-273. | doi:10.1198/073500104000000136 | peer-reviewed | Duration dependence in bull and bear phases - a direct test of whether regime hazard is constant, which is the geometric-duration assumption. |
| `marcucci2005155837081145` | Marcucci (2005) Forecasting Stock Market Volatility with Regime-Switching GARCH Models. *Studies in Nonlinear Dynamics & Econometrics* 9. | doi:10.2202/1558-3708.1145 | peer-reviewed | Regime-switching GARCH volatility forecasting comparison. |
| `bulla2006jcsda2006070` | Bulla & Bulla (2006) Stylized facts of financial time series and hidden semi-Markov models. *Computational Statistics & Data Analysis* 51:2192-2209. | doi:10.1016/j.csda.2006.07.021 | peer-reviewed | Hidden semi-Markov models for financial series; the direct response to the geometric-duration failure the agenda names. |
| `cho2007j14680262200` | Cho & White (2007) Testing for Regime Switching. *Econometrica* 75:1671-1720. | doi:10.1111/j.1468-0262.2007.00809.x | peer-reviewed | Quasi-likelihood-ratio test for regime switching with a tractable limiting distribution. |
| `chauvet2008073500107000` | Chauvet & Piger (2008) A Comparison of the Real-Time Performance of Business Cycle Dating Methods. *Journal of Business & Economic Statistics* 26:42-49. | doi:10.1198/073500107000000296 | peer-reviewed | Real-time (filtered, vintage-data) performance of business-cycle dating methods. **The cleanest available evidence on what a causal-time state assigner loses relative to a retrospective one.** |
| `kim2009jfrl20090400` | Kim (2009) Automatic variance ratio test under conditional heteroskedasticity. *Finance Research Letters* 6:179-185. | doi:10.1016/j.frl.2009.04.003 | peer-reviewed | Wild-bootstrap automatic variance ratio under conditional heteroskedasticity; the version applicable to volatility-clustered intraday data. |
| `barunik2010jphysa201005` | Barunik & Kristoufek (2010) On Hurst exponent estimation under heavy-tailed distributions. *Physica A: Statistical Mechanics and its Applications* 389:3844-3855. | doi:10.1016/j.physa.2010.05.025 | peer-reviewed | Behaviour of Hurst estimators under heavy tails; the failure mode that matters for returns. |
| `yu2010jartint20091` | Yu (2010) Hidden semi-Markov models. *Artificial Intelligence* 174:215-243. | doi:10.1016/j.artint.2009.11.011 | peer-reviewed | Survey of HSMM structure, inference and estimation; the reference for duration distributions and their computational cost. |
| `ang2012annurevfinan` | Ang & Timmermann (2012) Regime Changes and Financial Markets. *Annual Review of Financial Economics* 4:313-337. | doi:10.1146/annurev-financial-110311-101808 | peer-reviewed | Review of regime change in financial markets; the orientation source for the branch. |
| `anon2014ecta8609` | Carrasco et al. (2014) Optimal Test for Markov Switching Parameters. *Econometrica* 82:765-784. | doi:10.3982/ecta8609 | peer-reviewed | Optimal (asymptotically) test for Markov-switching parameters. The strongest available null-distribution result for "is there more than one state". |
| `chiappa20142200000054` | Chiappa (2014) Explicit-Duration Markov Switching Models. *Foundations and Trends® in Machine Learning* 7:803-886. | doi:10.1561/2200000054 | peer-reviewed (monograph, Foundations and Trends) | Explicit-duration Markov switching models: unified treatment of duration modelling and its inference cost. |
| `nystrup2016for2447` | Nystrup et al. (2016) Long Memory of Financial Time Series and Hidden Markov Models with Time‐Varying Parameters. *Journal of Forecasting* 36:989-1002. | doi:10.1002/for.2447 | peer-reviewed | Time-varying-parameter HMM; shows a two-state Gaussian HMM with adaptive parameters reproduces long memory, i.e. apparent long memory can be a regime artefact. |
| `pohle2017s13253017028` | Pohle et al. (2017) Selecting the Number of States in Hidden Markov Models: Pragmatic Solutions Illustrated Using Animal Movement. *Journal of Agricultural, Biological and Environmental Statistics* 22:270-293. | doi:10.1007/s13253-017-0283-8 | peer-reviewed | Selecting the number of HMM states: **documents that AIC and BIC routinely favour more states than are interpretable**, and argues against relying on them alone. The primary source for the agendas BIC-inconsistency question. |
| `ardia2018jijforecast2` | Ardia et al. (2018) Forecasting risk with Markov-switching GARCH models:A large-scale performance study. *International Journal of Forecasting* 34:733-747. | doi:10.1016/j.ijforecast.2018.05.004 | peer-reviewed | Large-scale performance study of MS-GARCH for risk forecasting - the out-of-sample evidence base for the family. |
| `gurrib2018bbs133201806` | Gurrib (2018) Performance of the Average Directional Index as a market timing tool for the most actively traded USD based currency pairs. *Banks and Bank Systems* 13:58-70. | doi:10.21511/bbs.13(3).2018.06 | peer-reviewed | The **only** peer-reviewed indexed record located that evaluates the Average Directional Index. Included solely as evidence for the folklore audit in section 8.5.2: it applies ADX without deriving it and without a null distribution. Its profitability claims are not assessed here. |
| `arxiv210700066` | Bilokon et al. (2021) Market regime classification with signatures. *arXiv*. | arXiv:2107.00066v1 | PREPRINT | Path-signature features for regime classification. **Preprint tier - not settled evidence.** |
| `xu2021flairsv34i11` | Xu & Liu (2021) A Regularized Vector Autoregressive Hidden Semi-Markov model, with Application to Multivariate Financial Data. *The International FLAIRS Conference Proceedings* 34. | doi:10.32473/flairs.v34i1.128424 | peer-reviewed (conference) | Regularized VAR-HSMM for multivariate financial data; states explicitly that the HMM geometric-duration assumption is too strong in practice. |
| `bucci2022jeconmod2022` | Bucci & Ciciretti (2022) Market regime detection via realized covariances. *Economic Modelling* 111:105832. | doi:10.1016/j.econmod.2022.105832 | peer-reviewed | Regime detection from realized covariances; unsupervised-learning comparison. |
| `arxiv230615835` | Issa & Horvath (2023) Non-parametric online market regime detection and regime clustering for multidimensional and path-dependent data structures. *arXiv*. | arXiv:2306.15835v1 | PREPRINT | Non-parametric online regime detection and clustering for path-dependent data. **Preprint tier - not settled evidence.** |
| `cont2024s13571024003` | Cont & Das (2024) Rough Volatility: Fact or Artefact?. *Sankhya B* 86:191-223. | doi:10.1007/s13571-024-00322-2 | peer-reviewed | Model-free demonstration that estimated roughness (H<0.5) can be an artefact of the estimation procedure rather than a property of the process. The cautionary case for all scaling-exponent state assignment. |
| `horvath2024jcf2024005` | Horvath et al. (2024) Clustering market regimes using the Wasserstein distance. *The Journal of Computational Finance*. | doi:10.21314/jcf.2024.005 | peer-reviewed | Wasserstein-distance clustering of market regimes; a distributional rather than parametric state assigner. |
| `luan2025dsfe2025016` | Luan & Hamp (2025) Automated regime classification in multidimensional time series data using sliced Wasserstein k-means clustering. *Data Science in Finance and Economics* 5:387-418. | doi:10.3934/dsfe.2025016 | peer-reviewed | Sliced-Wasserstein k-means regime classification for multidimensional series. |

### 7.3 Branch 3 - transition detection (14 records)

| id | citation | persistent id | tier | role in the argument |
|---|---|---|---|---|
| `wald19451177731118` | Wald (1945) Sequential Tests of Statistical Hypotheses. *The Annals of Mathematical Statistics* 16:117-186. | doi:10.1214/aoms/1177731118 | peer-reviewed | Sequential probability ratio test: the sequential-analysis foundation for online detection. |
| `wald19481177730197` | Wald & Wolfowitz (1948) Optimum Character of the Sequential Probability Ratio Test. *The Annals of Mathematical Statistics* 19:326-339. | doi:10.1214/aoms/1177730197 | peer-reviewed | Optimality of the SPRT - minimal expected sample size at given error probabilities. |
| `page19544112100` | PAGE (1954) CONTINUOUS INSPECTION SCHEMES. *Biometrika* 41:100-115. | doi:10.1093/biomet/41.1-2.100 | peer-reviewed | CUSUM: the original continuous-inspection scheme. Primary source for the frequentist online detector. |
| `hinkley1971583509` | HINKLEY (1971) Inference about the change-point from cumulative sum tests. *Biometrika* 58:509-523. | doi:10.1093/biomet/58.3.509 | peer-reviewed | Inference about the changepoint location from cumulative sums - the confidence interval on *when*, not just *whether*. |
| `lorden19711177693055` | Lorden (1971) Procedures for Reacting to a Change in Distribution. *The Annals of Mathematical Statistics* 42:1897-1908. | doi:10.1214/aoms/1177693055 | peer-reviewed | Asymptotic minimax detection delay subject to a false-alarm constraint. **The primary source for the detection-delay / average-run-length-to-false-alarm tradeoff the agenda calls the honest way to compare detectors.** |
| `moustakides19861176350164` | Moustakides (1986) Optimal Stopping Times for Detecting Changes in Distributions. *The Annals of Statistics* 14. | doi:10.1214/aos/1176350164 | peer-reviewed | Exact optimality of CUSUM under Lordens criterion; establishes what a detector can achieve. |
| `bai19982998540` | Bai & Perron (1998) Estimating and Testing Linear Models with Multiple Structural Changes. *Econometrica* 66:47. | doi:10.2307/2998540 | peer-reviewed | Estimation and testing of multiple structural changes with a stated asymptotic null - the retrospective upper bound on what an online detector could achieve. |
| `tzeleunglai199818737522` | Tze Leung Lai (1998) Information bounds and quick detection of parameter changes in stochastic systems. *IEEE Transactions on Information Theory* 44:2917-2929. | doi:10.1109/18.737522 | peer-reviewed | Information bounds for quick detection of parameter changes in stochastic systems; extends the delay/ARL theory beyond the i.i.d. case. |
| `bai2002jae659` | Bai & Perron (2002) Computation and analysis of multiple structural change models. *Journal of Applied Econometrics* 18:1-22. | doi:10.1002/jae.659 | peer-reviewed | Computation of the Bai-Perron estimator and its confidence intervals; the applied companion to the 1998 theory. |
| `arxiv07103742` | Prescott Adams & J. C. MacKay (2007) Bayesian Online Changepoint Detection. *arXiv*. | arXiv:0710.3742v1 | PREPRINT | Bayesian online changepoint detection: run-length posterior with a hazard function. **Preprint tier, never refereed, and still the canonical reference - a fact the agenda already flags and this review confirms.** |
| `fearnhead2007j14679868200` | Fearnhead & Liu (2007) On-Line Inference for Multiple Changepoint Problems. *Journal of the Royal Statistical Society Series B: Statistical Methodology* 69:589-605. | doi:10.1111/j.1467-9868.2007.00601.x | peer-reviewed | Exact online filtering for multiple changepoints with particle-resampling approximation. The peer-reviewed contemporary of BOCPD and the citable alternative to it. |
| `killick2012016214592012` | Killick et al. (2012) Optimal Detection of Changepoints With a Linear Computational Cost. *Journal of the American Statistical Association* 107:1590-1598. | doi:10.1080/01621459.2012.737745 | peer-reviewed | PELT: exact multiple-changepoint segmentation at linear cost, with the penalty acting as the model-selection device. |
| `truong2020jsigpro20191` | Truong et al. (2020) Selective review of offline change point detection methods. *Signal Processing* 167:107299. | doi:10.1016/j.sigpro.2019.107299 | peer-reviewed | Selective review of offline changepoint methods; the taxonomy that separates a mean shift from a variance shift, which is agenda branch 3s last open question. |
| `arxiv230204759` | Altamirano et al. (2023) Robust and Scalable Bayesian Online Changepoint Detection. *arXiv*. | arXiv:2302.04759v2 | PREPRINT | Robust and scalable BOCPD under outliers and model misspecification. **Preprint tier - not settled evidence.** |

### 7.4 Branch 4 - label-free validation (20 records)

| id | citation | persistent id | tier | role in the argument |
|---|---|---|---|---|
| `brock1992j15406261199` | BROCK et al. (1992) Simple Technical Trading Rules and the Stochastic Properties of Stock Returns. *The Journal of Finance* 47:1731-1764. | doi:10.1111/j.1540-6261.1992.tb04681.x | peer-reviewed | Bootstrap methodology for evaluating trading rules against null models fitted to the data. The methodological precursor to the reality check; cross-listed to branch 1 for its evidence on support/resistance rules. |
| `politis1994016214591994` | Politis & Romano (1994) The Stationary Bootstrap. *Journal of the American Statistical Association* 89:1303-1313. | doi:10.1080/01621459.1994.10476870 | peer-reviewed | Stationary bootstrap - resampling with geometric block lengths preserving stationarity. Primary source for dependent-data confidence intervals. |
| `andersen1997s09275398970` | Andersen & Bollerslev (1997) Intraday periodicity and volatility persistence in financial markets. *Journal of Empirical Finance* 4:115-158. | doi:10.1016/s0927-5398(97)00004-2 | peer-reviewed | Intraday volatility periodicity and its interaction with volatility persistence. **The agendas standing periodicity hazard rests on this record.** Cross-listed to branches 2 and 3. |
| `sullivan1999002210820016` | Sullivan et al. (1999) Data‐Snooping, Technical Trading Rule Performance, and the Bootstrap. *The Journal of Finance* 54:1647-1691. | doi:10.1111/0022-1082.00163 | peer-reviewed | Reality check applied to the full universe of technical trading rules; the worked precedent for treating a parameter grid as one family. |
| `white2000146802620015` | White (2000) A Reality Check for Data Snooping. *Econometrica* 68:1097-1126. | doi:10.1111/1468-0262.00152 | peer-reviewed | Reality check for data snooping: bootstrap null of no superior predictive ability over a full model family. |
| `lo2002fajv58n42453` | Lo (2002) The Statistics of Sharpe Ratios. *Financial Analysts Journal* 58:36-52. | doi:10.2469/faj.v58.n4.2453 | peer-reviewed | Asymptotic distribution of the Sharpe ratio under i.i.d. and under serial correlation; the interval a reported Sharpe requires. |
| `politis2004etc120028836` | Politis & White (2004) Automatic Block-Length Selection for the Dependent Bootstrap. *Econometric Reviews* 23:53-70. | doi:10.1081/etc-120028836 | peer-reviewed | Automatic (data-driven) block-length selection, removing the block-length magic number. |
| `hansen2005073500105000` | Hansen (2005) A Test for Superior Predictive Ability. *Journal of Business & Economic Statistics* 23:365-380. | doi:10.1198/073500105000000063 | peer-reviewed | Test for superior predictive ability; corrects the reality checks sensitivity to poor and irrelevant alternatives. |
| `romano2005j14680262200` | Romano & Wolf (2005) Stepwise Multiple Testing as Formalized Data Snooping. *Econometrica* 73:1237-1282. | doi:10.1111/j.1468-0262.2005.00615.x | peer-reviewed | Stepwise multiple testing with family-wise error control - identifies *which* models beat the benchmark, not merely whether any does. |
| `ledoit2008jjempfin2008` | Ledoit & Wolf (2008) Robust performance hypothesis testing with the Sharpe ratio. *Journal of Empirical Finance* 15:850-859. | doi:10.1016/j.jempfin.2008.03.002 | peer-reviewed | Studentized time-series bootstrap for the difference of two Sharpe ratios - the correct test for pairwise strategy comparison. |
| `patton2009074749308024` | Patton et al. (2009) Correction to “Automatic Block-Length Selection for the Dependent Bootstrap” by D. Politis and H. White. *Econometric Reviews* 28:372-375. | doi:10.1080/07474930802459016 | peer-reviewed | Correction to the 2004 block-length formula. **Must be applied with it; the uncorrected formula is wrong.** |
| `hsu2010jjempfin2010` | Hsu et al. (2010) Testing the predictive ability of technical analysis using a new stepwise test without data snooping bias. *Journal of Empirical Finance* 17:471-484. | doi:10.1016/j.jempfin.2010.01.001 | peer-reviewed | Stepwise SPA applied to technical analysis; the current state of the data-snooping-corrected evidence. |
| `anon2011ecta5771` | Hansen et al. (2011) The Model Confidence Set. *Econometrica* 79:453-497. | doi:10.3982/ecta5771 | peer-reviewed | Model confidence set: a set of models that contains the best with stated probability. The right object when the goal is state-model selection rather than a single winner. |
| `boudt2011jjempfin2010` | Boudt et al. (2011) Robust estimation of intraweek periodicity in volatility and jump detection. *Journal of Empirical Finance* 18:353-367. | doi:10.1016/j.jempfin.2010.11.005 | peer-reviewed | Robust (outlier-resistant) estimation of the intraweek periodicity factor and jump detection conditional on it - the deseasonalization estimator, not merely the phenomenon. |
| `bergmeir2012jins20111202` | Bergmeir & Benítez (2012) On the use of cross-validation for time series predictor evaluation. *Information Sciences* 191:192-213. | doi:10.1016/j.ins.2011.12.028 | peer-reviewed | Empirical study of cross-validation for time-series predictor evaluation. |
| `bailey2014jpm201440509` | Bailey & López de Prado (2014) The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality. *The Journal of Portfolio Management* 40:94-107. | doi:10.3905/jpm.2014.40.5.094 | peer-reviewed | Deflated Sharpe ratio: Sharpe significance adjusted for the number of trials, non-normality and sample length. |
| `bailey2014noti1105` | Bailey et al. (2014) Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance. *Notices of the American Mathematical Society* 61:458. | doi:10.1090/noti1105 | peer-reviewed | Minimum backtest length as a function of the number of trials; the quantitative statement of how quickly a grid search exhausts a sample. |
| `bailey2016jcf2016322` | Bailey et al. (2016) The probability of backtest overfitting. *The Journal of Computational Finance*. | doi:10.21314/jcf.2016.322 | peer-reviewed | Probability of backtest overfitting via combinatorially symmetric cross-validation - the closest peer-reviewed source to the agendas combinatorial purged CV. |
| `bergmeir2018jcsda2017110` | Bergmeir et al. (2018) A note on the validity of cross-validation for evaluating autoregressive time series prediction. *Computational Statistics & Data Analysis* 120:70-83. | doi:10.1016/j.csda.2017.11.003 | peer-reviewed | Conditions under which k-fold CV is valid for autoregressive models - the theoretical statement of when block/purged designs are and are not necessary. |
| `lpezdeprado2018jpm201844612` | López de Prado (2018) The 10 Reasons Most Machine Learning Funds Fail. *The Journal of Portfolio Management* 44:120-133. | doi:10.3905/jpm.2018.44.6.120 | peer-reviewed | Catalogue of failure modes in financial ML including leakage and improper cross-validation. **The purging and embargo prescription itself is presented here without derivation; see section 8.4.2.** |

### 7.5 Preprint-tier records (charter evidence-tier flag)

Five of the 96 included records are unrefereed preprints. Each is flagged here so that no downstream artifact can cite one without seeing its tier.

| id | citation | persistent id | branch | why it is nevertheless included |
|---|---|---|---|---|
| `arxiv210107410` | Chung & Bellotti (2021) Evidence and Behaviour of Support and Resistance Levels in Financial Time Series. *arXiv*. | arXiv:2101.07410v1 | 1 | The only located record testing support/resistance level behaviour with an explicit statistical procedure rather than by illustration. No refereed version located. |
| `arxiv210700066` | Bilokon et al. (2021) Market regime classification with signatures. *arXiv*. | arXiv:2107.00066v1 | 2 | Signature-based regime classification; no refereed version located. Included as evidence of the method family existing, not as a validated result. |
| `arxiv230615835` | Issa & Horvath (2023) Non-parametric online market regime detection and regime clustering for multidimensional and path-dependent data structures. *arXiv*. | arXiv:2306.15835v1 | 2 | Online non-parametric regime detection; no refereed version located. Same status as above. |
| `arxiv07103742` | Prescott Adams & J. C. MacKay (2007) Bayesian Online Changepoint Detection. *arXiv*. | arXiv:0710.3742v1 | 3 | It is the canonical and, as far as this search could establish, the **only** source for Bayesian online changepoint detection. No refereed version was located. Branch 3 cannot be written without it, and that dependence is itself a finding (section 8.3.1). |
| `arxiv230204759` | Altamirano et al. (2023) Robust and Scalable Bayesian Online Changepoint Detection. *arXiv*. | arXiv:2302.04759v2 | 3 | Robustified BOCPD; included as the documented failure-mode source for the canonical preprint above. No refereed version located. |

**Per-branch counts.** Branch 1: 15. Branch 2: 47. Branch 3: 14. Branch 4: 20. Total 96.
Cross-listed records are counted once, under their primary branch: `brock1992j15406261199` (4, also 1), `andersen1997s09275398970` (4, also 2 and 3),
`kim1994030440769490` (2, also 4 for the filtered-vs-smoothed leakage question).

## 8. Synthesis

### 8.0 How to read this section

Each method gets the three fields the objective specifies: **(a)** null
distribution or derivation, **(b)** primary source with identifier, **(c)**
documented failure modes and small-sample behaviour. Every substantive claim
carries its evidence basis in brackets, because full texts were not retrieved for
this corpus (section 10.3):

- `[abstract]` - the claim is supported by the record's abstract, retrieved from
  Crossref or from the OpenAlex inverted index and stored at
  `search_logs/regime-classification/gap-openalex-42-abstracts.json`.
- `[title]` - supported only by the record's title. Titles such as *The size and
  power of the variance ratio test in finite samples* assert the existence of the
  evidence but not its direction; where direction is claimed from a title alone
  that is stated.
- `[not-verified]` - the claim describes what the method is generally understood
  to do, and **was not confirmed against any retrieved text**. These are the
  claims a downstream artifact must not cite without reading the source.

Evidence tier (CLAUDE.md hierarchy) is recorded per record in section 7 and is
not repeated per sentence; every record in this synthesis is tier-1
(peer-reviewed literature) except the five marked **PREPRINT**.

### 8.1 Branch 1 - level estimation

#### 8.1.1 The question the agenda asked: does a significance test for a mode already exist?

**Yes. It exists, it is roughly forty-five years old, and there are three
independent families of it.** This is the most consequential finding in the
review, because the agenda's branch-1 falsification test - decide whether
estimated levels are distinguishable from those of a calibrated bounded random
walk - is exactly a mode-significance problem, and the agenda treats it as
something that may have to be invented.

**Family 1: critical bandwidth.**

- (a) Silverman (1981) observes that the number of modes of a Gaussian kernel
  density estimate is monotone decreasing in the bandwidth, so the smallest
  bandwidth consistent with at most *k* modes - the *critical bandwidth* - is a
  well-defined statistic for the hypothesis "the density has at most *k* modes"
  `[title]`. Silverman (1983) supplies the calibration that turns the statistic
  into a test, by bootstrapping from the density estimate at the critical
  bandwidth `[not-verified: title asserts "some properties of a test", the
  bootstrap-calibration mechanism was not confirmed from retrieved text]`.
- (b) doi:10.1111/j.2517-6161.1981.tb01155.x; doi:10.1017/cbo9780511662430.015.
- (c) Mammen, Marron & Fisher (1992) establish the asymptotics of the procedure
  `[title]`; Fischer, Mammen & Marron (1994) compare tests for multimodality in
  finite samples `[title]`; Ameijeiras-Alonso, Crujeiras & Rodriguez-Casal (2018)
  evaluate critical-bandwidth against excess-mass calibrations `[title]`. **The
  direction of those results - specifically whether the Silverman test is
  conservative and by how much - was not established from any text retrieved by
  this search and must not be asserted downstream.** A widely cited calibration
  correction (Hall & York, *Statistica Sinica* 2001) could not be resolved to a
  persistent identifier in Crossref, OpenAlex or Semantic Scholar and is
  therefore **not** in the corpus; this is recorded as verification gap VG-3 in
  section 10.

**Family 2: the dip test.**

- (a) Hartigan & Hartigan (1985): "The dip test measures multimodality in a
  sample by the maximum difference, over all sample points, between the empirical
  distribution function, and the unimodal distribution function that minimizes
  that maximum difference" `[abstract, verbatim]`. The uniform distribution is
  the asymptotically least-favourable unimodal distribution, and the statistic's
  distribution is obtained both asymptotically and empirically under sampling
  from the uniform `[abstract]`. **This is a bandwidth-free significance test for
  unimodality with a stated null** - the property the agenda needs, obtained
  without choosing a smoothing parameter.
- (b) doi:10.1214/aos/1176346577.
- (c) Because the null is *least favourable* rather than the true unimodal
  density, the test is by construction not exact against an arbitrary unimodal
  alternative `[abstract, by inference from the least-favourable construction]`.
  Its power against closely spaced modes was not established from retrieved text
  `[not-verified]`.

**Family 3: excess mass.**

- (a) Müller & Sawitzki (1991): the excess-mass functional "measures excessive
  empirical mass in comparison with multiples of uniform distribution", and "by
  the excess mass approach we separate the investigation about the number of
  modes from questions concerning their location" `[abstract, verbatim]`. The
  functional is estimable at a root-*n* rate, the asymptotic behaviour of the
  estimators is studied, and "tests for multimodality based on the excess mass
  are derived" `[abstract]`.
- (b) doi:10.1080/01621459.1991.10475103.
- (c) A published corrigendum exists (doi:10.2307/2291192, excluded as E2); any
  implementation must be checked against it. Mammen, Marron & Fisher (1992) and
  Ameijeiras-Alonso et al. (2018) cover the family's asymptotics and its
  comparison with critical bandwidth `[title]`.

**Practical consequence for the agenda.** The separation Müller & Sawitzki make
explicit - *how many modes* is a different question from *where they are* - maps
directly onto the agenda's distinction between establishing that levels exist and
estimating [L, U]. The count question has a test with a stated null. The location
question needs section 8.1.3.

#### 8.1.2 Bandwidth selection

- (a) Sheather & Jones (1991) select the bandwidth by approximately minimising an
  estimate of mean integrated squared error, with "the reintroduction of a
  non-stochastic term which was previously" omitted as the key to its performance
  `[abstract]`. It is a derived plug-in rule, not a convention.
- (b) doi:10.1111/j.2517-6161.1991.tb01857.x.
- (c) The abstract's own performance claim is scoped to *smooth* densities:
  "reliably good performance for smooth densities in simulations" `[abstract]`.
  Nothing in the corpus establishes its behaviour on a price distribution with
  atoms at round numbers, which is precisely the shape the price-clustering
  literature in section 8.1.4 predicts. **This is an open failure mode, not a
  settled one.**
- Alternative: Chaudhuri & Marron (1999) sidestep the single-bandwidth choice
  entirely. SiZer asks "which observed features are 'really there,' as opposed to
  being spurious sampling artifacts" and answers it by assessing significant zero
  crossings of derivatives across location *and* bandwidth simultaneously
  `[abstract]`. For the agenda this is attractive because it removes a tuning
  parameter that would otherwise need empirical justification, and because its
  output is a significance map rather than a point estimate
  (doi:10.1080/01621459.1999.10474186).

#### 8.1.3 Confidence intervals on mode location

- (a)/(b) Romano (1988), *Bootstrapping the mode*,
  doi:10.1007/BF00053066 `[title]`.
- (c) No abstract was retrievable from Crossref or OpenAlex. **The specific claim
  that the naive bootstrap fails for the mode without bandwidth adjustment was
  not verified from retrieved text and is marked `[not-verified]`.** It is
  load-bearing for the agenda's requirement that "a level without an interval is
  a drawing", and should be read in the original before any implementation.

#### 8.1.4 Do price levels exist, empirically?

The corpus supports a qualified yes, with a mechanism.

- Niederhoffer (1965), doi:10.1287/opre.13.2.258 - earliest located documentation
  of clustering in stock prices `[title]`.
- Donaldson & Kim (1993), doi:10.2307/2331416: the DJIA's "rise and fall is
  indeed restrained by 'support' and 'resistance' levels at multiples of 100"
  and, "having broken through a 100-level, the DJIA then moves by more than
  otherwise warranted"; significance established by "a Monte Carlo study and
  comparisons with other indices" `[abstract, verbatim]`. **This is a level test
  with an explicit simulated null** - a second template for the agenda's branch-1
  falsification, on real data rather than synthetic.
- Osler (2003), doi:10.1111/1540-6261.00588: take-profit orders cluster at round
  numbers and stop-loss orders cluster just beyond them, which supplies a
  mechanism for both the restraint and the post-break acceleration `[abstract]`.
  This directly addresses the agenda's book-derived-versus-price-derived
  question: the two are not independent, because the book *is* where the price
  effect comes from.
- Sonnemans (2006), doi:10.1016/j.euroecorev.2005.09.001 - guilder-to-euro
  redenomination as a natural experiment separating clustering from nominal-scale
  artefact `[title]`.
- Chung & Bellotti (2021), arXiv:2101.07410 - **PREPRINT tier; not settled.**

**Caution the corpus itself imposes.** Donaldson & Kim conclude their effect
"does not necessarily suggest that the market is inefficient" `[abstract]`. The
existence of a level is therefore established at tier 1; nothing in the corpus
establishes that a level is *exploitable*, and the review does not address that
question.

#### 8.1.5 What branch 1 still lacks after this search

1. No source in the corpus derives or empirically selects the **70% value-area
   convention** of Market Profile. See section 8.5.4 - this is a confirmed
   negative.
2. No source in the corpus addresses **level persistence or half-life** as a
   survival problem. The five purposeful web searches did not surface one, and no
   Crossref or arXiv query targeted it. Recorded as recall gap RG-2 (section
   10.2), not as a negative finding.
3. No source in the corpus addresses **DBSCAN or agglomerative clustering of
   swing extrema** for level construction. The agenda names Ester et al. (1996);
   no query targeted it. Recall gap RG-3.

### 8.2 Branch 2 - state assignment

#### 8.2.1 Kaufman Efficiency Ratio

**Negative finding.** No primary source and no derivation could be located. See
section 8.5.1.

#### 8.2.2 Variance ratio - the branch's strongest null

- (a) Lo & MacKinlay (1988) test the random-walk hypothesis "by comparing
  variance estimators derived from data sampled at different frequencies"
  `[abstract]`. A stated asymptotic null, in homoskedastic and
  heteroskedasticity-robust forms.
- (b) doi:10.1093/rfs/1.1.41.
- (c) Documented, extensively, and this is the deepest small-sample evidence base
  anywhere in the corpus:
  - Lo & MacKinlay (1989), doi:10.1016/0304-4076(89)90083-3, *The size and power
    of the variance ratio test in finite samples* - a Monte Carlo investigation
    `[title]`. Direction not established from retrieved text; the title
    guarantees the evidence exists but not what it says `[not-verified]`.
  - Chow & Denning (1993), doi:10.1016/0304-4076(93)90051-6 - single-horizon VR
    tests do not control the family-wise error rate across horizons; the joint
    statistic does `[title]`.
  - Wright (2000), doi:10.1080/07350015.2000.10524842: rank- and sign-based
    variance ratios "can be exact", "unlike conventional variance-ratio tests",
    and in Monte Carlo "can also be more powerful" `[abstract, verbatim]`.
    **This is the direct answer to the agenda's concern about VR size properties
    in short intraday windows: use the exact rank/sign version.**
  - Kim (2009), doi:10.1016/j.frl.2009.04.003 - wild-bootstrap automatic VR under
    conditional heteroskedasticity `[title]`; the version applicable to
    volatility-clustered data.

**Assessment.** Of every candidate state assigner in the agenda, the variance
ratio has the best-documented null and the best-documented small-sample
behaviour. If a single trend-versus-range statistic must be chosen on
distributional grounds alone, the corpus points at Wright's rank/sign VR.

#### 8.2.3 Hurst exponent and fractal dimension

- (a)/(b) Hurst (1951), doi:10.1061/TACEAT.0006518 - the rescaled range arises
  from a reservoir-storage problem, not from a distributional derivation; the
  abstract describes computing "cumulative sums of the departures of the annual
  totals from the mean" and taking "the range from the maximum to the minimum"
  `[abstract]`. **There is no null distribution in the original.**
- (c) The corpus is unusually blunt about this method's failure modes:
  - Mandelbrot & Wallis (1969), doi:10.1029/WR005i002p00321, state in the
    abstract that "Hurst's original claims must be tightened and hedged, and his
    estimates of H must be discarded, but his general idea will be shown to be
    correct" `[abstract, verbatim]`. A primary source disowning the original
    estimator is about as clear a documented failure mode as this review found.
  - Lo (1991), doi:10.2307/2938368, supplies the missing null: "A test for
    long-run memory that is robust to short-range dependence is developed... the
    relevant asymptotic sampling theory is derived via functional central limit
    theory." Applying it, "there is no evidence of long-range dependence in any
    of the indexes over any sample period or sub-period **once short-term
    autocorrelations are taken into account**" `[abstract, verbatim, emphasis
    added`]. **Classical R/S mistakes short memory for long memory. On financial
    data specifically, Lo's corrected test finds nothing.** Any use of a raw
    Hurst exponent as a trend/range state variable must answer this record.
  - Weron (2002), doi:10.1016/S0378-4371(02)00961-5, *Estimating long-range
    dependence: finite sample properties and confidence intervals* `[title]` -
    the source that would quantify the agenda's "below what window length is
    Hurst uninformative". No abstract retrievable; **direction not verified**.
  - Barunik & Kristoufek (2010), doi:10.1016/j.physa.2010.05.025 - Hurst
    estimation under heavy-tailed distributions `[title]`, i.e. under the
    distribution returns actually have.
  - Cont & Das (2024), doi:10.1007/s13571-024-00322-2, is the strongest caution:
    a model-free non-parametric roughness estimator with "good finite sample
    performance" on simulated fractional processes, applied to the claim that
    volatility is rough `[abstract]`. The title poses the question as *fact or
    artefact*. **The corpus therefore contains a live, recent dispute about
    whether an estimated scaling exponent measures the process or the estimator.**
- Alternative estimators in the corpus, each with its own derivation: DFA
  (Peng et al. 1994, doi:10.1103/PhysRevE.49.1685), multifractal DFA
  (Kantelhardt et al. 2002, doi:10.1016/s0378-4371(02)01383-3), and the wavelet
  estimator of Abry & Veitch (1998), doi:10.1109/18.650984, which is "shown to be
  unbiased under very general conditions, and efficient under Gaussian
  assumptions", and "highly robust against the presence of deterministic trends"
  `[abstract]`. **Of the four estimator families, only the wavelet estimator
  comes with an explicit unbiasedness and efficiency claim in its own abstract.**

#### 8.2.4 Markov-switching

- (a) Hamilton (1989), doi:10.2307/1912559 - the latent-state model whose
  *filtered* state probability at time *t* uses only information through *t*,
  which is what the agenda's causal-time constraint requires `[title]`.
  Estimation by EM: Hamilton (1990), doi:10.1016/0304-4076(90)90093-9 `[title]`.
- (b) As above.
- (c) **The null distribution for "is there more than one state" is the central
  difficulty, and the corpus documents it precisely.** Hansen (1992),
  doi:10.1002/jae.3950070506: "By viewing the likelihood as a function of the
  unknown parameters, empirical process theory enables us to bound the asymptotic
  distribution of standardized likelihood ratio statistics, even when
  conventional regularity conditions (such as unidentified nuisance parameters
  and identically zero scores) are violated" - and, applied to Hamilton's own
  GNP model, "the standardized likelihood ratio test **is unable to reject** the
  hypothesis of an AR(4) in favour of the Markov switching model" `[abstract,
  verbatim, emphasis added]`.

  This is a substantive negative result about the canonical model, in the corpus,
  at tier 1. It is followed by three attempts to supply a usable null: Garcia
  (1998), doi:10.2307/2527399 `[title]`; Cho & White (2007),
  doi:10.1111/j.1468-0262.2007.00809.x `[title]`; and Carrasco, Hu & Ploberger
  (2014), doi:10.3982/ECTA8609, an optimal test `[title]`. **The corpus does not
  settle which of these to use**, and this review does not adjudicate it.
- Volatility extensions with derivations: Gray (1996)
  doi:10.1016/0304-405x(96)00875-6; Klaassen (2002) doi:10.1007/s001810100100;
  Haas et al. (2004) doi:10.1093/jjfinec/nbh020; large-scale evaluation in Ardia
  et al. (2018) doi:10.1016/j.ijforecast.2018.05.004; comparison in Marcucci
  (2005) doi:10.2202/1558-3708.1145. All `[title]`.

#### 8.2.5 How many states? The agenda's BIC question, answered

- Pohle, Langrock, van Beest & Schmidt (2017), doi:10.1007/s13253-017-0283-8,
  *Selecting the Number of States in Hidden Markov Models: Pragmatic Solutions
  Illustrated Using Animal Movement*. No abstract was retrievable from Crossref
  or OpenAlex and the Springer page is paywalled (VG-4); **the claim that AIC and
  BIC systematically over-select states is therefore `[title]` plus
  `[not-verified]` and must be read in the original before it is relied on.**
- Psaradakis & Spagnolo (2003), doi:10.1111/1467-9892.00305, is retrievable and
  is the citable source: they "investigate the properties of alternative
  procedures that can be used to determine the state dimension of a
  Markov-switching autoregressive model", including "procedures that exploit the
  ARMA representation which Markov-switching processes admit, as well as
  procedures that are based on optimization of complexity-penalized likelihood
  measures" `[abstract, verbatim]`. The abstract as retrieved is truncated before
  the conclusion, so **the direction of their finding is not established here**.
- Biernacki, Celeux & Govaert (2000), doi:10.1109/34.865189 - integrated
  completed likelihood, the entropy-penalised criterion designed for the case
  where the latent classes, not the density, are the object of interest `[title]`.
  This is the criterion whose *motivation* matches the agenda's use case most
  closely.

#### 8.2.6 State duration: the geometric assumption is the model's weakest joint

The agenda's objection - that an HMM imposes geometric state durations while
regime duration is the quantity of interest - is corroborated in the corpus, and
one record states it in nearly the agenda's own words.

- Xu & Liu (2021), doi:10.32473/flairs.v34i1.128424: "HMM's implicit assumption
  that the state duration follows a geometric distribution is too strong to hold
  in practice" `[abstract, verbatim]`.
- Remedies with derivations: Bulla & Bulla (2006),
  doi:10.1016/j.csda.2006.07.021 `[title]`; the HSMM survey of Yu (2010),
  doi:10.1016/j.artint.2009.11.011 `[title]`; Chiappa (2014),
  doi:10.1561/2200000054, on explicit-duration switching models, which notes that
  arbitrary duration distributions are purchasable but that the additional
  variables "allow to define duration distributions of any form, but also to
  impose comp[utational constraints]" `[abstract, truncated in source]`.
- **Empirical evidence that the geometric assumption is wrong on this data**:
  Lunde & Timmermann (2004), doi:10.1198/073500104000000136, model "the
  (instantaneous) probability that a bull or bear market terminates as a function
  of its age", and report that "a random walk model is rejected both for bull and
  bear markets", while a GARCH model "is also found to be inconsistent with the
  very long bull markets observed in the data" `[abstract, verbatim]`. Duration
  dependence is present and is not captured by the obvious alternatives.

#### 8.2.7 Filtered versus smoothed probabilities - the lookahead audit

The agenda asks for a catalogue of published results that plot *smoothed* state
probabilities, which condition on the full sample and are therefore not available
at time *t*. This search did not produce that catalogue, and the corpus instead
supplies the two records that make it constructible:

- Kim (1994), doi:10.1016/0304-4076(94)90036-1 - the smoothing algorithm itself
  `[title]`. Every smoothed regime chart in the applied literature traces back
  here; identifying the affected results means tracking forward citations of this
  record, which is a citation-search task this review did **not** perform (RG-1,
  section 10.2).
- Chauvet & Piger (2008), doi:10.1198/073500107000000296, is the corpus's only
  direct measurement of the filtered/real-time penalty: using "a new 'real-time'
  dataset of coincident monthly variables", both a non-parametric algorithm and a
  Markov-switching dynamic-factor model "would have accurately identified the
  NBER business cycle chronology had they been in use over the past 30 years",
  and both "yielded significant improvement over the NBER in the speed with which
  business cycle troughs were identified" `[abstract, verbatim]`.
  **This is a positive result for causal-time state assignment, on vintage data,
  at tier 1** - and it is the single most encouraging record in the corpus for
  the agenda's central question. Its scope is monthly macroeconomic data; nothing
  in the corpus transfers it to intraday price data, and it must not be carried
  across (charter: measurement scope travels with the ranking).

#### 8.2.8 Rule-based dating as the comparator

- Pagan & Sossounov (2002), doi:10.1002/jae.664: they begin "with a definition of
  bull and bear markets and use an algorithm based on it to sort a given time
  series of equity prices into periods", then study the rule analytically and
  show "that bull and bear market characteristics depend upo[n]" the data
  generating process `[abstract, verbatim, truncated in source]`. **The value for
  the agenda is precisely the analytical step: a dating rule's output statistics
  are a function of the DGP, so the rule cannot be validated by inspecting its
  output.** That is the same trap the agenda's eye-labelling prohibition guards
  against, stated for algorithms.

#### 8.2.9 The branch-2 null

Dacco & Satchell (1999), doi:10.1002/(SICI)1099-131X(199901)18:1<1::AID-FOR685>3.0.CO;2-B,
is the record that most directly threatens branch 2 and is quoted at length
because of it:

> "Most non-linear techniques give good in-sample fits to exchange rate data but
> are usually outperformed by random walks or random walks with drift when used
> for out-of-sample forecasting. In the case of regime-switching models it is
> possible to understand why forecasts based on the true model can have higher
> mean squared error than those of a random walk or random walk with drift... **It
> requires only a small misclassification, when forecasting which regime the
> world will be in, to lose any advantage from knowing the correct model
> specification.**" `[abstract, verbatim, emphasis added]`

The mechanism is stated analytically for a segmented trend model `[abstract]`.
For the agenda this is the sharpest available statement of the cost structure:
the state assignment does not merely need to be right on average, it needs a
misclassification rate low enough that the correct specification still pays. No
record in the corpus quantifies that threshold for intraday equity or futures
data.

Corroborating in the opposite direction: Nystrup, Madsen & Lindström (2016),
doi:10.1002/for.2447, show that "a two-state Gaussian hidden Markov model with
time-varying parameters is able to reproduce the long memory of squared daily
returns that was previously believed to be the most difficult fact to reproduce
with a hidden Markov model" `[abstract, verbatim]`, and that this also improves
one-step density forecasts. Read together with Rydén, Teräsvirta & Åsbrink
(1998), doi:10.1002/(SICI)1099-1255(199805/06)13:3<217::AID-JAE476>3.0.CO;2-V,
whose abstract shows "a mixture of normal variables with zero mean can generate
series with most of the properties Granger and Ding singled out" `[abstract]`,
the corpus's position is: **an HMM can reproduce the stylized facts, and can
still fail to forecast.** These are not in conflict and the review does not
average them.

### 8.3 Branch 3 - the transition event

#### 8.3.1 Bayesian online changepoint detection rests on an unrefereed preprint

- (a) Adams & MacKay (2007) maintain a posterior over the *run length* since the
  last changepoint, propagated recursively with a hazard function `[title]`.
- (b) **arXiv:0710.3742. This is the primary source, it is a preprint, it was
  never refereed, and no journal version was located by any query in this
  review.** The agenda already flagged this; the review confirms it. Under the
  charter's evidence-tier rule the method is `preprint` tier and **no artifact
  may treat it as settled**.
- (c) Altamirano, Briol & Knoblauch (2023), arXiv:2302.04759, is the corpus's
  documented failure-mode source - robustness of BOCPD under outliers and
  misspecification - and is **also a preprint**. Branch 3's headline method
  therefore has both its derivation and its known-failure literature at tier
  `preprint`.

**The peer-reviewed alternative exists and is contemporaneous.** Fearnhead & Liu
(2007), doi:10.1111/j.1467-9868.2007.00601.x: "We propose an on-line algorithm
for exact filtering of multiple changepoint problems. This algorithm enables
simulation from the true joint posterior distribution of the number and position
of the changepoints for a class of changepoint models. The computational cost of
this exact algorithm is quadratic in the number of observations. We further show
how resampling ideas from particle filters can be used to reduce the
computational cost to linear in the number of observations, **at the expense of
introducing sm[all approximation error]**" `[abstract, verbatim, truncated in
source; emphasis added]`. This is an online Bayesian multiple-changepoint method
with an exact posterior, published in *JRSS-B*. **Recommendation for the agenda:
where BOCPD is used, Fearnhead & Liu should be run alongside it, so that no
result depends on a preprint alone.**

#### 8.3.2 Frequentist online detectors, all with derivations

- **CUSUM.** Page (1954), doi:10.1093/biomet/41.1-2.100 `[title]`; no abstract
  retrievable. Hinkley (1971), doi:10.1093/biomet/58.3.509, supplies inference
  about the changepoint *location* from cumulative sums, i.e. an interval on
  *when* rather than only a decision about *whether* `[title]`.
- **SPRT.** Wald (1945), doi:10.1214/aoms/1177731118 `[title]`; optimality in
  Wald & Wolfowitz (1948), doi:10.1214/aoms/1177730197 `[title]`.
- **Page-Hinkley.** The corpus contains both components (Page 1954, Hinkley 1971)
  but **no record under the composite name "Page-Hinkley test"**. The composite
  appears to be a later naming convention in the data-stream literature; no
  primary source for it under that name was located, and none is asserted here.
  Recorded as verification gap VG-5.

#### 8.3.3 Detection delay versus average run length to false alarm

This is the agenda's "honest way to compare detectors", and the corpus contains
its full theoretical chain.

- Lorden (1971), doi:10.1214/aoms/1177693055. The published abstract is one
  sentence - "A problem of optimal stopping is formulated and simple rules are
  proposed which are asymptotically optimal in an appropriate sense" `[abstract,
  verbatim]` - so the specific minimax worst-case-delay-subject-to-false-alarm
  criterion that carries Lorden's name is `[not-verified]` from retrieved text.
  The record is nonetheless the correct primary citation `[title]`.
- Moustakides (1986), doi:10.1214/aos/1176350164, closes the argument and its
  abstract is unambiguous: "It is shown that Page's stopping time is optimal for
  the detection of changes in distributions, in a well defined sense. This work
  is a generalization of an existing result where it was shown that Page's
  stopping time is optimal asymptotically" `[abstract, verbatim]`. **CUSUM is not
  a heuristic; it is exactly optimal under a stated criterion.**
- Lai (1998), doi:10.1109/18.737522, extends the theory beyond simple models:
  "By using information-theoretic bounds and sequential hypothesis testing theory,
  this paper provides a new approach to optimal detection of abrupt changes in
  stochastic systems... it leads to detection rules which have manageable
  computational complexity for on-line implementation and yet are nearly optimal"
  `[abstract, verbatim]`. Note the abstract's own framing: it "suggests
  alternative performance criteria which are more tractable and more appropriate
  for general stochastic systems" - i.e. **the delay/ARL criterion itself is not
  unique, and the choice of criterion is a modelling decision the agenda will
  have to make explicitly.**

#### 8.3.4 The retrospective upper bound

- Bai & Perron (1998), doi:10.2307/2998540: "This paper develops the statistical
  theory for testing and estimating multiple change points in regression models.
  The rate of convergence and limiting distribution for the estimated parameters
  are obtained. Several test statistics are proposed to determine the existence
  as well as the number of change points... the models allow for serially
  correlated disturbances (mixingales)" `[abstract, verbatim]`. A stated
  asymptotic null for both existence and number, with serial correlation
  permitted - which is the relevant case here. Computation and confidence
  intervals in Bai & Perron (2002), doi:10.1002/jae.659 `[title]`.
- Killick, Fearnhead & Eckley (2012), doi:10.1080/01621459.2012.737745, is the
  computational enabler: exact minimisation of a segmentation cost, including
  "penalized likelihood and minimum description length", at linear rather than
  quadratic cost `[abstract]`. **The penalty is the model-selection device, and
  choosing it is the same magic-number problem the agenda flags elsewhere; the
  abstract does not resolve it.**
- Truong, Oudre & Vayatis (2020), doi:10.1016/j.sigpro.2019.107299, is the
  taxonomy `[title]`; no abstract retrievable. It is the natural place to look
  for the agenda's mean-shift-versus-variance-shift distinction, and its cost
  functions formalise exactly that separation `[not-verified]`.

#### 8.3.5 What branch 3 lacks after this search

- **No record in the corpus reports a detection-delay/ARL operating curve for any
  detector on financial price data.** The theory (Lorden, Moustakides, Lai) is
  general; the finance application is absent from this corpus. The agenda's
  observation that this comparison "is largely absent from the trading
  literature" is **corroborated by this search**, subject to the recall limits in
  section 10.2.
- No record addresses **confirmation displacement in deseasonalized sigma**, the
  **failed-transition base rate**, or **volume-on-breakout against a
  time-of-day baseline**. These are the agenda's own constructions; nothing was
  found for or against them. Recall gap RG-4.

### 8.4 Branch 4 - validating a latent-state model without ground-truth labels

#### 8.4.1 Bootstrap under dependence

- (a)/(b) Politis & Romano (1994), doi:10.1080/01621459.1994.10476870: the
  stationary bootstrap resamples blocks of *random*, geometrically distributed
  length "as a means of calculating standard errors of estimators and constructing
  confidence regions for parameters based on weakly dependent stationary
  observations", generalising fixed-block schemes so as to "yield asymptotically
  valid procedures even for a multivariate parameter of the whole (i.e.,
  infinite-dimensional) joint distribution" `[abstract, verbatim]`.
- (c) The expected block length is a tuning parameter, and the corpus supplies
  its data-driven selection **plus a published correction that must be applied
  with it**:
  - Politis & White (2004), doi:10.1081/ETC-120028836 - "we propose practically
    useful estimators of the optimal block size" via flat-top lag windows
    `[abstract]`.
  - Patton, Politis & White (2009), doi:10.1080/07474930802459016 -
    **a correction to that formula.** `[title]` **An implementation using the
    2004 paper alone is using a formula its own authors corrected.** This is the
    single most actionable small-print item in branch 4.

#### 8.4.2 Purged and embargoed walk-forward - a documented gap

The agenda names purging, embargo, and combinatorial purged cross-validation.
What the corpus actually supports:

- **Peer-reviewed and derived:** Bailey, Borwein, López de Prado & Zhu (2016),
  doi:10.21314/JCF.2016.322, propose "a general framework to assess the
  probability of backtest overfitting (PBO)" implemented as "combinatorially
  symmetric cross-validation (CSCV)", explicitly because "standard statistical
  techniques designed to prevent regression overfitting, such as hold-out, tend
  to be unreliable and inaccurate in the context of investment backtests"
  `[abstract, verbatim]`. This is the closest peer-reviewed relative of the
  combinatorial purged scheme, and it *is* derived.
- **Not derived in anything this search retrieved:** the purging and embargo
  prescription itself. The corpus's only source is López de Prado (2018),
  doi:10.3905/jpm.2018.44.6.120, a practitioner catalogue of failure modes
  `[title]`; the book-length treatment (*Advances in Financial Machine Learning*,
  Wiley 2018) was not retrieved and carries no article-level DOI reachable by
  these queries. `gap-crossref-36`, which targeted the concept directly, returned
  no peer-reviewed methodological source - only an unrefereed 2026 SSRN posting
  (excluded as E7) and off-domain clinical machine-learning papers.
  **Finding: the embargo length is, on this corpus, a convention without a
  derivation or an empirical selection procedure.** It should be labelled
  `CONVENTION` in the agenda alongside the 70% value area until a source is
  found. This is a weaker negative than the section 8.5 items - the concept is
  clearly correct in motivation - but the *magnitude* has no published basis
  here.
- **What is derived, and is the better-grounded alternative:** Bergmeir & Benítez
  (2012), doi:10.1016/j.ins.2011.12.028 `[title]`, and Bergmeir, Hyndman & Koo
  (2018), doi:10.1016/j.csda.2017.11.003 `[title]`, address when cross-validation
  is and is not valid for autoregressive prediction. **Neither abstract was
  retrievable from Crossref or OpenAlex (VG-6), so their direction is
  `[not-verified]` here** - but they are the peer-reviewed anchors branch 4
  should be built on, and reading them is a prerequisite, not an optional extra.

#### 8.4.3 Multiple testing over the parameter grid

The agenda's "a five-parameter grid is thousands of comparisons and is registered
as one family" is exactly the problem this sub-corpus solves, and every member
has a derivation.

- White (2000), doi:10.1111/1468-0262.00152: data snooping "is practically
  unavoidable in the analysis of time-series data, as typically only a single
  history measuring a given phenomenon of interest is available for analysis"; it
  "is widely acknowledged by empirical researchers [to be] a dangerous practice
  to be avoided, but in fact it is endemic. The main problem has been a lack of
  sufficiently simple practical methods" `[abstract, verbatim]`.
- Hansen (2005), doi:10.1198/073500105000000063: the SPA test "compares favorably
  to the reality check... because it is more powerful and **less sensitive to poor
  and irrelevant alternatives**", achieved by "a studentized test statistic that
  reduces the influence of erratic forecasts and [a] sample-dependent null
  distribution" `[abstract, verbatim, emphasis added]`. **This is a documented
  failure mode of White's reality check, stated by the author of its successor:
  padding the model family with bad alternatives degrades the reality check's
  power. Since a parameter grid necessarily contains many bad settings, SPA, not
  the reality check, is the correct default for the agenda's use case.**
- Romano & Wolf (2005), doi:10.1111/j.1468-0262.2005.00615.x - stepwise
  identification of *which* models beat the benchmark under family-wise error
  control `[title]`.
- Hansen, Lunde & Nason (2011), doi:10.3982/ECTA5771, the model confidence set
  `[title]` - a set-valued answer, which is the right shape when the question is
  "which state model" rather than "does this one beat a benchmark".
- Applied precedent on this exact data class: Sullivan, Timmermann & White
  (1999), doi:10.1111/0022-1082.00163 `[title]`; Hsu, Hsu & Kuan (2010),
  doi:10.1016/j.jempfin.2010.01.001 `[title]`; and the methodological precursor,
  Brock, Lakonishok & LeBaron (1992), doi:10.1111/j.1540-6261.1992.tb04681.x
  `[title]`.

#### 8.4.4 Sharpe-ratio inference

- Lo (2002), doi:10.2469/faj.v58.n4.2453, derives "explicit expressions for the
  statistical distribution of the Sharpe ratio using standard asymptotic theory
  under several sets of assumptions... independently and identically distributed
  returns, stationary returns, and with time aggregation", and shows "that
  monthly Sharpe ratios cannot be annualized by multiplying by sqrt(12) except
  under very special circumstances" `[abstract, verbatim]`. **A named, derived
  failure mode of the most common reporting convention in the field.**
- Ledoit & Wolf (2008), doi:10.1016/j.jempfin.2008.03.002 - studentized
  time-series bootstrap for the *difference* of two Sharpe ratios `[title]`,
  which is the pairwise-comparison case the single-strategy interval does not
  cover.
- Bailey & López de Prado (2014), doi:10.3905/jpm.2014.40.5.094: the deflated
  Sharpe ratio corrects for selection bias, noting that "backtest optimizers
  search for combinations of parameters that maximize the simulated historical
  performance of a strategy, leading to back test overfitting" and that "not
  controlling for the number of trials involved in a particular discovery leads
  to overly optimistic performance expectations" `[abstract, verbatim]`.
  Companion: Bailey, Borwein, López de Prado & Zhu (2014),
  doi:10.1090/noti1105, on minimum backtest length `[title]`.

#### 8.4.5 Deseasonalization - the agenda's standing precondition

- Andersen & Bollerslev (1997), doi:10.1016/S0927-5398(97)00004-2 `[title]` - the
  record the agenda's periodicity hazard already rests on. No abstract
  retrievable from OpenAlex or Crossref (VG-7); the agenda's characterisation of
  it is `[not-verified]` by this review and should be confirmed against the
  original.
- Boudt, Croux & Laurent (2011), doi:10.1016/j.jempfin.2010.11.005 - **robust**
  estimation of intraweek periodicity and jump detection conditional on it
  `[title]`. This is the operationally important addition: a non-robust
  time-of-day mean is contaminated by the jumps one is trying to detect, so the
  deseasonalization step and the event-detection step are not separable. No
  abstract retrievable (VG-7).

### 8.5 Negative findings - the folklore audit

The task asked for an explicit list of methods for which no primary source or
derivation could be located. **That list is not empty.** Each entry below states
what was searched, what was found, and what the finding does and does not
license.

#### 8.5.1 Kaufman Efficiency Ratio - NO PRIMARY SOURCE LOCATED

- **Searched:** `q-arxiv-09` (`all:"efficiency ratio" AND all:"Kaufman"`),
  `q-arxiv-08`, `q-crossref-18`, `gap-crossref-40`.
- **Found:** `q-arxiv-09` returned **zero records** - `<opensearch:totalResults>0`
  in the log, the only query in this review that returned nothing at all.
  `gap-crossref-40` returned six records, none of which is a source for the
  Efficiency Ratio: the closest is an SSRN backtest of the Kaufman adaptive
  moving average (excluded as E8), which uses the ratio without deriving it.
- **(a) Null or derivation: NONE LOCATED.** No published distribution of the
  Efficiency Ratio under a random-walk null was found. The agenda's supposition
  that "its distribution under a random-walk null appears not to be published" is
  **corroborated by this search.**
- **(b) Primary source: NONE WITH A PERSISTENT IDENTIFIER.** The attribution to
  Perry J. Kaufman's books (*The New Commodity Trading Systems and Methods*,
  1987; *Smarter Trading*, 1995) could not be confirmed against any indexed
  record; neither book was retrievable by these queries and neither carries a DOI
  reachable by them. The agenda's own note that a specific edition and page still
  needs verifying from a licensed copy stands unresolved.
- **(c) Failure modes: NONE DOCUMENTED,** because there is no primary source to
  document them.
- **What this licenses:** deriving or simulating the null is unavoidable, and the
  agenda is right to make it a first task. **What it does not license:** claiming
  the ratio is meaningless. It is a well-defined deterministic function of a
  price path; it simply has no reference distribution in the indexed literature.

#### 8.5.2 Average Directional Index (ADX) - NO DERIVATION LOCATED

- **Searched:** `q-arxiv-10` (`all:"average directional" OR all:"choppiness
  index"`), `q-crossref-24`, `gap-crossref-38`, `q-websearch-01`.
- **Found:** `q-arxiv-10` reported 92 total hits, of which the ten retrieved are
  all unrelated uses of the words "average" and "directional". `q-crossref-24`
  returned an ARIMA supplementary-information file, a book on directional
  movement in dance, and ocean-wave statistics. `gap-crossref-38` returned book
  front matter and indexes. `q-websearch-01` returned **nine URLs, all tier-5 or
  below**: broker marketing (strike.money, warriortrading, fxcm), charting
  vendors (steema, agenatrader, stockcharts), and encyclopedia entries
  (Wikipedia, Grokipedia). **Not one peer-reviewed or standards-body source.**
- **(a) Null or derivation: NONE LOCATED.** The one peer-reviewed indexed record
  that evaluates the ADX at all - Gurrib (2018),
  doi:10.21511/bbs.13(3).2018.06, included in the corpus for exactly this purpose
  - "test[s] a trading system based on the average directional index, which is
  complemented with the parabolic stop and reverse indicator" and reports Sharpe
  and Sortino measures `[abstract, verbatim]`. **It applies the indicator; it
  does not derive it and it states no null distribution.** Its profitability
  findings are outside this review's scope and are not assessed.
- **(b) Primary source: NOT INDEXED.** The universal attribution is to J. Welles
  Wilder Jr., *New Concepts in Technical Trading Systems* (1978), a
  self-published trade book with no DOI, no ISBN record retrievable by these
  queries, and no presence in Crossref, OpenAlex, arXiv or Semantic Scholar.
  **The attribution itself rests entirely on tier-5 web sources** and is recorded
  as unverified.
- **(c) Failure modes: NONE DOCUMENTED IN PEER-REVIEWED LITERATURE.**
- **Verdict: ADX is, on the evidence of this search, an unattributed
  transformation producing a number with no reference distribution.** That is the
  agenda's own hypothesis, stated as a candidate; this review returns it as a
  finding, bounded by section 10.2's recall limits and by the fact that a
  book-form primary source is invisible to bibliographic APIs.

#### 8.5.3 Choppiness Index - NO SOURCE OF ANY KIND LOCATED

- **Searched:** `q-arxiv-10`, `gap-crossref-39`, `q-websearch-02`.
- **Found:** nothing. `gap-crossref-39` returned fractal-geometry book indexes,
  composite-material damage detection, radar target tracking, an OECD trade
  facilitation figure, and a SARS-CoV-2 fractal-signature preprint. Zero
  relevant records. `q-websearch-02` returned ten URLs, **all trade or vendor
  sources** (quantifiedstrategies, morpher, netpicks, TradingView support pages
  and user scripts, incrediblecharts, fxtradersedge, money365, stonehillforex).
- **(a) Null or derivation: NONE.** Not a weak one - none at all.
- **(b) Primary source: NONE.** Attribution to E. W. Dreiss appears in the trade
  results (`netpicks.com/choppiness-index-by-bill-dreiss/`) and **nowhere with a
  persistent identifier.** No book, paper, working paper, patent or standard was
  located. **This is the weakest-provenance method in the entire agenda.**
- **(c) Failure modes: NONE DOCUMENTED.**
- **Verdict: the Choppiness Index has no locatable primary source at any evidence
  tier above 5.** Both of the agenda's explicit folklore test cases fail the
  audit, and this one fails it more completely than ADX, which at least has a
  named book and one peer-reviewed application.

#### 8.5.4 Market Profile 70% value area - CONVENTION CONFIRMED, NO DERIVATION

- **Searched:** `q-websearch-03`, `q-websearch-05` (the latter aimed
  specifically at CME Group official documentation), `q-crossref-19`.
- **Found:** `q-websearch-03` and `q-websearch-05` between them returned
  seventeen URLs. **None is a CME Group or CBOT primary document.** The nearest
  approaches to tier-2 (official documentation) are two CQG help pages
  (`help.cqg.com/.../marketprofilemp.htm`,
  `.../marketprofilevalueareasmpva.htm`), which are vendor implementation
  documentation, not the originating specification. The remainder are blogs,
  a PDF-aggregator copy of a Market Profile handbook, Wikipedia and Grokipedia.
- **(a) Derivation: NONE LOCATED.** In particular, no source was found
  establishing the common informal justification that 70% approximates one
  standard deviation of a normal distribution - which would in any case be a
  post-hoc rationalisation rather than a derivation, since the TPO distribution
  is not assumed normal.
- **(b) Primary source: NOT LOCATED with a persistent identifier.** Attribution
  to J. Peter Steidlmayer and the CBOT appears only in tier-4/5 sources.
- **Verdict: the agenda's `CONVENTION` label on the 70% value area is correct and
  should stand.** This review's contribution is to convert "labelled CONVENTION
  until a derivation is located" into "a targeted search for the derivation was
  run and returned nothing".

#### 8.5.5 Summary of the negative list

| method | primary source located? | derivation? | null distribution? | best evidence tier found |
|---|---|---|---|---|
| Kaufman Efficiency Ratio | **no** (book attribution unverified) | **no** | **no** | 5 (trade books, uncited) |
| Average Directional Index (ADX) | **no** (Wilder 1978 not indexed) | **no** | **no** | 1 for *application only* (Gurrib 2018); 5 for the method |
| Choppiness Index | **no** | **no** | **no** | 5 (vendor pages only) |
| Market Profile 70% value area | **no** | **no** | n/a | 4 (vendor documentation) |
| Purge/embargo *length* in walk-forward CV | partial (concept only, no magnitude) | **no** | **no** | 1 for the concept's motivation; none for the magnitude |
| Page-Hinkley test *under that composite name* | components yes, composite no | yes, for the components | yes, for the components | 1 |

**Contrast - methods in the same agenda that DO have a stated null or
derivation:** dip test, excess mass, critical bandwidth, Sheather-Jones,
variance ratio (four variants), modified R/S, wavelet scaling estimator,
Markov-switching LR tests (three), ICL, CUSUM (with proved optimality), SPRT,
Bai-Perron, PELT, stationary bootstrap, reality check, SPA, stepwise multiple
testing, model confidence set, Sharpe-ratio asymptotics, deflated Sharpe,
CSCV/PBO. **The folklore is concentrated entirely in the trade-derived
indicators, and every method with an academic origin in this agenda has a
derivation.** That pattern is itself the review's most useful screening heuristic.

### 8.6 What the corpus does not contain

Stated so that its absence is not mistaken for a finding of absence:

1. **No record joins the four branches.** There is no source in the corpus that
   estimates levels, assigns states, detects transitions and validates the whole
   without labels in one framework. The agenda's integration is unsupported by
   precedent, which is a research opportunity and a risk in equal measure.
2. **No record applies detection-delay/ARL operating characteristics to price
   data** (section 8.3.5).
3. **No record addresses intraday regime classification with the
   deseasonalization precondition applied**, which is the specific configuration
   the agenda proposes. Andersen & Bollerslev and Boudt et al. establish the
   precondition; Chauvet & Piger demonstrate real-time state assignment on
   monthly macro data; nothing bridges them.
4. **No record in the corpus catalogues which published regime results plot
   smoothed rather than filtered probabilities.** That task remains open and is
   tractable via forward citation search on Kim (1994) - a search this review did
   not run.

## 9. Bibliography store

<!-- bibliography-store -->
- Store: `docs/literature/references_regime-classification.json` (CSL-JSON, canonical)
- Entries: **96** - equals frontmatter `n_included` and the section 7 corpus table.
- SHA-256: `80980318c0c67b2bac95c3c0cd24a908ac54fb7bdd8a23f4081f9bd7c2612e8d` -
  equals frontmatter `bibliography_sha256`. Canonical serialisation is
  `json.dumps(entries, indent=2, sort_keys=True, ensure_ascii=False)` plus a
  trailing newline, UTF-8, which is what is on disk.
- Persistent identifiers: **91 DOIs and 5 arXiv identifiers; every entry has
  one** (FAIR F1).
- Identifier verification, executed 2026-08-21, logged at
  `search_logs/regime-classification/gap-doicheck-43.json`: all 91 DOIs return
  handle-system `responseCode: 1` (registered and resolving) from
  `https://doi.org/api/handles/{doi}`; all 5 arXiv identifiers return HTTP 200
  from `https://arxiv.org/abs/{id}`. **0 unresolved identifiers.**
  Note on method: a HEAD request to `https://doi.org/{doi}` returns HTTP 403 for
  39 of the 91, because the publisher landing pages (Wiley, Oxford, Taylor &
  Francis, JSTOR, Econometric Society, Portfolio Management Research) block
  automated clients. That is a publisher bot policy, **not** a resolution
  failure, which is why the handle API is the check of record here.
- Two entries required author metadata from outside the aggregators: `10.3982/ECTA5771`
  (absent from both Crossref and OpenAlex; resolved from the Wiley publisher
  record, `gap-webfetch-41`) and `10.3982/ECTA8609` (absent from Crossref;
  resolved from OpenAlex). **No metadata field anywhere in the store was typed
  from model memory.**
- Derived exports (regenerable; never a source of truth):
  `python ~/.claude/scripts/build_bibliography.py export docs/literature/references_regime-classification.json --format bibtex|ris`

## 10. Limitations and verification gaps

### 10.1 Verification gaps

| id | severity | gap | consequence |
|---|---|---|---|
| VG-1 | **major** | The verbatim query strings for the **twenty-five original Crossref topical searches** (`q-crossref-01` to `q-crossref-25`) were never written to the logs. Only the API responses, their `total-results` counts and their returned items survive. | **PRISMA-S item 8 is not satisfied for 25 of 70 strategies, covering 186 of 518 identified records.** Those searches are not reproducible and cannot be updated; a refresh would have to redesign them, producing a different search. The strings are deliberately **not** reconstructed, because a reconstructed query presented as verbatim is a fabrication. This alone prevents the review from claiming a reproducible search strategy. |
| VG-2 | **major** | **No full text was retrieved for any of the 96 included records.** Screening and extraction used title, venue, year, author, and abstract where available. | Every `[title]` and `[not-verified]` mark in section 8 is a live gap. In particular, the *direction* of the findings in Lo & MacKinlay (1989), Weron (2002), Pohle et al. (2017), Truong et al. (2020), Bergmeir & Benitez (2012) and Bergmeir et al. (2018) is asserted nowhere in this review and must be read from the originals before any of them is relied on. |
| VG-3 | major | **Hall & York (2001), "On the calibration of Silverman's test for multimodality", *Statistica Sinica* 11:515-536, could not be resolved to any persistent identifier.** `gap-crossref-32` and `gap-crossref-37` both targeted it directly and returned unrelated works. *Statistica Sinica* content of that vintage is not DOI-registered in Crossref. | The corpus contains the Silverman critical-bandwidth test but **not** its principal published calibration correction. Section 8.1.1 therefore refuses to state the direction of the test's size distortion. Branch 1 must locate this paper before implementing the Silverman test. |
| VG-4 | minor | Abstract for Pohle et al. (2017), doi:10.1007/s13253-017-0283-8, is absent from Crossref and OpenAlex; `link.springer.com` returned HTTP 303 to an authentication endpoint. | The agenda's "documented inconsistency of BIC for hidden Markov models" is **not confirmed** by this review. Psaradakis & Spagnolo (2003) is the retrievable substitute, and its abstract is truncated before its conclusion. |
| VG-5 | minor | No primary source was located for the **Page-Hinkley test under that composite name**. Page (1954) and Hinkley (1971) are both in the corpus as separate works. | The agenda should cite the two components, not the composite, unless a source for the composite is found. |
| VG-6 | minor | Abstracts for Bergmeir & Benitez (2012) and Bergmeir, Hyndman & Koo (2018) are absent from both Crossref and OpenAlex. | Branch 4's cross-validation-validity anchors are included on title evidence only. |
| VG-7 | minor | Abstracts for Andersen & Bollerslev (1997) and Boudt, Croux & Laurent (2011) are absent from both aggregators. | The agenda's **standing periodicity hazard** rests on Andersen & Bollerslev, and this review could not verify its content beyond the title. The hazard is almost certainly correctly attributed, but it is recorded here as unverified rather than assumed. |
| VG-8 | minor | The full request URLs for `s2-ecta5771` and `s2-mcs-search` were not captured; only the error responses survive (HTTP 404 and HTTP 429 respectively). The two original OpenAlex DOI lookups (`openalex-ecta5771`, `openalex-ecta8609`) are reconstructed from the log filename and returned work id rather than captured verbatim. | Four further strategies fall short of PRISMA-S item 8, though all four were known-item lookups whose target is unambiguous. |
| VG-9 | minor | Nine of the 92 known-item DOI lookups resolved to unrelated works (exclusion E10): a book review, a coding-theory survey, meeting minutes, a competing-risks paper, and five others. | The known-item list was assembled from recalled or transcribed DOIs, and roughly **10% of them were wrong**. Every DOI that *did* resolve to a plausible work was nevertheless verified against its returned title before storage, so no mistyped DOI entered the corpus - but this failure rate is a standing argument against DOI-by-recall as a retrieval method, and is why every entry in the store came from an API response rather than from typing. |
| VG-10 | minor | Semantic Scholar was effectively unavailable: one 404, one HTTP 429 rate-limit, and a title search that did not return the target work. | One of the four intended aggregators contributed almost nothing. Coverage rests on Crossref, OpenAlex and arXiv. |

**No gap in this table was closed by substituting recalled knowledge for a
fetch.** Where a fetch failed, the claim it would have supported is marked
`[not-verified]` in section 8 or is absent.

### 10.2 Recall limitations

These are not verification failures; they are searches that were never run, and
each bounds how far the negative findings in section 8.5 can be pushed.

| id | limitation |
|---|---|
| RG-1 | **No forward or backward citation searching.** No Scopus, Web of Science, citationchaser or Connected Papers pass. The section 8.2.7 task - catalogue which published regime results plot smoothed probabilities - is precisely a forward-citation task on Kim (1994) and was not performed. |
| RG-2 | **Level persistence and half-life** were never searched. No query in any of the 70 targeted the survival function of an estimated level. Its absence from the corpus is uninformative. |
| RG-3 | **DBSCAN, agglomerative clustering and pivot-point clustering for level construction** were never searched, despite the agenda naming Ester et al. (1996). Uninformative absence. |
| RG-4 | **Confirmation displacement, failed-transition base rate, and volume-on-breakout against a time-of-day baseline** were never searched. Uninformative absence. |
| RG-5 | **Result sets were capped and never paged.** `max_results` 10-20 on arXiv, `rows` 5-10 on Crossref, first page only. `q-arxiv-02` retrieved 15 of 137 hits; `q-arxiv-10` retrieved 10 of 92; several Crossref queries reported millions of total hits and returned eight records. Recall is therefore bounded by each platform's relevance ranking, which is undocumented and not reproducible across time. **The caps have no empirical justification and are recorded as a defect, not a design choice** (CLAUDE.md: no arbitrary thresholds). |
| RG-6 | **No database indexing books was searched.** No JSTOR, EconLit, RePEc, Google Books or library catalogue. Since the three strongest negative findings (Efficiency Ratio, ADX, Market Profile value area) all have book-form attributions, **the negatives in section 8.5 are specifically "no source in the DOI-indexed literature", not "no source anywhere".** A reader with a licensed copy of Wilder (1978) or Kaufman (1987/1995) can close the attribution question; they cannot close the *derivation* and *null distribution* questions, because the search also found no derivation in the peer-reviewed literature that cites those books. |
| RG-7 | **`q-arxiv-08` contains a Boolean precedence defect**: `abs:"regime" AND abs:"efficiency ratio" OR abs:"trend strength" AND abs:"indicator"`, unparenthesised. It returned 5 records. A PRESS review would have caught it (section 4). |

### 10.3 Screening and extraction limitations

- **Single screener** (section 1.3, section 5). No agreement measure exists and
  none is reported. Exclusion E3 is explicitly marked as a decision a second
  screener might reasonably have reversed; it is unlikely to be the only one.
- **Screening on metadata only.** Where Crossref supplied no abstract - which is
  the majority of pre-2000 records and much of the statistics literature - the
  decision rested on title, venue and author alone.
- **No risk-of-bias instrument** (section 1.3, item 11). The evidence-tier and
  derivation-status columns are a substitute of convenience, not an equivalent.
- **No certainty-of-evidence rating** (item 23).
- The three records re-admitted this session (Kantelhardt 2002, Petruccelli 1990,
  Gurrib 2018) were originally excluded by the same screener in a prior session
  and included in this one, against unchanged criteria. **That is a directly
  observed instance of single-screener instability**, and it is the strongest
  concrete evidence in this document for why section 1.3's refusal to compute an
  agreement statistic from self-comparison is the right call: the same model with
  the same criteria produced different decisions on at least 3 of 462 records
  across sessions.

### 10.4 Provenance limitations inherited from the prior session

This review was written in a session that did **not** run the original searches;
that session terminated on an API error before writing anything. Everything in
sections 2, 3 and 5 concerning `q-arxiv-*`, `q-crossref-*`, `ki-batch*`,
`openalex-*`, `s2-*` and `q-websearch-*` is **reconstructed from the artifacts
those searches left on disk**, not observed. Specifically:

- Record counts are recomputed from the response files, so they are exact.
- arXiv query strings are the API's own echo inside the response, so they are
  verbatim.
- WebSearch query strings were written into `q-websearch.json` by the original
  session, so they are verbatim *as that session recorded them* - one degree of
  trust weaker than a server echo.
- Crossref topical query strings do not exist anywhere and are the subject of
  VG-1.
- Dates and times come from the response payloads and file timestamps.

A reader who requires end-to-end observed provenance should treat this review as
covering two sessions with a hard boundary between them, and should treat VG-1 as
the price of that boundary.

### 10.5 Scope exclusions applied by directive

Not limitations of the search, but boundaries set before it: the review does not
assess profitability of any method; does not address the project's architecture
or context-portability agendas; does not verify citations asserted elsewhere in
the repository (that is `literature-check`'s job, not this one); and writes to no
directory other than `docs/literature/`.

### 10.6 Gate verdict: `block`, on 40 G16 findings, all of which are false positives

The research-compile gate
(`~/.claude/skills/research-compile/assets/check_lit_review.py`, assertions
G1-G20) was run against this file on 2026-08-21. **Verdict: `block`.**

- **G1-G15 and G17-G20: pass.** No findings.
- **G16: 40 findings, severity `critical`,** each of the form
  `DOI <x> did not resolve (HTTP 403)` or `(HTTP 302)`.

**Every one of the 40 is a false positive, and the refutation is mechanical
rather than argumentative.** G16 implements resolution as an HTTP HEAD to
`https://doi.org/{doi}` and treats any terminal status outside 2xx-3xx as a
failure. Because urllib follows the redirect, the terminal status is the
*publisher's* response to an automated client, not the DOI system's. Of the 40,
thirty-eight publisher targets return HTTP 403 (INFORMS, Wiley, Oxford, Taylor &
Francis, ASCE, AGU, APS, Econometric Society, Business Perspectives, Now
Publishers) and two return an authentication HTTP 302 (Portfolio Management
Research, `idp.sams-sigma.com`) to any non-browser agent.
Verified by replicating the gate's exact request with a browser user-agent
string: `10.1287/opre.13.2.258` returns HTTP 403 under both, **from
`https://pubsonline.informs.org/doi/10.1287/opre.13.2.258`** - which is the
correct target, so the DOI resolved and then the publisher refused the client.

The authoritative check is the DOI handle system, which reports registration and
target independently of publisher access control:

```
GET https://doi.org/api/handles/{doi}   ->  responseCode: 1  (registered, resolving)
```

Run over all 91 DOIs in the store on 2026-08-21, logged verbatim at
`docs/literature/search_logs/regime-classification/gap-doicheck-43.json`:
**91 of 91 return `responseCode: 1`; zero failures.** The five arXiv identifiers
return HTTP 200 from `https://arxiv.org/abs/{id}`.

**This section does not ask for the verdict to be overridden.** The gate's
verdict is reported as `block` wherever this review is cited, per the
research-compile exit condition, and nothing here is a claim of `pass`. What is
recorded is the diagnosis: **the blocking findings are an artifact of G16's
resolution method, and the corpus's identifiers are sound.** Remediation belongs
in the gate (switch G16 to the handle API, or treat a 4xx from a redirect target
as `resolved-but-access-controlled`), not in this review or its store - and
modifying the gate is outside this agent's remit.
