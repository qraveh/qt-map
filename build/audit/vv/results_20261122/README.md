# results_20261122 — the single suite on the build of 22 Nov 2026: the seven technologies of 19 Nov (local writer job 20261122-1)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out results_20261122` run from `build/audit/vv/` on the dist of the commit that carries this folder (English page, Windows 11 / CPython 3.14.3, Playwright 1.64 Chromium — the local Code session's venv `C:\Users\raveh\.claude\tools\qt-atlas-playwright`; the log in its `runs/2026-11-22-20261122-1-pre-vv_single.log`).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 396 | 0 | ≈ 159 | every lens value, every architecture, every technology, every machine alone — 389 at results_20261109, and the seven technologies of 19 Nov 2026 (phonon, enc_zeeman, g_ddhf, ct_optical, dec_tn, fab_scd, fab_qphard), with the table mirror on every state |

**What changed.** No oracle or driver code: the graph gained seven alternates, 16 requires edges (three one-of groups, two soft), 10 alternatives edges and 3 conflict edges, and the oracle's states follow the graph. `test_oracle.py`'s place-list test pins the stations the 4 K lens lights; `ct_optical` joins that set (its photodiodes sit at 4 K), while `g_ddhf`'s control placement is room temperature only, as for the other gate mechanisms.

The Playwright suites on the same build: `c2_smoke` PASS, `mobile_check` PASS (logs `runs/2026-11-22-20261122-1-pre-*.log`).
