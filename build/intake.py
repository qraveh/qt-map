#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Atlas's side of the digest's intake: triage, verification worklist, application plan, decisions ledger.

The digest (qnews, the local pipeline) writes proposals into QT-Map/qnews-intake/ (its CHARTER; contract rev 3 of 5 Oct 2026):
papers relate to technologies (records, gaps, station amendments, works) and the industry stream proposes changes to the
register (one field of one machine, a new machine, an organisation event) with the owner's own words. qnews never edits the
Atlas. This tool is how the Atlas takes them: every proposal gets exactly one decision, recorded in data/intake/decisions.json
by its row_key, so nothing is read twice and nothing is lost.

    python3 build/intake.py status  --intake DIR                 counts: undecided rows by file and by tier
    python3 build/intake.py triage  --intake DIR --out DIR       triage.json (every undecided row, its tier and reason),
                                                                 verify.json (the source checks the session must make),
                                                                 packet.md (the editor's part, review-ready)
    python3 build/intake.py plan    --triage T --verified V --out DIR [--date D]
                                                                 draft register patch (build/register_patch.py format),
                                                                 draft change-ledger items, and the decisions to record
    python3 build/intake.py record  --plan P                     merge the plan's decisions into data/intake/decisions.json
    python3 build/intake.py decide  ROW_KEY DECISION --reason TEXT [--by editor]
    python3 build/intake.py check   [--intake DIR]               the ledger's shape; with DIR, every row_key exists there

TIERS — the rule table TIER_RULES below is the whole policy, printed by `status --rules`:
  auto     the session verifies the quote at the source, then applies: register fields that do not move a conclusion
           (qubit counts within 25 %, T1/T2 that are T1/T2, gate and readout times, readout error, access within its
           class, a retirement, a status_date within its year), organisation events (as change-ledger statements)
  hold     waits for a named work package, no decision needed now: two-qubit error figures wait for WP2's
           comparability classes (review R1-1)
  session  a written change a session makes in a weekly batch: the deep reviews' notes into the briefs (three languages),
           technology records (does the paper's device fit the technology; does the number beat the standing record)
  editor   the editor decides: a status that moves a machine into or out of the device counts of §8, any future-dated
           status (the Tempo case), a new machine, a new technology, a technology's status or descriptor
  attach   a work proposed for the references: numbered only when a change that cites it is applied
  reject   no decision needed beyond the reason: press alone, an unknown id, the reviewer's own inference
  landed   the Atlas already says it (the register value equals the proposal)
  stale    the register moved since the proposal was measured (`current` differs from the register now): re-read

DECISIONS (data/intake/decisions.json, keyed by the intake's row_key):
  applied   the change is in the Atlas data; `change` names the change-ledger item, `commit` the commit when known
  rejected  will not be applied; `reason` says why (qnews is asked not to re-propose the same machine, field and value)
  deferred  kept for a named later step (`until`: WP2, edition, a weekly brief pass, the editor's word)
  landed    found already true in the Atlas at triage
  approved  the editor said yes; not final — the next run applies it like an auto row (a new machine or a technology is
            written by the session by hand: plan.json `manual`) and records `applied`
Nothing here edits the intake (qnews owns it) or the register (register_patch.py does, on a reviewed plan)."""
import argparse, csv, datetime as dt, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
LEDGER = os.path.join(ROOT, 'data', 'intake', 'decisions.json')
REGISTER = os.path.join(ROOT, 'data', 'register', 'machines.csv')
GRAPH = os.path.join(ROOT, 'data', 'graph.json')
ORGS = os.path.join(ROOT, 'data', 'orgs', 'organisations.json')
WORKS = os.path.join(ROOT, 'data', 'work-numbers.json')
SITE = 'https://qodeh.com/publications/quantum-technology-atlas/'

FILES = ('register-amendment-candidates.csv', 'machine-candidates.csv', 'org-event-candidates.csv',
         'amendment-candidates.csv', 'map-gaps-candidates.csv', 'records-candidates.csv', 'works-candidates.csv')
DECISIONS = ('applied', 'rejected', 'deferred', 'landed', 'approved')
FINAL = ('applied', 'rejected', 'deferred', 'landed')
DEVICE = ('DEPLOYED', 'DEMONSTRATED', 'RETIRED')
STATUS_ORDER = ('PLANNED', 'ANNOUNCED', 'DEMONSTRATED', 'DEPLOYED', 'RETIRED')
AUTO_FIELDS = ('physical_qubits_num', 'qubits_accessible', 't1', 't2', 't_2q', 't_meas', 'readout_error', 'access',
               'status_date', 'codes', 'best_logical', 'demonstrated_algorithms', 'benchmark')
COUNT_JUMP = 0.25      # a qubit count that moves by more than this fraction is the editor's: the register's count may be
                       # defined differently from the owner's (IBM Nighthawk r2: 120 qubits, «458 physical» counts couplers)
COHERENCE_WORDS = re.compile(r'\bT[12]\*?\b|T_?[12]|coherence|relaxation|dephasing|energy decay', re.I)
HOLD_FIELDS = ('err_2q_median_num', 'err_2q_best', 'err_2q_median')
NUMERIC = ('physical_qubits_num', 'qubits_accessible', 'err_2q_median_num')
TEXT_TWIN = {'physical_qubits_num': 'physical_qubits', 'err_2q_median_num': 'err_2q_median'}   # the register's prose column

# the policy, one line per rule, in the order applied; printed by `status --rules` and quoted in the packet
TIER_RULES = [
    ('any', 'decided already in data/intake/decisions.json', 'skip'),
    ('register-amendment', 'machine id not in the register', 'reject'),
    ('register-amendment', 'source class D (press alone)', 'reject'),
    ('register-amendment', 'the register already holds the proposed value', 'landed'),
    ('register-amendment', 'the register value differs from `current` (the register moved since)', 'stale'),
    ('register-amendment', 'field status, event roadmap (stated for the future: the Tempo case)', 'editor'),
    ('register-amendment', 'field status, the change crosses the device boundary of §8 (DEPLOYED/DEMONSTRATED/RETIRED)', 'editor'),
    ('register-amendment', 'field status within the device or non-device set (e.g. DEPLOYED → RETIRED)', 'auto'),
    ('register-amendment', 'two-qubit error fields', 'hold (WP2)'),
    ('register-amendment', 'status_date whose year differs (it is the cohort date; a retirement date goes in the status text)', 'reject'),
    ('register-amendment', 'T1/T2 whose quote names another quantity (a bit-flip time)', 'hold (WP1)'),
    ('register-amendment', 'the register\'s prose beside the number already names the proposed value (a curated choice)', 'reject'),
    ('register-amendment', 'a qubit count that moves by more than 25 %', 'editor'),
    ('register-amendment', 'roadmap (merged, not replaced: the forecast ledger)', 'editor'),
    ('register-amendment', 'access that changes the cloud / on-premises / laboratory class', 'editor'),
    ('register-amendment', 'counts, times, readout error, access, status date, milestones', 'auto'),
    ('register-amendment', 'any other field', 'editor'),
    ('machine-candidate', 'a system the register does not hold', 'editor'),
    ('org-event', 'source class D', 'reject'),
    ('org-event', 'funding, acquisition, merger, listing, rename, closure, policy', 'auto (ledger statement)'),
    ('station amendment', 'the evidence is the reviewer\'s own inference', 'reject'),
    ('station amendment', 'change_kind status (an empty slot demonstrated) or descriptor', 'editor'),
    ('station amendment', 'change_kind note', 'session (weekly brief pass)'),
    ('map gap', 'a technology the Atlas lacks', 'editor'),
    ('record', 'station unknown', 'reject'),
    ('record', 'a dated record with its quote (does the device fit the technology? better than the standing record?)',
     'session (weekly pass)'),
    ('work', 'cited by an applied change of the same paper', 'attach'),
]


# ---------------------------------------------------------------- io
def read_csv(path):
    if not os.path.exists(path):
        return []
    with io.open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def load_ledger(path=LEDGER):
    if not os.path.exists(path):
        return {'note': NOTE, 'decisions': {}}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def save_ledger(led, path=LEDGER):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    led['note'] = NOTE
    led['decisions'] = dict(sorted(led['decisions'].items()))
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(led, f, ensure_ascii=False, indent=1)
        f.write('\n')


NOTE = ("One decision per proposal of the digest's intake (QT-Map/qnews-intake, contract rev 3), keyed by the intake's row_key. "
        "decision: applied (in the Atlas data; `change` = the change-ledger item, `commit` when known) | rejected (`reason`) | "
        "deferred (`until` names the later step) | landed (already true at triage). `file` = the intake file, `date` = the "
        "decision's date, `by` = editor | intake-run | session, `verified` = the source check (url, quote_found, checked). "
        "`runs`: one line per intake run (its date, the intake manifest's `updated` it read, the ticket that carried it, the count "
        "of decisions by kind). Written only by build/intake.py; read by qnews to close its rows. Policy: build/intake.py TIER_RULES.")


def norm(v):
    return re.sub(r'\s+', ' ', (v or '').strip()).lower()


def same_value(field, a, b):
    a, b = (a or '').strip(), (b or '').strip()
    if field in NUMERIC or field in ('t1', 't2', 't_2q', 't_meas', 'readout_error', 'err_2q_best'):
        try:
            x, y = float(a.replace(',', '')), float(b.replace(',', ''))
            return abs(x - y) <= 1e-9 + 0.005 * abs(y)
        except ValueError:
            pass
    if field == 'status':
        return status_word(a) == status_word(b)
    return norm(a) == norm(b)


def status_word(s):
    u = (s or '').upper().strip()
    for k in ('RETIRED', 'DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED'):
        if u.startswith(k):
            return k
    return 'OTHER'


def access_class(s):
    u = (s or '').lower()
    return ('cloud' in u and 'was cloud' not in u, 'on-prem' in u or 'sold' in u, 'lab' in u or 'research' in u)


def atlas_link(kind, ident):
    return SITE + {'machine': 'machine/%s.html', 'organisation': 'organisation/%s.html',
                   'technology': 'technology/%s.html'}[kind] % ident


# ---------------------------------------------------------------- context
class Atlas:
    def __init__(self, root=ROOT):
        self.machines = {m['machine_id']: m for m in read_csv(os.path.join(root, 'data', 'register', 'machines.csv'))}
        g = json.load(open(os.path.join(root, 'data', 'graph.json'), encoding='utf-8'))
        self.nodes = {n['id']: n for n in g['nodes']}
        o = json.load(open(os.path.join(root, 'data', 'orgs', 'organisations.json'), encoding='utf-8'))
        self.orgs = {x['slug']: x for x in o['organisations']}
        self.org_alias = {}
        for x in o['organisations']:
            for a in [x['slug'], x['name']] + list(x.get('aliases') or []):
                self.org_alias[norm(a)] = x['slug']
        self.devices = sum(1 for m in self.machines.values() if self.is_device(m))

    @staticmethod
    def is_device(m, status=None):
        """§8's definition (build/machines_chapter.py): a device is DEPLOYED, DEMONSTRATED or RETIRED and carries neither
        flag target-not-device nor component-only."""
        flags = set((m.get('flags') or '').split(';'))
        return status_word(status if status is not None else m.get('status')) in DEVICE and \
            not (flags & {'target-not-device', 'component-only'})


# ---------------------------------------------------------------- triage
def tier_register(r, A):
    m = A.machines.get(r.get('machine_id'))
    f, cur, new = r.get('field', ''), r.get('current', ''), r.get('proposed_value', '')
    if not m:
        return 'reject', 'machine id not in the register'
    if (r.get('source_class') or '').upper() == 'D':
        return 'reject', 'press alone is a lead, never a register change'
    now = m.get(f, m.get(TEXT_TWIN.get(f, ''), ''))
    if f in m and same_value(f, now, new):
        return 'landed', 'the register already says %s' % new
    if f in m and cur and not same_value(f, now, cur):
        return 'stale', 'the register says %r now, the proposal was measured against %r' % (now[:80], cur[:80])
    if f == 'status':
        a, b = status_word(now), status_word(new)
        if r.get('event') == 'roadmap':
            return 'editor', 'a status stated for the future (%s → %s): how a target is recorded is the editor\'s call' % (a, b)
        was, will = A.is_device(m), A.is_device(m, new)
        if was != will:
            return 'editor', 'moves the machine %s the device counts of §8 (%d → %d devices)' % (
                'into' if will else 'out of', A.devices, A.devices + (1 if will else -1))
        if (a in DEVICE) != (b in DEVICE):
            return 'editor', 'status %s → %s crosses the device boundary (the device count stays %d: a flag excludes it)' % (
                a, b, A.devices)
        return 'auto', 'status %s → %s stays %s the device set' % (a, b, 'inside' if b in DEVICE else 'outside')
    if f in HOLD_FIELDS:
        return 'hold', 'two-qubit error waits for WP2 (protocol, scope and conditioning per figure; review R1-1)'
    if f == 'status_date':
        y0, y1 = re.findall(r'(?:19|20)\d\d', now or ''), re.findall(r'(?:19|20)\d\d', new or '')
        if y0 and y1 and y0[0] != y1[0]:
            return 'reject', ('status_date is the cohort date — when the machine first existed (build/machines_chapter.py) — '
                              'and %s → %s would move its cohort; a retirement date belongs in the status text' % (y0[0], y1[0]))
    if f in ('t1', 't2') and not COHERENCE_WORDS.search(r.get('quote', '')):
        return 'hold', ('the quote does not name T1/T2 (e.g. a cat qubit\'s bit-flip time): one key, one meaning — '
                        'waits for WP1\'s field dictionary (review R1-4)')
    twin = m.get(TEXT_TWIN.get(f, ''), '')
    if twin and re.search(r'(?<![\d.])%s(?![\d.])' % re.escape(re.sub(r'[^\d.]', '', new) or '\x00'), twin):
        return 'reject', ('the register\'s note already weighs this value and keeps another: «%s»' % twin[:140])
    if f in ('physical_qubits_num', 'qubits_accessible'):
        try:
            a, b = float((now or '').replace(',', '')), float(re.sub(r'[^\d.]', '', new) or 'x')
            if a and abs(b - a) / a > COUNT_JUMP:
                return 'editor', 'the count moves %g → %g (over %d %%): check the definition against the register\'s note' % (
                    a, b, COUNT_JUMP * 100)
        except ValueError:
            pass
    if f == 'roadmap':
        return 'editor', 'a roadmap is merged, not replaced: it feeds the forecast ledger and the roadmap checks of §8.5'
    if f == 'access' and access_class(now) != access_class(new):
        return 'editor', 'the access class changes (cloud / on-premises / laboratory), which §8.1 counts'
    if f in AUTO_FIELDS:
        return 'auto', 'a register figure with the owner\'s own words'
    return 'editor', 'field %s has no rule' % f


def triage(intake_dir, A, led):
    out = []
    dec = led['decisions']
    for name in FILES:
        for r in read_csv(os.path.join(intake_dir, 'data', name)):
            k = r.get('row_key')
            if not k or r.get('proposal_status', 'proposed') != 'proposed' or dec.get(k, {}).get('decision') in FINAL:
                continue
            t = {'row_key': k, 'file': name, 'issue': r.get('issue', ''), 'source_url': r.get('source_url', ''),
                 'paper_id': r.get('paper_id', ''), 'paper_title': r.get('paper_title', ''),
                 'evidence': r.get('evidence', ''), 'verified_locally': r.get('verified_locally', '')}
            if name == 'register-amendment-candidates.csv':
                tier, why = tier_register(r, A)
                mid = r['machine_id']
                t.update(subject=('machine', mid), link=atlas_link('machine', mid) if mid in A.machines else '',
                         field=r['field'], current=r.get('current', ''), proposed=r.get('proposed_value', ''),
                         event=r.get('event', ''), quote=r.get('quote', ''), source_class=r.get('source_class', ''),
                         register_now=(A.machines.get(mid) or {}).get(r['field'], ''))
            elif name == 'machine-candidates.csv':
                slug = A.org_alias.get(norm(r.get('organisation')))
                tier, why = 'editor', 'a new machine changes the register\'s counts; the session drafts its cells per layer'
                t.update(subject=('machine-candidate', r.get('candidate_id', '')), name=r.get('machine_name', ''),
                         org=r.get('organisation', ''), org_slug=slug or '',
                         link=atlas_link('organisation', slug) if slug else '', family=r.get('family', ''),
                         qubits=r.get('qubits', ''), status=r.get('status', ''), quote=r.get('what_is_known', ''),
                         source_class='')
            elif name == 'org-event-candidates.csv':
                oid = r.get('org_id', '')
                slug = oid if oid in A.orgs else A.org_alias.get(norm(oid))
                if (r.get('source_class') or '').upper() == 'D':
                    tier, why = 'reject', 'press alone is a lead'
                elif not slug:
                    tier, why = 'editor', 'organisation %r is not among the Atlas\'s organisations' % oid
                else:
                    tier, why = 'auto', 'an organisation event, recorded as a change-ledger statement'
                t.update(subject=('organisation', slug or oid), link=atlas_link('organisation', slug) if slug else '',
                         event=r.get('event', ''), summary=r.get('summary', ''), date=r.get('date', ''),
                         quote=r.get('quote', ''), source_class=r.get('source_class', ''))
            elif name == 'amendment-candidates.csv':
                nid, kind = r.get('node_id', ''), r.get('change_kind', '')
                if nid not in A.nodes:
                    tier, why = 'reject', 'technology %r is not in the graph' % nid
                elif re.search(r"reviewer'?s (own )?inference|not the paper'?s", r.get('why', ''), re.I):
                    tier, why = 'reject', 'the evidence is the reviewer\'s inference, not the paper\'s'
                elif kind in ('status', 'descriptor'):
                    tier, why = 'editor', 'a technology\'s %s changes what the Atlas says it is' % kind
                else:
                    tier, why = 'session', 'a note for the technology\'s brief (three languages), in the weekly pass'
                t.update(subject=('technology', nid), link=atlas_link('technology', nid) if nid in A.nodes else '',
                         change_kind=kind, change=r.get('change', ''), quote=r.get('why', ''),
                         node_status=(A.nodes.get(nid) or {}).get('status', ''))
            elif name == 'map-gaps-candidates.csv':
                tier, why = 'editor', 'a new technology for the map (the seven-attribute test, a brief in three languages)'
                t.update(subject=('gap', r.get('gap_id', '')), layer=r.get('layer', ''),
                         change=r.get('description', ''), quote=r.get('proposal', ''))
            elif name == 'records-candidates.csv':
                nid = r.get('node_id', '')
                tier, why = ('session', 'a technology record: the weekly pass checks that the paper\'s device is this '
                             'technology and how the number stands against the standing records') if nid in A.nodes else \
                            ('reject', 'technology %r is not in the graph' % nid)
                t.update(subject=('technology', nid), key=r.get('key', ''), num=r.get('num', ''), unit=r.get('unit', ''),
                         scope=r.get('scope', ''), date=r.get('date', ''), quote=r.get('note', ''),
                         link=atlas_link('technology', nid) if nid in A.nodes else '')
            else:   # works
                tier, why = 'attach', 'numbered only when a change citing it is applied'
                t.update(subject=('work', r.get('doi') or r.get('arxiv') or r.get('url')), for_nodes=r.get('for_nodes', ''),
                         change=r.get('why', ''), title=r.get('title', ''))
            if dec.get(k, {}).get('decision') == 'approved' and tier in ('editor', 'stale'):
                tier, why = 'auto', 'approved by the editor on %s (%s); %s' % (dec[k].get('date', ''), dec[k].get('reason', ''), why)
            t['tier'], t['why_tier'] = tier, why
            out.append(t)
    return out


def verify_list(rows):
    """The checks the session makes before an auto row is applied: open the source, find the quote verbatim."""
    v = []
    for t in rows:
        if t['tier'] in ('auto', 'editor', 'stale') and t.get('source_url') and t['file'] != 'works-candidates.csv':
            v.append({'row_key': t['row_key'], 'url': t['source_url'], 'quote': t.get('quote', '')[:400],
                      'tier': t['tier'], 'subject': '%s:%s' % tuple(t['subject'])})
    return v


# ---------------------------------------------------------------- the editor's packet
def md_cell(s, n=220):
    s = re.sub(r'\s+', ' ', str(s or '')).replace('|', '\\|')
    return s if len(s) <= n else s[:n - 1] + '…'


def packet(rows, A, date):
    ed = [t for t in rows if t['tier'] == 'editor']
    by = {}
    for t in rows:
        by[t['tier']] = by.get(t['tier'], 0) + 1
    L = ['# Intake %s — the editor\'s part' % date, '',
         'Undecided proposals of the digest: %s. The editor decides the %d rows below; the rest the session applies after '
         'checking each quote at its source, or keeps for a named later step.' % (
             ', '.join('%s %d' % kv for kv in sorted(by.items())), len(ed)), '']
    reg = [t for t in ed if t['file'] == 'register-amendment-candidates.csv']
    if reg:
        L += ['## Register changes', '', '| Machine | Field | Register now → proposed | Owner\'s words | Source | Why it is yours |',
              '| --- | --- | --- | --- | --- | --- |']
        for t in reg:
            L.append('| [%s](%s) | %s | %s → **%s** | «%s» | [%s](%s) | %s |' % (
                t['subject'][1], t['link'], t['field'], md_cell(t['register_now'], 60), md_cell(t['proposed'], 60),
                md_cell(t['quote'], 160), t.get('source_class', ''), t['source_url'], md_cell(t['why_tier'], 140)))
        L.append('')
    mc = [t for t in ed if t['file'] == 'machine-candidates.csv']
    if mc:
        L += ['## New machines', '', '| Machine | Owner | Family, qubits, status | What is known | Source |', '| --- | --- | --- | --- | --- |']
        for t in mc:
            owner = '[%s](%s)' % (t['org'], t['link']) if t['link'] else md_cell(t['org'], 60)
            L.append('| %s | %s | %s, %s, %s | %s | [source](%s) |' % (md_cell(t['name'], 60), owner, t['family'],
                     t['qubits'], t['status'], md_cell(t['quote'], 200), t['source_url']))
        L.append('')
    tech = [t for t in ed if t['file'] in ('amendment-candidates.csv', 'map-gaps-candidates.csv')]
    if tech:
        L += ['## Technologies', '', '| Technology | Change | Evidence | Paper |', '| --- | --- | --- | --- |']
        for t in tech:
            subj = '[%s](%s)' % (t['subject'][1], t['link']) if t.get('link') else 'new: %s' % md_cell(t['change'], 80)
            L.append('| %s | %s | %s | [%s](%s) |' % (subj, md_cell(t['change'], 200), md_cell(t['quote'], 200),
                                                    md_cell(t['paper_title'], 70), t['source_url']))
        L.append('')
    other = [t for t in ed if t['file'] == 'org-event-candidates.csv']
    if other:
        L += ['## Organisations', '', '| Organisation | Event | Owner\'s words | Source |', '| --- | --- | --- | --- |']
        for t in other:
            L.append('| %s | %s | «%s» | [%s](%s) |' % (md_cell(t['subject'][1], 40), t['event'], md_cell(t['quote'], 160),
                                                       t.get('source_class', ''), t['source_url']))
        L.append('')
    if not ed:
        L += ['Nothing for the editor in this intake.', '']
    L += ['Policy: build/intake.py TIER_RULES (the rule that sent each row here is in the last column).', '']
    return '\n'.join(L)


# ---------------------------------------------------------------- plan (after verification)
def plan(rows, verified, date):
    """Auto rows whose quote the session found at the source become a draft register patch and draft change-ledger items;
    the decisions to record follow. Rows not verified stay undecided; landed/reject/hold/attach/session are decided here."""
    ok = {v['row_key']: v for v in verified if v.get('quote_found')}
    failed = {v['row_key']: v for v in verified if v.get('checked') and not v.get('quote_found')}
    patch, items, decisions, manual = [], [], {}, []
    applied_papers = set()
    for t in rows:
        k, tier = t['row_key'], t['tier']
        base = {'file': t['file'], 'date': date, 'by': 'intake-run'}
        if tier == 'landed':
            decisions[k] = dict(base, decision='landed', reason=t['why_tier'])
        elif tier == 'reject':
            decisions[k] = dict(base, decision='rejected', reason=t['why_tier'])
        elif tier.startswith('hold'):
            decisions[k] = dict(base, decision='deferred', until='WP1' if 'WP1' in t['why_tier'] else 'WP2',
                                reason=t['why_tier'])
        elif tier == 'session':
            decisions[k] = dict(base, decision='deferred', until='weekly brief pass', reason=t['why_tier'])
        elif tier == 'auto' and k in failed:
            decisions[k] = dict(base, decision='deferred', until='a source that shows it',
                                reason='the quote was not found at the source on %s: %s' % (date, failed[k].get('note', '')))
        elif tier == 'auto' and k in ok:
            v = ok[k]
            ver = {'url': v['url'], 'quote_found': True, 'checked': v.get('checked', date)}
            if t['file'] == 'register-amendment-candidates.csv':
                fields = {t['field']: t['proposed']}
                patch.append({'machine_id': t['subject'][1], 'action': 'status' if t['field'] == 'status' else 'update',
                              'fields': fields, 'evidence': t['source_url'], 'note': 'qnews %s · %s' % (t['issue'], k),
                              'quote': t['quote'], 'text_twin': TEXT_TWIN.get(t['field'], '')})
                items.append({'kind': 'status' if t['field'] == 'status' else 'update',
                              'subject': {'type': 'machine', 'id': t['subject'][1]}, 'fields': fields,
                              'note': '«%s» (source class %s; digest intake %s)' % (t['quote'], t.get('source_class', ''), t['issue']),
                              'sources': [t['source_url']], 'intake': k})
            elif t['file'] == 'org-event-candidates.csv':
                items.append({'kind': 'statement', 'subject': {'type': 'organisation', 'id': t['subject'][1]},
                              'fields': {'event': t['event'], 'date': t.get('date', '')},
                              'note': '%s — «%s»' % (t.get('summary', ''), t['quote']), 'sources': [t['source_url']], 'intake': k})
            elif t['file'] not in ('register-amendment-candidates.csv', 'org-event-candidates.csv', 'records-candidates.csv'):
                manual.append({'row_key': k, 'file': t['file'], 'subject': t['subject'], 'why': t['why_tier'],
                               'change': t.get('change') or t.get('name', ''), 'source_url': t['source_url']})
                continue
            elif t['file'] == 'records-candidates.csv':
                items.append({'kind': 'update', 'subject': {'type': 'technology', 'id': t['subject'][1]},
                              'fields': {'record': {'key': t['key'], 'num': t['num'], 'unit': t['unit'], 'scope': t['scope'],
                                                    'date': t['date']}},
                              'note': t['quote'], 'sources': [t['source_url']], 'intake': k})
            decisions[k] = dict(base, decision='applied', change='data/changes/%s.json#%d' % (date, len(items) - 1),
                                verified=ver, reason=t['why_tier'])
            if t.get('paper_id'):
                applied_papers.add(t['paper_id'])
    for t in rows:   # works ride with an applied change of the same paper
        if t['tier'] == 'attach' and t.get('paper_id') in applied_papers:
            decisions[t['row_key']] = {'file': t['file'], 'date': date, 'by': 'intake-run', 'decision': 'applied',
                                       'reason': 'cited by an applied change of the same paper'}
    return {'date': date, 'register_patch': {'rows': patch, 'doubts': []}, 'change_items': items, 'decisions': decisions,
            'manual': manual}


# ---------------------------------------------------------------- check
def check(led, intake_dir=None):
    errs = []
    for k, d in led.get('decisions', {}).items():
        if d.get('decision') not in DECISIONS:
            errs.append('%s: decision %r' % (k, d.get('decision')))
        if d.get('decision') == 'rejected' and not d.get('reason'):
            errs.append('%s: rejected without a reason' % k)
        if d.get('decision') == 'approved' and d.get('by') != 'editor':
            errs.append('%s: approved by %r — only the editor approves' % (k, d.get('by')))
        if d.get('decision') == 'deferred' and not d.get('until'):
            errs.append('%s: deferred without `until`' % k)
        if d.get('file') not in FILES:
            errs.append('%s: file %r' % (k, d.get('file')))
    if intake_dir:
        keys = {r.get('row_key') for n in FILES for r in read_csv(os.path.join(intake_dir, 'data', n))}
        errs += ['%s: not in the intake' % k for k in led.get('decisions', {}) if k not in keys]
    return errs


# ---------------------------------------------------------------- cli
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('status'); s.add_argument('--intake'); s.add_argument('--rules', action='store_true')
    s = sub.add_parser('triage'); s.add_argument('--intake', required=True); s.add_argument('--out', required=True)
    s.add_argument('--date', default=dt.date.today().isoformat())
    s = sub.add_parser('plan'); s.add_argument('--triage', required=True); s.add_argument('--verified', required=True)
    s.add_argument('--out', required=True); s.add_argument('--date', default=dt.date.today().isoformat())
    s = sub.add_parser('record'); s.add_argument('--plan', required=True)
    s.add_argument('--manifest-updated', default='', help="the intake's landed-manifest.json `updated` read by this run")
    s.add_argument('--ticket', default='', help='the hand-off ticket that carries this run')
    s = sub.add_parser('decide'); s.add_argument('row_key', nargs='?'); s.add_argument('decision', nargs='?', choices=DECISIONS)
    s.add_argument('--reason', default=''); s.add_argument('--by', default='editor'); s.add_argument('--file', default='')
    s.add_argument('--until', default=''); s.add_argument('--change', default='')
    s.add_argument('--from', dest='src', default='', help='a JSON list of {row_key, decision, reason[, until, by, date]}: '
                   "the editor's answers as a session wrote them (00_admin/intake/decisions/*.json)")
    s.add_argument('--intake', default='', help='resolve each row_key\'s intake file from this folder')
    s = sub.add_parser('check'); s.add_argument('--intake')
    a = ap.parse_args(argv)
    led = load_ledger()
    if a.cmd == 'status':
        if a.rules:
            for w, cond, tier in TIER_RULES:
                print('%-20s %-90s → %s' % (w, cond, tier))
            return 0
        rows = triage(a.intake, Atlas(), led) if a.intake else []
        by = {}
        for t in rows:
            by.setdefault(t['file'], {}).setdefault(t['tier'], 0)
            by[t['file']][t['tier']] += 1
        print('decided: %d · undecided: %d' % (len(led['decisions']), len(rows)))
        for f, d in by.items():
            print('  %-36s %s' % (f, ', '.join('%s %d' % kv for kv in sorted(d.items()))))
        return 0
    if a.cmd == 'triage':
        A = Atlas()
        rows = triage(a.intake, A, led)
        os.makedirs(a.out, exist_ok=True)
        json.dump(rows, open(os.path.join(a.out, 'triage.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(verify_list(rows), open(os.path.join(a.out, 'verify.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        open(os.path.join(a.out, 'packet.md'), 'w', encoding='utf-8').write(packet(rows, A, a.date))
        by = {}
        for t in rows:
            by[t['tier']] = by.get(t['tier'], 0) + 1
        print('triage: %d undecided · %s · verify %d' % (len(rows), ', '.join('%s %d' % kv for kv in sorted(by.items())),
                                                          len(verify_list(rows))))
        return 0
    if a.cmd == 'plan':
        rows = json.load(open(a.triage, encoding='utf-8'))
        ver = json.load(open(a.verified, encoding='utf-8'))
        p = plan(rows, ver, a.date)
        os.makedirs(a.out, exist_ok=True)
        json.dump(p, open(os.path.join(a.out, 'plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(p['register_patch'], open(os.path.join(a.out, 'register_patch.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)   # the input of build/register_patch.py
        print('plan: %d register rows · %d ledger items · %d decisions · %d for a session by hand' % (
            len(p['register_patch']['rows']), len(p['change_items']), len(p['decisions']), len(p['manual'])))
        return 0
    if a.cmd == 'record':
        p = json.load(open(a.plan, encoding='utf-8'))
        for k, d in p['decisions'].items():
            led['decisions'][k] = d
        n = {}
        for d in p['decisions'].values():
            n[d['decision']] = n.get(d['decision'], 0) + 1
        led.setdefault('runs', []).append({'date': p['date'], 'manifest_updated': a.manifest_updated, 'ticket': a.ticket,
                                           'decided': dict(sorted(n.items()))})
        save_ledger(led)
        print('recorded %d decisions · ledger %d' % (len(p['decisions']), len(led['decisions'])))
        return 0
    if a.cmd == 'decide':
        where = {}
        if a.intake:
            for n in FILES:
                for r in read_csv(os.path.join(a.intake, 'data', n)):
                    where[r.get('row_key')] = n
        todo = json.load(open(a.src, encoding='utf-8')) if a.src else \
            [{'row_key': a.row_key, 'decision': a.decision, 'reason': a.reason, 'until': a.until, 'change': a.change,
              'by': a.by, 'file': a.file}]
        n = 0
        for e in todo:
            k = e['row_key']
            if e.get('decision') not in DECISIONS or not (e.get('file') or where.get(k)):
                print('skipped %s: decision %r, file unknown' % (k, e.get('decision'))); continue
            if led['decisions'].get(k, {}).get('decision') in FINAL and e['decision'] == 'approved':
                print('skipped %s: already %s' % (k, led['decisions'][k]['decision'])); continue
            d = {'file': e.get('file') or where[k], 'date': e.get('date') or dt.date.today().isoformat(),
                 'by': e.get('by') or 'editor', 'decision': e['decision'], 'reason': e.get('reason', '')}
            for x in ('until', 'change'):
                if e.get(x): d[x] = e[x]
            led['decisions'][k] = d; n += 1
        save_ledger(led)
        print('decided %d' % n)
        return 0
    if a.cmd == 'check':
        errs = check(led, a.intake)
        print('intake ledger: %d decisions · %s' % (len(led['decisions']), 'OK' if not errs else '%d problems' % len(errs)))
        for e in errs[:40]:
            print('  ' + e)
        return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
