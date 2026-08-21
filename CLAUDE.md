# castles — Project-Local Rules

Inherits all user-global rules from `~/.claude/CLAUDE.md`.

**No cwd-scoped rule file is auto-activated here.** This path matches no glob in
`rules/quant-project.md`, `rules/population-health.md`, or `rules/publishing.md`.
`rules/quant-project.md` is adopted **by explicit reference** where a given
analysis justifies it, and each adoption is documented at its site. See
[ADR-0001](docs/decisions/ADR-0001-project-kind-and-scope.md) §Decision.

## Scope

Standing cross-domain research think tank. Output is systematic reviews and
methodology documentation over an intentionally unbounded topic domain. The
governing document is
[docs/methodology/charter_castles_2026-08-21.md](docs/methodology/charter_castles_2026-08-21.md);
the kind selection and its rationale are recorded in
[ADR-0001](docs/decisions/ADR-0001-project-kind-and-scope.md).

Scaffolded with `--kind=quant` for its literature-review and hypothesis-register
structure, **not** because the domain is markets-only. This path matches no cwd
glob in `rules/quant-project.md`, so those rules are not auto-activated; they are
adopted by explicit reference where a given analysis justifies them.

Distinctive method: nulls and negative results are objects of study, not dead
ends. Every null encountered is registered in [failure_log.md](failure_log.md)
and worked through the five-step protocol in the charter. Retrospective power is
never computed; the minimum detectable effect size is computed instead.

## Reproducibility contract

Every artifact-producing run in this project emits a 13-field ReproLog at
`logs/reproducibility/repro_log_{run_id}.json` per the
[emit-repro-log](https://github.com/s-koirala/dotfiles/tree/main/claude/skills/emit-repro-log)
skill. All commits use
[/commit-with-provenance](https://github.com/s-koirala/dotfiles/tree/main/claude/commands/commit-with-provenance.md)
with `--role={idea|code|prose|audit|multi}` per ICMJE 2026 disclosure.

Per-run scientific payloads go to `artifacts/runs/{HID}/[stage{N}/]{run_id}/sidecar.json`
— the single canonical sidecar path.

`artifacts/` and `logs/` are gitignored, so neither path resolves in a fresh
clone. **A tracked deliverable therefore cites the SHA-256 of the ReproLog and
the sidecar plus the git HEAD, and labels the path as an untracked locator —
never the path alone.** The clone-durable carrier for those digests is the
commit itself (`Repro-Log-Path:` / `Repro-Log-SHA256:` trailers written by
`/commit-with-provenance`).

Dataset provenance: `data/_manifest.json` (managed by
`~/.claude/scripts/build_data_manifest.py`). Run `--check` mode in CI to
detect drift.

## Quickstart

```bash
uv venv && uv sync
uv run pre-commit install
uv run pytest
```

## Project state

- **Kind:** quant
- **Bootstrap date:** 2026-08-21
- **Python version pin:** `>=3.11,<3.13`
- **Bootstrap script HEAD:** `f08015fb5782` (see `manifest.json`)

## Directory layout

See `manifest.json` for the canonical subdir list. Key conventions:

- `data/{raw,interim,processed,external}/` — read-only raw → analysis-ready
  pipeline; per-file SHA in `data/_manifest.json`. `data/metadata/` holds
  codebooks (TIER 4.0).
- `docs/{audits,decisions,deliverables,literature,methodology,research_notes,templates}/`
  — durable human-authored prose. Tracked. `docs/reports/` was retired; rendered
  deliverables live in `reports/` (see
  `~/.claude/docs/decisions/ADR-0002-output-root-retirement.md`).
- `artifacts/{models,runs}/` — machine-generated run output; the canonical home
  for run sidecars (`artifacts/runs/{HID}/[stage{N}/]{run_id}/sidecar.json`).
  Gitignored.
- `logs/reproducibility/` — ReproLog + render-log records + pip-freeze archive.
  Gitignored.
- `research/` — work in progress. `reports/` — rendered deliverables, tracked;
  `reports/figures/` for their figures.
- `runs/` — top-level run root retained for compatibility with pre-existing
  SKIE-Universe project layouts. **Not** a sidecar location: new run output and
  all sidecars go to `artifacts/runs/`
  (see `~/.claude/docs/decisions/ADR-0001-reprolog-sidecar-path.md`).

## Identity hygiene

**This repository is public and attributed under the author's real name**, by
explicit instruction on 2026-08-21. Repository-local git config only; global
config untouched:

```
user.name  = Sajan Koirala
user.email = 238704148+s-koirala@users.noreply.github.com
```

The author's real address is deliberately **not** in commit metadata and must not
be introduced into any commit, tag, or tracked file. The name is public by
choice; the address is not.

**Consequence, recorded deliberately.** `~/.claude/rules/publishing.md`
§Identity hygiene governs SKIE-pseudonym projects and forbids real-name metadata
in committed files. That rule is **not in force here** — this path matches none of
its cwd globs, and the author has chosen real-name attribution for this project.
Work intended for pseudonymous publication must therefore **not** originate in
this repository; it belongs in a separate publishing-kind project where the rule
does apply. See
[ADR-0001](docs/decisions/ADR-0001-project-kind-and-scope.md) §Identity.

Repo-relative paths remain the convention in tracked prose — absolute paths under
a home directory are brittle across machines regardless of identity policy.
