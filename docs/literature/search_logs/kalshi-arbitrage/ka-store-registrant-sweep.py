# Registration-agency metadata sweep over the 149-record CSL-JSON store.
#
# ADDED 2026-09-02 by round-2 audit remediation, findings QUANT-2-8 and
# REPRODUCIBILITY-2-6. Round 1 rewrote 27 year cells, 78 venue cells and 18 in-text
# citation years on the strength of a registration-agency sweep whose responses were
# never archived, breaking the record's own frontmatter guarantee that "every metadata
# field traces to a stored response in the search-log directory". This script performs
# the sweep, stores one row per DOI, and is the artifact the corpus record now cites.
#
# It is a READ-ONLY check. It does not write the store.
#
# Usage: python ka-store-registrant-sweep.py     (writes ka-store-registrant-sweep.json)
import io, json, pathlib, sys, time, urllib.error, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
STORE = pathlib.Path('docs/literature/references_kalshi-arbitrage.json')
UA = 'castles-lit-review/1.0 (mailto:238704148+s-koirala@users.noreply.github.com)'
HDR = {'User-Agent': UA, 'Accept': 'application/json'}


def get(url):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=45)
        return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:                                    # noqa: BLE001
        return 0, {'_error': str(e)}


def year_of(dp):
    try:
        return int(dp['date-parts'][0][0])
    except Exception:                                         # noqa: BLE001
        return None


rows, agree_y, cmp_y, agree_c, cmp_c = [], 0, 0, 0, 0
store = json.load(io.open(STORE, encoding='utf-8'))
for e in store:
    doi = e['DOI']
    row = {'doi': doi, 'store_id': e['id'],
           'store_year': year_of(e['issued']),
           'store_container': e.get('container-title'),
           'store_type': e.get('type'),
           'agency': None, 'http_status': None,
           'registrant_issued': None, 'registrant_container': None,
           'registrant_type': None, 'registrant_created': None,
           'year_agrees': None, 'container_agrees': None}
    st, body = get('https://api.crossref.org/works/' + urllib.parse.quote(doi))
    if st == 200 and body:
        m = body['message']
        row.update(agency='crossref', http_status=200,
                   registrant_issued=m.get('issued', {}).get('date-parts'),
                   registrant_container=(m.get('container-title') or [None])[0],
                   registrant_type=m.get('type'),
                   registrant_created=m.get('created', {}).get('date-parts'))
    else:
        st2, body2 = get('https://api.datacite.org/dois/' + urllib.parse.quote(doi, safe=''))
        if st2 == 200 and body2:
            a = body2['data']['attributes']
            row.update(agency='datacite', http_status=200,
                       registrant_issued=[[a.get('publicationYear')]],
                       registrant_container=(a.get('container') or {}).get('title')
                       or a.get('publisher'),
                       registrant_type=(a.get('types') or {}).get('resourceTypeGeneral'),
                       registrant_created=a.get('created'))
        else:
            row.update(agency=None, http_status='crossref:%s datacite:%s' % (st, st2))
    ry = None
    if row['registrant_issued']:
        try:
            ry = int(row['registrant_issued'][0][0])
        except Exception:                                     # noqa: BLE001
            ry = None
    if ry is not None and row['store_year'] is not None:
        cmp_y += 1
        row['year_agrees'] = (ry == row['store_year'])
        agree_y += row['year_agrees']
    if row['registrant_container'] and row['store_container']:
        cmp_c += 1
        row['container_agrees'] = (row['registrant_container'].strip().lower()
                                   == str(row['store_container']).strip().lower())
        agree_c += row['container_agrees']
    rows.append(row)
    time.sleep(0.12)

out = {'date': '2026-09-02',
       'finding': ['QUANT-2-8', 'REPRODUCIBILITY-2-6'],
       'purpose': ('archived evidence for the section-7 statement that all 149 store DOIs '
                   'were checked against a registration agency and that the store agrees '
                   'with the registrant on every comparable field'),
       'n_records': len(rows),
       'n_crossref': sum(r['agency'] == 'crossref' for r in rows),
       'n_datacite': sum(r['agency'] == 'datacite' for r in rows),
       'n_unresolved': sum(r['agency'] is None for r in rows),
       'year_comparisons': cmp_y, 'year_agreements': agree_y,
       'year_disagreements': cmp_y - agree_y,
       'container_comparisons': cmp_c, 'container_agreements': agree_c,
       'container_disagreements': cmp_c - agree_c,
       'rows': rows}
io.open(HERE / 'ka-store-registrant-sweep.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(out, indent=1, ensure_ascii=False) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=1))
