# results_c13 — the single suite on the build of 30 Sep 2026, evening: a late language no longer pulls the reader back, stale record pages removed, the release metadata brought up to date

`VV_PAGE=<abs path>/dist/Quantum-Technology-Atlas-2026.09.html python3 build/audit/vv/runner.py single --out build/audit/vv/results_c13` run on the dist of the commit that carries this folder (English page sha256 fc167d96b82cf870…).

| suite | states | disagreements | seconds | note |
|---|---|---|---|---|
| single | 392 | 0 | 426 | every lens value, every architecture, every technology, every machine alone — as results_c12 (182 machines) |

Neither the data nor the lit-set logic changed since results_c12: the commit changes when a late language fragment may reveal the URL's target (LANG_JS), removes record pages the build did not write, and corrects the About paragraph's edge count ("four kinds of edge") in the three languages. The suite confirms the page still lights exactly what the oracle derives.
