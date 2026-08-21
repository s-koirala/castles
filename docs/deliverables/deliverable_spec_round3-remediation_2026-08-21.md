---
type: deliverable_spec
slug: round3-remediation
date: 2026-08-21
session_objective: Remediate the two round-3 failures from deliverable_spec_think-tank-charter_2026-08-21.md — per-section citation/CONVENTION coverage in the charter, and an attributed method in architecture-agenda branch 1 — under a fresh 3-round audit cap.
predecessor: deliverable_spec_think-tank-charter_2026-08-21.md
---

# Deliverables

- [x] `docs/methodology/charter_castles_2026-08-21.md` (Rev 3) — per-section
  check PASS on all eight claim-bearing H2 spans (script output recorded in the
  predecessor spec's tick annotation); audit rounds 1–2 accept in
  [audit_trail_round3-remediation_2026-08-21.md](../audits/audit_trail_round3-remediation_2026-08-21.md)
  - state: Each of the six H2 sections that failed round 3 (Standing commitments;
    Admissible output types incl. the PRISMA specification; Evidence standard;
    Publication-bias posture; Prior art posture; Falsification of commitment 1)
    carries either an inline `](http` citation or an explicit `CONVENTION` label.
  - check: per-section script — for every claim-bearing H2 span (all eight named
    in the round-3 audit), the span contains `](http` or `CONVENTION`. Whole-file
    counts are inadmissible (predecessor audit F-5).

- [x] `docs/research_notes/research_agenda_architecture_2026-08-21.md` —
  per-branch check PASS (9/6/7 citations, Falsification block in each);
  round-1 majors REV-1-1 and REV-1-2 remediated and verified accept in round 2
  - state: Branch 1 (Platform selection) names at least one attributed method
    (author-year with DOI/URL); branches 2 and 3 retain theirs.
  - check: per-branch script — each of the three H2 branch spans contains a
    `**Falsification` block and ≥1 `](http` citation. Aggregate counts
    inadmissible (predecessor audit F-1/F-5).

- [x] `docs/deliverables/deliverable_spec_think-tank-charter_2026-08-21.md` —
  both boxes ticked with pointer + check output; round-3 failure records
  retained unedited; no unchecked deliverable rows remain
  - state: Its two unticked boxes are ticked, each annotated with a pointer to
    this spec and the passing check output.
  - check: no unchecked `- [ ]` deliverable rows remain in the predecessor spec.

- [x] `docs/audits/audit_trail_round3-remediation_2026-08-21.md` — written
  this session (rounds 1–2, WI-3 §2 fields), attested by independent verifier,
  SHA-256 ec2670f53bf16d2f51ffccc79ebbbdef37a084be35c0e16a34e70a1c220e3d85
  - state: WI-3 §2 trail for this session's audit round(s), with findings,
    refute-gate dispositions, and remediation records.
  - check: file exists, written this session, per skill §Post-loop field spec.

- [ ] Commit via /commit-with-provenance
  - state: All remediated files committed with Repro-Log trailers, role=multi.
  - check: `git log -1` shows Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance
    trailers.

# Delegation

- agent: general-purpose (citation sourcing — charter)
  objective: For each enumerated methodological claim in the six failing charter
    sections, locate and verify the primary source (title, authors, venue, year,
    resolving DOI/URL), or report that none exists so the claim is labelled
    CONVENTION. Candidate sources supplied in the brief must be verified against
    the actual record, not passed through.
  output: Structured per-claim list — claim, verdict (SOURCED | CONVENTION),
    full citation with resolving DOI/URL, and any misattribution correction.
  sources: WebSearch, WebFetch; publisher DOI pages, arXiv, PubMed/BMJ, Crossref.
  excluded: Does not edit files. Does not touch the architecture agenda. Does not
    assess whether the charter's positions are correct — sourcing fidelity only.
  check: structured per-claim verdict list returned in tool result.

- agent: general-purpose (citation sourcing — agenda branch 1)
  objective: Locate and verify primary-source attributions for the methods branch
    1 actually relies on: information-driven bar construction (time/tick/volume/
    dollar), floating-point comparison tolerance (ULP/relative error), and
    continuous-futures roll conventions. Verify each candidate against the record.
  output: Same structured per-claim format as above.
  sources: WebSearch, WebFetch; publisher DOI pages, arXiv, Crossref.
  excluded: Does not edit files. Does not touch the charter. Does not evaluate
    vendor claims or licensing questions — method attribution only.
  check: structured per-claim verdict list returned in tool result.

- agent: audit-remediate round (skill `audit-remediate`, post-edit)
  objective: One specialist audit round over the two remediated files, verifying
    the new citations (literature-check branch), the per-section coverage, and
    that no prior audit finding was regressed. Adversarial refute gate applies.
  output: Attested findings list + audit trail material per WI-3 §2.
  sources: The two remediated files, predecessor spec/audit trail, WebFetch.
  excluded: Does not re-litigate predecessor findings already closed on recorded
    evidence (e.g. the G16 DOI false-positive class — resolve handles, not
    publisher-page fetchability).
  check: round report returned; trail written.

# Self-executed

- Application of sourced citations / CONVENTION labels into the two files
  (reason: transcription integrating delegated results into prose authored from
  this project's own session reasoning, which a subagent cannot recover — the
  same recorded Rule 1 deviation as the predecessor spec, routed through the
  audit round above rather than exempted from it)
- Per-section/per-branch mechanical check script  (reason: deterministic
  check, no authored content — "formatting/deterministic" exclusion)
- Spec box-ticking, audit-trail assembly, ReproLog emission, commit
  (reason: orchestrator bookkeeping mandated by the gate; no authored research
  content)
