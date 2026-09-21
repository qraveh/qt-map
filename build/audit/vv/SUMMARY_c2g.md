# V&V runner summary

Generated 2026-09-21 14:45:09 from build/audit/vv/results_c2g/*.jsonl and progress.log.

| suite | total | agree | disagree |
|---|---|---|---|
| machines-run1-harness-check | 936 | 885 | 51 |
| machines | 936 | 936 | 0 |
| metamorphic | 200 | 200 | 0 |
| pairs | 3387 | 3387 | 0 |
| single | 326 | 326 | 0 |

## machines-run1-harness-check: 1 distinct disagreement signatures

- **bar-summary-missing-machine** [focus+machine] x51 — example: `{"actual": {"edges": 0, "lines": 2, "stations": 23}, "agree": false, "altuse": [], "card": "station", "expected": {"edges": 0, "lines": 2, "stations": 23}, "key": "{\"focus\": \"enc_dualrail\", \"isolate\": null, \"lens\": \"family\", \"machine\": \"ibm-nighthawk-r1\", \"toggles\": \"-\", \"values\": []}", "ms": 845, "page_state": {"focus": "enc_dualrail", "isolate": null, "lens": "family", "toggles": "-", "values": []}, "state": {"focus": "enc_dualrail", "isolate": null, "lens": "family", "machine": "ibm-nighthawk-r1", "toggles": "-", "values": []}, "violations": [{"check": "bar-summary-missi`

## Coverage against SPEC claim thresholds

- single 100 %: 326/326 (100.0 %)
- pairwise 100 %: 3387/3387 (100.0 %) (lens-value x focus sampled n=300)
- machines (C2) 100 %: 936/936 (100.0 %) (machine x lens-value / x focus sampled 60 each)
- random >= 5000 sequences with 0 unadjudicated: 0 sequences, 0 with violations (adjudication pending)
- metamorphic green: 200 cases, 0 failing

## progress.log DONE lines

```
SUITE single DONE 326/326 disagreements=0 seconds=213.4
SUITE machines DONE 936/936 disagreements=51 seconds=1016.6
SUITE metamorphic DONE 200/200 disagreements=0 seconds=2032.3
SUITE pairs DONE 3387/3387 disagreements=0 seconds=3862.5
SUITE machines DONE 936/936 disagreements=0 seconds=1444.4
```
