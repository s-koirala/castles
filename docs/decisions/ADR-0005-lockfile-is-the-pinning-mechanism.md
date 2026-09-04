# ADR-0005 — `uv.lock` is the pinning mechanism; `pyproject.toml` stays a range specification

- **Status:** Accepted
- **Date:** 2026-09-03
- **Deciders:** Sajan Koirala
- **Supersedes:** none. **Partially closes** verification gap VG-14 recorded in
  [lit_review_explosive-regime-dating_2026-08-24.md](../literature/lit_review_explosive-regime-dating_2026-08-24.md)
  §12.3 — see §"Why this does not fully close VG-14" below. Corrected
  2026-09-03 after audit finding REV-1-5: the header first read "Closes",
  contradicting the body three sections down, so a reader of the status block
  alone got exactly the claim the body exists to prevent.

## Context

The 2026-09-02 audit's reproducibility branch recorded three repository-level
gaps. VG-14: **no clone-durable environment specification exists.**
`pyproject.toml` declares every dependency unpinned (`ruff`, `pytest`,
`pre-commit`, `nbstripout`, `nbqa`, `pyyaml`, `jsonschema>=4.18`), `uv.lock` was
present in the working tree but **untracked**, and the only concrete environment
record was a `pip freeze` archived under `logs/reproducibility/env/`, which is
gitignored and therefore does not resolve in a fresh clone.

The consequence is specific, not theoretical. `CLAUDE.md` §Reproducibility
contract requires every artifact-producing run to log a `pip freeze` digest, and
the deliverables do cite one. But a digest whose referent is unreachable from a
clone pins nothing for anyone but the author, on the machine that produced it.

The question this ADR answers is which of two mechanisms carries the pin.

## Decision

**`uv.lock` is the pinning mechanism and is tracked. `pyproject.toml` remains a
range specification and is not pinned.**

Concretely:

- `uv.lock` is tracked. Two states exist and **both are named, because the pin
  must resolve**:
  - first tracked at **`2ba291f9922547e1848d7d505cedafb2979e2433`**, blob SHA-256
    `d2a0b28183f1d74260cd56bcd2881febf9e97d6d2e9dc58d07200db61c478597`
    (208,360 bytes);
  - **current state** at **`01ecfe7`**, blob SHA-256
    `eca78f9d52a8534f2890c99bd2f16b3aadc1455b0eb7b93c6d2e621240efd885`
    (208,234 bytes), which is also the worktree state. The file changed between
    the two because moving the dev dependencies to a PEP 735 group made `uv lock`
    re-record the project as `source = { virtual = "." }` rather than
    `{ editable = "." }`.

  Both digests are over the LF checkout form that `.gitattributes`
  (`uv.lock text eol=lf`) makes identical on every platform. Verify tracking with
  `git ls-files uv.lock`, the deliverable spec's own check for this item.

  **Two corrections to this bullet, both recorded rather than overwritten.**
  Its first draft asserted "is committed" in the present tense while the file was
  still untracked and named no commit (audit REV-1-5). Its second draft then
  paired commit `2ba291f` with the digest of the `01ecfe7` state — one pin naming
  two different file states, which resolves to nothing (audit QUANT-2-1). Both
  are the same defect this ADR identifies in `pip_freeze_sha256`: a digest whose
  referent cannot be resolved pins nothing. That it recurred twice inside the ADR
  arguing for resolvable pins is worth leaving on the record.
  It resolves the full dependency graph — 1,467 lines,
  every package with its registry source, sdist and wheel URLs and SHA-256
  hashes — under `requires-python = ">=3.11, <3.13"`, matching the Python pin
  already recorded in `CLAUDE.md` §Project state and `manifest.json`.
- `pyproject.toml` keeps its ranges. It declares what the project *needs*;
  the lockfile records what a resolution *was*.
- A run that must be reproduced is reproduced with `uv sync`, which installs
  from the lockfile, not with `uv pip install -e .`, which re-resolves.
- The `pip freeze` archives under `logs/reproducibility/env/` are retained as a
  per-run record but are **no longer the primary environment carrier**. They
  remain untracked locators, cited by digest, exactly as the reproducibility
  contract describes.

### Why the lockfile rather than pinned ranges

- It is the mechanism `uv` provides for this purpose, and `uv` is the project's
  declared environment manager (`~/.claude/CLAUDE.md` §Tooling defaults). Pinning
  `pyproject` by hand would duplicate the lockfile's job and the two would drift.
- The lockfile carries **hashes**, which pinned version ranges do not. A pinned
  `ruff==0.x.y` names a version; the lockfile names the artifact.
- It is multi-platform. The resolution markers cover win32, emscripten and the
  general case across both supported Python minors, so a clone on another
  platform resolves to the same intended graph rather than to whatever that
  platform's resolver picks.

### Why this does not fully close VG-14

Stated plainly, because the gap is easy to over-claim as closed:

- The lockfile pins the **declared** dependency graph. This project's deliverables
  are prose and JSON produced largely by LLM agents and by ad-hoc scripts run on
  the standard library; the lockfile does not pin those, and no lockfile could.
- The environment that produced the 2026-08-24 and 2026-09-02 corpora is **not**
  the environment this lockfile describes, and cannot be recovered — the
  corpus-producing ReproLog for commit `8aeebfe` carries the SHA-256 of the empty
  string as its `pip_freeze_sha256` (VG-15), so there is no record to pin
  against. This ADR fixes the mechanism going forward; it does not retroactively
  supply an environment for work already done.
- VG-16 (no entrypoint re-derives any reported number) is a separate gap,
  addressed separately by the test added under the same declaration.

## Consequences

**Positive**

- A fresh clone can construct a defined environment, which it could not before.
- Environment drift becomes visible as a lockfile diff in review, rather than
  invisible.
- The reproducibility contract's `pip_freeze_sha256` field stops being the only
  environment evidence, so its known weaknesses — untracked path, platform-
  dependent line endings, the empty-string failure mode seen in VG-15 and again
  in this session's own delivery log — stop being single points of failure.

**Negative**

- The lockfile must be regenerated deliberately when a dependency changes;
  a stale lockfile is a new way to be wrong, and nothing in CI currently checks
  it.
- Tracking a 1,467-line generated file makes some diffs noisy.

**Neutral**

- No existing deliverable's digests change. The lockfile is additive.

## Alternatives considered

- **Pin every dependency in `pyproject.toml` and do not track the lockfile.**
  Rejected: loses hashes and platform markers, duplicates the resolver's job by
  hand, and invites drift between the two files.
- **Track the `pip freeze` output at a tracked path instead.** Rejected: it is a
  flat list of one interpreter's installed packages on one platform with no
  source or hash information, and this session demonstrated two of its failure
  modes — a text-mode write producing CRLF bytes whose digest did not match the
  published value, and `uv pip freeze` exiting 0 with empty output, which would
  have archived the SHA-256 of the empty string.
- **Do nothing and keep citing untracked digests.** Rejected: that is the state
  VG-14 recorded as a defect.

## References

- `CLAUDE.md` §Reproducibility contract, §Project state.
- `~/.claude/CLAUDE.md` §Tooling defaults — `uv` as the environment manager.
- [lit_review_explosive-regime-dating_2026-08-24.md](../literature/lit_review_explosive-regime-dating_2026-08-24.md)
  §12.3 VG-14, VG-15, VG-16.
- [ADR-0002](ADR-0002-manifest-as-frozen-bootstrap-record.md) — the adjacent
  decision on what `manifest.json` freezes.
