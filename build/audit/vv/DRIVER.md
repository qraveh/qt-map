# driver.py — mapping from driver calls to the page

Target: `dist/Quantum-Technology-Map-2026.09.html` (file URL). Source of the markup/JS: `build/build_html.py` (MAPUI) and `build/map_js.py`.

## Lit detection (read())
- **stations**: every `#mapwrap g.station` WITHOUT class `dim`; node id = text of its child `text.id`. (`dimming()` sets `dim` on stations not in `litSets().keepN`; `sel` marks the focused station, `member` marks stations of an isolated path, `peek` is hover-only.)
- **lines**: every `#mapwrap path.pathline` WITHOUT class `dim`; path id = `data-path`. Note: with a lens value on and no isolate/focus the page dims every line, and with the family lens it keeps that family's lines.
- **edges**: every `#mapwrap g.edge` present in the DOM (`drawEdges()` removes and re-creates them; none are drawn-but-hidden). `(u, v, type)` comes from the D3-bound datum `g.__data__.src/.dst/.type` — the edge elements carry no id attributes. `type` is the graph type (`requires`, `replaces`, `conflicts`); `edges_toggle_names` maps `replaces` → `alternatives`.
- **legend**: `glyphs` = `#glyphlegend [data-mark]` (hub/offd/empty); `lens` = `#lenslegend [data-lv]` buttons with `aria-pressed` and the count in `span.cnt` (the `data-lv=""` button is "clear filter").
- **path_card**: `#insp` innerText (empty when `hidden`). Shows the isolated path's card or the focused station's card.
- **selection_summary**: `#barsum` innerText, only while it is shown (the page fills it only when `#mapbar` has class `collapsed`).
- **bbox_overflow**: any element of `#mapbar`, `#mapwrap`, visible `#insp` whose client rect extends past the viewport's left/right edge, ignoring elements inside an in-viewport horizontally scrolling ancestor; OR the document itself scrolls horizontally. The SVG inside `#mapwrap` scrolls by design and is not counted.
- **table_rows()**: the `h3` whose text starts with `7.2` and whose id starts with the current language prefix (`en-`/`ru-`), then the next `table`; rows = `tbody tr` (`data-row` = node id) in DOM order. The table is static: no sort or filter UI exists, so `sort`/`filter` are always `None`.

## Controls (all by real clicks / keys)
| call | action | wait condition |
|---|---|---|
| `set_lens(name)` | `select_option` on `select#lens` | `#lens.value === name` |
| `select_value(v, multi)` | click `#lenslegend [data-lv="v"]`, Ctrl held when `multi` | re-rendered button's `aria-pressed` |
| `select_mark(m, multi)` (extra) | click `#glyphlegend [data-mark="m"]` (switches lens to `marks`) | `#lenslegend [data-lv="m"]` pressed |
| `clear_values()` | click `#lenslegend [data-lv=""]` | that button gone |
| `toggle(t, on)` | click `#tg-req` / `#tg-rep` / `#tg-conf` if state differs | `aria-pressed` |
| `isolate(pid)` | click `#pathchips [data-chip-path="pid"]` (clears focus on the page) | chip `aria-pressed="true"` |
| `clear_isolate()` | click the pressed chip again | chip `aria-pressed="false"` |
| `focus(id)` | click `rect.box` of the station whose `text.id` = id | a `g.station.sel` with that id |
| `clear_focus()` | key `Escape` (page handler: `select(null)`) | no `g.station.sel` |
| `reset()` | click `#tg-reset` | lens `family`, no `sel`, no pressed chip |
| `zoom(p)` | type p into `#zoomlvl`, Enter | `#zoomlvl.value === p+'%'` (clamped 20–250) |
| `fit_width()` / `fit_height()` | click `#zoom-fit` / `#zoom-fith` | two animation frames |
| `set_theme(t)` | no control on the page: emulate `prefers-color-scheme` and set `<html data-theme>` (page observes it via MutationObserver) | attribute set |
| `set_lang(l)` | click first visible `[data-setlang="l"]` | `#app[data-lang] === l` |
| `set_viewport(w,h)` | `page.set_viewport_size` | `innerWidth/innerHeight` |
| `collapse_bar(c)` | click `#bartog` if state differs | `#mapbar.collapsed === c` |

## State
`state()` is the driver's own record, updated from the calls it made (not read from the page): `{"lens", "values": set, "toggles": {requires, alternatives, conflicts}, "isolate", "focus"}`. It mirrors the page's rules for control interplay: a plain value click replaces the set (clicking the sole value clears it), Ctrl-click toggles membership, a lens change clears values, isolate clears focus, reset restores defaults. `page_state()` reads the same fields back from the DOM controls (`#lens`, pressed lens buttons, toggle `aria-pressed`, pressed chip, `g.station.sel`); smoke.py asserts they agree after each step. Not modelled: clicking a station while a path is isolated keeps the isolation; clicking an edge of type conflicts moves focus.

## Network
Chromium has no outbound network here; the one external request (Google Fonts CSS) is answered with an empty 200 via `page.route` so it does not surface as a console error. URLs are listed in `MapPage.external`.
