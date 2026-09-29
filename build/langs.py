# -*- coding: utf-8 -*-
"""The Atlas's languages — one definition for every generator (29 Sep 2026: Hebrew joins English and Russian; until then the
build assumed exactly two languages). A language is added here and in its string tables; no other file names the list.

    LANGS        page order; the language switches list the languages in this order
    NATIVE       each language's own name (the switches, the Find menu, the record pages' language links)
    DIR          writing direction ('rtl'); a language not listed is 'ltr'
    FOLDER       a language's pages below dist/ ('' for English, 'ru/', 'he/')
    pick(L, x)   the language's item of a (en, ru[, he]) tuple/list or an {en, ru, he} dict — English when it is missing
"""
import re

LANGS = ['en', 'ru', 'he']
NATIVE = {'en': 'English', 'ru': 'Русский', 'he': 'עברית'}
DIR = {'he': 'rtl'}
FOLDER = {'en': '', 'ru': 'ru/', 'he': 'he/'}
FALLBACK = 'en'
IDX = {L: i for i, L in enumerate(LANGS)}   # a language's position in a (en, ru, he) tuple


def direction(L): return DIR.get(L, 'ltr')


def others(L): return [x for x in LANGS if x != L]


def up(L):
    """from a language's folder to dist/ ('' for English, '../' for ru/ and he/)"""
    return '../' * FOLDER[L].count('/')


def pick(L, x):
    """the language's item of a 2/3-tuple/list (en, ru[, he]) or of an {en, ru, he} dict; English when that item is missing or
    empty (a two-element pair keeps working: Hebrew then reads English until its third element is written)"""
    if isinstance(x, dict):
        v = x.get(L)
        return v if v not in (None, '') else x.get(FALLBACK)
    if isinstance(x, (tuple, list)):
        i = IDX.get(L, 0)
        v = x[i] if i < len(x) else None
        return v if v not in (None, '') else (x[0] if x else None)
    return x


def has(L, x):
    """True when x carries the language's own text (no fallback)"""
    if isinstance(x, dict): return x.get(L) not in (None, '')
    if isinstance(x, (tuple, list)):
        i = IDX.get(L, 0); return i < len(x) and x[i] not in (None, '')
    return L == FALLBACK


def fb_attrs(L, fallback=True):
    """the attributes of an element that shows English in place of language L: lang="en", and dir="ltr" inside a right-to-left
    language, so an English sentence keeps its punctuation where it belongs (29 Sep 2026)"""
    if not fallback or L == FALLBACK: return ''
    return ' lang="en"' + (' dir="ltr"' if direction(L) == 'rtl' else '')


def spans(texts, tag='span', cls='', attrs=''):
    """one element per language — <span class="lang-en">…</span><span class="lang-ru">…</span><span class="lang-he">…</span> — the
    missing languages in English (marked with fb_attrs); the page's stylesheet shows the current language's element only"""
    out = []
    for L in LANGS:
        c = ((cls + ' ') if cls else '') + 'lang-' + L
        out.append('<%s class="%s"%s%s>%s</%s>' % (tag, c, attrs, fb_attrs(L, not has(L, texts)), pick(L, texts), tag))
    return ''.join(out)


def js_config():
    """window.__LANGS for the page's scripts (the switch, the fragments, Find, the feedback sheet)"""
    import json
    return json.dumps({'list': LANGS, 'native': NATIVE, 'dir': {L: direction(L) for L in LANGS}, 'folder': FOLDER}, ensure_ascii=False, separators=(',', ':'))


# ---------- the twins of a template's language pairs (29 Sep 2026) ---------------------------------------------------------
# The templates of build_html.py (the map's controls, the masthead, the phone bar, Find, the feedback sheet) write their UI strings
# as sibling elements <x class="… lang-en">…</x><x class="… lang-ru">…</x>. Where a group lacks a language, fill_twins() adds that
# language's element after the group as a copy of the English one (marked with fb_attrs), so that every language shows a label and
# a translation only has to add its own element. Only groups of two languages or more are completed (a lone lang-en is meant to be
# English-only), never inside a script or a style; a copy that would duplicate an id stops the build.
_ATTRS = r'''(?:[^>"']|"[^"]*"|'[^']*')*'''   # a start tag's attributes, quoted values may hold '>'
_OPEN = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)\b(?=%s?\sclass="(?:[^"]*\s)?lang-(%s)(?:\s[^"]*)?")%s>' % (_ATTRS, '|'.join(LANGS), _ATTRS))
_ENDS = {}


def _end(h, name, pos):
    """the end of the element whose start tag ends at pos (same-name nesting counted)"""
    rx = _ENDS.get(name)
    if rx is None: rx = _ENDS[name] = re.compile(r'<(/?)%s\b%s>' % (name, _ATTRS), re.I)
    depth = 1
    for m in rx.finditer(h, pos):
        if m.group(1): depth -= 1
        elif not m.group(0).endswith('/>'): depth += 1
        if not depth: return m.end()
    return -1


def _complete(h):
    out = []; pos = 0; i = 0
    while True:
        m = _OPEN.search(h, i)
        if not m: break
        group = []; cur = m   # the sibling elements of one group: (lang, start, end of start tag, start of end tag, end)
        while cur and cur.group(2) not in [g[0] for g in group]:   # a language met again starts the next group
            e = _end(h, cur.group(1), cur.end())
            if e < 0: break
            group.append((cur.group(2), cur.start(), cur.end(), h.rfind('<', 0, e), e))
            s = e
            while s < len(h) and h[s] in ' \t\r\n': s += 1
            cur = _OPEN.match(h, s)
        if not group: i = m.end(); continue
        els = {}
        for L, a, b, cs, e in group:   # each member with its own inner groups completed
            out.append(h[pos:a]); el = h[a:b] + _complete(h[b:cs]) + h[cs:e]; out.append(el); els.setdefault(L, (el, b - a)); pos = e
        if len(group) >= 2 and LANGS[0] in els and set(els) != set(LANGS):
            src, tag_end = els[LANGS[0]]
            if ' id="' in src: raise SystemExit('langs.fill_twins: an English element with an id cannot be copied: %s' % src[:120])
            tag_end -= 1   # the start tag without its '>'
            for L in LANGS:
                if L in els: continue
                start = src[:tag_end].replace('lang-' + LANGS[0], 'lang-' + L, 1)
                start = re.sub(r' (?:lang|dir)="[^"]*"', '', start)
                out.append(start + fb_attrs(L) + src[tag_end:])
        i = pos
    out.append(h[pos:])
    return ''.join(out)


def fill_twins(h):
    """complete every language group of the markup h (scripts and styles left as they are)"""
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', h, flags=re.S | re.I)
    return ''.join(p if p[:7].lower() in ('<script', '<style>', '<style ') else _complete(p) for p in parts)
