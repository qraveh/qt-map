#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checks of build/intake.py on a fixture intake (contract rev 3 headers) against the repository's own register and graph.

    python3 build/audit/intake_test.py        prints one line per check; exit 1 on any failure
"""
import csv, json, os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'build'))
import intake as I

PROV = ['proposal_status', 'proposed', 'issue', 'paper_id', 'paper_title', 'source_url', 'evidence', 'verified_locally',
        'snapshot', 'row_key']
HEAD = {
    'register-amendment-candidates.csv': ['machine_id', 'field', 'current', 'proposed_value', 'event', 'quote', 'source_class'],
    'machine-candidates.csv': ['candidate_id', 'machine_name', 'organisation', 'body_id', 'country', 'city', 'family', 'qubits',
                               'status', 'what_is_known', 'why_missing', 'url', 'verification'],
    'org-event-candidates.csv': ['org_id', 'event', 'summary', 'date', 'quote', 'source_class'],
    'amendment-candidates.csv': ['node_id', 'layer', 'change_kind', 'change', 'why'],
    'map-gaps-candidates.csv': ['gap_id', 'kind', 'layer', 'description', 'machines', 'proposal'],
    'records-candidates.csv': ['key', 'num', 'unit', 'scope', 'date', 'node_id', 'url', 'note'],
    'works-candidates.csv': ['doi', 'arxiv', 'url', 'title', 'for_nodes', 'why'],
}
U = 'https://example.org/src'
RA = [
    ('k-tempo', dict(machine_id='ionq-tempo', field='status', current='DEPLOYED', proposed_value='ANNOUNCED', event='roadmap',
                     quote='IonQ Tempo Late 2026 100 99.9%', source_class='C')),
    ('k-retire', dict(machine_id='ibm-heron-r1', field='status', current='DEPLOYED', proposed_value='RETIRED', event='status',
                      quote='ibm_torino | 133 | 2026-04-01', source_class='C')),
    ('k-forte-err', dict(machine_id='ionq-forte', field='err_2q_median_num', current='0.004', proposed_value='0.004 (stated: 99.6%)',
                         event='spec', quote='IonQ Forte 36 99.6%', source_class='C')),
    ('k-forte-q', dict(machine_id='ionq-forte', field='physical_qubits_num', current='30', proposed_value='36', event='spec',
                       quote='IonQ Forte 36 99.6%', source_class='C')),
    ('k-aria', dict(machine_id='ionq-aria', field='qubits_accessible', current='', proposed_value='25', event='spec',
                    quote='providing up to 25 qubits in the Ionq Aria QPUs', source_class='C')),
    ('k-same', dict(machine_id='ibm-heron-r2', field='physical_qubits_num', current='156', proposed_value='156', event='spec',
                    quote='Heron r2 156 qubits', source_class='A')),
    ('k-stale', dict(machine_id='ibm-heron-r2', field='physical_qubits_num', current='150', proposed_value='160', event='spec',
                     quote='Heron 160 qubits', source_class='A')),
    ('k-press', dict(machine_id='ibm-heron-r2', field='access', current='cloud + on-prem (System Two)', proposed_value='cloud',
                     event='access', quote='x', source_class='D')),
    ('k-ghost', dict(machine_id='no-such-machine', field='t1', current='', proposed_value='1', event='spec', quote='x',
                     source_class='A')),
    ('k-cohort', dict(machine_id='ibm-heron-r1', field='status_date', current='Dec 2023', proposed_value='2026-04-01',
                      event='status', quote='ibm_torino | 133 | 2026-04-01', source_class='C')),
    ('k-bitflip', dict(machine_id='aliceandbob-helium', field='t1', current='', proposed_value='> 1 hour (measured bit-flip time)',
                       event='spec', quote='> 1 hour measured bit-flip time', source_class='C')),
    ('k-jump', dict(machine_id='ibm-nighthawk-r2', field='physical_qubits_num', current='120', proposed_value='458', event='spec',
                    quote='120 programmable qubits and 458 physical qubits', source_class='C')),
    ('k-jump2', dict(machine_id='ibm-heron-r2', field='physical_qubits_num', current='156', proposed_value='400', event='spec',
                     quote='Heron r2 400 qubits', source_class='A')),
    ('k-roadmap', dict(machine_id='pasqal-orion', field='roadmap', current=None, proposed_value='200+ logical qubits by 2029',
                       event='roadmap', quote='200+ logical qubits by 2029', source_class='C')),
    ('k-access', dict(machine_id='ibm-heron-r2', field='access', current='cloud + on-prem (System Two)', proposed_value='lab-only',
                      event='access', quote='lab only', source_class='A')),
    ('k-planned', dict(machine_id='ibm-kookaburra', field='status', current='', proposed_value='DEMONSTRATED',
                       event='status', quote='Kookaburra demonstrated', source_class='A')),
]


def write(d, name, rows):
    os.makedirs(os.path.join(d, 'data'), exist_ok=True)
    with open(os.path.join(d, 'data', name), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=HEAD[name] + PROV, lineterminator='\n'); w.writeheader()
        for k, r in rows:
            w.writerow(dict(r, proposal_status='proposed', proposed='2026-10-06', issue='2026-10-06', source_url=U,
                            row_key=k, paper_id=r.get('paper_id', ''), verified_locally='no'))


fails = 0


def check(ok, what):
    global fails
    print(('ok   ' if ok else 'FAIL ') + what)
    fails += 0 if ok else 1


A = I.Atlas()
# the fixture pins the register values it tests, so the checks hold whatever later intakes change in the real register
FIXED = {'ibm-heron-r1': {'status': 'DEPLOYED', 'status_date': 'Dec 2023'}, 'ionq-aria': {'qubits_accessible': ''},
         'ionq-forte': {'physical_qubits_num': '30', 'physical_qubits': "IonQ's page says 36; the benchmark of record is a "
                        "30-ion chain covering all 435 pairs"},
         'ibm-heron-r2': {'physical_qubits_num': '156', 'physical_qubits': '156 (heavy-hex)', 'access': 'cloud + on-prem (System Two)'},
         'ibm-nighthawk-r2': {'physical_qubits_num': '120', 'physical_qubits': '120 programmable qubits (458 on-chip elements)'},
         'ibm-kookaburra': {'status': 'PLANNED (not delivered)', 'flags': 'schedule-risk'},
         'aliceandbob-helium': {'t1': ''}, 'ionq-tempo': {'status': 'DEPLOYED', 'flags': 'conflicting-count;target-not-device'}}
for _m, _f in FIXED.items():
    A.machines[_m] = dict(A.machines[_m], **_f)
A.devices = sum(1 for m in A.machines.values() if A.is_device(m))
reg = A.machines
for _k, _r in RA:
    if _r.get('current') is None: _r['current'] = reg[_r['machine_id']][_r['field']]
RA[-1][1]['current'] = reg['ibm-kookaburra']['status']
with tempfile.TemporaryDirectory() as d:
    write(d, 'register-amendment-candidates.csv', RA)
    write(d, 'machine-candidates.csv', [('k-new', dict(candidate_id='MC-1', machine_name='Zeta-200', organisation='IonQ',
                                                         family='ION', qubits='200', status='ANNOUNCED',
                                                         what_is_known='IonQ announced Zeta-200'))])
    write(d, 'org-event-candidates.csv', [('k-org', dict(org_id='ionq', event='acquisition', summary='IonQ acquires X',
                                                         date='2026-10-01', quote='IonQ to acquire X', source_class='B')),
                                          ('k-org-d', dict(org_id='ionq', event='funding', summary='rumour', date='',
                                                           quote='said to', source_class='D'))])
    write(d, 'amendment-candidates.csv', [
        ('k-note', dict(node_id='transmon', layer='L1 carrier', change_kind='note', change='add a TLS note', why='Fig. 3')),
        ('k-infer', dict(node_id='ct_sfq', layer='L5 control', change_kind='note', change='SK penalty',
                         why="Mapping finite-gate-set to SFQ angle quantization is this reviewer's inference, not the paper's.")),
        ('k-desc', dict(node_id='g_bos', layer='L3', change_kind='descriptor', change='broaden', why='Eq. 27')),
        ('k-ghostnode', dict(node_id='no_such_node', layer='L3', change_kind='note', change='x', why='y'))])
    write(d, 'map-gaps-candidates.csv', [('k-gap', dict(gap_id='Q-1', kind='technology', description='polar molecules'))])
    write(d, 'records-candidates.csv', [('k-rec', dict(key='t2', num='0.001', unit='s', scope='best', date='2026',
                                                       node_id='transmon', note='«T2 = 1 ms»', paper_id='P1'))])
    write(d, 'works-candidates.csv', [('k-work', dict(arxiv='2609.0001', title='W', for_nodes='transmon', why='x',
                                                      paper_id='P1')),
                                      ('k-work2', dict(arxiv='2609.0002', title='W2', for_nodes='ion', why='x', paper_id='P2'))])
    rows = I.triage(d, A, {'decisions': {}})
    T = {r['row_key']: r for r in rows}
    check(T['k-tempo']['tier'] == 'editor' and 'future' in T['k-tempo']['why_tier'],
          'Tempo: a status stated for the future goes to the editor, never applied by itself')
    check(T['k-retire']['tier'] == 'auto', 'a retirement from the owner\'s retired list (DEPLOYED → RETIRED) is applied')
    check(T['k-forte-err']['tier'] == 'hold', 'a two-qubit error waits for WP2')
    check(T['k-forte-q']['tier'] == 'reject' and 'already weighs' in T['k-forte-q']['why_tier'],
          'Forte 30 → 36: the register\'s note already weighs IonQ\'s 36 against the 30-ion benchmark — a curated choice stands')
    check(T['k-aria']['tier'] == 'auto', 'a qubit count with the owner\'s words is applied')
    check(T['k-same']['tier'] == 'landed', 'a value the register already holds is landed, not news')
    check(T['k-stale']['tier'] == 'stale', 'a proposal measured against an older register value is stale')
    check(T['k-press']['tier'] == 'reject', 'press alone never changes the register')
    check(T['k-ghost']['tier'] == 'reject', 'an unknown machine is rejected')
    check(T['k-cohort']['tier'] == 'reject' and 'cohort' in T['k-cohort']['why_tier'],
          'a status_date that changes the year would move the cohort (§8.4 H7): rejected, the date goes in the status text')
    check(T['k-bitflip']['tier'] == 'hold' and 'WP1' in T['k-bitflip']['why_tier'],
          'a cat qubit\'s bit-flip time is not T1: held for WP1\'s field dictionary (R1-4)')
    check(T['k-jump']['tier'] == 'reject', 'Nighthawk r2 «458 physical»: the register\'s note already explains 458 = qubits + couplers + resets')
    check(T['k-jump2']['tier'] == 'editor', 'a qubit count that jumps by more than 25 %% (156 → 400) is checked by the editor')
    check(T['k-roadmap']['tier'] == 'editor', 'a roadmap is merged by the editor, not replaced')
    check(T['k-access']['tier'] == 'editor', 'an access change that leaves the cloud / on-premises class is the editor\'s')
    check(T['k-planned']['tier'] == 'editor' and 'into' in T['k-planned']['why_tier'],
          'a planned machine reported demonstrated enters the device counts: the editor\'s')
    check(T['k-new']['tier'] == 'editor' and T['k-new']['org_slug'] == 'ionq', 'a new machine is the editor\'s; its owner resolves')
    check(T['k-org']['tier'] == 'auto' and T['k-org-d']['tier'] == 'reject', 'an SEC-filed acquisition is recorded; a rumour is not')
    check(T['k-note']['tier'] == 'session', 'a deep review\'s note goes to the weekly brief pass')
    check(T['k-infer']['tier'] == 'reject', 'the reviewer\'s own inference is rejected')
    check(T['k-desc']['tier'] == 'editor', 'a technology\'s descriptor is the editor\'s')
    check(T['k-ghostnode']['tier'] == 'reject', 'an unknown technology is rejected')
    check(T['k-gap']['tier'] == 'editor', 'a new technology is the editor\'s')
    check(T['k-rec']['tier'] == 'session' and T['k-work']['tier'] == 'attach',
          'a technology record goes to the weekly pass; a work waits for a citing change')
    V = I.verify_list(rows)
    vk = {v['row_key'] for v in V}
    check({'k-retire', 'k-aria', 'k-org', 'k-tempo'} <= vk and 'k-press' not in vk and 'k-work' not in vk,
          'the source checks cover the applied and the editor\'s rows, not the rejected or the works')
    ver = [{'row_key': 'k-retire', 'url': U, 'quote_found': True, 'checked': '2026-10-06'},
           {'row_key': 'k-aria', 'url': U, 'quote_found': False, 'checked': '2026-10-06', 'note': 'page changed'},
           {'row_key': 'k-org', 'url': U, 'quote_found': True, 'checked': '2026-10-06'}]
    p = I.plan(rows, ver, '2026-10-06')
    D = p['decisions']
    check(D['k-retire']['decision'] == 'applied' and D['k-retire']['verified']['quote_found'],
          'a verified auto row is applied, with its source check recorded')
    check(D['k-aria']['decision'] == 'deferred' and 'not found' in D['k-aria']['reason'],
          'an auto row whose quote is not at the source is deferred, not applied')
    check('k-tempo' not in D and 'k-new' not in D and 'k-gap' not in D, 'the editor\'s rows stay undecided until he decides')
    check(D['k-press']['decision'] == 'rejected' and D['k-same']['decision'] == 'landed'
          and D['k-forte-err']['until'] == 'WP2' and D['k-note']['until'] == 'weekly brief pass',
          'rejections, landings and holds are decided with their reason')
    check('k-work' not in D and 'k-work2' not in D and D['k-rec']['until'] == 'weekly brief pass',
          'works wait for a citing change; the record is deferred to the weekly pass')
    check([r['machine_id'] for r in p['register_patch']['rows']] == ['ibm-heron-r1']
          and p['register_patch']['rows'][0]['fields'] == {'status': 'RETIRED'},
          'the register patch holds exactly the verified register change')
    check(any(i['kind'] == 'statement' and i['subject']['type'] == 'organisation' for i in p['change_items']),
          'the organisation event becomes a change-ledger statement')
    led = {'decisions': dict(D)}
    check(not I.check(led, d), 'the ledger passes its own check against the intake')
    rows2 = I.triage(d, A, led)
    check(not ({'k-retire', 'k-press', 'k-same'} & {r['row_key'] for r in rows2}) and 'k-tempo' in {r['row_key'] for r in rows2},
          'a decided row is never triaged again; an undecided one stays')
    bad = {'decisions': {'x': {'file': 'nope.csv', 'decision': 'maybe'}}}
    check(len(I.check(bad)) == 2, 'the ledger check refuses an unknown decision and an unknown file')
    led3 = {'decisions': dict(D, **{'k-tempo': {'file': 'register-amendment-candidates.csv', 'date': '2026-10-07',
                                                 'by': 'editor', 'decision': 'approved', 'reason': 'D1 option A'},
                                     'k-gap': {'file': 'map-gaps-candidates.csv', 'date': '2026-10-07', 'by': 'editor',
                                               'decision': 'approved', 'reason': 'add'}})}
    rows3 = {r['row_key']: r for r in I.triage(d, A, led3)}
    check(rows3['k-tempo']['tier'] == 'auto' and 'approved by the editor' in rows3['k-tempo']['why_tier'],
          'an approved editor row comes back as an auto row, its approval quoted')
    p3 = I.plan(list(rows3.values()), [{'row_key': 'k-tempo', 'url': U, 'quote_found': True, 'checked': '2026-10-07'},
                                       {'row_key': 'k-gap', 'url': U, 'quote_found': True, 'checked': '2026-10-07'}], '2026-10-07')
    check(p3['decisions']['k-tempo']['decision'] == 'applied' and [m['row_key'] for m in p3['manual']] == ['k-gap']
          and 'k-gap' not in p3['decisions'],
          'the approved register change is planned; the approved new technology is left to the session, still undecided')
    check(len(I.check({'decisions': {'z': {'file': 'map-gaps-candidates.csv', 'decision': 'approved', 'by': 'intake-run'}}})) == 1,
          'only the editor approves')
    md = I.packet(rows, A, '2026-10-06')
    check('ionq-tempo' in md and 'Zeta-200' in md and (I.SITE + 'machine/ionq-tempo.html') in md, 'the packet names the editor\'s rows with Atlas links')
print('%s: %d failed' % ('intake_test', fails))
sys.exit(1 if fails else 0)
