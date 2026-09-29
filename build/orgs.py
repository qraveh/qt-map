#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Organisation profiles for the Atlas: the snapshot data/orgs/organisations.json, the organisation card and the linker that
turns organisation names in a page into links to their cards (spec of 27 Sep 2026, with the follow-up decisions of the same
day). Python 3.11, stdlib only.

    python3 build/orgs.py --import    read the register and the Atlas data, write data/orgs/organisations.json
    python3 build/orgs.py --check     print counts: organisations by tier, machines resolved by each rule, the names that
                                      resolved to no register row, path actors matched / unmatched; exits 0

    import orgs
    orgs.load() · orgs.by_slug() · orgs.slug_for_machine(machine) · orgs.link_orgs(text, lang, base)
    orgs.profile_html(o, lang, base, machines_by_id, node_by_id, path_by_id)

Inputs (read-only): data/machines.json, data/graph.json, briefs/en/*.md, and the organisation register (SP04) in
QT_REGISTER_DIR if set, else /home/claude/work/QT-Map/quantum-register: quantum-organisation-register.csv,
corporate-families.csv, data/machines-by-organisation.csv, data/academic-bodies.csv, data/org-machine-relations.csv,
data/body-machine-relations.csv. The Atlas reads only the snapshot; the register is needed by --import (and by --check for the
per-rule counts).

Which organisations. Every organisation that builds a machine of data/machines.json, by the machine's org_id:
  1   a register name                → that register row (name, tier, segment, country, city, url, note)
  1*  none of the forms of rules 1-3 ("ionq", "hrl": an id rather than a name) → the register row whose name equals it
      ignoring case, else the only row whose first word equals it and whose name, less its parenthetical remarks, opens the
      machine's `org` string; failing both, rule 3 on the `org` string
  2   an academic-body id (ab-…)     → the body's row of academic-bodies.csv (name, country, city, website as url); tier
      "academic"; an id that the file lacks is resolved by rule 3 on the `org` string
  3   "unmatched"                    → the register row whose name, or one of whose rolled-up units (the register column and
      corporate-families.csv), equals the `org` string ignoring case
  3+  failing that, a string that opens with a register organisation - its name, a rolled-up unit, the `org` string of a
      machine already resolved to it, or a short name of ALIASES - followed by " with ", "(" or " / ": that organisation builds
      the machine. After " with " the first party named is the machine's host (a hosts entry); a parenthesis holds a remark;
      the parts of "A / B" are co-builders and the first one the register knows builds it ("CAS / Peking University")
  -   failing all, an entry named by the string, tier "unregistered"
Added to these: every organisation that a path's actors string names by its register name or a short name of ALIASES
(parenthetical remarks and "→ owner" removed, then split on ",", ";", " and ", "/"), with its data from the register and
possibly no machine. MERGE folds a register row named by the actors into the organisation that owns the machines under
another row ("Google" → Google Quantum AI); DISPLAY_NAME gives that organisation the name it is shown under.
Aliases: the distinct `org` strings of its machines, the rows merged into it, its short names (ALIASES) and, when it is shown
under a display name, its register name.

Fields. machines: ids by status class (DEPLOYED, DEMONSTRATED, ANNOUNCED, PLANNED, RETIRED, other; as machines_chapter.py) then
name. families: of its machines and architectures, in the report's family order. architectures: the paths of its machines and
the paths whose actors name it, in graph order. technologies: the 12 technologies held by most of its machines (a machine counts once
per technology; ties by layer, then graph order). hosts: machines whose host is not the organisation itself - from
machines-by-organisation.csv when the host text does not open with one of its own names (name, name less parenthetical
remarks, an abbreviation in parentheses, the initials of its name, its first word when the other words are generic, an
alias) nor names the same parties as its name or an alias (EQUIV: "CAS" = "Chinese Academy of Sciences"), or when the
relations tables give the machine a host, on-premise customer, colocation site, operator or owner that is not the
organisation; and from rule 3+ (" with "). note: the register's note, less notes that are curation remarks (NOTE_REMARKS).
mentions: the English briefs that name it, most mentions first, and the total number of mentions.

Matching of names (brief mentions and link_orgs alike): case-sensitive, whole words; a name shorter than 4 characters counts
only as a whole whitespace-delimited token (surrounding brackets, quotes, final punctuation and a possessive 's allowed).
Where names overlap, the longest wins ("Google Quantum AI" before "Google"), and each span belongs to one organisation. A name
followed in the same sentence by the word Computation / Computing (either case) that the organisation's own name lacks is a
phrase, not a mention ("Universal Quantum Computation" is not the company Universal Quantum).
"""
import csv, datetime, html, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'orgs', 'organisations.json')
MACHINES = os.path.join(ROOT, 'data', 'machines.json')
GRAPH = os.path.join(ROOT, 'data', 'graph.json')
BRIEFS = os.path.join(ROOT, 'briefs', 'en')
_REG_LIVE = '/home/claude/work/QT-Map/quantum-register'
REGISTER_LABEL = 'quantum-register (SP04)'

FAM_ORDER = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']     # as machines_chapter.FAM_ORDER
STAT_ORDER = ['DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED', 'RETIRED', 'OTHER']   # as machines_chapter.STAT_ORDER
TOP_STATIONS = 12
HOST_RELATIONS = ('hosts', 'customer-onprem', 'colocates', 'operates', 'owns')
# words that make a name generic after its first word ("Rigetti Computing", "Duke University"): the first word then names it
GENERIC_WORDS = {'ai', 'computing', 'computers', 'computer', 'corp', 'corporation', 'group', 'inc', 'labs', 'laboratories',
                 'laboratory', 'ltd', 'quantique', 'quantum', 'research', 'systems', 'tech', 'technologies', 'technology', 'university'}

# A register row that the path actors name, folded into the organisation that owns the machines under another row
MERGE = {'Google': ('reg', 'Google Quantum AI (ex-Atlantic Quantum)'),
         'USTC': ('reg', 'University of Science and Technology of China'),
         'ICFO': ('body', 'ab-es-icfo')}
DISPLAY_NAME = {('reg', 'Google Quantum AI (ex-Atlantic Quantum)'): 'Google Quantum AI'}
# Short and brand names → the register row they stand for; they count in the briefs and link like the name itself
ALIASES = {
    'Rigetti': 'Rigetti Computing',
    'AWS': 'Amazon Web Services',
    'D-Wave': 'D-Wave Quantum',
    'QCI': 'D-Wave Quantum',                    # Quantum Circuits Inc. is no register row: a rolled-up unit of D-Wave Quantum
    'Quantum Circuits Inc.': 'D-Wave Quantum',
    'HRL': 'HRL Laboratories (IBM)',
    'OQC': 'Oxford Quantum Circuits (OQC)',
    'SQC': 'Silicon Quantum Computing',
    'QuEra': 'QuEra Computing',
    'AQT': 'Alpine Quantum Technologies',
    'Oxford Ionics': 'IonQ',                    # a rolled-up unit of IonQ (acquired 2025)
    'Harvard': 'Harvard University',
    'MIT': 'Massachusetts Institute of Technology',
    'Caltech': 'California Institute of Technology',
    'Princeton': 'Princeton University',
    'Innsbruck': 'University of Innsbruck',
    'Maryland': 'University of Maryland, College Park',
    'Duke': 'Duke University',
    'Zhejiang': 'Zhejiang University',
    'SUSTech': 'Southern University of Science and Technology',
    'RIKEN': 'RIKEN Center for Quantum Computing',
    'Qudoor': 'QUDOOR',
    'QUDORA': 'Qudora Technologies',
    'QuiX': 'QuiX Quantum',
    'ORCA': 'ORCA Computing',
    'Groove': 'Groove Quantum',
    'Photonic Inc': 'Photonic Inc.',
}
EQUIV = {'chinese academy of sciences': 'cas'}          # one body under two names, for the host rule
NOTE_REMARKS = ('UNMATCHED ORG', 'org-alignment', 'body_id', 'must be carried', 'duplicate of')
GUARD_WORDS = ('Computation', 'Computing', 'computing', 'computation')

HEAD = {'en': ('Machines in the Atlas', 'Technologies its machines use', 'Architectures', 'Mentioned in the briefs of'),
        'ru': ('Машины в Атласе', 'Технологии её машин', 'Архитектуры', 'Упоминается в брифах')}
HEAD_CO = {'en': 'Machines it co-developed (filed under another organisation)', 'ru': 'Машины, созданные с её участием (учтены за другой организацией)'}
RULES = [('1', 'org_id is a register name'),
         ('1*', 'org_id is an id form of a register name (case, first word)'),
         ('2', 'org_id is an academic body of academic-bodies.csv'),
         ('3', 'org string equals a register name or rolled-up unit (ignoring case)'),
         ('3+', 'org string opens with a register organisation followed by " with ", "(" or " / "'),
         ('-', 'no register row: unregistered')]


# ---------------------------------------------------------------------------------------------------------------- text helpers

def slugify(name):
    """IBM → ibm; Alice & Bob → alice-bob; Université de Sherbrooke → universite-de-sherbrooke."""
    s = unicodedata.normalize('NFKD', name or '').encode('ascii', 'ignore').decode('ascii').lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-') or 'org'


def strip_par(s):
    """The string less its parenthetical remarks (nested ones too) and stray parentheses, whitespace collapsed."""
    s, prev = s or '', None
    while prev != s:
        prev, s = s, re.sub(r'\([^()]*\)', ' ', s)
    return ' '.join(s.replace('(', ' ').replace(')', ' ').split())


def split_actors(s):
    """A path's actors string → organisation names: parenthetical remarks and "→ owner" removed ("HRL→IBM" is HRL, now
    IBM's), then split on ',', ';', ' and ', '/'."""
    s = re.sub(r'\s*→\s*[^,;/]*', '', strip_par(s))
    return [t.strip() for t in re.split(r',|;| and |/', s) if t.strip()]


def status_class(s):
    u = (s or '').upper()
    for k in ('RETIRED', 'DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED'):
        if u.startswith(k):
            return k
    return 'OTHER'


def _ws(s):
    return ' '.join((s or '').split())


def _opens_with(text, names):
    """True when text (ignoring case) begins with one of names, followed by a non-alphanumeric character or the end."""
    t = _ws(text).casefold()
    for n in names:
        k = _ws(n).casefold()
        if k and t.startswith(k) and (len(t) == len(k) or not t[len(k)].isalnum()):
            return True
    return False


def own_names(name, aliases=()):
    """The names an organisation goes by in the register's free text (used to tell its own sites from a host)."""
    out = set()
    for n in [name] + list(aliases):
        n = _ws(n)
        if not n:
            continue
        out.add(n)
        if strip_par(n):
            out.add(strip_par(n))
        for inner in re.findall(r'\(([^()]+)\)', n):          # an abbreviation given in parentheses: OQC, KRISS
            if re.fullmatch(r'[A-Z][A-Z0-9&.\-]+', inner.strip()):
                out.add(inner.strip())
    words = strip_par(name).split()
    initials = ''.join(w[0] for w in words if w[:1].isupper())
    if len(initials) >= 3:                                     # USTC, BAQIS, AWS, IQCC
        out.add(initials)
    if len(words) >= 2 and len(words[0]) >= 4 and all(w.lower().strip('.,') in GENERIC_WORDS for w in words[1:]):
        out.add(words[0])                                      # Rigetti, QuEra, D-Wave, Duke
    return out


def parties(s):
    """The parties a host text or an org string names first: "Chinese Academy of Sciences + Peking University - lab" and
    "CAS / Peking University" both → {cas, peking university}."""
    lead = strip_par(re.split(r';|\s[-–—]\s', s or '')[0])
    out = set()
    for p in re.split(r'\s*(?:,|\+|/|\band\b|\bwith\b)\s*', lead):
        p = _ws(p).strip(' .').casefold()
        if p:
            out.add(EQUIV.get(p, p))
    return frozenset(out)


def first_party(s):
    """The first party of a list such as "ETH Zurich (CSCS) and Lockheed Martin" (split outside parentheses)."""
    depth = 0
    for i, c in enumerate(s):
        if c == '(':
            depth += 1
        elif c == ')':
            depth = max(0, depth - 1)
        elif depth == 0 and (c in ',;' or s.startswith(' and ', i)):
            return s[:i].strip()
    return s.strip()


def clean_note(note):
    note = (note or '').strip()
    return '' if any(k.casefold() in note.casefold() for k in NOTE_REMARKS) else note


# ------------------------------------------------------------------------------------------------------------ name matching
# A name is matched in text as written (case-sensitive, whole words). Inside HTML a name may carry entities (&amp;, &#x27;)
# and a line break or &nbsp; where it has a space; the matched span is normalised back to the name to find its organisation.

_OPENERS = ('&quot;', '&#x27;', '&#39;', '&lsquo;', '&ldquo;', '&laquo;', '(', '[', '{', '"', "'", '‘', '“', '«')
_CLOSERS = ('&quot;', '&#x27;', '&#39;', '&rsquo;', '&rdquo;', '&raquo;',
            ')', ']', '}', '"', "'", '’', '”', '»', '.', ',', ';', ':', '!', '?')
_POSSESSIVE = ("'s", '’s', '&#x27;s', '&#39;s', '&rsquo;s')
_SPACE = r'(?:\s|&nbsp;)+'


def _norm(s):
    return ' '.join(html.unescape(s or '').replace('’', "'").replace(' ', ' ').split())


def _char_pat(ch):
    if ch == ' ':
        return _SPACE
    if ch == '&':
        return '(?:&amp;|&#38;|&)'
    if ch == "'":
        return "(?:'|’|&#x27;|&#39;|&rsquo;)"
    if ch == '"':
        return '(?:"|&quot;)'
    if ch == '<':
        return '(?:&lt;|<)'
    if ch == '>':
        return '(?:&gt;|>)'
    return re.escape(ch)


def _guard(name):
    """The lookahead that stops a name of this organisation where a Computation / Computing word follows it."""
    words = [w for w in GUARD_WORDS if w.casefold() not in (name or '').casefold()]
    return r'(?!%s(?:%s)\b)' % (_SPACE, '|'.join(words)) if words else ''


def _trie_regex(terms):
    """One regex for all terms ({term: end guard}); at any position the longest term that fits is tried first."""
    root = {'kids': {}, 'end': None}
    for t, guard in terms.items():
        node = root
        for ch in t:
            node = node['kids'].setdefault(_char_pat(ch), {'kids': {}, 'end': None})
        node['end'] = guard

    def emit(node):
        alts = [tok + emit(kid) for tok, kid in sorted(node['kids'].items())]
        if node['end'] is None:
            return alts[0] if len(alts) == 1 else '(?:' + '|'.join(alts) + ')'
        if not alts:
            return node['end']
        if node['end'] == '':
            return '(?:' + '|'.join(alts) + ')?'
        return '(?:' + '|'.join(alts) + '|' + node['end'] + ')'
    return re.compile(r'(?<!\w)(?:' + emit(root) + r')(?!\w)')


def _is_space_at(s, j):
    return j < len(s) and (s[j].isspace() or s.startswith('&nbsp;', j))


def _exact_token(s, a, b):
    """s[a:b] is a whole whitespace-delimited token, allowing opening brackets/quotes before it and a possessive 's, closing
    brackets/quotes and final punctuation after it."""
    i = a
    while i > 0 and not s[i - 1].isspace() and not s.endswith('&nbsp;', 0, i):
        i -= 1
    pre = s[i:a]
    while pre:
        for o in _OPENERS:
            if pre.endswith(o):
                pre = pre[:-len(o)]
                break
        else:
            return False
    j = b
    while j < len(s) and not _is_space_at(s, j):
        j += 1
    post = s[b:j]
    for p in _POSSESSIVE:
        if post.startswith(p):
            post = post[len(p):]
            break
    while post:
        for c in _CLOSERS:
            if post.startswith(c):
                post = post[len(c):]
                break
        else:
            return False
    return True


class Matcher:
    """Finds organisation names (and aliases) in text; every matched span belongs to one organisation."""

    def __init__(self, organisations, guard=True):
        cand = defaultdict(dict)
        for o in organisations:
            for t in [o['name']] + list(o.get('aliases') or []):
                k = _norm(t)
                if k:
                    cand[k][o['slug']] = o
        self.owner, self.conflicts, terms = {}, [], {}
        for k in sorted(cand):
            # a name shared by several organisations goes to the one it names exactly, then to the one with more machines
            ranked = sorted(cand[k].values(), key=lambda o: (_norm(o['name']) != k, -len(o.get('machines') or []), o['slug']))
            self.owner[k] = ranked[0]['slug']
            terms[k] = _guard(ranked[0]['name']) if guard else ''
            if len(ranked) > 1:
                self.conflicts.append((k, [o['slug'] for o in ranked]))
        self.rx = _trie_regex(terms) if terms else None

    def spans(self, s):
        """(start, end, slug) of every organisation name in s, left to right."""
        pos = 0
        while self.rx is not None and s:
            m = self.rx.search(s, pos)
            if m is None:
                return
            k = _norm(m.group(0))
            slug = self.owner.get(k)
            if slug is None or (len(k) < 4 and not _exact_token(s, m.start(), m.end())):
                pos = m.start() + 1
                continue
            yield m.start(), m.end(), slug
            pos = m.end()


# ---------------------------------------------------------------------------------------------------------------- register

def register_dir():
    return os.environ.get('QT_REGISTER_DIR') or _REG_LIVE


def _csv(path):
    with open(path, encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def _unit_forms(u):
    """A rolled-up unit as the register writes it ("IBM Canada (site)", "AQT (Planegg site) — site") → the forms to match."""
    u = _ws(u)
    if not u:
        return []
    forms = [u]
    base = u.split(' — ')[0].strip()
    forms.append(base)
    m = re.match(r'^(.*\S)\s*\([^()]*\)$', base)
    if m:
        forms.append(m.group(1).strip())
    return [f for f in dict.fromkeys(forms) if f]


class Register:
    FILE = 'quantum-organisation-register.csv'

    def __init__(self, d):
        self.dir = d
        self.rows = _csv(os.path.join(d, self.FILE))
        self.mtime = os.path.getmtime(os.path.join(d, self.FILE))
        self.by_name = {r['name']: r for r in self.rows}
        self.by_fold, self.by_unit = defaultdict(list), defaultdict(list)
        for r in self.rows:
            self.by_fold[_ws(r['name']).casefold()].append(r)
            for u in (r.get('rolled_up_units') or '').split(';'):
                for f in _unit_forms(u):
                    self.by_unit[f.casefold()].append(r)
        for f in _csv(os.path.join(d, 'corporate-families.csv')):
            parent = self.by_name.get(f.get('parent', ''))
            if parent is not None:
                for form in _unit_forms(f.get('rolled_up_unit', '')):
                    self.by_unit[form.casefold()].append(parent)
        self.bodies = {b['body_id']: b for b in _csv(os.path.join(d, 'data', 'academic-bodies.csv'))}
        self.mbo = {r['machine_id']: r for r in _csv(os.path.join(d, 'data', 'machines-by-organisation.csv'))}
        self.rel = defaultdict(list)
        for fn in ('org-machine-relations.csv', 'body-machine-relations.csv'):
            for r in _csv(os.path.join(d, 'data', fn)):
                self.rel[r['machine_id']].append((r['relation'], r['subject_id']))
        self.ambiguous = []

    def match_ci(self, s):
        """The register row whose name, else one of whose rolled-up units, equals s ignoring case."""
        k = _ws(s).casefold()
        for table in (self.by_fold, self.by_unit):
            names = sorted({r['name'] for r in table.get(k, [])})
            if names:
                if len(names) > 1:
                    self.ambiguous.append((s, names))
                return self.by_name[s if s in names else names[0]]
        return None

    def match_first_word(self, oid, org):
        """The only register row whose first word is oid (ignoring case) and whose name, less remarks, opens the org string."""
        k = oid.casefold()
        cands = []
        for r in self.rows:
            bare = strip_par(r['name'])
            words = bare.split()
            if words and words[0].casefold() == k and _opens_with(org, [bare]):
                cands.append(r)
        return cands[0] if len(cands) == 1 else None

    def target_name(self, t):
        return (self.bodies.get(t) or {}).get('name') or t


def canon(key):
    """A key after MERGE: the register row the actors name → the organisation that owns the machines."""
    return MERGE.get(key[1], key) if key and key[0] == 'reg' else key


def _resolve(m, R):
    """(organisation key or None, rule, why the org string had to be used) for a machine, by rules 1, 1*, 2 and 3; keys
    are ('reg', name), ('body', id) or ('unreg', org string)."""
    oid, org = _ws(m.get('org_id')), _ws(m.get('org'))
    if oid in R.by_name:
        return canon(('reg', oid)), '1', ''
    if oid.startswith('ab-'):
        if oid in R.bodies:
            return ('body', oid), '2', ''
        why = 'org_id %s is not in academic-bodies.csv' % oid
    elif oid in ('unmatched', ''):
        why = 'org_id "unmatched"'
    else:
        r = R.match_ci(oid) or R.match_first_word(oid, org)
        if r is not None:
            return canon(('reg', r['name'])), '1*', ''
        why = 'org_id %s names no register row' % oid
    r = R.match_ci(org)
    return (canon(('reg', r['name'])) if r is not None else None), '3', why


_SEP = re.compile(r'\s+with\s+|\s*\(|\s+/\s+')


def _opening_org(org, known):
    """Rule 3+: (key, host or None) when org opens with a known organisation followed by " with ", "(" or " / "."""
    m = _SEP.search(org)
    if not m:
        return None
    head, sep, rest = org[:m.start()].strip(), m.group(0).strip(), org[m.end():]
    if sep == 'with':
        k = known(head)
        return (k, first_party(rest) or None) if k else None
    if sep == '(':
        k = known(head)
        return (k, None) if k else None
    for part in [head] + re.split(r'\s+/\s+', rest):         # "A / B": co-builders, the first one the register knows
        k = known(strip_par(part))
        if k:
            return k, None
    return None


# ------------------------------------------------------------------------------------------------------------------- build

def build(reg_dir=None):
    """→ (snapshot, diagnostics). Deterministic: the same inputs give the same snapshot."""
    R = Register(reg_dir or register_dir())
    with open(MACHINES, encoding='utf-8') as fh:
        M = json.load(fh)
    with open(GRAPH, encoding='utf-8') as fh:
        G = json.load(fh)
    machines = M['machines']
    mby = {m['id']: m for m in machines}
    node_ix = {n['id']: i for i, n in enumerate(G['nodes'])}
    node_layer = {n['id']: n.get('layer', 99) for n in G['nodes']}
    path_ix = {p['id']: i for i, p in enumerate(G['paths'])}
    path_fam = {p['id']: p.get('family') for p in G['paths']}

    # machines: rules 1, 1*, 2, 3; then 3+ with the org strings of the resolved machines as known names
    rule_of, pending = {}, []
    for m in machines:
        key, rule, why = _resolve(m, R)
        if key is None:
            pending.append((m, why))
        else:
            rule_of[m['id']] = (rule, key, why)
    by_string = {_ws(mby[i].get('org')).casefold(): k for i, (_r, k, _w) in rule_of.items() if k[0] == 'reg'}

    def known(name):
        name = _ws(name)
        if not name:
            return None
        r = R.match_ci(name)
        if r is not None:
            return canon(('reg', r['name']))
        if name.casefold() in by_string:
            return by_string[name.casefold()]
        if ALIASES.get(name) in R.by_name:
            return canon(('reg', ALIASES[name]))
        return None
    prefix_host = {}
    for m, why in pending:
        org = _ws(m.get('org'))
        hit = _opening_org(org, known)
        if hit:
            rule_of[m['id']] = ('3+', hit[0], why)
            if hit[1]:
                prefix_host[m['id']] = hit[1]
        else:
            rule_of[m['id']] = ('-', ('unreg', org), why)

    orgs, order = {}, []

    def org_for(key):
        if key not in orgs:
            orgs[key] = {'machines': [], 'aliases': set(), 'added': {}, 'arch': set()}
            order.append(key)
        return orgs[key]
    for m in machines:
        o = org_for(rule_of[m['id']][1])
        o['machines'].append(m['id'])
        if _ws(m.get('org')):
            o['aliases'].add(_ws(m.get('org')))
        if m.get('map_path'):
            o['arch'].add(m['map_path'])

    def name_of(key):
        kind, v = key
        if key in DISPLAY_NAME:
            return DISPLAY_NAME[key]
        return v if kind != 'body' else _ws(R.bodies[v].get('name')) or v

    actors = []
    for p in G['paths']:
        for tok in split_actors(p.get('actors')):
            if tok in R.by_name:
                key, via = canon(('reg', tok)), 'register'
            elif ALIASES.get(tok) in R.by_name:
                key, via = canon(('reg', ALIASES[tok])), 'alias'
            else:
                actors.append((p['id'], tok, None, ''))
                continue
            if key not in orgs:           # an organisation already built under another key with this very name takes it
                same = [k for k in order if name_of(k).casefold() == name_of(key).casefold()]
                key = same[0] if same else key
            org_for(key)['arch'].add(p['id'])
            actors.append((p['id'], tok, key, 'merge' if key != ('reg', tok) and via == 'register' else via))

    # aliases beyond the org strings: merged rows, short names, the register name behind a display name
    for src, key in MERGE.items():
        if key in orgs:
            orgs[key]['added'].setdefault(src, 'merge')
    for key, shown in DISPLAY_NAME.items():
        if key in orgs:
            orgs[key]['added'].setdefault(shown, 'display name')
            orgs[key]['added'].setdefault(key[1], 'register name')
    unused = []
    for short, target in ALIASES.items():
        key = canon(('reg', target))
        if key in orgs:
            orgs[key]['added'].setdefault(short, 'short name')
        else:
            unused.append((short, target))
    for o in orgs.values():
        o['aliases'] |= set(o['added'])

    # records
    recs = []
    for key in order:
        kind, v = key
        o = orgs[key]
        if kind == 'reg':
            r = R.by_name[v]
            d = {'name': name_of(key), 'tier': r.get('tier', ''), 'segment': r.get('segment', ''), 'country': r.get('country', ''),
                 'city': r.get('city', ''), 'url': r.get('url', ''), 'note': r.get('note', '')}
        elif kind == 'body':
            b = R.bodies[v]
            d = {'name': name_of(key), 'tier': 'academic', 'segment': '', 'country': b.get('country', ''),
                 'city': b.get('city', ''), 'url': b.get('website', b.get('url', '')), 'note': ''}
        else:
            d = {'name': v, 'tier': 'unregistered', 'segment': '', 'country': '', 'city': '', 'url': '', 'note': ''}
        raw_note = (d['note'] or '').strip()
        d = {k: _ws(x) if k != 'note' else clean_note(x) for k, x in d.items()}
        ms = sorted(o['machines'], key=lambda i: (STAT_ORDER.index(status_class(mby[i].get('status'))),
                                                   _ws(mby[i].get('name')).casefold(), i))
        fams = {mby[i].get('family') for i in ms} | {path_fam.get(p) for p in o['arch']}
        fams.discard(None)
        fams.discard('')
        held = Counter()
        for i in ms:
            held.update({c['node'] for cells in mby[i].get('layers', {}).values() for c in cells
                         if c.get('state') == 'station' and c.get('node') in node_ix})
        technologies = sorted(held.items(), key=lambda kv: (-kv[1], node_layer[kv[0]], node_ix[kv[0]]))[:TOP_STATIONS]
        aliases = sorted(o['aliases'], key=lambda s: (s.casefold(), s))
        own = own_names(d['name'], aliases)
        own_parties = {parties(n) for n in [d['name']] + aliases}
        own_ids = {v} if kind == 'body' else set()
        hosts = []
        for i in ms:
            row = R.mbo.get(i)
            if row is None:
                if i in prefix_host:
                    hosts.append({'machine': i, 'host_org': prefix_host[i]})
                continue
            host = _ws(row.get('host_org'))
            elsewhere = [t for rel, t in R.rel.get(i, []) if rel in HOST_RELATIONS
                         and t not in own_ids and not _opens_with(R.target_name(t), own)]
            same = _opens_with(host, own) or parties(host) in own_parties
            if host and (not same or elsewhere):
                hosts.append({'machine': i, 'host_org': host})
        recs.append(dict(key=key, **d, aliases=aliases, machines=ms, raw_note=raw_note, added=o['added'],
                         families=sorted(fams, key=lambda f: (FAM_ORDER.index(f) if f in FAM_ORDER else len(FAM_ORDER), f)),
                         architectures=sorted(o['arch'], key=lambda p: (path_ix.get(p, len(path_ix)), p)),
                         stations=[{'id': n, 'machines': c} for n, c in stations], hosts=hosts))

    # slugs: unique, in order of (slug, name, key)
    taken, collisions = set(), []
    for rec in sorted(recs, key=lambda r: (slugify(r['name']), r['name'], r['key'])):
        base = slug = slugify(rec['name'])
        n = 2
        while slug in taken:
            slug = '%s-%d' % (base, n)
            n += 1
        if slug != base:
            collisions.append((slug, rec['name']))
        taken.add(slug)
        rec['slug'] = slug

    # brief mentions (and the phrases the Computation / Computing guard keeps out)
    mt, bare = Matcher(recs), Matcher(recs, guard=False)
    per, guarded = defaultdict(Counter), defaultdict(lambda: [0, set()])
    for fn in sorted(f for f in os.listdir(BRIEFS) if f.endswith('.md')):
        with open(os.path.join(BRIEFS, fn), encoding='utf-8') as fh:
            text = fh.read()
        kept, starts = set(), set()
        for a, b, slug in mt.spans(text):
            per[slug][fn[:-3]] += 1
            kept.add((a, b, slug))
            starts.add((a, slug))
        for a, b, slug in bare.spans(text):
            if (a, b, slug) not in kept:
                nxt = re.match(r'\s*(\S+)', text[b:])
                phrase = _ws(text[a:b]) + (' ' + nxt.group(1).strip('.,;:)"”’\'') if nxt else '')
                g = guarded[(phrase, slug, 'shortened' if (a, slug) in starts else 'removed')]
                g[0] += 1
                g[1].add(fn[:-3])
    for rec in recs:
        c = per.get(rec['slug'], Counter())
        rec['mentions'] = {'briefs': sorted(c, key=lambda b: (-c[b], node_layer.get(b, 99), node_ix.get(b, 10 ** 6), b)),
                           'count': sum(c.values())}
    # co-developers: every organisation the register names in a machine's org string beside the builder the machine is filed
    # under ("Harvard / MIT / QuEra", "RIKEN with AIST, NICT, …") — the machine is listed on their pages too (27 Sep 2026)
    slug_of_machine = {i: rec['slug'] for rec in recs for i in rec['machines']}
    by_term = {}
    for rec in recs:
        for t_ in [rec['name']] + list(rec['aliases']):
            by_term.setdefault(t_.casefold(), rec['slug'])
    def co_slug(tok):
        k = tok.casefold()
        if k in by_term: return by_term[k]
        hits = {rec['slug'] for rec in recs if rec['name'].casefold().startswith(k + ',') or rec['name'].casefold().startswith(k + ' (')}
        return hits.pop() if len(hits) == 1 else None
    co = defaultdict(list)
    for m in machines:
        org = _ws(m.get('org')).replace('(', ',').replace(')', ',')
        for tok in re.split(r',|;|/| with | and |\+', org):
            tok = tok.strip(' .')
            slug = co_slug(tok) if tok else None
            if slug and slug != slug_of_machine.get(m['id']) and m['id'] not in co[slug]:
                co[slug].append(m['id'])
    for rec in recs:
        rec['co_machines'] = sorted(co.get(rec['slug'], []), key=lambda i: (STAT_ORDER.index(status_class(mby[i].get('status'))),
                                                                          _ws(mby[i].get('name')).casefold(), i))

    fields = ('slug', 'name', 'aliases', 'tier', 'segment', 'country', 'city', 'url', 'note', 'machines', 'co_machines', 'families',
              'architectures', 'stations', 'hosts', 'mentions')
    out = [{k: rec[k] for k in fields} for rec in sorted(recs, key=lambda r: r['slug'])]
    imported = datetime.datetime.fromtimestamp(R.mtime, datetime.timezone.utc).strftime('%Y-%m-%d')
    snap = {'source': {'register': REGISTER_LABEL, 'imported': imported, 'organisations': len(out)}, 'organisations': out}
    diag = {'rule_of': rule_of, 'slug_of': {rec['key']: rec['slug'] for rec in recs}, 'actors': actors,
            'collisions': collisions, 'conflicts': mt.conflicts, 'ambiguous': list(R.ambiguous), 'recs': recs,
            'machines': mby, 'register': R, 'guarded': guarded, 'unused_aliases': unused, 'prefix_host': prefix_host}
    return snap, diag


def dumps(snap):
    return json.dumps(snap, ensure_ascii=False, indent=1) + '\n'


def write(snap):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(dumps(snap))


# ---------------------------------------------------------------------------------------------------------------------- API

_CACHE = {}


def load():
    """The snapshot data/orgs/organisations.json (read once per process; treat it as read-only)."""
    if 'snap' not in _CACHE:
        with open(OUT, encoding='utf-8') as fh:
            _CACHE['snap'] = json.load(fh)
    return _CACHE['snap']


def by_slug():
    if 'by_slug' not in _CACHE:
        _CACHE['by_slug'] = {o['slug']: o for o in load()['organisations']}
    return _CACHE['by_slug']


def slug_for_machine(machine):
    """The slug of the organisation that builds the machine (a machines.json record or its id), or None."""
    if 'by_machine' not in _CACHE:
        _CACHE['by_machine'] = {i: o['slug'] for o in load()['organisations'] for i in o['machines']}
    mid = machine.get('id') if isinstance(machine, dict) else machine
    return _CACHE['by_machine'].get(mid)


def _matcher():
    if 'matcher' not in _CACHE:
        _CACHE['matcher'] = Matcher(load()['organisations'])
    return _CACHE['matcher']


_TAG = re.compile(r'<!--.*?-->|<![^>]*>|<\?[^>]*>|</?([A-Za-z][A-Za-z0-9:-]*)(?:[^>"\']|"[^"]*"|\'[^\']*\')*>', re.S)
_CLASS = re.compile(r'''\sclass\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+))''', re.I)
_RAWTEXT = ('script', 'style', 'textarea', 'title')                     # element bodies copied verbatim
_NOLINK_TAGS = {'a', 'svg', 'code', 'h1', 'h2', 'h3', 'h4'}             # nothing is linked inside these
_NOLINK_CLASSES = {'btitle', 'meta'}                                    # nor inside an element of these classes
_VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
_CLOSES_P = {'address', 'article', 'aside', 'blockquote', 'details', 'div', 'dl', 'fieldset', 'figcaption', 'figure', 'footer',
             'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'main', 'nav', 'ol', 'p', 'pre', 'section', 'table', 'ul'}


def link_orgs(text, lang='en', base=''):
    """text with the first occurrence of every known organisation (its name or an alias) wrapped in
    <a class="org" href="{base}organisation/{slug}.html">…</a>; longest names first; text nodes only - never inside a tag,
    an existing <a>…</a>, <code>, <h1>-<h4>, an element of class "btitle" or "meta", <svg>, <script>, <style>, <textarea>
    or <title>. lang is accepted for symmetry with the other helpers: organisation names are written the same way in both
    languages."""
    mt = _matcher()
    if not text or mt.rx is None:
        return text
    out, linked = [], set()
    stack = []          # [tag, depth] of the open elements inside which nothing is linked

    def link(seg):
        parts, i = [], 0
        for a, b, slug in mt.spans(seg):
            if slug in linked:
                continue
            linked.add(slug)
            parts.append(seg[i:a])
            parts.append('<a class="org" href="%sorganisation/%s.html">%s</a>' % (base, slug, seg[a:b]))
            i = b
        parts.append(seg[i:])
        return ''.join(parts)
    i = 0
    while True:
        m = _TAG.search(text, i)
        j = m.start() if m else len(text)
        if j > i:
            out.append(text[i:j] if stack else link(text[i:j]))
        if m is None:
            break
        tag, name = m.group(0), (m.group(1) or '').lower()
        out.append(tag)
        i = m.end()
        if not name:
            continue
        if tag.startswith('</'):
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0] == name:
                    stack[k][1] -= 1
                    if stack[k][1] == 0:
                        del stack[k:]
                    break
            continue
        if name in _RAWTEXT:
            c = re.compile(r'</%s\s*>' % name, re.I).search(text, i)
            k = c.end() if c else len(text)
            out.append(text[i:k])
            i = k
            continue
        if name in _VOID or tag[:-1].rstrip().endswith('/'):
            continue
        if stack and stack[-1][0] == 'p' and name in _CLOSES_P:
            stack.pop()                                     # a block element closes an open <p>
        same = [e for e in stack if e[0] == name]
        if same:
            same[-1][1] += 1                                # a nested element of the same kind inside a no-link element
            continue
        cm = _CLASS.search(tag)
        classes = set((next(g for g in cm.groups() if g is not None) if cm else '').split())
        if name in _NOLINK_TAGS or classes & _NOLINK_CLASSES:
            stack.append([name, 1])
    return ''.join(out)


def _fmt_q(q):
    if q is None or q == '':
        return ''
    try:
        f = float(q)
    except (TypeError, ValueError):
        return html.escape(str(q))
    return '{:,}'.format(int(f)) if f.is_integer() else '%g' % f


def profile_html(o, lang, base, machines_by_id, node_by_id, path_by_id):
    """An organisation's card, its headings in the page's language (English where the language has none, 29 Sep 2026); base: from the
    page to its language's root, so the links stay in that language; empty sections are left out."""
    from langs import pick
    L = lang
    h_m, h_t, h_a, h_b = pick(L, HEAD)
    e = html.escape
    b = e(base or '')

    def node_name(i):
        return e(pick(L, node_by_id.get(i) or {}) or i)
    meta = [e(x) for x in (o.get('tier'), o.get('segment')) if x]
    place = ', '.join(x for x in (o.get('city'), o.get('country')) if x)
    if place:
        meta.append(e(place))
    url = (o.get('url') or '').strip()
    if url:
        href = url if re.match(r'(?i)https?://', url) else 'https://' + url
        meta.append('<a href="%s">%s</a>' % (e(href), e(url)))
    out = ['<section class="orgcard"><h2>%s</h2>' % e(o['name'])]
    if meta:
        out.append('<p class="meta">%s</p>' % ' · '.join(meta))
    if o.get('note'):
        out.append('<p>%s</p>' % e(o['note']))
    ms = [machines_by_id[i] for i in o.get('machines') or [] if i in machines_by_id]
    if ms:
        lis = []
        for m in ms:
            bits = [e(m['status'])] if m.get('status') else []
            if _fmt_q(m.get('physical_qubits_num')):
                bits.append('%s q' % _fmt_q(m.get('physical_qubits_num')))
            if m.get('status_date'):
                bits.append(e(m['status_date']))
            lis.append('<li><a href="%smachine/%s.html">%s</a>%s</li>'
                       % (b, e(m['id']), e(m.get('name') or m['id']), (' — ' + ', '.join(bits)) if bits else ''))
        out.append('<h3>%s (%d)</h3><ul>%s</ul>' % (h_m, len(ms), ''.join(lis)))
    cms = [machines_by_id[i] for i in o.get('co_machines') or [] if i in machines_by_id]
    if cms:
        out.append('<h3>%s (%d)</h3><ul>%s</ul>' % (pick(L, HEAD_CO), len(cms), ''.join(
            '<li><a href="%smachine/%s.html">%s</a> — %s</li>' % (b, e(m['id']), e(m.get('name') or m['id']), e(m.get('org') or ''))
            for m in cms)))
    if o.get('stations'):
        out.append('<h3>%s</h3><ul>%s</ul>' % (h_t, ''.join(
            '<li><a href="%stechnology/%s.html">%s</a> · %d</li>' % (b, e(s['id']), node_name(s['id']), s['machines'])
            for s in o['stations'])))
    if o.get('architectures'):
        def short(p):
            pr = path_by_id.get(p) or {}
            return e(pick(L, pr) or pick(L, pr.get('short') or {}) or p)   # the full name (one name per architecture, 27 Sep 2026)
        out.append('<h3>%s</h3><ul>%s</ul>' % (h_a, ''.join(
            '<li><a href="%sarchitecture/%s.html">%s</a></li>' % (b, e(p), short(p)) for p in o['architectures'])))
    briefs = (o.get('mentions') or {}).get('briefs') or []
    if briefs:
        out.append('<h3>%s</h3><ul>%s</ul>' % (h_b, ''.join(
            '<li><a href="%stechnology/%s.html">%s</a></li>' % (b, e(i), node_name(i)) for i in briefs)))
    out.append('</section>')
    return '\n'.join(out)


# ---------------------------------------------------------------------------------------------------------------------- CLI

def _check(snap_file, built):
    orgs = snap_file['organisations'] if snap_file else []
    src = (snap_file or {}).get('source', {})
    print('snapshot %s: %d organisations, register imported %s'
          % (os.path.relpath(OUT, ROOT), len(orgs), src.get('imported', '—')) if snap_file else 'snapshot: missing')
    if built is None:
        print('register not found (%s): per-rule counts need it; counts below are from the snapshot' % register_dir())
        tiers = Counter(o['tier'] for o in orgs)
        print('organisations by tier: ' + ' · '.join('%s %d' % kv for kv in sorted(tiers.items(), key=lambda kv: (-kv[1], kv[0]))))
        print('machines: %d' % sum(len(o['machines']) for o in orgs))
        print('unregistered: ' + ('; '.join('"%s"' % o['name'] for o in orgs if o['tier'] == 'unregistered') or 'none'))
        return
    snap, diag = built
    print('snapshot current: %s' % ('yes' if snap_file and dumps(snap_file) == dumps(snap) else 'NO - run --import'))
    orgs = snap['organisations']
    names = {o['slug']: o['name'] for o in orgs}
    slug_of, mby = diag['slug_of'], diag['machines']
    tiers = Counter(o['tier'] for o in orgs)
    print('organisations: %d' % len(orgs))
    print('  by tier: ' + ' · '.join('%s %d' % kv for kv in sorted(tiers.items(), key=lambda kv: (-kv[1], kv[0]))))
    nm = sum(1 for o in orgs if o['machines'])
    print('  with machines: %d · from path actors only: %d' % (nm, len(orgs) - nm))
    rules = Counter(r for r, _k, _w in diag['rule_of'].values())
    print('machines: %d' % len(diag['rule_of']))
    for r, desc in RULES:
        print('  rule %-3s %4d  %s' % (r, rules.get(r, 0), desc))
    groups = defaultdict(list)
    for mid, (r, key, why) in sorted(diag['rule_of'].items()):
        groups[(r, key, why)].append(mid)
    print('org_id not a register name, resolved by case / first word (rule 1*):')
    for (r, key, _w), mids in sorted(groups.items(), key=lambda kv: kv[0][1]):
        if r == '1*':
            print('  %s → "%s" (%s)' % (', '.join(sorted({mby[i]['org_id'] for i in mids})), key[1], ', '.join(mids)))
    print('org strings resolved from the string itself (rules 3, 3+, -):')
    for (r, key, why), mids in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][2], ', '.join(kv[1]))):
        if r in ('3', '3+', '-'):
            for s in sorted({_ws(mby[i]['org']) for i in mids}):
                hosts = ['%s: host "%s"' % (i, diag['prefix_host'][i]) for i in mids if i in diag['prefix_host']]
                print('  [%s] "%s" → %s (%s; %s)%s' % (r, s, '"%s"' % names[slug_of[key]] if r != '-' else 'unregistered',
                                                       why, ', '.join(mids), ('; ' + '; '.join(hosts)) if hosts else ''))
    unreg = [o['name'] for o in orgs if o['tier'] == 'unregistered']
    print('org strings that resolved to no register row: %s' % ('; '.join('"%s"' % n for n in unreg) if unreg else 'none'))
    for (r, key, _w), mids in sorted(groups.items(), key=lambda kv: kv[0][1]):
        if r == '2':
            print('  academic body, not a register row: %s → "%s" (%s; %s)'
                  % (' | '.join('"%s"' % s for s in sorted({_ws(mby[i]['org']) for i in mids})), names[slug_of[key]], key[1], ', '.join(mids)))
    matched = [a for a in diag['actors'] if a[2] is not None]
    print('path actors: %d names, %d matched (%d register name, %d short name, %d merged), %d not'
          % (len(diag['actors']), len(matched), sum(a[3] == 'register' for a in matched), sum(a[3] == 'alias' for a in matched),
             sum(a[3] == 'merge' for a in matched), len(diag['actors']) - len(matched)))
    for pid in dict.fromkeys(a[0] for a in diag['actors']):
        ok = [a[1] if a[3] == 'register' else '%s→%s' % (a[1], names[slug_of[a[2]]]) for a in diag['actors'] if a[0] == pid and a[2]]
        no = [a[1] for a in diag['actors'] if a[0] == pid and a[2] is None]
        print('  %-11s %s%s' % (pid, ', '.join(ok) or '—', ('  · unmatched: ' + ', '.join(no)) if no else ''))
    print('aliases added (beyond the org strings of the machines):')
    for rec in sorted(diag['recs'], key=lambda r: r['slug']):
        if rec['added']:
            print('  %s: %s' % (rec['name'], ', '.join('%s [%s]' % (a, how) for a, how in sorted(rec['added'].items(), key=lambda kv: kv[0].casefold()))))
    if diag['unused_aliases']:
        print('  unused (organisation not in the Atlas): ' + ', '.join('%s → %s' % u for u in diag['unused_aliases']))
    only = [o for o in orgs if not o['machines']]
    if only:
        print('organisations from path actors only (no machine): ' + ', '.join('%s [%s]' % (o['name'], o['tier']) for o in only))
        for o in only:
            mine = {n.casefold() for n in [o['name']] + o['aliases']}
            named = ['%s (%s)' % (i, names[slug_of[diag['rule_of'][i][1]]]) for i in sorted(mby)
                     if {p.casefold() for p in re.split(r'\s+(?:with|and|\+|/)\s+|,\s*', strip_par(mby[i].get('org')))} & mine]
            if named:
                print('  "%s" is named in the org string of %s' % (o['name'], ', '.join(named)))
    if diag['collisions']:
        print('slug collisions: ' + '; '.join('%s ← "%s"' % c for c in diag['collisions']))
    if diag['conflicts']:
        print('names shared by several organisations: ' + '; '.join('"%s" → %s' % (k, ' > '.join(v)) for k, v in diag['conflicts']))
    amb = dict.fromkeys((s, tuple(n)) for s, n in diag['ambiguous'])
    if amb:
        print('case-insensitive matches with several register rows (first taken): '
              + '; '.join('"%s" → %s' % (s, ', '.join(n)) for s, n in amb))
    ment = [o for o in orgs if o['mentions']['count']]
    print('brief mentions: %d of %d organisations named in at least one English brief (%d mentions in all)'
          % (len(ment), len(orgs), sum(o['mentions']['count'] for o in orgs)))
    g = diag['guarded']
    print('Computation / Computing guard: %s' % ('; '.join(
        '%s "%s" ×%d, not %s (%s)' % (how, p, v[0], names[s], ', '.join(sorted(v[1])))
        for (p, s, how), v in sorted(g.items())) if g else 'removed nothing'))
    print('hosts: %d machines hosted by another organisation, across %d organisations'
          % (sum(len(o['hosts']) for o in orgs), sum(1 for o in orgs if o['hosts'])))
    dropped = [r['slug'] for r in diag['recs'] if r['raw_note'] and not r['note']]
    kept = [r['slug'] for r in diag['recs'] if r['note']]
    print('register notes: %d dropped as curation remarks (%s); %d kept (%s)'
          % (len(dropped), ', '.join(sorted(dropped)) or '—', len(kept), ', '.join(sorted(kept)) or '—'))


def main(argv):
    if '--import' in argv:
        if not os.path.isdir(register_dir()):
            print('orgs: register not found at %s (set QT_REGISTER_DIR)' % register_dir(), file=sys.stderr)
            return 1
        snap, _diag = build()
        write(snap)
        print('wrote %s: %d organisations (register imported %s)'
              % (os.path.relpath(OUT, ROOT), snap['source']['organisations'], snap['source']['imported']))
        return 0
    if '--check' in argv:
        snap_file = None
        if os.path.exists(OUT):
            with open(OUT, encoding='utf-8') as fh:
                snap_file = json.load(fh)
        built = build() if os.path.isdir(register_dir()) else None
        _check(snap_file, built)
        return 0
    print(__doc__.split('\n\n')[1])
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
