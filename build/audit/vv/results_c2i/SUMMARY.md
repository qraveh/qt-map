# V&V runner summary

Generated 2026-09-23 23:09:10 from build/audit/vv/results_c2i/*.jsonl and progress.log.

| suite | total | agree | disagree |
|---|---|---|---|
| machines | 936 | 936 | 0 |
| metamorphic-run1-harness-check | 200 | 199 | 1 |
| metamorphic | 200 | 200 | 0 |
| multi | 1330 | 1330 | 0 |
| pairs | 3387 | 3387 | 0 |
| single | 326 | 326 | 0 |
| strip | 300 | 300 | 0 |

## metamorphic-run1-harness-check: 1 distinct disagreement signatures

- **M2b-incompatible-isolate-did-not-release** [lens:aff+nvals:1+tog:r+focus+machine] x1 — example: `{"agree": false, "dec_cryo": {"unfiltered_has_dec_cryo": false, "union_has_dec_cryo": false}, "key": "meta-1-141", "state": {"focus": "g_mbq", "isolate": null, "lens": "aff", "machine": "ionq-superion-256", "toggles": "r", "values": [0.75]}, "violations": [{"check": "M2b-incompatible-isolate-did-not-release", "expected": {"focus": null, "machine": "ionq-superion-256"}, "page_state": {"focus": null, "isolate": "ion_elec", "lens": "aff", "toggles": "r", "values": [0.75]}, "path": "ion_elec"}]}`

## Coverage against SPEC claim thresholds

- single 100 %: 326/326 (100.0 %)
- pairwise 100 %: 3387/3387 (100.0 %) (lens-value x focus sampled n=300)
- machines (C2) 100 %: 936/936 (100.0 %) (machine x lens-value / x focus sampled 60 each)
- random >= 5000 sequences with 0 unadjudicated: 0 sequences, 0 with violations (adjudication pending)
- metamorphic green: 200 cases, 0 failing

## progress.log DONE lines

```
SUITE single DONE 326/326 disagreements=0 seconds=250.3
SUITE machines DONE 936/936 disagreements=0 seconds=1152.5
SUITE strip DONE 300/300 disagreements=0 seconds=2167.7
SUITE metamorphic DONE 200/200 disagreements=1 seconds=1591.2
SUITE metamorphic DONE 200/200 disagreements=0 seconds=2367.3
SUITE multi DONE 1330/1330 disagreements=0 seconds=2697.6
SUITE pairs DONE 3387/3387 disagreements=0 seconds=4186.2
```
