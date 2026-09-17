# C2 brief D — sortable tables with a restore-to-default (editor's review of 17 Sep 2026, second batch)

Budget 10 minutes. Working directory /home/claude/qt-map (branch c2-machines-2026-09-17). You own `build/map_js.py` (append a self-contained block after the table-zoom block), `build/page_css.py`, `build/build_html.py` (tagging only), `build/briefs.py` (one attribute), `build/make_sections.py` (one fix), `build/audit/c2_smoke.py` (add checks). Nothing else.

## Tables and what the editor asked
| table | where | sort behaviour |
|---|---|---|
| §3.1 Criteria scores (Platform · A … F · Maturity index) | report markdown, `### 3.1` | clicking **Platform** restores the default (build) order; every other column sorts asc/desc (numeric; cells contain `**bold**` markup — read the number) |
| §7.4 derived clocks per path | `sec9` 9.4 → h3 "7.4" | every **numeric** column asc/desc; a **↺ default order** control restores the build order |
| §7.5 hubs, §7.6 off-diagonal | h3 "7.5", "7.6" | same rule (numeric columns: Paths, Since, …); ↺ default |
| §7.12 Table B (machines vs path clock) | second table under h3 "7.12" | numeric columns asc/desc (values like `6.51e-7 s`, `×6.0`, `2.4 µs` — parse the first number, ignore text/units; `—`/`n/a`/empty sort last); ↺ default |
| §7.11 standard records | h3 "7.11" | sortable by **date** (values `2024-12`, `2020-08`, `2014-02`; also accept `Dec 2024`) asc/desc; ↺ default |
| Technology brief index (`div.tbl.bidx`, one per language, 96 rows: layer · id · technology · centrality · one line) | `build/briefs.py` | sortable by **centrality** asc/desc; ↺ default (the build order is grouped by layer) |

## Implementation
- **Tagging at build time**: in `build_html.py` add `data-sort="..."` to the `div.tbl` that follows the named h3 (there is a helper pattern at ~line 138 that finds the `div.tbl` after an h3 by its number; reuse it; for 7.12 take the second `div.tbl` after the h3). Values: `platform-default` (3.1), `numeric` (7.4, 7.5, 7.6, 7.12 B), `date` (7.11). In `briefs.py` add `data-sort="centrality"` to the two `div.tbl.bidx`. Every tagged table also gets `data-default="build"` so the JS knows it may restore.
- **JS** (`map_js.py`, appended block `tblsort`): on load, for each `div.tbl[data-sort]`: remember the original `<tr>` order (WeakMap); decide sortable columns — `numeric`: a column is sortable when ≥ 60 % of its body cells parse to a number (first number in the text: `[-−+]?\d[\d,]*(\.\d+)?([eE][-+]?\d+)?`, unicode minus, thousands commas; `—`, `n/a`, `not published`, empty → null, sorted last in both directions); `date`: the column whose header contains "date"/"дата" or whose cells match `^\d{4}-\d{2}`; `centrality`: the header named centrality/центральность; `platform-default`: the first column restores, the others numeric. Sortable headers get a `<button class="sortbtn">` with the header text and an indicator (` ▲` / ` ▼`, none in default order); click cycles asc → desc → default; `aria-sort` on the th. Rows keep their identity (move the same `<tr>` nodes; grouped-row tables such as 7.11 keep any group/header rows where they are — if a table has multi-row groups, sort within the tbody only and say so in the report).
- **↺ default order**: a small button in the table's toolbar (`div.tblzoom` when it exists; otherwise create a minimal toolbar with only this button), labelled `↺ default order` / `↺ исходный порядок` (lang-en/lang-ru spans); it restores the original order and clears indicators. For 3.1 the Platform header does the same.
- **§7.11 malformed row**: the ion T2 record's text contains `|0>,|1>` (records.json line ~199) — the pipes split the markdown row. Fix in `make_sections.py`'s renderer: escape `|` as `\|` in every cell it emits for §7.11 (and any other sec9 table that prints free text), so the row renders with the right number of cells. Do not edit records.json.
- CSS: sort buttons look like the header text (no border), indicator muted; toolbar consistent with the zoom bar; nothing overflows at 400 px.
- Determinism: no timestamps; run `python3 build/build.py` twice → identical sha256.

## Checks (extend c2_smoke.py, keep PASS/FAIL)
3.1: click "Maturity index" → rows descending by that column after two clicks (first asc) → click "Platform" → original order. 7.4: click a numeric header twice → descending; ↺ → original. 7.11: the ion T2 row has the same number of cells as the header; sort by date asc → first row's date ≤ last; ↺ restores. Brief index: click centrality → sorted; ↺ restores (both languages). 0 console errors; 400 px no overflow.
Reply (≤ 120 words): which tables got which columns sortable (counts), the smoke result, the 7.11 fix confirmed, dist size delta, anything ambiguous you decided.
