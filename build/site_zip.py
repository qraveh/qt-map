#!/usr/bin/env python3
"""The site zip, byte for byte the same whoever makes it (the editor's word of 30 Sep 2026: the Release asset and the file on
Zenodo must be identical). Every file of dist/ except media/ (the deploy copies the pictures from the media register), in byte
order of the path, each stamped with the commit's time, packed by Info-ZIP under TZ=UTC with -X (no extra fields: no uid/gid,
no extended timestamps) and -D (no directory entries), permissions 0644.

    python3 build/site_zip.py [OUT]      # default: quantum-technology-atlas-site.zip beside dist/; prints files, bytes, sha256

The time is the committer time of HEAD (SOURCE_DATE_EPOCH overrides it); run it on a clean tree after build.py, on Linux or
macOS with Info-ZIP 3.0 — the CI job that attaches the Release asset runs exactly this.
"""
import hashlib, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
NAME = 'quantum-technology-atlas-site.zip'


def commit_time():
    if os.environ.get('SOURCE_DATE_EPOCH'): return int(os.environ['SOURCE_DATE_EPOCH'])
    return int(subprocess.run(['git', 'log', '-1', '--format=%ct', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip())


def files():
    out = []
    for d, dirs, fs in os.walk(DIST):
        rel = os.path.relpath(d, DIST).replace(os.sep, '/')
        if rel == 'media' or rel.startswith('media/'): dirs[:] = []; continue
        out += [(f if rel == '.' else rel + '/' + f) for f in fs]
    return sorted(out, key=lambda p: p.encode('utf-8'))


def main(out):
    out = os.path.abspath(out); t = commit_time(); names = files()
    for n in names:
        p = os.path.join(DIST, *n.split('/')); os.chmod(p, 0o644); os.utime(p, (t, t))
    if os.path.exists(out): os.remove(out)      # zip adds to an existing archive
    subprocess.run(['zip', '-X', '-D', '-q', out, '-@'], cwd=DIST, input='\n'.join(names) + '\n', text=True, check=True,
                   env=dict(os.environ, TZ='UTC', LC_ALL='C'))
    h = hashlib.sha256(open(out, 'rb').read()).hexdigest()
    print('site zip: %s — %d files, %d bytes, sha256 %s (time %d)' % (os.path.relpath(out, ROOT), len(names), os.path.getsize(out), h, t))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, NAME))
