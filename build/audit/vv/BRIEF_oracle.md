# Brief — independent oracle for the Map's lit-set rules (SPEC step D.1; session C1, 16 Sep 2026)

Budget 8 minutes. Working directory /home/claude/qt-map. You must NOT open build/map_js.py, build/build_html.py, build/brief_js.py or dist/ — the oracle is independent of the implementation by design. Sources you may read: data/graph.json (structure: layers, nodes[id, layer, en, status, paths, families, hub, offdiag, b/c/d/e/f/g attribute blocks…], paths[id, family, slots…], edges[u, v, type…]), CHANGELOG.md, README.md, and the editor's rule documents /home/claude/work/QT-Map/00_admin/qt-map-project-config.md, /home/claude/work/QT-Map/00_admin/HANDOFF.md, /home/claude/work/QT-Map/00_admin/HANDOFF_20260909_beta_rev15_cloud.md.

The editor's rules as recorded in the programme notes (authoritative wording, 9–10 Sep 2026):
1. One lit set governs stations, path lines and relation edges: lit = isolate ∩ focus ∩ lens, where each term is "all stations" when that control is unset.
2. The edge toggles (requires / alternatives / conflicts) alone decide which relation types are drawn; a selection (lens filter and/or isolated path and/or clicked station) only narrows the drawn relations to those among lit stations, the clicked station included. No toggle → no edges, even for the clicked station.
3. A family-lens value keeps that family's path lines visible (lines of paths of the selected families are drawn even if the lens would otherwise hide them).
4. A clicked (focused) station lights its paths in full — every station on every path through it — plus its graph neighbours, but the neighbours only through relation types whose toggle is on.
5. Lens values multi-select (Ctrl/⌘/Shift-click): a station passes the lens term if its value for that lens is in the selected set; an empty selection = no lens filter. Lenses (14): family, marks (reading marks: hub · off-diagonal · empty slot), aff, time, det, mech, destr, mid, d, mod, place, f, g, status — each maps to a node attribute in graph.json (find the mapping from the data; document it).
6. Path isolation (14 paths): the isolate term = the stations on that path's slots.
7. Reset is global: family lens with no value, no edges, nothing isolated or focused.
8. Metamorphic expectations: adding a value to a lens never lights fewer stations of that lens; isolate then clear returns the previous set; toggling twice is identity; the union over all family-lens values equals the unfiltered set.

## Deliverables (all under build/audit/vv/)
- `RULES.md`: the rules restated precisely as you implement them, with the lens → attribute mapping and value sets, and a numbered §Ambiguities listing every point the written rules leave open and the choice you made (these become adjudication items for the differential run; do not guess silently).
- `oracle.py`: pure Python, stdlib only. `load(graph_path) -> Model`; `expected(model, state) -> {"stations": set[str], "lines": set[path_id], "edges": set[tuple(u, v, type)]}` where `state = {"lens": str|None, "values": set, "toggles": {"requires": bool, "alternatives": bool, "conflicts": bool}, "isolate": path_id|None, "focus": node_id|None}`; `lens_values(model, lens) -> list` (the reachable values of each lens); `all_single_states(model)` generator (every lens × value, every toggle alone, every isolation, every station focus); `random_state(model, rng)`; `metamorphic_checks(model, rng, n) -> list[str]` (violations, expected empty). Deterministic outputs (sorted where it matters).
- `test_oracle.py`: sanity tests on graph.json (default state lights all 96 stations and 14 lines and no edges; each isolation lights exactly the path's stations; focus on a hub station lights ≥ its paths' stations; metamorphic checks pass for 200 random states). Run it.

Reply (≤ 120 words): what the oracle covers, the ambiguity count and the three most consequential ones, test results.
