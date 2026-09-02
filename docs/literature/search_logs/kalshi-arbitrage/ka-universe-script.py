# Archived screening/dedup tooling for the kalshi-arbitrage registered search.
# Absolute scratch paths present at execution time have been replaced by the token
# <WORKDIR> so that no OS account name appears in a committed file (CLAUDE.md,
# identity hygiene). The scripts are reproducible from the stored ka-*.json logs.
import json, io, re, html, pathlib, sys
LOG = pathlib.Path('docs/literature/search_logs/kalshi-arbitrage')
def L(p): return json.load(io.open(p, encoding='utf-8'))
recs = []   # each: dict(arm, query_id, doi, arxiv, repec, oaid, s2id, title, year, venue, abstract, type)
def norm_doi(d):
    if not d: return None
    d = str(d).strip().lower()
    d = re.sub(r'^https?://(dx\.)?doi\.org/', '', d)
    return d or None
def add(**kw):
    kw.setdefault('abstract', None)
    recs.append(kw)
def oa_abs(w):
    inv = w.get('abstract_inverted_index')
    if not inv: return None
    pos = {}
    for word, idxs in inv.items():
        for i in idxs: pos[i] = word
    return ' '.join(pos[k] for k in sorted(pos))[:2500]
def push_oa(w, arm, qid):
    add(arm=arm, query_id=qid, doi=norm_doi(w.get('doi')), arxiv=None, repec=None,
        oaid=(w.get('id') or '').rsplit('/',1)[-1], s2id=None,
        title=(w.get('display_name') or w.get('title') or '').strip(),
        year=w.get('publication_year'),
        venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name'),
        type=w.get('type'), abstract=oa_abs(w))
def push_s2(pp, arm, qid):
    ext = pp.get('externalIds') or {}
    add(arm=arm, query_id=qid, doi=norm_doi(ext.get('DOI')),
        arxiv=ext.get('ArXiv'), repec=None, oaid=None, s2id=pp.get('paperId'),
        title=(pp.get('title') or '').strip(), year=pp.get('year'),
        venue=pp.get('venue'), type=None, abstract=(pp.get('abstract') or None))
for f in sorted(LOG.glob('ka-*.json')):
    name = f.stem
    if name in ('protocol-doicheck',): continue
    d = L(f)
    plat, arm, qid, raw = d.get('platform'), d.get('arm'), d.get('query_id'), d.get('raw')
    if d.get('http_status') != 200: continue
    if plat == 'crossref':
        msg = (raw or {}).get('message', {})
        items = msg.get('items') if 'items' in msg else ([msg] if msg.get('DOI') else [])
        for it in items or []:
            add(arm=arm, query_id=qid, doi=norm_doi(it.get('DOI')), arxiv=None, repec=None,
                oaid=None, s2id=None, title=(it.get('title') or [''])[0].strip(),
                year=(it.get('issued', {}).get('date-parts') or [[None]])[0][0],
                venue=(it.get('container-title') or [None])[0], type=it.get('type'),
                abstract=re.sub(r'<[^>]+>', ' ', it.get('abstract') or '') or None)
    elif plat == 'openalex':
        if isinstance(raw, dict) and 'results' in raw:
            for w in raw['results']: push_oa(w, arm, qid)
    elif plat == 'semanticscholar':
        if isinstance(raw, dict):
            for x in (raw.get('data') or []):
                pp = x.get('citingPaper') if 'citingPaper' in x else x
                if pp: push_s2(pp, arm, qid)
    elif plat == 'arxiv':
        txt = raw if isinstance(raw, str) else ''
        for m in re.finditer(r'<entry>(.*?)</entry>', txt, re.S):
            e = m.group(1)
            def g(tag):
                mm = re.search(r'<%s>(.*?)</%s>' % (tag, tag), e, re.S)
                return html.unescape(re.sub(r'\s+', ' ', mm.group(1)).strip()) if mm else None
            idu = g('id') or ''
            aid = idu.rsplit('/', 1)[-1]
            doim = re.search(r'<arxiv:doi[^>]*>(.*?)</arxiv:doi>', e, re.S)
            add(arm=arm, query_id=qid, doi=norm_doi(doim.group(1)) if doim else None,
                arxiv=aid, repec=None, oaid=None, s2id=None, title=g('title'),
                year=int((g('published') or '0000')[:4]) if g('published') else None,
                venue='arXiv', type='preprint', abstract=g('summary'))
    elif plat == 'nber':
        for r in (raw or {}).get('results', []):
            u = r.get('url') or ''
            mm = re.search(r'/papers/(w\d+)', u)
            add(arm=arm, query_id=qid, doi=('10.3386/' + mm.group(1)) if mm else None,
                arxiv=None, repec=None, oaid=None, s2id=None,
                title=(r.get('title') or '').strip(), year=None,
                venue='NBER Working Paper', type='working-paper',
                abstract=re.sub(r'<[^>]+>', ' ', r.get('abstract') or '') or None)
    elif plat and plat.startswith('repec'):
        for r in d.get('records', []):
            add(arm=arm, query_id=qid, doi=None, arxiv=None, repec=r['repec_path'],
                oaid=None, s2id=None, title=r['title'], year=None, venue='RePEc/IDEAS',
                type=None)
print('raw records pulled:', len(recs))
json.dump(recs, io.open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False)
