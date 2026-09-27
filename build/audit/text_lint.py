#!/usr/bin/env python3
"""text_lint — reader-facing text that must not reach the public pages, and stale counts that must not survive a re-cut.

The pre-publication review of 27 Sep 2026 found the same shape of error at every boundary where register text enters the pages:
a scraped <!-- script --> in a picture credit, a cataloguer's "Honest null" and "not re-fetched" in record notes, LaTeX source doubled
next to its rendering, and hand-written summaries still carrying the counts of an earlier register (136 machines, 14 paths, 96
technologies, 1,533 cells). This lint reads the built pages (scripts and styles stripped) and the hand-written sources, and fails on:

  1. internal or scraped strings in reader text (FORBIDDEN);
  2. retired counts in the hand-written layer (RETIRED_COUNTS — extend it at every re-cut);
  3. English UI words on the Russian main page's static text, and Cyrillic in the English page's UI (the machine cards are drawn
     by JavaScript and are covered by c2_smoke instead);
  4. article slips left by a rename ("a Atlas", "a architecture").

    python3 build/audit/text_lint.py            # exit 1 on any hit; prints file, rule and a snippet
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, 'dist')

FORBIDDEN = [r'<!--\s*function', r'toggleAuthorList', r'You must enable JavaScript', r'Honest null', r'not re-fetched', r'node attrs say',
             r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\\mathrm\{', r'\\mathcal\{', r'\\ket\{', r'\[object Object\]', r'\bNaN\b',
             r'claude\.ai/artifact']
RETIRED_COUNTS = [r'\b136 (machines|машин)', r'\b14 (architectures|paths|архитектур|путей)', r'\b96 (technologies|технологий|nodes|stations)',
                  r'\b1,533\b', r'\b1 533\b', r'\b153 (machines|машин)', r'\b110 (technologies|технологий)']
ARTICLES = [r'\ba (Atlas|architecture|Architecture|atlas)\b', r'\bA (Atlas|architecture)\b']
EN_UI_ON_RU = [r'Show table', r'Show records', r'\bregister card\b', r'Skip to the map']
CYR_IN_EN_UI = [r'<summary>[^<]*[А-Яа-я]', r'<button(?![^>]*data-setlang)[^>]*>[^<]*[А-Яа-я][^<]*</button>']   # the language switch itself says «Русский»

HAND_WRITTEN = ['report/report_EN.md', 'report/report_RU.md', 'README.md', 'CITATION.cff', '.zenodo.json', 'data/glossary-own.json',
                'data/glossary-field.json']   # the generators' comments may name retired counts as history; the pages are checked above


def strip_markup(h):
    h = re.sub(r'<script\b.*?</script>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<style\b.*?</style>', ' ', h, flags=re.S | re.I)
    return h


def visible(h):
    return re.sub(r'<[^>]+>', ' ', strip_markup(h))


def hits(text, patterns, label, path, out, limit=3):
    for p in patterns:
        ms = list(re.finditer(p, text))
        if ms:
            m = ms[0]; snip = text[max(0, m.start() - 50):m.end() + 50].replace('\n', ' ')
            out.append('%s: %s [%s] ×%d — …%s…' % (os.path.relpath(path, ROOT), label, p, len(ms), snip))


def main():
    out = []
    pages = sorted(glob.glob(os.path.join(DIST, '*.html')) + glob.glob(os.path.join(DIST, 'ru', '*.html'))
                   + glob.glob(os.path.join(DIST, '*', '*.html')) + glob.glob(os.path.join(DIST, 'ru', '*', '*.html'))
                   + glob.glob(os.path.join(DIST, 'lang', '*.js')))
    for p in pages:
        raw = open(p, encoding='utf-8').read()
        text = visible(raw) if p.endswith('.html') else raw
        hits(text, FORBIDDEN, 'forbidden', p, out)
        hits(text, ARTICLES, 'article', p, out)
        if os.path.basename(p) in ('Quantum-Technology-Atlas-2026.09.html', 'index.html') and os.sep + 'ru' + os.sep in p:
            hits(strip_markup(raw), EN_UI_ON_RU, 'english-ui-on-ru', p, out)
        if p.endswith('.html') and os.sep + 'ru' + os.sep not in p and os.path.dirname(p) == DIST:
            hits(strip_markup(raw), CYR_IN_EN_UI, 'cyrillic-in-en-ui', p, out)
    for rel in HAND_WRITTEN:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p): continue
        t = open(p, encoding='utf-8').read()
        hits(t, RETIRED_COUNTS, 'retired-count', p, out)
        hits(t, ARTICLES, 'article', p, out)
    print('text_lint: %d page(s) and %d source file(s) read; %d finding(s)' % (len(pages), len(HAND_WRITTEN), len(out)))
    for x in out: print('  ' + x[:300])
    return 1 if out else 0


if __name__ == '__main__':
    sys.exit(main())
