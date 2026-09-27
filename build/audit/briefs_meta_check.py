#!/usr/bin/env python3
"""briefs_meta_check — the briefs' front matter against the graph (one name, one layer, one status, one date per station).

The page shows the graph's name and 'since' on the brief since 27 Sep 2026 (briefs.load_briefs), so a divergence here is not
visible to readers; it is the authors' record drifting from the single source, and the list is the editor's worksheet for
choosing the better wording (the Russian brief titles are often the better Russian). Layer and status divergences fail the check:
the brief's layer line and status word are printed as written.

    python3 build/audit/briefs_meta_check.py            # summary + the divergences
    python3 build/audit/briefs_meta_check.py --quiet    # summary only; exit 1 on a layer or status divergence
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATUS = {'D': 'demonstrated', 'E': 'emerging', 'T': 'theory / design only', 'X': 'empty slot — no technology yet'}
STATUS_ALIASES = {'theory': 'theory / design only', 'empty slot': 'empty slot — no technology yet'}


def front(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    d = {}
    for line in (m.group(1).split('\n') if m else []):
        k, _, v = line.partition(':'); d[k.strip()] = v.strip().strip('"\'')
    return d


def main():
    quiet = '--quiet' in sys.argv
    g = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    names, since, hard, missing = [], [], [], []
    for n in g['nodes']:
        for lang in ('en', 'ru'):
            p = os.path.join(ROOT, 'briefs', lang, n['id'] + '.md')
            if not os.path.exists(p): missing.append((lang, n['id'])); continue
            d = front(p)
            if d.get('name') != n[lang]: names.append((lang, n['id'], d.get('name', ''), n[lang]))
            L = d.get('layer', '').split(' ')[0]
            if L != str(n['layer']): hard.append((lang, n['id'], 'layer', d.get('layer'), n['layer']))
            st = STATUS_ALIASES.get(d.get('status', ''), d.get('status', ''))
            if st != STATUS.get(n['status'], n['status']): hard.append((lang, n['id'], 'status', d.get('status'), STATUS.get(n['status'])))
            gs = str(n['since']) if n.get('since') is not None and n['since'] < 2030 else '—'
            if d.get('since', '—') not in (gs, '') and not (gs == '—' and d.get('since') in ('—', '-', '', '2030')):   # 2030 = the sentinel of an empty slot
                since.append((lang, n['id'], d.get('since'), gs))
    print('briefs_meta_check: %d stations · names differ %d · since differ %d · layer/status differ %d · missing briefs %d' % (
        len(g['nodes']), len(names), len(since), len(hard), len(missing)))
    if not quiet:
        for x in hard: print('  HARD', *x)
        for x in since: print('  since', *x)
        for lang, nid, a, b in names: print('  name %s %-14s brief: %s  |  graph: %s' % (lang, nid, a, b))
        for x in missing: print('  missing', *x)
    return 1 if (hard or missing) else 0


if __name__ == '__main__':
    sys.exit(main())
