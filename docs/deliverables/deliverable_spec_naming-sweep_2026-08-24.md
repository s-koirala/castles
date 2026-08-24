---
type: deliverable_spec
slug: naming-sweep
date: 2026-08-24
session_objective: Vocabulary-first re-sweep of regime/state naming conventions — empirical term harvest, variant-generation, tradition-clustered sweep, and a synonym-graph taxonomy — correcting the recall bottleneck of lit_review_regime-definitions_2026-08-21.md (vocabulary mismatch, the project's twice-documented failure class).
predecessor_corpora: lit_review_regime-definitions_2026-08-21.md (54 records, 59 definitions), lit_review_level-definitions_2026-08-21.md (81 records, 76 definitions), lit_review_regime-classification_2026-08-21.md (96 records), lit_review_regime-method-gaps_2026-08-21.md (50), lit_review_f005-class-n-tests_2026-08-21.md (7) — diffed against, never re-screened.
---

# Deliverables

- [x] `docs/literature/vocabulary_regime-synonyms_2026-08-24.md` — 137 head
  terms / 8 traditions / ~540 variants, all-fields rows, 25 harvest logs;
  methodology citations handle-verified (PRESS, Schlosser 2006, Hausner 2012);
  post-sweep addendum registers the 12 flagged families (audit REV-1-2);
  audit rounds 1–2 accept
  - state: Term registry built BEFORE any evidence query runs: terms harvested
    from the included records' keywords/index terms, canonical practitioner
    taxonomies, encyclopedia redirect graphs (vocabulary harvesting only, never
    evidence), and OpenAlex concepts — seeded by, and exceeding, the user's
    list (accumulation/distribution, support/resistance, supply/demand,
    channel, band, zone, corridor, trading band, congestion area, discovery,
    parabolic, breakout, runs, plus "regime" synonyms). Each term carries:
    tradition of origin, hypothesized synonym family, spatial-vs-temporal type,
    morphological variants, and the source the TERM was harvested from. The
    search-strategy methodology (PRESS guideline; pearl growing) cited from
    verified sources.
  - check: file exists; every term row carries all five fields; harvest
    provenance logged; methodology citations DOI-resolve (handle API).

- [x] `docs/literature/lit_review_regime-naming_2026-08-24.md` — umbrella +
  two part records (lowercase filename deviation declared in-part); merged
  store 53 entries, zero collisions, all ids resolve (deterministic check
  PASS); 112 synonym-graph rows; saturation statement explicit (NOT reached;
  6 in-line, 6 open in registry addendum); audit rounds 1–2 accept
  - state: Tradition-clustered sweep record over the registry's variants —
    TA-spatial, Wyckoff/cycle, auction/Market-Profile, trend-event,
    statistical (runs/drift/persistence), and regime-synonym clusters — with
    per-variant logged queries, zero-records as first-class negatives, new
    operational definitions numbered continuing the D-series, and the
    **synonym graph**: term → construct → tradition → operational
    definition(s) → null-distribution status, with the spatial/temporal
    boundary handled by cross-mapping spatial terms to the level survey rather
    than re-sweeping. Saturation status stated: either "one full round added
    no new synonym family" or the residual families logged open.
  - check: file + `references_regime-naming.json` exist; per-cluster
    provenance; every included record resolves to a store entry; saturation
    statement present.

- [x] `docs/literature/lit_review_regime-definitions_2026-08-21.md` (supplement pointer) —
  dated addendum present; append-only verified BYTE-LEVEL (prefix hashes to
  the recorded pre-addendum SHA-256 b5613407…); time-t-null universal
  superseded with bounded survivor
  - state: Dated append-only addendum pointing to the naming sweep as its
    vocabulary-expansion supplement, recording that the original query
    vocabulary was the recall bottleneck; no prior entry edited.
  - check: addendum section present; original sections byte-identical above it.

- [x] `docs/research_notes/research_agenda_regime-classification_2026-08-21.md` (rev 3, conditional) —
  integration branch taken: item (d) refuted-and-bounded (Phillips family),
  item (b) range bounded, compression two-sweep-stable, branch-3 comparator
  note; round-1 exclusivity-clause majors remediated to bounded form; Rev 2
  fixes intact; audit rounds 1–2 accept
  - state: IF the sweep surfaces new definitions, nulls, or corrections
    touching agenda claims (e.g. "range has no operational state definition at
    any tier"), a rev 3 integrates them; if nothing binds, the Verification
    status section records the sweep ran and changed nothing. Either way the
    outcome is explicit, not silent.
  - check: rev 3 with integration OR a dated no-change record; per-site
    inspection.

- [x] `docs/audits/audit_trail_naming-sweep_2026-08-24.md` — rounds 1–2
  written and independently attested (round-2 SHA-256 dbe2b18e…); 19 round-1
  findings + 5 refute dispositions + 5 round-2 minors on record
  - state: WI-3 §2 trail for this session's audit round(s), attested.
  - check: file exists, written this session, attested.

- [ ] Commit via /commit-with-provenance
  - state: All deliverables committed with Repro-Log trailers, role=multi.
  - check: `git log -1` shows Repro-Log-Path / Repro-Log-SHA256 / AI-Assistance
    trailers.

# Delegation

- agent: research-librarian (Stage 1–2 — term harvest + variant generation)
  objective: Build the term registry empirically with harvest provenance;
    generate morphological variants per term; verify the PRESS / pearl-growing
    methodology citations against primary sources.
  output: `docs/literature/vocabulary_regime-synonyms_2026-08-24.md` + harvest
    logs under docs/literature/search_logs/regime-naming/; return summary with
    term counts per tradition and any family not in the user's seed list.
  sources: The five predecessor corpora's included-record keywords (Read);
    WebSearch/WebFetch for textbook indexes, Investopedia/Wikipedia redirects,
    OpenAlex concepts; Crossref for methodology citations.
  excluded: Runs no evidence queries — harvesting only. Does not screen
    records. Does not edit predecessor artifacts.
  check: deliverable 1's check.

- agent: research-librarian ×2 (Stage 3 — tradition-clustered sweeps, parallel)
  objective: Agent A sweeps the practitioner clusters (TA-spatial,
    Wyckoff/cycle, auction/Market-Profile); Agent B sweeps the academic
    clusters (trend-event, statistical runs/drift/persistence, regime
    synonyms). Both work from the registry's variants verbatim, diff against
    predecessor corpora, and report newly-surfaced synonym families for the
    saturation check.
  output: Shared `docs/literature/lit_review_regime-naming_2026-08-24.md`
    written by Agent A (clusters A) then appended by Agent B (clusters B), or
    two part-files merged by the lead — return format: per-cluster verdicts,
    new definitions, synonym-graph rows, zero-record negatives, new families.
  sources: Crossref, OpenAlex, Semantic Scholar, arXiv, SSRN, WebSearch for
    tier-5; predecessor stores for dedup.
  excluded: Do not re-screen the 288 predecessor records; do not harvest new
    vocabulary beyond flagging families for the saturation check; do not edit
    the agenda or failure_log.
  check: deliverable 2's check.

- agent: audit-remediate round(s) (post-integration)
  objective: Specialist audit — harvest-provenance honesty, synonym-graph
    fidelity to sources, cross-map correctness against the level survey,
    saturation-statement honesty, agenda-integration fidelity.
  output: Attested findings + trail per WI-3 §2.
  sources: The session's artifacts, predecessor corpora, WebFetch.
  excluded: G16 publisher-403 class stays closed (handle-API test); logged
    minors from prior specs are not re-raised.
  check: round report; attested trail.

# Self-executed

- Registry→sweep sequencing, merge of part-files if needed, agenda/supplement
  integration edits  (reason: transcription integrating delegated results —
  recorded Rule 1 deviation, routed through the audit round)
- Deterministic checks (store counts, id resolution, append-only verification
  of the supplement addendum)  (reason: deterministic inspection, no authored
  content)
- Saturation adjudication: at most one supplementary harvest+sweep round if
  new families surface; residual families logged open otherwise  (reason:
  orchestrator routing decision recorded in the trail, no authored research
  content)
- Spec ticks, trail addenda, ReproLog, commit  (reason: gate-mandated
  bookkeeping)
