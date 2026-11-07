---
id: ro_cavity
name: Cavity-based mid-circuit readout of tweezer atoms
layer: "6 Readout"
status: emerging
since: 2022
one_line: Tweezer atoms at the antinodes of a high-finesse cavity send their fluorescence into one mode, counted in tens of microseconds while light shifts protect the neighbours — a mid-circuit readout ten times faster than the camera.
verdict: The only neutral-atom readout measured below 100 µs with the rest of the register coherent, but on five atoms, with 8% loss and no gate in the same apparatus; it displaces camera imaging only if a cavity array reads tens of qubits per cycle at the 99.9% the single-atom result shows.
updated: 2026-11-07
---

C = cooperativity, 4g²/κγ — the ratio of an atom's scattering into the cavity mode to its scattering into free space; SPCM = single-photon counting module; AOD = acousto-optic deflector; Purcell enhancement = the faster emission of an atom whose transition is resonant with a cavity mode.

## Identity & lineage

A camera collects the fluorescence of a tweezer atom over a solid angle of a fraction of a steradian and needs hundreds of microseconds to a millisecond to tell bright from dark; an optical cavity around the atom collects a large fraction of the same photons into one mode and sends them to a photon counter, so the same decision takes tens of microseconds. Cavity readout of single atoms is old cavity-QED physics; its use on a tweezer array began at Berkeley in 2022, where a strongly coupled cavity read one ⁸⁷Rb atom of a small tweezer array in tens of microseconds at about 0.5% state-preparation-and-measurement infidelity and about 1% loss, with no observable hyperfine decoherence on a second atom tens of microns away (Phys. Rev. Lett. 129, 203602) [D][919]. The 2026 result that makes it a readout technology rather than a demonstration is the same group's mid-circuit measurement and feed-forward on a register: five ⁸⁷Rb atoms 19.5 µm apart on the antinodes of a near-concentric Fabry–Pérot cavity (cooperativity 3.0), acousto-optic deflectors steering the probe to one atom at a time and a 1529 nm shielding beam that light-shifts the unmeasured atoms out of resonance; four qubits measured mid-circuit at 0.9 (+0.4/−0.3)% bright-state and 0.2 (+0.4/−0.2)% dark-state infidelity in 40 µs windows, the fifth qubit's coherence reduced by under 2%, and a measurement-and-feed-forward cycle of 45 µs — against a field in which "mid-circuit measurement-and-feedforward cycle times have remained slow, typically exceeding 1 ms" [P][920]. Tsinghua and the Beijing Academy of Quantum Information Sciences showed the other end of the design space: a millimetre-scale cavity of cooperativity 125 ± 13 holding up to 21 individually trapped ⁸⁷Rb atoms, with a hyperfine-state readout of one atom at 99.925 (+15/−18)% in a 4 µs window and 99.996% survival [P][921]; and Berkeley coupled a Rydberg array to a high-cooperativity cavity, suppressing the electric fields of the cavity actuators to about 3 mV/cm rms and reading the ground–Rydberg basis by Purcell-enhanced fluorescence in 7.5 µs at 3% and 5% infidelity [P][922].

Attributes (technology graph): carrier affinity 0.0 — natural. Characteristic time: none of its own. Readout: fluorescence into the cavity mode, counted by a single-photon counter, about 40 µs per atom (4 µs for one atom at high cooperativity), non-destructive, mid-circuit. Mobility: none. Control: optical, room temperature. Error structure: loss. Manufacturing: optical and mechanical assembly.

## Physics & limits

The readout time is the time to collect enough photons to decide, and the cavity multiplies the collection rate by its cooperativity: at C = 3 Berkeley needed a 40 µs window and found a mean bright-state detection time of 9.5 µs once an adaptive gate shut the probe after two photons [P][920]; at C = 125 Tsinghua decided in 4 µs [P][921]. Three limits are physical. Recoil: every scattered photon heats the atom, so the bright-state readout is limited by "recoil-induced mechanical effects and early-time depumping" and a long probe loses the atom — 95% loss without adaptive gating, 8% with it [P][920]. Serialisation: one cavity mode reads one atom at a time, 40 µs plus 20 µs of switching per atom, so a register of a hundred qubits would take milliseconds unless many cavities or many modes read in parallel. Electric fields: the mirrors and their actuators sit close to the atoms, and a Rydberg gate in the same apparatus needs those fields nulled, which Berkeley did to 3 mV/cm [P][922]. The measurement also shifts the unmeasured qubits' phase in proportion to the photon time in the cavity — 0.020(2) rad/µs, reduced to 0.002(2) rad/µs by feeding the measured photon count forward to the final pulse's phase [P][920]. What the physics does not limit is the gain over imaging: the camera term of the neutral-atom round is 0.5–1 ms of a 1–4.5 ms cycle [G:ATOM-IMAGING-CYCLE-2026-09], and the cavity brings its own term to tens of microseconds.

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: four of five rubidium qubits measured mid-circuit at sub-percent infidelity in 40 µs windows with a 45 µs measurement-and-feed-forward cycle and under 2% coherence loss on the unmeasured qubit [P][920]; for one atom, 99.925% in 4 µs with 99.996% survival in a cavity of cooperativity 125 [P][921]. Typical at scale: none — 21 atoms is the largest register in a cavity, and it was not read mid-circuit.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2022-11 | One ⁸⁷Rb atom of a tweezer array read in a cavity in tens of µs, ~0.5% SPAM infidelity, ~1% loss; no decoherence on a neighbour tens of µm away | UC Berkeley | [D][919] |
| 2026-06 | Five Rb atoms on cavity antinodes (C = 3.0); four measured mid-circuit, 0.9% / 0.2% infidelity, 40 µs windows; 45 µs measurement-and-feed-forward cycle; < 2% coherence loss on the fifth | UC Berkeley | [P][920] |
| 2026-07 | 21 Rb atoms in a cavity of cooperativity 125 ± 13; one-atom hyperfine readout 99.925% in 4 µs, survival 99.996% | Tsinghua / BAQIS | [P][921] |
| 2026-10 | Rydberg array in a high-cooperativity cavity: 3 mV/cm rms residual field; ground–Rydberg readout in 7.5 µs at 3% / 5% infidelity | UC Berkeley | [P][922] |

Dominant error term: recoil heating and depumping during the probe (bright-state infidelity and loss); the whole sequence of about 300 µs is then limited by slow microwave pulses, not by the readout [P][920].

## Manufacturing, materials & supply chain

The addition to the room-temperature optical assembly (`fab_optics`) is the cavity: two concave mirrors in vacuum with a mode waist of a few microns at the atoms, a servo on the cavity length, and single-photon counters on the output. Tsinghua's contribution is a fabrication method — mechanical shaping plus CO₂-laser polishing of fused-silica mirrors with sub-millimetre radii of curvature (0.99 mm) and very low roughness, giving a 1.67 mm cavity with a 9.5 µm waist, a finesse of about 9.5 × 10⁴ and a linewidth of 0.94 MHz [P][921]; Berkeley's is a near-concentric cavity with the atoms spaced 25 wavelengths apart on its antinodes [P][920]. Mirror coatings at this finesse come from a handful of suppliers and are the one concentrated input; everything else is the tweezer machine's. No product uses it. Export-control exposure is the apparatus' [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

The readout chain is a probe laser steered by AODs, a shielding beam steered the same way, a photon counter and a fast decision: the Berkeley loop programmes the next step in 5 µs and measures in 40 µs, and its feed-forward demonstrations — adaptive state discrimination at 81(2)% against 69–73% for fixed schemes, conditional state preparation at 85(2)% against 72–78% — are real-time classical control at the microsecond scale, which the camera route has never offered [P][920]. The burden grows with the register as one probe channel and one shielding channel per atom read in sequence; parallel readout needs several cavity modes or several cavities, none demonstrated. The competing route inside camera imaging — adaptive probing at a 15 µs average on a 25-site subarray [G:USTC-FASTREADOUT-2026-08] — reads many atoms at once and closes part of the gap without a cavity.

## Role in the stack

Architectures: an alternate readout on the rubidium/caesium array (`atom_rb`) and on the alkaline-earth array (`atom_ae`), where the clock transition's narrow linewidth changes the cavity design. It requires the atomic carrier and a high-finesse cavity in the optical assembly (`fab_optics`); it is an alternative to camera imaging (`ro_img`); and it is the same hardware as the atom–photon interface (`ic_atomcavity`), the MPQ cavities that collect an atom's photon for a network link, used here to collect the same photon for a decision. It serves the codes on both paths that need fast syndrome extraction and the derived clock of the neutral-atom round, whose imaging term it replaces by a tens-of-microseconds term — leaving the transport and the microwave pulses, which the Berkeley sequence shows at about 300 µs. It competes with the dual-species ancilla (`ro_dualspecies`), which buys isolation rather than speed, and with the erasure check (`ro_erasure`) on alkaline-earth atoms. Price of switching: a cavity in the chamber, nulled fields for Rydberg gates and serial readout; gained: a sub-100 µs measurement-and-feed-forward cycle.

## Evidence — how the numbers were measured

Berkeley's infidelities are per-atom averages over the array with a two-photon threshold, with asymmetric uncertainties from the counting statistics; the state-preserving fidelity of the unmeasured qubit is a Ramsey measurement, 100(2)% at maximum shielding; the 45 µs cycle is 5 µs of programming plus the 40 µs window, and the whole sequence of about 300 µs is dominated by microwave pulses at low Rabi frequency [P][920]. Tsinghua's 99.925% is the hyperfine-state readout of a single atom probed through the cavity's transmission, repeated over 20 cycles with recooling and optical pumping between them, with a final fluorescence image for survival — a readout fidelity, not a mid-circuit measurement inside a computation, and no two-qubit gate was shown in the same apparatus [P][921]. The 7.5 µs Rydberg-basis readout and its 3% and 5% infidelities are as the abstract states them [P][922]. Value conflict: the 99.925% and the 0.9% are not the same measurement — one atom through transmission at C = 125 against four atoms by fluorescence at C = 3 — and should not be compared as a progression. Not published: a cavity readout combined with a Rydberg gate on the same atoms, a parallel readout of several atoms, a run on more than five qubits.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| UC Berkeley / Lawrence Berkeley National Laboratory / Columbia (Stamper-Kurn) | research | US | Single-atom cavity readout (2022); five-atom mid-circuit measurement and feed-forward; Rydberg array in a cavity | [D][919][P][920], [922] |
| Tsinghua University / BAQIS (Chen) | research | CN | 21 atoms in a cooperativity-125 cavity; 99.925% readout in 4 µs; mirror fabrication | [P][921] |
| Max Planck Institute of Quantum Optics | research | DE | The atom–cavity interface as a network link (`ic_atomcavity`) | — |
| Atom Computing / Nu Quantum | developer | US/UK | Cavity networking of atom arrays by MoU — the interconnect use, not readout | [G:ATOM-NUQUANTUM-2026-06] |

**Money.** No dated money is attached to cavity readout. The Berkeley work is funded by AFOSR, ARO, DARPA, the NSF Challenge Institute for Quantum Computation and the Department of Energy, by the paper's acknowledgements [P][920].

**Market & supply chain.** No product reads its atoms through a cavity; the cavity makers are the mirror-coating houses and the groups themselves. If adopted, the technology ties the readout to the interconnect hardware the vendors are already buying for networking.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** No vendor roadmap names cavity readout; the academic record is Berkeley's, 2022 to 2026, each paper delivering the next step of the one before. The authors' outlook names "higher-cooperativity cavities" and "Rydberg quantum processors that are rapidly monitored and stabilized through cavity-based measurement" [P][920].

**Strategic reading.** The neutral-atom platform's round is set by imaging, and this is the one route that changes the imaging term by an order of magnitude rather than a factor of two. Whoever combines a cavity with Rydberg gates on the same atoms at the Tsinghua fidelity owns the fast neutral-atom syndrome cycle; the vendors' cavity purchases for networking put the hardware within reach, and the serialisation problem decides whether it scales.

## Outlook & open questions

Confirm within 12–24 months if a Rydberg gate and a cavity readout run on the same register, if a cavity reads several atoms in parallel, or if a mid-circuit readout above 99% is shown on more than five qubits. Demote if by 2028 no register beyond a handful of atoms is read this way, or if fast camera imaging closes the gap to within a factor of two. Best case by 2029: a neutral-atom machine whose syndrome round is set by the gate, not the camera; worst case: a two-laboratory technique that the camera caught up with.

Open questions: (1) can several atoms be read in one cavity mode at once, by frequency or by polarisation? (2) does the 8% loss fall to the 10⁻³ a code needs? (3) do the cavity's fields and the Rydberg gate coexist at 99.5% gate fidelity? (4) which species — Rb, Yb, Sr — gets the first cavity-read logical qubit? (5) does the interconnect hardware the vendors are buying become the readout too?

## References

[919] E. Deist *et al.*, “Mid-circuit cavity measurement in a neutral atom array,” *Phys. Rev. Lett.*, vol. 129, no. 20, Art. no. 203602, Nov. 2022, doi: [10.1103/PhysRevLett.129.203602](https://doi.org/10.1103/PhysRevLett.129.203602). [arXiv:2205.14138](https://arxiv.org/abs/2205.14138). [D]
[920] T.-C. Lee *et al.*, “Rapid cavity-based mid-circuit measurement and feedforward in a neutral atom array,” [arXiv:2606.24869](https://arxiv.org/abs/2606.24869), Jun. 2026. [P]
[921] J. Ye *et al.*, “Controlling atom array in an ultra-high-cooperativity optical cavity,” [arXiv:2607.04090](https://arxiv.org/abs/2607.04090), Jul. 2026. [P]
[922] T. Xiang *et al.*, “A Rydberg atom array coupled to a high-cooperativity optical cavity,” [arXiv:2610.20889](https://arxiv.org/abs/2610.20889), Oct. 2026. [P]

