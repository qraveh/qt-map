# results_20261106 — the single suite on the build of 6 Nov 2026: the map's Table view mirrors the lit-set state (ticket 20261106-1)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out build/audit/vv/results_20261106` run on the dist of the commit that carries this folder (English page, Windows 11 / CPython 3.14.3, Playwright 1.64 Chromium — the local Code session's venv `C:\mine\umbrella\tools\qt-atlas-playwright`).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 376 | 0 | 143 | every lens value, every architecture, every technology, every machine alone — as results_c14, plus the table mirror on every state |

**What is new in the oracle (build/audit/vv/oracle.py):** `expected()` returns a fourth key, `table`, from the same state: `visible` = the lens term (every technology when no value is kept; the focused technology always) and `dimmed` = the visible technologies that are not lit. The rule is the ticket's S3: the lens filter *hides* rows in the table (the map dims them); an isolated architecture, a focused technology or a chosen machine *dims* rows (as the map does); the focused technology never disappears. The driver (`driver.py`) reads the table's rows from the DOM in either view (`#maptable [data-id]`: `.out` = hidden, `.dim` = dimmed); the runner (`runner.py`) compares them as `table_visible` / `table_dimmed` beside `stations`, `lines`, `edges` — only on a page that has the table (the frozen baseline of 8106b9e has none, so the older results folders are unchanged).

Every one of the 376 records carries the table sizes (`actual.table_visible`, `actual.table_dimmed`) and agrees with the oracle. The map's own lit-set logic (`litSets()`) did not change in this commit: the `stations`, `lines` and `edges` expectations are those of results_c14, and the run confirms them.

The Playwright suites on the same build: `c2_smoke` PASS (the Table-view suite `tableview()` added: the switch both ways, the row count, sort sets the lens, a legend chip filters both views and the count line, the pinned-first row, four pins and the refused fifth, the tray's tint, "show on the map", the fragment as a fresh load and as an in-page change, a section anchor, the Hebrew table); `mobile_check` PASS (the phone's card list, the layer scope, the legend wrap, no horizontal scroll at 390 px). The logs: `C:\mine\umbrella\tools\qt-atlas-playwright\runs\2026-11-06-local-20261106-1-*.log`.
