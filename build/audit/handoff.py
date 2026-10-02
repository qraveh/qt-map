#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command hand-off of the current HEAD from the cloud clone to the local Code session (rev 3, 2 Oct 2026, tickets
20261001-1 and 20261002-1): the bundle, its clean-room proof, the ACCEPTANCE block of the note, and the machine-readable
manifest `<ticket>.json` that the code-side skill qt-atlas-code accepts (00_admin/skills/qt-atlas-code/references/manifest.md).

    python3 build/audit/handoff.py --ticket 20261002-1 --out <dir> [--note handoffs/HANDOFF_<date>_<slug>.md] [--rev N]
        [--full] [--class data,text,...] [--steps verify,fetch,checks,push] [--needs-word push] [--no-cleanroom] [--no-zip]

What it does:
  1. refuses a dirty working tree, a HEAD on main, or a branch that is not a child of main;
  2. the bundle, **incremental** by default (the editor's word of 2 Oct 2026): `git bundle create <out>/qt-map-<sha7>.bundle
     main..<branch>` plus any tag on the branch beyond main — only the new commits, tens of kilobytes instead of the 31 MB
     of the full history, so no parts and no inbox; its one prerequisite is main's commit, which the local clone holds.
     `--full` writes the old full-history bundle (`<branch> main --tags`) for a fresh clone; over 19 MB that one is also
     written in parts of 19 MB (`.00`, `.01`, …) for the device bridge's 20 MB cap, reassembled by concatenation;
  3. the clean room rehearses the local side's acceptance: a clone of this repository at main only, `git bundle verify`
     there (the prerequisite is present), `git fetch <bundle> <branch>`, the fetched head must be HEAD; then `build/build.py`,
     every file of dist/ equal to the working tree's byte for byte, the tree clean after the build; the site zip made there
     (build/site_zip.py, Info-ZIP) when present;
  4. the manifest: HEAD and refs as full shas, the bundle's kind, refs and prerequisites, the build's last lines, every
     language's page sha256 from dist/manifest.json, `change_class` from `git diff --name-only main...HEAD` (data / text /
     generator / ui / infra / edition — `ui` only when a page byte moved), `dist.changed` and `dist.pages_changed`,
     `removed_ids` (record pages deleted since main), the checks the classes call for (SKILL §4), the steps and which of
     them need the editor's word;
  5. prints the ACCEPTANCE block for the note and writes <out>/<ticket>.json.
Nothing here pushes, deletes or talks to the network."""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'build'))
from langs import LANGS

DEV_DOWNLOADS = r'C:\Users\raveh\Downloads'
DEV_INBOX = r'C:\MyDrive\QT-Map\50_data\inbox'
PART = 19 * 1024 * 1024
MUST_EXIST = ['build/build.py', 'build/editions.py', 'build/langs.py', 'build/manifest.py', 'build/site_zip.py', 'requirements.txt', 'dist/manifest.json']
UI = ('build/map_js.py', 'build/find_js.py', 'build/page_css.py', 'build/brief_js.py')
GENERATED = ('data/graph.json', 'data/machines.json', 'CHANGELOG.md', 'README.md', '.zenodo.json')   # written by the build: not a change of their own
CHECKS = {   # the matrix of SKILL §4, as commands the code side runs from the qt-map root; {thumbs} is its thumbs folder
    'data': ['build/audit/edges_check.py', 'build/audit/records_check.py', 'build/audit/machines_json_check.py', 'build/audit/propagate.py --check',
             'build/brief_refs.py --check', 'build/zenodo_meta.py --check'],
    'text': ['build/audit/text_lint.py', 'build/brief_refs.py --check', 'build/audit/propagate.py --check', 'build/audit/links_check.py'],
    'generator': ['build/audit/links_check.py --records', 'build/audit/text_lint.py', 'build/manifest.py --check'],
    'ui': ['build/audit/c2_smoke.py', 'build/audit/mobile_check.py'],
    'infra': ['build/manifest.py --check'],
    'edition': ['build/audit/release_check.py --smoke'],
}
ALWAYS = ['build/media.py --check --thumbs {thumbs}']


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()


def git(*a, cwd=ROOT):
    r = subprocess.run(['git'] + list(a), cwd=cwd, capture_output=True, text=True)
    if r.returncode: raise SystemExit('git %s failed: %s' % (' '.join(a), r.stderr.strip()))
    return r.stdout.strip()


def classify(paths):
    classes, generated = [], []
    for p in paths:
        if p.startswith('dist/'): continue
        if p in GENERATED: generated.append(p); continue
        if re.match(r'report/report_[A-Z]+\.md$', p):   # §7–§8 are regenerated into the reports; the hand-written sections make it text — the class is given when any of them moved
            classes.append('text') if 'text' not in classes else None; continue
        if p == 'build/editions.py':   # an edition only when the editions list or the status moved; the changelog writer and the errata are generator work
            d = subprocess.run(['git', 'diff', 'main...HEAD', '--', p], cwd=ROOT, capture_output=True, text=True).stdout
            c = 'edition' if re.search(r'^[+-](?!\+\+|--).*\b(EDITIONS\s*=|STATUS\s*=|\'edition\':|\'doi\':)', d, re.M) else 'generator'
        else:
            c = ('text' if p.startswith(('briefs/', 'data/i18n/', 'report/paths/')) else 'data' if p.startswith('data/')
                 else 'ui' if p in UI else 'generator' if p.startswith('build/') and p.endswith('.py') else 'infra')
        if c not in classes: classes.append(c)
    return classes, generated


def dist_tree(root):
    out = {}
    for d, _, fs in os.walk(os.path.join(root, 'dist')):
        for f in fs:
            p = os.path.join(d, f); out[os.path.relpath(p, root).replace(os.sep, '/')] = sha(p)
    return out


def main():
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    ticket = opt('--ticket')
    if not ticket: raise SystemExit('--ticket YYYYMMDD-N is required')
    out = os.path.abspath(opt('--out', os.path.join(ROOT, 'handoff_out'))); note = opt('--note'); rev = int(opt('--rev', '1'))
    if git('status', '--porcelain'): raise SystemExit('working tree not clean — commit first')
    head = git('rev-parse', 'HEAD'); short = head[:7]; subj = git('log', '-1', '--format=%s'); branch = git('rev-parse', '--abbrev-ref', 'HEAD')
    if branch == 'main': raise SystemExit('HEAD is on main — the cloud hands over a branch that is a child of main')
    main_sha = git('rev-parse', 'main')
    tags = {t: git('rev-parse', t + '^{}') for t in git('tag', '-l').split()}   # every tag with the commit it points at (the edition tag among them)
    if git('merge-base', 'main', 'HEAD') != main_sha: raise SystemExit('the branch is not a child of main — fetch and rebase first')
    # 2. the bundle — incremental (main..branch + the branch's own tags) unless --full
    full = '--full' in a
    os.makedirs(out, exist_ok=True); bundle = os.path.join(out, 'qt-map-%s.bundle' % short)
    if os.path.exists(bundle): os.remove(bundle)
    new_tags = [t for t in git('tag', '--merged', branch).split() if t not in git('tag', '--merged', 'main').split()]
    if full: git('bundle', 'create', bundle, branch, 'main', '--tags'); brefs = [branch, 'main'] + sorted(tags); prereq = []
    else: git('bundle', 'create', bundle, 'main..' + branch, *new_tags); brefs = [branch] + new_tags; prereq = [main_sha]
    v = subprocess.run(['git', 'bundle', 'verify', bundle], cwd=ROOT, capture_output=True, text=True)   # here main is present: the prerequisite resolves
    if v.returncode: raise SystemExit('bundle verify failed: ' + v.stderr)
    bsha = sha(bundle); bsize = os.path.getsize(bundle); parts = []
    if bsize > PART:
        with open(bundle, 'rb') as f:
            i = 0
            while True:
                chunk = f.read(PART)
                if not chunk: break
                pp = '%s.%02d' % (bundle, i); open(pp, 'wb').write(chunk); parts.append(os.path.basename(pp)); i += 1
    # 3. the clean room
    says, zsha, nzip = [], None, None
    if '--no-cleanroom' not in a:
        tmp = tempfile.mkdtemp(prefix='cleanroom-')
        git('clone', '-q', '--no-local', ROOT, tmp, '-b', 'main', cwd=ROOT)      # the local side's situation: a clone that holds main
        vv = subprocess.run(['git', 'bundle', 'verify', bundle], cwd=tmp, capture_output=True, text=True)
        if vv.returncode: raise SystemExit('clean room: bundle verify against a clone at main failed: ' + vv.stderr)
        git('fetch', '-q', bundle, '%s:%s' % (branch, branch), cwd=tmp); git('checkout', '-q', branch, cwd=tmp)
        if git('rev-parse', 'HEAD', cwd=tmp) != head: raise SystemExit('clean room: the bundle delivered %s, not HEAD %s' % (git('rev-parse', 'HEAD', cwd=tmp), head))
        b = subprocess.run([sys.executable, 'build/build.py'], cwd=tmp, capture_output=True, text=True, timeout=900)
        if b.returncode: raise SystemExit('clean-room build failed: ' + b.stderr[-800:])
        says = [l for l in b.stdout.splitlines() if l.startswith(('built ', 'zenodo cites:', 'CHANGELOG.md written'))]
        if git('status', '--porcelain', cwd=tmp): raise SystemExit('clean-room tree not clean after the build:\n' + git('status', '--porcelain', cwd=tmp))
        here, there = dist_tree(ROOT), dist_tree(tmp)
        diff = sorted(p for p in set(here) | set(there) if here.get(p) != there.get(p))
        if diff: raise SystemExit('clean-room dist differs from the working tree in %d file(s): %s' % (len(diff), ', '.join(diff[:8])))
        if '--no-zip' not in a and shutil.which('zip'):
            z = subprocess.run([sys.executable, 'build/site_zip.py'], cwd=tmp, capture_output=True, text=True, timeout=600)
            if z.returncode == 0:
                zp = os.path.join(tmp, 'quantum-technology-atlas-site.zip'); zsha = sha(zp); nzip = os.path.getsize(zp)
        shutil.rmtree(tmp, ignore_errors=True)
    # 4. the manifest
    dm = json.load(open(os.path.join(ROOT, 'dist', 'manifest.json'), encoding='utf-8'))
    changed = git('diff', '--name-only', 'main...HEAD').split()
    classes, generated = classify(changed)
    for c in (opt('--class', '') or '').split(','):
        if c and c not in classes: classes.append(c)
    dist_changed = any(p.startswith('dist/') for p in changed)
    pages_changed = any(p == 'dist/' + dm['languages'][L]['path'] for p in changed for L in LANGS)
    if 'ui' in classes and not pages_changed: classes.remove('ui')   # a UI module touched but no page byte moved: the Playwright suites would test nothing
    removed = sorted({re.sub(r'\.html$', '', p.split('/')[-1]) for p in git('diff', '--name-status', 'main...HEAD', '--', 'dist/').splitlines()
                      if p.startswith('D') and re.search(r'^D\s+dist/(?:[a-z]{2}/)?(technology|machine|architecture|organisation)/[^/]+\.html$', p)} - {'index'})
    checks = []
    for c in classes:
        for k in CHECKS.get(c, []):
            if k not in checks: checks.append(k)
    checks += [k for k in ALWAYS if k not in checks]
    steps = (opt('--steps', 'verify,fetch,checks,push')).split(','); needs = (opt('--needs-word', 'push')).split(',')
    m = {'ticket': ticket, 'rev': rev, 'note': note,
         'bundle': {'path': DEV_DOWNLOADS + '\\' + os.path.basename(bundle), 'sha256': bsha, 'bytes': bsize,
                    'kind': 'full' if full else 'incremental', 'refs': brefs, 'prerequisites': prereq,
                    'parts': parts, 'alt_paths': [DEV_INBOX + '\\' + os.path.basename(bundle)]},
         'head': {'sha': head, 'subject': subj, 'branch': branch},
         'refs': {'main': main_sha, 'tags': tags},
         'must_exist': MUST_EXIST,
         'build': {'cmd': 'pip install -r requirements.txt && python3 build/build.py', 'says': says},
         'dist': {'main': dm['main'], 'pages': {L: dm['languages'][L]['sha256'] for L in LANGS}, 'changed': dist_changed,
                  'pages_changed': pages_changed, 'changed_files': sum(1 for p in changed if p.startswith('dist/'))},
         'site_zip_sha256': zsha, 'site_zip_bytes': nzip,
         'change_class': classes, 'changed_files': [p for p in changed if not p.startswith('dist/')], 'generated_touched': generated,
         'checks': checks, 'removed_ids': removed, 'steps': steps, 'needs_word': needs}
    mp = os.path.join(out, ticket + '.json')
    open(mp, 'w', encoding='utf-8', newline='\n').write(json.dumps(m, ensure_ascii=False, indent=1) + '\n')
    # 5. the ACCEPTANCE block
    tagline = ', '.join('tag %s -> %s%s' % (t, s[:7], ' (= main)' if s == main_sha else '') for t, s in tags.items()) or 'no tags'
    acc = ['```', 'ACCEPTANCE',
           '  bundle          %s   (%s, %s bytes%s)' % (m['bundle']['path'], 'full history' if full else 'incremental: main..%s, prerequisite main %s' % (branch, main_sha[:7]),
                                                      '{:,}'.format(bsize), '; parts ' + ' '.join(parts) if parts else ''),
           '  bundle sha256   %s' % bsha,
           '  HEAD            %s  "%s"' % (head, subj),
           '  refs            %s -> %s; main -> %s; %s' % (branch, short, main_sha[:7], tagline),
           '  must exist      ' + ', '.join(MUST_EXIST),
           '  build cmd       ' + m['build']['cmd']]
    acc += ['  build says      ' + says[0]] + ['                  ' + s for s in says[1:]] if says else ['  build says      (no clean room run)']
    acc += ['  dist sha256     ' + ', '.join('%s %s…' % (L.upper(), dm['languages'][L]['sha256'][:16]) for L in LANGS),
            '  dist changed    %s' % ('yes (%d file%s; the pages %s)' % (m['dist']['changed_files'], '' if m['dist']['changed_files'] == 1 else 's', 'changed' if pages_changed else 'unchanged') if dist_changed else 'no'),
            '  removed ids     ' + (', '.join(removed) or '—'),
            '  change class    ' + (', '.join(classes) or '—'),
            '  tree after      git status --porcelain -> empty (working tree and clean room)',
            '  site zip        ' + ('sha256 %s (%s bytes, clean room, Info-ZIP)' % (zsha, '{:,}'.format(nzip)) if zsha else 'not made here'),
            '  origin/main at handout   %s' % main_sha[:7], '```']
    print('\n'.join(acc)); print('manifest', mp)


if __name__ == '__main__':
    main()
