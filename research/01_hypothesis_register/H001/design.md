---
name: H001 — Intra-series coherence on Kalshi cumulative threshold ladders, tested as an executability question
description: Pre-registration DESIGN DRAFT for hypothesis H001. NOT FROZEN.
type: project
hid: H001
hypothesis_id: H001
title: Intra-series coherence on Kalshi cumulative threshold ladders, tested as an executability question
tier: 3
status: draft-unfrozen
date: 2026-09-04
created: 2026-09-04
owner: Sajan Koirala
branch: kalshi-arbitrage / prediction-market microstructure
governing_decisions:
  - docs/decisions/ADR-0003-specification-not-execution.md
  - docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md
corpus:
  branch: kalshi-strategy-multivocal
  state: IN PROGRESS
  protocol: docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md
  protocol_sha256: 32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac
  registration_commit: 4821611c1c93b5f929a76f3ba6207e900440cee5
  corpus_record: docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md
  corpus_record_state: >
    EXISTS ON DISK, verified by directory listing on 2026-09-04 during this
    remediation pass. An earlier state of this front matter recorded it as
    "(DOES NOT EXIST YET)"; that statement was FALSE at the time it was audited
    and is corrected here. Pre-freeze checklist item 1 (§12) is DISCHARGED.
  corpus_record_sha256: >
    bedb10fbb71ee2024c6ca1852bb586d2146443ca09dae6df7edd6589bba6e430
    COMPUTED BY THE LEAD 2026-09-04, LAST, after every corpus-record edit for
    rounds 1 and 2 was final — M2 enumeration, head limitation 10 (known-item
    recall), DI-8, DI-9, and gap-register changes G-26 through G-29 all included.
    The ordering rule below was satisfied, not merely stated.
    SUPERSEDED WORDING, retained struck and legible because this field once
    asserted the opposite of `read_state_digest_discipline` six lines below, so
    that a tool or reader keying on this field alone received the superseded
    answer: ~~"TO COMPUTE — no shell or hashing tool was available in the session
    that performed this remediation, and NO DIGEST IS ASSERTED rather than
    guessed."~~ That stated reason no longer holds — the lead session does have a
    hashing tool — but NO DIGEST IS WRITTEN HERE, for a different and stronger
    reason, stated as the ORDERING RULE below.
    Command to run, from the repository root, at the time the ordering rule
    permits:
    `python -c "import hashlib,pathlib;print(hashlib.sha256(pathlib.Path('docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md').read_bytes()).hexdigest())"`.
    ORDERING RULE (binding, and the reason this field holds a placeholder rather
    than a value): the corpus-record digest is computed LAST, after every
    corpus-record edit for the round is final — M2 enumeration, the known-item
    recall result, the new data-integrity entries and the gap-register changes
    included. A digest taken mid-round pins a byte state that will not exist at
    freeze; it is not a weak pin but a false one, and it invites a reader to take
    a superseded state as the registered one. THIS RULE EXISTS BECAUSE ROUND 1
    VIOLATED IT: a corpus-record digest was computed and recorded in
    `read_state_digest_discipline` while the corpus record was still under edit,
    and it is struck there for that reason.
    CARRY THE LIMIT WITH THE NUMBER WHEN THE NUMBER IS WRITTEN — the same limit
    `read_state_digest_discipline` carries for the arm files. The digest, once
    computed, is of a POST-REMEDIATION byte state. That is NOT the state this
    draft read, and it does NOT retroactively verify any quotation already in
    this draft; §0.3 and remediation DI-8 both record in-place changes made after
    the draft was written. It pins the corpus record for a FUTURE re-read only.
    It is re-verified at freeze; a digest that differs at freeze is a changed
    corpus record, not a confirmation.
  arms_read_for_this_draft:
    - ks-venue-docs.json (30 documents, 132 clauses, complete as of 2026-09-04)
    - ks-lateral-records.json (32 classes, complete as of 2026-09-04)
    - ks-github-records.jsonl (43 artifacts, complete as of 2026-09-04; extraction
      found INCOMPLETE for ks-sc-001 and TRUNCATED for ks-sc-002 — see §1.6)
    - ks-instrument-verification.json (8 instruments, complete as of 2026-09-04)
    - ks-academic-candidates.json / ks-academic-identified-universe.json (PROVISIONAL — see §0.3)
  read_state_digest_discipline: >
    Every arm file above is a mutable working log that this draft quotes. A quote
    from a mutable file is unverifiable unless the file's byte state AT READ TIME
    is recorded, and §0.3 documents one case where this draft quoted a state that
    the file no longer holds. Therefore, before `/preregister` may run, the
    SHA-256 of EACH of the five arm files above must be computed and recorded
    beside its read date, by the same command given under
    `corpus_record_sha256`. The remediation session had no hashing tool and
    correctly declined to fabricate a digest; the LEAD SESSION computed the FIVE
    ARM-FILE digests on 2026-09-04 and they are recorded here, so this obligation
    is DISCHARGED AS TO COMPUTATION FOR THE ARM FILES ONLY. The corpus-record
    digest is DEFERRED under the ORDERING RULE in `corpus_record_sha256` above
    and is NOT asserted here:
      corpus record lit_review_kalshi-strategy-multivocal_2026-09-04.md
        = bedb10fbb71ee2024c6ca1852bb586d2146443ca09dae6df7edd6589bba6e430
          (computed LAST, 2026-09-04, per the ordering rule; supersedes the struck
           round-1 value below, which was taken mid-round)
        (round-1 value ~~b36795140b5bc93f449622d128fa512d285777f0abcf4ab2bdab1e399725134b~~
         STRUCK: computed mid-round while the corpus record was still under edit,
         which is the violation the ordering rule now forbids. Do not rely on it.)
      ks-academic-candidates.json
        = ad2b8208a25512cdd1337b040d38fa036c2afa0c5d1ba3dcf5af1c64b77f4b58
      ks-github-records.jsonl
        = 98e312934e12fb42b19f93f1542d8fc8950805df0d844d8c430e563c94989b19
      ks-venue-docs.json
        = cab38c3f50d1f6b43455c409bc4c8e20695979456eacaee92b8b11c8cc2fec1d
      ks-lateral-records.json
        = 3fd644ae22bbb7db981c543604c94dfd6f6f19130176f0b548ee9f9f284aa181
      ks-instrument-verification.json
        = af4da817c2d2dcabdf851df62637bcb5322b2d32b313b19680ff0b15ac2e7028
    CARRY THE LIMIT WITH THE NUMBERS. These are digests of the byte state on
    2026-09-04 AFTER round-1 audit remediation, which is NOT the state this draft
    read: §0.3 documents that this draft quoted ks-academic-candidates.json at a
    mid-run 480/144 state, and the corpus record was corrected in place by
    remediation DI-8 after the draft was written. They therefore pin the files
    for a FUTURE re-read; they do not retrospectively make this draft's existing
    quotations verifiable. Pre-freeze checklist item 7 stays OPEN on its
    remaining components: re-reading each file at the pinned digest and
    re-verifying the ks-sc-001 / ks-sc-002 sentences at byte depth.
freeze_status: >
  THIS DOCUMENT IS NOT FROZEN. /preregister has NOT been run. No ReproLog has been
  emitted for it, no commit carries it, and its SHA-256 is therefore NOT a
  registration hash — it is the digest of a draft that is expected to change.
  The corpus record this design depends on
  (docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md) NOW
  EXISTS; the previous statement in this field that it "does not exist" was false
  and pre-freeze checklist item 1 is DISCHARGED. The operative reason this design
  remains `draft-unfrozen` is now pre-freeze checklist items 2–7 (§12): the
  academic arm's stage-1 screening of ks-a-057 has not been performed; the
  KSL-C02 mutual-exclusivity flag has no S-D clause; the per-series fee
  multiplier table is not extracted, so p* in §1.5 is not computable; the
  rulebook in force was not located, so §8.1's point-in-time reconstruction is
  blocked at source; the venue clauses have not been re-retrieved and
  re-digested; and no read-time digest has been recorded for any arm file or for
  the corpus record. Freezing now would register a design whose cost function is
  not point-in-time reconstructible and whose quoted sources have no verifiable
  byte state.
citations: see §12 References. No DOI is asserted for any venue document; venue
  material is cited by clause id into ks-venue-docs.json with its retrieval date.
external_doi: null
---

# H001 — Intra-series coherence on Kalshi cumulative threshold ladders, tested as an executability question

## 0. Preliminaries the reader must have before §1

### 0.1 What this document is, and what it can never become

**castles specifies; it does not execute** ([ADR-0003](../../../docs/decisions/ADR-0003-specification-not-execution.md)).
This document specifies a test: its null, its statistic, its surrogates, its
aggregation rule, its refutation condition. **An executing project runs it.**
Nothing here acquires market data, calls an exchange API, fits anything,
backtests anything, states a tradeable rule, states a position size, or states an
expected return. Every parameter whose value would require data is left
`TO COMPUTE` with its selection procedure named; computing it is the executing
project's work and the value is recorded *there* with its provenance, never
backfilled here (ADR-0003 §Decision).

`rules/quant-project.md` and `REVIEW.md` bind this artifact by explicit adoption
([ADR-0004](../../../docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md)),
which states that blocking directives 1–7 "bind the branch's first empirical
stage, wherever it occurs" and that the obligation therefore attaches to *this
specification*: "a test specified here must be specifiable **under** directives
1-7, and any specification that could not satisfy them is defective at the point
of writing even though nothing here will run it." §§6, 7, 9, 10 and 11 below
discharge that obligation directive by directive.

**Layout deviation, recorded per instruction:** the `pre-register-hypothesis`
skill specifies `research/01_hypothesis_register/H<NNN>/design.md`, which sits
inside the `research/` work-in-progress root that `CLAUDE.md` §"Directory layout"
already sanctions; the only conflict is with the global default filename
`{type}_{description}_{YYYY-MM-DD}.md`, and the register's per-HID directory
convention is preferred because the HID directory already carries the type and
description that the default filename would encode.

### 0.2 Force of every number in this document

Under `~/.claude/CLAUDE.md` §"Parameter & Prompt Selection" and charter
commitment 3, no numeric threshold appears here without one of three labels:
`QUOTED` (verbatim from a source, with its locator), `TO COMPUTE` (with the
selection procedure named), or `CONVENTION` (with its provenance). There are no
bare numbers.

**Three numeric thresholds in the practitioner record are recorded as NOT
ADOPTABLE and are NOT used anywhere in this design.** The lateral arm's own
header (`ks-lateral-records.json`, `magic_number_note`) states: *"Several sources
state numeric thresholds with no derivation (KSL-C10 five percentage points;
KSL-C19 fifteen minutes / two to four hours / twenty-four to forty-eight hours;
KSL-C28 a ~$0.15 price floor). Each is recorded verbatim as that source's claim,
flagged in compiler_notes, and is NOT adopted. None may be carried into a
downstream parameter choice without its own empirical justification."* This
design carries none of the three. A fourth figure — KSL-C13's *"Polymarket takes
roughly 2% on winning positions and Kalshi charges up to a 3% taker fee, so a
combined 5% drag means any spread under about 6% is dead on arrival"* — is
likewise that source's own arithmetic on an observation whose capture time is not
recorded (its `compiler_notes`: *"the arithmetic is checkable, the observation is
not"*), and is not adopted either.

**Two further figures, both from `ks-sc-002`, are added to that NOT-ADOPTABLE
list by §1.6(ii):** the mid-range round-trip break-even move (`QUOTED 10.7¢`) and
the tail round-trip hurdle (`QUOTED 2.6¢`). Both are stated at README depth with
no derivation shown on the page, and neither is adopted as a parameter anywhere
in this design. They are used only as external reference points against which an
independently recomputed quantity is compared (§9.2 item 1).

### 0.3 State of the academic arm when this draft was written

**Read-time state, quoted with its provenance and its supersession recorded.**
`ks-academic-candidates.json` was read on 2026-09-04 during the drafting of this
design and reported, AT THAT READ, `n_deduplicated_records: 480` and
`n_in_reported_branches: 144`. **No SHA-256 was recorded at that read**, so the
byte state those two figures came from cannot now be reconstructed — a
verification gap recorded here rather than papered over. **On re-reading the same
file during the 2026-09-04 remediation pass, the file reports
`n_deduplicated_records: 528` and `n_in_reported_branches: 152` (lines 18–19).**
The earlier figures were therefore a mid-run state of a live arm and have been
superseded. **No claim anywhere in this design rests on either pair of counts**;
they are reported only to characterise the arm as incomplete. The digest of the
file as it now stands is `TO COMPUTE` by the command in the front matter's
`corpus_record_sha256` field applied to
`docs/literature/search_logs/kalshi-strategy-multivocal/ks-academic-candidates.json`,
and recording it is pre-freeze checklist item 7.

The same file states in its own `what_this_is_NOT` block:
*"No section 4.2 stage-1 disposition is assigned in this file. No record here is
included, excluded, or promoted."* and *"under section 4.4 every row is therefore
a G1 row until a screening session decides it: identified, eligibility not
assessed, nothing about its merits determined."* **The academic arm is treated as
PROVISIONAL and possibly mid-run.** No academic record is load-bearing anywhere
in this design. One identified record is named only as a screening obligation:
`ks-a-057`, *"Executable Arbitrage and Market Efficiency in Prediction Markets"*,
arXiv:2608.00666 (2026), identified from query `ks-arxiv-07`, **eligibility not
assessed**. If screening admits it, this design must be revised before freeze,
because a paper with that title may already answer, contradict, or pre-empt the
statistic in §1.

---

## 1. Hypothesis

### 1.1 H0 and H1

Let `L` be a single Kalshi **cumulative threshold ladder** — one underlying, one
expiry, rungs `i = 1 … n` with strictly increasing thresholds `k_1 < … < k_n`,
where rung `i` resolves YES iff the expiration value of the underlying exceeds
`k_i`, so that YES on rung `i` implies YES on every rung below it. Let `t` be one
instant, and let `T(L, t)` be the statistic defined in §1.4.

- **H0 (the null actually tested):** for every registered ladder `L`, every
  registered rung-pair or rung-subset within it, and every registered snapshot
  instant `t`, `T(L, t) <= 0`. In words: **there exists no set of simultaneously
  executable orders on one ladder at one instant whose worst-case settlement
  payoff is strictly positive after the venue's stated fee function, its stated
  rounding direction and granularity, the minimum tick, the size actually
  available at the touch, and full cash collateralisation.**

- **H1 (the alternative, stated with sign, magnitude AND frequency):** there
  exists at least one registered triple `(series, rung-subset, snapshot)` with
  `T(L, t) >= delta`, occurring at a relative frequency of at least `phi` across
  the registered family, and persisting for at least `m` consecutive snapshots.
  `delta`, `phi` and `m` are `TO COMPUTE`; their selection procedures are named
  in §9.2 and §9.3. H1 is a **union alternative** — an existence claim — and
  therefore requires family-wise control (§9.1).

**H0 is not a statement about prices and H1 is not a statement about prices.**
Neither refers to a deviation of a price sum from 1. Both refer to the worst-case
payoff of an *order set*, which is a different object: it is defined on the
executable side of the book at the size available there, not on a mid or a last
trade.

### 1.2 Why this and not a forecasting hypothesis

The signal is **internal to one book at one instant**. The relation being tested
is the ladder's own nesting relation, which the practitioner record states
plainly (KSL-C01, verbatim): *"Because a higher strike can only resolve yes if
every strike below it also does, prices must decline as the strike rises. A
ladder where Above $81.00 costs more than Above $80.50 is offering an arbitrage
once the gap clears Kalshi's per-trade fee, and it gets corrected fast."* Its
corroborating source states the same relation for CPI ladders: *"Above-3.0% can
never be worth more than above-2.5%, because every world where the first pays
also pays the second; when a thin ladder briefly quotes them out of order, you
are looking at a liquidity gap, not informa[tion]"*.

Because the relation is internal, **no probability estimate of the underlying
event is required at any point.** Consequently the researcher degrees of freedom
that a forecasting design introduces are structurally absent: there is no feature
set to choose, no model class to choose, no training window to choose, no
forecast horizon to choose, and no target variable whose definition could be
revised after seeing the data. What remains to be chosen is the cost function —
and the cost function is a published document, not a modelling choice (§1.3).

This is the reason the hypothesis is worth registering at Tier 3 rather than
abandoned in favour of a price hypothesis: the corpus's two nearest empirical
records both report that the price-forecasting route is closed (§1.6), and both
close it by way of costs rather than by way of prediction quality.

**Directive-8 compliance (`REVIEW.md`, citation or derivation).** The nesting
relation carries a citation (KSL-C01 and its corroborator). The cost function
carries a citation (venue clauses, §1.3). The statistic in §1.4 is an in-document
derivation from those two. No unattributed factor appears.

### 1.3 The cost function is documented, not assumed

Every element below is quoted from `ks-venue-docs.json`, retrieval date
**2026-09-04**, with its clause id. The arm's own `retrieval_date_warning`
applies to all of them: *"EVERY RULE IN THIS FILE IS DATED 2026-09-04 BY
RETRIEVAL … a clause quoted here without that retrieval date is worthless."*

| Element | Clause | Verbatim |
|---|---|---|
| Taker fee formula | `d01-c2` | `fees = round up(M x 0.07 x C x P x (1-P))` |
| Taker multiplier default | `d01-c3` | `M = the multiplier for each contract (default is 1 unless otherwise indicated)` |
| Maker fee formula | `d01-c4` | `fees = round up(M x 0.0175 x C x P x (1-P))` |
| Maker multiplier default | `d01-c5` | `M = the multiplier for each contract (default is 0 unless otherwise indicated)` |
| Rounding direction | `d01-c6` | `round up = rounds up such that the fee + positionCost is rounded to a centicent` |
| Who pays | `d01-c1` | `Trading fees are only charged for orders that are immediately matched with orders sitting on the orderbook…` |
| Per-membership-class rounding granularity | `d08-c1` | `* Direct member balances are aligned to $0.0001 (0.01c)` / `* Non-direct member balances are aligned to $0.01 (1c)` |
| Rounding fee exists as a distinct charge | `d08-c2` | `When a trade produces a balance change that is more precise than the user's target balance precision, the exchange charges a **rounding fee** to bring the balance back to that target.` |
| Net fee floored at zero | `d08-c3` | `**Net fee** = trade fee + rounding fee - rebate (always >= \$0.00)` |
| Cost is path-dependent within an order | `d08-c4` | `The fee accumulator is maintained per order across all fills regardless of whether the fills are taker or maker. If an order initially takes … and then becomes a resting maker order, the accumulated rounding carries over to subsequent maker fills.` |
| Minimum tick | `d21-c3` | `Minimum Tick:The Minimum Tick size for the Contracts hall be $0.01.` |
| Settlement value | `d21-c4` | `Settlement Value:T he Settlement Value for this Contractis $1.00.` |
| Settlement fee | `d01-c8`, qualified by `d07-c3` and `d18-c3` | `There is no settlement fee.` / `Settlement fees are zero for simple yes/no determinations but may apply for sub-cent scalar settlement.` / `"Traders may be charged fees for Settlement of Contracts in an amount to be reflected from time to time on Kalshi's website."` |

Four qualifications that the executing project may not drop:

1. **The tick and the settlement value are sampled from ONE series, not
   established venue-wide.** `d21-c3` and `d21-c4` come from the terms and
   conditions of a single contract (Kalshi Weather Index, San Francisco Bay
   Area). The venue arm states in its own `document_classes` note for class 2:
   *"ONE series out of the roughly ninety named in the fee schedule was specified
   at this depth; this is a sampled retrieval, not an enumeration of the contract
   set."* **No venue-wide minimum-tick clause was located.** The executing
   project must read the tick from the terms and conditions of each series it
   registers.
2. **The per-series multiplier is published but was not extracted.** `d01-c3` and
   `d01-c5` make `M` a per-series fact; `ks-vr-d01`'s `tables_not_quoted` states
   the per-series multiplier table (*"roughly 90 series"*) exists in the document
   but *"Column alignment in these tables is DESTROYED by text extraction … so NO
   cell value is quoted as verbatim."* `M` is therefore `TO COMPUTE` per series
   by re-reading the schedule in force at `t`.
3. **The maker leg is not free by default and is not a rebate.** `d01-c4`'s
   `what_it_constrains` field records: *"Where the maker multiplier is non-zero
   Kalshi charges makers a positive fee - it is not a rebate."* Any assumption
   that a passive leg is costless is a per-series fact to be read, never assumed
   (`d01-c5`).
4. **The taker fee applies per side.** `d01-c1` decides which side of a fill
   bears the fee; a two-leg order set that takes on both legs bears it twice.

### 1.4 The test statistic

Not a deviation of a price sum from 1. **The statistic is the worst-case
settlement payoff of the cheapest executable order set, net of stated fees,
upward rounding at the member's own granularity, and the carrying cost of full
cash collateral, with the size available at the touch inside the statistic rather
than in a footnote.**

Fix a ladder `L` at snapshot instant `t`. Because the ladder is cumulative and
nested, the settlement state space is exactly `n+1` states: state `j ∈ {0,…,n}`
means rungs `1…j` settle YES and rungs `j+1…n` settle NO.

An **order set** is an integer vector

```
q = ( q[i,s,d] )   for i = 1..n ;  s ∈ {YES, NO} ;  d ∈ {buy, sell}
```

`q[i,s,d]` is a contract count. Define:

- `p[i,s,d](t)` — the executable touch price for that leg at `t`, in dollars;
  the ask for a buy, the bid for a sell. **Never a mid, never a last trade.**
- `A[i,s,d](t)` — the size displayed at that touch at `t`, in contracts.
- `V` — settlement value per contract, `QUOTED $1.00` (`d21-c4`).
- `tau` — minimum tick, `QUOTED $0.01` for the sampled series (`d21-c3`), per
  series `TO COMPUTE` from that series' terms and conditions.
- `g` — the member's own balance-alignment granularity, `QUOTED $0.0001` for a
  direct member and `QUOTED $0.01` for a non-direct member (`d08-c1`). **`g` is a
  property of the participant, not of the venue**, so `T` is participant-indexed
  and must be reported for both values of `g`.
- `M_taker(series, t)`, `M_maker(series, t)` — the per-series multipliers in
  force **at `t`** (`d01-c3`, `d01-c5`), `TO COMPUTE` per series per snapshot
  from the schedule in force at `t` (§8).

**Gross worst-case payoff.** For a long YES on rung `i`, the payoff in state `j`
is `V·1{i <= j}`; for a long NO it is `V·1{i > j}`; a sell of either is the
negative of the corresponding long. Write the state-`j` gross settlement value of
`q` as `G(q, j)`, and the cash outlay at entry as

```
X(q) = Σ_{i,s}  p[i,s,buy](t) · q[i,s,buy]  −  Σ_{i,s} p[i,s,sell](t) · q[i,s,sell]
```

**Fee term.** Per leg, evaluated at that leg's own executable price, per
`d01-c2`/`d01-c4` with the rounding of `d01-c6` applied at the member's own
granularity `g` per `d08-c1`, `d08-c2` and floored per `d08-c3`:

```
F(q) = Σ_legs  ceil_g ( M_role(series,t) · c_role · q_leg · p_leg · (1 − p_leg) )
       + R_g(q)
c_taker = 0.07      (QUOTED, d01-c2)
c_maker = 0.0175    (QUOTED, d01-c4)
ceil_g(x) = the smallest multiple of g that is >= x        (d01-c6, d08-c1)
R_g(q)    = the residual rounding fee that returns the post-trade balance to the
            member's alignment g, accumulated PER ORDER across fills and carried
            across a taker→maker role transition within one order (d08-c2, d08-c4)
```

`R_g` is written separately from the `ceil_g` term because `d08-c2` states it is
a distinct charge *"over and above the published fee formula"* (`d08-c2`
`what_it_constrains`), and `d08-c4` states it is order-path-dependent, so it
cannot be evaluated fill-by-fill in isolation.

**Role ambiguity term.** `M_role` is not determined at submission time on every
series. `d18-c2` (QUOTED): *"for trades not involving an order that has been
resting on the order book for more than 5 seconds: (1) Traders executing against
a quoter will pay the equivalent of a "taker" fee, and (2) quoters whose quote is
accepted shall pay the equivalent of a "maker" fee. The Exchange will originally
assess normal fees, and the fee adjustment shall take place no greater than 5
seconds after execution."* Therefore `F(q)` is evaluated under **every admissible
role assignment** and the **maximum** is taken. Role assignment is a term of the
statistic, not a footnote (§5).

**Collateral term.** `d13-c2` / `d14-c2` (QUOTED, clean text at `d14-c2`): *"All
Member positions are fully cash collateralized, and no Member can take positions
that would lead to an exposure that exceeds the funds deposited in the Member
Account."* Write `W(q)` for the cash that must be posted and held — the worst-case
exposure of `q`, reduced by the netting that `d07-c1` states (*"Only net
positions are settled (after netting)"*) and by any venue collateral-return
mechanism the executing project verifies applies (KSL-C07, KSL-C08; both are
practitioner records referring to venue behaviour and both must be re-verified at
S-D depth before use). Then

```
K(q) = W(q) · r · H
r = the participant's cost of capital, TO COMPUTE (selection procedure §9.4)
H = the collateral holding interval, TO COMPUTE and UNBOUNDED ABOVE (see §5)
```

**The statistic.**

```
T(L, t) =   max            [  min      G(q, j)  −  X(q)  −  F(q)  −  K(q)  ]
          q ∈ Q(L,t)        j ∈ 0..n
```

subject to the admissibility set `Q(L,t)`:

```
(a) 0 <= q[i,s,d] <= A[i,s,d](t)                 size available at the touch
(b) the whole of q must be submissible within one token-bucket admission
    (d06-c8: "The whole batch must fit in the bucket at once. A 25-order create
    batch needs 250 tokens available when it arrives, or the entire batch is
    rejected."), evaluated at the entry tier — Basic (d06-c4)
(c) the resulting position respects the per-strike accountability level of every
    strike it touches simultaneously (d21-c2), and the per-contract regime of
    d17-c2
(d) prices are on the tick grid: p is an integer multiple of tau (d21-c3)
```

Two properties are deliberate. **First, `T` is a max of a min:** the inner
minimum over settlement states is what makes the claim a worst-case claim rather
than an expected-value claim, so no probability of any state is required — which
is the point of §1.2. **Second, constraint (a) puts depth inside the statistic:**
an order set that is only executable for one contract has its `T` computed at one
contract, so the tick and the rounding granularity are charged against it at
their full relative weight. A statistic computed on top-of-book prices without
`A[i,s,d](t)` would be a different and easier statistic, and this design does not
use it.

`T` is computed **per rung-subset**: the two-rung subsets are the direct test of
the KSL-C01 monotonicity relation, and the full-ladder subset is the general
case. Both are members of the family (§9.1).

### 1.5 The central tension, and the observation pre-committed to discriminate it

**The fee is a downward parabola in price.** `d01-c2` makes the taker fee
proportional to `P(1−P)`, maximal at `P = 0.5` and vanishing in both tails. The
lateral arm records the consequence as its own class, KSL-C03, *"Fee-curve
curvature confines surviving field-sum candidates to the longshot tail"*
(verbatim): *"A field-sum gap only survives net of fees where each leg costs
about a cent or less — the tails of the dome. Mid-priced fields have their gap
eaten by 2¢ a leg. The math forces the real candidates into longshot-heavy
events"*. Its corroborating source states the same shape: *"The basic formula is
0.07 * P * (1-P) where P is the contract price … The max fee is at 50¢ of 1.75¢
per contract. As you get close to 0 or 100%, the fee becomes smaller"*.

**But the same tail is where measurement is worst.** Two effects, both sourced:

- *The tick is a large relative error in the tail.* `tau` is fixed at `QUOTED
  $0.01` (`d21-c3`) regardless of price, so the smallest expressible price change
  is a constant absolute amount and therefore a growing *relative* amount as
  price falls. `d21-c3`'s own `what_it_constrains` field states it: *"One cent on
  a $1 payout is the smallest expressible edge, and it bounds any coherence or
  cross-venue discrepancy that could be expressed as a price difference on this
  venue."*
- *Upward fee rounding at the coarser granularity can exceed the theoretical fee
  entirely.* KSL-C04, *"Round-up-to-the-cent fee quantisation inflates the
  effective rate at small order size"* (verbatim): *"Fees are always rounded up
  to the nearest cent. This matters at the margins. … Ten contracts at 50¢
  produces a raw fee of $0.175, which rounds up to $0.18 - an effective rate of
  7.2%, not 7%. The smaller the trade, the more pronounced this effect; the
  larger the trade, the more it fades into the noise"*. Combined with `d08-c1`, a
  **non-direct member** is aligned to `QUOTED $0.01` rather than `QUOTED
  $0.0001`, so the rounding applies at a granularity 100× coarser. Define the
  **crossover price** `p*` as the price at which the theoretical per-contract fee
  equals the member's granularity:

  ```
  p*  solves   M_taker(series,t) · 0.07 · p · (1 − p)  =  g
  p* is TO COMPUTE per series, per membership class, per snapshot
  (selection procedure: solve the quadratic exactly from the multiplier in force
   at t and the member's own g; no search, no tuning, no free parameter)
  ```

  Below `p*` the *rounded* fee is strictly larger than the *formula* fee, and the
  divergence grows as price falls. **This design asserts no numeric value of
  `p*`** — it is a function of a multiplier the venue arm could not extract
  (§1.3 qualification 2).

**The two competing predictions, stated so they cannot both be accommodated
after the fact:**

- **P-EDGE.** Any surviving positive `T` concentrates in the tail, because the
  fee vanishes there (KSL-C03).
- **P-NOISE.** Any apparent positive `T` concentrates in the tail because
  measurement error concentrates there — the tick is a large relative error and
  the coarse rounding granularity swamps the theoretical fee — and the corpus's
  own reading of out-of-order ladder quotes is that they are *"a liquidity gap,
  not informa[tion]"* (KSL-C01 corroborator) and that they get *"corrected fast"*
  (KSL-C01).

Both predict the same *location*. They differ in *what else must be true there*,
and this design pre-commits to the discriminating observation before any data
exists.

**DISCRIMINATING OBSERVATION (pre-committed).** The joint behaviour of `T` under
three simultaneous perturbations that P-EDGE and P-NOISE order oppositely:

| Perturbation | P-EDGE predicts | P-NOISE predicts |
|---|---|---|
| Recompute `T` at the **non-direct granularity** `g = $0.01` instead of `$0.0001` (`d08-c1`) | sign of `T` preserved for the same triples | positive `T` largely extinguished; survivors are exactly those with `p > p*` |
| Recompute `T` at the **size actually at the touch**, `q = A(t)`, instead of `q = 1` | `T` scales approximately linearly and stays positive | `T` collapses, because the positive `T` triples are those with the thinnest or one-sided books |
| Recompute `T` on the **quantisation surrogate** (§3.1) and the **staleness surrogate** (§3.2) | `T` on real data lies outside the surrogate ensemble | `T` on real data lies inside the surrogate ensemble |

**Pre-committed verdict rule.** P-NOISE is retained — that is, H0 stands — unless
`T` is positive at the coarse granularity `g = $0.01`, **and** at the depth
actually displayed at the touch, **and** outside both surrogate ensembles, on the
same triples. Any two of the three without the third is recorded as
`undetermined` in the charter's sense (charter §"Negative-result protocol" step
3: *"A layer with no discriminating observation is recorded `undetermined`"*),
not as a partial confirmation.

The depth condition is not decorative. `ks-sc-002` reports, for its own capture
window, *"**Most listed contracts are never tradable.** 79% of the 54,380
contracts observed never showed a two-sided book"* and, directly about ladders,
*"Threshold-ladder markets list dozens of strikes, and market makers only quote
near the money."* If that generalises to the registered series, the tail rungs of
a ladder are precisely the rungs with the least depth, and a `T` computed without
constraint (a) would be measuring the absence of a book.

### 1.6 What it must beat

Two negative results are already in the corpus. Both are located in
`ks-github-records.jsonl` and both are quoted here with their record ids.

**Two findings against that arm log are recorded in this section and must be read
with the quotations below.** In both cases the *primary source* (the README at
the pinned commit) states more than the arm log's `F4_evidence_quotes` /
`F9_preconditions_stated` extraction carried, and in both cases the omitted
material bears directly on how this design uses the record. The arm log is **not
edited by this design** — an arm log is that arm's artifact — and the findings are
registered here instead, against the log, for that arm to act on.

**(i) The always-NO baseline — `ks-sc-001`, `github.com/sudo-ai-git/kalshi-backtest`,
pinned commit `c32b700111a321db16a8cfae5eceaab0ea167dd8`, README SHA-256
`50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118`, accessed
2026-09-04.**

Verbatim, from the record's `F9_preconditions_stated` ("correct baseline
required"): *"The correct null for any strategy is the **always-NO baseline**,
and every candidate must beat it."*

Verbatim, `F10_outcome_reported`: *"Best candidate strategy (BUY_NO @
high-NO-prob) | +1.37% ROI, CI [1.13, 1.61], n=23"*, with `uncertainty` recorded
as *"CI [1.13, 1.61], n=23, and the README states the candidate is 'statistically
indistinguishable' from the always-NO baseline"*, over a data span of *"~92,000
settled/closed Kalshi markets; NO-tilt measured across a 30k settled sample"*.

Verbatim, on why: *"Favorites >> longshots (the classic favorite-longshot bias),
but that bias is already priced in and eaten by fees/spread."*

**FINDING AGAINST THE ARM LOG — `ks-sc-001` extraction is INCOMPLETE.** An
earlier state of this section asserted a "correction to the framing this design
was handed", to the effect that the record does not state that *no* price-based
strategy beat the always-NO baseline. **That assertion was FALSE and is
withdrawn.** The primary source states exactly that, and states a conclusion in
the same terms. Two sentences present in the README at the pinned commit are
**absent from every field of the `ks-sc-001` record** in
`ks-github-records.jsonl`:

| Missing sentence (verbatim) | Location |
|---|---|
| *"No price-based strategy clears the honest bar."* | README.md at pinned commit `c32b700111a321db16a8cfae5eceaab0ea167dd8`, under the section heading *"The headline finding (from ~92,000 real settled markets)"* — the section the arm log already cites for its `F10` table row |
| *"**Conclusion: there is no demostrable price-based edge in the public settled-market data.**"* [*sic*: "demostrable" is the source's spelling and is transcribed unaltered] | README.md at the same pinned commit, as a standalone bolded concluding line |

**Provenance of this finding, stated at the same force as everything else here.**
The two sentences were obtained by **re-fetching the pinned raw README URL
(`https://raw.githubusercontent.com/sudo-ai-git/kalshi-backtest/c32b700111a321db16a8cfae5eceaab0ea167dd8/README.md`)
during the 2026-09-04 remediation pass** — a re-fetch, therefore, not a re-read of
the arm log. Two limits on it: the fetch returned converted text rather than raw
bytes, so **the README SHA-256 was NOT recomputed at re-fetch** and the digest
above is still the arm log's; and no line numbers were obtained, so the locations
above are section-level and do not reach the item-level precision the arm log's
own `location` convention uses. Re-verifying both sentences at byte depth, with a
recomputed digest, is folded into pre-freeze checklist item 7.

**What this design does with the record, stated as a choice and not as a
correction.** The source makes two claims of different strength about the same
question:

- the **stronger** claim — *"No price-based strategy clears the honest bar"*, with
  the always-NO baseline defined as that bar, and the bolded conclusion that
  there is no demonstrable price-based edge in the public settled-market data;
- the **weaker** claim — that its *best candidate* is *"statistically
  indistinguishable"* from the always-NO baseline at `n=23` with `CI [1.13,
  1.61]`.

**This design deliberately uses only the weaker claim.** That is a conservative
choice, and the distinction matters: using the weaker of two claims a source
makes is conservative, whereas asserting that the source did not make the
stronger one is false, and the earlier text did the second. The reasons for the
choice are properties of the *evidence*, not of the source's wording:

1. The stronger claim is a universal negative over an unenumerated strategy
   space. This design cannot verify the space searched from README depth, so it
   does not lean on the universal.
2. The record's own `F10.cost_treatment` states: *"README states fees/spread
   consume the bias; the ROI figure's own cost treatment is not stated in the
   README"* — so the `+1.37%` figure's cost basis is unknown and it is **not**
   used as a comparator here.
3. `n=23` is small enough that the comparison is uninformative in the charter's
   step-2 sense without an MDES, which the record does not supply.

The stronger claim is therefore **recorded, attributed, and not relied upon** —
and, because it points the same way as this design's own §1.2 argument, relying
on it would in any case be relying on agreement rather than on evidence.

**(ii) The break-even bar — `ks-sc-002`,
`github.com/himagna16/kalshi-microstructure`, pinned commit
`817fe37ceb184bd649b71d0dbebb4a8e5718bb59`, README SHA-256
`753d94ddd29ee97929fa4d483420e105aeee602f34f610d69ec65b4bb7668462`, accessed
2026-09-04.**

Verbatim, `F9_preconditions_stated` ("break-even move required for a taker round
trip"): *"A contract trading at 40–50¢ must move **10.7¢** (≈ 11 percentage
points of implied probability) before a taker round trip breaks even."*

**FINDING AGAINST THE ARM LOG — `ks-sc-002` extraction is TRUNCATED at exactly
this point.** The arm log's quote ends at "breaks even." The **next sentence in
the README** is:

| Missing sentence (verbatim) | Location |
|---|---|
| *"Even at the tails the hurdle is 2.6¢."* | README.md at pinned commit `817fe37ceb184bd649b71d0dbebb4a8e5718bb59`, cost-to-trade section, **immediately following** the sentence the arm log quotes as its "break-even move required for a taker round trip" precondition |

Obtained by the same 2026-09-04 re-fetch of the pinned raw README URL
(`https://raw.githubusercontent.com/himagna16/kalshi-microstructure/817fe37ceb184bd649b71d0dbebb4a8e5718bb59/README.md`),
under the same two limits: converted text rather than raw bytes, so the README
digest was **not** recomputed at re-fetch, and no line number was obtained.

**Why the truncation is material and not clerical.** An earlier state of this
section argued that the source states a break-even bar only mid-range and leaves
the tail bar entirely `TO COMPUTE`. **The source states a tail figure itself**,
in the sentence the arm log dropped, and a design that registers a ceiling
against the mid-range figure while the source's own tail figure is roughly a
quarter of it has registered the ceiling in the wrong place. §9.2 item 1 is
re-registered accordingly.

Verbatim, the fee statement both figures derive from: *"Kalshi charges takers
`0.07 × P × (1−P)` per contract per side. That fee is maximized exactly where
event trading is interesting — at uncertain prices — and it stacks on top of a
spread that is also widest mid-range"*. Data span: *"July 30 to August 17, 2026;
8.06M snapshots across 54,380 contracts; settlement outcome of 427,017 markets"*,
cost treatment *"Stated explicitly: spread plus the taker fee formula quoted
above"*.

**BOTH FIGURES ARE NOT ADOPTABLE.** `QUOTED 10.7¢` (mid-range) and `QUOTED 2.6¢`
(tail) are stated at README depth **with no derivation shown on the page**: the
fee formula is given, but neither the spread distribution used, nor the price
points at which "the tails" are evaluated, nor the arithmetic combining them is
stated. They fall under §0.2 on the same grounds as KSL-C10, KSL-C19, KSL-C28 and
KSL-C13's percentages, and neither may be carried into a downstream parameter
choice. Three further declarations attach, none of which may be dropped:

1. Both are **that source's own derivations at README depth**, not venue
   statements. The record's `F11_attribution_status` says so: *"The fee formula is
   stated as the venue's, without a citation to the venue's own fee schedule
   inside the README (an S-D document would carry it)."* This design carries the
   venue's own clause (`d01-c2`) instead.
2. `10.7¢` is stated **at 40–50¢, the middle of the price range**, and this
   hypothesis lives in the tail (§1.5); `2.6¢` is the source's own statement for
   "the tails", but the source does not say at which prices its tails begin.
   **The bar recomputed at the tail is `TO COMPUTE`** — selection procedure:
   evaluate the same round-trip construction using `d01-c2` with the in-force
   `M_taker(series, t)`, the observed per-rung spread distribution, and the
   member's own `g` per `d08-c1`, at the price decile of the triple under test.
   The recomputed tail bar — **not `10.7¢` and not `2.6¢`** — is the operative
   value of `delta` in §9.2. `2.6¢`, as the source's own tail statement, is
   retained there only as a **comparison reference**, and §9.2 item 1 states
   exactly what a disagreement with it does and does not license.
3. Both are **round-trip** figures — entry and exit both as taker. The statistic
   in §1.4 is a **hold-to-settlement** worst case, which does not pay an exit
   spread. The two are therefore not directly comparable and the executing
   project must state which it reports. This design reports the
   hold-to-settlement `T`, and reports the round-trip variant only as a
   sensitivity, because §5.3 establishes that hold-to-settlement is not a
   guaranteed exit and an exit may in fact be forced.

**Mechanism:** ladder nesting (KSL-C01 and its corroborator) constrains the joint
price vector; the venue's published cost function (`d01-c2`, `d01-c4`, `d01-c6`,
`d08-c1`–`d08-c4`) determines whether any violation of that constraint is
convertible into a strictly positive worst-case payoff at the size available.

**Primary citations:** see §13. Venue clauses are cited by clause id into
`ks-venue-docs.json` with retrieval date 2026-09-04, never by URL alone.

---

## 2. Universe and sample period

Bounded at pre-reg; no discretion later. **castles acquires none of this** —
§10 states what an executing project would have to obtain.

- **Instruments:** Kalshi cumulative threshold ladder series only. **Cumulative
  and nested, never mutually exclusive bands.** KSL-C01 states the contrast
  verbatim and it is a hard eligibility criterion: *"Compare that to a weather
  ladder , where the bands are mutually exclusive: the high temperature lands in
  82-83 or in 84-85, never both, so at most one band hits. The two ladders look
  identical on screen. Structurally they are opposites"*. A mutually exclusive
  field is a **different hypothesis with a different state space** (that is
  KSL-C02's field-sum relation) and is out of scope for H001. The concrete
  series list is `TO COMPUTE` — selection procedure: enumerate from the terms and
  conditions filed under CFTC Regulation 40.2 (`d22-c4`: *"( ii ) A copy of the
  rules that set forth the contract's terms and conditions;"*), retain those
  whose payout criterion is a threshold on a scalar underlying, and **register
  the resulting list before the first test** (§9.1).
- **Universe construction is a prerequisite step, not preprocessing.** KSL-C30
  (verbatim): *"Kalshi's raw /markets feed is flooded with auto-generated
  combination markets, so a scanner boasting that it "monitors 14,000 Kalshi
  markets" is mostly watching synthetic combinations with no independent
  liquidity."* A registered family built from the raw markets endpoint would be a
  family of mostly synthetic instruments and the family-wise correction in §9.1
  would be computed over the wrong denominator. The KSL-C30 source *"states no
  filter rule on this page"*, so the filter itself is `TO COMPUTE` — selection
  procedure: retain only markets whose ticker resolves to a single-outcome
  contract in a filed terms-and-conditions document, and report the retained
  count against the raw count.
- **The mutual-exclusivity flag is a practitioner claim, not yet an S-D fact.**
  KSL-C02 states *"Kalshi exposes a mutual-exclusivity flag on events, and any
  honest scan must gate on it"*. **No clause in `ks-venue-docs.json` documents
  that flag.** Recorded as an unverified precondition, referred to the
  exchange/regulator arm, and flagged as a data-acquisition risk in §10.
- **Frequency:** order-book snapshots at a stated, fixed resolution. **The value
  is `TO COMPUTE`** — selection procedure: the snapshot interval must be short
  relative to the measured quote-age distribution `Lambda` (§3.2) and must be
  feasible under the venue's published read budget (`d06-c1`, `d06-c2`), and is
  selected as the shortest interval satisfying both. The **only** empirical
  figure the corpus offers is a practitioner collector's, `ks-sc-002` (verbatim):
  *"a collector on a $6/month DigitalOcean droplet polled the Kalshi API roughly
  every 42 seconds (36,611 polling cycles, zero missed days) and recorded
  top-of-book quotes, sizes, and depth"*. That is recorded as the **only observed
  resolution in the corpus** and explicitly **not** adopted as this design's
  resolution: a 42-second interval is long relative to the KSL-C01 statement that
  out-of-order ladder quotes get *"corrected fast"*, and §9.3's persistence
  requirement `m` cannot be evaluated at a resolution coarser than the phenomenon.
- **Session(s):** continuous, minus the venue's stated unavailability. `d10-c1`
  (QUOTED): *"Every **Thursday from 3:00 AM to 5:00 AM ET**, Kalshi runs
  scheduled maintenance. During this window, a **trading pause** is in effect."*
  Snapshots inside a trading or exchange pause are registered as **ineligible**,
  not silently dropped, and their count is reported. `d03-c3` (QUOTED): *"Always
  check `status` on a market before placing orders; trading is only allowed when
  `status == "active"`."* — a snapshot of a non-active market yields no
  executable order set and `T` is undefined, not zero.
- **Train / validation / test windows:** time-ordered, disjoint, walk-forward.
  **k-fold is prohibited** (`rules/quant-project.md` §"Time-series integrity",
  adopted by ADR-0004). Window boundaries `TO COMPUTE` — selection procedure: set
  by calendar, fixed before the first test, and **aligned to fee-schedule and
  rule-change effective dates** so that no window straddles a change in the cost
  function (§8). This alignment requirement is a consequence of point-in-time
  discipline and it constrains the split before any data is seen.
- **Roll-handling note:** ladders are expiry-bounded, so there is no roll in the
  futures sense. There is a listing and delisting process instead, and it is
  fast: `d22-c3` (QUOTED) *"( 2 ) The Commission has received the submission by
  the open of business on the business day preceding the product's listing; and"*
  — one business day's notice. Series entering or leaving the registered universe
  mid-window must be handled by a rule fixed at registration, not by a later
  judgement.

---

## 3. Features

**This is not a supervised-learning design and there is no feature engineering.**
The fields below are the observable primitives the statistic reads, named so that
the executing project's `FEATURE_REGISTRY` and its point-in-time property test
(`pit-canary`, R3-5) have something to bind to. Version numbers are the executing
project's to assign; `@0.1.0` is a placeholder, not a claim about an existing
module.

- **Feature entries (`name@version`):**
  - `ladder_touch_quote@0.1.0` — per rung, per side, executable touch price
    `p[i,s,d](t)`. Bid/ask only. Mids and last trades are **excluded by
    construction**, because the hypothesis is about executability.
  - `touch_depth@0.1.0` — `A[i,s,d](t)`, size displayed at that touch. Load-bearing
    (§1.4 constraint (a)), not diagnostic.
  - `quote_age@0.1.0` — per rung, elapsed time at `t` since that rung's last quote
    change. The empirical distribution of this feature **is** the staleness
    surrogate's input (§3.2). If the executing project cannot measure it, the
    staleness null cannot be constructed and the design is not executable.
  - `ladder_membership@0.1.0` — the mapping from rungs to a single (underlying,
    expiry), with the nesting direction and the strike ordering, sourced from
    filed terms and conditions, not inferred from tickers.
  - `fee_schedule_in_force@0.1.0` — `(M_taker, M_maker, c_taker, c_maker,
    rounding rule)` **as of `t`**, not as of the analysis date (§8).
  - `rounding_granularity@0.1.0` — the participant's `g` per `d08-c1`. Constant
    per membership class, but the statistic must be reported at both values.
  - `market_status@0.1.0` — `d03-c3`'s `status`, plus the disputed/amended states
    KSL-C32 reports the API exposes.

**Point-in-time property test is mandatory and is not a formality here.**
`fee_schedule_in_force@0.1.0` is the feature most likely to leak, and §8 explains
exactly how.

---

## 4. Label construction

**Triple-barrier labelling per López de Prado's *Advances in Financial Machine
Learning* (AFML, hereafter; §3.4, "The Triple-Barrier Method") does not apply and
is not used.** There
is no forward-looking label to construct: the payoff of the order set in each
settlement state is fixed by the contract's own payout rule, known at `t`, and
the statistic takes the minimum over states. The template's fields are answered
as their nearest analogue so that the splitter in §6 has a horizon to purge on.

- **`pt_sl` (profit-take / stop-loss multipliers):** not applicable. No path-based
  exit is defined. Recorded as deliberately absent, not as unset.
- **`vertical_barrier` (duration):** the settlement horizon of the ladder. Its
  payout rule is `d13-c3` (QUOTED, degraded extraction, transcribed exactly as
  the extractor returned it and never to be re-quoted as clean rule text): *"(a)
  When a C ontract e xpires and h as a  P ayout C riterion that encompasses the
  Expiration Valueofthe Underlying,suchContractwillpaytheS ettlementV alueforsuch
  Contracts(e.g.$1.00)totheholders oflongpositionsins uchC ontracts."*
  **This horizon is not fixed at entry and is unbounded above** — see §5.3. Its
  effective upper bound is therefore `TO COMPUTE` and is an *empirical*
  distribution, not a constant.
- **`volatility_estimator`:** not applicable. No volatility scaling enters the
  statistic.
- **Meta-label horizon effective upper bound (feeds splitter `purge`):**
  `TO COMPUTE` — selection procedure: the empirical upper quantile of realised
  settlement-completion time measured over the registered series, taken at a
  quantile that is itself `CONVENTION` and must be recorded with its provenance
  in the executing project. It cannot be read from any venue document: `d07-c2`
  (QUOTED) *"Markets typically settle shortly after expiration, but timing can
  vary based on market type, data source availability, and manual review
  requirements."*; `d21-c10` (QUOTED) *"S ettlement D ate: The Settlement D ate o
  f the Contract shall b e no later than thed aya fterthe E xpiration Date, unless
  the Market Outcome is under review pursuant to Rule 7.1."* — and no maximum
  duration for that review is stated anywhere in the retrieved document set.

---

## 5. Estimator, and the execution-risk terms it must carry

### 5.1 Estimator

- **Model class:** none. `T(L, t)` is the value of a **deterministic constrained
  optimisation** — a max-min over integer order sets, expressible as a
  mixed-integer linear program once the `ceil_g` fee terms are linearised with
  the standard integer-multiple-plus-slack encoding. There is nothing to fit.
- **Hyperparameter grid:** none. There is no hyperparameter. This is a stated
  design property, not an omission: it is the second half of the §1.2 argument
  that the researcher degrees of freedom are absent.
- **Search protocol (grid / random / Bayesian, with budget):** not applicable to
  the estimator. The only quantities searched anywhere in this design are the
  surrogate ensemble sizes `B_quant` and `B_stale` (§3), both `TO COMPUTE` —
  selection procedure: increase `B` until the Monte-Carlo standard error of the
  surrogate's exceedance quantile is small relative to `delta`, and report the
  attained ratio.
- **Loss / metric:** none is minimised. `T` is reported, and its exceedance
  behaviour is tested (§9).

### 5.2 Execution risk is a term of the estimator, not a friction

Each item below enters `Q(L,t)`, `F(q)`, `K(q)` or the persistence requirement
`m`. None is a footnote.

**(a) Maker/taker role is reassigned after execution on at least one series.**
`d18-c2`, quoted in full in §1.4. Consequence: `M_role` is not a submission-time
constant, and `F(q)` is evaluated under both role assignments with the maximum
taken. A design that assumed maker treatment because a leg rested would be
mis-specified on that series.

**(b) Token-bucket rate limiting, all-or-nothing batches, and tiers that cannot
be bought.** `d06-c1` (QUOTED): *"Every authenticated request costs **tokens**.
Your tier sets your **budget**: the rate, in tokens per second, at which your
balance refills. Your sustained rate for an endpoint is `budget ÷ cost`."*
`d06-c2` (QUOTED): *"Most requests cost the default of **10 tokens**."*
`d06-c7` (QUOTED): *"A batch request costs the same as making each call
individually. Every item in the batch is billed separately"*.
`d06-c8` (QUOTED): *"The whole batch must fit in the bucket at once. A 25-order
create batch needs 250 tokens available when it arrives, or the entire batch is
rejected."*
`d06-c4` (QUOTED): *"* **Basic**: complete account signup. * **Advanced**: call
the [Upgrade Account API Usage Level endpoint](…). * **Expert, Premier, Paragon,
Prime, and Prestige**: earned automatically from your trading volume …, or
assigned by Kalshi."*
`d06-c5` (QUOTED): *"`volume share = your trailing 30-day volume ÷ (previous
month's exchange volume × 2)`"*.
`d06-c6` (QUOTED) gives the earn/keep ladder: *"| Expert | 0.075% | 0.05% | …
| Prestige | 1.00% | 0.80% |"*.
`d06-c9` (QUOTED): *"429 responses do not currently include `Retry-After` or
`X-RateLimit-*` headers."*

Three consequences, all first-order:
1. **"Simultaneously executable" is defined at the entry tier.** `Q(L,t)`
   constraint (b) is evaluated at **Basic**, because that is what a new
   participant has. Throughput above it is *earned from trailing volume share
   relative to the whole exchange* or granted at venue discretion — it cannot be
   purchased. KSL-C31 records the same structure independently: *"execution
   capacity is endogenous to trading activity."*
2. **A batch rejected in full is a leg-risk branch inside the worst case**, not
   an operational nuisance. The worst case over `j` in §1.4 must be taken jointly
   with the partial-execution branches admitted by the batch semantics.
3. **Backoff is unobservable**, so the latency cost of a throttled retry is
   itself `TO COMPUTE` from measurement, not from documentation.

**(c) Hold-to-settlement is NOT a guaranteed exit.** See §5.3.

**(d) Per-strike position accountability, consumed across strikes
simultaneously.** `d21-c2` (QUOTED): *"Position Accountability L evel: T he
Position Accountability L evel for the Contract s hall be $25,000 per strike, per
Member."* A laddered order set touches many strikes at once and consumes the
allowance at every one of them in the same instant, so the binding constraint on
`q` is a *vector* of per-strike constraints, not a scalar. Surrounding regime,
all QUOTED: `d17-c2` — two size regimes coexist and which binds is a per-contract
fact; `d17-c3` — above the level a member *"must refrain from increasing the size
of their position or reduce the size of their position in a timely fashion if
instructed"*; `d17-c4` — *"Kalshi shall have the authority to liquidate the
applicable position"*; `d17-c5` — market-maker levels of `$1M` / `$10M` against a
generally applicable level of `$250k` or less; `d17-c6` — market makers are
exempt from hard position limits on obligated contracts; `d17-c7` — a federal
ceiling sits above; `d14-c3` — positions across coordinated accounts aggregate,
so the constraint cannot be relaxed by splitting. The `$25,000` figure is `QUOTED`
from one series' filed terms; `d16-c5` records that the appendix naming which
contracts carry a higher limit is **confidential**, so the public record cannot
say which series differ.

**(e) Full cash collateralisation and its capital cost.** `d14-c2` (QUOTED, clean
text): *"All Member positions are fully cash collateralized, and no Member can
take positions that would lead to an exposure that exceeds the funds deposited in
the Member Account."* This is the entire reason `K(q)` exists in §1.4: there is no
leverage, the worst-case cash is posted, and it is posted for a holding interval
that §5.3 shows is unbounded above. `d07-c1` (QUOTED) *"* Only net positions are
settled (after netting)"* reduces `W(q)` where netting applies; KSL-C07 and
KSL-C08 describe venue mechanisms (collateral return at entry; closure by opening
the offsetting side with instant netting) that would reduce it further, and both
are **practitioner records that must be re-verified at S-D depth before entering
`W(q)`** — the lateral arm itself refers them onward.

**(f) Auto-generated combination markets make universe construction a
prerequisite.** KSL-C30, quoted in §2. This is placed under execution risk as
well as universe because it determines the denominator of the family-wise
correction (§9.1).

### 5.3 Why the exit is not guaranteed, stated separately because it drives `H`

- `d17-c9` (QUOTED): *"R ule7.2isa mendedtop rovidethattheExchangemaym odifya C
  ontract'sE xpiration Date in the event that a  market's Underlying c annot b e
  m easured on the original E xpirationD ate.Forexample,theE xchangem ayd elayE
  xpirationuntildatab ecomes available.R ule7.2isalsoa mendedtoprovidethattheE
  xchangem aym oveE xpiration earlier if the Payout Criterion is satisfied
  earlier."* — **expiration is movable in both directions.**
- `d21-c9` (QUOTED): *"C ontingencies: Before S ettlement, K alshi may, at its
  sole d iscretion, initiate the Market OutcomeReviewP rocesspursuanttoRule7.1
  oftheR ulebook."* — discretionary pre-settlement review, **not confined to data
  failure**.
- `d21-c10` (QUOTED, §4): settlement within one day *"unless the Market Outcome
  is under review"*, and **no maximum review duration is stated**.
- `d17-c8` (QUOTED): where the payout criterion cannot be determined, *"the
  Exchange will determine a fair p ayout a llocation"* — so the `$1.00`/`$0.00`
  payoff in `G(q, j)` has an **unpriced discretionary branch**.
- `d10-c2` (QUOTED): under an exchange pause a resting order **cannot** be
  cancelled — *"| **Cancel orders** | Yes | No |"*.
- `d23-c1` (QUOTED, CFTC press release 9267-26, 2026-07-14): *"The Commodity
  Futures Trading Commission today exercised its authority to stay an emergency
  rule change proposed by KalshiEX, LLC in response to a Michigan state court
  order directing the company to cancel certain previously executed trades … The
  CFTC also exercised its emergency authority to order KalshiEX, LLC to fulfill
  the open trades in accordance with its normal practices."* — **trade finality is
  contested, not assumed.**

Together these mean `H` in `K(q)` is a random variable with **no stated upper
bound** and with a discretionary branch on `G` itself. The executing project must
either measure `H`'s distribution or report `T` as a function of `H` across a
pre-registered range; it may not substitute a point value.

---

## 6. Splitter

- **Splitter choice:** `PurgedWalkForwardSplitter`. The splitter, and the `purge`
  and `embargo` constructs used throughout this section, are **López de Prado's**,
  AFML **§7.4** ("Purged K-Fold Cross-Validation" — purging and embargoing); named
  here with provenance because §0.2 and §1.2's directive-8 statement forbid an
  unattributed named method, and an earlier state of this document named all three
  with no citation anywhere. Walk-forward only; **k-fold
  is prohibited** by `rules/quant-project.md` §"Time-series integrity" as adopted
  in ADR-0004. CPCV is not used, because the resampling that H001 needs is
  supplied by the two surrogates in §3 rather than by combinatorial path
  recombination, and mixing the two would double-count the same dependence.
- **`embargo` selection method:** `TO COMPUTE` — selection procedure: the maximum
  of (i) the lag at which the residual PACF of the per-triple `T` series is
  indistinguishable from zero and (ii) the **Politis–White automatic block
  length** for the same series — **Politis & White 2004**, *Automatic Block-Length
  Selection for the Dependent Bootstrap*, Econometric Reviews 23(1):53–70,
  doi:10.1081/ETC-120028836, **as amended by Patton, Politis & White 2009**,
  *Correction to "Automatic Block-Length Selection for the Dependent Bootstrap"*,
  Econometric Reviews 28(4):372–375, doi:10.1080/07474930802459016. **Which
  formula to implement, stated so it cannot be resolved later by convenience:**
  the executing project implements the **corrected** formulae of Patton, Politis
  & White 2009 — never the 2004 formulae as originally printed — and, because
  §9.1 specifies a stationary bootstrap as primary, uses the **stationary-bootstrap
  optimal block length** as the primary quantity, with the circular-block variant
  reported only as the §9.1 sensitivity. Both papers are **cited by DOI and were
  NOT re-fetched in this drafting session**, in the same posture as the §13
  statistical instruments; verifying them at source is folded into pre-freeze
  checklist item 7. Data-driven, not chosen.
- **`purge` derivation:** `purge >= ` the §4 meta-label horizon upper bound,
  which is the empirical settlement-completion quantile. Because §5.3 leaves that
  horizon unbounded above at source, the purge must be derived from measurement
  and its **right-censoring must be reported**, not silently truncated.
- **If CPCV: `n_groups`, `n_test_groups`, selection rationale:** not applicable;
  CPCV is not used.

---

## 3. Null constructions (surrogates)

> Section numbering note: the 11-section template places surrogates nowhere, and
> ADR-0003 makes them mandatory ("its null, its statistic, its **surrogate**, its
> aggregation rule, its refutation condition"). They are inserted here as §3.1
> and §3.2 and cross-referenced from §§1, 5, 8 and 9. This is the one structural
> deviation from the template's section order, recorded rather than silent.

**Both surrogates are required. Neither alone is sufficient**, because they
absorb different alternatives: the quantisation null absorbs apparent violations
that are artifacts of the price grid and the fee rounding, and the staleness null
absorbs apparent violations that are artifacts of rungs being observed at
different effective times.

### 3.1 Quantisation null

**Claim being nulled:** an apparent violation no larger than one tick plus the
observed spread plus the fee-rounding residual is **not distinguishable from
coherence**.

**Surrogate construction, specified to implement:**

1. Take the observed ladder snapshot `(p[i,s,d](t), A[i,s,d](t))` for `i = 1…n`.
2. Compute, per rung, the **coherence-consistent interval** implied by nesting:
   the set of prices for rung `i` consistent with a monotone-decreasing price
   vector given the *other* rungs' observed touches. Project the observed touch
   onto that interval, giving a coherent reference ladder `p_coh`.
3. Re-quantise `p_coh` onto the venue's tick grid by an independent draw per rung
   per side: `p_surr[i,s,d] = tau · round( p_coh[i,s,d] / tau + u )` with
   `u ~ Uniform(-1/2, +1/2)` drawn independently across rungs and sides. This
   reproduces the fact that a coherent latent price is only ever *displayable* to
   the nearest tick (`d21-c3`).
4. Re-impose the observed per-rung half-spread, so the surrogate's bid/ask
   geometry matches the real one rung by rung.
5. Recompute `T` on the surrogate ladder with the identical fee, rounding and
   collateral machinery — including `ceil_g` at the member's own `g` (`d08-c1`,
   `d08-c2`) — and identical depth constraints `A[i,s,d](t)`.
6. Repeat `B_quant` times (`B_quant` `TO COMPUTE`, §5.1) to obtain the null
   ensemble `{T_surr}`.

**What it preserves:** ladder membership, nesting direction, per-rung spread,
per-rung depth, the fee function, the rounding granularity, the tick.
**What it destroys:** any sub-tick price information, which is exactly the
information the P-NOISE prediction says is spurious.

**Charter §"Gate on `construct`" conditions, discharged in advance:**
- (i) *named surrogate preserving known non-construct properties* — steps 1–4.
- (ii) *equivalence test against a pre-registered bound* — §9.2's `delta` is that
  bound, and the test against it is an equivalence test, not a failed difference
  test.
- (iii) **Positive control, required:** inject a synthetic monotonicity violation
  of magnitude exactly `delta` at the smallest depth of interest into a *coherent*
  ladder and confirm `T` recovers it. If the statistic cannot recover an injected
  violation at `delta`, no null result may be reported at all.
- (iv) *explicit scope* — nested cumulative ladders only, at the registered
  series, at the registered snapshot resolution, at both values of `g`; a null on
  this class is **silent** about mutually exclusive fields (KSL-C02) and about
  cross-venue relations (KSL-C05, KSL-C13).
- (v) **Negative control on the surrogate itself, required:** confirm by the same
  statistic that the surrogate ensemble does **not** exhibit systematic `T > 0`.
  The charter's stated hazard applies directly here: a surrogate that absorbs the
  alternative *"shrinks the real-vs-surrogate point estimate toward zero without
  inflating its standard error, so TOST rejects and licenses `construct-negative`
  precisely when the null was mis-specified."* Step 2's projection onto a coherent
  reference is exactly the kind of step that could absorb the alternative, which
  is why (v) is not optional.

### 3.2 Staleness null

**Claim being nulled:** an apparent violation arises when one rung's quote is
**stale relative to another's** — the rungs are observed at the same wall-clock
instant but reflect different information times.

**Surrogate construction, specified to implement:**

1. **Measure the staleness distribution per rung.** From the snapshot stream,
   compute for each rung `i` the empirical distribution `Lambda_i` of quote age
   at observation: the elapsed time between `t` and the last change of that
   rung's touch. `Lambda_i` is *measured*, never assumed, and is reported as part
   of the result. This is the input the design cannot proceed without (§3
   feature `quote_age@0.1.0`).
2. **Time-shift each rung independently, within its own observed distribution.**
   For each surrogate replicate and each rung `i` independently, draw
   `lambda_i ~ Lambda_i` and replace rung `i`'s quote at `t` by **the quote that
   rung actually displayed at `t − lambda_i`**, taken from that same rung's own
   realised quote path.
3. **Marginal preservation is by construction.** Because every surrogate value of
   rung `i` is drawn from rung `i`'s own realised quote path, and the shift
   distribution is rung `i`'s own measured `Lambda_i`, each rung's marginal price
   distribution is preserved up to the sampling error of the shift. What is
   randomised is **only the relative alignment of rungs** — which is precisely
   the quantity the staleness alternative implicates. Report the achieved
   marginal-preservation check (per-rung two-sample comparison of surrogate
   against observed marginals) as a validity condition of the surrogate; if it
   fails, the surrogate is mis-specified and the result is withheld.
4. Recompute `T` with the identical fee, rounding, depth and collateral
   machinery. Repeat `B_stale` times.

**Declared transfer.** The construction is the surrogate-data method of Theiler
et al. 1992 (cited in the charter §"Falsification of commitment 1" as the
project's only operational procedure), adapted from randomising phase in a single
time series to randomising *relative observation time across rungs of a
cross-sectional ladder*. **That adaptation is not licensed by the source and is
declared here as a transfer**, per charter commitment 5. The charter itself notes
that surrogate-data testing is *"a time-series technique with no cross-sectional
analogue"* — this construction is a candidate analogue and must be reviewed as
one, not assumed to inherit the original's guarantees.

**Charter gate conditions (iii) and (v) apply identically** and are not restated:
the positive control injects a violation into a *synchronously observed* ladder,
and the negative control confirms the staleness surrogate does not itself
manufacture `T > 0`.

### 3.3 Joint use

The two ensembles are combined, not chosen between. A triple is a candidate
violation only if `T` lies outside **both** ensembles at the registered level.
The combination rule (independent thresholds vs a joint ensemble built by
composing both perturbations) is `TO COMPUTE` — selection procedure: pre-register
the composed ensemble as primary and the two independent ensembles as
sensitivity, and report both.

---

## 7. Cost model

- **`cost_model_id`:** `kalshi_ladder_pit_v0` — **registered in the executing
  project's cost-model package, not here.** ADR-0003 makes registration of a
  runnable cost model out of scope for castles; this document specifies its
  required content.
- **Commission schedule source:** `ks-vr-d01`, *Trading Fees [Kalshi Exchange Fee
  Schedule]*, `https://kalshi.com/docs/kalshi-fee-schedule.pdf`, retrieved
  2026-09-04, retrieved-bytes SHA-256
  `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601`, effective
  date `QUOTED` *"Last updated and effective: July 7, 2026"*. Plus `ks-vr-d08`
  (*Fee Rounding*, SHA-256
  `7591cf0fb277eaf8fac8aedaf1645e58b61dacb22b5fed20ba7d8ea9f76ffa22`) for the
  rounding mechanics. **Both are the schedule as of the retrieval date only** —
  §8 forbids applying them across a historical window.
- **Slippage model version:** none, and the omission is deliberate and stated. `T`
  is defined on executable touch prices at the displayed size (§1.4 constraint
  (a)), so within-touch slippage is zero by construction. Slippage *beyond* the
  touch is excluded by refusing to size beyond it. What remains — the risk that
  the touch moves between observation and arrival — is handled by the staleness
  surrogate (§3.2) and by the persistence requirement `m` (§9.3), not by a
  slippage coefficient.
- **What the cost model must additionally carry, from §5:** the role-reassignment
  branch (`d18-c2`), the batch-rejection branch (`d06-c8`), the per-strike
  accountability vector (`d21-c2`), and the collateral term with its unbounded
  horizon (`d14-c2`, §5.3).

---

## 8. Point-in-time discipline, and gate thresholds

### 8.1 Point-in-time discipline (this is a leakage section, not a housekeeping one)

**The fee schedule, the tick and the rule set applied at time `t` must be the
ones in force at `t`.** Applying one current fee schedule across a historical
window is **look-ahead**, and the venue documents say exactly why.

- `d22-c1` (QUOTED, 17 CFR Part 40): *"( 3 ) The Commission has received the
  submission not later than the open of business on the business day that is 10
  business days prior to the registered entity's implementation of the rule or
  rule amendment."* The clause's own `what_it_constrains` field states the
  consequence: *"THE CHANGE-LATENCY BOUND. Every fee change, position-limit
  change, market-maker programme and block-trade threshold reaching this arm
  arrived by this route, so the minimum public notice on any of these
  executability preconditions is ten business days - and equally, **no such
  precondition is stable beyond that horizon**."*
- `d22-c3` (QUOTED): product listings require only **one** business day's notice.
- `d18-c1` (QUOTED): *"pursuant to Regulation 40.6(a), it is self-certifying an
  amendment to its Exchange Fee Schedule"* — fee terms change **by
  self-certification, not by approval**.
- `d18-c2`'s own filing carries an effective date (`d18` `effective_date_verbatim`,
  QUOTED): *"This amendment or any subpart thereof shall become effective upon
  exchange notice, but in any event not prior to the close of business July 24,
  2026 - ten (10) business days after the filing of this submission with the
  CFTC."*
- `d01-c11` (QUOTED): *"Please refer to https://kalshi.com/fee-schedule for
  scheduled upcoming fee changes."* — and the venue arm retrieved that URL
  (`KS-VR-Q18`) and *"found client-rendered with no fee text in the bytes."*
- `d02-c3` (QUOTED, Member Agreement): *"This Agreement may be amended
  unilaterally by Kalshi upon notice to You."*

**The leakage argument, stated plainly.** The schedule at `ks-vr-d01` is
effective 2026-07-07. Applying it to a snapshot at `t < 2026-07-07` uses a cost
function that **was not knowable at `t`** and that a participant at `t` could not
have faced. If the newer schedule is cheaper, `T` is inflated for the whole
pre-change window; if dearer, deflated. Either way the sign of the bias is
constant within a window and correlated with time, which is the textbook leakage
failure that `REVIEW.md` blocking directive 1 exists to stop. The formal
treatment is Kaufman, Rosset, Perlich & Stitelman 2012 (charter commitment 4),
and it applies here without modification: *every feature must be computable at
time `t` using only data available at time `t`* — and the fee schedule **is** a
feature (§3, `fee_schedule_in_force@0.1.0`).

**Required reconstruction, and the blocker in it.** The executing project must
reconstruct the schedule, the tick and the rule set in force at each `t` from the
filing register — the venue arm enumerated **111 KEX rule filings** (query
`KS-VR-Q32`) and retrieved five — and must record which filing governs each
snapshot. **This reconstruction is currently incomplete at source and that is a
stated blocker, not a caveat:** the venue arm's own document-class note reads
*"THE RULEBOOK IN FORCE ON 2026-09-04 WAS NOT LOCATED AT THE ENDPOINTS SEARCHED
ON THIS DATE"*, and `d18-c4`'s notice channel (`kalshi.com/regulatory/notices`)
was retrieved (`KS-VR-Q48`) and found *"client-rendered with no notice text in
the retrieved bytes, so the channel is NOT machine-readable by unauthenticated
HTTP fetch."*

**Consequence for the splitter:** window boundaries in §2 are aligned to
effective dates so that no train/validation/test window straddles a cost-function
change. This constraint is fixed here, before data.

### 8.2 Gate thresholds

- **`alpha`:** `TO COMPUTE`. If no derivation is available in the executing
  project, it is recorded `CONVENTION` **with its provenance stated**, per charter
  commitment 3. This design does **not** name a value.
- **`bh_threshold` (BH-FDR threshold):** **deliberately not used, and the refusal
  is the substantive choice.** H1 is an existence claim, and ADR-0003 §"Consequence
  for the multiple-testing convention" states that existence claims *"are union
  alternatives and require family-wise error control across the registered family
  — White's Reality Check or Hansen's SPA, which respect the dependence among
  members."* FDR control would be the correct instrument for an absence claim or a
  discovery-set claim; it is the wrong instrument here and substituting it would
  weaken the guarantee H1 needs. Recorded as a declined default with a reason, not
  as an unset field.
- **`dsr_activation_size` (Deflated Sharpe Ratio activation):** not applicable.
  **No Sharpe ratio is computed anywhere in this design**, because ADR-0003 and
  ADR-0004 forbid this repository from stating an expected return, and `T` is a
  worst-case payoff rather than a return series. `rules/quant-project.md`
  §Inference's Sharpe-CI directive is therefore **not vacuously satisfied — it is
  conditionally deferred**: *if* the executing project converts `T` into a
  realised return series, then a bootstrap CI on Sharpe is required, using Opdyke
  2007 or Lo 2002 for a single strategy and Ledoit & Wolf 2008 for pairwise
  comparison, per the rule file adopted in ADR-0004. That conditional obligation
  is registered here so a future stage cannot inherit a green check it never
  earned (ADR-0004 §"Alternatives considered", third bullet).
- **Power target:** `TO COMPUTE`, and it is **mandatory**. Charter step 2: *"MDES
  is undefined without the power target; the target is itself a `CONVENTION`
  requiring provenance under commitment 3."* See §9.4.

---

## 9. Aggregation, refutation, stopping, MDES

### 9.1 Aggregation rule and the registered family

**The family is `(series × rung-subset × snapshot)`.** Every registered triple is
one member. The rung-subset dimension includes all adjacent rung-pairs (the
direct KSL-C01 monotonicity test) and the full-ladder subset; whether
non-adjacent pairs and intermediate subsets are members is a **registration
decision that must be made before the first test**, because including them
multiplies the family size and cannot be recovered afterwards.

**This is an existence claim and it requires family-wise control.** ADR-0003,
quoted in §8.2. Under `rules/quant-project.md` §Inference as adopted by ADR-0004:

- **Primary: Hansen's SPA** (Hansen 2005), applied over the registered family
  with a **stationary bootstrap** whose block length is `TO COMPUTE` by the
  **Politis–White automatic procedure** — Politis & White 2004
  (doi:10.1081/ETC-120028836) **as amended by Patton, Politis & White 2009**
  (doi:10.1080/07474930802459016) — the same estimator §6 uses for the embargo,
  and implemented from the **corrected 2009 formulae**, taking the
  **stationary-bootstrap** optimal block length here because the primary
  resampler is the stationary bootstrap. Where the circular block bootstrap is
  run as the sensitivity below, the **circular-block** optimal block length of
  the same corrected paper is used for it; the two are not interchangeable and
  the executing project reports which it used for which resampler. Neither paper
  was re-fetched in this drafting session (§13).
- **Pre-registered sensitivity: White's Reality Check** (White 2000), on the
  identical family and the identical bootstrap. Reporting only whichever is more
  favourable is prohibited; both are reported.
- For any time-series mean or regression of `T` on snapshot time, standard errors
  are **Newey–West HAC with a data-dependent bandwidth** (Newey & West 1994) or
  the Andrews 1991 parametric plug-in, per the adopted rule file. A fixed
  hand-chosen lag is prohibited.

**Registration precedence, stated as a hard rule.** The family — the series list,
the rung-subset rule, the snapshot grid, and the count of members — **must be
written down and its digest recorded before the first test statistic is
computed.** ADR-0003 §"Consequence for the multiple-testing convention" makes the
reason explicit for the analogous cross-instrument case: *"Cross-instrument
structure must be declared before data is examined. Four instruments are either
four members of one family … or a replication design … These are different tests
and the choice is not recoverable after the fact."* The same applies to the
series dimension here: **multiple ladder series are members of ONE family, not a
replication design.** That choice is made here, in advance, and may not be
revisited.

**The denominator is contingent on universe construction.** KSL-C30 (§2) means a
family enumerated from the raw markets feed would be dominated by synthetic
combination markets; the family-wise correction would then be computed over a
denominator that includes instruments the statistic cannot be executed on. The
registered family is built from filed terms and conditions, and the retained-vs-raw
counts are reported.

### 9.2 Refutation condition — a magnitude and a frequency, pre-committed

**H0 is refuted only if all four hold simultaneously:**

1. **Magnitude.** `T >= delta` on the qualifying triples, where
   `delta` is `TO COMPUTE` — selection procedure: `delta = max(` one tick `tau`
   for the series (`d21-c3`), the member's rounding granularity `g` (`d08-c1`),
   the §1.6 break-even bar **recomputed at the price band of the triple** from
   `d01-c2` with the in-force multiplier and the measured spread distribution `)`.
   `delta` is a **smallest-effect-size-of-interest**, pre-registered, and is the
   bound in the equivalence test of §3.1 gate (ii).

   **Sanity reference, re-registered against the source's own TAIL figure.** The
   comparison reference is `QUOTED 2.6¢` — `ks-sc-002`'s *"Even at the tails the
   hurdle is 2.6¢."* (§1.6(ii)) — and **not** the mid-range `QUOTED 10.7¢` that
   an earlier state of this item named. The mid-range figure is the wrong
   comparator for a hypothesis that lives in the tail (§1.5), and registering a
   ceiling against it would have admitted a recomputed tail `delta` several times
   the source's own tail statement without raising anything.

   **What the reference does and does not license, stated because the obvious
   justification does not hold.** `2.6¢` is **NOT ADOPTABLE** (§0.2, §1.6(ii)):
   it is stated at README depth with no derivation, it does not say at which
   prices "the tails" begin, and it is a round-trip figure while `T` is
   hold-to-settlement. It therefore **never sets, caps, replaces or bounds
   `delta`**. Its sole registered use: if the independently recomputed tail
   `delta` exceeds it, that disagreement is a **mandatory review trigger** — the
   recomputation is re-derived and the discrepancy reported — and it is **not**,
   by itself, evidence of an arithmetic error. The earlier item claimed such a
   ceiling was justified because "the fee is monotonically smaller away from
   `P = 0.5`". **That justification is withdrawn as insufficient**: `d01-c2` makes
   only the *fee* term monotone in `|P − 0.5|`, whereas the round-trip bar is
   fee **plus spread**, and the sole statement in the corpus about the spread's
   shape is `ks-sc-002`'s own unquantified *"a spread that is also widest
   mid-range"*, with no tail spread distribution measured at the depth read. Fee
   monotonicity alone therefore supports only this: **the fee component of a tail
   bar is no larger than its mid-range value.** It supports nothing about the
   spread component, so the ordering of the *total* round-trip bar between
   mid-range and tail is not established, and a recomputed tail `delta` above the
   reference is as consistent with a wider-than-assumed tail spread as with an
   arithmetic mistake. The review must distinguish the two before either is
   asserted.
2. **Frequency.** The exceedance rate across the registered family is at least
   `phi`, `TO COMPUTE` — selection procedure: `phi` is set at the upper `1 −
   alpha` quantile of the exceedance rate under the **joint** surrogate ensemble
   of §3.3, plus a margin of the Monte-Carlo standard error of that quantile. It
   is therefore a *measured* null exceedance rate, not a chosen fraction.
3. **Persistence.** The exceedance holds on at least `m` consecutive snapshots,
   `m` `TO COMPUTE` — selection procedure: the smallest integer such that
   `m × (snapshot interval)` exceeds the upper quantile of the measured
   order-submission-to-acknowledgement latency at the entry tier (`d06-c4`),
   inflated by the unobservable backoff of `d06-c9`. This exists because KSL-C01
   states the phenomenon *"gets corrected fast"*, and a violation shorter than the
   time to submit against it is not a violation of *executability*.
4. **Family-wise significance.** Hansen SPA rejects at the registered `alpha` over
   the registered family, with White's Reality Check reported alongside (§9.1).

**A p-value alone never refutes H0.** Items 1–3 are magnitude and frequency
conditions and are checked independently of item 4. Conversely, items 1–3 without
item 4 do not refute H0 either.

**And the §1.5 discriminating rule sits on top of all four:** even a refutation
satisfying 1–4 is recorded as `undetermined` rather than as a positive unless it
survives at the coarse granularity, at the displayed depth, and outside both
surrogate ensembles.

### 9.3 Stopping rule

- **Stop criterion:** a **calendar-time budget fixed at registration**, with a
  **futility check** against the pre-registered `n_required` from the MDES
  computation (§9.4). No "keep collecting until `T` crosses something". No
  interim look that could alter the family.
- **Max folds:** the number of walk-forward folds implied by the registered
  window boundaries in §2; fixed at registration.
- **Max wall-clock budget:** `TO COMPUTE` by the executing project, recorded
  there. Data collection ends at the earlier of the calendar bound and the
  futility trigger.

### 9.4 MDES — computed pre-data, never retrospective power

**Retrospective power is never computed** (charter §"Negative-result protocol"
step 2; Hoenig & Heisey 2001: post-hoc power is a monotone transform of the
observed p-value and carries no information beyond it). The **minimum detectable
effect size** is computed instead, **before data**.

- **Quantity:** the smallest `delta_MDES` — in cents of worst-case net payoff per
  contract — that the §9.2 procedure would detect with probability at least
  `gamma`, at level `alpha`, over a family of `N` registered triples with the
  dependence structure the block bootstrap estimates.
- **Selection procedure (named, as required):** **simulation against the surrogate
  ensembles of §3**, not a closed-form formula. Inject a violation of magnitude
  `d` into a coherent ladder at the displayed depth (the §3.1(iii) positive
  control, run across a grid of `d`), pass it through the identical statistic,
  surrogates and SPA pipeline, and take `delta_MDES` as the smallest `d` at which
  the empirical detection rate reaches `gamma`. A closed form is unavailable
  because `T` is a max-min of a rounded, integer-constrained objective and has no
  tractable sampling distribution.
- **`gamma` (target detection probability):** `TO COMPUTE`; if no derivation is
  available it is recorded `CONVENTION` with its provenance. Charter step 2 makes
  the target mandatory and makes its provenance mandatory.
- **`N`:** determined by the registered family (§9.1).
- **Comparator, sourced not judged (charter step 2):** the comparator for
  `delta_MDES` is the §9.2 `delta` — itself built from `QUOTED` venue quantities
  (`tau`, `g`) and the §1.6 break-even construction **recomputed at the price
  band** from `d01-c2`, with the source's own tail figure `QUOTED 2.6¢` entering
  only as the §9.2 item 1 review trigger and never as a value. If
  `delta_MDES > delta`, **the design cannot resolve the effect it was built to
  find and the correct disposition is `archived(null, underpowered)` before any
  data is collected** (§11), not after.
- **Directionality caveat (charter step 2):** a tight MDES licenses an
  informative-null reading **only where the target is identified by the design**.
  Here the target is a worst-case payoff computed from observable executable
  quantities under a documented cost function, so identification rests on the
  fidelity of the cost function rather than on confounding control — which is why
  §1.3's four qualifications and §8.1's unlocated rulebook are the binding
  identification risks, not omitted covariates.

**No MDES value is stated in this document. Computing it is the executing
project's work (ADR-0003).**

---

## 10. Data requirements, and what castles does not acquire

**castles acquires NONE of the following** (ADR-0003). This section states what an
executing project would have to obtain, and — from the venue arm — which of it is
published and which is withheld or unreachable.

| Requirement | State in the corpus | Locator |
|---|---|---|
| Order-book snapshots with timestamps at a stated resolution | Public market data is unauthenticated-readable; **read throughput is metered**. The only observed collection resolution anywhere in the corpus is a practitioner's *"roughly every 42 seconds"* — recorded, **not adopted** (§2) | `d03-c1`, `d06-c1`–`d06-c3`, `ks-sc-002` |
| Displayed size at the touch, per rung per side | Stated to be available on the public market-data surface (order books, depth) | `d03-c1`; `ks-sc-002` records *"top-of-book quotes, sizes, and depth"* |
| Ladder membership and the mutual-exclusivity flag | Membership is derivable from filed terms and conditions. **The exclusivity flag is a PRACTITIONER claim (KSL-C02) with NO S-D clause in `ks-venue-docs.json`** — unverified at venue depth | `d22-c4`; KSL-C02 |
| Per-series fee multiplier `M` | **Published but not extractable at the depth reached.** The table exists in the schedule; its *"Column alignment … is DESTROYED by text extraction … so NO cell value is quoted"* | `d01-c3`, `d01-c5`, `ks-vr-d01.tables_not_quoted` |
| The member's own rounding granularity `g` | **Published and clean** | `d08-c1` |
| Minimum tick and settlement value per series | **Published per series in filed T&Cs; retrieved for ONE series only** — a sampled retrieval, not an enumeration | `d21-c3`, `d21-c4`, class-2 note |
| The rule set in force at each historical `t` | **NOT LOCATED.** *"THE RULEBOOK IN FORCE ON 2026-09-04 WAS NOT LOCATED AT THE ENDPOINTS SEARCHED ON THIS DATE."* Amendments are individually retrievable (111 KEX filings enumerated, 5 retrieved) | class-1 note, `KS-VR-Q32` |
| Pending fee changes | **Unreachable.** The pointer URL is client-rendered with no fee text in the bytes | `d01-c11`, `KS-VR-Q18` |
| Regulatory change notices | **Unreachable by unauthenticated HTTP.** *"client-rendered with no notice text in the retrieved bytes"* | `d18-c4`, `KS-VR-Q48` |
| Which series carry a position limit above the general one | **WITHHELD.** *"appendix A is confidential and submitted under a request for confidential FOIA treatment"* | `d16-c5` |
| Reportable position levels | **WITHHELD.** *"communicated to FCM members"*, not published | `d13-c4` |
| Market-maker obligation values (max spread, min size, min uptime, coverage) | **NAMED but NO VALUE STATED**; selection procedure in a confidential appendix; entry runs through a Market Maker Agreement that *"is not a published document and was not located"* | `d19-c5`, `d19-c3`, `d19-c1` |
| Settlement-source operating detail | **WITHHELD.** *"A ppendix E (Confidential) - Source Agency"* | `d21-c11` |

**Why the withheld items matter to *this* hypothesis and are not generic
grumbling:** `M` enters the fee term of `T` directly (§1.4) and is the reason
`p*` cannot be evaluated (§1.5); the unlocated in-force rulebook is the reason
§8.1's point-in-time reconstruction is currently blocked; and the unpublished
market-maker obligations mean the competitive floor a laddered order set would
face at the touch is not determinable from any public document (`d02-c1`
states market makers may receive fee discounts, rebates, disconnect-cancel
protection and *"GREATER THROUGHPUT"*, and that *"A cost or fill-rate figure
built from the public fee schedule and the public rate-limit tiers is therefore
an upper bound on a non-market-maker's competitiveness"*).

---

## 11. Decision rule

Null results stay in the register per the non-loss policy and are appended to
[failure_log.md](../../../failure_log.md) with a pointer to an autopsy document
(charter §"Negative-result protocol" step 5).

- **If refuted (all four §9.2 conditions AND the §1.5 discriminating rule):**
  `archived(positive)` **for the specification only.** The `promoted` status is
  **inert in this repository** (ADR-0003 §Consequences: *"`config/instruments/`,
  `logs/promotions/`, and the `promoted` status in `hypothesis_backlog.md` all
  presuppose an execution pipeline … they should not be populated"*). There is no
  paper-trade eligibility list here and none is created.
- **If §9.2 conditions 1–3 hold but SPA fails:** `archived(null)` with a
  multiple-testing note naming the family size and the block-bootstrap block
  length.
- **If `T` lies inside either surrogate ensemble:** `archived(null)` with the
  layer recorded as `data` or `precision` per the charter's step-3 procedure —
  and **only** if the §3 positive control (iii) succeeded and the negative control
  (v) held. If either control failed, the layer is `undetermined` and no null is
  claimed.
- **If the §1.5 discriminating rule is satisfied on two of three perturbations:**
  `undetermined`. Not a partial confirmation, not a trend.
- **If realised `N` < the pre-registered `n_required` from §9.4, or if
  `delta_MDES > delta`:** `archived(null, underpowered)` — and if this is known
  before collection, the correct action is not to collect.
- **In every branch:** the failure-taxonomy term and its layer are recorded from
  the charter's mapping table, and the transferable-positive field is filled,
  including *"none found"* where none exists (charter step 4, which requires the
  negative entry).

---

## 12. Reproducibility commitments

Per `~/.claude/CLAUDE.md` §Reproducibility, `CLAUDE.md` §"Reproducibility
contract", and the R1-A ReproLog schema. **castles produces no run, so these
fields have no trigger here** (ADR-0003 §Consequences: the contract *"remains
correct for the executing project and dormant for this one"*). They are stated so
the executing project inherits them.

- **git HEAD (at run):** auto-populated by the executing project.
- **`uv pip freeze` sha (at run, 64-hex):** auto-populated.
- **RNG seed:** `TO COMPUTE` — pre-registered by the executing project before the
  first surrogate replicate and never modified post-hoc. Used by `B_quant`,
  `B_stale`, the block bootstrap, and the MDES simulation; each stream is seeded
  separately and each seed is recorded.
- **Dataset checksums:** none. `data/_manifest.json` in this repository contains
  no market data and will not.
- **Reproducibility log path:** `logs/reproducibility/repro_log_<run_id>.json` —
  **in the executing project.** No ReproLog is emitted for this draft; drafting an
  unfrozen specification produces no artifact-bearing run, and emitting one would
  imply a freeze that has not occurred.
- **Design.md SHA at freeze:** **NOT COMPUTED. This document is not frozen.** Its
  SHA-256 is not a registration hash. `/preregister` has not been run and must not
  be run until every item of the checklist below is discharged (front matter
  `freeze_status`).

### Pre-freeze checklist — what must be true before `/preregister` may run

1. **DISCHARGED 2026-09-04.**
   `docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` exists
   and is the compiled corpus record. Its existence was verified by directory
   listing during the 2026-09-04 remediation pass; the front matter and
   `hypothesis_backlog.md` previously asserted the opposite and both have been
   corrected. **Residual obligation, carried into item 7:** its SHA-256 is not
   yet recorded, so *which bytes* of the corpus record this design was frozen
   against would not be reconstructible.
2. **OPEN.** The academic arm has completed stage-1 screening, and `ks-a-057`
   (arXiv:2608.00666, *"Executable Arbitrage and Market Efficiency in Prediction
   Markets"*) has a disposition. If included, §1 and §1.6 are revised first.
3. **OPEN.** The mutual-exclusivity flag (KSL-C02) is either confirmed by an S-D
   clause or the design's dependence on it is removed.
4. **OPEN.** The per-series fee multiplier table (`ks-vr-d01`) is extracted, or
   `M` is sourced from filings, so that `p*` in §1.5 is computable.
5. **OPEN.** The rulebook in force is located, or §8.1's point-in-time
   reconstruction is re-specified around its absence and that limitation is
   elevated into §1.
6. **OPEN.** The venue clauses are **re-retrieved and re-digested**; the arm's own
   `retrieval_date_warning` states that *"a re-retrieval that digests differently
   is a changed document, not a confirmation."*
7. **OPEN — read-time digest discipline (added 2026-09-04).** A SHA-256 is
   recorded for the corpus record and for each of the five arm files named in the
   front matter, beside the read date of the state this design quotes; the two
   `ks-sc-001` sentences and the one `ks-sc-002` sentence named in §1.6 are
   re-verified at byte depth with a recomputed README digest; and the two
   Politis–White references named in §6 and §9.1 are fetched at source rather
   than carried by DOI alone. **Items 2–7 are the operative reason this design
   remains `draft-unfrozen`.**

---

## 13. References

**Venue and regulator documents** — all cited by clause id into
`docs/literature/search_logs/kalshi-strategy-multivocal/ks-venue-docs.json`,
retrieval date **2026-09-04**, each record carrying its URL, HTTP status and a
SHA-256 of the retrieved bytes. Clauses used here: `d01-c1`, `d01-c2`, `d01-c3`,
`d01-c4`, `d01-c5`, `d01-c6`, `d01-c8`, `d01-c11`; `d02-c1`, `d02-c3`; `d03-c1`,
`d03-c3`; `d06-c1`, `d06-c2`, `d06-c4`, `d06-c5`, `d06-c6`, `d06-c7`, `d06-c8`,
`d06-c9`; `d07-c1`, `d07-c2`, `d07-c3`; `d08-c1`, `d08-c2`, `d08-c3`, `d08-c4`;
`d10-c1`, `d10-c2`; `d13-c2`, `d13-c3`, `d13-c4`; `d14-c2`, `d14-c3`; `d16-c5`;
`d17-c2`, `d17-c3`, `d17-c4`, `d17-c5`, `d17-c6`, `d17-c7`, `d17-c8`, `d17-c9`;
`d18-c1`, `d18-c2`, `d18-c3`, `d18-c4`; `d19-c1`, `d19-c3`, `d19-c5`; `d21-c2`,
`d21-c3`, `d21-c4`, `d21-c9`, `d21-c10`, `d21-c11`; `d22-c1`, `d22-c3`, `d22-c4`;
`d23-c1`. **No DOI is asserted for any of these and none exists.** Quotations
from `ks-vr-d13`, `ks-vr-d17` and `ks-vr-d21` are transcribed with their
extraction artifacts intact per that file's `quotation_discipline` and **must
never be re-quoted as clean rule text.**

**Practitioner (grey) records** — `ks-lateral-records.json`, execution date
2026-09-04, each carrying source URL, HTTP status, SHA-256 and a mechanically
verified verbatim quotation. Classes used: **KSL-C01** (nested-strike
monotonicity), **KSL-C02** (field-sum coherence and the exclusivity-flag gate;
cited as a *contrast*, since H001 is nested and not mutually exclusive),
**KSL-C03** (fee-curvature confinement to the longshot tail), **KSL-C04**
(round-up fee quantisation), **KSL-C07** and **KSL-C08** (collateral return;
netting — both referred for S-D re-verification), **KSL-C13** (rung differencing;
its 2%/3%/5%/6% figures **not adopted**), **KSL-C30** (auto-generated combination
markets), **KSL-C31** (token-bucket tiers), **KSL-C32** (disputed/amended market
states). Classes **KSL-C10**, **KSL-C19** and **KSL-C28** are named **only** to
record that their numeric thresholds are **not adoptable and are not used**
(§0.2). All are S-E commercial or vendor sources; per the arm's
`credibility_recording_constraint`, **no tier, band or rank is assigned** to any
of them, and outlet control and expertise are recorded as continuous attributes
following Adams, Smart & Huff 2017 (doi:10.1111/ijmr.12102), a **declared
transfer** from management and organizational studies.

**Software records** — `ks-github-records.jsonl`, access date 2026-09-04.
**`ks-sc-001`** `github.com/sudo-ai-git/kalshi-backtest` @
`c32b700111a321db16a8cfae5eceaab0ea167dd8`, README SHA-256
`50293b496c265abb368eee1bead288beafb437d565a2088ec5aa533a8ef76118`.
**`ks-sc-002`** `github.com/himagna16/kalshi-microstructure` @
`817fe37ceb184bd649b71d0dbebb4a8e5718bb59`, README SHA-256
`753d94ddd29ee97929fa4d483420e105aeee602f34f610d69ec65b4bb7668462`, MIT.
Both are self-published repositories with no external moderation; both README
records carry `F11_attribution_status` gaps (the *"favorite–longshot bias"* label
is used in each without a citation to its originating literature) and **this
design does not restate that label as established on their authority.**
**Two findings against this arm log are registered in §1.6** — the `ks-sc-001`
extraction is incomplete (two README sentences absent from every field) and the
`ks-sc-002` extraction is truncated (the immediately following tail-hurdle
sentence absent). Both were established by **re-fetching the pinned raw README
URLs on 2026-09-04**, in converted-text form; **neither README digest above was
recomputed at that re-fetch**, and the digests shown remain the arm log's. The
arm log itself is **not edited by this design**.

**Academic records** — `ks-academic-identified-universe.json`. **`ks-a-057`**,
*"Executable Arbitrage and Market Efficiency in Prediction Markets"*,
arXiv:2608.00666 (2026), from query `ks-arxiv-07`: **identified, eligibility not
assessed, PROVISIONAL** (§0.3). No academic record is load-bearing.

**Methodological instruments verified before protocol freeze** —
`ks-instrument-verification.json`, all at abstract or metadata depth with the
environment gap declared there: PRISMA-S (doi:10.1186/s13643-020-01542-z) with
its explicit all-fields self-endorsement; PRISMA 2020 (doi:10.1136/bmj.n71),
**not claimed** for this corpus; Arksey & O'Malley 2005
(doi:10.1080/1364557032000119616) as the domain-neutral scoping framework; Adams,
Smart & Huff 2017 (doi:10.1111/ijmr.12102); Garousi, Felderer & Mäntylä 2019
(doi:10.1016/j.infsof.2018.09.006), a declared transfer out of software
engineering; Kalliamvakou et al. (doi:10.1145/2597073.2597074,
doi:10.1007/s10664-015-9393-5); Munaiah et al. (doi:10.1007/s10664-017-9512-6);
Smith, Katz, Niemeyer & the FORCE11 Software Citation Working Group 2016
(doi:10.7717/peerj-cs.86); Klein et al. 2014 (doi:10.1371/journal.pone.0115253)
and Jones et al. 2016 (doi:10.1371/journal.pone.0167475) for content drift.

**Block-length selection for the dependent bootstrap (§6 embargo, §9.1 SPA /
Reality Check resampler)** — named here because §0.2 and §1.2's directive-8
statement require every named method to carry provenance, and an earlier state of
this document named the procedure in both sections with **no citation anywhere**:

- Politis, D. N., & White, H. (2004). *Automatic Block-Length Selection for the
  Dependent Bootstrap*. **Econometric Reviews** 23(1):53–70.
  doi:10.1081/ETC-120028836.
- Patton, A., Politis, D. N., & White, H. (2009). *Correction to "Automatic
  Block-Length Selection for the Dependent Bootstrap" by D. Politis and H.
  White*. **Econometric Reviews** 28(4):372–375. doi:10.1080/07474930802459016.

**Which to implement:** the **2009 corrected** formulae, never the 2004 formulae
as originally printed; the **stationary-bootstrap** optimal block length for the
primary §9.1 resampler, and the **circular-block** optimal block length wherever
a circular block bootstrap is run as sensitivity. **Neither record was re-fetched
in this drafting session** — both are cited by DOI in the same posture as the
statistical instruments below, and fetching them at source is pre-freeze
checklist item 7.

**Splitter machinery — purging, embargoing, triple-barrier labelling (§4 label
construction, §6 splitter)** — named here for the same directive-8 reason as the
block above: an earlier state of this document used the abbreviation "AFML" with
no bibliographic record anywhere, gave a wrong internal pointer for it, and named
`PurgedWalkForwardSplitter`, `purge` and `embargo` with no citation at all.

- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Hoboken,
  NJ: John Wiley & Sons. ISBN 978-1-119-48208-6. Cited at **§4** for the
  triple-barrier method (**§3.4**), and at **§6** for purging and embargoing
  (**§7.4**).

**This record was NOT re-fetched or re-opened in this drafting session** — it is
carried in the same posture as the statistical instruments below and the
Politis–White pair above: cited by publisher, edition and ISBN, **not
independently verified here**, with the section pointers taken from the work's own
chapter structure as this document's author records it and not from a page
consulted in this session. **No DOI is asserted.** Verifying the two section
pointers at source is folded into pre-freeze checklist item 7.

**Statistical instruments, adopted by explicit reference through
[ADR-0004](../../../docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md)
from `rules/quant-project.md` §Inference, cited as that rule file records them
and NOT independently re-verified in this drafting session** — flagged as such
rather than presented as verified: White 2000 reality check
(doi:10.1111/1468-0262.00152); Hansen 2005 SPA (doi:10.1198/073500105000000063);
Newey & West 1994 (doi:10.2307/2297912) and Andrews 1991 (doi:10.2307/2938229)
for HAC bandwidth; Opdyke 2007 (doi:10.1057/palgrave.jam.2250084), Lo 2002
(doi:10.2469/faj.v58.n4.2453) and Ledoit & Wolf 2008
(doi:10.1016/j.jempfin.2008.03.002) for the **conditionally deferred** Sharpe-CI
obligation of §8.2.

**Charter-cited instruments used directly here** — Hoenig & Heisey 2001
(doi:10.1198/000313001300339897), for the prohibition on retrospective power;
Theiler, Eubank, Longtin, Galdrikian & Farmer 1992
(doi:10.1016/0167-2789(92)90102-S), for surrogate-data testing, **applied as a
declared cross-sectional transfer** (§3.2); Kaufman, Rosset, Perlich & Stitelman
2012 (doi:10.1145/2382577.2382579), for the formal treatment of leakage (§8.1);
Lakens, Scheel & Isager 2018 (doi:10.1177/2515245918770963) and Schuirmann 1987
(doi:10.1007/BF01068419), for the SESOI and equivalence-testing basis of `delta`
(§9.2). Each is cited as the charter records it; none was re-fetched in this
drafting session.
