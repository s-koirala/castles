---
type: protocol
slug: kalshi-arbitrage-review
date: 2026-09-02
status: frozen-on-commit
review_type: scoping
review_standard: "Protocol written to PRISMA-P 2015 (Moher et al. 2015, doi:10.1186/2046-4053-4-1) and PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z), both ADAPTED for a non-clinical methods-and-markets literature. PRISMA 2020 (Page et al. 2021, doi:10.1136/bmj.n71) is NOT claimed: the items this design does not meet are enumerated by number in section 9.1."
output_class: "registered search producing a compiled corpus (research-compile skill), NOT a systematic review"
registration: >
  Not registered in PROSPERO: PROSPERO accepts only reviews with health-related
  outcomes, and this review has none. The registration event for this protocol
  is its provenance commit: the file is committed BEFORE any query executes and
  the commit records the file's SHA-256. The protocol cannot contain its own
  hash; the clone-durable carrier is the commit trailer, per the project
  reproducibility contract. The SHA-256 is computed and committed by the lead
  session, not by the drafting agent and not by the executing agent. Any
  post-freeze change is an amendment under section 10, never an edit to frozen
  text.
consumer: >
  docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md (the compiled corpus
  record) and, downstream of it,
  docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md
  (the new branch agenda). No empirical, data-acquisition, or trading-rule
  artifact consumes this protocol; those are out of scope by ADR-0003 and by the
  session's deliverable spec.
rule_adoption: >
  This branch is time-indexed financial analysis, so rules/quant-project.md and
  REVIEW.md are adopted BY EXPLICIT REFERENCE for the prediction-market branch
  and for that branch only (CLAUDE.md section Scope; recorded in
  ADR-0004-quant-rule-adoption-prediction-markets.md). At this literature-only
  stage the binding directive is REVIEW.md blocking directive 8 — every factor,
  signal, or trading rule carries a citation to published research or an in-repo
  derivation. REVIEW.md blocking directives 1-7 (look-ahead, split integrity,
  corporate-action adjustment, return convention, HAC standard errors, Sharpe
  confidence intervals, multiple testing) bind only a future EMPIRICAL stage;
  there is no data, no split, and no estimate at this stage for them to bind.
seed_corpus: "none — this is the first review on this question in the project. The known-item list in section 3.4 is a recall instrument built and identifier-verified at protocol time, not an inherited corpus."
planned_outputs:
  - docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md
  - docs/literature/references_kalshi-arbitrage.json
  - docs/literature/search_logs/kalshi-arbitrage/  (raw query logs, ka-* prefix)
protocol_doicheck: docs/literature/search_logs/kalshi-arbitrage/protocol-doicheck.json
ai_assistance: "Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK, research-librarian agent) drafted this protocol, resolved the known-item identifiers against Crossref, and verified every DOI cited anywhere in this file against the DOI Handle System (29/29 responseCode 1; log at the path above), plus one arXiv identifier against the arXiv API. NO evidence search was executed at protocol time and NO record was screened. Role per ICMJE 2026 disclosure: idea + prose + audit-support; the human author approves the frozen text by committing it."
competing_interests: none
---

# Protocol — registered search on arbitrage and market-making in binary event markets, with Kalshi as the venue of interest

This document is a PRISMA-P 2015 protocol in structure. Administrative items
(PRISMA-P 1-5) are carried in the frontmatter and section 10; introduction items
(6-7) in sections 0-1; methods items (8-17) in sections 2-8. A PRISMA-P item map
closes section 9, alongside the enumeration of PRISMA 2020 items this design
does NOT meet.

**Read section 9.1 before citing anything produced under this protocol.** What
follows registers a *search*. It does not register a systematic review, and the
corpus it produces must not be described as one.

**ADR-0003 boundary.** This repository specifies; it does not execute analysis.
The compiled corpus records what the literature *states*. It fits nothing,
acquires no market data, calls no exchange API, computes no price, and states no
tradeable rule. Anything the corpus identifies as unpublished-but-needed is a
`TO COMPUTE` handoff to an executing project, never computed here.

## 0. Rationale (PRISMA-P 6)

The project is opening a prediction-market branch. Before any branch agenda is
written, the published record on binary event contracts has to be assembled
against a frozen search, because the failure mode here is specific and known:
the trading-adjacent literature on event markets is heavily populated by
unattributed folklore rules ("the YES and NO legs must sum to a dollar, so any
gap is free money") whose published status is unverified. REVIEW.md blocking
directive 8 exists precisely to stop such a rule entering a project without a
citation or a derivation, and it cannot be applied to a corpus that was never
compiled.

A second reason the search must be frozen in advance: the venue of interest,
KalshiEX LLC, is recent relative to the literature that would bear on it. The
standing hazard is that evidence gathered on Betfair, the Iowa Electronic
Markets, PredictIt, Polymarket, or sportsbook data gets restated as a fact about
Kalshi. Section 8 fixes the separation rule in advance so that it is a
criterion, not a post-hoc judgement.

Third, search reproducibility does not follow from declaring a standard. Of 272
systematic reviews in high-impact pediatrics, cardiology, and surgery journals,
22% reported a reproducible search strategy for at least one database, 13% for
every database, and 22% reported the date the search ran; journal endorsement of
a reporting guideline was not associated with reproducibility
([Koffel & Rethlefsen 2016](https://doi.org/10.1371/journal.pone.0163309)).
Hence: verbatim queries in this file, executed as written, logged at execution
time.

## 1. Review question and objectives (PRISMA-P 7)

### 1.1 Review question

> For **binary event contracts** — claims on the realization of a verifiable
> event whose per-unit payoff is bounded and whose settlement is at one of the
> payoff endpoints, with the CFTC-designated contract market **KalshiEX LLC** as
> the venue of interest — what does the retrievable published literature
> **state** about:
> **(a)** no-arbitrage and internal-coherence conditions on contract prices
> (complementary YES/NO pricing, mutually-exclusive-and-exhaustive bundles,
> cross-market logical consistency), and measured violations of them;
> **(b)** price discrepancies between event-contract venues, and between event
> contracts and correlated instruments;
> **(c)** systematic mispricings, the favorite-longshot bias among them;
> **(d)** market-making and inventory-risk models, and the applicability
> conditions their own authors state for payoffs bounded in [0,1] with terminal
> settlement at an endpoint;
> **(e)** the transaction-cost, fee-structure, and capital-lockup frictions that
> determine whether a stated price discrepancy is an *executable* arbitrage;
> and for every item above, **is the evidence Kalshi-specific or generalized
> from another venue, and under what stated assumption does the generalization
> travel?**

**What makes it answerable and bounded.** The question asks what the literature
*states*, not what is true of Kalshi. Its answer is a corpus of attributed
claims, fully answerable from retrievable documents. It is bounded by (i) the
instrument rule in section 2.1, which excludes continuous-payoff instruments;
(ii) the contribution rule in section 2.2, which excludes records that neither
state a condition, measure a quantity, nor specify a model; and (iii) the strand
list S1-S7 in section 1.3, which is closed at freeze — a strand may be *reported
as empty*, but no strand may be added without a section 10 amendment.

### 1.2 Objectives

| # | Objective |
|---|---|
| O1 | Assemble the retrievable record of no-arbitrage / coherence conditions stated for binary event contracts, with the exact condition each source states and the market structure it assumes |
| O2 | Assemble the retrievable record of measured cross-venue and cross-instrument price discrepancies, with venue, period, and measurement method per record |
| O3 | Assemble the retrievable record of systematic mispricing findings (favorite-longshot bias and others), with the venue and wagering mechanism each was measured on |
| O4 | Assemble the market-making / inventory-risk model record, with each model's stated payoff support, objective, and applicability conditions — and whether the source itself addresses bounded [0,1] payoffs with terminal settlement at an endpoint |
| O5 | Assemble the friction record: fees, spreads, commissions, collateral and capital lockup, and any published treatment of when a discrepancy net of frictions is executable |
| O6 | Record, per included record, the venue the evidence comes from, so that section 8's Kalshi-specific vs generalized separation is mechanical rather than reconstructed |
| O7 | Record venue-structural facts about Kalshi from the documentation tier (section 2.7), each with document identity, version, and retrieval date |
| O8 | Record the gaps: strands for which the search returns nothing eligible, reported as findings rather than as silence |

**Objective prioritization (PRISMA-P 13).** Primary: O1, O4, O5 — these carry
the conditions under which any later empirical work would even be well posed.
Secondary: O2, O3, O7, O8. O6 is not prioritized because it is extracted for
*every* record unconditionally; it is the input to section 8, not an outcome
competing with the others.

### 1.3 Strands, closed at freeze

| strand | content |
|---|---|
| S1 | No-arbitrage and internal coherence for binary contracts |
| S2 | Cross-venue and cross-instrument price discrepancies |
| S3 | Favorite-longshot bias and other systematic mispricings |
| S4 | Market making, inventory risk, market scoring rules, automated market makers |
| S5 | Transaction costs, fees, collateral, capital lockup, executability |
| S6 | Microstructure of binary / limited-payoff instruments generally |
| S7 | Venue-structural facts about Kalshi (documentation tier only — section 2.7) |

## 2. Eligibility criteria (PRISMA-P 8) — FROZEN

Each criterion is singular and, where possible, decidable from the record's
title, abstract, and metadata without a judgement call. Where a judgement call
is unavoidable, section 2.6 states the rule that decides it. Screening verdicts
cite criteria by identifier. **No criterion may be reinterpreted after the first
query executes**; a needed change is a section 10 amendment.

### 2.1 In-scope instrument rule

An instrument is an **in-scope instrument** iff ALL of:

- **B-a.** Its payoff is a function of the realization of a **verifiable event**
  (an outcome that is adjudicated and settled), not of a continuously
  distributed price level. Contracts whose payoff is a continuous function of an
  underlying (vanilla options, futures, swaps) fail B-a.
- **B-b.** Its per-unit payoff at settlement takes **finitely many values and is
  bounded**, and the canonical case — the case the review question is about — is
  a payoff of exactly one unit on the event and zero otherwise. Parimutuel
  claims, fixed-odds bets, and cash-or-nothing binary options satisfy B-b.
- **B-c.** Its price is, or is convertible by a rule the source states to, an
  **implied probability in [0,1]** for the event.
- **B-d.** It is **traded** — on an exchange, betting exchange, bookmaker book,
  parimutuel pool, or automated market maker. A probability *elicited* from
  forecasters without a transferable traded claim (a survey, a scoring-rule
  tournament with no position) fails B-d.

### 2.2 In-scope contribution rule

A record makes an **in-scope contribution** iff it does at least one of:

- **C1 (condition).** States, derives, or tests a no-arbitrage, coherence, or
  internal-consistency condition on prices of in-scope instruments (S1).
- **C2 (measurement).** Measures price discrepancies, mispricing, bias,
  efficiency, or execution outcomes on in-scope instruments, reporting a
  quantity and the data it came from (S2, S3, S5).
- **C3 (model).** Specifies a market-making, inventory-risk,
  market-scoring-rule, or automated-market-maker model with a stated objective
  and stated applicability conditions, whether or not it is applied to in-scope
  instruments — see the transfer clause below (S4).
- **C4 (microstructure).** Analyses the microstructure of in-scope or
  limited-payoff instruments: spread formation, adverse selection, liquidity
  provision, order-flow informativeness (S6).

**Transfer clause for C3, stated in advance.** The market-making literature is
largely written for unbounded-payoff instruments. A C3 record whose instrument
is not in-scope under 2.1 is **eligible only if** the corpus can state what the
record's own text says about its payoff support and applicability conditions —
i.e. the record is admitted as a *model whose transfer must be argued*, and
extraction field E10 records the transfer status. It is never admitted as
evidence *about* binary contracts. A C3 record that states no applicability
condition and no payoff-support assumption is excluded under X6.

### 2.3 Inclusion criteria

- **I1.** The record concerns at least one in-scope instrument (2.1), OR is a C3
  model record admitted under the transfer clause (2.2).
- **I2.** The record makes at least one in-scope contribution C1-C4 (2.2).
- **I3.** A persistent identifier exists: DOI, arXiv id, RePEc handle, or
  Handle-System handle. A record failing I3 is excluded and logged with its best
  available locator (a FAIR F1 gap,
  [Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)), never
  silently dropped.
- **I4.** The record is retrievable at least to abstract depth by the executing
  agent. Records retrievable only as a bare title are excluded under X8.
- **I5.** Any language, any year, any document type (journal article, conference
  proceedings, chapter, monograph, working paper, preprint) satisfying I1-I4.
- **I6.** Documentation-tier venue records are governed by section 2.7 and are
  **not** screened against I1-I5; they enter a separate stream and are never
  counted in the peer-reviewed corpus flow.

### 2.4 Exclusion criteria

Every excluded record carries exactly one primary exclusion code — the first
that applies, in the order below — and may carry secondary codes.

- **X1 — not an in-scope instrument.** Fails 2.1 and is not a C3 transfer-clause
  record. Includes continuous-payoff derivatives, equity/FX/commodity
  microstructure with no binary claim, and general forecasting research with no
  traded claim.
- **X2 — no in-scope contribution.** Satisfies 2.1 but makes none of C1-C4:
  descriptive commentary, policy opinion, or a report of event-market prices
  with no condition, measurement, or model.
- **X3 — elicitation without trade.** Probability elicitation, forecasting
  tournaments, expert aggregation, scoring-rule *evaluation* with no
  transferable traded claim. Fails B-d.
- **X4 — pure decision or social-choice theory.** Information-aggregation
  theorems, mechanism-design results, and welfare analyses with no price
  condition, no measurement, and no market-maker specification.
- **X5 — blockchain/AMM mechanics without an event claim.** Constant-function
  market makers, liquidity-pool impermanent-loss analyses, and DEX microstructure
  where the traded object is a token pair rather than an event claim. Fails B-a.
  Retained ONLY where the same record also treats an event-claim market — then
  it is included on that part and E10 records the split.
- **X6 — model with no stated applicability condition.** A C3 record that states
  neither payoff support nor an applicability condition, so the transfer clause
  has nothing to record.
- **X7 — no persistent identifier.** Fails I3.
- **X8 — not retrievable to abstract depth.** Fails I4. Never completed from
  compiler memory; each instance is a table row with its best locator.
- **X9 — duplicate.** Same work under a second identifier; deduplicated per
  section 4.1 and itemized in the ledger.

### 2.5 Bounds and tier handling

- **Date bound: NONE.** Rationale, not convention: the conditions in S1 and the
  bias record in S3 have their primary statements decades before any
  CFTC-regulated event exchange existed (the known-item list in section 3.4
  contains verified records from 1981 onward), and the inventory-risk lineage in
  S4 begins in the same period. A lower bound would amputate exactly the
  foundational statements the question asks for, and an upper bound is
  meaningless for a search executed once. The absence of a date limit is
  recorded affirmatively, per PRISMA-S item 9.
- **Language bound: NONE.** Conditions, measured quantities, and model
  specifications are extractable from formulae and tables regardless of prose
  language. A non-English record is screened on an English abstract where one
  exists; otherwise on a translated title/abstract, with extraction depth
  flagged in E17.
- **Publication status: preprints and working papers ADMITTED**, with tier
  recorded per record. Justification against the CLAUDE.md evidence hierarchy:
  in this literature the working-paper stream (NBER, SSRN, RePEc, arXiv q-fin
  and cs.GT) carries results years before journal publication, and the venue of
  interest is recent enough that excluding preprints would bias the corpus
  toward the pre-Kalshi era. Tier-blind *admission* with tier-labelled *use* is
  the operationalization: no preprint-tier claim is reported as settled, and the
  tier travels with the claim into the corpus record's role column.
- **Evidence tier vocabulary** (CLAUDE.md evidence hierarchy): T1 peer-reviewed
  literature; T2 official documentation; T3 professional standards; T4 vetted
  technical forums; T5 anything else, admissible only with the tier recorded
  next to the claim it supports. Every included record carries its tier.

### 2.6 Decision rules for the unavoidable judgement calls

Six calls cannot be made mechanically from metadata. Each is decided by the rule
below, fixed at freeze; the screening log records the rule identifier applied.

- **J1 — fixed-odds sportsbook records.** IN SCOPE. Decision rule: a fixed-odds
  bet satisfies B-a, B-b, B-d, and satisfies B-c whenever the source states an
  odds-to-implied-probability conversion (including a stated overround
  normalization). If the source reports only odds and states no conversion, the
  record still passes B-c because that conversion is arithmetic and universal in
  the literature; the *absence* of an overround treatment is recorded in E12 as
  a friction-handling gap, never used as an exclusion.
- **J2 — parimutuel versus order-book venues.** BOTH in scope. The wagering
  mechanism (parimutuel pool, continuous double auction, bookmaker book,
  automated market maker) is an **extraction field (E6), not an eligibility
  filter**, because the review question asks about coherence conditions and
  frictions whose form depends on the mechanism. Excluding parimutuel records
  would remove most of the S3 record; excluding order-book records would remove
  most of the S1 and S6 record.
- **J3 — "prediction market" used metaphorically.** OUT. Decision rule: if the
  record's own text does not identify a market in which a claim is bought and
  sold, X3 applies, regardless of the phrase appearing in the title.
- **J4 — market-making records on unbounded instruments.** Decided entirely by
  the transfer clause in 2.2 plus X6. No separate judgement is exercised: state
  applicability conditions and the record is in, with transfer status recorded;
  state none and X6 applies.
- **J5 — venue-structural claims inside a peer-reviewed record.** A
  peer-reviewed record that describes Kalshi's rules, fees, or contract
  specifications is included as a T1 record for its C1-C4 contribution, but its
  venue-structural descriptions are extracted into the S7 stream **flagged as
  second-hand** and must be checked against the documentation-tier source (2.7)
  before the corpus record states them. Where they conflict, the corpus reports
  both and the discrepancy, and settles nothing.
- **J6 — same work, journal and working-paper twin.** X9 applies to the pair;
  the **journal version is retained** as the corpus entry and the twin is
  recorded in the dedup ledger, because tier travels with the claim and the
  higher tier is the honest label. Where the twin contains material the journal
  version dropped, both are retained and the relation recorded — the ledger says
  which.

### 2.7 Documentation-tier venue stream (S7) — separate, and separately constrained

Kalshi venue-structural facts come from the CFTC public record, the Federal
Register, the eCFR, and Kalshi's own filed rulebook. These are **T2 official
documentation** under the CLAUDE.md hierarchy, not peer-reviewed literature.
They are handled as a distinct stream with four constraints, all frozen here:

1. **They establish venue-structural facts only** — contract specification,
   settlement rule, fee schedule, position limits, membership and market-maker
   arrangements, designation and self-certification status. They may never
   establish a behavioural, empirical, or efficiency claim.
2. **They are never counted in the corpus flow.** The identified / screened /
   excluded / included counts in the corpus record cover the S1-S6 literature
   stream only. The S7 stream is reported as its own table with its own counts.
3. **Every S7 fact carries document identity, version or effective date, and ISO
   8601 retrieval date**, because rulebooks and fee schedules are revised and an
   undated rulebook citation is unverifiable at any later moment.
4. **Filer-published material is labelled as such.** A rulebook is the filer's
   own document; the CFTC public record shows what was filed and its regulatory
   status, not that the contents are independently verified. The corpus record
   says "as filed" or "as stated in the rulebook", never "Kalshi charges", where
   only the filed document is the source.

## 3. Search strategy (PRISMA-P 9, 10; PRISMA-S)

### 3.1 Information sources (PRISMA-S 1, 2, 3)

| source | platform / interface | access route |
|---|---|---|
| Crossref | Crossref REST API (api.crossref.org) | verbatim URLs, 3.2 |
| OpenAlex | OpenAlex REST API (api.openalex.org) | verbatim URLs, 3.2-3.3 |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | verbatim URLs, 3.2-3.3 |
| arXiv | arXiv API (export.arxiv.org) | verbatim URLs, 3.2 |
| SSRN | via Crossref (`query.container-title=SSRN`; DOI prefix 10.2139) — SSRN exposes no public search API | verbatim URLs, 3.2 |
| NBER | NBER working-paper listing API (www.nber.org/api/v1/...) AND via Crossref prefix filter `10.3386` | verbatim URLs, 3.2 |
| RePEc / IDEAS | IDEAS htsearch interface (ideas.repec.org/cgi-bin/htsearch) | verbatim URLs, 3.2 |
| Federal Register | Federal Register REST API (federalregister.gov/api/v1) | verbatim URLs, 3.5 — S7 stream only |
| CFTC public record | www.cftc.gov (DCM list, industry filings) | verbatim URLs, 3.5 — S7 stream only |
| eCFR | ecfr.gov | verbatim URL, 3.5 — S7 stream only |
| Kalshi rulebook | kalshi.com (filer-published) | verbatim URL, 3.5 — S7 stream only |

**Platform is named, not just the database**, because the same nominal database
searches differently through different interfaces
([Cochrane Handbook ch. 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04);
PRISMA-S items 1-2).

**RePEc and NBER are added beyond the dispatch-named source set**, with a
reason: this question's economics literature circulates through RePEc-indexed
working-paper series that Crossref covers unevenly, and NBER's own listing API
returns papers whose Crossref registration lags. Adding them is a recall
decision, recorded here rather than taken at execution.

**SSRN caveat, declared in advance.** SSRN has no public search API; the two
Crossref container-restricted queries are metadata-level only. If the executing
session has browser access it MAY additionally run the section 3.2 vocabulary
through SSRN's site search as a supplementary arm, logging it verbatim; if not,
the absence is recorded as a minor recall verification gap in the corpus record,
not passed over in silence.

**Anticipated access gap AG-1.** `https://kalshi.com/regulatory/rulebook`
returned HTTP 429 to an unauthenticated request at protocol time (recorded in
the doicheck log). If it is still unreachable at execution, the S7 stream
records the gap and falls back to the CFTC public record and the Federal
Register for whatever venue-structural facts those carry; it does not substitute
recalled content for a fetch.

**Execution discipline.** Every query below is executed **verbatim**. The raw
response is saved under `docs/literature/search_logs/kalshi-arbitrage/` under
its query id, and the ISO 8601 execution date, HTTP status, platform-reported
total-hit count, and retrieved-record count are written in the same write, at
execution time. Nothing is reconstructed afterwards (PRISMA-S item 8). HTTP 429
or other transient failure is logged as executed-with-zero-records and re-run
verbatim under a `-b` suffix; if that also fails, a retry-until-200 re-run under
a `-c` suffix, with the retry count recorded — `CONVENTION`, inherited verbatim
from the executed practice of
`docs/methodology/protocol_explosive-regime-review_2026-08-24.md` (section 3.1
and its amendment A2). Query URLs remain byte-identical across retries; only the
suffix and retry count differ.

**Retrieval caps.** `rows=20` (Crossref), `per-page=25` (OpenAlex),
`max_results=50` (arXiv), `limit=50` (Semantic Scholar), `perPage=50` (NBER) are
`CONVENTION` — the house convention carried from
`protocol_explosive-regime-review_2026-08-24.md` section 3.2, adopted here so
that screening budget is comparable across this project's protocols. They are
**caps on retrieval depth, not eligibility limits**: the total-hit count reported
by each platform is preserved in the raw log even when it exceeds the cap
(PRISMA-S item 9), and any query whose total-hit count exceeds its cap is
flagged in the corpus record as a depth-truncation gap.

**Filters.** No date filter, no language filter, and no document-type filter is
applied anywhere in section 3.2. The only subject filters are the arXiv category
restrictions on `ka-arxiv-03` and `ka-arxiv-05`, which are `CONVENTION` — the
arXiv-category-narrowing convention used in
`protocol_explosive-regime-review_2026-08-24.md` section 3.2, applied only to
the two queries whose bare phrases ("market making", "binary option") return
predominantly out-of-domain physics and mathematics records. The unrestricted
forms of those phrases are covered by `ka-crossref-07`, `ka-crossref-11`,
`ka-openalex-06`, and `ka-s2-02`, so no vocabulary is category-gated out of the
strategy as a whole.

### 3.2 Topical queries — verbatim, ready to paste

Vocabulary source: the strand list S1-S7 (section 1.3), expanded with the
surface forms the known-item records use in their own titles and venues
(verified metadata, section 3.4) — "prediction market", "event contract",
"betting exchange", "parimutuel", "favorite-longshot bias", "market scoring
rule", "automated market maker", "inventory risk", "no-arbitrage", "binary
option". No term in the strategy comes from unverified recall.

#### Crossref (15)

```text ka-crossref-01
https://api.crossref.org/works?query.bibliographic=prediction+market+arbitrage+no+arbitrage+bounds+binary+contracts&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-02
https://api.crossref.org/works?query.bibliographic=coherence+probability+prices+mutually+exclusive+exhaustive+outcomes+sum+to+one&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-03
https://api.crossref.org/works?query.bibliographic=cross+market+arbitrage+betting+exchange+bookmaker+price+discrepancy&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-04
https://api.crossref.org/works?query.bibliographic=prediction+market+prices+compared+with+options+futures+implied+probabilities&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-05
https://api.crossref.org/works?query.bibliographic=favorite+longshot+bias+betting+markets+explanations&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-06
https://api.crossref.org/works?query.bibliographic=prediction+market+forecast+accuracy+calibration+bias+event+contracts&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-07
https://api.crossref.org/works?query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-08
https://api.crossref.org/works?query.bibliographic=automated+market+maker+logarithmic+market+scoring+rule+bounded+loss+liquidity&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-09
https://api.crossref.org/works?query.bibliographic=transaction+costs+commission+fees+betting+exchange+arbitrage+profitability&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-10
https://api.crossref.org/works?query.bibliographic=collateral+margin+capital+lockup+event+contract+settlement+risk&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-11
https://api.crossref.org/works?query.bibliographic=binary+option+microstructure+bid+ask+spread+informed+trading&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-12
https://api.crossref.org/works?query.bibliographic=Kalshi+regulated+event+contract+exchange+prediction+market+design&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-13
https://api.crossref.org/works?query.bibliographic=prediction+market+arbitrage+market+making&query.container-title=SSRN&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-14
https://api.crossref.org/works?query.bibliographic=event+contracts+Kalshi+Polymarket+PredictIt&query.container-title=SSRN&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```
```text ka-crossref-15
https://api.crossref.org/works?query.bibliographic=prediction+markets+event+contracts+betting+market+efficiency&filter=prefix:10.3386&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```

#### OpenAlex (6)

```text ka-openalex-01
https://api.openalex.org/works?search=%22prediction%20market%22%20arbitrage&per-page=25
```
```text ka-openalex-02
https://api.openalex.org/works?search=%22favorite-longshot%20bias%22&per-page=25
```
```text ka-openalex-03
https://api.openalex.org/works?search=%22market%20scoring%20rule%22%20OR%20%22automated%20market%20maker%22&per-page=25
```
```text ka-openalex-04
https://api.openalex.org/works?search=%22betting%20exchange%22%20arbitrage%20efficiency&per-page=25
```
```text ka-openalex-05
https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20prediction%20market&per-page=25
```
```text ka-openalex-06
https://api.openalex.org/works?search=%22inventory%20risk%22%20market%20making%20optimal%20quotes&per-page=25
```

#### arXiv (6)

```text ka-arxiv-01
https://export.arxiv.org/api/query?search_query=abs:%22prediction%20market%22%20AND%20abs:%22arbitrage%22&max_results=50
```
```text ka-arxiv-02
https://export.arxiv.org/api/query?search_query=abs:%22market%20scoring%20rule%22%20OR%20abs:%22automated%20market%20maker%22&max_results=50
```
```text ka-arxiv-03
https://export.arxiv.org/api/query?search_query=abs:%22market%20making%22%20AND%20abs:%22inventory%22%20AND%20cat:q-fin*&max_results=50
```
```text ka-arxiv-04
https://export.arxiv.org/api/query?search_query=abs:%22favorite-longshot%22%20OR%20abs:%22longshot%20bias%22&max_results=50
```
```text ka-arxiv-05
https://export.arxiv.org/api/query?search_query=abs:%22binary%20option%22%20AND%20cat:q-fin*&max_results=50
```
```text ka-arxiv-06
https://export.arxiv.org/api/query?search_query=abs:%22Kalshi%22%20OR%20abs:%22Polymarket%22%20OR%20abs:%22PredictIt%22&max_results=50
```

#### Semantic Scholar (4)

```text ka-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=prediction%20market%20arbitrage%20no-arbitrage%20bounds&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20making%20inventory%20risk%20binary%20event%20contracts&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-03
https://api.semanticscholar.org/graph/v1/paper/search?query=favorite%20longshot%20bias%20prediction%20markets&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-04
https://api.semanticscholar.org/graph/v1/paper/search?query=event%20contract%20exchange%20prediction%20market%20microstructure&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```

#### NBER (2)

```text ka-nber-01
https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search?page=1&perPage=50&q=prediction%20markets
```
```text ka-nber-02
https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search?page=1&perPage=50&q=betting%20market%20arbitrage
```

#### RePEc / IDEAS (2)

```text ka-repec-01
https://ideas.repec.org/cgi-bin/htsearch?q=prediction+market+arbitrage
```
```text ka-repec-02
https://ideas.repec.org/cgi-bin/htsearch?q=favorite+longshot+bias
```

**Count: 35 topical discovery queries** — 15 Crossref (of which 2
SSRN-container-restricted and 1 NBER-prefix-restricted), 6 OpenAlex, 6 arXiv, 4
Semantic Scholar, 2 NBER, 2 RePEc/IDEAS. Six further documentation-stream
queries are in section 3.5.

### 3.3 Forward-citation arm — the vocabulary-independent recall instrument

Topical queries recall only what the strategy's vocabulary anticipates. The
forward-citation arm recalls whatever cites an anchor, however it is worded, and
is therefore the structural defence against a vocabulary miss.

**Anchor selection rule, derived rather than chosen by count:** exactly one
anchor per literature strand S1-S6, being the known-item record for that strand
whose citing literature is broadest among the verified items.

| anchor | strand | DOI |
|---|---|---|
| A1 Oliven & Rietz (2004) | S1 | 10.1287/mnsc.1040.0191 |
| A2 Franck, Verbeek & Nüesch (2013) | S2 | 10.1111/ecca.12009 |
| A3 Snowberg & Wolfers (2010) | S3 | 10.1086/655844 |
| A4 Hanson (2003) | S4 | 10.1023/A:1022058209073 |
| A5 Levitt (2004) | S5 | 10.1111/j.1468-0297.2004.00207.x |
| A6 Glosten & Milgrom (1985) | S6 | 10.1016/0304-405X(85)90044-3 |

**OpenAlex, per anchor, two steps, both logged.**

1. Resolve the anchor DOI to its OpenAlex work id:
   `https://api.openalex.org/works/https://doi.org/{ANCHOR_DOI}`
   (query ids `ka-fc-oa-a1-resolve` … `ka-fc-oa-a6-resolve`).
2. Retrieve the citing set with cursor paging, **no cap**:
   `https://api.openalex.org/works?filter=cites:{WORK_ID}&per-page=200&cursor=*`
   (`ka-fc-oa-a1` … `ka-fc-oa-a6`), iterating `cursor` until exhausted. The
   citing-set size OpenAlex reports is recorded alongside the count actually
   retrieved; any shortfall is a verification gap in the corpus record.

**Semantic Scholar, per anchor, offset paging, no cap.**

`https://api.semanticscholar.org/graph/v1/paper/DOI:{ANCHOR_DOI}/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset={k}`
(`ka-fc-s2-a1` … `ka-fc-s2-a6`), iterating `offset` until a short page returns.

**Scale note and its consequence, decided in advance.** A6 (Glosten & Milgrom)
has a very large citing literature, most of it out of scope under X1. It is
retained as the S6 anchor because no narrower record spans that strand, and its
citing set is screened at **title level** against section 2 like every other arm
— **no sampling and no citation-count floor**, since either would be an
unlabelled constant selecting against recent work. If the A6 arm cannot be
retrieved in full, that is a MAJOR recall verification gap recorded in the
corpus record, and the corpus states that S6 rests on the topical queries plus
the known-item arm alone.

**Backward citation-chasing.** The reference lists of INCLUDED C1 and C3 records
are hand-checked for in-scope work not otherwise retrieved; each addition is
logged with the carrier record (`ka-bc-{n}`). Bounded to included records;
standard PRISMA-S supplementary method.

The union of topical, forward-citation, known-item, and backward arms is
deduplicated (section 4.1) before screening.

### 3.4 Known-item arm — the recall check, resolved and identifier-verified at protocol time

Every identifier below was resolved against the Crossref REST API on
**2026-09-02** and verified against the **DOI Handle System** (`responseCode` 1
for all 29 DOIs cited anywhere in this protocol; the one arXiv identifier
verified against the arXiv API). The verification record — retrieved title,
container, volume/issue/page, author surnames and issued date per identifier —
is `docs/literature/search_logs/kalshi-arbitrage/protocol-doicheck.json`.
**No identifier here was written from memory.**

**Set-size rule, derived rather than chosen:** (a) at least two verified anchors
per strand S1-S6 where the strand admits two, so a strand cannot pass the recall
check on a single lucky retrieval; and (b) every model lineage named explicitly
in the review question — Glosten-Milgrom, Avellaneda-Stoikov and successors,
LMSR and other automated market scoring rules — carries its own verified anchor.
The 23 rows below are the output of that rule. The rule is frozen; the count is
its consequence.

| KI | record (verified metadata) | identifier | strand | anticipated role |
|---|---|---|---|---|
| KI-01 | Oliven K, Rietz T (2004). Suckers Are Born but Markets Are Made: Individual Rationality, Arbitrage, and Market Efficiency on an Electronic Futures Market. *Management Science* 50(3):336-351 | doi:10.1287/mnsc.1040.0191 | S1, S2 | recall anchor for arbitrage relations in a binary event market |
| KI-02 | Manski C (2006). Interpreting the predictions of prediction markets. *Economics Letters* 91(3):425-429 | doi:10.1016/j.econlet.2006.01.004 | S1 | recall anchor for what a contract price does and does not identify |
| KI-03 | Wolfers J, Zitzewitz E (2006). Interpreting Prediction Market Prices as Probabilities. NBER Working Paper 12200 | doi:10.3386/w12200 | S1 | working-paper-tier twin test for the dedup ledger and J6 |
| KI-04 | Wolfers J, Zitzewitz E (2004). Prediction Markets. *Journal of Economic Perspectives* 18(2):107-126 | doi:10.1257/0895330041371321 | S1, S3 | survey-tier recall anchor; used for its bibliography, not as primary evidence |
| KI-05 | Berg J, Forsythe R, Nelson F, Rietz T (2008). Results from a Dozen Years of Election Futures Markets Research. *Handbook of Experimental Economics Results*, ch. 80, 742-751 | doi:10.1016/S1574-0722(07)00080-7 | S2, S3 | Iowa Electronic Markets record — a NON-Kalshi venue by construction (section 8) |
| KI-06 | Rhode P, Strumpf K (2004). Historical Presidential Betting Markets. *Journal of Economic Perspectives* 18(2):127-142 | doi:10.1257/0895330041371277 | S2, S5 | historical venue and market-organization recall anchor |
| KI-07 | Franck E, Verbeek E, Nüesch S (2013). Inter-market Arbitrage in Betting. *Economica* 80(318):300-325 (Crossref issued 2012-12-17) | doi:10.1111/ecca.12009 | S2, S5 | recall anchor for cross-venue arbitrage measured against frictions |
| KI-08 | Angelini G, De Angelis L (2019). Efficiency of online football betting markets. *International Journal of Forecasting* 35(2):712-721 | doi:10.1016/j.ijforecast.2018.07.008 | S2, S3 | recency anchor for cross-venue efficiency measurement |
| KI-09 | Thaler R, Ziemba W (1988). Anomalies: Parimutuel Betting Markets: Racetracks and Lotteries. *Journal of Economic Perspectives* 2(2):161-174 | doi:10.1257/jep.2.2.161 | S3 | the anomaly-statement anchor for the FLB strand |
| KI-10 | Snowberg E, Wolfers J (2010). Explaining the Favorite-Long Shot Bias: Is it Risk-Love or Misperceptions? *Journal of Political Economy* 118(4):723-746 | doi:10.1086/655844 | S3 | competing-explanations anchor |
| KI-11 | Ottaviani M, Sørensen P (2010). Noise, Information, and the Favorite-Longshot Bias in Parimutuel Predictions. *American Economic Journal: Microeconomics* 2(1):58-85 | doi:10.1257/mic.2.1.58 | S3 | mechanism-tied anchor, ties S3 to E6 |
| KI-12 | Hanson R (2003). Combinatorial Information Market Design. *Information Systems Frontiers* 5(1):107-119 | doi:10.1023/A:1022058209073 | S1, S4 | market-scoring-rule lineage anchor |
| KI-13 | Hanson R. Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation. *The Journal of Prediction Markets* 1(1):3-15 (Crossref issued 2012-12-13) | doi:10.5750/jpm.v1i1.417 | S4 | LMSR anchor in its own venue |
| KI-14 | Chen Y, Pennock D. A Utility Framework for Bounded-Loss Market Makers | arXiv:1206.5252 | S4 | bounded-loss market-maker anchor; preprint tier recorded |
| KI-15 | Abernethy J, Chen Y, Vaughan J (2013). Efficient Market Making via Convex Optimization, and a Connection to Online Learning. *ACM Trans. Econ. Comput.* 1(2):1-39 | doi:10.1145/2465769.2465777 | S4 | axiomatic market-maker-design anchor |
| KI-16 | Othman A, Pennock D, Reeves D, Sandholm T (2013). A Practical Liquidity-Sensitive Automated Market Maker. *ACM Trans. Econ. Comput.* 1(3):1-25 | doi:10.1145/2509413.2509414 | S4, S5 | AMM successor anchor |
| KI-17 | Kroer C, Dudík M, Lahaie S, Balakrishnan S (2016). Arbitrage-Free Combinatorial Market Making via Integer Programming. *Proc. 2016 ACM Conf. on Economics and Computation*, 161-178 | doi:10.1145/2940716.2940767 | S1, S4 | anchor joining the arbitrage-condition and market-maker strands |
| KI-18 | Glosten L, Milgrom P (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. *Journal of Financial Economics* 14(1):71-100 | doi:10.1016/0304-405X(85)90044-3 | S6 | named-lineage anchor; transfer clause applies |
| KI-19 | Kyle A (1985). Continuous Auctions and Insider Trading. *Econometrica* 53(6):1315 | doi:10.2307/1913210 | S6 | informed-trading lineage anchor; transfer clause applies |
| KI-20 | Ho T, Stoll H (1981). Optimal dealer pricing under transactions and return uncertainty. *Journal of Financial Economics* 9(1):47-73 | doi:10.1016/0304-405X(81)90020-9 | S4, S6 | inventory-risk antecedent anchor; transfer clause applies |
| KI-21 | Avellaneda M, Stoikov S (2008). High-frequency trading in a limit order book. *Quantitative Finance* 8(3):217-224 | doi:10.1080/14697680701381228 | S4 | named-lineage anchor; transfer clause applies |
| KI-22 | Guéant O, Lehalle C-A, Fernandez-Tapia J (2013). Dealing with the inventory risk: a solution to the market making problem. *Mathematics and Financial Economics* 7(4):477-507 (Crossref issued 2012-09-04) | doi:10.1007/s11579-012-0087-0 | S4 | Avellaneda-Stoikov successor anchor; transfer clause applies |
| KI-23 | Levitt S (2004). Why are Gambling Markets Organised so Differently from Financial Markets? *The Economic Journal* 114(495):223-246 | doi:10.1111/j.1468-0297.2004.00207.x | S5, S6 | market-organization and pricing anchor |

**How the known-item arm is used.** Each KI is fetched, screened against section
2 **like any other record** — a KI is not auto-included — and force-entered into
the record universe so that it cannot be missed. Separately, each KI is checked
for **independent retrieval** by at least one section 3.2 query or section 3.3
arm. A KI not independently retrieved is reported in the corpus record as a
**per-item recall failure** with the strand it belongs to. **No numeric recall
target is set**: a pass threshold on recall would be an unlabelled constant, and
PRISMA-S prescribes what is reported, never how much is enough. Per-item
failures are reported and interpreted, not scored.

"Anticipated role" above is a **search-design annotation stating which strand
the item was selected to test recall for**. It is not a claim about the record's
content, and it must not be transcribed into the corpus record as one; the
corpus states only what a record's own text says, after retrieval.

### 3.5 Venue-structural arm (S7) — documentation tier, verbatim

Executed and logged exactly like the topical queries, into the same log
directory, but the results enter the S7 stream (section 2.7) and never the S1-S6
corpus flow.

```text ka-doc-01
https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=Kalshi&per_page=100&order=newest&fields%5B%5D=title&fields%5B%5D=document_number&fields%5B%5D=publication_date&fields%5B%5D=agencies&fields%5B%5D=html_url&fields%5B%5D=type
```
```text ka-doc-02
https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=event%20contracts&conditions%5Bagencies%5D%5B%5D=commodity-futures-trading-commission&per_page=100&order=newest&fields%5B%5D=title&fields%5B%5D=document_number&fields%5B%5D=publication_date&fields%5B%5D=html_url&fields%5B%5D=type
```
```text ka-doc-03
https://www.cftc.gov/IndustryOversight/TradingOrganizations/DCMs/index.htm
```
```text ka-doc-04
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations
```
```text ka-doc-05
https://kalshi.com/regulatory/rulebook
```
```text ka-doc-06
https://www.ecfr.gov/current/title-17/chapter-I/part-40/section-40.11
```

Six documentation queries. `ka-doc-01`, `ka-doc-02`, `ka-doc-03`, `ka-doc-04`
and `ka-doc-06` returned HTTP 200 to an unauthenticated reachability probe at
protocol time; `ka-doc-05` returned HTTP 429 (gap AG-1, section 3.1). **No
result payload was retrieved or inspected at protocol time and no record entered
any universe** — the probe checked reachability only, with output discarded.

### 3.6 Strategy peer review (PRISMA-S 14 / PRESS)

**Not peer reviewed by a second human searcher; none exists in this project.**
This is a deviation from [PRESS 2015](https://doi.org/10.1016/j.jclinepi.2016.01.021)
and it is recorded rather than papered over. Mitigations, stated in advance:

1. The vocabulary is taken from the verified titles and venues of the known-item
   records (section 3.4), not from unverified recall.
2. The forward-citation arm (section 3.3) is vocabulary-independent by
   construction: it recalls whatever cites an anchor, whatever words it uses.
3. The known-item arm functions as the PRESS known-item recall check, with
   per-item reporting and no pass threshold.
4. The corpus record's limitations section must state that the strategy was not
   peer reviewed, and must not present recall as demonstrated.

## 4. Study records (PRISMA-P 11)

### 4.1 Data management (11a)

Raw responses per query id under
`docs/literature/search_logs/kalshi-arbitrage/`, filename prefix `ka-`
(`CONVENTION` — the project's search-log naming convention, matching the
executed practice for the explosive-regime search). Each log records at minimum:
`protocol_query_id`, the verbatim query string as executed, platform, ISO 8601
execution date, HTTP status, platform-reported total hits, records retrieved,
and retry suffix if any.

**Deduplication (PRISMA-S 16).** *Process*: identifier-level exact match on DOI
string first (case-normalized), then arXiv id, then RePEc handle, then
OpenAlex / Semantic Scholar internal id where no external identifier exists;
then a hand-verified same-work ledger for twins (working-paper/journal pairs,
publisher double registrations, proceedings/journal versions of one paper).
Same-work rule: titles match case- and punctuation-insensitively, **or** the twin
relation is documented by one of the records. *Software*: deduplication is
performed by the executing agent in Python under the project venv; no
reference-manager product is used, and the script or inline procedure is stored
with the logs. J6 governs which member of a twin pair is retained. The full
ledger is itemized in the corpus record.

Included records enter `docs/literature/references_kalshi-arbitrage.json`
(CSL-JSON) via `build_bibliography.py add --doi`; the store SHA-256 is written
into the corpus record's frontmatter via `sync-sha`.

### 4.2 Selection process (11b) — SINGLE-PASS SCREENING BY THE EXECUTING AGENT

**Stated plainly: screening is single-pass. There is no dual independent
screening, no second screener, no adjudicator, and no inter-rater agreement
statistic.** One agent session — the executing research-librarian — screens the
entire deduplicated record universe against section 2. This is a deliberate
design choice for a corpus-compilation stage, not an accident of resourcing, and
it is the single largest reason section 9.1 says this is not a systematic
review.

Concretely:

- **Screeners: 1.** Independent: **no** (independence is undefined with one
  screener). Automation tool: the LLM agent itself, declared with model and
  version in the corpus record's frontmatter — an LLM screener is an automation
  tool in PRISMA 2020 item 8's own terms
  ([Page et al. 2021](https://doi.org/10.1371/journal.pmed.1003583)).
- **Stage 1 — title/abstract.** Every deduplicated record receives one of
  `include`, `exclude` (with a primary X-code), or `promote` (eligibility not
  decidable at abstract depth). Each verdict cites the section 2 criterion or
  decision rule (I-, X-, B-, C-, J-) by identifier.
- **Stage 2 — full text, for promoted records only.** Depth is governed by
  decidability, not by budget: a record is promoted iff its abstract does not
  settle I1/I2, and no record is promoted for any other reason. Full text
  unobtainable after the retrieval chain (publisher, preprint twin, repository)
  → X8, logged with the locator and the chain that failed.
- **No agreement statistic is computed**, and none may be reported. With one
  screener there is nothing to agree with; reporting an agreement number here
  would be a fabrication.
- **What replaces dual screening, honestly stated as weaker:** (i) every verdict
  cites a criterion identifier, so a reader can re-decide any record against the
  frozen text; (ii) the full excluded list with reasons is published, not only
  the near-misses (section 4.3), so the screening is auditable end-to-end rather
  than spot-checkable; (iii) the downstream `literature-check` pass verifies the
  citations and attributed claims in the corpus record against primary sources.
  None of these is a substitute for an independent second screener, and the
  corpus record must say so in those words.

### 4.3 Recording exclusion reasons (PRISMA 2020 item 16b, applied more broadly)

Two tables, both required in the corpus record:

- **Table X-full — every excluded record.** Columns: `id`, `citation or best
  locator`, `identifier`, `stage_excluded` (identification / title-abstract /
  full-text), `primary_code` (X1-X9), `secondary_codes`, `criterion_cited`, and
  a one-line reason in the screener's own words. Every row has a non-empty
  reason. A record excluded at identification for duplication is an X9 row
  pointing at its retained twin.
- **Table X-nearmiss — records excluded after full-text assessment.** The PRISMA
  2020 item-16b table proper: records that looked eligible enough to reach full
  text and did not survive it, each with the criterion that decided it and a
  sentence saying what it was and why it failed. Dropping these silently is the
  most common way a search becomes unauditable, so the table is required even if
  empty — an empty table is reported as "no record reached full-text assessment
  and was then excluded", never omitted.

**Counts must reconcile** as arithmetic identities, reported in the corpus
record: `sum(per-source n_records) == n_identified`;
`n_identified − n_duplicates_removed == n_screened`;
`n_screened − n_excluded == n_included`; `len(bibliography store) == n_included`.
The S7 documentation stream is counted separately and is not part of these
identities (section 2.7 constraint 2).

## 5. Data items (PRISMA-P 12) — extraction fields, FROZEN

Extracted by the executing agent for every included record. Single extractor, no
duplicate extraction — see section 9.1, item 9.

| field | content |
|---|---|
| E1 | Identifiers (DOI / arXiv / RePEc handle), title, authors, venue, year, document type |
| E2 | Evidence tier T1-T5 per the CLAUDE.md hierarchy, and publication status (peer-reviewed / accepted preprint / preprint / working paper) |
| E3 | Strand(s) S1-S6 the record contributes to, and contribution type(s) C1-C4 |
| E4 | **Venue of the evidence** — the exact market(s) the record's data or model is about (Kalshi, Betfair, Iowa Electronic Markets, PredictIt, Polymarket, named sportsbook, racetrack parimutuel, laboratory market, simulated market, none/theoretical). Taken verbatim from the record; never inferred |
| E5 | Data period and sample description, where the record has data |
| E6 | **Wagering / trading mechanism** — parimutuel pool, continuous double auction, bookmaker fixed-odds book, automated market maker (named), call auction, other. Per J2 an extraction field, not a filter |
| E7 | Contract structure: payoff support, settlement rule, whether complementary legs (YES/NO) exist, whether bundles of mutually exclusive and exhaustive outcomes exist |
| E8 | **Condition stated (C1 records):** the no-arbitrage / coherence condition exactly as the record states it, with the market-structure assumptions the record attaches to it |
| E9 | **Quantity measured (C2 records):** what was measured, on what data, by what method, with the record's own reported figure and the uncertainty as the record reports it. No figure is re-derived, re-scaled, or rounded silently |
| E10 | **Model specification (C3 records):** objective function, state variables, payoff support ASSUMED BY THE MODEL, and every applicability condition the record states. Plus **transfer status** — does the record itself address bounded [0,1] payoffs with terminal settlement at an endpoint: `addressed` / `not addressed` / `explicitly excluded` |
| E11 | Microstructure result (C4 records): the mechanism analysed and the result as stated |
| E12 | **Frictions treated:** fees, commissions, bid-ask spread, slippage, collateral/margin, capital lockup and its duration, taxes — which are modelled or measured, which are assumed away, and which are not mentioned. "Not mentioned" is recorded explicitly, because an unstated friction is the usual reason a paper discrepancy is not an executable one |
| E13 | Executability statement: does the record state whether a discrepancy it reports was executable net of the frictions in E12, and on what evidence |
| E14 | **REVIEW.md blocking directive 8 field — attribution status.** For every factor, signal, or trading rule the record states or uses: is it carried by a citation to published research, by a derivation inside the record, or by neither? A record that uses an unattributed folklore rule is INCLUDED (that is itself a finding about the literature) with the gap recorded here; the corpus record may never restate such a rule as established, and the corpus record states no trading rule of its own at all |
| E15 | Kalshi relevance: `kalshi-specific` / `generalizable-with-stated-assumption` / `not-transferable-as-stated`, assigned per the section 8 rule, with the carrying assumption written out for the middle category |
| E16 | Code / data availability: named package, archive, replication file, or none |
| E17 | Retrieval and depth flags: retrieval date, depth reached (abstract / full text), language and translation status, paywall or access limitation encountered |

## 6. Appraisal posture (PRISMA-P 14) — no risk-of-bias instrument is applied

**No risk-of-bias assessment is performed, and none is claimed.** RoB 2 is for
randomized trials; QUADAS-2 for diagnostic-accuracy studies; PROBAST for
prediction-model studies. None maps onto "is this measurement of a
betting-market price discrepancy trustworthy", and this stage has neither the
budget nor the dual-assessment design that would make a project-local instrument
meaningful. Inventing an unvalidated scoring instrument and applying it
single-handed would produce a number with no interpretation, which is worse than
an acknowledged absence.

What the corpus record carries instead, per included record, is **descriptive
and non-scored**: the evidence tier (E2), the venue and data period (E4, E5),
the frictions treated and not treated (E12), the transfer status of any model
(E10), and the attribution status of any rule (E14). These are facts about the
record, not judgements about its quality. The corpus record must state that no
risk-of-bias assessment was performed (PRISMA 2020 items 11 and 18 — section
9.1).

## 7. Synthesis plan for the corpus record (PRISMA-P 15)

The output is `docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md`, a
compiled corpus record per the research-compile skill. Its structure is fixed
here:

1. **Search provenance.** Per-source table with source, platform, ISO 8601 date
   searched, verbatim query, platform-reported total hits, and records retrieved
   — one row per query id, including zero-yield queries and retries.
2. **Flow accounting.** The four arithmetic identities of section 4.3, plus
   Table X-full and Table X-nearmiss.
3. **Corpus table.** One row per included record with E1-E4, the E2 tier in the
   "role" column, and the strand(s) it serves.
4. **Synthesis by strand, S1 through S6.** Narrative, organized by strand, with
   an evidence table per strand: record × venue (E4) × mechanism (E6) × what the
   record states (E8/E9/E10/E11) × frictions treated (E12) × tier.
   - **Every claim line carries a resolvable citation.** A line with no citation
     is a defect, not a stylistic choice.
   - **Where the corpus disagrees, the disagreement is reported**, with both
     positions and their venues. Nothing is averaged away.
   - **No quantitative pooling.** Records differ in venue, mechanism, period and
     measurement; there is no common estimand, and pooling would manufacture
     one. Hand off to the meta-analysis skill only if a future stage establishes
     a common estimand. Vote counting is not used and must not be presented as
     inference.
5. **Kalshi-specific versus generalized separation** — section 8, rendered as a
   hard structural boundary: a column in the corpus table and a section boundary
   within each strand.
6. **S7 venue-structural table** — documentation-tier facts, each with document
   identity, version or effective date, retrieval date, and the "as filed"
   labelling of section 2.7 constraint 4. Counted separately.
7. **Gaps (O8).** Any strand with no eligible record is reported as an empty
   strand together with the queries that failed to populate it — an absence of
   evidence stated as such, never as a negative finding about the world.
8. **`TO COMPUTE` handoffs.** Anything the corpus identifies as needed but
   unpublished is recorded with what would have to be computed and on what data,
   and is not computed here (ADR-0003).
9. **Limitations**, stating in these terms: single-pass screening by one agent;
   no independent second screener; no risk-of-bias assessment; strategy not peer
   reviewed; any depth-truncation, recall, and access gaps; and the enumerated
   PRISMA 2020 items from section 9.1.

## 8. Kalshi-specific versus generalized — the separation rule

The hazard this rule exists to prevent: a measurement made on Betfair, the Iowa
Electronic Markets, PredictIt, Polymarket, or sportsbook data being restated as
a fact about Kalshi because both are "prediction markets".

**The rule, in three parts, binding on the corpus record:**

1. **Classification is mechanical, from E4.** A claim is **Kalshi-specific** iff
   the supporting record's own data or institutional object is KalshiEX LLC
   (E4 = Kalshi). Any other value of E4 makes the claim **venue-other**. A
   theoretical record with E4 = none/theoretical is **venue-none** and is
   classified by its assumptions, not by a venue.
2. **A venue-other or venue-none claim may be carried into a statement about
   binary event markets in general ONLY as
   `generalizable-with-stated-assumption` (E15), and the assumption must be
   written out on the same line as the claim.** The assumption must name what
   has to hold for the transfer: at minimum the **wagering mechanism** (E6 — a
   parimutuel result does not transfer to an order book without an argument),
   the **fee and commission structure** (E12), the **settlement and adjudication
   process** (E7), the **participant population**, and any **regulatory
   constraint** the source's venue operated under. A generalization whose
   assumption cannot be written out is recorded as `not-transferable-as-stated`
   and reported as such, not softened.
3. **Structural separation in the artifact, not just in prose.** Within each
   strand, the corpus record separates Kalshi-specific from generalized material
   by a section boundary, and the corpus table carries E15 as a column. A reader
   must be able to answer "what does the literature establish *on Kalshi data*"
   by reading one block, without reconstructing it from footnotes.

**Two corollaries, stated so they are not re-litigated at execution.**

- **An empty Kalshi-specific block is an acceptable and reportable outcome.** If
  the search returns no eligible record whose evidence is Kalshi data, the
  corpus record says exactly that, and every strand's substance sits in the
  generalized block with its assumptions. Filling the block by relabelling a
  Polymarket or Betfair result is the specific failure this rule forbids.
- **Venue-structural facts (S7) are not evidence about behaviour.** That
  Kalshi's filed rulebook specifies a fee formula is a T2 documentation fact
  about the venue; it is not a finding about arbitrage, spreads, or
  executability, and it may not license a behavioural claim. It may, however, be
  used to state whether a generalized claim's carrying assumption is satisfied
  at the venue — and when it is so used, the corpus says which document, which
  version, and which retrieval date carried it.

## 9. What this is not, and the conformance maps

### 9.1 What this is not

**This protocol registers a SEARCH producing a compiled corpus under the
research-compile skill. It does not register a systematic review, and the
artifact it produces is not one.** The distinction is not cosmetic: PRISMA 2020
is a reporting guideline for systematic reviews
([Page et al. 2021](https://doi.org/10.1136/bmj.n71)), and a corpus record that
borrowed its vocabulary while missing its design requirements would be a
reporting failure dressed as compliance.

Three design facts drive everything below: **screening is single-pass by one
agent** (section 4.2); **extraction is single-extractor** (section 5); and **no
risk-of-bias assessment is performed** (section 6).

**PRISMA 2020 items this design does NOT meet, enumerated by item number, each
with its reason:**

| item | topic | why unmet |
|---|---|---|
| 1 | Title: identify the report as a systematic review | The artifact is a compiled corpus record and is titled as one. Calling it a systematic review would be false; leaving item 1 unmet is the honest option |
| 2 | Abstract: PRISMA-for-Abstracts checklist | The corpus record carries structured frontmatter and a summary, but does not complete the abstract checklist — several of its required entries (risk of bias, certainty, synthesis method) have no content to report, per items 11, 13 and 15 below |
| 8 | Selection process: how many reviewers, whether independent, how conflicts were resolved | One screener, no independence, no conflict-resolution procedure because no conflict can arise. The automation-tool declaration (model and version) IS made, which is the part of item 8 that is met; the dual-independence part is not |
| 9 | Data collection process: same reporting for extraction | One extractor, no duplicate extraction of any field, no verification against a second extractor |
| 11 | Study risk of bias: tool used, and how it was applied | No risk-of-bias instrument is applied (section 6). No validated tool fits these study types, and an unvalidated single-assessor instrument would produce an uninterpretable judgement |
| 13b | Synthesis: preparation of the data for presentation or synthesis | No conversion, transformation, or harmonization of reported quantities is performed; figures are transcribed as the records state them |
| 13c | Synthesis: methods to tabulate or visually display results of individual studies | Evidence tables are descriptive by strand; no comparative display method is specified, because records are not comparable on a common estimand |
| 13d | Synthesis: methods used to synthesize results, model choice, heterogeneity, software | No statistical synthesis is performed at all (section 7, item 4) |
| 13e | Synthesis: methods used to explore causes of heterogeneity | Follows 13d — no synthesis, therefore no heterogeneity analysis |
| 13f | Synthesis: sensitivity analyses | Follows 13d |
| 14 | Reporting-bias assessment: methods for assessing risk of bias due to missing results | Not assessed. Funnel-plot methods need a common effect estimate and standard error, which this corpus does not have, and no substitute assessment (registry-versus-publication comparison, critical-evaluation uptake check) is performed at this stage |
| 15 | Certainty assessment: methods for assessing certainty in the body of evidence | GRADE is not applied. Evidence tiers (E2) are recorded per record; that is NOT a certainty-of-evidence assessment and must not be reported as one |
| 18 | Results: risk of bias in the included studies | Follows item 11 — nothing to report |
| 19 | Results: for each study, effect estimate and precision | Records are heterogeneous in outcome; extraction (E9) transcribes what each record reports, which is frequently not an effect estimate with precision. The item as written is not met |
| 20b | Results of statistical syntheses | Follows 13d |
| 20c | Results: causes of heterogeneity among study results | Follows 13d |
| 20d | Results: sensitivity analyses | Follows 13d |
| 21 | Results: reporting biases | Follows item 14 |
| 22 | Results: certainty of evidence | Follows item 15 |

Nineteen items: **1, 2, 8, 9, 11, 13b, 13c, 13d, 13e, 13f, 14, 15, 18, 19, 20b,
20c, 20d, 21, 22.**

**Separately, item 12 (effect measures) is INAPPLICABLE with rationale**, not
unmet by omission: the corpus's objects are stated conditions, model
specifications, and heterogeneously-measured discrepancies, not effect measures
for a common outcome. No effect measure is chosen because none exists to choose.

**Items the corpus record IS expected to meet** — stated so the enumeration
above is not read as a blanket disclaimer: 3 rationale; 4 objectives; 5
eligibility criteria (frozen here, cited by identifier); 6 information sources
with platforms and dates; 7 search strategies verbatim including zero-yield
queries; 10a/10b data items; 13a the grouping rule for synthesis; 16a flow; 16b
exclusions with reasons — met and exceeded, since every exclusion is published,
not only the full-text ones; 17 study characteristics; 20a characteristics of
contributing studies; 23a-23d discussion including limitations of the review
processes; 24a registration status (not registered, with the reason, and the
provenance commit named as the registration event); 24b protocol availability
(this file); 24c amendments (section 10); 25 support; 26 competing interests; 27
availability of data, code and materials.

**And what may not be said.** The corpus record, the branch agenda, and any
downstream artifact must not describe this work as a systematic review, must not
report an inter-rater agreement statistic, must not report a
certainty-of-evidence grade, and must not present the absence of a
risk-of-bias table as an oversight rather than a declared design limit.

### 9.2 PRISMA-P 2015 item map (protocol completeness)

| item | where |
|---|---|
| 1a title identification | document title + frontmatter `type: protocol` |
| 1b update | not an update; first review on this question in the project |
| 2 registration | frontmatter `registration` (no PROSPERO — non-health; the provenance commit is the registration event) |
| 3a/3b contributors | frontmatter `ai_assistance`; the repository author approves by commit; contact via the repository |
| 4 amendments | section 10 |
| 5a/5b/5c support | no external funding, no sponsor, self-directed (frontmatter `competing_interests`) |
| 6 rationale | section 0 |
| 7 objectives | section 1 |
| 8 eligibility | section 2 |
| 9 information sources | section 3.1 |
| 10 search strategy | sections 3.2-3.5 (verbatim, per platform, caps declared) |
| 11a data management | section 4.1 |
| 11b selection process | section 4.2 — single-pass, declared |
| 11c collection process | section 5 — single extractor, declared |
| 12 data items | section 5 |
| 13 outcomes and prioritization | section 1.2 |
| 14 risk of bias | section 6 — **declared not performed**, with rationale |
| 15a-15d synthesis | section 7 — narrative only; the pooling condition is stated as absent |
| 16 meta-bias | **not assessed** — see section 9.1, items 14 and 21 |
| 17 confidence in cumulative evidence | **not assessed** — see section 9.1, item 15. Evidence tiers are recorded and are not a substitute |

### 9.3 research-compile gate mapping

The corpus record is checked by `check_lit_review.py` (G1-G20). The design
decisions here map onto the gate as follows, so that no gate item is discovered
as a surprise at execution: `review_type: scoping` (G3 — the 16 PRISMA-S anchor
markers are enforced for `systematic` only, and understating the type to dodge
the gate would be a defect; this design genuinely is not systematic, for the
nineteen enumerated reasons in section 9.1); G4 platforms and dates per source
row (sections 3.1, 4.1); G5 one fenced verbatim query block per source row
(sections 3.2, 3.5); G6 the affirmative no-limits statement (section 2.5); G7
the affirmative not-peer-reviewed statement (section 3.6); G8 dedup process and
software (section 4.1); G9 the count identities (section 4.3); G10 the exclusion
table (section 4.3); G11 `screeners_n: 1`, `independent: no`,
`automation_tools` declared (section 4.2); G12-G15 the CSL-JSON store and its
SHA (section 4.1); G16 every DOI resolved by fetch, never from memory, with an
unresolvable DOI recorded as a `verification-gap` of severity `major`; G17
repro-envelope keys; G18 identity hygiene (below); G19 registration and protocol
path (frontmatter); G20 materials paths exist.

**Identity hygiene (G18 class).** No OS username, no email address, and no
absolute home-directory path appears in this protocol, and none may appear in
the corpus record, the CSL-JSON store, or the logs. Repo-relative paths
throughout. Real-name *attribution* is this repository's declared policy
(CLAUDE.md section Identity hygiene) and is carried by git config, not by file
contents.

## 10. Amendments policy — APPEND-ONLY ADDENDUM BELOW THIS SECTION

This protocol freezes at its provenance commit; the SHA-256 of the frozen file
is recorded in that commit by the lead session. During execution, **ANY**
deviation — a query that will not execute as written, a platform change, an
eligibility edge the criteria do not decide, a cap change, a source that becomes
unreachable, a decision rule that turns out not to decide — is recorded as a
**numbered, dated, append-only amendment** in the addendum below, stating:

1. the amendment number `A{n}` and the ISO 8601 date;
2. what changed, quoted against the frozen text it modifies;
3. why;
4. **at what execution stage** — specifically, whether the affected records had
   already been seen or screened when the deviation was decided;
5. which PRISMA-P item(s) it touches.

**Silent deviation is a conduct violation.** An amendment logged after the
affected screening decisions were made must say so in those words; that is a
weaker amendment than a pre-execution one, and the corpus record reports the
distinction. **Frozen text above this line is never edited**: a superseded
provision is superseded BY an addendum entry, in place, and the original wording
stays legible. The corpus record's frontmatter cites this protocol's path and
commit hash and enumerates every amendment it ran under; a corpus record that
ran under an amendment it does not enumerate is defective.

## 11. Conventions register — every convention-sourced element in this protocol

Per CLAUDE.md: zero arbitrary thresholds or magic numbers. Every numeric or
stylistic choice in this file is either derived with a stated rationale, or
labelled `CONVENTION` with the convention named. The complete register:

| element | status | source / derivation |
|---|---|---|
| Retrieval caps `rows=20`, `per-page=25`, `max_results=50`, `limit=50`, `perPage=50` | `CONVENTION` | House convention carried from `protocol_explosive-regime-review_2026-08-24.md` section 3.2 (executed and logged there), adopted for comparability of screening budget across this project's protocols. Caps on retrieval depth only; total-hit counts preserved and truncation flagged (section 3.1) |
| Retry suffixes `-b` / `-c` on HTTP 429 or other transient failure, with retry-until-200 on `-c` | `CONVENTION` | The naming-sweep retry convention as executed under `protocol_explosive-regime-review_2026-08-24.md` amendment A2 (section 3.1) |
| Search-log filename prefix `ka-` and directory `docs/literature/search_logs/kalshi-arbitrage/` | `CONVENTION` | Project search-log naming convention, matching the executed practice for the explosive-regime search (section 4.1) |
| Artifact filename pattern `{type}_{description}_{YYYY-MM-DD}.md` | `CONVENTION` | CLAUDE.md section Output Placement and Naming |
| arXiv category restriction `cat:q-fin*` on `ka-arxiv-03` and `ka-arxiv-05` | `CONVENTION` | The arXiv-category-narrowing convention of `protocol_explosive-regime-review_2026-08-24.md` section 3.2; applied only where the bare phrase returns predominantly out-of-domain records, with the unrestricted vocabulary retained elsewhere in the strategy (section 3.1) |
| Deduplication same-work rule (case- and punctuation-insensitive title match, or a documented twin relation) | `CONVENTION` | Carried from the naming-sweep deduplication rule used in this project (section 4.1) |
| Evidence tiers T1-T5 | **cited, not convention** | CLAUDE.md Evidence Hierarchy |
| Date bound: none | **derived** | The foundational statements for S1, S3 and S4 predate any regulated event exchange (verified known items from 1981 onward); a lower bound would amputate them, and an upper bound is meaningless for a single-execution search (section 2.5) |
| Language bound: none | **derived** | Conditions, quantities and model specifications are extractable independently of prose language; the screening-depth flag handles the remainder (section 2.5) |
| Preprints and working papers admitted | **derived** | The working-paper stream carries results ahead of journal publication and the venue of interest is recent; tier-blind admission with tier-labelled use (section 2.5) |
| Known-item set size (23 rows) | **derived** | Output of the two-anchors-per-strand rule plus the requirement that every model lineage named in the review question carry a verified anchor. The rule is frozen; the count is its consequence (section 3.4) |
| Forward-citation anchor count (6) | **derived** | One anchor per literature strand S1-S6 (section 3.3) |
| Recall-check pass criterion | **deliberately absent** | No numeric recall target is set: a threshold would be an unlabelled constant, and PRISMA-S prescribes what is reported, not how much is enough. Per-item recall failures are reported and interpreted (section 3.4) |
| Citation-count floor or sampling in the citation arms | **deliberately absent** | Either would be an unlabelled constant selecting against recent work (section 3.3) |
| Stage-2 promotion depth | **derived** | Governed by decidability — a record is promoted iff its abstract does not settle I1/I2 — not by a budget number (section 4.2) |
| Number of screeners (1) | **declared design choice** | Not a threshold: a stated design limit whose consequences are enumerated in section 9.1 (section 4.2) |

## 12. Works cited by this protocol

Every DOI below was verified against the DOI Handle System on 2026-09-02
(`responseCode` 1; 29 of 29 DOIs appearing anywhere in this file). The arXiv
identifier was verified against the arXiv API. Record:
`docs/literature/search_logs/kalshi-arbitrage/protocol-doicheck.json`.

**Reporting standards and search methodology**

- Moher D, Shamseer L, Clarke M, et al. Preferred reporting items for systematic
  review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic
  Reviews*. 2015;4(1). https://doi.org/10.1186/2046-4053-4-1
- Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated
  guideline for reporting systematic reviews. *BMJ*. 2021;372:n71.
  https://doi.org/10.1136/bmj.n71
- Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: An updated
  guideline for reporting systematic reviews. *PLOS Medicine*.
  2021;18(3):e1003583. https://doi.org/10.1371/journal.pmed.1003583
- Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to
  the PRISMA Statement for Reporting Literature Searches in Systematic Reviews.
  *Systematic Reviews*. 2021;10(1). https://doi.org/10.1186/s13643-020-01542-z
- McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. PRESS Peer
  Review of Electronic Search Strategies: 2015 Guideline Statement. *Journal of
  Clinical Epidemiology*. 2016;75:40-46.
  https://doi.org/10.1016/j.jclinepi.2016.01.021
- Koffel JB, Rethlefsen ML. Reproducibility of Search Strategies Is Poor in
  Systematic Reviews Published in High-Impact Pediatrics, Cardiology and Surgery
  Journals: A Cross-Sectional Study. *PLOS ONE*. 2016;11(9):e0163309.
  https://doi.org/10.1371/journal.pone.0163309
- Wilkinson MD, Dumontier M, Aalbersberg IJ, et al. The FAIR Guiding Principles
  for scientific data management and stewardship. *Scientific Data*.
  2016;3:160018. https://doi.org/10.1038/sdata.2016.18
- Lefebvre C, Glanville J, Briscoe S, et al. Searching for and selecting studies.
  In: *Cochrane Handbook for Systematic Reviews of Interventions*, ch. 4.
  https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04

**Known-item records — cited here for search design only. No claim is made in
this protocol about the content of any of them (section 3.4).**

- Oliven K, Rietz TA. *Management Science*. 2004;50(3):336-351.
  https://doi.org/10.1287/mnsc.1040.0191
- Manski CF. *Economics Letters*. 2006;91(3):425-429.
  https://doi.org/10.1016/j.econlet.2006.01.004
- Wolfers J, Zitzewitz E. NBER Working Paper 12200. 2006.
  https://doi.org/10.3386/w12200
- Wolfers J, Zitzewitz E. *Journal of Economic Perspectives*.
  2004;18(2):107-126. https://doi.org/10.1257/0895330041371321
- Berg J, Forsythe R, Nelson F, Rietz T. *Handbook of Experimental Economics
  Results*. 2008:742-751. https://doi.org/10.1016/S1574-0722(07)00080-7
- Rhode PW, Strumpf KS. *Journal of Economic Perspectives*. 2004;18(2):127-142.
  https://doi.org/10.1257/0895330041371277
- Franck E, Verbeek E, Nüesch S. *Economica*. 2013;80(318):300-325.
  https://doi.org/10.1111/ecca.12009
- Angelini G, De Angelis L. *International Journal of Forecasting*.
  2019;35(2):712-721. https://doi.org/10.1016/j.ijforecast.2018.07.008
- Thaler RH, Ziemba WT. *Journal of Economic Perspectives*. 1988;2(2):161-174.
  https://doi.org/10.1257/jep.2.2.161
- Snowberg E, Wolfers J. *Journal of Political Economy*. 2010;118(4):723-746.
  https://doi.org/10.1086/655844
- Ottaviani M, Sørensen PN. *American Economic Journal: Microeconomics*.
  2010;2(1):58-85. https://doi.org/10.1257/mic.2.1.58
- Hanson R. *Information Systems Frontiers*. 2003;5(1):107-119.
  https://doi.org/10.1023/A:1022058209073
- Hanson R. *The Journal of Prediction Markets*. 1(1):3-15.
  https://doi.org/10.5750/jpm.v1i1.417
- Chen Y, Pennock DM. A Utility Framework for Bounded-Loss Market Makers.
  arXiv:1206.5252. https://arxiv.org/abs/1206.5252
- Abernethy J, Chen Y, Vaughan JW. *ACM Transactions on Economics and
  Computation*. 2013;1(2):1-39. https://doi.org/10.1145/2465769.2465777
- Othman A, Pennock DM, Reeves DM, Sandholm T. *ACM Transactions on Economics
  and Computation*. 2013;1(3):1-25. https://doi.org/10.1145/2509413.2509414
- Kroer C, Dudík M, Lahaie S, Balakrishnan S. *Proceedings of the 2016 ACM
  Conference on Economics and Computation*. 2016:161-178.
  https://doi.org/10.1145/2940716.2940767
- Glosten LR, Milgrom PR. *Journal of Financial Economics*. 1985;14(1):71-100.
  https://doi.org/10.1016/0304-405X(85)90044-3
- Kyle AS. *Econometrica*. 1985;53(6):1315. https://doi.org/10.2307/1913210
- Ho T, Stoll HR. *Journal of Financial Economics*. 1981;9(1):47-73.
  https://doi.org/10.1016/0304-405X(81)90020-9
- Avellaneda M, Stoikov S. *Quantitative Finance*. 2008;8(3):217-224.
  https://doi.org/10.1080/14697680701381228
- Guéant O, Lehalle C-A, Fernandez-Tapia J. *Mathematics and Financial
  Economics*. 2013;7(4):477-507. https://doi.org/10.1007/s11579-012-0087-0
- Levitt SD. *The Economic Journal*. 2004;114(495):223-246.
  https://doi.org/10.1111/j.1468-0297.2004.00207.x

---

## Addendum (append-only; empty at freeze)

<!-- amendment entries: ### A{n} — {ISO date} — {execution stage} — {PRISMA-P item(s)} -->
