# -*- coding: utf-8 -*-
"""Register the sources of the architecture narratives (report/paths/<pid>.en.md, 26 Sep 2026) and resolve their citation
placeholders: [@KEY] → [CODE] (a new §9 entry per family prefix, or the existing code when the work is already in
data/sources.json); the RU prose file, when present, is resolved with the same mapping.

    python3 build/paths_import.py META.json [META2.json …] [--dry]

META.json is the writer's meta file: {"pid", "sources": [{"key","prefix","label","record"}], …}. Placeholders whose KEY has
no source record are reported and left in place (the build stops on them).
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
import report_import as RI
from collections import OrderedDict

def main():
    a = sys.argv[1:]; dry = '--dry' in a; files = [x for x in a if x.endswith('.json')]
    en = RI.read_lines(RI.EN); ru = RI.read_lines(RI.RU); he = RI.read_lines(RI.HE) if os.path.exists(RI.HE) else None   # the Hebrew report carries the same §9 register lines (29 Sep 2026)
    data = json.load(open(RI.SRC, encoding='utf-8'), object_pairs_hook=OrderedDict)
    codes = {}; log = []
    for f in files:
        P = json.load(open(f, encoding='utf-8')); pid = P['pid']
        for s in P.get('sources', []):
            kind, val = RI.canon(s['key']); c = RI.existing_code(kind, val, data)
            if c: codes[s['key']] = c; log.append('%s: %s → existing [%s]' % (pid, s['key'], c)); continue
            c = RI.next_code(s['prefix'], data, en); codes[s['key']] = c
            r = RI.make_record(s.get('record') or {}, s['key']); data[c] = [r]
            label = s.get('label') or r.get('title', '')[:90]
            entry = ' · [%s] %s — %s' % (c, label, r['url'])
            for ls in (en, ru) + ((he,) if he else ()):
                i = RI.register_line(ls, s['prefix']); ls[i] = ls[i].rstrip() + entry
            log.append('%s: %s → new [%s]' % (pid, s['key'], c))
        for lang in ('en', 'ru', 'he'):
            pf = os.path.join(ROOT, 'report', 'paths', '%s.%s.md' % (pid, lang))
            if not os.path.exists(pf): continue
            txt = open(pf, encoding='utf-8').read()
            # canonical matching: a placeholder's key may differ in form from the sidecar key (arxiv id vs url) — resolve by canon
            def repl(m):
                k = m.group(1)
                if k in codes: return '[%s]' % codes[k]
                try: kind, val = RI.canon(k)
                except SystemExit: return m.group(0)
                c = RI.existing_code(kind, val, data)
                if c: return '[%s]' % c
                for kk, cc in codes.items():
                    try:
                        if RI.canon(kk) == (kind, val): return '[%s]' % cc
                    except SystemExit: pass
                log.append('%s [%s]: UNRESOLVED %s' % (pid, lang, k)); return m.group(0)
            new = RI.PH.sub(repl, txt)
            if new != txt and not dry: open(pf, 'w', encoding='utf-8', newline='\n').write(new)
            log.append('%s [%s]: %d placeholders left' % (pid, lang, len(RI.PH.findall(new))))
    for l in log: print(l)
    if dry: print('dry run'); return
    RI.write_lines(RI.EN, en); RI.write_lines(RI.RU, ru)
    if he: RI.write_lines(RI.HE, he)
    with open(RI.SRC, 'w', encoding='utf-8', newline='\n') as fh: json.dump(data, fh, ensure_ascii=False, indent=1); fh.write('\n')

if __name__ == '__main__':
    main()
