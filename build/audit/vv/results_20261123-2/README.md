# results_20261123-2 — the single suite on the build of the table numbering (local writer job 20261123-2, 24 Nov 2026)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out results_20261123-2` run from `build/audit/vv/` on the dist of the commit that carries this folder (English page), with the Playwright venv's interpreter.

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 396 | 0 | ≈ 237 | every lens value, every architecture, every technology, every machine alone — the same 396 states as results_20261123 |

**What changed.** No oracle or driver code and no graph change: every table gains a number and a title (`build/tables.py`), the
references in the text become keys the build resolves, the Hebrew briefs gain their navigation words. The suite runs because the
change-impact matrix asks it for generator code; it shows the lens and lit-set behaviour unchanged.

The Playwright suites on the same build: `c2_smoke` PASS, `mobile_check` PASS, `build/audit/sort_check.py` PASS (9 views, 90
tables, 504 sortable columns, 108 Table-view columns); `build/audit/tablenum_check.py` 0 findings (30 report tables per language,
993 record pages).
