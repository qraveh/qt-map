# -*- coding: utf-8 -*-
"""Import a newly written brief into the references canon (26 Sep 2026, the 14 stations of the paths revalidation).

A new brief is written with citation placeholders — `[D][@arxiv:2306.11727]`, `[C][@u:https://…]`, `[D][@doi:10.…]` — and a
sidecar `<bid>.sources.json` ([{key, grade, record}] in order of first citation, record in the data/brief-sources.json schema).
This script resolves every key to a work the Atlas already knows (the report's bibliography data/sources.json → "report:CODE#i";
data/brief-sources.json by DOI, arXiv id or normalised URL) or adds the sidecar's record; fills data/brief-sources.json
`briefs[bid]` in order of first citation; takes the permanent numbers (build/worknum.py — a new work gets the next number);
replaces the placeholders by `[n]` in the English and, if present, the Russian text; and regenerates the md Sources lists
(brief_refs.write_all). Idempotent for a brief already imported (no placeholders left → nothing to do).

    python3 build/brief_import.py SIDECAR_DIR bid [bid …]      # then: python3 build/brief_refs.py --check
"""
import json, os, re, sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brief_refs as BR
import sources as S
import worknum

PH = re.compile(r'\[@([^\]\s]+)\]')


def canon_key(key):
    """the sidecar's key → (kind, canonical id)"""
    if key.startswith('arxiv:'): return 'arxiv:' + key[6:].strip()
    if key.startswith('doi:'): return 'doi:' + key[4:].strip().lower().rstrip('.')
    if key.startswith('u:'):
        u = key[2:].strip()
        if S.arxiv_of(u): return 'arxiv:' + S.arxiv_of(u)
        if S.doi_of(u): return 'doi:' + S.doi_of(u).lower().rstrip('.')
        return 'u:' + S.norm(u)
    raise ValueError('unknown key form: ' + key)


def index_known(db):
    """every strong id → the brief-sources key or report:CODE#i"""
    idx = {}
    for k, r in db['works'].items():
        for i in S.all_ids(r):
            if not i.startswith('t:'): idx.setdefault(i, k)
    for i, k in BR.report_index().items():
        if not i.startswith('t:'): idx.setdefault(i, k)
    return idx


def new_record(rec):
    r = OrderedDict()
    for k in BR.FIELDS:
        v = rec.get(k)
        if v in (None, '', [], False) and k != 'verified': continue
        r[k] = v
    if 'kind' not in r: r['kind'] = 'journal' if r.get('doi') else 'preprint' if r.get('arxiv') else 'web'
    if r.get('journal'): r['journal'] = S.JOURNALS.get(r['journal'], r['journal'])
    if r['kind'] == 'web' and not r.get('site'): r['site'] = S.host(r.get('url', ''))
    r['verified'] = bool(rec.get('verified'))
    return r


def import_brief(bid, side_dir, db):
    en = BR.read(BR.path(bid, 'en'))
    keys_in_text = []
    for m in PH.finditer(en):
        if m.group(1) not in keys_in_text: keys_in_text.append(m.group(1))
    if not keys_in_text:
        print('%s: no placeholders (already imported?)' % bid); return
    side = json.load(open(os.path.join(side_dir, bid + '.sources.json'), encoding='utf-8'))
    grade = {s['key']: s.get('grade') for s in side}
    recs = {s['key']: s.get('record') or {} for s in side}
    idx = index_known(db)
    work_of = {}
    for key in keys_in_text:
        cid = canon_key(key)
        cands = [cid]
        rec = recs.get(key, {})
        if rec and not rec.get('known'):
            cands += [i for i in S.all_ids(new_record(rec)) if not i.startswith('t:')]
        hit = next((idx[c] for c in cands if c in idx), None)
        kk = rec.get('known_key') if rec else None   # a sidecar may name the known work's key directly
        if hit is None and kk and (kk in db['works'] or kk.startswith('report:')): hit = kk
        if hit is None:
            if not rec or rec.get('known'):
                raise SystemExit('%s: %s is not a known work and the sidecar has no record for it' % (bid, key))
            r = new_record(rec)
            k = ('arxiv:' + r['arxiv']) if r.get('arxiv') else ('doi:' + r['doi'].lower().rstrip('.')) if r.get('doi') else S.norm(r['url'])
            if k in db['works']: hit = k
            else:
                db['works'][k] = r; hit = k
                for i in S.all_ids(r):
                    if not i.startswith('t:'): idx.setdefault(i, k)
                print('  + work %s' % k)
        work_of[key] = hit
    # the brief's entries in order of first citation; one work = one entry
    entries = []
    for key in keys_in_text:
        w = work_of[key]
        e = next((x for x in entries if x['work'] == w), None)
        if e is None: entries.append(OrderedDict([('work', w), ('grade', grade.get(key) or 'G')]))
    db['briefs'][bid] = entries
    nums = BR.numbers_of(bid, db)
    n_of = {e['work']: n for e, n in zip(entries, nums)}
    RUN = re.compile(r'(?:\[@[^\]\s]+\])+')   # adjacent placeholders → one IEEE run ([3], [5]–[7]); the grade tag before them stays
    def repl(m):
        keys = PH.findall(m.group(0))
        if any(k not in work_of for k in keys): return m.group(0)
        return BR.run_text([n_of[work_of[k]] for k in keys])
    for lang in ('en', 'ru'):
        p = BR.path(bid, lang)
        if not os.path.exists(p): continue
        t = BR.read(p)
        t2 = RUN.sub(repl, t)
        t2 = re.sub(r'(?m)^\(generated\)\n?', '', t2)
        if t2 != t: BR.write(p, t2)
    left = PH.findall(BR.read(BR.path(bid, 'en')))
    if left: raise SystemExit('%s: unresolved placeholders %s' % (bid, sorted(set(left))))
    print('%s: %d works, numbers %s' % (bid, len(entries), sorted(nums)))


if __name__ == '__main__':
    side_dir = sys.argv[1]; bids = sys.argv[2:]
    db = BR.load()
    for bid in bids: import_brief(bid, side_dir, db)
    BR.save(db); worknum.flush()
    BR.write_all(db)
    print('written; run: python3 build/brief_refs.py --check')
