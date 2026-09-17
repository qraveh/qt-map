# Lit-set rules as implemented by the oracle (SPEC D.1, session C1, 16 Sep 2026)

Sources: data/graph.json; editor's rules (programme notes 9–10 Sep 2026; project config line 35). Implementation files not read.

## State
`lens` (one of 14, or None), `values` (set; empty = no lens filter), `toggles` {requires, alternatives, conflicts}, `isolate` (path id | None), `focus` (station id | None). Reset = lens `family`, values ∅, all toggles off, isolate/focus None.

## Rules
1. **Lit stations** = I ∩ F ∩ L; each term = all 96 stations when unset.
   - I (isolate p) = every station listed in `paths[p].slots` (all layers).
   - F (focus s) = {s} ∪ stations of every path whose slots contain s ∪ neighbours of s over relation edges (either direction) whose type's toggle is on.
   - L (lens ℓ, values V≠∅) = stations whose value set for ℓ intersects V.
2. **Relation types**: toggle `requires` → edge type `requires`; `alternatives` → `replaces`; `conflicts` → `conflicts`. Only edges with both endpoints in `nodes` count (169). `defines` and `transfers` are never drawn by toggles.
3. **Edges drawn** = edges of toggled-on types; if any selection is active (V≠∅, isolate, or focus) only those with both endpoints lit. No toggle → no edges.
4. **Lines drawn**: path p is drawn iff (no isolate or p = isolate) ∧ (no focus or p passes through focus) ∧ lens term: family lens → `p.family ∈ V`; other lens → p has ≥ 1 station in L; no lens filter → pass.
5. Edge tuples are `(src, dst, type)` as stored.

## Lens → attribute mapping (reachable values)
| lens | attribute | values |
|---|---|---|
| family | `families` (list, multi) | ANNEAL ATOM DEFECT ION PHOTON SC SPIN TOPO |
| marks | `hub`→hub; `offdiag` non-empty→offdiag; id ∈ `empty_status`→empty (multi) | empty hub offdiag |
| aff | `aff` | 0.0 0.25 0.5 0.75 1.0 |
| time | `floor(b.t)`, else `floor(c.t)`; neither → none (log10 s decade) | -9 … -3, none |
| det | `b.det` | det her na |
| mech | `c.mech` (c null → none) | disp erasure fluor img none qcap s2c spd |
| destr | `c.destr` (c null → none) | False True none |
| mid | `c.mid` (c null → none) | False True none |
| d | `d` (mobility) | bus flying longrange none shared static transport |
| mod | `e.mod` | eo lf mw none opt |
| place | `e.place` | 4K RT mK none vac |
| f | `f` (list, multi; any match) | bias burst coherent erasure gauss leak loss pauli unknown |
| g | `g` (fab) | 3d cmos diamond mbe mems none optics pic sclitho stm |
| status | `status` | D E T X |

## Machine term (C2, 17 Sep 2026)
`machine` (a register machine id from `data/machines.json`, or None) is one more term of the same intersection, never a new mechanism (C2 brief, editor's rule). **M (machine m)** = the machine's real (non-gap) stations on every layer, primary and alternate, i.e. every `layers[*][*].node` that is a graph node (gap nodes `∅…` are not graph nodes and contribute nothing). Lit stations = I ∩ F ∩ L ∩ M; the focused station stays lit (ADJ-3). Lines: the machine keeps exactly its own `map_path` line, like an isolate — lines = (lines by rules 4/ADJ-1/ADJ-2) ∩ {map_path}; a machine counts as a selection for ADJ-1 (a non-family lens value does not remove the line the machine keeps) and for edges (rule 3: edges only between lit stations). Stations the machine uses only as an alternate are marked `altuse` on the page while lit (readout only, not a lit-set term). The card shown is the focused station's if any, else the machine's; reset clears the machine. Since C2 isolating a path no longer clears the focused station (driver state model updated).

## Metamorphic checks implemented
M1 adding a lens value never shrinks lit stations; M2 isolate→clear is identity; M3 double toggle is identity; M3b a toggle changes stations/lines only when a focus is set; M4 union over single family values = unfiltered stations (minus path-less stations) and lines; M5 selecting all values of a lens = unfiltered minus stations with no value for it; I1 no edge of an untoggled type.

## Ambiguities (adjudication items)
1. **Clicked station vs lens/isolate.** Rule 2 says "the clicked station included"; rule 1 is a strict intersection. Choice: strict — a focused station that fails the lens or isolate term is unlit, and its edges are not drawn.
2. **Lines under a non-family lens.** Unwritten. Choice: a line is drawn iff it has ≥ 1 lens-passing station (and passes isolate/focus). Alternatives: always drawn, or only if all its stations pass.
3. **Rule 3 vs isolate/focus.** Choice: the family-lens exception only replaces the lens term for lines; isolate and focus still intersect (an isolated SC path under lens ION is not drawn).
4. **"alternatives" = `replaces` edges.** No edge type is named "alternatives"; mapped to `replaces` (within-layer, 39 edges).
5. **Neighbour direction.** Focus neighbours taken over both directions of `requires`/`replaces`/`conflicts`.
6. **Focus with toggles off lights neighbours?** Rule 4: no; only path stations. So a toggle changes F (and hence stations) only under focus.
7. **Edges with no selection**: all edges of the toggled type are drawn, including those touching path-less `dec_cryo`.
8. **Isolated path's lines/edges**: isolate lights exactly one line; focus lights exactly the focused station's paths' lines (lines do not follow toggled neighbours).
9. **`transfers` edges** (4 station–station, 82 station–path) are not relation edges and never drawn by toggles.
10. **Path-less station `dec_cryo`** (status X, on no path) is lit by default but no family value reaches it, so rule 8's "union over family values = unfiltered set" fails literally; M4 exempts it. Also focusing it lights only itself (+ toggled neighbours) and no lines.
11. **marks "empty slot"**: `empty_slots` are slots with no station and cannot be lit; mapped to the 5 stations in `empty_status` (= status X). Stations with no mark never pass the marks lens (no "none" value).
12. **time lens** is continuous (ramp); binned to log10 decades; readout-only nodes use `c.t`; nodes with both use `b.t`; no time → `none` value selectable. Binning of the implementation may differ.
13. **destr/mid for non-readout nodes** (c null, 75): value `none`, selectable. The implementation may treat them as not colourable/non-selectable.
14. **Multi-valued lenses** (family, marks, f): a station passes if any of its values is selected (not all).
15. **Isolate term = slot stations of all layers**, incl. multiple alternatives per slot; empty slots contribute nothing.
16. **Lens set but values empty** is identical to no lens (lens choice alone changes colour, not lit set).
17. **Focus + isolate on a path not through focus** yields empty lit set and no lines (no fallback).

## Adjudications (SPEC D.7 first pass, session C1, 16 Sep 2026)
Source of disagreements: results_smoke/*.jsonl (baseline-8106b9e.html). Decisions are against the written rules; page code is cited only to state the de-facto rule or the bug location.

1. **Non-family lens value, no isolate/focus → page dims every line; oracle drew lines with ≥1 lens-passing station.** DESIGN-GAP. Rule cited: editor rule 3 ("a family value also keeps that family's lines") only speaks of family values; lines under other lenses are unwritten (Ambiguity 2). De-facto rule (map_js.py `dimming()`, `pathSel.classed('dim', d=>keepP?!keepP.has(d.id):lf)`): with no isolate/focus, a family value keeps that family's lines, any other lens value hides all lines. Change: oracle.py `expected()` lines block. Flag for the editor.
2. **Isolate + non-family lens → page still draws the isolated line.** DESIGN-GAP. Rule cited: none decides lines under isolate+lens (Ambiguity 3 covered only the family case). De-facto rule (map_js.py `litSets()`): isolate/focus fix the lines; only a family value narrows them further; a non-family lens value never removes a line that isolate/focus keep. Change: oracle.py lines block (`elif not (iso or foc): continue`). Flag for the editor.
3. **Focused station lit even when it fails the lens or isolate term.** ORACLE-FIX. Rule cited: editor rule 2, "the clicked station included" (overrides the strict reading of Ambiguity 1). Change: oracle.py `lit.add(foc)` after the intersection; edges follow (a focused station's toggled edges to lit stations are drawn); M4/M5 metamorphic checks exempt the focused station.
4. **Time lens binning.** DESIGN-GAP. Rule cited: the time lens is a continuous ramp; the notes give no bins (Ambiguity 12). De-facto rule (map_js.py `TBINS`, `timeBin()` l.149–150): nearest of 7 bin centres −8.5…−2.5 log10 s (≤3 ns, ~30 ns, ~300 ns, ~3 µs, ~30 µs, ~300 µs, ≥3 ms), ties to the lower bin, clamped at both ends; `b.t` before `c.t`; no time → `none`. The 7 stations "missing at −6" have t exactly −6.0 and tie into the ~300 ns bin. Every station is reachable: nearest-bin is total and every non-empty bin has a button (`lensItems(...).filter(n>0)` only drops empty bins). Change: oracle.py `_time_bucket()` (value = bin index − 9). Flag for the editor (integer decades land in the faster bin).
5. **f lens: no `burst` button; `bias` misses `cavity`, `g_bos`.** PAGE-BUG (reachable-value defect, SPEC §D.4). Rule cited: (f) is a list attribute; a station carrying a value must be selectable by it (Ambiguity 14, any match). Page code: map_js.py l.146 `lensValue(n,'f')` returns `n.f[0]` only, used by `nodeMatchesFilter()` (l.164) and the legend counts in `lensItems()` (l.158); l.176 drops zero-count items, so `burst` (only in `transmon.f[1..]`) has no button. Minimal reproducing state: reset → lens `f` → click `bias`: lit = {enc_cat, code_bosonic, g_catcnot}; expected also `cavity` (f=[loss,bias]) and `g_bos` (f=[erasure,bias,pauli]). Unreachable value: `burst` (transmon). Oracle unchanged.
6. **Legend counts are fixed totals.** Recorded rule: only the reading-marks keys are live counts; the family (and every other lens) legend shows static totals by design. Change: runner.py random suite checks live counts only when lens = `marks` (`legend-count-marks-not-live`) and otherwise checks the count equals the static total (`legend-static-total-mismatch`; f totals will still differ because of item 5).
7. **Click timeouts in random sequences.** PAGE-BUG (not DRIVER-FIX). Reproduction: viewport 1024×900 (also 600×800, 400×800), focus any station (e.g. `g_catcnot`), then click `#zoomlvl`, `#tg-reset`, a `#pathchips` chip or another station's `rect.box`: the inspector `aside#insp` (position: fixed, ~55–60 % of the viewport height from the bottom) intercepts pointer events, and the sticky `#mobilebar` (top 49 px) intercepts when Playwright scrolls the target to the top. The bar controls and stations under the fixed inspector cannot be clicked until the focus is cleared (Escape / background click). Locations: build/page_css.py l.437 `.insp{position:fixed;left:0;right:0;bottom:0…}` (narrow media block; desktop rule l.220 is also fixed) and l.393 `.mobilebar{position:sticky;top:0;z-index:55}`; map_js.py `select()` opens the inspector. The "action" field in those records is one step stale (the failing click is the next action). Driver unchanged.
8. **RU fallback static check.** Replaced (runner.py `run_static`, key `ru-fallbacks`): lists bilingual strings whose RU text is identical to EN (`T('en','ru')` calls in scripts + `{en,ru}` objects in JSON data blocks), skipping proper nouns/ids; informational (agree) unless an RU value is empty where EN is not.
9. **Marks legend counts.** Recorded rule: the marks legend counts are totals of the lens value over the graph, not of the lit set (observed 17 Sep on the fixed build; the editor's "live keys" wording is ambiguous) — runner check `legend-count-marks-not-live` downgraded to informational (recorded in `informational`, not a disagreement).
10. **17 Sep: the reading-marks lens was removed at the editor's decision; the glyphs and static legend keys remain.** Change: oracle.py drops `marks` from `LENSES`/`lens_values`; runner.py drops it from the `single`/`pairs`/`multi` generation and from the marks-legend informational check (the keys are static, not clickable, with totals as their counts).
