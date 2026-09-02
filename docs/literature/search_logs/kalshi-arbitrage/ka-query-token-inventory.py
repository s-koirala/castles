# Token inventory over the topical search strategy, as executed.
#
# ADDED 2026-09-02 by round-2 audit remediation, findings QUANT-2-1 and
# LITERATURE-2-1 (both critical). Round 1 asserted that the strings `dealer` and
# `limit order` appear in none of the topical queries. That test was run against
# the query strings AS STORED -- Crossref forms are `+`-separated and the arXiv /
# OpenAlex / Semantic Scholar forms are percent-encoded -- so it reported every
# multi-word token as absent, including `betting market`, which the same paragraph
# asserted was present. The test is only meaningful on URL-DECODED query text.
#
# This script re-runs it on that basis and writes ka-query-token-inventory.json.
# Input is the corpus record's own section-3 fenced query blocks, which are
# byte-identical to the protocol's section-3.1 blocks plus the retry re-issues.
#
# Usage: python ka-query-token-inventory.py            (writes the JSON beside itself)
import io, json, pathlib, re, urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
RECORD = pathlib.Path('docs/literature/lit_review_kalshi-arbitrage_2026-09-02.md')
PROTOCOL = pathlib.Path('docs/methodology/protocol_kalshi-arbitrage-review_2026-09-02.md')
TOPICAL = ('ka-crossref-', 'ka-openalex-', 'ka-arxiv-', 'ka-s2-', 'ka-nber-', 'ka-repec-')
TOKENS = ['parimutuel', 'pari-mutuel', 'pari mutuel', 'dealer', 'specialist',
          'limit order', 'order book', 'inventory risk', 'market making',
          'betting market', 'market maker', 'binary option', 'event contract']


def blocks(path):
    txt = io.open(path, encoding='utf-8').read()
    out = {}
    for qid, body in re.findall(r'```text (ka-[a-z0-9-]+)\n(.*?)\n```', txt, re.S):
        if qid.startswith(TOPICAL):
            out[qid] = body.strip()
    return out


def decode(u):
    return urllib.parse.unquote(u).replace('+', ' ').lower()


def inventory(qs):
    dec = {k: decode(v) for k, v in qs.items()}
    return {t: {'present_decoded': sorted(k for k, v in dec.items() if t in v),
                'present_raw_literal': sorted(k for k, v in qs.items() if t in v.lower())}
            for t in TOKENS}


rec, pro = blocks(RECORD), blocks(PROTOCOL)
out = {
    'date': '2026-09-02',
    'finding': ['QUANT-2-1', 'LITERATURE-2-1'],
    'method': ('percent-decode each fenced topical query block, map "+" to space, '
               'case-fold, then substring-test each token. present_raw_literal is the '
               'round-1 test, retained so the defect is visible and not merely asserted.'),
    'n_blocks_record': len(rec),
    'n_blocks_protocol_frozen': len(pro),
    'note_on_counts': ('the record carries the 35 frozen topical queries plus 10 retry '
                       're-issues (ka-s2-0{1..4}-b, -c and ka-repec-0{1,2}-supp); the '
                       'protocol carries the 35 frozen queries only'),
    'tokens_over_record_blocks': inventory(rec),
    'tokens_over_frozen_protocol_blocks': inventory(pro),
}
io.open(HERE / 'ka-query-token-inventory.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(out, indent=1, ensure_ascii=False) + '\n')
for t, v in out['tokens_over_record_blocks'].items():
    print('%-16s decoded=%s  raw=%s' % (t, v['present_decoded'], v['present_raw_literal']))
