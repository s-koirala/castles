---
type: research_agenda
slug: context-portability
date: 2026-08-21
status: open
corpus: none  # not yet commissioned
---

# Research agenda — context portability

**Question.** How should a markdown research document be compiled so that an LLM
agent working in a *different* directory can find it, load the right part of it,
and act on it correctly while doing statistical analysis, modelling, or coding —
and how would we know whether it worked?

**Why this thread matters beyond its own subject.** This is the first agenda in
the project that is not finance or trading infrastructure. Per
[the charter](../methodology/charter_castles_2026-08-21.md)
§"Falsification of commitment 1", the unbounded-domain claim is currently
supported by zero artifacts. This thread is a partial test of it: if the
five-step protocol and the falsification discipline can be executed here without
importing machinery the charter lacks, that is evidence for commitment 1. If it
cannot, that is evidence against. **Record which, explicitly, when this thread
produces its first result.**

**Standing hazard — the measurement problem is the same one as
[architecture §3](research_agenda_architecture_2026-08-21.md).** "Does providing
this document improve downstream performance" has the identical structure to
"does providing this forecast improve the trader's decisions": a treatment whose
effect runs through an agent's behaviour, no ground truth, and a noisy outcome.
Both require randomized evaluation and both are likely under-resolved at
realistic sample sizes. Neither should be answered by intuition, and neither
should be answered twice — whatever design works for one should be reused.

## 1. Document structure for machine retrieval

Open questions:

- **Position effects.** Model accuracy degrades for information placed in the
  middle of a long context ([Liu et al. 2023](https://arxiv.org/abs/2307.03172),
  "Lost in the Middle", TACL). If real and current, this makes document *order*
  a design variable, not a stylistic one, and argues for short documents over
  long ones regardless of total budget. Whether the effect persists in current
  long-context models is an empirical question with a moving answer — check the
  current generation, do not cite 2023 as settled.
- **Frontmatter as routing metadata.** What minimal schema lets a consuming
  agent decide *whether to read further* without reading the body: `type`,
  `slug`, `date`, `status`, evidence tier, applicability scope, staleness date.
  The charter already uses several of these; whether they are the right ones is
  untested.
- **Chunk boundaries.** If a document is retrieved rather than inlined, headings
  determine chunk boundaries. This makes heading granularity a retrieval
  parameter. What granularity, and selected against what objective?
- **Semantic density vs. redundancy.** Prose written for a human reader repeats
  itself for emphasis. Whether that redundancy helps or wastes budget for a
  machine reader is untested and cheap to test.
- **Assertion form.** Does an agent act more reliably on "MUST/SHOULD" (RFC 2119)
  than on descriptive prose? The charter and CLAUDE.md already assume so.

**Falsification:** construct a task set with a verifiable ground truth (e.g.
"apply the correct multiple-testing correction given this design"), and run
matched agents against the same content rendered in structurally different
forms. If task accuracy does not differ across forms beyond a pre-stated MDES at
a pre-stated target power, document structure does not matter at this margin and
this branch closes. State the MDES **before** collecting, per charter step 2 —
this branch is the most likely of the four to be underpowered.

## 2. Reference mechanism — how a document reaches the context window

Open questions:

- **The budget asymmetry.** Content in a `CLAUDE.md` is paid on *every* request
  in that project; content retrieved on demand is paid only when loaded. This is
  a measurable cost difference, and it argues that the always-loaded tier should
  hold routing information rather than substance.
- **Progressive disclosure as an architecture.** The skill mechanism already
  implements three tiers — a description scanned always, a body loaded on
  invocation, linked files loaded on demand. Whether research documents should
  adopt the same shape, and where the tier boundaries fall, is the branch's
  central design question.
- **Inline vs. link vs. retrieve.** Three mechanisms with different failure
  modes: inlining bloats and goes stale; linking depends on the agent choosing
  to follow; retrieval depends on the query matching. Which fails how often is
  measurable.
- **Import mechanisms.** `CLAUDE.md` supports `@path` imports; MCP exposes
  resources; skills carry bundled files. Each has different portability
  properties across directories.
- **Retrieval-augmented generation as the alternative**
  ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)) — and whether it earns
  its complexity at the scale of one researcher's document corpus, where the
  whole corpus may fit in a context window.
- **Information scent.** A link is followed only if its surrounding text
  signals what lies behind it. What makes a reference legible enough to follow is
  a findability question with an existing human-factors literature that may or
  may not transfer.

**Falsification:** instrument whether linked documents are actually opened.
Give an agent a task solvable only with content behind a link, vary the link's
surrounding description, and measure open-rate and task success. If open-rate is
near zero regardless of description, linking is not a viable mechanism for this
corpus and the branch collapses to inline-or-retrieve.

## 3. Cross-directory portability and staleness

Open questions:

- **Path resolution.** A document referencing `../../failure_log.md` breaks when
  copied elsewhere. Candidate mechanisms — copy, symlink, git submodule, git
  subtree, package install, a central store addressed absolutely — each trade
  freshness against isolation. Which is right likely depends on whether the
  consuming project needs to *pin* the document version.
- **Staleness as the dominant failure mode.** A document that described the code
  correctly six months ago and now does not is worse than no document, because
  it is confidently wrong. Candidate mitigations: an explicit `valid_as_of`
  date, a checksum against the artifact described, or a CI check. Which
  detects drift soonest is testable.
- **Provenance travelling with content.** When a document moves, its evidence
  tier, verification status, and date must move with it. Frontmatter achieves
  this only if the consuming agent reads frontmatter — see branch 1.
- **Namespace collisions.** Two projects each carrying a `charter.md` or an
  `ADR-0001` produce ambiguous references. This already occurs in this
  repository, where `ADR-0001` denotes two different documents depending on
  scope.
- **Verification status as a first-class field.** A consuming agent should be
  able to see that a claim is `pending` rather than settled — the same
  discipline the charter's evidence hierarchy imposes internally.

**Falsification:** take a document from this repository, install it into an
unrelated project by each candidate mechanism, and check whether every internal
reference resolves and every provenance field survives. A mechanism that loses
provenance or breaks references is eliminated. This test cannot fail to be
informative and is the cheapest in the agenda — run it first.

## 4. Effectiveness measurement

The hard branch, and the one the other three depend on.

Open questions:

- **What is the outcome?** Task success against a verifiable ground truth is the
  only defensible endpoint. Self-reported helpfulness and human impression are
  not, for the reasons recorded in
  [failure_log.md](../../failure_log.md) F003.
- **What is the unit of randomization?** Task, session, or document version.
  Sessions are correlated; tasks may not be exchangeable.
- **Sample size.** Agent task outcomes are noisy and the plausible effect is
  small. The MDES for a realistic design is very likely larger than the effect
  of interest, which would make the honest conclusion "this cannot be measured
  at the scale available" — a legitimate and useful result under the charter.
- **Contamination.** An agent that has already seen a document in one session
  may carry it forward, breaking the on/off contrast.
- **Construct validity.** "The document helped" is not directly observable. What
  is observable is task accuracy, tokens spent, and tool-call count — proxies
  whose relationship to the construct needs stating.

**Falsification:** compute the MDES for the proposed design under a stated
target power and a sourced plausible effect **before running anything**. If the
MDES exceeds any plausible document effect, state that plainly, close the
measurement branch, and downgrade branches 1–3 from *findings* to *design
rationale*. That is an honest position and is preferable to running an
underpowered study and reading noise. This falsification can genuinely fire and
would close the most important branch in the agenda — which is what makes it a
real test rather than a validation step.

## Cross-branch open questions

- Is the right unit a *document* at all? The alternative is an executable
  artifact — a skill, a lint rule, a test — which cannot go stale silently
  because it fails loudly. Where a research finding can be compiled into a check
  rather than described in prose, that may dominate every option in branch 2.
- Does the answer differ by task type? Statistical-method selection, code
  generation, and literature synthesis may have different optimal document
  shapes, in which case there is no single answer and the deliverable is a
  decision table rather than a recommendation.

## Verification status

Citations here are **unverified**. Liu et al. 2023 and Lewis et al. 2020 are
stated from prior knowledge and have not been checked against their primary
sources by the `literature-check` branch. Position-effect findings in particular
are model-generation-dependent and may not hold for current models — treat as a
hypothesis to test, not a result to build on.
