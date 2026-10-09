# V&V single suite — 9 Oct 2026 (branch c9-2026-10-09, ticket 20261009-2)

Run against the final built page `dist/Quantum-Technology-Atlas-2026.09.html` of the ticket — after the lens list went from 13 to 9 and the parallel-coordinates strip was removed (`map_js.py`, the oracle and the runner updated to match), §8.4's H7 and H8 retired to §8.1, the maturity index split (D6-1…D6-5 of the editor's approval of 9 Oct):

    VV_PAGE=…/dist/Quantum-Technology-Atlas-2026.09.html python3 runner.py single --out results_20261009/
    single: done=376/376 new=376 disagreements=0 seconds=449.5

The oracle self-test: OK. `c2_smoke.py`: PASS, 262 ok (the 25 strip checks removed with the strip; the lens lists count 9). `mobile_check.py`: 60 ok; the three picture assertions fail in the cloud (no `media/` folder here), as always.
