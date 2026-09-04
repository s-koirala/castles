---
title: "Compiled corpus record — stated trading, arbitrage, market-making and adjacent STRATEGIES for binary event contracts, with KalshiEX LLC as the venue of interest (multivocal branch)"
slug: kalshi-strategy-multivocal
date: 2026-09-04
objective: "What trading, arbitrage, market-making and adjacent STRATEGIES for binary event contracts does the retrievable multivocal record STATE, with KalshiEX LLC as the venue of interest; for each, what source states it, at what depth, on what venue was it established, and what preconditions does that source itself say it depends on?"
review_type: scoping
review_type_note: "The frozen protocol's own front matter reads `review_type: multivocal-corpus-compilation` and its section 8.2 fixes the output class as a scoping/mapping compilation in the sense of Arksey & O'Malley 2005 (doi:10.1080/1364557032000119616). The research-compile gate admits only {systematic, scoping, narrative}; `scoping` is the value in that enum that the protocol's own section 8.2 names. The mapping is recorded here so the two vocabularies are not confused, and understating the type to dodge gate items is not what is happening: every item the design does not meet is enumerated in section 13."
standard_declared: >
  SPLIT, and the split is load-bearing. (1) PRISMA-S (Rethlefsen et al. 2021,
  doi:10.1186/s13643-020-01542-z) applies here ON ITS OWN TERMS — NOT adapted,
  NOT by analogy. Its terminology section states verbatim: "Because we intend the
  checklist to be used in all fields and disciplines, we use 'systematic reviews'
  throughout this document as a representative name for the entire family of
  evidence syntheses. This includes, but is not limited to, scoping reviews,
  rapid reviews, realist reviews, metanarrative reviews, mixed methods reviews,
  umbrella reviews, and evidence maps." That is an explicit, quotable
  self-endorsement covering both this record's field and its output class, so
  PRISMA-S items 1, 8, 13 and 15 are claimed DIRECTLY. The predecessor record's
  blanket "PRISMA-S (adapted, non-clinical)" framing understates PRISMA-S and is
  deliberately NOT copied. (2) PRISMA 2020 (Page et al. 2021, doi:10.1136/bmj.n71)
  is NOT claimed and does NOT reach this record: its own scope statement is
  "designed primarily for systematic reviews of studies that evaluate the effects
  of health interventions", extended only to other SYSTEMATIC reviews. EVERY
  PRISMA 2020 ITEM INVOKED IN THIS RECORD — items 8 and 16b included, and they are
  invoked because the gate anchors carry those names — IS REASONING BY ANALOGY
  WITH NO CITED ENDORSEMENT, and is declared as such here and at each point of
  use. (3) The output class is a scoping/mapping compilation; framework citation
  Arksey & O'Malley 2005 (doi:10.1080/1364557032000119616, the domain-neutral
  record of the three), checklist citation Tricco et al. 2018 PRISMA-ScR
  (doi:10.7326/M18-0850) WITH its EQUATOR-developed health framing declared and NO
  claim of PRISMA-ScR compliance made. Declining a risk-of-bias instrument is
  supported by Levac, Colquhoun & O'Brien 2010 (doi:10.1186/1748-5908-5-69),
  "Scoping studies differ from systematic reviews because authors do not typically
  assess the quality of included studies" — declared transfer, that source is
  explicitly about health research. The evidence for every clause above is
  docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json
  instruments 6 and 7, verified before the protocol froze.
unit_of_account: >
  THE DISPOSITIONED RECORD. A record is an object to which this corpus assigns an
  F1 identifier and for which at least one arm log on disk holds the stored
  response that identified it. THE UNIT IS NOT HOMOGENEOUS ACROSS ARMS and no
  reading of any count in this record is valid without that sentence: the ACADEMIC
  arm's record is one bibliographic row returned by a scholarly index; the
  SOFTWARE arm's record is one public code or package artifact keyed by host plus
  full name (or package-index name); the VENUE arm's record is one retrieved
  document with a byte digest, which may carry many clauses; the LATERAL arm's
  record is one sourced STRATEGY CLASS, and two classes may share one retrieved
  payload. A count of 1,269 software rows and a count of 37 lateral rows are
  therefore NOT commensurable objects, and their sum means nothing except inside
  the section 4.5 flow identities, which are arithmetic over identifiers and not
  over comparable things. Section 5 states this again, with the arithmetic.
eligibility_inclusion:
  - "N1. The record concerns at least one in-scope instrument under section 2.2, or the counterparty leg extension there."
  - "N2. The record makes at least one strategy contribution K1-K4."
  - "N3. The record is retrievable by the executing agent without authentication, payment, or account creation, and its retrieved bytes can be digested — a SHA-256 over the retrieved payload is recordable. A record whose bytes cannot be digested is excluded under Y4."
  - "N4. The record is dated, or its access date is recordable. A publication date, commit or release date, effective date, or an ISO-8601 access timestamp all satisfy N4; at least one must be recorded."
  - "N5. Any language, any year, any source class S-A..S-E satisfying N1-N4. No document type is closed out in advance."
  - "N6. Where a record's eligibility turns on content that its metadata does not settle, it is promoted to stage 2 (section 4) rather than decided at stage 1."
eligibility_exclusion:
  - "Y1 — not an in-scope instrument. Fails section 2.2 and is not a stated counterparty leg of an in-scope pairing. Absorbs what the predecessor split across X1, X3 and X5."
  - "Y2 — no strategy contribution. Satisfies section 2.2 but makes none of K1-K4: descriptive commentary, market news, an explainer of what an event contract is, a price screenshot with no rule, no measurement, no precondition, and no tooling. Absorbs the predecessor's X2 and X4."
  - "Y3 — UNSOURCED. The strategy is asserted with no locatable source — it came from a summarizer, from an executing agent's own recall, or from a document that cannot be produced. Such a class is excluded, and it is never recorded as a finding."
  - "Y4 — not retrievable or not digestible. Fails N3: paywalled, behind authentication, dead link with no archived copy, or retrieved as a form that cannot be digested."
  - "Y5 — undated and no recordable access date. Fails N4."
  - "Y6 — paid product advertisement with no stated mechanism."
  - "Y7 — duplicate. The same work already dispositioned under another locator; deduplicated per section 4.1 and itemized in the ledger with a pointer to the retained record."
  - "Y8 — mirror or fork with no independent contribution."
  - "Y9 — out of the branch's question. In-scope instrument, real contribution, but about something the section 1.1 question does not ask — for example pure tax filing mechanics with no bearing on executability, or platform UX."
capacity_codes:
  - "G1 — identified, eligibility not assessed. The record entered the universe and no eligibility determination under N1-N6 was ever made for it. It is NOT eligible, NOT ineligible: it is UNDECIDED. Nothing about its merits was determined. G-rows sit inside n_excluded ONLY so the section 4.5 identities close, and are reported separately from every Y-code count (protocol section 4.4 rule 2)."
  - "G2 — eligible, extraction not performed. Count: 0. No record in this corpus carries G2."
registration: "not-registered (PROSPERO accepts only reviews with health-related outcomes and this review has none). The registration event is the provenance commit 4821611c1c93b5f929a76f3ba6207e900440cee5, which committed the frozen protocol before the first query of any arm executed."
protocol_path: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md   # frozen-prefix sha256 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac over the first 91,498 bytes, re-verified against the bytes on disk at authoring time; the M1 AND M2 addenda are appended BELOW the frozen line and the prefix digest is unchanged by either (re-verified after both appends; corrected 2026-09-04, round-2 finding CRITICAL-2-1, this comment previously named only the M1 addendum)
protocol_amendments: "TWO numbered append-only amendments, M1 and M2. CORRECTED 2026-09-04 by round-2 audit remediation (findings CRITICAL-2-1, SCOPE-2-1, QUANT-2-1, LITERATURE-2-1, raised independently by four branches): this field previously opened 'ONE numbered append-only amendment, M1', which was false from the moment M2 was issued during round-1 remediation, and protocol section 10 makes a corpus record that ran under an amendment it does not enumerate DEFECTIVE. The superseded opening is retained here. M2 (2026-09-04, POST-EXECUTION, raised by audit finding SCOPE-1-7) reconciles the frozen protocol's own section 4.2 disposition enumeration with its section 4.4 capacity codes: section 4.2 lists exactly three stage-1 outcomes (include / exclude-with-Y-code / promote) and section 4.4 then creates G1 and G2, which are none of the three, so 1,465 of the 1,574 screened records in THIS record - 93% of the delivered flow - took a path the frozen text did not enumerate. M2 rules that a G-code is a FOURTH stage-1 outcome and that section 4.2's 'exactly one disposition' is conditional on assessment capacity. M2 IS EXPLICITLY WEAKER THAN M1 AND SAYS SO: it is POST-EXECUTION, meaning the 1,465 G-dispositions were assigned BEFORE the contradiction was adjudicated, whereas every part of M1 was decided PRE-SCREENING. M2 changes no eligibility criterion, no disposition, no count and no arithmetic identity; the n_excluded == Y-rows + G-rows decomposition this record publishes (10 + 1,465 = 1,475) is exactly what it reconciles. Full text in the protocol addendum and at ks-amendments.jsonl line 3. M1 remains as enumerated below: M1, enumerated in full in section 3.3 of this record and registered at docs/literature/search_logs/kalshi-strategy-multivocal/ks-amendments.jsonl with its prose twin in the protocol's own addendum. M1 (2026-09-04) rules on ACADEMIC-arm query admissibility only and was decided PRE-SCREENING by the lead session, not by the executing agent: M1(a) GRANTED-WITH-NARROWED-CONSTRUAL, contract-family qualifiers (weather derivative, economic derivatives, macroeconomic derivatives) in the instrument slot, admissible only as an event-derivative family (conditions 1) or as a section 2.2 counterparty leg (condition 2, which is how `weather derivative` enters), queries ks-crossref-16/17, ks-openalex-09/10/11, ks-arxiv-09/10, traceability tag reached_via: M1a; M1(b) GRANTED-NARROWLY, the agent/model-class qualifier abs:\"trading agent\" in the strategy slot at ks-arxiv-13, on the ground that section 3.4's frozen lateral seed list item 10 already names model-agent forecasters, traceability tag reached_via: M1b; M1(c) GRANTED-AS-A-REACHING-DEVICE-ONLY, the container restriction query.container-title=SSRN at ks-crossref-14, admissible only because it REACHES a source otherwise unreachable (ks-ssrn-01 returned HTTP 403 unauthenticated) and never where it would EXCLUDE, traceability tag reached_via: M1c. M1 alters NO eligibility criterion, NO contribution code, NO extraction field, NO taxonomy class, NO screening rule and NO arithmetic identity. A reviewer rejecting any part may withdraw exactly the records tagged with that part's reached_via value and no others: 67 records reached only via M1a, 3 only via M1b, 20 only via M1c — and ALL of them are G1 rows whose eligibility was never decided, so no inclusion in this corpus rests on M1."
bibliography: docs/literature/references_kalshi-strategy-multivocal.json
bibliography_sha256: c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df
bibliography_store_covers: 99   # EQUALS n_included. The protocol section 4.5 identity `len(bibliography store) == n_included` CLOSES. The predecessor branch's verification gap AG-11 — 149 store entries against 327 included records — is NOT repeated. The store is a RECORD store, not a document store: two entries may share a URL and a byte digest where the unit of account (a strategy class) is finer than the document.
n_identified: 1986
n_duplicates_removed: 412
n_screened: 1574
n_excluded: 1475
n_criterion_excluded: 10      # Y-code rows only: Y2 3, Y3 5, Y4 1, Y9 1
n_capacity_gap: 1465          # G1 rows only: 528 academic + 937 software. G2 = 0. Reported SEPARATELY from every Y-code count, per protocol section 4.4 rule 2
n_included: 99
extraction_depth: "MIXED, and the mixture is the warrant label that travels with every claim (protocol field F6). Of the 99 included records: 28 S-C records at README-and-metadata depth, 12 S-C records at metadata depth, 26 S-D records at full-text depth of the retrieved bytes (two of those flagged DEGRADED by their own extraction, and two of the 26 scoped to a named part or body rather than a whole publication) and 2 S-D records at metadata depth (ks-vr-d24, ks-vr-d30, both of which are regulator query-result listings), 29 lateral records at full text of the retrieved page, and 2 lateral records at SECONDARY depth (KSL-C15, KSL-C25) where the rule text is quoted by a practitioner source and the primary document was not retrieved. NO record in this corpus is a peer-reviewed record: the academic arm assigned no verdict and contributes zero included records."
screening_verdict_source: "READ-BASED for 100% of the 109 records that received any eligibility verdict — 43 software artifacts assessed by the software arm at the depth its records state, 30 venue documents assessed by the lead session against the frozen N/Y criteria, 31 lateral class records (32 sourced by the arm, less KSL-C31 removed at the cross-arm deduplication step of section 5.2, which precedes screening) assessed by the lateral arm at retrieval, and 5 unsourced candidate classes dispositioned Y3. CORRECTION 2026-09-04 (finding REV-1-7): this field previously read '32 lateral class records assessed by the lateral arm at retrieval', which itemised to 110 against a stated total of 109; the superseded wording is recorded here, and the itemisation now closes at 43 + 30 + 31 + 5 = 109. NO KEYWORD CLASSIFIER ASSIGNED ANY VERDICT IN THIS CORPUS. The 1,465 G1 rows received NO verdict of any kind and are undecided, not classifier-verdicted: this is the structural difference from the predecessor branch, where 96.1% of dispositions were keyword-classifier outputs. The trade is deliberate and is not an improvement in coverage — it is a much smaller decided set."
materials_availability:
  - docs/literature/search_logs/kalshi-strategy-multivocal
  - docs/literature/references_kalshi-strategy-multivocal.json
  - docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md
  - docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md
competing_interests: none
ai_assistance: "Claude Opus 5 (model id claude-opus-5; Claude Code / Claude Agent SDK) executed all four arms and compiled this record. Role per ICMJE 2026 disclosure (https://www.icmje.org/recommendations/): code + prose + audit-support. AI is not and cannot be an author. The model is the declared automation tool for the selection process (see the prisma-2020-8 block in section 5, and note that PRISMA 2020 item 8 is invoked by ANALOGY per standard_declared clause 2). No metadata field, no quotation and no count in this record was written from model memory; every one traces to a stored response in the search-log directory named under materials_availability."
git_head_at_authoring: 4821611c1c93b5f929a76f3ba6207e900440cee5
pip_freeze_sha256: "495798ac328ee7cc673610470fe1d344e15a2dd942b22c0cb9ada0cd6a01115a"  # archived at logs/reproducibility/env/495798ac....txt, written by the SessionStart hook at 2026-09-04T10:06 local, BEFORE the first arm query at 2026-09-04T10:14:45-05:00. UNTRACKED LOCATOR (logs/ is gitignored); the clone-durable carrier is the Repro-Log-Path / Repro-Log-SHA256 trailer on the provenance commit. Every executing script in this branch used the Python 3.11 standard library only
dataset_checksums: "n/a (no dataset). NO MARKET DATA WAS ACQUIRED, NO EXCHANGE API WAS CALLED, no price was computed and nothing was fitted or backtested (ADR-0003). The corpus store digest is the frontmatter bibliography_sha256. Per-payload digests are carried per query in the arm logs and per record in the store's `note` and `custom.sha256_of_retrieved_bytes` fields."
rng_seed: "0. CORRECTED 2026-09-04 by round-1 audit remediation (finding REPRODUCIBILITY-1-4): this field previously read 'asserted at entry of every script in this branch — ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-query-table.py, and the store builder that emitted references_kalshi-strategy-multivocal.json', and THREE of those particulars were false. The superseded wording is retained here and the verified state is: PYTHONHASHSEED=0 is asserted at entry of THIRTEEN scripts — the five academic scripts ks-academic-extract.py, ks-academic-assemble.py, ks-academic-recovery-pass.py, ks-academic-runner.py and ks-academic-query-table-supplementary.py (the latter two always asserted and this field omitted them), plus all SEVEN S-C scripts under ks-github-scripts/ (run_search.py carried a no-op os.environ.setdefault that could not work and now carries a real assert; the other six had none and now do), plus the run_arm.py shim which inherits the runner's assert. ks-academic-query-table.py does NOT assert and correctly does not: it is a pure data table with no set or dict iteration and no hash-order dependence, and a comment in the file states why. THE STORE BUILDER CLAUSE IS WITHDRAWN AS FALSE: no script emitting references_kalshi-strategy-multivocal.json exists anywhere in this repository, so the store's construction is not re-runnable at all — registered as gap G-28. Verified by negative control: with PYTHONHASHSEED unset all thirteen assert-carrying scripts raise AssertionError at entry and nothing else executes; with PYTHONHASHSEED=0 all pass. THIS IS NOT A REPRODUCIBILITY CLAIM ABOUT THE VERDICTS: all 109 eligibility verdicts and all extractions in this corpus are single-pass LLM outputs with no archived prompt and no recoverable sampling parameters, and a re-run is not guaranteed to reproduce them. The seed pins the deterministic halves — deduplication, branching, ordering, serialization — and nothing else."
model_commit: "n/a (no model artifact; this record fits nothing and estimates nothing)"
---

# Compiled corpus record — stated strategies for binary event contracts, with KalshiEX LLC as the venue of interest (multivocal branch)

**Read this first.**

This artifact is a **compiled corpus record** produced by a **registered
multivocal search**. It is **not a systematic review** and must never be
described as one. It reports **no inter-rater agreement statistic** (there was
one screener; with one screener there is nothing to agree with and reporting an
agreement number would be a fabrication). It reports **no certainty-of-evidence
grade**. The absence of a risk-of-bias table is a **declared design limit**, not
an oversight (frozen protocol section 8, and Levac et al. 2010 on why a scoping
output class may decline one). It records what sources *state*. It fits nothing,
acquires no market data, calls no exchange API, computes no price, backtests
nothing, and **states no tradeable rule, no position size and no expected
return** (ADR-0003, restated in protocol section 9).

**What this artifact is NOT, stated before any number is read:**

- It is **not a finding that any strategy works**. Every outcome any source
  reports is transcribed verbatim and attributed to that source, and is never
  adopted as this corpus's own claim.
- It is **not an assessment of the academic literature.** See limitation 1.
- It is **not a census** of anything: not of repositories, not of venue
  documents, not of practitioner writing. Every arm reported coverage limits and
  they are carried here in full.
- It is **not a current statement of venue rules.** Every rule quoted is dated
  **2026-09-04 by retrieval**, and 17 CFR 40.6 requires only ten business days'
  notice for a rule change and one business day for a product listing
  (clauses `d22-c1`, `d22-c3`). A clause quoted without that date is worthless.

## The ten limitations a reader must carry into every number below

*(Was nine. A tenth was added 2026-09-04 by round-2 audit remediation — the known-item recall result, which round 1 executed but published only outside this record.)*

1. **The academic arm assigned NO screening verdict to any record. All 528 of its
   deduplicated records are `G1`: identified, eligibility not assessed.** Nothing
   about the merits of any of them is determined — they are not eligible and not
   ineligible, they are **undecided**. The arm's own candidate table says so in
   those words, and the branching labels `B1`-`B4` it carries are *routing signals
   over retrieved metadata*, not determinations under N1-N6, K1-K4 or Y1-Y9.
   **Consequence: this corpus contains zero peer-reviewed and zero preprint
   records, and every claim in it rests on S-C, S-D or S-E sources.** The
   evidence-hierarchy tier of the entire included corpus is therefore tier 2
   (official documentation) and tier 5 (everything else, admissible only with the
   tier recorded next to the claim), never tier 1.
   *Evidence:* `ks-academic-candidates.json` field `what_this_is_NOT`;
   `ks-academic-stage1-branch-rule.md` section "What this rule is NOT";
   `ks-academic-identified-universe.json` (528 rows).
2. **The software arm assessed 43 of the 981 artifacts it identified. 938 are
   `G1`** — 937 after the one cross-arm duplicate removed in section 5. The
   assessed subset is a **non-random sample of a non-random sample**: the frozen
   query grid's yield is already ranked and truncated by undisclosed
   platform-internal relevance and popularity signals, and the subset rule then
   drew deterministically from within that yield by `sha256(host + "/" +
   full_name)` order. No completeness bound is claimed and none is attributable
   to the repository-mining literature the protocol cites, which supplies none.
   *Evidence:* `ks-github-capacity-ledger.json` counts block;
   `ks-github-subset-rule.md` sections "The rule" and "Declared consequence".
3. **The venue arm's document-class pass is SAMPLED, not exhaustive.** Of the
   filing register's **111 enumerated KEX rule filings, five were retrieved in
   full**; of roughly **ninety contract series named in the fee schedule, ONE was
   specified** at terms-and-conditions depth; **34 further designated contract
   markets are enumerated and left unretrieved.** A per-series or per-filing
   statement in this record is a statement about the retrieved sample and about
   nothing else.
   *Evidence:* `ks-venue-docs.json` `document_classes` entries 1, 2, 7 and 9.
4. **THE RULEBOOK IN FORCE ON 2026-09-04 WAS NOT LOCATED.** The venue's own
   rulebook page returns **HTTP 200 with no rule text in the retrieved bytes** —
   the body is client-rendered behind an AWS WAF challenge (`KS-VR-Q01`,
   `KS-VR-Q01b`), and no rulebook PDF exists at any of five candidate paths
   probed (`KS-VR-Q02`, `Q14`, `Q15`, `Q16`, `Q17`). The same pattern holds for
   the venue's regulatory-notices channel (`KS-VR-Q48`), its pending-fee-change
   page (`KS-VR-Q18`), its contract-drafts page (`KS-VR-Q12`), the paired venue's
   rulebook route (`KS-VR-Q58`) and PredictIt's rules page (`KS-VR-Q61`). **HTTP
   200 is not retrieval.** The three rulebook copies reachable through the
   regulator are a 2019 redacted version (`ks-vr-d14`), a 2023 redline whose text
   extracts corrupted (`ks-vr-d13`), and a document that is not Kalshi's at all
   (`ks-vr-d12`, see section 11). **Every rulebook-level statement in this record
   is therefore made from a superseded or degraded copy, and is labelled as
   such.**
5. **Three of the most executability-relevant objects are WITHHELD AT SOURCE, not
   merely unretrieved.** They are filed confidentially under the redaction right
   17 CFR 40.6 grants (`d22-c2`), so no amount of further searching produces
   them:
   (a) **the market-maker/liquidity-provider selection procedure** — "The
   procedure by which the Exchange anticipates making such determinations is
   described in Appendix B" (`d19-c3`), Appendix B confidential;
   (b) **which contracts carry elevated position limits** — "appendix A is
   confidential and submitted under a request for confidential FOIA treatment"
   (`d16-c5`);
   (c) **the settlement Source Agency appendix** — "Appendix E (Confidential) -
   Source Agency" (`d21-c11`).
   Additionally the **Market Maker Agreement** that gates every incentive
   (`d19-c1`) is not a published document and was not located at any endpoint
   searched.
6. **Novelty differencing is an UPPER BOUND.** The prior-identifier index covers
   **6,923 of the predecessor branch's 8,813 records** — only those carrying a
   DOI, arXiv id, RePEc handle or Handle. A predecessor record with no identifier
   cannot be differenced by this index, so "novel" here means **"not matched in
   the index"**, never "not previously seen". The arm reports 437 of 528 novel
   and 91 already dispositioned; **437 is an upper bound on novelty with no
   recorded lower bound above 437 − (8,813 − 6,923) = 0 by that construction, and
   the corpus states no lower bound.**
   *Evidence:* `ks-prior-identifiers.json` `_meta`;
   `ks-academic-stage1-branch-rule.md` section "Novelty differencing".
7. **The unit of account is not homogeneous across arms.** See the front-matter
   `unit_of_account` field and section 5. Adding 1,269 software rows to 37
   lateral rows produces a number that is valid inside the flow identities and
   meaningless outside them.
8. **Every included record carries a standing findability gap.** ADR-0006 drops
   the predecessor's persistent-identifier requirement, so **no record in this
   corpus has a DOI, PMID, PMCID or arXiv id** and every locator is a URL subject
   to link rot and content drift. The SHA-256 of the retrieved bytes fixes the
   **bytes**, not the URL's future content. This is the price ADR-0006 records
   itself as paying, and it is the reason the research-compile gate's assertion
   G13 cannot pass for this artifact (section 15, gap **G-15**).
9. **The weather stratum's near-zero yield is NOT a clean absence.** **Two**
   executed academic queries in that stratum returned zero — `ks-arxiv-04` and
   `ks-openalex-04` (both HTTP 200, `n_returned` 0, `n_total_reported` 0, no
   failure field). Two further queries in that stratum, `ks-repec-04` and
   `ks-repec-04-b`, **never executed at all**: their logs carry
   `platform_interface_failure` and `n_returned_semantics: "no search executed;
   not an observed zero-yield"`. The one query aimed squarely at temperature
   settlement **never executed at all** across eleven attempts. See section 10,
   negative results **N-5** and **N-8**, data-integrity entry **DI-8**, and gap
   **G-26**. Do not read that stratum's emptiness as evidence about the
   literature.
   > **CORRECTION 2026-09-04 (round-1 audit; REV-1-1, SCOPE-1-1, QUANT-1-1,
   > LITERATURE-1-1, REPRODUCIBILITY-1-1, FORMAT-1-1).** This limitation
   > previously read *"Four executed academic queries in that stratum returned
   > zero, and the one query aimed squarely at temperature settlement **never
   > executed at all** across eleven attempts."* The words "Four executed" are
   > **struck**: they reported a platform-interface failure as an observed
   > zero-yield, the exact inference this record's own section 5.4 and section 10
   > say a defective record makes. The corrected count is **two**. The superseded
   > wording is retained above and not overwritten (protocol section 10; this
   > project's 21 CFR 11.10(e) practice).

---

## 1. Objective, eligibility and how records were grouped

The question this record answers is in the front matter and is quoted from the
frozen protocol section 1.1. It asks **what the record STATES**, not what is true
of the venue and not what is profitable. Its answer is a corpus of attributed
strategy statements.

**Eligibility** is the frozen N1-N6 / Y1-Y9 set reproduced byte-faithfully in the
front matter from protocol sections 2.3 and 2.4, together with the strategy-
contribution codes **K1** (states or implements), **K2** (measures or reports),
**K3** (precondition or constraint), **K4** (enabling data or tooling), and the
source classes **S-A** peer-reviewed, **S-B** preprint/working paper, **S-C**
public software repository or package, **S-D** exchange or regulator document,
**S-E** practitioner grey literature. The instrument scope is protocol section
2.2's B-a/B-b/B-c/B-d conjunction, carried by reference from the predecessor
protocol, plus the section 2.2 counterparty-leg extension, which admits a
non-binary leg **only when the record states the pairing** against an in-scope
instrument.

**Grouping for synthesis** is the protocol section 6 first-level taxonomy
**T1-T8**, reproduced in section 8. No class was prejudged; a class an arm found
that fitted no bucket would have been **added by amendment, never forced**, and
the lateral arm's log records `classes_fitting_no_taxonomy_bucket: []` and
`amendment_needed: null`, so no such amendment was required.

**Evidence-hierarchy tier per class of record** (CLAUDE.md, enforced during
screening and recorded in the section 7 corpus table's `role` column):
**tier 2 — official documentation** for every S-D record (the venue's and the
regulator's own documents); **tier 5 — everything else, admissible only with the
tier recorded next to the claim it supports** for every S-C and S-E record.
**Tier 1 (peer-reviewed literature) is empty in this corpus** — see limitation 1.
No S-C or S-E statement in this record is presented as established; each is
presented as *what that source states*.

---

## 2. Information sources and methods

<!-- prisma-s-1 -->
PRISMA-S items 1, 2 and 13, claimed directly (see `standard_declared`). One row
per source, naming the **platform/interface**, not merely the database. Every
source was searched on **2026-09-04**; the branch executed in a single window.
`n_records` is the count of records **that source returned into the arm's
universe**, in that arm's unit of account (front matter `unit_of_account`).

| source | platform | date_searched | query_id | n_records |
|---|---|---|---|---|
| Crossref | api.crossref.org REST, unauthenticated | 2026-09-04 | ks-crossref | 380 |
| OpenAlex | api.openalex.org REST, unauthenticated | 2026-09-04 | ks-openalex | 149 |
| arXiv | export.arxiv.org/api/query Atom API | 2026-09-04 | ks-arxiv | 70 |
| Semantic Scholar Academic Graph | api.semanticscholar.org/graph/v1, unauthenticated | 2026-09-04 | ks-s2 | 51 |
| RePEc / IDEAS | ideas.repec.org site search over HTML | 2026-09-04 | ks-repec | **0 — INTERFACE FAILURE, NOT A ZERO YIELD.** No search executed; see DI-8, G-26 |
| SSRN | papers.ssrn.com site search over HTML | 2026-09-04 | ks-ssrn | **0 — INTERFACE FAILURE, NOT A ZERO YIELD.** HTTP 403 unauthenticated; see DI-8 |
| GitHub repositories | api.github.com REST v3 /search/repositories, unauthenticated | 2026-09-04 | ks-gh | 832 |
| GitHub code | api.github.com REST v3 /search/code, unauthenticated | 2026-09-04 | ks-ghcode | **0 — INTERFACE FAILURE, NOT A ZERO YIELD.** HTTP 401 unauthenticated; see G-22, DI-8 |
| GitLab projects | gitlab.com REST v4 /api/v4/projects, unauthenticated | 2026-09-04 | ks-gl | 26 |
| PyPI | pypi.org JSON API /pypi/{name}/json | 2026-09-04 | ks-pypi | 11 |
| npm registry | registry.npmjs.org REST /-/v1/search | 2026-09-04 | ks-npm | 400 |
| Kaggle kernels | kaggle.com public API /api/v1/kernels/list | 2026-09-04 | ks-nb | **0 — INTERFACE FAILURE, NOT A ZERO YIELD.** HTTP 401 unauthenticated; see G-22, DI-8 |
| KalshiEX venue site | kalshi.com and assets.kalshi.com, direct HTTP | 2026-09-04 | ks-vr-kalshi | 5 |
| KalshiEX developer documentation | docs.kalshi.com, direct HTTP | 2026-09-04 | ks-vr-docskalshi | 5 |
| CFTC filings, orders, press and organization records | cftc.gov, direct HTTP | 2026-09-04 | ks-vr-cftc | 13 |
| eCFR | ecfr.gov renderer API v1 | 2026-09-04 | ks-vr-ecfr | 1 |
| Federal Register | federalregister.gov API v1 | 2026-09-04 | ks-vr-fedreg | 1 |
| Polymarket US (QCX LLC) documentation | docs.polymarket.us and polymarket.us, direct HTTP | 2026-09-04 | ks-vr-polymarketus | 4 |
| Polymarket documentation | docs.polymarket.com and polymarket.com, direct HTTP | 2026-09-04 | ks-vr-polymarket | 1 |
| CME, PredictIt and Betfair rule surfaces | cmegroup.com, predictit.org, betfair.com, direct HTTP | 2026-09-04 | ks-vr-othervenues | 0 |
| Open-web practitioner literature | Claude Agent SDK built-in web search, US-only index, plus direct HTTP retrieval | 2026-09-04 | ks-lateral | 37 |

<!-- prisma-s-2 -->
**Multi-database platform searches: none.** Every source above was queried at its
own endpoint. No federated or multi-database platform interface was used, so no
row above stands for more than one database.

<!-- prisma-s-3 -->
**Study registries searched: none.** PROSPERO accepts only reviews with
health-related outcomes and this review has none; ClinicalTrials.gov, ICTRP and
OSF hold no records of the classes this question asks about. This is a
deliberate non-search, not an omission.

<!-- prisma-s-4 -->
**Online and print sources purposefully searched or browsed.** Three of the four
arms are purposeful browsing rather than index querying, and that is the design:
the VENUE-AND-REGULATOR arm pursued documents **by document class** (rulebook and
amendments; contract specifications and settlement sources; fee schedule and
maker/taker structure; position and membership limits; market-maker and liquidity
programs; API documentation and rate limits; self-certification filings; agency
orders, letters, dockets and press; equivalent rule documents for paired venues)
directly at the publishers' own endpoints, with **no free-text web search engine
used by that arm at all**. The LATERAL/PRACTITIONER arm worked ten frozen seeds
through a general web-search endpoint and then retrieved candidates directly.
The SOFTWARE arm queried code hosts and package indexes. No print source was
consulted.

<!-- prisma-s-5 -->
**Citation searching: none as a distinct arm.** No backward or forward citation
chase was executed. The only reference-trail following that occurred is what was
visible inside pages the lateral arm had already retrieved, which the arm records
as such and which is **not** a citation-searching arm. This is a coverage limit,
not a claim.

<!-- prisma-s-6 -->
**Contacts with authors, experts, manufacturers or venues: none.** No account was
created, no login was performed, no API key was obtained, no authenticated
endpoint was called, and no order was placed. Two of the objects this record
names as gaps — the Market Maker Agreement and the confidential appendices — are
obtainable, if at all, only by contact of that kind, which this branch's
constraints forbid.

<!-- prisma-s-7 -->
**Other information sources and methods.** One: the **prior-identifier index**
`ks-prior-identifiers.json`, 6,923 identifiers derived entirely from two files
already in this repository, used by the academic arm for novelty differencing
against the 2026-09-02 branch. It **executes no query and retrieves nothing**; it
is an input to a search, never an output of one. Its coverage bound is
limitation 6.

---

## 3. Search strategies

<!-- prisma-s-8 -->
PRISMA-S item 8, claimed directly: the strategies below are **copied and pasted
exactly as run**. One fence per `query_id` in the source table above; inside each
fence, each query string occupies its own line, immediately preceded by a comment
line carrying that query's own identifier, execution timestamp, HTTP status and
returned count, **so that no character of any executed string is altered**.
**Zero-yield queries are never dropped** (protocol section 3.0): 72 of the 112
academic queries, 13 of the 59 software queries, and 23 of the 87 venue queries
returned nothing and every one of them is below.

```text ks-crossref
# ks-crossref-01 | executed 2026-09-04T10:14:45-05:00 | HTTP 200 | n_returned=20 | n_total_reported=320754
https://api.crossref.org/works?query.bibliographic=Kalshi+event+contract+execution&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-02 | executed 2026-09-04T10:14:47-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1560442
https://api.crossref.org/works?query.bibliographic=binary+event+contract+market+making&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-03 | executed 2026-09-04T10:14:49-05:00 | HTTP 200 | n_returned=20 | n_total_reported=845980
https://api.crossref.org/works?query.bibliographic=designated+contract+market+event+contract+inventory&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-04 | executed 2026-09-04T10:14:51-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1204378
https://api.crossref.org/works?query.bibliographic=sportsbook+prediction+market+arbitrage&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-05 | executed 2026-09-04T10:14:52-05:00 | HTTP 200 | n_returned=20 | n_total_reported=696269
https://api.crossref.org/works?query.bibliographic=sports+event+contract+mispricing&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-06 | executed 2026-09-04T10:14:54-05:00 | HTTP 200 | n_returned=20 | n_total_reported=439587
https://api.crossref.org/works?query.bibliographic=weather+event+contract+hedging&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-07 | executed 2026-09-04T10:14:56-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1516809
https://api.crossref.org/works?query.bibliographic=temperature+precipitation+event+contract+settlement+arbitrage&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-08 | executed 2026-09-04T10:14:58-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1990995
https://api.crossref.org/works?query.bibliographic=economic+event+contract+hedging+CME+fed+funds+futures&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-09 | executed 2026-09-04T10:14:59-05:00 | HTTP 200 | n_returned=20 | n_total_reported=343641
https://api.crossref.org/works?query.bibliographic=inflation+CPI+event+contract+mispricing&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-10 | executed 2026-09-04T10:15:01-05:00 | HTTP 200 | n_returned=20 | n_total_reported=919081
https://api.crossref.org/works?query.bibliographic=Kalshi+Polymarket+PredictIt+cross+venue+arbitrage&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-11 | executed 2026-09-04T10:15:03-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1316830
https://api.crossref.org/works?query.bibliographic=binary+event+contract+quoting+collateral+capital+efficiency&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-12 | executed 2026-09-04T10:15:05-05:00 | HTTP 200 | n_returned=20 | n_total_reported=2194293
https://api.crossref.org/works?query.bibliographic=prediction+market+forecasting+driven+trading+agent&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-13 | executed 2026-09-04T10:15:07-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1762881
https://api.crossref.org/works?query.bibliographic=Betfair+Iowa+Electronic+Markets+event+contract+coherence&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-14 | executed 2026-09-04T10:15:09-05:00 | HTTP 200 | n_returned=20 | n_total_reported=10737
https://api.crossref.org/works?query.bibliographic=Kalshi+event+contract+market+making+arbitrage&query.container-title=SSRN&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-15 | executed 2026-09-04T10:15:11-05:00 | HTTP 200 | n_returned=20 | n_total_reported=747296
https://api.crossref.org/works?query.bibliographic=event+contract+hedging+government+shutdown+payrolls+GDP+macroeconomic+announcement&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-16 | executed 2026-09-04T10:36:43-05:00 | HTTP 200 | n_returned=20 | n_total_reported=2074233
https://api.crossref.org/works?query.bibliographic=economic+derivatives+auction+binary+option+payrolls+CPI+arbitrage&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-17 | executed 2026-09-04T10:36:45-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1525537
https://api.crossref.org/works?query.bibliographic=weather+derivative+temperature+binary+option+hedging&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-18 | executed 2026-09-04T10:36:47-05:00 | HTTP 200 | n_returned=20 | n_total_reported=295107
https://api.crossref.org/works?query.bibliographic=Kalshi+event+contract+hedging&rows=20&select=DOI,title,issued,container-title,type,author,abstract
# ks-crossref-19 | executed 2026-09-04T10:36:49-05:00 | HTTP 200 | n_returned=20 | n_total_reported=1273517
https://api.crossref.org/works?query.bibliographic=fully+collateralized+binary+payoff+event+contract+exchange+inventory+capital&rows=20&select=DOI,title,issued,container-title,type,author,abstract
```

```text ks-openalex
# ks-openalex-01 | executed 2026-09-04T10:15:12-05:00 | HTTP 200 | n_returned=4 | n_total_reported=4
https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20AND%20%22market%20making%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-02 | executed 2026-09-04T10:15:16-05:00 | HTTP 200 | n_returned=25 | n_total_reported=30
https://api.openalex.org/works?filter=title_and_abstract.search:%22Kalshi%22%20AND%20%22arbitrage%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-03 | executed 2026-09-04T10:15:19-05:00 | HTTP 200 | n_returned=6 | n_total_reported=6
https://api.openalex.org/works?filter=title_and_abstract.search:%22sports%20betting%22%20AND%20%22arbitrage%22%20AND%20%22exchange%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-04 | executed 2026-09-04T10:15:23-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://api.openalex.org/works?filter=title_and_abstract.search:%22weather%22%20AND%20%22event%20contract%22%20AND%20%22hedging%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-05 | executed 2026-09-04T10:15:26-05:00 | HTTP 200 | n_returned=4 | n_total_reported=4
https://api.openalex.org/works?filter=title_and_abstract.search:%22prediction%20market%22%20AND%20%22macroeconomic%22%20AND%20%22hedging%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-06 | executed 2026-09-04T10:15:30-05:00 | HTTP 200 | n_returned=25 | n_total_reported=54
https://api.openalex.org/works?filter=title_and_abstract.search:%22Polymarket%22%20AND%20%22arbitrage%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-07 | executed 2026-09-04T10:15:34-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://api.openalex.org/works?filter=title_and_abstract.search:%22binary%20contract%22%20AND%20%22bid-ask%20spread%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-08 | executed 2026-09-04T10:15:37-05:00 | HTTP 200 | n_returned=25 | n_total_reported=269
https://api.openalex.org/works?filter=title_and_abstract.search:%22prediction%20market%22%20AND%20%22forecasting%22%20AND%20%22trading%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-09 | executed 2026-09-04T10:36:51-05:00 | HTTP 200 | n_returned=25 | n_total_reported=434
https://api.openalex.org/works?filter=title_and_abstract.search:%22weather%20derivative%22%20AND%20%22hedging%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-10 | executed 2026-09-04T10:36:56-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://api.openalex.org/works?filter=title_and_abstract.search:%22economic%20derivatives%22%20AND%20%22arbitrage%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-11 | executed 2026-09-04T10:37:01-05:00 | HTTP 200 | n_returned=11 | n_total_reported=11
https://api.openalex.org/works?filter=title_and_abstract.search:%22macroeconomic%20derivatives%22%20AND%20%22forecast%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-12 | executed 2026-09-04T10:37:05-05:00 | HTTP 200 | n_returned=17 | n_total_reported=17
https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20AND%20%22hedging%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-13 | executed 2026-09-04T10:37:09-05:00 | HTTP 200 | n_returned=5 | n_total_reported=5
https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20AND%20%22inventory%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
# ks-openalex-14 | executed 2026-09-04T10:37:14-05:00 | HTTP 200 | n_returned=2 | n_total_reported=2
https://api.openalex.org/works?filter=title_and_abstract.search:%22sportsbook%22%20AND%20%22market%20making%22&per-page=25&mailto=238704148%2Bs-koirala%40users.noreply.github.com
```

```text ks-arxiv
# ks-arxiv-01 | executed 2026-09-04T10:15:41-05:00 | HTTP 200 | n_returned=1 | n_total_reported=1
https://export.arxiv.org/api/query?search_query=abs:%22event%20contract%22%20AND%20abs:%22market%20making%22&max_results=50
# ks-arxiv-02 | executed 2026-09-04T10:15:44-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://export.arxiv.org/api/query?search_query=abs:%22Kalshi%22%20AND%20abs:%22arbitrage%22&max_results=50
# ks-arxiv-03 | executed 2026-09-04T10:16:03-05:00 | HTTP 200 | n_returned=50 | n_total_reported=69
https://export.arxiv.org/api/query?search_query=abs:%22prediction%20market%22%20AND%20abs:%22forecasting%22&max_results=50
# ks-arxiv-04 | executed 2026-09-04T10:16:07-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://export.arxiv.org/api/query?search_query=abs:%22event%20contract%22%20AND%20abs:%22hedging%22&max_results=50
# ks-arxiv-05 | executed 2026-09-04T10:16:11-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://export.arxiv.org/api/query?search_query=abs:%22event%20contract%22%20AND%20abs:%22inventory%22&max_results=50
# ks-arxiv-06 | executed 2026-09-04T10:16:15-05:00 | HTTP 200 | n_returned=2 | n_total_reported=2
https://export.arxiv.org/api/query?search_query=abs:%22betting%20exchange%22%20AND%20abs:%22execution%22&max_results=50
# ks-arxiv-07 | executed 2026-09-04T10:16:19-05:00 | HTTP 200 | n_returned=7 | n_total_reported=7
https://export.arxiv.org/api/query?search_query=abs:%22Polymarket%22%20AND%20abs:%22arbitrage%22&max_results=50
# ks-arxiv-08 | executed 2026-09-04T10:16:22-05:00 | HTTP 200 | n_returned=1 | n_total_reported=1
https://export.arxiv.org/api/query?search_query=abs:%22sports%20betting%22%20AND%20abs:%22mispricing%22&max_results=50
# ks-arxiv-09 | executed 2026-09-04T10:37:18-05:00 | HTTP 200 | n_returned=3 | n_total_reported=3
https://export.arxiv.org/api/query?search_query=abs:%22weather%20derivative%22%20AND%20abs:%22hedging%22&max_results=50
# ks-arxiv-10 | executed 2026-09-04T10:37:23-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://export.arxiv.org/api/query?search_query=abs:%22economic%20derivatives%22%20AND%20abs:%22arbitrage%22&max_results=50
# ks-arxiv-11 | executed 2026-09-04T10:37:27-05:00 | HTTP 200 | n_returned=2 | n_total_reported=2
https://export.arxiv.org/api/query?search_query=abs:%22Kalshi%22%20AND%20abs:%22market%20making%22&max_results=50
# ks-arxiv-12 | executed 2026-09-04T10:37:31-05:00 | HTTP 200 | n_returned=0 | n_total_reported=0
https://export.arxiv.org/api/query?search_query=abs:%22binary%20contract%22%20AND%20abs:%22spread%22&max_results=50
# ks-arxiv-13 | executed 2026-09-04T10:37:35-05:00 | HTTP 200 | n_returned=4 | n_total_reported=4
https://export.arxiv.org/api/query?search_query=abs:%22prediction%20market%22%20AND%20abs:%22trading%20agent%22&max_results=50
```

```text ks-s2
# ks-s2-01 | executed 2026-09-04T10:16:26-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-b | executed 2026-09-04T10:16:46-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-c | executed 2026-09-04T10:17:26-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-d | executed 2026-09-04T10:18:41-05:00 | HTTP 500 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-e | executed 2026-09-04T10:33:29-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-f | executed 2026-09-04T10:34:14-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-g | executed 2026-09-04T10:35:14-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-h | executed 2026-09-04T10:36:44-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-i | executed 2026-09-04T10:38:44-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-j | executed 2026-09-04T10:41:14-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-01-k | executed 2026-09-04T10:44:15-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=Kalshi%20event%20contract%20market%20making&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02 | executed 2026-09-04T10:19:07-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-b | executed 2026-09-04T10:19:27-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-c | executed 2026-09-04T10:20:07-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-d | executed 2026-09-04T10:21:22-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-e | executed 2026-09-04T10:44:45-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-f | executed 2026-09-04T10:45:30-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-g | executed 2026-09-04T10:46:30-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-h | executed 2026-09-04T10:48:00-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-02-i | executed 2026-09-04T10:50:01-05:00 | HTTP 200 | n_returned=50 | n_total_reported=65
https://api.semanticscholar.org/graph/v1/paper/search?query=sportsbook%20betting%20exchange%20arbitrage%20event%20contract&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03 | executed 2026-09-04T10:21:26-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-b | executed 2026-09-04T10:21:46-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-c | executed 2026-09-04T10:22:27-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-d | executed 2026-09-04T10:23:42-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-e | executed 2026-09-04T10:50:34-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-f | executed 2026-09-04T10:51:19-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-g | executed 2026-09-04T10:52:19-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-h | executed 2026-09-04T10:53:49-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-i | executed 2026-09-04T10:55:50-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-j | executed 2026-09-04T10:58:20-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-03-k | executed 2026-09-04T11:01:20-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04 | executed 2026-09-04T10:23:46-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-b | executed 2026-09-04T10:24:06-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-c | executed 2026-09-04T10:24:46-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-d | executed 2026-09-04T10:26:01-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-e | executed 2026-09-04T11:01:50-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-f | executed 2026-09-04T11:02:35-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-g | executed 2026-09-04T11:03:35-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-h | executed 2026-09-04T11:05:05-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-i | executed 2026-09-04T11:07:06-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-j | executed 2026-09-04T11:09:36-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-04-k | executed 2026-09-04T11:12:36-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=macroeconomic%20announcement%20event%20contract%20prediction%20market%20mispricing&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05 | executed 2026-09-04T10:26:06-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-b | executed 2026-09-04T10:26:26-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-c | executed 2026-09-04T10:27:06-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-d | executed 2026-09-04T10:28:21-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-e | executed 2026-09-04T11:13:06-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-f | executed 2026-09-04T11:13:51-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-g | executed 2026-09-04T11:14:51-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-h | executed 2026-09-04T11:16:22-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-i | executed 2026-09-04T11:18:22-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-j | executed 2026-09-04T11:20:52-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-05-k | executed 2026-09-04T11:23:52-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=language%20model%20agent%20prediction%20market%20forecasting%20trading&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-06 | executed 2026-09-04T10:28:25-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=regulated%20exchange%20binary%20event%20contract%20collateral%20capital%20efficiency%20spread&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-06-b | executed 2026-09-04T10:28:45-05:00 | HTTP 429 | n_returned=0 | n_total_reported=None
https://api.semanticscholar.org/graph/v1/paper/search?query=regulated%20exchange%20binary%20event%20contract%20collateral%20capital%20efficiency%20spread&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
# ks-s2-06-c | executed 2026-09-04T10:29:25-05:00 | HTTP 200 | n_returned=1 | n_total_reported=1
https://api.semanticscholar.org/graph/v1/paper/search?query=regulated%20exchange%20binary%20event%20contract%20collateral%20capital%20efficiency%20spread&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50
```

```text ks-repec
# CORRECTION 2026-09-04 (round-1 audit; LITERATURE-1-2, REPRODUCIBILITY-1-2). Each
# comment line below previously read "executed <ts> | HTTP 200 | n_returned=0",
# which presents an unexecuted query as executed and defeats the PRISMA-S item 8
# ground that strategies are copied and pasted exactly as run. Struck. The URLs are
# unchanged and remain verbatim as issued; the annotations now carry each log's own
# n_returned_semantics. See DI-8, G-26.
# ks-repec-01 | attempted 2026-09-04T10:29:30-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://ideas.repec.org/cgi-bin/htsearch?q=Kalshi+event+contract+market+making
# ks-repec-01-b | attempted 2026-09-04T11:23:52-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://ideas.repec.org/cgi-bin/htsearch?q=Kalshi+event+contract+market+making&cmd=Search%21&form=extended&wm=wrd&wf=4BFF&s=R
# ks-repec-01-c | attempted 2026-09-04T11:24:06-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://econpapers.repec.org/scripts/search.pf?ft=Kalshi+event+contract+market+making&adv=true&wp=on&art=on&bkchp=on&soft=on
# ks-repec-02 | attempted 2026-09-04T10:29:42-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://ideas.repec.org/cgi-bin/htsearch?q=sportsbook+betting+exchange+arbitrage+event+contract
# ks-repec-02-b | attempted 2026-09-04T11:24:26-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://econpapers.repec.org/scripts/search.pf?ft=sportsbook+betting+exchange+arbitrage+event+contract&adv=true&wp=on&art=on&bkchp=on&soft=on
# ks-repec-03 | attempted 2026-09-04T10:29:55-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://ideas.repec.org/cgi-bin/htsearch?q=macroeconomic+event+contract+prediction+market+hedging
# ks-repec-03-b | attempted 2026-09-04T11:24:42-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://econpapers.repec.org/scripts/search.pf?ft=macroeconomic+event+contract+prediction+market+hedging&adv=true&wp=on&art=on&bkchp=on&soft=on
# ks-repec-04 | attempted 2026-09-04T10:30:08-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://ideas.repec.org/cgi-bin/htsearch?q=weather+event+contract+temperature+hedging+prediction+market
# ks-repec-04-b | attempted 2026-09-04T11:25:09-05:00 (log field executed_at) | HTTP 200 | n_returned=0 | n_total_reported=None | n_returned_semantics="no search executed; not an observed zero-yield" | platform_interface_failure: body is the IDEAS/RePEc search FORM, not a result set
https://econpapers.repec.org/scripts/search.pf?ft=weather+event+contract+temperature+hedging+prediction+market&adv=true&wp=on&art=on&bkchp=on&soft=on
```

```text ks-ssrn
# ks-ssrn-01 | executed 2026-09-04T10:30:21-05:00 | HTTP 403 | n_returned=0 | n_total_reported=None
https://papers.ssrn.com/sol3/results.cfm?txtKey_Words=Kalshi+event+contract+arbitrage
```

```text ks-gh
# ks-gh-01 | executed 2026-09-04T15:10:27+00:00 | HTTP 200 | n_returned=50 | n_total_reported=928 | request_url=https://api.github.com/search/repositories?q=kalshi%20trading&per_page=50
kalshi trading
# ks-gh-02 | executed 2026-09-04T15:10:36+00:00 | HTTP 200 | n_returned=50 | n_total_reported=881 | request_url=https://api.github.com/search/repositories?q=kalshi%20bot&per_page=50
kalshi bot
# ks-gh-03 | executed 2026-09-04T15:10:44+00:00 | HTTP 200 | n_returned=50 | n_total_reported=381 | request_url=https://api.github.com/search/repositories?q=kalshi%20arbitrage&per_page=50
kalshi arbitrage
# ks-gh-04 | executed 2026-09-04T15:10:52+00:00 | HTTP 200 | n_returned=31 | n_total_reported=31 | request_url=https://api.github.com/search/repositories?q=kalshi%20market%20maker&per_page=50
kalshi market maker
# ks-gh-05 | executed 2026-09-04T15:11:01+00:00 | HTTP 200 | n_returned=50 | n_total_reported=71 | request_url=https://api.github.com/search/repositories?q=kalshi%20backtest&per_page=50
kalshi backtest
# ks-gh-06 | executed 2026-09-04T15:11:09+00:00 | HTTP 200 | n_returned=50 | n_total_reported=56 | request_url=https://api.github.com/search/repositories?q=kalshi%20client&per_page=50
kalshi client
# ks-gh-07 | executed 2026-09-04T15:11:17+00:00 | HTTP 200 | n_returned=35 | n_total_reported=35 | request_url=https://api.github.com/search/repositories?q=kalshi%20sdk&per_page=50
kalshi sdk
# ks-gh-08 | executed 2026-09-04T15:11:24+00:00 | HTTP 200 | n_returned=3 | n_total_reported=3 | request_url=https://api.github.com/search/repositories?q=kalshi%20data%20capture&per_page=50
kalshi data capture
# ks-gh-09 | executed 2026-09-04T15:11:32+00:00 | HTTP 200 | n_returned=50 | n_total_reported=124 | request_url=https://api.github.com/search/repositories?q=kalshi%20scanner&per_page=50
kalshi scanner
# ks-gh-10 | executed 2026-09-04T15:11:40+00:00 | HTTP 200 | n_returned=50 | n_total_reported=77 | request_url=https://api.github.com/search/repositories?q=kalshi%20api%20trading&per_page=50
kalshi api trading
# ks-gh-11 | executed 2026-09-04T15:11:48+00:00 | HTTP 200 | n_returned=50 | n_total_reported=1025 | request_url=https://api.github.com/search/repositories?q=polymarket%20arbitrage&per_page=50
polymarket arbitrage
# ks-gh-12 | executed 2026-09-04T15:11:56+00:00 | HTTP 200 | n_returned=50 | n_total_reported=4075 | request_url=https://api.github.com/search/repositories?q=polymarket%20bot&per_page=50
polymarket bot
# ks-gh-13 | executed 2026-09-04T15:12:04+00:00 | HTTP 200 | n_returned=50 | n_total_reported=103 | request_url=https://api.github.com/search/repositories?q=polymarket%20market%20maker&per_page=50
polymarket market maker
# ks-gh-14 | executed 2026-09-04T15:12:12+00:00 | HTTP 200 | n_returned=16 | n_total_reported=16 | request_url=https://api.github.com/search/repositories?q=predictit%20trading&per_page=50
predictit trading
# ks-gh-15 | executed 2026-09-04T15:12:20+00:00 | HTTP 200 | n_returned=50 | n_total_reported=541 | request_url=https://api.github.com/search/repositories?q=prediction%20market%20arbitrage&per_page=50
prediction market arbitrage
# ks-gh-16 | executed 2026-09-04T15:12:28+00:00 | HTTP 200 | n_returned=50 | n_total_reported=322 | request_url=https://api.github.com/search/repositories?q=prediction%20market%20backtest&per_page=50
prediction market backtest
# ks-gh-17 | executed 2026-09-04T15:12:36+00:00 | HTTP 200 | n_returned=50 | n_total_reported=111 | request_url=https://api.github.com/search/repositories?q=event%20contract%20trading&per_page=50
event contract trading
# ks-gh-18 | executed 2026-09-04T15:12:44+00:00 | HTTP 200 | n_returned=32 | n_total_reported=32 | request_url=https://api.github.com/search/repositories?q=manifold%20markets%20bot&per_page=50
manifold markets bot
# ks-gh-19 | executed 2026-09-04T15:12:51+00:00 | HTTP 200 | n_returned=15 | n_total_reported=15 | request_url=https://api.github.com/search/repositories?q=betfair%20arbitrage&per_page=50
betfair arbitrage
# ks-gh-20 | executed 2026-09-04T15:12:59+00:00 | HTTP 200 | n_returned=50 | n_total_reported=109 | request_url=https://api.github.com/search/repositories?q=prediction%20market%20market%20maker&per_page=50
prediction market market maker
```

```text ks-ghcode
# ks-ghcode-01 | executed 2026-09-04T15:13:37+00:00 | HTTP 401 | n_returned=0 | n_total_reported=None | request_url=https://api.github.com/search/code?q=kalshi%20arbitrage&per_page=50
kalshi arbitrage
# ks-ghcode-02 | executed 2026-09-04T15:13:37+00:00 | HTTP 401 | n_returned=0 | n_total_reported=None | request_url=https://api.github.com/search/code?q=kalshi%20market%20maker&per_page=50
kalshi market maker
```

```text ks-gl
# ks-gl-01 | executed 2026-09-04T15:13:38+00:00 | HTTP 200 | n_returned=3 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=kalshi%20trading&per_page=50&order_by=id&sort=desc
kalshi trading
# ks-gl-02 | executed 2026-09-04T15:13:39+00:00 | HTTP 200 | n_returned=3 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=kalshi%20bot&per_page=50&order_by=id&sort=desc
kalshi bot
# ks-gl-03 | executed 2026-09-04T15:13:41+00:00 | HTTP 200 | n_returned=1 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=kalshi%20arbitrage&per_page=50&order_by=id&sort=desc
kalshi arbitrage
# ks-gl-04 | executed 2026-09-04T15:13:42+00:00 | HTTP 200 | n_returned=0 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=kalshi%20client&per_page=50&order_by=id&sort=desc
kalshi client
# ks-gl-05 | executed 2026-09-04T15:13:44+00:00 | HTTP 200 | n_returned=2 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=polymarket%20arbitrage&per_page=50&order_by=id&sort=desc
polymarket arbitrage
# ks-gl-06 | executed 2026-09-04T15:13:46+00:00 | HTTP 200 | n_returned=14 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=polymarket%20bot&per_page=50&order_by=id&sort=desc
polymarket bot
# ks-gl-07 | executed 2026-09-04T15:13:48+00:00 | HTTP 200 | n_returned=1 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=prediction%20market%20arbitrage&per_page=50&order_by=id&sort=desc
prediction market arbitrage
# ks-gl-08 | executed 2026-09-04T15:13:51+00:00 | HTTP 200 | n_returned=2 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=prediction%20market%20backtest&per_page=50&order_by=id&sort=desc
prediction market backtest
# ks-gl-09 | executed 2026-09-04T15:13:53+00:00 | HTTP 200 | n_returned=0 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=event%20contract%20trading&per_page=50&order_by=id&sort=desc
event contract trading
# ks-gl-10 | executed 2026-09-04T15:13:54+00:00 | HTTP 200 | n_returned=0 | n_total_reported=None | request_url=https://gitlab.com/api/v4/projects?search=betfair%20arbitrage&per_page=50&order_by=id&sort=desc
betfair arbitrage
```

```text ks-pypi
# ks-pypi-01 | executed 2026-09-04T15:13:56+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/kalshi/json
kalshi
# ks-pypi-02 | executed 2026-09-04T15:13:56+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/kalshi-python/json
kalshi-python
# ks-pypi-03 | executed 2026-09-04T15:13:57+00:00 | HTTP 404 | n_returned=0 | n_total_reported=0 | request_url=https://pypi.org/pypi/kalshi-api/json
kalshi-api
# ks-pypi-04 | executed 2026-09-04T15:13:58+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/kalshi-client/json
kalshi-client
# ks-pypi-05 | executed 2026-09-04T15:13:58+00:00 | HTTP 404 | n_returned=0 | n_total_reported=0 | request_url=https://pypi.org/pypi/kalshi-trading/json
kalshi-trading
# ks-pypi-06 | executed 2026-09-04T15:13:59+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/kalshi-sdk/json
kalshi-sdk
# ks-pypi-07 | executed 2026-09-04T15:13:59+00:00 | HTTP 404 | n_returned=0 | n_total_reported=0 | request_url=https://pypi.org/pypi/kalshiclient/json
kalshiclient
# ks-pypi-08 | executed 2026-09-04T15:14:00+00:00 | HTTP 404 | n_returned=0 | n_total_reported=0 | request_url=https://pypi.org/pypi/kalshi-arbitrage/json
kalshi-arbitrage
# ks-pypi-09 | executed 2026-09-04T15:14:01+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/kalshi-bot/json
kalshi-bot
# ks-pypi-10 | executed 2026-09-04T15:14:01+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/py-clob-client/json
py-clob-client
# ks-pypi-11 | executed 2026-09-04T15:14:02+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/polymarket/json
polymarket
# ks-pypi-12 | executed 2026-09-04T15:14:02+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/polymarket-sdk/json
polymarket-sdk
# ks-pypi-13 | executed 2026-09-04T15:14:03+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/predictit/json
predictit
# ks-pypi-14 | executed 2026-09-04T15:14:04+00:00 | HTTP 404 | n_returned=0 | n_total_reported=0 | request_url=https://pypi.org/pypi/prediction-market/json
prediction-market
# ks-pypi-15 | executed 2026-09-04T15:14:04+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/manifoldpy/json
manifoldpy
# ks-pypi-16 | executed 2026-09-04T15:14:05+00:00 | HTTP 200 | n_returned=1 | n_total_reported=1 | request_url=https://pypi.org/pypi/betfairlightweight/json
betfairlightweight
```

```text ks-npm
# ks-npm-01 | executed 2026-09-04T15:14:06+00:00 | HTTP 200 | n_returned=50 | n_total_reported=268249 | request_url=https://registry.npmjs.org/-/v1/search?text=kalshi%20client&size=50
kalshi client
# ks-npm-02 | executed 2026-09-04T15:14:07+00:00 | HTTP 200 | n_returned=50 | n_total_reported=6499 | request_url=https://registry.npmjs.org/-/v1/search?text=kalshi%20trading&size=50
kalshi trading
# ks-npm-03 | executed 2026-09-04T15:14:08+00:00 | HTTP 200 | n_returned=50 | n_total_reported=163312 | request_url=https://registry.npmjs.org/-/v1/search?text=kalshi%20sdk&size=50
kalshi sdk
# ks-npm-04 | executed 2026-09-04T15:14:09+00:00 | HTTP 200 | n_returned=50 | n_total_reported=37149 | request_url=https://registry.npmjs.org/-/v1/search?text=kalshi%20bot&size=50
kalshi bot
# ks-npm-05 | executed 2026-09-04T15:14:11+00:00 | HTTP 200 | n_returned=50 | n_total_reported=163550 | request_url=https://registry.npmjs.org/-/v1/search?text=polymarket%20sdk&size=50
polymarket sdk
# ks-npm-06 | executed 2026-09-04T15:14:17+00:00 | HTTP 200 | n_returned=50 | n_total_reported=6687 | request_url=https://registry.npmjs.org/-/v1/search?text=polymarket%20trading&size=50
polymarket trading
# ks-npm-07 | executed 2026-09-04T15:14:18+00:00 | HTTP 200 | n_returned=50 | n_total_reported=15307 | request_url=https://registry.npmjs.org/-/v1/search?text=prediction%20market%20trading&size=50
prediction market trading
# ks-npm-08 | executed 2026-09-04T15:14:19+00:00 | HTTP 200 | n_returned=50 | n_total_reported=391175 | request_url=https://registry.npmjs.org/-/v1/search?text=event%20contract%20client&size=50
event contract client
```

```text ks-nb
# ks-nb-01 | executed 2026-09-04T15:14:20+00:00 | HTTP 401 | n_returned=0 | n_total_reported=None | request_url=https://www.kaggle.com/api/v1/kernels/list?search=kalshi+trading&pageSize=50
kalshi trading
# ks-nb-02 | executed 2026-09-04T15:14:21+00:00 | HTTP 401 | n_returned=0 | n_total_reported=None | request_url=https://www.kaggle.com/api/v1/kernels/list?search=kalshi+arbitrage&pageSize=50
kalshi arbitrage
# ks-nb-03 | executed 2026-09-04T15:14:22+00:00 | HTTP 401 | n_returned=0 | n_total_reported=None | request_url=https://www.kaggle.com/api/v1/kernels/list?search=prediction+market+backtest&pageSize=50
prediction market backtest
```

```text ks-vr-kalshi
# KS-VR-Q01 | executed 2026-09-04T15:09:11+00:00 | HTTP 200 | n_returned=0 | endpoint=kalshi.com venue site: rulebook page
https://kalshi.com/regulatory/rulebook
# KS-VR-Q01b | executed 2026-09-04T15:12:16+00:00 | HTTP 200 | n_returned=0 | endpoint=kalshi.com rulebook page, React Server Component payload (header RSC: 1)
https://kalshi.com/regulatory/rulebook
# KS-VR-Q02 | executed 2026-09-04T15:11:04+00:00 | HTTP 404 | n_returned=0 | endpoint=kalshi.com venue site: candidate rulebook PDF path
https://kalshi.com/docs/kalshi-rulebook.pdf
# KS-VR-Q03 | executed 2026-09-04T15:09:13+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: regulatory index
https://kalshi.com/regulatory
# KS-VR-Q04 | executed 2026-09-04T15:09:14+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: sitemap index
https://kalshi.com/sitemap.xml
# KS-VR-Q05 | executed 2026-09-04T15:09:14+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: robots.txt (access conditions)
https://kalshi.com/robots.txt
# KS-VR-Q06 | executed 2026-09-04T15:09:36+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: llms.txt document index
https://kalshi.com/llms.txt
# KS-VR-Q07 | executed 2026-09-04T15:09:37+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: AGENTS.md
https://kalshi.com/AGENTS.md
# KS-VR-Q08 | executed 2026-09-04T15:09:37+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: markdown sitemap
https://kalshi.com/sitemap.md
# KS-VR-Q09 | executed 2026-09-04T15:10:05+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: fee schedule PDF
https://kalshi.com/docs/kalshi-fee-schedule.pdf
# KS-VR-Q10 | executed 2026-09-04T15:10:06+00:00 | HTTP 404 | n_returned=0 | endpoint=kalshi.com venue site: legal-filings path
https://kalshi.com/docs/legal-filings
# KS-VR-Q11 | executed 2026-09-04T15:10:07+00:00 | HTTP 200 | n_returned=0 | endpoint=kalshi.com venue site: liquidity provider program page
https://kalshi.com/regulatory/liquidity-provider-program
# KS-VR-Q12 | executed 2026-09-04T15:10:08+00:00 | HTTP 200 | n_returned=0 | endpoint=kalshi.com venue site: contract drafts page
https://kalshi.com/regulatory/contract-drafts
# KS-VR-Q13 | executed 2026-09-04T15:10:08+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: member agreement PDF
https://kalshi.com/docs/kalshi-member-agreement.pdf
# KS-VR-Q14 | executed 2026-09-04T15:11:04+00:00 | HTTP 404 | n_returned=0 | endpoint=kalshi.com venue site: candidate rulebook PDF path (retry)
https://kalshi.com/docs/kalshi-rulebook.pdf
# KS-VR-Q15 | executed 2026-09-04T15:11:05+00:00 | HTTP 404 | n_returned=0 | endpoint=assets.kalshi.com: candidate rulebook asset path
https://assets.kalshi.com/documents/rulebook.pdf
# KS-VR-Q16 | executed 2026-09-04T15:11:06+00:00 | HTTP 404 | n_returned=0 | endpoint=kalshi.com venue site: candidate rulebook path
https://kalshi.com/rulebook
# KS-VR-Q17 | executed 2026-09-04T15:11:07+00:00 | HTTP 404 | n_returned=0 | endpoint=kalshi.com venue site: candidate rulebook markdown path
https://kalshi.com/docs/rulebook.md
# KS-VR-Q18 | executed 2026-09-04T15:11:07+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: fee-schedule HTML page
https://kalshi.com/fee-schedule
# KS-VR-Q19 | executed 2026-09-04T15:11:08+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com venue site: API overview markdown
https://kalshi.com/docs/api.md
# KS-VR-Q28 | executed 2026-09-04T15:16:07+00:00 | HTTP 200 | n_returned=1 | endpoint=kalshi.com llms-full.txt (venue machine-readable doc corpus)
https://kalshi.com/llms-full.txt
# KS-VR-Q48 | executed 2026-09-04T15:18:17+00:00 | HTTP 200 | n_returned=0 | endpoint=kalshi.com regulatory notices page
https://kalshi.com/regulatory/notices
```

```text ks-vr-docskalshi
# KS-VR-Q21b | executed 2026-09-04T15:11:26+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com developer portal: welcome
https://docs.kalshi.com/welcome
# KS-VR-Q22b | executed 2026-09-04T15:11:29+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com developer portal: llms.txt document index
https://docs.kalshi.com/llms.txt
# KS-VR-Q23b | executed 2026-09-04T15:11:30+00:00 | HTTP 404 | n_returned=0 | endpoint=docs.kalshi.com: candidate rate-limits path
https://docs.kalshi.com/getting-started/rate-limits
# KS-VR-Q24b | executed 2026-09-04T15:11:52+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: rate limits and tiers
https://docs.kalshi.com/getting_started/rate_limits.md
# KS-VR-Q25b | executed 2026-09-04T15:11:52+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: market settlement
https://docs.kalshi.com/getting_started/market_settlement.md
# KS-VR-Q26b | executed 2026-09-04T15:11:53+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: fee rounding
https://docs.kalshi.com/getting_started/fee_rounding.md
# KS-VR-Q27b | executed 2026-09-04T15:11:53+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: order groups
https://docs.kalshi.com/getting_started/order_groups.md
# KS-VR-Q28b | executed 2026-09-04T15:11:54+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: maintenance and pauses
https://docs.kalshi.com/getting_started/maintenance_and_pauses.md
# KS-VR-Q29b | executed 2026-09-04T15:11:55+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.kalshi.com: market lifecycle
https://docs.kalshi.com/getting_started/market_lifecycle.md
```

```text ks-vr-cftc
# KS-VR-Q20 | executed 2026-09-04T15:13:36+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov Industry Filings: DCM organization search
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations?keys=Kalshi&Show_All=1
# KS-VR-Q21 | executed 2026-09-04T15:13:39+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov Rule Amendments index
https://www.cftc.gov/IndustryOversight/RuleAmendments/index.htm
# KS-VR-Q22 | executed 2026-09-04T15:14:02+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM organization record (Kalshi, id 42993)
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations/42993
# KS-VR-Q23 | executed 2026-09-04T15:14:22+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov filings document (Kalshi Exhibit M rulebook, 2024-07-09 filing)
https://www.cftc.gov/filings/documents/2024/orgdcmkexkalshiexhm240709.pdf
# KS-VR-Q24 | executed 2026-09-04T15:14:23+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov filings document (Kalshi Amended Order of Designation)
https://www.cftc.gov/filings/documents/2025/orgdcmkexkalshiamord250117.pdf
# KS-VR-Q25 | executed 2026-09-04T15:14:24+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov filings document (KalshiEX LLC Designation Order 2020)
https://www.cftc.gov/filings/documents/2020/orgkexkalshidesignation201103.pdf
# KS-VR-Q26 | executed 2026-09-04T15:15:06+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov filings document (Exhibit M - Kalshi Rulebook Nov. 2023)
https://www.cftc.gov/filings/documents/2023/orgkexkalshiexhibitm231130.pdf
# KS-VR-Q27 | executed 2026-09-04T15:15:08+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov filings document (Exhibit M - KalshiEX LLC Rulebook redacted, 2020)
https://www.cftc.gov/filings/documents/2020/orgkexexhibitmrulebook200114.pdf
# KS-VR-Q29 | executed 2026-09-04T15:16:08+00:00 | HTTP 404 | n_returned=0 | endpoint=cftc.gov Industry Filings: Products/Contracts search for Kalshi
https://www.cftc.gov/IndustryOversight/IndustryFilings/ContractsProducts?keys=Kalshi&Show_All=1
# KS-VR-Q30 | executed 2026-09-04T15:16:29+00:00 | HTTP 200 | n_returned=13 | endpoint=cftc.gov Industry Filings: DCM Product filings, keyword Kalshi
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationProducts?keys=Kalshi&Show_All=1
# KS-VR-Q31 | executed 2026-09-04T15:16:35+00:00 | HTTP 200 | n_returned=13 | endpoint=cftc.gov Industry Filings: DCM Rule filings, keyword Kalshi
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules?keys=Kalshi&Show_All=1
# KS-VR-Q32 | executed 2026-09-04T15:16:55+00:00 | HTTP 200 | n_returned=111 | endpoint=cftc.gov Industry Filings: DCM Rule filings, keyword KEX (Kalshi exchange code)
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules?keys=KEX&Show_All=1
# KS-VR-Q33 | executed 2026-09-04T15:17:15+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 60688
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/60688
# KS-VR-Q34 | executed 2026-09-04T15:17:17+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 50281
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/50281
# KS-VR-Q35 | executed 2026-09-04T15:17:20+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 54071
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/54071
# KS-VR-Q36 | executed 2026-09-04T15:17:22+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 61617
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/61617
# KS-VR-Q37 | executed 2026-09-04T15:17:24+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 55868
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/55868
# KS-VR-Q38 | executed 2026-09-04T15:17:36+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules0504262797.pdf
# KS-VR-Q39 | executed 2026-09-04T15:17:37+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules0504262798.pdf
# KS-VR-Q40 | executed 2026-09-04T15:17:39+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rule022123kexdcm001.pdf
# KS-VR-Q41 | executed 2026-09-04T15:17:41+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rule022123kexdcm002.pdf
# KS-VR-Q42 | executed 2026-09-04T15:17:42+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules1114248725.pdf
# KS-VR-Q43 | executed 2026-09-04T15:17:44+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules1114248723.pdf
# KS-VR-Q44 | executed 2026-09-04T15:17:46+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules0712269458.pdf
# KS-VR-Q45 | executed 2026-09-04T15:17:47+00:00 | HTTP 200 | n_returned=0 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules04212519493.pdf
# KS-VR-Q46 | executed 2026-09-04T15:17:49+00:00 | HTTP 200 | n_returned=0 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules04212519494.pdf
# KS-VR-Q47 | executed 2026-09-04T15:17:50+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document
https://www.cftc.gov/filings/orgrules/rules04212519496.pdf
# KS-VR-Q49 | executed 2026-09-04T15:18:48+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document (LP Program 60688)
https://www.cftc.gov/filings/orgrules/rules0518263591.pdf
# KS-VR-Q50 | executed 2026-09-04T15:18:50+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document (LP Program 60688)
https://www.cftc.gov/filings/orgrules/rules0518263592.pdf
# KS-VR-Q53 | executed 2026-09-04T15:19:19+00:00 | HTTP 404 | n_returned=0 | endpoint=cftc.gov site search (solr) keyword Kalshi
https://www.cftc.gov/search/node?keys=Kalshi
# KS-VR-Q54 | executed 2026-09-04T15:19:57+00:00 | HTTP 200 | n_returned=0 | endpoint=cftc.gov Industry Filings: Commission Orders and Other Actions, keyword Kalshi
https://www.cftc.gov/IndustryOversight/IndustryFilings/CommissionOrdersandOtherActions?keys=Kalshi&Show_All=1
# KS-VR-Q55 | executed 2026-09-04T15:19:59+00:00 | HTTP 200 | n_returned=8 | endpoint=cftc.gov PressRoom press releases listing, keyword Kalshi
https://www.cftc.gov/PressRoom/PressReleases?combine=Kalshi
# KS-VR-Q56 | executed 2026-09-04T15:20:15+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov press release 9267-26
https://www.cftc.gov/PressRoom/PressReleases/9267-26
# KS-VR-Q57 | executed 2026-09-04T15:20:30+00:00 | HTTP 200 | n_returned=36 | endpoint=cftc.gov Industry Filings: full DCM list (Show_All) to identify peer event-contract venues
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations?Show_All=1
# KS-VR-Q72 | executed 2026-09-04T15:22:04+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM product filing record 63548 (Kalshi Weather Index SF Bay Area)
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationProducts/63548
# KS-VR-Q73 | executed 2026-09-04T15:22:11+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov product-term-certification document
https://www.cftc.gov/filings/ptc/ptc09012622855.pdf
# KS-VR-Q74 | executed 2026-09-04T15:22:13+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov product-term-certification document
https://www.cftc.gov/filings/ptc/ptc09012622854.pdf
# KS-VR-Q75 | executed 2026-09-04T15:22:48+00:00 | HTTP 200 | n_returned=0 | endpoint=cftc.gov DCM rule filing record 60455 (Rulebook changes, Apr 2026)
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/60455
# KS-VR-Q76 | executed 2026-09-04T15:23:01+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov DCM rule filing record 61508 (Block Trade Thresholds, non-sports)
https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizationRules/61508
# KS-VR-Q77 | executed 2026-09-04T15:23:03+00:00 | HTTP 200 | n_returned=1 | endpoint=cftc.gov orgrules filing document (block trade thresholds)
https://www.cftc.gov/filings/orgrules/rules0701268684.pdf
```

```text ks-vr-ecfr
# KS-VR-Q51 | executed 2026-09-04T15:19:16+00:00 | HTTP 200 | n_returned=1 | endpoint=ecfr.gov API: 17 CFR Part 40 (provisions common to registered entities)
https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-17?part=40
```

```text ks-vr-fedreg
# KS-VR-Q52 | executed 2026-09-04T15:19:18+00:00 | HTTP 200 | n_returned=5 | endpoint=federalregister.gov API: documents mentioning Kalshi
https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=Kalshi&per_page=40&order=newest&fields%5B%5D=title&fields%5B%5D=publication_date&fields%5B%5D=document_number&fields%5B%5D=type&fields%5B%5D=html_url&fields%5B%5D=agencies
```

```text ks-vr-polymarketus
# KS-VR-Q58 | executed 2026-09-04T15:20:46+00:00 | HTTP 200 | n_returned=1 | endpoint=polymarket.us venue rulebook probe
https://polymarket.us/rulebook
# KS-VR-Q63 | executed 2026-09-04T15:21:14+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.us machine index
https://docs.polymarket.us/llms.txt
# KS-VR-Q68 | executed 2026-09-04T15:21:35+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.us fee schedule
https://docs.polymarket.us/fees.md
# KS-VR-Q69 | executed 2026-09-04T15:21:36+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.us API rate limits
https://docs.polymarket.us/api-reference/rate-limits.md
# KS-VR-Q70 | executed 2026-09-04T15:21:38+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.us market maker program
https://docs.polymarket.us/incentives/market-maker.md
# KS-VR-Q71 | executed 2026-09-04T15:21:39+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.us trading restrictions
https://docs.polymarket.us/learn/trading/access-and-limits/trading-restrictions.md
```

```text ks-vr-polymarket
# KS-VR-Q59 | executed 2026-09-04T15:20:48+00:00 | HTTP 404 | n_returned=0 | endpoint=polymarket.com rulebook probe
https://polymarket.com/rulebook
# KS-VR-Q60 | executed 2026-09-04T15:20:51+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.com machine index
https://docs.polymarket.com/llms.txt
# KS-VR-Q64 | executed 2026-09-04T15:21:15+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.com fees document
https://docs.polymarket.com/trading/fees.md
# KS-VR-Q65 | executed 2026-09-04T15:21:16+00:00 | HTTP 200 | n_returned=1 | endpoint=docs.polymarket.com resolution document
https://docs.polymarket.com/concepts/resolution.md
```

```text ks-vr-othervenues
# KS-VR-Q61 | executed 2026-09-04T15:20:52+00:00 | HTTP 200 | n_returned=0 | endpoint=predictit.org rules page
https://www.predictit.org/support/rules
# KS-VR-Q62 | executed 2026-09-04T15:20:54+00:00 | HTTP 403 | n_returned=0 | endpoint=cmegroup event contracts landing
https://www.cmegroup.com/markets/event-contracts.html
# KS-VR-Q66 | executed 2026-09-04T15:21:17+00:00 | HTTP 403 | n_returned=0 | endpoint=betfair.com charges page
https://www.betfair.com/aboutUs/Betfair.Charges/
# KS-VR-Q67 | executed 2026-09-04T15:21:18+00:00 | HTTP 403 | n_returned=0 | endpoint=cmegroup robots
https://www.cmegroup.com/robots.txt
```

```text ks-lateral
# KSL-Q01 | kind=search | seed=1 | executed 2026-09-04T10:09:30-05:00 | HTTP None | n_returned=10
Kalshi strike ladder prices sum to more than 100 arbitrage event contracts
# KSL-Q02 | kind=search | seed=1 | executed 2026-09-04T10:09:30-05:00 | HTTP None | n_returned=10
Kalshi mutually exclusive market "sum of yes" prices arbitrage guaranteed profit
# KSL-Q03 | kind=search | seed=2 | executed 2026-09-04T10:09:30-05:00 | HTTP None | n_returned=10
Polymarket negative risk converter multi-outcome basket arbitrage
# KSL-Q04 | kind=search | seed=3 | executed 2026-09-04T10:09:30-05:00 | HTTP None | n_returned=7
Kalshi fed funds futures basis trade event contracts CME arbitrage
# KSL-Q05 | kind=search | seed=4 | executed 2026-09-04T10:09:48-05:00 | HTTP None | n_returned=7
Kalshi settlement source revision ambiguous resolution rule edge case trader dispute event contract
# KSL-Q06 | kind=search | seed=5 | executed 2026-09-04T10:09:48-05:00 | HTTP None | n_returned=10
Kalshi latency CPI release data scraping speed advantage event contract trading
# KSL-Q07 | kind=search | seed=6 | executed 2026-09-04T10:09:48-05:00 | HTTP None | n_returned=10
Kalshi maker fee rebate zero taker fee structure exploit market maker event contracts
# KSL-Q08 | kind=search | seed=7 | executed 2026-09-04T10:09:48-05:00 | HTTP None | n_returned=10
Kalshi market maker program liquidity provider incentive rebate apply
# KSL-Q09 | kind=search | seed=8 | executed 2026-09-04T10:10:02-05:00 | HTTP None | n_returned=10
Kalshi capital efficiency fully collateralized binary contract netting offsetting positions margin release
# KSL-Q10 | kind=search | seed=9 | executed 2026-09-04T10:10:02-05:00 | HTTP None | n_returned=10
Kalshi 1256 contract tax treatment 60/40 event contracts trader executability
# KSL-Q11 | kind=search | seed=10 | executed 2026-09-04T10:10:02-05:00 | HTTP None | n_returned=10
LLM agent forecaster trading Kalshi prediction market bot model-driven
# KSL-Q12 | kind=search | seed=3 | executed 2026-09-04T10:10:02-05:00 | HTTP None | n_returned=7
Kalshi weather contracts NWS model NBM ensemble forecast edge trading temperature
# KSL-Q13 | kind=search | seed=3 | executed 2026-09-04T10:11:40-05:00 | HTTP None | n_returned=8
Kalshi sportsbook line arbitrage vig-free implied probability event contract vs sportsbook price
# KSL-Q14 | kind=search | seed=5 | executed 2026-09-04T10:11:40-05:00 | HTTP None | n_returned=6
Kalshi economic data release trading strategy seconds after print BLS embargo repricing
# KSL-Q15 | kind=search | seed=3 | executed 2026-09-04T10:11:40-05:00 | HTTP None | n_returned=10
Kalshi inflation swap breakeven CPI contract hedge basis practitioner
# KSL-Q16 | kind=search | seed=8 | executed 2026-09-04T10:14:06-05:00 | HTTP None | n_returned=10
Kalshi interest on cash balance collateral yield event contracts carry
# KSL-Q17 | kind=search | seed=4 | executed 2026-09-04T10:14:06-05:00 | HTTP None | n_returned=10
Kalshi early settlement market closes before expiration contract settles early strategy
# KSL-Q18 | kind=search | seed=5 | executed 2026-09-04T10:14:06-05:00 | HTTP None | n_returned=9
Kalshi API rate limit tiers order throughput constraint market maker access
# KSL-Q19 | kind=search | seed=6 | executed 2026-09-04T10:14:06-05:00 | HTTP None | n_returned=10
Kalshi self-trade prevention wash trade rule order cancel restriction trading practice
# KSL-Q20 | kind=search | seed=2 | executed 2026-09-04T10:15:28-05:00 | HTTP None | n_returned=10
Kalshi combos multi-leg parlay contract price versus product of individual legs coherence
# KSL-Q21 | kind=search | seed=1 | executed 2026-09-04T10:15:28-05:00 | HTTP None | n_returned=22
Kalshi duplicate market same event two series different tickers price divergence within exchange
# KSL-Q22 | kind=search | seed=7 | executed 2026-09-04T10:15:28-05:00 | HTTP None | n_returned=10
Kalshi order book depth thin market liquidity provision practitioner spread capture inventory writeup
# KSL-R01 | kind=retrieval | seed=1 | executed 2026-09-04T10:10:43-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/kalshi-arbitrage-guide
# KSL-R02 | kind=retrieval | seed=1 | executed 2026-09-04T10:10:45-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.oddsshopper.com/articles/prediction-markets/kalshi-commodity-markets
# KSL-R03 | kind=retrieval | seed=2 | executed 2026-09-04T10:10:46-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://docs.polymarket.com/concepts/negative-risk
# KSL-R04 | kind=retrieval | seed=2 | executed 2026-09-04T10:10:43-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://github.com/Polymarket/neg-risk-ctf-adapter
# KSL-R05 | kind=retrieval | seed=8 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://news.kalshi.com/p/collateral-return
# KSL-R06 | kind=retrieval | seed=4 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://defirate.com/prediction-markets/how-contracts-settle/
# KSL-R07 | kind=retrieval | seed=6 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://whirligigbear.substack.com/p/makertaker-math-on-kalshi
# KSL-R08 | kind=retrieval | seed=6 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://blog.polytrage.com/kalshis-fee-structure-explained/
# KSL-R09 | kind=retrieval | seed=7 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/13823851-liquidity-incentive-program
# KSL-R10 | kind=retrieval | seed=7 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/15410219-liquidity-provider-program
# KSL-R11 | kind=retrieval | seed=7 | executed 2026-09-04T10:10:44-05:00 | HTTP 404 | n_returned=0
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/15410257-combo-incentive-program
# KSL-R12 | kind=retrieval | seed=10 | executed 2026-09-04T10:10:45-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://github.com/OctagonAI/kalshi-trading-bot-cli
# KSL-R13 | kind=retrieval | seed=10 | executed 2026-09-04T10:10:44-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.northlakelabs.com/max/blog/kalshi-weather-postmortem-and-pivot/
# KSL-R14 | kind=retrieval | seed=9 | executed 2026-09-04T10:10:46-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.convoyfinance.com/resources/kalshi-polymarket-taxes-llc-section-1256
# KSL-R15 | kind=retrieval | seed=5 | executed 2026-09-04T10:10:45-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/kalshi-trading-strategies-guide
# KSL-R16 | kind=retrieval | seed=3 | executed 2026-09-04T10:10:45-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://github.com/suislanchez/polymarket-kalshi-weather-bot
# KSL-R17 | kind=retrieval | seed=5 | executed 2026-09-04T10:12:53-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.oddsshopper.com/articles/prediction-markets/kalshi-cpi-inflation-markets
# KSL-R18 | kind=retrieval | seed=3 | executed 2026-09-04T10:12:53-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.oddsshopper.com/articles/prediction-markets/kalshi-economic-markets
# KSL-R19 | kind=retrieval | seed=3 | executed 2026-09-04T10:12:52-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.avo.bet/articles/kalshi-arbitrage-betting
# KSL-R20 | kind=retrieval | seed=3 | executed 2026-09-04T10:12:54-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide
# KSL-R21 | kind=retrieval | seed=6 | executed 2026-09-04T10:12:51-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/13823850-what-is-the-kalshi-volume-incentive-program
# KSL-R22 | kind=retrieval | seed=4 | executed 2026-09-04T10:12:51-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://kalshiview.com/blog/sports-on-kalshi-cftc-regulated-sports-contracts/
# KSL-R23 | kind=retrieval | seed=5 | executed 2026-09-04T10:12:55-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://apidog.com/blog/kalshi-api-devolpers-guide/
# KSL-R24 | kind=retrieval | seed=10 | executed 2026-09-04T10:12:52-05:00 | HTTP 404 | n_returned=0
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://github.com/0mnjb/Kalshi-AI-Trading-Bot
# KSL-R25 | kind=retrieval | seed=10 | executed 2026-09-04T10:12:53-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://github.com/aarora4/Awesome-Prediction-Market-Tools
# KSL-R26 | kind=retrieval | seed=7 | executed 2026-09-04T10:12:53-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://x.com/navnoorquant/article/2088369227283751256
# KSL-R27 | kind=retrieval | seed=5 | executed 2026-09-04T10:12:53-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://kairos.trade/blog/kalshi-trading-strategies
# KSL-R28 | kind=retrieval | seed=3 | executed 2026-09-04T10:12:54-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://news.kalshi.com/p/inflation
# KSL-R29 | kind=retrieval | seed=2 | executed 2026-09-04T10:12:54-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://pkg.go.dev/github.com/ivanzzeth/polymarket-go-gamma-client/examples/find-negrisk-opportunities
# KSL-R30 | kind=retrieval | seed=4 | executed 2026-09-04T10:12:54-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://mdf-law.com/kalshi-payout-disputes-attorney/
# KSL-R31 | kind=retrieval | seed=8 | executed 2026-09-04T10:12:55-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://medium.com/@mgoelzer/kalshi-market-mechanics-9f4bdec45e84
# KSL-R32 | kind=retrieval | seed=1 | executed 2026-09-04T10:12:55-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.predictionhunt.com/blog/kalshi-vs-polymarket-arbitrage
# KSL-R33 | kind=retrieval | seed=8 | executed 2026-09-04T10:14:35-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/13823847-apy-on-kalshi
# KSL-R34 | kind=retrieval | seed=8 | executed 2026-09-04T10:14:36-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://news.kalshi.com/p/interest-cash-open-positions
# KSL-R35 | kind=retrieval | seed=4 | executed 2026-09-04T10:14:35-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://ufoholdings.substack.com/p/i-lost-30k-due-to-kalshis-void-rules
# KSL-R36 | kind=retrieval | seed=4 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://docs.kalshi.com/getting_started/market_lifecycle
# KSL-R37 | kind=retrieval | seed=5 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://docs.kalshi.com/getting_started/rate_limits
# KSL-R38 | kind=retrieval | seed=4 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://docs.kalshi.com/getting_started/market_settlement
# KSL-R39 | kind=retrieval | seed=4 | executed 2026-09-04T10:14:37-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://gamingamerica.com/news/1044225/kalshi-makes-death-rule-official-after-controversial-khamenei-market
# KSL-R40 | kind=retrieval | seed=5 | executed 2026-09-04T10:14:37-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.oddsshopper.com/articles/prediction-markets/kalshi-jobs-report-markets
# KSL-R41 | kind=retrieval | seed=3 | executed 2026-09-04T10:14:37-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/kalshi-weather-trading-strategy
# KSL-R42 | kind=retrieval | seed=5 | executed 2026-09-04T10:14:37-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/kalshi-api-rate-limits
# KSL-R43 | kind=retrieval | seed=3 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.kalshiweatheredge.com/
# KSL-R44 | kind=retrieval | seed=7 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/16076644-liquidity-and-volume-incentive-programs-where-to-find-them
# KSL-R45 | kind=retrieval | seed=10 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem
# KSL-R46 | kind=retrieval | seed=3 | executed 2026-09-04T10:14:39-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://nexusfi.com/a/prediction-markets/weather-event-contracts
# KSL-R47 | kind=retrieval | seed=9 | executed 2026-09-04T10:14:38-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.natptax.com/news-insights/blog/prediction-market-contracts-are-showing-up-on-client-returns/
# KSL-R48 | kind=retrieval | seed=6 | executed 2026-09-04T10:14:39-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://marketmath.io/platforms/kalshi
# KSL-R49 | kind=retrieval | seed=2 | executed 2026-09-04T10:15:57-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.botforkalshi.com/blog/kalshi-parlay-strategy
# KSL-R50 | kind=retrieval | seed=4 | executed 2026-09-04T10:15:59-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.oddsshopper.com/articles/prediction-markets/kalshi-vs-polymarket-settlement-rules
# KSL-R51 | kind=retrieval | seed=7 | executed 2026-09-04T10:15:57-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/13823819-how-to-become-a-market-maker-on-kalshi
# KSL-R52 | kind=retrieval | seed=7 | executed 2026-09-04T10:15:57-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.navnoorbawaresearch.com/p/kalshi-publishes-one-liquidity-subsidy
# KSL-R53 | kind=retrieval | seed=3 | executed 2026-09-04T10:15:57-05:00 | HTTP 403 | n_returned=0
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://www.investing.com/analysis/when-markets-disagree-prediction-odds-and-optionsimplied-probabilities-200685270
# KSL-R54 | kind=retrieval | seed=2 | executed 2026-09-04T10:15:57-05:00 | HTTP 403 | n_returned=0
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://kalshi-parlays.com/combos-guide
# KSL-R55 | kind=retrieval | seed=7 | executed 2026-09-04T10:15:57-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://help.kalshi.com/en/articles/13823822-maker-order-protections
# KSL-R56 | kind=retrieval | seed=5 | executed 2026-09-04T10:15:58-05:00 | HTTP 200 | n_returned=1
curl -sSL --max-time 60 -A '<Chrome/124 UA>' -H 'Accept: text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.9' https://depthfeed.com/resources/kalshi-api-guide
```


<!-- prisma-s-9 -->
**Limits and restrictions.** **No date limit and no language limit were used, in
any arm** — the protocol section 12 conventions register derives both: strategy
statements, preconditions and tooling are not time-bounded in relevance, and a
lower date bound would amputate foundational statements. Field restriction, where
a platform offered it, was applied to **title-and-abstract only, never to full
text**, so behaviour is comparable across platforms; Crossref exposes no combined
title-and-abstract field and `query.bibliographic` was used instead, recorded per
query. **Retrieval caps** were in force and are a cap on retrieval depth, never
an eligibility limit: `rows=20` on Crossref, `per_page=25` on OpenAlex,
`max_results=50` on arXiv, `limit=50` on Semantic Scholar, `per_page=50` on the
code hosts. Total-hit counts are preserved in `n_total_reported` and truncation
is flagged per query — Crossref reported totals in the hundreds of thousands
against a 20-record retrieval, and **the gap between `n_total_reported` and
`n_returned` is the single largest uncharacterised part of this search.** Three
query-construction departures from the frozen text occurred and were adjudicated
before any screening: see section 3.3. **No popularity floor, star count, fork
count, watcher count, recency threshold, licence filter or curation classifier
was applied at any stage** of the software arm; the resulting sampling hazard is
declared in limitation 2 rather than thresholded away.

<!-- prisma-s-10 -->
**Published search filters used: none.** No validated or published search filter
exists for this domain, and none was applied. Applying a clinical filter here
would be an uncited transfer.

<!-- prisma-s-11 -->
**Strategies adapted or reused from a prior review.** The retrieval-cap values
and the deduplication same-work rule are carried, labelled `CONVENTION`, from
`protocol_kalshi-arbitrage-review_2026-09-02.md` sections 3.1 and 4.1, which in
turn carries the caps from `protocol_explosive-regime-review_2026-08-24.md`
section 3.2. The **query strings themselves are new**; the predecessor's
instrument and strategy vocabularies were carried and extended with the venue
name and the sports, weather, macro, cross-venue and regulated-DCM strata.

<!-- prisma-s-12 -->
**Search updating: none, and none is planned within this record.** This is a
single-execution search. Any re-execution is a new dated record, not an update to
this one. The SHA-256 of each retrieved payload is what a re-execution would be
compared against: **a re-retrieval that digests differently is a changed
document, not a confirmation.**

<!-- prisma-s-13 -->
**Date of the last search: 2026-09-04 for every strategy in every arm**, which
agrees with the `date_searched` column above row for row. The execution window
runs, computed over all **336** logged query timestamps normalised to UTC, from
`2026-09-04T15:09:11+00:00` (`KS-VR-Q01`, the venue arm's first probe of the
rulebook page) to `2026-09-04T11:25:09-05:00` = `16:25:09+00:00`
(`ks-repec-04-b`, the last academic retry).

**One post-execution correction to a query log is recorded rather than elided.**
`ks-openalex-02` carries a `note` stating that an earlier draft of its
*annotation* described the query as executed without a strategy conjunct; the
query string in `query_verbatim` is unchanged and is the full section-3.1
conjunction of instrument term and strategy term. The correction was made in the
same session and **before any screening**, the superseded annotation is preserved
in the log, and **no construction-rule departure occurred** — so this is not a
fourth part of M1. That file's modification time (11:28 local) is later than its
`executed_at` (10:15:16-05:00) for that reason, and the execution window above is
computed from `executed_at`, never from a file timestamp.

### 3.3 Amendments M1 and M2, enumerated

Protocol section 10 makes a corpus record that ran under an amendment it does not
enumerate **defective**. TWO amendments exist. M1's three parts are enumerated immediately below and M2 is enumerated at section 3.4. *(Corrected 2026-09-04, round-2 findings CRITICAL-2-1 / SCOPE-2-1 / QUANT-2-1 / LITERATURE-2-1. This sentence previously read "One amendment exists and all three of its parts are enumerated here", which was false and, worse, sat one sentence after this record quotes the very rule it breached. The superseded wording is retained here.)*; the full ruling text is in the front-matter
`protocol_amendments` field and in `ks-amendments.jsonl`.

| part | ruling | frozen text it touches | what was done | queries | traceability tag | records reaching the corpus only this way |
|---|---|---|---|---|---|---|
| **M1(a)** | granted, with the construal narrowed so it cannot travel further | section 3.1, "one **instrument term** drawn from the frozen instrument vocabulary — the terms naming binary event contracts, event derivatives, prediction markets, or the named venues" | `weather derivative`, `economic derivatives` and `macroeconomic derivatives` placed in the instrument slot. Admissible only under condition 1 (the family is itself an **event-derivative** family) or condition 2 (the term names a **section 2.2 counterparty leg**). `economic derivatives` and `macroeconomic derivatives` enter on condition 1; **`weather derivative` enters on condition 2 and NOT on condition 1**, because an HDD/CDD swap is index-linked, not binary | ks-crossref-16, ks-crossref-17, ks-openalex-09, ks-openalex-10, ks-openalex-11, ks-arxiv-09, ks-arxiv-10 | `reached_via: M1a` | 67, **all of them G1** |
| **M1(b)** | granted, narrowly | section 3.1, "one **strategy term** drawn from the frozen strategy vocabulary — arbitrage, coherence, mispricing, market making, quoting, inventory, spread, execution, hedging, forecasting-driven trading" | `abs:"trading agent"` used at ks-arxiv-13. Admissible only because section 3.4's frozen lateral seed list item 10 already names "forecasting-model-driven approaches, including model-agent forecasters" — the grant **aligns the two arms rather than widening the branch** | ks-arxiv-13 | `reached_via: M1b` | 3, **all of them G1** |
| **M1(c)** | granted, as a REACHING device only | section 3.1, "Category or subject narrowing is applied **only** where the unrestricted phrase returns predominantly out-of-domain records … each narrowing is recorded in the query table with the reason" | `query.container-title=SSRN` at ks-crossref-14. A container restriction is neither a category nor a subject narrowing. Admissible **only where it REACHES an otherwise-unreachable source, never where it EXCLUDES**: SSRN's own interface returned HTTP 403 unauthenticated at ks-ssrn-01, so the restriction adds a retrieval path and removes none | ks-crossref-14 | `reached_via: M1c` | 20, **all of them G1** |

**Execution stage, stated in the amendment's own words: PRE-SCREENING.** The
executing agent reported all three departures before assigning any stage-1
disposition, and **no record's eligibility was decided under any departure,
because no record's eligibility was decided at all.** This is **not** the
predecessor branch's A8 position (a frozen criterion relaxed *after* 33 affected
records had been screened, extracted and published) and this record does not
describe it as one. **Who decided:** the lead session, not the executing agent
and not the drafting agent. **What M1 does not touch:** no eligibility criterion
N1-N6 or Y1-Y9, no contribution code, no extraction field, no taxonomy class, no
screening rule, no arithmetic identity. **Withdrawal rule:** a reviewer who
rejects any part may withdraw exactly the records tagged with that part's
`reached_via` value and no others — and since all 90 such records are G1,
**no inclusion in this corpus rests on M1.**

### 3.4 Amendment M2, enumerated

*Added 2026-09-04 by round-2 audit remediation. Findings **CRITICAL-2-1**,
**SCOPE-2-1**, **QUANT-2-1** and **LITERATURE-2-1** — four independent branches —
recorded that this record ran under M2 and did not enumerate it, which protocol
section 10 makes **defective**. M2 was issued during round-1 remediation and
registered correctly in the two registers section 10 names; the third obligation,
enumeration here, was missed.*

**What M2 rules on.** Not query admissibility, as M1 does, but the **disposition
semantics of this record's own flow**. The frozen protocol's section 4.2 states
that every deduplicated record receives exactly ONE stage-1 disposition and
enumerates three — `include`, `exclude` with a Y-code, `promote`. Section 4.4 then
creates the capacity codes `G1` and `G2`, which are none of the three. **1,465 of
the 1,574 records screened in this corpus — 93% of the delivered flow — took the
path the frozen text did not enumerate.**

**The ruling.** A G-code is a **FOURTH stage-1 outcome**. Section 4.2's "exactly
one disposition" is read as conditional on assessment capacity: a record never
assessed receives exactly one disposition, and that disposition is a capacity
code. The arithmetic is untouched — G-rows sit inside `n_excluded` so the section
4.5 identities close, and they are reported decomposed, which is what this record
already does at `n_excluded == Y-rows + G-rows`, **10 + 1,465 = 1,475**.

**M2 IS WEAKER THAN M1, AND THIS RECORD MUST SAY SO RATHER THAN CARRY ONLY M1's
PRE-SCREENING BOAST.** M2 is **POST-EXECUTION**: the 1,465 G-dispositions were
assigned **before** the contradiction was adjudicated. Every part of M1, by
contrast, was decided **pre-screening**, before any record's eligibility was
determined. Protocol section 10 requires that an amendment logged after the
affected decisions were made say so in those words, and that **the corpus record
reports the distinction** — this section is where that obligation is discharged.
The alternative reading M2 forecloses is the damaging one: without it, a reader
reconciling this flow against section 4.2 alone would have to treat G-rows as a
species of `exclude`, which would silently convert **1,465 capacity gaps into
1,465 eligibility determinations** — the precise inference section 4.4 exists to
forbid and the same class of error as **DI-8**.

**What M2 does not touch.** No eligibility criterion `N1`–`N6` or `Y1`–`Y9`. No
contribution code, extraction field, taxonomy class or arithmetic identity. No
record's disposition and no count. Frozen text was not edited; the addendum
supersedes section 4.2's enumeration in place and the original wording stays
legible. The frozen prefix was re-hashed after the append and is byte-identical
to the registration commit. Full text: the protocol's own addendum and
`ks-amendments.jsonl` line 3.

10. **The academic arm's known-item recall against the predecessor corpus is
    4.3%, and that figure is published because it is low.** *(Added 2026-09-04 by
    round-2 audit remediation; findings CRITICAL-2-4, SCOPE-2-4, QUANT-2-3,
    LITERATURE-2-3. The check was executed in round 1 but published only in the
    session declaration, which is the audit loop's INPUT, not a deliverable a
    reader consumes.)* Of the **327** records the predecessor branch
    dispositioned `include`, the academic arm here identified **14**. Full result
    and inputs, each hashed:
    [ks-known-item-recall.json](docs/literature/search_logs/kalshi-strategy-multivocal/ks-known-item-recall.json).
    **Both bounds travel with the number and neither may be dropped.** First, the
    seed set is defensible but **imperfect**: the predecessor asks about
    arbitrage, coherence and market making, this branch asks about **stated
    strategies**, so a predecessor include is not automatically a record this
    branch ought to have retrieved, and a low figure is evidence about
    **vocabulary overlap between two protocols** rather than proof of a missed
    record. Second, the seed inherits the novelty index's own bound — it covers
    6,923 of the predecessor's 8,813 records (limitation 6), so predecessor
    includes carrying no identifier cannot appear in the seed at all. **It is not
    a screening statistic**: recall is measured against records the academic arm
    *identified*, and all 528 of those remain capacity-gap G-rows whose
    eligibility was never assessed. Registered as gap **G-29**.

---

## 4. Peer review of the search strategy

<!-- prisma-s-14 -->
**NOT PEER REVIEWED.** No PRESS 2015 review by an information specialist was
obtained, and none was simulated. Protocol section 3.5 declares this as a
standing limitation of the design rather than as an accident, and PRISMA 2020
item 8's dual-independence requirement is likewise unmet by design (section 13).
What *was* done, and what it is not a substitute for: the methodological
instruments the protocol declares were resolved and checked against primary
sources by a separate `literature-check` session **before the protocol froze**,
whose evidence record — including the verification **depth** of each record and
the declared gap in each proposed use — is
`ks-instrument-verification.json`. That session returned
**`proceed-with-remediation`**, and its own environment gap is carried here as
gap **G-14**: PDF text extraction was unavailable and seven publishers returned
HTTP 403, so instruments 1-5 were verified at **abstract or metadata depth** and
three sub-claims were corroborated only from search-index extraction rather than
from fetched primary text.

---

## 5. Managing records: the unit of account, the flow, and the arithmetic

<!-- prisma-s-15 -->
### 5.1 Records identified per source

The `n_records` column of the section 2 table is the per-source total and it sums
to **`n_identified` = 1,986**. Reconciled by arm:

| arm | source class yielded | records identified | what ONE record IS in this arm |
|---|---|---|---|
| ACADEMIC | S-A, S-B | **650** | one bibliographic row as the index returned it, before deduplication |
| SOFTWARE | S-C | **1,269** | one repository or package row as the host returned it, before deduplication |
| VENUE-AND-REGULATOR | S-D | **30** | one **retrieved document** with a byte digest, which may carry many clauses |
| LATERAL / PRACTITIONER | S-C, S-D, S-E | **37** | one sourced **strategy class** (32) or one candidate class dispositioned `Y3` (5); **two classes may share one retrieved payload** |
| **total** | | **1,986** | |

**THE HARDEST PROBLEM IN THIS RECORD, SOLVED EXPLICITLY AND NOT PAPERED OVER.**
Protocol section 4.5 states its identities over "records", but the four arms
return **heterogeneous units**: bibliographic records, software artifacts,
documents-carrying-clauses, and strategy-classes-carrying-a-source. The
resolution adopted, and declared in the front matter, is:

> **Unit of account = the DISPOSITIONED RECORD** — an object to which this corpus
> assigns an F1 identifier and for which at least one arm log holds the stored
> response that identified it.

Under that definition the identities close, and they close **arithmetically over
identifiers, not over comparable things**. Three consequences are stated rather
than hidden:

1. **The summands are not commensurable.** 1,269 software rows and 37 lateral
   rows are different kinds of object. Their sum is valid inside the identities
   and means nothing outside them. Do not compute a proportion across arms.
2. **The venue arm's 30 is a count of RETRIEVED documents, not of identified
   ones.** The arm additionally *enumerated* objects it did not retrieve: 111 KEX
   rule filings, roughly 90 contract series, 34 further designated contract
   markets. **Those are NOT in `n_identified`**, because no arm log holds a
   per-object stored response for any of them and introducing 235-odd rows the
   logs do not contain would breach this record's hard constraint that no record
   may appear that appears in no arm log. **The flow as published is therefore
   CONDITIONED on that reading**, and a reader who counts enumerated-but-
   unretrieved objects as identified must re-derive every count below. Recorded
   as gap **G-7**.
3. **The lateral arm's unit is finer than a document.** Two class records may
   share one URL and one byte digest (for example `KSL-C02`/`KSL-C03`, and
   `KSL-C23`/`KSL-C24`/`KSL-C25`). The CSL-JSON store therefore contains entries
   that share a URL, and it is a **record store, not a document store**. Said
   again in section 14.

<!-- prisma-s-16 -->
### 5.2 Deduplication: process AND software

**Process (protocol section 4.1, frozen).** Exact match on the strongest
available identifier first, in order: DOI (case-normalised), arXiv id, RePEc
handle, package-index name plus version, repository host plus full name, then
canonical URL after stripping tracking parameters. Where no identifier matched, a
hand-verified same-work ledger handled twins: normalised titles matching case-
and punctuation-insensitively, **only for normalised titles of 25 characters or
more** — a shorter string does not identify a work and merging on one would be a
false same-work claim. DataCite mints `10.48550/arXiv.<id>` for arXiv deposits,
so those DOIs were canonicalised to the arXiv id **before** the DOI-then-arXiv
ordering was applied. **Cross-class twins — a paper and its companion repository
— are NOT deduplicated**; protocol section 2.1 makes them two records with a
`companion_of` link.

**Software.** Python 3.11 standard library only, with **`PYTHONHASHSEED=0`
asserted at entry** of each script:
`ks-academic-extract.py` (parse and dedup),
`ks-academic-assemble.py` (candidate table),
`ks-academic-recovery-pass.py`,
and the store builder that emitted `references_kalshi-strategy-multivocal.json`.
The title-merge ledger is `ks-academic-dedup-title-ledger.json` (46 merges, each
carrying the retained and the dropped locator and the query the dropped row came
from). The software arm's harvest keyed on host-plus-full-name at retrieval, so
its intra-arm duplicates were collapsed **at harvest**; the arm log states the
collapse but publishes no count for it, and the count below is **derived** from
the arm's own two published figures.

**Duplicates removed: 412.**

| where | removed | derivation |
|---|---|---|
| ACADEMIC, intra-arm | 122 | 650 rows parsed from the stored payloads − 528 deduplicated rows. Re-derived from the payloads at authoring time and byte-agreeing with each query log's `n_returned` |
| SOFTWARE, intra-arm | 288 | 1,269 rows returned − 981 distinct artifacts. Per host: GitHub 832 − 647 = 185; GitLab 26 − 21 = 5; PyPI 11 − 11 = 0; npm 400 − 302 = 98. **DERIVED by this record from `ks-github-queries.json` and `ks-github-capacity-ledger.json`; the arm log itself publishes no such count** |
| VENUE, intra-arm | 0 | 30 distinct document ids. Six documents appear under two document *classes* each; that is one document in two classes, not a duplicate |
| LATERAL, intra-arm | 0 | 32 distinct class ids. Shared source URLs are not duplicates because the unit is the class |
| **CROSS-ARM** | **2** | itemised immediately below |

**Cross-arm duplicate ledger — both entries hand-verified, both published with a
pointer to the retained record.**

| dropped | retained | matching key under section 4.1 | why, and what was preserved |
|---|---|---|---|
| `KSL-C31` (lateral, `docs.kalshi.com/getting_started/rate_limits`) | `ks-vr-d06` (venue, `docs.kalshi.com/getting_started/rate_limits.md`) | canonical URL after stripping the `.md` content-negotiation suffix | The **same document** retrieved by two arms in two renderings, with two different byte digests because the renderings differ. The venue record carries nine clauses from it; the lateral record carries the burst-capacity and volume-share-tier statements. `ks-vr-d06` is retained as the fuller extraction, and the lateral rendering is carried as an **alternate locator with its own digest** on the T8 taxonomy row in section 8 |
| software-arm G1 row `OctagonAI/kalshi-trading-bot-cli` | `KSL-C27` (lateral) | repository host plus full name | The **same repository**. Deduplication happens **before** screening in the section 4.5 flow, so removing the row is not a merits determination and does not convert an undecided G1 row into a decided one (protocol section 4.4 rule 3 is not engaged). The lateral record is retained because it carries a completed extraction; the software arm never assessed its copy |

<!-- prisma-2020-8 -->
### 5.3 Selection process

**Invoked by ANALOGY.** PRISMA 2020 item 8 does not reach a record that is not a
systematic review (see `standard_declared` clause 2). It is used here because it
is the most legible way to tell a reader what was and was not done, and for no
other reason. The part of item 8 that IS met is the automation-tool declaration;
the dual-independence part is not met and cannot be.

- **screeners_n**: 1
- **independent**: no — single screener, no second screener, no adjudicator, no
  conflict-resolution procedure because no conflict can arise. **No inter-rater
  agreement statistic is computed, and none may be reported.**
- **automation_tools**: Claude Opus 5, model id `claude-opus-5` (Claude Code /
  Claude Agent SDK), acting as the single executing agent across all four arms
  and as the compiler of this record. It assigned every one of the 109
  eligibility verdicts in this corpus and performed every extraction.
  **No keyword or regular-expression classifier assigned any eligibility verdict
  in this corpus.** The academic arm's `B1`-`B4` branching rule
  (`ks-academic-stage1-branch-rule.md`) is a *reporting* router over retrieved
  metadata and decided nothing; the software arm's `SR-1`/`SR-2`/`SR-3` screen is
  a *capacity* subset rule and decided nothing. Both are stored with the logs so
  any row can be re-derived, and both are declared here as non-verdict machinery.

### 5.4 The flow, and the four arithmetic identities

```
n_identified            1986   = 650 academic + 1269 software + 30 venue + 37 lateral
n_duplicates_removed     412   = 122 + 288 + 0 + 0 intra-arm, + 2 cross-arm
n_screened              1574   = 528 academic + 980 software + 30 venue + 36 lateral
n_excluded              1475   = 10 Y-code rows + 1465 G-code rows
n_included                99   = 40 software + 28 venue + 31 lateral + 0 academic
len(CSL-JSON store)       99
```

| protocol section 4.5 identity | value | closes? |
|---|---|---|
| `sum(per-arm n_records) == n_identified` | 650 + 1269 + 30 + 37 = 1986 | **YES** — arithmetically, over a heterogeneous unit (section 5.1, gap **G-16**) |
| `n_identified - n_duplicates_removed == n_screened` | 1986 − 412 = 1574 | **YES** |
| `n_screened - n_excluded == n_included` | 1574 − 1475 = 99 | **YES** |
| `len(CSL-JSON store) == n_included` | 99 == 99 | **YES — the predecessor branch's gap AG-11 is NOT repeated** |

**`n_excluded` decomposed, with the G-rows reported separately from every Y-code
count as protocol section 4.4 rule 2 requires. A corpus record that folds G-rows
into the Y totals is defective; this one does not.**

| code | count | kind |
|---|---|---|
| Y2 no strategy contribution | 3 | criterion failure, assessment performed |
| Y3 unsourced | 5 | criterion failure — the class is reported as an ABSENCE and never as a finding |
| Y4 not retrievable or not digestible | 1 | criterion failure, retrieval chain logged |
| Y9 out of the branch's question | 1 | criterion failure, assessment performed |
| **Y total** | **10** | |
| G1 identified, eligibility not assessed | **1465** | **CAPACITY GAP, NOT A CRITERION FAILURE.** 528 academic + 937 software. Nothing about any of these records' merits was determined. They are not eligible and not ineligible: they are **undecided** |
| G2 eligible, extraction not performed | 0 | — |
| **n_excluded** | **1475** | |

**One arithmetic identity in an arm log DOES NOT CLOSE, and is not repaired
here.** The software arm's capacity ledger states stratum sizes (341 + 253 + 19 +
11 + 68 = 692), an allocation of 43, and `n_G1 = 938` with 289 records outside
every stratum. Its own arithmetic implies **649** in-stratum G1 rows (692 − 43),
of which the npm stratum should hold **63** (68 − 5). The ledger's enumerated
`G1_rows_within_the_strata` lists **647** rows, with **61** under `npm`. **The
enumeration is two rows short of the ledger's own arithmetic**, and after this
record's cross-arm dedup the shortfall stands at 646 enumerated against 648
implied. The headline count 938 (937 here) is the one this record uses, because
it is the count the arm states; **the enumerated list is therefore not a complete
Table Y-full for that arm, and it is short by exactly two rows whose identity is
unrecoverable from the log.** Recorded as gap **G-13** and as data-integrity
defect **DI-2**. Not resolved by rounding, not resolved by reclassification, not
resolved at all.

---

## 6. Excluded records

<!-- prisma-2020-16b -->
**Invoked by ANALOGY** (see `standard_declared` clause 2). Every excluded record
carries exactly one primary code and a reason in the screener's own words. The
ten Y-code rows and the five Y3-unsourced rows are inlined below; the 1,465
G-rows are published **by reference** to the two arm logs that already enumerate
them, for the reason stated after the table.

| id | citation | stage_excluded | reason |
|---|---|---|---|
| ks-sc-020 | `github.com/mateuszp87/kalshi-trading-agent` @ `81c626da42943172a31a358afd4d1e1dba6d8078`, accessed 2026-09-04 | stage-1, README-and-metadata depth | **Y2.** Satisfies section 2.2 by naming Kalshi, but makes none of K1-K4: the README's sole content line states no rule, no measurement, no executability precondition, and no statement of what the tooling does beyond its name. Y2 applied on an assessment actually performed, not stretched over an unassessed record |
| ks-sc-022 | `github.com/yintewang/Kalshi-Scanner` @ `0fb11f5c93bd2b1248f00af4e9c49a87bb2d5e9e`, accessed 2026-09-04 | stage-1, metadata depth | **Y2.** The only descriptive text the platform returns is "It scans things", which states no rule, no measurement, no precondition and no statement of function. **Depth limit recorded: no README exists at the pinned commit, so this disposition rests on metadata alone** |
| ks-sc-023 | `github.com/christianluevano522-bot/Kalshi-scanner`, accessed 2026-09-04 | stage-1, metadata depth | **Y4.** No commit or release identifier obtainable: the commit endpoint returned HTTP 409, the platform's empty-repository response. Without a commit or release the record names no fixed object and there are no bytes to digest. Reported as such rather than silently dropped; **retrieval failure is not evidence of absence and no substantive code was applied** |
| ks-vr-d05 | `kalshi.com/robots.txt`, sha256 `4ac884d2e8aa…`, accessed 2026-09-04 | stage-2, full text | **Y9.** In-scope publisher and a real document, but its content is the venue's crawl policy for named clients. It states no fee, limit, rule, interface capability or settlement mechanic that decides the executability of any strategy class, so it falls outside the section 1.1 question in the same way platform UX does. **Recorded, not deleted: it is the access condition under which the venue arm's own retrieval took place, and section 9 cites it for that** |
| ks-vr-d12 | Document served at the CFTC URL labelled "Kalshi Exhibit M", `cftc.gov/filings/documents/2024/orgdcmkexkalshiexhm240709.pdf`, sha256 `8e73d41f670c…`, accessed 2026-09-04 | stage-2, full text | **Y2.** The retrieved bytes are the rulebook of a **different applicant** (see section 11, defect **DI-1**). As retrieved and extracted it makes no strategy contribution about the venue of interest: only its title block was extracted, and it states nothing under K1-K4. **Deliberately excluded rather than included with a warning, so that it cannot be cited from this corpus's store at all** |
| ks-y3-1 | Candidate class "Within-venue duplicate-listing arbitrage (the same event listed under two Kalshi series or tickers, priced apart)", seed 1, query `KSL-Q21` | Y3 screen | **Y3 UNSOURCED.** The query executed specifically for this returned twenty-three results, all addressing cross-venue divergence or the venue's ticker naming scheme. **No retrieved page states that a single venue has listed the same event twice at divergent prices.** Reported as an absence; NOT entered in the taxonomy |
| ks-y3-2 | Candidate class "Cross-instrument basis against equity index options (event contract vs options-implied probability)", seed 3, query `KSL-Q21` | Y3 screen (Y4 secondary) | **Y3 UNSOURCED, with Y4 as the proximate cause.** The one candidate located returned **HTTP 403** to unauthenticated retrieval, so no verbatim evidence and no byte digest could be recorded. Not retrievable, therefore not sourceable, therefore not in the taxonomy. Referred to a later pass with a different retrieval path |
| ks-y3-3 | Candidate class "Inflation-swap / TIPS-breakeven basis against CPI event contracts", seed 3, query `KSL-Q15` | Y3 screen | **Y3 UNSOURCED.** The query returned inflation-swap explainers, central-bank research and the venue's own product page, but **no retrieved source STATES a pairing** of an in-scope binary CPI contract against an inflation swap or breakeven. Protocol section 2.2's counterparty-leg extension admits the non-binary leg only "when the record states the pairing"; no record states it |
| ks-y3-4 | Candidate class "Self-trade-prevention or wash-trade mechanics exploited as a strategy", seed 6, query `KSL-Q19` | Y3 screen | **Y3 UNSOURCED.** The query returned the venue's rulebook filings and prohibition language stating that wash trades and self-matching are prohibited. **No retrieved source states a STRATEGY built on these mechanics.** The prohibition itself is an S-D precondition, not a strategy class |
| ks-y3-5 | Candidate class "Latency arbitrage on the print itself (reading a scheduled release faster than the book reprices)", seed 5 | Y3 screen | **Y3 UNSOURCED, and this absence is the point.** This is the hypothesis seed 5 names, and **no retrieved source states it as an executable class for the series examined.** The sourced statements run the other way: the payrolls ladder stops trading one minute before the release (`KSL-C18`), and the one practitioner source addressing the race states there is none to win. A class the arm was primed to expect **is not in the retrieved record.** See negative result **N-1** |

### 6.1 Table Y-read — records excluded AFTER stage-2 assessment

Protocol section 4.6 requires this table even when empty, and it is not empty.

| id | what it was | why it did not survive reading |
|---|---|---|
| ks-vr-d05 | The venue's `robots.txt`, retrieved in full and read | **Y9.** Read in full; states a crawl policy and nothing that decides a strategy's executability |
| ks-vr-d12 | A CFTC-hosted PDF that the regulator's own index and filename attribute to Kalshi | **Y2.** Read in full at extraction depth `full-text`. The bytes are another venue's rulebook: **zero occurrences of "Kalshi", 389 of "Railbird"** over the extracted text. It survived retrieval and failed reading |

The three software-arm exclusions (`ks-sc-020`, `ks-sc-022`, `ks-sc-023`) were
dispositioned at stage 1 at README-and-metadata or metadata depth and are not
stage-2 rows; they appear in the main table above.

### 6.2 Table Y3-unsourced

Rows `ks-y3-1` … `ks-y3-5` above **are** Table Y3-unsourced. They are repeated
nowhere else and are entered in **no** taxonomy row: per ADR-0004 and REVIEW.md
blocking directive 8, an unattributed strategy is a **blocking defect, not a
finding**, and the only lawful place for it is an absence table.

### 6.3 Why the 1,465 G-rows are published by reference

They are already enumerated, row by row, in two files inside
`materials_availability`:
`ks-academic-identified-universe.json` (all **528** academic rows, each carrying
its query of origin, its identifiers, its branch label and its novelty flag) and
`ks-github-capacity-ledger.json` (the software arm's in-stratum G1 lists plus the
289-record out-of-stratum count). Reprinting 1,465 rows here would add no
information and would not be machine-readable. **Two caveats travel with that
reference and neither is cosmetic:** the software enumeration is **two rows
short of its own arithmetic** (section 5.4, gap **G-13**), and **every one of the
1,465 rows carries no eligibility determination of any kind** — reason, in the
words protocol section 4.4 rule 1 requires: *eligibility under N1-N6 was not
performed for this record and nothing about its merits was determined.*

---

## 7. Included corpus

<!-- included-corpus -->
**99 records. NONE carries a persistent identifier** — that is the decisive
departure ADR-0006 records, and limitation 8 is its consequence. The
machine-readable form is the CSL-JSON store (section 14). The table below is the
human-readable index; the `role` column carries the **evidence-hierarchy tier**
CLAUDE.md requires next to every claim a record supports.

| id | citation | persistent id | role in the argument |
|---|---|---|---|
| ks-sc-001 … ks-sc-019, ks-sc-021, ks-sc-024 … ks-sc-043 (**40 records**) | public code and package artifacts on github.com, gitlab.com, pypi.org and registry.npmjs.org, each pinned to a commit SHA or release tag as of the 2026-09-04 access date; full per-record metadata in `ks-github-records.jsonl` and in the store | **none** (S-C) | **Tier 5 — anything else, admissible only with the tier recorded.** 28 read at README-and-metadata depth, 12 at metadata depth. They supply what an artifact's own README or metadata **states** about a strategy class, plus two careful negative measurements (section 10). Their producers are platform handles; authority and knowledge are not determinable and are recorded as attributes, never as a rank |
| ks-vr-d01 … ks-vr-d04, ks-vr-d06 … ks-vr-d11, ks-vr-d13 … ks-vr-d30 (**28 records**) | KalshiEX LLC, Polymarket US / QCX LLC and Polymarket venue documents; CFTC filings, orders, press and organization records; eCFR 17 CFR Part 40; Federal Register API result — each with the SHA-256 of its retrieved bytes and its 2026-09-04 retrieval date | **none** (S-D) | **Tier 2 — official documentation.** **130** verbatim clauses across the included set (132 across all 30 retrieved documents; the two excluded records carry one clause each). These are the records that decide **executability**, and section 9 is built entirely from them. Every one is dated by retrieval and every one is amendable on ten business days' notice (`d22-c1`) |
| KSL-C01 … KSL-C30, KSL-C32 (**31 records**) | practitioner write-ups, vendor blogs, individual newsletters and Substack postmortems (24 S-E), venue-published help-centre and documentation pages (6 S-D), one public repository README (1 S-C) — each with the SHA-256 of its retrieved bytes | **none** | **Tier 2** for the six S-D records, **tier 5** for the twenty-four S-E records and the one S-C record. These are the records that **name the strategy classes**, and 27 of the 31 are flagged `lateral` by the arm — classes the ordinary arbitrage vocabulary misses. 29 at full-text depth, **2 at SECONDARY depth** (`KSL-C15`, `KSL-C25`) where the rule text is quoted by a practitioner and the primary document was not retrieved |
| — (**0 records**) | ACADEMIC arm | — | **Tier 1 is EMPTY.** 528 records identified, zero screened, zero included. See limitation 1 |

**Source-class composition of the included corpus:** S-C 41 (40 software arm +
`KSL-C27`), S-D 34 (28 venue arm + 6 lateral-arm venue-published records), S-E
24. **S-A 0, S-B 0.**

**Kalshi-specific vs transferred, across the 71 records that carry the F8 split:**
software arm — 20 `kalshi-specific`, 8 `transferred-with-stated-assumption`, 12
`not-transferable-as-stated`; lateral arm — 25 stated for Kalshi, 6 transferred
with the relation stated. The 28 venue records are not F8-split: an S-D record is
a document of the venue that publishes it, and section 9 states per clause which
venue it binds.

---

## 8. The strategy-class taxonomy, T1-T8

The protocol section 6 skeleton, populated **only** by what the arms attributed
to a source. **Every row carries at least one source id.** A row with an empty
source column is a blocking defect (protocol section 6; ADR-0004; REVIEW.md
blocking directive 8) and there are none. **No class was forced into a bucket:**
the lateral arm's log records `classes_fitting_no_taxonomy_bucket: []` and
`amendment_needed: null`, and `taxonomy_buckets_empty_from_this_arm: []`, so no
section 10 amendment to the taxonomy was needed and none was made.

Reading key. **Depth** is the record's warrant label (protocol field F6) and
travels with every claim derived from it: `RM` = README-and-metadata, `MD` =
metadata, `FT` = full text of the retrieved bytes, `SEC` = secondary (the rule
text is quoted by another source and the primary was not retrieved).
**Split** is F8: `K` Kalshi-specific, `T` transferred with the assumption stated,
`N` not transferable as stated. **`TO COMPUTE`** items are left uncomputed by
ADR-0003 and each names the selection procedure that would choose it; they are
collected as `TC-n` in section 12.

| class | one line | sources that STATE it (record id → depth → split) | Kalshi-specific or transferred | executability preconditions — all `TO COMPUTE`, with the selection procedure named |
|---|---|---|---|---|
| **T1** within-market coherence | Relations among prices inside one market or series: complementary legs, strike ladders, mutually exclusive and exhaustive bundles, monotonicity across strikes | `KSL-C01` FT/K (nested-strike monotonicity on a cumulative ladder); `KSL-C02` FT/K (field-sum coherence, gated on the venue's mutual-exclusivity flag); `KSL-C06` FT/T (venue-provided negative-risk conversion, **Polymarket mechanism, no Kalshi equivalent stated**); `KSL-C07` FT/K (collateral return paid at entry on a mutually exclusive group); `KSL-C29` FT/K (RFQ-priced combo referenced against the product of the single-leg books); `ks-sc-030` RM/T (GitLab artifact stating no-arbitrage violations between related markets). Venue clauses that bound it: `d07-c1`, `d21-c3`, `d21-c4`, `d13-c2`, `d14-c2` | **Mixed.** 4 of 6 stated for Kalshi; `KSL-C06` is a Polymarket mechanism and the sources state **no Kalshi equivalent**; `ks-sc-030` is a Polymarket artifact | **TC-1** the coherence-violation detection threshold net of fees — grid or Bayesian search over the threshold with a bootstrap CI on the resulting statistic, never a hand-set number. **TC-2** the fee-inclusive break-even band per series — derived from `d01-c2`/`d01-c4` with the **per-series multiplier**, which is in a ~90-row table whose cell alignment does not survive extraction (**DI-3**). **TC-12** the MDES for any decision rule, never retrospective power |
| **T2** cross-market / cross-venue | Price relations between the same or corresponding events on different venues | `KSL-C13` FT/K-as-to-geometry (synthesising a band probability by differencing adjacent nested rungs to compare against another venue's single contract); `KSL-C14` FT/T (**the settlement-clock and definition basis — a precondition that NEGATES the ordinary class**); `ks-sc-008` RM/T, `ks-sc-019` RM/T, `ks-sc-021` MD/T, `ks-sc-025` RM/K, `ks-sc-030` RM/T (cross-venue scanners and adapters). Venue clauses: `d25-c2`, `d26-c1`, `d26-c3`, `d29-c2`, `d29-c3`, `d25-c4` | **Transferred by construction** — the class is a relation between two venues. Only `ks-sc-025` is stated as Kalshi-specific | **TC-3** the minimum tradeable gap for a cross-venue pair, computed only after a **settlement-clock and definition alignment test** per `KSL-C14`; selection procedure: paired comparison of the two contracts' filed terms, then a studentised time-series bootstrap on the surviving series ([Ledoit & Wolf 2008](https://doi.org/10.1016/j.jempfin.2008.03.002)) — adopted by explicit reference under ADR-0004, not by default. **TC-5** achievable order rate per venue, which on the pair is metered on **incompatible bases** (`d26-c1`) |
| **T3** cross-instrument basis | Relations against a settlement-source market or a correlated conventional instrument, where the source states the pairing | `KSL-C10` FT/T (against the futures-implied probability of the same policy decision); `KSL-C11` FT/T (against sportsbook lines converted to implied probability); `KSL-C12` FT/K (against numerical weather guidance, with the **named settlement station** as the binding constraint); `ks-sc-004` RM/K (WTI backtest), `ks-sc-009` RM/K, `ks-sc-028` RM/N. Venue clauses: **`d21-c1`** (on that series the Source Agency **is the venue itself**), `d04-c1` (the perpetual-futures leg is restricted to Eligible Contract Participants) | **Mixed.** `KSL-C12`, `ks-sc-004` and `ks-sc-009` Kalshi-specific; `KSL-C10`/`KSL-C11` transferred with the pairing stated; `ks-sc-028` not transferable as stated | **TC-4** the forecast-error distribution for a weather basis — `KSL-C12`'s own source calls its ≈2.7 °F assumption "a guess, not a measurement"; selection procedure: estimate the station-level error distribution from the settlement station's own observation history with a bootstrap CI. **TC-2**, **TC-12**. **Precondition that may foreclose the class outright:** where `d21-c1` holds, there is **no independent third-party reference** to arbitrage against |
| **T4** systematic mispricing / behavioural | Persistent statistical deviations attributed to participant behaviour or market structure, including favourite-longshot type effects | `ks-sc-001` RM/K (favourite–longshot, **reported as already priced in and eaten by fees/spread**); `ks-sc-002` RM/K (contracts priced 10–15¢ realize YES 4% of the time, at close); `ks-sc-004` RM/K; `ks-sc-010` RM/T; `KSL-C19` FT/K (post-release overshoot); `KSL-C28` FT/K (base-rate divergence in retail-dominated categories, **adopted by its author after a reported failure**) | **Mostly Kalshi-specific as stated**; `ks-sc-010` transferred with the assumption stated | **TC-10** the price band at which a taker round trip is viable — derived from the stated fee function and a **measured** spread distribution, not chosen by hand. **TC-11** the NO-probability threshold defining `ks-sc-001`'s candidate — grid or cross-validated search with a bootstrap CI. **TC-12**. **TC-14** family-wise control across the classes tested ([White 2000](https://doi.org/10.1111/1468-0262.00152) reality check or [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA), adopted by explicit reference under ADR-0004 |
| **T5** market making and liquidity provision | Quoting, inventory, adverse-selection and spread-setting rules, and venue liquidity programs | `KSL-C21` FT/K (**S-D**: the venue pays for posted depth "even if your orders don't get filled"); `KSL-C22` FT/K (**S-D**: designated-liquidity-provider status allocated by a **reverse auction** on the minimum reward the applicant will accept); `KSL-C24` FT/K (pro-rata pot dilution makes the realised subsidy largest in the thinnest markets); `KSL-C25` **SEC**/K (maker order protections: correlated resting orders auto-cancel on an adverse position delta); `ks-sc-003` RM/K, `ks-sc-024` RM/N, `ks-sc-026` RM/T, `ks-sc-027` RM/N, `ks-sc-029` RM/T. Venue clauses: `d19-c1` … `d19-c7`, `d02-c1`, `d02-c2`, `d17-c5`, `d17-c6`, `d27-c1` | **Mixed.** The four venue-programme statements are Kalshi-specific; three of the five artifacts are Polymarket- or Betfair-established | **TC-7** the quoting spread, depth and uptime floor a **non-programme** quoter faces — **NOT COMPUTABLE FROM ANY PUBLIC DOCUMENT** (gap **G-2**): `d19-c5` names the four obligation dimensions and states **no value for any of them**. The lawful substitute is an MDES for detecting a difference against a stated alternative, never a retrospective power calculation (project charter). **TC-6** capacity ceiling per contract, which after `d17` is a per-contract fact read from each contract's terms and conditions |
| **T6** mechanism / rule / fee structure | Strategies whose object is the venue's own mechanics: fee and maker-taker structure, settlement and resolution rules, limits, contract-specification edges | `KSL-C03` FT/K (fee-curve curvature confines surviving field-sum candidates to the longshot tail); `KSL-C04` FT/K (round-up-to-the-cent quantisation inflates the effective rate at small size); `KSL-C05` FT/T (cross-venue fee-curve shape asymmetry as a leg-placement constraint); `KSL-C08` FT/K; `KSL-C09` FT/K (**interest accrues on the collateral behind open positions**); `KSL-C15` **SEC**/K (source-outage default and revision immunity); `KSL-C16` FT/K (per-series asymmetry in revision treatment); `KSL-C17` FT/K (unresolvable outcomes settle at an exchange-determined fair price, not void); `KSL-C18` FT/K (trading close **precedes** the scheduled release); `KSL-C23` FT/K (volume-incentive credit can exceed the whole taker fee at the low edge of the eligible band); `KSL-C26` FT/T (contract characterisation and entity structure as an after-tax executability constraint); `ks-sc-002` RM/K, `ks-sc-006` RM/K, `ks-sc-007` RM/K, `ks-sc-018` RM/K, `ks-sc-025` RM/K. Venue clauses: the whole of `d01`, `d08`, `d09`, `d10`, `d16`, `d17`, `d18`, `d20`, `d21`, `d22`, `d23` | **Overwhelmingly Kalshi-specific** — 14 of 16 records state the mechanics of a named venue | **TC-2** the per-series fee multiplier (blocked by **DI-3**). **TC-6**. **TC-12**. **Preconditions already SETTLED by the document set are in section 9 and are not `TO COMPUTE`** — this is the one class where the venue arm resolves more than it leaves open |
| **T7** information and forecasting | Strategies driven by an external forecast or information advantage, including model- and agent-based forecasting | `KSL-C20` FT/K (pre-committed surprise band with an explicit executability test); `KSL-C27` FT/K (**S-C**: model-derived probability differenced against the live order book); `ks-sc-005` RM/K (RL trader on hourly crypto markets), `ks-sc-011` RM/K, `ks-sc-028` RM/N, `ks-sc-031` RM/N, `ks-sc-041` MD/N | **Mixed.** 4 of 7 Kalshi-specific; 3 not transferable as stated | **TC-4**. **TC-12**. **Access precondition the source itself states:** `KSL-C20`'s source states that reading the release value "requires a separate authorized data integration" it does not provide. **Venue precondition:** `d18-c2` — on at least one series a **five-second resting test reassigns maker/taker roles after the fact** |
| **T8** infrastructure and tooling | Data capture, interface clients, backtest harnesses and analysis tooling that enable any of T1-T7 | 28 software-arm records: `ks-sc-001`, `-002`, `-004`, `-006` … `-009`, `-012` … `-018`, `-029`, `-031` … `-043` (RM or MD; 16 K, 3 T, 9 N); `KSL-C30` FT/K (**the venue's raw markets feed is flooded with auto-generated combination markets, so a scanner's market count is not a count of tradeable markets**); `KSL-C32` FT/K (dispute and re-determination are machine-readable market states); **`ks-vr-d06` FT/K** — clauses `d06-c1` … `d06-c9`, the authoritative token-bucket metering document, **carrying the alternate rendering `docs.kalshi.com/getting_started/rate_limits` retrieved by the lateral arm as `KSL-C31`, sha256 `3c7a9b2b702b66be5a0a2765522d373609fef91181e3bb4227977878371b19a1` per `ks-lateral-records.json`, 285,570 bytes, HTTP 200, retrieved 2026-09-04T10:14:38-05:00, deduplicated into this record per section 5.2** | **Mixed.** 19 of 31 Kalshi-specific (16 of the 28 artifacts, plus `KSL-C30`, `KSL-C32` and `ks-vr-d06`); the package-index clients for the paired venue are not transferable as stated | **TC-8** the universe-construction filter separating single-outcome markets from auto-generated combinations (`KSL-C30` states the requirement and **no filter rule**); selection procedure: derive from the venue's own series/event schema and validate against settled-market outcomes. **TC-9** the polling interval for any replication of a capture — justified against the venue's stated rate limits and the autocorrelation of the quote process, not chosen. **TC-5** |

**Empty classes: none.** All eight first-level classes are populated. That is a
finding about the retrieved record and **not** evidence that the partition is
correct or complete; a class that no arm found would have been reported as empty,
which would itself have been a finding.

**Bare numbers stated by sources, recorded verbatim, FLAGGED, and NOT ADOPTABLE.**
The user-level parameter rule (zero arbitrary thresholds, zero magic numbers;
in-repo carrier charter commitment 3) forbids carrying any of these into a
downstream parameter choice without its own empirical justification. The lateral
arm flagged them at execution and this record repeats the flag:

| source | figure, verbatim | why it is not adoptable |
|---|---|---|
| `KSL-C10` | "diverge by more than 5 percentage points after accounting for fees" | **Chain citation, not verified.** The source attributes the threshold to "Prevayo's 2026 analysis", gives no locator, and the underlying analysis was not retrieved |
| `KSL-C19` | "the first 15 minutes"; "Waiting 2 to 4 hours"; "peaks 24 to 48 hours before the release" | Carry **no measurement, no data span and no citation** on the page; the source presents them as practice |
| `KSL-C28` | "never trade contracts below ~$0.15" | The author's stated rule with **no fitted derivation** on the page |
| `KSL-C12` | "we used ≈2.7 °F" | The source itself says assuming a forecast-error distribution "is a guess, not a measurement" |
| `ks-sc-001` | "+1.37% ROI, CI [1.13, 1.61], n=23" | Reported by the source with its own caveat that the candidate is "statistically indistinguishable" from the always-NO baseline. Transcribed, attributed, **not adopted, not re-derived, not annualised** |

---

## 9. Executability preconditions — what the document set SETTLES and what it does NOT

This is the section that makes the taxonomy usable. **A stated discrepancy is not
an opportunity if a clause forecloses it.** Everything below is built from the
28 included S-D records and their **130** verbatim clauses (two further venue records
are excluded and are cited only where noted). Every clause is dated
**2026-09-04 by retrieval** and every one is amendable on ten business days'
notice for a rule change (`d22-c1`) or **one** business day for a product listing
(`d22-c3`).

**Attribution discipline, carried from the arm log:** no statement here asserts
venue conduct in this corpus's voice. The corpus never says "the venue charges
X"; it says **a named document states X as of a named date**. Two clauses
(`d27-c1`, `d26-c5`) contain contact email addresses and are therefore
**described rather than quoted**, so that no address enters this committed file
(rules/publishing.md identity hygiene, gate assertion G18); both are quotable in
full from `ks-venue-docs.json`.

### 9.1 SETTLED by the retrieved document set

| precondition | what the document set settles | clause ids |
|---|---|---|
| **Fee incidence and functional form** | Trading fees are charged only to the immediately-matched side unless a maker multiplier applies; the taker function is `fees = round up(M x 0.07 x C x P x (1-P))` and the maker function `fees = round up(M x 0.0175 x C x P x (1-P))`; the taker multiplier defaults to 1 and **the maker multiplier defaults to 0**; where non-zero, **the maker is CHARGED, not rebated**; rounding is always upward to a centicent; quote-and-cancel is not fee-bearing | `d01-c1` … `d01-c7` |
| **Cost is price-dependent and maximal mid-range** | The fee is a downward parabola in price, so cost is not constant across the price range | `d01-c2`, and independently at `ks-sc-002`, `KSL-C03` |
| **A second, unmodelled cost component exists** | A **rounding fee** is charged to realign balances to the member's precision, balance precision differs by membership class (`$0.0001` direct vs `$0.01` non-direct), net fee is floored at zero so no fill returns a net credit, and the fee accumulator is **per order across all fills**, so cost is path-dependent within an order | `d08-c1` … `d08-c4` |
| **Cross-venue maker treatment has OPPOSITE SIGN** | On the paired US venue the maker coefficient is **negative** — the maker is paid, at the point of trade, with no programme required. On a third entity makers are neither charged nor rebated. **Any strategy assuming symmetric maker treatment across a pair is mis-specified at the point of writing** | `d25-c2`, `d25-c3`, `d29-c2` |
| **Collateralisation** | All member positions are **fully cash collateralised**; no member may take exposure beyond deposited funds. This sets the capital denominator of any return: there is no leverage on the binary leg | `d14-c2`, `d13-c2` |
| **Netting** | Only net positions settle, which is what makes a within-market coherence position self-extinguishing at expiry | `d07-c1` |
| **Tick and payout** | Minimum tick `$0.01` and settlement value `$1.00` on the one series specified at this depth — one cent on a one-dollar payout is the smallest expressible edge | `d21-c3`, `d21-c4` |
| **Throughput is a token bucket, and the top tiers cannot be bought** | Budget is in tokens per second; most requests cost 10 tokens; write traffic draws on a budget separate from reads; **Basic (signup) = 100 tokens/s write = 10 orders/s**; Expert through Prestige are earned from volume share or **assigned at the venue's discretion**; volume share is trailing-30-day volume ÷ (previous month's exchange volume × 2), with stated earn/keep hysteresis; **batching does not relax the ceiling and a batch is all-or-nothing** | `d06-c1` … `d06-c9` |
| **A published position number exists, and a regime change moved it** | Rule 5.14(a) stated "Position Limits of 25,000 USD on all Contracts", expressed **per member in dollars of exposure**; the 2023 filing removed the global limit in favour of per-contract terms; the 2024 filing added **Position Accountability Levels**, which are a **discretionary instruction point with forced-liquidation authority**, not a hard cap; **market makers carry $1M or $10M levels where an ordinary member's generally applicable level is $250k or less**, and market makers are exempt from hard limits on their obligated contracts; a federal ceiling sits above the exchange's own; positions held under an express or implied agreement aggregate | `d16-c1` … `d16-c4`, `d17-c1` … `d17-c7`, `d13-c1`, `d14-c3`, `d21-c2` |
| **A block-trade route exists and is gated by size and status** | Default block minimum **25,000 contracts**, restricted to eligible contract participants. Below it every order must interact with the central limit order book | `d20-c1`, `d20-c3` |
| **Settlement is not always mechanical** | Where the source fails, payout becomes a **discretionary fair allocation** by the exchange; expiration timing is movable **in both directions** at exchange discretion; sole-discretion Market Outcome Review may be initiated before settlement on every contract in the series; first publication governs and post-expiration revisions do not reopen settlement; a status of "unavailable" on the index erases an observation | `d17-c8`, `d17-c9`, `d21-c5` … `d21-c10` |
| **Capital lockup has no stated upper bound** | Settlement is "no later than the day after the Expiration Date, **unless** the Market Outcome is under review", and **no maximum review duration is stated**; venue documentation separately states settlement timing "can vary" | `d21-c10`, `d07-c2` |
| **A recurring, scheduled dead window exists** | Thursday 03:00–05:00 ET maintenance trading pause; under a **trading** pause resting orders can be cancelled, under an **exchange** pause they cannot, and resting orders remain on the book by default in both | `d10-c1` … `d10-c3` |
| **Counterparty structure and transparency** | Customers trade peer-to-peer, the venue never takes the other side, and **every trade is published publicly through the API** — a participant's own execution footprint is public | `d04-c4`, `d03-c4` |
| **Observation is unauthenticated; execution is not** | Public market data requires no authentication; order entry does. A study can be run on data a strategy could not be executed on | `d03-c1` |
| **Access channel and participant eligibility** | Intermediated (FCM-carried) access became permissible only from 2025-01-17; binary event contracts are open to US residents 18+ with a valid SSN; **perpetual futures are restricted to Eligible Contract Participants**, so a binary-versus-perp basis is unavailable to a non-ECP; the designation itself is revocable on the Commission's own motion | `d15-c1`, `d15-c2`, `d11-c2`, `d04-c1`, `d04-c2`, `d15-c3` |
| **A non-market-maker faces a documented structural disadvantage** | The venue's own member agreement states market makers may receive fee discounts, rebates, revenue share, disconnect-cancel protection and **greater throughput**, "may be able to price their quotes in ways that are materially different", and that liquidity outside required windows "may be worse". **A cost or fill-rate figure built from the public fee schedule and public tier ladder is therefore an UPPER BOUND on a non-market-maker's competitiveness against the members who set the quotes** | `d02-c1`, `d02-c2` |
| **Rule-change latency** | Ten business days' minimum public notice for a rule change; **one** business day for a product listing; the Commission may stay a self-certified change before it takes effect, and did so against this venue | `d22-c1`, `d22-c3`, `d22-c6`, `d23-c1` |
| **Trade finality is contested, not assumed** | A state court directed cancellation of already-executed trades; the venue proposed an emergency rule change; the federal regulator **stayed it and ordered the open trades fulfilled**. This is a risk no fee, limit or rate-limit clause captures | `d23-c1`, `d23-c3` |
| **Terms are unilaterally amendable** | The member agreement may be amended unilaterally on notice, with deemed agreement absent termination — **no version of the executability preconditions is contractually stable for a participant** | `d02-c3` |

### 9.2 NOT settled — and the distinction between "not retrieved" and "WITHHELD AT SOURCE"

| what is not settled | status | evidence |
|---|---|---|
| **The market-maker/liquidity-provider selection procedure** | **WITHHELD AT SOURCE.** "The procedure … is described in Appendix B" — Appendix B is confidential. Admission is discretionary and by request. Whether a given participant could obtain the incentive terms **is not determinable from any public document** | `d19-c2`, `d19-c3` |
| **Which contracts carry elevated position limits** | **WITHHELD AT SOURCE.** "appendix A is confidential and submitted under a request for confidential FOIA treatment" | `d16-c5` |
| **How the settlement Source Agency operates** | **WITHHELD AT SOURCE.** "Appendix E (Confidential) - Source Agency". The public record of the settlement mechanism is **incomplete by design** | `d21-c11` |
| **The Market Maker Agreement itself** | **NOT A PUBLISHED DOCUMENT.** It is the gate on every incentive and on the elevated accountability levels, and it was not located at any endpoint searched | `d19-c1`, `d17-c5` |
| **The quoted spread, size, uptime and coverage a subsidised competitor must maintain** | **NAMED BUT UNVALUED.** The four obligation dimensions are named; **no value is stated for any of them**, and they are set per incentive period and not published | `d19-c5` |
| **The clearing counterparty, in the public 2020 filing** | **REDACTED.** Even the DCO is `[REDACTED]` in that version | `d14-c4` |
| **The 2020-filed position limit** | **REDACTED.** Defined as "maximum loss exposure" — a definition, not a number | `d14-c1` |
| **The reportable position level per contract** | **NOT PUBLISHED.** The rulebook states it is "communicated to FCM members", so its value is not obtainable from the document | `d13-c4` |
| **The per-series fee multipliers (~90 series) and the tiered perpetual-futures schedules** | **NOT EXTRACTABLE.** The tables are in the retrieved bytes but their cell alignment is destroyed by extraction, so **no cell value is quoted**. The shape of the tables is on the record; their contents are not | `d01` `tables_not_quoted`; defect **DI-3** |
| **The rulebook in force on the retrieval date** | **NOT LOCATED.** See limitation 4 | `KS-VR-Q01`, `Q01b`, `Q02`, `Q14`–`Q17` |
| **Achievable order rate expressed in one unit** | **STATED ON THREE INCOMPATIBLE BASES BY THE SAME VENUE, AND NOT RECONCILED HERE.** Two venue pages state a flat "~100 requests per second per API key" as a **default**; the authoritative document meters a token bucket in which 100 requests/s is the **Premier** tier, not the default. The paired venue states a flat 20 requests/s per key with no ladder. **No conversion is performed** | `d03-c2`, `d04-c3`, `d06-c1`, `d06-c2`, `d26-c1`; gap **G-11** |
| **Position size and block threshold in one unit** | **STATED IN DIFFERENT UNITS AND RECONCILED BY NO DOCUMENT.** The block threshold is in **contracts** (25,000); the position limit is in **USD of exposure** (25,000). **No reconciliation is performed here** | `d20-c1` note, `d16-c1`; gap **G-19** |
| **Interest paid on collateral behind open positions** | **TWO VENUE PAGES STATE DIFFERENT RATES.** A help-centre page states 3.25%; a second venue page headlines 4.05%. Both were retrieved. **The discrepancy is recorded, not resolved** | `KSL-C09` and its compiler note; gap **G-12** |
| **Maker/taker classification on at least one series** | **REASSIGNED AFTER THE FACT.** On KXMVE, for trades not involving an order resting more than five seconds, roles are reassigned by a post-trade adjustment. A strategy that assumes it earned maker treatment by resting **can be reclassified after execution** | `d18-c2` |
| **Whether "there is no settlement fee" holds** | **QUALIFIED BY TWO OTHER DOCUMENTS.** The fee schedule says there is none; the venue's settlement page says fees "may apply for sub-cent scalar settlement"; the RFQ filing quotes Rule 3.13(c) reserving the right to charge one, published on the website | `d01-c8`, `d07-c3`, `d18-c3` |
| **The venue's public change-notification channel** | **NOT MACHINE-READABLE.** The filing certifies that submissions are posted at the venue's notices URL; that URL returns HTTP 200 with **no notice text in the retrieved bytes** | `d18-c4`, `KS-VR-Q48`; and `ks-vr-d05` (excluded) is the crawl policy under which that retrieval took place |
| **Paired-venue market-maker programme terms** | **RETRIEVED IN FORM, EMPTY IN SUBSTANCE.** The entire public document is two sentences and publishes no obligation, no reward, no eligibility test and no term. Described rather than quoted here because it contains a contact address | `d27-c1` |
| **Higher paired-venue throughput** | **BILATERAL REQUEST, NOT A PUBLISHED LADDER** — the same discretionary gate in a different form. Described rather than quoted here because it contains a contact address | `d26-c5` |
| **Whether a two-leg cross-venue order survives a moving market** | **THE PAIRED VENUE DROPS ORDERS UNDER LATENCY.** A five-second stopgap rejects unprocessed inbound orders, and the venue states the reject message "`Global Rate Limit Exceeded`" is **misnamed by its own admission**. Leg risk is concentrated exactly in the states where a discrepancy would appear | `d26-c3`, `d26-c4` |
| **Open rulemakings that could change listing eligibility or published data** | **METADATA DEPTH ONLY.** Three proposed rules were identified and **not retrieved beyond metadata**: public-interest determinations for prediction markets (2026-06-12), data reporting requirements for certain event contracts (2026-07-01), and event contracts (2024-06-10) | `d24-c2`, `d24-c3`, `d24-c4` |

---

## 10. Negative results

This project's charter makes nulls **objects of study, not dead ends**. Nothing
below is a claim by this corpus; each is what a named source states, or what the
search itself did or did not do.

**N-1 — the post-print latency race is UNSOURCED as an executable class, and one
sourced clause runs against it.** Seed 5 was executed specifically for it. **No
retrieved source states it as an executable class for the series examined**, so
it is dispositioned `Y3` (`ks-y3-5`) and enters **no** taxonomy row. The sourced
statement that runs the other way is `KSL-C18`, quoted verbatim and attributed to
OddsShopper, 2026-08-19: *"on Kalshi's KXPAYROLLS ladder, trading closes at 8:29
AM ET and the report lands at 8:30, so whatever you hold going in is what gets
graded."* The same source states the close is tied to the expected release rather
than to a fixed clock — each monthly market carries a close set, in the
exchange's own wording, *"at 8:29 AM ET on the expected date of the data
release"*. **The venue removes the window by construction on that series.** The
lateral arm records this as a constraint (K3), not as a trade, and so does this
record. *Scope of the null: one series, one source, stated for the payrolls
ladder. It is not a statement about every scheduled-release series.*

**N-2 — the software arm's first careful negative.** `ks-sc-001`
(`github.com/sudo-ai-git/kalshi-backtest`, pinned commit, README depth) states,
verbatim and attributed: *"Best candidate strategy (BUY_NO @ high-NO-prob) |
+1.37% ROI, CI [1.13, 1.61], n=23"* over *"~92,000 settled/closed Kalshi
markets"*, and states in the same README that the candidate is **"statistically
indistinguishable" from the always-NO baseline**, that *"The correct null for any
strategy is the **always-NO baseline**, and every candidate must beat it"*, and
that the favourite–longshot bias *"is already priced in and eaten by
fees/spread."* **The ROI figure's own cost treatment is not stated in the
README.** Nothing here is re-derived, re-scaled, rounded or annualised, and
**+1.37% is not adopted as a finding of this corpus** — the record's own null
result is that its best candidate did not beat its own baseline.

**N-3 — the software arm's second careful negative.** `ks-sc-002`
(`github.com/himagna16/kalshi-microstructure` @ `817fe37c…`, README depth) states
over *"July 30 to August 17, 2026; 8.06M snapshots across 54,380 contracts"*:
*"**Prices are extremely well calibrated.** Brier score 0.009 at close, 0.062
even 24h out (vs ~0.24 for guessing the base rate). The market knows."* It also
states *"**Most listed contracts are never tradable.** 79% of the 54,380
contracts observed never showed a two-sided book"*, and that *"A contract trading
at 40–50¢ must move **10.7¢** (≈ 11 percentage points of implied probability)
before a taker round trip breaks even."* Brier scores are point values with no
interval stated. Attributed, not adopted. **The two records N-2 and N-3 are the
only measurements in this corpus that state a data span and a cost treatment at
all, and both of them are negative.**

**N-4 — a practitioner's reported failure, and the pivot it produced.**
`KSL-C28` (Northlake Labs, 2026-02-23) states, verbatim and attributed:
*"0-32. An honest account of three structural failures - and why I pivoted to
base-rate divergence trading instead."* and *"In market microstructure terms: I
was providing exit liquidity for the bots that got there first. They arbed the
anomaly; I picked up their leftovers and paid full fees for the privilege."*
**The losing record is reported for the ABANDONED model-versus-market weather
strategy; NO outcome is reported for the base-rate strategy the class actually
names.** The record is a registered null of exactly the kind the charter treats
as an object of study. Its `~$0.15` price floor is a bare number and is not
adoptable (section 8).

**N-5 — the weather stratum is NOT a clean absence, and must not be reported as
one.** **Two** academic queries in that stratum executed and returned zero:
`ks-arxiv-04` (HTTP 200, `n_returned` 0, `n_total_reported` 0, no failure field)
and `ks-openalex-04` (HTTP 200, `n_returned` 0, `n_total_reported` 0, no failure
field). **`ks-repec-04` and `ks-repec-04-b` did NOT execute.** Both logs carry
`platform_interface_failure` — *"PLATFORM INTERFACE FAILURE, NOT A ZERO-YIELD
RESULT … the body is the IDEAS/RePEc search FORM, not a result set … The query
therefore never executed … n_returned=0 here means NO SEARCH WAS RUN"* — and
`n_returned_semantics: "no search executed; not an observed zero-yield"`. They
are a **capacity gap** (**G-26**), not an observation.

> **CORRECTION 2026-09-04 (round-1 audit; REV-1-1, SCOPE-1-1, QUANT-1-1,
> LITERATURE-1-1, REPRODUCIBILITY-1-1, FORMAT-1-1).** This note previously read
> *"Four academic queries in that stratum executed and returned zero:
> `ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and
> `ks-repec-04-b` (HTTP 200, 0)."* Struck: it reported a capacity gap as an
> observed zero. The superseded wording is retained here. See **DI-8**.

**But `ks-s2-03` — the one query aimed squarely at
temperature settlement, verbatim
`https://api.semanticscholar.org/graph/v1/paper/search?query=weather%20event%20contract%20temperature%20settlement%20hedging&fields=title,year,venue,externalIds,abstract,citationCount,publicationTypes&limit=50`
— NEVER EXECUTED.** It was attempted **eleven times** (`ks-s2-03`, `-03-b`
through `-03-k`) and every attempt returned **HTTP 429**. The stratum's yield is
therefore the yield of a search **with its most on-point query missing**, and no
inference about the weather literature may be drawn from it. Across the whole
academic arm, **53 of 56 Semantic Scholar attempts returned HTTP 429 and one
returned HTTP 500**; only `ks-s2-02-i` and `ks-s2-06-c` succeeded. Recorded as
gap **G-9**.

**N-6 — five candidate classes were sought and not sourced.** Rows `ks-y3-1` …
`ks-y3-5` in section 6. Each is an **absence**, reported as an absence, never
asserted. Two of them (`ks-y3-2`, `ks-y3-3`) were sought against specific
executed queries that returned material which did not state the pairing; the
protocol's counterparty-leg extension admits the non-binary leg **only when the
record states the pairing**, and no record stated it.

**N-7 — the taxonomy needed no amendment, which is itself a negative result about
the taxonomy's coverage of what was found.** The lateral arm's log records
`classes_fitting_no_taxonomy_bucket: []`, `amendment_needed: null` and
`taxonomy_buckets_empty_from_this_arm: []`. **This is evidence that the eight
buckets absorbed everything the arms located; it is NOT evidence that the
partition is correct**, because a search that finds only what the partition
anticipates will always report this result.

**N-8 — two whole endpoints returned nothing, for reasons that are not evidence
about the literature.** RePEc **executed no search at all** across nine attempts
— four queries plus five retries (`ks-repec-01`, `-01-b`, `-01-c`, `-02`,
`-02-b`, `-03`, `-03-b`, `-04`, `-04-b`). Every attempt answered HTTP 200
carrying the IDEAS/RePEc search **form**, not a result set. Each log records
`n_returned_semantics: "no search executed; not an observed zero-yield"`.
**RePEc did not return zero; RePEc was never searched** (**G-26**). SSRN's own interface
returned **HTTP 403** unauthenticated at `ks-ssrn-01`. GitHub's code-search
endpoint returned **HTTP 401** without authentication and Kaggle's kernel list
likewise, so **no code-level search and no notebook search was executed at all**
(gap **G-22**). None of these is a finding about the absence of records; each is
a finding about the endpoint.

> **CORRECTION 2026-09-04 (round-1 audit; REV-1-1, LITERATURE-1-2,
> REPRODUCIBILITY-1-2).** This note previously read *"RePEc returned zero across
> nine attempts (four queries plus retries, all HTTP 200 with an empty result
> page)"*. Struck. "An empty result page" describes a search that ran and found
> nothing; the logs describe a form served and no search run. The superseded
> wording is retained here. See **DI-8**.

---

## 11. Data-integrity defects — recorded, not repaired

**DI-1 — the CFTC organization record links a document labelled "Kalshi Exhibit
M" whose bytes are another venue's rulebook.** The regulator's Kalshi
organization record (`ks-vr-d11`) lists
`https://www.cftc.gov/filings/documents/2024/orgdcmkexkalshiexhm240709.pdf` under
the label "Exhibit M", and the regulator's own filename encodes `kex kalshi exh
m`. The bytes served (sha256 `8e73d41f670c8ac8c656ff14a39afb1d9561948cec79b3482a18242af1a2f91a`,
402,074 bytes, HTTP 200, retrieved 2026-09-04T15:14:22+00:00) are titled
*"Exhibit M: Rulebook / Railbird Technologies, Inc. / Rulebook / Date:
7/3/2024"*. Over the extracted text the document contains **zero occurrences of
the string "Kalshi" and 389 occurrences of "Railbird"**.

**Consequence, stated plainly: anyone citing that locator as "Kalshi Exhibit M
(2024)" quotes another venue's rulebook.** Railbird Exchange, LLC is itself a
designated contract market (designated 2025-06-13, `d30-c2`), so the mistaken
citation would be to a real but *different* venue's rules — the most dangerous
kind of misattribution, because the document looks right.

**What this record does about it: records it and does not repair it.** The
document is **excluded** from the corpus under Y2 (section 6) so that it cannot
be cited from this corpus's store at all; the 2024 Kalshi rulebook exhibit is
recorded as **NOT LOCATED** at the endpoints searched on this date; and no
correction is asserted, because correcting a regulator's index is not this
corpus's act to perform. Gap **G-8**.

**DI-2 — the software arm's G1 enumeration is two rows short of its own
arithmetic.** Section 5.4. The `npm` stratum lists 61 rows where the ledger's own
stratum size (68) minus its own allocation (5) implies 63. The identity does not
close and the two missing rows are unrecoverable from the log. Gap **G-13**.

**DI-3 — three tables in the fee schedule are in the retrieved bytes and are not
extractable.** A general per-price fee table, a per-series non-standard
maker/taker multiplier table over roughly ninety series, and two tiered
perpetual-futures schedules across eleven volume tiers. Column alignment does not
survive text extraction — tier labels and values do not stay in register — so
**no cell value is quoted anywhere in this record.** The existence and shape of
the tables is on the record; their contents are not. This is what blocks **TC-2**.

**DI-4 — two venue-published pages state different interest rates on the same
programme.** A help-centre page states the rate is "set at 3.25%"; a second
venue page headlines 4.05%. Both were retrieved in the same pass. **Recorded, not
resolved.** Gap **G-12**.

**DI-5 — the same venue states its throughput ceiling on three incompatible
bases, and the paired venue on a fourth.** Section 9.2. **No conversion is
performed.** Gap **G-11**.

**DI-6 — the venue arm's own log states two mutually inconsistent counts of
retrieved rule filings.** Its document-class 1 note states that of 111 enumerated
KEX rule filings "five were retrieved in full"; its document-class 7 note states
that four self-certifications were retrieved and "The remaining 107 rule filings
are enumerated and left unretrieved", which implies four. **The two statements
differ by one and this record does not resolve them**; limitation 3 quotes the
"five" figure because it is the one document-class 1 states about the rulebook
lineage specifically. Gap **G-7**.

**DI-7 — two S-D records extract with damage and their quotations must never be
re-quoted as clean rule text.** `ks-vr-d13` and `ks-vr-d17` are track-changes
redlines carrying DRAFT watermarks; their extracted text contains interleaved
struck and inserted wording and spurious intra-word spaces, and `ks-vr-d21`
carries spurious intra-word spaces throughout. Quotations from them are
transcribed **exactly as extracted** so that they remain reproducible from the
bytes, which is why several quotations in section 9 look malformed. They are
flagged `extraction_defect` in the store.

**DI-8 — this record reported a platform-interface failure as an observed
zero-yield, and the report is corrected here rather than overwritten.** *Added
2026-09-04 by round-1 audit remediation. Raised independently by SIX of the seven
routed audit branches: **REV-1-1** (critical), **SCOPE-1-1** (critical),
**QUANT-1-1** (critical), **LITERATURE-1-1** (critical),
**REPRODUCIBILITY-1-1** (critical) and **FORMAT-1-1** (critical), with
**LITERATURE-1-2** and **REPRODUCIBILITY-1-2** (both major) on the second
instance.*

Two statements in this record were false. Head limitation 9 read *"Four executed
academic queries in that stratum returned zero"*, and section 10 note **N-5**
read *"Four academic queries in that stratum executed and returned zero:
`ks-arxiv-04` (HTTP 200, 0), `ks-openalex-04` (HTTP 200, 0), `ks-repec-04` and
`ks-repec-04-b` (HTTP 200, 0)."* A second instance, note **N-8**, read *"RePEc
returned zero across nine attempts (four queries plus retries, all HTTP 200 with
an empty result page)."*

**The evidence against them is in the arm logs' own fields.** `ks-repec-04.json`
and `ks-repec-04-b.json` each carry `platform_interface_failure` — *"PLATFORM
INTERFACE FAILURE, NOT A ZERO-YIELD RESULT … the body is the IDEAS/RePEc search
FORM, not a result set … The query therefore never executed … n_returned=0 here
means NO SEARCH WAS RUN"* — and `n_returned_semantics: "no search executed; not
an observed zero-yield"`. `ks-arxiv-04.json` and `ks-openalex-04.json` carry
HTTP 200, `n_returned` 0, `n_total_reported` 0 and **no** failure field, so those
two did execute. **The corrected executed-and-zero count is TWO.** All nine RePEc
attempts carry the same two fields, so none of them executed.

**Why this defect is the serious kind.** It is the exact inference this record's
own section 5.4 says a defective record makes — folding a capacity gap into an
observation — committed in the one limitation whose entire purpose is to stop a
reader making it. The same class extends to SSRN (HTTP 403), GitHub code search
(HTTP 401) and Kaggle kernels (HTTP 401), whose `n_records` of 0 in section 2 are
now flagged as interface failures rather than yields; PRISMA-S item 15 is claimed
directly on those counts, so an unflagged zero misreported the item.

**What changed and what did not.** Limitation 9, **N-5**, **N-8**, the four
section 2 source rows and the nine `ks-repec` annotations in the section 3 fence
are corrected in place with the superseded wording retained at each site. Gap
**G-9** is extended and gap **G-26** is added. **No arm log is edited** — the logs
are the primary record and were right all along. **No count changes**: RePEc
contributed 0 records to `n_identified` before and after, and both flow identities
still close. `failure_log.md` **F007** adjudicated this defect before the audit
raised it and is cross-referenced here so the two documents agree.

---

**DI-9 — two software-arm extractions are incomplete, and the corpus characterised
both sources at the truncated depth.** *Added 2026-09-04 by round-2 audit
remediation; findings **LITERATURE-2-2** and **QUANT-2-5**. The defects were
verified during round-1 remediation at primary-source depth, but the verification
was propagated only into an unfrozen draft design, leaving this record — the
artifact of record — carrying the truncated reading with no flag.*

**`ks-sc-001`.** The arm log's evidence quotes omit the record's own headline
null. Its README states, in bold, **"No price-based strategy clears the honest
bar."**, with the always-NO baseline defined as that bar, and closes
**"Conclusion: there is no demostrable price-based edge in the public
settled-market data."** *(the misspelling is the source's and is transcribed
exactly)*. The source therefore makes a **stronger** claim than the arm log
carries and a **weaker** one — that its best candidate is "statistically
indistinguishable" from the baseline at n=23. Downstream work that uses only the
weaker claim is being **conservative**; asserting that the source never made the
stronger one would be **false**, and one draft did assert exactly that before this
was caught.

**`ks-sc-002`.** The extraction stops one sentence early. The README gives the
40-50¢ round-trip hurdle of **10.7¢** and, in the very next sentence, **"Even at
the tails the hurdle is 2.6¢."** The dropped sentence matters because it reverses
the natural reading: a consumer told only the mid-range figure may conclude the
tails are unconstrained, when the source states a bar there too.

**Provenance and its limits.** Both sets of sentences were confirmed by
re-fetching the pinned raw README URLs on 2026-09-04. The fetch returns converted
text rather than raw bytes, so **the README digests in the store remain the arm
log's and were not recomputed**, and only section-level — not line-level —
locations were obtainable. **No arm log was edited**: the logs record what the
executing agent extracted, and correcting them retrospectively would destroy the
evidence that the extraction was incomplete. Both figures are added to the
non-adoptable register at **G-23**.


---

## 12. Named gaps and `TO COMPUTE` handoffs

The branch agenda consumes these by identifier. Every gap is an absence this
record could not close; every handoff is a parameter an executing project would
have to choose, left uncomputed under ADR-0003 with its selection procedure
named.

### 12.1 Named gaps

| id | gap |
|---|---|
| **G-1** | The **rulebook in force on 2026-09-04 was not located**. Every venue-side rule surface returns HTTP 200 with no rule text in the bytes. Every rulebook-level statement here comes from a superseded (2019, redacted) or degraded (2023 redline) copy |
| **G-2** | The **market-maker selection procedure is withheld at source** (confidential Appendix B, `d19-c3`), and the **Market Maker Agreement** that gates it is not a published document (`d19-c1`) |
| **G-3** | **Which contracts carry elevated position limits is withheld at source** (confidential Appendix A, `d16-c5`) |
| **G-4** | **The settlement Source Agency appendix is withheld at source** (confidential Appendix E, `d21-c11`) |
| **G-5** | **The entire academic corpus is undecided.** 528 records identified, **zero screened**. Tier 1 of the evidence hierarchy is empty in this record |
| **G-6** | **937 software artifacts are undecided.** No eligibility determination was made for any of them |
| **G-7** | **Venue-arm sampling, plus a count inconsistency.** 5 of 111 rule filings retrieved (or 4 — the log states both, **DI-6**); 1 of ~90 contract series specified; 34 further designated contract markets enumerated and unretrieved. **None of these enumerated-but-unretrieved objects is in `n_identified`**, and the flow is conditioned on that reading (section 5.1) |
| **G-8** | **The regulator's index mis-serves a document under this venue's label** (**DI-1**) |
| **G-9** | **The weather stratum's most on-point query never executed** across eleven attempts; 53 of 56 Semantic Scholar attempts returned HTTP 429; and the two RePEc queries in that same stratum (`ks-repec-04`, `ks-repec-04-b`) never executed either — see **G-26** and **DI-8**. *Extended 2026-09-04 by round-1 audit remediation (REV-1-1, LITERATURE-1-2, REPRODUCIBILITY-1-2); this row previously named Semantic Scholar only, which left RePEc non-execution in no gap row at all.* |
| **G-10** | **Novelty differencing is an upper bound**: the prior index covers 6,923 of 8,813 predecessor records |
| **G-11** | **Throughput is stated on four incompatible bases across the venue set and is not reconciled** (**DI-5**) |
| **G-12** | **Two venue pages state different collateral interest rates** (**DI-4**) |
| **G-13** | **The software G1 enumeration is two rows short of its own arithmetic** (**DI-2**) |
| **G-14** | **Instrument verification depth.** The pre-freeze `literature-check` session returned `proceed-with-remediation`: PDF extraction was unavailable and seven publishers returned HTTP 403, so instruments 1-5 were verified at abstract or metadata depth and three sub-claims were corroborated only from search-index extraction, not from fetched primary text |
| **G-15** | **No included record carries a DOI, PMID, PMCID or arXiv id**, by ADR-0006 design. The research-compile gate's assertion **G13 (FAIR F1) cannot pass** for this artifact, and the gate verdict is therefore not `pass` (section 15) |
| **G-16** | **The unit of account is heterogeneous across arms.** The identity `sum(per-arm n_records) == n_identified` closes arithmetically over identifiers and not over comparable objects (section 5.1) |
| **G-17** | **The Maker Order Protections Program document was not retrieved**; `KSL-C25` rests on a practitioner's quotation of it at **secondary** depth, and its qualification criteria and delta are not stated |
| **G-18** | **The venue's Combos help article was not retrieved**; the source behind `KSL-C29` states that article is controlling |
| **G-19** | **Block threshold (contracts) and position limit (USD of exposure) are in different units and no document reconciles them** |
| **G-20** | **CME, Betfair and PredictIt rule surfaces were not retrieved** (HTTP 403, HTTP 403, and HTTP 200 client-rendered respectively); sportsbook house rules were not attempted |
| **G-21** | **Forum and community archives, podcast and conference transcripts, and paywalled trade press were not reached as distinct endpoints** by the lateral arm; whatever surfaced from them surfaced only through general web search on a single US-only index |
| **G-22** | **No code-level and no notebook search was executed**: GitHub `/search/code` and the Kaggle kernels endpoint both return HTTP 401 unauthenticated, and no account was created |
| **G-23** | **SEVEN bare numbers from sources are recorded verbatim and are not adoptable** (section 8), and one of them is a **chain citation whose underlying analysis was not retrieved**. *Was five. Extended 2026-09-04 by round-2 audit remediation (QUANT-2-5, LITERATURE-2-2) to add the two figures `ks-sc-002` states for its round-trip break-even: **10.7¢** at the 40-50¢ band and **2.6¢** at the tails. Both are README-depth with no derivation on the page, and the tail figure was DROPPED at extraction — see **DI-9**. Neither may set, cap, replace or bound any parameter in any consumer.* |
| **G-24** | **Grey-literature content drift is unmitigated.** No page in the S-E set is under version control by its publisher and several carry moving `dateModified` timestamps. The byte digest fixes the bytes, not the URL's future content |
| **G-29** | **The academic arm's known-item recall against the predecessor corpus is 4.3%** (14 of 327 predecessor `include` records identified). Published in full at `ks-known-item-recall.json` with both of its bounds — the seed-set question-mismatch between the two protocols, and the 6,923-of-8,813 novelty-index bound — and with the note that it is not a screening statistic. See head limitation 10. Added 2026-09-04 by round-2 audit remediation (CRITICAL-2-4, SCOPE-2-4, QUANT-2-3, LITERATURE-2-3) |
| **G-28** | ~~**The CSL-JSON store builder was never archived.** No script anywhere in the repository emits `references_kalshi-strategy-multivocal.json`; the store's construction is therefore not re-runnable.~~ **CLOSED 2026-09-04 BY RECOVERY, not by argument** (round-2 finding QUANT-2-4). The gap was WRONGLY REGISTERED: the builder existed in the executing session's scratchpad at the time G-28 was written, and a recoverable artifact was recorded as an unrecoverable gap. It is now archived at `ks-store-builder.py`, already carried its own `PYTHONHASHSEED=0` entry assert and repo-relative paths, and **re-running it regenerates `references_kalshi-strategy-multivocal.json` byte-for-byte identical** — sha256 `c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df`, 167,673 bytes, 99 entries. The superseded gap text is retained struck above. The CSL-JSON store is now the only artifact in this branch that is re-derivable end to end |
| **G-27** | **S-D and S-E retrieved bytes are NOT in this repository, so their `sha256_of_retrieved_bytes` values are ATTESTATIONS a reader cannot check.** `local_payload_name` in `ks-lateral-records.json` resolves to nothing here. The bytes existed in the executing session's untracked, ephemeral scratchpad, and the lead session hashed all 32 lateral payloads there on 2026-09-04 before it was cleared: **32 matched, 0 mismatched, 0 missing**, recorded at `ks-payload-digest-verification.json`. That makes the attestation VERIFIED-ONCE, not verifiable — it is a check the same project ran on bytes a reader cannot obtain, and it is strictly weaker than archiving. **The bytes were deliberately NOT archived**: they are third-party web pages and this repository is public, so copying their bodies in would be republication of other people's copyrighted material, which is a different act from recording a digest of what was read. Partial exception: 22 of the 78 rows in `ks-lateral-queries.json` digest `result_links` stored INLINE in that same file and are genuinely self-checkable; all 22 were recomputed and match. Added 2026-09-04 by round-1 audit remediation (REPRODUCIBILITY-1-6) |
| **G-26** | **RePEc was never searched.** All nine RePEc attempts (four queries plus five retries) returned HTTP 200 carrying the IDEAS/RePEc search **form**, not a result set; every log records `n_returned_semantics: "no search executed; not an observed zero-yield"`. The RePEc `n_records` of 0 in section 2 is an **interface failure, not a zero yield**, and no inference about RePEc's holdings — or about the economics literature it indexes — may be drawn from it. Added 2026-09-04 by round-1 audit remediation (REV-1-1, LITERATURE-1-2, REPRODUCIBILITY-1-2); see **DI-8** and `failure_log.md` **F007** |
| **G-25** | **No archived copy (web-archive snapshot) was created for any retrieved page.** The reference-rot literature the protocol cites supplies the archiving remedy; this branch recorded digests instead, which is a **project design choice with no cited source** (protocol section 12) |

### 12.2 `TO COMPUTE` handoffs

| id | parameter left uncomputed | selection procedure named |
|---|---|---|
| **TC-1** | Coherence-violation detection threshold, net of fees | Grid, random or Bayesian search over the threshold with a bootstrap CI on the resulting statistic; never a hand-set number |
| **TC-2** | Fee-inclusive break-even band **per series** | Derive from `d01-c2`/`d01-c4` with the per-series multiplier — **currently blocked by DI-3**; the multiplier table is in the bytes and not extractable |
| **TC-3** | Minimum tradeable gap for a cross-venue pair | Only after a settlement-clock and definition alignment test per `KSL-C14`; then a studentised time-series bootstrap for pairwise comparison ([Ledoit & Wolf 2008](https://doi.org/10.1016/j.jempfin.2008.03.002)), adopted by explicit reference under ADR-0004 |
| **TC-4** | Forecast-error distribution for a weather basis | Estimate from the **named settlement station's** own observation history with a bootstrap CI; the ≈2.7 °F in the source is its author's stated guess |
| **TC-5** | Achievable order rate | A function of API tier (`d06-c1`–`d06-c6`), which is **endogenous to the participant's trailing volume share** and to total exchange volume; must be stated per tier and never as a venue constant |
| **TC-6** | Capacity ceiling per contract | Read from each contract's filed terms and conditions (`d17-c2`), which is why it is per contract and not per venue; the elevated market-maker levels are unreachable without **G-2** |
| **TC-7** | The competitive quoting floor a non-programme quoter faces | **Not computable from any public document** (**G-2**). Lawful substitute: an MDES for detecting a difference against a stated alternative — never retrospective power (project charter) |
| **TC-8** | Universe-construction filter separating single-outcome markets from auto-generated combinations | Derive from the venue's own series/event schema and validate against settled-market outcomes; `KSL-C30` states the requirement and no rule |
| **TC-9** | Polling interval for any replication of a market-data capture | Justified against the venue's stated rate limits and the autocorrelation of the quote process |
| **TC-10** | Price band at which a taker round trip is viable | Derived from the stated fee function and a **measured** spread distribution |
| **TC-11** | The NO-probability threshold defining `ks-sc-001`'s candidate | Grid or cross-validated search with a bootstrap CI |
| **TC-12** | Minimum sample size for any decision rule | **Minimum detectable effect size, never retrospective power** (project charter) |
| **TC-13** | Eligibility for the 1,465 undecided G1 rows | A later session decides them **as a numbered amendment stating the subset rule it applied, fixing that rule BEFORE any record in the subset is assessed** (protocol section 4.4 rule 4) |
| **TC-14** | Family-wise error control across strategy classes tested | [White 2000](https://doi.org/10.1111/1468-0262.00152) reality check or [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA, adopted by explicit reference under ADR-0004 |
| **TC-15** | Standard errors for any time-indexed estimate built on this corpus | Newey–West HAC with a data-dependent bandwidth ([Newey & West 1994](https://doi.org/10.2307/2297912)) or the [Andrews 1991](https://doi.org/10.2307/2938229) plug-in, adopted by explicit reference under ADR-0004 |

---

## 13. What this record does NOT claim

Consistent with frozen protocol section 8, and enumerated so that section 8's
list is not read as a blanket disclaimer.

**13.1 The standard split, restated because it is the most misreadable thing
here.** PRISMA-S applies **on its own terms** and its use is neither adapted nor
analogical — the terminology clause quoted in `standard_declared` is an explicit
self-endorsement for all fields and disciplines and for the whole family of
evidence syntheses including scoping reviews and evidence maps. **PRISMA 2020
does not reach this record**, its own scope statement extends only to systematic
reviews, and **every PRISMA 2020 item invoked anywhere in this file — items 8 and
16b, and the item numbers in the table below — is reasoning by analogy with no
cited endorsement.** No compliance with PRISMA 2020 is claimed anywhere in this
branch. PRISMA-ScR is cited as a checklist reference **with its
EQUATOR-developed health framing declared**, and **no claim of PRISMA-ScR
compliance is made**.

**13.2 Nineteen PRISMA 2020 items this design does not meet, by analogy.** Four
design facts drive all of them: screening is **single-pass by one agent with an
LLM as the automation tool**; extraction is **single-extractor**; **no validated
risk-of-bias instrument** is applied to any record; and the search strategies
received **no independent information-specialist peer review**.

Items **1, 2, 8, 9, 11, 13b, 13c, 13d, 13e, 13f, 14, 15, 18, 19, 20b, 20c, 20d,
21, 22** are unmet. Item **12** (effect measures) is **inapplicable with
rationale**, not unmet by omission: this corpus's objects are stated strategies,
preconditions and heterogeneously-reported outcomes, not effect measures for a
common outcome, so no effect measure is chosen because none exists to choose.
Of item 8, the automation-tool declaration **is** met (section 5.3); the
dual-independence half is not.

**13.3 And what may not be said.** This record, the branch agenda and every
downstream artifact must **not** describe this work as a systematic review, must
**not** report an inter-rater agreement statistic, must **not** report a
certainty-of-evidence grade, must **not** present the absence of a risk-of-bias
table as an oversight rather than a declared design limit, must **not** claim
PRISMA 2020 or PRISMA-ScR compliance, must **not** band or rank grey sources, and
must **not** claim completeness of any arm.

**13.4 Grey-source credibility is recorded and never used to stratify.** Protocol
field F15 records **outlet control** and **expertise** per S-C/S-D/S-E record in
that record's own observable terms, following Adams, Smart & Huff 2017
(doi:10.1111/ijmr.12102) — whose scheme states the gradation "is on a continuous
range between known and unknown", so **no tier, no band and no rank is assigned
anywhere**, and neither attribute entered any inclusion or exclusion decision.
Every record here was admitted on N1-N6 alone. Use of that scheme here is a
**declared transfer**: its field is management and organizational studies.
Likewise the multivocal-review guidance the protocol names scopes **itself** to
software engineering, and the repository-mining literature documents hazards and
**supplies no completeness bound**, so none is attributed to it.

**13.5 No strategy in this record is asserted to be executable, profitable, or
permitted.** Several sources state jurisdictional restrictions that were not
independently checked. The corpus states what sources state.

**13.6 Nothing here is a tradeable rule.** No position size, no expected return,
no edge, no implied probability, no Sharpe ratio and no fitted parameter appears
anywhere in this record. Where a source stated a position-sizing rule
(`KSL-C27`'s README), it was deliberately **not reproduced** by the arm and is
not reproduced here.

---

## 14. Bibliography store

<!-- bibliography-store -->
- **Store:** `docs/literature/references_kalshi-strategy-multivocal.json`
  (CSL-JSON, canonical serialization: `indent=2`, `sort_keys=True`,
  UTF-8, trailing newline, written in binary mode so that Windows text-mode CRLF
  translation cannot move the digest)
- **SHA-256:** `c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df` — equals frontmatter `bibliography_sha256`
- **Entries:** **99**, equal to `n_included`. **The identity `len(store) ==
  n_included` CLOSES**; the predecessor branch's gap AG-11 is not repeated.
- **Composition:** 40 `software` entries from the software arm, 28 venue and
  regulator entries (`report`, `webpage`, `regulation`), 31 lateral entries
  (`post-weblog`, `webpage`, `software`).

**S-C entries carry repository URL, commit-or-release identifier, and access
date**, per software citation principle 6 (specificity): *"Software citations
should facilitate identification of, and access to, the specific version of
software that was used. Software identification should be as specific as
necessary, such as using version numbers, revision numbers, or variants such as
platforms."* — Smith AM, Katz DS, Niemeyer KE, **FORCE11 Software Citation
Working Group**. *Software citation principles.* PeerJ Computer Science.
2016;2:e86. https://doi.org/10.7717/peerj-cs.86. **The FORCE11 Software Citation
Working Group is a NAMED AUTHOR on that record and is named here**; omitting it
misstates the author list. Where no persistent identifier exists the principles
permit a repository-URL-plus-commit fallback, which is what every S-C entry uses.

**The choice of CSL-JSON as the carrier, and the exact field names used
(`accessed`, `version`, `custom`), is a PROJECT DESIGN CHOICE attributable to the
Citation Style Language 1.0.2 specification and NOT to the software-citation
principles, which say nothing about CSL-JSON.** Recorded in protocol section 12
and repeated here so the attribution cannot drift.

**`webpage`, `report` and `regulation` entries for S-D documents carry the access
date and the SHA-256 of the retrieved bytes** in the entry `note` and in
`custom.sha256_of_retrieved_bytes`. **The byte digest is itself a project design
choice with no cited source** (protocol section 12): the reference-rot literature
establishes the hazard and prescribes archiving, not digesting.

**Three properties of this store that a reader must not mistake for defects:**

1. **No entry carries a DOI, PMID, PMCID or arXiv id.** That is ADR-0006's
   decisive departure, not an omission (limitation 8, gap **G-15**).
2. **It is a RECORD store, not a document store.** Where the lateral arm's unit
   (a strategy class) is finer than a document, two entries share a URL and a
   byte digest — for example `KSL-C02`/`KSL-C03` and
   `KSL-C23`/`KSL-C24`/`KSL-C25`. That is required for `len(store) ==
   n_included` to mean anything, given the declared unit of account.
3. **For lateral entries the `title` field carries this corpus's strategy-class
   name, not the source document's title**, because the arm log records no
   document title for those sources and inferring one from a URL slug would be
   fabrication. Every such entry says so in its own `note` under `TITLE BASIS`.

Derived exports are regenerable and are never a source of truth:
`python ~/.claude/scripts/build_bibliography.py export <store> --format bibtex|ris`.

---

## 15. Limitations and verification gaps

The ten limitations at the head of this document are the ones a reader must
carry into every number. This section records what could **not be verified**, in
the terms the research-compile skill requires — an unstated gap is
indistinguishable from a claim of completeness.

1. **The research-compile gate does not return `pass` for this artifact, and
   cannot.** Assertion **G13** requires a DOI, PMID, PMCID or arXiv id on every
   store entry (FAIR F1). **No entry has one, by ADR-0006 design** — that
   decision, its rejected alternatives and its reversal cost are recorded in
   ADR-0006, and the standing findability gap it buys is limitation 8. The gate's
   verdict is reported verbatim by the compiling session rather than worked
   around, and **success is not claimed on a non-`pass` verdict.** No other gate
   assertion is knowingly unmet: G14 closes at 99 == 99, G15 closes on the
   canonical digest, G9's three identities close, and G18 finds no OS username,
   no email address and no absolute home-directory path in either file.
2. **No DOI resolution was required or performed for this corpus**, because it
   contains no DOI. The instrument DOIs cited in `standard_declared` and in
   sections 13 and 14 were resolved and verified **before the protocol froze** by
   a separate `literature-check` session, at the depths that session records; its
   own environment gap is **G-14** and its verdict was
   `proceed-with-remediation`, not `pass`.
3. **Paywalled and blocked full text.** SSRN (HTTP 403), CME (HTTP 403 even on
   `robots.txt`), Betfair (HTTP 403), investing.com (HTTP 403), one venue help
   article (HTTP 404), and one lateral candidate behind a vendor paywall. Each is
   logged with its status in the arm query logs.
4. **Client-rendered surfaces that return HTTP 200 with no content.** The venue
   rulebook page, its notices page, its pending-fee-change page, its
   contract-drafts page, the paired venue's rulebook route, and PredictIt's rules
   page. **HTTP 200 is not retrieval**, and this record treats those as
   retrieval failures, never as evidence of absence.
5. **PDFs with no text layer.** The 2025 Market Maker Program schedules
   (`KS-VR-Q45`, `KS-VR-Q46`) were retrieved as PDFs with no extractable text and
   are not in the corpus.
6. **Rate-limited endpoints.** Semantic Scholar returned HTTP 429 on 53 of 56
   attempts and HTTP 500 on one (**G-9**); GitHub's unauthenticated REST core
   limit is 60 requests/hour and its search limit 10/minute, which bounds the
   software arm's harvest.
7. **Non-English records were not translated**, and none was excluded for
   language: no language limit was applied and none of the retrieved records
   required translation to be dispositioned at the depth reached.
8. **Every verdict and every extraction in this corpus is a single-pass LLM
   output with no archived prompt and no recoverable sampling parameters.** A
   re-run is not guaranteed to reproduce them. `PYTHONHASHSEED=0` pins the
   deterministic halves — deduplication, branching, ordering, serialization — and
   nothing else.
9. **The full gap list is section 12.1 (`G-1` … `G-29`, with `G-28` closed by recovery) and the full handoff list
   is section 12.2 (`TC-1` … `TC-15`).** They are numbered because the branch
   agenda consumes them by identifier, and a branch derived from anything else
   would not be traceable to this record.
