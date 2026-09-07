---
id: ct_pic_trap
name: PIC-generated tweezers / integrated optics for atoms
layer: "5 Control"
status: emerging
since: 2026
one_line: Generating, routing and collecting the light that traps, addresses and images single atoms from a photonic integrated circuit instead of free-space optics.
verdict: Four atoms trapped from a chip, fifty addressed through a chip, zero gates through either. Until a PIC holds atoms far enough from its surface to run Rydberg gates, this is packaging, not a scaling path.
updated: 2026-09-04
---

Λ = error-suppression factor per code-distance step; QBI = DARPA Quantum Benchmarking Initiative (Stage A concept → B R&D plan → C government V&V); G1–G7 = the report's goal classes (see Actors & economics).

## Identity & lineage
Move the optics that hold and address single atoms — lenses, modulators and deflectors on a metre-scale breadboard — onto a photonic chip. Two functions hide under one node and only the first is trap generation: emitting tweezer light from the chip (Pasqal, four rubidium atoms, ~27.5 s lifetime, August 2026 [C][1]), and coupling trapped atoms to on-chip photonics for imaging and collection (Chicago, 64 free-space tweezers over >100 nanophotonic cavities [D][3]; a 50-atom, 784-channel glass waveguide array [D][4]). Reconfiguring traps on chip, nobody has shown.

Control and fabrication: room-temperature optical control from a photonic IC, wrapping a natural carrier it never becomes. Error structure: coherent — coupling loss, cross-talk (0.4% measured [D][4]) and surface-induced light shifts, not decoherence.

## Physics & limits
A rubidium tweezer needs roughly a millikelvin of depth: several milliwatts focused to a micron waist at high numerical aperture. A grating or metasurface emitter can do that, and Pasqal's lifetime matches its own bulk systems [C][1], so coupling loss is not the first wall. Power is next: a thousand traps is watts on chip, where scattered light and coupler heating bind first.

The first wall is the surface. Rydberg states are enormously polarisable, so adsorbate-induced stray fields and blackbody radiation from a nearby dielectric shift and broaden the line every neutral-atom two-qubit gate depends on. Chicago holds atoms a few hundred nanometres above the chip for cavity coupling [D][3] — excellent for photon collection, hopeless for a blockade gate. A trap-generating chip must project its focus tens to hundreds of microns clear of itself, spending much of the footprint advantage. The second wall is reconfiguration: crossed deflectors sweep continuously and are already the bandwidth limit above ~10⁴ atoms, while on-chip switching is thermo-optic (microseconds to milliseconds, milliwatts dissipated each) or electro-optic in lithium niobate (nanoseconds, lossier, not trap-grade yet). What moves the floor: surface passivation letting atoms sit closer, and a low-loss switch fabric beating deflector rates.

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2024-07 | 64 tweezers over >100 nanophotonic cavities, 99.2% imaging fidelity, atoms a few hundred nm above the surface | University of Chicago | [D][3] |
| 2026-08 | 4 Rb atoms trapped by light from a SiN chip, ~27.5 s lifetime, stated as matching bulk optics | Pasqal | [C][1] |
| 2026-08 | 50 addressed ⁸⁷Rb atoms through a glass waveguide array: 0.4% cross-talk, 2.9 dB insertion loss, 93% fill, 118 Hz loss repair, 784-channel chip | USTC | [D][4] |

Two to three orders below free-space systems on atom count, and no gate or transport has run through a chip-generated trap anywhere. The 784-channel chip is the strongest scaling evidence, and it addresses atoms rather than trapping them.

## Manufacturing, materials & supply chain
Silicon nitride photonic-IC processes; the 50-atom array uses glass waveguides [D][4]. Pasqal's photonics came from Aeponyx at an undisclosed price under 18 months before the August 2026 release, and no foundry partner is named [C][2]. Nearest merchant capacity: imec's PIXEurope pilot line (~EUR 400 M, 2024-11-24) and GlobalFoundries' Quantum Technology Solutions ($375 M CHIPS letter of intent, 2026-05-21) — both name photonics as an output, neither names atom traps [G][5][G][6]. Thin-film lithium niobate vendors HyperLight and Lightium are the candidates if fast switching becomes the requirement [P][7]. No yield, per-channel cost or export-control category for atom-trap photonics was found as of 2026-09-04.

## Control, readout & I/O burden
The claim is footprint: Pasqal states up to 50× smaller optics once trap light is routed on chip [C][1]. At four atoms the burden is a few fibre couplings; the question starts at hundreds, where it becomes power per channel, fibre count into vacuum and switching bandwidth — none of which is published. The 784-channel chip at 2.9 dB insertion loss is the only channel-count datum [D][4]. A chip removes an optical table's alignment and drift burden and adds a fixed geometry unless switches are integrated.

## Role in the stack
It replaces free-space tweezer and addressing optics on the alkali neutral-atom path (Pasqal, QuEra, Infleqtion, Atom Computing) and requires a photonic-IC process underneath, providing no connectivity, gate or code of its own. Contribution to the derived clock is nil today; at scale, on-chip switching could become a new clock term if it cannot match deflector reconfiguration — the opposite of the intended effect. The same pattern runs on the ion side, where Sandia supplies Quantinuum integrated photonics for laser delivery [G][8]. Neighbouring empty slots: a gate through a chip-generated trap, and on-chip transport.

## Verification (QCVV)
Pasqal's lifetime and 50× footprint projection are company-reported without replication, and "matching bulk optics" is measured against its own systems, not an external reference [C][1]. The Chicago and USTC results carry no vendor roadmap and neither reports a gate fidelity, because neither has run a gate. Nothing published measures what matters most — trap depth, position stability and Rydberg-line shift against distance from the chip surface.

## Actors & economics
**Who.**
| Organisation | Role | Country | What they do here | Evidence |
|---|---|---|---|---|
| Pasqal | developer | FR | Only chip-generated atom traps demonstrated | [C][1] |
| Aeponyx | supplier | CA | SiN photonics behind Pasqal's chip; acquired | [C][2] |
| University of Chicago | research | US | Atom array over nanophotonic cavities, background-free imaging | [D][3] |
| USTC | research | CN | 50-atom addressing array, 784-channel chip | [D][4] |
| GlobalFoundries | supplier | US | Quantum unit naming photonics as an output | [G][6] |
| HyperLight | supplier | US | Lithium niobate for fast switching | [P][7] |

**Money.** 2024-09 · HyperLight and Lightium · Series B and seed · $37 M and $7 M · Summit Partners; Vsquared and Lakestar · closed [P][G:TFLN-FUNDING-2024-09]. 2025 (undated) · Pasqal · M&A of Aeponyx · undisclosed · closed, stated as under 18 months before 2026-08 [C][2]. 2026-08-28 · Pasqal · SPAC merger · ~$360 M cash · Nasdaq PSQL · closed [G:PASQAL-SPAC-2026-08].

**Market & supply chain.** The supply base is the general photonic-foundry ecosystem, not scarce; the scarce asset is trap design know-how, and Pasqal's arrived with one acquired startup — a single point of failure if that team disperses. What it threatens is the incumbent free-space chain: deflectors from AA Opto-Electronic and Gooch & Housego, the only vendors named in published tweezer work [D][9]. It pays for G3 and G4 by cutting footprint and alignment labour, nothing for G1, G2 or G5.

**IP & standards.** Aeponyx's pre-acquisition silicon-nitride portfolio is the core asset; Pasqal has disclosed nothing of its contents. No dated patent-family count for chip-generated atom tweezers was found as of 2026-09-04, and no standards activity addresses trap-grade photonics.

**Roadmaps & track record.** Pasqal states >10,000 atoms and 100 logical qubits by this route with no date attached [R][1], against one slip already on the free-space side — 10,000 physical moved from 2026 to 2028, 100 logical to 2029 [R][10][G:PASQAL-SPAC-2026-08]. First demonstration August 2026: no delivery record to score, and no rival chip-trap roadmap exists.

**Strategic reading.** If on-chip generation scales past the dozens it undercuts the free-space chain every tweezer and ion machine depends on and moves bargaining power to photonic foundries selling into datacom volumes; Pasqal wins by leading in a component competitors must then buy or build. If cross-talk, power and the surface problem cap channel counts in the tens, it stays packaging and the incumbent vendors keep their position — the likelier outcome on today's evidence.

*Open niche:* No benchmark exists for chip-generated trap quality against free-space tweezers. A small QCVV team could define one — trap depth per milliwatt delivered, position stability over hours, cross-talk at stated channel count, Rydberg-line shift versus distance from the chip — before a second vendor's claims need adjudicating. The last decides whether this can carry a gate at all.

## Outlook & open questions
Confirm/demote in 12–24 months: anyone runs a two-qubit gate through a chip-generated trap; chip-trapped atom count reaches the hundreds; a second vendor enters. Best case 2029: chip tweezers hold hundreds to thousands of atoms at free-space fidelity, shrinking a rack enough to change system cost. Worst case: the surface constraint forces long working distances, the footprint gain evaporates, and integrated optics stays confined to imaging and collection, where it already works. Open: how far from the chip must atoms sit for a clean Rydberg line; can on-chip switching beat deflector reconfiguration. Watch: Pasqal's next update and any gate through a chip trap.

## Sources
[1] Pasqal · "Pasqal brings qubit control on-chip" — four Rb atoms from a SiN PIC, ~27.5 s lifetime, up to 50× optical footprint reduction claimed, >10,000 atoms / 100 logical qubits long-term target · company newsroom · 2026-08-10 · https://www.pasqal.com/news/pasqal-brings-qubit-control-on-chip-advancing-the-path-to-fault-tolerant-quantum-computing-at-scale/ [C]
[2] "Pasqal demonstrates photonic chip-based control for neutral-atom quantum computers" — Aeponyx acquisition stated as under 18 months earlier, terms undisclosed, no foundry named · The Quantum Insider · 2026-08-10 · https://thequantuminsider.com/2026/08/10/pasqal-photonic-chip-control-neutral-atom-quantum-computers/ [P]
[3] Menon, Glachman, Pompili, Dibos, Bernien (University of Chicago) · "An integrated atom array–nanophotonic chip platform with background-free imaging" · Nature Communications 15, 6156 · 2024-07-22 · https://www.nature.com/articles/s41467-024-50355-4
[4] Hu, Zhang, Ma, Zhang, Chen, Zhu, Fan, Zhang, Wang, Li, Ren, Guo, Zou · "A scalable chip-integrated single-photon source array based on 50 individually addressable neutral atoms" · arXiv:2608.15637 · 2026-08-16 · https://arxiv.org/abs/2608.15637
[5] imec · European Commission and Chips JU select the PIXEurope consortium to lead the European photonic-IC pilot line · press release · 2024-11-24 · https://www.imec-int.com/en/press/european-commission-and-chips-ju-select-pixeurope-consortium-lead-european-pilot-line
[6] GlobalFoundries · launch of Quantum Technology Solutions, $375 M CHIPS letter of intent · press release · 2026-05-21 · https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/
[7] "Lithium niobate in vogue as thin-film developers raise cash" — HyperLight $37 M Series B, Lightium $7 M seed · optics.org · 2024-09 · https://optics.org/news/lithium-niobate-in-vogue-as-thin-film-developers-raise-cash [P]
[8] Sandia National Laboratories · renewed four-year CRADA with Quantinuum; MESA integrated-photonics chips for trapped-ion laser delivery · lab news · 2026-08-27 · https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/
[9] Bluvstein et al. (Harvard, MIT, QuEra) · 448-atom architecture; AA Opto-Electronic DTSX-400 deflectors and Hamamatsu imaging named in the apparatus · Nature 649, 39 · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[10] Pasqal · SPAC merger completed, ~$360 M cash, Nasdaq PSQL; roadmap 10,000 physical 2028, 100 logical 2029 · The Quantum Insider · 2026-08-28 · https://thequantuminsider.com/2026/08/28/pasqal-completes-spac-merger-with-360-million-in-cash/ [P]

## Open verification items
- The institutional affiliation of the 50-atom array authors is inferred from the author list (Zou, Guo, Ren, Li) as USTC; the abstract page does not state it.
- Aeponyx acquisition price and closing date remain undisclosed; only "less than 18 months" before 2026-08-10 is stated anywhere found.
- No independent replication of Pasqal's 27.5 s lifetime or of the 50× footprint projection, and no numbers behind the projection.
- No measurement anywhere of Rydberg-line shift or broadening as a function of atom–chip distance in a trap-generating geometry; the millikelvin-depth and milliwatt-per-trap figures in Physics are standard tweezer scalings, not values quoted by these sources.
- No yield, per-channel cost or export-control classification for atom-trap photonics was found.
