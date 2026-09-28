# results_c7 — the single suite on the build of 28 Sep 2026 (night): dec_cryo placed on the superconducting architecture; the fifteen new stations labelled; the architecture card lists its machines

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c7`

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 370 | 0 | 272 | every lens value, architecture, station and machine alone; `sc` now carries `dec_cryo` as an alternate in the decoder slot (the isolate lights it) |

The machines and strip suites of results_c6 stand: the machine cells and the strip rules are untouched by these three changes (a slot added to one architecture, fifteen short labels, a card block with links). `release_check.py --smoke` PASS on the same tree.
