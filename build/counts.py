# -*- coding: utf-8 -*-
"""Counts of the register per technology, as placeholders for the hand-written layer (29 Sep 2026).

A technology brief says how many register machines carry the technology ("The register lists 7 machines using it, among them …"),
and a technology's description on the map may say the same ("the most common ion control in the register (nine machines)"). Typed
in, those numbers went stale with the first re-cut of the register (ct_ionaod: twelve → fifteen). They are placeholders now:

    {{N_T_<TECH>_MACHINES}}   machines with a cell for the technology in any role (digits)
    {{N_T_<TECH>_PRIMARY}}    … as the primary technology of its layer
    {{N_T_<TECH>_ALTERNATE}}  … as an alternate
    {{N_T_<TECH>_DEVICES}}    … that are devices (deployed, demonstrated or retired; not a target or a component)
    {{N_T_<TECH>_VERIFIED}}   … whose cell for the technology is verified (✅: its cited source was opened and shows it; 30 Sep 2026)
    each also as _W (a word up to twenty, digits above; Hebrew masculine), _WF (feminine), _W_CAP / _WF_CAP (sentence start),
    and _MACH / _MACH_CAP for the counted noun ("seven machines" / «семь машин» / «שבע מכונות»).

<TECH> is the technology id upper-cased with hyphens as underscores (ct_ionaod → CT_IONAOD). build/make_sections.py fills the
map's descriptions when it writes data/graph.json; build/build_html.report_numbers fills the report, the glossaries and the briefs.
The words and declensions come from build/numwords.py; the device rule is machines_chapter's."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NON_DEVICE_FLAGS = {'target-not-device', 'component-only'}


def key(s): return re.sub(r'[^A-Z0-9]+', '_', str(s).upper()).strip('_')


def tech_counts(M=None):
    """{tech_id: {'MACHINES': n, 'PRIMARY': p, 'ALTERNATE': a, 'DEVICES': d, 'VERIFIED': v}} from data/machines.json"""
    if M is None: M = json.load(open(os.path.join(ROOT, 'data', 'machines.json'), encoding='utf-8'))
    out = {}
    for m in M['machines']:
        st = (m.get('status') or '').upper(); flags = set((m.get('profile') or {}).get('flags', []))
        device = st.startswith(('DEPLOYED', 'DEMONSTRATED', 'RETIRED')) and not (flags & NON_DEVICE_FLAGS)
        seen = set(); vseen = set()
        for cells in (m.get('layers') or {}).values():
            for c in cells:
                nid = c.get('node')
                if not nid or c.get('state', 'station') != 'station': continue
                d = out.setdefault(nid, {'MACHINES': 0, 'PRIMARY': 0, 'ALTERNATE': 0, 'DEVICES': 0, 'VERIFIED': 0})
                if nid not in seen:
                    d['MACHINES'] += 1; seen.add(nid)
                    if device: d['DEVICES'] += 1
                if (c.get('evidence') or {}).get('verified') and nid not in vseen:   # a machine counts once, on any verified cell
                    d['VERIFIED'] += 1; vseen.add(nid)
                if c.get('role') == 'primary': d['PRIMARY'] += 1
                elif c.get('role') == 'alternate': d['ALTERNATE'] += 1
    return out


def expand(prefix, d, lang):
    """a dict of counts → the placeholder variants (without the N_ prefix): digits, _W, _W_CAP, _WF, _WF_CAP; _MACH from 'MACHINES'"""
    import numwords as NW
    out = {}
    for k, v in d.items():
        out[f'{prefix}_{k}'] = NW.digits(lang, v)
        w = NW.word(lang, v, 'm'); wf = NW.word(lang, v, 'f')
        out[f'{prefix}_{k}_W'] = w; out[f'{prefix}_{k}_W_CAP'] = NW.cap(w); out[f'{prefix}_{k}_WF'] = wf; out[f'{prefix}_{k}_WF_CAP'] = NW.cap(wf)
    if 'MACHINES' in d:
        ph = NW.phrase(lang, d['MACHINES'], 'machine'); out[f'{prefix}_MACH'] = ph; out[f'{prefix}_MACH_CAP'] = NW.cap(ph)
    if 'DEVICES' in d:
        ph = NW.phrase(lang, d['DEVICES'], 'device'); out[f'{prefix}_DEV'] = ph; out[f'{prefix}_DEV_CAP'] = NW.cap(ph)
    return out


def tech_placeholders(lang, M=None, G=None):
    """{'T_CT_IONAOD_MACHINES': '15', …} for every technology of the graph (zero for one no machine carries)"""
    tc = tech_counts(M); out = {}
    ids = set(tc)
    if G is not None: ids |= {n['id'] for n in G.get('nodes', [])}
    for nid in ids:
        out.update(expand('T_' + key(nid), tc.get(nid, {'MACHINES': 0, 'PRIMARY': 0, 'ALTERNATE': 0, 'DEVICES': 0, 'VERIFIED': 0}), lang))
    return out


def fill(text, lang, vals):
    """replace {{N_…}} placeholders from vals (keys without the N_ prefix); an unknown placeholder raises"""
    def sub(m):
        k = m.group(1)
        if k not in vals: raise SystemExit('placeholder without a value: {{N_%s}}' % k)
        return vals[k]
    return re.sub(r'\{\{N_([A-Z0-9_]+)\}\}', sub, text)


if __name__ == '__main__':
    tc = tech_counts()
    for k in ('ct_ionaod', 'ct_ionmw', 'ct_vio', 'cx_reload', 'defect', 'fab_mbe', 'g_anneal', 'g_mwspin', 'ic_fanout', 'ic_multidie', 'ro_s2c', 'squeezed', 'code_detect', 'code_magic', 'fab_bulk', 'g_lointer', 'ct_ionlaser'):
        print(k, tc.get(k))
