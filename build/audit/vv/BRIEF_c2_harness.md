# Brief — extend the V&V harness for the C2 build (session C2, 17 Sep 2026)

Budget 10 minutes. Working directory /home/claude/qt-map/build/audit/vv. Target page for all runs: `VV_PAGE=/home/claude/qt-map/dist/Quantum-Technology-Map-2026.09.html` (the C2 build: defects 1/2/4 fixed, a Machine selector added). Read RULES.md §Adjudications, DRIVER.md, and the C2 change list in `../C2_BRIEF_ui.md`.

## 1. Driver state model (driver.py) — the page changed by design
- Isolating a path no longer clears the focused station (RULES.md: the three terms narrow each other). Update the driver's `state()` bookkeeping so `isolate()` keeps `focus`; the `driver-state-drift` signature must disappear.
- New control: `select_machine(machine_id|None)` — the `<select id="machine">` in the map bar (option values are machine ids; optgroups per family); `clear_machine()`; `state()` gains `"machine"`. `read()` gains `altuse` (set of station ids carrying class `altuse`) and `machine_card` (text of the inspector when a machine card is shown).
- Fit idempotence check: the page scrolls to align the bar when fitting; wait for the scroll to settle (poll `scrollY`/`scrollLeft` until unchanged for 2 frames, max 1 s) before reading the transform in both applications; if fit_width/fit_height still differ after settling, keep the violation (it is then real).

## 2. Oracle (oracle.py, RULES.md)
- `state["machine"]`: when set, the machine term = the machine's non-gap nodes (primary and alternate, all layers) from `/home/claude/qt-map/data/machines.json`; `expected()` intersects `stations` with it and `lines` with `{map_path}`; the focused station stays lit (existing rule). Load machines.json in `load()` (`Model.machines`). Add to RULES.md a §Machine term paragraph and, in §Adjudications, item 9: "marks legend counts are totals of the lens value over the graph, not of the lit set (observed 17 Sep on the fixed build; the editor's 'live keys' wording is ambiguous) — runner check downgraded to informational".
- `all_single_states` gains every machine alone (136 states); `random_state` may set a machine with probability 0.3.

## 3. Runner (runner.py)
- New suite `machines`: every machine alone; every machine × each toggle on; every machine × isolate = its own path and × one other path (expect the intersection); 60 sampled machine × lens-value pairs and 60 sampled machine × focus pairs (seeded). Compare lit sets, lines, edges with the oracle; also assert: the machine card is shown (unless a station is focused), the bar summary contains the machine name, `altuse` ⊆ lit stations, and after `reset()` the select is empty and `altuse` is empty.
- The `legend-count-marks-not-live` check becomes informational (recorded, not a disagreement).
- Random actions gain `select_machine` / `clear_machine`.

## 4. Runs (start them, do not wait): from this folder, with `VV_PAGE` set, `--out results_c2/`: `machines`, then `pairs` (resumable) and `multi` in the background with nohup (logs under logs/). `single` and `metamorphic` on this build already ran/are running — do not restart them.
Reply (≤ 120 words): driver/oracle/runner changes, the `machines` suite result (states, disagreements, signatures), whether the fit checks still fail after settling, and what is running in the background.
