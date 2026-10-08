---
id: fab_bulk
name: Bulk-optics and fibre assembly (photonic samplers)
layer: "10 Manufacturing"
status: demonstrated
since: 2020
one_line: "Photonic processors assembled from discrete parts — free-space squeezers and interferometers, fibre delay loops, fibre-coupled modulators and cryogenic single-photon detectors — aligned and locked by hand and servo rather than patterned on a wafer."
verdict: "The lowest-loss way to buy delay and squeezing, and how every beyond-classical photonic sampler, Jiuzhang 1.0 (2020) to Jiuzhang 4.0 (2026), was built; as of 2026-09-26 no published fault-tolerant photonic design assembles its processor this way, and only fibre delays and links carry over to the chip machines."
updated: 2026-09-30
---

OPO = optical parametric oscillator; (PP)KTP = (periodically poled) potassium titanyl phosphate; EOM = electro-optic modulator; MZI = Mach–Zehnder interferometer; SNSPD = superconducting nanowire single-photon detector; TES = transition-edge sensor; PIC = photonic integrated circuit; ECCN = US Export Control Classification Number; USTC = University of Science and Technology of China; G1–G7 = the report's goal classes (G1: analogue and NISQ simulation).

## Identity & lineage
Crystals in free-space cavities squeeze light, beamsplitters or fibre couplers interfere it, fibre spools delay it, fibre-coupled cryogenic detectors count it. Jiuzhang 1.0 fed 50 squeezed states into a 100-mode "ultralow-loss" interferometer, the whole set-up phase-locked [D][460]; Borealis moved interference into time, with fibre loops of 1, 6 and 36 bins at a 6 MHz clock [D][270]; Jiuzhang 4.0 joins three 16-mode interferometers through two arrays of 16 fibre delays [D][175]. ORCA sells racks of "telecoms-grade optical fibre components" at room temperature [C][464]. Attributes: carrier affinity 0.25 (hosts modes, not qubits); no characteristic time, readout, mobility or control modality of its own; loss error; optics manufacturing.

## Physics & limits
Fibre is nearly free per metre: ≤0.18 dB/km at 1550 nm, group index 1.4682 [G][816]. Borealis's 36-bin loop (6.0 µs, ≈1.2 km) thus costs ≈0.22 dB in the glass, Jiuzhang 4.0's longest delay (12 µs, ≈2.4 km) ≈0.44 dB [S][175], [270]; foundry silicon nitride at 0.5–1.8 dB/m would charge ~600–2,200 dB for 1.2 km [S][169]. Delay stays in fibre; loss sits at transitions and active parts. Loss also caps squeezing: at transmission η the measured quadrature variance η·e^(−2r) + (1 − η) cannot fall below 1 − η — a 16.0 dB ceiling at η = 0.975, the efficiency behind the 15 dB record from a free-space PPKTP cavity [D][344], but 1.7 dB at Borealis's ~33% [S][270]. Phase is the second limit: Borealis's residual loop phase noise grows with length — 0.02, 0.03 and 0.15 rad for loops 0–2 [D][270]. Assembly has no scaling term — each element is placed, coupled and locked singly — while Xanadu reckons fault tolerance would take a 20–30× cut, in decibels, in every component's insertion loss [S][173].

## Engineering state of the art
| Year | Figure | Who | Tag+key |
|---|---|---|---|
| 2016-09-06 | 15 dB squeezing observed; 9.3 mm PPKTP half-monolithic cavity; total detection efficiency 0.975 | Vahlbruch et al., AEI Hannover | [D][344] |
| 2020-11-23 | Fibre-coupled SNSPD, system detection efficiency 98.0 ± 0.5% at 1550 nm | NIST | [D][618] |
| 2020-12-18 | 50 squeezed states, 100 modes, 100 detectors, set-up phase-locked | USTC, Jiuzhang 1.0 | [D][460] |
| 2022-06-01 | 216 modes from three fibre loops; 16 TES at 95%; net transmittance ~33%; 10 kHz | Xanadu, Borealis | [D][270] |
| 2025-01-22 | Chip machine linked by stabilised fibre delay modules; ~14 dB loss | Xanadu, Aurora | [D][173] |
| 2026-05-13 | 8,176 modes; source 92%, system 51%, 16 SNSPDs at 93%; phase held to ~λ/200 | USTC, Jiuzhang 4.0 | [D][175] |

With Jiuzhang 4.0's source (92%) and detectors (93%) near unity, the ~40% (≈2.2 dB) lost between them sits in filters, meshes, delays and couplings [S][175]; its filter stage of three unbalanced MZIs transmits 99.8% [D][175]. Borealis loses ~20% in its filter stack and ~15% in its demultiplexer [D][270]. Dominant term: transitions and switching, not propagation.

## Manufacturing, materials & supply chain
Borealis's squeezer is a 10 mm KTP crystal in an OPO pumped at 775 nm; its loop beamsplitters are custom EOMs from QUBIG GmbH; its TES detectors reach 95%, with NIST Boulder's Lita, Gerrits and Nam among the authors [D][270]. SNSPD supply is a handful of firms: Single Quantum (Netherlands) reported its 400th SNSPD system in July 2026 [P][621]; Photon Spot (US) quotes ">90% quantum efficiency near 1550nm" [C][630]; ID Quantique passed to IonQ, a computer maker, through a controlling stake [C][633]. ORCA's PT-2 page names a Eurostars-funded collaboration with Pixel Photonics (detectors), Sparrow Quantum and the Niels Bohr Institute (sources) [C][465]. The US rule of 2024-09-06 defines 4A906 quantum computers by ≥34 physical qubits and C-NOT error and names no single-photon detector, squeezer or photonic item [G][301]; a sampler, with neither, is not obviously covered [S][301].

## Control, readout & I/O burden
The load is servo, not gates. Borealis locks each loop with a counter-propagating laser, piezos and lock-in detection, re-locking for 35 µs of every 100 µs — hence 10 kHz [D][270]; Jiuzhang 4.0 sets delay phases with fast piezo stretchers and its meshes thermally [D][175]. The electro-optic load (ct_eo) is small: three EOM-driven loop beamsplitters and a 1-to-16 demultiplexer of 15 EOMs, extinction above 200:1 [D][270]. Time multiplexing is the one scaling lever: 16 detectors read 216 or 8,176 modes, and Jiuzhang 4.0's 43 ns SNSPD recovery sets its 50 ns bin [D][175], [270]. Only detectors are cryogenic.

## Role in the stack
Manufacturing slot of the Boson sampler architecture (ph_sampler, G1), shared with fab_pic. It **requires** ct_eo — fibre-coupled modulators and delay loops; it **provides** no edge; it **replaces** nothing, while fab_pic replaces it (photonic foundry vs bulk-optics assembly). The replacement is partial: Aurora moved squeezing and interference onto chips yet links them with fibre delay modules [D][173]. This answers gap G-bulkoptics — the record samplers were built neither in a 300 mm PIC foundry nor with fab_optics's ion and atom optics; the Atlas added this technology rather than extend fab_optics to ph_cv and ph_fusion, whose processors are lithographed [D][169], [173]. The register lists {{N_T_FAB_BULK_MACHINES_W}} carriers, {{N_T_FAB_BULK_PRIMARY_W}} of them primary: Borealis (Xanadu, deployed 2022-06), Jiuzhang 1.0, 2.0 and 3.0 (USTC, demonstrated 2020–2023, now retired), Jiuzhang 4.0 (USTC, demonstrated 2026-05-13), PT-1 (ORCA, deployed 2023) and PT-2 (ORCA, deployed 2024–2026).

## Evidence — how the numbers were measured
{{N_T_FAB_BULK_VERIFIED_W_CAP}} cells are ✅. Two rest on architecture papers: Borealis's Methods (fibre delay lines, EOM beamsplitters, fibre coupling above 97%) [D][270] and Jiuzhang 4.0's Extended Data Fig. 1 (free-space unbalanced MZI on a PZT-mounted mirror), whose text confirms fibre delay loops but says only that the 16-mode interferometers "incorporate thermal tunability" [D][175]; PT-1's rests on ORCA's product page, "rack-mounted, room temperature and built with optical fibre components" [C][G:ORCA-PT1-2023]. PT-2 stays 🔎: its page gives no architecture [C][465], and the fibre reading rests on ORCA's technology page [C][464]. Jiuzhang 1.0–3.0 stay 🔎 too: their cells are inferred from the lineage, not read from a figure. As of 2026-09-26 no sampler has published an assembly yield, a per-element loss distribution or a realignment interval.

## Actors & economics
**Who.**

| Organisation | Role | Country | What exactly they do with this technology | Evidence |
|---|---|---|---|---|
| USTC | developer | CN | Jiuzhang: free-space filters, fibre delay arrays, SNSPD readout | [D][175] |
| Xanadu | developer | CA | Borealis fibre loops; fibre delay modules kept in Aurora | [D][173], [270] |
| ORCA Computing | developer | UK | PT racks of telecom fibre parts; bought GXC's integrated photonics division | [C][464][P][817] |
| NIST Boulder | research | US | Borealis TES; 98% SNSPD | [D][270], [618] |
| QUBIG GmbH | supplier | DE | Custom EOMs in Borealis's loops | [D][270] |
| Single Quantum; Photon Spot; ID Quantique | suppliers | NL; US; CH | SNSPD systems | [P][621][C][630][C][633] |

**Money.**
- 2024-01-30 · ORCA Computing · acquisition of GXC's integrated photonics division, Austin, Texas · undisclosed · announced [P][817]
- 2025-05-06 · IonQ · controlling stake in ID Quantique · undisclosed in the release · closed [C][633]

**Market & supply chain.** Of the {{N_T_FAB_BULK_MACHINES_W}} carriers only ORCA's PT-1 and PT-2 are sold as systems; USTC is academic, though Jiuzhang 4.0 lists Jiuzhang Quantum Technology Co. Ltd. among its affiliations [D][175]; Borealis was offered through the cloud rather than sold, and the register lists it as deployed, its roadmap field noting that Aurora superseded it. Scarce inputs: number-resolving detectors, low-loss squeezers. Pays into G1 only.

**IP & standards.** No assembly-specific patent count or standard found as of 2026-09-26.

**Roadmaps & track record.** USTC went from 100 to 8,176 modes in 2020–2026 by multiplexing, not by adding parts [D][175], [460]; Xanadu left assembly within three years of Borealis, keeping the fibre [D][173]; ORCA framed GXC as a step toward "scalable, fault-tolerant quantum computing" [P][817], with no PT product on it published as of 2026-09-26.

**Strategic reading.** Assembly wins where the figure of merit is one machine's transmission on the day; fault tolerance needs that loss replicated with statistics, which only lithography offers — so the sampler architecture ends here while the CV and fusion architectures moved to PICs. Durable value sits with suppliers of fibre delays, squeezers and detectors, which chip machines still buy.

## Outlook & open questions
Confirm if, by 2027-12-31, an assembled sampler beats Jiuzhang 4.0's 51% end-to-end efficiency at ≥8,000 modes, or ORCA publishes PT loop count and loss; demote if the next Jiuzhang or PT-3 puts its interferometers on a chip, leaving the technology only delays and detectors. Open questions. (1) What is each Borealis loop's round-trip transmission? (2) Are Jiuzhang 4.0's 16-mode interferometers bulk, fibre or integrated? (3) How often must a loop sampler be realigned, at what cost in uptime? (4) Can on-chip delay approach fibre's ~0.2 dB/km, or will every photonic computer keep fibre spools? (5) Does any export-control entry beyond the 2024 US quantum ECCNs capture SNSPD or TES systems?

## References
[169] K. Alexander *et al.*, “A manufacturable platform for photonic quantum computing,” *Nature*, vol. 641, no. 8064, pp. 876–883, Feb. 2025, doi: [10.1038/s41586-025-08820-7](https://doi.org/10.1038/s41586-025-08820-7). [D]
[173] H. A. Rad *et al.*, “Scaling and networking a modular photonic quantum computer,” *Nature*, vol. 638, no. 8052, pp. 912–919, Jan. 2025, doi: [10.1038/s41586-024-08406-9](https://doi.org/10.1038/s41586-024-08406-9). [D]
[175] H.-L. Liu *et al.*, “Gaussian boson sampling with 1,024 squeezed states in 8,176 modes,” *Nature*, vol. 653, no. 8115, pp. 687–692, May 2026, doi: [10.1038/s41586-026-10523-6](https://doi.org/10.1038/s41586-026-10523-6). [arXiv:2508.09092](https://arxiv.org/abs/2508.09092). [D]
[270] L. S. Madsen *et al.*, “Quantum computational advantage with a programmable photonic processor,” *Nature*, vol. 606, no. 7912, pp. 75–81, Jun. 2022, doi: [10.1038/s41586-022-04725-x](https://doi.org/10.1038/s41586-022-04725-x). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[344] H. Vahlbruch, M. Mehmet, K. Danzmann, and R. Schnabel, “Detection of 15 dB Squeezed States of Light and their Application for the Absolute Calibration of Photoelectric Quantum Efficiency,” *Phys. Rev. Lett.*, vol. 117, no. 11, Art. no. 110801, Sep. 2016, doi: [10.1103/PhysRevLett.117.110801](https://doi.org/10.1103/PhysRevLett.117.110801). [D]
[460] H.-S. Zhong *et al.*, “Quantum computational advantage using photons,” *Science*, vol. 370, no. 6523, pp. 1460–1463, Dec. 2020, doi: [10.1126/science.abe8770](https://doi.org/10.1126/science.abe8770). [arXiv:2012.01625](https://arxiv.org/abs/2012.01625). [D]
[464] ORCA Computing, “Technology — ORCA Computing.” [Online]. Available: https://orcacomputing.com/technology/ [C]
[465] ORCA Computing, “ORCA PT-2 — ORCA Computing.” [Online]. Available: https://orcacomputing.com/orca-pt-2/ [C]
[618] D. V. Reddy, R. R. Nerem, S. W. Nam, R. P. Mirin, and V. B. Verma, “Superconducting nanowire single-photon detectors with 98% system detection efficiency at 1550 nm,” *Optica*, vol. 7, no. 12, p. 1649, Dec. 2020, doi: [10.1364/OPTICA.400751](https://doi.org/10.1364/OPTICA.400751). [D]
[621] TipRanks, “Single Quantum Hits 400-System Milestone as It Deepens European Quantum Partnerships,” Jul. 4, 2026. [Online]. Available: https://www.tipranks.com/news/private-companies/single-quantum-hits-400-system-milestone-as-it-deepens-european-quantum-partnerships [P]
[630] Photon Spot, “Photon Spot — Cryogenic & Quantum Detection Systems.” [Online]. Available: https://www.photonspot.com/ [C]
[633] IonQ, “IonQ Completes Acquisition of ID Quantique, Cementing Leadership in Quantum Networking and Secure Communications,” May 6, 2025. [Online]. Available: https://investors.ionq.com/news/news-details/2025/IonQ-Completes-Acquisition-of-ID-Quantique-Cementing-Leadership-in-Quantum-Networking-and-Secure-Communications/default.aspx [C]
[816] Corning Incorporated, “Corning® SMF-28® Ultra Optical Fiber — Product Information (PI-1424-AEN),” Jul. 2025. [Online]. Available: https://www.corning.com/media/worldwide/coc/documents/Fiber/product-information-sheets/PI-1424-AEN.pdf [G]
[817] Tech.eu, “ORCA Computing acquires GXC's integrated photonics division,” Jan. 30, 2024. [Online]. Available: https://tech.eu/2024/01/30/orca-computing-acquires-gxcs-integrated-photonics-division/ [P]

## Open verification items
- Borealis per-loop transmissions: not stated in the Nature text consulted on 2026-09-26 (only ~33% net, ~20% filter stack, ~15% demultiplexer, fibre coupling above 97%), so no dB-per-loop figure is given.
- Jiuzhang 4.0 (arXiv v3, consulted 2026-09-26): the physical form of the 16-mode interferometers and the SNSPD maker are not stated; whether 99.8% is per filter MZI or for the cascade is ambiguous.
- Export controls: no entry naming SNSPDs, TES or squeezers was found in the 2024-09-06 US rule or by search (2026-09-26); EAR/Wassenaar detector entries (6A002) and national lists were not checked, nor whether a TES refrigerator meets 3A904's cooling threshold (≥600 µW at ≤0.1 K).
- PTB as a TES source was not verified (2026-09-26); only NIST's role is confirmed.
- ORCA–GXC: completion of the purchase and any PT product using GXC technology were not found (2026-09-26).
