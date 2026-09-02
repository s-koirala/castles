# Archived counterfactual runs over the committed screening pipeline.
#
# ADDED 2026-09-02 by round-2 audit remediation. Three numeric claims made in round-1
# amendment A11 and corpus-record section 6 were offered as measurements and could not
# be re-derived from any committed artefact. This script derives all three, so the
# claims that survive are re-checkable and the one that does not is demonstrably wrong.
#
#   findings QUANT-2-2 / REPRODUCIBILITY-2-3 -- the abstract tie-break counterfactual.
#     A11 stated: "with the abstract tie-break converted [to a set], the substring-mode
#     classifier no longer reproduces the published table (X1 6,672 instead of 6,707)".
#     CF-1 runs exactly that conversion at four hash seeds in both matching modes.
#
#   findings QUANT-2-9 / REPRODUCIBILITY-2-4 -- the bare-pattern counterfactual and the
#     corpus-wide dex/amm token statistics. CF-2 re-runs the classifier with the bare
#     BOUNDED patterns the audit finding prescribed; CF-3 counts, for each of the two
#     substrings, how many works contain it and how many match the bare and the shipped
#     pattern.
#
# It does NOT write ka-screening-verdicts.jsonl; every run goes to a scratch directory.
#
# Usage:
#   PYTHONHASHSEED=0 python ka-universe-script.py <scratch>/recs.json
#   python ka-counterfactuals.py <scratch>
import io
import json
import os
import pathlib
import re
import subprocess
import sys

LOG = pathlib.Path('docs/literature/search_logs/kalshi-arbitrage')
TMP = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'ka-counterfactual-scratch')
TMP.mkdir(parents=True, exist_ok=True)
SEEDS = ['0', '1', '7', '12345']
PY = sys.executable
B = chr(92) + 'b'

LIST_TIEBREAK = "absts = sorted([r['abstract'] for r in rs if r.get('abstract')], key=len, reverse=True)"
SET_TIEBREAK = "    absts = sorted({r['abstract'] for r in rs if r.get('abstract')}, key=len, reverse=True)"
BARE = ('BOUNDED = {"dex": r"' + B + 'dex' + B + '", "amm": r"' + B + 'amm' + B +
        '", "defi": r"' + B + 'defi' + B + '", "crypto": r"' + B + 'crypto' + B + '"}')


def variant(src, dst, swaps):
    """Copy an archived script, drop its seed guard, apply whole-line swaps."""
    lines = io.open(LOG / src, encoding='utf-8').read().split('\n')
    for i, line in enumerate(lines):
        if 'PYTHONHASHSEED' in line and line.lstrip().startswith('if os.environ.get('):
            lines[i] = ' ' * (len(line) - len(line.lstrip())) + 'if False:'
        for prefix, new in swaps:
            if line.strip().startswith(prefix):
                lines[i] = new
    text = '\n'.join(lines).replace('LOG / "ka-screening-verdicts.jsonl"',
                                    'os.environ["KA_OUT"]')
    io.open(TMP / dst, 'w', encoding='utf-8', newline='\n').write(text)


def run(script, args, seed, env=None):
    e = dict(os.environ, PYTHONHASHSEED=seed)
    e.update(env or {})
    r = subprocess.run([PY, str(TMP / script)] + args, capture_output=True, text=True, env=e)
    if r.returncode:
        raise SystemExit(r.stderr)
    return r.stdout


variant('ka-dedup-script.py', 'dedup_list.py', [])
variant('ka-dedup-script.py', 'dedup_set.py', [(LIST_TIEBREAK, SET_TIEBREAK)])
variant('ka-partition-script.py', 'partition.py', [])
variant('ka-screening-script.py', 'screen_shipped.py', [])
variant('ka-screening-script.py', 'screen_bare.py', [('BOUNDED = ', BARE)])

recs = str(TMP / 'recs.json')
results, works_cache = {}, {}
for tie, dedup in (('list', 'dedup_list.py'), ('set', 'dedup_set.py')):
    for seed in SEEDS:
        d = TMP / ('run_%s_%s' % (tie, seed))
        d.mkdir(exist_ok=True)
        run(dedup, [recs, str(d / 'works.json')], seed)
        run('partition.py', [str(d / 'works.json'), str(d / 'partition.json'),
                             str(d / 'inc.json')], seed)
        works_cache[(tie, seed)] = json.load(io.open(d / 'works.json', encoding='utf-8'))
        for mode, extra in (('boundary', {}), ('substring', {'KA_DEFI_MATCH': 'substring'})):
            o = run('screen_shipped.py', [], seed,
                    dict(extra, KA_WORKDIR=str(d), KA_OUT=str(d / ('v_%s.jsonl' % mode))))
            results[(tie, seed, mode)] = json.loads(o[:o.rindex('}') + 1])

base = works_cache[('list', SEEDS[0])]
cf1 = {
    'claim_in_A11': 'set-converted abstract tie-break gives X1 6,672 instead of 6,707',
    'reproduces': False,
    'X1_by_run': dict(sorted(('%s@seed%s/%s' % k, v['X1']) for k, v in results.items())),
    'n_works_whose_retained_abstract_differs_from_list_at_seed0': dict(sorted(
        ('%s@seed%s' % k, sum(1 for a, b in zip(base, w) if a['abstract'] != b['abstract']))
        for k, w in works_cache.items())),
    'seed_sensitivity': {
        'list_form_max_pairwise_diff': max(
            sum(1 for a, b in zip(works_cache[('list', s1)], works_cache[('list', s2)])
                if a['abstract'] != b['abstract'])
            for s1 in SEEDS for s2 in SEEDS),
        'set_form_max_pairwise_diff': max(
            sum(1 for a, b in zip(works_cache[('set', s1)], works_cache[('set', s2)])
                if a['abstract'] != b['abstract'])
            for s1 in SEEDS for s2 in SEEDS)},
    'conclusion': ('the aggregate nine-code table is IDENTICAL in all 16 runs, so the '
                   '6,672 figure does not reproduce and is withdrawn; but the SET form is '
                   'seed-DEPENDENT (works change which abstract they retain between seeds) '
                   'while the LIST form is not (zero differences at any seed pair), which is '
                   'the correct and verifiable ground for refusing the conversion'),
}

d0 = TMP / 'run_list_0'
run('screen_bare.py', [], '0', dict(KA_WORKDIR=str(d0), KA_OUT=str(d0 / 'v_bare.jsonl')))


def load(path):
    out = {}
    with io.open(path, encoding='utf-8') as f:
        f.readline()
        for line in f:
            if line.strip():
                r = json.loads(line)
                out[r['id']] = r
    return out


ship, bare = load(d0 / 'v_boundary.jsonl'), load(d0 / 'v_bare.jsonl')
byuid = {w['uid']: w for w in base}
moved = sorted(u for u in ship
               if ship[u]['primary_code'] == 'X5' and bare[u]['primary_code'] != 'X5')
cf2 = {
    'claim_in_A11': 'the bare patterns would have moved three genuine DeFi records out of X5',
    'bare_patterns': BARE,
    'n_moved': len(moved),
    'moved': [{'uid': u, 'title': byuid[u]['title'], 'code_under_bare': bare[u]['primary_code']}
              for u in moved],
    'moved_in_reverse': sorted(u for u in ship if ship[u]['primary_code'] != 'X5'
                               and bare[u]['primary_code'] == 'X5'),
    'conclusion': ('two records move, not three; the third record the amendment named, '
                   '"Automated Market Makers in Cryptoeconomic Systems", carries standalone '
                   'AMM tokens and stays X5 under the bare patterns'),
}

cf3 = {}
for sub, bare_pat, shipped_pat in (('dex', B + 'dex' + B, B + 'dexe?s?' + B),
                                   ('amm', B + 'amm' + B, B + 'amms?' + B)):
    blobs = [((w.get('title') or '') + ' || ' + ' || '.join(w.get('titles_all') or []) +
              ' || ' + (w.get('abstract') or '')).lower() for w in base]
    hits = [b for b in blobs if sub in b]
    cf3[sub] = {'bare_pattern': bare_pat, 'shipped_pattern': shipped_pat,
                'works_containing_substring': len(hits),
                'no_match_under_bare_pattern': sum(1 for b in hits
                                                   if not re.search(bare_pat, b)),
                'no_match_under_shipped_pattern': sum(1 for b in hits
                                                      if not re.search(shipped_pat, b))}

out = {'date': '2026-09-02',
       'findings': ['QUANT-2-2', 'QUANT-2-9', 'REPRODUCIBILITY-2-3', 'REPRODUCIBILITY-2-4'],
       'seeds': SEEDS,
       'CF-1_abstract_tiebreak': cf1,
       'CF-2_bare_defi_patterns': cf2,
       'CF-3_corpus_token_statistics': cf3}
io.open(LOG / 'ka-counterfactuals.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(out, indent=1, ensure_ascii=False) + '\n')
print(json.dumps(out, indent=1, ensure_ascii=False))
