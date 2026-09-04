# Hypothesis backlog

Append-only register of research hypotheses for this project. Per
SKIE-Universe convention (verified via `gh api` 2026-05-15). New entries added
via [/hypothesis-new](https://github.com/s-koirala/dotfiles/tree/main/claude/commands/hypothesis-new.md)
(R3-1 — pending). Append-only: archived hypotheses retain their row with
`status: archived`.

## Status legend

**Register scope, stated because one entry below is new.** This legend is a
**cross-project convention register**, not a local field list: the tokens in it
are the SKIE-Universe statuses verified via `gh api` on 2026-05-15. A token added
here by one project is a **proposal against a shared register** until it is
ratified upstream, and is marked as such in its own row.

| Status | Meaning |
|---|---|
| `specified-unfrozen` | **PROPOSED 2026-09-04 BY THIS PROJECT. NOT RATIFIED. This token is NOT part of the verified SKIE-Universe status convention** and must not be treated as one, cited as one, or relied on by any other project until it is. A design document has been drafted against the 11-section pre-registration template and is complete enough to review, but it is **not frozen**: `/preregister` has not run, no ReproLog exists, and the design.md SHA-256 is therefore not a registration hash. This status exists because `designed` below asserts a freeze that has not happened, and no other status in this legend is true of a drafted-but-unfrozen design. **What would ratify it, and nothing less:** (1) the token is added to the upstream status legend carried by [/hypothesis-new](https://github.com/s-koirala/dotfiles/tree/main/claude/commands/hypothesis-new.md) in the `s-koirala/dotfiles` repository, and its presence there is re-verified by `gh api` exactly as the 2026-05-15 verification of the existing tokens was; and (2) an ADR under [docs/decisions/](docs/decisions/) records the register change, its motivation, and the projects affected. Until both hold, this row stays marked PROPOSED and the token's use is local to this file. |
| `designed` | Pre-registration frozen via /preregister (R3-2a); design.md SHA recorded |
| `validated` | validate-data PASS on input dataset |
| `powered` | power-analysis run; n meets registered effect-of-interest |
| `running` | walk-forward / fit in progress |
| `kpi-reported` | KPI report card emitted to reports/{HID}/ |
| `promoted` | passed multipletest-gate; deployed to production — **inert in this repository** per [ADR-0003](docs/decisions/ADR-0003-specification-not-execution.md) §Consequences; presupposes an execution pipeline castles does not have and must not be populated |
| `archived` | null result kept (no deletion per non-loss policy); see failure_log.md |

## Backlog

| HID | Tier | Title | Status | Mechanism citation | Notes |
|---|---|---|---|---|---|
| H001 | 3 | Intra-series coherence on Kalshi cumulative threshold ladders, tested as an executability question rather than a price question | `specified-unfrozen` | Ladder-nesting relation: KSL-C01 (+ corroborator) in `docs/literature/search_logs/kalshi-strategy-multivocal/ks-lateral-records.json`. Cost function: clauses `d01-c2`, `d01-c4`, `d01-c6`, `d08-c1`–`d08-c4`, `d21-c3`, `d21-c4` in `.../ks-venue-docs.json`, retrieved 2026-09-04. No DOI is asserted for any of these and none exists; the academic arm is provisional and no academic record is load-bearing. | Design: [research/01_hypothesis_register/H001/design.md](research/01_hypothesis_register/H001/design.md). **Status is NOT `designed`**: this file's own legend defines `designed` as "pre-registration frozen via /preregister; design.md SHA recorded", and none of that is true — `/preregister` has not run, no ReproLog was emitted, and no SHA is recorded, because the corpus record the design depends on (`docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md`) does not yet exist and freezing would register a design against uncompiled literature. `specified-unfrozen` is proposed above for exactly this state. Tier 3 justification: the claim is about the venue's own price-grid, fee and collateral substrate at one instant rather than about a mechanism with peer-reviewed support (Tier 1) or an economic mechanism derived from theory (Tier 2), and the academic arm has produced no screened, included study that could ground either. Pre-freeze checklist in §12 of the design. Branch: kalshi-arbitrage / prediction-market microstructure; governed by ADR-0003 and ADR-0004. — **CORRECTION 2026-09-04 (audit round 1, findings REV-1-4 / QUANT-1-6). The clause above beginning "because the corpus record the design depends on … does not yet exist" is FALSE and is retained only because this register is append-only.** `docs/literature/lit_review_kalshi-strategy-multivocal_2026-09-04.md` **EXISTS on disk**, verified by directory listing on 2026-09-04; it is a deliverable of the same session that drafted the design. Pre-freeze checklist item 1 in §12 of the design is therefore **DISCHARGED**. **The status nevertheless remains `specified-unfrozen` and the design remains `draft-unfrozen`**, because the operative freeze blockers are now checklist items 2–7: (2) the academic arm's stage-1 screening of `ks-a-057` (arXiv:2608.00666) has not been performed; (3) the KSL-C02 mutual-exclusivity flag has no S-D clause in `ks-venue-docs.json`; (4) the per-series fee multiplier table (`ks-vr-d01`) is not extracted, so `p*` in §1.5 is not computable; (5) the rulebook in force was not located, so §8.1's point-in-time reconstruction is blocked at source; (6) the venue clauses have not been re-retrieved and re-digested; (7) no read-time SHA-256 is recorded for the corpus record or for any of the five arm files the design quotes. Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available in the remediation session and a fabricated digest would be worse than an absent one. — **CORRECTION 2026-09-04 (audit round 2, finding SCOPE-2-9). The sentence immediately above beginning "Digests remain `TO COMPUTE` — none is asserted here, because no hashing tool was available" is SUPERSEDED as to the five arm files and is restated as to the corpus record; it is retained only because this register is append-only.** The two registers disagreed: this row carried "no read-time digest is recorded for the corpus record or any arm file" as a live freeze blocker while the design's front-matter `read_state_digest_discipline` field recorded lead-computed digests. They are reconciled here, in the design's own wording. **Pre-freeze checklist item 7 is PARTLY DISCHARGED.** (7a) **Discharged as to computation, for the five arm files.** SHA-256 digests for `ks-academic-candidates.json`, `ks-github-records.jsonl`, `ks-venue-docs.json`, `ks-lateral-records.json` and `ks-instrument-verification.json` were computed by the lead session on 2026-09-04 and are recorded beside their read date in the design's front-matter `read_state_digest_discipline` field. The "no hashing tool was available" reason no longer holds for these five, and no digest was fabricated to obtain them. (7b) **The corpus-record digest is DEFERRED — deferred by an ordering rule, no longer by a missing tool — and no value is asserted for it in either register.** The round-2 disposition is that the corpus-record digest is computed **LAST**, after every corpus-record edit for the round is final (M2 enumeration, the known-item recall result, the new data-integrity entries, the gap-register changes), because a digest taken mid-round pins a byte state that will not exist at freeze and is therefore not a weak pin but a false one. **This ordering rule exists because round 1 violated it**: a corpus-record digest was computed and recorded in the design while the corpus record was still under edit. The placeholder to carry wherever that digest belongs is the literal string `TO COMPUTE BY LEAD AFTER ALL CORPUS-RECORD EDITS ARE FINAL`. ~~**Companion design-side edit NOT YET APPLIED as of this append**, stated so the two registers do not disagree a second time: the round-2 remediation session had no in-place file-edit tool, so the design's `corpus_record_sha256` field still carries the superseded "TO COMPUTE / no hashing tool was available" wording and its `read_state_digest_discipline` field still carries a corpus-record digest computed mid-round in round 1. **Until that edit lands, the corpus-record digest recorded in the design is SUPERSEDED, is not a pin, and must not be relied on; this row is the operative statement.**~~ — **STRUCK 2026-09-04, later the same day: the companion edit HAS landed.** The lead session applied it with an in-place edit tool, so `design.md` now carries the literal placeholder `TO COMPUTE BY LEAD AFTER ALL CORPUS-RECORD EDITS ARE FINAL` in **both** `corpus_record_sha256` and `read_state_digest_discipline`, with the round-1 mid-round value `b3679514…` retained struck and marked "do not rely on it", and with the ordering rule stated in the design itself. The two registers now agree and **neither is more operative than the other** on this item. The superseded flag is retained above rather than deleted because this register is append-only, and because a reader of an intermediate state of the repository would otherwise find a warning with no record of its resolution. (7c) **Components of item 7 that REMAIN OPEN, restated exactly as the design states them.** The five arm-file digests are of the **post-remediation** byte state, which is **not the state this draft read** — design §0.3 records that the draft quoted `ks-academic-candidates.json` at a superseded mid-run state, and the corpus record was corrected in place by remediation DI-8 after the draft was written. They therefore pin the files for a **future re-read** and do **not** retrospectively make the design's existing quotations verifiable. Still open: re-reading each file at its pinned digest, and re-verifying the `ks-sc-001` / `ks-sc-002` README sentences at byte depth (the round-1 re-fetch returned converted text, so neither README SHA-256 was recomputed and the digests carried in design §13 remain the arm log's). Checklist items 2–6 are untouched by this correction and remain open. **Status therefore remains `specified-unfrozen` and the design remains `draft-unfrozen`.** |

_Prior state of this table, retained: it was empty until 2026-09-04. The
bootstrap template's `H001` stub had been removed because it carried
`status: designed`, which this file's own legend defines as "pre-registration
frozen via /preregister; design.md SHA recorded" — no such pre-registration
existed. The H001 row above is a different, substantive entry and deliberately
does **not** claim that status either._

## Tiers

- **Tier 1:** Mechanism well-cited in peer-reviewed lit; high prior probability.
- **Tier 2:** Mechanism plausible from theory; weaker empirical support.
- **Tier 3:** Exploratory; structural hypothesis testing the substrate.
- **Tier 4:** Methodology/gate hypotheses (e.g., multiple-testing family scope).
- **Tier 5:** Replication / reanalysis of prior work.

## Reserved ID blocks

To avoid HID collision across parallel exploration:

| Block | Range | Reserved for |
|---|---|---|
| Main | H001–H099 | core hypotheses |
| Reanalysis | H100–H199 | replication of prior work |
| Methodology | H900–H999 | gate / framework hypotheses |
