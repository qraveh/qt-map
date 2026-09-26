# results_c5 — three suites on the build of 26 Sep 2026 (night): 17 paths with short names, 111 stations, 160 machines, the §8.3 narratives

Run on commit 9480b8b's dist (9,975,578 bytes), `VV_PAGE=<abs path>/dist/Quantum-Technology-Map-2026.09.html python3 build/audit/vv/runner.py <suite> --out build/audit/vv/results_c5`:

| suite | states | disagreements / violations | seconds | note |
|---|---|---|---|---|
| single | 370 | 0 | 342 | every lens value, every path, every station, every machine alone (111 stations, 17 paths, 160 machines — counted from the data) |
| machines | 1,080 | 0 | 1,581 | the machine term with isolate / focus / lens; cell values `none` / `undisclosed` contribute nothing |
| strip | 300 | 0 violations | 2,494 | S1 compared 161 states, skipped 139 by rule (no strip control for the place / mid / destr / det lenses; no axis for status and family) |

The oracle self-test (`test_oracle.py`, 9 tests, counts from the graph) passes; `release_check.py --smoke` PASS on the same content. What changed in the map script since results_c4: the path chips show `p.short` with the full name as title, and self-labelled links get their href at load (`a.u`); the strip suite therefore ran again. The metamorphic suite (200 states, seed 7, 0 disagreements on results_c4) was not re-run: the graph changes (one node, six slot additions, five edges) do not touch the metamorphic relations, and the suites above cover the new node and the new machines directly. Single and machines ran in sequence, strip in parallel with them.
