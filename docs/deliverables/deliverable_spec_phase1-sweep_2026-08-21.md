---
type: deliverable_spec
slug: phase1-sweep
date: 2026-08-21
session_objective: Gap-targeted Phase 1 scoping sweep (PRISMA-ScR-style formative collection) closing the five named corpus holes behind research_agenda_regime-classification_2026-08-21.md, then integrating results into an agenda revision.
predecessor_corpora: lit_review_regime-classification_2026-08-21.md (96 records), lit_review_level-definitions_2026-08-21.md (81 records) — NOT re-swept; this session targets only what they demonstrably lack.
---

# Deliverables

- [x] `docs/literature/lit_review_regime-definitions_2026-08-21.md` — store=54
  entries, every store id resolves in the review (deterministic check PASS),
  PRISMA-ScR partial declared; audit rounds 1–2 accept
  - state: Scoping survey of operational definitions of market regime/state
    (trend, range, compression, transition, and any others located), each
    classified by feature space, assignment mechanism, causal-filtered vs
    smoothed-lookahead, and presence of a published null distribution; PRISMA-ScR
    partial compliance declared with conformance notes; companion CSL-JSON store.
  - check: file + `references_regime-definitions.json` exist; per-source search
    provenance sections (database, verbatim query, date, counts); every included
    record resolves to a store entry.

- [x] `docs/literature/lit_review_regime-method-gaps_2026-08-21.md` — store=50,
  id-resolution check PASS, per-target verdicts explicit (A.1/A.2/C
  NONE-FOUND with establishing queries; A.3/B FOUND); audit rounds 1–2 accept
  - state: Targeted scoping record with three sections — (a) null/reference
    distributions for branch-2 assigners (Kaufman ER, ADX-class bounded
    oscillators, HSMM duration inference); (b) changepoint detector operating
    characteristics (detection delay vs ARL0); (c) purge/embargo length
    methodology above practitioner tier. Zero-record outcomes registered as
    first-class logged negatives, not omissions.
  - check: file + `references_regime-method-gaps.json` exist; each of the three
    sections carries verbatim queries with dates and counts; negatives explicit.

- [x] `docs/literature/lit_review_f005-class-n-tests_2026-08-21.md` — store=7,
  id-resolution check PASS; Hall & York + Cheng & Hall read in full (direction:
  conservative; i.i.d.-only confirmed); F005 verdict FOUND (Garzarelli et al.
  2014, five authors); audit rounds 1–2 accept
  - state: (a) Hall & York 2001 and Cheng & Hall 1998 located with retrievable
    full-text route and bibliographic records added to the store; the direction
    of the Silverman size distortion extracted or recorded unobtainable;
    (b) forward-citation search from the seven tested level definitions plus a
    targeted Class-N existence-test search — the F005 discriminating observation.
  - check: file exists; both calibration records present in a CSL-JSON store;
    forward-citation search provenance logged; an explicit found/none-found
    verdict for Class-N existence tests.

- [x] `docs/research_notes/research_agenda_regime-classification_2026-08-21.md` (rev 2) —
  per-gap-site check PASS (all five sites carry citations or upgraded logged
  negatives; `revision: 2` in frontmatter); round-1 majors REV-1-1/REV-1-2 and
  LITERATURE-1-1/1-2 remediated, round-2 verify accept
  - state: Revision integrating the three sweep records: each of the five gap
    sites (regime definitions; assigner nulls; detector operating
    characteristics; calibration papers; purge/embargo sources) carries either
    new citations or an upgraded logged-negative label with search pointer;
    frontmatter rev bump with revision note; no existing citation removed.
  - check: per-gap-site inspection — five sites each show a citation or a
    logged-negative pointer to a sweep record; `revision: 2` in frontmatter.

- [x] `failure_log.md` — F005 row update — dated addendum appended; layer
  `undetermined` → `data` under the promotion rule (observation obtained,
  points the stated way — verified by all three audit branches); original text
  retained struck; transferable positive re-argued against interest
  - state: Discriminating-observation outcome appended to the F005 row
    (append-only; original text retained). Layer changes ONLY if the observation
    was actually obtained and pointed a stated way, per charter step 3.
  - check: F005 row shows a dated addendum citing the forward-citation record;
    layer field unchanged unless the promotion rule's condition is met.

- [x] `docs/audits/audit_trail_phase1-sweep_2026-08-21.md` — rounds 1–2
  written and independently attested (round-2 SHA-256
  9b1e307f9afab949d2c226a79404c36c5d1e4676de7e0da7509b1f246d9c81ad); 19
  round-1 findings + 4 refute dispositions + 4 round-2 minors on record
  - state: WI-3 §2 trail for this session's audit round(s).
  - check: file exists, written this session, attested.

- [ ] Commit via /commit-with-provenance
  - state: All deliverables committed with Repro-Log trailers, role=multi.
  - check: `git log -1` shows Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance
    trailers.

# Delegation

- agent: research-librarian (G1 — regime definitions)
  objective: Build the regime-definitions scoping survey — enumerate operational
    definitions of market regime/state across peer-reviewed, preprint, and
    practitioner sources; classify each; determine which have published null
    distributions and which are folklore.
  output: `docs/literature/lit_review_regime-definitions_2026-08-21.md` +
    `docs/literature/references_regime-definitions.json` + search logs; return
    summary with counts and located gaps.
  sources: WebSearch, WebFetch; Crossref, arXiv, SSRN, OpenAlex, Semantic
    Scholar; econometrics and forecasting journals; practitioner sources tiered.
  excluded: Does not touch the existing 96-record corpus's ground (Markov-
    switching estimation mechanics already covered); does not edit the agenda or
    failure_log; does not evaluate profitability.
  check: files exist per deliverable 1's check.

- agent: research-librarian (G2/G3/G5 — method gaps)
  objective: Targeted sweeps for (a) assigner null distributions, (b) detector
    operating-characteristics literature, (c) purge/embargo methodology above
    practitioner tier; register zero-record outcomes explicitly.
  output: `docs/literature/lit_review_regime-method-gaps_2026-08-21.md` +
    `docs/literature/references_regime-method-gaps.json` + search logs; summary
    with per-target counts and negatives.
  sources: WebSearch, WebFetch; Crossref, arXiv, OpenAlex, Semantic Scholar;
    sequential-analysis and quality-control literature (ARL is a QC concept);
    IEEE/ACM for online detection.
  excluded: Does not re-run the ADX/Choppiness folklore audit (already resolved);
    does not touch regime definitions (G1's ground); does not edit the agenda.
  check: files exist per deliverable 2's check.

- agent: research-librarian (G4 — calibration + F005)
  objective: Obtain Hall & York 2001 and Cheng & Hall 1998 (bibliographic record
    + retrievable full-text route + extracted size-distortion direction); run the
    F005 discriminating observation — forward-citation search from the seven
    tested level definitions and a targeted Class-N existence-test search.
  output: `docs/literature/lit_review_f005-class-n-tests_2026-08-21.md` + store
    entries + search logs; explicit found/none-found verdict for Class-N tests;
    recommended F005 disposition with evidence.
  sources: WebSearch, WebFetch; Statistica Sinica archive (Hall & York has no
    DOI — G16 rule does not apply to it), JRSS-B/Wiley, Semantic Scholar and
    OpenAlex citation graphs for forward citation,
    lit_review_level-definitions_2026-08-21.md for the seven seed definitions.
  excluded: Does not update failure_log itself (lead integrates under the
    promotion rule); does not re-screen the level survey's 81 records.
  check: files exist per deliverable 3's check.

- agent: audit-remediate round(s) (skill `audit-remediate`, post-integration)
  objective: Specialist audit over the three sweep records, the agenda revision,
    and the F005 row update — citation fidelity, PRISMA-ScR declaration honesty,
    per-gap-site integration coverage, promotion-rule compliance.
  output: Attested findings + trail per WI-3 §2.
  sources: The five artifact deliverables, this spec, charter, WebFetch.
  excluded: G16 DOI class stays closed (handle resolution, not publisher-page
    fetchability); Hall & York's DOI-lessness is a recorded fact, not a finding.
  check: round report returned; trail attested.

# Self-executed

- Agenda-revision edits and failure_log F005 addendum integrating delegated
  results  (reason: transcription integrating subagent evidence into artifacts
  governed by this session's reasoning — recorded Rule 1 deviation, same as
  prior specs, routed through the audit round rather than exempted)
- Per-gap-site integration check  (reason: deterministic inspection, no
  authored content)
- Spec ticks, trail addenda, ReproLog emission, commit  (reason: orchestrator
  bookkeeping mandated by the gate; no authored research content)
