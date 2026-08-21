# castles

A standing cross-domain research think tank. Output is systematic reviews and
methodology documentation over an intentionally unbounded topic domain.

Distinctive method: nulls and negative results are objects of study, not dead
ends. Every null encountered is registered in [failure_log.md](failure_log.md)
and worked through the five-step protocol in
[the charter](docs/methodology/charter_castles_2026-08-21.md).

Scaffolded `--kind=quant` for its literature-review and hypothesis-register
structure, **not** because the domain is markets-only — see
[ADR-0001](docs/decisions/ADR-0001-project-kind-and-scope.md).

## Status

| Field | Value |
|---|---|
| Kind | `quant` (layout only — domain is cross-disciplinary; see ADR-0001) |
| Python | `>=3.11,<3.13` |
| License | `MIT` |
| Bootstrap date | `2026-08-21` |
| Dotfiles HEAD | `f08015fb5782` |

## AI-assistance statement

Per [ICMJE Recommendations](https://www.icmje.org/recommendations/) (updated
January 2026). AI is not an author and is not listed in `CITATION.cff`.

| Field | Value |
|---|---|
| Model | Claude Opus 5 (`claude-opus-5`), via Claude Code |
| Roles | idea (agenda subtopic enumeration), prose (charter, agendas, ADR, failure log), audit (specialist subagent branches), code (remediation and trail-generation scripts) |
| Human role | Sajan Koirala — scope direction, identity decision, thread commissioning. **Final review has NOT occurred.** |
| Audit trail | [`docs/audits/`](docs/audits/) — per-session, with JSON sidecar carrying artifact SHA-256 digests |
| Reproducibility log | None emitted to date: no run has written under `artifacts/`, `runs/`, or `logs/`, which is the trigger condition |

**Audit status, stated precisely.** Machine-authored prose here was audited by
specialist subagent branches **of the same model family** — not by independent
systems, and the adversarial refute gate was executed by the lead session rather
than by independent refuters. Coverage is per-round and **incomplete**: the
charter and failure_log were substantially rewritten *after* the round that
audited them, and the 2,179-line systematic review was produced by a single
screener that demonstrated instability against its own criteria. See the
residual-risk sections of [the audit trail](docs/audits/) for what each round did
and did not cover.

**No human has reviewed any artifact in this repository.** Treat everything as
draft.

## Layout

```
castles/
├── src/                  # source-layout package
├── tests/                # pytest suite
├── scripts/              # one-shot entrypoints
├── notebooks/            # exploratory (stripped via nbstripout)
├── data/
│   ├── raw/              # read-only vendor pulls (gitignored)
│   ├── interim/          # lossy transforms (gitignored)
│   ├── processed/        # analysis-ready (gitignored)
│   └── external/         # reference data
├── docs/
│   ├── audits/           # audit-remediate-loop trails
│   ├── decisions/        # ADRs (Nygard/MADR)
│   ├── literature/       # primary-source PDFs + notes
│   ├── methodology/      # method memos, derivations
│   ├── reports/          # stakeholder-facing reports
│   ├── research_notes/   # dated memos
│   └── templates/        # reusable doc templates
├── artifacts/
│   ├── models/           # versioned model binaries
│   └── runs/             # run aggregate outputs
├── runs/                 # top-level run outputs (SKIE-Universe convention)
├── research/             # hypothesis-register / analysis-stage subdirs
├── reports/              # rendered reports
├── config/               # validated configs (pydantic / yaml)
├── logs/
│   └── reproducibility/  # ReproLog records + pip-freeze archive
├── CLAUDE.md             # project-local Claude rules
├── CHANGELOG.md          # Keep-a-Changelog 1.1.0
├── CITATION.cff          # CFF v1.2.0
├── LICENSE
├── pyproject.toml        # PEP 621
├── .gitignore
├── .pre-commit-config.yaml
└── manifest.json         # bootstrap reproducibility anchor
```

## Setup

```bash
# Create venv from project pyproject.toml
uv venv && uv sync

# Install pre-commit hooks (seed-guard, citation-cff)
uv run pre-commit install

# Run tests
uv run pytest

# Check data manifest integrity
python ~/.claude/scripts/build_data_manifest.py --check
```

## Reproducibility

This project follows the 13-field ReproLog contract documented at
`~/.claude/skills/emit-repro-log/SKILL.md`. Every artifact-producing run
records:

- git HEAD
- pip freeze SHA-256 (full 64-hex, archived under `logs/reproducibility/env/`)
- dataset checksums from `data/_manifest.json`
- RNG seed
- model commit hash

Commits use `/commit-with-provenance --role=<role>` which emits
`Repro-Log-Path:` and `Repro-Log-SHA256:` trailers per ICMJE 2026 AI-assistance
disclosure.

## Citation

See [CITATION.cff](CITATION.cff) (CFF v1.2.0) for machine-readable citation
metadata. To add a reference to the bibliography:

```bash
# Via /cite-add slash command (resolves via CrossRef MCP)
/cite-add 10.1093/jamiaopen/ooy012
```

## Architecture decisions

See [docs/decisions/](docs/decisions/) for ADR records (Nygard/MADR format).
New decisions via `/adr-new "<title>"`.

## License

See [LICENSE](LICENSE).
