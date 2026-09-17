# Brief — adjudicate the smoke disagreements (SPEC step D.7 first pass; session C1, 16 Sep 2026)

Budget 8 minutes. Working directory /home/claude/qt-map/build/audit/vv. You may read everything here, build/map_js.py, build/build_html.py and data/graph.json. The written rules are RULES.md §1–§8 (from the editor's notes); RULES.md §Ambiguities lists the oracle's choices. results_smoke/*.jsonl holds the disagreements.

For each disagreement signature below decide, against the WRITTEN rule (not against the code), one of: ORACLE-FIX (the written rule supports the page; fix oracle.py and record the adjudication), PAGE-BUG (the written rule supports the oracle; record as a bug with a minimal reproducing state and the offending code location), DESIGN-GAP (the written rules do not decide; record the page's behaviour as the de-facto rule, flag for the editor, and make the oracle follow the page so the full run measures the rest). Signatures:
1. Non-family lens value with no isolate/focus: page dims every path line; oracle drew a line if ≥1 station passes. (Rule 3 says a family value keeps its family's lines — read it as: lines are hidden under a lens unless the lens is family.)
2. Isolate + lens: page still draws the isolated line.
3. Focused station lit even when it fails the lens or isolate (rule 2 says "the clicked station included").
4. Time lens: the page groups values into different bins than the oracle (7 stations missing at -6) — find the page's binning in map_js.py; is every station reachable by some bin?
5. f lens: the page has no "burst" button; under "bias" the page misses `cavity` and `g_bos` — is a lens value unreachable, and does a station with the attribute fail to light? (a station with an attribute value that no button can select = a reachable-value defect per SPEC §D.4).
6. Legend counts are fixed totals — the recorded rule says only the reading-marks keys are live; make the runner check live counts only for the marks keys and record the family totals as static by design.
7. Click timeouts in 9 of 14 random sequences — find the state/viewport where the click was intercepted (which element covers the station?); decide DRIVER-FIX (scroll/zoom before click, or click via the SVG datum) vs PAGE-BUG (a control overlays stations at that viewport — a real usability defect).
8. RU fallback static check: the build prints "0 RU fallbacks" itself; the page has no marker. Replace the check with: count RU strings identical to EN for keys that are not proper nouns/ids, list them, and mark the check "informational" unless a key is empty in RU.
Apply the ORACLE-FIX / DESIGN-GAP changes to oracle.py and runner.py (and the driver only for item 7 if DRIVER-FIX), append a numbered §Adjudications to RULES.md (signature → decision → rule cited → change made), re-run `python3 runner.py single --limit 40 --out results_smoke2/` and `python3 runner.py random --n 10 --out results_smoke2/`, and report.

Reply (≤ 150 words): the decision per signature (one line each), the smoke2 counts (compared / disagreements) and what remains as PAGE-BUG.
