# og:image of the Quantum Technology Map — photo collage

    programme   QT-Map · subproject media-register (SP08) · tier 40_outputs · 2026-09-26
    files       og-image_quantum-technology-map.jpg (1200 × 630, for og:image / twitter:image)
                og-image_quantum-technology-map_titled.jpg (the same with the title, for places that show no title)
    licence     CC BY 4.0 — Raveh Neeman (Qodeh), incorporating the works below
    kind        composite of photographs and micrographs (IPTC digital source type: composite); no generative model

A night sky of quantum hardware, laid out after Vincent van Gogh's *The Starry Night* (1889) but kept
photographic (the editor's choice among thirteen variants on 26 Sep 2026): the dilution refrigerator of a
superconducting quantum computer (IBM Quantum System One) stands where the cypress stands; a flat crystal of a
few hundred trapped ions is the swirl of the sky, the laser light of a strontium atomic clock drifts beside it;
three trapped beryllium ions and a glowing cloud of strontium atoms are stars and the moon, single-photon
detectors a further star; a wafer of superconducting annealing processors and two qubit chips are the village.

## Credit line (for the page that uses the image)

Image: Raveh Neeman, CC BY 4.0; a collage of photographs by OJB Quantum (CC BY 4.0), Steve Jurvetson (CC BY 2.0)
and the U.S. National Institute of Standards and Technology (public domain) — full list:
media-register/40_outputs/og-image/CREDITS.md.

## Works used (all changed: cropped, masked, recoloured toward night blue, blended, ringed with halos)

| Register id | Work | Author | Licence |
|---|---|---|---|
| mr-fb4e3109d3 | [IBM Quantum System One](https://commons.wikimedia.org/wiki/File:IBM_Quantum_System_One.jpg) | OJB Quantum | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| mr-f03a313ab0 | [24 Transmon Qubits Patterned by Direct Write LASER Lithography 002](https://commons.wikimedia.org/wiki/File:24_Transmon_Qubits_Patterned_by_Direct_Write_LASER_Lithography_002.jpg) | OJB Quantum | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| en-aa25554ed9 | [A Wafer of the Latest D-Wave Quantum Computers](https://commons.wikimedia.org/wiki/File:A_Wafer_of_the_Latest_D-Wave_Quantum_Computers_%2839188583425%29.jpg) | Steve Jurvetson | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) |
| en-85055f5d6b | [D-Wave Two 512 qubit Vesuvius chip](https://commons.wikimedia.org/wiki/File:D-Wave_Two_512_qubit_Vesuvius_chip.jpg) | Steve Jurvetson | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) |
| en-2f48c8da6b | [Quantum Simulator Crystal](https://commons.wikimedia.org/wiki/File:Quantum_Simulator_Crystal_%286967363274%29.jpg) | National Institute of Standards and Technology | public domain (US federal work) |
| en-8843b2ca88 | [3D strontium atomic clock](https://commons.wikimedia.org/wiki/File:17jila003_3d_strontium_atomic_clock.jpg) | National Institute of Standards and Technology | public domain (US federal work) |
| en-197d275f84 | [Fourier Transform, Beryllium Ions](https://commons.wikimedia.org/wiki/File:Fourier_Transform%2C_Beryllium_Ions_%285883951063%29.jpg) | National Institute of Standards and Technology | public domain (US federal work) |
| en-f5acc66ca3 | [Strontium Atomic Clock Demonstrates Super-Fine 'Ticks'](https://commons.wikimedia.org/wiki/File:Strontium_Atomic_Clock_Demonstrates_Super-Fine_%27Ticks%27_%285941085880%29.jpg) | National Institute of Standards and Technology | public domain (US federal work) |
| en-701bd3e9ed | [Single Photon Detectors](https://commons.wikimedia.org/wiki/File:Single_Photon_Detectors_%285941086280%29.jpg) | National Institute of Standards and Technology | public domain (US federal work) |

Title type: Cormorant SC SemiBold (SIL Open Font Licence; github.com/google/fonts, ofl/cormorantsc).

## Rebuild

`python3 build/og_image/build_collage.py <folder of the register's local picture copies> <outdir>` — reproduces
the chosen collage pixel for pixel from the register's local copies (`build/og_image/compose.py`), crops it to
1200 × 630 and writes both JPEGs (quality 88). The title needs `CormorantSC.ttf` (from the font repository
above) beside the script or in `FONT`.
