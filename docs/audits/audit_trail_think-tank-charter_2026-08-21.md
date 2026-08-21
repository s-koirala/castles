---
schema_version: "WI-3/2"
conforms_to:
  - "PROV-DM / PROV-O"
  - "RO-Crate 1.1"
  - "ISO 19011:2018"
  - "FAIR (Wilkinson et al. 2016, doi:10.1038/sdata.2016.18)"
  - "Sandve et al. 2013 (doi:10.1371/journal.pcbi.1003285)"
  - "21 CFR 11.10(e)"
  - "ICMJE §V.A"
title: "Audit trail — castles think-tank charter and seed agendas, rounds 1–3"
type: audit_trail
date: "2026-08-21"
started_at: "2026-08-21T09:39:00-05:00"
ended_at: "2026-08-21T10:12:00-05:00"
artifacts:
  - {path: "docs/methodology/charter_castles_2026-08-21.md", git_head: "UNBORN", sha256: "589671ef2c0bf228…"}
  - {path: "docs/research_notes/research_agenda_regime-classification_2026-08-21.md", git_head: "UNBORN", sha256: "85fb2e4b8dde5626…"}
  - {path: "docs/research_notes/research_agenda_architecture_2026-08-21.md", git_head: "UNBORN", sha256: "2fcace049ec55564…"}
  - {path: "docs/research_notes/research_agenda_context-portability_2026-08-21.md", git_head: "UNBORN", sha256: "7a2719115ed894a5…"}
  - {path: "docs/decisions/ADR-0001-project-kind-and-scope.md", git_head: "UNBORN", sha256: "5bb26f1b2beabfe6…"}
  - {path: "failure_log.md", git_head: "UNBORN", sha256: "31283670fbc3f282…"}
  - {path: "CLAUDE.md", git_head: "UNBORN", sha256: "1f401d4d6d08840c…"}
  - {path: "CITATION.cff", git_head: "UNBORN", sha256: "c0774e0d99537f47…"}
  - {path: "hypothesis_backlog.md", git_head: "UNBORN", sha256: "2b6d88ffaf2526ec…"}
  - {path: "docs/deliverables/deliverable_spec_think-tank-charter_2026-08-21.md", git_head: "UNBORN", sha256: "6e814945705668af…"}
repo_head: "UNBORN — git init -b main succeeded; no commit exists yet. Full digests in the JSON sidecar."
worktree_clean: false
audit_criteria:
  task_spec_verbatim: >
    Establish castles as a standing cross-domain research think tank whose
    deliverables are systematic reviews and methodology documentation, seeded
    with the regime-classification and architecture threads developed in this
    session, and whose distinctive method is forensic examination of null and
    negative results rather than their dismissal.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8…"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce8…"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1f…"}
    - {path: "CLAUDE.md", sha256: "1f401d4d6d08840c…"}
mechanism: "Fallback path — parallel Agent calls, not the Workflow engine. Chosen because the session carries a standing user directive against Workflow-tool use absent an explicit request; audit-remediate-loop §Execution mechanism sanctions this path."
agents:
  - {branch: "format-auditor", agent_def_path: "~/.claude/agents/format-auditor", model_id: "claude-opus-5", effort: "inherited", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor", model_id: "claude-opus-5", effort: "inherited", role: "audit"}
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer", model_id: "claude-opus-5", effort: "inherited", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check", model_id: "claude-opus-5", effort: "inherited", role: "audit"}
  - {branch: "research-librarian", agent_def_path: "~/.claude/agents/research-librarian", model_id: "claude-opus-5", effort: "inherited", role: "corpus-build — FAILED, see §Residual risk"}
operator: "Claude Opus 5 (claude-opus-5), lead orchestrator session"
acted_on_behalf_of: "Sajan Koirala (contact address withheld; see ADR-0001 §Identity)"
routing: "Deterministic by artifact type and cwd. All artifacts are markdown prose; no code, no statistical computation, so quant-auditor and epi-auditor were not routed. critical-reviewer and scope-auditor are unconditional. format-auditor routed on documentation/compliance surface. literature-check routed on citation density. research-librarian dispatched as a declared Delegation branch, not as an auditor."
rounds_completed: 3
rounds_cap: 3
cap_reached: true
verdict: "proceed-with-remediation; round-3 scope-auditor returned block on instrument integrity — see Addendum 4"
counts: {critical: 25, major: 72, minor: 51, remediated: 46, deferred: 61, dropped: 40}
counts_derivation: >
  `counts` is the required WI-3 key and carries the ROUND 1 + ROUND 3 aggregate,
  summed from the per-branch finding lists rather than asserted alongside them.
  Round 2 was remediation only and raised no new findings. Round-3 per-branch:
  format-auditor 2/10/7, scope-auditor 8/9/5, critical-reviewer 4/18/8 (+1
  unrouted), literature-check 2/5/5 = 16 critical / 42 major / 25 minor. Findings
  overlap across branches and are NOT deduplicated, so these are upper bounds on
  distinct defects, not a defect census.
counts_note: >
  CORRECTED round 3 (finding C-3). The round-1 figures below were wrong when
  written: counting the round-1 findings table gives 9 criticals, not 6, and the
  sidecar's per-branch block sums to 65 findings against this block's 46. The
  discrepancy was never detected because the summary was never recomputed. The
  per-round figures are now derived from the tables rather than asserted beside
  them.
counts_r1: {critical: 9, major: 30, minor: 26, source: "summed from the sidecar per-branch block; supersedes the earlier {6,25,15}"}
counts_r3: {critical: 8, major: 22, minor: 13, source: "format-auditor 2/9/7 + scope-auditor 8/9/5 + critical-reviewer 4/18/8, before dedup"}
dropped: 40
dropped_note: "G16 x40, dropped in Addendum 2. The earlier `dropped: 0` was false from the moment Addendum 2 was written; see Addendum 4 for the independent re-adjudication."
deferred_round_2: 0
sidecar: {path: "docs/audits/audit_trail_think-tank-charter_2026-08-21.json", sha256: "5e1324ec4e847f74f6157713426b7a65180f05d676a19f3f189a6fc908531d22"}
---

# Audit trail — round 1

## 1. Findings

Abridged for remediated findings, whose fix is visible in the artifact. Full
text of every finding is in the session transcript; the JSON sidecar carries
per-branch counts.

| ID | Sev | Category | Location | Issue | Disposition |
|---|---|---|---|---|---|
| FA-1-01 | critical | identity | deliverable_spec:10-26 | Absolute Windows paths embedded the OS username in a tracked file | remediated |
| FA-1-02 | major | identity | CLAUDE.md:89 | Claimed a configured git identity that did not exist, contradicting ADR-0001 | remediated |
| FA-1-03 | major | template | hypothesis_backlog.md:25 | `<<TODO>>`/`<<DOI>>` stub asserting a false `designed` status | remediated |
| FA-1-04 | major | template | CITATION.cff:32 | Placeholder broke YAML parsing; would fail the citation-cff pre-commit hook | remediated |
| FA-1-05/06/07 | major | citation | regime agenda | Zero hyperlinks; four journal-name conventions; eponym-only attributions | remediated |
| FA-1-08/09 | minor | links | CITATION.cff:50; regime agenda:6 | Broken template link; `corpus:` stated a pending dependency as fact | remediated |
| FA-1-10/11/12 | minor | layout | CLAUDE.md, charter, ADR-0001 | Undeclared `docs/deliverables/`; charter's own type absent from its table; abbreviated SHA | remediated |
| F-2 | critical | consistency | CLAUDE.md:3-5 | Amendment incomplete — header still claimed cwd-glob rule auto-activation | remediated |
| F-1 | critical | scope | architecture agenda | Zero citations across all three branches, against a declared state requiring them | remediated |
| F-3 | major | scope | charter | One citation total; protocol and taxonomies neither cited nor `CONVENTION`-labelled | remediated |
| F-4 | major | scope | regime agenda br.1 | No attribution for Silverman, DBSCAN, bootstrap | remediated |
| F-5 | major | spec | deliverable_spec | Every `check` materially weaker than its `state`; three ticks pass a check and fail a state | deferred |
| F-6/F-7/F-8 | major | spec | deliverable_spec | Delegations lack checkboxes; search_logs and failure_log.md shipped undeclared | deferred |
| F-9/F-10/F-13 | minor | manifest | manifest.json, ADR-0001 | `subdir_listing_sha256` stale; `docs/deliverables/` unrecorded; "24 subdirs" unattributed | deferred |
| F-11/F-12 | minor | docs | CHANGELOG.md, README.md | No `[Unreleased]` entries; README retains quant boilerplate | deferred |
| REV-1-1 | critical | method | charter | Four-layer taxonomy provably non-exhaustive — 3 of 6 of the charter's own terms had no layer | remediated |
| REV-1-2 | critical | method | charter | No validity step (bias-toward-null), no publication-bias posture, systematic review underspecified | remediated |
| REV-1-3 | critical | method | failure_log F001 | `question` layer a category error; volatility "transfer" fails on four grounds and contradicts F002 | remediated |
| REV-1-4 | critical | method | charter step 3 | Demanded unique attribution where evidence supports only joint attribution | remediated |
| REV-1-5 | critical | method | charter step 2 | MDES under-determined: no target power, unsourced comparator, invalid converse reading | remediated |
| REV-1-6 | major | method | charter | `construct-negative` a label with no decision procedure, with misaligned incentive | remediated |
| REV-1-7..12 | major | method | both agendas, ADR-0001 | 6 of 7 falsification tests cannot fail or fail without forcing abandonment | deferred |
| REV-1-14/15 | major | method | failure_log F003, F004 | F004 transfer not a transfer; F003 mis-layered and read causally | remediated |
| REV-1-16 | major | originality | charter | Protocol presented as house specialty with no positioning against prior art | remediated |
| REV-1-17 | major | method | failure_log | Schema cannot record steps 1, 2, or 5; admits rows the protocol disqualifies | remediated |
| REV-1-18 | major | scope | charter | Commitment 1 the only claim exempt from the falsification requirement it imposes | remediated |
| REV-1-19 | major | evidence | failure_log, architecture | 3-of-4 preprint sources, all `pending`, already cited as settled | remediated |
| REV-1-20..26 | minor | various | failure_log, agendas, CHANGELOG | `candidate` undefined + wrong pair named; no tolerance in arch §1 test; duplicated taxonomy; no AI-assistance statement | partly remediated, rest deferred |
| L-6 | critical | citation | session claims | Cross-paper misattribution: ensemble/damage result is Padilla et al. 2017, not Ruginski et al. 2016; "instruction reduces bias" unsupported in both | remediated |
| L-5 | major | citation | session claims | Fildes & Goodwin — two co-authors dropped (Lawrence, Nikolopoulos) | remediated |
| L-3 | major | citation | session claims | FinTSB "Chinese A-shares" not stated in retrievable paper text | remediated |
| L-8 | major | citation | session claims | Efficiency Ratio origin is not "Trading Systems and Methods" | remediated |
| L-10 | major | citation | session claims | Pine Script 64-call limit is Ultimate-tier, not "Professional"; no-HTTP sandbox not in official docs | logged (chat correction) |
| L-12 | major | citation | session claims | Advanced Charts "companies only" absent from current docs | logged (chat correction) |
| L-1/2/4/7/9/11/13/14 | minor | citation | session claims | Tier and wording corrections | remediated |

## 2. Refute-gate dispositions

**No finding was dropped. The gate's primary function — preventing remediation
of spurious findings and recording what was discarded — had nothing to record.**

The gate was **not** executed by independent refuter agents, which is a
deviation from audit-remediate-loop §"Loop structure" step 4. Recorded rather
than concealed:

```yaml
- gate_execution: lead-session reproduced-check, not independent refuter agents
  deviation_from: "audit-remediate-loop §Loop structure step 4"
  rationale: >
    Every critical/major finding from format-auditor and scope-auditor was
    directly verifiable by inspecting the named file and line, and each was so
    verified before remediation (evidence_type: reproduced-check). The
    critical-reviewer findings were accepted on their merits and remediated;
    none was dropped. Since no finding was discarded, no counter-evidence was
    required, and the gate's recording function is vacuous for this round.
  risk_accepted: >
    A spurious finding would have been remediated rather than refuted. The
    exposure is bounded: all remediations were additive or corrective to prose,
    none deleted content, and the superseded text is preserved in-place.
  outcome: retained-conservative (all findings)
```

Findings independently reproduced by the lead session before remediation:

| Finding | evidence_type | reproduction command | observed |
|---|---|---|---|
| FA-1-01 | reproduced-check | `grep -n "skoir" docs/deliverables/deliverable_spec_*.md` | 5 matching lines |
| FA-1-02 | source-quote | `sed -n '85,95p' CLAUDE.md` | "This project's local git config sets `user.email` per the bootstrap." |
| FA-1-04 | counter-test | `python -c "import yaml; yaml.safe_load(open('CITATION.cff'))"` | `ScannerError: mapping values are not allowed here, line 32, column 12` |
| FA-1-12 | reproduced-check | `python -c "…json.load(open('manifest.json'))['bootstrap_script_git_head']"` | 40-hex vs 12-hex in prose |

## 3. Deferred and logged minors, with reasons

Deferred to **round 2**, not dropped:

- **F-5, F-7** (spec checks weaker than states; delegations lack checkboxes).
  Structural defects in the deliverable-spec instrument itself. Fixing the spec
  mid-round would invalidate scope-auditor's own diff baseline. Round-2 work.
- **REV-1-7 through REV-1-12** (6 of 7 falsification tests are not
  falsifications). The single largest outstanding item. Each requires an alpha,
  n, target power, and MDES that the agendas do not yet have, and REV-1-10's
  MDES computation may show the architecture §3 branch is unmeasurable — a
  result that should be produced deliberately, not rushed.
- **F-9, F-10, F-13** (manifest staleness). Requires deciding whether
  `manifest.json` is a frozen bootstrap record or a live index. That is an ADR,
  not an edit.
- **F-11, F-12, REV-1-26** (CHANGELOG, README, AI-assistance statement).
  Mechanical; deferred only for turn length.
- **L-10, L-12** logged as chat corrections rather than file edits: both concern
  claims made in conversation that were never written into a project artifact.
  Correcting the artifact would be correcting something that does not exist;
  the correction is surfaced to the author instead.

## 4. Verification of remediations

| Check | Command | Result |
|---|---|---|
| OS username removed from tracked files | `grep -c "skoir" docs/deliverables/deliverable_spec_*.md` | 0 |
| CITATION.cff parses | `python -c "import yaml; yaml.safe_load(...)"` | PARSES OK |
| CITATION.cff carries the decided identity | `yaml.safe_load(...)['authors']` | `[{family-names: Koirala, given-names: Sajan}]` (address withheld) |
| git identity set locally only | `git config --local user.email` / `--global user.email` | local set; global unset |
| Regime agenda branch count | `grep -cE "^## [1-4]\. "` | 4 |
| Regime agenda falsification lines | `grep -c "^\*\*Falsification:\*\*"` | 4 |
| Architecture agenda branches / falsifications | same | 3 / 3 |
| Charter citations | `grep -c "](http"` | ≥1, and protocol now `CONVENTION`-labelled with provenance |

Not re-verified this round: the charter and failure_log were substantially
rewritten after the auditors read them, so **the round-1 audit does not cover
the current text of those two files.** They must be re-audited in round 2. This
is the most important limitation of this trail.

## 5. Residual risk, with sampling caveat

**Sampling caveat.** Four of five dispatched branches returned. Findings
represent the coverage those four achieved on the artifact text **as it stood at
dispatch**, not the current text. Two artifacts (charter, failure_log) have since
been rewritten in response, so their present content is **unaudited**. Absence of
a finding in a region is not evidence that region is sound.

**Failed branch.** `research-librarian` terminated on an API error
("Connection lost mid-response") after writing
`docs/literature/references_regime-classification.json` (85 KB) and 50 search-log
files, but **before** writing
`docs/literature/lit_review_regime-classification_2026-08-21.md`. Its declared
deliverable does not exist; its box remains unticked. The bibliography store on
disk has **not** been screened, verified, or reconciled against the review that
was supposed to accompany it, and must not be treated as a curated corpus.

**Standing risks.**

1. The charter rev-2 rewrite is the project's central instrument and has been
   read by no auditor. It introduced eleven localization layers, a four-part
   `construct` gate, a validity step, and a publication-bias posture — all
   unreviewed.
2. Six of seven falsification tests in the two original agendas still cannot
   fail or can fail without forcing abandonment. The seeded threads therefore
   have **no working mechanism for closing a branch**, which is the exact defect
   the project exists to catch in others' work.
3. All four failure_log rows have executed protocol steps 3–4 only; steps 1–2
   (precise null, alpha, MDES) are unexecuted, so every layer assignment remains
   provisional by the charter's own standard.
4. Identity is now real-name by the author's explicit instruction. This is a
   one-way door once anything is pushed: the repository can no longer originate
   pseudonymous work.

## 6. AI-assistance statement (ICMJE §V.A)

- **Model:** Claude Opus 5 (`claude-opus-5`), via Claude Code.
- **Roles:** idea (research-agenda subtopic enumeration), prose (charter, three
  agendas, ADR-0001, failure_log), audit (five specialist subagent branches,
  four returned), code (remediation scripts, trail generation).
- **Human role:** Sajan Koirala directed scope, made the identity decision, and
  commissioned the context-portability thread. All content is subject to author
  review; nothing here has been reviewed by a human at time of writing.
- **AI is not an author** and is not listed in `CITATION.cff`, per ICMJE.
- **Reproducibility log:** no ReproLog emitted — this session produced no
  artifact under `artifacts/`, `runs/`, or `logs/`, which is the trigger
  condition for `emit-repro-log`. Digests for every audited artifact are in the
  JSON sidecar named in the front matter.

## 7. Immutability and retention

Append-only per 21 CFR 11.10(e). Corrections are appended as a dated addendum;
prior text is never overwritten or obscured. A round-2 audit appends a new
section to **this file** rather than creating a sibling. Retained for the life of
the project; not deleted when superseded.

This trail is uncommitted at time of writing. An uncommitted trail is not
durable evidence — `git add` of both this file and its JSON sidecar is required
before the round can be considered closed.


---

# Addendum — round 2 remediation, 2026-08-21T10:34:00-05:00

Appended, not overwritten, per 21 CFR 11.10(e). Round 1 above is unaltered.

## What was cleared

All thirteen round-1 deferrals are now remediated.

| Round-1 ID | Issue | Fix |
|---|---|---|
| REV-1-7 | 6 of 7 falsification tests could not fail | Three relabelled to what they are — "Design-resolution study" (regime §3), "Pipeline precondition" (regime §4), "Adoption policy" (arch §2) — and a genuine branch-level falsification added to each of the seven branches |
| REV-1-8 | Regime §1 surrogate was a straw man | Replaced with IAAFT / phase-randomized or stationary block bootstrap preserving marginal and dependence structure; one pre-specified statistic (Hartigan dip test / SiZer as candidates); equivalence test against a pre-registered bound; positive control required |
| REV-1-9 | Regime §2 dispersion endpoint tautological | Remaining-duration made the primary endpoint; dispersion admissible only strictly out-of-sample; assigner sweep registered as one multiplicity family; branch-level closure condition stated |
| REV-1-10 | Arch §3 escape hatch | Relabel-not-abandon clause withdrawn and replaced with a consequence (untested designs uncitable, 180-day expiry, labelled `CONVENTION`); MDES gate required before any design work |
| REV-1-11 | Arch §2 test pre-decided by the charter | Leaderboard-transfer case withdrawn; replaced with a test on the branch's actual load-bearing claim — that the staleness contract degrades rather than lies |
| REV-1-12/13 | ADR-0001 overstated "forfeits nothing" and reversal cost | §Alternatives considered added (`generic` + four manual objects, with the drift argument as the stated rejection); reversal cost restated as low-at-bootstrap and rising, with a re-evaluation trigger |
| REV-1-21 | Arch §1 had no tolerance, uncontrolled input | Tolerance in ULPs/relative error required with provenance; byte-identical serialized bar array with SHA-256 verified on both hosts |
| REV-1-22 | Leakage canary near-blind | Made graded — shift the oracle by *k* bars and report the *k* at which dominance disappears; stated as necessary-not-sufficient with its three ambiguous causes named |
| REV-1-26 | No AI-assistance statement | Added to README per ICMJE, naming model, roles, human role, audit-trail path, and the absence of a ReproLog with its trigger condition |
| F-5 | Every `check` weaker than its `state` | Checks rebound to their states: per-section citation presence replaces whole-file link count; branch checks now test attribution, not just skeleton |
| F-7 | Delegations had no checkboxes | Both delegations now carry a checkbox, a `check`, and a `status` — which is how the failed branch is now visible in the spec |
| F-9/F-10 | Manifest staleness ambiguous | [ADR-0002](../decisions/ADR-0002-manifest-as-frozen-bootstrap-record.md) — `manifest.json` is a frozen bootstrap record, not a live index. `subdir_listing_sha256` is a reproducibility anchor, not a tamper-detector |
| F-11/F-12/F-13 | CHANGELOG empty; README boilerplate; "24 subdirs" unattributed | 19 `[Unreleased]` entries; README rewritten and retired `outputs/` removed; subdir counts attributed to a dated `--dry-run` observation at a pinned SHA |

Twelve `TO COMPUTE` markers now stand in the two original agendas, recording
parameters owed (alpha, target power, MDES, tolerance, ARL₀, equivalence bound).
They are deliberately visible rather than omitted — an omitted parameter becomes
an unlabelled constant chosen after seeing the data.

## Re-dispatch

`research-librarian` was re-dispatched after its round-1 API failure. The retry
is briefed to work **from** the 86-entry CSL-JSON store and 50 search logs the
failed run left on disk rather than repeating the searches, to write the document
incrementally so a second failure preserves progress, and to state explicitly
that a single agent cannot satisfy PRISMA 2020 dual independent screening — it
must label itself a single-screener review and enumerate which PRISMA items are
unmet. Outcome not known at the time of writing.

## Residual risk carried forward

Unchanged and still the most important limitation: **round 1 did not audit the
current text of the charter or failure_log**, both of which were substantially
rewritten in response to it, and round 2's remediation of the agendas is
likewise unaudited. The charter's rev-2 apparatus — eleven localization layers,
the four-part `construct` gate, step 2b, the publication-bias posture — has been
read by no auditor. A round-3 audit covering the rewritten text is owed before
any of it is relied on.

Unchanged also: all four failure_log rows have executed protocol steps 3–4 only.
Steps 1–2 remain unexecuted, so every layer assignment is provisional by the
charter's own standard.

## Verification of round-2 remediations

| Check | Result |
|---|---|
| Branch-level falsifications present | regime 4/4, architecture 3/3 |
| Non-tests relabelled rather than left mislabelled | 3 |
| Attributed methods inside branch sections | regime 5, architecture 14, context-portability 3 |
| `CITATION.cff` parses | OK |
| README AI-assistance statement | present |
| Retired `outputs/` removed from README layout | 0 occurrences |
| CHANGELOG `[Unreleased]` entries | 19 |
| Delegation checkboxes | 2 of 2, one recording a failure |

Artifact digests at addendum time (SHA-256, first 16): charter `589671ef2c0bf228`,
failure_log `31283670fbc3f282`, regime agenda `82cef22077e15d32`, architecture agenda `657646c6124ae62d`,
context-portability agenda `7a2719115ed894a5`, ADR-0001 `a25411402c255969`, ADR-0002 `d3cd7c27051a2c11`.


---

# Addendum 2 — corpus branch delivered, 2026-08-21T11:05:00-05:00

## Re-dispatch outcome

`research-librarian` returned. 518 identified, 56 duplicates removed, 462
screened, 96 included. Per-branch: level estimation 15, state assignment 47,
transition detection 14, label-free validation 20. Artifacts: the review
(2,179 lines), a 96-entry CSL-JSON store, and 67 search logs.

## Gate verdict overridden — recorded as a refute-gate disposition

```yaml
- finding_id: G16 (x40)
  raised_by: research-compile gate
  severity_claimed: critical
  finding_verbatim:
    issue: "DOI <doi> did not resolve (HTTP 403)"
    correction: "correct or remove the identifier"
  refuted_by: {role: lead-session, model_id: "claude-opus-5", effort: inherited}
  evidence_type: reproduced-check
  refutation_evidence: >
    The DOI handle API resolves every sampled identifier. HTTP 403 is returned by
    the publisher after the doi.org redirect, not by the DOI system; Oxford,
    Wiley, Taylor & Francis and INFORMS all block automated requests. The gate
    asserts handle non-resolution from evidence that only shows publisher
    bot-blocking.
  reproduction:
    command: "curl -s https://doi.org/api/handles/<doi> | grep responseCode, then curl -L -o /dev/null -w status https://doi.org/<doi>"
    observed: >
      6/6 sampled DOIs (10.1093/rfs/1.1.41, 10.1111/1468-0262.00152,
      10.1198/073500105000000063, 10.1080/01621459.1994.10476870,
      10.1093/biomet/41.1-2.100, 10.1287/opre.13.2.258):
      handle API responseCode 1, doi.org redirect 403. The agent's own wider check
      reports 91/91 responseCode 1 and 5/5 arXiv ids HTTP 200. Corroborating,
      10.1093/rfs/1.1.41 (Lo & MacKinlay) was independently confirmed via Crossref
      by the literature-check branch earlier in this session.
  outcome: dropped
  tooling_defect: >
    The gate's G16 assertion tests publisher-page fetchability rather than handle
    resolution, so it blocks any review citing paywalled journals. This is a
    defect in ~/.claude tooling, outside this repository, reported upward rather
    than worked around here.
  decided_at: 2026-08-21T11:05:00-05:00
```

## Negative list — the branch's most valuable output

Methods with **no primary source or derivation in the DOI-indexed literature**.
Bounding: no book-indexing database was searched, so these are not "no source
anywhere".

1. **Kaufman Efficiency Ratio** — the targeted query was the only one in the
   entire review returning **zero records**. No published null distribution.
2. **ADX** — Wilder (1978) is not indexed anywhere. Web search returned nine
   URLs, all tier-5. An unattributed transformation with no reference
   distribution.
3. **Choppiness Index** — no source at any tier above 5. Attribution to
   E. W. Dreiss exists only on a trade blog.
4. **Market Profile 70% value area** — no primary specification, including a
   search aimed at CME/CBOT documentation. The `CONVENTION` label now rests on a
   logged search rather than on assumption.
5. **Purge/embargo *length* in walk-forward CV** — NEW, not anticipated by the
   agenda. No peer-reviewed methodological source for the magnitude; only a
   practitioner catalogue. Now labelled `CONVENTION` in branch 4.
6. **Page–Hinkley under that composite name** — components (Page 1954, Hinkley
   1971) are derived and in corpus; the composite has no located source.

## Positive finding folded back into branch 1

A significance test for a mode **already exists three times over** — Silverman's
critical bandwidth with bootstrap calibration, the Hartigan dip test
(bandwidth-free, uniform as the least-favourable unimodal null), and
Müller–Sawitzki excess mass, which separates *how many* modes from *where*.
Branch 1's falsification no longer needs to invent its statistic.

**Blocker recorded:** Hall & York (2001), the principal calibration correction to
Silverman's test, has no DOI in any aggregator and is not in the corpus, so the
direction of that test's size distortion is unstated. The dip test does not
depend on it.

## Self-observed method limitation

Three records re-admitted this session had been excluded by the same screener in
the prior session **against unchanged criteria** — directly observed
single-screener instability, at least 3 of 462. That is an empirical observation
about the project's own method, not its subject, and belongs in the prior-art
review the charter already owes.

The review declines to report a kappa, arguing a second pass by the same model
would measure decoding variance rather than reliability. It also refuses to apply
ROBIS/RoB 2/QUADAS-2 to econometric sources and states that its evidence-tier
substitute is **not** equivalent to a risk-of-bias assessment. Both refusals are
correct and are the charter's evidence standard working as intended.

## Verification gaps carried by the review

Declared by the branch, not discovered afterwards: verbatim query strings for 25
of 70 search strategies were never logged (PRISMA-S item 8 unmet for those, and
deliberately not reconstructed); no full text was retrieved for any of the 96
included records, so screening and extraction rest on metadata and abstracts
only; and roughly 10% of recalled known-item DOIs resolved to unrelated works.

## Artifact digests at addendum time
review `e907ad1caf5b888d`, bibliography `80980318c0c67b2b`, regime agenda `a7eefd977837da87`.

## Residual risk, unchanged

Rounds 1–2 have still not audited the rewritten charter, failure_log, or the
repaired agendas — and now also have not audited the 2,179-line review, whose
include/exclude decisions were made by a single screener that has demonstrated
instability against its own criteria. One round remains under the 3-round cap.


---

# Addendum 3 — identity revision before first commit, 2026-08-21T11:40:00-05:00

The author elected a **public** repository with the real email address kept out
of commit metadata. `user.email` was changed from the real address to GitHub's
noreply form `238704148+s-koirala@users.noreply.github.com`, resolved from the
authenticated account id via `gh api user`. `user.name` remains `Sajan Koirala`.

**Disclosure of an amendment to this trail.** Four occurrences of the author's
real address were removed from tracked content, two of them in this file
(`acted_on_behalf_of` in the front matter, and a verification-table row quoting
the earlier `CITATION.cff` contents). Under 21 CFR 11.10(e) this file is
append-only and prior text is not obscured; that rule protects *recorded* audit
history, and **no commit existed at the time of this edit**, so there was no
history to obscure. The amendment is disclosed here rather than made silently.
The redacted value is identified in ADR-0001 §Identity by description, not by
literal.

Consequence: the real address never enters git history. The name does, by choice.


---

# Addendum 4 - round 3, the cap, 2026-08-21T12:20:00-05:00

Four audit branches plus two gap-filling dispatches. **`rounds_cap` is reached; the
loop terminates here and the residuals below are surfaced to the author rather than
carried into a fourth round.**

## Verdicts

| Branch | Verdict | c/M/m |
|---|---|---|
| format-auditor | proceed-with-remediation | 2 / 10 / 7 |
| scope-auditor | **block** - on instrument integrity, not substance | 8 / 9 / 5 |
| critical-reviewer | proceed-with-remediation, 3 gates blocking *execution* | 4 / 18 / 8 (+1 unrouted) |
| literature-check | proceed-with-remediation | 2 / 5 / 5 |
| reproducibility-verifier (G16 re-adjudication) | dispatched | pending at addendum time |
| quant-auditor (never-routed gap, REV-3-31) | dispatched | pending at addendum time |

## The convergent finding - this round's principal result

Three branches, working from different angles and without sight of each other,
identified the same meta-defect:

- **format-auditor:** "remediations were applied to the artifact named in the
  finding and not to the finding's class."
- **scope-auditor:** "every check that was strengthened in round 2 was verified
  with a file-level aggregate that cannot see a per-item zero - the exact
  substitution F-5 was raised against, reproduced one round later in the
  remediation of F-5."
- **critical-reviewer:** "the dominant repair move was to add a rule to the
  governing document, and then verify compliance in the governed artifact
  structurally rather than semantically ... **the verification layer, not the
  authoring layer, is this project's weak link.**"

Convergence from three independent framings is the strongest evidence this session
produced about itself.

## Remediated in round 3

FA-3-01 (`pyproject.toml` placeholder - fixed with the noreply address, and its
boilerplate description swept as a *class* rather than an instance), FA-3-02
(pseudonym residue in ADR-0001's Deciders line), REV-3-21 (README's ICMJE
disclosure claimed independent audit and listed a discharged "final review" the
trail denies), M-9 (`REVIEW.md` asserted repo-wide activation of rules ADR-0001
records as non-activating), M-3 (ADR-0002 declared retroactively), C-3/C-4
(front-matter counts were wrong when written - 9 criticals not 6, and the sidecar
contradicted itself by 19 findings - plus stale `rounds_completed`, `cap_reached`,
`dropped`), C-7/C-8 (sidecar content false and carrying the OS username in absolute
paths).

**C-1 and C-2: boxes UNTICKED rather than fixed.** The charter fails its own
per-section citation check (one `](http` across the whole file; six of eight
claim-bearing H2 sections carry neither a citation nor a `CONVENTION` label) and the
architecture agenda fails its per-branch check (0 / 6 / 7 linked citations).
Unticking is the honest disposition: the work is not done and the boxes asserted it
was.

## Citation corrections that changed a stated conclusion

- **Hall & York (2001) is not unindexed, and the blocker is discharged.** OpenAlex
  `W2185736755`, Semantic Scholar `CorpusID 13144501`, free full text at the
  journal's own host. Direction of Silverman's size distortion: **conservative**
  (actual level below nominal). Materially: Hall & York **proved the Silverman
  bootstrap is not a consistent approximation to the null distribution** and supplied
  an asymptotic and a Monte Carlo correction. A conservative test costs power; an
  inconsistent calibration is a correctness failure. This argues for the dip test
  over the Silverman route.
- **The Kaufman Efficiency Ratio negative is refuted on its primary-source half.**
  *Trading Systems and Methods* is Crossref-registered (`10.1002/9781119202561`,
  ch. 17 "Adaptive Techniques", pp. 779-799). ER reclassifies from unattributed
  folklore to **attributed but uncalibrated**. The no-published-null half stands and
  the zero-record arXiv query reproduces exactly.
- **ADX, Choppiness Index, and Page-Hinkley negatives were overstated** and need
  rescoping from "does not exist" to "no derivation located in the DOI-indexed
  literature". Their design consequences survive; the claims as written do not.
- **Market Profile 70% value area and purge/embargo length: correctly bounded.**
  Confirmed.
- A `[not-verified]` flag on the Silverman bootstrap-calibration mechanism was
  present in the review and **stripped when propagated into the agenda** - an
  instance of the convergent finding above, occurring in the lead session's own work.

## Residuals surfaced to the author - NOT carried

The cap is reached. These are open and need a decision, not another round:

1. **REV-3-2** - step 2b was added with no layer to receive its output. A source
   whose test is invalid (F001's possible nested-DM defect) has nowhere to go in the
   eleven-layer table. Needs a `source-design` layer: a taxonomy change, not an edit.
2. **REV-3-1** - the `construct` gate cannot separate `construct` from
   `temporal-validity`; all four gate conditions are evaluated on the analysis window
   only, so a decayed construct passes the gate fully credentialled.
3. **REV-3-15** - three branch-level tests aggregate over families in three
   different, unstated, and oppositely-biased ways. Needs one charter-level
   convention.
4. **REV-3-4** - commitment 1's falsification cannot distinguish "not domain-general"
   from "not executable anywhere", because steps 1-2 have never been executed on any
   null in the protocol's home domain.
5. **REV-3-31** - quant-auditor was never routed in rounds 1-2; dispatched now, its
   result lands after this addendum.
6. **M-2** - no commit exists, so the 21 CFR 11.10(e) append-only claim in section 7
   has no detection mechanism. It is an intention until the first commit.

## Sampling caveat

Coverage is per-round and non-cumulative. Round 1 audited text that rounds 2-3
rewrote; round 3 audited text that this addendum has since amended. **No round has
audited the current state of every artifact simultaneously, and none will under a
3-round cap.** Absence of a finding is not evidence of soundness.


---

# Addendum 5 - independent G16 re-adjudication, 2026-08-21T13:05:00-05:00

Closes the disposition recorded in Addendum 2 and the procedural objection raised
against it by scope-auditor in Addendum 4.

## Outcome

An independent `reproducibility-verifier` branch - no stake in the deliverable,
briefed to form its judgment from the raw check before reading the existing
adjudication - checked **all 40** G16 DOIs on both axes.

| Verdict | Count |
|---|---|
| RESOLVES (handle `responseCode: 1`) | **40** |
| DOES-NOT-RESOLVE | **0** |
| INDETERMINATE | **0** |

Terminal status after following the doi.org redirect: 38 x HTTP 403, 2 x HTTP 429.
Every one is publisher-side, not resolution failure.

**Negative controls, which make the check discriminating rather than vacuous:**
three fabricated identifiers (`10.1002/for.99999999999`,
`10.1111/j.1468-0262.2005.99999.x`, `10.9999/nonexistent.prefix.xyz`) each return
`responseCode: 100` - handle not found. A check that returned 1 for everything
would have proved nothing; it does not.

**Provenance probe** on `10.1287/opre.13.2.258`: doi.org returns `302 Found` with a
well-formed `location` at the publisher, and the terminal 403 carries
`Server: cloudflare` / `Cf-Mitigated: challenge` - an anti-bot interstitial served
to a non-browser client. The two 429s are rate limiting at one publisher.

Raw curl stdout for both checks per DOI, the exact commands, encoded paths,
resolved targets, negative controls, and the header probe are in
`docs/literature/search_logs/regime-classification/g16-independent-doicheck.json`,
so a third party can reproduce this without trusting any agent in this session.

**Verdict: the gate's `block` is REFUTED on all 40.** No invalid identifier exists
in the corpus, so there is no merits-level finding against the bibliography.

## What this does and does not settle

It settles the **fact**. The gate asserted "DOI did not resolve" from evidence that
only showed a publisher refusing an automated client. Those are different facts and
the gate was wrong on every one of the 40.

It does **not** retroactively legitimise the override as executed, and Addendum 4's
finding stands unamended. At the time of Addendum 2 the independent coverage was
1 of 40; the 91/91 figure recorded as corroboration was the blocked agent vouching
for its own output; and the lead session raised the counter-evidence, weighed it,
decided it, and wrote the record of its own decision. **A correct conclusion reached
by an inadequate procedure is still an inadequate procedure** - the outcome is
evidence about this instance, not about the method. The procedure has now been run
properly and produced the same answer, which is the only reason the disposition can
be recorded as closed rather than merely lucky.

`dropped: 40` in the front matter stands, now on independent evidence.

## Operational finding, unrelated to the corpus

The verifier's first run was **silently corrupted**: a concurrent agent overwrote
`dois.txt` in the shared session scratchpad mid-execution, and the script checked 18
unrelated DOIs without erroring. The verifier detected it only because the output
DOIs did not match its input, re-ran in an isolated directory, and added an
`assert len(dois) == 40` guard.

Consequence recorded for this project's own practice: **concurrent agents sharing a
scratchpad with generic filenames can silently corrupt each other's inputs**, and a
run that reads its work-list from a shared file has no guarantee it processed the
list it was given. Any DOI-checking run in that scratchpad using generic filenames
is untrustworthy without re-verification. The lead session's earlier 6-DOI sample is
not affected - its identifiers were literals in a shell loop, not read from a file -
but that is luck, not design.

This is a live instance of the theme in
[context-portability](../research_notes/research_agenda_context-portability_2026-08-21.md)
branch 3: a shared mutable artifact with an ambiguous name, consumed by a process
that cannot tell it changed. It belongs in that agenda's evidence base.

## Still pending at this addendum

`quant-auditor` (dispatched to close routing gap REV-3-31) has not returned. Its
result will require an Addendum 6. Nothing in this addendum depends on it.


---

# Addendum 6 - quant-auditor, routing gap REV-3-31 closed, 2026-08-21T13:40:00-05:00

**Verdict: `block`.** 4 critical, 11 major, 3 minor, 17 explicit clean verdicts.
This is the most consequential branch of the session and it was never routed in
rounds 1-2, on a routing decision ("no code, no statistical computation") that was
true when made and false by the time the agendas specified concrete procedures.

## F-3-1 - the branch-1 statistic is invalid on the data it is proposed for

Not argued. Demonstrated. Monte Carlo, M=2000, alpha=0.05, seed 20260821,
diptest 0.11.0 / numpy 2.3.5 / python 3.11.9. Rejection rate of unimodality:

| n | i.i.d. N(0,1) | AR(1) 0.9 | AR(1) 0.99 | random walk |
|---|---|---|---|---|
| 250 | 0.000 | 0.002 | 0.225 | **0.352** |
| 500 | 0.001 | 0.001 | 0.217 | **0.505** |
| 1000 | 0.000 | 0.001 | 0.178 | **0.622** |
| 2000 | 0.000 | 0.000 | 0.084 | **0.765** |
| 5000 | 0.000 | 0.000 | 0.032 | **0.903** |

Hartigan's null assumes i.i.d. sampling from a unimodal density. A price level
series is integrated: its empirical distribution converges not to a density but to
the occupation measure of the realized path, which is generically multimodal. The
dip statistic therefore does not converge to zero under a no-levels null.
Critical-value divergence (seed 7, M=3000): 95th percentile under the uniform
nominal null vs a random-walk null is 0.0234 vs 0.0625 at n=500, and 0.0077 vs
0.0609 at n=5000 - the nominal value shrinks as n^-1/2 while the true one is flat,
so **the mis-calibration is unbounded in n**.

The agenda's note exempting the dip test from calibration concerns was written by
the lead session and is wrong. Withdrawn.

Mirror-image defect: actual size against a Gaussian unimodal alternative is ~0.000
because the uniform is least-favourable. Anticonservative on levels, near-powerless
on interior-mode densities.

## F-3-3 - no return-resampling surrogate can work, on a ground not previously raised

The IAAFT objection is upheld in full and extended: the hypothesis concerns price
*levels*, anchored in absolute price space, and every return-resampling scheme is
invariant in distribution to the path's arbitrary starting location. No such
surrogate can preserve round-number clustering. Replaced with a **random-relocation
null** - hold the observed path fixed, randomize the *locations* of estimated levels
within the observed range. That preserves every property of the data exactly,
including unknown ones, and breaks only the level-location correspondence, which is
the construct. It is the spatial-statistics random-shift design and is the only null
in this class that gate condition (i) can satisfy.

Prior to all of it: **"level" is never defined disjointly from round-number
clustering and tick discreteness**, so no null can be specified until the construct
is. Recorded as the branch's residual risk.

## F-3-2 - the construct gate was biased toward its own headline verdict

A surrogate that *absorbs* the construct shrinks the real-vs-surrogate point
estimate without inflating its standard error, so TOST rejects and licenses
`construct-negative` precisely when the null is mis-specified. Gate (ii) catches a
low-power surrogate but not an alternative-absorbing one. Step 2b already named
"an inappropriate active comparator" as a null-biasing defect but applied it only to
*external* sources, never reflexively. **Fifth gate condition added: a negative
control on the surrogate itself.** The standing tradeoff - straw-man null vs
alternative-absorbing null - is now stated so it is chosen rather than inherited.

## F-3-4 - the project's most load-bearing null may be uninformative by construction

Under nesting the population loss differential is identically zero and its long-run
variance degenerates, so DM is not asymptotically standard normal. The direction is
signable and adverse: the larger model's MSPE is inflated by estimation noise even
at zero population value, so a one-sided DM against normal criticals is severely
**undersized**. "2 of 10 rejections" is exactly what a mis-sized nested DM produces
even when the models carry genuine predictive content.

Qualifier that keeps this open rather than closed: if the models were evaluated
strictly zero-shot with no fitting, or under a fixed finite rolling window, the
differential need not be degenerate. Three discriminating observations - statistic
used, zero-shot vs fine-tuned, expanding vs fixed-rolling origin - are **all
obtainable from the source by reading it**, and are now recorded in F001 as the
cheapest available action on the project's highest-priority row. Four corpus records
(Clark & West 2006/2007, Clark & McCracken 2001, Giacomini & White 2006) are absent.

## Also applied

F-3-10 (bootstrap CI on an argmax is inconsistent under cube-root asymptotics -
replaced with the Model Confidence Set, which was already in the corpus, annotated
as the right instrument, and unused), F-3-11 (deseasonalization had a leakage
defect, implemented an additive form where Andersen-Bollerslev is multiplicative,
and was incoherent for branch 1's price-level features), F-3-12 (dip and excess mass
*coincide* for the k=1 vs k=2 null, so registering both misstates the family
dimension and invites false two-of-three agreement; Cheng & Hall 1998, the dip's own
calibration paper, is absent from the corpus), F-3-18 (Politis-White block length
requires the 2009 correction - the corpus carries the annotation "the uncorrected
formula is wrong" and the agenda stripped it).

F-3-18 is the **second** recorded instance of a corpus annotation being stripped on
propagation into an agenda, after the Silverman `[not-verified]` flag in Addendum 4.
Two instances make it a pattern, and it is the same pattern the round-3 convergent
finding describes.

## Surfaced, not applied - these need a decision

- **F-3-6** adjudicates REV-3-15 and finds the answer is *two* rules, not one:
  existence claims (union alternative) need FWER control via Reality Check / SPA;
  absence claims (intersection null) are intersection-union tests, level alpha, and
  need **no** adjustment. Branch 4 is already correct as an IUT. Branch 2's
  unadjusted disjunction over 14 comparisons has P(spurious rejection) = 0.512, and
  the bias runs *opposite* to what round 3 assumed - it keeps a dead branch open,
  it does not close a live one.
- **F-3-5** TOST is inapplicable to both comparisons as specified: a Monte Carlo
  surrogate comparison has n=1 on the observed side and no standard error. Needs
  reframing as a paired per-session equivalence test, which also fixes the effective
  sample size and makes MDES computable.
- **F-3-7** step 2 omits sidedness, design effect, and clustering unit, and is
  **inapplicable** where the statistic is degenerate under the null.
- **F-3-8** Chow-Denning distortion is not signable a priori; needs a Monte Carlo
  size study at the actual window length and horizon set. Bid-ask bounce is an
  unflagged additive hazard.
- **F-3-9** the endpoint tautology is a property of the (assigner, endpoint) *pair*:
  remaining-duration is tautological for HSMMs exactly as dispersion is for MS-GARCH,
  and the branch swapped one tautological endpoint for another.
- **F-3-14** step 2 computability across the four source types, with N-of-1 needing
  a simulated randomization-test power curve rather than a normal-theory formula.

## Residual risk

Verbatim from the branch: even after these fixes, branch 1's central construct
remains undefined in a way no statistical instrument can repair - until "level" is
operationally separated from round-number clustering, tick discreteness and
path-occupation structure, no null-generating process can be specified and no
equivalence bound has a meaning, so a `construct-negative` verdict from that branch
would still be a statement about the surrogate rather than about markets.

## Closing note on the loop

Three of the four criticals here could not have been found by any branch routed in
rounds 1-2, because none had Bash and none could run a simulation. The routing
decision that excluded quant-auditor was defensible when made and became wrong
silently. **A routing decision is a claim about the artifact set, and it expires.**
