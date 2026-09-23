# results_c2h — metamorphic suite on the build of 23 Sep 2026 (evening), commit 0671118 (dist identical in d83c943 and after)

`VV_PAGE=dist/Quantum-Technology-Map-2026.09.html python3 build/audit/vv/runner.py metamorphic --n 200 --seed 7` — 200/200 states, 0 disagreements, 950 s.
Run because the zoom semantics changed (100 % = the fitted width; the driver's `zoom()` waits for the fit-relative value) and the controls bar starts collapsed (the driver expands it in `open()`).
The first attempt (before commit d83c943) flagged two states with a focus and a machine whose isolated path passed through the focused station: the page kept the focus and released the machine (adjudication 12); the check M2b expected both released and was corrected (runner.py, RULES.md).
The single suite (326 states, 0 disagreements) ran inside `release_check.py --smoke --vv` on the same build.
