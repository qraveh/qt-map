# results_20261109 — the single suite on the build of 9 Nov 2026: the Table view's scope rule (local writer job 20261109-1)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out build/audit/vv/results_20261109` run on the dist of the commit that carries this folder (English page, Windows 11 / CPython 3.14.3, Playwright 1.64 Chromium — the local Code session's venv `C:\Users\raveh\.claude\tools\qt-atlas-playwright`; the log in its `runs/2026-11-09-20261109-1-*-vv_single.log`).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 389 | 0 | ≈ 160 | every lens value, every architecture, every technology, every machine alone (389 since the six technologies and the E2 machines of 7 Nov), with the table mirror on every state |

**What changed in the oracle (build/audit/vv/oracle.py, `expected().table`):** the editor's remark 4 of 9 Nov 2026, decided by the writer under his standing instruction of 6 Nov: an isolated architecture or a chosen machine now **hides** the rows outside it in the Table view (the two selections define a subset), a focused technology only **dims** (its meaning is its context), the lens filter hides as before, and the focused technology never disappears. So `visible` = the lens term ∩ the isolate's technologies ∩ the machine's technologies (+ the focused technology), `dimmed` = visible − lit. Until results_20261106 `visible` was the lens term alone. The map's lit-set logic (`litSets()`) did not change: the `stations`, `lines` and `edges` expectations are those of results_20261106 and the run confirms them.

The driver reads the rows from the DOM as before (`#maptable [data-id]`: `.out` = hidden, `.dim` = dimmed); the runner compares `table_visible` / `table_dimmed` beside `stations`, `lines`, `edges`. The audit's own 180-state matrix (isolate × machine × focus × lens filter in the driver's gesture order; `00_admin/30_working/AUDIT_2026-11-09_map-table-controls.md`) agrees with the same oracle before and after the change.

The Playwright suites on the same build: `c2_smoke` PASS (the Table-view suite extended: a kept filter survives a sort, the scope hides rows and is named with ✕, Escape returns to the architecture card, the card beside the stage and its ⇤ / ▣, the time ruler, the compare control, the machine select in view with the bar folded); `mobile_check` PASS.
