# results_c8 — the single suite on the build of 28 Sep 2026 (day): the roundtable's simplification (hub withdrawn, four edge types, one word "technology", references re-enumerated)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c8` on the dist of commit aaa63bf.

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 370 | 0 | 303 | every lens value, every architecture, every technology, every machine alone (111 technologies, 17 architectures, 160 machines — counted from the data) |

What changed in the map script since results_c7: the hub glyph, its legend key and card line are gone (the glyph legend has two keys, off-diagonal and empty slot), the alternates' family badges are half-tone squares, the labels say "technology" — none of it touches the lit sets, which the single suite confirms. The machines suite (1,080 states, ≈ 26 min) is run after this commit and its result recorded in the hand-off note; the strip suite was not re-run (the strip's code is unchanged). The oracle self-test (`test_oracle.py`, 9 tests) passes — its former hub test now walks every technology shared by several architectures.
