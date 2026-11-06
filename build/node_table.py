# -*- coding: utf-8 -*-
"""One row builder for the node table — the report's §7.2 (printed) and the map's Table view (live) read the same strings
(ticket 20261106-1, the editor's decision 3 of 6 Nov 2026: §7.2 stays printed, generated from the same row builder as the live
table). Before this module the strings lived in build/make_sections.py alone.

    cells(G, lang, n)   -> dict: the eleven value strings of one technology in one language, each attribute split into the parts
                           the live table shows in columns of its own (time / entangling, control / placement, status / since)
    sec72(G, lang, n)   -> list: the eight attribute cells of §7.2 — the parts joined with §7.2's separators ("; ", " @ ", " · ")
    order(G)            -> the technologies in §7.2's order (layer, fabricated first, id)
    table_json(G)       -> what build_html.py embeds as window.__TABLE: the column labels, the caption, and one row per technology
                           with its cells in every language — the live table renders these strings and never recomputes them
    COLS[lang]          -> the live table's column labels, in §7.2's words

A dash ("—") means "not defined for this layer" (the attribute does not apply), never "unknown": §7.1 names which attributes a layer
carries. build/audit/table_check.py reads the built page and refuses a §7.2 cell that differs from the embedded row.
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
from langs import LANGS, pick

# the live table's columns, in §7.2's words (the printed header joins b, e and status · since into one cell each)
COLS = {
    'en': ['Layer', 'Technology', '(a) carrier affinity', '(b) time', 'entangling', '(c) readout', '(d) mobility', '(e) control', 'placement', '(f) error structure', '(g) manufacturing', 'status', 'since'],
    'ru': ['Слой', 'Технология', '(a) сродство носителя', '(b) время', 'запутывание', '(c) считывание', '(d) подвижность', '(e) управление', 'размещение', '(f) структура ошибки', '(g) производство', 'статус', 'с года'],
    'he': ['שכבה', 'טכנולוגיה', '(a) זיקת הנושא', '(b) זמן', 'שזירה', '(c) קריאה', '(d) ניידות', '(e) בקרה', 'מיקום', '(f) מבנה השגיאה', '(g) ייצור', 'מצב', 'מאז'],
}
# the caption under the live table (S2 of the ticket): one line, the terms defined in place; {s71} is the link to §7.1 in the page's language
CAPTION = {
    'en': 'Technologies × the seven design attributes of {s71}. — = the attribute does not apply to this layer.',
    'ru': 'Технологии × семь атрибутов проектирования {s71}. — = атрибут к этому слою не применим.',
    'he': 'טכנולוגיות × שבע תכונות התכן של {s71}. — = התכונה אינה חלה על השכבה הזו.',
}
# the one line under §7.2's heading (S7): the printed table is linked to its live twin on the map
LINKED = {
    'en': 'Linked to the map: [open as a table on the map](#map:view=table).',
    'ru': 'Связана с картой: [открыть как таблицу на карте](#map:view=table).',
    'he': 'מקושרת למפה: [פתיחה כטבלה במפה](#map:view=table).',
}
YES = {'en': 'yes', 'ru': 'да', 'he': 'כן'}
NO = {'en': 'no', 'ru': 'нет', 'he': 'לא'}
DESTR = {'en': 'destructive', 'ru': 'разрушающее', 'he': 'הרסנית'}
MID = {'en': 'mid-circuit', 'ru': 'внутрисхемное', 'he': 'mid-circuit'}


def _t(lang, triple):
    """a vocabulary entry [en, ru, he] in the language, English when the language has none"""
    return pick(lang, triple)


def logt(x):
    """a log10 time (seconds) as the report prints it: 3 significant digits in the unit that keeps the number above 1"""
    if x is None: return '—'
    v = 10 ** x
    if v >= 1: return f"{v:.0f} s"
    if v >= 1e-3: return f"{v*1e3:.3g} ms"
    if v >= 1e-6: return f"{v*1e6:.3g} µs"
    return f"{v*1e9:.3g} ns"


def name(lang, n): return n.get(lang) or n['en']


def layer_name(G, lang, k):
    L = next(l for l in G['layers'] if l['n'] == k)
    return pick(lang, (L['en'], L.get('ru', L['en']), L.get('he', L['en'])))


def cells(G, lang, n):
    """the eleven value strings of one technology: aff, time, det, c, d, mod, place, f, g, status, since (strings; '—' = not defined)"""
    V = G['vocab']; b = n['b']; c = n.get('c'); e = n['e']
    places = e['place'] if isinstance(e['place'], list) else [e['place']]   # list-valued since 17 Sep 2026: every stage, in the vocabulary's order (RT → 4 K → mK)
    places = [p for p in V['PLACE'] if p in places] + [p for p in places if p not in V['PLACE']]
    return {
        'aff': _t(lang, V['AFF']['%g' % n['aff']]),
        'time': logt(b['t']),
        'det': _t(lang, V['DET'][b['det']]),
        'c': ('—' if not c else '%s; %s; %s=%s; %s=%s' % (_t(lang, V['MECH'][c['mech']]), logt(c['t']), DESTR[lang], YES[lang] if c['destr'] else NO[lang], MID[lang], YES[lang] if c['mid'] else NO[lang])),
        'd': _t(lang, V['MOB'][n['d']]),
        'mod': '—' if e['mod'] == 'none' else _t(lang, V['MOD'][e['mod']]),
        'place': '—' if e['mod'] == 'none' else ' / '.join(_t(lang, V['PLACE'][p]) for p in places),
        'f': ', '.join(_t(lang, V['ERR'][x]) for x in n['f']),
        'g': _t(lang, V['FAB'][n['g']]),
        'status': _t(lang, V['STATUS'][n['status']]),
        'since': str(n['since']) if n['since'] < 2030 else '—',
    }


def sec72(G, lang, n):
    """§7.2's eight attribute cells, the parts joined with §7.2's separators — the only place the joins are written"""
    x = cells(G, lang, n); b = n['b']
    return [x['aff'],
            ('—' if (b['t'] is None and b['det'] == 'na') else '%s; %s' % (x['time'], x['det'])),
            x['c'], x['d'],
            ('—' if n['e']['mod'] == 'none' else '%s @ %s' % (x['mod'], x['place'])),
            x['f'], x['g'],
            (x['status'] if x['since'] == '—' else '%s · %s' % (x['status'], x['since']))]   # no year: the status alone (a trailing " · —" is what tidy() strips)


def order(G):
    """§7.2's order: by layer, the fabricated half first, then by id"""
    return sorted(G['nodes'], key=lambda x: (x['layer'], -x['aff'], x['id']))


def table_json(G):
    """window.__TABLE for the page: {cols:{L:[…13]}, cap:{L:…}, rows:[{id, l, i, n:{L:name}, c:{L:[…11]}}]} — the rows in §7.2's order,
    every language's strings embedded (the map's own strings are embedded for every language too: one page, three languages)"""
    keys = ['aff', 'time', 'det', 'c', 'd', 'mod', 'place', 'f', 'g', 'status', 'since']
    rows = []
    for i, n in enumerate(order(G), 1):
        rows.append({'id': n['id'], 'l': n['layer'], 'i': i,
                     'n': {L: name(L, n) for L in LANGS},
                     'c': {L: [cells(G, L, n)[k] for k in keys] for L in LANGS}})
    return {'cols': {L: COLS[L] for L in LANGS}, 'cap': {L: CAPTION[L] for L in LANGS},
            'lay': {L: {str(l['n']): layer_name(G, L, l['n']) for l in G['layers']} for L in LANGS}, 'rows': rows}
