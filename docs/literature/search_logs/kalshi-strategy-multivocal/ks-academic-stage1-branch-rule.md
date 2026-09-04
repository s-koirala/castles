# ACADEMIC arm — metadata branching rule

Protocol: `docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md`
(SHA-256 `32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac`,
registered at commit `4821611c1c93b5f929a76f3ba6207e900440cee5`).

Stored here because §4.2 requires it: "Where stage 1 is performed by keyword or
regular-expression branching over metadata, the branching rule is stored with the
logs and the disposition names the branch that produced it, so any row can be
re-derived."

## What this rule is NOT

**No §4.2 stage-1 disposition was assigned by this arm.** No record was included,
excluded, or promoted. The branch label is a *routing signal over retrieved
metadata*, not a determination under N1-N6, K1-K4 or Y1-Y9.

Under §4.4 every row produced by this arm is consequently a **G1** row —
identified, eligibility not assessed. Nothing about any record's merits was
determined. A later screening session decides them, and §4.4 rule 4 requires it
to fix its subset rule before assessing any record in the subset.

## Inputs

Title plus abstract exactly as the platform returned them in the stored payload
under `payloads/`, lowercased, HTML/JATS tags stripped. No full text was
retrieved. OpenAlex abstracts were reconstructed from
`abstract_inverted_index` by position order.

## Vocabularies (from §3.1's frozen instrument and strategy vocabularies)

- `INSTRUMENT`: `event contract`, `event derivative`, `prediction market`,
  `binary contract`, `binary option`, `betting exchange`, `betting market`,
  `sports ?book`, `parimutuel`, `pari-mutuel`, `designated contract market`,
  `event market`
- `VENUE`: `kalshi`, `polymarket`, `predictit`, `betfair`,
  `iowa electronic market`, `intrade`, `tradesports`, `manifold market`,
  `metaculus`, `hollywood stock exchange`
- `STRATEGY`: `arbitrage`, `coherence`, `mispric`, `market ?making`,
  `market maker`, `quoting`, `quote`, `inventory`, `spread`, `execution`,
  `hedg`, `forecast`, `trading strateg`, `backtest`, `order book`,
  `liquidity provision`

## Branches (total and mutually exclusive)

| branch | condition |
|---|---|
| `B1-instrument-and-strategy` | at least one INSTRUMENT or VENUE hit **and** at least one STRATEGY hit |
| `B2-instrument-only` | at least one INSTRUMENT or VENUE hit, no STRATEGY hit |
| `B3-strategy-only` | at least one STRATEGY hit, no INSTRUMENT or VENUE hit |
| `B4-neither` | no hit in either vocabulary |

`ks-academic-candidates.json` reports B1 and B2 rows. B3 and B4 rows are **not
discarded**: the full deduplicated universe, every row carrying its branch, is in
`ks-academic-identified-universe.json`. Reporting a subset is a reporting choice,
not an exclusion, and no B3 or B4 row has been assessed against any criterion.

## Contract-family signal lists (reporting aid only, no protocol status)

`sports`, `weather`, `macro`, `election`, `llm-agent` — used only to report which
of the dispatch's target strata a row speaks to. They decide nothing.

## Deduplication (§4.1)

1. DataCite mints `10.48550/arXiv.<id>` for arXiv deposits, so the same work
   reaches this arm under two locators; those DOIs are canonicalised to the arXiv
   id **before** §4.1's DOI-then-arXiv ordering is applied.
2. Exact match on the strongest available identifier: arXiv id (post-
   canonicalisation), then DOI (case-normalised).
3. Where no identifier matched, case- and punctuation-insensitive title match,
   **only** for normalised titles of 25 characters or more — a shorter string does
   not identify a work, and merging on one would be a false same-work claim. Every
   title merge is itemised in the ledger inside
   `ks-academic-candidates.json`'s sibling scratch record and reproduced by
   re-running the script; the retained and dropped locators are both recorded.

## Novelty differencing (§3.1)

Each row's DOI and arXiv id are looked up in `ks-prior-identifiers.json`
(6,923 identifiers from the 2026-09-02 branch). `prior_disposition` carries that
file's value or `null`; `novel_vs_2026_09_02` is `true` iff absent. That file's
own coverage limit stands: only 6,923 of the predecessor's 8,813 records carry an
identifier, so a predecessor record with no identifier cannot be differenced by
this index, and this arm's novelty counts are therefore an **upper bound** on
novelty.

## Determinism

`PYTHONHASHSEED=0` is asserted at entry of the extraction and assembly scripts,
per §3.0.
