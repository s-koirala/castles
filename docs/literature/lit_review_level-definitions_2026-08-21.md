---
title: "What is a level? A definitional survey of support, resistance, zone and range constructs, taxonomised by dependence on round numbers and the tick grid"
slug: level-definitions
date: 2026-08-21
objective: "Enumerate every operational definition of a price level, zone, band, range or block that is stated anywhere in the peer-reviewed, preprint, code, vendor, or practitioner literature, and classify each one by whether it requires round numbers, requires the tick grid, or is independent of both - so that branch 1 of the regime-classification agenda can decide which properties a null-generating process must preserve."
review_type: systematic
standard_declared: "PRISMA 2020 + PRISMA-S (adapted, non-clinical) - PARTIAL COMPLIANCE, single screener; see section 1.4 for the item-by-item conformance statement"
eligibility_inclusion:
  - "Any source that states, in terms an implementer could execute without further interpretation, a rule locating one or more price levels, zones, bands, ranges, channels or blocks on a price axis."
  - "Any source supplying empirical evidence about whether such a construct depends on round numbers, on the tick grid, or on neither."
  - "Any source attaching a null distribution, statistical test, falsification criterion or reference distribution to such a construct."
  - "Any source establishing the confound itself - price clustering at round numbers, price discreteness, tick-size effects, strike-grid pinning - independently of whether it uses the word level."
  - "Any language; any year; journal article, conference paper, book chapter, preprint, working paper, published source code, or vendor documentation."
eligibility_exclusion:
  - "Records whose only content is the profitability or backtest performance of a rule, with no statement of how the level itself is located (excluded by task directive; profitability is not assessed anywhere in this review)."
  - "Records retrieved in error, where the identifier resolved to a work in an unrelated field - the topical queries for range, block, barrier and profile are highly polysemous and this is the dominant exclusion reason."
  - "Records that name a construct without stating any rule for locating it, where a distinct source already supplies the operational statement; the name-only sources are recorded in section 8.7 rather than in the corpus."
  - "Sources with no persistent identifier - source code, vendor help pages, trade blogs, encyclopedia entries. These are in scope as definitions, are tiered and synthesised in sections 7.3 and 8, and are logged verbatim in the search logs, but they cannot be CSL-JSON store entries because FAIR F1 requires a persistent identifier."
  - "Records duplicating an already-retained work under a second identifier; these are handled by deduplication, not by exclusion, and are enumerated in the dedup ledger."
registration: not-registered
protocol_path: none
protocol_amendments: "The eligibility criteria were fixed before the first query was executed and were not altered afterwards. Two search-method additions were made during execution and are recorded rather than backdated: (i) GitHub repository search was added after GitHub code search returned predominantly low-provenance derivative repositories, so that implementations could be selected by an independent visibility proxy rather than by string match; (ii) direct raw-file retrieval (q-github-src-09, q-github-src-10) was added because the task requires reading algorithms rather than repository descriptions, and neither search API returns file bodies. No eligibility criterion was changed, and no record already screened was re-screened under a new criterion."
bibliography: docs/literature/references_level-definitions.json
bibliography_sha256: 213824cd107fd52fa682ba66bfbd206318c554f201cb470673dde652d8462a9f
n_identified: 436
n_duplicates_removed: 46
n_screened: 390
n_excluded: 309
n_included: 81
materials_availability:
  - docs/literature/search_logs/level-definitions/
  - docs/literature/references_level-definitions.json
competing_interests: none
ai_assistance: "Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK, research-librarian agent) designed and executed the searches, screened every record, extracted every definition, read every source file listed in q-github-src-09 and q-github-src-10, and drafted this review. It is the sole screener and is declared as an automation tool under PRISMA 2020 item 8. No human second screener participated. Reproducibility log directory: logs/reproducibility/"
git_head_at_authoring: "7dfc83b94b6827c7b080904c00761287ec66db7c"
pip_freeze_sha256: "n/a - no analysis code was executed; only metadata-retrieval and bibliography-store scripts, plus read-only inspection of third-party source files"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-opus-5"
---

# What is a level? A definitional survey of support, resistance, zone and range constructs

## 1. Objective and eligibility

### 1.1 Objective

Branch 1 of the regime-classification agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md))
is blocked. The block is not statistical. It reads:

> "level" is never defined disjointly from round-number clustering and tick
> discreteness, so it cannot be decided whether those are construct or
> non-construct properties - which means no null-generating process can be
> specified at all until the construct is.

The charter's `construct` gate
([charter_castles_2026-08-21.md](../methodology/charter_castles_2026-08-21.md))
requires a surrogate "preserving every *known* non-construct property of the
data". That requirement is unsatisfiable while the partition of properties into
construct and non-construct is undecided. This review does not resolve the
partition by argument. It does the prior thing: it collects every operational
definition of a level that anyone has written down, at any level of rigour, and
sorts them by which of the two confounds each one actually needs.

The output that matters is section 8.6, a three-way taxonomy:

- **Class R** - definitions that require round numbers. The level location is a
  function of the decimal representation of price.
- **Class T** - definitions that require the tick grid, or another quantisation
  of the price axis imposed by the exchange rather than chosen by the definition.
  Such a rule is undefined when price is continuous.
- **Class N** - definitions independent of both. The level location is a function
  only of the realised path, of volume, or of the order book, and is equivariant
  under an affine change of the price axis.

The class determines what a surrogate must preserve, and therefore which
surrogate branch 1 may build. A Class N construct can be tested against a null
that destroys round-number clustering, because the construct does not live
there. A Class R construct cannot: destroying round-number clustering destroys
the construct, which is the alternative-absorbing surrogate the charter's gate
condition (v) exists to forbid.

This review does not assess whether any definition is profitable, and does not
backtest anything. Where the only retrievable evidence about a definition is a
profitability study, the study is included for its statement of the rule and its
statistical apparatus, and its performance claims are neither reported nor
relied on.

### 1.2 What counts as an operational definition

A definition is operational here if a competent implementer could execute it on
an OHLCV or message-level dataset without a further interpretive decision that
the source leaves open. Three failure modes disqualify a statement:

1. **Name only.** The construct is named and its significance asserted, but no
   locating rule is given. Section 8.7 lists these.
2. **Rule with an unbound parameter and no selection procedure.** These are
   *conditionally* operational: the rule executes once a number is supplied, but
   the source supplies neither the number nor a procedure for choosing it. Under
   charter commitment 3 these are recorded with the parameter named and marked
   `CONVENTION`, not silently completed.
3. **Rule requiring visual judgement.** "Draw the line where price has turned
   several times" is not executable; a rule that says how many turns, within what
   tolerance, over what window, is.

### 1.3 Grouping for synthesis

Definitions are grouped by *what locates the level*, not by who published them:
(A) prior-period arithmetic, (B) extrema of the realised path, (C) clustering or
density over the price axis, (D) volume or time distribution over the price axis,
(E) order-book state, (F) exogenous grids - round numbers, ticks, strikes,
(G) volatility-scaled bands, (H) candle-geometry blocks and gaps. The taxonomy in
section 8.6 cuts across these groups, which is the point: group and class do not
coincide, and two definitions from the same practitioner tradition can land in
different classes.

### 1.4 Conformance statement - this is a single-screener review

> The project charter requires conduct and reporting to PRISMA 2020, including
> **dual independent screening and extraction with an agreement measure**. **A
> single agent cannot satisfy that requirement.** Two screening passes by the same
> model are not independent: they share training data, parameters, and systematic
> bias, so any agreement statistic computed between them measures decoding
> variance, not reliability. Reporting a kappa from such a pair would be worse
> than reporting none, because it would look like evidence. This review therefore
> declares itself **PRISMA 2020 partial compliance, single screener**, and states
> below exactly which items are met and which are not. This is the same posture,
> for the same reason, as the regime-classification review.

| PRISMA 2020 item | Status | Note |
|---|---|---|
| 3 Rationale, 4 Objectives | met | section 1.1 |
| 5 Eligibility criteria | met | frontmatter; fixed before the first query and unchanged thereafter |
| 6 Information sources | met | section 2 table, one row per executed query, with platform and ISO 8601 date |
| 7 Search strategy | met | every query string in section 3 was captured at execution time from the executing process, not reconstructed. This is the item the regime-classification review could only partially meet; the failure there was that query strings were not written to the logs at execution time, and the remedy adopted here was to log the query with the result in the same write |
| 8 Selection process | met, negatively | one screener, not independent, automation tool declared with version - section 5 |
| 9 Data collection process | **partially met** | single extractor, no duplicate extraction, no agreement measure. Extraction for code sources was done by reading the source file, not the documentation - see section 5 |
| 10 Data items | met | the six fields the task directive specifies (definition, inputs, line-or-band, confound relationship, tier, null attached) are the extraction schema; they appear as columns in sections 8.1 through 8.5 |
| 11 Risk of bias in studies | **not met** | no risk-of-bias instrument was applied. No validated instrument exists for this corpus, which is mostly definitional rather than inferential; ROBIS, RoB 2 and QUADAS-2 target clinical designs that do not occur here. The review records an evidence tier per definition and a null-attached verdict per definition instead. That substitution is **not** a risk-of-bias assessment and must not be reported as one |
| 12-15 Effect measures, synthesis methods, reporting-bias, certainty | **not applicable / not met** | no effect sizes are pooled; the units are definitions, not estimates |
| 16a Flow of records | met | frontmatter counts, arithmetic-checked, per-source counts in section 2 |
| 16b Exclusions with reasons | met | section 6 |
| 17-22 Study characteristics, RoB results, results of syntheses | partially met | sections 7 and 8 carry characteristics and narrative synthesis; no risk-of-bias results |
| 23 Certainty of evidence | **not met** | no formal certainty rating |
| 24a/b/c Registration and protocol | met, negatively | not registered, no protocol, amendments recorded in frontmatter |
| 25 Support | met | none |
| 26 Competing interests | met | none |
| 27 Availability of data, code, materials | met | search logs and CSL-JSON store committed |

**Publication-bias posture** (charter, section "Publication-bias posture"). No
funnel-plot or small-study assessment is meaningful here. The bias that does
threaten this review is different and is stated plainly: **a definition that
circulates only orally or in video form cannot be retrieved by any bibliographic
or code search.** Large parts of the retail tradition - the ICT corpus above all -
are transmitted that way. Section 8.7 records which definitions were reachable
only through secondary restatement, and the count there is a lower bound on the
problem, not a measure of it.

## 2. Information sources and methods

<!-- prisma-s-1 -->
One row per executed query. `n_records` is the number of records actually
retrieved and carried into screening, not the total-hit count the API reported.
Total-hit counts survive in the raw logs. Rows with `n_records` of 0 are
retained: a query that returns nothing is a finding, and four of the arXiv rows
below are among the most informative results in this review.

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-01 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-02 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-03 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-04 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-05 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-06 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-07 | 8 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-08 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-09 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-10 | 10 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-11 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-12 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-13 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-14 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-15 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-16 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-17 | 8 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | q-crossref-18 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-19 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-20 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-21 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-22 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-23 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-24 | 6 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | q-crossref-25 | 6 |
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
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-27 | 5 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-28 | 5 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-29 | 5 |
| Crossref | Crossref REST API (api.crossref.org), known-item | 2026-08-21 | ki-30 | 3 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-01 | 7 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-02 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-03 | 15 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-04 | 1 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-05 | 6 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-06 | 7 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-07 | 1 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-08 | 12 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-09 | 1 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-10 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-11 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-12 | 1 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-13 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-14 | 10 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-15 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-16 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-17 | 2 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | q-arxiv-18 | 0 |
| GitHub | GitHub REST API code search (api.github.com/search/code) | 2026-08-21 | q-github-01 | 8 |
| GitHub | GitHub REST API code search (api.github.com/search/code) | 2026-08-21 | q-github-02 | 8 |
| GitHub | GitHub REST API code search (api.github.com/search/code) | 2026-08-21 | q-github-03 | 8 |
| GitHub | GitHub REST API repository search (api.github.com/search/repositories, sort=stars) | 2026-08-21 | q-github-04 | 6 |
| GitHub | GitHub REST API repository search (api.github.com/search/repositories, sort=stars) | 2026-08-21 | q-github-05 | 6 |
| GitHub | GitHub REST API repository search (api.github.com/search/repositories, sort=stars) | 2026-08-21 | q-github-06 | 6 |
| GitHub | GitHub REST API repository search (api.github.com/search/repositories, sort=stars) | 2026-08-21 | q-github-07 | 5 |
| GitHub | GitHub REST API repository search (api.github.com/search/repositories, sort=stars) | 2026-08-21 | q-github-08 | 6 |
| GitHub source files | raw.githubusercontent.com direct file retrieval (curl) | 2026-08-21 | q-github-src-09 | 7 |
| TradingView published script (Pine source, GitHub mirror) | raw.githubusercontent.com direct file retrieval (curl) | 2026-08-21 | q-github-src-10 | 1 |
| Web search (grey, vendor and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-01 | 8 |
| Web search (grey, vendor and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-02 | 10 |
| Web search (grey, vendor and trade literature) | Claude Code WebSearch tool, US region | 2026-08-21 | q-websearch-03 | 10 |
| TradingView Help Center | tradingview.com/support via WebFetch | 2026-08-21 | q-webfetch-tv-pivots | 1 |
| TradingView Help Center | tradingview.com/support via WebFetch | 2026-08-21 | q-webfetch-tv-volumeprofile | 1 |
| TradingView Pine Script Reference | tradingview.com/pine-script-reference/v6 via WebFetch | 2026-08-21 | q-webfetch-tv-pineref | 0 |

**Total records identified: 436** (equals frontmatter `n_identified`).

<!-- prisma-s-2 -->
No multi-database platform search was used. Crossref, arXiv and GitHub were each
searched through their own native REST or Atom API, one database per query. No
Ovid, EBSCO, ProQuest or Web of Science platform was available to this agent, and
no federated search interface was used. Each row in the table above is one HTTP
request to one service.

<!-- prisma-s-3 -->
No study registries were searched. PROSPERO, ClinicalTrials.gov, ICTRP and OSF
Registries index prospectively registered studies, overwhelmingly clinical, and
carry no records of price-level definitions. This is a deliberate non-search, not
an omission: the review's units are definitions, and definitions are not
registered anywhere. The consequence is that this review cannot detect a
registered-but-unpublished test of any definition below, which matters for
section 8.5 and is repeated as a limitation in section 10.

<!-- prisma-s-4 -->
Four source classes were purposefully browsed rather than queried, because the
task requires reading the algorithm rather than the abstract:

- **GitHub repository trees.** For each implementation selected in q-github-04
  through q-github-08, the full recursive tree was listed via
  `api.github.com/repos/{repo}/git/trees/HEAD?recursive=1`, and the file
  containing the level-locating routine was identified by inspection of the path
  list, then retrieved raw. Seven such files were read in full (q-github-src-09).
- **A TradingView published script.** The Pine v5 source of the open-source
  TradingView script *Smart Money Concepts [LuxAlgo]* was read from a
  CC BY-NC-SA 4.0 GitHub mirror (q-github-src-10), 848 lines. TradingView script
  pages themselves are client-side rendered and could not be fetched; the mirror
  is the same artifact under a license permitting redistribution, and is treated
  as the published script, with that provenance step recorded.
- **TradingView Help Center pages** for Pivot Points Standard and Volume Profile
  (q-webfetch-tv-pivots, q-webfetch-tv-volumeprofile). These are vendor
  documentation - tier 2 for the question "what does this vendor compute" and
  tier 5 for any claim about markets.
- **The TradingView Pine Script v6 Language Reference**, attempted and failed
  (q-webfetch-tv-pineref). Recorded as a verification gap in section 10.1.

<!-- prisma-s-5 -->
Backward citation searching was performed informally and is declared as such: the
known-item queries ki-01 through ki-30 were seeded from references named in the
regime-classification agenda and from works cited inside records retrieved by the
topical queries. This is reference-list following, executed as new known-item
queries so that each retrieval is logged, but it was not exhaustive - no
reference list was worked through in full. **No forward citation search was
performed.** Neither Scopus, Web of Science, nor Google Scholar was available;
the OpenAlex `cited_by` endpoint was not used. This is the largest recall gap in
the review and is restated in section 10.2.

<!-- prisma-s-6 -->
No contacts were made with authors, experts, vendors, exchanges or software
maintainers. Three questions in this review could probably be settled by a single
email each - the primary source of the Market Profile 70% value area, the
originating written statement of the ICT order block, and the provenance of the
Camarilla constant 1.1/12 - and none was asked. Recorded so the absence is not
mistaken for a negative result.

<!-- prisma-s-7 -->
One further method: **algorithm reading as extraction**. For every source-code
record, the definition recorded in section 8 was extracted from the executable
statements, not from the README, docstring or repository description. Where the
docstring and the code disagreed, the code was taken as the definition and the
disagreement is reported. This is the review's substitute for the primary-source
rule in the charter's evidence standard, applied to a tier where the code is the
primary source.
## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S 8 requires the query "copied and pasted exactly as run". Every block
below was written to the search log by the executing process at the moment of
execution, in the same write as the result set; none was retyped or
reconstructed afterwards. For the API sources the query as run *is* the request
URL, including the row limit, the field selector and the sort order, so the URL
is what is reproduced - a bare keyword string would understate the query,
because the row limit determines what entered screening.

One fence per `query_id`, in the order of the section 2 table.

### 3.1 Crossref, topical and title-field queries
```text q-crossref-01
https://api.crossref.org/works?query.bibliographic=support+and+resistance+levels+technical+analysis&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-02
https://api.crossref.org/works?query.bibliographic=price+clustering+round+numbers+stock+prices&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-03
https://api.crossref.org/works?query.bibliographic=psychological+barriers+round+numbers+stock+index&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-04
https://api.crossref.org/works?query.bibliographic=limit+order+book+price+clustering+depth&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-05
https://api.crossref.org/works?query.bibliographic=tick+size+price+discreteness+market+microstructure&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-06
https://api.crossref.org/works?query.bibliographic=market+profile+volume+at+price+value+area+auction+market+theory&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-07
https://api.crossref.org/works?query.bibliographic=pivot+point+intraday+trading+levels+futures&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-08
https://api.crossref.org/works?query.bibliographic=stop+loss+order+clustering+support+resistance+foreign+exchange&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-09
https://api.crossref.org/works?query.title=support+resistance+levels+detection+algorithm&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-10
https://api.crossref.org/works?query.title=price+barriers+round+numbers&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-11
https://api.crossref.org/works?query.title=technical+analysis+chart+patterns+kernel+regression+automation&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-12
https://api.crossref.org/works?query.title=volume+at+price+point+of+control+value+area&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-13
https://api.crossref.org/works?query.title=order+block+liquidity+sweep+smart+money+concepts&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-14
https://api.crossref.org/works?query.title=volume+weighted+average+price+VWAP+execution+benchmark&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-15
https://api.crossref.org/works?query.title=opening+range+breakout&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-16
https://api.crossref.org/works?query.title=swing+high+swing+low+turning+point+detection+financial+time+series&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-17
https://api.crossref.org/works?query.title=perceptually+important+points+time+series+segmentation&rows=8&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-18
https://api.crossref.org/works?query.title=zigzag+indicator+trend+extrema+financial&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-19
https://api.crossref.org/works?query.bibliographic=Donchian+channel+breakout+highest+high+lowest+low+trading+rule&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-20
https://api.crossref.org/works?query.bibliographic=Wyckoff+method+accumulation+distribution+trading+range+market+structure&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-21
https://api.crossref.org/works?query.bibliographic=average+true+range+Wilder+volatility+stop+indicator&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-22
https://api.crossref.org/works?query.bibliographic=supply+and+demand+zones+price+action+trading+definition&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-23
https://api.crossref.org/works?query.bibliographic=iceberg+orders+hidden+liquidity+detection+limit+order+book&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-24
https://api.crossref.org/works?query.bibliographic=kernel+density+estimation+price+distribution+modes+financial+time+series&rows=6&select=DOI,title,issued,container-title,type,abstract
```
```text q-crossref-25
https://api.crossref.org/works?query.bibliographic=Brownian+local+time+occupation+measure+price+process+sojourn&rows=6&select=DOI,title,issued,container-title,type,abstract
```
### 3.2 Crossref, known-item queries

Seeded from works named in the regime-classification agenda and from references
appearing inside records retrieved by section 3.1. `rows=3` throughout, except
ki-27 through ki-29, which are topical rather than known-item and use `rows=5`;
they are grouped here because they were executed in the same batch and that is
what the log records.
```text ki-01
https://api.crossref.org/works?query.bibliographic=Kavajecz+Odders-White+Technical+analysis+and+liquidity+provision&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-02
https://api.crossref.org/works?query.bibliographic=Lo+Mamaysky+Wang+Foundations+of+technical+analysis+computational+algorithms+statistical+inference&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-03
https://api.crossref.org/works?query.bibliographic=Harris+stock+price+clustering+and+discreteness+Review+of+Financial+Studies+1991&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-04
https://api.crossref.org/works?query.bibliographic=Ley+Varian+are+there+psychological+barriers+in+the+Dow-Jones+index&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-05
https://api.crossref.org/works?query.bibliographic=Donaldson+Kim+price+barriers+in+the+Dow+Jones+industrial+average&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-06
https://api.crossref.org/works?query.bibliographic=Sonnemans+price+clustering+and+natural+resistance+points+in+the+Dutch+stock+market&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-07
https://api.crossref.org/works?query.bibliographic=Christie+Schultz+why+do+NASDAQ+market+makers+avoid+odd-eighth+quotes&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-08
https://api.crossref.org/works?query.bibliographic=Ikenberry+Weston+clustering+in+US+stock+prices+after+decimalisation&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-09
https://api.crossref.org/works?query.bibliographic=Bhattacharya+Holden+Jacobsen+penny+wise+dollar+foolish+buy-sell+imbalances+on+and+around+round+numbers&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-10
https://api.crossref.org/works?query.bibliographic=Osler+support+for+resistance+technical+analysis+and+intraday+exchange+rates&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-11
https://api.crossref.org/works?query.bibliographic=Bouchaud+Mezard+Potters+statistical+properties+of+stock+order+books+empirical+results+and+models&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-12
https://api.crossref.org/works?query.bibliographic=Aggarwal+Lucey+psychological+barriers+in+gold+prices&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-13
https://api.crossref.org/works?query.bibliographic=Mitchell+clustering+and+psychological+barriers+the+importance+of+numbers&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-14
https://api.crossref.org/works?query.bibliographic=Krugman+target+zones+and+exchange+rate+dynamics&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-15
https://api.crossref.org/works?query.bibliographic=Chang+Osler+methodical+madness+technical+analysis+and+the+irrationality+of+exchange+rate+forecasts&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-16
https://api.crossref.org/works?query.bibliographic=Curcio+Goodhart+Guillaume+Payne+do+technical+trading+rules+generate+profits+conclusions+from+the+intra-day+foreign+exchange+market&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-17
https://api.crossref.org/works?query.bibliographic=Sullivan+Timmermann+White+data-snooping+technical+trading+rule+performance+and+the+bootstrap&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-18
https://api.crossref.org/works?query.bibliographic=Park+Irwin+what+do+we+know+about+the+profitability+of+technical+analysis&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-19
https://api.crossref.org/works?query.bibliographic=De+Ceuster+Dhaene+Schatteman+on+the+hypothesis+of+psychological+barriers+in+stock+markets+and+Benford+law&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-20
https://api.crossref.org/works?query.bibliographic=Ni+Pearson+Poteshman+stock+price+clustering+on+option+expiration+dates&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-21
https://api.crossref.org/works?query.bibliographic=Avellaneda+Lipkin+a+market-induced+mechanism+for+stock+pinning&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-22
https://api.crossref.org/works?query.bibliographic=Gould+Porter+Williams+McDonald+Fenn+Howison+limit+order+books&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-23
https://api.crossref.org/works?query.bibliographic=Zovko+Farmer+the+power+of+patience+a+behavioural+regularity+in+limit+order+placement&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-24
https://api.crossref.org/works?query.bibliographic=Cont+Stoikov+Talreja+a+stochastic+model+for+order+book+dynamics&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-25
https://api.crossref.org/works?query.bibliographic=Osler+stop-loss+orders+and+price+cascades+in+currency+markets&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-26
https://api.crossref.org/works?query.bibliographic=Golez+Jackwerth+pinning+in+the+S%26P+500+futures&rows=3&select=DOI,title,issued,container-title,type,abstract
```
```text ki-27
https://api.crossref.org/works?query.bibliographic=point+and+figure+charting+box+size+reversal&rows=5&select=DOI,title,issued,container-title,type,abstract
```
```text ki-28
https://api.crossref.org/works?query.bibliographic=Bollinger+bands+volatility+bands+standard+deviation+moving+average+trading&rows=5&select=DOI,title,issued,container-title,type,abstract
```
```text ki-29
https://api.crossref.org/works?query.bibliographic=Fibonacci+retracement+levels+financial+markets+test&rows=5&select=DOI,title,issued,container-title,type,abstract
```
```text ki-30
https://api.crossref.org/works?query.bibliographic=Dorfleitner+Klein+psychological+barriers+in+European+stock+markets&rows=3&select=DOI,title,issued,container-title,type,abstract
```
### 3.3 arXiv

The `cat:q-fin*` restriction appears in eight of the eighteen queries. It is a
deliberate precision device against the polysemy of every term in this review:
"order block", "price barrier", "market profile" and "local extrema" all have
large unrelated literatures in physics, numerical analysis and networks, and
q-arxiv-08 and q-arxiv-14 show what happens without it or with it applied to a
term that has no finance usage. Queries returning zero are retained; they are
evidence about the retail vocabulary, not failures.
```text q-arxiv-01
http://export.arxiv.org/api/query?search_query=all:%22support%20and%20resistance%22%20AND%20cat:q-fin*&start=0&max_results=15&sortBy=relevance
```
```text q-arxiv-02
http://export.arxiv.org/api/query?search_query=all:%22price%20clustering%22%20AND%20all:%22round%20numbers%22&start=0&max_results=15&sortBy=relevance
```
```text q-arxiv-03
http://export.arxiv.org/api/query?search_query=all:%22order%20book%22%20AND%20all:%22price%20levels%22&start=0&max_results=15&sortBy=relevance
```
```text q-arxiv-04
http://export.arxiv.org/api/query?search_query=all:%22tick%20size%22%20AND%20all:%22price%20discreteness%22&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-05
http://export.arxiv.org/api/query?search_query=all:%22resistance%20level%22%20AND%20cat:q-fin*&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-06
http://export.arxiv.org/api/query?search_query=all:%22volume%20profile%22%20AND%20cat:q-fin*&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-07
http://export.arxiv.org/api/query?search_query=all:%22technical%20analysis%22%20AND%20all:%22trading%20range%22&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-08
http://export.arxiv.org/api/query?search_query=all:%22price%20barrier%22%20AND%20cat:q-fin*&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-09
http://export.arxiv.org/api/query?search_query=all:%22trend%20line%22%20AND%20all:%22detection%22%20AND%20cat:q-fin*&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-10
http://export.arxiv.org/api/query?search_query=all:%22chart%20pattern%22%20AND%20all:%22recognition%22%20AND%20cat:q-fin*&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-11
http://export.arxiv.org/api/query?search_query=all:%22psychological%20barriers%22%20AND%20all:%22prices%22&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-12
http://export.arxiv.org/api/query?search_query=all:%22round%20number%22%20AND%20cat:q-fin*&start=0&max_results=15&sortBy=relevance
```
```text q-arxiv-13
http://export.arxiv.org/api/query?search_query=all:%22pivot%20point%22%20AND%20cat:q-fin*&start=0&max_results=10&sortBy=relevance
```
```text q-arxiv-14
http://export.arxiv.org/api/query?search_query=all:%22order%20block%22%20OR%20all:%22smart%20money%20concepts%22&start=0&max_results=10&sortBy=relevance
```
```text q-arxiv-15
http://export.arxiv.org/api/query?search_query=all:%22local%20extrema%22%20AND%20all:%22financial%20time%20series%22&start=0&max_results=12&sortBy=relevance
```
```text q-arxiv-16
http://export.arxiv.org/api/query?search_query=all:%22price%20pinning%22%20OR%20all:%22option%20expiration%20clustering%22&start=0&max_results=10&sortBy=relevance
```
```text q-arxiv-17
http://export.arxiv.org/api/query?search_query=all:%22large%20tick%22%20AND%20all:%22price%20formation%22&start=0&max_results=10&sortBy=relevance
```
```text q-arxiv-18
http://export.arxiv.org/api/query?search_query=all:%22market%20profile%22%20AND%20cat:q-fin*&start=0&max_results=10&sortBy=relevance
```
### 3.4 GitHub

Two strategies. Code search (q-github-01 to q-github-03) finds files containing a
string, and returns whatever the index holds, which for these strings is
dominated by recently generated derivative repositories. Repository search sorted
by stars (q-github-04 to q-github-08) selects by an independent visibility proxy
and surfaced the established implementations that code search buried. Both are
reported because the contrast is itself a finding about where retail definitions
live.
```text q-github-01
def support_resistance language:python
```
```text q-github-02
"order_block" language:python
```
```text q-github-03
"value_area" "point of control" language:python
```
```text q-github-04
support-resistance in:name
```
```text q-github-05
smart-money-concepts in:name
```
```text q-github-06
market-profile in:name language:python
```
```text q-github-07
pivot points indicator in:name,description language:python
```
```text q-github-08
order-block detection in:name,description
```
### 3.5 Direct source retrieval

Neither GitHub search API returns file bodies. These two rows are the retrievals
of the files that were actually read.
```text q-github-src-09
curl -sL https://raw.githubusercontent.com/{repo}/{default-branch}/{path} for the seven paths listed below
```
```text q-github-src-10
curl -sL https://raw.githubusercontent.com/RouZuoMong2003/SmartMoneyConcepts-LuxAlgo/main/SmartMoneyConcepts_LuxAlgo.pine
```
### 3.6 Web search, vendor and trade sources
```text q-websearch-01
Pine Script "ta.pivothigh" definition "leftbars" "rightbars" returns price of the pivot high point
```
```text q-websearch-02
CME Group Market Profile TPO value area 70% one standard deviation Steidlmayer handbook definition
```
```text q-websearch-03
ICT "order block" original definition "last down candle before" operational rule Inner Circle Trader
```
### 3.7 Vendor documentation fetches
```text q-webfetch-tv-pivots
https://www.tradingview.com/support/solutions/43000521824-pivot-points-standard/
```
```text q-webfetch-tv-volumeprofile
https://www.tradingview.com/support/solutions/43000502040-volume-profile/
```
```text q-webfetch-tv-pineref
https://www.tradingview.com/pine-script-reference/v6/#fun_ta.pivothigh
```
<!-- prisma-s-9 -->
**No date limits, no language limits, and no publication-type limits were
applied.** Three restrictions were applied and are stated affirmatively because
they are limits in PRISMA-S terms even though they are not fields on a form:

1. **Row limits.** Every API query capped returned records at between 3 and 15.
   This is the binding limit in this review. The Crossref total-hit counts in the
   logs run to seven figures for the topical queries, because Crossref
   `query.bibliographic` is a relevance-ranked full-text match with no controlled
   vocabulary, and the tail is noise. The consequence is real and is not softened
   here: recall for the topical Crossref strategy is the recall of the top 6 to 10
   relevance-ranked hits, and nothing below that rank was seen.
2. **arXiv category restriction** to `q-fin*` on eight of eighteen queries, as
   described in section 3.3.
3. **Language of the query, not of the record.** All queries were issued in
   English. Records in other languages were eligible and one was included
   (khairov2025, in Russian, from a Tomsk State University journal); it was
   retrieved because its title carries an English translation in Crossref. A
   record whose metadata is entirely non-English would not have been retrieved by
   any query above. This is a real language limit imposed at the query end rather
   than the eligibility end, and it is not measurable from inside the review.

No controlled vocabulary was available on any source. Crossref, arXiv and GitHub
have no thesaurus; there is no MeSH or Emtree analogue for market microstructure.
The Cochrane Handbook chapter 4 requirement to combine controlled vocabulary with
free text is therefore unsatisfiable here, and the strategy is free-text only.
That is a structural weakness of every literature search in this domain, and the
compensation used is the deliberate synonym sweep visible in section 3.1: level,
barrier, clustering, discreteness, profile, value area, pivot, range, block,
zone, channel, pinning.

<!-- prisma-s-10 -->
No published search filters were used. No validated search filter exists for
market microstructure, technical analysis or price-level detection; the published
filter literature is clinical and methodological (study-design filters, RCT
filters, diagnostic-accuracy filters) and none transfers to this corpus.

<!-- prisma-s-11 -->
No search strategy was adapted or reused from a prior published review. The
strategy design does reuse a project-internal precedent: the source table shape,
the verbatim-capture-at-execution rule, and the known-item batching pattern are
carried over from
[lit_review_regime-classification_2026-08-21.md](lit_review_regime-classification_2026-08-21.md).
That review recorded a defect - twenty-five Crossref query strings lost because
they were not written to the log at execution time - and the remedy adopted here
is the single-write rule described in section 3. This review therefore fixes the
specific PRISMA-S 7 failure its predecessor reported.

<!-- prisma-s-12 -->
No search updates are scheduled and no email alerts were set. The search is a
single-day snapshot, 2026-08-21. Two properties of this corpus make the snapshot
age unevenly and both are stated: the peer-reviewed component is stable and will
age slowly; the GitHub and TradingView components are volatile, because
repositories are renamed, force-pushed and deleted, and a published script can be
edited in place with no version record. The commit hashes of the retrieved files
were **not** captured, only the default-branch content - a provenance weakness
recorded in section 10.1. Any rerun should pin by commit SHA.

<!-- prisma-s-13 -->
Date of last search, per strategy: Crossref topical and title-field, 2026-08-21;
Crossref known-item, 2026-08-21; arXiv, 2026-08-21; GitHub code and repository
search, 2026-08-21; GitHub raw source retrieval, 2026-08-21; web search,
2026-08-21; vendor documentation fetches, 2026-08-21. All strategies were
executed in a single session and every `date_searched` value in the section 2
table is 2026-08-21. No strategy was executed on any other date.

## 4. Peer review of the strategy

<!-- prisma-s-14 -->
**Not peer reviewed.** No PRESS 2015 review by an information specialist was
performed, and no second agent re-derived the strategy adversarially. The three
PRESS elements that can be self-assessed are reported, with the assessment marked
as self-assessment and therefore weak evidence:

- *Translation of the research question.* The question decomposes into a
  construct term (level, support, resistance, zone, range, band, block, channel),
  a confound term (round number, clustering, tick size, discreteness, grid,
  strike), and an evaluation term (test, null, detection, algorithm). Section 3.1
  crosses the first two systematically and the third opportunistically. The third
  axis is under-searched, and the null-attached column in sections 8.1
  to 8.5 is empty for most rows as a result.
- *Boolean and proximity operators.* Crossref exposes neither. `query.bibliographic`
  and `query.title` are relevance-ranked bag-of-words fields with no operator
  support, so no Boolean structure could be expressed on the source that supplied
  most records. arXiv does support Boolean and it was used. This asymmetry means
  the Crossref strategy is materially weaker than the arXiv strategy, and most of
  the corpus came from the weaker one.
- *Spelling, syntax, line numbers.* Checked at execution by the fact that every
  query returned a non-error response with a plausible hit count; two queries with
  obvious keyword-drift results (q-crossref-13 returning monetary-economics
  records for "smart money", q-crossref-16 returning literary works for "swing
  low") were left in the record rather than silently re-run, and their yield is
  reported as zero in section 6.

## 5. Managing records

<!-- prisma-s-15 -->
Total records identified per source are the `n_records` column of the section 2
table; they sum to 436. No source is represented outside that table. Records were
never held in a reference manager: each query wrote a JSON or Atom log to
`docs/literature/search_logs/level-definitions/` at execution time, and screening
was performed against those logs.

<!-- prisma-s-16 -->
Deduplication was two-stage and is enumerated record by record in
`docs/literature/search_logs/level-definitions/dedup-ledger.json`.

- **Stage 1, automated, exact identifier match.** Case-folded DOI for Crossref
  records; arXiv identifier with the version suffix stripped for arXiv records;
  `repo/path` for GitHub records. Software: Python 3.11 standard library set
  operations, executed in this session; no reference-manager deduplication was
  used, and no commercial deduplication tool was available. **398** of the 436
  identified records carry such an identifier; they resolve to **387** distinct
  identifiers, so stage 1 removed **11** duplicate instances.
- **Stage 2, manual, same work under a different identifier.** Three patterns:
  a working paper or preprint superseded by its published version (SSRN, NBER and
  arXiv records against journal DOIs); the same book chapter carried under several
  DOIs across editions or publisher platforms; and one arXiv-to-conference pair.
  **35** further records were removed, enumerated as 29 groups in the ledger with
  the retained identifier named for each. Stage 2 is a single-screener judgement
  and is the weakest step in the flow accounting.

Total duplicates removed: **46**. Records removed as duplicates are not eligible
for the item-16b near-miss table, which lists works excluded on eligibility
grounds.

<!-- prisma-2020-8 -->
PRISMA 2020 item 8, selection process. An LLM screener is an automation tool in
the item's own terms and is named here with its version.

- **screeners_n**: 1
- **independent**: no - single screener; no independent duplicate screening was
  performed, and no agreement statistic is reported, for the reason given in
  section 1.4
- **automation_tools**: Claude Opus 5 (model id `claude-opus-5`), running as the
  `research-librarian` agent under Claude Code / Claude Agent SDK. It decided
  every inclusion and exclusion, extracted every definition and every parameter
  value, read the seven Python source files and the one Pine source file in full,
  and assigned every taxonomy class in section 8.6. No other automation - no
  machine-learning classifier, no active-learning screener, no LLM-assisted
  ranking tool - was used at any stage.

Screening was single-stage on the metadata available in the logs (title,
container, abstract where Crossref supplied it) followed by full-text or
full-source assessment for every record that survived. For code records the
"full text" is the source file: a repository was never included on the strength of
its README, and two repositories that describe themselves as computing support and
resistance were excluded after reading the code, because what they compute is a
moving-average crossover.
## 6. Excluded records

<!-- prisma-2020-16b -->
Records that appeared to meet the inclusion criteria on their metadata and were
excluded after full assessment, with a reason each. This is not the full
exclusion list - 309 records were excluded in total - but the near-misses, which
are the ones a reader could reasonably expect to find in the corpus. Bulk
exclusions by category are summarised after the table.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| E1 | Anatomy of the retest in the QQQ opening range breakout (2026), doi:10.2139/ssrn.6745958 | full-text | Profitability evaluation of a retest rule. The opening-range definition it uses is not stated independently and appears identical to the one already included at doi:10.1016/j.frl.2012.09.001. Excluded under inclusion criterion 1 (profitability only, no locating rule). |
| E2 | Regime-conditional alpha in SPY 0DTE opening range breakout strategies (2026), doi:10.2139/ssrn.6355218 | full-text | Strike selection and filtering study; no level-locating rule stated. |
| E3 | Enhancing opening range breakout strategies with LSTM-based true range prediction (2026), doi:10.1007/978-981-92-0074-0_23 | full-text | Forecasting model applied to an already-defined range; contributes no definition. |
| E4 | Uji efektivitas metode breakout support resistance untuk probabilitas pada foreign exchange market (2024), doi:10.36985/saj8g536 | full-text | Effectiveness test of a breakout method. Full text was not retrievable and the retrieved metadata states an outcome without stating how the support and resistance levels are located, so no operational definition could be extracted. |
| E5 | A simple trading strategy with a stop-loss and take-profit order (2025), doi:10.2139/ssrn.5859402 | full-text | The levels here are strategy parameters chosen by the trader, not features estimated from the market. Out of scope by the definition in section 1.2. |
| E6 | Pricing a financial instrument: the economic value of the stop-loss order (2026), doi:10.2139/ssrn.7266458 | full-text | As E5. |
| E7 | Mid-price prediction in a limit order book (2015), doi:10.2139/ssrn.2544361 | title/abstract | Prediction of the mid-price; no price level is located. |
| E8 | Price impact cost modeling in a limit order book market (2007), doi:10.2139/ssrn.968295 | title/abstract | Cost model; no level. |
| E9 | Round numbers as goals (2010), doi:10.1177/0956797610391098 | full-text | Round-number psychology, but the outcome variables are athletic and test-score performance. No price axis, no locating rule. Retrieved by q-crossref-10 and genuinely near-miss on the confound axis. |
| E10 | Round numbers (1958), *Western Folklore*, doi:10.2307/1496200 | title/abstract | Retrieved in error by a title-field query; unrelated field. |
| E11 | Round numbers (1988), *Language in Society*, doi:10.1017/s0047404500012781 | title/abstract | Retrieved in error; unrelated field. |
| E12 | Index numbers and stock market indexes (1999), doi:10.1142/9789812816214_0019 | title/abstract | Index-number theory, not price levels; retrieved by keyword collision on "index" and "numbers". |
| E13 | Zigzag pixel indicator based secret data hiding method (2013), doi:10.1109/iccic.2013.6724286 | title/abstract | Steganography; retrieved by collision on "zigzag indicator". |
| E14 | Swing low (1945), *Phylon*, doi:10.2307/272503 | title/abstract | Retrieved in error by q-crossref-16; the query returned literary and musical works for the whole first page, which is reported in section 4 rather than hidden. |
| E15 | Price clustering asymmetries in limit order flows (2015), doi:10.2139/ssrn.2613532 | full-text | A genuine near-miss and the hardest call in this table. It bears directly on the confound axis, but it is an unrefereed working paper whose full text was not retrieved, and its clustering definition could not be extracted from metadata alone. Excluded rather than included on an unverified extraction. Recorded here so the decision is visible and reversible. |
| E16 | Round number price barriers in U.S. stock market (2018), doi:10.2139/ssrn.3187548 | full-text | As E15: on topic, working-paper tier, full text not retrieved, no locating rule extractable from the deposited metadata. The three peer-reviewed records at doi:10.2307/2331416, doi:10.1080/758526902 and doi:10.1016/s0927-5398(97)00024-8 cover the same definition with their apparatus visible. |
| E17 | Behavioral finance research of the Tehran Stock Exchange by mathematical round numbers (2023), doi:10.31838/rna/2023.06.01.011 | title/abstract | Applies an existing round-number definition to a new market; adds no definition and no null. |
| E18 | Proximity bias leading to psychological barriers in Pakistani stock market at index level (2020), doi:10.2139/ssrn.3683099 | title/abstract | As E17. |
| E19 | Optimal prediction of resistance and support levels, SSRN preprint version | deduplication-adjacent | Not excluded on eligibility: the published version at doi:10.1080/1350486x.2017.1297729 is included. Listed here only because a reader searching for the preprint should know it was seen and mapped. |
| E20 | Two GitHub repositories describing themselves as support-and-resistance detectors (repository names withheld; paths in the q-github-01 log) | full-source | Read in full. What the code computes is a moving-average crossover in one case and a fixed percentage offset from the last close in the other. Neither locates a level in any sense used in this review. This is the reason repository search by stars was added as a second strategy. |

**Bulk exclusions, by reason.** Of 390 screened records, 309 were excluded:
approximately 190 were retrieved-in-error keyword collisions, concentrated in
q-crossref-06 (auction, profile, value), q-crossref-13 (smart money, liquidity,
block), q-crossref-16 (swing high, swing low), q-crossref-20 (Wyckoff,
accumulation, distribution), q-crossref-22 (supply, demand, zone), q-arxiv-08
(barrier options) and q-arxiv-14 (order block in numerical linear algebra and in
network science); approximately 70 were method or application records with no
level-locating content, mostly limit-order-book forecasting and option pricing;
approximately 30 were GitHub repositories whose level routine was a wrapper
around an already-included algorithm or was absent; and approximately 19 were
trade or vendor pages superseded by a better source for the same definition.
These counts are approximate by category and exact only in total, because
category was recorded as a screening note rather than as a coded field - a
data-collection weakness recorded in section 10.3.

## 7. Included corpus

<!-- included-corpus -->
81 records, every one carrying a persistent identifier (FAIR F1) and every DOI
resolved live at gate time. The machine-readable form is the CSL-JSON store;
this table is the human-readable index.

**How to read the role column.** The leading letter is the group from section
1.3: A prior-period arithmetic, B extrema of the realised path, C clustering or
density over the price axis, D volume or time distribution over the price axis,
E order-book state, F exogenous grids, G volatility-scaled bands, H candle
geometry. `Dnn` is the definition identifier used in sections 8.1 to 8.6. The
bracketed flag is the **verification depth**, and it is the most important column
in this table:

- `abstract-verified` - the abstract was retrieved at execution time (Crossref
  deposit, or OpenAlex backfill logged as gap-openalex-abstracts) and every
  statement made about the record in section 8 is traceable to that text or to
  the record's title and venue. **Full texts were not obtained.**
- `metadata-only` - title, venue, year and DOI were verified by live resolution;
  **no content was retrieved at all.** These records are pointers. No claim in
  section 8 rests on a `metadata-only` record alone, and where one is the only
  support for a statement the statement is marked unverified.

Neither flag means the full text was read. **No full text was read in this
review.** The only sources read in full are the eight source files of
q-github-src-09 and q-github-src-10 and the two vendor pages of
q-webfetch-tv-pivots and q-webfetch-tv-volumeprofile, and those are not corpus
records because they have no persistent identifier. That inversion - the deepest
reading is on the lowest-tier sources - is the central limitation of this review
and is restated in section 10.3.

| id | citation | persistent id | role in the argument |
|---|---|---|---|
| aggarwal2006jrfe20060400 | Aggarwal & Lucey (2006). Psychological barriers in gold prices?. *Review of Financial Economics*. | 10.1016/j.rfe.2006.04.001 | F — barriers in gold, same family as D47. [abstract-verified] |
| anon2001cbo978051175 | (no author in record) (2001). Brownian local time. *Brownian Motion*. | 10.1017/cbo9780511750489.009 | N/A — Brownian local time and the occupation measure. Not a level definition: it is the null-side object that branch 1 needs, and the reason the dip test is invalid on integrated price. Metadata-only. [metadata-only] |
| anon2007978142001314 | (no author in record) (2007). Support and Resistance. *Technical Analysis of Stock Trends, Ninth Edition*. | 10.1201/9781420013146.ch13 | B — D-name the founding practitioner statement of support and resistance in the technical-analysis canon. Metadata-only; the chapter text was not retrieved and no locating rule from it is asserted here. [metadata-only] |
| anon2010978111853156 | (no author in record) (2010). TD Range Projection, TD Range Expansion Breakout, and TD Channels. *DeMark Indicators*. | 10.1002/9781118531563.ch9 | A — D22 TD range projection, range expansion breakout and TD channels. Metadata-only; no rule asserted. [metadata-only] |
| anon2012978111866243 | (no author in record) (2012). Point and Figure Fundamentals. *Point and Figure Charting*. | 10.1002/9781118662434.ch2 | F — D55 point and figure; the retrieved text confirms price-only inputs and no volume, and does not state the box-size rule. [abstract-verified] |
| anon2012978111919670 | (no author in record) (2012). Market Update. *Markets in Profile*. | 10.1002/9781119196709.app1 | D — Market Profile and auction-market theory, bracketing versus trend. The corpus source for the tradition that produced D32-D36; the 70% value area is not stated in the retrieved text. [abstract-verified] |
| anon2012978111919857 | (no author in record) (2012). Support and Resistance. *Stop and Make Money*. | 10.1002/9781119198574.ch16 | B — practitioner statement that support and resistance are levels where buyers and sellers reappear, that they invert on breach, and that sloped versions are trend lines and channels. Verified from the chapter abstract; no numeric rule is given. [abstract-verified] |
| anon2012978111920260 | (no author in record) (2012). Tight Trading Ranges. *Trading Price Action Trading Ranges*. | 10.1002/9781119202608.ch22 | B — D64 tight trading range as a practitioner construct; the retrieved text is explicitly non-numeric about its bounds. [abstract-verified] |
| anon2012978111920421 | (no author in record) (2012). Fibonacci and Elliott Wave. *Essentials of Technical Analysis for Financial Markets*. | 10.1002/9781119204213.ch11 | A — D11 Fibonacci retracement and Elliott wave; the retrieved text confirms the tradition and does not state the ratio set, which is taken from vendor documentation. [abstract-verified] |
| anon2012978111920442 | (no author in record) (2012). Average True Range (ATR). *12 Simple Technical Indicators*. | 10.1002/9781119204428.ch9 | G — D58 the true range and its average, stated verbatim, and its use to build a channel by adding to or subtracting from a prior close or open. The width primitive behind D58-D63. [abstract-verified] |
| anon2012978111920462 | (no author in record) (2012). Chart Patterns: Building Blocks Of Technical Analysis. *Trend Forecasting With Intermarket Analysis*. | 10.1002/9781119204626.ch3 | B — chart patterns as building blocks; scope only. [abstract-verified] |
| anon2012978111920780 | (no author in record) (2012). Donchian Channels. *Trading Regime Analysis*. | 10.1002/9781119207801.ch15 | G — D59 Donchian channel in a trend-regime context; the retrieved text does not state the highest-high, lowest-low rule, so the rule is recorded as not obtained. [abstract-verified] |
| anon2016978111920480 | (no author in record) (2016). Moving Average Envelopes and Bollinger Bands. *Technical Analysis and Chart Interpretations*. | 10.1002/9781119204800.ch17 | G — D56, D57 Bollinger Bands as a 20-period moving average with bands at two standard deviations, and moving-average envelopes at a fixed offset. The band width is a fitted dispersion, not a grid. [abstract-verified] |
| anon2020978111929559 | (no author in record) (2020). Pivot Point Moving Average System. *Candlestick and Pivot Point Trading Triggers*. | 10.1002/9781119295594.ch6 | A — D01-D06 practitioner pivot-point tradition; the chapter abstract confirms the moving-average system but not the pivot formulas, which are taken from vendor documentation instead. [abstract-verified] |
| avellaneda2003301 | Avellaneda & Lipkin (2003). A market-induced mechanism for stock pinning. *Quantitative Finance*. | 10.1088/1469-7688/3/6/301 | F — D52 a mechanism for pinning: delta-hedging drives price to the strike. A level with a derived, non-round, exogenous location. [abstract-verified] |
| avellaneda2012cpa21404 | Avellaneda et al. (2012). Mathematical Models for Stock Pinning near Option Expiration Dates. *Communications on Pure and Applied Mathematics*. | 10.1002/cpa.21404 | F — D52 mathematical models of pinning near expiration. Metadata-only. [metadata-only] |
| baryam2014arxiv1402091 | Bar-Yam et al. (2014). The $500.00 AAPL close: Manipulation or hedging? A quantitative analysis. | 10.48550/arXiv.1402.0910 | F — D52 the 500.00 AAPL close: a quantitative test discriminating hedging from manipulation at a round strike. Preprint tier. [abstract-verified] |
| bhattacharya2012mnsc11101364 | Bhattacharya et al. (2012). Penny Wise, Dollar Foolish: Buy–Sell Imbalances On and Around Round Numbers. *Management Science*. | 10.1287/mnsc.1110.1364 | F — D51 buy-sell imbalance one penny below and above round numbers, monotone in roundness. The strongest evidence that the level is the number itself and that it sits at a tick offset from it. Class R with a Class T component. [abstract-verified] |
| blau2016jjbusres2016 | Blau & Griffith (2016). Price clustering and the stability of stock prices. *Journal of Business Research*. | 10.1016/j.jbusres.2016.06.008 | F — clustering and price stability. Metadata-only. [metadata-only] |
| blau2019s23826266205 | Blau & Whitby (2019). Rethinking Decimalization: The Impact of Increased Tick Sizes on Trading Activity, Volatility, and Price Clustering. *Market Microstructure and Liquidity*. | 10.1142/s2382626620500069 | F — tick-size increase and clustering. Class T. [abstract-verified] |
| blau2021154275602020 | Blau et al. (2021). Price Clustering, Preferences for Round Prices, and Expected Returns. *Journal of Behavioral Finance*. | 10.1080/15427560.2020.1867143 | F — round-price preference and expected returns. [abstract-verified] |
| bouchaud2002301 | Bouchaud et al. (2002). Statistical properties of stock order books: empirical results and models. *Quantitative Finance*. | 10.1088/1469-7688/2/4/301 | E — D38 average book shape and the power-law distribution of incoming limit prices relative to the current price. Class N. [abstract-verified] |
| brock1992j15406261199 | BROCK et al. (1992). Simple Technical Trading Rules and the Stochastic Properties of Stock Returns. *The Journal of Finance*. | 10.1111/j.1540-6261.1992.tb04681.x | B,C — D76 trading range break: the level is the maximum or minimum of the previous n periods. Carries four explicit null models and a bootstrap - the design branch 1 names as its fallback. [abstract-verified] |
| cartea201616m1058406 | Cartea & Jaimungal (2016). A Closed-Form Execution Strategy to Target Volume Weighted Average Price. *SIAM Journal on Financial Mathematics*. | 10.1137/16m1058406 | A,D — D10 VWAP as an execution target with a closed-form strategy; establishes VWAP as a benchmark object rather than a support level. [abstract-verified] |
| cellier2007ssrn966454 | Cellier & Bourghelle (2007). Limit Order Clustering and Price Barriers on Financial Markets: Empirical Evidence from Euronext. | 10.2139/ssrn.966454 | E — D41 limit-order clustering and price barriers on Euronext. [abstract-verified] |
| chang1999146802970046 | Chang & Osler (1999). Methodical Madness: Technical Analysis and the Irrationality of Exchange‐rate Forecasts. *The Economic Journal*. | 10.1111/1468-0297.00466 | B — head-and-shoulders as an algorithmically defined pattern; a worked precedent for turning a chart shape into a rule. [abstract-verified] |
| choi2026jribaf202610 | Choi (2026). Strong clustering and weak barriers at round numbers in Bitcoin markets. *Research in International Business and Finance*. | 10.1016/j.ribaf.2026.103494 | F — clustering strong, barriers weak, in Bitcoin - a market with no exchange-mandated tick history. Metadata-only. [metadata-only] |
| christie1994j15406261199 | CHRISTIE & SCHULTZ (1994). Why do NASDAQ Market Makers Avoid Odd‐Eighth Quotes?. *The Journal of Finance*. | 10.1111/j.1540-6261.1994.tb04782.x | F — D49 odd-eighth avoidance: the price set actually used is a coarsening of the permitted grid. Class T. [abstract-verified] |
| chung2021arxiv2101074 | Chung & Bellotti (2021). Evidence and Behaviour of Support and Resistance Levels in Financial Time Series. | 10.48550/arXiv.2101.07410 | C — D28 heuristic discovery of SR levels with bounce counting, a decay function, and an explicit comparison against AR(1) and stationarity alternatives. The one preprint that attaches something like a null. Preprint tier. [abstract-verified] |
| cole2013978111868114 | Cole & Ness (2013). Decimalization and Discreteness. *Market Microstructure in Emerging and Developed Markets*. | 10.1002/9781118681145.ch11 | F — D50 statement of the discrete price set and its regulatory history. Class T. [abstract-verified] |
| cont2010opre10900780 | Cont et al. (2010). A Stochastic Model for Order Book Dynamics. *Operations Research*. | 10.1287/opre.1090.0780 | E — Markovian model of the book by price level; supplies the reference dynamics against which a depth-peak level would have to be tested. [abstract-verified] |
| dayri2015s23826266155 | Dayri & Rosenbaum (2015). Large Tick Assets: Implicit Spread and Optimal Tick Size. *Market Microstructure and Liquidity*. | 10.1142/s2382626615500033 | F — D50 large-tick assets and the implicit spread: the tick is not a nuisance but the price-formation unit. Class T. [abstract-verified] |
| deangelis20161350486x2017 | De Angelis & Peskir (2016). Optimal prediction of resistance and support levels. *Applied Mathematical Finance*. | 10.1080/1350486x.2017.1297729 | B — D73 resistance and support as conditional median curves of a hidden aspiration level under geometric Brownian motion. A level that is derived rather than detected, with a uniqueness proof. [abstract-verified] |
| deceuster1998s09275398970 | De Ceuster et al. (1998). On the hypothesis of psychological barriers in stock markets and Benford's Law. *Journal of Empirical Finance*. | 10.1016/s0927-5398(97)00024-8 | F — the Benford's-Law critique of the barrier literature: the null used by D47-type tests is itself mis-specified. Load-bearing for section 8.6.6. Metadata-only. [metadata-only] |
| donaldson19932331416 | Donaldson & Kim (1993). Price Barriers in the Dow Jones Industrial Average. *The Journal of Financial and Quantitative Analysis*. | 10.2307/2331416 | F — D46 round-number barrier at multiples of 100 in the DJIA. The only retrieved peer-reviewed source that both defines a level purely from the decimal representation and attaches a Monte Carlo null to it. Class R. [abstract-verified] |
| dorfleitner2009jgfj20080900 | Dorfleitner & Klein (2009). Psychological barriers in European stock markets: Where are they?. *Global Finance Journal*. | 10.1016/j.gfj.2008.09.001 | F — barriers across European indices, same family as D47. Metadata-only. [metadata-only] |
| frey2009ssrn1108485 | Frey & Sandås (2009). The Impact of Iceberg Orders in Limit Order Books. *SSRN Electronic Journal*. | 10.2139/ssrn.1108485 | E — D42 iceberg orders: resting size at a price that is not observable. Metadata-only. [metadata-only] |
| golez2012jjfineco2012 | Golez & Jackwerth (2012). Pinning in the S&amp;P 500 futures. *Journal of Financial Economics*. | 10.1016/j.jfineco.2012.06.010 | F — D52 pinning in S&P 500 futures. Metadata-only. [metadata-only] |
| gould2013146976882013 | Gould et al. (2013). Limit order books. *Quantitative Finance*. | 10.1080/14697688.2013.803148 | E — survey of limit order books; the source for what a price level means in a book. [abstract-verified] |
| gould2016s23826266165 | Gould & Bonart (2016). Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book. *Market Microstructure and Liquidity*. | 10.1142/s2382626616500064 | E — D43 queue imbalance at the best quote as a one-tick-ahead predictor. Class T by construction. [abstract-verified] |
| gu2008arxiv0801371 | Gu et al. (2008). Empirical shape function of limit-order books in the Chinese stock market. *arXiv*. | 10.48550/arXiv.0801.3712 | E,D — D38 empirical LOB shape function, with periodic peaks at a period of five ticks. A direct Class T artifact in a Class N-looking statistic. Preprint tier. [abstract-verified] |
| harris199143389 | Harris (1991). Stock Price Clustering and Discreteness. *Review of Financial Studies*. | 10.1093/rfs/4.3.389 | F — D48 clustering on round fractions, with an econometric model of the discrete price set traders use. The record that makes round numbers and the tick grid separable rather than one thing. Class R and Class T jointly. [abstract-verified] |
| henderson2021arxiv2103023 | Henderson et al. (2021). The Support and Resistance Line Method: An Analysis via Optimal Stopping. | 10.48550/arXiv.2103.02331 | B — D74 three-state path-dependent model of support and resistance solved by optimal stopping. Preprint tier. [abstract-verified] |
| holmberg2013jfrl20120900 | Holmberg et al. (2013). Assessing the profitability of intraday opening range breakout strategies. *Finance Research Letters*. | 10.1016/j.frl.2012.09.001 | A — D08 opening range breakout, with the opening range defined as the extremes of a fixed initial window. Metadata-only. [metadata-only] |
| ikenberry2007j1468036x200 | Ikenberry & Weston (2007). Clustering in US Stock Prices after Decimalisation. *European Financial Management*. | 10.1111/j.1468-036x.2007.00410.x | F — clustering after decimalisation: the grid changed, the clustering did not disappear. [abstract-verified] |
| jain2024arxiv2410087 | Jain et al. (2024). No Tick-Size Too Small: A General Method for Modelling Small Tick Limit Order Books. | 10.48550/arXiv.2410.08744 | F — small-tick versus large-tick LOB stylised facts and metrics. Class T. Preprint tier. [abstract-verified] |
| kakushadze2020arxiv2006141 | Kakushadze (2020). Option Pricing: Channels, Target Zones and Sideways Markets. *arXiv*. | 10.48550/arXiv.2006.14121 | G — channels, target zones and sideways markets priced as options; a band treated as a contract boundary. Preprint tier. [abstract-verified] |
| kavajecz2004hhg057 | Kavajecz & Odders-White (2004). Technical Analysis and Liquidity Provision. *Review of Financial Studies*. | 10.1093/rfs/hhg057 | E — D39 support and resistance levels coincide with peaks in depth on the limit order book, and technical rules locate depth already in place. The pivotal Class N record: a level defined without reference to any grid. [abstract-verified] |
| khairov20259 | Khairov & Spitsyn (2025). Neural network testing of a data labeling algorithm for classifying support and resistance levels in financial markets. *Vestnik Tomskogo gosudarstvennogo universiteta. Upravlenie, vychislitel'naya tekhnika i informatika*. | 10.17223/19988605/70/9 | C — D29 an algorithmic labelling rule for SR levels, used to train a CNN-LSTM-MLP classifier. Included for the labelling rule, not for the trading result. [abstract-verified] |
| kodmalwar2024icetems64039 | Kodmalwar et al. (2024). Testing the Accuracy of Fibonacci Retracement Levels Using Artificial Intelligence. *2024 2nd International Conference on Emerging Trends in Engineering and Medical Sciences (ICETEMS)*. | 10.1109/icetems64039.2024.10964965 | A — D11 an accuracy test of Fibonacci retracement levels; the only retrieved record that tests a ratio-based level at all. [abstract-verified] |
| koedijk1994016517659490 | Koedijk & Stork (1994). Should we care? psychological barriers in stock markets. *Economics Letters*. | 10.1016/0165-1765(94)90116-3 | F — early sceptical note on barrier testing. Metadata-only. [metadata-only] |
| kriuk2026001498820000 | Kriuk et al. (2026). DeepSupp: Attention-Driven Correlation Pattern Analysis for Dynamic Time Series Support and Resistance Levels Identification. *Proceedings of the 15th International Conference on Data Science, Technology and Applications*. | 10.5220/0014988200004091 | C — D30 DeepSupp: correlation-pattern attention for dynamic SR levels. Metadata-only. [metadata-only] |
| krugman19912937922 | Krugman (1991). Target Zones and Exchange Rate Dynamics. *The Quarterly Journal of Economics*. | 10.2307/2937922 | F,G — D53 target zone: an exogenously announced band whose edges are defended, with the interior behaviour derived. The only definition in the corpus where band edges are known ex ante by construction. [abstract-verified] |
| lallouache2013arxiv1307544 | Lallouache & Abergel (2013). Tick Size Reduction and Price Clustering in a FX Order Book. *arXiv*. | 10.48550/arXiv.1307.5440 | F,E — D41 limit orders persist at the pre-reform grid after a ten-fold tick reduction, producing price barriers and peaks in the book shape at round distances. The single most useful record in the review for separating Class R from Class T. Preprint tier. [abstract-verified] |
| ley1994758526902 | Ley & Varian (1994). Are there psychological barriers in the Dow-Jones index?. *Applied Financial Economics*. | 10.1080/758526902 | F — D47 psychological barrier tested on 41 years of DJIA closes; the level is a numerical value of the index, nothing else. Class R. [abstract-verified] |
| lintonen2019jas201919117 | Lintonen & Räty (2019). Self-learning of multivariate time series using perceptually important points. *IEEE/CAA Journal of Automatica Sinica*. | 10.1109/jas.2019.1911777 | B — D19 PIP applied to multivariate series. [abstract-verified] |
| lo2000002210820026 | Lo et al. (2000). Foundations of Technical Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation. *The Journal of Finance*. | 10.1111/0022-1082.00265 | B — D21 kernel-regression smoothing then local extrema of the smoothed series as the definition of a pattern point. The canonical academic answer to how one locates a turning point without eyeballing it. [abstract-verified] |
| madhavan2010978047006160 | Madhavan (2010). Volume‐Weighted Average Price (VWAP). *Encyclopedia of Quantitative Finance*. | 10.1002/9780470061602.eqf07036 | A,D — D10 VWAP defined as a volume-weighted price average; a level with no extremum and no cluster in it. [abstract-verified] |
| meer1988003132038890 | Meer et al. (1988). Extraction of trend lines and extrema from multiscale curves. *Pattern Recognition*. | 10.1016/0031-3203(88)90056-8 | B — D20 multiscale extraction of trend lines and extrema; the pattern-recognition ancestry of the extremum-based definitions. Metadata-only. [metadata-only] |
| mitchell2001fut2 | Mitchell (2001). Clustering and psychological barriers: the importance of numbers. *Journal of Futures Markets*. | 10.1002/fut.2 | F — survey of why clustering and barriers are expected; supplies the cultural and cognitive rationale, not a locating rule. [abstract-verified] |
| mitchell2006jintfin20050 | Mitchell & Izan (2006). Clustering and psychological barriers in exchange rates. *Journal of International Financial Markets, Institutions and Money*. | 10.1016/j.intfin.2005.03.003 | F — barriers in exchange rates, same family as D47. Metadata-only. [metadata-only] |
| moinas2005ssrn676564 | Moinas (2005). Hidden Limit Orders and Liquidity in Limit Order Markets. | 10.2139/ssrn.676564 | E — D42 hidden limit orders and liquidity. [abstract-verified] |
| osler2003154062610058 | Osler (2003). Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis. *The Journal of Finance*. | 10.1111/1540-6261.00588 | E,F — D45 stop-loss and take-profit order clustering, take-profits at round numbers and stop-losses just beyond them. The mechanism that makes round-number clustering part of the construct rather than a nuisance, which is exactly the question branch 1 is blocked on. [abstract-verified] |
| osler2005jjimonfin200 | Osler (2005). Stop-loss orders and price cascades in currency markets. *Journal of International Money and Finance*. | 10.1016/j.jimonfin.2004.12.002 | E — D45 stop-loss cascades: the level is where the orders are. Metadata-only. [metadata-only] |
| park2007j14676419200 | Park & Irwin (2007). WHAT DO WE KNOW ABOUT THE PROFITABILITY OF TECHNICAL ANALYSIS?. *Journal of Economic Surveys*. | 10.1111/j.1467-6419.2007.00519.x | C — survey placing D76 and its relatives in the evaluation literature; used only for scope, not for any performance claim. [abstract-verified] |
| phetking2009coginf200952 | Phetking et al. (2009). Identifying Zigzag based Perceptually Important Points for indexing financial time series. *2009 8th IEEE International Conference on Cognitive Informatics*. | 10.1109/coginf.2009.5250725 | B — D19 zigzag-based perceptually important points; explicit statement that generic dimensionality reduction destroys the points a level definition needs. [abstract-verified] |
| racorean2013arxiv1304684 | Racorean (2013). Time-independent pricing of options in range bound markets. | 10.48550/arXiv.1304.6846 | G — option pricing in range-bound markets; the range is exogenous. Preprint tier. [abstract-verified] |
| richards2012arxiv1210721 | Richards et al. (2012). Heavy-Tailed Features and Empirical Analysis of the Limit Order Book Volume Profiles in Futures Markets. | 10.48550/arXiv.1210.7215 | D — D37 heavy-tailed LOB volume profiles by book level. Preprint tier. [abstract-verified] |
| rosen2024ssrn5007093 | Rosen & Spaenjers (2024). Trading at Round Numbers. | 10.2139/ssrn.5007093 | F — trading at round numbers; working paper. Metadata-only, no abstract deposited. [metadata-only] |
| s2016ijci20165107 | S & P (2016). Opening Range Breakout Stock Trading Algorithmic Model. *International Journal on Cybernetics &amp; Informatics*. | 10.5121/ijci.2016.5107 | A — D08 opening range breakout stated as an algorithm. [abstract-verified] |
| selamat2010jcssp2010138 | Selamat (2010). Index Financial Time Series Based on Zigzag-Perceptually Important Points. *Journal of Computer Science*. | 10.3844/jcssp.2010.1389.1395 | B — D19 zigzag-PIP indexing. [abstract-verified] |
| sonnemans2006jeuroecorev2 | Sonnemans (2006). Price clustering and natural resistance points in the Dutch stock market: A natural experiment. *European Economic Review*. | 10.1016/j.euroecorev.2005.09.001 | F — D54 natural-experiment identification of a round-number level via currency redenomination. The one design in the corpus that can separate the number from the price. Metadata-only. [metadata-only] |
| sullivan1999002210820016 | Sullivan et al. (1999). Data‐Snooping, Technical Trading Rule Performance, and the Bootstrap. *The Journal of Finance*. | 10.1111/0022-1082.00163 | C — the data-snooping correction to D76 and its rule universe; the reality-check apparatus for a definition family. [abstract-verified] |
| tran2022arxiv2203079 | Tran et al. (2022). How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective. | 10.48550/arXiv.2203.07922 | E — information content of the book beyond the best levels. Preprint tier. [abstract-verified] |
| tsai2019access201928 | Tsai et al. (2019). Assessing the Profitability of Timely Opening Range Breakout on Index Futures Markets. *IEEE Access*. | 10.1109/access.2019.2899177 | A — D08 opening range on index futures, with the window length treated as a tunable. [abstract-verified] |
| tsinaslanidis2014jeswa2014040 | Tsinaslanidis & Kugiumtzis (2014). A prediction scheme using perceptually important points and dynamic time warping. *Expert Systems with Applications*. | 10.1016/j.eswa.2014.04.028 | B — D19 PIP with dynamic time warping. Metadata-only. [metadata-only] |
| wang2010bife201076 | Wang et al. (2010). A Nonparametric Kernel Regression Method for the Recognition of Visual Technical Patterns in China's Stock Market. *2010 Third International Conference on Business Intelligence and Financial Engineering*. | 10.1109/bife.2010.76 | B — D21 replication of the kernel-regression pattern definition on Chinese equities. [abstract-verified] |
| xiaoyanni2005jjfineco2004 | XIAOYANNI et al. (2005). Stock price clustering on option expiration dates. *Journal of Financial Economics*. | 10.1016/j.jfineco.2004.08.005 | F — D52 stock price clustering at option strikes on expiration dates. Metadata-only. [metadata-only] |
| xu2019arxiv1907062 | Xu et al. (2019). Multi-Level Order-Flow Imbalance in a Limit Order Book. | 10.48550/arXiv.1907.06230 | E — D44 multi-level order-flow imbalance. Preprint tier. [abstract-verified] |
| yap2022s24247863225 | Yap et al. (2022). Can exchange-traded funds be profitably traded with the trading range breakout technical trading rule?. *International Journal of Financial Engineering*. | 10.1142/s242478632250027x | B — D76 applied and extended with a volatility-scaled variant. [abstract-verified] |
| zovko2002308 | Zovko & Farmer (2002). The power of patience: a behavioural regularity in limit-order placement. *Quantitative Finance*. | 10.1088/1469-7688/2/5/308 | E — D40 relative limit price distribution, power law over a few ticks to about 2000 ticks. Class N in construction, measured in tick units. [abstract-verified] |

### 7.1 Preprint-tier records (charter evidence-tier flag)

The charter requires that evidence tier travel with the claim and that no
artifact treat a preprint-tier row as settled. Eleven included records are
arXiv preprints with no located refereed version:
`10.48550/arXiv.2101.07410`, `10.48550/arXiv.2103.02331`,
`10.48550/arXiv.1307.5440`, `10.48550/arXiv.2410.08744`,
`10.48550/arXiv.1402.0910`, `10.48550/arXiv.0801.3712`,
`10.48550/arXiv.2006.14121`, `10.48550/arXiv.1304.6846`,
`10.48550/arXiv.1210.7215`, `10.48550/arXiv.1907.06230`,
`10.48550/arXiv.2203.07922`. Two of these -
`10.48550/arXiv.1307.5440` and `10.48550/arXiv.2101.07410` - carry more weight in
section 8 than any other preprint, and both are flagged again at the point of use.

Four further records are working papers on SSRN with no located refereed version:
`10.2139/ssrn.966454`, `10.2139/ssrn.1108485`, `10.2139/ssrn.676564`,
`10.2139/ssrn.5007093`.

### 7.2 Practitioner and trade-press records that carry a DOI

Twelve included records are book chapters from the technical-analysis trade
literature that happen to carry publisher DOIs:
`10.1201/9781420013146.ch13`, `10.1002/9781119198574.ch16`,
`10.1002/9781119295594.ch6`, `10.1002/9781119196709.app1`,
`10.1002/9781118662434.ch2`, `10.1002/9781119204800.ch17`,
`10.1002/9781119204428.ch9`, `10.1002/9781119207801.ch15`,
`10.1002/9781119202608.ch22`, `10.1002/9781118531563.ch9`,
`10.1002/9781119204213.ch11`, `10.1002/9781119204626.ch3`.

They are **tier 5 under the CLAUDE.md hierarchy** and are in the corpus only
because the task directive requires retail and vendor definitions to be tiered
rather than excluded, and because a persistent identifier makes them citable. A
DOI is a locator, not a warrant. Nothing in section 8 treats a claim about
markets from one of these records as established; they are used only as evidence
about what the tradition asserts.

### 7.3 Definition sources with no persistent identifier

These are not corpus records - FAIR F1 forbids it - but they carry most of the
operational weight in section 8, because they are the only sources in this review
that were read in full. They are logged verbatim in the search logs and are cited
in section 8 by log identifier.

| source | what was read | tier | log |
|---|---|---|---|
| `day0market/support_resistance` | `pricelevels/cluster.py`, `pricelevels/scoring/touch_scorer.py` | 4 (published code) | q-github-src-09 |
| `BatuhanUsluel/Algorithmic-Support-and-Resistance` | `SupportAndResistance.py` | 4 | q-github-src-09 |
| `judopro/Stock_Support_Resistance_ML` | `find_support_resistance_kmeans.py` | 4 | q-github-src-09 |
| `bfolkens/py-market-profile` | `src/market_profile/__init__.py` | 4 | q-github-src-09 |
| `GregoryMorse/trendln` | `trendln/__init__.py` | 4 | q-github-src-09 |
| `joshyattridge/smart-money-concepts` | `smartmoneyconcepts/smc.py` | 4 | q-github-src-09 |
| TradingView published script *Smart Money Concepts [LuxAlgo]* | `SmartMoneyConcepts_LuxAlgo.pine`, Pine v5, 848 lines, via CC BY-NC-SA mirror | 4 (published script source) | q-github-src-10 |
| TradingView Help Center, Pivot Points Standard | all six pivot formula sets, verbatim | 2 (vendor documentation, for what the vendor computes) | q-webfetch-tv-pivots |
| TradingView Help Center, Volume Profile | POC, value-area algorithm, 70% default, VAH/VAL | 2 (vendor documentation) | q-webfetch-tv-volumeprofile |
| Pine Script `ta.pivothigh` / `ta.pivotlow` | signature and semantics, from secondary restatement only | 5 (vendor reference did not render) | q-websearch-01, q-webfetch-tv-pineref |
| ICT order block | the last-opposing-candle rule, from ten secondary restatements | 5 | q-websearch-03 |
| Market Profile 70% value area | the rule and the one-standard-deviation rationale, from ten secondary restatements | 5 | q-websearch-02 |

## 8. Synthesis

### 8.0 How to read this section

**76 distinct definitions** were located. Each carries an identifier `D01` to
`D76`, stable across this document. Sections 8.1 to 8.5 give them in full with
the six fields the task requires: the operational statement, the inputs, whether
the output is a line or a band and what sets the band width, the relationship to
the two confounds, the source and its evidence tier, and whether any null
distribution, test or falsification has ever been attached. The last of those
fields is tallied in section 8.6.6. Section 8.6 is the taxonomy. Section 8.7
lists the definitions for which no operational statement could be found at all.

**The classification test.** Class assignment is not a judgement about intent. It
is the outcome of one operation, stated here so it is checkable and so a
disagreement about a class is a disagreement about a computation:

> Let `L(p)` be the set of level locations a definition returns on a price path
> `p`. Apply the affine re-denomination `p -> a*p + b`, with `a > 0` not a power
> of ten and `b` not an integer multiple of the tick.
>
> - **Class N** if `L(a*p + b) = a*L(p) + b`. The definition is equivariant; it
>   sees only the geometry of the path, not the labels on the axis.
> - **Class R** if equivariance fails because the rule reads the decimal digits
>   of the price.
> - **Class T** if equivariance fails because the rule reads the minimum price
>   increment, or is undefined when price is continuous.

Two refinements are needed and both are reported rather than hidden:

- **N-X.** A definition can be equivariant and still not be a function of the
  path, because it is anchored to an exogenous institutional level that is
  neither round nor tick-derived - an option strike, an announced policy band.
  Under the literal test these are Class N. For surrogate design they behave
  nothing like the rest of Class N, so they are flagged `N-X` and counted
  separately inside N.
- **Affine-defective.** Several Class N definitions are equivariant under scaling
  but not under translation, because a tolerance is expressed as a percentage of
  price rather than as a percentage of a range or a multiple of a dispersion.
  Such a rule silently treats the zero of the price scale as meaningful. It is
  still Class N - it does not read digits or ticks - but the defect is recorded,
  because it makes the definition depend on the instrument's price level in a way
  its author almost certainly did not intend.

**Provenance convention in these tables.** `code` means the statement was
extracted by reading the executable source, cited by repository and file.
`vendor` means it was extracted verbatim from vendor documentation. `abstract`
means it comes from a retrieved abstract of a corpus record. `tier-5` means it
comes from secondary restatement only. A definition with no provenance marker of
the first three is not one this review can vouch for, and is marked as such.

### 8.1 Definitions that locate a line

#### 8.1.1 Group A - prior-period arithmetic

Every formula in D01 to D06 was read verbatim from TradingView Help Center,
Pivot Points Standard (log `q-webfetch-tv-pivots`). The vendor states the period
rule verbatim: "The 'current' and 'previous' values refer to the current and
previous bar of the timeframe selected in the 'Pivots Timeframe' option."

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D01 | Traditional pivots. `P = (prevHigh + prevLow + prevClose)/3`; `R1 = 2P - prevLow`; `S1 = 2P - prevHigh`; `R2 = P + (prevHigh - prevLow)`; `S2 = P - (prevHigh - prevLow)`; `R3 = 2P + (prevHigh - 2*prevLow)`; `S3 = 2P - (2*prevHigh - prevLow)`; `R4`, `R5`, `S4`, `S5` extend the pattern with coefficients 3 and 4 | prior period H, L, C | eleven lines, no band | **N.** Every expression is affine in prices; `L(a*p+b) = a*L(p)+b` holds exactly | vendor, tier 2 for what is computed / tier 5 as a market claim | none |
| D02 | Classic pivots. Same `P`; `R2 = P + (prevHigh - prevLow)`, `R3 = P + 2*(prevHigh - prevLow)`, `R4 = P + 3*(prevHigh - prevLow)`, mirrored for S | prior period H, L, C | nine lines | **N** | vendor | none |
| D03 | Fibonacci pivots. Same `P`; `R1 = P + 0.382*(prevHigh - prevLow)`, `R2 = P + 0.618*(...)`, `R3 = P + (...)`, mirrored | prior period H, L, C | seven lines | **N**. The 0.382 and 0.618 constants are unsourced in every retrieved record and are `CONVENTION` | vendor | none |
| D04 | Woodie pivots. `P = (prevHigh + prevLow + 2*currOpen)/4`; `R1 = 2P - prevLow`; `R3 = prevHigh + 2*(P - prevLow)`; `R4 = R3 + (prevHigh - prevLow)`, mirrored | prior H, L and **current open** | nine lines | **N**. Note the causal-time property: it uses the current period's open, so it is not computable before the period starts | vendor | none |
| D05 | DeMark pivots. `X = prevHigh + prevLow + 2*prevClose` if `prevOpen == prevClose`; `X = 2*prevHigh + prevLow + prevClose` if `prevClose > prevOpen`; else `X = 2*prevLow + prevHigh + prevClose`. Then `P = X/4`, `R1 = X/2 - prevLow`, `S1 = X/2 - prevHigh` | prior O, H, L, C | three lines | **N**. The branch on `prevOpen == prevClose` is an exact float equality on a discrete price grid, so in practice the branch fires only when the grid makes it possible - a latent Class T dependence in a Class N formula, and the only one of its kind found | vendor | none |
| D06 | Camarilla pivots. `R1 = prevClose + 1.1*(prevHigh - prevLow)/12`; `/6`, `/4`, `/2` for `R2` to `R4`; **`R5 = (prevHigh/prevLow)*prevClose`**, `S5 = prevClose - (R5 - prevClose)`, mirrored | prior H, L, C | eleven lines | **N, affine-defective.** `R1` to `R4` are affine. `R5` is a *ratio* of prices and is not translation-equivariant: it changes if a constant is added to the whole price series, so it treats price zero as meaningful. The constant `1.1/12` has no source at any tier | vendor | none |
| D07 | Previous period high, low, close. Resample the bar series to the target timeframe, take `max(high)` and `min(low)` of the completed prior period; flag `BrokenHigh` once price trades through it | OHLC, calendar | two lines plus break flags | **N** | code: `joshyattridge/smart-money-concepts`, `smc.previous_high_low` | none |
| D08 | Opening range. The high and low of the first `k` minutes of the session. `k` is not fixed by any source: the reference implementation defaults to 10 minutes; the corpus records treat it as a tunable | intraday OHLC, session clock | a band whose width is whatever the first `k` minutes produced | **N** | code: `bfolkens/py-market-profile`, `MarketProfileSlice.open_range`; abstract: three corpus records | profitability tests only, never a test of the range itself |
| D09 | Initial balance. As D08 with the window fixed at the first hour | intraday OHLC, session clock | band, width endogenous | **N** | code: same file, `initial_balance`, default `1 hour` | none |
| D10 | VWAP. Volume-weighted mean of traded price over a stated window | trades, volume | one line; bands only if a dispersion is added, and no retrieved source specifies that dispersion | **N** | abstract: encyclopedia entry and an execution-strategy paper | none as a level; extensive as an execution benchmark |
| D11 | Fibonacci retracement. Given a prior swing from `A` to `B`, place lines at `B - r*(B - A)` for `r` in a ratio set. The ratio set is not stated in any retrieved corpus record; the vendor pivot page uses 0.382 and 0.618 | two chosen swing points | lines | **N**. Depends entirely on how `A` and `B` were chosen, which is a Group B problem, not a Group A one | abstract, tier 5 | one accuracy test located, in a 2024 conference paper |
| D22 | TD range projection, TD range expansion breakout, TD channels | not obtained | not obtained | **unclassified** | metadata-only | none |

**Observation on Group A.** Every one of these is Class N, and eleven of the
twelve are exactly affine-equivariant. This is the least confounded family in the
entire review, and it is also the family with the weakest provenance: not one of
D01 to D06 has a primary source anywhere in the corpus, and the constants
`0.382`, `0.618`, `1.1/12` and the `/12, /6, /4, /2` ladder appear at no tier
above vendor documentation. Under charter commitment 3 they are unlabelled
constants. They are cleanly testable and have never been tested.

#### 8.1.2 Group B - extrema of the realised path

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D12 | `ta.pivothigh(source, leftbars, rightbars)`: bar `t` is a pivot high if its value exceeds all `leftbars` values before it and all `rightbars` values after it. Returns the price, or not-a-number. Confirmed only after `rightbars` further bars | one price series | line | **N** | tier 5 restatement only; the vendor reference page did not render (see section 10.1) | none |
| D13 | Centered rolling extremum: with an **odd** window `w` (default 21), bar `t` is a peak if `price[t] == rolling_max(price, w).shift(-(w-1)/2)[t]`. The odd-window constraint is enforced by an exception in the code | one price series | line | **N** | code: `day0market/support_resistance`, `pricelevels/cluster.py`, `RawPriceClusterLevels._find_potential_level_prices` | none |
| D14 | `swing_highs_lows(ohlc, swing_length=50)`: internally `swing_length *= 2`, then a swing high is a bar whose high equals the 100-bar rolling max of highs shifted by 50 - a centered window of 100 bars. The docstring says "the highest high out of the swing_length amount of candles before and after"; the code doubles first, so the docstring and the code describe different windows | OHLC | line | **N** | code: `joshyattridge/smart-money-concepts`, `smc.swing_highs_lows` | none |
| D15 | Three-bar naive extremum: `x[t-1] > x[t] < x[t+1]` for a minimum | one series | line | **N** | code: `GregoryMorse/trendln`, `METHOD_NAIVE` | none |
| D16 | As D15 after collapsing consecutive equal values, so that a flat spot does not suppress the extremum. This is a **direct accommodation of price discreteness**: flats exist because the price grid is discrete | one series | line | **N**, but its reason for existing is Class T | code: `trendln`, `METHOD_NAIVECONSEC` | none |
| D17 | Numerical-derivative extremum: compute first and second derivatives with a finite-difference scheme of even accuracy order (default 2); a point is an extremum where the first derivative is zero or changes sign, with the closer-to-zero of the two neighbours chosen, and the second derivative fixes the type | one series | line | **N** | code: `trendln`, `METHOD_NUMDIFF`, using `findiff` | none |
| D18 | ZigZag: track the running extreme in the current direction; reverse when the retracement `abs((x[t] - curVal)/curVal)*100` reaches `minSegSize` percent (default 0.1). Pivots are the extremes at each reversal | one price series | line | **N, affine-defective.** The threshold is a percentage *of price*, so the pivot set changes if a constant is added to the series | code: `BatuhanUsluel/Algorithmic-Support-and-Resistance`, `createZigZagPoints` | none |
| D19 | Perceptually important points: recursively select the point of maximum distance from the chord joining the current endpoints, retaining the points a human reader would call the turning points. The zigzag-based variant restricts candidates to zigzag reversals | one series | line | **N** | abstract: four corpus records | none for level existence; evaluated as dimensionality reduction |
| D20 | Multiscale extraction: smooth the curve at several scales and take extrema and straight segments that persist across scales | one series | line | **N** | metadata-only | none |
| D21 | Kernel-regression pattern points: smooth the price series by nonparametric kernel regression, then take local extrema **of the smoothed series** as the pattern points; a pattern is a stated ordering of five such extrema | one price series, a bandwidth | line | **N**. The bandwidth is the whole definition: it fixes how many extrema exist. Both corpus records use a plug-in bandwidth scaled by a constant that is itself unsourced | abstract | **yes** - conditional versus unconditional return distributions, with a goodness-of-fit test |
| D64 | Tight trading range. Not obtained: the retrieved text is explicitly non-numeric about the pattern's bounds | OHLC | band | **unclassified** | abstract, tier 5 | none |
| D73 | Resistance and support as the conditional median curves of a hidden aspiration level, under geometric Brownian motion, obtained as the boundaries of an optimal-stopping problem and characterised by nonlinear integral equations | a price model, a prior on the aspiration level | two curves in time, not horizontal lines | **N** | abstract | derivation with a uniqueness proof; no empirical null |
| D74 | A three-state path-dependent model in which the stock transitions between states, with buy and sell boundaries obtained from two linked optimal-stopping problems | a price model | boundaries | **N** | abstract, preprint tier | derivation only |
| D76 | Trading range break: resistance is the maximum of the previous `n` periods, support the minimum; a signal fires on penetration, optionally with a band of `x` percent to filter | one price series, `n`, optional band | line, plus an optional percentage band | **N** for the level; the optional filter band is a percentage of price and is affine-defective | abstract | **yes, and it is the strongest in the corpus** - bootstrap against a random walk, AR(1), GARCH-M and exponential GARCH, later corrected for data snooping by a reality check |

**Observation on Group B.** Thirteen definitions, all Class N, and they disagree
with each other about which bars are turning points. D15 and D17 will differ on
almost every series; D13 with `w=21` and D14 with an effective window of 100 will
differ on nearly all of them. No retrieved source compares them. The choice of
extremum detector is an unexamined researcher degree of freedom sitting upstream
of every clustering definition in Group C, which take extrema as their input.

### 8.2 Definitions built on a distribution over the price axis

#### 8.2.1 Group C - clustering and density of path features

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D23 | Agglomerative clustering of candidate prices: run single-linkage-style agglomerative clustering with `distance_threshold = distance` and `n_clusters = None` over the one-dimensional array of extremum prices; each cluster becomes one level at the mean or median of its members; the cluster size is retained as `peak_count`, which is the strength measure | extremum prices from a Group B rule, one merge distance | line, with an implied band equal to the cluster spread that the code discards | **N** if the merge distance is given in price units and rescaled with the axis. The library also exposes `merge_percent`, and that variant is affine-defective | code: `day0market/support_resistance`, `_cluster_prices_to_levels` | none |
| D24 | K-means on highs and on lows separately: fit `k = 1..10`, record within-cluster sum of squares, and take the first `k` whose successive WCSS difference falls below `saturation_point`, default 0.05. Cluster centres are the levels | highs and lows, one saturation threshold | line | **N in form.** But WCSS is in **squared price units**, and it is compared against an absolute constant. The selected number of levels therefore depends on the instrument's price level and on its volatility scale. This is not a subtle defect: run it on a 5-dollar stock and a 5000-point index and the elbow rule does different things. Recorded as N, affine-defective, and as an implementation error rather than a design choice | code: `judopro/Stock_Support_Resistance_ML` | none |
| D25 | Pairwise pivot grouping: for each zigzag pivot, collect all other pivots of the same direction within `time` bars and within `dif` percent in price; if more than `number` such pivots exist, emit a level at their arithmetic mean, spanning from the earliest to the latest member; consume the grouped pivots so they cannot seed another level | zigzag pivots, three parameters (defaults 150 bars, 0.05 percent, 3 points) | a horizontal segment with a start and end bar - a line in price, bounded in time | **N, affine-defective** (percentage of price) | code: `BatuhanUsluel/Algorithmic-Support-and-Resistance` | none |
| D26 | Hough transform: rasterise the price-time plane into an image whose vertical resolution is `1/hough_scale` price units per pixel (default `hough_scale = 0.01`, so 100 rows per price unit), mark extremum pixels, and take accumulator peaks as candidate lines; probabilistic and point variants iterate | extrema, a raster resolution, an angle discretisation of 1800 angles | line, generally sloped | **N** under the affine test, **but the definition quantises the price axis itself**. The grid is chosen by the algorithm rather than by the exchange, so it is not Class T; it is nonetheless a discretisation, and two levels closer than one raster row cannot be distinguished. This is the only definition in the corpus that imposes its own price grid | code: `GregoryMorse/trendln`, `hough`, `houghpt`, `prob_hough` | none |
| D27 | Best-fit line over extrema: enumerate candidate subsets of extrema, fit by least squares, accept when all members lie within `errpct` (default 0.005) of the fitted line scaled by the price range, and score by a Riemann-sum area between line and series | extrema, one tolerance | line, with a tolerance band of `errpct` | **N, affine-defective** | code: `trendln`, `calc_support_resistance` | none |
| D28 | Heuristic SR discovery for intraday series: propose candidate levels, count prior bounces at each, evaluate whether the level reverses trend, and model the level's strength as decaying with time since formation. The retrieved abstract states the ingredients - bounce counting, a decay function, statistical significance of reversal - but not the numeric thresholds | intraday OHLC | line | **N** | abstract, **preprint tier** | **yes** - the authors state the levels are "not explained simply by AR(1) processes, stationary or otherwise". This is the only retrieved source that tests a level definition against an explicit stochastic alternative rather than against a buy-and-hold benchmark |
| D29 | An algorithmic labelling rule that assigns SR labels to bars, used to train a causal-convolution CNN-LSTM-MLP classifier. The labelling rule is the definition; the network is a function approximator of it | OHLC | line | **N** (the labelling rule is path-based; its details were not retrieved) | abstract | none for the level; a trading comparison for the classifier |
| D30 | DeepSupp: attention over correlation patterns for dynamic SR levels | not obtained | not obtained | **unclassified** | metadata-only | none obtained |
| D31 | Touch scoring: given candidate levels, walk the bars and award `+2` for a touch by a wick that respects the level, `+1` for a touch at a high or low, `-1` when a wick cuts through, `-2` when a body cuts through, with a minimum of 5 bars between consecutive body-cut penalties; levels closer than `min_distance_between_levels` percent are treated as the same level; candidates within `diff_perc_from_extreme` percent of the series extremes are dropped | candidate levels, OHLC, five percentage parameters | line, with a percentage tolerance band | **N, affine-defective**; every tolerance is a percentage of price | code: `day0market/support_resistance`, `pricelevels/scoring/touch_scorer.py` | none. The scores `+2, +1, -1, -2` are unlabelled constants with no stated objective |
| D75 | Mode of the price marginal: estimate a density over realised prices by kernel density estimation and take its modes as levels, with mode prominence as strength. Equivalently, the modes of the occupation measure of the path | one price series, a bandwidth | line | **N**. The corpus contributes the reason this one is treacherous: over a fixed window the empirical price distribution converges not to a density but to the occupation measure of the realised path, that is to Brownian local time, which is generically multimodal for a driftless random walk | this review's own agenda proposes the estimator; the local-time source is metadata-only | **yes, negatively** - the branch-1 Monte Carlo already in the agenda shows the dip test rejects unimodality on random walks at rates rising to 0.903 at n = 5000 |

**Observation on Group C.** Every clustering definition takes its input from a
Group B extremum rule and none of them says which one. The composition is where
the researcher degrees of freedom multiply: extremum detector (at least seven
choices) crossed with merge rule (five) crossed with merge tolerance
(unbounded). No retrieved source, at any tier, reports a sensitivity analysis
over that grid.

#### 8.2.2 Group D - volume and time distribution over the price axis

This is the family where the tick grid enters the definition **by construction**,
and it is the only family where that is true of the mainstream implementation
rather than of an edge case.

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D32 | Point of control: bin price into rows, sum volume per row, take the row with maximum volume. The reference implementation sets `row_size = tick_size * prices_per_row` with `tick_size` defaulting to 0.05 and `prices_per_row` to 1, and rounds each close **up** to the next row boundary via `ceil(x * (1/row_size)) / (1/row_size)`. The vendor documentation gives the same construct as "the price level for the time period with the highest traded volume" and exposes only a row count, not a row size | traded price, volume, **a price quantisation** | line | **Class T.** The level is the identity of a bin, and the bin edges come from the tick. Change the tick and the POC moves. The vendor variant, which lets the user set a row count over the session range, is Class N with an internally chosen grid, so **the same named construct is Class T as implemented and Class N as documented** | code: `bfolkens/py-market-profile`; vendor: TradingView Volume Profile | none |
| D33 | Value area: set `target = value_area_pct * total_volume` with `value_area_pct` defaulting to **0.70**; start at the POC row; repeatedly compare the next row above and the next row below and add the larger, until the accumulated volume reaches the target; VAH and VAL are the highest and lowest included rows | as D32, plus one percentage | **band**; the width is whatever the expansion produced, so it is endogenous given the 70 percent | **Class T**, inherited from the binning | code: same file, `calculate_value_area`; vendor: "this percentage is set to 70%, however, it is up to the trader's discretion" | none |
| D34 | Time-price-opportunity profile: identical to D32 and D33 with the count of periods trading in a row substituted for volume | price, a period clock, a quantisation | line and band | **Class T** | code: `market_profile`, `mode='tpo'` | none |
| D35 | High and low volume nodes: local maxima and minima of the binned profile, obtained by a discrete relative-extremum filter over the row array | the binned profile | line | **Class T**, and additionally sensitive to the row size in a way the POC is not, since it is a second-difference of the binned counts | code: `market_profile`, `find_extrema` | none |
| D36 | Balanced target: reflect the POC through the wider of the two profile wings - if the distance from POC to the profile high exceeds the distance to the profile low, the target is `POC - (profileHigh - POC)`, else `POC + (POC - profileLow)` | the profile range and the POC | line | **N** given the POC; inherits T from it | code: `market_profile`, `calculate_balanced_target` | none |
| D37 | Limit-order-book volume profile: the distribution of resting volume across book levels, studied for heavy tails intraday and interday | book snapshots indexed by level | a profile, not a level | **Class T**; "level" here means the k-th price step from the best quote | abstract, preprint tier | distributional fits, not a level test |
| D38 | Average book shape function: the mean resting volume as a function of distance from the best quote, which has a maximum away from the best price and, in one market, **periodic peaks with a period of five ticks** | book snapshots | a shape, whose maximum is a level | **Class T**, explicitly: the period-five peaks are a property of the grid and of human price preferences on it, not of the path | abstract, preprint tier and peer-reviewed | none as a level test |

**The 70 percent is still unsourced.** The vendor states it and immediately
disowns it as discretionary. Ten tier-5 sources assert that it approximates the
68 percent mass within one standard deviation of a Gaussian. No source at any
tier above 5 was located, including a search aimed at the exchange that
originated the construct. This replicates, on an independent search, the negative
already recorded in the regime-classification corpus. The label `CONVENTION`
stands, and it now has two independent failed searches behind it rather than one.

### 8.3 Definitions built on order-book state

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D39 | **The level is a peak in resting depth on the limit order book.** Support and resistance levels coincide with depth peaks, and the corresponding technical rules are locating depth already in place rather than predicting it | full book, resting size by price | line at the depth peak; a band if a contiguous run of prices is used | **Class N.** The book sits on the tick grid, but the depth peak is a feature of where size rests, and it is equivariant under re-denomination of the axis. This is the single most important entry in the taxonomy: it is a definition of a level that is neither round-number nor tick-derived, has an economic mechanism, and has been measured | abstract, peer-reviewed | **yes** - the coincidence between technical levels and depth peaks is itself the tested claim |
| D40 | Relative limit price: the signed difference between an order's limit price and the best price on its side. Its unconditional distribution decays as a power law with exponent about -1.5 over a range from a few ticks to about 2000 ticks | order messages | a distribution, from which a modal offset could be read as a level | **Class T** in units; the distribution is defined over the tick lattice and its support is stated in ticks | abstract, peer-reviewed | power-law fit; no level test |
| D41 | Limit orders cluster at the **previously permitted** price set after a ten-fold tick reduction, and at halfway points between old allowed prices. These clusters are where the best quotes sit for most of the time, producing "price barriers" and distinct peaks in the average book shape at round distances. The residual clustering is attributed to manual traders still working to the old resolution, while automatic traders post one tick ahead of the clusters | order messages, tick-size regime history | line, at legacy grid points | **Class R and Class T jointly, and it is the record that proves they are separable.** The grid changed; the clustering did not follow it. The level is at a *former* grid point, which is a round number in the current grid's terms. Any surrogate that preserves the current tick grid but not the legacy one destroys this construct | abstract, **preprint tier** | descriptive; no formal null |
| D42 | Hidden or iceberg resting size at a price: displayed size understates true size, so a price can absorb more than the book shows | order messages, executions | line | **Class N** | abstract, working-paper tier | none as a level |
| D43 | Queue imbalance at the best quote as a one-tick-ahead predictor of the next price move | best bid and ask size | not a level; a state at the current level | **Class T** by construction - the prediction target is one tick | abstract, peer-reviewed | prediction tests |
| D44 | Multi-level order-flow imbalance: order flow aggregated across the first `k` book levels | book messages | not a level; a covariate indexed by level | **Class T** | abstract, preprint tier | regression tests |
| D45 | **The level is where the resting stop and target orders are.** Take-profit orders cluster strongly at round numbers; stop-loss orders cluster strongly *just beyond* round numbers. The first pattern predicts reversal at the level, the second predicts acceleration through it | order-book data on stop and target orders | line, with a systematic asymmetry - reversal orders at the number, acceleration orders past it | **Class R.** The clustering is at round numbers, and the mechanism runs through the number. This is the record the agenda already flags as arguing that round-number clustering is *part of* the construct | abstract, peer-reviewed | descriptive documentation, with the two technical predictions stated as testable |

**Observation on Group E.** This is the only group where a level has both a
location rule and a mechanism. It is also the group whose definitions the agenda
cannot currently use, because branch 1 operates on a price series and every
definition here needs message-level data. Recorded so the constraint is explicit:
**the best-evidenced level definitions in the corpus are not computable from the
data branch 1 has.**

### 8.4 Definitions anchored to an exogenous grid, and volatility-scaled bands

#### 8.4.1 Group F - exogenous grids

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D46 | Level at every multiple of 100 in an index. Test whether the index's rise and fall is restrained at those multiples and whether it moves more than otherwise warranted after breaking through one | the index level only | line | **Class R**, in the purest form found | abstract, peer-reviewed | **yes** - a Monte Carlo study plus comparison with other indices |
| D47 | Psychological barrier at round values, tested by examining the distribution of the trailing digits of the index and looking for depletion near the barrier | index closes only | line | **Class R** | abstract, peer-reviewed | **yes, and contested** - see section 8.5 |
| D48 | Prices cluster on round fractions; clustering rises with price level and volatility and falls with capitalisation and trade frequency. Traders use a *coarser discrete price set than the exchange permits*, and an econometric model of that choice is estimated | transaction prices, the permitted grid | line, at the chosen coarse set | **Class R and Class T jointly.** The permitted set is Class T; the chosen subset is Class R. The record's contribution is exactly that these two are different objects | abstract, peer-reviewed | **yes** - an estimated econometric model of clustering, with out-of-sample projections |
| D49 | Odd-eighth avoidance: the price set actually quoted is a strict coarsening of the permitted set | quotes, permitted grid | line | **Class T** | abstract, peer-reviewed | **yes** - a cross-sectional test |
| D50 | The tick grid itself as the level structure: for a large-tick asset the effective spread is almost always one tick, and an implicit spread must be defined to recover a meaningful notion of price distance; for a small-tick asset the book is sparse and prices move multiple ticks | trades, quotes, tick value | the lattice | **Class T** by definition | abstract, peer-reviewed and preprint | **yes** - a theoretical framework with an optimal-tick criterion, empirically fitted |
| D51 | Level at an integer, with the *active* prices one tick below (buying) and one tick above (selling). Buy-sell imbalance is monotone in the roundness of the adjacent round number, and is much stronger when the quote reaches the integer than when it crosses | transaction prices, signed volume, the tick | line at the integer; an asymmetric one-tick offset for the active side | **Class R and Class T jointly**, in a very specific way: the *anchor* is the round number, the *offset* is one tick. Neither confound alone reproduces it | abstract, peer-reviewed | **yes** - imbalance tests with a monotonicity prediction across roundness levels |
| D52 | Level at an option strike: on expiration dates the underlying clusters at strikes; a mechanism is derived in which aggregate delta-hedging by market makers exerts a restoring force whose strength depends on open interest, giving a finite pinning probability computable from volatility, time to maturity, open interest and a price-elasticity constant | underlying price, option open interest, expiry calendar | line at the strike | **Class N-X.** Equivariant under re-denomination, because the strike re-denominates with the price. Not path-derived: the location is set by a contract grid. Treating this as ordinary Class N would be a modelling error | abstract, peer-reviewed and preprint | **yes** - a pinning probability derived and computed, plus a quantitative single-event test |
| D53 | Target zone: an announced band with defended edges. The expectation of defence changes price behaviour throughout the interior, and the problem is formally similar to option pricing | the announced band, a policy rule | **band**, with the width announced ex ante | **Class N-X.** The only definition in the corpus whose band width is known in advance and is not estimated from anything | abstract, peer-reviewed | derivation with testable restrictions on interior dynamics |
| D54 | Natural resistance point identified by a currency redenomination: the same economic price acquires a different decimal representation, so round-number effects can be separated from real price levels | prices before and after redenomination | line | **Class R**, and the **only identification design in the corpus that can separate the number from the price** | metadata-only, peer-reviewed | **yes, by design** - a natural experiment |
| D55 | Point and figure: price is quantised into boxes and a column reverses after a stated number of boxes against the trend. The retrieved text confirms the method uses price only and ignores volume, and does **not** state the box-size or reversal rules | price only | a lattice of box boundaries | **Class T, tentative.** The classification follows from the construct being a quantisation; the primitive rule was not obtained, so this is an inference, flagged as such | abstract, tier 5 | none |

#### 8.4.2 Group G - volatility-scaled and range-scaled bands

This group answers the part of the task about how a *zone with a width* is
bounded. Six mechanisms were found: a fitted dispersion, a multiple of a range
statistic, a fixed percentage of price, a fixed fraction of an observed range, a
fixed number of ticks, and by eye.

| id | definition (operational) | inputs | band width set by | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D56 | Bollinger Bands: a moving average, normally 20 periods, with bands at a stated number of standard deviations of price, most commonly two | one price series | **a fitted dispersion** - the rolling standard deviation | **N** | abstract, tier 5 | none. The abstract's own claim that two standard deviations "would contain about 95% of all data points" is a Gaussian-iid statement about a series that is neither, and is recorded as an error in the source rather than repeated |
| D57 | Moving-average envelope: two lines a fixed percentage above and below a moving average | one price series | **a fixed percentage of price** | **N, affine-defective** | abstract, tier 5 | none |
| D58 | ATR channel: true range is the greatest of high minus low, previous close to high, and previous close to low; ATR is a moving average of true ranges; the channel is formed by adding to or subtracting from the previous bar's close or the current bar's open | OHLC | **a multiple of a range statistic** | **N**, and fully affine-equivariant: true range is a difference, so it is translation-invariant and scales with the axis | abstract, tier 5, stated verbatim | none |
| D59 | Donchian channel | not obtained. The retrieved chapter text discusses the construct's role in trend-regime analysis and does not state the highest-high, lowest-low rule | OHLC | **unclassified** | abstract, tier 5 | none |
| D60 | Equal highs and equal lows: two pivots at the same extreme type are "equal" when `abs(pivotLevel - candidateLevel) < threshold * ATR(200)`, with `threshold` defaulting to 0.1 and constrained to the interval 0 to 0.5 | OHLC, ATR | **a multiple of ATR** | **N** | code: LuxAlgo Pine source, `q-github-src-10` | none |
| D61 | Order-block volatility filter: a bar is a high-volatility bar when `high - low >= 2 * volatilityMeasure`, where `volatilityMeasure` is either `ATR(200)` or the cumulative mean true range `cum(TR)/bar_index`; for such bars the code **swaps** the values used as the block's top and bottom, so a volatile bar produces an inverted, narrower block | OHLC, ATR | **a multiple of ATR**, applied as a filter rather than as a width | **N** | code: LuxAlgo Pine source | none |
| D62 | Premium, discount and equilibrium zones: with `top` and `bottom` the running maximum and minimum since the last swing, the premium zone is `[0.95*top + 0.05*bottom, top]`, the discount zone is `[bottom, 0.95*bottom + 0.05*top]`, and the equilibrium zone is `[0.525*bottom + 0.475*top, 0.525*top + 0.475*bottom]` | running extremes | **fixed fractions of the observed range**: the outer 5 percent at each end and a 5 percent band around the midpoint | **N**, and affine-equivariant, because the fractions multiply a range rather than a price | code: LuxAlgo Pine source | none |
| D63 | Liquidity cluster: swing highs within `pip_range` of each other form one liquidity level, where `pip_range = (max(high) - min(low)) * range_percent` and `range_percent` defaults to 0.01. The level is swept at the first bar whose high reaches `level + pip_range` | swing extremes, the full observed range | **one percent of the entire observed high-low range** | **N**, affine-equivariant for the same reason as D62. Note the causal-time defect: `max(high)` and `min(low)` are taken over the whole sample, so the band width at time `t` uses information from after `t` | code: `joshyattridge/smart-money-concepts`, `smc.liquidity` | none |

### 8.5 Group H - candle geometry, and the retail block constructs

| id | definition (operational) | inputs | line or band | confound relation | source, tier | null attached |
|---|---|---|---|---|---|---|
| D65 | Order block, canonical statement: the last opposing candle before an impulsive move - the last down-close candle before an up-move for a bullish block, the last up-close candle before a down-move for a bearish block | OHLC | **band**, but the ten retrieved sources **do not agree** whether the band is the candle's body or its high-low range | **N** | tier 5 only; ten secondary restatements, no primary written source located | none |
| D66 | Order block, as implemented: walk bars; at each bar find the last swing high strictly before it; if the close exceeds that swing high and the swing has not been crossed before, search the bars between the swing high and the current bar for the **lowest low**, taking the last occurrence on ties; the block's bottom is that bar's low and its top is that bar's high; if no such interior bar exists the block defaults to the previous bar, **with top and bottom assigned from that bar's low and high respectively - that is, inverted**. The block is mitigated when a later low falls below its bottom, and is deleted when a later high exceeds its top. Strength is `min(highVolume, lowVolume)/max(highVolume, lowVolume)` over the block bar and its two neighbours | OHLC and volume | **band** equal to one candle's high-low range | **N** | code: `joshyattridge/smart-money-concepts`, `smc.ob` | none |
| D67 | Order block, LuxAlgo variant: as D66, but the candidate bar's high and low are replaced by `parsedHigh` and `parsedLow`, which are the bar's own high and low **unless** the bar is a high-volatility bar by D61, in which case they are swapped. Blocks are tracked separately for "internal" structure (pivot length 5) and "swing" structure (pivot length 50) | OHLC, ATR | band, one candle high-low, possibly inverted | **N** | code: LuxAlgo Pine source | none |
| D68 | Fair value gap: a three-bar pattern. Bullish when `high[t-1] < low[t+1]` and bar `t` closes up; the band is then `[high[t-1], low[t+1]]`. Bearish when `low[t-1] > high[t+1]` and bar `t` closes down; the band is `[high[t+1], low[t-1]]`. Consecutive gaps may be merged by taking the highest top and lowest bottom | OHLC | **band**, bounded by the extremes of the two outer candles | **N** | code: `smc.fvg` | none |
| D69 | Fair value gap with an automatic significance threshold: as D68, plus the requirement that the middle bar's `barDeltaPercent = (close - open)/(open * 100)` exceed `threshold`, where `threshold = 2 * cum(abs(barDeltaPercent))/bar_index` when auto-thresholding is on and 0 otherwise | OHLC | band as D68, with a filter | **N, affine-defective** - the delta is a percentage of the open. Also causally leaky by construction: the running mean is cumulative, so the threshold at bar `t` depends only on the past, which is correct, but the divisor `bar_index` makes early bars incomparable to late ones | code: LuxAlgo Pine source | none |
| D70 | Breaker block: an order block that has been mitigated, after which the same band is used with the opposite polarity. Implemented as a `breaker` flag on the block plus a reset when price exceeds the far side | OHLC | band, inherited | **N** | code: `smc.ob` internals | none |
| D71 | Liquidity sweep: the bar index at which a liquidity level from D63 is first exceeded by `pip_range` | swing extremes, OHLC | an event at a band edge, not a level | **N** | code: `smc.liquidity` | none |
| D72 | Break of structure and change of character: the broken swing level itself becomes the reference. A bullish break of structure occurs when price closes above the last swing high while the prior trend was bullish; a change of character is the same event when the prior trend was bearish | swing extremes from D14 | line at the broken swing | **N** | code: `smc.bos_choch` | none |

**Observation on Group H.** These are the definitions the retail literature is
loudest about and the ones with the weakest documentary base: **not one of the
eight has a source above tier 5, and none has any test attached.** They are,
however, fully operational, entirely Class N, and cheap to falsify - each one
reduces to inequalities among four OHLC values. The gap between how much is
claimed for them and how easily they could be tested is the largest in this
review.

### 8.6 The taxonomy

This is the section branch 1 needs. Every one of the 76 definitions is assigned
to exactly one class by the affine test of section 8.0. Assignments are
reproducible: apply the transform, look at whether the level set moves.

#### 8.6.1 Counts

| class | meaning | n | share |
|---|---|---|---|
| **R** | requires round numbers - the rule reads the decimal representation of price | **7** | 9 percent |
| **T** | requires the tick grid or another exchange-imposed quantisation - the rule reads the minimum price increment, or is undefined on a continuous price axis | **12** | 16 percent |
| **N** | independent of both - the level set is equivariant under affine re-denomination of the price axis | **53** | 70 percent |
| **unclassified** | no operational statement obtained, so the test cannot be applied | **4** | 5 percent |
| | | **76** | |

Three definitions carry a **joint R and T** dependence and are counted once, in
R, with the joint status recorded: D41 (limit orders clustering at the legacy
grid), D48 (traders choosing a coarse subset of the permitted grid) and D51 (an
integer anchor with a one-tick active offset). They are the most informative
records in the review precisely because they are joint: each one is a case where
the two confounds have been *observed coming apart*.

Two Class N definitions are flagged **N-X**: D52 (option-strike pinning) and D53
(announced target zone). They pass the affine test but are not functions of the
path, being anchored to an exogenous institutional grid. Collapsing them into N
for surrogate-design purposes would be an error.

Eight Class N definitions are flagged **affine-defective**: D06, D18, D24, D25,
D27, D31, D57 and D69. Each is equivariant under scaling but not under
translation, because a tolerance is a percentage of price rather than of a range
or of a dispersion. D24 is worse than the rest: its model-selection criterion
compares a within-cluster sum of squares, which has units of squared price,
against an absolute constant, so it is not even scale-equivariant.

#### 8.6.2 Class R - seven definitions

| id | short name | why it is R |
|---|---|---|
| D41 | limit-order clustering at legacy and round grid points | orders rest at prices that were round or permitted under a previous decimal regime; joint with T |
| D45 | stop-loss and take-profit order clustering | take-profits at round numbers, stop-losses just beyond them |
| D46 | multiples of 100 in an index | the level is literally a multiple of a power of ten |
| D47 | trailing-digit barrier | the statistic is a function of the digits |
| D48 | clustering on round fractions | the used price set is a round-number subset of the permitted set; joint with T |
| D51 | integer anchor with a one-tick offset | roundness is the anchor and the effect is monotone in it; joint with T |
| D54 | redenomination natural resistance point | the identification is the change of decimal representation at constant economic value |

**What Class R implies for a surrogate.** These seven cannot survive any
surrogate that randomises the price origin or rescales the axis. They also cannot
survive a return-resampling surrogate, for the reason the agenda already states:
resampled returns are invariant in distribution to the path's starting location,
so no round-number structure is preserved. If any of these is the construct under
test, the only admissible null is one that fixes the price axis and its decimal
labelling and randomises something else. The random-relocation null the agenda
already adopted does exactly the wrong thing for Class R: relocating a level
within the observed price range destroys its roundness, so the test would
correctly reject and the rejection would be uninformative about anything except
the fact that round numbers are round.

#### 8.6.3 Class T - twelve definitions

| id | short name | why it is T |
|---|---|---|
| D32 | volume-profile point of control | the level is the identity of a bin whose edges are `tick_size * prices_per_row` |
| D33 | value area | inherits the binning; the 70 percent is a separate unsourced convention |
| D34 | TPO profile | inherits the binning |
| D35 | high and low volume nodes | a second difference over the binned rows |
| D37 | book volume profile by level | "level" means the k-th tick from the best |
| D38 | average book shape function | its peaks occur at fixed tick distances, one market showing a period of five ticks |
| D40 | relative limit price distribution | defined on the tick lattice, support quoted in ticks |
| D43 | queue imbalance | the prediction target is one tick |
| D44 | multi-level order-flow imbalance | indexed by book level |
| D49 | odd-eighth avoidance | the object is a coarsening of the permitted grid |
| D50 | the tick grid as price structure | the grid is the definition |
| D55 | point-and-figure box lattice | a quantisation of price; classification tentative, primitive rule not obtained |

**What Class T implies for a surrogate.** A null that simulates price on a
continuous axis cannot express these definitions at all - not "loses power
against them", but cannot compute them. Any surrogate used to test a Class T
definition must generate prices on the same lattice with the same tick value. The
agenda's fallback null - a tick-grid jump-diffusion - is the right shape for this
class, and is the *only* class for which it is the right shape.

#### 8.6.4 Class N - fifty-three definitions

Listed by group, with the two N-X and eight affine-defective members flagged.

| group | ids | n |
|---|---|---|
| A prior-period arithmetic | D01, D02, D03, D04, D05, D06 (affine-defective), D07, D08, D09, D10, D11 | 11 |
| B extrema of the path | D12, D13, D14, D15, D16, D17, D18 (affine-defective), D19, D20, D21, D73, D74, D76 | 13 |
| C clustering and density | D23, D24 (affine-defective), D25 (affine-defective), D26, D27 (affine-defective), D28, D29, D31 (affine-defective), D75 | 9 |
| D distribution over price | D36 | 1 |
| E order-book state | D39, D42 | 2 |
| F exogenous grids | D52 (N-X), D53 (N-X) | 2 |
| G volatility and range bands | D56, D57 (affine-defective), D58, D60, D61, D62, D63 | 7 |
| H candle geometry | D65, D66, D67, D68, D69 (affine-defective), D70, D71, D72 | 8 |
| | | **53** |

**What Class N implies for a surrogate.** A Class N definition is compatible with
a null that destroys round-number structure and with a null defined on a
continuous price axis, because neither is where the construct lives. This is the
class for which the agenda's random-relocation null is admissible: relocating the
levels within the observed range breaks the level-location correspondence without
breaking anything the definition depends on.

#### 8.6.5 The result that unblocks branch 1

The three classes are not equally populated, and the imbalance is the answer.

**Seventy percent of the definitions people actually use are independent of both
confounds.** "Level" is not one construct entangled with round numbers and tick
discreteness. It is at least three constructs, and the largest of the three - by
a wide margin - is a claim about the geometry of the realised path that has
nothing to do with either confound. The block on branch 1 rested on the premise
that the construct could not be separated from the confounds. On the evidence
collected here that premise is false for 53 of 76 definitions, true for 7, and
true in a different way for 12.

Three further findings qualify that, and all three matter for what branch 1 does
next.

1. **The confounds are demonstrably separable, and one record demonstrates it.**
   After a ten-fold tick reduction on an FX platform, limit orders continued to
   cluster at the *old* permitted prices and at the halfway points between them
   (D41). The tick grid moved; the clustering did not. If round-number clustering
   and tick discreteness were the same phenomenon, that could not happen. This is
   a preprint-tier record and is flagged as such, but it is a direct observation
   of the two confounds coming apart, and no retrieved record contradicts it.

2. **Round-number clustering has a mechanism, so for Class R it is the
   construct, not a nuisance.** Take-profit orders cluster at round numbers and
   stop-loss orders just beyond them (D45); the buy-sell imbalance at a round
   number is monotone in its roundness and is far stronger on approach than on
   crossing (D51). A Class R level is not a level contaminated by round numbers;
   it is a level *made of* round numbers. Removing round-number structure from a
   surrogate used to test a Class R definition is precisely the
   alternative-absorbing surrogate the charter's gate condition (v) forbids -
   except in reverse: it would produce a false `construct`-positive by making the
   real data trivially different from the null.

3. **Class membership is a property of the definition, not of the tradition.**
   The Market Profile tradition contributes D32 to D36, which are Class T as
   implemented; the same tradition's initial balance (D09) is Class N. The retail
   smart-money tradition contributes eight Class N definitions in Group H and
   nothing in R or T. The academic barrier literature contributes almost all of
   Class R. A researcher who says "levels are just round numbers" and a
   researcher who says "levels are just the tick grid" are each describing a
   different 10 to 16 percent of the field.

**Therefore, the operational recommendation for branch 1.** Do not attempt to
test "levels" as a single construct. Pick one class, and the surrogate follows
from the class:

- **Class N**: the random-relocation null the agenda has already adopted is
  admissible. Every property of the data is preserved and only the
  level-location correspondence is broken. Add a positive control by injecting a
  synthetic level of known strength, as the gate requires.
- **Class T**: the random-relocation null is admissible only if relocation is
  constrained to the lattice. Off-lattice relocation makes the surrogate levels
  uncomputable rather than merely wrong.
- **Class R**: neither the random-relocation null nor any return-resampling null
  is admissible. The only design in the corpus that identifies a Class R level is
  the redenomination natural experiment (D54), which changes the decimal
  representation while holding economic value fixed. If branch 1 wants a verdict
  about Class R levels, it needs that design or an equivalent, not a surrogate.

A single further consequence follows and should be stated plainly, because it
changes what the branch is for. **A `construct-negative` verdict on Class N would
say nothing about Class R or Class T, and vice versa.** The charter's `construct`
gate requires an explicit scope - "instrument, timescale, feature set,
measurement". This review supplies the missing dimension of that scope: the
*definition class*. A branch-1 failure_log row that does not name a class is not
localised.

#### 8.6.6 Tally: has anyone ever attached a null, a test, or a falsification?

The task asks this of every definition. The answer, for 76 definitions, is that
**16 have had some form of statistical apparatus attached and 60 have had none.**
The 16 are not equally serious, so they are split by what was actually tested.

**Tested for existence or location of the level itself (7):**

| id | what was tested | instrument |
|---|---|---|
| D46 | whether an index is restrained at multiples of 100 and moves excessively after breaching one | Monte Carlo null plus cross-index comparison |
| D47 | whether the distribution of trailing digits is depleted near round values | digit-distribution tests, **and the null is contested** - see D-note below |
| D48 | which discrete price set traders actually use, and what drives the choice | an estimated econometric model of clustering with out-of-sample projections |
| D49 | whether quoted prices avoid a permitted subset of the grid | cross-sectional test across securities |
| D51 | whether order imbalance is monotone in roundness and asymmetric on approach versus crossing | imbalance tests with a pre-stated monotonicity prediction |
| D52 | whether the underlying pins at strikes, and with what probability | a derived pinning probability, computed and compared with observed frequencies; plus a single-event quantitative test |
| D54 | whether the round-number effect survives a change of decimal representation at constant economic value | natural experiment |

Every one of the seven is Class R or Class T or N-X. **Not one Class N definition
has ever had its existence tested.** That is the central negative of this review.

**Tested for a downstream consequence, not for the level (9):** D08 and D11
(accuracy or profitability of a rule that uses the level), D21 and D76
(conditional versus unconditional return distributions, with bootstrap and
data-snooping corrections), D28 (reversal significance against AR(1) and
stationarity alternatives - the closest any Class N definition comes), D29
(classifier performance), D39 (association between technical levels and book
depth), D50 (tick-size regime effects on market quality), D73 and D74
(derivations with uniqueness proofs but no empirical test) - the last two pair
into one entry, giving nine.

**D-note on D47.** The barrier literature's usual null is that the trailing
digits of the index are uniformly distributed, so that a deficit of observations
near a round value indicates a barrier. One corpus record argues this null is
wrong: under a multiplicative price process, digit frequencies follow a
Benford-type law rather than a uniform one, so a test calibrated against
uniformity will find barriers where none exist. This is a `metadata-only` record
in this review - the argument is taken from its title and from the citing
context, and the full text was not read. **It is flagged as a claim this review
could not verify**, and it is important enough that branch 1 should verify it
directly before using any D47-family statistic.

**Sixty definitions with nothing attached.** Including every pivot formula, every
extremum detector, every clustering rule, every volume-profile construct, every
band-width rule, and every candle-geometry block. The distribution of statistical
effort across this field is almost exactly inverted relative to the distribution
of use.

### 8.7 Definitions for which no operational statement was found

Six entries. Four are unclassifiable because nothing executable was retrieved;
two are operational but only through secondary restatement, which is a different
and lesser failure.

**No operational statement at all - name and role only:**

| id | name | what was retrieved | what is missing |
|---|---|---|---|
| D22 | TD range projection, TD range expansion breakout, TD channels | a chapter title and its book, verified by DOI resolution; no content | every rule. The construct is named, attributed, and locatable as a publication, and nothing about how it computes a level was obtained at any tier |
| D30 | DeepSupp dynamic support and resistance | title, venue, year, DOI; the arXiv version was deduplicated against the conference version | the discovery rule. The abstract retrieved by the arXiv query names "attention-driven correlation pattern analysis" and does not state what a level is |
| D59 | Donchian channel | a chapter discussing its role in trend-regime analysis, and the observation that ATR indicates volatility regime | the channel rule itself. The widely repeated highest-high, lowest-low over `n` periods statement appears in no retrieved source at any tier in this search |
| D64 | tight trading range | a chapter that describes the pattern's trading implications and explicitly declines to bound it - "a common pattern that has been called many different things, but none of the terms is adequately descriptive" | any bound. This is a rare case of a practitioner source stating that the construct has no agreed definition |

**Operational only through secondary restatement - no primary source located:**

| id | name | status |
|---|---|---|
| D65 | ICT order block | Ten tier-5 sources give a consistent core rule - the last opposing candle before an impulsive move - and **disagree about the band**: some bound the block by the candle body, others by its high-low range. Two independent code implementations (D66, D67) both use high-low, which is evidence about implementer consensus, not about the originator's intent. No primary written specification by the originator was located, and none may exist in text |
| D33 | the 70 percent value area | The rule is fully operational and was read from both code and vendor documentation. The **constant** has no primary source at any tier above 5, in two independent searches. The one-standard-deviation rationale is asserted only at tier 5 and would in any case be a Gaussian claim about a distribution that is not Gaussian |

**Two constants in the same position, recorded for the same reason:** the
Camarilla ladder `1.1/12, 1.1/6, 1.1/4, 1.1/2` (D06) and the Fibonacci pivot
ratios `0.382, 0.618` (D03, D11) appear in vendor documentation with no
derivation and no citation anywhere in this corpus. Under charter commitment 3
they are unlabelled constants. They are not listed as separate definitions
because the rules that use them are fully operational; the constants are simply
unsourced.

### 8.8 Where the corpus disagrees with itself

Four genuine conflicts, reported rather than averaged.

1. **Do round numbers act as barriers at all?** D46 reports that the DJIA's
   movement is restrained at multiples of 100, supported by a Monte Carlo study.
   The Benford critique argues the null used by that family of tests is
   mis-specified, because the distribution of trailing digits under a
   multiplicative price process is not uniform, so a barrier test calibrated
   against uniformity finds barriers that are not there. A 2026 study of Bitcoin
   reports strong clustering and **weak** barriers in the same data - clustering
   and barriers are separate claims and only the first survives. This review takes
   no position beyond recording that the strongest Class R evidence is about
   *clustering* and the weakest is about *barriers*, and that branch 1 should not
   treat the two as one hypothesis.

2. **Is the level in the price or in the book?** D39 places it in the book, as a
   depth peak that technical rules locate rather than create. D46 and D47 place it
   in the number. D41 places it in a *former* grid. These are not compatible, and
   the observable that discriminates them - whether the level moves when the grid
   moves, and whether it survives a redenomination - has been measured only once
   for each.

3. **Docstring against code.** D14's docstring and its implementation describe
   different windows, by a factor of two. Any user reading the documentation and
   any user reading the source will define swing points differently. Reported
   because it is a concrete instance of the review's own rule that code is the
   primary source for a code definition.

4. **A named construct is Class T in code and Class N in documentation.** D32,
   the point of control, is binned on the tick in the reference Python
   implementation and binned on a user-chosen row count in the vendor tool. Two
   analysts using "the POC" are not computing the same object, and the difference
   is exactly the confound this review was commissioned to separate.

### 8.9 What the corpus does not contain

- **No comparison of extremum detectors.** Seven Group B rules, no study
  comparing them, no sensitivity analysis, no agreement statistic.
- **No test of any pivot-point formula.** D01 to D06 are the most widely
  deployed level definitions in retail software and have no null, no reference
  distribution and no primary source in this corpus.
- **No test of any Group H construct.** Eight fully operational, entirely Class N
  definitions with zero tests attached.
- **No published null distribution for a clustering-based level.** D23 to D31 are
  all detection procedures with no false-positive rate.
- **No confidence interval on a level location anywhere in the corpus.** Not one
  retrieved source reports an interval for where a level is. The agenda's remark
  that "a level without an interval is a drawing" is, on this evidence, a
  description of the entire literature.
- **No causal-time audit.** D63 computes its band width from the full-sample
  range and D04 uses the current period's open. Neither source flags it. No
  retrieved source discusses lookahead in level construction at all.
## 9. Bibliography store

<!-- bibliography-store -->
- Store: `docs/literature/references_level-definitions.json` (CSL-JSON, canonical
  serialization written by `build_bibliography.py`)
- SHA-256: `213824cd107fd52fa682ba66bfbd206318c554f201cb470673dde652d8462a9f` -
  equals frontmatter `bibliography_sha256`
- 81 entries, one per included record; every entry carries a DOI, and every DOI
  was resolved live by the gate at authoring time
- 70 entries were created by DOI resolution against Crossref; 11 were created
  from DataCite CSL for arXiv identifiers, because the store builder resolves
  Crossref only and arXiv DOIs are registered with DataCite. Those 11 were
  reduced to the CSL fields the schema admits before insertion, and the reduction
  is the only place in this review where a stored field was touched by hand. The
  identifiers themselves were not typed - they came from the arXiv Atom responses
  logged under `q-arxiv-*`
- 30 abstracts absent from the Crossref deposits were backfilled from OpenAlex
  and logged as `gap-openalex-abstracts`. That log contributes **0** records to
  `n_identified`: every DOI in it was already an included record, and the request
  retrieved text for records already in the corpus rather than discovering new
  ones
- Derived exports (regenerable; never a source of truth):
  `python ~/.claude/scripts/build_bibliography.py export docs/literature/references_level-definitions.json --format bibtex|ris`

## 10. Limitations and verification gaps

### 10.1 Verification gaps

1. **No full text was read for any corpus record.** This is the dominant
   limitation and it is stated first because everything else follows from it. Of
   81 included records, 61 were extracted from a retrieved abstract and 20 from
   title, venue and DOI alone. Section 7 flags each record individually. Any
   statement in section 8 attributed to a `metadata-only` record is a claim this
   review could not verify, and four such claims are load-bearing enough to name
   here: the Benford critique of the barrier null (section 8.6.6), the
   redenomination natural experiment (D54), the option-expiration clustering
   result (D52) and the stop-loss cascade mechanism (D45, partly - the closely
   related order-clustering record is abstract-verified).
2. **The TradingView Pine Script Language Reference did not render.** The
   `ta.pivothigh` and `ta.pivotlow` definitions in D12 come from tier-5 secondary
   restatements, not from the vendor reference. Logged as
   `q-webfetch-tv-pineref` with `n_records = 0`. The restatements agree with each
   other, which is weak evidence, and the vendor's own wording was not obtained.
3. **Source files were retrieved by default branch, not by commit SHA.** The
   seven Python files and one Pine file that carry most of section 8 were fetched
   from `HEAD` of the default branch on 2026-08-21. A rerun after any push to
   those repositories will read different code, and this review records no hash
   that would detect it. This is a reproducibility defect in the review, not in
   the sources, and it is the single change most worth making before any rerun.
4. **The LuxAlgo Pine source was read from a third-party mirror**, not from
   TradingView. The mirror is licensed CC BY-NC-SA 4.0 and presents itself as the
   official open-source script. Its fidelity to the published version was not
   independently checked against TradingView, because the script page is
   client-side rendered.
5. **Two ICT-family band definitions could not be resolved.** Whether an order
   block is bounded by the candle body or by its high-low range is not agreed
   across the ten retrieved tier-5 sources. The two code implementations both use
   high-low. This review reports the disagreement rather than picking a side.
6. **No primary source was located for the 70 percent value area**, for the
   Camarilla constants, or for the Fibonacci pivot ratios. Two independent
   searches have now failed on the first of these.
7. **Author attribution is absent for twelve book-chapter records.** Crossref
   holds no author for those chapter DOIs, and this review did not supply names
   from memory. The section 7 citation for each therefore reads "(no author in
   record)". Naming the authors would have been easy and would have been exactly
   the fabrication the charter's attribution-fidelity commitment forbids.

### 10.2 Recall limitations

1. **No forward citation search.** No citing-reference search was run on any
   record. For a definitional survey this is a serious gap: the natural way to
   find every test ever applied to D46 is to look at what cites it, and that was
   not done. Section 8.6.6's count of 16 tested definitions is therefore a **lower
   bound**, and possibly a poor one.
2. **Row limits bind hard.** Topical Crossref recall is the recall of the top 6
   to 10 relevance-ranked hits per query. Crossref relevance ranking on
   free-text bag-of-words queries in a polysemous domain is not a good instrument,
   as q-crossref-16 and q-crossref-20 demonstrate in the logs.
3. **No book-indexing database was searched.** The technical-analysis canon is
   book-shaped. This review reached it only through publisher chapter DOIs, which
   exist for some titles and not others. A definition that lives only in a book
   without chapter DOIs is invisible to this search. Two of the four name-only
   entries in section 8.7 are almost certainly in this category.
4. **No non-English source, and no source transmitted by video.** The retail
   traditions most active in Group H teach primarily through video. Nothing in
   this method can see them.
5. **GitHub code search returns an index, not a census.** The three code-search
   queries returned predominantly recent derivative repositories. Repository
   search by stars corrected this but introduced a popularity bias of its own: an
   accurate, unstarred implementation was invisible to both strategies.
6. **No study registry, no grey-literature repository, no preprint server other
   than arXiv.** SSRN records entered only through Crossref DOIs, not through
   SSRN search; RePEc was not searched.

### 10.3 Screening and extraction limitations

1. **Single screener, no independence, no agreement measure.** See section 1.4.
   Every inclusion, exclusion and class assignment in this review is one model's
   judgement, uncorroborated.
2. **The deepest reading was done on the lowest-tier sources.** Eight source
   files and two vendor pages were read in full; not one peer-reviewed full text
   was. The consequence is a systematic asymmetry: Group A, G and H definitions
   are described with formula-level precision because their sources are code and
   vendor docs, while Group C, E and F definitions are described at abstract-level
   precision because their sources are journals behind paywalls. **A reader could
   mistake that asymmetry for a difference in how well-specified the definitions
   are.** It is not; it is a difference in what this review could open.
3. **Exclusion reasons were recorded as free-text screening notes, not as a coded
   field.** The category counts in section 6 are therefore approximate, exact only
   in the total. A coded exclusion field is the cheapest fix available to any
   rerun.
4. **The taxonomy assignments were made by applying the affine test mentally, not
   by executing it.** For the code-derived definitions the test is a reading of
   the source and is reliable. For the abstract-derived definitions it rests on
   the abstract's description of the rule, which is thinner. The six assignments
   most exposed to this are D19, D20, D29, D40, D44 and D55; D55 is already
   flagged as tentative in section 8.4.1.
5. **Stage 2 deduplication is a judgement.** 35 of the 46 removed duplicates were
   removed by a manual same-work grouping, enumerated in the ledger but not
   independently checked.

### 10.4 Scope exclusions applied by directive

Profitability was not assessed and no backtest was run. Where a corpus record's
only apparatus is a profitability test, that is recorded in the null column as
what it is and the performance claim is not repeated. The agendas, the charter,
the failure log and the audit trail were not modified. Citations asserted
elsewhere in the repository were not re-verified; the regime-classification
corpus and this one are separate stores and share no entries by construction,
although they share several works.

### 10.5 What this review does not settle

It does not establish that any level exists. It establishes what people mean when
they say one does, how many distinct things they mean, and which of those
meanings can be tested against which null. Branch 1 remains blocked on the
question of whether a level exists; it is no longer blocked on the question of
what would be tested, and section 8.6.5 states which surrogate is admissible for
each of the three answers.

### 10.6 Gate verdict: `block`, on G16 identifier-resolution findings, all false positives

The research-compile gate returns `block`. The verdict is reported unmodified and
is not softened, because a gate whose verdict is edited by the artifact it judges
is not a gate. What the verdict rests on is stated here so a reader can weigh it.

**Every finding is G16.** No G1 through G15 and no G17 through G20 assertion
fails. G16 issues an unauthenticated HTTP `HEAD` to `https://doi.org/{doi}` with
the user agent `skie-check-lit-review/0.1.0` and treats any non-2xx, non-3xx
response as an unresolved identifier.

**The finding count is not stable between runs.** Successive executions of the
gate on an artifact whose identifier set did not change returned 30, then 35,
then 32 findings. The variation comes from publisher bot-mitigation,
which is rate- and reputation-sensitive, so the flagged subset differs each time.
A gate assertion whose result depends on when it is run is not measuring the
artifact, and that is the substance of the objection here.

**Independent verification covers the whole corpus, not the flagged subset**,
precisely because the flagged subset is unstable. All 81 identifiers were
re-checked on 2026-08-21 by three methods that do not share the gate's failure
mode. Log:
`docs/literature/search_logs/level-definitions/g16-independent-doicheck.json`.

| check | question it answers | result |
|---|---|---|
| DOI Handle System REST, `doi.org/api/handles/{doi}` | does the global resolution system resolve this handle to a target | **81 of 81 resolved**, `responseCode = 1`, each with a publisher or repository target URL |
| Crossref REST `works/{doi}` | is the identifier registered with Crossref, and does the registered metadata match the store entry | **70 of 81 registered**, titles and publishers matching. The other 11 are the arXiv DOIs under the `10.48550` prefix, which are registered with **DataCite**, not Crossref; a Crossref 404 for them is the correct answer to the wrong question, and all 11 resolve through the Handle System |
| Browser-user-agent `GET` to `https://doi.org/{doi}` | does an ordinary client reach the publisher | 36 returned `HTTP 200`. 45 returned `HTTP 403` **from the publisher host, after `doi.org` had already redirected there** - which is only possible if resolution succeeded |

The 403s cluster by publisher - Wiley, Oxford University Press, Taylor and
Francis, World Scientific - and are access-control responses, not registration
failures. The discriminating observation is in the third row: the refusal is
issued by the publisher's own host at the end of the redirect chain, so the
identifier resolved and then the content was withheld from an unauthenticated
client. That is exactly the state the review reports for those records anyway,
since section 7 marks them `abstract-verified` or `metadata-only` and no full
text was read.

**Disposition.** This is a known instrument defect in the gate, already recorded
against the regime-classification review, which returned `block` for the same
reason on 40 identifiers. The correct remedy is a change to the gate - resolve
through the Handle API or the registration agency, or classify `403` as
`resolved-but-access-restricted` - and that change is out of scope here, because
this review may not modify the harness that judges it. Until it is made the
verdict stands at `block`, and this artifact is **not** reported as passing.

**What would change the verdict.** Nothing available inside this document. Either
the gate's resolution method changes, or 45 correctly registered, correctly
resolving records leave the corpus. Removing them to satisfy a user-agent check
would be the larger error by a wide margin, and it would delete most of the
peer-reviewed evidence in the review.
