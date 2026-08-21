# ADR-0002 — `manifest.json` is a frozen bootstrap record, not a live index

- **Status:** Accepted
- **Date:** 2026-08-21
- **Deciders:** Sajan Koirala
- **Supersedes:** none
- **Raised by:** scope-auditor findings F-9, F-10 (round-1 audit)

## Context

`bootstrap_project.py` writes `manifest.json` at project root recording
`bootstrap_script_version`, `bootstrap_script_git_head`, `kind`, `subdirs`,
`subdir_listing_sha256`, and a `files` map of rendered-template digests.

Two drifts appeared within an hour of bootstrap, both flagged by audit:

1. **`subdirs` no longer describes the tree.** Two directories exist on disk that
   the list does not contain: `docs/deliverables/` (mandated by the
   `/orchestrate` contract) and `docs/literature/search_logs/regime-classification/`
   (written by a delegated research branch). `subdir_listing_sha256` is computed
   over the on-disk tree and therefore no longer matches.
2. **`files["CLAUDE.md"]` is stale.** `CLAUDE.md` was amended in the bootstrap
   session itself, so the recorded digest was invalidated by the first authored
   edit in the project's life.

The auditor's objection is the important part: *a hash field that silently stops
matching is worse than no hash field*, because a reader cannot distinguish
"unchanged" from "nobody is maintaining this."

Two readings are available and they are not compatible:

- **Live index.** `manifest.json` describes the tree as it is now. Requires
  regeneration on every structural change, and every authored edit to a
  templated file.
- **Frozen record.** `manifest.json` describes what the bootstrap script
  produced, at a pinned dotfiles SHA, at a pinned instant. Drift from it is
  expected and is exactly the signal a reader wants.

## Decision

**`manifest.json` is a frozen bootstrap record.** It is not regenerated as the
project evolves, and its `timestamp_utc`, `subdirs`, `subdir_listing_sha256`,
and `files` describe the state at bootstrap only.

Consequently:

- **`subdir_listing_sha256` is not a tamper-detector and must not be read as
  one.** It is a reproducibility anchor: checking out dotfiles at
  `bootstrap_script_git_head` and re-running the script reproduces the recorded
  layout. That is its only guarantee.
- **`files` digests attest to what the script rendered, not to current content.**
  A mismatch means the file was edited after bootstrap, which is normal and
  expected for `CLAUDE.md`, `README.md`, `CITATION.cff`, and `CHANGELOG.md`.
- **`--migrate` remains the mechanism for converging on a newer script version**,
  and refreshing the manifest is its job — not something done by hand.
- Directories created after bootstrap by contract or by delegation
  (`docs/deliverables/`, `docs/literature/search_logs/`) are legitimate and are
  **not** drift to be corrected. They are documented in `CLAUDE.md` §Layout
  instead.

## Consequences

**Positive**

- The ambiguity the auditor identified is closed: a reader now knows what a
  mismatch means.
- No maintenance burden. Regenerating a manifest on every edit would be noise,
  and a manifest that changes constantly attests to nothing.
- The reproducibility guarantee that actually matters — layout reconstructible
  from a pinned script SHA — is preserved intact.

**Negative**

- There is now **no** live integrity check over tracked files. Nothing detects
  an unintended edit to a governance file. Accepted: git history serves that
  role once committed, and this project has no adversarial threat model.
- `docs/deliverables/` lacks the `.gitkeep` sentinel every bootstrap subdir
  carries, so it is invisible to git while empty. Harmless while it holds
  content; noted so a future reader is not surprised.

**Neutral**

- `--migrate --dry-run` will report `layout-drift` against this project because
  of the two post-bootstrap directories. Under this ADR that report is
  informational, not an error to fix. Do not "correct" it by deleting the
  directories.

## Open item

The bootstrap script emits both `runs/` and `artifacts/runs/` as siblings. The
upstream ADR-0002 in the dotfiles repository records this duplication as
"unresolved, not endorsed". This project inherits it and takes no position;
until a run writes to either, the question is moot here.
