# Retrieved bytes — what is in this repository and what is not

Which arms' retrieved bytes were retained, which were not, and what that means for the
SHA-256 values recorded in each arm's logs.

Written 2026-09-04 in response to audit finding `REPRODUCIBILITY-1-6`. It records a gap; it
does not close one. No log was edited to produce it, and no byte was synthesised.

## Summary

| arm | class | retrieved bytes in repo? | digests |
|---|---|---|---|
| academic | S-A / S-B | **yes** — 112 files under `payloads/` | **checkable** |
| software repository | S-C | **yes** — 49 files under `payloads/`, plus 29 README files | **checkable** |
| lateral / grey | S-D | **no** | **attestations** |
| venue documents | S-E | **no** | **attestations** |

## Retained

**Academic arm — 112 raw response payloads under `payloads/`:** `ks-crossref-*.json` (19),
`ks-openalex-*.json` (14), `ks-arxiv-*.xml` (13), `ks-s2-*.json` (56), `ks-repec-*.html` (9),
`ks-ssrn-01.html` (1). Each per-query log in this directory records `payload_sha256` over
those same bytes and `payload_path` pointing at the file. Both are checkable, and
[ks-academic-extract.py](ks-academic-extract.py) re-parses these files offline.

**Software-repository arm — 49 raw response payloads under `payloads/`:** `ks-gh-*.json.gz`
(20), `ks-gl-*.json.gz` (10), `ks-pypi-*.json.gz` (11), `ks-npm-*.json.gz` (8). Stored as
gzip containers; [ks-github-queries.json](ks-github-queries.json) states this in
`payload_sha256_basis` and its digests are over the uncompressed response bytes, so they are
checkable after decompression. Payloads exist only for queries that returned HTTP 200 — the
five PyPI names that 404'd are logged with no payload, as intended.

**Software-repository arm — 29 README files under
[ks-github-readme-evidence/](ks-github-readme-evidence)**, retrieved at each drawn record's
pinned commit SHA. The `platform_metadata.readme.sha256` values in
[ks-github-records.jsonl](ks-github-records.jsonl) are digests of these files and are
checkable.

## Not retained

**Lateral / grey arm (S-D) — [ks-lateral-records.json](ks-lateral-records.json).** All 32
records carry `sha256_of_retrieved_bytes`. **None of those payload objects is in this
repository.** All 32 also carry a `local_payload_name` (25 distinct values, e.g.
`s1_oddsshopper_ladder`, `s6_polytrage_fees`). **`local_payload_name` does not resolve.**
There is no file of that name under `payloads/`, anywhere else in this search-log tree, or
anywhere else in the repository. The field names an object in the executing session's own
working store, not a repository artifact, and a reader is entitled to read it as a promise
that the bytes were kept. They were not kept here.

Consequently every `sha256_of_retrieved_bytes` in ks-lateral-records.json is an
**attestation**: a claim by the executing session about bytes it saw, not a digest a reader
of this repository can recompute.

*Partial exception, at the query level.* 22 of the 78 rows in
[ks-lateral-queries.json](ks-lateral-queries.json) compute `payload_sha256` over the
`result_links` array, which is stored **inline in that same file** — its
`payload_sha256_basis` says so. Those 22 are genuinely self-checkable, and all 22 were
recomputed and matched on 2026-09-04. The other 56 query rows and all 32 record-level
digests remain attestations.

**Venue-document arm (S-E) — [ks-venue-docs.json](ks-venue-docs.json).** All 30 documents
carry `sha256_of_retrieved_bytes`; `payload_path` is null on every one of the 87 rows in
[ks-venue-queries.json](ks-venue-queries.json). This arm declared the position in its own
logs rather than leaving it to be discovered — the header's `payload_retention` field states
that raw payloads were retained outside the repository because they are large binary rule
documents and that the SHA-256 is the durable carrier per protocol section 5 field F12. The
declaration is accurate; the consequence is unchanged. Every S-E digest is an **attestation**.

## Where the S-D bytes actually are

The S-D payload objects were located outside the repository, in the untracked scratchpad of
the session that executed the arm, under the names `local_payload_name` records. All 32
record digests were recomputed against those bytes on 2026-09-04: **32 matched, 0
mismatched, 0 missing.** The digests are therefore truthful — they are digests of real
retrieved bytes — but that store is untracked, machine-local and ephemeral, so it is not
evidence any reader of this repository can reach, and this file's classification of the S-D
digests as attestations stands.

Whether to bring those bytes into the repository is a corpus-composition decision, and this
file does not make it. Until it is made, the check above is not repeatable by a third party.

## What this means for a reader

- A quotation or count sourced to the academic or software-repository arms can be checked
  against bytes in this repository.
- A quotation, count, effective date or rule clause sourced to the **lateral** or **venue**
  arms rests on the executing session's attestation. The
  [ks-lateral-records.json](ks-lateral-records.json) header records that 105 quoted fragments
  were checked against the retrieved payloads with 0 failures; that verification was real,
  but it was performed by the executing session against bytes a reader cannot obtain here.
- `local_payload_name` in ks-lateral-records.json should be read as an identifier in the
  executing session's store, **not** as a path into this repository.
