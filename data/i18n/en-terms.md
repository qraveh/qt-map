# English terms and house style of the Quantum Technology Atlas — the binding list (4 Oct 2026)

The editor's order (4 Oct 2026): the same check as for the Hebrew and Russian editions — every term in its quantum-mechanical context, the
most literate academic usage, the literature of the very device first. English is the Atlas's source language, so this list fixes (1) the
field's term where the Atlas's differed, (2) one spelling and one compound form, (3) the abbreviation policy, (4) the glossary's definitions.
Checked 4 Oct 2026 by seven research passes (617 items) against the device literature — Krantz et al. 2019 and Blais et al. 2021
(superconducting), Bruzewicz et al. 2019 and Saffman–Walker–Mølmer 2010 / Henriet et al. 2020 (ions, atoms), Burkard et al. 2023 (spins),
Slussarenko & Pryde 2019 and Bartolucci et al. 2023 (photonics), Terhal 2015 and Bravyi et al. 2024 (codes), the builders' own papers
(Google Quantum AI, IBM, Quantinuum, IonQ, Harvard/QuEra, PsiQuantum, Xanadu, Microsoft, D-Wave) — then Nielsen & Chuang and Preskill; usage
(Wikipedia, press) only as an indicator. The decisions and their evidence: the editor's working folder, DECISIONS_2026-10-04_english-terms.md.

## Spelling and typography
- British English with -ise: organisation, colour, fibre, centre, aluminium, modelling, neighbour, artefact, grey, favour; characterise,
  optimisation, stabiliser, initialisation, realise, quantisation, randomised benchmarking, polarised, ionising, generalise, depolarising.
  A quoted paper title keeps its own spelling ("color code", "randomized", "stabilizer"); a proper name keeps its form (Center for …, Gray code).
- "program" is a computer or quantum program; "programme" a plan, a funding or research programme.
- "analog" is the technical term (analog quantum simulation / simulator / evolution / mode / annealing, analog Hamiltonian simulation,
  digital-to-analog converter, analog signal / electronics / syndrome information); "analogue" only as the noun "a counterpart".
- One form: crosstalk · feed-forward · break-even · spacetime (codes, volume, distance) · readout (noun), read out (verb) · nearest-neighbour
  (attributive), nearest neighbour (noun) · post-selected, post-selection · two-qubit · single-shot · all-to-all · dual-rail · time-bin
  (attributive), time bin (noun) · bump-bonded (adj.), bump bond (noun) · on-chip / real-time (attributive) · multi-chip · fan-out · FD-SOI ·
  predecoder · microfabricated · 6-ring · bivariate bicycle (code) · BP+OSD · SiMOS · AlphaQubit 2 · coaxmon (lower-case) · imec · ETH Zürich ·
  beamsplitter · molecular beam epitaxy · superconducting nanowire single-photon detector · Pauli spin blockade · T centre (noun), T-centre
  (before a noun) · X loop / Z loop (nouns) · 3D, 2D · wafer-scale · co-design · state of the art (noun).
- En dash for pairs and ranges: Mølmer–Sørensen, Loss–DiVincenzo, Lutchyn–Oreg, Gottesman–Kitaev–Preskill, spin–photon, singlet–triplet,
  InAs–Pb, 1–4.5 ms, 99.0–99.6%; hyphen in III-V; "×" for multiplication (10×); "4 K", "300 mm" (no hyphen before a unit symbol); T1, T2,
  T2* in plain form (the three editions' labels and the glossary; $T_1$ only inside LaTeX); isotopes as ¹⁷¹Yb, ⁸⁷Rb; d=7 (compact) and
  "distance-7" as a modifier; units international (µs, ns, mK, GHz, dB, mdB).
- Not regulated (both forms acceptable): ~ vs ≈ and its spacing; ISO dates in data-like contexts versus written dates in prose.

## Terms (the field's form)
| English | note / authority |
|---|---|
| alkaline-earth(-like) atom (Sr, Yb); first mention "alkaline-earth and alkaline-earth-like atoms" | Yb is a lanthanide; Jenkins et al. 2022, Ma et al. 2022 |
| bare physical qubit (no encoding) — node enc_bare | the field's "bare qubit"; "two-level subspace" was the Atlas's |
| quantum annealing (analog evolution) — node g_anneal | D-Wave; the process is quantum annealing |
| continuous atom reloading (reservoir + optical conveyor belt) | Caltech/Endres 2024; bare "conveyor" collides with the spin conveyor |
| resource-state generator (RSG) (photonic) | Bartolucci et al. 2023; "factory" stays for magic states |
| fusion failure (heralded; erases one of the two outcomes) vs photon loss (erases both) | Bartolucci et al. 2023 |
| the dominant error is loss (photonics) | not "the only error" |
| the 50% fusion ceiling is a linear-optics bound (Calsamiglia & Lütkenhaus 2001); ancilla photons raise it to 75% | not "information-theoretic" |
| internal detection efficiency (SNSPD) | SNSPD literature |
| squeezing by a parametric process — χ⁽²⁾ down-conversion or χ⁽³⁾ four-wave mixing | Xanadu (SiN) |
| light-shift gate: a state-dependent optical dipole force (σzσz geometric phase); the MS gate leaves the motional mode as it found it | Leibfried et al. 2003; Sørensen & Mølmer 1999 |
| 1995 NIST gate: between one ion's internal state and its motion; two-ion gates 1998–2003 | Monroe et al. 1995 |
| laser-free (microwave-driven) gates — Oxford Ionics' "electronic qubit control"; the Atlas's shorthand "electronic gate" after the first mention | Harty et al.; Oxford Ionics |
| crossbar: proposed by Li et al. (QuTech, Sci. Adv. 2018), first demonstrated by Borsoi et al. 2024 | — |
| SiMOS accumulation layer (not inversion layer) | Burkard et al. 2023 |
| NV lacks inversion symmetry (spectral diffusion); SiV and SnV are inversion-symmetric; the T centre is not | Bradac et al. 2019 |
| Pauli spin blockade (PSB); Majorana zero modes (MZMs); leakage reduction units (LRUs); exchange-only = three spins, singlet–triplet = two spins plus a field gradient | Burkard 2023; Microsoft |
| quasiparticle poisoning (not "immunity"); post-fabrication frequency trimming; adiabatic quantum-flux-parametron (AQFP); flex cable; cooled far below aluminium's superconducting transition (≈1.2 K) | Krantz 2019; Takeuchi et al. |
| MWPM decodes the syndrome history — detection events across rounds — not one syndrome round; a detection event is a check whose outcome changed | Higgott & Gidney 2023 |
| I/O wall (the glossaried name; not "wiring wall") | the Atlas's own concept, one name |
| superconducting-qubit lithography (Al/AlOx/Al junctions, Nb wiring, 300 mm); "superconducting wiring" (not "SC wiring") | the fab_sc and fab_cmos nodes |
| STM hydrogen-resist lithography | Simmons group |
| homodyne detection (quadrature); static nearest-neighbour wiring (not "NN") | vocab labels |
| kept: fluorescence imaging (atom arrays), motional bus, erasure-native (the Atlas's word, now glossaried), erasure-adapted codes, electronic gate (shorthand), gate-defined quantum dot, mid-circuit, heralded, Rydberg blockade, tweezer array, zoned architecture, QCCD, omg, cat qubit, GKP, dual-rail, yoked, iceberg, gross, Relay-BP, Sparse Blossom, cultivation, transversal, break-even, Λ | the field's own terms |

## Abbreviations
Every abbreviation a reader cannot decode gets either a glossary hint (data/glossary-field.json `abbr-*`, shown at the first occurrence per
section in every edition: DARPA, ECCN, CHIPS, LOI, CMOS, RF, HRL, FPGA, GHZ, DAC, ASIC, SQC, DC, cQED, NQCC, EUV, US2QC, mdB, FD-SOI, MBE, TES,
EO, MAGIC, MEMS, STM, HPC, SQUID, SnV, TLS, #AQ, AOM, CVD, MBQC, MZI, QD, SNR, UHV, WISE, EDSR, ESR, HOM, LCD, PMT, QKD, RT, SHYPS, TRL, TSV, XEB,
kT, QFP, CLOPS — with the earlier SNSPD, SPAM, QND, TLS, GKP, DD, QCCD, MWPM, qLDPC, BB, EPLG, RB, QV, QBI, JJ, BP, SFQ, cryo-CMOS, AOD, SLM,
BTO, TFLN, NV, FT, QEC, 1Q/2Q, T1/T2/T2*, NISQ, QCVV, imec, Braket, RSA-2048, ECC-256, THC, QPU) or, when it occurs in fewer than three
documents, its expansion in parentheses at the first mention in the body of that brief (AWG, CCZ, CNN, CR, EOM, HEMT, LC, LER, MOT, OSD, RSFQ,
ERSFQ, SFWM, SNAIL, ZX, tCNOT = teleported CNOT, EMCCD, VIO (QuantWare's vertical-wiring architecture), 2DEG, CROT, DRAG, FP, HHL, IQP, LPCVD,
LUT, MOS, NMR, PEA, PPKTP, QAOA, QE, RoCE, CHSH, CD, LRU, AQFP, SPDC, CNC, RQL, ECDLP). The glossary's `match` lists carry plurals and compound
forms (transmons, cat-qubit, quasiparticles, dilution refrigerators, Mølmer–Sørensen gate, MS gates, spin–photon, T centres, post-selected, CX,
millikelvin, Bell pair, magic-state, SiMOS, FBQC, QPUs…) and `re` context rules where a form is ambiguous (Ge, DC, EO, annealing, carrier,
error suppression, teleportation, modality).

## Glossary definitions
A definition says what the thing is in the field's words, then why it matters to the reader named in `why`, in one or two sentences
(≤ 260 characters); the source in `src`. Seventy definitions were rewritten on 4 Oct 2026 (transmon, fluxonium, Josephson junction, GKP, cat
qubit, dual-rail, SFQ, cryo-CMOS, dilution refrigerator, quasiparticle burst, MS gate, QCCD, Rydberg, donor, AOD, SLM, heralded, SNSPD, BTO,
fusion-based, linear-optical, continuous-variable, Si/SiGe, SiMOS, NV, T1, T2, T2*, EPLG, RB, QCVV, fidelity, coherence, QBI, Genesis Q, qLDPC,
bivariate bicycle, gross code, tesseract, C4-Helix, surface / colour / repetition code, FT, break-even, syndrome, decoder, magic state,
transversal, teleportation, erasure, Majorana, P450, BP, error suppression, QEC cycle, Clifford, ZZ, RSA-2048, FeMoCo, Hubbard, THC, QND,
control modality, post-selection …); the Russian and Hebrew texts follow the English.
