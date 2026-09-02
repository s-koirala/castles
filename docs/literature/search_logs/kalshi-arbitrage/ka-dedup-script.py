# Archived screening/dedup tooling for the kalshi-arbitrage registered search.
# Absolute scratch paths present at execution time have been replaced by the token
# <WORKDIR> so that no OS account name appears in a committed file (CLAUDE.md,
# identity hygiene). The scripts are reproducible from the stored ka-*.json logs.
#
# REMEDIATION 2026-09-02, finding QUANT-1-6 (round-1 audit), protocol amendment A11.
# Two defects fixed, both of which made the published Table X-full row identifiers
# irreproducible while leaving every aggregate count unchanged:
#   (1) the title / abstract / venue tie-breaks below sorted on a single key (len)
#       over a *set*, so ties were broken by set iteration order, which depends on
#       PYTHONHASHSEED. The keys are now total: (len, value) and (-len, value).
#   (2) PYTHONHASHSEED was not pinned. It is now asserted at entry; the script
#       refuses to run unseeded rather than emitting an irreproducible uid map.
# Aggregate effect: none (15,924 raw / 8,813 works / 7,111 duplicates before and after).
# Row-id effect: total. See amendment A11 and corpus record section 5.
import json, io, os, re, sys, unicodedata, collections
if os.environ.get('PYTHONHASHSEED') != '0':
    raise SystemExit('QUANT-1-6: run with PYTHONHASHSEED=0; uid assignment is not '
                     'reproducible without it.')
recs = json.load(io.open(sys.argv[1], encoding='utf-8'))
def ntitle(t):
    if not t: return None
    t = unicodedata.normalize('NFKD', t)
    t = t.lower()
    t = re.sub(r'[^a-z0-9]+', ' ', t).strip()
    return t or None
parent = {}
def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb
for i, r in enumerate(recs):
    k = 'rec:%d' % i
    find(k)
    keys = []
    if r['doi']:   keys.append('doi:' + r['doi'])
    if r['arxiv']: keys.append('arx:' + re.sub(r'v\d+$', '', str(r['arxiv']).lower()))
    if r['repec']: keys.append('rep:' + r['repec'])
    if not (r['doi'] or r['arxiv'] or r['repec']):
        if r['oaid']: keys.append('oa:' + r['oaid'])
        if r['s2id']: keys.append('s2:' + r['s2id'])
    else:
        # OA/S2 ids still tie the record to its external-id twin
        if r['oaid']: keys.append('oa:' + r['oaid'])
        if r['s2id']: keys.append('s2:' + r['s2id'])
    nt = ntitle(r['title'])
    if nt and len(nt) > 12: keys.append('ti:' + nt)
    if not keys: keys.append('anon:%d' % i)
    for kk in keys: union(k, kk)
groups = collections.defaultdict(list)
for i in range(len(recs)):
    groups[find('rec:%d' % i)].append(i)
works = []
for g, idxs in groups.items():
    rs = [recs[i] for i in idxs]
    dois = sorted({r['doi'] for r in rs if r['doi']})
    arx = sorted({re.sub(r'v\d+$', '', str(r['arxiv']).lower()) for r in rs if r['arxiv']})
    rep = sorted({r['repec'] for r in rs if r['repec']})
    # QUANT-1-6: total sort keys. Length first (the original intent), value second
    # (the tie-break the original left to set iteration order).
    titles = sorted({r['title'] for r in rs if r['title']}, key=lambda t: (len(t), t))
    years = sorted({r['year'] for r in rs if r['year']})
    venues = sorted({r['venue'] for r in rs if r['venue']}, key=lambda v: (len(v), v))
    # NOT changed: this comprehension is a *list* over `rs`, whose order is the raw-record
    # order, and Python's sort is stable, so the longest-abstract pick was already total and
    # PYTHONHASHSEED-independent. Converting it to a set would silently change which abstract
    # a tied work carries, which would change token matching and hence screening codes -- a
    # re-screen, not a determinism fix. Left exactly as executed.
    absts = sorted([r['abstract'] for r in rs if r.get('abstract')], key=len, reverse=True)
    arms = sorted({r['arm'] for r in rs})
    qids = sorted({r['query_id'] for r in rs})
    works.append({
        'n_raw': len(rs), 'dois': dois, 'arxiv': arx, 'repec': rep,
        'title': titles[0] if titles else None, 'titles_all': titles,
        'year': years[0] if years else None, 'years_all': years,
        'venue': venues[0] if venues else None, 'venues_all': venues,
        'abstract': absts[0] if absts else None,
        'arms': arms, 'query_ids': qids,
        'oaids': sorted({r['oaid'] for r in rs if r['oaid']}),
        's2ids': sorted({r['s2id'] for r in rs if r['s2id']}),
    })
works.sort(key=lambda w: (-(w['n_raw']), w['title'] or ''))
for i, w in enumerate(works, 1): w['uid'] = 'U%05d' % i
print('raw records:', len(recs))
print('distinct works after dedup:', len(works))
print('duplicates removed:', len(recs) - len(works))
multi = [w for w in works if len(w['dois']) > 1]
print('groups spanning >1 DOI (twin/ledger review needed):', len(multi))
json.dump(works, io.open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
