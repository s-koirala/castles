# S-C arm — assessment subset rule

**Protocol:** `docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md`
**Protocol SHA-256:** `32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac`
**Registration commit:** `4821611c1c93b5f929a76f3ba6207e900440cee5`
**Arm:** SOFTWARE-REPOSITORY (§3.2), yields source class S-C.
**Fixed at:** 2026-09-04, **before** any record in the defined subset was assessed,
as §4.4 rule 4 requires.

## Why this file exists

The frozen §3.2 query grid returned more records than one execution session can
assess at the §5 extraction depth. §4.4 supplies the only lawful response: the
unassessed remainder is coded **G1 — identified, eligibility not assessed**, which
is a **capacity gap and not a criterion failure**, and §4.4 rule 4 requires the
subset rule to be *fixed before* any record in the subset is assessed. This file
is that fixing.

## What this rule is NOT

- It is **not** an eligibility criterion. No record is excluded by it. Records
  outside the subset are **G1 — undecided**, not ineligible (§4.4 rules 1 and 3).
- It applies **no popularity floor, star count, fork count, watcher count, or
  activity/recency threshold**. §3.2 forbids all of these: either would be an
  unlabelled constant selecting against recent and low-profile work. Stars and
  last-commit dates are recorded as attributes only.
- It runs **no curation classifier**. The Munaiah et al. `reaper` framework is
  cited by §7.2 only as establishing that a signal/noise problem exists; it is
  **not run and is not an eligibility filter** (§7.2(b)).
- It applies no date, language, or licence filter.

## The rule

Let a record's **screening text** be the concatenation of its platform-reported
identity and description fields only — for GitHub/GitLab: `full_name`,
`description`, `topics`; for PyPI: package name and `info.summary`; for npm:
package name, `description`, `keywords`. These are the platform's own metadata
fields, per §3.2's "fetched through the platform's REST API rather than scraped".

- **SR-1 (venue-of-interest stratum).** Screening text matches
  `/kalshi/i`. This is the §1.1 **venue of interest** (KalshiEX LLC). Topical,
  not qualitative.
- **SR-2 (cross-venue stratum).** Screening text does not match SR-1 but matches
  `/polymarket|predictit|manifold|betfair|smarkets|prediction[ -]?market|event[ -]contract|betting exchange/i`
  — an in-scope instrument venue or event-contract term under §2.2. Records here
  are expected to carry F8 = `transferred-…` and exist so the T2/T3 strata are
  not left wholly unassessed.
- **SR-3 (contribution screen at metadata depth).** Screening text additionally
  matches an **artifact-intent token from the frozen §3.2 list**:
  `/\bbot\b|trading|trader|arbitrage|\barb\b|market[ -]?mak|backtest|data capture|capture|\bclient\b|\bsdk\b|scanner|\bscan\b|quant|strateg/i`.
  A record failing SR-3 is **G1**, never Y2: §4.4 rule 3 forbids stretching a
  Y-code over an unassessed record.
- **SR-4 (assessment order).** Within each stratum, records are ordered ascending
  by `sha256(host + "/" + full_name)` rendered as lowercase hex. This key is
  deterministic and reproducible, and is **independent of stars, forks, activity,
  recency, and alphabetical position**. It is used *instead of* platform relevance
  rank, which §3.2 declares as the arm's unmitigated sampling hazard.
- **SR-5 (host allocation).** Assessment capacity is allocated per host so that
  host coverage is not an artefact of a single ordered cap. Allocations are
  **capacity numbers, not eligibility numbers**:

  | host | stratum | allocation |
  |---|---|---|
  | GitHub | SR-1 | 24 |
  | GitHub | SR-2 | 5 |
  | GitLab | SR-1 ∪ SR-2 | 3 |
  | PyPI | SR-1 ∪ SR-2 | 6 |
  | npm | SR-1 ∪ SR-2 | 5 |

  PyPI and npm allocations are not drawn by SR-4 order: their venue-matching sets
  are small enough that the allocation is filled by SR-4 order over the whole
  matching set, and PyPI's set is enumerated by the frozen package-name probe list
  in `ks-github-queries.json`, which is itself the query.

- **SR-6 (commit-identifier requirement is not a subset rule).** §3.2 requires a
  commit SHA or release tag as of the access date. A record for which the
  identifier could not be obtained is **reported as such** in
  `ks-github-records.jsonl` with `commit_identifier_obtained: false`, and is
  counted in `n_without_commit_identifier`. It is not silently dropped and it is
  not counted as an inclusion on the merits.

## Declared consequence

The assessed subset is a **non-random sample of a non-random sample**: the frozen
query grid's yield is already ranked and truncated by undisclosed
platform-internal relevance and popularity signals (§3.2, §7.2(a)), and SR-4 then
draws deterministically from within that yield. **No completeness bound is claimed
for this arm and none is attributable to the cited repository-mining literature,
which supplies none** (§7.2 declared gaps (i)).

## Rate-limit constraint recorded as a capacity fact

GitHub's unauthenticated REST core limit is 60 requests/hour and its search limit
10 requests/minute; `GET /search/code` returns HTTP 401 without authentication and
was therefore logged as attempted-and-blocked rather than executed. Kaggle's
kernel-list endpoint likewise returned HTTP 401. No account was created and no
authenticated endpoint was used, per the arm's execution constraints.
