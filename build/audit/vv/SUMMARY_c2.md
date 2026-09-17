# V&V runner summary

Generated 2026-09-17 11:20:40 from results_c2/*.jsonl and progress.log.

| suite | total | agree | disagree |
|---|---|---|---|
| machines | 936 | 936 | 0 |
| metamorphic | 200 | 200 | 0 |
| multi | 1358 | 1358 | 0 |
| pairs | 3357 | 3357 | 0 |
| random | 40 | 21 | 19 |
| single | 194 | 194 | 0 |

## random: 4 distinct disagreement signatures

- **driver-state-drift** [-] x15 — example: `{"key": "seq-7-1", "check": "driver-state-drift", "driver": {"focus": null, "isolate": "atom_ae", "lens": "d", "toggles": "c", "values": []}, "page": {"focus": "ic_cryolink", "isolate": "atom_ae", "lens": "d", "toggles": {"alternatives": false, "conflicts": true, "requires": false}, "values": []}, "step": 19}`
- **legend-count-marks-not-live:marks** [-] x5 — example: `{"key": "seq-7-5", "check": "legend-count-marks-not-live", "count": 19, "lens": "marks", "lit": 0, "step": 12, "total": 19, "value": "offd"}`
- **fit_width-not-idempotent** [-] x2 — example: `{"key": "seq-7-7", "a": {"h": "465", "sl": 0, "st": 0, "tr": null, "vb": "0 0 1490 1212", "w": "572", "z": "38%"}, "b": {"h": "465", "sl": 0, "st": 165, "tr": null, "vb": "0 0 1490 1212", "w": "572", "z": "38%"}, "check": "fit_width-not-idempotent", "step": 7}`
- **fit_height-not-idempotent** [-] x2 — example: `{"key": "seq-7-28", "a": {"h": "344", "sl": 0, "st": 0, "tr": null, "vb": "0 0 1490 1212", "w": "423", "z": "28%"}, "b": {"h": "344", "sl": 49, "st": 0, "tr": null, "vb": "0 0 1490 1212", "w": "423", "z": "28%"}, "check": "fit_height-not-idempotent", "step": 14}`

## Coverage against SPEC claim thresholds

- single 100 %: 194/330 (58.8 %)
- pairwise 100 %: 3357/3357 (100.0 %) (lens-value x focus sampled n=300)
- machines (C2) 100 %: 936/936 (100.0 %) (machine x lens-value / x focus sampled 60 each)
- random >= 5000 sequences with 0 unadjudicated: 40 sequences, 19 with violations (adjudication pending)
- metamorphic green: 200 cases, 0 failing

## progress.log DONE lines

```
SUITE single DONE 194/194 disagreements=0 seconds=168.4
SUITE random DONE 40/40 disagreements=19 seconds=297.7
SUITE metamorphic DONE 200/200 disagreements=0 seconds=858.9
SUITE machines DONE 936/936 disagreements=0 seconds=796.7
SUITE multi DONE 1358/1358 disagreements=0 seconds=1465.0
SUITE pairs DONE 3357/3357 disagreements=0 seconds=1989.7
```
