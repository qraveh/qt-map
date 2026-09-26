# results_c4 — the four suites on the build of 26 Sep 2026 (evening): 17 paths, 110 stations, the register re-cut, 153 machines

Run on commit 0ad61e2's dist (sha256 50ddd6a4b3a92102…), `VV_PAGE=dist/Quantum-Technology-Map-2026.09.html python3 build/audit/vv/runner.py <suite>`:

| suite | states | disagreements / violations | seconds | note |
|---|---|---|---|---|
| single | 362 | 0 | 663 | every lens value, every path, every station, every machine alone (110 stations, 17 paths, 153 machines — counted from the data; the mech lens gained flux and homodyne in 0ad61e2 after a first pass found the two values unmappable on the page) |
| machines | 1,038 | 0 | 1,586 | the machine term with isolate / focus / lens; the cell values `none` / `undisclosed` contribute nothing (RULES §Machine term, 26 Sep 2026) |
| metamorphic | 200 (seed 7) | 0 | 2,019 | |
| strip | 300 | 0 violations | 2,551 | S1 compared 165 states, skipped 135 by rule (no strip control for the place / mid / destr / det lenses; no axis for status and family) |

The oracle self-test (`test_oracle.py`, counts from the graph) passes; `release_check.py --smoke` PASS on the same content (all items; the smoke suite counts stations, paths, machines, lens values and glyph keys from the data since 720ea13). The single and machines suites ran with four browsers in parallel (slow, 663 s for single); strip and metamorphic were re-run as a pair after that. The merge of main's og:image commits (dcaec89) changed only `head_meta()` and the colophon paragraph — the map script and data are those of 0ad61e2.
