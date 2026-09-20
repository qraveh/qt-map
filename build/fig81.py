# -*- coding: utf-8 -*-
"""Figure 8.1 — physical qubit count against median two-qubit error, one mark per registered machine that publishes both.
Inline SVG generated deterministically from data/machines.json (no library, no randomness). Colour by family with the
figure's own validated palette (light: the page's family hues; dark: steps re-validated against the dark surface);
gate-capable devices are filled marks, announcements/targets hollow; a few marks carry direct labels (the largest
gate-capable device and the best two-qubit error of each large family); every mark has a native tooltip (<title>);
Table 8.3 and the H1/H2 tables are the table view. Text uses the page's ink tokens, never the series colour."""
import json, math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import machines_chapter as mc

W, H = 760, 440
ML, MR, MT, MB = 62, 30, 14, 46
FAMS = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT']
LIGHT = {'SC': '#2A78D6', 'ION': '#D95926', 'ATOM': '#199E70', 'PHOTON': '#4A3AA7', 'SPIN': '#D55181', 'DEFECT': '#C98500'}
DARK = {'SC': '#3987E5', 'ION': '#DD5622', 'ATOM': '#1BAF7A', 'PHOTON': '#9085E9', 'SPIN': '#D9628F', 'DEFECT': '#EDA100'}


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def fmt_e(x):
    m, e = ('%.1e' % x).split('e')
    return '%s×10%s' % (m, str(int(e)).translate(mc.SUP))


def build(lang):
    en = lang == 'en'
    M, G, NODE, LAYERS, PATHS, MS = mc.prep()
    pts = [m for m in MS if m['q'] and m['err'] is not None and m['err'] > 0 and m['family'] in FAMS and not (m['flags'] & mc.EXCL_ERR_FLAGS)]
    pts.sort(key=lambda m: (m['family'], m['id']))
    xs = [math.log10(m['q']) for m in pts]; ys = [math.log10(m['err']) for m in pts]
    x0, x1 = 0, math.ceil(max(xs)); y1 = max(math.ceil(max(ys)), -1)
    y0 = math.floor(min(ys) * 2) / 2 - 0.2   # the bottom edge sits half a decade under the lowest mark; ticks stay on the decades
    def X(v): return ML + (math.log10(v) - x0) / (x1 - x0) * (W - ML - MR)
    def Y(v): return MT + (y1 - math.log10(v)) / (y1 - y0) * (H - MT - MB)
    o = []
    o.append('<figure class="fig81"><svg viewBox="0 0 %d %d" role="img" aria-labelledby="fig81t-%s" style="max-width:%dpx;width:100%%;height:auto;display:block">' % (W, H, lang, W))
    o.append('<title id="fig81t-%s">%s</title>' % (lang, esc('Physical qubit count against median two-qubit error, %d machines' % len(pts) if en else 'Число физических кубитов против медианной двухкубитной ошибки, %d машин' % len(pts))))
    o.append('<style>.fig81 .gl{stroke:var(--rule);stroke-width:1}.fig81 .ax{fill:var(--muted);font:11px "JetBrains Mono",monospace}.fig81 .lb{fill:var(--ink2);font:11px system-ui,sans-serif}.fig81 .lg{fill:var(--ink2);font:11.5px system-ui,sans-serif}'
             + ''.join('.fig81 .f-%s{fill:%s;stroke:%s}' % (f, LIGHT[f], LIGHT[f]) for f in FAMS)
             + '@media (prefers-color-scheme: dark){' + ''.join(':root:not([data-theme="light"]) .fig81 .f-%s{fill:%s;stroke:%s}' % (f, DARK[f], DARK[f]) for f in FAMS) + '}'
             + ''.join(':root[data-theme="dark"] .fig81 .f-%s{fill:%s;stroke:%s}' % (f, DARK[f], DARK[f]) for f in FAMS)
             + '.fig81 .hollow{fill:var(--surface)!important}.fig81 .mk{stroke-width:1.6}.fig81 .ring{fill:none;stroke:var(--surface);stroke-width:2}</style>')
    # grid and axes
    for e in range(x0, x1 + 1):
        x = X(10 ** e); o.append('<line class="gl" x1="%.1f" y1="%d" x2="%.1f" y2="%d"/>' % (x, MT, x, H - MB))
        o.append('<text class="ax" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, H - MB + 16, '{:,}'.format(10 ** e)))
    for e in range(int(math.ceil(y0)), y1 + 1):
        y = Y(10 ** e); o.append('<line class="gl" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>' % (ML, y, W - MR, y))
        o.append('<text class="ax" x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle">10%s</text>' % (ML - 6, y, str(e).translate(mc.SUP)))
    o.append('<text class="ax" x="%.1f" y="%d" text-anchor="middle">%s</text>' % ((ML + W - MR) / 2, H - 6, esc('physical qubits (log scale)' if en else 'физических кубитов (лог. шкала)')))
    o.append('<text class="ax" transform="translate(12,%.1f) rotate(-90)" text-anchor="middle">%s</text>' % ((MT + H - MB) / 2, esc('median two-qubit error' if en else 'медианная двухкубитная ошибка')))
    # marks: hollow = not a gate-capable device (announcement, target, component); a 2px surface ring under every mark
    for m in pts:
        x, y = X(m['q']), Y(m['err']); hollow = not m['gatedev']
        tip = '%s — %s · %s %s · %s %s' % (m['name'], m['org'], '{:,}'.format(m['q']), 'qubits' if en else 'кубитов', fmt_e(m['err']), 'median 2Q error' if en else 'медианная 2Q-ошибка')
        o.append('<g class="pt"><title>%s</title><circle class="ring" cx="%.1f" cy="%.1f" r="6.2"/><circle class="mk f-%s%s" cx="%.1f" cy="%.1f" r="4.6"/></g>' % (esc(tip), x, y, m['family'], ' hollow' if hollow else '', x, y))
    boxes = []   # occupied label boxes (x0, y0, x1, y1); marks are avoided by trying the four corners around the point
    marks = [(X(m['q']), Y(m['err'])) for m in pts]
    def free(bx0, by0, bx1, by1):
        if bx0 < ML or bx1 > W - MR or by0 < MT or by1 > H - MB: return False
        for a in boxes:
            if not (bx1 < a[0] or bx0 > a[2] or by1 < a[1] or by0 > a[3]): return False
        for mx, my in marks:
            if bx0 - 4 < mx < bx1 + 4 and by0 - 4 < my < by1 + 4: return False
        return True
    # legend (identity is never colour alone: the family name sits beside each swatch; hollow = announced/target)
    nleg = len([f for f in FAMS if any(m['family'] == f for m in pts)]) + 1
    lx, ly = W - MR - 236, MT + 12   # top-right: the empty corner of a count–error plane (few qubits at high error sit top-left)
    boxes.append((lx - 8, ly - 10, W - MR, ly + nleg * 16))
    for i, f in enumerate([f for f in FAMS if any(m['family'] == f for m in pts)]):
        o.append('<circle class="mk f-%s" cx="%d" cy="%d" r="4.6"/><text class="lg" x="%d" y="%d" dominant-baseline="middle">%s</text>' % (f, lx, ly + i * 16, lx + 10, ly + i * 16, esc(mc.t(lang, mc.FAMN[f]))))
    n = len([f for f in FAMS if any(m['family'] == f for m in pts)])
    o.append('<circle class="mk f-SC hollow" cx="%d" cy="%d" r="4.6"/><text class="lg" x="%d" y="%d" dominant-baseline="middle">%s</text>' % (lx, ly + n * 16, lx + 10, ly + n * 16, esc('hollow: announced, target or component' if en else 'пустой: анонс, цель или компонент')))
    # direct labels: the largest gate-capable device and the best error of each of the three large families
    lab = {}
    for f in ('SC', 'ION', 'ATOM'):
        fp = [m for m in pts if m['family'] == f and m['gatedev']]
        if fp:
            big = max(fp, key=lambda m: (m['q'], m['name'])); best = min(fp, key=lambda m: (m['err'], m['name']))
            lab[big['id']] = big; lab[best['id']] = best
    for mid in sorted(lab, key=lambda k: (X(lab[k]['q']), Y(lab[k]['err']))):
        m = lab[mid]; x, y = X(m['q']), Y(m['err']); txt = m['name'][:28]; wdt = 6.2 * len(txt) + 4
        cands = [(9, -9, 'start'), (9, 15, 'start'), (-9, -9, 'end'), (-9, 15, 'end'), (9, -22, 'start'), (-9, -22, 'end'), (9, 28, 'start'), (-9, 28, 'end'), (0, -15, 'middle'), (0, 20, 'middle'), (9, -36, 'start'), (-9, -36, 'end'), (9, 42, 'start'), (-9, 42, 'end')]
        chosen = None
        for dx, dy, anchor in cands:
            lx = x + dx; bx0 = lx if anchor == 'start' else (lx - wdt if anchor == 'end' else lx - wdt / 2); by0 = y + dy - 11
            if free(bx0, by0, bx0 + wdt, by0 + 13): chosen = (lx, y + dy, anchor, bx0, by0, bx0 + wdt, by0 + 13); break
        if not chosen:   # nothing free: keep the first candidate rather than drop the label (the tooltip still names the machine)
            dx, dy, anchor = cands[0]; lx = x + dx; chosen = (lx, y + dy, anchor, lx, y + dy - 11, lx + wdt, y + dy + 2)
        boxes.append(chosen[3:]); marks.append((x, y))
        o.append('<text class="lb" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (chosen[0], chosen[1], chosen[2], esc(txt)))
    o.append('</svg>')
    cap = ('<b>Figure 8.1 — Physical qubit count against median two-qubit error</b>, for the %d registered machines that publish both (hero-pair numbers excluded). The families separate along the qubit axis more than along the error axis — the reading behind H1 and H2; hover a mark for the machine.' % len(pts)) if en else \
          ('<b>Рисунок 8.1 — Число физических кубитов против медианной двухкубитной ошибки</b> для %d зарегистрированных машин, публикующих обе величины (рекордные пары исключены). Семейства расходятся по оси числа кубитов сильнее, чем по оси ошибки — это чтение, стоящее за H1 и H2; наведите на метку, чтобы увидеть машину.' % len(pts))
    o.append('<figcaption>%s</figcaption></figure>' % cap)
    return '\n'.join(o) + '\n', len(pts)


if __name__ == '__main__':
    svg, n = build(sys.argv[1] if len(sys.argv) > 1 else 'en'); sys.stdout.write(svg); sys.stderr.write('%d points\n' % n)
