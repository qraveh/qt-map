---
id: fab_cryo_atom
name: Cryogenic tweezer-array apparatus (blackbody suppression)
layer: "10 Manufacturing"
status: emerging
since: 2021
one_line: The tweezer array behind 4–45 K shields in a room-temperature chamber — cryopumping stretches trap lifetimes to hours and cold shields cut the blackbody radiation that shortens Rydberg states and seeds correlated loss; gates inside it now match room temperature.
verdict: Three laboratories show the apparatus works and one shows gates in it at room-temperature fidelity; until a cold array beats a warm one on a gate or a QEC round, or a vendor ships one, cryogenics buys lifetime and loss suppression, not performance.
updated: 2026-11-07
---

BBR = blackbody radiation; T_eff = the effective blackbody temperature the atoms see, set by the shields and the warm solid angle of the windows; NA = numerical aperture; nS = a Rydberg S state of principal quantum number n.

## Identity & lineage

A neutral-atom machine is a vacuum chamber with lasers; this technology puts cold metal around the atoms. Two things improve. A surface at 4 K pumps the residual hydrogen that limits a room-temperature chamber's trap lifetime to tens of seconds, so single atoms stay for hours; and a shield at 4–45 K cuts the room-temperature blackbody radiation whose photons, at the tens of gigahertz that separate neighbouring Rydberg levels, drive a Rydberg atom into contaminant states and shorten its lifetime — at principal quantum numbers near 50–70 the blackbody-induced rate rivals spontaneous decay, as the quasiclassical tables of Beterov and colleagues set out [S][387]. The Institut d'Optique and Pasqal built the first such apparatus for tweezer arrays and reached 6,000 s trap lifetimes (Phys. Rev. Applied 16, 034013, 2021) [D][507], rearranged an 828-atom target array in 2,088 sites at 6 K with room-temperature objectives protruding into windowless thermal shields (Phys. Rev. Applied 22, 024073, 2024) [D][923], and in 2026 prepared defect-free arrays of up to 1,024 atoms at 4 K with trapping lifetimes near 5,000 s (PRX Quantum 7, 033032) [D][146]. JILA's cryogenic system combined a 4 K cryopumping surface, a cold box below 50 K and a room-temperature high-NA objective for a 3,000 s lifetime of a ⁸⁷Rb array with Rydberg control and integrated field electrodes (PRX Quantum 6, 020337, 2025) [D][924]. The 2026 results are what move it from an apparatus to a technology of the stack: Princeton's universal gate set in a cryogenic ¹³³Cs array — single-qubit fidelity 99.970(2)%, raw CZ fidelity 99.76(8)% — behind shields at 35 K and 4 K with the aspheric objectives inside the 4 K shield [P][925]; JILA's measurement that a 45 K shield lengthens Rydberg nS lifetimes by up to 45(11)% and cuts the avalanche rate of correlated loss by 22(2)% in arrays of up to 70 atoms [P][926]; and the Max Planck Institute of Quantum Optics' 16 × 16 ⁸⁸Sr array with every objective outside the glass cell and vacuum-limited lifetimes over 7,000 s [P][927].

Attributes (technology graph): carrier affinity 0.0 — natural. Characteristic time: none. Readout: none of its own. Mobility: none. Control: none of its own. Error structure: loss and correlated bursts — the two it suppresses. Manufacturing: optical and mechanical assembly, now cryogenic.

## Physics & limits

Blackbody radiation at 300 K has its spectral peak near 17 THz, but a Rydberg atom's neighbouring levels are tens of gigahertz apart, where the thermal occupation at room temperature is a few hundred photons per mode; those photons drive transitions to nearby Rydberg states at a rate that, for n ≈ 50–75, is comparable to spontaneous emission [S][387]. The contaminant states do two kinds of harm: they shorten the Rydberg lifetime that every Rydberg gate pays for, and they populate states whose interactions with the array's other atoms are uncontrolled, seeding the avalanches of correlated loss that JILA measured and modelled — cooling the environment reduces the thermal occupation, and the measured suppression follows the effective temperature the atoms see: behind a 45 K shield with warm windows, T_eff = 188(8) K, that is 44(3)% shielding, giving nS lifetimes up to 45(11)% longer and avalanche rates 22(2)% lower at n = 50 and 18(2)% at n = 60 [P][926]. Vacuum is the second gain: cryopumping on 4 K surfaces gives trap lifetimes of 3,000–7,000 s against tens of seconds, which is what makes the loss of imaging and cooling measurable at the 10⁻⁴ level [D][924] and makes thousand-atom defect-free registers reachable in a second rearrangement cycle [D][146].

The limits are engineering trades. Optical access against shielding: objectives inside the 4 K shield see a cold sky and need conductive coatings against stray charge (Princeton's indium-tin-oxide-coated aspheres, fields compensated below 7 mV/cm) [P][925]; objectives outside see every window as a warm patch of sky — MPQ's design "does not shield the atoms from exposure to room-temperature blackbody radiation" by its own account [P][927], and JILA's warm windows leave T_eff at 188 K rather than 45 K [P][926]. Cooling power against array size: Princeton estimates that the 0.4 W available at 4 K "can support more than ten thousand tweezers" of scattered light [P][925]. Vibration and drift of closed-cycle cryocoolers against tweezer stability, and the cost of a cryostat where a glass cell sufficed. What cryogenics does not do is improve the gate: Princeton's CZ error is dominated by atomic motion (Doppler shifts, 1.26 × 10⁻³) with Rydberg decay at 2.7 × 10⁻⁴, so "cryogenic operation leaves atomic motion as the dominant source of infidelity" [P][925].

## Engineering state of the art

Best demonstrated as of 7 Nov 2026: a universal gate set in a cryogenic array — 1Q 99.970(2)%, CZ 99.76(8)% raw by echo randomised benchmarking and 99.78(10)% by symmetric stabiliser benchmarking, a Rydberg lifetime near 406 µs at 55P₃/₂ [P][925]; the largest cold register, 1,024 atoms defect-free at 4 K [D][146]; the longest lifetimes, 6,000–7,000 s [D][507][P][927]. Typical at scale: none — no product runs cold.

**Records timeline**

| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2021-06 | Single atoms with 6,000 s trapping lifetimes in tweezer arrays at cryogenic temperature | Institut d'Optique / Pasqal | [D][507] |
| 2024-08 | 2,088-site array at 6 K; 828-atom target rearranged; room-temperature objectives inside windowless shields | Pasqal / Institut d'Optique | [D][923] |
| 2025-05 | 3,000 s lifetime; 4 K cryopumping surface, < 50 K cold box, room-temperature high-NA objective; Rydberg control and field nulling | JILA / NIST / CU Boulder | [D][924] |
| 2026-07 | 16 × 16 ⁸⁸Sr array, full optical access (objectives outside the cell), > 7,000 s vacuum-limited lifetime | MPQ / LMU | [P][927] |
| 2026-08 | Defect-free arrays of up to 1,024 atoms at 4 K, ~5,000 s trapping lifetime | Pasqal / Université Paris-Saclay | [D][146] |
| 2026-10 | Universal gate set in a cryogenic Cs array: 1Q 99.970(2)%, CZ 99.76(8)% raw; shields at 35 K and 4 K; Rydberg lifetime ~406 µs | Princeton | [P][925] |
| 2026-11 | 45 K shield: nS lifetimes up to 45(11)% longer, avalanche rate down 22(2)% (n = 50), arrays of up to 70 Rb atoms | JILA / NIST / CU Boulder | [P][926] |

Dominant error term: for the gate, atomic motion, not Rydberg decay [P][925]; for the array, the warm solid angle that keeps T_eff far above the shield temperature [P][926].

## Manufacturing, materials & supply chain

The cryogenics is commodity: MPQ names a commercial closed-cycle cryostat (ColdEdge Stinger) on a two-stage Sumitomo RDK-415D2 cryocooler, with about 40 cm² of surface at 4 K and a radiation shield near 20 K, the cold tip some 30 cm from the atoms [P][927]; Princeton's and JILA's are custom shield geometries around standard cold heads. The engineering that is not commodity is the shield geometry and the optical access — windowless shields with objectives protruding (Pasqal), objectives inside the 4 K shield with conductive coatings (Princeton), everything outside a glass cell (MPQ) — and the field control that cold dielectrics near the atoms demand. Supply-chain concentration is low on parts (cryocoolers, optics) and the know-how sits in four laboratories and one company; export-control exposure is the lasers' and the apparatus' [G:BIS-QUANTUM-ECCN-2024-09]. Unit cost: a cryostat and its compressor on top of the room-temperature machine, whose optical tier is already its largest line [G:ATOM-OPTICS-UNIT-COST-2026].

## Control, readout & I/O burden

Nothing changes in kind — the same lasers, AODs, cameras and electrodes — and one thing changes in place: where the objectives sit decides both the blackbody shielding and the optical path. Inside the shield (Princeton, NA 0.5) the optics are cold and the field compensation is local; outside (MPQ, NA 0.65; JILA; Pasqal) the optics are standard and the windows are warm. The cooling power at 4 K sets the scattered-light budget of the array — about 0.4 W, enough for more than ten thousand tweezers by Princeton's estimate [P][925] — and the control of stray fields on cold surfaces (below 7 mV/cm at Princeton, integrated electrodes at JILA) is a burden the warm machine does not carry [P][925][D][924].

## Role in the stack

Architectures: an alternate manufacturing route on the rubidium/caesium array (`atom_rb`) and on the alkaline-earth array (`atom_ae`), shown with Cs, Rb and Sr. It requires the room-temperature optical assembly (`fab_optics`), whose lasers, vacuum and objectives it keeps behind shields, and is its alternative: room-temperature against cryogenic apparatus. It serves the Rydberg gate (`g_ryd`) by lengthening the Rydberg lifetime and the analogue ground–Rydberg qubit (`enc_gr`) the same way; it serves continuous reloading (`cx_reload`) from the other side — long lifetimes and reloading are the two answers to atom loss, and a cold machine needs reloading less often. The register's neutral-atom machines are all room-temperature systems; Pasqal, the one company with a cold array, sells warm ones. Price of switching: a cryostat, cold-surface field control and a harder optical path; gained: hour-scale lifetimes, 10⁻⁴-level loss diagnostics, and a 20–50% suppression of the blackbody-driven decay and correlated loss that no warm machine can buy.

## Evidence — how the numbers were measured

Trap lifetimes are exponential fits to atom survival over hours; the 6,000 s, 3,000 s, ~5,000 s and > 7,000 s figures are vacuum-limited and depend on the cooling applied during the hold (MPQ's with pulsed Sisyphus and sideband cooling) [D][507], [924], [146][P][927]. Princeton's gate fidelities are randomised benchmarking (1Q), echo randomised benchmarking and symmetric stabiliser benchmarking (CZ), all raw — no SPAM-corrected CZ value is published — on a 7 × 2 array of 14 sites at about 55% filling [P][925]; the room-temperature comparison the authors draw is to the leading implementations, whose best raw CZ is 99.854(4)% [G:HARVARD-CZ-2026-04], so the cold gate sits inside the room-temperature range rather than above it. JILA's lifetime and avalanche figures are measured against a parameter-free rate model and against the same array at room temperature, with the effective temperature inferred from the lifetimes [P][926]. Value conflict: the MPQ apparatus is cryogenic for vacuum and not for blackbody — its own statement — so its 2 h lifetime does not imply Rydberg shielding; and the Princeton paper gives the shield temperatures (35 K and 4 K) but no effective temperature at the atoms. Not published: a cold array's QEC round, a gate fidelity above the warm best, a product.

## Actors & economics

**Who.**

| Organisation | Role | Country | What they do with it | Evidence |
|---|---|---|---|---|
| Pasqal / Institut d'Optique / Université Paris-Saclay | developer / research | FR | The first cryogenic tweezer arrays; 2,088 sites at 6 K; 1,024 atoms defect-free at 4 K | [D][507], [923], [146] |
| Princeton University (Thompson, Bakr) | research | US | Universal gate set in a cryogenic Cs array | [P][925] |
| JILA / NIST / University of Colorado Boulder (Regal, Kaufman) | research | US | 3,000 s system; blackbody and avalanche suppression measured | [D][924][P][926] |
| Max Planck Institute of Quantum Optics / LMU Munich (Bloch, Zeiher, Blatt) | research | DE | Full-optical-access Sr platform, 2 h lifetime; two authors are planqc co-founders | [P][927] |
| Google Quantum AI | developer | US | Neutral-atom hardware track at Boulder under Kaufman, ex-JILA; a JILA co-author now at Google | [G:GOOGLE-ATOMS-2026-03][P][926] |

**Money.** Pasqal's listing brought about $360 M in 2026-08 [G:PASQAL-SPAC-2026-08]; its cryogenic arrays are research, its machines in the register warm. QuEra's and Atom Computing's rounds [G:QUERA-230M-2025], [G:ATOM-300M-2026-06] fund room-temperature systems.

**Market & supply chain.** No cold neutral-atom machine is sold; the cryogenics market is the cryocooler makers', shared with every superconducting lab. If a vendor goes cold it buys a cryostat per machine and the know-how of one of four groups.

**IP & standards.** No patent search was made for this record. No standard.

**Roadmaps & track record.** Pasqal's roadmap speaks of 10,000 physical qubits [G:PASQAL-SPAC-2026-08]; neither it nor any other vendor's names a cryogenic product. The academic record is consistent: every lifetime promised since 2021 was delivered, and the first gates arrived in 2026.

**Strategic reading.** Cryogenics is the neutral-atom platform's reserve: a known way to buy an order of magnitude in lifetime and a measurable fraction in Rydberg loss, held until the warm machines run out of room. The groups holding it are Pasqal's and the Boulder cluster that Google now draws on; if either ships a cold array, the other vendors face a cryostat they did not budget for.

## Outlook & open questions

Confirm within 12–24 months if a cryogenic array runs a QEC round with a lower loss rate than a warm one, if a cold CZ exceeds the warm best, or if a vendor announces a cryogenic product. Demote if by 2028 the cold arrays remain lifetime demonstrations with gates at warm fidelity. Best case by 2029: thousand-atom cold machines whose correlated-loss floor is half the warm one's; worst case: a vacuum trick the field uses for diagnostics.

Open questions: (1) how far does T_eff fall with conductive window coatings, and does the avalanche rate follow? (2) does the Rydberg lifetime gain translate into gate fidelity once motion is cooled? (3) can the objectives sit cold at NA 0.65 without charging? (4) what is the vibration budget of a closed-cycle cryostat for a 10,000-tweezer array? (5) does Pasqal ship one?

## References

[146] D. Lim *et al.*, “Defect-free arrays at the thousand-atom scale in a 4-K cryogenic environment,” *PRX Quantum*, vol. 7, Art. no. 033032, Apr. 2026, doi: [10.1103/45t1-vl5y](https://doi.org/10.1103/45t1-vl5y). [arXiv:2604.07205](https://arxiv.org/abs/2604.07205). [D]
[387] I. I. Beterov, I. I. Ryabtsev, D. B. Tretyakov, and V. M. Entin, “Quasiclassical calculations of blackbody-radiation-induced depopulation rates and effective lifetimes of Rydberg nS, nP, and nD alkali-metal atoms with n ≤ 80,” *Phys. Rev. A*, vol. 79, no. 5, Art. no. 052504, 2009, doi: [10.1103/PhysRevA.79.052504](https://doi.org/10.1103/PhysRevA.79.052504). [arXiv:0810.0339](https://arxiv.org/abs/0810.0339). [S]
[507] K.-N. Schymik *et al.*, “Single Atoms with 6000-Second Trapping Lifetimes in Optical-Tweezer Arrays at Cryogenic Temperatures,” *Phys. Rev. Appl.*, vol. 16, no. 3, Art. no. 034013, Jun. 2021, doi: [10.1103/PhysRevApplied.16.034013](https://doi.org/10.1103/PhysRevApplied.16.034013). [arXiv:2106.07414](https://arxiv.org/abs/2106.07414). [D]
[923] G. Pichard *et al.*, “Rearrangement of single atoms in a 2000-site optical tweezers array at cryogenic temperatures,” *Phys. Rev. Appl.*, vol. 22, no. 2, Art. no. 024073, Aug. 2024, doi: [10.1103/PhysRevApplied.22.024073](https://doi.org/10.1103/PhysRevApplied.22.024073). [arXiv:2405.19503](https://arxiv.org/abs/2405.19503). [D]
[924] Z. Zhang *et al.*, “A high optical access cryogenic system for Rydberg atom arrays with a 3000-second trap lifetime,” *PRX Quantum*, vol. 6, no. 2, Art. no. 020337, May 2025, doi: [10.1103/PRXQuantum.6.020337](https://doi.org/10.1103/PRXQuantum.6.020337). [arXiv:2412.09780](https://arxiv.org/abs/2412.09780). [D]
[925] J. Jin, D. Seo, Y. Shi, Y. Lu, J. D. Thompson, and W. S. Bakr, “High-fidelity universal quantum gates in a cryogenic atom array,” [arXiv:2610.40329](https://arxiv.org/abs/2610.40329), Oct. 2026. [P]
[926] Z. Zhang *et al.*, “Cryogenic suppression of correlated loss in Rydberg atom arrays,” [arXiv:2611.06613](https://arxiv.org/abs/2611.06613), Nov. 2026. [P]
[927] A. Kumar *et al.*, “A cryogenic neutral-atom platform with full optical access and 2-hour trap lifetime,” [arXiv:2607.12988](https://arxiv.org/abs/2607.12988), Jul. 2026. [P]

