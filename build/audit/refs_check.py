#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent validation of every reference list in the built page: §9 (en, ru) and the 96 × 2 brief lists.

    python3 build/audit/refs_check.py [dist.html]        # exit 1 on any defect; prints one line per class

Reads the rendered page, not the data files, so it catches what the reader sees. Checks:
  numbering   numbers are the Map's permanent work numbers: each list ascends without repeats (gaps are normal — a brief shows
              its subset of the bibliography); every in-text citation [n] links to entry n of ITS OWN list; every entry is
              cited at least once from its own text (an uncited entry is dead weight); no bare "[n]" left as text
  one number  the same work (DOI, arXiv id or URL) carries the same number in §9 and in every brief, and one number never
              stands for two works
  ru = en     the Russian list of a brief has the same entries, in the same order, as the English one (a bibliography is not
              translated); the multiset of citation numbers in the RU text equals the EN one
  one work    the same work (DOI, arXiv id or URL) prints the same entry everywhere — in §9 and in every brief; a work with
              two different entries is reported with both forms
  formatting  every entry follows one of the IEEE forms the build emits (journal / preprint / report / online), with a
              linked identifier or URL, a final period, no doubled punctuation, no raw markdown, no "None"; the
              key-reference tooltips carry no markdown link syntax; the grade tag (D/C/S/G/P/R) follows a brief entry
  anchors     every href="#…src-n" resolves; every entry id is unique
"""
import collections, html as H, re, sys

PAGE = sys.argv[1] if len(sys.argv) > 1 else 'dist/Quantum-Technology-Map-2026.09.html'
h = open(PAGE, encoding='utf-8').read()
P = []   # problems
def prob(kind, msg): P.append((kind, msg))

def text(s):
    return H.unescape(re.sub(r'<[^>]+>', '', s))

# ---------- collect lists (entry id -> scope, number); §9 ids are "en-src-CODE[-k]", brief ids "brief-<bid>-<lang>-src-<n>"
LI = re.compile(r'<li id="([^"]+)" value="(\d+)"><span class="src">\[(\d+)\]</span> <span class="ref">(.*?)</span>(.*?)</li>', re.S)
def scope_of(lid):
    m = re.match(r'(brief-[a-z0-9_]+-(?:en|ru)-src)-\d+$', lid)
    if m: return m.group(1)
    m = re.match(r'((?:en|ru)-src)-', lid)
    return m.group(1) if m else lid
lists = {}; entry = {}
for m in LI.finditer(h):
    lid, val, n, ref, tail = m.groups()
    scope = scope_of(lid)
    lists.setdefault(scope, []).append((int(n), int(val), ref, tail, lid))
    entry[lid] = (scope, int(n))
print('lists:', len(lists), 'entries:', sum(len(v) for v in lists.values()))
ids = re.findall(r' id="([^"]+)"', h); c = collections.Counter(ids)
dup = [i for i, k in c.items() if k > 1 and 'src' in i]
if dup: prob('anchors', 'duplicate entry ids: %s' % dup[:5])

# ---------- numbering per list; citations per scope
CITE = re.compile(r'<a class="cite" href="#([^"]+)">\[(\d+)\]</a>')
cites = collections.defaultdict(list)
for m in CITE.finditer(h):
    tid, shown = m.group(1), int(m.group(2))
    if tid not in entry: prob('anchors', 'citation [%d] -> #%s: no such entry' % (shown, tid)); continue
    scope, n = entry[tid]
    cites[scope].append(n)
    if n != shown: prob('numbering', '%s: citation shows [%d] but links to entry %d (%s)' % (scope, shown, n, tid))
RANGE = re.compile(r'<a class="cite" href="#([^"]+)">\[(\d+)\]</a>–<a class="cite" href="#([^"]+)">\[(\d+)\]</a>')
for m in RANGE.finditer(h):
    a, b = int(m.group(2)), int(m.group(4)); scope = entry.get(m.group(1), (None, 0))[0]
    if scope: cites[scope] += list(range(a + 1, b))
for scope, items in lists.items():
    ns = [n for n, v, r, t, l in items]
    if ns != sorted(set(ns)): prob('numbering', '%s: numbers not ascending or repeated: %s…' % (scope, ns[:8]))
    for n, v, r, t, l in items:
        if n != v: prob('numbering', '%s: [%d] has value=%d' % (scope, n, v))
    used = set(cites.get(scope, []))
    for n in ns:
        if n not in used: prob('numbering', '%s: entry [%d] is never cited' % (scope, n))
for scope in cites:
    if scope not in lists: prob('anchors', '%s: citations but no list' % scope)

# ---------- ru = en for briefs
briefs = sorted({s.split('-')[1] for s in lists if s.startswith('brief-')})
for b in briefs:
    en = lists.get('brief-%s-en-src' % b, []); ru = lists.get('brief-%s-ru-src' % b, [])
    en_refs = [text(r) for n, v, r, t, l in en]; ru_refs = [text(r) for n, v, r, t, l in ru]
    if en_refs != ru_refs:
        diff = [(i + 1) for i, (a, bb) in enumerate(zip(en_refs, ru_refs)) if a != bb]
        prob('ru=en', '%s: RU list differs from EN (len %d vs %d; first differing entries %s)' % (b, len(en_refs), len(ru_refs), diff[:4]))
    ce = collections.Counter(cites.get('brief-%s-en-src' % b, [])); cr = collections.Counter(cites.get('brief-%s-ru-src' % b, []))
    if ce != cr:
        d = {n: (ce[n], cr[n]) for n in set(ce) | set(cr) if ce[n] != cr[n]}
        prob('ru=en', '%s: citation counts differ EN vs RU: %s' % (b, dict(list(d.items())[:6])))

# ---------- one work, one entry
def key_of(ref_html):
    m = re.search(r'href="https://doi\.org/([^"]+)"', ref_html)
    if m: return 'doi:' + m.group(1).lower()
    m = re.search(r'href="https://arxiv\.org/abs/([^"]+)"', ref_html)
    if m: return 'arxiv:' + m.group(1).lower()
    m = re.search(r'Available: <a href="([^"]+)"', ref_html)
    if m: return 'url:' + m.group(1).rstrip('/').lower()
    m = re.search(r'href="([^"#]+)"', ref_html)   # an in-page link (the Map citing its own section) is no identity
    return ('url:' + m.group(1).rstrip('/').lower()) if m else None
forms = collections.defaultdict(dict)   # key -> {entry text: [scopes]}
nokey = []
for scope, items in lists.items():
    for n, v, r, t, l in items:
        k = key_of(r)
        if not k:
            if 'class="xref"' not in r: nokey.append((scope, n, text(r)[:80]))
            continue
        forms[k].setdefault(text(r), []).append('%s[%d]' % (scope.replace('-src', ''), n))
for k, d in forms.items():
    if len(d) > 1:
        prob('one-work', '%s has %d entry forms: %s' % (k, len(d), ' || '.join('%r @ %s' % (f[:110], s[:3]) for f, s in d.items())))
# one number per work, one work per number — across §9 and every brief
num_of = collections.defaultdict(set); key_of_num = collections.defaultdict(set)
for scope, items in lists.items():
    for n, v, r, t, l in items:
        k = key_of(r)
        if not k: continue
        num_of[k].add(n); key_of_num[n].add(k)
for k, ns in num_of.items():
    if len(ns) > 1: prob('one-number', '%s carries numbers %s' % (k, sorted(ns)))
for n, ks in key_of_num.items():
    if len(ks) > 1: prob('one-number', '[%d] stands for %d works: %s' % (n, len(ks), sorted(ks)[:3]))
if nokey: prob('formatting', '%d entries carry no identifier or link, e.g. %s' % (len(nokey), nokey[:3]))

# ---------- formatting
A_ = r'(?:.+?, )?'                                   # authors or organisation (may be absent on a web entry)
T_ = r'“[^”]+[,.]”'                                     # title, closing with ,” (more follows) or .” (nothing follows but the link)
L_ = r'<a href="[^"]+"[^>]*>[^<]+</a>'
D_ = r'(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.? (?:\d{1,2}, )?)?\d{4}'
JOUR = re.compile(r'^' + A_ + T_ + r' <i>[^<]+</i>(?:, vol\. [^,]+)?(?:, no\. [^,]+)?(?:, (?:pp\. [^,]+|Art\. no\. [^,]+|p\. [^,]+))?(?:, ' + D_ + r')?(?:, doi: ' + L_ + r'\.|\.(?: \[Online\]\. Available: ' + L_ + r')?)(?: ' + L_ + r'\.)?(?: Also ' + L_ + r'\.)*$')
PRE = re.compile(r'^' + A_ + T_ + r' ' + L_ + r'(?:, ' + D_ + r')?\.(?: Also ' + L_ + r'\.)*$')
REP = re.compile(r'^' + A_ + T_ + r'(?: [^<]+?)?(?:, ' + D_ + r')?(?:, doi: ' + L_ + r'\.(?: \[Online\]\. Available: ' + L_ + r')?|\.(?: \[Online\]\. Available: ' + L_ + r')?)(?: Also ' + L_ + r'\.)*$')
WEB = re.compile(r'^' + A_ + T_ + r'(?: [^<]*?' + D_ + r'\.| [^<]+?\.)? \[Online\]\. Available: ' + L_ + r'(?: Also ' + L_ + r'\.)*$')
kinds = collections.Counter()
for scope, items in lists.items():
    for n, v, r, t, l in items:
        r = r.strip().replace('<wbr>', '')   # break opportunities inside link text are not part of the form
        if JOUR.match(r): kinds['journal'] += 1
        elif PRE.match(r): kinds['preprint'] += 1
        elif WEB.match(r): kinds['web'] += 1
        elif REP.match(r): kinds['report/other'] += 1
        elif re.match(r'^R\. Neeman, “Quantum Technology Map,”.*<a class="xref"', r): kinds['self'] += 1
        elif ' Retracted: <i>' in r and JOUR.match(r.split(' Retracted: ')[0]): kinds['journal (retracted)'] += 1
        else: kinds['UNMATCHED'] += 1; prob('formatting', '%s[%d]: form not recognised: %s' % (scope.replace('-src', ''), n, text(r)[:140]))
        tx = text(r)
        for bad, why in ((',,', 'doubled comma'), ('..', 'doubled period'), (',.', 'comma-period'), ('None', '"None"'), ('](http', 'raw markdown'), ('  ', 'double space'), ('“,', 'empty title'), (' ,', 'space before comma')):
            if bad in tx and not (bad == '..' and '...' in tx): prob('formatting', '%s[%d]: %s in %r' % (scope.replace('-src', ''), n, why, tx[:120]))
        if scope.startswith('brief-') and not re.search(r'<span class="tag tag-[DCSGPR]"', t): prob('grade', '%s[%d]: no grade tag' % (scope.replace('-src', ''), n))
print('forms:', dict(kinds))
# tooltips of the key references
for m in re.finditer(r'<div class="bkeys">.*?</div>', h, flags=re.S):
    for t in re.findall(r'title="([^"]*)"', m.group(0)):
        if '](http' in t: prob('formatting', 'key-reference tooltip carries markdown: %s' % H.unescape(t)[:100])
# bare [n] left in the prose of the briefs and the report (a citation not linked)
bare = re.findall(r'(?<![\w\[>])\[(\d{1,4})\](?![\]\(<])', re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S))
if bare: prob('numbering', 'bare [n] tokens in the rendered text (unlinked citations): %d, e.g. %s' % (len(bare), bare[:6]))
# anchors
for m in re.finditer(r'href="#((?:en|ru)-src-[^"]+|brief-[^"]+-src-\d+)"', h):
    if ' id="%s"' % m.group(1) not in h: prob('anchors', 'dangling %s' % m.group(1))

# ---------- report
by = collections.Counter(k for k, m in P)
print('problems by class:', dict(by) or 'none')
for k in by:
    ex = [m for kk, m in P if kk == k]
    for m in ex[:10]: print('  [%s] %s' % (k, m))
    if len(ex) > 10: print('  [%s] … %d more' % (k, len(ex) - 10))
sys.exit(1 if any(k != 'grade' for k in by) else 0)
