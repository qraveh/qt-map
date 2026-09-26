# -*- coding: utf-8 -*-
"""Permanent reference numbers — one integer per work, the same everywhere in the Map (editor's decision of 26 Sep 2026).

data/work-numbers.json is the table:  {"next": N, "works": [{"n": 54, "ids": [...], "label": "Nee26"}, ...]}
  n       the number the page prints, in §9, in every technology brief and in the station cards; never reused, never moved
  ids     the identities the work is known by — doi:…, arxiv:…, u:<normalised url> (strong), t:<title key> (weak, a fallback
          for records that gain a DOI later); a work matched by any strong id, or failing that by its title id, is that work
  label   a BibTeX-alpha mnemonic frozen at entry (Nee26, BGL+25; none for a work without personal authors) — stored for
          hand-offs, notes and duplicate detection, not printed

The table was seeded from §9 as it stood on 26 Sep 2026 (numbers 1–205 in order of first citation in the English text), then
from the briefs walked in map order (layer 1 → 10, node-table order), each brief's list in its own order of first citation.
A work that enters later takes the next number, wherever it is cited; nothing is ever renumbered. The build assigns numbers
to works it does not find and writes the table back; a work whose ids point at two numbers stops the build.
"""
import json, os, re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLE = os.path.join(ROOT, 'data', 'work-numbers.json')
STRONG = ('doi:', 'arxiv:', 'u:', 'map:')


def load():
    if not os.path.exists(TABLE): return OrderedDict([('next', 1), ('works', [])])
    with open(TABLE, encoding='utf-8') as f: return json.load(f, object_pairs_hook=OrderedDict)


def save(t):
    with open(TABLE, 'w', encoding='utf-8', newline='\n') as f: f.write(json.dumps(t, ensure_ascii=False, indent=1) + '\n')


class Numbers:
    def __init__(self):
        self.t = load(); self.by_id = {}; self.dirty = False
        for e in self.t['works']:
            for i in e['ids']: self.by_id[i] = e

    def find(self, ids):
        """the table entry a work's ids point at (strong ids first, the title id as a fallback); two entries → ValueError"""
        strong = [self.by_id[i] for i in ids if i.startswith(STRONG) and i in self.by_id]
        hits = {e['n']: e for e in strong}
        if len(hits) > 1: raise ValueError('work-numbers: ids %s point at numbers %s' % (ids, sorted(hits)))
        if hits: return next(iter(hits.values()))
        weak = [self.by_id[i] for i in ids if i.startswith('t:') and i in self.by_id]
        hits = {e['n']: e for e in weak}
        if len(hits) > 1: raise ValueError('work-numbers: title ids %s point at numbers %s' % (ids, sorted(hits)))
        return next(iter(hits.values())) if hits else None

    def number(self, ids, label=None):
        """the work's permanent number; a work not in the table gets the next one (the table is written by save())"""
        ids = [i for i in ids if i]
        e = self.find(ids)
        if e is None:
            e = OrderedDict([('n', self.t['next']), ('ids', list(ids))])
            if label: e['label'] = self.uniq(label)
            self.t['works'].append(e); self.t['next'] += 1; self.dirty = True
            for i in ids: self.by_id[i] = e
            return e['n']
        new = [i for i in ids if i not in e['ids']]
        if new:
            e['ids'] += new; self.dirty = True
            for i in new: self.by_id[i] = e
        return e['n']

    def uniq(self, label):
        """alpha labels are frozen at entry: a collision takes the next letter (Swa26, Swa26a, Swa26b …)"""
        have = {e.get('label') for e in self.t['works']}
        if label not in have: return label
        for k in range(26):
            cand = label + chr(ord('a') + k)
            if cand not in have: return cand
        return label + '+'

    def save(self):
        if self.dirty: save(self.t); self.dirty = False


_N = []


def numbers():
    if not _N: _N.append(Numbers())
    return _N[0]


def flush():
    if _N: _N[0].save()


# ---------- the mnemonic (BibTeX alpha rules: one author → three letters; two to four → initials; five or more → three + '+')
def _surname(a):
    a = a.strip(' ,')
    if ',' in a: return a.split(',')[0].strip()
    parts = a.split()
    while len(parts) > 1 and parts[-1].rstrip('.') in ('Jr', 'Sr', 'II', 'III'): parts.pop()
    last = parts[-1] if parts else a
    while len(parts) > 1 and parts[-2].lower() in ('de', 'van', 'von', 'der', 'den', 'da', 'di', 'del', 'la', 'le', 'du'):
        parts.pop(-2)
    return last


def alpha_label(r):
    au = [a for a in (r.get('authors') or []) if a.strip()]
    if not au: return None
    yy = re.match(r'(\d{4})', str(r.get('pubdate') or r.get('date') or ''))
    yy = yy.group(1)[2:] if yy else ''
    sn = [re.sub(r'[^A-Za-zÀ-ÿ]', '', _surname(a)) for a in au]
    sn = [s for s in sn if s]
    if not sn: return None
    n = r.get('n_authors') or (99 if r.get('etal') else len(sn))
    if len(sn) == 1 and n == 1: lab = sn[0][:3]
    elif n <= 4 and len(sn) == n: lab = ''.join(s[0].upper() for s in sn)
    else: lab = ''.join(s[0].upper() for s in sn[:3]) + '+'
    return lab + yy
