# results_20261127 — the single suite on the build of the page's Changelog (cloud thread, ticket 20261127-2, 27 Nov 2026)

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python runner.py single --out results_20261127` run from `build/audit/vv/` on the dist of the commit that carries this folder (English page), with a Playwright 1.63 venv (Chromium 158) in the cloud.

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 396 | 0 | ≈ 304 | every lens value, every architecture, every technology, every machine alone — the same 396 states as results_20261123-2 |

**What changed.** No oracle or driver code and no graph change: the colophon ends with a Changelog in each language and the contents
gain its entry (`build/editions.py: changelog_html`, `build/build_html.py`, `build/page_css.py`). The suite runs because the
change-impact matrix asks it for generator code; it shows the lens and lit-set behaviour unchanged. The oracle's self-test
(`test_oracle.py`): 9 tests OK.

`single.console.txt` holds 144 lines `Failed to load resource: net::ERR_FILE_NOT_FOUND`: the pictures, which the cloud clone does not
have (`dist/media/` is filled at deploy, `build/DEPLOY.md`), as in results_20261009.

The Playwright suites on the same build: `c2_smoke` PASS (308 ok, among them the contents column beside the text with no horizontal scroll);
`mobile_check` 68 ok, and its three picture assertions fail in the cloud for the same reason, as always. The Changelog itself was
checked on 1400×1000 and 390×844 in each language: visible, 19 lines, the last entry of the contents, no horizontal scroll, no
console error, and each colophon in its own script only.
