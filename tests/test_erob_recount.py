"""Re-derive the ER-RoB v1 domain-concern column and check it against the shipped review.

WHAT THIS TEST IS FOR
---------------------
The 2026-09-02 repository audit recorded VG-16: no committed entrypoint re-derives any
number the project reports. The most computation-like claim in the corpus is the ER-RoB v1
appraisal table in section 6 of the explosive-regime review — 72 rows, nine signalling-question
cells and eight domain-concern cells each. This module gives that claim a runnable reproduce
target.

Nothing here restates the shipped table. Every value on the left-hand side of every assertion
is computed from the two extraction logs

    docs/literature/search_logs/explosive-regime/se-extraction-primary.jsonl
    docs/literature/search_logs/explosive-regime/se-extraction-recheck.jsonl

by the rules frozen in the protocol and its append-only addendum. The right-hand side is what
the review and the amendments publish. A divergence is a finding, not a licence to widen the
expected set.

THE RULES ENCODED HERE, AND WHERE EACH COMES FROM
-------------------------------------------------
1. Q -> D concern rule. Protocol section 6 ("Risk of bias / appraisal instrument"):
   "'no' or 'unclear' on any question in a domain raises that domain's concern".
2. Domain-to-question map. Protocol addendum A8, which states it verbatim as
   "D1 from Q1, D2 from Q2, D3 from Q3 and Q4, D4 from Q5, D5 from Q6, D6 from Q7,
   D7 from Q8, D8 from Q9". Parsed from A8 rather than retyped, so an edit to the
   amendment is caught instead of silently ignored.
3. `partial` handling. CONVENTION, named: **amendment A7's CONVENTION**. Protocol section 6
   declares a three-level scale (yes / no / unclear); execution used four by adding `partial`,
   and section 6's rule is silent on the added level. A7 fixes the convention that `partial`
   "is treated as not-`yes` and therefore raises the domain's concern", and restricts it to
   the rule-derived domain column — which is the only column this module derives. Applied at
   `_domain_is_raised`.
4. Primary/recheck disagreement. CONVENTION, named: **review section 2.8's CONVENTION**
   (registered as amendment A6). Where the two extraction passes answer the same question
   differently, the appraisal records the more conservative answer under the order
   `no` > `unclear` > `partial` > `yes`. Applied at `_resolve_pair`. The ordering string is
   parsed out of section 2.8, not retyped.
5. Expected divergences. Amendment A8, which enumerates the recorded departures of the
   shipped domain column from the rule-derived one. Parsed from A8; see the shortfall note
   below for what A8 does and does not pin down.
6. Domain-concern vocabulary. Protocol section 6, which declares the instrument's judgments
   as `low / high / unclear`, cross-checked against the review's own section 6 legend, which
   declares the same three levels for the D columns published there. Both are parsed, not
   retyped, and `divergent_cells` refuses any cell outside them (see FAIL-CLOSED below).

FAIL-CLOSED CLASSIFICATION OF THE DOMAIN COLUMN
-----------------------------------------------
A census of divergences that silently drops a cell it cannot classify returns a short count,
and a short count reconciles against A8 exactly as a correct one does. `divergent_cells`
therefore places every cell of every D column and raises on the three ways a cell can resist
placement, naming the record, the domain and the offending value: a label outside the declared
scale (a case variant, a typo, an unstripped glyph, a level a successor instrument adds); a
recorded judgment where the rule finds the domain not assessable; and a not-assessable cell
where the rule reaches a judgment. The last two are the same defect on the other axis — the
review and the rule disagreeing about whether the cell exists — and A8 enumerates no such
category, so neither can be reconciled away. The vocabulary constraint is additionally stated
on its own, as a property of the inputs, by
`test_every_domain_concern_cell_is_a_declared_scale_level`, over the review's column and over
the primary log's raw `domain_concerns` field.

Every scalar this module compares against is parsed from one of those documents.
`test_no_free_numeric_constants` asserts that as a property of the source file, over numeric
literals AND over digits written inside string literals — a figure baked into a regex anchor or
a message is the same defect as one written as an `int`, and is harder to see. The only literals
it admits are the two allow-lists at the foot of this module: structural indices (`Match.group`
numbers and the like) and the document anchors, source filenames and section citations that
address the inputs. Both are keyed by the definition the literal is written in, so a licence
granted for one use does not travel to another, and every member carries an inline comment
naming what authorises it. Docstrings are exempt, and must be — this one and the guard's own
have to be able to name the figures the guard forbids.

SHORTFALLS IN THE INPUTS, RECORDED RATHER THAN PAPERED OVER
-----------------------------------------------------------
(a) `se-extraction-primary.jsonl` stores each signalling-question answer as one free-text
    string whose first token is the answer ("yes - H0 and deterministic spec stated; ...").
    There is no separate structured answer field. This module parses the leading token and
    `test_every_answer_parses_to_a_declared_scale_level` fails loudly if any cell does not
    begin with a scale level, rather than skipping it.
(b) `se-extraction-recheck.jsonl` carries `rob_q1_7` only. Q8 and Q9 exist in the primary pass
    alone, which is why the 12 recheck-only records show `n/a` for those two questions and why
    the Q8/Q9 denominator is smaller than the Q1-Q7 one. The module derives both denominators
    rather than assuming either.
(c) The recheck pass records no domain-concern judgment at all. For the 12 recheck-only
    records there is therefore no independently recorded D judgment to compare the rule
    against; the review's D cells for those rows are already rule-derived. Consistently,
    A8's divergence set contains no recheck-only record — but that consistency is an
    observation here, not something this module can independently verify.
(d) A8 enumerates its divergences as PER-DOMAIN COUNTS, not as record ids: "31 domain cells
    ... (D3 13, D4 6, D5 2, D6 1) ... (D3 8, D4 1) ... 13 cells run the other way
    (D3 1, D4 7, D5 5)". So "the recorded divergence set" is only defined up to a per-domain
    profile at the amendment level. Two tests together close that gap:
    `test_divergence_profile_matches_amendment_a8` checks the derived profile against A8's
    counts, and `test_no_divergent_cell_outside_the_marked_set` checks cell for cell against
    the review's own `section-sign` / `pilcrow` markers, which are the review's published claim
    about WHICH cells diverge. Either an extra divergent cell or a missing one fails at least
    one of the two.
(e) Section 2.8's CONVENTION takes the minimum over the two passes, so on a Q1-Q7 cell the
    two passes both answered, a change to the primary answer in the LESS concerning direction
    is absorbed when the recheck already holds the more concerning answer, and this module
    cannot see it. Established by mutation, not by inspection: flipping `eru-0131` Q5 from
    `no` to `yes` leaves every test passing, because the recheck pass answers that cell `no`;
    the same flip in the other direction, and any flip on Q8/Q9 where no second pass exists,
    fails immediately. The blind spot is a property of the declared resolution rule, not of
    the derivation — but it bounds what a green run here licenses.

WHAT THIS DOES NOT CHECK
------------------------
Whether the recorded Q answers are faithful to the source texts. That is the source-text
adjudication protocol section 4.3 requires and amendment A6 records as never having run. This
module checks arithmetic and rule application over the recorded answers; it cannot and does not
convert a convention-resolved appraisal into an adjudicated one.
"""

from __future__ import annotations

import ast
import json
import re
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from typing import TypedDict

import pytest

# --- repo-relative locations (this file lives in tests/, so the root is one level up) ---
ENCODING = "utf-8"  # one site for the codec name, so the guard below has one thing to license
REPO_ROOT = Path(__file__).resolve().parents[1]
SEARCH_LOGS = REPO_ROOT / "docs" / "literature" / "search_logs" / "explosive-regime"
PRIMARY_JSONL = SEARCH_LOGS / "se-extraction-primary.jsonl"
RECHECK_JSONL = SEARCH_LOGS / "se-extraction-recheck.jsonl"
REVIEW_MD = REPO_ROOT / "docs" / "literature" / "lit_review_explosive-regime-dating_2026-08-24.md"
PROTOCOL_MD = REPO_ROOT / "docs" / "methodology" / "protocol_explosive-regime-review_2026-08-24.md"

# --- document anchors and source citations, each named once ---
# Same rationale as `ENCODING` above: one site per anchor, so the magic-figure guard licenses
# each section number once rather than once per definition that cites it.
PROTOCOL_SECTION_6 = "## 6. Risk of bias"  # the span carrying the Q->D rule and the concern scale
PROTOCOL_SECTION_7 = "## 7. Synthesis plan"  # the next heading, which bounds that span
PROTOCOL_SCALE_SOURCE = "protocol section 6's declared domain-concern scale"
REVIEW_LEGEND_SOURCE = "the review's section 6 legend for the D columns"

# --- literal characters the review's section 6 legend assigns a meaning ---
# (glyphs, not thresholds: each is defined in that legend and carries no numeric content)
DAGGER = "†"  # section 2.8 resolution raised this cell
DOUBLE_DAGGER = "‡"  # single-pass record
SECTION_SIGN = "§"  # recorded `low` where the rule raises  (A8, lenient direction)
PILCROW = "¶"  # recorded raised where the rule leaves `low` (A8, strict direction)
EM_DASH = "—"  # twin record, appraised under its carrier
MIDDLE_DOT = "·"  # D-rule "not assessable"
CELL_MARKERS = DAGGER + DOUBLE_DAGGER + SECTION_SIGN + PILCROW

NOT_ASSESSABLE_CELL = frozenset({EM_DASH, "n/a", ""})
RAISED_CONCERN_LABELS = frozenset({"unclear", "high"})
LOW_CONCERN_LABEL = "low"
# The instrument's whole domain-concern vocabulary, against which `divergent_cells` fails closed.
# The PARTITION is this module's encoding and is argued: protocol section 6 says concern is
# "raised" without saying to what level, so `low` is the not-raised level by name and the other
# two are the raised ones. The EXTENT is not this module's to assert —
# `test_frozen_rule_texts_are_unchanged` checks this union against the scale the protocol declares
# for the instrument AND against the scale the review's own legend declares for the column read
# here. A level a successor instrument adds therefore fails at that guard, and a cell carrying it
# fails at the classifier, instead of being silently reclassified as non-divergent.
DOMAIN_CONCERN_SCALE = RAISED_CONCERN_LABELS | {LOW_CONCERN_LABEL}
RULE_LOW = "L"
RULE_RAISED = "R"
RULE_NOT_ASSESSABLE = MIDDLE_DOT

QUESTIONS = tuple(f"Q{i}" for i in range(1, 10))
DOMAINS = tuple(f"D{i}" for i in range(1, 9))

TABLE_HEADER_PREFIX = "| # | rec | study | tier | I2 | Q1 |"
TABLE_COLUMNS = (
    "row",
    "rec",
    "study",
    "tier",
    "i2",
    *(q.lower() for q in QUESTIONS),
    *(d.lower() for d in DOMAINS),
    "depth",
    "d_rule",
)


# ----------------------------------------------------------------------------------
# return shapes
# ----------------------------------------------------------------------------------
# Declared rather than left as `dict[str, ...]`: the loaders return heterogeneous mappings whose
# members callers use for member-specific behaviour (set difference on `unappraised`, `Counter`
# equality on `strict`), which an un-narrowed union or a plain `dict` value type forbids.
class PrimaryPass(TypedDict):
    """What `load_primary` returns. Two of the four members are sets, not dicts."""

    answers: dict[str, dict[str, str]]
    recorded_domains: dict[str, dict[str, str]]
    unappraised: set[str]
    twins: set[str]


class A8Divergences(TypedDict):
    """What `read_a8_divergence_enumeration` returns: A8's counts, split by direction."""

    lenient_total: int
    lenient_rule_decided_total: int
    lenient_rule_decided: Counter
    lenient_convention_decided_total: int
    lenient_convention_decided: Counter
    strict_total: int
    strict: Counter


class A12Accounting(TypedDict):
    """What `read_a12_partial_accounting` returns: A12's `partial` numerator and denominator.

    `total` is derived here by summing A12's own per-question split; `stated_partial_total` is
    the numerator A12 states in prose. They are separate members precisely so that
    `test_partial_extension_matches_amendments_a7_and_a12` can assert they agree — a
    disagreement is a divergence to report, not a parse failure to swallow.
    """

    by_question: Counter
    total: int
    stated_partial_total: int
    answered_cells: int
    q1_q7_records: int
    q1_q7_questions: int
    q8_q9_records: int
    q8_q9_questions: int


# ----------------------------------------------------------------------------------
# document helpers
# ----------------------------------------------------------------------------------
def _flatten(text: str) -> str:
    """Collapse whitespace so a regex is indifferent to the source's line wrapping.

    Blockquote markers are dropped first. Review section 2.8 states its CONVENTION inside a
    blockquote whose ordering string wraps across two lines, so the continuation line's own
    `>` marker would otherwise land in the middle of the `partial` > `yes` comparison.
    """
    return re.sub(r"\s+", " ", re.sub(r"(?m)^[ \t]*>[ \t]?", "", text))


def _slice(text: str, start_marker: str, end_marker: str) -> str:
    """Return the span of `text` from `start_marker` up to the next `end_marker`."""
    start = text.index(start_marker)
    return text[start : text.index(end_marker, start)]


def _amendment(protocol_text: str, name: str, next_name: str) -> str:
    return _flatten(_slice(protocol_text, f"### {name} ", f"### {next_name} "))


def _counts_by_domain(spec: str) -> Counter:
    """Parse an A8 enumeration fragment such as 'D3 13, D4 6, D5 2, D6 1'."""
    return Counter({d: int(n) for d, n in re.findall(r"(D\d)\s+(\d+)", spec)})


def _counts_by_question(spec: str) -> Counter:
    """Parse an A12 enumeration fragment such as 'Q1 2, Q2 3, ... Q9 29'."""
    return Counter({q: int(n) for q, n in re.findall(r"(Q\d)\s+(\d+)", spec)})


def _require(pattern: str, text: str, what: str) -> re.Match:
    match = re.search(pattern, text)
    assert match is not None, f"could not read {what} from its source document"
    return match


# ----------------------------------------------------------------------------------
# rules, read from the frozen protocol and its addendum
# ----------------------------------------------------------------------------------
def read_domain_question_map(protocol_text: str) -> dict[str, tuple[str, ...]]:
    """Domain-to-question map, parsed verbatim from amendment A8.

    A8 restates protocol section 6's map inline while recording the departure from
    section 6's Q->D rule, which makes it the one place the map appears as parseable prose.
    """
    a8 = _amendment(protocol_text, "A8", "A9")
    fragment = _require(r"\(D1 from Q1[^)]*\)", a8, "A8's domain-to-question map").group(0)
    return {
        domain: tuple(re.findall(r"Q\d", questions))
        for domain, questions in re.findall(r"(D\d) from ((?:Q\d)(?: and Q\d)*)", fragment)
    }


def _protocol_section_6(protocol_text: str) -> str:
    """Protocol section 6's text, flattened. One span, two readers."""
    return _flatten(_slice(protocol_text, PROTOCOL_SECTION_6, PROTOCOL_SECTION_7))


def read_domain_concern_scale(protocol_text: str) -> frozenset[str]:
    """The domain-concern vocabulary the ER-RoB v1 instrument declares.

    Protocol section 6 states it as a parenthesised slash-separated list while declaring the
    instrument: "domain-level concern judgments (low / high / unclear)". The vocabulary the
    classifier fails closed against is therefore read from the instrument that declares it,
    not introduced here as a constant.
    """
    fragment = _require(
        r"domain-level concern judgments \(([^)]*)\)",
        _protocol_section_6(protocol_text),
        PROTOCOL_SCALE_SOURCE,
    ).group(1)
    return frozenset(level.strip().lower() for level in fragment.split("/"))


def read_review_domain_concern_legend(review_text: str) -> frozenset[str]:
    """The vocabulary the review's section 6 legend declares for the D columns it publishes.

    A separate claim by a separate document from `read_domain_concern_scale`: the protocol
    declares the instrument's scale, this legend declares the scale of the actual column
    `divergent_cells` reads. Asserted equal at the frozen-text guard rather than assumed so,
    because a widening of either alone is exactly the drift the fail-closed classifier exists
    to catch.
    """
    fragment = _require(
        r"Domain concerns \(the `D\d`[^`]*`D\d` columns\): ((?:`[a-z]+` / )+`[a-z]+`)",
        _flatten(review_text),
        REVIEW_LEGEND_SOURCE,
    ).group(1)
    return frozenset(re.findall(r"`([a-z]+)`", fragment))


def read_resolution_order(review_text: str) -> tuple[str, ...]:
    """Conservative ordering for primary/recheck disagreement.

    CONVENTION, named: review section 2.8's CONVENTION, registered as protocol amendment A6.
    Parsed from section 2.8 so that an edit to the convention breaks the test.
    """
    section = _flatten(_slice(review_text, "### 2.8 Resolution rule", "### 2.9 Synthesis"))
    fragment = _require(
        r"the more conservative answer under the order ((?:`[a-z]+` > )+`[a-z]+`)",
        section,
        "section 2.8's resolution ordering",
    ).group(1)
    return tuple(re.findall(r"`([a-z]+)`", fragment))


def read_a8_divergence_enumeration(protocol_text: str) -> A8Divergences:
    """The recorded departures of the shipped domain column from the rule-derived one (A8)."""
    a8 = _amendment(protocol_text, "A8", "A9")
    lenient_total = int(
        _require(r"\*\*(\d+) domain cells are recorded `low`", a8, "A8's lenient total").group(1)
    )
    decided = _require(
        r"(\d+) of them with a `no` or `unclear` input \(([^)]*)\)",
        a8,
        "A8's rule-decided lenient subset",
    )
    convention = _require(
        r"and (\d+) whose only non-`yes` input is `partial` \(([^)]*)\)",
        a8,
        "A8's A7-CONVENTION-decided lenient subset",
    )
    strict = _require(
        r"\*\*(\d+) cells run the other way\*\*[^(]*\(([^)]*)\)",
        a8,
        "A8's strict-direction subset",
    )
    return A8Divergences(
        lenient_total=lenient_total,
        lenient_rule_decided_total=int(decided.group(1)),
        lenient_rule_decided=_counts_by_domain(decided.group(2)),
        lenient_convention_decided_total=int(convention.group(1)),
        lenient_convention_decided=_counts_by_domain(convention.group(2)),
        strict_total=int(strict.group(1)),
        strict=_counts_by_domain(strict.group(2)),
    )


def read_a12_partial_accounting(protocol_text: str) -> A12Accounting:
    """The `partial` extension's numerator, split and denominator.

    A7 records the extension but carries a denominator that A12 corrects; the addendum is
    append-only, so A12 is the live figure and is what this reads.

    Every figure here is CAPTURED, never used as an anchor. A12's sentence reads
    "<numerator> of <denominator> = <rate>", and its assessable-cell arithmetic reads
    "<records> × <questions> (Q1-Q7) + <records> × <questions> (Q8, Q9)". Anchoring either
    pattern on one of its own figures would hardcode a published number inside the parser that
    reads its sibling, and would turn a corrected figure into "could not read ..." — an
    input-parse error wearing the costume of a document-shape problem — instead of the
    divergence it is. The multiplication sign is matched literally rather than by `.`, which
    would accept any character in its place.
    """
    a12 = _amendment(protocol_text, "A12", "A13")
    split = _require(r"per-question split \(([^)]*)\)", a12, "A12's per-question `partial` split")
    deviation = _require(r"\*\*(\d+) of (\d+) = ", a12, "A12's corrected response-scale deviation")
    assessable = _require(
        r"(\d+) × (\d+) \(Q1-Q7\) \+ (\d+) × (\d+) \(Q8, Q9\)",
        a12,
        "A12's assessable denominators",
    )
    by_question = _counts_by_question(split.group(1))
    return A12Accounting(
        by_question=by_question,
        total=sum(by_question.values()),
        stated_partial_total=int(deviation.group(1)),
        answered_cells=int(deviation.group(2)),
        q1_q7_records=int(assessable.group(1)),
        q1_q7_questions=int(assessable.group(2)),
        q8_q9_records=int(assessable.group(3)),
        q8_q9_questions=int(assessable.group(4)),
    )


def read_review_corpus_shape(review_text: str) -> dict[str, int]:
    """Row count and exclusion-class sizes, parsed from review sections 6 and 6.1."""
    header = _flatten(_slice(review_text, "## 6. Appraisal", TABLE_HEADER_PREFIX))
    profile = _flatten(_slice(review_text, "### 6.1 Domain concern profile", "## 7. Synthesis"))
    return {
        "rows": int(
            _require(
                r"\*\*One row per included record: (\d+) rows\*\*",
                header,
                "the section 6 row count",
            ).group(1)
        ),
        "twins": int(
            _require(r"(\d+) are twins", profile, "the twin count").group(1),
        ),
        "no_fulltext": int(
            _require(
                r"(\d+) more have no full text at any stage", profile, "the no-full-text count"
            ).group(1)
        ),
        "recheck_only": int(
            _require(
                r"(\d+) further records were read only at the recheck pass",
                profile,
                "the recheck-only count",
            ).group(1)
        ),
    }


# ----------------------------------------------------------------------------------
# input loaders
# ----------------------------------------------------------------------------------
_ANSWER = re.compile(r"^\s*(yes|no|unclear|partial)\b", re.IGNORECASE)


def _leading_answer(cell: str, where: str) -> str:
    match = _ANSWER.match(cell)
    assert match is not None, f"{where}: answer prose does not begin with a scale level: {cell!r}"
    return match.group(1).lower()


def load_primary(path: Path) -> PrimaryPass:
    """Primary extraction pass: Q1-Q9 answers and the extractor's own domain judgments.

    A row whose `rob` is a sentence rather than an object is a record the primary pass could
    not appraise (no full text); it contributes no answers. A row carrying `twin_of` and no
    `rob` is a same-work twin, appraised under its carrier.

    `unappraised` and `twins` are SETS, not dicts: callers difference and length them
    (`primary["unappraised"] - rechecked`, `len(primary["twins"])`), which is why the return
    shape is declared as a `TypedDict` rather than flattened to `dict[str, dict]`.
    """
    answers: dict[str, dict[str, str]] = {}
    recorded: dict[str, dict[str, str]] = {}
    unappraised: set[str] = set()
    twins: set[str] = set()
    for line in path.read_text(encoding=ENCODING).splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rid, rob = row["id"], row.get("rob")
        if isinstance(rob, dict):
            answers[rid] = {q: _leading_answer(rob[q], f"{rid} {q}") for q in QUESTIONS}
            recorded[rid] = {d: str(v).strip().lower() for d, v in rob["domain_concerns"].items()}
        elif isinstance(rob, str):
            unappraised.add(rid)
        elif "twin_of" in row:
            twins.add(rid)
    return PrimaryPass(
        answers=answers,
        recorded_domains=recorded,
        unappraised=unappraised,
        twins=twins,
    )


def load_recheck(path: Path) -> dict[str, dict[str, str]]:
    """Dual re-extraction pass. Field `rob_q1_7` carries Q1-Q7 only (see shortfall (b))."""
    answers: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding=ENCODING).splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rob = row.get("rob_q1_7")
        if isinstance(rob, dict):
            answers[row["id"]] = {
                q: _leading_answer(str(cell["a"]), f"{row['id']} {q} (recheck)")
                for q, cell in rob.items()
            }
    return answers


def parse_appraisal_table(path: Path) -> list[dict[str, str]]:
    """Parse the section 6 appraisal table out of the review markdown.

    Pipes escaped as `\\|` inside a cell (the I2 column uses them for alternatives) are not
    column separators; splitting on unescaped pipes only is what keeps those rows aligned.
    """
    rows: list[dict[str, str]] = []
    inside = False
    for raw in path.read_text(encoding=ENCODING).splitlines():
        line = raw.strip()
        if line.startswith(TABLE_HEADER_PREFIX):
            inside = True
            continue
        if not inside:
            continue
        if not line.startswith("|"):
            break
        body = line.removeprefix("|").removesuffix("|")
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", body)]
        if set(cells[0]) <= set("-: "):  # the markdown alignment row
            continue
        assert len(cells) == len(TABLE_COLUMNS), f"unexpected column count in row {cells[0]!r}"
        rows.append(dict(zip(TABLE_COLUMNS, cells, strict=True)))
    return rows


def strip_markers(cell: str) -> str:
    """Drop the section 6 legend's glyphs, leaving the cell's value."""
    return "".join(ch for ch in cell if ch not in CELL_MARKERS).strip()


# ----------------------------------------------------------------------------------
# the rules themselves
# ----------------------------------------------------------------------------------
def _resolve_pair(primary: str | None, recheck: str | None, order: tuple[str, ...]) -> str | None:
    """CONVENTION (review section 2.8, amendment A6): keep the more conservative answer."""
    candidates = [a for a in (primary, recheck) if a is not None]
    if not candidates:
        return None
    return min(candidates, key=order.index)


def resolve_answers(
    record_ids, primary: dict, recheck: dict, order: tuple[str, ...]
) -> dict[str, dict[str, str | None]]:
    """The appraisal's Q cells, rebuilt from the two passes under section 2.8's CONVENTION."""
    resolved = {}
    for rid in record_ids:
        row = {}
        for q in QUESTIONS:
            row[q] = _resolve_pair(primary.get(rid, {}).get(q), recheck.get(rid, {}).get(q), order)
        resolved[rid] = row
    return resolved


def _domain_is_raised(answers: list[str]) -> bool:
    """Protocol section 6, with amendment A7's CONVENTION.

    Section 6: "'no' or 'unclear' on any question in a domain raises that domain's concern".
    A7's CONVENTION extends that to the fourth level execution added: `partial` "is treated as
    not-`yes` and therefore raises the domain's concern". Both reduce to the same predicate —
    the domain stays low only when every answered question in it is `yes` — so the rule is
    written that way rather than as a list of raising levels, which would need a membership
    decision for any level a successor instrument adds.
    """
    return not all(answer == "yes" for answer in answers)


def derive_domain_rule(resolved_row: dict[str, str | None], qd_map: dict) -> str:
    """One character per domain, in the section 6 legend's `L` / `R` / middle-dot encoding.

    The encoding is binary by construction: protocol section 6 says concern is "raised" and
    does not say to what level, so `R` is deliberately not split into `unclear` and `high`.
    """
    out = []
    for domain in DOMAINS:
        answers = [resolved_row[q] for q in qd_map[domain] if resolved_row[q] is not None]
        if not answers:
            out.append(RULE_NOT_ASSESSABLE)
        else:
            out.append(RULE_RAISED if _domain_is_raised(answers) else RULE_LOW)
    return "".join(out)


def divergent_cells(table: list[dict], resolved: dict, qd_map: dict) -> dict[str, list[tuple]]:
    """Cells where the shipped domain judgment and the rule-derived one disagree.

    Both directions are collected separately because A8 counts them separately and treats the
    lenient one — recorded `low` where the rule raises — as the direction that matters.

    THIS CLASSIFIER FAILS CLOSED, and the reason is the whole point of the module. A census of
    divergences that silently drops a cell it cannot place returns a short count, and a short
    count reconciles against A8 exactly as a correct one does: both
    `test_divergence_profile_matches_amendment_a8` and
    `test_no_divergent_cell_outside_the_marked_set` would stay green over an incomplete census.
    So every cell of every D column is placed, and the three ways a cell can fail to be
    placeable each raise, naming the record, the domain and the offending value:

    (i)   a domain-concern label outside the scale the protocol and the review's legend both
          declare — a case variant, a typo, an unstripped glyph, or a level a successor
          instrument adds;
    (ii)  a recorded judgment where the rule finds the domain not assessable;
    (iii) a not-assessable cell where the rule reaches a judgment.

    (ii) and (iii) are the same defect as (i) on the other axis: the review and the rule
    disagree about whether the cell exists at all, which is a divergence of a kind A8 does not
    enumerate and therefore cannot be reconciled away. Past those three guards the cross of
    `rule in {L, R}` with `recorded in DOMAIN_CONCERN_SCALE` is exhausted by the two branches
    below plus agreement, so nothing falls through unexamined.
    """
    lenient, strict = [], []
    for row in table:
        rule = derive_domain_rule(resolved[row["rec"]], qd_map)
        for index, domain in enumerate(DOMAINS):
            recorded = strip_markers(row[domain.lower()])
            where = f"{row['rec']} {domain}"
            assessable = rule[index] != RULE_NOT_ASSESSABLE
            if recorded in NOT_ASSESSABLE_CELL:
                assert not assessable, (
                    f"{where}: the review records no domain judgment ({recorded!r}) where the "
                    f"rule reaches one ({rule[index]!r}), so the cell is absent from the "
                    f"divergence census"
                )
                continue
            assert recorded in DOMAIN_CONCERN_SCALE, (
                f"{where}: domain-concern cell outside {PROTOCOL_SCALE_SOURCE} "
                f"{sorted(DOMAIN_CONCERN_SCALE)}: {recorded!r}"
            )
            assert assessable, (
                f"{where}: the review records {recorded!r} where the rule finds the domain not "
                f"assessable ({rule[index]!r}), so the cell is absent from the divergence census"
            )
            if rule[index] == RULE_RAISED and recorded == LOW_CONCERN_LABEL:
                lenient.append((row["rec"], domain))
            elif rule[index] == RULE_LOW and recorded in RAISED_CONCERN_LABELS:
                strict.append((row["rec"], domain))
    return {"lenient": lenient, "strict": strict}


# ----------------------------------------------------------------------------------
# fixtures
# ----------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def review_text() -> str:
    return REVIEW_MD.read_text(encoding=ENCODING)


@pytest.fixture(scope="module")
def protocol_text() -> str:
    return PROTOCOL_MD.read_text(encoding=ENCODING)


@pytest.fixture(scope="module")
def table() -> list[dict[str, str]]:
    return parse_appraisal_table(REVIEW_MD)


@pytest.fixture(scope="module")
def primary() -> PrimaryPass:
    return load_primary(PRIMARY_JSONL)


@pytest.fixture(scope="module")
def recheck() -> dict:
    return load_recheck(RECHECK_JSONL)


@pytest.fixture(scope="module")
def qd_map(protocol_text: str) -> dict:
    return read_domain_question_map(protocol_text)


@pytest.fixture(scope="module")
def resolved(table, primary, recheck, review_text) -> dict:
    order = read_resolution_order(review_text)
    return resolve_answers([r["rec"] for r in table], primary["answers"], recheck, order)


# ----------------------------------------------------------------------------------
# tests
# ----------------------------------------------------------------------------------
def test_frozen_rule_texts_are_unchanged(protocol_text: str, review_text: str):
    """Guard: the rules encoded above are the rules the sources state.

    Without this, an edit to protocol section 6, A7 or section 2.8 would leave the module
    quietly enforcing a superseded rule and still passing.

    The scale checks are the other half of `divergent_cells`' fail-closed classifier. That
    classifier refuses a domain-concern label outside `DOMAIN_CONCERN_SCALE`; these two
    assertions are what stop `DOMAIN_CONCERN_SCALE` from being a private opinion about the
    instrument. The protocol declares the scale for the instrument, the review's legend declares
    it for the column actually read, and the two are checked against each other as well as
    against this module — so a level added to either document fails here, loudly, rather than
    reaching the classifier as an unrecognised cell.
    """
    section6 = _protocol_section_6(protocol_text)
    assert (
        '"no" or "unclear" on any question in a domain raises that domain\'s concern' in section6
    ), "protocol section 6's Q->D concern rule is not the one this module encodes"

    declared = read_domain_concern_scale(protocol_text)
    published = read_review_domain_concern_legend(review_text)
    assert declared == DOMAIN_CONCERN_SCALE, (
        f"{PROTOCOL_SCALE_SOURCE} is not the vocabulary this module recognises: "
        f"protocol {sorted(declared)}, module {sorted(DOMAIN_CONCERN_SCALE)}"
    )
    assert published == DOMAIN_CONCERN_SCALE, (
        f"{REVIEW_LEGEND_SOURCE} is not the vocabulary this module recognises: "
        f"review {sorted(published)}, module {sorted(DOMAIN_CONCERN_SCALE)}"
    )

    a7 = _amendment(protocol_text, "A7", "A8")
    assert "`partial` is treated as not-`yes` and therefore raises the domain's concern" in a7, (
        "amendment A7's CONVENTION is not the one this module encodes"
    )
    assert "applied only in the rule-derived domain column" in a7, (
        "A7 no longer restricts its CONVENTION to the rule-derived column, which is the only "
        "column this module derives"
    )

    assert read_resolution_order(review_text) == (
        "no",
        "unclear",
        "partial",
        "yes",
    ), "review section 2.8's conservative ordering is not the one this module encodes"


def test_corpus_shape_reconciles_with_the_review(table, primary, recheck, review_text):
    """The exclusion classes derived from the logs match the ones review 6/6.1 declares."""
    shape = read_review_corpus_shape(review_text)
    ids = [row["rec"] for row in table]
    assert len(ids) == shape["rows"]
    assert len(set(ids)) == len(ids), "duplicate record id in the section 6 table"

    appraised, rechecked = set(primary["answers"]), set(recheck)
    recheck_only = rechecked - appraised
    no_fulltext = primary["unappraised"] - rechecked

    assert len(primary["twins"]) == shape["twins"]
    assert len(no_fulltext) == shape["no_fulltext"]
    assert len(recheck_only) == shape["recheck_only"]

    classes = [appraised | rechecked, no_fulltext, primary["twins"]]
    assert set().union(*classes) == set(ids), "table rows and log records do not cover each other"
    assert sum(len(c) for c in classes) == len(ids), "a record falls into two exclusion classes"


def test_every_answer_parses_to_a_declared_scale_level(primary, recheck):
    """Shortfall (a): the answer is the leading token of free-text prose. Parse it, or fail."""
    levels = set()
    for row in primary["answers"].values():
        assert set(row) == set(QUESTIONS)
        levels.update(row.values())
    for row in recheck.values():
        assert set(row) == set(QUESTIONS[:7]), "recheck pass is expected to carry Q1-Q7 only"
        levels.update(row.values())
    assert levels <= {"yes", "no", "unclear", "partial"}


def test_every_domain_concern_cell_is_a_declared_scale_level(table, primary, protocol_text):
    """The D column's counterpart to the Q-column check above: constrain the vocabulary.

    Both recorded D columns are covered — the review's appraisal-table column, which is what
    `divergent_cells` classifies, and the raw `domain_concerns` field of the primary log, which
    `load_primary` reads and nothing else consumed. They are checked SEPARATELY and never
    against each other: amendment A15 establishes that they are different columns — the
    review's being the extractor's judgments AFTER section 2.8's resolution raises — and reports
    the lenient divergence count as 31 against the first and 42 against the second. Asserting
    equality between them would be asserting something the amendment says is false.

    `divergent_cells` already refuses an out-of-scale label at the point of use. This states the
    same constraint as a property of the inputs, so a malformed cell is named as a data defect in
    its own right rather than surfacing only as a casualty of the A8 reconciliation.
    """
    scale = read_domain_concern_scale(protocol_text)
    admissible = NOT_ASSESSABLE_CELL | scale
    shipped = [
        (row["rec"], domain, cell)
        for row in table
        for domain in DOMAINS
        if (cell := strip_markers(row[domain.lower()])) not in admissible
    ]
    assert not shipped, (
        f"review D-column cell(s) outside {PROTOCOL_SCALE_SOURCE} {sorted(scale)}, as "
        f"(record, domain, value): {shipped}"
    )

    raw = [
        (rid, domain, value)
        for rid, judgments in primary["recorded_domains"].items()
        for domain, value in judgments.items()
        if value not in scale
    ]
    assert not raw, (
        f"raw `domain_concerns` value(s) outside {PROTOCOL_SCALE_SOURCE} {sorted(scale)}, as "
        f"(record, domain, value): {raw}"
    )


def test_resolved_answers_reproduce_the_shipped_q_cells(table, resolved):
    """Section 2.8's CONVENTION over the two logs rebuilds the table's Q column exactly.

    This is the load-bearing check under the D-rule derivation: if the Q cells the module
    reconstructs were not the Q cells the review published, a matching D column would prove
    nothing.
    """
    mismatches = []
    for row in table:
        for q in QUESTIONS:
            shipped = strip_markers(row[q.lower()])
            expected = None if shipped in NOT_ASSESSABLE_CELL else shipped
            if resolved[row["rec"]][q] != expected:
                mismatches.append((row["rec"], q, shipped, resolved[row["rec"]][q]))
    assert not mismatches, f"Q cells rebuilt from the logs differ from the review: {mismatches}"


def test_partial_extension_matches_amendments_a7_and_a12(table, resolved, protocol_text):
    """The `partial` cells and the answered-cell denominator reconcile with A12.

    Three separate reconciliations, because A12 states the numerator twice and the denominator
    as a product: the per-question split against the logs, A12's stated numerator against the
    sum of its own split, and the assessable-cell product against the logs. All three sides of
    A12 are captured, so a correction to any of them fails here as a divergence with a readable
    message rather than as a failure to match a pattern.
    """
    accounting = read_a12_partial_accounting(protocol_text)
    by_question = Counter()
    answered = 0
    for row in table:
        for q in QUESTIONS:
            answer = resolved[row["rec"]][q]
            if answer is None:
                continue
            answered += 1
            if answer == "partial":
                by_question[q] += 1
    assert by_question == accounting["by_question"]
    assert sum(by_question.values()) == accounting["total"]
    assert accounting["total"] == accounting["stated_partial_total"], (
        "A12's stated `partial` numerator and the sum of A12's own per-question split disagree: "
        f"stated {accounting['stated_partial_total']}, split sums to {accounting['total']}"
    )
    assert answered == accounting["answered_cells"]

    assert accounting["q1_q7_questions"] == len(QUESTIONS[:7]), (
        "A12's Q1-Q7 group size is not the one this module derives from the recheck pass's "
        "`rob_q1_7` field (shortfall (b))"
    )
    assert accounting["q8_q9_questions"] == len(QUESTIONS[7:]), (
        "A12's Q8/Q9 group size is not the one this module derives from the question set"
    )
    q1_q7 = sum(1 for r in table for q in QUESTIONS[:7] if resolved[r["rec"]][q] is not None)
    q8_q9 = sum(1 for r in table for q in QUESTIONS[7:] if resolved[r["rec"]][q] is not None)
    assert q1_q7 == accounting["q1_q7_records"] * accounting["q1_q7_questions"]
    assert q8_q9 == accounting["q8_q9_records"] * accounting["q8_q9_questions"]


def test_rule_derived_domain_column_reproduces_the_shipped_one(table, resolved, qd_map):
    """THE CENTRAL ASSERTION.

    For every one of the 72 appraisal rows, the domain-concern string derived from that row's
    Q cells — themselves rebuilt from the two extraction logs — equals the `D-rule` column the
    review publishes, character for character across all eight domains.
    """
    mismatches = []
    for row in table:
        shipped = row["d_rule"].strip().strip("`")
        derived = derive_domain_rule(resolved[row["rec"]], qd_map)
        if shipped != derived:
            mismatches.append((row["rec"], shipped, derived))
    assert not mismatches, f"rule-derived domain column diverges from the review: {mismatches}"


def test_divergence_profile_matches_amendment_a8(table, resolved, qd_map, protocol_text):
    """The recorded-vs-rule divergences are exactly the ones A8 enumerates.

    A8 splits the lenient direction into cells the frozen rule decides outright (a `no` or
    `unclear` input) and cells only A7's CONVENTION decides (a `partial` input and nothing
    else). Both subsets are recomputed here rather than taken from A8.
    """
    expected = read_a8_divergence_enumeration(protocol_text)
    found = divergent_cells(table, resolved, qd_map)

    rule_decided, convention_decided = Counter(), Counter()
    for rid, domain in found["lenient"]:
        answers = [resolved[rid][q] for q in qd_map[domain] if resolved[rid][q] is not None]
        if any(a in ("no", "unclear") for a in answers):
            rule_decided[domain] += 1
        else:
            convention_decided[domain] += 1

    assert len(found["lenient"]) == expected["lenient_total"]
    assert rule_decided == expected["lenient_rule_decided"]
    assert sum(rule_decided.values()) == expected["lenient_rule_decided_total"]
    assert convention_decided == expected["lenient_convention_decided"]
    assert sum(convention_decided.values()) == expected["lenient_convention_decided_total"]

    assert Counter(d for _, d in found["strict"]) == expected["strict"]
    assert len(found["strict"]) == expected["strict_total"]


def test_no_divergent_cell_outside_the_marked_set(table, resolved, qd_map):
    """Cell for cell: the derived divergences are exactly the cells the review marks.

    A8 pins the divergences down only to a per-domain count (shortfall (d)). The review's
    section 6 legend goes further and marks each divergent cell in place — section-sign for the
    lenient direction, pilcrow for the strict one. Comparing the derivation to those markers
    fails on a divergence in a cell the review does not mark, and on a marked cell the
    derivation does not reproduce.
    """
    found = divergent_cells(table, resolved, qd_map)
    marked_lenient, marked_strict = set(), set()
    for row in table:
        for domain in DOMAINS:
            cell = row[domain.lower()]
            if SECTION_SIGN in cell:
                marked_lenient.add((row["rec"], domain))
            if PILCROW in cell:
                marked_strict.add((row["rec"], domain))

    assert set(found["lenient"]) == marked_lenient, (
        "lenient-direction divergences derived from the logs are not the cells the review "
        f"marks: derived-only {sorted(set(found['lenient']) - marked_lenient)}, "
        f"marked-only {sorted(marked_lenient - set(found['lenient']))}"
    )
    assert set(found["strict"]) == marked_strict, (
        "strict-direction divergences derived from the logs are not the cells the review "
        f"marks: derived-only {sorted(set(found['strict']) - marked_strict)}, "
        f"marked-only {sorted(marked_strict - set(found['strict']))}"
    )


# ----------------------------------------------------------------------------------
# magic-number policy: the literals this module is permitted to contain
# ----------------------------------------------------------------------------------
# Both allow-lists are keyed by the DEFINITION the literal is written in (`<module>` for module
# level), not by value across the whole file. A licence granted for one use therefore does not
# travel: `9` is admitted as the exclusive bound of the domain index range and is still refused
# at any site that could pass off A8's convention-decided count of 9 as an index.
#
# `test_no_free_numeric_constants` skips these two definitions when it scans, since checking an
# allow-list against its own members is vacuous. That is the intended and only escape hatch:
# every member is visible here and carries an inline citation of what authorises it.
MODULE_SCOPE = "<module>"

STRUCTURAL_INDICES: dict[str, frozenset[int]] = {
    MODULE_SCOPE: frozenset(
        {
            1,  # Path.parents[1]; the low bound of the Q1.. and D1.. index ranges
            9,  # exclusive upper bound of the domain index range (D1-D8)
            10,  # exclusive upper bound of the question index range (Q1-Q9)
        }
    ),
    "_leading_answer": frozenset({1}),  # Match.group(1), the scale level
    "read_domain_question_map": frozenset({0}),  # Match.group(0), A8's whole map fragment
    "read_domain_concern_scale": frozenset({1}),  # Match.group(1), the parenthesised scale
    "read_review_domain_concern_legend": frozenset({1}),  # Match.group(1), the legend's list
    "read_resolution_order": frozenset({1}),  # Match.group(1)
    "read_a8_divergence_enumeration": frozenset({1, 2}),  # Match.group(1) / group(2)
    "read_a12_partial_accounting": frozenset({1, 2, 3, 4}),  # Match.group(1)..group(4)
    "read_review_corpus_shape": frozenset({1}),  # Match.group(1)
    "parse_appraisal_table": frozenset({0}),  # cells[0], the markdown alignment row
    "_docstring_ids": frozenset({0}),  # body[0], where a docstring sits if there is one
    # the Q1-Q7 / Q8-Q9 split point, which follows from the recheck pass's `rob_q1_7` field
    "test_every_answer_parses_to_a_declared_scale_level": frozenset({7}),
    "test_partial_extension_matches_amendments_a7_and_a12": frozenset({0, 1, 7}),
    "test_divergence_profile_matches_amendment_a8": frozenset({1}),  # Counter increment
}

DIGIT_BEARING_LITERALS: dict[str, frozenset[str]] = {
    MODULE_SCOPE: frozenset(
        {
            "utf-8",  # Python codec name, not a figure
            # the two source documents, named by the project's `{type}_{slug}_{date}.md`
            # convention; the date is part of the filename and cannot be derived from anything
            "lit_review_explosive-regime-dating_2026-08-24.md",
            "protocol_explosive-regime-review_2026-08-24.md",
            # document anchors and source citations, each written once at module level and
            # referenced by every definition that needs it, so the section number is licensed
            # here rather than in each of them
            "## 6. Risk of bias",  # protocol section 6's heading — the Q->D rule and the scale
            "## 7. Synthesis plan",  # the next heading, which bounds that span
            "protocol section 6's declared domain-concern scale",  # cited by section number
            "the review's section 6 legend for the D columns",  # cited by section number
        }
    ),
    "read_resolution_order": frozenset(
        {
            "### 2.8 Resolution rule",  # review section 2.8's heading — the span read
            "### 2.9 Synthesis",  # the next heading, which bounds that span
            "section 2.8's resolution ordering",  # failure text, citing section 2.8 by number
        }
    ),
    "read_review_corpus_shape": frozenset(
        {
            "## 6. Appraisal",  # review section 6's heading
            "### 6.1 Domain concern profile",  # review section 6.1's heading
            "## 7. Synthesis",  # the next heading, which bounds section 6.1
            "the section 6 row count",  # failure text, citing section 6 by number
        }
    ),
    "test_frozen_rule_texts_are_unchanged": frozenset(
        {
            # failure text, citing the rule's home section by number
            "protocol section 6's Q->D concern rule is not the one this module encodes",
            "review section 2.8's conservative ordering is not the one this module encodes",
        }
    ),
    "test_corpus_shape_reconciles_with_the_review": frozenset(
        {
            "duplicate record id in the section 6 table",  # failure text, citing section 6
        }
    ),
}

_ALLOW_LIST_NAMES = frozenset({"STRUCTURAL_INDICES", "DIGIT_BEARING_LITERALS"})
_DEFINITION_NODES = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
# A regex repetition count — `{m}`, `{m,}`, `{m,n}` — is pattern structure, not a figure.
_REGEX_REPETITION = re.compile(r"\{\d+(?:,\d*)?\}")
# A digit run NOT preceded by a word character, i.e. one standing alone as a quantity rather
# than bound into a token: the `50` of `**50 of` is caught; the `1` of `Q1`, the `12` of `A12`
# and the `7` of `rob_q1_7` are not. `\d` and `\w` escapes carry no digit character and so are
# excluded by construction; the class is written `\w` rather than spelled out as `[0-9A-Za-z_]`
# because this guard reports a character-class range bound like `0-9` — which is why any future
# pattern here should use the shorthand escapes. Digits in a backreference (`\1`) or a
# hex/unicode escape would likewise be reported. That direction is deliberate: an unfamiliar
# construct fails closed and is corrected in the open, rather than being silently admitted.
_FREE_DIGITS = re.compile(r"(?<!\w)\d+")


def _scoped_constants(tree: ast.Module) -> Iterator[tuple[str, ast.Constant]]:
    """Every `ast.Constant` in `tree`, paired with the definition it is written in.

    Comprehensions and lambdas are attributed to the enclosing `def`, which is the site a
    reader would look at to judge whether a literal is justified.
    """

    def descend(node: ast.AST, scope: str) -> Iterator[tuple[str, ast.Constant]]:
        for child in ast.iter_child_nodes(node):
            inner = child.name if isinstance(child, _DEFINITION_NODES) else scope
            if isinstance(child, ast.Constant):
                yield inner, child
            yield from descend(child, inner)

    yield from descend(tree, MODULE_SCOPE)


def _docstring_ids(tree: ast.Module) -> set[int]:
    """Ids of the string constants that are docstrings of the module, a class or a function."""
    ids: set[int] = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, *_DEFINITION_NODES)):
            continue
        first = node.body[0] if node.body else None
        if (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            ids.add(id(first.value))
    return ids


def _allow_list_ids(tree: ast.Module) -> set[int]:
    """Ids of every node inside the two allow-list definitions above."""
    ids: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.AnnAssign):
            targets = [node.target]
        elif isinstance(node, ast.Assign):
            targets = list(node.targets)
        else:
            continue
        # `node.value` is None for a bare `x: int` annotation, which the TypedDicts above use.
        if node.value is not None and any(
            isinstance(t, ast.Name) and t.id in _ALLOW_LIST_NAMES for t in targets
        ):
            ids.update(id(n) for n in ast.walk(node.value))
    return ids


def test_no_free_numeric_constants():
    """No magic numbers and no magic figures inside strings, enforced on this file itself.

    CLAUDE.md forbids arbitrary thresholds and unjustified constants. Every quantity this
    module compares against is parsed from the protocol, an amendment or the review — which is
    also what stops the module degenerating into a restatement of the shipped table.

    The scan covers BOTH numeric literals and digits written inside string literals, because a
    published figure baked into a regex anchor, an f-string or a message is the same defect as
    one written as an `int` — and is harder to see. Each is checked against the allow-list for
    the definition it is written in, so an index admitted for one use cannot serve another.

    Docstrings are exempt, and have to be: this one names 72 rows, 561 answered cells, 50
    `partial` cells and A8's 31 / 22 / 9 / 13 in order to say that hardcoding any of them fails
    here. A docstring is never compared against anything. Nothing else is exempt.

    The third assertion runs the allow-lists the other way: an entry that licenses nothing is
    itself a finding, because an exemption nobody exercises is an exemption nobody rechecks.
    That is what keeps the lists from growing into the hole they exist to close.
    """
    tree = ast.parse(Path(__file__).read_text(encoding=ENCODING))
    prose, declared = _docstring_ids(tree), _allow_list_ids(tree)

    free_numbers: list[tuple[str, object]] = []
    embedded_figures: list[tuple[str, list[str], str]] = []
    exercised: set[tuple[str, object]] = set()
    for scope, node in _scoped_constants(tree):
        value = node.value
        if id(node) in declared or isinstance(value, bool):
            continue
        if isinstance(value, int | float):
            if value in STRUCTURAL_INDICES.get(scope, frozenset()):
                exercised.add((scope, value))
            else:
                free_numbers.append((scope, value))
        elif isinstance(value, str) and id(node) not in prose:
            digits = _FREE_DIGITS.findall(_REGEX_REPETITION.sub("", value))
            if not digits:
                continue
            if value in DIGIT_BEARING_LITERALS.get(scope, frozenset()):
                exercised.add((scope, value))
            else:
                embedded_figures.append((scope, digits, value))

    unexercised = [
        (scope, member)
        for allow_list in (STRUCTURAL_INDICES, DIGIT_BEARING_LITERALS)
        for scope, members in allow_list.items()
        for member in members
        if (scope, member) not in exercised
    ]

    assert not free_numbers, (
        "unexplained numeric literal(s) in this module, as (definition, value): "
        f"{sorted(free_numbers, key=str)}"
    )
    assert not embedded_figures, (
        "unexplained digits inside string literal(s) in this module, as (definition, digits, "
        f"literal): {sorted(embedded_figures, key=str)}"
    )
    assert not unexercised, (
        "allow-list entr(ies) licensing nothing in this module, as (definition, member); drop "
        f"each rather than leaving an unexercised exemption: {sorted(unexercised, key=str)}"
    )
