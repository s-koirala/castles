# ADR-0001 — Project kind and scope

- **Status:** Accepted
- **Date:** 2026-08-21
- **Deciders:** Sajan Koirala
- **Supersedes:** none

## Context

`castles` is being established as a standing think tank producing systematic
reviews and methodology documentation across an intentionally unbounded domain.
Two decisions had to be made at bootstrap, both structural and both awkward to
reverse.

**Scaffold kind.** `bootstrap_project.py` offers `generic`, `quant`, `epi`, and
`publishing`. The kind is recorded in `manifest.json` and is a migration
precondition: `--migrate` exits 2 when `manifest.kind` differs from the passed
`--kind`. Changing kind later therefore means re-bootstrapping, not migrating.

The tension: the project's stated domain is explicitly not markets-specific, and
the working directory path matches none of the cwd globs in
`rules/quant-project.md`, `rules/population-health.md`, or `rules/publishing.md`.
On path-rule grounds the indicated kind is `generic`. But `generic` omits
`research/00_literature_review/`, `research/01_hypothesis_register/`,
`hypothesis_backlog.md`, and `REVIEW.md` — the structures that most directly
serve a literature-compilation project that treats nulls as objects of study.

**Domain scope.** Whether to declare a topic roadmap, or to leave topic
selection open and constrain only method.

## Decision

**Kind is `quant`.** The quant layout is a strict superset of `generic` — 28
subdirs against 24, both counts observed directly from
`bootstrap_project.py --dry-run` at dotfiles HEAD
`f08015fb578247d040177b15e81200edc0710093` on 2026-08-21, and the 28 corroborated
by `manifest.subdirs`. The choice **forfeits nothing in directory structure**;
one *semantic* forfeit did materialize (the templated `CLAUDE.md` §Scope
misdescribed the project) and was repaired — directory-count supersetting does
not bound semantic forfeits, and the first draft of this ADR presented it as if
it did. It supplies
the literature-review and hypothesis-register directories, the append-only
hypothesis backlog, and `REVIEW.md`, which `/code-review ultra` injects as
highest-priority instructions into every review agent.

The kind selection does **not** activate `rules/quant-project.md`. Rule
activation in `~/.claude/CLAUDE.md` is cwd-glob based and this path matches no
glob. The quant time-series-integrity rules are therefore adopted here by
explicit reference in the charter where they apply, not by automatic
inheritance. This is deliberate: those rules are correct for any time-indexed
analysis, including non-financial ones, and are worth applying on their merits
rather than by path accident.

Two markets-specific directories — `config/instruments/` and `logs/promotions/`
— are accepted as inert overhead.

**Scope is unbounded in domain, bounded in method.** No topic roadmap. The
charter at
[docs/methodology/charter_castles_2026-08-21.md](../methodology/charter_castles_2026-08-21.md)
constrains how a question is worked and never which question is taken up.

## Alternatives considered

**`--kind generic` plus creating the four objects by hand** — the four filesystem
objects that are the entire stated reason for choosing `quant`
(`research/00_literature_review/`, `research/01_hypothesis_register/`,
`hypothesis_backlog.md`, `REVIEW.md`). This costs minutes and incurs none of the
reversal friction above. **Rejected because** hand-created structure drifts from
the bootstrap script's expected subdir set, producing `layout-drift` (exit 3) on
every subsequent idempotency check — the same argument used below to justify
retaining the two inert directories. Recording this alternative closes a gap:
the first draft named no alternative, which is not an honest decision record.

**Scope of the inertness claim.** `manifest.kind` was asserted inert because rule
activation is cwd-glob based. That is only bounded-checked: **no consumer of
`manifest.kind` other than `--migrate`'s guard was identified as of 2026-08-21**,
by inspection of `bootstrap_project.py` and this project's `CLAUDE.md`. Future
tooling may consume it.

## Consequences

**Positive**

- The hypothesis register and failure log give nulls a durable home, which is the
  project's central method rather than an afterthought.
- `REVIEW.md` is in place, so code review carries project standards from the
  first commit.
- Adopting quant rules by reference rather than by path means they are applied
  where they are *justified*, and their application is documented at each site.

**Negative**

- The templated `CLAUDE.md` §Scope was rendered with quant boilerplate that
  misdescribes the project. Amended in this session; the amendment is the
  authoritative text.
- `config/instruments/` and `logs/promotions/` will stay empty unless a
  markets thread needs them. Retained rather than removed, since removal would
  produce layout drift against the bootstrap script's expected set.
- Reversal cost is **low at bootstrap** — one `manifest.json` field, two empty
  directories, and the authored files — and **rises with content volume**. The
  binding obstacle is `--migrate`'s exit-2 guard, which is a script policy, not a
  data constraint. The first draft of this ADR called the cost "high", which
  overstated it and would have functioned to immunize the decision from revisit.
  **Re-evaluation trigger:** before the first `skie-v*` release tag, or when a
  non-markets thread becomes the primary output stream.

**Neutral**

- `manifest.json` records `bootstrap_script_git_head: f08015fb578247d040177b15e81200edc0710093`, so the
  layout is reproducible by checking out that SHA of the dotfiles repository and
  re-running.

## Identity

**Resolved 2026-08-21 by the author.** The initial `git init -b main` succeeded
but the bootstrap commit was skipped for want of a configured identity. The
choice between real-name and SKIE-pseudonym attribution was deferred to the
author because it has publishing consequences under `rules/publishing.md`.

**Decision (2026-08-21, revised same day):** real-name attribution for the
*author name*, with the real email address kept out of commit metadata.

```
user.name  = Sajan Koirala
user.email = 238704148+s-koirala@users.noreply.github.com
```

Repository-local config only; global git config was not modified. The initial
decision wrote the author's real address; it was revised before the first commit
was made, so **the real address never entered git history.** The noreply form is
GitHub's, resolved from the authenticated account id via `gh api user`, so
commits still attribute correctly on GitHub.

**Repository is public.** Chosen deliberately by the author. Name is public;
address is not.

**Consequences.** `rules/publishing.md` §Identity hygiene does not bind this
repository (no cwd-glob match, and the author has chosen real-name attribution).
The practical constraint that follows: this repository cannot be the origin of
pseudonymously published work, because its git history will carry the real
identity permanently. Any SKIE-attributed output must be authored in a separate
publishing-kind project. This is a one-way door — rewriting history after the
fact is possible but unreliable once anything is pushed.

Committing is now unblocked. Nothing has been committed yet; the first commit is
left to the author.
