# Test plan and methodology — the strip as a second interface to the map (ADJ-13, 23 Sep 2026)

## 1. Object under test
The parallel-coordinates strip below the map ("Technologies across the seven attributes"): 96 polylines (one per technology,
`path.pcline[data-node]`), seven axes (`g.pc-axis[data-axis]`) with a title (`text.t[data-lens]`) and ticks
(`text.tick[data-lens][data-lv]`), a label line. Its contract is adjudication 13 of RULES.md: the strip *mirrors* the map's
lit set, focus, machine alternate-use, lens colouring, lens and filter marks; it *controls* the map through the same three
gestures the map already has (lens, filter value, focus) and lights the map on hover; hover is transient.

## 2. What can go wrong (risk analysis, from the map's logic)
The map's state has six terms — lens, filter values, edge toggles, isolated path, focused station, chosen machine — and
three release rules between the last three (ADJ-12). The strip can fail in four ways: (R1) it shows a lit set other than the
map's (a term missed, as before this work: isolate and machine were never reflected); (R2) a strip gesture produces a state
that the same gesture on the map would not (a different release, a stale filter, a lens switched without clearing values);
(R3) a visual attribute disagrees with the station's (colour, dashing, the value shown for a multi-value station under a
filter); (R4) hover leaves a residue or misses the other side. Each risk has a test class below.

## 3. Methodology
Oracle-based differential testing (the existing SPEC D method): the oracle (`oracle.py`) computes from the graph and a state
what the page must show; the driver (`driver.py`) applies the state through the page's controls and reads the DOM; the runner
records every disagreement. The strip is folded into this method rather than tested apart:
- **Mirror (R1, R3)** — `expected()` now returns `pc_bright` (= the lit set), `pc_hi` (= the effective focus), `pc_alt`
  (= the machine's alternate-only stations that are lit), `pc_axis` (= the axis of the lens), `pc_pressed` (= the filter's
  ticks, on the lens's own axis only). `read()` returns the strip's classes, colours and values. `diff()` compares all five in
  **every record of every differential suite** (single 326, pairs 3,387, multi 1,358, machines 936), so the mirror is verified
  over the whole state space those suites cover, not over a sample. `strip_checks()` adds three page-internal invariants per
  record: the value a line shows is one its station carries (the lit one under a filter; 'multi' for a multi-family station
  under the family lens); under a non-family lens the line's stroke equals the station's outline colour; no `hover` class is
  present when the pointer is off the map (reads move the pointer away first).
- **Control equivalence (R2)** — suite `strip`, S1: a random state is applied from the map's controls and read; the page is
  reset; the same state is applied from the strip where the strip has a control (lens by its axis title, values by its ticks,
  focus by its line; isolate, machine and toggles by the map, which the strip does not control) and read again; the two reads
  (stations, lines, edges, the five pc fields, the shown values, the page's control state) must be identical. States whose
  lens has no axis of its own (family, status) or only borrows one for the mark (destructive, mid-circuit, deterministic,
  placement) are recorded as skipped with the reason. S2: every axis title, clicked from a random state, yields its lens with
  no filter and the axis mark — also when that lens is already chosen with a filter (the title clears it). S3: for
  a random state and a random station, `focus` from the map and `pc_click` from the strip give identical full reads — this
  includes the ADJ-12 releases, since the strip calls the map's own `select`. 
- **Hover (R4)** — S4: from a random state, hovering a random line lights exactly that line and that station; hovering the
  station lights exactly that line; leaving restores a read identical to the one before.
- **Metamorphic** — the existing suite (M1–M4) runs on the new build unchanged: the strip refresh is on the same code path as
  the map's dimming, so any identity violated on the map would also appear in the pc fields of the differential records.
- **Smoke** — `c2_smoke.strip()`: the visual contract on a real viewport (axes above the lines so the ticks are clickable;
  (e) rows complete; a tick click presses the tick and the legend value; the strip inside full screen and with the bar
  collapsed; language switch relabels the axes).

## 4. Coverage
- Mirror: all states of single (every lens value alone, every toggle, every isolate, every focus), pairs (every pair of terms),
  multi (triples and more), machines (every machine × isolate/focus) — the same enumeration the map itself is verified with.
- Control: 300 random states (seed 1) for S1–S4; the S1 skip rate is reported (lenses without an axis).
- The seven axes: every tick value of every axis is exercised by S1 over the random states (values are drawn from the model's
  lens values, which the ticks must cover: a missing tick is a recorded skip, so a stale axis list shows up in the counts).

## 5. Pass criteria
0 disagreements in every differential suite (pc fields included), 0 violations in `strip`, metamorphic 0, smoke PASS,
release check PASS. A disagreement is a defect or an adjudication to write, never a tolerance.

## 6. How to run
    export VV_PAGE=dist/Quantum-Technology-Map-2026.09.html
    python3 build/audit/vv/runner.py single      --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py pairs       --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py multi       --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py machines    --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py metamorphic --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py strip --n 300 --out build/audit/vv/results_c2i
    python3 build/audit/vv/runner.py summary     --out build/audit/vv/results_c2i
    python3 build/audit/release_check.py --smoke --vv

## 7. What the first run found (23 Sep 2026)
The first full run against ebc8883 stopped after 302 single and 31 strip records with six disagreements of three kinds, each
fixed before the recorded run (results_c2i):
- **Page (rule violated).** `pcSetLens` returned early when the lens was already chosen, so clicking the title of the active axis
  left the filter in place; S2 from a state with that lens and a filter caught it. Now the title clears the filter — the lens
  with no filter, as the rule reads; the lens select cannot express a re-selection, the title can.
- **Page (mirror incomplete).** The (b) axis had the seven time bins but no row for the stations without a time value, while the
  time legend has "no time (code, decoder, fab)"; a filter by that value was neither pressed on the strip nor selectable from
  it (single, `lens=time values=[none]`, expected pressed tick missing). The axis now has a "—" tick at the height where those
  lines sit.
- **Driver.** `apply_state_via_strip` clicked the title of a lens that only borrows an axis (det, destr, mid, place — no title
  of its own), a null-element error in four records. Such states are skipped with the reason, as the plan says for lenses
  without an axis.
