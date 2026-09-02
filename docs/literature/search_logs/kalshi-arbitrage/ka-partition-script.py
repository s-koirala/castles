# Archived screening tooling for the kalshi-arbitrage registered search.
#
# ADDED 2026-09-02 by round-1 remediation, finding QUANT-1-6, protocol amendment A11.
# At first execution the two inputs this file now derives -- the amendment-A3 REVIEW /
# DEFAULT-X1 partition and the included-record uid set -- were unarchived scratch files
# (`partition.json`, `inc.json`), so the archived pipeline could not be re-run end to end
# from the committed logs. Both are derived here from artefacts that ARE committed:
#   partition : ka-screening-vocabulary.json (the published amendment-A3 token list)
#   include   : references_kalshi-arbitrage.json (the CSL-JSON store, keyed by DOI)
# No new decision is taken here; this file only makes an existing one reproducible.
#
# Usage: PYTHONHASHSEED=0 python ka-partition-script.py <works.json> <partition.json> <inc.json>
import json, io, os, re, sys, pathlib
if os.environ.get('PYTHONHASHSEED') != '0':
    raise SystemExit('QUANT-1-6: run with PYTHONHASHSEED=0.')
LOG = pathlib.Path('docs/literature/search_logs/kalshi-arbitrage')
STORE = pathlib.Path('docs/literature/references_kalshi-arbitrage.json')
works = json.load(io.open(sys.argv[1], encoding='utf-8'))
V = json.load(io.open(LOG / 'ka-screening-vocabulary.json', encoding='utf-8'))
TOK = [t.lower() for t in V['tokens']]


def blob(w):
    return ((w.get('title') or '') + ' || ' + ' || '.join(w.get('titles_all') or []) + ' || ' +
            (w.get('abstract') or '')).lower()


# --- amendment A3 partition, over the forward-citation-ONLY stratum ---------------
review, default_x1 = [], []
for w in works:
    if w['arms'] != ['forward-citation']:
        continue
    (review if any(t in blob(w) for t in TOK) else default_x1).append(w['uid'])
assert len(review) + len(default_x1) == V['n_stratum'], 'A3 stratum size drifted'
assert len(review) == V['n_review'] and len(default_x1) == V['n_default_x1'], 'A3 partition drifted'

# --- included set: the 149 store DOIs mapped onto uids -----------------------------
store = json.load(io.open(STORE, encoding='utf-8'))
by_doi, by_arxiv = {}, {}
for w in works:
    for d in w['dois']:
        by_doi.setdefault(d.lower(), w['uid'])
    for a in w['arxiv']:
        by_arxiv.setdefault(a.lower(), w['uid'])
inc_uids, unresolved = [], []
for e in store:
    d = (e.get('DOI') or '').lower()
    uid = by_doi.get(d)
    if uid is None:
        m = re.match(r'10\.48550/arxiv\.(.+)', d)      # arXiv DataCite DOI -> arXiv id
        uid = by_arxiv.get(m.group(1).lower()) if m else None
    (inc_uids.append(uid) if uid else unresolved.append(d))
assert not unresolved, 'store DOIs not present in the universe: %r' % unresolved
assert len(set(inc_uids)) == len(store) == 149, 'included set size drifted'

json.dump({'review': sorted(review), 'default_x1': sorted(default_x1)},
          io.open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({'include': [{'uid': u} for u in sorted(set(inc_uids))], 'x7': []},
          io.open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False)
print('REVIEW', len(review), 'DEFAULT-X1', len(default_x1), 'include', len(set(inc_uids)))
