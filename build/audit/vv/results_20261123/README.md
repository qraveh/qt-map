# results_20261123 — the single suite on the build of 23 Nov 2026: sorting in every language, the Hebrew page's false English twin (local writer job 20261123-1)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out results_20261123` run from `build/audit/vv/` on the dist of the commit that carries this folder (English page), with the Playwright venv's interpreter.

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 396 | 0 | ≈ 255 | every lens value, every architecture, every technology, every machine alone — the same 396 states as results_20261122 |

**What changed.** No oracle or driver code and no graph change: the job touches the sort block of `build/map_js.py` (QM-028), `build/langs.py`'s `fill_twins()` (QM-031), one list of paragraph openers in `build/build_html.py` and §1.2's header in the three reports (QM-029). The suite runs because the change-impact matrix asks it for generator code; it shows the lens and lit-set behaviour unchanged.

The Playwright suites on the same build: `c2_smoke` PASS, `mobile_check` PASS, `build/audit/sort_check.py` PASS (9 views, 90 tables, 504 sortable columns, 108 Table-view columns).
