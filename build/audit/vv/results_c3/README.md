# results_c3 — the strip and single suites on the build of 26 Sep 2026 (permanent reference numbers; §9 Monitor entry; upward scroll escape; the report self-reviewed)

`VV_PAGE=dist/Quantum-Technology-Map-2026.09.html python3 build/audit/vv/runner.py strip --n 300` on commit 0eaf513's dist (sha256
942f3b9d933ecfd3…, identical in the results commit — the ACCEPTANCE block of `HANDOFF_20260926_c3_rev3_cloud.md` names it): 300 random states,
0 violations, 1,496 s. S1 compared 161 states, skipped 139 by rule (the strip has no control for the place/mid/destr/det lenses;
no axis for the status and family lenses). The V&V single suite on the same build: 326 states, 0 disagreements, 153 s
(`single-release.progress.log`). Run because the map script changed in one block only — the scroll escape gained its upward branch
(`20201ae`); the selection logic is untouched since 9fc22a2 (full run: results_c2i; the strip after the mode changes: results_c2j). Earlier runs of both suites the same night on 448ebc7 and e7fc6b4 (the same map script; the report text before the prose-number fixes and before the permanent reference numbers) gave the same result: 300/0 and 326/0.
`release_check.py --smoke` on the same build: all 31 items pass once the tree is clean (refs_check "problems by class: none";
brief_refs --check OK; smoke incl. `stripmodes()` with the new upward check).
