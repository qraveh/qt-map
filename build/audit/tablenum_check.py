#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tablenum_check — every document table of the built Atlas carries its number and title (the editor's order of 23 Nov 2026,
local writer job 20261123-2; the rules in build/tables.py).

Reads dist/ after a build:
  1. each language's main page: every report table (a table fold that is not a brief's, a big-table fold) has the label
     «Table|Таблица|טבלה N-M» and a title after it; N is the chapter of the table's section, M runs 1, 2, 3 … per chapter;
     the three languages carry the same numbers in the same order;
  2. every brief's every language half: its tables numbered 1, 2, … with a title each;
  3. every record page (technology, machine, architecture): its tables numbered 1, 2, … with a title each;
  4. no {{TBL:…}} key is left in any page or language fragment;
  5. no reference of the old form is left in the pages' text: «Table 8.3», «Table A», «таблица 8.3», «табл. 8.3», «טבלה 8.3» …
     (the dated changelog lines and the errata say what changed when, in the words of the day, and are left out).

    python3 build/audit/tablenum_check.py        # exit 1 on any finding; prints the first findings
"""
import glob
import html as _html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, 'dist')
WORD = {'en': 'Table', 'ru': 'Таблица', 'he': 'טבלה'}
LABEL = re.compile(r'<span class="tno">(Table|Таблица|טבלה)&nbsp;<bdi dir="ltr">([0-9]+(?:-[0-9]+)?)</bdi></span>(.{0,200})', re.S)
OLD = {
    'en': re.compile(r'\bTables? (?:8\.[0-9]\b|[AB]\b)'),
    'ru': re.compile(r'(?:\b[Тт]аблиц[а-яё]*|\bтабл\.) (?:8\.[0-9]\b|[AB]\b)'),
    'he': re.compile(r'(?:ב|ל|ה|ו)?טבל[א-ת]* (?:8\.[0-9]\b|[AB]\b)'),
}
FINDINGS = []


def plain(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def title_after(rest):
    """the title text right after a label: « — Title» inside the same element"""
    m = re.match(r'\s*—\s*(.*?)(?:</strong>|</h[2-4]>|</summary>)', rest, re.S)
    return plain(m.group(1)) if m else ''


def text_only(h):
    """the page text outside scripts, styles and the dated change lists (changelog, errata)"""
    h = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<(ul|ol|div|section)[^>]*class="[^"]*(?:changelog|errata|editions)[^"]*"[^>]*>.*?</\1>', ' ', h, flags=re.S)
    return plain(h)


def check_report(L, path):
    h = open(path, encoding='utf-8').read()
    cut = h.find('<section class="brief')
    body = h[:cut] if cut > 0 else h
    seq = []
    for m in re.finditer(r'<details class="(?:tblfold" id="(?!brief-)[^"]+"[^>]*|fold big-table"[^>]*)><summary>(.*?)</summary>', body, re.S):
        lab = LABEL.search(m.group(1))
        if not lab:
            FINDINGS.append('%s main page: a report table without a label: %s' % (L, plain(m.group(1))[:60])); continue
        if lab.group(1) != WORD[L]:
            FINDINGS.append('%s main page: table %s labelled «%s»' % (L, lab.group(2), lab.group(1)))
        if not title_after(lab.group(3)):
            FINDINGS.append('%s main page: table %s has no title' % (L, lab.group(2)))
        seq.append(lab.group(2))
    per = {}
    for n in seq:
        c, k = n.split('-')
        per.setdefault(c, []).append(int(k))
    for c, ks in per.items():
        if ks != list(range(1, len(ks) + 1)):
            FINDINGS.append('%s main page: chapter %s numbered %s' % (L, c, ks))
    return seq


def check_doc(where, L, h):
    nums = [lab.group(2) for lab in LABEL.finditer(h)]
    for lab in LABEL.finditer(h):
        if not title_after(lab.group(3)):
            FINDINGS.append('%s: table %s has no title' % (where, lab.group(2)))
    if nums != [str(i) for i in range(1, len(nums) + 1)]:
        FINDINGS.append('%s: tables numbered %s' % (where, nums))
    ntab = len(re.findall(r'<table\b(?![^>]*class="(?:ttab|ctab)")', h))
    if ntab != len(nums):
        FINDINGS.append('%s: %d tables, %d labels' % (where, ntab, len(nums)))


def main():
    man = json.load(open(os.path.join(DIST, 'manifest.json'), encoding='utf-8'))
    seqs = {}
    for L, x in man['languages'].items():
        page = os.path.join(DIST, x['path'])
        seqs[L] = check_report(L, page)
        h = open(page, encoding='utf-8').read()
        for m in re.finditer(r'<section class="brief" id="brief-(\w+)" hidden>(.*?)</section>', h, re.S):
            for half in re.split(r'(?=<div class="bl lang-\w+"[ >])', m.group(2)):
                hm = re.match(r'<div class="bl lang-(\w+)"', half)
                if hm and 'data-lang-slot' not in half[:200]:
                    check_doc('%s main page, brief %s (%s)' % (L, m.group(1), hm.group(1)), hm.group(1), half)
        if '{{TBL:' in h:
            FINDINGS.append('%s main page: %d {{TBL:…}} key(s) left' % (L, h.count('{{TBL:')))
        for o in OLD[L].findall(text_only(h))[:5]:
            FINDINGS.append('%s main page: an old reference «%s»' % (L, o))
    langs = list(seqs)
    for L in langs[1:]:
        if seqs[L] != seqs[langs[0]]:
            FINDINGS.append('the numbers differ: %s %s vs %s %s' % (langs[0], seqs[langs[0]][:12], L, seqs[L][:12]))
    for f in sorted(glob.glob(os.path.join(DIST, 'lang', '*.js'))):
        t = open(f, encoding='utf-8').read()
        if '{{TBL:' in t:
            FINDINGS.append('%s: %d {{TBL:…}} key(s) left' % (os.path.relpath(f, DIST), t.count('{{TBL:')))
    nrec = 0
    for L, x in man['languages'].items():
        folder = os.path.join(DIST, x.get('folder', '')) if x.get('folder') else DIST
        for kind in ('technology', 'machine', 'architecture'):
            for f in sorted(glob.glob(os.path.join(folder, kind, '*.html'))):
                if f.endswith('index.html'):
                    continue
                h = open(f, encoding='utf-8').read(); nrec += 1
                body = h[h.find('<main'):h.find('</main>')] if '<main' in h else h
                check_doc(os.path.relpath(f, DIST), L, body)
                if '{{TBL:' in h:
                    FINDINGS.append('%s: {{TBL:…}} left' % os.path.relpath(f, DIST))
                for o in OLD[L].findall(text_only(body))[:3]:
                    FINDINGS.append('%s: an old reference «%s»' % (os.path.relpath(f, DIST), o))
    print('tablenum_check: report tables %s; record pages %d; %d finding(s)' % (
        ' · '.join('%s %d' % (L, len(s)) for L, s in seqs.items()), nrec, len(FINDINGS)))
    for x in FINDINGS[:40]:
        print('  ', x)
    sys.exit(1 if FINDINGS else 0)


if __name__ == '__main__':
    main()
