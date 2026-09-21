#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Release checklist for the Quantum Technology Map — one command, one PASS/FAIL per item.

    python3 build/audit/release_check.py            # static checks (≈ 3 min: builds twice)
    python3 build/audit/release_check.py --smoke    # + the Playwright smoke suite (≈ 6 min)
    python3 build/audit/release_check.py --vv       # + the V&V single suite against the oracle (≈ 3 min)

The static checks encode the bug classes that came back during September 2026 so they cannot come back silently:
  markdown tables emitted as text (rows without a blank line before them), mis-targeted table tags, headings whose ids
  drifted, hard-coded labels in tests, internal anchors that resolve nowhere, "§x.y" references to sections that do not
  exist, editor/AI/session/revision remnants in reader-facing text, family labels that differ between the map, §7 and §8,
  a build that is not byte-reproducible, a dist that is not committed. Exit code 1 when any item fails."""
import hashlib, html, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, 'dist', 'Quantum-Technology-Map-2026.09.html')
R = []


def item(name, ok, detail=''):
    R.append((name, bool(ok), detail))
    print(('  [ok]   ' if ok else '  [FAIL] ') + name + (('' if ok else ' — ' + str(detail)[:300])))


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run(cmd, timeout=300):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)


def text_of(h):
    t = re.sub(r'<script.*?</script>', '', h, flags=re.S); t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))


def main():
    print('release check —', ROOT)
    # 1. determinism: two builds, one hash; the tree clean afterwards
    r1 = run([sys.executable, 'build/build.py']); s1 = sha(DIST) if r1.returncode == 0 else None
    r2 = run([sys.executable, 'build/build.py']); s2 = sha(DIST) if r2.returncode == 0 else None
    item('build runs', r1.returncode == 0 and r2.returncode == 0, (r1.stderr or r2.stderr)[-300:])
    item('build is byte-reproducible (two runs, one sha256)', s1 and s1 == s2, (s1, s2))
    st = run(['git', 'status', '--porcelain']).stdout.strip()
    item('working tree clean after the build (dist committed)', st == '', st[:300])
    h = open(DIST, encoding='utf-8').read(); t = text_of(h)
    # 2. rendered-markdown integrity
    raw_rows = re.findall(r'<p>\|[^<]{0,200}', h)
    item('no markdown table rows rendered as paragraphs', not raw_rows, raw_rows[:2])
    stray = re.findall(r'<p>[^<]*\*\*[^<]*</p>', h)
    item('no unrendered ** emphasis in paragraphs', not stray, [x[:120] for x in stray[:2]])
    item('no escaped pipes (\\|) in the rendered text', '\\|' not in t)
    # 3. headings and ids: numbered, unique, in the TOC; §x.y references resolve
    ids = re.findall(r'<h[23] id="([^"]+)"', h)
    item('heading ids unique', len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1][:5])
    item('heading ids follow section numbers (en-s7-2 style)', all(re.match(r'(en|ru)-s(-about|\d+(-\d+)?)$', i) for i in ids), [i for i in ids if not re.match(r'(en|ru)-s(-about|\d+(-\d+)?)$', i)][:5])
    nav = re.findall(r'<nav class="toc".*?</nav>', h, flags=re.S)[0]; toc_hrefs = set(re.findall(r'href="#((?:en|ru)-s[^"]*)"', nav))
    # the TOC lists every h2 and the h3 of the graph and machines chapters (7.x, 8.x) by design
    must = [i for i in ids if re.match(r'(en|ru)-s\d+$', i) or re.match(r'(en|ru)-s[78]-\d+$', i)]
    missing_toc = [i for i in must if i not in toc_hrefs]
    item('every h2 and every 7.x/8.x h3 is in the TOC', not missing_toc, missing_toc[:6])
    secs = set(re.findall(r'<h3 id="en-s(\d+)-(\d+)"', h)); secs = {a + '.' + b for a, b in secs} | set(re.findall(r'<h2 id="en-s(\d+)"', h))
    refs = set(re.findall(r'(?<!CFR )§\s?(\d+(?:\.\d+)?)', t))   # "15 CFR §734.7" is a legal citation, not a section
    bad_refs = sorted(x for x in refs if x not in secs and not re.match(r'\d+\.\d+\.\d+', x))
    item('every §x.y reference names an existing section', not bad_refs, bad_refs[:8])
    # 4. sortable-table tags sit on the intended tables (a numeric column exists; the heading before the table matches the tag list)
    from importlib import import_module
    sys.path.insert(0, os.path.join(ROOT, 'build'))
    bh = import_module('build_html')
    problems = []
    for num, kind, nth in bh.SORT_TABLES:
        m = re.search(r'<h3 id="en-s' + num.replace('.', '-') + r'">', h)   # ids follow the section number
        if not m: problems.append((num, 'heading not found')); continue
        seg = h[m.end():]; nx = re.search(r'<h[23] id=', seg); seg = seg[:nx.start()] if nx else seg
        tbls = re.findall(r'<div class="tbl"[^>]*>', seg)
        if len(tbls) < nth or 'data-sort' not in tbls[nth - 1]: problems.append((num, 'tag not on table %d of %d' % (nth, len(tbls))))
    item('sortable-table tags land on the intended tables (by heading number)', not problems, problems)
    # 5. reader-facing text: no editor / AI / session / revision remnants (the Provenance line and Nature's "editor's note" are content)
    pats = [r"\beditor'?s? (?:review|decision|word|request|ruling)", r'\bbrief [A-F]\b', r'\bthis session\b', r'\bsubagent', r'\badjudication \d', r'\bRULES\.md', r'\bsince 1[0-9] Sep', r'\bbeta revision', r'\bБета-ревизи', r'рецензи[яи] редактора', r'\bTODO\b', r'\bTBD\b', r'\(brief ', r'\bV&V harness']
    hits = [(p, t[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')) for p in pats for m in re.finditer(p, t)]
    item('no editor/AI/session/revision remnants in the rendered text', not hits, hits[:3])
    # 6. internal anchors resolve; family labels agree across the map, §7 and §8
    all_ids = set(re.findall(r' id="([^"]+)"', h))
    hrefs = [x for x in re.findall(r'href="#([^"]+)"', h) if x and x != '!']
    dangling = sorted({x for x in hrefs if x not in all_ids and not x.startswith('n-') and not x.startswith('b-')})[:10]
    item('internal anchors resolve (static targets)', not dangling, dangling)
    mj = open(os.path.join(ROOT, 'build', 'map_js.py'), encoding='utf-8').read(); ms = open(os.path.join(ROOT, 'build', 'make_sections.py'), encoding='utf-8').read(); mc = open(os.path.join(ROOT, 'build', 'machines_chapter.py'), encoding='utf-8').read()
    f1 = dict(re.findall(r"(SC|ION|ATOM|PHOTON|SPIN|DEFECT|TOPO|ANNEAL):\['([^']+)'", mj)); f2 = dict(re.findall(r"'(SC|ION|ATOM|PHOTON|SPIN|DEFECT|TOPO|ANNEAL)':\('([^']+)'", ms)); f3 = dict(re.findall(r"'(SC|ION|ATOM|PHOTON|SPIN|DEFECT|TOPO|ANNEAL)': \('([^']+)'", mc))
    item('family labels agree across the map, §7 and §8', f1 == f2 == f3 and len(f1) == 8, (f1, f2, f3))
    # 6b. references and tooltips (21 Sep 2026): every citation code in the text has a source anchor; every cross-reference link
    #     resolves; no TeX remnant or currency-swallowed formula survives; every tooltip key has a text in both languages
    import html as _html, json as _json
    cited=set(re.findall(r'\[([A-Z]{1,2}\d{1,3})\]', t))
    for lang in ('en','ru'):
        anchored=set(re.findall(r'class="src" id="'+lang+r'-src-([A-Z0-9]+)"', h))
        item(f'every citation code has a source entry ({lang})', cited <= anchored, sorted(cited-anchored)[:8])
    remn=re.findall(r'\\(?:%|[A-Za-z]{2,})', t)
    item('no TeX remnants in the rendered text', not remn, remn[:6])
    item('no formula span longer than 60 characters (currency signs never open a formula)', 'class="m long"' not in h)
    tk=set(re.findall(r'data-t="([^"]+)"', h)); i=h.find('window.__TIPS='); j=h.find('</script>', i)
    tips=_json.loads(h[i+len('window.__TIPS='):j].rstrip(';')) if i>0 else {'en':{},'ru':{}}
    item('every tooltip key has a text in both languages', tk <= set(tips['en']) and tk <= set(tips['ru']), sorted(tk-set(tips['en']))[:5]+sorted(tk-set(tips['ru']))[:5])
    xr=[x for x in re.findall(r'<a class="xref" href="#([^"]+)"', h) if f' id="{x}"' not in h]
    item('every cross-reference (§, Figure, Table, H, F) resolves', not xr, xr[:6])
    # 7. the harness's own self-test and the chapter's classifiers still import
    to = run([sys.executable, 'build/audit/vv/test_oracle.py'])
    item('oracle self-test', to.returncode == 0 and 'OK' in (to.stdout + to.stderr), (to.stdout + to.stderr)[-200:])
    # 8. sizes
    item('dist under 12 MB', os.path.getsize(DIST) < 12 * 1024 * 1024, os.path.getsize(DIST))
    # optional: smoke, V&V single
    if '--smoke' in sys.argv:
        sm = run([sys.executable, 'build/audit/c2_smoke.py'], timeout=1200)
        item('smoke suite (Playwright)', 'RESULT: PASS' in sm.stdout, (sm.stdout + sm.stderr)[-400:])
    if '--vv' in sys.argv:
        env = dict(os.environ, VV_PAGE=DIST)
        vv = subprocess.run([sys.executable, 'runner.py', 'single', '--out', 'results_release/'], cwd=os.path.join(ROOT, 'build', 'audit', 'vv'), capture_output=True, text=True, timeout=1800, env=env)
        prog = open(os.path.join(ROOT, 'build', 'audit', 'vv', 'results_release', 'progress.log'), encoding='utf-8').read().strip().splitlines()[-1] if os.path.exists(os.path.join(ROOT, 'build', 'audit', 'vv', 'results_release', 'progress.log')) else ''
        item('V&V single suite: 0 disagreements', 'DONE' in prog and 'disagreements=0' in prog, prog)
    fails = [n for n, ok, d in R if not ok]
    print('RELEASE CHECK:', 'PASS' if not fails else 'FAIL ' + str(fails))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
