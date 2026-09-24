# results_c2j — the strip suite on the build of 24 Sep 2026 (brief references validated; scroll escape; strip modes; typography; page size)

`VV_PAGE=dist/Quantum-Technology-Map-2026.09.html python3 build/audit/vv/runner.py strip --n 300` on commit 1db5ead's dist (sha256
4c585ade28c380cf…, identical in the results commit): 300 random states, 0 violations, 1,765 s. S1 compared 161 states, skipped 139 by rule.
The V&V single suite (326 states, 0 disagreements) ran inside `release_check.py --smoke --vv` on the same build (log kept here as
single-release.progress.log). Run because the map script changed around the strip: the zoom block exposes `fitTo(avail)`, the full-screen
block defers to the map-and-strip mode, two blocks were added (strip modes, scroll escape); the selection logic is untouched since 9fc22a2
(full run: results_c2i).
