---
id: g_rip
name: Resonator-induced phase gate on fluxonium (all-microwave)
layer: "3 Gate mechanism"
status: emerging
since: 2026
one_line: An all-microwave controlled-phase gate — a detuned drive on the resonator coupling two fixed-frequency fluxoniums imprints a state-dependent phase; 128 ns, 99.44% on the best pair, one group.
verdict: Real on five fluxoniums at 96–99.4%, a decade after the same gate on transmons; it keeps its place only if a second group, or the first at 99.9%, shows that the connectivity-four cell beats the tunable coupler it competes with.
updated: 2026-11-07
---

RIP = resonator-induced phase; FRF = fluxonium–resonator–fluxonium (the unit cell); IRB = interleaved randomised benchmarking; ZZ = the always-on conditional frequency shift between two coupled qubits.

## Identity & lineage

Drive a resonator that couples two qubits, off resonance, and the resonator's frequency depends on the qubits' joint state; the drive therefore accumulates a phase that depends on that state, and when the pulse ends with the resonator empty the qubits are left with a controlled-phase gate and nothing else. Cross and Gambetta worked out the pulse shapes that keep the residual photons and the dephasing small (Phys. Rev. A 91, 032325, 2015) [S][907]; IBM demonstrated the gate on two four-qubit devices of 3D transmons, twelve pairs with detunings up to 1.8 GHz, per-gate fidelities 0.9655–0.9853 at 285–760 ns and a four-qubit GHZ state at 60.5% (Phys. Rev. Lett. 117, 250502, 2016) [D][908]. Its attraction was always frequency flexibility: fixed-frequency qubits far apart in frequency, no flux line, no tunable element. The transmon field went the other way — tunable couplers (`g_tc`) and cross-resonance (`g_cr`) — and the RIP gate waited for a carrier that needs it.

Fluxonium is that carrier: a low-frequency qubit (400–500 MHz here) with long relaxation and a large anharmonicity, whose two-qubit gates to date run through flux-tunable transmon couplers — a 22-qubit chain reached a best CZ of 99.9% at 32 ns with an average near 99% [P][909]. In August 2026 the Walther-Meißner-Institut and TU Munich replaced the tunable coupler by a lumped-element resonator: five fluxoniums at 399–493 MHz, four resonator couplers at 7.36–7.79 GHz, the centre qubit coupled to all four — a connectivity-four unit cell with the parasitic couplings suppressed by design. The RIP gate takes 128 ns; a refocused version (two 96 ns pulses with a π pulse on the spectator qubit between them) cancels the conditional phase a spectator would otherwise imprint. Refocused two-qubit fidelities by IRB: 99.20(5)%, 98.4(1)%, 96.2(2)% and 99.44(3)% on the four pairs, median 98.8(12)%; simultaneous single-qubit fidelity 99.957(5)% against a coherence limit of 99.96(1)%; residual static ZZ below 1 kHz on every pair (median 30(215) Hz); GHZ states of three, four and five qubits at 96.9(2)%, 95.4(2)% and 90.0(2)% after measurement-error correction [P][910].

Attributes (technology graph): carrier affinity 1.0 — fabricated. Characteristic time 128 ns, deterministic. Readout: none of its own (dispersive, through `ro_disp`). Mobility: static wiring. Control: microwave from room temperature. Error structure: coherent (spectator phases, calibration spread) and Pauli (dephasing through coupler photon loss). Manufacturing: superconducting lithography.

## Physics & limits

The gate's rate is set by the difference of dispersive shifts the two qubits give the coupler and by the drive amplitude; its error by two things the same drive brings. Photons leaking from the coupler during the pulse carry which-state information and dephase the qubits — small here, the authors find, as IBM found in 2016 where measurement-induced dephasing stayed near 10⁻³ at the lowest detuning tested [D][908] — and photons left in the coupler at the end entangle it with the qubits, which the pulse shaping of Cross and Gambetta is designed to prevent [S][907]. On the fluxonium cell the measured limit is neither: it is the spread of dispersive shifts and coupler frequencies across the four pairs, which the authors say "is not a limitation of the FRF architecture itself", and the device's readout, which they call its present limit [P][910]. The spectator problem is structural: a qubit in |1⟩ on a third arm of the cell shifted one pair's fidelity from 99.68(5)% to 96.1(6)% until refocused, and refocusing forbids running two gates on neighbouring pairs at once — parallelism is traded for isolation until the coupler–coupler detuning grows [P][910]. The floor is coherence: T₁ of 57–87 µs and echo T₂ of 65–87 µs over a 128 ns gate put the coherence-limited error in the 10⁻³ class, and the best pair is already within a factor of a few of it [P][910]. At 128 ns the gate is three to four times slower than a tunable-coupler CZ on fluxonium (32 ns) [P][909] or on transmons (30–70 ns, `g_tc`).

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: 99.44(3)% on one pair, 98.8(12)% median over four, 128 ns, with a five-qubit GHZ state at 90.0(2)% [P][910]. Typical at scale: none — one five-qubit device, one group, a preprint.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2015-03 | Pulse shapes for the RIP gate: adiabatic drive, no residual photons | IBM (theory) | [S][907] |
| 2016-12 | RIP gate on 3D transmons: 12 pairs, detunings to 1.8 GHz, per-gate 0.9655–0.9853, 285–760 ns, 4-qubit GHZ 60.5% | IBM | [D][908] |
| 2026-04 | The competing route: fluxonium CZ through flux-tunable transmon couplers, best 99.9% at 32 ns, 22-qubit chain | Quantum Science Center of the Greater Bay Area | [P][909] |
| 2026-08 | RIP gate on fluxonium: 5 qubits, connectivity four, 128 ns, 99.44(3)% best, 98.8(12)% median, ZZ < 1 kHz, GHZ₅ 90.0(2)% | WMI / TU Munich | [P][910] |

Dominant error term: pair-to-pair variation of dispersive shifts and coupler frequencies, then readout; coherence sets the floor [P][910].

## Manufacturing, materials & supply chain

The cell is standard superconducting lithography with the fluxonium's one extra feature, a junction array: a 100 mm high-resistivity silicon wafer etched of its native oxide, 150 nm of sputtered niobium patterned by maskless optical lithography and SF₆ reactive-ion etching, niobium air bridges over feed and flux lines, aluminium Josephson junctions by double-angle shadow evaporation (30 nm + 70 nm) with aluminium bandages to the niobium ground plane, and 2 µm niobium wires as the coupler inductors [P][910]. Nothing in it is foundry-specific — the process is a university cleanroom's — and that is the supply-chain statement: the gate has no industrial maker, no 300 mm process and no datasheet. The single point of failure is the one group. Export-control exposure is the hardware's [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

All-microwave: the gate needs one drive line per coupler resonator and the qubits' XY lines; the fluxonium still needs a static flux bias at half a flux quantum, but no fast flux pulse, which removes the flux-pulse distortion and the pulse-shaping of the tunable-coupler route. The line count per qubit is therefore about the degree of the lattice divided by two, plus one — the same order as a tunable-coupler lattice's flux lines, moved from flux to microwave. The channels are of the kind frequency-division multiplexing (`ct_fdm`) can share, since the coupler frequencies (7.36–7.79 GHz) are well separated from the qubits' (0.4–0.5 GHz) [P][910]. Readout is dispersive and, by the authors' account, the present device's limit; the GHZ fidelities fall from 96.9%, 95.4% and 90.0% to raw values of 64.8(1)%, 68.5(2)% and 62.4(1)% without measurement-error correction [P][910].

## Role in the stack

Architectures: an alternate gate on the transmon lattice with tunable couplers (`sc`), the path that carries fluxonium as its alternate carrier. It requires the fluxonium carrier, superconducting lithography and microwave control from room temperature or cryo-CMOS; it is an alternative to the flux-tunable coupler (`g_tc`) and to cross-resonance (`g_cr`), the other all-microwave gate on fixed-frequency qubits. The map's gap register listed this gate as a gap on fluxonium — an all-microwave parametric two-qubit gate that was neither cross-resonance nor a tunable coupler; the gap now has a technology, on one group's device. Price of switching from the tunable coupler: four times the gate time and, today, a lower median fidelity; gained: no flux line per coupler, frequency flexibility, a four-fold coupler cell and a residual ZZ below 1 kHz without a tunable element. Derived clock: the `sc` round is set by the primary gate (`g_tc`); a fluxonium lattice on RIP gates would add about 100 ns per two-qubit layer.

## Evidence — how the numbers were measured

Two-qubit fidelities are interleaved randomised benchmarking on each pair with the refocused gate; the spectator test compares one pair's IRB with the third qubit in |0⟩ and in |1⟩, without and with refocusing; single-qubit fidelities are simultaneous randomised benchmarking; GHZ fidelities are state tomography with measurement-error correction, the raw values given beside them; ZZ is measured per coupler with its uncertainty [P][910]. The abstract's "two-qubit gate fidelities exceeding 99%" is true of two pairs of four; the per-pair table shows 98.4(1)% and 96.2(2)% on the other two, and the median is 98.8(12)% — this record carries the table, not the abstract. IBM's 2016 figures are two-qubit randomised benchmarking per Clifford (0.93–0.97) converted to per-gate values (0.9655–0.9853) [D][908]. Not published: a parallel two-qubit gate on the cell, a per-pair error budget, a peer-reviewed version, any second device.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| Walther-Meißner-Institut / TU Munich (Filipp) | research | DE | The only RIP gate on fluxonium; the connectivity-four FRF cell | [P][910] |
| IBM | developer | US | Origin of the gate (theory 2015, 3D transmons 2016); not used in its production lattices | [S][907][D][908] |
| Quantum Science Center of the Greater Bay Area (Shenzhen) | research | CN | The competing fluxonium route: tunable-coupler CZ on a 22-qubit chain | [P][909] |
| Google Quantum AI | developer | US | Fluxonium through Atlantic Quantum (joined Google 2025-10); gate route unpublished | [G:GOOGLE-ATLANTIC-2025-10] |

**Money.** No dated money is attached to this gate. Google's absorption of Atlantic Quantum, the fluxonium start-up, carries no disclosed sum [G:GOOGLE-ATLANTIC-2025-10].

**Market & supply chain.** No product uses it; the fluxonium machines of the register use tunable couplers. The gate competes for the same slot on the same carrier, so its market is whatever fluxonium's becomes.

**IP & standards.** The gate's origin is IBM's and published; no patent search was made for this record. No standard.

**Roadmaps & track record.** No roadmap names a RIP gate on fluxonium. The WMI/TUM preprint's stated next steps are shorter pulses, higher coupler–coupler detuning to restore parallel gates, and a readout upgrade; it calls the cell "a viable building block for densely connected fluxonium processors" [P][910].

**Strategic reading.** The question the gate answers is whether fluxonium needs a tunable transmon coupler at all. If the RIP cell reaches 99.9% with parallel gates, fluxonium lattices lose a flux line per coupler and gain a degree-four cell; if the tunable-coupler chain reaches 99.9% median first, this stays a laboratory alternative. The decision is Google's and the Shenzhen group's more than Munich's.

## Outlook & open questions

Confirm within 12–24 months if a second group runs a RIP gate on fluxonium, if the WMI/TUM cell reaches 99.9% on a pair or 99.5% median, or if two gates run in parallel on neighbouring pairs. Demote if the tunable-coupler route reaches 99.9% median on a lattice while this stays below 99.5%, or if the preprint is not published by end-2027. Best case by 2029: a fluxonium lattice on resonator couplers with no fast flux lines; worst case: a single paper.

Open questions: (1) what sets the pair-to-pair spread, and can design remove it? (2) does the gate time fall below 60 ns without raising the photon-loss dephasing? (3) can parallel gates run on a connectivity-four cell at all? (4) does the readout limit go away with a Purcell filter and a better amplifier? (5) does anyone outside Munich build an FRF cell?

## References

[907] A. W. Cross and J. M. Gambetta, “Optimized pulse shapes for a resonator-induced phase gate,” *Phys. Rev. A*, vol. 91, no. 3, Art. no. 032325, Mar. 2015, doi: [10.1103/PhysRevA.91.032325](https://doi.org/10.1103/PhysRevA.91.032325). [arXiv:1411.5436](https://arxiv.org/abs/1411.5436). [S]
[908] H. Paik *et al.*, “Experimental demonstration of a resonator-induced phase gate in a multiqubit circuit-QED system,” *Phys. Rev. Lett.*, vol. 117, no. 25, Art. no. 250502, Dec. 2016, doi: [10.1103/PhysRevLett.117.250502](https://doi.org/10.1103/PhysRevLett.117.250502). [arXiv:1606.00685](https://arxiv.org/abs/1606.00685). [D]
[909] Z. Zhan *et al.*, “Scalable fluxonium quantum processors via tunable-coupler architecture,” [arXiv:2604.13363](https://arxiv.org/abs/2604.13363), Apr. 2026. [P]
[910] J. Schirk *et al.*, “High-fidelity entangled states in a connectivity-four fluxonium quantum processor,” [arXiv:2608.25503](https://arxiv.org/abs/2608.25503), Aug. 2026. [P]

