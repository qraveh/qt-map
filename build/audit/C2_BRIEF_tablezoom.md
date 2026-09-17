# C2 brief C — zoom bar for the big tables (editor's review of 17 Sep 2026, item 3)

Budget 8 minutes. Working directory /home/claude/qt-map (branch c2-machines-2026-09-17). You own `build/map_js.py` (append a self-contained block at the end), `build/page_css.py`, and `build/build_html.py` only if a hook is unavoidable. No other files.

## What the editor asked
The map has a zoom control ("fit width", "1:1", editable percentage; see `.zoomctl` markup in `build_html.py` line ~158 and its JS in `map_js.py` ~line 43 and ~396). Give the same control — **fit width · 1:1 · percentage** only (no fit height, no align-to-top) — to every big table in the document.

## Design
- A table is "big" when its natural width exceeds its wrapper: `table.scrollWidth > wrapper.clientWidth + 8` measured at load and on resize (debounced). Wrappers are `div.tbl` (build_html.py wraps every markdown table; there are ~353 tables, most small — only the big ones get a bar). Skip tables inside `details.fold` that are closed (measure when opened: listen to `toggle`).
- The bar: a small `.zoomctl`-styled row placed just above the table inside the wrapper (`div.tblzoom`), buttons "fit width" (`⟷`), "1:1", and the `.zlvl` percentage input (Enter applies; 20–200 %). Bilingual labels via the existing `lang-en`/`lang-ru` spans or the `T()` helper; keep the map's look (reuse the `.zoomctl` classes).
- Scaling: `transform: scale(z)` with `transform-origin: 0 0` on the `<table>`, and the wrapper gets an inner sizer so the layout height/width follow the scaled table (set the sizer's `height = table.offsetHeight*z`, `width = table.offsetWidth*z`), so no dead space and no clipped rows. Fit width: `z = min(1, (wrapper.clientWidth - 2) / table.offsetWidth)`. 1:1: `z = 1` (the wrapper scrolls horizontally as today). Percentage: any value in range. Default for a big table: **fit width** (that is the reason the bar exists); remember the last choice per table in memory only (no storage).
- Keep the sticky first column/header behaviour working at z = 1; at z ≠ 1 it may simply switch off (add a class `zoomed` on the wrapper and neutralise the sticky rules under it in CSS).
- Phone width: the bar must wrap, never overflow (400 px test).
- Determinism: no timestamps, no randomness; the build must remain byte-reproducible.

## Checks
`python3 build/build.py` twice → identical sha256; a Playwright check (extend `build/audit/c2_smoke.py` with 4–6 assertions, keep its PASS/FAIL output): the §7.2 node table and the §7.10 edge list get a bar at 1280 px and are scaled to fit (no horizontal scroll in their wrappers), a small brief table gets no bar; "1:1" restores scale 1; typing 60 + Enter gives 0.6; at 400 px the bars exist and nothing overflows the viewport; 0 console errors.
Reply (≤ 120 words): how many tables got a bar at 1280 and at 400 px, the smoke result, the dist size delta.
