# ADR-0006 — a multivocal source taxonomy for the strategy corpus, in a new branch rather than an amendment

- **Status:** Accepted
- **Date:** 2026-09-04
- **Deciders:** Sajan Koirala
- **Supersedes:** none. Bounded by
  [ADR-0003](ADR-0003-specification-not-execution.md); governed as to review
  standard by [ADR-0004](ADR-0004-quant-rule-adoption-prediction-markets.md),
  whose branch delimitation already covers the artifacts opened here.

## Context

The prediction-market branch's first corpus was compiled under
[docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md](../methodology/protocol_kalshi-arbitrage-review_2026-09-02.md),
frozen on 2026-09-02. **That protocol admits published literature into its corpus
flow and nothing else; its one documentation channel, the S7 stream of section
2.7, is fenced off from that flow and is described below.** Its inclusion
criterion I3 reads, verbatim from the frozen text (section 2.3):

> **I3.** A persistent identifier exists: DOI, arXiv id, RePEc handle, or
> Handle-System handle. A record failing I3 is excluded and logged with its best
> available locator (a FAIR F1 gap,
> [Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)), never
> silently dropped.

and its matching exclusion code reads, verbatim (section 2.4):

> **X7 — no persistent identifier.** Fails I3.

The consequence is structural, not incidental. A public software repository
implementing an event-contract trading bot, the KalshiEX rulebook and its
amendments, a CFTC order or self-certification filing, a fee schedule, an API
rate-limit page, and a practitioner write-up all lack a DOI, an arXiv id, a
RePEc handle, and a Handle-System handle. Every one of them is excluded by X7
before its content is ever read. The 2026-09-02 branch is therefore, by design,
unable to see the source classes in which most *stated* strategy content for
this instrument actually lives.

The frozen protocol did admit one narrow documentation channel — the S7
documentation-tier stream of its section 2.7 — but that stream is fenced by four
frozen constraints, the first of which is that S7 records "establish
venue-structural facts only … They may never establish a behavioural, empirical,
or efficiency claim," and the second of which is that they "are never counted in
the corpus flow." S7 cannot carry a strategy statement, and cannot carry a
repository or a practitioner source at all.

The 2026-09-04 session objective, declared in
[docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md](../deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md),
is to compile the comprehensive retrievable record of *stated* strategies for
binary event contracts with KalshiEX LLC as the venue of interest. That
objective is not reachable inside the frozen eligibility set.

## Decision

**A new branch is opened, with a widened source taxonomy, under a new protocol
frozen before its first query executes. The 2026-09-02 branch is left
byte-untouched.**

Concretely:

- The new protocol is
  [docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md](../methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md).
  It defines five source classes — S-A peer-reviewed, S-B preprint or working
  paper, S-C public software repository or package, S-D exchange or regulator
  document, S-E practitioner grey literature — with a record falling in exactly
  one, and inclusion criteria coded **N1-N6** (the letter N is used because the
  predecessor protocol already uses J1-J6 for its judgement-call decision rules,
  section 2.6).
- **The headline point of departure is that a persistent identifier is not
  required.** Four consequential departures travel with it and are named here
  rather than left implicit: I4's abstract-depth retrievability test becomes
  **N3**, a retrievability criterion (retrievable without authentication or
  payment, and digestible); I5's closed document-type list is replaced by **N5**,
  an any-source-class criterion; a new dating criterion **N4** is added, with its
  paired exclusion code Y5; and the predecessor's I6 plus §2.7 constraint 2,
  which keep documentation-tier records out of the corpus flow, are **NOT**
  carried — S-D records are counted in the new flow. Every other discipline of
  the precedent — frozen eligibility before search, verbatim query logging,
  criterion-coded verdicts, published exclusion tables, closing arithmetic
  identities, an enumeration of the reporting items not met, and append-only
  amendment — is carried over unchanged.
- **The new branch's prose artifacts name the branch in their front matter, so
  ADR-0004's clause ("any successor artifact that names this branch in its front
  matter") reaches the protocol and the corpus record directly. The CSL-JSON
  store and the search-log directory carry no front matter; they are governed
  derivatively as materials of those artifacts, and this ADR records that reading
  so a later reviewer does not have to reconstruct it. No new rule adoption is
  made here.** This ADR itself carries no front matter, in the house ADR format;
  it is reached by name from the artifacts that cite it.
- Nothing in the 2026-09-02 branch is edited, re-screened, re-counted, or
  re-dispositioned. Its counts, its verdicts, its addendum A0-A19, and its
  CSL-JSON store stand exactly as published.

## Alternatives considered

**(a) Amend the frozen 2026-09-02 protocol to relax I3/X7.** Rejected, and the
amendment record is the reason rather than an obstacle to it. That protocol's
section 10 permits only numbered, dated, append-only amendments, and states that
"**Frozen text above this line is never edited**: a superseded provision is
superseded BY an addendum entry, in place, and the original wording stays
legible." The nineteen amendments actually taken, A1 through A19, mostly changed
queries, dispositions, capacity accounting and extraction depth, and corrected
earlier amendments — A4 and A5 added the capacity codes X10 and X11, A16-A19
completed and corrected stage-2 work. Two are exceptions that prove the
difficulty rather than contradict it: **A8 relaxed frozen criterion I4** for 33
metadata-depth records, retrospectively and with the alternative reading
published (protocol lines 1533-1571), and **A18 §(c)** records that the bar A16
applied for admission was the negation of X6 rather than the transfer clause's
conjunction. Both were taken after the affected records were dispositioned, which
is precisely the weak-amendment position this ADR refuses to repeat at branch
scale. A4 is explicit about the intent, in a clause spanning lines 1378-1379:
"No eligibility criterion is altered, added, removed, or reinterpreted."

Relaxing I3 would be an eligibility change an order of magnitude larger than A8's
— it would change which records were ever *admissible*, not the depth at which 33
already-admitted records were read, and it would retroactively reopen every one
of the 8,813 dispositions made under the frozen bar. A8 shows that an eligibility
relaxation inside a frozen protocol is possible only at the cost of publishing an
alternative reading of the whole corpus ("A reader who declines this relaxation
should read the corpus as 116 included records plus 33 X8 exclusions"). At branch
scale that cost is unpayable: no single sentence can tell a reader how to read a
corpus whose entire admission bar moved. A widened eligibility criterion is a
different review, not an amendment to this one.

**(b) Admit the grey sources into the existing corpus record without touching
the protocol.** Rejected. It fails the branch's own registration discipline,
stated in the 2026-09-02 protocol's front matter: "The registration event for
this protocol is its provenance commit: the file is committed BEFORE any query
executes … Any post-freeze change is an amendment under section 10, never an
edit to frozen text." A corpus record containing records its own registered
protocol excludes is unauditable — a reader re-deciding any row against the
frozen text would reach `exclude, X7` for every added row. It is also the exact
failure the protocol's section 10 names: "Silent deviation is a conduct
violation."

**(c) Route the new sources through the existing protocol's S7
documentation-tier stream.** Rejected. Section 2.7 constraint 1 confines S7 to
venue-structural facts and forbids it from establishing "a behavioural,
empirical, or efficiency claim" — which is precisely what a stated strategy is.
Constraint 2 keeps S7 out of the corpus flow entirely, so no strategy admitted
that way would ever appear in the identified/screened/included accounting.
S-C repositories and S-E practitioner sources are not venue documents at all and
have no place in S7 under any reading. Stretching S7 to hold them would be a
reinterpretation of frozen text, which is alternative (a) in disguise.

**(d) Compile from model recall and cite sources opportunistically.** Rejected
as a blocking defect rather than a design option.
[ADR-0004](ADR-0004-quant-rule-adoption-prediction-markets.md) §"Which directives
bind at the present stage" makes `REVIEW.md` blocking directive 8 binding on this
branch: "Every factor, signal, or trading rule must carry a citation to published
research or an in-repo derivation. Unattributed folklore factors are blocking."
Widening the *source taxonomy* does not relax that obligation; the one thing it
does widen — what counts as the citation's carrier — is stated below and is
stated as a widening.

## What the widening costs

Stated plainly, because the new corpus is weaker than the old one and must be
read that way.

- **No peer review.** S-C, S-D and S-E records pass no external referee. S-D
  documents carry regulatory force but are filer-published or agency-published
  statements of rule, not evaluated evidence — the 2026-09-02 protocol's section
  2.7 constraint 4 already requires "as filed" language for exactly this reason,
  and that requirement is carried into the new protocol.
- **No persistent identifier.** A URL is not a handle. There is no resolution
  guarantee, no registered metadata, and no custodian obliged to keep the object
  reachable. Records admitted here are a standing gap against the F1 findability
  principle of the FAIR guiding principles
  ([Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18), the record the
  predecessor protocol already resolved and cites at its own I3) — which is what
  I3 existed to prevent and what this ADR knowingly accepts.
- **Content drift.** A repository's default branch moves, a rulebook is amended,
  a fee schedule is superseded, a blog post is silently edited or deleted. The
  object cited today is not necessarily the object a reader retrieves later; the
  empirical scale of the hazard and the citation-standard basis for recording an
  access date are carried in the new protocol §3.3 and §5, not asserted here.
  The new protocol's mitigations — commit or release identifier for S-C,
  document date and effective date **where the document states one** for S-D,
  ISO-8601 access date and a digest of the retrieved bytes for every class —
  reduce ambiguity about *what was read*; they do not restore retrievability.
- **Therefore: warrant is per record, and is labelled per record.** The new
  corpus may not be read at a uniform evidential level. Every row carries its
  source class, its extraction depth, and its access date, and no claim in the
  corpus record may be stated at a strength its own row does not support.

## The bound this puts on claims

Neither of the two governing ADRs is relaxed by this one.

- **[ADR-0003](ADR-0003-specification-not-execution.md) still holds in full.**
  The new branch compiles what sources *state*. It acquires no market data,
  calls no exchange API, computes no price, fits nothing, backtests nothing, and
  states no tradeable rule. Every parameter an executing project would need is
  left `TO COMPUTE` with its selection procedure named.
- **[ADR-0004](ADR-0004-quant-rule-adoption-prediction-markets.md) directive 8
  binds, with one widened reading recorded here.** Directive 8 requires "a
  citation to published research or an in-repo derivation". For this branch a
  public repository's README or code, and a rulebook or regulator clause, are
  read as satisfying the citation carrier; model recall is not, and no strategy
  class may be entered on recall alone. That reading widens the attribution
  requirement's *carrier* and is the one place where this ADR does so; the
  *obligation* — every strategy attributed to a producible object, an
  unattributed strategy a blocking defect — is unchanged. A strategy with no
  locatable source is excluded under the new protocol's Y3 and reported as an
  absence, never entered in the taxonomy.
- Directives 1-7 remain non-binding at this literature-only stage and remain
  binding on the first empirical stage, wherever it occurs — which, under
  ADR-0003, is not here.

## Consequences

**Positive**

- The session objective becomes reachable without touching a frozen artifact.
  The source classes where stated strategy content actually lives are admissible
  for the first time in this repository.
- The eligibility departures are named, counted and auditable — one decisive
  departure plus four consequential ones, listed in §Decision and again in the
  new protocol §2.3 — rather than a diffuse loosening a reviewer has to
  reconstruct.
- The 2026-09-02 corpus keeps its stronger warrant. Because the branches are
  separate, the higher-evidence corpus is not diluted by the multivocal one, and
  a downstream consumer can cite either at its own level.
- The capacity-gap discipline the older branch learned the hard way — X10 and
  X11, added by amendments A4 and A5, recording *undecided* rather than a
  criterion failure — is available to the new protocol at freeze rather than
  discovered mid-execution. So is the A8 lesson: a criterion that cannot be met
  by a class of records the review needs should be written correctly at freeze,
  not relaxed afterwards.

**Negative**

- The branch now has two corpora on adjacent questions with different admission
  bars. A careless later reader can merge them and silently average away the
  difference in warrant. The mitigation is prose — per-record source class and
  a stated non-merge rule in each corpus record — and nothing mechanical
  enforces it.
- The two protocols now use overlapping code letters for different things (J1-J6
  are judgement-call rules in the predecessor and are deliberately not reused as
  inclusion criteria here). The rename to N1-N6 removes the collision but a
  reader of both files must still hold two code tables.
- Grey and repository records will need re-verification to be cited at any later
  date, because of drift. The maintenance burden is real and is not funded.
- The de-duplication surface grows: the same strategy can appear as a paper, a
  repository implementing it, a rulebook clause enabling it, and a blog post
  restating it. The new protocol handles these as distinct records with a
  mirror/fork exclusion, but the judgement is not free of error.
- The new corpus will contain records the 2026-09-02 corpus explicitly excluded
  under X7. That is intended and must be stated wherever the two are cited
  together, or it reads as an inconsistency.

**Neutral**

- No governance regime changes. ADR-0004's adoption already reaches the new prose
  artifacts through its front-matter clause, and their materials derivatively;
  ADR-0003's boundary is unchanged.
- The precedent protocol's structure is reused, so review effort transfers.

## Reversal cost

**Low, and confined to the new branch.** Reversal means deleting or superseding
artifacts that no other artifact yet depends on:

- [docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md](../methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md)
  and its registration commit;
- `docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md`;
- `docs/literature/references_kalshi-strategy-multivocal.json`;
- `docs/literature/search_logs/kalshi-strategy-multivocal/`, including the
  pre-freeze instrument-verification record
  `ks-instrument-verification.json`;
- the rev-3 additions to
  [docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md](../research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md),
  which would revert to rev 2 by a revision note recording the withdrawal, not
  by silent deletion;
- this ADR, which would be superseded by a later ADR rather than removed.

**What would NOT have to be undone: anything in the 2026-09-02 branch.** Its
protocol, its addendum A0-A19, its corpus record, its CSL-JSON store, its search
logs, and every one of its dispositions are untouched by this decision and stay
valid whether or not the new branch survives. That containment is the reason a
new branch was chosen over an amendment, and it is the property that makes this
decision cheap to reverse.

**Re-evaluation trigger:** if the multivocal corpus's S-C/S-D/S-E records prove
unretrievable at re-verification in a later session at a rate that makes the
corpus uncitable, or if a subsequent branch needs to merge the two corpora, this
ADR is revisited before either happens.

## References

- [docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md](../methodology/protocol_kalshi-arbitrage-review_2026-09-02.md)
  — §2.3 (I3), §2.4 (X7), §2.6 (J1-J6 judgement-call rules), §2.7 (S7
  constraints), §4.3 (count identities), §9.1 (what this is not), §10
  (amendments policy), front matter (registration), addendum A4 (lines
  1378-1379), A5, A8 (lines 1533-1571), A18 §(c).
- [ADR-0003](ADR-0003-specification-not-execution.md) — specification, not
  execution.
- [ADR-0004](ADR-0004-quant-rule-adoption-prediction-markets.md) — branch
  delimitation and the binding of `REVIEW.md` directive 8.
- [ADR-0001](ADR-0001-project-kind-and-scope.md) — the adoption-by-explicit-
  reference mechanism and the house ADR format.
- [docs/deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md](../deliverables/deliverable_spec_kalshi-strategy-corpus_2026-09-04.md)
  — the session declaration this ADR serves.
- [docs/methodology/charter_castles_2026-08-21.md](../methodology/charter_castles_2026-08-21.md)
  — admissible output types; commitment 3, no unlabelled constants; commitment 5,
  attribution fidelity and the prohibition on chain citation.
- `docs/literature/search_logs/kalshi-strategy-multivocal/ks-instrument-verification.json`
  — the pre-freeze verification record for every methodological instrument the
  new protocol names.
- [Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18), *Scientific
  Data* 3:160018 — the FAIR guiding principles, cited here only as the predecessor
  protocol already cites it at I3; not re-verified in this session.
