# S4 completion-screen subset rule (SR-1 / SR-2), fixed before assessment

- **Fixed at:** 2026-09-03T17:51:21Z (UTC, `date -u` at the moment of writing)
- **Git HEAD at fixing:** `2ba291f9922547e1848d7d505cedafb2979e2433`
- **Stage:** completion of the stage-2 assessment that amendment A5 left unperformed
  for the 700 records dispositioned **X11** in
  `docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl`.
- **Status of this file:** written and hashed **before any X11 record was read for
  assessment**. It is cited by its SHA-256 in the protocol amendment that declares
  the stage and in the `_header` of `ka-s4-completion-screen.jsonl`.

## What this rule is for

The re-execution brief scopes the completion screen to *"every X11 record whose
transfer clause bears on strand S4"*. The subset that phrase denotes has to be
fixed from the frozen protocol before any record is read, otherwise membership is
decided by what turns up and the screen is unfalsifiable. This file fixes it.

## The frozen text the rule is derived from

Three frozen passages, quoted verbatim, are the whole derivation. **None is
altered, reinterpreted or extended here; the rule only composes them.**

1. **Section 1.3 Strands, closed at freeze** — the S4 row:

   > | S4 | Market making, inventory risk, market scoring rules, automated market makers |

2. **Section 2.2 In-scope contribution rule**, the C3 clause and the sentence that
   binds C3 to S4:

   > - **C3 (model).** Specifies a market-making, inventory-risk,
   >   market-scoring-rule, or automated-market-maker model with a stated objective
   >   and stated applicability conditions, whether or not it is applied to in-scope
   >   instruments — see the transfer clause below (S4).

   and, for the boundary, the C4 clause and the sentence that binds C4 to S6:

   > - **C4 (microstructure).** Analyses the microstructure of in-scope or
   >   limited-payoff instruments: spread formation, adverse selection, liquidity
   >   provision, order-flow informativeness (S6).

3. **Section 2.2 Transfer clause**, whose heading names the contribution type it
   governs:

   > **Transfer clause for C3, stated in advance.** The market-making literature is
   > largely written for unbounded-payoff instruments. A C3 record whose instrument
   > is not in-scope under 2.1 is **eligible only if** the corpus can state what the
   > record's own text says about its payoff support and applicability conditions —
   > i.e. the record is admitted as a *model whose transfer must be argued*, and
   > extraction field E10 records the transfer status. It is never admitted as
   > evidence *about* binary contracts. A C3 record that states no applicability
   > condition and no payoff-support assumption is excluded under X6.

**The composition.** The transfer clause is stated *for C3* and for no other
contribution type. Section 2.2 maps C3 to S4 and C4 to S6 explicitly, in the
criterion text itself. Therefore "the X11 records whose transfer clause bears on
strand S4" is, in the protocol's own mapping, exactly "the X11 records that make a
C3 contribution". The rule below says only that.

## SR-1 — the subset rule (inclusion in the subset)

> **SR-1.** A record dispositioned X11 is IN the S4 completion subset if and only
> if, on **reading the record's own retrievable text**, the record **specifies a
> model — an objective and a rule for a liquidity supplier's prices, quotes,
> inventory or state — of at least one of the four objects frozen section 1.3
> assigns to strand S4: market making, inventory risk, a market scoring rule, or an
> automated market maker.** This is the object half of the section 2.2 C3 clause.
> Whether the record's instrument is in scope under section 2.1 is irrelevant to
> subset membership, because C3 applies "whether or not it is applied to in-scope
> instruments".

### SR-1 note, stated in advance to prevent a circularity

The section 2.2 C3 clause has two conjuncts: a **model of an S4 object with a
stated objective**, and **stated applicability conditions**. SR-1 uses only the
first.

The second conjunct is deliberately **reserved as the eligibility test applied
inside the subset**, because it is exactly what the transfer clause and X6 turn
on: *"A C3 record that states no applicability condition and no payoff-support
assumption is excluded under X6."* If SR-1 required both conjuncts, a record
lacking applicability conditions would fall out of the subset instead of being
excluded under X6, no record could ever receive an X6 verdict at this stage, and
the transfer clause would have no work to do. That would make the completion
screen incapable of returning the one verdict the frozen protocol wrote for this
literature. The split is fixed here, before assessment, for that reason.

## SR-2 — the boundary (exclusion from the subset), fixed in advance

A record is OUT of the S4 completion subset — and therefore **keeps its X11
disposition, eligibility UNDECIDED, unchanged** — if any of the following holds.
These clauses are stated now so that the boundary is not drawn around whatever the
reading turns up.

- **SR-2a — C4, not C3.** The record reports or analyses microstructure (spread
  formation, adverse selection, liquidity provision, price impact, order-flow
  informativeness, market-maker behaviour observed in data) **without specifying a
  model of an S4 object in the SR-1 sense**. Section 2.2 assigns C4 to S6, and the
  transfer clause does not reach C4. Empirical papers *about* market makers are the
  central case.
- **SR-2b — incidental vocabulary.** The market-making / inventory / scoring-rule /
  AMM vocabulary appears only in the record's background, motivation, related work,
  data description, or venue name, and no such object is a subject the record
  itself models.
- **SR-2c — model of some other object.** The record specifies a model, but of an
  object outside the four section 1.3 S4 names: optimal execution or liquidation
  for a price-taking trader, portfolio choice, order routing or smart-order
  placement, auction or mechanism design with no liquidity-supplier objective,
  statistical price-formation models with no quoting agent, inventory models of
  physical goods (production, supply chain, warehousing) rather than of a dealer's
  position.
- **SR-2d — not readable.** The record cannot be retrieved to title-and-abstract
  depth by this stage's retrieval chain, so SR-1 cannot be applied to it by
  reading. Such records keep X11 and are **reported by name with the failure
  mode**. They are NOT coded X8: X8 asserts a criterion failure (fails I4) reached
  after a full stage-2 retrieval chain, and this stage's chain is a
  subset-membership chain, which is weaker.

## What the rule deliberately does NOT do

- **It contains no numeric element of any kind** — no count, cap, floor, score,
  similarity threshold, citation cutoff or sample size. There is therefore nothing
  in it to derive or to label CONVENTION. Its extension is whatever reading
  returns; the subset size is the rule's consequence, never its target.
- **It does not use the keyword classifier.** The classifier's R6 branch (MODEL
  token present, no EVENT token, no DeFi token) is what *created* the X11 stratum
  and is the defect this stage exists not to repeat. SR-1 membership is decided by
  reading the record, and no token list appears in SR-1 or SR-2.
- **It does not use retrieval provenance.** Membership is not decided by which arm
  or query returned the record — not by the section 3.3 A4 (Hanson, S4) versus A6
  (Glosten-Milgrom, S6) anchor split, and not by any strand labelling of the
  section 3.2 topical queries. Those labels are search-design annotations about what
  an instrument was selected to recall, not claims about a record's content;
  section 3.4 says so in terms for the known-item table's "anticipated role" column,
  and the same caution applies to the anchors. Provenance would have been mechanical
  and reading-free, and it was rejected for that reason: it is a proxy, and a proxy
  is what produced the X11 stratum.
- **It does not alter, add, remove or reinterpret any eligibility criterion.**
  I1-I6, X1-X9, B-a-B-d, C1-C4 and J1-J6 are applied exactly as frozen. X10 and X11
  are applied as amendments A4 and A5 define them.

## What happens to records IN the subset

Each is assessed at stage 2 against the FROZEN section 2 criteria by reading, and
receives a terminal verdict citing the criterion that decided it — `include` under
I1/I2 with the transfer clause carrying I1, or an exclusion code from section 2.4.
Where reading to the depth this stage reached does **not** settle the criterion,
the record is recorded as **still undecided, inside the subset, with the reason and
the depth reached** — a subset member is not forced to a verdict the evidence does
not support.

## What happens to records OUT of the subset

They keep X11 verbatim. The reading performed on them was a **subset-membership
determination under SR-1/SR-2 only** — it was not a section 2 eligibility
assessment. Specifically, for out-of-subset records this stage did not evaluate I3
or I4, did not run the section 2.4 first-code-that-applies ordering, and did not
attempt full text. Their eligibility remains UNDECIDED in exactly the sense
amendment A5 fixed, and this stage narrows it no further. The per-record membership
determinations are published for all 700 in
`docs/literature/search_logs/kalshi-arbitrage/ka-s4-subset-membership.json` so the
residual is auditable rather than merely counted.

## Prior exposure, disclosed

While verifying that the record universe rebuilds byte-identically from the archived
scripts (8,813 works, 7,111 duplicates removed) and that the uid join to the verdict
file is sound, the metadata of **one** X11 record — `U00024`, "Price Discovery under
Disposition Sales" — was printed to screen before this rule was fixed. It is
disclosed here rather than left to be found. The rule above was not shaped by it:
SR-1's content is the section 2.2 C3 object clause and nothing else, and `U00024` is
assessed under the rule like every other record.


---

# Post-stage disclosure, appended 2026-09-03 at audit remediation — NOT part of the rule as applied

**Everything above this marker is the rule exactly as the completion screen
applied it, byte for byte.** The first **10189 bytes** of this file — the whole of the
document above this line — hash to
`5f64d29b6868670c4cafc15c89618405c6a64675e4dc62b3557235140ef2c6c6`, which is the
value cited by `ka-s4-completion-screen.jsonl`'s `_header`, by
`ka-s4-subset-membership.json`, by `ka-s4-fulltext-extraction.jsonl`'s
`_header.prior_stage_files`, by amendment A16's *Artifacts* block and by the
2026-09-03 ReproLog's `config_resolved_sha256`. Those citations remain
verifiable as a **prefix digest**. Nothing above is edited, and this section
changes no clause of SR-1 or SR-2.

## The priority claim above is SELF-ATTESTED and carries no external timestamp

*(Audit finding REV-1-2, 2026-09-03, major, raised by the critical-reviewer
branch and not refuted.)*

The header of this file states a fixing time (`2026-09-03T17:51:21Z`, a `date -u`
string) and a "Git HEAD at fixing", and asserts under **Status of this file**
that the rule was "written and hashed **before any X11 record was read for
assessment**". **Every one of those assertions was written by the same agent, in
the same session, into the very artifact whose priority is in question.** They
are self-attestation. Stated precisely:

- A `date -u` string in a file is a claim about when the file was written, made
  by the writer, checkable by nobody.
- The SHA-256 chain outward — into `ka-s4-completion-screen.jsonl`'s `_header`,
  into the membership file, into A16, into the extraction file — establishes only
  that **those files were written after some version of this one**. It does not
  establish that this file preceded the *reading*. A digest orders writes; it
  does not order a write against an unrecorded act.
- **No commit carries this file at any point before the assessment.** The file
  was still untracked when the audit ran. There is therefore no external
  timestamp of any kind on the priority claim.
- The `Prior exposure, disclosed` section below the rule shows the author knew
  the priority question was live, and disclosed one record's metadata having been
  seen. That disclosure is a point in the rule's favour; it is not evidence of
  priority.

**What would have established it, and what the project already owns.** The
correct mechanism exists in this repository and was used for this review's parent
artifact: commit **`27d74738aa35ec1cdf1ec6915b50532e3620ea6f`** — subject
*"docs(protocol): register frozen kalshi-arbitrage search protocol (sha256
99524df02696)"* — committed the frozen protocol **before any query executed**, and
the corpus record's `registration:` frontmatter field cites that commit, in terms,
as the registration event. Applying the same discipline here would have meant:
commit this file (or a commit trailer carrying its SHA-256) **before the assessing
agent was dispatched**, and then cite *that commit* as the priority evidence
instead of a `date -u` string. That was not done. It is a process failure of the
dispatch.

**What this does and does not impeach.** It does **not** impeach the rule's
content. SR-1 is the section 2.2 C3 object clause and SR-2 is its boundary; both
are compositions of quoted frozen text, and the derivation is auditable on its
face by anyone holding the frozen protocol. What is unestablished is the
*ordering* — that the rule was fixed before the reading rather than shaped by it.
A reader who does not take the author's word for it has no independent ground for
the ordering, and this file no longer implies otherwise.

**Binding on any successor stage of this kind.** The rule file, or a commit
trailer carrying its digest, is committed **before** the assessing agent is
dispatched, and the commit hash — not a timestamp string written by the assessor
— is cited as the priority evidence.

*Recorded in the protocol's append-only addendum at amendment **A18**, which is
where a consumer of the protocol will find it.*
