# V&V runner summary

Generated 2026-09-17 14:48:41 from results_c2d/*.jsonl and progress.log.

| suite | total | agree | disagree |
|---|---|---|---|
| machines | 936 | 936 | 0 |
| metamorphic | 200 | 200 | 0 |
| single | 326 | 326 | 0 |

## Coverage against SPEC claim thresholds

- single 100 %: 326/326 (100.0 %)
- pairwise 100 %: 0/3387 (0.0 %) (lens-value x focus sampled n=300)
- machines (C2) 100 %: 936/936 (100.0 %) (machine x lens-value / x focus sampled 60 each)
- random >= 5000 sequences with 0 unadjudicated: 0 sequences, 0 with violations (adjudication pending)
- metamorphic green: 200 cases, 0 failing

## progress.log DONE lines

```
SUITE single DONE 326/326 disagreements=0 seconds=107.4
SUITE machines DONE 936/936 disagreements=0 seconds=619.0
SUITE metamorphic DONE 200/200 disagreements=0 seconds=833.3
```
