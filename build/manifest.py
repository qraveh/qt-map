#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dist/manifest.json — what the build wrote, for the deploy, the smoke test, the Wayback captures and the hand-off
(ticket 20261001-1, 2 Oct 2026): the edition, the main file, every language of build/langs.py with its folder, its page's
sha256 and size, the record-page counts, and the pictures the pages show. Deterministic — nothing but the edition's own
fields and the bytes of dist/ goes in, so the file reproduces byte for byte with the pages and is committed with them.

    python3 build/manifest.py            # write dist/manifest.json (build.py runs it last)
    python3 build/manifest.py --check    # exit 1 if the file is missing or does not match dist/
"""
import hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
from langs import LANGS, FOLDER, direction
import editions

DIST = os.path.join(ROOT, 'dist')
KINDS = ('technology', 'machine', 'architecture', 'organisation')   # the record-page folders, as build/pages.py writes them


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()


def manifest():
    ed = editions.EDITIONS[0]
    main = 'Quantum-Technology-Atlas-%s.html' % ed['edition']
    langs = {}
    for L in LANGS:
        folder = FOLDER[L]; page = os.path.join(DIST, folder, main)
        if not os.path.exists(page): raise SystemExit('manifest: %s missing — run build/build.py first' % os.path.relpath(page, ROOT))
        records = {}; npages = 0
        for k in KINDS:   # one page per record and an index.html per kind; record_pages counts both, as the build's own line does
            d = os.path.join(DIST, folder, k)
            html = [f for f in os.listdir(d) if f.endswith('.html')] if os.path.isdir(d) else []
            records[k] = sum(1 for f in html if f != 'index.html'); npages += len(html)
        langs[L] = {'folder': folder, 'path': folder + main, 'sha256': sha256(page), 'bytes': os.path.getsize(page),
                    'dir': direction(L), 'fragment': 'lang/%s.js' % L, 'record_pages': npages, 'records': records}
    mf = os.path.join(DIST, 'media-files.txt')
    media = [l for l in open(mf, encoding='utf-8').read().split('\n') if l] if os.path.exists(mf) else []
    return {'edition': ed['edition'], 'date': ed['date'], 'status': getattr(editions, 'STATUS', 'beta'), 'doi': ed.get('doi'),
            'main': main, 'default_lang': LANGS[0], 'languages': langs,
            'media': {'list': 'media-files.txt', 'count': len(media)}}


def dumps(m):
    return json.dumps(m, ensure_ascii=False, indent=1, sort_keys=True) + '\n'


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    m = manifest(); out = os.path.join(DIST, 'manifest.json')
    if '--check' in argv:
        cur = open(out, encoding='utf-8').read() if os.path.exists(out) else None
        if cur != dumps(m): raise SystemExit('manifest: dist/manifest.json %s — run build/build.py' % ('differs from dist/' if cur else 'missing'))
        print('manifest: up to date'); return
    open(out, 'w', encoding='utf-8', newline='\n').write(dumps(m))
    print('manifest.json written: %s' % ' · '.join('%s %s…' % (L, m['languages'][L]['sha256'][:16]) for L in LANGS))


if __name__ == '__main__':
    main()
