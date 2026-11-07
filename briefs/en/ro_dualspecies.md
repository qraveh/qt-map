---
id: ro_dualspecies
name: Dual-species ancilla readout (a second atomic species measured mid-circuit)
layer: "6 Readout"
status: emerging
since: 2023
one_line: A second atomic species in a co-aligned tweezer array, entangled with the data atoms by an interspecies Rydberg interaction and imaged on its own transition while they keep their coherence; shown with Rb–Cs and Na–Cs.
verdict: Two groups have the isolation and none has the fidelity — 0.82 per data qubit on a four-qubit stabiliser is a protocol, not a readout — and the millisecond camera clock stays; it displaces imaging the data species only when a plaquette readout above 99% appears, or a second species enters a product machine.
updated: 2026-11-07
---

QND = quantum non-demolition (a measurement that leaves the measured state in the eigenstate it reports); SLM = spatial light modulator; C₆ = the van der Waals coefficient of the Rydberg–Rydberg interaction; Förster resonance = a near-degeneracy of two-atom Rydberg pair states that strengthens their interaction.

## Identity & lineage

Measuring one atom of a neutral-atom register while the others keep their coherence is hard because the imaging light that reads the ancilla scatters off every atom of the same species. The dual-species answer is to make the ancilla a different element: its trapping wavelength, its imaging transition and its Rydberg levels are all far from the data species', so the ancilla can be imaged, reloaded and addressed with no light that the data atoms see, and the two are coupled only when a Rydberg pulse is applied to both. The University of Chicago built the platform — a two-dimensional array of individually controlled rubidium and caesium atoms with up to 512 trapping sites and negligible crosstalk, one element reloaded while the other's array is held, so the register has no off-time (Phys. Rev. X 12, 011040, 2022) [D][913] — and then used it twice as a readout: an array of caesium spectator qubits read mid-circuit, with real-time processing and feed-forward, to correct correlated phase errors on the rubidium data qubits (Science 380, 1265, 2023) [D][914]; and, after tuning the Rydberg states near a Förster resonance for a stronger interspecies interaction, an interspecies controlled-phase gate that made a Rb–Cs Bell state and a QND measurement of a rubidium qubit through a caesium ancilla (Nature Physics 20, 1744, 2024) [D][915]. Harvard's Ni group took the next step in 2026 with sodium as the ancilla and caesium as the data: co-localised arrays from two SLMs (Cs at 1064 nm, Na at 616 nm), a sodium atom at the centre of a plaquette of four caesium atoms, and a non-destructive readout of the plaquette's Z stabiliser by one global Rydberg pulse sequence, with no atom rearrangement, at a readout fidelity of 0.82(3) per data qubit [P][916]. A Maryland apparatus adds a third pair, rubidium with ytterbium-174 in co-aligned arrays under two 0.6-NA objectives aligned interferometrically, without gates yet [P][917].

Attributes (technology graph): carrier affinity 0.0 — natural. Characteristic time: none of its own. Readout: camera imaging of the ancilla species, about 0.5–1 ms, non-destructive for the data atoms, mid-circuit. Mobility: none. Control: optical, room temperature. Error structure: loss. Manufacturing: optical and mechanical assembly.

## Physics & limits

Two things the physics gives and one it charges for. The isolation is spectral and complete in principle: sodium's D lines sit at 589 nm, caesium's at 852 and 894 nm, so imaging light for one is hundreds of nanometres from any transition of the other, and the trap light of each is chosen to be magic for its own species and merely a weak, static shift for the other. The coupling is the Rydberg interaction between unlike atoms, which is generally weaker than between like atoms unless a Förster resonance is tuned into (Chicago's method, by electric field) [D][915] or the pulses are designed around it: Harvard measured an interspecies C₆ of 65.7 GHz·µm⁶ against 27.96 GHz·µm⁶ for Cs–Cs and found that the finite interspecies interaction itself spoils the ancilla's phase — a resonant pulse gave a phase of (0.54 ± 0.08)π per data atom instead of π — until the Rabi frequency and detuning are chosen as Δ = V/2 and Ω = √3·V/2, which "completely compensates for the finite interspecies interaction strength" [P][916]. The charge is everything twice: two laser systems, two trap wavelengths, two imaging paths, objectives corrected over both bands [P][917], and an ancilla whose own coherence sets the readout fidelity — on the Harvard plaquette the Ramsey contrast falls exponentially with the number of data qubits, 18% per additional data qubit in |1⟩, because "the single-Na Rydberg Ramsey decoherence during the Cs 2π pulse sets the overall contrast envelope" [P][916]. The clock does not change: the ancilla is still read by a camera, so the millisecond imaging term of the neutral-atom round stays [G:ATOM-IMAGING-CYCLE-2026-09]; what the second species buys is that the data qubits are not in the picture.

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: non-destructive readout of a four-qubit Z stabiliser of caesium data atoms through a sodium ancilla with global pulses only, 0.82(3) per data qubit [P][916]; for a single data qubit, the Chicago QND measurement through a caesium ancilla after an interspecies CZ [D][915]. Typical at scale: none — the largest dual-species register with gates is a plaquette.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2022-02 | Rb–Cs two-dimensional array, up to 512 sites, negligible crosstalk; one species reloaded while the other is held | University of Chicago | [D][913] |
| 2023-06 | Cs spectator qubits read mid-circuit; feed-forward corrects correlated phase errors on Rb data qubits | University of Chicago | [D][914] |
| 2024-09 | Förster-tuned interspecies interaction; interspecies blockade, state transfer, Rb–Cs Bell state by an interspecies CZ; QND measurement of a Rb qubit through a Cs ancilla | University of Chicago | [D][915] |
| 2026-05 | Na ancilla reads the Z stabiliser of a four-Cs plaquette with one global pulse sequence; 0.82(3) per data qubit; interaction-compensated pulse | Harvard | [P][916] |
| 2026-08 | Rb–¹⁷⁴Yb co-aligned arrays under interferometrically aligned 0.6-NA objectives; both species imaged site-resolved; no gates | Joint Quantum Institute / Maryland | [P][917] |
| 2026-09 | Rb–¹⁷¹Yb exchange-assisted CZ, 0.36 µs, 99.91% intrinsic — a simulation | QudeLeap / HKUST (Guangzhou) | [S][918] |

Dominant error term: the ancilla's Ramsey decoherence during the data atoms' Rydberg pulse, then the data pulse's own fidelity (a caesium 2π pulse at 95.1%) [P][916].

## Manufacturing, materials & supply chain

The apparatus is the room-temperature optical assembly of the single-species machine (`fab_optics`) with a second copy of the species-specific parts: a second cooling and trapping laser system, a second tweezer array from its own SLM at its own wavelength, a second imaging path, and objectives that hold two widely separated wavelengths to the same focal plane — the Maryland group's answer is a permanent interferometer that co-aligns two opposing 0.6-NA objectives [P][917]. Sodium's 589 nm needs light that few laser vendors supply at power; ytterbium brings a second oven and a second magneto-optical trap stage. The unit cost of the optical tier is already the largest term of a neutral-atom machine's bill [G:ATOM-OPTICS-UNIT-COST-2026], and the second species roughly doubles the species-specific part of it. Concentration risk is low — the parts are the laser and optics market's — and know-how high: three university groups. Export-control exposure is the lasers' and the apparatus' [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

The readout is a camera image of the ancilla species, taken while the data species sits in the dark, and so it inherits camera imaging's clock: the neutral-atom round is 1–4.5 ms, of which imaging is 0.5–1 ms [G:ATOM-IMAGING-CYCLE-2026-09]; adaptive fast readout has brought single-species imaging to a 15 µs average probe time on a 25-site subarray [G:USTC-FASTREADOUT-2026-08], and a second species can use the same cameras and the same tricks. The control burden is the Rydberg pulse design: global pulses on both species with the interaction-compensating detuning, or Förster tuning by electric field, plus the feed-forward path from the camera to the data qubits' controls, which Chicago closed in sequence in 2023 [D][914]. Nothing here scales worse than the single-species machine; everything is one more laser rack.

## Role in the stack

Architectures: an alternate readout on the rubidium/caesium tweezer array (`atom_rb`) and on the alkaline-earth array (`atom_ae`), where the ancilla may be the alkali and the data the ytterbium or strontium clock qubit, or the reverse. It requires an alkali or an alkaline-earth(-like) carrier as the second species, camera imaging (`ro_img`) for the ancilla and a second laser system in the optical assembly (`fab_optics`); it is an alternative to imaging the data species itself. It serves every code that needs mid-circuit stabiliser readout on atoms — the surface code and the high-rate codes on `atom_rb` — and it is the neutral-atom analogue of what the second species already does in trapped ions (sympathetic cooling and ancilla readout by a second ion species, in `ion_qccd`'s machines). It competes with the erasure check on alkaline-earth atoms (`ro_erasure`), which detects leakage without an ancilla, and with cavity readout (`ro_cavity`), which gives speed rather than isolation. The register's dual-isotope machine is a cousin: two isotopes of rubidium, not two elements. Price of switching: a second species' lasers and traps and a weaker, tuned interspecies gate; gained: an ancilla that can be imaged, reset and reloaded with no light the data atoms see.

## Evidence — how the numbers were measured

Harvard's 0.82(3) is the per-data-qubit readout fidelity extracted from the exponential decay of the sodium Ramsey contrast with the number of caesium data atoms in |1⟩; the parity is read from the fringe at a fixed phase, and non-destructive means the caesium atoms are neither transported nor imaged during the measurement — the paper's visible text gives a caesium imaging survival of 97.4% between successive images but no direct data-qubit survival after the stabiliser readout, and no sodium-imaging crosstalk figure on caesium [P][916]. Chicago's Bell-state, gate and QND fidelities are in the body of the Nature Physics paper, not in its abstract, and are not quoted in this record [D][915]; the 2023 Science result is a demonstration of correction, with the improvement in coherence stated in the paper's figures rather than its abstract [D][914]. The 99.91% Rb–Yb gate is a computed, loss-aware average gate fidelity from a multichannel model — "the full multichannel model predicts an intrinsic gate fidelity of 99.91%" — not a measurement, and the abstract's "we demonstrate" is the language of simulation [S][918]. Value conflict: none between the hardware papers; the one to avoid is reading the simulated 99.91% as a hardware result. Not published: a dual-species stabiliser readout above 90%, a repeated-round experiment, any dual-species register larger than a plaquette with gates.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| University of Chicago (Bernien) | research | US | Rb–Cs platform; spectator readout with feed-forward; interspecies CZ and QND readout | [D][913], [914], [915] |
| Harvard University (Ni, Yao) | research | US | Na–Cs plaquette stabiliser readout with global pulses | [P][916] |
| Joint Quantum Institute / University of Maryland | research | US | Rb–Yb dual-species apparatus | [P][917] |
| QudeLeap Research / HKUST (Guangzhou) | developer / research | CN | Rb–Yb interspecies gate design (simulation) | [S][918] |
| Google Quantum AI | developer | US | A neutral-atom hardware track since 2026-03, species not stated | [G:GOOGLE-ATOMS-2026-03] |

**Money.** No dated money is attached to dual-species readout. The neutral-atom companies' rounds — QuEra's $230 M+ [G:QUERA-230M-2025], Atom Computing's >$300 M [G:ATOM-300M-2026-06], Pasqal's ~$360 M through its listing [G:PASQAL-SPAC-2026-08] — fund single-species machines.

**Market & supply chain.** No product machine runs two species; every register machine on the two atom paths is single-species, and QuEra, Pasqal, Infleqtion and Atom Computing each build on one element. The technology's market is the laser market's second rack.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** No vendor roadmap names a second species. The academic record is steady: Chicago's three papers over 2022–2024 each delivered what the previous one promised, and Harvard's plaquette readout is the first stabiliser-level result.

**Strategic reading.** The technology answers the neutral-atom platform's measurement problem by isolation rather than speed, and it is the one route on which the ancilla can be continuously reloaded without touching the data. If a vendor adopts a second species, it will be for error correction's sake, and the choice of pair (alkali–alkali for simplicity, alkali–alkaline-earth for the clock qubit's coherence) will shape the next generation of machines; if none does, it remains the academic groups' tool.

## Outlook & open questions

Confirm within 12–24 months if a dual-species stabiliser readout reaches 99% per data qubit, if repeated rounds of ancilla readout and reload run on a code, or if a company announces a two-species machine. Demote if by 2028 the readout stays below 95% or the platforms stay at plaquette scale. Best case by 2029: a product machine with an alkali ancilla array over an alkaline-earth data array; worst case: a method of three laboratories.

Open questions: (1) does interspecies gate fidelity reach the 99.5% of same-species gates with Förster tuning or compensated pulses? (2) does the ancilla's Ramsey coherence hold over a six- or eight-body stabiliser? (3) which pair — Rb–Cs, Na–Cs, Rb–Yb — wins on laser cost and gate strength? (4) can the ancilla's camera readout be replaced by a cavity to recover the clock? (5) does any vendor commit?

## References

[913] K. Singh, S. Anand, A. Pocklington, J. T. Kemp, and H. Bernien, “A dual-element, two-dimensional atom array with continuous-mode operation,” *Phys. Rev. X*, vol. 12, no. 1, Art. no. 011040, Feb. 2022, doi: [10.1103/PhysRevX.12.011040](https://doi.org/10.1103/PhysRevX.12.011040). [arXiv:2110.05515](https://arxiv.org/abs/2110.05515). [D]
[914] K. Singh, C. E. Bradley, S. Anand, V. Ramesh, R. White, and H. Bernien, “Mid-circuit correction of correlated phase errors using an array of spectator qubits,” *Science*, vol. 380, no. 6651, pp. 1265–1269, Jun. 2023, doi: [10.1126/science.ade5337](https://doi.org/10.1126/science.ade5337). [arXiv:2208.11716](https://arxiv.org/abs/2208.11716). [D]
[915] S. Anand, C. E. Bradley, R. White, V. Ramesh, K. Singh, and H. Bernien, “A dual-species Rydberg array,” *Nat. Phys.*, vol. 20, no. 11, pp. 1744–1750, Sep. 2024, doi: [10.1038/s41567-024-02638-2](https://doi.org/10.1038/s41567-024-02638-2). [arXiv:2401.10325](https://arxiv.org/abs/2401.10325). [D]
[916] Y. Wang *et al.*, “Multi-qubit stabilizer readout on a dual-species Rydberg array,” [arXiv:2605.10924](https://arxiv.org/abs/2605.10924), May 2026. [P]
[917] K. Weber *et al.*, “Dual-species alkali and alkaline-earth-like optical tweezer arrays via interferometrically aligned high-NA objectives,” [arXiv:2608.13646](https://arxiv.org/abs/2608.13646), Aug. 2026. [P]
[918] H. Wang, E. Huang, M. Jing, H. Yao, X. Wang, and J. Liu, “An exchange-assisted entangling gate between 87Rb and 171Yb Rydberg atoms,” [arXiv:2609.11730](https://arxiv.org/abs/2609.11730), Sep. 2026. [S]

