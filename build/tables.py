# -*- coding: utf-8 -*-
"""Table numbering — every document table of the Atlas carries a label and a title above it (the editor's order of 23 Nov 2026:
«У всех таблиц помести явную нумерацию, например, Таблица 1-1; Правила нумерации возьми из лучших мировых образцов…»; local
writer job 20261123-2; the rules and their sources in 00_admin/30_working/DECISIONS_2026-11-24_table-numbering.md).

  - the report: tables numbered within each chapter in order of appearance, the chapter and the sequence joined by an ASCII
    hyphen-minus — «Table 8-3», the editor's form and O'Reilly's. A period would read as a section number (§8.3); an en dash, the
    Feynman Lectures' form, is reversed by the bidirectional algorithm inside Hebrew (U+2013 is a neutral), the hyphen-minus is
    not (UAX #9, rule W4: a single European separator between two European numbers);
  - a brief and a record page: tables numbered from 1 within the document — «Table 1» — as ISO, GOST and APA number a
    stand-alone document; a single table is still «Table 1»;
  - the label in the page language's word (Table, Таблица, טבלה) with the number in <bdi dir="ltr">, then a spaced em dash and
    the title, in sentence case and without a final period, above the table — the table fold's summary is its caption;
  - the text refers to a table by a key, {{TBL:s8-3}} (the first table under the heading of §8.3; s7-10#2 the second under
    §7.10), which the build replaces with the number: a table inserted later renumbers every reference to the ones after it;
  - the map's interface tables (the inspector, the Table view, the compare tray), the briefs' index and the colophon's list of
    editions are not document tables and carry no number.

number_report(h, L) numbers the report body of one language and returns it with the key → number map; number_doc(h, L) numbers
one document (a brief's half, a record page's body); resolve(h, L, keys) replaces the {{TBL:…}} keys and refuses an unknown one.
"""
import html as _html
import re

WORD = {'en': 'Table', 'ru': 'Таблица', 'he': 'טבלה'}
GENERIC = {'table', 'таблица', 'טבלה'}
SHOW = {'en': 'Show table', 'ru': 'Показать таблицу', 'he': 'הצג את הטבלה'}
OLD = re.compile(r'^(?:Table|Таблица|טבלה)\s+(?:\d+(?:\.\d+)*|[A-Z])\s*[—–-]\s*')   # «Table 8.1 — », «Table A — » before 24 Nov 2026
KEY = re.compile(r'\{\{TBL:([a-z0-9#-]+)\}\}')

# the titles of a brief's two kinds of table, by the first header cell, when the brief gives none (the briefs' own words:
# «Records timeline» / «Хронология рекордов» / «ציר הזמן של השיאים», «Who.» / «Кто.» / «מי.»)
DOC_TITLES = {
    'en': {'year': 'Records timeline', 'date': 'Records timeline', 'organisation': 'Who'},
    'ru': {'год': 'Хронология рекордов', 'дата': 'Хронология рекордов', 'организация': 'Кто'},
    'he': {'שנה': 'ציר הזמן של השיאים', 'תאריך': 'ציר הזמן של השיאים', 'ארגון': 'מי'},
}

_FOLD = re.compile(r'(<details class="tblfold" id="([^"]+)"[^>]*><summary>)(.*?)(</summary>)', re.S)
_BIG = re.compile(r'(<details class="fold big-table"><summary>)(.*?)(</summary>)', re.S)
_HEAD = re.compile(r'<h([23]) id="([a-z]+)-(s[a-z0-9-]+)"')


def _plain(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', '', s or ''))).strip()


def label(L, num):
    return '<span class="tno">%s&nbsp;<bdi dir="ltr">%s</bdi></span>' % (WORD.get(L, WORD['en']), num)


def _title(inner, L):
    """the title's HTML from a summary's inner HTML: the strong run's content, the old «Table 8.1 — » prefix and a final period
    dropped, the first letter capitalised (sentence case; Hebrew has no case)"""
    s = inner.strip()
    m = re.fullmatch(r'<strong>(.*)</strong>', s, re.S)
    if m:
        s = m.group(1).strip()
    lead = re.match(r'((?:<[^>]+>)*)', s).group(1)   # tags before the first letter stay in front of it
    body = OLD.sub('', s[len(lead):])
    body = re.sub(r'\.\s*$', '', body)
    body = body.replace(' — ', ': ', 1)   # the label's dash is the only one: «Table 8-5 — Verdict history: one row per edition»
    if body[:1].isalpha():
        body = body[:1].upper() + body[1:]
    return lead + body


def caption(L, num, title):
    return '<strong>%s%s</strong>' % (label(L, num), (' — ' + title) if title else '')


def _first_header(h, pos):
    m = re.search(r'<th[^>]*>(.*?)</th>', h[pos:pos + 4000], re.S)
    return _plain(m.group(1)).lower() if m else ''


def number_report(h, L):
    """The report body of language L: every table fold and big-table fold numbered per chapter (§N, from the h2 ids L-sN), the
    summary replaced by «label — title». Returns (html, {key: number}); key = the nearest heading's id without the language
    prefix (s8-3), and #k for the k-th table under the same heading (s7-10#2). A table before §1 or in an unnumbered chapter
    stops the build: it would carry no number."""
    keys, out, pos = {}, [], 0
    chap, sec, nsec, nchap = None, None, {}, {}
    events = sorted([(m.start(), 'h', m) for m in _HEAD.finditer(h) if m.group(2) == L] +
                    [(m.start(), 'f', m) for m in _FOLD.finditer(h)] +
                    [(m.start(), 'b', m) for m in _BIG.finditer(h)], key=lambda x: x[0])
    for at, kind, m in events:
        if kind == 'h':
            sec = m.group(3)
            if m.group(1) == '2':
                c = re.match(r's(\d+)$', sec)
                chap = c.group(1) if c else None
            continue
        if kind == 'f' and m.group(2).startswith('brief-'):
            continue   # a brief's table: numbered within its brief (number_doc)
        if chap is None:
            raise SystemExit('tables.number_report: a table under %s (%s) has no chapter number' % (sec, L))
        nchap[chap] = nchap.get(chap, 0) + 1
        num = '%s-%d' % (chap, nchap[chap])
        nsec[sec] = nsec.get(sec, 0) + 1
        key = sec if nsec[sec] == 1 else '%s#%d' % (sec, nsec[sec])
        if kind == 'f':
            inner = m.group(3)
            title = '' if _plain(inner).lower() in GENERIC else _title(inner, L)
            new = m.group(1) + caption(L, num, title) + m.group(4)
            anchor = m.group(2)
            if not title:
                raise SystemExit('tables.number_report: table %s (%s, %s) has no title — give it a bold caption line' % (num, key, L))
        else:
            inner = m.group(2)
            show = _plain(inner) in SHOW.values()
            title = '' if show else _title(inner, L)
            if show:
                raise SystemExit('tables.number_report: big table %s (%s, %s) is labelled «%s» only — give it a title' % (num, key, L, _plain(inner)))
            anchor = '%s-tbl-%s' % (L, key.replace('#', '-'))   # a big table's fold gets an id of its own, the link's target
            new = m.group(1).replace('<details class="fold big-table">', '<details class="fold big-table" id="%s">' % anchor) + caption(L, num, title) + m.group(3)
        keys[key] = (num, anchor)
        out.append(h[pos:at]); out.append(new); pos = m.end()
    out.append(h[pos:])
    return ''.join(out), keys


def number_doc(h, L):
    """One document — a brief's language half, a record page's body: its tables numbered from 1 in order. A table fold gets
    «label — title» as its summary, the title from its caption or, failing one, from the kind of table its first header names
    (DOC_TITLES); a plain table right under a heading (a record page's «Technologies by layer — …») takes the label into that
    heading, which is its caption: «Table 1 — Technologies by layer: the machine's cell per layer». Returns the html."""
    out, pos, n = [], 0, 0
    plain = [(m.start(), 'p', m) for m in re.finditer(r'(<h[2-4][^>]*>)((?:(?!</h[2-4]>).)*)(</h[2-4]>)(?=\s*<table\b)', h, re.S)]
    events = sorted([(m.start(), 'f', m) for m in _FOLD.finditer(h)] + plain, key=lambda x: x[0])
    for at, kind, m in events:
        n += 1
        if kind == 'f':
            inner = m.group(3)
            title = '' if _plain(inner).lower() in GENERIC else _title(inner, L)
            if not title:
                title = DOC_TITLES.get(L, DOC_TITLES['en']).get(_first_header(h, m.end()), '')
            if not title:
                raise SystemExit('tables.number_doc: table %d of a %s document has no title and no known kind (header «%s»)' % (n, L, _first_header(h, m.end())))
            out.append(h[pos:at]); out.append(m.group(1) + caption(L, str(n), title) + m.group(4)); pos = m.end()
        else:
            words = re.sub(r'\s+[—–]\s+', ': ', _plain(m.group(2)), count=1)
            out.append(h[pos:at]); out.append(m.group(1) + label(L, str(n)) + ' — ' + _html.escape(words, quote=False) + m.group(3)); pos = m.end()
    out.append(h[pos:])
    return ''.join(out)


def number_briefs(block):
    """The briefs' block of the main page: every language half of every brief numbered as one document (number_doc) — the
    block split before each <div class="bl lang-…">, as page_blocks splits it; a piece runs to the next half."""
    out = []
    for x in re.split(r'(?=<div class="bl lang-\w+"[ >])', block):
        m = re.match(r'<div class="bl lang-(\w+)"', x)
        out.append(number_doc(x, m.group(1)) if m else x)
    return ''.join(out)


def resolve(h, L, keys, where=''):
    """Every {{TBL:key}} of h replaced by its number (keys: key → (number, anchor)); in running text the number links to the
    table (a record page's link to the main page is rewritten by pages.py like every in-page link); inside a link, a tag or an
    attribute it is the bare number. An unknown key stops the build."""
    bad = sorted({k for k in KEY.findall(h) if k not in keys})
    if bad:
        raise SystemExit('tables.resolve: unknown table key(s) %s in %s (%s)' % (', '.join(bad), where or 'a page', L))
    if '{{TBL:' not in h:
        return h
    out = []
    for part in re.split(r'(<a\b[^>]*>.*?</a>|<button\b[^>]*>.*?</button>|<[^>]*>)', h, flags=re.S):   # no link inside a link or a button
        if part.startswith('<'):
            out.append(KEY.sub(lambda m: keys[m.group(1)][0], part))
        else:
            out.append(KEY.sub(lambda m: '<a class="xref" href="#%s">%s</a>' % (keys[m.group(1)][1], keys[m.group(1)][0]), part))
    return ''.join(out)


def resolve_plain(s, L, keys, where=''):
    """the keys of a plain text (a meta description) replaced by the bare numbers"""
    bad = sorted({k for k in KEY.findall(s) if k not in keys})
    if bad:
        raise SystemExit('tables.resolve_plain: unknown table key(s) %s in %s (%s)' % (', '.join(bad), where or 'a text', L))
    return KEY.sub(lambda m: keys[m.group(1)][0], s)


def resolve_halves(block, keys_by_lang, where='the briefs'):
    """resolve() over the briefs' block, each language half with its own language's keys"""
    out = []
    for x in re.split(r'(?=<div class="bl lang-\w+"[ >])', block):
        m = re.match(r'<div class="bl lang-(\w+)"', x)
        out.append(resolve(x, m.group(1), keys_by_lang[m.group(1)], where) if m and '{{TBL:' in x else x)
    return ''.join(out)
