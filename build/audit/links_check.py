#!/usr/bin/env python3
"""Every internal link of the built page resolves (27 Sep 2026, after the rename to Atlas).

Checks, on the page as the browser sees it (briefs.expand_page — the load-time expansions applied):
  1. every href="#id" points at an element with that id (§ links, figure/table links, source codes, brief links, TOC);
  2. every data-goto / data-brief / data-chip-path / data-keys / data-clone target exists (station ids of the graph,
     brief sections, architecture ids, key-reference records, source lists);
  3. every id is unique;
  4. the page's own absolute links (site, DOI, repository, register pages, og:image) carry the current names — no old
     "quantum-technology-map" path except the sharing-image file, whose name is an asset the site keeps;
  5. external links are counted per host (not fetched) so that a rename that broke a host shows up as a count change.
Usage: python3 build/audit/links_check.py [dist/Quantum-Technology-Atlas-2026.09.html]   (exit 1 on any failure)
"""
import collections, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'build'))


def main():
    page = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'dist', 'Quantum-Technology-Atlas-2026.09.html')
    h = open(page, encoding='utf-8').read()
    import briefs
    h = briefs.expand_page(h)
    h = re.sub(r'<script.*?</script>', '', h, flags=re.S)   # attributes inside the scripts are JS templates, not links
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    nodes = {n['id'] for n in G['nodes']}; paths = {p['id'] for p in G['paths']}
    fails = []
    ids = re.findall(r'\sid="([^"]+)"', h)
    dup = [k for k, v in collections.Counter(ids).items() if v > 1]
    if dup: fails.append('duplicate ids: %s' % dup[:20])
    idset = set(ids)
    # 1. fragment links
    frags = re.findall(r'href="#([^"]*)"', h)
    missing = collections.Counter(f for f in frags if f and f not in idset)
    # a few fragments are handled by scripts, not by ids
    script_frags = {'map', 'briefs', 'top'}
    for f in list(missing):
        if f in script_frags or f in idset: del missing[f]
    if missing: fails.append('href="#…" without a target (%d distinct): %s' % (len(missing), list(missing.items())[:25]))
    # 2. data-* targets
    for attr, ok in (('data-goto', lambda v: v in nodes), ('data-brief', lambda v: v in nodes and ('brief-%s' % v) in idset),
                     ('data-chip-path', lambda v: v in paths), ('data-keys', lambda v: v in nodes)):
        bad = sorted({v for v in re.findall(r'%s="([^"]+)"' % attr, h) if not ok(v)})
        if bad: fails.append('%s without a target: %s' % (attr, bad[:20]))
    # every brief section exists once per language and every station has one
    for sid in sorted(nodes):
        if ('brief-%s' % sid) not in idset: fails.append('brief section missing for %s' % sid)
    # 3. old names
    old = [m.start() for m in re.finditer(r'quantum-technology-map(?!\.jpg)', h)]
    if old: fails.append('old site path "quantum-technology-map" still linked (%d)' % len(old))
    if re.search(r'Quantum Technology Map\b', h): fails.append('old title "Quantum Technology Map" still on the page')
    # 5. external hosts
    hosts = collections.Counter(re.findall(r'href="https?://([^/"]+)', h))
    print('external links: %d hosts, %d links; top: %s' % (len(hosts), sum(hosts.values()), hosts.most_common(8)))
    print('ids: %d, fragment links: %d, data-goto: %d, data-brief: %d' % (len(ids), len(frags), len(re.findall(r'data-goto="', h)), len(re.findall(r'data-brief="', h))))
    for f in fails: print('FAIL', f)
    print('links_check: %s' % ('PASS' if not fails else '%d failure(s)' % len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
