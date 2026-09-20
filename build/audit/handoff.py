#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command hand-off of the current HEAD from the cloud clone to the editor's machine.

    python3 build/audit/handoff.py --out /mnt/user-data/outputs/handoff --handoff <HANDOFF.md> [--readme <40_outputs/README.md>]

What it does (the protocol of 00_admin/Cloud-Local-Protocol.md, mechanised):
  1. refuses if the working tree is not clean;
  2. `git bundle create` for HEAD + the current branch + main + tags, `git bundle verify`, sha256;
  3. clean-room clone of the bundle, `build/build.py`, sha256 of dist — must equal the committed dist byte for byte;
  4. copies the bundle and the built document (named Quantum-Technology-Map-<edition>_<status>_<sha>.html, the
     programme's "one file per handed-over build") into --out and writes handoff_manifest.json with the device paths
     (Downloads for the bundle, 40_outputs for the snapshot);
  5. rewrites the ACCEPTANCE block of the HANDOFF file (between the ``` fences) and the "Current:" line of the
     40_outputs README when given, so the notes never carry stale hashes.
Prints the ACCEPTANCE block. Exit 1 on any failure. Nothing here pushes, deletes or talks to the network."""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST_NAME = 'Quantum-Technology-Map-2026.09.html'
DEV_DOWNLOADS = r'C:\Users\raveh\Downloads'
DEV_OUTPUTS = r'C:\MyDrive\QT-Map\40_outputs'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def git(*a, cwd=ROOT):
    r = subprocess.run(['git'] + list(a), cwd=cwd, capture_output=True, text=True)
    if r.returncode: raise SystemExit('git %s failed: %s' % (' '.join(a), r.stderr.strip()))
    return r.stdout.strip()


def main():
    args = sys.argv[1:]
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(ROOT, 'handoff_out')
    hpath = args[args.index('--handoff') + 1] if '--handoff' in args else None
    rpath = args[args.index('--readme') + 1] if '--readme' in args else None
    if git('status', '--porcelain'): raise SystemExit('working tree not clean — commit first')
    head = git('rev-parse', 'HEAD'); short = head[:7]; subj = git('log', '-1', '--format=%s'); branch = git('rev-parse', '--abbrev-ref', 'HEAD')
    main_sha = git('rev-parse', '--short', 'main'); tags = git('tag', '--points-at', 'main')
    os.makedirs(out, exist_ok=True)
    bundle = os.path.join(out, 'qt-map-%s.bundle' % short)
    if os.path.exists(bundle): os.remove(bundle)
    git('bundle', 'create', bundle, 'HEAD', branch, 'main', '--tags')
    v = subprocess.run(['git', 'bundle', 'verify', bundle], cwd=ROOT, capture_output=True, text=True)
    if 'complete history' not in (v.stdout + v.stderr): raise SystemExit('bundle verify failed: ' + v.stderr)
    bsha = sha(bundle)
    # clean room
    tmp = tempfile.mkdtemp(prefix='cleanroom-')
    git('clone', '-q', bundle, tmp, '-b', branch, cwd=ROOT)
    b = subprocess.run([sys.executable, 'build/build.py'], cwd=tmp, capture_output=True, text=True, timeout=600)
    if b.returncode: raise SystemExit('clean-room build failed: ' + b.stderr[-500:])
    buildline = [l for l in b.stdout.splitlines() if l.startswith('built ')][-1]
    dsha = sha(os.path.join(tmp, 'dist', DIST_NAME)); dsha_committed = sha(os.path.join(ROOT, 'dist', DIST_NAME))
    if dsha != dsha_committed: raise SystemExit('clean-room dist differs from the committed dist: %s vs %s' % (dsha, dsha_committed))
    if git('status', '--porcelain', cwd=tmp): raise SystemExit('clean-room tree not clean after the build')
    shutil.rmtree(tmp, ignore_errors=True)
    # snapshot named by status and sha
    sys.path.insert(0, os.path.join(ROOT, 'build')); import editions as ed
    status = getattr(ed, 'STATUS', 'beta'); edition = ed.EDITIONS[0]['edition']
    snap = 'Quantum-Technology-Map-%s_%s_%s.html' % (edition, status, short)
    shutil.copyfile(os.path.join(ROOT, 'dist', DIST_NAME), os.path.join(out, snap))
    acceptance = '\n'.join([
        '```', 'ACCEPTANCE',
        '  bundle sha256   %s…' % bsha[:16],
        '  HEAD            %s  "%s"' % (head, subj),
        '  refs            main -> %s (unchanged), %s -> %s, tag %s -> %s' % (main_sha, branch, head, tags or '—', main_sha),
        '  must exist      build/build.py, build/editions.py, build/machines_json.py, build/machines_chapter.py, data/machines.json, data/forecast-ledger.json, build/audit/vv/runner.py, build/audit/c2_smoke.py, build/audit/release_check.py, requirements.txt',
        '  build cmd       pip install -r requirements.txt && python3 build/build.py',
        '  build says      CHANGELOG.md written        (line before it: "%s")' % buildline,
        '  dist sha256     %s…   (produced in a clean room from this bundle; cloud Linux/CPython 3.12 — msi Windows/CPython 3.14 and CI ubuntu/3.12 must agree)' % dsha[:16],
        '  tree after      git status --porcelain -> empty',
        '  origin/main at handout   %s' % main_sha, '```'])
    manifest = {'head': head, 'short': short, 'branch': branch, 'subject': subj, 'bundle': {'file': bundle, 'sha256': bsha, 'device': DEV_DOWNLOADS + '\\' + os.path.basename(bundle)},
                'snapshot': {'file': os.path.join(out, snap), 'sha256': dsha, 'device': DEV_OUTPUTS + '\\' + snap}, 'buildline': buildline, 'acceptance': acceptance}
    if hpath:
        s = open(hpath, encoding='utf-8').read()
        s2 = re.sub(r'```\nACCEPTANCE\n.*?\n```', acceptance, s, count=1, flags=re.S)
        s2 = re.sub(r'qt-map-[0-9a-f]{7}\.bundle` \(sha256 [0-9a-f]{16}…\)', 'qt-map-%s.bundle` (sha256 %s…)' % (short, bsha[:16]), s2)
        s2 = re.sub(r'\$env:USERPROFILE\\Downloads\\qt-map-[0-9a-f]{7}\.bundle', lambda m: '$env:USERPROFILE\\Downloads\\qt-map-%s.bundle' % short, s2)
        # only the "Built document at this commit" line names the current snapshot; the "Obsolete drops" line names the old ones
        s2 = re.sub(r'(Built document at this commit: `[^`]*40_outputs\\)Quantum-Technology-Map-[0-9.]+_[a-z]+_[0-9a-f]{7}\.html', lambda m: m.group(1) + snap, s2)
        s2 = re.sub(r'\(= `dist/` of [0-9a-f]{7};', lambda m: '(= `dist/` of %s;' % short, s2)
        if s2 == s: print('note: HANDOFF file unchanged (no ACCEPTANCE block or names found)')
        open(hpath, 'w', encoding='utf-8', newline='\n').write(s2); manifest['handoff'] = hpath
    if rpath:
        s = open(rpath, encoding='utf-8').read()
        # the old "Current" becomes "Previous" (one line carries both, so the README never loses the last snapshot's record)
        pm = re.search(r'^Current: `([^`]+)` \(sha256 ([0-9a-f]+)…, (\d{4}-\d{2}-\d{2})', s, flags=re.M)
        prev = (' Previous: `%s` (sha256 %s…, %s; superseded by this build).' % pm.groups()) if pm and pm.group(1) != snap else ''
        if pm and pm.group(1) == snap: prev = re.search(r'^Current: .*?( Previous: .*)?$', s, flags=re.M).group(1) or ''
        line = 'Current: `%s` (sha256 %s…, %s; branch `%s`, HEAD %s%s — not yet merged to main).%s' % (snap, dsha[:32], __import__('datetime').date.today().isoformat(), branch, short, (', handoff `00_admin/%s`' % os.path.basename(hpath)) if hpath else '', prev)
        s2 = re.sub(r'^Current: .*$', lambda m: line, s, count=1, flags=re.M)
        open(rpath, 'w', encoding='utf-8', newline='\n').write(s2); manifest['readme'] = rpath
    json.dump(manifest, open(os.path.join(out, 'handoff_manifest.json'), 'w', encoding='utf-8'), indent=1)
    print(acceptance); print('bundle', bundle, bsha[:16], '| snapshot', snap, dsha[:16])


if __name__ == '__main__':
    main()
