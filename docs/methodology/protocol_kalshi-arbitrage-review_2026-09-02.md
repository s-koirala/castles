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

### A0 — 2026-09-02 — addendum opened at round-1 audit remediation

This addendum was empty at freeze and remained empty through execution and first
publication of the corpus record. Amendments A1-A5 were logged only in
`docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md`, a file
the registration hash does not cover. Audit finding REV-1-13 (round 1,
2026-09-02) held that this did not meet section 10, which requires each
amendment to be recorded **in this addendum**. Amendment A12 below records the
correction. A1-A12 are transcribed here, byte-identical in content to the
working log.

**Frozen-prefix invariant.** Nothing above the addendum marker is altered. The
first 82677 bytes of this file — the file exactly as registered in commit
`27d74738aa35ec1cdf1ec6915b50532e3620ea6f` — still hash to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`. Verify with:

```
head -c 82677 docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md | sha256sum
```

The whole-file digest necessarily differs from the registered one. It is recorded
in the corpus record's section 13.1 and carried by the follow-on provenance
commit, which names the frozen hash it supersedes; it is not written here,
because a file cannot carry its own digest.

---

### A1 — 2026-09-02 — pre-screening (no record from the affected query had entered any universe) — PRISMA-P items 9, 10

**What changed.** The frozen retry convention (section 3.1) reads: "HTTP 429 or
other transient failure is logged as executed-with-zero-records and re-run
verbatim under a `-b` suffix; if that also fails, a retry-until-200 re-run under
a `-c` suffix, with the retry count recorded". Query `ka-doc-06`
(`https://www.ecfr.gov/current/title-17/chapter-I/part-40/section-40.11`)
returned **HTTP 200 whose body is an access interstitial** titled
"Federal Register :: Request Access" and contains none of the regulation text.
This amendment classifies a content-free HTTP 200 access interstitial as an
"other transient failure" for the purposes of that convention, and the `-b` and
`-c` retries were executed on that basis.

**Why.** The frozen text names HTTP 429 explicitly and "other transient failure"
generically. A 200 status carrying an access-denial body is not literally named.
Treating it as a success would have recorded a retrieval that did not occur;
treating it as a failure without saying so would have been a silent
reinterpretation of the frozen convention. The retries were run and logged
(`ka-doc-06-b.json`, `ka-doc-06-c.json`); both returned the same interstitial.
The retry logs carry a `content_gate` field stating the basis of the
classification.

**Execution stage.** Decided at execution of the S7 documentation arm, before
any S7 fact was extracted and before any S1-S6 record was screened. `ka-doc-06`
yielded zero content on all three attempts, so no record was affected by the
reclassification. The outcome is recorded as access gap **AG-2** in the corpus
record; no substitute source and no recalled regulation text was used.

**PRISMA-P items touched.** 9 (information sources), 10 (search strategy).

---

### A2 — 2026-09-02 — pre-screening (decided before any RePEc record entered the universe) — PRISMA-P items 9, 10

**What changed.** Section 3.1 names the RePEc source platform as the "IDEAS
htsearch interface (ideas.repec.org/cgi-bin/htsearch)" and section 3.2 gives the
two verbatim queries `ka-repec-01` and `ka-repec-02` as GET URLs against that
endpoint. **Both were executed verbatim and both returned HTTP 200 with a
results page containing zero result records** (logs `ka-repec-01.json`,
`ka-repec-02.json`; those logs are the primary record and stand unaltered). The
returned page's own search form declares `method="POST" action="/cgi-bin/htsearch2"`.
This amendment adds a **supplementary RePEc arm**, query ids
`ka-repec-01-supp` and `ka-repec-02-supp`, issuing the identical `q` values by
HTTP POST to `https://ideas.repec.org/cgi-bin/htsearch2`. The frozen queries are
not replaced, edited, or re-run under a different form; the supplementary arm is
additive and separately logged.

**Why.** The named endpoint no longer serves results to a GET request, so the
frozen RePEc arm returns a structurally empty page rather than a substantive
zero-yield. Reporting that as "RePEc returned nothing" would misdescribe the
literature; section 3.1 records that RePEc was added specifically as a recall
decision for working-paper series that Crossref covers unevenly, and abandoning
the arm would forfeit that recall without saying so.

**Retrieval depth.** The supplementary arm retrieves the platform's own default
result page. No cap is chosen by this amendment: the frozen cap register
(section 11) declares caps for Crossref, OpenAlex, arXiv, Semantic Scholar and
NBER only, and inventing a RePEc cap here would be an unlabelled constant. The
platform-reported total is preserved in the log and depth truncation is flagged
in the corpus record.

**Execution stage.** Decided at execution of the topical arm, after the two
frozen RePEc queries had been executed and logged with zero records, and
**before any record from either RePEc arm was screened**. No screening decision
predates this amendment.

**PRISMA-P items touched.** 9 (information sources), 10 (search strategy).

---

### A3 — 2026-09-02 — mid-screening (declared before any record in the affected stratum received a verdict; 3,300 of the 8,154 affected records had already been read individually) — PRISMA-P items 11b, 12; PRISMA 2020 item 8

> **SUPERSEDED IN PART BY A10 AND A13 (2026-09-02).** Six assertions of
> individual reading in this amendment are struck — one by A10, five by A13 —
> and the text below is retained unedited so the strike is checkable against it.
> **Read A10 and A13 before relying on anything in A3.**

**What changed.** Section 3.3 states that the A6 citing set "is screened at
**title level** against section 2 like every other arm — **no sampling and no
citation-count floor**", and section 4.2 states that "**Every** deduplicated
record receives one of `include`, `exclude` (with a primary X-code), or
`promote`". The deduplicated record universe is **8,813 works**, of which
**8,154** entered only through the forward-citation arms (6,851 through the A6
Glosten-Milgrom anchor alone). This amendment adds a **second automation tool**
to the screening step: a deterministic, published vocabulary pre-sorter that
partitions the forward-citation-only stratum into

- a **REVIEW stratum** — every record whose title *or* retrieved abstract
  contains at least one token from the published in-scope vocabulary list; each
  such record is read and verdicted individually by the LLM screener; and
- a **DEFAULT-X1 stratum** — records containing no listed token anywhere in
  title or abstract; each receives primary code **X1** by rule, with the
  reason "title and abstract contain no in-scope-instrument, market-making-model
  or event-market vocabulary token; fails 2.1 (B-a/B-b/B-c/B-d) and is not a C3
  transfer-clause record".

Neither the eligibility criteria nor the X-code definitions are changed. The
pre-sorter changes **who reads what**, not **what counts as eligible**.

**Why.** Individual reading of 8,154 titles was begun and carried through 3,300
records; completing the remainder by unaided sequential reading was not
achievable within this execution session. The alternatives were (a) to sample or
impose a citation-count floor — both forbidden by the frozen text and both
selecting against recent work; (b) to stop and report the arm as unscreened,
discarding the recall the arm exists to provide; or (c) to declare a
reproducible screening-support tool. (c) is the only one that preserves the
arm and remains auditable: the token list is published in
`ka-screening-vocabulary.json` and the partition is re-runnable by anyone
against the stored logs.

**What it can and cannot miss.** The pre-sorter can only fail on a record that
is in scope **and** whose title and retrieved abstract contain none of the
published tokens. It cannot fail on a record for a reason related to venue,
year, tier, citation count, or language. The residual risk is stated as a
recall verification gap in the corpus record's limitations section, and the
DEFAULT-X1 stratum count is reported separately from the individually-read
exclusions so the two are never conflated.

**Execution stage.** Decided during stage-1 screening. The 3,300
forward-citation-only records already read individually retain their individual
verdicts; the pre-sorter applies to the remainder and, for consistency of the
published partition, is also recorded for the already-read records so that the
partition is reproducible over the whole stratum. The 659 topical / known-item /
supplementary records are **not** affected: every one of them was read
individually. No record's verdict was reversed by this amendment.

**PRISMA-P items touched.** 11b (selection process), 12 (data items).
**PRISMA 2020 item touched.** 8 — the corpus record declares TWO automation
tools, the LLM screener and this pre-sorter, per the item's own terms.

---

### A4 — 2026-09-02 — post-stage-1 (declared after stage-1 verdicts, before any extraction) — PRISMA-P items 11b, 12, 15; PRISMA 2020 item 16b

**What changed.** Two things, both additive.

**(a) A tenth disposition code, X10, is added.** Section 2.4 fixes nine exclusion
codes X1-X9, all of them criterion failures. Stage-1 screening left a set of
records that **pass** eligibility (I1-I5) but for which the single extractor
could not perform the section-5 extraction (E1-E17) within this execution
session. Coding these under X8 ("not retrievable to abstract depth") would be
false — they are retrievable; nothing was tried and failed. Coding them as
included would be false too — the corpus would carry rows with no extraction
behind them. **X10 — "eligible under section 2; section-5 extraction not
performed within this execution session; a capacity gap, NOT a criterion
failure"** is therefore added as a *disposition* code. No eligibility criterion
is altered, added, removed, or reinterpreted. X10 rows sit in `n_excluded` so
that the section 4.3 arithmetic identities continue to hold, and every X10 row's
reason states in those words that it is not a criterion failure.

**Extraction-selection rule, stated so it is not arbitrary.** Which eligible
records were extracted is decided by the protocol's own objective prioritization
(section 1.2: "Primary: **O1, O4, O5**"). A record eligible at stage 1 is
extracted iff it serves a primary objective or the Kalshi stream — i.e. iff it
(i) has E4 = Kalshi; or (ii) is a section 3.4 known-item or a section 3.3
forward-citation anchor; or (iii) makes a C1 contribution (a stated
no-arbitrage / coherence condition, O1); or (iv) makes a C3 contribution
specifying a market-making, market-scoring-rule, inventory-risk or
automated-market-maker model (O4); or (v) makes a C2 contribution on
**cross-venue** price discrepancy or on **executability net of frictions** (O2
boundary case / O5). Records serving **only** the secondary objectives O2
(single-venue) and O3 (favorite-longshot bias and other systematic mispricings
measured on one venue) are dispositioned X10 unless they are an anchor or a
review of the strand. The rule is stated here in advance of its application; the
count is its consequence, not a target.

**(b) Table X-full is published as a machine-readable artifact rather than
inline.** Section 4.3 requires "Table X-full — every excluded record" in the
corpus record. The excluded set runs to thousands of rows; rendering it inline
would make the corpus record unreadable without adding any information. Table
X-full is therefore published in full at
`docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl`, one
JSON object per record with exactly the columns section 4.3 specifies, and the
corpus record carries (i) the per-code summary with counts and (ii) Table
X-nearmiss inline and complete. The search-log directory is named in the corpus
record's `materials_availability`, so the full table travels with the artifact.

**Why.** Both changes exist to keep the record honest at a scale the frozen
design did not anticipate: an uncapped forward-citation arm off Glosten-Milgrom
returned 6,463 citing works, and the deduplicated universe is 8,813. The
alternative to X10 was to overstate the corpus by listing unextracted records as
included; the alternative to (b) was an unreadable document.

**Execution stage.** Declared after stage-1 verdicts were formed and **before**
any extraction was written. No stage-1 eligibility verdict was changed by this
amendment.

**PRISMA-P items touched.** 11b, 12, 15. **PRISMA 2020 item touched.** 16b.

---

### A5 — 2026-09-02 — post-stage-1 (declared with A4, before extraction) — PRISMA-P item 11b

**What changed.** A4 added X10 for records that **pass** eligibility but were not
extracted. Stage-1 screening also left a second capacity residue with a
different logical status: **C3 model records on non-in-scope instruments whose
eligibility turns on the section 2.2 transfer clause**. For those, eligibility
is decided by what the record's own text says about its payoff support and
applicability conditions — which is, by construction, not decidable from a title
or an abstract. Section 4.2 promotes such a record to stage 2. Full-text stage-2
assessment was not performed for them within this execution session. Their
eligibility is therefore **undecided**, not "eligible-but-unextracted" (X10) and
not "full text unobtainable" (X8 — nothing was attempted and failed).

**X11 — "promoted to stage 2 under the section 2.2 transfer clause; stage-2
full-text assessment not performed within this execution session; eligibility
UNDECIDED; a capacity gap, not a criterion failure."**

X11 rows sit in `n_excluded` so the section 4.3 identities hold, and every X11
row's reason says in those words that eligibility is undecided. The corpus
record reports the X11 count separately from every criterion-failure code and
states that the S4/S6 transfer-clause literature is, in consequence, represented
in the corpus by its **anchors and its event-market-facing members only**, not
by the whole inventory-risk lineage the frozen design would have admitted.

**Why not stretch an existing code.** X8 asserts a retrieval attempt that failed;
none was made. X6 asserts the record states no applicability condition; that
cannot be asserted without reading it. Both would be false statements about the
record. An honest undecided is the only accurate disposition.

**Execution stage.** Declared with A4, before extraction. No eligibility verdict
was changed.

**PRISMA-P item touched.** 11b.

---

### A6 — 2026-09-02 — retrospective, post-extraction (no record's verdict is affected) — PRISMA-P items 9, 10

**What changed.** Section 3.3 of the frozen protocol provides a **backward
citation-chasing arm**: "The reference lists of INCLUDED C1 and C3 records are
hand-checked for in-scope work not otherwise retrieved; each addition is logged
with the carrier record (`ka-bc-{n}`)." **That arm was not executed**, and this
amendment records the non-execution. The arm is **not** executed retroactively;
doing so without a new dated log would fabricate provenance.

**Why.** Section 3.3 bounds the arm to the reference lists of *included* C1 and C3
records, which requires full texts. **No full text was retrieved in this execution**
(amendment A9), so the arm had no input. The corpus record disclosed the
non-execution in its `prisma-s-5` narrative and as gap G-7, but a narrative
disclosure is not what section 10 requires: section 10 requires **ANY** deviation
— explicitly including "a source that becomes unreachable" and "a query that will
not execute as written" — to be recorded as a numbered, dated, append-only
amendment. Recording it only as prose left the deliverable spec's requirement
("deviations recorded as numbered append-only protocol amendments, never silently")
unmet. Raised as audit finding **SCOPE-1-1**.

**Recall consequence.** The corpus contains **no record reachable only through an
included record's reference list**. Backward chasing is the arm that most reliably
recovers older foundational work whose title vocabulary has drifted away from
current terms, which is exactly the failure mode the known-item check exposed at
KI-20 (Ho & Stoll, "dealer pricing") and KI-21 (Avellaneda & Stoikov, "limit order
book"): neither term appears in any of the 35 frozen topical queries. The
un-executed arm and the two demonstrated vocabulary gaps are the same gap seen
twice.

**Execution stage.** Decided retrospectively, at round-1 audit remediation, after
extraction and after first publication. No screening or eligibility verdict is
altered by this amendment.

**PRISMA-P items touched.** 9 (information sources), 10 (search strategy).

---

### A7 — 2026-09-02 — retrospective (the arm was never run; its required gap entry was omitted) — PRISMA-P items 9, 10

**What changed.** Section 3.1 of the frozen protocol carries an **"SSRN caveat,
declared in advance"**: "SSRN has no public search API; the two Crossref
container-restricted queries are metadata-level only. If the executing session has
browser access it MAY additionally run the section 3.2 vocabulary through SSRN's
site search as a supplementary arm, logging it verbatim; **if not, the absence is
recorded as a minor recall verification gap in the corpus record, not passed over
in silence**." The arm was not run, **and the required gap entry was not written**.
This amendment records the absence and creates the gap entry as access gap
**AG-9** in the corpus record's section 13.3, and gap **G-9** in section 10.

**Why.** The frozen text makes the arm optional but the *disclosure* mandatory.
The corpus record as first published contained no SSRN gap anywhere: not in the
AG-1..AG-8 table, not in the G-1..G-7 gap list, and not in the amendment ledger. A
grep for "SSRN site", "SSRN search", "no public search API" and "browser access"
returned nothing. Under section 10 that is a **silent deviation**, which the
protocol classes in terms as a conduct violation. Raised as audit finding
**LITERATURE-1-7**.

**Recall consequence, stated at its true size.** SSRN carries the densest and least
peer-reviewed part of this corpus. **31 of the 149 included records carry
`10.2139/ssrn.*` DOIs, and 13 of the 19 Kalshi-specific records do.** SSRN was
reached only through two Crossref container-restricted queries, `ka-crossref-13`
and `ka-crossref-14`, each capped at `rows=20` against platform-reported totals of
10,991 and 1,093 — a retrieval ratio of roughly 0.2% and 1.8%. The un-run arm
therefore sits on top of the stratum where this corpus's recall is weakest and its
Kalshi-specific content is densest.

**Execution stage.** Decided retrospectively at round-1 audit remediation. No
verdict is altered.

**PRISMA-P items touched.** 9 (information sources), 10 (search strategy).

---

### A8 — 2026-09-02 — retrospective, post-extraction (all 33 affected records were already screened, extracted and published as included) — PRISMA-P items 11a, 11b

**What changed.** Frozen criterion **I4** reads: "The record is retrievable at
least to abstract depth by the executing agent. Records retrievable only as a bare
title are excluded under X8." Frozen code **X8** reads: "not retrievable to
abstract depth. Fails I4." **This amendment relaxes I4 for the 33 included records
that were retrieved only to title, venue and year**, admitting them at metadata
depth rather than excluding them under X8. It also **strikes an unauthorised
rewording of X8** that had appeared in the corpus record's frontmatter — "or full
text unobtainable after the retrieval chain" — a clause that is nowhere in the
frozen protocol and that had the effect of making the empty X8 row look correct.

**Why.** Of the 149 included records, **116 reached abstract depth and 33 reached
metadata depth only**. Abstracts for those 33 were requested from Crossref,
OpenAlex, arXiv, Semantic Scholar and DOI content negotiation, and none returned
one (access gap AG-7). On the frozen text those 33 fail I4 and belong under X8. The
corpus record's section 6 nonetheless declared X8 unused, on the ground that "no
full text was attempted and failed" — a reason drawn from the reworded frontmatter
clause, not from the frozen criterion, which says nothing about full text. That is
criterion drift, and it was unlabelled. Raised as audit finding **QUANT-1-3**.

**Why relaxation rather than exclusion.** The two available dispositions were
(a) exclude the 33 under X8, which changes `n_included` to 116, changes
`n_excluded` to 8,697, and changes the bibliography SHA-256; or (b) relax I4 with
a stated rationale. **(b) is chosen**, on the ground that the 33 carry no claim in
the corpus: each is named with its topic and **none of their findings is stated
anywhere**, because at metadata depth there is nothing to state. They therefore
inflate no conclusion. The cost of (b) is that `n_included: 149` is not the number
the frozen criteria alone would produce, and the corpus record says so at every
site: section 6, section 13.2, AG-7 and the frontmatter's `extraction_depth` key.
**A reader who declines this relaxation should read the corpus as 116 included
records plus 33 X8 exclusions.**

**Execution stage.** Decided retrospectively at round-1 audit remediation. All 33
records were already screened, extracted and published as included when the
amendment was taken; this is the weakest possible stage for an amendment and the
corpus record reports it as such.

**PRISMA-P items touched.** 11a (eligibility criteria), 11b (selection process).

---

### A9 — 2026-09-02 — extraction stage (all 149 included records affected) — PRISMA-P items 12, 15

**What changed.** The frozen protocol's section 5 extraction fields **E8**
(condition as stated), **E9** (quantity measured with its uncertainty), **E10**
(model objective, state variables, payoff support, applicability conditions),
**E12** (frictions modelled / assumed away / not mentioned) and **E13**
(executability) presuppose a **stage-2 assessment of retrieved text**. This
amendment records that **no full text was read for any included record and no
stage-2 assessment was performed for any record**, so those five fields are
partially completed at best, and that E12's value "not mentioned" is **not
distinguishable** from "not stated in the abstract".

**Why.** The decision was disclosed in the corpus record's section 13.2 but was
never converted into a numbered amendment, although it substitutes a different
*kind* of extraction for the one the protocol specifies — a larger deviation than
several that did receive amendments. A4 amends only the extraction-*selection*
rule and the Table X-full publication format; A5 covers only the transfer-clause
records. The decision that **no** included record would be read at full text had no
amendment of its own. Raised as audit finding **SCOPE-1-2**.

**Consequence, carried in the machine-readable header.** The constraint now
travels in the corpus record's frontmatter as `extraction_depth:`, not only in
prose, so a downstream consumer reading the header alone cannot mistake this for a
full-text review. Two dependent consequences are recorded elsewhere: the backward
citation-chasing arm had no input (A6), and the 33 metadata-depth records required
a relaxation of I4 (A8).

**Execution stage.** Decided at extraction, before section 8 was drafted; recorded
as an amendment retrospectively at round-1 remediation. All 149 included records
are affected.

**PRISMA-P items touched.** 12 (data items), 15 (data synthesis).

---

### A10 — 2026-09-02 — retrospective (all 8,664 non-include dispositions had already been made and published) — PRISMA-P items 11b, 12; PRISMA 2020 item 8

**What changed.** **The full five-list keyword classifier is declared the PRISMA
2020 item-8 automation tool of record for all 8,664 non-include dispositions.**
The tool is the archived script
`docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py`: token lists
`EVENT`, `CONTRIB`, `MODEL`, `DEFI` and `ELICIT`, and rules **R0-R9**, all
published verbatim in the file. This declaration **supersedes** the narrower one
made under A3, which named only the R2 branch (the 5,249-record DEFAULT-X1
partition).

Three specific statements are **struck**:

1. A3's sentence *"The 659 topical / known-item / supplementary records are not
   affected: every one of them was read individually."*
2. The verdicts file's header claim that the rule set *"encodes that reading so the
   mapping from record to verdict is reproducible byte-for-byte from the stored
   logs."*
3. The corpus record's section 5 sentence *"All 8,813 were screened at title level
   (and at abstract level where an abstract had been retrieved)."*

Two disposition-code descriptions are **restated** to what the execution supports.
**X10** is not "ELIGIBLE under section 2"; it is a **keyword-identified candidate
stratum** — an event-claim token and a contribution token both present — for which
no eligibility determination under I1-I5 was ever made. **X11** is not "promoted to
stage 2"; it is a **keyword-identified model-record stratum** — a model token
present and no event-claim token — for which the section 4.2 promotion condition
("a record is promoted iff its abstract does not settle I1/I2, and no record is
promoted for any other reason") was **never evaluated**, so eligibility is
UNDECIDED.

**Why.** Reading the archived pipeline back at round-1 audit, every disposition
except the 149 includes and one hand-verified J6 same-work twin is a rule output.
The R3-R8 branches assign X10, X2, X5, X11, X3 and X1 from substring membership in
the five hard-coded lists, and they run over **all three** strata alike: the
DEFAULT-X1 stratum, the A3 "REVIEW" stratum described as individually read, and the
659 topical / known-item / supplementary records described the same way. Re-running
that logic with `PYTHONHASHSEED=0` over a universe rebuilt from the stored
`ka-*.json` logs, using only the published vocabulary and the store's 149 included
DOIs, **reproduces the published nine-code table exactly**: `include` 149, `X1`
6,707, `X2` 338, `X3` 35, `X5` 159, `X7` 236, `X9` 1, `X10` 545, `X11` 643. No
individual reading is recoverable from any artefact in this repository, and a claim
that the rules "encode" a reading no artefact records is **unfalsifiable**. Under
the evidence discipline this project runs on, an unfalsifiable claim is withdrawn,
not defended. Raised as audit finding **QUANT-1-1** (critical).

**What the declaration costs the corpus, stated plainly.** **3,414 dispositions
were presented as individual screening verdicts and were not** — the 2,905-record
REVIEW stratum plus the 659 topical / known-item / supplementary records, less
overlap with the includes. Combined with the 5,249 already declared under A3, the
total is **8,663 classifier verdicts against 150 read-based ones** (149 includes +
1 hand-verified twin), or **98.3% of the flow**. A disposition code in this
artifact is therefore a statement about which tokens a record's title and retrieved
abstract contain, and about nothing else. The criterion cited on each row states
which criterion the rule was **written to stand in for**, not which criterion a
reader applied.

**What does not change.** **No verdict value changes under A10.** The 149-record
corpus is unaltered, no record is re-screened, and no criterion is reinterpreted.
What changes is what the record says produced the verdicts.

**Execution stage.** Decided retrospectively at round-1 audit remediation, after
all dispositions were made, after extraction and after first publication. This is
the weakest stage at which an amendment can be taken, and the corpus record reports
it as such.

**PRISMA-P items touched.** 11b (selection process), 12 (data items).
**PRISMA 2020 item touched.** 8 — the item's automation-tool declaration was
materially incomplete as first published and this amendment completes it.

---

### A11 — 2026-09-02 — retrospective, post-publication (the only amendment that changes a published verdict) — PRISMA-P items 11b, 12

**What changed.** Two defects in the archived pipeline are fixed and the verdicts
file is re-emitted.

**(a) Word-boundary matching for four DeFi tokens (finding QUANT-1-2).** The X5
branch (rule R5, "traded object is a token pair or liquidity pool, not an event
claim; fails B-a") tested its `DEFI` vocabulary as **unanchored substrings**. Three
of the four short tokens fire inside unrelated English words: `dex` inside
*index*, *indexed*, *stockindex*, *sensex-index*; `amm` inside *programming*,
*programmable*, *hammer*, *notamment*, *constamment*, *indépendamment*; `defi`
inside *defined*, *definition*, *definitions*, *predefined*, *indefinite*.
Corpus-wide, **289 of the 305 works containing the string `dex` contain no
word-boundary `dex` at all**, and 83 of the 128 containing `amm` contain no
word-boundary `amm`. The consequence was that records with **no DeFi content**
were published with a **false criterion-failure reason under B-a** — for example
*"A symbolic closed-form solution to sequential market making with inventory"*,
*"Adverse-selection considerations in the market-making of corporate bonds"*,
*"Modeling the Impacts of Market Activity on Bid-Ask Spreads in the Option
Market"*, *"Market microstructure of FT-SE 100 index futures"*. These are C3
transfer-clause candidates in the corpus's largest strand.

The four tokens are now matched as `\bdexe?s?\b`, `\bamms?\b`, `\bdefi\b` and
`\bcrypto`. **The inflected forms are not invented**: they are exactly the forms
attested in this record universe. `\bdex\b` alone — the pattern the audit finding
prescribed — would have wrongly moved three genuine DeFi records out of X5
(*"Funding-Aware Optimal Market Making for Perpetual DEXs"*; *"Dynamic Function
Market Maker"*, whose abstract reads "decentralised automated market makers
(AMMs)"; *"Automated Market Makers in Cryptoeconomic Systems"*), so the plural
forms are admitted and this departure from the prescription is recorded here
rather than taken silently. Every other `DEFI` token is eight characters or longer
or contains a space and is left as a substring test, which is the frozen
behaviour. An audit toggle `KA_DEFI_MATCH=substring` reproduces the pre-amendment
behaviour byte for byte so a third party can re-derive the deltas without editing
the file.

**Effect, exact.** `X5` **159 → 94** (−65); `X11` **643 → 700** (+57); `X7`
**236 → 244** (+8). Every other code is unchanged (`X1` 6,707, `X2` 338, `X3` 35,
`X9` 1, `X10` 545, `include` 149) and the total is unchanged at 8,813, so the
frozen section 4.3 arithmetic identities still close. **65 records moved.** 57 fall
to X11 — eligibility undecided, the weakest disposition available. 8 fall to X7
because they carry no persistent identifier and the classifier's own
first-code-that-applies ordering routes the model branch to an I3 failure; that is
a criterion failure, but of I3 (a fact about retrieved metadata) and not of B-a (a
judgement about the traded object). Derived counts that change with it:
**capacity dispositions 1,188 → 1,245**, **criterion exclusions 7,476 → 7,419**.

**Why this is a bug fix and not a re-screen.** No record was read, no criterion was
reinterpreted, and no eligibility judgement was made or revised. A published rule
produced a wrong output for a mechanical reason; the rule is corrected and re-run.
The direction of every move is **away** from a criterion failure and **toward** an
undecided or identifier-based disposition, i.e. toward disclosure.

**(b) Determinism (finding QUANT-1-6).** `ka-dedup-script.py` selected a work's
title and venue by sorting a **set** on a single key (`len`), so ties resolved on
set iteration order, which depends on `PYTHONHASHSEED`. That changed the final
sort key and hence every `uid` — and `uid` is the row identifier of the published
Table X-full. Measured: a `PYTHONHASHSEED=0` rebuild from the stored logs
reproduces every aggregate exactly (15,924 raw / 8,813 works / 7,111 duplicates,
and all nine screening codes) but agrees with the published file on only **2,630 of
8,813** `uid`-to-record mappings, so **6,183 published row identifiers were not
reproducible**. The corpus record's claim that the scripts were "re-runnable
byte-for-byte" was false at the row level. Fixes: title and venue tie-breaks are
now total, `key=(len(v), v)`; `PYTHONHASHSEED=0` is **asserted at entry** by
`ka-dedup-script.py`, `ka-partition-script.py` and `ka-screening-script.py`, which
refuse to run unseeded; the X9 twin is keyed by DOI rather than by a
run-generated uid; and the two inputs that were unarchived scratch files at first
execution (the A3 partition and the included-record set) are now derived from
committed artefacts by a new archived script `ka-partition-script.py`, so the
pipeline runs end to end from the stored logs.

**Deliberately not changed.** The **abstract** tie-break is left exactly as
executed. It is a list comprehension over the raw-record order and Python's sort is
stable, so it was already seed-independent; converting it to a set would have
changed which abstract a tied work carries, hence its token matches, hence its
screening code. That would have been a re-screen disguised as a determinism fix,
and it is not done. This was verified: with the abstract tie-break converted, the
substring-mode classifier no longer reproduces the published table (`X1` 6,672
instead of 6,707); with it left alone, it reproduces the table exactly.

**Consequence for a reader holding the pre-amendment Table X-full.** The `uid`
values in the re-emitted `ka-screening-verdicts.jsonl` **do not correspond** to the
previously published ones. **Join on the `identifier` field, never on `id`.**

**Execution stage.** Decided retrospectively at round-1 audit remediation, after
first publication.

**PRISMA-P items touched.** 11b (selection process), 12 (data items).

---

### A12 — 2026-09-02 — retrospective (the amendment mechanism itself) — PRISMA-P item 5

**What changed.** **A1-A12 are appended to the frozen protocol's own append-only
addendum**, which was empty at first publication. Until this amendment every
amendment lived only in this external log file.

**Why.** Protocol section 10 requires each deviation to be recorded "as a
**numbered, dated, append-only amendment** in the addendum below", and names the
addendum in its own heading: "APPEND-ONLY ADDENDUM BELOW THIS SECTION". The
addendum carried only its placeholder comment. The consequence was concrete rather
than formal: **a reader who verified sha256
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4` obtained a
protocol whose text asserts an amendment mechanism and shows no amendments**, while
the amendments themselves sat in a file the registration hash does not cover. The
corpus record compounded this by stating that the amendments were "none an edit to
the frozen protocol file" as though that were compliance, when section 10 asks for
an append, not an edit. Raised as audit finding **REV-1-13**.

**How the frozen text is protected.** Nothing above the addendum marker is
touched. The frozen prefix — **the first 82,677 bytes, the file exactly as
registered in commit `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`** — still hashes to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`, and that is
verifiable by `head -c 82677 <file> | sha256sum`. The whole-file digest
necessarily changes. It is recorded in the corpus record's section 13.1 and
carried by the follow-on provenance commit, which names the frozen hash it
supersedes; it is not written inside the protocol file itself, because a file
cannot carry its own digest.

**Also under this amendment.** The corpus record's section 13.1 amendment table
gains the two required elements it was missing for every entry: **why** the
amendment was taken, and **which PRISMA-P item(s) it touches**.

**Execution stage.** Retrospective, at round-1 audit remediation.

**PRISMA-P item touched.** 5 (amendments).

---

### A13 — 2026-09-02 — retrospective, round-2 audit remediation (strike list only; no verdict, count or eligibility judgement is affected) — PRISMA-P items 11b, 12; PRISMA 2020 item 8

**What changed.** **A10's strike of the individual-reading claims is completed.**
A10 struck three named sentences. It did not reach five further assertions of
individual reading inside **A3**, which survived verbatim in this log and — because
A12 transcribed A1-A12 into the frozen protocol's addendum — were carried into the
protocol of record. The consequence was concrete: **the protocol and the corpus
record contradicted each other on the exact fact the critical finding was about.**
A reader who verified the protocol and read its addendum was told that 3,300
records had been read individually and that every REVIEW-stratum record "is read
and verdicted individually by the LLM screener", while A10, twelve pages later in
the same file, stated that 8,663 of 8,813 verdicts are classifier outputs and that
"no individual reading is recoverable from any artefact in this repository". Raised
as audit findings **REV-2-1**, **SCOPE-2-5** and **REPRODUCIBILITY-2-7**.

**Five further statements are struck**, each quoted so the strike is checkable
against the unaltered text it strikes:

1. A3's heading parenthetical *"3,300 of the 8,154 affected records had already
   been read individually"*.
2. A3's REVIEW-stratum definition clause *"each such record is read and verdicted
   individually by the LLM screener"*.
3. A3's **Why** sentence *"Individual reading of 8,154 titles was begun and carried
   through 3,300 records"*.
4. A3's **What it can and cannot miss** clause *"and the DEFAULT-X1 stratum count is
   reported separately from the individually-read exclusions so the two are never
   conflated"* — which presupposes a population of individually-read exclusions.
   There is exactly one: the hand-verified J6 same-work twin excluded X9.
5. A3's **Execution stage** sentence *"The 3,300 forward-citation-only records
   already read individually retain their individual verdicts"*.

(A10 had already struck A3's sixth such statement, *"The 659 topical / known-item /
supplementary records are not affected: every one of them was read individually."*
It is not re-struck here; it is listed so the six are seen together.)

**What is true in place of the struck statements.** Of the 8,813 works, **150 carry
a read-based verdict** — the 149 included records, read at abstract or metadata
depth and extracted, plus the one hand-verified X9 twin — and **8,663 were
verdicted by the keyword classifier**, rules R0-R9. By A3 stratum, net of the
read-based records that fall inside each: DEFAULT-X1 **5,249** classifier / 0
read-based; REVIEW **2,843** classifier / 62 read-based; topical, known-item and
supplementary **571** classifier / 88 read-based. **No forward-citation record
carries a read-based verdict except where it is also one of the 149 includes.** The
split is re-derivable from the committed pipeline.

**Strike, do not delete.** A3's text is **not** edited. A one-line supersession
banner is inserted at the head of A3 in this log and in the protocol addendum
reading `SUPERSEDED IN PART BY A10 AND A13`, so that a reader arriving at A3
directly cannot read it as current before reaching A10 and A13. That banner
insertion is the only modification made to previously-appended addendum text, it
is recorded here, and it is navigational: it adds a pointer and removes nothing.
The frozen prefix — the first 82,677 bytes — is untouched and still hashes to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`.

**What does not change.** No verdict value, no count, no eligibility judgement and
no record's disposition. What changes is what the protocol of record says produced
them, which is now the same thing the corpus record says.

**Execution stage.** Retrospective, at round-2 audit remediation, after all
dispositions, after extraction, after first publication and after round-1
remediation.

**PRISMA-P items touched.** 11b (selection process), 12 (data items).
**PRISMA 2020 item touched.** 8 — the automation-tool declaration, completed.

---

### A14 — 2026-09-02 — retrospective, round-2 audit remediation (evidence corrections to A11; both declared departures stand) — PRISMA-P items 11b, 12

**What changed.** **A11's two declared departures are upheld; three numbers offered
as evidence for them are corrected, and the counterfactual runs that settle them are
archived.** Audit round 2 adjudicated both departures on the merits and upheld both
(finding **QUANT-2-9**). What it found defective was the evidence A11 recorded, not
the decisions A11 took. Nothing in the pipeline is changed by this amendment and no
disposition moves.

**(a) The abstract tie-break refusal — right decision, wrong evidence** (findings
**QUANT-2-2**, **REPRODUCIBILITY-2-3**). A11's *Deliberately not changed* paragraph
justified leaving the abstract tie-break as executed with this sentence, which is
**struck**:

> *"This was verified: with the abstract tie-break converted, the substring-mode
> classifier no longer reproduces the published table (`X1` 6,672 instead of 6,707);
> with it left alone, it reproduces the table exactly."*

It does not reproduce. The conversion was re-run from the committed logs at
`PYTHONHASHSEED` 0, 1, 7 and 12345 in both matching modes — sixteen runs — and
**every one produces the published nine-code table exactly, `X1` = 6,707 included**.

**The replacement justification, which is measured rather than asserted.** The
executed **list** form is order-total by construction: it is a list comprehension
over raw-record order and Python's sort is stable, so `reverse=True` does not
reverse ties. Measured over the same sixteen runs, the list form retains an
**identical** abstract for all 8,813 works at every seed — **0** differences at
every seed pair. The **set** form does not: between seed pairs, **19 to 24 works**
change which of their tied abstracts they retain. Converting the tie-break would
therefore **introduce** a hash-seed dependency into a step that does not have one,
for no determinism benefit, and would silently change which abstract a tied work
carries — a re-screen disguised as a determinism fix. That is why it is not done,
and that is now the recorded ground.

**(b) The DeFi word-boundary departure — upheld, overstated by one record**
(finding **QUANT-2-9**). A11(a) stated that the bare patterns the audit finding
prescribed *"would have wrongly moved three genuine DeFi records out of X5"* and
named *"Funding-Aware Optimal Market Making for Perpetual DEXs"*, *"Dynamic
Function Market Maker"* and *"Automated Market Makers in Cryptoeconomic Systems"*.
**The third name is struck.** Re-running the classifier with
`BOUNDED = {\bdex\b, \bamm\b, \bdefi\b, \bcrypto\b}` moves exactly **two** records
out of X5 (both to X11), giving `X5` 92 and `X11` 702 against the shipped 94 and
700. *"Automated Market Makers in Cryptoeconomic Systems: A Taxonomy and
Archetypes"* **stays X5 under the bare patterns**, because its abstract carries four
standalone `amm` tokens and matches `\bamm\b` directly. The departure stands on two
records, not three.

**(c) Two corpus-wide figures were measured under the rejected patterns** (findings
**QUANT-2-9**, **REPRODUCIBILITY-2-4**). A11(a) published *"289 of the 305 works
containing the string `dex` contain no word-boundary `dex` at all"* and *"83 of the
128 containing `amm`"* without saying which pattern "word-boundary" denoted. Both
were computed under the **bare** patterns, which A11 itself rejected. Both figures
are correct **as measured under `\bdex\b` and `\bamm\b`** and are retained with that
label, because the bare pattern is the right instrument for sizing the substring
defect. The corresponding figures **under the shipped patterns** are added so the
two are never confused: `\bdexe?s?\b` leaves **284** of 305 unmatched, and
`\bamms?\b` leaves **64** of 128 unmatched.

**(d) A11's prescribed migration key is not a key** (findings **QUANT-2-6**,
**REPRODUCIBILITY-2-5**). A11 closed with *"Join on the `identifier` field, never on
`id`."* That instruction is **narrowed**, not withdrawn: `identifier` is the empty
string for **1,890 of the 8,813 rows** (21.4%) — every work carrying no DOI, no
arXiv id and no RePEc handle — so those rows collapse to a single join value and
cannot be reconciled at all. The join is defined for the **6,923** rows that carry a
persistent identifier, on which the values are unique. Two further corrections: the
verdicts header called the row identifier `uid` while the emitted field is named
`id`, and that wording is fixed; and the pre-remediation verdicts file was
**overwritten in place, was never committed, and is not recoverable from git**, so
A11(b)'s figures *"2,630 of 8,813 uid-to-record mappings agree"* and *"6,183
published row identifiers were not reproducible"* **cannot be checked by anyone**.
They are **downgraded from measurements to a stated, unverifiable assertion of the
round-1 remediation session** and are labelled as such wherever they appear. The
determinism defect they describe is independently established by the seed guard and
by the tie-break argument above; only the two magnitudes are unverifiable.

**Archived evidence.** All three counterfactuals are now a committed, re-runnable
script and a committed result file:
`docs/literature/search_logs/kalshi-arbitrage/ka-counterfactuals.py` and
`ka-counterfactuals.json`. A third party can re-derive every number in this
amendment without editing any archived script.

**What does not change.** The code is not changed. `ka-dedup-script.py` keeps the
list tie-break; `ka-screening-script.py` keeps `\bdexe?s?\b`, `\bamms?\b`,
`\bdefi\b` and `\bcrypto`. Both declared departures stand. `X5` 94, `X11` 700, `X7`
244 and every other count are unaltered.

**Execution stage.** Retrospective, at round-2 audit remediation.

**PRISMA-P items touched.** 11b (selection process), 12 (data items).

---

### A15 — 2026-09-02 — retrospective, round-2 audit remediation (a false factual claim about this protocol's own queries) — PRISMA-P item 10

**What changed.** **A6's assertion about the topical strategy's vocabulary is
struck.** A6's *Recall consequence* paragraph reads, of KI-20 (Ho & Stoll, *"dealer
pricing"*) and KI-21 (Avellaneda & Stoikov, *"limit order book"*):

> *"neither term appears in any of the 35 frozen topical queries. The un-executed
> arm and the two demonstrated vocabulary gaps are the same gap seen twice."*

**Both sentences are struck.** The `limit order` half is false, and the
"demonstrated vocabulary gap" conclusion does not follow for either item. Raised as
audit findings **QUANT-2-1** and **LITERATURE-2-1**, both critical.

**Why it was wrong.** The round-1 token test was run against the query strings **as
stored** — Crossref forms are `+`-separated and the arXiv, OpenAlex and Semantic
Scholar forms are percent-encoded — so it reported every multi-word token as
absent. On that basis `betting market` is absent too, which the same round-1
paragraph denied. The test is only meaningful on **URL-decoded** query text.

**What the decoded test returns**, re-run mechanically and archived at
`docs/literature/search_logs/kalshi-arbitrage/ka-query-token-inventory.json`:

- `parimutuel` (and `pari-mutuel`, `pari mutuel`) — **absent** from all 35 frozen
  topical queries and from all 45 fenced blocks in the corpus record.
- `dealer` — **absent**.
- `specialist` — **absent**.
- `limit order` — **PRESENT**, carried by `ka-crossref-07`
  (`query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book`),
  which executed with HTTP 200 and returned 20 records against a platform-reported
  **79,887**.
- `betting market` — **PRESENT**, carried by `ka-crossref-05`, `ka-crossref-15` and
  `ka-nber-02`, all executed.

**What replaces the struck conclusion.** Three title strings — `parimutuel`,
`dealer`, `specialist` — appear in the protocol's vocabulary paragraph (section 3.1)
and were **never operationalised in any query**. That is a real and narrow defect of
the strategy and it is recorded as one. It does **not** establish that vocabulary is
why those items were missed: every platform in this design matches a bag-of-words
relevance query over title, abstract and container rather than gating on an exact
phrase, and the rank-and-position evidence that would discriminate a vocabulary gap
from a retrieval cap was not extracted. **For all four genuine topical misses the
cause is undetermined between retrieval cap and vocabulary, and no demonstrated
vocabulary gap is claimed for any of them.** For KI-21 specifically the live
explanation is the cap, not vocabulary. A6's underlying point — that backward
citation chasing is the arm that most reliably recovers older foundational work
whose title vocabulary has drifted — is **retained**; what is struck is the false
premise it was rested on.

**What does not change.** The backward arm is still not executed and is still not
executed retroactively. Gap G-7 stands. No record's verdict is affected.

**Execution stage.** Retrospective, at round-2 audit remediation.

**PRISMA-P item touched.** 10 (search strategy).
