#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""table_check — the printed §7.2 and the map's live table are one source (ticket 20261106-1, 6 Nov 2026).

build/node_table.py writes the cell strings once; build/make_sections.py prints them as §7.2 of the report, build/build_html.py embeds
them as window.__TABLE for the map's Table view. This check reads every language's built main page and refuses any of the three to drift:

  1. the embedded rows (window.__TABLE) equal node_table.cells() recomputed from data/graph.json — every technology, every language;
  2. the page's §7.2 table has one row per technology in the same order, and every attribute cell's text equals node_table.sec72()
     (the parts joined with §7.2's separators), the layer cell "n Name" and the technology cell "Name id";
  3. the column labels and the caption are present for every language.

    python3 build/audit/table_check.py        # exit 1 on any difference; prints the first differences per language
"""
import html as _html, json, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'build'))
from langs import LANGS, FOLDER   # noqa: E402
import node_table as nt            # noqa: E402


class _Table(HTMLParser):
    """the first <table> after the given heading id: rows as lists of cell texts (tags stripped, whitespace collapsed)"""
    def __init__(self, hid):
        super().__init__(); self.hid = hid; self.seen = False; self.intab = 0; self.rows = []; self.row = None; self.cell = None; self.done = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.seen:
            if tag in ('h2', 'h3', 'h4') and a.get('id') == self.hid: self.seen = True
            return
        if self.done: return
        if tag == 'table': self.intab += 1
        elif self.intab and tag == 'tr': self.row = []
        elif self.intab and tag in ('td', 'th') and self.row is not None: self.cell = []
    def handle_endtag(self, tag):
        if not self.seen or self.done: return
        if tag in ('td', 'th') and self.cell is not None: self.row.append(re.sub(r'\s+', ' ', ''.join(self.cell)).strip()); self.cell = None
        elif tag == 'tr' and self.row is not None: self.rows.append(self.row); self.row = None
        elif tag == 'table' and self.intab: self.intab -= 1; self.done = True
    def handle_data(self, d):
        if self.cell is not None: self.cell.append(d)


def main():
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    order = nt.order(G); problems = []
    for L in LANGS:
        folder = os.path.join(ROOT, 'dist', FOLDER[L].strip('/')) if FOLDER[L] else os.path.join(ROOT, 'dist')
        pages = [f for f in os.listdir(folder) if re.match(r'Quantum-Technology-Atlas-.*\.html$', f)] if os.path.isdir(folder) else []
        if not pages: problems.append('%s: no built main page in %s' % (L, folder)); continue
        h = open(os.path.join(folder, sorted(pages)[0]), encoding='utf-8').read()
        m = re.search(r'window\.__TABLE=(\{.*?\});window\.__KEYREFS=', h, flags=re.S)
        if not m: problems.append('%s: window.__TABLE not embedded' % L); continue
        T = json.loads(m.group(1))
        # 1. the embedded rows against the data
        rows = T.get('rows') or []
        if [r['id'] for r in rows] != [n['id'] for n in order]: problems.append('%s: embedded rows are not §7.2\'s order (%d rows)' % (L, len(rows)))
        keys = ['aff', 'time', 'det', 'c', 'd', 'mod', 'place', 'f', 'g', 'status', 'since']
        bad = 0
        for r, n in zip(rows, order):
            want = [nt.cells(G, L, n)[k] for k in keys]
            if r['c'].get(L) != want or r['n'].get(L) != nt.name(L, n):
                bad += 1
                if bad <= 3: problems.append('%s: embedded row %s differs: %s ≠ %s' % (L, n['id'], r['c'].get(L), want))
        if not T.get('cols', {}).get(L) or not T.get('cap', {}).get(L): problems.append('%s: column labels or caption missing' % L)
        # 2. the printed §7.2 against the data
        p = _Table('%s-s7-2' % L); p.feed(h)
        body = [r for r in p.rows if r and re.fullmatch(r'\d+', r[0])]   # the numbered rows; the header row starts with "#"
        if len(body) != len(order): problems.append('%s: §7.2 has %d rows, the graph %d' % (L, len(body), len(order)))
        bad = 0
        for r, n in zip(body, order):
            want = ['%d %s' % (n['layer'], nt.layer_name(G, L, n['layer'])), '%s %s' % (nt.name(L, n), n['id'])] + nt.sec72(G, L, n)
            got = [_html.unescape(x) for x in r[1:]]
            if got != want:
                bad += 1
                if bad <= 3:
                    k = next((i for i, (a, b) in enumerate(zip(got, want)) if a != b), None)
                    problems.append('%s: §7.2 row %s cell %s: %r ≠ %r' % (L, n['id'], k, got[k] if k is not None else got, want[k] if k is not None else want))
        if bad > 3: problems.append('%s: … %d §7.2 rows differ' % (L, bad))
        if not p.seen: problems.append('%s: heading %s-s7-2 not found' % (L, L))
    print('table_check: %d language(s); %d problem(s)' % (len(LANGS), len(problems)))
    for x in problems: print('  ' + x[:400])
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
