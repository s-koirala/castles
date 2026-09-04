# Archived executor scripts — kalshi-strategy-multivocal

What each archived script does, what it consumes, whether that input is in the repository,
and precisely what a re-runner can and cannot reproduce.

Protocol: [docs/methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md](../../methodology/protocol_kalshi-strategy-multivocal_2026-09-04.md)
(sha256 `32dfea6da36cc367ece91cc282dda50e1be7ad6cc2af02dc96e62ed52b7ad6ac`),
registration commit `4821611c1c93b5f929a76f3ba6207e900440cee5`.
Retained and non-retained response bytes are inventoried in [PAYLOADS.md](PAYLOADS.md).

## Before running anything

`PYTHONHASHSEED=0` must be set **in the environment before the interpreter starts** — hash
randomisation is fixed at start-up, so a script cannot set it for itself. Every executable
script here asserts it at entry and refuses to run without it.

```bash
PYTHONHASHSEED=0 python <script>
```

The one exception is [ks-academic-query-table.py](ks-academic-query-table.py), a pure data
table with no hash-order dependence; it carries a comment saying so instead of an assert.

## Import-name shims

The archived filenames are hyphenated and therefore not legal Python module names, so the
scripts that import each other had nothing to bind to. Two shims restore the bindings
without renaming the archived files (whose names are cited elsewhere in the corpus record):

| shim | loads | re-exports |
|---|---|---|
| [queries.py](queries.py) | [ks-academic-query-table.py](ks-academic-query-table.py) | `QUERIES`, `CR`, `CROSSREF_SEL`, `OA_MAIL` |
| [run_arm.py](run_arm.py) | [ks-academic-runner.py](ks-academic-runner.py) | `execute`, `main`, `fetch`, `now`, and the module's constants |

The shims add nothing and compute nothing. The archived files remain the sources of truth.

## ACADEMIC arm (S-A / S-B) — this directory

Run order: **runner → supplementary → recovery-pass → extract → assemble.**

| script | what it does | consumes | input archived? | reproducible? |
|---|---|---|---|---|
| [ks-academic-query-table.py](ks-academic-query-table.py) | the frozen section-3.1 query table | nothing | n/a | fully — it is data |
| [ks-academic-runner.py](ks-academic-runner.py) | executes the table; writes `payloads/` and one `ks-*.json` log per query | `queries` | yes (shim) | **no** — live API calls. A re-run re-queries the platforms and will not return the 2026-09-04 result sets. Its `run_summary.json` was not retained; the per-query `ks-*.json` logs carry the same content and are archived. |
| [ks-academic-query-table-supplementary.py](ks-academic-query-table-supplementary.py) | supplementary block (crossref-16…19, openalex-09…14, arxiv-09…13) | `run_arm`, `queries` | yes (shims) | **no** — live API calls |
| [ks-academic-recovery-pass.py](ks-academic-recovery-pass.py) | Semantic Scholar retry chain and RePEc alternate-interface probes | `run_arm`, `queries` | yes (shims) | **no** — live API calls |
| [ks-academic-extract.py](ks-academic-extract.py) | parses payloads into rows, dedupes per section 4.1, differences against the prior branch; writes `candidates.json` and `title_merge_ledger.json` | `payloads/`, [ks-prior-identifiers.json](ks-prior-identifiers.json) | **yes** | **yes, offline and exactly** — see below |
| [ks-academic-assemble.py](ks-academic-assemble.py) | adds contribution-code and strategy-class signals, sorts, resolves DOIs; writes [ks-academic-candidates.json](ks-academic-candidates.json) and [ks-academic-identified-universe.json](ks-academic-identified-universe.json) | `candidates.json` | **not archived — regenerate it** (see below) | signals and ordering: yes, offline. The `doi_handle_responseCode` column: **no** — it is a live doi.org handle lookup. |

### The one missing academic intermediate, and how to get it back

`candidates.json` is the hand-off from extract to assemble. It was written into the
executing session's working directory, not into this repository, and was not archived.
It is **not fabricated here**; it is regenerated in one offline command:

```bash
PYTHONHASHSEED=0 python ks-academic-extract.py
```

Verified on 2026-09-04 against the archived payloads:

- `title_merge_ledger.json` regenerated **byte-identical** to the archived
  [ks-academic-dedup-title-ledger.json](ks-academic-dedup-title-ledger.json)
  (sha256 `15dbb51e4bc6f5763847131bc7edea89ea8c10f2625705b6cfda037c49e97c74` both ways).
- `candidates.json` regenerated with 528 rows, the same record-id set as the archived
  [ks-academic-identified-universe.json](ks-academic-identified-universe.json), and every
  shared field identical row-for-row. The universe file adds only the three columns
  assemble computes (`contribution_code_signals`, `strategy_class_signal`,
  `doi_handle_responseCode`).
- Console figures reproduced: 650 raw rows, 528 deduplicated, 122 duplicates; branch counts
  B1 116 / B2 36 / B3 208 / B4 168; 437 novel vs the 2026-09-02 branch, 91 prior-dispositioned.

The regenerated files are deliberately **not** committed: they are byte-equivalent to
material already archived, and the corpus record's file inventory is the lead's to set.

## SOFTWARE-REPOSITORY arm (S-C) — [ks-github-scripts/](ks-github-scripts)

Run order: **run_search → run_search2 → draw_and_pin → get_readmes → write_logs →
write_ledger → verify_quotes.**

| script | what it does | consumes | input archived? | reproducible? |
|---|---|---|---|---|
| [run_search.py](ks-github-scripts/run_search.py) | 20 GitHub repository-search queries; writes `payloads/ks-gh-*.json.gz` and `_stage1_gh.json` | nothing | n/a | **no** — live API calls |
| [run_search2.py](ks-github-scripts/run_search2.py) | GitLab, PyPI, npm, Kaggle, and the auth-gated GitHub code-search attempt; writes `_stage2.json` | `run_search` | yes | **no** — live API calls |
| [draw_and_pin.py](ks-github-scripts/draw_and_pin.py) | applies the SR-1…SR-5 subset rule, draws the sample, pins each drawn record to a commit SHA; writes `_drawn.json` and `_pins.json` | `_stage1_gh.json`, `_stage2.json` | **no** — but both are re-derivable, see below | the draw: **yes, offline and exactly**. The pin: **no** — live commit lookups. |
| [get_readmes.py](ks-github-scripts/get_readmes.py) | fetches each drawn record's README at its pinned SHA into [ks-github-readme-evidence/](ks-github-readme-evidence); writes `_readmes.json` | `_drawn.json`, `_pins.json` | `_drawn.json` re-derivable; `_pins.json` **not** | **no** — the README bytes are archived, but re-fetching needs the pins |
| [write_logs.py](ks-github-scripts/write_logs.py) | emits [ks-github-queries.json](ks-github-queries.json) and [ks-github-records.jsonl](ks-github-records.jsonl) | all five stage files + [extractions.json](ks-github-scripts/extractions.json) | extractions.json yes; `_pins.json` and `_readmes.json` **no** | **no** — blocked on `_pins.json` / `_readmes.json` |
| [write_ledger.py](ks-github-scripts/write_ledger.py) | emits the G1/G2 capacity ledger [ks-github-capacity-ledger.json](ks-github-capacity-ledger.json) | `_drawn.json`, `_stage1_gh.json`, `_stage2.json`, ks-github-records.jsonl | stage files re-derivable | **yes, offline**, once the three stage files are rebuilt |
| [verify_quotes.py](ks-github-scripts/verify_quotes.py) | checks every extracted quote is an exact substring of the retrieved bytes | extractions.json, ks-github-readme-evidence/, `_stage1_gh.json`, `_stage2.json` | READMEs **yes**; stage files re-derivable | **partially** — see below |

### The five missing S-C stage files

None of `_stage1_gh.json`, `_stage2.json`, `_drawn.json`, `_pins.json`, `_readmes.json` was
retained; they were written into this directory during the run and later removed. They are
**not fabricated here.** Their status splits cleanly:

**Re-derivable offline, verified.** `_stage1_gh.json`, `_stage2.json` and `_drawn.json` are
pure functions of the archived response bytes under `payloads/`, because those payloads are
the raw API responses the harvest functions consume. Replaying `harvest_gh()` and the
stage-2 harvests over the archived bytes on 2026-09-04 reproduced, exactly:

| quantity | rebuilt | recorded in [ks-github-capacity-ledger.json](ks-github-capacity-ledger.json) |
|---|---|---|
| identified — github.com / gitlab.com / pypi.org / registry.npmjs.org | 647 / 21 / 11 / 302 | 647 / 21 / 11 / 302 |
| identified, total | 981 | 981 |
| stratum sizes gh_sr1 / gh_sr2 / gitlab / pypi / npm | 341 / 253 / 19 / 11 / 68 | 341 / 253 / 19 / 11 / 68 |
| drawn subset | 43 records | 43 assessed records in ks-github-records.jsonl — **identical set** |

**Not re-derivable.** `_pins.json` holds live GitHub/GitLab commit-lookup responses and
`_readmes.json` the manifest of the README fetch. Neither response set was stored. A re-run
would pin to today's HEAD, not to the 2026-09-04 SHAs the records name, so the pins in
[ks-github-records.jsonl](ks-github-records.jsonl) cannot be re-obtained — only checked
against the platform if those commits still exist. The README **bytes** are archived (below),
so nothing downstream of the fetch is lost, only the fetch's own re-execution.

### README evidence

[ks-github-readme-evidence/](ks-github-readme-evidence) holds the 29 README files retrieved
at the pinned SHAs — the directory the scripts wrote as `_readmes/`. Both
[get_readmes.py](ks-github-scripts/get_readmes.py) and
[verify_quotes.py](ks-github-scripts/verify_quotes.py) now point at the archived name.
It covers 26 of the 29 GitHub records and all 3 GitLab records. The 3 GitHub records with no
file are exactly the three carrying `readme.retrieved: false` in ks-github-records.jsonl —
two with no README at the pinned SHA, one with no commit identifier (HTTP 409). Nothing is
missing that the record does not already declare missing.

### What verify_quotes.py can and cannot check today

It builds each source string from two halves: the README bytes (archived) and the platform
`description` field (held only in the lost stage files). Rebuild the two stage files first
and it runs in full. Against the archived README bytes **alone**, 130 of the 132 GitHub and
GitLab quotes are reproducible as exact substrings; the remaining 2 belong to records with no
archived README and were drawn from platform metadata. No quote whose README is archived
failed to reproduce. The PyPI and npm records draw entirely on the stage-2 metadata and
cannot be checked until `_stage2.json` is rebuilt.

## What was changed in these scripts, and what was not

Changed: absolute home-directory paths replaced by paths derived from each script's own
location; the no-op `os.environ.setdefault("PYTHONHASHSEED", "0")` in the S-C arm replaced
by a real entry assert, and the same assert added to the other S-C scripts; `_readmes`
repointed to the archived directory name; import-name shims added; re-runner notes added to
docstrings.

Not changed: every query, endpoint, cap, regex, allocation, threshold, digest basis and
output schema. No recorded count, digest, verdict or quotation in any log was touched. No
script gained randomness, a network call, or a write outside this directory tree.
