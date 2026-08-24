---
type: protocol
slug: explosive-regime-review
date: 2026-08-24
status: frozen-on-commit
review_standard: "PRISMA 2020 (Page et al. 2021, doi:10.1136/bmj.n71); protocol per PRISMA-P 2015 (Moher et al. 2015, doi:10.1186/2046-4053-4-1); search reporting per PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z)"
registration: >
  Not registered in PROSPERO: PROSPERO accepts only reviews with health-related
  outcomes, which this methodology review has none of. The registration event
  for this protocol is its provenance commit: the file is committed BEFORE any
  search executes, and the commit records the file's SHA-256. The protocol
  cannot contain its own hash; the clone-durable carrier is the commit itself
  (per the project reproducibility contract, the Repro-Log trailer convention).
  Any post-freeze change is an amendment under section 10, never an edit to
  frozen text.
consumer: >
  docs/research_notes/research_agenda_regime-classification_2026-08-21.md,
  branch 3 (the transition event). The agenda's Rev 3 flag is binding: the
  Phillips date-stamping records' content claims rest on abstract-level
  verification and are "flagged for a full-text pass before any branch-3
  specification cites their critical values quantitatively." This review is
  that full-text pass, plus the surrounding operating-characteristics corpus.
seed_corpus: "docs/literature/lit_review_regime-naming-b_2026-08-24.md, NB-04/NB-05 and the cluster-1/cluster-5 explosive-family records; term registry docs/literature/vocabulary_regime-synonyms_2026-08-24.md, addendum row 'bubble / explosive / exuberance'"
planned_outputs:
  - docs/literature/lit_review_explosive-regime_{execution-date}.md
  - docs/literature/references_explosive-regime.json
  - docs/literature/search_logs/explosive-regime/  (raw query logs, er-* prefix)
protocol_doicheck: docs/literature/search_logs/explosive-regime/protocol-doicheck.json
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent) drafted this protocol, resolved the known-item DOIs against Crossref, and verified every cited DOI against the DOI Handle System (25/25 responseCode 1; log at the path above). No evidence search was executed at protocol time. Role per ICMJE 2026 disclosure: idea + prose + audit-support; the human author approves the frozen text by committing it."
competing_interests: none
---

# Protocol — systematic review of explosive-regime date-stamping methods

This document is a PRISMA-P 2015 protocol. Administrative items (PRISMA-P
1–5) are carried in the frontmatter and section 10; introduction items (6–7)
in sections 0–1; methods items (8–17) in sections 2–9. A full PRISMA-P item
map closes section 9.

**ADR-0003 boundary.** This repository specifies; it does not execute. The
review synthesizes PUBLISHED operating characteristics. It runs no
simulations, fits nothing, and computes no critical values. Every quantity
that would require computation on this project's own setting (intraday
futures) is a `TO COMPUTE` handoff to the executing project. The only
computations the review itself performs are review-conduct bookkeeping:
deduplication, the screening agreement statistic, and checksum/provenance
records.

## 0. Rationale (PRISMA-P 6)

The regime-classification agenda (Rev 3) records that the recursive
right-tailed unit-root family — SADF ([Phillips, Wu & Yu 2011](https://doi.org/10.1111/j.1468-2354.2010.00625.x),
*Int Econ Rev* 52:201–226), GSADF/date-stamping ([Phillips, Shi & Yu 2015](https://doi.org/10.1111/iere.12132),
*Int Econ Rev* 56:1043–1078) — is the only detector the naming sweeps
*classified* as carrying a time-t assignment null, refuting the agenda's
prior universal (d). That classification rests on abstract-depth screening
(lit_review_regime-naming-b, NB-04/NB-05). Branch 3 intends to admit the
family into its comparator set. Before any branch-3 specification cites the
family's critical values, delay behavior, or validity conditions, the
published record of those properties must be assembled at full-text depth,
against a frozen protocol, with the family's direct competitors alongside —
otherwise the agenda inherits a single-lineage view of a literature that
contains published critiques (non-stationary volatility, multiplicity across
recursive tests, periodically-collapsing alternatives).

## 1. Review question and objectives (PRISMA-P 7)

**Refined question.** For real-time explosive-regime date-stamping methods
applied to financial price and asset-price series — the recursive
right-tailed unit-root family (SADF; GSADF and its date-stamping strategy;
the PSY/BSADF real-time monitoring sequence and its limit theory
([Phillips, Shi & Yu 2015b](https://doi.org/10.1111/iere.12131)); the
reverse-regression implosion-dating extension
([Phillips & Shi 2018, *Econometric Theory*; Crossref issued 2017](https://doi.org/10.1017/s0266466617000202));
and its direct competitors as defined by the in-scope rule in §2.1 — what
operating characteristics (size, power, date-stamping accuracy and delay,
false-alarm behavior) and validity conditions (assumptions under which the
stated null's limit theory holds) are published, and what is the causality
status (real-time versus full-sample) of each published characteristic?

**PICO adaptation for method evaluation** (no health population exists;
the mapping is declared, not forced):

| Element | This review |
|---|---|
| Population | Financial price / asset-price series (any asset class, any observation frequency) to which an in-scope detector is applied or for which one is evaluated, including simulated series from stated DGPs |
| Index methods | The recursive right-tailed unit-root family named above, plus direct competitors satisfying the in-scope rule (§2.1) — anticipated from the known-item list: Chow-type and CUSUM-based bubble monitors and the persistence-change line ([Homm & Breitung 2012, *J Financial Econometrics* 10(1); Crossref issued 2011](https://doi.org/10.1093/jjfinec/nbr009); [Busetti & Taylor 2004](https://doi.org/10.1016/j.jeconom.2003.10.028)); volatility-robust and sign-based variants ([Harvey, Leybourne, Sollis & Taylor 2016](https://doi.org/10.1016/j.jempfin.2015.09.002); [Harvey, Leybourne & Zu 2019](https://doi.org/10.1017/s0266466619000057); [Harvey, Leybourne, Taylor & Zu 2024](https://doi.org/10.1111/jtsa.12784)); real-time monitoring procedures ([Astill, Harvey, Leybourne, Sollis & Taylor 2018](https://doi.org/10.1111/jtsa.12409); [Astill, Harvey, Leybourne, Taylor & Zu 2021](https://doi.org/10.1093/jjfinec/nbab009); [Phillips & Shi 2020, Handbook of Statistics 42](https://doi.org/10.1016/bs.host.2018.12.002)). The competitor set is OPEN: any method the searches locate that satisfies §2.1 enters; the list above is the anticipated floor, not a bound |
| Comparators | Each other, plus each study's stated benchmarks (the DGPs and rival tests it evaluates against) |
| Outcomes | O1 empirical size under the stated null; O2 power under stated DGPs (including periodically-collapsing alternatives — Evans 1991, §3.4); O3 date-stamping accuracy and detection delay for origination and termination; O4 false-alarm behavior across the recursive test sequence (family-wise false-detection rate, or ARL₀ where the surveillance framing is used — evaluation-criteria taxonomy per [Frisén 2003](https://doi.org/10.1111/j.1751-5823.2003.tb00205.x)); O5 validity conditions — the assumptions under which the limit theory holds (error structure, volatility specification, drift/deterministic-term specification, minimum-window rule r₀, sample-size regime); O6 causality status — whether each reported characteristic attaches to a genuinely real-time recursive statistic (data through t only, critical values fixed ex ante) or to a full-sample/retrospective procedure |

**Outcome prioritization (PRISMA-P 13).** Primary: O1–O4. Secondary: O5, O6,
and code/data availability. O6 is secondary as an *outcome* but is extracted
for every record because the consumer agenda's standing causal-time hazard
makes it load-bearing: a full-sample date-stamp reported as a time-t claim is
exactly the smoothed-probability defect the agenda catalogues.

## 2. Eligibility criteria (PRISMA-P 8) — FROZEN

Each criterion is singular and testable. Screening verdicts cite criteria by
identifier. No criterion may be reinterpreted after the first query executes;
a needed change is a §10 amendment.

### 2.1 In-scope detector rule

A procedure is an **in-scope detector** iff ALL of:

- **S-a.** Its alternative hypothesis is explosive or mildly explosive
  autoregressive behavior — an autoregressive root ρ > 1, or ρ = 1 + c/kₙ
  with c > 0 in the [Phillips & Magdalinos 2007](https://doi.org/10.1016/j.jeconom.2005.08.002)
  moderate-deviations sense.
- **S-b.** It produces a time-indexed output: a date-stamp, an online
  monitoring/stopping decision, or an episode origination/termination
  estimate — a statement that the series is in the explosive state at or
  from a specific observation.
- **S-c.** It states a null hypothesis with a reference distribution
  (derived limit theory, simulated critical values, or bootstrap), against
  which the time-indexed decision is taken.

### 2.2 Inclusion criteria

- **I1.** The record concerns at least one in-scope detector (§2.1).
- **I2.** The record does at least one of:
  - **I2a** — derives a null limit distribution, critical values, or
    consistency/delay theory for an in-scope detector (theory paper);
  - **I2b** — reports simulated operating characteristics (any of O1–O4)
    for an in-scope detector under stated DGPs (simulation study);
  - **I2c** — is an empirical application that ADDITIONALLY reports at least
    one operating characteristic with a stated null — e.g., a
    design-specific size simulation, or delay measured against a declared
    benchmark chronology. Applications reporting only test outcomes on real
    data fail I2c and are excluded under X1.
- **I3.** A persistent identifier exists (DOI, arXiv ID, or Handle-System
  handle). A record failing I3 is excluded and logged with its best locator
  (FAIR F1 gap), not silently dropped.
- **I4.** Any language, any year, any document type (journal article,
  chapter, monograph, working paper, preprint) satisfying I1–I3.

### 2.3 Exclusion criteria

- **X1.** Plain empirical applications: apply an in-scope detector to data,
  report detected episodes, no operating characteristic with a stated null.
  These are the bulk of this literature and are excluded by I2c; near-misses
  go to the item-16b table with reasons.
- **X2.** Full-sample-only bubble *existence* tests with no time-indexed
  output (variance-bounds tests, West's specification test, Diba–Grossman
  cointegration tests): fail S-b. Retained ONLY inside an included
  comparison study meeting I2 — the comparison's operating characteristics
  are the object, not the full-sample test.
- **X3.** **LPPL / log-periodic family: OUT as index method.** Decision and
  rationale in §2.5.
- **X4.** General changepoint detectors without an explosivity alternative
  (CUSUM/Page–Hinkley for mean or variance shifts, BOCPD, Bai–Perron): fail
  S-a. Covered by branch 3's other comparator line and the
  regime-method-gaps corpus; re-reviewing them here would duplicate a
  delivered sweep.
- **X5.** Pure economic theory of rational bubbles with no test procedure
  (existence/no-existence theorems, equilibrium models): fails S-b and S-c.
- **X6.** Records whose eligibility cannot be verified at any retrievable
  depth (no abstract on any queried platform, no working-paper twin, full
  text unobtainable): excluded with reason, never completed from compiler
  memory; each is a §16b row.
- **X7.** Same-work duplicates under a second identifier: deduplicated per
  §4.1, itemized in the review's ledger.

### 2.4 Bounds and tier handling

- **Date bound: none.** Rationale: the family's direct antecedents predate
  the seeds (Busetti & Taylor 2004; Phillips & Magdalinos 2007; Evans 1991),
  and the vocabulary (§3.2) is specific enough that unrestricted dates carry
  a small junk cost. A lower bound would amputate the persistence-change
  lineage the comparison literature builds on.
- **Language bound: none.** Operating-characteristics tables are numerically
  extractable regardless of prose language. Non-English records screened on
  an English abstract where one exists; otherwise the record is screened on
  translated title/abstract and its extraction depth flagged.
- **Tier handling.** Peer-reviewed, accepted-preprint, preprint, and
  institutional working papers are all admissible, each with tier RECORDED
  per record (charter: evidence tier travels with the claim; no preprint-tier
  claim treated as settled). Justification against the evidence-tier rule:
  this literature's newest robustness and monitoring results circulate as
  working papers years before journal publication (observed in the seed
  corpus: PSY circulated as SSRN/working-paper twins from 2012–2013 before
  IER 2015; the dedup ledger of the naming sweep holds the twins).
  Tier-blind *admission* with tier-labelled *use* recovers recency without
  laundering preprints into settled claims.
- **Predecessor-store overlap: re-inclusion permitted.** Deliberate deviation
  from the naming-sweep diff discipline, declared here: the sweeps were
  recall instruments and excluded prior coverage; this is a depth review
  whose corpus must be self-contained (NB-04/NB-05 are its seeds). A record
  held by a predecessor store that meets I1–I3 is re-included here, with its
  predecessor entry cross-referenced.

### 2.5 LPPL decision (X3), in full

The Johansen–Ledoit–Sornette log-periodic family
([Johansen, Ledoit & Sornette 2000](https://doi.org/10.1142/s0219024900000115))
is **out as an index method** on the eligibility rule itself, not by fiat:

1. **Fails S-c as recorded at the current screening depth.** The seed corpus
   (naming sweep NB-03) classifies its null as "partial (hazard model;
   formal existence test not stated in this record)" — the LPPL fit carries
   a crash-hazard model, not a stated reference distribution for a time-t
   explosive-state assignment.
2. **Fails S-b as published.** NB-03's causality code is R: published fits
   are episode-retrospective; a rolling implementation is possible but is
   not the published object.
3. **Scope economics.** The LPPL literature is a large econophysics subfield
   with its own estimation controversies; admitting it as an index method
   would roughly triple the corpus while answering a different question
   (parametric precursor-fitting, not null-referenced state assignment).

**Boundary kept honest:** any head-to-head comparison study that evaluates
an in-scope detector against LPPL and reports operating characteristics
enters under I2 (the comparison is in; LPPL rides along as that study's
comparator). And if the searches surface an LPPL-family paper that *does*
state a time-t assignment null with a reference distribution — i.e., passes
S-a/S-b/S-c on its own text — that paper is in-scope by rule, and its
existence is reported as a finding against reason 1. The exclusion is of
the family as currently classified, not of the possibility.

## 3. Search strategy (PRISMA-P 9, 10; PRISMA-S)

### 3.1 Information sources

| source | platform | access route |
|---|---|---|
| Crossref | Crossref REST API (api.crossref.org) | verbatim URLs, §3.2 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | verbatim URLs, §3.2–3.3 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | verbatim URLs, §3.2–3.3 |
| arXiv | arXiv API (export.arxiv.org) | verbatim URLs, §3.2 |
| SSRN | via Crossref (DOI prefix 10.2139, `query.container-title=SSRN`) — SSRN exposes no public search API | verbatim URLs, §3.2 |

Platform, not just database, is named because the same nominal database
searches differently per platform. SSRN caveat, declared in advance: Crossref
coverage of SSRN is metadata-level; if the executing session has browser/web
access it MAY additionally run the §3.2 vocabulary through SSRN's site
search and log it as a supplementary arm; if not, the absence is recorded as
a minor recall verification gap in the review's §10, not silently.

At execution: every query URL below is executed verbatim, the raw response
saved to `docs/literature/search_logs/explosive-regime/` under its query_id,
and the ISO 8601 execution date and retrieved-record count recorded at
execution time in the same write. Nothing is reconstructed afterwards
(PRISMA-S item 8). Rate-limit errors (HTTP 429) are logged as executed with
zero records and re-run verbatim under a `-b` suffix, per the naming-sweep
convention.

### 3.2 Topical queries — verbatim, ready to execute

Vocabulary source: the term registry's addendum family "bubble / explosive /
exuberance" (surface forms: bubble regime, explosive behavior/regime,
(irrational) exuberance, mildly explosive, super-exponential growth,
date-stamping) plus the method-name vocabulary (SADF, GSADF, BSADF,
sup ADF, right-tailed unit root) that names the family in its own
literature. Retrieval caps (`rows`/`per-page`/`max_results`) are
screening-budget caps on retrieval depth, not eligibility limits; total-hit
counts are preserved in the raw logs (PRISMA-S item 9). No date, language,
or type filters anywhere.

```text er-crossref-01
https://api.crossref.org/works?query.bibliographic=sup+ADF+test+explosive+behavior+bubble+date+stamping&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-02
https://api.crossref.org/works?query.bibliographic=generalized+sup+ADF+GSADF+multiple+bubbles+real+time+detection&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-03
https://api.crossref.org/works?query.bibliographic=recursive+right-tailed+unit+root+test+explosive+episodes&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-04
https://api.crossref.org/works?query.bibliographic=mildly+explosive+process+limit+theory+asset+prices&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-05
https://api.crossref.org/works?query.bibliographic=bubble+detection+tests+size+power+Monte+Carlo+comparison&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-06
https://api.crossref.org/works?query.bibliographic=CUSUM+monitoring+explosive+episodes+speculative+bubble&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-07
https://api.crossref.org/works?query.bibliographic=date+stamping+origination+termination+bubble+episodes+exuberance&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-08
https://api.crossref.org/works?query.bibliographic=testing+speculative+bubbles+comparison+alternative+methods+power&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-09
https://api.crossref.org/works?query.bibliographic=explosive+bubbles+non-stationary+volatility+wild+bootstrap+unit+root&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-10
https://api.crossref.org/works?query.bibliographic=real+time+bubble+monitoring+false+detection+delay+critical+values&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-11
https://api.crossref.org/works?query.bibliographic=explosive+bubble+date+stamping+unit+root&query.container-title=SSRN&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-crossref-12
https://api.crossref.org/works?query.bibliographic=SADF+GSADF+bubble+test+power+comparison&query.container-title=SSRN&rows=20&select=DOI,title,issued,container-title,type,abstract
```
```text er-arxiv-01
http://export.arxiv.org/api/query?search_query=abs:%22SADF%22+OR+abs:%22GSADF%22&max_results=50
```
```text er-arxiv-02
http://export.arxiv.org/api/query?search_query=abs:%22date-stamping%22+AND+abs:%22bubble%22&max_results=50
```
```text er-arxiv-03
http://export.arxiv.org/api/query?search_query=abs:%22mildly+explosive%22&max_results=50
```
```text er-arxiv-04
http://export.arxiv.org/api/query?search_query=abs:%22explosive+behavior%22+AND+cat:q-fin*&max_results=50
```
```text er-arxiv-05
http://export.arxiv.org/api/query?search_query=abs:%22right-tailed%22+AND+abs:%22unit+root%22&max_results=50
```
```text er-arxiv-06
http://export.arxiv.org/api/query?search_query=abs:%22bubble+detection%22+AND+cat:q-fin*&max_results=50
```
```text er-openalex-01
https://api.openalex.org/works?search=%22sup%20ADF%22%20bubble%20date%20stamping&per-page=25
```
```text er-openalex-02
https://api.openalex.org/works?search=%22generalized%20sup%20ADF%22%20OR%20%22GSADF%22&per-page=25
```
```text er-openalex-03
https://api.openalex.org/works?search=%22mildly%20explosive%22%20bubble%20test&per-page=25
```
```text er-openalex-04
https://api.openalex.org/works?filter=title_and_abstract.search:%22explosive%20behavior%22%20%22critical%20values%22&per-page=25
```
```text er-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=SADF%20GSADF%20bubble%20date%20stamping%20critical%20values&fields=title,year,venue,externalIds,citationCount&limit=50
```
```text er-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=recursive%20unit%20root%20explosive%20bubble%20monitoring%20size%20power&fields=title,year,venue,externalIds,citationCount&limit=50
```

24 topical discovery queries (12 Crossref incl. 2 SSRN-restricted, 6 arXiv,
4 OpenAlex, 2 Semantic Scholar).

### 3.3 Forward-citation arms — the core recall instrument

The citing literatures of the two seeds are where this family's operating
characteristics live: every simulation study, robustness critique, and
competitor comparison cites PWY 2011 or PSY 2015. Per seed, per platform:

**OpenAlex (both seeds).** Two-step, both steps logged:
1. Resolve the seed DOI to its OpenAlex work ID:
   `https://api.openalex.org/works/https://doi.org/10.1111/j.1468-2354.2010.00625.x`
   (er-fc-oa-pwy-resolve) and
   `https://api.openalex.org/works/https://doi.org/10.1111/iere.12132`
   (er-fc-oa-psy-resolve).
2. Retrieve the FULL citing set with cursor paging — no cap:
   `https://api.openalex.org/works?filter=cites:{WORK_ID}&per-page=200&cursor=*`
   (er-fc-oa-pwy, er-fc-oa-psy), iterating `cursor` until exhausted. The
   citing-set size reported by OpenAlex is recorded alongside the count
   actually retrieved; any shortfall is a verification gap.

**Semantic Scholar (both seeds).** Citations endpoint with offset paging —
no cap:
`https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/j.1468-2354.2010.00625.x/citations?fields=title,year,venue,externalIds,citationCount&limit=1000&offset={k}`
(er-fc-s2-pwy) and the same for `DOI:10.1111/iere.12132` (er-fc-s2-psy),
iterating offset until the returned page is short. Rate-limit failures are
logged and retried; if a citing set is unretrievable after retry, that arm
is a MAJOR recall verification gap in the review's §10 (the arms are the
recall instrument; a topical-query-only corpus does not satisfy this
protocol).

The union of the four arms is deduplicated against the topical retrievals
before screening. All citing records are screened at title level against
§2 — no sampling, no citation-count floor (a floor would be an unlabelled
constant selecting against recent records).

Backward citation-chasing: the reference lists of INCLUDED comparison and
simulation studies (I2b records) are hand-checked for in-scope detectors
not yet retrieved; each such addition is logged with its carrier record
(er-bc-{n}). This is bounded work (included studies only) and is the
standard PRISMA-S supplementary method.

### 3.4 Known-item list — resolved against Crossref at protocol time

Each item below was resolved by a Crossref bibliographic query on
2026-08-24 and its DOI verified against the DOI Handle System
(responseCode 1; log: `docs/literature/search_logs/explosive-regime/protocol-doicheck.json`).
None was passed through from memory. At execution each is fetched,
screened against §2 like any other record, and force-included in the
record universe (not automatically in the corpus).

| KI | record | identifier | anticipated role |
|---|---|---|---|
| KI-01 | Phillips, Wu & Yu (2011). Explosive Behavior in the 1990s Nasdaq. *Int Econ Rev* 52:201–226 | doi:10.1111/j.1468-2354.2010.00625.x | seed; SADF; adjudication (i) |
| KI-02 | Phillips, Shi & Yu (2015). Testing for Multiple Bubbles: Historical Episodes… *Int Econ Rev* 56:1043–1078 | doi:10.1111/iere.12132 | seed; GSADF/date-stamping; adjudication (i) |
| KI-03 | Phillips, Shi & Yu (2015). Testing for Multiple Bubbles: Limit Theory of Real-Time Detectors. *Int Econ Rev* | doi:10.1111/iere.12131 | limit theory companion; carries the real-time detector theory |
| KI-04 | Homm & Breitung (2012). Testing for Speculative Bubbles in Stock Markets: A Comparison of Alternative Methods. *J Financial Econometrics* 10(1) (Crossref issued 2011, online-first) | doi:10.1093/jjfinec/nbr009 | the comparison line; Chow/CUSUM competitors; O1–O2 |
| KI-05 | Phillips & Magdalinos (2007). Limit theory for moderate deviations from a unit root. *J Econometrics* | doi:10.1016/j.jeconom.2005.08.002 | mildly-explosive limit theory; O5 |
| KI-06 | Harvey, Leybourne, Sollis & Taylor (2016). Tests for explosive financial bubbles in the presence of non-stationary volatility. *J Empirical Finance* | doi:10.1016/j.jempfin.2015.09.002 | Harvey/Leybourne line; volatility validity conditions |
| KI-07 | Harvey, Leybourne & Zu (2019). Sign-based unit root tests for explosive financial bubbles… *Econometric Theory* | doi:10.1017/s0266466619000057 | Harvey/Leybourne line; robust variants |
| KI-08 | Harvey, Leybourne, Taylor & Zu (2024). A new heteroskedasticity-robust test for explosive bubbles. *J Time Series Analysis* | doi:10.1111/jtsa.12784 | Harvey/Leybourne line; recency anchor |
| KI-09 | Astill, Harvey, Leybourne, Sollis & Taylor (2018). Real-Time Monitoring for Explosive Financial Bubbles. *J Time Series Analysis* | doi:10.1111/jtsa.12409 | monitoring competitor; O3–O4 |
| KI-10 | Astill, Harvey, Leybourne, Taylor & Zu (2021). CUSUM-Based Monitoring for Explosive Episodes… *J Financial Econometrics* | doi:10.1093/jjfinec/nbab009 | CUSUM monitoring under time-varying volatility |
| KI-11 | Phillips & Shi (2018). Financial Bubble Implosion and Reverse Regression. *Econometric Theory* (Crossref issued 2017) | doi:10.1017/s0266466617000202 | Shi/Phillips monitoring line; termination dating |
| KI-12 | Phillips & Shi (2020). Real time monitoring of asset markets: Bubbles and crises. *Handbook of Statistics* 42 | doi:10.1016/bs.host.2018.12.002 | Shi/Phillips monitoring line; practice-facing statement |
| KI-13 | Busetti & Taylor (2004). Tests of stationarity against a change in persistence. *J Econometrics* | doi:10.1016/j.jeconom.2003.10.028 | persistence-change antecedent used by the comparison line |
| KI-14 | Evans (1991). Pitfalls in Testing for Explosive Bubbles in Asset Prices. *American Economic Review* 81(4) | **no DOI** — two Crossref queries (query.title variants, 2026-08-24) return no record; the pre-1997 AER back-catalog is not DOI-registered. FAIR F1 gap carried; identifier (JSTOR stable ID) to be resolved at execution, and if unresolvable the gap is a §10 verification-gap row | the periodically-collapsing DGP against which power (O2) must be read |

The task-named "Harvey/Leybourne bubble-testing line" and "Shi/Phillips
monitoring papers" resolve to KI-06…KI-08 and KI-09…KI-12 respectively; the
Crossref lookups surfaced KI-07, KI-08, and KI-10 as line members not named
in the dispatch — recorded here so the known-item list is the verified list,
not the remembered one.

### 3.5 Strategy peer review (PRISMA-S 14 / PRESS)

Not peer reviewed by a second human searcher; none exists in this project.
Mitigations, stated: vocabulary is drawn from the empirically built term
registry rather than ad hoc recall; the forward-citation arms are
vocabulary-independent (they recall whatever cites the seeds, however it is
worded), which is the structural defense against the F005-class failure
(vocabulary the query set missed); the known-item list functions as the
PRESS known-item recall check — a strategy that fails to retrieve KI-04
through KI-13 through queries or citation arms is defective, and any KI
record NOT independently retrieved by at least one query or arm is reported
in the review as a per-item recall failure.

## 4. Study records (PRISMA-P 11)

### 4.1 Data management (11a)

Raw responses per query_id under
`docs/literature/search_logs/explosive-regime/`. Deduplication:
identifier-level (DOI string; arXiv/OpenAlex ID where no DOI), then a
hand-verified same-work ledger for twins (SSRN/NBER working-paper twins of
journal records, publisher double-registrations), rule as in the
naming-sweep §5: same work iff titles match case/punctuation-insensitively
or the twin relation is documented. The ledger is itemized in the review.
Included records enter `docs/literature/references_explosive-regime.json`
(CSL-JSON) via `build_bibliography.py add --doi`; the store SHA-256 is
recorded in the review frontmatter.

### 4.2 Selection process (11b) — dual screening design

- **Two independent LLM agent sessions** (screener A, screener B), each
  receiving: the identical deduplicated record universe, this protocol's §2
  verbatim, and nothing else — no shared reasoning, no access to the other's
  verdicts, separately spawned sessions with no common conversational state.
  The screening prompt is frozen verbatim before execution and archived in
  the search-log directory (er-screening-prompt.txt).
- **Stage 1 — title/abstract:** each screener returns, per record,
  include / exclude / uncertain-promote-to-fulltext, citing the §2 criterion
  by identifier. `uncertain` counts as `include` for stage-2 promotion.
- **Stage 2 — full text:** every stage-1 survivor is assessed at full-text
  depth against §2 by both screeners. Full text unobtainable → X6, logged.
- **Agreement statistic:** Cohen's kappa
  ([Cohen 1960](https://doi.org/10.1177/001316446002000104)),
  κ = (p₀ − pₑ)/(1 − pₑ), computed by the lead session on the STAGE-1
  verdicts, binarized as include-or-promote vs exclude; p₀ = observed
  proportion of records with identical binary verdicts, pₑ = chance
  agreement from each screener's marginal include rate. Reported WITH the
  raw agreement proportion and the 2×2 count table — κ alone is not
  interpretable across prevalence. No target κ threshold is set (any cutoff
  here would be an unlabelled constant); κ is reported, and every
  disagreement is adjudicated regardless of κ.
- **Adjudication:** each disagreement goes to a third agent session, blind
  to verdict provenance (it sees the record and §2, not which screener said
  what, nor that a disagreement occurred vs a routine check), deciding
  strictly against the written criteria and citing the deciding criterion.
- **Honest compliance statement:** both screeners and the adjudicator are
  instances of the same base model (recorded with version in the review).
  This is a partial-compliance operationalization of PRISMA 2020 item 8's
  dual-human screening: the sessions are context-independent but not
  model-independent, so κ measures decoding-and-context variance, not
  inter-rater reliability between cognitively independent raters. Under
  PRISMA 2020 item 8 the model is declared as the automation tool and the
  sole effective screener class; no human second screener exists. The
  review states this in its conformance map, and κ is not presented as
  evidence of screener independence.

### 4.3 Data collection process (11c) — extraction

**Decision: single primary extractor, with independent dual re-extraction
of every numeric operating-characteristic field on every included record.**
Rationale (against the dual-on-a-subset alternative): a percentage subset
would be an unlabelled constant; full dual extraction of descriptive fields
buys little (descriptive errors are recoverable at synthesis and visible in
the evidence tables); numeric errors are the non-recoverable failure mode —
the charter's "numeric claims require the primary source" makes the
size/power/delay numbers the load-bearing content. So: one agent extracts
all fields; a second, context-independent agent re-extracts fields E9–E13
below from the source with no sight of the first extraction; mismatches are
resolved against the source text and the mismatch count reported.
Compliance status: partial (dual on load-bearing fields, single elsewhere),
declared in the conformance map.

## 5. Data items (PRISMA-P 12) — extraction fields, frozen

| field | content |
|---|---|
| E1 | identifiers (DOI/arXiv), title, authors, venue, year, tier (peer-reviewed / accepted-preprint / preprint / working-paper) |
| E2 | study type per I2 (theory / simulation / application-with-OC / comparison) |
| E3 | detectors evaluated (named; in-scope rule S-a/S-b/S-c satisfaction per detector) |
| E4 | null specification: H₀ process, drift/deterministic-term specification, error assumptions |
| E5 | critical-value provenance: derived limit distribution / simulated finite-sample / bootstrap; and for whom (which statistic, which sample-size regime) |
| E6 | DGPs used for evaluation (null DGPs; alternatives incl. collapse mechanism — Evans-type periodically collapsing yes/no) |
| E7 | minimum-window rule r₀ and any tuning constants, with the study's stated provenance for each (derived / simulated / convention) |
| E8 | causality status per reported characteristic (O6): real-time recursive vs full-sample retrospective; what information enters the statistic at decision time t |
| E9 | size results: nominal levels, sample sizes, empirical size (table/figure refs + extracted values) |
| E10 | power results: DGPs, parameterizations, empirical power (refs + values) |
| E11 | date-stamping accuracy/delay: estimator, bias/MAE/delay distributions for origination and termination (refs + values) |
| E12 | false-alarm behavior: family-wise false-detection treatment across the recursive sequence, ARL₀ or equivalent if surveillance-framed |
| E13 | validity conditions claimed (O5): assumptions stated for the limit theory; robustness failures reported (e.g., size distortion under non-stationary volatility) |
| E14 | code/data availability: named package, archive, or none |
| E15 | setting: asset class, frequency, sample span — and the transfer distance to intraday futures (free-text, feeds appraisal D8) |
| E16 | publication-bias posture fields (charter): preregistration/registry record (expected none — recorded as such, not skipped); is a critical/negative evaluation of the family the study's primary declared outcome |

## 6. Risk of bias / appraisal instrument (PRISMA-P 14)

**No standard RoB tool fits econometric method studies.** RoB 2
(Sterne et al. 2019) is for randomized trials; QUADAS-2
([Whiting et al. 2011, *Ann Intern Med*](https://doi.org/10.7326/0003-4819-155-8-201110180-00009))
for diagnostic-accuracy studies of index tests against a reference standard;
PROBAST ([Wolff et al. 2019, *Ann Intern Med*](https://doi.org/10.7326/M18-1376))
for prediction-model studies. None maps onto "does this Monte Carlo
characterize this detector honestly." This protocol therefore declares a
**project-local instrument, `CONVENTION`-labelled**, ADAPTED from the
QUADAS-2/PROBAST signalling-question design: domains, closed signalling
questions, domain-level concern judgments (low / high / unclear), and — as
in both parent instruments — **no composite numeric score**. The adaptation
inherits the parents' form, not their validation; the instrument is
unvalidated and says so wherever the review reports it.

**ER-RoB v1 — domains and signalling questions** (answered yes / no /
unclear per included study; "no" or "unclear" on any question in a domain
raises that domain's concern):

| domain | signalling question |
|---|---|
| D1 null & critical values | Q1. Is the null hypothesis stated with its drift/deterministic specification, and is the critical-value provenance explicit (derived limit theory vs simulated-only vs bootstrap)? |
| D2 size | Q2. Is empirical size reported under the stated null DGP at stated nominal levels and sample sizes? |
| D3 power & DGP realism | Q3. Is power reported under explicitly parameterized explosive alternatives? Q4. Do the alternatives include a collapse mechanism (periodically-collapsing or equivalent), rather than pure explosion only? |
| D4 date-stamping | Q5. Are origination/termination dating accuracy or detection-delay distributions reported (not just episode counts)? |
| D5 causality status | Q6. Is the procedure evaluated in its real-time form (statistic at t uses data through t only; critical values fixed ex ante), and is any full-sample variant kept distinct from the real-time claims? |
| D6 multiplicity | Q7. Is the multiplicity of the recursive test sequence addressed (family-wise false-detection control, ARL₀, or an explicit accounting of per-observation vs per-episode error rates)? |
| D7 reproducibility | Q8. Are code and/or data available such that the reported operating characteristics could be regenerated? |
| D8 applicability | Q9. Is the evaluated setting (frequency, sample length, volatility structure) close enough to the consumer setting (intraday futures) that transfer is credible — or does the study itself report frequency/volatility sensitivity? (Applicability concern, per QUADAS-2's distinct applicability axis) |

Nine signalling questions across eight domains. Applied by the primary
extractor; the dual re-extraction agent (§4.3) independently answers
Q1–Q7 for each record, disagreements resolved against the source. Domain
concerns feed the synthesis as a concern profile per study, never a score.

## 7. Synthesis plan (PRISMA-P 15)

- **15a/15b — structure.** Narrative synthesis structured BY OUTCOME DOMAIN
  (O1…O6), each domain a section with an evidence table over the included
  studies: detector × DGP/setting × reported characteristic × concern
  profile × tier. A per-detector summary table closes the synthesis:
  what is known, under which validity conditions, at which causality
  status, on whose evidence.
- **15c — meta-analysis condition, stated in advance.** Quantitative
  pooling ONLY if ≥2 studies from non-overlapping author teams report the
  same characteristic (e.g., empirical size at the same nominal level) for
  the same detector under the same DGP family with matched sample size and
  minimum-window rule. Expectation, recorded now: this condition will
  rarely or never be met — Monte Carlo designs in this literature differ in
  DGP, T, and r₀ — and the anticipated outcome is a structured
  no-meta-analysis with the condition's failure documented per
  characteristic (15d: structured summary in evidence tables, no pooled
  estimates, no vote counting presented as inference).
- **`TO COMPUTE` handoffs (ADR-0003).** Anything the synthesis identifies
  as unpublished-but-needed for branch 3 — e.g., operating characteristics
  under intraday periodicity, size under the project's deseasonalization
  policy, delay/ARL₀ at branch-3-relevant settings — is recorded as a
  `TO COMPUTE` handoff with the DGP and design sketch, never computed here.

## 8. Meta-bias assessment (PRISMA-P 16)

Funnel-plot asymmetry ([Egger et al. 1997](https://doi.org/10.1136/bmj.315.7109.629))
is generally **inapplicable to a methods literature**: there is no common
effect estimate with a standard error across studies to plot, and
"precision" has no uniform meaning across Monte Carlo designs. Declared
inapplicable-with-rationale, NOT skipped. What IS assessed, per included
detector family:

1. **Existence and uptake of critical evaluations.** Do published
   negative/critical evaluations of the family exist (size distortion,
   power failure, dating bias), and are they cited by the family's
   application literature — or does the application stream cite only the
   originating papers? (Citation-uptake check on the included corpus, not a
   new search.)
2. **Originator-favorability check.** Do comparison studies with an
   originating author among the authors reach systematically more
   favorable verdicts on that method than third-party comparisons? Reported
   descriptively over the included comparisons.
3. **Charter publication-bias fields** (E16): preregistration/registry
   records per source (expected none in econometrics — recorded as
   unknown/none per study, not skipped); whether critical results are
   primary declared outcomes or secondary asides.

## 9. Pre-specified adjudications, confidence statement, and conformance

### 9.1 Adjudications the review MUST deliver

Verdict vocabulary for (ii)–(iv), fixed now:
`assignment-null` — the stated null attaches to the state-assignment
decision at time t (the statistic is computable at t from information
through t, and its reference distribution under H₀ governs the time-t
decision); `episode-statistic-null` — the null governs statistics of
completed/ex-post episodes; `mixed`; `indeterminate-from-full-text`.

**(i) Phillips full-text confirmation.** Question: do the FULL TEXTS of
PWY 2011 (KI-01) and PSY 2015 (KI-02, with KI-03 consulted where 2015a
delegates theory to 2015b) support the agenda Rev 3 sentence "date-stamps
an explosive state in real time against derived critical values"?
Criteria, in advance — SUPPORTED iff both: (a) the date-stamping rule as
defined in the paper uses only data through t plus critical values fixed
ex ante of t; (b) the critical values used for date-stamping are delivered
by derived limit theory (asymptotic distributions stated in the paper or
its named companion), not solely by finite-sample simulation with theory
absent. PARTIAL iff (a) holds but the operational critical values are
simulated finite-sample values (theory present but not the operational
source, or right-tail response-surface values); UNSUPPORTED iff (a) fails —
including the case where the date-stamping strategy as published is
full-sample (e.g., GSADF episode dating that conditions on the whole
sample) and only a variant is real-time. The verdict must state, per
paper, WHICH statistic (SADF / GSADF / BSADF sequence) carries the
real-time property, since the agenda sentence quantifies over the family.
The verdict feeds back to the agenda as a Rev 4 edit executed by the
consumer, not by this review.

**(ii) NB-02 — Johansen & Sornette 2001**
([doi:10.21314/jor.2002.058](https://doi.org/10.21314/jor.2002.058)),
drawdown outliers. Question: does its stated null (stretched-exponential
drawdown distribution + surrogate confirmation) attach to the assignment
of a drawdown-episode state at time t, or to the distribution of completed
drawdowns ex post? Criteria: `assignment-null` iff the paper states a
decision rule executable at some time t during an episode (with the
episode boundary knowable at t or at a stated bounded lag) whose reference
distribution under the null governs that decision; `episode-statistic-null`
iff the null is fitted to and tested on the population of completed
drawdowns. The naming sweep's causality code F ("episode boundary
confirmed one move later") is the abstract-depth prior; the full text
decides.

**(iii) NB-08 — Landriault, Li & Zhang 2017**
([doi:10.1017/jpr.2017.20](https://doi.org/10.1017/jpr.2017.20)), drawdown
laws. Same criteria as (ii), applied to analytic apparatus: `assignment-null`
iff the derived first-passage laws are presented as (or directly yield) a
stopping-time test with a known null distribution for an online decision;
`episode-statistic-null` iff they characterize functionals of completed
drawdown/drawup paths without an assignment procedure. An apparatus paper
with no assignment procedure of its own but from which one is derivable
is `episode-statistic-null` with the derivability noted — derivability is
a `TO COMPUTE`-adjacent observation, not a published assignment null.

**(iv) NB-13 — Baur & Lucey 2009**
([doi:10.1016/j.jfs.2008.08.001](https://doi.org/10.1016/j.jfs.2008.08.001)),
flight-to-quality. Question: "a definition and a test" — does the test
govern day-t classification (null on the day-t assignment) or sample-level
comovement coefficients estimated over the full sample, with day labels
descriptive? Criteria: `assignment-null` iff the test statistic for a
given day's label is computable from information through that day and
carries a stated reference distribution; `episode-statistic-null` iff the
test is on regression/correlation coefficients over the sample.
Full-sample coefficient tests that *induce* day labels are
`episode-statistic-null` even though day labels exist — the null must
attach to the ASSIGNMENT, not to a parameter whose estimate labels days
retroactively.

Records (ii)–(iv) are force-screened into the record universe regardless of
query recall (they are already identified; their adjudication is a stated
deliverable). Their inclusion in the CORPUS still requires passing §2 —
if one fails eligibility (likely for NB-02/NB-08/NB-13, which are not
explosive-family detectors), it is adjudicated in a dedicated review
section as an out-of-corpus adjudication target, and the verdict is
reported with full-text citations. Adjudications feed the agenda's
"nearest unadjudicated candidates" sentence (Rev 4, consumer-side edit).

### 9.2 Confidence in cumulative evidence (PRISMA-P 17)

GRADE is built for effect estimates on health outcomes and is inapplicable
here in its scored form; declared as such. In its place, each synthesis
claim carries: the evidence tier of its supporting records (charter
hierarchy), the concern profile from ER-RoB v1, and the causality status
(O6). A claim supported only by preprint-tier or high-concern records is
flagged and may not be treated as settled downstream (charter rule).

### 9.3 PRISMA-P 2015 item map (protocol completeness)

| item | where |
|---|---|
| 1a title identification | document title + frontmatter `type: protocol` |
| 1b update | not an update of an existing review — first review on this question in the project; the naming sweep was a scoping recall instrument, not a systematic review |
| 2 registration | frontmatter `registration` (no PROSPERO — non-health; provenance commit is the registration event) |
| 3a/3b contributors | frontmatter `ai_assistance`; repository author (real-name attribution per project CLAUDE.md) approves by commit; contact via repository |
| 4 amendments | §10 |
| 5a/5b/5c support | no external funding; no sponsor; self-directed project (frontmatter `competing_interests`) |
| 6 rationale | §0 |
| 7 objectives | §1 |
| 8 eligibility | §2 |
| 9 information sources | §3.1 |
| 10 search strategy | §3.2–3.4 (verbatim, per platform, with caps declared) |
| 11a data management | §4.1 |
| 11b selection | §4.2 |
| 11c collection | §4.3 |
| 12 data items | §5 |
| 13 outcomes & prioritization | §1 (outcomes table + prioritization) |
| 14 risk of bias | §6 |
| 15a–15d synthesis | §7 |
| 16 meta-bias | §8 |
| 17 confidence | §9.2 |

### 9.4 PRISMA 2020 conformance map (anticipated, for the executed review)

Statuses fixed in advance; the executed review restates this table with
actuals. "met*" = met in adapted form with the adaptation stated.

| item | topic | anticipated status |
|---|---|---|
| 1 | title | met — identified as a systematic review |
| 2 | abstract | met — structured frontmatter + abstract section |
| 3 | rationale | met (§0 carried into the review) |
| 4 | objectives | met (§1) |
| 5 | eligibility criteria | met — frozen here, cited by identifier |
| 6 | information sources | met — per-platform with dates at execution |
| 7 | search strategies | met — verbatim, all queries incl. zero-yield |
| 8 | selection process | **partial** — dual LLM-agent screening, single base model; model+version declared as the automation tool; no human screener. κ reported with raw agreement |
| 9 | data collection | **partial** — single extractor; independent dual re-extraction of numeric OC fields and RoB Q1–Q7 only |
| 10 | data items | met (§5) |
| 11 | risk of bias | met* — project-local `CONVENTION` instrument (ER-RoB v1), unvalidated, adapted from QUADAS-2/PROBAST; no validated tool exists for the study type |
| 12 | effect measures | **inapplicable with rationale** — outcomes are native operating characteristics (size/power/delay), not effect measures; no transformation applied |
| 13 | synthesis methods | met (§7); pooling condition pre-stated |
| 14 | reporting bias | met* — §8 posture; funnel methods inapplicable, stated substitutes |
| 15 | certainty | met* — §9.2 tier + concern-profile substitute for GRADE |
| 16a/16b | flow & near-misses | met — full accounting; every near-miss with reason |
| 17 | study characteristics | met — corpus table with tier and depth flags |
| 18 | RoB results | met — ER-RoB v1 profile per study |
| 19 | individual results | met — per-study OC extraction |
| 20 | synthesis results | met — narrative by outcome domain |
| 21 | reporting-bias result | met* — §8 items 1–3 reported |
| 22 | certainty result | met* — per-claim flags |
| 23 | discussion | met — incl. limitations of single-model screening |
| 24a/24b/24c | registration, protocol, amendments | **partial** — no registry entry exists for non-health methodology reviews; this protocol + its provenance commit + §10 amendment log are the substitute, stated openly |
| 25 | support | met — none |
| 26 | competing interests | met — none |
| 27 | data/materials availability | met — CSL-JSON store, raw logs, this protocol, all tracked |

**Identity hygiene (G18 class):** no OS username, no real-name email, no
absolute home-directory paths in this protocol, the review, the store, or
the logs. Repo-relative paths throughout. Real-name *attribution* is this
repository's declared policy and is carried by git config, not by file
contents.

## 10. Amendments policy — APPEND-ONLY ADDENDUM BELOW THIS SECTION

This protocol freezes at its provenance commit (SHA-256 recorded in the
commit trailer). During execution, ANY deviation — a query that cannot
execute as written, a platform change, an eligibility edge the criteria do
not decide, a cap change — is recorded as a dated amendment entry in the
addendum section below, stating: what changed, why, at what execution stage
(before/after the affected records were seen), and which PRISMA-P item it
touches. Silent deviation is a conduct violation; an amendment logged after
the affected screening decisions were made must say so. The executed
review's frontmatter cites this protocol's path and commit hash and
enumerates the amendments it ran under. Frozen text above this section is
never edited; a superseded provision is superseded BY an addendum entry,
in place.

---

## Addendum (append-only; empty at freeze)

<!-- amendment entries: ### A{n} — {ISO date} — {stage} — {PRISMA-P item(s)} -->
