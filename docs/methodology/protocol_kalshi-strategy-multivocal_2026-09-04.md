---
type: protocol
slug: kalshi-strategy-multivocal
date: 2026-09-04
status: frozen-on-commit
review_type: multivocal-corpus-compilation
review_standard: >
  The search-reporting standard is PRISMA-S (Rethlefsen et al. 2021,
  doi:10.1186/s13643-020-01542-z), applied NOT by analogy: PRISMA-S self-scopes
  to all fields and disciplines and to the whole family of evidence syntheses,
  in its own terminology section, so its use for a non-clinical multivocal
  corpus is authorised by the source itself. The predecessor protocol's blanket
  "both ADAPTED" framing understates PRISMA-S and is deliberately not copied.
  The protocol's document structure follows PRISMA-P 2015 (Moher et al. 2015,
  doi:10.1186/2046-4053-4-1), adapted for a multivocal source taxonomy.
  PRISMA 2020 (Page et al. 2021, doi:10.1136/bmj.n71) is NOT claimed and its own
  scope statement does not reach a non-systematic review; every PRISMA 2020 item
  invoked in section 8 is therefore reasoning by analogy with no cited
  endorsement, and section 8 says so in those words. The output class is a
  scoping/mapping compilation in the sense of Arksey & O'Malley 2005
  (doi:10.1080/1364557032000119616). Instrument verification record:
  docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json.
output_class: >
  registered multivocal search producing a COMPILED CORPUS RECORD, not a
  systematic review and not a meta-analysis. The corpus record states what
  sources STATE; it states no tradeable rule and reports no result of its own.
registration: >
  Not registered in PROSPERO: PROSPERO accepts only reviews with health-related
  outcomes, and this review has none. The registration event for this protocol
  is its provenance commit: the file is committed BEFORE any query of any arm
  executes, and that commit records the file's SHA-256. The protocol cannot
  contain its own hash; the clone-durable carrier is the commit trailer, per the
  project reproducibility contract in CLAUDE.md. The SHA-256 is computed and
  committed by the LEAD session — not by the drafting agent and not by any
  executing agent. Any post-freeze change is an append-only amendment under
  section 10, never an edit to frozen text.
consumer: >
  docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md (the
  compiled corpus record), docs/literature/references_kalshi-strategy-multivocal.json
  (the CSL-JSON store), and downstream of both,
  docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md
  at revision 3. No empirical, data-acquisition, price-computing, or
  trading-rule artifact consumes this protocol; those are out of scope by
  ADR-0003 and by the session deliverable spec.
rule_adoption: >
  This branch is time-indexed financial analysis, so rules/quant-project.md and
  REVIEW.md are adopted BY EXPLICIT REFERENCE for the prediction-market branch
  and for that branch only (CLAUDE.md section Scope), as recorded in
  docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md. ADR-0004
  delimits the branch by path list plus "any successor artifact that names this
  branch in its front matter"; this file names it, so the adoption reaches it
  without a new decision. At this literature-only stage the binding directive is
  REVIEW.md blocking directive 8: "Every factor, signal, or trading rule must
  carry a citation to published research or an in-repo derivation. Unattributed
  folklore factors are blocking." ADR-0006 records the reading adopted for this
  branch — that an S-C repository artifact, an S-D rule document or a dated S-E
  write-up is a locatable source that satisfies the citation carrier, while
  model recall is not — and that reading is a widened one, recorded there as
  such. An unattributed strategy is a BLOCKING DEFECT, never a finding.
  REVIEW.md blocking directives 1-7 bind only a future EMPIRICAL stage, which
  under ADR-0003 does not occur in this repository.
branch: kalshi-arbitrage / prediction-market microstructure
scope_decision: docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md
predecessor_protocol: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md
instrument_verification: docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json
planned_outputs:
  - docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md
  - docs/literature/references_kalshi-strategy-multivocal.json
  - docs/literature/search_logs/kalshi-strategy-multivocal/  (raw query logs, ks-* prefix)
ai_assistance: >
  Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK) drafted
  this protocol. NO search arm was executed at protocol-drafting time and NO
  record was screened. Every methodological instrument named in sections 7, 8
  and 13 was resolved and verified before freeze by a separate literature-check
  session, whose evidence record — including the verification DEPTH of each
  record and the declared gap in each proposed use — is at
  docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json.
  Role per ICMJE 2026 disclosure: idea + prose + audit-support. The human author
  approves the frozen text by committing it.
competing_interests: none
---

# Protocol — registered multivocal search on stated strategies for binary event contracts, with KalshiEX LLC as the venue of interest

This document mirrors the structure of the branch's predecessor,
[docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md](protocol_kalshi-arbitrage-review_2026-09-02.md),
which remains frozen and byte-untouched. It is a **separate review** with a
**wider source taxonomy**, opened under
[ADR-0006](../decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md).

**Read section 8 before citing anything produced under this protocol.** What
follows registers a *search*. It does not register a systematic review, and the
corpus it produces must not be described as one.

**ADR-0003 boundary, restated at the head because it bounds every section
below.** This repository specifies; it does not execute. The compiled corpus
records what sources *state*. It fits nothing, acquires no market data, calls no
exchange API, computes no price, backtests nothing, and states no tradeable
rule. Anything the corpus identifies as unpublished-but-needed is a `TO COMPUTE`
handoff to an executing project, never computed here. The full restatement is
section 9.

---

## 1. Objective and question

### 1.1 The question

> What trading, arbitrage, market-making and adjacent **STRATEGIES** for binary
> event contracts does the retrievable multivocal record **STATE**, with
> **KalshiEX LLC** as the venue of interest; for each, **what source states it**,
> **at what depth**, **on what venue was it established**, and **what
> preconditions does that source itself say it depends on**?

**What makes it answerable and bounded.** The question asks what the record
*states*, not what is true of Kalshi and not what is profitable. Its answer is a
corpus of attributed strategy statements, fully answerable from retrievable
documents and artifacts. Four bounds:

1. the instrument rule in section 2.2, carried by reference from the predecessor
   protocol, which excludes continuous-payoff instruments;
2. the contribution rule in section 2.3, which excludes records that state no
   strategy, report no outcome, state no executability precondition, and provide
   no enabling data or tooling;
3. the search-arm list in section 3, closed at freeze — an arm may be *reported
   as empty*, but no arm may be added without a section 10 amendment;
4. the source-class list in section 2.1, closed at freeze on the same terms.

**Comprehensiveness is bounded and the bound is published.** No search is
exhaustive. The corpus record states per-arm coverage, the strata left
unassessed, and every gap it could not close. An unbounded claim of completeness
is a defect of the corpus record. In particular, no completeness bound is
claimed for the software-repository arm, and none is attributed to the
repository-mining literature named in section 7, which documents hazards and
supplies no such bound.

### 1.2 Objectives

| # | Objective |
|---|---|
| O1 | Assemble the retrievable record of STATED strategy classes for binary event contracts, each attributed to at least one locatable source at a stated extraction depth |
| O2 | Record, per strategy class, the venue on which the strategy was established, and whether the record is Kalshi-specific or transferred from another venue |
| O3 | Record, per strategy class, the executability preconditions the SOURCE ITSELF states — fees, settlement mechanics, rule constraints, collateral, latency, data availability |
| O4 | Record, per record, any outcome the source reports, verbatim and attributed, and never adopted as this project's own claim |
| O5 | Record the venue-and-regulator document set that decides whether a stated strategy is executable at all, with document identity, date, and retrieval digest |
| O6 | Record the gaps: strategy areas for which no source was located, reported as absent, never asserted |
| O7 | Record the capacity gaps: strata identified but left unassessed, dispositioned as undecided rather than as ineligible (section 4) |

**Prioritization.** Primary: O1, O3, O6 — a class without a source is a blocking
defect (ADR-0004, directive 8), and a class without its stated preconditions is
not usable by any downstream consumer. Secondary: O2, O4, O5, O7.

---

## 2. Source taxonomy and eligibility — FROZEN

Every criterion below is decidable, where possible, from a record's metadata and
its first-level content without a judgement call. Screening verdicts cite
criteria by identifier. **No criterion may be reinterpreted after the first query
of any arm executes**; a needed change is a section 10 amendment.

### 2.1 Source classes

Every record carries **exactly one** source class. The classes are ordered; a
record is assigned the **first** class whose test it satisfies, which makes the
partition total and unambiguous without further judgement.

| class | test (first match wins) |
|---|---|
| **S-A** peer-reviewed | The record appeared in a venue that applies external peer review before publication — journal, peer-reviewed conference proceedings, edited scholarly volume — and the record is the published version |
| **S-B** preprint / working paper | The record is a scholarly manuscript distributed without completed external peer review: preprint server, institutional or series working paper, thesis, technical report of a research institution |
| **S-C** public software repository or package | The primary artifact is executable or library code, or a package/notebook distribution, publicly readable without authentication. Its documentation (README, docs site, docstrings, issues) is part of the record |
| **S-D** exchange or regulator document | The publisher is a trading venue, a clearing organization, or a public authority, and the document states rules, specifications, fees, filings, orders, or technical interface documentation. Includes rulebooks, contract specifications, fee schedules, API documentation, self-certifications, agency orders and letters, and register or code publications |
| **S-E** practitioner grey literature | Anything else retrievable and dated: practitioner write-ups, blogs, newsletters, forum and community threads, conference or podcast transcripts, trade press, vendor and data-provider material that is not the venue's own rule document |

**Disambiguation rules, fixed here so the partition does not depend on the
screener's mood:**

- A repository accompanying a paper is **two records** where both are retrievable
  and each makes its own contribution — the paper under S-A or S-B, the
  repository under S-C — linked by a `companion_of` field. It is one record
  where only one of the two is retrievable.
- A venue's own *blog post* is **S-E**, not S-D. S-D is for documents that state
  rules, specifications, filings, or interfaces. A marketing post states none.
- A regulator's *press release about* an order is S-D; a trade-press *article
  about* the same order is S-E.
- A preprint later published is one record at its **published** version (S-A) if
  the published version is retrievable; otherwise S-B, with the relation noted.

**S-C, S-D and S-E records are counted in this protocol's corpus flow.** The
predecessor protocol's I6 and its §2.7 constraint 2 keep documentation-tier
records out of its flow entirely; that fencing is deliberately **not** carried
here, because a corpus whose question is what the multivocal record states cannot
report a flow that omits three of its five source classes. The consequence is
that this protocol's counts are not comparable line-for-line with the
predecessor's, and the corpus record says so.

### 2.2 Instrument scope — carried by reference, quoted verbatim

The in-scope instrument definition is **not restated in different words**. It is
adopted unchanged from
[protocol_kalshi-arbitrage-review_2026-09-02.md](protocol_kalshi-arbitrage-review_2026-09-02.md)
§2.1, quoted here verbatim so that this protocol is self-contained without
forking the definition:

> An instrument is an **in-scope instrument** iff ALL of:
>
> - **B-a.** Its payoff is a function of the realization of a **verifiable event**
>   (an outcome that is adjudicated and settled), not of a continuously
>   distributed price level. Contracts whose payoff is a continuous function of an
>   underlying (vanilla options, futures, swaps) fail B-a.
> - **B-b.** Its per-unit payoff at settlement takes **finitely many values and is
>   bounded**, and the canonical case — the case the review question is about — is
>   a payoff of exactly one unit on the event and zero otherwise. Parimutuel
>   claims, fixed-odds bets, and cash-or-nothing binary options satisfy B-b.
> - **B-c.** Its price is, or is convertible by a rule the source states to, an
>   **implied probability in [0,1]** for the event.
> - **B-d.** It is **traded** — on an exchange, betting exchange, bookmaker book,
>   parimutuel pool, or automated market maker. A probability *elicited* from
>   forecasters without a transferable traded claim (a survey, a scoring-rule
>   tournament with no position) fails B-d.

Any later divergence between this quotation and the frozen source text is
resolved **in favour of the source text**, and the divergence is recorded as an
amendment under section 10.

**One extension, stated as an extension and not as a re-definition.** A record
may be in scope by virtue of the *counterparty leg* of a cross-instrument
strategy — a settlement-source market such as an interest-rate future, a weather
product, or an index option — **only when** the record states the pairing against
an in-scope instrument. The non-binary leg is never in scope on its own. This is
a further stated widening relative to the predecessor and is listed as such in
section 2.3.

### 2.3 Inclusion criteria (N)

**Why the letter N.** The predecessor protocol uses **J1-J6** for its
judgement-call decision rules (its §2.6), so reusing J for inclusion criteria
here would give a reader grepping both files two unrelated rules under one code.
A, B, C, E, F, G, I, J, K, M, S, T, X and Y are all taken across the two
protocols; **N** is unused. The rename is recorded here so the choice is durable
rather than mysterious.

**Strategy-contribution codes (K).** A record makes an in-scope **strategy
contribution** iff it does at least one of:

- **K1 (states or implements).** States, derives, or implements a strategy or
  rule class for in-scope instruments — an arbitrage or coherence relation to be
  traded, a quoting or inventory rule, a signal, a systematic entry/exit
  discipline, or executable code that does any of these.
- **K2 (measures or reports).** Measures or reports an outcome of such a strategy
  or rule class — a realized or simulated return, a violation frequency, a fill
  rate, a spread capture, a backtest figure — attributable to a stated method and
  a stated data span.
- **K3 (precondition or constraint).** States a precondition, constraint, fee,
  rule, limit, interface capability, or settlement mechanic that **decides
  executability** of a strategy class, whether or not it names the strategy.
- **K4 (enabling data or tooling).** Provides data, an interface client, a
  capture pipeline, a backtest harness, or an analysis tool that enables K1, K2
  or K3, with its own documentation stating what it does.

**Inclusion criteria:**

- **N1.** The record concerns at least one in-scope instrument under section 2.2,
  or the counterparty leg extension there.
- **N2.** The record makes at least one strategy contribution K1-K4.
- **N3.** The record is **retrievable** by the executing agent without
  authentication, payment, or account creation, and its retrieved bytes can be
  **digested** — a SHA-256 over the retrieved payload is recordable. A record
  whose bytes cannot be digested is excluded under Y4.
- **N4.** The record is **dated**, or its **access date is recordable**. A
  publication date, commit or release date, effective date, or an ISO-8601 access
  timestamp all satisfy N4; at least one must be recorded.
- **N5.** Any language, any year, **any source class S-A..S-E** satisfying
  N1-N4. No document type is closed out in advance.
- **N6.** Where a record's eligibility turns on content that its metadata does not
  settle, it is promoted to stage 2 (section 4) rather than decided at stage 1.

> **N-NOTE — the departures from the 2026-09-02 protocol, named rather than
> buried.**
> **A persistent identifier is NOT required.** The predecessor's criterion I3
> requires a DOI, arXiv id, RePEc handle, or Handle-System handle, and its code
> X7 excludes every record without one. This protocol imposes no such
> requirement and has **no** exclusion code corresponding to X7.
>
> The persistent-identifier requirement is the DECISIVE departure and the one
> this branch exists for. It is not the only one, and the others are named rather
> than buried: **N3** replaces I4's abstract-depth test with
> retrievability-without-payment plus digestibility; **N4** adds a dating
> requirement the predecessor has none of; **N5** replaces I5's closed
> document-type list; the predecessor's **I6** and **§2.7 constraint 2**, which
> keep documentation-tier records out of the corpus flow, are deliberately NOT
> carried, so S-D records are counted in this flow; and the exclusion set is
> **Y1-Y9, not X1-X9**, with X3-X6 dropped and Y6/Y8/Y9 new. The inclusion
> criteria otherwise track I1-I6 in structure and intent. Section 2.2's
> counterparty-leg extension is a further stated widening. (Y3 and Y5 likewise
> have no predecessor analogue: they pair with the attribution obligation and
> with N4 respectively.)
>
> The decision, its rejected alternatives, and its costs are recorded in
> [ADR-0006](../decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md).
> The consequence carried into every downstream artifact: records admitted here
> carry a standing findability gap of the kind the predecessor's I3 existed to
> prevent (see ADR-0006 §"What the widening costs", which carries the citation)
> and are subject
> to content drift, so **warrant is per record and is labelled per record** — see
> section 5, fields F2 and F6, and section 7.

### 2.4 Exclusion criteria (Y)

Every excluded record carries exactly one **primary** exclusion code — the first
that applies, in the order below — and may carry secondary codes. Every excluded
record is published with its reason (section 4).

- **Y1 — not an in-scope instrument.** Fails section 2.2 and is not a stated
  counterparty leg of an in-scope pairing. Absorbs what the predecessor split
  across X1, X3 and X5.
- **Y2 — no strategy contribution.** Satisfies section 2.2 but makes none of
  K1-K4: descriptive commentary, market news, an explainer of what an event
  contract is, a price screenshot with no rule, no measurement, no precondition,
  and no tooling. Absorbs the predecessor's X2 and X4.
- **Y3 — UNSOURCED.** The strategy is asserted with **no locatable source** — it
  came from a summarizer, from an executing agent's own recall, or from a
  document that cannot be produced. Such a class is **excluded, and it is never
  recorded as a finding.** Per ADR-0004 and `REVIEW.md` blocking directive 8 an
  unattributed strategy is a blocking defect. The corpus record reports the
  unsourced class **as an absence**, in a named-gap section, never in the
  taxonomy.
- **Y4 — not retrievable or not digestible.** Fails N3: paywalled, behind
  authentication, dead link with no archived copy, or retrieved as a form that
  cannot be digested. The retrieval chain attempted is logged with the best
  available locator; a record is never completed from compiler memory.
- **Y5 — undated and no recordable access date.** Fails N4.
- **Y6 — paid product advertisement with no stated mechanism.** The record
  advertises a signal service, a bot, a course, or a data product and states no
  mechanism, rule, precondition, or measurable outcome. A paid product that DOES
  state a mechanism is assessed on that mechanism under K1/K3 and is not excluded
  by Y6.
- **Y7 — duplicate.** The same work already dispositioned under another locator;
  deduplicated per section 4.1 and itemized in the ledger with a pointer to the
  retained record.
- **Y8 — mirror or fork with no independent contribution.** A copy, mirror,
  vendored bundle, or fork of an already-included artifact that adds no strategy
  contribution of its own. A fork that adds a strategy, a venue adaptation, or a
  measurement is **included** as its own record and cites its parent. The
  underlying hazard — that a repository is not necessarily a project — is
  documented in the repository-mining literature named in section 7.
- **Y9 — out of the branch's question.** In-scope instrument, real contribution,
  but about something the section 1.1 question does not ask — for example pure
  tax filing mechanics with no bearing on executability, or platform UX.

The predecessor's **X6** (model with no stated applicability condition) has no
analogue here, because this protocol has no transfer clause of the kind X6
policed; a market-making model record is assessed under K1/K3 like any other.

**Capacity dispositions are NOT exclusions on the merits** and are coded
separately in section 4.

### 2.5 No post-freeze change to eligibility

**No eligibility criterion in section 2 may be changed, added, removed, or
reinterpreted after this file's registration commit.** Every change is an
append-only amendment recorded under section 10, exactly as the predecessor
protocol's §10 requires ("Frozen text above this line is never edited"). A
superseded provision is superseded **by** an addendum entry, in place, with the
original wording left legible. Silent deviation is a conduct violation, and an
amendment declared after the affected records were screened must say so in those
words.

The predecessor's amendment **A8** is the standing warning here: it relaxed
frozen criterion I4 after 33 affected records had been screened, extracted and
published, and had to publish an alternative reading of the whole corpus as the
price. This protocol's criteria are written to be met by the record classes it
actually intends to admit, so that no relaxation of that kind is needed.

---

## 3. Search arms — closed at freeze

Four arms. Each may be reported empty; none may be added or dropped without a
section 10 amendment.

### 3.0 What every arm must record, per query, without exception

This is the PRISMA-S obligation, and PRISMA-S applies here on its own terms, not
by analogy — see section 8. For **every** query executed in **every** arm, one
machine-readable log entry under
`docs/literature/search_logs/kalshi-strategy-multivocal/`, filename prefix `ks-`
(`CONVENTION` — the project search-log naming convention, matching the executed
practice of the `ka-` prefix in the predecessor branch), carrying at minimum:

| field | content | PRISMA-S item |
|---|---|---|
| `query_id` | The identifier assigned in the arm's query table (section 3.5), stable across retries | — |
| `query_verbatim` | The query string **exactly as executed**, byte-for-byte, including operators, quoting, and encoding | 8 ("copied and pasted exactly as run") |
| `endpoint` | The API endpoint URL or the platform and interface used | 1 ("stating the platform for each") |
| `executed_at` | ISO-8601 timestamp **with UTC offset** | 13 (date of search) |
| `http_status` | Status returned, or the client-side error | — |
| `n_returned` | Records returned in this response | 15 (per-source totals) |
| `n_total_reported` | Total hits the platform reports, where the platform reports one; `null` otherwise, with truncation flagged | 15 |
| `payload_sha256` | SHA-256 digest of the raw response bytes as received | — (project design choice, section 12) |
| `payload_path` | Repo-relative path of the stored raw payload, where stored | — |
| `retry_of` | The `query_id` this entry retries, if any | — |

A query that returns zero records is logged identically and is reported in the
corpus record. **Zero-yield queries are never dropped**; suppressing them is the
most common way a search strategy becomes non-reproducible.

Execution is deterministic where any script is involved: `PYTHONHASHSEED=0` is
asserted at entry of every dedup and screening script, matching the predecessor
branch's practice.

### 3.1 ACADEMIC arm (yields S-A, S-B)

**Endpoints/platforms.** Crossref REST, OpenAlex, arXiv API, Semantic Scholar,
RePEc/IDEAS, SSRN where reachable without authentication.

**Query construction rule — this is what freezes, not the strings.** Each query
is the conjunction of (i) one **instrument term** drawn from the frozen
instrument vocabulary — the terms naming binary event contracts, event
derivatives, prediction markets, or the named venues — and (ii) one **strategy
term** drawn from the frozen strategy vocabulary — arbitrage, coherence,
mispricing, market making, quoting, inventory, spread, execution, hedging,
forecasting-driven trading — with (iii) an optional **venue narrowing** term.
Every query is executed unrestricted by date and unrestricted by language.
Field restriction, where a platform offers it, is applied to title-and-abstract
only, never to full text, so that behaviour is comparable across platforms.
Category or subject narrowing is applied **only** where the unrestricted phrase
returns predominantly out-of-domain records, and the unrestricted form of the
same vocabulary is retained elsewhere in the arm; each narrowing is recorded in
the query table with the reason.

**Novelty differencing.** The arm records, per candidate, whether the record
already appears among the predecessor branch's dispositions. A record already
dispositioned there is still eligible here — the two protocols have different
admission bars — but the corpus record reports the overlap explicitly.

**Retrieval depth caps.** Per-response retrieval caps are `CONVENTION`, carried
from `protocol_kalshi-arbitrage-review_2026-09-02.md` §3.1 ("Retrieval caps"),
whose values appear in the §3.2 query strings, which in turn carries them from
`protocol_explosive-regime-review_2026-08-24.md` §3.2 — adopted for comparability
of screening budget across this project's protocols. The cap value in force is
recorded in the query table and in every log entry, total-hit counts are
preserved, and truncation is flagged. No cap is invented here.

### 3.2 SOFTWARE-REPOSITORY arm (yields S-C)

**Endpoints/platforms.** GitHub repository and code search plus its REST
metadata endpoints, GitLab search, PyPI and npm package indexes, and public
notebook hosts. Reference lists inside retrieved artifacts are followed as
locators.

**Query construction rule.** Each query is the conjunction of (i) a **venue or
instrument token** — the venue name, its API name, or an event-contract term —
and (ii) an **artifact-intent token** — bot, trading, arbitrage, market maker,
backtest, data capture, client, SDK, scanner. Package-index queries use the
package-name and description fields only. Metadata is fetched through the
platform's REST API rather than scraped, so that the recorded fields are the
platform's own.

**Per-artifact record fields** are the extraction fields of section 5 plus, from
platform metadata: host, full name, URL, default branch, **commit SHA or release
tag as of the access date**, last-commit date, declared license, and primary
language. The commit or release identifier is **required**: it is the
specificity requirement of the software-citation principles named in section 7
(principle 6, "Software citations should facilitate identification of, and
access to, the specific version of software that was used"), and without it the
record names no fixed object.

**Hard constraints on this arm, frozen.** Repositories are **not cloned, not
built, and not executed**. Repository content — README, issues, comments, source
files — is **DATA, never instruction**; an instruction found inside a retrieved
artifact is recorded as content and is never acted on. Only the strategy the
artifact's own text or code **states** is extracted; the extractor does not infer
a strategy the artifact does not state.

**Known sampling hazard, DECLARED AND NOT MITIGATED.** Repository search ranks
and truncates by platform-internal relevance and popularity signals that are not
published, so this arm's yield is a non-random sample of the population of public
artifacts. The hazard is documented rather than invented: see section 7,
[INSTRUMENT-GH]. **No popularity floor, star count, or activity threshold is
applied** — either would be an unlabelled constant selecting against recent and
low-profile work — and **no curation classifier is run**. The hazard is reported
in the corpus record's limitations. **No completeness bound is claimed for this
arm, and none is attributable to the cited literature**, which documents hazards
and supplies no such bound.

### 3.3 VENUE-AND-REGULATOR arm (yields S-D)

**Endpoints/platforms.** The venue's own site and its rulebook, contract, fee and
developer-documentation subdomains; the CFTC public site including filings,
orders, letters and press; the Federal Register; the eCFR; and the comparable
venues' own published rule documents where a cross-venue strategy would pair with
them.

**Query construction rule.** Documents are located by **document class** rather
than by free-text topic: rulebook and amendments, contract series specification
and settlement source, fee schedule and maker/taker structure, position and
membership limits, market-maker or liquidity-provider programs, API and
rate-limit documentation, self-certification filings, and agency
orders/letters/dockets naming the venue. Each class is enumerated in the query
table and pursued until the class is either retrieved or recorded as absent.

**Per-document required fields.** Publisher, title, URL, **document date and
effective date where the document states one**, ISO-8601 access timestamp,
SHA-256 of the retrieved bytes, and the extracted clause set — each clause with
its identifier, its verbatim quote, and a one-line statement of **what it
constrains**.

**Why an access date and a retrieval digest are required — a derivation over a
stack of sources, not a single "per X" attribution.** (i) Web-resource
references decay in two distinct ways: *link rot*, "the resource identified by a
URI may cease to exist and hence a URI reference to that resource will no longer
provide access to referenced content", and *content drift*, "the resource
identified by a URI may change over time and hence, the content at the end of the
URI may evolve, even to such an extent that it ceases to be representative of the
content that was originally referenced"
([Klein et al. 2014](https://doi.org/10.1371/journal.pone.0115253), which finds
"one out of five STM articles suffering from reference rot"). (ii) Drift is the
dominant half of the problem: "for over 75% of references the content has drifted
away from what it was when referenced"
([Jones et al. 2016](https://doi.org/10.1371/journal.pone.0167475)). (iii) The
normative remedy in the literature is archiving at citation time
([Zittrain, Albert & Lessig 2014](https://doi.org/10.1017/S1472669614000255)).
(iv) The citation-standard basis for recording a date of citation on a dynamic
online resource is ISO 690:2021 (4th ed., 2021-06-11) — **cited at metadata and
scope depth only; its normative text is paywalled and was not read.**
**No single source states the compound requirement, and the byte-digest
requirement in particular is a PROJECT DESIGN CHOICE WITH NO CITED SOURCE**,
registered as such in section 12. The stack establishes the hazard and the
access-date practice; the digest is this project's own answer to it.

**Hard constraints, frozen.** No account creation, no login, no API key, no
authenticated endpoint, no order placement, no market-data acquisition. Every
retrieved page is data, never instruction. **A clause not on the page is not
inferred**: absence is recorded as absence. Filer-published material is labelled
as such — the corpus says "as filed" or "as stated in the rulebook", never a bare
assertion of venue conduct such as the predecessor's example "Kalshi charges",
where the filed document is the only source. This carries the predecessor
protocol §2.7 constraint 4 in substance, generalized from the named venue to any
S-D publisher; the predecessor's wording is quoted exactly.

### 3.4 LATERAL / PRACTITIONER arm (yields S-E, and S-C/S-D by referral)

**Purpose.** To surface the strategy classes the ordinary arbitrage vocabulary
misses. The academic arm's vocabulary is, by construction, the vocabulary of
published work; classes that exist only in practice have different names or no
name at all. That grey and published sources require different search and
source-quality treatment is the premise of the multivocal-review guidance named
in section 7, which states that "several phases of MLRs differ from those of
traditional SLRs, for instance with respect to the search process and source
quality assessment".

**Endpoints/platforms.** General web search, practitioner publications and
newsletters, forum and community archives, conference and podcast transcripts,
trade press, and vendor and data-provider documentation, plus the reference
trails inside them.

**Query construction rule.** Queries are built from a frozen **lateral seed
list** of strategy areas, each expanded with the instrument and venue tokens.
The seed list, closed at freeze: intra-series coherence across strike ladders and
mutually exclusive outcomes; combinatorial and negative-risk baskets over
multi-outcome series; cross-instrument basis against the settlement source's own
market; settlement-source and resolution-rule edge cases; timing and latency
around scheduled data releases; maker-incentive and fee-structure exploitation;
liquidity-provision programs; inventory and capital-efficiency structures
specific to fully-collateralised binaries; account and tax structure where it
bears on executability; and forecasting-model-driven approaches including
model-agent forecasters. A seed area that returns nothing is reported as an
empty seed, not deleted.

**Hard constraint, frozen and blocking.** A class with **no locatable source** is
reported **UNSOURCED under Y3** and **must not enter the taxonomy**. No class may
be entered on model recall. No trading advice, no position sizing, and no
expected-return claim is produced by this arm or by any consumer of it.

### 3.5 Query tables — filled at execution, frozen as to rule

The concrete query strings are **not** fixed in this file. Each arm carries a
numbered query table which the executing agent fills in and logs:

| `query_id` | arm | endpoint | `query_verbatim` | `executed_at` | `n_returned` | `n_total_reported` | `payload_sha256` |
|---|---|---|---|---|---|---|---|

**What freezes is the construction rule in sections 3.1-3.4 and the recording
obligation in section 3.0.** A query that cannot be expressed under its arm's
construction rule may not be executed without a section 10 amendment, and an
executed query that departs from the rule is an amendment recorded before its
results are screened. The corpus record reproduces the completed tables in full,
including zero-yield rows.

**Search-strategy peer review.** No independent information specialist reviews
these strategies. That is a declared limitation, reported in the corpus record in
those words, and it is part of why section 8 says this is not a systematic
review.

---

## 4. Screening

### 4.1 Data management and deduplication

Raw payloads and per-query logs under
`docs/literature/search_logs/kalshi-strategy-multivocal/`, prefix `ks-`.

**Deduplication process, frozen.** Exact match on the strongest available
identifier first, in order: DOI (case-normalized), arXiv id, RePEc handle,
package index name plus version, repository host plus full name, then canonical
URL after stripping tracking parameters. Where no identifier matches, a
hand-verified same-work ledger handles twins: titles matching case- and
punctuation-insensitively, **or** a twin relation documented by one of the
records. Cross-class twins — a paper and its companion repository — are **not**
deduplicated; section 2.1 makes them two records with a `companion_of` link.
Deduplication is performed in Python under the project venv with
`PYTHONHASHSEED=0` asserted at entry; the script is stored with the logs. The
full ledger is itemized in the corpus record.

Included records enter
`docs/literature/references_kalshi-strategy-multivocal.json` (CSL-JSON), with
`software` entries for S-C records carrying repository URL, commit or release
identifier, and access date; `report` or `webpage` entries for S-D and S-E
carrying access date and the retrieved-bytes digest where one exists. The field
set and its normative basis — and the part of it that is a project choice rather
than a standard requirement — are stated in section 7 under [INSTRUMENT-SWCITE].

### 4.2 Stage 1 — automated / keyword disposition

Every deduplicated record receives exactly one stage-1 disposition: `include`,
`exclude` with a primary Y-code, or `promote` where eligibility is not decidable
at metadata depth (N6). Every verdict cites the criterion that decided it by
identifier (N-, K-, Y-, B-).

**Declared plainly: screening is single-pass.** One executing agent session
screens each arm's universe. There is no dual independent screening, no second
screener, no adjudicator, and **no inter-rater agreement statistic is computed or
may be reported** — with one screener there is nothing to agree with, and
reporting an agreement number would be a fabrication. The LLM agent is an
**automation tool** and is declared with its model and version in the corpus
record's front matter.

Where stage 1 is performed by keyword or regular-expression branching over
metadata, the branching rule is stored with the logs and the disposition names
the branch that produced it, so any row can be re-derived.

### 4.3 Stage 2 — read-based assessment

A record is promoted to stage 2 **iff** its metadata does not settle N1/N2 — by
decidability, never by a budget number. Stage-2 assessment is by **reading** the
record at the depth section 5 field F5 records: full text, abstract,
README-and-metadata, or metadata. The disposition states which.

Where the retrieval chain for a promoted record fails, the failure is Y4 with the
chain that failed logged. **Retrieval failure is not evidence of absence** and is
never converted into a substantive exclusion code.

### 4.4 Capacity gaps are not eligibility determinations

This is the predecessor branch's X10/X11 lesson, adopted at freeze rather than
discovered mid-execution. In that branch, amendments A4 and A5 had to introduce
two codes after screening because records that were merely *unassessed* were
otherwise indistinguishable from records that had *failed a criterion*.

Two capacity codes exist here from the start:

- **G1 — identified, eligibility not assessed.** The record entered the universe
  and no eligibility determination under N1-N6 was ever made for it. It is **not**
  eligible, **not** ineligible: it is **undecided**.
- **G2 — eligible, extraction not performed.** The record passed section 2 and no
  section-5 extraction was performed within the execution session.

**Rules, frozen:**

1. G1 and G2 are **capacity gaps, not criterion failures**. Every G-row's reason
   says, in those words, that eligibility (G1) or extraction (G2) was not
   performed and that nothing about the record's merits was determined.
2. G-rows sit inside `n_excluded` **only** so the arithmetic identities below
   close, and the corpus record reports the G1 and G2 counts **separately** from
   every Y-code count. A corpus record that folds G-rows into the Y totals is
   defective.
3. No G-row may be converted to a Y-code without the assessment that a Y-code
   asserts. Stretching Y2 or Y4 over an unassessed record is a false statement
   about that record.
4. A later session may decide a G-row, and does so as a numbered amendment
   stating the subset rule it applied and fixing that rule **before** any record
   in the subset is assessed.

### 4.5 Arithmetic identities that must close

Reported in the corpus record's front matter and reconciled in its flow section:

```
sum(per-arm n_records)               == n_identified
n_identified - n_duplicates_removed  == n_screened
n_screened   - n_excluded            == n_included
len(CSL-JSON store)                  == n_included
```

`n_excluded` is the sum of all Y-code rows **plus** all G-code rows, and the
corpus record publishes that decomposition. A count is never resolved by
rounding, by silent reclassification, or by dropping a row. Unlike the
predecessor, this flow includes S-C, S-D and S-E records (section 2.1).

### 4.6 Exclusion reporting

Two tables, both required in the corpus record, both required even if empty:

- **Table Y-full — every excluded record.** Columns: `id`, best locator,
  `source_class`, `stage_excluded`, `primary_code`, `secondary_codes`,
  `criterion_cited`, and a one-line reason in the screener's own words. Every row
  has a non-empty reason.
- **Table Y-read — records excluded after stage-2 reading.** The records that
  looked eligible enough to be read and did not survive it, each with the
  criterion that decided it and a sentence on what it was and why it failed. An
  empty table is reported as "no record reached stage-2 assessment and was then
  excluded", never omitted.

A third table is required for the unsourced classes: **Table Y3-unsourced**,
listing every strategy class encountered without a locatable source, so the
absence is visible rather than silently missing from the taxonomy.

---

## 5. Extraction schema — FROZEN

Extracted by the executing agent for every included record. **Single extractor,
no duplicate extraction** — see section 8, item 9.

| field | content |
|---|---|
| **F1** | **Record id.** Stable within this corpus, prefix `ks-`, assigned at deduplication and never reused |
| **F2** | **Source class** S-A / S-B / S-C / S-D / S-E, assigned by the first-match rule of section 2.1, plus the identifier or locator actually used (DOI, arXiv id, handle, repository host+full name+commit/release, package name+version, canonical URL) and, where none is persistent, an explicit `persistent_identifier: none` marker |
| **F3** | **Strategy class assigned** from the section 6 taxonomy, plus the contribution codes K1-K4 the record satisfies. A record may carry more than one class; each class carries its own evidence quote |
| **F4** | **Verbatim evidence quote** — the source's own words (or its own code, quoted as code) stating the strategy, the precondition, or the outcome. Transcribed exactly, never paraphrased, never silently corrected. A quotation that cannot be reproduced from the retrieved bytes is a defect |
| **F5** | **Evidence location** — file path and line range, section number, page, clause id, URL fragment, or timestamp, precise enough that a reader re-retrieving the object can find the quote |
| **F6** | **Extraction depth** — `full-text` / `abstract` / `README-and-metadata` / `metadata`. This is the record's warrant label and travels with every claim derived from it |
| **F7** | **Venue on which the strategy is established** — the exact market(s) the record's statement, data, or code is about, taken verbatim from the record and never inferred. `none/theoretical` where the record states no venue |
| **F8** | **Kalshi-specific vs transferred** — `kalshi-specific` / `transferred-with-stated-assumption` / `not-transferable-as-stated`. For the middle value the carrying assumption is written out in the record's own terms. Assigned from F7 mechanically, not reconstructed later |
| **F9** | **Preconditions the SOURCE ITSELF states** — fees and their structure, minimum tick and spread, collateral and capital lockup and its duration, position and rate limits, settlement source and resolution rule, latency or co-location requirement, data availability, account or membership status. Each precondition is quoted or cited to F5. **A precondition the source does not state is recorded as "not stated", never supplied by the extractor** |
| **F10** | **Outcome reported** — whether the source reports any outcome for the strategy and, if so, that outcome **verbatim, with its data span, its cost treatment and its uncertainty exactly as the source states them**. No figure is re-derived, re-scaled, rounded, or annualized. **The outcome is attributed, never adopted**: the corpus reports that the source states it, and states nothing itself |
| **F11** | **Attribution status (REVIEW.md directive 8 field).** For every rule the record states or uses: carried by a citation, by a derivation inside the record, or by neither. A record using an unattributed rule is INCLUDED — that is itself a finding about the literature — with the gap recorded here, and the corpus record may never restate such a rule as established |
| **F12** | **Retrieval and drift flags** — ISO-8601 access timestamp, SHA-256 of retrieved bytes, commit/release or effective date where applicable, archived-copy locator where used, and any access limitation encountered. The basis for the access timestamp is the reference-rot stack derived in §3.3; **the byte digest is a project design choice with no cited source**, registered in §12 |
| **F13** | **Relations** — `companion_of`, `fork_of`, `supersedes`, `duplicate_of`, each pointing at an F1 id in this corpus |
| **F14** | **`TO COMPUTE` handoffs** — every parameter an executing project would have to choose in order to act on this record, named with the selection procedure that would choose it, and left uncomputed per ADR-0003 |
| **F15** | **Grey-source credibility attributes (S-C, S-D, S-E only)** — the two dimensions of the Adams, Smart & Huff scheme named in §7, **recorded per record as attributes and NOT used to stratify, band, or rank**: *outlet control* and *expertise*, each described in the record's own observable terms (who produces it, whether production is moderated or edited under stated criteria, whether the producer's authority and knowledge can be determined). The source states the gradation is continuous; §7 states why no tier is assigned |

---

## 6. Strategy-class taxonomy skeleton

A **first-level partition only**, to be populated by the arms and **not
prejudged**. No class is asserted to exist in the record until an arm attributes
it to a source; a class populated by nothing is reported as **empty**, which is
itself a finding.

| class | scope |
|---|---|
| **T1** within-market coherence | Relations among prices inside one market or series: complementary legs, strike ladders, mutually exclusive and exhaustive bundles, monotonicity across strikes |
| **T2** cross-market / cross-venue | Price relations between the same or corresponding events on different venues |
| **T3** cross-instrument basis | Relations against a settlement-source market or a correlated conventional instrument, where the source states the pairing |
| **T4** systematic mispricing / behavioural | Persistent statistical deviations attributed to participant behaviour or market structure, including favourite-longshot type effects |
| **T5** market making and liquidity provision | Quoting, inventory, adverse-selection and spread-setting rules, and venue liquidity programs |
| **T6** mechanism / rule / fee structure | Strategies whose object is the venue's own mechanics: fee and maker-taker structure, settlement and resolution rules, limits, contract specification edges |
| **T7** information and forecasting | Strategies driven by an external forecast or information advantage, including model- and agent-based forecasting |
| **T8** infrastructure and tooling | Data capture, interface clients, backtest harnesses and analysis tooling that enable any of T1-T7 |

**A class an arm finds that does not fit is added by amendment under section 10,
not forced into a bucket.** Forcing is a silent redefinition of the taxonomy and
is the reason this rule is stated at freeze. Each taxonomy row in the corpus
record carries: the class, at least one source, the extraction depth of that
source, the venue of establishment, the Kalshi-specific/transferred split, and
the stated preconditions. **A row with an empty source column is a blocking
defect.**

---

## 7. Quality appraisal and source-handling instruments for S-C, S-D and S-E

Peer review does not exist for these classes, so the instruments governing their
admission and their credibility recording are **named external records, verified
before freeze**. Each was resolved and checked by a separate literature-check
session; the evidence, including the **verification depth** of each record and
the **declared gap** in each proposed use, is at
`docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json`.
**A placeholder surviving into the registration commit is itself a defect**;
none survives.

**Every record below was verified at ABSTRACT or METADATA depth, not from
publisher full text** (PDF text extraction was unavailable and the publishers
returned HTTP 403 to unauthenticated fetch). Three sub-claims were corroborated
only from search-index extraction and are marked where they are used. That depth
travels with every use made of them here.

### 7.1 [INSTRUMENT-MLR] — multivocal review conduct, and the credibility scheme

**(a) Conduct of a multivocal review.**
[Garousi, Felderer & Mäntylä 2019](https://doi.org/10.1016/j.infsof.2018.09.006),
*Information and Software Technology* 106:101-121, "Guidelines for including grey
literature and conducting multivocal literature reviews in software engineering".
Used for the premise that grey and published sources require different search and
source-quality treatment: "several phases of MLRs differ from those of
traditional SLRs, for instance with respect to the search process and source
quality assessment", and the guidelines "cover all phases of conducting and
reporting MLRs in SE from the planning phase, over conducting the review to the
final reporting of the review."

> **Declared gap, carried to the point of use.** The source **scopes itself to
> software engineering** — its guidelines are offered for conducting MLRs "in any
> area of SE", not in any field. Use here, for a binary-event-contract strategy
> corpus, is a **DECLARED TRANSFER** and is labelled as one wherever the corpus
> record relies on it. Its specific quality-assessment criteria table was
> corroborated only from citing papers and search-index extraction, because the
> publisher full text is paywalled; **no criterion from that table is applied as
> a rule in this protocol**, and the appraisal here is limited to the two
> recorded attributes in 7.1(b).

**(b) The credibility scheme, cited to its originating source.**
[Adams, Smart & Huff 2017](https://doi.org/10.1111/ijmr.12102), *International
Journal of Management Reviews* 19(4):432-454, "Shades of Grey: Guidelines for
Working with the Grey Literature in Systematic Reviews for Management and
Organizational Studies". The two dimensions, verbatim: **outlet control** —
"the extent to which content is produced, moderated or edited in conformance with
explicit and transparent knowledge creation criteria"; **expertise** — "the
extent to which the authority and knowledge of the producer of the content can be
determined".

The scheme is cited **here, to its originators**, and not to the MLR guideline
that reproduces it: citing the reproducer would be the chain-citation error the
charter's commitment 5 forbids.

> **CRITICAL CONSTRAINT, frozen.** The source states the scheme is a
> **continuum**: "Rather than having discrete bands, the gradation in both
> dimensions is on a continuous range between known and unknown." Therefore
> **this protocol does NOT impose a 1st/2nd/3rd tier as a hard membership rule,
> does not band records, and does not rank them**. Outlet control and expertise
> are recorded as **per-record attributes** (field F15) in the record's own
> observable terms, and they are **not a stratifier**: no screening verdict, no
> inclusion decision, and no weighting anywhere in this branch may be made from
> them. Imposing discrete tiers in a frozen protocol would overstate what the
> source licenses. The source is management and organizational studies; use here
> is a declared transfer, and its tier-to-source-type mapping was verified at
> secondary depth only (publisher full text HTTP 403) and is **not used**.

### 7.2 [INSTRUMENT-GH] — repository-mining hazards, and what they do and do not license

**(a) The hazards.**
[Kalliamvakou, Gousios, Blincoe, Singer, German & Damian 2014](https://doi.org/10.1145/2597073.2597074),
"The promises and perils of mining GitHub", MSR 2014:92-101; extended as
[Kalliamvakou et al. 2016](https://doi.org/10.1007/s10664-015-9393-5), *Empirical
Software Engineering* 21(5):2035-2071. Verbatim from the MSR abstract: "mining
GitHub for research purposes should take various potential perils into
consideration. We show, for example, that the majority of the projects are
personal and inactive; that GitHub is also being used for free storage and as a
Web hosting service; and that almost 40% of all pull requests do not appear as
merged, even though they were." The journal version adds: "approximately half of
GitHub's registered users do not have public activity."

These support §3.2's declared sampling hazard and §2.4's Y8 mirror/fork code.

> **Declared gaps, carried to the point of use.** (i) These papers document
> hazards and give recommendations; they supply **NO completeness bound**, and
> this protocol does **not** cite them for one — §1.1 and §3.2 claim no
> completeness for any arm. (ii) All findings are **conditioned on 2013-2014
> GitHub data** and are not re-verified for the platform's current state.
> (iii) The fork-specific peril ("Peril I: A repository is not necessarily a
> project") and the non-development-repository peril were verified **only from
> search-index extraction** of the PDFs, not from fetched primary text.

**(b) That the signal/noise problem exists — and why no filter follows from it.**
[Munaiah, Kroh, Cabrey & Nagappan 2017](https://doi.org/10.1007/s10664-017-9512-6),
*Empirical Software Engineering* 22(6):3219-3253, "Curating GitHub for engineered
software projects": "there are limited means of separating the signal (e.g.
repositories containing engineered software projects) from the noise (e.g.
repositories containing home work assignments). The proportion of noise in a
random sample of repositories could skew the study and may lead to researchers
reaching unrealistic, potentially inaccurate, conclusions."

> **Interaction with §3.2, stated so no reader concludes otherwise.** This
> protocol applies **no popularity floor, no activity threshold, and no curation
> classifier**. Munaiah et al. is cited **only** as establishing that the
> signal/noise problem exists, and therefore as the reason §3.2's hazard is
> **declared and not mitigated**. **The `reaper` tool was NOT run, and its
> framework is NOT applied as an eligibility filter here.** The paper's
> operationalisation is a **trained classifier** over measured dimensions — the
> paper reports its best classifier at 82% precision and 86% recall against a
> 200-repository ground truth — not a deterministic rule list; adopting it would
> require declaring a variant and would import a classifier's error rates into
> eligibility, which this protocol declines to do.

### 7.3 [INSTRUMENT-SWCITE] — what an S-C record must carry

**(a) Principles.**
[Smith, Katz, Niemeyer & FORCE11 Software Citation Working Group 2016](https://doi.org/10.7717/peerj-cs.86),
*PeerJ Computer Science* 2:e86, "Software citation principles". The working group
is a named author on the record and is not dropped. Three principles are relied
on, verbatim: **principle 2 (credit and attribution)**, "Software citations
should facilitate giving scholarly credit and normative, legal attribution to all
contributors to the software"; **principle 3 (unique identification)**, a software
citation "should include a method for identification that is machine actionable,
globally unique, interoperable, and recognized by at least a community of the
corresponding domain experts"; **principle 6 (specificity)**, "Software citations
should facilitate identification of, and access to, the specific version of
software that was used. Software identification should be as specific as
necessary, such as using version numbers, revision numbers, or variants such as
platforms."

Principle 6 is the basis for §3.2's required commit-or-release identifier.
Principle 3 is why a bare repository URL is never sufficient on its own.

> **Declared gap.** The principles say **NOTHING about CSL-JSON**. They justify
> recording an identifier, a specific version, and contributors; they do not
> prescribe a carrier format.

**(b) Field-level guidance where a repository has no DOI.**
[Katz, Chue Hong, Clark, Muench, Stall, Bouquin et al. 2021](https://doi.org/10.12688/f1000research.26932.2),
*F1000Research* 9:1257 (version 2, 12 January 2021), "Recognizing the value of
software: a software citation guide". This — not the principles paper — is the
record cited for **what fields a software citation should carry when no
persistent identifier exists**, which is the ordinary case for this branch's S-C
records.

**(c) The carrier format is a project choice.** Citation Style Language 1.0.2
Specification, Appendix IV (Variables), `docs.citationstyles.org` — no DOI;
**tier-2 official documentation** under the CLAUDE.md evidence hierarchy. CSL
1.0.2 defines `accessed` as a date variable and `version` as a standard variable,
but it is a **style and rendering specification that prescribes no metadata
schema**. Therefore **the CSL-JSON field set used in §4.1 is a documented PROJECT
DESIGN CHOICE**, labelled as such here and in §12, and is not presented as a
standard requirement.

### 7.4 What this section does NOT do

- **No numeric quality score is assigned**, here or by any consumer. A score
  would be an unlabelled constant with no external derivation, which the
  inherited parameter-selection rule and charter commitment 3 forbid.
- **No tiering, banding or ranking of grey sources** — see 7.1(b).
- **No certainty-of-evidence grade is produced.** Source class is not a certainty
  grade and may not be reported as one. GRADE is named in §8 item 15 **as the
  framework NOT applied, and is not cited here because it is not used.**
- **No risk-of-bias instrument is applied to any record.** The support for
  declining one is stated in §8: scoping studies "differ from systematic reviews
  because authors do not typically assess the quality of included studies"
  ([Levac, Colquhoun & O'Brien 2010](https://doi.org/10.1186/1748-5908-5-69) —
  health-framed, declared).
- The descriptive provenance fields that remain (F2 source class, F6 extraction
  depth, F10 reported outcome, F11 attribution status, F12 retrieval and drift
  flags, F15 credibility attributes) are **provenance, not appraisal**, and the
  corpus record must say so in those words.

---

## 8. What this protocol does NOT claim

**This protocol registers a multivocal SEARCH producing a COMPILED CORPUS
RECORD. It does not register a systematic review, and the artifact it produces is
not one.** The distinction is not cosmetic: PRISMA 2020 is a reporting guideline
for systematic reviews, and a corpus record borrowing its vocabulary while
missing its design requirements would be a reporting failure dressed as
compliance.

### 8.1 The standard split — which guideline applies on its own terms, and which does not

**PRISMA-S applies here on its own terms. It is NOT "adapted" and its use is NOT
reasoning by analogy.** PRISMA-S's terminology section states, verbatim:

> "Because we intend the checklist to be used in all fields and disciplines, we
> use 'systematic reviews' throughout this document as a representative name for
> the entire family of evidence syntheses. This includes, but is not limited to,
> scoping reviews, rapid reviews, realist reviews, metanarrative reviews, mixed
> methods reviews, umbrella reviews, and evidence maps."

That is an explicit, quotable self-endorsement covering both this document's
field and its output class. The search-reporting obligations in §3.0 are
therefore claimed **under PRISMA-S directly**: item 1 (name each source, stating
the platform), item 8 (search strategies "copied and pasted exactly as run"),
item 13 (date of the search), item 15 (records identified per source).
**The predecessor protocol's blanket "both ADAPTED" framing understates PRISMA-S
and is deliberately not copied into this file.**

**PRISMA 2020 does not reach this record, and every item invoked below is
reasoning by analogy with no cited endorsement.** PRISMA 2020's own scope is
"designed primarily for systematic reviews of studies that evaluate the effects
of health interventions", extended only to "reports of systematic reviews
evaluating other interventions (such as social or educational interventions)" and
to "systematic reviews with objectives other than evaluating interventions" — in
every case to *systematic* reviews. This is not one. The item-by-item map in §8.3
is offered because it is the most legible way to tell a reader what is missing,
**not** because the guideline endorses its use here; that is stated in those
words, and no compliance with PRISMA 2020 is claimed anywhere in this branch.

### 8.2 The output class, and its citable basis

The output class is a **scoping/mapping compilation**. Its framework citation is
[Arksey & O'Malley 2005](https://doi.org/10.1080/1364557032000119616),
*International Journal of Social Research Methodology* 8(1):19-32, "Scoping
studies: towards a methodological framework" — the domain-neutral record of the
three, published in a general social-research-methodology journal.

Its checklist citation is
[Tricco et al. 2018](https://doi.org/10.7326/M18-0850), *Annals of Internal
Medicine* 169(7):467-473, "PRISMA Extension for Scoping Reviews (PRISMA-ScR):
Checklist and Explanation": "Scoping reviews, a type of knowledge synthesis,
follow a systematic approach to map evidence on a topic and identify main
concepts, theories, sources, and knowledge gaps. … The final checklist contains
20 essential reporting items and 2 optional items." **Declared: PRISMA-ScR is
EQUATOR-developed and health-framed on its face**; it is cited as a checklist
reference and its framing is not concealed. **No claim of PRISMA-ScR compliance
is made**, because this record's screening and extraction are single-pass and its
sources are multivocal.

Declining a risk-of-bias instrument is supported by
[Levac, Colquhoun & O'Brien 2010](https://doi.org/10.1186/1748-5908-5-69),
*Implementation Science* 5:69: "Scoping studies differ from systematic reviews
because authors do not typically assess the quality of included studies."
**Declared: Levac et al. is explicitly about health research**; use here is a
transfer of a methodological point, not of a clinical one.

All three records were verified at abstract depth (see §7's depth statement and
the instrument-verification record).

### 8.3 PRISMA 2020 items this design does NOT meet — by analogy, per §8.1

Four design facts drive everything below: **screening is single-pass by one agent
with an LLM as the automation tool** (§4.2); **extraction is single-extractor**
(§5); **no validated risk-of-bias instrument is applied to any record** (§7); and
**the search strategies receive no independent information-specialist peer
review** (§3.5).

| item | topic | why unmet |
|---|---|---|
| 1 | Title: identify the report as a systematic review | The artifact is a compiled corpus record and is titled as one. Calling it a systematic review would be false |
| 2 | Abstract: PRISMA-for-Abstracts checklist | Not completed; several required entries (risk of bias, certainty, synthesis method) have no content to report, per items 11, 13 and 15 |
| 8 | Selection process: how many reviewers, whether independent, conflict resolution | One screener, no independence, no conflict-resolution procedure because no conflict can arise. The automation-tool declaration IS made — that part of item 8 is met; the dual-independence part is not |
| 9 | Data collection process | One extractor, no duplicate extraction of any field, no verification against a second extractor |
| 11 | Study risk of bias: tool and its application | No validated instrument fits S-C/S-D/S-E records; the §7 instruments govern admission, source handling and provenance, not risk of bias. Declining one is supported for a scoping output class by Levac et al. (§8.2) |
| 12 | Effect measures | **Inapplicable with rationale**, not unmet by omission: the corpus's objects are stated strategies, preconditions and heterogeneously-reported outcomes, not effect measures for a common outcome. No effect measure is chosen because none exists to choose |
| 13b | Preparation of data for synthesis | No conversion, transformation, or harmonization is performed; figures are transcribed as the sources state them (F10) |
| 13c | Methods to tabulate or display individual results | Tables are descriptive by strategy class; records are not comparable on a common estimand |
| 13d | Methods to synthesize results | No statistical synthesis is performed at all |
| 13e | Exploring causes of heterogeneity | Follows 13d |
| 13f | Sensitivity analyses | Follows 13d |
| 14 | Reporting-bias assessment | Not assessed. Funnel-plot methods need a common effect estimate and standard error, which this corpus does not have. The repository-search and grey-literature selection hazards are **declared** (§3.2, §7.2) rather than assessed |
| 15 | Certainty assessment | GRADE — named as the framework **not applied**, and not cited here because it is not used — is not applied. Source class and extraction depth are recorded and are NOT a certainty-of-evidence assessment |
| 18 | Results: risk of bias in included studies | Follows item 11 |
| 19 | Results: effect estimate and precision per study | Sources are heterogeneous; F10 transcribes what each reports, which is frequently not an effect estimate with precision |
| 20b | Results of statistical syntheses | Follows 13d |
| 20c | Causes of heterogeneity | Follows 13d |
| 20d | Sensitivity analyses | Follows 13d |
| 21 | Results: reporting biases | Follows item 14 |
| 22 | Results: certainty of evidence | Follows item 15 |

Nineteen items unmet: **1, 2, 8, 9, 11, 13b, 13c, 13d, 13e, 13f, 14, 15, 18, 19,
20b, 20c, 20d, 21, 22.** **Item 12 is recorded separately as inapplicable with
rationale**, not unmet by omission.

**Items the corpus record IS expected to meet**, stated so the enumeration above
is not read as a blanket disclaimer: 3 rationale; 4 objectives; 5 eligibility
criteria (frozen here, cited by identifier); 6 information sources with platforms
and dates; 7 search strategies verbatim including zero-yield queries; 10a/10b
data items; 13a the grouping rule; 16a flow; 16b exclusions with reasons — met
and exceeded, since every exclusion is published rather than only the read-stage
ones; 17 record characteristics; 20a characteristics of contributing records;
23a-23d discussion including limitations of the review process; 24a registration
status (not registered, with the reason, and the provenance commit named as the
registration event); 24b protocol availability (this file); 24c amendments
(section 10); 25 support; 26 competing interests; 27 availability of data, code
and materials. These are listed as the reporting content the corpus record
carries, not as compliance with a guideline whose scope does not reach it.

### 8.4 And what may not be said

The corpus record, the branch agenda, and every downstream artifact must not
describe this work as a systematic review, must not report an inter-rater
agreement statistic, must not report a certainty-of-evidence grade, must not
present the absence of a risk-of-bias table as an oversight rather than a
declared design limit, must not claim PRISMA 2020 or PRISMA-ScR compliance, must
not band or rank grey sources, and must not claim completeness of any arm.

---

## 9. Scope boundary — ADR-0003, restated verbatim in force

[ADR-0003](../decisions/ADR-0003-specification-not-execution.md) governs this
protocol without exception. Restated so that no section above can be read past
it:

**No artifact produced under this protocol acquires market data, calls an
exchange API, computes a price, fits a model, backtests anything, or states a
tradeable rule.**

Concretely, and blocking:

- No account, no login, no API key, no authenticated endpoint, no order
  placement, no order-book capture, no tick or trade data acquisition.
- No price, spread, implied probability, edge, expected value, Sharpe ratio, or
  position size is computed anywhere in this branch's artifacts.
- No repository is cloned, built, or executed (§3.2).
- No strategy is recommended, endorsed, sized, or presented as profitable. An
  outcome a source reports is reported **as that source's statement** (F10) and
  is never adopted.
- **Every parameter an executing project would have to choose is left
  `TO COMPUTE`, with its selection procedure named** — the estimator, the search
  or cross-validation design, the information criterion, or the bootstrap
  interval that would choose it — per CLAUDE.md §Scope's inherited user-global
  rules (`~/.claude/CLAUDE.md` §"Parameter & Prompt Selection", not tracked in
  this repository) and, as the in-repo carrier, charter commitment 3 "No
  unlabelled constants"; and per ADR-0003 §Decision. A number filled in here
  instead of handed off is a defect, not a convenience.
- Where the corpus exposes a testable proposition, the branch **specifies** the
  test — null, statistic, surrogate, aggregation rule, refutation condition — and
  runs none of it. A specification written here must be specifiable **under**
  `REVIEW.md` directives 1-7; a specification that could not satisfy them is
  defective at the point of writing even though nothing here will run it
  (ADR-0004 §"These seven bind the branch's first empirical stage").

---

## 10. Amendment mechanism — APPEND-ONLY ADDENDUM BELOW THIS SECTION

This protocol freezes at its provenance commit. During execution, **ANY**
deviation — a query that will not execute as written, a platform change, an
eligibility edge the criteria do not decide, a source class that does not
partition a record cleanly, a taxonomy class that does not fit, a cap change, a
source that becomes unreachable — is recorded as a **numbered, dated,
append-only amendment** `M{n}`, stating:

1. the amendment number `M{n}` and the ISO-8601 date;
2. what changed, **quoted against the frozen text it modifies**;
3. why;
4. **at what execution stage** — specifically, whether the affected records had
   already been seen, screened, or extracted when the deviation was decided;
5. which arm(s), criteria, or fields it touches, by identifier.

**Every amendment is recorded in two places, and both are required:**

- `docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl`,
  one JSON object per amendment, machine-readable, written at the time the
  deviation is decided;
- this file's own **Addendum** below, in prose.

A discrepancy between the two is itself a defect and is corrected by a further
amendment, never by editing either record.

**Frozen text above this line is never edited.** A superseded provision is
superseded **by** an addendum entry, in place, and the original wording stays
legible. **Silent deviation is a conduct violation.** An amendment logged after
the affected decisions were made must say so in those words; that is a weaker
amendment than a pre-execution one, and the corpus record reports the
distinction. The predecessor's A8 is the worked example of how expensive a
retrospective eligibility amendment is (§2.5). The corpus record's front matter
cites this protocol's path and commit hash and enumerates every amendment it ran
under; a corpus record that ran under an amendment it does not enumerate is
defective.

---

## 11. Registration

**The registration event for this protocol is its provenance commit.**

1. The file is committed **before any query of any arm executes**.
2. That commit records the file's **SHA-256**, carried in the commit subject and
   in the `Repro-Log-SHA256:` / `Repro-Log-Path:` trailers written by
   `/commit-with-provenance`, per the CLAUDE.md reproducibility contract. The
   commit is the clone-durable carrier, because `logs/` and `artifacts/` are
   gitignored and their paths do not resolve in a fresh clone.
3. **The hash is computed and committed by the LEAD session** — not by the
   drafting agent and not by any executing agent. This mirrors the predecessor
   protocol's registration clause and exists so that the party that freezes the
   protocol is not the party that benefits from a looser one.
4. **This file cannot contain its own hash.** Any construction that appeared to
   do so would be false: writing the digest into the file changes the digest.
   The hash lives in the commit, and the corpus record cites it from there.
5. **Not registered in PROSPERO**: PROSPERO accepts only reviews with
   health-related outcomes, and this review has none. The absence of an external
   registry is a limitation, reported as such, not a compliance claim.
6. The registration commit must be an **ancestor of every commit** touching
   `docs/literature/search_logs/kalshi-strategy-multivocal/`, with **exactly two
   permitted exceptions**, both of which are pre-registration inputs that execute
   no query, retrieve nothing, and contain no search result:
   - `ks-instrument-verification.json` — the verification evidence on which
     section 7's instruments are named. It must exist before the protocol that
     cites it can freeze, or section 7 would freeze around unverified records.
   - `ks-prior-identifiers.json` — the novelty-differencing index the ACADEMIC
     arm consumes (section 3.1). It is derived entirely from two files already in
     the repository — the predecessor branch's `ka-screening-verdicts.jsonl` and
     `ka-s4-completion-screen.jsonl`, both pinned by SHA-256 inside it — and it
     is an input to a search, never an output of one.

   Both are listed here **by name in frozen text** so the exception cannot later
   be widened by argument: any other file appearing in that directory before the
   registration commit is a freeze violation. That ancestry, with these two
   exclusions and no others, is the mechanical check that the protocol froze
   first.

---

## 12. Conventions register

Per the inherited parameter-selection rule (`~/.claude/CLAUDE.md` §"Parameter &
Prompt Selection", untracked; in-repo carrier: charter commitment 3, "No
unlabelled constants"): zero arbitrary thresholds, zero magic numbers. Every
numeric or stylistic choice in this file is either derived with a stated
rationale, labelled `CONVENTION` with its provenance, quoted from a cited source,
or deliberately absent.

| element | status | source / derivation |
|---|---|---|
| Search-log directory `docs/literature/search_logs/kalshi-strategy-multivocal/` and filename prefix `ks-` | `CONVENTION` | Project search-log naming convention, matching the executed `ka-` practice of `protocol_kalshi-arbitrage-review_2026-09-02.md` §4.1 |
| Artifact filename pattern `{type}_{description}_{YYYY-MM-DD}.md` | `CONVENTION` | CLAUDE.md-inherited naming rule (`~/.claude/CLAUDE.md` §"Output Placement & Naming", untracked); in-repo carrier: charter §"Admissible output types" |
| Per-response retrieval caps in the ACADEMIC arm | `CONVENTION`, value carried not invented | Carried from `protocol_kalshi-arbitrage-review_2026-09-02.md` §3.1 ("Retrieval caps"), whose values appear in the §3.2 query strings, which in turn carries them from `protocol_explosive-regime-review_2026-08-24.md` §3.2. Caps bound retrieval depth only; total-hit counts are preserved and truncation is flagged (§3.1) |
| `PYTHONHASHSEED=0` asserted at entry of every script | **derived** | Determinism of dedup and screening output; carried from the predecessor branch's executed practice |
| Deduplication same-work rule (case- and punctuation-insensitive title match, or a documented twin relation) | `CONVENTION` | Carried from `protocol_kalshi-arbitrage-review_2026-09-02.md` §4.1 |
| Inclusion-criterion letter `N` (N1-N6) | **derived** | The predecessor uses J1-J6 for judgement-call rules (its §2.6); A, B, C, E, F, G, I, J, K, M, S, T, X, Y are taken across the two protocols. N is unused (§2.3) |
| Number of source classes (5) | **derived** | The partition of retrievable record types the §1.1 question requires, with peer-review status and publisher type as the two discriminating axes. Not a budget |
| Number of search arms (4) | **derived** | One arm per source-locating mechanism: scholarly indexes, code hosts, venue/regulator publishers, open web. Arms are not sized; each runs its construction rule to completion or reports its stopping point |
| Taxonomy first-level classes (8) | **derived, and explicitly provisional** | A partition of the strategy space named in the §1.1 question; §6 requires that a class which does not fit be **added by amendment**, so the count is a consequence of the partition and not a cap |
| Date bound: none | **derived** | Strategy statements, preconditions and tooling are not time-bounded in relevance, and the venue of interest is recent; a lower bound would amputate the foundational statements and an upper bound is meaningless for a single-execution search |
| Language bound: none | **derived** | Strategy statements and preconditions are extractable independently of prose language; the extraction-depth flag (F6) handles the remainder |
| Persistent identifier requirement: **none** | **decided, recorded** | The decisive departure from the predecessor's I3/X7; decision, alternatives and costs in [ADR-0006](../decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md) |
| S-C required commit or release identifier | **cited** | Software citation principle 6 (specificity), Smith et al. 2016 (§7.3a), verified at abstract depth |
| `accessed_at` on every S-C/S-D/S-E record | **cited stack, derived requirement** | Klein et al. 2014; Jones et al. 2016; Zittrain et al. 2014; ISO 690:2021 at metadata/scope depth (§3.3). No single source states the compound requirement |
| **SHA-256 digest of retrieved bytes** | **PROJECT DESIGN CHOICE, no cited source** | Explicitly labelled: the reference-rot literature establishes the hazard and the archiving remedy, and none of it prescribes a byte digest. This project's own answer (§3.3, F12) |
| CSL-JSON as the store format and its exact field names | **PROJECT DESIGN CHOICE, documented** | CSL 1.0.2 defines `accessed` and `version` but is a style/rendering spec prescribing no metadata schema; the software-citation principles say nothing about CSL-JSON (§7.3c) |
| Repository popularity / star / activity floor | **deliberately absent** | Any floor would be an unlabelled constant selecting against recent and low-profile artifacts. The resulting sampling hazard is declared in §3.2 and §7.2 instead of thresholded away |
| Curation classifier (`reaper`) as an eligibility filter | **deliberately not applied** | Munaiah et al. 2017 report a trained classifier at 82% precision / 86% recall against a 200-repository ground truth — figures quoted from the source, not adopted as parameters. Applying it would import classifier error into eligibility (§7.2b) |
| Grey-source credibility tiers or bands | **deliberately absent** | Adams, Smart & Huff state the gradation is continuous, "Rather than having discrete bands"; F15 records the two dimensions as attributes and nothing stratifies on them (§7.1b) |
| Numeric quality score for S-C/S-D/S-E | **deliberately absent** | No external derivation exists for such a score; §7 records descriptive provenance fields instead |
| Recall-check pass criterion | **deliberately absent** | A numeric recall target would be an unlabelled constant. Per-arm coverage limits are reported and interpreted |
| Stage-2 promotion depth | **derived** | Governed by decidability — a record is promoted iff its metadata does not settle N1/N2 — not by a budget number (§4.3) |
| Number of screeners (1) and extractors (1) | **declared design choice** | Not a threshold: a stated design limit whose consequences are enumerated in §8 |

Numbers quoted from cited sources and **not** adopted as this project's
parameters: "almost 40% of all pull requests do not appear as merged";
"approximately half of GitHub's registered users do not have public activity";
82% precision / 86% recall on a 200-repository ground truth; "one out of five STM
articles suffering from reference rot"; "over 75% of references the content has
drifted"; "more than 70% of the URLs within the Harvard Law Review and other
journals, and 50% of the URLs within United States Supreme Court opinions";
PRISMA-ScR's "20 essential reporting items and 2 optional items". Each is a
verbatim source figure with its citation at the point of use.

**Identity hygiene.** No OS username, no email address, and no absolute
home-directory path appears in this protocol, and none may appear in the corpus
record, the CSL-JSON store, or the logs. The two `~/.claude/` references above
are named as untracked rule locations, not as filesystem paths to be resolved,
and each carries an in-repo substitute. Repo-relative paths throughout.
Real-name *attribution* is this repository's declared policy (CLAUDE.md
§"Identity hygiene") and is carried by git config, not by file contents.

---

## 13. Works and documents cited by this protocol

**No external bibliographic citation is asserted in this file beyond the
reporting guidelines named in the front matter and the appraisal instruments
named in §7** — PRISMA-P 2015 (Moher et al. 2015, doi:10.1186/2046-4053-4-1),
PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z) and PRISMA 2020
(Page et al. 2021, doi:10.1136/bmj.n71), each carried unchanged from the
predecessor protocol §12 and resolved there against the DOI Handle System (29/29
responseCode 1; record at
`docs/literature/search_logs/kalshi-arbitrage/protocol-doicheck.json`); plus the
§7 instruments, each verified before freeze and recorded at
`docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json`.

**External records relied on, with verification depth.** All were verified at
abstract or metadata depth unless stated; none was read from publisher full text
in the verifying session.

| record | DOI / locator | used for | depth |
|---|---|---|---|
| Garousi V, Felderer M, Mäntylä MV. *Guidelines for including grey literature and conducting multivocal literature reviews in software engineering.* Information and Software Technology. 2019;106:101-121 | 10.1016/j.infsof.2018.09.006 | MLR conduct premise (§3.4, §7.1a). **Declared transfer from software engineering** | abstract; criteria table from citing papers / search-index only, and not applied |
| Adams RJ, Smart P, Huff AS. *Shades of Grey: Guidelines for Working with the Grey Literature in Systematic Reviews for Management and Organizational Studies.* International Journal of Management Reviews. 2017;19(4):432-454 | 10.1111/ijmr.12102 | Originating source of the outlet-control / expertise dimensions (§7.1b, F15). **Continuum, not tiers** | abstract; tier mapping secondary depth only, not used |
| Kalliamvakou E, Gousios G, Blincoe K, Singer L, German DM, Damian D. *The promises and perils of mining GitHub.* MSR 2014:92-101 | 10.1145/2597073.2597074 | Repository-mining hazards (§3.2, §7.2a, Y8). **No completeness bound attributable** | abstract; peril headings from search-index extraction only |
| Kalliamvakou E, et al. *An in-depth study of the promises and perils of mining GitHub.* Empirical Software Engineering. 2016;21(5):2035-2071 | 10.1007/s10664-015-9393-5 | Extended version of the above; conditioned on 2013-2014 data | abstract |
| Munaiah N, Kroh S, Cabrey C, Nagappan M. *Curating GitHub for engineered software projects.* Empirical Software Engineering. 2017;22(6):3219-3253 | 10.1007/s10664-017-9512-6 | That the signal/noise problem exists (§7.2b). **Classifier NOT applied here** | abstract |
| Smith AM, Katz DS, Niemeyer KE, FORCE11 Software Citation Working Group. *Software citation principles.* PeerJ Computer Science. 2016;2:e86 | 10.7717/peerj-cs.86 | Principles 2, 3, 6 (§3.2, §7.3a). **Says nothing about CSL-JSON** | abstract |
| Katz DS, Chue Hong NP, Clark T, Muench A, Stall S, Bouquin D, et al. *Recognizing the value of software: a software citation guide.* F1000Research. 2021;9:1257 (v2, 12 January 2021) | 10.12688/f1000research.26932.2 | Field-level guidance where a repository has no DOI (§7.3b) | metadata |
| Citation Style Language 1.0.2 Specification, Appendix IV (Variables) | `docs.citationstyles.org` — no DOI; tier-2 official documentation | `accessed` and `version` variables; **prescribes no metadata schema** (§7.3c) | official documentation |
| Klein M, Van de Sompel H, Sanderson R, Shankar H, Balakireva L, Zhou K, Tobin R. *Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot.* PLoS ONE. 2014;9(12):e115253 | 10.1371/journal.pone.0115253 | Link rot and content drift definitions; hazard scale (§3.3) | full-text (verifying session) |
| Jones SM, Van de Sompel H, Shankar H, Klein M, Tobin R, Grover C. *Scholarly Context Adrift: Three out of Four URI References Lead to Changed Content.* PLOS ONE. 2016;11(12):e0167475 | 10.1371/journal.pone.0167475 | Drift dominance (§3.3) | full-text (verifying session) |
| Zittrain J, Albert K, Lessig L. *Perma: Scoping and Addressing the Problem of Link and Reference Rot in Legal Citations.* Legal Information Management. 2014;14(2):88-99 | 10.1017/S1472669614000255 | Normative archiving remedy (§3.3) | full-text (verifying session) |
| ISO 690:2021, *Information and documentation — Guidelines for bibliographic references and citations to information resources*, 4th ed., 2021-06-11 | no DOI | Citation-standard basis for a date of citation on dynamic online resources (§3.3) | **metadata / scope only; normative text paywalled and not read** |
| Arksey H, O'Malley L. *Scoping studies: towards a methodological framework.* International Journal of Social Research Methodology. 2005;8(1):19-32 | 10.1080/1364557032000119616 | Output-class framework citation; domain-neutral (§8.2) | abstract |
| Tricco AC, Lillie E, Zarin W, et al. *PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation.* Annals of Internal Medicine. 2018;169(7):467-473 | 10.7326/M18-0850 | Checklist citation. **EQUATOR-developed and health-framed; no compliance claimed** (§8.2) | abstract |
| Levac D, Colquhoun H, O'Brien KK. *Scoping studies: advancing the methodology.* Implementation Science. 2010;5:69 | 10.1186/1748-5908-5-69 | Support for declining a quality-appraisal instrument. **Health-framed** (§7.4, §8.2) | abstract |

**In-repository documents this protocol depends on, cited by path:**

- [docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md](protocol_kalshi-arbitrage-review_2026-09-02.md)
  — the precedent whose structure this mirrors; §2.1 quoted in §2.2 above; §2.3
  (I3, I4, I5, I6) and §2.4 (X7) are the criteria this protocol departs from;
  §2.6 (J1-J6, the reason for the N rename); §2.7 (S7 constraints); §3.1
  (retrieval caps); §4.3 count identities; §9.1 enumeration form; §10 amendment
  mechanism; addendum A4, A5, A8, A18 §(c).
- [docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md](../decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md)
  — the scope decision registering this branch and the widened directive-8
  carrier reading.
- [docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md](../decisions/ADR-0004-quant-rule-adoption-prediction-markets.md)
  — the review-standard adoption and blocking directive 8.
- [docs/decisions/ADR-0003-specification-not-execution.md](../decisions/ADR-0003-specification-not-execution.md)
  — the scope boundary restated in §9.
- [docs/methodology/charter_castles_2026-08-21.md](charter_castles_2026-08-21.md)
  — admissible output types; commitment 3 (no unlabelled constants); commitment 5
  (attribution fidelity; the prohibition on chain citation applied in §7.1b); the
  systematic-review standard this document declines to claim.
- [docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md](../deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md)
  — the session declaration this protocol serves.
- `docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json`
  — the pre-freeze instrument verification record, including every declared gap
  carried into §7.
- `CLAUDE.md` — reproducibility contract, identity hygiene, and the inherited
  user-global rules named in §9 and §12.
- `REVIEW.md` — blocking directive 8, quoted verbatim in the front matter,
  adopted for this branch by ADR-0004.

---

## Addendum (append-only; empty at freeze)

No amendment has been made. The first amendment entry is `M1`.

Entries below this line are added, never edited, and each states its number,
date, what changed quoted against the frozen text, why, the execution stage at
which it was decided, and the identifiers it touches. The machine-readable twin
of every entry lives at
`docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl`.


---

### M1 - 2026-09-04 - three ACADEMIC-arm query-construction departures, adjudicated PRE-SCREENING - section 3.1; PRISMA-S items 1, 8

**Execution stage - this is a PRE-SCREENING amendment, and that is the strongest
form section 10 recognises.** The executing agent reported all three departures in
its return, before assigning any stage-1 disposition. Every one of the arm's 528
identified records is a `G1` row: identified, eligibility not assessed. **No
record's eligibility was decided under any departure, because no record's
eligibility was decided at all.** This is not the predecessor's A8 position
(section 2.5), and the corpus record must not describe it as one.

**Who decided.** The lead session, not the executing agent and not the drafting
agent - the same allocation section 11(3) fixes for the freeze hash, for the same
reason: the party that runs the queries is not the party that rules on whether
they were in bounds.

#### M1(a) - contract-family qualifiers in the INSTRUMENT slot - GRANTED, with the reading fixed

*Frozen text (section 3.1), quoted:* each query conjoins "one **instrument term**
drawn from the frozen instrument vocabulary - the terms naming binary event
contracts, event derivatives, prediction markets, or the named venues".

*What was done:* `weather derivative`, `economic derivatives` and
`macroeconomic derivatives` were placed in the instrument slot
(`ks-crossref-16`, `ks-crossref-17`, `ks-openalex-09`, `ks-openalex-10`,
`ks-openalex-11`, `ks-arxiv-09`, `ks-arxiv-10`).

*Ruling - GRANTED, and the construal is narrowed so it cannot travel further.* A
contract-family qualifier may occupy the instrument slot **only** where one of
two conditions holds, and the query log must record which:

1. the family is itself an **event-derivative family** - its payoff is contingent
   on the occurrence or non-occurrence of a verifiable event. `economic
   derivatives` and `macroeconomic derivatives` satisfy this directly: they name
   the auction-based binary claims on scheduled data releases, which is an event
   derivative under any reading of the frozen phrase "event derivatives"; or
2. the term names a **section 2.2 counterparty leg** - the non-binary instrument
   a basis strategy would pair against. `weather derivative` enters on this
   condition and **not** on condition 1: an HDD/CDD swap is index-linked, not
   binary, and is not an event contract. Its admission is as a counterparty leg,
   which section 2.2 already contemplates.

*What this does NOT license.* It does not open the instrument slot to any
financial-instrument noun. A term that names neither an event-contingent payoff
family nor a section 2.2 counterparty leg remains outside the slot.

*Traceability requirement, binding on the corpus record.* Records reaching the
corpus **only** through `ks-crossref-16/17`, `ks-openalex-09/10/11` or
`ks-arxiv-09/10` are tagged `reached_via: M1a`, so a reviewer who rejects this
construal can withdraw exactly those records and no others.

#### M1(b) - an agent/model-class qualifier in the STRATEGY slot - GRANTED, narrowly

*Frozen text (section 3.1), quoted:* "one **strategy term** drawn from the frozen
strategy vocabulary - arbitrage, coherence, mispricing, market making, quoting,
inventory, spread, execution, hedging, forecasting-driven trading".

*What was done:* `ks-arxiv-13` used `abs:"trading agent"`, which is not in that
list.

*Ruling - GRANTED, narrowly.* An agent- or model-class qualifier is admissible in
the strategy slot **only** where the branch's own frozen text already names the
area. It does here: section 3.4's frozen lateral seed list, item 10, names
"forecasting-model-driven approaches, including model-agent forecasters". The
protocol therefore already contemplates the object; the academic arm's vocabulary
simply did not carry a term for it. Granting this **aligns the two arms rather
than widening the branch**.

*What this does NOT license.* An agent-class term whose area is **not** named in
section 3.4's seed list is outside the slot. `trading agent` is admitted; a
general actor-class noun is not.

*Traceability:* records reaching only through `ks-arxiv-13` are tagged
`reached_via: M1b`.

#### M1(c) - container narrowing to SSRN - GRANTED, as a REACHING device only

*Frozen text (section 3.1), quoted:* "Category or subject narrowing is applied
**only** where the unrestricted phrase returns predominantly out-of-domain
records ... each narrowing is recorded in the query table with the reason."

*What was done:* `ks-crossref-14` set `query.container-title=SSRN`. A container
restriction is neither a category nor a subject narrowing, so the frozen clause
does not authorise it on its face.

*Ruling - GRANTED, and the distinction that makes it admissible is stated so it
binds future queries.* A container restriction is admissible **only where it
REACHES a source that is otherwise unreachable**, never where it EXCLUDES records
that would otherwise be retrieved. This one reaches: SSRN's own search interface
returned HTTP 403 unauthenticated (`ks-ssrn-01`), and SSRN is the container of a
large share of this branch's most on-point records. The restriction adds a
retrieval path; it removes none. A container restriction used to filter an
otherwise-successful query is a different act and stays unauthorised.

*Precedent, recorded rather than relied on:* the predecessor branch executed the
same device at `ka-crossref-13/14`. Precedent is not authority here - the ruling
rests on the reach/exclude distinction, not on the predecessor's practice.

*Traceability:* records reaching only through `ks-crossref-14` are tagged
`reached_via: M1c`.

#### What M1 does not touch

No eligibility criterion `N1`-`N6` or `Y1`-`Y9` is altered, added, removed, or
reinterpreted. No contribution code, no extraction field, no taxonomy class, no
screening rule, and no arithmetic identity is changed. M1 rules on **query
admissibility only**, and it was decided before any record was screened.


---

### M2 - 2026-09-04 - section 4.2's disposition enumeration reconciled with section 4.4's capacity codes - POST-EXECUTION, and the weakness is declared

**Raised by audit finding SCOPE-1-7.** This amendment corrects an internal
contradiction in the FROZEN TEXT, not a departure by an executing agent.

**What the frozen text says, quoted against itself.** Section 4.2 states that
every deduplicated record receives exactly ONE stage-1 disposition and enumerates
three: `include`, `exclude` with a Y-code, and `promote`. Section 4.4 then creates
the capacity codes `G1` and `G2`, which are none of the three, and states that a
capacity gap is "NOT a criterion failure and NOT an eligibility determination".

**Why it matters.** **1,465 of the 1,574 screened records - 93% of the delivered
flow - took the path section 4.2 does not enumerate.** A reader reconciling the
corpus record against section 4.2 alone would conclude either that 1,465 records
are missing a disposition or that G-rows are a species of `exclude`. The second
reading is the one section 4.4 exists to forbid, and it is the reading that would
convert 1,465 capacity gaps into 1,465 eligibility determinations.

**Ruling.** Section 4.2's enumeration is incomplete, and **a G-code is a FOURTH
stage-1 outcome**. Section 4.2's "exactly one disposition" is read as conditional
on assessment capacity: a record that is never assessed receives exactly one
disposition, and that disposition is a capacity code. The arithmetic is unchanged
- G-rows are counted inside `n_excluded` so the section 4.5 identities close, and
they are reported decomposed, exactly as the corpus record does
(`n_excluded == Y-rows + G-rows`, 10 + 1,465 = 1,475).

**Execution stage - POST-EXECUTION, and this is a WEAKER amendment than M1.**
Section 10 requires that an amendment logged after the affected decisions were
made say so in those words. It is said here: the 1,465 G-dispositions were
assigned before this contradiction was adjudicated. Nothing about them changes -
no record moves, no count moves, no eligibility is decided - but the reconciliation
is retrospective and the corpus record reports it as such. This is the second
weakness class the predecessor's A8 illustrates, at far lower cost: A8 relaxed an
eligibility criterion retrospectively, whereas M2 reconciles two sections of
procedure that were always meant to agree.

**What M2 does not touch.** No eligibility criterion `N1`-`N6` or `Y1`-`Y9`. No
contribution code, extraction field, taxonomy class or arithmetic identity. No
record's disposition. Frozen text is not edited; this addendum supersedes section
4.2's enumeration in place and the original wording stays legible.
