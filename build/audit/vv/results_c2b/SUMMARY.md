# V&V runner summary

Generated 2026-09-17 13:32:40 from results_c2b/*.jsonl and progress.log.

| suite | total | agree | disagree |
|---|---|---|---|
| machines | 936 | 936 | 0 |
| metamorphic | 200 | 200 | 0 |
| single | 327 | 327 | 0 |

## Coverage against SPEC claim thresholds

- single 100 %: 327/326 (100.3 %)
- pairwise 100 %: 0/3387 (0.0 %) (lens-value x focus sampled n=300)
- machines (C2) 100 %: 936/936 (100.0 %) (machine x lens-value / x focus sampled 60 each)
- random >= 5000 sequences with 0 unadjudicated: 0 sequences, 0 with violations (adjudication pending)
- metamorphic green: 200 cases, 0 failing

## progress.log DONE lines

```
SUITE single DONE 327/327 disagreements=0 seconds=218.7
SUITE machines DONE 936/936 disagreements=0 seconds=827.3
SUITE metamorphic DONE 200/200 disagreements=0 seconds=1023.6
```
