#!/usr/bin/env python3
"""The Zenodo metadata as the record carries it (aligned with record 22674815 on 30 Sep 2026). .zenodo.json gets from the build
the English abstract as its description — the page's own sentence, the editor's text for ORCID — one isIdenticalTo per language
page, and one `cites` per work of the Atlas's shared numbering (data/work-numbers.json), in reference-number order: the publisher
DOI where the work has one, else its arXiv DOI 10.48550/arXiv.<id>. Web-only sources have no DOI and stay out, and so does the
Atlas's own section (a `map:` id — #687, §3.2). Edition 2026.09: 438 = 303 publisher DOIs + 135 arXiv DOIs; 444 web-only; one
self-reference.

    python3 build/zenodo_meta.py            # rewrites .zenodo.json when it is stale (build.py runs it)
    python3 build/zenodo_meta.py --check    # exit 1 when .zenodo.json differs from what the build gives
"""
import json, os, re, sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZEN = os.path.join(ROOT, '.zenodo.json')
TABLE = os.path.join(ROOT, 'data', 'work-numbers.json')
ARXIV = '10.48550/'


def cites():
    """[(n, doi)] in number order; counts {'doi': …, 'arxiv': …, 'web': …, 'self': …}"""
    works = json.load(open(TABLE, encoding='utf-8'))['works']
    out, k = [], {'doi': 0, 'arxiv': 0, 'web': 0, 'self': 0}
    for w in sorted(works, key=lambda w: w['n']):
        ids = w['ids']
        if any(i.startswith('map:') for i in ids): k['self'] += 1; continue
        doi = [i[4:] for i in ids if i.startswith('doi:') and not i.startswith('doi:' + ARXIV)]
        ax = [i[6:] for i in ids if i.startswith('arxiv:')] + [re.sub(r'^arxiv\.', '', i[4 + len(ARXIV):], flags=re.I) for i in ids if i.startswith('doi:' + ARXIV)]
        if doi: out.append((w['n'], doi[0])); k['doi'] += 1
        elif ax: out.append((w['n'], ARXIV + 'arXiv.' + ax[0])); k['arxiv'] += 1
        else: k['web'] += 1
    return out, k


def apply(z):
    """the metadata as the record carries it (aligned with Zenodo record 22674815 on 30 Sep 2026): the description is the
    English abstract — the page's own sentence, the editor's text for ORCID (build_html.abstract); one isIdenticalTo per
    language page; the other related identifiers (GitHub) kept; then the cites. What the legacy .zenodo.json format cannot
    hold stays on the record only: the three languages (the field takes one), the Russian and Hebrew abstracts and the
    technical description — Zenodo copies them into each new version."""
    sys.path.insert(0, os.path.join(ROOT, 'build'))
    import build_html; from editions import SITE; from langs import LANGS, FOLDER
    z['description'] = build_html.abstract('en')
    pages = [OrderedDict([('identifier', SITE + FOLDER[L]), ('relation', 'isIdenticalTo'), ('resource_type', 'publication-report')]) for L in LANGS]
    other = [r for r in z.get('related_identifiers', []) if r.get('relation') != 'cites'
             and not (r.get('relation') == 'isIdenticalTo' and str(r.get('identifier', '')).startswith('https://qodeh.com/'))]
    z['related_identifiers'] = pages + other + [OrderedDict([('identifier', d), ('relation', 'cites')]) for _, d in cites()[0]]
    return z


def render(z): return json.dumps(z, ensure_ascii=False, indent=2) + '\n'


def main(argv):
    cur = open(ZEN, encoding='utf-8').read()
    new = render(apply(json.loads(cur, object_pairs_hook=OrderedDict)))
    _, k = cites()
    summary = 'zenodo cites: %d (publisher DOI %d, arXiv DOI %d; left out: web-only %d, self %d)' % (k['doi'] + k['arxiv'], k['doi'], k['arxiv'], k['web'], k['self'])
    if '--check' in argv:
        print(summary + ('; .zenodo.json up to date' if new == cur else '; .zenodo.json STALE — run build/zenodo_meta.py'))
        return 0 if new == cur else 1
    if new != cur: open(ZEN, 'w', encoding='utf-8', newline='\n').write(new)
    print(summary + ('; .zenodo.json written' if new != cur else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
