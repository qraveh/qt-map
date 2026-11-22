---
id: fab_qphard
name: Quasiparticle and radiation hardening of superconducting circuits (gap engineering, phonon traps, event detectors)
layer: "10 Manufacturing"
status: demonstrated
since: 2022
one_line: "Changes to the superconducting-qubit process that keep impact-generated quasiparticles away from the junctions — thin–thick junction leads, low-gap traps, high-gap base layers, back-side metal — and detectors that flag the impacts; six strongly gap-engineered qubits showed none of the 154 bursts their weakly engineered neighbours saw in 6,000 s."
verdict: "Real and in use: gap-engineered junctions took out of Google's 72-qubit processor the impact bursts that came every ten seconds on its predecessor, and back-side copper cut correlated poisoning a hundredfold on a three-qubit test. A second vendor's burst-free long code would confirm it; demote the detector half — one laboratory, one measured qubit — if no detector flag reaches a decoder by 2028."
updated: 2026-11-22
---

QP = quasiparticle; GE = gap-engineered; Δ = the superconducting gap, δΔ = its difference across a junction; MKID = microwave kinetic inductance detector; RReCS = rapid repetitive correlated sampling; x_qp = QP density as a fraction of the Cooper-pair density; SPAM = state preparation and measurement; TLS = two-level-system defect; Λ = error-suppression factor per code-distance step; SFQ = single flux quantum (superconducting digital logic); DAC = digital-to-analogue converter; LLNL = Lawrence Livermore National Laboratory.

## Identity & lineage

A high-energy particle crossing a superconducting-qubit chip — a cosmic-ray muon, or a gamma ray from trace radioactivity — deposits up to 1 MeV in the substrate [D][290]; the phonons it radiates break Cooper pairs across the chip, and the QPs that tunnel through the Josephson junctions absorb the qubits' energy. On 26 qubits of a Google Sycamore processor such impacts arrived on average every 10 s, drove the count of simultaneous decay errors from about 4 to about 24 — the whole patch — and decayed over 25–30 ms, tens of thousands of error-correction cycles [D][289]; in repetition codes they set a logical floor near 10⁻⁶ [D][1]. This technology is the set of process changes that make the chip indifferent to such events, and the detectors that report them: gap engineering, which turns the junction's thin lead into a barrier QPs cannot climb; low-gap traps and bandages that collect QPs away from the junctions; back-side normal metal that downconverts phonons below the pair-breaking energy; high-gap base layers; and detectors that time-stamp impacts for the control system.

Gap engineering is two decades old — the Chalmers group's lineage of it opens with a 2004 Phys. Rev. Lett. by Aumentado, Keller, Martinis and Devoret [P][939]; Yale's 2012 transmon combined oxygen-doped aluminium junction electrodes with clean aluminium as QP traps and found T1 insensitive to the change [D][940] — single devices. Multi-qubit hardware followed in October 2022 from Syracuse University and the University of Wisconsin–Madison: 10 µm electroplated copper islands on the back side downconverted 95% of injected phonons and, on three qubits per chip monitored simultaneously, cut correlated QP poisoning by two orders of magnitude (Nat. Commun. 13, 6425) [D][941]. In December 2024 Google showed on a 12-qubit checkerboard that strongly gap-engineered qubits saw none of the impact bursts their weakly engineered neighbours did (Phys. Rev. Lett. 133, 240601) [D][290], and credited "gap-engineered Josephson junctions" with removing impact failures from its 72-qubit processor [D][1]. MIT reported (published 2025) that the gap landscape around the junction changes the recovery after a correlated event from about 6 ms to 0.7–0.8 ms in a 10-qubit array (Nat. Commun. 16, 6428) [D][942]. Two works of autumn 2026 extend it: Chalmers carries the landscape beyond the junction with a gold-capped niobium island and low-gap aluminium bandages [P][939], and Lawrence Livermore sandwiches a six-qubit chip between two MKID arrays whose event triggers launch the qubit measurement, events seen by both arrays being read as penetrating (Phys. Rev. Applied 26, 044052) [D][943].

Attributes (technology graph): carrier affinity 1.0 — fabricated. Characteristic time: none. Readout: none of its own — the event detector reads radiation, not qubits. Mobility: none. Control modality: none of its own, placed at none; the detector's microwave readout shares the qubits' controller. Error structure: correlated bursts — the one it suppresses. Manufacturing: superconducting lithography, with thin-film, back-side and detector steps added.

## Physics & limits

A QP near the gap edge can tunnel across a junction and take the qubit's energy only if the gap on the far side exceeds the near side's by less than hf_q. Aluminium's gap rises as the film thins — the empirical model Google uses is Δ = Δ_bulk + A/t with Δ_bulk = 180 µeV and A = 900 µeV·nm — so a junction with one thin and one thick lead is a step: 30 nm against 100 nm targets about 5 GHz, below the 7–7.3 GHz maximum qubit frequency ("weak"); 15 nm against 100 nm targets about 12 GHz, above it ("strong") [D][290]. Strongly engineered qubits held under flood illumination until x_qp ≃ 6×10⁻⁵, above the ≃ 10⁻⁵ of a large impact [D][290]. The step holds only while the thin lead is the highest-gap metal of the qubit: niobium or tantalum capacitor pads would let QPs flow straight into it [D][290]. Chalmers' design answers that: a 150 nm sputtered niobium island and ground plane (Δ/h ∼ 360 GHz) capped in situ by 10 nm of gold, joined to 18 nm / 100 nm aluminium junction leads (estimated δΔ ≈ 40 µeV, δΔ/h ≈ 10 GHz) through 300 nm aluminium bandages whose lower gap collects the QPs [P][939].

Three limits survive. Gap engineering stops QP-induced relaxation, not QP-induced frequency shifts: QPs near a junction still reduce its supercurrent, so a burst can dephase a qubit it no longer flips [P][939] — Google's strongly engineered qubits shifted in frequency as the square root of the optical power [D][290], and Chalmers' protected device showed dephasing and SPAM infidelity rising with light while T1 held [P][939]. Impacts also scramble TLS defects, which gap engineering "does not address" [D][290]. And phonon downconversion pays in volume: Martinis' estimate, as Iaia et al. state it, put a 100-fold T1 gain after an impact at 6 µm of normal metal, while copper continuous over the back side would damp the qubits through a transmission-line mode — hence islands of (200 µm)², 10 µm thick [D][941].

## Engineering state of the art

Best demonstrated as of 22 Nov 2026: no impact burst on six strongly gap-engineered qubits in 6,000 s, against 154 on their six weakly engineered neighbours [D][290]; a distance-29 repetition code on a gap-engineered 72-qubit processor, Λ = 8.4 ± 0.1, far below the old 10⁻⁶ floor down to an apparent 10⁻¹⁰ [D][1]. Typical at scale: Google's processors; SEEQC's SFQ-controlled module also states gap-engineered qubit junctions [D][304].

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2012 | Bandgap-engineered transmon: oxygen-doped Al junction electrodes, clean Al traps; T1 insensitive to the change | Yale | [D][940] |
| 2021-12 | The problem measured: impact bursts every 10 s on 26 Sycamore qubits, 25–30 ms recovery | Google | [D][289] |
| 2022-10 | Back-side 10 µm Cu islands: 95% of injected phonons downconverted, correlated poisoning down two orders, three qubits per chip | Syracuse U. / UW–Madison | [D][941] |
| 2024-12 | 12-qubit checkerboard: 0 bursts on strongly GE qubits (15/100 nm leads) vs 154 on weakly GE (30/100 nm) in 6,000 s | Google | [D][290] |
| 2024-12 | Gap-engineered 72-qubit processor: d = 29 repetition code, Λ = 8.4 ± 0.1, floor 10⁻¹⁰ from bursts of another kind about once an hour | Google | [D][1] |
| 2025-07 | 10-qubit array: cosmic rays cause 17.1 ± 1.3% of correlated events; junction placement cuts recovery from ~6 ms to 0.7–0.8 ms | MIT / MIT Lincoln Laboratory | [D][942] |
| 2026-10 | Nb/Au island, Al bandages, 18/100 nm leads: no excess relaxation up to 10 nW at 1550 nm; all-Al onset above 0.1 nW | Chalmers | [P][939] |
| 2026-10 | Two MKID arrays sandwiching a 6-qubit chip: 8σ trigger, penetrating events ~25% of all, T1 and T2 down by up to 30.5% after them | LLNL | [D][943] |

Dominant error term: what hardening leaves — six bursts in 2×10¹⁰ cycles on the gap-engineered processor, decaying in about 400 µs over neighbourhoods of about 30 qubits, whose cause Google does "not yet understand" [D][1]; and the QP dephasing that junction gap engineering does not stop [P][939].

## Manufacturing, materials & supply chain

Gap engineering at the junction is a deposition recipe: by Google's account it "requires no additional fabrication complexity, only requiring modified deposition of aluminum"; the test chip carried both variants, made in two sequential lithography steps [D][290]. Its floor is film control — Chalmers stays at 18 nm or thicker "because of fabrication reproducibility and the need for the junction leads to withstand ion milling" [P][939]. The landscape beyond the junction costs more steps: sputtered niobium, an in-situ gold cap against the lossy native oxide, ion milling of the gold at the contacts, evaporated aluminium bandages [P][939]. Back-side downconversion asks for double-side-polished wafers, a Ti/Cu seed, electroplated copper grown at about 3.3 µm/h, and a lattice of dicing-saw cuts 20 µm into the silicon [D][941]. The detector is a separate chip: nine (later 25) MKIDs of 20 nm aluminium on 20 × 20 × 0.65 mm sapphire, each chip in its own gold-plated copper box, the three boxes stacked on one bracket at the mixing chamber [D][943]. Nothing is scarce; the know-how sits with Google and a handful of laboratories. Export-control exposure is that of the processor it hardens [G:BIS-QUANTUM-ECCN-2024-09].

## Control, readout & I/O burden

Hardening adds no line. The detector adds one feedline per array — nine resonances within about 200 MHz, inside one DAC channel — and its own measurement chain, isolated from the qubits' by more than 50 dB; the controller watches the arrays continuously, triggers at eight standard deviations of each resonator's noise, records a 15 µs buffer and a 700 µs window, and launches the qubit measurement with 10–15 µs latency [D][943]. That latency is nine to fourteen cycles of a processor with a 1.1 µs cycle [D][1] — enough to flag a burst lasting milliseconds, not to stop the cycle in which it lands. No published work found feeds a detector flag to a decoder; MIT names the route — sensors in qubit arrays "to flag that an error may have occurred" [D][942].

## Role in the stack

Architectures: a manufacturing technology on the transmon lattice (`sc`), beside `fab_sc` and `fab_cmos`. It requires the superconducting-qubit process (`fab_sc`) and refines it — the same junction lithography with other lead thicknesses, bandages, caps and back-side metal — rather than replacing it. It serves the transmon (`transmon`), whose error structure carries the burst channel, and through it the codes and decoders that assume independent errors (`code_surface`, `dec_mwpm`, `dec_fpga`): Google's repetition code passed its old 10⁻⁶ floor once impact bursts were gone [D][1]. Every measurement read is on transmons, so the fluxonium (`fluxonium`) and the bosonic, dual-rail and annealing architectures do not carry it yet. It bears on two conflict edges of the map without settling them. SFQ control (`ct_sfq`) poisons transmons with photons above the aluminium gap, and gap engineering is among that edge's listed mitigations: SEEQC's five-qubit module drives gap-engineered transmons with SFQ pulses and saw no noticeable T1 change on its centre qubit after up to 50 µs of off-resonant clocking, which the authors attribute to the junctions' gap engineering together with aluminium in the bump bonds as a quasiparticle trap and an SFQ pulse shaped to carry less spectral content above 100 GHz — three mitigations at once, none isolated [D][304]. The transducer's optical pump (`ic_transducer`) breaks Cooper pairs; Chalmers' device stood more than an order of magnitude more light, in a package built as the worst case and at powers the authors call low against what transducers need [P][939]. Price of switching: thinner leads and, beyond the junction, a few process steps; gained: a repetition-code floor four orders of magnitude lower.

## Evidence — how the numbers were measured

Google's burst counts are RReCS — every qubit prepared in |1⟩, idled 1 µs and measured every 100 µs, in 100 datasets of 60 s — with events found by a matched filter and compared with an independent-error model from each qubit's T1 and readout [D][290]. The repetition-code floor comes from 2×10¹⁰ cycles in 5.5 h, with the lower distances subsampled from the d = 29 data [D][1]. Iaia et al.'s factor of 20 is a pump–probe figure — phonons injected by biased junctions at the chip edge — while the two orders are coincidences of charge-parity switches on three qubits over several days, without injection [D][941]. Chalmers compares two single-qubit chips, one per package, under continuous 1550 nm light in reflective copper boxes; its thresholds are package-specific, and a light-absorbing coating raised the threshold about a hundredfold in a proof of concept [P][939]. LLNL states reductions in T1 and T2 of up to 30.5%; what it measured is the single-shot excited-state population at one delay, averaged over more than 1,000 dual-event shots on one qubit of the six [D][943]. Value conflict: Chalmers' abstract says "more than an order of magnitude"; its onsets, above 0.1 nW for aluminium and none up to 10 nW for niobium, span two decades — both are given here. Back-side phonon downconversion is Iaia et al.'s, not part of the Chalmers device. The once-an-hour bursts on the gap-engineered 72-qubit processor are, by Google's account, "different from previously observed high-energy impact events" [D][1]. Not published in what was read: burst statistics from any other vendor; the junction recipe of Google's 105-qubit processor; a decoder that uses detector flags.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| Google Quantum AI | developer | US | Gap-engineered junctions in its processors; the 12-qubit test and the 72-qubit repetition code | [D][290], [1] |
| Syracuse University / University of Wisconsin–Madison (Plourde, McDermott) | research | US | Back-side copper phonon downconversion on multi-qubit chips | [D][941] |
| MIT / MIT Lincoln Laboratory (Oliver, Formaggio) | research | US | Cosmic-ray coincidence timing; the gap landscape at the junction | [D][942] |
| Lawrence Livermore National Laboratory (Rosen, DuBois) | research | US | MKID arrays sandwiching a qubit chip | [D][943] |
| Chalmers University of Technology (Van Laer, Delsing, Gasparinetti) | research | SE | Niobium/gold landscape for qubits near optical fields | [P][939] |
| Yale University (Schoelkopf, Devoret) | research | US | The 2012 bandgap-engineered transmon | [D][940] |
| SEEQC | developer | US | Gap-engineered qubit junctions and aluminium bump traps in its SFQ-controlled module | [D][304] |

**Money.** No dated money is attached to this technology; the work sits inside vendor and laboratory programmes, LLNL's under its Department of Energy operating contract [D][943].

**Market & supply chain.** Nothing to buy: a recipe, an electroplating step and an MKID chip; value accrues to whoever solves the residual bursts, not to a supplier.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** Google's Phys. Rev. Lett. paper said strong gap engineering "removes high-energy impact events as a roadblock" [D][290]; its processor paper delivered the impact half and found the next floor [D][1]. No vendor roadmap found names an event detector.

**Strategic reading.** Hardening is cheap enough to become default and will not differentiate anyone for long; the next floor will — the vendor that explains the once-an-hour bursts, or turns detector flags into erasure-like information for its decoder, moves it. Groups that need optics or SFQ beside transmons need the landscape beyond the junction more than the junction step.

## Outlook & open questions

Confirm within 12–24 months if a second vendor publishes a long repetition code or burst sampling free of impact bursts, or if a detector flag enters a real-time decoder. Demote if the residual bursts prove QP-mediated through a path gap engineering cannot block, or if the niobium/gold landscape loses coherence at processor scale. Best case by 2029: the 10⁻¹⁰ floor explained and removed, detector flags used as erasures; worst case: a floor of unknown origin where the impact bursts were, and QP dephasing as the new correlated channel.

Open questions: (1) what causes the once-an-hour, 400 µs bursts on a gap-engineered processor? (2) how large is QP-induced dephasing during a burst, per surface-code cycle? (3) does the barrier survive niobium or tantalum pads at processor scale? (4) can a detector's flag reach the decoder within a few cycles? (5) how much optical power does a protected qubit stand in a package built for a transducer?

## References

[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[289] M. McEwen *et al.*, “Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits,” *Nat. Phys.*, vol. 18, no. 1, pp. 107–111, Dec. 2021, doi: [10.1038/s41567-021-01432-8](https://doi.org/10.1038/s41567-021-01432-8). [arXiv:2104.05219](https://arxiv.org/abs/2104.05219). [D]
[290] M. McEwen *et al.*, “Resisting High-Energy Impact Events through Gap Engineering in Superconducting Qubit Arrays,” *Phys. Rev. Lett.*, vol. 133, no. 24, Art. no. 240601, Dec. 2024, doi: [10.1103/PhysRevLett.133.240601](https://doi.org/10.1103/PhysRevLett.133.240601). [arXiv:2402.15644](https://arxiv.org/abs/2402.15644). [D]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [arXiv:2503.09879](https://arxiv.org/abs/2503.09879). [D]
[939] T. H. Haug *et al.*, “A quasiparticle-protected superconducting qubit,” [arXiv:2610.12227](https://arxiv.org/abs/2610.12227), Oct. 2026. [P]
[940] L. Sun *et al.*, “Measurements of Quasiparticle Tunneling Dynamics in a Bandgap-Engineered Transmon Qubit,” *Phys. Rev. Lett.*, vol. 108, Art. no. 230509, 2012, doi: [10.1103/PhysRevLett.108.230509](https://doi.org/10.1103/PhysRevLett.108.230509). [arXiv:1112.2621](https://arxiv.org/abs/1112.2621). [D]
[941] V. Iaia *et al.*, “Phonon downconversion to suppress correlated errors in superconducting qubits,” *Nat. Commun.*, vol. 13, Art. no. 6425, Oct. 2022, doi: [10.1038/s41467-022-33997-0](https://doi.org/10.1038/s41467-022-33997-0). [arXiv:2203.06586](https://arxiv.org/abs/2203.06586). [D]
[942] P. M. Harrington *et al.*, “Synchronous detection of cosmic rays and correlated errors in superconducting qubit arrays,” *Nat. Commun.*, vol. 16, Art. no. 6428, Jul. 2025, doi: [10.1038/s41467-025-61385-x](https://doi.org/10.1038/s41467-025-61385-x). [arXiv:2402.03208](https://arxiv.org/abs/2402.03208). [D]
[943] A. R. Castelli *et al.*, “Superconducting-qubit decoherence correlated with detected radiation events,” *Phys. Rev. Appl.*, vol. 26, no. 4, Art. no. 044052, Oct. 2026, doi: [10.1103/ddyy-t37l](https://doi.org/10.1103/ddyy-t37l). [arXiv:2512.18171](https://arxiv.org/abs/2512.18171). [D]

