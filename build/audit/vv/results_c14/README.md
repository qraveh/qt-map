# results_c14 — the single suite on the build of 2 Oct 2026: the frontier counts benchmarked devices, decoder modes from the register field, H6 reads ranges

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c14` run on the dist of the commit that carries this folder (English page, cloud Linux / CPython 3.11, Playwright Chromium).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 392 | 0 | 362 | every lens value, every architecture, every technology, every machine alone — as results_c13 (182 machines) |

The commit changes the machines chapter's rules (gate-capable vs benchmarked, the decoder classes, the H6 parser), the cards' profile block and the page chrome (the Find hint, the translated masthead); the graph and the lit-set logic did not change, so the oracle's expectations are those of results_c13, and the run confirms the map's state logic is untouched. The Playwright suites: `c2_smoke` PASS (exit 0); `mobile_check` PASS with the five thumbnails of the Transmon and Trapped-ion cards placed under `dist/media/` for the run (the thumbnails live on the editor's machine; without them the card's picture figure removes itself on the image's error event and three picture checks fail — an environment condition, not a defect).
