# C2 brief F — control placement as a list; SCE at 4 K; "in-vacuum" is not a temperature (editor's decision of 17 Sep 2026)

Budget 10 minutes. Working directory /home/claude/qt-map (branch c2-machines-2026-09-17). You own `data/graph_data.py`, `build/map_js.py`, `build/make_sections.py`, `build/briefs.py` (only if it prints `e.place`), `build/build_html.py` (only if it prints `e.place`), `build/audit/vv/oracle.py`, `build/audit/vv/RULES.md`, `build/audit/c2_smoke.py`, `build/audit/vv/test_oracle.py`. Nothing else. Then rebuild (`python3 build/build.py` regenerates data/graph.json and the report sections).

## Data model
`e.place` becomes a **list** for every node (like `f`), first entry = primary stage. Vocabulary `PLACE` in graph_data.py: keep `RT`, `4K`, `mK`, `none`; **remove `vac`** ("in-vacuum integrated" is a location, not a temperature). The lens label already reads "Control: placement (temperature stage)".

## Node edits (graph_data.py `N(...)` rows ~246–269; the 12th positional argument is place)
- `ct_sfq`: name EN "SCE (SFQ) digital control (4 K or millikelvin)", RU "Цифровое управление на SCE (SFQ) (4 K или милликельвины)"; place `["mK","4K"]`; description EN: "Single-flux-quantum (superconducting-electronics) digital circuits either at the mK stage — pulse trains drive qubits from a flip-chip (1Q > 99 %, 99.9 % peak; nW/qubit claimed) — or at the 4 K stage as an in-fridge controller (DigiQ, 2022: the largest designs fit the few-watt budget of the 4 K stage); the same circuit family loads D-Wave's on-chip flux DACs." RU accordingly. Add to its `defines`/sources list (whatever field carries citations for this node — inspect the existing row) the DigiQ reference: "DigiQ: A Scalable Digital Controller for Quantum Computers Using SFQ Logic, HPCA 2022, https://arxiv.org/abs/2202.01407".
- `ct_cryocmos`: place `["4K","mK"]` (its own description already says "4 K (or 7 mK)").
- `ct_ionlaser`: place `["RT"]`; description EN prepend "In-vacuum integrated photonics at room temperature (cryogenic traps at 4–10 K exist): " to the existing text; RU accordingly.
- Every other node: place `[<current value>]`.

## Consumers to make list-aware
- `map_js.py`: `lensValue(n,'place')` → first entry; `lensValues(n,'place')` → the list (the existing f logic); `lensColor` colours by the matched selected value for `place` as for `f`; `lensItems` counts by membership; the station card's "(e) control" row prints the modality and every stage joined by " / ".
- `make_sections.py::coordE` prints every stage joined by " / "; §7.2's (e) column follows.
- `briefs.py` / `build_html.py`: if either prints `e.place`, join the list; otherwise leave.
- `oracle.py`: `place` lens membership over the list (as `f`); `lens_values` from the data; `RULES.md`: one line under §Machine term or a new §Place: "place is list-valued since 17 Sep 2026 (ct_sfq mK+4K, ct_cryocmos 4K+mK); 'vac' removed".
- `test_oracle.py` and `c2_smoke.py`: place lens value "4 K stage" lights `ct_cryocmos`, `ct_sfq` and `ro_spd`; "millikelvin stage" lights `ct_sfq` too; no value "vac" anywhere in the DOM; the ct_sfq card shows "4 K stage / millikelvin stage".

## Checks
`python3 build/build.py` twice → identical sha256; `git diff --stat`; `grep -c '"vac"' data/graph.json` → 0; smoke PASS; test_oracle OK. Reply (≤ 100 words): what changed per file, the counts of stations per place value after the change, smoke/oracle results, dist delta.
