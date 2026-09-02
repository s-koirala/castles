# Protocol amendments — kalshi-arbitrage registered search

Append-only. Governed by section 10 of
`docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md`
(frozen SHA-256 `99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`,
registration commit `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`).

Each entry states: number and ISO 8601 date; what changed, quoted against the
frozen text; why; the execution stage at which it was decided, including whether
the affected records had already been seen or screened; and the PRISMA-P item(s)
touched.

**Status of this file, corrected 2026-09-02 under audit finding REV-1-13.** As
first written this header said "The frozen protocol file is NOT edited", and
treated that as compliance with section 10. It is not. Section 10 requires each
amendment to be recorded "in the addendum below" of the protocol itself, under a
heading that reads "APPEND-ONLY ADDENDUM BELOW THIS SECTION" — an **append**, not
an edit. Keeping every amendment outside the protocol meant a reader verifying the
registered SHA-256 obtained a protocol asserting an amendment mechanism with no
entries in it. **Amendment A12 corrects this: A1-A12 are now appended to the
protocol's own addendum.** Nothing above the addendum marker is altered, so the
frozen prefix — the first 82,677 bytes, the file exactly as registered — still
hashes to `99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`
(verify with `head -c 82677 <file> | sha256sum`). This file remains the working
log and is byte-identical in amendment content to the protocol addendum.
The **protocol-with-addendum** whole-file digest is recorded in the corpus
record's section 13.1 and carried by the follow-on provenance commit; it is
deliberately **not** written inside the protocol file, because a digest of a file
cannot be stored in that file.

Twelve amendments: **A1-A5** decided during execution; **A6-A12** added by
round-1 audit remediation on 2026-09-02, each naming the audit finding that
required it.

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
