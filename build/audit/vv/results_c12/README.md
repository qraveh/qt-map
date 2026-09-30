# results_c12 — the single suite on the build of 30 Sep 2026: the Hebrew edition complete, the register at 182 machines, the map's slot and edge changes of the fact-check

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c12` run on the dist of the 30 Sep content commit (English page sha256 e51de3aedb7f3603…).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 392 | 0 | 357 | every lens value, every architecture, every technology, every machine alone — one state fewer than results_c11: Bell-1 and RacQ became one register row |

The lit-set logic is unchanged. The data under it changed: the dual-rail architecture gained ic_multidie as an alternate in slot 9, the dec_rl edge now points to dec_mwpm, several machines' cells moved (Alice & Bob's manufacturing, D-Wave's dual-rail manufacturing, Boson 4's evidence) and one row merged — the suite confirms the page lights what the oracle derives from the new data.
