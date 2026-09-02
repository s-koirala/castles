# arXiv venue sweep over the 25 `10.48550` rows of the CSL-JSON store.
#
# ADDED 2026-09-02 by round-2 audit remediation, finding LITERATURE-2-4. The round-1
# tier check compared this artifact's section-7 table against its own section-8 claim
# lines, so it could not detect a preprint row whose registrant or arXiv record names a
# peer-reviewed venue. Chen & Pennock, "A Utility Framework for Bounded-Loss Market
# Makers", was carried as a 2012 T5 preprint; arXiv:1206.5252 is the 2012 bulk upload
# of the UAI proceedings and the arXiv record carries report number UAI-P-2007-PG-49-56.
#
# This script re-checks every arXiv row against the arXiv abstract record's
# journal_ref / Related DOI / Report number fields and archives the result.
# It is READ-ONLY and does not write the store.
#
# Usage: python ka-store-arxiv-venuecheck.py    (writes ka-store-arxiv-venuecheck.json)
import html, io, json, pathlib, re, time, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
STORE = pathlib.Path('docs/literature/references_kalshi-arbitrage.json')
HDR = {'User-Agent': 'Mozilla/5.0 (compatible; castles-lit-review/1.0)'}


def text_of(fragment):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', fragment))).strip() or None


def cell(body, cls):
    m = re.search(r'<td class="tablecell ' + cls + r'"[^>]*>(.*?)</td>', body, re.S)
    return text_of(m.group(1)) if m else None


def labelled(body, label):
    m = re.search(re.escape(label) + r'</td>\s*<td class="tablecell[^"]*">(.*?)</td>', body, re.S)
    return text_of(m.group(1)) if m else None


rows = []
for e in json.load(io.open(STORE, encoding='utf-8')):
    doi = (e.get('DOI') or '')
    if not doi.lower().startswith('10.48550'):
        continue
    aid = re.split(r'arxiv\.', doi, flags=re.I)[-1]
    body = urllib.request.urlopen(
        urllib.request.Request('https://arxiv.org/abs/' + aid, headers=HDR), timeout=45
    ).read().decode('utf-8', 'replace')
    jref = cell(body, 'jref')
    report = labelled(body, 'Report&nbsp;number:')
    rel = labelled(body, 'Related&nbsp;DOI:')
    rows.append({
        'doi': doi, 'arxiv_id': aid, 'store_id': e['id'],
        'store_year': e['issued']['date-parts'][0][0],
        'journal_ref': jref, 'report_number': report, 'related_doi': rel,
        'comments': cell(body, 'comments'),
        'has_non_arxiv_venue_evidence': bool(jref or report or rel),
    })
    time.sleep(1.0)

hits = [r for r in rows if r['has_non_arxiv_venue_evidence']]
out = {
    'date': '2026-09-02', 'finding': ['LITERATURE-2-4'],
    'n_arxiv_rows': len(rows), 'n_with_venue_evidence': len(hits),
    'records_with_venue_evidence': [r['arxiv_id'] for r in hits],
    'bounded_negative': ('arXiv journal_ref is author-supplied and frequently not updated '
                         'after publication, so "no venue evidence" bounds what arXiv records, '
                         'not what was published'),
    'store_edited': False,
    'rows': rows,
}
io.open(HERE / 'ka-store-arxiv-venuecheck.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(out, indent=1, ensure_ascii=False) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=1))
