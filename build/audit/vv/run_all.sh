#!/bin/bash
# Full V&V runs on the baseline page (session C1, 16 Sep 2026). Each suite in its own browser; logs under logs/.
cd /home/claude/qt-map/build/audit/vv
for s in single static multi metamorphic pairs; do
  nohup python3 runner.py $s --out results/ > logs/$s.log 2>&1 &
done
for k in 1 2 3 4; do
  nohup python3 runner.py random --n 250 --seed $((100+k)) --out results/random-s$k/ > logs/random-s$k.log 2>&1 &
done
wait
echo ALL-DONE >> results/progress.log
