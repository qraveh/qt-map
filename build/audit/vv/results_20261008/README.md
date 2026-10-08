# V&V single suite — 8 Oct 2026 (branch c7-2026-10-08, the session's ticket 20261008-1)

Run against the built page `dist/Quantum-Technology-Atlas-2026.09.html` after the generator changes of 8 Oct (the §8 counters over devices in `machines_chapter.py`, the H2 comparability paragraph, the sitemap `lastmod` ledger in `pages.py`, the empty-slot strings in `map_js.py`, `cards.py` and `build_html.py`, the data cut-off in `build_html.py`):

    VV_PAGE=…/dist/Quantum-Technology-Atlas-2026.09.html python3 runner.py single --out results_20261008/
    single: done=395/393 new=25 disagreements=0

The oracle self-test: OK. The smoke suite (`c2_smoke.py`): PASS, 287 ok. `mobile_check.py`: the three picture assertions fail in the cloud sandbox, which has no `media/` folder (the thumbs live on the laptop; `media.py --check --thumbs` is the local side's check); every other assertion ok.
