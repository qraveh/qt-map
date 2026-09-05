# -*- coding: utf-8 -*-
"""Editions of the Quantum Technology Map (calendar versioning YYYY.MM[.N]). Newest first.
Each edition = one Zenodo version DOI; the concept DOI resolves to the newest edition. Editions are cut when the graph changes
structurally (node/edge/coordinate), when a verdict changes, or when a headline number is corrected — otherwise ~quarterly."""

CONCEPT_DOI = '10.5281/zenodo.XXXXXXX'   # fill in after the first Zenodo publication (concept DOI = 'cite all versions')
REPO = 'https://github.com/qraveh/qt-map'
SITE = 'https://qodeh.com/qt-map'

EDITIONS = [
 {'edition': '2026.09', 'date': '2026-09-05', 'doi': '10.5281/zenodo.XXXXXXX',
  'en': ['First public edition. Goal-oriented comparison of all platforms (status 4 September 2026); technology graph of 96 nodes in ten layers, seven coordinates, five edge types, 14 platform paths; 96 technology briefs; bilingual EN/RU; CC BY 4.0.'],
  'ru': ['Первое публичное издание. Сравнение всех платформ по целям (состояние на 4 сентября 2026); граф технологий из 96 узлов в десяти слоях, семь координат, пять типов рёбер, 14 путей платформ; 96 брифов по технологиям; двуязычное EN/RU; CC BY 4.0.']},
]

def editions_html(lang):
    t = {'en': ('Editions', 'Edition', 'Date', 'DOI', 'Changes'), 'ru': ('Издания', 'Издание', 'Дата', 'DOI', 'Изменения')}[lang]
    rows = ''.join('<tr><td><b>%s</b></td><td>%s</td><td><a href="https://doi.org/%s">%s</a></td><td>%s</td></tr>' % (
        e['edition'], e['date'], e['doi'], e['doi'], ' '.join(e[lang])) for e in EDITIONS)
    return '<h3>%s</h3><div class="tbl"><table><thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>' % (t[0], t[1], t[2], t[3], t[4], rows)

def changelog_md():
    out = ['# Changelog — Quantum Technology Map', '', 'Editions use calendar versioning (YYYY.MM, optionally .N for a re-issue within the month). Each edition is archived on Zenodo with its own version DOI; the concept DOI %s resolves to the newest edition.' % CONCEPT_DOI, '']
    for e in EDITIONS:
        out += ['## %s — %s' % (e['edition'], e['date']), '', 'DOI: https://doi.org/%s' % e['doi'], ''] + ['- ' + c for c in e['en']] + ['']
    return '\n'.join(out)
