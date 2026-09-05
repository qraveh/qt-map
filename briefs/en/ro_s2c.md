---
id: ro_s2c
name: Spin-to-charge conversion + rf reflectometry
layer: "6 Readout"
tier: 3
status: demonstrated
since: 2004
one_line: Spin converted into a charge-motion event by Pauli blockade or energy-selective tunnelling, then read by an rf-matched charge sensor in microseconds without destroying the qubit.
verdict: The readout every silicon path uses and the term that sets the silicon clock — 6 µs at 99.2% or 100 µs at 99.9%, with no published device delivering both.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Spin carries no charge, so a tunnelling event is made spin-conditional — Pauli blockade (two-spin parity, scale = singlet–triplet splitting) or energy-selective Elzerman tunnelling (single spin, needing Zeeman ≫ kT) — and a charge sensor reports it. The sensor is a single-electron transistor or a gate-based single-electron box read via quantum capacitance, in an LC tank near 0.1–2 GHz. Elzerman single-shot readout dates to 2004. Coordinates: readout — spin-to-charge, ~6 µs, non-destructive, mid-circuit-capable; control — low-frequency drive from room temperature, sensor in CMOS, carrier immobile.

## Physics & limits
Per-shot signal-to-noise is the phase shift integrated against amplifier noise over a window capped by T₁ and floored by tank bandwidth — the whole trade: 99.2% under 6 µs [D][1] against 99.9% SPAM at 100 µs [D][2]. Elzerman readout dies as kT approaches the Zeeman energy, so hot (≈1 K) operation costs readout first; Pauli blockade survives there but answers parity. Relaxation inside the window returns a false ground state, and sensor charge noise walks the threshold, so measurement error is drifting and correlated, not independent as decoders assume. Quantum-limited amplification and in-fridge demodulation move the floor.

## Engineering state of the art
| year | figure | who | tag+key |
|---|---|---|---|
| 2023-02-23 | 99.2% single-shot in <6 µs, rf single-electron box | Quantum Motion | [D][1] |
| 2025-09-24 | 99.9% SPAM at 100 µs, 300 mm SiMOS | Diraq | [D][2] |

Dominant term: SNR at short windows, T₁ at long; no foundry device publishes sub-10 µs readout above 99.5%.

## Manufacturing, materials & supply chain
Built in the qubit's own 300 mm CMOS stack, the sensor adds no materials risk; the gate-based box, needing only an electrode and a tank, is the foundry-favoured form. Instrumentation is bought, not built: Zurich Instruments' SHFQC-LRT gives ≤32 µs weighted integration [C][3], and Quantum Machines' OPX1000 lists nine spin customers including Diraq, HRL, imec and Equal1 [C][5]. Frequency multiplexing keeps line count sub-linear: the wall at 10³ is tank spacing across the band; at 10⁴–10⁶ it is aggregate readout bandwidth and amplifier count, not the sensor. HRL's 4 K controller (366 DACs, ≤3.5 W) shows the chain can move inside the fridge [D][6].

## Role in the stack
Required by quantum-dot and donor spins, with no replace or conflict edges — the load-bearing readout node in both the silicon/germanium quantum-dot spin path and the donor-spin path. With exchange gates in tens of nanoseconds, readout at 6–100 µs sets derived clock = sum of the syndrome round: gate layers + transport + readout + reset: 8.5×10⁻⁶ s at the fast end, 6.3 µs of it readout. Verification: the two headline figures are different devices with different sensors — a speed–fidelity curve, not one system — and the 99.9% bundles initialisation. Neither is replicated independently.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do | Evidence |
|---|---|---|---|---|
| Quantum Motion | developer | UK | Single-electron-box readout, 99.2% in <6 µs | [D][1] |
| Diraq | developer | Australia | 99.9% SPAM on 300 mm imec SiMOS | [D][2] |
| Silicon Quantum Computing | developer | Australia | Readout of donor nuclear registers | [D][G:SQC-11Q-2025-12] |
| HRL Laboratories | developer | USA | Readout sequenced by 4 K cryo-CMOS | [D][G:HRL-CRYOCMOS-4K-2026] |
| Zurich Instruments | supplier | Switzerland | Sells the reflectometry instruments | [C][3] |
| Quantum Machines | supplier | Israel | Readout stack for nine spin teams | [C][5] |

**Money.** 2025-02-25 · Quantum Machines · Series C · $170 M · PSG Equity, Intel Capital · closed [C][G:QM-SERIESC-2025-02]. 2025-11-06 · Diraq, Quantum Motion, SQC · QBI Stage B · ≤$15 M each · DARPA · selected [G:QBI-STAGEB-2025-11]. 2026-05-07 · Quantum Motion · Series C · $160 M · DCVC, Kembara · closed [C][G:QM-160M-2026-05]. 2026-05-21 · Diraq · CHIPS LOI · ≤$38 M · US Commerce · non-binding [G:CHIPS-LOI-2026-05].

**Market & supply chain.** Zurich Instruments and Quantum Machines supply the rf chain nearly every spin team buys rather than builds [C][3][5]; cryogenic amplification is the second pinch point. Pays into G2, G3, G7.

**IP & standards.** No dated patent family for spin-to-charge conversion or rf reflectometry in a named database as of 4 Sep 2026.

**Roadmaps & track record.** Diraq (2026-08-27 · 150 k physical, 1 k logical by 2029 · unmet; its 2026-07-09 release said "thousands by 2029") [R][G:DIRAQ-FUNDING]. Zurich Instruments (2026-03-09 · ZQCS for "several thousand qubits" · shipping) [P][4]. No vendor promises a dated readout rate; instruments ship on schedule, qubit counts do not.

**Strategic reading.** Readout is the one silicon subsystem bought rather than built, so control-electronics vendors keep leverage whichever qubit wins; if the gate-based box displaces the sensor transistor, the foundry captures it and per-qubit-sensor designs lose twice.

*Open niche:* every headline number here is combined SPAM or an uncharacterised single-shot fidelity — separating readout from initialisation error, and characterising crosstalk between multiplexed tanks, is open ground.

## Outlook & open questions
Confirm or demote in 12–24 months: ≥99.9% below 20 µs on a foundry device; ≥16 sensors multiplexed on one line with a crosstalk number. Best case 2029: >100 sensors read under 10 µs each, demodulated in-fridge. Worst case: readout stays the clock-setting term and the largest syndrome-cycle error. Open: (1) tanks per quantum-limited amplifier; (2) whether parity readout suffices without a per-qubit ancilla; (3) how correlated threshold drift looks to a decoder.

## Sources
[1] G. A. Oakes, V. N. Ciriano-Tejel, M. F. Gonzalez-Zalba et al. (Quantum Motion, Cambridge, UCL, CEA-Leti, Hitachi Cambridge) · "Fast High-Fidelity Single-Shot Readout of Spins in Silicon Using a Single-Electron Box" · Physical Review X 13, 011023 · 2023-02-23 · https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.011023 [D]
[2] Diraq and imec · "300 mm foundry SiMOS spin qubits: two-qubit fidelity and SPAM" · Nature · 2025-09-24 · https://www.nature.com/articles/s41586-025-09531-9 [D]
[3] Zurich Instruments · "SHFQC-LRT Long Readout Time option" · product release · 2025-01-30 · https://www.zhinst.com/en/products/shfqc-lrt-long-readout-time [C]
[4] Zurich Instruments (Rohde & Schwarz) · ZQCS quantum control platform launch, >1,000 channels per rack · trade press · 2026-03-09 · http://quantumwire.com/articles/zurich-instruments-zqcs [P]
[5] Quantum Machines · "Semiconductor spin qubits" — OPX1000, QDAC-II, QSwitch, named customers · company page · accessed 2026-09-04 · https://www.quantum-machines.co/qubit-types/semiconductor-spin-qubits/ [C]
[6] HRL Laboratories · "A silicon quantum processor that runs itself" — 4 K cryo-CMOS controller, 366 DACs, ≤3.5 W · arXiv:2604.16216 · 2026-07-29 · https://arxiv.org/abs/2604.16216 [D]

## Open verification items
The multimode-reflectometry preprint arXiv:2512.05087 (98% in 8 µs to 2 GHz) is not included in the records table: its authors and institution could not be resolved (the abstract page returns no metadata; the arXiv export API is robots-disallowed). The ZQCS channel count is a trade-press restatement of a vendor launch, not a primary release. No source gives an RB-separated readout-only fidelity for the Diraq/imec 99.9%, quoted as SPAM.
