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
title: "Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 1"
type: audit_trail
date: "2026-09-02"
started_at: "2026-09-02T13:05:41-05:00"
ended_at: "2026-09-02T16:48:23-05:00"
artifacts:
  - {path: "docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "43e3a8a62e1b23c072706f016b7ec46b3e21ef5997d398bc34283df262d91a3f"}
  - {path: "docs/literature/references_kalshi-arbitrage.json", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164"}
  - {path: "docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "51034c44e6e21b5f9281fa7150bbf939867b46b3b863c4be8e329d0ff35ff886"}
  - {path: "docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4"}
repo_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C — Kalshi / binary-event-market arbitrage branch. Item 5 (the corpus record): search provenance, per-source counts, inclusion/exclusion with reasons, and a synthesis of what the literature establishes about no-arbitrage and coherence conditions for binary contracts, longshot bias, inventory-risk market-making models and their applicability to bounded [0,1] payoffs, and cross-venue price-discrepancy evidence. Every claim carries a citation; each Kalshi-specific claim is separated from claims generalized from other venues, and each generalization states the assumption that carries it. Item 1 (ADR-0004): adoption scope names the branch, not the repository; states which REVIEW.md blocking directives bind a literature-only stage versus a future empirical stage; states the ADR-0003 boundary. Item 2 (the protocol): registered search, not a dual-screened systematic review, with the unmet PRISMA 2020 items enumerated. FOCUS FOR THIS ROUND: (a) protocol-vs-execution fidelity against the frozen protocol sha256 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4, registration commit 27d7473 — were the queries executed verbatim, did every deviation become a numbered append-only amendment, and did any eligibility criterion drift; (b) THE CENTRAL QUESTION: the executor reports 1,188 records reaching the end of screening unresolved — 545 coded X10 (eligible, extraction not performed) and 643 coded X11 (transfer-clause record promoted, stage-2 not assessed, eligibility UNDECIDED) — both codes introduced by post-hoc amendments A4 and A5. Is a 149-record corpus with 643 undecided records a defensible compiled corpus, is the defect disclosed with the right severity, and are the synthesis claims correctly bounded by it, or does the review state conclusions this corpus cannot carry; (c) amendment A3 declared a SECOND automation tool mid-screening — a deterministic vocabulary pre-sorter that verdicted 5,249 of 8,154 forward-citation-only records X1 by rule rather than by reading — assess whether that is adequately disclosed, whether its residual risk is correctly stated as unquantifiable, and whether any synthesis claim depends on the un-read stratum; (d) AG-5: NO full text was read for ANY of the 149 included records — extraction reached abstract depth for 116 and metadata-only for 33. Does any synthesis claim require full-text evidence it does not have, and is 'not mentioned' correctly distinguished from 'not stated in the abstract'; (e) AG-3: Semantic Scholar returned HTTP 429 on all 4 frozen queries and all 8 retries, so one of the four protocol-named databases contributed zero records — is the recall consequence stated; (f) REVIEW.md blocking directive 8, binding here by ADR-0004: does every factor, signal or trading rule in the synthesis carry a citation or an in-repo derivation, with zero unattributed folklore factors; (g) the Kalshi-specific versus generalized separation — 23 Kalshi-specific claim lines against 76 generalized, with 15 of the 19 Kalshi-specific records being T5 preprints or working papers and 5 sharing a first author: is the thinness and non-independence of the Kalshi evidence base disclosed, does any generalized claim leak into a Kalshi block, and does every generalization state the assumption that carries it; (h) the known-item recall check recovered 16 of 23, with 4 genuine topical-strategy misses (Rhode and Strumpf, Thaler and Ziemba, Ho and Stoll, Avellaneda and Stoikov) — the executor interprets this as retrieval depth rather than vocabulary being the binding constraint and labels that an interpretation rather than a demonstration; assess whether that reading is supported; (i) AG-1: the Kalshi rulebook returned HTTP 429 across 9 attempts, so the entire venue-structural fee, settlement, position-limit and membership record is unestablished and two second-hand fee claims found inside research records are unverifiable — is any synthesis claim resting on unverified venue structure; (j) the gate verdict reported is 'block' on 83 G16 identifier-resolution findings, all of the standing-closed publisher-landing-page class (81 HTTP 403, 1 HTTP 302 login gate, 1 HTTP 404 dead registered target) against 149/149 DOI Handle System responseCode 1 — adjudicate whether that block is correct or whether the G16 class closure applies.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md", sha256: "6425f053ce0e3dfd0554d7a103f3f65b76fdd46b95f4c4df6b5147eafd30e17d"}
    - {path: "docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md", sha256: "99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4"}
    - {path: "docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md", sha256: "51034c44e6e21b5f9281fa7150bbf939867b46b3b863c4be8e329d0ff35ff886"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill)."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "quant-auditor", agent_def_path: "~/.claude/agents/quant-auditor.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-opus-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Opus 5, claude-opus-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, quant-auditor, literature-check) → adversarial refuter → trail-assembly agent (this document)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. Four branches routed. critical-reviewer (design, conduct, interpretation, RQI dimensions) and scope-auditor (declared-spec coverage against deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C, and protocol-vs-execution presence) are unconditional. quant-auditor routed on focus items (a), (b), (c) and (h) — the screening classifier, the flow identities, the X10/X11 strata, the A3 pre-sorter partition and the known-item depth probe are reproducible computations against the stored logs and the archived scripts, not prose checks. literature-check routed on focus items (d), (f), (g) and (j) — extraction depth, directive-8 attribution, the Kalshi-vs-generalized separation and identifier resolution are citation- and source-fidelity claims. epi-auditor was not routed (no population-health artifact, no human-subjects data). Efforts: critical-reviewer high, scope-auditor medium, quant-auditor high, literature-check high."
rounds_completed: 1
rounds_cap: 3
cap_reached: false
verdict: "block"
counts: {raw_critical: 3, raw_major: 38, raw_minor: 24, refuted: 4, retained_conservative: 0, to_remediate: 37, minors_logged: 24}
sidecar: {path: "docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.json", sha256: "fcad5133001899a700596842e1691a353d1e5375751683f5d72a2eb2cf395a4c"}
---

# Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 1

Round 1 of a fresh 3-round cap opened by
[deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md](../deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md)
Thread C. Audited artifacts: the Kalshi / binary-event-market arbitrage corpus
record, its 149-record CSL-JSON bibliography store, ADR-0004 (quant-rule
adoption for the prediction-market branch), and the frozen search protocol
(worktree versions at HEAD `27d7473`; all four artifact digests are in the
front matter and the JSON sidecar, and the worktree is dirty — `worktree_clean:
false`). The frozen protocol
[protocol_kalshi-arbitrage-review_2026-09-02.md](../methodology/protocol_kalshi-arbitrage-review_2026-09-02.md)
was the primary conformance criterion; its on-disk digest recomputes to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`, matching
the registration digest named in the task spec and in registration commit
`27d7473`, so the register-before-execute ordering holds and the file audited
is the file a verifier obtains.

Branch verdicts: critical-reviewer proceed-with-remediation, scope-auditor
proceed-with-remediation, quant-auditor **block**, literature-check **block**.
Round verdict: **block** (3 criticals raised, 38 majors raised, 4 refuted at
the gate, 37 critical/major findings retained for remediation, 24 minors
logged, 0 retained-conservative). The block is driven by the two retained
criticals — QUANT-1-1 (an undeclared five-list keyword classifier produced
3,414 dispositions presented as individually-read screening verdicts, so the
PRISMA 2020 item-8 declaration is materially incomplete) and REV-1-2 (mutually
exclusive assertions of Kalshi's trading mechanism, both sourced to a
documentation stream the artifact's own S7 table says establishes neither) —
not by the reported G16 gate finding, which is dispositioned rather than
remediated (see below). Full finding payloads, refute-gate dispositions, and
per-branch residual-risk statements are held verbatim in the JSON sidecar
([audit_trail_kalshi-arbitrage-review_2026-09-02.json](audit_trail_kalshi-arbitrage-review_2026-09-02.json),
SHA-256 `fcad5133…`); the sections below carry the required record.

Focus items that closed without a finding. (f) REVIEW.md blocking directive 8,
binding here by ADR-0004: every rule-shaped statement in the synthesis carries
its source and an explicit E14 non-endorsement, the corpus states no rule of
its own, and no unattributed folklore factor was found in any branch — the one
challenge to the E14 determinations (LITERATURE-1-13) was refuted at the gate
on the records' own stored abstracts. (j) The reported gate `block` on 83 G16
identifier-resolution findings is **dispositioned, not remediated**: the DOI
Handle System responseCode is the authoritative resolution test and it passed
149/149; an unauthenticated HEAD against a publisher landing page is not a
resolution test, so all 81 HTTP 403 cases and the 1 HTTP 302 login gate fall in
the standing closed publisher-landing-page class. Three branches reached that
conclusion independently, two of them after re-resolving samples of 12
identifiers each through the Handle System. The single HTTP 404 dead registered
target is materially different from that class, is correctly carried separately
as AG-8, and does not breach I4 because that record was retrieved to abstract
depth. What G16 does not test — the year, venue, tier and author list attached
to a resolving identifier — is where this corpus actually fails, and those
failures are carried as LITERATURE-1-1, -2, -3, -19 and -20.

## findings-table

One row per finding — 41 critical/major (37 retained, 4 dropped) and 24 minors,
65 rows. All eight schema fields (id, severity, category, location, issue,
evidence, fix, reference) plus branch and disposition; issue/evidence/fix are
compressed for tabular legibility — the full verbatim text of every finding is
in the JSON sidecar, and every critical/major claim is reproduced verbatim and
unabridged in the refute-gate section below.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-1-1 | critical | interpretation | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1341-1343 (vs :1986-1987) | The strand-S4 headline states a universal negative about an entire literature that the corpus's own limitations section says it cannot state. S4 is the largest strand (61 of 149) and serves primary objective O4; 643 records were promoted under the C3 transfer clause and never assessed (X11), four o… | "The corpus's central S4 finding is that the first literature states its own applicability conditions in terms of the binary payoff, and the second does not." — contradicted at :1986 by "The corpus c… | Rewrite the 8.4 preamble to the depth the corpus reached: 'in the records whose abstracts were retrieved, the event-market design literature states its applicability conditions in terms of the binary payoff, while no re… | CHAMP item 28 (conclusions limited to what the analysis supports); frozen protocol §2.2 transfer clause + §5 field E10 | critical-reviewer | **refuted → dropped** |
| SCOPE-1-3 | major | changed | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:31-35 (frontmatter), 641-664 (section 6), 2080-2086 (13.2) | The delivered flow accounting differs in kind from the flow the protocol defines. `n_excluded: 8664` silently absorbs 1,188 records that are not criterion failures — 545 eligible-but-unextracted (X10) and 643 with eligibility UNDECIDED (X11). The distinction is stated in sections 6 and 13.2 but car… | Frontmatter: `n_screened: 8813 / n_excluded: 8664 / n_included: 149`. Section 5 identity table: "`n_screened - n_excluded == n_included` \| 8,813 - 8,664 = 149 \| 149 \| yes". Section 13.2: "Both are… | Add frontmatter keys `n_eligible_unextracted: 545` and `n_eligibility_undecided: 643` (or an `n_excluded_criterion: 7476` split), and carry the same split in the section 5 identity table so the arithmetic identity is st… | S-5 (inclusion/exclusion with reasons), S-4 check note | scope-auditor | **refuted → dropped** |
| QUANT-1-9 | major | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1335-1343,1980-1987 | The S4 strand-level conclusion is stronger than the corpus can carry and is contradicted by the corpus's own gap statement. Section 8.4 asserts as 'the corpus's central S4 finding' that the event-market maker literature states applicability conditions in terms of the binary payoff 'and the second d… | 8.4 header text quoted above versus G-5: 'four are at metadata depth with transfer status not addressed'; 13.2: 'A reader who wants the S4 inventory-risk lineage in full ... will find them in the X11… | Restate as: 'at the depth reached, the retrieved text of four of the five lineage anchors states no payoff-support condition, and the one that does assumes a Brownian reference price' - drop the universal 'and the secon… | Frozen protocol section 7 item 4 (no vote counting; report disagreement, claim nothing beyond the records) | quant-auditor | **refuted → dropped** |
| LITERATURE-1-13 | major | depth-exceeded | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1014-1017, :1124-1125, :2069-2079 | E14 attribution determinations -- the field that discharges REVIEW.md blocking directive 8 -- are asserted at abstract depth, where they are not determinable, and E14 is then omitted from the s13.2 list of fields disclosed as partially completed. Whether a rule is 'carried by a derivation inside th… | s8.1.2:1014 'the record states these as its own constructions with an internal derivation, so they are attributed within the record' (Nunes 2026, abstract depth). s8.2.2:1124 'the record states its o… | Downgrade every E14 determination to 'not determinable at abstract depth' unless the abstract itself states the attribution, add E14 to the s13.2 enumeration, and state what that does to the directive-8 assurance at thi… | protocol_kalshi-arbitrage-review_2026-09-02.md s5 field E14; ADR-0004 'Binding now -- REVIEW.md blocking directive 8' | literature-check | **refuted → dropped** |
| REV-1-2 | critical | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1280-1284 (vs :1361-1363 and :1937) | The corpus asserts Kalshi's trading mechanism in two mutually exclusive ways in the same section, and sources the assertion to a documentation stream that explicitly does not establish it. 8.3.2 calls the venue order-driven and uses that to block transfer of the entire sportsbook favorite-longshot… | ":1280-1284: "Carries only to (E6) a bookmaker book. Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9), so the supply-side channel as stated does not transf… | Remove the venue-mechanism assertion from both places. In 8.3.2 restate the Levitt carrying assumption without asserting Kalshi's mechanism — mark it `not-transferable-as-stated` under AG-1 like the other two transfers… | CHAMP items 26, 28; frozen protocol §2.7 constraint 1 and §8 corollary 2 (S7 facts may state whether a carrying assumption is sat… | critical-reviewer | retained → remediate |
| REV-1-3 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1253-1256 (vs :1937) | A carrying assumption is discharged against a venue-structural fact the S7 stream records as unretrieved. The Thaler & Ziemba transfer — the line the corpus calls 'the property that makes the whole binary-contract literature transferable at all' — is carried by asserting that the CFTC record establ… | "it holds at any venue whose contract settles at an endpoint — which the CFTC record establishes for Kalshi as a class of instrument (section 9) even though no rulebook was retrieved." | Replace with the S7 facts actually held: 'the CFTC record establishes only that the venue is a designated contract market as of 11/03/2020 and that its instrument class is the subject of active rulemaking; the settlemen… | CHAMP item 26; frozen protocol §2.7 constraints 1 and 3, §8 corollary 2 | critical-reviewer | retained → remediate |
| REV-1-4 | major | interpretation | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1304-1307 | A single T5 preprint read at abstract depth is reported as having established a fact about the venue, and that asserted fact is then used to discharge the carrying assumption of a separate generalized claim. The frozen protocol's tier rule is tier-blind admission with tier-labelled use and states i… | "Carries wherever a quote-setter faces informed order flow, which the Kalshi adverse-selection evidence in 8.4.1 establishes is the case there — this is the corpus's strongest cross-strand link betwe… | Downgrade the verb and carry the tier: 'one T5 preprint, at abstract depth, reports informed price impact on the venue (Bartlett & O'Hara 2026); if that measurement holds, the Shin mechanism's precondition is met. The c… | CHAMP item 25 (indecisive evidence not read as established); frozen protocol §2.5 evidence-tier vocabulary | critical-reviewer | retained → remediate |
| REV-1-5 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:590-591 (vs :628) | The flow narrative asserts that every screened record was read, which the amendment-A3 disclosure contradicts. 5,249 of 8,813 records — 60% of the screened universe and at least 78% of the 6,707 X1 exclusions — received their verdict from a deterministic token rule, not from a screener reading a ti… | ":590: "All 8,813 were screened at title level (and at abstract level where an abstract had been retrieved)." versus :628: "a 5,249-record DEFAULT-X1 stratum verdicted X1 by rule" | Rewrite the flow sentence as: '2,905 records in the forward-citation-only stratum plus the 659 records outside it were read individually at title level (and at abstract level where an abstract had been retrieved); the r… | CHAMP item 20; PRISMA 2020 item 8 (automation tools and how they were used) | critical-reviewer | retained → remediate |
| REV-1-6 | major | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:628, :650, :2055 | The A3 pre-sorter's actual reach is not recoverable from the record. The stated partition (2,905 REVIEW + 5,249 DEFAULT-X1 = 8,154) cannot be reconciled on the page with the amendment note that 3,300 records had already been read individually and retain their verdicts: at least 395 already-read rec… | ":2055: "Partly — 3,300 of the 8,154 had already been read individually and retain their individual verdicts; no verdict was reversed" against :628: "partitioned the 8,154-record forward-citation-onl… | Publish the exact count of records whose sole verdict is the token rule (derivable from ka-screening-verdicts.jsonl by counting rows whose verdict source is the pre-sorter), reconcile it against the 3,300 already-read f… | PRISMA 2020 item 8; PRISMA-S item 15; CHAMP item 20 | critical-reviewer | retained → remediate |
| REV-1-7 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991 (vs :711-859) | The disclosure of the Kalshi evidence base's thinness understates it against the artifact's own corpus table. Of the 19 records flagged E4/E15 = K, exactly two are T1 (Goel 2026, Subramanian 2026) and 17 are T5, not 15. The non-independence disclosure is also incomplete: it names the five-record Kr… | "Five of the nineteen Kalshi-specific records share a first author, and fifteen of the nineteen are T5 preprints or working papers." | Correct to 'seventeen of the nineteen are T5 preprints or working papers; the only two peer-reviewed-tier Kalshi records are Goel 2026 and Subramanian 2026' and 'seven of the nineteen come from two author groups (five K… | CHAMP item 23; RQI presentation dimension | critical-reviewer | retained → remediate |
| REV-1-8 | major | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:24-25, :34-35, :51-58, :576-579 | The artifact's machine-readable and first-read surfaces misstate the flow that its prose later corrects. The frontmatter lists X10 and X11 under the key `eligibility_exclusion`, which is the exact opposite of what section 1 says they are ('not eligibility criteria'), and publishes `n_excluded: 8664… | ":24-25: "X10 (amendment A4) ELIGIBLE ... X11 (amendment A5) ELIGIBILITY UNDECIDED" listed under `eligibility_exclusion:`; :34 "n_excluded: 8664"; against :591-593 "1,188 are capacity dispositions, n… | Move X10/X11 out of `eligibility_exclusion` into a separate frontmatter key (e.g. `disposition_codes_non_criterion`), add `n_criterion_excluded: 7476`, `n_capacity_disposition: 1188` and `n_eligibility_undecided: 643` t… | PRISMA 2020 items 16a and 2; CHAMP item 23; PRISMA-S item 15 | critical-reviewer | retained → remediate |
| REV-1-9 | major | interpretation | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2112-2128 | The known-item recall interpretation is contradicted by the artifact's own query list and its excusal of three misses is over-broad. (a) The supporting premise is factually wrong: no query in section 3 contains the token 'parimutuel' — it appears in the protocol's vocabulary paragraph but was never… | "two are S3 classics whose titles use vocabulary the strategy carries (\"parimutuel\", \"betting markets\"), so their non-retrieval indicates the retrieval **caps** rather than the vocabulary" | Delete 'parimutuel' from the vocabulary-carried claim or add the query that carries it; restate the interpretation as undetermined between cap and vocabulary, since the strategy contains no query that would have retriev… | CHAMP item 29; PRISMA-S item 14 / PRESS 2015 known-item check | critical-reviewer | retained → remediate |
| REV-1-10 | major | interpretation | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1963-1968, :1975-1979, :1368-1371, :1768-1773 | Corpus-level absence claims are stated without the depth and screening qualifiers that the same artifact establishes elsewhere. 'No record in the corpus measures or models the cost of capital locked in an event-contract position', 'There is no market-making model fitted to Kalshi' and 'the corpus c… | "**No record in the corpus measures or models the cost of capital locked in an event-contract position until settlement.** `ka-crossref-10` was written for exactly this and returned nothing eligible.… | Restate every corpus-level absence with its two qualifiers, e.g. 'no retrieved abstract among the 116 abstract-depth records states a measurement of capital-lockup cost; the 33 metadata-depth records, the 545 X10 and 64… | CHAMP item 25 (indecisive read as indecisive) and item 28; frozen protocol §5 field E12 | critical-reviewer | retained → remediate |
| REV-1-11 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:137 (vs :216-218 and :2099) | The primary search-provenance table records the wrong HTTP status for a documented access gap. The row for ka-fc-s2-a3 shows http 200, while the PRISMA-S 5 narrative and access gap AG-4 both state HTTP 404 for that anchor. The table is the artifact's PRISMA-S item 1/2/13 audit surface and the row i… | ":137: "\| Semantic Scholar \| ... \| ka-fc-s2-a3 \| 0 \| not reported \| 200 \| cursor/offset paged, 1 pages \|" against :216-218: "the Semantic Scholar arm returned 156, 39, 535, 426 and 6,147 for… | Correct the http column for ka-fc-s2-a3 to 404 against the stored log, remove the misleading 'cursor/offset paged, 1 pages' note, and add 'AG-4' to the note column so the table row points at its own gap entry. Re-check… | PRISMA-S items 1, 2, 8; CHAMP item 23 | critical-reviewer | retained → remediate |
| REV-1-12 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:563-566 (vs :2098) | The record's own summary of why recall is not demonstrated omits the largest of its three recall failures. Section 4 lists the missing peer review, the single unresolved forward-citation anchor and the unexecuted backward arm, but not AG-3 — that all four Semantic Scholar topical queries and all ei… | ":564-566: "**recall is not demonstrated** — the strategy was not peer reviewed, one of the six forward-citation anchors could not be resolved on the Semantic Scholar arm, and the backward citation-c… | Add AG-3 to the section 4 mitigation-(iv) sentence as the first item, and state the recall consequence in terms of the strategy: the four Semantic Scholar topical queries carried the unrestricted forms of 'market making… | PRISMA-S items 3 and 14; CHAMP item 29 | critical-reviewer | retained → remediate |
| REV-1-13 | major | design | docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1064-1087, :1202-1205; docs/literature/lit_review_kalshi-arbitrag… | The frozen amendment procedure was not followed and the deviation is not itself declared. Protocol §10 requires every deviation to be recorded 'in the addendum below', names the addendum 'APPEND-ONLY ADDENDUM BELOW THIS SECTION', and specifies five required elements per amendment including the reas… | "protocol :1202: "## Addendum (append-only; empty at freeze)" with no entries, against protocol :1071 "recorded as a **numbered, dated, append-only amendment** in the addendum below" and corpus :2048… | Either append A1-A5 to the protocol's addendum and record the resulting new SHA-256 in a follow-on provenance commit that names the frozen hash it supersedes, or add a numbered amendment A0 stating that the addendum mec… | CHAMP item 6 (consistency with the pre-registered protocol); frozen protocol §10 | critical-reviewer | retained → remediate |
| SCOPE-1-1 | major | omitted | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:219-223 (prisma-s-5); docs/methodology/protocol_kalshi-arbitrage-review… | A protocol-mandated search arm (backward citation chasing, `ka-bc-{n}`) was not executed, and its non-execution was not recorded as a numbered append-only protocol amendment. The declared spec requires every deviation from the frozen protocol to take that form; amendments A1-A5 cover retry classifi… | Spec: "deviations recorded as numbered append-only protocol amendments, never silently" (deliverable_spec line 129-130). Protocol: "Backward citation-chasing. The reference lists of INCLUDED C1 and C… | Add a numbered append-only amendment (A6) in ka-protocol-amendments.md recording the non-execution of the backward arm, its cause (no full text retrieved, so the arm had no input) and its recall consequence, and cite th… | S-5 (lit review state: search provenance + amendment discipline), S-4 (search logs check) | scope-auditor | retained → remediate |
| SCOPE-1-2 | major | changed | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2065-2090 (13.2), 2044-2057 (13.1) | The protocol's extraction stage was delivered in a different kind than specified: fields E8-E13 presuppose a stage-2 assessment of retrieved text, and none was performed for any of the 149 included records (abstract depth 116, metadata-only 33). The substitution is disclosed in 13.2 but was never c… | Artifact 13.2: "**No full text was read.** Extraction reached abstract depth for 116 of the 149 included records and metadata depth ... for the remaining 33 ... E8 ... E9 ... E10 ... E12 ... and E13… | Record the zero-full-text extraction decision as its own numbered amendment with the date and stage at which it was taken, and add a one-line statement of it to the artifact frontmatter (e.g. an `extraction_depth:` key)… | S-5 (lit review state: synthesis over extracted records) | scope-auditor | retained → remediate |
| SCOPE-1-4 | major | spec-conflict | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:14-25 (frontmatter `eligibility_exclusion`) vs :66-72 and :84-88 (secti… | The artifact's own frontmatter places X10 and X11 inside the `eligibility_exclusion` list, i.e. inside the restatement of the frozen eligibility criteria, while section 1 states in terms that they are "**not** eligibility criteria" and that the criteria "were not modified during execution". The fro… | Frontmatter: "eligibility_exclusion: ... - \"X10 (amendment A4) ELIGIBLE under section 2 and NOT a criterion failure ...\" - \"X11 (amendment A5) ELIGIBILITY UNDECIDED and NOT a criterion failure ...… | Move X10/X11 out of `eligibility_exclusion` into a separate frontmatter key (e.g. `disposition_codes_added:`) that names their amendment numbers, so the frozen criteria list in the header is byte-faithful to the protoco… | S-5, S-2 (frozen protocol eligibility criteria) | scope-auditor | retained → remediate |
| QUANT-1-1 | critical | method | C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:21-141; C:/Users/skoir/castles/docs/li… | Every screening disposition except the 149 includes and the single hand-verified X9 twin was produced by an undisclosed five-list keyword classifier, not by a screener reading records. The corpus declares only ONE rule-based stratum (the amendment-A3 DEFAULT-X1 partition, 5,249 records) and asserts… | ka-screening-script.py assigns every non-include verdict from hard-coded EVENT/CONTRIB/MODEL/DEFI/ELICIT substring lists (R3-R8). I re-ran that logic over the rebuilt universe (PYTHONHASHSEED=0) usin… | Add a numbered amendment declaring the full classifier (all five token lists, R0-R9) as the automation tool of record for all 8,664 non-include dispositions; correct the PRISMA item-8 block and section 6 to state that n… | PRISMA 2020 item 8, Page et al. 2021 https://doi.org/10.1371/journal.pmed.1003583; frozen protocol section 4.2 (single-pass scree… | quant-auditor | retained → remediate |
| QUANT-1-2 | major | numerical | C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:40-42,107-108; C:/Users/skoir/castles/… | The X5 rule ('traded object is a token pair or liquidity pool, not an event claim; fails B-a') fires on unanchored substrings. 'dex' matches inside 'index' and 'amm' inside 'programming', so records with no DeFi content are published with a false criterion-failure reason. The affected records are C… | Recomputation over the rebuilt universe: 283 works contain 'dex' only as a substring of 'index'; of the 159 X5 rows, 42 have no word-boundary DeFi token at all — e.g. 'A symbolic closed-form solution… | Re-run the classifier with word-boundary matching (\bdex\b, \bamm\b, \bdefi\b, \bcrypto), re-emit ka-screening-verdicts.jsonl, and correct the X5 count and the section 6 per-code table; the 42 reclassified records fall… | Frozen protocol section 2.4 X5 and section 2.1 B-a; published table ka-screening-verdicts.jsonl | quant-auditor | retained → remediate |
| QUANT-1-3 | major | method | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:22,643-646,709-859,2069-2073 | Eligibility-criterion drift without an amendment: 33 included records were retrieved only to title/venue/year ('meta' depth), which fails frozen criterion I4 and is exactly the case frozen exclusion X8 covers. The frontmatter restates X8 with an added clause not in the frozen protocol ('or full tex… | Frozen protocol lines 220-221: 'I4. The record is retrievable at least to abstract depth by the executing agent. Records retrievable only as a bare title are excluded under X8'; line 255: 'X8 - not r… | Either file a numbered amendment that explicitly relaxes I4 with its rationale and restates n_included, or exclude the 33 under X8 and re-derive n_excluded/n_included and the bibliography SHA; in both cases remove the f… | Frozen protocol sections 2.3 I4, 2.4 X8, and section 10 ('ANY deviation ... is recorded as a numbered, dated, append-only amendme… | quant-auditor | retained → remediate |
| QUANT-1-4 | major | method | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:24-25,85-88,656-657,2080-2086 | The X10 and X11 strata are described in eligibility terms the execution cannot support. X10 is said to mark records that 'passed eligibility' (545 records) and X11 records 'promoted to stage 2' under the transfer clause (643 records). Both sets were assigned by token rules (R3: event-token AND cont… | ka-screening-script.py R3/R6 branches; reproduction reproduces both counts exactly from tokens alone. Frozen protocol 4.2: 'a record is promoted iff its abstract does not settle I1/I2, and no record… | Relabel X10 as 'keyword-identified candidate stratum; eligibility not assessed' and X11 as 'keyword-identified model-record stratum; neither stage-1 nor stage-2 assessment performed', and propagate the weaker wording to… | Frozen protocol section 4.2 stage-1/stage-2 definitions; amendments A4, A5 | quant-auditor | retained → remediate |
| QUANT-1-5 | major | assumption | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1249-1256,1279-1284,1539-1542,1929-1938,1969-1974 | Three synthesis claims rest on Kalshi venue-structural facts the S7 stream explicitly did not establish, contradicting the corpus's own G-3 statement that only two claims are marked not-transferable-as-stated. The retrieved CFTC pages establish designation status/date and an intermediation-permissi… | 8.3.2: 'it holds at any venue whose contract settles at an endpoint - which the CFTC record establishes for Kalshi as a class of instrument (section 9)'; 8.3.2: 'Kalshi is an order-driven exchange in… | Strike the three appeals to the CFTC record for settlement structure and trading mechanism, mark the affected transfers not-transferable-as-stated (Thaler-Ziemba endpoint premise, Levitt bookmaker-versus-exchange block,… | Frozen protocol section 2.7 constraints 1 and 4; section 8 corollary 2 | quant-auditor | retained → remediate |
| QUANT-1-6 | major | reproducibility | C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py:44-58; C:/Users/skoir/castles/docs/literat… | The archived pipeline is not deterministic, so the published Table X-full row identifiers are not reproducible and the 'byte-for-byte' auditability claim fails. Record-level title and abstract selection tie-breaks on set iteration order, which depends on PYTHONHASHSEED; that changes the sort key an… | Two consecutive local runs of ka-dedup-script.py on identical input (recs.json, 15,924 records) gave identical aggregate counts (8,813 works / 7,111 duplicates, matching the record) but differed in u… | Make tie-breaks total (key=(len(t), t) for titles/abstracts/venues), pin PYTHONHASHSEED in the archived scripts, re-emit ka-screening-verdicts.jsonl, and/or key verdict rows by persistent identifier rather than by run-g… | CLAUDE.md Reproducibility (deterministic ordering); corpus record section 5 'both re-runnable against the stored ka-*.json logs' | quant-auditor | retained → remediate |
| QUANT-1-7 | major | reproducibility | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:42-46; C:/Users/skoir/castles/logs/reproducibili… | The execution run that produced the corpus emitted no ReproLog and the tracked deliverable cites none. The project contract requires a 13-field ReproLog per artifact-producing run and requires a tracked deliverable to cite the ReproLog SHA-256 and the sidecar SHA-256 alongside the git HEAD. | Frontmatter carries git_head_at_authoring only, with pip_freeze_sha256: 'n/a (no project-venv code execution...)' and dataset_checksums: 'n/a'. logs/reproducibility contains a registration-phase log… | Emit the 13-field ReproLog and sidecar for the execution run (Python 3.11 stdlib env still has a pip freeze), and add repro_log_sha256 / sidecar_sha256 to the corpus record frontmatter as untracked locators plus digests. | CLAUDE.md 'Reproducibility contract' and 'Reproducibility (hook-enforced)' | quant-auditor | retained → remediate |
| QUANT-1-8 | major | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:628,2059-2063; C:/Users/skoir/castles/docs/liter… | The A3 residual risk is declared 'unquantified and unquantifiable' and is described as failing only on records whose title AND abstract contain no published token. In fact a majority of the DEFAULT-X1 stratum had no abstract at all, so those exclusions rest on title text alone - a quantifiable and… | Recomputation over the rebuilt universe reproduces the published partition exactly (REVIEW 2,905 / DEFAULT-X1 5,249, matching ka-screening-vocabulary.json) and shows only 2,159 of the 5,249 DEFAULT-X… | Report the title-only rule-exclusion count (3,090) in section 13.1 and in the A3 entry, and restate the residual risk as partially quantified (bounded below by the title-only stratum) rather than unquantifiable. | Amendment A3; ka-screening-vocabulary.json fields_scanned | quant-auditor | retained → remediate |
| LITERATURE-1-1 | major | misattributed-citation-year | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:711-859 (corpus table) and :917-1882 (synthesis… | Systematic publication-year misattribution. The section-7 corpus table's displayed year disagrees with the DOI registrant's metadata AND with the record's own CSL-JSON store for ~20 records, and several of those wrong years are carried into section-8 citation strings. This is the load-bearing defec… | Fetched Crossref for each DOI: 10.1111/ecca.12009 = Franck, Verbeek & Nuesch, Economica 80(318):300-325, online 2012-12-17 / print 2013 -- table line 754 says 'Franck (2010)'. 10.5750/jpm.v1i2.423 =… | Regenerate the section-7 year column from the CSL-JSON store's `issued` field (the store is correct -- verified for 10.1111/ecca.12009 and 10.5750/jpm.v1i2.423), state in the table header which metadata field the year c… | https://api.crossref.org/works/10.1111/ecca.12009 ; https://api.crossref.org/works/10.1287/opre.2022.0417 ; https://api.crossref.… | literature-check | retained → remediate |
| LITERATURE-1-2 | major | misattributed-venue | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:711-859 | The corpus table's container-title is wrong for at least nine records, and disagrees with both the DOI registrant and the artifact's own CSL-JSON store. Venue is the field the evidence-tier assignment is derived from, so a wrong venue propagates into a wrong tier. | 10.5750/jpm.v1i2.423 shown as 'SSRN Electronic Journal' (Crossref and the store both give 'The Journal of Prediction Markets'; store entry at references_kalshi-arbitrage.json:1967 reads "container-ti… | Regenerate the venue column from the store's `container-title`; for arXiv-DOI records that have a journal version, record the journal and the arXiv id separately rather than labelling the journal record 'arXiv'. | https://api.crossref.org/works/10.1016/j.cnsns.2022.106994 ; https://api.crossref.org/works/10.1080/14697688.2017.1395230 ; https… | literature-check | retained → remediate |
| LITERATURE-1-3 | major | evidence-hierarchy | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:715 vs :1555; :740 vs :1148; :756 vs :1856; :846… | The evidence tier recorded in the corpus table contradicts the tier written on the claim line for four records. The protocol's whole tier discipline is 'tier-blind admission with tier-labelled use, and the tier travels with the claim' (protocol s2.5); a record carrying two different tiers in one ar… | Taleb 10.1080/14697688.2017.1395230: table line 846 'T5'; s8.1.2 line 1027 '(Taleb 2017 ... T1, abstract depth)'. Crossref confirms Quantitative Finance 18(1), journal article -> T1 correct, table wr… | Reconcile each to a single tier with the deciding evidence named, and add a mechanical check that no DOI carries two tier values in the artifact. | ~/.claude/CLAUDE.md Evidence Hierarchy; protocol_kalshi-arbitrage-review_2026-09-02.md s2.5 | literature-check | retained → remediate |
| LITERATURE-1-4 | major | unsupported-attribution | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1255-1256, :1280-1282, :1541-1542 | Three synthesis statements assert Kalshi venue-structural facts and cite 'the CFTC record (section 9)' as their source, but section 9's own S7 table states those facts are not established. This is the AG-1 failure mode the record claims to have contained, and it is the exact hazard protocol s8 exis… | s8.3.2:1255 'it holds at any venue whose contract settles at an endpoint -- which the CFTC record establishes for Kalshi as a class of instrument (section 9)'. s8.3.2:1280 'Kalshi is an order-driven… | Mark all three claims `not-transferable-as-stated`, delete the 'the CFTC record establishes' attributions, and correct the G-3 count. If endpoint settlement is to be asserted for Kalshi as a class, source it to a retrie… | protocol_kalshi-arbitrage-review_2026-09-02.md s2.7 constraint 1 and s8 corollary 2 | literature-check | retained → remediate |
| LITERATURE-1-5 | major | method-misattribution | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1571-1576 (and :1352, :1359) | Glosten-Harris (1988) is conflated with Glosten & Milgrom (1985). The corpus uses Bartlett & O'Hara's adaptation of the Glosten-Harris spread decomposition as evidence that Glosten & Milgrom's apparatus 'has been transferred to a binary event venue by others'. These are two different models by diff… | s8.4.3:1573-1576: 'The corpus nevertheless records that its apparatus *has* been transferred to a binary event venue by others -- the Kalshi adverse-selection record adapts the Glosten-Harris decompo… | Either drop the transfer sentence from the Glosten & Milgrom entry, or add Glosten & Harris 1988 to the corpus as the record whose apparatus was transferred and attribute it there. Do not use surname overlap as an attri… | https://api.crossref.org/works/10.2139/ssrn.6615739 ; Glosten & Harris 1988, https://doi.org/10.1016/0304-405X(88)90034-7 | literature-check | retained → remediate |
| LITERATURE-1-6 | major | unsupported-interpretation | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:2105-2131 | The known-item recall reading is over-broad in one direction and refuted by the frozen strategy in the other. (i) Three misses are excused as 'structural, not a recall failure' because each is its own forward-citation anchor -- but that exculpation covers only the one arm each anchors; all three co… | Line 2112-2115 classes KI-01 Oliven & Rietz, KI-18 Glosten & Milgrom and KI-23 Levitt as structural because 'a citing set contains the works that cite the anchor, never the anchor itself'. True only… | Restate the three anchor misses as 'not retrieved by any arm other than their own citing-set definition', so effective recall reads 16/23 rather than an implied 16/20. Withdraw the depth-not-vocabulary conclusion or sup… | protocol_kalshi-arbitrage-review_2026-09-02.md s3.4 'Per-item failures are reported and interpreted, not scored' | literature-check | retained → remediate |
| LITERATURE-1-7 | major | protocol-fidelity | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:199-205, :2092-2103 | Silent protocol deviation. The frozen protocol s3.1 'SSRN caveat, declared in advance' requires that if the SSRN site-search supplementary arm is not run, 'the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence.' The corpus record records no such… | Protocol lines 380-385 state the requirement. Grepping the corpus record for 'SSRN site', "SSRN's site", 'SSRN search', 'no public search API' and 'browser access' returns no matches. The gap table s… | Add the SSRN supplementary-arm absence to s13.3 as a numbered recall verification gap with its consequence for the Kalshi-specific stratum, or record it as amendment A6 with the stage at which it was decided. | protocol_kalshi-arbitrage-review_2026-09-02.md s3.1 SSRN caveat; s10 amendments policy | literature-check | retained → remediate |
| LITERATURE-1-8 | major | provenance-integrity | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:137 | The section-2 PRISMA-S 1/2/13 provenance table -- the artifact's canonical per-query record -- misreports a stored HTTP status, on the row that documents access gap AG-4. | Table row: '\| Semantic Scholar \| ... \| ka-fc-s2-a3 \| 0 \| not reported \| 200 \| cursor/offset paged, 1 pages \|'. The stored log docs/literature/search_logs/kalshi-arbitrage/ka-fc-s2-a3-p001.jso… | Correct the ka-fc-s2-a3 row to 404 and add the AG-4 note to the row's note column. | docs/literature/search_logs/kalshi-arbitrage/ka-fc-s2-a3-p001.json | literature-check | retained → remediate |
| LITERATURE-1-9 | major | missing-from-synthesis | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:746, :844, :859 | Three included records whose 'role in the argument' column affirmatively states they enter a named section-8 block appear nowhere in section 8. Two of them are Kalshi-specific, and one of those is a peer-reviewed T1 record -- so the omission both falsifies the role column and biases the Kalshi bloc… | Line 844 subramanian2026ijfmd2026100, 'Prediction market efficiency: evidence from Kalshi on pricing accuracy, forecasting, and risk', T1, K, S6, role 'enters the Kalshi-specific block of its strand'… | Name all three in their declared blocks at their stated extraction depth, or change the role column to say the record was included but not carried into the synthesis and give the reason. | https://api.crossref.org/works/10.3386/w34702 | literature-check | retained → remediate |
| LITERATURE-1-10 | major | misstated-limitation | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991 (G-6) and :1238-1240 | The disclosed non-independence of the Kalshi evidence base understates itself. G-6 states 'fifteen of the nineteen are T5 preprints or working papers'; the corpus table shows seventeen of nineteen. Understating a limitation in the sentence whose job is to state it is a disclosure defect, not a roun… | Enumerating the E4/E15 = K rows of the section-7 table: bartlett T5, brgi T5, diercks T5, goel T1, greene T5, gupta T5, krause x5 all T5, lee x2 T5, lim T5, mohanty T5, moulinier T5, polson T5, subra… | Correct G-6 to seventeen of nineteen, and state that after the synthesis omissions only one peer-reviewed Kalshi record actually carries a claim line. | — | literature-check | retained → remediate |
| LITERATURE-1-11 | major | grouping-rule-violation | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:74-82 vs :889-914, :1063-1098, :1191-1245 | The PRISMA 2020 item-13a grouping rule is declared as 'records are grouped by the protocol's frozen strand list' (i.e. mechanically from extraction field E3), but the strand recorded for a record in the corpus table repeatedly differs from the strand under which its claim is synthesized. The groupi… | s8.1.1 (strand S1) has three bullets; two are from records the table does not assign to S1 -- Burgi (table line 731: S3+S5) and Polson (table line 824: S6). Only Moulinier is an S1 record. s8.2.1 (S2… | Either correct the E3 strand values in the corpus table so they match where each record is synthesized, or move the claim lines to the strand the table assigns. State which of the two is the authoritative record of E3. | protocol_kalshi-arbitrage-review_2026-09-02.md s5 field E3; s7 item 4 | literature-check | retained → remediate |
| LITERATURE-1-12 | major | separation-rule-violation | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1080-1087, :1203-1209, :2170-2172 | Non-Kalshi evidence is stated inside Kalshi-specific blocks without a carrying assumption, and s13.7 then asserts as an absolute that this never happens. The separation rule is the branch's headline control (protocol s8) and the claim of its perfect observance is false as written. | s8.3.1:1203-1209 states, inside the Kalshi-specific block: 'A cross-platform study of 72.1 million Kalshi trades ... with 404.5 million Polymarket trades reports a statistically significant bias on b… | Split mixed-venue records: state the Kalshi-measured part in the K block and the other-venue part in the generalized block with its carrying assumption, or restate the K-block line so it makes no claim about the non-Kal… | protocol_kalshi-arbitrage-review_2026-09-02.md s8 parts 1-3 | literature-check | retained → remediate |
| LITERATURE-1-14 | major | conclusion-exceeds-corpus | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1335-1343 | A strand-level conclusion the corpus cannot carry. The S4 header states as 'the corpus's central S4 finding' that the inventory-risk lineage 'does not' state applicability conditions in terms of the binary payoff. That is a positive claim about non-statement, drawn from five named-lineage anchors o… | Line 1341-1343: 'The corpus's central S4 finding is that the first literature states its own applicability conditions in terms of the binary payoff, and the second does not.' Against it: s8.4.3 recor… | Rewrite the S4 header claim to 'does not, at the extraction depth reached, in the records this corpus assessed' and cross-reference the 643 X11 records at the point of the claim rather than only in s13.2. | — | literature-check | retained → remediate |
| LITERATURE-1-15 | major | frontmatter-contradicts-body | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:14-25, :31-35 | The machine-readable frontmatter -- the surface a downstream artifact consumes -- contradicts the body on the status of the 1,188 unresolved records. X10 and X11 are listed under `eligibility_exclusion:` alongside the nine criterion codes, while the body insists in bold that they are 'not eligibili… | Frontmatter `eligibility_exclusion:` lines 15-25 lists X1..X9 and then X10 and X11 as members of the same list. Body s1:84-88: 'Two disposition codes were added during execution (amendments A4 and A5… | Move X10/X11 out of `eligibility_exclusion` into a separate `disposition_codes` key, and add explicit frontmatter fields `n_eligible_not_extracted: 545` and `n_eligibility_undecided: 643`. | — | literature-check | retained → remediate |
| REV-1-14 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2140 (vs :164-165) | The depth-truncation summary cites a platform-reported total for the NBER arm that the search-provenance table records as unavailable. Section 13.5 states 'both NBER queries retrieved 50 against a reported 21,594'; the section 2 table gives `platform_total_hits` = 'not reported' for ka-nber-01 and… | "both NBER queries retrieved 50 against a reported 21,594" | Resolve against ka-nber-01.json and ka-nber-02.json: if the API returned a total, put it in the table's platform_total_hits column per query; if it did not, delete the 21,594 figure from 13.5 and record the NBER truncat… | PRISMA-S item 9; CHAMP item 23 | critical-reviewer | logged, not remediated |
| REV-1-15 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:212-218 (vs :2142-2144) | A completeness claim is made for a platform that reported no totals. PRISMA-S 5 states retrieval was complete 'against the count each platform reported', but the Semantic Scholar forward-citation rows all carry `platform_total_hits` = 'not reported', so completeness of that arm is unverifiable; the… | "Retrieval was complete against the count each platform reported: OpenAlex returned 153/153, 37/37, 321/321, 499/499, 382/382 and 6,463/6,463 for anchors A1-A6; the Semantic Scholar arm returned 156,… | Restrict the completeness claim to OpenAlex and state for the Semantic Scholar arm that the service reported no citing-set total, so retrieval completeness there is asserted only by the short-page termination condition… | PRISMA-S items 5 and 9 | critical-reviewer | logged, not remediated |
| REV-1-16 | minor | standard-coverage | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2094-2103 | A gap the frozen protocol required to be recorded by name is not recorded. Protocol §3.1 states that if the executing session lacks browser access for the SSRN supplementary site-search arm, 'the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence… | "AG-6 \| RePEc/IDEAS via the frozen GET endpoint \| HTTP 200 with a structurally empty results page, twice" — the AG table's last recall-source row; no SSRN entry appears anywhere in the table | Add an AG row: 'SSRN site search — supplementary arm not run (no browser route); SSRN reached only via the two rows=20 Crossref container-restricted queries ka-crossref-13/14 against platform totals of 10,991 and 1,093,… | Frozen protocol §3.1 SSRN caveat; PRISMA-S item 4 | critical-reviewer | logged, not remediated |
| REV-1-17 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1080-1087 | A two-venue measurement is placed in a Kalshi-specific block without stating the venue split. The line reports 113,338 Bitcoin and Ethereum contracts across Kalshi and Polymarket as one aggregate; only the risk-neutral-skewness sub-result is attributed to Kalshi. The frozen separation rule classifi… | "implied volatility surfaces, risk-neutral densities and variance risk premia are extracted from 113,338 Bitcoin and Ethereum contracts traded between September 2025 and February 2026; risk-neutral s… | State that the 113,338-contract sample spans both venues and that the record's abstract does not give the Kalshi share, then keep only the explicitly Kalshi-attributed sub-result (near-zero risk-neutral skewness from mu… | Frozen protocol §8 rule 1 and corollary 1; CHAMP item 23 | critical-reviewer | logged, not remediated |
| SCOPE-1-5 | minor | documented-drift | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:41 (frontmatter `ai_assistance`) vs :2055 (amendment A3), :2059-2063 | Two screening automation tools were used but only one is named at the declaration site. The frontmatter declares the model as "the declared PRISMA 2020 item-8 automation tool for screening"; the second tool — a deterministic vocabulary pre-sorter that verdicted 5,249 of 8,154 forward-citation-only… | Frontmatter: "The model is also the declared PRISMA 2020 item-8 automation tool for screening." A3: "A second declared automation tool: a deterministic published vocabulary pre-sorter partitioning th… | Name both automation tools in the frontmatter item-8 declaration, with the A3 amendment number and the 5,249/2,905 stratum split, so the declaration site matches the ledger. | S-5 (search provenance) | scope-auditor | logged, not remediated |
| SCOPE-1-6 | minor | changed | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:137 (section 2 table row ka-fc-s2-a3) vs :216-218 and docs/literature/s… | The delivered per-query provenance table reports an HTTP status that contradicts both the stored log and the artifact's own prose. The spec requires one log row per query recording the HTTP result; the table row is the human-readable carrier of that record and it is wrong for this query. | Table: "\| Semantic Scholar \| ... \| ka-fc-s2-a3 \| 0 \| not reported \| 200 \| cursor/offset paged, 1 pages \|". Prose at prisma-s-5: "the Semantic Scholar arm returned ... and **HTTP 404 for A3**"… | Correct the `http` cell for ka-fc-s2-a3 to 404 in the section 2 table. | S-4 (one log per query, verbatim record) | scope-auditor | logged, not remediated |
| SCOPE-1-7 | minor | partial | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1073-1079 (8.2.1) vs :1674-1683 (8.5.1) and :1940-1948 (section 9) | The J5 second-hand/unverified flag on the only named Kalshi fee magnitude is carried in 8.5.1 and section 9 but not at the 8.2.1 restatement, where the 2.00-cent figure appears unhedged inside a Kalshi-specific measurement line. 8.1.1 hedges it as "a stated 2.00-cent Kalshi fee"; 8.2.1 does not. A… | 8.2.1: "show a median cross-venue mid divergence of 0.60 cents against a 2.00-cent Kalshi fee". 8.5.1: "**J5 flag:** ... **That check could not be performed** ... flagged second-hand and unverified,… | Add the J5 marker or an explicit cross-reference to 8.5.1 on the 8.2.1 line (and on any other line restating a venue-structural constant), so every occurrence of the figure carries its unverified status. | S-5 (each claim bounded; protocol J5) | scope-auditor | logged, not remediated |
| SCOPE-1-8 | minor | documented-drift | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1980-1987 (G-5), 1333-1343 (8.4 preamble) | One named minimum element of the spec item — "inventory-risk market-making models and their applicability to bounded [0,1] payoffs" — is delivered as a declared absence rather than as a synthesis. Four of the five named-lineage anchors sit at metadata depth with transfer status `not addressed`, and… | G-5: "The inventory-risk lineage's applicability to [0,1] payoffs is asserted by transfer, not by the lineage ... The corpus cannot say whether the originals address bounded payoffs, because it did n… | Keep the gap statement and add a one-line pointer from the spec item's check text (or the artifact's opening summary) to G-5, so the shortfall against the spec's named minimum element is visible without reading section… | S-5 | scope-auditor | logged, not remediated |
| SCOPE-1-9 | minor | partial | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1080-1087 (8.2.1) | A Kalshi-specific block carries a pooled two-venue measurement without stating the Kalshi share. The 113,338-contract sample spans Kalshi and Polymarket; only the skewness statement is bounded to "multi-strike Kalshi events". The separation rule the spec imposes (Kalshi-specific claims separated fr… | 8.2.1: "binary contracts on Kalshi and Polymarket are treated as structurally identical to cash-or-nothing digital options, and implied volatility surfaces, risk-neutral densities and variance risk p… | Either state the Kalshi share of the 113,338 contracts, or mark the pooled quantities as cross-venue and keep only the Kalshi-bounded statements in the K block. | S-5 (Kalshi-specific vs generalized separation) | scope-auditor | logged, not remediated |
| SCOPE-1-10 | minor | added | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1996-2007 (section 11 `TO COMPUTE` handoffs) | Section 11 ships a five-row handoff register naming computations, data sources and derivation tasks. The spec's state for this artifact names search provenance, counts, inclusion/exclusion with reasons and a bounded synthesis; the handoff/branch-derivation content belongs to the unshipped research… | Spec item 5 state (lines 141-149) names no handoff register. Artifact section 11: "\| TC-4 \| Whether the Cartea-Jaimungal / Avellaneda-Stoikov single-parameter identification ... binds any market-ma… | Either add a line to the spec item recording section 11 as intended content of the corpus record, or move the handoff register into the research agenda when that artifact is written and leave a pointer here. | S-5 vs S-6 | scope-auditor | logged, not remediated |
| SCOPE-1-11 | minor | documented-drift | docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:154-160; repository (no matching file) | Spec item `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md` has no artifact satisfying it — the file does not exist. The box is unchecked, so the absence is declared rather than concealed, and Thread C is incomplete at this round; recording it here so the loop tra… | Glob for `docs/research_notes/research_agenda_prediction-market-microstructure*` returns no files. Spec: "- [ ] `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md`". | Ship the agenda (its inputs G-1 through G-7 are already written), or convert the box to a dated deferral naming the successor session, so the absence is a decision rather than an open box. | S-6 | scope-auditor | logged, not remediated |
| QUANT-1-10 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991,709-859 | G-6 understates the tier concentration it exists to disclose: it reports 'fifteen of the nineteen are T5 preprints or working papers' whereas the corpus table marks seventeen of the nineteen Kalshi records T5. | Parsing the section 7 table: 149 rows, E4/E15 counts K=19, G=69, N=61; among the 19 K rows tier counts are T5=17, T1=2 (the two T1 being Goel 2026 and Subramanian 2026). | Correct G-6 to 'seventeen of the nineteen are T5', keeping the five-shared-first-author statement. | Section 7 corpus table, E2/E4 columns | quant-auditor | logged, not remediated |
| QUANT-1-11 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2098 | AG-3's headline sentence is false as written: Semantic Scholar contributed thousands of records through its /citations endpoint; only the four topical /paper/search queries returned zero. | AG-3: 'One of the four named bibliographic databases contributed zero records to the corpus.' Section 2 table: ka-fc-s2-a1/a2/a4/a5/a6 contributed 156+39+535+426+6,147 = 7,303 records; the log ka-s2-… | Rewrite as 'the Semantic Scholar topical arm contributed zero records; the same platform's citation arm contributed 7,303', and state the recall consequence as loss of the four topical query strategies rather than loss… | Corpus section 2 per-query table; ka-s2-0*.json logs | quant-auditor | logged, not remediated |
| QUANT-1-12 | minor | method | C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:1-234; C:/Users/skoir/castles/docs/… | Three protocol deviations are disclosed in prose but never filed as numbered amendments, contrary to the frozen amendments policy that any deviation whatsoever becomes an amendment: (a) the backward citation-chasing arm ka-bc-{n} was not executed at all; (b) extraction fields E8-E13 were only parti… | Protocol section 10: 'ANY deviation ... is recorded as a numbered, dated, append-only amendment'; section 3.3 specifies the backward arm; corpus prisma-s-5: 'the protocol's ka-bc-{n} backward citatio… | File A6/A7/A8 covering the non-execution of the backward arm, the partial completion of E8-E13, and the choice to keep the amendments outside the frozen file to preserve its SHA-256 (noting the protocol's internal confl… | Frozen protocol sections 3.3, 5, 10 | quant-auditor | logged, not remediated |
| QUANT-1-13 | minor | verification-gap | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2105-2131 | The known-item interpretation ('retrieval depth, not vocabulary, is the binding constraint') is supported for three of the four genuine misses and unverified for the fourth; the record asserts all four are consistent with the cap explanation. | Live re-execution of the frozen Crossref strings at depth 1,000 (audit-side check, 2026 session): on ka-crossref-05, Thaler & Ziemba 10.1257/jep.2.2.161 ranks 346 and Rhode & Strumpf 10.1257/08953300… | Cite the depth probe per item and state that the cap explanation is demonstrated for KI-06, KI-09 and KI-21 and remains unexplained for KI-20. | Crossref REST API query.bibliographic with rows=200/offset paging; corpus section 13.4 | quant-auditor | logged, not remediated |
| QUANT-1-14 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:199-206,2092-2103 | The protocol's SSRN caveat requires that, if no supplementary SSRN site search was run, the absence be recorded as a recall verification gap; the corpus states no browse arm was run but files no corresponding AG row. Separately, 990 dedup merge groups span more than one DOI while only the 24 twin s… | Protocol 3.1: 'if not, the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence'; corpus 13.3 lists AG-1..AG-8 with no SSRN row. Re-run of ka-dedup-… | Add an AG row for the un-run SSRN site-search arm, and state the 990/24 review coverage of multi-DOI merge groups as a dedup verification gap. | Frozen protocol sections 3.1 (SSRN caveat) and 4.1 (dedup, J6) | quant-auditor | logged, not remediated |
| QUANT-1-15 | minor | numerical | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:964-967,1879 | One transcription substitutes a different quantity for the source's own: the record's $1.12 million is realized arbitrage profit across two channels, not the magnitude of reconstructed payoff-bound violations. | arXiv 2608.00666 abstract (fetched this session): 'Our reconstruction estimates \$1.12 million in arbitrage profit across two realization channels: \$1.086 million from converter ...'. Corpus: 'the r… | Change to 'estimates 1.12 million dollars in realized arbitrage profit across two channels (1.086 million from the converter channel)'. | https://arxiv.org/abs/2608.00666 | quant-auditor | logged, not remediated |
| QUANT-1-16 | minor | reporting | C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2015-2040 | Gate adjudication, recorded for completeness: the reported `block` on 83 G16 findings is the standing-closed publisher-landing-page class and should not block; the corpus's own disposition is correct but carries no audit-side verification. | Independent Handle System checks this session on a 12-DOI sample spanning all three sub-cases returned responseCode 1 with the registered targets the record names, including 10.3905/jod.2019.26.4.128… | Record the audit-side sample verification in the gate-disposition paragraph and reconcile the 150-vs-149 doicheck count. | DOI Handle System REST API https://doi.org/api/handles/{doi}; deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md line 234… | quant-auditor | logged, not remediated |
| LITERATURE-1-16 | minor | internally-contradicted-statement | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:2098 | AG-3's bolded headline claim is contradicted by the next sentence of the same table cell and by the section-2 table. Semantic Scholar did not contribute zero records; its /citations endpoint contributed 7,303 records to the universe. What contributed zero is the Semantic Scholar topical vocabulary… | AG-3 cell: 'One of the four named bibliographic databases contributed zero records to the corpus. The Semantic Scholar /paper/search endpoint refused every unauthenticated request; only its /citation… | Restate AG-3 as 'the Semantic Scholar topical (vocabulary) arm contributed zero records; the forward-citation arm on the same platform contributed 7,303', and state the recall consequence in terms of the four frozen S2… | — | literature-check | logged, not remediated |
| LITERATURE-1-17 | minor | extraction-code-misuse | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1587-1599 | The E10 transfer-status value `explicitly excluded` is assigned to Gueant, Lehalle & Fernandez-Tapia on the corpus's own inference rather than on the record's statement. The record assumes a Brownian reference price; it does not state that bounded [0,1] payoffs are outside its scope. The code as de… | s8.4.3:1594-1597 'Transfer status: explicitly excluded by the stated model -- a Brownian reference price is unbounded and cannot be a [0,1] probability that must terminate at an endpoint, so this mod… | Record the status as `not addressed` (the record states no payoff-support condition) and carry the Brownian-price incompatibility as a separate, explicitly labelled corpus inference rather than as an extracted field val… | — | literature-check | logged, not remediated |
| LITERATURE-1-18 | minor | disclosure-placement | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:585-594, :2059-2063, :2092-2103 | The A3 pre-sorter's residual risk is stated in prose at s13.1 but never registered as a gap alongside AG-1..AG-8 or G-1..G-7, as amendment A3 itself promised; and the flow narrative in s5 does not carry the partition, so a reader of the flow alone infers that all 8,813 records were read individuall… | Amendment A3 (ka-protocol-amendments.md:123-126): 'The residual risk is stated as a recall verification gap in the corpus record's limitations section.' The corpus record's gap register s13.3 lists A… | Add the A3 pre-sorter residual risk as a numbered gap (AG-9 or G-8), qualify the s5 flow sentence with the 2,905/5,249 partition at the point where the 8,813 figure is stated, and add the affirmative sentence that all 1… | — | literature-check | logged, not remediated |
| LITERATURE-1-19 | minor | citation-fidelity | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:715, :743, :746, :774, :823 | Author-name and title fidelity defects carried unflagged from source metadata into citation strings. | Line 715/1555 'Abramovicz' -- Crossref's deposit for 10.5750/jpm.v1i2.423 does read 'Michael Abramovicz', but the author of record for this JPM paper is Michael Abramowicz; the corpus reproduces a re… | Add a metadata-defect column or footnote so a known registrant typo is cited with a [sic]-style flag and the corrected form; repair the mangled title and the stray asterisk; fill the two null years from Crossref. | https://api.crossref.org/works/10.5750/jpm.v1i2.423 ; https://api.crossref.org/works/10.3386/w34702 | literature-check | logged, not remediated |
| LITERATURE-1-20 | minor | truncated-author-list | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1454 | A four-author paper is cited with three surnames and no 'et al.', which reads as a complete author list. | s8.4.2:1454 cites '[Agrawal, Delage, Peters, Wang & Ye 2011]' correctly for a five-author paper, then '[Gao, Wang & Wu 2022](https://doi.org/10.1287/opre.2022.0417)'. Crossref for that DOI returns fo… | Cite as 'Gao, Wang, Wu & Yu 2025' or 'Gao et al. 2025', consistent with the year correction in LITERATURE-1-1. | https://api.crossref.org/works/10.1287/opre.2022.0417 | literature-check | logged, not remediated |
| LITERATURE-1-21 | minor | gate-adjudication | C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:2015-2040 | Adjudication of the reported gate `block`. On the G16 identifier-resolution question the standing closed-class disposition does apply and the block should not stand on those 83 findings -- but the artifact should not be released on that basis, because the identifier-metadata defects that G16 does n… | I independently resolved a sample of the store's identifiers: 10.65109/bbzi6501 returns handle responseCode 1 with registered target dl.acm.org/doi/10.5555/3463952.3464011; 10.1111/ecca.12009, 10.575… | Close the 83 G16 findings under the standing publisher-landing-page class with the per-identifier Handle log as evidence, and re-run the gate after remediating the metadata findings above -- G16 tests whether an identif… | — | literature-check | logged, not remediated |

## refute-gate

Every critical/major finding passed the adversarial refute gate before
remediation; a drop requires concrete counter-evidence, never bare disagreement
([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)). Forty-one dispositions:
**4 dropped** (REV-1-1, SCOPE-1-3, QUANT-1-9, LITERATURE-1-13 — each defeated
by a line-anchored re-read or a reproduced check that contradicted the claim's
own evidentiary premise) and **37 retained** after failed refutation attempts.
There are no retained-conservative entries this round (`retained_conservative:
0`); all four drops carry concrete counter-evidence of the enumerated types
(`source-quote`, `reproduced-check`), so none is a bare-disagreement drop. Two
entries carry `reproduction_required: true` (SCOPE-1-3, dropped;
LITERATURE-1-2, retained); their `reproduction: {command, observed}` blocks are
lifted from the refutation evidence and given with those entries. Claims are
reproduced verbatim and unabridged; retained-after-failed-refutation entries
are included alongside the drops.

### REV-1-1 — dropped (refuted)

- raised_by: critical-reviewer; severity_claimed: critical; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false; outcome: **dropped**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1341-1343 (vs :1986-1987)
> **issue:** The strand-S4 headline states a universal negative about an entire literature that the corpus's own limitations section says it cannot state. S4 is the largest strand (61 of 149) and serves primary objective O4; 643 records were promoted under the C3 transfer clause and never assessed (X11), four of the five named inventory-risk anchors are at metadata depth, and no record was read at full text. A claim of the form 'literature L does not state applicability conditions' cannot be supported from unread abstracts plus an unassessed promoted set — it is precisely the 'not mentioned' vs 'not stated in the abstract' conflation the record elsewhere flags as undecidable.
> **evidence:** "The corpus's central S4 finding is that the first literature states its own applicability conditions in terms of the binary payoff, and the second does not." — contradicted at :1986 by "The corpus cannot say whether the originals address bounded payoffs, because it did not read them."
> **fix:** Rewrite the 8.4 preamble to the depth the corpus reached: 'in the records whose abstracts were retrieved, the event-market design literature states its applicability conditions in terms of the binary payoff, while no retrieved abstract in the inventory-risk lineage does; four of five named-lineage anchors are at metadata depth and 643 C3 records were promoted and never assessed, so this is a statement about retrieved abstracts, not about either lineage.' Add a gap entry in section 10 naming the 643 undecided C3 records as an S4-completeness gap for objective O4.
> **reference:** CHAMP item 28 (conclusions limited to what the analysis supports); frozen protocol §2.2 transfer clause + §5 field E10

Refutation (counter-evidence, `source-quote`):

> Both quoted strings reproduce verbatim (:1341-1343 and :1986-1987 confirmed by numbered read of C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md). But the defect claim's premise — that :1341-1343 is an unscoped universal negative about an entire literature — is falsified by the document itself on three independent, self-obtained counts.
>
> (1) Scope is declared as BINDING at the head of the very section containing the sentence. Section 8 opens (:863) "**Reading rules for this section, all binding.**" and rule 2 (:867-870) reads: "**Extraction depth is abstract or metadata, never full text** (section 13.2). Every statement below is a statement about **what a record's abstract or metadata says**, transcribed as the record states it. Where an abstract does not settle a point, this section says so instead of inferring it." Section 8.4 begins at :1333, i.e. inside that scope. Under a declared binding rule, "the second does not" already means "no retrieved abstract/metadata in the second lineage states it" — which is the scope the finding says is absent and which its own claimed fix would inline. That is a redundancy-of-emphasis argument, not an unsupported claim.
>
> (2) The S4 body applies that qualifier per record, explicitly and repeatedly, so the reader cannot reach the alleged universal reading. :1567 "the transfer clause has nothing to work with **at the depth reached**"; :1578 "Transfer status: **not addressed** at the depth reached"; :1580-1583 same for Kyle 1985; :1573-1577 for Glosten & Milgrom, which additionally records the opposite of a universal negative — "the corpus nevertheless records that its apparatus *has* been transferred to a binary event venue by others ... even though this corpus did not read the original's own statement of it"; and the block summary at :1628-1629 "*All are transfer-clause records; none states a bounded-payoff condition **at the depth reached**.*" The four-of-five metadata-depth fact the finding cites as unacknowledged is stated in-line at each anchor (:1565 "**metadata depth: no abstract was returned by any source**", :1572, :1580).
>
> (3) The 643 X11 records are explicitly declared OUTSIDE the corpus, so a "corpus's central S4 finding" does not quantify over them. :2080-2086: "643 were promoted under the transfer clause and never assessed (X11) ... A reader who wants the S4 inventory-risk lineage **in full** ... will find them in the X11 and X10 rows of the verdicts file and **not in this corpus**." The synthesis covers the 149 included records; the finding's inference that the headline claims coverage of the unassessed promoted set has no textual basis.
>
> (4) No contradiction exists between the two cited locations. :1341-1343 is a statement at retrieved-text depth (per rule 2); G-5 at :1986-1987 is a statement about the ORIGINALS' full texts ("The corpus cannot say whether the originals address bounded payoffs, because it did not read them"). Different depths, compatible propositions — G-5 exists precisely to publish the depth limitation, and its own headline (:1980-1981, "asserted by transfer, not by the lineage") uses the same form as :1341-1343, so the document is consistent rather than self-contradicting. CHAMP item 28 (conclusions limited to what the analysis supports) is satisfied by the binding-scope declaration plus per-record depth marks; the "not mentioned vs not stated in the abstract" undecidability the finding invokes (:2078-2079) is scoped there to extraction field E12, and rule 2 resolves it globally in favor of the decidable reading.

### SCOPE-1-3 — dropped (refuted)

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **reproduced-check**; reproduction_required: **true**; outcome: **dropped**

Claim verbatim:

> **category:** changed
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:31-35 (frontmatter), 641-664 (section 6), 2080-2086 (13.2)
> **issue:** The delivered flow accounting differs in kind from the flow the protocol defines. `n_excluded: 8664` silently absorbs 1,188 records that are not criterion failures — 545 eligible-but-unextracted (X10) and 643 with eligibility UNDECIDED (X11). The distinction is stated in sections 6 and 13.2 but carries no marker at the frontmatter/identity-table level where the numbers are consumed and re-cited downstream, so a reader taking the header at face value receives a completed-screen corpus that does not exist.
> **evidence:** Frontmatter: `n_screened: 8813 / n_excluded: 8664 / n_included: 149`. Section 5 identity table: "`n_screened - n_excluded == n_included` | 8,813 - 8,664 = 149 | 149 | yes". Section 13.2: "Both are capacity gaps, not criterion failures, and both are counted inside `n_excluded` only so the frozen arithmetic identities hold."
> **fix:** Add frontmatter keys `n_eligible_unextracted: 545` and `n_eligibility_undecided: 643` (or an `n_excluded_criterion: 7476` split), and carry the same split in the section 5 identity table so the arithmetic identity is stated over criterion exclusions plus capacity gaps rather than over an undifferentiated 8,664.
> **reference:** S-5 (inclusion/exclusion with reasons), S-4 check note

Refutation (counter-evidence, `reproduced-check`):

> Reproduced the file at every location the finding cites. Three of its assertions are false as stated.
>
> (1) "carries no marker at the frontmatter ... level" — FALSE. The frontmatter itself, in the same block as the counts, declares both codes with the capacity/criterion distinction spelled out in capitals. docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md lines 24-25, inside `eligibility_exclusion`:
>   - "X10 (amendment A4) ELIGIBLE under section 2 and NOT a criterion failure: serves only a secondary objective and section-5 extraction was not performed within this execution session"
>   - "X11 (amendment A5) ELIGIBILITY UNDECIDED and NOT a criterion failure: C3 transfer-clause record promoted to stage 2, stage-2 full-text assessment not performed within this execution session"
> Line 28 (`protocol_amendments`) further names "A4 (disposition code X10 ...)" and "A5 (disposition code X11)". A reader taking the header at face value is therefore told, inside the header, that the exclusion set contains two non-criterion dispositions — the opposite of "receives a completed-screen corpus".
>
> (2) "carries no marker at the ... identity-table level" and "the distinction is stated in sections 6 and 13.2" — FALSE. The finding cites section 5's identity table (line 578) but omits the paragraph 13 lines below it in the same section. Lines 590-594, bolded in source: "8,664 were excluded, of which **1,188 are capacity dispositions, not criterion failures** (545 X10 + 643 X11) — this is the single most important number in the flow and section 13.2 states its consequence." That is exactly the split the finding says is absent at that level, stated with both component counts and flagged as the most important number in the flow. The distinction is additionally stated at lines 84-89, i.e. in section 1, ahead of the entire body: "Two disposition codes were added during execution (amendments A4 and A5) and are **not** eligibility criteria ... Both are capacity gaps".
>
> (3) "The delivered flow accounting differs in kind from the flow the protocol defines" — FALSE. The governing accounting is prescribed verbatim by the registered append-only amendments, not deviated from. docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md, A4: "X10 rows sit in `n_excluded` so that the section 4.3 arithmetic identities continue to hold, and every X10 row's reason states in those words that it is not a criterion failure." A5: "X11 rows sit in `n_excluded` so the section 4.3 identities hold ... The corpus record reports the X11 count separately from every criterion-failure code." Both amendments are dated post-stage-1/pre-extraction, state "No eligibility verdict was changed", and are enumerated in the artifact's own frontmatter. The protocol's frozen identity set (docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md line 810: `n_screened − n_excluded == n_included`) is satisfied, and the amendment is the instrument that placed the capacity rows inside n_excluded.
>
> (4) The finding's own proposed key is already published and arithmetically closed in the artifact. Section 6 per-code table (lines 649-657) gives X1 6,707 + X2 338 + X3 35 + X5 159 + X7 236 + X9 1 = 7,476 criterion exclusions, + X10 545 + X11 643 = 8,664. The "n_excluded_criterion: 7476" the fix asks for is directly readable from the delivered table.
>
> (5) The stated downstream harm is unsupported: `grep -rn "8,664\|8664"` across docs/, reports/ and research/ returns no occurrence of the figure outside this artifact, so no downstream re-citation of an undifferentiated 8,664 exists.
>
> Residue not refuted (not the defect as claimed): the five numeric frontmatter keys are not themselves split, and the identity-table row shows only 8,813 - 8,664 = 149. That is a placement preference about where an already-stated, already-quantified, protocol-prescribed distinction is repeated, not the claimed defect of a silent absorption unmarked at the header.

`reproduction` block, lifted from the refutation evidence:

```yaml
reproduction:
  command: "grep -rn \"8,664\\|8664\" docs/ reports/ research/   # test the stated downstream harm; plus a line-anchored re-read of lit_review_kalshi-arbitrage_2026-09-02.md at :24-25, :28, :84-89, :578, :590-594, :649-657 and of ka-protocol-amendments.md A4/A5"
  observed: "No occurrence of the figure outside the audited artifact, so no downstream re-citation of an undifferentiated 8,664 exists. The re-read returned the capacity/criterion split inside the front matter itself (lines 24-25, X10 \"ELIGIBLE ... NOT a criterion failure\", X11 \"ELIGIBILITY UNDECIDED ... NOT a criterion failure\"), in section 1 ahead of the body (lines 84-89), and in bold in section 5 thirteen lines below the identity table (lines 590-594, \"1,188 are capacity dispositions, not criterion failures (545 X10 + 643 X11)\"); the section 6 per-code table closes arithmetically as 6,707 + 338 + 35 + 159 + 236 + 1 = 7,476 criterion exclusions plus 545 X10 plus 643 X11 = 8,664, i.e. the \"n_excluded_criterion: 7476\" key the fix asks for is already derivable from the delivered table. Amendments A4 and A5 prescribe the placement of the capacity rows inside n_excluded so the frozen section 4.3 identities hold. Three of the finding's assertions are therefore false as stated."
```

### QUANT-1-9 — dropped (refuted)

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false; outcome: **dropped**

Claim verbatim:

> **category:** reporting
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1335-1343,1980-1987
> **issue:** The S4 strand-level conclusion is stronger than the corpus can carry and is contradicted by the corpus's own gap statement. Section 8.4 asserts as 'the corpus's central S4 finding' that the event-market maker literature states applicability conditions in terms of the binary payoff 'and the second does not', while G-5 concedes the corpus 'cannot say whether the originals address bounded payoffs, because it did not read them' and the whole transfer-clause lineage sits unassessed in the 643 X11 rows.
> **evidence:** 8.4 header text quoted above versus G-5: 'four are at metadata depth with transfer status not addressed'; 13.2: 'A reader who wants the S4 inventory-risk lineage in full ... will find them in the X11 and X10 rows of the verdicts file and not in this corpus.'
> **fix:** Restate as: 'at the depth reached, the retrieved text of four of the five lineage anchors states no payoff-support condition, and the one that does assumes a Brownian reference price' - drop the universal 'and the second does not'.
> **reference:** Frozen protocol section 7 item 4 (no vote counting; report disagreement, claim nothing beyond the records)

Refutation (counter-evidence, `source-quote`):

> Both cited locations reproduce verbatim, but the alleged contradiction dissolves against binding text in the same artifact that the finding does not engage.
>
> 1. Section 8 opens (C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:861-871) with "**Reading rules for this section, all binding.**" whose item 2 reads: "**Extraction depth is abstract or metadata, never full text** (section 13.2). Every statement below is a statement about **what a record's abstract or metadata says**, transcribed as the record states it." Section 8.4 (lines 1333-1343) is inside that scope. So "the second does not" is, by the document's own binding interpretive rule, a statement about the retrieved abstract/metadata of the S4 inventory-risk records, not about the unread originals. G-5 (lines 1980-1987) disclaims a different object, and says so explicitly: "The corpus cannot say whether **the originals** address bounded payoffs, because it did not read them." A statement about retrieved text and a disclaimer about originals are not in contradiction; no line of G-5 asserts that the retrieved text of any lineage anchor does state a binary-payoff applicability condition.
>
> 2. The retrieved-text reading is exactly what 8.4.3 discharges per record (lines 1563-1607). All five anchors are recorded as not stating such a condition at the depth reached: Ho & Stoll "nothing in the retrieved metadata states a payoff support"; Glosten & Milgrom "not addressed at the depth reached"; Kyle "not addressed at the depth reached"; Avellaneda & Stoikov "the retrieved text states a securities-market setting and no bounded-payoff condition"; Gueant, Lehalle & Fernandez-Tapia "explicitly excluded by the stated model". The universal in 8.4 is therefore true of every record it ranges over at the declared depth — it is not a vote count, and it is not an inference beyond the records.
>
> 3. The finding's supporting premise that "the whole transfer-clause lineage sits unassessed in the 643 X11 rows" is factually wrong on the artifact's own records. The named-lineage anchors are included, not X11: Table X-nearmiss row U01465 (line 690) states "not excluded — listed here only because a reader may expect it under X11 with the rest of the transfer-clause lineage; **it is included as a named-lineage C3 record**." Section 13.2 (lines 2084-2086) says a reader wanting the lineage "**in full**" will find it in X11 — i.e. the unassessed remainder beyond the anchors, not the whole lineage.
>
> Reference check: protocol section 7 item 4 exists (docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:871-882) and forbids pooling/vote counting and requires disagreement to be reported. Nothing in it is violated by an aggregate statement of what the retrieved text of five enumerated records does and does not state.

### LITERATURE-1-13 — dropped (refuted)

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **source-quote**; reproduction_required: false; outcome: **dropped**

Claim verbatim:

> **category:** depth-exceeded
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1014-1017, :1124-1125, :2069-2079
> **issue:** E14 attribution determinations -- the field that discharges REVIEW.md blocking directive 8 -- are asserted at abstract depth, where they are not determinable, and E14 is then omitted from the s13.2 list of fields disclosed as partially completed. Whether a rule is 'carried by a derivation inside the record' cannot be read off an abstract.
> **evidence:** s8.1.2:1014 'the record states these as its own constructions with an internal derivation, so they are attributed within the record' (Nunes 2026, abstract depth). s8.2.2:1124 'the record states its own strategies with an internal derivation' (Vlastakis et al., abstract depth). s13.2:2074-2079 names E8, E9, E10, E12 and E13 as 'partially completed at best' and explicitly handles E12's 'not mentioned' versus 'not stated in the abstract' distinction -- but E14 is not in that list, despite being the most full-text-dependent field of the set. AG-5 (line 2100) confirms no full text was read for any record.
> **fix:** Downgrade every E14 determination to 'not determinable at abstract depth' unless the abstract itself states the attribution, add E14 to the s13.2 enumeration, and state what that does to the directive-8 assurance at this stage.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s5 field E14; ADR-0004 'Binding now -- REVIEW.md blocking directive 8'

Refutation (counter-evidence, `source-quote`):

> The finding's load-bearing premise -- "Whether a rule is 'carried by a derivation inside the record' cannot be read off an abstract" -- is false at every site it cites. I pulled the stored abstract for each record from C:\Users\skoir\castles\docs\literature\references_kalshi-arbitrage.json (149 CSL-JSON entries, `abstract` field present), i.e. exactly the depth-of-record the review declares.
>
> (1) Site :1014, Nunes 2026 (id nunes2026ssrn6446502). Review text: "the record states these as its own constructions with an internal derivation, so they are attributed within the record". Stored abstract, verbatim: "We document three systematic trading strategies deployable on binary prediction markets... We derive closed-form edge conditions, analyse failure modes, and discuss deployment constraints..." The abstract states both halves of the E14 determination in its own words -- own construction ("We document... we short the overpriced outcomes") and internal derivation ("We derive closed-form edge conditions"). It also carries no citation to prior published research for any of the three strategies. The E14 value is read off the abstract, not inferred past it.
>
> (2) Site :1792, Greene 2026 (id greene2026ssrn6442939). Review text: "the record states a constructed statistic". Abstract: "we construct the Trend Quality Ratio (TQR), defined as the slope of a linear pre-close price trend normalized by its residual dispersion." Directly stated.
>
> (3) Site :1124, Vlastakis, Dotsis & Markellos 2008 (id vlastakis2008for1085). Review text: "the record states its own strategies with an internal derivation". Abstract: "The paper also investigates the profitability of strategies based on: combined betting, simple heuristic rules, regression models and prediction encompassing... Simple trading rules and betting strategies based on forecast encompassing are found capable of also producing significant positive returns." The strategies are stated as the paper's own, built in-paper from named constructions, with no external attribution -- the E14 trichotomy (citation / derivation-inside-record / neither) resolves at abstract depth. The only clause that reaches slightly past the abstract is "derivation" as applied to the "simple heuristic rules" component; that does not change the recorded value, which is that attribution is internal to the record and not a citation.
>
> The finding's own claimed fix concedes the escape clause -- "unless the abstract itself states the attribution" -- and in all three instances the abstract does state it. The dependent claim (E14 must be added to the s13.2 enumeration as "partially completed at best") therefore collapses with the premise: I confirm E14 is absent from the s13.2 list at :2074-2079 and that AG-5 (:2100) records no full text was read, but the stated rationale for adding it -- that E14 is "the most full-text-dependent field of the set" and its values are "not determinable" at this depth -- is contradicted by the source text at each site where E14 was actually exercised. E14 was invoked at exactly three places (grep for "E14": :884 and :2169 are policy statements, not determinations), and all three are abstract-determinable.
>
> Separately, the directive-8 assurance does not rest on the E14 source-attribution values in the first place. ADR-0004:50-55 defines the binding obligation as constraining what the branch artifact writes: "Every factor, signal, or trading rule appearing in branch artifacts carries a citation to published research or an in-repo derivation." The review discharges that at :883-885 and :2169 by stating no rule of its own and restating none as established -- a property of the corpus record, verifiable without any full text.

### REV-1-2 — retained

- raised_by: critical-reviewer; severity_claimed: critical; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1280-1284 (vs :1361-1363 and :1937)
> **issue:** The corpus asserts Kalshi's trading mechanism in two mutually exclusive ways in the same section, and sources the assertion to a documentation stream that explicitly does not establish it. 8.3.2 calls the venue order-driven and uses that to block transfer of the entire sportsbook favorite-longshot literature — a decision the record itself labels 'the single largest structural reason the sportsbook FLB literature must not be restated as a Kalshi finding'. 8.4.1 calls the same venue quote-driven. The order-driven premise is attributed to 'the CFTC record's own designation category (section 9)', but 'Designated Contract Market' is a regulatory category, and S7-5 records contract specifications and settlement rules as Not established. A conclusion-bearing transfer decision therefore rests on an unverified venue-structural fact that the artifact's own S7 table denies having.
> **evidence:** ":1280-1284: "Carries only to (E6) a bookmaker book. Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9), so the supply-side channel as stated does not transfer" versus :1361-1363: "the venue's quote-driven microstructure is interpreted through makers as relatively well-informed traders"; and :1937: "**Not established.** Kalshi's fee schedule, position limits, contract specifications, settlement and adjudication rules"
> **fix:** Remove the venue-mechanism assertion from both places. In 8.3.2 restate the Levitt carrying assumption without asserting Kalshi's mechanism — mark it `not-transferable-as-stated` under AG-1 like the other two transfers that need an unretrieved venue fact, and increment the count in G-3 from two to three. In 8.4.1 attribute 'quote-driven' to the source record ('the record characterises the venue as quote-driven') rather than stating it as a venue fact.
> **reference:** CHAMP items 26, 28; frozen protocol §2.7 constraint 1 and §8 corollary 2 (S7 facts may state whether a carrying assumption is satisfied only with document, version and retrieval date)

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; the finding reproduces exactly and the artifact's own text forecloses every available defense. (1) All three quoted passages reproduce verbatim at the stated lines of docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md: :1279-1284 asserts "Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9)" and uses it to block the Levitt transfer; :1361-1362 states "the venue's quote-driven microstructure"; :1937 S7-5 records contract specifications and settlement rules as "Not established." (2) The cited authority denies the premise: S7-1 at :1933 says the DCM designation "fixes the venue's regulatory category and its designation date, nothing else," and the section 9 preamble (:1886-1892) binds S7 records so they "may never establish a behavioural, empirical or efficiency claim." So section 9 cannot license the order-driven assertion. (3) The document treats the two labels as mutually exclusive alternatives itself, at :1760-1761 ("a quote-driven market ... over an order-driven one") and in the self-disagreement register at :1882 ("Is a quote-driven or an order-driven venue cheaper to trade?"), which does not log the Kalshi-internal contradiction. (4) Grep for order-driven/quote-driven/order book/limit order across the file finds no alternative establishment of Kalshi's matching mechanism from any corpus record; remaining hits (:998, :1164, :1816) are carrying-assumption phrasings and :1648 repeats the same unsupported assertion. (5) The count sub-claim also verifies: :2096 (AG-1) and G-3 at :1969-1972 enumerate exactly two section-8 claims marked not-transferable-as-stated (8.1.2 and 8.2.2), and the Levitt line at :1280 is not among them.

### REV-1-3 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1253-1256 (vs :1937)
> **issue:** A carrying assumption is discharged against a venue-structural fact the S7 stream records as unretrieved. The Thaler & Ziemba transfer — the line the corpus calls 'the property that makes the whole binary-contract literature transferable at all' — is carried by asserting that the CFTC record establishes endpoint settlement for Kalshi contracts. Section 9 establishes only designation status and date, an intermediation-order modification, and Federal Register document counts; S7-5 records settlement and adjudication rules as Not established, and S7-6 records the eCFR text as unretrieved.
> **evidence:** "it holds at any venue whose contract settles at an endpoint — which the CFTC record establishes for Kalshi as a class of instrument (section 9) even though no rulebook was retrieved."
> **fix:** Replace with the S7 facts actually held: 'the CFTC record establishes only that the venue is a designated contract market as of 11/03/2020 and that its instrument class is the subject of active rulemaking; the settlement rule for any listed contract is unretrieved (S7-5), so this transfer is recorded as pending that document.' Either mark the line `not-transferable-as-stated` or cite the specific Federal Register document whose retrieved text carries the settlement characterisation.
> **reference:** CHAMP item 26; frozen protocol §2.7 constraints 1 and 3, §8 corollary 2

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; the finding reproduces exactly. The quoted text is present verbatim at docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1253-1256. Section 9's S7 table contains six rows and none establishes endpoint settlement: S7-1 (designation status/date 11/03/2020), S7-2 (2025-01-17 intermediation-order modification), S7-3 (five Federal Register documents matching "Kalshi"), S7-4 (570-document count). The ka-doc-01 query at line ~1911 requests only fields[]=title,document_number,publication_date,agencies,html_url,type, so no FR document text was retrieved and no settlement characterisation could have been read. S7-3's own license column denies the reading the cited line needs: "No. It establishes that the venue and its instrument class are the subject of active federal rulemaking, and identifies which documents a successor stage must read." S7-5 (line 1937) records settlement and adjudication rules as "Not established / none retrieved"; S7-6 records 17 CFR 40.11 as unretrieved. Three internal contradictions corroborate the defect rather than refute it: (1) section 8 reading rule 4 (lines 873-880) names "the settlement and adjudication process (E7)" as a component every carrying assumption must write out, mandating `not-transferable-as-stated` otherwise; (2) gap G-3 states "Nothing in the corpus establishes Kalshi's own contract mechanics" and counts exactly two `not-transferable-as-stated` marks in section 8 (8.1.2, 8.2.2), not including this line; (3) line 948 resolves a structurally identical venue-structural question the opposite way — "the corpus cannot settle that from the documentation it retrieved (section 9)" — citing the same section. The only construction that would rescue the line, inferring endpoint settlement from DCM designation plus FR document titles, is barred by section 8 reading rule 2, which forbids inference beyond what an abstract or metadata states. No concrete counter-evidence exists.

### REV-1-4 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1304-1307
> **issue:** A single T5 preprint read at abstract depth is reported as having established a fact about the venue, and that asserted fact is then used to discharge the carrying assumption of a separate generalized claim. The frozen protocol's tier rule is tier-blind admission with tier-labelled use and states in terms that no preprint-tier claim is reported as settled. 'Establishes' is exactly the settled-claim verb. The chain is compounded: it licenses the Shin insider-trading FLB mechanism onto Kalshi at the same time that 8.3.2's Berkowitz line states odds-with-embedded-margin results do not transfer to a cent-denominated exchange.
> **evidence:** "Carries wherever a quote-setter faces informed order flow, which the Kalshi adverse-selection evidence in 8.4.1 establishes is the case there — this is the corpus's strongest cross-strand link between a generalized mechanism and a Kalshi-measured primitive."
> **fix:** Downgrade the verb and carry the tier: 'one T5 preprint, at abstract depth, reports informed price impact on the venue (Bartlett & O'Hara 2026); if that measurement holds, the Shin mechanism's precondition is met. The corpus does not treat a single preprint-tier abstract as establishing the precondition.' Delete the superlative 'strongest cross-strand link' or restate it as a hypothesis for the successor stage.
> **reference:** CHAMP item 25 (indecisive evidence not read as established); frozen protocol §2.5 evidence-tier vocabulary

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation obtained; every checkable component of the finding reproduced. (1) The evidence string is verbatim at lit_review_kalshi-arbitrage_2026-09-02.md:1304-1307, including the verb "establishes" and the superlative "the corpus's strongest cross-strand link". (2) The referenced 8.4.1 support is preprint-tier only: the informed-price-impact measurement is sourced solely to "(Bartlett & O'Hara 2026, T5 preprint, abstract depth)" at lines 1345-1357, corroborated by corpus table row 723 ("T5 | K | S6 | abs"); the other two 8.4.1 entries (Burgi et al. 2025, Gupta 2026) are likewise T5, so no T1 source exists in 8.4.1 that could bear "establishes". (3) The frozen protocol rule is as quoted — protocol_kalshi-arbitrage-review_2026-09-02.md section 2.5 (~line 281): "Tier-blind *admission* with tier-labelled *use* is the operationalization: no preprint-tier claim is reported as settled, and the tier travels with the claim into the corpus record's role column." Line 1304-1307 carries neither tier nor depth label on the asserted venue fact. (4) I searched for a countervailing hedge and found none: section 10 gaps G-1..G-7 and section 11 contain only the global concession in G-6 that the Kalshi block is "thin in peer-reviewed tier"; no caveat attaches to this specific cross-strand link, and the protocol requires the tier to travel with the claim, not with the document. (5) Counter-test on internal consistency reinforced rather than undercut the finding: Shin 1992 (10.2307/2234526) appears twice with contradictory transfer verdicts — at line 1053-1056 (section 8.1.2) "Both carry only to venues whose price is an odds quote containing a bookmaker's margin (E6 = bookmaker fixed-odds book)", versus the Kalshi transfer asserted at 1302-1307. Only defect located in the finding is a section locator slip: the Berkowitz et al. 2017 cent-denominated-exchange non-transfer line is at line 1046-1050 in section 8.1.2, not section 8.3.2 (which begins at line 1247). The quoted substance of that line reproduces verbatim, so this is a mis-citation inside the finding's supporting argument, not grounds to drop the defect claim.

### REV-1-5 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:590-591 (vs :628)
> **issue:** The flow narrative asserts that every screened record was read, which the amendment-A3 disclosure contradicts. 5,249 of 8,813 records — 60% of the screened universe and at least 78% of the 6,707 X1 exclusions — received their verdict from a deterministic token rule, not from a screener reading a title. The two statements sit 38 lines apart in the same artifact and a reader auditing the screening from the flow narrative alone gets the wrong picture of what happened.
> **evidence:** ":590: "All 8,813 were screened at title level (and at abstract level where an abstract had been retrieved)." versus :628: "a 5,249-record DEFAULT-X1 stratum verdicted X1 by rule"
> **fix:** Rewrite the flow sentence as: '2,905 records in the forward-citation-only stratum plus the 659 records outside it were read individually at title level (and at abstract level where an abstract had been retrieved); the remaining 5,249 received a DEFAULT-X1 verdict from the amendment-A3 token rule without individual reading.' State the split again in the section 6 per-code table.
> **reference:** CHAMP item 20; PRISMA 2020 item 8 (automation tools and how they were used)

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation obtained; the finding reproduces in full. (1) Both quoted strings match verbatim at the stated lines (590 and 628; 38 lines apart). (2) Recomputing from docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl (8,813 verdict rows) confirms every number: rule R2 = "DEFAULT-X1 stratum of amendment A3 (no in-scope vocabulary token in title or abstract) -> X1" applies to exactly 5,249 records, all arms == ["forward-citation"]; the forward-citation-only stratum is exactly 8,154 (8,154 - 5,249 = 2,905 REVIEW; 8,813 - 8,154 = 659 outside); primary_code X1 totals 6,707, giving 5,249/8,813 = 59.6% and 5,249/6,707 = 78.3%, so "60%" and "at least 78%" are both correct. (3) The artifact's own JSONL header states the distinction the flow sentence elides: "The screener read every record in the topical / known-item / supplementary set and in the amendment-A3 REVIEW stratum... The DEFAULT-X1 stratum was verdicted by rule per amendment A3." (4) The only candidate refutation - that line 590 says "screened" rather than "read", so a deterministic token rule might qualify as title-level screening - fails against the frozen protocol docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md sec 4.2, which defines screening as "One agent session - the executing research-librarian - screens the entire deduplicated record universe against section 2", with "Stage 1 - title/abstract. Every deduplicated record receives one of include, exclude ..., or promote. Each verdict cites the section 2 criterion or decision rule ... by identifier." Line 590 therefore restates the pre-amendment design without carrying the A3 deviation. (5) grep for "pre-sorter", "REVIEW stratum", "by rule", "individually" returns only lines 28 (frontmatter), 628, and 2055 - the split is disclosed nowhere in or adjacent to the flow paragraph, and nowhere in the section 6 per-code table. Separate adjacent tension noted but not refuting: line 2055 says 3,300 of the 8,154 "had already been read individually and retain their individual verdicts" while the REVIEW stratum is 2,905, implying at least 395 already-read records sit inside the 5,249 count; the contradiction at line 590 holds at either magnitude.

### REV-1-6 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:628, :650, :2055
> **issue:** The A3 pre-sorter's actual reach is not recoverable from the record. The stated partition (2,905 REVIEW + 5,249 DEFAULT-X1 = 8,154) cannot be reconciled on the page with the amendment note that 3,300 records had already been read individually and retain their verdicts: at least 395 already-read records must sit inside the 5,249, so the number of records whose ONLY verdict is machine-rule-derived is somewhere between 4,854 and 5,249 and is never stated. The section 6 per-code table compounds this by reporting X1 = 6,707 as a single number with no read/rule split. Without that number a reader cannot size the residual risk that 13.1 correctly calls unquantifiable.
> **evidence:** ":2055: "Partly — 3,300 of the 8,154 had already been read individually and retain their individual verdicts; no verdict was reversed" against :628: "partitioned the 8,154-record forward-citation-only stratum into a 2,905-record REVIEW stratum read individually by the screener and a 5,249-record DEFAULT-X1 stratum verdicted X1 by rule"
> **fix:** Publish the exact count of records whose sole verdict is the token rule (derivable from ka-screening-verdicts.jsonl by counting rows whose verdict source is the pre-sorter), reconcile it against the 3,300 already-read figure, and split the X1 row of the section 6 table into read-verdicted and rule-verdicted sub-rows.
> **reference:** PRISMA 2020 item 8; PRISMA-S item 15; CHAMP item 20

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation found; every check I ran confirmed the finding.
>
> 1. Quotes reproduce verbatim. C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:628 states the partition "into a 2,905-record REVIEW stratum read individually by the screener and a 5,249-record DEFAULT-X1 stratum verdicted X1 by rule"; :2055 states "Partly — 3,300 of the 8,154 had already been read individually and retain their individual verdicts". :650 table row is "| X1 | 6,707 | ..." as a single unsplit number.
>
> 2. Arithmetic holds. 2,905 + 5,249 = 8,154 (full stratum), and the 3,300 already-read are stated as drawn from that same 8,154, so |already-read ∩ DEFAULT-X1| >= 3,300 - 2,905 = 395. The overlap is forced, not speculative.
>
> 3. Counter-test on the cited artifact contradicts refutation rather than supporting it. Parsing docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl (8,813 rows): rule counts are R2=5,249, R8=1,458, and X1 splits exactly as (X1,R2)=5,249 / (X1,R8)=1,458. Every row carries only {id, citation, identifier, stage_excluded, verdict, primary_code, secondary_codes, criterion_cited, rule, reason, arms} — there is no field marking whether a record had been individually read. The header "counts" block reports only per-code totals (X1: 6707). So the JSONL cannot separate read-verdicted from rule-only records inside the 5,249; the auditor's own suggested derivation is not actually executable on the published artifact, which strengthens rather than weakens the defect claim.
>
> 4. The archived generator confirms the conflation is by construction. docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py assigns rule R2 to any uid in DEFAULT_X1 unconditionally ("elif uid in DEFAULT_X1: v, code, rule = 'exclude', 'X1', 'R2'"), with no branch for previously-read records.
>
> 5. The amendment file states the conflation explicitly. ka-protocol-amendments.md §A3 Execution stage: the pre-sorter "applies to the remainder and, for consistency of the published partition, is also recorded for the already-read records so that the partition is reproducible over the whole stratum." That is precisely the claim that 5,249 overstates the pre-sorter's exclusive reach.
>
> 6. No statement of the true count exists anywhere. grep for 5,249/5249/4,854/4854/3,300/3300/1,458/1458/"by rule"/"individually-read" across the lit review returns only lines 628 and 2055; no artifact under docs/literature/search_logs/kalshi-arbitrage/ records the identity of the 3,300 already-read records (the "3300" grep hits in ka-fc-oa-*.json, ka-openalex-*.json, ka-ki-*.json are incidental numeric matches in raw API dumps, not a read-set roster).

### REV-1-7 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991 (vs :711-859)
> **issue:** The disclosure of the Kalshi evidence base's thinness understates it against the artifact's own corpus table. Of the 19 records flagged E4/E15 = K, exactly two are T1 (Goel 2026, Subramanian 2026) and 17 are T5, not 15. The non-independence disclosure is also incomplete: it names the five-record Krause cluster but not the two-record Lee cluster (10.2139/ssrn.6748186 and 10.2139/ssrn.6964226, both 'Lee, Lee & Lee 2026'), so 7 of 19 Kalshi records come from two author groups, not 5 of 19 from one. A limitation stated at less than its true size is a reporting defect in the direction that flatters the corpus.
> **evidence:** "Five of the nineteen Kalshi-specific records share a first author, and fifteen of the nineteen are T5 preprints or working papers."
> **fix:** Correct to 'seventeen of the nineteen are T5 preprints or working papers; the only two peer-reviewed-tier Kalshi records are Goel 2026 and Subramanian 2026' and 'seven of the nineteen come from two author groups (five Krause, two Lee)'. Repeat the corrected counts at the 8.3.1 concentration caveat (:1238-1240), which carries the same wrong number.
> **reference:** CHAMP item 23; RQI presentation dimension

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation. Attempted counter-test confirmed the finding instead. Programmatic extraction of all corpus-table rows with E4/E15 = K yields exactly 19 records; the table's own tier column gives T1 = 2 (goel2026jiref2026105, subramanian2026ijfmd2026100) and T5 = 17, contradicting line 1989's "fifteen of the nineteen are T5 preprints or working papers." All 17 non-T1 K records are SSRN/arXiv preprints or working papers (Bürgi/CESifo, Diercks/NBER), so no narrower reading of "preprints or working papers" recovers 15. Author check against references_kalshi-arbitrage.json: the five krause2026ssrn* records are sole-authored "David Krause"; lee2026ssrn6748186 (Seungju Lee, Yebon Lee, Jaewook Lee) and lee2026ssrn6964226 (Jaewook Lee, Yebon Lee, Seungju Lee) are the same three-author group with permuted order — 7 of 19 from two groups, only the Krause 5 disclosed. The same wrong count is repeated at lines 1239-1240. Sole nuance found, insufficient to refute: the Lee pair do not literally share a *first* author (Seungju vs Jaewook), so the artifact's phrase "share a first author" is not itself false for the Krause cluster; but the finding's charge of an incomplete non-independence disclosure and the 15-vs-17 tier miscount both stand.

### REV-1-8 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:24-25, :34-35, :51-58, :576-579
> **issue:** The artifact's machine-readable and first-read surfaces misstate the flow that its prose later corrects. The frontmatter lists X10 and X11 under the key `eligibility_exclusion`, which is the exact opposite of what section 1 says they are ('not eligibility criteria'), and publishes `n_excluded: 8664` — a figure containing 1,188 records the body calls capacity dispositions and 643 whose eligibility is undecided. The section 5 identity table repeats 8,664 with no split. The 'Read this first' block, the only summary a reader may read, names the absent risk-of-bias table and the absent agreement statistic but names neither of the two limitations the body calls largest: 1,188 records unresolved at end of screening, and zero full texts read. Any downstream tool or reader consuming the frontmatter alone will treat 149/8,813 as a completed screen.
> **evidence:** ":24-25: "X10 (amendment A4) ELIGIBLE ... X11 (amendment A5) ELIGIBILITY UNDECIDED" listed under `eligibility_exclusion:`; :34 "n_excluded: 8664"; against :591-593 "1,188 are capacity dispositions, not criterion failures ... this is the single most important number in the flow"
> **fix:** Move X10/X11 out of `eligibility_exclusion` into a separate frontmatter key (e.g. `disposition_codes_non_criterion`), add `n_criterion_excluded: 7476`, `n_capacity_disposition: 1188` and `n_eligibility_undecided: 643` to the frontmatter, split the section 5 identity table row the same way while showing that the frozen identity still closes, and add two sentences to 'Read this first': no full text was read for any included record, and 1,188 records reached the end of screening unresolved of which 643 have undecided eligibility.
> **reference:** PRISMA 2020 items 16a and 2; CHAMP item 23; PRISMA-S item 15

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; every claimed location reproduces verbatim. (1) docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:13 opens `eligibility_exclusion:` and lines :24-25 place X10 ("ELIGIBLE under section 2 and NOT a criterion failure") and X11 ("ELIGIBILITY UNDECIDED and NOT a criterion failure") inside that key, while :84-88 states "Two disposition codes were added during execution (amendments A4 and A5) and are **not** eligibility criteria" and :71-72 asserts the eligibility criteria are what is restated under that key — a direct contradiction. (2) :34 is `n_excluded: 8664`; a grep of the whole file shows 7476/1188/643 appear only in body prose (:591-592, :643-669, :2080-2081) and in no frontmatter key — there is no n_criterion_excluded / n_capacity_disposition / n_eligibility_undecided. (3) :576-579 identity table carries the single undifferentiated row "8,813 - 8,664 = 149" with no split. (4) The "Read this first" block :51-57 names only the absent inter-rater agreement statistic and the absent risk-of-bias table; it does not mention that no full text was read or that 1,188 records were unresolved. (5) The body designates exactly those two as its most important disclosures: :591-593 "1,188 are capacity dispositions, not criterion failures (545 X10 + 643 X11) — this is the single most important number in the flow"; :2065 section heading "The largest limitation: extraction depth and extraction coverage"; :2069 "No full text was read."; :2080 "1,188 records that reached the end of screening were not resolved." Arithmetic verified: 545+643=1,188; 8,664-1,188=7,476; 8,813-8,664=149. No counter-test or source reading contradicts the defect claim.

### REV-1-9 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2112-2128
> **issue:** The known-item recall interpretation is contradicted by the artifact's own query list and its excusal of three misses is over-broad. (a) The supporting premise is factually wrong: no query in section 3 contains the token 'parimutuel' — it appears in the protocol's vocabulary paragraph but was never operationalized in any of the 35 topical queries — so the Thaler & Ziemba miss is at least as consistent with a vocabulary gap as with a depth cap, and the depth-not-vocabulary reading loses its stated evidence. (b) The three 'structural, not a recall failure' items are excused on the ground that a citing set cannot contain its own anchor. That argument covers only the forward-citation arm; the 35 topical queries and the supplementary arms also failed to retrieve Oliven & Rietz, Glosten & Milgrom and Levitt, and that failure is unexcused. The honest count of topical-strategy misses is 7 of 23, not 4.
> **evidence:** "two are S3 classics whose titles use vocabulary the strategy carries (\"parimutuel\", \"betting markets\"), so their non-retrieval indicates the retrieval **caps** rather than the vocabulary"
> **fix:** Delete 'parimutuel' from the vocabulary-carried claim or add the query that carries it; restate the interpretation as undetermined between cap and vocabulary, since the strategy contains no query that would have retrieved Ho & Stoll's title terms either. Re-label the three anchor items as 'not recoverable by the forward-citation arm they define; also not retrieved by any topical query, which is an unexcused topical-strategy miss', and report the topical-arm miss count as 7 of 23 alongside the 16-of-23 any-arm figure.
> **reference:** CHAMP item 29; PRISMA-S item 14 / PRESS 2015 known-item check

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; both premises reproduce.
>
> (a) Verified by exhaustive read of section 3 (docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:239-528) plus `grep -i "parimutuel|pari-mutuel"` over the whole file and over all 86 stored logs. The token appears in the artifact only at lines 680-681, 684, 781-858 (record titles), 1158-1958 (synthesis prose) and 2118/2121 (the disputed passage) — never inside a fenced query. A programmatic scan of the `url` field of every JSON in docs/literature/search_logs/kalshi-arbitrage/ returned zero matches for "mutuel"; the ten log files that contain the substring hold it only in retrieved-result titles. The token's only strategy-side occurrence is the protocol's vocabulary list, docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:433, which declares it but never operationalizes it. So the claim at line 2121 that the strategy "carries" parimutuel is unsupported by any executed query.
>
> Partial mitigation found (does not refute): the other half of the parenthetical does hold — ka-crossref-05 is `...query.bibliographic=favorite+longshot+bias+betting+markets+explanations...`, and both KI-06 ("Historical Presidential Betting Markets") and KI-09 ("Anomalies: Parimutuel Betting Markets...") carry "betting markets" in their titles. The depth-cap reading therefore retains some support via that token, but the finding's stated defect — the "parimutuel" half is factually wrong, and no query exists for it to have "sat below the rows=20 cut" on — is true as written.
>
> (b) Verified against docs/literature/search_logs/kalshi-arbitrage/ka-known-item-recall.json. All seven non-retrieved items, including the three anchors, carry `"independent_query_ids": []` — KI-01/A1, KI-18/A6, KI-23/A5 alongside KI-06, KI-09, KI-20, KI-21. Empty lists mean no topical, supplementary or other forward-citation arm retrieved them either, so the "structural, not a recall failure" excusal at lines 2113-2117 covers only the anchor's own citing-set arm and leaves the topical-arm miss unstated. The same over-broad wording is duplicated in that log's `structural_note` ("their non-retrieval is structural, not a vocabulary failure"). No disclosure elsewhere blunts it: section 4 (line 561) repeats only "16 of 23 ... with the seven misses itemized and interpreted in section 13.4".

### REV-1-10 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** interpretation
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1963-1968, :1975-1979, :1368-1371, :1768-1773
> **issue:** Corpus-level absence claims are stated without the depth and screening qualifiers that the same artifact establishes elsewhere. 'No record in the corpus measures or models the cost of capital locked in an event-contract position', 'There is no market-making model fitted to Kalshi' and 'the corpus contains no record that measures the capital-lockup cost' are universal negatives over 149 records of which 33 were seen only as title/venue/year and none at full text — a record can measure capital lockup without saying so in its abstract, which is the exact 'not mentioned versus not stated in the abstract' indistinguishability declared at 13.2. None of these gap statements is conditioned on the 5,249-record un-read A3 stratum whose residual risk 13.1 calls unquantifiable, nor on the 545 X10 / 643 X11 records. The 'absence of evidence, not evidence of absence' caveat attached to G-2 disclaims a statement about the world but not the statement about the corpus, which is the one actually at risk.
> **evidence:** "**No record in the corpus measures or models the cost of capital locked in an event-contract position until settlement.** `ka-crossref-10` was written for exactly this and returned nothing eligible. Absence of evidence, not evidence of absence."
> **fix:** Restate every corpus-level absence with its two qualifiers, e.g. 'no retrieved abstract among the 116 abstract-depth records states a measurement of capital-lockup cost; the 33 metadata-depth records, the 545 X10 and 643 X11 records, and the 5,249 records verdicted by the A3 token rule were not assessed for it.' Apply the same edit to G-4, to the 8.4.1 'no record specifies a market-making model fitted to Kalshi' bullet, and to the 8.5.2 capital-lockup bullet.
> **reference:** CHAMP item 25 (indecisive read as indecisive) and item 28; frozen protocol §5 field E12

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; the finding reproduces at all four cited locations and no counter-evidence was obtained.
>
> Reproduction (C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md, 2177 lines):
> - 1963-1968 (G-2): "No record in the corpus measures or models the cost of capital locked in an event-contract position until settlement." Followed only by "Absence of evidence, not evidence of absence." No depth or stratum qualifier.
> - 1975-1979 (G-4): "There is no market-making model fitted to Kalshi." No qualifier.
> - 1368-1371 (8.4.1): "No record in this corpus specifies a market-making model fitted to, or calibrated on, Kalshi." No qualifier.
> - 1768-1773 (8.5.2): "the corpus contains no record that measures the capital-lockup cost ... and no record that states a collateral or margin rule" plus "the search returned nothing eligible."
>
> Candidate refutations tested, all fail:
> 1. Section 10 preamble (:1952) reads "Stated as gaps — absences of evidence — never as findings about the world." This is exactly the world-scoped caveat the finding identifies as insufficient; it disclaims nothing about corpus scope, depth, or unscreened strata.
> 2. Section 8 reading rule 2 (:867-870) is a binding depth qualifier, but it is scoped to positive transcription ("Every statement below is a statement about what a record's abstract or metadata says"), does not govern corpus-level negatives, does not reach sections 10/11, and never mentions X10/X11/A3.
> 3. Grepping the whole of section 10 (1950-1996) for X10, X11, A3, "5,249", "abstract depth", "un-read" returns a single hit — "did not read them" inside G-5 — which is a different gap (inventory-risk lineage anchors). G-5 therefore demonstrates the artifact applies exactly the qualifier pattern the finding asks for, and does not apply it to G-2 or G-4. This corroborates rather than refutes.
> 4. The underlying facts the finding relies on are confirmed in the same artifact: 13.2 §1 (:2069-2078) states abstract depth for 116 of 149, metadata depth for 33, no full text, and that E12 "not mentioned" is "not distinguishable from 'not stated in the abstract' for most records"; 13.2 §2 (:2080-2087) states 545 X10 + 643 X11 unresolved; :628 and :2055 state the 5,249-record DEFAULT-X1 rule stratum.
>
> One argument partially cuts toward the artifact and was considered: "the corpus" is a defined term (149 included records, :592-594), so a claim scoped to it is literally true irrespective of X10/X11/A3. That is a scope-of-term argument, not counter-evidence, and it does not touch the depth limb, which stands on its own. It is also undercut by two adjacent statements that exceed corpus scope: 8.5.2's "the search returned nothing eligible" conflicts with X10 being coded "ELIGIBLE, not a criterion failure" (:656), and TC-3 (:~2004) asserts "it is a genuine open computation, not a literature-retrieval failure" — a claim about the world that the 545 eligible-unextracted and 643 unassessed records cannot support.

### REV-1-11 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:137 (vs :216-218 and :2099)
> **issue:** The primary search-provenance table records the wrong HTTP status for a documented access gap. The row for ka-fc-s2-a3 shows http 200, while the PRISMA-S 5 narrative and access gap AG-4 both state HTTP 404 for that anchor. The table is the artifact's PRISMA-S item 1/2/13 audit surface and the row is the one a reader would check to verify the gap; as written the gap is invisible in the table and a reader reconciling table against narrative finds a contradiction with no way to resolve it from the page.
> **evidence:** ":137: "| Semantic Scholar | ... | ka-fc-s2-a3 | 0 | not reported | 200 | cursor/offset paged, 1 pages |" against :216-218: "the Semantic Scholar arm returned 156, 39, 535, 426 and 6,147 for A1, A2, A4, A5 and A6 and **HTTP 404 for A3** (`10.1086/655844` is not indexed by that service)"
> **fix:** Correct the http column for ka-fc-s2-a3 to 404 against the stored log, remove the misleading 'cursor/offset paged, 1 pages' note, and add 'AG-4' to the note column so the table row points at its own gap entry. Re-check every other row's http value against its stored ka-*.json in the same pass.
> **reference:** PRISMA-S items 1, 2, 8; CHAMP item 23

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; the finding is confirmed by three independent checks I ran myself.
>
> 1. Table row reproduced verbatim at C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:137 — "| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a3 | 0 | not reported | 200 | cursor/offset paged, 1 pages |". Header at :100 is "| source | platform | date_searched | query_id | n_records | platform_total_hits | http | note |", so column 7 ("200") is unambiguously the http column. No column-misread defense is available.
>
> 2. Both narrative sites reproduced and contradict it. PRISMA-S 5 at :216-218 states the Semantic Scholar arm returned counts for A1, A2, A4, A5, A6 "and **HTTP 404 for A3** (`10.1086/655844` is not indexed by that service)". AG-4 in the section 13.3 access-gap table states "Semantic Scholar forward-citation arm for anchor A3 (`10.1086/655844`) | HTTP 404 — the service does not index that identifier".
>
> 3. Decisive counter-check against the stored provenance log, which the table is supposed to transcribe: C:\Users\skoir\castles\docs\literature\search_logs\kalshi-arbitrage\ka-fc-s2-a3-p001.json records protocol_query_id "ka-fc-s2-a3", http_status 404, total_hits null, retrieved_count 0, retry_attempts 6, and raw.error "Paper with id DOI:10.1086/655844 not found". The stored log agrees with the narrative and disagrees with the table, so the table row — not the narrative — carries the error. The row's note "cursor/offset paged, 1 pages" is likewise unsupported: nothing was paged, the request 404'd.
>
> 4. No reconciling row exists elsewhere. grep for "ka-fc-s2-a3" across the artifact returns only :137 (the wrong row) and :355 (the verbatim query block), so a reader cannot resolve the contradiction from the page, exactly as the finding states.
>
> The defect claim is true as written: wrong HTTP status on the PRISMA-S item 1/2/13 audit surface, contradicting both the narrative and the stored log.

### REV-1-12 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** consistency
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:563-566 (vs :2098)
> **issue:** The record's own summary of why recall is not demonstrated omits the largest of its three recall failures. Section 4 lists the missing peer review, the single unresolved forward-citation anchor and the unexecuted backward arm, but not AG-3 — that all four Semantic Scholar topical queries and all eight retries returned HTTP 429, so one of the four protocol-named bibliographic databases contributed zero records to the topical strategy. A reader who reads section 4 as the recall statement, which is what it is written to be, is told a smaller story than section 13.3 tells.
> **evidence:** ":564-566: "**recall is not demonstrated** — the strategy was not peer reviewed, one of the six forward-citation anchors could not be resolved on the Semantic Scholar arm, and the backward citation-chasing arm did not execute at all" against :2098: "**One of the four named bibliographic databases contributed zero records to the corpus.**"
> **fix:** Add AG-3 to the section 4 mitigation-(iv) sentence as the first item, and state the recall consequence in terms of the strategy: the four Semantic Scholar topical queries carried the unrestricted forms of 'market making inventory risk binary event contracts' (the ka-s2-02 pairing that section 3's PRISMA-S 9 statement relies on to argue no vocabulary is category-gated out of the strategy) — so the arXiv `cat:q-fin*` narrowing on ka-arxiv-03 and ka-arxiv-05 is, in execution, no longer offset as that paragraph claims.
> **reference:** PRISMA-S items 3 and 14; CHAMP item 29

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; the finding reproduces exactly. Section 4 of docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md spans lines 550-567 in full (next heading "## 5. Managing records" is at line 568), so the section is a single paragraph and there is no other sentence in it that could carry the omitted item. Lines 563-566 read: "(iv) this record states, in these words, that **recall is not demonstrated** — the strategy was not peer reviewed, one of the six forward-citation anchors could not be resolved on the Semantic Scholar arm, and the backward citation-chasing arm did not execute at all." Those three items map to the peer-review deviation, AG-4 (line 2099) and the non-executed backward arm. A grep for "ka-s2" and "Semantic Scholar" across the file returns hits at lines 135-140, 176-187, 212, 215, 246, 472-505, 523, 565, 599, 2098, 2099, 2103 — the only hit inside 550-567 is line 565, which is AG-4. AG-3 therefore appears nowhere in section 4. Line 2098 states AG-3's consequence as "**One of the four named bibliographic databases contributed zero records to the corpus.**", and lines 176-187 confirm all twelve ka-s2-01..04 rows (frozen + -b + -c) returned n_records 0 with HTTP 429. The auditor's supporting cross-reference also checks out: line 523 lists `ka-s2-02` among the four queries said to carry the unrestricted forms that offset the arXiv `cat:q-fin*` narrowing on ka-arxiv-03/ka-arxiv-05, and that query returned zero. (The other three offsetting queries — ka-crossref-07, ka-crossref-11, ka-openalex-06 — did execute, which bears only on the wording of the proposed fix, not on the defect claim.) No source check, counter-test or logical argument disproves the claim that section 4's recall statement omits the AG-3 zero-contribution database failure.

### REV-1-13 — retained

- raised_by: critical-reviewer; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** design
> **location:** docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1064-1087, :1202-1205; docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2044-2058
> **issue:** The frozen amendment procedure was not followed and the deviation is not itself declared. Protocol §10 requires every deviation to be recorded 'in the addendum below', names the addendum 'APPEND-ONLY ADDENDUM BELOW THIS SECTION', and specifies five required elements per amendment including the reason and the PRISMA-P item(s) touched. The protocol's addendum is still empty; all five amendments live in a separate untracked-by-the-registration-hash log file, so a reader who verifies sha256 99524df0... obtains a protocol whose text asserts an amendment mechanism and shows no amendments. The corpus record's §13.1 enumeration, which is the only in-deliverable record, omits two of the five required elements (the reason, and the PRISMA-P item touched) for all five amendments.
> **evidence:** "protocol :1202: "## Addendum (append-only; empty at freeze)" with no entries, against protocol :1071 "recorded as a **numbered, dated, append-only amendment** in the addendum below" and corpus :2048 "none an edit to the frozen protocol file"
> **fix:** Either append A1-A5 to the protocol's addendum and record the resulting new SHA-256 in a follow-on provenance commit that names the frozen hash it supersedes, or add a numbered amendment A0 stating that the addendum mechanism was displaced by an external amendment log in order to preserve the registration hash, with the reason. Either way, add the missing 'why' and 'PRISMA-P item(s) touched' columns to the corpus's §13.1 table.
> **reference:** CHAMP item 6 (consistency with the pre-registered protocol); frozen protocol §10

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; finding reproduced in full. (1) sha256 of docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md = 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4, matching the registration hash, so the inspected file is the one a verifier obtains. (2) Protocol :1064 header reads "## 10. Amendments policy — APPEND-ONLY ADDENDUM BELOW THIS SECTION"; :1071 requires every deviation "recorded as a **numbered, dated, append-only amendment** in the addendum below", with element 3 "why;" and element 5 "which PRISMA-P item(s) it touches." (3) Protocol :1202-1204 is EOF (file is 1204 lines) and contains only "## Addendum (append-only; empty at freeze)" plus the HTML comment template — zero entries. (4) All five amendments A1-A5 live in docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md, a separate file outside the registration hash; its header asserts "The frozen protocol file is NOT edited" but states no reason for the displacement and is not itself a numbered amendment. (5) Searched the frozen protocol for any provision authorizing an external amendment log — grep -i "amend" hits lines 17, 124, 163, 404, 1004, 1021, 1064-1087, 1098, 1204; frontmatter :17 states "Any post-freeze change is an amendment under section 10, never an edit to frozen text" and §9.2 maps PRISMA-P item 4 to section 10. No authorization for an off-file addendum exists, so the deviation is real and undeclared. (6) Corpus §13.1 table columns are exactly "# | date | what changed | stage decided | were affected records already screened?" — no reason column, no PRISMA-P column; grep -n "PRISMA-P" on the corpus returns a single hit at line 7 (frontmatter, unrelated to amendments), confirming no PRISMA-P item is attributed to any amendment anywhere in the deliverable; frontmatter protocol_amendments: (:28) likewise carries neither. Only nuance found: A2's "what changed" cell embeds a partial rationale ("added after both frozen GET queries returned HTTP 200 with an empty results page"), making "omits the reason for all five" marginally strong for that one row — a precision quibble, not counter-evidence. The PRISMA-P omission holds for all five, and the core procedural claim is confirmed.

### SCOPE-1-1 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** omitted
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:219-223 (prisma-s-5); docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:610-616
> **issue:** A protocol-mandated search arm (backward citation chasing, `ka-bc-{n}`) was not executed, and its non-execution was not recorded as a numbered append-only protocol amendment. The declared spec requires every deviation from the frozen protocol to take that form; amendments A1-A5 cover retry classification, the RePEc POST arm, the vocabulary pre-sorter and two disposition codes, and none covers the dropped arm.
> **evidence:** Spec: "deviations recorded as numbered append-only protocol amendments, never silently" (deliverable_spec line 129-130). Protocol: "Backward citation-chasing. The reference lists of INCLUDED C1 and C3 records are hand-checked ... each addition is logged with the carrier record (`ka-bc-{n}`)." Artifact: "the protocol's `ka-bc-{n}` backward citation-chasing arm was **not executed** ... This is a recall gap, recorded in section 13.3, not a silent omission." The amendment ledger (section 13.1) has no entry for it.
> **fix:** Add a numbered append-only amendment (A6) in ka-protocol-amendments.md recording the non-execution of the backward arm, its cause (no full text retrieved, so the arm had no input) and its recall consequence, and cite that amendment number at prisma-s-5 and 13.3. Do not execute the arm retroactively without a new dated log.
> **reference:** S-5 (lit review state: search provenance + amendment discipline), S-4 (search logs check)

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation found; the finding reproduces exactly. (1) The artifact at prisma-s-5 states the `ka-bc-{n}` backward citation-chasing arm was "not executed". (2) The frozen protocol section 3.3 states the arm in mandatory form ("The reference lists of INCLUDED C1 and C3 records are hand-checked ... each addition is logged with the carrier record (`ka-bc-{n}`)") and section 4.1 makes it one of the four arms whose union is deduplicated before screening; it is not written as conditional. (3) ka-protocol-amendments.md contains exactly five entries A1-A5 with the contents the finding describes; none concerns the backward arm (the only "A6" occurrences in that file denote the Glosten-Milgrom forward-citation anchor). Section 13.1 and the frontmatter both independently assert the amendment set is five. Section 13.3's gap table AG-1..AG-8 also has no backward-arm row; AG-5 records only "Full texts, all 149 included records | Not attempted within this execution". (4) The only candidate refutation — that non-execution was protocol-compliant because the arm's input set was empty for want of full texts — is foreclosed by the protocol's own section 10: "During execution, ANY deviation — a query that will not execute as written, a platform change, an eligibility edge the criteria do not decide, a cap change, a source that becomes unreachable, a decision rule that turns out not to decide — is recorded as a numbered, dated, append-only amendment", followed by "Silent deviation is a conduct violation." An arm rendered inoperable by an upstream non-retrieval is squarely within that enumeration. (5) The spec text is reproduced as quoted at deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md lines 128-135, and its check row certifies "the five deviations recorded as numbered append-only amendments A1-A5", carrying an explicit NOTE-exemption only for the X10/X11 unresolved-record residue, not for the dropped arm.

### SCOPE-1-2 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** changed
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2065-2090 (13.2), 2044-2057 (13.1)
> **issue:** The protocol's extraction stage was delivered in a different kind than specified: fields E8-E13 presuppose a stage-2 assessment of retrieved text, and none was performed for any of the 149 included records (abstract depth 116, metadata-only 33). The substitution is disclosed in 13.2 but was never converted into a numbered amendment. A4 amends only the extraction-*selection* rule and the Table X-full publication format; A5 covers only the 643 transfer-clause records. The decision that no included record would be read at full text has no amendment of its own.
> **evidence:** Artifact 13.2: "**No full text was read.** Extraction reached abstract depth for 116 of the 149 included records and metadata depth ... for the remaining 33 ... E8 ... E9 ... E10 ... E12 ... and E13 are therefore **partially completed at best**, and E12's 'not mentioned' value is not distinguishable from 'not stated in the abstract' for most records." Section 13.1 lists five amendments, none of which is that decision.
> **fix:** Record the zero-full-text extraction decision as its own numbered amendment with the date and stage at which it was taken, and add a one-line statement of it to the artifact frontmatter (e.g. an `extraction_depth:` key) so the constraint travels with the machine-readable header, not only with section 13.2.
> **reference:** S-5 (lit review state: synthesis over extracted records)

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation on four independent lines; all failed, and two of them corroborate the finding.
>
> 1. Quoted evidence reproduces verbatim. docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md 13.2 reads "**No full text was read.** Extraction reached **abstract depth for 116 of the 149 included records and metadata depth (title, venue, year) for the remaining 33**", and names E8, E9, E10, E12, E13 as "**partially completed at best**". Section 13.1 lists exactly five amendments (A1-A5) in its table; none is the zero-full-text decision.
>
> 2. Counter-test — does a sixth amendment exist anywhere? docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md contains exactly five `### A{n}` headers (lines 15, 47, 85, 142, 201): A1, A2, A3, A4, A5. `grep` for "A6" across the amendments file, docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md, and the protocol's append-only addendum (below section 10) returns nothing. No sixth amendment exists.
>
> 3. Counter-test — do A4/A5 in fact cover it? Read in full. A4 adds disposition code X10 plus the extraction-*selection* rule (which eligible records are extracted, per objective prioritization O1/O4/O5) and moves Table X-full to a machine-readable artifact. A5 adds X11 and is explicitly scoped: "C3 model records on non-in-scope instruments whose eligibility turns on the section 2.2 transfer clause ... Full-text stage-2 assessment was not performed for them" — the 643 promoted records only. Neither amendment states that zero of the 149 *included* records would be read at full text. The finding's scoping of A4 and A5 is accurate.
>
> 4. Best available refutation angle — "abstract depth is within spec, so no amendment is owed". This does not hold. Protocol section 5 (frozen) opens "Extracted by the executing agent for every included record" over fields E1-E17, and E8/E9/E10 demand the condition "exactly as the record states it, with the market-structure assumptions the record attaches to it", the reported figure "with the uncertainty as the record reports it", and "every applicability condition the record states" — none of which the artifact claims to have met (its own words: "partially completed at best"). Protocol section 10 is categorical: "During execution, **ANY** deviation — ... a decision rule that turns out not to decide — is recorded as a **numbered, dated, append-only amendment**", and "**Silent deviation is a conduct violation**". E17's "depth reached (abstract / full text)" is a per-record recording field, not a licence for a session-wide zero-full-text rule. Decisively, A4 and A5 were themselves raised as numbered amendments for structurally identical capacity-driven depth decisions ("section-5 extraction not performed within this execution session"; "stage-2 full-text assessment not performed within this execution session"), which fixes the record's own operative standard and makes the unnumbered treatment of the included-record depth decision an inconsistency rather than a defensible reading.
>
> 5. Frontmatter check: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md lines 1-57 carry no `extraction_depth` key or equivalent; the only depth statements there are eligibility criteria I4 and X8 ("retrievable at least to abstract depth"), which concern retrievability for screening, not extraction depth. `protocol_amendments:` enumerates A1-A5 and nothing else. The constraint travels only in section 13.2 prose and one reading rule at section 8 ("Extraction depth is abstract or metadata, never full text"), exactly as the finding states.
>
> No concrete counter-evidence obtained. Finding stands.

### SCOPE-1-4 — retained

- raised_by: scope-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** spec-conflict
> **location:** docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:14-25 (frontmatter `eligibility_exclusion`) vs :66-72 and :84-88 (section 1); docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:240-258 (X1-X9), :793-798 (Table X-full `primary_code` X1-X9)
> **issue:** The artifact's own frontmatter places X10 and X11 inside the `eligibility_exclusion` list, i.e. inside the restatement of the frozen eligibility criteria, while section 1 states in terms that they are "**not** eligibility criteria" and that the criteria "were not modified during execution". The frozen protocol enumerates X1-X9 only and bounds Table X-full's `primary_code` domain to X1-X9. The delivered artifact therefore both asserts and denies that the frozen criteria set changed.
> **evidence:** Frontmatter: "eligibility_exclusion: ... - \"X10 (amendment A4) ELIGIBLE under section 2 and NOT a criterion failure ...\" - \"X11 (amendment A5) ELIGIBILITY UNDECIDED and NOT a criterion failure ...\"". Section 1: "the eligibility criteria are fixed in the frozen protocol sections 1 and 2 and were not modified during execution"; "**Two disposition codes were added during execution** (amendments A4 and A5) and are **not** eligibility criteria."
> **fix:** Move X10/X11 out of `eligibility_exclusion` into a separate frontmatter key (e.g. `disposition_codes_added:`) that names their amendment numbers, so the frozen criteria list in the header is byte-faithful to the protocol and the added codes are visibly a disposition layer rather than a criteria edit.
> **reference:** S-5, S-2 (frozen protocol eligibility criteria)

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted on four independent lines; all failed. Every quoted element reproduces byte-for-byte at the stated locations.
>
> (1) Frontmatter reproduces. C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md line 14 is the key `eligibility_exclusion:`; lines 15-23 are X1-X9; lines 24-25 are exactly the quoted X10/X11 entries ("X10 (amendment A4) ELIGIBLE under section 2 and NOT a criterion failure: ...", "X11 (amendment A5) ELIGIBILITY UNDECIDED and NOT a criterion failure: ..."). So the added codes are inside the `eligibility_exclusion` list as claimed.
>
> (2) Section 1 reproduces. Line 65 is "## 1. Objective and eligibility". Lines 67-72 read "...the eligibility criteria are fixed in the frozen protocol sections 1 and 2 and were not modified during execution. They are restated in this record's frontmatter under `eligibility_inclusion` / `eligibility_exclusion` and are cited by identifier throughout." Lines 84-88 read "**Two disposition codes were added during execution** (amendments A4 and A5) and are **not** eligibility criteria." Both quoted passages are verbatim.
>
> (3) Attempted counter-reading — that `eligibility_exclusion` is defined somewhere in the artifact as the record's *exclusion-code domain* (which would legitimately include X10/X11, since amendment A4 puts X10 rows inside `n_excluded`) rather than as the frozen-criteria restatement. This fails: `grep -rn "eligibility_exclusion|eligibility_inclusion"` over the corpus record, the frozen protocol, and ka-protocol-amendments.md returns exactly three hits — lit review lines 8, 14, and 71. Line 71 is the only definition of what the key holds, and it says it holds the restated frozen criteria. No competing definition exists anywhere in the artifact set, and the frozen protocol specifies no frontmatter schema for this key at all.
>
> (4) Attempted counter-reading — that the artifact never *asserts* a criteria change because each frontmatter entry self-labels "NOT a criterion failure" and carries its amendment number. This is mitigation, not refutation, and it is actively contradicted by the artifact's own taxonomy. Amendment A4 (docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md) states: "Section 2.4 fixes nine exclusion codes X1-X9, all of them criterion failures" and X10 "is therefore added as a *disposition* code. No eligibility criterion is altered, added, removed, or reinterpreted." A3 likewise states "Neither the eligibility criteria nor the X-code definitions are changed." So the project's own amendment record classes X1-X9 as the exclusion/criterion-failure set and X10/X11 as a separate disposition layer — which is precisely the distinction the frontmatter placement collapses.
>
> (5) Protocol side reproduces. protocol_kalshi-arbitrage-review_2026-09-02.md §2.4 (approx. lines 240-258) enumerates exactly X1-X9 as bulleted definitions with no tenth or eleventh code; §4.3 (approx. lines 793-798) specifies Table X-full's column "`primary_code` (X1-X9)", bounding the domain to nine codes. `grep -n "X10|X11|disposition code"` over the frozen protocol returns zero hits, confirming the frozen text neither contains nor anticipates the added codes.
>
> Consequence still stands: the delivered corpus record uses X10/X11 as live `primary_code` values (lit review lines 656-657 report 545 X10 and 643 X11 rows; lines 687-688 show X10 rows in Table X-nearmiss), so the emitted values exceed the frozen protocol's declared domain while the frontmatter key that section 1 declares to be the byte-faithful restatement of the frozen criteria carries them. No concrete counter-evidence obtained. Finding stands as stated (severity not assessed).

### QUANT-1-1 — retained

- raised_by: quant-auditor; severity_claimed: critical; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** method
> **location:** C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:21-141; C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:621-639
> **issue:** Every screening disposition except the 149 includes and the single hand-verified X9 twin was produced by an undisclosed five-list keyword classifier, not by a screener reading records. The corpus declares only ONE rule-based stratum (the amendment-A3 DEFAULT-X1 partition, 5,249 records) and asserts that the 2,905-record REVIEW stratum and the 659 topical/known-item/supplementary records were 'read individually'. 3,414 dispositions are therefore rule outputs presented as individual screening verdicts, and PRISMA 2020 item 8's automation-tool declaration is materially incomplete.
> **evidence:** ka-screening-script.py assigns every non-include verdict from hard-coded EVENT/CONTRIB/MODEL/DEFI/ELICIT substring lists (R3-R8). I re-ran that logic over the rebuilt universe (PYTHONHASHSEED=0) using only the published vocabulary and the store's included DOIs and reproduced the published table exactly: {'include':149,'X10':546 (=545+the X9 twin),'X1':6707,'X11':643,'X5':159,'X3':35,'X2':338,'X7':236} vs published {'X1':6707,'X11':643,'X10':545,'X2':338,'X7':236,'X5':159,'include':149,'X3':35,'X9':1}. No individual reading is recoverable from any artifact; the verdicts header's claim that the rule set 'encodes that reading' is unfalsifiable and unsupported.
> **fix:** Add a numbered amendment declaring the full classifier (all five token lists, R0-R9) as the automation tool of record for all 8,664 non-include dispositions; correct the PRISMA item-8 block and section 6 to state that no record outside the 149 includes carries a read-based verdict; strike the A3 sentence 'every one of them was read individually'.
> **reference:** PRISMA 2020 item 8, Page et al. 2021 https://doi.org/10.1371/journal.pmed.1003583; frozen protocol section 4.2 (single-pass screening, each verdict cites a criterion) sha256 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation on four independent paths; all failed, and two of them independently corroborated the defect.
>
> (1) Mechanism, verified at source. ka-screening-script.py lines 21-44 define five hard-coded substring lists (EVENT, CONTRIB, MODEL, DEFI, ELICIT); lines 88-141 assign every disposition outside `X9` (1 hand row), `INCLUDE` (inc.json) and `DEFAULT_X1` (partition.json) from those lists via branches R3-R8, and lines 163-166 of the same file WRITE ka-screening-verdicts.jsonl, header included. The script is therefore the emitter of record, not a description of one.
>
> (2) The archived script is the executed script. diff of the live scratch copy (scratchpad/verdicts.py, mtime 11:26, i.e. the run that produced the 11:26 jsonl) against the committed docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py is empty apart from the 3-line path-redaction header comment. No hand-adjudication layer exists between reading and output.
>
> (3) Row tally confirms the 3,414 figure exactly. Over all 8,813 rows of ka-screening-verdicts.jsonl: rule R2 (DEFAULT-X1) 5,249; R0 (include) 149; R9 1; and R1 236 + R3 545 + R4 338 + R5 159 + R6 643 + R7 35 + R8 1,458 = 3,414 rows whose verdict is a token-list output. secondary_codes is empty on all 8,813 rows and no row carries any override field, so no read-based verdict is recoverable for any of the 3,414.
>
> (4) The disclosure claim holds. ka-screening-vocabulary.json publishes ONE flat 130-token list scoped to the A3 REVIEW / DEFAULT-X1 partition; it is not the five-list classifier (the DEFI list's uniswap/blockchain/cryptocurrency/yield-farming and the ELICIT list's delphi/crowdsourc/wisdom-of-crowd appear nowhere in it). lit_review lines 621-628 declare exactly two automation tools — the LLM screener and the A3 pre-sorter — and affirmatively state the 2,905-record REVIEW stratum was "read individually by the screener"; ka-protocol-amendments.md:99 and :133-134 repeat this ("read and verdicted individually by the LLM screener"; the 659 topical/known-item/supplementary records "every one of them was read individually"). grep across the lit review, protocol, amendments and ADR-0004 returns no mention of the five token lists or of R3-R8 as an automation tool; the only reference to ka-screening-script.py is an incidental path in the frontmatter `pip_freeze_sha256` field (line 43), not an item-8 declaration. Frozen protocol sha256 recomputes to 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4 as cited, and its section 4.2 (lines 763-771) names "the LLM agent itself" as the automation tool and requires each verdict to cite a criterion.
>
> One supporting sentence in the auditor's evidence did NOT reproduce, but it does not touch the defect. Re-running the exact archived logic (patched only for paths) against the scratch inputs yields include 149 / X10 420 / X1 7,252 / X11 413 / X5 113 / X3 50 / X2 251 / X7 164 / X9 1 with 1,120 per-record mismatches against the published table, not the exact match the finding claims; the same test over all nine rebuilt universe snapshots present (rf_works, works2-4, works_s1/s2, works_u1-u3) gives 729-1,128 mismatches and never an exact hit, because works.json was rebuilt at 12:10 (after the 11:26 verdicts run) and the title/abstract merge is not order-stable. This falsifies the auditor's "reproduced the published table exactly" wording — and, incidentally, the corpus record's own claim that the table is "reproducible byte-for-byte from the stored logs" — but the defect is established without it, by (1)-(4) above: the emitting script is archived, is byte-identical to the executed one, and assigns 3,414 dispositions from undeclared keyword lists that the PRISMA item-8 block does not name and that the A3 text contradicts by asserting individual reading. Not refuted.

### QUANT-1-2 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** numerical
> **location:** C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:40-42,107-108; C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:653
> **issue:** The X5 rule ('traded object is a token pair or liquidity pool, not an event claim; fails B-a') fires on unanchored substrings. 'dex' matches inside 'index' and 'amm' inside 'programming', so records with no DeFi content are published with a false criterion-failure reason. The affected records are C3 transfer-clause candidates in the corpus's largest strand.
> **evidence:** Recomputation over the rebuilt universe: 283 works contain 'dex' only as a substring of 'index'; of the 159 X5 rows, 42 have no word-boundary DeFi token at all — e.g. 'A symbolic closed-form solution to sequential market making with inventory', 'Adverse-selection considerations in the market-making of corporate bonds', 'Modeling the Impacts of Market Activity on Bid-Ask Spreads in the Option Market', 'Market microstructure of FT-SE 100 index futures'.
> **fix:** Re-run the classifier with word-boundary matching (\bdex\b, \bamm\b, \bdefi\b, \bcrypto), re-emit ka-screening-verdicts.jsonl, and correct the X5 count and the section 6 per-code table; the 42 reclassified records fall to X11 (undecided) at worst, not to a B-a criterion failure.
> **reference:** Frozen protocol section 2.4 X5 and section 2.1 B-a; published table ka-screening-verdicts.jsonl

Refutation attempt (outcome: failed; evidence_type `none`):

> Could not refute; the defect reproduced in full. (1) Mechanism confirmed at ka-screening-script.py:40-42 where DEFI holds bare "dex","amm","defi","crypto", matched by any_in via unanchored `t in b` (lines 52-53) and consumed by the X5 branch at lines 107-108. (2) Rebuilt the universe independently with the archived ka-universe-script.py + ka-dedup-script.py over the stored ka-*.json logs: 15,924 raw records -> 8,813 distinct works, matching the published header n_records=8813 and counts X5=159. (3) Over the rebuilt universe, 305 works contain substring "dex" and 276 contain it ONLY inside index/indexes/indexed/indexing (284 have no token starting with "dex"). (4) All four named exemplars are published with primary_code X5, rule R5, reason "traded object is a token pair or liquidity pool rather than an event claim; fails B-a", and none contains a real DeFi token: U03611 "Market microstructure of FT-SE 100 index futures" (only "index"), U01358 "Adverse-selection considerations in the market-making of corporate bonds" (only "index"), U00763 "Modeling the Impacts of Market Activity on Bid-Ask Spreads in the Option Market" (only "index"), U00079 "A Symbolic Closed-Form Solution to Sequential Market Making with Inventory" (only "programming", matching "amm"). (5) X5=159 is reproduced verbatim at lit_review_kalshi-arbitrage_2026-09-02.md:653. Only divergence: re-running with word-boundary anchoring I count 64 of 159 X5 rows lacking any word-boundary DeFi token (substring-only culprits: dex 29, defi 23 from define/definition, amm 13 from programming/gamma), versus the auditor's 42. That is a magnitude difference in the finding's favor, not a counter-example; one of my 64 (U02673 "Funding-Aware Optimal Market Making for Perpetual DEXs") is genuinely DeFi and was wrongly excluded by my stricter suffix rule, so the true figure sits between 42 and 64 - still far above zero. Incidental (separate from this finding): uid assignment is not reproducible across processes because ka-dedup-script.py:49 uses sorted({r['title']...}, key=len), whose ties depend on set iteration order and thus PYTHONHASHSEED; my rebuild disagreed with the published uid->title map on 3,884 of 8,813 records for that reason alone.

### QUANT-1-3 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** method
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:22,643-646,709-859,2069-2073
> **issue:** Eligibility-criterion drift without an amendment: 33 included records were retrieved only to title/venue/year ('meta' depth), which fails frozen criterion I4 and is exactly the case frozen exclusion X8 covers. The frontmatter restates X8 with an added clause not in the frozen protocol ('or full text unobtainable after the retrieval chain'), and section 6 then declares X8 unused because 'no full text was attempted and failed'.
> **evidence:** Frozen protocol lines 220-221: 'I4. The record is retrievable at least to abstract depth by the executing agent. Records retrievable only as a bare title are excluded under X8'; line 255: 'X8 - not retrievable to abstract depth. Fails I4.' Corpus table: depth counts abs=116, meta=33; AG-7 states abstracts were requested from five sources for those 33 and 'none returned one'. No amendment A1-A5 touches I4 or X8.
> **fix:** Either file a numbered amendment that explicitly relaxes I4 with its rationale and restates n_included, or exclude the 33 under X8 and re-derive n_excluded/n_included and the bibliography SHA; in both cases remove the frontmatter's unauthorized X8 rewording.
> **reference:** Frozen protocol sections 2.3 I4, 2.4 X8, and section 10 ('ANY deviation ... is recorded as a numbered, dated, append-only amendment')

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation. All claimed evidence reproduced, and every counter-avenue tested failed. (1) Frozen protocol docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md lines 220-221 read "I4. The record is retrievable at least to abstract depth by the executing agent. Records retrievable only as a bare title are excluded under X8"; line 255 reads "X8 - not retrievable to abstract depth. Fails I4." (2) Lit review line 22 frontmatter reads "X8 not retrievable to abstract depth, or full text unobtainable after the retrieval chain (fails I4)" - the trailing clause has no counterpart in the frozen text. (3) Depth counts confirmed by parsing the corpus table: abs=116, meta=33, sum 149 = n_included. (4) Section 6 declares X8 unused because "no full text was attempted and failed". (5) Access-gap AG-7 (line 2103) contradicts that on its own terms: abstracts for the 33 WERE requested from Crossref, OpenAlex, arXiv, Semantic Scholar and DOI content negotiation and "none returned one" - an attempt at abstract depth that failed, the literal X8/I4 trigger. (6) Amendments file ka-protocol-amendments.md: A1 eCFR interstitial, A2 RePEc POST arm, A3 vocabulary pre-sorter, A4 X10, A5 X11 - none touches I4 or X8; A4 and A5 both restate X8 in the reworded full-text sense ("X8 asserts a retrieval attempt that failed"). Counter-avenues closed: (a) I6/section 2.7 documentation-tier exemption does not cover these records - all 33 meta rows carry tier T1 (19) or T5 (14), the peer-reviewed corpus flow, e.g. berg2008s15740722070 (known item KI-05, T1); (b) the "bare title" reading of I4's second sentence is closed by X8's own definition line; (c) the protocol does not anticipate a metadata depth value - section 5 field E17 (line 837) enumerates only "depth reached (abstract / full text)", so the "meta" value is introduced by the review, not the frozen protocol.

### QUANT-1-4 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** method
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:24-25,85-88,656-657,2080-2086
> **issue:** The X10 and X11 strata are described in eligibility terms the execution cannot support. X10 is said to mark records that 'passed eligibility' (545 records) and X11 records 'promoted to stage 2' under the transfer clause (643 records). Both sets were assigned by token rules (R3: event-token AND contribution-token; R6: model-token AND no event-token), so no eligibility determination and no promotion decision was made for any of the 1,188 records.
> **evidence:** ka-screening-script.py R3/R6 branches; reproduction reproduces both counts exactly from tokens alone. Frozen protocol 4.2: 'a record is promoted iff its abstract does not settle I1/I2, and no record is promoted for any other reason' - a condition never evaluated for the 643.
> **fix:** Relabel X10 as 'keyword-identified candidate stratum; eligibility not assessed' and X11 as 'keyword-identified model-record stratum; neither stage-1 nor stage-2 assessment performed', and propagate the weaker wording to sections 5, 6, 13.2 and the amendments file.
> **reference:** Frozen protocol section 4.2 stage-1/stage-2 definitions; amendments A4, A5

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; every element of the finding reproduced. (1) ka-screening-script.py R3 branch is `if ev and co -> X10` and R6 is `elif mo -> X11`, where ev/co/mo are pure substring matches (any_in) over title+titles_all+abstract against the EVENT/CONTRIB/MODEL token lists; no eligibility predicate and no full-text step enters either branch. (2) Recounted the 8,813 rows of ka-screening-verdicts.jsonl: X10=545, X11=643 (sum 1,188), include=149 — matching lit review lines 656-657 and 2080-2086. (3) Protocol section 4.2 quote is verbatim: "a record is promoted iff its abstract does not settle I1/I2, and no record is promoted for any other reason"; R6's positive model-token match is not an undecidability test, so the 643 were promoted under a rule the frozen protocol forbids. (4) The eligibility wording is present at all four cited locations ("ELIGIBLE under section 2", "records that passed eligibility", "promoted to stage 2"). Counter-test ran against refutation: all 545 X10 rows share one distinct reason/rule/criterion_cited/stage_excluded value, as do all 643 X11 rows, so no per-record determination is stored; and direct inspection of X11 membership shows records that cannot be C3 model records at all — U00024 "Price Discovery under Disposition Sales" (J Financial Markets 2011), U00039 "Glued to the TV: Distracted Noise Traders and Stock Market Liquidity" (J Finance 2016), U00052 "Noise Traders" (NBER 2006), U00096 "Asset Price Dynamics with Limited Attention" (RFS 2010), U00101 "Asymmetric Trading Costs Prior to Earnings Announcements" (2017) — empirical papers that matched MODEL tokens such as "liquidity provision", "specialist" or "immediacy". The only available defense (lit review line 628: the LLM screener "decided every include / exclude / promote verdict", A3 pre-sorter confined to the 8,154-record forward-citation stratum; verdicts header: the rule set "encodes that reading") is contradicted by the archived script, in which only INCLUDE, DEFAULT_X1, X7SET and the single X9 twin are exogenous inputs while all X10/X11 verdicts are computed from tokens for every remaining record irrespective of stratum. No artifact records an individual eligibility or promotion determination for any of the 1,188.

### QUANT-1-5 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** assumption
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1249-1256,1279-1284,1539-1542,1929-1938,1969-1974
> **issue:** Three synthesis claims rest on Kalshi venue-structural facts the S7 stream explicitly did not establish, contradicting the corpus's own G-3 statement that only two claims are marked not-transferable-as-stated. The retrieved CFTC pages establish designation status/date and an intermediation-permission change only; S7-5 records fee, settlement, contract-specification, position-limit and membership facts as unestablished.
> **evidence:** 8.3.2: 'it holds at any venue whose contract settles at an endpoint - which the CFTC record establishes for Kalshi as a class of instrument (section 9)'; 8.3.2: 'Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9), so the supply-side channel as stated does not transfer'; 8.4.2: 'a continuous double auction, which is the microstructure the CFTC record associates with a designated contract market'. Section 9's own S7-1/S7-2 rows answer 'may it license a behavioural claim?' with 'No. It fixes the venue's regulatory category and its designation date, nothing else'.
> **fix:** Strike the three appeals to the CFTC record for settlement structure and trading mechanism, mark the affected transfers not-transferable-as-stated (Thaler-Ziemba endpoint premise, Levitt bookmaker-versus-exchange block, the CDA microstructure attribution), and correct G-3's count of not-transferable marks.
> **reference:** Frozen protocol section 2.7 constraints 1 and 4; section 8 corollary 2

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation found; the attempt to disprove instead corroborated the finding.
>
> 1) All three quoted passages reproduce verbatim at the stated lines of C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md: L1254-1256 ("...it holds at any venue whose contract settles at an endpoint - which the CFTC record establishes for Kalshi as a class of instrument (section 9) even though no rulebook was retrieved"), L1280-1284 ("Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9)"), L1539-1542 ("...a continuous double auction, which is the microstructure the CFTC record associates with a designated contract market"). Each attributes the venue-structural premise to the CFTC record, not to a corpus record; no adjacent qualifier withdraws the attribution.
>
> 2) I checked the primary retrieval logs the corpus itself cites as the whole of that CFTC record (docs/literature/search_logs/kalshi-arbitrage/ka-doc-03.json and ka-doc-04.json). Case-insensitive term counts over the served HTML: "double auction" 0/0, "order book" 0/0, "order-driven" 0/0, "auction" 0/0, "expir" 0/0. "settle" occurs 0 times in ka-doc-03 and twice in ka-doc-04, both in unrelated rows (Nodal Exchange "financially settled power contracts"; EOX Exchange application text) - never in the Kalshi row, whose entire content is "Kalshi | Designated | 11/03/2020 | On January 17, 2025, the Commission granted Kalshi's petition to modify its Order of Designation to permit intermediated futures trading." ka-doc-03 contains no occurrence of "Kalshi" at all (the corpus records this itself at L1902). So the retrieved CFTC record contains no statement about endpoint settlement, order-driven versus quote-driven structure, or continuous double auction, for Kalshi or for DCMs generally.
>
> 3) The corpus's own section 9 rows agree with the auditor: S7-1's licence column reads "No. It fixes the venue's regulatory category and its designation date, nothing else"; S7-3's reads "No. It establishes that the venue and its instrument class are the subject of active federal rulemaking..."; S7-5 marks settlement and adjudication rules, contract specifications, fees, position limits, membership and any DMM programme "Not established" (HTTP 429 x9), and asserts that "Every place in section 8 where a carrying assumption needed one of them is marked not-transferable-as-stated."
>
> 4) The count contradiction reproduces: grep for `not-transferable-as-stated` in section 8 returns exactly two claim-level marks (L971, L1112; L881 is the rule statement, L2004 is a section 11 handoff), matching G-3's "two" at L1969-1974 - while the three passages above rest on settlement-structure and trading-mechanism facts that S7 did not establish and are not so marked.
>
> The only near-defence available is a parsing one for L1280-1281 ("order-driven exchange in the CFTC record's own designation category" could be read as citing CFTC solely for the designation category), but that reading leaves "order-driven" with no cited source at all, which does not make the defect claim false. Nothing here constitutes concrete counter-evidence.

### QUANT-1-6 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reproducibility
> **location:** C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py:44-58; C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:596-620,626-639,45
> **issue:** The archived pipeline is not deterministic, so the published Table X-full row identifiers are not reproducible and the 'byte-for-byte' auditability claim fails. Record-level title and abstract selection tie-breaks on set iteration order, which depends on PYTHONHASHSEED; that changes the sort key and hence every uid.
> **evidence:** Two consecutive local runs of ka-dedup-script.py on identical input (recs.json, 15,924 records) gave identical aggregate counts (8,813 works / 7,111 duplicates, matching the record) but differed in uid->record mapping for 4,415 of 8,813 works; with PYTHONHASHSEED=0 fixed, two runs differ in 0 records, and the unseeded run differs from the seeded one in 4,535 titles and 3,867 abstracts. Frontmatter declares rng_seed: 0, which pins nothing here.
> **fix:** Make tie-breaks total (key=(len(t), t) for titles/abstracts/venues), pin PYTHONHASHSEED in the archived scripts, re-emit ka-screening-verdicts.jsonl, and/or key verdict rows by persistent identifier rather than by run-generated uid.
> **reference:** CLAUDE.md Reproducibility (deterministic ordering); corpus record section 5 'both re-runnable against the stored ka-*.json logs'

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; the finding reproduces. Rebuilt the universe with ka-universe-script.py (15,924 records, matching frontmatter n_identified), then ran ka-dedup-script.py three times unseeded and twice with PYTHONHASHSEED=0 (PYTHONHASHSEED was unset in the ambient env). All five runs printed identical aggregates (8,813 works / 7,111 duplicates) but the three unseeded outputs had three distinct MD5s (553b6f6d..., 016426ff..., 91f51345...) while the two seeded outputs were byte-identical (7e37a167...). uid->record diff unseeded run1 vs run2: 4,780 of 8,813 uids carry a different record (4,769 title, 4,555 dois, 4,108 abstract); run1 vs seeded: 5,004. (My count differs from the auditor's 4,415 only because each unseeded run draws a fresh hash seed.) Mechanism confirmed at line 49: titles = sorted({...}, key=len) sorts a SET with a non-total key, so titles[0] among distinct titles tied at minimum length falls out of PYTHONHASHSEED-dependent set iteration order; 942 of 8,813 groups have >=2 distinct titles tied at minimum length. That title feeds the uid sort key at line 65, renumbering downstream uids. Concrete: run1 U00016 = 'A macroeconomic forecasting market' vs run2 U00015 = same work; run1 U00018 = 'Complexity of Combinatorial Market Makers' (matching the published ka-dedup-ledger.json U00018) vs a different work in run2. U00001's title is 'A Practical Liquidity-Sensitive Automated Market Maker' unseeded but 'A practical liquidity-sensitive automated market maker' under PYTHONHASHSEED=0, and the ledger publishes the former, so the declared rng_seed: 0 does not even regenerate the published strings. ka-screening-verdicts.jsonl rows are keyed by the run-generated uid ({"id": "U00001", ...}) and its header asserts byte-for-byte reproducibility, and lit_review line 620 calls the scripts 're-runnable against the stored ka-*.json logs' — neither holds for row identity. Two secondary inaccuracies in the finding do not touch the claim: line 52 (absts) is a list comprehension over deterministic rs order, so abstract differences are a downstream consequence of uid remapping, not an abstract-level tie-break; and line 51 venues is sorted without a key and is already total, so the claimed fix's venue clause is unnecessary. The load-bearing defect claim is true.

### QUANT-1-7 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reproducibility
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:42-46; C:/Users/skoir/castles/logs/reproducibility/
> **issue:** The execution run that produced the corpus emitted no ReproLog and the tracked deliverable cites none. The project contract requires a 13-field ReproLog per artifact-producing run and requires a tracked deliverable to cite the ReproLog SHA-256 and the sidecar SHA-256 alongside the git HEAD.
> **evidence:** Frontmatter carries git_head_at_authoring only, with pip_freeze_sha256: 'n/a (no project-venv code execution...)' and dataset_checksums: 'n/a'. logs/reproducibility contains a registration-phase log for this protocol (config_resolved_sha256 = 99524df0..., phase 'register', git_head 8aeebfe) but none for the search execution; artifacts/runs/ is empty, so no sidecar exists for the run.
> **fix:** Emit the 13-field ReproLog and sidecar for the execution run (Python 3.11 stdlib env still has a pip freeze), and add repro_log_sha256 / sidecar_sha256 to the corpus record frontmatter as untracked locators plus digests.
> **reference:** CLAUDE.md 'Reproducibility contract' and 'Reproducibility (hook-enforced)'

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation found; the finding reproduces exactly. (1) logs/reproducibility/ contains 12 ReproLogs; the only one bearing the kalshi protocol digest is repro_log_28961af5a9ce4aa88ffbb817dcba2e60.json with config_resolved_sha256=99524df02696a59a..., phase="register", git_head=8aeebfe9adec (parent of registration commit 27d74738). No log exists with git_head at/after 27d74738 or with an execution/deliver phase for this search. A repo-wide `find -name repro_log_*.json` outside .git returns only those 12 files, so no execution log lives elsewhere. (2) artifacts/runs/ contains only .gitkeep — no sidecar exists. (3) `grep -c -iE "repro|sidecar"` over docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md returns 0: the deliverable cites no ReproLog path or digest and no sidecar digest anywhere in the file. (4) Lines 42-46 match the quoted evidence verbatim (git_head_at_authoring: 27d74738...; pip_freeze_sha256: "n/a (no project-venv code execution...)"; dataset_checksums: "n/a (no dataset...)"). Three counter-arguments were tested and failed: (a) scope escape via the emit-repro-log skill trigger ("artifact write to artifacts/ or logs/") does not hold, because CLAUDE.md §Reproducibility contract states the broader obligation "Every artifact-producing run in this project emits a 13-field ReproLog at logs/reproducibility/repro_log_{run_id}.json", and this run produced ~190 stored search responses plus a 149-record corpus and bibliography store; (b) the deliverable is indeed still untracked (git ls-files empty; listed as ?? in git status), which is a timing quibble that defeats only the citation half of the finding while the missing-ReproLog-for-the-run half stands independently; (c) the 2026-09-02 union-gate waivers (docs/audits/union_gate_waivers_2026-09-02.md, docs/deliverables/gate_waiver_0dd6aec6-5e0.md) are stop-hook waivers scoped to the Phase-2 explosive-regime spec and neither waive the ReproLog contract nor mention the kalshi execution run.

### QUANT-1-8 — retained

- raised_by: quant-auditor; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** reporting
> **location:** C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:628,2059-2063; C:/Users/skoir/castles/docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:120-126
> **issue:** The A3 residual risk is declared 'unquantified and unquantifiable' and is described as failing only on records whose title AND abstract contain no published token. In fact a majority of the DEFAULT-X1 stratum had no abstract at all, so those exclusions rest on title text alone - a quantifiable and materially larger exposure than the stated one.
> **evidence:** Recomputation over the rebuilt universe reproduces the published partition exactly (REVIEW 2,905 / DEFAULT-X1 5,249, matching ka-screening-vocabulary.json) and shows only 2,159 of the 5,249 DEFAULT-X1 records carry any abstract: 3,090 (58.9%) were rule-excluded on title alone. Corpus-wide, 4,779 of 8,813 works have an abstract.
> **fix:** Report the title-only rule-exclusion count (3,090) in section 13.1 and in the A3 entry, and restate the residual risk as partially quantified (bounded below by the title-only stratum) rather than unquantifiable.
> **reference:** Amendment A3; ka-screening-vocabulary.json fields_scanned

Refutation attempt (outcome: failed; evidence_type `none`):

> No refutation. Independent reproduction confirms the finding in full.
>
> (1) Rebuilt the universe from the archived tooling: ka-universe-script.py -> 15,924 raw records; ka-dedup-script.py -> 8,813 distinct works, 7,111 duplicates removed. Matches ka-dedup-ledger.json (n_raw_records 15924, n_distinct_works 8813).
>
> (2) Forward-citation-only stratum (arms == ["forward-citation"]) = 8,154, matching ka-screening-vocabulary.json n_stratum.
>
> (3) Applying the published token list over the declared fields_scanned blob (title || titles_all || abstract, case-insensitive substring, ANY-token match) reproduces the published partition exactly: REVIEW 2,905 / DEFAULT-X1 5,249 (published n_review 2905, n_default_x1 5249).
>
> (4) Abstract coverage inside DEFAULT-X1: 2,159 records carry an abstract; 3,090 do not (58.9%) — i.e. a majority of the stratum was rule-excluded on title text alone. Corpus-wide, 4,779 of 8,813 works have an abstract. All three figures match the auditor's evidence exactly.
>
> (5) The reporting defect verifies at the cited locations. lit_review_kalshi-arbitrage_2026-09-02.md:628 states the pre-sorter "can only fail on a record whose title *and* abstract contain none of the published tokens"; the same file at 2059-2063 (section 13.1) states the residual risk "is unquantified and unquantifiable without the second screener this design does not have". ka-protocol-amendments.md:120-126 carries the same conjunctive framing ("title and retrieved abstract contain none of the published tokens"). A grep of the whole lit review for unquantif|quantifiab|title alone|title-only|no abstract|3,090|2,159|4,779 returns no abstract-coverage statistic for the DEFAULT-X1 stratum; section 13.3 AG-7 quantifies missing abstracts only for the 33 *included* records, not for the excluded stratum. So the count is nowhere reported and the "unquantifiable" declaration stands unqualified.
>
> The one additional observation found does not weaken the finding: 727 REVIEW-stratum records also lack an abstract, so title-only matching also drove inclusion decisions, broadening rather than narrowing the exposure.

### LITERATURE-1-1 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** misattributed-citation-year
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:711-859 (corpus table) and :917-1882 (synthesis claim lines)
> **issue:** Systematic publication-year misattribution. The section-7 corpus table's displayed year disagrees with the DOI registrant's metadata AND with the record's own CSL-JSON store for ~20 records, and several of those wrong years are carried into section-8 citation strings. This is the load-bearing defect for an artifact whose stated rule is that 'every claim line carries a resolvable citation'.
> **evidence:** Fetched Crossref for each DOI: 10.1111/ecca.12009 = Franck, Verbeek & Nuesch, Economica 80(318):300-325, online 2012-12-17 / print 2013 -- table line 754 says 'Franck (2010)'. 10.5750/jpm.v1i2.423 = published year 2012 -- table line 715 says 'Abramovicz (2007)' and s8.4.2:1555 cites 'Abramovicz 2007'. 10.1016/j.qref.2016.07.016 = QREF vol 64, 2017 -- table line 753 says 'Flepp (2013)' and s8.5.2:1763 / s8.7:1882 cite 'Flepp, Nuesch & Franck 2013'. 10.1287/opre.2022.0417 = Operations Research vol 73, 2025 -- table line 758 says 'Gao (2022)' and s8.4.2:1454 cites 'Gao, Wang & Wu 2022'. Further table-vs-store-id disagreements: Angelini (2017) vs id angelini2019; Othman (2010) vs id othman2013 and s8.4.2 'Othman, Pennock, Reeves & Sandholm 2013'; Liu (2009) vs id liu2016 (JET 2016) and s8.4.3 'Liu & Wang 2009'; Ottaviani (2008) vs id ottaviani2010 (AEJ Micro 2010); Manski (2004) vs id manski2006 (Econ Letters 2006, Crossref-verified); Wolfers (2004) vs id wolfers2006 (NBER w12200, verified issue date May 2006); Birge (2018) vs id birge2021 (OR 2021) and s8.4.3:1639 'Birge, Feng, Keskin & Schultz 2018'; Hanke (2018) vs id hanke2019 (JOD 2019) and s8.1.2:1036 'Hanke, Poulsen & Weissensteiner 2018'; Dudik (2020) vs id dudk2021.
> **fix:** Regenerate the section-7 year column from the CSL-JSON store's `issued` field (the store is correct -- verified for 10.1111/ecca.12009 and 10.5750/jpm.v1i2.423), state in the table header which metadata field the year column carries, and re-derive every section-8 citation year from the store rather than from the table.
> **reference:** https://api.crossref.org/works/10.1111/ecca.12009 ; https://api.crossref.org/works/10.1287/opre.2022.0417 ; https://api.crossref.org/works/10.1016/j.qref.2016.07.016 ; https://www.nber.org/papers/w12200

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; the defect reproduces and is broader than claimed. (1) Programmatic diff of the section-7 corpus table's displayed year against the `issued.date-parts[0][0]` field of each record's own entry in docs/literature/references_kalshi-arbitrage.json: 149 table rows joined by id, 27 mismatches (finding said ~20). All ten table-vs-store disagreements named in the finding reproduce verbatim at the stated line numbers: L715 abramovicz2012jpmv1i2423 shows 2007 vs store 2012; L717 angelini2019 shows 2017 vs 2019; L728 birge2021 shows 2018 vs 2021; L750 dudk2021 shows 2020 vs 2021; L753 flepp2017 shows 2013 vs 2017; L754 franck2012 shows 2010 vs 2012; L758 gao2025 shows 2022 vs 2025; L772 hanke2019 shows 2018 vs 2019; L798 liu2016 shows 2009 vs 2016; L803 manski2006 shows 2004 vs 2006; L816 othman2013 shows 2010 vs 2013; L819 ottaviani2010 shows 2008 vs 2010; L853 wolfers2006 shows 2004 vs 2006. Seventeen further rows the finding did not enumerate also mismatch (e.g. L711 abernethy2011 2010 vs 2011, L746 diercks2026 'n.d.' vs 2026, L823 petersNone 2007 vs store null, L828/L829 restocchi2019, L832 sung2009, L838 sethi2015, L840 slamka2013). (2) Independent Crossref API fetches confirm the store, not the table: 10.1111/ecca.12009 = Franck/Verbeek/Nuesch, Economica 80(318):300-325, issued 2012-12-17, print 2013 (table says 2010); 10.1287/opre.2022.0417 = Gao/Wang/Wu/Yu, Operations Research 73(1):157-177, issued 2025-01 (table and s8.4.2 say 2022); 10.1016/j.qref.2016.07.016 = Flepp/Nuesch/Franck, QREF vol 64:306-317, issued 2017-05 (table and s8.5.2/s8.7 say 2013); 10.5750/jpm.v1i2.423 = Abramovicz, J. Prediction Markets 1(2):111-125, issued 2012-12-14 (table and s8.4.2 say 2007); 10.3386/w12200 = Wolfers & Zitzewitz, issued 2006-05 (table says 2004); 10.1016/j.econlet.2006.01.004 = Manski, Economics Letters 91(3):425-429, issued 2006-06 (table says 2004). (3) Carry-through into section 8 reproduces at every line cited: L1036 '[Hanke, Poulsen & Weissensteiner 2018]' -> doi 10.3905/jod.2019.26.4.128; L1454 '[Gao, Wang & Wu 2022]' -> 10.1287/opre.2022.0417; L1555 '[Abramovicz 2007]' -> 10.5750/jpm.v1i2.423; L1639 '[Birge, Feng, Keskin & Schultz 2018]' -> 10.1287/opre.2021.2109; L1763 and L1882 '[Flepp, Nuesch & Franck 2013]' -> 10.1016/j.qref.2016.07.016. (4) Counter-hypothesis tested and rejected: I grepped the whole review for any stated convention that the year column carries something other than publication year (e.g. first working-paper year). The table preamble at L699-709 documents only the venue-class, tier, strand and depth columns; no year-semantics note exists anywhere in the file, so the divergence is not an explained convention.

### LITERATURE-1-2 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **reproduced-check**; reproduction_required: **true**; outcome: **retained**

Claim verbatim:

> **category:** misattributed-venue
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:711-859
> **issue:** The corpus table's container-title is wrong for at least nine records, and disagrees with both the DOI registrant and the artifact's own CSL-JSON store. Venue is the field the evidence-tier assignment is derived from, so a wrong venue propagates into a wrong tier.
> **evidence:** 10.5750/jpm.v1i2.423 shown as 'SSRN Electronic Journal' (Crossref and the store both give 'The Journal of Prediction Markets'; store entry at references_kalshi-arbitrage.json:1967 reads "container-title": "The Journal of Prediction Markets"). 10.1016/j.qref.2016.07.016 shown as 'SSRN Electronic Journal' (Crossref: The Quarterly Review of Economics and Finance). 10.1287/opre.2022.0417 shown as 'ACM Conference on Economics and Computation' (Crossref: Operations Research). 10.1016/j.cnsns.2022.106994 shown as 'arXiv' (Crossref: Communications in Nonlinear Science and Numerical Simulation). 10.1080/14697688.2017.1395230 shown as 'arXiv' (Crossref: Quantitative Finance). 10.3386/w12200 shown as 'Federal Reserve Bank of San Francisco, Worki' (DOI prefix 10.3386 is NBER; verified NBER WP 12200). 10.1287/opre.1110.0922 shown as 'Operational Research' (correct title: Operations Research). 10.3905/jod.2019.26.4.128 shown as 'Jurnal derivate' (The Journal of Derivatives). 10.48550/arxiv.2302.00196 shown as 'Information Technology Convergence and Servi.'
> **fix:** Regenerate the venue column from the store's `container-title`; for arXiv-DOI records that have a journal version, record the journal and the arXiv id separately rather than labelling the journal record 'arXiv'.
> **reference:** https://api.crossref.org/works/10.1016/j.cnsns.2022.106994 ; https://api.crossref.org/works/10.1080/14697688.2017.1395230 ; https://api.crossref.org/works/10.5750/jpm.v1i2.423

Refutation attempt (outcome: failed; evidence_type `reproduced-check`):

> Refutation attempt failed; the finding is confirmed on all three legs (table text, CSL-JSON store, Crossref registrant).
>
> 1) Table text reproduces verbatim at C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md (grep of the nine DOIs):
> - L715 abramovicz2012jpmv1i2423 / 10.5750/jpm.v1i2.423 -> "SSRN Electronic Journal"
> - L716 agrawal2011opre11100922 / 10.1287/opre.1110.0922 -> "Operational Research"
> - L753 flepp2017jqref2016070 / 10.1016/j.qref.2016.07.016 -> "SSRN Electronic Journal"
> - L755 frongillo2023anaxiomati / 10.48550/arxiv.2302.00196 -> "Information Technology Convergence and Servi."
> - L756 gampe2023jcnsns202210 / 10.1016/j.cnsns.2022.106994 -> "arXiv"
> - L758 gao2025opre20220417 / 10.1287/opre.2022.0417 -> "ACM Conference on Economics and Computation"
> - L772 hanke2019jod201926412 / 10.3905/jod.2019.26.4.128 -> "Jurnal derivate"
> - L846 taleb2017146976882017 / 10.1080/14697688.2017.1395230 -> "arXiv"
> - L853 wolfers2006w12200 / 10.3386/w12200 -> "Federal Reserve Bank of San Francisco, Worki"
>
> 2) Store disagrees with the table for all nine. Parsed C:\Users\skoir\castles\docs\literature\references_kalshi-arbitrage.json (DOI | container-title | publisher):
> 10.5750/jpm.v1i2.423 | The Journal of Prediction Markets | University of Buckingham Press
> 10.1287/opre.1110.0922 | Operations Research | INFORMS
> 10.1287/opre.2022.0417 | Operations Research | INFORMS
> 10.1016/j.qref.2016.07.016 | The Quarterly Review of Economics and Finance | Elsevier BV
> 10.1016/j.cnsns.2022.106994 | Communications in Nonlinear Science and Numerical Simulation | Elsevier BV
> 10.1080/14697688.2017.1395230 | Quantitative Finance | Informa UK Limited
> 10.3905/jod.2019.26.4.128 | The Journal of Derivatives | Pageant Media US
> 10.3386/w12200 | (none) | National Bureau of Economic Research  [contradicts the table's "Federal Reserve Bank of San Francisco"]
> 10.48550/arxiv.2302.00196 | (none) | arXiv  [contradicts the table's "Information Technology Convergence and Servi."]
>
> The auditor's exact line citation checks out: references_kalshi-arbitrage.json:1967 reads "container-title": "The Journal of Prediction Markets", inside the record whose "id" (L1969) is abramovicz2012jpmv1i2423 — the same id as table row L715 that prints "SSRN Electronic Journal". DOI 10.5750/jpm.v1i2.423 appears at L1957/L1959 of that same record.
>
> 3) Live Crossref (curl https://api.crossref.org/works/<doi>) agrees with the store and against the table for every DOI I could query:
> 10.1016/j.cnsns.2022.106994 -> ["Communications in Nonlinear Science and Numerical Simulation"], Elsevier BV
> 10.1080/14697688.2017.1395230 -> ["Quantitative Finance"], Informa UK Limited
> 10.5750/jpm.v1i2.423 -> ["The Journal of Prediction Markets"], University of Buckingham Press
> 10.1287/opre.2022.0417 -> ["Operations Research"], INFORMS
> 10.3386/w12200 -> container-title empty, publisher "National Bureau of Economic Research", type "report" (confirms the 10.3386 prefix is NBER, not FRBSF)
>
> No counter-evidence of any kind was obtainable: the table venues are not an alternate-but-valid rendering (e.g. a preprint-server label for a record whose DOI resolves to a journal), because several are simply different journals ("Operational Research" vs Operations Research; "Jurnal derivate" vs The Journal of Derivatives) or unrelated venues ("Information Technology Convergence and Servi." for an arXiv record; FRBSF for an NBER working paper). The defect claim stands as written.

`reproduction` block, lifted from the refutation evidence:

```yaml
reproduction:
  command: "grep -n over the nine DOIs in docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md; parse of docs/literature/references_kalshi-arbitrage.json for (DOI, container-title, publisher); then curl https://api.crossref.org/works/<doi> for 10.1016/j.cnsns.2022.106994, 10.1080/14697688.2017.1395230, 10.5750/jpm.v1i2.423, 10.1287/opre.2022.0417, 10.3386/w12200"
  observed: "Table, store and registrant disagree exactly as the finding states. Table rows L715/L716/L753/L755/L756/L758/L772/L846/L853 print \"SSRN Electronic Journal\", \"Operational Research\", \"SSRN Electronic Journal\", \"Information Technology Convergence and Servi.\", \"arXiv\", \"ACM Conference on Economics and Computation\", \"Jurnal derivate\", \"arXiv\" and \"Federal Reserve Bank of San Francisco, Worki\". The store gives, for the same DOIs, The Journal of Prediction Markets; Operations Research; The Quarterly Review of Economics and Finance; (none)/arXiv; Communications in Nonlinear Science and Numerical Simulation; Operations Research; The Journal of Derivatives; Quantitative Finance; (none)/National Bureau of Economic Research. Live Crossref agrees with the store against the table on every DOI queried, including publisher \"National Bureau of Economic Research\", type \"report\" for the 10.3386 prefix. references_kalshi-arbitrage.json:1967 reads \"container-title\": \"The Journal of Prediction Markets\" inside the record whose id is abramovicz2012jpmv1i2423 — the same id as the table row printing \"SSRN Electronic Journal\". No alternate-but-valid rendering explains the divergence."
```

### LITERATURE-1-3 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** evidence-hierarchy
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:715 vs :1555; :740 vs :1148; :756 vs :1856; :846 vs :1027
> **issue:** The evidence tier recorded in the corpus table contradicts the tier written on the claim line for four records. The protocol's whole tier discipline is 'tier-blind admission with tier-labelled use, and the tier travels with the claim' (protocol s2.5); a record carrying two different tiers in one artifact defeats it. Two of the four are peer-reviewed journal articles mis-tiered T5 in the table, which understates the corpus's peer-reviewed base.
> **evidence:** Taleb 10.1080/14697688.2017.1395230: table line 846 'T5'; s8.1.2 line 1027 '(Taleb 2017 ... T1, abstract depth)'. Crossref confirms Quantitative Finance 18(1), journal article -> T1 correct, table wrong. Gampe & Griffin 10.1016/j.cnsns.2022.106994: table line 756 'T5'; s8.6.2 line 1856 'T1'. Crossref confirms Comm. Nonlinear Sci. Numer. Simul. vol 118, journal article -> T1 correct, table wrong. Abramovicz 10.5750/jpm.v1i2.423: table line 715 'T1'; s8.4.2 line 1555 'T5'. Constantinou & Fenton 10.5750/jgbe.v7i2.630: table line 740 'T1'; s8.2.2 line 1148 'T5 journal-tier record without a peer-review claim in the retrieved metadata'.
> **fix:** Reconcile each to a single tier with the deciding evidence named, and add a mechanical check that no DOI carries two tier values in the artifact.
> **reference:** ~/.claude/CLAUDE.md Evidence Hierarchy; protocol_kalshi-arbitrage-review_2026-09-02.md s2.5

Refutation attempt (outcome: failed; evidence_type `none`):

> Could not refute; the finding reproduces exactly and is corroborated by the artifact's own bibliography. (1) Line-level reproduction in docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md: 10.5750/jpm.v1i2.423 table line 715 = T1 vs claim line 1555 = T5; 10.5750/jgbe.v7i2.630 table line 740 = T1 vs claim line 1148 = "T5 journal-tier record without a peer-review claim in the retrieved metadata"; 10.1016/j.cnsns.2022.106994 table line 756 = T5 vs claim line 1855 = T1; 10.1080/14697688.2017.1395230 table line 846 = T5 vs claim line 1027 = T1. A grep for each DOI returns exactly two hits per DOI (table + claim line), so no third occurrence reconciles them and no errata note exists. (2) No dual-axis defense is available: protocol_kalshi-arbitrage-review_2026-09-02.md s2.5 lines 283-286 defines a single tier vocabulary (T1 peer-reviewed ... T5 other) and states "Every included record carries its tier"; lit_review line 697 states the table's `tier` column is that same CLAUDE.md evidence tier. Same axis, two values. (3) Independent confirmation of which half is wrong, from docs/literature/references_kalshi-arbitrage.json rather than the auditor's Crossref call: taleb2017146976882017 is type "article-journal", container-title "Quantitative Finance", vol 18 iss 1 pp 1-5; gampe2023jcnsns202210 is type "article-journal", container-title "Communications in Nonlinear Science and Numerical Simulation", vol 118 p 106994. Both are peer-reviewed journal articles, so the table's T5 for these two is the erroneous value, matching the auditor's claim that the corpus table understates the peer-reviewed base.

### LITERATURE-1-4 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** unsupported-attribution
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1255-1256, :1280-1282, :1541-1542
> **issue:** Three synthesis statements assert Kalshi venue-structural facts and cite 'the CFTC record (section 9)' as their source, but section 9's own S7 table states those facts are not established. This is the AG-1 failure mode the record claims to have contained, and it is the exact hazard protocol s8 exists to prevent.
> **evidence:** s8.3.2:1255 'it holds at any venue whose contract settles at an endpoint -- which the CFTC record establishes for Kalshi as a class of instrument (section 9)'. s8.3.2:1280 'Kalshi is an order-driven exchange in the CFTC record's own designation category (section 9), so the supply-side channel as stated does not transfer' -- and this is called 'the single largest structural reason the sportsbook FLB literature must not be restated as a Kalshi finding'. s8.4.2:1541 'a continuous double auction, which is the microstructure the CFTC record associates with a designated contract market'. Against these, S7-1 (line 1933) states the CFTC filings page 'fixes the venue's regulatory category and its designation date, nothing else', and S7-5 (line 1937) records contract specifications, settlement and adjudication rules as 'Not established'. Consequently G-3 (line 1973) is wrong that there are only 'two such marks in section 8'.
> **fix:** Mark all three claims `not-transferable-as-stated`, delete the 'the CFTC record establishes' attributions, and correct the G-3 count. If endpoint settlement is to be asserted for Kalshi as a class, source it to a retrieved document, not to a DCM designation table.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s2.7 constraint 1 and s8 corollary 2

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; the finding reproduces. (1) All three quoted passages are verbatim at the stated lines of docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md (:1254-1256, :1280-1284, :1541-1542), and grep for "CFTC record" returns exactly those three lines, so there is no better-sourced variant or adjacent sourcing text. (2) Checking the cited source, section 9: S7-1 (:1933) licenses only "the venue's regulatory category and its designation date, nothing else"; S7-2 (:1934) only intermediation permission "and on nothing else"; S7-3/S7-4 are title-level Federal Register hit lists (verbatim query at :1911 requests only title/document_number/publication_date/agencies/html_url/type -- no document text); S7-5 (:1937) marks contract specifications, settlement and adjudication rules "Not established"; S7-6 (:1938) marks 17 CFR 40.11 unretrieved, so no regulatory definition of an event contract was read; ka-doc-03 (:1902), the DCM index page, "contains no occurrence of the string 'Kalshi'". Nothing retrieved states endpoint settlement, an order-driven mechanism, or any microstructure associated with DCM designation. (3) The protocol reference is real and confirms the hazard: protocol s2.7 constraint 1 at :335-338, and s8 corollary 2 at protocol :938-944 requires that when an S7 fact is used to state a carrying assumption is satisfied, "the corpus says which document, which version, and which retrieval date carried it" -- the three passages name none, and the facts they invoke are absent from the S7 table. (4) Only partial narrowing found, which does not rescue the artifact: counting `not-transferable-as-stated` within section 8 (lines 861-1883) gives exactly two marks (:971 in 8.1.2, :1112 in 8.2.2; :881 is the rule statement, :2004 and :2096 lie outside section 8), so G-3's count of "two" is accurate for the file as it currently stands and is only "wrong" conditional on applying the finding's own fix. That is a scope quibble on a derived sub-claim, not counter-evidence against the core defect, which stands.

### LITERATURE-1-5 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** method-misattribution
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1571-1576 (and :1352, :1359)
> **issue:** Glosten-Harris (1988) is conflated with Glosten & Milgrom (1985). The corpus uses Bartlett & O'Hara's adaptation of the Glosten-Harris spread decomposition as evidence that Glosten & Milgrom's apparatus 'has been transferred to a binary event venue by others'. These are two different models by different author pairs -- Glosten & Harris, 'Estimating the components of the bid/ask spread', JFE 1988, an empirical spread-decomposition regression, versus Glosten & Milgrom 1985, a sequential-trade adverse-selection model. Glosten & Harris 1988 is not in the 149-record corpus at all.
> **evidence:** s8.4.3:1573-1576: 'The corpus nevertheless records that its apparatus *has* been transferred to a binary event venue by others -- the Kalshi adverse-selection record adapts the Glosten-Harris decomposition (8.4.1) -- so the transfer exists in the literature'. The referenced 8.4.1 text (line 1349) correctly reports Bartlett & O'Hara using 'adaptations of Kyle's lambda and the Glosten-Harris decomposition' (confirmed against the SSRN abstract for 10.2139/ssrn.6615739, which names Kyle's lambda and the Glosten-Harris framework). The Kyle entry at line 1580 makes the parallel move correctly, because Kyle's lambda does come from Kyle 1985; the Glosten-Milgrom entry does not.
> **fix:** Either drop the transfer sentence from the Glosten & Milgrom entry, or add Glosten & Harris 1988 to the corpus as the record whose apparatus was transferred and attribute it there. Do not use surname overlap as an attribution bridge.
> **reference:** https://api.crossref.org/works/10.2139/ssrn.6615739 ; Glosten & Harris 1988, https://doi.org/10.1016/0304-405X(88)90034-7

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; every leg of the finding reproduced.
>
> (1) Text at C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1569-1576 is verbatim as quoted. The entry is headed "**Glosten & Milgrom 1985**" with doi:10.1016/0304-405X(85)90044-3, and its transfer sentence reads "The corpus nevertheless records that its apparatus *has* been transferred to a binary event venue by others -- the Kalshi adverse-selection record adapts the Glosten-Harris decomposition (8.4.1)". The antecedent of "its" is Glosten & Milgrom 1985; the evidence offered is the Glosten-Harris decomposition. No lineage argument (e.g. that Glosten & Harris 1988 operationalizes the Glosten-Milgrom adverse-selection component) is made anywhere in the entry or elsewhere in the document, so no "derivation bridge" defense is available on the text as written.
>
> (2) Line 1349 and 1359 correctly report Bartlett & O'Hara as adapting "Kyle's lambda and the Glosten-Harris decomposition". This matches the stored abstract for 10.2139/ssrn.6615739 in docs/literature/references_kalshi-arbitrage.json:1491: "Adapting Kyle's lambda and the Glosten-Harris decomposition..." So 8.4.1 is accurate and it is 8.4.3 that misattributes.
>
> (3) Counter-test on the corpus: parsed docs/literature/references_kalshi-arbitrage.json (149 records confirmed). Zero records have any author with family name "Harris". The only Glosten-authored record is glosten19850304405x8590, authors ['Glosten','Milgrom'], DOI 10.1016/0304-405x(85)90044-3. Grep for the Glosten & Harris 1988 DOI fragments ("88)90034", "9034050288") returns 0 hits. The only occurrence of the string "Glosten-Harris" in the bibliography is inside the Bartlett & O'Hara abstract text, not as a record. So Glosten & Harris 1988 (JFE 21(1):123-142, doi:10.1016/0304-405X(88)90034-7) is genuinely absent from the corpus, as claimed.
>
> (4) The finding's contrast case holds: the Kyle 1985 entry at :1578-1581 says "Kyle's lambda is adapted to Kalshi in 8.4.1", and Kyle's lambda does originate in Kyle 1985 (doi:10.2307/1913210), which IS the corpus record cited there. The parallel construction is valid for Kyle and invalid for Glosten & Milgrom.
>
> (5) Checked whether the document discloses the distinction elsewhere: grep for "Glosten" across all four artifacts returns lines 690, 721, 743, 764, 788, 1349, 1359, 1569, 1575, 1612, 1614, 2112 in the review plus protocol lines 582/600/631/655/1188 — all refer to Glosten & Milgrom 1985 or to the Bartlett & O'Hara abstract. Nothing anywhere identifies Glosten & Harris 1988 as a separate work. No mitigating disclosure exists.

### LITERATURE-1-6 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** unsupported-interpretation
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:2105-2131
> **issue:** The known-item recall reading is over-broad in one direction and refuted by the frozen strategy in the other. (i) Three misses are excused as 'structural, not a recall failure' because each is its own forward-citation anchor -- but that exculpation covers only the one arm each anchors; all three could have been retrieved by the 35 topical queries and by the other five anchors' citing sets, and were not. (ii) The conclusion that 'retrieval depth, not vocabulary, is this strategy's binding constraint' is contradicted for KI-20 by the strategy text itself.
> **evidence:** Line 2112-2115 classes KI-01 Oliven & Rietz, KI-18 Glosten & Milgrom and KI-23 Levitt as structural because 'a citing set contains the works that cite the anchor, never the anchor itself'. True only of the arm they define. Line 2124-2128 asserts the four genuine misses indicate caps rather than vocabulary. But KI-20 Ho & Stoll, 'Optimal dealer pricing under transactions and return uncertainty', uses 'dealer pricing', and the string 'dealer' appears in none of the 35 frozen topical queries (protocol s3.2, lines 439-558); likewise 'specialist' (KI-18's title term) appears in none. That is a demonstrable vocabulary gap, not a depth gap. The rank/position evidence needed to test the depth hypothesis is in the retained ka-*.json logs and is never reported.
> **fix:** Restate the three anchor misses as 'not retrieved by any arm other than their own citing-set definition', so effective recall reads 16/23 rather than an implied 16/20. Withdraw the depth-not-vocabulary conclusion or support it by reporting, from the stored logs, whether the four missed items appear anywhere in the platform-reported result sets below the cap.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s3.4 'Per-item failures are reported and interpreted, not scored'

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; the finding is corroborated on both prongs.
>
> PRONG (i) reproduced. C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md line 2112 heads the bullet "Structural, not a recall failure (3)" and justifies it at 2113-2115 only by "a citing set contains the works that cite the anchor, never the anchor itself, so these three could not have been recovered by the arm they define" — an exculpation valid solely for the anchor's own arm. The underlying per-item log C:\Users\skoir\castles\docs\literature\search_logs\kalshi-arbitrage\ka-known-item-recall.json shows KI-01 (10.1287/mnsc.1040.0191), KI-18 (10.1016/0304-405x(85)90044-3) and KI-23 (10.1111/j.1468-0297.2004.00207.x) each with "independent_query_ids": [] — i.e. not retrieved by any of the 35 topical queries nor by any of the other five anchors' citing sets either, so the non-retrieval is not explained by the structural argument given. The log's own "structural_note" repeats the same over-broad wording ("structural, not a vocabulary failure"). Combined with lines 2108 and 2116-2117 ("16 of 23" plus exactly 4 "genuine" failures), the implied effective denominator of 20 is a fair reading. Nothing in the artifact narrows the exculpation to the one arm.
>
> PRONG (ii) reproduced, and my independent counter-test went against the artifact, not against the auditor. grep over C:\Users\skoir\castles\docs\methodology\protocol_kalshi-arbitrage-review_2026-09-02.md returns "dealer" only at line 657 (the KI-20 known-item table row) and "specialist" only at line 655 (KI-18's row); neither string occurs in any of the 35 frozen topical query strings in s3.2 (lines 439-558). I then re-executed the frozen ka-crossref-07 query verbatim (query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book) at rows=1000 against api.crossref.org. Platform total 79,890; 1000 returned. KI-21 Avellaneda & Stoikov 10.1080/14697680701381228 appears at rank 982 — far below the frozen rows=20 cap. KI-20 Ho & Stoll 10.1016/0304-405X(81)90020-9 does NOT appear anywhere in the top 1000. That is direct evidence that KI-20's miss on this query is not a cap/depth artifact: raising the cap fifty-fold still does not surface it, which is what a lexical/vocabulary gap looks like and not what a depth gap looks like. The artifact's line 2127 conclusion ("retrieval depth, not vocabulary, is this strategy's binding constraint") is therefore unsupported for KI-20 by the strongest available test.
>
> Auditor's ancillary claim also reproduced: grep for rank/position reporting across the review returns no rank or below-cap position evidence for any of the four missed items (hits at lines 903, 961, 967, 1104, 1128-1132, 1178, 1769-1770, 1888, 1937, 1966, 2003-2005 are all "position" in the trading/portfolio sense, none are retrieval ranks).

### LITERATURE-1-7 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** protocol-fidelity
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:199-205, :2092-2103
> **issue:** Silent protocol deviation. The frozen protocol s3.1 'SSRN caveat, declared in advance' requires that if the SSRN site-search supplementary arm is not run, 'the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence.' The corpus record records no such gap anywhere, and no amendment covers it. Protocol s10 classes silent deviation as a conduct violation.
> **evidence:** Protocol lines 380-385 state the requirement. Grepping the corpus record for 'SSRN site', "SSRN's site", 'SSRN search', 'no public search API' and 'browser access' returns no matches. The gap table s13.3 runs AG-1..AG-8 and contains no SSRN entry; s10 gaps G-1..G-7 contain none; the five amendments A1-A5 contain none. This is material: SSRN carries the majority of the Kalshi-specific corpus (13 of the 19 K records are 10.2139/ssrn.* DOIs) and SSRN was reached only through two Crossref container-restricted queries at rows=20 (ka-crossref-13, ka-crossref-14).
> **fix:** Add the SSRN supplementary-arm absence to s13.3 as a numbered recall verification gap with its consequence for the Kalshi-specific stratum, or record it as amendment A6 with the stage at which it was decided.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s3.1 SSRN caveat; s10 amendments policy

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; the finding reproduces exactly and is if anything understated. (1) Protocol requirement confirmed verbatim at docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:380-385 ("if not, the absence is recorded as a minor recall verification gap in the corpus record, not passed over in silence"), and section 10 line 1080 confirms "Silent deviation is a conduct violation." (2) Case-insensitive grep for 'ssrn' across the corpus record returns ONLY the two Crossref query.container-title=SSRN URLs (lines 305, 308) and DOIs/venue strings inside record rows; no gap statement. Repo-wide grep for 'site search|site-search|supplementary arm|no public search API|browser access|recall verification gap' returns SSRN hits only in the sibling explosive-regime review, never in the kalshi corpus record. (3) Section 13.3 gap table enumerates AG-1..AG-8 (Kalshi rulebook 429, eCFR interstitial, Semantic Scholar topical 429, S2 anchor A3 404, full texts, RePEc GET empty, Gomez-Gonzalez full text 404, 33 missing abstracts) with no SSRN entry. (4) Section 10 gaps G-1..G-7 contain no SSRN entry. (5) Amendments A1-A5, both in section 13.1 and in the append-only source docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md, are eCFR-interstitial reclassification, RePEc POST supplementary arm, vocabulary pre-sorter, X10, X11 — no A6 and the only "supplementary arm" in that file is RePEc's. (6) Section 13.5 depth truncation names the Crossref rows=20 truncations generically but makes no SSRN recall statement; section 2 prisma-s-4's "no search-engine or hand-browse arm was run" is a bare negative that neither names SSRN nor labels a recall verification gap. (7) Materiality verified independently and is larger than the finding states: parsing the section 7 included-corpus table, the stratum column equals K for 19 records, of which 15 (not 13) carry 10.2139/ssrn.* DOIs; SSRN was reached only through ka-crossref-13 (20 of 1,093) and ka-crossref-14 (20 of 10,991). (8) Counter-check on precedent cuts against refutation: the identical protocol clause in docs/literature/lit_review_explosive-regime-dating_2026-08-24.md was discharged explicitly at lines 189-191 and as gap VG-5 at line 2124, so the omission here departs from both the frozen protocol and the project's own established practice.

### LITERATURE-1-8 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** provenance-integrity
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:137
> **issue:** The section-2 PRISMA-S 1/2/13 provenance table -- the artifact's canonical per-query record -- misreports a stored HTTP status, on the row that documents access gap AG-4.
> **evidence:** Table row: '| Semantic Scholar | ... | ka-fc-s2-a3 | 0 | not reported | 200 | cursor/offset paged, 1 pages |'. The stored log docs/literature/search_logs/kalshi-arbitrage/ka-fc-s2-a3-p001.json records "http_status": 404, "retry_attempts": 6, "raw": {"error": "Paper with id DOI:10.1086/655844 not found"}. The record's own narrative agrees with the log and disagrees with its own table: prisma-s-5 (line 216) says 'HTTP 404 for A3' and AG-4 (line 2099) says 'HTTP 404'. Section 3 asserts 'each string was written to its log file in the same write as the HTTP status'. I checked every stored log's http_status: this is the only row that disagrees with the table.
> **fix:** Correct the ka-fc-s2-a3 row to 404 and add the AG-4 note to the row's note column.
> **reference:** docs/literature/search_logs/kalshi-arbitrage/ka-fc-s2-a3-p001.json

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempt failed; the finding reproduces exactly. (1) Line 137 of docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md reads: "| Semantic Scholar | Semantic Scholar Graph API (api.semanticscholar.org) | 2026-09-02 | ka-fc-s2-a3 | 0 | not reported | 200 | cursor/offset paged, 1 pages |", and the table header at line 100 names that column "http". (2) docs/literature/search_logs/kalshi-arbitrage/ka-fc-s2-a3-p001.json records "http_status": 404, "retrieved_count": 0, "retry_attempts": 6, "raw": {"error": "Paper with id DOI:10.1086/655844 not found"}. (3) `ls` of the search_logs dir shows ka-fc-s2-a3-p001.json is the ONLY log for that query id, so there is no later successful page whose 200 the row could legitimately be reporting. (4) The record contradicts itself internally: line 216 says "HTTP 404 for A3" and AG-4 in section 13.3 (line ~2099) says "HTTP 404 - the service does not index that identifier". (5) Counter-test against the only available defense (that "200" might be a placeholder/convention rather than a literal status): the same http column carries 12 rows with value 429 (ka-s2-01/02/03/04 plus their -b and -c retries), proving non-200 statuses are transcribed literally in this table. Distinct column values across the table are 200 (74 rows) and 429 (12 rows) only. The 200 on the ka-fc-s2-a3 row is therefore a genuine misreport of a stored HTTP status on the row documenting access gap AG-4.

### LITERATURE-1-9 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** missing-from-synthesis
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:746, :844, :859
> **issue:** Three included records whose 'role in the argument' column affirmatively states they enter a named section-8 block appear nowhere in section 8. Two of them are Kalshi-specific, and one of those is a peer-reviewed T1 record -- so the omission both falsifies the role column and biases the Kalshi block toward T5 and toward the concentrated first author.
> **evidence:** Line 844 subramanian2026ijfmd2026100, 'Prediction market efficiency: evidence from Kalshi on pricing accuracy, forecasting, and risk', T1, K, S6, role 'enters the Kalshi-specific block of its strand' -- absent from s8.6.1 and from the whole document outside the table (grep confirms one occurrence). Line 746 diercks2026w34702, 'Kalshi and the Rise of Macro Markets', NBER WP, K, S6 -- absent (grep: one occurrence); Crossref confirms this record exists as Diercks, Katz & Wright, January 2026, so '(n.d.)' in the table is also wrong. Line 859 trumbelj2014jijforecast2 (Strumbelj, IJF 2014, G, S1) -- absent. The omission is internally inconsistent with s8.2.1's own reasoning for naming Lim at metadata depth: 'It is listed because omitting a directly on-point Kalshi record would misrepresent the corpus.'
> **fix:** Name all three in their declared blocks at their stated extraction depth, or change the role column to say the record was included but not carried into the synthesis and give the reason.
> **reference:** https://api.crossref.org/works/10.3386/w34702

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; every element of the finding reproduced independently.
>
> 1. Location check. Lines 746, 844, 859 of C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md are exactly the three table rows described, with the role text quoted verbatim by the auditor ("Kalshi-data evidence; enters the Kalshi-specific block of its strand" for diercks2026w34702 and subramanian2026ijfmd2026100; "evidence from another venue; enters the generalized block..." for trumbelj2014jijforecast2).
>
> 2. Absence check, run wider than the auditor's. Grepped the whole file for the citekeys AND for surname/title variants that a differently-rendered citation would carry: "Diercks", "Subramanian", "Strumbelj", "Štrumbelj", plus the three DOIs (10.3386/w34702, 10.1504/ijfmd, 10.1016/j.ijforecast.2014.02.008). Each returns exactly one hit — its own table row (746 / 844 / 859). Section 8 spans line 861 to 1022 (headers 8.1–8.7, with 8.6.1 "Kalshi-specific" at 1777 absolute). Read 8.6.1 in full: it names Bartlett & O'Hara 2026, Lee Lee & Lee 2026b, Greene 2026, Krause 2026e — no Subramanian, no Diercks. So no alternate-rendering escape hatch exists; the records are absent from the synthesis, not merely absent under one key spelling.
>
> 3. Internal-inconsistency check, and it is worse than reported. Beyond the s8.2.1 Lim passage the auditor quotes (line 1071), s13.2 item 1 states as a global property of the record: "records at metadata depth are named without their findings being stated," over the 116 abstract-depth + 33 metadata-depth = 149 included records. Subramanian and Štrumbelj are depth "meta" and Diercks is depth "abs"; all three are among the 149. The omission therefore contradicts a second self-description of the document, not only the per-row role column.
>
> 4. Corpus-membership check. Parsed docs/literature/references_kalshi-arbitrage.json (149 entries): all three ids are present, so they are genuinely included records, not screened-out rows left in a table.
>
> 5. Source check on the auditor's Crossref reference. Live query to https://api.crossref.org/works/10.3386/w34702 returns title "Kalshi and the Rise of Macro Markets", authors Diercks (Anthony), Katz (Jared Dean), Wright (Jonathan), issued 2026-01, created 2026-01-20 — confirming the auditor's citation. The project's own CSL store already carries issued {"date-parts": [[2026, 1]]} for this id, so the table's "Diercks (n.d.)" also contradicts the repository's own bibliography, independent of Crossref.
>
> No counter-test contradicted any part of the claim. The only reduction I can offer is a severity-quibble (the T1 Kalshi record is the load-bearing part; the T1/G Štrumbelj omission is comparatively minor), and severity quibbles are not refutation.

### LITERATURE-1-10 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** misstated-limitation
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991 (G-6) and :1238-1240
> **issue:** The disclosed non-independence of the Kalshi evidence base understates itself. G-6 states 'fifteen of the nineteen are T5 preprints or working papers'; the corpus table shows seventeen of nineteen. Understating a limitation in the sentence whose job is to state it is a disclosure defect, not a rounding error.
> **evidence:** Enumerating the E4/E15 = K rows of the section-7 table: bartlett T5, brgi T5, diercks T5, goel T1, greene T5, gupta T5, krause x5 all T5, lee x2 T5, lim T5, mohanty T5, moulinier T5, polson T5, subramanian T1, yurchyna T5 = 19 records, 17 T5, 2 T1. Compounding it, one of the two T1 records (Subramanian) never reaches the synthesis (see LITERATURE-1-9), so the synthesized Kalshi block is effectively 18 of 18 T5. The five-Krause first-author concentration count (line 1238-1240, line 1988) does check out.
> **fix:** Correct G-6 to seventeen of nineteen, and state that after the synthesis omissions only one peer-reviewed Kalshi record actually carries a claim line.
> **reference:** (none given)

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; finding independently confirmed. (1) G-6 at lit_review_kalshi-arbitrage_2026-09-02.md:1988-1991 reads verbatim "fifteen of the nineteen are T5 preprints or working papers". (2) Field-parsing the section-7 table (lines 692-861) on the E4/E15 column yields exactly 19 rows valued K (no variant tokens; 69 G, 61 N), of which 17 are tier T5 and 2 are T1 (goel2026jiref2026105, subramanian2026ijfmd2026100). This reproduces the auditor's enumeration exactly. (3) Counter-test on the strongest available refutation path -- that "T5 preprints or working papers" is a narrower predicate than tier T5, which could make 15 correct if two T5 records were non-preprint grey literature -- fails: all 17 T5 K-records are SSRN Electronic Journal preprints (13), working papers (Buergi/CESifo, Diercks/NBER w34702), or arXiv (Mohanty, arxiv.2604.01431). Every one satisfies the predicate, so no reading yields fifteen. (4) The Krause five-first-author count checks out (5 krause* K rows), as the finding concedes. (5) The compounding claim also holds: grep for Subramanian returns a single hit, the section-7 table row at line 844 (depth `meta`), with no occurrence anywhere in the section-8 synthesis. Defect is real: a two-record understatement inside the sentence whose function is to disclose the corpus non-independence limitation.

### LITERATURE-1-11 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** grouping-rule-violation
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:74-82 vs :889-914, :1063-1098, :1191-1245
> **issue:** The PRISMA 2020 item-13a grouping rule is declared as 'records are grouped by the protocol's frozen strand list' (i.e. mechanically from extraction field E3), but the strand recorded for a record in the corpus table repeatedly differs from the strand under which its claim is synthesized. The grouping is therefore reconstructed, not mechanical, and the apparent depth of the thin Kalshi strands is inflated by it.
> **evidence:** s8.1.1 (strand S1) has three bullets; two are from records the table does not assign to S1 -- Burgi (table line 731: S3+S5) and Polson (table line 824: S6). Only Moulinier is an S1 record. s8.2.1 (S2) draws on Mohanty (table line 806: S6) and Goel (table line 765: S6). s8.3.1 (S3) draws on Yurchyna (table line 856: S5), Krause 7117919 and Krause 7119120 (table lines 783-784: S6) and Lee 6964226 (table line 793: S6).
> **fix:** Either correct the E3 strand values in the corpus table so they match where each record is synthesized, or move the claim lines to the strand the table assigns. State which of the two is the authoritative record of E3.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s5 field E3; s7 item 4

Refutation attempt (outcome: failed; evidence_type `none`):

> Could not refute; the claim reproduces exactly. Corpus-table E3 cells: L731 Burgi ssrn.5502658 = S3+S5; L824 Polson ssrn.7254820 = S6; L806 Mohanty arxiv.2604.01431 = S6; L765 Goel iref.2026.105577 = S6; L856 Yurchyna ssrn.7364100 = S5; L783/784 Krause ssrn.7117919 / ssrn.7119120 = S6; L793 Lee ssrn.6964226 = S6. Synthesis: s8.1.1 (S1) has exactly three bullets (Burgi L893, Polson L902, Moulinier L913) and only Moulinier's E3 (S1+S2+S5) contains S1; s8.2.1 (S2) carries Mohanty L1092 and Goel L1098; s8.3.1 (S3) carries Yurchyna L1226, Krause 7117919 L1233, Krause 7119120 L1237, Lee 6964226 L1244. Two counter-tests failed to break it: (1) references_kalshi-arbitrage.json is plain CSL-JSON with no strand field (key union: DOI, ISBN, ISSN, URL, abstract, author, categories, container-title, container-title-short, event, id, issue, issued, language, number, page, publisher, source, title, type, version, volume), so no alternative authoritative E3 store exists and the corpus table is the sole E3 record; (2) grep of each record outside the table shows Polson, Mohanty, Goel, Krause 7117919 and Krause 7119120 are cited ONLY in the mismatched strand and never in their recorded S6, so the placement is not a secondary appearance alongside a compliant primary one. Protocol s7 item 3 fixes the table column as 'the strand(s) it serves' and s5 E3 as 'Strand(s) S1-S6 the record contributes to'; each K row's own role cell reads 'enters the Kalshi-specific block of its strand', which the placement contradicts. No amendment (s13.1 A1-A5) covers strand-placement discretion, and s13.6 omits item 13a from the unmet-item list, i.e. the record asserts 13a compliance. Only inaccuracy found is a wording nuance: the declaration at :74-82 does not literally say 'mechanically' (protocol s8.1 reserves that word for the E4-based venue classification); this is a phrasing quibble that does not affect the E3-vs-placement inconsistency.

### LITERATURE-1-12 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** separation-rule-violation
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1080-1087, :1203-1209, :2170-2172
> **issue:** Non-Kalshi evidence is stated inside Kalshi-specific blocks without a carrying assumption, and s13.7 then asserts as an absolute that this never happens. The separation rule is the branch's headline control (protocol s8) and the claim of its perfect observance is false as written.
> **evidence:** s8.3.1:1203-1209 states, inside the Kalshi-specific block: 'A cross-platform study of 72.1 million Kalshi trades ... with 404.5 million Polymarket trades reports a statistically significant bias on both, with Kalshi longshots overpriced ... and a stated cross-platform contrast in sign' -- the 'on both' and 'cross-platform contrast' clauses are Polymarket findings placed in a K block with no assumption line. s8.2.1:1080-1087 states, in the K block, that IV surfaces, risk-neutral densities and variance risk premia are extracted from '113,338 Bitcoin and Ethereum contracts' -- a sample spanning Kalshi and Polymarket per the record's own title. Against these, s13.7:2170-2172 claims 'Every claim generalized from Betfair, the Iowa Electronic Markets, PredictIt, Polymarket, sportsbook or racetrack data appears in a generalized block with its carrying assumption on the same line, never in a Kalshi-specific block.'
> **fix:** Split mixed-venue records: state the Kalshi-measured part in the K block and the other-venue part in the generalized block with its carrying assumption, or restate the K-block line so it makes no claim about the non-Kalshi arm. Then weaken s13.7 to what is true after the split.
> **reference:** protocol_kalshi-arbitrage-review_2026-09-02.md s8 parts 1-3

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation failed; the finding reproduces exactly and is corroborated by the corpus's own source record.
>
> 1. Locations reproduce verbatim. lit_review_kalshi-arbitrage_2026-09-02.md:1080-1087 sits inside the block opened at :1063 "#### 8.2.1 Kalshi-specific" and reads "binary contracts on Kalshi and Polymarket are treated as structurally identical to cash-or-nothing digital options, and implied volatility surfaces, risk-neutral densities and variance risk premia are extracted from 113,338 Bitcoin and Ethereum contracts traded between September 2025 and February 2026". :1203-1209 sits inside the block opened at :1191 "#### 8.3.1 Kalshi-specific" and reads "A cross-platform study of 72.1 million Kalshi trades ... with 404.5 million Polymarket trades reports a statistically significant bias on both ... and a stated cross-platform contrast in sign". :2170-2172 reads as quoted in the finding. Neither K-block line carries a carrying assumption; grep for "assumption" over both blocks returns nothing inside 8.2.1 or 8.3.1.
>
> 2. Source check confirms the mixed-venue sample rather than refuting it. references_kalshi-arbitrage.json record lee2026ssrn6748186 is titled "Cryptocurrency Prediction Markets through the Derivatives Lens: Evidence from Kalshi and Polymarket" and its stored abstract states "We exploit this equivalence on 113,338 Bitcoin and Ethereum contracts traded on Kalshi and Polymarket ... extracting implied volatility surfaces, risk-neutral densities, and variance risk premia", and further "The VRP differs markedly across platforms, with Polymarket's roughly 16 times larger than Kalshi's". The VRP quantity the K block states is therefore explicitly a cross-platform result, not a Kalshi-measured one. Record gupta2026ssrn6858200 likewise pairs Kalshi with Polymarket trades.
>
> 3. The review's own classification legend contradicts its placement. lit_review:699-706 defines the E4/E15 column as "**K** = Kalshi-specific (the record's own data or institutional object is KalshiEX LLC)". The corpus table nevertheless assigns K to both records: :792 lee2026ssrn6748186 "| T5 | K | S2 | abs | Kalshi-data evidence; enters the Kalshi-specific block of its strand" and :770 gupta2026ssrn6858200 identically. Both records' own data span Kalshi and Polymarket, so K is inconsistent with the legend and with protocol s8 part 1 ("Kalshi-specific iff the supporting record's own data or institutional object is KalshiEX LLC ... Any other value of E4 makes the claim venue-other").
>
> 4. Counter-test for an existing split: awk over section 8 (lines 860-1800) returns every Polymarket mention — :906, :979, :1005, :1075, :1078, :1080, :1204. No line in any 8.x.2 generalized block carries the Polymarket arm of Lee 2026a or Gupta 2026, so the split the finding asks for does not already exist elsewhere in the document. (Line :906, in the 8.1.1 Kalshi-specific block, is a further instance of the same pattern beyond the three cited.)
>
> Only defense found, and it is not admissible as refutation: s13.7 is worded narrowly as "Every claim *generalized from* ... Polymarket ... data", and one could argue a venue-attributed Polymarket finding stated as Polymarket's is not a "generalization". That is a semantic narrowing, not counter-evidence, and it does not touch the first half of the finding — non-Kalshi evidence (including a cross-platform VRP quantity whose Polymarket arm is 16x the Kalshi arm) stated inside Kalshi-specific blocks with no carrying assumption, under an E4=K classification that the document's own legend does not support.

### LITERATURE-1-14 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** conclusion-exceeds-corpus
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:1335-1343
> **issue:** A strand-level conclusion the corpus cannot carry. The S4 header states as 'the corpus's central S4 finding' that the inventory-risk lineage 'does not' state applicability conditions in terms of the binary payoff. That is a positive claim about non-statement, drawn from five named-lineage anchors of which four were read at metadata depth only, while 643 X11 records -- transfer-clause records of exactly that class -- were never assessed at all.
> **evidence:** Line 1341-1343: 'The corpus's central S4 finding is that the first literature states its own applicability conditions in terms of the binary payoff, and the second does not.' Against it: s8.4.3 records Ho & Stoll, Glosten & Milgrom, Kyle, Krishnan and Liu & Wang all at 'metadata depth' with transfer status 'not addressed ... at the depth reached'; G-5 (line 1980-1987) hedges correctly -- 'The corpus cannot say whether the originals address bounded payoffs, because it did not read them'; and A5 (amendments file, line 220-223) states the transfer-clause literature is represented 'by its anchors and its event-market-facing members only'.
> **fix:** Rewrite the S4 header claim to 'does not, at the extraction depth reached, in the records this corpus assessed' and cross-reference the 643 X11 records at the point of the claim rather than only in s13.2.
> **reference:** (none given)

Refutation attempt (outcome: failed; evidence_type `none`):

> Attempted refutation on three fronts; all failed, and the checks corroborated the finding.
>
> 1. Quoted text reproduces verbatim. lit_review_kalshi-arbitrage_2026-09-02.md lines 1341-1343: "The corpus's central S4 finding is that the first literature states its own applicability conditions in terms of the binary payoff, and the second does not." No local depth or coverage qualifier appears anywhere in the 8.4 header block (lines 1335-1343).
>
> 2. Attempted defense via a governing scope convention. Section 8's binding reading rules (lines 863-885) do carry a depth caveat at rule 2 (line 867-870): "Extraction depth is abstract or metadata, never full text ... Every statement below is a statement about what a record's abstract or metadata says." But this does not refute the finding, for two reasons obtained from the text itself: (a) the same rule's second clause — "Where an abstract does not settle a point, this section says so instead of inferring it" — is precisely what the S4 header violates, since the per-record entries in 8.4.3 do say so ("not addressed at the depth reached", lines 1564-1580) while the header does not; (b) rule 2 governs extraction depth only and says nothing about corpus coverage, so it cannot scope a claim ranging over 643 never-assessed records.
>
> 3. Attempted defense via coverage. Confirmed the X11 stratum is exactly the class the header generalizes over: line 657 "X11 | 643 | ... C3 transfer-clause record promoted to stage 2 and not assessed"; line 2084-2086 "A reader who wants the S4 inventory-risk lineage in full ... will find them in the X11 and X10 rows of the verdicts file and not in this corpus." The 643 are cited only in s6/s13.2, never at the claim site.
>
> Corroborating (not refuting) evidence found while checking:
> - 8.4.3 confirms all five named records at metadata depth with transfer status not addressed: Ho & Stoll (1564-1568), Glosten & Milgrom (1572), Kyle (1579), Krishnan (1615), Liu & Wang (1619), plus the bundle note at 1627-1628 "none states a bounded-payoff condition at the depth reached." Only one record (Gueant, Lehalle & Fernandez-Tapia, 1594-1597) is affirmatively "explicitly excluded"; the rest are silence, not negation.
> - G-5 (lines 1980-1987) directly contradicts the header: "The corpus cannot say whether the originals address bounded payoffs, because it did not read them."
> - docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md lines 219-223 confirms the corpus represents this literature "by its anchors and its event-market-facing members only", and lines 226-227 state the governing principle the header breaches: "X6 asserts the record states no applicability condition; that cannot be asserted without reading it."
>
> No concrete counter-evidence obtained. The defect claim stands.

### LITERATURE-1-15 — retained

- raised_by: literature-check; severity_claimed: major; refuted_by: refuter (effort: high)
- evidence_type: **none**; reproduction_required: false; outcome: **retained**

Claim verbatim:

> **category:** frontmatter-contradicts-body
> **location:** C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md:14-25, :31-35
> **issue:** The machine-readable frontmatter -- the surface a downstream artifact consumes -- contradicts the body on the status of the 1,188 unresolved records. X10 and X11 are listed under `eligibility_exclusion:` alongside the nine criterion codes, while the body insists in bold that they are 'not eligibility criteria', and no frontmatter field carries the 1,188 count at all.
> **evidence:** Frontmatter `eligibility_exclusion:` lines 15-25 lists X1..X9 and then X10 and X11 as members of the same list. Body s1:84-88: 'Two disposition codes were added during execution (amendments A4 and A5) and are not eligibility criteria.' Frontmatter carries n_identified/n_duplicates_removed/n_screened/n_excluded/n_included but no field for the 545 X10 + 643 X11, so a consumer reading only the frontmatter sees 8,664 criterion exclusions and a settled 149-record corpus -- the exact reading s13.2 calls 'the single most important number in the flow'.
> **fix:** Move X10/X11 out of `eligibility_exclusion` into a separate `disposition_codes` key, and add explicit frontmatter fields `n_eligible_not_extracted: 545` and `n_eligibility_undecided: 643`.
> **reference:** (none given)

Refutation attempt (outcome: failed; evidence_type `none`):

> Refutation attempted and failed; the finding reproduces exactly.
>
> (1) Frontmatter, lines 14-25 of C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md: the key `eligibility_exclusion:` is followed by eleven sibling list items X1..X9, then line 24 `- "X10 (amendment A4) ELIGIBLE under section 2 and NOT a criterion failure: ..."` and line 25 `- "X11 (amendment A5) ELIGIBILITY UNDECIDED and NOT a criterion failure: ..."`. X10/X11 are structurally members of the eligibility-criterion list.
>
> (2) Body line 84-88: "**Two disposition codes were added during execution** (amendments A4 and A5) and are **not** eligibility criteria." Verbatim match to the auditor's quote.
>
> (3) Contradiction is worse than the finding states, not better. Body line 68-71: the eligibility criteria "are fixed in the frozen protocol sections 1 and 2 and **were not modified during execution**. They are restated in this record's frontmatter under `eligibility_inclusion` / `eligibility_exclusion`." X10/X11 were added *during* execution (amendments A4/A5), so the frontmatter list falsifies the body's own description of what that list contains.
>
> (4) Counter-test for the "no frontmatter field carries the 1,188" claim: I enumerated every top-level frontmatter key in lines 1-47 (title, slug, date, objective, review_type, standard_declared, eligibility_inclusion, eligibility_exclusion, registration, protocol_path, protocol_amendments, bibliography, bibliography_sha256, n_identified, n_duplicates_removed, n_screened, n_excluded, n_included, materials_availability, competing_interests, ai_assistance, git_head_at_authoring, pip_freeze_sha256, dataset_checksums, rng_seed, model_commit) and grepped the file for 1188/1,188/545/643. Every hit is in the body (lines 591-592, 656-657, 662, 2080-2081); zero hits in lines 1-47. No frontmatter field carries 545, 643, or 1,188. The frontmatter flow set is exactly n_identified 15924 / n_duplicates_removed 7111 / n_screened 8813 / n_excluded 8664 / n_included 149.
>
> (5) The body's own characterization of the missing number is confirmed at lines 591-592: "8,664 were excluded, of which **1,188 are capacity dispositions, not criterion failures** (545 X10 + 643 X11) — this is the single most important number in the flow", restated at 13.2 (lines 2080-2085). The finding's attribution of that phrase to s13.2 rather than the flow paragraph is a citation-location slip, not a defect in the claim; 13.2 does restate the 1,188.
>
> (6) Best available mitigation, insufficient to refute: the X10/X11 *strings* inside the list do say "NOT a criterion failure", and the amendments file (docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:155-157, 218-219) documents the deliberate choice that "X10 rows sit in `n_excluded` so that the section 4.3 arithmetic identities continue to hold". That explains the placement of the *counts* inside n_excluded but does not place X10/X11 outside the `eligibility_exclusion` key, does not reconcile them with body line 68-71's "not modified during execution", and supplies no count field. A machine consumer keying on `eligibility_exclusion` still reads eleven criteria, and no consumer of the frontmatter alone can recover the 1,188 split.
>
> No source quote, reproduced check, counter-test, or logical argument available to me contradicts the defect claim.

## deferred-logged-minors

Twenty-four minors logged, not remediated this round (full payloads in the JSON
sidecar; compressed rows in the findings table above). Convergent clusters are
grouped so remediation can address them once:

- **REV-1-16 / QUANT-1-14 (first limb) / LITERATURE-1-7 overlap**
  (standard-coverage / reporting, three-way convergent): the frozen protocol
  §3.1 SSRN caveat requires the un-run SSRN site-search arm to be recorded by
  name as a minor recall verification gap; no AG row and no named statement
  carries it. LITERATURE-1-7 raises the same omission as a major and is being
  remediated; these two carry the AG-row form of the fix and the Kalshi-stratum
  materiality.
- **QUANT-1-11 / LITERATURE-1-16** (reporting /
  internally-contradicted-statement, convergent): AG-3's bolded headline "one
  of the four named bibliographic databases contributed zero records" is false
  as written — the Semantic Scholar topical arm returned zero, while the same
  platform's citation arm contributed 7,303 records. Restate in terms of the
  arm, not the database.
- **QUANT-1-10 / LITERATURE-1-10 overlap** (reporting): G-6's "fifteen of the
  nineteen are T5" is seventeen of nineteen on the corpus table's own tier
  column. LITERATURE-1-10 carries this as a major with the compounding
  synthesis-omission consequence; this minor is the same arithmetic.
- **SCOPE-1-6 / REV-1-11 / LITERATURE-1-8 overlap** (changed / consistency /
  provenance-integrity): the ka-fc-s2-a3 row's `http` cell reads 200 where the
  stored log, the PRISMA-S 5 narrative and AG-4 all say 404. Two majors carry
  it; this minor states the one-cell fix.
- **REV-1-17 / SCOPE-1-9** (consistency / partial, convergent): the
  113,338-contract Kalshi+Polymarket aggregate sits inside the 8.2.1
  Kalshi-specific block with no venue split; the major LITERATURE-1-12 carries
  the separation-rule violation and the s13.7 absolute that it falsifies.
- **SCOPE-1-5** (documented-drift): the front-matter PRISMA item-8 declaration
  names one automation tool where two were used; convergent with the critical
  QUANT-1-1, which finds a third undeclared classifier and is being remediated.
- **QUANT-1-12** (method): three further undeclared deviations — the
  non-executed backward arm, the partial completion of E8-E13, and the off-file
  amendment ledger — each already carried as a major (SCOPE-1-1, SCOPE-1-2,
  REV-1-13); this minor states them as a single A6/A7/A8 filing.
- **REV-1-14** (consistency): §13.5 cites a platform-reported NBER total of
  21,594 that the section-2 table records as "not reported" for both NBER
  queries.
- **REV-1-15** (reporting): the PRISMA-S 5 completeness claim covers a platform
  that reported no totals; only the OpenAlex form (7,855 of 7,855) is
  verifiable.
- **SCOPE-1-7** (partial): the J5 second-hand/unverified flag on the 2.00-cent
  fee is carried in 8.5.1 and section 9 but not at the 8.2.1 restatement.
- **SCOPE-1-8** (documented-drift): the spec's named minimum element
  "inventory-risk market-making models and their applicability to bounded [0,1]
  payoffs" is delivered as a declared absence (G-5) rather than a synthesis;
  documented, so a note rather than a defect.
- **SCOPE-1-10** (added): section 11's five-row `TO COMPUTE` handoff register
  has no spec item behind it in this artifact; small, defensible scope creep,
  no tradeable rule stated.
- **SCOPE-1-11** (documented-drift):
  `docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md`
  does not exist, so Thread C is incomplete at this round. The spec box is
  unchecked, so the absence is declared rather than concealed. **Carried on the
  trail so Thread C is not closed on the corpus record alone.**
- **QUANT-1-13** (verification-gap): an audit-side depth probe at rows=1000
  demonstrates the cap explanation for KI-06, KI-09 and KI-21 and leaves KI-20
  unexplained; the major REV-1-9 and LITERATURE-1-6 carry the interpretation
  defect itself.
- **QUANT-1-15** (numerical): the arXiv 2608.00666 transcription substitutes
  "reconstructed depth-aware violations" for the source's "arbitrage profit
  across two realization channels"; five other numeric transcriptions
  spot-checked exact.
- **QUANT-1-14 (second limb)** (reporting): 990 dedup merge groups span more
  than one DOI while only the 24 twin sets touching included records were
  reviewed under J6, leaving 966 merge decisions unreviewed for over-merging.
- **QUANT-1-16 / LITERATURE-1-21** (reporting / gate-adjudication, convergent):
  the G16 gate adjudication itself, recorded for completeness on both branches
  — the 83 findings are the standing closed publisher-landing-page class and
  should not block; QUANT-1-16 additionally flags the unexplained 150-vs-149
  count in ka-store-doicheck.json.
- **LITERATURE-1-17** (extraction-code-misuse): `explicitly excluded` is
  assigned to Gueant, Lehalle & Fernandez-Tapia on the corpus's own inference
  rather than the record's statement, against section 8 reading rule 2.
- **LITERATURE-1-18** (disclosure-placement): the A3 residual risk is never
  registered as a numbered gap as amendment A3 itself promised, and the record
  never affirmatively states that no included record originated in the
  5,249-record DEFAULT-X1 stratum — the one sentence that would close focus
  item (c).
- **LITERATURE-1-19** (citation-fidelity): a reproduced registrant typo
  ("Abramovicz"), a mangled title ("LOGARITHMIC MARKETS CORING RULES"), a stray
  asterisk ("Das * (2005)") and two null years.
- **LITERATURE-1-20** (truncated-author-list): a four-author paper cited with
  three surnames and no "et al.".

Per project policy, logged minors are carried on the trail and addressed
opportunistically or in a later spec; they do not gate the round verdict. Open
minors from the phase1-sweep, round3-remediation, naming-sweep and
phase2-explosive-review specs remain open by policy and were not re-raised
here.

## verification-of-remediations

**Nothing to verify from a prior round of this loop.** This is round 1 of a
fresh 3-round cap (`rounds_completed: 1`, `cap_reached: false`,
`prior_dispositions: null`); no round-0 remediation exists to confirm, and this
file has no prior round section.

**Positive verifications performed this round** (checks that closed rather than opened items):

- *Registration integrity (focus a, first limb).* The on-disk digest of the
  frozen protocol recomputes to
  `99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4`, matching
  the registration hash named in the task spec; commit
  `27d74738aa35ec1cdf1ec6915b50532e3620ea6f` carries the registration subject
  and is the commit immediately following the ADR-0004 commit, so
  register-before-execute holds. The 35 frozen topical query strings were
  checked against the stored `ka-*.json` `url` fields and executed as written;
  no query was silently altered. What failed is not query fidelity but
  amendment discipline (REV-1-13, SCOPE-1-1, SCOPE-1-2).
- *Flow arithmetic.* All four frozen arithmetic identities reconcile: sum of
  per-query `n_records` = 15,924 = `n_identified`; 15,924 − 7,111 = 8,813 =
  `n_screened`; 8,813 − 8,664 = 149 = `n_included`; and the section 6 per-code
  table sums 6,707 + 338 + 35 + 159 + 236 + 1 + 545 + 643 = 8,664. Two branches
  recomputed these independently, one by hand from the section 2 table and one
  by re-running the archived `ka-universe-script.py` and `ka-dedup-script.py`
  over the stored logs (15,924 raw → 8,813 distinct works / 7,111 duplicates,
  matching `ka-dedup-ledger.json`). No finding was raised against the flow
  arithmetic; the findings against the flow are about what the numbers *mean*
  (REV-1-8, LITERATURE-1-15), not whether they add up.
- *A3 partition reproducibility.* Applying the published 130-token vocabulary
  over the declared `fields_scanned` blob reproduces the published partition
  exactly — REVIEW 2,905 / DEFAULT-X1 5,249 against
  `ka-screening-vocabulary.json`'s `n_review` 2905 / `n_default_x1` 5249 — and
  the forward-citation-only stratum is exactly 8,154. The A3 tool is therefore
  genuinely deterministic and genuinely re-runnable, which is what the
  amendment claims for it. Its defects are disclosure and reach (REV-1-5,
  REV-1-6, QUANT-1-8), not reproducibility.
- *Verdict-ledger integrity.* The 8,813-row `ka-screening-verdicts.jsonl` was
  parsed row by row: per-code totals match the section 6 table exactly (X1
  6,707; X2 338; X3 35; X5 159; X7 236; X9 1; X10 545; X11 643; include 149),
  the rule marginals partition without remainder (R2 5,249 + R8 1,458 = X1
  6,707), and every included record in the ledger is present in the 149-entry
  CSL-JSON store.
- *Directive-8 attribution (focus f).* Every rule-shaped statement in the
  synthesis — Nunes's spread-vs-twice-taker-fee condition, the monotone strike
  ladder, Greene's drift-per-noise statistic, Vlastakis's strategies — was
  traced to its source record and to an explicit E14 non-endorsement, and the
  corpus states no rule of its own. The one challenge to that finding
  (LITERATURE-1-13) was refuted at the gate against the records' own stored
  abstracts. Zero unattributed folklore factors.
- *Identifier resolution (focus j).* Two branches independently re-resolved
  samples of 12 store identifiers each through the DOI Handle System REST API;
  all returned `responseCode` 1 with the registered targets the corpus names,
  including the 302 login-gate case (`10.3905/jod.2019.26.4.128`) and the 404
  case (`10.17811/ebl.7.4.2018.129-136`, correctly and additionally flagged
  AG-8). The 83 G16 findings are closed under the standing
  publisher-landing-page class.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples; the examined evidence may not be
representative. Four specialist branches read four artifacts against the frozen
protocol, the deliverable spec, the stored search logs, the archived pipeline
scripts and a subset of the cited sources; they did not exhaustively verify
every sentence, every citation-claim pairing, every extracted numeral, every
screening verdict against its record, or every cross-artifact dependency.
Absence of a finding is not evidence of absence of a defect — the same
asymmetry the charter enforces for statistical nulls applies to this audit's
own coverage. Three concrete demonstrations of that asymmetry arose this round:
only about 12 of 149 identifiers were fetched and 4 of those 12 surfaced a year
or venue defect, so the true error rate in the section-7 table is very likely
materially higher than the rows enumerated; only 5 of the 149 abstract
transcriptions were independently re-fetched; and the X5 substring-matching
defect (QUANT-1-2) was found only because one branch re-ran the archived
classifier, with the refuter's independent recount putting the affected
population at 64 rather than the 42 first reported.

**Per-branch residual risk** (full statements verbatim in the sidecar):

- *critical-reviewer.* RQI dimensions D1 (importance) and D2 (originality) are
  adequate and carry no finding: the review question is well posed, bounded by
  an instrument rule and a contribution rule fixed before execution, it asks
  what the literature states rather than what is true of the venue, and the
  artifact makes no novel empirical claim. Two risks survive any prose fix.
  First, the 643 X11 records leave the corpus's eligible set undetermined at
  more than four times the size of its included set, concentrated in exactly
  the C3 transfer-clause class that feeds the largest strand and a primary
  objective, so every S4 statement must be treated as provisional by the
  successor stage. Second, no full text was read for any of the 149 records, so
  every extraction field the protocol froze as the reason for the review — E8
  conditions as stated, E10 model applicability conditions, E12 frictions — is
  partially completed at best, and the corpus cannot distinguish a friction a
  paper ignored from one its abstract omitted. Both are disclosed; neither is
  repaired by disclosure. Not opened by this branch, by scope: CHAMP items 7-16
  (the statistical mechanics of the transcribed estimates — p-values, HC1
  standard errors, t-statistics, Brier scores, Clark-West tests and
  Mincer-Zarnowitz slopes in 8.2.1, 8.3.1 and 8.6.1 are quoted from source
  abstracts and were not audited for validity), citation resolution, the
  reproducibility envelope, and promised-vs-shipped completeness.
- *scope-auditor.* Presence-side coverage of the declared spec is high: every
  named element of spec item 5 has a delivered location, and ADR-0004 and the
  protocol satisfy their spec items in full. The residual risk is not omission
  but disclosure form — a downstream artifact that cites the front-matter flow
  counters, the eligibility list or the amendment ledger without reading
  sections 6 and 13 will inherit a corpus described as fully screened when 643
  records remain eligibility-UNDECIDED and 5,249 were verdicted by rule rather
  than by reading. This branch checks presence, not correctness: no transcribed
  figure, page citation or substantive verdict was verified here.
- *quant-auditor.* Even after every fix this branch names, the corpus's
  substantive content rests on 116 abstract-depth and 33 metadata-depth
  readings by a single unverified extractor over a 149-record set selected from
  an 8,813-record universe whose 8,664 non-inclusions were decided by keyword
  rule, so the true recall and the eligibility status of the 1,188 X10/X11
  records remain unknown, and only 5 of the 149 abstract transcriptions were
  independently re-fetched in this audit.
- *literature-check.* Four items are unclosed. (1) The frozen protocol's
  SHA-256 could not be computed in that branch's environment (no hashing tool
  available); the register-before-execute ordering was verified from
  `.git/logs/HEAD` instead, and the digest itself was subsequently confirmed by
  the refuter and again during trail assembly. (2) About 137 of the 149
  identifiers were never fetched; given the hit rate on the 12 that were,
  remediation of LITERATURE-1-1 and -1-2 should be a full regeneration of the
  year and venue columns from the store, not a patch of the enumerated rows.
  (3) No full text was obtained, so whether the abstract-depth transcriptions
  misstate the underlying papers is untested; the artifact's own AG-5
  disclosure is the only control and it is accurate. (4) The A3 DEFAULT-X1
  stratum is unquantifiable by construction as the record states; no included
  record was found attributed to it, but the record never asserts this
  affirmatively, so the confirmation rests on absence rather than on a stated
  check (LITERATURE-1-18).

**Cross-branch residual.** The audit did not re-run the search, did not read
any full text, did not re-screen any of the 8,664 non-included records against
the frozen criteria, and did not verify the substantive results of any source.
The two retained criticals bound what the corpus can be said to be at all: with
3,414 dispositions produced by an undeclared keyword classifier (QUANT-1-1) on
top of the 5,249 declared rule verdicts, the honest description of this
artifact is a keyword-compiled candidate set with a hand-curated 149-record
core, not a screened corpus — and the round verdict of **block** stands on
that, independently of the G16 gate finding, which is dispositioned rather than
remediated.

## ai-assistance-statement

Per [ICMJE Recommendations §V.A (updated January 2026)](https://www.icmje.org/recommendations/):
AI cannot be an author; AI-assistance use is disclosed.

- Models used: Claude Opus 5 (model id `claude-opus-5`, Anthropic, via Claude
  Code / Claude Agent SDK) — all branches: four specialist audit agents
  (critical-reviewer at high effort, scope-auditor at medium effort,
  quant-auditor at high effort, literature-check at high effort, each with
  `model: inherit` in its agent definition), the adversarial refuter (high
  effort), and the trail-assembly agent that authored this document.
- Roles: audit (findings, refutations, independent recomputation of the PRISMA
  flow and the A3 partition, re-execution of the archived pipeline scripts,
  live Crossref and DOI Handle System resolution, one live re-execution of a
  frozen Crossref query at rows=1000) and prose (assembly of this trail). No
  authored research content; the audited artifacts were not modified by this
  round's agents.
- Note recorded rather than resolved: QUANT-1-7 (retained) concerns the audited
  execution run's own missing ReproLog and the absence of any ReproLog or
  sidecar digest in the corpus record's front matter. That is a property of the
  audited artifacts, not of this audit; the model id declared here is this
  audit's own.
- Responsible human: Sajan Koirala, who directed the audit-remediate loop and
  under whose review the verdict and remediations proceed.
- Reproducibility log: ReproLog emission is sequenced with the
  `/commit-with-provenance` step; the log lands at
  `logs/reproducibility/repro_log_{run_id}.json` (gitignored, an untracked
  locator), and its clone-durable digest is carried by the commit's
  `Repro-Log-Path:` / `Repro-Log-SHA256:` trailers per CLAUDE.md
  §Reproducibility contract. The commit hash is to be recorded here as a dated
  addendum when it lands.

## immutability-and-retention

This trail and its JSON sidecar
([audit_trail_kalshi-arbitrage-review_2026-09-02.json](audit_trail_kalshi-arbitrage-review_2026-09-02.json),
SHA-256 `fcad5133001899a700596842e1691a353d1e5375751683f5d72a2eb2cf395a4c`,
holding the round-1 payload verbatim per FAIR I1) are committed to the
repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. Later rounds of this loop append
new round sections to this file; corrections to any recorded entry are appended
as a dated addendum that identifies what it corrects — prior entries are never
edited, overwritten, or deleted. Retention follows the repository's git
history; the tracked file is the durable record, and the front-matter digests
bind it to the exact artifact states audited (HEAD
`27d74738aa35ec1cdf1ec6915b50532e3620ea6f`, `worktree_clean: false`).

---

# Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 2

Appended round section per 21 CFR 11.10(e): the round-1 entries above are
unmodified. Round 2 is a verify-and-hunt round over the 37 critical/major
findings retained at the round-1 gate — all 37 remediated by the lead between
rounds, plus the lead's closure of QUANT-1-7 — and over what those remediations
themselves introduced. Five branches were routed (`reproducibility-verifier`
added to the round-1 four). All five branch verdicts:
**proceed-with-remediation**. Round verdict: **block** — 2 criticals raised
(QUANT-2-1 and LITERATURE-2-1, which are the same defect found independently by
two branches: the withdrawal of the depth-not-vocabulary reading replaced one
false premise with another, and that false premise was written into the
append-only registered protocol addendum as amendment A6), 34 majors raised,
3 refuted and dropped at the adversarial gate, 33 critical/major findings
retained for remediation, 19 minors logged, 0 retained-conservative.

The file-level YAML front matter at the top of this document is the round-1
record and is not edited; the round-2 front matter is carried verbatim in the
fenced block below (and, as JSON, in the round-2 sidecar).

```yaml
schema_version: "WI-3/2"
conforms_to:
  - "PROV-DM / PROV-O"
  - "RO-Crate 1.1"
  - "ISO 19011:2018"
  - "FAIR (Wilkinson et al. 2016, doi:10.1038/sdata.2016.18)"
  - "Sandve et al. 2013 (doi:10.1371/journal.pcbi.1003285)"
  - "21 CFR 11.10(e)"
  - "ICMJE §V.A"
title: "Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 2"
type: audit_trail
date: "2026-09-02"
started_at: "2026-09-02T14:12:06-05:00"
ended_at: "2026-09-02T14:41:38-05:00"
artifacts:
  - {path: "docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "acfc6a57a4ecdaa56a95372930711ed3c7f97f8bb50acc76f0cb3a52a5ee79c0"}
  - {path: "docs/literature/references_kalshi-arbitrage.json", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "fb0cf87ed53dcb0b37076fc5e441c0125ad94644603deb9a9604d5ce5f5c8164"}
  - {path: "docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "42bc6116ee554ee5cc80743d14d2f3d834f4feb389b53b5eaf2820c27322a762"}
  - {path: "docs/decisions/ADR-0004-quant-rule-adoption-prediction-markets.md", git_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", sha256: "51034c44e6e21b5f9281fa7150bbf939867b46b3b863c4be8e329d0ff35ff886"}
repo_head: "27d74738aa35ec1cdf1ec6915b50532e3620ea6f"
worktree_clean: false
audit_criteria:
  task_spec_verbatim: |
    docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C — Kalshi / binary-event-market arbitrage branch. Item 5: a compiled corpus record with search provenance, per-source counts, inclusion/exclusion with reasons, and a synthesis of what the literature establishes about no-arbitrage and coherence conditions for binary contracts, longshot bias, inventory-risk market-making models and their applicability to bounded [0,1] payoffs, and cross-venue price-discrepancy evidence; every claim cited; Kalshi-specific claims separated from generalized ones with the carrying assumption stated. Item 1: ADR-0004. Item 2: the frozen protocol. ROUND 2 — VERIFY THE ROUND-1 REMEDIATIONS AND HUNT WHAT THEY INTRODUCED. Round 1 returned verdict BLOCK with 3 critical and 38 major raised, 4 refuted, 37 retained; all 37 are now remediated. Do NOT re-raise a round-1 finding that is genuinely fixed; DO verify each fix holds and DO raise anything the remediation broke or over-claimed. Claims to verify: (1) QUANT-1-1 (critical) was COMPLIED WITH, not contested — the remediator re-ran the archived pipeline under PYTHONHASHSEED=0 and reproduced the published nine-code table exactly, confirming that every non-include verdict comes from five hard-coded substring lists via rules R3-R8 across all three strata. Published split is now 150 read-based dispositions (149 includes plus 1 hand-verified X9 twin) against 8,663 classifier verdicts, 98.3 percent. Amendment A10 declares the classifier as the PRISMA item-8 automation tool of record; the claims 'every one of them was read individually' and 'All 8,813 were screened at title level' are struck. VERIFY the strike is complete — grep for any surviving assertion that records were read, screened or assessed individually — and verify the 150/8663 split against the verdict files. (2) QUANT-1-2 (critical bug): word-boundary re-run moved 65 records, X5 159 to 94, X11 643 to 700, X7 236 to 244. The remediator DEPARTED from the prescribed fix twice, both declared: 8 of the 65 fall to X7 (a criterion failure, of I3 not B-a, an ordering consequence of R1 running after X1/X2/X5), and the pattern used was \bdexe?s?\b / \bamms?\b / \bdefi\b / \bcrypto rather than bare \bdex\b, because bare \bdex\b would have wrongly moved three genuine DeFi records OUT of X5. Adjudicate both departures. Verify the re-emitted ka-screening-verdicts.jsonl joins on identifier not id, that the audit toggle KA_DEFI_MATCH=substring reproduces the defective behaviour, and that derived totals updated everywhere (capacity dispositions 1188 to 1245, criterion exclusions 7476 to 7419). (3) REV-1-2 (critical): the order-driven/quote-driven contradiction — verify BOTH venue-mechanism assertions are gone, that the Levitt transfer is now marked not-transferable-as-stated, and that G-3's count went from two to five with all five itemized. (4) The remediation found MORE than the audit did in several places and self-reported it: 27 wrong publication years (audit said ~20), 78 wrong container-titles (audit said at least 9), 6 tier contradictions (audit said 4), 19 included records carrying no section 8 claim line (audit said 3, new section 8.8 lists the other 16), 10 records synthesized under a strand E3 does not assign. Spot-verify a sample of each against Crossref/DataCite and the store. Note the sweep reports 149 DOIs checked, 122 Crossref plus 26 DataCite equals 148 verified, 1 unresolvable at either registration agency (10.11179/ker.74.119, new gap AG-10) — check that arithmetic and the AG-10 disclosure. (5) The depth-not-vocabulary reading was WITHDRAWN: parimutuel, dealer, specialist and limit order appear in none of the 45 fenced topical query blocks, so KI-20 Ho-Stoll and KI-21 Avellaneda-Stoikov are demonstrated vocabulary gaps and the topical-arm miss count is restated as 7 of 23. Verify the token absence claim against the protocol's query blocks and that the restated count is consistent. (6) QUANT-1-6 determinism: the published file agreed with a seeded rebuild on only 2,630 of 8,813 uids, so 6,183 row ids were irreproducible; title/venue tie-breaks fixed and the seed pinned. The remediator DELIBERATELY DID NOT convert the abstract tie-break to a set, having verified that doing so changes X1 to 6,672 — i.e. it would be a re-screen disguised as a determinism fix. Adjudicate that refusal. (7) QUANT-1-7 was handed back and the LEAD has now closed it: five frontmatter keys filled with repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json (sha256 416d4d4891ffd9804f0276e91dc96d5c48460764722191ede10d5fbf476b94ee), sidecar artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json (sha256 96c4134c03f247edc2837e178525a9f215fb8eeb2ab30ca3b9ac53a5e1d5647a), pip_freeze_sha256 51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e. Section 13.8 states two scope limits: the ReproLog covers the search-execution and remediation run but not the protocol-drafting stage which emitted none, and the archived pip-freeze describes the lead session's interpreter whereas the search scripts ran on the Python 3.11 standard library alone. Verify the digests resolve and that those two scope limits are honestly stated rather than used to excuse the gap. (8) Seven new amendments A6-A12, total 12; frozen prefix must still hash to 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4 over the first 82677 bytes and the full protocol to 42bc6116ee554ee5cc80743d14d2f3d834f4feb389b53b5eaf2820c27322a762. (9) The G16 gate: the record still self-reports verdict block on 83 findings, now dispositioned by SECTION HEADING rather than file-and-line. Confirm the disposition is correctly recorded and that the two substantive residuals AG-8 and AG-10 are carried. (10) THE STANDING QUESTION THIS ROUND MUST ANSWER: after all 37 remediations, is this artifact now a defensible compiled corpus, or does the combination of 98.3 percent classifier-produced dispositions, 700 records with undecided eligibility, 545 eligible-but-unextracted, and zero full texts read mean the synthesis claims still exceed what the corpus can carry? Give a direct answer, because this round's verdict determines whether the deliverable ships or is surfaced to the author as not shippable.
  files_consulted:
    - {path: "~/.claude/CLAUDE.md", sha256: "9cedf7468cd844c8a43707f5a37c9218c81130e07264e7bba5d83619f4850d5f"}
    - {path: "~/.claude/rules/quant-project.md", sha256: "433d08b43becdce817d6baa00faf5f70b671352110748ca3405a9487759bb39f"}
    - {path: "~/.claude/rules/population-health.md", sha256: "f955fca41e427bad0b389ace10fe499a618f147c4db21b1995a24d12c89ed966"}
    - {path: "~/.claude/rules/publishing.md", sha256: "a0c0980c28dfbf1fb7424f880d72e2f7f5875886b71db2b1e4039970af033479"}
    - {path: "CLAUDE.md", sha256: "2d37579a3e967ea72a2805789f2ea0c40222da211ef7e7ce4d3ad8bc03d41759"}
    - {path: "docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md", sha256: "6425f053ce0e3dfd0554d7a103f3f65b76fdd46b95f4c4df6b5147eafd30e17d"}
    - {path: "docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md", sha256: "42bc6116ee554ee5cc80743d14d2f3d834f4feb389b53b5eaf2820c27322a762"}
    - {path: "docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md (round-1 trail, digest as it stood when this round opened)", sha256: "e4a072e42e298d528f3319798f748a9c863df8f135fe9761eda56791aee4f6fa"}
mechanism: "Workflow engine — workflows/audit-remediate.js (deterministic routing, parallel specialist auditors, schema-validated findings, adversarial refute gate on every critical/major finding per audit-remediate-loop skill). Round 2 is a verify-and-hunt round: every round-1 remediation that is mechanically checkable was re-derived independently from the committed logs and the archived scripts, and every new critical/major finding passed the refute gate before retention."
agents:
  - {branch: "critical-reviewer", agent_def_path: "~/.claude/agents/critical-reviewer.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "scope-auditor", agent_def_path: "~/.claude/agents/scope-auditor.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "quant-auditor", agent_def_path: "~/.claude/agents/quant-auditor.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "literature-check", agent_def_path: "~/.claude/agents/literature-check.md", model_id: "claude-opus-5", effort: "high", role: "audit"}
  - {branch: "reproducibility-verifier", agent_def_path: "~/.claude/agents/reproducibility-verifier.md", model_id: "claude-opus-5", effort: "medium", role: "audit"}
  - {branch: "refuter", agent_def_path: "workflows/audit-remediate.js (inline adversarial refute-gate branch; no standalone agent file)", model_id: "claude-opus-5", effort: "high", role: "refute"}
operator: "Sajan Koirala (responsible human; repo git identity user.name = Sajan Koirala, user.email = 238704148+s-koirala@users.noreply.github.com)"
acted_on_behalf_of: "Delegation chain: Sajan Koirala → lead orchestrator session (Claude Opus 5, claude-opus-5) → workflows/audit-remediate.js → routed specialist branches (critical-reviewer, scope-auditor, quant-auditor, literature-check, reproducibility-verifier) → adversarial refuter → trail-assembly agent (this round section)"
routing: "Deterministic by artifact type and audit focus per workflows/audit-remediate.js. Five branches routed over the same four Thread C artifacts. The round-1 four are re-routed for continuity of verification: critical-reviewer (adequacy of the 37 remediations, interpretation, RQI dimensions, and the standing shippability question) high; scope-auditor (declared-spec coverage against deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C after remediation) medium; quant-auditor (independent re-execution of the archived screening pipeline, the A11 word-boundary deltas, the flow identities, the registrant metadata sweep and the DOI arithmetic) high; literature-check (primary-source and identifier re-verification of the year, container-title, tier and author-list sweeps, and of the new section 8.8) high. reproducibility-verifier is routed this round because the remediation introduced digest, ReproLog, determinism-seed and re-execution claims (A11, A12, §13.8, the re-emitted verdicts file) that are re-derivable and were not part of round 1's routing; medium effort. epi-auditor was not routed (no population-health artifact, no human-subjects data)."
rounds_completed: 2
rounds_cap: 3
cap_reached: false
verdict: "block"
counts: {raw_critical: 2, raw_major: 34, raw_minor: 19, refuted: 3, retained_conservative: 0, to_remediate: 33, minors_logged: 19}
sidecar: {path: "docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json", sha256: "2eb62d0a716b19ac0e6607f02d760fb30fdbe7231537474c12520a68fb51a4f0"}
```

Notes on the round-2 record. `started_at` / `ended_at` bound the trail-assembly
interval for this round section. Two of the four audited artifacts moved between
rounds: the corpus record from `43e3a8a6…` to `acfc6a57…` (the 37 remediations
plus new sections 8.8 and 13.9) and the frozen protocol from `99524df0…` to
`42bc6116…`, because amendment A12 appended A1–A12 into its append-only
addendum — the frozen prefix over the first 82,677 bytes still hashes to
`99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4` and is
byte-identical to the blob in registration commit `27d7473`, independently
confirmed on two branches, so the register-before-execute ordering survives the
amendment. The bibliography store (`fb0cf87e…`) and ADR-0004 (`51034c44…`) are
unchanged. `repo_head` is unchanged at `27d74738…`: every remediated artifact is
still in the worktree, untracked or modified, so `worktree_clean: false`. The
round-1 sidecar digest (`fcad5133…`) is bound into the round-1 front matter and
that file is untouched; the round-2 payload is written to a separate sibling,
`audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json`, per append-only
retention. The round-1 trail is listed in `files_consulted` as the source of the
prior dispositions the four round-1 refutations bind this round; its digest is
recorded there as the file stood when this round opened.

**On the verdict.** Five branches each returned `proceed-with-remediation`, and
the round verdict is nonetheless **block**. That is not an override of the
branches: the loop's gate is severity-based, and two criticals survived the
adversarial refuter (QUANT-2-1 and LITERATURE-2-1, one defect found twice
independently). Both are prose-and-amendment fixes; neither requires re-running
the search or re-screening a record. The direct answer to the task spec's
standing question, on which all five branches agree and which is reproduced in
full in the residual-risk section below: the artifact **is** now a defensible
compiled corpus record — of what a published keyword classifier retrieved and
what 116 abstracts plus 33 metadata stubs state — and its section-8 synthesis no
longer exceeds that capacity, because the remediation trimmed the claims to it.
It is not yet shippable, for a different reason than round 1's: the remediation
introduced fresh factual errors inside the very passages written to remove
over-claiming, and three of its traceability rows name edit sites that were not
edited. Close those and it ships as a corpus record; it must not be cited
downstream as a coverage claim about the literature.

## findings-table

One row per finding — 36 critical/major (33 retained, 3 dropped at the gate)
and 19 minors, 55 rows. All eight schema fields (id, severity, category,
location, issue, evidence, fix, reference) plus branch and disposition;
issue, evidence and fix are compressed for tabular legibility. The full
unabridged text of every finding, every refutation and every per-branch residual
statement is held verbatim in the JSON sidecar
([audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json](audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json),
SHA-256 `2eb62d0a716b19ac0e6607f02d760fb30fdbe7231537474c12520a68fb51a4f0`), and every critical/major claim is reproduced verbatim and
unabridged in the refute-gate section below. Counts object, verbatim from the
round payload: raw_critical 2, raw_major 34, raw_minor 19, refuted 3,
retained_conservative 0, to_remediate 33, minors_logged 19.

| id | severity | category | location | issue (compressed) | evidence (anchor) | fix (compressed) | reference | branch | disposition |
|---|---|---|---|---|---|---|---|---|---|
| REV-2-7 | major | verification-gap | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:751-753; docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdi… | The verification route the record prescribes for the re-emitted verdicts file does not resolve the include set. The record instructs the reader to join on `identifier`, but the verdicts file's `identifier` is the merge-group representative, which for J6 twin sets is not the DOI the bibliography store retains. In the fi… | **Consequence for a reader holding the pre-remediation Table X-full:** `uid` values in the re-emitted file do not correspond to the old ones. **Join on the `identifier` f… | State in section 5 and in the verdicts header that `identifier` is the merge-group representative and may differ from the store DOI where J6 retained a different version; report the number of include rows affected; and name ka-dedup-ledger.… | CHAMP item 23 (enough detail for re-analysis); PRISMA 2020 item 27 | critical-reviewer | **refuted → dropped** |
| SCOPE-2-1 | major | partial | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2563-2571 (G-5); 2041-2154 (8.4.3); 2760-2779 (13.2) | One of the five synthesis components the deliverable spec names for item 5 — 'inventory-risk market-making models and their applicability to bounded [0,1] payoffs' — is delivered as a declared non-answer rather than as synthesis. Four of the five named-lineage anchors sit at metadata depth with transfer status 'not add… | G-5: 'Of the five named-lineage anchors, four are at metadata depth with transfer status `not addressed`, and the one whose model is stated in the retrieved text assumes… | Either (a) retrieve and extract the five inventory-risk anchors (Ho & Stoll 1981, Avellaneda & Stoikov 2008, Glosten & Milgrom 1985, Kyle 1985, Guéant-Lehalle-Fernandez-Tapia 2012 — all canonical and retrievable) so the applicability compon… | S-5 | scope-auditor | **refuted → dropped** |
| LITERATURE-2-2 | major | unverifiable / fabricated count | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2849-2850 | 'the 45 fenced topical query blocks in section 3' is a count that does not exist in the protocol and contradicts the same document 19 lines earlier. | Review :2849-2850 says 'none of the **45 fenced topical query blocks in section 3**'. Review :2830 says 'The **35 topical queries**'. Protocol A6 :1480 says 'the 35 froze… | Replace 45 with 35 and state the derivation (section 3.2 fences only), or state 41 and name the 6 S7 doc fences separately. A count used as the denominator of a negative existence claim must be reproducible from the cited section. | — | literature-check | **refuted → dropped** |
| REV-2-1 | major | consistency | docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1303,1317,1327,1346-1352; docs/literature/search_logs/kalshi-arbit… | The QUANT-1-1 strike is INCOMPLETE, and amendment A12 propagated the unstruck text into the frozen protocol's own addendum. A10 strikes exactly three sentences, only one of which is A3's; four further A3 assertions of individual reading survive verbatim in both the amendment log and — new this round — inside the protoc… | ### A3 — 2026-09-02 — mid-screening (declared before any record in the affected stratum received a verdict; 3,300 of the 8,154 affected records had already been read indi… | Append a numbered amendment (A13) that strikes the remaining four A3 assertions by quoted sentence — the heading parenthetical '3,300 … had already been read individually', 'each such record is read and verdicted individually by the LLM scr… | CHAMP item 6 (consistency with the pre-registered protocol); PRISMA 2020 item 8 | critical-reviewer | retained → remediate |
| REV-2-2 | major | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:62-68 vs :2998,:3006 | Two rows of the round-1 traceability table cite an edit site that does not exist. QUANT-1-1's fix row names '"Read this first" item 2' and REV-1-8's names '"Read this first" items 1-4'. The 'Read this first' block contains no numbered items, does not state that 98.3% of dispositions are classifier outputs, and does not… | **Read this first.** This artifact is a **compiled corpus record** produced by a **registered search**. It is **not a systematic review**, it reports **no inter-rater agr… | Either add the numbered items 1-4 the traceability table claims (at minimum: 98.3% of dispositions are keyword-classifier outputs; 1,245 records ended screening unresolved; no full text was read; 33 of 149 are metadata-depth only), or corre… | SAMPL (reporting completeness); CHAMP item 17 | critical-reviewer | retained → remediate |
| REV-2-3 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:575-577 vs :628-635, :2589-2595, :3010 | The REV-1-12 fix did not reach the claim it was supposed to withdraw. Section 4 states 'this record withdraws the offsetting claim rather than leaving it standing on queries that never ran', G-8 states 'In execution the narrowing is not offset', and the 13.9 row records the fix as 'the `prisma-s-9` offsetting claim wit… | the unrestricted forms of both phrases are carried by `ka-crossref-07`, `ka-crossref-11`, `ka-openalex-06` and `ka-s2-02`, so no vocabulary is category-gated out of the s… | Rewrite the closing clause of the prisma-s-9 paragraph in place: state that the offsetting forms were carried by ka-crossref-07, ka-crossref-11 and ka-openalex-06 as executed and by ka-s2-02 as planned, that ka-s2-02 returned zero (AG-3), a… | PRISMA-S item 9; CHAMP item 19 (no selective reporting) | critical-reviewer | retained → remediate |
| REV-2-4 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2806 (AG-1 row) vs :2537-2546 (G-3) | The REV-1-2 remediation raised the not-transferable-as-stated count from two to five and itemized all five in G-3, every one of them needing a fact blocked by AG-1 (S7-5). The AG-1 row in the access-gap table still reports the pre-remediation count of two and names only the two original sites. The access-gap table is t… | Two generalized claims in section 8 are marked `not-transferable-as-stated` because of it (8.1.2 protocol-executable arbitrage; 8.2.2 bookmaker-plus-exchange arbitrage),… | Update the AG-1 'what could not be extracted as a result' cell to five marks and list the same five sites G-3 lists (8.1.2 Gebele; 8.2.2 Franck; 8.3.2 Thaler & Ziemba; 8.3.2 Levitt; 8.4.2 continuous-double-auction attribution), or replace t… | CHAMP item 18; internal consistency | critical-reviewer | retained → remediate |
| REV-2-5 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2412-2434 (section 8.8) | Section 8.8, created by this remediation, mis-describes its own 16-row table three times. The table has 9 metadata-depth rows (Berg, Cao, Koch, Restocchi, Sestovic x2, Sethi, Swanson, Zhou) and 7 abstract-depth rows (Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung). The prose says eleven are metadata dep… | **Eleven of the sixteen are at metadata depth**, where naming without stating is the only honest disposition. **Five are at abstract depth and simply were not carried** —… | Restate as nine metadata-depth and seven abstract-depth, and list all seven abstract-depth records (adding Oliven & Rietz) as unexcused synthesis omissions; regenerate the counts mechanically from the table's own depth column rather than by… | SAMPL (numerical consistency); CHAMP item 22 | critical-reviewer | retained → remediate |
| REV-2-6 | major | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:248-250, :2598-2600, :2814, :2733 | The SSRN recall-gap consequence is understated against the record's own section-7 table. Counting rows carrying both an E4/E15 value of K and a 10.2139/ssrn.* identifier gives 15 of the 19 Kalshi-specific records, not 13. The number 13 is repeated at four sites (prisma-s-4, G-9, AG-10 row's neighbour AG-9, amendment A7… | **31 of the 149 included records carry `10.2139/ssrn.*` DOIs, and 13 of the 19 Kalshi-specific records do** | Recount the intersection mechanically from the section-7 table and change 13 to 15 at all four sites (prisma-s-4, G-9, AG-9, amendment A7); state the derivation so the number is re-checkable. | CHAMP item 18; SAMPL (numerical consistency) | critical-reviewer | retained → remediate |
| REV-2-8 | major | interpretation | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2141-2143 | A residual venue-mechanism presupposition survives the REV-1-2 fix, and it decides a transfer. The bookmaker market-making entry in 8.4.3 states unconditionally that E6 blocks the transfer 'to an order-driven exchange'. The destination of every transfer in this corpus is the venue of interest, whose mechanism the recor… | *Transfer status: `addressed` for the payoff support — these are state-contingent claims with endpoint settlement — but the mechanism is a bookmaker book, so E6 blocks th… | Rewrite the clause conditionally — 'E6 blocks the transfer to any order-driven venue; whether the venue of interest is one is not established (S7-5, AG-1)' — and either add the site to the G-3 table as a sixth mark or state why it is not on… | CHAMP item 30 (conclusions limited to what the analysis supports); CHAMP item 27 | critical-reviewer | retained → remediate |
| SCOPE-2-2 | major | spec-conflict | docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:125-138 (Thread C, search-logs + store item) | The canonical spec's ticked PASSED check for the search-logs/store item records verification evidence that the post-remediation artifact contradicts on four numbers, and the spec was not updated when the remediation moved them. A reader taking the spec as the acceptance record gets a completeness picture the delivery n… | Spec: 'all 86 protocol query rows executed, with the five deviations recorded as numbered append-only amendments A1-A5' and 'amendment A5's disposition code X11 leaves 64… | Append a dated correction note under that spec item restating the check as executed-after-remediation: twelve amendments, two protocol arms unexecuted (A6, A7) with G-7/G-9 as their recall consequence, 700/545/1,245 as the unresolved split,… | S-4 | scope-auditor | retained → remediate |
| SCOPE-2-3 | major | omitted | spec (Thread C item 6) — docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md | The spec-declared branch agenda does not exist anywhere in the repository, although the corpus record's section 10 gaps (G-1…G-10) and section 11 TO COMPUTE handoffs were written as its input and ADR-0004 delimits the prediction-market branch to include that path. The spec box is unchecked, so the absence is declared r… | Glob of docs/research_notes/ returns only research_agenda_context-portability_2026-08-21.md, research_agenda_architecture_2026-08-21.md, research_agenda_regime-classifica… | Write the agenda against G-1…G-10 and TC-1…TC-5 with one genuine branch-level falsification test each, or, if it is being deferred to a successor session, record the deferral as a dated spec note naming the successor so the absence is a dec… | S-6 | scope-auditor | retained → remediate |
| SCOPE-2-4 | major | partial | docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md:11 vs spec Thread D (docs/deliverables/deliverable_spec_open-items-k… | The audit trail shipped for this branch is delivered under a path no spec item names, and it covers only Thread C. The spec's Thread D item declares a single trail at docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md covering 'this session's audit round(s) over Threads B and C'. No trail covering Thread… | Spec Thread D: '`docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` … WI-3 §2 trail for this session's audit round(s) over Threads B and C'. Shipped: docs… | Either rename/extend the Thread D spec item to name the per-branch trail slug actually in use (audit_trail_kalshi-arbitrage-review_*) and add an explicit statement that Thread B carried no audit round because it was discharged pre-session,… | S-7 | scope-auditor | retained → remediate |
| SCOPE-2-5 | major | partial | docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:107,121,131-132,147,150-153; mirrored via A12 at docs/metho… | The A10 strike of the individual-reading claims is incomplete. A10 strikes exactly three named sentences (A3's '659 … every one of them was read individually', the verdicts-file 'encodes that reading' claim, and the corpus record's section-5 'All 8,813 were screened at title level'). It does not strike A3's four other… | ka-protocol-amendments.md:107 'A3 … 3,300 of the 8,154 affected records had already been read individually'; :121 'each such record is read and verdicted individually by… | Extend A10 (or issue A13, append-only) with an explicit strike list naming those four A3 statements by quotation, and re-append the corrected amendment text to the protocol addendum, recomputing and republishing the protocol-with-addendum d… | S-5 | scope-auditor | retained → remediate |
| QUANT-2-1 | critical | method | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2856-2866 (and 2849) | The withdrawal of the depth-not-vocabulary reading over-corrected into a false factual claim about the artifact's own queries. Section 13.4 asserts that for KI-21 (Avellaneda & Stoikov, 'High-frequency trading in a limit order book') 'the string `limit order` appears in **none** of them [the topical queries]' and concl… | Independent extraction of the 41 topical fenced blocks from lit_review section 3 and URL-decoding: `parimutuel` False, `pari-mutuel` False, `dealer` False, `specialist` F… | Restate 13.4: `limit order` IS carried by ka-crossref-12, so KI-21 is not a demonstrated vocabulary gap; its miss is undetermined between vocabulary and the rows=20 cap against 4,458,996 reported results, and the cap explanation is the live… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 3 fence ka-crossref-12; section 2 provenance… | quant-auditor | retained → remediate |
| QUANT-2-2 | major | numerical | docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:553-560; docs/methodology/protocol_kalshi-arbitrage-review_… | The deliberate refusal to convert the abstract tie-break to a set is defended by a specific numeric verification that does not reproduce. A11 states: 'This was verified: with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (`X1` 6,672 instead of 6,707); with it l… | Reconstruction fidelity first: PYTHONHASHSEED=0 rerun of ka-universe-script.py -> ka-dedup-script.py -> ka-partition-script.py -> ka-screening-script.py reproduces ka-scr… | Strike the '6,672 instead of 6,707' sentence from A11 (b) in both ka-protocol-amendments.md and the protocol addendum and replace it with the correct and sufficient justification, which is the stability argument already in ka-dedup-script.p… | Re-execution transcript; docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py:73 | quant-auditor | retained → remediate |
| QUANT-2-3 | major | method | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:38,110,949,950; artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae52… | The A10 restatement of X10 was not propagated to four sites, three of which are in the very section the frontmatter NOTE claims was made consistent. Amendment A10 and the verdicts-file header state that X10 is 'NOT an eligibility determination... eligibility under I1-I5 was never assessed'. Surviving contradictions: (a… | lit_review:110 'X10 marks records that **passed** eligibility and were not extracted'; lit_review:949 'X10: eligible S4/S7 platform-design record serving a secondary obje… | Rewrite line 110 to match the frontmatter wording ('X10 marks a keyword-identified candidate stratum whose eligibility was never assessed'); rewrite the two section-6 itemized reasons to drop 'eligible'; rename the frontmatter key to `n_key… | protocol amendment A10, ka-protocol-amendments.md:408-441 | quant-auditor | retained → remediate |
| QUANT-2-4 | major | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2431-2434 | Section 8.8, which the remediation added, miscounts its own table in the direction that flatters the corpus. The prose reads 'Eleven of the sixteen are at metadata depth' and 'Five are at abstract depth and simply were not carried — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung — and that is a synthesis omission, not… | Mechanical tally of the 8.8 table depth column: abs = Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung (7); meta = Berg, Cao, Koch, Restocchi, Sestovic x2,… | Change 'Eleven' to 'Nine' and 'Five' to 'Seven', and add Oliven & Rietz to the enumerated list. | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 8.8 table, rows 2412-2428 | quant-auditor | retained → remediate |
| QUANT-2-5 | major | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2415; docs/literature/search_logs/kalshi-arbitrage/ka-gate-verdict.json | Section 8.8, added by the remediation, cites Berg et al. 2008 under a DOI that does not exist: `10.1007/s15740722070`. The store and the section-7 table both carry `10.1016/s1574-0722(07)00080-7`; the string in 8.8 is the record's internal store key `berg2008s15740722070` with a Springer prefix pasted on. This defeats… | https://doi.org/api/handles/10.1007/s15740722070 -> HTTP 404 (no handle). Correct identifier verified: https://api.crossref.org/works/10.1016%2Fs1574-0722%2807%2900080-7… | Correct the 8.8 Berg cell to `10.1016/s1574-0722(07)00080-7`, then re-run the research-compile gate against the remediated document and re-record ka-gate-verdict.json with its new date/verdict, so the disposition in section 12 describes the… | DOI Handle System REST API https://doi.org/api/handles/{doi}; docs/literature/references_kalshi-arbitrage.json… | quant-auditor | retained → remediate |
| QUANT-2-6 | major | reproducibility | docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl (header `remediation.row_ids`); ka-screening-script.py:24… | The join key the remediation prescribes for reconciling the re-emitted verdicts against the pre-remediation file is not a key. The header instructs 'Join on the `identifier` field, not on `id`', but `identifier` is the empty string for 1,890 of the 8,813 rows (21.4%) — every record with no DOI, no arXiv id and no RePEc… | Tally over ka-screening-verdicts.jsonl: 8,813 data rows; distinct `identifier` values = 6,924; exactly one duplicated value, the empty string, with multiplicity 1,890. Fi… | State that the join is only defined for the 6,923 rows carrying a persistent identifier and that the other 1,890 are unreconcilable; rename the header's 'uid values in this file' to 'id values'; and either archive the pre-remediation verdic… | docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:181-190 | quant-auditor | retained → remediate |
| QUANT-2-7 | major | reproducibility | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:52 (frontmatter pip_freeze_sha256); logs/reproducibility/repro_log_8f5b0… | The pip-freeze digest published to close QUANT-1-7 does not verify against the archived file. The frontmatter and the ReproLog both publish pip_freeze_sha256 = 51760dc96e6e...c0550e and point at logs/reproducibility/env/51760dc9....txt. Hashing that file as stored gives 3796147276...0c40. The published digest is the CR… | sha256(raw bytes, 3405 bytes, contains CR) = 379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40; sha256(bytes with \r\n->\n) = 51760dc96e6ea3cbf93f08976bc35… | Either re-archive the pip-freeze with LF endings so the filename, the raw digest and the published digest coincide, or add an explicit note in the ReproLog and section 13.8 that pip_freeze_sha256 is computed over LF-normalized content. Do n… | CLAUDE.md §Reproducibility (hook-enforced): 'Every bootstrap, backtest, or inference run must log: git HEAD, p… | quant-auditor | retained → remediate |
| QUANT-2-8 | major | reproducibility | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:967-977 (section 7 preamble) | The single largest metadata remediation in this round has no archived evidence log. Section 7 states that all 149 DOIs were fetched from a registration agency at remediation time (122 Crossref, 26 DataCite, 1 unresolvable), that the store 'was checked against the registrant and found correct on every comparable field:… | ls docs/literature/search_logs/kalshi-arbitrage/ contains no registrant-metadata sweep log; ka-store-doicheck.json fields are {date_checked, method: 'DOI Handle System RE… | Emit and commit the sweep log (one row per DOI: registrant queried, HTTP status, returned issued/container-title/type, store value, agree/disagree) as ka-store-registrant-sweep.json, and cite it at section 7 the way every other check in thi… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md frontmatter ai_assistance: 'every metadata field tra… | quant-auditor | retained → remediate |
| QUANT-2-9 | major | numerical | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:857,873-878; docs/literature/search_logs/kalshi-arbitrage/ka-protocol-am… | ADJUDICATION OF THE TWO DECLARED QUANT-1-2 DEPARTURES, plus an overstatement in the second. Departure 1 (8 of 65 records fall to X7 rather than X11): UPHELD. All 8 carry no DOI, arXiv id or RePEc handle, so under the frozen first-code-that-applies ordering the model branch legitimately routes them to an I3 failure; the… | Bare-pattern rerun: {include 149, X1 6707, X2 338, X3 35, X5 92, X7 244, X9 1, X10 545, X11 702} vs published X5 94 / X11 700 — differing records are exactly 'Dynamic Fun… | In A11 and section 6, name only the two records the bare patterns would have moved and drop the third; and either recompute 289/305 and 83/128 with the shipped patterns (284/305, 64/128) or state explicitly that those two figures are measur… | Re-execution of ka-screening-script.py with BOUNDED overridden; docs/literature/search_logs/kalshi-arbitrage/k… | quant-auditor | retained → remediate |
| LITERATURE-2-1 | critical | misquoted / false supporting premise introduced by remediati… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2856-2862; docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.… | The round-1 remediation withdrew a wrong premise (the 'parimutuel' depth-not-vocabulary reading) and replaced it with another wrong premise. The claim that KI-21 Avellaneda & Stoikov is a 'demonstrable vocabulary gap' because 'the string `limit order` appears in none' of the topical queries is factually false, and the… | Review :2859-2862 — 'KI-21 Avellaneda & Stoikov, *High-frequency trading in a limit order book* — the string `limit order` appears in **none** of them. ... No cap can exp… | Strike the KI-21 sentence and A6's 'neither term appears' sentence. Restate: `ka-crossref-07` did ask for 'market making inventory risk optimal bid ask quotes limit order book', so for KI-20 and KI-21 the cause of the miss is NOT a vocabula… | Protocol section 3.2 fenced block ka-crossref-07 (primary artifact text); PRISMA-S item 8 (search strategies a… | literature-check | retained → remediate |
| LITERATURE-2-3 | major | misdated citation of a canonical method source; the year-swe… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1000-1004, 1069, 1128, 1189, 1856 | The remediation rewrote 27 year cells to the registrant `issued` field on the stated ground that it is 'the registrant's earliest recorded publication date'. For the University of Buckingham Press (10.5750) stratum that field is a retro-registration date, not a publication date, and the artifact now publishes 'Hanson 2… | Artifact :1128 'Hanson (2012). LOGARITHMIC MARKETS CORING RULES ... 10.5750/jpm.v1i1.417' and :1856 '([Hanson 2012](https://doi.org/10.5750/jpm.v1i1.417), T1, abstract de… | Add a documented exception to the year CONVENTION for retro-registered DOIs: where the registrant's `issued` year is inconsistent with the registrant's own volume/issue and `created` fields, carry the volume-year and record both. At minimum… | Crossref REST API record for 10.5750/jpm.v1i1.417 (volume 1, issue 1, pages 3-15, created 2020-08-26) | literature-check | retained → remediate |
| LITERATURE-2-4 | major | misdated + tier-too-low | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1089, 1861-1869 | Chen & Pennock, 'A Utility Framework for Bounded-Loss Market Makers', is cited as a 2012 T5 preprint. It is a peer-reviewed UAI 2007 proceedings paper; arXiv:1206.5252 is the 2012 bulk upload of the UAI proceedings. The artifact says it read this record at abstract depth, and the arXiv abstract page carries the journal… | Artifact :1089 'Chen (2012). A Utility Framework for Bounded-Loss Market Makers. arXiv. 10.48550/arxiv.1206.5252 \| T5'; :1867 '([Chen & Pennock 2012](https://arxiv.org/ab… | Cite as Chen & Pennock (2007), UAI 2007, and re-tier T1 with the arXiv posting recorded as the retrieved manifestation. Re-run the tier check against the registrant/arXiv journal-ref rather than against the artifact's other copy of its own… | — | literature-check | retained → remediate |
| LITERATURE-2-5 | major | broken identifier + internal count errors in newly added tex… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2415, 2431-2434 | Section 8.8 is new in this remediation and it introduces a non-resolving DOI and two wrong counts, one of which contradicts the list printed immediately after it. | (a) :2415 'Berg et al. 2008 `10.1007/s15740722070`'. The section-7 row for the same record (:1078) carries `10.1016/s1574-0722(07)00080-7`. `10.1007/s15740722070` is a ma… | Correct the Berg DOI to 10.1016/s1574-0722(07)00080-7; change 'Eleven'→'Nine' and 'Five'→'Seven'; add Oliven & Rietz to the abstract-depth-not-carried list. Generate the 8.8 DOI column from the store rather than from the record id. | — | literature-check | retained → remediate |
| LITERATURE-2-6 | major | misattributed author lists | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1043, 1895, 1927 | Section-8 claim lines truncate author lists without 'et al.', naming three authors for four- and five-author papers. The remediation swept years and container-titles but did not sweep author lists, and the artifact elsewhere prints full lists for 4- and 5-author works, so a reader cannot tell truncation from a complete… | (a) :1895 '[Chen, Fortnow & Lambert 2008](https://doi.org/10.1145/1386790.1386822)'. Crossref author order for that DOI: Yiling Chen, Lance Fortnow, Nicolas Lambert, Davi… | Regenerate every section-8 author list from the CSL-JSON store's `author` array with an explicit, stated rule (full list, or first-author + 'et al.' above N), and re-check all multi-author claim lines. Two verified errors in a non-exhaustiv… | Crossref REST API records for 10.1145/1386790.1386822 and 10.1287/opre.2022.0417 | literature-check | retained → remediate |
| LITERATURE-2-7 | major | verdict-source attribution arithmetic does not close | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:679-687 | At the primary site of the QUANT-1-1 remediation, the enumeration of which strata make up the 8,663 classifier verdicts sums to 8,813 — i.e. it re-includes the 150 read-based records the sentence has just carved out. | :681-686 'The other 8,663 were verdicted by the deterministic five-list keyword classifier ... rules R0-R9 — including the 5,249-record amendment-A3 DEFAULT-X1 stratum (r… | State the three strata net of the 150 read-based records (or say 'the classifier-verdicted subsets of' those strata and give the net figures), so the enumeration reconciles to 8,663. | — | literature-check | retained → remediate |
| REPRODUCIBILITY-2-1 | major | data_hashed | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:frontmatter pip_freeze_sha256; logs/reproducibility/repro_log_8f5b02d3bf… | The QUANT-1-7 closure digest for the environment does not verify against the bytes of the file it names. Four of the five filled keys verify byte-exactly; this one does not. | sha256 of logs/reproducibility/env/51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e.txt as stored on disk (3,405 bytes, 172 CRLF line endings) = 379614727… | Either re-archive the pip-freeze with LF endings so the content-addressed filename and the declared digest match the bytes, or state the normalisation rule next to the key ('SHA-256 over the LF-normalised text') so a verifier can reproduce… | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-2 | major | entrypoint_runs | logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json; docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:29… | §13.8 states the ReproLog 'covers the search-execution and remediation run'. The emitted log cannot cover the remediation run: its git_head is the pre-remediation registration commit and its phase names only the search execution. | ReproLog fields: "phase": "search-execution", "git_head": "27d74738aa35ec1cdf1ec6915b50532e3620ea6f". That commit is the registration commit (git log confirms subject 'do… | Emit a second ReproLog with phase 'remediation' at the follow-on provenance commit's HEAD and cite both, or narrow §13.8 to say the ReproLog covers the search-execution run only and that the remediation run's provenance is carried by the fo… | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-3 | major | seeds_pinned | docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1748-1756 (amendment A11 'Deliberately not changed'); mirrored at… | The empirical claim used to justify refusing the prescribed abstract tie-break conversion — presented as measured — does not reproduce from the archived pipeline. The refusal itself is correct, but on a ground the artifact does not state. | A11 asserts: 'This was verified: with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (X1 6,672 instead of 6,707)… | Strike the '6,672 instead of 6,707' sentence from A11 by append-only correction and replace the justification with the verifiable one: a set-based abstract tie-break re-introduces hash-seed dependence, which is what the amendment was fixing… | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-4 | major | data_hashed | docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1685-1705 (A11(a)); docs/literature/lit_review_kalshi-arbitrage_20… | The declared departure from the prescribed \bdex\b fix is justified by counts that do not reproduce, and the corpus-wide statistics quoted in the same paragraphs are computed under the pattern the script does NOT implement. | Claim: '\bdex\b alone … would have wrongly moved three genuine DeFi records out of X5 (Funding-Aware Optimal Market Making for Perpetual DEXs; Dynamic Function Market Mak… | Correct the departure justification to one record (the DEXs plural), and either restate the two corpus-wide statistics under the implemented patterns (284/305, 64/128) or label them explicitly as computed under the prescribed bare patterns. | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-5 | major | data_hashed | docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl:header.remediation.row_ids; ka-screening-script.py:245-24… | The prescribed migration key for the re-emitted verdicts file is null for 21% of rows, and the pre-remediation file it is meant to migrate from was overwritten in place and never archived, so neither the migration nor the '6,183 irreproducible row ids' measurement can be performed or checked by anyone. | 'Join on the identifier field, not on id.' Parsing the 8,813 data rows: 1,890 (21.4%) carry identifier == "" — all 244 X7 by construction, plus 1,554 X1, 85 X2, 5 X3, 2 X… | Publish a uid_old→uid_new crosswalk (or the pre-remediation file itself) alongside the re-emitted verdicts, and state that 1,890 rows have no persistent join key so the citation string is the only available fallback for them. | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-6 | major | data_hashed | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:967-976 (§7 regeneration note); docs/literature/search_logs/kalshi-arbit… | The round-1 registration-agency metadata sweep that authorises the 27 year, 78 venue and 2 tier corrections has no stored response artefact, breaking the artifact's own stated provenance rule for every other network step. | The review asserts '122 resolved at api.crossref.org, 26 at api.datacite.org … the store was checked against the registrant and found correct on every comparable field: 0… | Archive the 148 registrant responses as ka-store-registrant-sweep.json (DOI → agency, year, container-title, HTTP status) or downgrade the '0 disagreements' sentence to an unverified assertion of the remediation session. | — | reproducibility-verifier | retained → remediate |
| REPRODUCIBILITY-2-7 | major | llm_provenance | docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1303, 1315-1317, 1327-1328, 1346-1348 (addendum A3); duplicated at… | The QUANT-1-1 strike is incomplete in the governing document. The review body is clean, but the frozen protocol's own addendum — transcribed into the protocol under A12 on the same day A10 struck the claim — still asserts individual reading of forward-citation records in four places, with no supersession marker. | Surviving in the protocol addendum: the A3 heading '(… 3,300 of the 8,154 affected records had already been read individually)'; 'each such record is read and verdicted i… | Append an A3 supersession note inside the protocol addendum (strike-don't-delete) stating that every 'read individually' assertion in A3 is withdrawn by A10 and that no forward-citation record carries a read-based verdict; mirror it in ka-p… | — | reproducibility-verifier | retained → remediate |
| REV-2-9 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:766-772 | The PRISMA item-8 block reports the QUANT-1-1 reproduction against 'the published nine-code table' and then prints the pre-A11 counts (X5 159, X7 236, X11 643). Section 6 now publishes X5 94, X7 244, X11 700 as the record's table, so 'the published nine-code table' names two different tables in one artifact. The compli… | reproduces the published nine-code table **exactly** (`X1` 6,707, `X2` 338, `X3` 35, `X5` 159, `X7` 236, `X9` 1, `X10` 545, `X11` 643, `include` 149) | Insert 'as first published, pre-A11' before the count list here and in the identical sentence in amendment A10, and add one clause noting that the post-A11 table in section 6 differs on X5/X7/X11 by the word-boundary fix. | SAMPL (numerical consistency) | critical-reviewer | logged, not remediated |
| REV-2-10 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2990 vs :2996-3034 | The traceability section's header count disagrees with its own table. The table carries exactly two rows marked critical (QUANT-1-1, REV-1-2) and thirty-five marked major, totalling 37; the header says three critical and 34 major. The round-1 disposition record names two retained criticals, so the table is right and th… | **37 findings survived the round-1 adversarial refute gate (3 critical, 34 major); 4 were refuted and dropped.** | Correct the header to '2 critical, 35 major', or state that the third raw critical was among the four refuted and name it. | internal consistency | critical-reviewer | logged, not remediated |
| REV-2-11 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2758-2800 | Section 13.2 announces three statements and then makes four, with the fourth inserted out of order: the list runs 1, 2, 4, 3, and the item numbered 4 — the 98.3% classifier disclosure, which the same item calls 'the limitation that conditions all three above' — sits between items 2 and 3. The QUANT-1-1 traceability row… | Three statements, all unwelcome and all true. | Change 'Three statements' to 'Four statements' and reorder the list so the numbering is monotone, keeping the classifier item at the position its own text claims (first, or explicitly framed as conditioning the other three). | SAMPL (presentation); CHAMP item 22 | critical-reviewer | logged, not remediated |
| REV-2-12 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1177 vs :2028; :1078 vs :2415 | Two records carry different identifying metadata at two sites after the LITERATURE-1-1/1-2 sweep. (a) Peters, So & Ye is 'Peters (n.d.)' in the section-7 table but cited as 'Peters, So & Ye 2007' in 8.4.2, which breaks the stated year convention that section-8 citation years are re-derived from the store's `issued` fie… | \| petersNone978354077105 \| Peters (n.d.). Pari-Mutuel Markets: Mechanisms and Performance. Lecture Notes in Computer Science. \| 10.1007/978-3-540-77105-0_11 \| T1 \| G \| S4… | Backfill the Peters `issued` year from the registrant into the store and regenerate both the table cell and the 8.4.2 citation, or state at both sites that the store carries no year and drop 2007 from the citation; correct the Berg DOI in 8… | CHAMP item 18; FAIR F1 | critical-reviewer | logged, not remediated |
| REV-2-13 | minor | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2763-2765 and :2415-2429 vs :2255-2262, :2399 | The record states an absolute rule for metadata-depth records and then departs from it once without flagging the departure as an exception. Section 13.2 and the eleven 'metadata depth; no finding can be stated' rows of section 8.8 say such records are named without their findings being stated; 8.5.2 states Flepp's clai… | records at metadata depth are named without their findings being stated | Restate the rule as 'metadata-depth records are named, and no finding is stated beyond what the title itself asserts, which is flagged where it occurs', and carry the 'title only' flag onto the Flepp cell of the 8.7 disagreement table. | CHAMP item 24; SAMPL (interpretation discipline) | critical-reviewer | logged, not remediated |
| REV-2-14 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:856-868 vs :894 | The X5 false-fire evidence cannot be reconciled with the move count as printed. The three token classes are given as 51, 9 and 17 hits, summing to 77, against 65 records moved; the record does not say whether the counts are token hits or records, nor that a record may fire on more than one token. A reader auditing the… | `dex` inside *index* (51 hits among the affected records; 289 of the 305 works in the whole universe containing the string `dex` contain no word-boundary `dex` at all), `… | State the unit explicitly (token hits vs records) and give the record-level partition of the 65 — how many fired on dex only, amm only, defi only, and on more than one — so 51/9/17 and 65 reconcile on the page. | CHAMP item 23 (enough numerical detail to re-derive) | critical-reviewer | logged, not remediated |
| REV-2-15 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1761-1772, :76-114 | RQI dimension 2 (originality) is not addressed explicitly. The corpus contains four survey- or review-tier records covering large parts of the same literature (Ziemba 2023; Newall & Cortis 2021; Ottaviani & Sorensen 2008; Hausch, Lo & Ziemba 2008), and the record says only that they are used for framing and bibliograph… | *All four are used for their framing and their bibliography, not as primary evidence, per the protocol's treatment of survey-tier records.* | Add two or three sentences to section 1 stating what this record adds over the four survey-tier records it contains — at minimum the Kalshi-specific/generalized separation with a written carrying assumption per claim line, and the per-recor… | RQI dimension 2 (originality), van Rooyen et al. 1999, https://doi.org/10.1016/S0895-4356(99)00047-5 | critical-reviewer | logged, not remediated |
| SCOPE-2-6 | minor | partial | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2990 | The remediation traceability section misstates the round-1 disposition counts it exists to carry: it says 37 findings survived the gate as '3 critical, 34 major'. Two of the three raw criticals survived (REV-1-2, QUANT-1-1); the third, REV-1-1, was refuted and dropped — as the same section states six paragraphs later.… | Review 13.9: '37 findings survived the round-1 adversarial refute gate (3 critical, 34 major); 4 were refuted and dropped.' The trail sidecar docs/audits/audit_trail_kals… | Correct the sentence to '2 critical, 35 major' and state that the third raw critical (REV-1-1) was refuted, so the surviving-critical count and the table agree. | S-5 | scope-auditor | logged, not remediated |
| QUANT-2-10 | minor | reproducibility | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2975-2985 (section 13.8); logs/reproducibility/repro_log_8f5b02d3bf61492… | Section 13.8's two declared scope limits are honestly stated and are NOT used to excuse the gap — the record says plainly 'That is a contract breach, not a design choice'. But a third limit is undeclared and the prose overstates coverage in one respect: 13.8 says the ReproLog covers 'the search-execution and remediatio… | repro_log_8f5b02d3....json: {"phase": "search-execution", "git_head": "27d74738aa35ec1cdf1ec6915b50532e3620ea6f", "timestamp_utc": "2026-09-02T17:37:38Z", "dataset_checks… | Either emit a second ReproLog for the remediation run with phase='remediation' and the follow-on HEAD, or restate 13.8 as 'the ReproLog covers the search-execution run; the remediation run's ReproLog is emitted with the follow-on provenance… | CLAUDE.md §Reproducibility contract: 'Every artifact-producing run in this project emits a 13-field ReproLog a… | quant-auditor | logged, not remediated |
| QUANT-2-11 | minor | parameter | docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:80,83 | The `\bcrypto` pattern is prefix-anchored, not word-bounded, and its documented admitted-form list is not what the regex does. The adjacent comment declares 'crypto -- prefix-anchored: "crypto", "cryptocurrency", "cryptoeconomic", "crypto-asset"'. The pattern also matches cryptography, cryptographic, cryptology, crypta… | Corpus-wide check over the rebuilt 8,813-work universe: zero records whose ONLY DEFI hit is `crypto` match on a cryptograph*/cryptolog*/cryptanaly* form (the 4 X5 records… | Either tighten to `\bcrypto(currenc\|economic\|-?asset\|s?\b)` matching the declared list, or amend the comment to state that the prefix also admits cryptograph*/cryptolog*/cryptanaly* and record that this was checked to have zero effect on th… | docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:72-84 | quant-auditor | logged, not remediated |
| QUANT-2-12 | minor | numerical | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2830,2849 | The topical arm is given two different and both-incorrect sizes nineteen lines apart in the same subsection, and one of them is the denominator of the token-absence verification. Line 2830: 'The 35 topical queries'. Line 2849: 'none of the 45 fenced topical query blocks in section 3'. The record actually publishes 41 t… | Classification of the 86 fenced blocks in lit_review section 3 by query_id prefix: topical 41, known-item 23, forward-citation 18, supplementary/doc 4. Same tally from th… | Replace both figures with the audited counts: 41 topical query executions (33 distinct queries plus 8 retries), and restate the token-absence tests against '41 topical query blocks'. | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 2 provenance table and section 3 fences; com… | quant-auditor | logged, not remediated |
| QUANT-2-13 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1343,1479,1606 | The REV-1-10 qualifier was applied to the section-10 gap statements (G-2, G-4, G-5) but not to three same-form universal negatives left in section 8. Lines 1343 ('which no record in this corpus establishes for Kalshi'), 1479 ('which no record in this corpus verifies') and 1606 ('no record in the corpus reconciles them'… | lit_review:2521 (G-2): 'Qualified under finding REV-1-10, because the previous wording ("no record in the corpus") was a universal negative over 149 records of which 33 w… | Add the one-clause REV-1-10 qualifier ('among the 116 abstract-depth included records; the 33 metadata-depth, 545 X10, 700 X11 and 5,249 A3-rule records were not assessed') at each of the three sites, or scope them to 'no record read at abs… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 10, gaps G-2 and G-4 | quant-auditor | logged, not remediated |
| QUANT-2-14 | minor | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2815 (AG-10 row), 967-972 | AG-10's arithmetic and its literal statement both verify, but it is recorded as an unresolvable verification gap when the record is in fact verifiable by a method the artifact already uses elsewhere. 10.11179/ker.74.119 is registered with JaLC (Japan Link Center), which is neither Crossref nor DataCite as AG-10 correct… | https://doi.org/ra/10.11179/ker.74.119 -> [{"DOI":"10.11179/ker.74.119","RA":"JaLC"}]; api.crossref.org 404 and api.datacite.org 404 (AG-10 as stated is correct). GET htt… | Resolve the record against JaLC (or doi.org content negotiation), record the response alongside the sweep log, and either close AG-10 or downgrade it to 'verified at its registration agency JaLC rather than at Crossref/DataCite'. Update the… | DOI Proxy RA service https://doi.org/ra/{doi}; DOI content negotiation, https://citation.crosscite.org/docs.ht… | quant-auditor | logged, not remediated |
| LITERATURE-2-8 | minor | internal citation-year inconsistency; declared convention vi… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1005, 1125, 2082, 2568 | One DOI carries two different citation years inside the artifact, which is the exact defect the year sweep declared it had eliminated. | Convention at :1000-1004: 'this artifact carries the earlier consistently so that the table, the section-8 claim lines and the store cannot disagree', and 10.1007/s11579-… | Pick one and apply it at all three sites; re-run the '18 citation years re-derived' sweep over the other eleven records in the twelve-record list, since the sweep demonstrably missed this one. | — | literature-check | logged, not remediated |
| LITERATURE-2-9 | minor | missing citation for a declared reporting standard | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:7, 3052-3055 | Section 14 'Works cited by this record beyond the corpus' cites PRESS 2015 and PRISMA 2020 — the latter explicitly disclaimed by the record — but omits PRISMA-P 2015 and PRISMA-S, the two standards the frontmatter declares the record was written to and whose item numbers structure sections 2 and 5. | Frontmatter :7 'PRISMA-P 2015 (protocol) + PRISMA-S (adapted, non-clinical) for search reporting'; the record uses '<!-- prisma-s-1 -->' through '<!-- prisma-s-16 -->' as… | Add Moher D, Shamseer L, Clarke M, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015. Systematic Reviews. 2015;4(1). doi:10.1186/2046-4053-4-1; and Rethlefsen ML, Kirtley S, Waffenschmidt S,… | ~/.claude/CLAUDE.md Evidence Hierarchy tier 3 (professional standards must be cited at the point of claim) | literature-check | logged, not remediated |
| LITERATURE-2-10 | minor | incomplete citation / formatting defect in the human-readabl… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1097, 1177 | Two section-7 citation cells are malformed: a stray literal asterisk in an author field, and a citation published with no year where the registrant's own record supplies one indirectly. | (a) :1097 'Das * (2005). A learning market-maker in the Glosten–Milgrom model.' — stray '*' where the author surname belongs (Sanmay Das). (b) :1177 'Peters (n.d.). Pari-… | Strip the stray asterisk. For Peters, carry 2007 with a note that the registrant records no `issued` and the year is taken from the registrant's `created`/series volume, or keep n.d. and add that note — but do not publish a bare n.d. when t… | — | literature-check | logged, not remediated |
| REPRODUCIBILITY-2-8 | minor | cross_platform | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2849-2850, 2858-2861 (§13.4) | The restated vocabulary-gap claim cites a block count the protocol cannot supply, and contradicts the same section's own figure 20 lines earlier. | 'appears in none of the 45 fenced topical query blocks in section 3'. Parsing the protocol's fenced blocks: 42 total, of which 35 are topical query blocks (Crossref 15, O… | Change '45' to '35 fenced topical query blocks' at both sites. | — | reproducibility-verifier | logged, not remediated |
| REPRODUCIBILITY-2-9 | minor | cross_platform | docs/literature/search_logs/kalshi-arbitrage/ka-gate-verdict.json (83 occurrences of claim_location) | An artefact staged for commit embeds an absolute Windows path containing the OS account name, in the one file the remediation added to the search-log directory without applying the <WORKDIR> scrubbing used on every archived script. | All 83 findings carry "claim_location": "C:/Users/skoir/castles/docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md". ka-universe-script.py, ka-dedup-script.py, ka-… | Rewrite claim_location to the repo-relative path docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md before the provenance commit. | — | reproducibility-verifier | logged, not remediated |
| REPRODUCIBILITY-2-10 | minor | cross_platform | docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl; .gitattributes:14-18 | The primary machine-readable output is emitted with platform-native line endings and is not covered by the repository's eol=lf rules, so its bytes — and hence any digest taken over it — are platform-dependent. Same class as REPRODUCIBILITY-2-1. | ka-screening-verdicts.jsonl contains 8,814 CRLF terminators (io.open text mode on Windows); every other kalshi artefact is pure LF (review 3,055 LF / 0 CRLF; protocol 1,8… | Add '*.jsonl text eol=lf' to .gitattributes and open the output file with newline='\n' in ka-screening-script.py, so the verdicts file is byte-stable and hashable across platforms. | — | reproducibility-verifier | logged, not remediated |

## refute-gate

Every critical and major finding was put to an adversarial refuter at high
effort, with the standing rule that a drop requires concrete counter-evidence —
a counter-test, a source quote, or a logical disproof — and that bare
disagreement is not refutation ([arXiv 2604.19049](https://arxiv.org/abs/2604.19049)).
36 findings were gated; 3 were dropped and 33 retained. No finding was retained
as "conservative" (retained_conservative 0): every retained finding has a
refutation attempt on the record that failed on evidence. Each entry below
carries the claim **verbatim and unabridged**, the raiser, the refuter, the
enumerated evidence type, and — where the gate required reproduction — the
reproduction block lifted from the refutation evidence.

### REV-2-7 — dropped (refuted)

- **raised_by:** critical-reviewer (severity claimed: major; category: verification-gap)
- **refuted_by:** refuter, effort high
- **evidence_type:** `counter-test`
- **reproduction_required:** true
- **outcome:** dropped

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:751-753; docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl:2,5,64,201

> The verification route the record prescribes for the re-emitted verdicts file does not resolve the include set. The record instructs the reader to join on `identifier`, but the verdicts file's `identifier` is the merge-group representative, which for J6 twin sets is not the DOI the bibliography store retains. In the first 40 include rows alone, four identifiers are absent from the 149-entry store: 10.1145/1807342.1807402 (store retains 10.1145/2509413.2509414), 10.2139/ssrn.898597 (store retains 10.3386/w12200), 10.2139/ssrn.976809, 10.5555/3463952.3464011 (store retains 10.65109/bbzi6501). Row counts and code counts reconcile exactly (149 include rows; counts_by_rule sums to 8,813; n_read_based_verdicts 150, n_classifier_verdicts 8,663; X1 = R2 5,249 + R8 1,458 = 6,707), so the 150/8,663 split itself verifies at the aggregate level — but the record-level join that would let a reader confirm which 149 records carry the read-based verdict fails for roughly a tenth of them, and the record names no crosswalk.

*Evidence as filed (verbatim).*

> **Consequence for a reader holding the pre-remediation Table X-full:** `uid` values in the re-emitted file do not correspond to the old ones. **Join on the `identifier` field, never on `id`.**

*Fix as filed (verbatim).*

> State in section 5 and in the verdicts header that `identifier` is the merge-group representative and may differ from the store DOI where J6 retained a different version; report the number of include rows affected; and name ka-dedup-ledger.json as the crosswalk (or add a `store_doi` field to the 149 include rows so the join closes without one).

*Reference:* CHAMP item 23 (enough detail for re-analysis); PRISMA 2020 item 27

**reproduction**

````text
command:  Build the crosswalk from ka-dedup-ledger.json `included_twin_pairs` (24 entries of {uid, retained, twins[], title}) and re-run the join of the 149 include rows of ka-screening-verdicts.jsonl against the 149-entry CSL-JSON store.
observed: 0 include rows unresolved. The raw string join does miss 19/149 (5/149 after arXiv-form normalisation), including the four the finding names, but every one of them resolves through the ledger (U00001 10.1145/1807342.1807402 -> 10.1145/2509413.2509414; U00004 10.2139/ssrn.898597 -> 10.3386/w12200; plus U00063, U00200, U00854); the remaining 14 are `arXiv:N` vs `10.48550/arXiv.N` form only.
````

**Refutation evidence (verbatim).**

> Two limbs of the defect claim fail on direct test.
> 
> (1) "the record names no crosswalk" is false, and the named crosswalk closes the join completely. docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:700-706, in the same section 5 deduplication block, states: "J6 was applied to every included record carrying more than one DOI: the journal or registered version is retained and the working-paper, preprint or proceedings twin is recorded; 24 such twin sets are itemized in [ka-dedup-ledger.json](docs/literature/search_logs/kalshi-arbitrage/ka-dedup-ledger.json)." I built the crosswalk from that file's `included_twin_pairs` (24 entries, each {uid, retained, twins[], title}; the file's own j6_note reads "the retained identifier and the twins are itemized below for the included corpus") and re-ran the join of the 149 include rows against the 149-entry store: 0 include rows unresolved. All 5 non-arXiv mismatches resolve through the ledger (U00001 identifier 10.1145/1807342.1807402 -> retained 10.1145/2509413.2509414; U00004 10.2139/ssrn.898597 -> 10.3386/w12200; plus U00063, U00200, U00854), and the remaining 14 misses are purely `arXiv:N` vs `10.48550/arXiv.N` form. The ledger is keyed by the SAME post-A11 uids present in the re-emitted verdicts file, so it crosswalks on both uid and twin DOI.
> 
> (2) The "verification route the record prescribes" is misidentified. The sentence at lines 751-753 is scoped by its own lead-in: "**Consequence for a reader holding the pre-remediation Table X-full:** `uid` values in the re-emitted file do not correspond to the old ones. **Join on the `identifier` field, never on `id`.**" Per amendment A4 (line 2730), Table X-full IS ka-screening-verdicts.jsonl published as a machine-readable artifact. The prescribed join is therefore old verdicts file <-> re-emitted verdicts file, where `identifier` carries identical merge-group-representative semantics on both sides and closes 1:1. The record nowhere prescribes `identifier` as the join key to references_kalshi-arbitrage.json.
> 
> Reproduced but not decisive: the raw string join of include-row `identifier` against store DOI does miss 19/149 (5/149 after arXiv normalization), with exactly four in the first 40 include rows at the exact DOIs named (rows 1, 2, 13, 26: 10.1145/1807342.1807402, 10.2139/ssrn.898597, 10.2139/ssrn.976809, 10.5555/3463952.3464011), and the store does retain 10.1145/2509413.2509414, 10.3386/w12200, 10.65109/bbzi6501. Aggregates also reconcile as the finding states (counts_by_rule sums 8,813; 150/8,663; X1 6,707 = 5,249 + 1,458). But since the record names an artifact that resolves every one of those rows, the CHAMP-23 / PRISMA-27 re-analysis test is met; the residual is that the crosswalk is signposted 45 lines above the join sentence rather than beside it, which is an ergonomics point, not a verification gap.

### SCOPE-2-1 — dropped (refuted)

- **raised_by:** scope-auditor (severity claimed: major; category: partial)
- **refuted_by:** refuter, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** dropped

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2563-2571 (G-5); 2041-2154 (8.4.3); 2760-2779 (13.2)

> One of the five synthesis components the deliverable spec names for item 5 — 'inventory-risk market-making models and their applicability to bounded [0,1] payoffs' — is delivered as a declared non-answer rather than as synthesis. Four of the five named-lineage anchors sit at metadata depth with transfer status 'not addressed', the one readable anchor is excluded by its own Brownian-reference-price assumption, and the 700 X11 records are precisely the transfer-clause class that would answer the question and are UNDECIDED. The other four spec components (no-arbitrage/coherence S1, cross-venue discrepancy S2, longshot bias S3, frictions S5) are delivered; this one is not.

*Evidence as filed (verbatim).*

> G-5: 'Of the five named-lineage anchors, four are at metadata depth with transfer status `not addressed`, and the one whose model is stated in the retrieved text assumes a Brownian reference price, which is `explicitly excluded` for a bounded probability … The corpus cannot say whether the originals address bounded payoffs, because it did not read them. Nor can it say it for the lineage at large: 700 X11 records are transfer-clause records of exactly this class and none was assessed.' Frontmatter: 'NO FULL TEXT WAS READ FOR ANY INCLUDED RECORD (amendment A9).'

*Fix as filed (verbatim).*

> Either (a) retrieve and extract the five inventory-risk anchors (Ho & Stoll 1981, Avellaneda & Stoikov 2008, Glosten & Milgrom 1985, Kyle 1985, Guéant-Lehalle-Fernandez-Tapia 2012 — all canonical and retrievable) so the applicability component is answered from the sources rather than by transfer, or (b) amend the deliverable spec's item-5 wording, by dated append-only note, to require 'what the corpus at abstract depth can state about applicability', so the shipped artifact and the promise agree.

*Reference:* S-5

**reproduction**

````text
command:  Depth-label count over section 8.4.3 (lit_review:2041-2154) plus a read of the five named inventory-risk anchors and of spec item 5 (deliverable_spec:139-152).
observed: 11 abstract-depth records against 3-4 metadata-depth in 8.4.3; of the five anchors, three are metadata depth and two (Avellaneda & Stoikov 2008 at :2076-2082, GLFT at :2089) are read at abstract depth with transfer status determined; four affirmative applicability determinations are present, so the component is delivered as bounded synthesis rather than as a declared non-answer.
````

**Refutation evidence (verbatim).**

> Reproduced at the cited locations; two of the finding's three supporting propositions are false against the artifact, and the section it points at contains the synthesis it says is missing.
> 
> (1) "The one readable anchor is excluded by its own Brownian-reference-price assumption" is false. lit_review_kalshi-arbitrage_2026-09-02.md:2076-2082 records Avellaneda & Stoikov 2008 at ABSTRACT depth with an applicability determination made from the retrieved source text: "(doi:10.1080/14697680701381228, T1, abstract depth, abstract truncated by the publisher at the retrieved length). Transfer status: not addressed - the retrieved text states a securities-market setting and no bounded-payoff condition." Of the five anchors the finding's own fix names (Ho & Stoll, Avellaneda & Stoikov, Glosten & Milgrom, Kyle, GLFT), THREE are metadata depth (2045, 2053, 2069-2070) and TWO are read at abstract depth with transfer status determined (2080, 2089). "Four of the five ... at metadata depth" is not reproducible for that set. The fix itself asks to retrieve A&S 2008 and GLFT 2012 "so the applicability component is answered from the sources" - both were already retrieved and answered from the retrieved text.
> 
> (2) "Delivered as a declared non-answer rather than as synthesis" is false. Depth-label count over 8.4.3 (2041-2154): 11 abstract-depth records vs 3-4 metadata-depth. The section carries four affirmative applicability determinations, not zero: GLFT at 2089 "Transfer status: explicitly excluded by the stated model - a Brownian reference price is unbounded and cannot be a [0,1] probability that must terminate at an endpoint, so this model as stated does not apply to a binary event contract"; and the three betting-venue makers (Birge/Feng/Keskin/Schultz 2021, Makropoulou & Markellos 2011, Hodges/Lin/Liu 2013) at 2141 "Transfer status: `addressed` for the payoff support - these are state-contingent claims with endpoint settlement - but the mechanism is a bookmaker book, so E6 blocks the transfer to an order-driven exchange." That is precisely protocol objective O4 (protocol_kalshi-arbitrage-review_2026-09-02.md:133: "each model's stated payoff support, objective, and applicability conditions - and whether the source itself addresses bounded [0,1] payoffs with terminal settlement at an endpoint"), populated per record, plus 13 abstract-depth records whose model content is stated (Feys 2026 parameter-identity, Das 2005, Back & Baruch 2004, Tanaka 2005, Chakraborty & Kearns 2011, Manaster & Mann 1996, Antweiler 2014, Luckner & Weinhardt 2008).
> 
> (3) Spec text read at deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:139-152: item 5 requires "at minimum the no-arbitrage and coherence conditions ... longshot bias, inventory-risk market-making models and their applicability to bounded [0,1] payoffs, and cross-venue price-discrepancy evidence", with the spec's own check line being citation resolvability, Kalshi-vs-generalized separation, and zero unattributed factors - a coverage list, not a demand for a positive applicability result. Coverage is delivered: S4 is the largest strand (61 of 149, header at 1774) across 8.4.1 (Kalshi measurement, Bartlett & O'Hara adapting Kyle's lambda to the venue at 1803-1817), 8.4.2 (1846-1955, makers written natively for bounded [0,1] payoffs, applicability conditions stated per record), and 8.4.3. The artifact frontmatter objective (line 5) scopes the question as "the applicability conditions their own authors state", which the read records answer.
> 
> What survives is the residual-coverage bound (700 X11 undecided; three anchors unread), already disclosed at G-5 and 13.2 and covered by separate findings. That limits completeness; it does not establish that the item-5 component was shipped as a non-answer.

### LITERATURE-2-2 — dropped (refuted)

- **raised_by:** literature-check (severity claimed: major; category: unverifiable / fabricated count)
- **refuted_by:** refuter, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** dropped

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2849-2850

> 'the 45 fenced topical query blocks in section 3' is a count that does not exist in the protocol and contradicts the same document 19 lines earlier.

*Evidence as filed (verbatim).*

> Review :2849-2850 says 'none of the **45 fenced topical query blocks in section 3**'. Review :2830 says 'The **35 topical queries**'. Protocol A6 :1480 says 'the 35 frozen topical queries'. Actual fence count in the protocol: 41 blocks matching '```text ka-' — 35 topical in section 3.2 (15 Crossref :439-483, 6 OpenAlex :487-504, 6 arXiv :508-525, 4 Semantic Scholar :529-540, 2 NBER :544-549, 2 RePEc :553-558) plus 6 `ka-doc-*` S7 documentation queries at :683-700, which frozen protocol section 2.7 constraint 2 excludes from the literature stream and which are therefore not 'topical'. No denominator of 45 is derivable.

*Fix as filed (verbatim).*

> Replace 45 with 35 and state the derivation (section 3.2 fences only), or state 41 and name the 6 S7 doc fences separately. A count used as the denominator of a negative existence claim must be reproducible from the cited section.

*Reference:* none filed

**reproduction**

````text
command:  awk 'NR>=292 && NR<=602 && /^```text ka-/' docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md | sed 's/```text //' | grep -vE '^ka-(fc|ki)-' | wc -l
observed: 45 — 86 fenced blocks in the review's own section 3 less 18 forward-citation and 23 known-item fences, leaving exactly the topical set (15 Crossref, 6 OpenAlex, 6 arXiv, 4 Semantic Scholar + 8 verbatim -b/-c retries, 2 NBER, 2 RePEc + 2 -supp). The denominator is reproducible from the section the sentence names, and the negative existence claim over it also holds (grep -icE 'parimutuel|pari-mutuel|pari%20mutuel|pari mutuel' over 292-602 returns 0).
````

**Refutation evidence (verbatim).**

> The denominator 45 IS reproducible, and from exactly the section the sentence names. The finding assumed "section 3" refers to the protocol; the unqualified self-reference resolves to the review's own section 3, "## 3. Search strategies" (docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:292-602), which reproduces every query verbatim, "one fence per query_id" (:295-296).
> 
> Counter-count run over that range:
> - Total fenced blocks matching '^```text ka-' in lines 292-602: 86.
> - Minus forward-citation arm: 12 ka-fc-oa-* (a1..a6 plus a1-resolve..a6-resolve) and 6 ka-fc-s2-* = 18.
> - Minus known-item arm: 23 ka-ki-ki01..ki23.
> - Remainder = 45, and it is exactly the topical set: 15 ka-crossref-*, 6 ka-openalex-*, 6 ka-arxiv-*, 4 ka-s2-0{1..4} plus their 8 verbatim retry re-runs ka-s2-0N-b / ka-s2-0N-c, 2 ka-nber-*, 2 ka-repec-* plus 2 ka-repec-0N-supp. Command: awk 'NR>=292 && NR<=602 && /^```text ka-/' | sed 's/```text //' | grep -vE '^ka-(fc|ki)-' | wc -l  ->  45.
> 
> The finding's own alternative is also wrong for this section: the 6 ka-doc-* S7 fences are not in review section 3 at all — they are at :2462-2477, inside "## 9. S7 venue-structural stream — documentation tier, counted separately". So neither 41 nor "35 plus 6 doc" describes review section 3; 45 does.
> 
> No contradiction with :2830. "The 35 topical queries" counts distinct frozen queries (protocol 3.2, A6 :1480); "45 fenced topical query blocks" counts fences in section 3, which additionally carry the 8 -b/-c retry executions (frozen retry convention, protocol 3.1, amendment A1 :1235-1237) and the 2 -supp RePEc POST re-issues added by amendment A2 (:1274-1278). Different objects, both correct; the sentence says "blocks", not "queries".
> 
> The negative existence claim over that denominator also holds: grep -icE 'parimutuel|pari-mutuel|pari%20mutuel|pari mutuel' over lines 292-602 returns 0.

### REV-2-1 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: consistency)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1303,1317,1327,1346-1352; docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:107,121,131,150-156

> The QUANT-1-1 strike is INCOMPLETE, and amendment A12 propagated the unstruck text into the frozen protocol's own addendum. A10 strikes exactly three sentences, only one of which is A3's; four further A3 assertions of individual reading survive verbatim in both the amendment log and — new this round — inside the protocol document whose post-addendum digest 42bc6116… the record now publishes. A reader who verifies the protocol and reads its addendum is told 3,300 records were read individually and that every REVIEW-stratum record 'is read and verdicted individually by the LLM screener'; the deliverable says 150 of 8,813 carry a read-based verdict and that 'No individual reading is recoverable from any artefact in this repository.' The two documents of record now contradict each other on the fact a critical finding was raised about. The deliverable body itself is clean (grep for read/screened/assessed individually returns only the correction sentences at lines 679 and 2742).

*Evidence as filed (verbatim).*

> ### A3 — 2026-09-02 — mid-screening (declared before any record in the affected stratum received a verdict; 3,300 of the 8,154 affected records had already been read individually) — PRISMA-P items 11b, 12; PRISMA 2020 item 8

*Fix as filed (verbatim).*

> Append a numbered amendment (A13) that strikes the remaining four A3 assertions by quoted sentence — the heading parenthetical '3,300 … had already been read individually', 'each such record is read and verdicted individually by the LLM screener', 'Individual reading of 8,154 titles was begun and carried through 3,300 records', and 'The 3,300 forward-citation-only records already read individually retain their individual verdicts' — and add a one-line 'SUPERSEDED BY A10/A13 — see below' marker at the head of A3 in the protocol addendum. Re-record the protocol-with-addendum digest.

*Reference:* CHAMP item 6 (consistency with the pre-registered protocol); PRISMA 2020 item 8

**Refutation evidence (verbatim).**

> Refutation attempted and failed; the finding reproduces exactly. (1) Line-for-line reproduction: the four A3 assertions of individual reading survive verbatim at protocol_kalshi-arbitrage-review_2026-09-02.md:1303, 1317, 1327, 1347 and at ka-protocol-amendments.md:107, 121, 131, 151 — matching the cited locations. (2) A10 self-limits its strike: its text reads "Three specific statements are **struck**", item 1 being only A3's 659-record sentence; the other two struck items belong to the verdicts file and the corpus record, not A3. The four assertions are therefore unstruck by the amendment's own exhaustive enumeration. (3) Digest verified independently: sha256sum of the current protocol file returns 42bc6116ee554ee5cc80743d14d2f3d834f4feb389b53b5eaf2820c27322a762, identical to the protocol-with-addendum digest published at deliverable lines 2715 and 2738; head -c 82677 | sha256sum returns 99524df02696a59ab878173ce7f3636d9cd07067b5a801a677cdf5d126fa13f4, confirming the frozen-prefix claim. The published digest thus does cover a document containing the unstruck text. (4) Intra-document contradiction confirmed: the same protocol file contains both A3's "each such record is read and verdicted individually by the LLM screener" (1317) and A10's "No individual reading is recoverable from any artefact in this repository", while the deliverable states "records carrying a read-based verdict: 150 of 8,813 (1.7%)" (line 794) and "No record outside the 149 includes carries a verdict from a screener reading it" (line 42). (5) Two candidate defenses tested and both fail: (a) grep for supersede/SUPERSEDED/A10 in the protocol addendum region preceding and within A3 (lines 1190-1305) returns no supersession marker — the "Superseded in part by A10" note exists only in the deliverable's amendment table at line 2729, not in the protocol document of record; (b) A10's blanket sentence about unrecoverable reading does not function as a strike given A10's own three-item enumeration. (6) The finding's own qualifier is also correct: grep of the deliverable for "individually" returns only lines 2729, 2736, 2742 — all correction text — so the deliverable body is clean, as the auditor stated. No concrete counter-evidence exists.

### REV-2-2 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: reporting)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:62-68 vs :2998,:3006

> Two rows of the round-1 traceability table cite an edit site that does not exist. QUANT-1-1's fix row names '"Read this first" item 2' and REV-1-8's names '"Read this first" items 1-4'. The 'Read this first' block contains no numbered items, does not state that 98.3% of dispositions are classifier outputs, and does not name the 1,245 unresolved records — which was the substance of REV-1-8 ('"Read this first" named neither largest limitation'). The disclosure exists in the frontmatter, section 5, section 6, 13.2, 13.6 and G-10, so the substance is not lost, but the one front-of-document orientation block a downstream reader is told to read first still says only that this is not a systematic review, and the traceability record over-reports its own edits.

*Evidence as filed (verbatim).*

> **Read this first.** This artifact is a **compiled corpus record** produced by a **registered search**. It is **not a systematic review**, it reports **no inter-rater agreement statistic**, it reports **no certainty-of-evidence grade**, and the absence of a risk-of-bias table is a **declared design limit**, not an oversight (frozen protocol section 9.1).

*Fix as filed (verbatim).*

> Either add the numbered items 1-4 the traceability table claims (at minimum: 98.3% of dispositions are keyword-classifier outputs; 1,245 records ended screening unresolved; no full text was read; 33 of 149 are metadata-depth only), or correct the two 13.9 rows to name the sites that were actually edited. Do not leave the table asserting an edit that was not made.

*Reference:* SAMPL (reporting completeness); CHAMP item 17

**Refutation evidence (verbatim).**

> Refutation attempt failed; the finding reproduces exactly. (1) The "Read this first" block at docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:62-68 is a single unnumbered paragraph running from "**Read this first.** This artifact is a **compiled corpus record**..." to "...states no tradeable rule (ADR-0003)."; the next block is "**Provenance.**" at :70. `awk 'NR>=62 && NR<=75' | grep -E '^[0-9]+\.|item|98\.3|1,245|full text|metadata'` returns no match (exit 1), so the block contains no numbered items, no 98.3% classifier disclosure, no 1,245-record disclosure, no zero-full-text or metadata-depth statement. (2) The traceability rows at :2998 and :3006 nevertheless name '"Read this first" item 2' (QUANT-1-1) and '"Read this first" items 1-4' (REV-1-8) as fix sites. (3) A search for the "98.3" string shows the only numbered-item instance is at :2793, inside section 13.2 — a list whose items are 1, 2, 4, 3 (out-of-order numbering in the source) covering exactly the four disclosures the row claims for the front block: zero full text / 33 metadata-depth (item 1), 1,245 unresolved (item 2), 98.3% classifier (item 4), extraction-selection rule (item 3). That confirms the "items 1-4" were written into 13.2, not into "Read this first", and the QUANT-1-1 row separately and correctly cites "13.2 item 4" as a distinct site — so the "Read this first" citation in both rows is an additional, unmade edit. No counter-evidence found; the defect claim is true as stated.

### REV-2-3 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: consistency)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:575-577 vs :628-635, :2589-2595, :3010

> The REV-1-12 fix did not reach the claim it was supposed to withdraw. Section 4 states 'this record withdraws the offsetting claim rather than leaving it standing on queries that never ran', G-8 states 'In execution the narrowing is not offset', and the 13.9 row records the fix as 'the `prisma-s-9` offsetting claim withdrawn'. The prisma-s-9 paragraph is unedited and still asserts the offsetting conclusion, still resting it in part on ka-s2-02, one of the four Semantic Scholar queries that returned HTTP 429 and contributed zero records (AG-3). PRISMA-S item 9 is the site a reader checks for the date/language/subject-limit statement; it now says the opposite of section 4 and of section 10.

*Evidence as filed (verbatim).*

> the unrestricted forms of both phrases are carried by `ka-crossref-07`, `ka-crossref-11`, `ka-openalex-06` and `ka-s2-02`, so no vocabulary is category-gated out of the strategy as a whole.

*Fix as filed (verbatim).*

> Rewrite the closing clause of the prisma-s-9 paragraph in place: state that the offsetting forms were carried by ka-crossref-07, ka-crossref-11 and ka-openalex-06 as executed and by ka-s2-02 as planned, that ka-s2-02 returned zero (AG-3), and that the 'no vocabulary is category-gated' conclusion is therefore withdrawn as executed, cross-referencing section 4 and G-8.

*Reference:* PRISMA-S item 9; CHAMP item 19 (no selective reporting)

**Refutation evidence (verbatim).**

> Could not refute; the finding reproduces exactly at every cited location. (1) docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:562-577 — the full prisma-s-9 paragraph closes, unqualified, "the unrestricted forms of both phrases are carried by `ka-crossref-07`, `ka-crossref-11`, `ka-openalex-06` and `ka-s2-02`, so no vocabulary is category-gated out of the strategy as a whole." No "as planned"/"as designed" scope marker, no AG-3 mention, no cross-reference to section 4 or G-8, and no adjacent qualifying note — the paragraph runs uninterrupted from 562 to 577 and line 579 opens prisma-s-10. (2) :628-635 section 4 says "In execution, therefore, the narrowing is not offset, and this record withdraws the offsetting claim rather than leaving it standing on queries that never ran." (3) :2589-2595 G-8 says "In execution the narrowing is not offset (finding REV-1-12)." (4) :3010 the 13.9 row records the REV-1-12 fix as "...with the `prisma-s-9` offsetting claim withdrawn" — naming a site that is in fact unedited. Counter-test attempted on the finding's factual premise, to see whether ka-s2-02 actually returned records (which would relocate the error to section 4 rather than prisma-s-9): the section 2 table at :204-206 carries rows ka-s2-02, ka-s2-02-b and ka-s2-02-c, each with n_records = 0 and http_status = 429. ka-s2-02 contributed zero, so prisma-s-9 does rest its offsetting conclusion in part on a query that never executed, and the contradiction with sections 4 and 10 is real.

### REV-2-4 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: consistency)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2806 (AG-1 row) vs :2537-2546 (G-3)

> The REV-1-2 remediation raised the not-transferable-as-stated count from two to five and itemized all five in G-3, every one of them needing a fact blocked by AG-1 (S7-5). The AG-1 row in the access-gap table still reports the pre-remediation count of two and names only the two original sites. The access-gap table is the per-source register a reader uses to size the consequence of the blocked rulebook, so it now understates that consequence by three marks, including the two the record itself calls load-bearing (G-3 marks 3 and 4).

*Evidence as filed (verbatim).*

> Two generalized claims in section 8 are marked `not-transferable-as-stated` because of it (8.1.2 protocol-executable arbitrage; 8.2.2 bookmaker-plus-exchange arbitrage), and both J5 second-hand fee claims are unverifiable

*Fix as filed (verbatim).*

> Update the AG-1 'what could not be extracted as a result' cell to five marks and list the same five sites G-3 lists (8.1.2 Gebele; 8.2.2 Franck; 8.3.2 Thaler & Ziemba; 8.3.2 Levitt; 8.4.2 continuous-double-auction attribution), or replace the enumeration with a pointer to the G-3 table so the count cannot drift again.

*Reference:* CHAMP item 18; internal consistency

**Refutation evidence (verbatim).**

> Attempted refutation failed; the defect reproduces exactly as stated.
> 
> 1. AG-1 cell verbatim at docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2806: "The entire S7 fee, settlement, position-limit, membership and market-maker record (S7-5). Two generalized claims in section 8 are marked `not-transferable-as-stated` because of it (8.1.2 protocol-executable arbitrage; 8.2.2 bookmaker-plus-exchange arbitrage), and both J5 second-hand fee claims are unverifiable" — still two marks, still the two original sites.
> 
> 2. G-3 at :2536-2546 states "**The count is now five, not two** (findings REV-1-2, REV-1-3, QUANT-1-5, LITERATURE-1-4)" and tabulates five rows; rows 3, 4 and 5 (Thaler & Ziemba 8.3.2; Levitt 8.3.2; continuous-double-auction attribution 8.4.2) each name "(S7-5)" as the unretrieved fact — the identical S7-5 record AG-1's own cell names as what it blocked. So the added three are caused by AG-1, not by some other gap; no alternative-attribution defence exists.
> 
> 3. Independently verified all five marks exist in section 8: :1325 (8.1.2, cites AG-1 by name), :1492 (8.2.2), :1672 (8.3.2 Thaler/Ziemba, "counted in gap G-3"), :1711 (8.3.2 Levitt, "did not retrieve (AG-1) ... counted in gap G-3"), :2021 (8.4.2 microstructure, "counted in gap G-3").
> 
> 4. The document's own findings register at :2999 confirms the supersession: REV-1-2 remediation is recorded as "G-3 count raised from two to five". The "two" surviving at :2806 is precisely the superseded number.
> 
> 5. No compensating text elsewhere: grep for AG-1 (lines 235, 1323, 1374, 1519, 1711, 1824, 2176, 2209, 2399, 2456, 2614, 2806) shows no other place restating the count; the S7-5 row at :2489 uses an uncounted universal ("Every place in section 8 ... is marked not-transferable-as-stated"), which does not correct AG-1's explicit enumeration.
> 
> Load-bearing element of the claim also confirmed: G-3 marks 3 and 4 are the two the record itself calls load-bearing (:2548-2553), and both are absent from AG-1's cell.

### REV-2-5 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: consistency)
- **refuted_by:** refuter, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2412-2434 (section 8.8)

> Section 8.8, created by this remediation, mis-describes its own 16-row table three times. The table has 9 metadata-depth rows (Berg, Cao, Koch, Restocchi, Sestovic x2, Sethi, Swanson, Zhou) and 7 abstract-depth rows (Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung). The prose says eleven are metadata depth, says five are abstract depth, and then names six. The distinction is not cosmetic: the abstract-depth rows are the ones the record itself classes as 'a synthesis omission, not a depth limit', so the count of unexcused omissions is understated by two, and Oliven & Rietz — a forward-citation anchor read at abstract depth — is silently moved out of that class.

*Evidence as filed (verbatim).*

> **Eleven of the sixteen are at metadata depth**, where naming without stating is the only honest disposition. **Five are at abstract depth and simply were not carried** — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung — and that is a synthesis omission, not a depth limit.

*Fix as filed (verbatim).*

> Restate as nine metadata-depth and seven abstract-depth, and list all seven abstract-depth records (adding Oliven & Rietz) as unexcused synthesis omissions; regenerate the counts mechanically from the table's own depth column rather than by hand.

*Reference:* SAMPL (numerical consistency); CHAMP item 22

**reproduction**

````text
command:  sed -n '2414,2432p' docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md | awk -F'|' 'NF>5 {gsub(/ /,"",$6); print $6}' | sort | uniq -c
observed: 7 abs, 9 meta over the 16 data rows (abs = Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung; meta = Berg, Cao, Koch, Restocchi, Sestovic x2, Sethi, Swanson, Zhou), against prose that says eleven metadata-depth, says five abstract-depth, and then names six.
````

**Refutation evidence (verbatim).**

> Finding fully reproduced; not refuted. Mechanical count of the depth column in section 8.8's table (docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md, header at line 2414, 16 data rows at lines 2416-2431) via `sed -n '2414,2432p' ... | awk -F'|' 'NF>5 {gsub(/ /,"",$6); print $6}' | sort | uniq -c` returns exactly: 7 abs, 9 meta. Metadata-depth rows: Berg et al. 2008, Cao 2026, Koch 2007, Restocchi et al. 2019, Sestovic 2017 (10.2139/ssrn.3044673), Sestovic 2017 (10.2139/ssrn.3035848), Sethi 2015, Swanson 2026, Zhou 2007 = 9. Abstract-depth rows: Bakalo 2026, Dalen 2026, Donatoni 2022, Marek 2019, Oliven & Rietz 2004, Portnaya 2026, Sung 2009 = 7. The prose immediately following (lines 2433-2436) reads verbatim: "**Eleven of the sixteen are at metadata depth**, where naming without stating is the only honest disposition. **Five are at abstract depth and simply were not carried** — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung — and that is a synthesis omission, not a depth limit." Three independent errors confirmed: (1) "Eleven" vs. actual 9; (2) "Five" vs. actual 7; (3) the stated count "Five" contradicts its own enumeration of six names. The Oliven & Rietz claim is also confirmed: its table row reads "| Oliven & Rietz 2004 `10.1287/mnsc.1040.0191` | T1 | G | S1+S6 | abs | forward-citation anchor A1; named as an anchor in section 13.4 but carries no claim line |" — depth abs, yet absent from the enumerated abstract-depth omission list, so it is silently excluded from the class the record itself calls "a synthesis omission, not a depth limit". No counter-evidence found.

### REV-2-6 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: consistency)
- **refuted_by:** refuter, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:248-250, :2598-2600, :2814, :2733

> The SSRN recall-gap consequence is understated against the record's own section-7 table. Counting rows carrying both an E4/E15 value of K and a 10.2139/ssrn.* identifier gives 15 of the 19 Kalshi-specific records, not 13. The number 13 is repeated at four sites (prisma-s-4, G-9, AG-10 row's neighbour AG-9, amendment A7). The 31-of-149 figure checks out (31 SSRN rows in the table) and the 19 Kalshi rows check out, so the error is confined to the intersection — and it understates a limitation in exactly the direction the record elsewhere calls 'a reporting defect in the direction that flatters the corpus'.

*Evidence as filed (verbatim).*

> **31 of the 149 included records carry `10.2139/ssrn.*` DOIs, and 13 of the 19 Kalshi-specific records do**

*Fix as filed (verbatim).*

> Recount the intersection mechanically from the section-7 table and change 13 to 15 at all four sites (prisma-s-4, G-9, AG-9, amendment A7); state the derivation so the number is re-checkable.

*Reference:* CHAMP item 18; SAMPL (numerical consistency)

**reproduction**

````text
command:  Mechanical parse of the 149 data rows of the section-7 table (header at lit_review:1063) on the pipe delimiter; count E4/E15 values, count identifiers matching ^10\.2139/ssrn\., and intersect the two.
observed: E4/E15 distribution G 69 / K 19 / N 61 (sums to 149); 31 rows carry an SSRN DOI; the K-and-SSRN intersection is 15, not the published 13 — the fifteen being bartlett2026ssrn6615739, brgi2025ssrn5502658, greene2026ssrn6442939, gupta2026ssrn6858200, krause2026ssrn7117919, krause2026ssrn7119120, krause2026ssrn7021660, krause2026ssrn7110758, krause2026ssrn7087538, lee2026ssrn6748186, lee2026ssrn6964226, lim2026ssrn6704139, moulinier2026ssrn7170178, polson2026ssrn7254820, yurchyna2026ssrn7364100.
````

**Refutation evidence (verbatim).**

> Attempted refutation failed; the finding reproduces exactly. Mechanically parsed the 149 data rows of the section-7 included-corpus table (header at docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1063), splitting on the pipe delimiter — every row carries exactly the 8 declared columns, so column 5 is E4/E15 and column 3 is the persistent id. Counts: E4/E15 distribution G 69 / K 19 / N 61 (sums to 149, so the 19-record Kalshi denominator is correct); rows with a persistent id matching ^10\.2139/ssrn\. = 31 (so the 31-of-149 figure is correct, and the CSL-JSON store at docs/literature/references_kalshi-arbitrage.json independently holds 149 entries of which 31 carry an SSRN identifier); intersection of E4/E15=K with an SSRN DOI = 15, not 13. The 15 rows are bartlett2026ssrn6615739, brgi2025ssrn5502658, greene2026ssrn6442939, gupta2026ssrn6858200, krause2026ssrn7117919, krause2026ssrn7119120, krause2026ssrn7021660, krause2026ssrn7110758, krause2026ssrn7087538, lee2026ssrn6748186, lee2026ssrn6964226, lim2026ssrn6704139, moulinier2026ssrn7170178, polson2026ssrn7254820, yurchyna2026ssrn7364100. The erroneous 13 is present at all four claimed sites: line 249 (prisma-s-4 narrative), the G-9 bullet in section 10, the A7 amendment row (line 2733), and the AG-9 access-gap row (line 2814). No alternative reading rescues 13: the artifact's own column legend defines K as "the record's own data or institutional object is KalshiEX LLC" and section 7 is the only source of the 19 denominator; the CSL-JSON store carries no E4/E15 field and so supplies no competing intersection. The error is confined to the intersection and understates the SSRN dependency by two records.

### REV-2-8 — retained

- **raised_by:** critical-reviewer (severity claimed: major; category: interpretation)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2141-2143

> A residual venue-mechanism presupposition survives the REV-1-2 fix, and it decides a transfer. The bookmaker market-making entry in 8.4.3 states unconditionally that E6 blocks the transfer 'to an order-driven exchange'. The destination of every transfer in this corpus is the venue of interest, whose mechanism the record now says it cannot establish (S7-5 Not established, AG-1); and the determination flips on that unknown — if the venue is quote-driven, as the Burgi record characterises it at 8.4.1, E6 would license rather than block the transfer. This site is not among the five marks G-3 itemizes, so a blocked-transfer conclusion is being asserted on the same unretrieved fact that five other transfers are correctly marked `not-transferable-as-stated` for.

*Evidence as filed (verbatim).*

> *Transfer status: `addressed` for the payoff support — these are state-contingent claims with endpoint settlement — but the mechanism is a bookmaker book, so E6 blocks the transfer to an order-driven exchange.*

*Fix as filed (verbatim).*

> Rewrite the clause conditionally — 'E6 blocks the transfer to any order-driven venue; whether the venue of interest is one is not established (S7-5, AG-1)' — and either add the site to the G-3 table as a sixth mark or state why it is not one.

*Reference:* CHAMP item 30 (conclusions limited to what the analysis supports); CHAMP item 27

**Refutation evidence (verbatim).**

> No refutation available; the finding reproduces exactly. (1) Line 2143 of docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md reads verbatim "but the mechanism is a bookmaker book, so E6 blocks the transfer to an order-driven exchange" with no conditional and no AG-1/S7-5 citation. (2) Section 8 preamble item 4 (line ~1229) fixes the transfer destination as the venue of interest and mandates the `not-transferable-as-stated` mark whenever the E6 carrying assumption cannot be written out. (3) The venue's mechanism is on record as unestablished at S7-5 (line 2489), 8.4.1 (line ~1824, "This corpus does not know Kalshi's trading mechanism"), and section 12 (line 2399). (4) The G-3 table (lines 2542-2546) itemizes exactly five marks at 8.1.2, 8.2.2, 8.3.2, 8.3.2, 8.4.2 — none at 8.4.3 — and REV-1-2's remediation row (line 2999) names only 8.3.2 and 8.4.1 as sites touched, so this site was not swept. (5) The document's own precedent refutes any "a block is the safe default" defence: G-3 mark 4 is itself a block ("Levitt bookmaker-versus-exchange block", needing "Kalshi's trading mechanism, E6 (S7-5)"), and the withdrawn 8.3.2 wording ("Kalshi is an order-driven exchange ... so the supply-side channel as stated does not transfer") is structurally the same sentence still standing at 2143. The only defect I found in the finding is its flip clause: E6's category list (line 826) distinguishes `bookmaker fixed-odds book` from other quote-driven forms (AMM, dealer), so a quote-driven venue would not automatically license the transfer — a quibble about the counterfactual's strength, not about the defect, since the asserted block still rests wholly on the unretrieved E6.

### SCOPE-2-2 — retained

- **raised_by:** scope-auditor (severity claimed: major; category: spec-conflict)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:125-138 (Thread C, search-logs + store item)

> The canonical spec's ticked PASSED check for the search-logs/store item records verification evidence that the post-remediation artifact contradicts on four numbers, and the spec was not updated when the remediation moved them. A reader taking the spec as the acceptance record gets a completeness picture the delivery no longer supports.

*Evidence as filed (verbatim).*

> Spec: 'all 86 protocol query rows executed, with the five deviations recorded as numbered append-only amendments A1-A5' and 'amendment A5's disposition code X11 leaves 643 records with eligibility UNDECIDED … so 1,188 records reached the end of screening unresolved' and '149 files in the log directory'. Delivery: twelve amendments A1-A12 (review 13.1); A6 'the protocol's ka-bc-{n} backward citation-chasing arm was not executed', A7 'the SSRN supplementary site-search arm was not run'; X11 = 700 and capacity dispositions = 1,245 (review section 5 split table, frontmatter n_eligibility_undecided: 700, n_capacity_disposition: 1245); the log directory now holds 150 files.

*Fix as filed (verbatim).*

> Append a dated correction note under that spec item restating the check as executed-after-remediation: twelve amendments, two protocol arms unexecuted (A6, A7) with G-7/G-9 as their recall consequence, 700/545/1,245 as the unresolved split, and the current file count. Do not edit the original tick text; supersede it in place as the spec already does for Thread B.

*Reference:* S-4

**Refutation evidence (verbatim).**

> Refutation attempted on four independent axes; every one confirmed the finding instead.
> 
> (1) Location reproduces verbatim. docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md lines 125-138 are the ticked "[x] docs/literature/search_logs/kalshi-arbitrage/ + references_kalshi-arbitrage.json" item, whose check line 131-138 reads exactly as quoted: "149 files in the log directory; all 86 protocol query rows executed, with the five deviations recorded as numbered append-only amendments A1-A5" and "X11 leaves 643 records with eligibility UNDECIDED and A4's X10 leaves 545 ... so 1,188 records reached the end of screening unresolved".
> 
> (2) Amendment count: `grep -oE 'A1[0-2]|A[1-9]' docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md | sort -u` yields A1-A12 (twelve). Review frontmatter line 29 states "Twelve numbered append-only amendments, all enumerated in section 13.1", and enumerates A6 ("backward citation-chasing arm ka-bc-{n} not executed") and A7 ("SSRN supplementary site-search arm not run; gap AG-9"). Spec's "five deviations ... A1-A5" is contradicted, and A6/A7 additionally contradict the spec's "all 86 protocol query rows executed".
> 
> (3) X11 / unresolved split: review frontmatter n_eligibility_undecided: 700 (line 39), n_capacity_disposition: 1245 (line 37); section-5 split table lines 658-659 give X10=545, X11=700; line 852 states "Was 643 before A11" and line 889 shows the A11 delta table row "X11 | 643 | 700 | +57". Spec's 643 and 1,188 are both superseded (545+700=1,245).
> 
> (4) File count: `ls docs/literature/search_logs/kalshi-arbitrage/ | wc -l` returns 150, not the spec's 149. (The store itself still parses as a 149-entry JSON list, so only the directory count moved — but that is the number the spec asserts.)
> 
> (5) No superseding note exists. Grep of the whole spec for correction/supersede/amend returns only line 60, which supersedes the Thread B description, not this Thread C item; the spec's last touch is commit 3cdbfe3 (the session declaration), i.e. it was never updated after remediation. The defect claim stands as stated.

### SCOPE-2-3 — retained

- **raised_by:** scope-auditor (severity claimed: major; category: omitted)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* spec (Thread C item 6) — docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md

> The spec-declared branch agenda does not exist anywhere in the repository, although the corpus record's section 10 gaps (G-1…G-10) and section 11 TO COMPUTE handoffs were written as its input and ADR-0004 delimits the prediction-market branch to include that path. The spec box is unchecked, so the absence is declared rather than concealed, but the branch deliverable set is incomplete and the artifact under audit is the only place its content currently lives (as gaps, not as falsifiable branches).

*Evidence as filed (verbatim).*

> Glob of docs/research_notes/ returns only research_agenda_context-portability_2026-08-21.md, research_agenda_architecture_2026-08-21.md, research_agenda_regime-classification_2026-08-21.md. ADR-0004 §Decision delimits the branch as including 'docs/research_notes/research_agenda_prediction-market-microstructure_*'. Spec item state: 'numbered research branches derived from the gaps the corpus exposes, each with a falsification test that is a genuine branch-level test … and each with its evidence tier.'

*Fix as filed (verbatim).*

> Write the agenda against G-1…G-10 and TC-1…TC-5 with one genuine branch-level falsification test each, or, if it is being deferred to a successor session, record the deferral as a dated spec note naming the successor so the absence is a decision rather than an open box.

*Reference:* S-6

**Refutation evidence (verbatim).**

> Refutation attempted on four fronts; all four confirmed the finding rather than disproving it.
> 
> (1) File absence — reproduced. `ls docs/research_notes/` returns exactly four entries: .gitkeep, research_agenda_architecture_2026-08-21.md, research_agenda_context-portability_2026-08-21.md, research_agenda_regime-classification_2026-08-21.md. No prediction-market agenda. Repo-wide `grep -rn "research_agenda_prediction-market"` returns only *references* to the path (ADR-0004:42, spec:154, protocol_kalshi-arbitrage-review:22, and two audit-trail entries), never a file. `find . -iname "*prediction*market*" -not -path "./.git/*"` returns only ADR-0004 itself. `git status --porcelain` shows no untracked or staged file at that path, so it is not merely uncommitted.
> 
> (2) Content-elsewhere hypothesis — tested and failed. If the branch agenda's content lived under some other filename, the finding's "does not exist anywhere in the repository" would be wrong. `grep -rln "falsification test" --include=*.md docs/ research/ reports/` returns six files, none of them a prediction-market branch agenda (charter, two deliverable specs, ADR-0003, the regime-classification lit review, and a 2026-08-21 audit trail). No candidate carrier exists.
> 
> (3) Deferral-note hypothesis — tested and failed. This was the strongest available refutation: if a dated deferral naming a successor already existed, the "open box" characterization would be false. Spec line 154 is verbatim `- [ ] docs/research_notes/research_agenda_prediction-market-microstructure_2026-09-02.md`, an unchecked in-scope Thread C deliverable whose `state:` text matches the finding's quotation exactly ("numbered research branches derived from the gaps the corpus exposes, each with a falsification test that is a genuine branch-level test … and each with its evidence tier"). `grep -i "defer|successor session|out of scope for this session"` over the spec returns a single hit, line 9, and that declaration scopes out different things — dual-screened PRISMA review, empirical microstructure analysis, Kalshi API acquisition, backtest/trading rule — and does not name the agenda. The spec's "Self-executed" section (lines ~266-282) likewise does not cover it. So no deferral exists.
> 
> (4) Premise checks — both hold. ADR-0004 §Decision (lines 39-43) does delimit the branch as including `docs/research_notes/research_agenda_prediction-market-microstructure_*`. The corpus record's declared inputs exist as claimed: lit_review_kalshi-arbitrage_2026-09-02.md §10 "Gaps the corpus exposes" runs G-1 (line 2506) through G-10 (line 2601), and §11 "`TO COMPUTE` handoffs" (line 2607) runs TC-1 through TC-5 (lines 2614-2618).
> 
> One nuance found, which does not refute: round 1 already logged this same absence as SCOPE-1-11 at *minor*/documented-drift (audit_trail_kalshi-arbitrage-review_2026-09-02.md:167), disposition "logged, not remediated," where SCOPE-2-3 states it at *major*/omitted. That is a severity re-grading between rounds, not a factual contradiction — and severity quibbles are not refutation. The defect claim itself is true on every element.

### SCOPE-2-4 — retained

- **raised_by:** scope-auditor (severity claimed: major; category: partial)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md:11 vs spec Thread D (docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:164-170)

> The audit trail shipped for this branch is delivered under a path no spec item names, and it covers only Thread C. The spec's Thread D item declares a single trail at docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md covering 'this session's audit round(s) over Threads B and C'. No trail covering Thread B exists, and the round-2 trail for this branch will inherit the same unnamed path unless the spec is reconciled.

*Evidence as filed (verbatim).*

> Spec Thread D: '`docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` … WI-3 §2 trail for this session's audit round(s) over Threads B and C'. Shipped: docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md, title 'Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 1', artifacts list containing only the four Thread C files.

*Fix as filed (verbatim).*

> Either rename/extend the Thread D spec item to name the per-branch trail slug actually in use (audit_trail_kalshi-arbitrage-review_*) and add an explicit statement that Thread B carried no audit round because it was discharged pre-session, or write the spec-named session trail that covers both threads. One or the other, recorded.

*Reference:* S-7

**Refutation evidence (verbatim).**

> Attempted refutation failed; every element of the finding reproduced.
> 
> 1. Spec item exists as quoted. docs/deliverables/deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md:164-170 (Thread D — session close) reads: "- [ ] `docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` / - state: WI-3 §2 trail for this session's audit round(s) over Threads B and C; 22 front-matter keys; 7 body sections; refute-gate dispositions verbatim for every gated finding; attested."
> 
> 2. That file does not exist. `ls docs/audits/audit_trail_open-items-kalshi-arbitrage_2026-09-02.md` -> "No such file or directory". A full listing of docs/audits/ shows no file with that slug; the only 2026-09-02 trail is audit_trail_kalshi-arbitrage-review_2026-09-02.{md,json}.
> 
> 3. The shipped trail's path is named by no spec item. `grep -rn "audit_trail_open-items-kalshi\|audit_trail_kalshi-arbitrage-review" docs/` returns exactly four hits: three self-references inside the shipped trail (lines 50, 83, 1461) and spec line 164 naming the OTHER path. Grepping the spec for the slug "kalshi-arbitrage-review" returns only lines 100 and 201, both of which name docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md — a protocol, not a trail. So no spec item names the shipped trail path.
> 
> 4. The shipped trail covers Thread C only. Line 11 title: "Audit trail — Thread C Kalshi / binary-event-market arbitrage branch, round 1"; body H1 at line 53 is identical; line 57: "Thread C. Audited artifacts: the Kalshi / binary-event-market arbitrage corpus". The `artifacts:` front-matter block lists exactly the four Thread C files (lit_review_kalshi-arbitrage, references_kalshi-arbitrage.json, ADR-0004, protocol_kalshi-arbitrage-review). audit_criteria.task_spec_verbatim is scoped verbatim to "Thread C — Kalshi / binary-event-market arbitrage branch", and `routing:` scopes scope-auditor to "deliverable_spec_open-items-kalshi-arbitrage_2026-09-02.md Thread C".
> 
> 5. No Thread B coverage anywhere in it. Case-insensitive `grep -in "thread b"` over the shipped trail returns zero hits.
> 
> Candidate refutations checked and each failed:
> - A Thread B trail elsewhere in this session: docs/audits/session_trail_2026-09-02.md is a hook-generated session-start log (lines of the form "timestamp | session=... | reason=other | cwd=... | git=..."), not a WI-3 trail; `grep -in "thread b\|thread c\|audit_trail"` over it returns zero hits. docs/audits/audit_trail_round3-remediation_2026-08-21.md is a prior-session (2026-08-21) trail, not "this session's audit round(s)" the Thread D item requires.
> - A recorded deviation legitimizing the alternate slug: the spec's "# Recorded deviations" section contains a single entry, about round-1 remediation of Thread A being delegated rather than self-executed. Nothing about trail naming. The shipped trail contains no reconciliation note either (no occurrence of "open-items-kalshi" in it).
> - The spec's Delegation block (lines ~236-244) says the loop's output is "the two audit trail files under `docs/audits/`", which maps to the two spec-named trails (Thread A: audit_trail_phase2-explosive-review_2026-08-24.md at spec:40; Thread D: audit_trail_open-items-kalshi-arbitrage_2026-09-02.md at spec:164) — it does not name or license the shipped slug, so it does not close the gap.
> 
> The defect claim is true as stated.

### SCOPE-2-5 — retained

- **raised_by:** scope-auditor (severity claimed: major; category: partial)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:107,121,131-132,147,150-153; mirrored via A12 at docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1303,1317,1327,1343,1346-1352

> The A10 strike of the individual-reading claims is incomplete. A10 strikes exactly three named sentences (A3's '659 … every one of them was read individually', the verdicts-file 'encodes that reading' claim, and the corpus record's section-5 'All 8,813 were screened at title level'). It does not strike A3's four other assertions that 3,300 forward-citation records and the whole REVIEW stratum were read individually. Because A12 appended A1-A12 verbatim into the frozen protocol's append-only addendum, the protocol of record now asserts individual reading of 3,300 records while A10, twelve pages later, states that 8,663 of 8,813 verdicts are classifier outputs and 'no individual reading is recoverable from any artefact in this repository'. The review body itself is clean; the provenance record is not.

*Evidence as filed (verbatim).*

> ka-protocol-amendments.md:107 'A3 … 3,300 of the 8,154 affected records had already been read individually'; :121 'each such record is read and verdicted individually by the LLM screener'; :131 'Individual reading of 8,154 titles was begun and carried through 3,300 records'; :150-152 'The 3,300 forward-citation-only records already read individually retain their individual verdicts'. Against A10 at :440-459: 'every disposition except the 149 includes and one hand-verified J6 same-work twin is a rule output … the total is 8,663 classifier verdicts against 150 read-based ones'.

*Fix as filed (verbatim).*

> Extend A10 (or issue A13, append-only) with an explicit strike list naming those four A3 statements by quotation, and re-append the corrected amendment text to the protocol addendum, recomputing and republishing the protocol-with-addendum digest (the frozen 82,677-byte prefix is unaffected).

*Reference:* S-5

**Refutation evidence (verbatim).**

> Refutation failed; the finding reproduces exactly. (1) Every quoted line verifies verbatim: ka-protocol-amendments.md:107 ("3,300 of the 8,154 affected records had already been read individually"), :121 ("such record is read and verdicted individually by the LLM screener"), :131 ("Individual reading of 8,154 titles was begun and carried through 3,300"), :150-152 ("The 3,300 forward-citation-only records already read individually retain their individual verdicts"), and A10's :450 ("individual reading is recoverable from any artefact in this repository") / "8,663 classifier verdicts against 150 read-based ones". (2) The A10 strike list at ka-protocol-amendments.md:419-428 contains exactly three enumerated items (A3's 659-record sentence, the verdicts-file "encodes that reading" claim, the corpus record's section-5 sentence); none is an A3 3,300-record statement. (3) The A12 mirror is verbatim: protocol_kalshi-arbitrage-review_2026-09-02.md:1303, 1317, 1327, 1343, 1346-1352 carry the uncorrected A3 text, and the same file carries A10's contradicting statements at :1646 and :1655, so both sides of the contradiction sit inside the single protocol of record. (4) No later amendment repairs it: A11 is confined to \b-anchoring four DEFI tokens and PYTHONHASHSEED determinism, A12 to the append mechanism; grep for "3,300" returns only the three uncorrected A3 hits in each of the two provenance documents and zero in the review. (5) Counter-test on whether both claims can hold: A10 partitions the 8,154 forward-citation-only stratum as 5,249 DEFAULT-X1 + 2,905 REVIEW (5,249+2,905=8,154 exactly) and declares both classifier-produced, leaving only 150 read-based dispositions corpus-wide; A3's 3,300 come from that same stratum, so the two are arithmetically irreconcilable. Only partial mitigation exists and it does not reach the cited locations: A10's prose withdraws the REVIEW-stratum half in substance ("3,414 dispositions were presented as individual screening verdicts and were not - the 2,905-record REVIEW stratum plus the 659"), and lit_review_kalshi-arbitrage_2026-09-02.md:2729 annotates A3 "Superseded in part by A10", but that annotation lives only in the review body the finding already concedes is clean, and nothing anywhere addresses the "3,300 ... retain their individual verdicts" sentence. The asymmetry stands: A10 struck A3's 659-record sentence by name while leaving the structurally identical 3,300-record sentences unstruck in the frozen addendum.

### QUANT-2-1 — retained

- **raised_by:** quant-auditor (severity claimed: critical; category: method)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2856-2866 (and 2849)

> The withdrawal of the depth-not-vocabulary reading over-corrected into a false factual claim about the artifact's own queries. Section 13.4 asserts that for KI-21 (Avellaneda & Stoikov, 'High-frequency trading in a limit order book') 'the string `limit order` appears in **none** of them [the topical queries]' and concludes 'for KI-20 and KI-21 the vocabulary gap is demonstrated while the cap explanation is not'. That is false for KI-21. Topical query ka-crossref-12, published verbatim in the record's own section 3, is `query.bibliographic=market making inventory risk optimal bid ask quotes limit order book`. The claim is only true against the percent-encoded literal text; the arXiv/OpenAlex/S2 fences are URL-encoded and the record's own token test evidently ran on the encoded strings. The same paragraph's counter-assertion that '`betting market` **is** carried' fails the identical raw-string test and only holds after decoding, so the test was applied inconsistently. Consequence for a downstream decision: ka-crossref-12 retrieved 20 records against a platform-reported total of 4,458,996 (section 2 table), so KI-21's miss is more consistent with the retrieval cap the remediation just withdrew than with a vocabulary gap. A successor stage acting on 13.4 would add vocabulary already present and leave the binding constraint untouched. (The parallel claims for `parimutuel`, `dealer` and `specialist` are correct and verified absent even after URL-decoding; only the `limit order` claim, i.e. KI-21, is refuted.)

*Evidence as filed (verbatim).*

> Independent extraction of the 41 topical fenced blocks from lit_review section 3 and URL-decoding: `parimutuel` False, `pari-mutuel` False, `dealer` False, `specialist` False, `limit order` TRUE, `betting market` TRUE. Matching block: `https://api.crossref.org/works?query.bibliographic=market making inventory risk optimal bid ask quotes limit order book&rows=20&...` (fence id ka-crossref-12). Raw (undecoded) test returns False for both `limit order` and `betting market`, which is the only way the record's two adjacent claims can both be produced.

*Fix as filed (verbatim).*

> Restate 13.4: `limit order` IS carried by ka-crossref-12, so KI-21 is not a demonstrated vocabulary gap; its miss is undetermined between vocabulary and the rows=20 cap against 4,458,996 reported results, and the cap explanation is the live one. Keep the KI-20 (`dealer`), KI-09 (`parimutuel`) and KI-18 (`specialist`) vocabulary-gap findings, which verify. State that the token test is run on URL-decoded query strings and re-run it for `betting market` on the same basis.

*Reference:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 3 fence ka-crossref-12; section 2 provenance table row ka-crossref-12 (retrieved 20 / total 4,458,996)

**Refutation evidence (verbatim).**

> NOT REFUTED — the defect claim reproduces. I extracted all 86 fenced query blocks from section 3 of C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md (offsets 29543-45581, "## 3. Search strategies" to "## 4. Peer review of the strategy") and ran the token test raw and URL-decoded (unquote_plus).
> 
> Results: 'limit order' raw=[] decoded=['ka-crossref-07']; 'betting market' raw=[] decoded=['ka-crossref-05','ka-crossref-15','ka-nber-02']; 'parimutuel' raw=[] decoded=[]; 'pari-mutuel' raw=[] decoded=[]; 'dealer' raw=[] decoded=[]; 'specialist' raw=[] decoded=[].
> 
> The carrier is at line 340: `https://api.crossref.org/works?query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book&rows=20&select=...` — fence id ka-crossref-07 (fence header line 339), a Crossref topical-arm query. So the section 13.4 assertion at lines 2859-2860 that for KI-21 "the string `limit order` appears in **none** of them" is false, and the conclusion at lines 2864-2866 ("for KI-20 and KI-21 the vocabulary gap is demonstrated") is unsupported for KI-21. The inconsistency claim also reproduces: the raw (undecoded) test returns False for BOTH 'limit order' and 'betting market', so the record's two adjacent claims in the same passage can only be produced by applying the test on different bases.
> 
> Independent corroboration from the record's own prose: line 576 states the unrestricted forms of the arXiv category-narrowed phrases "are carried by `ka-crossref-07`, `ka-crossref-11`, `ka-openalex-06` and `ka-s2-02`" — the record elsewhere affirms ka-crossref-07 carries the market-making/limit-order-book vocabulary that 13.4 says is absent.
> 
> The finding's KI-20/KI-09/KI-18 exclusions verify as stated ('dealer', 'parimutuel', 'pari-mutuel', 'specialist' absent even after decoding), so those parts of 13.4 stand.
> 
> Two citation errors INSIDE the finding's evidence, which do not touch the defect claim: (1) the carrier fence is ka-crossref-07, not ka-crossref-12 — ka-crossref-12 is `Kalshi+regulated+event+contract+exchange+prediction+market+design` (line 354-355); (2) consequently the cited section 2 figures are the wrong row: the section 2 table gives ka-crossref-07 as retrieved 20 / total 79,887 (line 139), while 20 / 4,458,996 is ka-crossref-12 (line 144). The cap-vs-vocabulary point survives at 20 of 79,887, only with a smaller reported total than the finding states. These are attribution slips in the evidence, not grounds to drop the finding.

### QUANT-2-2 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: numerical)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:553-560; docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1749-1756; docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py:68-73

> The deliberate refusal to convert the abstract tie-break to a set is defended by a specific numeric verification that does not reproduce. A11 states: 'This was verified: with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (`X1` 6,672 instead of 6,707); with it left alone, it reproduces the table exactly.' I rebuilt the universe from the committed logs, converted line 73 to a set comprehension, and re-ran the full chain in both matching modes at PYTHONHASHSEED 0, 1, 7 and 12345. Every run reproduces the published table exactly, including X1 = 6,707. ADJUDICATION OF THE REFUSAL: UPHELD on the merits — the list comprehension is over raw-record order, Python's sort is stable, reverse=True does not reverse ties, so the executed form is already seed-independent, and converting it would introduce a seed dependency for no determinism benefit. But the sole cited evidence for the departure is wrong as recorded, and it sits in a frozen append-only amendment that has been transcribed into the registered protocol.

*Evidence as filed (verbatim).*

> Reconstruction fidelity first: PYTHONHASHSEED=0 rerun of ka-universe-script.py -> ka-dedup-script.py -> ka-partition-script.py -> ka-screening-script.py reproduces ka-screening-verdicts.jsonl BYTE-FOR-BYTE (4,890,628 bytes, identical sha256, 0 differing lines of 8,814). With `absts = sorted({...}, key=len, reverse=True)`: word-boundary mode seeds 0/1/7/12345 -> {include 149, X1 6707, X2 338, X3 35, X5 94, X7 244, X9 1, X10 545, X11 700}; KA_DEFI_MATCH=substring mode seeds 0/1/7 -> {include 149, X1 6707, X2 338, X3 35, X5 159, X7 236, X9 1, X10 545, X11 643} — i.e. the as-first-published table, exactly. No run produces X1 6,672.

*Fix as filed (verbatim).*

> Strike the '6,672 instead of 6,707' sentence from A11 (b) in both ka-protocol-amendments.md and the protocol addendum and replace it with the correct and sufficient justification, which is the stability argument already in ka-dedup-script.py lines 68-72: the list form is order-total by construction, so no conversion is needed and conversion would only add a seed dependency. Do not change the code.

*Reference:* Re-execution transcript; docs/literature/search_logs/kalshi-arbitrage/ka-dedup-script.py:73

**Refutation evidence (verbatim).**

> REFUTATION ATTEMPT FAILED — the finding is independently confirmed. I re-executed the chain myself in an isolated mirror of docs/literature/search_logs/kalshi-arbitrage (repo untouched; ka-screening-verdicts.jsonl sha256 9f41f6f48154c440c4bf173c15a361a6c8b222d6933a4092c591b658e8c780d0 before and after).
> 
> (1) Reconstruction fidelity holds. PYTHONHASHSEED=0, cwd=mirror root: ka-universe-script.py -> ka-dedup-script.py -> ka-partition-script.py -> ka-screening-script.py gave 15,924 raw / 8,813 works / 7,111 duplicates, REVIEW 2,905 / DEFAULT-X1 5,249 / include 149, and the emitted ka-screening-verdicts.jsonl matched the committed file BYTE-FOR-BYTE (identical sha256, 4,890,628 bytes).
> 
> (2) Counter-test on the A11 claim. I converted ka-dedup-script.py:73 to `absts = sorted({r['abstract'] for r in rs if r.get('abstract')}, key=len, reverse=True)` and re-ran the full chain at PYTHONHASHSEED 0, 1, 7, 12345 in both matching modes:
>   word-boundary (default): {include 149, X1 6707, X2 338, X3 35, X5 94, X7 244, X9 1, X10 545, X11 700} at all four seeds;
>   KA_DEFI_MATCH=substring: {include 149, X1 6707, X2 338, X3 35, X5 159, X7 236, X9 1, X10 545, X11 643} at all four seeds.
> The substring-mode result is character-for-character the published nine-code table quoted at ka-protocol-amendments.md:448-449 and protocol:1644-1645. X1 = 6,707 in every run. Row-level comparison of the word-boundary set-form output against the as-executed list-form output: 0 of 8,813 primary_code values differ, at every seed.
> 
> (3) I stress-tested alternative readings of "converted to a set" so the claim could not be rescued by construal: set + total key (-len, value); list + total key (-len, value); set + key=(len, value) with reverse=True — all four seeds/modes tested reproduce the same published table, X1 = 6,707. Even the maximally-divergent variant that inverts the selection rule entirely (set + key=(len, value), i.e. shortest abstract) yields X1 = 6,716, not 6,672, and it trips the A3 partition assertion (REVIEW 2,885 / DEFAULT-X1 5,269) before reaching the classifier. No configuration I could construct produces 6,672. Grep confirms "6,672" occurs nowhere in the repository except the A11 sentence itself.
> 
> (4) The auditor's UPHELD adjudication of the refusal is also corroborated, so the defect is confined to the cited evidence sentence: the set conversion IS genuinely seed-dependent at the abstract level (20-23 of 8,813 works select a different abstract between seed 0 and seeds 1/7/12345, and 17 differ from the as-executed list form at seed 0), yet none of those differences crosses a token boundary, so no screening code moves. Converting therefore adds a PYTHONHASHSEED dependency for zero determinism benefit — exactly the stability argument already recorded at ka-dedup-script.py:68-72.
> 
> Conclusion: the A11 sentence "with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (X1 6,672 instead of 6,707)" is false as recorded, in ka-protocol-amendments.md:557-559 and, transcribed, in protocol_kalshi-arbitrage-review_2026-09-02.md:1753-1755. Finding stands.

### QUANT-2-3 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: method)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:38,110,949,950; artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json key `X10_eligible_not_extracted`

> The A10 restatement of X10 was not propagated to four sites, three of which are in the very section the frontmatter NOTE claims was made consistent. Amendment A10 and the verdicts-file header state that X10 is 'NOT an eligibility determination... eligibility under I1-I5 was never assessed'. Surviving contradictions: (a) section 1 line 110 — 'X10 marks records that **passed** eligibility and were not extracted', two sentences after the paragraph that says the two codes are not eligibility criteria; (b) section 6 itemized rows 949-950 — 'X10: eligible S4/S7 platform-design record...' and 'X10: eligible; bears on settlement...'; (c) frontmatter machine-readable key `n_eligible_not_extracted: 545`, whose name asserts the struck claim to any tool reading only the header, which is the exact consumer REV-1-8 was raised to protect; (d) the sidecar repeats it as `X10_eligible_not_extracted`. A consumer parsing the frontmatter or the sidecar recovers precisely the claim QUANT-1-1/QUANT-1-4 withdrew.

*Evidence as filed (verbatim).*

> lit_review:110 'X10 marks records that **passed** eligibility and were not extracted'; lit_review:949 'X10: eligible S4/S7 platform-design record serving a secondary objective'; lit_review:38 'n_eligible_not_extracted: 545'; sidecar `"unresolved": {"X10_eligible_not_extracted": 545, ...}`. Against lit_review:25 'eligibility under I1-I5 was never assessed' and lit_review:851 same.

*Fix as filed (verbatim).*

> Rewrite line 110 to match the frontmatter wording ('X10 marks a keyword-identified candidate stratum whose eligibility was never assessed'); rewrite the two section-6 itemized reasons to drop 'eligible'; rename the frontmatter key to `n_keyword_candidate_unextracted` (or keep the key and add an adjacent `n_eligible_not_extracted_note: 'eligibility not assessed; see A10'`); rename the sidecar key to match.

*Reference:* protocol amendment A10, ka-protocol-amendments.md:408-441

**Refutation evidence (verbatim).**

> Refutation attempted and failed; every claimed site reproduced verbatim at the stated location.
> 
> (1) docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:110 reads "X10 marks records that **passed** eligibility / and were not extracted" — two lines after "are **not** eligibility criteria" (108-109). I read lines 108-140 in full: no correction, no strikethrough, no A10 pointer follows it before the "## 2. Information sources and methods" heading at line 114.
> 
> (2) Lines 949-950 reproduce exactly: "X10: eligible S4/S7 platform-design record serving a secondary objective..." and "X10: eligible; bears on settlement and adjudication (E7)...". Read in context (845-860) — plain itemized rows, no qualifier.
> 
> (3) Line 38 reads "n_eligible_not_extracted: 545". Line 25 in the SAME frontmatter block reads "X10 ... not an eligibility determination: ... eligibility under I1-I5 was never assessed" — direct self-contradiction inside the machine-readable header. Line 664 makes the exposure explicit and worse, not better: "The same three counts are carried in the frontmatter as `n_criterion_excluded`, `n_eligible_not_extracted` and `n_eligibility_undecided`, so a tool reading only the machine-readable header sees them too (findings REV-1-8, LITERATURE-1-15)" — i.e. the document itself directs the header-only consumer (the exact REV-1-8 consumer) to that key. The explanatory row at line 658 for the same count says "eligible-or-not is **unknown**", contradicting the key name it explains.
> 
> (4) Sidecar reproduced: artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json line 60, "unresolved": {"X10_eligible_not_extracted": 545, "X11_eligibility_undecided": 700, "total": 1245}.
> 
> Source check: ka-protocol-amendments.md A10 (lines ~408-441) confirms the restatement is binding — "**X10** is not 'ELIGIBLE under section 2'; it is a **keyword-identified candidate stratum** ... for which no eligibility determination under I1-I5 was ever made." Line 851 and line 2782/2786 of the lit review carry the corrected wording, proving the propagation was partial rather than the finding misreading a deliberate convention.
> 
> Counter-evidence against refutation: the review's own remediation ledger at line 3016 records QUANT-1-4 as remediated in "Section 1; section 6 rows; 13.2 item 2; frontmatter" — precisely the four surviving sites — so the document asserts a fix at locations that still carry the struck claim. No counter-test, source quote, or logical argument disproves the defect; the claim is true as stated.

### QUANT-2-4 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: reporting)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2431-2434

> Section 8.8, which the remediation added, miscounts its own table in the direction that flatters the corpus. The prose reads 'Eleven of the sixteen are at metadata depth' and 'Five are at abstract depth and simply were not carried — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung — and that is a synthesis omission, not a depth limit.' The table's own depth column is 9 meta and 7 abs, the sentence that says 'Five' then lists six names, and the seventh abstract-depth record (Oliven & Rietz 2004, forward-citation anchor A1 and one of the corpus's T1 records) is omitted from the list entirely. The understated quantity is the one the sentence exists to state: unforced synthesis omissions are 7, reported as 5.

*Evidence as filed (verbatim).*

> Mechanical tally of the 8.8 table depth column: abs = Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung (7); meta = Berg, Cao, Koch, Restocchi, Sestovic x2, Sethi, Swanson, Zhou (9). 9+7=16. Cross-checked against the section 7 table depth column: every one of the 15 resolvable 8.8 rows agrees with section 7.

*Fix as filed (verbatim).*

> Change 'Eleven' to 'Nine' and 'Five' to 'Seven', and add Oliven & Rietz to the enumerated list.

*Reference:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md section 8.8 table, rows 2412-2428

**Refutation evidence (verbatim).**

> Attempted refutation failed; the finding reproduces exactly. Mechanical tally of the section 8.8 table depth column (docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md, 16 data rows, extracted with awk -F'|' on field 6) yields meta = 9 (Berg, Cao, Koch, Restocchi, Sestovic 3044673, Sestovic 3035848, Sethi, Swanson, Zhou) and abs = 7 (Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung); 9+7=16, matching the section's own stated total of 16. The prose immediately below reads verbatim: "**Eleven of the sixteen are at metadata depth**" (actual 9) and "**Five are at abstract depth and simply were not carried** — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung" (actual 7; the enumerated list itself contains six names, so the sentence is internally inconsistent independent of the table). Three separate errors, all confirmed: the meta count is overstated by 2, the abs count is understated by 2, and the count word "Five" contradicts its own six-item list. Cross-check of the omitted record: section 7 line 1169 records oliven2004mnsc10400191 as "T1 | G | S1+S6 | abs" with role "included and extracted, but carries NO claim line in section 8 (LITERATURE-1-9)" — identical tier/strand/depth to the 8.8 row at line 2421, so the 8.8 table row is correct and it is the prose that is wrong, not the table. No alternative reading rescues the prose: "Eleven"/"Five" cannot be counting anything else in the table (there are exactly 16 rows and only two depth values), and the direction of both errors flatters the corpus by moving two unforced synthesis omissions into the "depth limit, nothing could be said" bucket. Severity as reported (major/reporting) is consistent with the sentence being the one place the section quantifies its own unforced omissions.

### QUANT-2-5 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: reporting)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2415; docs/literature/search_logs/kalshi-arbitrage/ka-gate-verdict.json

> Section 8.8, added by the remediation, cites Berg et al. 2008 under a DOI that does not exist: `10.1007/s15740722070`. The store and the section-7 table both carry `10.1016/s1574-0722(07)00080-7`; the string in 8.8 is the record's internal store key `berg2008s15740722070` with a Springer prefix pasted on. This defeats the deliverable-spec check 'every claim line carries a resolvable citation'. It also invalidates the G16 disposition as it now stands: ka-gate-verdict.json was written at 11:53 against the pre-remediation document (review mtime 13:18) and its disposition asserts 'All findings are G16 identifier-resolution findings of the standing closed publisher-landing-page class', a class defined by HTTP 403 at the publisher with Handle responseCode 1. This identifier is not in that class — it does not resolve at the Handle System at all. The gate was not re-run after remediation.

*Evidence as filed (verbatim).*

> https://doi.org/api/handles/10.1007/s15740722070 -> HTTP 404 (no handle). Correct identifier verified: https://api.crossref.org/works/10.1016%2Fs1574-0722%2807%2900080-7 returns 'Chapter 80 Results from a Dozen Years of Election Futures Markets Research', issued 2008, container 'Handbook of Experimental Economics Results' — matching lit_review:1078 and the store. ka-gate-verdict.json findings list contains no entry for s15740722070 (83 findings: 81 x HTTP 403, 1 x 404, 1 x 302).

*Fix as filed (verbatim).*

> Correct the 8.8 Berg cell to `10.1016/s1574-0722(07)00080-7`, then re-run the research-compile gate against the remediated document and re-record ka-gate-verdict.json with its new date/verdict, so the disposition in section 12 describes the document that ships.

*Reference:* DOI Handle System REST API https://doi.org/api/handles/{doi}; docs/literature/references_kalshi-arbitrage.json entry for 10.1016/s1574-0722(07)00080-7

**Refutation evidence (verbatim).**

> No refutation. Every element of the finding reproduced, and each counter-avenue tested failed. (1) docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2415 reads "| Berg et al. 2008 `10.1007/s15740722070` | T1 | G | S2 | meta | metadata depth; no finding can be stated |", while line 1078 and docs/literature/references_kalshi-arbitrage.json (id berg2008s15740722070) both carry 10.1016/s1574-0722(07)00080-7. (2) The 8.8 identifier does not exist: GET https://doi.org/api/handles/10.1007/s15740722070 -> HTTP 404 with body {"responseCode":100,"handle":"10.1007/s15740722070"} (100 = Handle Not Found); https://api.crossref.org/works/10.1007%2Fs15740722070 -> HTTP 404. (3) The correct identifier resolves: handle API responseCode 1, HTTP 200; Crossref returns title "Chapter 80 Results from a Dozen Years of Election Futures Markets Research", issued 2008, container "Handbook of Experimental Economics Results" — matching line 1078 and the store. (4) Counter-avenue "the 8.8 column is a store-key column, not a DOI column" is closed: sibling cells in the same column are genuine DOIs that resolve with responseCode 1 (10.2139/ssrn.6150527, 10.1287/mnsc.1040.0191, 10.1007/s10614-015-9514-7 all checked, all responseCode 1). (5) G16 disposition invalidated as claimed: ka-gate-verdict.json mtime 2026-09-02 11:53:48 vs review mtime 13:18:55; it records 83 findings, all G16, and a grep for "s15740722070" over that file returns 0 matches — the bad identifier is in no finding. Its disposition asserts "All findings are G16 identifier-resolution findings of the standing closed publisher-landing-page class; the resolution test is the DOI Handle System responseCode, and ka-store-doicheck.json records responseCode 1 for 149/149 identifiers"; ka-store-doicheck.json keys the Berg record on 10.1016/s1574-0722(07)00080-7 with responseCode 1, and contains no entry for 10.1007/s15740722070, which returns responseCode 100 — outside the asserted class. (6) Section 8.8 is absent from git HEAD's copy of the review (grep -c "8.8 Included records" on HEAD = 0), confirming it postdates the gate run, which was therefore not re-run against the shipping document.

### QUANT-2-6 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: reproducibility)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl (header `remediation.row_ids`); ka-screening-script.py:245-247

> The join key the remediation prescribes for reconciling the re-emitted verdicts against the pre-remediation file is not a key. The header instructs 'Join on the `identifier` field, not on `id`', but `identifier` is the empty string for 1,890 of the 8,813 rows (21.4%) — every record with no DOI, no arXiv id and no RePEc handle gets `ident = ""` at ka-screening-script.py:188. Those 1,890 rows collapse to a single join value and cannot be reconciled at all. Two secondary defects compound it: the header calls the row identifier `uid` ('uid values in this file are regenerated...') while the emitted field is named `id`; and the pre-remediation verdicts file was overwritten in place and is not archived, so the prescribed join cannot be exercised by anyone and the headline claim '6,183 of 8,813 differed' is unverifiable from the shipped artifacts.

*Evidence as filed (verbatim).*

> Tally over ka-screening-verdicts.jsonl: 8,813 data rows; distinct `identifier` values = 6,924; exactly one duplicated value, the empty string, with multiplicity 1,890. Field name in every row is `id` (e.g. `"id": "U00001"`); no `uid` field exists. `2,630 + 6,183 = 8,813` checks arithmetically but no pre-remediation file exists in docs/literature/search_logs/kalshi-arbitrage/ to check it against.

*Fix as filed (verbatim).*

> State that the join is only defined for the 6,923 rows carrying a persistent identifier and that the other 1,890 are unreconcilable; rename the header's 'uid values in this file' to 'id values'; and either archive the pre-remediation verdicts file as ka-screening-verdicts.pre-A11.jsonl or drop the unverifiable '2,630 of 8,813' figure to a stated-not-verifiable note.

*Reference:* docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:181-190

**Refutation evidence (verbatim).**

> No refutation found; every component of the finding reproduced independently. (1) Tally over docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl: 8,813 data rows, 6,924 distinct `identifier` values, exactly one duplicated value — the empty string at multiplicity 1,890 (21.4%) — so the header-prescribed join on `identifier` is undefined for those 1,890 rows and well-defined only for the 6,923 rows carrying a persistent identifier. (2) Field-name mismatch confirmed: row keys are ['id','citation','identifier','stage_excluded','verdict','primary_code','secondary_codes','criterion_cited','rule','reason','arms']; no row contains a `uid` field, while the header's remediation.row_ids reads "uid values in this file are regenerated...". (3) Cited source location confirmed: ka-screening-script.py line 188 is `ident = ""` as the else-branch of the DOI/arXiv/RePEc cascade at lines 181-188, and line 190 emits `"id": uid`. (4) No pre-remediation archive exists: a repo-wide find returns only the single ka-screening-verdicts.jsonl (no *pre-A11* / *pre-remediation* file); `git log` on that path is empty and `git status` shows the entire kalshi-arbitrage log directory untracked (`??`), so no VCS copy of the overwritten file exists either. (5) Counter-test for re-derivability failed to rescue the claim: the only audit toggle in the pipeline is KA_DEFI_MATCH=substring (ka-screening-script.py:85-88), which reverts DeFi token matching, not uid assignment; ka-dedup-script.py:17, ka-partition-script.py:14 and ka-screening-script.py:25 all hard-refuse to run unless PYTHONHASHSEED=0, while the pre-remediation uids arose from unseeded set-iteration tie-breaks — hence unrecoverable. The "2,630 of 8,813 agree / 6,183 differed" figure (lit_review_kalshi-arbitrage_2026-09-02.md:730, protocol_kalshi-arbitrage-review_2026-09-02.md:1736, ka-protocol-amendments.md:540) therefore has no shipped artifact against which it can be checked.

### QUANT-2-7 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: reproducibility)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:52 (frontmatter pip_freeze_sha256); logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json

> The pip-freeze digest published to close QUANT-1-7 does not verify against the archived file. The frontmatter and the ReproLog both publish pip_freeze_sha256 = 51760dc96e6e...c0550e and point at logs/reproducibility/env/51760dc9....txt. Hashing that file as stored gives 3796147276...0c40. The published digest is the CRLF->LF-normalized hash, and the normalization is disclosed nowhere in the ReproLog, the frontmatter or section 13.8. Because logs/ is gitignored, the digest is the only clone-durable carrier for this artifact, so a third party running sha256sum on the file they are handed gets a mismatch and has no way to know it is a line-ending convention rather than a substituted file. The ReproLog and sidecar digests, by contrast, both verify raw.

*Evidence as filed (verbatim).*

> sha256(raw bytes, 3405 bytes, contains CR) = 379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40; sha256(bytes with \r\n->\n) = 51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e = published value. Control: sha256(repro_log_8f5b02d3....json raw) = 416d4d48...b94ee (matches published); sha256(sidecar.json raw) = 96c4134c...5647a (matches published).

*Fix as filed (verbatim).*

> Either re-archive the pip-freeze with LF endings so the filename, the raw digest and the published digest coincide, or add an explicit note in the ReproLog and section 13.8 that pip_freeze_sha256 is computed over LF-normalized content. Do not leave the two conventions undocumented in one 13-field record.

*Reference:* CLAUDE.md §Reproducibility (hook-enforced): 'Every bootstrap, backtest, or inference run must log: git HEAD, project-venv pip freeze, dataset checksum, RNG seed, model commit hash.'

**Refutation evidence (verbatim).**

> Refutation attempt failed; the finding reproduces byte-for-byte and is corroborated by the canonical tool contract.
> 
> 1. Digest mismatch reproduced (Python hashlib, and independently sha256sum): logs/reproducibility/env/51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e.txt is 3405 bytes and contains 172 CRLF pairs (CRLF count 172 == total LF count 172, i.e. every line terminator is CRLF).
>    sha256(raw bytes)            = 379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40
>    sha256(bytes, \r\n -> \n)     = 51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e  <- the published value, and the filename
>    Both auditor-claimed digests match to the last hex digit.
> 
> 2. Controls reproduced: sha256(logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json) = 416d4d4891ffd9804f0276e91dc96d5c48460764722191ede10d5fbf476b94ee and sha256(artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json) = 96c4134c03f247edc2837e178525a9f215fb8eeb2ab30ca3b9ac53a5e1d5647a, both equal to the frontmatter values, raw, with no normalization. So the mismatch is specific to pip_freeze_sha256, not a global hashing convention a reader could infer.
> 
> 3. Non-disclosure verified at all three sites the finding names. The ReproLog is a flat 13-field record with pip_freeze_sha256 and pip_freeze_path and no note field of any kind. Frontmatter line 50 comments only on the archive location and on the stdlib-only execution. Section 13.8 states two scope limits (protocol-drafting stage not covered; freeze bounds rather than pins the scripts' dependencies) and neither mentions line endings. A repo-wide grep for CRLF / LF-normal / normalized-newline across docs/ and artifacts/runs/kalshi-arbitrage/ returns only unrelated hits (statistical "self-normalization" in bibliography abstracts).
> 
> 4. Counter-evidence I looked for actually strengthens the finding. The canonical implementation at C:\Users\skoir\.claude\skills\emit-repro-log\assets\emit_repro_log.py (capture(), lines ~244-247) does: freeze_bytes = _pip_freeze_bytes(); freeze_sha = hashlib.sha256(freeze_bytes).hexdigest(); freeze_path.write_bytes(freeze_bytes). Hash and archive are taken over the same byte string and the write is binary, so the project's own tool guarantees raw-file-hash == published digest == filename. SKILL.md line 28 likewise defines the field as the SHA-256 of freeze stdout. This archive therefore does not satisfy the contract the tool implements, so "the convention is documented elsewhere in the skill" is not available as a defence.
> 
> No counter-test, source quote, or logical argument disproved any element of the claim: mismatch is real, normalization is the explanation, disclosure is absent, controls verify raw.

### QUANT-2-8 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: reproducibility)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:967-977 (section 7 preamble)

> The single largest metadata remediation in this round has no archived evidence log. Section 7 states that all 149 DOIs were fetched from a registration agency at remediation time (122 Crossref, 26 DataCite, 1 unresolvable), that the store 'was checked against the registrant and found correct on every comparable field: 0 year disagreements in 148 comparisons, 0 container-title disagreements in the 119 records for which a registrant supplies one', and that on that basis 27 year cells, 78 venue cells and 18 in-text citation years were rewritten. No log of that sweep exists in docs/literature/search_logs/kalshi-arbitrage/. The only DOI-check artifact, ka-store-doicheck.json, was written at 11:20 (pre-remediation), records a different test (DOI Handle System responseCode, 150/150), and cannot support any of the year/container assertions. This contradicts the record's own frontmatter guarantee that 'every metadata field traces to a stored response in the search-log directory', and it is the one remediation whose correctness the reader is asked to take on assertion.

*Evidence as filed (verbatim).*

> ls docs/literature/search_logs/kalshi-arbitrage/ contains no registrant-metadata sweep log; ka-store-doicheck.json fields are {date_checked, method: 'DOI Handle System REST API ... responseCode 1 == handle resolves', n_checked: 150, n_responsecode_1: 150, failures: [], records}. MITIGATING, independently established by this audit: the 122/25/1/1 prefix split is arithmetically exact (122 non-arXiv-non-RG-non-JaLC + 25 x 10.48550 + 1 x 10.13140 + 1 x 10.11179 = 149); the section-7 table reproduces the store with 0 year and 0 container mismatches across all 149 rows; all inline section-8 citation years agree with the store; and a random 18-record sample of the store re-fetched live from Crossref agreed on year and container-title 18/18.

*Fix as filed (verbatim).*

> Emit and commit the sweep log (one row per DOI: registrant queried, HTTP status, returned issued/container-title/type, store value, agree/disagree) as ka-store-registrant-sweep.json, and cite it at section 7 the way every other check in this record is cited.

*Reference:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md frontmatter ai_assistance: 'every metadata field traces to a stored response in the search-log directory'

**Refutation evidence (verbatim).**

> Attempted refutation failed; the finding is confirmed on three independent checks. (1) Directory listing of docs/literature/search_logs/kalshi-arbitrage/ (151 files) contains no registrant-metadata sweep log; no file is named or shaped like a per-DOI Crossref/DataCite fetch of the store. (2) ka-store-doicheck.json parses to {date_checked, method: "DOI Handle System REST API https://doi.org/api/handles/{doi}; responseCode 1 == handle resolves", n_checked: 150, n_responsecode_1: 150, failures: [], records}, and every entry in records is exactly {"id": ..., "responseCode": 1} — no issued, no container-title, no registration agency — so it cannot support the section-7 assertions of 0 year disagreements in 148 comparisons or 0 container-title disagreements in 119 records. (3) Counter-test of the strongest available defense (that the responses already sit in the directory under other filenames): I parsed every non-bulk log (ka-crossref-*, ka-ki-*, ka-doc-*, ka-s2-*, protocol-doicheck.json, ka-store-doicheck.json) for records keyed to the 149 store DOIs extracted from references_kalshi-arbitrage.json. Only 57/149 store DOIs appear at all; only 45 carry issued/published/publicationYear and only 29 carry container-title — far short of the asserted 148 year and 119 container comparisons. The frontmatter guarantee is verbatim at line 60: "every metadata field traces to a stored response in the search-log directory". Section 7 at lines 967-977 cites no log, unlike section 12 (line 2626) and dataset_checksums (line 55), which both cite ka-store-doicheck.json by path. Git corroborates: the only commit touching this directory is 27d7473 and all files in it are currently untracked, so no sweep log was ever committed either.

### QUANT-2-9 — retained

- **raised_by:** quant-auditor (severity claimed: major; category: numerical)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:857,873-878; docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:493-508; docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1689-1704

> ADJUDICATION OF THE TWO DECLARED QUANT-1-2 DEPARTURES, plus an overstatement in the second. Departure 1 (8 of 65 records fall to X7 rather than X11): UPHELD. All 8 carry no DOI, arXiv id or RePEc handle, so under the frozen first-code-that-applies ordering the model branch legitimately routes them to an I3 failure; the reclassification is from a false B-a criterion failure to a true I3 one and is correctly declared. Departure 2 (plural/prefix forms rather than bare word boundaries): UPHELD ON SUBSTANCE BUT OVERSTATED BY ONE. Re-running with BOUNDED = {\bdex\b, \bamm\b, \bdefi\b, \bcrypto\b} moves TWO records out of X5, not the three the amendment names. 'Automated Market Makers in Cryptoeconomic Systems' remains X5 under the bare patterns because its abstract contains the standalone token 'amm design'. Separately, the two corpus-wide figures quoted as the defect's magnitude — '289 of the 305 works containing `dex` contain no word-boundary `dex`' and '83 of the 128 containing `amm`' — are computed with the bare patterns the remediation explicitly rejected; the shipped patterns give 284/305 and 64/128.

*Evidence as filed (verbatim).*

> Bare-pattern rerun: {include 149, X1 6707, X2 338, X3 35, X5 92, X7 244, X9 1, X10 545, X11 702} vs published X5 94 / X11 700 — differing records are exactly 'Dynamic Function Market Maker' and 'Funding-Aware Optimal Market Making for Perpetual DEXs'. U00378 blob: 'proper design of automated market makers (amms) ... amm design is, however, complex ... amm taxonomy ... amm archetypes' -> matches \bamm\b. Corpus-wide over the rebuilt 8,813-work universe: 'dex' substring 305, \bdex\b 16 (no-wb 289), \bdexe?s?\b 21 (no-wb 284); 'amm' substring 128, \bamm\b 45 (no-wb 83), \bamms?\b 64 (no-wb 64). VERIFIED SOUND alongside this: KA_DEFI_MATCH=substring reproduces the pre-remediation table exactly (X5 159, X11 643, X7 236, all other codes unchanged), and the 65/57/8 split and the 1,188->1,245 / 7,476->7,419 derived totals close.

*Fix as filed (verbatim).*

> In A11 and section 6, name only the two records the bare patterns would have moved and drop the third; and either recompute 289/305 and 83/128 with the shipped patterns (284/305, 64/128) or state explicitly that those two figures are measured against \bdex\b/\bamm\b to size the defect, not against the adopted patterns.

*Reference:* Re-execution of ka-screening-script.py with BOUNDED overridden; docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:83

**Refutation evidence (verbatim).**

> Attempted refutation failed; the finding reproduces exactly. Rebuilt the pipeline offline from committed logs (ka-universe-script.py -> 15,924 raw; ka-dedup-script.py -> 8,813 works; ka-partition-script.py -> REVIEW 2,905 / DEFAULT-X1 5,249 / include 149) under PYTHONHASHSEED=0, then ran a scratch copy of ka-screening-script.py with BOUNDED injected from JSON (committed verdicts file untouched). CONTROL: shipped patterns reproduce the published table exactly (include 149, X1 6707, X2 338, X3 35, X5 94, X7 244, X9 1, X10 545, X11 700); KA_DEFI_MATCH=substring reproduces the pre-remediation table exactly (X5 159, X11 643, X7 236, others unchanged). SUB-CLAIM 1 CONFIRMED: with BOUNDED = {\bdex\b, \bamm\b, \bdefi\b, \bcrypto\b} the counts are X5 92 / X11 702 and exactly TWO records differ from the shipped run - U02297 "Dynamic Function Market Maker" (X5->X11) and U02674 "Funding-Aware Optimal Market Making for Perpetual DEXs" (X5->X11). U00378 "Automated Market Makers in Cryptoeconomic Systems" REMAINS X5 under the bare patterns; its blob yields 4 matches of \bamm\b ("amm design is, however, complex", "we developed an amm taxonomy", "three amm archetypes") and 0 matches of \bdex\b, \bdefi\b, \bcrypto\b. Result is identical whether crypto is bounded (\bcrypto\b) or left as the shipped prefix (\bcrypto): X5 92 / X11 702, same two records. So the doc's claim at lit_review:873-878, ka-protocol-amendments.md:504-508 and protocol:1699-1704 that \bdex\b "would have wrongly moved three genuine DeFi records out of X5" is overstated by one. SUB-CLAIM 2 CONFIRMED: over the rebuilt 8,813-work universe, 'dex' substring 305, \bdex\b 16 (289 without), \bdexe?s?\b 21 (284 without); 'amm' substring 128, \bamm\b 45 (83 without), \bamms?\b 64 (64 without). The quoted figures 289/305 and 83/128 (lit_review:857; ka-protocol-amendments.md:493-494; protocol:1689-1690) are therefore measured against the bare patterns the remediation rejected, not against the adopted \bdexe?s?\b / \bamms?\b, which give 284/305 and 64/128. Only counter-observation found is cosmetic and does not touch the defect: the doc's plural-form justification does hold for U02297, which genuinely moves under \bamm\b; it fails only for the third named record.

### LITERATURE-2-1 — retained

- **raised_by:** literature-check (severity claimed: critical; category: misquoted / false supporting premise introduced by remediation)
- **refuted_by:** refuter, effort high
- **evidence_type:** `reproduced-check`
- **reproduction_required:** true
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2856-2862; docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1475-1482 (amendment A6)

> The round-1 remediation withdrew a wrong premise (the 'parimutuel' depth-not-vocabulary reading) and replaced it with another wrong premise. The claim that KI-21 Avellaneda & Stoikov is a 'demonstrable vocabulary gap' because 'the string `limit order` appears in none' of the topical queries is factually false, and the same false claim has now been written into the append-only protocol addendum as amendment A6.

*Evidence as filed (verbatim).*

> Review :2859-2862 — 'KI-21 Avellaneda & Stoikov, *High-frequency trading in a limit order book* — the string `limit order` appears in **none** of them. ... No cap can explain a miss on a term the strategy never asked for.' Protocol A6 :1479-1480 — 'KI-20 (Ho & Stoll, "dealer pricing") and KI-21 (Avellaneda & Stoikov, "limit order book"): neither term appears in any of the 35 frozen topical queries.' But protocol section 3.2, fenced block `ka-crossref-07` at :457-459, reads verbatim: `https://api.crossref.org/works?query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book&rows=20&...`. The phrase 'limit order book' is present (plus-encoded, exactly as `parimutuel` would have been); the same paragraph treats plus/hyphen variants as equivalent when it checks `pari-mutuel` and `pari mutuel`. The same query also carries 'market making' and 'inventory risk', which is the Ho & Stoll / Avellaneda-Stoikov lineage vocabulary, so the vocabulary-gap reading fails on substance for KI-20 as well even though the bare token `dealer` is genuinely absent (verified: `dealer` occurs in the protocol only at :657 (KI table), :824, :826, :1479 — never inside a fenced query). `parimutuel` and `specialist` absences are confirmed true (`parimutuel` only at :175, :180, :300-304, :433 prose, :646, :648, :824, :826, :918; `specialist` only at :655).

*Fix as filed (verbatim).*

> Strike the KI-21 sentence and A6's 'neither term appears' sentence. Restate: `ka-crossref-07` did ask for 'market making inventory risk optimal bid ask quotes limit order book', so for KI-20 and KI-21 the cause of the miss is NOT a vocabulary gap and remains undetermined between retrieval cap (rows=20 against a Crossref total) and ranking. Only `parimutuel` (KI-09) and `specialist` (KI-18) are demonstrated vocabulary absences. A6 is append-only, so issue a correcting amendment (A13) rather than editing A6, and re-hash.

*Reference:* Protocol section 3.2 fenced block ka-crossref-07 (primary artifact text); PRISMA-S item 8 (search strategies as run)

**reproduction**

````text
command:  Read protocol_kalshi-arbitrage-review_2026-09-02.md:457-459 (fence ka-crossref-07) and count the fenced query blocks in section 3.2.
observed: The fence reads `https://api.crossref.org/works?query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book&rows=20&select=...`; 41 fenced blocks total, of which the 35 topical queries at :439-556 include ka-crossref-07 — so A6's "neither term appears in any of the 35 frozen topical queries" is false for KI-21, and review :139 logs that query as executed with 20 retrieved against 79,887 total, leaving the cap explanation live.
````

**Refutation evidence (verbatim).**

> Refutation attempt failed; the finding is confirmed. (1) Reproduced the primary artifact text: protocol_kalshi-arbitrage-review_2026-09-02.md:457-459 fenced block `ka-crossref-07` reads verbatim `https://api.crossref.org/works?query.bibliographic=market+making+inventory+risk+optimal+bid+ask+quotes+limit+order+book&rows=20&select=...` — the phrase `limit order book` is present, plus-encoded. (2) Confirmed `ka-crossref-07` is inside the topical set: counting `^```text ` blocks gives 41 total, of which lines 439-556 are the 35 topical queries (crossref 15 + openalex 6 + arxiv 6 + s2 4 + nber 2 + repec 2 = 35) and lines 683-698 are the 6 documentary `ka-doc-*` blocks; A6's "35 frozen topical queries" is therefore exactly the set containing ka-crossref-07. (3) Reproduced both challenged claims verbatim: review :2859-2862 "KI-21 Avellaneda & Stoikov, *High-frequency trading in a limit order book* — the string `limit order` appears in **none** of them. ... No cap can explain a miss on a term the strategy never asked for."; protocol A6 :1479-1480 "KI-20 (Ho & Stoll, \"dealer pricing\") and KI-21 (Avellaneda & Stoikov, \"limit order book\"): neither term appears in any of the 35 frozen topical queries." (4) The only available defense — that the literal space-separated string `limit order` is absent because the URL is plus-encoded — is defeated by the document's own matching standard: the immediately preceding paragraph (review :2848-2850) tests the parallel claim by enumerating variants, "The string `parimutuel` (and `pari-mutuel`, and `pari mutuel`) appears in none of the 45 fenced topical query blocks", i.e. semantic-token equivalence, not literal string form. (5) Independent counter-evidence internal to the same review: line :576 states "the unrestricted forms of both phrases are carried by `ka-crossref-07`, `ka-crossref-11`, `ka-openalex-06` and `ka-s2-02`, so no vocabulary is category-gated out of the strategy as a whole" — the review asserts at :576 that ka-crossref-07 carries this vocabulary and at :2859 that the strategy never asked for it. (6) The competing cap explanation is still live rather than excluded: review :139 logs ka-crossref-07 as executed, retrieved 20, total hits 79887. (7) The finding's subsidiary concession checks out: `dealer` occurs in the protocol only at :657 (KI-20 table row) and :1479 (A6 prose), never inside a fenced query. Net: the "demonstrable vocabulary gap" premise for KI-21 is factually false as written and has been propagated into the append-only A6 amendment, exactly as the finding states.

### LITERATURE-2-3 — retained

- **raised_by:** literature-check (severity claimed: major; category: misdated citation of a canonical method source; the year-sweep's stated justification is false for a whole stratum)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1000-1004, 1069, 1128, 1189, 1856

> The remediation rewrote 27 year cells to the registrant `issued` field on the stated ground that it is 'the registrant's earliest recorded publication date'. For the University of Buckingham Press (10.5750) stratum that field is a retro-registration date, not a publication date, and the artifact now publishes 'Hanson 2012' for the canonical LMSR paper actually published in 2007 — misdating the S4 anchor by five years at both its table row and its section-8 claim line.

*Evidence as filed (verbatim).*

> Artifact :1128 'Hanson (2012). LOGARITHMIC MARKETS CORING RULES ... 10.5750/jpm.v1i1.417' and :1856 '([Hanson 2012](https://doi.org/10.5750/jpm.v1i1.417), T1, abstract depth)'. Crossref for 10.5750/jpm.v1i1.417 returns issued [[2012,12,13]] but ALSO volume 1, issue 1, page 3-15, and created 2020-08-26 — i.e. a bulk retro-registration. The store itself carries volume '1' and page '3-15' (references_kalshi-arbitrage.json:392-408), so the contradicting evidence is inside the artifact. The canonical citation is Hanson R. (2007), Journal of Prediction Markets 1(1):3-15 (confirmed by search; JPM vol 1 = 2007). Same defect: Abramovicz 10.5750/jpm.v1i2.423 published as '2012' (Crossref issued 2012-12-14, but vol 1 issue 2 pp.111-125 = 2007); Seemann 10.5750/jpm.v2i3.445 published as '2012' (vol 2 = 2008); Antweiler 10.5750/jpm.v7i3.824 published as '2014' (Crossref issued 2014-01-16, vol 7 issue 3 pp.61-86 = 2013). The sweep's control — ':974-975 0 year disagreements in 148 comparisons' — compares store to registrant and is structurally blind to this class.

*Fix as filed (verbatim).*

> Add a documented exception to the year CONVENTION for retro-registered DOIs: where the registrant's `issued` year is inconsistent with the registrant's own volume/issue and `created` fields, carry the volume-year and record both. At minimum restore Hanson 2007, Abramovicz 2007, Seemann 2008 and re-check the other 10.5750 rows. Note in section 7 that 'registrant issued = earliest recorded publication date' is false for this registrant.

*Reference:* Crossref REST API record for 10.5750/jpm.v1i1.417 (volume 1, issue 1, pages 3-15, created 2020-08-26)

**Refutation evidence (verbatim).**

> No refutation. Every element of the finding reproduced, and my independent counter-test corroborated it rather than disproving it.
> 
> Reproduced in the artifact: docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1128 carries "Hanson (2012). LOGARITHMIC MARKETS CORING RULES ... | 10.5750/jpm.v1i1.417", and :1856 carries "([Hanson 2012](https://doi.org/10.5750/jpm.v1i1.417), T1, abstract depth)". The convention text at :982 does state the year is the store's issued field, "the registrant's earliest recorded publication date". The control at :974 is stated as "0 year disagreements in 148 comparisons" store-vs-registrant, so it cannot detect a registrant-side error.
> 
> Live Crossref query for 10.5750/jpm.v1i1.417 returned exactly what the finding claims: volume 1, issue 1, page 3-15, issued 2012-12-13, published-online 2012-12-13, published-print null, created 2020-08-26. The store (references_kalshi-arbitrage.json:380-408) carries volume "1", page "3-15", issued 2012-12-13.
> 
> Counter-test I ran to try to rescue the 2012 year (volume-to-year mapping from the registrant's own records): 10.5750/jpm.v14i1.1796 has issued 2020-09-23 and created 2020-09-22 — a contemporaneous registration, so JPM vol 14 = 2020. With annual volumes that places vol 1 = 2007, vol 2 = 2008, vol 7 = 2013, matching the finding's stated years. The retro-registered rows all have created 2020-08-26: v1i1 issued 2012-12-13, v1i2 issued 2012-12-14, v2i3 issued 2012-12-14, v6i3 issued 2013-01-22, v7i3 issued 2014-01-16.
> 
> Logical disproof of the convention's premise, from the registrant's own data: v1i1 (vol 1) and v2i3 (vol 2) carry issued dates one day apart (2012-12-13 and 2012-12-14). Two different annual volumes of the same journal cannot have been published one day apart, so `issued` for this 10.5750 stratum is a batch registration timestamp, not a publication date. The artifact's stated ground for the year sweep is therefore false for this stratum, and the S4 anchor is misdated by five years at both cited locations. The defect claim stands.

### LITERATURE-2-4 — retained

- **raised_by:** literature-check (severity claimed: major; category: misdated + tier-too-low)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1089, 1861-1869

> Chen & Pennock, 'A Utility Framework for Bounded-Loss Market Makers', is cited as a 2012 T5 preprint. It is a peer-reviewed UAI 2007 proceedings paper; arXiv:1206.5252 is the 2012 bulk upload of the UAI proceedings. The artifact says it read this record at abstract depth, and the arXiv abstract page carries the journal reference.

*Evidence as filed (verbatim).*

> Artifact :1089 'Chen (2012). A Utility Framework for Bounded-Loss Market Makers. arXiv. 10.48550/arxiv.1206.5252 | T5'; :1867 '([Chen & Pennock 2012](https://arxiv.org/abs/1206.5252), T5 preprint, abstract depth)'. arXiv:1206.5252 (fetched) states: 'Appears in Proceedings of the Twenty-Third Conference on Uncertainty in Artificial Intelligence (UAI2007)', report id UAI-P-2007-PG-49-56. Under the artifact's own tier legend (:984, 'T1 peer-reviewed'), a UAI proceedings paper is T1, not T5. The section-7/section-8 tier-consistency sweep at :1013-1035 checked internal agreement only, so it could not catch a tier that is internally consistent and externally wrong.

*Fix as filed (verbatim).*

> Cite as Chen & Pennock (2007), UAI 2007, and re-tier T1 with the arXiv posting recorded as the retrieved manifestation. Re-run the tier check against the registrant/arXiv journal-ref rather than against the artifact's other copy of its own value; other 10.48550 rows in the corpus need the same pass.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Attempted refutation failed; the finding is confirmed against the primary source. (1) Both cited locations reproduce verbatim: :1089 renders "Chen (2012). A Utility Framework for Bounded-Loss Market Makers. arXiv. | 10.48550/arxiv.1206.5252 | T5", and :1866-1867 renders "([Chen & Pennock 2012](https://arxiv.org/abs/1206.5252), T5 preprint, abstract depth)". (2) I fetched https://arxiv.org/abs/1206.5252 myself: report number UAI-P-2007-PG-49-56, comments "Appears in Proceedings of the Twenty-Third Conference on Uncertainty in Artificial Intelligence (UAI2007)", submitted 20 June 2012 — i.e. the 2012 bulk proceedings upload of a 2007 peer-reviewed paper, exactly as alleged. (3) The tier legend at :984 defines "T1 peer-reviewed", and the artifact's own table already tiers conference proceedings T1 (chen2008 and chen2010 and chen2013 ACM EC, chakraborty2015 AAAI), so T5 here contradicts the artifact's internal practice, not merely an external standard. (4) The only candidate defense — the artifact's declared year CONVENTION at :1000 — does not cover this case and in fact cuts against the artifact: that convention exists to carry the EARLIER of two registrant dates ("For 12 records the registrant also records a later print year ... this artifact carries the earlier consistently"), whereas here the true publication year (2007) is earlier than the stored issued field (2012) and the artifact carries the LATER value. The convention also governs year only and says nothing about tier. (5) Root cause confirmed in the bibliography: the record chen2012autilityfr in docs/literature/references_kalshi-arbitrage.json holds "issued": [[2012]], "publisher": "arXiv", "type": "article", with no container-title, and the artifact's stated tier-derivation rule (:1035, "Venue is the field the tier is derived from"; tier resolved from registrant type and container-title) therefore mechanically yields T5. (6) grep for "UAI" and "Uncertainty in Artificial" across the lit review, the CSL-JSON store and the protocol returns zero hits, so the proceedings provenance is nowhere recorded as a deliberate exception. Both prongs of the finding — misdated and tier-too-low — stand.

### LITERATURE-2-5 — retained

- **raised_by:** literature-check (severity claimed: major; category: broken identifier + internal count errors in newly added text)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2415, 2431-2434

> Section 8.8 is new in this remediation and it introduces a non-resolving DOI and two wrong counts, one of which contradicts the list printed immediately after it.

*Evidence as filed (verbatim).*

> (a) :2415 'Berg et al. 2008 `10.1007/s15740722070`'. The section-7 row for the same record (:1078) carries `10.1016/s1574-0722(07)00080-7`. `10.1007/s15740722070` is a mangled reconstruction from the internal id `berg2008s15740722070` — wrong registrant prefix (10.1007 vs 10.1016) and stripped punctuation; it resolves to nothing. (b) :2431 'Eleven of the sixteen are at metadata depth' — the table's own depth column gives 9 meta (Berg, Cao, Koch, Restocchi, Sestovic x2, Sethi, Swanson, Zhou) and 7 abs (Bakalo, Dalen, Donatoni, Marek, Oliven, Portnaya, Sung); each agrees with the section-7 depth column. (c) :2432-2433 'Five are at abstract depth ... — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung' names six, and omits Oliven, so the true figure is seven.

*Fix as filed (verbatim).*

> Correct the Berg DOI to 10.1016/s1574-0722(07)00080-7; change 'Eleven'→'Nine' and 'Five'→'Seven'; add Oliven & Rietz to the abstract-depth-not-carried list. Generate the 8.8 DOI column from the store rather than from the record id.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Refutation attempt failed — every sub-claim reproduced exactly at the stated locations in C:\Users\skoir\castles\docs\literature\lit_review_kalshi-arbitrage_2026-09-02.md.
> 
> (a) Broken DOI CONFIRMED. Line 2415 reads: "| Berg et al. 2008 `10.1007/s15740722070` | T1 | G | S2 | meta | metadata depth; no finding can be stated |". Line 1078 (section 7) carries "10.1016/s1574-0722(07)00080-7" for the same record id berg2008s15740722070. The CSL store docs/literature/references_kalshi-arbitrage.json (line 95) gives DOI "10.1016/s1574-0722(07)00080-7" and URL "http://dx.doi.org/10.1016/s1574-0722(07)00080-7" for id berg2008s15740722070, so the store is unambiguous and section 8.8 disagrees with it. Independent resolution test against the DOI handle system: GET https://doi.org/api/handles/10.1007/s15740722070 returns HTTP 404 with {"responseCode":100,...} (handle not found), while GET https://doi.org/api/handles/10.1016/s1574-0722(07)00080-7 returns {"responseCode":1,...} resolving to https://linkinghub.elsevier.com/retrieve/pii/S1574072207000807. The auditor's account of the mangling (10.1007 vs 10.1016 registrant prefix, punctuation stripped, reconstructed from the record id string) is consistent with the observed value.
> 
> (b) Count error CONFIRMED. Line 2431 asserts "Eleven of the sixteen are at metadata depth". Machine read of the depth column of the 16-row table at lines 2414-2429 gives meta = 9 (Berg, Cao, Koch, Restocchi, Sestovic ssrn.3044673, Sestovic ssrn.3035848, Sethi, Swanson, Zhou) and abs = 7 (Bakalo, Dalen, Donatoni, Marek, Oliven & Rietz, Portnaya, Sung). 9+7=16, so the table is internally complete and "Eleven" contradicts the table printed immediately above the sentence. Depths also match the section-7 depth column (e.g. Berg :1078 "meta").
> 
> (c) Second count error CONFIRMED. Lines 2432-2433 read "**Five are at abstract depth and simply were not carried** — Bakalo, Dalen, Donatoni, Marek, Portnaya, Sung". The stated figure is five, the enumeration lists six names, and Oliven & Rietz 2004 (line 2421, depth "abs") is absent from the list; the table's abstract-depth count is seven. Three-way inconsistency (figure vs. its own list vs. the table).
> 
> No counter-evidence of any kind was obtained. I did not evaluate the proposed fix.

### LITERATURE-2-6 — retained

- **raised_by:** literature-check (severity claimed: major; category: misattributed author lists)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1043, 1895, 1927

> Section-8 claim lines truncate author lists without 'et al.', naming three authors for four- and five-author papers. The remediation swept years and container-titles but did not sweep author lists, and the artifact elsewhere prints full lists for 4- and 5-author works, so a reader cannot tell truncation from a complete list.

*Evidence as filed (verbatim).*

> (a) :1895 '[Chen, Fortnow & Lambert 2008](https://doi.org/10.1145/1386790.1386822)'. Crossref author order for that DOI: Yiling Chen, Lance Fortnow, Nicolas Lambert, David M. Pennock, Jennifer Wortman — five authors. (b) :1927 and :1043 'Gao, Wang & Wu 2025' for 10.1287/opre.2022.0417. Crossref authors: Jianjun Gao, Zizhuo Wang, Weiping Wu, Dian Yu — four; Dian Yu is dropped. Contrast the artifact's own full lists at :1909 'Othman, Pennock, Reeves & Sandholm', :1919 'Agrawal, Delage, Peters, Wang & Ye', :2134 'Birge, Feng, Keskin & Schultz' — so the convention is 'full list', and these two are errors rather than an abbreviation style.

*Fix as filed (verbatim).*

> Regenerate every section-8 author list from the CSL-JSON store's `author` array with an explicit, stated rule (full list, or first-author + 'et al.' above N), and re-check all multi-author claim lines. Two verified errors in a non-exhaustive sample of six means the class is unbounded until swept.

*Reference:* Crossref REST API records for 10.1145/1386790.1386822 and 10.1287/opre.2022.0417

**Refutation evidence (verbatim).**

> Attempted refutation failed; every element of the finding independently reproduced and my counter-checks corroborated it.
> 
> 1. Claim lines reproduced verbatim at docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:
>    - :1895 "([Chen, Fortnow & Lambert 2008](https://doi.org/10.1145/1386790.1386822), T1,"
>    - :1927 "([Gao, Wang & Wu 2025](https://doi.org/10.1287/opre.2022.0417), T1, abstract"
>    - The section-8.2 remediation-narrative instance is at :1042 ("Gao, Wang & Wu was shown as an"), not :1043 as the finding states; :1043 is the continuation clause of the same sentence. Off-by-one in the citation, same defect, not a refutation.
> 
> 2. Crossref REST API, queried directly:
>    - 10.1145/1386790.1386822 "Complexity of combinatorial market makers" -> authors: Yiling Chen (first), Lance Fortnow, Nicolas Lambert, David M. Pennock, Jennifer Wortman. FIVE authors; artifact names three with "&" and no "et al." Pennock and Wortman dropped.
>    - 10.1287/opre.2022.0417 "Price Interpretability of Prediction Markets: A Convergence Analysis" -> authors: Jianjun Gao (first), Zizhuo Wang, Weiping Wu, Dian Yu. FOUR authors; artifact names three. Dian Yu dropped.
> 
> 3. Counter-check against the project's own bibliography store, docs/literature/references_kalshi-arbitrage.json (149 items, read as UTF-8): entry chen2008138679013868 carries all five authors (Chen, Fortnow, Lambert, Pennock, Wortman); entry gao2025opre20220417 carries all four (Gao, Wang, Wu, Yu). The truncation is introduced in the prose claim lines, not inherited from the CSL-JSON store — so the store cannot be invoked as the authority that makes the short forms correct.
> 
> 4. Tested the strongest available defence — that a declared abbreviation convention makes three-name forms legitimate. It fails on two counts:
>    - No author-list, citation, or abbreviation convention is declared anywhere in the review or in docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md (grep for "author list", "citation convention", "first author", "abbreviat" returns only one unrelated hit at :2580 about a first-author name cluster).
>    - The artifact's operative convention is full-list, confirmed at :1909 "Othman, Pennock, Reeves & Sandholm 2013" (4 authors, complete), :1919 "Agrawal, Delage, Peters, Wang & Ye 2011" (5, complete), :2134 "Birge, Feng, Keskin & Schultz 2021" (4, complete). Further, when the artifact does truncate it marks the truncation: :1937 "Dudík, Wang, Pennock et al. 2021". An unmarked "&"-terminated list therefore reads as complete, which is exactly the ambiguity the finding asserts.
> 
> Both cited instances are confirmed misattributed author lists; no concrete counter-evidence exists.

### LITERATURE-2-7 — retained

- **raised_by:** literature-check (severity claimed: major; category: verdict-source attribution arithmetic does not close)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:679-687

> At the primary site of the QUANT-1-1 remediation, the enumeration of which strata make up the 8,663 classifier verdicts sums to 8,813 — i.e. it re-includes the 150 read-based records the sentence has just carved out.

*Evidence as filed (verbatim).*

> :681-686 'The other 8,663 were verdicted by the deterministic five-list keyword classifier ... rules R0-R9 — including the 5,249-record amendment-A3 DEFAULT-X1 stratum (rule R2), the 2,905-record A3 REVIEW stratum, and the 659 topical / known-item / supplementary records.' 5,249 + 2,905 + 659 = 8,813, not 8,663. The section-6 per-code table (:845-852) does close correctly at 8,663 classifier + 1 hand-verified X9 = 8,664 excluded, + 149 included = 8,813, so the defect is confined to the section-5 narrative but sits on the sentence that carries the corrected split.

*Fix as filed (verbatim).*

> State the three strata net of the 150 read-based records (or say 'the classifier-verdicted subsets of' those strata and give the net figures), so the enumeration reconciles to 8,663.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Attempted refutation failed; the defect reproduces exactly as reported.
> 
> 1. Text reproduced at [docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md](docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md):679-687. Lines 679-686 read: "**150 records carry a read-based verdict** (the 149 includes ... plus one hand-verified J6 same-work twin excluded X9). **The other 8,663 were verdicted by the deterministic five-list keyword classifier** ... rules R0-R9 — including the 5,249-record amendment-A3 DEFAULT-X1 stratum (rule R2), the 2,905-record A3 REVIEW stratum, and the 659 topical / known-item / supplementary records." Arithmetic: 5,249 + 2,905 + 659 = 8,813 = 8,663 + 150. Overstated by exactly the 150 the same sentence carved out.
> 
> 2. The three strata are provably disjoint and exhaustive over the full 8,813, so "including" cannot be read as a loose non-exhaustive list of subsets of 8,663. Amendment A3 (:2729) defines the partition: "A deterministic published vocabulary pre-sorter partitioning the 8,154-record forward-citation-only stratum into a 2,905-record REVIEW stratum and a 5,249-record DEFAULT-X1 stratum". 2,905 + 5,249 = 8,154 by that definition, and 8,813 − 8,154 = 659, which is exactly the residual arm the sentence labels "topical / known-item / supplementary". A partition of 8,813 cannot be contained in a set of 8,663.
> 
> 3. No alternative denominator rescues the sentence. Frontmatter :42 states "READ-BASED: 150 of 8,813 ... CLASSIFIER-BASED: 8,663", and :794-795 repeats 150 (1.7%) / 8,663 (98.3%). The 8,663 figure is therefore the document's own committed value, not the auditor's inference.
> 
> 4. Section-6 per-code table (:845-852) verified independently to close correctly: 6,707 + 338 + 35 + 94 + 244 + 1 + 545 + 700 = 8,664 excluded; removing the single hand-verified X9 row leaves 8,663 classifier verdicts. So the section-6 accounting is right and the defect is isolated to the section-5 narrative sentence, exactly as the finding states.
> 
> 5. Searched the whole file for any offsetting qualifier: grep for 5,249 / 2,905 / 659 / 8,663 / 8,813 returns no sentence anywhere that states the strata net of the read-based records, and no adjacent text at :676-695 carves the 150 back out. Line 685 is the only occurrence of 659 in a stratum sense (the other, :196, is an unrelated OpenAlex per-query count).
> 
> No counter-evidence exists. Finding stands.

### REPRODUCIBILITY-2-1 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: data_hashed)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:frontmatter pip_freeze_sha256; logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json; logs/reproducibility/env/51760dc9….txt

> The QUANT-1-7 closure digest for the environment does not verify against the bytes of the file it names. Four of the five filled keys verify byte-exactly; this one does not.

*Evidence as filed (verbatim).*

> sha256 of logs/reproducibility/env/51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e.txt as stored on disk (3,405 bytes, 172 CRLF line endings) = 379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40. The declared value 51760dc9…c0b550e is recovered only after CRLF→LF normalisation (Path.read_text().encode()). No normalisation convention is stated in the frontmatter, in §13.8, or in the ReproLog. By contrast I confirmed byte-exact: protocol full 42bc6116…, frozen prefix over the first 82,677 bytes 99524df0… (and byte-identical to the blob in commit 27d7473, so the addendum is genuinely append-only), bibliography fb0cf87e…, repro_log 416d4d48…, sidecar 96c4134c….

*Fix as filed (verbatim).*

> Either re-archive the pip-freeze with LF endings so the content-addressed filename and the declared digest match the bytes, or state the normalisation rule next to the key ('SHA-256 over the LF-normalised text') so a verifier can reproduce it.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Refutation attempt failed; every limb of the finding reproduced exactly, and the counter-tests I ran strengthened it rather than undermining it.
> 
> (1) Primary claim reproduces byte-for-byte. logs/reproducibility/env/51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e.txt is 3,405 bytes with 172 CRLF pairs out of 172 total LF (i.e. every line ends CRLF; first bytes are b'aiohappyeyeballs==2.6.1\r\naiohttp==3.13.2\r\n'). hashlib.sha256 over the raw bytes = 379614727648a27ea24a9eda1b789f3af7fd4d4b96fa5861ca2ef41dfbbd0c40. sha256 after b.replace(b'\r\n', b'\n') = 51760dc96e6ea3cbf93f08976bc3518cca5ca832cf22e993a06729118b0c550e, i.e. exactly the declared value in the lit_review frontmatter (line 50) and in the ReproLog's pip_freeze_sha256/pip_freeze_path. Auditor's numbers are exact, including the byte count and the CRLF count.
> 
> (2) Second limb (no stated normalisation rule) also holds. I grepped the frontmatter, read section 13.8 in full, and dumped logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json. The 13.8 QUANT-1-7 closure table says only "64-hex SHA-256 of the archived pip-freeze"; no normalisation convention appears in any of the three locations. A repo-wide grep for CRLF / line-ending / LF-normali across docs/ and CLAUDE.md returned no such rule.
> 
> (3) The only viable refutation avenue — a documented project-wide LF-normalisation convention living outside those three places — is contradicted by the governing skill. C:\Users\skoir\.claude\skills\emit-repro-log\assets\emit_repro_log.py lines 245-249 compute `freeze_sha = hashlib.sha256(freeze_bytes).hexdigest()` and then `freeze_path.write_bytes(freeze_bytes)` — the digest is over the exact bytes written, no normalisation, and the filename is content-addressed by that same digest. SKILL.md line 49 makes the intent explicit: binary mode is mandated because "Windows text-mode CRLF translation would invalidate byte-identity SHA-256." The canonical convention is byte-exact, so the on-disk file cannot have been produced by the reference writer as-is.
> 
> (4) Counter-test for a de facto normalisation convention: negative. I hashed the other cited files as stored. repro_log_...json contains 20 CRLF pairs and still verifies byte-exact against declared 416d4d48… ; references_kalshi-arbitrage.json (0 CRLF) verifies byte-exact against fb0cf87e… ; sidecar.json (0 CRLF) verifies byte-exact against 96c4134c… . So a CRLF-containing file in the same closure set is hashed byte-exactly, proving no consistent LF-normalisation rule exists and the pip-freeze archive is the sole outlier.
> 
> No counter-evidence of any kind was obtainable. The digest genuinely does not verify against the bytes of the file it names, and the file's own content-addressed name is likewise wrong for its stored bytes.

### REPRODUCIBILITY-2-2 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: entrypoint_runs)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json; docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2985-2995 (§13.8)

> §13.8 states the ReproLog 'covers the search-execution and remediation run'. The emitted log cannot cover the remediation run: its git_head is the pre-remediation registration commit and its phase names only the search execution.

*Evidence as filed (verbatim).*

> ReproLog fields: "phase": "search-execution", "git_head": "27d74738aa35ec1cdf1ec6915b50532e3620ea6f". That commit is the registration commit (git log confirms subject 'docs(protocol): register frozen kalshi-arbitrage search protocol'), and every round-1 remediation edit — the A11 script rewrite, ka-partition-script.py, the re-emitted verdicts file, the A12 addendum transcription — postdates it and is still uncommitted (git status shows the protocol as ' M' and the review/search logs as '??'). A ReproLog whose git HEAD predates the edits it claims to cover records the wrong tree state, which is precisely the failure mode the 13-field contract exists to prevent.

*Fix as filed (verbatim).*

> Emit a second ReproLog with phase 'remediation' at the follow-on provenance commit's HEAD and cite both, or narrow §13.8 to say the ReproLog covers the search-execution run only and that the remediation run's provenance is carried by the follow-on commit trailers.

*Reference:* none filed

**Refutation evidence (verbatim).**

> No refutation found; every claim reproduced. (1) The ReproLog at logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json contains exactly "phase": "search-execution" and "git_head": "27d74738aa35ec1cdf1ec6915b50532e3620ea6f". (2) git log confirms 27d7473 is the registration commit, subject 'docs(protocol): register frozen kalshi-arbitrage search protocol (sha256 99524df02696)', and it is also current HEAD. (3) git status --porcelain confirms every round-1 remediation edit postdates that commit and is uncommitted: ' M docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md' (the A12 addendum carrier) plus untracked ka-partition-script.py, ka-screening-script.py, ka-screening-verdicts.jsonl and ka-protocol-amendments.md. So the log's recorded tree state excludes the edits it is said to cover. (4) The §13.8 sentence reproduces verbatim at line 2975: "the ReproLog covers the search-execution and remediation run, **not** the protocol-drafting stage"; the 13.8 heading (line 2940) and line 2959 make the same combined-run claim. (5) Counter-test attempted and negative: I enumerated phase and git_head across all 14 ReproLogs in logs/reproducibility/. Only one belongs to this review (8f5b02d3, phase search-execution). A 'documentation-remediation' log exists (e23cae86) but its git_head is 57b409cb, an unrelated earlier deliverable, so no remediation-phase log covers this review. The strongest mitigating text is lines 2982-2984 ("git_head_at_authoring is 27d74738... for the execution run; the remediation run's HEAD is the follow-on provenance commit"), but that qualifies the frontmatter key git_head_at_authoring rather than the ReproLog's own git_head field, and does not retract the coverage claim two sentences earlier; it is a partial instance of the auditor's own proposed fix, not counter-evidence. Incidental check, no defect: the cited repro_log_sha256 416d4d4891ffd9804f0276e91dc96d5c48460764722191ede10d5fbf476b94ee matches the file's actual SHA-256.

### REPRODUCIBILITY-2-3 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: seeds_pinned)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1748-1756 (amendment A11 'Deliberately not changed'); mirrored at docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:558 and ka-dedup-script.py:~L110 comment

> The empirical claim used to justify refusing the prescribed abstract tie-break conversion — presented as measured — does not reproduce from the archived pipeline. The refusal itself is correct, but on a ground the artifact does not state.

*Evidence as filed (verbatim).*

> A11 asserts: 'This was verified: with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (X1 6,672 instead of 6,707).' I rebuilt the universe from the committed logs and patched the tie-break under both natural readings — sorted({...}, key=len, reverse=True) and sorted({...}, key=lambda a: (-len(a), a)) — then re-ran partition + screening. Result under BOTH readings and in BOTH modes: X1 = 6,707, and the full nine-code table is unchanged (word-boundary: 149/545/6707/700/94/35/338/244/1; substring: 149/545/6707/643/159/35/338/236/1). Only 7 of 8,813 works change abstract and none changes a screening code. Separately I verified the refusal is nonetheless right for a reason A11 does not give: sorting a set on key=len is genuinely PYTHONHASHSEED-dependent (works.json differed between seed 0 and seed 7), whereas the retained list form is not (dedup output identical at seeds 0, 1, 12345).

*Fix as filed (verbatim).*

> Strike the '6,672 instead of 6,707' sentence from A11 by append-only correction and replace the justification with the verifiable one: a set-based abstract tie-break re-introduces hash-seed dependence, which is what the amendment was fixing. Archive the counterfactual patch so a third party can re-derive whichever number is claimed.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Refutation attempted and failed; the finding is independently corroborated. I rebuilt the pipeline end to end from the committed logs (ka-universe-script.py -> 15,924 raw records; ka-dedup-script.py -> 8,813 works / 7,111 duplicates; ka-partition-script.py -> REVIEW 2905 / DEFAULT-X1 5249 / include 149; ka-screening-script.py with output redirected so the committed ka-screening-verdicts.jsonl was untouched), all under PYTHONHASHSEED=0.
> 
> Baseline reproduces the published nine-code table exactly in both modes: word-boundary 149/545/X1=6707/700/94/35/338/244/1; substring 149/545/X1=6707/643/159/35/338/236/1.
> 
> I then patched the abstract tie-break to a set under seven distinct readings: (r1) sorted({...}, key=len, reverse=True); (r2) sorted({...}, key=lambda a:(-len(a),a)); (r3) sorted({...}, key=lambda a:(len(a),a), reverse=True); (r4) sorted({...}, key=lambda a:(-len(a),a), reverse=False); (r7) sorted(list({...}), key=len, reverse=True); (p2) the r1 conversion applied to the pre-remediation script with title/venue tie-breaks reverted to bare key=len; and r1 swept over PYTHONHASHSEED 0, 1, 7, 42, 12345. In EVERY case, in BOTH DEFI match modes, X1 = 6707 and the full nine-code table is byte-identical to baseline. Abstract deltas were 17 works (r1) and 7 works (r2, matching the auditor's stated 7 of 8,813); none changed a screening code.
> 
> I additionally tested two variants that go beyond a tie-break change (shortest-abstract key=len; pure lexicographic sorted({...}, reverse=True)). Both violate the A3 partition asserts in ka-partition-script.py (REVIEW 2885 and 2900 vs the published 2905), and with the asserts bypassed yield X1 = 6716 and 6709 respectively. No construction I could find yields 6,672.
> 
> The A11 sentence at docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md ('This was verified: with the abstract tie-break converted, the substring-mode classifier no longer reproduces the published table (X1 6,672 instead of 6,707); with it left alone, it reproduces the table exactly.') is present verbatim at the stated location and mirrored in ka-protocol-amendments.md. Its first clause does not reproduce; its second clause does. The finding's claim stands.

### REPRODUCIBILITY-2-4 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: data_hashed)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1685-1705 (A11(a)); docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:854-880 (§6 X5 correction)

> The declared departure from the prescribed \bdex\b fix is justified by counts that do not reproduce, and the corpus-wide statistics quoted in the same paragraphs are computed under the pattern the script does NOT implement.

*Evidence as filed (verbatim).*

> Claim: '\bdex\b alone … would have wrongly moved three genuine DeFi records out of X5 (Funding-Aware Optimal Market Making for Perpetual DEXs; Dynamic Function Market Maker; Automated Market Makers in Cryptoeconomic Systems).' Running both patterns over the rebuilt 8,813-work universe, exactly ONE record's DEFI membership differs (U02674, the Perpetual DEXs record). The other two named records are retained by \bamms?\b and \bcrypto, which are byte-identical between the prescribed and implemented pattern sets, so \bdex\b could not have moved them. Second: 'Corpus-wide, 289 of the 305 works containing the string dex contain no word-boundary dex at all, and 83 of the 128 containing amm contain no word-boundary amm.' Measured: 289/305 and 83/128 hold under bare \bdex\b and \bamm\b; under the implemented \bdexe?s?\b and \bamms?\b the figures are 284/305 and 64/128.

*Fix as filed (verbatim).*

> Correct the departure justification to one record (the DEXs plural), and either restate the two corpus-wide statistics under the implemented patterns (284/305, 64/128) or label them explicitly as computed under the prescribed bare patterns.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Refutation attempt failed; the finding reproduces exactly on both limbs. Rebuilt the universe from the committed logs with PYTHONHASHSEED=0 via ka-universe-script.py + ka-dedup-script.py: 15,924 raw / 8,813 works / 7,111 duplicates, matching the archived pipeline. LIMB 1 (three named records): under the doc's own stated counterfactual (\bdex\b substituted for \bdexe?s?\b, all other DEFI tokens as implemented), exactly ONE work's DEFI membership changes — U02674 "Funding-Aware Optimal Market Making for Perpetual DEXs" (\bdexe?s?\b True / \bdex\b False; amm, defi, crypto all False; no long/spaced DEFI substring present). U02297 "Dynamic Function Market Maker" is False under BOTH \bdexe?s?\b and \bdex\b and is retained solely by \bamms?\b, which is unchanged in that counterfactual, so \bdex\b cannot have moved it. U00378 "Automated Market Makers in Cryptoeconomic Systems: A Taxonomy and Archetypes" is retained under BOTH pattern sets by amm (\bamms?\b True AND \bamm\b True) and by \bcrypto (True in both), so no variant of this change can move it out of X5. Tested the alternate charitable reading too: the round-1 finding as written in docs/audits/audit_trail_kalshi-arbitrage-review_2026-09-02.md:136 prescribed all four bare patterns (\bdex\b, \bamm\b, \bdefi\b, \bcrypto), not \bdex\b alone; under that all-bare set 4 works differ (U00056, U02297, U02674, U08726) — a different count and a different set from the doc's three, and still excluding U00378. Both readings falsify the doc's sentence. LIMB 2 (corpus-wide statistics): over the 8,813-work blob (title + titles_all + abstract, lowercased, identical to blob() in ka-screening-script.py), 305 works contain substring "dex"; \bdex\b matches 16 -> 289 with no word-boundary hit; \bdexe?s?\b matches 21 -> 284. 128 works contain substring "amm"; \bamm\b matches 45 -> 83; \bamms?\b matches 64 -> 64. The quoted 289/305 and 83/128 are exact under the PRESCRIBED bare patterns and incorrect (284/305, 64/128) under the patterns ka-screening-script.py:83 actually implements, exactly as the finding states. No concrete counter-evidence obtained; the defect claim is true as stated.

### REPRODUCIBILITY-2-5 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: data_hashed)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl:header.remediation.row_ids; ka-screening-script.py:245-247; protocol §A11 'Consequence for a reader'

> The prescribed migration key for the re-emitted verdicts file is null for 21% of rows, and the pre-remediation file it is meant to migrate from was overwritten in place and never archived, so neither the migration nor the '6,183 irreproducible row ids' measurement can be performed or checked by anyone.

*Evidence as filed (verbatim).*

> 'Join on the identifier field, not on id.' Parsing the 8,813 data rows: 1,890 (21.4%) carry identifier == "" — all 244 X7 by construction, plus 1,554 X1, 85 X2, 5 X3, 2 X5. Empty strings are not a join key. The as-first-published ka-screening-verdicts.jsonl is untracked and was overwritten by the A11 re-emission (git status shows the file as '??', so no prior blob exists in history), therefore the stated measurement '2,630 of 8,813 uids agreed / 6,183 differed' rests on no retained artefact.

*Fix as filed (verbatim).*

> Publish a uid_old→uid_new crosswalk (or the pre-remediation file itself) alongside the re-emitted verdicts, and state that 1,890 rows have no persistent join key so the citation string is the only available fallback for them.

*Reference:* none filed

**Refutation evidence (verbatim).**

> Could not refute; every claim reproduced. (1) Parsed all 8,813 data rows of ka-screening-verdicts.jsonl: exactly 1,890 (21.45%) carry identifier == "" (literal empty string, key present). Breakdown by primary_code matches the finding digit-for-digit: X1 1,554; X7 244; X2 85; X3 5; X5 2 (sum 1,890). All 244 X7 rows are empty by construction, since X7 is defined as "no DOI, arXiv identifier or RePEc handle in any retrieved metadata record". The 6,923 non-empty identifiers are unique, so the prescribed key works for exactly 78.55% of rows. (2) Prescribing text confirmed verbatim at protocol line 1759: "Join on the `identifier` field, never on `id`." — no carve-out for null-key rows; the header remediation.row_ids field repeats it plus "6,183 of 8,813 differed". (3) Counter-tests, all failing to refute: git log --all for the path returns empty and git ls-files shows only protocol-doicheck.json tracked in that directory, so no prior blob exists (the only *verdicts* blobs in history, commit 8aeebfe, belong to the unrelated explosive-regime review); a filesystem-wide search for *verdict*/*crosswalk*/*uid*/*.bak/*.orig/*pre-rem* found no pre-remediation copy or crosswalk; ka-screening-script.py writes the same path in mode "w" with no backup and ka-dedup-script.py was edited in place, its pre-A11 non-total sort keys gone and now hard-exiting via raise SystemExit('QUANT-1-6: run with PYTHONHASHSEED=0...'), so the old uid map cannot be regenerated from any retained artefact; the only surviving uids are 23 in ka-known-item-recall.json plus 24 in ka-dedup-ledger.json = 40 distinct (0.45% of rows) with no old->new mapping key; and the run sidecar retains screening_dispositions_as_first_published as aggregate counts only, with no row-level uids, so the 6,183 figure cannot be checked from it. (4) Two details strengthen the finding: the proposed citation fallback is not fully unique (the 1,890 null-key rows carry only 1,888 distinct citation strings, so two collide), and ka-known-item-recall.json has mtime 11:24, predating both the dedup remediation (12:50) and the verdicts re-emission (14:04), so its 23 uids are stale pre-remediation ids never regenerated. Only wording quibble, not a refutation: for the 6,923 populated-identifier rows a reader already holding the pre-amendment Table X-full CAN perform the migration, so "the migration cannot be performed" is over-broad — it fails for 21.4% of rows, not all. The defect claim itself (prescribed key null for 1,890 rows; pre-remediation file overwritten in place and never archived, leaving the 6,183 measurement uncheckable) is true as stated.

### REPRODUCIBILITY-2-6 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: data_hashed)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:967-976 (§7 regeneration note); docs/literature/search_logs/kalshi-arbitrage/ (no sweep artefact)

> The round-1 registration-agency metadata sweep that authorises the 27 year, 78 venue and 2 tier corrections has no stored response artefact, breaking the artifact's own stated provenance rule for every other network step.

*Evidence as filed (verbatim).*

> The review asserts '122 resolved at api.crossref.org, 26 at api.datacite.org … the store was checked against the registrant and found correct on every comparable field: 0 year disagreements in 148 comparisons, 0 container-title disagreements in the 119 records for which a registrant supplies one.' The search-log directory contains ka-store-doicheck.json (Handle System only: method 'https://doi.org/api/handles/{doi}', n_checked 150, n_responsecode_1 150) and protocol-doicheck.json; there is no Crossref/DataCite sweep file, and no file in that directory postdates the sweep except the scripts, the amendment log and the gate verdict. The frontmatter claims 'every metadata field traces to a stored response in the search-log directory'. What IS reproducible, and I verified it: the §7 table is regenerated from the store — 148 of 149 rows parsed, 0 year mismatches and 0 venue mismatches against references_kalshi-arbitrage.json. The arithmetic also checks: 122+26 = 148, +1 unresolvable (10.11179/ker.74.119) = 149, and AG-10 is disclosed at §13.3 and §13.9 item 4.

*Fix as filed (verbatim).*

> Archive the 148 registrant responses as ka-store-registrant-sweep.json (DOI → agency, year, container-title, HTTP status) or downgrade the '0 disagreements' sentence to an unverified assertion of the remediation session.

*Reference:* none filed

**Refutation evidence (verbatim).**

> No counter-evidence found; the finding reproduces exactly. (1) ka-store-doicheck.json is Handle-System-only: method = "DOI Handle System REST API https://doi.org/api/handles/{doi}; responseCode 1 == handle resolves", n_checked 150, n_responsecode_1 150, and all 150 record objects have the single key shape ('id','responseCode') — no year, container-title or agency field, so it cannot substantiate the "0 year disagreements in 148 comparisons / 0 container-title disagreements in 119" sentence at lit_review_kalshi-arbitrage_2026-09-02.md:967-976. (2) Repo-wide find for *registrant*/*sweep*/*agency* returns only unrelated audit-trail and deliverable-spec files; no Crossref/DataCite registrant sweep artefact exists in docs/literature/search_logs/kalshi-arbitrage/ or anywhere else, and no DataCite response file exists in the repo at all. (3) ka-protocol-amendments.md contains zero occurrences of "registrant" and no metadata-sweep record (its Crossref mentions concern search caps and abstract retrieval). (4) artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json (1868 bytes) holds only flow counts, screening dispositions and hashes — no registrant payload. (5) Counter-test for an alternative provenance path failed: of the 149 DOIs in references_kalshi-arbitrage.json, only 26 appear in any stored Crossref response (the pre-remediation ka-crossref-*.json query sets, 10:22-10:23); the remaining 123 have no registration-agency response stored, and the "agency" string hits are inside OpenAlex page dumps (an aggregator, not a registrant). The frontmatter claim quoted by the auditor is present verbatim at line 48, and AG-10 is disclosed at line 2815 / section 13.9, consistent with the auditor's account.

### REPRODUCIBILITY-2-7 — retained

- **raised_by:** reproducibility-verifier (severity claimed: major; category: llm_provenance)
- **refuted_by:** refuter, effort high
- **evidence_type:** `none`
- **reproduction_required:** false
- **outcome:** retained

**Claim (verbatim).** *Location:* docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md:1303, 1315-1317, 1327-1328, 1346-1348 (addendum A3); duplicated at docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md:107,131,150

> The QUANT-1-1 strike is incomplete in the governing document. The review body is clean, but the frozen protocol's own addendum — transcribed into the protocol under A12 on the same day A10 struck the claim — still asserts individual reading of forward-citation records in four places, with no supersession marker.

*Evidence as filed (verbatim).*

> Surviving in the protocol addendum: the A3 heading '(… 3,300 of the 8,154 affected records had already been read individually)'; 'each such record is read and verdicted individually by the LLM screener'; 'Individual reading of 8,154 titles was begun and carried through 3,300 records'; 'The 3,300 forward-citation-only records already read individually retain their individual verdicts'. A10 struck only the trailing sentence about the 659 topical records. Grep for 'A10' or 'supersed' within the A3 entry (protocol lines 1300-1365) returns nothing; the 'Superseded in part by A10' marker exists only in the review's §13.1 table. The re-run verdicts file contradicts the surviving text directly: counts_by_rule = R0 149, R9 1, and R2 5,249 + R3-R8 3,414 classifier outputs, i.e. zero read-based verdicts anywhere in the 8,154-record forward-citation stratum. Because the protocol is the registered, higher-authority document, the retracted claim currently survives at the authoritative site.

*Fix as filed (verbatim).*

> Append an A3 supersession note inside the protocol addendum (strike-don't-delete) stating that every 'read individually' assertion in A3 is withdrawn by A10 and that no forward-citation record carries a read-based verdict; mirror it in ka-protocol-amendments.md.

*Reference:* none filed

**Refutation evidence (verbatim).**

> NOT REFUTED. Every load-bearing element of the finding reproduced at the stated locations.
> 
> (1) All four "read individually" assertions survive verbatim in the protocol addendum A3: docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md line 1303 (heading, "3,300 of the 8,154 affected records had already been read individually"), line 1317 ("such record is read and verdicted individually by the LLM screener"), line 1327 ("Individual reading of 8,154 titles was begun and carried through 3,300"), line 1347 ("forward-citation-only records already read individually retain their individual verdicts"). Mirrored at docs/literature/search_logs/kalshi-arbitrage/ka-protocol-amendments.md lines 107, 121, 131, 151.
> 
> (2) No supersession marker exists inside A3. grep for 'A10|supersed|struck|strike|withdraw' over the protocol returned hits only at lines 1083-1084, 1228, 1535, 1605, 1612, 1616, 1648, 1662, 1793 — none inside the A3 entry (protocol lines ~1300-1365).
> 
> (3) A10's scope confirmed by reading protocol lines 1605-1675: it strikes exactly three statements — A3's 659-record sentence, the verdicts-file "encodes that reading" claim, and the corpus record's section-5 sentence. None of the four surviving A3 assertions is struck.
> 
> (4) The "Superseded in part by A10" marker exists only in the review's section 13.1 table (docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md line 2729), not in the protocol.
> 
> ADDITIONAL CORROBORATION FOUND: Protocol section 10 (line 1083) states the document's own convention — "a superseded provision is superseded BY an addendum entry, in place, and the original wording stays legible." The missing in-place marker therefore violates the protocol's own registered mechanism, strengthening the finding. There is no blanket "later entry supersedes earlier" rule that could serve as an implicit marker. Also, A3 (3,300 read) and A10 (REVIEW stratum = 2,905, none read) numerically contradict each other within the same addendum. The verdicts header independently confirms verdict_source_by_rule = "keyword classifier ...; no record read" for R1-R8, n_read_based_verdicts = 150, n_classifier_verdicts = 8,663.
> 
> ONE CORRECTION TO THE FINDING'S EVIDENCE TEXT (does not refute): the assertion "zero read-based verdicts anywhere in the 8,154-record forward-citation stratum" is strictly false. Counter-test — filtering ka-screening-verdicts.jsonl on set(arms) == {"forward-citation"} yields exactly 8,154 rows with counts R0 61, R1 236, R2 5,249, R3 426, R4 300, R5 46, R6 627, R7 31, R8 1,177, R9 1. That is 62 read-based verdicts (61 R0 includes + 1 R9 hand-verified twin), not zero. The finding's per-rule figures were also mis-grouped: R3-R8 sum to 3,170 corpus-wide; 3,414 is R1+R3..R8. These corrections change the magnitude, not the defect: A3 asserts 3,300 individually-read forward-citation records where 62 exist, and that retracted claim still stands unmarked at the registered, higher-authority document. The defect claim is TRUE. Note for remediation: the claimed fix's phrase "no forward-citation record carries a read-based verdict" should not be adopted verbatim, since 62 do.

## deferred-logged-minors

19 minor findings were logged and are **not** remediated this round, per the
loop's severity gate: the round's remediation budget goes to the 2 criticals and
31 majors. They are recorded here so that deferral is a decision on the record
rather than an omission, and they carry into round 3 unless a later round shows
one to be materially worse than logged. The round-1 trail's 24 deferred minors
also remain open and are not restated here.

| id | category | location | issue (compressed) | fix (compressed) | branch |
|---|---|---|---|---|---|
| REV-2-9 | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:766-772 | The PRISMA item-8 block reports the QUANT-1-1 reproduction against 'the published nine-code table' and then prints the pre-A11 counts (X5 159, X7 236, X11 643). Section 6 now publishes X5 94, X7 244, X11 700 as the record's table, so 'the published nine-code table' names two different tables in one… | Insert 'as first published, pre-A11' before the count list here and in the identical sentence in amendment A10, and add one clause noting that the post-A11 table in section 6 differs on X5/X7/X11 by t… | critical-reviewer |
| REV-2-10 | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2990 vs :2996-3034 | The traceability section's header count disagrees with its own table. The table carries exactly two rows marked critical (QUANT-1-1, REV-1-2) and thirty-five marked major, totalling 37; the header says three critical and 34 major. The round-1 disposition record names two retained criticals, so the t… | Correct the header to '2 critical, 35 major', or state that the third raw critical was among the four refuted and name it. | critical-reviewer |
| REV-2-11 | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2758-2800 | Section 13.2 announces three statements and then makes four, with the fourth inserted out of order: the list runs 1, 2, 4, 3, and the item numbered 4 — the 98.3% classifier disclosure, which the same item calls 'the limitation that conditions all three above' — sits between items 2 and 3. The QUANT-… | Change 'Three statements' to 'Four statements' and reorder the list so the numbering is monotone, keeping the classifier item at the position its own text claims (first, or explicitly framed as condit… | critical-reviewer |
| REV-2-12 | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1177 vs :2028; :1078 vs :2415 | Two records carry different identifying metadata at two sites after the LITERATURE-1-1/1-2 sweep. (a) Peters, So & Ye is 'Peters (n.d.)' in the section-7 table but cited as 'Peters, So & Ye 2007' in 8.4.2, which breaks the stated year convention that section-8 citation years are re-derived from the… | Backfill the Peters `issued` year from the registrant into the store and regenerate both the table cell and the 8.4.2 citation, or state at both sites that the store carries no year and drop 2007 from… | critical-reviewer |
| REV-2-13 | consistency | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2763-2765 and :2415-2429 vs :2255-2262, :2399 | The record states an absolute rule for metadata-depth records and then departs from it once without flagging the departure as an exception. Section 13.2 and the eleven 'metadata depth; no finding can be stated' rows of section 8.8 say such records are named without their findings being stated; 8.5.2… | Restate the rule as 'metadata-depth records are named, and no finding is stated beyond what the title itself asserts, which is flagged where it occurs', and carry the 'title only' flag onto the Flepp… | critical-reviewer |
| REV-2-14 | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:856-868 vs :894 | The X5 false-fire evidence cannot be reconciled with the move count as printed. The three token classes are given as 51, 9 and 17 hits, summing to 77, against 65 records moved; the record does not say whether the counts are token hits or records, nor that a record may fire on more than one token. A… | State the unit explicitly (token hits vs records) and give the record-level partition of the 65 — how many fired on dex only, amm only, defi only, and on more than one — so 51/9/17 and 65 reconcile on… | critical-reviewer |
| REV-2-15 | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1761-1772, :76-114 | RQI dimension 2 (originality) is not addressed explicitly. The corpus contains four survey- or review-tier records covering large parts of the same literature (Ziemba 2023; Newall & Cortis 2021; Ottaviani & Sorensen 2008; Hausch, Lo & Ziemba 2008), and the record says only that they are used for fra… | Add two or three sentences to section 1 stating what this record adds over the four survey-tier records it contains — at minimum the Kalshi-specific/generalized separation with a written carrying assu… | critical-reviewer |
| SCOPE-2-6 | partial | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2990 | The remediation traceability section misstates the round-1 disposition counts it exists to carry: it says 37 findings survived the gate as '3 critical, 34 major'. Two of the three raw criticals survived (REV-1-2, QUANT-1-1); the third, REV-1-1, was refuted and dropped — as the same section states si… | Correct the sentence to '2 critical, 35 major' and state that the third raw critical (REV-1-1) was refuted, so the surviving-critical count and the table agree. | scope-auditor |
| QUANT-2-10 | reproducibility | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2975-2985 (section 13.8); logs/reproducibility/repro_log_8f5b02d3bf61492… | Section 13.8's two declared scope limits are honestly stated and are NOT used to excuse the gap — the record says plainly 'That is a contract breach, not a design choice'. But a third limit is undeclared and the prose overstates coverage in one respect: 13.8 says the ReproLog covers 'the search-exec… | Either emit a second ReproLog for the remediation run with phase='remediation' and the follow-on HEAD, or restate 13.8 as 'the ReproLog covers the search-execution run; the remediation run's ReproLog… | quant-auditor |
| QUANT-2-11 | parameter | docs/literature/search_logs/kalshi-arbitrage/ka-screening-script.py:80,83 | The `\bcrypto` pattern is prefix-anchored, not word-bounded, and its documented admitted-form list is not what the regex does. The adjacent comment declares 'crypto -- prefix-anchored: "crypto", "cryptocurrency", "cryptoeconomic", "crypto-asset"'. The pattern also matches cryptography, cryptographic… | Either tighten to `\bcrypto(currenc\|economic\|-?asset\|s?\b)` matching the declared list, or amend the comment to state that the prefix also admits cryptograph*/cryptolog*/cryptanaly* and record that th… | quant-auditor |
| QUANT-2-12 | numerical | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2830,2849 | The topical arm is given two different and both-incorrect sizes nineteen lines apart in the same subsection, and one of them is the denominator of the token-absence verification. Line 2830: 'The 35 topical queries'. Line 2849: 'none of the 45 fenced topical query blocks in section 3'. The record act… | Replace both figures with the audited counts: 41 topical query executions (33 distinct queries plus 8 retries), and restate the token-absence tests against '41 topical query blocks'. | quant-auditor |
| QUANT-2-13 | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1343,1479,1606 | The REV-1-10 qualifier was applied to the section-10 gap statements (G-2, G-4, G-5) but not to three same-form universal negatives left in section 8. Lines 1343 ('which no record in this corpus establishes for Kalshi'), 1479 ('which no record in this corpus verifies') and 1606 ('no record in the cor… | Add the one-clause REV-1-10 qualifier ('among the 116 abstract-depth included records; the 33 metadata-depth, 545 X10, 700 X11 and 5,249 A3-rule records were not assessed') at each of the three sites,… | quant-auditor |
| QUANT-2-14 | reporting | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2815 (AG-10 row), 967-972 | AG-10's arithmetic and its literal statement both verify, but it is recorded as an unresolvable verification gap when the record is in fact verifiable by a method the artifact already uses elsewhere. 10.11179/ker.74.119 is registered with JaLC (Japan Link Center), which is neither Crossref nor DataC… | Resolve the record against JaLC (or doi.org content negotiation), record the response alongside the sweep log, and either close AG-10 or downgrade it to 'verified at its registration agency JaLC rathe… | quant-auditor |
| LITERATURE-2-8 | internal citation-year inconsistency; declared convention vi… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1005, 1125, 2082, 2568 | One DOI carries two different citation years inside the artifact, which is the exact defect the year sweep declared it had eliminated. | Pick one and apply it at all three sites; re-run the '18 citation years re-derived' sweep over the other eleven records in the twelve-record list, since the sweep demonstrably missed this one. | literature-check |
| LITERATURE-2-9 | missing citation for a declared reporting standard | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:7, 3052-3055 | Section 14 'Works cited by this record beyond the corpus' cites PRESS 2015 and PRISMA 2020 — the latter explicitly disclaimed by the record — but omits PRISMA-P 2015 and PRISMA-S, the two standards the frontmatter declares the record was written to and whose item numbers structure sections 2 and 5. | Add Moher D, Shamseer L, Clarke M, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015. Systematic Reviews. 2015;4(1). doi:10.1186/2046-4053-4-1; and Ret… | literature-check |
| LITERATURE-2-10 | incomplete citation / formatting defect in the human-readabl… | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:1097, 1177 | Two section-7 citation cells are malformed: a stray literal asterisk in an author field, and a citation published with no year where the registrant's own record supplies one indirectly. | Strip the stray asterisk. For Peters, carry 2007 with a note that the registrant records no `issued` and the year is taken from the registrant's `created`/series volume, or keep n.d. and add that note… | literature-check |
| REPRODUCIBILITY-2-8 | cross_platform | docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md:2849-2850, 2858-2861 (§13.4) | The restated vocabulary-gap claim cites a block count the protocol cannot supply, and contradicts the same section's own figure 20 lines earlier. | Change '45' to '35 fenced topical query blocks' at both sites. | reproducibility-verifier |
| REPRODUCIBILITY-2-9 | cross_platform | docs/literature/search_logs/kalshi-arbitrage/ka-gate-verdict.json (83 occurrences of claim_location) | An artefact staged for commit embeds an absolute Windows path containing the OS account name, in the one file the remediation added to the search-log directory without applying the <WORKDIR> scrubbing used on every archived script. | Rewrite claim_location to the repo-relative path docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md before the provenance commit. | reproducibility-verifier |
| REPRODUCIBILITY-2-10 | cross_platform | docs/literature/search_logs/kalshi-arbitrage/ka-screening-verdicts.jsonl; .gitattributes:14-18 | The primary machine-readable output is emitted with platform-native line endings and is not covered by the repository's eol=lf rules, so its bytes — and hence any digest taken over it — are platform-dependent. Same class as REPRODUCIBILITY-2-1. | Add '*.jsonl text eol=lf' to .gitattributes and open the output file with newline='\n' in ka-screening-script.py, so the verdicts file is byte-stable and hashable across platforms. | reproducibility-verifier |

Three of the nineteen are the same defect seen from three branches and should be
fixed once: REV-2-10 and SCOPE-2-6 both record that section 13.9's header says
"3 critical, 34 major" where its own table and the round-1 sidecar give 2
critical and 35 major; QUANT-2-12 and REPRODUCIBILITY-2-8 both record the
topical-arm block count, which LITERATURE-2-2's refutation resolves in favour of
45 for the review's section 3 (a different object from the protocol's 35 frozen
topical queries) — so those two minors should be closed by stating the
derivation at both sites, not by changing the number.

## verification-of-remediations

This round's primary task was to verify the 37 round-1 remediations rather than
to re-audit the artifact from scratch. What was independently re-derived, and
what it showed:

- **The archived pipeline reproduces byte-for-byte.** Two branches independently
  re-ran `ka-universe-script.py` → `ka-dedup-script.py` → `ka-partition-script.py`
  → `ka-screening-script.py` under `PYTHONHASHSEED=0` from the committed logs and
  regenerated `ka-screening-verdicts.jsonl` byte-identically (4,890,628 bytes,
  sha256 `9f41f6f4…`), with 15,924 raw / 8,813 works / 7,111 duplicates, REVIEW
  2,905 / DEFAULT-X1 5,249 / include 149 and the post-A11 nine-code table
  149/545/6707/700/94/35/338/244/1. The `KA_DEFI_MATCH=substring` audit toggle
  reproduces the as-first-published table exactly (X5 159, X11 643, X7 236), so
  the −65 / +57 / +8 deltas are third-party re-derivable. **QUANT-1-2 verified.**
- **QUANT-1-1 verified as complied with, not contested,** and the 150 / 8,663
  split confirmed in the verdicts header and in the section-6 per-code table.
  The strike is **not** complete, however: four A3 assertions of individual
  reading survive in the protocol's own addendum (REV-2-1, SCOPE-2-5,
  REPRODUCIBILITY-2-7 — three branches, one defect), so the review body is clean
  while the registered document of record is not.
- **Both declared QUANT-1-2 departures adjudicated.** Routing 8 identifier-less
  records to X7 is **upheld** on all branches: it follows the classifier's
  published first-code-that-applies ordering and is a fact about retrieved
  metadata. The inflected patterns (`\bdexe?s?\b` / `\bamms?\b`) are **upheld on
  substance but overstated by one record** — re-execution shows the bare patterns
  would have moved two records, not three (QUANT-2-9, REPRODUCIBILITY-2-4).
- **The QUANT-1-6 refusal to convert the abstract tie-break is adjudicated
  CORRECT**, but on a ground the artifact does not state: the executed list form
  is already order-total and seed-independent, whereas a set form re-introduces
  hash-seed dependence. The specific number A11 offers as its evidence
  (`X1` 6,672) does not reproduce under any of eleven constructions tried across
  two branches and four seeds (QUANT-2-2, REPRODUCIBILITY-2-3).
- **REV-1-2 verified.** Both venue-mechanism assertions are gone, the Levitt
  transfer is marked `not-transferable-as-stated`, and G-3 carries five itemized
  marks. One residual site survives the sweep (REV-2-8) and the AG-1 row still
  reports the superseded count of two (REV-2-4).
- **The protocol digests verify.** Frozen prefix `99524df0…` over the first
  82,677 bytes, byte-identical to the blob in commit `27d7473`; full protocol
  `42bc6116…`. **Amendment A12's append-only property holds.**
- **QUANT-1-7's closure digests resolve**, except one: the ReproLog
  (`416d4d48…`), the sidecar (`96c4134c…`) and the bibliography (`fb0cf87e…`)
  verify byte-exactly; `pip_freeze_sha256` verifies only after CRLF→LF
  normalisation, undisclosed (QUANT-2-7, REPRODUCIBILITY-2-1). §13.8's two
  declared scope limits are **honestly stated and not used to excuse the gap** —
  the record says plainly that the missing protocol-stage ReproLog is "a contract
  breach, not a design choice" — but a third, undeclared limit exists: no
  ReproLog covers the remediation run (REPRODUCIBILITY-2-2, QUANT-2-10).
- **The metadata sweep's results check out; its evidence log does not exist.**
  Live Crossref re-checks agreed 18/18 on one branch and on two further
  independent spot-checks; the §7 table regenerates from the store with zero year
  and zero venue mismatches; the DOI arithmetic closes (122 + 26 = 148 verified,
  +1 unresolvable = 149) and AG-10 is honestly disclosed. But no registrant sweep
  log was archived (QUANT-2-8, REPRODUCIBILITY-2-6), and the sweep's control is
  self-referential store-vs-registrant, which is structurally blind to the
  retro-registration class that misdates Hanson's LMSR by five years
  (LITERATURE-2-3).
- **The depth-not-vocabulary withdrawal over-corrected.** `parimutuel`,
  `pari-mutuel`, `dealer` and `specialist` are genuinely absent from the topical
  queries (verified on three branches, decoded and raw), so KI-09 and KI-18 stand
  as demonstrated vocabulary gaps; `limit order book` is **present**, in
  `ka-crossref-07`, so KI-21 is not (QUANT-2-1, LITERATURE-2-1 — the two
  criticals). The 45-block denominator the record uses is reproducible from the
  review's own section 3 and is not an error (LITERATURE-2-2, dropped).
- **The G16 gate disposition is correctly recorded** (81 HTTP 403 + 1 302 + 1 404
  = 83; AG-8 and AG-10 both carried), but the gate was run at 11:53 against the
  pre-remediation document and section 8.8 — added afterwards — introduces an
  identifier outside the class the disposition asserts (QUANT-2-5).
- **The remediation's self-reported over-findings verify** (27 year cells, 78
  container-titles, 6 tier contradictions, 19 records with no claim line, 10
  strand-mismatched records), except that new section 8.8 miscounts its own table
  and carries a mangled DOI (REV-2-5, QUANT-2-4, LITERATURE-2-5).
- **A visible pattern, and the one process finding of this round:** section 13.9's
  traceability table over-reports its own edits. REV-2-2 and REV-2-3 each catch a
  fix row naming a site that was not changed, and QUANT-2-3 catches a third. The
  13.9 table must not be treated as evidence that a fix landed; each row needs
  re-verification at its named site before this artifact ships.

## residual-risk-and-sampling-caveat

**Sampling caveat.** An audit samples. Every branch examined a subset of the
artifact — a subset of claim lines against their sources, a subset of DOIs
against their registrants, a subset of table rows against the store, a subset of
pipeline configurations against the published counts — and the examined evidence
may not be representative of the whole. Two of this round's findings say so in
their own terms: LITERATURE-2-6 states that two verified author-list errors in a
non-exhaustive sample of six means the class is "unbounded until swept", and
QUANT-2-8 accepts a 18-record live Crossref sample as mitigating rather than as
proof. Where a check was exhaustive it is described as exhaustive above; where it
was a sample it bounds nothing beyond itself. Absence of a finding in a class
this round is not evidence that the class is clean, and a clean spot-check is not
a clean sweep. One branch additionally records a **capability** limit rather than
a sampling limit: literature-check had no shell in this session and could not
verify four claims by execution (both protocol digests, the three
ReproLog/sidecar/pip-freeze digests, the verdicts join key and toggle, and the
150/8,663 split row-by-row); those four were carried by the quant and
reproducibility branches, which did execute them, and are recorded as verified
above on that basis.

**Per-branch residual risk, verbatim from the round payload.**

### critical-reviewer

> DIRECT ANSWER TO THE STANDING QUESTION. Yes, this is now a defensible compiled corpus record — but only as a record of what a published keyword classifier retrieved and what 116 abstracts plus 33 metadata stubs state, and it is defensible because the remediation trimmed the claims down to that, not because the evidence base improved. Every claim I could test in section 8 is now a transcription of one record with its carrying assumption on the line, and the four claim classes that previously exceeded the corpus have been repaired at their own sites: the corpus-level universal negatives (G-2, G-4, 8.4.1) are bounded to the 116 abstracts and name the 33 + 545 + 700 + 5,249 unassessed strata; the S4 central finding is bounded to records assessed at the depth reached; the venue-mechanism contradiction is gone from both sites with G-3 raised to five itemized marks; and the Shin/Glosten-Milgrom attribution bridges are downgraded or withdrawn. The frontmatter now carries the split (7,419 / 545 / 700) and the 150-vs-8,663 verdict source, so a machine consumer cannot read 149/8,813 as a completed screen. On my checks the arithmetic holds: nine codes sum to 8,813 both pre- and post-A11, counts_by_rule sums to 8,813, X1 = R2 + R8, 65 = 57 + 8, 1,188 + 57 = 1,245, 122 + 26 + 1 = 149 with 25 arXiv DataCite DOIs confirmed in both the table and the store, 149 table rows / 116 abs / 33 meta / 90 T1 / 19 K, and two independent Crossref spot-checks (Abramovicz 10.5750/jpm.v1i2.423 -> journal-article, The Journal of Prediction Markets, 2012; Flepp 10.1016/j.qref.2016.07.016 -> journal-article, QREF, 2017) confirm the tier and venue sweep. Both declared departures adjudicate as ACCEPTED: routing 8 identifier-less records to X7 follows the classifier's own published first-code-that-applies ordering and is a fact about retrieved metadata, all eight named; and the inflected word-boundary patterns are strictly narrower than the frozen substring behaviour except where widening was needed to keep three genuine DeFi records in X5, with the counter-examples named. The refusal to convert the abstract tie-break also adjudicates as CORRECT — ka-universe-script.py iterates sorted(LOG.glob(...)) so raw-record order is already deterministic, the sort is stable, and converting it would have moved X1 to 6,672, i.e. re-screened 35 records under cover of a determinism fix. What the corpus still cannot carry, and what no prose fix will change: with 700 undecided transfer-clause records feeding the largest strand, 4 of 5 named-lineage anchors at metadata depth, and zero full texts, S4 supports no statement about the inventory-risk literature at large, only about the anchors named — the record says exactly this at 8.4 and G-5, so the claim and the capacity now match, but the reader should treat S4 as a reading list with transfer flags rather than as a synthesis. The remaining exposure is auditability, which is this record's whole defence and where three of this round's findings land: the protocol addendum now reasserts the struck individual-reading claim (REV-2-1), the prescribed verdicts-to-store join fails for roughly a tenth of the include rows (REV-2-7), and the prisma-s-9 offsetting claim the record says it withdrew is still standing at its own site (REV-2-3). A visible pattern is that the traceability table over-reports its own edits — REV-2-2 and REV-2-3 both catch fix rows naming sites that were not changed — so the 13.9 table should not be trusted as evidence that a fix landed; each row needs re-verification at its named site before this ships. RQI coverage: importance covered (adequate — the question is well posed, the protocol fixes it, and ADR-0004 scopes the governing rule set correctly and argues both failure modes); originality covered by REV-2-15 (gap, minor); method covered by checklists A and B; presentation covered by REV-2-5/2-9/2-10/2-11/2-14; interpretation covered by REV-2-8 and REV-2-13. No unrouted-analysis finding: CHAMP items 7-16 are quant-auditor's and were routed.

### scope-auditor

> Direct answer to the standing question. Judged strictly on spec-to-delivery coverage — the only question this branch answers — the artifact is now a defensible compiled corpus record, but it is not yet a complete delivery of Thread C. Defensible, because after the 37 remediations every limit that bounds the claims is declared at the level a consumer meets first: the frontmatter carries screening_verdict_source (150 read-based / 8,663 classifier), extraction_depth (zero full texts, 116 abstract, 33 metadata), and the three unresolved-count keys; the flow table splits n_excluded into 7,419 criterion failures and 1,245 capacity dispositions; the classifier is declared as the item-8 automation tool with its script, rules and re-runnable audit toggle archived; the Kalshi/generalized separation is repaired and 13.7 no longer asserts the absolute it once did; the twelve deviations are numbered, dated and now carried in the protocol's own addendum. A corpus record whose every disposition is a published rule output, and which says so on its first page, states less than a review but states it honestly. Not complete, because the spec's item-5 synthesis has one of five named components (applicability of inventory-risk models to bounded [0,1] payoffs) that the corpus answers only by declaring it unanswerable at the depth reached (SCOPE-2-1); because two Thread C/D artifacts remain undelivered (SCOPE-2-3, SCOPE-2-4); and because the spec's own ticked acceptance evidence now contradicts the delivery on four numbers (SCOPE-2-2). The residual risk that survives all prose repair is unchanged in kind from round 1 and is a coverage risk, not a wording risk: 700 undecided records of exactly the class that carries the largest strand, 545 unextracted, and no full text anywhere in the corpus mean the S4 strand is a bibliography with abstracts attached rather than a synthesis, and the SSRN-dense included set (31 of 149, 13 of 19 Kalshi records) sits on an arm that was never run (G-9). Nothing in the shipped artifact overstates that now; the exposure is that a downstream agenda will treat a declared non-answer as a negative finding. That is what SCOPE-2-1's fix and the missing agenda's falsification tests must be written against.

### quant-auditor

> The pipeline, the corpus store, the flow arithmetic and the registration integrity all verify independently — I rebuilt the universe from the committed logs and reproduced ka-screening-verdicts.jsonl byte-for-byte, confirmed the frozen 82,677-byte prefix hash against the tracked file at commit 27d7473, confirmed the substring toggle reproduces the pre-fix nine-code table exactly, and matched 18/18 store records live against Crossref — so the remaining exposure is not in the numbers the corpus reports but in three self-verification claims the remediation made about its own decisions that do not reproduce (X1 6,672, the third DeFi record, the `limit order` absence), one non-resolving DOI introduced in new section 8.8, and the fact that the 700 X11 undecided records still outnumber the 149 includes 4.7:1 in exactly the transfer-clause class that feeds S4, with zero full texts read, so E8/E10/E12 remain partially completed at best regardless of any prose fix. ON THE STANDING QUESTION: yes, this is now a defensible compiled corpus and its section-8 synthesis does not exceed what the corpus can carry — 102 of 104 claim bullets carry a resolvable primary citation, the Kalshi/generalized split is enforced per line with the carrying assumption written on it, the five load-bearing transfers are marked not-transferable-as-stated, the 17-of-19-T5 concentration and the 98.3% classifier share are stated in the frontmatter and in G-6/G-10, and the two corpus-negative bullets are scoped to the 116 abstract-depth records; what still exceeds the evidence is not the synthesis but section 13.4's causal diagnosis of the artifact's own recall failures and the residual 'eligible' language on the 545 X10 records.

### literature-check

> VERIFIED AND HOLDING (do not re-raise): REV-1-2 — both venue-mechanism assertions are gone; :1699-1714 marks the Levitt transfer `not-transferable-as-stated` and :1818-1827 attributes 'quote-driven' to Bürgi et al. as what that record says; G-3 is now five itemized rows at :2540-2546. The Glosten & Milgrom / Glosten & Harris disentangling at :2054-2067 is a correct method attribution (Glosten & Harris 1988, JFE 21(1), 10.1016/0304-405X(88)90034-7 is indeed a different paper, and the Kyle-lambda bridge kept at :2068-2075 is sound). AG-10 is honestly stated: 10.11179/ker.74.119 is registered with JaLC (confirmed via doi.org/ra/10.11179), resolves at the Handle System (responseCode 1 → hdl 2433/24842), and is registered with neither Crossref nor DataCite as claimed. The DOI-sweep arithmetic closes: 122 Crossref + 26 DataCite = 148 verified + 1 unresolvable = 149. Section 14's PRESS 2015 and PRISMA 2020 citations are correct. Claim-to-source fidelity spot-checks passed: Bartlett & O'Hara (10.2139/ssrn.6615739) and Feys (arXiv:2606.01477) match their abstracts; the Thaler & Ziemba, Snowberg & Wolfers and Ottaviani & Sørensen claim lines at 8.3.2 match the sources and carry correct assumptions; Buckle 10.1177/155862351801300305 and Gao et al. 10.1287/opre.2022.0417 container-titles are correct as rewritten; Hodges 2013 and Dudík 2021 are correct. The 19 = 3 added + 16 listed split reconciles against the section-7 role column. ADR-0004's citation of REVIEW.md blocking directive 8 is accurate (REVIEW.md:30).
> 
> VERIFICATION GAPS ON MY BRANCH: Bash is disabled in this session, so I could NOT verify by execution (a) the frozen-prefix hash 99524df0… over 82677 bytes or the full-protocol hash 42bc6116…, (b) the ReproLog / sidecar / pip-freeze SHA-256s at :50-54 (both paths are gitignored and resolve in no clone), (c) the ka-screening-verdicts.jsonl join key or the KA_DEFI_MATCH=substring toggle, (d) the 150/8,663 split row-by-row against the verdicts file. I verified the split only as published arithmetic, where section 6 closes correctly and section 5's enumeration does not (LITERATURE-2-7). Those four remain open for the quant branch; I am not accepting them on cached knowledge.
> 
> THE STANDING QUESTION — direct answer. Judged on citation and attribution alone, the synthesis does NOT exceed what the corpus can carry, but only because the remediation attached corpus-scope qualifiers to every universal negative (:1833-1844, :2264-2270, :2520-2526, :2554-2559) and because section 8's claim lines are, on the sample I checked against primary sources, accurate transcriptions with their carrying assumptions written on the line. What the artifact is now is defensible: a keyword-partitioned, abstract-depth index of 149 records with a heavily hedged narrative over 116 abstracts. What it is not, and no longer claims to be, is a compiled corpus of the literature — 98.3% classifier dispositions, 700 undecided, 545 unextracted and zero full texts are all disclosed at their true size. The blocker is not over-claiming; it is that the remediation introduced fresh factual errors in the very passages written to fix over-claiming (LITERATURE-2-1 propagated into an append-only registered protocol amendment, LITERATURE-2-5's broken DOI and two wrong counts in brand-new section 8.8), and that the metadata sweep's control was self-referential (store-vs-registrant), letting a canonical method source — Hanson's LMSR — ship misdated by five years. These are prose- and metadata-level fixes; none requires re-screening. Ship after they are closed, not before.

### reproducibility-verifier

> WHAT I VERIFIED AS GENUINELY FIXED (do not re-raise): the archived pipeline now runs end-to-end from committed logs and is byte-exact. I re-ran ka-universe-script.py -> ka-dedup-script.py -> ka-partition-script.py -> ka-screening-script.py under PYTHONHASHSEED=0 and regenerated ka-screening-verdicts.jsonl BYTE-IDENTICALLY to the published file (sha256 9f41f6f48154c440…), with 15,924 raw / 8,813 works / 7,111 duplicates, REVIEW 2,905 / DEFAULT-X1 5,249 / include 149, and the exact post-A11 table 149/545/6707/700/94/35/338/244/1. The KA_DEFI_MATCH=substring toggle reproduces the as-first-published table exactly (X5 159, X11 643, X7 236), so the deltas -65/+57/+8 are third-party re-derivable. Determinism is real and stronger than claimed: dedup output is identical at PYTHONHASHSEED 0, 1 and 12345. Criterion/capacity totals reconcile (7,419 + 1,245 + 149 = 8,813; 6,707+338+35+94+244+1 = 7,419; 545+700 = 1,245) and match the sidecar's two disposition tables. The 150/8,663 split is confirmed in the verdicts header (n_read_based_verdicts 150 = 149 include + 1 X9; n_classifier_verdicts 8,663; 8,663/8,813 = 98.30%). The frozen prefix is byte-identical to the blob in commit 27d7473 and both protocol digests verify. ReproLog and sidecar resolve byte-exactly and the ReproLog carries all 13 fields. The G16 gate disposition is correctly recorded (81 HTTP-403 + 1 302 + 1 404 = 83; AG-8 and AG-10 both carried) and every section-heading citation I checked resolves in the named predecessor files, including the verbatim 'handle-API responseCode 1 is the resolution test' string. §7 regeneration reproduces from the store with zero year and zero venue mismatches; the 10 [synth Sn] markers are present and count correctly; the topical-token-absence claim holds. The QUANT-1-2 departure to X7 for 8 records is correct under protocol §2.4's first-code-that-applies ordering, since X5 precedes X7 and no longer applies once the token match is anchored.
> 
> DIRECT ANSWER TO THE STANDING QUESTION. The mechanics are now defensible; the synthesis is not, and the artifact says so about itself. As a COMPILED CORPUS RECORD the deliverable is shippable in kind: every count is reproducible from committed artefacts, the automation tool of record is declared, the 98.3% classifier share is on the front page, and 545 X10 / 700 X11 / 33 metadata-depth / zero full texts are named at every synthesis site with the carrying assumption on the claim line. But the corpus cannot carry strand-level statements about what the literature establishes. 8,663 of 8,813 dispositions are statements about token co-occurrence in a title and abstract, nothing more; 700 records with UNDECIDED eligibility are concentrated in the transfer-clause class that feeds S4, the largest strand, and outnumber the 149 includes 4.7:1; the 149 includes were read at abstract depth (116) or metadata depth (33) and never at full text, so E8/E10/E12 are partial by construction and no stage-2 assessment exists for any record. Any sentence in section 8 of the form 'the literature states/does not state X' is bounded by a screen that never read the 1,245 unresolved records. Ship it as a corpus record with the §13 limitations intact; do NOT let any downstream artefact cite its strand conclusions as a coverage claim about the literature. Two lower-order items for the record: uv.lock is untracked (git status '??'), so the declared environment is not clone-durable — immaterial here only because the scripts import stdlib only (json, io, os, re, pathlib, collections, unicodedata, html, sys), which I confirmed by running them under a bare CPython 3.11.9; and no digest is published for the 4.9 MB ka-screening-verdicts.jsonl, the artifact's largest machine-readable output.

**Residual risk that survives every fix in this round's list.** It is unchanged
in kind from round 1 and is a coverage risk, not a wording risk: 8,663 of 8,813
dispositions (98.3%) are statements about token co-occurrence in a title and
abstract; 700 records ended screening with eligibility UNDECIDED, concentrated in
exactly the transfer-clause class that feeds S4, the largest strand, and
outnumbering the 149 includes 4.7:1; 545 more are unextracted; and no full text
was read for any included record, so extraction fields E8/E10/E12 are partial by
construction. No prose repair changes any of that. The artifact now states each
of these at its true size, at the front of the document and at every synthesis
site, which is why the branches call it defensible — but the standing exposure is
that a downstream artefact will read a declared non-answer as a negative finding.
The research agenda that does not yet exist (SCOPE-2-3) is the place that risk
has to be managed, and its falsification tests must be written against the
strata this corpus never assessed.

## ai-assistance-statement

Per ICMJE Recommendations (updated January 2026) §V.A, and per
`~/.claude/rules/publishing.md` as adopted by this project's CLAUDE.md
reproducibility contract. AI is not an author of this record; the responsible
human is the operator named in the front matter.

- **Models used.** Claude Opus 5 (`claude-opus-5`), Anthropic, throughout: the
  lead orchestrator session, all five routed specialist audit branches
  (critical-reviewer high, scope-auditor medium, quant-auditor high,
  literature-check high, reproducibility-verifier medium), the adversarial
  refuter (high), and the trail-assembly agent that wrote this round section. No
  other model was used in this round.
- **Role.** `audit` for the five specialist branches (finding generation against
  the artifacts, the frozen protocol, the deliverable spec and the primary
  sources); `refute` for the adversarial gate (attempted disproof of every
  critical and major finding); `prose` for this trail's narrative sections;
  `code` for the re-execution work — the pipeline rebuilds, the pattern
  counterfactuals, the digest computations, the table re-derivations and the live
  registration-agency queries. No finding, refutation, count or digest in this
  record was accepted on model recall: every number reported as verified above
  was produced by executing a command or fetching a source in this round, except
  the four items literature-check could not execute, which are attributed to the
  branches that did.
- **Human oversight.** Sajan Koirala, operator, under whose review the verdict
  and the remediation set proceed. The delegation chain is recorded in
  `acted_on_behalf_of`.
- **Reproducibility log.** The audited artifact's own run is covered by
  `logs/reproducibility/repro_log_8f5b02d3bf61492b8bf9ae5214594f10.json`
  (SHA-256 `416d4d4891ffd9804f0276e91dc96d5c48460764722191ede10d5fbf476b94ee`,
  verified byte-exact this round) with sidecar
  `artifacts/runs/kalshi-arbitrage/8f5b02d3bf61492b8bf9ae5214594f10/sidecar.json`
  (SHA-256 `96c4134c03f247edc2837e178525a9f215fb8eeb2ab30ca3b9ac53a5e1d5647a`);
  both paths are gitignored and are therefore **untracked locators**, cited by
  digest per this project's CLAUDE.md reproducibility contract. This audit round
  emits its own ReproLog at `logs/reproducibility/repro_log_{run_id}.json`
  sequenced with the `/commit-with-provenance` step; its clone-durable digest is
  carried by that commit's `Repro-Log-Path:` / `Repro-Log-SHA256:` trailers, and
  the commit hash is to be recorded here as a dated addendum when it lands.
  Findings REPRODUCIBILITY-2-1/2-2 and QUANT-2-7/2-10 concern defects in the
  audited artifact's ReproLog, not in this trail's.

## immutability-and-retention

This trail and its two JSON sidecars — the round-1 payload in
[audit_trail_kalshi-arbitrage-review_2026-09-02.json](audit_trail_kalshi-arbitrage-review_2026-09-02.json)
(SHA-256 `fcad5133001899a700596842e1691a353d1e5375751683f5d72a2eb2cf395a4c`) and
the round-2 payload in
[audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json](audit_trail_kalshi-arbitrage-review_2026-09-02.round2.json)
(SHA-256 `2eb62d0a716b19ac0e6607f02d760fb30fdbe7231537474c12520a68fb51a4f0`), each holding its round verbatim per FAIR I1 — are committed to
the repository and are **append-only**, per 21 CFR 11.10(e): record changes must
not obscure previously recorded information. This round section was **appended**;
not one character of the round-1 front matter, findings table, refute-gate
entries, minors, verification, residual-risk, AI-assistance or
immutability sections was edited, and the round-1 sidecar is byte-identical to
the file whose digest the round-1 front matter binds. A round-3 section, if the
loop runs again under the 3-round cap (`rounds_completed: 2`, `rounds_cap: 3`,
`cap_reached: false`), appends below this one with its own sidecar. Corrections
to anything recorded in either round — including any correction to a digest, a
count, or a disposition in this section — are appended as a dated addendum that
identifies what it corrects and why; prior entries are never edited, overwritten
or deleted. Retention follows the repository's git history; the tracked files are
the durable record, and the front-matter digests bind this round to the exact
artifact states audited (HEAD `27d74738aa35ec1cdf1ec6915b50532e3620ea6f`,
`worktree_clean: false`, four artifact SHA-256s recorded above).
