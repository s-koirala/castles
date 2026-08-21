# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `docs/methodology/charter_castles_2026-08-21.md` — project charter: standing
  commitments, admissible output types, and the negative-result protocol.
- `failure_log.md` — append-only null register, seeded with F001–F004.
- `docs/research_notes/research_agenda_regime-classification_2026-08-21.md`.
- `docs/research_notes/research_agenda_architecture_2026-08-21.md`.
- `docs/research_notes/research_agenda_context-portability_2026-08-21.md`.
- `docs/decisions/ADR-0001-project-kind-and-scope.md`.
- `docs/deliverables/` — per-session deliverable declarations (`/orchestrate`).
- `docs/audits/audit_trail_think-tank-charter_2026-08-21.md` + JSON sidecar.
- AI-assistance statement in README, per ICMJE 2026.

### Changed
- `CLAUDE.md` §Scope — replaced quant boilerplate with the think-tank charter
  scope; recorded that no cwd-scoped rule file auto-activates at this path.
- `CLAUDE.md` §Identity hygiene — recorded the real-name attribution decision.
- `README.md` — same boilerplate correction; removed retired `outputs/` from the
  layout block.
- `CITATION.cff` — real-name authorship; corrected abstract.
- Charter revised to rev 2 after round-1 audit: layer set expanded from four to
  eleven, `construct` gated, validity step 2b added, PRISMA 2020 adopted for
  systematic reviews, falsification added for commitment 1.
- `failure_log.md` revised to rev 2: F001, F003, F004 re-localized; two transfers
  withdrawn to "none found"; evidence tier added.
- Both original agendas: falsification tests repaired — three relabelled as
  design-resolution studies / preconditions / adoption policy, and a genuine
  branch-level test added to each of the seven branches.

### Fixed
- `CITATION.cff` no longer fails YAML parsing (unquoted `<<TODO: …>>` placeholder
  containing `': '`), which would have failed the `citation-cff` pre-commit hook.
- `hypothesis_backlog.md` — removed template stub row asserting a false
  `designed` status with no pre-registration behind it.
- Removed absolute paths carrying the OS username from the tracked deliverable
  spec.

## [0.0.1] - 2026-08-21

### Added
- Initial bootstrap via `/bootstrap-project --kind=quant`.
- Directory tree per SKIE-Universe canonical layout.
- `manifest.json` recording `bootstrap_script_git_head=f08015fb5782`.
- Pre-commit hooks registered: ruff, nbstripout, nbqa, seed-guard, citation-cff.
