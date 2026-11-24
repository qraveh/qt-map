#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Offline test of build/tables.py, the table numbering of 20261123-2 — no build, no browser.

    python build/audit/tables_test.py        # exit 1 on any failure
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'build'))
import tables as T  # noqa: E402

RESULTS = []


def case(name, fn):
    try:
        fn()
        RESULTS.append((name, True, ''))
    except AssertionError as e:
        RESULTS.append((name, False, str(e)))
    except SystemExit as e:
        RESULTS.append((name, False, 'SystemExit: %s' % e))
    except Exception as e:  # a crash is a failure too
        RESULTS.append((name, False, '%s: %s' % (type(e).__name__, e)))


def fold(i, summary, head='Goal'):
    return ('<details class="tblfold" id="%s" data-def="1" open><summary>%s</summary><div class="tbl"><table><thead><tr><th>%s</th>'
            '</tr></thead><tbody><tr><td>x</td></tr></tbody></table></div></details>' % (i, summary, head))


REPORT = ('<h2 id="en-s1">1 Criteria</h2><h3 id="en-s1-1">1.1 Why</h3>' + fold('en-tbl-0', '<strong>Error classes</strong>') +
          '<h3 id="en-s1-2">1.2 Axes</h3>' + fold('en-tbl-1', '<strong>The six axes</strong>') +
          '<h2 id="en-s7">7 Graph</h2><h3 id="en-s7-2">7.2 Node table</h3><details class="fold big-table"><summary>The technologies'
          '</summary><table><tr><td>t</td></tr></table></details>' +
          '<h3 id="en-s7-10">7.10 Machines</h3>' + fold('en-tbl-5', '<strong>Table A — the Technology × Machine matrix</strong>') +
          fold('en-tbl-6', '<strong>Table B — machines against the clock.</strong>') +
          '<h2 id="en-s8">8 Machines</h2><h3 id="en-s8-3">8.3 Idea</h3>' + fold('en-tbl-7', '<strong>Table 8.3 — architectures: the bet</strong>') +
          '<p>See Table {{TBL:s8-3}} and Table {{TBL:s7-10#2}}.</p>')


def t_report_numbers_per_chapter():
    h, keys = T.number_report(REPORT, 'en')
    assert {k: v[0] for k, v in keys.items()} == {'s1-1': '1-1', 's1-2': '1-2', 's7-2': '7-1', 's7-10': '7-2', 's7-10#2': '7-3', 's8-3': '8-1'}, keys
    assert keys['s8-3'][1] == 'en-tbl-7' and keys['s7-2'][1] == 'en-tbl-s7-2', keys
    assert '<details class="fold big-table" id="en-tbl-s7-2">' in h, 'the big table has no id'
    assert 'Table&nbsp;<bdi dir="ltr">7-3</bdi></span> — Machines against the clock</strong>' in h, 'old prefix and final period not dropped'
    assert '— The Technology × Machine matrix</strong>' in h, 'the old «Table A —» prefix stays or no capital'
    assert '— Architectures: the bet</strong>' in h
    assert '<summary><strong><span class="tno">Table&nbsp;<bdi dir="ltr">7-1</bdi></span> — The technologies</strong></summary>' in h, 'big table'


def t_report_refs_resolved():
    h, keys = T.number_report(REPORT, 'en')
    r = T.resolve(h, 'en', keys)
    assert 'See Table <a class="xref" href="#en-tbl-7">8-1</a> and Table <a class="xref" href="#en-tbl-6">7-3</a>.' in r and '{{TBL:' not in r, r[-160:]


def t_refs_inside_links_and_attributes_stay_bare():
    keys = {'s8-3': ('8-3', 'en-tbl-20')}
    r = T.resolve('<a class="xref" href="#en-s8-3">Table {{TBL:s8-3}}</a> <span title="see Table {{TBL:s8-3}}">x</span>', 'en', keys)
    assert r == '<a class="xref" href="#en-s8-3">Table 8-3</a> <span title="see Table 8-3">x</span>', r


def t_title_dash_becomes_colon():
    h, _ = T.number_report('<h2 id="en-s8">8</h2><h3 id="en-s8-4">8.4</h3>' + fold('en-tbl-8', '<strong>Verdict history — one row per edition</strong>'), 'en')
    assert '— Verdict history: one row per edition</strong>' in h, h


def t_refs_inside_buttons_stay_bare():
    keys = {'s7-2': ('7-1', 'en-tbl-s7-2')}
    r = T.resolve('<button type="button" class="chip" data-tablerow="ion">↑ Table {{TBL:s7-2}} row</button>', 'en', keys)
    assert r == '<button type="button" class="chip" data-tablerow="ion">↑ Table 7-1 row</button>', r


def t_halves_resolved_by_their_language():
    keys = {'en': {'s8-2': ('8-2', 'en-tbl-19')}, 'ru': {'s8-2': ('8-2', 'ru-tbl-19')}}
    r = T.resolve_halves('<div class="bl lang-en">row {{TBL:s8-2}}</div><div class="bl lang-ru">строка {{TBL:s8-2}}</div>', keys)
    assert 'href="#en-tbl-19">8-2' in r and 'href="#ru-tbl-19">8-2' in r, r


def t_unknown_key_stops():
    try:
        T.resolve('<p>{{TBL:s9-9}}</p>', 'en', {'s8-3': ('8-3', 'en-tbl-20')})
    except SystemExit as e:
        assert 's9-9' in str(e)
        return
    raise AssertionError('an unknown key passed')


def t_untitled_report_table_stops():
    try:
        T.number_report('<h2 id="en-s4">4 Fit</h2>' + fold('en-tbl-7', '<span class="tlbl">table</span>'), 'en')
    except SystemExit as e:
        assert '4-1' in str(e) and 'no title' in str(e)
        return
    raise AssertionError('an untitled table passed')


def t_show_table_only_stops():
    try:
        T.number_report('<h2 id="en-s7">7</h2><h3 id="en-s7-2">7.2</h3><details class="fold big-table"><summary>Show table</summary></details>', 'en')
    except SystemExit as e:
        assert 'Show table' in str(e)
        return
    raise AssertionError('a big table titled only «Show table» passed')


def t_table_before_chapter_one_stops():
    try:
        T.number_report('<h2 id="en-s-about">About</h2>' + fold('en-tbl-0', '<strong>X</strong>'), 'en')
    except SystemExit as e:
        assert 'no chapter number' in str(e)
        return
    raise AssertionError('a table in About passed')


def t_brief_tables_skipped_by_report():
    h, keys = T.number_report('<h2 id="en-s8">8</h2>' + fold('brief-ion-en-tbl-0', '<span class="tlbl">table</span>', 'Year'), 'en')
    assert keys == {} and 'tno' not in h


def t_doc_default_titles_three_languages():
    for L, generic, year, org, want1, want2 in (
            ('en', 'table', 'Year', 'Organisation', 'Records timeline', 'Who'),
            ('ru', 'таблица', 'Год', 'Организация', 'Хронология рекордов', 'Кто'),
            ('he', 'טבלה', 'שנה', 'ארגון', 'ציר הזמן של השיאים', 'מי')):
        h = T.number_doc(fold('a', '<span class="tlbl">%s</span>' % generic, year) + fold('b', '<strong>%s.</strong>' % want2, org), L)
        assert '<bdi dir="ltr">1</bdi></span> — %s</strong>' % want1 in h, (L, h[:300])
        assert '<bdi dir="ltr">2</bdi></span> — %s</strong>' % want2 in h, (L, 'final period not dropped')
        assert ('>%s&nbsp;<bdi' % T.WORD[L]) in h


def t_doc_plain_table_under_heading():
    h = T.number_doc('<div class="space"><h4>Technologies by layer — the machine\'s cell per layer</h4><table class="ptab mtab"><tr><td>x</td></tr></table></div>', 'en')
    assert '<h4><span class="tno">Table&nbsp;<bdi dir="ltr">1</bdi></span> — Technologies by layer: the machine\'s cell per layer</h4><table' in h, h


def t_doc_unknown_untitled_stops():
    try:
        T.number_doc(fold('a', '<span class="tlbl">table</span>', 'Mystery'), 'en')
    except SystemExit as e:
        assert 'mystery' in str(e)
        return
    raise AssertionError('an untitled table of no known kind passed')


def t_briefs_halves_numbered_apart():
    block = ('<section class="brief" id="brief-ion" hidden><div class="bl lang-en">' + fold('brief-ion-en-tbl-0', '<span class="tlbl">table</span>', 'Year') +
             fold('brief-ion-en-tbl-1', '<strong>Who.</strong>', 'Organisation') + '</div><div class="bl lang-ru">' +
             fold('brief-ion-ru-tbl-0', '<span class="tlbl">таблица</span>', 'Год') + '</div></section><section class="brief" id="brief-sc" hidden>'
             '<div class="bl lang-en">' + fold('brief-sc-en-tbl-0', '<strong>Records timeline</strong>', 'Year') + '</div></section>')
    h = T.number_briefs(block)
    assert h.count('<bdi dir="ltr">1</bdi>') == 3 and h.count('<bdi dir="ltr">2</bdi>') == 1, h
    assert 'Таблица&nbsp;<bdi dir="ltr">1</bdi></span> — Хронология рекордов' in h


def t_hebrew_label_isolated():
    assert T.label('he', '8-3') == '<span class="tno">טבלה&nbsp;<bdi dir="ltr">8-3</bdi></span>'


def main():
    for name, fn in sorted((k, v) for k, v in globals().items() if k.startswith('t_') and callable(v)):
        case(name[2:], fn)
    for name, ok, why in RESULTS:
        print('%s %s%s' % ('PASS' if ok else 'FAIL', name, '' if ok else ' — ' + why))
    bad = sum(1 for r in RESULTS if not r[1])
    print('\n%d tests, %d failed' % (len(RESULTS), bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
