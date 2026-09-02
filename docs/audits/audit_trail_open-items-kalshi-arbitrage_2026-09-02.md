---
schema_version: WI-3/2
conforms_to: skills/audit-remediate-loop/SKILL.md §"Audit-trail field spec"
title: Session audit trail — open items close-out and the Kalshi/binary-event-market branch
type: audit_trail
date: 2026-09-02
started_at: 2026-09-02T09:54:52-05:00
ended_at: 2026-09-02T16:40:00-05:00
artifacts:
  - {path: docs/literature/lit_review_explosive-regime-dating_2026-08-24.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 1760be0c6288878d}
  - {path: docs/literature/references_explosive-regime.json, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 13c76d8fd56ff86e}
  - {path: docs/research_notes/research_agenda_regime-classification_2026-08-21.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 31473c70c51d6d4c}
  - {path: docs/methodology/protocol_explosive-regime-review_2026-08-24.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 9d400eb557680d39}
  - {path: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 4ee8ef348fbd5c19}
  - {path: docs/literature/references_kalshi-arbitrage.json, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: fb0cf87ed53dcb0b}
  - {path: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 21a77d10841ba7f1}
  - {path: docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: 51034c44e6e21b5f}
  - {path: docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md, git_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f, sha256: f9659fa7e1054389}
repo_head: 27d74738aa35ec1cdf1ec6915b50532e3620ea6f
worktree_clean: false
audit_criteria:
  task_spec_path: docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md
  task_spec_sha256: 2c0ac94cc893c84e
  task_spec_verbatim: >
    Close every open item carried by this project — the four unchecked Phase 2
    explosive-regime deliverables and the two standing round-3 audit failures —
    and open a new prediction-market branch with a registered literature search
    on arbitrage and market-making in binary event markets (Kalshi-specific
    where the literature supports it).
  consulted:
    - {path: CLAUDE.md, sha256: 2d37579a3e967ea7}
    - {path: REVIEW.md, sha256: fd766934cb4709d7}
mechanism: Workflow engine — .claude/workflows/audit-remediate.js, one invocation per round
agents:
  - {branch: critical-reviewer, agent_def_path: ~/.claude/agents/critical-reviewer.md, model_id: claude-opus-5, effort: high, role: argument review}
  - {branch: scope-auditor, agent_def_path: ~/.claude/agents/scope-auditor.md, model_id: claude-opus-5, effort: high, role: spec-vs-delivery diff}
  - {branch: quant-auditor, agent_def_path: ~/.claude/agents/quant-auditor.md, model_id: claude-opus-5, effort: high, role: method fidelity}
  - {branch: literature-check, agent_def_path: ~/.claude/agents/literature-check.md, model_id: claude-opus-5, effort: high, role: citation verification}
  - {branch: reproducibility-verifier, agent_def_path: ~/.claude/agents/reproducibility-verifier.md, model_id: claude-opus-5, effort: high, role: repro envelope + attestation}
operator: claude-opus-5 (lead session, orchestrator)
acted_on_behalf_of: Sajan Koirala
routing: deterministic from extensions, cwd globs and flags; quant-auditor selected over epi-auditor (neutral cwd default); reproducibility-verifier added from round 2 onward
rounds_completed: 5
rounds_cap: 3
cap_reached: true
verdict: proceed-with-remediation (Thread A, cap reached); block (Thread C, round 2, remediated but unverified)
counts:
  audit_rounds: 5
  agents: 184
  raw_critical: 5
  raw_major: 146
  raw_minor: 95
  refuted: 11
  remediated: 140
  minors_logged: 95
sidecar: {path: docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.json, sha256: 4a8520439ca9de0e2a9b0bd8abf218ea36c61059b386a515e45545bbaf966a32}
---

# Session audit trail — open items + Kalshi branch

This is the **session-level** trail required by the declaration's Thread D. The
per-round finding tables, refute-gate dispositions and logged minors live in the
two thread trails, which this file indexes rather than duplicates:

- [audit_trail_phase2-explosive-review_2026-08-24.md](audit_trail_phase2-explosive-review_2026-08-24.md) — Thread A, rounds 1–3
- [audit_trail_kalshi-arbitrage-review_2026-09-02.md](audit_trail_kalshi-arbitrage-review_2026-09-02.md) — Thread C, rounds 1–2

## 1. Findings table

Per-finding rows with all eight schema fields, branch, disposition and
remediation reference are in the two thread trails and their JSON sidecars.
Session totals: **5 critical, 146 major, 95 minor raised across five rounds;
11 refuted at the gate; 140 remediated; 95 minors logged, not remediated.**

Every critical was retained except by explicit counter-evidence:

| id | thread | round | issue | disposition |
|---|---|---|---|---|
| QUANT-1-1 | C | 1 | 98.3% of screening dispositions produced by an undeclared keyword classifier, presented as individual reading | remediated — complied with, reproduced under `PYTHONHASHSEED=0`; amendment A10 |
| REV-1-2 | C | 1 | Kalshi's trading mechanism asserted order-driven and quote-driven in the same section, both sourced to a record denying it | remediated — both assertions removed; G-3 marks 2 → 6 |
| REV-1-1 | C | 1 | S4 headline a universal negative the corpus cannot state | **refuted** |
| QUANT-2-1 | C | 2 | the round-1 withdrawal over-corrected into a new false claim about the artifact's own queries | remediated — token inventory mechanically derived; A15 |
| LITERATURE-2-1 | C | 2 | same defect, independently raised | remediated with QUANT-2-1 |

## 2. Refute-gate dispositions

Recorded verbatim per finding in the two thread trails. Session gate metrics:

| round | thread | raw critical+major | killed by gate | kill rate |
|---|---|---|---|---|
| 1 | A | 27 | 3 | 11.1% |
| 2 | A | 30 | 0 | 0.0% |
| 3 | A | 17 | 1 | 5.9% |
| 1 | C | 41 | 4 | 9.8% |
| 2 | C | 36 | 3 | 8.3% |
| **total** | | **151** | **11** | **7.3%** |

**Calibration note, recorded because it matters for the gate's own evaluation.**
The skill cites ~79–83% adversarial kill rates as directional
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). This session ran at
**7.3%** — an order of magnitude lower. Two readings are available and the
evidence here does not separate them: either the auditors were unusually
accurate on documentary artifacts, or the refuters were insufficiently
adversarial. The round-2 Thread A result (30 raised, **zero** killed) is the
sharpest single datapoint. This is an input to the gate-recall calibration in
`~/.claude/skills/audit-remediate-loop/evals/`, not a finding about these
deliverables.

## 3. Deferred and logged minors

95 minors were logged and not remediated, per the skill's triage rule (drop
minors unless the task invites polish; this task did not). They are enumerated
per round in the thread trails. None was re-raised as major by a later round.

## 4. Verification of remediations

Verified by the lead session, independently of the remediating agent:

| claim | method | result |
|---|---|---|
| explosive-regime protocol frozen prefix intact | `sha256(first 51,478 bytes)` | `33c01c5225…` — **matches**, append-only respected across A4–A14 |
| Kalshi protocol frozen prefix intact | `sha256(first 82,677 bytes)` | `99524df026…` — **matches**, append-only respected across A1–A15 |
| corpus store I3 GAP notes | parse + count | 7 of 72 — **matches** the corrected count |
| Kalshi store parses | `json.load` | 149-entry list |
| ReproLog pip-freeze digests | `sha256(bytes on disk)` | **failed initially**, see §5; corrected and re-verified |
| trail front-matter completeness | key-presence check | 22/22 on both thread trails |

**Not verified: everything written after Thread A round 3 and after Thread C
round 2.** Those passes had no audit round behind them. This includes the
Thread A round-3 remediation in full, the Thread C round-2 remediation in full,
the lead's agenda corrections of the same rounds, and the lead's
`.gitattributes` change. They are recorded as delivered, not as checked.

## 5. Residual risk

**Sampling caveat.** These findings come from LLM auditors sampling artifacts,
not from exhaustive verification. Absence of a finding in a region is not
evidence that the region is correct. Two independent demonstrations of this from
within the session: the Thread A round-3 re-read of three texts found four
locator errors and one misattributed theorem that **no auditor in three rounds
had raised**; and the Thread C round-2 remediation found 27 wrong years where
the audit had said ~20, and 19 records missing claim lines where the audit had
said 3.

### 5.1 The dominant residual — verification is not converging

Three false claims appeared inside Thread A round-1's fixes, four inside round
2's, each found by the following round. **Nothing checked round 3, and nothing
checked Thread C round 2.** The round-over-round error rate in remediation did
not fall. Any statement introduced by those two passes carries the same prior
of error as the statements the earlier rounds caught, and no mechanism in this
session estimated that prior.

### 5.2 Thread A — explosive-regime review

- **7 of 72 records have been re-read at full text across three rounds.** The
  measured locator error rate on re-read texts is 19 (Phillips line) + 4 (NB
  line). There is no basis for assuming the ~60 un-re-read records are cleaner.
  §7.2, §7.5, §7.6 and §7.7 were never re-read at any round.
- 280 records (47.8% of those reaching full text) excluded because full text was
  unobtainable; direction unknown, magnitude unbounded.
- The backward citation-chasing arm ran only post-freeze, by a weaker route than
  the protocol specifies, and named one probable eligible pre-2011 miss
  (`er-bc-1`) that the frozen corpus does not contain and did not admit.
- The ER-RoB appraisal is convention-resolved, not source-adjudicated: 90 of 357
  comparable cells decided by a direction-safe rule without reopening a source.
- Model identity across screening stages is **unresolvable from the logs** — the
  ReproLog schema carries no model-id field.
- Distinct-work count is deliberately two-valued: 69 under three adjudicated
  twin pairs, 68 if the fourth is one work.

### 5.3 Thread C — Kalshi corpus

- **98.3% of screening dispositions are keyword-classifier outputs.** 150 of
  8,813 records carry a verdict from anything reading them.
- **1,245 records ended screening unresolved** — 545 eligible-but-unextracted,
  700 with eligibility undecided. The undecided stratum is ~4.7× the included
  set and concentrated in the transfer-clause class feeding the largest strand.
- **No full text was read for any of the 149 included records.** 116 reached
  abstract depth, 33 metadata only. The extraction fields the protocol froze as
  the reason for the review — conditions as stated, model applicability
  conditions, frictions — are partially completed at best.
- Semantic Scholar contributed **zero** records (HTTP 429 across all queries and
  retries); one of four named databases is absent.
- Kalshi venue structure — trading mechanism, fee schedule, settlement rule — is
  **unretrieved**. Six transfers are marked `not-transferable-as-stated` as a
  result.
- The Kalshi-specific evidence base is 19 records, 17 of them T5, 5 sharing a
  first author.
- Recall cause for the four genuine known-item misses is **undetermined** between
  retrieval cap and vocabulary; neither the original reading nor the round-1
  over-correction survives.
- Two figures (2,630 / 6,183 irreproducible row ids) are **permanently
  unverifiable** — the file they were measured against was overwritten in place
  and never committed.

### 5.4 Repository-level, outside both reviews

Recorded as VG-14/15/16 in the Thread A review and **not repaired**:

- `pyproject.toml` pins no dependency; `uv.lock` untracked.
- The ReproLog for the corpus-producing commit `8aeebfe` has a vacuous
  environment record — `pip_freeze_sha256` is the SHA-256 of the empty string.
- No committed entrypoint re-derives any reported number; `tests/` and `src/`
  are empty, so the README Quickstart's `uv run pytest` verifies nothing.

### 5.5 A defect this session introduced and corrected

The lead session published a `pip_freeze_sha256` that did not verify against the
file it named: the digest was computed over the LF string, and the archive was
then written in text mode on Windows, substituting CRLF. Caught independently by
two round-2 branches. The archive was rewritten with LF so the published digest
verifies byte-exactly; the digest was not re-derived to match the file. The
superseded CRLF copy has been deleted. `.gitattributes` now carries
`*.jsonl text eol=lf`, closing the gap that had made one evidence log's digest
unpublishable.

## 6. AI-assistance statement (ICMJE §V.A)

| stage | model | role |
|---|---|---|
| orchestration, remediation of agenda artifacts, ADR-0004, bookkeeping | claude-opus-5 | idea, prose, audit |
| Thread A review authoring and three remediation passes | claude-opus-5 (research-librarian) | prose, audit |
| Thread C protocol, search execution, two remediation passes, branch agenda | claude-opus-5 (research-librarian) | prose, audit |
| five specialist audit rounds, 184 agents | claude-opus-5 | audit |
| Phase 2 corpus production (prior session, commit `8aeebfe`) | claude-fable-5 | screening, adjudication |

Models cannot be authors (ICMJE 2026). All AI output in this session was
reviewed by the named human author, who bears responsibility for it.

Reproducibility logs: `logs/reproducibility/repro_log_28961af5a9ce4aa88ffbb817dcba2e60.json`
(protocol registration), `repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json`
(Kalshi search execution), `repro_log_ee8bebfaafec4ce1962ee57746c90a36.json`
(Thread A round-3 remediation) — all **untracked locators**; `logs/` is
gitignored and the clone-durable carrier is the provenance commit's trailers.

## 7. Immutability and retention

Append-only per 21 CFR 11.10(e): corrections to this trail are appended as dated
addenda and never overwrite recorded information. The two thread trails are
governed by the same rule and already carry per-round append sections. Retained
for the life of the repository; superseded values are struck, never deleted.
