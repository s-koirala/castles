---
title: "F005 discriminating observation: forward-citation search from the seven tested level definitions, targeted search for any Class N existence test, and retrieval of the two missing modality-calibration papers"
slug: f005-class-n-tests
date: 2026-08-21
objective: "Part 1: obtain and read the two calibration papers named as blockers in branch 1 of the regime-classification agenda - Hall & York (2001) on the Silverman bandwidth test and Cheng & Hall (1998) on the excess mass and dip tests - and extract the direction and form of the Silverman test's size distortion and the scope of the Cheng-Hall calibration. Part 2: execute the discriminating observation recorded in failure_log row F005 - a forward-citation search from the seven definitions of a price level whose existence or location has been statistically tested (all Class R, Class T, or N-X), plus a targeted search for any statistical test of a path-derived (Class N) level's existence or location - and return an explicit FOUND or NONE-FOUND verdict."
review_type: scoping
standard_declared: "PRISMA-S-conformant search reporting (verbatim queries, per-source counts, ISO 8601 dates), applied to a targeted two-part retrieval rather than a full systematic review; single screener; the item-level conformance posture follows the level-definitions survey and is stated in section 5"
eligibility_inclusion:
  - "Part 1: the two named calibration papers, at any retrievable route, with full-text extraction."
  - "Part 2: any record reporting a statistical test - a stated null, a reference distribution, a significance level, or a confidence interval - of the existence or location of a price level whose locating rule is a function only of the realised path, volume, or order book (Class N under the level-definitions survey's affine criterion), including approach/breach designs of the D46 type and effect-at-level designs of the D51 type transposed to path-derived anchors."
  - "Any year, any language, any venue including preprints and working papers, with the evidence tier recorded per record."
eligibility_exclusion:
  - "Tests of Class R (round-number), Class T (tick-grid), or N-X (exogenous institutional grid) levels: these are the seven seeds' own class and are already catalogued by the level-definitions survey."
  - "Downstream-consequence tests (profitability of a rule using the level, conditional-return trading endpoints, association of levels with book depth) - the boundary fixed by the survey's section 8.6.6, applied unchanged here."
  - "The 81 records already included in the level-definitions corpus: task directive forbids re-screening them; where a candidate resolved to one of them it was marked not-re-screened."
  - "Records retrieved in error by keyword collision (the dominant exclusion, as in the parent survey)."
registration: not-registered
protocol_path: none
protocol_amendments: "The task directive fixed both parts, the seed set, the platforms, and the verdict format before any query was executed. One method addition during execution is recorded rather than backdated: a second, broader keyword net was applied to the titles not matched by the first net, after the first net's candidates showed that the relevant 52-week-high literature does not use the vocabulary of the first net. No eligibility criterion changed."
bibliography: references_f005-class-n-tests.json
bibliography_sha256: c26524e066db4d685cfba39c891814f3229dc743f8ae41efccd5186e9466bc22
n_identified: 3769
n_duplicates_removed: 1821
n_screened: 1948
n_excluded: 1941
n_included: 7
materials_availability:
  - search_logs/f005-class-n-tests/
  - references_f005-class-n-tests.json
competing_interests: none
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent) designed and executed every query, screened every record, read the two Part 1 papers and the decisive Part 2 paper in full text, and drafted this review. It is the sole screener and is declared as an automation tool under PRISMA 2020 item 8. No human second screener participated. Reproducibility log: logs/reproducibility/repro_log_4471f7f2091348dd901d083fdf8bc908.json (untracked locator; sha256 1b8da281d63eee4dc9428b3a64751c57a994643e8b1595c5d9a7c88818284be9)."
git_head_at_authoring: "6f16cd5549bd8e9f40d4883cb0ad297d2e1a055d"
pip_freeze_sha256: "51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e"
dataset_checksums: "n/a - no dataset; the corpus store digest is bibliography_sha256 above"
rng_seed: 0
model_commit: "n/a - hosted model; version identifier claude-fable-5"
---

# F005 discriminating observation, and the two missing calibration papers

## 1. Objective and scope

[failure_log.md](../../failure_log.md) row F005 records the central negative of
the level-definitions survey
([lit_review_level-definitions_2026-08-21.md](lit_review_level-definitions_2026-08-21.md)):
of 76 operational definitions of a price level, the only 7 ever tested for the
level's own existence or location (D46, D47, D48, D49, D51, D52, D54) all
require an exogenous anchor, and **no Class N definition - path-derived,
70% of the corpus - has a located existence test**. F005's layer is
`undetermined`; its recorded discriminating observation is "a forward-citation
search from the seven tested definitions, plus a targeted search for any Class N
existence test", which the survey explicitly did not run (its own section 10.2
names the absent forward-citation search as its largest recall gap). This
review runs that observation.

Part 1 is separate and narrower: branch 1 of the
[regime-classification agenda](../research_notes/research_agenda_regime-classification_2026-08-21.md)
names two calibration papers as blockers - Hall & York (2001), absent from the
corpus because it has no DOI, and Cheng & Hall (1998), absent although its DOI
is known. Both are retrieved, verified, and read here.

**Non-goals, per task directive:** this review does not edit failure_log.md
(the lead session integrates the evidence under the charter's promotion rule -
a layer changes only if the discriminating observation was obtained and points
a stated way); it does not re-screen the survey's 81 included records; it does
not touch the research agenda.

## 2. Information sources

<!-- prisma-s-1 -->
One row per executed query batch. For the fc- rows, `n_records` is the number
of citing records retrieved and carried into screening (all pages, paginated by
cursor or offset; every page URL is in the log file). Rows with `n_records` 0
are retained: they are screening-support retrievals, not identification.

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| OpenAlex citations of D46 Donaldson & Kim 1993 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-donaldson1993 | 120 |
| OpenAlex citations of D47 Ley & Varian 1994 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-leyvarian1994 | 70 |
| OpenAlex citations of D48 Harris 1991 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-harris1991 | 601 |
| OpenAlex citations of D49 Christie & Schultz 1994 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-christieschultz1994 | 770 |
| OpenAlex citations of D51 Bhattacharya et al. 2012 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-bhattacharya2012 | 31 |
| OpenAlex citations of D52 Avellaneda & Lipkin 2003 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-avellanedalipkin2003 | 76 |
| OpenAlex citations of D54 Sonnemans 2006 | OpenAlex REST API (api.openalex.org) | 2026-08-21 | fc-openalex-sonnemans2006 | 100 |
| Semantic Scholar citations of D46 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-donaldson1993 | 131 |
| Semantic Scholar citations of D47 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-leyvarian1994 | 77 |
| Semantic Scholar citations of D48 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-harris1991 | 579 |
| Semantic Scholar citations of D49 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-christieschultz1994 | 790 |
| Semantic Scholar citations of D51 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-bhattacharya2012 | 95 |
| Semantic Scholar citations of D52 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-avellanedalipkin2003 | 75 |
| Semantic Scholar citations of D54 | Semantic Scholar Academic Graph API (api.semanticscholar.org) | 2026-08-21 | fc-s2-sonnemans2006 | 110 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | dq-crossref-01 | 10 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | dq-crossref-02 | 10 |
| Crossref | Crossref REST API (api.crossref.org), title-field | 2026-08-21 | dq-crossref-03 | 10 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | dq-crossref-04 | 10 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | dq-crossref-05 | 10 |
| Crossref | Crossref REST API (api.crossref.org), topical | 2026-08-21 | dq-crossref-06 | 10 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | dq-arxiv-01 | 4 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | dq-arxiv-02 | 0 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | dq-arxiv-03 | 2 |
| arXiv | arXiv API v1 (export.arxiv.org, Atom) | 2026-08-21 | dq-arxiv-04 | 1 |
| OpenAlex full-text search | OpenAlex REST API (api.openalex.org) | 2026-08-21 | dq-openalex-01 | 25 |
| OpenAlex full-text search | OpenAlex REST API (api.openalex.org) | 2026-08-21 | dq-openalex-02 | 25 |
| OpenAlex full-text search | OpenAlex REST API (api.openalex.org) | 2026-08-21 | dq-openalex-03 | 25 |
| Statistica Sinica publisher site + Crossref + DataCite (known-item, Hall & York 2001) | WebSearch; www3.stat.sinica.edu.tw via WebFetch/curl; api.crossref.org; api.datacite.org | 2026-08-21 | ki-f005-01 | 1 |
| Handle System + Crossref + OUP (blocked) + author self-archive (known-item, Cheng & Hall 1998) | doi.org/api/handles; api.crossref.org; academic.oup.com; www.math.ntu.edu.tw via curl | 2026-08-21 | ki-f005-02 | 1 |
| Web searches supporting screening | Claude Code WebSearch tool, US region | 2026-08-21 | ws-f005-screening | 0 |
| Metadata re-retrieval supporting screening | Crossref; OpenAlex; Semantic Scholar; Handle System; arXiv; nature.com (redirect); papers.ssrn.com (403) | 2026-08-21 | screening-support-f005 | 0 |

**Total records identified: 3,769** (equals frontmatter `n_identified`).

<!-- prisma-s-2 -->
No multi-database platform search was used. OpenAlex, Semantic Scholar,
Crossref, arXiv, and DataCite were each queried through their own native REST
or Atom API; each table row is one query (paginated where the log shows
multiple page URLs). No Ovid, EBSCO, ProQuest, Web of Science, Scopus, or
Google Scholar interface was available to this agent.

<!-- prisma-s-5 -->
**This review is itself the forward-citation search** the level-definitions
survey declared missing (its section 10.2). Citing-work sets were taken from
two independent citation indexes - OpenAlex (`filter=cites:` endpoint) and
Semantic Scholar (`/citations` endpoint) - for each of the seven seed papers,
and unioned after deduplication. Per-seed deduplicated citing-work counts
screened: D46 Donaldson & Kim 158; D47 Ley & Varian 90; D48 Harris 726; D49
Christie & Schultz 1,002; D51 Bhattacharya et al. 111; D52 Avellaneda & Lipkin
99; D54 Sonnemans 136 - sum of per-seed unions 2,322; distinct across all
seeds 1,825. No backward (reference-list) search was performed: the seeds'
references predate the seeds and cannot contain a later Class N test.

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S 8: every block below was written to the search log by the executing
process at the moment of execution; none was retyped afterwards. For the API
sources the query as run is the request URL. For the fc- rows the block shows
the first-page URL; subsequent cursor/offset pages are recorded verbatim in the
same log file under `query_url_verbatim`.

```text fc-openalex-donaldson1993
https://api.openalex.org/works?filter=cites:W2123305298&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-leyvarian1994
https://api.openalex.org/works?filter=cites:W1964342500&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-harris1991
https://api.openalex.org/works?filter=cites:W2003569572&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-christieschultz1994
https://api.openalex.org/works?filter=cites:W1964211014&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-bhattacharya2012
https://api.openalex.org/works?filter=cites:W2153270647&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-avellanedalipkin2003
https://api.openalex.org/works?filter=cites:W3125836525&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-openalex-sonnemans2006
https://api.openalex.org/works?filter=cites:W3125088490&per-page=200&select=id,doi,title,publication_year,type&cursor=*
```
```text fc-s2-donaldson1993
https://api.semanticscholar.org/graph/v1/paper/DOI:10.2307/2331416/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-leyvarian1994
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/758526902/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-harris1991
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1093/rfs/4.3.389/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-christieschultz1994
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/j.1540-6261.1994.tb04782.x/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-bhattacharya2012
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1287/mnsc.1110.1364/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-avellanedalipkin2003
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1088/1469-7688/3/6/301/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text fc-s2-sonnemans2006
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.euroecorev.2005.09.001/citations?fields=title,year,externalIds&limit=500&offset=0
```
```text dq-crossref-01
https://api.crossref.org/works?query.bibliographic=support+resistance+levels+statistical+significance+test&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-crossref-02
https://api.crossref.org/works?query.bibliographic=support+resistance+levels+bootstrap+confidence+interval&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-crossref-03
https://api.crossref.org/works?query.title=existence+of+support+and+resistance+levels&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-crossref-04
https://api.crossref.org/works?query.bibliographic=pivot+point+statistical+test+null+distribution+intraday&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-crossref-05
https://api.crossref.org/works?query.bibliographic=52-week+high+anchoring+price+barrier+stock&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-crossref-06
https://api.crossref.org/works?query.bibliographic=price+clustering+previous+highs+lows+technical+levels+order+book&rows=10&select=DOI,title,issued,container-title,type,abstract
```
```text dq-arxiv-01
http://export.arxiv.org/api/query?search_query=all:%22support%20and%20resistance%22%20AND%20all:%22statistical%22%20AND%20cat:q-fin*&start=0&max_results=15&sortBy=relevance
```
```text dq-arxiv-02
http://export.arxiv.org/api/query?search_query=all:%22support%20and%20resistance%22%20AND%20all:%22bootstrap%22&start=0&max_results=15&sortBy=relevance
```
```text dq-arxiv-03
http://export.arxiv.org/api/query?search_query=all:%22resistance%20levels%22%20AND%20all:%22significance%22%20AND%20cat:q-fin*&start=0&max_results=15&sortBy=relevance
```
```text dq-arxiv-04
http://export.arxiv.org/api/query?search_query=all:%2252-week%20high%22%20AND%20cat:q-fin*&start=0&max_results=15&sortBy=relevance
```
```text dq-openalex-01
https://api.openalex.org/works?search=%22support%20and%20resistance%22%20existence%20statistical%20test%20price%20levels&per-page=25&select=id,doi,title,publication_year,type
```
```text dq-openalex-02
https://api.openalex.org/works?search=%22moving%20average%22%20%22psychological%20barrier%22&per-page=25&select=id,doi,title,publication_year,type
```
```text dq-openalex-03
https://api.openalex.org/works?search=%2252-week%20high%22%20barrier%20anchoring%20volatility&per-page=25&select=id,doi,title,publication_year,type
```
```text ki-f005-01
WebSearch: Hall York "calibration of Silverman's test for multimodality" Statistica Sinica site:www3.stat.sinica.edu.tw
then: https://www3.stat.sinica.edu.tw/statistica/j11n2/j11n28/j11n28.htm
then: https://www3.stat.sinica.edu.tw/statistica/oldpdf/A11n28.pdf
then: https://api.crossref.org/works?query.bibliographic=Hall+York+calibration+of+Silverman%27s+test+for+multimodality&rows=5&select=DOI,title,container-title,issued
then: https://api.datacite.org/dois?query=Silverman%20multimodality%20calibration&page%5Bsize%5D=5
```
```text ki-f005-02
https://doi.org/api/handles/10.1111/1467-9868.00141
then: https://api.crossref.org/works/10.1111/1467-9868.00141
then: https://academic.oup.com/jrsssb/article-pdf/60/3/579/49589002/jrsssb_60_3_579.pdf (publisher block)
then WebSearch: "Calibrating the excess mass and dip tests of modality" Cheng Hall filetype:pdf
then: https://www.math.ntu.edu.tw/~cheng/edit_cheng/calibrating.pdf
```
```text ws-f005-screening
three screening-support web searches, recorded verbatim in search_logs/f005-class-n-tests/ws-f005-screening.json; no records identified
```
```text screening-support-f005
twenty-one screening-support metadata fetches, recorded verbatim in search_logs/f005-class-n-tests/screening-support-f005.json; no records identified
```

<!-- prisma-s-9 -->
No date, language, or document-type limits were applied to any query. The
`cat:q-fin*` restriction on dq-arxiv-01 and dq-arxiv-03 is a precision device
against keyword polysemy, inherited from the parent survey's strategy, not an
eligibility limit; dq-arxiv-02 ran without it and returned zero records.

<!-- prisma-s-14 -->
The search strategy was not peer reviewed. No PRESS review was available; the
single-agent constraint is the same one declared by the parent survey.

<!-- prisma-s-16 -->
Deduplication was programmatic, in Python 3.11 standard library (no dedup
software package): key = normalized DOI (lowercased, resolver prefix stripped,
arXiv ids mapped to their 10.48550 DOI form) where present, else normalized
title (alphanumeric only, first 80 characters); plus a recorded manual merge
list of four same-work identifier pairs (arXiv/journal and SSRN/journal
versions), enumerated with the arithmetic in
[search_logs/f005-class-n-tests/screening-ledger-f005.json](search_logs/f005-class-n-tests/screening-ledger-f005.json).
3,769 identified - 1,821 duplicates = 1,948 distinct records screened.

## 4. Selection process

<!-- prisma-2020-8 -->
- **screeners_n**: 1
- **independent**: no - single screener, no duplicate screening, no agreement
  statistic, for the reason stated in the parent survey's section 1.4 (two
  passes by the same model are not independent).
- **automation_tools**: Claude Fable 5 (model id `claude-fable-5`), running as
  the `research-librarian` agent under Claude Code / Claude Agent SDK, decided
  every inclusion and exclusion. Two deterministic keyword nets (regexes
  recorded in the screening ledger) were used as a title triage aid: net 1
  matched 396 titles, net 2 matched a further 75, and all 471 were read
  individually by the screener with year and seed provenance. Titles matching
  neither net (about 1,354) were screened by the nets only and not individually
  read - a coverage limit stated plainly in section 10. Thirteen boundary
  records were adjudicated on abstract or full text.

## 5. Conformance posture

Scoping retrieval, not a full systematic review: no risk-of-bias instrument, no
certainty rating, no synthesis of effect sizes (the units are tests, not
estimates). Search reporting follows PRISMA-S items 1, 2, 5, 8, 9, 14, 16 as
anchored above; flow counts follow PRISMA 2020 item 16a and are
arithmetic-checked; exclusion reporting follows item 16b (section 6); the
selection declaration follows item 8 (section 4).

## 6. Excluded near-misses

<!-- prisma-2020-16b -->
Records that appeared to meet the Part 2 inclusion criterion on their metadata
and were excluded after adjudication, with a reason each. Bulk exclusions are
summarised after the table.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| N1 | Gomes & Waelbroeck (2010), An empirical study of liquidity dynamics and resistance and support levels, *Quantitative Finance* 10(10), doi:10.1080/14697680902814258 | abstract + definitional statement | Association of liquidity accumulation with reference price levels (levels as prices crossable with difficulty; liquidity as shares required to push price through). Same instrument class as D39 (Kavajecz & Odders-White), which the parent survey classifies as a downstream-consequence test, not an existence test. Boundary applied unchanged. |
| N2 | De Angelis & Peskir (2016), Optimal prediction of resistance and support levels, *Applied Mathematical Finance*, doi:10.1080/1350486x.2017.1297729 | abstract | Optimal-stopping theory in which the level is a hidden aspiration variable with an assumed prior law; existence is a model assumption, not a tested hypothesis. Already in the level-definitions corpus (survey note E19); not re-screened beyond this boundary check. |
| N3 | Chung & Bellotti (2021), Evidence and Behaviour of Support and Resistance Levels in Financial Time Series, arXiv:2101.07410 | not re-screened | Already included in the level-definitions corpus as D28 and adjudicated there as a downstream-consequence test ("the closest any Class N definition comes"). Task directive forbids re-screening the survey's 81 included records; the adjudication stands unrevisited. |
| N4 | Zhang, Chang & Yu (2012), Clustering analysis of Dow Jones 30 based on extreme points, doi:10.1109/csip.2012.6308960 | abstract | Clusters *stocks* by the timing of their synchronic extreme points; no price level is located or tested. Keyword collision on "extreme points". |
| N5 | Ponomarev (2013), Price Discovery in the Foreign Exchange Market: The Analysis of Highs and Lows, doi:10.2139/ssrn.2353534 | abstract | Tests non-randomness of price action after breakouts of monthly and 52-week highs and lows, but the stated endpoint is systematic alpha generation - the profitability exclusion class the parent survey fixed. Unrefereed working paper. Recorded as corroborating context for section 9.2, not as an included test. |
| N6 | Faulty Anchors: Individual Investor Order Intensity and Order Type at the 52 Week High (2017), doi:10.2139/ssrn.3021585 | title only - verification gap | No abstract retrievable from Crossref, OpenAlex, or Semantic Scholar; SSRN page returns HTTP 403 to this agent. Title indicates the D51 instrument (order behaviour at the level) transposed to a path-derived anchor, which would be a further included record if confirmed. Excluded as unadjudicable rather than ineligible; flagged to the lead session. |
| N7 | The support and resistance line method: an analysis via optimal stopping (2026), *Finance and Stochastics*, doi:10.1007/s00780-026-00596-6 | title/venue | Continuation of the N2 optimal-stopping line: analysis of the method under an assumed model, not an empirical existence test. Also retrieved by the parent survey's q-arxiv-01. |
| N8 | The implications of a price anchoring effect at the upstairs market of the London Stock Exchange (2014), doi:10.1016/j.irfa.2013.12.001 | title | Block-trade price anchoring in the upstairs market; no path-derived level located or tested. No abstract retrievable. |
| N9 | Li, Luo & Xiao, Moving Average's Role as a Psychological Barrier (2022), doi:10.2139/ssrn.4310592 | deduplication-adjacent | Not excluded on eligibility: earlier SSRN version of the included record doi:10.2139/ssrn.4486459. Its Crossref record supplied the abstract quoted in section 9.3; listed so a reader searching for either version knows both were seen and mapped. |
| N10 | Driessen, Lin & Van Hemert working paper trail and the 52-week-high momentum literature (George & Hwang tradition; e.g. doi:10.2139/ssrn.1087391, doi:10.2139/ssrn.4353530 and cognates retrieved by dq-crossref-05, dq-openalex-03) | title/abstract | Return-predictability (momentum) endpoints: downstream-consequence tests of the 52-week-high anchor, not existence tests. The existence-type designs from this family are the three included in section 9.2. |

**Bulk exclusions.** Of 1,948 screened, 1,941 were excluded. The dominant
category by far is the Class R / Class T price-clustering and round-number
barrier literature that cites the seven seeds - the seeds' own research
tradition, out of scope by eligibility criterion 1 (several hundred titles:
clustering by market, by asset class, by decade). The remainder are
microstructure, market-quality, and behavioural-finance works citing the seeds
for background; keyword collisions (sea levels, steganography, psychology of
round numbers off the price axis); and non-research items. Category counts
were not coded per record; the exact number is the total only - the same
data-collection weakness the parent survey records in its section 10.3.

## 7. Included corpus

<!-- included-corpus -->
Seven records. Tier vocabulary: 1 peer-reviewed, 5 preprint/working paper
(CLAUDE.md evidence hierarchy; tier recorded next to every claim it supports).

| id | citation | identifier | role and tier |
|---|---|---|---|
| hallyork2001statsinica | Hall & York (2001). On the calibration of Silverman's test for multimodality. *Statistica Sinica* 11(2):515-536. | none - no DOI exists (Crossref and DataCite absence confirmed by logged queries; FAIR F1 unsatisfiable for this record) | Part 1 blocker 1. Tier 1, peer-reviewed. Full text read from the publisher's open PDF. [full-text-verified] |
| cheng1998146798680014 | Cheng & Hall (1998). Calibrating the Excess Mass and Dip Tests of Modality. *JRSS-B* 60(3):579-589. | 10.1111/1467-9868.00141 (handle responseCode 1) | Part 1 blocker 2. Tier 1, peer-reviewed. Full text read from the first author's institutional self-archive. [full-text-verified] |
| garzarelli2014srep04487 | Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014). Memory effects in stock price dynamics: evidences of technical trading. *Scientific Reports* 4:4487. | 10.1038/srep04487 (arXiv:1110.5197 v1, whose author list lacks Pompa) | Part 2: the decisive Class N existence test - bounce-vs-cross at path-derived extrema against a stated null. Tier 1, peer-reviewed. Full text read (arXiv version). [full-text-verified] |
| driessen2011rfr026 | Driessen, Lin & Van Hemert (2013). How the 52-Week High and Low Affect Option-Implied Volatilities and Stock Return Moments. *Review of Finance* 17(1):369-401. | 10.1093/rof/rfr026 | Part 2: approach/breach design at a trailing-extremum level. Tier 1, peer-reviewed. [abstract-verified] |
| huddart2009mnsc10800920 | Huddart, Lang & Yetman (2009). Volume and Price Patterns Around a Stock's 52-Week Highs and Lows. *Management Science* 55(1):16-31. | 10.1287/mnsc.1080.0920 | Part 2: volume response at the crossing of a path-derived range limit. Tier 1, peer-reviewed. [abstract-verified] |
| mizrach2009096031008021 | Mizrach & Weerts (2009). Highs and lows: a behavioural and technical analysis. *Applied Financial Economics* 19(10):767-777. | 10.1080/09603100802199679 | Part 2: turnover at n-day highs/lows, increasing in n. Tier 1, peer-reviewed. [abstract-verified] |
| li2023ssrn4486459 | Li, Luo & Xiao (2023). Moving Average as a Psychological Barrier: Evidence from International Markets. SSRN working paper. | 10.2139/ssrn.4486459 (earlier version 10.2139/ssrn.4310592) | Part 2: barrier methodology at the moving average, a path-derived level. **Tier 5, unrefereed working paper** - no journal version exists in Crossref as of 2026-08-21 (logged query). [abstract-verified] |

## 8. Part 1 - the two calibration papers

### 8.1 Hall & York (2001): retrieved, read, and the size-distortion direction now stated

**Full-text route.** The paper is open access on the publisher's own site. The
abstract page is
`https://www3.stat.sinica.edu.tw/statistica/j11n2/j11n28/j11n28.htm` (its
on-page full-text link is password-gated), but the PDF is served without
authentication from the volume archive:
**`https://www3.stat.sinica.edu.tw/statistica/oldpdf/A11n28.pdf`** (282,488
bytes, retrieved 2026-08-21, read in full). Metadata confirmed from the
document itself: Peter Hall and Matthew York, Centre for Mathematics and Its
Applications, Australian National University; *Statistica Sinica* 11 (2001),
515-536. The absence of a DOI was confirmed against Crossref and DataCite by
logged queries (ki-f005-01) and matches recorded project knowledge.

**Direction of the size distortion: conservative.** The abstract's first
sentence (p. 515):

> "It is known that Silverman's bootstrap test for multimodality tends towards
> conservatism, even in large samples, in the sense that the actual level tends
> to be less than the nominal one."

**Form and magnitude** (Section 4, "Numerical Results", pp. 523-524, Table 1
"Asymptotic level of Silverman's critical bandwidth test"): simulating at
n = 10,000 from a standard normal on I = [-1.5, 1.5] (5,000 samples, 5,000
resamples each), the asymptotic actual levels at nominal levels 0.01, 0.05,
0.10, 0.20 are **0.000, 0.010, 0.032, 0.102** - roughly a factor 2 to
effectively infinite undersizing, persisting in the limit: "the critical
bandwidth test is particularly conservative, even in the limit" (p. 523). The
introduction adds the structural reason (Section 1, p. 516): "the bootstrap
part of the algorithm does not consistently estimate the distribution of the
test statistic under the null hypothesis, even up to scale or location
changes", so calibration "amounts to substantially more than adjusting its
level ... The nature of the test has to be altered."

**The calibration proposed** (Sections 2.1-2.2, pp. 517-519): reject H0 when
P(h*crit / hcrit <= lambda | data) >= 1 - alpha, with the constant lambda
chosen as a function of alpha - explicitly *not* an adjustment of the nominal
level: "we are not calibrating by adjusting the nominal level, alpha; rather,
we are calibrating by selecting an appropriate lambda for any given value of
alpha" (p. 518). Two routes: **Method 1**, asymptotic - the limiting bootstrap
distribution of the statistic depends on no unknowns (Theorem 3.2), so
lambda(alpha) is an absolute constant, tabulated and approximated by the
rational-polynomial (4.1) with the seven fitted coefficients of Table 2
(a1 = 0.94029 ... a7 = 0.42423), giving an asymptotically exact-level test;
**Method 2**, Monte Carlo calibration on samples from a unimodal density,
which additionally corrects second-order (sample-size) effects. Scope caveats
relevant to branch 1: the calibration is derived for j = 1 (one mode); for
j >= 2 the limiting distribution depends on 2j - 2 unknowns and "the bootstrap
test cannot be calibrated by simply forming the ratio" (Section 2.4, p. 520);
and the theory assumes i.i.d. sampling from a smooth compactly-supported
density (Theorem 3.1's conditions, p. 521) - it does not repair the
integrated-data defect the agenda demonstrates.

**Consequence for the agenda.** The blocker sentence "the direction of the
Silverman test's size distortion is therefore unstated" is now resolved:
**conservative (undersized), by a factor quantified in Table 1, uniformly in
the nominal levels examined, and persisting asymptotically.** An uncalibrated
Silverman route would under-reject - on i.i.d. data. This does not offset the
agenda's separate Monte Carlo finding that the dip-family nulls
over-reject on integrated data; the two defects are about different nulls on
different data-generating processes.

### 8.2 Cheng & Hall (1998): DOI verified, read, and the i.i.d.-only claim confirmed

**DOI verification.** `https://doi.org/api/handles/10.1111/1467-9868.00141`
returns `responseCode: 1` with handle target
`https://academic.oup.com/jrsssb/article/60/3/579/7083086` (log ki-f005-02).
The publisher target answers this agent's fetches with a Cloudflare challenge
- a publisher-side block, recorded and not counted as a resolution failure per
task directive. Full text was read instead from the first author's
institutional self-archive:
`https://www.math.ntu.edu.tw/~cheng/edit_cheng/calibrating.pdf` (the published
JRSS-B typescript, 60(3):579-589).

**What the calibration addresses** (Summary, p. 579, quoted from the Crossref
deposit and confirmed against the full text): the traditional dip and excess
mass tests, calibrated against "properties of samples of uniform random
variables", are so conservative that "the asymptotic levels of such tests are
zero, for each non-zero value of nominal level" (Section 1.2, p. 580). The
proposed method "exploits the fact that the limiting distribution of the
excess mass statistic under the null hypothesis depends on unknowns only
through a constant, which may be estimated" - the constant is
d = |f''(x0)| / f(x0)^3 at the mode; the calibrated test resamples from a
data-determined unimodal calibration distribution matching the estimated d and
computes Monte Carlo critical points (Section 2.3). The calibrated test "is
shown to have greater power and level accuracy than the bandwidth test has.
The latter tends to be quite conservative, even in an asymptotic sense"
(Summary) - independently corroborating section 8.1's direction, and citing
the same quantification: "for nominal levels 0.01, 0.05, 0.1 and 0.2 the
asymptotic levels of the bandwidth test are 0.000, 0.010, 0.032 and 0.102"
(Section 3, p. 583, attributed to York (1998) - the numbers that appear as
Hall & York (2001) Table 1).

**The i.i.d.-only claim: confirmed.** The agenda states the paper "addresses
the i.i.d. case only and does not repair the defect above." Correct. The
entire framework is built on "the empirical distribution function of an
n-sample drawn from F" (Section 1.3, p. 580); the resampling scheme draws
conditionally independent samples from a fitted unimodal density (Section 2.3,
p. 582); the theory (Theorems 1-3, Section 4) is stated for that sampling
model. Nowhere does the paper treat dependent, integrated, or time-series
data; no mixing condition, no block resampling, no occupation-measure setting
appears anywhere in the text. The agenda's demonstration that the dip null is
anticonservative on integrated price paths is untouched by this calibration,
which corrects a *different* (conservative, i.i.d.-side) error.

## 9. Part 2 - the F005 discriminating observation

### 9.1 The decisive record: a statistical existence test of a path-derived level

**Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014), "Memory effects
in stock price dynamics: evidences of technical trading", *Scientific Reports*
4:4487, doi:10.1038/srep04487** (read in full via arXiv:1110.5197 v1, whose
author list lacks Pompa; the published version carries five authors). Tier 1,
peer-reviewed.

- **Level definition (Class N by the survey's affine criterion).** A support
  or resistance is a previous local minimum or maximum of the price series
  subsampled at timescale tau, equipped with a stripe of width
  delta(tau) = the mean absolute price increment at that timescale (their
  eq. (1)). Every ingredient is a function of the realised path alone: local
  extrema are affine-equivariant, and the stripe width is an average of
  absolute increments - translation-invariant and scale-equivariant. The
  definition satisfies L(a p + b) = a L(p) + b exactly; it requires neither
  round numbers nor the tick grid. It is a Group B (path-extremum) rule with a
  dispersion-scaled tolerance, not identical to any of the survey's 76
  numbered definitions but squarely inside the class the survey's section
  8.6.6 declares untested.
- **The test.** "We measure the conditional probability of bounce p(b|bprev)
  given bprev previous bounces" - bounce versus cross whenever the price
  enters the stripe - estimated by Bayesian inference under a Bernoulli model,
  and compared against **"the time series of the shuffled returns of the
  price ... a time series with the same statistical properties but without any
  memory effect. As shown in the graphs, the probabilities of bounce of the
  shuffled time series are nearly 0.5 while the probabilities of bounce of the
  stock data are well above 0.5."** A chi-squared independence test at a
  declared alpha = 0.05 further establishes that p(b|bprev) *increases* with
  the number of previous bounces at timescales of 45, 60 and 90 seconds (not
  at 180 seconds).
- **Data.** Tick-by-tick prices of 9 London Stock Exchange stocks, all 251
  trading days of 2002.
- **Reading.** This is precisely the object F005 says does not exist: a
  statistical test, with a stated null and significance level, of whether
  path-derived levels deflect prices - an existence test of the Class N
  construct, not a profitability or downstream-consequence endpoint.

**Provenance caveat, stated against interest of a clean narrative.** This
record was *retrieved by the parent survey* (its q-arxiv-01 raw log contains
arXiv:1110.5197) and does not appear in its corpus, its near-miss table, or
its section 8.6.6 tally: it is among the ~309 bulk exclusions with no
per-record reason coded. It was re-found here by the direct-query arm
(dq-arxiv-01, dq-openalex-01), not by the citation graph - it cites the
econophysics literature, not the seven seeds. Both facts matter for the F005
disposition (section 9.5).

### 9.2 The 52-week-high family: approach/breach designs at a trailing extremum

The 52-week high/low is the trailing-window path extremum - the Donchian-type
construct the survey files as D59 (Class N; max/min over n periods is
affine-equivariant). Three peer-reviewed records apply to it the same two
instrument families the survey counts as existence tests for Class R levels:

- **Driessen, Lin & Van Hemert (2013), *Review of Finance* 17(1):369-401,
  doi:10.1093/rof/rfr026** - found by the **forward-citation arm**: it cites
  D46 (Donaldson & Kim) and appears in fc-openalex-donaldson1993. From the
  abstract: "IVs and stock betas decrease when approaching a high or low, and
  ... volatilities increase after breakthroughs. The effects are economically
  large and significant." Restraint on approach plus excess movement after
  breach is the D46 apparatus - transposed from multiples of 100 to a
  path-derived level.
- **Huddart, Lang & Yetman (2009), *Management Science* 55(1):16-31,
  doi:10.1287/mnsc.1080.0920** - "Volume is strikingly higher, in both
  economic and statistical terms, when the stock price crosses either the
  upper or lower limit of its past trading range", robust to controls for past
  returns and news arrival. Behavioural response *at the level crossing*.
- **Mizrach & Weerts (2009), *Applied Financial Economics* 19(10):767-777,
  doi:10.1080/09603100802199679** - "turnover rises on n-day highs and lows
  and is an increasing function of n", with persistence and post-event
  abnormal returns.

Classification honesty: these three test the *effect of the level on market
behaviour at and after its location* (the D46/D51 instrument types), not the
bounce-vs-cross deflection of the path itself; only Garzarelli tests the
latter. Whether the survey's "existence or location of the level itself"
boundary admits the approach/breach family for Class N exactly as it admitted
D46 for Class R is a taxonomy call that belongs to the lead session; the
verdict below does not depend on it.

### 9.3 The moving-average barrier: preprint-tier corroboration from the citation graph

**Li, Luo & Xiao, "Moving Average as a Psychological Barrier: Evidence from
International Markets", SSRN, doi:10.2139/ssrn.4486459** (earlier version
doi:10.2139/ssrn.4310592, whose Crossref deposit carries the abstract) - found
by the **forward-citation arm** in D46's citing set. From the abstract of the
2022 version: "We show that the moving averages (MAs) of stock market indices
act as psychological barriers and affect investors' trading. Market indices do
not move continuously near their MAs ... the MA of a stock market index exerts
significant impact on future index returns when it is crossed over, and the MA
effect is distinct from both the 52-week high and historical high effects."
The moving average is path-derived and affine-equivariant - Class N (it is the
centre line of the survey's D56/D57 band constructs). The discontinuity-near-
the-level claim is barrier-existence methodology at a Class N level. **Tier 5:
unrefereed working paper; no journal version exists in Crossref as of
2026-08-21 (logged query).** It corroborates but does not carry the verdict.

### 9.4 Verdict

**FOUND.** A statistical test of a path-derived (Class N) level's existence
exists in the peer-reviewed literature:

> Garzarelli, Cristelli, Pompa, Zaccaria & Pietronero (2014), *Scientific
> Reports* 4:4487, doi:10.1038/srep04487, tests the Class N construct "previous local
> extremum at timescale tau with dispersion-scaled stripe" and concludes that
> prices bounce on these levels with probability significantly above the ~0.5
> of a shuffled-return null, with the bounce probability increasing in the
> number of previous bounces (chi-squared, alpha = 0.05, significant at
> timescales 45-90 s; not at 180 s) - i.e., the levels exist as
> price-deflecting objects, and their strength grows with visibility,
> consistent with a self-fulfilling mechanism.

Supporting peer-reviewed records at the trailing-extremum (D59-family) level:
Driessen, Lin & Van Hemert (2013); Huddart, Lang & Yetman (2009); Mizrach &
Weerts (2009). Preprint-tier corroboration at the moving average: Li, Luo &
Xiao (2022/2023). Coverage establishing the verdict: 1,825 distinct citing
works screened across the seven seeds (per-seed counts in section 2), plus 13
direct targeted queries; the verdict is existential, so screening coverage
bounds only how much *more* might exist, not the verdict itself.

Two limits on what FOUND means, recorded so the finding is not over-read:

1. **The found tests do not satisfy the castles charter's gate.** Garzarelli's
   null is a shuffled-return (return-resampling) surrogate - exactly the class
   the regime-classification agenda rules inadmissible for branch 1's own
   test, because return resampling cannot preserve round-number clustering and
   destroys nonlinear dependence. The literature contains an existence test of
   a Class N level; it does not contain one whose null generating process
   meets charter gate condition (i). Branch 1's design work is narrowed, not
   discharged.
2. **No confidence interval on a level location was found.** F005's subsidiary
   negative ("no source reports a confidence interval on a level location")
   survives this search: Garzarelli tests deflection at given extrema; the
   52-week-high family tests behaviour at a defined location; De Angelis &
   Peskir derive median curves under an assumed prior, which is not a
   frequentist located interval. That part of the gap is intact.

### 9.5 Recommended F005 disposition (for the lead session; this review edits nothing)

The charter's promotion rule requires the discriminating observation to have
been obtained and to point a stated way. Both conditions now hold.

- **Observation obtained:** forward-citation search from all seven seeds (two
  independent citation indexes, 1,825 distinct citing works screened) plus 13
  direct targeted queries, all logged verbatim.
- **Which way it points:** to the **`data` alternative** F005 itself
  enumerated - "the tests exist but are unindexed and the survey missed them"
  - with a sharpening: one decisive test (Garzarelli 2014) was *retrieved but
  bulk-excluded* by the survey (a screening disposition, not a recall gap),
  and three peer-reviewed 52-week-high records were never retrieved (a recall
  gap of exactly the kind the survey's missing forward-citation search
  predicted, plus vocabulary mismatch: the arXiv phrase-query "support and
  resistance" does not match Garzarelli's "supports and resistances", and the
  52-week-high literature does not use the word "level" in titles).
- **Recommended row edits:** (i) layer `undetermined` -> `data`
  (survey-recall/screening artifact), citing this review; (ii) the row's
  headline sentence "not one Class N definition has ever had its existence
  tested" is **refuted as stated** and should be revised to the surviving
  narrower negatives: no Class N existence test with a charter-admissible
  null, and no confidence interval on any level location; (iii) the
  "transferable positive" claim - "the testability gap tracks the
  identification problem, not neglect" - is weakened and should be re-argued
  or withdrawn: Garzarelli tested Class N existence without an exogenous
  anchor, using a surrogate, in 2014; (iv) the level-definitions survey's
  section 8.6.6 tally ("16 tested, 60 untested") was already declared a lower
  bound by the survey; this review supplies the records that show the bound is
  not tight, and the survey's erratum decision belongs to the lead session.

## 10. Limitations and verification gaps

1. **Single screener**, no independence, no agreement statistic - inherited
   constraint, declared in section 4.
2. **Coverage of the citing-title space is net-bounded:** ~1,354 of 1,948
   distinct titles matched neither keyword net and were not individually read.
   A NONE-FOUND verdict could not have been asserted on this coverage; the
   FOUND verdict does not depend on it.
3. **Verification gaps** (severity major, per agent contract):
   - `10.2139/ssrn.3021585` ("Faulty Anchors", N6): unadjudicable - no
     abstract at any API and SSRN blocks retrieval (HTTP 403). Potentially a
     further included record.
   - Publisher blocks: academic.oup.com (Cheng & Hall - resolved via author
     self-archive), nature.com (Garzarelli - resolved via arXiv),
     papers.ssrn.com (Li-Luo-Xiao - resolved via the earlier version's
     Crossref abstract deposit; the *full text* of the Li-Luo-Xiao paper was
     not read, so its methodology is known only from its abstract).
   - Driessen, Huddart, and Mizrach were adjudicated on Crossref/OpenAlex
     abstract deposits, not full text ([abstract-verified] in section 7).
4. **Hall & York (2001) has no persistent identifier.** Confirmed against
   Crossref and DataCite (logged). The CSL-JSON entry carries the stable
   publisher URL and an explanatory note; FAIR F1 is unsatisfiable for this
   record and the store validator's error on it is expected and true, not a
   defect to repair. The research-compile gate's G13 assertion fails on this
   entry by design of the record, not of the review.
5. **No Scopus, Web of Science, or Google Scholar** was available; the
   citation graph is as complete as OpenAlex and Semantic Scholar jointly are.
   4a. **G16 gate disposition.** The research-compile gate's G16 assertion
   (script-user-agent HEAD to doi.org) reported HTTP 403 for four DOIs, with
   the flagged set differing between two runs - the same publisher-side
   intermittent bot-block class already documented for the parent survey. An
   independent triple check (Crossref registration, Handle System resolution,
   browser-user-agent GET) confirms **all six DOIs in the store are registered
   and handle-resolve (responseCode 1)**; log:
   [search_logs/f005-class-n-tests/g16-independent-doicheck-f005.json](search_logs/f005-class-n-tests/g16-independent-doicheck-f005.json).
   The G16 findings are disposed as false positives on that evidence, per the
   precedent set for the level-definitions review.
6. **Part 1 page-pointer precision:** quotations from Hall & York are cited to
   the journal pagination visible in the retrieved PDF; quotations from Cheng
   & Hall to the JRSS-B pagination of the self-archived typescript, which
   matches the published pagination (579-589).

## 11. Bibliography store

<!-- bibliography-store -->
[references_f005-class-n-tests.json](references_f005-class-n-tests.json) -
CSL-JSON, 7 entries, canonical digest in the frontmatter
(`bibliography_sha256`). Six entries carry DOIs verified against the Handle
System on 2026-08-21; the seventh (Hall & York 2001) carries the publisher URL
and a note documenting the confirmed absence of any DOI. Raw search logs:
[search_logs/f005-class-n-tests/](search_logs/f005-class-n-tests/) - 14
forward-citation logs, 13 direct-query logs, 2 known-item logs, 2
screening-support logs, 1 screening ledger, 1 independent DOI-check log.
