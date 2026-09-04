---
type: research_agenda
slug: prediction-market-microstructure
branch: kalshi-arbitrage / prediction-market microstructure
date: 2026-09-02
status: open
revision: 3
revision_note: >
  Rev 3 (2026-09-04) opens FIVE new branches -- 7, 8, 9, 10 and 11 -- and every one
  of them is derived from a NAMED gap MV-G-n or `TO COMPUTE` handoff MV-TC-n in the
  2026-09-04 multivocal corpus record, citing that identifier at its head. Nothing in
  rev 3 is derived from model recall, from the author's sense of what would be
  interesting, or from any citation the multivocal corpus record, its arm logs and
  ks-instrument-verification.json do not already carry. A branch derived from
  anything else would be a defect: that is the rule rev 1 was written under and it
  still binds.

  WHAT REV 3 CORRECTS IN REV 2 -- two corrections, both running AGAINST rev 2's own
  statements, which is the direction that matters for a document now asserting
  something different from what it asserted yesterday. (1) BRANCH 0's precondition
  status is PARTLY DISCHARGED, and rev 2's sentence "every fact this branch needs is
  still unretrieved" is FALSE as of 2026-09-04. The multivocal branch's venue arm
  retrieved, at full text of the retrieved bytes, most of Branch 0's list: the fee
  schedule and its functional form (d01-c1..d01-c7), a second unmodelled rounding-fee
  component (d08-c1..d08-c4), minimum tick and settlement value on the one series
  specified at that depth (d21-c3, d21-c4), full cash collateralisation (d13-c2,
  d14-c2), netting (d07-c1), the position-limit regime and its 2023 and 2024 changes
  (d16, d17), the block-trade route (d20-c1, d20-c3), the token-bucket throughput
  document (d06-c1..d06-c9), and the EXISTENCE of a market-maker programme (d19).
  What remains open is a different KIND of thing from what rev 2 described: the
  rulebook in force is NOT LOCATED (MV-G-1), while the market-maker selection procedure
  and the Market Maker Agreement (MV-G-2), the schedule of contracts carrying elevated
  position limits (MV-G-3) and the settlement Source Agency appendix (MV-G-4) are
  WITHHELD AT SOURCE under a confidentiality right, and the per-series fee multipliers
  are in the retrieved bytes and NOT EXTRACTABLE (DI-3, blocking MV-TC-2). More
  searching closes the first class and CANNOT close the second. Branch 0 stays open and
  its content changes.

  (2) HAZARD H-4 is PARTLY SUPERSEDED. Rev 2 states the corpus "can say neither that
  the venue is order-driven nor that it is quote-driven" and that no branch may
  assume either. The multivocal corpus's section 9.1 states, from clauses d20-c1 and
  d20-c3 read at full text, that the default block minimum is 25,000 contracts
  restricted to eligible contract participants and that BELOW IT EVERY ORDER MUST
  INTERACT WITH THE CENTRAL LIMIT ORDER BOOK; the same section states from d04-c4 and
  d03-c4 that customers trade peer-to-peer, the venue never takes the other side, and
  every trade is published publicly. A PURE QUOTE-DRIVEN DEALERSHIP READING IS
  THEREFORE EXCLUDED FOR SUB-BLOCK ORDER FLOW BY A VENUE FILING. A hybrid is NOT
  excluded; the statement is bounded to the retrieved filings, of which five (or four
  -- the venue arm's log states both, DI-6) of 111 enumerated rule filings were
  retrieved; and the rulebook in force is still not located (MV-G-1). The correction
  makes Branch 2b HARDER, not easier: Glosten & Milgrom's binding conditions are pure
  dealership, unit trades and no limit orders, and a CLOB statement runs against the
  first and third of those. The supersession block sits under the hazards, and H-4's
  own text is left standing rather than reworded.

  (3) CORRECTED 2026-09-04, audit finding REV-1-3 -- AN IDENTIFIER-SPACE COLLISION,
  now declared and swept. Rev 3 consumes gap and handoff identifiers from TWO corpus
  records whose identifier spaces COLLIDE: the predecessor corpus supplies G-1..G-10
  and TC-1..TC-5, which branches 1-6 consume, and the 2026-09-04 multivocal corpus
  supplies ~~G-1..G-25~~ G-1..G-28 and TC-1..TC-15, which branches 7-11 consume. (The
  struck range is rev 3's wording as first written and is retained legible; the range
  moved to G-28 by round-1 remediation of the multivocal corpus record on 2026-09-04
  -- see item (4) below.) A bare "G-9" or
  "TC-3" was therefore AMBIGUOUS in this document and resolved to two different
  objects -- the collision was real and was nowhere declared. Rev 3 as first written
  used bare identifiers for BOTH corpora; that is corrected here. THE FIX IS
  AGENDA-LOCAL AND RENUMBERS NOTHING: every reference to the multivocal corpus now
  carries the prefix MV- (MV-G-n, MV-TC-n) and the predecessor's bare G-n / TC-n are
  left exactly as they were. The convention is stated once under "How to read this
  document" and every bare multivocal identifier in the body -- front matter, hazards
  H-6..H-9, the H-3/H-4 supersession block, Branch 0's rev-3 debt table, Branch 1's
  rev-3 note, Branch 6's rev-3 extension, branches 7-11 in full, the H001 section, the
  cross-branch questions and the verification status -- has been swept to the prefixed
  form. NEITHER corpus record is edited by this correction; the prefix lives in this
  agenda only. No branch derivation is orphaned: every branch still names the gap or
  handoff it comes from, in the corpus-correct form.

  (4) CORRECTED 2026-09-04, audit findings CRITICAL-2-3 / SCOPE-2-7 -- THE MULTIVOCAL
  GAP RANGE MOVED, AND EVERY RANGE DECLARATION IN THIS DOCUMENT WAS STALE. Rev 3 as
  first written declared the multivocal corpus's gap range as ~~G-1..G-25~~ in four
  places: this note, the corpus_multivocal front-matter field, "How to read this
  document", and the verification-status collision bullet. The struck range is retained
  legible everywhere because it was true when it was written. Round-1 remediation of
  that corpus record, on 2026-09-04, ADDED THREE GAPS, so the sole admissible source
  range for branches 7-11 is now G-1..G-28, cited in this agenda as MV-G-1..MV-G-28:

  -- MV-G-26: REPEC WAS NEVER SEARCHED. All nine attempts were served the search form
  rather than a result set, so no RePEc row is a search result and none may be scored
  as "states nothing". Cited at this agenda's own RePEc statement in Branch 6's rev-3
  extension, alongside MV-G-9 and MV-G-22.

  -- MV-G-27: THE S-D AND S-E RETRIEVED BYTES ARE NOT ARCHIVED, so their sha256 values
  are ATTESTATIONS A READER CANNOT CHECK. The corpus lead verified all 32 lateral
  payload digests ONCE against an ephemeral scratchpad and all 32 matched, which makes
  them VERIFIED-ONCE, NOT VERIFIABLE; the bytes were deliberately not copied in because
  they are third-party pages and this repository is public. THIS IS AN EVIDENCE-POSTURE
  CHANGE AND NOT BOOKKEEPING, because this agenda cites INTO ks-lateral-records.json at
  load-bearing points (KSL-C09, KSL-C14, KSL-C15, KSL-C16, KSL-C30, KSL-C32). It is
  therefore carried as standing hazard H-10 and in the verification status, not left in
  the front matter.

  -- MV-G-28: the CSL-JSON store builder was never archived. ~~REGISTERED, AND UNDER
  REVISION BY THE LEAD AT TIME OF WRITING -- it may be downgraded or closed.~~
  **RESOLVED 2026-09-04, LATER THE SAME DAY: MV-G-28 IS CLOSED BY RECOVERY, and the
  gap should never have been registered.** Round-2 audit finding QUANT-2-4
  established that the builder EXISTED when the gap was written, in the same
  executing-session scratchpad from which fifteen other scripts had just been
  archived; a recoverable artifact had been recorded as a permanent one. It is now
  archived at `ks-store-builder.py` and re-running it regenerates
  `references_kalshi-strategy-multivocal.json` BYTE-FOR-BYTE IDENTICAL (sha256
  `c7545d31...`, 167,673 bytes, 99 entries), which makes the CSL-JSON store the only
  artifact in that branch re-derivable end to end. Recorded here rather than silently
  dropped because the lesson generalises and this agenda is where a later reader
  looks: **registering a gap is a claim about the world and carries the same evidence
  burden as any other claim.** No branch below is derived from MV-G-28, and none
  should be.

  NEITHER CORPUS RECORD IS EDITED OR RENUMBERED by this correction; the MV- prefix
  remains agenda-local. NO BRANCH DERIVATION IS ORPHANED and no branch is added:
  MV-G-26 and MV-G-27 bound claims branches 6-11 already make, and MV-G-28 is carried
  as registered-and-in-revision only.

  Rev 3 changes NO branch 1-6 test, NO verdict and NO count, and withdraws nothing.
  It adds branches 7-11, hazards H-6..H-9, the H-4 supersession block, an H001
  cross-reference section, and seven agenda-local `TO COMPUTE` items labelled
  A3-TC-1..A3-TC-7 so that they can never be confused with the multivocal corpus's own
  MV-TC-1..MV-TC-15. Four nulls this session encountered are registered in
  failure_log.md as F006-F009 under the charter's negative-result protocol and are
  NOT restated as branches here.

  Rev 2 (2026-09-03) re-grounds the S4-derived branches on the full-text evidence
  produced by protocol amendment A17, after amendment A16 took the corpus from 149
  to 327 records. Branch 2's motivating premise is CORRECTED, not merely updated:
  TWO of the five records it named as "named-lineage anchors" whose monotone
  inventory result must be re-derived turn out not to be inventory-control models at
  all -- Glosten & Milgrom and Kyle. [corpus-inference] FOR THE KYLE HALF, and the
  two halves do not rest on the same kind of evidence: Glosten & Milgrom is
  established from the authors' own footnote on binding inventory constraints and the
  zero-profit condition; Kyle is established over pp. 1315-1317 only, read as page
  images, as an INFERENCE FROM ABSENCE -- Kyle states no inventory objective and
  states no absence of one either, and the remaining pages of the article were not
  read. Marker added 2026-09-04, finding QUANT-2-3; the corpus record's section 8.4
  legend defines [corpus-inference] as a step this corpus takes from something an
  author states to something the author does not state, and this field is the one a
  tool reads. Corrected 2026-09-03, audit finding QUANT-1-4:
  this note said "three of the five", which the body does not establish and cannot.
  The other three named anchors are Ho & Stoll, unread at any depth, and Krishnan
  1992 and Liu & Wang 2016, both [meta] in the corpus -- so "on their own texts" is
  false of any third candidate. See the supersession markers in Branch 2. Every
  S4-derived claim below now cites a record at a stated depth, and where that depth
  is an abstract the claim says so. Nothing here is derived from model recall.
  Rev 1 (2026-09-02) opens the branch agenda declared by
  deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C item 6.
  Written under audit finding SCOPE-2-3, which recorded that the spec-declared
  agenda did not exist anywhere in the repository although the corpus record's
  section 10 gaps (G-1…G-10) and section 11 TO COMPUTE handoffs (TC-1…TC-5) --
  THE PREDECESSOR CORPUS'S OWN IDENTIFIERS, carried bare throughout this document
  per the prefix convention -- had
  been written as its input. Every branch below is derived from a named gap or
  handoff; nothing here is derived from model recall.
corpus: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md  # 327 records after amendment A16 (149 before); compiled corpus record, NOT a systematic review. 33 records read at full text under A17; the other 294 were not. The CSL-JSON store still covers only 149 (AG-11). Its gaps G-1..G-10 and handoffs TC-1..TC-5 are cited BARE in this agenda. BOUNDED (added 2026-09-04, finding REV-2-1): 327 = 149 + 178 and 178 is an UPPER bound -- the bar A16 applied was the negation of X6, not the section 2.2 transfer clause's conjunction, so the transfer-clause-admitted set lies in [0, 178] and the corpus size is conditioned at [149, 327] (A18 sections (c)-(d); corpus record section 8.4.4). A READER MUST NOT READ 178 AS THE COUNT OF RECORDS THE TRANSFER CLAUSE ADMITS. No claim line in the corpus record's section 8 rests on any of the 178, so no claim this agenda draws from it inherits the interval
corpus_multivocal: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md  # ADDED AT REV 3, and it is a SECOND corpus, not a replacement: it answers a different question (what strategies does the retrievable multivocal record STATE) on a different source population (venue and regulator filings, public code, practitioner pages), and its gaps ~~G-1..G-25~~ G-1..G-28 -- RANGE EXTENDED 2026-09-04 by round-1 remediation of that record, which added G-26 (RePEc never searched), G-27 (S-D/S-E bytes not archived, digests attested not verifiable) and G-28 (CSL-JSON store builder never archived -- SINCE CLOSED BY RECOVERY on 2026-09-04, round-2 finding QUANT-2-4: the builder existed all along, is archived at ks-store-builder.py, and regenerates the store byte-for-byte); struck range retained legible, findings CRITICAL-2-3 / SCOPE-2-7 -- and handoffs TC-1..TC-15 -- CITED IN THIS AGENDA AS MV-G-1..MV-G-28 AND MV-TC-1..MV-TC-15 because they collide with the predecessor's, finding REV-1-3 -- are the sole admissible source of branches 7-11. Compiled corpus record produced by a registered multivocal search; NOT a systematic review; NO risk-of-bias table (declared design limit); NO inter-rater statistic (one screener); NO certainty grade
corpus_multivocal_unit_of_account: >
  THE DISPOSITIONED RECORD, AND THE UNIT IS NOT HOMOGENEOUS ACROSS ARMS. No count
  below is readable without this sentence. The ACADEMIC arm's record is one
  bibliographic row; the SOFTWARE arm's is one public code or package artifact keyed
  by host plus full name; the VENUE arm's is one retrieved document with a byte
  digest, which may carry many clauses; the LATERAL arm's is one sourced STRATEGY
  CLASS, and two classes may share one retrieved payload. Software rows and lateral
  rows are NOT commensurable objects and their sum means nothing outside the corpus
  record's own flow identities, which are arithmetic over identifiers rather than
  over comparable things (corpus gap MV-G-16). Any branch below that cites a count
  cites it as an identifier count and never as a count of comparable objects.
corpus_multivocal_flow: >
  n_identified 1,986; n_duplicates_removed 412; n_screened 1,574; n_excluded 1,475,
  of which n_criterion_excluded 10 (Y-code rows only: Y2 3, Y3 5, Y4 1, Y9 1) and
  n_capacity_gap 1,465 (G1 rows only -- 528 academic plus 937 software; G2 = 0);
  n_included 99. THE 1,465 ARE UNDECIDED, NOT INELIGIBLE: no eligibility
  determination under N1-N6 was ever made for any of them, and they sit inside
  n_excluded only so the flow identities close. All 109 records that received any
  verdict were read-based; NO keyword classifier assigned any verdict in that
  corpus. The bibliography store covers 99, equalling n_included.
corpus_multivocal_gate: >
  THE MULTIVOCAL CORPUS'S OWN RESEARCH-COMPILE GATE RETURNS `block`, BY DESIGN, ON
  FAIR F1 (gate assertion G13). NO included record in it carries a DOI, PMID, PMCID
  or arXiv id -- ADR-0006 deliberately dropped the persistent-identifier requirement
  so that venue filings, regulator documents, code artifacts and practitioner pages
  could enter at all, and every locator is consequently a URL subject to link rot and
  content drift (corpus gap MV-G-15, with MV-G-24 for the drift and MV-G-25 for the
  absence of any web-archive snapshot). The SHA-256 recorded per record fixes the
  BYTES, not the URL's future content -- and for the S-D and S-E arms those bytes are
  NOT ARCHIVED, so the recorded digest is an ATTESTATION rather than a value a reader
  can recompute (MV-G-27, added 2026-09-04; hazard H-10). A `block` verdict here is a
  declared consequence of a recorded decision, not an unremediated defect, and it is
  stated in the front matter so that no successor reports the gate as passing.
corpus_multivocal_protocol: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md  # frozen-prefix sha256 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac over the first 91,498 bytes; ONE append-only amendment M1, which alters no eligibility criterion, no contribution code, no extraction field, no taxonomy class, no screening rule and no arithmetic identity, and every record reached only via M1 is a G1 row whose eligibility was never decided -- so no inclusion rests on it. Registration event: provenance commit 4821611c1c93b5f929a76f3ba6207e900440cee5, committed before the first query of any arm executed
corpus_multivocal_bibliography: docs/literature/references_kalshi-strategy-multivocal.json  # sha256 c7545d314e6c1af0d98266b22f4c4c5970e0eefc698a88a142511c6491aa51df; 99 entries, equal to n_included
corpus_multivocal_search_logs: docs/literature/search_logs/kalshi-strategy-multivocal  # the arm logs, the per-query stored responses and payloads, and ks-instrument-verification.json. Every quotation in branches 7-11 traces to a stored response in this directory. BOUNDED (added 2026-09-04, findings CRITICAL-2-3 / SCOPE-2-7): the S-D and S-E payload BYTES are not archived here, so their digests are attestations verified once by the lead and not recomputable by a reader (MV-G-27, hazard H-10)
corpus_extraction_log: docs/literature/search_logs/kalshi-arbitrage/ka-s4-fulltext-extraction.jsonl  # sha256 b7970a22c93430b69e30344737c2f8fa0f003a2f7c029545b77f8e6990ee902a
corpus_completion_screen: docs/literature/search_logs/kalshi-arbitrage/ka-s4-completion-screen.jsonl  # sha256 8e25fa353dad315c10a7734c0e1c5a627a305b7f1fd05ab1d34406d940ef8848
protocol: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md  # frozen prefix sha256 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4 (first 82,677 bytes, unchanged and re-verified 2026-09-03); with addendum A1-A19 sha256 7f49fdaf8cab08b2d6484ff7258c906f492fbf9cb5262b934e2c83717fe3ac18 (206,123 bytes), superseding the A1-A18 value dcfae5643ff86e49bbcf33a68e730fcb9d7f46b41f30cbd62bafdd297c3fc4dc (183,534 bytes), the A1-A17 value e93e01516f840a2f9adc2f319f128c4d13403281005fea42037b46790c1b3982 (160,105 bytes) and the A1-A15 value 21a77d10841ba7f15ea58d5a58a1bca57818b2ed1a0f3bf53a1dbce6a8dcc53b. A18 (2026-09-03, round-4 audit remediation) changes no verdict and no count; it strikes A17's false four-moved claim, declares the subset rule's pre-fixing self-attested, and records that 178 is an upper bound. A19 (2026-09-04, round-5 audit remediation) changes no verdict, no transfer status and no count; it publishes the quotation audit that re-checked 231 quoted spans against 33 re-retrieved sources and corrects the seven that were altered, records the operative reading of field E10, carries the [corpus-inference] marker for the Kyle half of A18 (g), and publishes the post-A18 digest A18 promised. This front-matter field is one of the four carriers of record for the whole-file value, which A19 (e) explains cannot be written inside the protocol itself
bibliography: docs/literature/references_kalshi-arbitrage.json  # sha256 fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164 -- UNCHANGED and now covering only 149 of the corpus's 327 records (corpus gap AG-11). Identifiers for the other 178 are in corpus_completion_screen
governing_decisions:
  - docs/decisions/ADR-0003-specification-not-execution.md   # castles specifies; it does not execute
  - docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md  # rules/quant-project.md + REVIEW.md adopted for this branch only
  - docs/decisions/ADR-0006-multivocal-scope-for-strategy-corpus.md  # ADDED AT REV 3; the decision that admits non-identifier-bearing sources and thereby produces gap MV-G-15
related_specifications:
  - research/01_hypothesis_register/H001/design.md   # DRAFT, NOT FROZEN. See section "Relationship to H001" below
scope_boundary: >
  This document SPECIFIES tests. It runs none of them. No branch below acquires
  Kalshi market data, calls an exchange API, fits a model, backtests, or states a
  tradeable rule (ADR-0003, ADR-0004 §Boundary). Every parameter that an executing
  project would have to choose is left `TO COMPUTE` with the selection procedure
  named, never a bare number (CLAUDE.md §Parameter & Prompt Selection).
  RESTATED AT REV 3 BECAUSE BRANCHES 7-11 ARE CLOSER TO THE MONEY THAN BRANCHES 1-6
  WERE: no branch below states a tradeable rule, a position size, or an expected
  return. Branch 7 returns executability VERDICTS, never a gap value; Branch 9
  returns an alignment verdict, never a spread; Branch 10 returns a lag distribution
  and a carry-rate SENSITIVITY RANGE, never a cost of carry to be netted into a
  return; Branch 11 returns a contradiction set, never an achievable order rate.
---

# Research agenda — prediction-market microstructure (Kalshi branch)

**Question.** For a regulated binary event-contract venue, which of the
no-arbitrage/coherence conditions, systematic mispricings, and market-making
results established on *other* venues and for *unbounded* payoffs actually transfer
— and under which stated, checkable preconditions?

## How to read this document

**Identifier convention — read this first, because TWO corpora with COLLIDING
identifier spaces are cited below (stated once, finding REV-1-3, 2026-09-04).**
This agenda draws on two corpus records. The **predecessor** corpus,
`lit_review_kalshi-arbitrage_2026-09-02.md`, names gaps **G-1…G-10** and handoffs
**TC-1…TC-5**, and **branches 1–6** derive from those. The **multivocal** corpus,
`lit_review_kalshi-strategy-multivocal_2026-09-04.md`, names gaps ~~**G-1…G-25**~~
**G-1…G-28** *(range extended 2026-09-04 by round-1 remediation of that corpus record,
findings **CRITICAL-2-3** / **SCOPE-2-7**; the struck range is this section's wording as
first written and is retained legible — see the rev-3 range correction in the front
matter, item (4), and in the verification status)* and
handoffs **TC-1…TC-15**, and **branches 7–11** derive from those. **The two
numbering spaces overlap, so a bare `G-9` or `TC-3` would be ambiguous and would
resolve to two different objects.** Therefore, throughout this document:

- **`G-n` and `TC-n`, bare, always mean the PREDECESSOR corpus.**
- **`MV-G-n` and `MV-TC-n` always mean the MULTIVOCAL corpus.**
- **`A3-TC-n` means an agenda-local `TO COMPUTE` item created by rev 3**, belonging
  to neither corpus.

**The `MV-` prefix is agenda-local and renumbers nothing.** Neither corpus record is
edited by this convention, and each keeps its own bare numbering internally; a
reader following a citation into the multivocal corpus looks up `MV-G-12` as its
`G-12`. Defect ids (`DI-n`), predecessor auxiliary gaps (`AG-n`), corpus clause ids
(`d01-c1`, `KSL-C14`) and hazards (`H-n`) are unaffected — none of them collides.

Each branch states: the **gap or handoff it comes from**, the **claim at issue**,
one **falsification test** (H0, statistic, comparison/surrogate, refutation
condition, unit of analysis), the **evidence tier** the branch currently stands on,
and its **preconditions**. A branch is *complete* when its test is fully specified,
not when it has been run (ADR-0003 §Consequences).

**What counts as a falsification test here, stated because the 2026-08-21 agendas
got this wrong and the spec names the defect explicitly.** A falsification test
must be a statement about the *world* that the branch's own claim forbids, with a
statistic and a refutation condition attached. **These do not count and are not
written as tests below:** a *design-resolution study* (choosing between two
implementations), a *precondition* (retrieving a document the test needs), and an
*adoption policy* (deciding to use a convention). Where a branch needs one of
those, it is listed under **Preconditions**, never under **Falsification test**.
Branch 0 is a retrieval task and is therefore stated as a precondition branch with
**no** falsification test, and says so.

**Branch count, stated so the spec check is unambiguous. Restated at rev 2.**
**Seven research branches — 1, 2, 2b, 3, 4, 5, 6 — each carrying exactly one
falsification test**, plus **one precondition branch, Branch 0, carrying none by
design**. **Branch 2b is new at rev 2**: the full texts showed that two records rev 1
had filed under Branch 2 are **adverse-selection models** -- Glosten & Milgrom by
their own footnote on binding inventory constraints, Kyle by this corpus's reading of
the specification over pp. 1315-1317, the only pages read, which is an inference from
absence **[corpus-inference]** -- so their transfer question is a different question
and now has its own branch rather than being lost. *(Marker added 2026-09-04,
findings **REV-2-3** and **LITERATURE-2-4**: this sentence said "adverse-selection
models with no inventory objective" as established fact. "Adverse-selection models"
is author-supportable for both; "no inventory objective" is not, for Kyle.)* Rev 1 had six research branches. Branch 0 is numbered
because four other branches are blocked on it and a reader needs a name for the
blocker; it is not counted as a research branch and no test is claimed for it.

**Branch count, restated at rev 3.** **Twelve research branches — 1, 2, 2b, 3, 4,
5, 6, 7, 8, 9, 10, 11 — each carrying exactly one falsification test**, plus
**Branch 0, still the only precondition branch and still carrying no test by
design**. **Branches 7, 8, 9, 10 and 11 are new at rev 3** and each is derived from
a named gap or handoff in the 2026-09-04 multivocal corpus record, cited at its
head: Branch 7 from **MV-G-2, MV-G-3, MV-G-4** (the withheld-at-source set); Branch
8 from **MV-G-1**, with **MV-G-24** and **MV-G-25**; Branch 9 from **MV-TC-3** and
**MV-G-20**; Branch 10 from **MV-G-12** and **MV-TC-12**; Branch 11 from **MV-G-11**
and **MV-TC-5**, with **MV-G-19**.
Branch 8 is the one that most resembles a retrieval task and it is written with an
explicit paragraph on why it is not one; if that paragraph does not convince a
reviewer, the correct disposition is to demote Branch 8 to a second precondition
branch, not to keep it as a test.

**Evidence tiers** are CLAUDE.md's: T1 peer-reviewed, T2 official documentation,
T3 professional standard, T4 vetted technical forum, T5 other. A branch's tier is
the tier of the *weakest* record its motivating claim rests on.

## Standing hazards — read before any branch

**H-1. The corpus behind this agenda is a compiled corpus record, not a review.**
**Restated 2026-09-03.** 96.1% of its 8,813 dispositions are keyword-classifier
outputs (was 98.3%); 347 records carry a read-based verdict (was 150); **full text
was read for 33 of the 327 included records and for none of the other 294**; 33 of
the original 149 are metadata-depth only; and the **178 records amendment A16
admitted carry no extraction at all**, so they enlarge the corpus's extent without
enlarging its claims. Gap **G-10**. Consequence for this agenda:
**an absence in the corpus is not evidence of absence in the literature**, and no
branch below may take "the corpus contains no record that does X" as a finding. Where
a branch rests on such an absence it is marked **absence-of-evidence** and its first
precondition is a targeted retrieval.

**H-2. 1,055 records ended screening unresolved and they are still concentrated in
this agenda's largest strand.** **Restated 2026-09-03.** Amendment A16 assessed 197
of the 700 X11 records by reading and decided 190 of them; **510 remain** — 503
never assessed at stage 2 at all, plus 7 assessed and unresolved — alongside 545
X10 records whose eligibility was never assessed. Gap **G-5**. Any branch that
claims novelty must still check its claim against those strata, which are in
`ka-screening-verdicts.jsonl` and *not* in the corpus.
**And a new hazard the re-execution creates, stated because it cuts the other way:**
the 178 records A16 moved *into* the corpus were read for **eligibility only**. A
branch that checks its novelty against "the corpus" must now check against two
populations with different warrants — 149 extracted records and 178 unextracted
ones — and the 178 can refute a novelty claim without ever having supported one.
**88 of the 503 could not be read past a title at all**, and per amendment A16 §(e)
and `ka-s4-retrieval-log.json` that is a retrieval failure (78 HTTP 429, 19 HTTP
403), **not** evidence that those records state nothing.

**H-3. The venue's own mechanics are unretrieved.** The filer-published rulebook
returned HTTP 429 on nine attempts (AG-1) and 17 CFR 40.11 returned an access
interstitial (AG-2). Six transfers in the corpus are marked
`not-transferable-as-stated` for want of facts in those documents (G-3). **Branch 0
is a hard precondition for branches 1, 3, 4 and 5**, and a branch that proceeds
without it is discharging a carrying assumption against a fact nobody has.

**H-4. Venue mechanism is not established, in either direction.** The corpus can
say neither that the venue is order-driven nor that it is quote-driven (S7-5, G-3
mark 6). No branch may assume either. Where a test's design depends on the answer,
both arms are specified.

**H-5. The Kalshi evidence base is thin and not independent.** 17 of 19
Kalshi-specific records are T5; exactly one peer-reviewed record contributes a
stated finding; 7 of 19 come from two author groups; 15 of 19 are SSRN DOIs sitting
on top of an arm that was never run (G-6, G-9). **No branch may treat the Kalshi
block as a replicated literature.**

---

### H-3 and H-4 — PARTLY SUPERSEDED at rev 3. Original text left standing above.

**H-3 is partly discharged.** The 2026-09-04 multivocal branch's venue arm retrieved
30 venue and regulator documents carrying 130 verbatim clauses, at full text of the
retrieved bytes, including most of what H-3 said was unretrieved: fee incidence and
functional form (`d01-c1`…`d01-c7`), a second and unmodelled rounding-fee component
(`d08-c1`…`d08-c4`), minimum tick and settlement value on the one series specified at
terms-and-conditions depth (`d21-c3`, `d21-c4`), full cash collateralisation with no
leverage on the binary leg (`d13-c2`, `d14-c2`), netting (`d07-c1`), the
position-limit regime across its 2023 and 2024 changes (`d16`, `d17`), the block-trade
route (`d20-c1`, `d20-c3`), and the authoritative token-bucket throughput document
(`d06-c1`…`d06-c9`). **The rulebook in force on 2026-09-04 was still NOT LOCATED**
(gap **MV-G-1**): the venue's rulebook page returns HTTP 200 with **no rule text in
the retrieved bytes** and no PDF exists at any of five candidate paths probed; the
three copies reachable through the regulator are a 2019 redacted version, a 2023
redline whose text extracts corrupted, and — see H-8 — a document that is not this
venue's at all. **HTTP 200 is not retrieval**, and every rulebook-level statement
available to this agenda comes from a superseded or degraded copy.

**H-4 is partly superseded, in one direction only.** The multivocal corpus's
section 9.1 states, from `d20-c1` and `d20-c3` at full-text depth, that the default
block minimum is 25,000 contracts restricted to eligible contract participants and
that **below it every order must interact with the central limit order book**; and,
from `d04-c4` and `d03-c4`, that customers trade peer-to-peer, the venue never takes
the other side of a trade, and every trade is published publicly through the API.
**Consequence: a pure quote-driven dealership reading is excluded for sub-block order
flow by a venue filing.** Three limits travel with that, and none may be dropped:
(i) it is bounded to the retrieved filings, of which **five — or four; the venue
arm's own log states both counts and this agenda does not resolve them (DI-6,
MV-G-7)** — of 111 enumerated rule filings were retrieved; (ii) a **hybrid** is not
excluded, and the venue's member agreement separately states that market makers
"may be able to price their quotes in ways that are materially different" and that
liquidity outside required windows "may be worse" (`d02-c1`, `d02-c2`); (iii) the
rulebook in force is not located (**MV-G-1**), so this is a dated statement about
filings and not a statement about the rules operating on any given day.
**Direction of the consequence for Branch 2b, stated because it is unfavourable:**
Glosten & Milgrom's binding conditions are a pure dealership market, unit trades and
no limit orders. A stated CLOB runs against the first and the third. Branch 2b's
mechanism half therefore gets **harder**, not easier, and a successor that reads this
correction as progress toward running Branch 2b has read it backwards.

**H-6. The multivocal corpus contains ZERO peer-reviewed and ZERO preprint records,
and its academic arm assigned no verdict at all.** All 528 of its academic records
are `G1` — identified, eligibility not assessed — and are **undecided**, neither
eligible nor ineligible (gap **MV-G-5**); 937 software artifacts are likewise
undecided (**MV-G-6**). **Tier 1 of the evidence hierarchy is empty in that
corpus**, and every branch derived from it stands on tier 2 (venue and regulator
documents) or tier 5 (code artifacts and practitioner pages). Branches 7-11 state
their tier at their head and none of them claims T1. The trade is deliberate and is
**not** an improvement in coverage: it is a much smaller decided set, arrived at by
reading rather than by classifier.

**H-7. WITHHELD AT SOURCE is not the same hazard as NOT RETRIEVED, and confusing
them wastes a successor's entire budget.** Three of the most executability-relevant
objects are filed confidentially under the redaction right 17 CFR 40.6 grants
(`d22-c2`), so **no amount of further searching produces them**: the market-maker
and liquidity-provider selection procedure ("The procedure by which the Exchange
anticipates making such determinations is described in Appendix B", Appendix B
confidential — `d19-c2`, `d19-c3`, gap **MV-G-2**); which contracts carry elevated
position limits ("appendix A is confidential and submitted under a request for
confidential FOIA treatment" — `d16-c5`, **MV-G-3**); and the settlement Source
Agency appendix ("Appendix E (Confidential) - Source Agency" — `d21-c11`,
**MV-G-4**). The Market Maker Agreement that gates every incentive is **not a
published document** and was not located at any endpoint searched (`d19-c1`). A
fourth object is named but **unvalued**: the quoted spread, size, uptime and
coverage a subsidised competitor must maintain — four obligation dimensions named
with **no value stated for any of them**, set per incentive period and not published
(`d19-c5`, handoff **MV-TC-7**, which records that the competitive quoting floor is
**not computable from any public document** and that the lawful substitute is an
MDES against a stated alternative, **never** retrospective power). Branch 7 exists
to find out whether this set decides anything.

**H-8. Two documentary traps that will corrupt a successor's citations if they are
not carried explicitly.** (i) **The regulator's own index mis-serves a document
under this venue's label** (defect **DI-1**, gap **MV-G-8**): a filing listed as
"Exhibit M" under this venue's organization record serves bytes titled *"Exhibit M:
Rulebook / Railbird Technologies, Inc."*, containing **zero occurrences of the
venue's name and 389 of the other venue's**, and Railbird Exchange, LLC is itself a
designated contract market — so the mistaken citation is to a real but *different*
venue's rules, which is the most dangerous kind of misattribution because the
document looks right. The corpus **records and does not repair it**, and excludes the
document so it cannot be cited from its store. **Every PDF a successor retrieves must
be identity-checked against its own title block before use**; the corpus's own
procedure — counting occurrences of the venue name in the extracted text — is cheap
and is the transferable positive of that defect. (ii) **Two S-D records extract with
damage** (**DI-7**): track-changes redlines carrying DRAFT watermarks, with
interleaved struck and inserted wording and spurious intra-word spaces, transcribed
exactly as extracted so they remain reproducible from the bytes. **Their quotations
must never be re-quoted as clean rule text.**

**H-9. Five bare numbers sit in the multivocal record, quoted verbatim from
sources, and NONE of them is adoptable** (gap **MV-G-23**; `~/.claude/CLAUDE.md`
§"Parameter & Prompt Selection"; charter commitment 3). They are: a
five-percentage-point cross-venue divergence threshold, which is a **chain citation**
whose underlying analysis was never retrieved; a cluster of post-release timing
figures carrying **no measurement, no data span and no citation** on the page that
states them; a *"never trade contracts below ~$0.15"* rule with **no fitted
derivation**; a *"we used ≈2.7 °F"* forecast-error assumption whose own source calls
it *"a guess, not a measurement"*; and a `+1.37% ROI, CI [1.13, 1.61], n=23` result
whose own source states the candidate is *"statistically indistinguishable"* from an
always-NO baseline. **No branch below carries any of them into a parameter choice.**
Where a branch needs the quantity, it names the selection procedure instead. Two of
the five are separately registered as nulls in
[failure_log.md](../../failure_log.md) F008 and F009. **A related hazard on
locators:** no included record in that corpus carries a DOI, PMID, PMCID or arXiv id
(**MV-G-15**, by ADR-0006 design), no web-archive snapshot was created for any
retrieved page (**MV-G-25**), and several grey-literature pages carry moving
`dateModified` timestamps (**MV-G-24**) — the byte digest fixes the bytes, **not**
the URL's future content.

**H-10. The lateral and practitioner BYTES this agenda cites are NOT ARCHIVED, so
their digests are ATTESTATIONS A READER CANNOT CHECK** *(gap **MV-G-27**, registered
by round-1 remediation of the multivocal corpus record on 2026-09-04; carried into
this agenda under findings **CRITICAL-2-3** / **SCOPE-2-7**)*. The S-D and S-E
retrieved bytes were **deliberately not copied into the repository** — they are
third-party pages and this repository is public — so the `sha256` recorded against
each is an **attestation by the corpus lead**, not a value a reader can recompute.
The lead verified all **32** lateral payload digests **once**, against an ephemeral
scratchpad, and all 32 matched. **That makes them VERIFIED-ONCE, not verifiable**,
and the distinction is the whole hazard: a successor inherits a single unrepeatable
check rather than a reproducible one, and the scratchpad it was run against no longer
exists. **This is an evidence-posture change and not bookkeeping**, because this
agenda cites *into* `ks-lateral-records.json` at load-bearing points — `KSL-C09`
(interest accrues on the collateral behind open positions; Branch 10's documentary
half), `KSL-C14` (the settlement-clock and definition alignment precondition, which
is Branch 9's entire warrant), `KSL-C15`/`KSL-C16` (revision treatment, in Branch 9's
dimension list), and `KSL-C30`/`KSL-C32` (Branch 10's universe filter and its stratum
identification) — and every one of those citations now rests on a digest the corpus
record itself describes as uncheckable by a reader. **Consequence, binding on every
branch below:** an S-D or S-E quotation is cited as *attested at the stated retrieval
date*, never as *verifiable*, and a successor that needs one of those clauses to be
**true** rather than to be **attested** must re-retrieve the page itself and record
its own digest. Under **MV-G-24** (moving `dateModified` timestamps) and **MV-G-25**
(no web-archive snapshot) the re-retrieved bytes may legitimately differ, so **a
mismatch is not evidence that the attestation was wrong** — which is precisely why
the attestation cannot be promoted to a verification by any later check either. **No
branch is withdrawn by this hazard and none is added**; what changes is the label
every lateral citation in this agenda carries.

---

## Branch 0 — Venue mechanics as a dated document set (precondition branch)

**From:** G-3, TC-1, AG-1, AG-2 — **predecessor-corpus identifiers, bare per the
prefix convention.** **Tier of the motivating evidence:** T2 (official
documentation), currently *unretrieved*.

**What is needed.** The filer-published rulebook plus the CFTC filing record, as a
**dated document set**, yielding: fee schedule; tick size; settlement source and
settlement rule per contract family; position limits; membership and market-maker
programme terms; permitted pre-settlement position transformations; and **the
trading mechanism** (order-driven book vs quote-driven dealer vs hybrid).

**No falsification test is stated for this branch, and that is deliberate.** It is a
retrieval task, not a claim about the world. Writing a "test" here would be exactly
the design-resolution-mislabelled-as-test defect this agenda is written against.

**Refutation condition for the branch's *own* premise, which is testable:** the
branch assumes the documents exist and are publicly reachable. If a session with a
working route to the filer's document establishes that the rulebook is not
publicly published, the premise is refuted and G-3's six marks become permanent
rather than pending.

**Preconditions.** A retrieval route that survives the venue's rate limiting; a
dated snapshot with its retrieval log, per this project's provenance rule.

**Precondition status at rev 2 (2026-09-03): UNCHANGED, and every fact this branch
needs is still unretrieved.** The 2026-09-03 re-execution retrieved 33 full texts and
none of them was a venue document. The rulebook is still unreachable (AG-1, HTTP 429
on nine attempts); 17 CFR 40.11 still returns an access interstitial (AG-2); S7-5
still reads `Not established`. Specifically **not** obtained: the fee schedule, the
tick size, the settlement source and rule per contract family, the position limits,
the membership and market-maker programme terms, the permitted pre-settlement
transformations, and **the trading mechanism**. The corpus's six G-3 marks stand at
six.

**What the re-execution did change here, and it raises the stakes rather than
lowering them.** Two included records now state venue-mechanism boundaries **in their
own words**, read at full text — Abernethy, Chen & Vaughan exclude the continuous
double auction from their framework outright (*"These markets do not fall into our
framework and deserve separate treatment"*), and Othman, Pennock, Reeves & Sandholm
restrict their maker to a setting with **no persistent limit orders**. Against those,
Chakraborty, Das & Peabody carry an LMSR maker **into** a continuous double auction,
in a simulation with no budget constraint. **So the mechanism question is no longer
this agenda's caution about a literature; it is a boundary the literature draws on
itself, and which side of it the venue falls on is exactly the fact Branch 0 cannot
get.** A successor that proceeds without Branch 0 is not merely under-evidenced; it is
choosing a side of an author-stated exclusion by default.

**Blocks:** branches 1, 2b (mechanism half only), 3, 4, 5.

**PRECONDITION STATUS AT REV 3 (2026-09-04): PARTLY DISCHARGED, and the rev-2
paragraph above is superseded on its facts while its text is left standing.** The
multivocal branch's venue arm obtained, at full text of the retrieved bytes and with
per-document byte digests: **the fee schedule and its functional form** (`d01`),
**the second, unmodelled rounding-fee component** (`d08`), **minimum tick and
settlement value** on the one series specified at that depth (`d21-c3`, `d21-c4`),
**full cash collateralisation** (`d13-c2`, `d14-c2`), **netting** (`d07-c1`), **the
position-limit regime** and its accountability-level successor (`d16`, `d17`), **the
block-trade route** (`d20`), **the throughput document** (`d06`), and **the existence
and shape of the market-maker programme** (`d19`). It also settles, from `d20-c3`,
that below the block threshold every order must interact with the central limit order
book — see the H-4 supersession block.

**What Branch 0 still owes, and it is now TWO different kinds of debt, which is the
substantive change.** *(Every identifier in this table is a MULTIVOCAL-corpus
identifier and carries the `MV-` prefix; the branch's own `From:` line above cites
the PREDECESSOR's bare `G-3`, and the two are different objects — finding REV-1-3.)*

| still missing | class | why more searching will or will not help |
|---|---|---|
| the rulebook in force on the retrieval date | **NOT LOCATED** (MV-G-1) | a better route might help; five candidate paths and two client-rendered surfaces have failed |
| the market-maker selection procedure; the Market Maker Agreement | **WITHHELD AT SOURCE** (MV-G-2) | **searching cannot close it** — confidential appendix, plus an unpublished agreement |
| which contracts carry elevated position limits | **WITHHELD AT SOURCE** (MV-G-3) | **searching cannot close it** |
| the settlement Source Agency appendix | **WITHHELD AT SOURCE** (MV-G-4) | **searching cannot close it** |
| the quoting obligations a subsidised competitor must meet | **NAMED BUT UNVALUED** (`d19-c5`, MV-TC-7) | not published at all; the lawful substitute is an MDES, never retrospective power |
| the per-series fee multipliers over ~90 series | **NOT EXTRACTABLE** (DI-3, blocking MV-TC-2) | the bytes are in hand; the table's cell alignment does not survive extraction |
| the reportable position level per contract | **NOT PUBLISHED** (`d13-c4`) | the rulebook states it is "communicated to FCM members" |

**Consequence for the blocked branches.** Branches 1 and 5 are **unblocked in part**:
fee, tick, collateral and netting are in hand, and Branch 5's permitted-transformation
question now has a partial documentary base. Branch 3's mechanism arm can be
**selected** rather than left two-armed for sub-block flow, subject to the three
limits in the H-4 block. Branch 4's friction side is **still open**, and Branch 10
below is the branch that addresses the one term rev 2 called its binding constraint.
Branch 2b's mechanism half is **harder**, not easier.

---

## Branch 1 — Does the coherence condition bind on a live binary event book?

**From:** G-1 — **the PREDECESSOR corpus's G-1, not the multivocal corpus's
`MV-G-1`; the two are different objects (finding REV-1-3)** — and the S1 strand of
the corpus. **Tier:** T1 (the coherence
condition is stated in peer-reviewed sources in the corpus); the venue-side premise
is T2-*unretrieved*.

**Claim at issue.** That for a set of mutually exclusive and exhaustive contracts on
one event, quoted prices imply probabilities summing to one up to a bound set by the
fee, spread and collateral structure — and that observed violations are therefore
informative about frictions rather than about mispricing.

**Falsification test.**
- **Unit of analysis:** one (event, timestamp) pair over a mutually exclusive and
  exhaustive contract family.
- **H0:** the distribution of the coherence residual — the signed excess of the
  summed best-executable implied probabilities over one — is centred at the value
  predicted by the venue's own fee and spread structure (Branch 0 output), against
  the alternative that it is displaced from it.
- **Statistic:** the location of the residual distribution, estimated with a
  HAC-consistent standard error; bandwidth by the
  [Newey & West 1994](https://doi.org/10.2307/2297912) data-dependent rule or the
  [Andrews 1991](https://doi.org/10.2307/2938229) plug-in, **selection rule named,
  value `TO COMPUTE`**. Serial dependence within an event is the reason a HAC
  estimator rather than an i.i.d. one is specified.
- **Comparison:** the *predicted* residual location computed from Branch 0's fee and
  tick schedule, not zero. A test against zero would reject on the fee alone and
  would be uninformative, which is the failure mode this specification exists to
  avoid.
- **Refutation condition:** the branch's claim is refuted if the residual location
  is statistically distinguishable from the friction-predicted value **and** the
  displacement does not shrink as the executable-depth constraint is tightened. If
  it shrinks with depth, the residual is a liquidity artefact and the claim
  survives.
- **Multiplicity:** the test is run over many contract families. This is an
  **existence** claim ("there exist families where coherence fails beyond
  frictions"), so it needs family-wise control —
  [White 2000](https://doi.org/10.1111/1468-0262.00152) reality check or
  [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA. Family definition
  and α `TO COMPUTE`.

**Preconditions.** Branch 0 (fee, tick, collateral); a book snapshot at executable
depth, which is out of scope here (ADR-0003) and belongs to an executing project.

**Absence-of-evidence flag.** The corpus contains no record that nets a measured
event-exchange discrepancy against a fully specified friction set on an order book
(G-1). Under H-1 that is not evidence that none exists; a targeted retrieval
against the 545 X10 and **510** residual X11 strata is the first step. **Restated at
rev 2:** amendment A16 assessed 197 of the original 700 by reading and admitted 178 of
them to the corpus — so part of that targeted retrieval has been performed, and it
**did not** turn up a record netting a measured discrepancy against a friction set,
because it assessed eligibility and not content. The 178 were never extracted, so this
absence-of-evidence flag is **weaker** after the re-execution, not stronger.

**Note at rev 3.** The fee side of this branch's comparison is now documentary rather
than pending — `d01-c1`…`d01-c7` state the taker and maker functions, the multiplier
defaults, the upward rounding to a centicent, and that a non-zero maker multiplier
**charges** rather than rebates; `d08` adds a second, path-dependent rounding-fee
component accumulated **per order across all fills**. **The per-series multiplier is
still not extractable (DI-3, MV-TC-2)**, so the predicted residual location is
computable per series only for series whose multiplier is recoverable, and the branch
must state which those are before running. This is a change in what blocks the branch,
not a change to its test, and the test above is unaltered. The intra-series
instantiation of this question is `research/01_hypothesis_register/H001/design.md`
— see "Relationship to H001" below.

---

## Branch 2 — Do inventory-risk market makers survive the bounded-payoff restriction?

**From:** G-5, TC-4, and the corpus's S4 strand. **Tier:** T1 for the lineage.
**Depth of the motivating evidence, rev 2:** **full text**, for four of the five
records this branch turns on, read on 2026-09-03 under protocol amendment A17 and
recorded with their retrieval routes, content digests and first-page identity checks
in
[ka-s4-fulltext-extraction.jsonl](../literature/search_logs/kalshi-arbitrage/ka-s4-fulltext-extraction.jsonl).
The fifth, **Ho & Stoll 1981**, was attempted through six routes and **not
obtained**, and has no abstract in any source; the branch's treatment of it rests on
**no depth at all** and says so at every point below.

---

### SUPERSEDED — Branch 2's rev 1 premise, and why it was wrong

**Rev 1 said:** *"the transfer itself is **asserted by transfer, not by the lineage**
— four of five named-lineage anchors are at metadata depth and the one whose model is
stated assumes a Brownian reference price, which is explicitly excluded for a
probability bounded in [0,1] (Guéant, Lehalle & Fernandez-Tapia 2012)."*

**Three things in that sentence are now corrected.**

1. **The arithmetic was inherited wrong.** The corpus's five named-lineage anchors at
   metadata depth were Ho & Stoll, Glosten & Milgrom, Kyle, Krishnan and Liu & Wang —
   **five, not four** — and Guéant was at **abstract** depth, not metadata. Rev 1
   substituted Guéant for a fifth metadata-depth anchor. The corpus record's own
   sentence carried the same off-by-one and is corrected at its site in section 8.4.
2. **The depth claim is obsolete.** Glosten & Milgrom, Kyle, Avellaneda & Stoikov and
   Guéant et al. were read at **full text**. Only Ho & Stoll remains unread, and it is
   now unread for a stated and enumerated reason rather than for want of trying.
3. **The premise the branch was built on is a category error, and this is the
   substantive correction.** Rev 1 treated Glosten & Milgrom and Kyle as
   "named-lineage anchors" whose *monotone inventory-reservation-price* result must be
   re-derived under a bounded payoff. **Neither model has an inventory objective --
   Glosten & Milgrom on the authors' own statement, Kyle [corpus-inference] over
   pp. 1315-1317 only, as an inference from absence.** *(Marker added inline
   2026-09-04, findings **QUANT-2-3** and **LITERATURE-2-4**; the qualification was
   previously carried only in the bullets below this line.)*
   The two halves of that claim do **not** rest on the same kind of evidence, and this
   agenda no longer runs them together. *(Corrected 2026-09-03, audit finding
   LITERATURE-1-1: the form previously used here -- "and both say so in their own
   texts" -- is correct for Glosten & Milgrom and incorrect for Kyle, and the Kyle
   bullet carried no [corpus-inference] marker although the corpus record's section
   8.4 legend defines that marker for exactly this step.)*
   - **Glosten & Milgrom 1985 [FT] -- the authors say so.** *"Our central assumption
     about the specialist is that he earns zero expected profits on each purchase and
     each sale, and he faces no transaction costs."* The bid and the ask are
     conditional expectations of V given the arriving order. The authors state, in a
     footnote, that the assumption *"results in the specialist sometimes accumulating
     large inventories of stock and sometimes large inventories of cash"* and that
     *"if we were to recognize binding inventory constraints, we could not have a zero
     profit condition."* **That is an author-stated fact about inventory:** the
     specialist's inventory is explicitly not controlled, and the authors say why it
     cannot be. The extraction record carries the same reading -- its
     `applicability_conditions_stated` include *"the authors note that binding
     inventory constraints are inconsistent with the zero-profit condition and assume
     carrying capacity large enough that they do not bind"*.
   - **Kyle 1985 [FT] -- Kyle does not say so, and the claim is this corpus's
     inference.** What p. 1316 states is only this: *"The prices determined by market
     makers are assumed to equal the expectation of the liquidation value of the
     commodity, conditional on the market makers' information sets at the dates the
     prices are determined. Thus, market makers earn on average zero profits."* **That
     sentence says nothing about inventory.** The observation that the model carries
     **no inventory state variable and no reservation price** is a true observation
     about the specification as this corpus read it, and it is an inference **from an
     absence** -- not a statement of Kyle's. **[corpus-inference]** Two limits on it,
     stated because they bound how much weight it takes: (i) the extraction read
     **pp. 1315-1317 only** -- the abstract, introduction and section-2 model setup,
     read as rendered page images because the retrieved scan has no text layer -- and
     the extraction row says in terms that *"the remaining pages were NOT read"*, so
     the absence is established over the three pages read and not over the article;
     (ii) Kyle nowhere says his model does or does not have an inventory
     objective, and this corpus attributes no such statement to him -- the same
     discipline section 8.4.3's Kyle entry applies to the payoff-support
     incompatibility.

   **Consequence.** Branch 2's H0 as written — *"for each named-lineage model, the
   monotone inventory-reservation-price result is derivable…"* — is **vacuous for
   Glosten & Milgrom and for Kyle**, because there is no such result in either model
   to re-derive — **[corpus-inference] for the Kyle half, established over
   pp. 1315-1317 only, as an inference from absence** *(marker added 2026-09-04,
   finding **QUANT-2-3**: this is the stated ground for removing Kyle from the model
   set, so it is exactly the site at which the marker is load-bearing)*. Running the test on them would have produced a `fails` verdict that
   said nothing about bounded payoffs and everything about the branch's own mislabelling.
   **The model set is corrected below.** This is the branch's rev-1 premise being
   contradicted by the full texts, and it is corrected rather than withdrawn because
   the branch's *question* survives intact — only its membership list was wrong.

---

### The branch as it now stands

**Claim at issue, unchanged.** That the inventory-control lineage's central
qualitative prediction — a maker's reservation price moves monotonically against
accumulated inventory — holds when the underlying is a probability bounded in [0,1]
and settling at an endpoint, rather than an unbounded diffusion.

**The corrected model set, with each member's stated payoff support quoted from its
own text.** These are the models that have an inventory objective and therefore have
something to re-derive:

| model | depth | payoff support the model assumes, as the authors state it | status for this branch |
|---|---|---|---|
| **Ho & Stoll 1981** `10.1016/0304-405X(81)90020-9` | **none — full text not obtained, no abstract exists** | **unknown to this corpus** | **In the set on the strength of other authors' descriptions of it, and on nothing this corpus read.** Retrieving it is the branch's first precondition |
| **Avellaneda & Stoikov 2008** `10.1080/14697680701381228` | **[FT]** | `dS_u = σ dW_u` — driftless **arithmetic Brownian motion**, terminal value a **mark-to-market** at S_T, not a settlement | In the set. The substitution the test requires is well defined |
| **Guéant, Lehalle & Fernandez-Tapia** `10.1007/s11579-012-0087-0` | **[FT]** (accepted manuscript) | **Brownian reference price** with standard deviation σ; terminal value cash plus `q_T S_T`, again mark-to-market; inventory constrained to \|q\| ≤ Q | In the set. The inventory constraint is what reduces the HJB system to linear ODEs, so the substitution interacts with the solution method and not only with the model |
| ~~Glosten & Milgrom 1985~~ | **[FT]** | `V ≥ 0, var(V) < ∞`, realised at a terminal date T₀ | **REMOVED from the set.** No inventory objective; nothing to re-derive. It re-enters the agenda in the new Branch 2b below |
| ~~Kyle 1985~~ | **[FT]**, pp. 1315-1317 only | ex post liquidation value **normally distributed**, `N(p₀, Σ₀)` | **REMOVED from the set.** No inventory objective; nothing to re-derive. **[corpus-inference]** -- Kyle states no inventory objective and states no *absence* of one either; the model as this corpus read it carries no inventory state variable and no reservation price, and that reading is the corpus's, from the three pages read and not from the article *(marker added 2026-09-03, finding LITERATURE-1-1)* |

**Falsification test, restricted to the corrected set.**

- **Unit of analysis:** the model, not the market. This remains a **derivation** test,
  specifiable without any data, which is why it still sits before branch 3.
- **H0:** for each model in the corrected set, the monotone
  inventory-reservation-price result is derivable when the reference-price process is
  replaced by a process with support in [0,1] and an absorbing endpoint at settlement,
  with all other assumptions unchanged.
- **Statistic / procedure:** re-derive each model's first-order condition under the
  substituted process and record, per model, one of `holds`, `holds under an added
  condition C` (with C stated), or `fails`.
- **Refutation condition:** the branch's claim — that the lineage transfers — is
  refuted for any model whose result requires unbounded support, and the refutation is
  **per model**, not per lineage.
- **What the substituted process must satisfy, now specifiable from a full text
  instead of being left vague.** Rev 1 said only "support in [0,1] and an absorbing
  endpoint". Two corpus records read at full text state such a process explicitly, and
  a successor should use one of them rather than invent one:
  - [Moallemi, Robinson & Zhu 2026](https://arxiv.org/abs/2607.17428) **[FT]** state
    the structure directly — *"Outcome contracts in prediction markets stand out from
    other assets as their prices are bounded between zero and one, and at resolution
    they collapse to one of the two endpoints"* — and their Assumption 3 makes the
    endpoints **absorbing**, with volatility strictly positive in the interior and a
    unique solution up to the boundary, plus an informational-time condition
    guaranteeing resolution at T. They derive `Var[P_T | F_t] = P_t(1 − P_t)`.
  - [Feil & Nendel 2026](https://arxiv.org/abs/2607.17991) **[FT]** generate the price
    as `p_t = f(L_t)` with `f ∈ C²(ℝ; (0,1))`, `f'` and `f''` bounded and Lipschitz,
    the logistic function given as a member; settlement is `Y ∈ {0,1}`.
  **These are stated as candidate substitutions with their own conditions attached,
  not as a recommended choice.** Choosing between them is a design resolution, not a
  test, and belongs under preconditions.
- **A large part of this test has already been performed in the literature, and the
  branch must not claim it as novel.** [Feil & Nendel 2026](https://arxiv.org/abs/2607.17991)
  **[FT]** formulate the maker's stochastic control problem natively for a `{0,1}`
  settlement with price in `(0,1)`, and their objective adds a **terminal settlement
  risk penalty** on remaining inventory that the mark-to-market classical problem has
  no analogue of. They state, in their own words, *"To the best of our knowledge,
  optimal market making in prediction markets has not yet been studied within a
  stochastic control framework."* Their reported numerical finding is **the
  diminishing importance of inventory risk as prices approach zero or one** — a result
  on **their** model, reported here as theirs, and neither a claim about any venue nor
  a rule. **Consequence for this branch:** H0 as stated asks whether the *classical*
  models survive substitution; Feil & Nendel show what a model *built for* the bounded
  case looks like. Those are different questions, and a successor that conflates them
  will report a discovery that is a citation.
- **A second result the branch inherits and must not re-derive.**
  [Feys 2026](https://arxiv.org/abs/2606.01477) **[FT]** shows that under five stated
  axioms the Cartea–Jaimungal running-penalty coefficient and the Avellaneda–Stoikov
  risk-aversion parameter are **one parameter**, not two. Any re-derivation in this
  branch that carries both and calibrates them separately is defective at the point of
  writing. Note the limits the author states on his own result: he does **not** model
  adverse selection, path-functional preferences are *"genuinely outside the scope"*,
  and his mid-price is a continuous semimartingale with a Brownian benchmark — so the
  identification is established for the unbounded case, and whether it survives the
  substitution H0 specifies is itself open.
- **Independent check the corpus supplies, now marked for depth.** The corpus records
  an **unresolved internal disagreement** on the sign of this effect — the lineage
  predicts a negative inventory-to-reservation-price relation, while futures
  transaction data show a positive one
  ([Manaster & Mann 1996](https://doi.org/10.1093/rfs/9.3.953), **[abs]** — full text
  attempted 2026-09-03, `oa_status: closed`, no location to fetch). **This check rests
  on an abstract.** A derivation that reproduces the negative sign without addressing
  that evidence has not completed the test; a derivation that *dismisses* the evidence
  on the strength of an abstract has not either.

**Preconditions, restated against what was and was not retrieved.**
- **None from Branch 0.** The branch remains venue-independent by construction, which
  is why it is still the one branch that can proceed while AG-1 stands.
- **Rev 1's first task is now partly discharged.** Rev 1 said: *"Full texts of the five
  named-lineage anchors, which the corpus does not have (AG-5): four are at metadata
  depth. Retrieving them is the branch's first task and is a precondition, not a
  test."* **Four were retrieved on 2026-09-03.** What remains is **Ho & Stoll 1981**,
  and it remains for enumerated reasons: Unpaywall `closed`; Semantic Scholar `CLOSED`;
  OpenAlex with every `pdf_url` null; ScienceDirect PDF HTTP 403; a course-page mirror
  returning HTTP 200 `text/html` that was an *"Account Suspended"* page; two guessed
  Wharton working-paper URLs at HTTP 404. RePEc states *"No abstract is available for
  this item."* **A route that requires institutional access or an interlibrary request
  is the remaining precondition, and this project has neither.**
- **Until Ho & Stoll is read, the branch may not state what its model assumes.** Every
  description of it available to this corpus is a description by *other* authors — by
  Avellaneda & Stoikov, and by Feil & Nendel. Those are evidence about what those
  authors believe Ho & Stoll to contain, and a successor that uses them as the model
  specification is fitting a secondary source.

---

## Branch 2b — Does the adverse-selection lineage transfer, and is that a different question? (new at rev 2)

**From:** the removal of Glosten & Milgrom and Kyle from Branch 2's model set, which
leaves a real question with no home. **Tier:** T1. **Depth:** **[FT]** for both
records.

**Why this branch exists.** Branch 2 asks whether an *inventory-control* result
survives a bounded payoff. **Glosten & Milgrom is an adverse-selection model whose
authors state that binding inventory constraints are inconsistent with their
zero-profit condition; Kyle carries no inventory state variable in the pages this
corpus read -- [corpus-inference].** Their transfer question is therefore a different
one, and rev 1 lost it by filing them under Branch 2. *(Restated 2026-09-04, findings
**REV-2-3** and **LITERATURE-2-4**. This paragraph is the entire warrant for creating
this branch, and it previously read "Glosten & Milgrom and Kyle are adverse-selection
models with zero-expected-profit makers and no inventory state" -- stating as
established fact the one proposition the Branch 2 bullet flags as an inference from
absence over three pages. **A reader who reaches Branch 2b without reading Branch 2's
superseded-premise block now gets the qualification here.**)*

**Precondition on this branch's own founding premise, stated because it bounds what
the branch may conclude.** The Kyle half of the premise above is **unverified over the
unread remainder of the article**: the extraction read **pp. 1315-1317 only** -- the
abstract, the introduction and the section-2 model setup, as rendered page images, the
scan having no text layer -- and the extraction row states in terms that *"the
remaining pages were NOT read"*. Nothing in this branch may treat "Kyle has no
inventory state" as established over Kyle 1985 as a whole until the remainder of the
article is read. *(Added 2026-09-04, finding **REV-2-3**.)*

**Claim at issue.** That the adverse-selection lineage's central result — a positive
bid–ask spread arises from informed trading even with a risk-neutral, zero-expected-profit
maker — carries to a payoff bounded in [0,1] settling at an endpoint.

**What the full texts already settle, and what they do not.**
- **Glosten & Milgrom's stated support condition is satisfied by such a payoff.** The
  authors write, p. 76: *"At some time T₀ in the future, some random dollar value V
  [V ≥ 0, var(V) < ∞] per share will be realized, and the informed have information
  about this random variable V."* No distributional form is imposed. *(Quotation
  completed 2026-09-04, **LITERATURE-2-1** quotation audit: it was previously cut at
  "will be realized." with a full stop the source does not carry there. Re-verified
  against p. 76 of the retrieved scan rendered as a page image; otherwise verbatim.)*
  **[FT]** **A payoff bounded in [0,1] realised at a terminal date meets that
  condition — and that inference is the corpus's, not the authors'.** The authors
  nowhere discuss binary, bounded or event contracts. Their own section-3 example is a
  **two-point-valued** security: *"Suppose that the stock can have either of two
  values, V = 1 or V = 11."*
- **Kyle's stated support condition is not.** *"The ex post liquidation value of the
  risky asset, denoted ṽ, is normally distributed with mean p₀ and variance Σ₀"*
  (p. 1317), and the author states that normality is what buys the model's linear
  structure (p. 1316). **[FT]** A value supported in [0,1] is not a realisation of a
  normal distribution — again the corpus's inference from the author's stated
  assumption, and not the author's statement.
- **Therefore the branch's live question is not the payoff at all; it is the
  mechanism.** Glosten & Milgrom's binding conditions are a **pure dealership market**
  in which *"the specialist performs no brokerage services, and in effect all orders
  are market orders"*, **unit trades only**, and **no limit orders** — with the authors
  noting that including limit orders *"may well alter the characteristics of
  transaction prices"*.

**Falsification test.**
- **Unit of analysis:** the model.
- **H0:** the Glosten–Milgrom spread result is derivable when V is restricted to
  {0,1} (or to [0,1] with an endpoint realisation), with all other assumptions
  unchanged.
- **Statistic / procedure:** re-derive the bid and ask as conditional expectations
  under the restricted support and record `holds`, `holds under an added condition C`,
  or `fails`. The authors' own two-valued example is the natural starting point and its
  presence in the paper is itself a partial answer.
- **Refutation condition:** H0 is refuted if the result requires a support the
  restriction forbids, or if the restriction makes the zero-expected-profit condition
  inconsistent with the market-clearing condition.
- **The second, harder half, which the branch must state and cannot answer:** whether
  the *mechanism* conditions hold on the venue. They are pure dealership, unit trades
  and no limit orders. **Not one of the three is established for the venue of
  interest** (S7-5 `Not established`, AG-1). **Blocked on Branch 0**, and the block is
  on the mechanism, not the payoff.

**Preconditions.** Branch 0, for the mechanism half only. The derivation half has
none: both texts are in hand.

**Absence-of-evidence flag.** The corpus records **no** transfer of the Glosten &
Milgrom apparatus to a binary event venue by anyone. The apparent one was withdrawn
under corpus finding LITERATURE-1-5: **Glosten & Harris (1988)** is a different paper
by a different author pair, and it is not in the corpus.  Under H-1 that absence is not
evidence that no such transfer exists.

**Rev-3 note, and it runs against this branch.** The H-4 supersession block records
that a venue filing states, for sub-block order flow, that **every order must interact
with the central limit order book** (`d20-c3`), and that customers trade peer-to-peer
with the venue never taking the other side (`d04-c4`). Two of Glosten & Milgrom's
three binding mechanism conditions — pure dealership, and no limit orders — are
therefore **contradicted for sub-block flow** by a retrieved document, rather than
merely unestablished. The branch's mechanism half moves from *unknown* to *probably
unsatisfied*, and the honest statement of what remains is narrower: whether the
adverse-selection result survives on a limit-order market is a question the authors
themselves flag (*"may well alter the characteristics of transaction prices"*) and
which this branch would have to answer before, not after, the payoff substitution.

---

## Branch 3 — Is the favourite-longshot bias present on the venue, and is it the same object?

**From:** G-3 marks 3 and 4, G-4, G-6, and the S3 strand. **Tier:** T1 for the FLB
literature; **T5** for every Kalshi-specific record that would motivate expecting it
here, and one author group supplies five of them (H-5). **Depth at rev 2: abstract,
throughout.** No record motivating this branch was read at full text; the 2026-09-03
extraction covered the S4 core set only, and the three Kalshi-specific records that
bear on this branch are behind an SSRN HTTP 403 (corpus gap AG-12). **This branch
rests entirely on abstracts and says so.** One S4 record it borrows from was read:
[Makropoulou & Markellos 2011](https://doi.org/10.1111/j.1467-9485.2011.00557.x), the
information-based derivation of the FLB, was **attempted at full text on 2026-09-03
and not obtained** (`oa_status: closed`), so it too remains an abstract-depth
citation.

**Claim at issue.** That the favourite-longshot bias measured on sportsbooks,
racetracks and parimutuel pools is the same phenomenon as any price-probability
curvature observed on a regulated event-contract exchange — and therefore that its
explanations transfer.

**Falsification test.**
- **Unit of analysis:** the (contract, resolution) pair, binned by quoted implied
  probability.
- **H0:** the calibration curve of quoted implied probability against realised
  frequency is flat in the deviation sense — the deviation from the 45° line does
  not vary monotonically with the quoted probability — against the alternative that
  it is monotone in the direction the sportsbook literature reports.
- **Statistic:** a monotone-trend statistic on the binned deviations with a
  distribution-free null (permutation of the resolution labels within event date),
  and a bootstrap CI on the deviation at each bin. Bin edges `TO COMPUTE` by a
  stated rule — equal-count bins with count chosen by cross-validation of the
  calibration estimator, **not** a round number.
- **Comparison:** the *same* estimator applied to a bookmaker or parimutuel dataset
  from the corpus's own T1 sources, so that a difference in the estimator's
  behaviour cannot be confused with a difference in the venue.
- **Refutation condition, and this is the branch's substantive content:** the "same
  object" claim is refuted if the venue curve and the comparison-venue curve differ
  in **sign or monotonicity direction**, not merely in magnitude. A magnitude
  difference is consistent with the same phenomenon under different frictions; a
  sign difference is not.
- **Mechanism confound that must be handled, not assumed away (H-4).** Every leading
  explanation in the corpus is mechanism-dependent — bookmaker price setting under
  information asymmetry, insider-driven odds movement, risk-love preferences. If
  Branch 0 shows the venue is order-driven, the bookmaker-conduct explanations are
  **not** available and the test is a test of the preference-side explanations only;
  if quote-driven, both classes are live. The branch specification is therefore
  **two-armed** and the arm is selected by Branch 0's output, never assumed.

**Preconditions.** Branch 0 (mechanism, settlement rule); resolution outcomes;
composition control across the 2025 asset-class boundary (TC-5 — **the PREDECESSOR
corpus's TC-5, not the multivocal `MV-TC-5` cited by Branch 11**) — a re-estimate that
pools across a composition break measures the break.

**Absence-of-evidence flag.** G-4: no abstract this corpus read states a
market-making model fitted to this venue. Bounded to the 116 abstract-depth records.

**Rev-3 note on the two-armed design.** Per the H-4 supersession block, the
order-driven arm is now **selected** for sub-block order flow on the strength of
`d20-c3`, subject to that block's three limits — the filing sample, the unexcluded
hybrid, and the missing rulebook in force. The two-armed specification is **not
withdrawn**: it stands for block-size flow, for any quote-driven overlay a hybrid
would carry, and for any date whose rule surface is not reconstructible, which is
Branch 8's object. A successor that deletes the quote-driven arm on the strength of
one clause has over-read one filing.

---

## Branch 4 — Is a stated cross-venue discrepancy executable after the full friction set?

**From:** G-2, TC-3, the S2 and S5 strands — **predecessor-corpus identifiers; the
multivocal `MV-TC-3` that Branch 9 derives from is a DIFFERENT handoff (finding
REV-1-3).** **Tier:** T1 for the cross-venue
arbitrage literature; **the friction side is unevidenced** — G-2 records that no
retrieved abstract among the 116 read at abstract depth states a measurement or a
model of the cost of capital locked in an event-contract position until settlement.
**Depth at rev 2: abstract, throughout — and G-2's negative is now WEAKER, not
stronger.** The 178 records amendment A16 admitted were read for eligibility and never
extracted, so a capital-lockup measurement could sit inside them and the corpus would
not know. The one full-text record that touches this branch's object is
[Hanson 2003](https://doi.org/10.1023/A:1022058209073) **[FT]**, whose third stated
design condition is a **collateral** condition — how to ensure users can cover their
bets *"without needlessly preventing them from using previous bets as collateral for
future bets"*. That is a design requirement stated by a mechanism designer, not a
measurement of a cost, and it does not close G-2; it is recorded because it was
invisible when that record sat at metadata depth.

**Claim at issue.** That a price discrepancy between two venues on the same event
constitutes an arbitrage opportunity once fees, spread, collateral and capital
lockup to settlement are netted.

**Falsification test.**
- **Unit of analysis:** the (event, venue-pair, timestamp) triple.
- **H0:** the net-of-friction discrepancy, computed at **executable** depth on both
  legs and charged the full lockup cost to settlement, has a distribution whose
  upper tail is not distinguishable from what the friction model alone generates.
- **Statistic:** the frequency and size of net-positive discrepancies, with a
  bootstrap CI; the surrogate is the **same computation with the two legs' event
  identities permuted**, which preserves each venue's marginal price process and
  friction structure while destroying the same-event correspondence that an
  arbitrage requires. A returns-resampling surrogate is **not** admissible here: it
  destroys the settlement-endpoint structure the claim depends on.
- **Refutation condition:** the claim is refuted if the net-of-friction upper tail
  is indistinguishable from the permuted surrogate. It is *not* refuted by a small
  effect; it is refuted by an effect that the surrogate reproduces.
- **Capital lockup is the parameter that decides this test and it has no source.**
  It is `TO COMPUTE` as a function of contract duration against a funding-cost
  series (TC-3), and until it is computed the test **cannot be run** and no
  executability claim may be stated. This is the branch's binding constraint and it
  is stated here rather than discovered later.

**Preconditions.** Branch 0 (fees, collateral, settlement); a funding-cost series;
synchronised quotes at executable depth on both venues — all out of scope here.

**Rev-3 note: this branch's two hardest premises now have named successors.** The
"same event" premise is not a premise at all but a proposition to be tested, and it
is Branch 9. The capital-lockup term this branch calls its binding constraint is
Branch 10. Neither is folded into Branch 4, because doing so would give this branch
three tests, and the agenda's rule is one falsification test per branch.

---

## Branch 5 — Does the protocol-executable / payoff-space distinction have a venue counterpart?

**From:** TC-2, TC-1, G-3 mark 1 — **predecessor-corpus identifiers; the multivocal
`MV-TC-2` cited in Branch 1's rev-3 note is a DIFFERENT handoff (finding REV-1-3).**
**Tier:** T5 (the distinction is stated in a
preprint the corpus carries at abstract depth,
[Gebele, Mutzel & Matthes 2026](https://arxiv.org/abs/2608.00666)); the venue side
is T2-*unretrieved*.

**Claim at issue.** That an arbitrage which exists in payoff space is realisable
only if the venue's rules permit the specific pre-settlement position
transformations the strategy requires — so that "arbitrage exists" and "arbitrage is
executable" are different claims with different evidence.

**Falsification test.**
- **Unit of analysis:** the (payoff-space arbitrage, venue rule set) pair.
- **H0:** the set of payoff-space arbitrages on this venue's contract families is
  **equal** to the set realisable under the venue's stated pre-settlement
  transformation rules, against the alternative that the realisable set is a proper
  subset.
- **Statistic:** the cardinality ratio realisable / payoff-space, enumerated over a
  stated contract-family census rather than sampled.
- **Refutation condition:** H0 is refuted by the exhibition of **one** payoff-space
  arbitrage that the rule set forbids. This is a single-counterexample test and
  needs no multiplicity control — which is why it is worth stating separately from
  branch 1 rather than folding into it.
- **Symmetry the branch must not lose:** the converse is also informative. A
  transformation the rules permit that creates a realisable position with no
  payoff-space counterpart would refute the *framing*, not just H0.

**Preconditions.** Branch 0 (permitted transformations — TC-1); the contract-family
census. Marked `not-transferable-as-stated` in the corpus until Branch 0 returns.

**Rev-3 note.** Branch 7 is this branch's documentary sibling and the two must not be
merged: Branch 5 asks whether the *permitted-transformation* rule set is binding on a
payoff-space arbitrage; Branch 7 asks whether the *public document set* decides
executability at all, given that three of its most decision-relevant components are
withheld at source. Branch 5 can be refuted while Branch 7's H0 survives, and the
converse.

---

## Branch 6 — Are the corpus's own unresolved strata hiding the answer?

**From:** G-5, G-7, G-10, H-1, H-2 — **predecessor-corpus identifiers throughout the
original test; the rev-3 extension below cites the multivocal corpus and carries the
`MV-` prefix.** **Tier:** n/a — this is a branch about the
corpus, and it is the only branch whose object is the evidence base rather than the
market.

**Claim at issue.** That the corpus's declared gaps are gaps in the *literature*
rather than gaps in this *search*.

**Falsification test.**
- **Unit of analysis:** the gap statement.
- **H0:** for each of G-1, G-2, G-4 and G-5, no record in the **510 residual** X11
  stratum, the 545 X10 stratum, the 3,090 title-only DEFAULT-X1 stratum **or the 178
  records amendment A16 admitted but never extracted** states the thing the gap says
  is absent. **The fourth set is new at rev 2 and it is the easiest to reach**, because
  those records are already read to abstract depth, already carry persistent
  identifiers, and are already in the corpus — they were simply never extracted.
  **A first, cheap pass of this branch is therefore available now**: screen the 178
  abstracts against G-4's predicate ("states a market-making model fitted to or
  calibrated on Kalshi") and against G-5's ("states a payoff support or an
  applicability condition for a bounded payoff"). Nothing in Branch 0 blocks it.
- **Statistic:** a targeted screen of those strata, read rather than classified,
  against the gap's own predicate. The strata are enumerated in
  `ka-screening-verdicts.jsonl` and, for the 190 records amendment A16 decided, in
  `ka-s4-completion-screen.jsonl`, so the sampling frame is fixed and published.
  **A16 is a worked precedent for this branch's method** — a subset rule fixed and
  hashed before assessment, one verdict per record with the criterion cited, and the
  residual counted and published — and a successor should follow it rather than
  reinvent it. **One caution A16 supplies:** 88 of the 503 residual X11 records could
  not be read past a title, 78 of them on HTTP 429 rate limits and 19 on HTTP 403 bot
  blocks (`ka-s4-retrieval-log.json`). **A screen that scores those as "does not state
  it" will manufacture the very absence the branch is testing.**
- **Refutation condition:** H0 is refuted for a gap by **one** record in those
  strata that states what the gap says is absent. Each such record also converts a
  corpus-record gap statement into a corpus-record error, which goes to
  [failure_log.md](../../failure_log.md) under the charter's null protocol.
- **Why this is a genuine test and not a chore:** the corpus itself declares its
  absences bounded to what it read (G-2, G-4, "Qualified under finding REV-1-10"),
  so the branch has a real chance of failing, and failing would change what
  branches 1, 2 and 4 may claim as novel.
- **Precondition, not part of the test:** the backward citation-chasing arm never
  ran (G-7, amendment A6) because it needs full texts. Running it is a retrieval
  task and belongs under preconditions.

**Minimum detectable effect, not retrospective power** (charter). Before screening,
state the smallest number of hits in the stratum that would be treated as refuting
each gap. That number is `TO COMPUTE` from the stratum size and the screening
budget; it must be fixed **before** the screen, or the test is unfalsifiable.

**Rev-3 extension of the same branch to the second corpus, stated as an extension
rather than a new branch because the test is identical.** The multivocal corpus adds
**1,465 undecided `G1` rows** — 528 academic and 937 software — for which **no
eligibility determination was ever made** (**MV-G-5**, **MV-G-6**), and its handoff
**MV-TC-13** already names the procedure: a later session decides them *"as a numbered
amendment stating the subset rule it applied, fixing that rule BEFORE any record in
the subset is assessed"*. The caution transfers with the method and is sharper in the
second corpus than in the first: **53 of 56 Semantic Scholar attempts returned HTTP
429**, RePEc's interface never returned a result set at all, and GitHub's code-search
and Kaggle's kernel endpoints both returned HTTP 401 unauthenticated, so **no
code-level and no notebook search was executed** (**MV-G-9**, **MV-G-22**, and
**MV-G-26** — *added to that corpus record by round-1 remediation on 2026-09-04 and
cited here under findings CRITICAL-2-3 / SCOPE-2-7: **RePEc was never searched**, all
nine attempts having been served the search form rather than a result set, so no
RePEc row is a search result at all* — and
[failure_log.md](../../failure_log.md) **F007**). Scoring any of those as "states
nothing" manufactures the absence.

---

## Branch 7 — Does the PUBLIC document set decide executability for any stated strategy class?

**From:** **MV-G-2**, **MV-G-3**, **MV-G-4** — the three objects the multivocal
corpus records as **WITHHELD AT SOURCE** rather than merely unretrieved — with
**MV-TC-7** (the competitive quoting floor, *"not computable from any public
document"*) as the worked instance and **MV-G-17**/**MV-G-18** bounding the class
census. **Tier:** T2 for the venue
and regulator clauses this branch reads; **T5** for the strategy-class census, whose
rows rest on S-C and S-E records because the multivocal corpus contains **no T1
records at all** (**MV-G-5**, hazard H-6). **No part of this branch claims T1.**
**Carried from hazard H-10 (MV-G-27):** the S-E rows in that census rest on digests
that are **attested, not verifiable**, so the census is cited as attested at its
retrieval date.

**Claim at issue.** That a participant can determine, from public documents alone,
whether a stated strategy class is executable *for them*. This is the premise every
other branch in this agenda silently assumes when it says a precondition is
"checkable", and hazard H-7 is the reason it is no longer safe to assume.

**Why this is a test and not a survey.** The claim forbids a specific state of the
world: that there exists a class whose executability verdict *changes* depending on
the value of a document nobody outside the exchange and the regulator can read. One
such class refutes it. The branch is enumerative, needs no market data, no API call
and no venue access, and can be run entirely against documents already retrieved.

**Falsification test.**
- **Unit of analysis:** the (strategy class, precondition) pair, over the corpus's
  own **T1–T8** census as published, with the census version fixed and hashed before
  enumeration (**A3-TC-1**).
- **H0:** for every class in the census, every precondition its **own sources** state
  it depends on is decided by the SETTLED set (corpus §9.1) — equivalently, the
  withheld-at-source set (§9.2) is disjoint from the union of stated preconditions.
  The alternative is that at least one class's verdict turns on a withheld object.
- **Statistic:** the count of (class, precondition) pairs whose decision requires an
  element of the withheld set, **enumerated exhaustively over a fixed census, not
  sampled**, reported together with the census digest and the substitution table.
  There is no sampling variance to report and none is invented; what is reported
  alongside the count is the **per-pair verdict list**, so that a reviewer can
  disagree pair by pair.
- **Surrogate / comparison — a two-reconstruction contrast, because a bare count of
  "things we cannot read" is not a test of anything.** Run the enumeration twice:
  (i) **withheld-as-unknown**, in which any precondition depending on a withheld
  object is `undetermined`; (ii) **most-permissive reconstruction**, in which each
  withheld object is replaced by the most permissive value the *public* documents
  bound it to — for example, position accountability levels bounded above by the
  federal ceiling that sits above the exchange's own (`d17`, `d21-c2`), and
  market-maker obligations bounded only by the fact that the four dimensions are
  **named with no value stated** (`d19-c5`), i.e. effectively unbounded. **A class
  whose verdict is identical under both reconstructions is NOT decided by the
  withheld object. A class whose verdict flips IS.**
- **Negative control on the procedure itself, required, and modelled on the charter's
  `construct` gate condition (v):** apply the same substitution to preconditions that
  are **settled** — fee incidence and functional form (`d01`), tick and settlement
  value (`d21-c3`, `d21-c4`), full cash collateralisation (`d13-c2`, `d14-c2`). Their
  verdicts **must not flip**. If they do, the enumeration procedure is unstable, the
  contrast measures the procedure rather than the documents, and **the test is void
  and reports nothing**.
- **Aggregation rule:** per class. The branch-level proposition is an **existence**
  claim in the refuting direction, so a single flip refutes H0 and **no multiplicity
  control is required** — the same reasoning Branch 5 gives for its
  single-counterexample structure. If a successor instead reports the *proportion* of
  classes that flip as a finding about the venue, that is a different and weaker claim
  over a census that is not a random sample of anything, and it must be labelled as
  such.
- **Refutation condition:** H0 is refuted by the exhibition of **one** class whose
  executability verdict flips between the two reconstructions. **The converse is the
  informative outcome and the branch must not treat it as a failure:** if no class
  flips, then the withheld appendices are **not executability-decisive for the classes
  as stated**, which would be a substantive result and would materially cheapen every
  other branch in this agenda.

**`TO COMPUTE`, with the selection procedure named — no bare numbers.**
- **A3-TC-1** — the class × precondition census version and the substitution table.
  **Selection procedure:** take the census from the multivocal corpus's §8 table as
  published; derive the substitution table from §9.1 and §9.2 only; fix and hash both
  **before** any enumeration, following the worked precedent of the predecessor
  branch's amendment A16 and the multivocal protocol's §4.4 rule 4 (a subset rule
  fixed and hashed before assessment, one verdict per row with the criterion cited,
  the residual counted and published).
- **A3-TC-7** — an MDES if, and only if, any statistical comparison is later attached
  to this branch. **Selection procedure:** corpus handoff **MV-TC-12** — minimum
  detectable effect size computed pre-data against a **sourced** comparator and a
  stated target detection probability, **never** retrospective power (charter step 2).

**Preconditions.** The §8 census and the §9.1/§9.2 tables, all in hand. **Two bounds
on the census that must be carried into the result:** the Maker Order Protections
Program document was not retrieved and the class that depends on it rests on a
practitioner's quotation at **secondary** depth (**MV-G-17**), and the venue's Combos
help article — which the source behind the combination class states is *controlling* —
was not retrieved either (**MV-G-18**). **Not blocked on Branch 0**, which is the
point: this is the only branch in the agenda that is fully runnable today.

**Scope boundary.** The branch returns **verdicts** — decided, undetermined,
flips-on-a-withheld-object — and never a gap value, a size, a rule or a return.

---

## Branch 8 — Is the rule surface in force at a past instant reconstructible?

**From:** **MV-G-1** (*the rulebook in force on 2026-09-04 was not located*), with
**MV-G-24** (grey-literature content drift unmitigated) and **MV-G-25** (no
web-archive snapshot was created for any retrieved page, and recording digests
instead is a **project design choice with no cited source**). **Tier:** T2 for the
documents and
the regulator's filing register; the failure record itself is this project's own
execution log and carries no tier.

**Claim at issue.** That a point-in-time study of this venue can state the rule text
in force at each of its timestamps. **Every other branch in this agenda, and H001,
assumes this silently** — a fee function, a tick, a position limit, a close time and a
settlement rule are all dated facts on a surface the venue may amend on **ten**
business days' notice for a rule change (`d22-c1`) and **one** business day for a
product listing (`d22-c3`), with the member agreement separately amendable
unilaterally on notice with deemed agreement absent termination (`d02-c3`). **No
version of the executability preconditions is contractually stable for a
participant**, and this branch is where that fact is made falsifiable instead of
lamented.

**Why this is NOT a retrieval task, stated explicitly because it is the obvious
objection and because Branch 0 is the counter-example in the same document.**
Retrieving one document is a precondition and belongs to Branch 0. The object here is
different: it is the **reconstructibility of the mapping from timestamp to rule
text**, over a census fixed in advance — a property of the documentary world that can
be false, is checkable, and has a stated refutation condition. **If a reviewer is not
persuaded by that distinction, the correct disposition is to demote this branch to a
second precondition branch alongside Branch 0 — not to keep it as a test.** That
disposition is offered here rather than defended away.

**Falsification test.**
- **Unit of analysis:** the (rule surface, timestamp) pair.
- **H0:** for every timestamp in the registered census, the text of each named rule
  surface in force at that timestamp is recoverable from a retrievable, dated
  document. The alternative is that at least one (surface, timestamp) pair has no
  recoverable text.
- **Statistic:** the recovery count over the census — recovered / attempted — with
  **every attempt carrying its HTTP outcome and the byte digest of what it returned**,
  and every failure classified into the corpus's own taxonomy: `WITHHELD AT SOURCE`,
  `NOT LOCATED`, `DEGRADED` (extraction damage, **DI-7**), `NOT MACHINE-READABLE`
  (HTTP 200 with no rule text in the bytes), `MIS-SERVED` (**DI-1**). **A bare
  recovery rate is not reported**: the taxonomy is the result, because the four
  classes have different remedies and averaging them hides exactly the distinction
  hazard H-7 exists to preserve.
- **Positive control, required:** timestamps for which an effective date **is**
  documented — the self-certified filings enumerated in the regulator's own register,
  and the notice periods `d22-c1`/`d22-c3` imply. The procedure **must** recover
  those. If it cannot recover a rule surface whose filing the regulator itself
  enumerates, the failure is in the **retrieval route**, not in the archive, and the
  branch has measured its own instrument.
- **Negative control, required, and it is not hypothetical:** a timestamp **before**
  the venue's designation, for which **no** rule surface should be recoverable. A
  procedure that "recovers" one is matching on the wrong object — and that failure
  mode is live rather than theoretical, because the regulator's index is already
  recorded as serving **another venue's rulebook** under this venue's label
  (**DI-1**, **MV-G-8**, hazard H-8). **Every retrieved document must be
  identity-checked against its own title block before it is counted as a recovery**;
  the corpus's own check — counting occurrences of the venue's name in the extracted
  text — is the cheap version and is adopted here by reference to that defect record.
- **Aggregation rule:** per (surface, timestamp). The branch's claim is **universal**,
  so it is refuted by one pair with no recoverable text and needs no multiplicity
  control. **The claim in the other direction — that point-in-time work is feasible on
  this venue — is not an existence claim and requires the whole census**, which is why
  the census must be fixed before any retrieval and not grown to fit what was found.
- **Refutation condition:** H0 is **already refuted in one direction by the record in
  hand** — the rulebook in force on the retrieval date was not located, at five
  candidate PDF paths and two client-rendered surfaces, and the reachable copies are a
  2019 redacted version, a 2023 redline whose text extracts corrupted, and a
  mis-served document that is not this venue's. So the branch's live content is not
  *whether* H0 fails but **over what scope**, and the census fixes the scope.
  **Refutation condition for the branch's own premise**, on the model Branch 0 uses:
  if a session with a working route establishes that the rulebook is **not publicly
  published in machine-retrievable form at all**, the premise that a route exists is
  refuted, the blocker becomes **permanent**, and every point-in-time branch in this
  agenda must carry it as a standing limitation rather than as a pending precondition.

**`TO COMPUTE`, with the selection procedure named.**
- **A3-TC-2** — the (surface, timestamp) census. **Selection procedure:** enumerate
  surfaces and dates from the regulator's own filing register — **111 enumerated
  filings**, of which five, or four, were retrieved (the venue arm's log states both
  counts; **DI-6**, **MV-G-7**, and this agenda does not resolve the inconsistency) —
  and from the venue's stated notice periods; fix and hash the census **before** any
  retrieval, per the §4.4 rule-4 precedent. **No count and no date range is chosen by
  hand.**
- **A3-TC-7** — MDES per **MV-TC-12** if any statistical comparison is attached. Never
  retrospective power.

**Preconditions.** A retrieval route that survives the venue's bot mitigation — the
same precondition Branch 0 carries, and the reason these two branches are adjacent
rather than merged. **Carried, not resolved:** DI-6's count inconsistency, and DI-1's
mis-served document. **Carried from hazard H-10 (MV-G-27), and it bears directly on
this branch's method:** the corpus's own choice to record a digest *instead of*
creating an archive snapshot is precisely what MV-G-25 flags as unsourced, and for the
S-D and S-E bytes the digest is not even recomputable by a reader — so this branch's
own statistic, which requires *"the byte digest of what it returned"* per attempt,
must archive its bytes or state in its output that its digests inherit the same
attested-not-verifiable status.

**Blocks:** every branch that states a dated venue fact — 1, 3, 5, 7, 9, 10, 11 — in
the specific sense that each of them may state its fact **as of the retrieval date**
and may not state it as of any other date until this branch returns.

---

## Branch 9 — Is a headline-matched cross-venue pair one proposition, or two?

**From:** **MV-TC-3**, which does not merely permit but **requires** a
settlement-clock and definition alignment test before any cross-venue gap is
computed — *"the minimum tradeable gap for a cross-venue pair … only after a
settlement-clock and definition alignment test per `KSL-C14`"* — together with
**MV-G-20** (CME, Betfair and PredictIt rule surfaces **not retrieved**: HTTP 403,
HTTP 403, and HTTP 200 client-rendered respectively; sportsbook house rules not
attempted) and **MV-G-1**. *(Note the collision this prefix resolves: the
PREDECESSOR corpus's bare `TC-3`, which Branch 4 derives from, is the capital-lockup
handoff and is a different object — finding REV-1-3.)* **Tier:** T2 for the
paired-venue clauses that were
retrieved (`d25`, `d26`, `d29`); **T5** for `KSL-C14`, the lateral record that
states the precondition and which the corpus marks as *a precondition that
NEGATES the ordinary class*. **And `KSL-C14`'s payload bytes are NOT ARCHIVED, so its
digest is attested and not verifiable (MV-G-27, hazard H-10)** — this branch's entire
warrant is therefore an attested T5 clause, which is stated here at the head rather
than discovered by a successor.

**Claim at issue.** That two contracts on different venues carrying the **same
headline event** resolve on the **same proposition** — so that a price difference
between them is a *discrepancy* rather than a difference between two contracts. Rev
2's Branch 4 assumed this in its unit of analysis, the "(event, venue-pair,
timestamp) triple". Rev 3 makes it a proposition instead of a premise.

**Falsification test.**
- **Unit of analysis:** the (headline, venue-pair, contract-pair) triple, over a
  census of matched headlines fixed before matching (**A3-TC-3**).
- **H0:** for every matched pair, the two **filed terms** agree on every enumerated
  definitional dimension: settlement source; observation window and settlement clock;
  first-publication and revision treatment; source-unavailability handling;
  expiration-timing discretion; and the mutual-exclusivity and rounding convention.
  The alternative is that at least one dimension diverges, in which case the pair
  prices two different propositions and **no arbitrage statement is available at all**.
- **Statistic:** the per-pair **divergence vector** over the enumerated dimensions,
  and the count of pairs with a non-zero vector, enumerated over the fixed census
  rather than sampled. **A dimension that is undecidable from the public documents is
  recorded `undetermined` and the pair is NOT scored as aligned** — an undetermined
  dimension is not agreement. This is the same discipline that failure_log F007
  applies retrospectively to an unexecuted query, applied here prospectively.
- **Surrogate / negative control, required:** deliberately mis-paired contracts —
  each venue-A contract paired with a venue-B contract from the **same family but a
  different threshold or a different date**. The alignment procedure **must** return
  divergence on those. If it returns "aligned" for contracts known to be mis-paired,
  it has no discriminating power and **the test is void**.
- **Positive control, required:** two contracts from the **same venue and series** at
  adjacent rungs, which must return alignment on every dimension **except** the
  threshold. A procedure that finds spurious divergence there is measuring extraction
  noise — a live risk, since two of the corpus's own S-D records extract with damage
  (**DI-7**, hazard H-8) and their text must never be re-quoted as clean rule text.
- **Aggregation rule:** per pair. The proposition "the same headline is one
  proposition" is universal, so **one** divergent pair refutes it and no multiplicity
  control is needed for the alignment test itself. **If any executable statement is
  later attached to a surviving aligned pair, it inherits family-wise control** —
  corpus handoff **MV-TC-14**, [White 2000](https://doi.org/10.1111/1468-0262.00152)
  reality check or [Hansen 2005](https://doi.org/10.1198/073500105000000063) SPA,
  adopted by explicit reference under
  [ADR-0004](../decisions/ADR-0004-quant-rule-adoption-prediction-markets.md).
- **Refutation condition:** refuted by **one** matched pair diverging on any
  enumerated dimension. **The branch's prior is that H0 fails**, because `KSL-C14`
  already states the settlement-clock and definition basis as a precondition that
  negates the ordinary cross-venue class; so the informative outcome is the *other*
  one — **a pair that aligns on every dimension** — and the branch's real product is
  the **divergence taxonomy**: which dimension diverges, how often, and whether any
  dimension ever aligns.

**Why the venue documents make this more than a definitional quibble.** The corpus
records, at full-text depth, that the paired US venue's maker coefficient is
**negative** where this venue's maker is **charged** — *"Any strategy assuming
symmetric maker treatment across a pair is mis-specified at the point of writing"*
(`d25-c2`, `d25-c3`, `d29-c2`) — and that the paired venue **drops orders under
latency**, with a five-second stopgap rejecting unprocessed inbound orders under a
reject message the venue itself admits is misnamed (`d26-c3`, `d26-c4`), so that leg
risk is concentrated exactly in the states where a discrepancy would appear. **The
alignment question is therefore prior to, and cheaper than, any price work**, and a
successor that measures gaps before running this test is measuring the difference
between two contracts and calling it a discrepancy.

**`TO COMPUTE`, with the selection procedure named.**
- **A3-TC-3** — the matched-headline census and the definitional-dimension list.
  **Selection procedure:** dimensions taken **only** from the clause set already
  retrieved (settlement source `d21-c11`-adjacent, clock and expiration discretion
  `d17-c9`/`d21-c5`…`d21-c10`, revision treatment `KSL-C15`/`KSL-C16`, unavailability
  `d21`), never invented; the census fixed and hashed before matching, per §4.4
  rule 4. **`KSL-C15` and `KSL-C16` are attested-not-verifiable digests** (MV-G-27,
  hazard H-10), so the revision-treatment dimension is labelled as resting on an
  attestation wherever it appears in the divergence vector.
- Downstream and explicitly **out of scope here** (ADR-0003): **MV-TC-3**'s
  studentised time-series bootstrap for pairwise comparison
  ([Ledoit & Wolf 2008](https://doi.org/10.1016/j.jempfin.2008.03.002), adopted by
  explicit reference under ADR-0004), which may be applied only to pairs this branch
  returns as aligned.

**Preconditions.** **MV-G-20 blocks the filed-terms half for most candidate pairs** —
three comparison venues' rule surfaces were not retrieved at all — and **MV-G-1**
blocks this venue's rulebook. The paired US venue's clauses (`d25`, `d26`, `d29`) are
in hand and are the one pair for which the test is partly runnable today. **Branch 8
governs whether any of it is stateable as of a date other than the retrieval date.**

**Scope boundary.** The branch returns an **alignment verdict and a divergence
taxonomy**. It never returns a gap, a spread, a size or a return.

---

## Branch 10 — Is the capital-lockup term bounded?

**From:** **MV-G-12** — *two venue pages state different collateral interest rates*
(defect **DI-4**: a help-centre page states the rate is "set at 3.25%", a second venue
page headlines 4.05%; both retrieved in the same pass; **recorded, not resolved**) —
together with **MV-TC-12** (MDES, never retrospective power) and the corpus's §9.1
entry *"Capital lockup has no stated upper bound"*: settlement is *"no later than the
day after the Expiration Date, **unless** the Market Outcome is under review"*, and
**no maximum review duration is stated** (`d21-c10`), with venue documentation
separately stating settlement timing *"can vary"* (`d07-c2`). **Tier:** T2 for the
clauses; the two conflicting rate figures are **quoted, attributed and NOT ADOPTABLE**
(hazard H-9, **MV-G-23**). **The `KSL-` clauses this branch relies on — `KSL-C09`,
`KSL-C30`, `KSL-C32` — carry attested-not-verifiable digests (MV-G-27, hazard H-10)**,
so the documentary half below is cited as attested at its retrieval date.

**Claim at issue.** That the cost of capital locked in a position until settlement is
a **bounded, computable term** that can be netted into an executability statement.
Rev 2's Branch 4 called this parameter "the parameter that decides this test" and
recorded that it "has no source". **Rev 3's correction:** the multivocal corpus
supplies the **documentary** half — positions are **fully cash collateralised** with
no leverage on the binary leg (`d13-c2`, `d14-c2`), only net positions settle
(`d07-c1`), interest accrues on the collateral behind open positions (`KSL-C09`), and
settlement is next-day **unless** a review intervenes, with the review's duration
unstated — and it leaves the term **uncomputed**, with the rate itself **contradicted
between two of the venue's own pages**.

**Falsification test.**
- **Unit of analysis:** the (market, settlement event) pair.
- **H0:** realised time from expiration to settlement is bounded by the documented
  next-day term, **and** its distribution does not differ between markets that entered
  a Market Outcome Review or dispute state and those that did not. The alternative is
  a right tail that the documented term does not bound, concentrated in the review
  stratum.
- **Statistic:** the difference between the review and non-review strata in the
  settlement-lag distribution — location **and upper-tail quantiles**, because the
  claim is about the tail and a location-only comparison would answer a different
  question. Interval by bootstrap; where the series is time-indexed, standard errors
  per corpus handoff **MV-TC-15** — Newey–West HAC with the
  [Newey & West 1994](https://doi.org/10.2307/2297912) data-dependent bandwidth or the
  [Andrews 1991](https://doi.org/10.2307/2938229) plug-in, adopted by explicit
  reference under ADR-0004. **Quantile choice and bandwidth are `TO COMPUTE` with the
  rule named; neither is a number chosen here.**
- **Surrogate:** **label permutation** — permute the review / non-review labels
  **within expiration date**, preserving the calendar and the venue's operating
  structure while destroying the review correspondence. The calendar must be preserved
  because the venue documents a **recurring scheduled dead window**, a Thursday
  03:00–05:00 ET maintenance trading pause under which resting orders behave
  differently depending on the pause type (`d10-c1`…`d10-c3`); a surrogate that
  ignores it manufactures a lag difference out of the maintenance schedule. **A
  duration- or returns-resampling surrogate is NOT admissible**, for the reason rev
  2's Branch 4 already gives: it destroys the settlement-endpoint structure the claim
  depends on.
- **Aggregation rule:** per series first, then family-wise across series under
  **MV-TC-14** (White 2000 reality check or Hansen 2005 SPA, adopted by explicit
  reference under ADR-0004). The per-series step comes first because the corpus
  records that expiration timing is movable **in both directions at exchange
  discretion** and that sole-discretion Market Outcome Review may be initiated before
  settlement on **every** contract in a series (`d17-c9`, `d21-c5`…`d21-c10`), so
  series are not exchangeable.
- **Refutation condition:** the claim — that lockup is an **unbounded** cost term —
  is refuted if the review-stratum lag distribution is indistinguishable from the
  permuted surrogate **and** the observed upper tail lies inside the documented
  next-day term. **It is not refuted by a small difference in means**; it is refuted
  by an upper tail the surrogate reproduces. Conversely, **one** settlement lag
  outside the documented term with a review state recorded establishes that the
  documentary gap has an economic counterpart — and that single observation is enough,
  because the claim under test is about the existence of an unbounded tail.

**The rate is `TO COMPUTE` and may NOT be taken from either venue page.**
- **A3-TC-5** — the carry rate. **Selection procedure:** a funding-cost series stated
  with its source and matched to the realised lockup horizon this branch measures.
  **The two conflicting venue figures are used for exactly one purpose — as the
  endpoints of a SENSITIVITY RANGE over which the conclusion's stability is
  reported** — and for no other. Quoting either as *the* rate would adopt a number
  the corpus records as contradicted by the same venue on the same day (**MV-G-12**,
  **DI-4**), and would be the defect hazard H-9 exists to prevent.
- **A3-TC-4** — the tail quantile and the interval method. **Selection procedure:**
  the quantile fixed before data against the **sourced comparator** the charter's
  step 2 requires — here the venue's own documented next-day term, which is a
  decision-relevant threshold stated by a document rather than a judgement call;
  interval method per MV-TC-15 above.
- **A3-TC-7 / MV-TC-12** — the MDES, computed **pre-data**, against that same sourced
  comparator and a **stated target detection probability**, which is itself a
  `CONVENTION` requiring provenance under charter commitment 3. **Retrospective power
  is never computed** (charter step 2; [Hoenig & Heisey 2001](https://doi.org/10.1198/000313001300339897)).

**Preconditions.** Per-market settlement timestamps and market states — **out of
scope here** (ADR-0003) and belonging to an executing project. The identification
route the corpus supplies is `KSL-C32`: **dispute and re-determination are
machine-readable market states**, which is what makes the two strata separable at all.
**`TO COMPUTE` before the census exists:** the universe filter **MV-TC-8**, separating
single-outcome markets from the auto-generated combination markets that flood the raw
feed (`KSL-C30` states the requirement and **no rule**) — without it the census is
dominated by combinations and the lag distribution is a statement about
auto-generation. **Both `KSL-C32` and `KSL-C30` are attested-not-verifiable
(MV-G-27, hazard H-10)**, so a successor that cannot reproduce the machine-readable
state names from the live API must treat the identification route as unconfirmed
rather than assume the attestation still describes the feed.

**Scope boundary.** The branch returns a **lag distribution, a stratum contrast and a
carry-rate sensitivity range**. It never nets a cost into a return, never states a
size, and never states a rule.

---

## Branch 11 — Are the venue's stated operational limits reconcilable to ONE basis?

**From:** **MV-G-11** (*throughput is stated on four incompatible bases across the
venue set and is not reconciled*; defect **DI-5**) and **MV-TC-5** (*achievable order
rate … a function of API tier, which is endogenous to the participant's trailing
volume share and to total exchange volume; must be stated per tier and never as a
venue constant*), with **MV-G-19** (*block threshold in contracts and position limit
in USD of exposure are in different units and no document reconciles them*) as the
same failure mode in a second place. *(The PREDECESSOR corpus's bare `TC-5`, cited in
Branch 3's preconditions, is the 2025 asset-class composition handoff and is a
different object — finding REV-1-3.)* **Tier:** T2 throughout — every statement this
branch enumerates is a venue or paired-venue document.

**Claim at issue.** That the venue's published operational limits can be expressed on
a single basis, so that a specification can state the order rate and the position
ceiling a strategy requires and **check them against the documents**. Every branch in
this agenda that says a design is "feasible within the venue's limits" is asserting
this.

**The contradiction the corpus already records, which is why the branch's prior is
that H0 fails.** Two venue pages state a flat *"~100 requests per second per API
key"* as a **default** (`d03-c2`, `d04-c3`); the **authoritative** document meters a
**token bucket** in which most requests cost 10 tokens, write traffic draws on a
budget separate from reads, the signup tier is 100 tokens/s write = 10 orders/s, and
100 requests/s is the **Premier** tier rather than the default — with the top tiers
**earned from volume share or assigned at the venue's discretion**, and **batching
does not relax the ceiling** (`d06-c1`…`d06-c9`). The paired venue states a flat 20
requests/s per key with no ladder (`d26-c1`). **The corpus performs no conversion and
neither does this branch**; producing one is the branch's work.

**Falsification test.**
- **Unit of analysis:** the (limit statement, limit statement) **pair**, over the
  enumerated statement set — `d03-c2`, `d04-c3`, `d06-c1`…`d06-c6`, `d26-c1` for
  throughput; `d16-c1` and `d20-c1` for size.
- **H0:** there exists a **single conversion** under which all enumerated statements
  are simultaneously satisfiable — equivalently, no pair of statements admits a value
  that one permits and another forbids. The alternative is that at least one pair is
  contradictory under every admissible conversion.
- **Statistic:** the **contradiction set** — the enumerated list of contradictory
  pairs under the best available conversion, exhaustive over pairs. The conversion
  itself must be stated **as a function with its inputs named**, and every input
  either quoted from a clause **with its id** or marked `undetermined`: tokens per
  request, the read/write budget split, the tier-assignment rule and its trailing
  volume-share definition with its stated earn/keep hysteresis, and — for the size
  half — the price at which a contract count converts to USD of exposure, which is
  itself a variable and not a constant. **No rate is reported as a single number**;
  the output is a set and a function.
- **Positive control on the conversion, required:** apply it to two statements the
  **same** document makes about the **same** tier (`d06-c1`, `d06-c2`), which are
  mutually consistent by construction. **If the conversion contradicts a document
  with itself, the conversion is wrong and the documents are not**, and the branch
  reports nothing until the conversion is repaired.
- **Negative control, required:** a deliberately wrong conversion — for instance one
  that treats every request as costing a single token, ignoring the stated per-request
  cost — **must** produce contradictions that the correct conversion does not. A
  conversion under which nothing ever contradicts is not detecting anything.
- **Aggregation rule:** exhaustive over pairs, so there is **no sampling and no
  multiplicity control** — every pair is examined and the result is a set, not an
  estimate. Reporting a "contradiction rate" would imply a sample that does not exist.
- **Refutation condition:** H0 is refuted by **one** contradictory pair. **Standing
  consequence, which is the branch's actual product:** until the contradiction set is
  **empty**, no branch, no hypothesis design and no specification in this project may
  state an achievable order rate as a venue constant — **MV-TC-5's per-tier form is
  the only admissible expression**, and it must carry the tier's endogeneity to the
  participant's own trailing volume share and to total exchange volume. Position-size
  statements inherit the identical rule from **MV-G-19** until the contracts-versus-USD
  reconciliation is stated with the price it assumes.

**`TO COMPUTE`, with the selection procedure named.**
- **A3-TC-6** — the conversion function and its inputs. **Selection procedure:** every
  input taken **verbatim from a clause with its id**, or marked `undetermined` and
  propagated as such; **no input is fitted, chosen or assumed**, because the object
  under test is whether the documents cohere and a fitted input would make them cohere
  by construction.

**Preconditions. NONE beyond the clauses already retrieved.** This branch requires no
market data, no exchange API call, no account and no venue access, and it is
therefore — with Branch 7 — **the cheapest branch in the agenda and the one a
successor should run first.** Two carried caveats: the throughput clauses are dated by
retrieval and amendable on the notice periods in `d22` (Branch 8's object), and the
tier ladder's top rungs are **assigned at the venue's discretion**, so a conversion
can describe the ladder without predicting any participant's place on it.

**Scope boundary.** The branch returns a **contradiction set and a conversion
function**. It never states an achievable order rate for any participant, a position
size, or a return.

---

## Relationship to `research/01_hypothesis_register/H001/design.md` (new at rev 3)

**H001 is a DRAFT and is explicitly NOT FROZEN.** Its own front matter states that
`/preregister` has not been run, that no ReproLog has been emitted for it, that no
commit carries it, and that **its SHA-256 is therefore not a registration hash but the
digest of a draft that is expected to change**. Nothing in this agenda may cite it as
a registered design, and this section exists so that the overlap is stated rather than
discovered.

**Where H001 overlaps this agenda, and which is the parent.**

| overlap | parent | why |
|---|---|---|
| **Intra-series coherence on cumulative threshold ladders** | **Branch 1 is the parent; H001 is the child.** | Branch 1 states the general coherence claim over mutually exclusive and exhaustive families; H001 instantiates one case of it — a single cumulative threshold ladder, one instant — and pre-commits a statistic, two null constructions, an aggregation rule, a refutation condition and an MDES for that case. A child may be narrower than its parent and must not be broader; H001's H0 is a statement about the worst-case settlement payoff of an **order set**, not about a price sum, and is therefore strictly narrower than Branch 1's residual claim. |
| **The mandatory comparator** | **Neither; they agree independently.** | H001 §1.6 ("What it must beat") and the always-NO baseline registered as the transferable positive of [failure_log.md](../../failure_log.md) **F008** are the same obligation reached by two routes. Recorded because independent agreement is worth more than a cross-citation. |
| **The fee function and the rounding direction** | **Branch 7 is the parent for whether the document set decides them; H001 consumes them.** | H001 §1.3 treats the cost function as documented rather than assumed. Branch 7 asks whether that documentation is sufficient in general; **DI-3/MV-TC-2** is the live limit for both — the per-series multiplier is in the retrieved bytes and not extractable. |
| **Capital lockup** | **NO OVERLAP, stated so a reader does not assume one.** | Branch 10's object is the hold-to-settlement carry term. H001's H0 is defined at **one instant** on **one book** and carries full cash collateralisation without a lockup term. H001 would consume Branch 10's output only if it were extended to a hold-to-settlement variant, which its §1.1 H0 does not describe. |
| **Point-in-time rule surface** | **Branch 8 is the parent.** | H001's §8.1 point-in-time discipline is a leakage condition on data; Branch 8's object is whether the **rule text** in force at a past instant is recoverable at all. A design that pins its data to a timestamp but not its rule surface has pinned half of what it needs. |

**No branch above is derived from H001**, and H001 is not a gap or a handoff. It is
cited here as a related specification, never as a source of a branch.

---

## Cross-branch open questions

- **Is "the venue" a single object across time?** The 2025 asset-class boundary
  (TC-5, the predecessor corpus's) means a statistic estimated across it may be
  measuring a composition
  change. Every branch that pools across it inherits this. **Sharpened at rev 3:**
  the multivocal corpus adds a second sense in which the venue is not one object
  across time — its **terms** are unilaterally amendable on notice with deemed
  agreement absent termination (`d02-c3`), rule changes take ten business days'
  notice and product listings one (`d22-c1`, `d22-c3`), and the rulebook in force on
  any given date is not located (**MV-G-1**). Composition drift and rule drift are
  different problems with different remedies, and Branch 8 is the second one's home.
- **Does the bounded-payoff restriction change the *question* or only the model?**
  **Partly answered at rev 2, from a full text rather than an abstract.** Branch 2
  tests whether the lineage's results survive substitution. It does not ask whether
  the right maker for a [0,1] payoff belongs to that lineage at all — and
  [Feil & Nendel 2026](https://arxiv.org/abs/2607.17991) **[FT]** answer that question
  in the negative for their own setting, by building the control problem natively:
  settlement `Y` in `{0,1}`, price a martingale in `(0,1)`, quotes constrained to
  `[0,1]`, and an objective carrying a **terminal settlement risk penalty** the
  classical mark-to-market problem has no analogue of. Their reported numerical
  finding is that inventory risk *diminishes* in importance as prices approach zero or
  one — their result on their model, not a claim about any venue. **The corpus's
  market-scoring-rule and cost-function families are likewise written natively for
  bounded payoffs**, and two of them state the [0,1]-with-absorbing-endpoints structure
  explicitly ([Moallemi, Robinson & Zhu 2026](https://arxiv.org/abs/2607.17428)
  **[FT]**; [Chakraborty, Das & Peabody 2015](https://doi.org/10.1609/aaai.v29i1.9313)
  **[FT]**, on an asset traded *"at prices in the interval [0,1]"*). **So the honest
  cross-branch statement is now: the transfer question is not moot, but it is no longer
  the only question, and a successor that spends its budget re-deriving Avellaneda &
  Stoikov under a bounded process while a natively-bounded formulation exists is
  choosing the harder path for no stated reason.**
- **What does this branch owe the other threads?** The coherence-residual statistic
  in branch 1 and the calibration-deviation statistic in branch 3 are both
  time-indexed and both would inherit `rules/quant-project.md` directives 1-7 at
  their first empirical stage (ADR-0004). Any successor specification that could not
  satisfy no-look-ahead and time-ordered splits is defective **at the point of
  writing**, even though nothing here will run it. **Added at rev 3:** Branch 10's
  settlement-lag statistic is time-indexed in the same sense and inherits the same
  directives, which is why its standard-error route is named (MV-TC-15) rather than
  left to an executing project to choose.
- **Which branches are runnable TODAY, with no data and no venue access? (new at rev
  3)** **Branch 7** and **Branch 11**, in full; **Branch 9** for the one venue pair
  whose clauses were retrieved; **Branch 6**'s cheap pass over the 178 unextracted
  records and, under MV-TC-13, over the multivocal corpus's 1,465 undecided rows;
  **Branch 2**'s derivation half. Everything else waits on a document or on an
  executing project. **This ordering is a consequence of the gaps, not a priority
  judgement**, and it is stated because rev 2 left a reader with no way to tell which
  branches were blocked on the world and which merely on effort.

## Verification status

**Every substantive citation in this document is drawn from the compiled corpus
record named in the frontmatter and carries the identifier that record carries.**
Nothing here was written from model recall. **Identifier form, added 2026-09-04
(finding REV-1-3):** multivocal-corpus identifiers are carried with the agenda-local
`MV-` prefix and predecessor identifiers bare, per the convention stated under "How
to read this document"; **the underlying identifier in each corpus record is
unchanged**, and no record was renumbered by this agenda.

**Four methodology citations are NOT corpus records and are marked as such.** They
are the inference conventions adopted for this branch by
[ADR-0004](../decisions/ADR-0004-quant-rule-adoption-prediction-markets.md) from
`rules/quant-project.md`, and they bind the branch's first empirical stage wherever
it occurs. Each was verified against Crossref on 2026-09-02 (author, year,
container) and each resolves at the DOI Handle System with `responseCode` 1:
Newey & West 1994, *Automatic Lag Selection in Covariance Matrix Estimation*,
*Review of Economic Studies* (`10.2307/2297912`); Andrews 1991, *Heteroskedasticity
and Autocorrelation Consistent Covariance Matrix Estimation*, *Econometrica*
(`10.2307/2938229`); White 2000, *A Reality Check for Data Snooping*, *Econometrica*
(`10.1111/1468-0262.00152`); Hansen 2005, *A Test for Superior Predictive Ability*,
*JBES* (`10.1198/073500105000000063`). They are cited for their **procedure**, not
for a result, and no operating characteristic is quoted from any of them.

**What that inherits, stated because it bounds every branch above. Restated at rev
2.** The corpus is a compiled corpus record, not a systematic review: **96.1%** of its
dispositions are keyword-classifier outputs (was 98.3%); **full text was read for 33
of its 327 included records and for none of the other 294**; 33 of the original 149
included records are metadata-depth only; **178 of the 327 carry no extraction at all
and are not in the bibliography store** (corpus gap AG-11); and **1,055** records ended
screening unresolved (was 1,245). The corpus's own gate returns `block` on 83 G16 identifier findings, 81
dispositioned as the standing publisher-403 class and two dispositioned
individually; the DOI Handle System resolves 149 of 149. **A branch that needs a
claim to be true, rather than to be *stated by a retrieved record*, must retrieve
the full text itself.**

**Round-2 corrections inherited from the corpus record**, all dated 2026-09-02, all
material to what this agenda may assert:

- **No demonstrated vocabulary gap** is claimed for any known-item miss. The corpus
  briefly asserted that `dealer` and `limit order` appear in none of its topical
  queries and that KI-20 and KI-21 were therefore demonstrated vocabulary gaps.
  `limit order` **is** carried, by `ka-crossref-07`. The cause of the four genuine
  misses is undetermined between vocabulary and the retrieval cap. **Consequence for
  this agenda:** a successor must not "fix" the search by adding vocabulary
  `ka-crossref-07` already carries; the live constraint for KI-21 is the `rows=20`
  cap against a platform-reported 79,887.
- **The arXiv `cat:q-fin*` narrowing is offset in weakened form, not unoffset.**
  Three of the four offsetting queries executed and returned records; one returned
  zero (G-8).
- **15, not 13, of the 19 Kalshi-specific records are SSRN DOIs** (G-9), so H-5 is
  worse than the corpus first reported.
- **Six transfers, not five, are `not-transferable-as-stated`** for want of the
  venue's mechanism (G-3), which is why Branch 0 is a precondition for four of the
  research branches rather than three — five at rev 2, counting Branch 2b's mechanism
  half.

**Rev-2 corrections inherited from the corpus record**, all dated 2026-09-03, all
material to what this agenda may assert:

- **The corpus grew from 149 records to 327** (amendment A16) and **33 of them were
  read at full text** (amendment A17). The frozen prefix of the protocol is unchanged
  and was re-verified against the bytes on disk after both appends.
- **Branch 2's rev-1 premise was contradicted by the full texts** and is corrected at
  its site with a supersession marker. Glosten & Milgrom and Kyle have **no inventory
  objective**. **Glosten & Milgrom say so in their own text** -- the footnote on
  binding inventory constraints and the zero-profit condition. **Kyle does not discuss
  inventory at all**: his model carries no inventory state variable and no reservation
  price, and that is **this corpus's reading of his specification, not a statement of
  his**, reached from pp. 1315-1317, the only pages read. **[corpus-inference]**
  Branch 2b now carries their transfer question. *(Corrected 2026-09-03, finding
  LITERATURE-1-1: this bullet previously said "both say so in their own texts", which
  is false of Kyle.)*
- **Three transfer determinations in the corpus's section 8.4 changed, and one was
  confirmed, on the strength of sentences the authors wrote.** Kyle and Avellaneda &
  Stoikov moved from `not addressed` to `explicitly excluded`; Glosten & Milgrom moved
  from `not addressed` to `addressed`; Guéant et al.'s `explicitly excluded` was
  **confirmed** at full text and extended -- a confirmation is not a move. **All three
  changes ran against the corpus's prior reading**, which is the direction that matters
  for a document now asserting less than it did. *(Corrected 2026-09-03, finding
  REV-1-3: this bullet said "Four transfer determinations ... changed" and then
  contradicted itself two lines later with "Three of the four moved". The same false
  count sat in protocol amendment A17 section (e), which is append-only and is
  corrected by amendment A18, and in the corpus record's section 8.4 caveat block,
  corrected in place.)*
- **Ho & Stoll 1981 remains unread**, with an enumerated six-route failure record. Any
  statement in this agenda about what that model assumes is a statement about what
  *other* authors say it assumes, and is marked as such in Branch 2.
- **The three Kalshi-specific S4 records are still at abstract depth** because SSRN
  returns HTTP 403 to unauthenticated sessions (corpus gap AG-12). **The
  `quote-driven` characterisation that H-4 quarantines could not be checked against its
  record's own text**, so H-4 stands exactly as written.
- **A retrieval failure is not evidence of absence**, and this agenda binds itself to
  that rule: 88 of the 503 residual X11 records survived a four-arm chain with nothing
  filled, 78 of them on HTTP 429 and 19 on HTTP 403. No branch may score those as
  records that state nothing.

**Rev-3 corrections and inheritances from the SECOND corpus**, all dated 2026-09-04,
all material to what this agenda may assert:

- **The identifier spaces of the two corpora COLLIDE, and the collision is now
  declared rather than latent** *(finding **REV-1-3**, 2026-09-04)*. The predecessor
  supplies G-1..G-10 and TC-1..TC-5; the multivocal corpus supplies ~~G-1..G-25~~
  **G-1..G-28** *(range corrected in the next bullet; the struck value is this
  bullet's wording as first written)* and
  TC-1..TC-15. Rev 3 as first written cited both bare, so a bare `G-9` or `TC-3`
  resolved to two different objects. Every multivocal reference in this document now
  carries the **`MV-`** prefix, the convention is stated once under "How to read this
  document", **neither corpus record is edited**, and **no branch derivation is
  orphaned** — each of branches 7-11 still names the gap or handoff it comes from.
- **The multivocal corpus's gap range MOVED, and every range declaration in this
  document was stale until this correction** *(dated 2026-09-04, findings
  **CRITICAL-2-3** / **SCOPE-2-7**)*. Rev 3 as first written declared that corpus's
  range as ~~G-1..G-25~~ in four places — the revision note, the `corpus_multivocal`
  front-matter field, "How to read this document", and the collision bullet
  immediately above. **Round-1 remediation of that corpus record added THREE gaps**, so
  the sole admissible source range for branches 7-11 is **G-1..G-28**, cited here as
  **MV-G-1..MV-G-28**. The struck range is retained legible everywhere because it was
  true when it was written. The three additions:
  - **MV-G-26 — RePEc was never searched.** All nine attempts were served the search
    form rather than a result set, so no RePEc row is a search result and none may be
    scored as "states nothing". **Now cited at this agenda's own RePEc statement**, in
    Branch 6's rev-3 extension, alongside MV-G-9 and MV-G-22.
  - **MV-G-27 — the S-D and S-E retrieved bytes are not archived**, so their digests
    are attestations. **Carried as standing hazard H-10 and in the next bullet**,
    because it changes this agenda's evidence posture rather than its bookkeeping.
  - **MV-G-28 — the CSL-JSON store builder was never archived. REGISTERED, AND UNDER
    REVISION BY THE LEAD AT TIME OF WRITING**, so it may be downgraded or closed. It is
    recorded here for range completeness only: **no branch is derived from it and
    nothing in this agenda treats it as settled.**
  **Neither corpus record is edited and neither is renumbered** by this correction; the
  `MV-` prefix remains agenda-local. **No branch derivation is orphaned and no branch is
  added** — MV-G-26 and MV-G-27 bound claims branches 6-11 already make.
- **Digests this agenda relies on are ATTESTED, not verifiable** (**MV-G-27**, hazard
  **H-10**). The S-D and S-E payload bytes behind every `KSL-` clause cited above were
  **deliberately not copied into this public repository**, being third-party pages, so
  their `sha256` values cannot be recomputed by a reader. All **32** lateral payload
  digests were verified **once** by the corpus lead against an **ephemeral scratchpad**
  and all 32 matched — **VERIFIED-ONCE, not verifiable**, and the scratchpad no longer
  exists. Every `KSL-` citation in Branch 7's census, in Branch 9 (`KSL-C14`,
  `KSL-C15`, `KSL-C16`), in Branch 10 (`KSL-C09`, `KSL-C30`, `KSL-C32`) and in the H001
  cross-reference table is to be read as **attested at the stated retrieval date**.
  Under MV-G-24 and MV-G-25 a re-retrieval may legitimately return different bytes, so
  a mismatch is **not** evidence that the attestation was wrong — and the attestation
  cannot be promoted to a verification by any later check either. **This is the one
  rev-3 inheritance that changes the standing of evidence this agenda has ALREADY
  cited, rather than adding a new limitation to evidence it has not.**
- **Rev 2's Branch 0 status paragraph is false on its facts as of 2026-09-04** and is
  superseded in place by the rev-3 status block, with the rev-2 text left standing.
  The fee schedule, tick, settlement value, collateralisation, netting, position-limit
  regime, block route and throughput document **were** retrieved by the multivocal
  branch's venue arm.
- **H-4 is partly superseded**: a venue filing states that below the block threshold
  **every order must interact with the central limit order book** (`d20-c3`), and that
  customers trade peer-to-peer with the venue never taking the other side (`d04-c4`).
  A pure quote-driven reading is excluded for sub-block flow; a hybrid is not; and
  **Branch 2b gets harder**, because two of Glosten & Milgrom's three binding
  mechanism conditions are contradicted rather than merely unestablished.
- **The distinction between NOT RETRIEVED and WITHHELD AT SOURCE is new to this
  agenda at rev 3** and changes what "more searching" can buy: the market-maker
  selection procedure (**MV-G-2**), the elevated-position-limit schedule (**MV-G-3**)
  and the settlement Source Agency appendix (**MV-G-4**) are filed confidentially and
  cannot be obtained by any search. Hazard H-7; Branch 7 tests whether it matters.
- **The second corpus's gate returns `block` on FAIR F1 by design** (**MV-G-15**): no
  included record carries a DOI, PMID, PMCID or arXiv id, because ADR-0006 dropped the
  persistent-identifier requirement to admit venue filings, code artifacts and
  practitioner pages at all. Recorded in the front matter so that no successor reports
  the gate as passing, and paired with **MV-G-24** (content drift), **MV-G-25** (no
  archived snapshots) and **MV-G-27** (unarchived S-D/S-E bytes) as the standing
  findability and verifiability cost.
- **The second corpus contains NO peer-reviewed and NO preprint record**
  (**MV-G-5**), and 1,465 of its rows are **undecided**, not ineligible (**MV-G-5**,
  **MV-G-6**, and **MV-TC-13** for the procedure that would decide them). Branches
  7-11 stand on tier 2 and tier 5 and say so at their heads.
- **Four nulls this session encountered are registered in
  [failure_log.md](../../failure_log.md) as F006-F009** under the charter's
  negative-result protocol, and **none of them is restated as a branch here**: the
  post-print latency race foreclosed on one series by a stated trading close (F006);
  the weather/temperature stratum's emptiness, which is `undetermined` because the
  on-point query **never executed** across eleven attempts and the RePEc rows are
  interface failures rather than searches (F007); and two nulls **reported by
  sources** — a repository whose best candidate is statistically indistinguishable
  from an always-NO baseline (F008) and one deriving a taker round-trip break-even in
  cents at a stated price band (F009). **Every one of those rows records that protocol
  steps 1-2 were NOT executed**, in those words.
- ~~**One discrepancy between the second corpus record and its own arm log is recorded
  and NOT repaired here**, because this agenda does not edit either document: the
  corpus record's §10 N-5 states that four academic queries in the weather stratum
  *executed* and returned zero, while `ks-repec-04.json`'s own
  `platform_interface_failure` field states that its query **never executed** and that
  `n_returned: 0` there means **no search was run**. The arm log is preferred, the
  executed-and-zero count in that stratum is **two**, and the full statement is in
  failure_log F007.~~
- **CORRECTED 2026-09-04, findings CRITICAL-2-2 / SCOPE-2-6 — THAT DISCREPANCY IS
  CLOSED, and the struck bullet above was wrong about another document's state rather
  than about its own conclusion.** The struck text is rev 3's wording as first written
  and is retained legible. **What was wrong with it:** it asserted, in the present
  tense and explicitly as a LIVE, un-repaired discrepancy that this agenda declines to
  fix, that the multivocal corpus record's §10 note **N-5** *still* states that four
  academic queries in the weather stratum executed and returned zero. **That is no
  longer true.** In the same round-1 remediation round, that corpus record was
  **corrected at six loci** — head limitation 9, note **N-5**, note **N-8**, four rows
  of the section-2 source table, and nine `ks-repec` annotations in the section-3
  fence — gap **MV-G-9** was **extended**, new gap **MV-G-26** (*RePEc was never
  searched*) and new data-integrity entry **DI-8** were **added**, and
  [failure_log.md](../../failure_log.md) **F007** received a **dated addendum**
  recording all of it. **The executed-and-zero count of TWO now appears in BOTH
  documents**, so the corpus record and its own arm log agree and there is nothing left
  to prefer between them. **This agenda's CONCLUSION was always right and is
  unchanged:** the executed-and-zero count in the weather stratum is **two**, and a
  RePEc row is an interface failure rather than a search. What was wrong was only this
  agenda's description of another document's *current* state — which is the failure
  mode a document citing across records is most exposed to, and the reason this
  correction is dated and appended rather than silently applied. **This agenda still
  edits neither the corpus record nor the arm logs** (**DI-8**, **MV-G-26**); it
  records that the repair happened elsewhere, and by whom.
