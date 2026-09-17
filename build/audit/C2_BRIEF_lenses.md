# C2 brief E — lens labels, reading-marks simplification, §7.6 diagonal (editor's decisions of 17 Sep 2026)

Budget 10 minutes. Working directory /home/claude/qt-map (branch c2-machines-2026-09-17). You own `build/map_js.py`, `build/page_css.py`, `build/build_html.py`, `build/make_sections.py`, `report/report_EN.md`, `report/report_RU.md`, `build/audit/vv/oracle.py`, `build/audit/vv/runner.py`, `build/audit/vv/RULES.md`, `build/audit/c2_smoke.py`. Nothing else.

## 1. Lens labels — logical and intuitive, no coordinate letters
The `LENSES` object in `map_js.py` (already in the editor's order) carries the report's coordinate letters "(a)…(g)", which now read as random. Replace the labels (EN / RU) with plain names, one scheme, colon-prefixed where a family of lenses exists:
```
family : Platform family                           / Семейство платформ
g      : Manufacturing technology                  / Технология производства
f      : Dominant error structure                  / Доминирующая структура ошибок
d      : Mobility / connectivity                   / Подвижность / связность
mod    : Control: modality                         / Управление: модальность
place  : Control: placement (temperature stage)    / Управление: размещение (температурная ступень)
time   : Characteristic time (gate or readout)     / Характерное время (гейт или считывание)
mech   : Readout: mechanism                        / Считывание: механизм
destr  : Readout: destructive?                     / Считывание: разрушающее?
mid    : Readout: mid-circuit?                     / Считывание: внутрисхемное?
det    : Entangling: deterministic / heralded      / Перепутывание: детерминированное / heralded
aff    : Carrier affinity: natural ↔ fabricated    / Сродство носителя: естественный ↔ изготовленный
status : Technology status                         / Статус технологии
```
The coordinate letter stays where it belongs — the station card's coordinate rows and the report — and may appear once in the lens legend's title as a muted suffix (e.g. "coordinate (e)") if the legend has a title; do not put it back into the dropdown.

## 2. Reading marks: no lens, badges instead (editor's decision)
- Remove the `marks` lens from `LENSES` and from every code path that offers it as a lens (lens select, `lensItems`, `lensValue/lensValues`, `lensColor`, `nodeMatchesFilter`, the code that switches to the marks lens on a legend-key click ~line 316, `catLabel`). The **glyphs on the stations** (◎ hub, ⤢ off-diagonal, ∅ empty slot) stay as drawn; the glyph-legend keys for them stay as **static keys with counts** (not clickable), each with a `title` giving the one-line definition below.
- Station card (`inspect(n)`): add a "Reading marks" line with badges when applicable — `◎ hub — required by stations of N families (…names…)` (N = reach families beyond its own; from `n.reach` / `n.reach_degree`), `⤢ off-diagonal — <flag definitions from the OFFDIAG vocabulary, e.g. "natural carrier + microwave control">` (from `n.offdiag`), `∅ empty slot` when status X. One line each, bilingual.
- Definitions (EN/RU) to use everywhere they appear: hub = "a station that stations of at least two families (or one family, recently) require — where a fix or a stall propagates across platforms" / "станция, которую требуют станции как минимум двух семейств (или одного — недавно): где исправление или застой распространяются на другие платформы"; off-diagonal = "a station that takes a trait from the other side of the natural/fabricated divide (see §7.6)" / "станция, берущая свойство с другой стороны раздела естественное/изготовленное (см. §7.6)".

## 3. §7.6 — the diagonal on paper
In `make_sections.py` (`sec9`, subsection 9.6 → 7.6), before the existing off-diagonal table, add a short paragraph and a 2×2 table (EN and RU): rows = carrier class of the path (natural: ions, atoms, photons, defects; fabricated: superconducting, spin, topological — take the classes from the paths' `cls`), columns = trait side (natural-side traits: optical control, µs–ms gates and readout, no semiconductor/photonic-chip fabrication, local connectivity; fabricated-side traits: microwave control, sub-µs gates, ≤ 10 µs readout, cold electronics at 4 K/mK, transport/long-range connectivity, erasure conversion, photonic interconnect). Diagonal cells: "the stereotype — most stations"; off-diagonal cells: list the flagged stations with their flags (`NAT_MW`, `NAT_FAST_GATE`, `NAT_FAST_READ`, `NAT_FAB` in the natural row; `FAB_FAR`, `FAB_ERASURE`, `FAB_COLD`, `FAB_PHOTONIC` in the fabricated row), computed from graph.json. Keep the existing table below it. Determinism as always.

## 4. Harness
`oracle.py`: remove the marks lens from the lens list and `lens_values`; `runner.py`: drop marks from `single`/`pairs`/`multi` generation and from the marks-legend informational check (the keys are static now); `RULES.md`: one line under §Adjudications ("10. 17 Sep: the reading-marks lens was removed at the editor's decision; the glyphs and static legend keys remain"). `c2_smoke.py`: the lens select has 13 options in the editor's order with the new labels (EN and RU); the station card of `code_surface` shows a hub badge and of `ct_sfq` an off-diagonal badge; legend keys not clickable (no lens change on click).

## Checks
`python3 build/build.py` twice → identical sha256; smoke PASS at 1280 and 400 px; `python3 build/audit/vv/test_oracle.py` passes. Reply (≤ 120 words): what changed per file, smoke and oracle-test results, dist delta.
