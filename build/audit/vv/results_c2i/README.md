# results_c2i — the full V&V run on the build of 23 Sep 2026 (night): folds, the strip as a second interface (adjudication 13)

Page under test: `dist/Quantum-Technology-Map-2026.09.html` of commit 7ee5f82 (`VV_PAGE` set to dist; the map script and the styles are
byte-identical in 7664ac8 and in the results commit — those two change the strip block's heading markup and the audit files only).
Two lanes on the two-core sandbox, 21:23–23:09 UTC; the strip suite and every differential suite now compare the strip's five fields
(`pc_bright`, `pc_hi`, `pc_alt`, `pc_axis`, `pc_pressed`) and run the three strip invariants (`strip_checks`) on every record.

| suite | states | disagreements | seconds |
|---|---|---|---|
| single | 326 | 0 | 250 |
| pairs | 3,387 | 0 | 4,186 |
| multi | 1,330 | 0 | 2,698 |
| machines | 936 | 0 | 1,153 |
| metamorphic (`--n 200`, seed 1) | 200 | 0 | 2,367 (re-run; run 1: 1,591) |
| strip (`--n 300`, seed 1) | 300 | 0 violations | 2,168 |

Strip suite: S1 (map-driven state = strip-driven state) compared 161 of the 300 states — aff 18, time 22, mech 22, d 17, mod 34, f 21,
g 27 — and skipped 139 by rule (family 17 and status 25 have no axis; det 18, destr 23, mid 24, place 32 borrow an axis for the mark
but have no title or tick of their own); no state was skipped for a missing tick, so the axes cover every lens value the model draws.
S2 (axis titles), S3 (strip click = map click, ADJ-12 releases included) and S4 (hover transience both ways) ran on all 300.

What the first attempts found, before this recorded run (all in `STRIP_TEST_PLAN.md` §7 and RULES.md):
- page: `pcSetLens` returned early when the lens was already chosen, so the axis title did not clear the filter — fixed (7ee5f82);
- page: the (b) axis had no tick for the stations without a time value (`lens=time values=[none]` could not be pressed or mirrored) — the "—" tick added (7ee5f82);
- driver: `apply_state_via_strip` clicked a title that does not exist for det/destr/mid/place — skipped with the reason (7ee5f82);
- runner: metamorphic M2b took the machine to keep from the raw state, not from the effective selection — with focus g_mbq set last, the page had already
  released the Superion 256 (path ion_elec), then M2b isolated ion_elec and expected the machine to stay (`meta-1-141`). The check now starts
  from `oracle.effective()`; the first run is kept as `metamorphic-run1-harness-check.jsonl` (200 states, that one record) and the suite was re-run in full.

`SUMMARY.md` is the runner's own tally (`runner.py summary --out results_c2i`).
