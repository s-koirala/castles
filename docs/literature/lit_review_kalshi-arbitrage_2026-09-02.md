---
title: "Compiled corpus record — arbitrage, coherence and market making in binary event contracts, with KalshiEX LLC as the venue of interest"
slug: kalshi-arbitrage
date: 2026-09-02
objective: "What does the retrievable published literature state about no-arbitrage and internal-coherence conditions for binary event contracts and measured violations of them, cross-venue and cross-instrument price discrepancies, systematic mispricings including the favorite-longshot bias, market-making and inventory-risk models and the applicability conditions their own authors state for payoffs bounded in [0,1] settling at an endpoint, and the frictions that decide whether a stated discrepancy is executable — and is each item Kalshi-specific or generalized from another venue?"
review_type: scoping
standard_declared: "PRISMA-P 2015 (protocol) + PRISMA-S (adapted, non-clinical) for search reporting. PRISMA 2020 is NOT claimed; the nineteen items this design does not meet are enumerated by number in section 4 of the frozen protocol's section 9.1 and restated in section 13.6 below."
eligibility_inclusion:
  - "I1 the record concerns at least one in-scope instrument per protocol section 2.1 (B-a verifiable-event payoff; B-b finitely-many bounded payoff values; B-c price convertible to an implied probability in [0,1]; B-d traded), OR is a C3 model record admitted under the section 2.2 transfer clause"
  - "I2 the record makes at least one in-scope contribution C1 (states/derives/tests a no-arbitrage or coherence condition), C2 (measures discrepancy, mispricing, bias, efficiency or execution outcomes), C3 (specifies a market-making / inventory-risk / market-scoring-rule / automated-market-maker model with a stated objective and stated applicability conditions), or C4 (analyses microstructure of in-scope or limited-payoff instruments)"
  - "I3 a persistent identifier exists (DOI, arXiv id, RePEc handle, or Handle-System handle)"
  - "I4 the record is retrievable at least to abstract depth"
  - "I5 any language, any year, any document type including preprints and working papers"
eligibility_exclusion:
  - "X1 not an in-scope instrument under 2.1 and not a C3 transfer-clause record"
  - "X2 satisfies 2.1 but makes none of C1-C4"
  - "X3 elicitation without a transferable traded claim (fails B-d)"
  - "X4 pure decision or social-choice theory with no price condition, measurement or market-maker specification"
  - "X5 blockchain/automated-market-maker mechanics where the traded object is a token pair rather than an event claim (fails B-a)"
  - "X6 C3 model record stating neither payoff support nor an applicability condition"
  - "X7 no persistent identifier (fails I3)"
  - "X8 not retrievable to abstract depth (fails I4)"
disposition_codes_added:
  - "NOTE (findings SCOPE-1-4, LITERATURE-1-15, QUANT-1-4). X10 and X11 are NOT eligibility criteria and were previously listed inside `eligibility_exclusion` above, which contradicted section 1. They are disposition codes added during execution by amendments A4 and A5 and restated by amendment A10. The `eligibility_exclusion` list above is now byte-faithful to the frozen protocol's X1-X9."
  - "X10 (amendments A4, A10) KEYWORD-IDENTIFIED CANDIDATE STRATUM, not a criterion failure and not an eligibility determination: title/abstract carry an event-claim token and a contribution token; no record was read, eligibility under I1-I5 was never assessed, and section-5 extraction was not performed"
  - "X11 (amendments A5, A10) KEYWORD-IDENTIFIED MODEL-RECORD STRATUM, not a criterion failure and not an eligibility determination: title/abstract carry a market-making or inventory-model token and no event-claim token; no record was read, neither the section 4.2 stage-1 promotion condition nor any stage-2 assessment was evaluated, so eligibility is UNDECIDED"
registration: "not-registered (PROSPERO accepts only reviews with health-related outcomes and this review has none). The registration event is the provenance commit 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, subject 'docs(protocol): register frozen kalshi-arbitrage search protocol (sha256 99524df02696)', which committed the frozen protocol before any query executed."
protocol_path: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md
protocol_amendments: "Fifteen numbered append-only amendments, all enumerated in section 13.1, all recorded in docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md AND (from A12) transcribed into the frozen protocol's own append-only addendum as protocol section 10 requires: A1 (eCFR content-free HTTP 200 classified as a transient failure for retry purposes), A2 (supplementary RePEc POST arm after the frozen GET endpoint returned an empty result page), A3 (deterministic vocabulary pre-sorter over the forward-citation-only stratum), A4 (disposition code X10 plus publication of Table X-full as a machine-readable artifact), A5 (disposition code X11), A6 (backward citation-chasing arm ka-bc-{n} not executed), A7 (SSRN supplementary site-search arm not run; gap AG-9), A8 (criterion I4 relaxed for 33 metadata-depth included records), A9 (zero-full-text extraction; E8-E13 partial), A10 (the full five-list keyword classifier declared the automation tool of record for all 8,664 non-include dispositions), A11 (X5 word-boundary defect corrected and the pipeline made deterministic), A12 (the amendment mechanism itself: A1-A5 were logged outside the protocol addendum; A1-A12 are now appended to it), A13 (A10 strike of the individual-reading claims completed: five surviving A3 assertions struck by quotation and a supersession banner added at the head of A3), A14 (evidence corrections to A11 — the 6,672 tie-break figure struck and replaced by measured seed sensitivity, the three-record bare-pattern claim corrected to two, the dex/amm corpus statistics labelled by the pattern each is measured under, and the identifier join key narrowed to the 6,923 rows on which it is defined; both declared departures upheld), A15 (A6 assertion 'neither term appears in any of the 35 frozen topical queries' struck as false — `limit order` is carried by ka-crossref-07 — and no demonstrated vocabulary gap is claimed for any known-item miss)."
bibliography: docs/literature/references_kalshi-arbitrage.json
bibliography_sha256: fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164
n_identified: 15924
n_duplicates_removed: 7111
n_screened: 8813
n_excluded: 8664
n_criterion_excluded: 7419
n_capacity_disposition: 1245
n_keyword_candidate_unextracted: 545   # RENAMED 2026-09-02, finding QUANT-2-3, from `n_eligible_not_extracted`. The old name asserted, to any tool reading only this header, the eligibility determination amendment A10 struck: no record in this stratum was read and eligibility under I1-I5 was never assessed. Consumers pinned to the old key must migrate.
n_eligibility_undecided: 700
n_included: 149
extraction_depth: "NO FULL TEXT WAS READ FOR ANY INCLUDED RECORD (amendment A9). 116 of 149 reached abstract depth; 33 reached metadata depth (title, venue, year only). Extraction fields E8-E13 are partially completed at best and no stage-2 assessment was performed for any record. Metadata-depth inclusion runs against frozen criterion I4 and is authorised by amendment A8, not by the frozen text."
screening_verdict_source: "READ-BASED: 150 of 8,813 records (the 149 includes and one hand-verified J6 same-work twin). CLASSIFIER-BASED: 8,663 (the five-list keyword classifier archived at docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py, rules R0-R9, declared the PRISMA 2020 item-8 automation tool of record by amendment A10). No record outside the 149 includes carries a verdict from a screener reading it."
materials_availability:
  - docs/literature/search_logs/kalshi-arbitrage
  - docs/literature/references_kalshi-arbitrage.json
  - docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md
competing_interests: none
ai_assistance: "Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK, research-librarian agent) executed the frozen protocol's queries, built the record universe, performed the single-pass screening, resolved every identifier against the DOI Handle System, and drafted this record. Role per ICMJE 2026 disclosure: code + prose + audit-support. The model is also the declared PRISMA 2020 item-8 automation tool for screening. No result in this record was written from model memory; every metadata field traces to a stored response in the search-log directory."
git_head_at_authoring: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f
pip_freeze_sha256: "51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e"  # archived at logs/reproducibility/env/51760dc9….txt (UNTRACKED LOCATOR). The search itself ran on the Python 3.11 standard library only; executing scripts archived at docs/literature/search_logs/kalshi-arbitrage/ka-universe-script.py, ka-dedup-script.py, ka-partition-script.py, ka-screening-script.py. Finding QUANT-1-7, filled by the lead session.
repro_log_path: "logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json"  # UNTRACKED LOCATOR (logs/ is gitignored); the clone-durable carrier is the Repro-Log-Path / Repro-Log-SHA256 trailer on the provenance commit
repro_log_sha256: "416d4d4891ffd9804f0276e91dc96d5c48460764722191ede10d5fbf476b94ee"
sidecar_path: "artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json"  # UNTRACKED LOCATOR (artifacts/ is gitignored)
sidecar_sha256: "7207fad1866437d188f621e13042ac9a3e95481e46490d3f28949426880e2a67"  # supersedes 96c4134c03f247edc2837e178525a9f215fb8eeb2ab30ca3b9ac53a5e1d5647a. The sidecar carries BOTH the as-first-published and the post-A11 word-boundary disposition tables; round-2 remediation renamed its `X10_eligible_not_extracted` key to `X10_keyword_candidate_unextracted` (finding QUANT-2-3) and re-recorded the protocol-with-addendum digest, so its digest moved. No count in it changed.
dataset_checksums: "n/a (no dataset; no market data was acquired and no exchange API was called). The corpus store digest is the frontmatter bibliography_sha256; the store DOI-resolution record is docs/literature/search_logs/kalshi-arbitrage/ka-store-doicheck.json"
rng_seed: "0 — and, from amendment A11, PYTHONHASHSEED=0 is asserted at entry by ka-dedup-script.py, ka-partition-script.py and ka-screening-script.py. Before A11 the frontmatter declared rng_seed: 0 while pinning nothing that mattered: record-level title and venue tie-breaks resolved on set iteration order, so every Table X-full row identifier depended on the interpreter's hash seed (finding QUANT-1-6)."
model_commit: "n/a (no model artifact; this record fits nothing and estimates nothing)"
---

# Compiled corpus record — arbitrage, coherence and market making in binary event contracts, with KalshiEX LLC as the venue of interest

**Read this first.** This artifact is a **compiled corpus record** produced by a
**registered search**. It is **not a systematic review**, it reports **no
inter-rater agreement statistic**, it reports **no certainty-of-evidence grade**,
and the absence of a risk-of-bias table is a **declared design limit**, not an
oversight (frozen protocol section 9.1). It records what the retrieved
literature *states*; it fits nothing, acquires no market data, calls no exchange
API, computes no price, and states no tradeable rule (ADR-0003).

**The four limitations a reader must carry into every number below.** Added
2026-09-02 under finding **REV-2-2**: the round-1 traceability table recorded
QUANT-1-1 and REV-1-8 as fixed at *"'Read this first' item 2"* and *"items 1-4"*,
and this block contained no numbered items and named neither of the two largest
limitations. The disclosure existed in the frontmatter, sections 5, 6, 13.2 and
13.6 and gap G-10, so nothing was lost — but the one front-of-document block a
reader is told to read first did not carry it. It does now.

1. **98.3% of the dispositions in this flow are keyword-classifier outputs.** 150
   of 8,813 records carry a verdict from anyone reading them (the 149 includes and
   one hand-verified same-work twin); the other **8,663** were verdicted by the
   deterministic five-list keyword classifier archived at
   [ka-screening-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py),
   which amendment **A10** declares the PRISMA 2020 item-8 automation tool of
   record. A disposition code in this artifact states which tokens a record's title
   and retrieved abstract contain, and nothing else.
2. **1,245 records ended screening unresolved** — 545 X10 and 700 X11 — and they
   are **capacity gaps, not criterion failures**. No eligibility determination was
   made for any of them. They are counted inside `n_excluded` only so the frozen
   arithmetic identities close.
3. **No full text was read for any included record** (amendment **A9**). Every
   claim in section 8 is a transcription of an abstract or of metadata.
4. **33 of the 149 included records were retrieved to metadata depth only** —
   title, venue and year. On the frozen text they fail criterion I4 and belong
   under X8; their inclusion is authorised by amendment **A8**, not by the
   protocol. A reader who declines A8 should read this corpus as **116 included
   records plus 33 X8 exclusions**.

**Provenance.** Frozen protocol
[docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md](docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md),
SHA-256 `99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`,
registered in commit `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`. Every query in
this record executed on **2026-09-02**, after that commit.

## 1. Objective and eligibility

The review question, the objectives O1-O8 and their prioritization (primary:
**O1** conditions, **O4** models, **O5** frictions), the strand list S1-S7, and
the eligibility criteria are fixed in the frozen protocol sections 1 and 2 and
were not modified during execution. They are restated in this record's
frontmatter under `eligibility_inclusion` / `eligibility_exclusion` and are cited
by identifier throughout.

**Grouping rule for synthesis (PRISMA 2020 item 13a).** Records are grouped by
the protocol's frozen strand list — S1 no-arbitrage and coherence; S2 cross-venue
and cross-instrument price discrepancies; S3 favorite-longshot bias and other
systematic mispricings; S4 market making, inventory risk, market scoring rules
and automated market makers; S5 transaction costs, fees, collateral, capital
lockup and executability; S6 microstructure of binary and limited-payoff
instruments — and, **within each strand, by the section 8 separation rule**:
Kalshi-specific material first, generalized material second, with the carrying
assumption written on the same line as every generalized claim.

**Correction to that rule, finding LITERATURE-1-11.** The grouping is **not**
mechanical from extraction field E3. For **10** of the 149 records the strand
under which the claim line is synthesized in section 8 is not among the strands
E3 assigns in the section 7 table. **E3, as recorded in the section 7 table,
remains the authoritative record of the field**; the section 8 placement is the
reconstruction. The 10 are marked in the section 7 `strand(s)` column with a
`[synth Sn]` suffix naming the block their claim line actually sits in, so both
values are visible on the same row and neither is silently overwritten. They are:
Flepp (E3 S4+S6, synthesized under S5), Gill 2026b (S5 / S6), Glosten & Milgrom
(S6 / S4), Goel (S6 / S2), Krause 2026c (S6 / S3), Krause 2026d (S6 / S3), Kyle
(S6 / S4), Mohanty & Krishnamachari (S6 / S2), Polson (S6 / S1), Saliou et al.
(S5 / S6). A reader counting strand depth from section 8 alone will therefore
over-count S1, S2, S3 and S4 and under-count S5 and S6.

**Two disposition codes were added during execution** (amendments A4 and A5) and
are **not** eligibility criteria. **X10 marks a keyword-identified candidate
stratum whose eligibility was never assessed**; X11 marks a keyword-identified
model-record stratum whose eligibility is **undecided** because neither the
section 4.2 stage-1 promotion condition nor any stage-2 assessment was evaluated.
Both are capacity gaps and both are reported as such in sections 6 and 13.
**Corrected 2026-09-02 under finding QUANT-2-3**: this sentence previously read
"X10 marks records that **passed** eligibility and were not extracted", two
sentences after the paragraph stating that the two codes are not eligibility
criteria — the exact claim amendment A10 withdrew.

## 2. Information sources and methods

<!-- prisma-s-1 -->
PRISMA-S 1/2/13. One row per protocol query id in the S1-S6 literature stream,
including zero-yield queries and every retry. The S7 documentation stream is
counted separately in section 9 and is **not** part of these counts (frozen
protocol section 2.7 constraint 2). `n_records` is the number of records the
query contributed to the record universe; `platform_total_hits` is the total the
platform itself reported, preserved even where it exceeds the retrieval cap.

| source | platform | date_searched | query_id | n_records | platform_total_hits | http | note |
|---|---|---|---|---|---|---|---|
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-01 | 15 | 15 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-02 | 50 | 198 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-03 | 44 | 44 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-04 | 2 | 2 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-05 | 12 | 12 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-arxiv-06 | 50 | 61 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-01 | 20 | 1486628 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-02 | 20 | 2329830 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-03 | 20 | 2067828 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-04 | 20 | 1606625 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-05 | 20 | 381712 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-06 | 20 | 1952274 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-07 | 20 | 79887 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-08 | 20 | 478035 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-09 | 20 | 680973 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-10 | 20 | 2375993 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-11 | 20 | 673302 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-12 | 20 | 4458996 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-13 | 20 | 10991 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-14 | 20 | 1093 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-crossref-15 | 20 | 3217 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a1 | 153 | 153 | 200 | cursor/offset paged, 1 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a1-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a2 | 37 | 37 | 200 | cursor/offset paged, 1 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a2-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a3 | 321 | 321 | 200 | cursor/offset paged, 2 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a3-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a4 | 499 | 499 | 200 | cursor/offset paged, 3 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a4-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a5 | 382 | 382 | 200 | cursor/offset paged, 2 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a5-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a6 | 6463 | 6463 | 200 | cursor/offset paged, 33 pages |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-fc-oa-a6-resolve | 0 | 1 | 200 | anchor DOI -> OpenAlex work-id resolution step; contributes no record to the universe (the citing set does) |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a1 | 156 | not reported | 200 | cursor/offset paged, 1 pages |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a2 | 39 | not reported | 200 | cursor/offset paged, 1 pages |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a3 | 0 | not reported | **404** | **AG-4** — corrected 2026-09-02 under findings REV-1-11 / LITERATURE-1-8; the row previously read `200` with a `cursor/offset paged, 1 pages` note, contradicting `prisma-s-5` and AG-4. The stored log `ka-fc-s2-a3-p001.json` records `"http_status": 404`, `"retry_attempts": 6`, `"raw": {"error": "Paper with id DOI:10.1086/655844 not found"}`. No page was retrieved, so no paging note applies |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a4 | 535 | not reported | 200 | cursor/offset paged, 1 pages |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a5 | 426 | not reported | 200 | cursor/offset paged, 1 pages |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a6 | 6147 | not reported | 200 | cursor/offset paged, 7 pages |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki01 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki02 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki03 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki04 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki05 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki06 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki07 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki08 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki09 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki10 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki11 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki12 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki13 | 1 | 1 | 200 |  |
| arXiv | arXiv API (export.arxiv.org) | 2026-09-02 | ka-ki-ki14 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki15 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki16 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki17 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki18 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki19 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki20 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki21 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki22 | 1 | 1 | 200 |  |
| Crossref | Crossref REST API (api.crossref.org) | 2026-09-02 | ka-ki-ki23 | 1 | 1 | 200 |  |
| NBER | NBER listing API (www.nber.org/api/v1) | 2026-09-02 | ka-nber-01 | 50 | not reported | 200 |  |
| NBER | NBER listing API (www.nber.org/api/v1) | 2026-09-02 | ka-nber-02 | 50 | not reported | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-01 | 25 | 794 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-02 | 25 | 481 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-03 | 25 | 2060 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-04 | 25 | 99 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-05 | 25 | 64 | 200 |  |
| OpenAlex | OpenAlex REST API (api.openalex.org) | 2026-09-02 | ka-openalex-06 | 25 | 659 | 200 |  |
| repec-ideas (htsearch2, HTTP POST) | repec-ideas (htsearch2, HTTP POST) | 2026-09-02 | ka-repec-01-supp | 10 | 830 | 200 | platform default result page (no cap chosen by the executing agent) |
| RePEc / IDEAS | IDEAS htsearch (ideas.repec.org/cgi-bin/htsearch) | 2026-09-02 | ka-repec-01 | 0 | not reported | 200 |  |
| repec-ideas (htsearch2, HTTP POST) | repec-ideas (htsearch2, HTTP POST) | 2026-09-02 | ka-repec-02-supp | 10 | 121 | 200 | platform default result page (no cap chosen by the executing agent) |
| RePEc / IDEAS | IDEAS htsearch (ideas.repec.org/cgi-bin/htsearch) | 2026-09-02 | ka-repec-02 | 0 | not reported | 200 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-01-b | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-01-c | 0 | not reported | 429 | protocol section 3.1 retry-until-200 convention; URL byte-identical to the frozen query |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-01 | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-02-b | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-02-c | 0 | not reported | 429 | protocol section 3.1 retry-until-200 convention; URL byte-identical to the frozen query |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-02 | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-03-b | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-03-c | 0 | not reported | 429 | protocol section 3.1 retry-until-200 convention; URL byte-identical to the frozen query |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-03 | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-04-b | 0 | not reported | 429 |  |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-04-c | 0 | not reported | 429 | protocol section 3.1 retry-until-200 convention; URL byte-identical to the frozen query |
| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-s2-04 | 0 | not reported | 429 |  |

**Whole-table re-check, same finding.** Every row's `http` value was re-verified
against its own stored `ka-*.json` at remediation time by reading `http_status`
out of each log and comparing it to the cell. `ka-fc-s2-a3` was the only
disagreement in the table; every other row matches its log. The forward-citation
arms are logged per page under `-pNNN` ids and were checked page by page.

<!-- prisma-s-2 -->
No multi-database platform search was used. Each source above was searched
through its own API or interface; no host platform (Ovid, EBSCOhost,
Web of Science) covered more than one database in a single query.

<!-- prisma-s-3 -->
No study registries were searched. PROSPERO, ClinicalTrials.gov, ICTRP and OSF
index health-outcome and trial protocols; this review has no health outcome and
no trial. The absence is affirmative, not an omission.

<!-- prisma-s-4 -->
Two online sources were searched or browsed outside the bibliographic databases,
both in the S7 documentation stream and both reported in section 9: the CFTC
public record (`cftc.gov`) and the Federal Register API. The Kalshi filer-published
rulebook (`kalshi.com/regulatory/rulebook`) was attempted three times and refused
every attempt (access gap AG-1, section 13.3). No other online source was
browsed, and no search-engine or hand-browse arm was run.

**The SSRN supplementary arm was not run, and its absence is recorded here rather
than passed over (finding LITERATURE-1-7, amendment A7).** Frozen protocol section
3.1 carries an "SSRN caveat, declared in advance": SSRN has no public search API,
so if the executing session has browser access it MAY run the section 3.2
vocabulary through SSRN's own site search as a supplementary arm, "if not, the
absence is recorded as a minor recall verification gap in the corpus record, not
passed over in silence." The arm was not run and the required gap entry was
**omitted from the record as first published** — a silent deviation, which
protocol section 10 classes as a conduct violation. It is now recorded as access
gap **AG-9** (section 13.3) and as amendment **A7**. The consequence is not minor
for this corpus: **31 of the 149 included records carry `10.2139/ssrn.*` DOIs, and
15 of the 19 Kalshi-specific records do**, and SSRN was reached only through two
Crossref container-restricted queries capped at `rows=20` (`ka-crossref-13`,
`ka-crossref-14`) against platform-reported totals of 10,991 and 1,093.

**Derivation of the 15, stated so the number is re-checkable (finding REV-2-6).**
It is the count of rows in the section-7 table carrying **both** `E4/E15` = `K`
**and** a `10.2139/ssrn.*` identifier: `ssrn.6615739`, `ssrn.5502658`,
`ssrn.6442939`, `ssrn.6858200`, `ssrn.7117919`, `ssrn.7119120`, `ssrn.7021660`,
`ssrn.7110758`, `ssrn.7087538`, `ssrn.6748186`, `ssrn.6964226`, `ssrn.6704139`,
`ssrn.7170178`, `ssrn.7254820`, `ssrn.7364100`. The record published **13** at
four sites until this remediation (`prisma-s-4`, G-9, AG-9, amendment A7); the
marginals it was checked against — 31 SSRN rows, 19 `K` rows — are both correct, so
the error was confined to the intersection, and it understated the limitation in
exactly the direction this record elsewhere calls "a reporting defect in the
direction that flatters the corpus".

<!-- prisma-s-5 -->
Citation searching was performed in **both** directions.
**Forward (citing references):** the frozen protocol's six anchors, one per
strand S1-S6, were resolved and their complete citing sets retrieved with no cap
and no citation-count floor, on two independent tools — OpenAlex
(`filter=cites:` with cursor paging) and the Semantic Scholar Graph API
(`/citations` with offset paging). Retrieval was complete against the count each
platform reported: OpenAlex returned 153/153, 37/37, 321/321, 499/499, 382/382
and 6,463/6,463 for anchors A1-A6; the Semantic Scholar arm returned 156, 39,
535, 426 and 6,147 for A1, A2, A4, A5 and A6 and **HTTP 404 for A3**
(`10.1086/655844` is not indexed by that service), a per-anchor gap recorded in
section 13.3.
**Backward (cited references):** the protocol's `ka-bc-{n}` backward
citation-chasing arm was **not executed**. Section 3.3 bounds it to the reference
lists of included C1 and C3 records, which requires full texts; no full text was
retrieved in this execution (section 13.2), so the arm had no input. This is a
recall gap, recorded in section 13.3 as G-7, and — **corrected here under finding
SCOPE-1-1** — as numbered append-only protocol amendment **A6**. The
non-execution of a protocol-mandated search arm is a deviation from the frozen
text, and the frozen protocol's section 10 requires every deviation to take the
form of a numbered amendment. Reporting it only as a narrative gap, as this
record did when first published, did not meet that requirement. The arm is
**not** executed retroactively; A6 records the non-execution, its cause and its
recall consequence.

<!-- prisma-s-6 -->
No contacts were made with authors, experts, manufacturers, exchanges or
regulators. The protocol provides for none, and contacting the venue of interest
would have crossed the dispatch boundary against acquiring venue data.

<!-- prisma-s-7 -->
Two further search methods were used. **(a) The known-item arm** (frozen protocol
section 3.4): each of the 23 identifier-verified known items was fetched directly
and force-entered into the record universe so it could not be missed, then
screened against section 2 like any other record. **(b) The supplementary RePEc
arm** added by amendment A2 after the frozen GET endpoint returned a structurally
empty results page. No other method was used; in particular no grey-literature
repository, no dissertation database and no trial-register search was run.

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S 8 — copied and pasted exactly as run, one fence per `query_id`. Nothing
below was retyped or reconstructed: each string was written to its log file in
the same write as the HTTP status, the platform-reported total and the retrieved
count, at execution time. Forward-citation arms are shown at their first page;
the paging parameter (`cursor` for OpenAlex, `offset` for Semantic Scholar)
varies across the pages named in the `note` column of the table above, and every
page is stored under its own `-pNNN` log id.

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
```text ka-fc-oa-a1
https://api.openalex.org/works?filter=cites:W2167866999&per-page=200&cursor=*   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-oa-a1-resolve
https://api.openalex.org/works/https://doi.org/10.1287/mnsc.1040.0191
```
```text ka-fc-oa-a2
https://api.openalex.org/works?filter=cites:W3125514734&per-page=200&cursor=*   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-oa-a2-resolve
https://api.openalex.org/works/https://doi.org/10.1111/ecca.12009
```
```text ka-fc-oa-a3
https://api.openalex.org/works?filter=cites:W3123039092&per-page=200&cursor=*   [page 1 of 2; paging parameter varies per the protocol]
```
```text ka-fc-oa-a3-resolve
https://api.openalex.org/works/https://doi.org/10.1086/655844
```
```text ka-fc-oa-a4
https://api.openalex.org/works?filter=cites:W2120832833&per-page=200&cursor=*   [page 1 of 3; paging parameter varies per the protocol]
```
```text ka-fc-oa-a4-resolve
https://api.openalex.org/works/https://doi.org/10.1023/A:1022058209073
```
```text ka-fc-oa-a5
https://api.openalex.org/works?filter=cites:W3121231812&per-page=200&cursor=*   [page 1 of 2; paging parameter varies per the protocol]
```
```text ka-fc-oa-a5-resolve
https://api.openalex.org/works/https://doi.org/10.1111/j.1468-0297.2004.00207.x
```
```text ka-fc-oa-a6
https://api.openalex.org/works?filter=cites:W1985808284&per-page=200&cursor=*   [page 1 of 33; paging parameter varies per the protocol]
```
```text ka-fc-oa-a6-resolve
https://api.openalex.org/works/https://doi.org/10.1016/0304-405X(85)90044-3
```
```text ka-fc-s2-a1
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1287/mnsc.1040.0191/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-s2-a2
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/ecca.12009/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-s2-a3
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1086/655844/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-s2-a4
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1023/A:1022058209073/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-s2-a5
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/j.1468-0297.2004.00207.x/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 1; paging parameter varies per the protocol]
```
```text ka-fc-s2-a6
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/0304-405X(85)90044-3/citations?fields=title,year,venue,externalIds,abstract,citationCount&limit=1000&offset=0   [page 1 of 7; paging parameter varies per the protocol]
```
```text ka-ki-ki01
https://api.crossref.org/works/10.1287%2Fmnsc.1040.0191
```
```text ka-ki-ki02
https://api.crossref.org/works/10.1016%2Fj.econlet.2006.01.004
```
```text ka-ki-ki03
https://api.crossref.org/works/10.3386%2Fw12200
```
```text ka-ki-ki04
https://api.crossref.org/works/10.1257%2F0895330041371321
```
```text ka-ki-ki05
https://api.crossref.org/works/10.1016%2FS1574-0722%2807%2900080-7
```
```text ka-ki-ki06
https://api.crossref.org/works/10.1257%2F0895330041371277
```
```text ka-ki-ki07
https://api.crossref.org/works/10.1111%2Fecca.12009
```
```text ka-ki-ki08
https://api.crossref.org/works/10.1016%2Fj.ijforecast.2018.07.008
```
```text ka-ki-ki09
https://api.crossref.org/works/10.1257%2Fjep.2.2.161
```
```text ka-ki-ki10
https://api.crossref.org/works/10.1086%2F655844
```
```text ka-ki-ki11
https://api.crossref.org/works/10.1257%2Fmic.2.1.58
```
```text ka-ki-ki12
https://api.crossref.org/works/10.1023%2FA%3A1022058209073
```
```text ka-ki-ki13
https://api.crossref.org/works/10.5750%2Fjpm.v1i1.417
```
```text ka-ki-ki14
https://export.arxiv.org/api/query?id_list=1206.5252
```
```text ka-ki-ki15
https://api.crossref.org/works/10.1145%2F2465769.2465777
```
```text ka-ki-ki16
https://api.crossref.org/works/10.1145%2F2509413.2509414
```
```text ka-ki-ki17
https://api.crossref.org/works/10.1145%2F2940716.2940767
```
```text ka-ki-ki18
https://api.crossref.org/works/10.1016%2F0304-405X%2885%2990044-3
```
```text ka-ki-ki19
https://api.crossref.org/works/10.2307%2F1913210
```
```text ka-ki-ki20
https://api.crossref.org/works/10.1016%2F0304-405X%2881%2990020-9
```
```text ka-ki-ki21
https://api.crossref.org/works/10.1080%2F14697680701381228
```
```text ka-ki-ki22
https://api.crossref.org/works/10.1007%2Fs11579-012-0087-0
```
```text ka-ki-ki23
https://api.crossref.org/works/10.1111%2Fj.1468-0297.2004.00207.x
```
```text ka-nber-01
https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search?page=1&perPage=50&q=prediction%20markets
```
```text ka-nber-02
https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search?page=1&perPage=50&q=betting%20market%20arbitrage
```
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
```text ka-repec-01-supp
POST https://ideas.repec.org/cgi-bin/htsearch2  body: q=prediction+market+arbitrage
```
```text ka-repec-01
https://ideas.repec.org/cgi-bin/htsearch?q=prediction+market+arbitrage
```
```text ka-repec-02-supp
POST https://ideas.repec.org/cgi-bin/htsearch2  body: q=favorite+longshot+bias
```
```text ka-repec-02
https://ideas.repec.org/cgi-bin/htsearch?q=favorite+longshot+bias
```
```text ka-s2-01-b
https://api.semanticscholar.org/graph/v1/paper/search?query=prediction%20market%20arbitrage%20no-arbitrage%20bounds&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-01-c
https://api.semanticscholar.org/graph/v1/paper/search?query=prediction%20market%20arbitrage%20no-arbitrage%20bounds&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-01
https://api.semanticscholar.org/graph/v1/paper/search?query=prediction%20market%20arbitrage%20no-arbitrage%20bounds&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-02-b
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20making%20inventory%20risk%20binary%20event%20contracts&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-02-c
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20making%20inventory%20risk%20binary%20event%20contracts&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-02
https://api.semanticscholar.org/graph/v1/paper/search?query=market%20making%20inventory%20risk%20binary%20event%20contracts&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-03-b
https://api.semanticscholar.org/graph/v1/paper/search?query=favorite%20longshot%20bias%20prediction%20markets&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-03-c
https://api.semanticscholar.org/graph/v1/paper/search?query=favorite%20longshot%20bias%20prediction%20markets&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-03
https://api.semanticscholar.org/graph/v1/paper/search?query=favorite%20longshot%20bias%20prediction%20markets&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-04-b
https://api.semanticscholar.org/graph/v1/paper/search?query=event%20contract%20exchange%20prediction%20market%20microstructure&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-04-c
https://api.semanticscholar.org/graph/v1/paper/search?query=event%20contract%20exchange%20prediction%20market%20microstructure&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```
```text ka-s2-04
https://api.semanticscholar.org/graph/v1/paper/search?query=event%20contract%20exchange%20prediction%20market%20microstructure&fields=title,year,venue,externalIds,abstract,citationCount&limit=50
```

<!-- prisma-s-9 -->
**No date limit, no language limit and no document-type limit was applied
anywhere in the topical strategy.** This is the affirmative statement PRISMA-S 9
requires, and each absence is derived rather than conventional (frozen protocol
section 2.5): a lower date bound would amputate the foundational S1, S3 and S4
statements, which are verified from 1981 onward; conditions, measured quantities
and model specifications are extractable from formulae and tables independently
of prose language; and preprints and working papers are admitted tier-blind with
the tier travelling with the claim, because in this literature the working-paper
stream carries results years ahead of journal publication and the venue of
interest is recent. The only subject restrictions anywhere are the arXiv category
filters `cat:q-fin*` on `ka-arxiv-03` and `ka-arxiv-05`, declared `CONVENTION` in
the protocol and applied only where the bare phrase returns predominantly
out-of-domain physics and mathematics.

**The offsetting claim, as designed and as executed (findings REV-1-12, REV-2-3).**
As **designed**, the unrestricted forms of both narrowed phrases were carried by
four queries: `ka-crossref-07` and `ka-openalex-06` and `ka-s2-02` for the
`ka-arxiv-03` vocabulary (*market making* / *inventory*), and `ka-crossref-11` for
the `ka-arxiv-05` vocabulary (*binary option*). **As executed, three of the four
carried it and one returned nothing.**

| offsetting query | narrowed query it offsets | status | records / platform total |
|---|---|---|---|
| `ka-crossref-07` | `ka-arxiv-03` | executed, HTTP 200 | 20 / 79,887 |
| `ka-openalex-06` | `ka-arxiv-03` | executed, HTTP 200 | 25 / 659 |
| `ka-s2-02` | `ka-arxiv-03` | **HTTP 429 on all three attempts; zero records (AG-3)** | 0 |
| `ka-crossref-11` | `ka-arxiv-05` | executed, HTTP 200 | 20 / 673,302 |

**Therefore the conclusion "no vocabulary is category-gated out of the strategy as
a whole" is withdrawn as an unqualified statement and replaced by what the
execution supports.** No token was gated out entirely: both narrowed phrases were
also asked for without a category filter, on queries that ran and returned records.
What the execution lost is **redundancy** — the offset was designed to rest on four
queries across three platforms and rests on three across two, each capped at 20 or
25 records against platform totals of 659 to 673,302, so the surviving offset is
itself depth-truncated (section 13.5). The Semantic Scholar arm, which was the only
one of the four whose form pairs *market making inventory risk* with *binary event
contracts*, contributed nothing. See section 4 and gap G-8.

<!-- prisma-s-10 -->
No published search filter was used. No validated topic or study-design filter
exists for event-contract or market-microstructure literature, and none was
adapted from a clinical filter collection.

<!-- prisma-s-11 -->
No search strategy was adapted or reused from a prior review. The vocabulary was
built from the verified titles and venues of the 23 known-item records (frozen
protocol section 3.2), not from a previously published strategy and not from
model recall. The retrieval caps, the retry suffixes, the log-filename prefix and
the arXiv-category narrowing are house conventions carried from
`docs/methodology/protocol_explosive-regime-review_2026-08-24.md` and are labelled
`CONVENTION` in the frozen protocol's section 11 register.

<!-- prisma-s-12 -->
No update is planned and no alert was set. This is a single-execution search; a
re-run would be a new registered search with its own protocol and its own
provenance commit.

<!-- prisma-s-13 -->
Date of last search, every strategy and every arm: **2026-09-02**. This agrees
with the `date_searched` column of the table in section 2 for all 86 rows and
with the `date_executed` field of every stored log.

## 4. Peer review of the strategy

<!-- prisma-s-14 -->
**The search strategy was NOT peer reviewed.** No second human searcher and no
information specialist exists in this project, so the PRESS 2015 review step
([McGowan et al. 2016](https://doi.org/10.1016/j.jclinepi.2016.01.021)) was not
performed. This is a deviation and it is recorded rather than papered over. The
frozen protocol's four declared mitigations were carried out and are reported
here with their outcomes: (i) the vocabulary was taken from verified known-item
metadata; (ii) the forward-citation arm ran uncapped on two independent tools and
is vocabulary-independent by construction; (iii) the known-item arm functioned as
the PRESS known-item recall check and returned **16 of 23 items retrieved
independently of their own fetch**, with the seven misses itemized and
interpreted in section 13.4; (iv) this record states, in these words, that
**recall is not demonstrated** — and the list of reasons, **corrected under
finding REV-1-12**, opens with the largest of them rather than omitting it:
**(a)** all four Semantic Scholar topical queries and all eight of their retries
returned HTTP 429, so **one of the four protocol-named bibliographic databases
contributed zero records to the topical strategy** (AG-3, section 13.3); **(b)**
the strategy was not peer reviewed; **(c)** one of the six forward-citation
anchors could not be resolved on the Semantic Scholar arm (AG-4, HTTP 404);
**(d)** the backward citation-chasing arm did not execute at all (amendment A6);
**(e)** the SSRN supplementary arm was not run and its declared-in-advance gap
entry was omitted from the record as first published (AG-9, amendment A7).

**What (a) costs the strategy, stated against this record's own argument.** The
`prisma-s-9` paragraph in section 3 argued that no vocabulary is category-gated out
of the strategy, because the arXiv `cat:q-fin*` narrowing on `ka-arxiv-03` and
`ka-arxiv-05` is offset by four unrestricted forms — including the `ka-s2-02`
"market making inventory risk binary event contracts" pairing. All four Semantic
Scholar topical queries returned zero.

**Restated precisely, correcting an over-withdrawal (finding REV-2-3).** The
round-1 wording of this paragraph said "in execution, therefore, the narrowing is
**not** offset". That is too strong, and it contradicted the `prisma-s-9` paragraph
it claimed to have withdrawn — which was in fact left unedited. Checked against the
section-2 table: **three of the four offsetting queries executed with HTTP 200 and
returned records** (`ka-crossref-07` 20/79,887 and `ka-openalex-06` 25/659 for the
`ka-arxiv-03` vocabulary; `ka-crossref-11` 20/673,302 for the `ka-arxiv-05`
vocabulary), and one, `ka-s2-02`, returned zero. **What is withdrawn is the
unqualified form of the claim, not the claim that the phrases were asked for
unrestricted.** What the execution lost is redundancy and one platform: the offset
now rests on three capped queries across two platforms instead of four across
three, and the one query whose form paired the market-making vocabulary with the
binary-event-contract vocabulary is the one that returned nothing. The full
statement, with the per-query table, is at `prisma-s-9`; the gap is G-8.

## 5. Managing records

<!-- prisma-s-15 -->
Per-source and per-query record counts are the `n_records` column of the table in
section 2; the arithmetic identities the frozen protocol section 4.3 requires are:

| identity | left | right | holds |
|---|---|---|---|
| `sum(n_records per query) == n_identified` | 15,924 | 15,924 | yes |
| `n_identified - n_duplicates_removed == n_screened` | 15,924 - 7,111 = 8,813 | 8,813 | yes |
| `n_screened - n_excluded == n_included` | 8,813 - 8,664 = 149 | 149 | yes |
| `len(bibliography store) == n_included` | 149 | 149 | yes |

**The `n_excluded` row split, finding REV-1-8.** The identity above closes on
8,664, and the frozen protocol's section 4.3 arithmetic is unchanged. But 8,664
is not 8,664 criterion failures, and publishing it as one number lets a consumer
of this table read 149/8,813 as a completed screen. The split:

| component of `n_excluded` | n | what it is |
|---|---|---|
| criterion failures (X1, X2, X3, X5, X7, X9) | 7,419 | a section-2 criterion was cited against the record — by the keyword classifier, not by a reader |
| X10, keyword-identified candidate stratum | 545 | eligible-or-not is **unknown**; extraction not performed |
| X11, keyword-identified model-record stratum | 700 | eligibility **UNDECIDED**; neither stage assessed |
| **capacity dispositions, subtotal** | **1,245** | **not criterion failures** |
| **`n_excluded`, total** | **8,664** | identity closes: 8,813 − 8,664 = 149 |

The same three counts are carried in the frontmatter as `n_criterion_excluded`,
`n_keyword_candidate_unextracted` and `n_eligibility_undecided`, so a tool reading
only the machine-readable header sees them too (findings REV-1-8,
LITERATURE-1-15). The second key was named `n_eligible_not_extracted` until
2026-09-02; it is **renamed under finding QUANT-2-3** because the old name
asserted in the header the eligibility determination amendment A10 struck from the
body. The sidecar key `X10_eligible_not_extracted` is renamed to
`X10_keyword_candidate_unextracted` for the same reason.

No source is absent from that table: the S1-S6 stream is exactly the 86 rows
listed, and the six S7 documentation queries are counted separately in section 9
and never enter these identities.

**Flow, stated as a sequence.** 15,924 records were retrieved across 86 executed
queries on six platforms and four search arms (topical, forward-citation,
known-item, supplementary). Deduplication collapsed them to 8,813 distinct works,
removing 7,111 duplicate retrievals; 5,555 merge groups contained more than one
raw record, which is what an uncapped two-tool forward-citation design produces.
All 8,813 received a disposition. **How, corrected under findings REV-1-5 and
QUANT-1-1:** the previous wording of this sentence — "All 8,813 were screened at
title level (and at abstract level where an abstract had been retrieved)" —
asserted that every record was read. It was not. **150 records carry a read-based
verdict** (the 149 includes, read at abstract or metadata depth and extracted,
plus one hand-verified J6 same-work twin excluded X9). **The other 8,663 were verdicted by the deterministic five-list keyword classifier archived at
[ka-screening-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py)**,
rules R0-R9. Amendment A10 declares that classifier the PRISMA 2020 item-8
automation tool of record for all of them.

**The 8,663 by stratum, net of the 150 (finding LITERATURE-2-7).** The three
strata partition the 8,813 works, so the classifier subtotals must be stated **net
of the read-based records that fall inside them** or the enumeration re-includes
the 150 the sentence has just carved out — which is what it did until this
remediation, summing to 8,813:

| amendment-A3 stratum | records | read-based | **classifier-verdicted** |
|---|---|---|---|
| DEFAULT-X1 (rule R2) | 5,249 | 0 | **5,249** |
| REVIEW | 2,905 | 62 | **2,843** |
| topical / known-item / supplementary | 659 | 88 | **571** |
| **total** | **8,813** | **150** | **8,663** |

The split is re-derivable from the committed pipeline: the A3 partition is
`ka-partition-script.py` over the `arms == ['forward-citation']` stratum, and the
read-based set is the 149 store DOIs plus the one hand-verified X9 twin. The
2,843 + 571 = **3,414** figure is the same one amendment A10 reports as the
dispositions that were presented as individual screening verdicts and were not.

8,664 were excluded, of which **1,245 are capacity dispositions, not criterion
failures** (545 X10 + 700 X11) — this is the single most important number in the
flow and section 13.2 states its consequence. 149 records were included and
extracted. The 1,245 figure is 57 higher than the 1,188 first published, because
amendment A11 corrected an unanchored-substring defect in the X5 rule and moved
57 records out of a criterion failure into the undecided stratum (section 6).

<!-- prisma-s-16 -->
**Deduplication process.** Identifier-level exact match on DOI first
(case-normalized), then arXiv id (version suffix stripped), then RePEc handle,
then OpenAlex and Semantic Scholar internal ids; then a same-work merge on a
case- and punctuation-insensitive normalized title, applied transitively via
union-find over all identifier and title keys. This is the frozen protocol
section 4.1 rule, including its `CONVENTION`-labelled title clause. J6 was applied
to every included record carrying more than one DOI: the journal or registered
version is retained and the working-paper, preprint or proceedings twin is
recorded; 24 such twin sets are itemized in
[ka-dedup-ledger.json](docs/literature/search_logs/kalshi-arbitrage/ka-dedup-ledger.json).
One further twin was found by hand at extraction time and could not have been
caught by the title rule — `10.2139/ssrn.294306` (2001 working paper) is the same
work as `10.1111/j.1354-7798.2005.00274.x` (European Financial Management 2005),
whose titles differ by a trailing word; the journal version is retained and the
twin is the single X9 row in the exclusion record.

**Deduplication software.** Performed by the executing agent in Python 3.11 using
the standard library only; **no reference-manager product was used**. The script
is archived verbatim at
[ka-dedup-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py)
and the universe builder it consumes at
[ka-universe-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-universe-script.py),
both re-runnable against the stored `ka-*.json` logs.

**Determinism, corrected under finding QUANT-1-6, amendment A11.** As executed and
first published, the pipeline was **not** deterministic and the "re-runnable
byte-for-byte" claim this record made was false at the row level. Record-level
title and venue selection inside a merge group sorted a **set** on a single key
(`len`), so ties were broken by set iteration order, which depends on
`PYTHONHASHSEED`. That changed `works.sort`'s key and hence every `uid`, and
`uid` is the row identifier of the published Table X-full. Measured: a
`PYTHONHASHSEED=0` rebuild from the stored logs reproduces every aggregate exactly
(15,924 raw / 8,813 works / 7,111 duplicates, and all nine screening codes).

**The magnitude of the row-id drift is stated but NOT verifiable, and that is now
said in place of reporting it as a measurement (findings QUANT-2-6,
REPRODUCIBILITY-2-5, amendment A14).** Round 1 published "agrees with the published
file on only **2,630 of 8,813** `uid`-to-record mappings; **6,183 published row ids
are not reproducible**". **Nobody can check those two numbers.** The
pre-remediation verdicts file was **overwritten in place** by the round-1
re-emission and had never been committed, so it is not in git history either; the
file the comparison was made against no longer exists. The two figures are
therefore carried as an **unverifiable assertion of the round-1 remediation
session**, not as a measurement, and a reader must treat them that way. What **is**
independently established, and re-derivable from the committed pipeline: the
unseeded pipeline is non-deterministic at the row level (the round-1 auditor
measured 4,415 of 8,813 `uid`s differing between two unseeded local runs and 0
between two seeded runs), and the seeded pipeline is now stable by construction —
the seed guard refuses to run unseeded, and `ka-counterfactuals.py` reproduces the
identical `works.json` at four hash seeds.

Three fixes, all in the archived scripts:
(i) the title and venue tie-breaks are now total, `key=(len(v), v)`;
(ii) `PYTHONHASHSEED=0` is asserted at entry by `ka-dedup-script.py`,
`ka-partition-script.py` and `ka-screening-script.py`, which now refuse to run
unseeded rather than emitting an irreproducible map; and
(iii) the two inputs that were unarchived scratch files at first execution — the
amendment-A3 partition and the included-record set — are now derived from
committed artefacts by
[ka-partition-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-partition-script.py),
so the pipeline runs end to end from the stored logs.
**Not fixed, and stated rather than hidden:** the abstract tie-break was left
exactly as executed. It is a list comprehension over the raw-record order and
Python's sort is stable, so it was already seed-independent — but converting it to
a set would have changed which abstract a tied work carries, hence its token
matches, hence its screening code. That would have been a re-screen disguised as a
determinism fix, and it is not done here. **The evidence offered for that refusal
was itself wrong and is replaced (findings QUANT-2-2, REPRODUCIBILITY-2-3,
amendment A14).** Amendment A11 claimed the conversion made the classifier miss the
published table, `X1` 6,672 instead of 6,707. **It does not.** Re-run from the
committed logs at `PYTHONHASHSEED` 0, 1, 7 and 12345 in both matching modes —
sixteen runs — the aggregate table is identical in every one, `X1` = 6,707
included. The verifiable ground for the refusal, measured over the same runs, is
**seed sensitivity**: the shipped **list** form retains an identical abstract for
all 8,813 works at every seed (**0** differences at every seed pair), while the
**set** form changes which tied abstract 19-24 works retain between seed pairs.
Converting would **introduce** a hash-seed dependency into a step that has none.
The runs are archived at
[ka-counterfactuals.json](docs/literature/search_logs/kalshi-arbitrage/ka-counterfactuals.json)
and re-derivable by
[ka-counterfactuals.py](docs/literature/search_logs/kalshi-arbitrage/ka-counterfactuals.py).

**Consequence for a reader holding the pre-remediation Table X-full:** the row
identifiers in the re-emitted file do not correspond to the old ones. **Join on the
`identifier` field, not on `id`** — and note the field names: the emitted row
identifier is `id`, not `uid`, which the verdicts header called it until this
remediation. **The join is defined for 6,923 of the 8,813 rows.** `identifier` is
the empty string for the other **1,890** (21.4%) — every work with no DOI, no arXiv
id and no RePEc handle — so those rows collapse to a single join value and **cannot
be reconciled at all**; for them the citation string is the only fallback and it is
not a key. On the 6,923 that do carry one, the values are unique.

<!-- prisma-2020-8 -->
PRISMA 2020 item 8, selection process. An LLM screener is an automation tool in
the item's own terms ([Page et al. 2021](https://doi.org/10.1371/journal.pmed.1003583))
and is named here with its version, as is the second tool added by amendment A3.

**This block was materially incomplete as first published and is corrected here
under finding QUANT-1-1 (critical), by amendment A10.** The previous text declared
two automation tools and attributed every verdict outside one 5,249-record stratum
to a screener reading the record. Reading the archived pipeline back, that is not
what happened. `ka-screening-script.py` assigns **every** non-include verdict from
five hard-coded substring lists (`EVENT`, `CONTRIB`, `MODEL`, `DEFI`, `ELICIT`)
through rules R3-R8. Re-running that logic under `PYTHONHASHSEED=0` over a
universe rebuilt from the stored logs, using only the published vocabulary and the
store's included DOIs, reproduces the published nine-code table **exactly**
(`X1` 6,707, `X2` 338, `X3` 35, `X5` 159, `X7` 236, `X9` 1, `X10` 545, `X11` 643,
`include` 149). No individual reading is recoverable from any artefact in this
repository, and the verdicts file's former claim that the rule set "encodes that
reading" was **unfalsifiable and unsupported**. It is withdrawn.

- **screeners_n**: 1
- **independent**: no — single screener; independence is undefined with one screener, and no inter-rater agreement statistic is computed or reported, because with one screener there is nothing to agree with and reporting a number would be a fabrication
- **automation_tools**:
  **(1) The five-list keyword classifier** archived verbatim at
  [ka-screening-script.py](docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py)
  — token lists `EVENT`, `CONTRIB`, `MODEL`, `DEFI`, `ELICIT`, rules **R0-R9**,
  all published in the file. Amendment A10 declares this **the automation tool of
  record for all 8,664 non-include dispositions** (8,663 assigned by the
  classifier; 1 hand-verified). Its declaration supersedes the narrower amendment-A3
  declaration, which named only the R2 branch.
  **(2) Claude Opus 5**, model id `claude-opus-5`, running as the
  `research-librarian` agent under Claude Code / the Claude Agent SDK. Its
  read-based verdicts cover **the 149 included records** (read at abstract or
  metadata depth and extracted per section 5) **and the single hand-verified J6
  same-work twin** excluded X9 under rule R9. It also authored the rule set and the
  token lists, and it wrote this record.
  **(3) The amendment-A3 vocabulary pre-sorter**, token list published at
  [ka-screening-vocabulary.json](docs/literature/search_logs/kalshi-arbitrage/ka-screening-vocabulary.json)
  — the R2 branch of tool (1), retained as a separate declaration because its token
  list and its 2,905 / 5,249 partition counts are published separately.
- **records carrying a read-based verdict**: **150 of 8,813 (1.7%)**
- **records carrying a classifier verdict**: **8,663 of 8,813 (98.3%)**
- **what a disposition code in this artifact therefore means**: that the record's
  title and retrieved abstract contain, or do not contain, particular published
  tokens. It does **not** mean a screener judged the record against the criterion
  the code names. The criterion citation on each row states which criterion the
  rule was written to stand in for, not which criterion was applied by a reader.

**What replaces dual screening, stated as weaker than it.** Every verdict cites a
section-2 criterion by identifier and a published rule id, so any reader can
re-decide any record against the frozen text; the **entire** excluded list is
published with reasons, not only the near-misses, at
[ka-screening-verdicts.jsonl](docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl)
(8,813 rows, one per record, with the same columns the frozen protocol section
4.3 specifies for Table X-full); and a downstream `literature-check` pass
verifies the citations and attributed claims in this record against primary
sources. **None of these is a substitute for an independent second screener**,
and this record does not present them as one.

## 6. Excluded records

**Read the whole of this preamble before reading the table.** Every count below
except `include` and the single X9 row is a **keyword-classifier output**, not a
screener's verdict (finding QUANT-1-1, amendment A10). The `what it means` column
therefore states two things per row: the section-2 criterion the rule was written
to stand in for, and the token condition that actually fired.

**Per-code summary of all 8,664 exclusions.** X4 and X6 were not used: no record
was excluded for being pure decision theory, and none for stating no applicability
condition (that judgement requires a full text, which was not read — see X11).

**X8 was not used either, and that is a deviation, not a clean result (finding
QUANT-1-3, amendment A8).** The previous wording justified the empty X8 row by
saying "no full text was attempted and failed" — but the frozen protocol does not
define X8 in terms of full text. Its frozen text is *"X8 — not retrievable to
abstract depth. Fails I4"*, and frozen criterion I4 reads *"the record is
retrievable at least to abstract depth by the executing agent. Records retrievable
only as a bare title are excluded under X8."* **33 of the 149 included records
were retrieved only to title, venue and year** (AG-7: abstracts were requested for
them from Crossref, OpenAlex, arXiv, Semantic Scholar and DOI content negotiation,
and none returned one). On the frozen text those 33 fail I4 and belong under X8.
They were included anyway. The frontmatter had also restated X8 with a clause that
is not in the frozen protocol — *"or full text unobtainable after the retrieval
chain"* — which is now struck. Amendment **A8** records the relaxation of I4
explicitly, with its rationale, rather than leaving it as unlabelled drift. Under
A8 `n_included` remains 149 and the bibliography SHA-256 is unchanged; a reader
who declines the relaxation should read this corpus as 116 included records plus
33 X8 exclusions, and section 13.2 states what those 33 can and cannot support.

| code | n | verdict source | what it means, and what actually fired |
|---|---|---|---|
| X1 | 6,707 | classifier (R2: 5,249; R8: 1,458) — the per-rule split published under finding REV-1-6 | criterion stood in for: not an in-scope instrument under 2.1 and not a C3 transfer-clause record. Fired on: **R2** — the amendment-A3 DEFAULT-X1 rule, no published vocabulary token anywhere in title or abstract; **R8** — the classifier's fall-through, no event-claim token, no model token, no elicitation token |
| X2 | 338 | classifier (R4) | criterion: satisfies 2.1 but makes none of C1-C4. Fired on: an event-claim token present and no contribution token |
| X3 | 35 | classifier (R7) | criterion: elicitation without a transferable traded claim; fails B-d. Fired on: no event-claim token, no model token, an elicitation token present |
| X5 | **94** | classifier (R5) | criterion: traded object is a token pair or liquidity pool, not an event claim; fails B-a. Fired on: no event-claim token, a model token, and a **word-boundary** DeFi token. **Was 159 before amendment A11 — see the correction below** |
| X7 | **244** | classifier (R1) | criterion: no DOI, arXiv id or RePEc handle in any retrieved metadata record; fails I3. Fired on: the record would otherwise have taken the R3 or R6 branch and carries no persistent identifier. **Was 236 before A11** |
| X9 | 1 | **hand-verified by the screener** | same-work twin, verified at extraction time; J6 retains the journal version (`10.1111/j.1354-7798.2005.00274.x`) and records the working-paper twin (`10.2139/ssrn.294306`). **The only non-include verdict in the whole flow that the classifier did not assign** |
| **X10** | **545** | classifier (R3) | **amendments A4 + A10 — KEYWORD-IDENTIFIED CANDIDATE STRATUM, not a criterion failure and not an eligibility determination.** Fired on: an event-claim token **and** a contribution token both present, which is the A4 extraction-selection rule's keyword proxy for "serves only secondary objective O2 or O3". No record was read; eligibility under I1-I5 was never assessed (finding QUANT-1-4) |
| **X11** | **700** | classifier (R6) | **amendments A5 + A10 — KEYWORD-IDENTIFIED MODEL-RECORD STRATUM, not a criterion failure and not an eligibility determination.** Fired on: a market-making or inventory-model token present and no event-claim token. Neither the section 4.2 stage-1 promotion condition (*"a record is promoted iff its abstract does not settle I1/I2"*) nor any stage-2 assessment was evaluated for any of them, so eligibility is **UNDECIDED** (finding QUANT-1-4). **Was 643 before A11** |

**Correction to the X5 rule, finding QUANT-1-2, amendment A11.** The X5 branch
tested its DeFi vocabulary as **unanchored substrings**. Three of the four short
tokens fired inside unrelated English words: `dex` inside *index* (51 hits among
the affected records), `amm` inside *programming* (9) and inside *programmable*,
*hammer*, *notamment*, *constamment*, and `defi` inside *defined*, *definition*,
*predefined*, *indefinite* (17 across those forms).

**Corpus-wide magnitude of the defect, with the pattern each figure is measured
under stated (findings QUANT-2-9, REPRODUCIBILITY-2-4).** The record previously
published *"289 of the 305 works containing `dex` contain no word-boundary `dex`"*
and *"83 of the 128 containing `amm`"* without saying which pattern
"word-boundary" meant, and both were in fact computed under the **bare** patterns
`\bdex\b` and `\bamm\b` — the patterns this remediation explicitly rejected, not
the ones it shipped. Both are given here, each labelled:

| substring | works containing it | no match under the **bare** pattern (`\bdex\b`, `\bamm\b`) | no match under the **shipped** pattern (`\bdexe?s?\b`, `\bamms?\b`) |
|---|---|---|---|
| `dex` | 305 | **289** | **284** |
| `amm` | 128 | **83** | **64** |

The bare-pattern column is the right one for **sizing the substring defect**, since
it counts works where the substring fires and no standalone token exists; the
shipped-pattern column describes **what the classifier now does**. Both are
re-derivable from the committed pipeline by
[ka-counterfactuals.py](docs/literature/search_logs/kalshi-arbitrage/ka-counterfactuals.py). Records with no DeFi content were therefore published with a **false
criterion-failure reason under B-a** — among them *"A symbolic closed-form
solution to sequential market making with inventory"*, *"Adverse-selection
considerations in the market-making of corporate bonds"*, *"Modeling the Impacts
of Market Activity on Bid-Ask Spreads in the Option Market"* and *"Market
microstructure of FT-SE 100 index futures"*. These are C3 transfer-clause
candidates in the corpus's largest strand, which is where the error does the most
damage.

The four tokens are now matched with word boundaries — `\bdexe?s?\b`,
`\bamms?\b`, `\bdefi\b`, `\bcrypto` — and the classifier was re-run and
`ka-screening-verdicts.jsonl` re-emitted. The inflected forms admitted are exactly
those attested in this universe, so none is invented: the bare patterns the audit
finding prescribed would have wrongly moved **two** genuine DeFi records out of X5
— *"Funding-Aware Optimal Market Making for Perpetual DEXs"*, whose only DeFi token
is `DEXs`, and *"Dynamic Function Market Maker"*, whose abstract reads
"decentralised automated market makers (AMMs)". **Corrected from three to two under
finding QUANT-2-9**, which is adjudicated *upheld on substance, overstated by one*:
the third record the round-1 text named, *"Automated Market Makers in
Cryptoeconomic Systems: A Taxonomy and Archetypes"*, **stays X5 under the bare
patterns**, because its abstract carries four standalone `amm` tokens
(*"...automated market makers (AMMs) is crucial... AMM design..."*) and so matches
`\bamm\b` directly. Re-running the classifier with
`BOUNDED = {\bdex\b, \bamm\b, \bdefi\b, \bcrypto\b}` gives `X5` **92** and `X11`
**702** against the shipped **94** and **700** — a two-record difference, and the
two are the two named. The departure from the prescribed pattern therefore rests on
two records, not three, and is recorded here. Every other DeFi token is eight characters or longer, or contains a
space, and is left as a substring test, which is the frozen behaviour.

**Before and after, exact.** Both runs are reproducible from the committed logs;
the pre-remediation behaviour can be re-derived without editing the script by
setting `KA_DEFI_MATCH=substring`.

| code | before (as published) | after (amendment A11) | delta |
|---|---|---|---|
| X5 | 159 | **94** | **−65** |
| X11 | 643 | **700** | **+57** |
| X7 | 236 | **244** | **+8** |
| X1, X2, X3, X9, X10, include | 6,707 / 338 / 35 / 1 / 545 / 149 | unchanged | 0 |
| total | 8,813 | 8,813 | 0 |

**65 records moved, none of them into a B-a criterion failure**, which was the
point of the fix. **57** fall to **X11** — eligibility undecided, the weakest
disposition available and the honest one for a model record nobody read. **8** fall
to **X7** — they carry no persistent identifier in any retrieved metadata record,
so under the classifier's own first-code-that-applies ordering (R1 is applied after
X1/X2/X5) the model branch routes them to an **I3** failure. **This departs from
the audit finding's prescription that the reclassified records "fall to X11 at
worst".** X7 is a criterion failure — but it is a failure of I3, a fact about the
retrieved metadata, not of B-a, a judgement about the traded object; the
prescription's substance is met and the departure is recorded rather than papered
over. The eight are: *A Symbolic Closed-Form Solution to Sequential Market Making
with Inventory*; *Dealers, insiders and bandits*; *Designing Automated Market
Makers with Adaptive Liquidity*; *Essays on Modeling of Blind Principal Bid Basket
Trading Cost*; *FEEDBACK TRADING z*; *Three essays on market microstructure*; *Why
Is the VIX Index Related to the Liquidity Premium*; *Topics in stochastic control
with applications to algorithmic trading*.

**The A3 residual risk is partly quantified, not unquantifiable (finding
QUANT-1-8).** Section 13.1 previously called it "unquantified and unquantifiable"
and described it as failing only on records whose title **and** abstract contain no
published token. In fact **only 2,159 of the 5,249 DEFAULT-X1 records carry any
abstract: 3,090 (58.9%) were rule-excluded on title text alone**, so for those the
"title and abstract" condition reduces to a title condition and the exposure is
materially larger than stated. Corpus-wide, 4,779 of 8,813 works have an abstract.
The residual risk is therefore **bounded below by the 3,090-record title-only
stratum** and is reported that way in section 13.1.

**Table X-nearmiss (PRISMA 2020 item 16b proper).** **No record reached full-text
assessment and was then excluded**, because no full-text assessment was performed
in this execution. The table is therefore reported as empty in those words rather
than omitted. The **700** X11 rows are the records that *would* have populated it
and did not, which is why they are counted and named rather than folded into a
criterion code. (643 before amendment A11; see the X5 correction above.)

<!-- prisma-2020-16b -->
**Itemized exclusions of records that looked eligible.** These are the individual
rows PRISMA 2020 item 16b exists for: records a reader would expect to find in the
corpus and will not. The full 8,664-row table is the JSONL artifact named above.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| U07089 | Inter-market Arbitrage in Sports Betting. RePEc/IDEAS listing, no year in retrieved metadata | identification | X7: no DOI, arXiv id or RePEc handle in any retrieved record; only a bare IDEAS surface form was returned, so the record cannot be resolved (fails I3, FAIR F1 gap) |
| U07161 | Is weak form efficiency an illusion? Evidence from a market for state contingent claims | identification | X7: no persistent identifier in any retrieved metadata record; retained here as a locator so the gap is visible rather than dropped |
| U06950 | Improved Liquidity for Prediction Markets | identification | X7: no persistent identifier; a directly on-topic S4 record that cannot enter the store under I3/FAIR F1 |
| U03575 | Market Scoring Rules Act As Opinion Pools For Risk-Averse Agents | identification | X7: no persistent identifier; an S4 market-scoring-rule record lost to I3 |
| U04329 | Risk-Averse Market Maker and Supply of Liquidity | identification | X7: no persistent identifier; S4 inventory-risk record lost to I3 |
| U05985 | Betting exchanges: a market maker process | identification | X7: no persistent identifier; an S4/S6 record on the exact mechanism of interest, lost to I3 |
| U08200 | The Bookie Puzzle: Auction versus Dealer Markets in Online Sports Betting | identification | X7: no persistent identifier; an S6 mechanism-comparison record lost to I3 |
| U03957 | Parimutuel Versus Fixed-Odds Markets | identification | X7: no persistent identifier; an S6 mechanism-comparison record lost to I3 |
| U07810 | Price formation in parimutuel markets | identification | X7: no persistent identifier; an S4/S6 record lost to I3 |
| U00257 | The Price of Running Liquid Prediction Markets | identification | X7: no persistent identifier; an S5 subsidy-cost record lost to I3 |
| U07153 | Is Liquidity Related to Prediction Market Efficiency? | identification | X7: no persistent identifier; an S5/S6 record lost to I3 |
| U01176 | A Parimutuel Market Microstructure for Contingent Claims Trading. SSRN Electronic Journal (2001), doi:10.2139/ssrn.294306 | title-abstract | X9: hand-verified same work as the retained European Financial Management (2005) version doi:10.1111/j.1354-7798.2005.00274.x; J6 retains the journal version and records the working-paper twin here |
| U06369 | Do Large Language Models Know What They Don't Know? Kalshibench. arXiv (2025) | title-abstract | X2: uses Kalshi contracts as a benchmark for language-model calibration; states no price condition, measures no price quantity and specifies no market-maker model, so it satisfies 2.1 but makes none of C1-C4 |
| U05722 | AURA Policy Uncertainty Index: A Real-Time, Market-Implied Index Constructed from Prediction Market Prices (2026) | title-abstract | X2: constructs an index from event-contract prices; reports prices as an input to a macro indicator and states no coherence condition, no measured discrepancy and no market-maker model |
| U01605 | Augur: a decentralized, open-source platform for prediction markets | title-abstract | X10: keyword-identified candidate stratum — an S4/S7 platform-design record whose tokens matched the A4 secondary-objective proxy. **No eligibility determination was made** (A10, QUANT-2-3); extraction not performed in this execution (capacity gap, not a criterion failure) |
| U08027 | Settlement Manipulation in Prediction Markets. arXiv (2026) | title-abstract | X10: keyword-identified candidate stratum; its tokens bear on settlement and adjudication (E7) rather than on a primary objective, so it was dispositioned under the A4 extraction-selection rule and not extracted. **Eligibility was never assessed** (A10, QUANT-2-3) |
| U01609 | Automated Market Making and Loss-Versus-Rebalancing. arXiv (2022) | title-abstract | X5: the traded object is a token pair in a constant-function pool, not an event claim; fails B-a. Its loss-versus-rebalancing apparatus nevertheless reaches the corpus through the included record that transfers it to prediction markets |
| U01465 | An equivalence between the Kyle (1985) and the Glosten-Milgrom (1985) models. Economics Letters (1992) | n/a (included) | not excluded — listed here only because a reader may expect it under X11 with the rest of the transfer-clause lineage; it is included as a named-lineage C3 record |

## 7. Included corpus

<!-- included-corpus -->
149 records, each carrying a persistent identifier (FAIR F1). The
machine-readable form is the CSL-JSON store; this table is the human-readable
index.

**This table was regenerated from the store on 2026-09-02 under findings
LITERATURE-1-1, LITERATURE-1-2 and LITERATURE-1-3.** As first published its year
and venue columns were hand-composed and disagreed with the DOI registrant, and
with the artifact's own CSL-JSON store, for a large minority of rows. What was
verified and what changed:

- **All 149 DOIs were fetched from a registration agency at remediation time**:
  122 resolved at `api.crossref.org`, 26 at `api.datacite.org` (25 arXiv DataCite
  DOIs plus one ResearchGate DOI). **One did not resolve at either** —
  `10.11179/ker.74.119` (Tanaka, *The Kyoto Economic Review*), whose registration
  agency is neither; it is recorded as verification gap **AG-10** in section 13.3
  and its metadata is carried from the store unverified against a registrant.
- **The store was checked against the registrant and found correct on every
  comparable field.** **Re-run and archived 2026-09-02 under findings QUANT-2-8 and
  REPRODUCIBILITY-2-6** — the round-1 sweep asserted these numbers with no stored
  response behind them, which broke this record's own frontmatter guarantee that
  "every metadata field traces to a stored response in the search-log directory".
  The sweep is now a committed script and a committed per-DOI log,
  [ka-store-registrant-sweep.py](docs/literature/search_logs/kalshi-arbitrage/ka-store-registrant-sweep.py)
  and
  [ka-store-registrant-sweep.json](docs/literature/search_logs/kalshi-arbitrage/ka-store-registrant-sweep.json)
  (one row per DOI: agency queried, HTTP status, registrant `issued` / `created` /
  `container-title` / `type`, the store's value, and an agree/disagree flag). **What
  it returns, and how it differs from what round 1 published:**
  **147** year comparisons, **0** disagreements — not 148. Two records cannot be
  compared, not one: `10.11179/ker.74.119` (no registration agency, AG-10) and
  `10.1007/978-3-540-77105-0_11` (Peters, So & Ye), whose Crossref record carries
  `issued.date-parts = [[null]]`.
  **94** `container-title` comparisons, **0** disagreements. A registrant supplies a
  container for **119** of the 149 — that marginal is correct — but the store also
  carries one for only 94 of those 119; the other **25** are the arXiv DataCite rows,
  for which the store carries no `container-title` at all, so there is nothing to
  compare. Round 1 reported the 119 marginal as though it were the comparison count,
  which credited 25 non-comparisons as agreements.
- **27 year cells and 78 venue cells were rewritten** to the store's values, and
  **18 citation years inside section 8** were re-derived from the same field.
- **2 tier cells were corrected** (see the tier note below).

**Columns, with the field each carries, stated so the table is auditable.**
`citation` is `author-surname (year). title. venue.` where **`year` is the
CSL-JSON store's `issued` field** — the registrant's earliest recorded publication
date — and **`venue` is the store's `container-title`, or its `publisher` where the
registrant records no container**. `tier` is the CLAUDE.md evidence tier (T1
peer-reviewed, T2 official documentation, T3 professional standard, T4 vetted
technical forum, T5 other, admissible only with the tier recorded next to the
claim). `E4/E15` is the venue of the evidence and its section-8 classification:
**K** = Kalshi-specific (the record's own data or institutional object is KalshiEX
LLC), **G** = generalizable-with-stated-assumption (evidence from another venue;
the carrying assumption is written on the claim line in section 8), **N** =
venue-none / theoretical (classified by its assumptions, not by a venue).
`strand(s)` carries extraction field **E3**, which is authoritative; a `[synth Sn]`
suffix names the section-8 block a record's claim line actually sits in where that
differs (finding LITERATURE-1-11, 10 records). `depth` is the extraction depth
actually reached (E17): **abs** = abstract (116 records), **meta** = title / venue
/ year metadata only (33 records; their inclusion runs against frozen criterion I4
and is authorised by amendment A8, not by the frozen text). **No record in this
corpus was read at full text** — see section 13.2 and amendment A9.

**`year` convention, named rather than left implicit.** `CONVENTION`: one year per
record, taken from the store's `issued` field. For **12** records the registrant
also records a later print year and the commonly used citation year is that later
one. Both are correct; this artifact carries the earlier consistently so that the
table, the section-8 claim lines and the store cannot disagree. The 12 are
`10.1111/ecca.12009` (2012 / print 2013), `10.1007/s11579-012-0087-0` (2012/2013),
`10.1080/14697688.2017.1395230` (2017/2018), `10.1177/1527002513493630`
(2013/2015), `10.1002/for.1085` (2008/2009), `10.1177/1527002517696957`
(2017/2018), `10.1111/j.1468-0335.2008.00716.x` (2009/2010),
`10.1007/s10614-015-9514-7` (2015/2016), `10.1007/s00199-018-1155-3` (2018/2019),
`10.1093/oep/gpaf023` (2025/2026), `10.1080/00036846.2015.1111993` (2015/2016) and
`10.1093/ej/ueaf040` (2025/2026).

**Documented exception to that convention: retro-registered DOIs (finding
LITERATURE-2-3).** The convention's stated ground — that the registrant's `issued`
field is "the registrant's earliest recorded publication date" — **is false for the
University of Buckingham Press prefix `10.5750`**, and stating it as a universal
put a five-year misdating of the corpus's canonical LMSR paper into both its table
row and its section-8 claim line. All seven `10.5750` records were deposited at
Crossref on **2020-08-26** (`created`), and their `issued` / `published-online`
values are the **2012-2014 dates on which a back-catalogue was reposted to the
publisher's OJS platform**, not the dates of publication. The discriminator is the
registrant's own `volume`/`issue`: JPM volume 1 issue 1 cannot have been published
in 2012 and carry a 2012 deposit of volume 14.

**The rule, stated so it is checkable.** *Where the registrant's `issued` year is
inconsistent with the registrant's own `volume`/`issue`, the volume-year is carried
and **both** values are recorded on the row.* The volume-year is not inferred: it is
read from **RePEc/EconPapers**, an independent bibliographic registry of the same
series (`RePEc:buc:jpredm`, `RePEc:buc:jgbeco`), and the per-record evidence is
archived at
[ka-store-retroreg-yearcheck.json](docs/literature/search_logs/kalshi-arbitrage/ka-store-retroreg-yearcheck.json).
Five rows change:

| record | registrant `issued` | RePEc volume-year | carried |
|---|---|---|---|
| Hanson `10.5750/jpm.v1i1.417` | 2012-12-13 | JPM **1(1)**, 2007, pp. 3-15 | **2007** |
| Abramovicz `10.5750/jpm.v1i2.423` | 2012-12-14 | JPM **1(2)**, 2007, pp. 111-125 | **2007** |
| Seemann `10.5750/jpm.v2i3.445` | 2012-12-14 | JPM **2(3)**, 2008, pp. 33-46 | **2008** |
| Bergfjord `10.5750/jpm.v6i3.589` | 2013-01-22 | JPM **6(3)**, 2012, pp. 14-26 | **2012** |
| Antweiler `10.5750/jpm.v7i3.824` | 2014-01-16 | JPM **7(3)**, 2013, pp. 61-86 | **2013** |

Two `10.5750` rows do **not** change. `10.5750/jgbe.v7i2.630` (Constantinou &
Fenton) is confirmed at JGBE 7(2), 2013, which is what the record already carried.
`10.5750/jpm.v14i1.1796` (Stershic & Gujral, 2020) **could not be checked** —
RePEc's coverage of this series ends at volume 9 (2015) — and is carried on the
registrant's `issued` value **unverified against an independent registry**. That is
recorded as a residual, not closed.

**What the store does and does not carry.** The CSL-JSON store is **not** edited:
it remains a faithful mirror of the registrant, so the sweep's "0 year
disagreements" statement above stays true and `bibliography_sha256` is unchanged.
The exception lives in this record, on the row, with both values visible. A
consequence a reader must see: the store `id` strings still encode the registrant
year (`hanson2012jpmv1i1417`), so a store key is an identifier and **not** a
citation year.

**Author lists on section-8 claim lines (finding LITERATURE-2-6).** `CONVENTION`,
now stated rather than left implicit: **every in-text citation prints the store's
complete `author` family-name list**, comma-separated with `&` before the last, and
**no `et al.` and no truncation is used anywhere**. The record already printed full
lists for four- and five-author works, so a truncated list was indistinguishable
from a complete one. A mechanical sweep of every `[Authors YEAR](identifier)` form
in the document against the store's `author` array found **eight citation forms
truncated at three surnames** where the store carries four or five — Grant,
Oikonomidis, Bruce & Johnson (three sites); Bergfjord, Kildal, McPherson, Loftaas &
Valvik; Chen, Fortnow, Lambert, Pennock & Wortman; Gao, Wang, Wu & Yu; Rana,
Nadkarni, Moshrefi & Viswanath; Nueve, Nguyen, Frongillo & Waggoner; Bhaskara,
Frongillo, Lindgren & Papireddygari; Xi, Moallemi, Pai & Wang — all corrected, and
the sweep now returns zero mismatches. The section-7 table's `citation` column is a
separate and deliberately different form: **first author only**, as its own legend
above states, because it is an index row rather than a citation.

**arXiv venue sweep, finding LITERATURE-2-4.** A record's tier was being decided
against this artifact's own other copy of its own value rather than against the
registrant, which cannot detect a preprint whose journal or proceedings venue the
registrant records. **All 25 `10.48550` rows were re-checked against the arXiv
abstract record's `journal_ref`, `Related DOI` and `Report number` fields on
2026-09-02** (archived at
[ka-store-arxiv-venuecheck.json](docs/literature/search_logs/kalshi-arbitrage/ka-store-arxiv-venuecheck.json)).
**Exactly one of the 25 carries non-arXiv venue evidence:** `1206.5252`
(Chen & Pennock), report number `UAI-P-2007-PG-49-56`, Comments *"Appears in
Proceedings of the Twenty-Third Conference on Uncertainty in Artificial
Intelligence (UAI2007)"*. It is re-tiered **T5 → T1** and re-dated **2012 → 2007**,
with the arXiv posting recorded as the retrieved manifestation. **The other 24 carry
no `journal_ref`, no related DOI and no report number**, so on the evidence
available they are preprint-only manifestations and their T5 tier and arXiv-posting
years stand. That is a bounded negative — arXiv `journal_ref` is author-supplied and
frequently not updated after publication — and it is stated as such rather than as
"none of the other 24 was ever published". The section-7 tier distribution moves to
**T1 91 / T5 58**.

**Tier reconciliation, finding LITERATURE-1-3.** The protocol's discipline is
tier-blind admission with tier-labelled use, and the tier travels with the claim
(protocol section 2.5); a record carrying two different tiers in one artifact
defeats it. A mechanical check over every DOI in the artifact found **six** records
whose section-7 tier contradicted the tier written on their section-8 claim line —
two more than the audit finding named. Each is reconciled to one value with the
deciding evidence named, which in every case is the registrant's `type` and
`container-title`:

| record | table said | claim line said | registrant | resolved to | where the edit is |
|---|---|---|---|---|---|
| Taleb `10.1080/14697688.2017.1395230` | T5 | T1 | Crossref `journal-article`, *Quantitative Finance* | **T1** | table corrected |
| Gampe & Griffin `10.1016/j.cnsns.2022.106994` | T5 | T1 | Crossref `journal-article`, *Comm. Nonlinear Sci. Numer. Simul.* | **T1** | table corrected |
| Abramovicz `10.5750/jpm.v1i2.423` | T1 | T5 | Crossref `journal-article`, *The Journal of Prediction Markets* | **T1** | claim line corrected (8.4.2) |
| Constantinou & Fenton `10.5750/jgbe.v7i2.630` | T1 | T5 | Crossref `journal-article`, *The Journal of Gambling Business and Economics* | **T1** | claim line corrected (8.2.2) |
| Bergfjord et al. `10.5750/jpm.v6i3.589` | T1 | T5 | Crossref `journal-article`, *The Journal of Prediction Markets* | **T1** | claim line corrected (8.2.2) |
| Stershic & Gujral `10.5750/jpm.v14i1.1796` | T1 | T5 | Crossref `journal-article`, *The Journal of Prediction Markets* | **T1** | claim line corrected (8.2.2) |

Two of the six are journal articles that the table had mis-tiered T5, which
understated the corpus's peer-reviewed base by two records. The section-7 tier
distribution was **T1 88 / T5 61** before reconciliation and **T1 90 / T5 59**
after it; the round-2 arXiv venue sweep above moves Chen & Pennock as well, giving
the current **T1 91 / T5 58**. The check is mechanical and re-runnable: no DOI in
this artifact now carries two tier values.

**Venue is the field the tier is derived from**, so the 78 venue corrections above
are tier-relevant and not cosmetic. The ones that changed a record's apparent kind:
Abramovicz and Flepp et al. were shown as *SSRN Electronic Journal* and are journal
articles in *The Journal of Prediction Markets* and *The Quarterly Review of
Economics and Finance*; Antweiler and Bergfjord et al. were shown as *RePEc/IDEAS*
and are *Journal of Prediction Markets* articles; Gao, Wang, Wu & Yu was shown as an
ACM conference and is *Operations Research*; Othman et al. was shown as an ACM
conference and is *ACM Transactions on Economics and Computation*; Gampe & Griffin
and Taleb were shown as *arXiv* and are journal articles; Wolfers & Zitzewitz and
Diercks et al. were shown against a wrong or absent publisher and are NBER working
papers (`10.3386` is the NBER prefix).

**Records included but not carried into section 8, finding LITERATURE-1-9.** A
mechanical check of every included DOI against the text of section 8 found **19**
records with no claim line anywhere in the synthesis, while their `role in the
argument` column affirmatively stated that they enter a named section-8 block. That
column was therefore false for 19 rows. Three of them are the ones the finding
named and they are **added to section 8** in this remediation at their stated
extraction depth: **Subramanian 2026** (T1, Kalshi-specific, added to 8.6.1),
**Diercks, Katz & Wright 2026** (Kalshi-specific, added to 8.6.1) and
**Štrumbelj 2014** (added to 8.1.2). For the other **16**, the role column now says
what is true: included and extracted, but carrying no claim line, with the reason.
The omission was not neutral — one of the two peer-reviewed Kalshi records in the
whole corpus was among the missing, so the synthesized Kalshi block was
effectively 18-of-18 T5 before this fix (finding LITERATURE-1-10).

| id | citation | persistent id | tier | E4/E15 | strand(s) | depth | role in the argument |
|---|---|---|---|---|---|---|---|
| abernethy2011199357419936 | Abernethy (2011). An optimization-based framework for automated market-making. Proceedings of the 12th ACM conference on Electronic commerce. | 10.1145/1993574.1993621 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| abernethy2013246576924657 | Abernethy (2013). Efficient Market Making via Convex Optimization, and a Connection to Online Learning. ACM Transactions on Economics and Computation. | 10.1145/2465769.2465777 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| abernethy2014260005726029 | Abernethy (2014). A general volume-parameterized market making framework. Proceedings of the fifteenth ACM conference on Economics and computation. | 10.1145/2600057.2602900 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| abernethy2015272873227287 | Abernethy (2015). On risk measures, market making, and exponential families. ACM SIGecom Exchanges. | 10.1145/2728732.2728734 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| abramovicz2012jpmv1i2423 | Abramovicz (**2007**). THE HIDDEN BEAUTY OF THE QUADRATIC MARKET SCORING RULE: A UNIFORM LIQUIDITY MARKET MAKER, WITH VARIATIONS. The Journal of Prediction Markets. | 10.5750/jpm.v1i2.423 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue **Year exception, finding LITERATURE-2-3:** the registrant's `issued` value is `2012-12-14`, a retro-registration/online-repost date; the volume-year verified at RePEc is 2007. |
| agrawal2011opre11100922 | Agrawal (2011). A Unified Framework for Dynamic Prediction Market Design. Operations Research. | 10.1287/opre.1110.0922 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| angelini2019jijforecast2 | Angelini (2019). Efficiency of Online Football Betting Markets. International Journal of Forecasting. | 10.1016/j.ijforecast.2018.07.008 | T1 | G | S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| antweiler2014jpmv7i3824 | Antweiler (**2013**). Liquidity Provision And Cross Arbitrage In Continuous Double-Auction Prediction Markets. The Journal of Prediction Markets. | 10.5750/jpm.v7i3.824 | T1 | G | S4+S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line **Year exception, finding LITERATURE-2-3:** the registrant's `issued` value is `2014-01-16`, a retro-registration/online-repost date; the volume-year verified at RePEc is 2013. |
| ashiya2013152700251349 | Ashiya (2013). Lock! Risk-Free Arbitrage in the Japanese Racetrack Betting Market. Journal of Sports Economics. | 10.1177/1527002513493630 | T1 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| avellaneda2008146976807013 | Avellaneda (2008). High-frequency trading in a limit order book. Quantitative Finance. | 10.1080/14697680701381228 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| back2004j14680262200 | Back (2004). Information in Securities Markets: Kyle Meets Glosten and Milgrom. Econometrica. | 10.1111/j.1468-0262.2004.00497.x | T1 | N | S4+S6 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| bakalo2026ssrn6150527 | Bakalo (2026). Understanding the Favorite–Longshot Bias: Review of Explanations and a Hedging-Based Mechanism. Elsevier BV. | 10.2139/ssrn.6150527 | T5 | G | S3 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| bartlett2026ssrn6615739 | Bartlett (2026). Adverse Selection in Prediction Markets: Evidence from Kalshi. Elsevier BV. | 10.2139/ssrn.6615739 | T5 | K | S6 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| berg2008s15740722070 | Berg (2008). Results from a Dozen Years of Election Futures Markets Research. Handbook of Experimental Economics Results. | 10.1016/s1574-0722(07)00080-7 | T1 | G | S2 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| bergfjord2013jpmv6i3589 | Bergfjord (**2012**). Arbitrage Trade In Prediction Markets. The Journal of Prediction Markets. | 10.5750/jpm.v6i3.589 | T1 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line **Year exception, finding LITERATURE-2-3:** the registrant's `issued` value is `2013-01-22`, a retro-registration/online-repost date; the volume-year verified at RePEc is 2012. |
| berkowitz2017152700251769 | Berkowitz (2017). The Conversion of Money Lines Into Win Probabilities. Journal of Sports Economics. | 10.1177/1527002517696957 | T1 | G | S1 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| bhaskara2023ageneralth | Bhaskara (2023). A General Theory of Liquidity Provisioning for Prediction Markets. arXiv. | 10.48550/arxiv.2311.08725 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| birge2021opre20212109 | Birge (2021). Dynamic Learning and Market Making in Spread Betting Markets with Informed Bettors. Operations Research. | 10.1287/opre.2021.2109 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| brahma2010comparingp | Brahma (2010). Comparing Prediction Market Structures, With an Application to Market Making. arXiv. | 10.48550/arxiv.1009.1446 | T5 | G | S4 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| buckle2018155862351801 | Buckle (2018). The Efficiency of Sport Betting Markets: An Analysis Using Arbitrage Trading within Super Rugby. International Journal of Sport Finance. | 10.1177/155862351801300305 | T1 | G | S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| brgi2025ssrn5502658 | Bürgi (2025). Makers and Takers: The Economics of the Kalshi Prediction Market. Elsevier BV. | 10.2139/ssrn.5502658 | T5 | K | S3+S5 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| cao2026ssrn7049119 | Cao (2026). Retail-Adjusted Expected Value in Prediction Markets: Calibration, Longshot Bias, and Consumer Welfare. Elsevier BV. | 10.2139/ssrn.7049119 | T5 | G | S3+S5 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| chakraborty2011199357419936 | Chakraborty (2011). Market making and mean reversion. Proceedings of the 12th ACM conference on Electronic commerce. | 10.1145/1993574.1993622 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| chakraborty2015aaaiv29i1931 | Chakraborty (2015). Price Evolution in a Continuous Double Auction Prediction Market With a Scoring-Rule Based Market Maker. Proceedings of the AAAI Conference on Artificial Intelligence. | 10.1609/aaai.v29i1.9313 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| chen2012autilityfr | Chen (**2007**). A Utility Framework for Bounded-Loss Market Makers. **Proceedings of the Twenty-Third Conference on Uncertainty in Artificial Intelligence (UAI 2007), pp. 49-56**; retrieved manifestation arXiv:1206.5252. | 10.48550/arxiv.1206.5252 | **T1** | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue. **Tier and year corrected 2026-09-02, finding LITERATURE-2-4** — see the arXiv venue sweep note below |
| chen2008138679013868 | Chen (2008). Complexity of Combinatorial Market Makers. Proceedings of the 9th ACM conference on Electronic commerce. | 10.1145/1386790.1386822 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| chen2010180734218073 | Chen (2010). A New Understanding of Prediction Markets Via No-Regret Learning. Proceedings of the 11th ACM conference on Electronic commerce. | 10.1145/1807342.1807372 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| chen2013248254024826 | Chen (2013). Cost function market makers for measurable spaces. Proceedings of the fourteenth ACM conference on Electronic commerce. | 10.1145/2482540.2482608 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| cheng2026arbitragea | Cheng (2026). Arbitrage Analysis in Polymarket NBA Markets. arXiv. | 10.48550/arxiv.2605.00864 | T5 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| constantinou2013jgbev7i2630 | Constantinou (2013). Profiting from arbitrage and odds biases of the European football gambling market. The Journal of Gambling Business and Economics. | 10.5750/jgbe.v7i2.630 | T1 | G | S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| dalen2025towardblac | Dalen (2025). Toward Black Scholes for Prediction Markets: A Unified Kernel and Market Maker's Handbook. arXiv. | 10.48550/arxiv.2510.15205 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| dalen2026whathappen | Dalen (2026). What Happens When Institutional Liquidity Enters Prediction Markets: Identification, Measurement, and a S. arXiv. | 10.48550/arxiv.2604.10005 | T5 | G | S4+S5 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| das2005146976805001 | Das * (2005). A learning market-maker in the Glosten–Milgrom model. Quantitative Finance. | 10.1080/14697680500148067 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| dellavedova2026ssrn6191618 | Della Vedova (2026). Who Profits from Prediction Markets? Execution, not Information. Elsevier BV. | 10.2139/ssrn.6191618 | T5 | G | S4+S5 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| depken2021s41302020001 | Depken (2021). Integrity Fees in Sports Betting Markets. Eastern Economic Journal. | 10.1057/s41302-020-00179-z | T1 | N | S5 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| diercks2026w34702 | Diercks (2026). Kalshi and the Rise of Macro Markets. National Bureau of Economic Research. | 10.3386/w34702 | T5 | K | S6 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| donatoni2022146976882022 | Donatoni (2022). Market making with inventory control and order book information. Quantitative Finance. | 10.1080/14697688.2022.2028888 | T1 | G | S4+S6 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| dubach2026theanatomy | Dubach (2026). The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book. arXiv. | 10.48550/arxiv.2604.24366 | T5 | G | S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| dudik2012222901222290 | Dudik (2012). A tractable combinatorial market maker using constraint generation. Proceedings of the 13th ACM Conference on Electronic Commerce. | 10.1145/2229012.2229047 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| dudk2021bbzi6501 | Dudík (2021). Log-time Prediction Markets for Interval Securities. International Joint Conference on Autonomous Agents and Multiagent Systems. | 10.65109/bbzi6501 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| feil2026optimalmar | Feil (2026). Optimal Market Making in Prediction Markets. arXiv. | 10.48550/arxiv.2607.17991 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| feys2026avellaneda | Feys (2026). Avellaneda-Stoikov and Cartea-Jaimungal as One Framework: A Forced Uniqueness Theorem for Inventory Marke. arXiv. | 10.48550/arxiv.2606.01477 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| flepp2017jqref2016070 | Flepp (2017). The liquidity advantage of the quote-driven market: Evidence from the betting industry. The Quarterly Review of Economics and Finance. | 10.1016/j.qref.2016.07.016 | T1 | G | S4+S6 [synth S5] | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| franck2012ecca12009 | Franck (2012). Inter-Market Arbitrage in Betting. Economica. | 10.1111/ecca.12009 | T1 | G | S2+S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| frongillo2023anaxiomati | Frongillo (2023). An Axiomatic Characterization of CFMMs and Equivalence to Prediction Markets. arXiv. | 10.48550/arxiv.2302.00196 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| gampe2023jcnsns202210 | Gampe (2023). Dynamics of a Binary Option Market with Exogenous Information and Price Sensitivity. Communications in Nonlinear Science and Numerical Simulation. | 10.1016/j.cnsns.2022.106994 | T1 | N | S6 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| gao2010978364217572 | Gao (2010). An Axiomatic Characterization of Continuous-Outcome Market Makers. Lecture Notes in Computer Science. | 10.1007/978-3-642-17572-5_44 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| gao2025opre20220417 | Gao (2025). Price Interpretability of Prediction Markets: A Convergence Analysis. Operations Research. | 10.1287/opre.2022.0417 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| gauriot2025ueaf040 | Gauriot (2025). How Market Prices React to Information: Evidence from Binary Options Markets. The Economic Journal. | 10.1093/ej/ueaf040 | T1 | G | S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| gebele2026executable | Gebele (2026). Executable Arbitrage and Market Efficiency in Prediction Markets. arXiv. | 10.48550/arxiv.2608.00666 | T5 | G | S1+S2+S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| gebele2026semanticno | Gebele (2026). Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets. arXiv. | 10.48550/arxiv.2601.01706 | T5 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| gill2026ssrn7245879 | Gill (2026). Trading the Jump in Prediction Markets. Elsevier BV. | 10.2139/ssrn.7245879 | T5 | G | S5 [synth S6] | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| gill2026ssrn7110798 | Gill (2026). The Term Structure of a Prediction Market. Elsevier BV. | 10.2139/ssrn.7110798 | T5 | G | S6 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| glosten19850304405x8590 | Glosten (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. Journal of Financial Economics. | 10.1016/0304-405x(85)90044-3 | T1 | N | S6 [synth S4] | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| goel2026jiref2026105 | Goel (2026). Measuring macroeconomic surprise magnitude with prediction markets: Market-implied dispersion from Kalshi. International Review of Economics &amp; Finance. | 10.1016/j.iref.2026.105577 | T1 | K | S6 [synth S2] | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| gomezgonzalez2018ebl742018129 | Gomez-Gonzalez (2018). The betting market over time: overround and surebets in European football. Economics and Business Letters. | 10.17811/ebl.7.4.2018.129-136 | T1 | G | S2+S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| grant20181351847x2018 | Grant (2018). New entry, strategic diversity and efficiency in soccer betting markets: the creation and suppression of . The European Journal of Finance. | 10.1080/1351847x.2018.1443148 | T1 | G | S2+S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| greene2026ssrn6442939 | Greene (2026). Trend Quality and Predictability in Prediction Markets: Evidence from Minute-Level Kalshi Data. Elsevier BV. | 10.2139/ssrn.6442939 | T5 | K | S6 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| groeger2016theinforma | Groeger (2016). The Informational Content of the Limit Order Book: An Empirical Study of Prediction Markets. arXiv. | 10.48550/arxiv.1609.03471 | T5 | G | S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| gupta2026ssrn6858200 | Gupta (2026). Who Profits in Binary Prediction Markets? Maker-Taker Dynamics, Behavioral Bias, and Sentiment Arbitrage . Elsevier BV. | 10.2139/ssrn.6858200 | T5 | K | S3+S5 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| guant2012s11579012008 | Guéant (2012). Dealing with the Inventory Risk. A solution to the market making problem. Mathematics and Financial Economics. | 10.1007/s11579-012-0087-0 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| hanke2019jod201926412 | Hanke (2019). Numeraire Dependence in Risk-Neutral Probabilities of Event Outcomes. The Journal of Derivatives. | 10.3905/jod.2019.26.4.128 | T1 | N | S1 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| hanson2003a10220582090 | Hanson (2003). Combinatorial Information Market Design. Information Systems Frontiers. | 10.1023/a:1022058209073 | T1 | N | S1+S4 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| hanson2012jpmv1i1417 | Hanson (**2007**). LOGARITHMIC MARKETS CORING RULES FOR MODULAR COMBINATORIAL INFORMATION AGGREGATION. The Journal of Prediction Markets. | 10.5750/jpm.v1i1.417 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue **Year exception, finding LITERATURE-2-3:** the registrant's `issued` value is `2012-12-13`, a retro-registration/online-repost date; the volume-year verified at RePEc is 2007. |
| hausch2008978981281919 | Hausch (2008). Introduction to the Efficiency of Win Markets and the Favorite-Longshot Bias. World Scientific Handbook in Financial Economics Series. | 10.1142/9789812819192_0025 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| hegarty2025gpaf023 | Hegarty (2025). Market structure and prices in online betting markets: theory and evidence. Oxford Economic Papers. | 10.1093/oep/gpaf023 | T1 | N | S3+S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| ho19810304405x8190 | Ho (1981). Optimal dealer pricing under transactions and return uncertainty. Journal of Financial Economics. | 10.1016/0304-405x(81)90020-9 | T1 | N | S4 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| hodges2013j1468036x201 | Hodges (2013). Fixed Odds Bookmaking with Stochastic Betting Demands. European Financial Management. | 10.1111/j.1468-036x.2010.00601.x | T1 | N | S3+S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| hofer2017jjedc2016120 | Hofer (2017). Relative pricing of binary options in live soccer betting markets. Journal of Economic Dynamics and Control. | 10.1016/j.jedc.2016.12.007 | T1 | G | S6 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| kizildemir2025jqas20240064 | Kizildemir (2025). A family of solutions related to Shin’s model for probability forecasts. Journal of Quantitative Analysis in Sports. | 10.1515/jqas-2024-0064 | T1 | G | S1 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| koch2007ssrn964438 | Koch (2007). Bookmaker and pari-mutuel betting: Is a (reverse) favourite-longshot bias built-in?. Elsevier BV. | 10.2139/ssrn.964438 | T5 | G | S3 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| kotawala2026locallycoh | Kotawala (2026). Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents. arXiv. | 10.48550/arxiv.2605.30335 | T5 | N | S1 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| krause2026ssrn7117919 | Krause (2026). Calibration and Forecast Accuracy of Macroeconomic Prediction Markets: Evidence from Kalshi, 2025-2026. Elsevier BV. | 10.2139/ssrn.7117919 | T5 | K | S6 [synth S3] | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| krause2026ssrn7119120 | Krause (2026). Information Efficiency Across Macroeconomic Prediction Markets: Evidence from Kalshi. Elsevier BV. | 10.2139/ssrn.7119120 | T5 | K | S6 [synth S3] | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| krause2026ssrn7021660 | Krause (2026). The Limits of Prediction: A Comparative Analysis of Market Efficiency Across Three Kalshi Prediction Mark. Elsevier BV. | 10.2139/ssrn.7021660 | T5 | K | S6 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| krause2026ssrn7110758 | Krause (2026). Market Efficiency and the Favorite-Longshot Bias in Unemployment Prediction Markets. Elsevier BV. | 10.2139/ssrn.7110758 | T5 | K | S3 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| krause2026ssrn7087538 | Krause (2026). Zero-Price Contracts and the Favorite-Longshot Bias in CPI Prediction Markets. Elsevier BV. | 10.2139/ssrn.7087538 | T5 | K | S3 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| krishnan1992016517659290 | Krishnan (1992). An equivalence between the Kyle (1985) and the Glosten—Milgrom (1985) models. Economics Letters. | 10.1016/0165-1765(92)90014-p | T1 | N | S4+S6 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| kroer2016294071629407 | Kroer (2016). Arbitrage-Free Combinatorial Market Making via Integer Programming. Proceedings of the 2016 ACM Conference on Economics and Computation. | 10.1145/2940716.2940767 | T1 | N | S1+S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| kyle19851913210 | Kyle (1985). Continuous Auctions and Insider Trading. Econometrica. | 10.2307/1913210 | T1 | N | S6 [synth S4] | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| lange2005j13547798200 | Lange (2005). A Parimutuel Market Microstructure for Contingent Claims. European Financial Management. | 10.1111/j.1354-7798.2005.00274.x | T1 | N | S4+S6 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| lee2026ssrn6748186 | Lee (2026). Cryptocurrency Prediction Markets through the Derivatives Lens: Evidence from Kalshi and Polymarket. Elsevier BV. | 10.2139/ssrn.6748186 | T5 | K | S2 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| lee2026ssrn6964226 | Lee (2026). Underreaction, Salience, and Hot-Hand Beliefs in Sports Event-Contract Markets: Evidence from Kalshi NBA . Elsevier BV. | 10.2139/ssrn.6964226 | T5 | K | S6 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| lekwijit2018jm2062017006 | Lekwijit (2018). Optimizing the liquidity parameter of logarithmic market scoring rules prediction markets. Journal of Modelling in Management. | 10.1108/jm2-06-2017-0066 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| levitt2004j14680297200 | Levitt (2004). Why are Gambling Markets Organised so Differently from Financial Markets?. The Economic Journal. | 10.1111/j.1468-0297.2004.00207.x | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| li2013248254024825 | Li (2013). An axiomatic characterization of adaptive-liquidity market makers. Proceedings of the fourteenth ACM conference on Electronic commerce. | 10.1145/2482540.2482575 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| lim2026ssrn6704139 | Lim (2026). Kalshi's Ceiling: Settlement Asymmetry and the Intraday Limits of Cross-Venue Repricing in Event Contract. Elsevier BV. | 10.2139/ssrn.6704139 | T5 | K | S2 | meta | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| liu2016jjet20160100 | Liu (2016). Market making with asymmetric information and inventory risk. Journal of Economic Theory. | 10.1016/j.jet.2016.01.005 | T1 | N | S4 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| luckner2008cecandeee200 | Luckner (2008). Arbitrage Opportunities and Market-Making Traders in Prediction Markets. 2008 10th IEEE Conference on E-Commerce Technology and the Fifth IEEE Conference on Enterprise Computing, E-Commerce and E-Services. | 10.1109/cecandeee.2008.131 | T1 | G | S4 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| lycsa2015000368462015 | Lyócsa (2015). What drives intermediation costs? A case of tennis betting market. Applied Economics. | 10.1080/00036846.2015.1111993 | T1 | G | S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| makropoulou2011j14679485201 | Makropoulou (2011). Optimal Price Setting in Fixed‐Odds Betting Markets Under Information Uncertainty. Scottish Journal of Political Economy. | 10.1111/j.1467-9485.2011.00557.x | T1 | N | S3+S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| manaster199693953 | Manaster (1996). Life in the Pits: Competitive Market Making and Inventory Control. Review of Financial Studies. | 10.1093/rfs/9.3.953 | T1 | G | S4+S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| manski2006jeconlet2006 | Manski (2006). Interpreting the predictions of prediction markets. Economics Letters. | 10.1016/j.econlet.2006.01.004 | T1 | N | S1 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| marek2019sportsbett | Marek (2019). Sports Betting Arbitrage in English Football. Unpublished. | 10.13140/rg.2.2.13916.03201 | T5 | G | S2+S5 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| moallemi2026uniformlos | Moallemi (2026). Uniform-Loss Automated Market Making for Prediction Markets. arXiv. | 10.48550/arxiv.2607.17428 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| mohanty2026dopredicti | Mohanty (2026). Do Prediction Markets Forecast Cryptocurrency Volatility? Evidence from Kalshi Macro Contracts. arXiv. | 10.48550/arxiv.2604.01431 | T5 | K | S6 [synth S2] | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| montone2012ssrn2199035 | Montone (2012). Optimal Mark-up and Arbitrages in the Betting Market. SSRN Electronic Journal. | 10.2139/ssrn.2199035 | T5 | G | S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| moshrefi2026apmmautoma | Moshrefi (2026). APMM: Automated Parlay Market Maker. arXiv. | 10.48550/arxiv.2607.18299 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| moulinier2026ssrn7170178 | Moulinier (2026). Mistiming is not Arbitrage: A Pre-registered Falsification of Cross-Platform Prediction-market Arbitrage,. Elsevier BV. | 10.2139/ssrn.7170178 | T5 | K | S1+S2+S5 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| nechepurenko2026permarketi | Nechepurenko (2026). Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Dec. arXiv. | 10.48550/arxiv.2605.02287 | T5 | G | S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| newall2021risks9010022 | Newall (2021). Are Sports Bettors Biased toward Longshots, Favorites, or Both? A Literature Review. Risks. | 10.3390/risks9010022 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| nueve2025smoothquad | Nueve (2025). Smooth Quadratic Prediction Markets. arXiv. | 10.48550/arxiv.2505.02959 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| nueve2026adaptiveli | Nueve (2026). Adaptive Liquidity in Prediction Markets via Online Learning. arXiv. | 10.48550/arxiv.2605.09599 | T5 | N | S1+S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| nunes2026ssrn6446502 | Nunes (2026). Statistical Arbitrage in Binary Prediction Markets: Three Systematic Strategies and Their Empirical Prope. Elsevier BV. | 10.2139/ssrn.6446502 | T5 | G | S1 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| oliven2004mnsc10400191 | Oliven (2004). Suckers Are Born but Markets Are Made: Individual Rationality, Arbitrage, and Market Efficiency on an Ele. Management Science. | 10.1287/mnsc.1040.0191 | T1 | G | S1+S6 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| othman2013250941325094 | Othman (2013). A Practical Liquidity-Sensitive Automated Market Maker. ACM Transactions on Economics and Computation. | 10.1145/2509413.2509414 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| othman2011978364225510 | Othman (2011). Liquidity-Sensitive Automated Market Makers via Homogeneous Risk Measures. Lecture Notes in Computer Science. | 10.1007/978-3-642-25510-6_27 | T1 | N | S4 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| othman2012222901222290 | Othman (2012). Profit-charging market makers with bounded loss, vanishing bid/ask spreads, and unlimited market depth. Proceedings of the 13th ACM Conference on Electronic Commerce. | 10.1145/2229012.2229074 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| ottaviani2010mic2158 | Ottaviani (2010). Noise, Information and the Favorite-Longshot Bias in Parimutuel Predictions. American Economic Journal: Microeconomics. | 10.1257/mic.2.1.58 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| ottaviani2008b97804445074 | Ottaviani (2008). The Favorite-Longshot Bias: An Overview of the Main Explanations. Handbook of Sports and Lottery Markets. | 10.1016/b978-044450744-0.50009-3 | T1 | G | S3 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| palumbo2026ssrn6325658 | Palumbo (2026). A Microstructure Perspective on Prediction Markets. Elsevier BV. | 10.2139/ssrn.6325658 | T5 | G | S6 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| pennock2004988772988799 | Pennock (2004). A dynamic pari-mutuel market for hedging, wagering, and information aggregation. Proceedings of the 5th ACM conference on Electronic commerce. | 10.1145/988772.988799 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| petersNone978354077105 | Peters (**2007**). Pari-Mutuel Markets: Mechanisms and Performance. Lecture Notes in Computer Science (*Internet and Network Economics*, WINE 2007). | 10.1007/978-3-540-77105-0_11 | T1 | G | S4 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line **Year exception, found by the QUANT-2-8 sweep:** the registrant's `issued` is `[[null]]` and the store carries no year, so this row read `(n.d.)` while its own section-8 claim line read `Peters, So & Ye 2007` — the table and the claim line disagreed. Resolved to **2007** on the registrant's `created` date `2007-12-03` and OpenAlex `publication_year` 2007; the store is left faithful to the registrant. |
| polson2026ssrn7254820 | Polson (2026). Prediction Markets, Bayes and Kalshi. Elsevier BV. | 10.2139/ssrn.7254820 | T5 | K | S6 [synth S1] | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| portnaya2026dopredicti | Portnaya (2026). Do Prediction Markets Match Option Prices? Bitcoin Threshold Evidence from Binance and Polymarket. arXiv. | 10.48550/arxiv.2606.19517 | T5 | G | S1+S2 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| rahman2025sokmarketm | Rahman (2025). SoK: Market Microstructure for Decentralized Prediction Markets (DePMs). arXiv. | 10.48550/arxiv.2510.15612 | T5 | G | S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| rana2026parlaymark | Rana (2026). ParlayMarket: Automated Market Making for Parlay-style Joint Contracts. arXiv. | 10.48550/arxiv.2603.22596 | T5 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| restocchi2019jfrl20180800 | Restocchi (2019). The temporal evolution of mispricing in prediction markets. Finance Research Letters. | 10.1016/j.frl.2018.08.003 | T1 | G | S2 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| restocchi2019jphysa201809 | Restocchi (2019). The stylized facts of prediction markets: Analysis of price changes. Physica A: Statistical Mechanics and its Applications. | 10.1016/j.physa.2018.09.183 | T1 | G | S6 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| rhode2004089533004137 | Rhode (2004). Historical Presidential Betting Markets. Journal of Economic Perspectives. | 10.1257/0895330041371277 | T1 | G | S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| rothschild2014af140031 | Rothschild (2014). The extent of price misalignment in prediction markets. Algorithmic Finance. | 10.3233/af-140031 | T1 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| sung2009j14680335200 | SUNG (2009). Revealing Weak‐Form Inefficiency in a Market for State Contingent Claims: The Importance of Market Ecolog. Economica. | 10.1111/j.1468-0335.2008.00716.x | T1 | G | S1+S6 | abs | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| saguillo2025unravellin | Saguillo (2025). Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets. arXiv. | 10.48550/arxiv.2508.03474 | T5 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| saliou2026ssrn7222239 | Saliou (2026). Efficient Prices, Inefficient Spreads: Attention and Liquidity in Prediction Markets. Elsevier BV. | 10.2139/ssrn.7222239 | T5 | G | S5 [synth S6] | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| seemann2012jpmv2i3445 | Seemann (**2008**). THE EFFECT OF STOCK ENDOWMENTS ON THE LIQUIDITY OF PREDICTION MARKETS. The Journal of Prediction Markets. | 10.5750/jpm.v2i3.445 | T1 | G | S5 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line **Year exception, finding LITERATURE-2-3:** the registrant's `issued` value is `2012-12-14`, a retro-registration/online-repost date; the volume-year verified at RePEc is 2008. |
| sestovic2017ssrn3044673 | Sestovic (2017). Risk-Return Optimisations Can Lead to Favourite-Longshot Bias in Prediction Markets Operated by Bookmaker. SSRN Electronic Journal. | 10.2139/ssrn.3044673 | T5 | G | S3 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| sestovic2017ssrn3035848 | Sestovic (2017). Bookmaker Margins and Favourite-Longshot Bias in Football Prediction Markets. SSRN Electronic Journal. | 10.2139/ssrn.3035848 | T5 | G | S3 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| sethi2015s10614015951 | Sethi (2015). Belief Aggregation with Automated Market Makers. Computational Economics. | 10.1007/s10614-015-9514-7 | T1 | N | S4 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| shin19922234526 | Shin (1992). Prices of State Contingent Claims with Insider Traders, and the Favourite-Longshot Bias. The Economic Journal. | 10.2307/2234526 | T1 | N | S3 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| slamka2013tem201221916 | Slamka (2013). Prediction Market Performance and Market Liquidity: A Comparison of Automated Market Makers. IEEE Transactions on Engineering Management. | 10.1109/tem.2012.2191618 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| snowberg2010655844 | Snowberg (2010). Explaining the Favorite–Long Shot Bias: Is it Risk-Love or Misperceptions?. Journal of Political Economy. | 10.1086/655844 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| sobel2008b97804445074 | Sobel (2008). Unifying the Favorite-Longshot Bias with Other Market Anomalies. Handbook of Sports and Lottery Markets. | 10.1016/b978-044450744-0.50011-1 | T1 | G | S3 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| stershic2020jpmv14i11796 | Stershic (2020). Arbitrage in Political Prediction Markets. The Journal of Prediction Markets. | 10.5750/jpm.v14i1.1796 | T1 | G | S1+S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| subramanian2026ijfmd2026100 | Subramanian (2026). Prediction market efficiency: evidence from Kalshi on pricing accuracy, forecasting, and risk. International Journal of Financial Markets and Derivatives. | 10.1504/ijfmd.2026.10080801 | T1 | K | S6 | meta | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| swanson2026ssrn6073727 | Swanson (2026). The Effects of Monetary Policy on Macroeconomic Expectations: High-Frequency Evidence from Prediction Mar. Elsevier BV. | 10.2139/ssrn.6073727 | T5 | G | S6 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| taleb2017146976882017 | Taleb (2017). Election Predictions as Martingales: An Arbitrage Approach. Quantitative Finance. | 10.1080/14697688.2017.1395230 | T1 | G | S1 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| tanaka2005inventorye | Tanaka (2005). Inventory Effects of Two Risk-Averse Market Makers. The Kyoto Economic Review. | 10.11179/ker.74.119 | T1 | N | S4 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| tarnaud2018s00199018115 | Tarnaud (2018). Convergence within binary market scoring rules. Economic Theory. | 10.1007/s00199-018-1155-3 | T1 | N | S4 | meta | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| tetlock2008ssrn929916 | Tetlock (2008). Liquidity and Prediction Market Efficiency. Elsevier BV. | 10.2139/ssrn.929916 | T5 | G | S5 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| thaler1988jep22161 | Thaler (1988). Anomalies: Parimutuel Betting Markets: Racetracks and Lotteries. Journal of Economic Perspectives. | 10.1257/jep.2.2.161 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| vidalpuga2017s13209017015 | Vidal-Puga (2017). On the effect of taxation in the online sports betting market. SERIEs. | 10.1007/s13209-017-0156-y | T1 | N | S5 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| vlastakis2008for1085 | Vlastakis (2008). How efficient is the European football betting market? Evidence from arbitrage and trading strategies. Journal of Forecasting. | 10.1002/for.1085 | T1 | G | S2 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| wolfers2006w12200 | Wolfers (2006). Interpreting Prediction Market Prices as Probabilities. National Bureau of Economic Research. | 10.3386/w12200 | T5 | N | S1 | abs | venue-none / theoretical; classified by its stated assumptions, not by a venue |
| xi2026volatility | Xi (2026). Volatility in Prediction Markets: A Structural Approach. arXiv. | 10.48550/arxiv.2607.08199 | T5 | G | S1+S6 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| yang2026ssrn6396698 | Yang (2026). Skilled Liquidity Provision in Prediction Markets: Evidence from 150 Million Trades. Elsevier BV. | 10.2139/ssrn.6396698 | T5 | G | S4+S5 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| yurchyna2026ssrn7364100 | Yurchyna (2026). Composition Shift and the Measurement of Bias in a Growing Prediction Market: Evidence from Kalshi, 2021-. Elsevier BV. | 10.2139/ssrn.7364100 | T5 | K | S5 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand |
| zhou2007ssrn997788 | Zhou (2007). Trading the Tradesports NFL Market: An Analysis of Liquidity and Pricing Efficiency. SSRN Electronic Journal. | 10.2139/ssrn.997788 | T5 | G | S5 | meta | included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9): at the depth reached it adds no statement the named record in its block does not already carry, or it is at metadata depth and its findings therefore cannot be stated |
| ziemba2023annurevfinan | Ziemba (2023). Pari-Mutuel Betting Markets: Racetracks and Lotteries Revisited. Annual Review of Financial Economics. | 10.1146/annurev-financial-053122-021925 | T1 | G | S3 | abs | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |
| trumbelj2014jijforecast2 | Štrumbelj (2014). On determining probability forecasts from betting odds. International Journal of Forecasting. | 10.1016/j.ijforecast.2014.02.008 | T1 | G | S1 | meta | evidence from another venue; enters the generalized block with its carrying assumption written on the claim line |

## 8. Synthesis by strand

**Reading rules for this section, all binding.**

1. **Every claim line carries a resolvable citation.** A line with no citation is
   a defect, not a stylistic choice.
2. **Extraction depth is abstract or metadata, never full text** (section 13.2).
   Every statement below is a statement about **what a record's abstract or
   metadata says**, transcribed as the record states it. Where an abstract does
   not settle a point, this section says so instead of inferring it.
3. **No quantitative pooling and no vote counting.** Records differ in venue,
   mechanism, period and measurement; there is no common estimand. Figures are
   transcribed, never re-derived, re-scaled or rounded silently.
4. **The section 8 separation is structural.** Each strand opens with a
   **Kalshi-specific** block and then a **generalized** block. Every generalized
   claim carries its **carrying assumption** on the same line, naming what must
   hold for the transfer: the wagering mechanism (E6), the fee and commission
   structure (E12), the settlement and adjudication process (E7), the participant
   population, and any regulatory constraint the source's venue operated under.
   Where an assumption cannot be written out, the claim is marked
   `not-transferable-as-stated` and is reported that way, not softened.
5. **This corpus states no trading rule of its own** (REVIEW.md blocking
   directive 8, binding here by ADR-0004). Where a record states one, the
   attribution status of that rule is recorded (E14) and the rule is **not**
   restated here as established.

### 8.1 Strand S1 — no-arbitrage and internal coherence for binary contracts

#### 8.1.1 Kalshi-specific

- Kalshi contract prices are informative and improve in accuracy as a market
  approaches close, on transaction-level data covering over 300,000 contracts
  ([Bürgi, Deng & Whelan 2025](https://doi.org/10.2139/ssrn.5502658), T5 working paper,
  abstract depth).
- One record states the price-as-probability reading explicitly for the venue: an
  event contract settles at one dollar or zero, "so its price is a probability
  and the exchange is a market quoted in the currency of Bayes", with Kalshi as
  the leading case; it states three requirements for that reading to support
  inference across a board of contracts — a latent parameter low-dimensional
  relative to the number of listed contracts, a posterior that carries parameter
  uncertainty into every derived contract, and a sizing rule
  ([Polson 2026](https://doi.org/10.2139/ssrn.7254820), T5 preprint,
  abstract depth). The corpus records this as a **stated modelling position**,
  not as a demonstrated property of Kalshi prices.
- A pre-registered falsification finds **no** structurally protected cross-venue
  arbitrage between Kalshi and Polymarket on executable quotes: at true alignment
  the median cross-venue mid divergence is 0.60 cents against a stated 2.00-cent
  Kalshi fee, and only 7.03% of 20,915 aligned minutes carry a fee-clearing edge
  with a median life of one minute; deliberately mistiming one venue's quotes
  makes the apparent edge grow monotonically to 23.8% at seven minutes and 40.8%
  at sixty ([Moulinier 2026](https://doi.org/10.2139/ssrn.7170178), T5 preprint,
  abstract depth). **The corpus reports this against the opposite claim in
  8.1.2 without averaging them away.**

#### 8.1.2 Generalized (each line states the assumption that carries it)

- The foundational negative result: if traders are risk-neutral price takers with
  heterogeneous beliefs, a contract price **reveals nothing about the dispersion**
  of beliefs and only partially identifies their central tendency; most persons
  hold beliefs above price when price exceeds 0.5 and below it when price is
  under 0.5 ([Manski 2006](https://doi.org/10.1016/j.econlet.2006.01.004), T1,
  abstract depth). *Carries to any venue whose contracts are all-or-nothing
  claims traded by price-taking participants; it is a statement about the mapping
  from beliefs to price and is independent of mechanism, fee structure and
  regulatory status, so no venue-matching assumption is needed.*
- The complementary positive result: sufficient conditions exist under which
  prediction-market prices correspond to mean beliefs, and for a broad class of
  models prices are usually close to mean beliefs, with **risk aversion and the
  belief distribution** as the key driving parameters
  ([Wolfers & Zitzewitz 2006](https://doi.org/10.3386/w12200), T5 working paper,
  abstract depth). *Carries only under the two named parameters: a venue whose
  participant population is materially more risk-averse, or whose belief
  distribution is materially more dispersed, is outside the stated sufficient
  conditions. Neither parameter has been measured on Kalshi in this corpus.*
- Coherence is violated in practice on venues where it can be measured. Logically
  related contracts are persistently misaligned, arbitrage opportunities between
  **identical contracts on different exchanges** persist, order-book depth
  understates the true size of the opportunity (established by a randomized field
  trial of several thousand dollars of transactions), and misalignment among
  identical and logically related contracts on the **same** exchange clusters at
  moments of high information flow
  ([Rothschild & Pennock 2014](https://doi.org/10.3233/af-140031), T1, abstract
  depth). *Carries to a venue with (E6) a continuous double auction, (E7) contract
  families whose logical relations are declared, and (E12) fees low enough that
  the measured misalignment exceeds them; the field-trial component additionally
  assumes a venue where an outside party may transact, which a CFTC-designated
  contract market's membership arrangements may or may not permit — the corpus
  cannot settle that from the documentation it retrieved (section 9).*
- The mutually-exclusive-and-exhaustive condition is stated operationally for an
  on-chain venue: a market's condition set must be exhaustive and mutually
  exclusive, so the collective prices of all related outcomes should be one
  dollar; despite that design, dependent assets are mispriced and outcomes can be
  bought below or sold above one dollar in aggregate
  ([Saguillo et al. 2025](https://arxiv.org/abs/2508.03474), T5 preprint,
  abstract depth). *Carries to any venue that lists a declared
  mutually-exclusive-and-exhaustive family; the mispricing measurement itself does
  not carry, because it is measured on that venue's own book and fee schedule.*
- A distinction the corpus treats as the central S1 result of the recent
  literature: **payoff-space** no-arbitrage, which follows from terminal payoffs,
  is not the same as **protocol-executable** no-arbitrage, which depends on the
  position transformations a venue actually makes available before settlement.
  On a venue whose linked binary markets represent mutually exclusive outcomes
  but whose adapter operationalizes only the NO-to-YES direction before
  settlement, violations of payoff bounds need not be exploitable; the record
  estimates 1.12 million dollars in reconstructed depth-aware violations
  ([Gebele, Mutzel & Matthes 2026](https://arxiv.org/abs/2608.00666), T5 preprint, abstract
  depth). *Carries to Kalshi only under an explicit statement of which position
  transformations Kalshi's own rulebook makes available before settlement —
  which is exactly the venue-structural fact the AG-1 access gap (section 13.3)
  prevented this corpus from retrieving. The claim is therefore recorded as*
  `not-transferable-as-stated` *until that document is obtained.*
- Cross-venue coherence fails for a reason upstream of price: without a shared
  notion of event identity, liquidity does not pool across venues, arbitrage
  becomes capital-intensive or unenforceable, and prices systematically violate
  the law of one price, so prices reflect platform-local beliefs rather than one
  globally aggregated probability
  ([Gebele & Matthes 2026](https://doi.org/10.48550/arxiv.2601.01706), T5 preprint,
  abstract depth). *Carries to any multi-venue comparison, including
  Kalshi-versus-Polymarket, under the assumption that the two venues' contract
  definitions are not machine-identical — which the record's own framing asserts
  and which the Kalshi rulebook would be needed to verify.*
- Coherence can fail compositionally even when every component is locally
  coherent: a composed quote can violate probability axioms, and the residual
  distance from the coherent polytope is computable at runtime from declared
  coupling constraints, with a deterministic projection that repairs it
  ([Kotawala 2026](https://doi.org/10.48550/arxiv.2605.30335), T5 preprint,
  abstract depth). *Venue-none; it carries to a contract board under the
  assumption that the board's logical coupling constraints are declared and
  machine-readable, which no record in this corpus establishes for Kalshi.*
- Combinatorial market making can be operated **arbitrage-free by construction**
  via integer programming, at the cost that arbitrage-free pricing under a
  subsidy bound is `#P`-hard in the worst case; the authors demonstrate
  tractability on real combinatorial bets from a basketball tournament with an
  outcome space of size two to the sixty-third
  ([Kroer et al. 2016](https://doi.org/10.1145/2940716.2940767), T1, abstract
  depth). *Venue-none; it carries as a design statement, not as evidence about any
  operating venue.*
- On a venue with a public order book, single-market arbitrage anomalies are
  **exceedingly rare** — 7 executable in-game episodes with a median duration of
  3.6 seconds across 173 games reconstructed from over 75 million limit-order-book
  snapshots — while combinatorial inefficiencies are more frequent at 290 active
  episodes ([Cheng, Yang & Zou 2026](https://arxiv.org/abs/2605.00864), T5 preprint, abstract
  depth). *Carries to Kalshi only under matched (E6) continuous-double-auction
  microstructure, (E12) comparable taker fees, and (E5) comparable contract
  duration; the record's venue is Polymarket and its sport-specific in-game
  setting is not matched by any Kalshi record in this corpus.*
- Three systematic strategies are documented on binary prediction markets, one of
  which is a stated structural condition rather than a strategy: a spread-based
  edge exists **when the market-maker spread exceeds twice the taker fee**; a
  mutually-exclusive family whose YES prices collectively exceed unity signals
  oversubscription; and a strike ladder must be monotone, so a lower strike
  pricing below a higher strike is a pure arbitrage
  ([Nunes 2026](https://doi.org/10.2139/ssrn.6446502), T5 preprint, abstract
  depth). **REVIEW.md directive 8 note (E14):** the record states these as its own
  constructions with an internal derivation, so they are attributed within the
  record; **this corpus nevertheless states none of them as a rule**, and a reader
  must not read the monotone-ladder or sum-to-unity conditions as endorsed
  tradeable rules here. *The first condition carries only where the fee schedule
  is known and the spread is observable; on Kalshi the fee schedule is a
  filer-published document this corpus could not retrieve (AG-1).*
- Against the price-space treatments, one strand of the corpus prices the event
  claim as a derivative. Binary election estimates can be treated as martingales
  and priced by arbitrage as binary options, with the arbitrage valuation
  minimizing the Brier score conventionally used to grade probability assessors;
  when uncertainty about the final outcome is high the arbitrage value moves
  toward one half ([Taleb 2017](https://doi.org/10.1080/14697688.2017.1395230),
  T1, abstract depth). *Carries to any venue whose contract is a
  cash-or-nothing digital on a verifiable event, under the assumption that the
  underlying belief process is continuously updated and that there is no
  settlement-timing wedge — the second assumption is precisely what one Kalshi
  record disputes (8.2.1).*
- Risk-neutral outcome probabilities are **numeraire-dependent** for events that
  themselves move exchange rates, so state prices differ across affected currency
  pairs and quoted odds that ignore this can create approximate arbitrage; the
  record states that quoted odds appear to ignore the effect
  ([Hanke, Poulsen & Weissensteiner 2019](https://doi.org/10.3905/jod.2019.26.4.128), T1, abstract
  depth). *Carries to any multi-currency event-contract venue; whether it carries
  to Kalshi depends on whether Kalshi lists contracts on events with a
  first-order exchange-rate impact and settles in a single currency, which no
  record in this corpus establishes.*
- The conversion from quoted odds to an implied probability is not unique. Seven
  published methods for converting money lines reduce to three distinct estimates
  of bookmaker commission and subjective win probability, one of which is biased
  when the line implies a very heavy favorite; the choice of method should depend
  on the market inefficiency being studied, the favorite-longshot bias among them
  ([Berkowitz et al. 2017](https://doi.org/10.1177/1527002517696957), T1,
  abstract depth). *Carries wherever prices are quoted as odds with an embedded
  margin; it does **not** carry to a venue quoting a cent-denominated price with
  an explicit separate fee, which is the structural distinction between a
  bookmaker book and an event exchange.*
- A family of closed-form solutions related to Shin's model produces probability
  forecasts from odds and is evaluated on sports betting data sets
  ([Kizildemir, Akin & Alkan 2025](https://doi.org/10.1515/jqas-2024-0064), T1,
  abstract depth); the underlying model derives the favorite-longshot bias from
  the presence of insider traders in a market for state-contingent claims
  ([Shin 1992](https://doi.org/10.2307/2234526), T1, abstract depth).
  *Both carry only to venues whose price is an odds quote containing a
  bookmaker's margin (E6 = bookmaker fixed-odds book), because the overround is
  the object the normalization removes.*
- **Added under finding LITERATURE-1-9, at metadata depth.** The determination of
  probability forecasts from betting odds is treated directly in
  ([Štrumbelj 2014](https://doi.org/10.1016/j.ijforecast.2014.02.008), T1,
  *International Journal of Forecasting*, **metadata depth — no abstract
  retrieved**). Its topic is on the same odds-to-probability conversion question
  as the Berkowitz and Kizildemir entries above; **this corpus states no finding of
  it**, because it did not read one. *If read, it would carry under the same
  bookmaker-margin assumption as the entries above.*

### 8.2 Strand S2 — cross-venue and cross-instrument price discrepancies

#### 8.2.1 Kalshi-specific

- One record makes the venue's settlement mechanics the explanatory object,
  arguing from **settlement asymmetry** to an intraday ceiling on cross-venue
  repricing in event contracts ([Lim 2026](https://doi.org/10.2139/ssrn.6704139),
  T5 preprint). **Extraction depth: metadata only — no abstract was returned by
  any source, so this corpus states the record's topic and cannot state its
  measured quantity, its data period, or the direction of its finding.** It is
  listed because omitting a directly on-point Kalshi record would misrepresent
  the corpus.
- Cross-venue: on 855 deterministically matched MLB moneylines and all four
  strikes of one Federal Reserve decision, Kalshi one-minute bid/ask candlesticks
  joined to a full Polymarket order-book archive show a median cross-venue mid
  divergence of 0.60 cents against a 2.00-cent Kalshi fee
  ([Moulinier 2026](https://doi.org/10.2139/ssrn.7170178), T5 preprint, abstract
  depth). This is the corpus's only Kalshi-versus-Polymarket price-divergence
  measurement.
- Cross-instrument: **the Kalshi-measured part of a mixed-venue record.**
  Risk-neutral skewness recovered from **multi-strike Kalshi events** is reported
  as near zero
  ([Lee, Lee & Lee 2026a](https://doi.org/10.2139/ssrn.6748186), T5 preprint,
  abstract depth). **Separation-rule repair, finding LITERATURE-1-12:** the rest of
  this record's result is not Kalshi-specific and was previously stated inside the
  Kalshi block without a carrying assumption. Its 113,338-contract Bitcoin and
  Ethereum sample spans **Kalshi and Polymarket**, and the implied-volatility
  surfaces, risk-neutral densities and variance risk premia are extracted from that
  pooled sample; the record's own framing treats binary contracts on **both**
  venues as structurally identical to cash-or-nothing digital options. That
  pooled-sample material is reported in 8.2.2 with its assumption. The corpus
  cannot say what the pooled quantities would be on Kalshi alone, because the
  abstract does not split them.
- Cross-instrument, other direction: daily probability changes in Kalshi macro
  contracts forecast cryptocurrency realized volatility through a monetary-policy
  channel (Fed repricing, in-sample t = 3.63) and a recession-risk channel (out
  of sample MSFE ratio 0.979, Clark-West p = 0.020)
  ([Mohanty & Krishnamachari 2026](https://arxiv.org/abs/2604.01431), T5
  preprint, abstract depth).
- Kalshi-implied dispersion carries information beyond professional forecasts: a
  one-unit increase in the market-implied interquartile range is associated with a
  0.75 increase in the absolute headline-CPI surprise (HC1 SE 0.17, t = 4.44,
  R-squared 0.20, N = 45) in the record's declared primary specification
  ([Goel 2026](https://doi.org/10.1016/j.iref.2026.105577), T1, abstract depth).

#### 8.2.2 Generalized (each line states the assumption that carries it)

- **Moved here from the Kalshi block by finding LITERATURE-1-12.** Binary
  contracts on Kalshi **and Polymarket** are treated as structurally identical to
  cash-or-nothing digital options, and implied-volatility surfaces, risk-neutral
  densities and variance risk premia are extracted from a pooled sample of 113,338
  Bitcoin and Ethereum contracts traded between September 2025 and February 2026
  ([Lee, Lee & Lee 2026a](https://doi.org/10.2139/ssrn.6748186), T5 preprint,
  abstract depth). *Carries as a Kalshi statement only under the assumption that
  the two venues' Bitcoin and Ethereum contract families are close enough that a
  pooled surface describes either one — which the record asserts by construction
  and which no record in this corpus verifies. The Kalshi-only quantity the
  abstract does isolate (near-zero risk-neutral skewness from multi-strike Kalshi
  events) is stated in 8.2.1 instead.*
- A combined bet at a bookmaker and at a betting exchange yields a guaranteed
  positive return in **19.2%** of matches in the top-five European soccer leagues;
  bookmakers frequently posted arbitrage positions and experienced, on average,
  negative margins from them, which the authors read as bookmakers pricing over
  future customer trading behaviour rather than over a single bet
  ([Franck, Verbeek & Nüesch 2012](https://doi.org/10.1111/ecca.12009), T1,
  abstract depth). *Carries only to a venue pairing (E6) a bookmaker fixed-odds
  book with an exchange, with (E12) the bookmaker's margin as the friction and
  (E7) identical settlement rules on both sides. Kalshi is a single exchange, so
  the mechanism pairing this result depends on does not exist there; recorded*
  `not-transferable-as-stated` *for Kalshi.*
- Efficiency differs across bookmakers and leagues: with the best odds selected
  across 41 bookmakers on 11 European leagues over 11 years, eight markets are
  efficient and three show inefficiencies implying profit opportunities
  ([Angelini & De Angelis 2019](https://doi.org/10.1016/j.ijforecast.2018.07.008),
  T1, abstract depth). *Carries under (E6) a multi-bookmaker fixed-odds market and
  (E12) a best-odds-across-books selection step; both are structurally absent at a
  single exchange.*
- Combined betting across bookmakers produces "limited but highly profitable"
  arbitrage opportunities, and simple trading rules and forecast-encompassing
  strategies produce significant positive returns
  ([Vlastakis, Dotsis & Markellos 2008](https://doi.org/10.1002/for.1085), T1,
  abstract depth). **E14 attribution note:** the record states its own strategies
  with an internal derivation; this corpus restates none of them as a rule.
  *Same carrying assumption as the line above.*
- Arbitrage opportunities exist but are frequently **not exploitable** because of
  venue conduct rather than price: bookmakers split into "position-takers", who
  change odds infrequently and actively restrict informed traders, and
  "book-balancers", who manage inventory by adjusting odds and restrict customers
  little; of 545 identified arbitrage portfolios, around 50% require a bet on the
  favourite at a position-taking bookmaker, and those firms' management practices
  generally prevent execution
  ([Grant, Oikonomidis, Bruce & Johnson 2018](https://doi.org/10.1080/1351847x.2018.1443148),
  T1, abstract depth). *This is the sharpest generalized statement in the corpus of
  the difference between a measured discrepancy and an executable one. It carries
  to any venue that can restrict or refuse a participant; whether a
  CFTC-designated contract market can do so, and on what terms, is a
  venue-structural fact this corpus could not retrieve (AG-1, section 9).*
- One in every three trades in a Super Rugby betting market provided an arbitrage
  opportunity, with odds differing by bookmaker geography
  ([Buckle & Huang 2018](https://doi.org/10.1177/155862351801300305), T1,
  abstract depth). *Carries under (E6) multi-bookmaker fixed odds and a
  geographically segmented participant population.*
- Bookmaker odds accuracy did **not** improve over 2005/06-2011/12 across 14
  European leagues, and consistent odds biases and numerous arbitrage
  opportunities are demonstrated
  ([Constantinou & Fenton 2013](https://doi.org/10.5750/jgbe.v7i2.630), **T1** —
  corrected from T5 under finding LITERATURE-1-3; Crossref records a
  `journal-article` in *The Journal of Gambling Business and Economics*, so the
  previous hedge "journal-tier record without a peer-review claim in the retrieved
  metadata" was wrong on the retrieved metadata — abstract depth). *Same fixed-odds carrying assumption.*
- Prices (overround) fell continuously from 2000-01 to 2016-17 while the number of
  "surebets" among major bookmakers **increased** in recent years
  ([Gomez-Gonzalez & Del Corral 2018](https://doi.org/10.17811/ebl.7.4.2018.129-136),
  T1, abstract depth). *Carries under (E12) an overround-based margin, which is
  the bookmaker construct; an exchange's explicit taker fee is not an overround
  and the two are not interchangeable without an argument this corpus does not
  have.*
- Arbitrage exists on a racetrack parimutuel pool but is **rare after frictions**:
  2 of 175 Japanese thoroughbred races, with guaranteed profits of 5,120 yen and
  340 yen after accounting for the minimum betting unit and the price impact of
  the arbitrage bet itself on the odds
  ([Ashiya 2013](https://doi.org/10.1177/1527002513493630), T1, abstract depth).
  *Carries only to (E6) parimutuel pools, where the arbitrageur's own bet moves
  the payout; on an order book the analogous friction is depth, not pool
  dilution, and the two are not the same object.*
- Cross-border, cross-platform arbitrage in political event markets is **rare and
  difficult to exploit**, though inter-market opportunities exist and the authors
  hypothesise national differences in political opinion as the cause
  ([Bergfjord, Kildal, McPherson, Loftaas & Valvik 2012](https://doi.org/10.5750/jpm.v6i3.589),
  **T1** — corrected from T5 under finding LITERATURE-1-3; Crossref records a
  `journal-article` in *The Journal of Prediction Markets* — abstract depth). *Carries under (E7) contracts written on the same event with the
  same settlement source and (E4) participant populations of different
  nationality.*
- Contracts on one US political venue are "chronically mispriced" relative to
  another, with large arbitrage profits in 2016 election markets and non-negligible
  profits in 2020, and the authors attribute part of the distortion to **market
  design** ([Stershic & Gujral 2020](https://doi.org/10.5750/jpm.v14i1.1796), **T1** —
  corrected from T5 under finding LITERATURE-1-3; Crossref records a
  `journal-article` in *The Journal of Prediction Markets* — abstract depth). *Carries under matched contract definitions across the two
  venues and under each venue's own position and fee limits, which the record
  identifies as the design feature doing the work.*
- Historical evidence that the mechanism is old rather than new: large,
  well-organised US presidential betting markets operated from 1868 to 1940, were
  "fairly efficient" despite limited participant information and active
  manipulation attempts, and disappeared largely because of scientific polling and
  competing gambling forms
  ([Rhode & Strumpf 2004](https://doi.org/10.1257/0895330041371277), T1, abstract
  depth). *Carries as a statement about market organization, not about price
  levels; no fee or settlement matching is possible across that time gap.*

### 8.3 Strand S3 — favorite-longshot bias and other systematic mispricings

#### 8.3.1 Kalshi-specific

- **The corpus's most consistent Kalshi finding, and its clearest internal
  disagreement.** A clear favorite-longshot bias is reported on Kalshi:
  low-price contracts win far less often than break-even requires, while
  high-price contracts win more often and yield small positive returns
  ([Bürgi, Deng & Whelan 2025](https://doi.org/10.2139/ssrn.5502658), T5, abstract
  depth). In an unemployment-contract subsample of 287 contracts (July 2021-March
  2026), longshots priced below 0.30 carry a bias of -0.077 (p < 0.001) against an
  actual win rate of 4.0%, with an overall market bias of -0.054 (p = 0.006) and
  well-calibrated favorites
  ([Krause 2026a](https://doi.org/10.2139/ssrn.7110758), T5 preprint, abstract
  depth). A study of 72.1 million Kalshi trades (18.3 billion dollars
  notional, July 2021-November 2025) reports **Kalshi longshots overpriced for all
  sub-25% buckets (p < 0.001)**
  ([Gupta 2026](https://doi.org/10.2139/ssrn.6858200), T5 preprint,
  abstract depth). **Separation-rule repair, finding LITERATURE-1-12:** this line
  previously carried the record's Polymarket arm inside the Kalshi block — "a
  statistically significant bias on both" and "a stated cross-platform contrast in
  sign" — with no carrying assumption. Those are not Kalshi measurements and they
  are moved to 8.3.2 with their assumption. Only the Kalshi-measured part remains
  here.
- **Against those three, one Kalshi record finds no such bias in its segment:** in
  95 CPI contracts across 12 months with 58,138 price observations there is **no
  evidence of the classic favorite-longshot bias**; zero-priced contracts were
  perfectly calibrated at a 0% win rate, and excluding them, contracts priced
  0.01-0.28 show slight overpricing (bias -0.08, p < 0.001) while contracts above
  0.70 are well calibrated (bias -0.03, p = 0.589)
  ([Krause 2026b](https://doi.org/10.2139/ssrn.7087538), T5 preprint, abstract
  depth). **The corpus reports the disagreement and settles nothing**: the records
  differ in contract family (unemployment versus CPI versus all), period, and the
  treatment of zero-priced contracts, and no record in the corpus reconciles them.
- A fourth record makes the measurement itself the problem: with 376.8 million
  Kalshi fills through June 2026, sports contracts went from 0.009% of the
  in-scope sample in calendar 2024 to 58.8% after May 2025, and **41% of the
  aggregate change in the Mincer-Zarnowitz slope at that boundary is composition
  rather than any change in how the market prices risk**, so a naive before/after
  design across early 2025 largely measures the arrival of an asset class
  ([Yurchyna 2026](https://doi.org/10.2139/ssrn.7364100), T5 preprint, abstract
  depth). *This is a methodological warning that applies to every other
  Kalshi-specific line in this strand, and the corpus records it as such.*
- Calibration, not bias: across 594 unique macro markets and 1,860 observations on
  nine series (2025-June 2026) the overall Brier score is 0.0987, a stated 60.5%
  improvement over random guessing, with near-perfect calibration on Federal Funds
  Rate markets (Brier 0.0001) and the poorest on Unemployment Rate markets (Brier
  0.1302) ([Krause 2026c](https://doi.org/10.2139/ssrn.7117919), T5 preprint,
  abstract depth); a companion record covers 2,668 settled contracts on eight
  series from July 2021 to June 2026, grouping them into Federal Reserve,
  inflation and labour categories and testing for the favorite-longshot bias
  ([Krause 2026d](https://doi.org/10.2139/ssrn.7119120), T5 preprint, abstract
  depth). **A concentration caveat the corpus states plainly, corrected under findings
  REV-1-7 and LITERATURE-1-10 to the size it actually has: seven of the nineteen
  Kalshi-specific records come from two author groups — five Krause and two
  "Lee, Lee & Lee" (`10.2139/ssrn.6748186`, `10.2139/ssrn.6964226`) — and
  seventeen of the nineteen are T5 preprints or working papers. The only two
  peer-reviewed-tier Kalshi records in the whole corpus are Goel 2026 and
  Subramanian 2026. This block is not nineteen independent research groups, and it
  is not fifteen-of-nineteen preprint as this record previously said.**
- Underreaction rather than bias: across 41.8 million transactions on 1,496 NBA
  and NFL games matched to play-by-play win-probability benchmarks, prices adjust
  to scoring news only gradually and incompletely within short post-event windows
  ([Lee, Lee & Lee 2026b](https://doi.org/10.2139/ssrn.6964226), T5 preprint,
  abstract depth).

#### 8.3.2 Generalized (each line states the assumption that carries it)

- **Moved here from the Kalshi block by finding LITERATURE-1-12.** The same
  cross-platform record that measures Kalshi longshot overpricing also reports a
  statistically significant bias on **Polymarket**, over 404.5 million Polymarket
  trades, and a stated cross-platform **contrast in sign** between the two venues
  ([Gupta 2026](https://doi.org/10.2139/ssrn.6858200), T5 preprint, abstract
  depth). *The Polymarket arm carries to Kalshi under nothing: it is a measurement
  on a different venue with a different mechanism, a different fee base and a
  permissionless participant population. The cross-platform contrast is a joint
  claim about both venues and is reported here as the record states it, with the
  Kalshi half of it stated in 8.3.1 and the contrast itself carried by neither
  block alone. This corpus draws no conclusion about the sign difference.*
- The anomaly statement itself: wagering markets are better suited than stock
  markets to testing efficiency and rationality because each bet has a
  **well-defined termination point at which its value becomes certain**
  ([Thaler & Ziemba 1988](https://doi.org/10.1257/jep.2.2.161), T1, abstract
  depth). *This is the property that makes the whole binary-contract literature
  transferable at all, and it holds at any venue whose contract settles at an
  endpoint.* **Whether Kalshi is such a venue is NOT established by this corpus,
  and the sentence that said it was is withdrawn (findings REV-1-3, QUANT-1-5,
  LITERATURE-1-4).** The previous wording read "which the CFTC record establishes
  for Kalshi as a class of instrument (section 9)". Section 9 establishes only
  that "Kalshi" appears in the CFTC's designated-contract-market industry-filings
  table with status Designated and date 11/03/2020 (S7-1), that the Commission
  granted a petition to modify its Order of Designation to permit intermediated
  futures trading on 2025-01-17 (S7-2), and the counts and titles of matching
  Federal Register documents (S7-3, S7-4). S7-1's own "may it license a
  behavioural claim?" cell reads: *"No. It fixes the venue's regulatory category
  and its designation date, nothing else."* The settlement rule for any listed
  Kalshi contract is recorded as **Not established** at S7-5, and the eCFR text at
  S7-6. **Designated Contract Market is a regulatory category, not a settlement
  specification.** This transfer is therefore marked
  `not-transferable-as-stated` and is pending the document named at TC-1; it is
  counted in gap G-3.
- Competing explanations are separable empirically: tests over a wider choice set
  including exacta, quinella and trifecta pools discriminate risk-love from
  misperception explanations of the bias
  ([Snowberg & Wolfers 2010](https://doi.org/10.1086/655844), T1, abstract depth).
  *Carries only to venues offering compound bets over the same outcome space
  (E6 parimutuel pools with exotic pools); an exchange listing only single binary
  claims does not admit the test as stated.*
- A mechanism-tied prediction: the expected return on an outcome tends to increase
  in the fraction of bets laid on it, and the **direction and extent** of the bias
  depend on the ratio of private information to noise, itself a function of the
  number of bettors, the number of outcomes, the amount of private information,
  recreational participation, bet divisibility and ex post noise
  ([Ottaviani & Sørensen 2010](https://doi.org/10.1257/mic.2.1.58), T1, abstract
  depth). *Carries to a parimutuel mechanism as stated; transfer to an order book
  requires an argument the record does not supply, but the named drivers
  (participant mix, outcome count, recreational share) are observable in principle
  at any venue.*
- A supply-side explanation: in sports gambling the bookmaker announces a price and
  adjusts it little, taking large positions rather than matching buyers and
  sellers, and this price-setting mechanism achieves substantially higher profits
  because bookmakers predict outcomes better than bettors and choose prices that
  deviate from the market-clearing price to exploit bettor biases
  ([Levitt 2004](https://doi.org/10.1111/j.1468-0297.2004.00207.x), T1, abstract
  depth). *Carries only to (E6) a bookmaker book.* **What this corpus can and
  cannot say about the other side of that comparison, corrected under finding
  REV-1-2 (critical).** The previous wording read: "Kalshi is an order-driven
  exchange in the CFTC record's own designation category (section 9), so the
  supply-side channel as stated does not transfer", and called that "the single
  largest structural reason the sportsbook FLB literature must not be restated as
  a Kalshi finding". **The premise is not established.** Designated Contract
  Market is a regulatory category; it does not specify a trading mechanism, and
  S7-5 records Kalshi's contract specifications, settlement and adjudication rules
  as **Not established**. The record also asserted the opposite mechanism 80 lines
  later, at 8.4.1, where the venue was called quote-driven — two mutually
  exclusive venue facts in one section, neither retrieved. **The venue-mechanism
  assertion is removed from both sites.** Whether the Levitt supply-side channel
  transfers to Kalshi turns on Kalshi's E6, which this corpus did not retrieve
  (AG-1), so the transfer is marked `not-transferable-as-stated` and counted in
  gap G-3. What survives is weaker and is all this corpus has: the Levitt
  mechanism requires a price-setting intermediary taking the other side, and **no
  record in this corpus establishes that Kalshi has one or does not.**
- An information-based supply-side variant: a bookmaker requires a premium for
  quoting odds days before an event, reflecting the uncertainty of public
  information exploitable by expert bettors, which yields expected returns to
  bettors increasing monotonically in winning probability — an
  **information-based** derivation of the favourite-longshot bias
  ([Makropoulou & Markellos 2011](https://doi.org/10.1111/j.1467-9485.2011.00557.x),
  T1, abstract depth). *Same bookmaker carrying assumption.*
- An imperfect-competition explanation: favourite-longshot bias can emerge from
  bookmaking markets being imperfectly competitive, because when people disagree
  about outcome probabilities the demand for longshot bets is less sensitive to
  odds than the demand for favourites; the claim is tested on odds from over
  150,000 European soccer games in two different market structures
  ([Hegarty & Whelan 2025](https://doi.org/10.1093/oep/gpaf023), T1, abstract depth).
  *Carries under (E6) bookmaking with market power; an exchange with many
  competing makers is a different competitive structure and the record's own
  comparison is what identifies the effect.*
- An insider-trading explanation: prices of state-contingent claims in the presence
  of insider traders produce the favourite-longshot bias
  ([Shin 1992](https://doi.org/10.2307/2234526), T1, abstract depth).
  *Carries wherever a quote-setter faces informed order flow.* **Downgraded
  under finding REV-1-4.** The previous wording said the Kalshi adverse-selection
  evidence in 8.4.1 "establishes" that this is the case on the venue, and called
  the link "the corpus's strongest cross-strand link". What 8.4.1 actually holds is
  **one T5 preprint, read at abstract depth**, reporting informed price impact on
  Kalshi ([Bartlett & O'Hara 2026](https://doi.org/10.2139/ssrn.6615739)).
  "Establishes" is the settled-claim verb, and the frozen protocol's tier rule is
  tier-blind admission with **tier-labelled use**, under which no preprint-tier
  claim is reported as settled. Restated: *if that measurement holds, the Shin
  mechanism's precondition is met on the venue. This corpus does not treat a single
  preprint-tier abstract as establishing the precondition, and the cross-strand
  link is recorded as a hypothesis for a successor stage, not as a result.* The
  chain was compounded: it licensed the Shin insider-trading mechanism onto Kalshi
  at the same time that 8.3.2's Berkowitz line states that odds-with-embedded-margin
  results do not carry to a cent-denominated exchange.
- A risk-management explanation: a bookmaker facing unbalanced liability exposures
  and noisy betting demands sets odds to influence betting flow, and the
  favourite-longshot bias arises from the model **only under specific
  assumptions** ([Hodges, Lin & Liu 2013](https://doi.org/10.1111/j.1468-036x.2010.00601.x),
  T1, abstract depth). *The record's own qualification is the carrying assumption
  and is recorded as stated.*
- Both directions of the bias are present in the literature: a review concludes the
  evidence is consistent with the average sports bettor exhibiting **both**
  longshot bias and favorite bias, with the direction depending on market
  structure ([Newall & Cortis 2021](https://doi.org/10.3390/risks9010022), T1,
  abstract depth). *Carries as a statement about the literature, not about any
  venue; it is the reason this corpus does not report a single sign for the bias.*
- The surveys that frame the strand: a state-of-the-art review of racetrack and
  lottery markets covering arbitrage and risk arbitrage, syndicates, betting
  exchange rebates, behavioural biases and mispricing information
  ([Ziemba 2023](https://doi.org/10.1146/annurev-financial-053122-021925), T1,
  abstract depth); an overview of the main explanations of the bias
  ([Ottaviani & Sørensen 2008](https://doi.org/10.1016/b978-044450744-0.50009-3),
  T1, metadata depth); a unification of the bias with other market anomalies
  ([Sobel & Ryan 2008](https://doi.org/10.1016/b978-044450744-0.50011-1),
  T1, metadata depth); and an introduction to win-market efficiency and the bias
  ([Hausch, Lo & Ziemba 2008](https://doi.org/10.1142/9789812819192_0025), T1,
  abstract depth). *All four are used for their framing and their bibliography,
  not as primary evidence, per the protocol's treatment of survey-tier records.*

### 8.4 Strand S4 — market making, inventory risk, market scoring rules, automated market makers

This is the largest strand in the corpus (61 of 149 records) and the one where the
frozen protocol's **transfer clause** does the most work. Two sub-literatures sit
here and they must not be run together: the **event-market market-maker design**
literature, which is written natively for bounded [0,1] payoffs settling at an
endpoint, and the **inventory-risk dealer** lineage, which is written for
unbounded-payoff instruments and reaches this corpus only as a model whose
transfer must be argued.

**The corpus's central S4 finding, restated to the size the corpus can carry
(finding LITERATURE-1-14).** The previous wording was: "the first literature
states its own applicability conditions in terms of the binary payoff, and the
second does not." The second half is a positive claim about non-statement, and the
corpus cannot make it. Corrected: **among the records this corpus assessed, and at
the extraction depth it reached, the first literature states its applicability
conditions in terms of the binary payoff and the second does not.** The
qualifications are not decorative. Of the five named-lineage anchors in 8.4.3,
**four were read at metadata depth only** (Ho & Stoll, Glosten & Milgrom, Kyle,
Krishnan, Liu & Wang) with transfer status "not addressed **at the depth
reached**"; gap G-5 states in terms that "the corpus cannot say whether the
originals address bounded payoffs, because it did not read them"; and **700 X11
records — transfer-clause records of exactly this class — were never assessed at
all** (section 6, section 13.2). Amendment A5 records that the transfer-clause
literature is represented here "by its anchors and its event-market-facing members
only". A reader wanting to know whether the inventory-risk lineage states a payoff
support must read those 700 rows of the verdicts file, not this section.

#### 8.4.1 Kalshi-specific

- Adverse selection is measured on the venue and is contract-family-dependent:
  using 41.6 million trades and adaptations of Kyle's lambda and the
  Glosten-Harris decomposition, **single-name markets exhibit greater informed
  price impact than broad-based markets**; yet effective spreads are only modestly
  wider and market makers earn twice as much per contract. The record resolves
  that tension with a frequency-magnitude decomposition: traders systematically
  overbet YES in markets that predominantly settle NO, generating a **behavioural
  surplus that cross-subsidizes adverse selection**. An adapted VPIN toxicity
  metric predicts maker losses in single-name markets but not broad-based ones
  ([Bartlett & O'Hara 2026](https://doi.org/10.2139/ssrn.6615739), T5 preprint,
  abstract depth). *This is the corpus's single most important Kalshi-specific
  result for S4, and note what it is: the classical inventory/adverse-selection
  apparatus is applied to the venue by adapting Kyle and Glosten-Harris — the
  transfer is performed by that record's authors, not by this corpus.*
- Maker-taker structure and who earns: **one record characterises the venue as
  quote-driven** and interprets makers through that characterisation as relatively
  well-informed traders who post offers and seek positive expected returns ([Bürgi, Deng & Whelan 2025](https://doi.org/10.2139/ssrn.5502658),
  T5, abstract depth). **Attribution, finding REV-1-2:** "quote-driven" is
  stated here as *what that record says*, not as a fact about the venue. This
  corpus does not know Kalshi's trading mechanism: the rulebook was unreachable
  (AG-1) and S7-5 records the contract specifications as Not established. The same
  record's characterisation is also in direct tension with 8.3.2's former
  order-driven assertion, now withdrawn, and with 8.4.2's former attribution of a
  continuous double auction to the CFTC record, also now withdrawn. **The corpus
  reports the tension and settles nothing.** A separate record decomposes 72.1
  million Kalshi trades to ask whether liquidity providers systematically profit
  from uninformed order flow
  ([Gupta 2026](https://doi.org/10.2139/ssrn.6858200), T5 preprint, abstract
  depth).
- **No retrieved abstract among the 116 abstract-depth included records states a
  market-making model fitted to, or calibrated on, Kalshi**, and the Kalshi block
  of S4 is entirely measurement while the model block below is entirely venue-none
  or other-venue. **Qualified under finding REV-1-10**, because the previous
  wording was a universal negative over the corpus and this corpus cannot make one:
  the **33 metadata-depth** included records were never read past title, venue and
  year; the **545 X10** and **700 X11** records were never assessed; and the
  **5,249 records** verdicted by the amendment-A3 token rule were never read at
  all. A record can fit a model to Kalshi without saying so in an abstract, which is
  the exact "not mentioned versus not stated in the abstract" indistinguishability
  declared at 13.2. The asymmetry is carried into section 10 as gap G-4 with the
  same qualifiers attached there.

#### 8.4.2 Generalized, part one — market makers written natively for bounded [0,1] payoffs

These records are **venue-none** and their applicability conditions are stated in
terms of the binary-payoff structure itself, so the transfer question for them is
about the *venue's mechanism*, not about the payoff support.

- The lineage's origin: market scoring rules combine the individual-elicitation
  property of scoring rules with the group-consensus property of betting markets,
  and only **logarithmic** versions preserve the probability of a conditioning
  event and hence conditional independence relations — the stated reason LMSR is
  the modular choice ([Hanson 2007](https://doi.org/10.5750/jpm.v1i1.417), T1,
  abstract depth; combinatorial design in
  [Hanson 2003](https://doi.org/10.1023/A:1022058209073), T1, metadata depth).
  *Applicability condition stated by the author: contracts on combinations of base
  events whose conditional structure is to be preserved.*
- The utility characterization: utility-based market makers that always accept
  orders at their risk-neutral prices have **bounded loss** under necessary and
  sufficient conditions the record derives; hyperbolic-absolute-risk-aversion
  utility makers are equivalent to weighted pseudospherical scoring-rule makers,
  and Hanson's LMSR maker corresponds to a negative-exponential utility maker.
  The record states the **tradeoff between market liquidity and worst-case loss**
  explicitly ([Chen & Pennock 2007](https://arxiv.org/abs/1206.5252), **T1**, UAI
  2007 proceedings, retrieved as arXiv:1206.5252, abstract depth). *Transfer
  status: `addressed` — the bounded payoff is the premise, not an assumption to be
  relaxed.* **Corrected 2026-09-02, finding LITERATURE-2-4:** this was cited as a
  2012 T5 preprint. arXiv:1206.5252 is the 2012 bulk upload of the UAI proceedings;
  the arXiv record's own **report number is `UAI-P-2007-PG-49-56`** and its Comments
  field reads *"Appears in Proceedings of the Twenty-Third Conference on Uncertainty
  in Artificial Intelligence (UAI2007)"*. The work is a peer-reviewed conference
  paper, so it is **T1**, and the arXiv posting is the retrieved manifestation, not
  the work.
- The convex-analytic characterization: any market satisfying a stated set of
  conditions **must** price securities via a convex cost function constructed by
  conjugate duality, which reduces automated market making to convex optimization
  over a convex hull rather than over the outcome space
  ([Abernethy, Chen & Vaughan 2013](https://doi.org/10.1145/2465769.2465777), T1,
  abstract depth); the framework's precursor is
  [Abernethy, Chen & Wortman Vaughan 2011](https://doi.org/10.1145/1993574.1993621)
  (T1, abstract depth), its axioms are extended to adaptive liquidity by
  [Li & Vaughan 2013](https://doi.org/10.1145/2482540.2482575) (T1, abstract
  depth), to measurable spaces and continuous random variables by
  [Chen, Ruberry & Wortman Vaughan 2013](https://doi.org/10.1145/2482540.2482608)
  (T1, abstract depth), and connected to risk measures and exponential families by
  [Abernethy, Frongillo & Kutty 2015](https://doi.org/10.1145/2728732.2728734)
  (T1, abstract depth). *Applicability condition stated across the set: securities
  with **bounded payoff** over a possibly infinite outcome space.*
- The learning-theoretic equivalence: any cost-function-based prediction market can
  be read as an algorithm for learning from expert advice, and a bound on the
  market organizer's loss yields a regret bound of order square-root-T for the
  corresponding learning algorithm
  ([Chen & Vaughan 2010](https://doi.org/10.1145/1807342.1807372), T1, abstract
  depth). *Applicability condition: the market's outcome set is the learning
  problem's expert set — a structural correspondence, not a market assumption.*
- The impossibility results that bound the design space: LMSR pricing over
  combinatorial outcome spaces is `#P`-hard even under severely restricted betting
  languages, and even where matching without a market maker is polynomial
  ([Chen, Fortnow, Lambert, Pennock & Wortman 2008](https://doi.org/10.1145/1386790.1386822), T1,
  abstract depth); and continuous-outcome market makers cannot satisfy a set of
  desirable axioms simultaneously
  ([Gao & Chen 2010](https://doi.org/10.1007/978-3-642-17572-5_44), T1, abstract
  depth). *These are the corpus's clearest statements of what a binary-contract
  market maker cannot be asked to do.*
- The four-desiderata result: bounded loss, ability to profit, vanishing bid/ask
  spread and unlimited market depth were previously attainable only three at a
  time; the record constructs makers satisfying **all four** by extending
  constant-utility cost functions with two added functions on the quoted prices
  ([Othman & Sandholm 2012](https://doi.org/10.1145/2229012.2229074), T1, abstract
  depth). Practical liquidity sensitivity plus the ability to run at a profit,
  rather than at a deficit, is the stated defect the practical liquidity-sensitive
  maker repairs
  ([Othman, Pennock, Reeves & Sandholm 2013](https://doi.org/10.1145/2509413.2509414),
  T1, abstract depth), with a risk-measure formulation in
  [Othman & Sandholm 2011](https://doi.org/10.1007/978-3-642-25510-6_27) (T1,
  metadata depth). *Applicability condition stated by the authors: the maker's
  loss bound and profit property are properties of the cost function, and hold for
  any bounded-payoff security set.*
- Unification and generalization: a convex-optimization framework expresses LMSR,
  cost-function makers, utility-based markets and the sequential convex parimutuel
  mechanism as one model differing only in the choice of a concave value function,
  equivalent to convex risk minimization for the market maker
  ([Agrawal, Delage, Peters, Wang & Ye 2011](https://doi.org/10.1287/opre.1110.0922),
  T1, abstract depth); a volume-parameterized framework prices on liabilities
  **and** total traded volume and recovers cost-function, profit-charging and
  buy-only markets as special cases
  ([Abernethy, Frongillo, Li & Vaughan 2014](https://doi.org/10.1145/2600057.2602900),
  T1, abstract depth); a multivariate-utility mechanism unifies several schemes and
  yields convergence results whose limiting wealth distribution lies on the Pareto
  frontier of participants' utilities
  ([Gao, Wang, Wu & Yu 2025](https://doi.org/10.1287/opre.2022.0417), T1, abstract
  depth); and convergence within **binary** market scoring rules is characterized
  in [Tarnaud 2018](https://doi.org/10.1007/s00199-018-1155-3) (T1, metadata
  depth).
- Combinatorial and structured contracts: a tractable combinatorial maker sits
  between independent securities and full combinatorial pricing using convex
  optimization with constraint generation
  ([Dudik, Lahaie & Pennock 2012](https://doi.org/10.1145/2229012.2229047), T1,
  abstract depth); interval securities over a continuous variable are priced in
  **logarithmic** time in the number of intervals, replicating LMSR exponentially
  faster ([Dudík, Wang, Pennock et al. 2021](https://doi.org/10.65109/bbzi6501),
  T1, abstract depth); and the parlay problem — the full combinatorial family of
  joint contracts on M binary events with maker loss bounded at order M-squared —
  is solved in [Moshrefi, Rana & Viswanath 2026](https://arxiv.org/abs/2607.18299)
  (T5 preprint, abstract depth) and, via a shared pairwise exponential-family
  belief state so that all base and parlay prices are marginals of one coherent
  distribution, in
  [Rana, Nadkarni, Moshrefi & Viswanath 2026](https://doi.org/10.48550/arxiv.2603.22596) (T5
  preprint, abstract depth). *The second of these is the corpus's only explicit
  link between a market-maker design and the S1 coherence condition: the design
  enforces coherence by construction rather than leaving it to arbitrageurs.*
- The DeFi bridge, stated as an equivalence rather than an analogy: **every
  constant-function market maker with a concave potential on n assets is
  equivalent to a cost-function prediction market on n outcomes**, and the
  construction converts one into the other in both directions
  ([Frongillo, Papireddygari & Waggoner 2023](https://doi.org/10.48550/arxiv.2302.00196),
  T5 preprint, abstract depth). *This is why the corpus excludes token-pair
  constant-function-market-maker records under X5 while still admitting their
  apparatus: the transfer is licensed by a stated equivalence theorem, not by
  resemblance.* The loss-versus-rebalancing apparatus is carried across the same
  bridge to define **uniform** automated market makers whose instantaneous loss is
  proportional to pool value and independent of the current price, for the class of
  win-martingales ([Moallemi, Robinson & Zhu 2026](https://arxiv.org/abs/2607.17428),
  T5 preprint, abstract depth).
- Liquidity as a decision rather than a constant: liquidity is fixed ex ante in
  existing mechanisms, which enforces a static trade-off between price
  responsiveness and worst-case loss; treating liquidity selection as an online
  learning problem mixes a family of cost-function markets with learnable weights
  and is stated to preserve **no-arbitrage**, bounded worst-case loss,
  expressiveness and positive upside
  ([Nueve, Nguyen, Frongillo & Waggoner 2026](https://doi.org/10.48550/arxiv.2605.09599), T5
  preprint, abstract depth); liquidity provisioning by third parties in
  cost-function markets is generalized in
  [Bhaskara, Frongillo, Lindgren & Papireddygari 2023](https://arxiv.org/abs/2311.08725) (T5
  preprint, abstract depth); the smooth quadratic market incentivizes collective
  steepest gradient descent with a better worst-case monetary loss for
  Arrow-Debreu securities
  ([Nueve & Waggoner 2025](https://doi.org/10.48550/arxiv.2505.02959), T5
  preprint, abstract depth); and the LMSR liquidity parameter `b` is studied as a
  design decision in its own right
  ([Lekwijit & Sutivong 2018](https://doi.org/10.1108/jm2-06-2017-0066), T1,
  abstract depth). **Convention note:** these records treat the liquidity
  parameter as a quantity to be chosen by a stated criterion, which is the posture
  CLAUDE.md requires of any tunable value; this corpus adopts none of their
  numerical settings.
- **The one record in the corpus that solves the market-making control problem
  natively for the binary settlement structure**: because prediction-market
  settlement is binary, optimal market making "leads to an optimization problem
  that is fundamentally different from the ones studied in classical settings";
  the record models the market price as a conditional probability generated by a
  transformed latent belief diffusion and has the maker choose bid and ask quotes
  to maximize expected terminal wealth
  ([Feil & Nendel 2026](https://arxiv.org/abs/2607.17991), T5 preprint, abstract
  depth). *This is the corpus's direct answer to review-question item (d): the
  difference from the classical inventory problem is asserted by the authors and
  is the premise of their formulation.* A companion attempt at a unifying kernel
  proposes a logit jump-diffusion with risk-neutral drift treating the traded
  probability as a Q-martingale, exposing belief volatility, jump intensity and
  dependence as quotable risk factors
  ([Dalen 2025](https://doi.org/10.48550/arxiv.2510.15205), T5 preprint, abstract
  depth).
- Mechanism comparisons on event markets: a simulation comparison of four applied
  automated market makers reports that logarithmic scoring rules and the dynamic
  parimutuel mechanism perform best on the record's criteria
  ([Slamka, Skiera & Spann 2013](https://doi.org/10.1109/tem.2012.2191618), T1,
  abstract depth); a live-trading experimental design compares two microstructures
  with the same trading population
  ([Brahma, Das & Magdon-Ismail 2010](https://doi.org/10.48550/arxiv.1009.1446),
  T5 preprint, abstract depth); LMSR is integrated into a continuous double auction
  with a self-contained algorithm requiring no special-purpose specification
  ([Chakraborty, Das & Peabody 2015](https://doi.org/10.1609/aaai.v29i1.9313), T1,
  abstract depth); and the dynamic parimutuel market is introduced as a hybrid
  offering infinite buy-in liquidity and zero institutional risk while still
  reacting continuously to information
  ([Pennock 2004](https://doi.org/10.1145/988772.988799), T1, abstract depth).
  *The mechanism comparison is the transfer question in its operational form: a
  result proved for a dealer-style scoring-rule maker does not automatically hold
  in a continuous double auction.* **Corrected under findings QUANT-1-5 and
  LITERATURE-1-4:** the previous wording ended "...which is the microstructure the
  CFTC record associates with a designated contract market". It does not. The
  retrieved CFTC pages carry a designation status, a designation date and an
  intermediation-permission change, and nothing about matching, quoting or order
  handling; S7-5 records contract specifications as Not established. **This corpus
  does not know which microstructure Kalshi runs**, so the mechanism-comparison
  transfer is marked `not-transferable-as-stated` and counted in gap G-3.
- The parimutuel-as-microstructure statement: parimutuel trading is a call auction
  with non-continuous trading, riskless funding of payouts from the amounts
  wagered, and equilibrium conditions requiring relative claim prices to equal
  relative aggregate amounts wagered
  ([Lange & Economides 2005](https://doi.org/10.1111/j.1354-7798.2005.00274.x), T1,
  abstract depth), with mechanism and performance analysis in
  [Peters, So & Ye 2007](https://doi.org/10.1007/978-3-540-77105-0_11) (T1,
  metadata depth). *These state the E6 boundary explicitly and are the corpus's
  basis for refusing to carry parimutuel results into order-book settings without
  an argument.*
- The quadratic market scoring rule provides **uniform liquidity across the
  probability spectrum**, unlike the logarithmic rule
  ([Abramovicz 2007](https://doi.org/10.5750/jpm.v1i2.423), **T1** — corrected
  from T5 under finding LITERATURE-1-3; Crossref records a `journal-article` in
  *The Journal of Prediction Markets* — abstract depth).
  *Directly relevant to a venue listing contracts at extreme prices, and the corpus
  notes it alongside the Kalshi zero-price-contract finding in 8.3.1 without
  asserting a link neither record makes.*

#### 8.4.3 Generalized, part two — the inventory-risk lineage, transfer status recorded per record

- **Ho & Stoll 1981** — optimal dealer pricing under transactions and return
  uncertainty ([doi:10.1016/0304-405X(81)90020-9](https://doi.org/10.1016/0304-405X(81)90020-9),
  T1, **metadata depth: no abstract was returned by any source**). Transfer status:
  **not addressed** — nothing in the retrieved metadata states a payoff support,
  and the corpus therefore records that the transfer clause has nothing to work
  with at the depth reached. It is retained as a named-lineage anchor, not as
  evidence about binary contracts.
- **Glosten & Milgrom 1985** — bid, ask and transaction prices in a specialist
  market with heterogeneously informed traders
  ([doi:10.1016/0304-405X(85)90044-3](https://doi.org/10.1016/0304-405X(85)90044-3),
  T1, **metadata depth**). Transfer status: **not addressed** at the depth reached.
  **The transfer sentence that stood here is withdrawn (finding
  LITERATURE-1-5).** It read that the corpus "records that its apparatus *has*
  been transferred to a binary event venue by others — the Kalshi adverse-selection
  record adapts the Glosten-Harris decomposition (8.4.1)". That is an attribution
  bridge built on a shared surname. **Glosten & Harris (1988), *Estimating the
  components of the bid/ask spread*, JFE 21(1), `10.1016/0304-405X(88)90034-7`, is
  a different paper by a different author pair from Glosten & Milgrom (1985)**: an
  empirical spread-decomposition regression, not a sequential-trade
  adverse-selection model. What Bartlett & O'Hara adapt at 8.4.1 is the
  Glosten-Harris decomposition. **Glosten & Harris 1988 is not in this
  149-record corpus**, so this corpus records no transfer of the Glosten &
  Milgrom apparatus to a binary event venue at all. The parallel move made for
  Kyle two entries below is sound, because Kyle's lambda does come from Kyle 1985;
  this one was not, and it is removed rather than softened.
- **Kyle 1985** — continuous auctions and insider trading
  ([doi:10.2307/1913210](https://doi.org/10.2307/1913210), T1, **metadata
  depth**). Transfer status: **not addressed** at the depth reached. The corpus
  does record that Kyle's own apparatus has been carried to the venue by others —
  Bartlett & O'Hara adapt **Kyle's lambda** to Kalshi at 8.4.1, and lambda is
  Kyle's construct — so unlike the Glosten & Milgrom entry above, this attribution
  bridge holds. The transfer is still performed by that record's authors, not by
  this corpus, and this corpus did not read Kyle's own statement of applicability.
- **Avellaneda & Stoikov 2008** — the dealer's role is to provide liquidity by
  quoting bid and ask prices at which he will buy and sell a specific quantity
  ([doi:10.1080/14697680701381228](https://doi.org/10.1080/14697680701381228), T1,
  abstract depth, abstract truncated by the publisher at the retrieved length).
  Transfer status: **not addressed** — the retrieved text states a securities-market
  setting and no bounded-payoff condition.
- **Guéant, Lehalle & Fernandez-Tapia 2012** — the maker's return from the quoted
  spread and the frequency of providing liquidity is challenged by the price risk
  of the inventory; the market is modelled with a **reference price following a
  Brownian motion** with standard deviation sigma, arrival rates of
  liquidity-consuming orders depending on distance to the reference price, and the
  maker maximizing expected utility of profit and loss over a finite horizon
  ([doi:10.1007/s11579-012-0087-0](https://doi.org/10.1007/s11579-012-0087-0), T1,
  abstract depth). Transfer status: **explicitly excluded by the stated model** —
  a Brownian reference price is unbounded and cannot be a [0,1] probability that
  must terminate at an endpoint, so this model as stated does not apply to a
  binary event contract. *This is the corpus's cleanest instance of the transfer
  clause biting, and it is the reason the S4 native literature in 8.4.2 exists as
  a separate lineage.*
- **The two frameworks are one framework.** A small set of axioms on the maker's
  dynamic preference functional — cash-additivity, normalization, concavity, strong
  dynamic consistency and law-invariance — forces the functional to be the entropic
  certainty-equivalent on liquidation-adjusted terminal wealth with a **single**
  positive parameter, so the Cartea-Jaimungal running-penalty coefficient and the
  Avellaneda-Stoikov risk-aversion parameter are **not independent** and must not
  be calibrated separately ([Feys 2026](https://arxiv.org/abs/2606.01477), T5
  preprint, abstract depth). *This is a parameter-identification statement, and it
  is the corpus's most directly usable warning for any future empirical stage: two
  parameters routinely fitted independently are, under those axioms, one
  parameter.*
- Learning and equilibrium bridges within the lineage: a **learning** market maker
  extends Glosten-Milgrom, tracking a changing true value with informed traders
  receiving noisy signals ([Das 2005](https://doi.org/10.1080/14697680500148067),
  T1, abstract depth); the Kyle and Glosten-Milgrom models are shown equivalent
  ([Krishnan 1992](https://doi.org/10.1016/0165-1765(92)90014-p), T1, metadata
  depth) and unified when the informed trader optimizes his times of trading
  ([Back & Baruch 2004](https://doi.org/10.1111/j.1468-0262.2004.00497.x), T1,
  abstract depth); market making with asymmetric information **and** inventory
  risk is treated jointly in [Liu & Wang 2016](https://doi.org/10.1016/j.jet.2016.01.005)
  (T1, metadata depth); two risk-averse makers sharing clearing risk in a
  Kyle-type batch model produce a linear aggregate pricing schedule that inventory
  shifts vertically and the coalition parameter tilts
  ([Tanaka 2005](https://doi.org/10.11179/ker.74.119), T1, abstract depth); and
  market-making profitability is characterized without stochastic assumptions on
  price evolution, exhibiting a trade-off between local price fluctuation and
  adverse drift ([Chakraborty & Kearns 2011](https://doi.org/10.1145/1993574.1993622),
  T1, abstract depth). *All are transfer-clause records; none states a
  bounded-payoff condition at the depth reached.*
- The empirical inventory result that contradicts the models: futures transaction
  data show traders control inventory throughout the day, yet the correlation
  between inventory and reservation prices is **positive**, contradicting the
  negative relation inventory-control models predict
  ([Manaster & Mann 1996](https://doi.org/10.1093/rfs/9.3.953), T1, abstract
  depth). *Recorded as a standing disagreement inside the lineage, on futures data;
  it is not transferred to event contracts here.*
- The betting-venue market-making models, which sit between the two lineages: a
  bookmaker faces sophisticated bettors and can be manipulated through information
  asymmetry, and the record derives how to set spread lines as prices
  ([Birge, Feng, Keskin & Schultz 2021](https://doi.org/10.1287/opre.2021.2109),
  T1, abstract depth); optimal price setting under information uncertainty gives an
  information-based derivation of the favourite-longshot bias
  ([Makropoulou & Markellos 2011](https://doi.org/10.1111/j.1467-9485.2011.00557.x),
  T1, abstract depth); and a bookmaker facing stochastic betting demands sets odds
  to influence flow and mitigate unbalanced liability
  ([Hodges, Lin & Liu 2013](https://doi.org/10.1111/j.1468-036x.2010.00601.x), T1,
  abstract depth). *Transfer status: `addressed` for the payoff support — these are
  state-contingent claims with endpoint settlement — but the mechanism is a
  bookmaker book, so **E6 blocks the transfer to any order-driven venue; whether the
  venue of interest is one is not established** (S7-5 `Not established`, AG-1), and
  the determination therefore reads `not-transferable-as-stated` rather than
  `blocked`.* **Conditioned 2026-09-02 under finding REV-2-8**, which found this a
  residual venue-mechanism presupposition surviving the REV-1-2 fix: the clause
  previously read "so E6 blocks the transfer to an order-driven exchange", asserting
  the venue's mechanism at the site where the conclusion turns on it. It is the
  sixth mark in the G-3 table.
- Liquidity provision measured on event venues: an automated maker engaging in
  zero-profit **cross-arbitrage** in multi-contract markets is proposed as a way to
  supply artificial liquidity in a continuous double auction, with an empirical
  analysis of observed spreads, offer acceptance and order sizes on an election
  market ([Antweiler 2013](https://doi.org/10.5750/jpm.v7i3.824), T1, abstract
  depth); and traders are observed taking the market-maker role in a sports
  prediction market where arbitrage was studied
  ([Luckner & Weinhardt 2008](https://doi.org/10.1109/cecandeee.2008.131), T1,
  abstract depth). *These are the corpus's only records that join the maker
  question to the coherence question on an operating event venue.*

### 8.5 Strand S5 — transaction costs, fees, collateral, capital lockup, executability

**This strand is the corpus's weakest, and the weakness is structural.** The
review question asks what determines whether a stated discrepancy is
*executable*. The literature that measures discrepancies rarely nets them against
a fully specified friction set, and the frozen protocol's field E12 exists to
record what is modelled, what is assumed away and what is **not mentioned** —
"not mentioned" being the usual reason a paper discrepancy is not an executable
one. At the extraction depth reached, E12 could be completed only where an
abstract named a friction; for the majority of this strand the honest E12 entry
is **not determinable at abstract depth**.

#### 8.5.1 Kalshi-specific

- A named fee magnitude enters the corpus once, and second-hand: the
  cross-venue falsification states a **2.00-cent Kalshi fee** as the threshold its
  edge must clear ([Moulinier 2026](https://doi.org/10.2139/ssrn.7170178), T5
  preprint, abstract depth). **J5 flag:** this is a venue-structural claim inside a
  research record. The protocol requires it to be checked against the
  documentation-tier source before this corpus states it. **That check could not
  be performed** — the filer-published rulebook and fee schedule were unreachable
  (AG-1, section 9). The figure is therefore reported **as the record states it**,
  flagged second-hand and unverified, and this corpus does not assert it as
  Kalshi's fee.
- A second record reconstructs the venue's fee schedule from **sixteen dated
  captures of its own published document** and reports a finding about the 2025
  maker fee ([Yurchyna 2026](https://doi.org/10.2139/ssrn.7364100), T5 preprint,
  abstract depth, abstract truncated before the numeric value). **J5 flag, same
  disposition**: second-hand, unverified against the documentation tier, and the
  numeric value is not stated here because the retrieved abstract does not carry
  it. *That a researcher had to reconstruct the fee schedule from dated captures
  is itself the corpus's most informative statement about the S5 evidence base:
  the fee schedule is a moving, filer-published object.*
- Execution rather than information as the source of returns is asserted by title
  in [Della Vedova 2026](https://doi.org/10.2139/ssrn.6191618) (T5 preprint,
  **metadata depth — no abstract retrieved**), and skilled liquidity provision
  across 150 million trades in [Yang 2026](https://doi.org/10.2139/ssrn.6396698)
  (T5 preprint, **metadata depth**). Both are on-point for O5 and **neither can be
  reported beyond its title at the depth reached**; they are named so the reader
  knows they exist and knows this corpus did not read them.

#### 8.5.2 Generalized (each line states the assumption that carries it)

- The friction that decides the parimutuel case is the **minimum betting unit plus
  the price impact of one's own bet on the pool odds**, and netting them reduces
  arbitrage from a screen-level phenomenon to 2 races in 175
  ([Ashiya 2013](https://doi.org/10.1177/1527002513493630), T1, abstract depth).
  *Carries only to parimutuel pools; the order-book analogue is depth, and this
  corpus has no record that performs the same netting on an order book at a
  CFTC-designated contract market.*
- The friction that decides the bookmaker case is **not a price at all** but the
  bookmaker's right to restrict or refuse the informed customer
  ([Grant, Oikonomidis, Bruce & Johnson 2018](https://doi.org/10.1080/1351847x.2018.1443148),
  T1, abstract depth). *Carries to any venue with participant-conduct rules; the
  corresponding Kalshi rules are exactly what AG-1 blocked.*
- Bookmaker margins vary across matches, time and firms, and match, tournament and
  player characteristics explain the variation, so **intermediation cost is
  itself a modelled quantity** in a market for state-contingent assets
  ([Lyócsa & Fedorko 2015](https://doi.org/10.1080/00036846.2015.1111993), T1,
  abstract depth). *Carries under (E6) fixed-odds bookmaking with an embedded
  margin.*
- Taxation changes the odds and the intermediary's payoff in a way that depends on
  the **taxation base**: a gross-profit tax and a volume-based betting duty are
  characterized in subgame-perfect equilibrium for fixed-odds, spread and
  parimutuel bets, and the record states that taxing gross profit maximizes the
  utilitarian objective ([Vidal-Puga 2017](https://doi.org/10.1007/s13209-017-0156-y),
  T1, abstract depth). *Carries wherever the intermediary's marginal cost on bet
  volume is negligible, which the record states as its market's relevant feature;
  whether that holds for a clearing-member exchange is not established here.*
- A levy on the **handle** rather than on the **hold** changes the intermediary's
  incentives over contract design — for example toward half-point lines that
  eliminate pushes — which is a statement that fee *base* and not only fee *level*
  is a structural variable
  ([Depken & Gandar 2021](https://doi.org/10.1057/s41302-020-00179-z), T1,
  abstract depth). *Carries to any venue whose fee is levied on notional rather
  than on net revenue; which base a CFTC-designated contract market uses is a
  documentation-tier fact this corpus could not retrieve.*
- The overround is the bookmaker's price and it moved: it fell continuously from
  2000-01 to 2016-17 while surebets increased
  ([Gomez-Gonzalez & Del Corral 2018](https://doi.org/10.17811/ebl.7.4.2018.129-136),
  T1, abstract depth), and a risk-averse bookmaker should charge a **higher
  mark-up on events with more outcomes** and should dynamically adjust odds to
  reduce profit volatility, thereby **generating** arbitrage opportunities; the
  empirical counterpart reports a 1.33% mark-up increase per additional outcome,
  daily arbitrage opportunities with an instantaneous gross return of 1.14% per
  operation, and an average bettor expected loss of 5.67%
  ([Montone 2012](https://doi.org/10.2139/ssrn.2199035), T5 working paper,
  abstract depth). *The mark-up-per-outcome result carries only to a
  margin-quoting intermediary; the corpus notes that its structural claim —
  arbitrage as a by-product of the intermediary's own risk management — has no
  order-book counterpart in this corpus.*
- Subsidy is the market operator's cost of liquidity in a scoring-rule market, and
  the corpus records the design statements that bound it (8.4.2) but has **no
  record that measures the realized subsidy cost of an operating event exchange**.
  Endowment design is shown to affect prediction-market liquidity
  ([Seemann, Hungenberg & Enders 2008](https://doi.org/10.5750/jpm.v2i3.445), T1,
  abstract depth) and liquidity is linked to prediction-market efficiency in
  [Tetlock 2008](https://doi.org/10.2139/ssrn.929916) (T5 working paper,
  **metadata depth**). *The endowment result carries only to play-money or
  operator-endowed markets, which a real-money exchange is not.*
- The mechanism comparison that bears directly on execution cost: a quote-driven
  market is reported to hold a **liquidity advantage** over an order-driven one in
  the betting industry
  ([Flepp, Nüesch & Franck 2017](https://doi.org/10.1016/j.qref.2016.07.016), T1,
  **metadata depth — no abstract retrieved**, so the corpus states the record's
  claim direction from its title and nothing further). *If it holds, it cuts
  against the assumption that an exchange dominates a bookmaker on cost, and the
  corpus flags it as an unresolved tension rather than picking a side.*
- Capital lockup and collateral: **no retrieved abstract among the 116
  abstract-depth included records states a measurement of the capital-lockup cost
  of holding an event-contract position to settlement, and none states a collateral
  or margin rule for such a position.** **Qualified under finding REV-1-10**: the
  33 metadata-depth records, the 545 X10 records, the 700 X11 records and the 5,249
  A3-rule records were **not assessed for it**, so this is a statement about 116
  abstracts, not about the corpus and certainly not about the literature. The
  frozen protocol asked for this (O5, E12) and the queries written for it returned
  nothing eligible. Reported as gap G-2 in section 10; an absence of evidence, not
  a finding about the world.

### 8.6 Strand S6 — microstructure of binary and limited-payoff instruments

#### 8.6.1 Kalshi-specific

- **Added under finding LITERATURE-1-9, at metadata depth.** A peer-reviewed
  record on Kalshi pricing accuracy, forecasting and risk exists in this corpus and
  carried no claim line at all until this remediation
  ([Subramanian 2026](https://doi.org/10.1504/ijfmd.2026.10080801), **T1**,
  *International Journal of Financial Markets and Derivatives*, **metadata depth —
  no abstract was returned by any source**). **This corpus states the record's
  topic and nothing further**: not its data period, not its measured quantity, not
  the direction of any finding. It is named because it is one of only **two**
  peer-reviewed Kalshi records in the whole corpus, and because omitting it made
  the synthesized Kalshi block effectively 18-of-18 T5 while gap G-6 reported the
  base as 2-of-19 peer-reviewed. The same reasoning this record already gave for
  naming Lim at metadata depth in 8.2.1 applies here and was not applied.
- **Added under finding LITERATURE-1-9, at metadata depth.** A Kalshi-specific NBER
  working paper on the venue and the growth of macro event markets
  ([Diercks, Katz & Wright 2026](https://doi.org/10.3386/w34702), T5, NBER working
  paper, **metadata depth**). Its topic is stated; **no finding of it is stated
  here**. The section-7 table previously carried it as "(n.d.)"; the registrant
  records January 2026 (finding LITERATURE-1-1).
- Effective spreads on the venue are "only modestly wider" in single-name markets
  than in broad-based ones despite greater informed price impact
  ([Bartlett & O'Hara 2026](https://doi.org/10.2139/ssrn.6615739), T5 preprint,
  abstract depth).
- Price adjustment to news is gradual and incomplete within short post-event
  windows across 41.8 million in-play transactions on 1,496 NBA and NFL games
  matched to a second-by-second win-probability benchmark
  ([Lee, Lee & Lee 2026b](https://doi.org/10.2139/ssrn.6964226), T5 preprint,
  abstract depth).
- A drift-per-noise statistic computed from within-market minute-level price paths
  is associated with higher short-horizon continuation and lower ex-post forecast
  error in non-zero-trend regimes, with significant differences between top and
  bottom deciles ([Greene 2026](https://doi.org/10.2139/ssrn.6442939), T5
  preprint, abstract depth). **E14 note:** the record states a constructed
  statistic; this corpus does not restate it as a signal and states no rule
  derived from it.
- Efficiency varies with the event's own characteristics: a scheduled release with
  a clear consensus forecast showed the most gradual information incorporation,
  while a policy decision combining a rate outcome with a human-judgment component
  showed noisier incorporation
  ([Krause 2026e](https://doi.org/10.2139/ssrn.7021660), T5 preprint, abstract
  depth).

#### 8.6.2 Generalized (each line states the assumption that carries it)

- Prices in binary-options markets react "mostly efficiently and quickly" to
  public information shocks whose occurrence is near-random by a knife-edge
  condition, with a **short-lived under-reaction** when shocks are large
  ([Gauriot & Page 2025](https://doi.org/10.1093/ej/ueaf040), T1, abstract depth).
  *Carries to Kalshi under matched (E6) continuous trading and (E7) an
  objectively adjudicated settlement source; it is the closest generalized
  analogue to the Kalshi in-play underreaction result above, and the two agree in
  direction on the large-shock case while disagreeing on the baseline.*
- Order-book evidence on a binary-options venue finds **little evidence of
  convergence in beliefs**, and derives bounds on beliefs from order-submission
  decisions rather than from execution prices alone
  ([Groeger 2016](https://arxiv.org/abs/1609.03471), T5 preprint, abstract depth).
  *Carries under a public limit order book with observable submissions.*
- On the largest on-chain venue, a continuous tick-level archive of 30 billion
  order-book events over 52 days on a pre-registered stratified panel of 600
  markets yields eight stylized facts including a **longshot spread premium**, a
  depth profile closer to uniform than to top-of-book, broad maker-wallet
  diversity with a concentrated tail, and category-conditional effective-spread
  differences ([Dubach 2026](https://arxiv.org/abs/2604.24366), T5 preprint,
  abstract depth). *Carries to Kalshi under matched (E6) order-book trading and
  (E12) fee structure; the maker-population fact does not carry, because
  wallet-level diversity is a property of a permissionless venue and a
  CFTC-designated contract market's membership arrangements are different by
  construction.*
- Informed trading on decentralized event venues has converged methodologically on
  three approaches — a composite wallet-market screen over 210,000 wallet-market
  pairs, an event-level sign-randomization test classifying 3.14% of accounts as
  skilled winners and flagging 1,950 accounts as insiders, and a per-market
  information-leakage score
  ([Nechepurenko 2026](https://arxiv.org/abs/2605.02287), T5 preprint, abstract
  depth). *Carries only where account-level identity persists across markets,
  which is a property of the on-chain setting.*
- A design review of decentralized prediction markets decomposes them into eight
  modules — infrastructure, market topic, share structure and pricing, market
  initialization, trading, resolution, settlement, archiving — and records that
  modern designs deviate materially from earlier ones
  ([Rahman, Al-Chami & Clark 2025](https://doi.org/10.48550/arxiv.2510.15612), T5
  preprint, abstract depth). *Used here as a structural vocabulary for E7, not as
  evidence about any venue.*
- Volatility must be modelled differently for these instruments: prices are
  bounded probabilities, payoffs are binary, and contracts resolve at known
  deadlines, so the ARCH/GARCH workhorses natural for positive-valued price
  processes are not
  ([Xi, Moallemi, Pai & Wang 2026](https://arxiv.org/abs/2607.08199), T5 preprint,
  abstract depth). *Venue-none; it carries to any binary event contract by the
  same payoff argument that separates 8.4.2 from 8.4.3, and it is the corpus's
  clearest statement that standard time-series machinery does not port
  unexamined.*
- A continuous dynamical model of a binary-option market with exogenous
  information shows price always converges when information is constant, and that
  **price sensitivity** strongly affects price lag versus information when
  information changes ([Gampe & Griffin 2023](https://doi.org/10.1016/j.cnsns.2022.106994),
  T1, abstract depth). *Venue-none; the applicability condition is the stated
  purchasing rule.*
- Further S6 records are carried in the corpus at metadata depth only and their
  content is **not** stated here: relative pricing of binary options in live
  soccer betting ([Hofer & Leitner 2017](https://doi.org/10.1016/j.jedc.2016.12.007),
  T1), the stylized facts of prediction-market price changes
  ([Restocchi, McGroarty & Gerding 2019](https://doi.org/10.1016/j.physa.2018.09.183),
  T1), the term structure of a prediction market
  ([Gill 2026a](https://doi.org/10.2139/ssrn.7110798), T5), a microstructure
  perspective on prediction markets
  ([Palumbo 2026](https://doi.org/10.2139/ssrn.6325658), T5), attention and
  liquidity in prediction markets
  ([Saliou, Dubinin & Zhang 2026](https://doi.org/10.2139/ssrn.7222239), T5),
  and jump trading in prediction markets
  ([Gill 2026b](https://doi.org/10.2139/ssrn.7245879), T5). *Naming them without
  stating their findings is the honest disposition at metadata depth.*

### 8.7 Where the corpus disagrees with itself

Reported, not averaged away.

| question | position A | position B | what separates them |
|---|---|---|---|
| Is there an exploitable Kalshi-Polymarket arbitrage? | Cross-venue divergence is 0.60 cents median against a 2.00-cent fee and edges live one minute ([Moulinier 2026](https://doi.org/10.2139/ssrn.7170178)) | Depth-aware payoff-bound violations on linked binary markets total 1.12 million dollars, though only the NO-to-YES direction is protocol-executable pre-settlement ([Gebele, Mutzel & Matthes 2026](https://arxiv.org/abs/2608.00666)) | A is a **two-venue executable-quote** measurement with clock alignment as the identified artifact; B is a **single-venue payoff-space** measurement with the protocol's own transformation set as the executability filter. They measure different objects and the corpus does not treat either as refuting the other |
| Does Kalshi show a favorite-longshot bias? | Yes, clearly, in overall pricing ([Bürgi, Deng & Whelan 2025](https://doi.org/10.2139/ssrn.5502658)), in unemployment contracts ([Krause 2026a](https://doi.org/10.2139/ssrn.7110758)) and in all sub-25% buckets ([Gupta 2026](https://doi.org/10.2139/ssrn.6858200)) | No, not in CPI contracts, where zero-priced contracts are perfectly calibrated and high-probability contracts are well calibrated ([Krause 2026b](https://doi.org/10.2139/ssrn.7087538)) | Contract family, sample period, and the treatment of zero-priced contracts; and, per [Yurchyna 2026](https://doi.org/10.2139/ssrn.7364100), sample **composition**, since 41% of the aggregate change in the Mincer-Zarnowitz slope at the 2025 boundary is composition rather than repricing |
| Does inventory move a dealer's reservation price down? | Yes — the prediction of the inventory-control lineage ([Ho & Stoll 1981](https://doi.org/10.1016/0304-405X(81)90020-9); [Guéant, Lehalle & Fernandez-Tapia 2012](https://doi.org/10.1007/s11579-012-0087-0)) | No — futures transaction data show a **positive** correlation between inventory and reservation prices, as a strong and consistent regularity ([Manaster & Mann 1996](https://doi.org/10.1093/rfs/9.3.953)) | The disagreement is internal to the unbounded-payoff lineage and is transferred here **unresolved**; no record in this corpus tests either sign on an event contract |
| Is a quote-driven or an order-driven venue cheaper to trade? | Quote-driven holds a liquidity advantage in betting ([Flepp, Nüesch & Franck 2017](https://doi.org/10.1016/j.qref.2016.07.016), metadata depth) | Bookmaker price-setting exists precisely to extract profit from bettors, implying a cost to the trader ([Levitt 2004](https://doi.org/10.1111/j.1468-0297.2004.00207.x)) | The first is a liquidity statement and the second a profit statement; they are not logically inconsistent, and the corpus flags that no record measures both on one venue. **And neither side of this question can be applied to Kalshi at all (finding REV-1-2): the venue's own trading mechanism is unretrieved (S7-5, AG-1), so this corpus cannot say which column Kalshi belongs in.** |

### 8.8 Included records that carry no claim line in section 8

**Finding LITERATURE-1-9.** A mechanical check of every included DOI against the
text of section 8 found **19** of the 149 included records with no claim line
anywhere in the synthesis, while the section-7 `role in the argument` column
affirmatively stated that each enters a named section-8 block. Three are added
above at their stated extraction depth (Subramanian, Diercks et al., Štrumbelj).
The remaining **16 are named here rather than left invisible**, with their strand
and depth, so a reader can see exactly what was included and not used. Their
section-7 role column now says the same thing.

| record | tier | E4/E15 | E3 strand(s) | depth | why no claim line |
|---|---|---|---|---|---|
| Bakalo 2026 `10.2139/ssrn.6150527` | T5 | G | S3 | abs | its FLB explanation review is covered by the Newall & Cortis and Ottaviani & Sørensen survey entries in 8.3.2 |
| Berg, Forsythe, Nelson & Rietz 2008 `10.1016/s1574-0722(07)00080-7` | T1 | G | S2 | meta | metadata depth; no finding can be stated |
| Cao 2026 `10.2139/ssrn.7049119` | T5 | G | S3+S5 | meta | metadata depth |
| Dalen 2026 `10.48550/arxiv.2604.10005` | T5 | G | S4+S5 | abs | the record's companion kernel paper is cited in 8.4.2; this one is not, and should have been |
| Donatoni 2022 `10.1080/14697688.2022.2028888` | T1 | G | S4+S6 | abs | inventory-control-with-order-book-information; not carried into 8.4.3 |
| Koch 2007 `10.2139/ssrn.964438` | T5 | G | S3 | meta | metadata depth |
| Marek 2019 `10.13140/RG.2.2.13916.03201` | T5 | G | S2+S5 | abs | not carried into 8.2.2; registrant records it as *Unpublished* |
| Oliven & Rietz 2004 `10.1287/mnsc.1040.0191` | T1 | G | S1+S6 | abs | forward-citation anchor A1; named as an anchor in section 13.4 but carries no claim line |
| Portnaya 2026 `10.48550/arxiv.2606.19517` | T5 | G | S1+S2 | abs | Bitcoin threshold / option-price comparison; not carried into 8.2.2 |
| Restocchi et al. 2019 `10.1016/j.frl.2018.08.003` | T1 | G | S2 | meta | metadata depth |
| Sung 2009 `10.1111/j.1468-0335.2008.00716.x` | T1 | G | S1+S6 | abs | weak-form inefficiency in a state-contingent-claims market; not carried into 8.1.2 |
| Šestovic 2017 `10.2139/ssrn.3044673` | T5 | G | S3 | meta | metadata depth |
| Šestovic 2017 `10.2139/ssrn.3035848` | T5 | G | S3 | meta | metadata depth |
| Sethi 2015 `10.1007/s10614-015-9514-7` | T1 | N | S4 | meta | metadata depth |
| Swanson 2026 `10.2139/ssrn.6073727` | T5 | G | S6 | meta | metadata depth |
| Zhou 2007 `10.2139/ssrn.997788` | T5 | G | S5 | meta | metadata depth |

**Nine of the sixteen are at metadata depth**, where naming without stating is
the only honest disposition. **Seven are at abstract depth and simply were not
carried** — Bakalo, Dalen, Donatoni, Marek, **Oliven & Rietz**, Portnaya, Sung —
and that is a synthesis omission, not a depth limit. It is recorded here as one.

**Corrected 2026-09-02 under findings REV-2-5, QUANT-2-4 and LITERATURE-2-5.**
As first written this paragraph said *eleven* metadata-depth and *five*
abstract-depth, then listed six names, and omitted Oliven & Rietz — a T1
forward-citation anchor (A1) read at abstract depth — from the abstract-depth list
entirely. The counts are now generated from the table's own `depth` column rather
than by hand: **9 `meta`** (Berg, Cao, Koch, Restocchi, Šestovic ×2, Sethi,
Swanson, Zhou) and **7 `abs`** (the seven named above), 9 + 7 = 16. The quantity
the sentence exists to state is the count of **unforced synthesis omissions**, and
it was understated by two in the direction that flatters the corpus. The Berg cell
also carried `10.1007/s15740722070` — the record's own store key
`berg2008s15740722070` with a Springer prefix pasted on, an identifier that
resolves nowhere. It is corrected to the store's and section-7 table's value
`10.1016/s1574-0722(07)00080-7`, and the section-8.8 identifier column is
generated from the store rather than from the record id.

## 9. S7 venue-structural stream — documentation tier, counted separately

**Constraints, all from frozen protocol section 2.7 and all binding on this
section.** These records establish **venue-structural facts only** — contract
specification, settlement rule, fee schedule, position limits, membership and
market-maker arrangements, designation and self-certification status. They may
**never** establish a behavioural, empirical or efficiency claim. They are
**never** counted in the S1-S6 flow of section 5. Every fact carries document
identity, version or effective date, and ISO 8601 retrieval date. Filer-published
material is labelled "as filed": the CFTC public record shows what was filed and
its regulatory status, not that the contents are independently verified.

**S7 query execution, counted separately from the corpus flow.**

| query_id | source | platform | date_searched | http | platform_total | retrieved | outcome |
|---|---|---|---|---|---|---|---|
| ka-doc-01 | Federal Register | federalregister.gov REST API v1 | 2026-09-02 | 200 | 5 | 5 | complete; term "Kalshi", all agencies |
| ka-doc-02 | Federal Register | federalregister.gov REST API v1 | 2026-09-02 | 200 | 570 | 100 | **depth-truncated**: `per_page=100` against 570 matching documents, 6 pages reported, 1 retrieved |
| ka-doc-03 | CFTC public record | www.cftc.gov (DCM index page) | 2026-09-02 | 200 | not reported | 1 page | page retrieved; **contains no occurrence of the string "Kalshi"** in the served HTML |
| ka-doc-04 | CFTC public record | www.cftc.gov (DCM industry-filings page) | 2026-09-02 | 200 | not reported | 1 page | page retrieved; carries the designated-contract-market table used below |
| ka-doc-05 | Kalshi rulebook (filer-published) | kalshi.com | 2026-09-02 | 429 | n/a | 0 | **AG-1 confirmed at execution**: HTTP 429 on the frozen query and on both the `-b` and the retry-until-200 `-c` re-runs (9 attempts) |
| ka-doc-06 | eCFR | ecfr.gov | 2026-09-02 | 200 | n/a | 0 | **AG-2**: HTTP 200 whose body is an access interstitial titled "Federal Register :: Request Access" and contains none of the regulation text; classified a transient failure by amendment A1 and re-run under `-b` (5 attempts) and `-c` (9 attempts) with the same result |

**S7 queries, verbatim as executed** (these are reported here and not in section 3, because
the documentation stream is counted separately and must never enter the S1-S6 flow):

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

**S7 facts established, with their source, version and retrieval date.**

| # | fact, as filed / as served | document identity | version / effective date | retrieved | may it license a behavioural claim? |
|---|---|---|---|---|---|
| S7-1 | "Kalshi" appears in the CFTC's designated-contract-market industry-filings table with status **Designated** and date **11/03/2020** | CFTC, "Industry Filings: Designated Contract Markets (DCM)", www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations | page as served on the retrieval date; the page carries no version identifier | 2026-09-02 | No. It fixes the venue's regulatory category and its designation date, nothing else |
| S7-2 | The same table's remarks column states: "On January 17, 2025, the Commission granted Kalshi's petition to modify its Order of Designation to permit intermediated futures trading" | same as S7-1 | as served | 2026-09-02 | No. It records a change in permitted intermediation, which bears on the **participant population** term of every carrying assumption in section 8, and on nothing else |
| S7-3 | Five Federal Register documents match the term "Kalshi": Proposed Rule 2026-15948 "Conflicts and Affiliations" (2026-08-06); Proposed Rule 2026-13239 "Data Reporting Requirements for Certain Event Contracts" (2026-07-01); Proposed Rule 2026-11854 "Prediction Markets; Public Interest Determinations" (2026-06-12); Rule 2025-22807 "Fees for Reviews of the Rule Enforcement Programs of Designated Contract Markets and Registered Futures Associations" (2025-12-15); Proposed Rule 2024-12125 "Event Contracts" (2024-06-10) | Federal Register API, `conditions[term]=Kalshi` | each document's own publication date, listed | 2026-09-02 | No. It establishes that the venue and its instrument class are the subject of active federal rulemaking, and identifies which documents a successor stage must read |
| S7-4 | 570 Federal Register documents match the term "event contracts" with the Commodity Futures Trading Commission as agency | Federal Register API, `conditions[term]=event contracts` + agency filter | continuous series; 100 of 570 retrieved | 2026-09-02 | No. It bounds the size of the regulatory record, and flags that this corpus read one page of six |
| S7-5 | **Not established.** Kalshi's fee schedule, position limits, contract specifications, settlement and adjudication rules, membership arrangements and any designated-market-maker programme | filer-published rulebook at kalshi.com/regulatory/rulebook | none retrieved | attempted 2026-09-02, refused (HTTP 429 x9) | n/a — **the corpus states none of these facts.** Every place in section 8 where a carrying assumption needed one of them is marked `not-transferable-as-stated` |
| S7-6 | **Not established.** The text of 17 CFR 40.11 (review of event contracts / self-certification prohibitions) | eCFR, title 17 chapter I part 40 section 40.11 | none retrieved | attempted 2026-09-02, refused by an access interstitial x15 | n/a — the corpus states nothing about the regulation's content |

**J5 second-hand venue claims found inside peer-reviewed and preprint records,
and their disposition.** Two records state venue-structural facts about Kalshi
(a 2.00-cent fee, and a reconstructed 2025 maker fee) — see 8.5.1. The protocol
requires each to be checked against the documentation tier before this corpus
states it. **Neither check could be performed**, because S7-5 failed. Both are
reported flagged second-hand and unverified, and this corpus asserts neither as a
fact about the venue. Where the two conflict with each other the corpus would
report both and settle nothing; at the depth reached they cannot even be compared,
because one abstract does not carry its numeric value.

## 10. Gaps the corpus exposes

Stated as gaps — absences of evidence — never as findings about the world.

- **G-1. No strand is empty, but S5 is nearly so on its own terms.** Every strand
  S1-S6 returned at least one eligible record, so no strand is reported empty.
  S5 nevertheless has **no record that nets a measured event-exchange discrepancy
  against a fully specified friction set on an order book**; the netting exercises
  in the corpus are parimutuel ([Ashiya 2013](https://doi.org/10.1177/1527002513493630))
  or bookmaker-conduct-based ([Grant, Oikonomidis, Bruce & Johnson 2018](https://doi.org/10.1080/1351847x.2018.1443148)).
  The queries that failed to populate it are `ka-crossref-09`, `ka-crossref-10`
  and `ka-openalex-04`, whose retrieved records were overwhelmingly
  X1-classified equity and foreign-exchange transaction-cost literature.
- **G-2. Collateral and capital lockup are absent from what this corpus read.**
  The frozen protocol named capital lockup and its duration as an E12 field and as
  part of objective O5. **No retrieved abstract among the 116 abstract-depth
  included records states a measurement or a model of the cost of capital locked in
  an event-contract position until settlement.** `ka-crossref-10` was written for
  exactly this and returned nothing eligible. **Qualified under finding REV-1-10**,
  because the previous wording ("no record in the corpus") was a universal negative
  over 149 records of which 33 were never read past title, venue and year: **the 33
  metadata-depth records, the 545 X10 records, the 700 X11 records and the 5,249
  records verdicted by the amendment-A3 token rule were not assessed for it.** The
  standing "absence of evidence, not evidence of absence" caveat disclaims a
  statement about the world; it did not disclaim the statement about the corpus,
  which is the one that was at risk. This one now does both.
- **G-3. Nothing in the corpus establishes Kalshi's own contract mechanics, and
  this record previously discharged four carrying assumptions against facts it did
  not have.** The entire S7 fee, settlement, position-limit, membership and
  market-maker record is unretrieved (S7-5, S7-6). What the retrieved CFTC pages
  establish is a designation status, a designation date and an
  intermediation-permission change — S7-1's own cell reads *"it fixes the venue's
  regulatory category and its designation date, nothing else"* — and **Designated
  Contract Market is a regulatory category, not a settlement rule and not a trading
  mechanism.** Every generalized claim in section 8 whose carrying assumption needs
  one of those facts is marked `not-transferable-as-stated`. **The count is now
  six, not two** (findings REV-1-2, REV-1-3, QUANT-1-5, LITERATURE-1-4 raised it
  from two to five; finding **REV-2-8** adds the sixth):

  | # | transfer | where | what unretrieved fact it needed |
  |---|---|---|---|
  | 1 | protocol-executable arbitrage (Gebele, Mutzel & Matthes) | 8.1.2 | which pre-settlement position transformations Kalshi's rulebook makes available |
  | 2 | bookmaker-plus-exchange arbitrage (Franck, Verbeek & Nüesch) | 8.2.2 | that Kalshi is a single exchange rather than a bookmaker/exchange pairing |
  | 3 | **added** — Thaler & Ziemba endpoint-settlement premise | 8.3.2 | the settlement rule for any listed Kalshi contract (S7-5) |
  | 4 | **added** — Levitt bookmaker-versus-exchange block | 8.3.2 | Kalshi's trading mechanism, E6 (S7-5) |
  | 5 | **added** — continuous-double-auction microstructure attribution | 8.4.2 | Kalshi's trading mechanism, E6 (S7-5) |
  | 6 | **added round 2 (REV-2-8)** — bookmaker market-making transfer, E6 block | 8.4.3 | Kalshi's trading mechanism, E6 (S7-5). The entry asserted unconditionally that E6 blocks the transfer *"to an order-driven exchange"*. The destination of every transfer in this corpus is the venue of interest, whose mechanism this record now says it cannot establish; and the determination **flips** on that unknown — on the quote-driven characterisation the Burgi record gives at 8.4.1, E6 would license rather than block it. The clause is now conditional |

  Marks 3 and 4 matter beyond their own lines. Mark 3 carried the property this
  record called "the property that makes the whole binary-contract literature
  transferable at all". Mark 4 carried what this record called "the single largest
  structural reason the sportsbook FLB literature must not be restated as a Kalshi
  finding". **Both of those load-bearing statements now rest on an unretrieved
  document (TC-1), not on the CFTC record.**
- **G-4. No abstract this corpus read states a market-making model fitted to
  Kalshi.** **Qualified under finding REV-1-10**: this is a statement about the 116
  abstract-depth included records. The 33 metadata-depth records, the 545 X10, the
  700 X11 and the 5,249 A3-rule records were not assessed for it. S4's Kalshi block
  is entirely measurement and its model block is entirely venue-none or
  other-venue.
  The one record that formulates the control problem natively for binary
  settlement ([Feil & Nendel 2026](https://arxiv.org/abs/2607.17991)) is not
  calibrated to any named venue in its abstract.
- **G-5. The inventory-risk lineage's applicability to [0,1] payoffs is asserted
  by transfer, not by the lineage.** Of the five named-lineage anchors, four are at
  metadata depth with transfer status `not addressed`, and the one whose model is
  stated in the retrieved text assumes a **Brownian reference price**, which is
  `explicitly excluded` for a bounded probability
  ([Guéant, Lehalle & Fernandez-Tapia 2012](https://doi.org/10.1007/s11579-012-0087-0)).
  The corpus cannot say whether the originals address bounded payoffs, because it
  did not read them. Nor can it say it for the lineage at large: **700 X11 records
  are transfer-clause records of exactly this class and none was assessed.**
- **G-6. Author concentration and tier thinness in the Kalshi block, corrected to
  their true size (findings REV-1-7, LITERATURE-1-10).** **Seventeen of the
  nineteen** Kalshi-specific records are T5 preprints or working papers — not
  fifteen, as this record previously said. **The only two peer-reviewed-tier Kalshi
  records in the corpus are Goel 2026 (`10.1016/j.iref.2026.105577`) and
  Subramanian 2026 (`10.1504/ijfmd.2026.10080801`)**, and Subramanian is at
  metadata depth, so exactly **one** peer-reviewed Kalshi record contributes a
  stated finding to this artifact. **Seven of the nineteen come from two author
  groups** — five with Krause as first author, two by "Lee, Lee & Lee"
  (`10.2139/ssrn.6748186`, `10.2139/ssrn.6964226`) — not five of nineteen from one
  group. The Kalshi evidence base in this corpus is recent, very thin in
  peer-reviewed tier, and not independent across records. Understating a limitation
  in the sentence whose job is to state it is a reporting defect in the direction
  that flatters the corpus, and both numbers were understated.
- **G-7. Backward citation chasing never ran** (section 2, `prisma-s-5`;
  amendment **A6**), so the corpus contains no record reachable only through an
  included record's reference list.
- **G-8. One of the four named bibliographic databases contributed zero records to
  the topical strategy.** All four Semantic Scholar topical queries and all eight
  retries returned HTTP 429 (AG-3). This is not only a volume loss: the
  `prisma-s-9` argument that no vocabulary is category-gated out of the strategy
  rested on four queries carrying the unrestricted forms that offset the arXiv
  `cat:q-fin*` narrowing on `ka-arxiv-03` and `ka-arxiv-05`, and one of the four was
  `ka-s2-02`. **Restated under finding REV-2-3** — the round-1 wording, "in
  execution the narrowing is not offset", overstated the loss and is corrected:
  three of the four offsetting queries did execute and did return records
  (`ka-crossref-07`, `ka-openalex-06`, `ka-crossref-11`), so no vocabulary was gated
  out entirely. **What the gap costs is redundancy and one platform**: the offset
  rests on three capped queries across two platforms rather than four across three,
  and the lost query is the only one whose form paired the market-making vocabulary
  with the binary-event-contract vocabulary. The per-query table is at
  `prisma-s-9`.
- **G-9. The SSRN supplementary arm was not run and its declared-in-advance gap
  entry was omitted from this record as first published** (AG-9, amendment **A7**;
  finding LITERATURE-1-7). 31 of the 149 included records, and **15** of the 19
  Kalshi-specific records, carry `10.2139/ssrn.*` DOIs, and SSRN was reached only
  through two Crossref container-restricted queries capped at `rows=20`. (**15,
  corrected from 13 under finding REV-2-6**; see the derivation at `prisma-s-4`.)
- **G-10. 98.3% of dispositions in this flow are keyword-classifier outputs**
  (finding QUANT-1-1, amendment A10). 150 of 8,813 records carry a read-based
  verdict. The recall consequence is not quantifiable without a second screener
  this design does not have; the **lower bound** on the exposure is the
  **3,090-record title-only** stratum of the A3 rule (section 13.1).

## 11. `TO COMPUTE` handoffs

Recorded, not computed here (ADR-0003). Each names what would have to be computed
and on what data; none is a trading rule and none is executed in this repository.

| # | what would have to be computed | on what data | why it is not computed here |
|---|---|---|---|
| TC-1 | The venue's fee schedule, tick size, position limits, settlement source and permitted pre-settlement position transformations, as a dated document set | The filer-published rulebook plus the CFTC filing record for the venue | Documentation retrieval, blocked by AG-1; it is a retrieval task for a session with a working route to the filer's document, not an analysis task |
| TC-2 | Whether the payoff-space versus protocol-executable distinction ([Gebele, Mutzel & Matthes 2026](https://arxiv.org/abs/2608.00666)) has a Kalshi counterpart | TC-1 plus the venue's own contract-family definitions | Requires TC-1; without it the transfer is `not-transferable-as-stated` |
| TC-3 | The capital-lockup cost of an event-contract position held to settlement, as a function of contract duration | Venue contract specifications plus a funding-cost series | The corpus returned no record that does this; it is a genuine open computation, not a literature-retrieval failure |
| TC-4 | Whether the Cartea-Jaimungal / Avellaneda-Stoikov single-parameter identification ([Feys 2026](https://arxiv.org/abs/2606.01477)) binds any market-making model that a future empirical stage might fit | The axioms as stated in that record, checked against the candidate model | A derivation task; this corpus records the claim and does not verify the proof |
| TC-5 | A composition-controlled re-estimate of any Kalshi calibration statistic across the 2025 asset-class boundary | Kalshi fill data — **out of scope for this repository under ADR-0003 and the session's deliverable spec** | Named so the successor knows the design constraint ([Yurchyna 2026](https://doi.org/10.2139/ssrn.7364100)) before it fits anything |

## 12. Bibliography store

<!-- bibliography-store -->
- Store: `docs/literature/references_kalshi-arbitrage.json` (CSL-JSON, canonical serialization)
- SHA-256: `fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164` — equals frontmatter `bibliography_sha256`
- Entries: 149, equal to `n_included`; every entry carries a DOI (FAIR F1)
- Identifier resolution: all 149 DOIs were resolved against the **DOI Handle System** (`https://doi.org/api/handles/{doi}`) on 2026-09-02 and every one returned `responseCode` 1. The per-identifier record is [ka-store-doicheck.json](docs/literature/search_logs/kalshi-arbitrage/ka-store-doicheck.json). **Caveat, stated so it is not mistaken for a resolution failure:** an unauthenticated HTTP HEAD to `https://doi.org/{doi}` returns 403 for 83 of the 149 identifiers. That is publisher bot-blocking at the landing page, not a failure of the handle to resolve; the Handle System is the authoritative resolution test and it passed 149/149.
- Derived exports (regenerable; never a source of truth): `python ~/.claude/scripts/build_bibliography.py export docs/literature/references_kalshi-arbitrage.json --format bibtex|ris`

**Gate verdict and its disposition, stated plainly. Re-run against the remediated
document on 2026-09-02 under finding QUANT-2-5.** The gate verdict on file until
this remediation had been produced at 11:53 against the **pre-remediation**
document, so it did not describe the artifact that ships; and its disposition line
asserted that *"All findings are G16 identifier-resolution findings of the standing
closed publisher-landing-page class"*, a class defined by HTTP 403 at the publisher
plus Handle `responseCode` 1 — which is **not** exact, because two of the 83 are not
403s. Both defects are corrected here. The re-run is recorded at
[ka-gate-verdict.json](docs/literature/search_logs/kalshi-arbitrage/ka-gate-verdict.json),
which supersedes the 11:53 run and carries the full finding list and a fresh
Handle System check.

The research-compile gate returns `block` on the remediated record with **83
findings, every one of them a G16 identifier-resolution finding and no finding of
any other kind** (G1-G15 and G17-G20 all pass) — the same count and the same
composition as before remediation, which is what should be expected of a
remediation that changed no identifier except one. **81 of the 83** are the
**publisher landing-page class**, a standing closed disposition in this project:
the resolution test is the DOI Handle System `responseCode`, not the fetchability
of the publisher's page (the standing disposition and its citation sites are given
by section heading in the adjudication below). **The other two are dispositioned
individually rather than absorbed into the class.** The Handle System check was
re-run over the store on the same date and returns `responseCode` 1 for **149 of
149**. The three sub-cases:

| sub-case | n | what the gate saw | what the Handle System returned | disposition |
|---|---|---|---|---|
| HTTP 403 | 81 | publisher refuses an unauthenticated HEAD | `responseCode` 1 | **closed class**; identifier resolves |
| HTTP 302 | 1 | `10.3905/jod.2019.26.4.128` redirects to a login-gated page (`implicit-login=true`) | `responseCode` 1, registered target `pm-research.com/lookup/doi/...` | **not the 403 class**; identifier resolves and the full text is paywalled. Dispositioned on its own terms (QUANT-2-5) |
| HTTP 404 | 1 | `10.17811/ebl.7.4.2018.129-136` — the **registered target URL itself** returns 404 at the publisher's article page | `responseCode` 1, registered target `unioviedo.es/reunido/index.php/EBL/article/view/12711` | **not the 403 class and not bot-blocking**: the DOI resolves and the landing page the registrant points at is dead, so this record's full text is not reachable through its own identifier. Recorded as access gap **AG-8** |

This record therefore does **not** claim a gate `pass`. It reports the gate's
verdict verbatim (`block`, 83 G16 findings) together with the standing
disposition and the per-identifier evidence.

**Adjudication by audit round 1, recorded here as the disposition of the gate
rather than as a remediation of it.** The round-1 auditor adjudicated this
record's own `block` and **disagreed with it on the merits**. The adjudication,
adopted:

1. **The authoritative resolution test is the DOI Handle System `responseCode`,
   not the fetchability of a publisher landing page.** An unauthenticated HTTP
   HEAD against a publisher's article page is a test of that publisher's bot
   policy, not of whether the identifier resolves. On the authoritative test this
   store passes **149 of 149**, with the per-identifier record at
   [ka-store-doicheck.json](docs/literature/search_logs/kalshi-arbitrage/ka-store-doicheck.json).
2. **81 of the 83 findings fall in the standing-closed publisher-landing-page
   class** — corrected from "all 83" under finding **QUANT-2-5**, because the 404
   and the 302 are not HTTP 403 and the 404 is a dead registered target rather than
   a bot policy. That class is a standing disposition in this project, recorded in
   the deliverable specs and audit trails cited below **by section heading rather
   than by file-and-line**, because line references are brittle across edits:
   - `docs/deliverables/deliverable_spec_naming-sweep_2026-08-24.md`, section
     **`# Delegation`**, in the `excluded:` field of each audit work item
     ("G16 publisher-403 class stays closed (handle-API test)");
   - `docs/deliverables/deliverable_spec_phase2-explosive-review_2026-08-24.md`,
     section **`# Delegation`**, same field ("G16 publisher-403 class closed");
   - `docs/audits/audit_trail_naming-sweep_2026-08-24.md`, sections
     **`## verification-of-remediations`** and
     **`## residual-risk-and-sampling-caveat`** under
     **`# Audit trail — Naming sweep, round 1`**, and
     **`## deferred-logged-minors`** and
     **`## residual-risk-and-sampling-caveat`** under
     **`# Audit trail — Naming sweep, round 2`** — where the disposition is
     recorded as *"handle-API responseCode 1 is the resolution test (five
     predecessor reviews carry identical dispositions with logs)"*.

   Cited by heading, not by file-and-line, deliberately: the predecessor line
   numbers this record previously gave are brittle across any edit to those files
   and would decay into false citations.
3. **One substantive residual survives the class closure and is kept: AG-8.**
   `10.17811/ebl.7.4.2018.129-136` resolves (`responseCode` 1) but its **registered
   target URL itself returns HTTP 404**. That is not publisher bot-blocking; the
   landing page the registrant points at is dead, so the record's full text is not
   reachable through its own identifier. It stays in section 13.3 as access gap
   AG-8 and is the one G16-adjacent defect this record does not close.
4. **A second residual is added by this remediation: AG-10.** One of the 149 store
   DOIs, `10.11179/ker.74.119`, is registered with neither Crossref nor DataCite,
   so its bibliographic metadata could not be verified against a registration
   agency during the LITERATURE-1-1/1-2 metadata sweep. The Handle System resolves
   it; the metadata is carried from the store unverified.

**Standing verdict of this record: the gate returns `block` on the document that
ships; 81 of the 83 G16 findings are dispositioned as a closed class by
adjudication, and the other two — one HTTP 302 paywall redirect and one HTTP 404
dead registered target — are dispositioned individually; the residual is two access
gaps, AG-8 and AG-10.** This record does not restate the verdict as `pass` and does
not suppress it.

## 13. Limitations and verification gaps

### 13.1 Amendments this record ran under

**Fifteen.** Five ran during execution; seven were added by round-1 audit
remediation on 2026-09-02; **three more (A13, A14, A15) were added by round-2 audit
remediation on the same day**, and all three correct what earlier amendments
*asserted*, not what the pipeline *did*: no verdict value, no count and no
eligibility judgement moves under any of them. All are recorded in
[ka-protocol-amendments.md](docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md)
and — **corrected under finding REV-1-13** — all fifteen are now also appended to
the **frozen protocol's own append-only addendum**, which is where protocol section
10 requires them ("recorded as a numbered, dated, append-only amendment **in the
addendum below**"). Until this remediation the addendum was empty, so a reader who
verified the registered SHA-256 obtained a protocol whose text asserted an
amendment mechanism and showed no amendments. Nothing above the addendum marker was
touched: the frozen prefix — the first 82,677 bytes, the file exactly as
registered — still hashes to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`, and the
**protocol-with-addendum SHA-256 is
`21a77d10841ba7f15ea58d5a58a1bca57818b2ed1a0f3bf53a1dbce6a8dcc53b`** (file size
132,488 bytes), to be carried by the follow-on provenance commit, which must name
the frozen hash it supersedes. **That digest supersedes
`42bc6116ee554ee5cc80743d14d2f3d834f4feb389b53b5eaf2820c27322a762` (118,837
bytes)**, which was the value after amendment A12 appended A1-A12 and which is now
stale: round-2 remediation appended A13-A15 and inserted the A3 supersession banner
recorded in A13. Both values are given so a reader holding either can tell which
document is in hand.
Verify the invariant with
`head -c 82677 docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md | sha256sum`.

The table below carries **all five required elements** of protocol section 10.
The two that were missing — **why**, and **which PRISMA-P item(s) it touches** —
are added under the same finding.

| # | date | what changed | why | stage decided / records already screened? | PRISMA-P item(s) |
|---|---|---|---|---|---|
| A1 | 2026-09-02 | An HTTP 200 whose body is a content-free access interstitial is classified an "other transient failure" for the frozen retry convention | The frozen text names HTTP 429 explicitly and "other transient failure" generically; a 200 carrying an access-denial body is not literally named. Treating it as success would have recorded a retrieval that did not occur | S7 execution. No — `ka-doc-06` yielded zero content on all three attempts, so no record was affected | 9, 10 |
| A2 | 2026-09-02 | Supplementary RePEc arm by HTTP POST to `/cgi-bin/htsearch2`, added after both frozen GET queries returned HTTP 200 with an empty results page; the frozen queries are not replaced and their logs stand unaltered | The named endpoint no longer serves results to a GET; reporting that as "RePEc returned nothing" would have misdescribed the literature and forfeited the recall the arm was added for | topical execution. No — decided before any RePEc record was screened | 9, 10 |
| A3 | 2026-09-02 | A deterministic published vocabulary pre-sorter partitioning the 8,154-record forward-citation-only stratum into a 2,905-record REVIEW stratum and a 5,249-record DEFAULT-X1 stratum | Reading 8,154 titles individually was not achievable in the session; the alternatives were sampling or a citation floor (both forbidden by the frozen text), or reporting the arm unscreened | mid-screening. **Superseded in part by A10**: the REVIEW stratum was not individually read either | 11b, 12; PRISMA 2020 item 8 |
| A4 | 2026-09-02 | Disposition code X10 plus its objective-prioritization extraction-selection rule; Table X-full published as a machine-readable artifact rather than inline | Coding eligible-but-unextracted records under X8 would have been false (nothing was tried and failed) and including them would have been false too (no extraction behind the row); an 8,664-row inline table would be unreadable | post-stage-1, pre-extraction. No eligibility verdict was changed. **Restated by A10**: X10 is a keyword stratum, not an eligibility determination | 11b, 12, 15; PRISMA 2020 item 16b |
| A5 | 2026-09-02 | Disposition code X11 | X8 asserts a failed retrieval attempt and X6 asserts an unstated applicability condition; neither could be asserted truthfully, and an honest undecided was the only accurate disposition | post-stage-1, pre-extraction. No eligibility verdict was changed. **Restated by A10** | 11b |
| **A6** | 2026-09-02 | **The protocol's `ka-bc-{n}` backward citation-chasing arm was not executed** and is not executed retroactively | Protocol section 3.3 bounds the arm to the reference lists of INCLUDED C1 and C3 records, which requires full texts; none was retrieved (A9), so the arm had no input. Recording it only as a narrative gap did not meet section 10, which requires a numbered amendment for **any** deviation (finding SCOPE-1-1) | post-extraction, retrospective. No record's verdict is affected; the recall consequence is gap G-7 | 9, 10 |
| **A7** | 2026-09-02 | **The SSRN supplementary site-search arm was not run**, and the recall verification gap the frozen protocol required in that case is recorded now as AG-9 | Protocol section 3.1's "SSRN caveat, declared in advance" requires that if the arm is not run "the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence". The record as first published contained no such entry — a silent deviation, which section 10 classes as a conduct violation (finding LITERATURE-1-7) | retrospective. 31 of 149 included records and 15 of 19 Kalshi records are SSRN DOIs (15 corrected from 13, finding REV-2-6), so the gap is material | 9, 10 |
| **A8** | 2026-09-02 | **Criterion I4 is explicitly relaxed** for the 33 included records retrieved only to title, venue and year. The frontmatter's unauthorised X8 rewording ("or full text unobtainable after the retrieval chain") is struck | Frozen I4 requires retrievability to abstract depth and sends bare-title records to X8; 33 included records fail it. The choice was to exclude them (changing `n_included` and the bibliography SHA) or to relax I4 with a stated rationale. The relaxation is chosen because the 33 are named without their findings being stated, so they carry no claim; but relaxing a frozen criterion silently is drift, and this amendment ends the silence (finding QUANT-1-3) | retrospective, post-extraction. `n_included` stays 149; a reader declining the relaxation should read 116 + 33 X8 | 11a, 11b |
| **A9** | 2026-09-02 | **No full text was read for any included record**; extraction reached abstract depth for 116 and metadata depth for 33, and no stage-2 assessment was performed for any record | Extraction fields E8-E13 presuppose a stage-2 assessment of retrieved text. The substitution was disclosed in 13.2 but was never converted into an amendment; A4 amends only the extraction-*selection* rule and A5 only the 700 transfer-clause records (finding SCOPE-1-2). The constraint now also travels in the frontmatter as `extraction_depth:` | extraction. All 149 affected | 12, 15 |
| **A10** | 2026-09-02 | **The full five-list keyword classifier (`ka-screening-script.py`, token lists EVENT/CONTRIB/MODEL/DEFI/ELICIT, rules R0-R9) is declared the PRISMA 2020 item-8 automation tool of record for all 8,664 non-include dispositions.** The A3 sentence "every one of them was read individually" is struck, as is the verdicts-file claim that the rule set "encodes that reading". X10 and X11 are restated as keyword-identified strata | Re-reading the archived pipeline, every disposition except the 149 includes and one hand-verified twin is a rule output. Re-running the logic under `PYTHONHASHSEED=0` over a universe rebuilt from the stored logs reproduces the published nine-code table exactly. The previous declaration named only the 5,249-record DEFAULT-X1 partition, leaving **3,414 rule outputs presented as individual screening verdicts** (finding QUANT-1-1, critical) | retrospective. No verdict value changes under A10; what changes is what the record says produced them | 11b, 12; PRISMA 2020 item 8 |
| **A11** | 2026-09-02 | **The X5 rule's four short DeFi tokens are matched with word boundaries instead of bare substrings**, the classifier re-run and `ka-screening-verdicts.jsonl` re-emitted (X5 159→94, X11 643→700, X7 236→244); and the pipeline is made deterministic (total dedup tie-breaks, `PYTHONHASHSEED=0` asserted, the previously unarchived partition and include inputs derived by a committed script) | `dex` fired inside *index*, `amm` inside *programming*, `defi` inside *defined*, so 65 records with no DeFi content carried a false B-a criterion-failure reason (finding QUANT-1-2). Separately, record-level tie-breaks resolved on set iteration order, so the published Table X-full row identifiers were not reproducible (finding QUANT-1-6) | retrospective, post-publication. **This is the only amendment that changes a published verdict.** It is a bug fix to a rule output, not a re-screen: no record was re-read and no criterion was reinterpreted | 11b, 12 |
| **A12** | 2026-09-02 | **A1-A12 are appended to the frozen protocol's own append-only addendum**, which was empty at first publication. Frozen prefix (first 82,677 bytes) unchanged and still hashes to `99524df02696…`; protocol-with-addendum digest was `42bc6116…` at A12 and is `21a77d1084…` after A13-A15 | Section 10 requires amendments "in the addendum below" and names it "APPEND-ONLY ADDENDUM BELOW THIS SECTION"; recording them only in an external log meant a reader verifying the registered hash saw a mechanism with no entries (finding REV-1-13). Nothing above the addendum marker is edited, so the frozen prefix still hashes to the registered value | retrospective | 5 (amendments) |
| **A13** | 2026-09-02 | **A10's strike of the individual-reading claims is completed.** Five further A3 assertions are struck by quotation — the heading parenthetical "3,300 … had already been read individually", "each such record is read and verdicted individually by the LLM screener", "Individual reading of 8,154 titles was begun and carried through 3,300 records", the "reported separately from the individually-read exclusions" clause, and "The 3,300 forward-citation-only records already read individually retain their individual verdicts" — and a `SUPERSEDED IN PART BY A10 AND A13` banner is inserted at the head of A3 in both the working log and the protocol addendum. The classifier/read-based split is published by stratum, net of the 150 | A10 struck three sentences and reached only one of A3's six. A12 had already transcribed A1-A12 into the protocol addendum, so **the protocol of record and this corpus record contradicted each other on the exact fact the round-1 critical finding was about**: the protocol asserted individual reading of 3,300 records while A10, in the same file, stated that no individual reading is recoverable from any artefact (findings REV-2-1, SCOPE-2-5, REPRODUCIBILITY-2-7) | retrospective, round-2 remediation. No verdict, count or eligibility judgement changes | 11b, 12; PRISMA 2020 item 8 |
| **A14** | 2026-09-02 | **Evidence corrections to A11; both declared departures upheld.** (a) A11's "`X1` 6,672 instead of 6,707" tie-break sentence is struck — it does not reproduce at any of four hash seeds in either matching mode — and is replaced by the measured ground: the shipped list form is seed-invariant (0 works differ at every seed pair) while the set form is not (19-24 differ), so conversion would *introduce* a seed dependency. (b) The bare-pattern claim is corrected from three records to **two**. (c) The 289/305 and 83/128 statistics are labelled as measured under the *rejected bare* patterns, with the shipped-pattern values 284/305 and 64/128 added beside them. (d) The `identifier` join is narrowed to the 6,923 rows on which it is defined, the header's `uid` is corrected to `id`, and A11's 2,630 / 6,183 row-id figures are downgraded to an unverifiable assertion because the pre-remediation file was overwritten and never committed. All three counterfactuals are archived at `ka-counterfactuals.py` / `.json` | Round 2 adjudicated both A11 departures **upheld on the merits** and found the *evidence recorded for them* wrong: three numbers presented as measurements do not reproduce from the archived pipeline, and the prescribed migration key is null for 21.4% of rows (findings QUANT-2-2, QUANT-2-6, QUANT-2-9, REPRODUCIBILITY-2-3, REPRODUCIBILITY-2-4, REPRODUCIBILITY-2-5) | retrospective, round-2 remediation. **No code changes and no disposition moves**: X5 94, X11 700, X7 244 stand | 11b, 12 |
| **A15** | 2026-09-02 | **A6's assertion about this protocol's own queries is struck as false.** A6 stated that neither `dealer` nor `limit order` "appears in any of the 35 frozen topical queries" and concluded to "two demonstrated vocabulary gaps". `limit order` **is** carried, by `ka-crossref-07`. The token test is restated as running on **URL-decoded** query text, the decoded inventory is archived at `ka-query-token-inventory.json`, and the conclusion is replaced: `parimutuel`, `dealer` and `specialist` were never operationalised — a real and narrow defect — but **no demonstrated vocabulary gap is claimed for any of the four genuine known-item misses**, whose cause is undetermined between vocabulary and the retrieval cap | The round-1 remediation withdrew a wrong premise and replaced it with another wrong premise, then wrote it into the append-only addendum. The round-1 test ran against the stored query strings, in which Crossref forms are `+`-separated and the rest percent-encoded, so it reported every multi-word token absent — including `betting market`, which the same paragraph asserted was present (findings QUANT-2-1, LITERATURE-2-1, both critical) | retrospective, round-2 remediation. G-7 stands; the backward arm is still not executed | 10 |

**A3 was the weakest of the original five** because it was decided *during*
screening rather than before it. **A10 makes it weaker still**, and this record
says so: the "individually-read REVIEW stratum" A3 described was not individually
read either.

**A3's residual risk, corrected from "unquantifiable" to partly quantified
(finding QUANT-1-8).** The risk was previously stated as failing only on a record
whose title **and** abstract contain none of the published tokens. **Only 2,159 of
the 5,249 DEFAULT-X1 records carry an abstract at all: 3,090 (58.9%) were
rule-excluded on title text alone**, and for those the condition reduces to a
title condition. The residual risk is therefore **bounded below by that
3,090-record title-only stratum** — a quantified and materially larger exposure
than "an in-scope record whose title and abstract contain none of the published
tokens" implied. It remains unbounded above without the second screener this
design does not have. Corpus-wide, 4,779 of 8,813 works have an abstract.

### 13.2 The largest limitation: extraction depth and extraction coverage

Three statements, all unwelcome and all true.

1. **No full text was read.** Extraction reached **abstract depth for 116 of the
   149 included records and metadata depth (title, venue, year) for the remaining
   33**. Every claim in section 8 is a transcription of what a record's abstract
   or metadata states. Where an abstract does not settle a point, section 8 says
   so rather than inferring it, and records at metadata depth are named without
   their findings being stated. The frozen protocol's fields **E8** (condition as
   stated), **E9** (quantity measured with its uncertainty), **E10** (model
   objective, state variables, payoff support, applicability conditions), **E12**
   (frictions modelled / assumed away / not mentioned) and **E13** (executability)
   are therefore **partially completed at best**, and E12's "not mentioned" value
   is not distinguishable from "not stated in the abstract" for most records.
   **This decision is now amendment A9** (finding SCOPE-1-2): it was disclosed
   here but never converted into a numbered amendment, although it substitutes a
   different kind of extraction for the one the protocol specifies. It also travels
   in the frontmatter as `extraction_depth:`, so it is not lost to a consumer that
   reads only the header. **And the 33 metadata-depth records fail frozen criterion
   I4** (finding QUANT-1-3): on the frozen text they belong under X8, and their
   inclusion is authorised by amendment **A8**, not by the protocol. A reader who
   declines A8 should read this corpus as **116 included records plus 33 X8
   exclusions**.
2. **1,245 records that reached the end of screening were not resolved**
   (1,188 before amendment A11 moved 57 records from X5 into X11). **545** carry
   X10 and **700** carry X11. **Restated under finding QUANT-1-4**: the previous
   wording said the 545 "passed eligibility" and the 700 were "promoted under the
   transfer clause". Neither happened. Both sets were assigned by token rules over
   titles and abstracts; **no eligibility determination and no promotion decision
   was made for any of the 1,245**. X10 is a keyword-identified candidate stratum
   whose eligibility is **unknown**; X11 is a keyword-identified model-record
   stratum whose eligibility is **UNDECIDED**. Both are capacity gaps, not
   criterion failures, and both are counted inside `n_excluded` only so the frozen
   arithmetic identities hold. A reader who wants the S4 inventory-risk lineage in
   full, or the single-venue favorite-longshot literature in full, will find them
   in the X11 and X10 rows of the verdicts file and **not** in this corpus.
4. **98.3% of the flow's dispositions are keyword-classifier outputs** (finding
   QUANT-1-1, amendment A10). 150 of 8,813 records carry a verdict from a screener
   reading them. This is the limitation that conditions all three above, and it was
   not stated at all in the record as first published.
3. **The extraction-selection rule was the protocol's own objective
   prioritization**, not a budget number: primary objectives O1, O4, O5 plus the
   Kalshi stream and the anchors (amendment A4). The rule was stated before it was
   applied. The count of 149 is its consequence, not a target.

### 13.3 Access gaps, per record and per source

| id | what could not be retrieved | attempts | what could not be extracted as a result |
|---|---|---|---|
| AG-1 | Kalshi filer-published rulebook, `kalshi.com/regulatory/rulebook` | HTTP 429 on the frozen query and on the `-b` and `-c` retries (9 attempts) | The entire S7 fee, settlement, position-limit, membership and market-maker record (S7-5). **Six** generalized claims in section 8 are marked `not-transferable-as-stated` or conditioned because of it; the enumeration is **the G-3 table in section 10 and is not repeated here**, so the count cannot drift between the two sites again (finding REV-2-4 — this cell reported the pre-REV-1-2 count of two and named only the two original sites while G-3 listed five). Both J5 second-hand fee claims are unverifiable |
| AG-2 | 17 CFR 40.11 text via eCFR | HTTP 200 access interstitial on the frozen query and on the `-b` (5) and `-c` (9) retries | Any statement about the regulation's content (S7-6) |
| AG-3 | Semantic Scholar topical arm, `ka-s2-01` … `ka-s2-04` | HTTP 429 on all four frozen queries and on all four `-b` retries and all four `-c` retry-until-200 runs (12, 12, 9 and 9 attempts) | **One of the four named bibliographic databases contributed zero records to the corpus.** The Semantic Scholar `/paper/search` endpoint refused every unauthenticated request; only its `/citations` endpoint responded |
| AG-4 | Semantic Scholar forward-citation arm for anchor A3 (`10.1086/655844`) | HTTP 404, 6 retry attempts, stored in `ka-fc-s2-a3-p001.json` with `"error": "Paper with id DOI:10.1086/655844 not found"` | The S3 anchor's citing set was retrieved on one tool (OpenAlex, 321/321) rather than two. **The section-2 provenance table recorded this row as HTTP 200 until this remediation and is corrected** (findings REV-1-11, LITERATURE-1-8); every other row in that table was re-checked against its own stored log and agrees |
| AG-5 | Full texts, all 149 included records | Not attempted within this execution | See 13.2 |
| AG-6 | RePEc/IDEAS via the frozen GET endpoint | HTTP 200 with a structurally empty results page, twice | The frozen RePEc arm contributed zero records; the amendment-A2 POST arm contributed 20 from a platform-reported 830 and 121, which is itself a depth truncation |
| AG-8 | Full text of Gomez-Gonzalez & Del Corral 2018 via its own DOI | Handle System resolves (`responseCode` 1); the registered target URL returns HTTP 404 | The record is carried at abstract depth only and cannot be deepened through its identifier |
| AG-7 | Abstracts for 33 included records | Requested from Crossref, OpenAlex, arXiv, Semantic Scholar and DOI content negotiation; none returned one | Those records are carried at metadata depth and their findings are not stated. **On the frozen text they fail I4 and belong under X8**; their inclusion is authorised by amendment A8 (finding QUANT-1-3) |
| **AG-9** | **SSRN site search, as a supplementary arm** | **Not run.** The frozen protocol's section 3.1 "SSRN caveat, declared in advance" made this arm conditional on browser access and required that, if not run, "the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence" | **The required gap entry was omitted from this record as first published — a silent deviation** (finding LITERATURE-1-7, amendment A7). SSRN was reached only through two Crossref container-restricted queries capped at `rows=20` against platform-reported totals of 10,991 and 1,093. **31 of the 149 included records, and 15 of the 19 Kalshi-specific records, carry `10.2139/ssrn.*` DOIs** (15 corrected from 13, finding REV-2-6), so the un-run arm sits on top of the corpus's densest and least peer-reviewed stratum. Reported as gap G-9 |
| **AG-10** | **Registrant metadata for `10.11179/ker.74.119`** (Tanaka, *The Kyoto Economic Review*) | Queried at `api.crossref.org` (HTTP 404) and `api.datacite.org` (not found) during the round-1 metadata sweep; its registration agency is neither | The other **148** of 149 store DOIs were verified against a registration agency (122 Crossref, 26 DataCite). This one's year, container-title and type are carried from the CSL-JSON store **unverified against a registrant**. Its Handle System resolution passes (`responseCode` 1) |

### 13.4 Known-item recall check — reported per item, with no pass threshold

The frozen protocol sets **no numeric recall target**, because a threshold would
be an unlabelled constant, and requires per-item reporting instead. **16 of 23
known items were retrieved independently of their own direct fetch.** The seven
that were not split into two kinds, and the distinction matters:

- **Not recoverable by the arm they define — but unexcused elsewhere (3).** KI-01
  Oliven & Rietz, KI-18 Glosten & Milgrom and KI-23 Levitt are themselves
  forward-citation anchors A1, A6 and A5. A citing set contains the works that cite
  the anchor, never the anchor itself, so these three could not have been recovered
  by **that one arm**. **Corrected under findings REV-1-9 and LITERATURE-1-6:** the
  previous wording called them "structural, not a recall failure", which
  over-excused them. The exculpation covers exactly one arm. **The 35 topical
  queries, the other five anchors' citing sets, the known-item arm and the
  supplementary arms also failed to retrieve all three, and that failure is not
  excused by anything.** Stated correctly: *not recoverable by the forward-citation
  arm they define; also not retrieved by any topical query, which is an unexcused
  topical-strategy miss.* **The honest topical-arm miss count is therefore 7 of 23**,
  alongside the 16-of-23 any-arm figure. A reader must not read 16/23 as 16/20.
- **Genuine per-item recall failures of the topical strategy (4).** KI-06 Rhode &
  Strumpf, *Historical Presidential Betting Markets*; KI-09 Thaler & Ziemba,
  *Anomalies: Parimutuel Betting Markets*; KI-20 Ho & Stoll, *Optimal dealer
  pricing*; KI-21 Avellaneda & Stoikov, *High-frequency trading in a limit order
  book*. **Interpretation, withdrawn and replaced (findings REV-1-9, LITERATURE-1-6).**
  The previous reading was: two are S3 classics whose titles use vocabulary the
  strategy carries — *"parimutuel", "betting markets"* — so their non-retrieval
  indicates the retrieval **caps** rather than the vocabulary; the other two are S4
  inventory-risk anchors missed for the same reason; therefore **retrieval depth,
  not vocabulary, is this strategy's binding constraint**.

  **The supporting premise was factually wrong, and the round-1 replacement for it
  was wrong too.** Round 1 withdrew the depth-not-vocabulary reading on the ground
  that `parimutuel` appears in no query, and replaced it with the assertion that
  `dealer` and `limit order` likewise appear in none, so that KI-20 and KI-21 are
  *demonstrated* vocabulary gaps. **The `limit order` half of that assertion is
  false** (findings QUANT-2-1, LITERATURE-2-1, both critical). The round-1 token
  test was run against the query strings **as stored**, in which the Crossref forms
  are `+`-separated and the arXiv / OpenAlex / Semantic Scholar forms are
  percent-encoded; on that basis `limit order` and `betting market` are *both*
  absent, and the previous paragraph asserted the first and denied the second. The
  test is only meaningful on **URL-decoded** query text, and it is now stated,
  re-run on that basis, and archived.

  **Token inventory of the search strategy, re-derived mechanically.** The test
  input is the 45 fenced topical query blocks of section 3 — which are the 35
  frozen topical queries of protocol section 3.1 plus 10 retry re-issues
  (`ka-s2-0{1..4}-b`, `-c`, `ka-repec-0{1,2}-supp`) — percent-decoded, with `+`
  mapped to space and case-folded. The script and its output are archived at
  [ka-query-token-inventory.json](docs/literature/search_logs/kalshi-arbitrage/ka-query-token-inventory.json).

  | token | present in the decoded topical strategy? | carried by | executed with a 200 and a non-zero count? |
  |---|---|---|---|
  | `parimutuel` (and `pari-mutuel`, `pari mutuel`) | **no** | — | — |
  | `dealer` | **no** | — | — |
  | `specialist` | **no** | — | — |
  | `limit order` | **YES** | `ka-crossref-07` | yes — 20 records retrieved against a platform-reported 79,887 |
  | `order book` | **YES** | `ka-crossref-07` | yes — same query |
  | `inventory risk` | **YES** | `ka-crossref-07`, `ka-openalex-06`, `ka-s2-02` | two of three: `ka-crossref-07` (20 / 79,887) and `ka-openalex-06` (25 / 659); `ka-s2-02` returned zero (AG-3) |
  | `market making` | **YES** | `ka-arxiv-03`, `ka-crossref-07`, `ka-crossref-13`, `ka-openalex-06`, `ka-s2-02` | four of five; `ka-s2-02` zero |
  | `betting market` | **YES** | `ka-crossref-05`, `ka-crossref-15`, `ka-nber-02` | yes, all three |

  **What that settles, and what it does not.** It settles that three title strings
  — `parimutuel` (KI-09), `dealer` (KI-20), `specialist` (KI-18) — were named in the
  protocol's vocabulary paragraph and **never operationalised in any query**. That
  is a real and narrow defect of the strategy, and it is reported as one. It does
  **not** settle that vocabulary is why those items were missed, for two reasons the
  record has to state rather than argue past: every platform here matches a
  bag-of-words relevance query over title, abstract and container, not an exact
  phrase gate, so a record can be retrieved on tokens other than the ones in its own
  title — Thaler & Ziemba's title also contains *betting markets*, which **is**
  carried by three executed queries, and Ho & Stoll is squarely the subject
  `ka-crossref-07` and `ka-openalex-06` asked for; and the rank-and-position
  evidence that would discriminate the hypotheses was not extracted.

  **Restated, for all four genuine misses:** *the cause is undetermined between
  retrieval cap and vocabulary, and this record's evidence does not settle which
  constraint bound.* No demonstrated vocabulary gap is claimed for any of the four.
  For **KI-21** in particular the live explanation is the retrieval cap, not
  vocabulary: `ka-crossref-07` asked for *market making inventory risk optimal bid
  ask quotes limit order book* and returned `rows=20` against a platform-reported
  **79,887**. For **KI-20** both explanations remain open: `dealer` was never asked
  for, but the query that would have been expected to retrieve it was itself capped
  at 20 of 79,887 and 25 of 659. The discriminating test — whether the missed items
  appear anywhere in the platform-reported result sets below the cap — is in the
  retained `ka-*.json` logs and **was not extracted**; it is named here as the test
  a successor stage should run rather than asserted as if it had been run. A
  successor acting on the round-1 wording would have added vocabulary that
  `ka-crossref-07` already carries and left the cap untouched.

The per-item record is
[ka-known-item-recall.json](docs/literature/search_logs/kalshi-arbitrage/ka-known-item-recall.json).

### 13.5 Depth truncation

Every query whose platform-reported total exceeded its retrieval cap is a
depth-truncation gap, and the table in section 2 preserves both numbers for all 86
rows. The severe cases: all fifteen Crossref queries retrieved 20 records against
platform totals between 1,093 and 4,458,996; the six OpenAlex queries retrieved 25
against totals between 64 and 2,060; `ka-arxiv-02` retrieved 50 of 198 and
`ka-arxiv-06` 50 of 61; both NBER queries retrieved 50 against a reported 21,594;
and the supplementary RePEc arm retrieved 10 of 830 and 10 of 121. **The
forward-citation arms are the exception and the reason the corpus is not simply a
function of the caps**: they ran uncapped and retrieved 7,855 of 7,855 reported
citing works on OpenAlex.

### 13.6 What this record is not

Repeating the frozen protocol's section 9.1 so that no downstream artifact
inherits a false claim. This is **not a systematic review**. Screening was
**single-pass**, and — corrected under finding QUANT-1-1 — it was
**overwhelmingly not performed by an agent reading records at all**: 8,663 of
8,813 dispositions are outputs of a published keyword classifier and 150 are
read-based (section 6, amendment A10). Extraction was **single-extractor** and
reached **no full text** (amendment A9); **no
risk-of-bias assessment was performed** and none is claimed, because RoB 2,
QUADAS-2 and PROBAST do not map onto these study types and an unvalidated
single-assessor instrument would produce an uninterpretable number. The evidence
tiers recorded per record are **not** a certainty-of-evidence assessment and must
not be reported as one. No inter-rater agreement statistic exists. No reporting-bias
assessment was performed: funnel-plot methods need a common effect estimate and
standard error, which this corpus does not have. The nineteen PRISMA 2020 items
this design does not meet are **1, 2, 8, 9, 11, 13b, 13c, 13d, 13e, 13f, 14, 15,
18, 19, 20b, 20c, 20d, 21, 22**; item 12 is **inapplicable with rationale** rather
than unmet, because the corpus's objects are stated conditions, model
specifications and heterogeneously-measured discrepancies, not effect measures for
a common outcome.

### 13.7 Scope boundaries honoured

No Kalshi market data was acquired; no exchange trading or market-data API was
called; no price was computed; **no tradeable rule is stated anywhere in this
record**. Where a record states a rule of its own, its attribution status is
recorded (E14) and the rule is not restated as established (see 8.1.2 and 8.6.1).
**The separation rule, restated to what is true after repair (finding
LITERATURE-1-12).** This paragraph previously asserted as an absolute that every
claim generalized from Betfair, the Iowa Electronic Markets, PredictIt,
Polymarket, sportsbook or racetrack data appears in a generalized block with its
carrying assumption on the same line, "never in a Kalshi-specific block". **That
was false as written.** Two mixed-venue records had non-Kalshi material stated
inside Kalshi blocks with no carrying assumption: at 8.3.1 a cross-platform record
was reported as finding "a statistically significant bias on both" with "a stated
cross-platform contrast in sign", both of which are joint Kalshi/Polymarket
claims; and at 8.2.1 implied-volatility surfaces, risk-neutral densities and
variance risk premia were reported from a 113,338-contract sample the record's own
title says spans Kalshi **and** Polymarket. Both are split in this remediation —
the Kalshi-measured part stays in the K block, the rest moves to the generalized
block with its assumption written on the line — and both moves are labelled at
both sites.

**What is true after the split:** every claim in this record generalized from
another venue appears in a **generalized** block with its carrying assumption on
the same line. **What this record no longer claims:** that this was true of the
artifact as first published, or that the separation rule was observed without
exception during synthesis. It was not, and the exception is named above.
Mixed-venue records are the failure mode: their Kalshi arm and their other-venue
arm must be stated separately or not at all.

### 13.8 Reproducibility record for the execution and remediation runs

**Finding QUANT-1-7.** The project contract (CLAUDE.md, *Reproducibility
contract*) requires a 13-field ReproLog per artifact-producing run at
`logs/reproducibility/repro_log_{run_id}.json`, a per-run sidecar at
`artifacts/runs/{HID}/[stage{N}/]{run_id}/sidecar.json`, and — because both paths
are gitignored and resolve in no fresh clone — requires a **tracked deliverable to
cite the SHA-256 of each alongside the git HEAD, labelling the path as an untracked
locator and never the path alone**.

**The search-execution run emitted neither.** `logs/reproducibility/` holds a
registration-phase log for this protocol (`config_resolved_sha256` =
`99524df02696…`, phase `register`, git HEAD `8aeebfe`) and **no log for the search
execution**; `artifacts/runs/` is empty, so no sidecar exists. The frontmatter
carried `git_head_at_authoring` only, with `pip_freeze_sha256` and
`dataset_checksums` stated as `n/a`. That is a contract breach, not a design
choice, and it is recorded as one.

**This is the citation site. The lead session is emitting the ReproLog and the
sidecar for the combined execution + round-1-remediation run and will supply the
digests.** Fill exactly these five frontmatter keys and this table; nothing else
in this record depends on them:

| key | where it goes | what to fill |
|---|---|---|
| `repro_log_path` | frontmatter | `logs/reproducibility/repro_log_{run_id}.json` — **label it an untracked locator** |
| `repro_log_sha256` | frontmatter | 64-hex SHA-256 of that file |
| `sidecar_path` | frontmatter | `artifacts/runs/{HID}/{run_id}/sidecar.json` — **untracked locator** |
| `sidecar_sha256` | frontmatter | 64-hex SHA-256 of that file |
| `pip_freeze_sha256` | frontmatter | 64-hex SHA-256 of the archived pip-freeze for the Python 3.11 environment the scripts ran in |

The clone-durable carrier for the two digests is the provenance commit itself, via
its `Repro-Log-Path:` and `Repro-Log-SHA256:` trailers. **All five keys were
filled by the lead session on 2026-09-02** and QUANT-1-7 is closed at the
frontmatter. **Four** scope limits stand, and the contract is satisfied only
within them.

1. **The ReproLog covers the SEARCH-EXECUTION run only — not the remediation
   run, and not the protocol-drafting stage.** Corrected 2026-09-02 after audit
   findings REPRODUCIBILITY-2-2 and QUANT-2-7; the first version of this
   paragraph claimed it covered the remediation run, which is impossible: the
   log's `git_head` is `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`, the
   registration commit, which **predates** every remediation edit. The
   remediation run's environment is not captured by any ReproLog; its HEAD is
   the delivering provenance commit. The protocol-drafting stage emitted no
   ReproLog at all.
2. **The archived pip-freeze bounds rather than pins.** It describes the lead
   session's interpreter; the search scripts ran on the Python 3.11 standard
   library alone.
3. **The sidecar was edited by round-2 remediation and its digest moved.** The
   published `sidecar_sha256` is now
   `7207fad1866437d188f621e13042ac9a3e95481e46490d3f28949426880e2a67`, superseding
   `96c4134c03f247edc2837e178525a9f215fb8eeb2ab30ca3b9ac53a5e1d5647a`. Two changes,
   both disclosure-only: the `unresolved` block's `X10_eligible_not_extracted` key
   is renamed `X10_keyword_candidate_unextracted` (finding **QUANT-2-3** — the old
   name asserted, to any tool reading only the sidecar, the eligibility
   determination amendment A10 struck), with the old name and the reason retained
   beside it; and `protocol_sha256_with_addendum` is advanced to `21a77d1084…` with
   the superseded `42bc6116…` retained. **No count in the sidecar changed.** A
   reader holding the earlier digest is holding the pre-round-2 file.
4. **The pip-freeze digest was wrong when first published and is now correct.**
   Audit findings REPRODUCIBILITY-2-1 and QUANT-2-7 established that
   `pip_freeze_sha256` did not verify against the bytes of the file it named.
   Cause: the lead session hashed the LF-terminated string but wrote the archive
   in text mode on Windows, which substituted CRLF, so the stored bytes hashed
   to `379614727648a27e…` while the published digest was the LF digest
   `51760dc96e6ea3cb…`. The archive has been rewritten with LF line endings; the
   content is unchanged and the published digest now verifies byte-exactly
   against the file. The digest was never re-derived to match the file — the
   file was corrected to match the digest. **Verified on 2026-09-02 after the
   rewrite:** `logs/reproducibility/env/51760dc9….txt` is 3,233 bytes with **zero**
   CRLF sequences and hashes raw to `51760dc96e6ea3cb…`, which is both its
   content-addressed filename and the published `pip_freeze_sha256`. **Residual,
   recorded not hidden:** the superseded CRLF copy
   `379614727648a27e….txt` is still present in the same untracked directory, so a
   reader handed that directory sees two files; only the LF one is the digest the
   frontmatter and the ReproLog name.

The sidecar carries **both** disposition tables — as first published and post-A11
word-boundary — so a reader can see what the bug-fix moved.
`git_head_at_authoring` is `27d74738aa35ec1cdf1ec6915b50532e3620ea6f` for the
execution run; the remediation run's HEAD is the follow-on provenance commit, which
must also carry the current protocol-with-addendum digest
`21a77d10841ba7f15ea58d5a58a1bca57818b2ed1a0f3bf53a1dbce6a8dcc53b` (amendments
A1-A15), **not** the superseded `42bc6116…` recorded at amendment A12.

Determinism, which is the other half of a reproducibility claim, is handled by
amendment A11 and reported in section 5.

### 13.9 Audit remediation — traceability, one row per finding

**Two rounds are recorded here, round 1 first and round 2 second.** Every edit
made under either is traceable to a finding id in these tables, and every edit site
also carries the finding id inline. The refuted findings of each round are named
below the tables so that a later round does not re-raise them.

**This table over-reported its own edits in round 1, and that is corrected rather
than quietly repaired (findings REV-2-2, REV-2-3).** Three rows named an edit site
that did not exist or an edit that was not made: two cited *"Read this first"*
numbered items in a block that contained none, and one recorded the `prisma-s-9`
offsetting claim as withdrawn when that paragraph was never touched. The
corresponding edits **have now been made** — the numbered items exist and
`prisma-s-9` is rewritten — and each affected row says so explicitly and dates it
to round 2. **A traceability table that over-reports is worse than none**, because
it converts an unmade edit into a verified one; the rule adopted here is that a row
may name only a site whose text was actually changed, and any row whose site was
added later carries the round that added it.

#### Round 1 — 37 findings survived the adversarial refute gate (3 critical, 34 major); 4 were refuted and dropped

| finding | severity | what was wrong | where the fix is |
|---|---|---|---|
| **QUANT-1-1** | critical | 3,414 keyword-rule outputs were presented as individual screening verdicts; the item-8 declaration named only the 5,249-record DEFAULT-X1 partition | Amendment **A10**, completed by **A13** at round 2; frontmatter `screening_verdict_source`; section 5 flow and its by-stratum split table; the PRISMA 2020 item-8 block; section 6 preamble and the `verdict source` column; 13.2 item 4; 13.6; `ka-screening-script.py` header + emitted `automation_tools` / `note`. **Row corrected (REV-2-2):** it named *"Read this first" item 2*, and that block had no numbered items in round 1. The item exists now — it is **item 1** — and was **added at round 2**, not round 1. |
| **REV-1-2** | critical | Kalshi called order-driven at 8.3.2 and quote-driven at 8.4.1; the order-driven premise sourced to a DCM designation category | 8.3.2 Levitt entry (mechanism assertion removed, marked `not-transferable-as-stated`); 8.4.1 (quote-driven attributed to the source record); G-3 count raised from two to five in round 1, **and to six at round 2 under REV-2-8**, which found a residual venue-mechanism presupposition surviving this fix at 8.4.3 |
| **QUANT-1-2** | major | X5 matched unanchored substrings (`dex` in *index*, `amm` in *programming*) | `ka-screening-script.py` `BOUNDED` / `any_defi`; verdicts re-emitted; section 6 before/after table (X5 159→94, X11 643→700, X7 236→244); amendment **A11**; every downstream count. **Both declared departures adjudicated UPHELD at round 2 (QUANT-2-9); their evidence corrected** — three records → two, and the 289/305 and 83/128 statistics labelled as bare-pattern measurements with 284/305 and 64/128 added |
| **REV-1-3** | major | Thaler & Ziemba endpoint premise discharged against a CFTC record that does not establish settlement | 8.3.2 Thaler & Ziemba entry; G-3 row 3 |
| **REV-1-4** | major | A single T5 abstract said to "establish" the Shin precondition on the venue | 8.3.2 Shin entry (verb downgraded, tier carried, superlative removed) |
| **REV-1-5** | major | The flow narrative asserted every screened record was read | Section 5 flow paragraph |
| **REV-1-6** | major | The A3 pre-sorter's true reach was not recoverable from the record | Superseded in substance by A10 (the answer is 8,663, all of them); the per-rule split is published in section 6's X1 row and in the verdicts header's `counts_by_rule` |
| **REV-1-7** | major | Kalshi non-independence understated: 15-of-19 T5, one author group | 8.3.1 concentration caveat; G-6 (17 of 19; seven from two groups) |
| **REV-1-8** | major | Frontmatter and section 5 published 8,664 as one number; X10/X11 under `eligibility_exclusion`; "Read this first" named neither largest limitation | Frontmatter `disposition_codes_added` + three new count keys; section 5 `n_excluded` split table. **Row corrected (REV-2-2):** the *"Read this first" items 1-4"* this row claimed were **not written in round 1** — the block contained no numbered items and named neither largest limitation, so the substance of this finding went unfixed at the one site it named while being fixed everywhere else. **The four items were added at round 2** and are the site now. |
| **REV-1-9** | major | Depth-not-vocabulary reading rested on a token no query carries; three misses over-excused | 13.4, both bullets. **Superseded in part at round 2 (QUANT-2-1, LITERATURE-2-1):** the round-1 replacement reading was itself false, and 13.4 is rewritten around a mechanically derived token inventory |
| **REV-1-10** | major | Corpus-level universal negatives stated without depth and screening qualifiers | 8.4.1 model bullet; 8.5.2 capital-lockup bullet; G-2; G-4 |
| **REV-1-11** | major | `ka-fc-s2-a3` row showed HTTP 200 against a stored 404 | Section 2 table row + whole-table re-check note; AG-4 |
| **REV-1-12** | major | Section 4's recall statement omitted AG-3, the largest failure | Section 4 mitigation (iv), rewritten as (a)-(e); new gap G-8. **Row corrected (REV-2-3):** it recorded *"the `prisma-s-9` offsetting claim withdrawn"*, and `prisma-s-9` was **never edited in round 1** — it still asserted the offsetting conclusion, contradicting both section 4 and G-8. **`prisma-s-9` was rewritten at round 2**, and the withdrawal is now stated there with a per-query execution table. Round 2 also found the round-1 replacement wording ("in execution the narrowing is not offset") **too strong**: three of the four offsetting queries did execute and did return records. |
| **REV-1-13** | major | Amendments lived outside the protocol's own addendum; two required elements missing | Amendment **A12**; protocol addendum now carries A1-A15 (A13-A15 added at round 2); 13.1 table gains `why` and `PRISMA-P item(s)` columns |
| **SCOPE-1-1** | major | Backward arm dropped without a numbered amendment | Amendment **A6**; cited at `prisma-s-5` and G-7 |
| **SCOPE-1-2** | major | Zero-full-text extraction never converted into an amendment | Amendment **A9**; frontmatter `extraction_depth`; 13.2 item 1 |
| **SCOPE-1-4** | major | X10/X11 inside `eligibility_exclusion` contradicted section 1 | Frontmatter `disposition_codes_added`; section 1 |
| **QUANT-1-3** | major | 33 metadata-depth includes fail frozen I4; frontmatter reworded X8 without authority | Amendment **A8**; frontmatter X8 line restored to the frozen wording; section 6 X8 paragraph; 13.2; AG-7 |
| **QUANT-1-4** | major | X10/X11 described in eligibility terms the execution cannot support | Section 1; section 6 rows; 13.2 item 2; frontmatter; `ka-screening-script.py` `RULES` and `REASON`. **Four sites survived and are fixed at round 2 (QUANT-2-3):** section 1's *"X10 marks records that passed eligibility"*, two itemized section-6 reasons, the frontmatter key `n_eligible_not_extracted` and the sidecar key `X10_eligible_not_extracted` |
| **QUANT-1-5** | major | Three synthesis claims rested on unestablished venue-structural facts | 8.3.2 (×2), 8.4.2; G-3 |
| **QUANT-1-6** | major | Pipeline non-deterministic; published Table X-full row ids irreproducible | `ka-dedup-script.py` total tie-breaks + seed guard; new `ka-partition-script.py`; section 5 determinism paragraph; frontmatter `rng_seed`; amendment **A11**. **Evidence corrected at round 2 (QUANT-2-2, QUANT-2-6, REPRODUCIBILITY-2-3, REPRODUCIBILITY-2-5), amendment A14:** the tie-break counterfactual did not reproduce, the `identifier` join is null for 21.4% of rows, and the 2,630 / 6,183 row-id magnitudes are unverifiable because the pre-remediation file was overwritten |
| **QUANT-1-7** | major | No ReproLog, no sidecar, no digests cited | **Section 13.8** (citation site); five frontmatter keys, filled by the lead session 2026-09-02 with the two digests and the pip-freeze SHA. **Closed within the four scope limits now stated at 13.8** — two at round 1, two added at round 2 (REPRODUCIBILITY-2-1/2-2, QUANT-2-7 for the pip-freeze digest and the ReproLog's coverage; and the sidecar digest advanced by the QUANT-2-3 key rename). |
| **QUANT-1-8** | major | A3 residual risk called unquantifiable when a lower bound is computable | Section 6 closing paragraph; 13.1 closing paragraph (3,090 title-only) |
| **LITERATURE-1-1** | major | ~20 publication years wrong against registrant and against the store | Section 7 table regenerated (27 year cells); 18 section-8 citation years re-derived; section 7 legend states the field and the print/online convention. **Qualified at round 2 (LITERATURE-2-3):** the convention's stated ground was false for the `10.5750` retro-registered stratum, and five year cells plus their claim lines are corrected under a documented exception |
| **LITERATURE-1-2** | major | ≥9 container-titles wrong; venue is the field tier derives from | Section 7 table regenerated (78 venue cells); legend lists the tier-relevant ones |
| **LITERATURE-1-3** | major | 4 records carried two different tiers | Six found, not four; section 7 tier-reconciliation table; 2 table cells and 4 claim lines corrected. **Extended at round 2 (LITERATURE-2-4):** the check compared this artifact against itself and so could not see a preprint row whose venue a registrant records; all 25 arXiv rows are re-checked against the arXiv record and Chen & Pennock moves T5→T1 |
| **LITERATURE-1-4** | major | "The CFTC record establishes…" for three venue facts it does not | Same three sites as QUANT-1-5; G-3 |
| **LITERATURE-1-5** | major | Glosten-Harris 1988 conflated with Glosten & Milgrom 1985 | 8.4.3 Glosten & Milgrom entry (transfer sentence withdrawn); Kyle entry (bridge affirmed, because Kyle's lambda is Kyle's) |
| **LITERATURE-1-6** | major | Known-item reading over-broad and contradicted by the strategy | 13.4, both bullets. **Superseded in part at round 2** — see REV-1-9 above |
| **LITERATURE-1-7** | major | SSRN caveat's declared-in-advance gap entry never recorded | Amendment **A7**; AG-9; G-9; `prisma-s-4` |
| **LITERATURE-1-8** | major | Same HTTP-status defect as REV-1-11 | Section 2 table row; AG-4 |
| **LITERATURE-1-9** | major | 3 included records with an affirmative role column appear nowhere in section 8 | **19** found, not 3; three added to 8.6.1 and 8.1.2; new **section 8.8** lists the other 16; their section-7 role column corrected. **Section 8.8 was itself defective and is corrected at round 2** (REV-2-5, QUANT-2-4, QUANT-2-5, LITERATURE-2-5): it miscounted its own depth column 11/5 against a true 9/7, listed six names under "five", omitted Oliven & Rietz, and carried a non-resolving Berg DOI |
| **LITERATURE-1-10** | major | G-6 said 15 of 19 T5; the table shows 17 | G-6; 8.3.1 |
| **LITERATURE-1-11** | major | Item-13a grouping declared mechanical from E3 but reconstructed | Section 1 grouping-rule correction; `[synth Sn]` suffix on 10 rows of the section-7 `strand(s)` column; legend |
| **LITERATURE-1-12** | major | Non-Kalshi evidence inside Kalshi blocks; 13.7 asserted the opposite as an absolute | 8.2.1 / 8.2.2 (Lee et al. split); 8.3.1 / 8.3.2 (Gupta split); 13.7 weakened to what is true after the split |
| **LITERATURE-1-14** | major | S4 header stated a positive claim about non-statement the corpus cannot carry | 8.4 header paragraph |
| **LITERATURE-1-15** | major | Frontmatter contradicted the body on the 1,245 unresolved records | Frontmatter `disposition_codes_added` + count keys |

**Refuted at the round-1 gate and NOT acted on — do not re-raise:**
**REV-1-1** and **QUANT-1-9** (both claimed the central S4 finding is a universal
negative the corpus cannot state — the claim as now written at 8.4 is bounded to
the records assessed and the depth reached, which is what LITERATURE-1-14
required); **SCOPE-1-3** (claimed the flow accounting silently absorbs the
unresolved records — it does not; they are named at every site and now in the
frontmatter too); **LITERATURE-1-13** (claimed E14 attribution determinations are
not determinable at abstract depth).

#### Round 2 — 33 findings survived the adversarial refute gate (2 critical, 31 major); 3 were refuted and dropped

**The pattern round 2 identified, stated before the table because it is the point.**
Both surviving criticals are the same failure: a round-1 remediation **withdrew a
wrong premise and replaced it with another wrong premise**, in each case a false
factual claim about this artifact's own queries. Three further findings caught the
13.9 table naming edit sites that were never edited. The lesson recorded here as a
standing rule for this branch: **a withdrawal that overshoots is as damaging as the
original error, and a claim about what a remediation just changed is a claim like
any other and must be verified against the file, not against the intention.**

| finding | severity | what was wrong | where the fix is |
|---|---|---|---|
| **QUANT-2-1** | critical | 13.4 asserted that `limit order` appears in **none** of the topical queries and concluded that KI-21 is a demonstrated vocabulary gap. False: `ka-crossref-07` carries it. The token test had been run on the stored (`+`-separated / percent-encoded) query strings, so it also reported `betting market` absent while the same paragraph asserted it present | **Section 13.4 rewritten** around a mechanically derived token inventory table; new archived artefacts `ka-query-token-inventory.py` / `.json`; amendment **A15**. The recall conclusion is re-derived: no demonstrated vocabulary gap is claimed for any of the four genuine misses |
| **LITERATURE-2-1** | critical | The same false claim, written into the append-only protocol addendum as part of **A6** | Amendment **A15** strikes A6's *"neither term appears in any of the 35 frozen topical queries"* and its *"two demonstrated vocabulary gaps"* conclusion by quotation. A6 is not edited; it is superseded |
| **REV-2-1** | major | A10's strike was incomplete and A12 propagated the unstruck A3 text into the protocol addendum, so the protocol and this record contradicted each other on individual reading | Amendment **A13** strikes five further A3 assertions by quotation; `SUPERSEDED IN PART BY A10 AND A13` banner inserted at the head of A3 in `ka-protocol-amendments.md` **and** in the protocol addendum; protocol-with-addendum digest re-recorded as `21a77d1084…` |
| **SCOPE-2-5** | major | Same defect seen from the provenance side | Same fix — amendment **A13** |
| **REPRODUCIBILITY-2-7** | major | Same defect seen from the reproducibility side; asked specifically for a strike-don't-delete supersession note inside the addendum | Same fix — amendment **A13**; the banner adds a pointer and removes nothing, and A3's text is retained unedited so the strike is checkable against it |
| **REV-2-2** | major | Two round-1 traceability rows cited *"Read this first"* numbered items that did not exist | **"Read this first" gains items 1-4** (98.3% classifier dispositions; 1,245 unresolved; no full text read; 33 metadata-depth includes); the two 13.9 rows are corrected to say the items were added at round 2 |
| **REV-2-3** | major | The REV-1-12 fix never reached `prisma-s-9`, which still asserted the offsetting conclusion and rested it partly on `ka-s2-02`, a query that returned zero | **`prisma-s-9` rewritten** with a per-query execution table; **section 4** and **G-8** restated. The round-1 replacement wording was also **too strong** and is corrected: three of the four offsetting queries executed and returned records, so no vocabulary was gated out entirely; what was lost is redundancy and one platform |
| **REV-2-4** | major | The AG-1 row reported the pre-REV-1-2 count of two blocked transfers while G-3 listed five | **AG-1's consequence cell** now states six and **points at the G-3 table instead of re-enumerating**, so the two sites cannot drift apart again |
| **REV-2-5** | major | 8.8 mis-described its own 16-row table: eleven/five against a true nine/seven, six names under "five", Oliven & Rietz omitted | **Section 8.8 closing paragraph** restated to 9 metadata / 7 abstract with all seven named; counts generated from the table's own `depth` column |
| **QUANT-2-4** | major | Same miscount, framed as understating unforced synthesis omissions by two | Same fix — section 8.8 |
| **LITERATURE-2-5** | major | Same miscount plus the non-resolving Berg DOI | Same fix, and the Berg cell corrected to `10.1016/s1574-0722(07)00080-7` |
| **QUANT-2-5** | major | 8.8 cited Berg under `10.1007/s15740722070` — the store key with a Springer prefix pasted on, resolving nowhere — and the gate verdict on file predated the remediated document | Berg cell corrected; **the research-compile gate re-run against the remediated document and `ka-gate-verdict.json` re-recorded**; section 12 disposition restated against the new run |
| **REV-2-8** | major | 8.4.3's bookmaker entry asserted unconditionally that E6 blocks the transfer *"to an order-driven exchange"*, deciding a transfer on the venue mechanism the record says it cannot establish | **8.4.3 clause made conditional** and re-marked `not-transferable-as-stated`; **G-3 gains a sixth mark** naming this site |
| **LITERATURE-2-7** | major | The enumeration of which strata make up the 8,663 classifier verdicts summed to 8,813, re-including the 150 read-based records | **Section 5** gains a by-stratum table net of the 150: 5,249 + 2,843 + 571 = 8,663, with the derivation named |
| **QUANT-2-3** | major | A10's restatement of X10 did not reach four sites, three of them in the section the frontmatter NOTE claims was made consistent | **Section 1 line rewritten**; **two section-6 itemized reasons** drop "eligible"; frontmatter key renamed `n_eligible_not_extracted` → **`n_keyword_candidate_unextracted`**; **sidecar key renamed** to match, with the old name and the reason retained beside it |
| **LITERATURE-2-3** | major | 27 year cells were rewritten to the registrant `issued` field on the stated ground that it is the earliest recorded publication date; false for the `10.5750` retro-registered stratum, misdating the canonical LMSR paper by five years | **Documented exception added to the year CONVENTION** in section 7 with the discriminator stated; **five year cells and their claim lines corrected** (Hanson 2007, Abramovicz 2007, Seemann 2008, Bergfjord 2012, Antweiler 2013) against RePEc/EconPapers; evidence archived at `ka-store-retroreg-yearcheck.json`. The store is **not** edited |
| **LITERATURE-2-4** | major | Chen & Pennock cited as a 2012 T5 preprint; it is a peer-reviewed UAI 2007 proceedings paper | **Section 7 row and 8.4.2 claim line corrected** to 2007 / T1 with the arXiv posting recorded as the retrieved manifestation; **all 25 arXiv rows swept** against the arXiv record and the result archived at `ka-store-arxiv-venuecheck.json` (exactly one carries venue evidence) |
| **LITERATURE-2-6** | major | Section-8 claim lines truncated author lists without "et al.", and the artifact elsewhere prints full lists, so truncation was indistinguishable from completeness | **Author-list CONVENTION stated** in section 7 (full list always, no `et al.`); **eight citation forms corrected at ten sites**, regenerated from the store's `author` array; the sweep now returns zero mismatches |
| **QUANT-2-2** | major | A11's *"`X1` 6,672 instead of 6,707"* justification for refusing the tie-break conversion does not reproduce | Amendment **A14(a)** strikes the sentence and replaces it with the measured ground — the list form is seed-invariant (0 differences at every seed pair), the set form is not (19-24) — and section 5's determinism paragraph is rewritten to match. Counterfactual archived at `ka-counterfactuals.py` / `.json`. **The refusal itself stands** |
| **REPRODUCIBILITY-2-3** | major | Same defect, with the additional requirement that the counterfactual patch be archived | Same fix; the patch is generated and run by the committed `ka-counterfactuals.py`, which edits no archived script |
| **QUANT-2-9** | major | Both QUANT-1-2 departures **adjudicated upheld**; departure 2 overstated by one record, and two corpus-wide figures were computed under the rejected bare patterns | Amendment **A14(b)(c)**; section 6 names **two** records, not three, and gives both the bare-pattern (289/305, 83/128) and shipped-pattern (284/305, 64/128) statistics with the pattern labelled on each |
| **REPRODUCIBILITY-2-4** | major | Same defect | Same fix |
| **QUANT-2-6** | major | The prescribed `identifier` join is null for 1,890 of 8,813 rows; the header calls the row id `uid` while the field is `id`; the pre-remediation file was overwritten | Amendment **A14(d)**; verdicts header rewritten and the file re-emitted with `row_ids`, `row_ids_migration_key` and `pre_remediation_file` fields; section 5 states the 6,923 / 1,890 split. The 2,630 / 6,183 figures are **downgraded to an unverifiable assertion** |
| **REPRODUCIBILITY-2-5** | major | Same defect, asking for a crosswalk or the pre-remediation file | **Neither can be produced**: the file was overwritten in place and was never committed, so it is not in git history. That is stated at both sites rather than worked around |
| **QUANT-2-8** | major | The 149-DOI registration-agency sweep authorising 27 year, 78 venue and 18 citation-year rewrites had no archived response artefact | **`ka-store-registrant-sweep.py` / `.json` committed** (one row per DOI) and cited at section 7. Re-running it also corrected two of the numbers round 1 published: **147** year comparisons, not 148, and **94** container comparisons, not 119 |
| **REPRODUCIBILITY-2-6** | major | Same defect | Same fix |
| **SCOPE-2-2** | major | The spec's ticked PASSED check for the search-logs/store item contradicts the delivery on four numbers | **Dated correction note appended under that spec item**, superseding in place without editing the original tick text |
| **SCOPE-2-3** | major | The spec-declared branch agenda did not exist anywhere in the repository | **`docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md` written**, with numbered branches derived from G-1…G-10 and TC-1…TC-5, one branch-level falsification test each and its evidence tier, inside the ADR-0003 boundary |
| **SCOPE-2-4** | major | The audit trail ships under a path no spec item names and covers only Thread C | **Thread D spec item extended** to name the per-branch trail slug in use and to record that Thread B carried no audit round because it was discharged pre-session |
| **REPRODUCIBILITY-2-1** | major | `pip_freeze_sha256` did not verify against the bytes of the archived file | **Closed by the lead session** before this remediation: the archive was rewritten with LF line endings so the published digest verifies byte-exactly. Recorded at 13.8 limit 4 |
| **QUANT-2-7** | major | Same defect | Same fix |
| **REPRODUCIBILITY-2-2** | major | 13.8 claimed the ReproLog covers the remediation run; its `git_head` predates every remediation edit | **Closed by the lead session**: 13.8 limit 1 now states the log covers the search-execution run only |
| **LITERATURE-2-8** | *minor, logged* | One DOI carried two citation years inside the artifact (`10.1007/s11579-012-0087-0`, 2012 in the table and at two claim sites, 2013 at a third) | Logged rather than gated at round 2; **fixed anyway** at 8.6.2, and the whole-document year sweep against the store now returns zero mismatches |

**Three round-2 findings have their edit sites in other tracked files, not in this
record**, so the "finding id inline at every edit site" rule is satisfied there
rather than here: **SCOPE-2-2** and **SCOPE-2-4** in
[docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md](docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md)
(a dated correction note under the Thread C search-logs/store item, and a rename
plus a Thread B coverage statement on the Thread D item), and **SCOPE-2-3** in the
new
[docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md](docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md),
whose frontmatter names the finding. **No spec box was ticked by this remediation**
and no commit was made.

**Refuted at the round-2 gate and NOT acted on — do not re-raise:** **REV-2-7**,
**SCOPE-2-1**, **LITERATURE-2-2**.

**Findings that changed no number in the corpus.** Every round-2 finding is a
correction to what this record or the protocol *says*, or to an artefact that was
missing. **No screening verdict, no disposition count, no eligibility judgement and
no included record moved at round 2.** The nine-code table is `include` 149, `X1`
6,707, `X2` 338, `X3` 35, `X5` 94, `X7` 244, `X9` 1, `X10` 545, `X11` 700 before
and after, and `bibliography_sha256` is unchanged at
`fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164`. What changed is
five citation years, one tier, eight author lists, one identifier, six counts stated
about the corpus, and three amendments' worth of struck assertions.

**QUANT-1-7 was handed back to the lead session and is now closed.** The five
reproducibility keys were filled on 2026-09-02 with
`repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json` (sha256 `416d4d48…`) and
`artifacts/runs/kalshi-arbitrage/8f5b02d3…/sidecar.json` (sha256 `96c4134c…`),
both untracked locators. Section 13.8 states the two scope limits that survive
the fill.

## 14. Works cited by this record beyond the corpus

- McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. *Journal of Clinical Epidemiology*. 2016;75:40-46. https://doi.org/10.1016/j.jclinepi.2016.01.021
- Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *PLOS Medicine*. 2021;18(3):e1003583. https://doi.org/10.1371/journal.pmed.1003583
