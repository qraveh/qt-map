---
id: enc_zeeman
name: Zeeman ground-state qubit (nuclear-spin-free ion)
layer: "2 Encoding"
status: demonstrated
since: 2005
one_line: "The two spin sublevels m = ±1/2 of the S₁/₂ ground level of an ion without nuclear spin (⁴⁰Ca⁺, ⁸⁸Sr⁺, ¹³⁸Ba⁺), driven by RF fields or Raman beams and read by shelving to D₅/₂; AQT's 31-qubit LYNX register runs on it, with a mean two-qubit error of 2.84(8)×10⁻³ over all 276 pairs of a 24-qubit register."
verdict: "Two decades in laboratories and a processor register since Oct 2026, on a company preprint, with coherence bought by magnetic engineering and spin echo: the qubit moves 28.0 MHz per mT, so its T₂ is the field's — 18(1) ms in the 2021 Innsbruck–AQT rack, 0.35(10) s Ramsey and 3.3(5) s echoed on LYNX. Confirmed if LYNX's figures pass peer review or reach delivered units; demoted to a laboratory memory if AQT's next processor moves to a hyperfine isotope."
updated: 2026-11-22
---

RF = radio frequency; SPAM = state preparation and measurement; RB = randomised benchmarking; QV = quantum volume; GHZ = Greenberger–Horne–Zeilinger state; TEM00/TEM10 = Gaussian and first-order Hermite–Gauss laser modes; EMCCD = electron-multiplying CCD camera; QCCD = quantum charge-coupled device; µ-metal = nickel–iron magnetic shielding alloy; T₁, T₂ = population lifetime and phase-coherence time; AQT = Alpine Quantum Technologies; rms = root mean square; AC Stark shift = light shift; SmCo = samarium–cobalt.

## Identity & lineage

An ion whose nucleus carries no spin — ⁴⁰Ca⁺, ⁸⁸Sr⁺, ¹³⁸Ba⁺ — has a ground level S₁/₂ with exactly two sublevels, m = ±1/2: the bare spin of the valence electron, split by an applied field. The qubit lives there: no hyperfine structure, hence no field-insensitive clock point (as in `enc_hf`), and no optical decay, hence no lifetime ceiling (as in `enc_opt`). The splitting is a radio frequency set by the field: 4.8 MHz in Oxford's 2006 gate [D][972], 10.5 MHz at Mainz [D][973], 13.366 MHz for ⁸⁸Sr⁺ at the Weizmann Institute [D][974], about 18 MHz on LYNX [P][975]. Papers call it a spin, Zeeman or ground-state qubit.

The hardware record begins in Innsbruck in 2005: a Bell state of two ⁴⁰Ca⁺ ions, made on the optical S–D qubit and transferred into the Zeeman sublevels, was prepared at 89% fidelity and stayed entangled for more than 20 s as a decoherence-free pair, against about 1 ms of single-ion coherence [D][976]. Oxford ran the first gate found acting directly on two such spin qubits in 2006 — a light-shift gate at 83% Bell-state fidelity — citing the absence of spectator levels to leak into [D][972]. Poschinger and Schmidt-Kaler's group, then at Ulm, later at Mainz, built a spin qubit in a segmented micro-trap in 2009 [D][977]; Weizmann read a ⁸⁸Sr⁺ Zeeman qubit at 0.9989(1) in 2011 [D][974]; Oxford entangled a ⁴⁰Ca⁺ Zeeman qubit with a ⁴³Ca⁺ hyperfine qubit at 99.8(6)% in 2015 [D][978]; Mainz reached 2.1(1) s spin-echo coherence in 2016 [D][973] and ran a six-qubit shuttling processor on spin qubits in 2022 [D][979]. In 2026 Innsbruck and AQT entangled ¹³⁸Ba⁺ Zeeman qubits in chains of up to 12 ions [D][980], and LYNX made the encoding a 31-qubit register [P][975]. People carried it: M. Hettrich, an author of the 2009 paper, signs LYNX [D][977], [P][975]. The map's year, 2005, is the Innsbruck pair — the earliest two-qubit device found storing and measuring qubits in this encoding; the earliest native gate found followed in 2006.

Attributes (technology graph): carrier affinity 0 — natural. Characteristic time: none of its own; its clock is its coherence. Readout: none of its own — `ro_fluor` after shelving one state to D₅/₂. Mobility: none. Control modality: none of its own (RF fields or lasers drive it), placed at room temperature. Error structure: Pauli (magnetic dephasing, spin flips from stray resonant light) and coherent (field-gradient phases, calibrated out). Manufacturing: none — magnets and shielding are its hardware.

## Physics & limits

Field sensitivity is the defining fact. With g ≈ 2 the ⁴⁰Ca⁺ ground-state qubit moves 28.0 MHz per mT, five times the least sensitive S–D line (5.6 MHz per mT) [D][253]; one nanotesla of noise is 28 Hz of detuning [S]. Coherence is therefore a property of the magnetic environment: usual laboratory measures give 10–40 ms; Mainz's two-layer µ-metal shield with Sm₂Co₁₇ permanent magnets gave 300(50) ms Ramsey and 2.1(1) s spin echo (residual noise ≤ 2.7 pT rms), and needed shield and magnets together [D][973]. The 2021 Innsbruck–AQT rack measured 18(1) ms Ramsey on this qubit [D][253]; LYNX reports 0.35(10) s Ramsey and 3.3(5) s with a π pulse every 300 µs [P][975]. Gradients become phases: about 80 mHz/µm residual on LYNX [P][975], up to 2π × 7 kHz across Mainz's transport trap, calibrated out [D][979].

There is no decay, so T₁ is set by stray resonant light: 10(3) s on LYNX, limited by leaking 397 nm light [P][975]. A spin-1/2 level has no spectator sublevel [D][972]; leakage needs scattering into the D levels, and Innsbruck measures all off-resonant scattering in its ¹³⁸Ba⁺ gate at 1.2×10⁻⁴ [D][980].

Readout cannot be direct: the splitting is below the 22 MHz linewidth of the 397 nm line, so both states fluoresce [D][977]. One state is shelved into D₅/₂ — with high fidelity only by a narrow-line laser — or mapped onto an ancilla [D][974]. The encoding removes the optical phase from the gates, not the narrow-line laser from the machine.

How the gate fits. The two spin states take different light shifts in circularly polarised light [G], so a moving polarisation gradient exerts a spin-dependent force — from the σ± components of a walking wave at Oxford [D][972], from beams of orthogonal linear polarisation at Mainz [D][979]. The Innsbruck–AQT gate makes the gradient transverse with overlapped TEM00 and TEM10 beams and needs only a differential AC Stark shift between the qubit states [D][980]. Off-resonant light references no optical phase to the qubit [D][978]; LYNX's gate is insensitive to optical phase, and its built-in echo doubles as dynamical decoupling for the whole register [P][975].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: one ⁴⁰Ca⁺ chain of 31 qubits (AQT LYNX, company preprint) — two-qubit error 2.84(8)×10⁻³ mean (median 2.7×10⁻³) over all 276 pairs of a 24-qubit register, 1.0(1)×10⁻² over 10 pairs of the full register; single-qubit error 8(5)×10⁻⁵ and 1.6(2)×10⁻⁴; SPAM 11(1)×10⁻⁴; 31-qubit GHZ fidelity 0.65(2); QV 2¹⁵ [P][975]. Peer-reviewed: 99.8(6)% Bell-state fidelity (readout-corrected) on a ⁴⁰Ca⁺–⁴³Ca⁺ pair [D][978]; gate errors below 5×10⁻³ in chains of up to 12 ¹³⁸Ba⁺ ions [D][980]; gates of about 99.6(2)% in a six-qubit shuttling processor [D][979]. Typical at scale: one processor.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2005-07 | Two ⁴⁰Ca⁺ ions: Bell state stored in the Zeeman sublevels, 89%, entangled > 20 s | Innsbruck | [D][976] |
| 2006-09 | First gate found acting directly on two ⁴⁰Ca⁺ spin qubits; Bell fidelity 83% | Oxford | [D][972] |
| 2011-07 | ⁸⁸Sr⁺ Zeeman-qubit readout 0.9989(1) by 674 nm shelving | Weizmann Institute | [D][974] |
| 2015-12 | ⁴⁰Ca⁺ Zeeman – ⁴³Ca⁺ hyperfine Bell state 99.8(6)% (readout-corrected), 27.4 µs gate | Oxford | [D][978] |
| 2016-09 | One ion: spin echo 2.1(1) s, Ramsey 300(50) ms (µ-metal + Sm₂Co₁₇) | Mainz | [D][973] |
| 2022-02 | Six spin qubits, shuttling processor; flag-conditioned parity check 93.2(2)% | Mainz | [D][979] |
| 2026-10 | ¹³⁸Ba⁺ Zeeman qubits: light-gradient gate error < 5×10⁻³ in up to 12 ions | Innsbruck / AQT | [D][980] |
| 2026-10 | LYNX: 31 ⁴⁰Ca⁺ qubits; 2.84(8)×10⁻³ mean over the 276 pairs of a 24-qubit register (1.0(1)×10⁻² over 10 pairs at 31); 3.3(5) s with echo | AQT | [P][975] |

Dominant error term: magnetic dephasing — in Innsbruck's budget for a 220 µs ¹³⁸Ba⁺ gate, qubit T₂ decoherence is the largest term by a narrow margin, 9.6×10⁻⁴ against 8.7×10⁻⁴ for motional decoherence, of 2.9×10⁻³ [S][980]; readout adds 11(1)×10⁻⁴ on LYNX, at the floor set by the D₅/₂ lifetime [P][975].

## Manufacturing, materials & supply chain

Nothing is fabricated for the encoding; its hardware is magnetic. Mainz's enclosure has two 2 mm µ-metal layers around 6 mm of aluminium (20–30 dB from 50 Hz to 100 kHz), from Sekels GmbH, with 80 Sm₂Co₁₇ magnets (−0.03 %/K) from IBS Magnet [D][973]; the 2021 Innsbruck–AQT rack used an ASTM A753 Alloy 4 shield, temperature-compensated SmCo magnets giving 0.50 mT and three sets of compensation coils [D][253]. ⁴⁰Ca is calcium's natural majority isotope, so nothing is enriched [G]. LYNX's light — 397 and 866 nm for cooling and detection, 729 and 854 nm for sideband cooling, pumping and shelving, 405 nm for gates — is standard calcium optics; the RF antenna is the encoding's own item [P][975]. Export-control exposure is the hardware's [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

On LYNX one collective RF field near 2π × 18 MHz, from an antenna, rotates every qubit about x and y; one 405 nm beam steered by acousto-optic deflectors (waist ≈ 1 µm, crosstalk < 10⁻³) adds local z rotations; an entangling gate uses one composite 405 nm beam per qubit, TEM00 plus TEM10 in orthogonal linear polarisations, propagating along the field [P][975]. Durations: about 90 µs per single-qubit rotation, 210 µs per entangling gate with its echo, 6.5 ms per dense 15-qubit layer — 150 layers per second without overheads, 44 with them [P][975]. The RF drive is global, so drive lines do not grow with the register; the per-qubit channels are optical [S]. Readout shelves |S₁/₂, −1/2⟩ into D₅/₂ with several 729 nm pulses, then images 397 nm fluorescence on an EMCCD camera in about 2 ms [P][975]. Mainz shelves by two rapid-adiabatic-passage pulses and counts photons for 800 µs on singled ions after transport, with state preparation below 10⁻³ infidelity [D][979].

## Role in the stack

Architectures: slot 2 of Trapped ions — linear Paul trap with individual laser addressing (`ion_chain`: LYNX, the Innsbruck ¹³⁸Ba⁺ chains) and of Trapped ions — QCCD (`ion_qccd`: Mainz), beside `enc_hf`, `enc_opt` and `enc_omg`. It **requires** the carrier `ion` in a nuclear-spin-free species and reads through `ro_fluor` after shelving. It **replaces** `enc_hf` (hyperfine clock levels vs Zeeman sublevels of a nuclear-spin-free isotope: field immunity traded for a two-level ground state, an RF drive and no enrichment), `enc_opt` (on the same ⁴⁰Ca⁺ ion, the laser-phase limit and 1.17 s lifetime [D][253] exchanged for five times the field sensitivity) and `enc_omg`, whose ground-state level it can supply — Innsbruck calls its gate compatible with omg (optical–metastable–ground) encodings [D][980]. Gate partner: `g_ms` — LYNX's only entangler, the structured-light light-shift gate, is native here because the two spin states feel opposite polarisation-gradient forces. Control: `ct_ionaod`; the RF antenna has no node. Not on `ion_elec`: no laser-free two-qubit gate on this encoding appears in the sources read. Conflict: the `ro_fluor`–`enc_hf` mechanism applies more strongly here, since both spin states scatter detection light, but no source read measures spectator error from mid-circuit detection on a Zeeman register; the nearest measured price is LYNX's 10(3) s T₁ from leaking 397 nm light [P][975], and Mainz moves the ion out of the laser zone while it waits [D][973]. Register: AQT LYNX, entered under the optical qubit, is a Zeeman machine by its own description.

## Evidence — how the numbers were measured

LYNX's two-qubit figure is interleaved RB with up to 50 two-qubit Cliffords on each of the 276 pairs of the 24-qubit register; the 31-qubit figure covers 10 pairs. Single-qubit figures are standard RB up to 400 Cliffords; idle qubits lose 1.8(2)×10⁻⁵ per Clifford, attributed to lifetime and RF pulse quality, not crosstalk. The GHZ fidelity is raw; SPAM was measured in the 31-qubit register. The paper calls the echoed coherence an "effective coherence time T₂*", the reverse of the usual naming; this record gives both values with their conditions [P][975]. All LYNX figures are one version of a company preprint, not peer-reviewed as of 22 Nov 2026.

Value conflicts: the Ramsey T₂ of AQT's ground-state qubit is 18(1) ms on the 2021 rack [D][253] and 0.35(10) s on LYNX [P][975] — different machines; the Atlas uses LYNX's. Not published: LYNX's magnetic environment (18 MHz implies about 0.64 mT [S]), its leakage per gate, a two-qubit error budget, register-wide T₂ without echo, any mid-circuit measurement.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| AQT (Alpine Quantum Technologies) | developer | AT | LYNX: 31 ⁴⁰Ca⁺ Zeeman qubits, structured-light gate, RF rotations | [P][975] |
| University of Innsbruck (Blatt, Monz) | research | AT | 2005 Zeeman Bell states; 2026 ¹³⁸Ba⁺ light-gradient gates with AQT | [D][976], [980] |
| University of Mainz (Schmidt-Kaler, Poschinger) | research | DE | Spin-qubit QCCD: shielded long-lived qubit, six-qubit shuttling processor | [D][973], [979] |
| University of Oxford | research | UK | First gate on ⁴⁰Ca⁺ spin qubits; mixed-isotope logic with ⁴³Ca⁺ | [D][972], [978] |
| Weizmann Institute of Science (Ozeri) | research | IL | ⁸⁸Sr⁺ Zeeman-qubit readout and tomography | [D][974] |
| Instituto de Física Teórica UAM-CSIC (Bermudez) | research | ES | Theory of the structured-light gate | [D][980] |

**Money.** No dated money is attached to the encoding. LYNX acknowledges Horizon Europe grant 101114305 (MILLENION-SGA1), European Innovation Council grant 190118992 (QCDC) and project P2508223 of aws, the Austrian promotional bank, without sums [P][975].

**Market & supply chain.** LYNX's first units are scheduled for select strategic partners in Q4 2026 [R][G:AQT-LYNX-QV-2026-05]. No other company was found publishing a processor on this encoding; its inputs — samarium-cobalt magnets, µ-metal, calcium-wavelength lasers — are generic.

**IP & standards.** The LYNX paper cites AQT's granted European patent EP4322071B1 for the transverse state-dependent force [P][975], the Innsbruck paper an application of the same title, no. 19/102,679, filed 4 Aug 2023 [D][980]; both concern the gate, not the encoding. No patent search was made for this record. No standard.

**Roadmaps & track record.** The 2021 Innsbruck–AQT rack was the first phase of a 50-qubit demonstrator [D][253]; LYNX holds 31 and names more ions per trapping region and more regions as its path [R][975]. Innsbruck lists a move to hyperfine ¹³⁷Ba⁺ among possible improvements, to suppress the T₂ term [R][980].

**Strategic reading.** The encoding buys simplicity — no enrichment, no gigahertz drive, one RF antenna, gates without optical phase — and pays in field sensitivity. AQT bets that shielding, permanent magnets and echo-embedded gates make that price small; its academic partners list a hyperfine isotope among the possible ways to remove it. AQT's next processor decides which reading holds.

## Outlook & open questions

Confirm within 12–24 months if LYNX's figures appear in a peer-reviewed paper or in delivered units, or a second group runs a register of ten or more Zeeman qubits at 10⁻³-class two-qubit error. Demote if AQT's next processor moves to a hyperfine isotope, or if echoed coherence across a 50-ion register falls below a second. Best case by 2029: ⁴⁰Ca⁺ Zeeman registers in multi-zone traps with optical-phase-free gates; worst case: one vendor's encoding, replaced by ¹³⁷Ba⁺ or ⁴³Ca⁺.

Open questions: (1) What is LYNX's magnetic environment, and what T₂ does it give across 31 ions without echo? (2) Can a chain of Zeeman qubits take a mid-circuit measurement without depolarising its neighbours, when both spin states scatter 397 nm light? (3) What is the leakage per gate into D₃/₂ and D₅/₂? (4) Does the echo-embedded gate keep its 10⁻³-class error through transport between zones? (5) Will Innsbruck and AQT move to ¹³⁷Ba⁺?

## References

[253] I. Pogorelov *et al.*, “Compact Ion-Trap Quantum Computing Demonstrator,” *PRX Quantum*, vol. 2, no. 2, Art. no. 020343, Jun. 2021, doi: [10.1103/PRXQuantum.2.020343](https://doi.org/10.1103/PRXQuantum.2.020343). [arXiv:2101.11390](https://arxiv.org/abs/2101.11390). [D]
[972] J. P. Home *et al.*, “Deterministic entanglement and tomography of ion–spin qubits,” *New Journal of Physics*, vol. 8, no. 9, Art. no. 188, Sep. 2006, doi: [10.1088/1367-2630/8/9/188](https://doi.org/10.1088/1367-2630/8/9/188). [arXiv:quant-ph/0603273](https://arxiv.org/abs/quant-ph/0603273). [D]
[973] T. Ruster, C. T. Schmiegelow, H. Kaufmann, C. Warschburger, F. Schmidt-Kaler, and U. G. Poschinger, “A long-lived Zeeman trapped-ion qubit,” *Applied Physics B*, vol. 122, no. 10, Art. no. 254, Sep. 2016, doi: [10.1007/s00340-016-6527-4](https://doi.org/10.1007/s00340-016-6527-4). [arXiv:1606.07220](https://arxiv.org/abs/1606.07220). [D]
[974] A. Keselman, Y. Glickman, N. Akerman, S. Kotler, and R. Ozeri, “High-fidelity state detection and tomography of a single-ion Zeeman qubit,” *New Journal of Physics*, vol. 13, no. 7, Art. no. 073027, Jul. 2011, doi: [10.1088/1367-2630/13/7/073027](https://doi.org/10.1088/1367-2630/13/7/073027). [arXiv:1103.5253](https://arxiv.org/abs/1103.5253). [D]
[975] A. Erhard, G. Jacob, M. Hettrich, P. C. Holz, J. Ulmanis, and T. Feldker, “LYNX - A trapped-ion quantum information processor,” [arXiv:2610.32518](https://arxiv.org/abs/2610.32518), Oct. 2026. [P]
[976] H. Häffner *et al.*, “Robust entanglement,” *Applied Physics B*, vol. 81, no. 2-3, pp. 151–153, Jul. 2005, doi: [10.1007/s00340-005-1917-z](https://doi.org/10.1007/s00340-005-1917-z). [arXiv:quant-ph/0508021](https://arxiv.org/abs/quant-ph/0508021). [D]
[977] U. G. Poschinger *et al.*, “Coherent manipulation of a ⁴⁰Ca⁺ spin qubit in a micro ion trap,” *Journal of Physics B: Atomic, Molecular and Optical Physics*, vol. 42, no. 15, Art. no. 154013, Jul. 2009, doi: [10.1088/0953-4075/42/15/154013](https://doi.org/10.1088/0953-4075/42/15/154013). [arXiv:0902.2826](https://arxiv.org/abs/0902.2826). [D]
[978] C. J. Ballance *et al.*, “Hybrid quantum logic and a test of Bell's inequality using two different atomic isotopes,” *Nature*, vol. 528, no. 7582, pp. 384–386, Dec. 2015, doi: [10.1038/nature16184](https://doi.org/10.1038/nature16184). [arXiv:1505.04014](https://arxiv.org/abs/1505.04014). [D]
[979] J. Hilder *et al.*, “Fault-Tolerant Parity Readout on a Shuttling-Based Trapped-Ion Quantum Computer,” *Phys. Rev. X*, vol. 12, no. 1, Art. no. 011032, Feb. 2022, doi: [10.1103/PhysRevX.12.011032](https://doi.org/10.1103/PhysRevX.12.011032). [arXiv:2107.06368](https://arxiv.org/abs/2107.06368). [D]
[980] T. Faorlin *et al.*, “Entangling Ions with Engineered Light Gradients,” *Phys. Rev. Lett.*, vol. 137, no. 17, Art. no. 170601, Oct. 2026, doi: [10.1103/4smy-6w2n](https://doi.org/10.1103/4smy-6w2n). [arXiv:2603.07548](https://arxiv.org/abs/2603.07548). [D]

