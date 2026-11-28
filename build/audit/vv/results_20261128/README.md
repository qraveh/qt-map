# results_20261128 — the single suite on the build of review R2 (cloud thread, ticket 20261128-2, 28 Nov 2026)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out results_20261128` run from `build/audit/vv/` on the dist of the commit that carries this folder (English page), with a Playwright 1.63 venv (Chromium 158) in the cloud (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 398 | 0 | ≈ 232 | every lens value, every architecture, every technology, every machine alone — two states more than results_20261127 (the two new machines) |

**What changed.** No oracle, driver or generator code: the register gained two machines (oxford-ion-network, ethz-surface41) with their station rows, and one station moved (umd-duke-ion's decoder from dec_mwpm to the gap ∅G-lut), so the lit sets of the machine and technology states change. The suite runs because the change-impact matrix asks it when the stations change. The oracle's self-test (`test_oracle.py`): 9 tests OK.

`single.console.txt` holds 144 lines `Failed to load resource: net::ERR_FILE_NOT_FOUND`: the pictures, which the cloud clone does not have (`dist/media/` is filled at deploy, `build/DEPLOY.md`), as in results_20261127.

Skipped: `c2_smoke` and `mobile_check` — no UI code and no page chrome changed.
