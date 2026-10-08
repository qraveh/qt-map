# machine-2q-classes.csv — the comparability class of every two-qubit error figure (WP2, the editor's decision D4 of 8 Oct 2026)

One row per machine whose register row carries a two-qubit error figure (`err_2q_median` / `err_2q_best` in machines.csv). The classes say under what protocol, scope and conditioning the figure was measured, so that figures are compared only within a class (report §1.1; review R1, finding 1). The build does not rank by this file yet; H2 and the evidence axis A will (WP2).

| column | meaning |
|---|---|
| `machine_id` | the key of machines.csv |
| `err_2q_protocol` | **P-avg** — average gate infidelity from the randomised-benchmarking family (standard, interleaved, simultaneous RB; Magesan et al. 2011); **P-proc** — process (Pauli) infidelity from XEB, cycle benchmarking, layer fidelity / EPLG or GST (convertible to P-avg by ×4/5 for two qubits — Horodecki 1999, Nielsen 2002; IBM's EPLG is already converted); **P-sur** — a surrogate: a vendor dashboard with no named protocol, a statement, a Bell-state fidelity, a target — not rankable |
| `err_2q_scope` | the context of the measurement: **S-iso** an isolated pair (neighbours idle), **S-sim** simultaneous (neighbours driven), **S-layer** a layer over a chain (layer fidelity), **S-cycle** inside a code cycle; empty for surrogates |
| `err_2q_stat` | which statistic over the device's pairs the figure is: **best** / **median** / **mean** / **zone** (averaged over a zone) / **worst** / **single** (one pair only) |
| `err_2q_cond` | the conditioning: **C-none** unconditioned; **C-erase** erasure-excised; **C-loss** loss-postselected; **C-herald** detection-conditional; marks **+leak** / **-leak** (leakage counted in the error or not), **raw** / **spam** (SPAM-corrected) |
| `err_2q_n` | the number of pairs the statistic is over, where stated |
| `err_2q_source` | the URL where the protocol was read |
| `err_2q_quote` | the verbatim sentence or table label (≤ 25 words) naming the protocol and the statistic |
| `confidence` | **high** — protocol and statistic both named at the source; **medium** — one inferred from the figure's context; **low** — nothing at the source, tagged from the register's own text |
| `note` | what could not be settled |

A row with `confidence` low or `err_2q_protocol` P-sur does not enter a class-restricted ranking. The class tags were assigned on 8 Oct 2026 from the machines' own sources (the pilot of WP2; 65 machines); the register's wrong two-qubit values found on the way were corrected in machines.csv the same day (data/changes/2026-10-08.json).
