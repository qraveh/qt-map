# results_c8 — the single and machines suites on the build of 28 Sep 2026 (day): the roundtable's simplification (hub withdrawn, four edge types, one word "technology", references re-enumerated)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c8` on the dist of commit aaa63bf.

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 370 | 0 | 303 | every lens value, every architecture, every technology, every machine alone (111 technologies, 17 architectures, 160 machines — counted from the data) |
| machines | 1,080 | 0 | 1,504 | the machine term with isolate / focus / lens (run after the single suite's commit, on the same English page — sha256 1b925bfb…, unchanged by the later Russian-only fix) |

What changed in the map script since results_c7: the hub glyph, its legend key and card line are gone (the glyph legend has two keys, off-diagonal and empty slot), the alternates' family badges are half-tone squares, the labels say "technology" — none of it touches the lit sets, which the single suite confirms. The strip suite was not re-run (the strip's code is unchanged). The oracle self-test (`test_oracle.py`, 9 tests) passes — its former hub test now walks every technology shared by several architectures.
