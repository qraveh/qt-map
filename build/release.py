#!/usr/bin/env python3
"""Stamp the edition's identifiers into every file that carries them, then (optionally) build.

    python3 build/release.py stamp --concept 10.5281/zenodo.C --version 10.5281/zenodo.V \
        [--site https://qodeh.com/publications/quantum-technology-map/] [--date YYYY-MM-DD] [--edition 2026.09] \
        --status beta|release [--build]
    python3 build/release.py show

Files touched: build/editions.py (CONCEPT_DOI, SITE, STATUS, EDITIONS[0].doi/date/edition), CITATION.cff, .zenodo.json, README.md.
`beta` = DOI reserved on Zenodo but not published: the document shows the DOI as reserved, cites the site, and emits no
citation_doi meta; CITATION.cff carries the url and no doi. `release` = the edition is published on Zenodo and the DOI resolves.
"""
import argparse, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOI_RE = re.compile(r'^10\.5281/zenodo\.\d+$')

def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8', newline='\n').write(s)

def current():
    ns = {}
    exec(rd('build/editions.py'), ns)
    e = ns['EDITIONS'][0]
    return dict(concept=ns['CONCEPT_DOI'], version=e['doi'], site=ns['SITE'], status=ns.get('STATUS', 'beta'), date=e['date'], edition=e['edition'])

def stamp(a):
    cur = current()
    concept, version = a.concept or cur['concept'], a.version or cur['version']
    site, status = a.site or cur['site'], a.status or cur['status']
    date, edition = a.date or cur['date'], a.edition or cur['edition']
    for d in (a.concept, a.version):
        if d and not DOI_RE.match(d): sys.exit('not a Zenodo DOI: %s' % d)
    if status not in ('beta', 'release'): sys.exit('status must be beta or release')
    # build/editions.py
    s = rd('build/editions.py')
    s = re.sub(r"CONCEPT_DOI = '[^']*'", "CONCEPT_DOI = '%s'" % concept, s)
    s = re.sub(r"SITE = '[^']*'", "SITE = '%s'" % site, s)
    s = re.sub(r"STATUS = '[^']*'", "STATUS = '%s'" % status, s)
    s = re.sub(r"(\{'edition': ')[^']*(', 'date': ')[^']*(', 'doi': ')[^']*(')", lambda m: m.group(1) + edition + m.group(2) + date + m.group(3) + version + m.group(4), s, count=1)
    wr('build/editions.py', s)
    # CITATION.cff
    c = rd('CITATION.cff')
    c = re.sub(r'^doi: .*\n', '', c, flags=re.M)
    if status == 'release':
        c = re.sub(r'^(url: .*)$', 'doi: "%s"\n\\1' % concept, c, count=1, flags=re.M)
    c = re.sub(r'^url: .*$', 'url: "%s"' % site, c, flags=re.M)
    c = re.sub(r'^date-released: .*$', 'date-released: "%s"' % date, c, flags=re.M)
    c = re.sub(r'^version: .*$', 'version: "%s"' % edition, c, flags=re.M)
    wr('CITATION.cff', c)
    # .zenodo.json
    z = json.loads(rd('.zenodo.json'))
    z['version'] = edition; z['publication_date'] = date
    z['notes'] = re.sub(r'https://qodeh\.com[^\s.]*', site, z.get('notes', ''))
    for r in z.get('related_identifiers', []):
        if str(r.get('identifier', '')).startswith('https://qodeh.com'): r['identifier'] = site
    wr('.zenodo.json', json.dumps(z, ensure_ascii=False, indent=2) + '\n')
    # README.md — header line and the citation line
    r = rd('README.md')
    r = re.sub(r'10\.5281/zenodo\.[0-9X]+', concept, r)
    r = re.sub(r'https://qodeh\.com/[^\s)\]]*', site, r)
    r = re.sub(r'qodeh\.com/qt-map', site.replace('https://', '').rstrip('/'), r)
    r = re.sub(r'\*\*Edition [^*]*\*\*', '**Edition %s%s**' % (edition, ' (beta)' if status == 'beta' else ''), r, count=1)
    r = re.sub(r'archived on Zenodo, DOI', ('DOI reserved on Zenodo,' if status == 'beta' else 'archived on Zenodo, DOI'), r, count=1)
    wr('README.md', r)
    print('stamped:', dict(concept=concept, version=version, site=site, status=status, date=date, edition=edition))
    if a.build:
        subprocess.run([sys.executable, os.path.join(ROOT, 'build', 'build.py')], check=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='cmd', required=True)
    st = sub.add_parser('stamp'); st.add_argument('--concept'); st.add_argument('--version'); st.add_argument('--site'); st.add_argument('--status'); st.add_argument('--date'); st.add_argument('--edition'); st.add_argument('--build', action='store_true')
    sub.add_parser('show')
    a = ap.parse_args()
    if a.cmd == 'show': print(json.dumps(current(), indent=2))
    else: stamp(a)
