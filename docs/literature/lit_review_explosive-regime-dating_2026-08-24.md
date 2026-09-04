---
type: lit_review
review_kind: systematic review (PRISMA 2020)
slug: explosive-regime-dating
date: 2026-08-24
execution_dates: "search and dual screening 2026-08-24; extraction 2026-08-25; synthesis and adjudication 2026-09-02"
protocol: docs/methodology/protocol_explosive-regime-review_2026-08-24.md
protocol_sha256_at_registration: 33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54
protocol_registration_commit: 9deee0c
protocol_sha256_with_addendum: e0df3297c5971735a6f4b610e988087f086e576f4ccb131d2430c8bc353a9184   # A1-A16, 96,223 bytes. A16 appended 2026-09-04 by the round-5 remediation (finding REV-2-4): it strikes A15 section (c)'s 'passes on 9 tests' by quotation and re-attests the mechanical ground against the delivered 10-test module; no appraisal cell and no count changes. Supersedes the A1-A15 value eed7db745ff7fe241f85246c37f8f244890fb23712bf7c712093f3a40f9df9e0 (91,329 bytes) and the A1-A14 value 9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa. Frozen prefix re-verified after every append: the first 51,478 bytes still hash to 33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54
protocol_sha256_with_addendum_A1_A14: 9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa  # superseded by the round-4 append
protocol_sha256_with_addendum_A1_A13: 92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2  # superseded by the round-3 append
protocol_sha256_with_addendum_A1_A11: 0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b  # superseded by the round-2 append
protocol_sha256_with_addendum_A1_A3: c5a4be8d84241f0ea34dfc0f6e08a0c88ee5d4f81d05a6edd934e5db7fb72721  # superseded 2026-09-02
protocol_frozen_prefix_bytes: 51478   # SHA-256 of the first 51478 bytes still equals protocol_sha256_at_registration
amendments_run_under: [A1, A2, A3]
amendments_appended_by_this_document: [A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]   # appended to the protocol addendum, not requested of a consumer session (see 12.5); A12 and A13 are round-2 correcting entries over A7, A10(b) and A11; A14 is a round-3 correcting entry over A13(b) and A9, plus the LF-digest CONVENTION
review_standard: "PRISMA 2020 (Page et al. 2021, doi:10.1136/bmj.n71); search reporting per PRISMA-S (Rethlefsen et al. 2021, doi:10.1186/s13643-020-01542-z)"
registration: "No registry entry. PROSPERO accepts only health-outcome reviews; this is a methodology review. The registration event is the protocol's provenance commit 9deee0c, which predates every execution date in the search logs."
search_logs: docs/literature/search_logs/explosive-regime/
candidate_store: docs/literature/references_explosive-regime-dating.json   # 1,996 deduplicated candidate records
bibliography: docs/literature/references_explosive-regime.json             # 72 included records
bibliography_sha256: 13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521
bibliography_sha256_after_round1: 8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124   # superseded by the round-2 note append
bibliography_sha256_as_first_delivered: 1abbb9d8b253ff2d10c5f021205101ab4bd610812ffd75d8f6bdcde024bbb7dc
counts:
  identified: 4898
  deduplicated_universe: 1996
  duplicates_removed: 2902
  screened_title_abstract: 1996
  excluded_title_abstract: 1410
  assessed_full_text: 586
  excluded_full_text_substantive: 234
  excluded_full_text_unobtainable_X6: 280
  included: 72
  distinct_works_included: 69   # under the 3 twin pairs adjudicated at extraction. 68 under the review's own uniform twin standard, which the fourth pair (eru-0198/eru-0259) meets; the review does not renumber to 68 because that is a re-appraisal of a frozen corpus, not a correction - the refusal is operational, not evidential (VG-13, A13(b), A14(a), round-3 finding LITERATURE-3-2)
agreement:
  cohens_kappa_stage1: 0.433012
  raw_agreement_stage1: 0.806613
consumer: docs/research_notes/research_agenda_regime-classification_2026-08-21.md (branch 3; Definitional basis (d))
ai_assistance: >
  DECLARED PER STAGE against the AI-Assistance trailer on the commit carrying
  each artifact, because this review's original single-model declaration
  conflicts with those trailers and the ReproLog carries no model field, so the
  conflict cannot be resolved from the logs (12.1 L-15, 12.3 VG-11).
  Protocol registration (commit 9deee0c): claude-fable-5.
  Search execution, deduplication, stage-1 and stage-2 screening, both blind
  adjudications, primary extraction and the NB adjudications (commit 8aeebfe):
  claude-fable-5. Independent numeric re-extraction
  (se-extraction-recheck.jsonl): UNRECORDED - the artifact was untracked, so no
  trailer exists for it. Synthesis, appraisal resolution under 2.8, the section
  8 and 9 write-ups, the post-freeze backward-chase diagnostic, this document
  and the round-1 and round-2 audit remediations: claude-opus-5 (Claude Code /
  Claude Agent SDK). Decoding configuration for every stage is UNRECORDED
  (VG-11). Screeners A and B and the blind adjudicator were separately spawned
  context-independent sessions of one base model within a single stage, so the
  kappa reported in 3.3 measures BETWEEN-SESSION variance of the SCREENING stage
  under an UNRECORDED decoding configuration (no temperature, top_p, max_tokens,
  thinking budget or seed is recorded in any artifact; VG-11). It says nothing
  about the synthesis model, and if the extraction passes
  ran under different models the 2.8 divergence rate is partly a between-model
  quantity. Under PRISMA 2020 item 8 the model is declared as the automation
  tool and the sole effective screener class; no human screener exists at any
  stage. Role for this document per ICMJE 2026 disclosure: prose, synthesis,
  adjudication write-up, audit-support. The human author approves by
  committing.
competing_interests: none
ADR_boundary: "ADR-0003 - this review synthesizes PUBLISHED operating characteristics only. No simulation was run, nothing was fitted, no critical value was computed. Bookkeeping computations only: deduplication, Cohen's kappa, dual-pass agreement counts, checksums, DOI handle verification."
---

# Systematic review — operating characteristics and validity conditions of explosive-regime date-stamping methods

## Abstract (PRISMA 2020 item 2)

**Objective.** For real-time explosive-regime date-stamping methods applied to
financial price series — the recursive right-tailed unit-root family and its
direct competitors — establish what operating characteristics (size, power,
date-stamping accuracy and delay, false-alarm behaviour) and validity conditions
are *published*, and what the causality status of each published characteristic
is (real-time versus full-sample). The review exists to discharge a precondition
of branch 3 of the consumer agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md)),
which flagged the Phillips date-stamping records for a full-text pass before any
branch-3 specification cites their critical values quantitatively.

**Design.** PRISMA 2020 systematic review against a protocol frozen and committed
before any query executed
([protocol_explosive-regime-review_2026-08-24.md](../methodology/protocol_explosive-regime-review_2026-08-24.md),
SHA-256 `33c01c5225…` at commit `9deee0c`). Five platforms, 24 topical queries,
four forward-citation arms over the two seed papers, and a 14-item known-item
arm — **the protocol's fifth supplementary arm, backward citation-chasing, did
not run in the execution window**; it was executed only afterwards, over a
frozen corpus, as a recall diagnostic (amendment A11). Dual LLM-agent screening
at title/abstract and at full text, blind adjudication of disagreements,
project-local appraisal instrument ER-RoB v1 — executed with a fourth response
level the frozen instrument does not define (A7) and with domain concerns
recorded as extractor judgments rather than derived by the frozen rule (A8), so
both columns are reported.

**Results.** 4,898 raw records; 1,996 after deduplication; 1,410 excluded at
title/abstract; 586 assessed at full text; 234 excluded on substantive criteria
and 280 excluded as full-text-unobtainable (X6); **72 records included** (69
distinct works plus 3 same-work twins adjudicated at extraction; a fourth pair,
`eru-0198` / `eru-0259`, **meets the same documentary standard as those three**
but was never given twin treatment, so the distinct-work count is
**69 as the review's arithmetic runs and 68 under its own uniform standard** —
the review does not renumber because that is a re-appraisal of a frozen corpus
rather than a correction; §5.4, VG-13, A13(b), A14(a)). Cohen's κ on stage-1 verdicts was 0.433
(raw agreement 0.807). Quantitative pooling was pre-specified as conditional on
matched detector × DGP × T × r₀ across non-overlapping author teams; that
condition is met nowhere in the corpus, so the synthesis is structured narrative
with evidence tables and **no pooled estimates and no vote counting**.

**Principal findings.** Coverage fractions are stated over **assessable
denominators** — 65 records for Q1–Q7 and D1–D6, 53 for Q8/Q9 and D7/D8, and
**63 distinct works for O6** — not
over 72, because 3 twins and 4 no-full-text records cannot contribute a
numerator by construction, and 12 further records were read only at the recheck
pass where Q8/Q9 are unanswerable. Domain concerns are given on the
**rule-derived** column (protocol §6's Q→D rule, amendment A7's CONVENTION for
`partial`) with the extractor's recorded judgment alongside.
(1) The agenda's Rev 3 sentence "date-stamps an explosive state in real time
against derived critical values" is **PARTIAL** on full text: the real-time
property holds for the *sequence* statistics ADF_r (PWY) and BSADF_{r₂} (PSY),
not for SADF/GSADF, which both papers describe as ex-post existence statistics;
and the operational critical values are simulated or a stated divergence
convention, not values delivered by the derived limit theory. (2) **Over the O6
assessable denominator of 63 distinct works** — 69 distinct works minus the 4
with no full text (NE) and the 2 whose text does not state a causality status
(NS), the 3 same-work twins having already been removed with the record set —
**22 (35%) evaluate a detector in genuinely real-time form**; 21 are full-sample
only; 17 use a causal statistic but report only ex-post evaluation; 3 split the
attribution per statistic. The earlier form of this sentence gave 22 / 22 / 19
over 72 records and called 72 "the right denominator": that mixes three of the
six classes with a denominator containing all six, counts three twins twice
under codes inherited from their carriers, and counts four records that were
never read. The record-level partition over all 72 (RT 22, FS 22, CS 19,
SPLIT 3, NS 2, NE 4) is retained in §7.6 alongside the distinct-work partition.
*(Findings REV-2-2, REV-2-3, SCOPE-2-4, QUANT-2-2.)* (3) Date-stamping
accuracy or delay is reported in **23 of 65 assessable records (35%)**; D4
concern is raised by the rule in 42 of 65, recorded high in 41. (4) Multiplicity
across the recursive sequence is addressed in **19 of 65 (29%)**; D6 concern is
raised by the rule in 46 of 65, recorded high in 33. The corpus's only direct
family-wise measurement of the standard PSY dating rule reports FWER 0.55–0.93
— **on working-paper-tier evidence** (`eru-1289` was tiered from a 2025 chapter
DOI that was never obtained; the extracted text is Cowles DP 2331, 2022).
(5) Reproducibility is the corpus's weakest domain: code or data locators in
**8 of 53 assessable records (15%)**; D7 concern is raised by the rule in 48 of
53, recorded high in 46. (6) Applicability to the consumer's intraday-futures
setting is credible for exactly one of the 53 assessable records. (7) NB-02,
NB-08 and NB-13 are all adjudicated **episode-statistic-null** — NB-02 and
NB-08 on the full text of the version at issue, **NB-13 provisionally, on the
2006 working-paper twin, the 2009 journal version never having been obtained**.

**Limitations.** Screening was two context-independent sessions of one base
model, not two humans; κ therefore measures between-session variance under an
**unrecorded decoding configuration**, not inter-rater reliability — and the
model identity differs between this review's original declaration and the
provenance trailers on the commits that carry the verdict files, a conflict the
logs cannot resolve (L-15, VG-11). 280 records
(47.8% of those reaching full text) were excluded because full text could not be
obtained, which is a recall-side risk of unknown direction. 4 included records
were never read at full text. The dual re-extraction pass prescribed by protocol
§4.3 ran but its mismatch reconciliation did not; 90 of 357 comparable appraisal
cells diverged between passes and are resolved here by a declared conservative
rule rather than against the source, so **the ER-RoB v1 profile is
convention-resolved and may not be cited as an adjudicated appraisal**.
**The protocol's backward citation-chasing arm was never executed during the
search**, so pre-2011 antecedent coverage rests on the known-item list alone and
three of fourteen known items failed the recall check; the arm was run once
afterwards over a frozen corpus, through publisher-deposited reference lists and
only 22 of 27 carriers, and it named **one** record the corpus does not contain
(`er-bc-1`), which was not admitted. Its second named candidate, `er-bc-2`, was
a false positive: that work is in the universe as `eru-0209`/`eru-1027`, was
dual-screened at both stages and was excluded X7 / S-c-fail, so the arm's
absence test — DOI or exact normalised title — is looser than the "177
referenced DOIs absent from the universe" figure implies (§2.2, A12). **Records inside the frozen included set fail the
frozen eligibility criteria as written**: seven fail I3 (no DOI, arXiv ID or
Handle) and three same-work twins survive X7, so 72 records are 69 distinct
works; the corpus was not re-screened, and both are recorded as amendments A10(a)
and A10(b). Three further records that protocol §9.1 required to be
force-screened into the universe never entered it (A9).

## 1. Rationale and objectives (items 3, 4)

Rationale is carried in force from protocol §0 and is not restated beyond its
operative claim: the consumer agenda's Rev 3 refutation of its Definitional-basis
universal (d) rests on abstract-depth screening of two Phillips records, and
branch 3 intends to admit the recursive right-tailed family into its comparator
set. Citing a detector's critical values, delay behaviour or validity conditions
from an abstract is the failure this review exists to prevent.

Objectives are protocol §1 unchanged. Outcome domains, prioritised as in the
protocol (primary O1–O4; secondary O5, O6, with O6 extracted for every record):

| | outcome |
|---|---|
| O1 | empirical size under the stated null |
| O2 | power under stated DGPs, including periodically-collapsing alternatives |
| O3 | date-stamping accuracy and detection delay, origination and termination |
| O4 | false-alarm behaviour across the recursive test sequence (FWER, ARL₀) |
| O5 | validity conditions — assumptions under which the stated limit theory holds |
| O6 | causality status — real-time recursive versus full-sample retrospective |

The evaluation-criteria taxonomy for O4 is
[Frisén 2003](https://doi.org/10.1111/j.1751-5823.2003.tb00205.x), as the
protocol declares.

## 2. Methods (items 5–15)

### 2.1 Eligibility criteria (item 5) — frozen, unchanged

Criteria S-a/S-b/S-c (in-scope detector), I1–I4 (inclusion) and X1–X7 (exclusion)
are protocol §2 and were not reinterpreted at any stage. Every screening verdict
in the logs cites a criterion by identifier. No eligibility criterion was altered
by this document or by any amendment.

The LPPL exclusion (X3) held in execution: no retrieved LPPL-family record passed
S-a/S-b/S-c on its own text, so the protocol §2.5 contingency ("if the searches
surface an LPPL-family paper that *does* state a time-t assignment null … that
paper is in-scope by rule, and its existence is reported as a finding") did not
fire. The boundary was honoured in the other direction: two included records
evaluate an in-scope detector *against* LPPL comparators and enter under I2 —
Ardila, Sanadgol & Sornette 2018
([doi:10.3934/QFE.2018.4.904](https://doi.org/10.3934/QFE.2018.4.904),
`eru-0731`) and Bertelsen 2019 (SSRN twin
[doi:10.2139/ssrn.3392208](https://doi.org/10.2139/ssrn.3392208), `eru-0813`).

### 2.2 Information sources and search (items 6, 7)

Every query URL in protocol §3.2–3.4 was executed verbatim; the raw response,
platform, ISO 8601 execution date, HTTP status, total-hit count and
retrieved-record count were written at execution time into
[docs/literature/search_logs/explosive-regime/](search_logs/explosive-regime/),
one file per query id, each carrying the protocol query id in a
`protocol_query_id` field (amendment A1 renamed the file prefix `er-*` to `se-*`
and preserved the 1:1 mapping). Nothing was reconstructed afterwards.

| source | platform | arm | queries | date executed | records retrieved |
|---|---|---|---|---|---|
| Crossref | Crossref REST API | topical (incl. 2 SSRN-restricted) | 12 | 2026-08-24 | 240 |
| arXiv | arXiv API | topical | 6 | 2026-08-24 | 20 |
| OpenAlex | OpenAlex REST API | topical | 4 | 2026-08-24 | 89 |
| Semantic Scholar | S2 Graph API `/paper/search` | topical (each 429 twice, then 200 under A2) | 2 | 2026-08-24 | 40 |
| OpenAlex | OpenAlex REST API | forward citation, PWY seed | 1 (6 cursor pages) | 2026-08-24 | 1,148 |
| OpenAlex | OpenAlex REST API | forward citation, PSY seed | 1 (6 cursor pages) | 2026-08-24 | 1,081 |
| Semantic Scholar | S2 Graph API `/paper/citations` | forward citation, PWY seed | 1 (2 offset pages) | 2026-08-24 | 1,116 |
| Semantic Scholar | S2 Graph API `/paper/citations` | forward citation, PSY seed | 1 (2 offset pages) | 2026-08-24 | 1,150 |
| Crossref / OpenAlex | REST APIs | known item (KI-01…KI-14) | 14 | 2026-08-24 | 14 |
| **total** | | | **42 executed logs** | | **4,898** |

Retrieval caps (`rows=20`, `per-page=25`, `max_results=50`, `limit=50`) are
screening-budget caps on retrieval depth, not eligibility filters; total-hit
counts are preserved verbatim in each log (PRISMA-S item 9) and are large for the
Crossref topical arm (e.g. `se-crossref-10`: total 5,855,009, retrieved 20)
because `query.bibliographic` is a ranked-relevance endpoint with no boolean
restriction. The forward-citation arms carry the recall load and are uncapped.

No date, language or document-type filter was applied anywhere.

**Zero-yield and failed executions, reported per item 7.** `se-s2-01`,
`se-s2-01-b`, `se-s2-02` and `se-s2-02-b` returned HTTP 429 with zero records.
Amendment A2, logged before any screening decision, authorised a second verbatim
re-run under a `-c` suffix with retry-until-200 backoff; `se-s2-01-c` returned 19
records and `se-s2-02-c` returned 21. Query strings are byte-identical to
protocol §3.2; only the retry count deviates.

**SSRN supplementary arm: not run.** Protocol §3.1 permits an optional SSRN
site-search arm and requires that its absence be recorded rather than passed
over. It was not run. Recorded as a minor recall verification gap (§12.3, VG-5).

**Backward citation-chasing (`er-bc-*`): NOT run in the registered execution
window; executed 2026-09-02 as a post-freeze recall diagnostic.** Protocol §3.3
prescribes hand-checking the reference lists of included I2b comparison and
simulation studies for in-scope detectors not otherwise retrieved, each addition
logged with its carrier as `er-bc-{n}`. At the 2026-08-24/25 execution dates no
`se-bc-*` log existed and no included record carried a backward-chase
provenance: the arm did not run. That was a **MAJOR** protocol-vs-execution gap
— it is the one supplementary method that recovers detectors the seeds do not
cite, and its absence compounded the known-item recall failure on the antecedent
layer reported next (§2.3).

The arm has now been executed, after the corpus was frozen, and logged at
[docs/literature/search_logs/explosive-regime/se-bc-01.json](search_logs/explosive-regime/se-bc-01.json)
under amendment **A11**. What it is and what it is not:

- **Scope.** All 27 I2b-bearing included records (I2b 24, I2a\|I2b 2, I2b\|I2c 1).
- **Route deviation, declared.** §3.3's "hand-checked" implies the reference list
  of the source document. Reference lists were taken instead from
  publisher-deposited metadata: Crossref `reference` arrays (18 carriers) and,
  where Crossref carried none, OpenAlex `referenced_works` (4 carriers).
  Deposited lists are not guaranteed complete, so this is a weaker instrument
  than reading the PDFs.
- **Carrier coverage 22 of 27.** Five carriers yielded no deposited reference
  list at either platform: `eru-0813`, `eru-1289`, `eru-1770`, `eru-0268`,
  `eru-1310`.
- **Yield.** 392 unique referenced DOIs; 177 absent from the 1,996-record
  deduplicated universe by DOI or normalised title; hand-checked at title and,
  where a deposited abstract existed, at abstract depth against §2.1's
  S-a/S-b/S-c.
- **Result as corrected on re-check: ONE candidate addition, not two, plus 6
  named near-misses.** `er-bc-1` Hall, Psaradakis & Sola (1999), *Detecting
  periodically collapsing bubbles: a Markov-switching unit root test* (carriers
  `eru-0463`, `eru-0526`, `eru-1509`), which passes S-a/S-b/S-c on its deposited
  abstract and reports simulation evidence — i.e. a plausible I2b include on the
  pre-2011 antecedent layer the recall check flagged. **This is the diagnostic's
  entire yield of records the corpus does not contain.** Near-misses with
  reasons, including Chu, Stinchcombe & White (1996) and Banerjee, Lumsdaine &
  Stock (1992), are enumerated in the log.
- **`er-bc-2` was NOT a recall gap and the claim that it was is withdrawn.** The
  diagnostic reported `er-bc-2` Banerjee, Chevillon & Kratz (2013), *Detecting
  and Forecasting Large Deviations and Bubbles in a Near-Explosive Random
  Coefficient Model*, `10.2139/ssrn.2322360` (carrier `eru-0604`), as a second
  candidate "absent from the 1,996-record universe" with eligibility
  "indeterminate at retrievable depth". **That is false.** The same work is in
  the universe twice and was dual-screened at both stages:
  - `eru-0209`, *"Detecting and Forecasting Large Deviations and Bubbles **with**
    a Near-Explosive Random Coefficient Model"* (2013, no DOI, Semantic Scholar
    `paperId` `0b2057876edebb2a0bc64d9983e9491436579fc7`) — the working paper.
    Stage 1: PROMOTE / PROMOTE (`screen-verdicts-R1.jsonl`, `-R2.jsonl`).
    Stage 2: `EXCLUDE`, criterion **X7**, "working-paper twin of eru-1027"
    (R1); `X6` (R2); terminal under A3.
  - `eru-1027`, *Probabilistic forecasting of bubbles and flash crashes*,
    Banerjee/Chevillon/Kratz, *Econometrics Journal* 2020,
    [doi:10.1093/ectj/utaa004](https://doi.org/10.1093/ectj/utaa004) — the
    published version, with a full deposited abstract of the same NERC model.
    Stage 1: PROMOTE / PROMOTE. Stage 2: `EXCLUDE`, criterion **S-c-fail**,
    "NERC predictive-probability model (ESSEC WP twin); no null-referenced
    time-t decision" (R1); `X6` (R2); terminal under A3.
  So the work was screened and excluded on a substantive criterion, not missed.
  It is removed from the candidate list and from every downstream statement.
  *(Finding LITERATURE-2-1; protocol amendment **A12**.)*
- **Why the dedup key missed it, and what that bounds.** The chase matched
  referenced DOIs against the universe by DOI **or** exact normalised title.
  `er-bc-2`'s DOI `10.2139/ssrn.2322360` is genuinely absent from the store, and
  the two normalised titles differ by one word — "**in** a Near-Explosive…"
  versus "**with** a Near-Explosive…" — so neither key fired. The consequence is
  general: **"177 referenced DOIs absent from the 1,996-record universe" means
  absent *by those two keys*, not absent as works.** One of the two records the
  diagnostic escalated from that pool turned out to be in the corpus already, so
  the 177 is an upper bound on genuine absence, of unquantified looseness. The
  same weakness applies to the 6 near-misses, which were adjudicated at title and
  abstract depth against the same universe.
- **The remaining candidate is not admitted, and the corpus stays at 72.** The
  included set is frozen by commit `8aeebfe`; admitting a record after freeze
  would require re-running dual screening over a changed universe, which this
  pass does not do. It is also a **single-agent** hand-check with no second
  screener and no blind adjudication, so it is a recall diagnostic, not a
  screening stage.

**Net effect on the review's own claims.** The gap changes character but does
not close. Before: a prescribed arm never ran, and the size of what it would
have recovered was unbounded. Now: the arm has run once, through a weaker
retrieval route, over 22 of 27 carriers, and has named **one** specific record
the frozen corpus does not contain and that looks eligible — `er-bc-1`. Every
coverage statement in §6.1 and §7 — in particular the O4 synthesis claim in
§7.4, the §7.2 O2 claim and the §7.7 pooling outcome — is bounded by that, by
the 5 uncovered carriers, by the deposited-reference-list route, and now also by
the demonstrated looseness of the arm's own absence test (the `er-bc-2`
correction above). Carried as §12.1 L-5 and §12.3 VG-4, both restated.
*(Findings SCOPE-1-4, LITERATURE-2-1.)*

### 2.3 Known-item recall check (PRESS surrogate, protocol §3.5)

Protocol §3.5 makes the known-item list the PRESS recall instrument: a KI record
not independently retrieved by at least one topical or forward-citation arm is a
per-item recall failure to be reported. Three of fourteen failed
(`se-ki-recall-check.json`):

| KI | record | independently retrieved by | verdict |
|---|---|---|---|
| KI-05 | Phillips & Magdalinos 2007, [doi:10.1016/j.jeconom.2005.08.002](https://doi.org/10.1016/j.jeconom.2005.08.002) (`eru-0092`) | none | **recall failure** |
| KI-13 | Busetti & Taylor 2004, [doi:10.1016/j.jeconom.2003.10.028](https://doi.org/10.1016/j.jeconom.2003.10.028) (`eru-0069`) | none | **recall failure** |
| KI-14 | Evans 1991, *AER* 81(4), no DOI (`eru-0059`) | none | **recall failure** |
| KI-01…KI-04, KI-06…KI-12 | — | 2–6 arms each | pass |

All three failures are antecedents that predate both seeds and therefore cannot
appear in a forward-citation arm; the topical queries did not reach them within
their declared caps. The finding bounds what the strategy can be trusted to
recall: pre-2011 methodological antecedents are recalled by the known-item arm or
not at all. All three entered the record universe via the known-item arm and were
screened like any other record; all three were excluded (§3.4).

### 2.4 Deduplication (protocol §4.1)

Two-stage, logged in `se-dedup-ledger.json`:

- **R1 identifier-level** union-find over normalised DOI, version-stripped arXiv
  id, OpenAlex work id and Semantic Scholar paperId: 4,898 → 2,255 (2,643 merge
  events).
- **R2 title-level** exact normalised-title match (NFKD, lowercased,
  non-alphanumerics removed) on residual clusters: 245 candidate groups, all 245
  applied, all hand-verified before application; composition is working-paper
  twins, publisher double-registrations and cross-arm re-retrievals without shared
  identifiers. No fuzzy-similarity threshold was used — the protocol rule is exact
  match, and a similarity cutoff would have been an unlabelled constant.
  2,255 → 1,996.

Total duplicates removed: **2,902**. Near-identical titles failing the exact rule
(e.g. "Double Asymptotics for an Explosive Continuous Time Model" vs "Double
asymptotics for explosive continuous time models") were deliberately not merged
and left to the review-stage hand-verified twin ledger. That deferral was not
fully discharged: three same-work twins survive inside the frozen included set
(§5.3).

### 2.5 Selection process (item 8)

Exactly protocol §4.2, with amendment A3. Two independent sessions (R1, R2) of one
base model each received the identical deduplicated universe, protocol §2
verbatim, and the frozen screening prompt (`er-screening-prompt.txt`); no shared
state. Stage 1 title/abstract, verdicts `INCLUDE` / `PROMOTE` / `EXCLUDE` with a
criterion identifier, `PROMOTE` counting as advance. Stage 2 full text, both
screeners, `INCLUDE` / `EXCLUDE` / `X6`. Disagreements to a third session blind to
verdict provenance.

**Amendment A3**, logged pre-adjudication, fixed the access-asymmetry case the
protocol did not anticipate: where exactly one screener reached full-text depth,
that screener's substantive verdict stands and the record is flagged
`single-screener-fulltext`; X6-vs-X6 remains X6; INCLUDE-vs-EXCLUDE goes to blind
adjudication; EXCLUDE-vs-EXCLUDE code mismatches are terminal agreement with the
code conflict logged. A3 weakened dual assessment for 153 records and is declared
in the conformance map (§12.4) and the limitations (§12.1, L-3).

**Honest compliance statement, as executed — PRISMA item 8's automation-tool
declaration, made here on the same record as the rest of the document.**
Screener A, screener B and the adjudicator are context-independent sessions of
the *same* base model. **That model is declared `claude-fable-5`**, which is the
`AI-Assistance` trailer on commit `8aeebfe`, the commit that carries every
stage-1 and stage-2 verdict file and both blind adjudications. It is **not**
`claude-opus-5`, which is what this review asserted here as settled fact when
first delivered; the review's own original declaration conflicts with the
repository's provenance record and the ReproLog carries no model field, so the
conflict cannot be adjudicated from the logs and the trailer — the only
clone-durable carrier — is what is declared. Per-stage table, the two readings
consistent with the evidence, and the consequence for κ: §12.1 **L-15** and
§12.3 **VG-11**. *(Findings QUANT-1-3, REV-2-1, LITERATURE-2-5.)*

**The model's decoding configuration is not recorded anywhere, and this
qualifies every reading of κ below.** No temperature, top-p, max-tokens,
thinking-budget or session seed is recorded in `er-screening-prompt.txt`, in any
verdict JSONL, or in either ReproLog. Under PRISMA 2020 item 8 the model is the
declared automation tool and the sole effective screener class, and no human
screener exists at any stage. κ therefore measures **between-session variance
under an unrecorded decoding configuration** — it is not inter-rater reliability
between cognitively independent raters, it is not presented as evidence of
screener independence, and the stronger reading "κ measures the model's decoding
variance" is **not** falsifiable from this record, because the screening stage
cannot be re-run to a comparable κ without the sampling settings. Recorded as
part of verification gap **VG-11**. *(Finding REPRODUCIBILITY-2-3.)*

### 2.6 Data collection and data items (items 9, 10)

Extraction fields E1–E16 are protocol §5, unchanged. Protocol §4.3 prescribes one
primary extractor over all fields plus a context-independent second agent
re-extracting the numeric fields E9–E13 and answering Q1–Q7 with no sight of the
first extraction. Both passes ran (`se-extraction-primary.jsonl`, 72 record rows
plus one adjudication row; `se-extraction-recheck.jsonl`, 65 rows of which 63
substantive). The reconciliation step did not run; see §2.8 and §12.1 (L-2).

### 2.7 Appraisal instrument (item 11)

**ER-RoB v1**, the project-local `CONVENTION` instrument declared in protocol §6:
eight domains, nine closed signalling questions, domain-level concern judgments,
**no composite score**. It is adapted in form from the signalling-question design
of QUADAS-2
([Whiting et al. 2011](https://doi.org/10.7326/0003-4819-155-8-201110180-00009))
and PROBAST ([Wolff et al. 2019](https://doi.org/10.7326/M18-1376)); it inherits
their form and **not** their validation. It is unvalidated, and every table
reporting it says so. No other instrument was substituted; no domain or question
was added, dropped or reworded.

**The response scale WAS altered, and the earlier form of this sentence did not
except it.** Protocol §6 declares a three-level scale — questions "answered
yes / no / unclear per included study". Execution used a **four-level** scale by
adding `partial`, in **50 of the 561 answered Q-cells (8.9%)** (Q1 2, Q2 3,
Q3 1, Q4 8, Q5 2, Q6 1, Q7 1, Q8 3, Q9 29).

> **Denominator correction.** The earlier form of this figure gave 585, i.e.
> 65 records × 9 questions. That contradicts this review's own assessable-
> denominator rule: Q8 and Q9 are `n/a` for the 12 recheck-only records, and
> §6.1 fixes the Q8/Q9 denominator at 53, so 24 of those 585 cells were never
> answered. The count of answered, non-`n/a`, non-twin Q-cells is
> **65 × 7 (Q1–Q7) + 53 × 2 (Q8, Q9) = 455 + 106 = 561**. Exclusion classes, by
> name: 4 records with no full text at any stage, 3 same-work twins appraised
> under their carriers, and the 12 recheck-only records on Q8/Q9 only. The 50-cell
> numerator and its per-question split are unchanged and reconcile cell for cell
> with the `partial` column of §6.1. The wrong figure is embedded in protocol
> amendment **A7**, which is inside an append-only addendum and is therefore
> corrected by a new amendment **A12** rather than edited.
> *(Findings QUANT-2-1, REV-2-12.)* The frozen concern rule raises a domain on `no`
or `unclear` and says nothing about `partial`, so until now every domain
judgment resting on a `partial` cell rested on an undeclared convention. The
extension is recorded as amendment **A7**, which also fixes and labels the
CONVENTION that `partial` counts as not-`yes` for the rule-derived domain column
reported in §6. The domains and the nine questions themselves are unchanged;
the response scale is not. The addition was made during appraisal entry, before
any amendment was requested, so A7 is post-hoc and says so.
*(Finding QUANT-1-1.)*

| domain | signalling question |
|---|---|
| D1 null & critical values | Q1 null stated with its drift/deterministic specification, and critical-value provenance explicit? |
| D2 size | Q2 empirical size under the stated null DGP at stated levels and sample sizes? |
| D3 power & DGP realism | Q3 power under explicitly parameterised explosive alternatives? Q4 alternatives include a collapse mechanism? |
| D4 date-stamping | Q5 origination/termination accuracy or delay distributions reported? |
| D5 causality status | Q6 evaluated in real-time form, with any full-sample variant kept distinct? |
| D6 multiplicity | Q7 multiplicity of the recursive sequence addressed? |
| D7 reproducibility | Q8 code and/or data available to regenerate the reported characteristics? |
| D8 applicability | Q9 evaluated setting close enough to intraday futures for credible transfer, or frequency/volatility sensitivity reported? |

### 2.8 Resolution rule for the unreconciled dual-extraction pass — DECLARED DEVIATION

Protocol §4.3 requires that primary/recheck mismatches be "resolved against the
source text and the mismatch count reported". Comparing the two passes on the 51
records where both answered Q1–Q7 gives **90 divergent cells out of 357**
(25.2%), distributed Q1 6, Q2 7, Q3 3, Q4 23, Q5 14, Q6 12, Q7 25. No
reconciliation record exists in the search-log directory and the mismatch count
had never been reported. Re-opening 51 full texts to adjudicate 90 cells was not
undertaken in this pass.

The deviation is therefore declared, not silently absorbed, and a rule is fixed
and applied uniformly:

> **CONVENTION (this document, §2.8).** Where the two extraction passes give
> different answers to the same signalling question, the appraisal table records
> the more conservative answer under the order `no` > `unclear` > `partial` >
> `yes`, marked `†`. Where that resolution raises the concern implied for a
> domain above the concern the primary extractor recorded, the domain cell is
> raised to match and marked `†`. Divergence is never resolved toward lower
> concern.

The rule is chosen to be direction-safe, not to be right: it cannot understate
concern, and it is not a substitute for the source-text adjudication the protocol
requires. **Recorded as protocol amendment A6**, appended to the protocol
addendum by this document (§12.5). The consequence is stated wherever the
appraisal is used: the ER-RoB v1 profile is convention-resolved, not
source-adjudicated, and may not be cited as an adjudicated appraisal (§6
header, L-2).

The divergence is not random. 25 of the 90 cells are Q7 (multiplicity), where the
primary pass read "asymptotic control only, no finite-sample family-wise
accounting" as `no`/`unclear` while the recheck read the same extracted facts as
satisfying the question's third disjunct ("an explicit accounting of
per-observation vs per-episode error rates") and answered `yes`. A further 23 are
Q4 (collapse mechanism), where the passes differ on whether a sharp
re-initialisation collapse counts as "a collapse mechanism … rather than pure
explosion only". Both are wording ambiguities in ER-RoB v1 itself, recorded as
instrument defects for any successor version (§12.2).

### 2.9 Synthesis methods (item 13)

Narrative synthesis structured by outcome domain (O1…O6), each with an evidence
table over the included studies, closed by a per-detector summary. The
meta-analysis condition was pre-specified in protocol §7 (15c): pooling only if
≥2 studies from non-overlapping author teams report the same characteristic for
the same detector under the same DGP family with matched sample size and
minimum-window rule.

**That condition is met nowhere in the corpus.** §7.7 documents its failure
characteristic by characteristic. Consequently there is no pooled estimate, no
forest plot, and — the failure mode the protocol names explicitly — **no vote
counting presented as inference**. Counts of studies reporting a property appear
below as descriptions of the *literature's coverage*, never as evidence about a
detector's properties.

### 2.10 Effect measures (item 12) — inapplicable with rationale

Outcomes are native operating characteristics (rejection frequencies, date bias
in sample fractions, delay in observations, FWER, AUROC). There is no common
effect estimate across studies and no transformation was applied. Declared
inapplicable with rationale, per protocol §9.4.

## 3. PRISMA 2020 flow accounting (items 16a, 16b)

### 3.1 Flow

```
IDENTIFICATION
  Records retrieved, all arms (42 executed query logs)             4,898
    topical Crossref 240 | topical arXiv 20 | topical OpenAlex 89
    topical Semantic Scholar 40 | forward-citation OpenAlex 2,229
    forward-citation Semantic Scholar 2,266 | known-item 14
  Duplicates removed                                               2,902
    identifier-level merge events            2,643  (4,898 -> 2,255)
    title-level merges applied                 245  (2,255 -> 1,996)
  Records screened (deduplicated universe)                         1,996

SCREENING (stage 1, title/abstract, both screeners)
  Excluded at title/abstract                                       1,410
    both screeners exclude                     1,377
    adjudicated to exclude                        33
  Advanced to full text                                              586
    both screeners advance                       233
    adjudicated to advance                       353  (352 PROMOTE + 1 INCLUDE)

ELIGIBILITY (stage 2, full text, both screeners under A3)
  Records assessed at full text                                      586
  Excluded, substantive criteria                                     234
  Excluded, full text unobtainable (X6, both screeners)              280

INCLUDED
  Records included in the review                                      72
    both screeners include                        41
    A3 single-screener full text                  21
    blind adjudication -> include                 10
  Distinct works (3 same-work twins collapse)                         69

NOT IN ANY OF THE ABOVE, and prescribed to be
  Protocol 9.1 force-screen targets never entered into the universe     3
    NB-02 doi:10.21314/jor.2002.058
    NB-08 doi:10.1017/jpr.2017.20
    NB-13 doi:10.1016/j.jfs.2008.08.001
```

**Three protocol-mandated records are missing from this flow (finding
SCOPE-1-1).** Protocol §9.1's final paragraph requires NB-02, NB-08 and NB-13 to
be "force-screened into the record universe regardless of query recall". They
were not. None of the three DOIs appears in `screen-verdicts-R1.jsonl`,
`screen-verdicts-R2.jsonl`, `screen-verdicts-ADJ.jsonl` or the 1,996-record
candidate store; they appear only in `se-nb-adjudications.json` and
`protocol-doicheck.json`. **The identification count 4,898 and the deduplicated
universe 1,996 therefore exclude all three**, and no screening verdict citing a
criterion identifier exists for any of them. They were adjudicated directly as
out-of-corpus targets in §9, where all three fail S-a, S-b and S-c on full text,
so no substantive verdict changes — but the screening audit trail §9.1 requires
does not exist and cannot be manufactured after the fact. Recorded as protocol
amendment **A9** and verification gap **VG-9**; the corpus is frozen and is not
re-screened.

### 3.2 Reconciliation against the logs — RECONCILES EXACTLY

Every stage number was recomputed from the primitive verdict files rather than
copied from the summary file, and each identity below was checked:

| identity | check | result |
|---|---|---|
| universe | `se-dedup-ledger.json.counts.final_universe` = rows in `screen-verdicts-R1.jsonl` = rows in `screen-verdicts-R2.jsonl` = entries in `references_explosive-regime-dating.json` | 1,996 = 1,996 = 1,996 = 1,996 ✓ |
| identification | Σ `arm_counts` over 42 logs = `raw_records_all_arms` | 4,898 = 4,898 ✓ |
| dedup | 4,898 − 2,643 = 2,255; 2,255 − 245 = 1,996 | ✓ |
| κ 2×2 marginals | R1 advance 233 + 296 = 529 = `INCLUDE` 77 + `PROMOTE` 452; R2 advance 233 + 90 = 323 = 93 + 230; R1 exclude 1,377 + 90 = 1,467; R2 exclude 1,377 + 296 = 1,673 | ✓ |
| κ table total | 233 + 296 + 90 + 1,377 | 1,996 ✓ |
| adjudication volume | binarised disagreements 296 + 90 = 386 = rows in `screen-verdicts-ADJ.jsonl` | 386 = 386 ✓ |
| stage-1 advance | 233 both-advance + 353 adjudicated-advance = `se-stage1-advance-set.json` size | 586 = 586 ✓ |
| stage-1 exclude | 1,377 both-exclude + 33 adjudicated-exclude | 1,410 ✓; 1,410 + 586 = 1,996 ✓ |
| stage-2 assessed | rows in `screen2-verdicts-R1.jsonl` = rows in `screen2-verdicts-R2.jsonl` = Σ of the seven `se-stage2-crosstable.json` cells (41 + 21 + 132 + 16 + 20 + 76 + 280) | 586 = 586 = 586 ✓ |
| stage-2 substantive exclusions | 76 both-exclude-same + 20 code-mismatch + 132 exclude-vs-X6 + 6 adjudicated-exclude | 234 ✓ |
| stage-2 adjudication | 16 INCLUDE-vs-EXCLUDE = rows in `screen2-verdicts-ADJ.jsonl` = 10 include + 6 exclude | ✓ |
| included | 41 + 21 + 10 | 72 ✓; 234 + 280 + 72 = 586 ✓ |
| I2 mix | I2a 43 + I2b 24 + I2b\|I2c 1 + I2a\|I2b 2 + I2c 2 | 72 ✓ |
| extraction coverage | record rows in `se-extraction-primary.jsonl` (excluding the `ADJUDICATION-i` row) = included set, no extras, no omissions | 72 ✓ |

**Verdict: the flow reconciles exactly with the logs at every stage, with one
stated exception.** No number was adjusted to make a stage balance. The
exception is not an arithmetic one: the universe the identities reconcile
against is the universe *as executed*, which is three records short of the
universe protocol §9.1 prescribes, because the three force-screen targets never
entered it (§3.1, A9, VG-9). Every identity below holds over the executed
universe; none of them would detect a record that was never identified. The one number in the summary file that is
not independently derivable — the split of the 386 adjudicated records into 353
advance and 33 exclude — was recomputed from the adjudicator's own verdicts
(`PROMOTE` 352, `INCLUDE` 1, `EXCLUDE` 33) and matches.

### 3.3 Screening agreement (item 8)

From `se-kappa-computation.json`, recomputed here from the primitive verdict
files and confirmed:

| | screener B advance | screener B exclude | total |
|---|---|---|---|
| **screener A advance** | 233 | 296 | 529 |
| **screener A exclude** | 90 | 1,377 | 1,467 |
| **total** | 323 | 1,673 | 1,996 |

p₀ = 1,610 / 1,996 = **0.806613**;
pₑ = (529·323 + 1,467·1,673)/1,996² = **0.658923**;
κ = (p₀ − pₑ)/(1 − pₑ) = **0.433012**
([Cohen 1960](https://doi.org/10.1177/001316446002000104)). Raw verdict
differences before binarisation: 408; binarised disagreements: 386.

No target κ was set in the protocol, deliberately (any cutoff would have been an
unlabelled constant), and none is imposed now. κ is reported with the raw
agreement and the full 2×2 table because κ alone is not interpretable across
prevalence: here the advance prevalence is 26.5% for A and 16.2% for B, and the
asymmetry (296 A-advance/B-exclude versus 90 the other way) shows the two sessions
differ mainly in threshold, not in ordering. Every one of the 386 disagreements
went to blind adjudication regardless of κ.

**What κ does and does not license.** It is not evidence of screener
independence (§2.5). It is evidence that the two sessions of the same model,
given identical inputs, disagreed on 19.3% of records — which is the honest
measure of how much the stage-1 boundary depends on **between-session variance
of the screening stage**, and is the main reason the 234 substantive full-text
exclusions are enumerated in full in §13 rather than summarised. It is **not**
decomposable into decoding stochasticity versus context-ordering effects,
because the sessions' decoding configuration (temperature, top-p, max-tokens,
thinking budget, seed) is recorded nowhere and the stage cannot be re-run to a
comparable κ (§2.5, VG-11). *(Finding REPRODUCIBILITY-2-3.)*

### 3.4 Excluded at title/abstract, with reasons (item 16a)

Reason codes are the criteria cited by the screeners themselves. Because the two
screeners assign codes independently and A3 does not apply at stage 1, the
distribution is given per screener over the 1,377 records both excluded, plus the
adjudicator's codes over the 33 records adjudicated to exclude.

| criterion | screener A, both-exclude (n=1,377) | screener B, both-exclude (n=1,377) | adjudicator, adjudicated-exclude (n=33) |
|---|---|---|---|
| I1 — no in-scope detector concerned | 773 | 767 | 19 |
| X1 — plain empirical application, no OC with a stated null | 381 | 427 | 6 |
| X4 — changepoint detector without an explosivity alternative | 87 | 10 | 5 |
| S-a fail — alternative is not explosive/mildly explosive | 61 | 94 | — |
| X5 — rational-bubble theory with no test procedure | 33 | 40 | — |
| X3 — LPPL / log-periodic family | 18 | 20 | — |
| X2 — full-sample existence test, no time-indexed output | 9 | 9 | 1 |
| S-b fail — no time-indexed output | 6 | 8 | — |
| S-c fail — no stated null with a reference distribution | 6 | 1 | — |
| I2 fail — no operating characteristic and no theory | 3 | 1 | 2 |

The two screeners agree closely on the two dominant reasons (I1 ≈ 770, X1
381 vs 427) and diverge on the X4-versus-S-a boundary (87/61 versus 10/94) — the
same code, different label, for changepoint detectors without an explosive
alternative. That divergence is a code-taxonomy overlap in the protocol, not a
disagreement about the records, and it does not affect any advance/exclude
decision.

The three known-item recall failures were all excluded here or at stage 2:

| record | stage | verdict | deciding criterion |
|---|---|---|---|
| `eru-0059` Evans 1991 (KI-14) | stage 1, adjudicated | EXCLUDE | X2 — "simulation critique of full-sample existence tests (Diba–Grossman battery); no time-indexed output (S-b)" |
| `eru-0092` Phillips & Magdalinos 2007 (KI-05) | stage 2, both screeners | EXCLUDE | S-b fail — "estimation limit theory only; no time-indexed detector output" |
| `eru-0069` Busetti & Taylor 2004 (KI-13) | stage 2, both screeners | EXCLUDE | S-a fail — "alternatives are I(0)/I(1) persistence changes, never explosive root" |

This is the intended behaviour of the frozen criteria, and it is worth stating
plainly because the protocol anticipated these three as corpus members: Evans
1991 supplies the periodically-collapsing DGP against which power must be read
but is not itself an in-scope detector; Phillips & Magdalinos 2007 supplies the
mildly-explosive limit theory but states no test; Busetti & Taylor 2004's
alternative is a persistence change, not an explosive root. All three are
therefore cited in this review as *antecedents inside included studies* (they are
the DGP and the limit theory those studies use) and not as included evidence.

### 3.5 Excluded at full text, with reasons (item 16b)

**234 records excluded on substantive criteria**, every one enumerated with its
record id, title, identifier, criterion and the screener's stated reason, in §13.
Summary distribution of the deciding code:

| criterion | n | reading |
|---|---|---|
| X1 | 109 | plain empirical application; detector applied, episodes reported, no operating characteristic with a stated null |
| X7 | 31 | same-work duplicate surviving the automatic dedup, caught at full text |
| S-b fail | 25 | no time-indexed output |
| I1 | 20 | full text shows no in-scope detector |
| S-c fail | 8 | no stated null with a reference distribution |
| X2 | 5 | full-sample existence test only |
| I2 | 5 | neither theory nor reported operating characteristic |
| S-a fail | 4 | alternative not explosive |
| X4 | 4 | changepoint detector, no explosivity alternative |
| X5 | 2 | rational-bubble theory, no test |
| I3 | 1 | no persistent identifier and no retrievable locator |
| code conflict (both exclude, codes differ) | 20 | terminal agreement under A3; both codes recorded in §13 |

X1 at 109 of 234 confirms the protocol's stated expectation that plain
applications "are the bulk of this literature".

**280 records excluded because full text could not be obtained (X6).** Both
screeners exhausted their retrieval chains independently on every one of these.
This is 47.8% of the 586 records that reached full text and is the single largest
threat to the corpus's completeness; it is treated as a major limitation, not a
footnote (§12.1, L-4). The X6 records are *not* individually enumerated in §13:
X6 is an access outcome, not an eligibility judgment, and the protocol's own
framing (§2.3 X6, A3) treats them as a distinct class. Their record ids are
recoverable in full from `se-stage2-crosstable.json` key `both_x6`.

### 3.6 The 153 records where only one screener reached full text (amendment A3)

Under A3, 21 became includes and 132 became excludes. The direction of the
asymmetry is worth recording: of the 153 asymmetric pairs, screener A held the
full text in 113 and screener B in 40. A3 therefore converts, for 153 records,
"dual full-text assessment" into "one full-text assessment plus one failed
retrieval". The 21 A3 includes are individually flagged in the corpus table
(§5.1) and four of them were never subsequently read at full text by the
extraction stage either (§5.4).

## 4. The included corpus at a glance

**Two columns, because the record set and the work set are not the same set.**
The frozen included set is **72 records but 69 distinct works** (§5.3, amendment
A10(b)). Every record-level distribution below therefore counts `eru-0154`,
`eru-0904` and `eru-0622` a second time, under codes inherited from their
carriers `eru-0126`, `eru-1526` and `eru-0675`. The distinct-work column removes
them. Neither column is "the" answer: the frozen set is a record set, so record
counts are what the corpus contains, while a coverage or prevalence statement
about the *literature's works* must use the right-hand column. Where a synthesis
claim in §7 quantifies over works it now names the distinct-work denominator
explicitly. *(Finding REV-2-3.)*

| dimension | distribution over 72 records | over 69 distinct works |
|---|---|---|
| evidence tier (charter hierarchy, recorded per record, **as corrected**) | peer-reviewed journal article 53; working paper 13 (incl. 1 SSRN carrier of a peer-reviewed article, and `eru-1289`, re-tiered from "peer-reviewed book chapter" — the 2025 CUP chapter carrying its DOI was never obtained and the extracted text is Cowles DP 2331 (2022); finding LITERATURE-1-2, L-10, VG-6); preprint 4; other (student research paper, bachelor thesis) 2 | peer-reviewed 53; working paper **10**; preprint 4; other 2 — all three twins are working-paper tier |
| study type (I2) | I2a theory 43; I2b simulation 24; I2a+I2b 2; I2c application-with-OC 2; I2b+I2c 1 | I2a **41**; I2b **23**; I2a+I2b 2; I2c 2; I2b+I2c 1 |
| screening path | dual include 41; A3 single-screener 21; blind adjudication 10 | not restated — screening path is a property of the record, not of the work |
| causality status (O6) | RT real-time evaluated 22; FS full-sample only 22; CS causal statistic, ex-post evaluation 19; SPLIT (per-statistic attribution required) 3; not stated in text 2; not extracted (no full text) 4 | RT 22; FS **21**; CS **17**; SPLIT 3; NS 2; NE 4 — the twins are CS (`eru-0154`), CS (`eru-0904`) and FS (`eru-0622`) |
| authorship lineage | PSY/Phillips lineage 21; Harvey–Leybourne–Taylor–Astill lineage 16; other/third-party 35 | PSY/Phillips **19**; HLTA 16; other **34** — `eru-0154` and `eru-0904` are both PSY-lineage twins, `eru-0622` is other-lineage |
| extraction depth | full text with dual numeric pass 51; full text at recheck only, single pass 12; full text, single pass 2; twin extracted under its carrier 3; **no full text at any stage 4** | dual numeric pass 51; recheck only 12; single pass 2; **no full text 4** — the twin class disappears by construction |
| code or data locator (E14) | public locator 8; explicitly none 44; partial 1; not extracted 19 | public locator 8; explicitly none 44; partial 1; not extracted **16** — the 3 twins are inside the record-level "not extracted 19" |

**Evidence-tier note, per the charter rule that tier travels with the claim.**
Four records are preprint tier and two are below working-paper tier. Every claim
in §7 that rests on one of them is flagged inline and may not be treated as
settled downstream. The tier-blind *admission* with tier-labelled *use* policy is
protocol §2.4 and was justified there by the observed lag between working-paper
circulation and journal publication in this literature; the corpus bears that
out — PSY circulated as working papers from 2012–2013 before *IER* 2015, and five
of the corpus's 2025–2026 records are accepted-but-not-yet-paginated.

### 4.1 O6 coding scheme used in the tables

The protocol requires the causality status of each reported characteristic. Three
codes are used, assigned from the extracted E8 field and, where the extraction
records a per-statistic split, reported as SPLIT rather than forced:

| code | meaning |
|---|---|
| **RT** | the detector is real-time in construction (statistic at *t* uses data through *t*; thresholds fixed ex ante of *t*) **and** the reported characteristics are measured in that form (training/monitoring split, stopping time, or first-crossing rule evaluated sequentially) |
| **CS** | causal statistic, retrospective evaluation: the statistic is computable at *t*, but the reported characteristics come from full-sample or pseudo-real-time evaluation, or the critical values condition on the whole sample |
| **FS** | full-sample / retrospective statistic; no time-*t* claim attaches to the reported characteristic |
| **SPLIT** | the record's own text attributes real-time status to one statistic and ex-post status to another; the attribution is stated per statistic in §8 |
| **NS** | causality status not stated in the extracted text |
| **NE** | not extracted — no full text obtained at any stage |

The distinction CS-versus-RT is the one the consumer agenda's standing causal-time
hazard turns on. A record coded CS has *not* published a real-time operating
characteristic even though its statistic could carry one; treating a CS record's
numbers as real-time performance is exactly the smoothed-probability defect the
agenda catalogues.

## 5. Study characteristics (item 17)

One row per included record, in the frozen included-set order (dual includes, then
A3 single-screener includes, then blind adjudications). Citations are the
extraction stage's E1 field. `O6` is the code from §4.1.

| # | rec | citation | tier | I2 | screening path | detector(s) evaluated | O6 | code/data | extraction depth |
|---|---|---|---|---|---|---|---|---|---|
| 1 | eru-0131 | Phillips PCB, Wu Y, Yu J (2011). Explosive Behavior in the 1990s Nasdaq: When Did Exuberance Escalate Asset Values? International Economic Review 52(1):201-226. doi:10.1111... | peer-reviewed | I2a | dual | forward recursive right-tailed ADF sequence (ADF_r) + sup_r ADF_r (SADF); rolling-window ADF... | SPLIT | none stated (no code or data archive; data from Datastrea... | full text, dual numeric pass |
| 2 | eru-0150 | Homm U, Breitung J (2012). Testing for Speculative Bubbles in Stock Markets: A Comparison of Alternative Methods. Journal of Financial Econometrics 10(1):198-231. doi:10.10... | peer-reviewed | I2b | dual | comparison study: PWY SADF, Bhargava statistic, Busetti-Taylor, Kim, Chow-type DF break test... | FS | — | full text at recheck only, single pass |
| 3 | eru-0238 | Phillips PCB, Shi S, Yu J (2014). Specification Sensitivity in Right-Tailed Unit Root Testing for Explosive Behaviour. Oxford Bulletin of Economics and Statistics 76(3):315... | peer-reviewed | I2a | dual | SADF under alternative null/regression specifications: deterministic drift, localized (local... | FS | no code archive stated | full text, dual numeric pass |
| 4 | eru-0259 | Franses PH (2016). A simple test for a bubble based on growth and acceleration. Computational Statistics & Data Analysis 100:160-169. doi:10.1016/j.csda.2014.06.006 | peer-reviewed | I2b | dual | growth-acceleration balance test on recursive residuals (journal descendant of the EI 2013-1... | RT | — | full text at recheck only, single pass |
| 5 | eru-0348 | Sollis R (2016). Fixed and Recursive Right-Tailed Dickey-Fuller Tests in the Presence of a Break under the Null. Journal of Time Series Econometrics 8(1):1-19. doi:10.1515/... | peer-reviewed | I2b | dual | size analysis of fixed right-tailed DF and recursive SDF (SADF-type, r0 = 0.10) tests when a... | FS | no code archive | full text, dual numeric pass |
| 6 | eru-0393 | Phillips PCB, Shi S, Yu J (2015). Testing for Multiple Bubbles: Historical Episodes of Exuberance and Collapse in the S&P 500. International Economic Review 56(4):1043-1078... | peer-reviewed | I2a | dual | GSADF (double-recursive sup ADF, ex-post test) + BSADF date-stamping sequence (ex-ante); com... | SPLIT | Gauss and Matlab code publicly available (sites.google.co... | full text, dual numeric pass |
| 7 | eru-0395 | Phillips PCB, Shi S, Yu J (2015). Testing for Multiple Bubbles: Limit Theory of Real-Time Detectors. International Economic Review 56(4):1079-1134. doi:10.1111/iere.12131 | peer-reviewed | I2a | dual | PWY DF_r detector, PSY BSDF_r(r0) detector, sequential PWY detector; CUSUM (Homm-Breitung) a... | RT | Gauss/Matlab code public (sites.google.com/site/shupingsh... | full text, dual numeric pass |
| 8 | eru-0463 | Harvey DI, Leybourne SJ, Sollis R (2017). Improving the accuracy of asset price bubble start and end date estimators. Journal of Empirical Finance 40:121-138. doi:10.1016/j... | peer-reviewed | I2b | dual | model-based minimum-sum-of-squared-residuals (break-point) estimators with BIC model selecti... | FS | — | full text at recheck only, single pass |
| 9 | eru-0503 | Harvey DI, Leybourne SJ, Sollis R, Taylor AMR (2016). Tests for explosive financial bubbles in the presence of non-stationary volatility. Journal of Empirical Finance 38(B)... | peer-reviewed | I2a | dual | PWY SADF under non-stationary volatility; two wild-bootstrap implementations (first-differen... | FS | no code archive stated; commodity price data application ... | full text, dual numeric pass |
| 10 | eru-0559 | Phillips PCB, Shi S (2018). Financial Bubble Implosion and Reverse Regression. Econometric Theory 34(4):705-753. doi:10.1017/S0266466617000202 (Crossref issued 2017) | peer-reviewed | I2a | dual | BSDF (PSY) under a four-regime model (normal / mildly explosive / mildly integrated collapse... | SPLIT | no code archive stated in WP text (PSY code ecosystem app... | full text, dual numeric pass |
| 11 | eru-0597 | Kholodilin KA, Michelsen C, Ulbricht D (2018). Speculative price bubbles in urban housing markets. Empirical Economics 55(4):1957-1983. doi:10.1007/s00181-017-1347-x | peer-reviewed | I2b\|I2c | dual | Chow-type unit-root break statistic (DFC, Homm-Breitung 2012 variant) for explosive roots; n... | FS | R code by authors 'available upon request' (fn.3, WP p.10... | full text, dual numeric pass |
| 12 | eru-0604 | Landgraf N (2016/2017). Testing for Multiple Bubbles in Asset Prices. MaRBLe Research Papers (Maastricht University). doi:10.26481/marble.2016.v1.257 | other | I2b | dual | generalized sup DFC (GsupDFC): Chow-type DF statistic with double-sup window variation (GSAD... | FS | no code archive | full text, dual numeric pass |
| 13 | eru-0607 | Pavlidis EG, Paya I, Peel DA (2017). Testing for Speculative Bubbles Using Spot and Forward Prices. International Economic Review 58(4):1191-1226. doi:10.1111/iere.12249 | peer-reviewed | I2b | dual | GSADF/BSADF (PSY 2015a) applied to spot-forward differentials s_{t+n} - f_{t,n} and f_{t,n} ... | CS | no code archive stated; data: DM-USD and GBP-USD spot/for... | full text, dual numeric pass |
| 14 | eru-0609 | Astill S, Harvey DI, Leybourne SJ, Taylor AMR (2017). Tests for an end-of-sample bubble in financial time series. Econometric Reviews 36(6-9):651-666. doi:10.1080/07474938.... | peer-reviewed | I2a\|I2b | dual | end-of-sample bubble tests on finite m-observation windows: S_m (Andrews-type sum statistic)... | RT | no code archive stated | full text, dual numeric pass |
| 15 | eru-0689 | Whitehouse EJ (2019). Explosive Asset Price Bubble Detection with Unknown Bubble Length and Initial Condition. Oxford Bulletin of Economics and Statistics 81(1):20-41. doi:... | peer-reviewed | I2a | dual | GLS-demeaned variants of forward-recursive right-tailed DF tests; limiting distributions for... | FS | — | full text at recheck only, single pass |
| 16 | eru-0735 | Astill S, Harvey DI, Leybourne SJ, Sollis R, Taylor AMR (2018). Real-Time Monitoring for Explosive Financial Bubbles. Journal of Time Series Analysis 39(6):863-891. doi:10.... | peer-reviewed | I2a | dual | MAX_m and SEQ_m real-time bubble monitors built from subsample statistics S_{e,m} (Astill-Ha... | RT | no code archive stated | full text, dual numeric pass |
| 17 | eru-0748 | Harvey DI, Leybourne SJ, Zu Y (2019). Testing explosive bubbles with time-varying volatility. Econometric Reviews 38(10):1131-1151. doi:10.1080/07474938.2018.1536099 | peer-reviewed | I2a | dual | supBZ: WLS-based (volatility-weighted) variant of the PWY supDF test; union-of-rejections U ... | FS | no code archive stated; empirical application with bootst... | full text, dual numeric pass |
| 18 | eru-0883 | Tao Y, Phillips PCB, Yu J (2019). Random coefficient continuous systems: Testing for extreme sample path behavior. Journal of Econometrics 209(2):208-237. doi:10.1016/j.jec... | peer-reviewed | I2a | dual | continuous-time random coefficient (random persistence) system estimated with realized volat... | RT | — | full text at recheck only, single pass |
| 19 | eru-0889 | Horvath L, Liu Z, Rice G, Wang S (2020). Sequential monitoring for changes from stationarity to mild non-stationarity. Journal of Econometrics 215(1):209-238. doi:10.1016/j... | peer-reviewed | I2a | dual | sequential CUSUM/KPSS-type detector V_M(k) with weighted boundary functions g_M(k) for onlin... | RT | no code archive stated | full text, dual numeric pass |
| 20 | eru-0891 | Harvey DI, Leybourne SJ, Zu Y (2020). Sign-Based Unit Root Tests for Explosive Financial Bubbles in the Presence of Deterministically Time-Varying Volatility. Econometric T... | peer-reviewed | I2a | dual | sign-based variant of the PSY test (sPSY) - pivotal under deterministically time-varying vol... | FS | — | full text at recheck only, single pass |
| 21 | eru-0924 | Laurent S, Shi S (2019/2022). Unit Root Test with High-Frequency Data. SSRN 3421332 (doi:10.2139/ssrn.3421332); published as 'Unit Root Testing with High-Frequency Data', E... | working-paper carrier | I2a | dual | real-time monitoring device for deviations from random-walk dynamics using intraday high-fre... | CS | — | full text at recheck only, single pass |
| 22 | eru-1031 | Phillips PCB, Shi S (2020). Real time monitoring of asset markets: Bubbles and crises. In: Handbook of Statistics 42 (Financial, Macro and Micro Econometrics Using R), 61-8... | peer-reviewed | I2a | dual | PSY BSADF monitoring for bubbles AND crises (random-drift-martingale crash regime); composit... | CS | R package psymonitor (public, CRAN/GitHub) with full call... | full text, dual numeric pass |
| 23 | eru-1038 | Horvath L, Liu Z, Lu S (2020). Sequential Monitoring of Changes in Housing Prices. SSRN doi:10.2139/ssrn.3529058 / arXiv:2002.04101 (published as Horvath, Liu, Lu, Economet... | preprint | I2a | dual | sequential change-point monitor for a linear + autoregressive housing-price model: weighted ... | RT | no code archive stated | full text, dual numeric pass |
| 24 | eru-1044 | Monschang V, Wilfling B (2021). Sup-ADF-style bubble-detection methods under test. Empirical Economics 61:145-172. doi:10.1007/s00181-020-01859-7 | peer-reviewed | I2b | dual | third-party evaluation of six sup-ADF-style tests: SADF, GSADF, sign-based SADF/GSADF (HLZ),... | CS | no code archive stated | full text, dual numeric pass |
| 25 | eru-1049 | Pedersen TQ, Schutte ECM (2020). Testing for explosive bubbles in the presence of autocorrelated innovations. Journal of Empirical Finance 58:207-225. doi:10.1016/j.jempfin... | peer-reviewed | I2b | dual | SADF/GSADF and BSADF date-stamping under autocorrelated (ARMA) innovations; proposed sieve-b... | CS | no code archive stated; data: OECD price-rent ratios (pub... | full text, dual numeric pass |
| 26 | eru-1112 | Chen Y, Phillips PCB, Shi S (2022). Common Bubble Detection in Large Dimensional Financial Systems. Journal of Financial Econometrics 20(5):989-1063. doi:10.1093/jjfinec/nb... | peer-reviewed | I2a | dual | PSY-factor procedure: PSY recursive test applied to estimated common factor(s) of a large pa... | CS | no code archive stated in WP | full text, dual numeric pass |
| 27 | eru-1117 | Astill S, Harvey DI, Leybourne SJ, Taylor AMR, Zu Y (2021). CUSUM-Based Monitoring for Explosive Episodes in Financial Data in the Presence of Time-Varying Volatility. Jour... | peer-reviewed | I2a | dual | CUSUM_V: Homm-Breitung CUSUM monitor generalized to time-varying volatility via nonparametri... | RT | simulations in Gauss 9.0; no code archive stated | full text, dual numeric pass |
| 28 | eru-1384 | Kurozumi E, Skrobotov A, Tsarev A (2022). Time-Transformed Test for Bubbles under Non-stationary Volatility. Journal of Financial Econometrics 21(4):1282-1314. doi:10.1093/... | peer-reviewed | I2a | dual | time-transformed SADF (SADF_tt): applies SADF to a variance-clock time-transformed series so... | FS | R code public: sites.google.com/site/antonskrobotov/ (fn.... | full text, dual numeric pass |
| 29 | eru-1394 | Astill S, Taylor AMR, Kellard N, Korkos I (2023). Using covariates to improve the efficacy of univariate bubble detection methods. Journal of Empirical Finance 70:342-366. ... | peer-reviewed | I2a | dual | covariate-augmented sub-sample CADF versions of PSY (sup CADF / BSCADF) with sieve/wild boot... | CS | no code archive stated | full text, dual numeric pass |
| 30 | eru-1519 | Whitehouse EJ, Harvey DI, Leybourne SJ (2023). Real-Time Monitoring of Bubbles and Crashes. Oxford Bulletin of Economics and Statistics 85(3):482-513. doi:10.1111/obes.12540 | peer-reviewed | I2a\|I2b | dual | S_MIN(m, n): real-time crash-detection monitor applied after AMAX(k)-style bubble detection;... | RT | no code archive stated (author site hosts data for relate... | full text, dual numeric pass |
| 31 | eru-1526 | Lui YL, Phillips PCB, Yu J (2024). Robust testing for explosive behavior with strongly dependent errors. Journal of Econometrics 238(2):105626. doi:10.1016/j.jeconom.2023.1... | peer-reviewed | I2a | dual | DF-bar_n,HAR: heteroskedasticity-and-autocorrelation-robust right-tailed DF test valid under... | CS | no code archive stated | full text, dual numeric pass |
| 32 | eru-1604 | Pavlidis EG (2025). Bubbles and crashes: A tale of quantiles. Journal of Time Series Analysis 46(5):884-907. doi:10.1111/jtsa.12794 | peer-reviewed | I2b | dual | quantile unit root tests for bubbles: t_n(tau) at upper quantiles (U_n(tau)) and QKS sup-sta... | FS | no code archive stated | full text, dual numeric pass |
| 33 | eru-1716 | Boswijk HP, Yu J, Zu Y (2024). Testing for an Explosive Bubble using High-Frequency Volatility. arXiv:2405.02087 (working paper) | preprint | I2a | dual | RVPWY: PWY-type supremum test on low-frequency (daily) price increments standardized by intr... | RT | no code archive stated | full text, dual numeric pass |
| 34 | eru-1813 | Vriz GL, Grossi L (2025). Green bubbles: A four-stage paradigm for detection and propagation. Energy Economics 149:109095. doi:10.1016/j.eneco.2025.109095 | peer-reviewed | I2b | dual | four-stage bubble paradigm: BSADF/GSADF for exuberance detection + Kolmogorov-Smirnov change... | CS | no code archive stated; RENIXX and covariate data from co... | full text, dual numeric pass |
| 35 | eru-1844 | Whitehouse EJ, Harvey DI, Leybourne SJ (2025). Real-time monitoring procedures for early detection of bubbles. International Journal of Forecasting 41(3):1260-1277. doi:10.... | peer-reviewed | I2a | dual | A_MAX^AR(k) and A_MAX^TR(k): modified AMAX subsample monitors with alternative variance stan... | RT | dataset link published: sites.google.com/site/ejwhitehous... | full text, dual numeric pass |
| 36 | eru-1845 | Horvath L, Trapani L (2025). Real-Time Monitoring with RCA Models. Econometric Theory (forthcoming/online). doi:10.1017/S0266466625000052 | peer-reviewed | I2a | dual | weighted CUSUM, standardized CUSUM (Darling-Erdos), and Page-CUSUM online detectors on WLS r... | RT | no code archive stated; applications: UK Covid-19 hospita... | full text, dual numeric pass |
| 37 | eru-1852 | Breitung J, Diegel M (2025). Sequential Detector Statistics for Speculative Bubbles. Journal of Time Series Analysis 46(5):828-847. doi:10.1111/jtsa.12845 | peer-reviewed | I2a | dual | heteroskedasticity-robust LBI (locally best invariant) statistic and CUSUM/mCUSUM/wCUSUM seq... | RT | working-paper version referenced for extensions; no code ... | full text, dual numeric pass |
| 38 | eru-1920 | Kurozumi E, Skrobotov A (2026). Confidence sets for the emergence, collapse, and recovery dates of a bubble. Econometric Reviews (forthcoming). doi:10.1080/07474938.2026.27... | peer-reviewed | I2a | dual | confidence sets for bubble break dates (T_e emergence, T_c collapse, T_r recovery) by invert... | FS | no code archive stated (Skrobotov's site hosts code for r... | full text, dual numeric pass |
| 39 | eru-1921 | Astill S, Taylor AMR, Zu Y (2026). Covariate-Augmented CUSUM Bubble Monitoring Procedures. Econometric Theory, 1-30. doi:10.1017/S0266466626100383 | peer-reviewed | I2a | dual | CUSUM_WMV: covariate-augmented, volatility-robust (WLS) CUSUM real-time bubble monitor; comp... | RT | Supplementary Material (Cambridge); no code archive state... | full text, dual numeric pass |
| 40 | eru-1929 | Sarkar A, Wells MT (2026). Double Local-to-Unity: Inference under Nearly Nonstationary Volatility. SSRN/arXiv working paper. doi:10.2139/ssrn.6865190 (arXiv:2512.06823) | preprint/working-paper | I2a | dual | moderate-deviation limit theory for AR models with jointly persistent mean and volatility dy... | FS | GitHub referenced for simulation details ('see GitHub', p... | full text, dual numeric pass |
| 41 | eru-1950 | Sarkar A, Wells MT (2026). Is there an AI bubble? Robust date-stamping for periods of exuberance. Frontiers of Mathematical Finance. doi:10.3934/fmf.2026005 | peer-reviewed | I2a | dual | SV-ADF: stochastic-volatility-robust recursive ADF date-stamping under double local-to-unity... | CS | replication code on GitHub (Section 6, p.25); AI-assistan... | full text, dual numeric pass |
| 42 | eru-0100 | Phillips PCB, Yu J (2009). Limit Theory for Dating the Origination and Collapse of Mildly Explosive Periods in Time Series Data. SMU Working Paper (unpublished; SMU InK soe... | working-paper | I2a | A3 single-screener | limit theory for the PWY date estimators r_e-hat, r_f-hat (origination and collapse of mildl... | RT | — | full text at recheck only, single pass |
| 43 | eru-0112 | Shi S, Anderson H, Vahid F (2010). Testing for Periodically Collapsing Bubbles: A Generalized sup ADF Test. Working paper (ANU/Monash; S2 CorpusId 16858475; no persistent i... | working-paper | I2a | A3 single-screener | generalized sup ADF test for periodically collapsing bubbles - an early precursor formulatio... | NE | — | NO FULL TEXT |
| 44 | eru-0154 | Phillips PCB, Yu J (2011). The Timeline of Financial Bubbles During the Subprime Crisis (working-paper twin of Quantitative Economics 2(3):455-491, doi:10.3982/QE82) | working-paper | I2a | A3 single-screener | — | CS | — | twin (extracted under eru-0126) |
| 45 | eru-0268 | Mihailovic D (2014). Detecting speculative bubbles in GARCH processes: A time-series based test for predicting explosive behavior. Unpublished manuscript/thesis (S2 CorpusI... | other | I2b | A3 single-screener | time-series test for explosive behavior in GARCH processes (per title; content unverified) | RT | — | full text at recheck only, single pass |
| 46 | eru-0427 | Shi S (2016). Speculative Bubbles or Market Fundamentals? An Investigation of US Regional Housing Markets. CAMA Working Paper 46/2016, ANU. (Published descendant: Economic ... | working-paper | I2a | A3 single-screener | PSY procedure applied to an estimated bubble component after removing fundamentals (interest... | CS | no code archive stated | full text, dual numeric pass |
| 47 | eru-0513 | Virtanen T, Tolo E, Viren M, Taipalus K (2017/2018). Use of unit root methods in early warning of financial crises. ESRB Working Paper No. 45 / Journal of Financial Stabili... | working-paper | I2c | A3 single-screener | RADF (rolling ADF, fixed window) and SADF unit-root bubble signals as crisis early-warning i... | RT | no code archive; data partly proprietary (BIS/ECB series) | full text, dual numeric pass |
| 48 | eru-0526 | Fulop A, Yu J (2017). Bayesian Analysis of Bubbles in Asset Prices. Econometrics 5(4):47. doi:10.3390/econometrics5040047 | peer-reviewed | I2b | A3 single-screener | two-regime switching model (mean-reverting around stochastic trend vs explosive bubble regim... | RT | no code archive stated | full text, dual numeric pass |
| 49 | eru-0622 | Pavlidis, Martinez-Garcia, Grossman (2017). Detecting Periods of Exuberance... Dallas Fed Globalization Institute WP 325. doi:10.24149/gwp325 | working-paper | I2b | A3 single-screener | — | FS | — | twin (extracted under eru-0675) |
| 50 | eru-0675 | Pavlidis EG, Martinez-Garcia E, Grossman V (2018). Detecting periods of exuberance: A look at the role of aggregation with an application to house prices. Economic Modellin... | peer-reviewed | I2b | A3 single-screener | SADF, GSADF (evaluated); panel GSADF (Pavlidis et al. 2016) as benchmark comparator | FS | data public (S&P Dow Jones, BLS, Dallas Fed International... | full text, dual numeric pass |
| 51 | eru-0691 | Kruse R, Wegener C (2018). Explosive behaviour and long memory with an application to European bond yield spreads. Scottish Journal of Political Economy 65(2):139-162. doi:... | peer-reviewed | I2b | A3 single-screener | PWY-type right-tailed DF t-test against explosiveness, with long-memory-adjusted critical va... | FS | no code archive stated | full text, dual numeric pass |
| 52 | eru-0749 | Hafner CM (2020). Testing for Bubbles in Cryptocurrencies with Time-Varying Volatility. Journal of Financial Econometrics 18(2):233-249. doi:10.1093/jjfinec/nby023 | peer-reviewed | I2b | A3 single-screener | PSY-type bubble tests under time-varying volatility with deterministic long-run + stochastic... | NE | — | NO FULL TEXT |
| 53 | eru-0823 | Phillips PCB, Shi S (2019). Detecting Financial Collapse and Ballooning Sovereign Risk. Oxford Bulletin of Economics and Statistics 81(6):1336-1361. doi:10.1111/obes.12307 | peer-reviewed | I2a | A3 single-screener | PSY BSDF procedure applied to crisis (collapse) detection under a new L-process (local-level... | CS | psymonitor R package ecosystem (companion); no archive st... | full text, dual numeric pass |
| 54 | eru-0904 | Lui YL (with Phillips PCB, Yu J) (2019). Testing for Rational Bubbles under Strongly Dependent Errors. Working paper (SMU/S2 CorpusId 221208907); earlier title of the work ... | working-paper | I2a | A3 single-screener | — | CS | — | twin (extracted under eru-1526) |
| 55 | eru-0959 | Harvey DI, Leybourne SJ, Whitehouse EJ (2020). Date-stamping multiple bubble regimes. Journal of Empirical Finance 58:226-246. doi:10.1016/j.jempfin.2020.06.004 | peer-reviewed | I2a | A3 single-screener | two-step dating: (1) recursive unit root tests identify a date window containing an explosiv... | FS | — | full text at recheck only, single pass |
| 56 | eru-1155 | Harsha S, Ismail B (2018). Improved Test for Detecting Explosive Bubbles. Journal of Data Science 16(3):495-508. doi:10.6339/JDS.201707_15(3).0007 | peer-reviewed | I2b | A3 single-screener | Max-variant tests: Max conventional ADF, Max recursive SADF, Max rolling SADF (max of statis... | FS | no code archive | full text, dual numeric pass |
| 57 | eru-1260 | Wang X, Yu J (2023). Bubble testing under polynomial trends. The Econometrics Journal 26(1):25-44. doi:10.1093/ectj/utac020 | peer-reviewed | I2a | A3 single-screener | right-tailed unit root tests in an AR(2) regression robust to polynomial trends; critique: s... | FS | — | full text at recheck only, single pass |
| 58 | eru-1310 | Ibragimov R, Parlour CA, Walden J (with He S, Prokhorov A, Skrobotov A per S2 author merge) (2022). Fundamental Value Pricing and Bubbles for Nontraditional Assets: The Cas... | working-paper | I2b | A3 single-screener | fundamental-value pricing framework for cryptocurrencies with bubble testing component (per ... | NE | — | NO FULL TEXT |
| 59 | eru-1405 | Liu Y, Phillips PCB, Yu J (2023). A Panel Clustering Approach to Analyzing Bubble Behavior. International Economic Review 64(4):1347-1395. doi:10.1111/iere.12647 | peer-reviewed | I2a | A3 single-screener | post-clustering panel approach: recursive k-means clustering of mixed-root panel autoregress... | NS | no code archive stated | full text, dual numeric pass |
| 60 | eru-1580 | Harvey DI, Leybourne SJ, Taylor AMR, Zu Y (2024). A new heteroskedasticity-robust test for explosive bubbles. Journal of Time Series Analysis 46(1):102-132. doi:10.1111/jts... | peer-reviewed | I2a | A3 single-screener | PSY-tilde: modified PSY/GSADF tests on volatility-purged data y_t / sigma_t-hat (Beare 2018 ... | FS | supplementary material with Tables S1-S2; no code archive... | full text, dual numeric pass |
| 61 | eru-1715 | Kurozumi E, Nishi M (2025). Testing for a bubble with a stochastically varying explosive coefficient. Journal of Time Series Analysis 46(1):133-160. doi:10.1111/jtsa.12768 | peer-reviewed | I2a | A3 single-screener | recursive stochastic unit root tests SSU/GSSU (Lee-Nagakura-type STUR statistics in SADF/GSA... | NS | no code archive stated (GAUSS) | full text, single pass |
| 62 | eru-1890 | Harvey DI, Leybourne SJ, Tatlow BS, Zu Y (2025). Unit Root Tests for Explosive Financial Bubbles in the Presence of Deterministic Level Shifts. Oxford Bulletin of Economics... | peer-reviewed | I2a | A3 single-screener | sign-based PSY variants under deterministic level shifts; new tests robust to level shifts (... | NE | — | NO FULL TEXT |
| 63 | eru-0126 | Phillips PCB, Yu J (2011). Dating the timeline of financial bubbles during the subprime crisis. Quantitative Economics 2(3):455-491. doi:10.3982/QE82 | peer-reviewed | I2a | adjudicated | modified PWY recursive DF procedures: coefficient-based DF_r and t-statistic DF_r^t detector... | CS | no code archive stated | full text, dual numeric pass |
| 64 | eru-0198 | Franses PH (2013). Are we in a bubble? A simple time-series-based diagnostic. Econometric Institute Report 2013-12, Erasmus School of Economics. (hdl.handle.net/1765/39598) | working-paper | I2b | adjudicated | growth-acceleration balance diagnostic: under no-bubble ARMA dynamics the (1-L^2)-type trans... | RT | no code archive | full text, single pass |
| 65 | eru-0731 | Ardila D, Sanadgol D, Sornette D (2018). Out-of-sample forecasting of housing bubble tipping points. Quantitative Finance and Economics 2(4):904-930. doi:10.3934/QFE.2018.4... | peer-reviewed | I2c | adjudicated | supDF (PWY forward recursive DF), supBT (Busetti-Taylor), supKBT (Kim/Busetti-Taylor Chow-ty... | RT | no code archive stated; data from OECD/BIS/Dallas Fed pub... | full text, dual numeric pass |
| 66 | eru-0813 | Bertelsen KP (2019). Comparing Tests for Identification of Bubbles. CREATES Research Paper 2019-16, Aarhus University. (I3 via SSRN twin doi:10.2139/ssrn.3392208) | working-paper | I2b | adjudicated | head-to-head comparison: LPPL and generalized LPPL (GLPPL, novel: non-zero required rate of ... | FS | no code archive | full text, dual numeric pass |
| 67 | eru-0855 | Zhang H-G, Wu L (2019). High-Dimensional Multiple Bubbles Prediction Based on Sparse Constraints. IEEE Access 7:32586-32596. doi:10.1109/ACCESS.2019.2893929 | peer-reviewed | I2a | adjudicated | WSADF: data-driven self-adaptive evolutionary bubble prediction algorithm extending the SADF... | CS | — | full text at recheck only, single pass |
| 68 | eru-1289 | Shi S, Phillips PCB (2022). Econometric Analysis of Asset Price Bubbles. **Cowles Foundation DP 2331 (2022) — the extracted version.** The DOI doi:10.1017/9781108910095.003 resolves to the chapter in *Financial Econometrics: Theory and Applications*, CUP, **2025**, pp.30-59, which was NOT obtained (LITERATURE-1-2) | **working-paper** (tier corrected; the DOI's peer-reviewed chapter was not read) | I2b | adjudicated | PSY real-time explosive-root strategy reviewed, plus PSY(multiple): a multiple-testing imple... | CS | no code archive stated in DP (psymonitor ecosystem applies) | full text, dual numeric pass |
| 69 | eru-1509 | Morita R, Psaradakis Z, Sola M, Yunis P (2023). On testing for bubbles during hyperinflations. Studies in Nonlinear Dynamics and Econometrics 28(2). doi:10.1515/snde-2022-0014 | peer-reviewed | I2b | adjudicated | Markov regime-switching AR with three INDEPENDENT Markov chains (intercept/growth, AR-root, ... | CS | no code archive stated | full text, dual numeric pass |
| 70 | eru-1761 | Blasques F, Koopman SJ, Mingoli G, Telg S (2025). A Novel Test for the Presence of Local Explosive Dynamics. Journal of Time Series Analysis (2025). doi:10.1111/jtsa.70001 | peer-reviewed | I2b | adjudicated | MAR (mixed causal-noncausal autoregressive) based test: assesses at time t whether the curre... | RT | no code archive stated | full text, dual numeric pass |
| 71 | eru-1770 | Giancaterini F, Hecq A, Jasiak J, Manafi Neyazi A (2026). Bubble Detection with Application to Green Bubbles: A Noncausal Approach. arXiv:2505.14911v2 (working paper) | preprint | I2b | adjudicated | spectral-tail-process bubble diagnostic in MAR (mixed causal-noncausal) models: tests at tim... | CS | no code archive stated | full text, dual numeric pass |
| 72 | eru-1889 | Magdalinos T, Petrova K (2025). Uniform Inference with General Autoregressive Processes. Federal Reserve Bank of New York Staff Reports, no. 1151. doi:10.59576/sr.1151 | working-paper | I2a | adjudicated | IV-based t-statistic with data-driven combination of near-stationary and mildly explosive in... | RT | no code archive stated in the extracted text; data: Bloom... | full text, dual numeric pass |

### 5.1 Persistent identifiers and FAIR F1 status (criterion I3)

Every DOI carried by an included record was verified against the DOI Handle
System on 2026-09-02: **62 of 62 returned `responseCode` 1**. Two further records
carry arXiv identifiers verified against the arXiv API on the same date
(`eru-1716` → arXiv:2405.02087v1; `eru-1770` → arXiv:2505.14911v2). One carries a
Handle verified against the Handle System (`eru-0198` → hdl 1765/39598,
`responseCode` 1). Three DOIs absent from the candidate store were resolved at
full-text extraction and are carried into the included-corpus store with a
provenance note: `eru-0622` → [doi:10.24149/gwp325](https://doi.org/10.24149/gwp325),
`eru-0813` → [doi:10.2139/ssrn.3392208](https://doi.org/10.2139/ssrn.3392208),
`eru-1289` → [doi:10.1017/9781108910095.003](https://doi.org/10.1017/9781108910095.003).

**Seven included records have no DOI, no arXiv ID and no Handle** — `eru-0100`,
`eru-0112`, `eru-0154`, `eru-0268`, `eru-0427`, `eru-0904`, `eru-1310`. The
count is seven, not the five this review first reported, and the review's own
identifier tally proves it: 62 DOIs + 2 arXiv IDs + 1 Handle = 65 records with a
protocol-accepted persistent identifier, out of 72, leaving **seven** without
one. The two records omitted from the first count are the twins `eru-0154` and
`eru-0904`. *(Finding REV-1-2.)*

**A twin does not inherit its carrier's DOI for I3 purposes.** `eru-0154`'s
carrier `eru-0126` and `eru-0904`'s carrier `eru-1526` both hold DOIs, but I3 is
a property of the *record*, and each twin is a distinct row in the frozen
included set with its own entry in the store, its own contribution to every
record-level count, and its own FAIR F1 obligation. The carrier's identifier
resolves the carrier, not the twin: nothing about `10.3982/QE82` locates the
working-paper text that `eru-0154` is. §5.3 already states that `eru-0154` has
"no independent identifier"; that is exactly an I3 failure and it is now counted
as one. Both store entries carry an explicit `I3 GAP` note as of this pass, as
the other five already did.

Criterion I3 as written requires one of the three identifier types, and says a
record failing I3 "is excluded and logged with its best locator (FAIR F1 gap),
not silently dropped". All seven were nonetheless included by the screeners.
**The corpus is frozen at 72 and this review does not re-screen it**; the
discrepancy between the frozen criterion and the frozen included set is recorded
as a finding and as a numbered protocol amendment (A10(a)), not repaired
(§12.1, L-6; §12.3, VG-8). All seven entered through the A3 single-screener
path, where the screener that reached full text asserted a "repository" route
and the other screener recorded "no retrievable locator on any queried
platform". Their best available locator is the Semantic Scholar `paperId`
carried in the `custom` block of each store entry.

### 5.2 Included-corpus bibliography

`docs/literature/references_explosive-regime.json` — 72 CSL-JSON entries, a
strict subset of the candidate store with (i) the three extraction-resolved DOIs
added under a provenance note, (ii) the included-set path and I2 type carried in
`custom`, and (iii) I3-gap and twin notes. No metadata was written from memory;
every added field traces to a log file or to a live identifier check dated
2026-09-02.

**Updated 2026-09-02 by the round-1 audit remediation**, in four ways, none of
which changes the corpus's composition: `eru-0154` and `eru-0904` gained the
`I3 GAP` note the other five I3-failing records already carried (REV-1-2);
`eru-1289` gained a version-and-tier correction note (LITERATURE-1-2); the 13
records with a Crossref volume/issue/page discrepancy and the 3 with a
pagination update each gained a note recording the discrepancy and pointing at
L-13 (LITERATURE-1-4); and `eru-0749` gained a note recording that its Crossref
record carries no pagination, so its citation could not be checked. No `DOI`,
`title`, `author`, `issued` or `custom` field was altered.

**Updated again 2026-09-02 by the round-2 audit remediation**, in one way, also
notes-only: `eru-0198` and `eru-0259` each gained a note recording that they are
a **probable, unadjudicated same-work twin pair** whose adjudication the
extraction logs asked for and never received, and that the distinct-work count is
69 if they are two works and 68 if they are one (§5.4, VG-13, amendment A13(b)).
A successor reading only the store would otherwise never learn of that gap. No
other entry and no other field changed. *(Finding SCOPE-2-3.)*

SHA-256: `13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521`
(after the round-1 remediation: `8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124`; as first
delivered: `1abbb9d8b253ff2d10c5f021205101ab4bd610812ffd75d8f6bdcde024bbb7dc`).

Protocol §4.1 reserves this filename for the post-screening included corpus and
amendment A1 recorded that the pre-screening candidate universe would be
delivered as `references_explosive-regime-dating.json` instead. The included-corpus
store did not exist before this document; it is created here, which discharges
§4.1 late rather than not at all.

### 5.3 Three same-work twins inside the frozen included set

The dedup ledger's R2 rule is exact normalised-title match, and it deliberately
left near-identical titles to a review-stage hand-verified twin ledger (§2.4).
Three pairs survived into the frozen included set and were identified at
extraction:

| twin | carrier | relation as documented at extraction |
|---|---|---|
| `eru-0622` Dallas Fed Globalization Institute WP 325 | `eru-0675` Pavlidis, Martínez-García & Grossman 2018, *Economic Modelling* [doi:10.1016/j.econmod.2018.07.021](https://doi.org/10.1016/j.econmod.2018.07.021) | working-paper twin; extraction performed once on the WP text, which is the version the journal article derives from |
| `eru-0154` "The Timeline of Financial Bubbles During the Subprime Crisis" | `eru-0126` Phillips & Yu 2011, *Quantitative Economics* [doi:10.3982/QE82](https://doi.org/10.3982/QE82) | working-paper form of the QE article (Cowles DP 1770 lineage); no independent identifier |
| `eru-0904` "Testing for Rational Bubbles under Strongly Dependent Errors" | `eru-1526` Lui, Phillips & Yu 2024, *J. Econometrics* [doi:10.1016/j.jeconom.2023.105626](https://doi.org/10.1016/j.jeconom.2023.105626) | earlier-titled working paper of the same work (author line, subject and LPY lineage documented at extraction) |

Consequence stated plainly: **the corpus contains 72 records but 69 distinct
works** — 69 being the count under the three twin pairs *adjudicated at
extraction* above. **A fourth pair, `eru-0198` / `eru-0259`, meets the same
documentary standard those three were declared on — same sole author, same
subject, documented working-paper-to-journal chain, one text read — but was never
given twin treatment, so both its records carry independent appraisal rows and
both count in every assessable denominator. Under the uniform standard the figure
is 68.** The review reports 69 because renumbering to 68 would re-derive the 65
assessable denominator and every "of 65" fraction inside a corpus it is forbidden
to re-screen; that refusal is **operational, not evidential**, and is stated as
such at §5.4, VG-13 and amendment **A14(a)** rather than presented as an evidence
gap. **The standard governing a twin declaration in this review is documentary
and single-text**, not "both full texts compared" — §5.4 states it in full, since
no earlier version of this document did, which is how one pair came to be judged
by a stricter rule than the other three. *(Finding LITERATURE-3-2.)* Every count
in this review is reported over records because the frozen set is a record set;
wherever a count over works would differ materially it is now given both ways
(§4, §7.6, §10.2).

**The no-double-counting assurance, narrowed to what is actually true.** Each
twin is extracted once, under its carrier, so **no operating characteristic in
the §7 evidence tables is double-counted**: those tables cite the carrier record
and its table or equation, never the twin. That is the whole of the assurance.
It does **not** extend to the record-level *distributions*: `eru-0154` (O6 CS,
PSY lineage), `eru-0904` (O6 CS, PSY lineage) and `eru-0622` (O6 FS,
other lineage) each carry codes inherited from their carriers, so every
distribution counted over 72 records counts those three works twice. The earlier
form of this sentence, of L-7 and of amendment A10(b) said flatly that no
operating characteristic is double-counted, which a reader could and did take as
covering the §4, §7.6 and §10.2 tables; it does not. Distinct-work counts are
now given beside the record counts at each of those three sites, and the O6
coverage fraction in §7.6 is stated over distinct works. *(Finding REV-2-3;
A10(b) is inside the protocol's append-only addendum and is corrected there by
amendment **A13**, not edited.)*

Under criterion X7 these three should have been deduplicated. They were not, and
the corpus is frozen; recorded as a finding (§12.1, L-7) and as a numbered
protocol amendment (A10(b)), not repaired.

**The twins also fail I3, and the carriers' DOIs do not cover them.** `eru-0154`
and `eru-0904` carry no DOI, arXiv ID or Handle of their own. Their carriers do,
but I3 is a property of the record and each twin is a separate row in the frozen
set; the carrier's identifier resolves the carrier's text, not the twin's. Both
are therefore counted among the **seven** I3 failures in §5.1, not the five this
review first reported, and both store entries now carry an `I3 GAP` note.
`eru-0622`, the third twin, does carry its own DOI
([doi:10.24149/gwp325](https://doi.org/10.24149/gwp325)) and passes I3.
*(Finding REV-1-2.)*

### 5.4 Records with no full text at any stage — four

These four are included in the corpus but were never read. Nothing in §6 or §7
attributes any content to them, and each is named at every point where its absence
matters:

| record | citation | what could not be extracted | what is known, and from where |
|---|---|---|---|
| `eru-0112` | Shi, Anderson & Vahid (2010). *Testing for Periodically Collapsing Bubbles: A Generalized sup ADF Test*. Working paper (ANU/Monash; Semantic Scholar CorpusId 16858475) | everything: E1–E16, all nine ER-RoB questions. No identifier resolved; no working locator recoverable | that a "generalized sup ADF" formulation for periodically collapsing bubbles circulated under this author line in 2010, i.e. before the PSY "Testing for Multiple Bubbles" papers — a lineage datum recorded from the Semantic Scholar metadata record only, and **not** a content claim. Not a twin of `eru-0393`/`eru-0395` (different author set and title) |
| `eru-0749` | Hafner (2020). *Testing for Bubbles in Cryptocurrencies with Time-Varying Volatility*. *J. Financial Econometrics* 18(2):233–249, [doi:10.1093/jjfinec/nby023](https://doi.org/10.1093/jjfinec/nby023) | all numeric operating characteristics; the paper's own statement of its bootstrap size adjustment | its headline result is attested *inside another included full text* — `eru-1384` (Kurozumi, Skrobotov & Tsarev 2022) cites Hafner's modification of the HLST algorithm. That attribution belongs to `eru-1384`, not to `eru-0749`, and is used only in that form |
| `eru-1310` | Ibragimov, Parlour & Walden et al. (2022). *Fundamental Value Pricing and Bubbles for Nontraditional Assets*. Unpublished working paper | everything. Identification itself is fragile: title-only, no DOI, ambiguous author merge in the Semantic Scholar record | nothing beyond the metadata record. This record's identification, not merely its content, is uncertain |
| `eru-1890` | Harvey, Leybourne, Tatlow & Zu (2025). *Unit Root Tests for Explosive Financial Bubbles in the Presence of Deterministic Level Shifts*. *Oxford Bull. Econ. Stat.*, [doi:10.1111/obes.12668](https://doi.org/10.1111/obes.12668) | all numeric operating characteristics and the stated validity conditions | that deterministic level shifts are treated as a further validity condition on the Harvey–Leybourne line — from the indexed abstract. Recorded as an abstract-level pointer and used in §7.5 only as "a further validity condition is under study", never as an extracted result |

Three further records carry version or chain caveats that stop short of "no full
text" and are flagged wherever their numbers appear:

- `eru-1715` Kurozumi & Nishi (2025), [doi:10.1111/jtsa.12768](https://doi.org/10.1111/jtsa.12768):
  the PDF was unobtainable; content was obtained by fetching the publisher's
  full-text HTML through an intermediary summarisation step, so one model sits in
  the chain between the source and the extraction. Its numerals were flagged for
  the dual re-extraction pass and the dual pass never covered it. Numbers from
  this record are single-pass and intermediary-mediated.
- `eru-0259` Franses (2016), [doi:10.1016/j.csda.2014.06.006](https://doi.org/10.1016/j.csda.2014.06.006):
  the journal PDF was unobtainable (publisher paywall, no OA deposit located);
  extraction was performed on the working-paper twin `eru-0198` (Econometric
  Institute Report 2013-12). Numbers attributed to `eru-0259` are the
  working-paper's numbers.

  > **Withdrawn sentence (finding QUANT-3-5).** This bullet previously read
  > "Twin status **was verified** against the published article's indexed
  > abstract", four paragraphs before the blockquote below says same-work
  > identity "cannot be settled at the depth available". Those two sentences
  > cannot both stand. The affirmative one is **withdrawn**, and here is why
  > rather than merely that. It was a transcription of the recheck extraction
  > log's `doc` field, which says: "Twin status verified against the published
  > article's indexed abstract (same author, same growth-vs-acceleration
  > imbalance test on (1-L^2)y via recursive residuals, same Monte Carlo claim
  > of high power)." **The abstract that sentence names is not retained anywhere
  > and is not retrievable now.** `eru-0259`'s entry in the 1,996-record
  > candidate store carries **no `abstract` field** (only `eru-0198` does), and
  > on 2026-09-02 the CSDA article's abstract is **not deposited** in Crossref,
  > **not** present in OpenAlex (`W2007843530`) and **not** present in Semantic
  > Scholar — all three checked directly on this pass. So the comparison the
  > log asserts cannot be re-opened from this repository or from any of the three
  > metadata sources the review uses. The primary extraction log, written by the
  > other pass, records the pair as "**PROBABLE** SAME-WORK TWIN PAIR …
  > recorded as probable-twin for the review's dedup ledger to adjudicate" — so
  > the two passes disagree on the strength of the claim, and the review adopts
  > the weaker one. *(Also finding LITERATURE-3-2.)*

  > **This pair is a fourth X7 twin candidate that the review never adjudicated,
  > and §5.3's three-twin enumeration does not cover it (finding SCOPE-2-3;
  > amendment A13(b), verification gap VG-13).** What actually distinguishes it
  > from the three declared pairs — **restated round 3, because the round-2 form
  > of this sentence named two differences that are not true** (finding
  > LITERATURE-3-2) — is the *treatment*, not the membership: both records carry
  > **independent** appraisal rows in §6 (rows 4 and 64), where each declared
  > twin's row is `—` "appraised under its carrier"; and both **count in the 65
  > assessable denominator**, where the three declared twins are subtracted from
  > it (72 − 4 no-full-text − 3 twins = 65). Two claims are struck: "**unlike**
  > the three declared twins, both records are in the frozen included set" —
  > both members of all four pairs are in the frozen 72, which is why 72 records
  > are 69 works (§5.3); and "neither store entry carries a twin note" — the
  > round-2 remediation added a probable-twin note to **both** entries (§5.2),
  > so that sentence was already false when it was written. The project's own
  > extraction logs asked for the adjudication and it never happened:
  > `se-extraction-primary.jsonl` records `eru-0259` as "PROBABLE SAME-WORK TWIN
  > PAIR (eru-0198 WP, eru-0259 journal) … recorded as probable-twin for the
  > review's dedup ledger to adjudicate. If confirmed, the canonical extraction
  > moves under eru-0259 … and eru-0198 becomes a twin stub", and
  > `se-extraction-recheck.jsonl` records `eru-0198` as `{"twin_of":
  > "eru-0259"}`.
  >
  > **The two appraisal rows are two passes over one document.** Row 4
  > (`eru-0259`) is single-pass *recheck only*; row 64 (`eru-0198`) is
  > single-pass *primary only*; and the recheck pass's own `doc` field names the
  > EI Report 2013-12 PDF for `eru-0259`. Their cells diverge at **Q4** (`no` vs
  > `partial`) and **Q7** (`yes` vs `no`) — the two ER-RoB v1 questions L-11
  > names as ambiguous. Because the divergence sits across two *record ids*
  > rather than two passes over one id, it is **not** inside the 90-of-357
  > inter-pass divergence count of §2.8, which runs over the 51 records where one
  > id was answered by both passes. So the true inter-pass divergence on this
  > text is unrecorded in that statistic.
  >
  > **The evidentiary standard for a twin declaration, stated explicitly —
  > because the round-2 text applied one standard here and a different one to
  > the three declared pairs (finding LITERATURE-3-2).** The standard actually
  > used for the three declared pairs, read off §5.3's own "relation as
  > documented at extraction" column, is **documentary and single-text**: same
  > author line, same subject, and a documented working-paper-to-journal chain,
  > recorded at extraction, with **only one of the two texts ever read**. It is
  > not "both full texts compared". `eru-0622`/`eru-0675` was declared with
  > extraction "performed once on the WP text"; `eru-0904`/`eru-1526` was
  > declared on "author line, subject and LPY lineage documented at extraction"
  > and its titles differ too, so the title-mismatch objection does not separate
  > that pair from this one either.
  >
  > **On that standard `eru-0198`/`eru-0259` qualifies.** Sole author Philip Hans
  > Franses on both; the same growth-versus-acceleration imbalance test on
  > (1−L²)-differenced data via recursive residuals; and an explicit EI Report
  > 2013-12 → *CSDA* 100:160–169 chain. Round 2's stated ground for refusing —
  > "the journal text was never obtained" — **does not distinguish this pair from
  > `eru-0622`/`eru-0675`, whose journal text was likewise never read.** That was
  > a refusal on a ground the review does not apply elsewhere, and it is
  > withdrawn as the reason.
  >
  > **The reason the count nevertheless stays conditional is OPERATIONAL, not
  > evidential, and this review states which it is.** The three declared pairs
  > were given carrier/twin treatment *at extraction*: one extraction, one
  > appraisal row, the twin subtracted from every assessable denominator. This
  > pair was not — it was extracted and appraised twice, and both rows count in
  > the 65. Declaring it a twin now would not be a bookkeeping correction; it
  > would re-derive the 65 denominator, §6's row count, §6.1's per-domain
  > distributions and every "of 65" fraction in §7.3, §7.4 and §7.6, inside a
  > corpus this review is forbidden to re-screen and in a pass no further audit
  > round will check. **So: on the review's own declared standard the pair is a
  > twin and the distinct-work count is 68; the review does not renumber to 68
  > because doing so is a re-appraisal it may not perform, and it reports 69 as
  > the count under the three pairs adjudicated at extraction with 68 stated
  > beside it at every site.** A consumer who needs one number should use **68**
  > and read this box; a consumer reproducing the review's arithmetic should use
  > 69. What is *not* recorded any longer is a claim that the evidence is too
  > thin to decide — it is not, and saying so was the dodge.
  >
  > **What remains genuinely unsettled**, and is the residue VG-13 now carries:
  > no side-by-side reading of the two texts was ever performed, the journal text
  > is still unobtainable, and the two appraisal rows are two passes over one
  > document and are therefore not independent evidence either way. The corpus is
  > frozen and is not re-screened; §5.3's "69 distinct works" is retained as the
  > count under the three pairs *adjudicated at extraction*, explicitly
  > conditional.
- `eru-0150` Homm & Breitung (2012), [doi:10.1093/jjfinec/nbr009](https://doi.org/10.1093/jjfinec/nbr009),
  the corpus's canonical third-party comparison study: the journal version was
  unobtainable; extraction was performed on the June 2009 University of Bonn
  working paper. **This matters substantively.** The published version adds a
  CUSUM-based monitoring procedure that the working paper does not contain, so
  every O4 statement about Homm & Breitung's *monitoring* procedure in this review
  is sourced from other records citing it, never from `eru-0150` itself.

## 6. Appraisal — ER-RoB v1 per included study (items 11, 18)

**One row per included record: 72 rows** — 72 records, **69 distinct works**
(three same-work twins, appraised under their carriers and shown `—`; §5.3,
amendment A10(b)). No count in this section is a count of studies.

> **This appraisal is CONVENTION-RESOLVED, not source-adjudicated, and may not
> be cited as an adjudicated appraisal.** Protocol §4.3 requires primary/recheck
> mismatches to be "resolved against the source text". That reconciliation did
> not run (amendment A6, §2.8, L-2). 90 of 357 comparable cells diverged between
> the two extraction passes and are resolved here by the declared conservative
> ordering rule of §2.8, without reopening a single source. Every downstream use
> of an ER-RoB v1 concern in this review carries the same caveat, and any
> consumer citing a concern profile from §6 or §6.1 must carry it too.
> *(Finding SCOPE-1-3.)*

The instrument is the project-local `CONVENTION` instrument declared in protocol
§6 and reproduced in §2.7. It is **unvalidated**, adapted in form from QUADAS-2
and PROBAST but inheriting none of their validation, and it produces **no
composite score** — a concern profile per study, nothing summable.

**The instrument as executed departs from the instrument as frozen in two ways,
both now recorded as amendments.** (i) The frozen response scale is three levels
(`yes` / `no` / `unclear`); execution used four, adding `partial` in 50 of the
**561** answered Q-cells (8.9%) — 65 × 7 for Q1–Q7 plus 53 × 2 for Q8/Q9, not
65 × 9 = 585, because Q8 and Q9 are `n/a` for the 12 recheck-only records
(§2.7 denominator correction; amendment **A12**) — and the frozen concern rule
is undefined for the added
level — amendment **A7**, which fixes and labels the CONVENTION that `partial`
counts as not-`yes`. (ii) The frozen Q→D rule ("`no` or `unclear` on any
question in a domain raises that domain's concern") was not applied
mechanically; the D cells are the primary extractor's recorded judgments. The
divergence is not "a few cells": **31 D cells are recorded `low` where the rule
raises concern, and 13 run the other way** — amendment **A8**. Both columns are
therefore reported below. *(Findings QUANT-1-1, QUANT-1-2, REV-1-3.)*

> **What the 31 is counted against, stated because amendment A8's prose is not
> precise about it.** *(Added 2026-09-03, round-4 findings QUANT-1-6 and REV-1-6;
> protocol amendment **A15**.)* The **31** — and its 22 / 9 split — is counted
> against **the D column printed below**, i.e. the primary extractor's judgments
> **after** the §2.8 resolution raises marked `†`. A8 describes that column as
> "the primary extractor's own judgments, not as mechanical derivations from the
> Q cells", which reads as the *raw* `domain_concerns` field of
> `se-extraction-primary.jsonl`. Against that raw field the lenient count is
> **42** (D1 4, D2 1, D3 21, D4 9, D5 6, D6 1), of which 33 have a `no`/`unclear`
> input and 9 a `partial`-only input. The **strict** count is **13** (D3 1, D4 7,
> D5 5) under **both** readings. The legend below is precise where A8 is not, and
> the two extra domains D1 and D2 appear only in the raw-field count because the
> §2.8 resolution had already raised those cells. **No appraisal cell changes**;
> A8's decision to report both columns rather than restore the rule retroactively
> stands. Mechanical ground: `tests/test_erob_recount.py` (tracked at `01ecfe7`)
> reproduces the published 31/13 against this column.

Legend:

- Q-cell values are `yes` / `partial` / `unclear` / `no`; `n/a` = the question
  could not be answered because the underlying field was not extracted;
  `—` = twin record, appraised under its carrier.
- `†` on a Q cell: the primary and re-extraction passes diverged; the more
  conservative answer is shown, per the §2.8 resolution rule.
- `†` on a D cell: the domain concern is raised above the primary extractor's
  recorded value because of that resolution.
- `‡`: single-pass only — either the primary extractor could not reach the full
  text and the re-extraction pass supplied Q1–Q7 (Q8, Q9 then unanswerable), or
  the re-extraction pass never covered the record.
- Domain concerns (the `D1`…`D8` columns): `low` / `unclear` / `high`. These are
  **the primary extractor's own recorded judgments**, reproduced verbatim except
  where a `†` marks a raise under §2.8. They are *not* mechanical derivations
  from the Q cells.
- `D-rule` (final column): the **mechanically rule-derived** domain judgment, one
  character per domain in the order D1…D8, derived from that row's Q cells by
  protocol §6's rule with amendment A7's CONVENTION:
  - `L` — every answered question in the domain is `yes`, so the rule leaves the
    domain `low`;
  - `R` — at least one answered question is `no`, `unclear` or `partial`, so the
    rule **raises** the domain above `low`;
  - `·` — not assessable: the question was `n/a` (no full text, or Q8/Q9
    unanswerable on a recheck-only record) or the record is a twin.

  The rule is binary by construction. Protocol §6 says concern is "raised"; it
  does not say *to what level*, so `R` is deliberately not split into `unclear`
  and `high` — splitting it would require a cutoff the frozen instrument does not
  supply, i.e. an unlabelled constant.
- `§` on a D cell: the recorded judgment is `low` while `D-rule` gives `R`
  — the recorded cell is **less** concerning than the frozen rule produces.
  31 cells (D3 21, D4 7, D5 2, D6 1). Of these, 22 have a `no` or `unclear`
  input that the frozen rule decides outright (D3 13, D4 6, D5 2, D6 1) and 9
  turn on a `partial` input that only A7's CONVENTION decides (D3 8, D4 1).
- `¶` on a D cell: the recorded judgment is `unclear` or `high` while `D-rule`
  gives `L` — the recorded cell is **more** concerning than the rule produces.
  13 cells (D3 1, D4 7, D5 5).
- The `§` direction is the one that matters: it runs *toward lower concern*,
  against the direction-safe posture §2.8 adopts everywhere else. §6.1 therefore
  states the corpus profile on `D-rule` first and on the recorded judgments as a
  sensitivity.
- Tier abbreviations: `peer-rev`, `WP` (working paper), `preprint`, `other`.

| # | rec | study | tier | I2 | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | appraisal depth | D-rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | eru-0131 | Phillips, Wu & Yu 2011, *Explosive Behavior in the 1990s Nasdaq: When Did ...* | peer-rev | I2a | yes | yes | yes | yes | no | yes | unclear† | no | no | low | low | low | high | low | unclear | high | high | dual | `LLLRLRRR` |
| 2 | eru-0150 | Homm & Breitung 2012, *Testing for Speculative Bubbles in Stock Markets:...* | peer-rev | I2b | yes‡ | yes‡ | yes‡ | yes‡ | yes‡ | no‡ | yes‡ | n/a | n/a | low‡ | low‡ | low‡ | low‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LLLLRL··` |
| 3 | eru-0238 | Phillips, Shi & Yu 2014, *Specification Sensitivity in Right-Tailed Unit Ro...* | peer-rev | I2a | yes | yes | yes | yes | no | no | no† | no | no | low | low | low | low§ | high | high | high | high | dual | `LLLRRRRR` |
| 4 | eru-0259 | Franses 2016, *A simple test for a bubble based on growth and ac...* | peer-rev | I2b | yes‡ | yes‡ | yes‡ | no‡ | no‡ | yes‡ | yes‡ | n/a | n/a | low‡ | low‡ | high‡ | high‡ | low‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LLRRLL··` |
| 5 | eru-0348 | Sollis 2016, *Fixed and Recursive Right-Tailed Dickey-Fuller Te...* | peer-rev | I2b | yes | yes | no | no | no | no | no† | no | partial | low | low | high | high | high | high | high | unclear | dual | `LLRRRRRR` |
| 6 | eru-0393 | Phillips, Shi & Yu 2015, *Testing for Multiple Bubbles: Historical Episodes...* | peer-rev | I2a | yes | yes | yes | yes | no† | unclear† | unclear† | yes | no | low | low | low | high† | unclear† | unclear | low | high | dual | `LLLRRRLR` |
| 7 | eru-0395 | Phillips, Shi & Yu 2015, *Testing for Multiple Bubbles: Limit Theory of Rea...* | peer-rev | I2a | yes | no | yes | no† | yes | yes | unclear† | yes | no | low | high | unclear | low | low | unclear | low | high | dual | `LRRLLRLR` |
| 8 | eru-0463 | Harvey, Leybourne & Sollis 2017, *Improving the accuracy of asset price bubble star...* | peer-rev | I2b | yes‡ | no‡ | yes‡ | yes‡ | yes‡ | no‡ | yes‡ | n/a | n/a | low‡ | high‡ | low‡ | low‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LRLLRL··` |
| 9 | eru-0503 | Harvey et al. 2016, *Tests for explosive financial bubbles in the pres...* | peer-rev | I2a | yes | yes | yes | no | no | no | no† | no | partial | low | low | low§ | high | high | high | high | unclear | dual | `LLRRRRRR` |
| 10 | eru-0559 | Phillips & Shi 2018, *Financial Bubble Implosion and Reverse Regression* | peer-rev | I2a | yes | no | yes | partial† | yes | partial† | no† | no | no | low | high | low§ | low | unclear | high | high | high | dual | `LRRLRRRR` |
| 11 | eru-0597 | Kholodilin, Michelsen & Ulbricht 2018, *Speculative price bubbles in urban housing markets* | peer-rev | I2b\|I2c | unclear† | unclear† | yes | no | yes | no | no | no | no | unclear† | unclear† | unclear | high¶ | high | high | high | high | dual | `RRRLRRRR` |
| 12 | eru-0604 | Landgraf 2016/2017, *Testing for Multiple Bubbles in Asset Prices* | other | I2b | yes | partial† | yes | yes | no | no | no† | no | no | low | unclear | low | low§ | high | high | high | high | dual | `LRLRRRRR` |
| 13 | eru-0607 | Pavlidis, Paya & Peel 2017, *Testing for Speculative Bubbles Using Spot and Fo...* | peer-rev | I2b | yes | no | yes | yes | yes | unclear† | no | no | partial | low | high | low | low | unclear† | high | high | unclear | dual | `LRLLRRRR` |
| 14 | eru-0609 | Astill et al. 2017, *Tests for an end-of-sample bubble in financial ti...* | peer-rev | I2a\|I2b | yes | yes | yes | no | no | yes | no | no | partial | low | low | unclear | high | unclear¶ | high | high | unclear | dual | `LLRRLRRR` |
| 15 | eru-0689 | Whitehouse 2019, *Explosive Asset Price Bubble Detection with Unkno...* | peer-rev | I2a | yes‡ | no‡ | yes‡ | no‡ | no‡ | no‡ | yes‡ | n/a | n/a | low‡ | high‡ | high‡ | high‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LRRRRL··` |
| 16 | eru-0735 | Astill et al. 2018, *Real-Time Monitoring for Explosive Financial Bubbles* | peer-rev | I2a | yes | yes | yes | no† | no† | yes | yes | no | partial | low | low | unclear | high† | low | low | high | unclear | dual | `LLRRLLRR` |
| 17 | eru-0748 | Harvey, Leybourne & Zu 2019, *Testing explosive bubbles with time-varying volat...* | peer-rev | I2a | yes | partial† | yes | no | no | no | no† | no | partial | low | unclear | low§ | high | high | high | high | unclear | dual | `LRRRRRRR` |
| 18 | eru-0883 | Tao, Phillips & Yu 2019, *Random coefficient continuous systems: Testing fo...* | peer-rev | I2a | yes‡ | yes‡ | yes‡ | unclear‡ | no‡ | yes‡ | no‡ | n/a | n/a | low‡ | low‡ | unclear‡ | high‡ | low‡ | high‡ | n/a | n/a | single-pass (recheck only) | `LLRRLR··` |
| 19 | eru-0889 | Horvath et al. 2020, *Sequential monitoring for changes from stationari...* | peer-rev | I2a | yes | yes | yes | no | partial† | yes | yes | no | partial | low | low | low§ | high | low | low | high | unclear | dual | `LLRRLLRR` |
| 20 | eru-0891 | Harvey, Leybourne & Zu 2020, *Sign-Based Unit Root Tests for Explosive Financia...* | peer-rev | I2a | yes‡ | yes‡ | yes‡ | yes‡ | yes‡ | no‡ | yes‡ | n/a | n/a | low‡ | low‡ | low‡ | low‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LLLLRL··` |
| 21 | eru-0924 | Laurent & Shi 2019/2022, *Unit Root Test with High-Frequency Data* | WP | I2a | yes‡ | yes‡ | yes‡ | no‡ | no‡ | unclear‡ | no‡ | n/a | n/a | low‡ | low‡ | high‡ | high‡ | unclear‡ | high‡ | n/a | n/a | single-pass (recheck only) | `LLRRRR··` |
| 22 | eru-1031 | Phillips & Shi 2020, *Real time monitoring of asset markets: Bubbles an...* | peer-rev | I2a | yes | no | no | no† | no | unclear† | yes | yes | no | low | high | high | high | unclear | low | low | high | dual | `LRRRRLLR` |
| 23 | eru-1038 | Horvath, Liu & Lu 2020, *Sequential Monitoring of Changes in Housing Prices* | preprint | I2a | yes | yes | yes | no | yes | yes | yes | no | no | low | low | low§ | high¶ | low | low | high | high | dual | `LLRLLLRR` |
| 24 | eru-1044 | Monschang & Wilfling 2021, *Sup-ADF-style bubble-detection methods under test* | peer-rev | I2b | yes | yes | yes | yes | partial† | unclear† | no† | no | partial | low | low | low | low§ | unclear | high | high | unclear | dual | `LLLRRRRR` |
| 25 | eru-1049 | Pedersen & Schutte 2020, *Testing for explosive bubbles in the presence of ...* | peer-rev | I2b | yes | yes | yes | partial† | yes | no† | no† | no | partial | low | low | low§ | low | high | high | high | unclear | dual | `LLRLRRRR` |
| 26 | eru-1112 | Chen, Phillips & Shi 2022, *Common Bubble Detection in Large Dimensional Fina...* | peer-rev | I2a | yes | no | yes | no† | yes | unclear† | no† | no | no | low | high | unclear | unclear¶ | unclear | high† | high | high | dual | `LRRLRRRR` |
| 27 | eru-1117 | Astill et al. 2021, *CUSUM-Based Monitoring for Explosive Episodes in ...* | peer-rev | I2a | yes | yes | yes | no† | no† | yes | yes | no | partial | low | low | unclear | high† | low | low | high | unclear | dual | `LLRRLLRR` |
| 28 | eru-1384 | Kurozumi, Skrobotov & Tsarev 2022, *Time-Transformed Test for Bubbles under Non-stati...* | peer-rev | I2a | yes | yes | yes | no | no | no | no† | yes | partial | low | low | low§ | high | high | high | low | unclear | dual | `LLRRRRLR` |
| 29 | eru-1394 | Astill et al. 2023, *Using covariates to improve the efficacy of univa...* | peer-rev | I2a | yes | yes | yes | no | yes | yes | no | no | partial | low | low | low§ | high¶ | low | high | high | unclear | dual | `LLRLLRRR` |
| 30 | eru-1519 | Whitehouse, Harvey & Leybourne 2023, *Real-Time Monitoring of Bubbles and Crashes* | peer-rev | I2a\|I2b | yes | yes | yes | yes | yes | yes | yes | no | partial | low | low | unclear¶ | low | low | low | high | unclear | dual | `LLLLLLRR` |
| 31 | eru-1526 | Lui, Phillips & Yu 2024, *Robust testing for explosive behavior with strong...* | peer-rev | I2a | yes | yes | yes | no† | yes | unclear† | unclear† | no | partial | low | low | low§ | high¶ | unclear† | unclear | high | unclear | dual | `LLRLRRRR` |
| 32 | eru-1604 | Pavlidis 2025, *Bubbles and crashes: A tale of quantiles* | peer-rev | I2b | yes | yes | yes | yes | no | no | no | no | partial | low | low | low | low§ | high | high | high | unclear | dual | `LLLRRRRR` |
| 33 | eru-1716 | Boswijk, Yu & Zu 2024, *Testing for an Explosive Bubble using High-Freque...* | preprint | I2a | yes | yes | yes | no | no | yes | no† | no | yes | low | low | low§ | high | high¶ | high | high | low | dual | `LLRRLRRL` |
| 34 | eru-1813 | Vriz & Grossi 2025, *Green bubbles: A four-stage paradigm for detectio...* | peer-rev | I2b | unclear† | no | no† | no† | no† | unclear† | no† | no | no | unclear† | high | high† | high† | low§ | high | high | high | dual | `RRRRRRRR` |
| 35 | eru-1844 | Whitehouse, Harvey & Leybourne 2025, *Real-time monitoring procedures for early detecti...* | peer-rev | I2a | yes | yes | yes | no† | no† | yes | yes | partial | partial | low | low | unclear | high† | low | low | unclear | unclear | dual | `LLRRLLRR` |
| 36 | eru-1845 | Horvath & Trapani 2025, *Real-Time Monitoring with RCA Models* | peer-rev | I2a | yes | yes | yes | partial† | yes | yes | yes | no | partial | low | low | low§ | low | low | low | high | unclear | dual | `LLRLLLRR` |
| 37 | eru-1852 | Breitung & Diegel 2025, *Sequential Detector Statistics for Speculative Bu...* | peer-rev | I2a | yes | yes | yes | no | yes | yes | yes | no | partial | low | low | unclear | low | low | low | high | unclear | dual | `LLRLLLRR` |
| 38 | eru-1920 | Kurozumi & Skrobotov 2026, *Confidence sets for the emergence, collapse, and ...* | peer-rev | I2a | yes | yes | yes | no† | yes | no | no† | no | no | low | low | unclear | low | high | unclear | high | high | dual | `LLRLRRRR` |
| 39 | eru-1921 | Astill, Taylor & Zu 2026, *Covariate-Augmented CUSUM Bubble Monitoring Proce...* | peer-rev | I2a | yes | yes | yes | no | no† | yes | yes | no | no | low | low | unclear | high† | low | low | high | high | dual | `LLRRLLRR` |
| 40 | eru-1929 | Sarkar & Wells 2026, *Double Local-to-Unity: Inference under Nearly Non...* | preprint | I2a | yes | no† | no | no | no | no | no | partial | partial | low | high | high | high | high | high | unclear | unclear | dual | `LRRRRRRR` |
| 41 | eru-1950 | Sarkar & Wells 2026, *Is there an AI bubble? Robust date-stamping for p...* | peer-rev | I2a | yes | no† | yes | no† | yes | yes | unclear† | yes | partial | low | high† | low§ | high¶ | low | unclear | low | unclear | dual | `LRRLLRLR` |
| 42 | eru-0100 | Phillips & Yu 2009, *Limit Theory for Dating the Origination and Colla...* | WP | I2a | yes‡ | no‡ | no‡ | yes‡ | yes‡ | yes‡ | yes‡ | n/a | n/a | low‡ | high‡ | high‡ | low‡ | low‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LRRLLL··` |
| 43 | eru-0112 | Shi, Anderson & Vahid 2010, *Testing for Periodically Collapsing Bubbles: A Ge...* | WP | I2a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | no full text; ER-RoB v1 not applied | `········` |
| 44 | eru-0154 | Phillips PCB, Yu J (2011). The Timeline of Financial Bubbles | WP | I2a | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | twin of eru-0126 | `········` |
| 45 | eru-0268 | Mihailovic 2014, *Detecting speculative bubbles in GARCH processes:...* | other | I2b | yes‡ | no‡ | yes‡ | yes‡ | no‡ | yes‡ | no‡ | n/a | n/a | low‡ | high‡ | low‡ | high‡ | low‡ | high‡ | n/a | n/a | single-pass (recheck only) | `LRLRLR··` |
| 46 | eru-0427 | Shi 2016, *Speculative Bubbles or Market Fundamentals? An In...* | WP | I2a | yes | no | no | no | no† | unclear | no | no | no | low | high | high | high† | high | unclear | high | high | dual | `LRRRRRRR` |
| 47 | eru-0513 | Virtanen et al. 2017/2018, *Use of unit root methods in early warning of fina...* | WP | I2c | unclear† | no | no | no | no† | yes | partial† | no | no | unclear† | high | high | high† | unclear¶ | unclear | high | high | dual | `RRRRLRRR` |
| 48 | eru-0526 | Fulop & Yu 2017, *Bayesian Analysis of Bubbles in Asset Prices* | peer-rev | I2b | partial† | no† | partial† | no† | yes | yes | no† | no | no | high | high | unclear | low | low | high | high | high | dual | `RRRLLRRR` |
| 49 | eru-0622 | Pavlidis, Martinez-Garcia & Grossman 2017, *Detecting Periods of Exuberance..* | WP | I2b | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | twin of eru-0675 | `········` |
| 50 | eru-0675 | Pavlidis, Martinez-Garcia & Grossman 2018, *Detecting periods of exuberance: A look at the ro...* | peer-rev | I2b | yes | no | unclear† | no† | no | no | no | partial | partial | low | high | high† | high | unclear | high | high | unclear | dual | `LRRRRRRR` |
| 51 | eru-0691 | Kruse & Wegener 2018, *Explosive behaviour and long memory with an appli...* | peer-rev | I2b | yes | yes | yes | no | no | no | no | no | partial | low | low | unclear | high | high | high | high | unclear | dual | `LLRRRRRR` |
| 52 | eru-0749 | Hafner 2020, *Testing for Bubbles in Cryptocurrencies with Time...* | peer-rev | I2b | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | no full text; ER-RoB v1 not applied | `········` |
| 53 | eru-0823 | Phillips & Shi 2019, *Detecting Financial Collapse and Ballooning Sover...* | peer-rev | I2a | yes | no | yes | partial† | yes | unclear† | no† | no | partial | low | high | low§ | low | unclear† | high | high | unclear | dual | `LRRLRRRR` |
| 54 | eru-0904 | Lui 2019, *Testing for Rational Bubbles under Strongly Depen...* | WP | I2a | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | twin of eru-1526 | `········` |
| 55 | eru-0959 | Harvey, Leybourne & Whitehouse 2020, *Date-stamping multiple bubble regimes* | peer-rev | I2a | yes‡ | no‡ | no‡ | yes‡ | yes‡ | no‡ | yes‡ | n/a | n/a | low‡ | high‡ | high‡ | low‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LRRLRL··` |
| 56 | eru-1155 | Harsha & Ismail 2018, *Improved Test for Detecting Explosive Bubbles* | peer-rev | I2b | unclear† | no | yes | yes | no | no | no | no | no | unclear† | high | low | low§ | high | high | high | high | dual | `RRLRRRRR` |
| 57 | eru-1260 | Wang & Yu 2023, *Bubble testing under polynomial trends* | peer-rev | I2a | yes‡ | yes‡ | yes‡ | no‡ | no‡ | no‡ | yes‡ | n/a | n/a | low‡ | low‡ | high‡ | high‡ | high‡ | low‡ | n/a | n/a | single-pass (recheck only) | `LLRRRL··` |
| 58 | eru-1310 | Ibragimov, Parlour & Walden 2022, *Fundamental Value Pricing and Bubbles for Nontrad...* | WP | I2b | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | no full text; ER-RoB v1 not applied | `········` |
| 59 | eru-1405 | Liu, Phillips & Yu 2023, *A Panel Clustering Approach to Analyzing Bubble B...* | peer-rev | I2a | yes | partial† | yes | no | no† | no | no | no | no | low | high | low§ | high† | high | high | high | high | dual | `LRRRRRRR` |
| 60 | eru-1580 | Harvey et al. 2024, *A new heteroskedasticity-robust test for explosiv...* | peer-rev | I2a | yes | yes | yes | no† | no | no | no† | no | partial | low | low | low§ | high | high | high | high | unclear | dual | `LLRRRRRR` |
| 61 | eru-1715 | Kurozumi & Nishi 2025, *Testing for a bubble with a stochastically varyin...* | peer-rev | I2a | yes‡ | yes‡ | yes‡ | no‡ | no‡ | unclear‡ | no‡ | no‡ | no‡ | low‡ | low‡ | low‡§ | high‡ | high‡ | unclear‡ | high‡ | high‡ | single-pass (primary only) | `LLRRRRRR` |
| 62 | eru-1890 | Harvey et al. 2025, *Unit Root Tests for Explosive Financial Bubbles i...* | peer-rev | I2a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | no full text; ER-RoB v1 not applied | `········` |
| 63 | eru-0126 | Phillips & Yu 2011, *Dating the timeline of financial bubbles during t...* | peer-rev | I2a | yes | no | no | no† | no† | yes | unclear† | no | no | low | high | high | high† | low | unclear | high | high | dual | `LRRRLRRR` |
| 64 | eru-0198 | Franses 2013, *Are we in a bubble? A simple time-series-based di...* | WP | I2b | yes‡ | yes‡ | yes‡ | partial‡ | no‡ | yes‡ | no‡ | no‡ | no‡ | low‡ | low‡ | low‡§ | low‡§ | high‡¶ | high‡ | high‡ | high‡ | single-pass (primary only) | `LLRRLRRR` |
| 65 | eru-0731 | Ardila, Sanadgol & Sornette 2018, *Out-of-sample forecasting of housing bubble tippi...* | peer-rev | I2c | yes | no | no | no | no† | yes | no† | no | partial | low | high | high | high† | low | high | high | unclear | dual | `LRRRLRRR` |
| 66 | eru-0813 | Bertelsen 2019, *Comparing Tests for Identification of Bubbles* | WP | I2b | partial† | yes | yes | partial† | yes | no | no† | no | no | unclear | low | low§ | low | low§ | high | high | high | dual | `RLRLRRRR` |
| 67 | eru-0855 | Zhang & Wu 2019, *High-Dimensional Multiple Bubbles Prediction Base...* | peer-rev | I2a | unclear‡ | no‡ | no‡ | no‡ | no‡ | unclear‡ | no‡ | n/a | n/a | unclear‡ | high‡ | high‡ | high‡ | unclear‡ | high‡ | n/a | n/a | single-pass (recheck only) | `RRRRRR··` |
| 68 | eru-1289 | Shi & Phillips 2022, *Econometric Analysis of Asset Price Bubbles* (DP 2331; tier corrected to WP) | WP | I2b | yes | yes | yes | no† | yes | yes | yes | no | partial | low | low | unclear | high¶ | low | low | high | unclear | dual | `LLRLLLRR` |
| 69 | eru-1509 | Morita et al. 2023, *On testing for bubbles during hyperinflations* | peer-rev | I2b | yes | yes | yes | no† | no | no† | no | no | no | low | low | low§ | high | high† | unclear | high | high | dual | `LLRRRRRR` |
| 70 | eru-1761 | Blasques et al. 2025, *A Novel Test for the Presence of Local Explosive ...* | peer-rev | I2b | yes | yes | yes | partial† | no† | yes | no | no | partial | low | low | low§ | high† | unclear¶ | low§ | high | unclear | dual | `LLRRLRRR` |
| 71 | eru-1770 | Giancaterini et al. 2026, *Bubble Detection with Application to Green Bubble...* | preprint | I2b | yes | yes | yes | partial† | no | unclear† | no | no | partial | low | low | low§ | low§ | high† | unclear | high | unclear | dual | `LLRRRRRR` |
| 72 | eru-1889 | Magdalinos & Petrova 2025, *Uniform Inference with General Autoregressive Pro...* | WP | I2a | yes | yes | yes | no | no | yes | no | no | partial | low | low | unclear | high | low | high | high | unclear | dual | `LLRRLRRR` |

### 6.1 Domain concern profile across the corpus (item 18)

**Denominators first, because they are not 72.** Of the 72 records, 3 are twins
appraised `—` under their carriers and cannot contribute a numerator by
construction; 4 more have no full text at any stage, so every Q cell is `n/a`;
and 12 further records were read only at the recheck pass, where Q8 and Q9 were
unanswerable. The assessable denominators are therefore **65 for Q1–Q7 and
D1–D6**, and **53 for Q8/Q9 and D7/D8**. Every fraction below and in §7 is
stated over its assessable denominator, with the excluded classes named.
*(Finding REV-1-4.)*

**(a) Rule-derived profile — the primary statement.** This is protocol §6's
Q→D rule applied mechanically, with amendment A7's CONVENTION for `partial`
(the `D-rule` column of §6). `low` means every answered question in the domain
is `yes`; `raised` means at least one is not.

| domain | low | raised | assessable n | not assessable |
|---|---|---|---|---|
| D1 null & critical-value provenance | 58 | 7 | 65 | 4 no-full-text + 3 twins |
| D2 size | 39 | 26 | 65 | 4 + 3 |
| D3 power & DGP realism | 13 | 52 | 65 | 4 + 3 |
| D4 date-stamping accuracy / delay | 23 | 42 | 65 | 4 + 3 |
| D5 causality status | 27 | 38 | 65 | 4 + 3 |
| D6 multiplicity | 19 | 46 | 65 | 4 + 3 |
| D7 reproducibility | 5 | 48 | 53 | 16 unanswerable + 3 twins |
| D8 applicability to intraday futures | 1 | 52 | 53 | 16 + 3 |

**(b) Recorded-judgment profile — reported as sensitivity.** These are the
primary extractor's own domain judgments after the §2.8 resolution, i.e. the
`D1`…`D8` columns of §6. They diverge from (a) in 44 cells: 31 marked `§`
(recorded `low`, rule raises — *toward lower concern*) and 13 marked `¶`
(recorded `unclear`/`high`, rule leaves `low`). Amendment A8.

| domain | low | unclear | high | n/a | — | divergences vs (a) |
|---|---|---|---|---|---|---|
| D1 null & critical-value provenance | 58 | 6 | 1 | 4 | 3 | 0 |
| D2 size | 39 | 3 | 23 | 4 | 3 | 0 |
| D3 power & DGP realism | 33 | 16 | 16 | 4 | 3 | 21 `§`, 1 `¶` |
| D4 date-stamping accuracy / delay | 23 | 1 | 41 | 4 | 3 | 7 `§`, 7 `¶` |
| D5 causality status | 24 | 14 | 27 | 4 | 3 | 2 `§`, 5 `¶` |
| D6 multiplicity | 20 | 12 | 33 | 4 | 3 | 1 `§` |
| D7 reproducibility | 5 | 2 | 46 | 16 | 3 | 0 |
| D8 applicability to intraday futures | 1 | 29 | 23 | 16 | 3 | 0 |

Where (a) and (b) differ materially the difference is stated, not averaged. The
largest gap is D3, where the recorded judgments put 33 records at `low` and the
frozen rule puts 13 — a direct consequence of 41 records answering Q4 (collapse
mechanism) `no` while D3 was nonetheless recorded `low` in 13 of them and
`partial`-driven in 8 more.

Underlying signalling-question distributions (after the §2.8 resolution), with
their assessable denominators:

| question | yes | partial | unclear | no | assessable n | n/a | — |
|---|---|---|---|---|---|---|---|
| Q1 null + CV provenance stated | 58 | 2 | 5 | 0 | 65 | 4 | 3 |
| Q2 empirical size reported | 39 | 3 | 1 | 22 | 65 | 4 | 3 |
| Q3 power under parameterised explosive alternatives | 52 | 1 | 1 | 11 | 65 | 4 | 3 |
| Q4 collapse mechanism in the alternatives | 15 | 8 | 1 | 41 | 65 | 4 | 3 |
| Q5 dating accuracy / delay distributions | 23 | 2 | 0 | 40 | 65 | 4 | 3 |
| Q6 evaluated in real-time form | 27 | 1 | 13 | 24 | 65 | 4 | 3 |
| Q7 recursive-sequence multiplicity addressed | 19 | 1 | 6 | 39 | 65 | 4 | 3 |
| Q8 code/data available | 5 | 3 | 0 | 45 | 53 | 16 | 3 |
| Q9 applicability to intraday futures | 1 | 29 | 0 | 23 | 53 | 16 | 3 |

**Four readings the profile supports, each stated as a property of the
literature's reporting, not of any detector's quality, and each stated on the
rule-derived column (a) with the recorded column (b) alongside.**

1. **D1 is the corpus's strongest domain: 58 of 65 assessable records `low`
   under the rule (89%); 58 low / 1 high as recorded.** This literature states
   its null and the provenance of its critical values. That is the precondition
   for everything else and it is met almost universally. This is the one domain
   where the two columns agree cell for cell.
2. **D4 is the corpus's weakest substantive domain among those every record can
   be scored on: 42 of 65 raised (65%), 23 low; as recorded, 41 high / 23 low /
   1 unclear.** Most records that propose or evaluate a *date-stamping* method
   do not report the accuracy or delay of the dates it produces. Detection power
   is reported; dating error is not. For a consumer whose object is the date,
   this is the single most important gap in the published record. D4 also
   carries the largest two-way divergence (7 `§`, 7 `¶`), so the recorded and
   rule-derived counts happen to land close for opposite reasons.
3. **D6 is next weakest: 46 of 65 raised (71%), 19 low; as recorded, 33 high /
   12 unclear / 20 low.** The recursive sequence's multiplicity is handled
   asymptotically in most of the family literature (diverging critical-value
   sequences, α_T → 0) and measured in finite samples almost nowhere. §7.4 gives
   the one direct measurement.
4. **D7 is the weakest domain overall: 48 of 53 assessable records raised
   (91%), 5 low; as recorded, 46 high / 2 unclear / 5 low.** The denominator is
   53, not 72 and not 56: 16 records could not be scored on Q8 (4 with no full
   text, 12 read only at the recheck pass where Q8/Q9 are unanswerable) and 3
   are twins. Eight records of the 53 publish a code or data locator (5 `yes`,
   3 `partial`). The operating characteristics this review synthesises are, for
   the most part, not independently regenerable from what their authors
   published.

D8 deserves separate emphasis because it is the consumer's question: of the 53
assessable records, exactly one (`eru-1716`, Boswijk, Yu & Zu 2024) is judged
`yes` — it uses intraday data explicitly, though its own authors state the test
operates at low frequency with intraday data entering only through realised
volatility. Everything else in the corpus is `partial` (a transferable
mechanism, wrong frequency) or `no`.

**What none of these numbers is.** Each is a count of records whose *reporting*
satisfies a signalling question, resolved by convention rather than against the
sources (A6, L-2), under an unvalidated instrument (L-11), over a corpus that
lost 47.8% of its full-text-stage records to unobtainability (L-4) and whose
backward-chase arm ran only as a post-freeze diagnostic (A11, L-5). None of them
is a measurement of any detector's quality.


## 7. Synthesis by outcome domain (items 13, 20)

Every value below is a *published* number transcribed from a source document at
the extraction stage, with its table or page location. **Nothing here was
computed, simulated or re-derived by this review** (ADR-0003). Where a value is
single-pass or intermediary-mediated the row says so. Where a value is
preprint-tier the row says so.

**Reading rule, stated once and applied throughout, and corrected here.** A count
of records is a fact about **this corpus's** coverage — never about the
literature, and never about a detector. "Nine records report X" means nine
records *in the frozen 72-record set* report X; it is not evidence that X holds,
and it is not an estimate of how many works in the literature report X.

The earlier form of this rule said "a fact about the literature's coverage",
which licenses exactly the generalisation the corpus cannot support: the corpus
lost 47.8% of its full-text-stage records to unobtainability with unknown
direction (L-4, VG-2), failed three of fourteen known-item recall checks on the
pre-2011 antecedent layer (§2.3), and ran its backward-chase arm only after
freeze, over 22 of 27 carriers, through deposited reference lists (A11, L-5,
VG-4). **Every coverage fraction in §6.1, §7 and §10.4 is a census statistic of
the frozen set, not a sample estimate of a literature-level proportion.** No
binomial interval is attached to any of them, and none should be: there is no
sampling frame under which the 72 are a probability sample of anything. Where a
§7 claim could be read as a universal negative about the literature, the bound is
attached at the point of claim, not deferred to §12.1. *(Finding REV-2-5.)*

### 7.1 O1 — empirical size under the stated null

**What the family's own papers report.** Under a martingale null with
asymptotically negligible drift and iid errors, the recursive right-tailed family
is close to nominal in the sample sizes its originators simulate:

| detector | reported size | design | source |
|---|---|---|---|
| SADF | 0.041 / 0.049 / 0.042 / 0.054 / 0.060 at 5% | T = 100/200/400/800/1600, asymptotic CVs, **lag k = 0**, r₀ = 0.01+1.8/√T | `eru-0393` Table 2 **p.1058**, [PSY 2015a](https://doi.org/10.1111/iere.12132) |
| GSADF | 0.061 / 0.058 / 0.055 / 0.069 / 0.070 at 5% | same design, **lag k = 0** | `eru-0393` Table 2 **p.1058** |
| SADF, GSADF — **same null DGP, lag order overspecified** | SADF up to **0.184**; **GSADF up to 0.787** at 5% (fixed k = 6, T = 100, r₀ = 0.190). Under significance-test kmax = 6 at T = 100: SADF **0.145**, GSADF **0.697** — the pair the authors themselves single out in the text | identical null DGP (3) with d = η = 1, asymptotic CVs, 5,000 replications; **only the fitted lag order changes** — a specification choice, not a departure from the stated null | `eru-0393` Table 2 **p.1058** |
| ADF₁ (full-sample) | 0.049 at 5% | n = 120, 10,000 reps, Nasdaq-calibrated no-bubble DGP (g = 0.00 column) | `eru-0131` Table 3 Panel A p.219, [PWY 2011](https://doi.org/10.1111/j.1468-2354.2010.00625.x) |
| SADF, GSADF (third-party replication) | SADF 0.0385–0.0457; GSADF 0.0484–0.0566 at 5%, asymptotic CVs | T = 100–1600, homoskedastic null | `eru-1044` Table 2, [Monschang & Wilfling 2021](https://doi.org/10.1007/s00181-020-01859-7) |
| supDF / supDFC / supK / supBT / supB (comparison line) | 0.053 / 0.046 / 0.050 / 0.049 / 0.041 at 5% | T = 100, no-bubble fundamental DGP, detrended | `eru-0150` Tables 4–5 first row, Homm & Breitung WP (see §5.4 version caveat) |
| supADF / CUSUM / mCUSUM / wCUSUM / AHLT10 | 0.056 / 0.040 / 0.044 / 0.037 / 0.071 at 5% | 10,000 reps, τ = 100 | `eru-1852` Table 3, [Breitung & Diegel 2025](https://doi.org/10.1111/jtsa.12845) |

**What the critique literature reports.** The corpus's size results are dominated
not by the null-case numbers above but by the size *failures* under departures
from the iid-homoskedastic null. These are the corpus's most replicated finding —
seven independent author teams, each identifying a different departure:

| departure from the stated null | reported size at nominal 5% | source |
|---|---|---|
| non-stationary (deterministically time-varying) volatility | PWY asymptotically oversized up to ≈ 0.62; wild-bootstrap PWY\* asymptotic size 0.05 across all σ₁/σ₀ | `eru-0503` Figures 1–2, [HLST 2016](https://doi.org/10.1016/j.jempfin.2015.09.002) |
| single/dual volatility shift, sign-based comparison | PSY 0.042–0.64 across shift configurations | `eru-0891` Table 2, [Harvey, Leybourne & Zu 2020](https://doi.org/10.1017/s0266466619000057) (single-pass, §5.4) |
| autocorrelated (ARMA) innovations, fixed lag k = 0 | severe over-rejection, up to ≈ 1.00 in the worst MA(3) cells | `eru-1049` Tables 2–3, [Pedersen & Schutte 2020](https://doi.org/10.1016/j.jempfin.2020.06.002) |
| strongly dependent (long-memory) errors | standard DF t: 0.05 at d = 0 → 0.48 (n = 100), 0.56 (n = 500) at d = 0.45 | `eru-1526` Table 2, [Lui, Phillips & Yu 2024](https://doi.org/10.1016/j.jeconom.2023.105626) |
| long memory, PWY with unadjusted CVs | 0.0450 (dᵤ=0) → 0.3156 (dᵤ=0.2) → 0.4670 (dᵤ=0.4) at T = 250 | `eru-0691` Table 1, [Kruse & Wegener 2018](https://doi.org/10.1111/sjpe.12179) |
| leverage / asymmetric conditional volatility (TGARCH) | GSADF up to 0.29 | `eru-1044` Table 4 |
| stochastic volatility (Heston) at daily frequency | classical PWY **0.048–0.392** (was reported as 0.048–0.282, which omitted the c = 1.5 column; L-21) | `eru-1716` Table 1, [Boswijk, Yu & Zu 2024](https://arxiv.org/abs/2405.02087) — **preprint tier** |
| price jumps under in-fill asymptotics | right-sided DF up to 0.397 | `eru-0924` Table 2, [Laurent & Shi](https://doi.org/10.2139/ssrn.3421332) (published *Econometric Theory* 38(1):113–171) |
| deterministic drift break under the null | DF_μ diverges; size tends to 1 or 0 depending on break sign | `eru-0348` Theorem 1 and Table 2, [Sollis 2016](https://doi.org/10.1515/jtse-2013-0004) |
| polynomial deterministic trend | AR(1)-based GSADF/BSADF false-detection probability → 1 | `eru-1260` Theorem 2.1.2–2.1.3, [Wang & Yu 2023](https://doi.org/10.1093/ectj/utac020) (single-pass, §5.4) |
| serially correlated innovations, third-party comparison | GSADF up to 0.7290 (AR(1)) | `eru-0813` Table 2, Bertelsen 2019 — **working-paper tier** |
| end-of-sample regime, MA errors | BSADF_B 0.106–0.208 at nominal 0.05 | `eru-0609` Table 1, [Astill et al. 2017](https://doi.org/10.1080/07474938.2017.1307490) |
| heavy tails and lag-length misspecification | GSADF up to 0.67 | `eru-1604`, [Pavlidis 2025](https://doi.org/10.1111/jtsa.12794) |

**Synthesis claim (O1), and the near-nominal figures are conditional on a
specification choice as well as on the null.** *The recursive right-tailed
family's near-nominal size is a property of its stated null **and of a small
fixed lag order**, not of the family.* Before any departure from the null is
considered, the originators' own Table 2 (p.1058) shows GSADF size rising to
**0.787** at nominal 5% — nearly sixteen times nominal — under the **same** null
DGP, with only the fitted lag order changed to k = 6 at T = 100; and to 0.697
when kmax = 6 is chosen by sequential significance testing, alongside SADF 0.145.
Lag-order selection is a specification decision the analyst makes, not a property
of the data-generating process, so a synthesis reporting only the k = 0 column
would imply the stated null is safe irrespective of lag choice. It is not, and
PSY's own recommendation follows from exactly this: "size is reasonably well
controlled when a small fixed lag length is used in the recursive tests"
(p.1058). *(Finding REV-3-6.)* Beyond the lag-order axis, every departure from
`iid errors + constant unconditional variance + asymptotically negligible drift +
no deterministic trend + no jumps` that the corpus tests produces size distortion,
in most cases severe, and **upward in every case the corpus tests except the
drift-break null (`eru-0348`), where the direction depends on the sign of the
break**: Sollis 2016 Theorem 1 and Table 2 report that DF_μ diverges and size
tends to 1 *or to 0* according to the break sign. A downward distortion is a
power failure, not a false-alarm failure, and a consumer would draw the opposite
operational conclusion from it, so the exception is stated here and carried into
TC-1 rather than absorbed into "always upward". *(Finding QUANT-1-5.)*
Evidence tier: peer-reviewed for all but two rows; concern profile
(**convention-resolved, not source-adjudicated** — §6 header, A6): D2 recorded
`low` for every source in the second table (these papers exist to measure
size). Causality
status: **all of these are O6=FS or CS results**, measured on full-sample
statistics; not one of them is a real-time false-alarm rate.

`TO COMPUTE` handoff **TC-1**, with **lag-order selection as a declared input**
(finding REV-3-6) — the corpus's own originator table moves GSADF size from 0.061
to 0.787 on that choice alone, under an unchanged null, so a size figure reported
without its lag rule is uninterpretable: size of any chosen detector under the
executing project's own intraday null, reported as a function of the lag rule
used (fixed k, BIC, or sequential significance testing at a stated kmax) — deseasonalised intraday futures returns exhibit
all four of the departures above simultaneously (intraday periodicity is a
deterministic volatility path; microstructure noise is autocorrelated; jumps are
present; drift is not negligible at short horizons). No published size figure in
this corpus transfers. **TC-1 must be two-sided, not one-sided.** The rationale
cannot be "size is distorted upward, so measure how far upward": under a
deterministic drift break the corpus's own evidence (`eru-0348`) has size going
to 1 *or* to 0 with the break sign, so TC-1 measures the empirical rejection
frequency against the nominal level in both directions and reports the sign of
the drift/level configuration that produced it. *(Finding QUANT-1-5.)*

### 7.2 O2 — power, and the periodically-collapsing alternative

**Coverage, over the assessable denominator.** Q3 and Q4 are answerable for 65
of the 72 records — 4 have no full text at any stage and 3 are twins appraised
under their carriers. Power under explicitly parameterised explosive
alternatives is reported in **52 of 65 assessable records (80%)**. Power under
an alternative with a *collapse mechanism* is reported in **15 of 65 (23%)**,
partially in 8, and not at all in 41. This is the single largest coverage
asymmetry in the corpus: most evaluations test detection of a bubble that never
bursts. *(Finding REV-1-4; the record-set denominator 72 is not used here
because 7 records cannot contribute a numerator by construction.)*

**The Evans-type result the corpus is built around.** The comparison line's
Evans-DGP power table is the corpus's clearest statement of what collapse does to
this literature's tests (order supDF / supDFC / supK / supBT / supB, T = 100,
5% level, Evans bubble scaled ×20, α=1, δ=0.5, τ=0.05, R=0.05):

| π (bubble survival probability) | supDF | supDFC | supK | supBT | supB |
|---|---|---|---|---|---|
| 0.999 | 0.902 | 0.899 | 0.043 | 0.931 | 0.290 |
| 0.85 | 0.624 | 0.072 | 0.330 | 0.073 | 0.042 |
| 0.25 | 0.253 | 0.023 | 0.210 | 0.021 | 0.033 |

Source: `eru-0150` Table 5, Homm & Breitung working paper (§5.4 version caveat).
The reading the source itself gives: break-type tests (supDFC, supBT, supB) lose
power against periodically collapsing bubbles when collapses occur late in the
sample — rejection below 10% at π = 0.85 — while the recursive supDF degrades far
more gracefully. This is the empirical content of the Evans (1991) critique
carried forward, and it is the reason the recursive family displaced the
Chow-type line for this problem.

PWY report the corresponding inconsistency analytically and by simulation for
their own statistic (`eru-0131` Table 4 p.221 and the Appendix **pp.222–224**), and PSY
2015a make Evans-type collapse a core power DGP with a survival-probability grid
(`eru-0393` Tables 4–5), where the declared contribution includes demonstrating
that PWY's own SADF is inconsistent in multi-bubble samples — an originator team
publishing the failure of its predecessor.

**Documented power deficits of the family, third-party.**

| finding | reported magnitude | source |
|---|---|---|
| aggregation attenuates SADF/GSADF power (index vs constituents) | primary declared outcome; power deficiency across monthly US metro and quarterly international house-price designs | `eru-0675`/`eru-0622`, [Pavlidis, Martínez-García & Grossman 2018](https://doi.org/10.1016/j.econmod.2018.07.021) |
| GSADF power deficit against a rolling IVX comparator on spot–forward differentials | substantial across DGPs | `eru-0607`, [Pavlidis, Paya & Peel 2017](https://doi.org/10.1111/iere.12249) |
| single-series family tests have low power for short-lived / slow bubbles (motivating panel clustering) | stated as the paper's motivation, with panel remedy | `eru-1405`, [Liu, Phillips & Yu 2023](https://doi.org/10.1111/iere.12647) |
| SADF/GSADF power deficiency under a stochastically varying explosive coefficient | primary declared outcome | `eru-1715`, [Kurozumi & Nishi 2025](https://doi.org/10.1111/jtsa.12768) — single-pass, intermediary-mediated (§5.4) |
| SADF/GSADF power and size deficiencies against quantile-autoregression alternatives | primary declared outcome | `eru-1604`, [Pavlidis 2025](https://doi.org/10.1111/jtsa.12794) |
| very low power at very short samples (T = 20) even with a design-specific simulation | size 0.059, break dates "detected very imprecisely" | `eru-0597`, [Kholodilin, Michelsen & Ulbricht 2018](https://doi.org/10.1007/s00181-017-1347-x) |

**Synthesis claim (O2).** Power results in this corpus are not comparable across
studies: the DGPs differ (linear non-collapsing, Evans periodically collapsing,
randomly starting, four-regime local-to-unity, random-coefficient, noncausal MAR),
the collapse mechanism differs (stochastic Evans collapse vs sharp
re-initialisation vs mildly-integrated collapse), and the localising rate differs
(fixed ρ, ρ = 1+c/T, ρ = 1+c/T^α). The corpus supports one robust qualitative
statement — *break-type and recursive tests rank differently under collapsing
versus non-collapsing alternatives, and the ranking reverses with the collapse
probability* — and no quantitative pooling (§7.7).

**Recall bound at the point of claim (finding REV-2-6).** "Not comparable across
studies" is a property of *this corpus's* power studies. The corpus lost 47.8%
of its full-text-stage records (L-4, VG-2) and its backward-chase arm ran only
after freeze, naming `er-bc-1` (Hall, Psaradakis & Sola 1999) — a
Markov-switching simulation study of periodically collapsing bubbles, i.e.
directly on this characteristic — which was not admitted (A11, L-5, VG-4). A
comparable pair on the Evans-collapse alternative may exist outside this corpus.

### 7.3 O3 — date-stamping accuracy and detection delay

**Coverage, over the assessable denominator.** Q5 is answerable for 65 of the
72 records (4 no full text, 3 twins). Dating accuracy or delay is reported in
**23 of 65 assessable records (35%)**, partially in 2, and not at all in 40.
Under the frozen Q→D rule, D4 concern is raised for 42 of 65; as recorded by
the extractor it is high for 41 and low for 23 (§6.1). Restated bluntly:
**most of this literature evaluates detection, not dating**, including many
papers whose stated contribution is a dating procedure. *(Finding REV-1-4.)*

**The family's own dating numbers** (mean estimate, SD in parentheses, in
sample-fraction units unless noted):

| quantity | reported value | design | source |
|---|---|---|---|
| PSY origination r̂ₑ (true 0.40) | 0.45 (0.03) | single bubble, α = 0.6, finite-sample 95% quantiles, 5,000 reps | `eru-0395` Tables 1–10, [PSY 2015b](https://doi.org/10.1111/iere.12131) |
| PSY termination r̂_f (true 0.55) | 0.55 (0.01) | same | `eru-0395` |
| PWY origination r̂ₑ (true 0.40) | 0.46 (0.03) | same | `eru-0395` |
| PWY termination r̂_f (true 0.55) | 0.55 (0.01) | same | `eru-0395` |
| PS reverse-regression origination bias | +0.07 (0.04), i.e. a seven-observation delay at T = 100 | Table 1, invariant across η and DGP | `eru-0559`, [Phillips & Shi 2018](https://doi.org/10.1017/S0266466617000202) |
| PS reverse-regression collapse-date bias, by collapse type | sudden −0.00 (0.01); disturbing +0.02 (0.01); smooth +0.09 (0.04) | Table 2 | `eru-0559` |
| PSY crash-origination bias (Phillips & Shi 2019 SDR) | 0.20 (0.11) at r_c = 0.6 falling to 0.06 (0.03) at r_c = 0.9 | Table 1 | `eru-0823`, [Phillips & Shi 2019](https://doi.org/10.1111/obes.12307) |
| PSY **mean bias in the estimated origination date**, standard per-observation CVs | 7.56 months (4.99), **at successful-detection rate 0.84** | monthly, T = 120, 10-year span, M = 2,000 | `eru-1289` **Table 2 p.21**, [Shi & Phillips 2022](https://doi.org/10.1017/9781108910095.003) — **WORKING-PAPER tier** (§7.4 tier correction, L-10, VG-6) |
| PSY **mean bias in the estimated collapse date**, standard CVs | 0.79 months (1.72) | same | `eru-1289` **Table 2 p.21** — **WORKING-PAPER tier** |
| PSY mean bias in the estimated origination date, FWER-controlled (simulated max-PSY critical values, control window T_w = T) | 12.20 months (5.33), **at successful-detection rate 0.75** | same | `eru-1289` **Table 2 p.21** — **WORKING-PAPER tier** |
| PSY mean bias in the estimated collapse date, FWER-controlled | 0.77 months (**1.71**) | same | `eru-1289` **Table 2 p.21** — **WORKING-PAPER tier** |
| common-factor PSY dating bias (large-N) | τ̂_c bias 0.007 of sample at N = 100, T = 60, rising to 0.17 with few assets and long spans | Figure 3 | `eru-1112`, [Chen, Phillips & Shi 2022](https://doi.org/10.1093/jjfinec/nbab027) |

**The single most consumer-relevant number in the corpus** is the
`eru-1289` pair, and it is **working-paper-tier evidence** (`eru-1289` = Cowles
DP 2331 (2022); the 2025 CUP chapter its DOI resolves to was never obtained —
§7.4 tier correction, L-10, VG-6). Controlling the family-wise error rate of the
PSY dating recursion **increases the mean bias in the estimated origination date
from 7.56 to 12.20 months while the successful-detection rate falls from 0.84 to
0.75** (DP 2331 **Table 2, p.21** — not Table 1, which is the FWER triple on
p.20); the mean bias in the estimated collapse date is essentially unchanged
(0.79 → 0.77). Both are the paper's averaged signed error
`(1/M)Σ(t̂⁽ᵐ⁾ − t)` in months: its Table 2 caption calls the quantity a *bias*
and its §5.2 text calls it an *averaged delay*, and they are the same statistic
under two names. This review says "mean bias in the estimated date" at every site
so that the paired detection-rate cost is not dropped, which is what the earlier
label "origination delay" did. The multiplicity fix is not free; it is paid
**twice** — in dating bias and in successful-detection rate — and asymmetrically
between origination and collapse. Any branch-3 specification that adopts
FWER-controlled PSY dating inherits both costs explicitly.
*(Findings REV-3-3, QUANT-3-3; re-read against DP 2331 on 2026-09-02, L-19.)*

**Third-party dating evaluations.**

| finding | source |
|---|---|
| break-date estimators compared: τ̂_P1 (pointwise-CV first crossing) downward-biased with the largest SD; τ̂_P2 (5% supDF CV first crossing) late-biased; τ̂_K roughly 10% of sample late; all poor at T = 200; τ̂_DFC most reliable at T = 400 | `eru-0150` Table 6, Homm & Breitung WP |
| accuracy of PSY start/end dates measured as the frequency of falling within k ∈ {0,1,5} observations of truth, conditional on PSY rejection; proposes improved estimators | `eru-0463`, [Harvey, Leybourne & Sollis 2017](https://doi.org/10.1016/j.jempfin.2016.11.001) (single-pass, §5.4) |
| PSY dating fragments multi-regime episodes; two-step PSY-window + BIC dating compared by histogram | `eru-0959`, [Harvey, Leybourne & Whitehouse 2020](https://doi.org/10.1016/j.jempfin.2020.06.004) (single-pass) |
| Bayesian filtered-probability dating: per-period false-flag rate 0.018 versus PSY's 0.057 under the true regime-switching DGP; PSY criticised for episode fragmentation | `eru-0526`, [Fulop & Yu 2017](https://doi.org/10.3390/econometrics5040047) |
| date-stamping delay under serially correlated innovations, with episode screens (minimum duration log T) | `eru-1049` Table 7 |
| confidence *sets* for emergence, collapse and recovery dates by inverting location tests; break-order misidentification 16% / 27% / 19% for small/medium/large magnitudes | `eru-1920`, [Kurozumi & Skrobotov 2026](https://doi.org/10.1080/07474938.2026.2700653) |
| SV-robust date-stamping: separate diverging thresholds log(ns)/10 (origination) and log(ns)/2 (collapse); lower MSE than PWY across configurations | `eru-1950`, [Sarkar & Wells 2026](https://doi.org/10.3934/fmf.2026005) |

**Synthesis claim (O3).** Origination is dated late and with material dispersion;
termination is dated more accurately than origination in every design in the
corpus that reports both (`eru-0395`, `eru-0559`, `eru-1289`). The asymmetry is
structural, not incidental: origination requires the recursive statistic to
*accumulate* enough explosive evidence to cross a diverging threshold, whereas
collapse produces a rapid divergence of the statistic in the opposite direction.
Evidence tier: peer-reviewed **except the four `eru-1289` rows, which are
WORKING-PAPER tier** — the 2025 CUP chapter carrying that record's DOI was never
obtained, and the text this review extracted and re-read is Cowles DP 2331 (2022)
(§7.4 tier correction, L-10, VG-6). Under the charter rule that the tier travels
with the claim, §7.3 is a site it must reach: four of the thirteen rows above are
`eru-1289`, and this section calls that pair the single most consumer-relevant
number in the corpus. The earlier form of this line said "peer-reviewed
throughout", which contradicted the correction. *(Finding REV-3-4.)* Concern
profile (**convention-resolved, not source-adjudicated** — §6 header, A6): the
sources of these numbers are precisely the minority with D4 low. Causality
status: `eru-0395` and `eru-1289` are O6=RT and CS respectively — the `eru-1289`
dating-bias figures are measured on a causal statistic in a pseudo-real-time
monitoring illustration.

`TO COMPUTE` handoff **TC-2**: **the mean bias in the estimated origination
date, its dispersion, and the successful-detection rate that goes with it** for
the chosen detector at branch-3-relevant sampling frequency and episode duration.
The three must be reported together — DP 2331's own trade-off is only visible
when they are (§7.4, L-19). Every dating-error number above is monthly or in
sample fractions at T ≤ 400; none transfers to an intraday setting where an
episode may span a few hundred bars.

### 7.4 O4 — false-alarm behaviour across the recursive sequence

**Coverage, over the assessable denominator.** Q7 is answerable for 65 of the
72 records (4 no full text, 3 twins). Multiplicity across the recursive sequence
is addressed in **19 of 65 assessable records (29%)**, partially in 1, unclear
in 6, not addressed in 39. Under the frozen Q→D rule, D6 concern is raised for
46 of 65; as recorded by the extractor it is high for 33, unclear for 12 and low
for 20 (§6.1). *(Finding REV-1-4.)*

**How the family handles multiplicity.** Asymptotically, and by construction: the
critical-value sequence is made to diverge (α_n → 0), so the probability of any
false origination detection vanishes as n → ∞. PWY state the condition as
eq. (13) with the operational rule cv_adf(s) = log(log(ns))/100 (`eru-0131`
p.210, p.207); PSY 2015b give the rate conditions cv_T → ∞ and cv_T/T^{1−α/2} → 0
under which the crossing-time estimators are consistent (`eru-0395` Theorems 2–3,
8). In finite samples with α fixed at 0.05 — which is what every application does
— that control is not in force.

**The one direct finite-sample measurement in the corpus.**

| quantity | reported value | source |
|---|---|---|
| FWER of the PSY dating recursion over a 10-year span, standard per-observation 95% CVs | **0.55** (T = 40, quarterly) | `eru-1289` Table 1 p.20, [Shi & Phillips 2022](https://doi.org/10.1017/9781108910095.003) |
| same 10-year span, higher sampling frequency | **0.78** (T = 120, monthly), rising to **0.93** (T = 520, weekly) | `eru-1289` Table 1 p.20 |
| cost of the multiple-testing critical values, paid in dating accuracy and detection rate rather than in delay-to-detection | mean bias in the estimated origination date 7.56 (4.99) → 12.20 (5.33) months, **at successful-detection rate 0.84 → 0.75**; mean bias in the estimated collapse date 0.79 (1.72) → 0.77 (1.71) (§7.3) | `eru-1289` Table 2 p.21 |

This is an originator-team paper quantifying its own procedure's multiplicity
defect, and it is the corpus's most important O4 datum: **used as conventionally
applied, the PSY date-stamping recursion has a family-wise false-detection
probability between roughly one-half and nine-tenths over a decade of data — on
working-paper-tier evidence.**

> **Tier correction, and it travels with the claim (finding LITERATURE-1-2).**
> `eru-1289` was tiered "peer-reviewed chapter" on the strength of its DOI
> [10.1017/9781108910095.003](https://doi.org/10.1017/9781108910095.003). That
> DOI resolves (Crossref, checked 2026-09-02) to a chapter in *Financial
> Econometrics: Theory and Applications*, Cambridge University Press, **2025**,
> pp. 30–59. The text this review actually extracted is **Cowles Foundation
> Discussion Paper 2331 (2022)**, the working-paper twin. The chapter was never
> obtained, so the peer-reviewed tier was taken from a version that was not
> read, and the record's stated year (2022) is the working paper's, not the
> DOI's. **The FWER triple 0.55 / 0.78 / 0.93 is therefore tiered
> WORKING-PAPER**, not peer-reviewed chapter, wherever it is used — here, in
> the abstract's principal finding (4), in §7.8, and in §14's inputs to the
> consumer agenda. `eru-1289` is added to L-10 (version caveats) and VG-6 as a
> **fourth** working-paper-extraction case. Under the charter rule that tier
> travels with the claim, no consumer may treat the FWER measurement as settled
> peer-reviewed evidence; it is the corpus's only direct finite-sample
> multiplicity measurement *and* it is working-paper tier, and both facts must
> be carried together.

Concern profile for this record, **convention-resolved and not
source-adjudicated** (§6 header, A6), read off §6's row 68 and corrected — the
earlier form of this sentence said "D4 low", which its own appraisal row
contradicts: D6 recorded `low` and rule-derived `low`; **D4 recorded `high`
where the rule derives `low`** (marked `¶`, because Q5 is `yes`); D7 recorded
`high` and rule-derived raised.

**The surveillance line, which controls false alarms by design.** The competitor
literature the protocol brought in under §2.1 treats false-alarm rate as the
primary design object rather than an afterthought:

| procedure | false-alarm control mechanism | reported behaviour | source |
|---|---|---|---|
| MAX_m / SEQ_m end-of-sample monitors | closed-form FPR for any monitoring horizon, invertible to fix the FPR ex ante | theoretical FPR available in closed form (eq. 5), monotonically increasing in horizon | `eru-0735`, [Astill et al. 2018](https://doi.org/10.1111/jtsa.12409) |
| CUSUM vs volatility-standardised CUSUMV | boundary constants calibrated so FPR matches MAX10's 0.10 under homoskedasticity (b = 0.147 / 0.177) | standard CUSUM's null limit depends on the volatility path and its FPR fails under time-varying volatility; CUSUMV restores it | `eru-1117`, [Astill et al. 2021](https://doi.org/10.1093/jjfinec/nbab009) |
| covariate-augmented CUSUM monitors | Chu–Stinchcombe–White crossing function, FPR calibrated to 0.10 by t = 241 (b = 0.1395 standard, 0.1679 volatility-corrected) | FPR retained under time-varying volatility | `eru-1921`, [Astill, Taylor & Zu 2026](https://doi.org/10.1017/S0266466626100383) |
| two-stage bubble-then-crash monitor AMAX(k) → SMIN(m,n) | AMAX carries the AHLST closed-form FPR; the crash monitor's FPR has **no closed form** and is *bounded* rather than derived | SMIN(m,n) runs only after AMAX(k) has signalled, so under H₀ its FPR is bounded by AMAX(k)'s FPR at the false-detection time and under H₁,₁ by AMAX(k)'s true-positive rate there; the authors state further theoretical analysis "is not possible" and measure it by simulation. **The earlier cell read "crash monitor never signals before the crash by construction", which the source contradicts — corrected round 4, L-21** | `eru-1519`, [Whitehouse, Harvey & Leybourne 2023](https://doi.org/10.1111/obes.12540) |
| recursive-mean/trend-adjusted AMAX (MR, TR) | same closed-form FPR (Theorem 1: modifications do not raise false detection) | detection accelerated shortly after onset at unchanged FPR | `eru-1844`, [Whitehouse, Harvey & Leybourne 2025](https://doi.org/10.1016/j.ijforecast.2024.12.005) |
| CUSUM detectors with weighted boundaries — **one open-ended, one closed-ended** | `eru-1038` (open-ended): boundary **g(M,s) = c·M^{1/2}(1 + s/M)(s/(M+s))^γ**, eq. (2.8), with c = c(γ, α) chosen so that lim_{M→∞} P{τ_M < ∞} = α under H₀ over an unterminated horizon. `eru-0889` (**closed-ended, in its own words**: "we consider here closed-ended procedures in which we stop the detection procedure after observing T observations"): boundary g_M(k) = c(1 + d₀M^{−τ})M^{1/2}(1 + k/M)·f(k/(k+M)), with the limiting crossing probability taken at θ = lim T/(T+M) | γ trades detection speed against false alarms, but **the two papers choose differently**: `eru-0889` — "As a compromise, we use γ = 0.35 in the empirical study"; `eru-1038` — "we recommend γ = .45 to achieve fast and reliable detection". **The earlier cell dropped the c·M^{1/2} factor from the boundary, called both procedures open-ended, and attributed γ = 0.35 to both — corrected round 4, L-21** | `eru-0889`, [Horváth et al. 2020](https://doi.org/10.1016/j.jeconom.2019.08.010); `eru-1038`, [Horváth, Liu & Lu 2020](https://doi.org/10.2139/ssrn.3529058) |
| weighted-CUSUM / Page-CUSUM on RCA residuals | Darling–Erdős boundary asymptotics; procedure-wise size controlled over open- and closed-ended monitoring | valid irrespective of stationarity of the observed process | `eru-1845`, [Horváth & Trapani 2025](https://doi.org/10.1017/S0266466625000052) |
| sequential detector statistics (LBI, point-optimal, wCUSUM) | constant vs time-varying boundaries with simulated constants controlling sequence-wise crossing probability | argmax dating avoids the systematic small-sample delay of boundary-crossing dating | `eru-1852`, [Breitung & Diegel 2025](https://doi.org/10.1111/jtsa.12845) |

**Synthesis claim (O4), and it is the review's sharpest — restated
corpus-scoped.** *Within this corpus, the recursive right-tailed family and the
surveillance family answer different questions about false alarms.* **No record
in this corpus reports a detection-delay-versus-ARL₀ characterisation for the
recursive right-tailed family.** What the corpus does report for that family is
asymptotic type-I control through a diverging critical-value sequence, plus one
finite-sample family-wise measurement at fixed α — FWER 0.55–0.93 over a decade
(`eru-1289`, **working-paper tier**, see the tier correction above).
**Nine records in this corpus** (`eru-0735`, `eru-1117`, `eru-1519`, `eru-1844`,
`eru-1845`, `eru-0889`, `eru-1038`, `eru-1921`, `eru-1852`) report a
false-positive rate over a stated monitoring horizon in closed form. For a
consumer whose comparison metric is detection delay against a stated ARL₀ —
which is branch 3's declared metric — **the surveillance line is the line in
this corpus that publishes a quantity of the required kind, and the recursive
family is not represented in this corpus by any record that does.**

**Recall bound attached at the point of the claim, not deferred to §12.1
(finding REV-1-13).** This is a statement about *this corpus's coverage*, not a
universal negative about the literature. The corpus that supports it excluded
280 records — 47.8% of everything reaching full text — solely because the text
could not be obtained, with unknown direction (L-4, VG-2); ran the protocol's
backward citation-chasing arm only as a post-freeze diagnostic over 22 of 27
carriers' *deposited* reference lists (A11, L-5, VG-4); and failed the known-item
recall check on three pre-2011 antecedents (§2.3). The review's own reading
rule applies to this claim as to every other: **a count of records is a fact
about *this corpus's* coverage, never about the literature and never about a
detector** (§7 header, as corrected under REV-2-5). A
delay-versus-ARL₀ result for the recursive family may exist outside this corpus;
nothing here bounds that possibility. The correctly-scoped O5 claim ("no record
in the corpus evaluates a detector under more than two departures
simultaneously") is the template this claim now follows.

Evidence tier: peer-reviewed throughout the surveillance table; `eru-1921` is a
2026 online-first article; the recursive family's single FWER datum is
working-paper tier. Concern profile, **convention-resolved and not
source-adjudicated** (§6 header, A6): D6 is recorded `low` for every one of the
nine surveillance records, and the frozen Q→D rule derives `low` for all nine
too — this is one of the places where the two columns of §6 agree cell for
cell.

`TO COMPUTE` handoff **TC-3**: ARL₀ and conditional detection delay for the
chosen detector on deseasonalised intraday futures. The corpus publishes FPR over
a *fixed monitoring horizon*, not ARL₀; the two are related but not
interchangeable, and no record in the corpus reports ARL₀ under that name.

### 7.5 O5 — validity conditions

The validity conditions the corpus states, grouped by what they constrain. Every
row is extracted from a full text; the source column names the record whose text
states the condition.

| what is assumed | as stated | records |
|---|---|---|
| **null process** | martingale / unit root with drift d·T^{−η}, η > 1/2 ("asymptotically negligible drift") | `eru-0393`, `eru-0238`, `eru-0427`, `eru-1031` |
| | the asymptotic SADF distribution is **discontinuous at η = 0.5**: a PWY-type Wiener functional for η > 0.5, a standard-normal-type functional dominated by the deterministic trend for 0 ≤ η < 0.5, with the boundary case depending on nuisance parameters | `eru-0238`, [PSY 2014](https://doi.org/10.1111/obes.12026) |
| **errors** | iid (0, σ²) in the base theory; extensible to weakly dependent errors via linear-process assumptions with summable coefficients and finite fourth moments | `eru-0131`, `eru-0395`, `eru-0463`, `eru-0559` |
| | conditional heteroskedasticity permitted without correction in the end-of-sample/subsampling designs (stationary and ergodic innovations suffice) | `eru-0609`, `eru-1844` |
| | ARMA innovations require a sieve bootstrap with sieve order q ≥ ADF lag k; k > q re-creates the oversizing | `eru-1049` |
| | long memory d ∈ (0, 1/2) invalidates the standard CVs; a HAR (fixed-b) standardisation with ELW-estimated d restores them | `eru-1526`, `eru-0691` |
| **volatility** | unconditional volatility must be constant; the Cavaliere–Taylor class σ_t = ω(t/T), non-stochastic, strictly positive, càdlàg, breaks the pivotal null limit | `eru-0503`, `eru-0748`, `eru-0891`, `eru-1384`, `eru-1580` |
| | remedies published: wild bootstrap (`eru-0503`), sign transformation (`eru-0891`), WLS by kernel spot-variance (`eru-0748`, `eru-1580`), time deformation to integrated-variance time (`eru-1384`), realised-volatility devolatisation (`eru-1716`) | |
| | stochastic, *persistent* volatility (nearly nonstationary SV) requires its own double-local-to-unity limit theory; OLS limits are N(0, 2c) in the nearly-stationary case and Cauchy in the mildly explosive case, robust to the SV specification | `eru-1929` (**preprint tier**), `eru-1950` |
| **deterministic terms** | a drift break under the null makes DF_μ diverge (size → 1 or 0) | `eru-0348` |
| | a polynomial trend of order m ≥ 2 makes AR(1)-based GSADF/BSADF false detection tend to one; an AR(2)-based statistic is claimed consistent | `eru-1260` |
| | deterministic level shifts identified as a further validity condition — **abstract-level pointer only, full text not obtained** | `eru-1890` (§5.4) |
| **jumps** | jump terms enter the in-fill limit distributions; ignoring them distorts size up to 0.397; remedy is jump dummies | `eru-0924` |
| **alternative** | mildly explosive ρ = 1 + c/k_n, k_n → ∞, k_n = o(n), in the [Phillips & Magdalinos 2007](https://doi.org/10.1016/j.jeconom.2005.08.002) moderate-deviations sense; x₀ = o_p(√k_n); no intercept in the explosive DGP, to avoid a deterministically explosive component | `eru-0131`, `eru-0100`, `eru-0126` |
| | PSY-type four-regime model with collapse by re-initialisation to the pre-bubble level plus O_p(1) | `eru-0395`, `eru-0503`, `eru-1580` |
| | PWY's own detector is **inconsistent** for a second bubble in a multi-bubble sample: DF diverges to −∞ until the in-recursion second bubble dominates | `eru-0395` **Theorems 4–5 pp.1086–1087** (the DF/BSDF limit behaviour) and **Theorems 6–7 p.1088** (the inconsistency itself — Theorem 6: "r̂₂ₑ and r̂₂_f are not consistent estimators of r₂ₑ and r₂_f"; Theorem 7: r̂₂ₑ →ₚ r₂ₑ + r₁_f − r₁ₑ, i.e. biased by the first bubble's duration). The earlier form cited Theorems 4–5 for both; corrected round 4, L-21 |
| **minimum window r₀** | PWY: r₀ = 0.10 — **convention, no derivation stated** | `eru-0131` Table 1 note p.213 |
| | PSY: r₀ = 0.01 + 1.8/√T — stated as an empirical rule from "extensive simulation"; **CONVENTION, not derived** | `eru-0393` |
| | minimum episode duration δ·log(T) with frequency-dependent δ, which PSY themselves call "inevitably arbitrary" | `eru-0393` fn.10 p.1052 |
| | monitoring window m: trade-off documented (smaller m detects faster, larger m gives higher eventual power); m = 10 recommended | `eru-0735`, `eru-1844` |
| **sample-size regime** | bubble duration must be a non-vanishing fraction of the sample for PSY-type validity; the end-of-sample designs instead take T → ∞ with the bubble length m finite | `eru-0609` |

**Synthesis claim (O5).** The family's stated null is narrow and its published
robustness is a patch-set: each departure has a named remedy, each remedy is
published by a small number of teams, and **no record in the corpus evaluates a
detector under more than two departures simultaneously.** The consumer's setting
presents at least four at once (§7.1, TC-1). The tuning constants r₀ and the
minimum-duration δ·log(T) are `CONVENTION` in the family's own words — PWY state
r₀ = 0.10 with no derivation, PSY call the duration rule "inevitably arbitrary" —
so any branch-3 specification that adopts them adopts an unlabelled constant
unless it re-derives them, which is `TO COMPUTE` handoff **TC-4**.

### 7.6 O6 — causality status of each published characteristic

This is the domain the consumer agenda's standing hazard turns on, and the review's
finding is a distribution, not a single verdict:

| O6 code | records (n = 72) | distinct works (n = 69) | reading |
|---|---|---|---|
| **RT** | 22 | 22 | the reported characteristic is measured on a genuinely real-time procedure |
| **CS** | 19 | 17 | the statistic is causal but the reported characteristic is measured ex post, or its critical values condition on the whole sample |
| **FS** | 22 | 21 | full-sample statistic; no time-*t* claim attaches |
| **SPLIT** | 3 | 3 | the record's own text attributes real-time status to one statistic and ex-post status to another (`eru-0131`, `eru-0393`, `eru-0559`) |
| **NS** | 2 | 2 | causality status not stated in the extracted text (`eru-1405`, `eru-1715`) |
| **NE** | 4 | 4 | no full text (§5.4) |

**The two columns differ because three records are the same works as three
others.** `eru-0154` (CS) and `eru-0904` (CS) are working-paper twins of
`eru-0126` and `eru-1526`; `eru-0622` (FS) is the working-paper twin of
`eru-0675` (§5.3, A10(b)). Their O6 codes are inherited from the carriers, so the
record column counts those three works twice. §5.3's assurance that "no
operating characteristic is double-counted" is true of §7's *evidence tables*,
which cite the carrier, and was **not** true of this distribution as previously
reported. *(Finding REV-2-3.)*

**The O6 assessable denominator, fixed here and used at every site.** Coverage
fractions on O6 are stated over **63 distinct works** = 69 distinct works − 4 NE
(no full text at any stage, so no status could be extracted) − 2 NS (a full text
was read and does not state a causality status). The three same-work twins are
already excluded by using the distinct-work column, exactly as §6.1 excludes them
from every Q-cell denominator. The partition over 63 is RT 22 + FS 21 + CS 17 +
SPLIT 3. This replaces the two mutually inconsistent denominators the earlier
form of this review used at the two O6 sites — 72 in the abstract and 65 here,
the latter imported from the Q1–Q7 assessable denominator where it does not
apply. *(Findings REV-2-2, SCOPE-2-4, QUANT-2-2.)*

**Three specific causality traps documented inside the corpus, each in the source's
own words.**

1. **The sup statistic is not a date-stamper.** PWY: "However, sup_{r∈[r₀,1]} ADF_r
   cannot reveal the location of the exuberance" (`eru-0131`, *IER* 52:**214**). PSY:
   "the new date-stamping strategy may be used as an ex ante real-time dating
   procedure, whereas the GSADF test is an ex post statistic used for analyzing a
   given data set for bubble behavior" (`eru-0393`, *IER* 56:**1053**). Any claim that
   "SADF/GSADF date-stamps in real time" is contradicted by both originating
   papers.
2. **Reverse regression is not forward-causal.** Phillips & Shi's implosion-dating
   extension runs recursions on time-reversed data, so recovery-date estimation
   conditions on post-collapse observations. The forward BSDF sequence is causal;
   the reverse-sample statistic is not (`eru-0559`).
3. **A causal statistic with full-sample critical values is not real-time.** The
   `psymonitor` composite bootstrap estimates the null model "using the full sample
   period" (`eru-1031`), so the statistic is causal while its critical values are
   not. `eru-1921` makes the same observation about wild-bootstrap PSY monitors
   from outside the originator line. A record can be CS on this ground alone.

**Synthesis claim (O6).** Of the **63 distinct works that carry an extracted
causality status** (69 distinct works, less 4 with no full text and 2 whose text
does not state one), **22 — 35%, just over one in three — publish a
characteristic measured on a genuinely real-time procedure**, and the ones that
do are concentrated in the surveillance / monitoring line rather than in the
recursive right-tailed family. The earlier form of this sentence said "fewer
than one in three" over a denominator of 65; that was false at 65 (22/65 =
33.8%), is false at 63 (34.9%) and is false at 66 (33.3%, exactly one in three).
It is true only over the full 72-record partition (22/72 = 30.6%), which is a
different quantity — it divides by four records that were never read and by three
twins. The corpus-scoped reading rule of §7 applies: this is a count of works in
*this corpus*, bounded by the 47.8% X6 loss (L-4) and the post-freeze
backward-chase arm (A11, L-5). The family's
real-time claim is a claim about the *statistic's construction*; the family's
published operating characteristics are, with the notable exception of `eru-0395`,
about ex-post performance.

### 7.7 Meta-analysis condition (item 13, protocol §7 15c) — failed, characteristic by characteristic

The pooling condition required ≥2 studies from **non-overlapping author teams**
reporting the **same characteristic** for the **same detector** under the **same
DGP family** with **matched T and r₀**. Evaluated per characteristic:

| characteristic | why pooling fails |
|---|---|
| empirical size of SADF at 5% | `eru-0393` (T = 100–1600, asymptotic CVs, k = 0, r₀ = 0.01+1.8/√T) and `eru-1044` (same T range, same CV type) are the closest pair and *are* non-overlapping teams — but `eru-1044`'s null adds a TGARCH branch and its homoskedastic arm uses a different replication count and a different lag convention; the r₀ rule matches, the error DGP does not. No matched cell. |
| empirical size of GSADF at 5% | same pair, same failure; additionally `eru-0813`'s GSADF size is measured as a "pseudo-size" bubble-detection rate under four different no-bubble processes, which is not the same quantity |
| power under Evans-type collapse | `eru-0150` (T = 100, bubble scaled ×20, π grid) and `eru-0131` (**T = 100**, **bubble scaled ×20** — Pₜ = Pᶠₜ + 20Bₜ — π grid, α = 1, ζ = 0.5, τ = 0.05, g = 0.05; Table 4 note p.221) are non-overlapping teams reporting the same DGP family. **Corrected round 4 (L-21): the earlier text gave `eru-0131` as `n = 120` with "different scaling" and rested the no-match verdict on "different scaling, different sample size". Both grounds are withdrawn on the PWY side — n = 120 is PWY's Table 3, the *non-collapsing* power design, not its Evans table, and the ×20 scaling is the same one this row attributes to `eru-0150`.** What survives is **different tests** (ADF₁ and supᵣ ADFᵣ versus supDF/supDFC/supK/supBT/supB). Whether the remaining cells match cannot be settled here: `eru-0150`'s own text was **not obtained on this pass either** (§5.4, L-21), so its T, scaling and calibration are known only as transcribed at extraction. No matched cell is asserted, and none is ruled out. |
| origination date bias | `eru-0395` (fractions, T = 100–400, α = 0.6 localising rate) and `eru-1289` (months, 10-year span, quarterly/monthly) are overlapping teams *and* incommensurable units. `eru-0150`'s τ̂ estimators are different estimators entirely. |
| detection delay | reported in months (`eru-1289`), in sample fractions (`eru-0559`), as histograms without tabulated moments (`eru-0959`, `eru-1844`), and as TPR-versus-horizon curves (`eru-0735`, `eru-1117`). No two studies report the same summary of the same quantity. |
| FWER / FPR | `eru-1289` reports FWER of a dating recursion over a calendar span; the surveillance line reports FPR over a monitoring horizon calibrated to a target. Different estimands. |

**Outcome: structured no-meta-analysis — the PRE-REGISTERED EXPECTATION
CONFIRMED, not a finding.** Protocol §7 15c set the pooling condition and stated
in advance that it was unlikely to be met; recording its failure discharges the
pre-registration, and calling it a "finding" overstates what a confirmed prior
expectation delivers. The failure is systematic rather than incidental within
this corpus — these Monte Carlo designs are chosen to display each new method's
contribution, not to be commensurable with predecessors.

**Corpus-scoped on the §7.4 / O5 template, with the recall bound at the point of
claim.** What is established is that **no two records in the frozen 72-record
set** meet the matched detector × DGP × T × r₀ condition across non-overlapping
teams. That is a statement about this corpus, not about the state of the
evidence: the corpus lost 47.8% of its full-text-stage records to
unobtainability with unknown direction, and **L-4 concedes explicitly that the
pooling condition "could in principle be met by a pair inside the X6 set"**. The
same concession is now made for the post-freeze backward-chase arm, which L-5
did not previously extend to it: **`er-bc-1` (Hall, Psaradakis & Sola 1999) is a
simulation study of periodically collapsing bubbles by a team non-overlapping
with `eru-0150` and `eru-0131`**, i.e. exactly the configuration whose absence
the Evans-collapse power row rests on, and it was named by the A11 diagnostic
and not admitted. Its admission could in principle supply the non-overlapping
second arm on that characteristic. A pooled cell may therefore exist outside this
corpus; nothing here bounds that possibility. *(Findings REV-2-6, REV-1-13.)*

### 7.8 Per-detector summary — what is known, under which conditions, at which causality status

**Read the last column with the §6 caveat attached.** The "concern flags" are
ER-RoB v1 domain concerns as recorded by the primary extractor and resolved by
the §2.8 convention — **convention-resolved, not source-adjudicated** (§6
header, A6, L-2) — and they are the extractor's recorded judgments rather than
the frozen Q→D rule's output, which differs in 44 of the corpus's domain cells
(A8, §6.1). No flag here may be cited as an adjudicated appraisal.
**Read the table as corpus-scoped throughout**: "what is published" means what
is published *in this corpus*, which lost 47.8% of its full-text-stage records
to unobtainability (L-4) and whose backward-chase arm ran only as a post-freeze
diagnostic that already named one probable miss (L-5, A11). A detector line may
be missing from this table entirely. *(Findings SCOPE-1-3, REV-1-13.)*

| detector | what is published *in this corpus* | validity conditions | causality status | on whose evidence | concern flags (recorded, convention-resolved) |
|---|---|---|---|---|---|
| **ADF_r recursive sequence (PWY)** | consistency of the crossing-time date estimators under diverging-CV rate conditions; size 0.049 at the no-bubble corner; inconsistency against Evans-type collapse | iid or weakly dependent errors; drift η > 1/2; r₀ = 0.10 by convention; cv rule log(log(ns))/100 by convention | **RT for the sequence**, FS for sup ADF_r | `eru-0131`, `eru-0100`, `eru-0126` | D4 high (no dating-error distributions in `eru-0131`); D7 high |
| **SADF (sup statistic)** | size and power tables at T = 100–1600; specification sensitivity to the null drift exponent | asymptotic distribution discontinuous at η = 0.5 | **FS — existence test, explicitly not a date-stamper** | `eru-0131`, `eru-0393`, `eru-0238`, `eru-1044` | D4 n/a by construction |
| **GSADF** | size 0.055–0.070 at 5% **at lag k = 0**, but **severe distortion under lag overspecification of the same null — up to 0.787 at 5% (fixed k = 6, T = 100), and 0.697 under significance-test kmax = 6** (`eru-0393` Table 2 p.1058, §7.1); power under Evans and randomly-starting bubbles; consistency for multiple bubbles where SADF is inconsistent | as SADF, plus r₀ = 0.01+1.8/√T (convention) | **FS — "an ex post statistic", authors' words** | `eru-0393`, `eru-1044` | D6 high as conventionally applied |
| **BSADF sequence / PSY date-stamping** | date estimates with means and SDs; **mean bias in the estimated origination date** 7.56 months at successful-detection rate 0.84 (standard CVs) or 12.20 months at 0.75 (FWER-controlled), Table 2 p.21; FWER 0.55–0.93 untreated, Table 1 p.20 — **the dating-bias and FWER figures are working-paper tier** (`eru-1289` = Cowles DP 2331; the 2025 chapter its DOI resolves to was never obtained, §7.4) | as GSADF, plus minimum duration δ·log(T) ("inevitably arbitrary") | **RT in construction**; characteristics measured RT in `eru-0395`, CS elsewhere | `eru-0395`, `eru-1289`, `eru-1044` | D6 high untreated; D7 low (`psymonitor` R package is the corpus's strongest reproducibility case, `eru-1031`) |
| **Reverse-regression implosion dating (PS 2018)** | collapse-date bias by collapse type (−0.00 to +0.09 of sample) | mildly-integrated collapse γ_T = 1 − c₂T^{−β} | **SPLIT — forward BSDF causal, reverse recursion not** | `eru-0559`, `eru-0823` | D5 must be read per statistic |
| **Wild-bootstrap / sign / WLS / time-transformed variants** | restored size under non-stationary volatility (asymptotic size 0.05 across shift configurations for PWY\*) | Cavaliere–Taylor volatility class σ_t = ω(t/T), non-stochastic càdlàg | **FS** — all evaluated as full-sample tests | `eru-0503`, `eru-0748`, `eru-0891`, `eru-1384`, `eru-1580` | D4 high (none reports dating accuracy) |
| **HAR / long-memory-robust DF (LPY)** | restored size under d ∈ (0,0.45); recursive dating with an ELW-estimated memory path | strongly dependent errors, fixed-b HAR standardisation | **CS** — dating recursion causal, evaluated ex post | `eru-1526`, `eru-0691` | D7 high |
| **End-of-sample monitors (AHLST MAX/SEQ, AMAX, AMAX-MR/TR)** | closed-form FPR at any horizon; TPR-versus-time detection profiles; MR/TR accelerate detection at unchanged FPR | stationary ergodic innovations; conditional heteroskedasticity permitted; window m a documented trade-off | **RT — the corpus's cleanest real-time designs** | `eru-0735`, `eru-0609`, `eru-1844`, `eru-1519` | D4 high (delay is given as curves, not distributions) |
| **CUSUM-family monitors (HB CUSUM, CUSUMV, covariate-augmented)** | FPR calibrated to a target and retained under time-varying volatility; standard CUSUM's FPR fails under time-varying volatility | volatility-path dependence of the CUSUM null limit; training/monitoring split | **RT** | `eru-1117`, `eru-1921`, `eru-1852` | D8 unclear |
| **Sequential monitors (Horváth line, RCA)** — `eru-1038` open-ended, `eru-0889` **closed-ended**, `eru-1845` both (corrected round 4, L-21) | limiting false-alarm probability α over the stated monitoring horizon; stopping-time limit theory | weak dependence (Bernoulli shift), finite fourth moments; boundary weight γ a documented trade-off | **RT** | `eru-0889`, `eru-1038`, `eru-1845` | D8 unclear; not bubble-specific |
| **Bayesian filtered-probability dating** | per-period false-flag rate 0.018 vs PSY's 0.057; longer, fewer episodes under a regime-change-averse loss | two-state SV; sequential parameter learning is what makes it real-time | **RT** — the paper's core critique is that full-sample MCMC parameter estimates make "filtered" probabilities non-causal | `eru-0526` | D7 high |
| **Noncausal / MAR bubble tests** | size conditional on tail exceedances; forward-looking maximum-bubble-size and burst-horizon statements | heavy-tailed (α-stable or Student-t) innovations; anticipative dynamics | **RT** (`eru-1761`), **CS** (`eru-1770`, preprint tier) | `eru-1761`, `eru-1770` | tier flag on `eru-1770` |
| **Panel / common-factor extensions** | dating bias as a function of N and T; group-specific roots via clustering | large-N factor structure; the first factor carries the bubble | **CS** | `eru-1112`, `eru-1405`, `eru-0597` | D4 high |

**The one row a branch-3 comparator set should not omit.** `eru-1716`
(Boswijk, Yu & Zu 2024, preprint tier) devolatises daily increments by realised
volatility computed from five-minute intraday data and then runs the recursive
sup-DF, reporting classical PWY size of **0.048–0.392** under a Heston null at
n = 252 (Table 1, nominal 5% row across all nine (a, c) cells; the earlier
`0.048–0.282` stopped at the c = 0.3 column and omitted the table's maximum,
0.392 at a = 0.01, c = 1.5 — L-21). It is the only record in the corpus whose design touches intraday data at
all, and its authors state explicitly that the test itself still operates at low
frequency, with intraday data entering only through the volatility estimate. The
corpus contains **no** published operating characteristic for any of these
detectors applied *at* intraday frequency.

## 8. Full-text extraction for both Phillips records, and adjudication (i)

Protocol §9.1(i) is the branch-3 precondition this review exists to discharge.
The question, fixed in advance: **do the FULL TEXTS of PWY 2011 (KI-01) and
PSY 2015 (KI-02, with KI-03 consulted where 2015a delegates theory to 2015b)
support the agenda Rev 3 sentence "date-stamps an explosive state in real time
against derived critical values"?**

Criteria, fixed in advance and applied unchanged:

- **SUPPORTED** iff both (a) the date-stamping rule as defined in the paper uses
  only data through *t* plus critical values fixed ex ante of *t*, and (b) the
  critical values used for date-stamping are delivered by derived limit theory,
  not solely by finite-sample simulation with theory absent.
- **PARTIAL** iff (a) holds but the operational critical values are simulated
  finite-sample values or right-tail response-surface values.
- **UNSUPPORTED** iff (a) fails.

The verdict must state, per paper, **which statistic** carries the real-time
property, since the agenda sentence quantifies over the family.

**Retrieval note, recorded because the dispatch premise was false.** Four
in-cap retrieval attempts failed for KI-01/02/03 (eliScholar returned a 0-byte
file; SMU InK was bot-blocked; `cowles.yale.edu` and CiteSeerX served HTML). A
documented cap deviation (web search plus a Cowles reprint fetch) secured the
published *International Economic Review* texts of all three. The deviation was
confined to these three §9.1(i) adjudication carriers and is recorded here
rather than absorbed. Recorded as protocol amendment **A5**, appended to the
protocol addendum by this document (§12.5).

**Source-text provenance, and what has now been re-checked.** Every quotation,
equation number and page reference in §8 was originally a transcription made once
by one agent from the Cowles reprint of the published *IER* text. §9.5 records
the retrieval route and a SHA-256 content digest per text. **All three Phillips
texts were re-fetched on 2026-09-02** — over plain HTTP, the scheme the round-1
attempt did not try — and every quoted string and reported number below was
re-read against the retrieved file and **verified**. Two things did not survive
that re-read and are fixed at their sites: **nineteen page locators were wrong**
(almost all by one page; full old→new table in §12.1 **L-18**, whose round-2
headline count of "fourteen" is corrected there under LITERATURE-3-3), and one
paraphrase was quotation-marked as if verbatim. No digest was taken at extraction
time, so version identity between the 2026-08 and 2026-09 retrievals is still not
establishable; that residue is verification gap **VG-10**, now downgraded to
minor. *(Findings QUANT-1-7, LITERATURE-2-2, QUANT-2-4, QUANT-2-3.)*

### 8.1 PWY 2011 — `eru-0131`, [doi:10.1111/j.1468-2354.2010.00625.x](https://doi.org/10.1111/j.1468-2354.2010.00625.x)

**Extraction, from the published *IER* 52(1):201–226 text (Cowles Foundation
Paper 1349 reprint).**

| field | extracted content |
|---|---|
| E3 detectors | forward recursive right-tailed ADF sequence ADF_r with date-stamping via eq. (8); sup_{r∈[r₀,1]} ADF_r as the existence test; rolling ADF (window N = 77) as robustness |
| E4 null | ρ = 1 in ADF regression (7) with intercept μ_x and J lags; limit in demeaned Brownian motion (p.207); errors NID(0,σ²) assumed for the bias-correction machinery, but the asymptotics do not require normality — "The asymptotic theory developed below does not require the normality assumption, whereas the bias correction explained later does use the distributional assumption" (fn. 6, p.207); the mildly-explosive model (9) carries no intercept, to avoid a deterministically explosive component (p.208) |
| E5 critical-value provenance | limit distributions **derived**: under the null, ADF_r ⇒ ∫W dW / (∫W²)^{1/2} (p.207). Operational test-level values **simulated**: "The critical values for the ADF statistic and sup_{r∈[r₀,1]} ADF_r are obtained by Monte Carlo simulation with 10,000 replications" (Table 1 note, p.213). Date-stamping critical values are a **stated convention**: "The setting employed is cv_adf_n(s) = log(log(ns))/100. For the sample sizes considered in our empirical application, this setting leads to critical values around the 4% significance level" (p.207); numerically 0.013–0.018 for n = 389 (p.214) |
| E7 tuning | r₀ = 0.10 (39 of 389 observations) — convention, no derivation stated (Table 1 note p.213); rolling window N = 77 = 20% of sample, alternatives 60 and 120 tried (fn. 14 p.215); lag by Campbell–Perron top-down testing at 5%, max 12 (Table 1 note p.213; text p.214); optional minimum duration log(n)/n (fn. 10 p.212) |
| E8 causality | ADF_s at fraction s is computable from observations 1…⌊ns⌋ only; the date-stamp rule (8) is a first-crossing rule against a cv function fixed ex ante of *t*. The sup statistic is a full-sample existence statistic |
| E9 size | 0.049 at nominal 5%, n = 120, 10,000 replications, at the no-bubble corner g = 0.00 of the power design (Table 3 Panel A, p.219) |
| E11 dating | dating rules (8), (15), (21) with consistency shown under model (14) (mildly explosive with re-initialisation); **no simulated bias/MAE/delay distributions for the date estimators** |
| E12 false alarm | asymptotic only: under the null, P(any origination detected) → 0 as n → ∞ because α_n → 0 and cv diverges (eq. 13, p.210). No finite-sample family-wise accounting, no ARL₀ |
| E13 validity | consistency of dating requires only that cv diverge more slowly than n^{1−δ/2} (condition (20), p.212); mildly explosive ρ_n = 1 + c/k_n with k_n → ∞, k_n = o(n), x₀ = o_p(√k_n) |
| E14 code/data | none stated |

**Verdict for PWY 2011: PARTIAL.**

- Criterion (a) **HOLDS for the recursive ADF_r sequence.** Verbatim:
  "r̂ₑ = inf_{s≥r₀} {s : ADF_s > cv_adf(s)}, r̂_f = inf_{s≥r̂ₑ} {s : ADF_s <
  cv_adf(s)}" (eq. (8), *IER* 52:**207**). The statistic at s uses data through ⌊ns⌋
  only, and the threshold path is fixed ex ante.
- Criterion (a) **FAILS for the sup statistic.** Verbatim: "However,
  sup_{r∈[r₀,1]} ADF_r cannot reveal the location of the exuberance"
  (*IER* 52:**214**). SADF is an existence test, not a date-stamper.
- Criterion (b) **FAILS as the operational source.** The limit distribution of
  ADF_r is derived, but the values actually used are Monte Carlo simulated
  (test level) or a stated divergence convention calibrated to "around the 4%
  significance level" (dating). Theory is present; it is not the source of the
  numbers.

**Statistic attribution:** the real-time property attaches to the recursive
ADF_r sequence (and its rolling variant); **not** to SADF.

### 8.2 PSY 2015a — `eru-0393`, [doi:10.1111/iere.12132](https://doi.org/10.1111/iere.12132), with the companion PSY 2015b — `eru-0395`, [doi:10.1111/iere.12131](https://doi.org/10.1111/iere.12131)

**Extraction, from the published *IER* 56(4) texts (Cowles reprints 1498, 1499).**

| field | PSY 2015a (`eru-0393`) | PSY 2015b (`eru-0395`) |
|---|---|---|
| E4 null | y_t = dT^{−η} + y_{t−1} + ε_t, ε iid(0,σ²), **η > 1/2** (eq. (3), p.1047); intercept in the empirical regression (4); limit theory invariant between negligible-drift and no-drift nulls (p.1050) | X_t = kT^{−η} + X_{t−1} + ε_t, η > 1/2, X₀ = O_p(1) (eq. (1), p.1081); fitted regression has intercept, no trend (eq. (3), p.1082) |
| E5 CV provenance | asymptotic distributions **derived** (Theorem 1); asymptotic CVs by numerical simulation of the limit functional (2,000 replications, 2,000-step Wiener approximation); finite-sample CVs by Monte Carlo, 2,000 replications (Table 1 and its note, p.1050); the empirical dating exercise compares BSADF_{r₂} with the 95% SADF critical value from Monte Carlo at each r₂ (p.1066). Theory requires α_T → 0 with slowly diverging cv (eqs (10)–(11)); in practice α_T is fixed at 0.05 (p.1052) | null distributions inherited from PSY 2015a Theorem 1; alternative-hypothesis limit forms of DF_r, BSDF_r and sequential DF derived in Theorems 1, 4, 5 with divergence rates T^{1−α/2} up and −T^{(1−α)/2} down; simulations use finite-sample 95% quantiles from 5,000 replications (p.1090). Consistency requires cv_T → ∞ with cv_T/T^{1−α/2} → 0 (eqs (15)–(16), Theorems 2–3) |
| E7 tuning | r₀ = 0.01 + 1.8/√T, "based on extensive simulation" — a stated empirical rule, **CONVENTION**; minimum duration δ·log(T) with frequency-dependent δ, which the authors call "inevitably arbitrary" (fn. 10, p.1052); k = 0 recommended after the size study; sequential-PWY re-initialisation needs two confirming observations (fn. 23, p.1062) | minimum window 12 observations in all simulations (T = 100 ⇒ r₀ = 0.12); L_T = δ·log(T)/T; α_T = 0.05 finite-sample quantiles |
| E8 causality | BSADF_{r₂} uses only windows ending at r₂, so it is computable at r₂ from data through r₂ | both detectors use the information set I_r = {1,…,⌊Tr⌋}; date estimates are first crossing times against cv sequences fixed under the null |
| E9 size | SADF 0.041–0.060 and GSADF 0.055–0.070 at nominal 5%, T = 100–1600, k = 0 (Table 2, p.1058) — all ten values verified cell for cell against the reprint; severe distortion under lag overspecification, **worst cell GSADF 0.787** (fixed lag k = 6, T = 100), and the authors' own highlighted case "when T = 100, r₀ = 0.190, and kmax = 6, the size of SADF and GSADF is 0.145 and 0.697" (significance-test lag selection, p.1058). *The earlier form of this cell gave "up to 0.697/0.401", which paired the T = 100 significance-test GSADF figure with the T = 400 fixed-lag k = 6 GSADF figure and omitted the table's maximum; corrected on re-reading (L-18).* | not reported — all simulations use finite-sample 95% quantiles as detection thresholds; no null-side rejection rates tabulated |
| E11 dating | consistency results (i)–(iii), pp.1056–1057: PWY consistent for the first bubble, **inconsistent for the second** when the first is longer, with misdating limit r_{2e} + r_{1f} − r_{1e}; BSADF consistent for all origination/termination dates under rate condition (11). Detection frequencies by count (Tables 6–7); **delay distributions delegated to the companion** | **the delay-distribution record of the family**: mean (SD) of estimated dates per cell; single bubble r_e = 0.40 ⇒ PSY r̂ₑ 0.45 (0.03), delay 0.05 falling to 0.03 as δ_T rises 1.06→1.10; delay grows 0.04→0.06 as duration goes 0.10T→0.20T (p.1090); first-bubble detection delay 4–7 observations (p.1092); PWY delay for the second bubble 11 observations vs PSY's 6 at duration 0.20T (p.1093); asymptotic misdating of PWY's second bubble r̂_{2e} → r_{2e} + (r_{1f} − r_{1e}) (Theorem 7). Termination estimates near-exact (SD 0.00–0.01), attributed to the sharp-collapse DGP |
| E12 false alarm | asymptotic false-detection probability → 0 via diverging cv (eqs (10)–(11), pp.1054–1055; "The probability of false rejection of normal behavior then goes to zero", p.1055); **no finite-sample FWER or ARL₀**; the CUSUM comparator carries the Chu et al. (1996) monitoring bound P(crossing) ≤ exp(−κ_α/2)/2 (p.1062) | no finite-sample family-wise analysis; asymptotic no-false-positive property via the Theorem 2–3 conditions; successful detection is defined conditionally on r_e ≤ r̂ₑ < r_f (p.1090) |
| E13 validity | iid errors for Theorem 1; η > 1/2 (results differ for η < 1/2, fn. 8); r₀ ≤ r_{1e} for identification of the first bubble; r₀ < r_{2e} − r_{1f} to separate episodes. Failures reported: GSADF size distortion under lag overspecification; GARCH of empirical magnitude harmless (Table 3); non-stationary-volatility defect acknowledged citing Harvey et al.'s wild bootstrap (fn. 14); **the PSY strategy flags crashes (1917, 2009 subprime) as exuberance episodes** (p.1066) | iid errors; η > 1/2; r₀ < r_e needed for identification, else origination is estimated with delay at r₀; r₀ > r_{2f} − r_{1f} degrades PSY to delayed detection and kills sequential PWY entirely (eq. (23), pp.1089–1090); abrupt O_p(1) collapse specification, graduated collapse deferred. Failures: PWY inconsistent for the second bubble (Theorems 6–7); CUSUM detection rate **decreases** with sample size (Table 4, p.1092) |
| E14 code/data | Gauss and Matlab code publicly available (fn. 4, p.1046); EViews add-in | Gauss/Matlab code public (fn. 5, p.1081) |

**Verdict for PSY 2015: PARTIAL.**

- Criterion (a) **HOLDS for the BSADF sequence.** The paper states the causal
  split itself, verbatim: "Importantly, the new date-stamping strategy may be
  used as an ex ante real-time dating procedure, whereas the GSADF test is an ex
  post statistic used for analyzing a given data set for bubble behavior"
  (*IER* 56:**1053**). The companion defines both detectors on I_r = {1,…,⌊Tr⌋}
  (*IER* 56:**1082**) and derives their real-time limit theory (Theorems 1–9).
- Criterion (a) **FAILS for GSADF as a date-stamper**, by the authors' own
  sentence above. Episode dates quoted from GSADF subsamples are full-sample.
- Criterion (b) **FAILS as the operational source.** Limit distributions are
  derived (Theorem 1 eq. (5); the companion's Theorems 1–9), but every
  operational quantile is simulated: "The asymptotic critical values are obtained
  by numerical simulations with 2000 replications… The finite sample critical
  values are obtained from Monte Carlo simulation with 2000 replications"
  (Table 1 note, *IER* 56:**1050**); and the dating exercise "compared the backward
  SADF statistic with the 95% SADF critical value (obtained from Monte Carlo
  simulations with 2,000 replications) for each observation of interest" within
  "a (pseudo) real-time bubble monitoring exercise" (*IER* 56:**1066**).

**Statistic attribution:** the real-time property attaches to BSADF_{r₂}(r₀) —
and, per the companion's Theorems 2–3 and 8–9, to the PWY ADF_{r₂} special case
and the sequential-PWY variant — **not** to GSADF, which is the ex-post summary
statistic sup_{r₂} BSADF_{r₂}(r₀).

### 8.3 Confirm-or-correct: the verdict on the agenda sentence

**The agenda's Rev 3 sentence is CORRECTED, not confirmed. Verdict: PARTIAL.**

The sentence — "date-stamps an explosive state in real time against derived
critical values" — has two clauses and the full texts split them:

1. **"in real time" — SUPPORTED, but only under correct statistic
   attribution.** The sequence statistics ADF_r (PWY) and BSADF_{r₂} (PSY) are
   each computable at *t* from data through *t* with a threshold path fixed ex
   ante, and PSY 2015b proves consistency of the resulting crossing-time date
   estimators under the rate conditions cv_T → ∞, cv_T/T^{1−α/2} → 0
   (Theorems 2–3, 8). It is **NOT** supported for SADF or GSADF, which both
   papers describe in their own words as full-sample, ex-post existence
   statistics. The agenda sentence as written quantifies over the family and is
   therefore too strong.
2. **"against derived critical values" — NOT SUPPORTED as an operational
   description.** In both papers the critical values actually used are Monte
   Carlo simulated (asymptotic-functional or finite-sample) or, in PWY's dating
   rule, a stated divergence convention log(log(ns))/100 at "around the 4%
   significance level". The derived limit theory delivers the distributional
   *form* and the consistency *rate conditions*; it does not deliver the numbers.

**Prescribed Rev 4 correction, for the consumer to execute (protocol §9.1(i)
makes the agenda edit a consumer-side action, not this review's).** Replace the
Definitional-basis (d) and branch-3 wording with an attribution-correct form,
e.g.:

> The recursive right-tailed unit-root family date-stamps an explosive state in
> real time **through its sequence statistics** — ADF_r
> ([PWY 2011](https://doi.org/10.1111/j.1468-2354.2010.00625.x) eq. (8)) and
> BSADF_{r₂} ([PSY 2015a](https://doi.org/10.1111/iere.12132) p.1053, with limit
> theory in [PSY 2015b](https://doi.org/10.1111/iere.12131)) — **not** through
> SADF or GSADF, which their authors describe as ex-post existence statistics.
> The operational critical values are **simulated from a derived null limit
> theory** (or, in PWY's dating rule, a stated divergence convention), not
> derived values.

**What this does and does not do to the agenda's Rev 3 refutation of universal
(d).** It does not restore the universal. A time-t assignment null *is* attached
to a state assignment by the ADF_r / BSADF sequence, with a stated reference
distribution; universal (d) remains refuted. What falls is the *strength* of the
Rev 3 sentence: the family's real-time date-stamping is carried by two specific
sequence statistics, and its critical values are simulated, which matters
directly for branch 3 because simulated finite-sample critical values are
design-dependent (they depend on T, r₀, lag order and the assumed error and
volatility structure — §7.5) and therefore do not transfer to a new setting
without being re-simulated there. That re-simulation is `TO COMPUTE` handoff
**TC-5**.

## 9. Adjudications (ii)–(iv): NB-02, NB-08, NB-13 against the time-t assignment-null standard

### 9.0 The standard being applied, and why these three are adjudicated outside the corpus

The consumer agenda's Rev 3 text records that outside the explosive family "no
other located vocabulary was *classified by the sweeps* as carrying a time-t
assignment null — but the nearest candidates are unadjudicated, not absent:
drawdown/drawup episodes (NB-02/NB-08) and flight-to-quality (NB-13) attach
stated nulls at filtered causality and were screened only at abstract depth;
whether their nulls attach to the assignment procedure itself awaits the
full-text pass." This section is that pass.

**Verdict vocabulary, fixed in protocol §9.1 before any of the three full texts
was read:**

- `assignment-null` — the stated null attaches to the state-assignment decision
  at time *t*: the statistic is computable at *t* from information through *t*,
  and its reference distribution under H₀ governs the time-*t* decision.
- `episode-statistic-null` — the null governs statistics of completed / ex-post
  episodes.
- `mixed`.
- `indeterminate-from-full-text`.

All three records fail the corpus's eligibility criteria (they are not
explosive-family detectors), so protocol §9.1's final paragraph applies: they are
adjudicated as **out-of-corpus adjudication targets** in this dedicated section,
with full-text citations, and their eligibility failure is recorded per record.
None of them is in the 72.

**They are also not in the 1,996, and §9.1 required them to be (finding
SCOPE-1-1).** The same paragraph that authorises out-of-corpus adjudication
first requires that "records (ii)–(iv) are force-screened into the record
universe regardless of query recall (they are already identified; their
adjudication is a stated deliverable). Their inclusion in the CORPUS still
requires passing §2." Only the second half was executed. A grep of
[docs/literature/search_logs/explosive-regime/](search_logs/explosive-regime/)
for `10.21314/jor.2002.058`, `10.1017/jpr.2017.20` and
`10.1016/j.jfs.2008.08.001` returns matches in `se-nb-adjudications.json` and
`protocol-doicheck.json` only — not in either 1,996-row screening-verdict file,
not in the adjudication file, not in the candidate store. Consequences, stated
rather than smoothed over:

- the §3.1 identification count 4,898 and the deduplicated universe 1,996
  **exclude** all three;
- no screening verdict citing a criterion identifier exists for any of them, so
  the eligibility failures below rest on this section's full-text reading alone
  rather than on two screeners plus an adjudicator;
- the §3.2 statement that the flow reconciles exactly with the logs holds over
  the universe as executed, which is three records short of the universe §9.1
  prescribes.

The substantive verdicts are unaffected — all three fail S-a, S-b and S-c on
full text and would have been excluded at §2 in any case. Recorded as protocol
amendment **A9** and verification gap **VG-9**. The corpus is frozen and is not
re-screened.

### 9.1 NB-02 — Johansen & Sornette, drawdown outliers

**Record.** *Large stock market price drawdowns are outliers*, [doi:10.21314/jor.2002.058](https://doi.org/10.21314/jor.2002.058)
(*Journal of Risk* 4(2):69–110). **Version adjudicated:** arXiv:cond-mat/0010050v2
(25 July 2001), the preprint twin; the journal full text is not open access. The
v2 revision postdates submission and matches the journal record's title, authors,
abstract, section structure and tables.

**Verdict: `episode-statistic-null`.**

**The evidence that decides it, verbatim from the adjudicated text.**

1. The episode boundary is defined ex post: "We define a drawdown as a persistent
   decrease in the price (specifically the closing price) over consecutive days.
   A drawdown is thus the cumulative loss from the last maximum to the **next**
   minimum of the price" (§1, p.1). The drawdown is not knowable at any time
   during the episode; it is knowable only after the subsequent reversal. This is
   consistent with the naming sweep's causality code F, and the full text confirms
   it rather than merely leaving it open.
2. The null is a distributional law over *completed* drawdowns: "we shall take the
   stretched exponential law as our null hypothesis" (§1, **p.2** — was `p.1`;
   corrected on the round-3 re-read, L-20), fitted in §3
   (eq. (4)) to the population of drawdowns extracted from each full historical
   sample.
3. The test is a sample-level surrogate comparison: "for each financial time
   series, we have reshuffled the daily returns 1000 times and hence generated
   1000 synthetic data sets for each" (§5 *Synthetic tests and statistical
   significance*, **p.9** — was `p.8`), and "The third column gives the
   number of drawdowns above the threshold in the true data. The fourth column
   gives the number of surrogate data sets with 0, 1, 2, 3, … drawdowns larger
   than the threshold. The last column quantifies the corresponding confidence
   level" (§5, **p.9** — was `p.8`; both corrected on the round-3 re-read,
   L-20). The estimand is a count over the whole sample against a
   surrogate ensemble.
4. The conclusion attaches to a class of completed episodes, not to any
   assignment: "The remaining 1–2% of the largest drawdowns are not at all
   explained by the exponential null-hypothesis or its extension in terms of the
   stretched exponential" (§6 *Summary and discussion*, item 6, **p.10** — the
   numbered list runs pp.9–10 and item 6 falls wholly on p.10; tightened on the
   round-3 re-read, L-20).

Against the protocol §9.1(ii) criteria: the `assignment-null` condition requires a
decision rule executable at some time *t* during an episode, with the episode
boundary knowable at *t* or at a stated bounded lag, whose reference distribution
under the null governs that decision. **No such rule is stated anywhere in the
paper.** The `episode-statistic-null` condition — the null is fitted to and tested
on the population of completed drawdowns — holds exactly.

**Eligibility, from full text.** S-a **FAIL**: the alternative is a specific
amplification mechanism / transient dependence among successive daily drops
producing outlier drawdowns, not explosive or mildly explosive autoregressive
behaviour; no autoregressive root ρ > 1 appears anywhere in the paper. S-b
**FAIL**: the output is a sample-level outlier classification of completed
episodes. S-c: a null with a reference distribution *is* stated, but it does not
govern a time-indexed decision, so S-c as written also fails.

### 9.2 NB-08 — Landriault, Li & Zhang, drawdown laws

**Record.** *A unified approach for drawdown (drawup) of time-homogeneous
Markov processes*, [doi:10.1017/jpr.2017.20](https://doi.org/10.1017/jpr.2017.20)
(*Journal of Applied Probability* 54(2):603–626). **Version adjudicated:** the
journal version itself, open-access PDF from Cambridge Core. The arXiv preprint
twin (arXiv:1702.07786) was not needed.

**Verdict: `episode-statistic-null`.**

**The evidence that decides it.** The paper is pure analytic apparatus. It derives
the exact joint law of (τ_a, M_{τ_a}, Y_{τ_a}) — the first passage time of the
drawdown process over a threshold *a*, the running maximum at that time, and the
overshoot — for time-homogeneous Markov processes: "the joint law of the three
drawdown quantities is shown to be the unique solution to an integral equation
which is expressed in terms of fundamental two-sided exit quantities of the
underlying process" (abstract, p.603); "In general, our main result reduces the
drawdown problem to fundamental two-sided exit quantities" (§1, p.605).

There is **no null-versus-alternative decision problem, no test statistic, no
critical value and no procedure assigning a state to any time index** anywhere in
pp.603–626. The paper's only contact with sequential decision-making is a
citation of quickest-detection methods as one application area among several:
"Drawdowns are also closely related to many problems in mathematical finance,
actuarial science, and statistics such as the pricing of Russian options …,
De Finetti's dividend problem …, loss-carry-forward taxation models …, and
change-point detection methods (see, e.g. [31])" (§1, p.604). No procedure is
proposed. The references close the paper with no concluding test proposal.

Under protocol §9.1(iii) the `assignment-null` condition — that the derived
first-passage laws be presented as, or directly yield, a stopping-time test with
a known null distribution for an online decision — **fails on the "presented as"
limb**.

**Derivability, noted per the protocol's explicit rule.** τ_a = inf{t > 0 : Y_t >
a} **is** an online stopping time: Y_t = M_t − X_t is computable at *t* from data
through *t* ("Let τ_a = inf{t > 0 : Y_t > a} be the first time the magnitude of
drawdowns exceeds a given threshold a > 0. Note that (sup_{0≤s≤t} Y_s > a) =
(τ_a ≤ t) P-almost surely. Hence, the distributional study of the maximum drawdown
of X is equivalent to the study of the stopping time τ_a", §1, p.604). The derived
law of τ_a is exactly the null run-length / false-alarm distribution that a
drawdown-based monitoring rule would require, so an assignment procedure with a
known null distribution is **directly derivable** from **Theorem 1 (p.609)** and
its spectrally-negative and Lévy corollaries (**Corollary 2, p.610**;
**Corollary 3, p.611**). **Corrected on the round-3 re-read:** the earlier form
of this sentence, and the §9.5 and TC-6 rows that repeated it, cited
"Theorem 3.1". The paper numbers its results sequentially, not by section; its
main result is Theorem 1, and the only occurrence of the string "Theorem 3.1" in
the text is a citation to *another* paper's theorem (reference [23], p.613). The
substance of the derivability claim is unchanged. *(L-20.)* Protocol §9.1(iii) rules that derivability
is a `TO COMPUTE`-adjacent observation and **not** a published assignment null,
so the verdict stands at `episode-statistic-null` with the derivability recorded.

That derivability is the most actionable thing in this section for branch 3 and is
carried forward as `TO COMPUTE` handoff **TC-6**.

**Eligibility, from full text.** S-a **FAIL**: there is no alternative hypothesis
at all, let alone an explosive one; this is probability theory under a single
specified process. S-b **FAIL**: no time-indexed state-assignment output.
S-c **FAIL** as written: exact laws under null processes are derived, but no
decision is taken against them.

### 9.3 NB-13 — Baur & Lucey, flight-to-quality

**Record.** *Flights and contagion—An empirical analysis of stock–bond
correlations*, [doi:10.1016/j.jfs.2008.08.001](https://doi.org/10.1016/j.jfs.2008.08.001)
(*Journal of Financial Stability* 5(4):339–352). **Version adjudicated:** IIIS
Discussion Paper No. 122 (March 2006), the working-paper twin. **The journal
full text was NOT obtained** after four attempts: (1) SSRN 886119 delivery —
Cloudflare challenge; (2) OpenAlex and Semantic Scholar OA lookup — status
CLOSED, no OA location; (3) web search for a mirrored PDF — none; (4) search for
a cached SSRN PDF — none. The version caveat is stated in full below.

**Verdict: `episode-statistic-null` — PROVISIONAL ON THE WORKING-PAPER TWIN.**

> **CONVENTION (this document, §9.3), registered as protocol amendment A13(c).**
> Two things below are this review's constructions, not the frozen protocol's,
> and the earlier form of this passage presented the first as protocol text:
>
> 1. **The gloss on `indeterminate-from-full-text`.** Protocol §9.1 defines
>    `assignment-null` and `episode-statistic-null` at length and then lists
>    `mixed` and `indeterminate-from-full-text` **as bare tokens with no
>    definition at all**. The reading that `indeterminate-from-full-text` is
>    "for the case where a full text was read and did not decide" is *this
>    document's* gloss. The frozen protocol decides neither the meaning of its
>    two undefined tokens nor the version-mismatch case, and saying otherwise —
>    as the round-1 text did — attributes a definition to the protocol that the
>    protocol does not make. *(Finding LITERATURE-2-6.)*
> 2. **The scope qualifier "PROVISIONAL ON THE WORKING-PAPER TWIN".** §9.1's
>    verdict vocabulary defines no scope qualifier. This is an extension of the
>    same class as A7's fourth response level, and it is registered the same way:
>    as a numbered, post-hoc amendment, **A13(c)**, cross-referenced from §9.4,
>    §14 item 3 and VG-3. *(Finding REV-2-4.)*
>
> A reader who rejects the gloss in (1) may read NB-13 as
> `indeterminate-from-full-text` for the 2009 journal version. The evidence
> below is unchanged either way, and so is the operational instruction to the
> consumer.

*Why this label and not `indeterminate-from-full-text`, on the convention just
declared (findings REV-1-6, REV-2-4, LITERATURE-2-6).* Under this document's
gloss, `indeterminate-from-full-text` is for the case where a full text was read
and did not decide. That is not this case: a
full text **was** read and **did** decide, decisively, under §9.1(iv)'s
pre-specified criterion — the DP 122 construction is a full-sample
coefficient test that induces day labels, which §9.1(iv) rules
`episode-statistic-null` in advance and by name. Relabelling it
`indeterminate-from-full-text` would misdescribe that: it would suggest the
adjudicated text was ambiguous, when the ambiguity is entirely about **which
version** the label attaches to. The verdict token therefore stays inside the
frozen vocabulary and unaltered; **"provisional on the working-paper twin" is a
scope label on the adjudicated object, not a fifth verdict** (A13(c)). What it
means operationally:

- The verdict is established for **IIIS DP 122 (2006)**.
- It is **extended** to *J. Financial Stability* 5(4):339–352 (2009) by an
  absence-of-evidence inference — "no accessible trace of the journal version
  suggests a day-*t*-computable statistic with a stated reference distribution
  was added" — and an absence-of-evidence inference cannot carry a definite
  adjudication. The extension is the provisional part.
- The journal version demonstrably differs from DP 122 in ways this review can
  see: the sentence the agenda quotes appears in the journal abstract and not in
  DP 122, the country set differs, and the analysis is reorganised around a
  definition-and-test framing (see the version caveat below).
- Consequence for the consumer: the agenda may record NB-13 as adjudicated
  `episode-statistic-null` **on the 2006 working paper, provisional for the 2009
  journal version**, and may not record it as unqualifiedly
  adjudicated-and-negative. The verdict is re-openable under protocol §10 if the
  journal text surfaces (VG-3).

**The evidence that decides it.**

1. The test is a two-stage full-sample construction, and the paper says so
   itself: "Our two-stage approach has the main advantage that the test for the
   presence of flight-to-quality and contagion is not based on a priori defined
   crisis periods … but on **an a posteriori analysis** of these phenomena"
   (DP 122, §2 *Econometric Framework*, **p.5** — the section opens on p.4 and
   the quoted sentence falls wholly on p.5; tightened on the round-3 re-read,
   L-20).
2. Stage 1 estimates DCC-GARCH conditional correlations over the whole sample and
   forms the cumulative abnormal correlation change CACC_t = ρ_t − ρ_{t−K}
   (eq. (6)); "The time-series CACC_t combined with a threshold can reveal
   abnormal and extreme correlation changes for every time t" (DP 122, §2, p.6).
   The threshold, however, is a full-sample quantity: "The plots show absolute
   correlation changes in falling stock markets that are larger than **one
   standard deviation of the correlation distribution**" (DP 122, §4.1, p.14) —
   an exceedance rule against a full-sample standard deviation, not an ex-ante
   reference distribution.
3. Stage 2's inference is coefficient t-tests on full-sample regressions
   (eqs (7)–(8)): "t-statistics larger than 3 (2) are highly significant at the
   1% (5%) level" (notes to the regression tables, DP 122 **pp.19 and 24**;
   page locators supplied on the round-3 re-read, L-20).
4. The concepts themselves are defined as sample-level comovement statements:
   "In accordance with the literature, we define contagion as an increase of the
   correlation coefficient in a crisis period compared to a benchmark period.
   Flight-to-quality from stocks to bonds is defined as a decrease in the
   correlation coefficient and simultaneously falling stock markets" (DP 122,
   §1, p.2).

Day labels (October 1997, June 1998, post-September-11) exist, but they are
induced retroactively from full-sample estimates: the DCC parameters, the
standard-deviation threshold and every regression coefficient are functions of the
complete sample. No test statistic for a given day's label is computable from
information through that day, and no reference distribution for a day-*t*
assignment decision is stated anywhere. This is precisely the configuration
protocol §9.1(iv) pre-specifies: "Full-sample coefficient tests that *induce* day
labels are `episode-statistic-null` even though day labels exist — the null must
attach to the ASSIGNMENT, not to a parameter whose estimate labels days
retroactively."

**Version caveat, recorded rather than smoothed over.** The sentence the agenda
quotes — "We propose a definition and a test for flight-to-quality,
flight-from-quality and cross-asset contagion" — appears in the journal/SSRN-2008
abstract but **not** in the DP 122 abstract; the journal version reorganises the
analysis (eight countries including Japan, versus DP 122's Europe + US) around
that definition-and-test framing. The verdict is nevertheless attached to the
journal version's claims because (a) the journal abstract's definitions are the
same full-sample comovement-coefficient constructs documented in the DP 122 text,
and (b) §9.1(iv) rules that full-sample coefficient tests inducing day labels are
`episode-statistic-null` regardless of the existence of day labels. No accessible
trace of the journal version suggests a day-*t*-computable statistic with a stated
reference distribution was added between DP 122 and the journal text. **If the
journal full text later surfaces and contradicts this, the verdict is re-openable
under protocol §10.** This is a verification gap (§12.3, VG-3), not a resolved
question.

**Eligibility, from full text.** S-a **FAIL**: the alternative is a change in
stock–bond comovement, not explosive autoregressive behaviour; no root ρ > 1
appears. S-b **FAIL**: day labels are induced retroactively; no time-indexed
assignment decision is produced at *t*. S-c **FAIL** as written: the stated
inference (coefficient t-tests) does not govern a time-indexed decision.

### 9.4 Consequence for the agenda

All three nearest candidates are `episode-statistic-null`, but they are not
equally established: **two are adjudicated on the full text of the version the
agenda's claim is about; the third is provisional pending the journal version.**
NB-02 rests on the arXiv v2 preprint twin, which matches the journal record's
title, authors, abstract, section structure and tables; NB-08 rests on the
published article. NB-13 rests on IIIS DP 122 (2006), and the 2009 journal
version was never obtained after four documented attempts (§9.3, VG-3).

The agenda's "nearest unadjudicated candidates" sentence is therefore discharged
**with that asymmetry carried, not flattened**: outside the explosive family,
the three nearest located candidates have now been adjudicated at full-text
depth — two definitively, one on a working-paper twin with the journal version
unread — and none of the three, on the texts actually read, attaches its stated
null to a time-*t* assignment. Rev 4 should record the three verdicts, remove
"unadjudicated", and carry NB-13's provisional status rather than describing it
as adjudicated-and-negative without qualification. **The provisional qualifier is
outside protocol §9.1's frozen verdict vocabulary and is registered as amendment
A13(c); the protocol's `indeterminate-from-full-text` token is undefined in the
frozen text and the gloss this review applies to it is a declared CONVENTION of
§9.3, not protocol text.** A consumer transcribing the verdict must carry that
provenance with it. *(Findings REV-1-6, REV-2-4, LITERATURE-2-6.)*

One qualification the agenda must carry with it, because it is the only route
from this section to a usable detector: NB-08's first-passage law for the
drawdown stopping time τ_a **is** the null run-length distribution an online
drawdown monitor would need. It is derivable, not published as a test, and
deriving it is a `TO COMPUTE` for the executing project, not a citation.

### 9.5 Source-text provenance for §8 and §9 — retrieval route and content digest per text

§8's confirm-or-correct verdict and §9's three adjudications carry the whole
branch-3 precondition, and every one of them originally rested on verbatim
quotations and table/page locations transcribed from a primary text at a single
session. The repository holds no cached full text for any of them, so at first
delivery method fidelity at the decisive points was **asserted, not
re-openable**. This table records the retrieval route per text and a SHA-256
content digest of the file retrieved on 2026-09-02, so a successor auditor can
re-open the quoted page without repeating the retrieval search. **All seven
texts have now been retrieved, digested and re-read** — the
four Phillips-line texts in round 2 (which turned up the locator errors of L-18),
the three NB texts in **round 3** (L-20). Every digest in the table below has
been reproduced on **three** independent fetches (rounds 1, 2 and 3 of the
2026-09-02 remediation) and is byte-identical across all three. **The four
Phillips-line digests and NB-08's were reproduced a fourth time on 2026-09-03**
(round 4, L-21) and are again byte-identical; NB-02 and NB-13 were **not**
re-fetched on that pass, because round 4's boundary was the load-bearing set
(§7 synthesis prose plus the consumer agenda's citation sites) and neither text
is cited there.
*(Findings QUANT-1-7, LITERATURE-2-2, QUANT-2-4, QUANT-2-3, QUANT-3-4, REV-3-5.)*

**Round-2 correction, and it is a correction of this review's own claim.** The
first form of this table marked all four Phillips-line texts **FAILED** with
digest "none", and L-16/VG-10 concluded from that that §8.3's verdict and
§7.4's FWER triple "cannot presently be re-opened from this environment". **The
un-refetchability claim did not hold.** All four were retrieved on 2026-09-02,
and the per-host, per-attempt evidence is archived at
[se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json)
(SHA-256 `f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9`).
The precise failure mode, stated so the earlier claim is checkable rather than
merely withdrawn:

| host | attempt | result |
|---|---|---|
| `korora.econ.yale.edu` **:443 (https)** | p1349, p1498, p1499 | **connection refused** — `WinError 10061`, TCP refused on port 443. This is what the round-1 pass attempted, and it is all it attempted. |
| `korora.econ.yale.edu` **:80 (http)** | p1349, p1498, p1499 | **HTTP 200, `application/pdf`** — 258,681 / 1,204,657 / 470,694 bytes. The host serves the reprints over plain HTTP and does not listen on 443. DNS resolves to 128.36.64.198. |
| `cowles.yale.edu` (landing page) | round 1 | HTML, as recorded — the round-1 pass reached a landing page, not the file. |
| `cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf` | round 2 | **HTTP 200, `application/pdf`**, 591,865 bytes. |

The round-1 entry "host did not accept a connection" was therefore true of port
443 and **false of the host**; it was a scheme-level retrieval failure recorded
as an access barrier. *(Findings LITERATURE-2-2, QUANT-2-4.)*

| text | what §8/§9 quotes from it | retrieval route as executed | re-fetch 2026-09-02 | SHA-256 of retrieved file |
|---|---|---|---|---|
| `eru-0131` PWY 2011, *IER* 52(1):201–226 | eq. (8) date-stamp rule; cv_adf(s) = log(log(ns))/100 and the "around the 4% significance level" gloss, **p.207**; eq. (13), **p.210**; Table 3 Panel A **p.219** | published version, Cowles Foundation Paper 1349 reprint, `korora.econ.yale.edu/phillips/pubs/art/p1349.pdf` (recorded in `se-extraction-primary.jsonl` E1.fulltext_source) | **OK over http://** (https refused); 258,681 bytes; 27 pages; p.1 reads "EXPLOSIVE BEHAVIOR IN THE 1990S NASDAQ … COWLES FOUNDATION PAPER NO. 1349"; journal pagination 201–226 confirmed from the running heads | `a35fac94e4b04a1ecd93aa9bb5dcb2f9ecde4b5418ec20566ec70eed264f7ec4` |
| `eru-0393` PSY 2015a, *IER* 56(4):1043–1078 | "the new date-stamping strategy may be used as an ex ante real-time dating procedure, whereas the GSADF test is an ex post statistic", **p.1053**; Table 1 note **p.1050**; Table 2 size figures **p.1058** | published version, Cowles reprint `korora.econ.yale.edu/phillips/pubs/art/p1498.pdf` | **OK over http://** (https refused); 1,204,657 bytes; 37 pages; pagination 1043–1078 confirmed | `dfd19565775d1c9814ac1d33128223f585f201a0e740020f13e3254ed83a8c81` |
| `eru-0395` PSY 2015b, *IER* 56(4):1079–1134 | Theorems 2–3, 8 rate conditions; Tables 1–10 dating means and SDs (**pp.1090–1095**) | published version, Cowles Foundation Paper 1499, `korora.econ.yale.edu/phillips/pubs/art/p1499.pdf` | **OK over http://** (https refused); 470,694 bytes; 57 pages; pagination 1079–1134 confirmed | `85a984e9cab1aaf42d4decf22a2066ea6aedf0d32600d6042bddebefb8d7d012` |
| `eru-1289` Shi & Phillips, Cowles DP 2331 (2022) | Table 1 FWER triple 0.55 / 0.78 / 0.93 (**p.20**); Table 2 origination bias 7.56 → 12.20 months (**p.21**) | Cowles Discussion Paper 2331 text; the extraction log records no URL for this record | **OK** at `https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf`; 591,865 bytes; 31 pages. The 2025 CUP chapter carrying the record's DOI is still **not** obtained (LITERATURE-1-2) — this digest fixes the working paper, which is the version extracted | `309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e` |
| NB-02 Johansen & Sornette | drawdown definition **p.1**; "we shall take the stretched exponential law as our null hypothesis" **p.2**; §5 surrogate counts **p.9**; §6 item 6 **p.10** (arXiv v2 printed pagination = PDF page − 2; three locators corrected round 3, L-20) | arXiv:cond-mat/0010050v2, `arxiv.org/pdf/cond-mat/0010050v2` (`se-nb-adjudications.json`, `version_adjudicated`) | **OK**, 1,205,388 bytes, page 1 reads "arXiv:cond-mat/0010050v2 25 Jul 2001 — Large Stock Market Price Drawdowns Are Outliers — Anders Johansen and Didier Sornette" | `d8ae7e69dce54dc97a3b014f4865ad263a0cf4d2d6a75fa8476214d3bc12973f` |
| NB-08 Landriault, Li & Zhang, *J. Appl. Prob.* 54(2):603–626 | abstract p.603; τ_a definition and the change-point-detection citation p.604; §2 two-sided exit quantities pp.605 ff.; **Theorem 1 p.609** (was cited as "Theorem 3.1" — corrected round 3, L-20), Corollary 2 p.610, Corollary 3 p.611 | Cambridge Core open-access PDF, `cambridge.org/core/services/aop-cambridge-core/content/view/S0021900217000201` | **OK**, 255,312 bytes, page 1 reads "J. Appl. Prob. 54, 603–626 (2017) doi:10.1017/jpr.2017.20 … A UNIFIED APPROACH FOR DRAWDOWN (DRAWUP) OF TIME-HOMOGENEOUS MARKOV PROCESSES" | `87277984ef7ecf4c61509577257de911b40ed18331d32013ac7249b3ebe13413` |
| NB-13 Baur & Lucey, IIIS DP 122 (2006) | §1 p.2 definitions; §2 *a posteriori* sentence **p.5**, CACC eq. (6) and its threshold sentence **p.6**; §4.1 p.14 one-standard-deviation threshold (printed pagination = PDF page − 3; verified round 3, L-20) | `tcd.ie/triss/assets/PDFs/iiis/iiisdp122.pdf` | **OK**, 1,233,602 bytes, page 1 reads "IIIS Discussion Paper No.122/March 2006 — Flight-to-quality or Contagion? An Empirical Analysis of Stock-bond correlations — Dirk Baur … Brian M. Lucey" | `9e38c95673c9880aa2d8db353c06b020be49e86b78b9280bbeea44d8c476379a` |

The three non-Phillips rows (NB-02, NB-08, NB-13) were re-fetched again on this
pass and returned **byte-identical digests** to those recorded in round 1
(`d8ae7e69…`, `87277984…`, `9e38c956…`), which is a small independent check that
the digest column is stable.

**What this establishes now, and it is more than round 1 claimed.** All seven
texts are re-fetchable and digested. For the four Phillips-line texts the
quotations and page locators were **re-read against the retrieved files on this
pass**, not merely bound to the right document:

- Every quoted string in §8.1, §8.2, §8.3 and §7.6 verified **verbatim** in the
  retrieved reprints. Nothing quoted was found to be misquoted, with one
  exception fixed at its site: §8.1's `"the asymptotics do not require
  normality"` was quotation-marked but is a paraphrase; PWY fn. 6 reads "The
  asymptotic theory developed below does not require the normality assumption".
- **The three NB texts have now been re-read (round 3), and the residue is
  closed.** Round 2 re-fetched them but did not read them, and said so; round 3
  re-fetched them a third time (digests again byte-identical) and read every
  quoted string and every page locator against the retrieved file. Result:
  **all fourteen quoted strings taken from the three adjudicated texts verify
  verbatim** (five in §9.1, four in §9.2, five in §9.3); **four page locators
  were wrong or loose** (three in §9.1, one in §9.3); and **one result was
  misattributed** (§9.2's "Theorem 3.1" is the paper's Theorem 1 — the string
  "Theorem 3.1" in that paper is a citation to another work). All are corrected
  at their sites and tabulated in **L-20**. NB-08's locators verified exactly as
  published. **One quoted sentence in §9.3 is NOT covered by this check and
  remains unverified**: "We propose a definition and a test for
  flight-to-quality, flight-from-quality and cross-asset contagion" is
  attributed to the *journal/SSRN-2008 abstract*, not to DP 122, and the journal
  text was never obtained (VG-3). *(Findings REV-3-5, QUANT-3-4.)*
- Every *headline* number verified: PWY's 0.049 at the g = 0.00 column of Table 3
  Panel A and its Table 4 Evans-model power row; all ten of PSY 2015a's Table 2
  k = 0 size figures, cell for cell; PSY 2015b's delay figures (0.05→0.03,
  0.04→0.06, 4–7 observations, 11 vs 6); and **`eru-1289`'s FWER triple
  0.55 / 0.78 / 0.93** (DP 2331 Table 1, p.20) and its 7.56 → 12.20-month
  origination bias (Table 2, p.21).
- **One number did not survive the re-read**, and it is a summary rather than a
  headline: §8.2's E9 cell gave lag-overspecification distortion "up to
  0.697/0.401", which pairs two unrelated cells of PSY Table 2 and omits the
  table's maximum (GSADF 0.787 at fixed lag k = 6, T = 100). Restated at its site
  and recorded in L-18.
- **Page locators did not verify.** **Nineteen** of them were wrong, almost all
  by exactly one page — round 2 reported this as "fourteen", which its own L-18
  table already contradicted; the recount is in L-18 (LITERATURE-3-3). They are
  corrected throughout §7, §8 and this section, and the full old→new list is
  given in §12.1 **L-18**. The three §9 NB texts' own locators were corrected
  separately in round 3 (**L-20**) and are not in that count.
  *(Findings QUANT-2-3, LITERATURE-3-3.)*
- **One of round 3's own corrections did not survive round 4.** The L-18 row for
  PWY's Table 4 was corrected to "**p.221** (Appendix pp.222–225)"; the Appendix
  in fact runs **pp.222–224**, ending on p.224 where REFERENCES begin. Round 4
  also found four further errors in §7's synthesis prose that neither earlier
  round reached — an `eru-0131` design attribution, an `eru-1716` size range, an
  `eru-1519` claim the source contradicts, an `eru-0395` result attributed to the
  wrong numbered theorem, and a `eru-0889` / `eru-1038` cell carrying three
  errors at once. All six sites are tabulated in **L-21**, together with the six
  load-bearing records that could not be retrieved at all (**VG-17**).
  *(Round 4, 2026-09-03.)*

**What is still not established.** A digest fixes a *file*, not a *version*:
the Cowles reprints are reprints of the published *IER* articles and carry the
journal pagination, but the extraction stage took no digest, so this pass cannot
prove that the file retrieved in 2026-09 is byte-identical to the one read in
2026-08. It can only show that the quoted content and (as corrected) the
locators are present in the file now served at the recorded URL. And
`eru-1289`'s **2025 CUP chapter remains unobtained**, so the tier correction of
L-10 stands unchanged: the FWER triple is working-paper-tier evidence that has
now been re-read, not peer-reviewed-chapter evidence.

## 10. Reporting bias and meta-bias (items 14, 21)

Funnel-plot asymmetry ([Egger et al. 1997](https://doi.org/10.1136/bmj.315.7109.629))
is **declared inapplicable with rationale**, as protocol §8 fixes in advance:
there is no common effect estimate with a standard error across these studies to
plot, and "precision" has no uniform meaning across Monte Carlo designs with
different DGPs, sample sizes and replication counts. It is not skipped; three
substitutes were pre-specified and all three were assessed.

### 10.1 Existence and uptake of critical evaluations

**Existence: abundant.** Classified from field E16 across the 53 records where it
was extracted: the study's primary declared outcome is a critical/negative
evaluation of the family in **7** records, partly so in **27**, and not so in
**19**. A methods literature in which roughly two-thirds of the evaluative records
declare a size failure, power deficit or dating defect as a primary or joint
contribution is not one that suppresses negative results about its index method.

The seven whose primary declared outcome *is* a critical evaluation:
`eru-0691` (size failure under long memory), `eru-0731` (out-of-sample forecasting
failure of the PWY statistic), `eru-1049` (size failure under autocorrelated
innovations), `eru-0503` (size failure under non-stationary volatility),
`eru-1044` (third-party stress test of the whole sup-ADF family), `eru-0813`
(explicit critical comparison of two families by a third party), `eru-0348` (size
failure under a realistic drift-break null).

**Uptake: the check as designed cannot be run, and this is a design finding.**
Protocol §8 item 1 asks whether the critical evaluations "are cited by the
family's *application* literature — or does the application stream cite only the
originating papers", and specifies a citation-uptake check "on the included
corpus, not a new search". But criterion X1 excludes plain applications by
construction: 109 of the 234 substantive full-text exclusions are X1. **The
corpus therefore contains almost none of the stream whose citation behaviour item
1 asks about.** The protocol's item-1 check and its X1 exclusion are mutually
inconsistent; recorded as a protocol defect (§12.2, I-2), not silently dropped.

What *is* observable is uptake within the method stream, and it is high:

| uptake event | source |
|---|---|
| the originator team's practice-facing synthesis adopts the Harvey et al. non-stationary-volatility remedy | `eru-1031` |
| the originator team formalises and remedies an external critique, citing Kruse–Wegener and Pedersen–Schutte by name | `eru-1526` |
| PSY 2015a itself acknowledges the non-stationary-volatility defect and cites the wild-bootstrap remedy (fn. 14) | `eru-0393` |
| the originator team quantifies its own procedure's multiplicity defect and the delay cost of fixing it | `eru-1289` |
| the originator team documents the specification fragility of its own test family | `eru-0238` |
| PSY 2015a's declared contribution includes demonstrating the inconsistency of its own predecessor PWY | `eru-0393`, `eru-0395` |

### 10.2 Originator-favourability check

Reported descriptively, as the protocol requires, and with the caveat that
"favourability" is a judgment this review is making about other authors' verdicts,
not a measurement.

Authorship lineage across the 72 records: **21** carry a PSY-lineage author
(Phillips, Shi, Yu, Wu); **16** carry a Harvey–Leybourne–Taylor–Astill-line
author; **35** are neither. **Over the 69 distinct works the counts are 19 / 16 /
34**: `eru-0154` and `eru-0904` are PSY-lineage working-paper twins of
`eru-0126` and `eru-1526`, and `eru-0622` is an other-lineage twin of `eru-0675`
(§5.3, A10(b)). The distinct-work figures are the ones a favourability check
should read, since counting a working paper and its journal version as two
independent lineage observations overstates originator presence by exactly the
mechanism the check exists to detect. Neither figure changes the check's verdict
below. *(Finding REV-2-3.)*

The check does **not** find systematic originator favourability. The strongest
counter-evidence is that the sharpest negative results about the recursive family
in the corpus come from the originator team itself: `eru-0393`/`eru-0395` prove
PWY's inconsistency for a second bubble; `eru-0238` documents the family's
specification fragility to the null drift exponent; `eru-1289` measures its
FWER at 0.55–0.93 and prices the fix in origination-date bias **and in
successful-detection rate** (7.56 → 12.20 months at 0.84 → 0.75, Table 2 p.21 —
L-19); `eru-0393` reports its
own strategy flagging the 1917 and 2009 crashes as exuberance episodes.

Two directional cautions are recorded rather than resolved:

1. **Benchmark self-reference.** `eru-0675`'s critical evaluation of the family's
   aggregation-induced power loss is by a team one of whose members co-authored
   the panel GSADF used as the improved benchmark — a partial self-reference on
   the comparator, recorded at extraction.
2. **Rival-family authorship.** `eru-0731`'s negative out-of-sample verdict on the
   PWY statistic comes from the Sornette group, i.e. the originators of the LPPL
   family that this protocol excludes as an index method under X3. A negative
   verdict on one family from the originators of a rival family is exactly the
   configuration this check exists to flag, and it is flagged; the record is
   retained (it meets I2) and its verdict is not treated as neutral third-party
   evidence anywhere in §7.

The Harvey–Leybourne–Taylor line's 16 records are, as a group, a
critique-and-remedy programme against the PSY family's homoskedasticity and
deterministic-specification assumptions. Their negative findings about PSY are
therefore third-party relative to PSY but not disinterested relative to their own
proposed replacements, and §7 attributes every remedy claim to the record
proposing it.

### 10.3 Charter publication-bias fields (E16)

- **Preregistration / registry record: none, in every one of the 53 records where
  E16 was extracted.** Recorded as `none (recorded)` per record rather than
  skipped, per the charter rule. This is the expected state of econometrics and
  is not evidence of anything about these particular papers; it does mean that
  the distinction between a pre-planned and a post-hoc Monte Carlo design is
  unobservable throughout this corpus, and that no claim in §7 can be qualified
  by design preregistration.
- **Critical results as primary versus secondary declared outcomes:** the 7 / 27 /
  19 split in §10.1.
- **Nineteen records have no E16 extraction** because their full text was not
  reached at the primary pass (§5.4 and the recheck-only class).

### 10.4 The reporting bias this corpus most plausibly carries

Stated as a hypothesis, not a finding, and offered for falsification rather than
belief: the corpus shows no sign of suppressed *negative* results, and every sign
of **selective reporting of favourable operating characteristics within
otherwise-honest papers**. The mechanism is visible in the coverage asymmetries
of §6.1, over their assessable denominators — 52 of 65 report power, 39 of 65
report size, 23 of 65 report dating accuracy, 19 of 65 address multiplicity, 8
of 53 publish code. Papers proposing a dating
method that do not report dating error, and papers proposing a recursive
procedure that do not report its family-wise error rate, are not withholding a
negative result; they are choosing which characteristic to display. The effect on
a downstream consumer is the same as publication bias: the published record
over-represents the characteristics on which these detectors do well.

## 11. `TO COMPUTE` handoffs (ADR-0003)

Everything the synthesis identifies as unpublished-but-needed for branch 3, with
its DGP and design sketch. **None of these was computed here.** They are handoffs
to the executing project.

| id | what must be computed | why the published record does not supply it | design sketch |
|---|---|---|---|
| **TC-1** | empirical size of the chosen detector under the executing project's own intraday null, measured **two-sided** | every published size figure assumes at most two departures from the iid-homoskedastic null; deseasonalised intraday futures present intraday periodicity (a deterministic volatility path), autocorrelated microstructure noise, jumps and non-negligible short-horizon drift simultaneously (§7.1, §7.5). **The distortion is not uniformly upward**: under a deterministic drift break the corpus's own evidence has size tending to 1 *or* to 0 according to the sign of the break (`eru-0348`, Sollis 2016, Theorem 1 and Table 2, §7.1), which is a power failure rather than a false-alarm failure and would lead a consumer to the opposite operational conclusion | null DGP calibrated to the project's own deseasonalised series; nominal 5%; T at the project's bar count; r₀ and lag from TC-4. Report the rejection frequency against the nominal level **in both directions**, with the sign of the drift/level configuration that produced it, rather than a one-sided "how far above nominal" statistic *(finding QUANT-1-5)* |
| **TC-2** | origination-date error and its dispersion at branch-3 frequency and episode duration | published dating errors are 4–7 observations at T ≤ 400 (`eru-0395`) or a **mean bias in the estimated origination date** of 7.56 → 12.20 months **at successful-detection rate 0.84 → 0.75** (`eru-1289` Table 2 p.21, **working-paper tier**, §7.4); nothing at intraday frequency, where an episode may span a few hundred bars (§7.3) | mildly explosive alternative with duration set to the project's target episode length; report mean and SD of r̂ₑ − rₑ, not just detection frequency |
| **TC-3** | ARL₀ and conditional detection delay for the chosen detector | the corpus publishes FPR over a *fixed monitoring horizon* (`eru-0735`, `eru-1117`, `eru-1519`, `eru-1844`), not ARL₀; no record in the corpus reports ARL₀ under that name (§7.4) | surveillance framing per [Frisén 2003](https://doi.org/10.1111/j.1751-5823.2003.tb00205.x); report the delay-versus-ARL₀ curve, which is branch 3's declared comparison metric |
| **TC-4** | r₀ and the minimum-duration constant, derived rather than adopted | PWY state r₀ = 0.10 with no derivation; PSY's r₀ = 0.01 + 1.8/√T is "based on extensive simulation" and their duration rule δ·log(T) is, in their own words, "inevitably arbitrary" (§7.5). Adopting either is adopting an unlabelled constant | grid or Bayesian search over (r₀, δ) against a stated objective (e.g. delay at fixed ARL₀), with bootstrap CIs, on the project's own DGP |
| **TC-5** | finite-sample critical values for the chosen sequence statistic at the project's T, r₀, lag order and volatility structure | the operational critical values in both Phillips papers are simulated and therefore design-dependent; they do not transfer (§8.3) | Monte Carlo under the project's own null, with the replication count and the threshold divergence path both recorded as parameters, not conventions |
| **TC-6** | the null run-length distribution of a drawdown-threshold stopping rule | NB-08 derives the exact joint law of (τ_a, M_{τ_a}, Y_{τ_a}) but publishes no test; the assignment procedure is derivable and not published (§9.2) | instantiate **Theorem 1 (p.609)** and its spectrally-negative / Lévy corollaries (Corollary 2 p.610, Corollary 3 p.611) of [Landriault, Li & Zhang 2017](https://doi.org/10.1017/jpr.2017.20) for the project's price process; the derived law of τ_a is the ARL₀ the monitor needs. **The earlier "Theorem 3.1" reference was wrong** (round-3 re-read, L-20) |
| **TC-7** | size and delay of a *combined*-departure design | no record in the corpus evaluates any detector under more than two simultaneous departures from its stated null (§7.5) | factorial over {volatility path, error dependence, jumps, deterministic term}, at least 2×2×2×2, reporting size and delay jointly |

## 12. Limitations, certainty, verification gaps and conformance (items 15, 22, 23, 24)

### 12.1 Limitations of the evidence and of the review process (item 23)

Ordered by how much each could change a conclusion, most first. Each carries the
sections it affects.

**L-1 — Screening was one model, not two raters (PRISMA item 8, partial) — and
the model identity on the record is not the one this review first declared; see
L-15.** Screener A, screener B and the adjudicator are context-independent
sessions of a single base model, declared by the commit that carries their
verdict files as `claude-fable-5`. They share training, priors and failure
modes. κ = 0.433 with raw
agreement 0.807 measures between-session variance under an **unrecorded decoding
configuration**, **not** inter-rater reliability, and is not evidence of
independence; the sampling settings that would make the stage re-runnable to a
comparable κ are in no artifact (§2.5, VG-11). A systematic blind spot common
to the base model would be invisible to this design at every stage: it would
exclude the same records twice and adjudicate them out a third time. No human
screened any record. *Affects:* everything downstream of §3; most acutely the
1,410 stage-1 exclusions, which no human eye has seen.

**L-2 — The prescribed dual-extraction reconciliation did not run; the ER-RoB
profile is CONVENTION-RESOLVED, not source-adjudicated.** Protocol §4.3 requires
mismatches to be resolved against the source text and the mismatch count
reported. 90 of 357 comparable appraisal cells (25.2%) diverged between passes;
no reconciliation record exists; this document resolves them by the declared
conservative rule of §2.8 instead of against the sources. The appraisal in §6 is
therefore *direction-safe but not adjudicated*: where a `†` appears, the true
answer may be less concerning than shown, and cannot be less concerning than the
primary extractor's own record. **No concern profile from §6 or §6.1 may be
cited as an adjudicated appraisal**, here or downstream; the caveat is stated in
§6's header and repeated at every point of use in §7. Recorded as protocol
amendment A6. *Affects:* §6, §6.1 and every concern-profile qualification in §7.
*(Finding SCOPE-1-3.)*

**L-3 — Amendment A3 converted dual full-text assessment into single assessment
for 153 records.** For 21 of the 72 included records, exactly one screener ever
read the full text; the other exhausted its retrieval chain and returned X6. A3
is a defensible rule (X6 is an access outcome, not an eligibility judgment) but
its effect is that 29% of the corpus rests on one agent's full-text reading of
one document. *Affects:* §5.1, §5.4, and the four no-full-text records, all of
which are A3 includes.

**L-4 — 280 records (47.8% of those reaching full text) were excluded because
full text could not be obtained.** This is the largest single threat to
completeness and its direction is unknown: paywalled and repository-blocked
records are not a random sample of the literature, and the block pattern
correlates with publisher rather than with content. Nothing in this review can
bound the number of eligible studies lost this way. *Affects:* every coverage
statement in §6.1 and §7; the meta-analysis condition in §7.7 could in principle
be met by a pair inside the X6 set.

**L-5 — Backward citation-chasing did not run in the execution window; it ran
once after corpus freeze, through a weaker route, and named ONE record the
corpus does not contain — its second named candidate was a false positive.**
Protocol §3.3's `er-bc-*` arm is the only
supplementary method that recovers detectors the two seeds do not cite. It did
not run at the 2026-08-24/25 execution dates. It was executed 2026-09-02 as a
post-freeze recall diagnostic under amendment **A11**
([se-bc-01.json](search_logs/explosive-regime/se-bc-01.json), §2.2): 27 I2b
carriers targeted, **22 covered** (5 had no deposited reference list at Crossref
or OpenAlex), reference lists taken from **publisher-deposited metadata rather
than the source PDFs**, 392 unique referenced DOIs, 177 absent from the
1,996-record universe by DOI or exact normalised title, and **1 candidate
addition** — `er-bc-1` Hall, Psaradakis & Sola (1999), which passes S-a/S-b/S-c
on its deposited abstract. **It was not admitted**: the corpus is
frozen at 72 and this pass does not re-open it. The diagnostic was also
single-agent, with no second screener and no adjudication.

**The withdrawn second candidate, and what its withdrawal costs.** The arm also
named `er-bc-2` Banerjee, Chevillon & Kratz (2013) as absent from the universe
with eligibility "indeterminate at retrievable depth". It is not absent: the
work is `eru-0209` (2013 working paper, no DOI) and `eru-1027` (Econometrics
Journal 2020, doi:10.1093/ectj/utaa004) in the 1,996, both PROMOTE/PROMOTE at
stage 1 and both excluded at stage 2 (X7 and S-c-fail respectively, R2 X6,
terminal under A3). The claim that it was a recall gap is withdrawn (A12).
**This is not only a subtraction from the gap; it is an addition to it.** The
arm's absence test is DOI-or-exact-normalised-title, and here it was defeated by
a one-word title variant ("in a" vs "with a") on a record carrying no DOI. So
the "177 absent" figure is an upper bound on genuine absence with unquantified
looseness, and the arm's *negative* results — the 175 references it judged
uninteresting and the 6 named near-misses — carry the same weakness.

Combined with the
three known-item recall failures on the antecedent layer (§2.3), the corpus's
coverage of *pre-2011* methodological antecedents rests on the known-item list
plus one bounded, weakly-routed backward pass that already found a probable miss
on exactly that layer. **Concession stated symmetrically with L-4:** just as
§7.7's pooling condition "could in principle be met by a pair inside the X6
set", it could in principle be met by admitting `er-bc-1`, which is a
simulation study of periodically collapsing bubbles by a team non-overlapping
with `eru-0150` and `eru-0131` — the pair whose non-matching underwrites the
Evans-collapse power row. *Affects:* the competitor set's completeness; §7.8's
per-detector table may omit a detector line entirely; the O4 synthesis claim in
§7.4, the O2 claim in §7.2 and the §7.7 pooling outcome, each of which now
carries this bound at its point of use. *(Findings SCOPE-1-4, LITERATURE-2-1,
REV-2-6.)*

**L-6 — SEVEN included records fail criterion I3 as written.** `eru-0100`,
`eru-0112`, `eru-0154`, `eru-0268`, `eru-0427`, `eru-0904` and `eru-1310` have
no DOI, no arXiv ID and no Handle. The count is seven, not the five this review
first reported: 62 DOIs + 2 arXiv IDs + 1 Handle = 65 identified records out of
72. The two omitted from the first count are the twins `eru-0154` and
`eru-0904`; **a twin does not inherit its carrier's DOI for I3 purposes**,
because I3 is a property of the record and each twin is a distinct row in the
frozen set with its own store entry and its own contribution to every count
(§5.1, §5.3). I3 says such a record "is excluded and logged with its best
locator … not silently dropped"; all seven were included instead. The corpus is
frozen and this review does not re-screen it, so the discrepancy is recorded as
protocol amendment **A10(a)**, not repaired. Best locators (Semantic Scholar
`paperId`) are carried in the store, and all seven store entries now carry an
`I3 GAP` note. *Affects:* §5.1; two of the seven are also L-9 records and two are
also L-7 twins. *(Findings REV-1-2, SCOPE-1-5.)*

**L-7 — Three same-work twins survive in the frozen included set.** `eru-0622`,
`eru-0154` and `eru-0904` duplicate `eru-0675`, `eru-0126` and `eru-1526`
respectively (§5.3). Under X7 they should have been merged. Each is extracted
once, under its carrier, so **no operating characteristic in the §7 evidence
tables is double-counted** — but "72 records" is 69 distinct works, and any
downstream count over records overstates the corpus by three. **The narrower
assurance is the true one:** the record-level distributions in §4, §7.6 and
§10.2 *did* count these three works twice under codes inherited from their
carriers (O6 CS/CS/FS; two of the three PSY-lineage), and each of those three
sites now carries the distinct-work count beside the record count.
Recorded as protocol amendment **A10(b)**, corrected as to the scope of the
assurance by **A13**. *Affects:* every count in this document, which is why 69
is stated alongside 72 in the frontmatter, the abstract, the §4 table, the §6
header and §7.6, and why the three twins are excluded from every assessable
denominator in §6.1 and §7. *(Findings SCOPE-1-5, REV-2-3.)*

**L-8 — The meta-bias item-1 check is inconsistent with criterion X1.** Protocol
§8 asks whether the *application* literature cites the family's critical
evaluations, and specifies that the check run on the included corpus; X1 excludes
plain applications from that corpus by construction (109 of 234 substantive
exclusions). The check as designed cannot be run and was replaced by an
in-corpus uptake observation, declared as such (§10.1). *Affects:* §10.1.

**L-9 — Four included records were never read.** `eru-0112`, `eru-0749`,
`eru-1310`, `eru-1890`. No content is attributed to any of them anywhere in §6
or §7; one (`eru-1310`) has uncertain *identification*, not merely uncertain
content. *Affects:* §5.4 (enumerated), §7.5 (where `eru-1890`'s abstract-level
pointer is used and labelled).

**L-10 — FOUR records carry version or extraction-chain caveats.**
`eru-0150`'s journal version (which adds a CUSUM monitoring procedure) was
unobtainable and the 2009 working paper was extracted instead; `eru-0259`'s
journal version was unobtainable and its working-paper twin was extracted;
`eru-1715` was extracted through an intermediary summarisation of publisher HTML
and its numerals were never dual-checked; and **`eru-1289`** was tiered
"peer-reviewed chapter" from its DOI while the text actually extracted is Cowles
DP 2331 (2022) — the 2025 CUP chapter that DOI resolves to was never obtained,
so the tier was taken from a version that was not read. `eru-1289` is re-tiered
**working-paper**, and every claim it supports — the FWER triple **and the
dating-bias pair** — carries that tier wherever it is used. **Enumeration
extended round 3 (finding REV-3-4):** §7.4, the abstract's principal finding (4),
§7.8, §14, **and §7.3 (four of its thirteen dating rows, plus its tier line,
which previously asserted "peer-reviewed throughout")** and **§11 TC-2**. The
round-1 form of this enumeration omitted §7.3 and §11, which is how §7.3 came to
assert the opposite of the correction it was subject to. *Affects:* §7.1, §7.2,
§7.3, §7.4, §7.8 and §11 wherever those records are cited, each flagged at the
point of use. *(Findings LITERATURE-1-2, REV-3-4.)*

**L-11 — ER-RoB v1 is unvalidated and two of its questions are ambiguous.**
The instrument is a `CONVENTION` adapted from QUADAS-2 and PROBAST in form only.
Q7's three-disjunct wording and Q4's "collapse mechanism" wording produced 48 of
the 90 inter-pass divergences (§2.8). Domain concerns are ordinal judgments, not
measurements, and are not summable — no composite score is reported and none
should be constructed downstream. *Affects:* §6, §6.1.

**L-12 — The O6 coding scheme in §4.1 is this review's construction.** RT / CS /
FS / SPLIT is a synthesis-stage taxonomy applied to the extracted E8 text, not a
classification any source paper makes of itself. Where a source states the split
itself it is quoted (§7.6); where the code rests on this review's reading of the
E8 field, the record is codeable differently by a reader who weights "statistic
construction" over "evaluation design". The counts in §7.6 should be read as a
coarse partition, not a measurement.

**L-13 — A Crossref cross-check of all 62 DOI-bearing records surfaced
13 volume/issue/page discrepancies, not the two first reported.** The earlier
form of this limitation asserted that "two metadata discrepancies surfaced at
verification". That was an incomplete check reported as a complete one. The
check has now been run over **all 62 DOI-bearing included records** — every
record in the store carrying a DOI — comparing the extraction stage's E1
citation string (which §5 reproduces verbatim) against the Crossref work record,
field by field on container title, volume, issue and page range, on
2026-09-02. 62 of 62 records were retrieved from `api.crossref.org` on the first
or a retried attempt; none failed. *(Finding LITERATURE-1-4.)*

> **Scope correction, round 2 (findings QUANT-2-6, LITERATURE-2-4).** The earlier
> form of this paragraph said the comparison was made "field by field on
> container title, volume, issue, page range **and year**" and then closed the
> year dimension with a CONVENTION covering seven records. **The year field had
> not been checked across the 62.** It has been now, in both directions, and the
> result is in (e) below: 19 online/print divergences rather than 7, 22
> label-versus-store divergences, and a CONVENTION that the review's own labels
> contradict in 12 of the 19. L-13's round-1 defect was "a partial check reported
> as complete"; the round-1 remediation reproduced it on the year field alone.
>
> **Evidence is now archived, not just asserted (finding REPRODUCIBILITY-2-4).**
> The round-1 pass retained no machine-readable record of the 62 Crossref
> retrievals, so its 13 discrepancies were re-openable only by re-querying a
> mutable API. The full per-record result — DOI, HTTP status, attempt number,
> retrieved container title / volume / issue / page / `issued` /
> `published-online` / `published-print` / `created`, the store year, the review's
> display-label year, three derived divergence flags, and a **SHA-256 of the
> canonically serialised Crossref message** so a successor can detect drift — is
> at
> [se-crossref-recheck-01.json](search_logs/explosive-regime/se-crossref-recheck-01.json),
> SHA-256 `9457d3de7e3e3e60cc2b5832785b0b8b6da462153a627ddc69e29f72cd77ac9d`.
> The same log carries the 63 Handle-System resolutions (62 DOIs + 1 Handle, all
> `responseCode` 1) and the 2 arXiv resolutions that §12.3 and §15 assert.

**(a) Volume / issue / page discrepancies — 13 records.** In every row the
Crossref title matches the review's, so these are metadata errors in the
citation string, not misidentified records.

| record | DOI | review §5 / E1 citation | Crossref |
|---|---|---|---|
| `eru-0675` | 10.1016/j.econmod.2018.07.021 | *Economic Modelling* **73**:404–416 (2018) | *Economic Modelling* **80**:87–102 (2019) |
| `eru-0691` | 10.1111/sjpe.12179 | *Scottish J. Political Economy* **65(2)**:139–**162** | **66(1)**:139–**153** |
| `eru-0855` | 10.1109/ACCESS.2019.2893929 | *IEEE Access* 7:**32586–32596** | 7:**38356–38368** |
| `eru-1112` | 10.1093/jjfinec/nbab027 | *J. Financial Econometrics* **20(5)**:989–1063 | **21(4)**:989–1063 |
| `eru-1155` | 10.6339/JDS.201707_15(3).0007 | *J. Data Science* **16(3)**:495–508, labelled **2018** | **15(3)**:495–508, `published-online` **2021-03-08** (store also 2021; the label year 2018 matches no source — see (e4)) |
| `eru-1384` | 10.1093/jjfinec/nbac004 | *J. Financial Econometrics* 21(4):1282–**1314** | 21(4):1282–**1307** |
| `eru-1509` | 10.1515/snde-2022-0014 | *Studies in Nonlinear Dynamics & Econometrics* **28(2)**, no page range | **28(1)**:**25–37** |
| `eru-1580` | 10.1111/jtsa.12784 | *J. Time Series Analysis* **46(1)**:**102–132** | **46(5)**:**846–866** |
| `eru-1715` | 10.1111/jtsa.12768 | *J. Time Series Analysis* **46(1)**:**133–160** | **46(5)**:**945–965** |
| `eru-1761` | 10.1111/jtsa.70001 | *J. Time Series Analysis* (2025), no page range | **46(5):966–980** |
| `eru-1813` | 10.1016/j.eneco.2025.109095 | *Energy Economics* **149**:109095 (2025) | **154**:109095 (2026) |
| `eru-1852` | 10.1111/jtsa.12845 | *J. Time Series Analysis* 46(5):**828–847** | 46(5):**829–845** |
| `eru-1921` | 10.1017/S0266466626100383 | *Econometric Theory*, **1–30** | **1–29** |

The two substantial ones are `eru-1580` and `eru-1715`: both are cited with
issue 46(1) and a page range that belongs to neither record. `eru-0675`,
`eru-0855` and `eru-1112` are also substantial. The rest are off-by-one or
off-by-a-few page-range errors, or a page range the citation omits.

**(b) Records where the citation states "forthcoming"/no pagination and Crossref
now supplies it — 3 records, an update rather than an error.** `eru-1845`
*Econometric Theory* → 42(3):514–547; `eru-1890` *Oxford Bull. Econ. Stat.* →
87(5):880–898; `eru-1920` *Econometric Reviews* → pp. 1–35, still no volume.

**(c) Version/year misattribution — 1 record.** `eru-1289`: DOI
10.1017/9781108910095.003 resolves to a 2025 CUP chapter, pp. 30–59, while the
extracted text is Cowles DP 2331 (2022). Handled at L-10 and §7.4 as a tier
correction, not a page correction. *(Finding LITERATURE-1-2.)*

**(d) One record cannot be checked against Crossref.** `eru-0749`
(10.1093/jjfinec/nby023) has no volume, issue or page range in its Crossref
record, so the citation's *J. Financial Econometrics* 18(2):233–249 could not be
confirmed or refuted. It is a no-full-text record (L-9) in any case.

**(e) The YEAR field, checked across all 62 and reported in full — replacing the
seven-record note that stood here.** Three year fields exist per record and they
do not agree: the **display-label year** in the §5/§6 citation strings, the
**store `issued` year** in `references_explosive-regime.json`, and Crossref's
`published-online` / `published-print` / `issued`. All three were compared for
all 62 records on 2026-09-02; the per-record values and flags are in
[se-crossref-recheck-01.json](search_logs/explosive-regime/se-crossref-recheck-01.json).

**(e1) Online-versus-print year divergence: 19 records, not 7.**

| record | label | store | Crossref online | Crossref print | label follows |
|---|---|---|---|---|---|
| `eru-0150` | 2012 | 2011 | 2011 | 2012 | **print** |
| `eru-0238` | 2014 | 2013 | 2013 | 2014 | **print** |
| `eru-0348` | 2016 | 2015 | 2015 | 2016 | **print** |
| `eru-0559` | 2018 | 2017 | 2017 | 2018 | **print** |
| `eru-0597` | 2018 | 2017 | 2017 | 2018 | **print** |
| `eru-0689` | 2019 | 2018 | 2018 | 2019 | **print** |
| `eru-0691` | 2018 | 2018 | 2018 | 2019 | online |
| `eru-0748` | 2019 | 2018 | 2018 | 2019 | **print** |
| `eru-0891` | 2020 | 2019 | 2019 | 2020 | **print** |
| `eru-1044` | 2021 | 2020 | 2020 | 2021 | **print** |
| `eru-1112` | 2022 | 2021 | 2022 | 2023 | online |
| `eru-1117` | 2021 | 2021 | 2021 (2021-05-05) | **2023** (2023-01-19) | online |
| `eru-1260` | 2023 | 2022 | 2022 | 2023 | **print** |
| `eru-1384` | 2022 | 2022 | 2022 | 2023 | online |
| `eru-1509` | 2023 | 2023 | 2023 | 2024 | online |
| `eru-1580` | 2024 | 2024 | 2024 | 2025 | online |
| `eru-1604` | 2025 | 2024 | 2024 | 2025 | **print** |
| `eru-1715` | 2025 | 2024 | 2024 | 2025 | **print** |
| `eru-1845` | 2025 | 2025 | 2025 | 2026 | online |

**`eru-1117`'s print year is TWO years later, not one** — online 2021-05-05,
print 2023-01-19. The earlier text said "one later" for all seven it listed.

**(e2) The CONVENTION as declared is contradicted by the review's own labels in
12 of these 19.** The stated rule was "**the review dates a record by first
publication (online-first or working paper), not by issue year**". It holds for
the 7 records the earlier note listed (`eru-0691`, `eru-1112`, `eru-1117`,
`eru-1384`, `eru-1509`, `eru-1580`, `eru-1845`) and **fails for the other 12**,
where the display label is the print/issue year: `eru-0150`, `eru-0238`,
`eru-0348`, `eru-0559`, `eru-0597`, `eru-0689`, `eru-0748`, `eru-0891`,
`eru-1044`, `eru-1260`, `eru-1604`, `eru-1715`. The earlier note enumerated
exactly the compliant subset and omitted the non-compliant one. **The rule is
therefore restated as a description of intent that execution did not follow
uniformly, not as a convention the corpus obeys.** The corpus is frozen and the
labels are not renormalised; a consumer citing any of these 19 records should
take the year from the store plus this table, not from the §5 string.

**(e3) Display label versus store `issued` year: 22 of the 62 differ.** Thirteen
of the 22 are already in (e1)'s table (`eru-0150`, `eru-0238`, `eru-0348`,
`eru-0559`, `eru-0597`, `eru-0689`, `eru-0748`, `eru-0891`, `eru-1044`,
`eru-1112`, `eru-1260`, `eru-1604`, `eru-1715`). The remaining **nine** are
`eru-0259` (label 2016 / store 2014; Crossref print 2016,
created 2014-06-11), `eru-0463` (2017 / 2016; print 2017-01, created
2016-11-09), `eru-0513` (label "2017/2018" / store 2016; SSRN, no Crossref
online or print date, created 2021-11-17), `eru-0604` (label "2016/2017" / store
2017), `eru-0749` (2020 / 2018; online 2018-10-16, no print date — and the label
year matches neither), `eru-0889` (2020 / 2019; print 2020-03, created
2019-10-01), `eru-1155` (2018 / 2021), `eru-1394` (2023 / 2022; print 2023-01,
created 2022-12-22), `eru-1526` (2024 / 2023; print 2024-01, created
2023-12-05). In most of these the store carries the Crossref `created` (deposit)
year while the label carries the issue year.

**(e4) One label year matches nothing, and it belongs in (a).** `eru-1155`
(*Improved Test for Detecting Explosive Bubbles*,
`10.6339/JDS.201707_15(3).0007`) is labelled **2018** in §5 while the store says
2021, Crossref `published-online` and `issued` both say **2021-03-08**, and the
DOI slug encodes `201707`. No source supports 2018. It was already flagged in (a)
for its volume (16(3) → 15(3)); its **year** is added to that flag here.

**(e5) What this does and does not affect.** Nothing in §7 is located by year:
every extracted operating characteristic is cited by record id and by table or
equation number. The year errors affect citation strings and any downstream
bibliography built from §5 rather than from the CSL-JSON store. `eru-0675` and
`eru-1813` remain in (a) rather than here — Crossref records no online-first date
for either, so their years are simply wrong, not convention-driven.

**What is not fixed.** The §5 corpus table still reproduces the extraction
stage's citation strings verbatim rather than silently normalising them, because
§5 is a record of what the extraction stage produced; the corrections live here,
in one place, with the Crossref values beside them. None of the 13 discrepancies
affects any extracted operating characteristic: every number in §7 is located by
table or equation, not by page. The CSL-JSON store carries no `page` field for
these records, so §5's page ranges rest solely on the E1 strings and on this
table.

**L-15 — The automation tool's identity differs between the review's own
declaration and the repository's provenance record, and the logs cannot resolve
it (PRISMA item 8).** This review as first delivered declared `claude-opus-5` as
the base model for every stage. The repository's provenance trailers say
otherwise for the stages that produced the verdict and extraction files.
Reconciled per stage against the commit that carries each artifact:

| stage | artifacts | carrier commit | `AI-Assistance` trailer |
|---|---|---|---|
| protocol registration | `protocol_explosive-regime-review_2026-08-24.md` (frontmatter also names "Claude Fable 5") | `9deee0c` | `claude-fable-5 (role=multi)` |
| search execution, dedup | 42 query logs, `se-dedup-ledger.json`, candidate store | `8aeebfe` | `claude-fable-5 (role=multi)` |
| stage-1 and stage-2 screening, both blind adjudications | `screen-verdicts-R1/R2/ADJ.jsonl`, `screen2-verdicts-R1/R2/ADJ.jsonl` | `8aeebfe` | `claude-fable-5 (role=multi)` |
| primary extraction; NB adjudications | `se-extraction-primary.jsonl`, `se-nb-adjudications.json` | `8aeebfe` | `claude-fable-5 (role=multi)` |
| independent numeric re-extraction | `se-extraction-recheck.jsonl` | **none — untracked at the time of writing** | **no trailer exists; the model identity for this pass is unrecorded** |
| synthesis, appraisal resolution, §8/§9 write-up, this document | this review, `references_explosive-regime.json`, `se-bc-01.json` | delivered by the current session | `claude-opus-5` |

**This is not resolved by papering over it.** The ReproLog cited by `8aeebfe`
(`repro_log_f5419aa650e249378ff40828424696bb.json`) carries **no model field** —
the 13-field ReproLog schema has `model_hash`, which is `null`, and no model-id
field at all — so the conflict cannot be adjudicated from the logs. Two readings
are consistent with the evidence and this review cannot choose between them:
either the screening and extraction stages genuinely ran under a different base
model than the synthesis stage, or the trailers on `9deee0c`/`8aeebfe` are
mislabelled. **What is recorded is the trailer**, and the trailer is the only
clone-durable carrier, so the trailer is what this review now declares, per
stage, in its frontmatter and its AI-assistance statement.

**Consequence for κ.** κ = 0.433 was described as measuring "decoding-and-context
variance between two context-independent sessions of the same base model". The
*stage* attribution survives, because both screeners and the adjudicator sit in
the same commit under the same trailer: whatever model ran stage 1, it ran both
sessions. What does **not** survive is any implication that κ characterises the
model that wrote the synthesis. If the stages did run under different models, κ
is a property of the screening stage and says nothing about the synthesis
model's reading of the same records — and the independent re-extraction, whose
model is unrecorded, may not even be the same model as the primary extraction it
is supposed to check, which would make the 90/357 divergence rate of §2.8 partly
a between-model quantity rather than a within-model one.

**And the word "decoding" does not survive either.** Calling κ a *decoding*
variance asserts a mechanism, and the mechanism is untestable from this record:
**the screening sessions' decoding configuration is recorded in no artifact** —
`er-screening-prompt.txt` fixes the prompt and nothing else; the verdict JSONLs
carry verdict, criterion and note only; neither ReproLog has a sampling-parameter
field. Temperature, top-p, max-tokens, thinking budget and seed are therefore
unknown, the stage cannot be re-run to a comparable κ, and the observed variance
cannot be apportioned between decoding stochasticity, context ordering and
prompt-position effects. κ is restated throughout as **between-session variance
of the screening stage under an unrecorded decoding configuration** (§2.5, §3.3,
abstract, §15). The missing settings are not recoverable — no dispatch record
survives in the repository — so this is a named unclosable gap, not a to-do.
Recorded as verification gap **VG-11**. *(Finding REPRODUCIBILITY-2-3.)*
*(Finding QUANT-1-3.)*

**L-16 — NARROWED. The §8 and §9 primary texts have all been re-fetched and
digested, and their quotations and numbers re-verified; what remains unverifiable
is version identity between the 2026-08 and 2026-09 retrievals.** The earlier
form of this limitation said the three Phillips reprints and Cowles DP 2331
"could not be re-fetched — the Cowles reprint host that served them at extraction
did not respond" and concluded that §8.3's verdict and §7.4's FWER triple "cannot
presently be re-opened". **That conclusion was wrong and is withdrawn.** The
round-1 pass attempted `korora.econ.yale.edu` over HTTPS only; the host refuses
TCP on port 443 and serves all three reprints over plain HTTP on port 80, and
Cowles DP 2331 is served over HTTPS at its direct file path. All seven §9.5 texts
were retrieved on 2026-09-02, per-attempt evidence archived at
[se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json),
digests in the §9.5 table.

What that buys: every quoted string in §7.6, §8.1, §8.2 and §8.3 verified
verbatim against the retrieved text; every reported number verified, including
`eru-1289`'s FWER triple 0.55 / 0.78 / 0.93 (DP 2331 Table 1, p.20) and its
7.56 → 12.20-month origination bias (Table 2, p.21). §8.3's confirm-or-correct
verdict and §7.4's FWER triple are therefore **no longer single-session
transcriptions**; they have been read twice, in two sessions, from files whose
digests are on the record.

What it does not buy, and what VG-10 is now narrowed to: **no digest was taken
at extraction time**, so this review cannot prove that the files retrieved in
2026-09 are the files read in 2026-08 — only that the quoted content is present
in the files now served at the recorded URLs. And the re-read found that the
locators were not right: **nineteen** page references were wrong, corrected in
L-18 (round 2 reported that count as "fourteen"; see the recount box in L-18,
LITERATURE-3-3).

**Round 3 closes the NB residue.** Round 2 left the three §9 NB texts re-fetched
but not re-read, and carried that as a residue inside VG-10 at `minor` — the same
gap whose stated ground for downgrade was a re-read that did not cover it. Round
3 re-read all three against a third fetch: fourteen quoted strings verify
verbatim, four locators were wrong or loose and one result was misattributed, all
corrected and tabulated in **L-20**. VG-10 is now **only** the version-identity
residue; the §9 transcription risk is discharged, not carried at a severity that
understated it. *(Findings QUANT-1-7, LITERATURE-2-2, QUANT-2-4, QUANT-2-3,
REV-3-5, QUANT-3-4.)*

**L-18 — NINETEEN page locators in §7, §8 and the §9.5 provenance table were
wrong; corrected here against the retrieved texts.** The quoted strings and the
extracted numbers were right; the page attributions were not, and §9.5 exists
precisely so a successor can re-open the quoted page, so wrong locators defeated
its purpose.

> **Count corrected, round 3 (finding LITERATURE-3-3).** Round 2 published this
> finding under the headline "**fourteen** page locators", and repeated that
> figure at seven sites in this review and once in the consumer agenda. **The
> table below has always carried nineteen corrected rows plus one row that
> supplied locators where none had been given** — nine for PWY 2011, seven for
> PSY 2015a, three for PSY 2015b, and the `eru-1289` row that added p.20/p.21.
> A recount of the table under every counting rule tried (rows, distinct old
> page numbers, distinct new page numbers) yields **19**; no rule reproduces 14,
> so "fourteen" is withdrawn as a plain miscount rather than reinterpreted. The
> corrections themselves were all applied in the body text and are unaffected;
> only the headline count was wrong, and it was wrong in the *under*-reporting
> direction. Every site that carried "fourteen" now carries **nineteen**. The
> consumer agenda's copy of the figure is a consumer-side correction this
> document does not make; it is listed in §14.

The errors are almost all **+1** — one page later than the true page — but the
offset is not universal, so this is transcription error rather than a pagination
convention. Locators that were **already correct** and are not in the table:
PWY's Table 3 Panel A note, PSY 2015a's fn. 4 (p.1046) and fn. 9 (p.1050), and
PSY 2015b's simulation-section locators at pp.1092 and 1093 and its Table 4
(p.1092). **The round-2 form of this sentence also named "PWY's Table 4 (p.221)"
and "all of PSY 2015b's simulation-section locators (pp.1090, …)" as already
correct while listing both as changed rows below — a narrowing of `pp.221–222`
to `p.221`, and of `pp.1090–1091` to `p.1090`, is a correction, not a locator
that was already right. The sentence is fixed here (LITERATURE-3-3).**

| text | item | as published (old) | verified (new) |
|---|---|---|---|
| PWY 2011 (`eru-0131`) | eq. (8) date-stamp rule; ADF_r limit; fn. 6 normality; cv_adf = log(log(ns))/100 and the "around the 4% significance level" gloss | p.208 | **p.207** |
| | mildly-explosive model (9), no intercept | p.209 | **p.208** |
| | eq. (13), asymptotic no-false-detection | p.211 | **p.210** |
| | fn. 10 minimum duration; condition (20) | p.213 | **p.212** |
| | Table 1 and its note (r₀ = 0.10; Monte Carlo 10,000 reps) | p.214 | **p.213** |
| | 0.013–0.018 for n = 389; "sup ADF_r cannot reveal the location of the exuberance" | p.215 | **p.214** |
| | fn. 14 window alternatives 60/120; N = 77 | p.216 | **p.215** |
| | Table 3 Panel A (size 0.049 at g = 0.00) | p.220 | **p.219** |
| | Table 4 (Evans-model power) | pp.221–222 | **p.221** (Appendix **pp.222–224** — the range `pp.222–225` published at round 3 was itself wrong; the Appendix opens on p.222 and ends on p.224, where REFERENCES begin; corrected round 4, L-21) |
| PSY 2015a (`eru-0393`) | eq. (3) null | p.1048 | **p.1047** |
| | Table 1 and its note ("2000 replications") | p.1051 | **p.1050** |
| | fn. 10 "inevitably arbitrary"; α_T fixed at 0.05 | p.1053 | **p.1052** |
| | **"…ex ante real-time dating procedure, whereas the GSADF test is an ex post statistic"** | p.1054 | **p.1053** |
| | consistency results (i)–(iii) and the misdating limit | p.1057 | **pp.1056–1057** |
| | fn. 23 sequential-PWY re-initialisation; Chu et al. monitoring bound | p.1063 | **p.1062** |
| | "(pseudo) real-time"; BSADF vs 95% SADF CV; 1917 / 2009 crash flags | p.1067 | **p.1066** |
| PSY 2015b (`eru-0395`) | eq. (1) null; fn. 5 Gauss/Matlab | p.1082 | **p.1081** |
| | eq. (3) fitted regression; I_r = {1,…,⌊Tr⌋} | p.1083 | **p.1082** |
| | delay 0.05→0.03 and 0.04→0.06 | pp.1090–1091 | **p.1090** |
| `eru-1289` (Cowles DP 2331) | Table 1 FWER triple; Table 2 origination bias | (no locator given) | **p.20**, **p.21** |

**One quotation was also mis-marked.** §8.1 gave `"the asymptotics do not require
normality"` inside quotation marks; PWY fn. 6 reads "The asymptotic theory
developed below does not require the normality assumption, whereas the bias
correction explained later does use the distributional assumption". The full
sentence now appears in its place.

**One number was also mis-summarised.** §8.2's E9 cell gave PSY 2015a's
lag-overspecification size distortion as "up to 0.697/0.401". Table 2 (p.1058)
pairs SADF and GSADF row-wise across four lag rules; 0.697 is the GSADF
significance-test-`kmax = 6` figure at T = 100 (the authors' own highlighted
case, alongside SADF 0.145) and 0.401 is the GSADF fixed-lag `k = 6` figure at
T = 400 — two unrelated cells, and the table's actual maximum, **GSADF 0.787 at
fixed lag k = 6, T = 100**, was omitted. Restated at its site. The ten k = 0
figures §7.1 reports from the same table verify cell for cell.

**One substantive mislabel in §7.4's FWER table.** The second row read "same,
longer span / higher frequency". DP 2331 §5.2 generates all three cells "over a
10-year period with sampling frequencies of quarterly, monthly, and weekly (i.e.,
T = {40, 120, 520})" — the span is the same in all three; only the frequency
changes. Corrected. The third row said "delay cost of the max-over-window
bootstrap fix … origination delay 7.56 → 12.20 months"; DP 2331 Table 2 reports
these as the **mean bias in the estimated bubble origination date** in months,
at successful-detection rates 0.84 and 0.75 respectively. Corrected.

**L-18 is scoped to the four Phillips-line texts.** The three §9 NB texts were
re-read in round 3; their four locator corrections and one result misattribution
are in **L-20**, kept separate so the two counts never merge.

**Two of these corrections propagate outside this review.** The
`p.1054 → p.1053` locator on the "ex ante real-time … ex post statistic"
quotation appears in the consumer agenda
([research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md)),
as does the prescribed Rev 4 wording in §8.3 that carries it. Correcting the
agenda is a consumer-side action under protocol §9.1(i) and is **not** made by
this document. *(Finding QUANT-2-3.)*

**L-19 — The `eru-1289` dating figures were labelled as the wrong quantity, and
attributed to the wrong table, at four sites round 2 did not reach.** Round 2
established from the retrieved DP 2331 that 7.56 and 12.20 are the **mean bias in
the estimated bubble origination date**, in months, at successful-detection rates
0.84 and 0.75, reported in **Table 2 on p.21** — and corrected §7.4, §9.5, §14
and L-18 accordingly. Four sites were left on the withdrawn label: §7.3's two
table rows and its prose called them "PSY origination delay" **and cited
`eru-1289` Table 1**, which is the FWER table on p.20; §7.8's BSADF row and §11's
TC-2 repeated "origination delay". The successful-detection-rate cost that the
corrected form carries (0.84 → 0.75) was absent from all four, so a consumer
reading §7.3 — the section that calls this "the single most consumer-relevant
number in the corpus" — got a delay figure with its paired accuracy cost stripped
out and a wrong table reference on top. All four are corrected, and §17's
assurance that no number was changed at one site only is corrected with them.

**Re-verified directly, not inherited from round 2.** DP 2331 was re-fetched on
2026-09-02 (round 3) from `https://cowles.yale.edu/sites/default/files/2022-08/d2331_0.pdf`;
the file is 591,865 bytes with SHA-256 `309a38ae13210f56f81db2a871b428a56cad99547966a9d4e1418d9c40e4167e`,
byte-identical to the round-2 digest in §9.5. Read off that file:

- **Table 1**, printed **p.20** (PDF page 21): "Table 1: The family wise error
  rates of the PSY procedure"; PSY (standard) 0.55 / 0.78 / 0.93 across
  quarterly T = 40, monthly T = 120, weekly T = 520; PSY (multiple) 0.04 / 0.06 /
  0.05.
- **Table 2**, printed **p.21** (PDF page 22): "Table 2: The successful detection
  rates and the biases of the estimated bubble origination and collasping dates
  [*sic*]"; at T = 120, PSY (standard) SDR **0.84**, origination **7.56 (4.99)**,
  collapse **0.79 (1.72)**; PSY (multiple) SDR **0.75**, origination
  **12.20 (5.33)**, collapse **0.77 (1.71)**.
- The §5.2 text states the trade-off in the authors' own words: "the succesful
  [*sic*] detection rate of PSY (multiple) is lower (75% versus 84%) and the bias
  in the estimated bubble origination date is larger (12.20 months versus 7.56
  months)". The same section defines the quantity as an *averaged delay*,
  `(1/M)Σ(t̂ₑ⁽ᵐ⁾ − tₑ)`, so "delay" and "bias" are the paper's two names for one
  statistic; this review standardises on "mean bias in the estimated date"
  because that phrasing keeps the SDR cost attached.
- Simulation design confirmed: data generated "over a 10-year period" with
  M = 2,000 replications.

**Two further errors surfaced on that re-read, and are corrected here.**
(i) §7.3's FWER-controlled collapse-date row gave the standard deviation as
**1.72**; DP 2331 Table 2 gives **1.71** for that cell (1.72 is the *standard*-CV
row). (ii) §7.3 described the FWER-controlled critical values as a
"multiple-window bootstrap". DP 2331 §5.1 constructs them by simulating
`max_s PSY_s` over a control window from the null model xₜ = xₜ₋₁ + εₜ and taking
the 95th percentile, and says only that the approach is "in the same spirit as
bootstrapping methods"; it is a simulated max-statistic critical value, and the
control window here is T_w = T — one window, not multiple. Relabelled.
*(Findings REV-3-3, QUANT-3-3, REV-3-4.)*

**L-20 — The three §9 NB texts have now been re-read; four locators were wrong
or loose and one result was misattributed.** Round 2 re-fetched NB-02, NB-08 and
NB-13 but did not re-read them, and carried that as a residue inside VG-10 at
`minor`. Round 3 fetched all three a third time — digests byte-identical to
rounds 1 and 2 (`d8ae7e69…`, `87277984…`, `9e38c956…`) — and read every quoted
string and every page locator against the retrieved files.

**What verified.** All fourteen strings quoted from the three adjudicated texts
verify **verbatim**: five in §9.1, four in §9.2, five in §9.3. Every §9 verdict
and every eligibility judgment is unaffected. §9.1's and §9.3's assertions that
no autoregressive root ρ > 1 appears in either paper verify mechanically — the
strings "explosive", "unit root" and "autoregressive" occur zero times in either
full text.

**What did not.**

| text | item | as published (old) | verified (new) |
|---|---|---|---|
| NB-02 (arXiv:cond-mat/0010050v2) | "we shall take the stretched exponential law as our null hypothesis" (§1) | p.1 | **p.2** |
| | "…we have reshuffled the daily returns 1000 times…" (§5) | p.8 | **p.9** |
| | "The third column gives the number of drawdowns above the threshold…" (§5) | p.8 | **p.9** |
| | §6 item 6, "The remaining 1–2%…" | pp.9–10 | **p.10** (the numbered list runs pp.9–10; item 6 falls wholly on p.10) |
| NB-13 (IIIS DP 122) | "…not based on a priori defined crisis periods … but on an a posteriori analysis…" (§2) | pp.4–5 | **p.5** (§2 opens on p.4) |
| NB-08 (*J. Appl. Prob.* 54) | the theorem from which the drawdown stopping-time law is derived | "Theorem 3.1" | **Theorem 1, p.609** (with Corollary 2 p.610, Corollary 3 p.611) |

The NB-08 row is a **result misattribution, not a page error**, and it is the
more consequential of the two kinds: the paper numbers its results sequentially
rather than by section, and the only occurrence of the string "Theorem 3.1" in
its text is a citation to another paper's theorem (reference [23], p.613). A
successor following the old reference would have landed on someone else's
result. Corrected at §9.2, §9.5 and TC-6. NB-08's own page locators (p.603,
p.604 ×2, p.605) verified exactly as published, and NB-13's p.2, p.6 and p.14
locators verified exactly.

**Pagination conventions, recorded so a successor need not rediscover them.**
NB-02's arXiv v2: printed page = PDF page − 2. NB-08: PDF page 1 = printed
p.603. NB-13's DP 122: printed page = PDF page − 3.

**What this re-read does NOT cover, stated because no further audit round will
check it.** One sentence quoted in §9.3 — "We propose a definition and a test for
flight-to-quality, flight-from-quality and cross-asset contagion" — is attributed
to the *journal/SSRN-2008 abstract*, not to DP 122, and the journal text was
never obtained (VG-3). It remains an unverified single-session transcription.
Page locators for the §9.3 regression-table notes were absent and have been
supplied (pp.19, 24). *(Findings REV-3-5, QUANT-3-4.)*

**L-21 — Round-4 targeted verification of the LOAD-BEARING locator set only;
six error sites found, six load-bearing texts unreachable.** This pass is **not** a
sweep of the corpus. Its scope was fixed before any source was opened and is
stated here so the boundary is auditable: an item is load-bearing iff it is a
page locator, table/theorem/equation/footnote identifier, or a quoted string
that appears **inside §7's synthesis prose** — the §7.1–§7.6 "Synthesis claim"
paragraphs, the `TO COMPUTE` handoff paragraphs, the §7.2–§7.4 lead-in
paragraphs those claims rest on, §7.6's three causality traps, §7.7's
pooling-failure rows and §7.8's per-detector rows — **or** is cited by
[research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md).
**Rows of §7's evidence tables that no synthesis paragraph re-cites are
inventory, not load-bearing, and were deliberately NOT verified.** The
load-bearing set is **50 items over 21 records** — 20 of the frozen 72 plus
NB-08, which §9.0 adjudicates outside the corpus. Verdicts: **35 verified,
7 corrected, 8 unverifiable.** Verification log:
[se-verify-loadbearing-01.json](search_logs/explosive-regime/se-verify-loadbearing-01.json).

**Against the corpus: 14 of the 72 records have now been read at full text at
some verification round — the four Phillips-line records before this pass
(`eru-0131`, `eru-0393`, `eru-0395`, `eru-1289`) and ten added here
(`eru-1044`, `eru-1852`, `eru-1921`, `eru-1845`, `eru-1844`, `eru-0889`,
`eru-1038`, `eru-1716`, `eru-1519`, `eru-1031`), several of the ten at their
load-bearing points only and three of them in a working-paper, preprint or
accepted-manuscript version rather than the version their DOI names.
Fifty-eight have not been read at any verification round.** Every number in
this review outside the 50-item set above rests on a single-session extraction
transcription that no round has re-opened, and the error rate measured on
re-read texts across rounds 2, 3 and 4 gives no ground for assuming otherwise.

**What this pass corrected.**

| § | item | as published (old) | verified (new) |
|---|---|---|---|
| §7.2 | PWY's Evans-model appendix | Appendix `pp.222–225` | **pp.222–224** — the Appendix opens on p.222 and ends on p.224, where REFERENCES begin. The `pp.222–225` form was introduced by the round-3 L-18 table itself |
| §7.7 pooling row | `eru-0131`'s Evans-collapse power design | `n = 120`, "different scaling", verdict resting on "different scaling, different sample size" | **T = 100** and **bubble scaled ×20** (Pₜ = Pᶠₜ + 20Bₜ), Table 4 note p.221. `n = 120` is PWY's **Table 3**, the non-collapsing design. Both stated grounds for the no-match verdict are withdrawn; "different tests" survives, and no matched cell is asserted either way because `eru-0150` is still unobtained |
| §7.1, §7.8 | `eru-1716` classical PWY size under the Heston null | `0.048–0.282` | **0.048–0.392** — the nominal-5% PWY column of Table 1 runs 0.048 (a = 0.25, c = 0.06) to 0.392 (a = 0.01, c = 1.5); the old range stopped at the c = 0.3 column |
| §7.4 surveillance table | `eru-1519`'s crash monitor | "crash monitor never signals before the crash by construction" | **contradicted by the source.** SMIN(m,n)'s FPR has no closed form; it is *bounded* by AMAX(k)'s FPR (under H₀) or true-positive rate (under H₁,₁) at the detection time, and the authors state further theoretical analysis "is not possible" and measure it by simulation |
| §7.4 surveillance table, §7.8 | `eru-0889` / `eru-1038` weighted-boundary CUSUM row | boundary "g(M,k)(1+k/M)(k/(k+M))^γ"; both called **open-ended**; "γ = 0.35 adopted as the compromise" for both | the boundary is **g(M,s) = c·M^{1/2}(1 + s/M)(s/(M+s))^γ** (`eru-1038` eq. 2.8); `eru-0889` is **explicitly closed-ended** — "we consider here closed-ended procedures in which we stop the detection procedure after observing T observations" — and its boundary carries an extra c(1 + d₀M^{−τ}) factor and a general f(·); γ = 0.35 is **`eru-0889`'s** choice, while **`eru-1038` recommends γ = .45**. Three errors in one cell |
| §7.5 | the PWY-inconsistency result in `eru-0395` | "Theorems 4–5" | **Theorems 4–5 pp.1086–1087** carry the DF/BSDF *limit behaviour*; the *inconsistency* is **Theorems 6–7 p.1088**. Same class of error as L-20's NB-08 row: a result attributed to the wrong numbered theorem |

**What re-verified unchanged.** All four Phillips-line digests reproduced
byte-identical on a **fourth** independent fetch (`a35fac94…`, `dfd19565…`,
`85a984e9…`, `309a38ae…`), as did NB-08 (`87277984…`). Every L-18 locator this
pass re-opened held: PWY p.207 (eq. (8), the cv rule, "around the 4%
significance level", fn. 6), p.210 (eq. (13)), p.213 (Table 1 note, r₀ = 0.10,
10,000 reps), p.214 (the "cannot reveal the location" quotation), p.219 (Table 3
Panel A, 0.049 at g = 0.00, n = 120, 10,000 reps), p.221 (Table 4); PSY 2015a
p.1050 (Table 1 note, 2,000 reps; the r₀ = 0.01 + 1.8/√T rule and its "extensive
simulation" ground), p.1052 (fn. 10 "inevitably arbitrary"), p.1053 (the ex
ante / ex post quotation, verbatim), p.1058 (Table 2 — all ten k = 0 cells, the
0.184/0.787 fixed-k = 6 pair, the 0.145/0.697 significance-test pair, the 5,000
replications, and the "size is reasonably well controlled when a small fixed lag
length is used in the recursive tests" sentence); PSY 2015b pp.1085/1088
(Theorems 2–3 and 8 and their rate conditions), pp.1090–1095 (Tables 1–10; the
0.45/0.46/0.55 dating cells at α = 0.6), p.1092 (Table 4, T = 100/200/400);
DP 2331 p.20 (Table 1, FWER 0.55/0.78/0.93 at T = 40/120/520 over one 10-year
span, M = 2,000) and p.21 (Table 2, 7.56 (4.99) → 12.20 (5.33) at SDR
0.84 → 0.75, collapse 0.79 (1.72) → 0.77 (1.71)); NB-08 Theorem 1 p.609,
Corollary 2 p.610, Corollary 3 p.611, and the "Theorem 3.1" string on p.613 as a
citation to reference [23]. Newly verified at full text and unchanged:
`eru-1044` Tables 2 and 4, `eru-1852` Table 3, `eru-1921`'s t = 241 / b = 0.1395
/ 0.1679 calibration, `eru-1844`'s Theorem 1, `eru-1845`'s Darling–Erdős and
open/closed-ended size control, `eru-0889`'s "As a compromise, we use γ = 0.35",
and `eru-1031`'s "Using the full sample period" (in the Cowles DP 2152 twin —
the Handbook chapter itself is still unobtained).

**What this pass could NOT reach, with the failure mode per host.** Six
load-bearing records: `eru-0150` (Homm & Breitung — publisher closed, no OA
deposit; the June 2009 Bonn working paper the extraction used is no longer
served at the recorded path), `eru-0348` (Sollis — De Gruyter returns HTTP 202
with an empty body; the Newcastle ePrints record has no deposited file),
`eru-0559` (Phillips & Shi — Southampton ePrints returns HTTP 401 on both http
and https; the SMU deposit returns a 212-byte stub), `eru-0238` (PSY 2014 — no
OA location in OpenAlex; no Cowles reprint found under the Phillips article
index), `eru-0735` (Astill et al. 2018) and `eru-1117` (Astill et al. 2021 —
OUP returns HTTP 403 to every user agent tried; the Nottingham repository
returns HTTP 403). Every attempt is recorded per host and per scheme in the
verification log. Consequences carried at their sites: §7.1's drift-break
exception (`eru-0348`, the ground for TC-1 being two-sided) is **still
single-session transcription**; §7.2's Evans π-grid table and §7.7's pooling
verdict on that characteristic depend on `eru-0150`, unread twice now; §7.3's
`eru-0559` reverse-regression bias rows, §7.6's causality trap 2, and two rows
of the §7.4 surveillance table (`eru-0735`, `eru-1117`, including the
`b = 0.147 / 0.177` constants and the "eq. 5" locator) are **unverified**.
Verification gap **VG-17**. *(Round 4, 2026-09-03.)*

**L-17 — Three protocol-mandated records never entered the screened universe.**
Protocol §9.1 requires NB-02, NB-08 and NB-13 to be force-screened into the
record universe regardless of query recall. They were not (§3.1, §9.0, amendment
A9): the identification count 4,898 and the universe 1,996 exclude all three,
and no screening verdict citing a criterion identifier exists for any of them.
Their §9 verdicts are unaffected in substance — all three fail S-a, S-b and S-c
on full text — but the dual-screening audit trail the protocol requires for them
does not exist. Verification gap **VG-9**. *(Finding SCOPE-1-1.)*

**L-14 — Certainty in cumulative evidence is not GRADE.** Protocol §9.2 declares
GRADE inapplicable in its scored form (it is built for effect estimates on health
outcomes) and substitutes, per synthesis claim: the evidence tier of the
supporting records, their ER-RoB v1 concern profile (convention-resolved, not
source-adjudicated — L-2, A6), and their causality status.
That substitute is what §7 carries inline. It is weaker than GRADE in one
specific way worth naming: it has no mechanism for downgrading on *imprecision*,
because the corpus reports almost no Monte Carlo standard errors.

### 12.2 Defects found in the frozen protocol itself

Recorded for a successor protocol; none of them was acted on by editing frozen
text.

| id | defect |
|---|---|
| **I-1** | §4.2's stage-2 rule did not anticipate differential full-text obtainability. Repaired in execution by amendment A3, at the cost documented in L-3. |
| **I-2** | §8 item 1's citation-uptake check presupposes an application stream that §2.3 X1 excludes (L-8). |
| **I-3** | ER-RoB v1 Q4 and Q7 are ambiguous enough to produce a 25% inter-pass divergence rate (L-11). Q7 should be split into "asymptotic control stated" and "finite-sample family-wise rate reported"; Q4 should name the collapse mechanisms that count. |
| **I-4** | The stage-1 exclusion-code taxonomy overlaps: X4 (changepoint detector without explosivity alternative) and S-a fail (alternative not explosive) name the same records, and the two screeners split them differently (§3.4). No decision was affected, but the code counts are not comparable across screeners. |
| **I-5** | §3.5's known-item recall check has no remedy attached. Three items failed it and the protocol prescribes only that the failure be reported — which is done — but a failed PRESS check would normally trigger a strategy revision, and no revision path exists in the frozen text. |
| **I-6** | §4.3 requires a mismatch count to be reported but names no artifact to write it to, which is how the reconciliation came to be skipped without leaving a hole anyone could see (L-2). |

### 12.3 Verification gaps

| id | severity | gap |
|---|---|---|
| **VG-1** | major | Four included records were never read at full text: `eru-0112`, `eru-0749`, `eru-1310`, `eru-1890` (§5.4). |
| **VG-2** | major | 280 records were excluded at full text solely because the text could not be obtained (§3.5, L-4). |
| **VG-3** | major | NB-13's journal version was not obtained after four attempts; the adjudication rests on the IIIS DP 122 working-paper twin plus the journal abstract, and the verdict is explicitly re-openable under protocol §10 if the journal text surfaces (§9.3). **The scope qualifier that carries this — "provisional on the working-paper twin" — is not in protocol §9.1's frozen verdict vocabulary and is registered as amendment A13(c); the protocol leaves `indeterminate-from-full-text` undefined, so the reason for preferring the qualified `episode-statistic-null` rests on a declared CONVENTION of §9.3 rather than on protocol text** (REV-2-4, LITERATURE-2-6). |
| **VG-4** | major | Backward citation-chasing (`er-bc-*`) did not run in the execution window. Executed 2026-09-02 as a post-freeze recall diagnostic under amendment A11 ([se-bc-01.json](search_logs/explosive-regime/se-bc-01.json)): 22 of 27 I2b carriers covered, reference lists from publisher-deposited metadata rather than source PDFs, single-agent hand-check with no second screener. It surfaced **1** candidate addition (`er-bc-1` Hall, Psaradakis & Sola 1999), **not** admitted, because the corpus is frozen at 72. Its second named candidate `er-bc-2` (Banerjee, Chevillon & Kratz 2013) was a **false positive**: that work is in the universe as `eru-0209`/`eru-1027`, was dual-screened at both stages and excluded X7 / S-c-fail, so it is not a recall gap (A12, LITERATURE-2-1). That failure also bounds the arm's own absence test — DOI or exact normalised title, defeated here by a one-word title variant — so "177 referenced DOIs absent from the universe" is an upper bound on genuine absence with unquantified looseness, and the arm's negative results carry the same weakness. The gap is now bounded and named rather than unbounded, but it is not closed (§2.2, L-5). |
| **VG-5** | minor | The optional SSRN site-search supplementary arm was not run; protocol §3.1 requires the absence to be recorded, which this discharges (§2.2). |
| **VG-6** | minor | `eru-0150` (the canonical third-party comparison study), `eru-0259` and **`eru-1289`** were extracted from working-paper versions, not from the published versions their DOIs resolve to; `eru-0150`'s published CUSUM monitoring section is therefore not in the corpus (§5.4), and `eru-1289`'s 2025 CUP chapter was never obtained, so its FWER measurement is working-paper tier (§7.4, L-10). |
| **VG-7** | minor | `eru-1715` was extracted through an intermediary summarisation of publisher HTML and never dual-checked (§5.4). |
| **VG-8** | minor | **Seven** included records have no persistent identifier of any protocol-accepted type — `eru-0100`, `eru-0112`, `eru-0154`, `eru-0268`, `eru-0427`, `eru-0904`, `eru-1310`. Not five: the twins `eru-0154` and `eru-0904` do not inherit their carriers' DOIs, because I3 is a property of the record (§5.1, §5.3, L-6, amendment A10(a)). |
| **VG-9** | major | The three protocol §9.1 force-screen targets (NB-02, NB-08, NB-13) never entered the 1,996-record screened universe, so no dual-screening verdict with a criterion identifier exists for any of them; their eligibility failure rests on §9's full-text reading alone (§3.1, §9.0, L-17, amendment A9). |
| **VG-10** | **minor** — **and now scoped to ONE residue only: version identity** | **NARROWED round 2, RE-SCOPED round 3.** The round-1 form of this gap said the three Phillips reprints and Cowles DP 2331 could not be re-fetched and that §8.3's verdict and §7.4's FWER triple "cannot presently be re-opened". All four were re-fetched, digested and re-read on 2026-09-02 (§9.5; per-attempt log [se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json), SHA-256 over LF-normalised bytes `f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9`); the round-1 failure was HTTPS-only retrieval against a host that serves over plain HTTP, not an access barrier. Every quoted string and every reported number verified, including the FWER triple; 19 wrong page locators were found and corrected (L-18). **The single remaining residue:** no content digest was taken at extraction time (2026-08), so version identity between the text read then and the file retrieved now cannot be established — only content presence in the current file, on three independent fetches that returned byte-identical digests. **The §9 residue that round 2 folded into this gap has been discharged and is no longer here.** Round 2 downgraded this gap major → minor on the strength of a Phillips re-read, then folded into it a second, unlike residue — that the three §9 NB texts were re-fetched but **not** re-read — so an unverified-locator risk of exactly the class that had just produced 19 errors was carried at `minor` inside a gap whose stated ground for downgrade did not cover it. Round 3 re-read all three (**L-20**): fourteen quoted strings verify verbatim, four locators were wrong or loose and one result was misattributed, all corrected. The correct disposition was to do the re-read, not to re-severity it. (§9.5, L-16, L-18, L-20; findings REV-3-5, QUANT-3-4.) |
| **VG-13** | major | **A fourth, PROBABLE same-work twin pair inside the frozen included set was never adjudicated:** `eru-0198` (Erasmus Econometric Institute Report 2013-12, Handle 1765/39598) and `eru-0259` (Franses 2016, *CSDA* 100:160–169, doi:10.1016/j.csda.2014.06.006). The primary extraction log records `eru-0259` as extracted from `eru-0198`'s text and flags the pair "PROBABLE SAME-WORK TWIN PAIR … recorded as probable-twin for the review's dedup ledger to adjudicate"; the recheck log records `eru-0198` as `twin_of: eru-0259`. That adjudication never ran. Both records carry independent §6 appraisal rows (rows 4 and 64) whose Q4 and Q7 cells diverge and both count in the 65 assessable denominator — where each of the three *declared* twins is instead shown `—`, appraised under its carrier, and subtracted from that denominator. The two rows are two passes over **one** document, so they are not independent evidence and their divergence is not inside the 90-of-357 inter-pass count. **Restated round 3 (LITERATURE-3-2, QUANT-3-5):** (i) the round-2 form of this gap said "neither store entry carries a twin note" — the round-2 store update added one to **both**, so that clause was false when written and is struck; (ii) the sentence "twin status was verified against the published article's indexed abstract" is **withdrawn** — `eru-0259` has no `abstract` field in the candidate store and the CSDA abstract is not deposited in Crossref, OpenAlex or Semantic Scholar as of 2026-09-02, so the comparison cannot be re-opened; (iii) the stated ground "same-work identity cannot be settled because the journal text was never obtained" **does not distinguish this pair from `eru-0622`/`eru-0675`**, whose journal text was likewise never read, and is withdrawn as the reason. On the documentary standard the review actually applies to its three declared pairs — same author line, same subject, documented WP→journal chain, one text read — **this pair qualifies and the distinct-work count is 68**. The review does not renumber to 68 because that would re-derive the 65 denominator and every "of 65" fraction inside a frozen corpus, which is a re-appraisal, not a correction; the refusal is **operational, not evidential, and is labelled as such**. **72 records are 69 distinct works under the three pairs adjudicated at extraction, and 68 under the uniform standard.** The corpus is frozen and is not re-screened (amendment A13(b), **A14(a)**, §5.4). |
| **VG-11** | major | The automation tool's identity conflicts between this review's declaration (`claude-opus-5`) and the `AI-Assistance` trailers on the commits carrying the screening, extraction and NB-adjudication artifacts (`claude-fable-5`, commits `9deee0c` and `8aeebfe`). The ReproLog cited by `8aeebfe` records no model field, so the conflict **cannot be resolved from the logs**. The model identity for the independent re-extraction pass is unrecorded entirely, that artifact having been untracked (§12.1 L-15, frontmatter, AI-assistance statement). **Model CONFIGURATION is unrecorded for every stage and is unclosable:** no temperature, top-p, max-tokens, thinking budget or session seed appears in `er-screening-prompt.txt`, in any verdict or extraction JSONL, or in either ReproLog, so the screening stage is not re-runnable to a comparable κ and the interpretation of κ is restated as between-session variance under an unrecorded decoding configuration rather than as decoding variance (§2.5, §3.3, §15). The remediation-stage ReproLog `repro_log_a0f236b34b25417cb697df683198b3ef.json` itself carries `model_hash: null`, reproducing for the 2026-09-02 stage the omission this gap charges upstream. *(Finding REPRODUCIBILITY-2-3.)* |
| **VG-12** | minor | The backward-chase diagnostic of VG-4 could not cover 5 of 27 I2b carriers (`eru-0813`, `eru-1289`, `eru-1770`, `eru-0268`, `eru-1310`), and took reference lists from publisher-deposited metadata rather than from source PDFs, so its own coverage is bounded (A11, `se-bc-01.json`). **Its absence test is also weaker than reported:** DOI-or-exact-normalised-title matching missed a work present in the universe under a one-word title variant, so "177 referenced DOIs absent" is an upper bound with unquantified looseness (A12(c), LITERATURE-2-1). |
| **VG-17** | major | Six **load-bearing** records could not be retrieved on the round-4 targeted verification pass (`eru-0150`, `eru-0348`, `eru-0559`, `eru-0238`, `eru-0735`, `eru-1117`), so every §7 synthesis claim resting on them is still a single-session extraction transcription that no round has re-opened. The affected claims are named individually in **L-21**; the most consequential are §7.1's drift-break exception (the stated ground for TC-1 being two-sided, `eru-0348`), §7.2's Evans π-grid power table and the §7.7 pooling verdict that rests on it (`eru-0150`, now unobtained on two separate passes), and §7.3's reverse-regression dating-bias rows (`eru-0559`). Per-host, per-scheme attempt evidence is in [se-verify-loadbearing-01.json](search_logs/explosive-regime/se-verify-loadbearing-01.json). This gap is **narrower than VG-1**: those four records were never read at any stage, whereas these six were extracted once and could not be re-opened. |

**Repository-level gaps.** The three gaps below are **not** properties of this
review, its corpus, its protocol or its logs. They are properties of the
`castles` repository's reproducibility apparatus, they were found by the round-2
audit while checking this review's provenance claims, and they bound what a
successor can re-derive from a fresh clone. **This document does not repair
them** — that is a repository-maintenance action for the author, outside the
scope of a literature review — but recording them silently would leave the
review's own provenance claims resting on infrastructure whose weaknesses are
undisclosed. Each is scoped explicitly.

| id | severity | scope | gap |
|---|---|---|---|
| **VG-14** | major | **repository-level**, not review-level | **No clone-durable environment specification exists for the runs that produced or remediated this review.** `pyproject.toml` declares every dependency unpinned — no `==`, no version floors — and the only lock artifact, `uv.lock`, is untracked (`git ls-files uv.lock` returns nothing). The pip-freeze archives that would substitute live under `logs/reproducibility/env/`, which `.gitignore` excludes. A fresh clone therefore resolves an arbitrary dependency set. The Python version is correctly pinned (`requires-python >=3.11,<3.13`, matching the ReproLog host record 3.11.9), so the gap is package-level only. Remedy available to the author: commit `uv.lock`, or copy the pinned freeze to a tracked path and cite its SHA-256. *(Finding REPRODUCIBILITY-2-1.)* **PARTIALLY CLOSED 2026-09-03 (finding REPRODUCIBILITY-1-2). The superseded text above is retained per this review's supersession convention and is no longer true as written:** `uv.lock` is now tracked — `git ls-files uv.lock` returns `uv.lock` — committed at **`2ba291f9922547e1848d7d505cedafb2979e2433`** (*build: track uv.lock as the pinning mechanism; ADR-0005; declare s4-reexecution session*), SHA-256 **`eca78f9d52a8534f2890c99bd2f16b3aadc1455b0eb7b93c6d2e621240efd885`** over the LF checkout form that `.gitattributes` (`uv.lock text eol=lf`) fixes on every platform; 1,467 lines resolving the full dependency graph with per-artifact hashes under `requires-python >=3.11,<3.13`. The decision is recorded as [ADR-0005](../decisions/ADR-0005-lockfile-is-the-pinning-mechanism.md), whose header reads *Partially closes* and which names **three residuals that keep this gap open**: (i) the lockfile pins the declared dependency graph only, and this review's deliverables were produced largely by LLM agents and by ad-hoc standard-library scripts that no lockfile pins; (ii) **the environment that produced this corpus is not the environment the lockfile describes and cannot be recovered** — the corpus-stage ReproLog carries the SHA-256 of the empty string as its `pip_freeze_sha256` (VG-15), so there is nothing to pin against, and the ADR fixes the mechanism going forward only; (iii) nothing in CI checks the lockfile against `pyproject.toml`, so a stale lockfile is a new failure mode. **VG-14 therefore stays open at reduced severity for this review's own runs, and is closed only for future ones.** |
| **VG-15** | major | **repository-level**, not review-level | **The ReproLog for the stage that produced the frozen corpus is vacuous in environment and in data.** `repro_log_f5419aa650e249378ff40828424696bb.json` (commit `8aeebfe` — search, screening, extraction) records `pip_freeze_sha256` = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, which is the SHA-256 of the **empty string**, and the file it points at under `logs/reproducibility/env/` is 0 bytes. Its `config_resolved_sha256` is `null` and `dataset_checksums` is `{}`, so neither the protocol version nor the 1,996-record candidate store nor any verdict file was checksummed at the moment the run that created them executed. §15 cites this ReproLog as an environment record while disclosing only its missing model field (L-15, VG-11); the environment and input-state defects are named here. **The corpus's input state is fixed retrospectively instead** — by the digests recorded in the 2026-09-02 sidecar and by commit `8aeebfe`'s tree — which is weaker than a contemporaneous record and is not equivalent to one. **The claim this row previously made about the remediation-stage ReproLog was also wrong and is corrected (finding REPRODUCIBILITY-3-1).** It said `a0f236b3…` "is by contrast complete on 13 fields with verified dataset checksums". Complete on 13 fields, yes — but it is the **round-1** log, and **round 2 emitted no ReproLog and no sidecar at all**, so from the moment of the round-2 edits every input it checksums (`references_explosive-regime.json` at `8ed6f9ca…`, `se-bc-01.json` at `3ea52681…`) was a superseded state and its `config_resolved_sha256` was the A1–A11 protocol digest, not the A1–A13 one the document then carried. Restated accurately: **the round-1 remediation log is complete on 13 fields but pins pre-round-2 input states**, and it is superseded by the round-3 log `ee8bebfa…` in §15. *(Findings REPRODUCIBILITY-2-2, REPRODUCIBILITY-3-1.)* |
| **VG-16** | major | **repository-level**, not review-level | **No committed entrypoint re-derives any number this review reports.** `CLAUDE.md`'s Quickstart advertises `uv run pytest`, but `tests/` and `src/` contain no tracked files, and the project venv was never populated — the 172-package freeze recorded for the remediation run is the *global* interpreter's, not the project venv the reproducibility contract calls for. Every headline count (31/13 D-cell divergences, 50 `partial` cells, 90 of 357 inter-pass divergences, the 65/53 assessable denominators, I3 = 7, 62 DOI-bearing records) was produced by throwaway code. The counts **are** re-derivable from the tracked logs — the round-2 audit re-derived all of them independently and they matched — but a successor gets no guarantee of the same parse, and the §6 table uses escaped pipes inside I2 cells, which silently breaks naive column splitting. Remedy available to the author: commit the recount as `tests/test_erob_recount.py` reading `se-extraction-primary.jsonl`, `se-extraction-recheck.jsonl` and the §6 table, and record the *project-venv* freeze in the next ReproLog. *(Finding REPRODUCIBILITY-2-5.)* **PARTIALLY CLOSED 2026-09-03 (finding REPRODUCIBILITY-1-2), FOR THE ER-RoB DOMAIN COLUMN ONLY. The superseded text above is retained and is no longer true as written:** `tests/test_erob_recount.py` is tracked, committed at **`01ecfe7822ccca794272c35956ac8f8289d0c20b`** (*test: re-derive the ER-RoB domain column from the extraction logs; repair uv run*) — ~~707 lines and 9 tests **as committed at that hash**, green under `uv run pytest tests/test_erob_recount.py`~~. **SUPERSEDED 2026-09-04 (finding REV-2-4). The struck description above is the round-1 state and is retained so that state stays checkable; it is not the delivered artifact.** The delivered module is **1,149 lines, 56,401 bytes, 10 tests**, SHA-256 **`90981cd076377c56b438a49e11264a3dd67b7fb35f0dc976e055b96480d96994`** over the bytes on disk (no CRLF), **re-attested green — 10 passed — under `uv run pytest tests/test_erob_recount.py` on 2026-09-04** against that file and not against the 707-line state. **It is not yet committed at the time this row was written**, so the digest above is its durable identity and the commit that carries it must be named here at session close; the `01ecfe7` / 707-line / 9-test triple is kept as the superseded value. **What the two audit rounds did to the module body, since the line count alone does not say it:** round 1 (CODE-1-1, CODE-1-2, CODE-1-3) rewrote the no-magic-number guard to walk string constants as well as numeric ones, re-keyed both allow-lists by enclosing definition, and added an assertion that no allow-list entry goes unexercised; round 2 (CODE-2-1) made `divergent_cells` a **total** classifier and added the tenth test, `test_every_domain_concern_cell_is_a_declared_scale_level`. **The round-2 fix found four fail-open paths where the finding named one**: besides an unrecognised domain-concern label falling through both the lenient and the strict branch, the assessability axis was unconstrained in both directions — a recorded judgment where the rule derives *not assessable*, and a *not assessable* cell where the rule reaches a judgment. **All four hole cells of the 576-cell cross-tab are empty in the shipped §6 table, so the guards are additive and no count, no cell and no published figure moves.** The scale vocabulary is now parsed out of protocol §6 and this review's own §6 legend rather than hardcoded, so a level added to either document fails at the guard instead of being silently dropped. It re-derives the §6 D column from the two extraction logs by protocol §6's rule with A7's CONVENTION and §2.8's resolution ordering, parsing the rule and the ordering out of the amendments rather than retyping them, and it reproduces amendment A8's published **31 / 13** exactly. **What stays open:** every other count this review reports — the 50 `partial` cells, the 561 and 65/53 assessable denominators, 90 of 357 inter-pass divergences, I3 = 7, the 62 DOI-bearing records, the O6 and lineage distributions — still has no committed entrypoint and was produced by throwaway code. The `uv run` repair means the Quickstart now executes; it does not mean the numbers are covered. The 2026-09-03 audit round raised two further findings against the module itself (CODE-1-1, CODE-1-2 — the no-magic-number guard walking only numeric AST constants, and a published figure carried inside a regex string literal); those are remediated in `tests/` outside this review and are not this document's to report. **VG-16 is closed for the ER-RoB domain column and open for every other reported count.** |

**Identifier and metadata verification — asserted, and now archived.** All DOI
and arXiv identifier checks passed: 62/62 DOIs `responseCode` 1, two arXiv IDs
resolved, one Handle `responseCode` 1, all re-run 2026-09-02. There is no
unresolved-identifier gap among records that have identifiers. Separately, a
Crossref metadata cross-check of all 62 DOI-bearing records retrieved 62 of 62
and surfaced 13 volume/issue/page discrepancies, 3 pagination updates and 1
version misattribution (L-13(a)–(d)), plus — on the round-2 re-run that actually
checked the year field — 19 online/print year divergences, 22 label-versus-store
divergences and one label year matching no source (L-13(e)). That is a
metadata-accuracy finding, not an identifier-resolution gap.

**These checks now have a machine-readable log; in round 1 they did not
(finding REPRODUCIBILITY-2-4).** Round 1 replaced a partial check with a complete
one but retained none of the retrieved payloads, so its 13 discrepancies were
re-openable only by re-querying a mutable API — and Crossref records mutate,
which is exactly why 13 of them diverged from the extraction citations in the
first place. **Every SHA-256 published below for a `.json` evidence log is taken over
LF-normalised bytes** — the bytes `.gitattributes` (`*.json text eol=lf`)
guarantees on checkout on every platform. Round 2 published these two digests
over CRLF working-tree bytes written by a Windows host, so **no consumer of the
committed repository could have reproduced them**; the two files have been
rewritten with LF terminators (line endings only, no field value changed) and
the digests republished. Superseded values, kept so the round-2 text remains
checkable: `se-crossref-recheck-01.json` `cb9b0c26…`,
`se-fetch-recheck-01.json` `30b69960…`. *(Finding REPRODUCIBILITY-3-2;
CONVENTION registered as amendment **A14(d)**.)* Every per-record result, plus a
SHA-256 of each canonically serialised Crossref message, plus the 63
Handle-System resolutions and the 2 arXiv resolutions, is archived at
[se-crossref-recheck-01.json](search_logs/explosive-regime/se-crossref-recheck-01.json)
(SHA-256 `9457d3de7e3e3e60cc2b5832785b0b8b6da462153a627ddc69e29f72cd77ac9d`),
and the §9.5 source-text retrieval attempts at
[se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json)
(SHA-256 `f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9`) —
the same treatment `se-bc-01.json` already gave the backward-chase arm
(itself now `75f36b547b305857e6af20a8127c0f0cbdb83df655749ee22e51e6ee052c2a9f`
over LF bytes; no digest for it had previously been published).

**Round 3's own evidence is archived the same way.** The third re-fetch of all
seven §9.5 texts, the DP 2331 and PSY 2015a table transcriptions behind L-19,
the NB re-read behind L-20, and the three-source abstract lookup behind the
§5.4 withdrawal are at
[se-verify-r3-01.json](search_logs/explosive-regime/se-verify-r3-01.json)
(SHA-256 over LF bytes
`a92fae17c041674094c0cfdb7753b18ef54da6fabb5c8ffb4cb68adc945a44bf`).

**One evidence file deliberately carries no published digest.**
`se-extraction-recheck.jsonl` gets only `text=auto` with `eol` unspecified from
`.gitattributes`, and `core.autocrlf` is `true` on the execution host, so its
checkout form is **platform-dependent**: a digest published for it would be
reproducible on some clones and not others. None is published, and none may be
until `*.jsonl text eol=lf` is added to `.gitattributes` — a repository
maintenance action outside this review's scope, of the same class as VG-14 and
VG-16. *(Finding REPRODUCIBILITY-3-2.)*

### 12.4 PRISMA 2020 conformance map — actuals

The protocol fixed anticipated statuses in advance (§9.4). This table restates it
with what was achieved. Changes from the anticipated status are marked **▲** and
explained.

| item | topic | anticipated | actual | note |
|---|---|---|---|---|
| 1 | title | met | met | identified as a systematic review in the title and frontmatter |
| 2 | abstract | met | met | structured abstract, immediately below the frontmatter |
| 3 | rationale | met | met | §1 |
| 4 | objectives | met | met | §1 |
| 5 | eligibility criteria | met | **partial ▲** | frozen protocol §2, cited by identifier in every verdict — with **four** departures now recorded as amendments: **seven** included records fail I3 as written (not five; L-6, A10(a)), three same-work twins survive X7 (L-7, A10(b)), **a fourth pair (`eru-0198`/`eru-0259`) is a probable X7 twin that was flagged for adjudication and never adjudicated** (§5.4, VG-13, A13(b)), and the three §9.1 force-screen targets never entered the screened universe so no criterion-citing verdict exists for them (L-17, A9) |
| 6 | information sources | met | met | §2.2, per platform with execution dates |
| 7 | search strategies | met | **partial ▲** | §2.2; all 42 logs including the four zero-yield 429s. The protocol's backward citation-chasing arm did not run in the execution window; it ran once after corpus freeze, over 22 of 27 carriers, from publisher-deposited reference lists (A11, `se-bc-01.json`, L-5, VG-4), and its yield was **1** candidate addition rather than the 2 first reported — its DOI-or-normalised-title absence test is defeated by one-word title variants, which also bounds its "177 absent" figure (A12(b)–(c), VG-12). The optional SSRN arm did not run (VG-5) |
| 8 | selection process | partial | **partial** | dual LLM-agent screening, single base model, declared as the automation tool; κ with raw agreement and the 2×2 table; **▲ further weakened** by A3 for 153 records (L-3), and **▲** the automation tool's identity is declared per stage against the commit trailers because the review's original single-model declaration conflicts with them and the ReproLog carries no model field (L-15, VG-11) |
| 9 | data collection | partial | **partial, and weaker than anticipated ▲** | dual re-extraction of E9–E13 and Q1–Q7 ran, but the prescribed mismatch reconciliation did not (L-2); resolution rule declared in §2.8 |
| 10 | data items | met | met | protocol §5 unchanged; §5 and §7 report them |
| 11 | risk of bias | met\* | **partial ▲** | ER-RoB v1, `CONVENTION`, unvalidated, stated at every point of report — but the instrument as executed departs from the instrument as frozen in two recorded ways: a fourth response level `partial` in **50 of 561 answered Q-cells** (65 × 7 for Q1–Q7 plus 53 × 2 for Q8/Q9; A7 as corrected by A12), undefined in the frozen concern rule (A7), and 44 domain cells departing from the frozen Q→D rule, 31 of them toward lower concern (A8). Both columns are reported in §6 and §6.1 |
| 12 | effect measures | inapplicable with rationale | inapplicable with rationale | §2.10 |
| 13 | synthesis methods | met | met | §2.9, §7; pooling condition pre-stated and its failure documented per characteristic (§7.7) |
| 14 | reporting bias | met\* | met\* | §10; funnel methods inapplicable with rationale, three substitutes assessed; **▲** item-1 substitute changed because of I-2 |
| 15 | certainty | met\* | met\* | tier + concern profile + causality status per claim; §12.1 L-14 states its weakness, and the concern profile is convention-resolved rather than source-adjudicated (L-2, A6) |
| 16a | flow | met | met | §3.1, reconciled identity by identity in §3.2 |
| 16b | near-misses with reasons | met | met | all 234 substantive full-text exclusions enumerated in §13; the 280 X6 records are a declared distinct class recoverable from `se-stage2-crosstable.json` |
| 17 | study characteristics | met | met | §5 corpus table with tier, I2, path, O6, code availability and extraction depth |
| 18 | RoB results | met | met | §6 (72 rows, both the recorded-judgment and the rule-derived domain columns, every divergent cell marked), §6.1 (both distributions, over assessable denominators of 65 and 53, not 72) |
| 19 | individual results | met | met | §7 evidence tables carry per-study values with table/page locations; full extraction in `se-extraction-primary.jsonl` and `se-extraction-recheck.jsonl` |
| 20 | synthesis results | met | met | §7, narrative by outcome domain, no pooling |
| 21 | reporting-bias result | met\* | met\* | §10.1–§10.4 |
| 22 | certainty result | met\* | met\* | per-claim tier and concern flags inline in §7 |
| 23 | discussion / limitations | met | met | §12.1, including the single-model screening limitation |
| 24a/b/c | registration, protocol, amendments | partial | **partial** | no registry entry exists for non-health methodology reviews; protocol + provenance commit `9deee0c` + the §10 amendment log are the substitute. Execution ran under A1–A3; **A4–A13 are appended to the protocol addendum by this document** (§12.5), all ten labelled post-hoc. A12 and A13 are round-2 correcting entries over A7, A10(b) and A11, appended rather than edited because §10 makes the addendum append-only |
| 25 | support | met | met | none |
| 26 | competing interests | met | met | none |
| 27 | data/materials availability | met | **partial ▲** | Stated as of the delivering commit rather than in the present tense, because the present tense was false when this review was written. **Tracked at commit `8aeebfe`:** the candidate store, the 42 raw query logs, the dedup ledger, the KI recall check, the screening prompt, five verdict JSONL files, `se-extraction-primary.jsonl`, `se-nb-adjudications.json`, the stage crosstables and the κ computation. **Untracked when this review was written, and tracked only by the commit that delivers it:** this review, `references_explosive-regime.json`, `se-extraction-recheck.jsonl` and `se-bc-01.json`. **Not tracked in any commit and not resolvable in a fresh clone:** the ReproLog and the sidecar, which are gitignored — §15 therefore cites their SHA-256 digests and labels their paths as untracked locators, per the repository's reproducibility contract. All paths are repo-relative |

**Identity hygiene (G18 class).** No OS username, no real-name email address and
no absolute home-directory path appears in this review, in
`references_explosive-regime.json`, or in any path cited here. All paths are
repo-relative. Real-name *attribution* is this repository's declared policy and is
carried by git config, not by file contents.

### 12.5 Amendments this document APPENDS to the frozen protocol

Protocol §10 makes the addendum append-only and **assigns amendment entries to
the executing session**. This document is the executing session for all **eleven**
deviations below, so they are appended here rather than deferred to a consumer
session. **A12 and A13 are round-2 correcting entries**, appended 2026-09-02
after an independent audit found two wrong numbers and one over-broad assurance
inside A7, A10(b) and A11. **A14 is a round-3 correcting entry**, appended the
same day after a third audit found that A13(b) had refused an adjudication on a
ground the review does not apply elsewhere, that A9's adjudication evidence had
never been re-read, and that the digests published for two evidence logs could
not be reproduced from the committed repository. Under §10 those entries cannot be edited, so the
correction is itself an amendment; each superseded figure is flagged in its own
row above. The earlier form of this section listed A4–A6 as amendments the review
"requests" and asked a consumer session to append them; that left the
registration carrier — the artefact that makes protocol-vs-execution fidelity
auditable — inconsistent with executed conduct at ship time. *(Findings REV-1-1,
SCOPE-1-2.)*

**Frozen text above the addendum is not touched.** The protocol's byte prefix
through the end of §10's frozen text still hashes to
`33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`, the
registration digest at commit `9deee0c`, verified by re-hashing the first
N bytes of the current file where N is the length of the file at that commit.
Only the append-only addendum grew; the check above was **re-run after the
round-3 A14 append** and still holds. The frontmatter field
`protocol_sha256_with_addendum` is updated to the A1–A14 digest
`9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa` and
`amendments_appended_by_this_document` replaces the former
`amendments_this_document_requests`. The A1–A11 and A1–A13 digests that this
document carried before the round-2 and round-3 appends are retained in the
frontmatter as `protocol_sha256_with_addendum_A1_A11` and
`protocol_sha256_with_addendum_A1_A13`, so all three states are checkable.

| id | date | stage | PRISMA-P item(s) | post-hoc? | what it records |
|---|---|---|---|---|---|
| **A4** | 2026-09-02 | output naming; decided pre-execution | 4 | entry post-hoc | Delivered filename `lit_review_explosive-regime-dating_2026-08-24.md` versus the frontmatter's `planned_outputs` pattern. Content, structure and scope unchanged. |
| **A5** | 2026-09-02 | §8 extraction, before the affected texts were read | 11c | entry post-hoc | Retrieval-cap deviation confined to the three §9.1(i) adjudication carriers: a web search plus a Cowles reprint fetch outside the declared attempt cap secured the published *IER* texts of KI-01/02/03. |
| **A6** | 2026-09-02 | extraction | 11c, 14 | **yes — logged after the affected appraisal entries** | §4.3's source-text reconciliation did not run. 90 of 357 comparable cells diverged; resolved by the declared conservative rule of §2.8. Consequence: the ER-RoB profile is convention-resolved, not source-adjudicated (L-2). |
| **A7** | 2026-09-02 | appraisal | 14 | **yes** | ER-RoB v1's frozen three-level response scale was extended to four by adding `partial`, in 50 of 585 answered Q-cells; the frozen concern rule is undefined for the added level. Fixes and labels the CONVENTION that `partial` counts as not-`yes` (§2.7, §6). *(QUANT-1-1.)* **Denominator superseded by A12: the correct figure is 50 of 561** (65 × 7 + 53 × 2); A7's text is not edited because the addendum is append-only. |
| **A8** | 2026-09-02 | appraisal | 14 | **yes** | Departure from §6's Q→D concern rule: 31 domain cells recorded `low` where the rule raises concern, 13 recorded above `low` where the rule does not. Both columns now reported, with per-domain divergence counts and every divergent cell marked (§6, §6.1). *(REV-1-3, QUANT-1-2.)* |
| **A9** | 2026-09-02 | screening | 8, 9, 11c | **yes** | §9.1's force-screening of NB-02/NB-08/NB-13 into the record universe did not happen; the three were adjudicated out-of-corpus without entering the 1,996 (§3.1, §9.0, L-17, VG-9). *(SCOPE-1-1.)* |
| **A10** | 2026-09-02 | screening | 8, 11c | **yes** | (a) Seven included records fail I3 as written, and a twin does not inherit its carrier's DOI for I3 purposes. (b) Three same-work twins survive X7, so 72 records is 69 distinct works (L-6, L-7). *(SCOPE-1-5, REV-1-2.)* **A10(b)'s no-double-counting assurance is narrowed by A13(a)** — it holds for §7's evidence tables, not for the §4/§7.6/§10.2 record-level distributions — **and a fourth, probable, unadjudicated twin pair is disclosed by A13(b)**. A10's text is not edited because the addendum is append-only. |
| **A11** | 2026-09-02 | supplementary search, **after corpus freeze** | 9, 10, 11c | **yes, in both senses** | The backward citation-chasing arm did not run in the execution window and was executed here as a post-freeze recall diagnostic: 22 of 27 carriers, publisher-deposited reference lists, 2 candidate additions surfaced and **not** admitted, corpus left frozen at 72 (§2.2, L-5, VG-4, VG-12). *(SCOPE-1-4.)* **Yield corrected by A12: 1 candidate addition, not 2** — `er-bc-2` is in the universe as `eru-0209`/`eru-1027` and was screened and excluded. A11's text is not edited because the addendum is append-only. |
| **A12** | 2026-09-02 (round 2) | correcting entry over A7 and A11 | 9, 11c, 14 | **yes** | Two numbers inside earlier append-only entries are wrong and are corrected without editing them. (a) **A7's `partial` denominator 585 → 561** (65 × 7 for Q1–Q7 + 53 × 2 for Q8/Q9); the 50-cell numerator and its per-question split are unchanged. (b) **A11's yield 2 candidate additions → 1**: `er-bc-2` is in the 1,996 as `eru-0209` (X7) and `eru-1027` (S-c-fail), and A11's DOI-or-normalised-title absence test is defeated by one-word title variants, which bounds the "177 absent" figure. *(QUANT-2-1, REV-2-12, LITERATURE-2-1.)* |
| **A13** | 2026-09-02 (round 2) | correcting entry over A10(b); §9.1 vocabulary scope qualifier | 8, 11c | **yes** | (a) **A10(b)'s no-double-counting assurance is narrowed**: true of §7's evidence tables, false of the record-level distributions in §4, §7.6 and §10.2, which counted the three twins a second time under inherited codes; distinct-work counts now given at all three. (b) A **fourth, probable** same-work twin pair is disclosed — `eru-0198` / `eru-0259` — unadjudicated because the journal text was never obtained. (c) The **§9.1 verdict-vocabulary scope qualifier** "PROVISIONAL ON THE WORKING-PAPER TWIN" on NB-13 is registered as a post-hoc CONVENTION of the review, not of the frozen protocol, together with the fact that the protocol defines neither `indeterminate-from-full-text` nor the version-mismatch case. *(REV-2-3, SCOPE-2-3, REV-2-4, LITERATURE-2-6.)* |

| **A14** | 2026-09-02 (round 3) | correcting entry over A13(b) and A9; digest convention | 8, 11c, 27 | **yes** | Four parts. (a) **A13(b)'s ground for refusing to adjudicate the fourth twin pair is withdrawn** — "the journal text was never obtained" does not distinguish `eru-0198`/`eru-0259` from `eru-0622`/`eru-0675`, which the review *does* declare a twin pair on an unread journal text. The twin-declaration standard actually used is registered as a CONVENTION (documentary, single-text: same author line, same subject, documented WP→journal chain), the fourth pair is recorded as **meeting** it, and the refusal to renumber 69 → 68 is relabelled **operational** (it would re-derive the frozen 65 denominator) rather than evidential. (b) §5.4's "twin status was verified against the published article's indexed abstract" is **withdrawn as irreproducible** — no abstract for `eru-0259` exists in the candidate store, Crossref, OpenAlex or Semantic Scholar. (c) **A9's §9.1 adjudication evidence has been re-read**: 14 quotations verbatim, 4 locators wrong or loose, and **one result misattributed** (NB-08's Theorem 1, not "Theorem 3.1"). (d) **CONVENTION:** every published `.json` evidence-log SHA-256 is over **LF-normalised** bytes; round 2's CRLF digests are superseded and republished; no digest is published for `se-extraction-recheck.jsonl` while `*.jsonl` lacks `eol=lf`. *(LITERATURE-3-2, QUANT-3-5, REV-3-5, QUANT-3-4, REPRODUCIBILITY-3-2.)* |

**What remains incomplete after this append.** The protocol record is now
consistent with executed conduct, but four of the eleven amendments record
things that cannot be repaired by bookkeeping: A9's missing screening verdicts
do not exist and cannot be reconstructed; A10's I3 and X7 failures are inside a
frozen corpus this review does not re-screen; A11's arm ran once, late,
through a weaker retrieval route, left **one** named candidate outside the
corpus, and has now been shown to use an absence test that its own headline
figure overstates; and A13(b)'s fourth twin pair is **not** blocked by the
journal text after all (**A14(a)** withdraws that ground) but by the fact that
declaring it would re-derive a frozen corpus's assessable denominator, which
remediation may not do. Each is carried as a limitation and a verification gap
as well as an amendment.

**And a note on the shape of this section.** Three of the eleven amendments
(A12, A13, A14) exist only because entries appended in an earlier round contained
errors or refused on grounds the review does not apply elsewhere. That is the
append-only rule working as designed — the wrong figures and the withdrawn
grounds stay on the record with their corrections attached, rather than being
quietly overwritten — but it means the addendum is now a record of **three**
audit rounds, and a reader must follow the pointers in the A7, A9, A10, A11 and
A13 rows rather than reading those rows alone. **The trend is worth stating
plainly at the end of the last round available:** each audit round has found
errors inside the previous round's corrections — round 2 inside round 1's, round
3 inside round 2's — at a rate that has not yet fallen. Nothing in this document
should be read as evidence that the process has converged; it should be read as
the state after three rounds, with §18's residual-risk list attached.


## 13. PRISMA item 16b — records excluded at full text, with reasons

All **234** records excluded on substantive criteria at stage 2, each with its
record id, title as held in the candidate store, publication year where the store
carries one, identifier where one exists, the deciding criterion, the retrieval
route the screener recorded, the screener's stated reason, and the path by which
the exclusion became terminal. Rows are sorted by record id.

Where the `path` reads *both-exclude, code conflict*, both screeners excluded and
their criterion codes differed; both codes are shown and the adjudicator was not
invoked (protocol amendment A3). Where it reads *A3 single-screener exclude*, one
screener reached full text and excluded while the other returned X6. Where it
reads *blind adjudication → exclude*, the two screeners split INCLUDE/EXCLUDE and
a third blind session decided.

The 280 records excluded because full text could not be obtained (X6) are **not**
listed here: X6 is an access outcome rather than an eligibility judgment, and the
protocol treats it as a distinct class. Their record ids are recoverable in full
from `docs/literature/search_logs/explosive-regime/se-stage2-crosstable.json`,
key `both_x6`.

| rec | title | yr | identifier | criterion | route | reason | path |
|---|---|---|---|---|---|---|---|
| eru-0002 | 11. Testing Bubbles: Exuberance and collapse in the Shanghai A-share stock ... | — | — | X7 | repository | ORCA copy; same-work duplicate of eru-0498 (ANU Press chapter with DOI) | both-exclude |
| eru-0011 | Federal Reserve Bank of Dallas Globalization and Monetary Policy Institute ... | — | — | X7 | repository | earlier draft of eru-0228 (Monitoring Housing Markets; documented in WP 165 footnote) | A3 single-screener exclude (other screener X6) |
| eru-0012 | Federal Reserve Bank of Dallas Globalization and Monetary Policy Institute ... | — | — | X1 | repository | GSADF application to Colombian housing; no operating characteristics reported | A3 single-screener exclude (other screener X6) |
| eru-0015 | Gelişen-8 (D-8) Piyasalarında Balon Oluşumu: Küresel Salgın Dönemi Üzerine | — | — | X1 | repository | SADF application to D-8 markets; no operating characteristics | A3 single-screener exclude (other screener X6) |
| eru-0016 | Identifying Speculative Bubbles | — | 10.5089/9781498332071.001.a001 | I1 | publisher | IMF surveillance framework discussion; no explosive-AR detector with stated null | both-exclude |
| eru-0017 | İKTİSADİ VE İDARİ BİLİMLER FAKÜLTESİ DERGİSİ | — | — | I1 | none | Journal-title record (faculty journal), not a study | A3 single-screener exclude (other screener X6) |
| eru-0018 | Journal of Econometrics | — | — | X7 / I1 | repository | defective metadata record duplicating eru-1526 (Lui-Phillips-Yu JoE HAR test) // R2: Journal-title record (Journal of Econometrics), not a study | both-exclude, code conflict |
| eru-0024 | Monitoring Explosive Prices in the Brazilian Real Estate Market (2008 | — | — | X1 | repository | forward-searching ARIMA application to Brazilian housing; no OC | A3 single-screener exclude (other screener X6) |
| eru-0027 | Observation-Driven filters for Time-Series with Stochastic Trends and Mixed... | — | — | I1 | repository | observation-driven bubble filter; estimation not null-referenced time-indexed test (S-c fail) | A3 single-screener exclude (other screener X6) |
| eru-0029 | Property Prices and Speculative Bubbles | — | 10.5089/9781451841756.001.a001 | X2 | publisher | full-sample bubble existence testing on HK property; no time-indexed output | both-exclude |
| eru-0043 | Testing for Bubbles in the Colombian Housing Market: A New Approach 1 | — | — | X1 | repository | GSADF application to Colombian housing; no OC reported | A3 single-screener exclude (other screener X6) |
| eru-0069 | Tests of stationarity against a change in persistence | 2004 | 10.1016/j.jeconom.2003.10.028 | S-a-fail | repository | KI-13 full text: alternatives are I(0)/I(1) persistence changes, never explosive root | both-exclude |
| eru-0087 | A LIMIT THEOREM FOR MILDLY EXPLOSIVE AUTOREGRESSION WITH STABLE ERRORS | 2007 | 10.1017/s0266466607070090 | S-b-fail | publisher | mildly explosive AR with stable errors; estimation limit theory, no detector | both-exclude |
| eru-0091 | Explosive Behavior and the Nasdaq Bubble in the 1990s: When Did Irrational ... | 2007 | 10.2139/ssrn.972730 | X7 | none | SSRN twin of eru-0131 (PWY Nasdaq, KI-01) | both-exclude |
| eru-0092 | Limit theory for moderate deviations from a unit root | 2007 | 10.1016/j.jeconom.2005.08.002 | S-b-fail | repository | KI-05 full text: estimation limit theory only; no time-indexed detector output | both-exclude |
| eru-0095 | Are there speculative bubbles in stock markets? Evidence from an alternativ... | 2008 | 10.4310/sii.2008.v1.n2.a8 | X2 | openalex-oa | residual-based full-sample existence test; no date-stamping output (S-b fail) | both-exclude |
| eru-0103 | Speculative Bubbles and Financial Crisis | 2009 | 10.20955/wp.2009.029 | X5 | openalex-oa | general-equilibrium bubble theory; no test procedure | both-exclude |
| eru-0106 | Dating the Timeline of Financial Bubbles During the Subprime Crisis 1 | 2010 | — | X7 | repository | CFDP 1770 working-paper twin of eru-0154 (Phillips-Yu 2011 QE) | both-exclude |
| eru-0127 | Dating the timeline of financial bubbles during the subprime crisis P | 2011 | — | X7 | repository | same-work duplicate of eru-0154 (Phillips-Yu 2011 QE) | both-exclude |
| eru-0128 | Double Asymptotics for an Explosive Continuous Time Model | 2011 | — | S-b-fail | publisher | double asymptotics for explosive continuous-time estimation; no time-indexed detector | A3 single-screener exclude (other screener X6) |
| eru-0146 | Specification Sensitivities in Right-Tailed Unit Root Testing | 2011 | — | X7 | none | working-paper twin of eru-0238 (specification sensitivity, PSY) | both-exclude |
| eru-0147 | Specification Sensitivities in Right-Tailed Unit Root Testing for Financial... | 2011 | 10.2139/ssrn.1873871 | X7 | none | SSRN twin of eru-0238 (specification sensitivities, financial bubbles variant) | both-exclude |
| eru-0164 | Detecting Asset Price Bubbles in the Near-Explosive Random Coefficient Auto... | 2012 | — | S-b-fail / I3 | repository | near-explosive RCA parameter inference; no time-indexed date-stamping output // R2: No DOI/arXiv/handle; best locator ESSEC/Albany PDF; NERC theory... | both-exclude, code conflict |
| eru-0175 | Mildly explosive autoregression under weak and strong dependence | 2012 | 10.1016/j.jeconom.2012.01.024 | S-b-fail | repository | Mildly explosive estimator asymptotics under dependence; no time-indexed procedure | A3 single-screener exclude (other screener X6) |
| eru-0176 | Multiple Changes in Persistence vs. Explosive Behaviour: The Dotcom Bubble | 2012 | 10.2139/ssrn.2035033 | X1 | openalex-oa | SSRN twin of eru-0301; LKT persistence plus PWY application; no OC | A3 single-screener exclude (other screener X6) |
| eru-0181 | Specification Sensitivity in Right-Tailed Unit Root Testing for Explosive B... | 2012 | 10.2139/ssrn.1981951 | X7 | none | SSRN/CFDP 1842 twin of eru-0238 | both-exclude |
| eru-0184 | Steady-state distributions for models of bubbles: their existence and econo... | 2012 | — | I1 / X7 | repository | TAR steady-state distribution theory; no null-referenced time-indexed detector // R2: WP twin of eru-0306 (Econ Modelling 2014); same work | both-exclude, code conflict |
| eru-0185 | Testing for Explosive Behavior in Relative Price Measures : Implications fo... | 2012 | — | X1 | repository | GSADF application to relative PCE inflation measures; no OC | A3 single-screener exclude (other screener X6) |
| eru-0186 | Testing for Multiple Bubbles | 2012 | 10.2139/ssrn.1981976 | X7 | repository (Cowles DP 1843 PDF; SSRN twin doi:10.2139/ssrn.1981976) | WP twin of PSY 2015 (KI-02/03): same GSADF/BSADF date-stamping and limit-theory work (abstract pp.1-2); twin relation documented (protocol SS2.4). | blind adjudication -> exclude |
| eru-0204 | Bias-corrected estimation in potentially mildly explosive autoregressive mo... | 2013 | — | S-b-fail | repository | MC comparison of bias-corrected estimators incl. mildly explosive; estimation not detection | A3 single-screener exclude (other screener X6) |
| eru-0206 | Bubbles in food commodity markets: Four decades of evidence | 2013 | 10.1016/j.jimonfin.2013.08.008 | X1 | repository | GSADF application to food commodity futures; no own OC | A3 single-screener exclude (other screener X6) |
| eru-0207 | Bubbles in Grain Futures Markets: When are They Most Likely to Occur? | 2013 | 10.22004/ag.econ.285803 | X1 | openalex-oa | bubble date-stamping in grain futures plus logit determinants; wild bootstrap CVs only | A3 single-screener exclude (other screener X6) |
| eru-0209 | Detecting and Forecasting Large Deviations and Bubbles with a Near-Explosiv... | 2013 | — | X7 | none | working-paper twin of eru-1027 (near-explosive random coefficient forecasting) | A3 single-screener exclude (other screener X6) |
| eru-0210 | Detecting bubbles in Hong Kong residential property market | 2013 | 10.1016/j.asieco.2013.04.005 | X1 | repository | HKIMR WP twin: PWY-type test applied to HK property; no OC | A3 single-screener exclude (other screener X6) |
| eru-0215 | Essays on Asset Prices and Macroeconomic Fundamentals | 2013 | 10.17169/refubium-15048 | X1 | repository | thesis: MS models plus sequential unit-root application to exchange rates; no OC | A3 single-screener exclude (other screener X6) |
| eru-0220 | Explosive Target Balances | 2013 | 10.2139/ssrn.2286075 | X7 | none | SSRN duplicate of eru-0279 (Explosive Target Balances, CESifo/EM twins) | A3 single-screener exclude (other screener X6) |
| eru-0221 | From hero to zero: Evidence of performance reversal and speculative bubbles... | 2013 | 10.1016/j.eneco.2013.01.006 | X1 | repository | sup ADF and MS-ADF applied to German renewable stocks; no OC | A3 single-screener exclude (other screener X6) |
| eru-0228 | Monitoring Housing Markets for Episodes of Exuberance: An Application of th... | 2013 | 10.2139/ssrn.2378505 | X1 | repository | Dallas Fed WP 165 (twin of eru-0340): SADF/GSADF housing application; simulated CVs, no OC | A3 single-screener exclude (other screener X6) |
| eru-0233 | Rational speculative bubbles in the Asian stock markets: Tests on determini... | 2013 | 10.1057/jam.2013.13 | X2 | openalex-oa | cointegration existence tests, Asian markets; no time-indexed output | both-exclude |
| eru-0237 | Renewed Momentum in the German Housing Market: Boom or Bubble? | 2013 | 10.2139/ssrn.2286048 | X7 | none | SSRN twin of eru-0486 (Chen-Funke German housing monitoring) | A3 single-screener exclude (other screener X6) |
| eru-0242 | TESTING FOR MULTIPLE BUBBLES: HISTORICAL EPISODES OF EXUBERANCE AND COLLAPS... | 2013 | — | X7 | repository | CFDP 1914 working-paper twin of eru-0393 (PSY 2015a, KI-02) | both-exclude |
| eru-0258 | Are Transient Explosive Roots the Signature of a Bubble? A Markov Regime Sw... | 2014 | — | I2 | publisher | Bayesian MS-BMA critique of explosive-root signature; no OC for in-scope detectors | A3 single-screener exclude (other screener X6) |
| eru-0261 | Asymptotic distributions related to mildly-explosive second order autoregre... | 2014 | 1409.8571 | S-b-fail | arxiv | mildly explosive AR(2) estimator limit theory; no time-indexed detector | both-exclude |
| eru-0265 | BUBBLING OVER ALONG THE OIL FUTURES YIELD CURVE | 2014 | — | X1 / X7 | repository | GSADF+FLUC application to oil futures; no own operating characteristics // R2: WP twin of eru-0332 (JEF 2015 oil futures); same work | both-exclude, code conflict |
| eru-0269 | Die Target-Forderungen der Deutschen Bundesbank: Eine Zeitreihenanalyse | 2014 | — | X1 | repository | BSADF applied to Bundesbank Target2 claims; no OC | A3 single-screener exclude (other screener X6) |
| eru-0275 | Econometric Tests for Speculative Bubbles | 2014 | — | I2 | repository | pedagogical survey of bubble tests; no original theory, simulation, or OC | A3 single-screener exclude (other screener X6) |
| eru-0279 | Explosive Target balances of the German Bundesbank | 2014 | 10.1016/j.econmod.2014.07.008 | X1 | repository | SADF/GSADF applied to Target balances (via CESifo 4297 twin); no OC | A3 single-screener exclude (other screener X6) |
| eru-0281 | Financial Bubble Implosion | 2014 | 10.2139/ssrn.2533015 | X7 | none | SSRN twin of eru-0559 (Financial Bubble Implosion, CFDP 1967) | both-exclude |
| eru-0296 | Rational Bubbles in the Indian Stock Market: Empirical Evidence from NSE-50... | 2014 | — | X2 | repository | linear/nonlinear cointegration existence tests, NSE; no time-indexed output | A3 single-screener exclude (other screener X6) |
| eru-0300 | SFB 823 Monitoring stationarity and cointegration D iscussion P aper | 2014 | — | X4 / X7 | repository | monitors stationarity-to-I(1) change; no explosivity alternative // R2: SFB 823 DP twin of eru-0369; same title | both-exclude, code conflict |
| eru-0301 | Signalling the Dotcom bubble: A multiple changes in persistence approach | 2014 | 10.1016/j.qref.2014.08.006 | X1 | repository | Persistence-change and PWY applied to NASDAQ; no operating characteristics | A3 single-screener exclude (other screener X6) |
| eru-0303 | Speculative Price Bubbles in Urban Housing Markets in Germany | 2014 | 10.2139/ssrn.2519076 | X7 | none | SSRN twin of eru-0597 (DIW dp1417 German urban housing bubbles) | A3 single-screener exclude (other screener X6) |
| eru-0306 | Steady state distributions for models of locally explosive regimes: Existen... | 2014 | 10.1016/j.econmod.2014.03.015 | I1 | repository | published twin of eru-0184: TAR steady-state theory, no null-referenced detector | both-exclude |
| eru-0326 | Are there multiple bubbles in the ethanol–gasoline price ratio of Brazil? | 2015 | 10.1016/j.rser.2015.07.085 | X1 | repository | GSADF ethanol-gasoline application; simulation only for critical values | A3 single-screener exclude (other screener X6) |
| eru-0330 | Bias-corrected estimation in mildly explosive autoregressions | 2015 | — | X7 | none | twin of eru-0204 (Kaufmann-Kruse bias-corrected mildly explosive estimation) | A3 single-screener exclude (other screener X6) |
| eru-0332 | Bubbling over! The behaviour of oil futures along the yield curve | 2015 | 10.1016/j.jempfin.2015.08.009 | X1 | openalex-oa | GSADF/BSADF application to oil futures; simulated CVs only, no OC | both-exclude |
| eru-0334 | Date Stamping Bubbles in Real Estate Investment Trusts | 2015 | 10.2139/ssrn.2722343 | X1 | openalex-oa | SADF/GSADF REIT application; simulated critical values only | A3 single-screener exclude (other screener X6) |
| eru-0340 | Episodes of Exuberance in Housing Markets: In Search of the Smoking Gun | 2015 | 10.1007/s11146-015-9531-2 | X1 | openalex-oa | SADF/GSADF applied to 22 housing markets; simulated CVs, no OC | both-exclude |
| eru-0344 | Explosive Behaviour in Australian Housing Markets: Rational Bubbles or Not? | 2015 | 10.2139/ssrn.2704108 | X1 | repository | SADF/GSADF Australian housing application; no OC | A3 single-screener exclude (other screener X6) |
| eru-0345 | Explosive bubbles in house prices? Evidence from the OECD countries | 2015 | 10.1016/j.intfin.2015.07.006 | X1 | openalex-oa | SADF/GSADF house-price application; no operating characteristics | A3 single-screener exclude (other screener X6) |
| eru-0364 | Is the United States in the middle of a healthcare bubble? | 2015 | 10.1007/s10198-015-0668-y | X1 | publisher | GSADF plus switching regression on US healthcare prices; MC for CVs only | A3 single-screener exclude (other screener X6) |
| eru-0365 | JOURNAL OF TIME SERIES ECONOMETRICS | 2015 | 10.1515/jtse | I1 | publisher | journal-level metadata record, not a study | both-exclude |
| eru-0367 | Limit theory for an explosive autoregressive process | 2015 | 10.1016/j.econlet.2014.12.004 | S-b-fail | repository | explosive AR limit theory (via SMU twin text); no time-indexed detector | A3 single-screener exclude (other screener X6) |
| eru-0368 | Limit Theory for Continuous Time Systems with Mildly Explosive Regressors | 2015 | — | S-b-fail | publisher | continuous-time mildly explosive limit theory; no time-indexed detector | A3 single-screener exclude (other screener X6) |
| eru-0369 | Monitoring Stationarity and Cointegration | 2015 | 10.2139/ssrn.2624657 | X7 / S-a-fail | none | SSRN twin of eru-0300 (Wagner-Wied monitoring stationarity/cointegration) // R2: Stationarity/cointegration monitoring; alternative is I(1), not ex... | both-exclude, code conflict |
| eru-0375 | Real estate market in Lebanon, real demand or a possible bubble? - | 2015 | — | X1 | repository | MBA project applying GSADF to Lebanon real estate; no OC | A3 single-screener exclude (other screener X6) |
| eru-0380 | Speculative bubbles in Bitcoin markets? An empirical investigation into the... | 2015 | 10.1016/j.econlet.2015.02.029 | I1 | openalex-oa | Econophysics fundamental-value model; no in-scope detector | A3 single-screener exclude (other screener X6) |
| eru-0394 | Testing for Multiple Bubbles in the 35 Large and Medium Cities of Real Esta... | 2015 | — | X1 | repository | backward GSADF application to Chinese city housing; simulated CVs only, no own OC | A3 single-screener exclude (other screener X6) |
| eru-0403 | The Test of Multiple Price Bubbles in Tehran Stock Market: an Application o... | 2015 | 10.18869/acadpub.jemr.6.21.7 | X1 | openalex-oa | GSADF/BSADF application to Tehran stock market; no OC | A3 single-screener exclude (other screener X6) |
| eru-0408 | 1 FINANCIAL BUBBLE DETECTION : A NON-LINEAR METHOD WITH APPLICATION TO S & ... | 2016 | — | I1 | repository | ANN-Bayesian nonlinear bubble dating; no explosive-AR null with reference distribution | A3 single-screener exclude (other screener X6) |
| eru-0411 | Análisis de procesos explosivos en el precio de los activos financieros: ev... | 2016 | 10.14718/revfinanzpolitecon.2016.8.1.5 | X1 | openalex-oa | Spanish application of explosive-root tests worldwide; no OC | both-exclude |
| eru-0413 | An empirical investigation of bubble and contagion effects in the Thai stoc... | 2016 | — | I1 | repository | thesis applying regime-switching bubble models to Thai market; no in-scope detector test | A3 single-screener exclude (other screener X6) |
| eru-0414 | A Note on Testing for the Periodically Collapsing Bubbles in Japanese REIT ... | 2016 | — | X2 | repository | MTAR cointegration bubble existence tests on Japanese REITs; no time-indexed output | A3 single-screener exclude (other screener X6) |
| eru-0422 | Asymptotic Inference for AR(1) Penal Data | 2016 | 1611.04248 | S-b-fail | arxiv | panel AR(1) estimation limit theory incl. explosive; no time-indexed detector | both-exclude |
| eru-0438 | Double asymptotics for explosive continuous time models | 2016 | 10.1016/j.jeconom.2016.02.014 | S-b-fail | repository | published twin of eru-0128: double asymptotics for explosive continuous-time estimation | A3 single-screener exclude (other screener X6) |
| eru-0451 | Explosive Bubbles and Cyclical Linkages of the Asia Pacific Housing Prices | 2016 | 10.66674/m1eyj576 | X1 | openalex-oa | SADF/GSADF application to Asia-Pacific housing; no OC | both-exclude |
| eru-0453 | Explosive earnings dynamics: Whoever has will be given more | 2016 | — | S-b-fail | repository | panel explosiveness test on earnings; full-sample, no time-indexed output | A3 single-screener exclude (other screener X6) |
| eru-0454 | Explosive oil prices | 2016 | 10.1016/j.eneco.2016.09.012 | X1 | repository | PWY/PSY sequences applied to oil; no own OC | A3 single-screener exclude (other screener X6) |
| eru-0462 | Identifying Currency Bubbles using Markov-Switching Models: The Latin Ameri... | 2016 | 10.34626/9knz-5s23 | X1 | openalex-oa | GSADF plus MS models applied to Latin American currencies; no OC | A3 single-screener exclude (other screener X6) |
| eru-0464 | Inflation and Bubbles in the Japanese Condominium Market | 2016 | — | X1 | repository | RADF/SADF/GSADF application to Japanese condominiums; no OC | A3 single-screener exclude (other screener X6) |
| eru-0475 | New evidence for explosive behavior of commodity prices | 2016 | — | X1 | publisher | panel GSADF with Hommel multiple-test wrapper on commodities; no OC reported | both-exclude |
| eru-0476 | Non-linearities in financial bubbles: Theory and Bayesian evidence from S&P500 | 2016 | 10.1016/j.jfs.2016.04.007 | I1 / S-c-fail | openalex-oa | ANN-Bayesian nonlinear bubble dating; no explosive-AR null with reference distribution // R2: Bayesian recursive date-stamping; no null reference d... | both-exclude, code conflict |
| eru-0477 | NON-LINEARITIES IN FINANCIAL BUBBLES : THEORY & BAYESIAN EVIDENCE FROM S & ... | 2016 | — | I1 / X7 | repository | working-paper twin of ANN-Bayesian dating paper; same S-c failure // R2: WP twin of eru-0476; same work | both-exclude, code conflict |
| eru-0479 | Periodically collapsing bubbles in the South African stock market | 2016 | 10.1016/j.ribaf.2016.04.010 | X1 | repository | GSADF South Africa application; no OC | A3 single-screener exclude (other screener X6) |
| eru-0484 | Recurrent explosive behaviour of debt-to-GDP ratio | 2016 | — | X1 | repository | SADF/GSADF application to debt-to-GDP ratios; no OC | A3 single-screener exclude (other screener X6) |
| eru-0486 | Renewed Momentum in the German Housing Market: Real-Time Monitoring of Boom... | 2016 | — | X1 | repository | recursive unit-root tests on German housing with fundamentals; no OC | A3 single-screener exclude (other screener X6) |
| eru-0492 | Speculative Bubbles or Market Fundamentals? An Investigation of US Regional... | 2016 | 10.2139/ssrn.2814791 | X7 | none | SSRN twin of eru-0427 (Shi fundamental-adjusted BSADF housing) | A3 single-screener exclude (other screener X6) |
| eru-0498 | Testing Bubbles: Exuberance and collapse in the Shanghai A-share stock market | 2016 | 10.22459/cnseg.07.2016.11 | X1 | openalex-oa | SADF/GSADF application to Shanghai A-shares; no OC | both-exclude |
| eru-0501 | Testing for Speculative Bubbles in Large-Dimensional Financial Panel Data Sets | 2016 | — | X7 | none | WP twin of eru-1225 (right-tailed PANIC); same work | A3 single-screener exclude (other screener X6) |
| eru-0509 | The oil price crash in 2014/15: Was there a (negative) financial bubble? | 2016 | 10.1016/j.enpol.2016.06.020 | X1 | openalex-oa | PSY and LPPL oil-crash application; no operating characteristics | A3 single-screener exclude (other screener X6) |
| eru-0527 | Bubble Detection in the Malaysian Housing Market | 2017 | 10.22452/mjes.vol54no2.2 | X1 | openalex-oa | PSY application to Malaysian housing; no OC | both-exclude |
| eru-0535 | Datestamping the Bitcoin and Ethereum Bubbles | 2017 | 10.2139/ssrn.3079712 | X7 | none | SSRN twin of eru-0593 (retracted FRL Bitcoin/Ethereum datestamping) | A3 single-screener exclude (other screener X6) |
| eru-0538 | Detecting Financial Bubbles Using Gap between Common Stocks and Preferred S... | 2017 | — | I1 | repository | common-preferred stock gap index; no null-referenced explosive-AR test | A3 single-screener exclude (other screener X6) |
| eru-0542 | Do 18th century ‘bubbles’ survive the scrutiny of 21st century time series ... | 2017 | 10.1016/j.econlet.2017.09.004 | X1 | repository | PSY on 18th-century bubbles; bootstrap critical values only | A3 single-screener exclude (other screener X6) |
| eru-0544 | Do bubbles have an explosive signature in markov switching models? | 2017 | 10.1016/j.econmod.2017.06.001 | I2 / S-c-fail | openalex-oa | Bayesian MS-BMA explosive-signature study; no OC for in-scope detectors // R2: Bayesian Markov-switching classification; no null reference distribu... | both-exclude, code conflict |
| eru-0547 | Do iron ore price bubbles occur? | 2017 | 10.1016/j.resourpol.2017.08.003 | X1 | publisher | GSADF application to iron ore prices; no OC | A3 single-screener exclude (other screener X6) |
| eru-0548 | DP 2017 / 02 Explosiveness in G 11 currencies ∗ | 2017 | — | X7 | repository | RBNZ DP record duplicating eru-0555 (Steenkamp, Explosiveness in G11 currencies) | both-exclude |
| eru-0551 | Essays on value at risk and asset price bubbles | 2017 | — | X1 | publisher | thesis using BSADF dating to define VaR backtest periods; no OC | A3 single-screener exclude (other screener X6) |
| eru-0555 | Explosiveness in G11 currencies | 2017 | 10.1016/j.econmod.2017.08.007 | X1 | repository | robust explosiveness tests applied to G11 currencies (via RBNZ DP twin); no own OC | A3 single-screener exclude (other screener X6) |
| eru-0557 | Exuberance in British Share Prices during the Railway Mania of the 1840s: E... | 2017 | — | X1 | repository | PSY application to 1840s railway mania share prices; no OC | A3 single-screener exclude (other screener X6) |
| eru-0558 | Exuberance in the U.K. Regional Housing Markets | 2017 | — | X1 | repository | GSADF/panel application to UK regional housing; simulated CVs only | A3 single-screener exclude (other screener X6) |
| eru-0562 | Harvey, David I. and Leybourne, Stephen J. and Sollis, Robert and Taylor, A... | 2017 | — | X7 | none | mangled citation record duplicating eru-0503 (KI-06 HLST 2016) | both-exclude |
| eru-0568 | Identifying bubbles in Latin American equity markets: Phillips-Perron-based... | 2017 | 10.1016/j.ememar.2017.09.001 | X1 | repository | Phillips-Perron-based recursive application to Latin America; no own OC | A3 single-screener exclude (other screener X6) |
| eru-0571 | Inference in continuous systems with mildly explosive regressors | 2017 | 10.1016/j.jeconom.2017.08.016 | S-b-fail | openalex-oa | continuous-system mildly explosive inference; estimation theory, no detector | A3 single-screener exclude (other screener X6) |
| eru-0572 | In-fill Asymptotic Theory for Structural Break Point in Autoregression: A U... | 2017 | — | X7 | none | WP twin of eru-0998 (Econometric Reviews 2020), per its own abstract | A3 single-screener exclude (other screener X6) |
| eru-0589 | Quantitative Easing and Exuberance in Government Bond Markets: Evidence fro... | 2017 | 10.2139/ssrn.3035371 | X1 | repository | GSADF bond-market application; simulated critical values only | A3 single-screener exclude (other screener X6) |
| eru-0590 | Random Coefficient Continuous Systems: Testing for Extreme Sample Path Beha... | 2017 | 10.2139/ssrn.3085943 | X7 | none | SSRN twin of eru-0883 (random coefficient continuous systems) | both-exclude |
| eru-0592 | Residential Property Price Determination and Bubble Detection: Evidence fro... | 2017 | — | X1 | repository | SADF/GSADF application to seven housing markets; no OC | A3 single-screener exclude (other screener X6) |
| eru-0593 | RETRACTED: Datestamping the Bitcoin and Ethereum bubbles | 2017 | 10.1016/j.frl.2017.12.006 | X1 | openalex-oa | retracted FRL article; PWY/PSY application to Bitcoin/Ethereum; no OC | A3 single-screener exclude (other screener X6) |
| eru-0594 | Rtadf: Testing for Bubbles with EViews | 2017 | 10.18637/jss.v081.c01 | X1 | publisher OA (JSS PDF, doi:10.18637/jss.v081.c01) | Software add-in; SS5 S&P500 illustration reports only test outcomes; Table 2 gives runtimes; CVs replicate PSY Table 8; no O1-O4 reported. | blind adjudication -> exclude |
| eru-0598 | STRUCTURAL CHANGE IN NONSTATIONARY AR(1) MODELS | 2017 | 10.1017/s0266466617000317 | S-c-fail | repository | break-point and t-ratio estimation asymptotics in explosive AR; no null-referenced time-indexed rule | both-exclude |
| eru-0600 | Testing for bubbles in stock markets with irregular dividend distribution | 2017 | 10.1016/j.frl.2017.12.015 | X1 | repository | GSADF with wild bootstrap p-values; application only | A3 single-screener exclude (other screener X6) |
| eru-0605 | Testing for Multiple Bubbles in Asset Prices 1 | 2017 | — | X7 | repository | same-work duplicate of eru-0604 (MaRBLe DOI version) | both-exclude |
| eru-0606 | Testing for Multiple Bubbles in Iranian Foreign Exchange Market:The Applica... | 2017 | 10.29252/jemr.7.27.7 | X1 | openalex-oa | RTADF application to Iranian FX market; no OC | both-exclude |
| eru-0618 | UNIVERSITY OF WAIKATO Hamilton New Zealand Bubble Contagion: Evidence from ... | 2017 | — | X1 / X7 | repository | PSY application to Japan stock/real-estate, contagion; no OC // R2: Waikato WP twin of eru-0647; same title | both-exclude, code conflict |
| eru-0625 | 글로벌 부동산 버블 위험 진단 및 영향 분석 (A Diagnosis of Bubble Risk in the Global Real Est... | 2018 | 10.2139/ssrn.3300034 | X1 | openalex-oa | GSADF plus cointegration applied to global real estate (Korean); no OC | A3 single-screener exclude (other screener X6) |
| eru-0628 | An Anatomy of Stock Market Bubbles | 2018 | 10.3968/10513 | I2 / I2-fail | openalex-oa | survey of bubble definitions and detection methods; no theory, simulation, or OC // R2: Survey/anatomy of bubble definitions and tests; no OC or th... | both-exclude, code conflict |
| eru-0629 | An Examination of the Occurrence of Speculative Bubbles in the US Stock Mar... | 2018 | — | X1 | repository | GSADF application to US indexes; simulated CVs only, no OC | A3 single-screener exclude (other screener X6) |
| eru-0634 | A supreme test for periodic explosive GARCH | 2018 | 1812.03475 | X4 / X7 | arxiv | GARCH parameter-change test; null and alternative strictly stationary, no explosive-root alternative // R2: arXiv twin of eru-1544 (Richter-Wang-Wu... | both-exclude, code conflict |
| eru-0647 | Bubble contagion: Evidence from Japan’s asset price bubble of the 1980-90s | 2018 | 10.1016/j.jjie.2018.09.002 | X1 | repository | PSY plus contagion test applied to Japan; no OC | A3 single-screener exclude (other screener X6) |
| eru-0650 | Bubbles in US regional house prices: evidence from house price–income ratio... | 2018 | 10.1080/00036846.2017.1418080 | X1 | repository | PSY applied to US state house-price ratios; no OC | A3 single-screener exclude (other screener X6) |
| eru-0657 | Co-explosivity in the cryptocurrency market | 2018 | 10.1016/j.frl.2018.07.005 | X1 | publisher | GSADF co-explosivity application to cryptocurrencies; no OC | A3 single-screener exclude (other screener X6) |
| eru-0678 | Diagnosing Housing Bubbles across Rich Countries | 2018 | 10.5539/ijef.v10n4p179 | X1 | openalex-oa | GSADF plus probit application to housing; no OC | both-exclude |
| eru-0679 | DIPARTIMENTO DI SCIENZE ECONOMICHE ED AZIENDALI “M.FANNO” CORSO DI LAUREA M... | 2018 | — | X1 | repository | masters thesis applying PSY to cryptocurrencies; no OC | A3 single-screener exclude (other screener X6) |
| eru-0692 | exuber: Econometric Analysis of Explosive Time Series | 2018 | 10.32614/cran.package.exuber | I2 | CRAN reference manual PDF (doi:10.32614/cran.package.exuber) | Package manual: function documentation only (radf, datestamp, radf_mc_cv pp.6-7,17); no derivation, no simulated OC, no application; fails I2a/I2b/... | blind adjudication -> exclude |
| eru-0701 | Identification of Rational Bubbles in Emerging Markets of SAARC | 2018 | — | X1 | repository | SADF application to SAARC markets; no OC | A3 single-screener exclude (other screener X6) |
| eru-0728 | On parameter estimation of state space models and its applications | 2018 | 10.7282/t3r214td | I1 | openalex-oa | thesis: state-space SMC bubble filtering; no null-referenced time-indexed test | A3 single-screener exclude (other screener X6) |
| eru-0751 | Testing for moderate explosiveness | 2018 | 10.1111/ectj.12120 | S-a-fail | repository | Journal version of eru-0752; assessed on WP text; explosiveness is null, no dating | A3 single-screener exclude (other screener X6) |
| eru-0752 | Testing for Moderate Explosiveness in the Presence of Drift | 2018 | — | S-b-fail / S-a-fail | openalex-oa | t-test with moderate-explosiveness null; full-sample degree inference, no time-indexed output // R2: Null is moderate explosiveness (degree test); ... | both-exclude, code conflict |
| eru-0765 | Time-Varying Parameters in Continuous and Discrete Time | 2018 | — | I2 | repository | continuous-discrete time correspondence theory; no null distribution, CVs, or OC | A3 single-screener exclude (other screener X6) |
| eru-0766 | Too Much or Less? Money Supply in Japan | 2018 | 10.24818/18423264/52.3.18.02 | X1 | openalex-oa | GSADF application to Japanese money supply; no OC | both-exclude |
| eru-0768 | Using Market Expectations to Test for Speculative Bubbles in the Crude Oil ... | 2018 | 10.1111/jmcb.12525 | X1 | openalex-oa | GSADF/IVX with market expectations applied to oil; no own OC | A3 single-screener exclude (other screener X6) |
| eru-0788 | Another Look at Cryptocurrency Bubbles | 2019 | 10.2139/ssrn.3424726 | X1 | repository | PWY-type dating applied to cryptocurrencies; simulated CVs only | A3 single-screener exclude (other screener X6) |
| eru-0819 | Dating the start of the US house price bubble: an application of statistica... | 2019 | 10.1007/s00181-019-01648-x | X4 | repository | SPC control charts for mean shifts in price growth; no explosive-AR alternative | A3 single-screener exclude (other screener X6) |
| eru-0821 | Detecting bubbles in Bitcoin price dynamics via market exuberance | 2019 | 10.1007/s10479-019-03321-z | I1 | publisher | continuous-time attention model, Protter mathematical bubble; no explosive-AR null test | A3 single-screener exclude (other screener X6) |
| eru-0822 | Detecting Bubbles in the US and UK Real Estate Markets | 2019 | 10.1007/s11146-018-9693-9 | X1 | publisher | shrinkage regressions plus SADF/GSADF dating on real estate; no OC | both-exclude |
| eru-0844 | Estimating Multiple Breaks in Nonstationary Autoregressive Models ∗ August ... | 2019 | — | S-c-fail / X7 | repository | multiple-break LSE estimation theory for explosive AR; no null-referenced decision rule // R2: WP twin of eru-0978; same title and date | both-exclude, code conflict |
| eru-0846 | Examining Rational Bubbles in Oil Prices : Evidence from Frequency Domain E... | 2019 | — | I1 | repository | frequency-domain econophysics bubble identification; no explosive-AR detector applied | A3 single-screener exclude (other screener X6) |
| eru-0849 | Explosiveness in foreign remittance inflow to Pakistan | 2019 | — | X1 | repository | rolling ADF/GSADF application to Pakistan remittances; no OC | A3 single-screener exclude (other screener X6) |
| eru-0852 | Financial Bubbles : New Evidence from South Africa’s Stock Market | 2019 | — | X1 | repository | GSADF application to South Africa stock market; no OC | A3 single-screener exclude (other screener X6) |
| eru-0854 | Fundamental bubbles in equity markets | 2019 | 10.1007/s00500-019-04514-1 | I1 | publisher | affine-model bubble measure via nonstationary discrepancies; no explosive-AR detector | A3 single-screener exclude (other screener X6) |
| eru-0859 | Institutional Knowledge at Singapore Management University Limit Theory for... | 2019 | — | X7 | repository | SMU IR duplicate of eru-0367 (Wang-Yu explosive AR limit theory) | both-exclude |
| eru-0860 | Institutional Knowledge at Singapore Management University Limit Theory for... | 2019 | — | X7 | repository | SMU IR duplicate of eru-0100 (PY2009 dating limit theory) | both-exclude |
| eru-0861 | Institutional Knowledge at Singapore Management University Mild-explosive a... | 2019 | — | S-b-fail / X7 | repository | mild-explosive AR with serially correlated errors; estimation theory only // R2: SMU listing duplicate of eru-1011 | both-exclude, code conflict |
| eru-0862 | INTERROGATION OF A BUBBLE IN THE INDIAN MARKET | 2019 | 10.34218/jom.6.3.2019.008 | X1 | repository | GSADF application to Indian indices; simulated CVs only | both-exclude |
| eru-0869 | Kripto Para Değerleri için Spekülatif Fiyat Balonlarının Test Edilmesi :... | 2019 | — | X1 | repository | GSADF application to Bitcoin (Turkish); no OC | A3 single-screener exclude (other screener X6) |
| eru-0873 | Mild explosivity in recent crude oil prices | 2019 | 10.1016/j.eneco.2019.05.002 | X1 | openalex-oa | PSY application to crude oil with robustness checks; no OC with stated null | both-exclude |
| eru-0888 | Sentiment-Induced Bubbles in the Cryptocurrency Market | 2019 | 10.3390/jrfm12020053 | S-c-fail | openalex-oa | sentiment smooth-transition AR bubble model; no null-referenced time-indexed decision | both-exclude |
| eru-0900 | Testing for Exuberance Behavior in Agricultural Commodities of Pakistan | 2019 | — | X1 | repository | GSADF application to Pakistani agricultural commodities; no OC | A3 single-screener exclude (other screener X6) |
| eru-0901 | Testing for Multiple Bubbles in Inflation for Pakistan | 2019 | — | X1 | repository | GSADF application to Pakistani inflation series; no OC | A3 single-screener exclude (other screener X6) |
| eru-0903 | Testing for randomness in a random coefficient autoregression model | 2019 | 10.1016/j.jeconom.2019.01.005 | S-a-fail | repository | Granger DP 18/03: randomness test for RCA coefficient; alternative not explosive root | A3 single-screener exclude (other screener X6) |
| eru-0907 | TESTING MULTIPLE FINANCIAL BUBBLES IN THE NASDAQ INDEX | 2019 | — | X1 | repository | SWER application of recursive tests to Nasdaq; no OC | A3 single-screener exclude (other screener X6) |
| eru-0926 | What Can Predict Bubbles in Cryptocurrency Prices? Identification and expla... | 2019 | — | X1 | repository | thesis: PSY applied to cryptocurrencies plus logit predictors; no OC | A3 single-screener exclude (other screener X6) |
| eru-0928 | Whether the Multiple Bubbles Exist in the Bond Markets of Developed Countries? | 2019 | — | X1 | repository | SADF/GSADF application to developed-country bond markets; no OC | A3 single-screener exclude (other screener X6) |
| eru-0949 | Avaliação de bolhas no mercado brasileiro de capitais: um estudo setorial | 2020 | 10.13059/racef.v11i3.704 | I1 | openalex-oa | Brazilian sectoral AR(1) bubble assessment; no null-referenced explosive-AR test | A3 single-screener exclude (other screener X6) |
| eru-0960 | Date-stamping the Tadawul bubble through the SADF and GSADF econometric app... | 2020 | — | X1 | repository | SADF/GSADF date-stamping of Tadawul bubble; no OC | A3 single-screener exclude (other screener X6) |
| eru-0975 | Empirical analysis of market behaviour: a mesoscopic approach | 2020 | 10.6035/14102.2020.253593 | X1 | openalex-oa | agent-based thesis using GSADF only to mark bubble periods; no OC | A3 single-screener exclude (other screener X6) |
| eru-0976 | EMPIRICAL TESTS OF STOCK MARKET BUBBLES IN CHINA BASED ON GSADF METHOD | 2020 | 10.46609/ijsser.2020.v05i03.004 | X1 | openalex-oa | GSADF application to Chinese stock indices; no OC | both-exclude |
| eru-0978 | Estimating multiple breaks in nonstationary autoregressive models | 2020 | 10.1016/j.jeconom.2020.06.005 | S-c-fail | repository | Break-date estimation theory for bubble regimes; no null-referenced test | A3 single-screener exclude (other screener X6) |
| eru-0981 | exuber: Recursive Right-Tailed Unit Root Testing with R | 2020 | 10.24149/gwp383 | X7 | repository (Dallas Fed GWP 383 PDF, doi:10.24149/gwp383) | Title, authors, abstract identical to JSS exuber paper (eru-1251, doi:10.18637/jss.v103.i10); same-work twin under SS4.1 title-match rule. | blind adjudication -> exclude |
| eru-0994 | How explosive are cryptocurrency prices? | 2020 | 10.1016/j.frl.2020.101603 | X1 | repository | PWY-style explosiveness applied to cryptocurrencies; no OC | A3 single-screener exclude (other screener X6) |
| eru-0999 | Institutional Knowledge at Singapore Management University Institutional Kn... | 2020 | — | X7 | repository | SMU IR duplicate of eru-0367 (same article 2512) | both-exclude |
| eru-1000 | International Journal of Social Science and Economic Research | 2020 | — | I1 | repository | agent-based price-limit simulation; no in-scope detector | both-exclude |
| eru-1011 | Mild-explosive and local-to-mild-explosive autoregressions with serially co... | 2020 | — | X7 | none | duplicate of eru-0861 (same SMU working paper, title match) | A3 single-screener exclude (other screener X6) |
| eru-1012 | Mildly Explosive Autoregression with Anti‐persistent Errors* | 2020 | 10.1111/obes.12395 | S-b-fail | repository | mildly explosive AR with anti-persistent errors (via SMU twin); estimation theory | A3 single-screener exclude (other screener X6) |
| eru-1013 | Mildly explosive dynamics in U.S. fixed income markets | 2020 | 10.1016/j.ejor.2020.03.053 | X1 | openalex-oa | GSADF application to US fixed-income spreads; no OC | both-exclude |
| eru-1016 | Model Selection for Explosive Models | 2020 | 10.1108/s0731-905320200000041003 | S-b-fail / S-c-fail | arxiv | information-criteria selection between UR and explosive models; no time-indexed output // R2: Information-criterion model selection UR vs explosive... | both-exclude, code conflict |
| eru-1020 | Nordic house price bubbles? | 2020 | — | X1 | repository | BSADF plus cointegration application to Nordic housing; no OC | A3 single-screener exclude (other screener X6) |
| eru-1023 | Point optimal testing with roots that are functionally local to unity | 2020 | 10.1016/j.jeconom.2020.03.003 | S-b-fail | repository | point-optimal FLUR tests incl. explosive subperiods; full-sample presence test, no dating | A3 single-screener exclude (other screener X6) |
| eru-1027 | Probabilistic forecasting of bubbles and flash crashes | 2020 | 10.1093/ectj/utaa004 | S-c-fail | repository | NERC predictive-probability model (ESSEC WP twin); no null-referenced time-t decision | A3 single-screener exclude (other screener X6) |
| eru-1040 | Speculative bubbles in segmented markets: Evidence from Chinese cross-liste... | 2020 | 10.1016/j.jimonfin.2020.102222 | X1 | openalex-oa | GSADF application to A-H price differentials; no OC | both-exclude |
| eru-1043 | Study on the Price Bubble of XRP | 2020 | — | I1 | repository | XRP intrinsic-value bubble measurement; no explosive-AR detector applied | A3 single-screener exclude (other screener X6) |
| eru-1050 | Testing for multiple bubbles in the copper price: Periodically collapsing b... | 2020 | 10.1016/j.resourpol.2020.101587 | X1 | openalex-oa | GSADF application to copper price; no OC | both-exclude |
| eru-1053 | The bubble contagion effect of COVID-19 outbreak: Evidence from crude oil a... | 2020 | 10.1016/j.frl.2020.101703 | X1 | openalex-oa | PSY real-time procedure applied to oil/gold COVID contagion; no OC | A3 single-screener exclude (other screener X6) |
| eru-1067 | Unit root tests for explosive behaviour | 2020 | — | I3 | repository | conference slides on Stata radf command; no DOI/arXiv/handle; best locator RePEc/BC | A3 single-screener exclude (other screener X6) |
| eru-1100 | Booms and Busts in the Oil Market: Identifying Speculative Bubbles Using a ... | 2021 | 10.1155/2021/8883416 | X1 | openalex-oa | continuous-time random-persistence detection applied to oil; no own OC | A3 single-screener exclude (other screener X6) |
| eru-1105 | Bubbles During Covid-19 Period: Evidence from the United States Using the G... | 2021 | 10.2478/hjbpa-2021-0005 | X1 | openalex-oa | GSADF application to Dow Jones COVID period; no OC | both-exclude |
| eru-1107 | Bubbles in the Field | 2021 | — | I1 | repository | quasi-control-asset bubble test via Cantelli bounds; no explosive-AR alternative | A3 single-screener exclude (other screener X6) |
| eru-1108 | Bubbles in US gasoline prices: Assessing the role of hurricanes and anti–pr... | 2021 | 10.1016/j.jcomm.2021.100219 | X1 | repository | rolling right-tailed unit-root application to gasoline prices; no OC | both-exclude |
| eru-1123 | Diagnosing housing fever with an econometric thermometer | 2021 | 10.1111/joes.12430 | I2 | repository | selective review and practice guide with application; no original theory or OC | A3 single-screener exclude (other screener X6) |
| eru-1126 | Does COVID-19 Drive Stock Price Bubbles in Medical Mask? | 2021 | 10.46557/001c.22976 | X1 | openalex-oa | SADF/GSADF application to medical mask stocks; no OC | both-exclude |
| eru-1132 | Emerging stock market exuberance and international short-term flows | 2021 | 10.1016/j.intfin.2021.101417 | X1 | repository | PSY date-stamping applied to EME flows; no OC | A3 single-screener exclude (other screener X6) |
| eru-1158 | Institutional Knowledge at Singapore Management University Institutional Kn... | 2021 | — | X7 | repository | SMU IR duplicate of eru-1012 | A3 single-screener exclude (other screener X6) |
| eru-1162 | KOVİD-19 SÜRECİNDE SEKTÖR ENDEKSLERİNİN FİYAT BALONLARI AÇISINDAN TEST EDİL... | 2021 | — | X1 | repository | GSADF application to Borsa Istanbul sector indices; no OC | A3 single-screener exclude (other screener X6) |
| eru-1172 | On the Asymptotic Behavior of Bubble Date Estimators | 2021 | 10.2139/ssrn.3939356 | S-c-fail | arxiv | four-regime bubble date estimation asymptotics; no null-referenced decision rule | both-exclude |
| eru-1179 | Quantitative easing and exuberance in stock markets: Evidence from the euro... | 2021 | 10.1016/j.jimonfin.2021.102471 | X1 | openalex-oa | BSADF euro-area QE application; simulated CVs only | A3 single-screener exclude (other screener X6) |
| eru-1208 | The nexus of renewable energy equity and agricultural commodities in the Un... | 2021 | 10.1016/j.energy.2021.122377 | X1 | openalex-oa | Markov-switching plus SADF application to energy/agriculture; no OC | both-exclude |
| eru-1213 | Time-Transformed Test for the Explosive Bubbles under Non-stationary Volati... | 2021 | 10.2139/ssrn.3755872 | X7 | arxiv | SSRN/arXiv twin of eru-1384 (time-transformed test); carrier moved to published DOI | both-exclude |
| eru-1224 | 2022 ASYMPTOTIC THEORY FOR MODERATE DEVIATIONS FROM THE UNIT BOUNDARY IN QU... | 2022 | — | S-b-fail | arxiv | Assessed on arXiv 2204.02073 title variant: quantile AR moderate-deviation estimation | A3 single-screener exclude (other screener X6) |
| eru-1225 | A CROSS-SECTIONAL METHOD FOR RIGHT-TAILED PANIC TESTS UNDER A MODERATELY LO... | 2022 | 10.1017/s0266466622000044 | S-b-fail | publisher | Right-tailed PANIC panel existence tests; no time-indexed dating output | A3 single-screener exclude (other screener X6) |
| eru-1242 | A review of Phillips‐type right‐tailed unit root bubble detection tests | 2022 | 10.1111/joes.12524 | I2 / I2-fail | openalex-oa | review of Phillips-type tests with psymonitor demo; no original theory, sim, or OC // R2: Survey of Phillips-type tests; no new OC or theory | both-exclude, code conflict |
| eru-1251 | <b>exuber</b>: Recursive Right-Tailed Unit Root Testing with <i>R</i> | 2022 | 10.18637/jss.v103.i10 | X1 | publisher OA (JSS PDF, doi:10.18637/jss.v103.i10) | Software paper: SS4 speed benchmarks only; SS5 artificial-series demo and house-price application report test outcomes/datestamps; no O1-O4 reported. | blind adjudication -> exclude |
| eru-1278 | Dissecting the dot-com bubble in the 1990s NASDAQ | 2022 | 2206.14130 | X1 | arxiv | PSY variants applied to individual Nasdaq stocks; no OC | both-exclude |
| eru-1291 | Emtia Piyasalarında Fiyat Balonları: Covid-19 Dönemi İçin Bir İnceleme | 2022 | 10.29228/ideas.63952 | X1 | openalex-oa | SADF/GSADF application to commodities COVID period; no OC | both-exclude |
| eru-1293 | ESTIMATION AND INFERENCE WITH NEAR UNIT ROOTS | 2022 | 10.1017/s0266466622000342 | S-b-fail | openalex-oa | near-unit-root estimation and inference framework; no time-indexed detector | both-exclude |
| eru-1333 | Mildly Explosive Autoregression with Strong Mixing Errors | 2022 | 10.3390/e24121730 | S-b-fail | openalex-oa | mildly explosive AR with mixing errors; estimation limit theory only | A3 single-screener exclude (other screener X6) |
| eru-1351 | Regime Switching Mechanism during Energy Futures' Price Bubbles | 2022 | 10.32479/ijeep.12549 | X1 | openalex-oa | GSADF plus Markov-switching application to energy futures; no OC | both-exclude |
| eru-1364 | Testing for Co‐explosive Behaviour in Financial Time Series | 2022 | 10.1111/obes.12487 | S-b-fail | repository | co-explosivity stationarity test over episodes; no time-indexed explosive-state assignment | A3 single-screener exclude (other screener X6) |
| eru-1395 | Value-at-risk in the presence of asset price bubbles | 2022 | 10.1080/15140326.2021.1927441 | X1 | publisher | BSADF date-stamping used within VaR backtesting application; no detector OC | A3 single-screener exclude (other screener X6) |
| eru-1401 | An Application of the “Recursive Flexible Window” Methodology to Test for F... | 2023 | 10.33423/jabe.v25i4.6346 | X1 | openalex-oa | PSY application to Indian indices; recaps PSY simulations, no own OC | both-exclude |
| eru-1404 | An Investigation on Real Estate Market Dynamics and Bubble Formation Modeling | 2023 | 10.2478/picbe-2023-0144 | I2 / I2-fail | openalex-oa | conference survey of housing bubble modeling; no theory, simulation, or OC // R2: Survey-style proceedings paper; no own application or OC | both-exclude, code conflict |
| eru-1420 | Based on GSADF model - To study the impact of surging cross-border capital ... | 2023 | 10.54097/hbem.v18i.12792 | X1 | openalex-oa | GSADF surge measurement plus growth regressions; no OC | both-exclude |
| eru-1442 | Detecting housing bubble in Poland: Investigation into two housing booms | 2023 | 10.1016/j.habitatint.2023.102928 | X1 | repository | SADF/GSADF Polish housing application | A3 single-screener exclude (other screener X6) |
| eru-1486 | Improving the Accuracy of Bubble Date Estimators Under Time-Varying Volatility | 2023 | 10.2139/ssrn.4469884 | S-c-fail | arxiv | WLS bubble-date estimation under time-varying volatility; no null-referenced decision rule | both-exclude |
| eru-1506 | Multiple-bubble testing in the cryptocurrency market: a case study of bitcoin | 2023 | 2401.05417 | X1 | arxiv | RTADF/GSADF application to Bitcoin; no OC | both-exclude |
| eru-1516 | Quickest Detection Problems for Ornstein–Uhlenbeck Processes | 2023 | 10.1287/moor.2021.0186 | X4 | openalex-oa | OU mean-reversion-change quickest detection; general changepoint, explosivity not the stated alternative | both-exclude |
| eru-1540 | Testing for explosive bubbles: a review | 2023 | 10.1515/demo-2022-0152 | I2 / I2-fail | arxiv | review of explosive-bubble testing methods; no original theory, simulation, or OC // R2: Review of explosive-bubble testing; no new OC | both-exclude, code conflict |
| eru-1544 | Testing for parameter change epochs in GARCH time series | 2023 | 10.1093/ectj/utad006 | X4 | repository (White Rose eprints, published OA version, doi:10.1093/ectj/utad006) | Alternative is GARCH parameter-change epoch (volatility recursion alpha1+beta1>=1, Lee-Hansen sense); 'test is not of unit-root type' (p.470); no r... | blind adjudication -> exclude |
| eru-1549 | The Detection of Asset Price Bubbles in the Cryptocurrency Markets with an ... | 2023 | 10.2139/ssrn.4316094 | I1 | openalex-oa | Strict-local-martingale model-risk framework; no section-2.1 detector | A3 single-screener exclude (other screener X6) |
| eru-1594 | Asymptotic theory for explosive fractional Ornstein-Uhlenbeck processes | 2024 | 10.1214/24-ejs2293 | S-b-fail | openalex-oa | explosive fractional OU estimation asymptotics; no time-indexed detector | both-exclude |
| eru-1602 | Bitcoin’s bubbly behaviors: does it resemble other financial bubbles of the... | 2024 | 10.1057/s41599-024-03220-0 | I1 | openalex-oa | descriptive comparison of Bitcoin with historical bubbles; no in-scope detector | both-exclude |
| eru-1607 | Bubble Spillover of Assets: Evidence from the Exchange Rates of Some Newly ... | 2024 | 10.26650/ekoist.2024.41.1418412 | X1 | openalex-oa | GSADF exchange-rate bubble spillover application; no OC | A3 single-screener exclude (other screener X6) |
| eru-1618 | Comparative Analysis of Stock Bubble in S&P 500 Individual Stocks: A Study ... | 2024 | 10.3390/jrfm17020059 | X1 | openalex-oa | SADF/GSADF comparison on S&P500 stocks; MC only for critical values | A3 single-screener exclude (other screener X6) |
| eru-1625 | Detecting house price bubbles in G7 countries: New evidence and heterogeneo... | 2024 | 10.1016/j.frl.2024.106107 | X1 | openalex-oa | GSADF/BSADF application to G7 housing plus determinants; no OC | A3 single-screener exclude (other screener X6) |
| eru-1671 | INFERENCE IN MILDLY EXPLOSIVE AUTOREGRESSIONS UNDER UNCONDITIONAL HETEROSKE... | 2024 | 10.1017/s0266466624000215 | S-b-fail | repository | CI construction for mildly explosive AR under heteroskedasticity; no time-indexed detector | both-exclude |
| eru-1679 | Local powers of least‐squares‐based test for panel fractional Ornstein–Uhle... | 2024 | 10.1111/jtsa.12777 | S-b-fail | openalex-oa | panel fractional OU persistence-sign test; no time-indexed output | A3 single-screener exclude (other screener X6) |
| eru-1688 | OLS Limit Theory for Drifting Sequences of Parameters on the Explosive Side... | 2024 | 10.59576/sr.1113 | S-b-fail | publisher | OLS limit theory for drifting explosive parameters; no time-indexed detector | both-exclude |
| eru-1689 | On Bubbles in Cryptocurrency Prices | 2024 | 10.2139/ssrn.4913885 | X5 | repository | Equilibrium crypto-bubble model; no test procedure | A3 single-screener exclude (other screener X6) |
| eru-1758 | An Improved Procedure for Retrospectively Dating the Emergence and Collapse... | 2025 | 10.1111/jtsa.12810 | S-c-fail | repository | OLS-based retrospective dating estimator theory; no null-referenced decision rule | A3 single-screener exclude (other screener X6) |
| eru-1765 | A Structural Indicator for Identifying Real Estate Bubbles | 2025 | 10.3790/gjrer.2025.1465004 | I1 / S-c-fail | publisher | functional-distribution structural indicator; PSY only cited, no explosive-AR test applied // R2: Structural supply-demand indicator; no null refer... | both-exclude, code conflict |
| eru-1780 | Contagion of commodity futures price bubbles: perspectives from futures-lev... | 2025 | 10.1007/s11403-025-00441-7 | X1 | publisher | GSADF plus TVP-VAR contagion application to commodity futures; no OC | A3 single-screener exclude (other screener X6) |
| eru-1821 | Inflation or Speculative Bubbles? Observing Housing Prices in Türkiye by Us... | 2025 | 10.15388/ekon.2025.104.3.3 | X1 | openalex-oa | PANICCA plus panel GSADF application to Turkish housing; no OC | both-exclude |
| eru-1823 | Interpreting Market Behavior: Price Bubbles in the Non-Metallic Mineral Sec... | 2025 | 10.55026/jobaf.1601072 | X1 | publisher | GSADF application to BIST stone-soil index post-earthquake; no OC | A3 single-screener exclude (other screener X6) |
| eru-1843 | Real‐time detection of local no‐arbitrage violations | 2025 | 10.3982/qe2585 | S-a-fail | arxiv | sequential no-arbitrage-violation detectors; drift-burst alternative, not explosive AR root | both-exclude |
| eru-1853 | Sequential Monitoring for Changes in GARCH(1,1) Models Without Assuming Sta... | 2025 | 10.1111/jtsa.12824 | X4 | arxiv | GARCH volatility-regime monitoring; alternative concerns volatility process, not price AR root | A3 single-screener exclude (other screener X6) |
| eru-1864 | Testing for Asset Price Bubbles: An Alternative Approach | 2025 | 10.46557/001c.124262 | I1 | openalex-oa | cross-sectional core-extraction bubble identification; no null-referenced explosive-AR test | both-exclude |
| eru-1872 | The role of vaccination roll-out in the monitoring of Covid-19 pandemic spr... | 2025 | 10.1016/j.physa.2025.131160 | X1 | openalex-oa | Covariate-BSADF applied to Covid surges; no null-referenced OC reported | A3 single-screener exclude (other screener X6) |
| eru-1874 | The speculative tech bubbles of US artificial intelligence sector | 2025 | 10.17811/ebl.14.4.2025.177-192 | X1 | openalex-oa | GSADF application to AI stocks; no OC | both-exclude |
| eru-1882 | TOWARD A UNIFORM ASYMPTOTIC THEORY FOR MILDLY EXPLOSIVE AUTOREGRESSION | 2025 | 10.1017/s0266466625100224 | S-b-fail | openalex-oa | uniform Cauchy limit theory for mildly explosive AR; no time-indexed detector | both-exclude |
| eru-1959 | Near-Unit-Root Theory for Affine Processes | 2026 | 10.2139/ssrn.7210624 | S-b-fail | arxiv | near-unit-root estimation theory for affine processes; no time-indexed detector | both-exclude |
| eru-1961 | Path-Explosive Behaviour in Economic Time Series: A Realization-Centred Exp... | 2026 | 2604.16186 | S-c-fail | arxiv | realization-centred descriptive diagnostics; explicitly no null reference distribution | both-exclude |
| eru-1973 | Speculative Bubble Dynamics and Systemic Risk in Shadow Banking Institution... | 2026 | 10.65672/fs.2026.2.7 | X1 | openalex-oa | BSADF application to shadow banking equities; no OC | both-exclude |
| eru-1991 | TÜRKİYE'DE SEÇİLMİŞ İL VE İLÇELERDE KONUT FİYAT BALONU ANALİZİ: GSADF VE AD... | 2026 | 10.29228/ijbemp.90553 | X1 | openalex-oa | GSADF application to Turkish district housing; no OC | A3 single-screener exclude (other screener X6) |
| eru-1994 | Unravelling Systemic Risk Dynamics amid Financial Asset Bubbles in Times of... | 2026 | 10.24818/ea/2026/71/328 | X1 | openalex-oa | BSADF bubble identification plus systemic risk metrics; no OC | both-exclude |

## 14. What the consumer agenda should do with this (Rev 4 inputs)

Stated as inputs, not as edits: protocol §9.1 makes the agenda revision a
consumer-side action.

1. **Definitional basis (d).** The Rev 3 refutation of the universal **stands** —
   a time-*t* assignment null with a stated reference distribution does exist in
   this literature. The Rev 3 *sentence* must be corrected for statistic
   attribution and critical-value provenance; the replacement wording is drafted
   in §8.3.
2. **Branch 3 comparator set.** The recursive right-tailed family belongs there,
   with the attribution correction; **no record in this corpus** publishes the
   quantity branch 3 declares as its comparison metric for that family. The
   surveillance / monitoring line (`eru-0735`, `eru-1117`, `eru-1519`,
   `eru-1844`, `eru-1845`, `eru-0889`, `eru-1038`, `eru-1921`, `eru-1852`) —
   nine records in this corpus — does publish a false-alarm rate over a stated
   horizon in closed form and should enter the comparator set on that ground
   alone. Both halves are corpus-scoped statements bounded by L-4 (280
   unobtainable full texts) and L-5 (the backward-chase arm ran only as a
   post-freeze diagnostic); neither is a universal claim about the literature
   (§7.4, finding REV-1-13). The BSADF comparator carries a binding multiplicity
   condition: FWER 0.55–0.93 as conventionally applied, on **working-paper-tier**
   evidence (`eru-1289` = Cowles DP 2331, Table 1 p.20, §7.4), with the
   multiple-testing critical values costing mean origination-date bias
   7.56 → 12.20 months at successful-detection rate 0.84 → 0.75 (Table 2 p.21).
   All three FWER values are measured over the **same** 10-year span at
   quarterly / monthly / weekly frequency (T = 40 / 120 / 520); the earlier
   description "longer span / higher frequency" was wrong and is corrected
   (L-18). The triple and the delay figures were **re-read against the retrieved
   DP text on 2026-09-02** and verified, so VG-10 no longer bars a consumer from
   citing them, subject only to the working-paper tier.
3. **"Nearest unadjudicated candidates".** All three are adjudicated
   `episode-statistic-null` (§9), **but not on equal footing**: NB-02 and NB-08
   are adjudicated on the full text of the version at issue, while NB-13 is
   adjudicated on the 2006 IIIS DP 122 working-paper twin and its extension to
   the 2009 journal version rests on an absence-of-evidence inference, the
   journal full text never having been obtained (§9.3, §9.4, VG-3). The word
   "unadjudicated" should be removed and the three verdicts recorded **with
   NB-13's provisional status carried**, not as unqualified
   adjudicated-and-negative. Record also the NB-08 derivability note, which is
   the only route in that group to an online drawdown monitor and is TC-6, and
   the fact that none of the three ever entered the screened universe as
   protocol §9.1 required (A9, VG-9). **Carry the provenance of the qualifier
   too:** "provisional on the working-paper twin" is not in protocol §9.1's
   frozen verdict vocabulary and is registered as amendment **A13(c)**, and the
   reason for preferring it over `indeterminate-from-full-text` rests on a
   declared CONVENTION of §9.3 — the protocol leaves that token undefined and
   decides neither its meaning nor the version-mismatch case.
   *(Findings REV-1-6, REV-2-4, LITERATURE-2-6.)*
4. **Every "pending full-text pass" caveat attached to the Phillips records is
   discharged** by §8 — as a *correction*, not a confirmation. Sites in the agenda
   that carry the caveat (Definitional basis (d), branch 3, Verification status)
   should be updated to point at §8.3's verdict rather than at a pending pass.
5. **Seven `TO COMPUTE` handoffs (§11) are now specified**, none executed, per
   ADR-0003. TC-4 is the one that blocks a parameter choice: r₀ and the
   minimum-duration constant are `CONVENTION` in the family's own words and
   cannot be adopted from the literature without becoming unlabelled constants in
   this project.
6. **Page locators the agenda must correct (findings QUANT-2-3,
   LITERATURE-3-3).** **Nineteen** page references in this review were wrong and
   are corrected in §12.1 **L-18** after re-reading the retrieved source texts —
   **not fourteen**, which is the count round 2 published and which the agenda
   copied at its line "retrieved PDFs corrected 14 locators in the review". That
   sentence must be restated as **19**; it is a consumer-side correction this
   document does not make. Four further locator corrections in §9 are recorded
   separately in **L-20** and are not inside the 19. Two of them have already propagated
   into the agenda and must be fixed there, since correcting the agenda is a
   consumer-side action under protocol §9.1(i):
   - The PSY 2015a locator on **"the new date-stamping strategy may be used as an
     ex ante real-time dating procedure, whereas the GSADF test is an ex post
     statistic"** is ***IER* 56:1053**, not 1054. This appears in the agenda's
     branch-3 material and inside the prescribed Rev 4 wording drafted in §8.3.
   - The PWY 2011 locator on **"however, sup_{r∈[r₀,1]} ADF_r cannot reveal the
     location of the exuberance"** is ***IER* 52:214**, not 215.
   The quoted strings themselves verify verbatim; only the page attributions were
   wrong. If the agenda carries any further locator taken from §7, §8 or §9, it
   should be checked against L-18's table rather than against the earlier text.
7. **The backward-chase gap the agenda inherits is ONE named record, not two
   (finding LITERATURE-2-1).** `er-bc-1` Hall, Psaradakis & Sola (1999) is the
   only record the A11 diagnostic named that the corpus does not contain.
   `er-bc-2` Banerjee, Chevillon & Kratz (2013) was a false positive — that work
   is in the universe as `eru-0209`/`eru-1027` and was dual-screened and excluded
   (X7 / S-c-fail) — and must not be transcribed as a recall gap. The
   diagnostic's absence test (DOI or exact normalised title) is looser than its
   "177 absent" headline implies, so the inherited gap is *named but not
   exhaustively bounded* (A12, L-5, VG-4).
8. **The agenda's `eru-1289` sentence names the wrong quantity and drops half the
   cost (findings REV-3-3, QUANT-3-3).** The agenda reads "buys that back at a
   **delay cost of 7.56 → 12.20 months**". DP 2331 Table 2 (p.21) reports these
   as the **mean bias in the estimated bubble origination date**, in months, and
   they are paid **together with** a fall in the successful-detection rate from
   **0.84 to 0.75** — a cost the agenda's sentence omits entirely. Restate as
   "mean origination-date bias 7.56 → 12.20 months **at successful-detection
   rate 0.84 → 0.75**", and carry the **working-paper tier** with it
   (`eru-1289` = Cowles DP 2331; the 2025 CUP chapter its DOI resolves to was
   never obtained — L-10, VG-6). This is a consumer-side edit; it is not made
   here.
9. **The agenda's locator-count sentence is wrong (finding LITERATURE-3-3).**
   The agenda reads "retrieved PDFs corrected **14** locators in the review".
   The correct figure is **19** (L-18's recount box); four further §9 locator
   corrections are recorded separately in L-20 and are not inside the 19. Also a
   consumer-side edit.
10. **Round-4 result for the agenda: no required edit, one advisory, one
    informational note (L-21, VG-17, 2026-09-03).** The round-4 pass re-read
    every locator and quotation the agenda carries from this review against the
    retrieved full texts. **All of them verify** — PWY eq. (8) p.207;
    log(log(ns))/100 and "around the 4% significance level" p.207; PWY Table 1
    note p.213 with 10,000 reps; *IER* 52:214; PSY Table 1 note p.1050 with
    2,000 reps; *IER* 56:1053; PSY 2015b Theorems 2–3 and 8 with their rate
    conditions; `eru-1289` Table 1 p.20 and Table 2 p.21 with 7.56 → 12.20 at
    0.84 → 0.75; NB-08 Theorem 1 p.609. **None of round 4's six corrections
    touches a value the agenda carries**, so items 6, 8 and 9 above remain the
    agenda's outstanding edits and round 4 adds no new required one. Two
    non-required notes for the lead:
    - *Advisory.* Where the agenda writes "BSADF_{r₂} (PSY 2015a **p.1053**)",
      p.1053 is correct for the quotation it is paired with but loose as a
      locator for the statistic itself: BSADF_{r₂}(r₀) is **defined on p.1051**
      and the crossing-time equations (7)–(8) span pp.1052–1053. Not an error;
      change only if a definition locator is wanted.
    - *Informational.* The agenda's branch-3 admission of the surveillance line
      rests on §7.4's nine-record claim. Two of those nine (`eru-0735`,
      `eru-1117`) could not be retrieved on this pass and their cell contents —
      including the `b = 0.147 / 0.177` constants and the "eq. 5" locator — are
      now recorded as unverified (**VG-17**); and a third (`eru-0889`) is
      **closed-ended**, not open-ended as §7.4's row had said. The nine-record
      count and the branch-3 consequence are unchanged.

## 15. Provenance

| item | value |
|---|---|
| protocol | `docs/methodology/protocol_explosive-regime-review_2026-08-24.md` |
| protocol SHA-256 at registration | `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54` (commit `9deee0c`, verified by re-hashing the file as of that commit) |
| protocol SHA-256 with addendum A1–A3 | `c5a4be8d84241f0ea34dfc0f6e08a0c88ee5d4f81d05a6edd934e5db7fb72721` (commit `8aeebfe`) — **superseded 2026-09-02** |
| protocol SHA-256 with addendum A1–A11 | `0c961d3089414aa3016adaced2aa755e1fdf5d9a4db7c962b25bd3d507876b3b` (A4–A11 appended by this document, §12.5) — **superseded 2026-09-02 by the round-2 append** |
| protocol SHA-256 with addendum A1–A13 | `92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2` (A12 and A13 appended by the round-2 remediation) — **superseded 2026-09-02 by the round-3 append** |
| protocol SHA-256 with addendum A1–A16 | `e0df3297c5971735a6f4b610e988087f086e576f4ccb131d2430c8bc353a9184` over 96,223 bytes (**A16** appended 2026-09-04 by the round-5 remediation, finding REV-2-4 — it strikes A15 §(c)'s *"passes on 9 tests"* by quotation and re-attests the mechanical ground against the delivered 10-test module; no appraisal cell, no D judgment and no count changes), superseding the A1–A15 value `eed7db745ff7fe241f85246c37f8f244890fb23712bf7c712093f3a40f9df9e0` over 91,329 bytes (**A15**, round-4, findings QUANT-1-6 / REV-1-6) and the A1–A14 value `9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa` (**A14**, round-3, §12.5). **A16 does not state its own post-append digest**, because a whole-file digest cannot be written inside the file it digests; this row and the front matter are the carriers it names. **Frozen-prefix check, re-run after both appends:** SHA-256 of the first **51,478** bytes of the current protocol file — its byte length at commit `9deee0c` — is `33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`, the registration digest, so no byte above the append-only addendum changed. The protocol file contains **no CRLF**, so this digest is platform-independent |
| registration precedes execution | commit `9deee0c` predates every `date_executed` in the search logs (all 2026-08-24) |
| search logs | `docs/literature/search_logs/explosive-regime/` — 42 executed query logs, dedup ledger, KI recall check, screening prompt, six verdict/extraction JSONL files, stage crosstables, κ computation, NB adjudications |
| candidate store | `docs/literature/references_explosive-regime-dating.json` — 1,996 CSL-JSON entries |
| included-corpus store | `docs/literature/references_explosive-regime.json` — 72 CSL-JSON entries |
| included-corpus store SHA-256 | `13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521` (after the round-1 remediation: `8ed6f9caffd22107d8e6f67458e0d6f75d7e6ae6f95b204aa57a110b5cf74124`; as first delivered: `1abbb9d8b253ff2d10c5f021205101ab4bd610812ffd75d8f6bdcde024bbb7dc`). Both 2026-09-02 remediations added **notes only** — no `DOI`, `title`, `author`, `issued` or `custom` field was altered in either pass (§5.2) |
| backward-chase log | `docs/literature/search_logs/explosive-regime/se-bc-01.json` — the `er-bc-*` arm, executed post-freeze under amendment A11 (§2.2); carries an appended `corrections_2026-09-02` block recording the `er-bc-2` withdrawal (A12(b), LITERATURE-2-1). The as-executed fields are not edited |
| identifier / metadata recheck log | `docs/literature/search_logs/explosive-regime/se-crossref-recheck-01.json`, SHA-256 `9457d3de7e3e3e60cc2b5832785b0b8b6da462153a627ddc69e29f72cd77ac9d` — 62 Crossref works with a per-record message digest, 63 Handle-System resolutions, 2 arXiv resolutions, and the three year-divergence flags of L-13(e). Written 2026-09-02 because round 1 asserted these checks without retaining their responses (REPRODUCIBILITY-2-4) |
| source-text re-fetch log | `docs/literature/search_logs/explosive-regime/se-fetch-recheck-01.json`, SHA-256 `f93061d1871baab9f6e4af534227fef0c6158684417c987747132895192b43a9` — per-host, per-scheme, per-attempt record of the §9.5 retrievals, including the refused HTTPS attempts that round 1 mis-recorded as an access barrier (LITERATURE-2-2, QUANT-2-4) |
| load-bearing locator verification log | `docs/literature/search_logs/explosive-regime/se-verify-loadbearing-01.json`, SHA-256 **`fb532ba9c820ee569859359dc48fbb3b25aa0857697c08fb9ca8713a59f838d8`** over the 88,377 bytes on disk (round 5, 2026-09-04), **superseding `dfd4f6a12414bb0f93c34deb15d4fa89a128ee3b3517781f3c275796a6324c81`** (83,706 bytes, round 4, 2026-09-03). **The 2026-09-04 change, finding QUANT-1-5's own denominator corrected under finding QUANT-2-2:** the `scan_scope` field pinned the candidate denominator to git HEAD `01ecfe7822ccca794272c35956ac8f8289d0c20b`, where the two declared regexes return **91 occurrences / 42 distinct strings**, not the published 107/54 — because that HEAD predates the same pass's six corrections to §7. Both states are now published side by side: the pre-correction pool the pass actually drew from (**91 / 42**, §7 = lines 1467–2038 at `01ecfe7`) and the post-correction measurement (**107 / 54**, §7 = lines 1485–2058 in the delivered file, §7 bytes pinned in the log at SHA-256 `eacc69757d3cc5e96449b4f2442ffbcdb343b7d7be13b9003d017796206c4b15`). **17 candidate occurrences were added to §7 by this pass's own corrections and 1 was removed** — 91 + 17 − 1 = 107 — so the coverage figure is restated against the 91 and is labelled an upper bound rather than a ratio. **No item, verdict, retrieval record or pre-existing count changed.** **Prior state of this row, retained verbatim so the digest chain stays checkable; every "this value" below refers to `dfd4f6a1…`, not to the current digest:** the 50-item load-bearing set, its per-item verdict, the retrieval route and content digest per text, and the per-host / per-scheme attempt record for the six records that could not be retrieved (L-21, VG-17). **This value supersedes `d76a4c60b0c86d9accdb62cf5861d0a477d33e3bd1566bde4ed85f7c76b25495` (79,443 bytes), which is the state the 2026-09-03 audit round read and which the audit trail pins.** The change is **purely additive** and was made on 2026-09-03 under finding **QUANT-1-5**: three keys were added and nothing else — `scope.inclusion_rule_priority_is_SELF_ATTESTED` (the pre-fixing claim carries no external timestamp and, as recorded, is unfalsifiable), `counts.sec7_candidate_denominator` (the §7 candidate pool the 50-item set was drawn from: 77 locator occurrences over 26 distinct strings plus 30 quoted-span occurrences over 28 distinct strings = **107 occurrences**, against which **45** of the 50 items carry a §7 site and 5 carry an agenda site), and a supersession note. **No verdict, item, retrieval record or pre-existing count changed** — deleting the three added keys and re-serialising reproduces `d76a4c60…` byte-exactly, which is the check that establishes it |
| **round-3 verification log** | `docs/literature/search_logs/explosive-regime/se-verify-r3-01.json`, SHA-256 `a92fae17c041674094c0cfdb7753b18ef54da6fabb5c8ffb4cb68adc945a44bf` — the third re-fetch of all seven §9.5 texts with per-text digest and a match flag against the §9.5 column; the DP 2331 Table 1 / Table 2 transcription behind L-19; the PSY 2015a Table 2 transcription behind the §7.1 lag-overspecification row; the NB re-read behind L-20; and the Crossref / OpenAlex / Semantic Scholar / candidate-store abstract lookup behind the §5.4 withdrawal |
| **digest convention for `.json` evidence logs** | Every SHA-256 above is taken over **LF-normalised bytes**, which `.gitattributes` (`*.json text eol=lf`) makes the checkout form on every platform. Round 2's published digests were over CRLF working-tree bytes and were unreproducible from the committed repository; superseded values are kept in §12.3. `se-extraction-recheck.jsonl` carried **no** published digest at the time A14(d) was written, because `*.jsonl` then got only `text=auto` and `core.autocrlf` is `true` here, so its checkout form was platform-dependent (§12.3). **LEAD-SESSION UPDATE, 2026-09-02, after A14 was written:** the repository gap is closed — `.gitattributes` now carries `*.jsonl text eol=lf` (and `*.csl text eol=lf`), and the six working-tree `.jsonl` files under `docs/` were normalised to LF, which is their checkout form under the new rule. `se-extraction-recheck.jsonl` therefore now has a stable published digest: **`51cdeed131dc651928c16037c62789dcad11825e883b3f95b786d4e30cb7e600`** (LF bytes). This update was made by the lead session as repository bookkeeping and was **not** verified by any audit round — round 3 was the cap. Amendment **A14(d)**; finding REPRODUCIBILITY-3-2 |
| ReproLog for the **round-3** remediation — the pass whose content this document now is (**untracked locator** — `logs/` is gitignored and does not resolve in a fresh clone) | path `logs/reproducibility/repro_log_ee8bebfaafec4ce1962ee57746c90a36.json`; SHA-256 **`9e21ad6ad0e4066b193dd8e1d775293283362faa26cfd4cc28b95be7abcc0be6`**, taken over the bytes on disk (the file contains no CRLF, so the digest is platform-independent). Complete on all 13 fields: `config_resolved_sha256` = `9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa` (the A1–A14 protocol), `dataset_checksums` over nine inputs including `references_explosive-regime.json` `13c76d8f…`, `se-bc-01.json` `75f36b54…`, `se-crossref-recheck-01.json` `9457d3de…`, `se-fetch-recheck-01.json` `f93061d1…` and the new `se-verify-r3-01.json` `a92fae17…`; `pip_freeze_sha256` = `379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40` over 172 packages; `git_head` = `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`; `env_id` = `d2a0b28183f1d74260cd56bcd2881febf9e97d6d2e9dc58d07200db61c478597` (`uv.lock`, **untracked** — VG-14); `model_hash` **null** (VG-11); `rng_seed` 0; `phase` `deliver`; host Windows 10 / Python 3.11.9 / AMD64. **Two limits stated rather than buried:** the freeze is the *global* interpreter's, not the project venv's (VG-16); and the emit-repro-log helper's preferred `uv pip freeze` exits 0 with empty stdout on this host, which would have written the SHA-256 of the empty string — the exact defect VG-15 charges against the corpus-stage log — so `python -m pip freeze` was captured explicitly instead |
| run sidecar for the **round-3** remediation (**untracked locator** — `artifacts/` is gitignored) | path `artifacts/runs/explosive-regime-dating/ee8bebfaafec4ce1962ee57746c90a36/sidecar.json`; SHA-256 **`e3e970a19a281ef7de6c7b88bd6319715fc43dcd3c23ed1d4e3b51b6081c5da7`**, taken over the bytes on disk |
| ReproLog + sidecar for the **round-1** remediation — **superseded, retained so the round-1 state stays checkable** | path `logs/reproducibility/repro_log_a0f236b34b25417cb697df683198b3ef.json`, SHA-256 `20acd0bc95084d4f096e5c2f22922ecf1cb3594e2bd7547cefa2c10c6fe51df7`; sidecar `artifacts/runs/explosive-regime-dating/a0f236b34b25417cb697df683198b3ef/sidecar.json`, SHA-256 `d2835f07146e0d4ff1de55891d894ac347e587b271d9301b06c363b9b7004ff9`. It is complete on 13 fields but **pins pre-round-2 input states** (`references_explosive-regime.json` at `8ed6f9ca…`, `se-bc-01.json` at `3ea52681…`, `config_resolved_sha256` = the A1–A11 digest) |
| ReproLog for the **round-2** remediation | **NONE WAS EMITTED.** Round 2 wrote no ReproLog and no sidecar, and this section cited the round-1 pair for a document whose content was by then round-2's — so between the round-2 edits and this append there was no provenance record matching the artifact. Disclosed rather than backfilled: a ReproLog emitted now could not honestly carry a round-2 timestamp or a round-2 input state. The round-3 log above is the first record that matches its artifact since round 1. *(Finding REPRODUCIBILITY-3-1.)* |
| git HEAD | `27d74738aa35ec1cdf1ec6915b50532e3620ea6f` — the **pre-delivery** HEAD, i.e. the commit this document was written against. The commit that delivers this document is its child and is not yet known here; the clone-durable carrier of the ReproLog path and digest is that commit's `Repro-Log-Path:` / `Repro-Log-SHA256:` trailers, per the repository reproducibility contract |
| earlier-stage ReproLog | commit `8aeebfe` (search, screening, extraction) cites `logs/reproducibility/repro_log_f5419aa650e249378ff40828424696bb.json`, SHA-256 `7716edd8e6cdc0e81d84f624eda853f7474d096fe2c4c3598ffcd8d4e37bac7f`. It records **no model field**, which is why the automation-tool identity cannot be resolved from the logs (L-15, VG-11). **It is also vacuous as an environment and data record, and this row previously implied otherwise:** its `pip_freeze_sha256` is `e3b0c442…b855`, the SHA-256 of the empty string, and the env file it points at is 0 bytes; its `config_resolved_sha256` is `null` and its `dataset_checksums` is `{}`. So the stage that produced the frozen corpus has **no** environment record and **no** contemporaneous checksum of the protocol, the candidate store or any verdict file; the corpus's input state is fixed only retrospectively, by the 2026-09-02 sidecar digests and by commit `8aeebfe`'s tree. Repository-level gap **VG-15** (REPRODUCIBILITY-2-2) |
| environment specification | ~~**None that resolves in a fresh clone.** `pyproject.toml` pins no package version and `uv.lock` is untracked; the pip-freeze archives live under gitignored `logs/reproducibility/env/`.~~ **SUPERSEDED 2026-09-03 (REPRODUCIBILITY-1-2):** `uv.lock` **is tracked**, committed at `2ba291f9922547e1848d7d505cedafb2979e2433`, SHA-256 `eca78f9d52a8534f2890c99bd2f16b3aadc1455b0eb7b93c6d2e621240efd885` over its LF checkout form; it is the pinning mechanism per [ADR-0005](../decisions/ADR-0005-lockfile-is-the-pinning-mechanism.md), and `pyproject.toml` deliberately keeps ranges. Reproduce with `uv sync`, not `uv pip install -e .`. Python is pinned (`>=3.11,<3.13`; host 3.11.9). **The lockfile does not describe the environment that produced this review** — that environment is unrecoverable (VG-15) — so **VG-14 remains open for these runs** and is closed only prospectively; see the VG-14 row in §12.3 for the three residuals ADR-0005 names |
| reproduce target | ~~**None.** No tracked file under `tests/` or `src/` re-derives any number reported here.~~ **SUPERSEDED 2026-09-03 (REPRODUCIBILITY-1-2), for one number only:** `tests/test_erob_recount.py` is tracked at `01ecfe7822ccca794272c35956ac8f8289d0c20b` (~~707 lines, 9 tests as committed at that hash; green under `uv run pytest tests/test_erob_recount.py`~~ — **superseded 2026-09-04, finding REV-2-4: the delivered module is 1,149 lines, 56,401 bytes, 10 tests, SHA-256 `90981cd076377c56b438a49e11264a3dd67b7fb35f0dc976e055b96480d96994`, re-attested green at 10 passed on 2026-09-04 and not yet committed; the struck triple is the round-1 state and is retained so it stays checkable**) and re-derives the §6 ER-RoB domain-concern column from `se-extraction-primary.jsonl` and `se-extraction-recheck.jsonl`, reproducing amendment A8's 31/13 exactly. **Every other count in this review still has no committed entrypoint** and was produced by throwaway code — the 50 `partial` cells, the 561 / 65 / 53 denominators, 90 of 357 divergences, I3 = 7, 62 DOI-bearing records, the O6 and lineage distributions. Repository-level gap **VG-16** (REPRODUCIBILITY-2-5) is therefore **closed for the ER-RoB domain column and open for everything else** |
| model identity per stage | declared in the frontmatter `ai_assistance` block and in the AI-assistance statement below, against the `AI-Assistance` trailer on each artifact's carrier commit |
| identifier verification | 62/62 DOIs `responseCode` 1 against the DOI Handle System; 2 arXiv IDs resolved against the arXiv API; 1 Handle `responseCode` 1 — all re-run and **archived** 2026-09-02 in `se-crossref-recheck-01.json` (round 1 asserted these without retaining the responses; REPRODUCIBILITY-2-4) |
| computations performed by this review | deduplication re-verification, κ and its 2×2 recomputation, dual-pass divergence counts, flow-identity reconciliation, SHA-256 digests, identifier resolution; and, in the 2026-09-02 remediation: the complete 62/62 Crossref metadata cross-check (L-13), the mechanical Q→D recount over all 72 appraisal rows (§6, §6.1, A7, A8), the I3 identifier recount (§5.1), the post-freeze backward-chase retrieval and diff (A11, `se-bc-01.json`), and content digests for three of the seven §8/§9 primary texts (§9.5); and, in the 2026-09-02 **round-2** remediation: re-fetch and SHA-256 of all **seven** §9.5 primary texts, verbatim re-verification of every §7.6/§8 quotation and every reported number against them, correction of **19** page locators (L-18 — the round-2 change note said 14; recounted round 3, LITERATURE-3-3), a full three-way year-field comparison over all 62 DOI-bearing records (L-13(e)), re-resolution of 63 handles and 2 arXiv IDs, and recomputation of the O6 and lineage distributions over distinct works (§4, §7.6, §10.2); and, in the 2026-09-02 **round-3** remediation: a **third** re-fetch and SHA-256 of all seven §9.5 texts (all seven digests reproduced), a direct re-read of DP 2331's Tables 1 and 2 and of PSY 2015a's Table 2, the first re-read of the three §9 NB texts (14 quotations verified verbatim, 5 locators corrected, 1 result misattribution found), a four-source lookup for `eru-0259`'s journal abstract (Crossref, OpenAlex, Semantic Scholar, candidate store — absent from all four), the L-18 recount, and SHA-256 recomputation of three evidence logs over LF-normalised bytes. **No simulation, no fitting, no critical value** (ADR-0003) |

**Standards and methods cited by this review**

- Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement. *BMJ*. 2021;372:n71. [doi:10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71)
- Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S. *Syst Rev*. 2021;10:39. [doi:10.1186/s13643-020-01542-z](https://doi.org/10.1186/s13643-020-01542-z)
- Moher D, Shamseer L, Clarke M, et al. PRISMA-P 2015. *Syst Rev*. 2015;4:1. [doi:10.1186/2046-4053-4-1](https://doi.org/10.1186/2046-4053-4-1)
- Cohen J. A coefficient of agreement for nominal scales. *Educ Psychol Meas*. 1960;20(1):37–46. [doi:10.1177/001316446002000104](https://doi.org/10.1177/001316446002000104)
- Whiting PF, Rutjes AWS, Westwood ME, et al. QUADAS-2. *Ann Intern Med*. 2011;155(8):529–536. [doi:10.7326/0003-4819-155-8-201110180-00009](https://doi.org/10.7326/0003-4819-155-8-201110180-00009)
- Wolff RF, Moons KGM, Riley RD, et al. PROBAST. *Ann Intern Med*. 2019;170(1):51–58. [doi:10.7326/M18-1376](https://doi.org/10.7326/M18-1376)
- Egger M, Davey Smith G, Schneider M, Minder C. Bias in meta-analysis detected by a simple, graphical test. *BMJ*. 1997;315:629–634. [doi:10.1136/bmj.315.7109.629](https://doi.org/10.1136/bmj.315.7109.629)
- Frisén M. Statistical surveillance: optimality and methods. *Int Stat Rev*. 2003;71(2):403–434. [doi:10.1111/j.1751-5823.2003.tb00205.x](https://doi.org/10.1111/j.1751-5823.2003.tb00205.x)

All eight DOI handles were verified `responseCode` 1 on 2026-09-02.

**Bibliography of included records.** The 72 included records are not repeated as
a reference list here: they are enumerated with full citations in §5, appraised in
§6, cited by record id and DOI throughout §7 and §8, and carried in machine-readable
CSL-JSON in `docs/literature/references_explosive-regime.json` with the SHA-256
above. Records excluded at full text are enumerated in §13.

**AI-assistance statement (ICMJE 2026) — declared per stage, because the
identity is not uniform and the conflict cannot be resolved from the logs.**
This review as first delivered named `claude-opus-5` for every stage. The
repository's `AI-Assistance` commit trailers say `claude-fable-5` for the
commits that carry the protocol and the verdict/extraction artifacts, and the
ReproLog cited by those commits carries no model field, so the two records
cannot be reconciled from evidence. What is durable is the trailer, so the
trailer is what is declared:

| stage | artifacts | carrier commit | declared model |
|---|---|---|---|
| protocol registration | the frozen protocol (its own frontmatter also names Claude Fable 5) | `9deee0c` | `claude-fable-5` |
| search execution, deduplication | 42 query logs, dedup ledger, candidate store | `8aeebfe` | `claude-fable-5` |
| title/abstract screening (two sessions) and blind adjudication | `screen-verdicts-R1/R2/ADJ.jsonl` | `8aeebfe` | `claude-fable-5` |
| full-text screening (two sessions) and blind stage-2 adjudication | `screen2-verdicts-R1/R2/ADJ.jsonl` | `8aeebfe` | `claude-fable-5` |
| primary extraction; §9 NB adjudications | `se-extraction-primary.jsonl`, `se-nb-adjudications.json` | `8aeebfe` | `claude-fable-5` |
| independent numeric re-extraction | `se-extraction-recheck.jsonl` | none — untracked at the time | **unrecorded** |
| flow reconciliation, appraisal resolution under §2.8, synthesis, §8/§9 write-ups, prose | this document | delivered by the current session | `claude-opus-5` |
| round-1 audit remediation: amendments A4–A11, the 62/62 Crossref cross-check, the Q→D recount, the post-freeze backward-chase arm, §9.5 digests | this document, the store, `se-bc-01.json`, the protocol addendum | delivered by the current session | `claude-opus-5` (Claude Code / Claude Agent SDK) |
| round-2 audit remediation: amendments A12–A13, the seven-text re-fetch and quotation/locator re-verification, the three-way year-field comparison over 62 records, the distinct-work recount, the O6 and `partial` denominator corrections | this document, the protocol addendum, `se-bc-01.json` (corrections block), `se-crossref-recheck-01.json`, `se-fetch-recheck-01.json` | delivered by the current session | `claude-opus-5` (Claude Code / Claude Agent SDK) |

All screening and adjudication sessions were separately spawned and
context-independent within their stage. Under PRISMA 2020 item 8 the model is
declared as the automation tool and the sole effective screener class; no human
screener or extractor exists at any stage.

**What κ then measures, stated no more strongly than the record supports.**
κ = 0.433 compares two context-independent sessions that sit in the same stage
under the same trailer, so what it measures is **between-session variance of the
screening stage under an UNRECORDED decoding configuration**. The earlier form of
this sentence said κ "measures decoding-and-context variance of the screening
model". That reading is not falsifiable from this record and is withdrawn as
stated: **no temperature, top-p, max-tokens, thinking-budget or session seed is
recorded anywhere** — not in `er-screening-prompt.txt`, not in any verdict
JSONL, not in either ReproLog — so the screening stage cannot be re-run to a
comparable κ, and the split of the observed variance between decoding
stochasticity, context ordering and prompt-position effects is unobservable.
The missing sampling parameters are recorded as a named, unclosable component of
**VG-11**. *(Finding REPRODUCIBILITY-2-3.)* κ does not characterise the
synthesis model, and it does not characterise the extraction passes — whose
model identities are, for the recheck pass, unrecorded, so the 90/357 inter-pass
divergence of §2.8 may be partly a between-model quantity rather than the
within-model quantity it was described as. See §12.1 L-15 and §12.3 VG-11.

**The remediation-stage ReproLog reproduces upstream's own defect.**
`repro_log_a0f236b34b25417cb697df683198b3ef.json` — the 2026-09-02 run's own
ReproLog — carries `"model_hash": null` and no model-id field, which is exactly
the omission L-15/VG-11 charges against the 2026-08 stages; the only artifact
carrying `ai_assistance = claude-opus-5` for that run is the sidecar, which is
gitignored and therefore does not resolve in a fresh clone. The clone-durable
carrier for this stage is the `AI-Assistance` trailer on the commit that
delivers this document. Recorded rather than repaired: this document does not
rewrite an emitted ReproLog. *(Finding REPRODUCIBILITY-2-3.)*

The model is not an author. The human author approves this document by
committing it.

## 16. Change note — round-1 audit remediation, 2026-09-02

A seven-branch specialist audit (critical-reviewer, scope-auditor,
quant-auditor, literature-check) with an adversarial refute gate raised 27 major
findings against this review; 3 were refuted and dropped, 24 survived. Twenty of
the twenty-four are remediated here; four (REV-1-7, QUANT-1-6, LITERATURE-1-6,
SCOPE-1-6) fall on
[research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md)
and are not this document's to make.

**Direction of every change: more disclosure, not less.** No disclosure was
weakened to close a finding. The frozen 72-record corpus was not re-screened and
its composition is unchanged; the frozen protocol text above its append-only
addendum is unchanged, verified by hashing the file's byte prefix at the
registration length (§15).

| finding | change, and where |
|---|---|
| **REV-1-1**, **SCOPE-1-2** | A4, A5 and A6 appended to the protocol's append-only addendum rather than deferred to a consumer session; §12.5 rewritten from "amendments this document requests" to "amendments this document appends"; frontmatter `amendments_this_document_requests` replaced by `amendments_appended_by_this_document: [A4…A11]`; `protocol_sha256_with_addendum` recomputed to the A1–A11 digest `0c961d30…` with the A1–A3 digest retained as superseded; §15 carries both plus the frozen-prefix check |
| **QUANT-1-1** | A7 appended, recording the four-level response scale (`partial` in 50 answered Q-cells) against the frozen three-level instrument and fixing the `CONVENTION` that `partial` counts as not-`yes`; §2.7's "no domain or question was added, dropped or reworded" now excepts the response scale explicitly; §6 header restates it. **Round 2:** A7's denominator 585 was wrong and is corrected to **561** by A12 (QUANT-2-1, REV-2-12) |
| **REV-1-3**, **QUANT-1-2** | A8 appended, recording the departure from §6's Q→D rule. §6 gains a `D-rule` column giving the mechanically rule-derived judgment per domain, a `§` marker on all 31 cells recorded `low` where the rule raises concern, and a `¶` marker on all 13 that run the other way; the legend gives the per-domain counts and states the direction (the 31 run *toward lower concern*, against §2.8's posture); §6.1 restates the corpus profile on the rule-derived column with the recorded column as sensitivity; the abstract's D-domain claims follow |
| **REV-1-4** | Assessable denominators (65 for Q1–Q7/D1–D6, 53 for Q8/Q9/D7/D8) stated and used in §6.1, §7.2, §7.3, §7.4 and the abstract, with the excluded classes named at each site; §6.1 reading 4's "out of 56 assessable" corrected to 53 |
| **REV-1-5** | The abstract's Design sentence now states the backward-chase arm as a non-execution; the Limitations paragraph adds the unexecuted arm (and its post-freeze diagnostic run) and the I3/X7 eligibility violations |
| **REV-1-2** | I3 failure count corrected from five to seven at every site: §5.1 (rewritten), §5.3, §12.1 L-6, §12.3 VG-8, §12.4 item 5, amendment A10(a). The rule that a twin does not inherit its carrier's DOI for I3 purposes is stated in §5.1, §5.3, L-6 and A10(a). `eru-0154` and `eru-0904` gained `I3 GAP` notes plus their best locators in the store |
| **SCOPE-1-5** | The I3 and X7 deviations are now numbered amendments A10(a) and A10(b), not only review limitations; §6's header states 72 records / 69 distinct works |
| **SCOPE-1-1** | A9 appended. The §9.1 force-screening failure is disclosed in §3.1 (with the three records shown outside the flow), in §3.2 (the exact-reconciliation claim now states its exception), and in §9.0 with the grep evidence; new limitation L-17 and verification gap VG-9 |
| **SCOPE-1-4** | **The arm was executed**, post-freeze, and logged at [se-bc-01.json](search_logs/explosive-regime/se-bc-01.json) under amendment A11: 22 of 27 I2b carriers covered, reference lists from publisher-deposited metadata, 392 unique referenced DOIs, 177 outside the universe, 2 candidate additions (`er-bc-1`, `er-bc-2`) and 6 named near-misses. Neither candidate is admitted; the corpus stays at 72. §2.2 rewritten; L-5, VG-4 and new VG-12 restated. **Round 2:** the yield was **1**, not 2 — `er-bc-2` was already in the universe as `eru-0209`/`eru-1027`, dual-screened and excluded (A12(b), LITERATURE-2-1) |
| **REV-1-6** | NB-13's verdict retained as `episode-statistic-null` but explicitly **provisional on the working-paper twin**, with the reason for not using `indeterminate-from-full-text` argued in §9.3; §9.4 rewritten from "strengthens" to "two adjudicated on full text; the third provisional"; §14 item 3 carries the qualification |
| **REV-1-13** | The O4 synthesis claim in §7.4 rewritten corpus-scoped on the O5 template, with the L-4/L-5 recall bound attached at the point of the claim; §14 item 2 follows |
| **SCOPE-1-3** | §6's header carries a blockquote stating that the appraisal is convention-resolved and may not be cited as an adjudicated appraisal; repeated at every downstream use in §7.4 and in L-2 and §12.4 item 11 |
| **QUANT-1-3** | Model identity reconciled per stage against the commit trailers in the frontmatter `ai_assistance` block, in new limitation L-15 (with the stage table) and in the §15 AI-assistance statement; the conflict is stated as unresolvable from the logs, not papered over; what κ then measures is restated; new verification gap VG-11 |
| **QUANT-1-4** | §15 gains ReproLog path and SHA-256, sidecar path and SHA-256, and the pre-delivery git HEAD, all labelled untracked locators per the repository reproducibility contract; §12.4 item 27 re-worded to state tracking status as of the delivering commit, naming what was tracked at `8aeebfe`, what this commit tracks, and what is gitignored |
| **QUANT-1-5** | §7.1's "always upward" replaced with the drift-break exception (`eru-0348`, size → 1 or 0 with the break sign); TC-1's rationale now requires a two-sided measurement |
| **QUANT-1-7** | New §9.5 records the retrieval route per primary text and SHA-256 content digests for the three that could be re-fetched on 2026-09-02; the four that could not are named, and §8's and §9's verdicts on them are marked as resting on single-session transcription. New limitation L-16 and verification gap VG-10. **Round 2:** the "could not be re-fetched" claim was false (HTTPS-only attempt against an HTTP-only host); all four were retrieved, digested and re-read, L-16 and VG-10 narrowed, per-attempt log `se-fetch-recheck-01.json` archived (LITERATURE-2-2, QUANT-2-4) |
| **LITERATURE-1-2** | `eru-1289` re-tiered **working-paper**, with the tier travelling with the FWER claim in §7.4, the abstract, §14 and the store note; the DOI's 2025 chapter and the extracted 2022 DP are no longer silently mixed in §4 or §5; added to L-10 as a fourth version-caveat case and to VG-6 |
| **LITERATURE-1-4** | The **complete** 62/62 Crossref cross-check was run. L-13 rewritten to report 13 volume/issue/page discrepancies, 3 pagination updates, 1 version misattribution, 1 record Crossref cannot verify, and a stated year-of-record `CONVENTION` covering 7 further divergences. Every discrepancy is also noted on its store entry |

**Artifacts changed by this pass.** This review; the protocol's addendum
(append-only, A4–A11); `docs/literature/references_explosive-regime.json` (notes
only — no `DOI`, `title`, `author`, `issued` or `custom` field altered); and one
new search log, `se-bc-01.json`. No verdict file, no extraction file and no
count in §3 was touched.

**Not remediated here.** REV-1-7, QUANT-1-6, LITERATURE-1-6 and SCOPE-1-6 all
land on the consumer agenda and are the lead session's to make. §14 carries the
inputs they need.

## 17. Change note — round-2 audit remediation, 2026-09-02

A five-branch specialist audit (critical-reviewer, scope-auditor, quant-auditor,
literature-check, reproducibility-verifier) with an adversarial refute gate ran
against the round-1 remediation and raised **30 major findings. The refute gate
dropped none of them.** Twenty-four fall on this review and are remediated here;
six (REV-2-7, SCOPE-2-1, SCOPE-2-2, QUANT-2-5, LITERATURE-2-7, LITERATURE-2-8)
fall on the consumer agenda and are not this document's to make.

**Three of the findings say that claims made by the round-1 remediation itself
were false.** They are listed first, because a false claim inside a fix is worse
than the defect it was fixing.

| finding | what was claimed in round 1 | what is true | where it is now |
|---|---|---|---|
| **LITERATURE-2-1** | The A11 backward-chase diagnostic named `er-bc-2` (Banerjee, Chevillon & Kratz 2013) as a second candidate addition "absent from the 1,996-record universe", eligibility "indeterminate at retrievable depth" | **The work is in the universe**, twice: `eru-0209` (2013 WP, no DOI) and `eru-1027` (*Econometrics Journal* 2020, doi:10.1093/ectj/utaa004). Both PROMOTE/PROMOTE at stage 1; both excluded at stage 2 — X7 and S-c-fail respectively, R2 X6, terminal under A3. The dedup key failed on a one-word title variant ("in a" / "with a") against a record carrying no DOI | §2.2 (candidate list and dedup-failure note), abstract Limitations, L-5, VG-4, VG-12, §14 item 7, protocol amendment **A12(b)–(c)**, and a `corrections_2026-09-02` block in `se-bc-01.json`. Yield restated as **1** candidate addition; the "177 absent" figure restated as an upper bound |
| **LITERATURE-2-2 / QUANT-2-4** | §9.5 recorded all three Phillips reprints and Cowles DP 2331 as un-refetchable ("host `korora.econ.yale.edu` did not accept a connection"; "`cowles.yale.edu` … returned HTML"), with digest `none`; L-16/VG-10 concluded the §8.3 verdict and §7.4 FWER triple "cannot presently be re-opened" | **All four were re-fetched.** `korora.econ.yale.edu` refuses TCP on **port 443** and serves all three reprints over **plain HTTP on port 80**; DP 2331 is served over HTTPS at its direct file path. Round 1 attempted HTTPS only and recorded a scheme failure as an access barrier | §9.5 (per-host/per-scheme attempt table, four digests), L-16 narrowed, VG-10 downgraded major → minor, §8 preamble, §14 item 2, and the archived per-attempt log [se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json) |
| **QUANT-2-3** | §9.5 existed so a successor could "re-open the quoted page" | **Nineteen page locators were wrong** (round 2 published this as "fourteen"; recounted round 3 under LITERATURE-3-3, and its own L-18 table always carried 19 corrected rows plus one that supplied absent locators), almost all by one page. The quoted strings and the headline numbers verify verbatim against the retrieved texts; only the page attributions failed. The re-read additionally found one paraphrase quotation-marked as verbatim, one mis-summarised number (PSY Table 2's lag-overspecification distortion, given as "0.697/0.401" — two unrelated cells, omitting the maximum 0.787), and one mislabelled row in §7.4's FWER table (a "longer span" that DP 2331 §5.2 fixes at 10 years for all three cells) | New **L-18** with the full old→new table and the three non-locator corrections; applied in round 2 at §7.1, §7.4, §7.5, §7.6, §8.1, §8.2, §8.3 and §9.5 — **and NOT at §7.3, §7.8 or §11 TC-2, which round 2's own assurance implied it had reached; those three are corrected in round 3 under L-19** (REV-3-3, QUANT-3-3); **two locators must also be corrected in the consumer agenda** (§14 item 6) |

**The remaining twenty-one.**

| finding | what changed, and where |
|---|---|
| **REV-2-1 / LITERATURE-2-5** | §2.5's "Honest compliance statement, as executed" still named `claude-opus-5` for screening while every other reconciled site named `claude-fable-5`. Rewritten to declare `claude-fable-5` per the `8aeebfe` trailer, to say plainly that this review's original declaration was the conflicting one, and to point at L-15/VG-11 |
| **REPRODUCIBILITY-2-3** | Model *configuration* was unrecorded while §15 leaned on it to call κ a decoding variance. Every κ site (frontmatter, abstract, §2.5, §3.3, L-1, L-15, §15) now says **between-session variance under an unrecorded decoding configuration**; the missing sampling parameters are a named unclosable component of VG-11; the remediation ReproLog's own `model_hash: null` is disclosed |
| **REV-2-2 / SCOPE-2-4 / QUANT-2-2** | O6 had two denominators, one of which made a false statement ("fewer than one in three" at 22/65 = 33.8%). **One denominator is fixed: 63 distinct works with an extracted causality status** (69 − 4 NE − 2 NS), with the excluded classes named, used in the abstract and in §7.6; the figure is 22/63 = 35%. The full six-class partition is retained over 72 records and 69 distinct works in §7.6's table |
| **REV-2-3** | §5.3, L-7 and A10(b) assured the reader that the three twins cause no double-counting; true of §7's evidence tables, false of the §4, §7.6 and §10.2 distributions. Assurance narrowed at all three sites; distinct-work columns added to §4, §7.6 and §10.2 (O6 22/21/17/3/2/4; lineage 19/16/34; tier 53/10/4/2; I2 41/23/2/2/1; E14 "not extracted" 16); registered as amendment **A13(a)** |
| **REV-2-4 / LITERATURE-2-6** | NB-13's "PROVISIONAL ON THE WORKING-PAPER TWIN" is not in §9.1's frozen vocabulary, and the justification attributed to the protocol a definition of `indeterminate-from-full-text` that the protocol does not make — §9.1 lists that token, and `mixed`, with **no gloss at all**. Both are now labelled CONVENTIONs of §9.3 and registered as amendment **A13(c)**, cross-referenced from §9.4, §14 item 3 and VG-3 |
| **REV-2-5** | §7's reading rule said a record count is a fact about "the literature's coverage" — the exact generalisation the corpus cannot support. Restated as "a fact about *this corpus's* coverage, never about the literature and never about a detector", with the census-not-sample point made explicitly and no binomial interval claimed; propagated to the §7.4 quotation site |
| **REV-2-6** | §7.7's outcome was generalised to "the state of the evidence" and called a finding although protocol §7 15c pre-registered it. Rewritten corpus-scoped on the O5/§7.4 template, relabelled **pre-registered expectation confirmed**, with the A11 bound attached at the point of claim and `er-bc-1` named as a record whose admission could supply the non-overlapping second arm on Evans-collapse power. The same one-line bound added to §7.2's synthesis claim; the symmetric concession added to L-5 |
| **REV-2-12 / QUANT-2-1** | The `partial`-cell denominator 585 (65 × 9) contradicted the review's own assessable-denominator rule. Corrected to **561** (65 × 7 + 53 × 2) at §2.7, §6 and §12.4 item 11, with the arithmetic and the exclusion classes shown; 50/561 = 8.9%. A7 is inside the append-only addendum and is corrected by **A12(a)**, not edited |
| **SCOPE-2-3** | The X7 drift declared in round 1 enumerated three twin pairs; §5.4 documents a fourth (`eru-0198` / `eru-0259`) whose extraction substitution the review already described. Disclosed in full at §5.4 and §5.3, registered as **A13(b)** and verification gap **VG-13**: the pair is a *probable, unadjudicated* twin — the project's own extraction logs flagged it for adjudication and the adjudication never ran — so distinct works are **69 if two works, 68 if one**. Also recorded: the two §6 rows are two passes over one document, so their Q4/Q7 divergence is an inter-pass divergence that the 90-of-357 count does not contain |
| **QUANT-2-6 / LITERATURE-2-4** | L-13 claimed a field-by-field check "including year" and then closed the year dimension on seven records. **The year field has now been checked across all 62**, in three directions. L-13's completeness claim is narrowed to container title, volume, issue and page range, and L-13(e) is replaced by a full report: **19** online/print year divergences (not 7); the declared CONVENTION contradicted by the review's own labels in **12** of those 19; **22** label-versus-store divergences; `eru-1117` corrected from "one later" to two (online 2021-05-05, print 2023-01-19); `eru-1155`'s year added to L-13(a), its label 2018 matching no source |
| **REPRODUCIBILITY-2-4** | The 62/62 Crossref cross-check, the DOI Handle re-resolutions and the arXiv/Handle checks had no archived evidence. All re-run and archived with a per-record Crossref message digest at [se-crossref-recheck-01.json](search_logs/explosive-regime/se-crossref-recheck-01.json); the §9.5 retrievals archived at [se-fetch-recheck-01.json](search_logs/explosive-regime/se-fetch-recheck-01.json). Both cited from L-13, §12.3 and §15 |
| **REPRODUCIBILITY-2-1 / 2-2 / 2-5** | **Repository-level, not review-level, and not repaired here.** Recorded as named verification gaps with their scope stated: **VG-14** unpinned dependencies with an untracked `uv.lock`; **VG-15** the corpus-producing ReproLog's empty-string pip-freeze digest, null config digest and empty dataset checksums; **VG-16** no committed entrypoint that re-derives any reported number. §15 gains an environment-specification row and a reproduce-target row saying "none", and the earlier-stage ReproLog row now names the environment and input-state defects rather than only the missing model field |

**Direction of every change: more disclosure, not less.** Three claims were
withdrawn — `er-bc-2` as a recall gap, "cannot presently be re-opened", and
"fewer than one in three" — and each was withdrawn because it was **false**, not
because it was inconvenient; each withdrawal is accompanied by the evidence that
defeated it and, where the withdrawal removes a gap, by the new gap it exposes
(A12(c)'s bound on the arm's absence test; VG-10's residual version-identity
problem; VG-13's fourth twin).

> **This paragraph's closing assurance was false and is withdrawn (round 3,
> findings REV-3-3, QUANT-3-3, REV-3-4, LITERATURE-3-3).** It read: "No number
> was changed at one site only: the denominators 561 and 63, the candidate count
> 1, and every corrected page locator were grepped across the document." Those
> four items were indeed propagated. **Three other round-2 corrections were
> not.** (i) The `eru-1289` quantity relabel (origination *delay* → mean bias in
> the estimated origination date, with its 0.84 → 0.75 successful-detection-rate
> cost) reached §7.4, §9.5, §14 and L-18 but **not** §7.3, §7.8 or §11 TC-2 —
> and §7.3 additionally attributed the figures to Table 1 when they are in
> Table 2. (ii) The `eru-1289` working-paper tier reached the abstract, §7.4,
> §7.8, §11 and §14 but **not** §7.3, which affirmatively asserted
> "peer-reviewed throughout". (iii) L-18's own headline count, "fourteen", was
> wrong at all seven of its sites and contradicted L-18's own table. All are
> corrected in round 3 (L-19, L-20, and the recount box in L-18). The lesson the
> round-2 text drew — that a grep sweep discharges the obligation — holds only
> for numerals; a *relabelled quantity* and a *tier* are not greppable as
> numbers, and both slipped through.

**What did not change.** The frozen 72-record corpus was not re-screened and its
composition is unchanged. No verdict file, no extraction file and no §3 flow
count was touched. The frozen protocol text above its append-only addendum is
unchanged: the SHA-256 of its first **51,478** bytes — the file's byte length at
registration commit `9deee0c` — is still
`33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`.

**Artifacts changed by this pass.** This review; the protocol addendum
(append-only, **A12** and **A13** appended, digest with addendum now
`92fff3f271adb44404b1bb6933eb1de1bce417024dc2a07afc4cfc02f14155c2`, frozen
prefix unchanged); `se-bc-01.json` (a `corrections_2026-09-02` block appended,
as-executed fields untouched); two new search logs,
`se-crossref-recheck-01.json` and `se-fetch-recheck-01.json`; and
`references_explosive-regime.json`, **notes only** on `eru-0198` and `eru-0259`
(new SHA-256 `13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521`,
§5.2). The 1,996-record candidate store was not altered.

**Not remediated here.** REV-2-7, SCOPE-2-1, SCOPE-2-2, QUANT-2-5,
LITERATURE-2-7 and LITERATURE-2-8 land on
[research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md)
and are the lead session's to make. §14 carries the inputs, including the two
page locators (item 6) and the corrected backward-chase gap (item 7) that this
round's findings add to that list.


## 18. Change note — round-3 audit remediation, 2026-09-02

**This was the last audit round. There is no round 4, and nothing written in
this section has been independently checked.** Read §18.4 before relying on
anything here.

A five-branch specialist audit ran against the round-2 remediation and raised
**17 major findings; the refute gate dropped one** (QUANT-3-2, which claimed
L-18 had turned a correct `pp.1090–1091` locator into a wrong `p.1090`). Of the
sixteen retained, **five** (REV-3-1, REV-3-2, SCOPE-3-1, QUANT-3-1,
LITERATURE-3-1) land on the consumer agenda and are the lead session's; **eleven**
land on this document and are remediated below.

### 18.1 Findings that say a round-2 correction was itself wrong

Round 1's corrections contained three false claims; round 2's contain four. The
pattern has not attenuated, and §18.4 says so plainly rather than implying
convergence.

| finding | what round 2 claimed | what is true | where it is now |
|---|---|---|---|
| **REV-3-3 / QUANT-3-3** | Round 2 corrected the `eru-1289` figures to "mean bias in the estimated origination date … at successful-detection rate 0.84 → 0.75, Table 2 p.21" and asserted the correction had been propagated | **Four sites were left on the withdrawn label**: §7.3's two table rows and its prose (which also cited **Table 1**, the FWER table on p.20), §7.8's BSADF row and §11's TC-2. Re-read directly against DP 2331 on this pass: the figures are in **Table 2, p.21**; the quantity is the averaged signed error `(1/M)Σ(t̂ − t)` in months, which Table 2's caption calls a bias and §5.2's text calls an averaged delay; the SDR falls 0.84 → 0.75 | All four corrected; new **L-19** with the verbatim table transcription; §17's propagation assurance withdrawn |
| **REV-3-4** | The round-1 tier correction said `eru-1289`'s working-paper tier "travels with the claim … wherever it is used" and enumerated the sites | §7.3 was **not** in the enumeration, and its tier line asserted "peer-reviewed throughout" — the direct negation of the correction — over four `eru-1289` rows it calls "the single most consumer-relevant number in the corpus" | §7.3's tier line rewritten, tier flags added inline to the four rows, L-10's enumeration extended to §7.3 and §11 TC-2 |
| **LITERATURE-3-3** | "**Fourteen** page locators in §7, §8 and §9 were wrong", repeated at seven sites in this review and once in the agenda | L-18's own table has always carried **nineteen** corrected rows plus one that supplied locators where none had been given. No counting rule reproduces 14. The corrections themselves were all applied; only the count was wrong, in the under-reporting direction | Recount box inside L-18; **nineteen** at all seven review sites; the agenda's copy listed as a consumer-side edit (§14 item 9) |
| **REPRODUCIBILITY-3-2** | `se-crossref-recheck-01.json` `cb9b0c26…` and `se-fetch-recheck-01.json` `30b69960…` were published as the clone-durable carriers of round 2's two headline corrections | Both digests were over **CRLF working-tree bytes** while `.gitattributes` forces `*.json text eol=lf`, so **no consumer of the committed repository could reproduce either** — and they carry the sole archived evidence for the un-refetchability withdrawal and for L-13(e) | Both logs rewritten with LF terminators (line endings only), digests republished as `9457d3de…` and `f93061d1…` at all six citation sites; `se-bc-01.json` normalised and published at `75f36b54…`; CONVENTION registered as **A14(d)** |

### 18.2 The other seven

| finding | what changed, and where |
|---|---|
| **REV-3-5 / QUANT-3-4** | VG-10 was downgraded major → minor on the strength of a Phillips re-read, and a second, unlike residue was then folded into it: the three §9 NB texts were re-fetched but never re-read, so §9.1–§9.3's quotations and locators were unverified transcriptions of the class that had just produced 19 errors. **The residue is discharged rather than re-severitied.** All three texts were fetched a third time (digests byte-identical) and read: 14 quotations verify verbatim; **4 locators were wrong or loose** (3 in NB-02, 1 in NB-13); **1 result was misattributed** — NB-08's law comes from **Theorem 1 (p.609)**, not "Theorem 3.1", which in that paper is a citation to another work. New **L-20**; VG-10 now carries the version-identity residue only; amendment **A14(c)** |
| **REV-3-6** | §7.1 — the section that *is* the O1 synthesis — reported only the k = 0 column of PSY 2015a's Table 2 and filed every size failure under "departures from the stated null", so lag overspecification (a specification choice, not a departure) was invisible and the synthesis read as if the originators' own null-case size were near-nominal. Verified directly against the reprint: under the **same** null DGP (3) with d = η = 1, GSADF size reaches **0.787** at fixed k = 6, T = 100 — nearly sixteen times nominal — and 0.697 under significance-test kmax = 6 with SADF 0.145. A row is added to §7.1's first table, the O1 synthesis claim is qualified, §7.8's GSADF row carries the distortion, and **lag-order selection is now a declared TC-1 input** |
| **QUANT-3-5** | §5.4 asserted "Twin status **was verified** against the published article's indexed abstract" four paragraphs before asserting that same-work identity "cannot be settled at the depth available". The affirmative sentence is **withdrawn as irreproducible**: `eru-0259` has no `abstract` field in the candidate store, and the *CSDA* abstract is not deposited in Crossref, not in OpenAlex (`W2007843530`) and not in Semantic Scholar — all four sources queried on this pass and logged. The primary extraction log calls the pair "PROBABLE"; the review adopts that. Amendment **A14(b)** |
| **LITERATURE-3-2** | The fourth twin pair was refused on a ground the review does not apply elsewhere. **The standard is now stated**: a twin declaration here rests on documentary evidence at extraction — same author line, same subject, documented WP→journal chain, **one text read** — which is exactly how `eru-0622`/`eru-0675` and `eru-0904`/`eru-1526` were declared, both on unread journal texts and the latter on differing titles. `eru-0198`/`eru-0259` **meets that standard**, so the refusal is relabelled **operational, not evidential**: declaring it would re-derive the frozen 65-record assessable denominator and every "of 65" fraction, which remediation may not do. **72 records are 69 distinct works as the arithmetic runs and 68 under the uniform standard**, said that way at the frontmatter, the abstract, §5.3, §5.4 and VG-13. Two false differentiators struck: both members of all four pairs are in the frozen 72, and the store *does* carry twin notes on both records (round 2 added them). Amendment **A14(a)** |
| **REPRODUCIBILITY-3-1** | **Round 2 emitted no ReproLog and no sidecar**, and §15 cited the round-1 pair (`a0f236b3…`) for a document whose content was by then round-2's — so every input those records checksum was a superseded state, and VG-15's description of that log was wrong in consequence. A ReproLog **and** a sidecar are emitted for **this** pass, complete on all 13 fields, and cited in §15 with the round-1 pair retained as superseded and round-2's absence disclosed rather than backfilled. VG-15 corrected |
| **round-3 by-product (REV-3-3)** | Re-reading DP 2331 surfaced two further errors round 2 had not caught: §7.3's FWER-controlled collapse-date SD was **1.72**; Table 2 gives **1.71**. And the FWER-controlled critical values were described as a "multiple-window bootstrap"; DP 2331 §5.1 simulates `max_s PSY_s` from the null model and takes the 95th percentile over a **single** control window T_w = T, and says only that the approach is "in the same spirit as bootstrapping". Both corrected at §7.3 and recorded in L-19 |
| **round-3 by-product (REPRODUCIBILITY-3-2)** | The `emit-repro-log` helper prefers `uv pip freeze`, which on this host exits 0 with **empty** stdout because no project venv is populated. Taking it would have written `pip_freeze_sha256 = e3b0c442…b855`, the SHA-256 of the empty string — the exact defect VG-15 charges against the corpus-stage log. `python -m pip freeze` (172 packages) was captured explicitly instead, and the substitution is recorded in §15 and in the sidecar |

### 18.3 What did not change

The frozen 72-record corpus was not re-screened and its composition is unchanged.
No verdict file, no extraction file, no §3 flow count and no appraisal cell was
touched. **`references_explosive-regime.json` was not edited this round**; its
SHA-256 is still `13c76d8fd56ff86eed3f4b0ed7766ef72946a1b6d995aa7c7604348229ce5521`.
The protocol's frozen text above its append-only addendum is unchanged: the
SHA-256 of its first **51,478** bytes is still
`33c01c522521a9f0f9ee39caa7a71b1fcf51ca50a7b471cc4cc7ee2db7301a54`, re-verified
**after** the A14 append.

**Artifacts changed by this pass.** This review; the protocol addendum
(append-only, **A14** appended, digest with addendum now
`9d400eb557680d393af052bcb48eb52e880b3f9182b081b56c7ceaff3f83ecaa`, frozen
prefix unchanged); one new search log, `se-verify-r3-01.json`
(`a92fae17…`); and three existing logs rewritten with **LF line terminators
only, no field value altered** — `se-crossref-recheck-01.json`,
`se-fetch-recheck-01.json`, `se-bc-01.json`. Neither reference store was altered.
**This review file is itself written with LF terminators from this round on**, so
that a digest taken over its bytes on disk equals the digest of the blob any
clone checks out (`.gitattributes`: `*.md text eol=lf`); it had been CRLF, which
is the same trap REPRODUCIBILITY-3-2 found in the evidence logs. No character of
its content changed in that step.

### 18.4 Residual risk after three rounds — read this before citing anything

No further audit round will check this section, so it states what remains
*unverified* rather than what was fixed.

1. **Claims this pass could not verify, and did not pretend to.**
   - The sentence "We propose a definition and a test for flight-to-quality,
     flight-from-quality and cross-asset contagion", quoted in §9.3, is
     attributed to the *journal/SSRN-2008* abstract. That text was never obtained
     (VG-3) and the sentence remains an unverified single-session transcription.
   - `eru-1289`'s **2025 CUP chapter** is still unobtained, so the whole
     working-paper-tier caveat stands (VG-6, L-10).
   - **Version identity** between the texts read in 2026-08 and the files fetched
     in 2026-09 is still unprovable — no extraction-time digest exists. Three
     independent fetches returning byte-identical digests bound the risk; they do
     not close it (VG-10).
   - The **four never-read records** (VG-1) and the **280 unobtainable full
     texts** (VG-2) are unchanged and unchangeable by remediation.
2. **Sections this round did NOT re-read, and which therefore still carry the
   error rate the re-read sections had before correction.** §7.2 (O2 power),
   §7.5 (O5 validity conditions), §7.6 (O6 causality) and §7.7 cite tables and
   pages in roughly sixty records whose full texts have **never** been
   re-fetched or re-read at any round. The three rounds have re-read seven texts
   out of a 72-record corpus. **The measured locator error rate on the texts that
   were re-read is high — 19 of the Phillips-line locators and 4 of the NB
   locators were wrong. There is no reason to assume the un-re-read majority is
   cleaner, and this review does not assume it.** That is the single largest
   residual risk in the document.
3. **Numbers whose sole check is a single reading.** Every operating
   characteristic in §7 other than those from the seven re-read texts rests on
   one extraction pass (or two unreconciled passes resolved by convention —
   §2.8, A6). §6's appraisal is convention-resolved, not source-adjudicated.
4. **The distinct-work count is deliberately ambiguous.** 69 and 68 are both
   correct under stated standards (§5.3, VG-13, A14(a)). A consumer needing one
   number should use **68** and read VG-13.
5. **Repository-level gaps this document cannot repair.** VG-14 (no clone-durable
   environment spec), VG-15 (vacuous corpus-stage ReproLog), VG-16 (no committed
   entrypoint re-derives any number). Added this round: `*.jsonl` has no
   `eol=lf` in `.gitattributes`, so no digest can be published for
   `se-extraction-recheck.jsonl` until that is fixed.
6. **Model identity and configuration remain unresolved and unclosable** (VG-11).
7. **The `research-compile` gate returns `block` on this document, and that is
   disclosed rather than engineered away.**
   `python ~/.claude/skills/research-compile/assets/check_lit_review.py` was run
   against this file on 2026-09-02 and returned **`verdict: block`**. Its
   findings fall into four kinds, and only the third is a defect of this review:
   - **Gate-side method artifact (33 of the findings, all G16).** The gate reports
     "DOI … did not resolve (HTTP 403)" for a large and *run-varying* subset of
     the corpus DOIs — 33 on one run, fewer on another. Checked directly on this
     pass: a plain request to `doi.org/{doi}` returns 403 for these DOIs, while
     the **Handle System API** (`doi.org/api/handles/{doi}`, the method this
     review's own identifier check uses) returns `responseCode: 1` for every one
     sampled, including `10.1111/iere.12132`, `10.1111/j.1468-2354.2010.00625.x`,
     `10.3982/QE82` and `10.1093/jjfinec/nbr009`. The identifiers resolve; the
     gate's resolver is being refused. §12.3's 62/62 result stands.
   - **Frontmatter-schema mismatch (G2, G19, and the `n_*` and repro-envelope
     keys).** The gate expects `title`, `objective`, `review_type`,
     `standard_declared`, `eligibility_inclusion`/`_exclusion`, `protocol_path`,
     `protocol_amendments`, `n_identified`/`n_screened`/`n_excluded`/
     `n_included`/`n_duplicates_removed`, `materials_availability`, and a
     five-key repro envelope. This document carries the same information under a
     different vocabulary (`review_kind`, `protocol`, `review_standard`,
     `counts:`, §2.1, §15) established before round 1 and referenced by name
     throughout the document and by the consumer agenda. **The keys were not
     added in this round**: a bulk frontmatter rewrite in the final pass, with no
     audit round left to check it, is exactly the class of confident sweeping
     change that produced the defects rounds 2 and 3 had to fix. It is a real
     conformance gap and it is left open and named, not closed by assertion.
   - **Genuine, already-disclosed gaps.** `eru-0198` carries no
     DOI/PMID/PMCID/arXiv (it has a Handle) — this is **VG-8** and **L-6**, seven
     such records, disclosed since round 1. `screeners_n`, `independent` and
     `automation_tools` are declared in §2.5 and the frontmatter
     `ai_assistance` block in prose rather than in the keys the gate parses.
   - **A serialisation demand this review declines.** The gate wants
     `references_explosive-regime.json` in its own canonical serialisation, which
     would change the store's SHA-256 (`13c76d8f…`) — a digest cited in the
     frontmatter, §5.2, §15 and the round-3 ReproLog. Reserialising in an
     unaudited pass to satisfy a formatter would invalidate all of them. Not
     done.

   **A consumer should read the gate result as: this document does not conform to
   the project's lit-review frontmatter schema, and that non-conformance is now
   on the record.** It is not evidence that the DOIs are bad or the corpus
   unresolved.
8. **The error rate across rounds has not fallen.** Round 1's remediation
   contained three false claims; round 2's contained four, including one inside
   the fix that was created to correct a false claim. This round found and
   corrected them, and no round will now do the same for this one. **Treat every
   uncited assertion in this document as carrying a non-trivial prior of being
   wrong in detail**, and re-open any number that matters against the source
   before acting on it. The §9.5 digest table and `se-verify-r3-01.json` exist to
   make that cheap.

**Not remediated here.** REV-3-1, REV-3-2, SCOPE-3-1, QUANT-3-1 and
LITERATURE-3-1 land on
[research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md)
and are the lead session's to make. §14 carries the inputs, with **two new
consumer-side corrections added this round**: the agenda's "delay cost of
7.56 → 12.20 months" sentence (item 8) and its "corrected 14 locators" sentence
(item 9).

## 19. Change note — round-4 targeted locator verification, 2026-09-03

This is **not** a fourth audit round and **not** a corpus sweep. It executes
Thread C of
[deliverable_spec_s4-reexecution-and-repo-gaps_2026-09-03.md](../deliverables/deliverable_spec_s4-reexecution-and-repo-gaps_2026-09-03.md):
verify the **load-bearing** locators and quoted strings against retrieved full
texts, correct every site of every error, and **leave the rest visibly
unverified rather than silently unverified.**

### 19.1 The boundary, fixed before any source was opened

An item is load-bearing iff it is a page locator, a table / theorem / equation /
footnote identifier, or a quoted string, and it appears **inside §7's synthesis
prose** — the six "Synthesis claim" paragraphs, the four `TO COMPUTE` handoff
paragraphs, the §7.2–§7.4 lead-in paragraphs those claims rest on, §7.6's three
causality traps, §7.7's six pooling-failure rows and §7.8's twelve per-detector
rows — **or** it is cited by
[research_agenda_regime-classification_2026-08-21.md](../research_notes/research_agenda_regime-classification_2026-08-21.md).

**Rows of §7's evidence tables that no synthesis paragraph re-cites are
inventory, not load-bearing, and were deliberately not verified.** So were §8,
§9.1 and §9.3, which rounds 2 and 3 already re-read, and every record outside
the resulting 21. The set is **50 items over 21 records** — 20 of the frozen 72
plus NB-08. Two agenda locators lie outside this review's corpus entirely
(Hall & York 2001 *Statistica Sinica* 11:515–536 and Hamilton 1989
*Econometrica* 57(2):357–384) and are **out of scope by construction** — they
belong to other reviews' corpora, not this one.

### 19.2 Result

- **35 verified**, **7 corrected**, **8 unverifiable** (see L-21 for the
  correction table and VG-17 for the unreachable records).
- Corrected: the PWY Appendix range (a round-3 correction that was itself
  wrong), `eru-0131`'s Evans-collapse design in the §7.7 pooling row,
  `eru-1716`'s PWY size range, `eru-1519`'s crash-monitor claim, `eru-0395`'s
  theorem attribution for the PWY-inconsistency result, and two errors in the
  `eru-0889` / `eru-1038` surveillance row — an incomplete boundary function,
  and a horizon type and a γ value each attributed to the wrong one of the two
  papers.
- **Read against 72.** Fourteen of the 72 records have now been read at full
  text at some verification round: `eru-0131`, `eru-0393`, `eru-0395` and
  `eru-1289` before this pass, and `eru-1044`, `eru-1852`, `eru-1921`,
  `eru-1845`, `eru-1844`, `eru-0889`, `eru-1038`, `eru-1716`, `eru-1519` and
  `eru-1031` here — the last several at their load-bearing points only, and
  `eru-1519` (Sheffield SERPS 2022007), `eru-1031` (Cowles DP 2152) and
  `eru-0889` (Reading CentAUR accepted manuscript) in a version other than the
  one their DOI names. **Fifty-eight records have never been read at any
  verification round**, and the error rate measured on re-read texts across
  rounds 2, 3 and 4 gives no ground for assuming they are clean. The three NB
  texts re-read at round 3 are additional to these fourteen and sit outside the
  frozen 72 (§9.0).

### 19.3 What this round did not do, stated so the absence is a decision

It did not re-screen the corpus, alter the frozen 72, touch the frozen protocol,
or edit the consumer agenda. Agenda corrections arising from it are listed in
§14 and are the lead session's to apply. It did not verify §7's evidence-table
inventory rows, and it could not reach six of the seventeen load-bearing records
at all (VG-17).
