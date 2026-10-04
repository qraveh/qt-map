# -*- coding: utf-8 -*-
"""Technology graph — single source of truth.
Nodes = technologies (not platforms). Layers 1..10. Seven attributes (a..g).
Three spaces kept apart: design (coords), evaluation (dated attrs/defines), actors&goals (annotations).
"""
LAYERS = [
 (1,"carrier","Qubit carrier","Носитель кубита"),
 (2,"encoding","Encoding","Кодирование"),
 (3,"gate","Gate mechanism","Механизм вентиля"),
 (4,"connect","Connectivity / transport","Связность / транспорт"),
 (5,"control","Control","Управление"),
 (6,"readout","Readout","Считывание"),
 (7,"code","Code","Код"),
 (8,"decoder","Decoder","Декодер"),
 (9,"interconnect","Interconnect","Межсоединение"),
 (10,"fab","Manufacturing","Производство"),
]
# attribute vocabularies (design space) -----------------------------------------
AFF = {0.0:("natural","естественный"),0.25:("photon (natural particle, engineered modes)","фотон (естественная частица, искусственно сформированные моды)"),
       0.5:("intermediate / carrier-agnostic","промежуточный / не зависящий от носителя"),0.75:("hybrid (fabricated host)","гибридный (искусственная матрица)"),1.0:("fabricated","искусственный")}
DET = {"det":("deterministic","детерминированное"),"her":("probabilistic / heralded","вероятностное / с оповещением (heralded)"),"na":("n/a","н/п")}
MECH = {"disp":("dispersive microwave","дисперсионное СВЧ"),"fluor":("fluorescence (PMT/SNSPD)","флуоресценция (ФЭУ/SNSPD)"),"img":("fluorescence imaging (camera)","регистрация флуоресценции (камера)"),
        "s2c":("spin-to-charge + rf reflectometry","преобразование спина в заряд + радиочастотная рефлектометрия"),"spd":("single-photon detection","детектирование одиночных фотонов"),"qcap":("rf quantum capacitance (parity)","радиочастотное измерение квантовой ёмкости (чётность)"),
        "erasure":("ancilla erasure check","проверка стирания через анциллу"),"flux":("flux latch (QFP/SQUID)","защёлка потока (QFP/СКВИД)"),"homodyne":("homodyne detection (quadrature)","гомодинное измерение квадратуры"),"none":("—","—")}
MOB = {"static":("static nearest-neighbour wiring","статическая разводка ближайших соседей"),"longrange":("long-range static couplers","дальние статические связи"),"transport":("physical transport","физический транспорт"),
       "bus":("shared bus (motional / cavity)","общая шина (колебательные моды / резонатор)"),"flying":("flying qubits (photons)","летающие кубиты (фотоны)"),"shared":("shared-line crossbar","кроссбар с общими линиями"),"none":("—","—")}
MOD = {"opt":("optical","оптическое"),"mw":("microwave","СВЧ"),"lf":("low-frequency electrical","низкочастотное электрическое"),"eo":("electro-optic","электрооптическое"),"none":("—","—")}
PLACE = {"RT":("room temperature","комнатная"),"4K":("4 K stage","ступень 4 K"),"mK":("millikelvin stage","милликельвиновая ступень"),"none":("—","—")}   # list-valued per node since 17 Sep 2026 (first entry = primary stage); "vac" removed — in-vacuum integration is a location, not a temperature
ERR = {"erasure":("erasure-convertible","преобразуемая в стирание"),"bias":("biased","смещённая"),"pauli":("stochastic Pauli","стохастическая паулиевская"),"coherent":("coherent / calibration","когерентная / калибровочная"),
       "leak":("leakage","утечка"),"burst":("correlated bursts","коррелированные всплески"),"loss":("loss (erasure)","потеря (стирание)"),"gauss":("Gaussian (small-shift)","гауссова (малые сдвиги)"),"unknown":("unknown / contested","неизвестна / оспаривается"),"none":("—","—")}
FAB = {"cmos":("CMOS foundry 300 mm","КМОП-фабрика 300 mm"),"sclitho":("superconducting lithography","литография сверхпроводниковых схем"),"3d":("3D machined cavities","механическая обработка объёмных резонаторов"),"mems":("MEMS / surface-electrode traps","МЭМС / планарные ловушки"),
       "pic":("photonic IC foundry","фабрика ФИС"),"optics":("optical / mechanical assembly","оптическая / механическая сборка"),"mbe":("III-V MBE heterostructures","гетероструктуры A3B5 (МЛЭ)"),"stm":("STM hydrogen-resist lithography","СТМ-литография"),"diamond":("diamond growth / implantation","выращивание алмаза / имплантация"),"none":("—","—")}
STATUS = {"D":("demonstrated","продемонстрировано"),"E":("emerging","формируется"),"T":("theory / design only","только теория / проект"),"X":("empty slot — no technology yet","пустой слот — технологии ещё нет")}
OUT = {"channel":("error channel","канал ошибок"),"clock":("clock (cycle time)","такт (время цикла)"),"count":("count with quality","число кубитов с учётом качества"),"path":("scaling path","путь масштабирования")}

def N(id,layer,en,ru,aff,cls,b_t,det,c,mob,mod,place,f,g,status,den,dru,defines=(),attrs_en="",attrs_ru=""):
    assert isinstance(place,list) and place and all(p in PLACE for p in place), (id,place)   # place is a list: first entry = primary stage
    return dict(id=id,layer=layer,en=en,ru=ru,aff=aff,cls=cls,b=dict(t=b_t,det=det),c=c,d=mob,e=dict(mod=mod,place=place),f=f,g=g,status=status,
                desc=dict(en=den,ru=dru),defines=[dict(out=o,metric=m,value=v,date=d,url=u) for (o,m,v,d,u) in defines],attrs=dict(en=attrs_en,ru=attrs_ru))
def C(mech,t,destr,mid): return dict(mech=mech,t=t,destr=destr,mid=mid)

NODES=[]
# ---------------------------------------------------------------- L1 CARRIER
NODES += [
N("transmon",1,"Transmon","Трансмон",1.0,["fab"],-8.0,"det",C("disp",-6.5,False,True),"static","mw",["RT"],["leak","pauli","burst","coherent"],"sclitho","D",
  "Anharmonic LC oscillator; ~200–300 MHz anharmonicity bounds gates at ~10 ns; T1 ~70–100 µs.","Ангармонический LC-осциллятор; ангармонизм ~200–300 MHz ограничивает вентиль снизу ~10 ns; T1 ~70–100 µs.",
  [("channel","Willow mean T1 / T2,CPMG","68 µs / 89 µs (QEC chip)","2024-12","https://www.nature.com/articles/s41586-024-08449-y"),
   ("channel","Willow mean simultaneous CZ error","0.33 ± 0.18% (spec sheet)","2024-12","https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf"),
   ("channel","correlated burst rate","~1 per hour on the 72-qubit processor (d=29 repetition code, 3×10⁹ cycles); decay ~400 µs; 10⁻¹⁰ logical floor","2024-12","https://arxiv.org/abs/2408.13687")],
  "Willow 105 q; IBM Heron/Nighthawk 156/120 q; Zuchongzhi 3.x 105–107 q.","Willow 105 q; IBM Heron/Nighthawk 156/120 q; Zuchongzhi 3.x 105–107 q."),
N("fluxonium",1,"Fluxonium","Флаксониум",1.0,["fab"],-7.3,"det",C("disp",-6.5,False,True),"static","lf",["RT"],["pauli","coherent"],"sclitho","D",
  "Low-frequency (0.2–1 GHz) superconducting qubit with large anharmonicity; longer T1, flux-biased.","Низкочастотный (0.2–1 GHz) сверхпроводниковый кубит с большим ангармонизмом; больший T1, смещение потоком.",
  [("channel","record 2Q (CNOT, Manucharyan group)","99.94% in 60 ns, > 99.9% over 24 days","2024-07","https://arxiv.org/abs/2407.15783"),
   ("channel","MIT FTF CZ (RL-optimised mean)","99.922%","2023-09","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035")],
  "Atlantic Quantum absorbed by Google (Oct 2025); D-Wave on-chip flux-DAC control on fluxonium (Jan 2026); D-Wave's DR17/DR49/DR181 are dual-rail cavity qubits, not fluxonium.","Atlantic Quantum поглощена Google (окт. 2025); D-Wave — управление флаксониумом через потоковые ЦАП на чипе (янв. 2026); DR17/DR49/DR181 у D-Wave — двухрельсовые кубиты в резонаторах, а не флаксониум."),
N("cavity",1,"Bosonic cavity mode","Бозонная мода резонатора",1.0,["fab"],-6.5,"det",C("disp",-6.0,False,True),"bus","mw",["RT"],["loss","bias"],"3d","D",
  "Harmonic mode of a 3D/planar superconducting resonator; single-photon T1 10 ms (Al, Yale 2013), cavity-qubit T2 34 ms (Weizmann 2023); errors = photon loss (structured).","Гармоническая мода 3D/планарного сверхпроводникового резонатора; T1 фотона 10 ms (Al, Yale 2013), T2 резонаторного кубита 34 ms (Weizmann 2023); ошибки — потеря фотона (структурированная).",
  [("channel","cavity single-photon lifetime (Al, Yale)","10 ms","2013","https://arxiv.org/abs/1302.4408"),
   ("channel","cavity-qubit coherence (Weizmann)","T1 25.6 ms / T2 34 ms","2023-09","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030336")],
  "The 25.6 ms / 34 ms figures are Weizmann (Milul/Rosenblum, PRX Quantum 4, 030336), not a Yale-lineage result; the cavity material is not stated, so 'Nb-coated' is unsupported.","Значения 25.6 ms / 34 ms — Weizmann (Milul/Rosenblum, PRX Quantum 4, 030336), а не результат линии Yale; материал резонатора не указан, поэтому «покрытие Nb» не подтверждено."),
N("ion",1,"Trapped atomic ion","Ион в ловушке",0.0,["nat"],-4.2,"det",C("fluor",-5.0,False,True),"transport","opt",["RT"],["coherent","leak","pauli"],"mems","D",
  "Yb⁺/Ba⁺/Ca⁺ ions in rf traps; motional coupling (MHz) bounds gates at µs; hour-scale memory.","Ионы Yb⁺/Ba⁺/Ca⁺ в РЧ-ловушках; связь через колебательные моды (МГц) ограничивает вентиль снизу микросекундами; память часового масштаба.",
  [("channel","Helios (98 q) 2Q / SPAM","7.9×10⁻⁴ / 4.8×10⁻⁴","2025-11","https://arxiv.org/abs/2511.05465"),
   ("channel","memory","> 1 hour single-qubit coherence","2021","https://arxiv.org/abs/2008.00251")],
  "Quantinuum Helios 98 q; IonQ Tempo 100 q chain.","Quantinuum Helios 98 q; IonQ Tempo — цепочка 100 q."),
N("alkali",1,"Alkali atom (Rb/Cs) in optical tweezers","Щелочной атом (Rb/Cs) в пинцете",0.0,["nat"],-6.6,"det",C("img",-3.3,False,True),"transport","opt",["RT"],["loss","leak","coherent"],"optics","D",
  "Hyperfine qubit; Rydberg interaction (MHz–GHz) allows sub-µs gates; T2 ~1–13 s; dominant error is atom loss.","Сверхтонкий кубит; ридберговское взаимодействие (МГц–ГГц) допускает суб-µs вентили; T2 ~1–13 s; доминирующая ошибка — потеря атома.",
  [("count","atoms with coherence","6,100 Cs atoms, T2 12.6(1) s, 23-min trap lifetime (Caltech)","2024-03","https://arxiv.org/abs/2403.12021"),
   ("count","continuous operation","> 3,000 qubits held > 2 h; 300,000 atoms/s reloaded into tweezers, 30,000 initialised qubits/s","2025-09","https://www.nature.com/articles/s41586-025-09596-6"),
   ("count","trapped (no gates)","11,022 Rb atoms in 18,225 metasurface tweezers","2026-06","https://arxiv.org/abs/2606.02715")],
  "Harvard/QuEra 448-atom FT processor; Gemini 260 q.","Процессор Harvard/QuEra на 448 атомах; Gemini 260 q."),
N("ae_atom",1,"Alkaline-earth(-like) atom (Yb/Sr) — erasure-native","Щёлочноземельный (и подобный ему) атом (Yb/Sr) — естественные стирания",0.0,["nat"],-6.6,"det",C("img",-3.3,False,True),"transport","opt",["RT"],["erasure","loss"],"optics","D",
  "Nuclear-spin / clock-state qubits with metastable levels; decays are detectable → erasures (98% theory, 56% shown).","Кубиты на ядерном спине / часовых состояниях с метастабильными уровнями; распады детектируемы → стирания (98% теория, 56% показано).",
  [("channel","erasure conversion demonstrated","56% of 1Q errors → erasures (¹⁷¹Yb)","2023-05","https://arxiv.org/abs/2305.05493"),
   ("channel","Yb CZ","99.72% post-selected / 99.40% raw","2024-11","https://arxiv.org/abs/2411.11708")],
  "Atom Computing (Yb), Princeton, Caltech (Sr), Pasqal (Rb→?)","Atom Computing (Yb), Princeton, Caltech (Sr)."),
N("photon",1,"Single photon (discrete variable)","Одиночный фотон (дискретные переменные)",0.25,["pho"],-7.0,"her",C("spd",-8.0,True,False),"flying","eo",["RT"],["loss"],"pic","D",
  "Heralded (SFWM) or quantum-dot photons; entangling is probabilistic (fusion); the error is loss = erasure.","Фотоны с оповещением (SFWM) или от квантовых точек; запутывание вероятностное (слияние); ошибка — потеря = стирание.",
  [("channel","source purity / HOM (Omega)","99.5% / 99.5%","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","QD source system efficiency","71.2% (first above 2/3 loss threshold)","2023-11","https://arxiv.org/abs/2311.08347")],
  "", ""),
N("squeezed",1,"Squeezed light mode (CV)","Сжатая мода света (непрерывные переменные)",0.25,["pho"],-6.0,"her",C("spd",-8.0,True,False),"flying","eo",["RT"],["gauss","loss"],"pic","D",
  "Continuous-variable modes for GKP/cluster states; needs ~10 dB *effective* squeezing for FT (0.62 dB on chip today); raw on-chip squeezing is a different quantity (1.4 dB measured on TFLN).","Моды непрерывных переменных для GKP/кластерных состояний; для отказоустойчивости нужно ~10 dB *эффективного* сжатия (сегодня 0.62 dB на чипе); сырое сжатие на чипе — другая величина (1.4 dB измерено на TFLN).",
  [("channel","on-chip GKP effective squeezing (Xanadu)","0.62 dB vs ~9.75 dB required","2025-06","https://www.nature.com/articles/s41586-025-09044-5"),
   ("channel","on-chip raw squeezing (poled TFLN)","1.4 dB measured (> 10 dB loss-corrected)","2025-08","https://arxiv.org/abs/2508.08599")],
  "Xanadu's 0.62 dB is GKP *effective* squeezing, not raw quadrature squeezing — the two are not comparable. The readout attribute is kept as single-photon detection, but CV practice is homodyne detection.","0.62 dB у Xanadu — *эффективное* сжатие GKP, а не сырое квадратурное; величины несопоставимы. Атрибут считывания оставлен как детектирование одиночных фотонов, хотя в практике непрерывных переменных применяется гомодинное детектирование."),
N("qd_spin",1,"Gate-defined quantum-dot spin (Si/SiGe, SiMOS, Ge)","Спин в квантовой точке, формируемой затворами (Si/SiGe, SiMOS, Ge)",1.0,["fab"],-7.3,"det",C("s2c",-5.2,False,True),"static","lf",["RT"],["coherent","pauli","leak"],"cmos","D",
  "Electron/hole spin in a CMOS-fabricated dot; exchange (10–100 MHz) gives ns–100 ns gates; readout via charge sensor.","Спин электрона/дырки в квантовой точке, изготовленной по КМОП-технологии; обмен (10–100 MHz) даёт вентили ns–100 ns; считывание через зарядовый сенсор.",
  [("channel","2Q on 300 mm foundry wafer","99.04–99.56% (Diraq/imec)","2025-09","https://www.nature.com/articles/s41586-025-09531-9"),
   ("count","largest arrays","18 qubits (Groove/QuTech Ge; HRL EO)","2026-04","https://arxiv.org/abs/2604.01063")],
  "Intel, Diraq, Quantum Motion, HRL→IBM, QuTech, Quobly, Equal1.","Intel, Diraq, Quantum Motion, HRL→IBM, QuTech, Quobly, Equal1."),
N("donor",1,"Donor spin (P in ²⁸Si)","Донорный спин (P в ²⁸Si)",0.5,["int"],-6.0,"det",C("s2c",-5.0,False,True),"static","lf",["RT"],["pauli"],"stm","D",
  "STM-placed phosphorus atoms; nuclear qubits gated through a shared electron's hyperfine coupling; no foundry path.","Атомы фосфора, размещённые методом СТМ; ядерные кубиты управляются через сверхтонкую связь с общим электроном; нет фабричного пути.",
  [("channel","nuclear-spin gates (range reported)","99.5–99.99%; Bell > 99% (single 99.90(4)% CZ not isolable in the abstract)","2025-12","https://www.nature.com/articles/s41586-025-09827-w")],
  "SQC (Australia), founded 2017; the first deterministically placed single-donor device is UNSW/Simmons (2012). ²⁸Si feedstock from ASP Isotopes and DOE/ORNL.","SQC (Австралия), основана в 2017; первое устройство с детерминированно размещённым одиночным донором — UNSW/Simmons (2012). Сырьё ²⁸Si — ASP Isotopes и DOE/ORNL."),
N("defect",1,"Colour-centre / defect spin (NV, SiV, SnV, T centre)","Центр окраски / спин дефекта (NV, SiV, SnV, T-центр)",0.5,["int"],-6.0,"det",C("fluor",-4.0,False,True),"flying","opt",["RT"],["pauli","loss"],"diamond","D",
  "Optically addressable spin in a solid host; network node with spin–photon interface rather than a processor qubit.","Оптически адресуемый спин в твердотельной матрице; узел сети со спин-фотонным интерфейсом, а не процессорный кубит.",
  [("channel","NV gate errors (GST)","< 0.1% [P] — press release only, no primary paper","2025-03","https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/")],
  "QuTech/Fujitsu, Harvard, Photonic Inc (T centres), Quantum Brilliance. Element Six's DNV-B1 is an NV-*ensemble* sensing grade, not a single-defect node substrate.","QuTech/Fujitsu, Harvard, Photonic Inc (T-центры), Quantum Brilliance. DNV-B1 от Element Six — сенсорный сорт для *ансамблей* NV, а не подложка для узлов на одиночных дефектах."),
N("majorana",1,"Majorana parity (InAs–Pb tetron)","Майорановская чётность (тетрон InAs–Pb)",1.0,["fab"],-6.0,"det",C("qcap",-4.0,False,True),"static","lf",["RT"],["unknown"],"mbe","E",
  "Gate-defined nanowire device; only single-wire parity readout demonstrated; topological protection contested.","Нанопроволочное устройство, формируемое затворами; продемонстрировано только считывание чётности одной проволоки; топологическая защита оспаривается.",
  [("channel","single-nanowire parity switching time","22 ± 1 s Z-parity lifetime in one wire of one tetron (not a qubit lifetime); two-loop device Z 12.4 ms vs X 14.5 µs (2025)","2026-06","https://arxiv.org/abs/2606.03884")],
  "Microsoft; no two-qubit operation, no Bell test. DARPA US2QC: final Validation & Co-Design stage since 2025-02-06 (not QBI Stage B).","Microsoft; нет двухкубитной операции, нет теста Белла. DARPA US2QC: финальная стадия Validation & Co-Design с 2025-02-06 (не QBI Stage B)."),
N("fluxq",1,"rf-SQUID flux qubit (annealer)","Потоковый кубит на ВЧ-СКВИДе (отжигатель)",1.0,["fab"],-8.5,"na",C("disp",-6.0,False,False),"longrange","lf",["mK"],["pauli","coherent"],"sclitho","D",
  "Analog-Hamiltonian carrier; 4,400+ qubits with 20-way Zephyr coupling; not a gate-model qubit.","Носитель аналогового гамильтониана; 4 400+ кубитов со связностью Zephyr 20; не вентильный кубит.",
  [("count","Advantage2","4,400+ qubits, degree 20","2025-05","https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/")],"D-Wave.","D-Wave."),
]
# ---------------------------------------------------------------- L2 ENCODING
NODES += [
N("enc_bare",2,"Bare physical qubit (no encoding)","«Голый» физический кубит (без кодирования)",1.0,["fab"],None,"na",None,"none","none",["none"],["leak"],"none","D",
  "Computational subspace of an anharmonic oscillator; leakage to |2⟩ is the price.","Вычислительное подпространство ангармонического осциллятора; цена — утечка в |2⟩.",
  [("channel","leakage suppression","72× (all-microwave reset), residual 6.4×10⁻⁴ after 40 cycles","2025-12","https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31")],
  "USTC leakage suppression = PRL 135, 260601 (2025-12-22), Λ = 1.40(6) at d=7; the paper does not name the processor 'Zuchongzhi 3.2'.","Подавление утечки USTC — PRL 135, 260601 (2025-12-22), Λ = 1.40(6) при d=7; в статье процессор «Zuchongzhi 3.2» не назван."),
N("enc_hf",2,"Hyperfine / clock-state qubit","Сверхтонкий кубит / кубит на часовом переходе",0.0,["nat"],None,"na",None,"none","none",["none"],["pauli","leak"],"none","D",
  "Ground-state hyperfine (or nuclear-spin) levels of atoms and ions; second-to-hour coherence.","Сверхтонкие (или ядерно-спиновые) уровни основного состояния атомов и ионов; когерентность от секунд до часов.",
  [("channel","leakage per 1Q Clifford (Helios)","1.1×10⁻⁵","2025-11","https://arxiv.org/abs/2511.05465")],"",""),
N("enc_opt",2,"Optical narrow-line qubit (ion S–D, atom clock)","Оптический кубит на узком переходе (S–D иона, часовой переход атома)",0.0,["nat"],None,"na",None,"none","none",["none"],["pauli","leak"],"none","D",
  "Qubit on an optical transition to a metastable level: the S₁/₂–D₅/₂ quadrupole line of an alkaline-earth ion (⁴⁰Ca⁺ at 729 nm, ⁸⁸Sr⁺ at 674 nm) or the ¹S₀–³P₀ clock line of a neutral Sr/Yb atom. One narrow-line laser drives every gate; coherence is bounded by the upper level's lifetime and the laser's phase noise, not by hyperfine structure — the classic Innsbruck encoding, still the AQT product's, and planqc's clock qubit.","Кубит на оптическом переходе в метастабильный уровень: квадрупольная линия S₁/₂–D₅/₂ иона щёлочноземельного металла (⁴⁰Ca⁺ на 729 nm, ⁸⁸Sr⁺ на 674 nm) или часовая линия ¹S₀–³P₀ нейтрального атома Sr/Yb. Один узкополосный лазер делает все вентили; когерентность ограничена временем жизни верхнего уровня и фазовым шумом лазера, а не сверхтонкой структурой — классическое инсбрукское кодирование, до сих пор в продукте AQT, и кубит на часовом переходе planqc.",
  [("channel","D₅/₂ lifetime (⁴⁰Ca⁺), the encoding's ceiling","τ = 1.17 s (AQT demonstrator, ⁴⁰Ca⁺ |4S₁/₂,m=−1/2⟩–|3D₅/₂,m=−1/2⟩ at 729 nm)","2021-01","https://arxiv.org/abs/2101.11390")],
  "Register carriers: AQT IBEX Q1, PSNC PIAST-Q (an AQT system), Innsbruck (⁴⁰Ca⁺ S–D); planqc MAQCS (Sr clock qubit — resolves the register's gap G-enc-clock). Hyperfine-free ⁴⁰Ca⁺ has no field-insensitive clock transition, so its T2 rests on magnetic shielding and laser stability; the atomic clock line is field-insensitive but laser-linewidth-limited; the 'omg' erasure proposal reuses the same metastable manifold.","Носители в реестре: AQT IBEX Q1, PSNC PIAST-Q (система AQT), Инсбрук (S–D ⁴⁰Ca⁺); planqc MAQCS (кубит на часовом переходе Sr — закрывает пробел реестра G-enc-clock). У ⁴⁰Ca⁺ нет сверхтонкой структуры и нечувствительного к полю часового перехода, поэтому его T2 держится на магнитном экранировании и стабильности лазера; атомная часовая линия нечувствительна к полю, но ограничена шириной линии лазера; предложение кодирования со стираниями «omg» использует то же метастабильное многообразие."),
N("enc_gr",2,"Ground–Rydberg analog qubit","Аналоговый кубит основное–ридберговское состояние",0.0,["nat"],None,"na",None,"none","none",["none"],["loss","coherent"],"none","D",
  "The two computational states are a ground level and a Rydberg level: the native encoding of an analog Rydberg machine, whose limit is the Rydberg lifetime (~100 µs), not hyperfine coherence.","Два вычислительных состояния — основной уровень и ридберговский: собственное кодирование аналоговой ридберговской машины; предел — время жизни ридберговского состояния (~100 µs), а не сверхтонкая когерентность.",
  (),"Coherence is bounded by the Rydberg lifetime and laser phase noise; there is no shelved memory.","Когерентность ограничена временем жизни ридберговского состояния и фазовым шумом лазера; защищённой памяти нет."),
N("enc_omg",2,"Metastable ('omg') erasure encoding","Метастабильное («omg») кодирование со стираниями",0.0,["nat"],None,"na",None,"none","none",["none"],["erasure"],"none","E",
  "Qubit in metastable manifold so that decay leaves the subspace detectably; ions (proposal) and Yb atoms (shown).","Кубит в метастабильном многообразии: распад выводит из подпространства детектируемо; ионы (предложение) и атомы Yb (показано).",
  [("channel","erasure fraction (theory)","98% of errors convertible (¹⁷¹Yb)","2022-01","https://arxiv.org/abs/2201.03540"),
   ("channel","[[4,2,2]] with erasure info","logical decay 1.9(4)× slower (unconditional decoding)","2026-06","https://arxiv.org/abs/2506.13724")],
  "The 3.6(1)× often quoted is the post-selected hold; the architecturally relevant figure is the unconditional 1.9(4)× (arXiv:2506.13724 v1 and v2).","Часто цитируемое 3.6(1)× относится к постселектированному удержанию; архитектурно значимо безусловное 1.9(4)× (arXiv:2506.13724 v1 и v2)."),
N("enc_dualrail",2,"Dual-rail (erasure) encoding","Двухрельсовое кодирование (со стираниями)",0.25,["fab","pho"],None,"na",None,"none","none",["none"],["erasure"],"none","D",
  "One excitation in two modes/transmons/cavities; loss leaves the codespace → detected as erasure (80–90% of gate errors).","Одно возбуждение в двух модах/трансмонах/резонаторах; потеря выводит из кодового пространства → детектируется как стирание (80–90% ошибок вентиля).",
  [("channel","cavity dual-rail CZ","erasure 0.53%/gate, residual Pauli < 0.1%, 500 ns","2026-08","https://www.nature.com/articles/s41586-026-10822-y"),
   ("channel","transmon dual-rail","erasure 2.5×10⁻²/check, residual 6×10⁻⁴, bias 42","2026-04","https://arxiv.org/abs/2604.16292")],
  "D-Wave/QCI (Aqumen), AWS, SUSTech (four transmons, not cavities); photonic dual-rail is native.","D-Wave/QCI (Aqumen), AWS, SUSTech (четыре трансмона, не резонаторы); для фотонов двухрельсовое кодирование естественно."),
N("enc_cat",2,"Cat-code encoding (biased noise)","Кошачье кодирование (смещённый шум)",1.0,["fab"],None,"na",None,"none","none",["none"],["bias"],"none","D",
  "Two-photon-dissipation-stabilised coherent states; bit-flips exponentially suppressed, phase-flips grow ∝ n̄.","Когерентные состояния, стабилизированные двухфотонной диссипацией; перевороты бита подавлены экспоненциально, перевороты фазы растут ∝ n̄.",
  [("channel","bit-flip time","44 min mean (12-cat chip, preliminary); 22 s squeezed cat","2025-09","https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record"),
   ("channel","phase-flip per CX (Ocelot)","9.6(4)×10⁻² at n̄=2 (bit-flip 3.5(4)×10⁻³); bias > 25 under the gate, > 30 idle","2025-02","https://www.nature.com/articles/s41586-025-08642-7")],
  "Alice & Bob (DARPA QBI Stage A only), AWS. The '27–33' figures quoted elsewhere are phase-flip *times* in µs, not bias values.","Alice & Bob (DARPA QBI только Stage A), AWS. Числа «27–33», встречающиеся в других местах, — это *времена* переворота фазы в µs, а не значения смещения."),
N("enc_gkp",2,"GKP grid encoding","GKP-кодирование (решётка)",0.75,["fab","pho"],None,"na",None,"none","none",["none"],["gauss"],"none","E",
  "Grid states in a bosonic (microwave cavity) or optical mode; corrects small shifts; needs ~10 dB squeezing.","Решёточные состояния в бозонной (СВЧ-резонатор) или оптической моде; исправляет малые сдвиги; нужно ~10 dB сжатия.",
  [("channel","single-mode GKP logical error","8.1×10⁻³/round (survival 0.24×0.39)","2026-07","https://arxiv.org/abs/2607.06718"),
   ("channel","GKP qudit gain beyond break-even (UCSB + Google)","1.82–1.87","2025-05","https://www.nature.com/articles/s41586-025-08899-y"),
   ("channel","best bosonic memory gain (GKP, Yale)","2.27(7)","2023-03","https://www.nature.com/articles/s41586-023-05782-6")],
  "Nord Quantique (microwave), Xanadu (optical). The GKP-qudit work is Brock et al. (UC Santa Barbara + Google, Nature 641, 612), not Yale; Nord Quantique's magic-state SPAM is 8(5)×10⁻³ (7(7)×10⁻⁴ on cardinal states).","Nord Quantique (СВЧ), Xanadu (оптика). Работа по GKP-кудитам — Brock et al. (UC Santa Barbara + Google, Nature 641, 612), а не Yale; SPAM магических состояний у Nord Quantique — 8(5)×10⁻³ (7(7)×10⁻⁴ на кардинальных состояниях)."),
N("enc_eo",2,"Exchange-only / singlet–triplet spin encoding","Чисто обменное / синглет-триплетное спиновое кодирование",1.0,["fab"],None,"na",None,"none","none",["none"],["leak","coherent"],"none","D",
  "Encoded spin qubits controlled purely by baseband exchange pulses; leakage 0.015%/Clifford (AEON).","Кодированные спиновые кубиты, управляемые только импульсами обмена в основной полосе частот; утечка 0.015%/Клиффорд (AEON).",
  [("channel","EO 1Q error (18 qubits)","2×10⁻⁴ mean","2026-07","https://arxiv.org/abs/2604.16216")],"HRL → IBM.","HRL → IBM."),
N("enc_timebin",2,"Time-bin / path photonic encoding","Time-bin / путевое фотонное кодирование",0.25,["pho"],None,"na",None,"none","none",["none"],["loss"],"none","D",
  "Photonic dual-rail in time or path; loss is the error and it is heralded.","Фотонное двухрельсовое кодирование во времени или по пути; ошибка — потеря, и она сопровождается оповещением.",[],
  "Origin: Brendel, Gisin, Tittel and Zbinden, Phys. Rev. Lett. 82, 2594 (1999). No mobility of its own — the attribute is 'none', inherited from the host carrier.","Происхождение: Brendel, Gisin, Tittel, Zbinden, Phys. Rev. Lett. 82, 2594 (1999). Собственной подвижности нет — атрибут «—», наследуется от носителя."),
N("enc_parity",2,"Fermion-parity encoding (tetron)","Кодирование в фермионной чётности (тетрон)",1.0,["fab"],None,"na",None,"none","none",["none"],["unknown"],"none","T",
  "Qubit in joint parity of two Majorana wires; X-measurement lifetime 1000× shorter than Z in 2025 data.","Кубит в совместной чётности двух майорановских проволок; время жизни X-измерения в 1000 раз короче Z (данные 2025).",
  [("channel","Z / X parity lifetimes","12.4 ms / 14.5 µs in the quoted tuning (~9.3 ms / ~4 µs in others; the ~10³ ratio is robust, the point values are not)","2025-07","https://arxiv.org/abs/2507.08795")],
  "The gap is attributed to the larger quasiparticle-capture cross-section of the two-wire X loop — flux noise is not the stated cause. DARPA US2QC: final Validation & Co-Design stage since 2025-02-06, not QBI Stage B.","Разрыв объясняется большим сечением захвата квазичастиц у двухпроволочной X-петли — потоковый шум как причина в статье не назван. DARPA US2QC: финальная стадия Validation & Co-Design с 2025-02-06, не QBI Stage B."),
]
# ---------------------------------------------------------------- L3 GATE MECHANISM
NODES += [
N("g_tc",3,"Tunable-coupler CZ / iSWAP","CZ / iSWAP через перестраиваемый элемент связи",1.0,["fab"],-7.4,"det",None,"static","mw",["RT"],["coherent","leak","pauli"],"sclitho","D",
  "Flux-tunable coupler switches ZZ/exchange on and off; 30–70 ns gates.","Перестраиваемый потоком элемент связи включает/выключает ZZ/обмен; вентили 30–70 ns.",
  [("channel","record CZ (tunable coupler, IQM)","99.93% over 40 h","2025-08","https://arxiv.org/abs/2508.16437"),
   ("channel","record CZ (double-transmon coupler)","99.90% in 48 ns","2024-11","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050"),
   ("clock","gate time (Willow)","~30 ns CZ","2024-12","https://www.nature.com/articles/s41586-024-08449-y"),
   ("channel","fleet EPLG (full width)","best 0.19% (ibm_boston), typical 0.37%","2026-07","https://www.ibm.com/quantum/blog/whats-new-q2-2026")],
  "The often-quoted Oxford '25 ns at 99.8%' is a fixed-coupling coaxmon pair with no tunable coupler and does not belong to this node.","Часто цитируемое оксфордское «25 ns при 99.8%» — пара coaxmon с фиксированной связью, без перестраиваемого элемента связи; к этому узлу не относится."),
N("g_cr",3,"Cross-resonance (fixed-frequency, all-microwave)","Кросс-резонанс (фиксированная частота, только СВЧ)",1.0,["fab"],-6.5,"det",None,"static","mw",["RT"],["coherent","pauli"],"sclitho","D",
  "Microwave-only entangling gate on fixed-frequency transmons; 180–500 ns; superseded by tunable couplers in IBM Heron.","Чисто СВЧ вентиль на трансмонах фиксированной частоты; 180–500 ns; вытеснен перестраиваемыми элементами связи в IBM Heron.",
  [("channel","CR CNOT with intrinsic static-ZZ suppression (Kandala)","99.77(2)% in a single 180 ns pulse","2021","https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501")],
  "Kandala 2021 suppresses the static ZZ intrinsically (two fixed coupling elements retuning the dressed levels), not by an active cancellation drive; the pulse is 180 ns, not 320 ns. CR stayed IBM's native gate through Condor; Heron introduced the tunable-coupler CZ.","Kandala 2021 подавляет статический ZZ внутренне (два фиксированных элемента связи перестраивают одетые уровни), а не активным компенсирующим драйвом; импульс 180 ns, не 320 ns. Кросс-резонансный вентиль (CR) оставался основным вентилем IBM вплоть до Condor; CZ на перестраиваемом элементе связи появился в Heron."),
N("g_ryd",3,"Rydberg-blockade CZ","CZ через ридберговскую блокаду",0.0,["nat"],-6.6,"det",None,"transport","opt",["RT"],["loss","leak","coherent"],"optics","D",
  "Global Rydberg pulses entangle neighbouring atoms; 270 ns; fast for a natural carrier.","Глобальные ридберговские импульсы запутывают соседние атомы; 270 ns; быстро для естественного носителя.",
  [("channel","record CZ","99.854% raw / 99.941% loss-post-selected","2026-04","https://arxiv.org/abs/2604.25987"),
   ("clock","gate time","270 ns","2025-06","https://arxiv.org/abs/2506.20661")],"",""),
N("g_rydanalog",3,"Analog Rydberg Hamiltonian evolution","Аналоговая эволюция под ридберговским гамильтонианом",0.0,["nat"],None,"na",None,"none","opt",["RT"],["coherent","loss"],"optics","D",
  "Global laser fields drive a programmable Ising/XY Hamiltonian on the whole array at once — no discrete entangling gate, no circuit; the geometry of the tweezer pattern is the program.","Глобальные лазерные поля задают программируемый гамильтониан Изинга/XY сразу на всём массиве — без дискретного запутывающего вентиля и без схемы; программа — геометрия массива пинцетов.",
  (),"Figures of merit are the many-body coherence time, the number of atoms and the range of programmable geometries, not a gate fidelity.","Показатели — время многочастичной когерентности, число атомов и диапазон программируемых геометрий, а не точность вентиля."),
N("g_ms",3,"Mølmer–Sørensen / light-shift laser gate","Вентиль Мёльмера–Соренсена / на световом сдвиге (лазерный)",0.0,["nat"],-4.2,"det",None,"bus","opt",["RT"],["coherent","leak","pauli"],"optics","D",
  "Laser-driven spin-motion coupling; 70 µs (Helios) to 550–880 µs (IonQ Forte chains); 1.6 µs record.","Лазерная связь спин–движение; 70 µs (Helios) — 550–880 µs (цепочки IonQ Forte); рекорд 1.6 µs.",
  [("channel","Helios 2Q","7.9×10⁻⁴ in ~70 µs","2025-11","https://arxiv.org/abs/2511.05465"),
   ("clock","IonQ Forte MS duration (30-ion chain, all 435 pairs)","550–883 µs (median 672 µs)","2023-08","https://arxiv.org/abs/2308.05071"),
   ("clock","fastest laser gate (Schäfer et al., Oxford)","99.8% at 1.6 µs","2018","https://arxiv.org/abs/1709.06952")],
  "The 1.6 µs record is Schäfer et al. (Oxford, Nature 555, 2018), not Ballance. The Forte figure is one 30-ion chain benchmarked over all 435 pairs.","Рекорд 1.6 µs — Schäfer et al. (Oxford, Nature 555, 2018), а не Ballance. Данные Forte — одна цепочка из 30 ионов, промерены все 435 пар."),
N("g_elec",3,"Electronic microwave gate (ions, laser-free: near-field or static gradient)","Электронный СВЧ-вентиль (ионы, без лазера: ближнее поле или статический градиент)",1.0,["nat"],-3.7,"det",None,"bus","mw",["RT"],["pauli","coherent"],"mems","D",
  "Chip currents create microwave gradients; no lasers for gates, no ground-state cooling; 120–226 µs.","Токи на чипе создают СВЧ-градиенты; без лазеров для вентилей, без охлаждения в основное состояние; 120–226 µs.",
  [("channel","record 2Q","8.4×10⁻⁵ without ground-state cooling","2025-10","https://arxiv.org/abs/2510.17286"),
   ("clock","gate duration","225.8 µs (2025); ≈120 µs in 2024 (two 60 µs pulses, arXiv:2407.07694)","2025-10","https://arxiv.org/html/2510.17286")],"Oxford Ionics → IonQ.","Oxford Ionics → IonQ."),
N("g_exch",3,"Exchange gate (spins; incl. shuttled-spin CZ)","Обменный вентиль (спины; вкл. CZ на переносимых спинах)",1.0,["fab"],-7.0,"det",None,"static","lf",["RT"],["coherent","pauli","leak"],"cmos","D",
  "Voltage-pulsed exchange J (10–90 MHz); 58–500 ns; ~80% of error is calibration/control (HRL).","Обмен J (10–90 MHz) под импульсами напряжения; 58–500 ns; ~80% ошибки — калибровка/управление (HRL).",
  [("channel","foundry CZ","99.04–99.56% (300 mm)","2025-09","https://www.nature.com/articles/s41586-025-09531-9"),
   ("channel","EO CNOT best / mean","9×10⁻⁴ / 3×10⁻³","2026-07","https://arxiv.org/abs/2604.16216"),
   ("clock","mobile-spin CZ","98.86% in 58 ns","2026-05","https://www.nature.com/articles/s41586-026-10423-9")],
  "Best exchange gate is HRL's exchange-only CNOT at 9×10⁻⁴; SQC (Nature 2025): nuclear CZ 99.90(4)%, 1Q 99.10–99.99%, Bell 91.4–99.5% local and 87.0–97.0% non-local — no Bell > 99%.","Лучший обменный вентиль — чисто обменный CNOT у HRL, 9×10⁻⁴; SQC (Nature 2025): ядерный CZ 99.90(4)%, однокубитные 99.10–99.99%, Bell 91.4–99.5% локально и 87.0–97.0% нелокально — никакого Bell > 99%."),
N("g_fusion",3,"Linear-optical fusion (heralded)","Линейно-оптическое слияние (с оповещением)",0.25,["pho"],-7.0,"her",None,"flying","eo",["RT"],["loss"],"pic","D",
  "Probabilistic Bell measurement on photons (50%, 75% boosted); failure is heralded → erasure.","Вероятностное измерение Белла на фотонах (50%, 75% с усилением); неудача сопровождается оповещением → стирание.",
  [("channel","fusion Bell fidelity","99.22%","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],"",""),
N("g_lointer",3,"Programmable linear-optical interferometer (no entangling primitive)","Программируемый линейно-оптический интерферометр (без запутывающего примитива)",0.25,["pho"],None,"na",None,"flying","eo",["RT"],["loss"],"optics","D",
  "A mesh of beamsplitters and phase shifters, or a time-multiplexed fibre loop, that scatters photons or squeezed light for sampling; it implements no entangling gate and no correction, so a machine built on it is a sampler, not a computer.","Сетка светоделителей и фазовращателей или волоконная петля с временным мультиплексированием, рассеивающая фотоны или сжатый свет для сэмплирования; ни запутывающего вентиля, ни коррекции — машина на нём сэмплер, а не компьютер.",
  (),"Loss per element and the number of modes set what can be sampled; classical spoofing of lossy samplers is the standing challenge.","Потери на элемент и число мод определяют, что можно сэмплировать; классическая имитация сэмплеров с потерями — постоянный вызов."),
N("g_bos",3,"Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beamsplitter)","Бозонные вентили через анциллу (CX кошачьих кубитов, CZ двухрельсовых, светоделитель)",1.0,["fab"],-6.3,"det",None,"bus","mw",["RT"],["erasure","bias","pauli"],"3d","D",
  "Transmon ancilla, or a differentially driven DC-SQUID beamsplitter coupler between modes; ~500 ns.","Анцилла-трансмон либо элемент связи типа светоделителя на дифференциально управляемом ПТ-СКВИДе между модами; ~500 ns.",
  [("channel","dual-rail cavity CZ","post-selected infidelity 0.029% (bound 0.12%), 500 ns","2026-08","https://www.nature.com/articles/s41586-026-10822-y"),
   ("channel","cavity beamsplitter (DC-SQUID coupler)","> 99.98%, ~100 ns swaps","2023-03","https://arxiv.org/abs/2303.00959")],
  "The beamsplitter coupler of arXiv:2303.00959 is a differentially driven DC-SQUID, not a SNAIL. Quantum Circuits was never in DARPA QBI; Alice & Bob reached Stage A only.","Элемент связи типа светоделителя в arXiv:2303.00959 — дифференциально управляемый ПТ-СКВИД, а не SNAIL. Quantum Circuits никогда не входила в DARPA QBI; Alice & Bob дошла только до Stage A."),
N("g_mbq",3,"Measurement-based Majorana gate","Майорановский вентиль через измерения",1.0,["fab"],None,"det",None,"static","lf",["RT"],["unknown"],"mbe","X",
  "Braiding by sequences of parity measurements — nothing demonstrated; single-wire readout only.","Плетение последовательностями измерений чётности — ничего не продемонстрировано; только считывание одной проволоки.",
  [("channel","status","no two-qubit operation, no entanglement","2026-06","https://arxiv.org/abs/2606.03884")],"",""),
N("g_anneal",3,"Quantum annealing (analog evolution)","Квантовый отжиг (аналоговая эволюция)",1.0,["fab"],-8.4,"na",None,"longrange","lf",["mK"],["coherent","pauli"],"sclitho","D",
  "Coherent quenches 3.6–27 ns on 1,222–5,627 qubits; not a gate.","Когерентные квенчи 3.6–27 ns на 1 222–5 627 кубитах; не вентиль.",
  [("clock","coherent quench","3.6–27 ns","2025-03","https://arxiv.org/abs/2403.00910")],
  "Pasqal's 10,000 physical qubits slipped from 2026 to 2028 (100 logical in 2029); QuEra's Series B expansion closed 2025-09-09 (Google, SoftBank Vision Fund 2, NVentures); Quantinuum's magnetism result is Trotterised *digital* simulation, not analog evolution.","10 000 физических кубитов Pasqal сдвинуты с 2026 на 2028 (100 логических — 2029); расширение раунда серии B у QuEra закрыто 2025-09-09 (Google, SoftBank Vision Fund 2, NVentures); результат Quantinuum по магнетизму — троттеризованная *цифровая* симуляция, а не аналоговая эволюция."),
]
# ---------------------------------------------------------------- L4 CONNECTIVITY / TRANSPORT
NODES += [
N("cx_nn",4,"Static nearest-neighbour lattice","Статическая решётка со связью ближайших соседей",1.0,["fab"],None,"na",None,"static","none",["none"],["coherent"],"sclitho","D",
  "Heavy-hex (degree 2.3) or square lattice (degree 3.5–3.6) with on-chip couplers; ZZ crosstalk is the tax.","Решётка heavy-hex (степень 2.3) или квадратная решётка (степень 3.5–3.6) с элементами связи на чипе; налог — перекрёстные помехи ZZ.",
  [("count","Nighthawk","120 q, 218 couplers, 5,000 2Q gates/circuit","2025-11","https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance"),
   ("channel","CZ crosstalk (fitted budget term, Willow d=7)","5.5×10⁻⁴","2024-08","https://arxiv.org/abs/2408.13687")],
  "The 5.5×10⁻⁴ is a fitted component of the Willow error budget, not a directly measured crosstalk figure. EUV is a single point of failure for the spin branch only — no fielded transmon lattice uses it. Rigetti: median 2Q 99.5% at 36 q falls to 99.1% at 108 q (12 chiplets).","5.5×10⁻⁴ — подобранная компонента бюджета ошибок Willow, а не напрямую измеренные перекрёстные помехи. EUV — единая точка отказа только для спиновой ветви: ни одна работающая трансмонная решётка её не использует. Rigetti: медианная точность двухкубитного вентиля 99.5% при 36 q падает до 99.1% при 108 q (12 чиплетов)."),
N("cx_lr",4,"Long-range on-chip couplers (c-couplers, mm-scale)","Дальние элементы связи на чипе (c-couplers, mm-масштаб)",1.0,["fab"],None,"na",None,"longrange","none",["none"],["coherent"],"sclitho","E",
  "Resonator/coupler links beyond NN; enables degree-6 qLDPC layouts; 2 mm CZ 99.81% (IQM); IBM Loon components without numbers.","Связи через резонаторы/элементы связи дальше ближайших соседей; открывает qLDPC-разводки степени 6; CZ на 2 mm 99.81% (IQM); компоненты IBM Loon без чисел.",
  [("path","long-range CZ","99.81% over ≥ 2 mm","2023","https://arxiv.org/abs/2208.09460"),
   ("path","IBM Loon","c-couplers + multilayer routing shown, no performance numbers","2025-11","https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance")],"",""),
N("cx_qccd",4,"Ion shuttling (QCCD, junctions, grid traps)","Перемещение ионов (QCCD, перекрёстки, решётчатые ловушки)",0.0,["nat"],-1.3,"na",None,"transport","none",["none"],["coherent"],"mems","D",
  "Ions moved between zones at m/s with sub-quantum heating; transport + cooling dominate runtime (55 ms per full layer on Helios).","Ионы перемещаются между зонами со скоростью порядка m/s при нагреве меньше кванта; транспорт + охлаждение доминируют во времени (55 ms на полный слой Helios).",
  [("clock","time per full-width layer (Helios)","~55 ms","2025-11","https://arxiv.org/html/2511.05465v1"),
   ("path","junction transport","4 m/s, 0.013–0.03 quanta/round trip","2022","https://arxiv.org/abs/2206.11888"),
   ("path","grid-trap ion exchange","2.5 kHz","2024-03","https://arxiv.org/abs/2403.00756"),
   ("path","two-module matter link (Universal Quantum)","2,424 transfers/s, loss infidelity < 7×10⁻⁸","2023-02","https://www.nature.com/articles/s41467-022-35285-3")],
  "A chip-to-chip matter link between two ion-trap modules exists (Universal Quantum, Nat. Commun. 14, 531, 2023); the empty slot here is a link across more than two modules, not chip-to-chip itself.","Межчиповый канал переноса ионов между двумя модулями ионных ловушек существует (Universal Quantum, Nat. Commun. 14, 531, 2023); пустой слот здесь — связь более чем двух модулей, а не сама стыковка чип-чип."),
N("cx_bus",4,"Ion-chain motional bus (all-to-all in chain)","Шина на колебательных модах ионной цепочки (все со всеми в цепочке)",0.0,["nat"],-3.2,"na",None,"bus","none",["none"],["coherent"],"mems","D",
  "Shared motional modes give all-to-all within one chain; gates slow with chain length (median 672 µs on Forte's 30-ion chain).","Общие колебательные моды дают связность «все со всеми» внутри одной цепочки; вентили замедляются с её длиной (медиана 672 µs на 30-ионной цепочке Forte).",
  [("count","independently benchmarked chain (Forte)","30 ions, all 435 pairs","2023-08","https://arxiv.org/abs/2308.05071"),
   ("count","largest claimed chain (Tempo)","100 ions, #AQ 64 [C] — a company claim, no per-pair data","2025-10","https://ionq.com/quantum-systems/tempo")],
  "IonQ Forte is a 30-ion chain (435 pairs), not 36; the 100-ion all-to-all Tempo chain is a company claim with no published gate time or per-pair fidelity.","IonQ Forte — цепочка из 30 ионов (435 пар), а не 36; 100-ионная цепочка Tempo со связностью «все со всеми» — заявление компании без опубликованного времени вентиля и попарной точности."),
N("cx_aod",4,"Atom transport by AOD tweezers (zoned architecture)","Транспорт атомов пинцетами на АОД (зонная архитектура)",0.0,["nat"],-3.0,"na",None,"transport","none",["none"],["loss"],"optics","D",
  "Coherence-preserving moves of 100s µm in 0.4–1.6 ms at ~99.95%; storage/entangling/readout zones.","Сохраняющие когерентность перемещения на сотни µm за 0.4–1.6 ms при ~99.95%; зоны хранения/запутывания/считывания.",
  [("clock","move time","610 µm in 1.6 ms at 99.95%; 270 µm in 400 µs at 99.8%","2025-09","https://arxiv.org/abs/2403.12021"),
   ("count","zoned FT processor","448 atoms, 256 in entangling zone","2025-11","https://www.nature.com/articles/s41586-025-09848-5")],
  "Harvard's continuously reloaded 3,000-atom system moves atoms ~0.5 m on optical-lattice conveyor belts, using AOD tweezers only for local rearrangement. TU/e's 3D acousto-optic lensing (arXiv:2510.09398) is a design study [S] with no atoms.","Система Harvard на 3 000 атомов с непрерывной дозагрузкой перемещает атомы на ~0.5 m оптическими решёточными конвейерами, а пинцеты на АОД использует только для локальной перестановки. Трёхмерная акустооптическая фокусировка из TU/e (arXiv:2510.09398) — расчётная работа [S], без атомов."),
N("cx_reload",4,"Continuous atom reloading (reservoir + optical conveyor belt)","Непрерывная дозагрузка атомов (резервуар + оптический конвейер)",0.0,["nat"],-1.1,"na",None,"transport","opt",["RT"],["loss"],"optics","D",
  "A continuously fed atom reservoir (optical-lattice conveyor belts, a cavity-enhanced lattice or a molasses-stopped beam) from which tweezers extract new atoms into the array while the stored qubits keep their coherence; it replaces atom loss and turns a one-lifetime run into continuous operation.","Непрерывно пополняемый резервуар атомов (конвейеры на оптической решётке, решётка, усиленная резонатором, или остановленный молассой пучок), из которого пинцеты извлекают новые атомы в массив, пока хранимые кубиты сохраняют когерентность; замещает потерю атомов и превращает прогон длиной в одно время жизни ловушки в непрерывную работу.",
  [("clock","reload flux","≈ 300,000 atoms/s into tweezers; > 30,000 initialised qubits/s (15,000/s sorted into defect-free batches)","2025-09","https://www.nature.com/articles/s41586-025-09596-6"),
   ("count","continuous run","> 2 h, > 5 × 10⁷ atoms cycled through a 3,000-qubit array","2025-09","https://www.nature.com/articles/s41586-025-09596-6")],
  "Reload flux and coherence during reload are the figures of merit; a ~10,000-qubit processor at 1 ms per gate layer needs about 15,000 rearranged qubits per second (Chiu et al., a sufficiency estimate).","Показатели — поток дозагрузки и когерентность во время дозагрузки; процессору на ~10 000 кубитов при 1 ms на слой вентилей нужно около 15 000 переставленных кубитов в секунду (Chiu et al., оценка достаточности)."),
N("cx_shuttle",4,"Spin shuttling (conveyor mode)","Перемещение спинов (конвейерный режим)",1.0,["fab"],-6.7,"na",None,"transport","none",["none"],["coherent"],"cmos","E",
  "Spins carried 10 µm in < 200 ns at 99.5%; gates between moving spins 98.86%; gives fabricated carriers transport connectivity.","Спины переносятся на 10 µm за < 200 ns при 99.5%; вентили между движущимися спинами 98.86%; даёт искусственным носителям транспортную связность.",
  [("path","conveyor shuttling","10 µm, 99.54%, up to 64 m/s","2025-06","https://www.nature.com/articles/s41565-025-01920-5"),
   ("path","weight-4 parity via shuttled ancilla","97.7% per shuttle","2026-07","https://www.nature.com/articles/s41586-026-10766-3")],"",""),
N("cx_switch",4,"Photonic switching / routing (electro-optic, feed-forward)","Фотонная коммутация / маршрутизация (электрооптика, прямая связь)",0.25,["pho"],-6.0,"na",None,"flying","eo",["RT"],["loss"],"pic","D",
  "Every switch costs loss: 0.19 dB/MZI at system scale (Aurora), 100 mdB for the best in-line element (PsiQuantum BTO); FT needs ~7 mdB.","Каждый переключатель стоит потерь: 0.19 dB/MZI в масштабе системы (Aurora), 100 mdB у лучшего элемента в линии (BTO у PsiQuantum); для отказоустойчивости нужно ~7 mdB.",
  [("channel","best in-line switch (PsiQuantum BTO)","100 mdB insertion; 52(12) mdB fibre-to-chip","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","system-scale switch loss (Aurora)","0.19 dB/MZI; requirement ≈ 7 mdB","2025-01","https://www.nature.com/articles/s41586-024-08406-9"),
   ("channel","BTO phase shifter","0.33 dB·V","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "A '30 mdB' switch figure sometimes quoted is untraceable to any source. Omega's single-mode SiN loss is 1.8(2) dB/m against the 0.5 dB/m multimode figure — unreconciled.","Иногда цитируемые «30 mdB» для переключателя не прослеживаются ни к одному источнику. Потери одномодового SiN в Omega — 1.8(2) дБ/м против многомодовых 0.5 dB/m; расхождение не устранено."),
N("cx_crossbar",4,"Crossbar shared-line control (spins)","Кроссбар с общими линиями (спины)",1.0,["fab"],None,"na",None,"shared","lf",["RT"],["coherent"],"cmos","E",
  "Shared plunger/barrier lines: 23 lines for 16 dots, T = 6√g − 1 scaling; no coherent qubit operation shown.","Общие линии плунжерных и барьерных затворов: 23 линии на 16 точек, масштабирование T = 6√g − 1; когерентных операций с кубитами не показано.",
  [("path","control lines vs dots (no coherent qubit operation)","23 lines for 16 dots","2024-01","https://www.nature.com/articles/s41565-023-01491-3")],
  "The 2024 crossbar (16 dots, 23 lines; founding paper online 2023-08-28) showed no coherent qubit operation. The 'one of four pairs gated' result belongs to imec/Diraq's individually wired 8-qubit 300 mm device (Nat. Commun. 17, 5878, 2026-07), not to a crossbar.","Кроссбар 2024 года (16 точек, 23 линии; основополагающая статья онлайн 2023-08-28) не показал когерентных операций с кубитами. Результат «сработала одна пара из четырёх» относится к индивидуально разведённому 8-кубитному 300 mm устройству imec/Diraq (Nat. Commun. 17, 5878, 2026-07), а не к кроссбару."),
]
# ---------------------------------------------------------------- L5 CONTROL
NODES += [
N("ct_rt",5,"Room-temperature electronics + per-qubit coax/flex","Электроника при комнатной температуре + коаксиальный / гибкий кабель на кубит",1.0,["fab"],None,"na",None,"none","mw",["RT"],["coherent"],"sclitho","D",
  "One rf line per qubit through the fridge; the I/O wall: > 4,000 rf lines (KIDE), 1,121 qubits (Condor).","Одна РЧ-линия на кубит через криостат; стена ввод-вывод: > 4 000 РЧ-линий (KIDE), 1 121 кубит (Condor).",
  [("path","I/O wall","> 4,000 high-density rf lines per fridge","2026","https://bluefors.com/"),
   ("count","largest single-fridge chip","1,121 qubits (Condor)","2023-12","https://www.ibm.com/quantum/blog/quantum-roadmap-2033")],"",""),
N("ct_vio",5,"Vertical (out-of-plane) signal delivery — VIO, coaxmon, 3D wiring","Вертикальный (внеплоскостной) подвод сигналов — VIO, коаксмон, 3D разводка",1.0,["fab"],None,"na",None,"none","mw",["RT"],["coherent"],"sclitho","D",
  "Room-temperature electronics reach every qubit through wiring that leaves the chip plane — coaxial pins, through-substrate vias, a signal-routing interposer — instead of in-plane lines; it is what lets a lattice grow beyond the edge-routed few hundred qubits.","Электроника комнатной температуры достигает каждого кубита через разводку, выходящую из плоскости кристалла — коаксиальные штыри, сквозные переходные отверстия, интерпозер маршрутизации сигналов — вместо линий в плоскости; именно это позволяет решётке расти за пределы нескольких сотен кубитов с краевой разводкой.",
  (),"Lines per qubit stay ~1–2; the price is a packaging process and the crosstalk of dense vertical pins.","Линий на кубит по-прежнему ~1–2; цена — процесс корпусирования и перекрёстные помехи плотных вертикальных штырей."),
N("ct_cryocmos",5,"Cryo-CMOS controller (4 K / mK)","Крио-КМОП-контроллер (4 K / mK)",1.0,["fab"],None,"na",None,"none","mw",["4K","mK"],["coherent"],"cmos","D",
  "CMOS ASICs at 4 K (or 7 mK) generating pulses next to the qubits; 2–23 mW/qubit at 4 K; 20 nW/MHz per cell at mK.","Заказные КМОП-схемы (ASIC) при 4 K (или 7 mK), формирующие импульсы рядом с кубитами; 2–23 mW/кубит при 4 K; 20 nW/MHz на ячейку при mK.",
  [("path","HRL 4 K controller sequencing QEC","≤ 3.5 W, 366 DACs; d=5 *bit-flip-only* repetition code Λ=4.7 without room-temperature real-time electronics (arXiv Apr–May 2026, Nature Jul 2026)","2026-07","https://arxiv.org/abs/2604.16216"),
   ("path","IBM 14 nm at 4 K","23 mW/qubit; 1Q 8×10⁻⁴","2024-02","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326"),
   ("path","mK CMOS next to spin qubits","~20 nW/MHz per cell; fidelity impact 0.07%","2025-06","https://www.nature.com/articles/s41586-025-09157-x")],"",""),
N("ct_sfq",5,"SFQ digital control (4 K / mK)","Цифровое управление на БОК-логике (4 K / mK)",1.0,["fab"],None,"na",None,"none","mw",["mK","4K"],["pauli"],"sclitho","E",
  "Single-flux-quantum (superconducting-electronics) digital circuits either at the mK stage — pulse trains drive qubits from a flip-chip (1Q > 99 %, 99.9 % peak; nW/qubit claimed) — or at the 4 K stage as an in-fridge controller (DigiQ, 2022: the largest designs fit the few-watt budget of the 4 K stage); the same circuit family loads D-Wave's on-chip flux DACs.","Одноквантовые (сверхпроводниковая электроника) цифровые схемы либо на mK-ступени — цепочки импульсов управляют кубитами с flip-chip (однокубитные > 99 %, пик 99,9 %; заявлено нВт/кубит), — либо на ступени 4 K как контроллер внутри криостата (DigiQ, 2022: крупнейшие проекты укладываются в бюджет в несколько ватт ступени 4 K); та же схемотехника загружает потоковые ЦАП на чипе у D-Wave.",
  [("path","SEEQC mK SFQ control","1Q > 99%, up to 99.9% (Nature Electronics)","2026-03","https://www.nature.com/articles/s41928-026-01576-6"),
   ("path","DigiQ: A Scalable Digital Controller for Quantum Computers Using SFQ Logic, HPCA 2022","4 K in-fridge SFQ controller; the largest designs fit the few-watt budget of the 4 K stage","2022-02","https://arxiv.org/abs/2202.01407"),
   ("path","QP-poisoning-limited SFQ MCM","1.2% error/Clifford, 0.96% from photon-mediated QP","2023-07","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310")],
  "SEEQC–IBM integration under DARPA QBI (since Jun 2025).","Интеграция SEEQC–IBM в рамках DARPA QBI (с июня 2025)."),
N("ct_fluxdac",5,"On-chip flux-DAC multiplexing","Мультиплексирование потоковых ЦАП на чипе",1.0,["fab"],None,"na",None,"none","lf",["mK"],["coherent"],"sclitho","D",
  "Annealer-heritage SFQ flux DACs: ~200–300 bias lines for 10⁴ qubits; applied to fluxonium (bump-bonded MCM).","Потоковые ЦАП на БОК-логике из наследия отжигателей: ~200–300 линий смещения на 10⁴ кубитов; применено к флаксониуму (многокристальный модуль на столбиковых выводах).",
  [("path","bias lines per qubits","~300 bias lines into the QPU, of which ~200 multiplexed lines address ~10⁵ on-chip DACs (whitepaper 2026-01-23); fluxonium MCM at 10 mK","2026-01","https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf")],
  "The 200 and 300 in D-Wave's texts count different line sets: ~300 bias lines in total, ~200 multiplexed lines addressing the DAC network (both in the 2026-01-23 whitepaper). NASA JPL fabricated key components of the module.","200 и 300 в текстах D-Wave считают разные наборы линий: ~300 линий смещения всего, ~200 мультиплексированных линий адресуют сеть ЦАП (обе цифры в белой книге 2026-01-23). Ключевые компоненты модуля изготовлены в NASA JPL."),
N("ct_laser",5,"Laser + AOD/SLM optical control (atoms)","Оптическое управление лазером через АОД/SLM (атомы)",0.0,["nat"],None,"na",None,"none","opt",["RT"],["coherent"],"optics","D",
  "SLM-generated tweezer arrays (12,000 sites), AOD moves, Rydberg lasers; 33 W for 18,225 tweezers; the binding constraint above 10⁴ sites is the AOD time–bandwidth product, not an SLM refresh rate.","Массивы пинцетов от SLM (12 000 сайтов), перемещения на АОД, ридберговские лазеры; 33 W на 18 225 пинцетов; выше 10⁴ сайтов ограничивает произведение время–полоса у АОД, а не частота обновления SLM.",
  [("count","SLM array","~12,000 sites, 6,100 atoms","2025-09","https://arxiv.org/abs/2403.12021"),
   ("path","metasurface tweezers","18,225 traps from 33 W","2026-06","https://arxiv.org/abs/2606.02715")],
  "The '~10 MHz SLM refresh' sometimes quoted is unsourced: LCOS panels frame at tens of hertz, and deflector reconfiguration is bounded by acoustic transit. The only end-to-end vendor loop figure is QuEra Gemini: one shot per second at 260 qubits.","Иногда цитируемое «обновление SLM ~10 MHz» не подкреплено источником: панели LCOS обновляются с частотой десятков герц, а перестройка дефлектора ограничена акустическим пробегом. Единственная сквозная вендорская цифра — QuEra Gemini: один выстрел в секунду на 260 кубитах."),
N("ct_pic_trap",5,"PIC-generated tweezers / integrated optics for atoms","Пинцеты от ФИС / интегральная оптика для атомов",0.25,["nat"],None,"na",None,"none","opt",["RT"],["coherent"],"pic","E",
  "Trap generation moved onto a photonic chip (4 atoms, 27.5 s lifetimes); fabricated-world optics for a natural carrier.","Генерация ловушек перенесена на фотонный чип (4 атома, время жизни 27.5 s); оптика искусственного мира для естественного носителя.",
  [("path","on-chip traps","4 Rb atoms, 27.5 s lifetime","2026-08","https://www.pasqal.com/newsroom/pasqal-brings-qubit-control-on-chip/")],
  "Pasqal. Two functions hide here and only the first is trap generation: UChicago's 2024 tweezers are free-space traps over nanophotonic cavities, and USTC's 2026 glass-waveguide chip addresses trapped atoms rather than generating the traps.","Pasqal. Здесь скрыты две функции, и только первая — генерация ловушек: пинцеты UChicago 2024 года — ловушки в свободном пространстве над нанофотонными резонаторами, а стеклянно-волноводный чип USTC 2026 года адресует уже атомы в ловушках, а не создаёт ловушки."),
N("ct_ionlaser",5,"Laser control with integrated photonics (ions)","Лазерное управление с интегральной фотоникой (ионы)",0.0,["nat"],None,"na",None,"none","opt",["RT"],["coherent"],"pic","D",
  "In-vacuum integrated photonics at room temperature (cryogenic traps at 4–10 K exist): Waveguides in the trap deliver all wavelengths; > 99.3% 2Q (ETH). Helios (≥ 7 wavelengths, 8 zones) still delivers its light as focused free-space beams — integrated delivery is a stated direction, not yet in a product.","Интегральная фотоника в вакууме при комнатной температуре (существуют криогенные ловушки при 4–10 K): Волноводы в ловушке доставляют все длины волн; двухкубитный вентиль > 99.3% (ETH). Helios (≥ 7 длин волн, 8 зон) по-прежнему доставляет свет сфокусированными пучками в свободном пространстве — встроенная в ловушку доставка света заявлена как направление, в продукте её ещё нет.",
  [("path","waveguide-delivered 2Q gate","> 99.3%","2020-10","https://www.nature.com/articles/s41586-020-2823-6")],"",""),
N("ct_ionaod",5,"Free-space laser addressing of ions (AOM/AOD beams)","Свободнопространственная лазерная адресация ионов (пучки АОМ/АОД)",0.0,["nat"],None,"na",None,"none","opt",["RT"],["coherent"],"optics","D",
  "Individual and global gate beams steered onto a chain by acousto-optic modulators or deflectors through bulk optics above the trap — the most common ion control in the register ({{N_T_CT_IONAOD_MACHINES_W}} machines), and the one that does not scale past one chain without integrated delivery.","Индивидуальные и глобальные вентильные пучки, наводимые на цепочку акустооптическими модуляторами или дефлекторами через объёмную оптику над ловушкой — самое распространённое управление ионами в реестре ({{N_T_CT_IONAOD_MACHINES_W}} машин) и то, которое не масштабируется дальше одной цепочки без встроенной доставки света.",
  (),"Beam-pointing stability and crosstalk between neighbouring ions bound the fidelity; one optical assembly per chain.","Стабильность наведения и перекрёстные помехи между соседними ионами ограничивают точность; одна оптическая сборка на цепочку."),
N("ct_ionmw",5,"Chip-integrated microwave control (ions)","СВЧ-управление, интегрированное в чип (ионы)",1.0,["nat"],None,"na",None,"none","mw",["RT"],["pauli"],"mems","D",
  "Electronic signal sources replace gate lasers: ~200 sources for 1,000 ions (WISE); 1Q 1.5×10⁻⁷ without shielding.","Электронные источники сигнала заменяют лазеры вентилей: ~200 источников на 1 000 ионов (WISE); однокубитная ошибка 1.5×10⁻⁷ без экранирования.",
  [("channel","chip-integrated microwave 1Q","1.5×10⁻⁷ error per Clifford","2024-12","https://arxiv.org/abs/2412.04421"),
   ("path","WISE architecture","1,000 ions with ~200 signal sources (design)","2023","https://arxiv.org/abs/2305.12773")],"Oxford Ionics/IonQ, eleQtron (MAGIC).","Oxford Ionics/IonQ, eleQtron (MAGIC)."),
N("ct_base",5,"Baseband electrical control (spins, Majorana)","Электрическое управление в основной полосе частот (спины, майораны)",1.0,["fab"],None,"na",None,"none","lf",["RT"],["coherent"],"cmos","D",
  "Voltage pulses on gates; digital, dense; the calibration burden shows up as coherent error.","Импульсы напряжения на затворах; цифровое, плотное; бремя калибровки проявляется как когерентная ошибка.",
  [("channel","extrinsic control share of CNOT error","~80% (HRL)","2026-07","https://arxiv.org/abs/2604.16216")],
  "QuTech's baseband hopping-gate figure of 99.50(6)% is a lower bound, not a point estimate. HRL's Λ = 4.7 is a bit-flip-only repetition code, and its [[4,2,2]] fidelity of 0.95 is post-selected.","99.50(6)% для вентиля перескока (hopping) в основной полосе частот у QuTech — нижняя граница, а не точечная оценка. Λ = 4.7 у HRL — код с повторением только по перевороту бита, а его [[4,2,2]] с точностью 0.95 — с постселекцией."),
]
# ---------------------------------------------------------------- L6 READOUT
NODES += [
N("ro_disp",6,"Dispersive microwave readout (+TWPA, Purcell)","Дисперсионное СВЧ-считывание (+TWPA, фильтр Парселла)",1.0,["fab"],None,"na",C("disp",-6.55,False,True),"none","mw",["RT"],["leak"],"sclitho","D",
  "Resonator shift read through a parametric amplifier; 240 ns pulse at 99.94% (IQM); readout-induced leakage is the hidden cost.","Сдвиг резонатора, читаемый через параметрический усилитель; импульс 240 ns при 99.94% (IQM); скрытая цена — утечка, наведённая считыванием.",
  [("clock","readout pulse / fidelity (IQM)","240 ns pulse (≈280 ns full window) / 99.94% simultaneous assignment; QNDness 99.3%","2025-09","https://arxiv.org/abs/2508.16437"),
   ("channel","at-scale readout error","~1×10⁻² (fleet)","2025-08","https://www.ibm.com/quantum/hardware")],"",""),
N("ro_reset",6,"Fast unconditional / dissipative qubit reset","Быстрый безусловный / диссипативный сброс кубита",1.0,["fab"],None,"na",None,"none","mw",["RT"],["leak"],"sclitho","D",
  "Returning a qubit to |0⟩ in ~100–500 ns by coupling it to a lossy resonator or by a measurement-free dissipative drive — a per-cycle cost term of every surface-code budget that the readout node alone does not describe.","Возврат кубита в |0⟩ за ~100–500 ns связью с резонатором с потерями или диссипативным приводом без измерения — слагаемое стоимости каждого цикла поверхностного кода, которое узел считывания сам по себе не описывает.",
  (),"Reset time and residual excitation (~10⁻³) are the figures of merit; leakage removal is the companion problem.","Показатели — время сброса и остаточное возбуждение (~10⁻³); сопутствующая задача — удаление утечки."),
N("ro_fluxro",6,"Flux readout via QFP / SQUID shift registers (annealers)","Считывание потока через QFP / СКВИД и сдвиговые регистры (отжигатели)",1.0,["fab"],None,"na",C("flux",-4.0,True,False),"none","lf",["mK"],["pauli"],"sclitho","D",
  "The annealer's own readout: the final flux state of each qubit is latched by a quantum-flux-parametron and clocked out through on-chip shift registers to a handful of lines — thousands of qubits read per anneal; no qubit is coupled to a resonator (the shift registers end in frequency-multiplexed microresonators at the chip edge).","Собственное считывание отжигателя: конечное состояние потока каждого кубита защёлкивается квантовым потоковым параметроном и выводится сдвиговыми регистрами на чипе по нескольким линиям — тысячи кубитов за один отжиг; ни один кубит не связан с резонатором (сдвиговые регистры оканчиваются частотно-мультиплексированными микрорезонаторами на краю чипа).",
  (),"A read of the whole chip takes 17–235 µs and ends the sample; it is not a mid-circuit measurement.","Считывание всего чипа занимает 17–235 µs и завершает выборку; это не измерение внутри схемы."),
N("ro_fluor",6,"Fluorescence state detection (ions, defects)","Детектирование состояния по флуоресценции (ионы, дефекты)",0.0,["nat"],None,"na",C("fluor",-4.0,False,True),"none","opt",["RT"],["pauli"],"optics","D",
  "State-dependent scattering counted by PMT/SNSPD; 11 µs at 99.93% record; SPAM 4.8×10⁻⁴ on Helios.","Зависимое от состояния рассеяние, считаемое ФЭУ/SNSPD; рекорд 11 µs при 99.93%; SPAM 4.8×10⁻⁴ на Helios.",
  [("clock","fastest ion readout","11 µs at 99.931% (¹⁷¹Yb⁺, MoSi SNSPD)","2019","https://www.nature.com/articles/s42005-019-0195-8"),
   ("channel","Helios SPAM","4.8×10⁻⁴","2025-11","https://arxiv.org/abs/2511.05465")],
  "The Kyoto/Yaqumo 17.6 µs result (arXiv:2605.24175) is neutral ¹⁷⁴Yb *imaging* — spinless, not qubit-state-resolved — and is not an ion-readout record.","Результат Kyoto/Yaqumo 17.6 µs (arXiv:2605.24175) — *регистрация флуоресценции* нейтрального бесспинового ¹⁷⁴Yb, не разрешающая состояние кубита; это не рекорд считывания ионов."),
N("ro_img",6,"Fluorescence imaging of atom arrays","Регистрация флуоресценции массивов атомов",0.0,["nat"],None,"na",C("img",-3.3,False,True),"none","opt",["RT"],["loss"],"optics","D",
  "Camera imaging, 0.5–1 ms typical; non-destructive with 0.24% loss; fast neutral-Yb imaging emerging (17.6 µs, 99.89%).","Регистрация флуоресценции на камере, типично 0.5–1 ms; неразрушающая, с потерей 0.24%; формируется быстрая регистрация нейтрального Yb (17.6 µs, 99.89%).",
  [("clock","typical mid-circuit readout","~0.5–1 ms; 0.46% bit-flip, 0.24% loss","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("clock","fast imaging (emerging)","17.6 µs, 99.89% discrimination, 98.8% survival — neutral ¹⁷⁴Yb, spinless (not qubit-state-resolved)","2026-08","https://arxiv.org/html/2605.24175")],"",""),
N("ro_s2c",6,"Spin-to-charge conversion + rf reflectometry","Преобразование спина в заряд + радиочастотная рефлектометрия",1.0,["fab"],None,"na",C("s2c",-5.2,False,True),"none","lf",["RT"],["coherent"],"cmos","D",
  "Pauli/energy-selective tunnelling sensed by a gate-based single-electron box (SEB) or an SET; 99.2% in < 6 µs; 99.9% at 100 µs.","Туннелирование по Паули/энергии, регистрируемое одноэлектронным боксом на затворе (SEB) или одноэлектронным транзистором (SET); 99.2% за < 6 µs; 99.9% за 100 µs.",
  [("clock","fast readout (Oakes et al., Quantum Motion; rf single-electron box)","99.2% in < 6 µs","2023-02","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.011023"),
   ("channel","best SPAM","99.9% (100 µs integration)","2025-09","https://www.nature.com/articles/s41586-025-09531-9")],
  "The 99.2% in < 6 µs is Oakes et al., PRX 13, 011023 (2023), Quantum Motion — an rf single-electron box, not an SET.","99.2% за < 6 µs — Oakes et al., PRX 13, 011023 (2023), Quantum Motion: радиочастотный одноэлектронный бокс, а не SET."),
N("ro_spd",6,"Single-photon detection (SNSPD / TES)","Детектирование одиночных фотонов (SNSPD / TES)",0.25,["pho"],None,"na",C("spd",-8.0,True,False),"none","eo",["4K"],["loss"],"pic","D",
  "Destructive by nature; 93.4% wafer-scale median to 99.73% on a hero device, 3 ps jitter, 1–4 K; thousands of channels needed.","Разрушающее по природе; от 93.4% медианы в масштабе пластины до 99.73% на рекордном устройстве, джиттер 3 пс, 1–4 K; нужны тысячи каналов.",
  [("channel","wafer-scale median on-chip efficiency (PsiQuantum Omega, 300 mm)","93.4% at ~2 K","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","best on-chip efficiency (laboratory device)","99.73%","2025-10","https://www.nature.com/articles/s41377-025-02031-5")],
  "The '98.9% median (PsiQuantum)' sometimes quoted is superseded: the Omega paper gives 93.4% median on-chip efficiency — 0.30 dB per detection rather than 0.05 dB.","Иногда цитируемая «98.9% медиана (PsiQuantum)» вытеснена: статья по Omega даёт 93.4% медианной эффективности на чипе — 0.30 dB на детектирование вместо 0.05 dB."),
N("ro_homodyne",6,"Homodyne quadrature detection (CV)","Гомодинное детектирование квадратур (непрерывные переменные)",0.25,["pho"],None,"na",C("homodyne",-6.0,True,True),"none","eo",["RT"],["gauss"],"pic","D",
  "Measurement of a field quadrature against a shared local oscillator — the computational measurement of continuous-variable and GKP machines (Aurora); photon counting remains the heralding path, and the samplers (Borealis, Jiuzhang) count photons.","Измерение квадратуры поля относительно общего гетеродина — вычислительное измерение машин на непрерывных переменных и GKP (Aurora); счёт фотонов остаётся каналом оповещения, а сэмплеры (Borealis, Jiuzhang) считают фотоны.",
  (),"Detector efficiency and electronic noise set the effective squeezing; at the 1 MHz clock the detection is not the bottleneck.","Эффективность детектора и электронный шум определяют эффективное сжатие; при такте 1 MHz детектирование не является узким местом."),
N("ro_qcap",6,"rf quantum-capacitance parity readout","Радиочастотное считывание чётности по квантовой ёмкости",1.0,["fab"],None,"na",C("qcap",-4.0,False,True),"none","lf",["RT"],["unknown"],"mbe","E",
  "Interferometric parity readout of a Majorana wire; 1% assignment error, SNR 1 in 3.6 µs.","Интерферометрическое считывание чётности майорановской проволоки; 1% ошибка присвоения, SNR 1 за 3.6 µs.",
  [("clock","readout","1% error; SNR 1 in 3.6 µs","2025-02","https://www.nature.com/articles/s41586-024-08445-2"),
   ("clock","independent replication (QuTech, InSb Kitaev chain)","~1.85 ms dwell, SNR ~1.93","2026-02","https://www.nature.com/articles/s41586-025-09927-7")],
  "The independent replication is van Loo et al., Nature 650 (2026-02-11), on an InSb minimal Kitaev chain; arXiv:2607.09511 is the follow-on coherent parity qubit, a different result.","Независимая репликация — van Loo et al., Nature 650 (2026-02-11), на минимальной цепочке Китаева в InSb; arXiv:2607.09511 — последующий когерентный кубит чётности, другой результат."),
N("ro_erasure",6,"Mid-circuit erasure check","Внутрисхемная проверка стирания",0.5,["fab","nat","pho"],None,"na",C("erasure",-6.4,False,True),"none","mw",["RT"],["erasure"],"none","D",
  "Ancilla-based detection of leakage/loss without disturbing the code: 384 ns (transmon), 1.8 µs (cavity), 20 µs (Yb atoms).","Детекция утечки/потери через анциллу без возмущения кода: 384 ns (трансмон), 1.8 µs (резонатор), 20 µs (атомы Yb).",
  [("clock","transmon dual-rail check","384 ns; FP/FN ≈ separation error 0.8% (SNR 11.6)","2026-04","https://arxiv.org/abs/2604.16292"),
   ("clock","cavity dual-rail check","1.8 µs, FP 0.51% / FN 3.7%","2025-01","https://www.nature.com/articles/s41534-024-00944-4"),
   ("clock","Yb erasure detection","20 µs (1Q) / 420 µs (2Q)","2023-05","https://arxiv.org/abs/2305.05493")],"",""),
]
# ---------------------------------------------------------------- L7 CODE
NODES += [
N("code_surface",7,"Rotated surface code (+ yoked variants)","Повёрнутый поверхностный код (+ yoked-варианты)",0.5,["fab","nat"],None,"na",None,"static","none",["none"],["pauli"],"none","D",
  "2D nearest-neighbour code; threshold 0.94%; ~650–1,500 physical per logical at 10⁻¹² (yokes cut ~1,500 to 600–800).","2D-код ближайших соседей; порог 0.94%; ~650–1 500 физических на логический при 10⁻¹² (yoked-варианты снижают ~1 500 до 600–800).",
  [("channel","Λ (Willow, d=3→7)","2.14 ± 0.02; d=7 record 7.72×10⁻⁴/cycle (Jul 2026)","2026-07","https://www.nature.com/articles/s41586-026-10759-2"),
   ("channel","Λ (USTC 107 q, d=7)","1.40(6)","2025-12","https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31"),
   ("channel","neutral-atom d=3→5","2.14(13)× in 4-round circuit","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("count","teraquop footprint, plain patches (p=10⁻³)","~1,500 physical/logical (800 with 1D yokes, 600 with 2D yokes)","2023-12","https://arxiv.org/abs/2312.04522"),
   ("count","teraquop footprint with correlated matching (p=10⁻³)","~650 physical/logical","2023-12","https://arxiv.org/abs/2312.08813")],"",""),
N("code_color",7,"Colour code (transversal Cliffords)","Цветовой код (трансверсальные клиффордовы вентили)",0.5,["fab","nat"],None,"na",None,"static","none",["none"],["pauli"],"none","D",
  "Triangular 2D code with transversal H/S/CNOT; ~1.9× the surface-code footprint; hosts distillation and injection.","Треугольный 2D-код с трансверсальными H/S/CNOT; ~1.9× площади поверхностного кода; несёт дистилляцию и инъекцию.",
  [("channel","Λ₃/₅ (Google)","1.56(4); logical Clifford 0.0027","2025-05","https://www.nature.com/articles/s41586-025-09061-4"),
   ("channel","5-to-1 distillation on logical qubits","d=3: 95.1%→99.4%; d=5: 92.5%→98.6%","2025-07","https://www.nature.com/articles/s41586-025-09367-3")],"",""),
N("code_qldpc",7,"Non-local qLDPC codes (bivariate bicycle, 'gross')","Нелокальные qLDPC-коды (bivariate bicycle, «gross»)",0.5,["fab","nat"],None,"na",None,"longrange","none",["none"],["pauli"],"none","E",
  "The surface code is itself a qLDPC code with 2D-local checks and vanishing rate; this node is the non-local, constant-rate family. 'Gross' = IBM's [[144,12,12]] bivariate bicycle code (144 = a gross, 12 dozen; 'two-gross' = [[288,12,18]]): 12 logical in 288 qubits incl. checks, threshold 0.8%, needs degree-6 connectivity. Hardware: IonQ's eight codes on one 40-ion chain reach break-even within error bars in one code the paper does not identify — not in [[18,4,3]], 4 logical in 18 ions; Zhejiang's [[18,4,4]] stays short of break-even.","Поверхностный код сам является qLDPC-кодом с 2D-локальными проверками и исчезающей скоростью; этот узел — нелокальное семейство с постоянной скоростью. «Gross» = код IBM [[144,12,12]] (144 = гросс, 12 дюжин; «two-gross» = [[288,12,18]]): 12 логических в 288 кубитах с проверками, порог 0.8%, нужна связность степени 6. На железе: восемь кодов IonQ на одной цепочке из 40 ионов достигают безубыточности в пределах погрешности в одном коде, который статья не называет, — не в [[18,4,3]] с 4 логическими в 18 ионах; Zhejiang [[18,4,4]] до безубыточности не дотягивает.",
  [("count","gross code overhead","288 physical for 12 logical (~24/logical) vs ~3,000 surface","2024-03","https://arxiv.org/abs/2308.07915"),
   ("channel","IonQ memories on a 40-ion ¹³³Ba chain: eight codes, BB [[18,4,3]] (4 logical in 18 ions) to [[30,4,5]]","3.95 ± 0.68 s in one code the paper does not identify vs 3.84 ± 0.48 s physical (= 3 T2*; the June version gave 3.3 ± 0.9 s); BB [[18,4,3]] 2.48 ± 0.40 s; logical runs leakage-post-selected — break-even within error bars (arXiv version of 14 Sep 2026)","2026-09","https://arxiv.org/abs/2606.06455"),
   ("channel","Zhejiang [[18,4,4]] on 32 SC qubits","8.91%/logical/cycle (not break-even)","2025-05","https://arxiv.org/html/2505.09684"),
   ("count","RSA-2048 with qLDPC (Pinnacle)","< 100,000 physical qubits at 10⁻³, 1 µs cycle","2026-02","https://arxiv.org/abs/2602.11457")],
  "IBM Kookaburra (2026, not yet delivered). The IonQ abstract states '4 logical into 18 physical' without code notation; Table II of the arXiv version of 14 Sep 2026 names it BB[[18,4,3]], at 2.48 ± 0.40 s below the physical 3.84 ± 0.48 s.","IBM Kookaburra (2026, ещё не поставлен). В аннотации IonQ сказано «4 логических в 18 физических» без нотации кода; таблица II версии arXiv от 14 сентября 2026 называет его BB[[18,4,3]] — 2.48 ± 0.40 s, ниже физических 3.84 ± 0.48 s."),
N("code_highrate",7,"High-rate concatenated codes with transversal gates","Высокоскоростные каскадные коды с трансверсальными вентилями",0.0,["nat"],None,"na",None,"transport","none",["none"],["pauli"],"none","D",
  "Iceberg [[k+2,k,2]], [[80,48,4]], tesseract colour code [[16,6,4]] (subsystem variant [[16,4,2,4]] at Quantinuum): many logical qubits per physical block; needs all-to-all.","Iceberg [[k+2,k,2]], [[80,48,4]], тессерактный цветовой код [[16,6,4]] (подсистемный вариант [[16,4,2,4]] у Quantinuum): много логических кубитов на физический блок; нужна связность «все со всеми».",
  [("count","Helios [[80,48,4]]","48 corrected logical qubits; logical gate error 1.0–1.2×10⁻⁴","2026-02","https://arxiv.org/abs/2602.22211"),
   ("count","Harvard tesseract [[16,6,4]]","up to 96 d=4 logical qubits active","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("count","Quantinuum tesseract [[16,6,4]] on ions","transversal logical Clifford group in depth-one circuits, 12 addressable logical CZ pairs","2026-06","https://www.nature.com/articles/s41586-026-10628-y")],
  "The tesseract is [[16,6,4]], a doubly-even self-dual 4D CSS code; the [[16,4,4]] sometimes quoted is wrong. Quantinuum uses its subsystem variant [[16,4,2,4]].","Тессеракт — [[16,6,4]], дважды-чётный самодуальный 4D CSS-код; иногда встречающееся [[16,4,4]] неверно. Quantinuum использует его подсистемный вариант [[16,4,2,4]]."),
N("code_erasure",7,"Erasure-adapted codes","Коды, адаптированные к стираниям",0.5,["fab","nat","pho"],None,"na",None,"static","none",["none"],["erasure"],"none","E",
  "Surface/loss-tolerant codes fed with erasure flags: threshold 0.94% → 4.15%; dual-rail simulation Λ≈27 (idealised).","Поверхностные коды и коды, устойчивые к потерям, с флагами стирания: порог 0.94% → 4.15%; симуляция двухрельсовых кубитов Λ≈27 (идеализировано).",
  [("channel","threshold with 98% erasure","4.15% vs 0.937%","2022-01","https://arxiv.org/abs/2201.03540"),
   ("channel","[[4,2,2]] erasure teleportation (atoms)","logical decay 1.9(4)× slower with erasure info in unconditional decoding","2026-06","https://arxiv.org/abs/2506.13724")],
  "Use 1.9(4)× architecturally: it is the unconditional decoding gain. The 3.6(1)× often quoted is the post-selected hold.","Архитектурно использовать 1.9(4)×: это выигрыш безусловного декодирования. часто цитируемое 3.6(1)× — постселектированное удержание."),
N("code_bosonic",7,"Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC)","Бозонное каскадирование (repetition-cat, LDPC-cat, GKP+qLDPC)",0.75,["fab","pho"],None,"na",None,"static","none",["none"],["bias","gauss"],"none","E",
  "Outer code exploits inner bias/shift correction; Ocelot's two points are not a distance scan; LDPC-cat assumes 0.1% phase-flip (measured ~10%).","Внешний код использует смещение шума/коррекцию сдвигов внутреннего; две точки Ocelot — не скан по расстоянию; LDPC-cat предполагает 0.1% переворотов фазы (измерено ~10%).",
  [("channel","repetition-cat (Ocelot)","d=3 1.75% at |α|²=1 → d=5 1.65% at |α|²=1.5 per 2.8 µs cycle — different n̄, not a distance scan","2025-02","https://www.nature.com/articles/s41586-025-08642-7"),
   ("count","LDPC-cat estimate","758 cats → 100 logical at 10⁻⁸ (assumes 0.1% phase-flip)","2024-01","https://arxiv.org/abs/2401.09541"),
   ("count","repetition-cat estimate (Gouzien et al.)","126,133 cats for a 256-bit elliptic-curve logarithm in 9 h","2023-02","https://arxiv.org/abs/2302.06639")],
  "Ocelot's 'd=3→5 nearly flat' is not a distance scan: the two points sit at different mean photon numbers. Gouzien et al. size ECC-256, not RSA-2048.","«Почти плоско от d=3 к d=5» у Ocelot — не скан по расстоянию: точки взяты при разных средних числах фотонов. Gouzien et al. оценивают ECC-256, а не RSA-2048."),
N("code_fusion",7,"Fusion-based fault tolerance","Отказоустойчивость на основе слияний",0.25,["pho"],None,"na",None,"flying","none",["none"],["loss"],"none","T",
  "Resource states + fusions; loss threshold 2.7%/photon (boosted 6-ring), 17.4% only for a {7,4}-encoded resource state of ~168 photons; no demonstration.","Ресурсные состояния + слияния; порог потерь 2.7%/фотон (усиленный 6-ring), 17.4% — только для {7,4}-кодированного ресурсного состояния из ~168 фотонов; демонстраций нет.",
  [("channel","loss threshold","2.7% per photon (boosted 6-ring); 17.4% ({7,4}-encoded resource state)","2025-06","https://arxiv.org/abs/2506.11975")],
  "FBQC framework = Bartolucci et al., Nat. Commun. 14, 912 (2023-02). The 2.7% (boosted 6-ring) and Sparrow's 0.38–0.82% (unencoded 6-ring, arXiv:2606.28490, 2026) assume different boosting, bias models and decoders and remain unreconciled.","Каркас FBQC — Bartolucci et al., Nat. Commun. 14, 912 (2023-02). 2.7% (усиленный 6-ring) и 0.38–0.82% у Sparrow (некодированный 6-ring, arXiv:2606.28490, 2026) исходят из разных допущений об усилении, модели смещения шума и декодере и не сведены."),
N("code_aft",7,"Algorithmic FT / transversal architectures","Алгоритмическая отказоустойчивость / трансверсальные архитектуры",0.0,["nat"],None,"na",None,"transport","none",["none"],["pauli"],"none","E",
  "Constant syndrome rounds per logical gate via transversal gates + correlated decoding; amortises slow cycles (> 10× spacetime).","Постоянное число синдромных раундов на логический вентиль через трансверсальные вентили + коррелированное декодирование; амортизирует медленные циклы (> 10× пространство-время).",
  [("clock","rounds per logical gate","O(d) → O(1)","2024-06","https://arxiv.org/abs/2406.17653"),
   ("count","Shor / P-256 on reconfigurable atoms","10,000 atoms minimum (26,000 time-efficient); P-256 in days, RSA-2048 one to two orders longer","2026-03","https://arxiv.org/abs/2603.28627"),
   ("count","RSA-2048 on reconfigurable atoms (ISCA 2025)","5.6 days on 19 M qubits at a 1 ms cycle","2025-05","https://arxiv.org/abs/2505.15907")],
  "'RSA-2048 with ~10⁴ atoms' is what neither paper says: arXiv:2603.28627 is Shor/P-256, and the RSA-2048 point on the same trade curve is 19 M qubits for 5.6 days (ISCA 2025). Transversal architectures are not atoms-only — Quantinuum ran the tesseract [[16,6,4]] on trapped ions (Nature 654, 2026-06).","«RSA-2048 на ~10⁴ атомах» не утверждает ни одна из статей: arXiv:2603.28627 — это Shor/P-256, а точка RSA-2048 на той же кривой компромисса — 19 млн кубитов за 5.6 суток (ISCA 2025). Трансверсальные архитектуры не привязаны к атомам — Quantinuum выполнила тессерактный [[16,6,4]] на ионах (Nature 654, 2026-06)."),
N("code_magic",7,"Magic-state factory (cultivation / distillation / code switching)","Фабрика магических состояний (культивация / дистилляция / переключение кодов)",0.5,["fab","nat"],None,"na",None,"static","none",["none"],["pauli"],"none","D",
  "Non-Clifford resource; cultivation reaches 10⁻⁹ T-error at ~cost of a CNOT (theory), 0.9999 shown at 8% acceptance.","Ресурс для не-клиффордовых вентилей; культивация даёт 10⁻⁹ T-ошибки за ~цену CNOT (теория), показано 0.9999 при 8% принятых.",
  [("channel","cultivation (Google)","0.9999(1), 8% acceptance, 40× error reduction","2025-12","https://arxiv.org/abs/2512.13908"),
   ("channel","code switching (Quantinuum)","≤ 5.1×10⁻⁴ at 82.6% acceptance","2025-06","https://arxiv.org/abs/2506.14169")],"",""),
]
# ---------------------------------------------------------------- L8 DECODER
NODES += [
N("code_mitig",7,"Error mitigation in the code slot (ZNE, PEC) — not a code","Смягчение ошибок в слоте кода (ZNE, PEC) — не код",0.5,["fab","nat","pho"],None,"na",None,"static","none",["none"],["pauli"],"none","D",
  "Zero-noise extrapolation, probabilistic error cancellation and tensor-network post-processing: what actually occupies the code slot of a utility-scale NISQ machine. They reduce the bias of an expectation value at exponential sampling cost and correct nothing — the honest name for a stack without a code.","Экстраполяция к нулевому шуму, вероятностное подавление ошибок и постобработка тензорными сетями: то, что на деле занимает слот кода у NISQ-машины «утилитарного» масштаба. Они уменьшают смещение среднего при экспоненциальной цене выборки и ничего не исправляют — честное имя стека без кода.",
  (),"Sampling overhead grows exponentially with circuit volume; no logical qubit exists.","Накладные расходы на выборку растут экспоненциально с объёмом схемы; логического кубита нет."),
N("code_detect",7,"Error-detection codes ([[4,2,2]], d=2 surface, iceberg, spacetime)","Коды обнаружения ошибок ([[4,2,2]], поверхностный d = 2, iceberg, пространственно-временные)",0.5,["fab","nat","pho"],None,"na",None,"static","none",["none"],["pauli"],"none","D",
  "Codes that flag an error and discard the run instead of correcting it — the [[4,2,2]] code, the distance-2 surface code, spacetime codes: the first rung of the QEC ladder, run on five register machines, with acceptance fraction as the cost.","Коды, которые помечают ошибку и отбрасывают прогон вместо исправления — код [[4,2,2]], поверхностный код расстояния 2, пространственно-временные коды: первая ступень лестницы QEC, запущенная на пяти машинах реестра; цена — доля принятых прогонов.",
  (),"Post-selection cost grows with circuit size; no suppression with distance.","Цена постселекции растёт с размером схемы; подавления с ростом расстояния нет."),
N("dec_mwpm",8,"MWPM / Sparse Blossom (+ correlated matching)","MWPM / Sparse Blossom (+коррелированное паросочетание)",0.5,["fab","nat"],None,"na",None,"none","none",["none"],["pauli"],"none","D",
  "Matching decoder; < 1 µs/round at d=17 on one core (throughput), 0.8 µs FPGA latency at d=13 (Micro Blossom); Λ=2.04 on Willow vs 2.14 neural.","Декодер на основе паросочетаний; < 1 µs/раунд при d=17 на одном ядре (пропускная способность), 0.8 µs задержки на ПЛИС при d=13 (Micro Blossom); Λ=2.04 на Willow против 2.14 у нейросетевого.",
  [("clock","PyMatching v2 throughput","< 1 µs/round at d=17, p=0.1%","2023-03","https://arxiv.org/abs/2303.15933"),
   ("clock","Micro Blossom FPGA (ASPLOS 2025)","0.8 µs average latency at d=13, p=0.1%","2025-02","https://arxiv.org/abs/2502.14787")],
  "Micro Blossom's published figure is 0.8 µs at d=13 (ASPLOS 2025, arXiv:2502.14787); the repository's 367 ns appears in no paper. Willow's real-time decoder is a parallelised Sparse Blossom variant built by Google, not stock PyMatching.","Опубликованный результат Micro Blossom — 0.8 µs при d=13 (ASPLOS 2025, arXiv:2502.14787); 367 ns из репозитория не встречаются ни в одной статье. Декодер реального времени Willow — параллелизованный вариант Sparse Blossom, сделанный Google, а не стандартный PyMatching."),
N("dec_nn",8,"Neural decoders (AlphaQubit 2, CNN, transformers)","Нейросетевые декодеры (AlphaQubit 2, CNN, трансформеры)",0.5,["fab","nat"],None,"na",None,"none","none",["none"],["pauli"],"none","D",
  "Learned decoders make ~6% fewer errors than a tensor-network decoder and ~30% fewer than correlated matching on Sycamore data, and 20–29% fewer than matching in simulation to d=11; FPGA NN decode 124 ns at d=3; sub-µs throughput per cycle shown to d=11, on recorded or simulated data, not live.","Обучаемые декодеры делают на ~6% меньше ошибок, чем тензорно-сетевой декодер, и на ~30% меньше, чем коррелированное паросочетание, на данных Sycamore, а в моделировании до d=11 — на 20–29% меньше, чем паросочетание; нейросетевой декодер на ПЛИС — 124 ns при d=3; пропускная способность быстрее 1 µs на цикл показана до d=11, на записанных или смоделированных данных, не вживую.",
  [("channel","Willow d=7 with AlphaQubit 2","7.72×10⁻⁴/cycle","2026-07","https://www.nature.com/articles/s41586-026-10759-2"),
   ("clock","FPGA NN decoder","124 ns decode, 550 ns closed loop (d=3)","2026-05","https://arxiv.org/abs/2605.04892")],"",""),
N("dec_relaybp",8,"Relay-BP for qLDPC (FPGA)","Relay-BP для qLDPC (ПЛИС)",0.5,["fab","nat"],None,"na",None,"none","none",["none"],["pauli"],"none","D",
  "Belief propagation with relays: 24 ns/iteration, average < 1 µs per cycle, ~100× lower LER than BP+OSD.","Распространение доверия (belief propagation) с реле: 24 ns/итерация, в среднем < 1 µs на цикл, частота логических ошибок в ~100 раз ниже, чем у BP+OSD.",
  [("clock","FPGA Relay-BP","average < 1 µs per cycle at p < 3×10⁻³ (simulated syndromes)","2025-10","https://arxiv.org/abs/2510.21600")],
  "A '480 ns per 12-cycle window' figure sometimes quoted is ~25× off the paper's average of under 1 µs per cycle. Relay-BP originates with Müller et al., arXiv:2506.01779 (2025-06-02); arXiv:2510.21600 is the FPGA implementation.","Иногда цитируемые «480 ns на окно из 12 циклов» расходятся примерно в 25 раз со средним значением статьи — менее 1 µs на цикл. Relay-BP берёт начало от Müller et al., arXiv:2506.01779 (2025-06-02); arXiv:2510.21600 — это реализация на ПЛИС."),
N("dec_fpga",8,"FPGA real-time decoders (LCD, Deltaflow)","ПЛИС-декодеры реального времени (LCD, Deltaflow)",0.5,["fab","nat"],None,"na",None,"none","none",["none"],["pauli"],"none","D",
  "Local-clustering < 1 µs/round to d=17; Riverlane + Rigetti real-time loop 9.6 µs (6.5 µs decode + 3.1 µs communication, 2×2 stability patch, arXiv:2410.05202) vs Google 63 µs.","Декодер локальной кластеризации (LCD) < 1 µs/раунд до d=17; контур реального времени Riverlane + Rigetti 9.6 µs (6.5 µs декодирование + 3.1 µs связь, патч стабильности 2×2, arXiv:2410.05202) против 63 µs у Google.",
  [("clock","Riverlane LCD","< 1 µs/round to d=17","2025-12","https://www.nature.com/articles/s41467-025-66773-x"),
   ("clock","Google real-time at d=5","63 µs latency, Λ=2.0","2024-08","https://arxiv.org/abs/2408.13687")],"",""),
N("dec_gpu",8,"GPU decoding via NVQLink","GPU-декодирование через NVQLink",0.5,["fab","nat"],None,"na",None,"none","none",["none"],["pauli"],"none","D",
  "3.84 µs round trip; Helios+GH200 BP+OSD median 67 µs (5.4× LER gain); platform-agnostic layer.","Круговая задержка 3.84 µs; Helios+GH200 BP+OSD медиана 67 µs (выигрыш по частоте логических ошибок 5.4×); платформенно-независимый слой.",
  [("clock","NVQLink RoCE round trip","3.84 µs mean","2025-10","https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/")],
  "NVQLink was announced on 2025-10-28.","NVQLink анонсирован 2025-10-28."),
N("dec_corr",8,"Correlated / loss-aware decoding (transversal, atom loss)","Коррелированное декодирование / декодирование с учётом потерь (трансверсальные вентили, потеря атомов)",0.0,["nat"],None,"na",None,"none","none",["none"],["loss","erasure"],"none","D",
  "Decodes across transversal gates and uses loss flags; 1.73× QEC gain on 448-atom processor.","Декодирует сквозь трансверсальные вентили и использует флаги потерь; выигрыш QEC 1.73× на процессоре из 448 атомов.",
  [("channel","loss-aware ML decoding gain","1.73(13)×","2025-11","https://www.nature.com/articles/s41586-025-09848-5")],"",""),
N("dec_rl",8,"In-loop RL calibration / control steering","RL-калибровка в контуре / подстройка управления",1.0,["fab"],None,"na",None,"none","none",["none"],["coherent"],"none","D",
  "Reinforcement learning tunes > 1,000 control parameters during QEC: ~20% extra suppression, 3.5× drift robustness.","Обучение с подкреплением подстраивает > 1 000 параметров управления во время QEC: ~20% дополнительного подавления, 3.5× устойчивость к дрейфу.",
  [("channel","RL-steered QEC","20% LER cut, 3.5× stability vs drift; the same Willow d=7 run that yields 7.72(9)×10⁻⁴/cycle (see dec_nn)","2025-11","https://arxiv.org/abs/2511.08493")],"",""),
N("dec_cryo",8,"Cryogenic / on-chip decoder (cryo-CMOS, SFQ)","Криогенный декодер / декодер на чипе (крио-КМОП, БОК)",1.0,["fab"],None,"na",None,"none","mw",["mK"],["pauli"],"sclitho","X",
  "Designs only: NISQ+ (≤ 20 ns, SFQ), QECOOL (2.8 µW), Pinball/CryoZip (4 K predecoders) — no fabricated decoder chip.","Только проекты: NISQ+ (≤ 20 ns, БОК), QECOOL (2.8 µW), Pinball/CryoZip (предекодеры при 4 K) — ни одного изготовленного чипа-декодера.",
  [("path","QECOOL on-line SFQ decoder (simulation)","2.78 µW at 2 GHz; latency not published","2021-03","https://arxiv.org/abs/2103.14209"),
   ("clock","NISQ+ approximate SFQ decoder (design)","≤ 20 ns latency","2020-04","https://arxiv.org/abs/2004.04794"),
   ("path","cryo-CMOS predecoder (design)","3,780× syndrome-bandwidth reduction at < 0.56 mW","2025-12","https://arxiv.org/abs/2512.09807")],
  "arXiv:2103.14209 is QECOOL — an SFQ decoder, not cryo-CMOS; the ≤ 20 ns latency belongs to NISQ+ (arXiv:2004.04794).","arXiv:2103.14209 — это QECOOL, декодер на БОК-логике, а не на крио-КМОП; задержка ≤ 20 ns относится к NISQ+ (arXiv:2004.04794)."),
]
# ---------------------------------------------------------------- L9 INTERCONNECT
NODES += [
N("ic_mcm",9,"Multi-chip modules / l-couplers (same cryostat)","Многокристальные модули / l-couplers (один криостат)",1.0,["fab"],None,"na",None,"longrange","mw",["mK"],["coherent"],"sclitho","E",
  "Chiplet tiling (Rigetti 12×9 q, 99.1%) and metre-scale l-couplers between modules (IBM Cockatoo 2027 [R]).","Плитка чиплетов (Rigetti 12×9 q, 99.1%) и метровые l-couplers между модулями (IBM Cockatoo 2027 [R]).",
  [("count","chiplet tiling","108 q from 12 chiplets, median 2Q 99.1% (vs 99.5% at 36 q)","2026-04","https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system"),
   ("path","coupled cryogenic cells","two cells coupled; 0.53 m² wiring area each","2026-08","https://www.ibm.com/quantum/blog/modular-cryogenics")],"",""),
N("ic_multidie",9,"Multi-die packaging in one module (flip-chip, bump-bonded control die)","Многокристальная сборка в одном модуле (flip-chip, bump-bonding с управляющим кристаллом)",1.0,["fab"],None,"na",None,"static","mw",["mK"],["coherent"],"sclitho","D",
  "A qubit die flip-chipped to a wiring or control die inside one package — Sycamore, Zuchongzhi, Ocelot, the SFQ flip-chip module: the interconnect below the module scale, which the multi-chip-module node does not cover.","Кристалл с кубитами, соединённый flip-chip с кристаллом разводки или управления внутри одного корпуса — Sycamore, Zuchongzhi, Ocelot, модуль flip-chip на БОК-логике: межсоединение ниже масштаба модуля, которое узел многокристальных модулей не описывает.",
  (),"Bump yield and thermal mismatch are the limits; it moves the I/O wall, not the module wall.","Пределы — выход годных столбиковых соединений и тепловое рассогласование; сдвигает стену разводки, а не стену модулей."),
N("ic_fanout",9,"Cryogenic signal fan-out for spin arrays (router die, 3D stacked wiring)","Криогенная разводка сигналов для спиновых массивов (кристалл-маршрутизатор, 3D многослойная разводка)",1.0,["fab"],None,"na",None,"static","lf",["mK","4K"],["coherent"],"cmos","E",
  "A millikelvin router (Intel's Pando Tree fanning out to 64 channels), 3D stacked cryogenic wiring or on-die routing that takes a spin array from tens to thousands of gate lines — the interconnect layer the spin architectures had no slot for.","Милликельвиновый маршрутизатор (Pando Tree Intel с разводкой на 64 канала), 3D многослойная криогенная разводка или маршрутизация на кристалле, ведущие спиновый массив от десятков к тысячам линий затворов — слой межсоединения, для которого у спиновых путей не было слота.",
  (),"Channel count per die and heat load per line are the figures of merit; no inter-module link yet.","Показатели — число каналов на кристалл и тепловая нагрузка на линию; межмодульной связи пока нет."),
N("ic_cryolink",9,"Cryogenic microwave link between refrigerators","Криогенная СВЧ-линия связи между криостатами",1.0,["fab"],None,"na",None,"longrange","mw",["mK"],["loss","coherent"],"sclitho","E",
  "30 m superconducting waveguide at < 50 mK; Bell fidelity 80.4% at 12.5 kHz; 0.55–0.65 dB total loss.","30-метровый сверхпроводниковый волновод при < 50 mK; точность состояния Белла 80.4% при 12.5 kHz; суммарные потери 0.55–0.65 dB.",
  [("channel","30 m link Bell fidelity / rate","80.4% / 12.5 kHz","2023-05","https://www.nature.com/articles/s41586-023-05885-0"),
   ("path","2026 modular link","waveguide loss < 0.03 dB/30 m; end-to-end transfer loss 0.55–0.65 dB, i.e. 86–88% transmission","2026-04","https://arxiv.org/html/2604.15971v1")],
  "ETH Zürich. A '75–79% transfer efficiency' sometimes quoted is not implied by 0.55–0.65 dB, which is 86–88% transmission; the ETH paper attributes the loss to the 26 demountable module joints, and any residue would be node emission/absorption efficiency.","ETH Zürich. Иногда цитируемая «эффективность передачи 75–79%» не следует из 0.55–0.65 dB, что соответствует пропусканию 86–88%; статья ETH относит потери к 26 разъёмным стыкам модулей, а остаток пришёлся бы на эффективность излучения/поглощения в узлах."),
N("ic_ionphoton",9,"Ion–photon link","Ион-фотонный интерфейс",0.0,["nat"],None,"na",None,"flying","opt",["RT"],["loss"],"optics","D",
  "Remote Bell pairs at 9.7–250 s⁻¹ with 94–97% fidelity; teleported CZ 86%; needs ≥ 10⁴ s⁻¹.","Удалённые пары Белла при 9.7–250 s⁻¹ с точностью 94–97%; телепортированный CZ 86%; нужно ≥ 10⁴ s⁻¹.",
  [("channel","distributed CZ (Oxford)","remote Bell 96.9% at 9.7 s⁻¹; teleported CZ 86.2%","2025-02","https://www.nature.com/articles/s41586-024-08404-x"),
   ("clock","entanglement rate record","250 s⁻¹ at F > 94%","2024","https://arxiv.org/abs/2404.16167")],
  "The 2007 first remote ion–ion entanglement is Monroe's group (Michigan, later Maryland/Duke) — the lineage holding today's rate record — not the Wineland/NIST line. IonQ's 2026-04 interconnect milestone discloses no rate, fidelity or distance and asserts no measured Bell state.","Первая удалённая запутанность ион–ион 2007 года — группа Monroe (Michigan, позже Maryland/Duke), та же линия, что держит нынешний рекорд скорости, а не линия Wineland/NIST. В сообщении IonQ от 2026-04 не раскрыты ни скорость, ни точность, ни расстояние и не заявлено измеренное состояние Белла."),
N("ic_atomcavity",9,"Atom–photon cavity interface","Атом-фотонный интерфейс через резонатор",0.0,["nat"],None,"na",None,"flying","opt",["RT"],["loss"],"optics","E",
  "Tweezer atoms coupled to cavities: ~90% generation-to-detection atom–photon efficiency (MPQ); no inter-module rates yet.","Атомы в пинцетах, связанные с резонаторами: ~90% эффективность атом–фотон от генерации до детектирования (MPQ); межмодульных скоростей пока нет.",
  [("channel","atom–photon efficiency (MPQ, Science 385, 179)","~90% generation-to-detection","2024-07","https://arxiv.org/abs/2407.09109")],
  "Atom Computing–Nu Quantum/Cisco (MoUs, no numbers). A 'cavity-carved Bell fidelity 91%' sometimes quoted is not in the source abstract. Nu Quantum's $60 M Series A closed 2025-12-10, led by National Grid Partners.","Atom Computing–Nu Quantum/Cisco (меморандумы, без чисел). Иногда цитируемая «точность состояния Белла 91% через вырезание резонатором (cavity carving)» отсутствует в аннотации источника. Раунд серии A Nu Quantum на $60 млн закрыт 2025-12-10 во главе с National Grid Partners."),
N("ic_spinphoton",9,"Spin–photon solid-state link (SiV, NV, T centre)","Твердотельный спин-фотонный интерфейс (SiV, NV, T-центр)",0.5,["int"],None,"na",None,"flying","opt",["RT"],["loss"],"diamond","D",
  "Entanglement over 25–35 km deployed fibre at 0.02–1 Hz with F 0.53–0.86; two distinct inter-cryostat teleported-CNOT results — post-selected on T centres (Photonic Inc.) and unconditional on NV (QuTech).","Запутанность на 25–35 km проложенного волокна при 0.02–1 Hz с F 0.53–0.86; два разных результата по телепортированному CNOT между криостатами — постселектированный на T-центрах (Photonic Inc.) и безусловный на NV (QuTech).",
  [("channel","SiV over 35 km","F = 0.69, ≤ 1 Hz","2024-05","https://www.nature.com/articles/s41586-024-07252-z"),
   ("channel","NV Delft–The Hague 25 km","F = 0.534, 0.022 s⁻¹","2024-04","https://arxiv.org/html/2404.03723"),
   ("channel","T-centre inter-cryostat link (Photonic Inc.)","Bell F = 0.60(8) at 7.5 mHz; teleported-CNOT sequence post-selected, no gate fidelity","2024-06","https://arxiv.org/html/2406.01704v1"),
   ("channel","NV unconditional teleported CNOT (QuTech)","63(4)% (4-qubit GHZ 64(4)%), real-time feed-forward, no post-selection","2026-05","https://www.nature.com/articles/s41467-026-72818-6")],
  "Both results exist and differ in kind: Photonic Inc.'s 2024 T-centre demonstration is a post-selected preprint with a truth table rather than a gate fidelity; QuTech's 2026 NV result is unconditional. Quoting them together without that distinction overstates the T-centre platform.","Оба результата существуют и различаются по природе: демонстрация Photonic Inc. на T-центрах (2024) — постселектированный препринт с таблицей истинности вместо точности вентиля; результат QuTech на NV (2026) — безусловный. Совместное цитирование без этого различия завышает оценку платформы на T-центрах."),
N("ic_transducer",9,"Microwave–optical transducer (useful efficiency)","СВЧ-оптический преобразователь (полезной эффективности)",1.0,["fab"],None,"na",None,"flying","eo",["mK"],["loss"],"pic","X",
  "Best: η_tot 15%, N_add 0.16 (EO); useful regime needs η > 1/2 and N_add ≪ 1; ~3 orders of magnitude short (IBM analysis).","Лучшее: η_tot 15%, N_add 0.16 (электрооптика); полезный режим требует η > 1/2 и N_add ≪ 1; ~3 порядка не хватает (анализ IBM).",
  [("channel","state of the art (review)","η_int 99.5%, η_tot 15%, N_add 0.16 (EO, 60 mK)","2026-05","https://arxiv.org/html/2605.26976"),
   ("path","gap to useful","3 orders of magnitude (noise, η, rate) for 99.7% remote gates at MHz","2025-03","https://arxiv.org/abs/2503.10842")],"",""),
N("ic_fibre",9,"Fibre links between photonic modules","Волоконные линии связи между фотонными модулями",0.25,["pho"],None,"na",None,"flying","eo",["RT"],["loss"],"pic","D",
  "Chip-to-chip Bell 99.72% over 42 m (loss excluded); Aurora inter-rack fibre.","Межчиповые пары Белла 99.72% на 42 m (без учёта потерь); межстоечное волокно Aurora.",
  [("channel","chip-to-chip Bell fidelity","99.72% over 42 m, conditional on heralded events (channel loss excluded)","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "Facet coupling is quoted on two different bases: Xanadu 0.085 dB/facet [C] against PsiQuantum's published 52(12) mdB [D] for the same interface.","Стыковка на торце приводится на двух разных основаниях: 0.085 dB/торец у Xanadu [C] против опубликованных 52(12) мдБ у PsiQuantum [D] для того же интерфейса."),
]
# ---------------------------------------------------------------- L10 MANUFACTURING
NODES += [
N("fab_cmos",10,"300 mm CMOS foundry (spins, cryo-CMOS, superconducting wiring)","КМОП-фабрика 300 mm (спины, крио-КМОП, сверхпроводниковая разводка)",1.0,["fab"],None,"na",None,"none","none",["none"],["coherent"],"cmos","D",
  "Intel D1 EUV (24k devices/wafer, 96% tune-up), imec (2Q > 99%), GF 22FDX (1,024 dots), ST FD-SOI; GF now a multi-modality foundry ($375 M LOI).","Intel D1 EUV (24 тыс. устройств/пластина, 96% выход), imec (двухкубитные > 99%), GF 22FDX (1 024 точки), ST FD-SOI; GF — многомодальная фабрика ($375 млн, письмо о намерениях).",
  [("path","wafer-scale statistics","> 24,000 devices/wafer, CD < 0.5 nm","2024-10","https://arxiv.org/abs/2410.16583"),
   ("path","wafer-level yield (cryo-prober, 1.6 K)","96% of 232 twelve-dot devices tuned to single-electron occupancy; 99.8% of dots","2024-05","https://www.nature.com/articles/s41586-024-07275-6"),
   ("path","multi-modality foundry LOI","GlobalFoundries $375 M (SC, ion, photonic, topological, spin)","2026-05","https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion")],"",""),
N("fab_sc",10,"Superconducting-qubit lithography (Al/AlOx/Al junctions, Nb wiring, 300 mm)","Литография сверхпроводниковых кубитов (переходы Al/AlOx/Al, разводка из Nb, 300 mm)",1.0,["fab"],None,"na",None,"none","none",["none"],["coherent"],"sclitho","D",
  "IBM Albany 300 mm / Anderon foundry; Google Santa Barbara; Rigetti ABAA trimming (97.4% frequency-targeting success); OQC 500-qubit wafer-scale package.","IBM Albany 300 mm / фабрика Anderon; Google Santa Barbara; Rigetti ABAA-подстройка (97.4% попаданий в частоту); OQC — 500-кубитная пластинная упаковка.",
  [("path","junction frequency targeting (ABAA)","97.4% success, 0.9 ± 2.4% of prediction","2024-08","https://www.nature.com/articles/s43246-024-00596-z"),
   ("count","wafer-scale package (OQC)","> 500 qubits on one 3-inch sapphire die; T1 ~97 µs, T2e ~129 µs; no per-qubit control lines in the measured configuration","2026-02","https://arxiv.org/abs/2602.12773"),
   ("path","Anderon foundry","$1 B CHIPS + $1 B IBM; SC wiring/TSV/bump; 30× device output vs 200 mm","2026-05","https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding")],
  "The OQC package is on 3-inch sapphire; its abstract rounds median T1 and T2e together to ~100 µs, while the body reports T1 97 µs and T2e 129 µs separately; it is a packaging result, not a processor.","Сборка OQC выполнена на 3-дюймовом сапфире; аннотация округляет медианы T1 и T2e вместе до ~100 µs, а основной текст приводит их раздельно: T1 97 µs и T2e 129 µs; это результат по упаковке, а не по процессору."),
N("fab_3d",10,"3D machined superconducting cavities","Объёмные сверхпроводниковые резонаторы (механическая обработка)",1.0,["fab"],None,"na",None,"none","none",["none"],["loss"],"3d","D",
  "Machined aluminium cavities reach Q > 0.5×10⁹ (10 ms photon lifetime, Yale 2013); niobium accelerator cavities with no qubit attached hold photons for 0.5–2 s at ~10 mK (Fermilab 2020); cm-scale footprint per qubit — the scaling liability of cavity-based bosonic codes.","Механически обработанные алюминиевые резонаторы достигают Q > 0.5×10⁹ (время жизни фотона 10 ms, Yale 2013); ниобиевые ускоряющие резонаторы без кубита удерживают фотоны 0.5–2 s при ~10 mK (Fermilab 2020); сантиметровая площадь на кубит — масштабная обуза бозонных кодов на резонаторах.",
  [("channel","cavity Q (Al, Yale)","> 0.5×10⁹, single-photon lifetime 10 ms","2013","https://arxiv.org/abs/1302.4408")],
  "The 25.6 ms / 34 ms coherence figures are Weizmann (PRX Quantum 4, 030336), and neither the abstract nor the journal summary states the cavity material — 'Nb-coated' is unsupported.","Значения когерентности 25.6 ms / 34 ms — Weizmann (PRX Quantum 4, 030336); ни аннотация, ни резюме журнала не указывают материал резонатора — «покрытие Nb» не подтверждено."),
N("fab_trap",10,"Ion-trap fabrication (surface-electrode chips; machined 3D blade traps)","Изготовление ионных ловушек (планарные чипы; фрезерованные 3D ловушки-лезвия)",0.0,["nat"],None,"na",None,"none","none",["none"],["coherent"],"mems","D",
  "MEMS/CMOS-fab traps: Helios 1,228 electrodes / 273 signals; Oxford Ionics chips from standard semiconductor fabs; SkyWater in-house at IonQ.","МЭМС/КМОП-ловушки: Helios 1 228 электродов / 273 сигнала; чипы Oxford Ionics с обычных полупроводниковых фабрик; SkyWater внутри IonQ.",
  [("path","Helios trap","1,228 electrodes, 273 independent signals (2.8 per qubit)","2025-11","https://arxiv.org/html/2511.05465"),
   ("path","standard-fab traps","99.99% 2Q on chips from standard semiconductor fabs","2025-10","https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing")],"",""),
N("fab_pic",10,"Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm)","Фабрика ФИС (SiN, BTO, TFLN, SNSPD на 300 mm)",0.25,["pho"],None,"na",None,"none","none",["none"],["loss"],"pic","D",
  "GlobalFoundries Fab 8 for PsiQuantum (SiN 0.5 dB/m multimode but 1.8(2) dB/m single-mode, BTO switches, on-chip SNSPD at 93.4% median); TFLN/SiN for Xanadu; also ion integrated photonics and atom PIC traps.","GlobalFoundries Fab 8 для PsiQuantum (SiN 0.5 dB/m многомодовый, но 1.8(2) дБ/м одномодовый, BTO-переключатели, SNSPD на чипе с медианой 93.4%); TFLN/SiN для Xanadu; также интегральная фотоника ионов и ловушки атомов на ФИС.",
  [("channel","SiN waveguide loss (multimode)","0.5 dB/m","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","SiN waveguide loss (single-mode)","1.8(2) dB/m","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","wafer-scale median on-chip SNSPD efficiency","93.4% at ~2 K, 300 mm","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "The 0.5 dB/m figure is the multimode waveguide's; the single-mode Omega routing waveguide is 1.8(2) dB/m — two waveguides, not a conflict. The 98.9% median SNSPD efficiency sometimes quoted is superseded by 93.4%.","0.5 dB/m — значение многомодового волновода; одномодовый разводочный волновод Omega даёт 1.8(2) дБ/м — это два разных волновода, а не противоречие. Иногда цитируемая медианная эффективность SNSPD 98.9% вытеснена значением 93.4%."),
N("fab_optics",10,"Optical / mechanical assembly (lasers, vacuum, objectives)","Оптическая / механическая сборка (лазеры, вакуум, объективы)",0.0,["nat"],None,"na",None,"none","none",["none"],["coherent"],"optics","D",
  "Room-temperature systems: Pasqal Orion 3 kW / 2,500 kg; continuous reload hardware (2 optical-lattice conveyors, 300,000 atoms/s into tweezers → 30,000 initialised qubits/s).","Системы при комнатной температуре: Pasqal Orion 3 kW / 2 500 кг; аппаратура непрерывной дозагрузки (2 оптических решёточных конвейера, 300 000 атомов/с в пинцеты → 30 000 инициализированных кубитов/с).",
  [("path","system power / mass","3 kW avg, 2,500 kg (Orion Gamma)","2025-11","https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf"),
   ("path","continuous reload hardware","300,000 atoms/s reloaded into tweezers; 30,000 initialised qubits/s","2025-09","https://www.nature.com/articles/s41586-025-09596-6")],
  "The two rates are different quantities and both are correct: 300,000 atoms/s is the reload rate into tweezers, 30,000/s the rate of initialised qubits. Long-range transport in that system is by optical-lattice conveyor belts.","Две скорости — разные величины, и обе верны: 300 000 атомов/с — темп дозагрузки в пинцеты, 30 000/с — темп инициализированных кубитов. Дальний транспорт в этой системе выполняют оптические решёточные конвейеры."),
N("fab_bulk",10,"Bulk-optics and fibre assembly (photonic samplers)","Сборка из объёмной оптики и волокна (фотонные сэмплеры)",0.25,["pho"],None,"na",None,"none","none",["none"],["loss"],"optics","D",
  "Table-top optics and fibre loops assembled by hand — Jiuzhang, Borealis, PT-2 — as opposed to a photonic-IC foundry; it is how every beyond-classical sampler was built and how none of the fault-tolerant photonic machines will be.","Настольная оптика и волоконные петли, собранные вручную — Jiuzhang, Borealis, PT-2 — в отличие от фабрики ФИС; так была построена каждая машина сэмплирования за пределами классики и так не будет построена ни одна отказоустойчивая фотонная машина.",
  (),"Alignment drift and per-element loss set the run length; no volume manufacturing path.","Дрейф юстировки и потери на элемент определяют длительность прогона; пути к серийному производству нет."),
N("fab_mbe",10,"III-V MBE heterostructures (InAs–Pb wires, QD sources)","Гетероструктуры A3B5 (МЛЭ; проволоки InAs–Pb, КТ-источники)",0.75,["fab","pho"],None,"na",None,"none","none",["none"],["unknown"],"mbe","D",
  "In-house Microsoft growth for tetrons (no external replication); GaAs quantum-dot photon sources (Quandela).","Собственное выращивание у Microsoft для тетронов (без внешней репликации); GaAs квантово-точечные источники фотонов (Quandela).",
  [("path","replication","no independent replication of the InAs–Pb stack","2026-06","https://www.nature.com/articles/s41586-026-10567-8")],
  "Lead against aluminium in Microsoft's stacks: the superconductor's own gap ≈1.3 meV vs 295 µeV and the induced gap ≈570 vs 129 µeV, each about fourfold; the top-quintile topological gap ~70 vs ~30 µeV, about twofold (tetron preprint, 2026; PRB 107, 245423). The lineage starts with in-situ epitaxial Al on InAs nanowires (Copenhagen, 2015); the 2018 quantised-Majorana-conductance claim, made on InSb–Al wires (Nature 556), was retracted on 2021-03-08. MBE growth equipment is export-controlled under ECCN 3B001.a.3; the 2024 rule's 3C907 covers only epitaxy of isotopically enriched Si or Ge. QuTech's InSb wires are grown at TU Eindhoven (Bakkers).","Свинец против алюминия в стеках Microsoft: собственная щель сверхпроводника ≈1.3 meV против 295 µeV и наведённая щель ≈570 против 129 µeV — примерно вчетверо; топологическая щель по верхней квинтили ~70 против ~30 µeV — примерно вдвое (препринт о тетроне, 2026; PRB 107, 245423). Линия начинается с эпитаксиального Al, выращенного in situ на нанопроводах InAs (Копенгаген, 2015); заявление 2018 года о квантованной майорановской проводимости, сделанное на проводах InSb–Al (Nature 556), отозвано 2021-03-08. Ростовое оборудование МЛЭ подпадает под экспортный контроль по ECCN 3B001.a.3; 3C907 из правила 2024 года покрывает лишь эпитаксию изотопно обогащённых Si или Ge. Проволоки InSb для QuTech выращивают в TU Eindhoven (группа Bakkers)."),
N("fab_stm",10,"STM hydrogen-resist lithography (donors)","СТМ-литография (доноры)",0.5,["int"],None,"na",None,"none","none",["none"],["pauli"],"stm","D",
  "Atom-precise placement of P donors (~3 nm); bespoke, serial, no foundry route.","Атомно-точное размещение доноров P (~3 nm); штучно, последовательно, без фабричного пути.",
  [("count","register size","11 qubits","2025-12","https://www.nature.com/articles/s41586-025-09827-w")],
  "The ~3 nm figure is the incorporated donor's positional uncertainty from segregation and diffusion during encapsulation — the limiting step is thermal, not lithographic; ~1 nm is not supported.","~3 nm — неопределённость положения встроенного донора из-за сегрегации и диффузии при заращивании: ограничивающая стадия термическая, а не литографическая; ~1 nm не подтверждается."),
N("fab_diamond",10,"Diamond growth / implantation (NV, SiV, SnV)","Выращивание алмаза / имплантация (NV, SiV, SnV)",0.5,["int"],None,"na",None,"none","none",["none"],["pauli"],"diamond","D",
  "SnV nanocavities (QuTech, PRX 2026): 327 characterised at room temperature on two chips, coupled centres in 7 of 9 cooled, two measured above cooperativity one — no chip-wide yield published; Quantum Brilliance diamond foundry.","SnV-нанорезонаторы (QuTech, PRX 2026): 327 охарактеризованы при комнатной температуре на двух чипах, связанные центры в 7 из 9 охлаждённых, у двух измерена кооперативность выше единицы — выход годных по чипу не опубликован; алмазная фабрика Quantum Brilliance.",
  [("path","device yield","327 cavities resonance-characterised at room temperature (mean Q 1.1(4)×10⁴); coherent cooperativity > 1 shown on 2","2026-06","https://journals.aps.org/prx/abstract/10.1103/z514-v4n6")],
  "Element Six's DNV-B1 (2020) is an NV-*ensemble* sensing grade, not a substrate for single-defect network nodes, which need electronic-grade plates.","DNV-B1 от Element Six (2020) — сенсорный сорт для *ансамблей* NV, а не подложка для сетевых узлов на одиночных дефектах, где нужны пластины электронного качества."),
]
# ---------------------------------------------------------------- extra nodes (added while assembling paths)
NODES += [
N("enc_spin_ld",2,"Single-spin (Loss–DiVincenzo) / nuclear-spin encoding","Кодирование на одиночном спине (Лосса–ДиВинченцо) / ядерном спине",0.75,["fab","int"],None,"na",None,"none","none",["none"],["coherent","pauli"],"none","D",
  "Bare spin-1/2 of an electron, hole or nucleus; needs microwave/EDSR for 1Q.","«Голый» спин-1/2 электрона, дырки или ядра; для однокубитных вентилей нужны СВЧ/EDSR.",[],"",""),
N("g_cv",3,"CV Gaussian gates + GKP-assisted non-Gaussian operations","Гауссовы вентили на непрерывных переменных + негауссовы операции с помощью GKP",0.25,["pho"],-6.0,"det",None,"flying","eo",["RT"],["gauss","loss"],"pic","D",
  "Beamsplitters, squeezers and homodyne feed-forward on optical modes at 1 MHz clock (Aurora).","Светоделители, сжиматели и прямая связь по результатам гомодинных измерений на оптических модах при такте 1 MHz (Aurora).",
  [("clock","Aurora clock","1 MHz, 12 modes per cycle","2025-01","https://www.nature.com/articles/s41586-024-08406-9")],
  "Time-domain-multiplexed CV cluster states originate with Yokoyama et al. (University of Tokyo, 2013, > 10,000 modes); Xanadu's Aurora is the first modular chip-based networked version, not the first such state.","Кластерные состояния на непрерывных переменных с временным мультиплексированием восходят к Yokoyama et al. (University of Tokyo, 2013, > 10 000 мод); Aurora у Xanadu — первая модульная сетевая версия на чипах, а не первое такое состояние."),
N("g_mwspin",3,"Microwave / optical spin gates (defect centres, 1Q spins)","СВЧ / оптические спиновые вентили (центры окраски, однокубитные спины)",0.5,["int","fab"],-6.0,"det",None,"static","mw",["RT"],["pauli","coherent"],"diamond","D",
  "ESR/EDSR-driven rotations and hyperfine-conditional gates; < 0.1% error on NV electron+nuclear registers.","Вращения на ESR/EDSR и сверхтонко-условные вентили; ошибка < 0.1% на регистрах NV электрон+ядро.",
  [("channel","NV 1Q/2Q (GST)","< 0.1% [P] — press release only, no primary paper","2025-03","https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/")],
  "The Fujitsu/QuTech '< 0.1%' figure is cited from the press release [P], which names a Phys. Rev. Applied paper (2025-03-21) not yet located by us.","Значение «< 0.1%» от Fujitsu/QuTech цитируется по пресс-релизу [P], который называет статью в Phys. Rev. Applied (2025-03-21), нами пока не найденную."),
N("g_catcnot",3,"Bias-preserving cat–cat CNOT","Сохраняющий смещение CNOT между кошачьими кубитами",1.0,["fab"],None,"det",None,"bus","mw",["RT"],["bias"],"sclitho","X",
  "Required by every cat-qubit resource estimate; proposed since 2019 (Guillaud–Mirrahimi) and 2020 (Puri et al.), the first unitary scheme in July 2026; no demonstration.","Требуется каждой оценкой ресурсов для кошачьих кубитов; предложен с 2019 (Guillaud–Mirrahimi) и 2020 (Puri et al.), первая унитарная схема — июль 2026; демонстрации нет.",
  [("channel","status","no experimental bias-preserving cat–cat CNOT","2026-07","https://arxiv.org/abs/2607.22852")],"",""),
N("src_resource",3,"Multi-photon resource-state generator (RSG; 6-ring etc.)","Генератор многофотонных ресурсных состояний (RSG; 6-ring и т.п.)",0.25,["pho"],None,"her",None,"flying","eo",["RT"],["loss"],"pic","X",
  "Fusion-based FT needs 24–168-photon encoded resource states at high rate; largest fused deterministic-emitter graph states are 8 photons at < 1 Hz.","Для отказоустойчивости на основе слияний нужны кодированные ресурсные состояния из 24–168 фотонов с высокой скоростью; крупнейшие слитые графовые состояния от детерминированных излучателей — 8 фотонов при < 1 Hz.",
  [("count","largest emitter-fused graph state","8 qubits, 0.4–2.3 coincidences/min","2024-05","https://www.nature.com/articles/s41586-024-07357-5"),
   ("count","independent emitter graph states (C2N Paris-Saclay)","reconfigurable 4-photon graph states from one quantum dot, ~0.5 Hz","2025-05","https://www.nature.com/articles/s41467-025-59693-3")],
  "Quandela's Lucy was delivered to CEA in 2025-10 and launched on the Joliot-Curie HPC system on 2026-04-14 — delivery and integration, two dates for two events.","Lucy у Quandela поставлена в CEA в 2025-10 и запущена на суперкомпьютере Joliot-Curie 2026-04-14 — поставка и интеграция, две даты для двух событий."),
N("ct_eo",5,"Electro-optic drive + feed-forward electronics (room temperature)","Электрооптическое управление + электроника прямой связи (комн. т.)",0.25,["pho"],None,"na",None,"none","eo",["RT"],["loss"],"pic","D",
  "MHz–GHz switching of BTO/TFLN modulators conditioned on detector outcomes within one clock cycle.","МГц–ГГц переключение BTO/TFLN-модуляторов по результатам детекторов в пределах одного такта.",
  [("clock","single-clock-cycle feed-forward","1 MHz (Aurora)","2025-01","https://www.nature.com/articles/s41586-024-08406-9")],"",""),
N("ro_imgfast",6,"Fast (≤ 20 µs) atom-array readout","Быстрое (≤ 20 µs) считывание массивов атомов",0.0,["nat"],None,"na",C("img",-4.75,False,True),"none","opt",["RT"],["loss"],"optics","E",
  "Neutral-Yb imaging in 17.6 µs at 99.89% discrimination / 98.8% survival (Kyoto); cuts the imaging term 30–50×, but the whole QEC round improves only ~2× — transport and the camera link remain.","Регистрация флуоресценции нейтрального Yb за 17.6 µs при 99.89% различения / 98.8% выживания (Kyoto); сокращает вклад регистрации в 30–50 раз, но весь раунд QEC улучшается лишь ~в 2 раза — остаются транспорт и канал камеры.",
  [("clock","fast imaging","17.6 µs, 99.89%, survival 98.8% — neutral ¹⁷⁴Yb, spinless","2026-08","https://arxiv.org/html/2605.24175")],
  "The 30–50× applies to the imaging term alone (Amdahl): a 1–4.5 ms round is imaging plus transport plus a 442 µs camera-to-server transfer, so the round improves ~2×. The 'suppression vanished once reloading was included' result belongs to Atom Computing's toric code (arXiv:2606.04079), not to the Harvard 448-atom processor.","Множитель 30–50 относится только к вкладу регистрации флуоресценции (закон Амдала): раунд в 1–4.5 ms складывается из регистрации, транспорта и передачи кадра камера-сервер за 442 µs, поэтому раунд улучшается ~в 2 раза. Результат «подавление исчезло, как только включили дозагрузку» относится к торическому коду Atom Computing (arXiv:2606.04079), а не к 448-атомному процессору Harvard."),
]
SINCE={'transmon': 2007, 'fluxonium': 2009, 'cavity': 2013, 'ion': 1995, 'alkali': 2016, 'ae_atom': 2019, 'photon': 2001, 'squeezed': 2012, 'qd_spin': 2012, 'donor': 2012, 'defect': 2004, 'majorana': 2025, 'fluxq': 2011, 'enc_bare': 2007, 'enc_hf': 1995, 'enc_opt': 2003, 'enc_omg': 2023, 'enc_dualrail': 2023, 'enc_cat': 2020, 'enc_gkp': 2020, 'enc_eo': 2013, 'enc_timebin': 1999, 'enc_parity': 2025, 'enc_spin_ld': 1998, 'g_tc': 2014, 'g_cr': 2011, 'g_ryd': 2010, 'g_ms': 2003, 'g_elec': 2024, 'g_exch': 2018, 'g_fusion': 2005, 'g_bos': 2018, 'g_mbq': 2030, 'g_anneal': 2011, 'g_cv': 2020, 'g_mwspin': 2004, 'g_catcnot': 2030, 'src_resource': 2030, 'cx_nn': 2014, 'cx_lr': 2023, 'cx_qccd': 2002, 'cx_bus': 2003, 'cx_aod': 2022, 'cx_shuttle': 2025, 'cx_switch': 2015, 'cx_crossbar': 2023, 'ct_rt': 2007, 'ct_cryocmos': 2024, 'ct_sfq': 2026, 'ct_fluxdac': 2026, 'ct_laser': 2016, 'ct_pic_trap': 2026, 'ct_ionlaser': 2020, 'ct_ionmw': 2024, 'ct_base': 2012, 'ct_eo': 2020, 'ro_disp': 2005, 'ro_fluor': 1995, 'ro_img': 2016, 'ro_s2c': 2004, 'ro_spd': 2001, 'ro_qcap': 2025, 'ro_erasure': 2023, 'ro_imgfast': 2026, 'code_surface': 2023, 'code_color': 2024, 'code_qldpc': 2025, 'code_highrate': 2024, 'code_erasure': 2025, 'code_bosonic': 2024, 'code_fusion': 2030, 'code_aft': 2025, 'code_magic': 2025, 'dec_mwpm': 2015, 'dec_nn': 2024, 'dec_relaybp': 2025, 'dec_fpga': 2025, 'dec_gpu': 2025, 'dec_corr': 2025, 'dec_rl': 2026, 'dec_cryo': 2030, 'ic_mcm': 2025, 'ic_cryolink': 2020, 'ic_ionphoton': 2007, 'ic_atomcavity': 2024, 'ic_spinphoton': 2013, 'ic_transducer': 2030, 'ic_fibre': 2025, 'fab_cmos': 2022, 'fab_sc': 2007, 'fab_3d': 2013, 'fab_trap': 2006, 'fab_pic': 2015, 'fab_optics': 2016, 'fab_mbe': 2015, 'fab_stm': 2012, 'fab_diamond': 2010, 'enc_gr': 2017, 'g_rydanalog': 2017, 'g_lointer': 2020, 'cx_reload': 2024, 'ct_ionaod': 2016, 'ct_vio': 2016, 'ro_reset': 2018, 'ro_fluxro': 2011, 'ro_homodyne': 2012, 'code_mitig': 2017, 'code_detect': 2017, 'ic_multidie': 2017, 'ic_fanout': 2025, 'fab_bulk': 2020}
for n in NODES: n["since"]=SINCE[n["id"]]
# fix: fluorescence readout is shared by ions and defect spins
for n in NODES:
    if n["id"]=="ro_fluor": n["cls"]=["nat","int"]
    if n["id"]=="cx_qccd": n["b"]["t"]=-2.7   # ~2 ms per QEC round incl. transport & cooling (per-layer 55 ms on Helios)
    if n["id"]=="cx_bus": n["b"]["t"]=None

# ---------------------------------------------------------------- PLATFORM PATHS (one node per layer; alternates listed)
def P(id,en,ru,family,cls,slots,actors,cycle_measured,goals):
    return dict(id=id,en=en,ru=ru,family=family,cls=cls,slots=slots,actors=actors,cycle=cycle_measured,goals=goals)
PATHS=[
P("sc","Transmon lattice with tunable couplers","Решётка трансмонов с перестраиваемыми элементами связи","SC","fab",
  {1:["transmon","fluxonium"],2:["enc_bare"],3:["g_tc","g_cr"],4:["cx_nn","cx_lr"],5:["ct_rt","ct_vio","ct_cryocmos","ct_sfq"],6:["ro_disp","ro_reset"],7:["code_surface","code_color","code_qldpc","code_magic","code_detect","code_mitig"],8:["dec_nn","dec_mwpm","dec_fpga","dec_relaybp","dec_rl","dec_gpu","dec_cryo"],9:["ic_mcm","ic_multidie","ic_cryolink","ic_transducer"],10:["fab_sc","fab_cmos"]},
  "IBM (Heron, Nighthawk), Google (Willow), Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu/RIKEN, QuantWare","1.1 µs (Willow QEC cycle)","G2 G3 G4"),
P("cat","Bosonic cavity qubits — cat and GKP","Бозонные кубиты в резонаторах — кошачьи кубиты и GKP","SC","fab",
  {1:["cavity"],2:["enc_cat","enc_gkp"],3:["g_bos","g_catcnot"],4:["cx_nn"],5:["ct_rt"],6:["ro_disp"],7:["code_bosonic"],8:["dec_mwpm"],9:["ic_mcm","ic_multidie"],10:["fab_sc","fab_3d"]},
  "Alice & Bob, AWS, Nord Quantique","2.8 µs (Ocelot cycle)","G3 G4"),
P("dualrail","Dual-rail erasure qubits","Двухрельсовые кубиты со стираниями","SC","fab",
  {1:["cavity","transmon"],2:["enc_dualrail"],3:["g_bos"],4:["cx_nn"],5:["ct_rt","ct_vio","ct_fluxdac"],6:["ro_erasure","ro_disp"],7:["code_erasure"],8:["dec_mwpm"],9:["ic_mcm","ic_multidie"],10:["fab_3d","fab_sc"]},
  "D-Wave/QCI, AWS, SUSTech","~2 µs (CZ 500 ns + 384 ns check)","G3 G4"),
P("ion_qccd","Trapped ions — QCCD (transport between zones)","Ионы в ловушках — QCCD (перемещение между зонами)","ION","nat",
  {1:["ion"],2:["enc_hf"],3:["g_ms","g_elec"],4:["cx_qccd"],5:["ct_ionaod","ct_ionlaser","ct_ionmw"],6:["ro_fluor"],7:["code_highrate","code_color","code_magic","code_detect"],8:["dec_gpu","dec_mwpm"],9:["ic_ionphoton"],10:["fab_trap","fab_optics","fab_cmos","fab_pic"]},
  "Quantinuum (H1, H2, Helios, Sol), Universal Quantum","~1–5 ms syndrome cycle; 55 ms per full layer (Helios)","G2 G3 G6 G7"),
P("ion_chain","Trapped ions — linear Paul trap with individual laser addressing","Ионы в ловушках — линейная ловушка Пауля с индивидуальной лазерной адресацией","ION","nat",
  {1:["ion"],2:["enc_hf","enc_opt","enc_omg"],3:["g_ms"],4:["cx_bus"],5:["ct_ionaod","ct_ionlaser"],6:["ro_fluor"],7:["code_qldpc","code_highrate","code_color","code_detect","code_magic"],8:["dec_mwpm","dec_relaybp"],9:["ic_ionphoton"],10:["fab_trap","fab_optics","fab_pic"]},
  "IonQ (Aria, Forte, Tempo), AQT, Qudoor, Maryland/Duke (EURIQA), Innsbruck","~ms (IonQ decoder assumption); 1–5 ms cycles in QCCD-class experiments","G2 G3 G6 G7"),
P("ion_elec","Trapped ions — electronic qubit control (microwave / RF gates)","Ионы в ловушках — электронное управление кубитами (СВЧ / РЧ вентили)","ION","nat",
  {1:["ion"],2:["enc_hf","enc_omg"],3:["g_elec"],4:["cx_bus","cx_qccd"],5:["ct_ionmw"],6:["ro_fluor"],7:["code_qldpc","code_highrate"],8:["dec_relaybp","dec_mwpm"],9:["ic_ionphoton"],10:["fab_trap","fab_cmos","fab_optics"]},
  "Oxford Ionics (IonQ), eleQtron, QUDORA, Universal Quantum","~1–5 ms (IonQ decoder assumption)","G2 G3 G6 G7"),
P("atom_rb","Rydberg tweezer array — alkali (Rb/Cs)","Ридберговский массив пинцетов — щелочные атомы (Rb/Cs)","ATOM","nat",
  {1:["alkali"],2:["enc_hf"],3:["g_ryd"],4:["cx_aod","cx_reload"],5:["ct_laser","ct_pic_trap"],6:["ro_img"],7:["code_highrate","code_surface","code_color","code_aft","code_magic"],8:["dec_corr","dec_nn","dec_gpu","dec_mwpm"],9:["ic_atomcavity"],10:["fab_optics","fab_pic"]},
  "Harvard/MIT, QuEra (Gemini), Pasqal (Orion), Infleqtion, Google (2026; species not stated)","~1–4.5 ms per QEC round","G1 G3 G7"),
P("atom_ae","Rydberg tweezer array — alkaline-earth (Yb/Sr), erasure-native","Ридберговский массив пинцетов — щёлочноземельные атомы (Yb/Sr), естественные стирания","ATOM","nat",
  {1:["ae_atom"],2:["enc_omg","enc_hf","enc_opt"],3:["g_ryd"],4:["cx_aod","cx_reload"],5:["ct_laser"],6:["ro_img","ro_erasure","ro_imgfast"],7:["code_erasure","code_surface"],8:["dec_corr","dec_mwpm"],9:["ic_atomcavity"],10:["fab_optics"]},
  "Atom Computing/Microsoft, Princeton, Caltech, planqc, Yaqumo","~1–4 ms","G1 G3 G7"),
P("atom_analog","Neutral-atom analog simulator (Rydberg arrays, lattice gases)","Аналоговый симулятор на нейтральных атомах (ридберговские массивы, решёточные газы)","ATOM","nat",
  {1:["alkali","ae_atom"],2:["enc_gr"],3:["g_rydanalog"],4:["cx_aod"],5:["ct_laser"],6:["ro_img"],7:[],8:[],9:[],10:["fab_optics"]},
  "QuEra (Aquila), Pasqal (Fresnel; Orion in analog mode), ICFO (QUIONE)","n/a — analog evolution, µs-class; no cycle","G1"),
P("ph_fusion","Fusion-based photonic (FBQC)","Фотоника на основе слияний (FBQC)","PHOTON","pho",
  {1:["photon"],2:["enc_timebin","enc_dualrail"],3:["g_fusion","src_resource"],4:["cx_switch"],5:["ct_eo"],6:["ro_spd"],7:["code_fusion"],8:["dec_mwpm"],9:["ic_fibre"],10:["fab_pic","fab_mbe"]},
  "PsiQuantum (Omega), Quandela, QuiX","MHz–GHz by design; no logical cycle","G4 G6"),
P("ph_cv","Continuous-variable photonic — GKP","Фотоника на непрерывных переменных — GKP","PHOTON","pho",
  {1:["squeezed"],2:["enc_gkp"],3:["g_cv","g_fusion"],4:["cx_switch"],5:["ct_eo"],6:["ro_homodyne","ro_spd"],7:["code_bosonic","code_qldpc"],8:["dec_relaybp","dec_mwpm"],9:["ic_fibre"],10:["fab_pic"]},
  "Xanadu (Aurora)","1 MHz clock (Aurora); no logical cycle","G4 G6"),
P("ph_sampler","Boson sampler","Бозонный сэмплер","PHOTON","pho",
  {1:["squeezed","photon"],2:[],3:["g_lointer"],4:["cx_switch"],5:["ct_eo"],6:["ro_spd"],7:[],8:[],9:[],10:["fab_bulk","fab_pic"]},
  "USTC (Jiuzhang), Xanadu (Borealis), ORCA","n/a — sampling; MHz-class clock, no cycle","G1"),
P("spin_qd","Silicon / germanium quantum-dot spins","Кремниевые / германиевые спины в квантовых точках","SPIN","fab",
  {1:["qd_spin"],2:["enc_spin_ld","enc_eo"],3:["g_exch","g_mwspin"],4:["cx_nn","cx_shuttle","cx_crossbar"],5:["ct_base","ct_cryocmos","ct_rt"],6:["ro_s2c"],7:["code_surface","code_qldpc"],8:["dec_mwpm"],9:["ic_fanout"],10:["fab_cmos"]},
  "Intel, Diraq, Quantum Motion, HRL→IBM, QuTech/Groove, Quobly, Equal1","~100 µs – 300 µs (readout-limited)","G4 G7"),
P("spin_donor","Donor spins in silicon","Донорные спины в кремнии","SPIN","int",
  {1:["donor"],2:["enc_spin_ld"],3:["g_exch","g_mwspin"],4:["cx_nn"],5:["ct_base","ct_rt"],6:["ro_s2c"],7:["code_surface"],8:["dec_mwpm"],9:[],10:["fab_stm"]},
  "SQC","~ms (nuclear-spin gates µs, readout 100 µs)","G7"),
P("defect","Colour-centre spins — network nodes (NV/SiV/T)","Спины центров окраски — узлы сети (NV/SiV/T)","DEFECT","int",
  {1:["defect"],2:["enc_spin_ld"],3:["g_mwspin"],4:["cx_nn"],5:["ct_base","ct_rt"],6:["ro_fluor"],7:["code_qldpc"],8:[],9:["ic_spinphoton"],10:["fab_diamond","fab_pic"]},
  "QuTech/Fujitsu, Harvard, Photonic Inc, Quantum Brilliance","n/a (network node)","G6"),
P("topo","Topological — tetron (Majorana)","Топологические — тетрон (майорановские)","TOPO","fab",
  {1:["majorana"],2:["enc_parity"],3:["g_mbq"],4:["cx_nn"],5:["ct_base"],6:["ro_qcap"],7:[],8:[],9:[],10:["fab_mbe"]},
  "Microsoft","n/a (no qubit)","—"),
P("anneal","Quantum annealer — flux qubits","Квантовый отжигатель — потоковые кубиты","ANNEAL","fab",
  {1:["fluxq"],2:[],3:["g_anneal"],4:["cx_lr"],5:["ct_fluxdac"],6:["ro_fluxro","ro_disp"],7:[],8:[],9:[],10:["fab_sc"]},
  "D-Wave","µs–ms anneal; 3.6–27 ns quenches","G1 G5"),
]
# ---------------------------------------------------------------- EDGES
def E(t,a,b,en,ru): return dict(type=t,src=a,dst=b,en=en,ru=ru)
# short names (nicknames) for the map's path chips and the §8.3 headings — decided 26 Sep 2026 from the architecture pass
SHORT_PATH={"sc":("Transmon lattice","Решётка трансмонов"),"cat":("Cat & GKP cavities","Кошачьи кубиты и GKP"),"dualrail":("Dual-rail erasure","Двухрельсовые со стираниями"),
 "ion_qccd":("QCCD ions","Ионы QCCD"),"ion_chain":("Laser-addressed chain","Лазерно-адресуемая цепочка"),"ion_elec":("Electronic ion gates","Электронные вентили на ионах"),
 "atom_rb":("Alkali Rydberg gates","Ридберговские вентили (Rb/Cs)"),"atom_ae":("Alkaline-earth arrays","Щёлочноземельные массивы"),"atom_analog":("Analog atom simulator","Аналоговый атомный симулятор"),
 "ph_fusion":("Photon fusion","Фотонное слияние"),"ph_cv":("Optical GKP","Оптический GKP"),"ph_sampler":("Boson sampling","Бозонный сэмплинг"),
 "spin_qd":("CMOS spin qubits","КМОП-спиновые кубиты"),"spin_donor":("Donor spins","Донорные спины"),"defect":("Spin–photon nodes","Спин-фотонные узлы"),
 "topo":("Majorana parity","Майорановская чётность"),"anneal":("Flux-qubit annealer","Потоковый отжигатель")}
for _p in PATHS: _p["short"]={"en":SHORT_PATH[_p["id"]][0],"ru":SHORT_PATH[_p["id"]][1]}
# slots an architecture leaves empty by design — not a missing technology but a layer its mode of operation has no use for
# (27 Sep 2026: the analog simulator's "∅ empty slot" in the code layer read as a gap). Other empty slots stay gaps.
NA_SLOTS={
 "atom_analog":{7:("no code — analog operation","нет кода — аналоговый режим"),8:("no decoder — analog operation","нет декодера — аналоговый режим"),9:("no interconnect — a single array","нет межсоединения — один массив")},
 "anneal":{2:("no encoding layer — the flux qubit is the annealer's variable","нет слоя кодирования — потоковый кубит и есть переменная отжига"),7:("no code — annealing","нет кода — отжиг"),8:("no decoder — annealing","нет декодера — отжиг"),9:("no interconnect — one QPU","нет межсоединения — один QPU")},
 "ph_sampler":{2:("no encoding layer — photon-number sampling","нет слоя кодирования — выборка числа фотонов"),7:("no code — sampling","нет кода — сэмплирование"),8:("no decoder — sampling","нет декодера — сэмплирование"),9:("no interconnect — one interferometer","нет межсоединения — один интерферометр")},
}
for _p in PATHS: _p["na"]={str(k):list(v) for k,v in NA_SLOTS.get(_p["id"],{}).items()}
EDGES=[]
REQ=[
("g_tc","transmon","flux-tunable coupler between transmons","перестраиваемый элемент связи между трансмонами"),
("g_cr","transmon","fixed-frequency transmons","трансмоны фиксированной частоты"),
("g_ryd","alkali","Rydberg excitation of the atom","ридберговское возбуждение атома"),("g_ryd","ae_atom","Rydberg excitation of the atom","ридберговское возбуждение атома"),
("g_ryd","ct_laser","Rydberg lasers, global pulses","ридберговские лазеры, глобальные импульсы"),
("g_ms","ion","spin–motion coupling","связь спин–движение"),("g_ms","ct_ionlaser","laser fields (integrated delivery)","лазерные поля (встроенная доставка)"),
("g_elec","ion","chip currents act on the ion","токи чипа действуют на ион"),("g_elec","ct_ionmw","electronic signal sources","электронные источники сигнала"),
("g_exch","qd_spin","exchange between dots","обмен между точками"),("g_exch","donor","exchange between donors","обмен между донорами"),("g_exch","ct_base","voltage pulses on gates","импульсы напряжения на затворах"),
("g_fusion","photon","photons to fuse","фотоны для слияния"),("g_fusion","ro_spd","heralding detection","оповещающее детектирование"),("g_fusion","cx_switch","feed-forward routing","маршрутизация с прямой связью"),
("g_cv","squeezed","squeezed modes","сжатые моды"),("g_cv","ct_eo","homodyne feed-forward","прямая связь по гомодинным измерениям"),
("g_bos","cavity","bosonic modes","бозонные моды"),("g_bos","transmon","ancilla transmon","анцилла-трансмон"),
("g_catcnot","enc_cat","two cat qubits","два кошачьих кубита"),
("g_mbq","majorana","Majorana wires","майорановские проволоки"),("g_mbq","ro_qcap","measurement-based","через измерения"),
("g_mwspin","defect","spin register","спиновый регистр"),
("src_resource","g_fusion","fusions build the resource state","слияния строят ресурсное состояние"),("src_resource","photon","deterministic or multiplexed photons","детерминированные или мультиплексированные фотоны"),
("enc_cat","cavity","two-photon dissipation on a mode","двухфотонная диссипация на моде"),("enc_gkp","cavity","microwave GKP","СВЧ GKP"),("enc_gkp","squeezed","optical GKP needs ~10 dB squeezing","оптический GKP требует ~10 dB сжатия"),
("enc_dualrail","ro_erasure","erasure check","проверка на стирание"),("enc_omg","ae_atom","metastable manifold","метастабильное многообразие"),("enc_omg","ion","metastable ion levels","метастабильные уровни иона"),("enc_opt","ion","S–D quadrupole transition of an alkaline-earth ion","S–D квадрупольный переход иона щёлочноземельного металла"),("enc_opt","ae_atom","¹S₀–³P₀ clock transition of Sr/Yb","часовой переход ¹S₀–³P₀ Sr/Yb"),
("enc_eo","qd_spin","three-dot encoded qubit","кубит на трёх точках"),("enc_timebin","photon","photonic modes","фотонные моды"),("enc_parity","majorana","two wires per tetron","две проволоки на тетрон"),("enc_bare","transmon","anharmonic subspace","ангармоническое подпространство"),
("cx_qccd","ion","ions to move","перемещаемые ионы"),("cx_qccd","fab_trap","junction / grid traps","ловушки с перекрёстками / решётчатые"),
("cx_aod","ct_laser","AOD deflectors","акустооптические дефлекторы (АОД)"),("cx_shuttle","qd_spin","spins to move","переносимые спины"),("cx_shuttle","fab_cmos","uniform conveyor gates","однородные конвейерные затворы"),
("cx_lr","fab_sc","multilayer routing","многослойная разводка"),("cx_switch","fab_pic","low-loss switches","переключатели с малыми потерями"),("cx_crossbar","qd_spin","dot array","массив точек"),
("ct_sfq","fab_sc","flip-chip SFQ MCM","flip-chip SFQ MCM"),("ct_cryocmos","fab_cmos","cryo ASIC","крио-ASIC"),("ct_fluxdac","fab_sc","on-chip SFQ DACs","on-chip SFQ DAC"),
("ct_pic_trap","fab_pic","photonic chip","фотонный чип"),("ct_ionlaser","fab_pic","integrated waveguides","интегральные волноводы"),("ct_ionmw","fab_trap","current traces in the trap","токовые дорожки в ловушке"),("ct_eo","fab_pic","modulators","модуляторы"),
("ro_disp","transmon","dispersive shift","дисперсионный сдвиг"),("ro_disp","cavity","ancilla-mediated readout","считывание через анциллу"),
("ro_fluor","ion","cycling transition","циклический переход"),("ro_fluor","defect","optical readout of the spin","оптическое считывание спина"),
("ro_img","alkali","imaging transition","переход для регистрации флуоресценции"),("ro_img","ae_atom","imaging transition","переход для регистрации флуоресценции"),("ro_imgfast","ae_atom","Yb fast imaging","быстрая регистрация флуоресценции Yb"),
("ro_s2c","qd_spin","charge sensor","зарядовый сенсор"),("ro_s2c","donor","charge sensor","зарядовый сенсор"),("ro_spd","photon","detection","детекция"),("ro_qcap","majorana","quantum capacitance","квантовая ёмкость"),
("ro_erasure","enc_dualrail","erasure-detectable encoding","кодирование с детектируемыми стираниями"),("ro_erasure","enc_omg","erasure-detectable encoding","кодирование с детектируемыми стираниями"),
("code_surface","cx_nn","2D nearest-neighbour checks","2D-проверки ближайших соседей"),("code_color","cx_nn","2D checks","2D-проверки"),
("code_qldpc","cx_lr","degree-6 long-range checks","дальние проверки степени 6"),("code_qldpc","cx_qccd","long-range via transport","дальние связи через транспорт"),("code_qldpc","cx_bus","all-to-all in chain","«все со всеми» в цепочке"),("code_qldpc","cx_aod","long-range via transport","дальние связи через транспорт"),
("code_highrate","cx_aod","transversal blocks by transport","трансверсальные блоки через транспорт"),("code_highrate","cx_qccd","all-to-all via QCCD","«все со всеми» через QCCD"),("code_highrate","cx_bus","all-to-all in chain","«все со всеми» в цепочке"),
("code_erasure","ro_erasure","erasure flags","флаги стирания"),("code_erasure","dec_corr","erasure-/loss-aware decoding (flags are useless to a plain matcher)","декодирование с учётом стирания/потерь (простому паросочетанию флаги бесполезны)"),("code_bosonic","enc_cat","biased inner qubit","смещённый внутренний кубит"),("code_bosonic","enc_gkp","GKP inner qubit","внутренний GKP-кубит"),
("code_fusion","g_fusion","fusion measurements","измерения слияния"),("code_fusion","src_resource","resource states","ресурсные состояния"),
("code_aft","cx_aod","transversal gates by transport","трансверсальные вентили через транспорт"),("code_aft","cx_qccd","transversal gates by ion shuttling (Quantinuum tesseract on ions)","трансверсальные вентили через перемещение ионов (тессеракт Quantinuum на ионах)"),("code_aft","dec_corr","correlated decoding","коррелированное декодирование"),
("code_magic","code_surface","host code","код-носитель"),("code_magic","code_color","host code","код-носитель"),
("dec_fpga","code_surface","matching/clustering on surface syndromes","паросочетание/кластеризация на синдромах поверхностного кода"),("dec_nn","code_surface","trained on surface-code syndromes","обучен на синдромах поверхностного кода"),
("dec_relaybp","code_qldpc","qLDPC syndromes","синдромы qLDPC"),("dec_corr","code_highrate","transversal circuits","трансверсальные схемы"),("dec_rl","dec_mwpm","decoder steering reweights the matching graph","управление декодером перевзвешивает граф паросочетаний"),
("dec_cryo","ct_sfq","cold digital logic","холодная цифровая логика"),("dec_cryo","ct_cryocmos","cold digital logic","холодная цифровая логика"),
("ic_mcm","fab_sc","chiplets, couplers","чиплеты, элементы связи"),("ic_cryolink","fab_sc","superconducting waveguide","сверхпроводниковый волновод"),
("ic_ionphoton","ion","ion–photon entanglement","запутанность ион–фотон"),("ic_ionphoton","ro_spd","photon detection","детекция фотонов"),
("ic_atomcavity","alkali","cavity-coupled atoms","атомы в резонаторе"),("ic_atomcavity","ae_atom","cavity-coupled atoms","атомы в резонаторе"),("ic_atomcavity","fab_optics","cavities","резонаторы"),
("ic_spinphoton","defect","spin–photon interface","спин-фотонный интерфейс"),("ic_spinphoton","ro_spd","photon detection","детекция фотонов"),
("ic_transducer","fab_pic","electro-optic / optomechanical chip","электрооптический / оптомеханический чип"),("ic_transducer","ro_spd","heralded entanglement through the transducer needs single-photon detection","запутанность с оповещением через преобразователь невозможна без детектора одиночных фотонов"),("ic_transducer","transmon","microwave qubit","СВЧ-кубит"),("ic_fibre","fab_pic","chip-to-fibre coupling","стыковка чип–волокно"),
("transmon","fab_sc","JJ lithography","литография JJ"),("fluxonium","fab_sc","JJ arrays","массивы JJ"),("cavity","fab_3d","machined cavities","механически обработанные резонаторы"),("fluxq","fab_sc","annealer fab","производство отжигателей"),
("ion","fab_trap","surface-electrode or 3D blade trap","планарная или 3D ловушка-лезвие"),("ion","fab_optics","lasers, vacuum","лазеры, вакуум"),("alkali","fab_optics","tweezers, vacuum","пинцеты, вакуум"),("ae_atom","fab_optics","tweezers, clock lasers","пинцеты, часовые лазеры"),
("photon","fab_pic","sources, waveguides","источники, волноводы"),("squeezed","fab_pic","squeezers","сжиматели"),("qd_spin","fab_cmos","300 mm dots","точки на 300 mm"),("donor","fab_stm","STM placement","размещение методом СТМ"),("defect","fab_diamond","host crystal","кристалл-матрица"),("majorana","fab_mbe","InAs–Pb stack","стек InAs–Pb"),
("g_rydanalog","alkali","Rydberg excitation of the atom","ридберговское возбуждение атома"),("g_rydanalog","ae_atom","Rydberg excitation of an alkaline-earth atom (Sr)","ридберговское возбуждение щёлочноземельного атома (Sr)"),("g_rydanalog","enc_gr","ground–Rydberg computational states","вычислительные состояния основное–ридберговское"),
("g_rydanalog","ct_laser","global Rydberg lasers","глобальные ридберговские лазеры"),("enc_gr","alkali","an atom with a Rydberg level","атом с ридберговским уровнем"),("enc_gr","ae_atom","an alkaline-earth(-like) atom with a Rydberg level","щёлочноземельный атом с ридберговским уровнем"),
("g_lointer","photon","single photons in the mesh","одиночные фотоны в сетке"),("g_lointer","squeezed","squeezed light in the mesh","сжатый свет в сетке"),("g_lointer","ct_eo","phase shifters and switches","фазовращатели и переключатели"),
("cx_reload","ct_laser","lattice and tweezer light","свет решётки и пинцетов"),("cx_reload","fab_optics","second MOT region, conveyor optics, vacuum","вторая область МОЛ, оптика конвейера, вакуум"),
("ct_ionaod","fab_optics","bulk optics above the trap","объёмная оптика над ловушкой"),("g_ms","ct_ionaod","laser fields delivered from free space","лазерные поля из свободного пространства"),
("ct_vio","fab_sc","through-substrate vias, coaxial pins, interposers","сквозные переходы, коаксиальные штыри, интерпозеры"),
("ro_reset","transmon","the qubit to be reset","сбрасываемый кубит"),("ro_reset","ro_disp","the readout resonator used as the loss channel","резонатор считывания как канал потерь"),
("ro_fluxro","fluxq","flux qubits latched by QFPs","потоковые кубиты, защёлкиваемые QFP"),("ro_fluxro","ro_disp","frequency-multiplexed microresonators read the latched flux at the chip edge","частотно-мультиплексированные микрорезонаторы считывают защёлкнутый поток на краю чипа"),("ro_fluxro","ct_fluxdac","on-chip shift registers and DACs","сдвиговые регистры и ЦАП на чипе"),
("ro_homodyne","squeezed","a field quadrature to measure","квадратура поля для измерения"),("ro_homodyne","ct_eo","local-oscillator phase control","управление фазой гетеродина"),

("ic_multidie","fab_sc","bump-bonded superconducting dies","сверхпроводниковые кристаллы со столбиковыми соединениями"),("ic_fanout","fab_cmos","a CMOS router die at cryogenic temperature","криогенный КМОП-кристалл маршрутизации"),
("ic_fanout","ct_cryocmos","cryogenic electronics behind the fan-out","криогенная электроника за разводкой"),
# --- added 27 Sep 2026 (the edge audit: undeclared dependencies; group members are one-of for their source — see GROUP)
("enc_hf","ion","hyperfine ground levels of the ion","сверхтонкие уровни основного состояния иона"),("enc_hf","alkali","hyperfine ground levels of the atom","сверхтонкие уровни основного состояния атома"),("enc_hf","ae_atom","nuclear-spin ground levels (¹⁷¹Yb, ⁸⁷Sr)","ядерно-спиновые уровни основного состояния (¹⁷¹Yb, ⁸⁷Sr)"),
("enc_spin_ld","qd_spin","a single electron spin in a dot","одиночный электронный спин в точке"),("enc_spin_ld","donor","the donor's electron or nuclear spin","электронный или ядерный спин донора"),("enc_spin_ld","defect","the defect's electron or nuclear spin","электронный или ядерный спин дефекта"),
("enc_dualrail","cavity","two cavity modes, one excitation","две моды резонатора, одно возбуждение"),("enc_dualrail","transmon","two transmons, one excitation","два трансмона, одно возбуждение"),("enc_dualrail","photon","two optical modes, one photon","две оптические моды, один фотон"),
("dec_mwpm","code_surface","graph-like syndromes","графоподобные синдромы"),("dec_mwpm","code_bosonic","repetition-cat syndromes","синдромы repetition-cat"),("dec_mwpm","code_fusion","fusion-network syndrome graph","граф синдромов сети слияний"),("dec_mwpm","code_erasure","erasure-weighted matching","паросочетание с весами стираний"),
("cx_aod","alkali","atoms to move","перемещаемые атомы"),("cx_aod","ae_atom","atoms to move","перемещаемые атомы"),("cx_bus","ion","collective motional modes of the chain","коллективные колебательные моды цепочки"),
("g_anneal","fluxq","Ising Hamiltonian of coupled flux qubits","гамильтониан Изинга связанных потоковых кубитов"),("g_anneal","ct_fluxdac","h and J programmed by flux DACs","h и J программируются потоковыми ЦАП"),
("enc_eo","g_exch","all operations by exchange pulses","все операции — обменными импульсами"),("g_mbq","enc_parity","acts on the tetron parity qubit","действует на кубит чётности тетрона"),
("g_tc","ct_rt","flux pulses and microwave drive","потоковые импульсы и СВЧ-накачка"),("g_tc","ct_cryocmos","flux pulses and microwave drive","потоковые импульсы и СВЧ-накачка"),
("g_cr","ct_rt","microwave drive at the target qubit's frequency","СВЧ-накачка на частоте целевого кубита"),("g_cr","ct_cryocmos","microwave drive at the target qubit's frequency","СВЧ-накачка на частоте целевого кубита"),("g_bos","ct_rt","microwave pump tones","СВЧ-тоны накачки"),
("g_mwspin","qd_spin","ESR/EDSR single-spin rotations","ЭСР/ЭДСР-вращения одиночного спина"),("g_mwspin","donor","ESR/NMR rotations","ЭСР/ЯМР-вращения"),
("g_tc","fluxonium","fluxonium CZ via a transmon coupler","CZ на флаксониумах через трансмонный элемент связи"),("enc_bare","fluxonium","two lowest fluxonium levels","два нижних уровня флаксониума"),("ro_disp","fluxonium","dispersive shift of a fluxonium","дисперсионный сдвиг флаксониума"),
("code_surface","cx_aod","degree-4 checks by moving atoms","проверки степени 4 перемещением атомов"),
("code_color","cx_qccd","weight-6 checks by ion transport","проверки веса 6 транспортом ионов"),("code_color","cx_bus","all-to-all in the chain","«все со всеми» в цепочке"),("code_color","cx_aod","checks by moving atoms","проверки перемещением атомов"),
("dec_corr","code_aft","correlated decoding of transversal circuits","коррелированное декодирование трансверсальных схем"),("dec_corr","code_erasure","loss- and erasure-aware decoding","декодирование с учётом потерь и стираний"),("code_erasure","dec_mwpm","erasure-weighted matching","паросочетание с весами стираний"),
("ro_spd","squeezed","photon-number-resolving detection of squeezed light","детекция сжатого света с разрешением числа фотонов"),("g_exch","ct_cryocmos","exchange pulses from cryo-CMOS","обменные импульсы от крио-КМОП"),
("ct_laser","fab_optics","lasers, AOD/SLM, objectives","лазеры, АОД/SLM, объективы"),("cavity","fab_sc","planar or on-chip bosonic modes","планарные бозонные моды или моды на чипе"),
("photon","fab_mbe","quantum-dot single-photon sources","источники одиночных фотонов на квантовых точках"),("squeezed","fab_bulk","bulk-optics OPO squeezers","сжиматели на параметрических генераторах (объёмная оптика)"),
("code_qldpc","ic_spinphoton","non-local checks over spin–photon links between nodes","нелокальные проверки через спин-фотонные интерфейсы между узлами"),("code_qldpc","cx_shuttle","non-local checks by spin shuttling","нелокальные проверки через перемещение спинов"),("code_qldpc","cx_switch","non-local checks by photonic switching","нелокальные проверки через фотонную коммутацию"),
("enc_dualrail","ro_spd","photon loss heralded at detection","потеря фотона сопровождается оповещением при детекции"),("g_fusion","squeezed","fusion of GKP-encoded modes by beamsplitters and homodyne readout","слияние GKP-кодированных мод светоделителями и гомодинным считыванием"),
("ro_disp","fluxq","dispersive shift of a resonator by the latched flux state (via a QFP)","дисперсионный сдвиг резонатора защёлкнутым потоковым состоянием (через QFP)"),
("g_mwspin","ct_base","microwave and baseband pulses on the spin","СВЧ- и низкочастотные импульсы на спине"),("g_mwspin","ct_rt","microwave drive from room temperature","СВЧ-накачка с комнатной температуры"),
("g_mbq","ct_base","gate voltages that set the measurement","затворные напряжения, задающие измерение"),("g_catcnot","ct_rt","microwave drives of the cat modes","СВЧ-накачки мод кошачьих кубитов"),
("ct_eo","fab_bulk","fibre-coupled modulators and free-space optics","волоконные модуляторы и свободнопространственная оптика"),
]
# One-of groups (27 Sep 2026): a requires edge with a group is satisfied by any member of its (src, group) set; a group has >= 2
# members; a source may carry several groups (g_tc: carrier and control). Strength: hard = the source cannot exist without it,
# soft = the usual route (counts toward reach only where the architecture holds it, like a group member). Scope link = the need belongs
# to the link, not to the path's readout slot (the slot check exempts it).
GROUP={}
GROUP_LABEL={"carrier":("one carrier of several","один из носителей"),"encoding":("one encoding of several","одно из кодирований"),"control":("one control route of several","один из способов управления"),
 "connectivity":("one connectivity of several","одна из связностей"),"measurement":("one readout of several","одно из считываний"),"code":("one code of several","один из кодов"),
 "decoder":("one decoder of several","один из декодеров"),"fab":("one manufacturing route of several","один из способов изготовления")}   # how a one-of group reads in the tables (27 Sep 2026)
def _grp(src,name,*dsts):
    assert len(dsts)>=2,(src,name)
    for d in dsts: GROUP[(src,d)]=name
_grp("g_ryd","carrier","alkali","ae_atom"); _grp("g_rydanalog","carrier","alkali","ae_atom"); _grp("enc_gr","carrier","alkali","ae_atom"); _grp("enc_omg","carrier","ae_atom","ion"); _grp("enc_opt","carrier","ion","ae_atom")
_grp("enc_gkp","carrier","cavity","squeezed"); _grp("g_lointer","carrier","photon","squeezed"); _grp("g_ms","control","ct_ionlaser","ct_ionaod"); _grp("g_exch","carrier","qd_spin","donor"); _grp("g_exch","control","ct_base","ct_cryocmos")
_grp("ro_disp","carrier","transmon","cavity","fluxonium","fluxq"); _grp("ro_fluor","carrier","ion","defect"); _grp("ro_img","carrier","alkali","ae_atom"); _grp("ro_s2c","carrier","qd_spin","donor"); _grp("ro_erasure","encoding","enc_dualrail","enc_omg"); _grp("ro_spd","carrier","photon","squeezed"); _grp("enc_dualrail","measurement","ro_erasure","ro_spd"); _grp("g_fusion","carrier","photon","squeezed")
_grp("code_qldpc","connectivity","cx_lr","cx_qccd","cx_bus","cx_aod","cx_shuttle","cx_switch","ic_spinphoton"); _grp("code_highrate","connectivity","cx_aod","cx_qccd","cx_bus"); _grp("code_aft","connectivity","cx_aod","cx_qccd"); _grp("code_surface","connectivity","cx_nn","cx_aod"); _grp("code_color","connectivity","cx_nn","cx_qccd","cx_bus","cx_aod")
_grp("code_bosonic","encoding","enc_cat","enc_gkp"); _grp("code_magic","code","code_surface","code_color"); _grp("code_erasure","decoder","dec_corr","dec_mwpm"); _grp("dec_corr","code","code_highrate","code_aft","code_erasure"); _grp("dec_mwpm","code","code_surface","code_bosonic","code_fusion","code_erasure")
_grp("dec_cryo","control","ct_sfq","ct_cryocmos"); _grp("ic_atomcavity","carrier","alkali","ae_atom")
_grp("enc_hf","carrier","ion","alkali","ae_atom"); _grp("enc_spin_ld","carrier","qd_spin","donor","defect"); _grp("enc_dualrail","carrier","cavity","transmon","photon"); _grp("cx_aod","carrier","alkali","ae_atom")
_grp("g_tc","control","ct_rt","ct_cryocmos"); _grp("g_tc","carrier","transmon","fluxonium"); _grp("g_cr","control","ct_rt","ct_cryocmos"); _grp("g_mwspin","carrier","defect","qd_spin","donor"); _grp("enc_bare","carrier","transmon","fluxonium")
_grp("cavity","fab","fab_3d","fab_sc"); _grp("photon","fab","fab_pic","fab_mbe"); _grp("squeezed","fab","fab_pic","fab_bulk"); _grp("ct_eo","fab","fab_pic","fab_bulk"); _grp("g_mwspin","control","ct_base","ct_rt")
SOFT={("g_lointer","ct_eo"),("qd_spin","fab_cmos"),("g_bos","transmon"),("dec_fpga","code_surface"),("dec_nn","code_surface"),("donor","fab_stm"),("defect","fab_diamond"),("dec_rl","dec_mwpm"),
      ("dec_mwpm","code_surface"),("dec_mwpm","code_bosonic"),("dec_mwpm","code_fusion"),("dec_mwpm","code_erasure")}   # matching's positive need is usual, not absolute; its impossibilities are the colour-code and qLDPC conflicts
SCOPE_LINK={("ic_ionphoton","ro_spd"),("ic_spinphoton","ro_spd"),("ic_transducer","ro_spd"),("ic_transducer","fab_pic")}
_LAYER_OF={}
def _edge_kind(a,b):
    La,Lb=_LAYER_OF[a],_LAYER_OF[b]
    if La==Lb: return "same-layer"
    if Lb==10: return "fabrication"
    if Lb==1: return "carrier"
    if Lb==5: return "control"
    if La==6: return "readout"
    if Lb==6: return "measurement"
    if La==7 and Lb==4: return "connectivity"
    if {La,Lb}=={7,8}: return "decoder-code"
    if Lb==2: return "encoding"
    return "built-from"
EDGE_KIND={"carrier":("acts on the carrier","действует на носитель"),"fabrication":("fabrication route","маршрут изготовления"),"control":("signal delivery","подача сигналов"),"readout":("readout apparatus","система считывания"),
 "measurement":("measurement or heralding","измерение или оповещение"),"connectivity":("the code's connectivity need","связность, нужная коду"),"decoder-code":("decoder ↔ code","декодер ↔ код"),"encoding":("needs a particular encoding","нужно определённое кодирование"),
 "built-from":("built from other operations","строится из других операций"),"same-layer":("part of, or a refinement","часть или уточнение")}
for _n in NODES: _LAYER_OF[_n["id"]]=_n["layer"]
_seen=set()
for (a,b,en,ru) in REQ:
    assert (a,b) not in _seen,("duplicate requires edge",a,b); _seen.add((a,b))
for k in list(GROUP)+list(SOFT)+list(SCOPE_LINK): assert k in _seen,("group/soft/scope names a missing edge",k)
EDGES += [dict(type="requires",src=a,dst=b,en=en,ru=ru,any=((a,b) in GROUP),group=GROUP.get((a,b)),strength=("soft" if (a,b) in SOFT else "hard"),scope=("link" if (a,b) in SCOPE_LINK else "slot"),kind=_edge_kind(a,b)) for (a,b,en,ru) in REQ]
REP=[
("transmon","fluxonium","alternative superconducting carriers","альтернативные сверхпроводниковые носители"),("alkali","ae_atom","alternative atomic species","альтернативные виды атомов"),("photon","squeezed","DV vs CV photonics","фотоника дискретных vs непрерывных переменных"),("qd_spin","donor","dot vs donor spins","спины точек vs доноров"),
("enc_bare","enc_dualrail","bare vs erasure encoding","голое кодирование vs кодирование со стираниями"),("enc_bare","enc_cat","bare vs cat","голое vs кошачий кубит"),("enc_cat","enc_gkp","cat vs GKP","кошачий кубит vs GKP"),("enc_hf","enc_omg","ground vs metastable manifold","основное vs метастабильное многообразие"),("enc_hf","enc_opt","hyperfine ground levels vs optical S–D qubit","сверхтонкие уровни основного состояния vs оптический S–D кубит"),("enc_eo","enc_spin_ld","encoded vs bare spin","кодированный vs голый спин"),
("g_tc","g_cr","tunable vs fixed-frequency","перестраиваемый vs фиксированная частота"),("g_ms","g_elec","laser vs electronic gates","лазерные vs электронные вентили"),("g_fusion","g_cv","DV fusion vs CV Gaussian","слияние на дискретных vs гауссовы вентили на непрерывных переменных"),("g_bos","g_catcnot","ancilla-mediated vs direct cat CNOT","через анциллу vs прямой CNOT кошачьих кубитов"),
("cx_nn","cx_lr","NN vs long-range couplers","ближайшие соседи vs дальние элементы связи"),("cx_qccd","cx_bus","shuttling vs chain bus","перемещение vs шина цепочки"),("cx_nn","cx_shuttle","static vs shuttled spins","статические vs переносимые спины"),("cx_nn","cx_crossbar","individual vs shared lines","индивидуальные vs общие линии"),
("ct_rt","ct_cryocmos","RT vs 4 K control","комнатное vs 4 K управление"),("ct_rt","ct_sfq","RT vs mK SFQ","комнатное vs БОК при mK"),("ct_cryocmos","ct_sfq","cryo-CMOS vs SFQ","cryo-CMOS vs SFQ"),("ct_rt","ct_fluxdac","RT lines vs on-chip DACs","комнатные линии vs ЦАП на чипе"),("ct_laser","ct_pic_trap","free-space vs PIC optics","свободное пространство vs оптика на ФИС"),("ct_ionlaser","ct_ionmw","laser vs microwave ion control","лазерное vs СВЧ управление ионами"),
("ro_img","ro_imgfast","ms vs µs imaging","регистрация флуоресценции за ms vs за µs"),
("code_surface","code_color","surface vs colour","surface vs colour"),("code_surface","code_qldpc","local (surface) vs non-local constant-rate qLDPC — alternatives for the same slot, combinable hierarchically (surface/LPU processing + gross memory)","локальный (поверхностный) vs нелокальный qLDPC постоянной скорости — альтернативы для того же слота, совместимы иерархически (обработка в поверхностном коде/LPU + gross-память)"),("code_qldpc","code_highrate","non-local BB memory (gross) vs high-rate transversal blocks ([[16,6,4]] tesseract, [[16,4,2,4]])","нелокальная BB-память (gross) vs высокоскоростные трансверсальные блоки ([[16,6,4]] тессеракт, [[16,4,2,4]])"),("code_surface","code_highrate","2D vs high-rate transversal","2D vs высокоскоростные трансверсальные"),("code_surface","code_erasure","Pauli vs erasure-adapted","паулиевский vs адаптированный к стираниям"),("code_fusion","code_bosonic","DV fusion FT vs GKP concatenation","отказоустойчивость на основе слияний vs каскадирование GKP"),
("dec_mwpm","dec_nn","matching vs neural","паросочетание vs нейросетевой"),("dec_mwpm","dec_relaybp","matching vs BP","matching vs BP"),("dec_fpga","dec_gpu","FPGA vs GPU","FPGA vs GPU"),("dec_fpga","dec_cryo","RT FPGA vs cryo decoder","ПЛИС при комн. т. vs крио-декодер"),
("ic_mcm","ic_cryolink","same-fridge vs inter-fridge","один криостат vs между криостатами"),("ic_cryolink","ic_transducer","microwave link vs optical link","СВЧ-канал связи vs оптический канал связи"),
("fab_sc","fab_3d","planar vs 3D","планарное vs 3D"),("fab_cmos","fab_stm","foundry vs STM","фабрика vs СТМ"),("fab_trap","fab_cmos","MEMS vs standard CMOS fab for traps","МЭМС vs стандартная КМОП-фабрика для ловушек"),
("enc_hf","enc_gr","hyperfine vs ground–Rydberg encoding","сверхтонкое vs основное–ридберговское кодирование"),("g_ryd","g_rydanalog","gate vs analog Rydberg operation","вентильная vs аналоговая ридберговская работа"),
("g_fusion","g_lointer","fusion vs sampling interferometer","слияние vs интерферометр сэмплирования"),("cx_aod","cx_reload","one-shot loading vs continuous reload","однократная загрузка vs непрерывная дозагрузка"),
("ct_ionlaser","ct_ionaod","integrated vs free-space laser delivery","встроенная vs свободнопространственная доставка света"),("ct_ionmw","ct_ionaod","electronic vs free-space laser addressing","электронная vs свободнопространственная лазерная адресация"),
("ct_rt","ct_vio","edge-routed vs vertical signal delivery","краевая vs вертикальная разводка сигналов"),
("ro_spd","ro_homodyne","photon counting vs homodyne detection","счёт фотонов vs гомодинное детектирование"),("code_surface","code_detect","correcting vs detecting code","корректирующий vs обнаруживающий код"),
("code_surface","code_mitig","a code vs error mitigation","код vs смягчение ошибок"),("ic_mcm","ic_multidie","module-to-module vs die-to-die","модуль–модуль vs кристалл–кристалл"),
("ic_mcm","ic_fanout","coupled modules vs signal fan-out","связанные модули vs разводка сигналов"),("fab_pic","fab_bulk","photonic foundry vs bulk-optics assembly","фотонная фабрика vs сборка из объёмной оптики"),
]
EDGES += [E("replaces",a,b,en,ru) for (a,b,en,ru) in REP]
CON=[
("code_highrate","cx_nn","needs all-to-all connectivity","нужна связность «все со всеми»"),
("code_qldpc","cx_nn","needs degree ≥ 6; heavy-hex insufficient without c-couplers","нужна степень ≥ 6; решётки heavy-hex недостаточно без c-couplers"),
("code_aft","cx_nn","transversal permutations need transport","трансверсальные перестановки требуют транспорта"),
("enc_cat","code_surface","unbiased code wastes the bias — needs repetition/XZZX/elevator codes","несмещённый код теряет смещение — нужны коды с повторением/XZZX/elevator"),
("enc_dualrail","code_surface","a surface code decoded without its erasure flags wastes the encoding — the flags must reach an erasure-aware decoder","поверхностный код, декодируемый без флагов стирания, обесценивает кодирование — флаги должны доходить до декодера, учитывающего стирания"),
("ro_spd","code_surface","destructive detection precludes repeated syndrome extraction on the same photon","разрушающая детекция исключает повторное извлечение синдрома с того же фотона"),
("g_ms","cx_bus","gate time grows with chain length (median 672 µs on Forte's 30-ion chain)","время вентиля растёт с длиной цепочки (медиана 672 µs на 30-ионной цепочке Forte)"),
("fab_3d","cx_nn","cm-scale cavities cannot tile dense 2D lattices","сантиметровые резонаторы не укладываются в плотные 2D-решётки"),
("cx_crossbar","g_exch","shared lines vs per-pair exchange calibration","общие линии vs попарная калибровка обмена"),
("ct_sfq","transmon","SFQ switching photons cause quasiparticle poisoning unless shielded (0.96% error source in 2023 MCM)","фотоны переключений БОК-схем вызывают отравление квазичастицами без экранирования (0.96% — источник ошибки в многокристальном модуле 2023 г.)"),
("code_color","dec_mwpm","colour-code syndromes contain three-body (hyperedge) events that pairwise matching cannot decode","синдромы цветового кода содержат трёхчастичные (гиперрёберные) события, которые попарное паросочетание не декодирует"),
("dec_gpu","transmon","GPU decoding over NVQLink adds a ~4 µs round trip to a ~1 µs surface-code cycle","GPU-декодирование через NVQLink добавляет ~4 µs кругового пути к циклу поверхностного кода ~1 µs"),
("cx_reload","alkali","scattered cooling and MOT light reaching stored qubits","рассеянный свет охлаждения и МОЛ доходит до хранимых кубитов"),
("cx_reload","ae_atom","MOT light and repumper depleting stored atoms","свет МОЛ и репампера опустошает хранимые атомы"),
# --- added 27 Sep 2026 (the edge audit: incompatibilities with a physical mechanism, each with its price, mitigation, status and source)
("code_qldpc","dec_mwpm","one fault of a bivariate bicycle code flips three checks (hyperedges); pairwise matching cannot decode it","один сбой в bivariate bicycle-коде переворачивает три проверки (гиперрёбра); попарное паросочетание его не декодирует"),
("g_cr","code_surface","collision-free fixed frequencies force a sparse heavy-hex lattice; the degree-4 surface code then needs flag qubits and longer rounds","бесстолкновительные фиксированные частоты вынуждают разреженную решётку heavy-hex; поверхностный код степени 4 тогда требует флаговых кубитов и более длинных раундов"),
("ro_img","enc_hf","same-species imaging light scattered and re-absorbed dephases the hyperfine data atoms","рассеянный и переизлучённый свет регистрации флуоресценции атомов того же вида дефазирует сверхтонкие кубиты данных"),
("ro_fluor","enc_hf","fluorescence-detection light reaches spectator ions during mid-circuit readout","свет флуоресцентной детекции доходит до соседних ионов при считывании в середине схемы"),
("ic_transducer","transmon","the transducer's optical pump at the millikelvin stage creates quasiparticles and heats the qubit chip","оптическая накачка преобразователя на милликельвиновой ступени рождает квазичастицы и греет чип кубитов"),
("ct_cryocmos","transmon","milliwatt-class CMOS dissipation at the mixing chamber against a cooling budget of tens of microwatts","милливаттное тепловыделение КМОП на камере смешения против бюджета охлаждения в десятки микроватт"),
("ct_sfq","fluxonium","switching photons above 2Δ break Cooper pairs in the junction film — the transmon mechanism, not yet measured on a fluxonium","фотоны переключений выше 2Δ разрывают куперовские пары в плёнке перехода — механизм трансмона, на флаксониуме ещё не измерен"),
("squeezed","cx_switch","loss adds vacuum noise: after a fraction 1−η of loss no more than −10·log₁₀(1−η) dB of squeezing survives, so the ~10 dB GKP needs put the switch's loss budget below 10 %","потери добавляют вакуумный шум: после доли потерь 1−η выживает не больше −10·log₁₀(1−η) дБ сжатия, поэтому ~10 dB, нужные GKP, ограничивают потери переключателя 10 %"),
]
EDGES += [E("conflicts",a,b,en,ru) for (a,b,en,ru) in CON]
# Conflict semantics: "conflicts" = the two technologies work together only with a mitigating element or a change of
# a third layer; every conflict edge carries the mechanism (en/ru above), the measured price, the mitigation, a status and a source.
# status: open = no demonstrated mitigation at scale · mitigated = mitigation demonstrated at small scale · bypass = resolved by choosing another node in a third layer
CONX={
("cx_reload","alkali"):dict(
  price=("a separate MOT region 0.5 m away with conveyor transport, or a reservoir a few hundred µm away with molasses stopping","отдельная область МОЛ в 0.5 m с конвейерным транспортом или резервуар в нескольких сотнях µm с остановкой молассой"),
  mitig=("dynamical decoupling of the stored qubits; spatial separation","динамическая развязка хранимых кубитов; пространственное разделение"),
  status="mitigated",date="2025-09",url="https://www.nature.com/articles/s41586-025-09596-6"),
("cx_reload","ae_atom"):dict(
  price=("the MOT run without the repumper; stored atoms shelved in ³P₀ (13 s lifetime)","МОЛ без репампера; хранимые атомы укрыты в ³P₀ (время жизни 13 s)"),
  mitig=("shelving; separation","укрытие; разделение"),
  status="mitigated",date="2024-02",url="https://arxiv.org/abs/2402.04994"),
("code_qldpc","dec_mwpm"):dict(
  price=("no matching decoder has run a bivariate bicycle code: the syndrome graph has hyperedges, so the decoders that run it are BP+OSD (offline) and Relay-BP (real-time, FPGA)","ни один декодер на основе паросочетаний не запускал bivariate bicycle-код: в графе синдромов есть гиперрёбра, поэтому его декодируют BP+OSD (офлайн) и Relay-BP (реальное время, ПЛИС)"),
  mitig=("Relay-BP (dec_relaybp) or BP+OSD; matching stays for the surface-like codes","Relay-BP (dec_relaybp) или BP+OSD; паросочетание остаётся для кодов, подобных поверхностному"),
  status="bypass",date="2025-06",url="https://arxiv.org/abs/2506.01779"),
("g_cr","code_surface"):dict(
  price=("a cross-resonance lattice avoids frequency collisions by keeping the degree at 2–3 (heavy-hex); the surface code's weight-4 checks then need flag qubits, a longer syndrome circuit and a lower threshold than on a degree-4 lattice","решётка с кросс-резонансными вентилями избегает частотных столкновений, держа степень 2–3 (heavy-hex); проверки веса 4 поверхностного кода тогда требуют флаговых кубитов, более длинной схемы синдрома и дают порог ниже, чем на решётке степени 4"),
  mitig=("tunable couplers (g_tc) — IBM's move from Eagle's cross-resonance to Heron's tunable couplers, still on heavy-hex; the degree-4 square lattice came with Nighthawk (2025); or heavy-hex codes on the cross-resonance lattice","перестраиваемые элементы связи (g_tc) — переход IBM от кросс-резонанса у Eagle к перестраиваемым элементам связи Heron, ещё на heavy-hex; квадратная решётка степени 4 пришла с Nighthawk (2025); либо heavy-hex-коды на решётке с кросс-резонансом"),
  status="bypass",date="2020-01",url="https://arxiv.org/abs/1907.09528"),
("ro_img","enc_hf"):dict(
  price=("a mid-circuit image of one atom scatters resonant light that the stored hyperfine qubits absorb; without separation or shelving the data qubits decohere during every measurement","внутрисхемная регистрация флуоресценции одного атома рассеивает резонансный свет, который поглощают хранимые сверхтонкие кубиты; без разделения или укрытия кубиты данных декогерируют при каждом измерении"),
  mitig=("a separate readout zone reached by transport (cx_aod), a second species, or shelving the data qubits in metastable levels (enc_omg)","отдельная зона считывания через транспорт (cx_aod), второй вид атомов или укрытие кубитов данных в метастабильных уровнях (enc_omg)"),
  status="mitigated",date="2023-05",url="https://arxiv.org/abs/2305.19266"),
("ro_fluor","enc_hf"):dict(
  price=("detection light on one ion reaches its neighbours in the same chain; mid-circuit measurement of a hyperfine qubit therefore needs distance or a hidden manifold","свет детекции одного иона доходит до соседей в той же цепочке; считывание сверхтонкого кубита в середине схемы поэтому требует расстояния или скрытого многообразия"),
  mitig=("zoned QCCD traps that move the measured ion away (cx_qccd), a second species, or metastable shelving (enc_omg)","зонированные QCCD-ловушки, уносящие измеряемый ион (cx_qccd), второй вид ионов или укрытие в метастабильных уровнях (enc_omg)"),
  status="mitigated",date="2021-04",url="https://arxiv.org/abs/2003.01293"),
("ic_transducer","transmon"):dict(
  price=("the optical pump light that drives the conversion reaches the mixing chamber: its stray light breaks Cooper pairs and heats the stage, so the first qubit-to-photon transduction ran the pump pulsed at a low duty cycle","оптическая накачка, ведущая преобразование, стоит на камере смешения: её рассеянный свет разрывает куперовские пары и греет ступень, поэтому первая трансдукция кубит → фотон работала импульсной накачкой с малым коэффициентом заполнения"),
  mitig=("pulsed, low-duty-cycle pumping; the transducer on a separate chip or module with filtered optical access","импульсная накачка с малым коэффициентом заполнения; преобразователь на отдельном чипе или модуле с фильтрованным оптическим доступом"),
  status="open",date="2020-12",url="https://arxiv.org/abs/2004.04838"),
("ct_cryocmos","transmon"):dict(
  price=("a full CMOS controller dissipates milliwatts; the mixing chamber of a dilution refrigerator offers tens of microwatts, so the controller sits at 3–4 K (< 2 mW per channel set, 2019) and only microwatt-class parts — multiplexers, switches — go beside the transmons","полный КМОП-контроллер рассеивает милливатты; камера смешения растворительного криостата даёт десятки микроватт, поэтому контроллер стоит на ступени 3–4 K (< 2 mW на набор каналов, 2019), а рядом с трансмонами — только микроваттные части: мультиплексоры, переключатели"),
  mitig=("the controller at the 4 K stage with wiring down to the qubits; a millikelvin multiplexer that routes pulses without generating them; spin qubits operated at ~1 K do not see the conflict","контроллер на ступени 4 K с разводкой вниз к кубитам; милликельвиновый мультиплексор, который проводит импульсы, не порождая их; спиновые кубиты при ~1 K конфликта не видят"),
  status="mitigated",date="2019-11",url="https://arxiv.org/abs/1902.10864"),
("ct_sfq","fluxonium"):dict(
  price=("inferred from the transmon case: the same aluminium junctions, the same pair-breaking photons; no fluxonium driven by SFQ pulses has been reported, and a fluxonium biased at half flux is less sensitive to quasiparticle tunnelling than a transmon (Pop et al. 2014), so the price may be lower","выведено из случая трансмона: те же алюминиевые переходы, те же разрывающие пары фотоны; флаксониум, управляемый импульсами БОК, не сообщался, а флаксониум при половине кванта потока менее чувствителен к туннелированию квазичастиц, чем трансмон (Pop et al. 2014), так что цена может быть ниже"),
  mitig=("as for the transmon: the driver on a separate die, bandwidth limiting, quasiparticle traps, shielding","как для трансмона: драйвер на отдельном кристалле, ограничение полосы, ловушки квазичастиц, экранирование"),
  status="open",date="2023-09",url="https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310"),
("squeezed","cx_switch"):dict(
  price=("the fault-tolerance threshold of a GKP architecture is stated as ~10 dB of effective squeezing; a total loss of 1 dB on the route (η = 0.79) caps the reachable squeezing at 6.9 dB and 0.46 dB (η = 0.9) at 10 dB, so the switch budget is the tightest number of the architecture","порог отказоустойчивости архитектуры на GKP задан как ~10 dB эффективного сжатия; суммарные потери 1 dB на маршруте (η = 0,79) ограничивают достижимое сжатие 6,9 dB, а 0,46 dB (η = 0,9) — 10 dB, поэтому бюджет переключателя — самое жёсткое число архитектуры"),
  mitig=("loss budgets per mode and switch, the lowest-loss switch technologies (BTO, MEMS), or a discrete-variable encoding where loss is a heralded erasure","бюджет потерь на моду и переключатель, переключатели с наименьшими потерями (BTO, МЭМС) или кодирование на дискретных переменных, где потеря — стирание с оповещением"),
  status="open",date="2021-02",url="https://arxiv.org/abs/2010.02905"),
("code_highrate","cx_nn"):dict(
  price=("no nearest-neighbour device has run a high-rate code beyond the four-qubit [[4,2,2]] detection code; on a static lattice the non-local checks need SWAP networks whose depth grows with the check span, and errors accumulate with it","ни одно устройство со связностью ближайших соседей не запускало код высокой скорости крупнее четырёхкубитного кода обнаружения [[4,2,2]]; на статической решётке нелокальные проверки требуют SWAP-сетей, глубина которых растёт с размахом проверки, и ошибки накапливаются вместе с ней"),
  mitig=("long-range on-chip couplers (IBM c-couplers, Loon 2025-11) or physical transport (atoms, ions)","дальние элементы связи на чипе (IBM c-couplers, Loon 2025-11) или физический транспорт (атомы, ионы)"),
  status="open",date="2025-06",url="https://arxiv.org/abs/2506.03094"),
("code_qldpc","cx_nn"):dict(
  price=("bivariate bicycle codes need a degree-6 Tanner graph — two long-range connections per qubit — which heavy-hex (degree 2–3) cannot provide; without c-couplers no gross code runs","bivariate bicycle-коды требуют графа Таннера степени 6 — две дальние связи на кубит, — чего heavy-hex (степень 2–3) не даёт; без c-couplers gross-код не запускается"),
  mitig=("c-couplers (Loon), then Kookaburra module; measured coupler fidelity and length not yet published","c-couplers (Loon), затем модуль Kookaburra; измеренные точность и длина элемента связи пока не опубликованы"),
  status="open",date="2024-03",url="https://www.nature.com/articles/s41586-024-07107-7"),
("code_aft","cx_nn"):dict(
  price=("transversal gates between logical blocks need block-to-block qubit permutations; on a static lattice that is O(d) SWAP depth per logical gate, which erases the constant-depth advantage","трансверсальные вентили между логическими блоками требуют перестановок кубитов между блоками; на статической решётке это SWAP-глубина O(d) на логический вентиль, что уничтожает преимущество постоянной глубины"),
  mitig=("physical transport (AOD tweezers, ion shuttling) — the reason the architecture is atom/ion-native","физический транспорт (пинцеты на АОД, перемещение ионов) — поэтому архитектура естественна для атомов/ионов"),
  status="bypass",date="2025-09",url="https://www.nature.com/articles/s41586-025-09543-5"),
("enc_cat","code_surface"):dict(
  price=("a CSS surface code corrects X and Z symmetrically, so a bias > 25 (Ocelot, 2025) buys nothing; the ~10× qubit saving of cat architectures exists only with bias-tailored codes","CSS-поверхностный код исправляет X и Z симметрично, поэтому смещение > 25 (Ocelot, 2025) ничего не даёт; ~10-кратная экономия кубитов архитектур на кошачьих кубитах существует только с кодами под смещённый шум"),
  mitig=("repetition (Ocelot), XZZX, elevator or LDPC-cat codes instead of the plain surface code","коды с повторением (Ocelot), XZZX, elevator или LDPC-cat вместо обычного поверхностного кода"),
  status="bypass",date="2025-02",url="https://www.nature.com/articles/s41586-025-08642-7"),
("enc_dualrail","code_surface"):dict(
  price=("a matching decoder that ignores erasure flags sees a threshold of 0.937% instead of 4.15% — the erasure advantage is lost entirely","декодер паросочетания, игнорирующий флаги стирания, видит порог 0.937% вместо 4.15% — преимущество стирания теряется полностью"),
  mitig=("erasure-aware decoding (heralded-loss matching) — a decoder change, not a hardware change","декодирование с учётом стирания (паросочетание, учитывающее потери с оповещением) — замена декодера, не железа"),
  status="mitigated",date="2022-01",url="https://arxiv.org/abs/2201.03540"),
("ro_spd","code_surface"):dict(
  price=("a detected photon is gone: no repeated syndrome extraction on the same carrier, so a surface-code memory cycle cannot be run on flying qubits","обнаруженный фотон исчезает: повторное извлечение синдрома с того же носителя невозможно, поэтому цикл памяти поверхностного кода на летающих кубитах не запускается"),
  mitig=("fusion-based / measurement-based fault tolerance, where every photon is measured exactly once by design","отказоустойчивость на основе слияний / измерений, где каждый фотон по построению измеряется ровно один раз"),
  status="bypass",date="2023-02",url="https://www.nature.com/articles/s41467-023-36493-1"),
("g_ms","cx_bus"):dict(
  price=("spectral crowding of the motional modes makes the gate slower and less faithful as the chain grows: median 672 µs on Forte's 30-ion chain vs ~10–30 µs on short chains","спектральная теснота колебательных мод делает вентиль медленнее и менее точным с ростом цепочки: медиана 672 µs на 30-ионной цепочке Forte против ~10–30 µs на коротких цепочках"),
  mitig=("short chains in zoned QCCD traps (Quantinuum), amplitude/phase-modulated gates, or electronic gates on ≤ 4-ion segments","короткие цепочки в зонированных QCCD-ловушках (Quantinuum), амплитудно/фазово-модулированные вентили или электронные вентили на сегментах ≤ 4 ионов"),
  status="open",date="2025",url="https://www.ionq.com/quantum-systems/forte"),
("fab_3d","cx_nn"):dict(
  price=("cm-scale machined cavities give ~1 mode per cm²; a dense 2D lattice of them is impossible, so 3D bosonic qubits stop at a few tens of modes per module","сантиметровые фрезерованные резонаторы дают ~1 моду на cm²; плотная 2D-решётка из них невозможна, поэтому 3D-бозонные кубиты останавливаются на десятках мод на модуль"),
  mitig=("mm-scale coaxial λ/4 and double-post cavities, or planar bosonic modes; density still an order below transmon lattices","миллиметровые коаксиальные λ/4 и двухштыревые резонаторы или планарные бозонные моды; плотность всё ещё на порядок ниже решёток трансмонов"),
  status="open",date="2026-07",url="https://arxiv.org/abs/2607.06718"),
("cx_crossbar","g_exch"):dict(
  price=("one shared line drives many exchange gates at once, but J varies dot-to-dot with disorder; the 2024 16-dot crossbar showed no coherent qubit operation","одна общая линия управляет многими обменными вентилями сразу, но J меняется от точки к точке из-за беспорядка; 16-точечный кроссбар 2024 г. не показал когерентной работы кубитов"),
  mitig=("300 mm uniformity (~1% device-to-device), local floating-gate trims, or a semi-shared scheme with per-qubit correction lines","однородность 300 mm (~1% от прибора к прибору), локальные подстроечные плавающие затворы или полуобщая схема с корректирующими линиями на кубит"),
  status="open",date="2024-07",url="https://www.nature.com/articles/s41467-024-50355-4"),
("code_color","dec_mwpm"):dict(
  price=("weight-6 checks produce detection events that fire in triples; a plain matcher is not applicable, and the decoders that are (restriction, Möbius, Chromobius) lose accuracy — Google's d=5 colour memory reached 8.19(14)×10⁻³ per cycle with the search-based Tesseract decoder, worse than its d=5 surface code","проверки веса 6 дают события детекции тройками; плоское паросочетание неприменимо, а применимые декодеры (restriction, Möbius, Chromobius) теряют точность — память на цветовом коде d=5 у Google достигла 8.19(14)×10⁻³ за цикл с поисковым декодером Tesseract, хуже её же поверхностного кода d=5"),
  mitig=("hyperedge-capable decoders: Chromobius / restriction decoders, Tesseract (search), neural decoders; hook-free one-ancilla circuits (2026) reduce the hyperedge burden","декодеры с гиперрёбрами: Chromobius / restriction, Tesseract (поиск), нейросетевые; схемы без hook-ошибок с одной анциллой (2026) снижают нагрузку гиперрёбер"),
  status="mitigated",date="2026-07",url="https://www.nature.com/articles/s41586-026-10759-2"),
("dec_gpu","transmon"):dict(
  price=("NVQLink's measured round trip is 3.84 µs mean / 3.96 µs max, i.e. 3–4 surface-code cycles of a Willow-class transmon (~1.1 µs): syndromes queue faster than any single-cycle reaction, so real-time feed-forward (non-Clifford, teleportation) must wait","измеренный круговой путь NVQLink 3.84 µs в среднем / 3.96 µs максимум — 3–4 цикла поверхностного кода трансмона класса Willow (~1.1 µs): синдромы накапливаются быстрее любой реакции за один цикл, и обратная связь в реальном времени (не-Клиффорд, телепортация) вынуждена ждать"),
  mitig=("windowed / streaming decoding with an FPGA predecoder at the fridge, deferring only the reaction-critical decisions; slower carriers (atoms, ions: ms cycles) do not see the conflict","оконное / потоковое декодирование с ПЛИС-предекодером у криостата, откладывающее только критичные к реакции решения; медленные носители (атомы, ионы: циклы в ms) конфликта не видят"),
  status="open",date="2025-11",url="https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/"),
("ct_sfq","transmon"):dict(
  price=("photons emitted by switching junctions lie above the aluminium gap (2Δ ≈ 90 GHz) and break Cooper pairs in the qubit film: T1 decay plus correlated, non-Pauli bursts; 0.96(2)% of the 1.2(1)% error per Clifford in the 2023 multi-chip module","фотоны переключающихся переходов лежат выше щели алюминия (2Δ ≈ 90 GHz) и разрывают куперовские пары в плёнке кубита: распад T1 плюс коррелированные не-паулиевские всплески; 0.96(2)% из 1.2(1)% ошибки на Клиффорд в многочиповом модуле 2023 г."),
  mitig=("driver on a separate die, pulse-bandwidth limiting (projected 0.1%), quasiparticle traps / gap engineering, mm-wave shielding; SEEQC 2026 reports no detectable poisoning at 5 qubits (press, not independently measured)","драйвер на отдельном кристалле, ограничение полосы импульсов (прогноз 0.1%), ловушки квазичастиц / инженерия щели, mm-волновое экранирование; SEEQC 2026 сообщает об отсутствии детектируемого отравления на 5 кубитах"),
  status="open",date="2023-09",url="https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310"),
}
CONSTAT={"open":("open — no mitigation shown at scale","открыт — смягчение в масштабе не показано"),"mitigated":("mitigated at small scale","смягчён в малом масштабе"),"bypass":("bypassed by choosing another technology in place of one of the two","обходится выбором другой технологии вместо одной из двух")}
for e in EDGES:
    if e["type"]=="conflicts":
        x=CONX.get((e["src"],e["dst"]))
        if x: e.update(price=dict(en=x["price"][0],ru=x["price"][1]),mitig=dict(en=x["mitig"][0],ru=x["mitig"][1]),status=x["status"],date=x["date"],url=x["url"])
assert all(e.get("status") for e in EDGES if e["type"]=="conflicts"), "every conflict edge needs CONX detail"
# ---------------------------------------------------------------- DERIVATIONS (memberships, off-diagonal, empty slots, clock, validity)
import json, math, os
NODE={n["id"]:n for n in NODES}
# ---------------------------------------------------------------- STANDARD RECORDS (dated, sourced; nulls are honest "not published")
_REC_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)),"records.json")
RECORDS=json.load(open(_REC_PATH,encoding="utf-8"))
RECKEYS={"t1":("T1 relaxation","T1-релаксация"),"parity_life":("parity lifetime (single wire, not a qubit T1)","время жизни чётности (одна проволока, не T1 кубита)"),"t_bitflip":("bit-flip time (cat qubit, protected axis)","время переворота бита (кошачий кубит, защищённая ось)"),"t2":("T2 coherence (echo/DD)","когерентность T2 (эхо/DD)"),"t1q":("1Q gate time","время однокубитного вентиля"),
 "idle_err_round":("idle / memory error per round","ошибка простоя/памяти за раунд"),"leak_rate":("leakage per gate","утечка за вентиль"),"burst_rate":("correlated-burst rate","частота коррелированных всплесков"),
 "err_2q_parallel":("2Q error under full-width parallel operation","ошибка двухкубитного вентиля при параллельной работе всей ширины"),"crosstalk":("crosstalk","перекрёстные помехи"),
 "degree":("connectivity degree","степень связности"),"t_move_round":("transport per round","транспорт на раунд"),"t_move_layer":("transport per gate layer","транспорт на слой вентилей"),
 "t_ff":("feed-forward latency","задержка прямой связи"),"lines_per_qubit":("control lines per qubit","линий управления на кубит"),"calib_cadence":("recalibration interval","интервал перекалибровки"),
 "t_reset":("reset / initialisation time","время сброса/инициализации"),"reset_err":("reset error","ошибка сброса"),"spam":("SPAM error","ошибка SPAM"),"qnd":("QND fidelity / survival","точность неразрушающего измерения (QND) / выживание"),
 "d2_layers":("2Q layers per syndrome round","слоёв двухкубитных вентилей за раунд синдрома"),"d1_layers":("1Q layers per round","слоёв однокубитных вентилей за раунд"),"rate":("code rate k/n","скорость кода k/n"),"accept":("acceptance fraction","доля принятых"),
 "magic_rate":("magic states per round per factory","магических состояний за раунд на фабрику"),"magic_cost":("qubit·rounds per magic state","кубит·раундов на магическое состояние"),
 "t_decode":("decode latency per round","задержка декодирования за раунд"),"yield":("device yield","выход годных"),"spread":("parameter spread","разброс параметров"),
 "reload_flux":("initialised qubits delivered to the array per second, sustained","инициализированных кубитов в массив в секунду, устойчиво"),"t_trap":("trap lifetime of a stored atom, vacuum- or tweezer-limited","время жизни атома в ловушке, ограниченное вакуумом или пинцетом")}
for n in NODES: n["records"]=[]
for r in RECORDS:
    assert r["node"] in NODE, r["node"]; assert r["key"] in RECKEYS, r["key"]
    NODE[r["node"]]["records"].append({k:v for k,v in r.items() if k!="node"})
def rec(nid,key,prefer=("typical","best","theory"),unit=None):
    """first numeric record of a node by scope preference; None if unpublished"""
    rs=[r for r in NODE[nid]["records"] if r["key"]==key and r["num"] is not None and (unit is None or r["unit"]==unit)]
    for sc in prefer:
        for r in rs:
            if r["scope"]==sc: return r
    return rs[0] if rs else None
def _pow(x): return None if x is None else 10**x
LAYER_BY_ID={l[0]:l for l in LAYERS}
FAMILY_OF={p["id"]:p["family"] for p in PATHS}

OFFDIAG_RULES = {
 "NAT_MW":  ("natural carrier + microwave/electronic control","естественный носитель + СВЧ/электронное управление"),
 "FAB_FAR": ("fabricated carrier + far connectivity (transport / long-range)","искусственный носитель + дальняя связность (транспорт / дальние связи)"),
 "FAB_ERASURE": ("fabricated carrier + erasure error structure","искусственный носитель + структура ошибок со стираниями"),
 "FAB_COLD": ("fabricated carrier + control/decoding in the cold stage","искусственный носитель + управление/декодирование в холодной ступени"),
 "FAB_PHOTONIC": ("fabricated/solid-state carrier + photonic interconnect","искусственный/твердотельный носитель + фотонное межсоединение"),
 "NAT_FAST_GATE": ("natural carrier + sub-microsecond gate","естественный носитель + субмикросекундный вентиль"),
 "NAT_FAST_READ": ("natural carrier + ≤ 10 µs readout","естественный носитель + считывание ≤ 10 µs"),
 "NAT_FAB": ("natural carrier + semiconductor / photonic-chip fabrication","естественный носитель + полупроводниковое / фотонно-чиповое производство"),
}
def offdiag_flags(node, cls):
    L=node["layer"]; f=set()
    if cls=="nat":
        if node["e"]["mod"]=="mw" and L in (3,5): f.add("NAT_MW")
        if L==3 and node["b"]["t"] is not None and node["b"]["t"]<=-6.0: f.add("NAT_FAST_GATE")
        if L==6 and node["c"] and node["c"]["t"] is not None and node["c"]["t"]<=-4.5: f.add("NAT_FAST_READ")
        if node["g"] in ("cmos","pic") and L in (4,5,10): f.add("NAT_FAB")
    if cls in ("fab","int"):
        if node["d"] in ("transport","longrange") and L in (4,9): f.add("FAB_FAR")
        if "erasure" in node["f"] and L in (2,6,7): f.add("FAB_ERASURE")
        if any(p in ("4K","mK") for p in node["e"]["place"]) and L in (5,8): f.add("FAB_COLD")
        if node["d"]=="flying" and L==9: f.add("FAB_PHOTONIC")
    return f

def compute():
    # membership
    member={n["id"]:[] for n in NODES}
    for p in PATHS:
        for L,ids in p["slots"].items():
            for i,nid in enumerate(ids):
                assert nid in NODE, nid
                member[nid].append((p["id"],L,i==0))
    transfers=[]
    for n in NODES:
        paths=[m[0] for m in member[n["id"]]]
        fams=sorted(set(FAMILY_OF[p] for p in paths))
        n["paths"]=paths; n["families"]=fams
        n["transfer_degree"]=max(0,len(paths)-1); n["family_degree"]=max(0,len(fams)-1)
        for p in paths:
            if p!=paths[0]: transfers.append(dict(type="transfers",src=n["id"],dst=p,en="",ru=""))
    # off-diagonal
    offd=[]
    for n in NODES:
        flags=set(); ctx=set()
        for (pid,L,prim) in member[n["id"]]:
            cls=next(p["cls"] for p in PATHS if p["id"]==pid)
            fl=offdiag_flags(n,cls)
            if fl: flags|=fl; ctx.add(pid)
        n["offdiag"]=sorted(flags); n["offdiag_paths"]=sorted(ctx)
        if flags: offd.append(n["id"])
    # dependency reach: families whose paths contain a node that *requires* this node
    fam_of_node={n["id"]:set(n["families"]) for n in NODES}
    for n in NODES: n["reach"]=set()
    path_nodes={p["id"]:set(i for ids in p["slots"].values() for i in ids) for p in PATHS}
    for e in EDGES:
        if e["type"]=="requires":
            src=NODE[e["src"]]
            for pid in src["paths"]:
                if (e.get("any") or e.get("strength")=="soft") and e["dst"] not in path_nodes[pid]: continue   # a one-of or soft dependency counts only where realised
                NODE[e["dst"]]["reach"].add(FAMILY_OF[pid])
    for n in NODES:
        n["reach"]=sorted(n["reach"]|set(n["families"])); n["reach_degree"]=max(0,len(n["reach"])-1)
    # empty slots
    empty=[n["id"] for n in NODES if n["status"]=="X"]
    empty_slots=[]
    for p in PATHS:
        for L in range(1,11):
            ids=p["slots"].get(L,[])
            if not ids:
                if str(L) in p.get("na",{}): continue          # empty by design (NA_SLOTS), not a gap
                empty_slots.append(dict(path=p["id"],layer=L))
            elif all(NODE[i]["status"]=="X" for i in ids): empty_slots.append(dict(path=p["id"],layer=L,only=ids))
    # derived clock per path — syndrome round as the sum of its phases (not max):
    #   t_round = d2·(t_2Q + t_move_layer) + d1·t_1Q + t_meas + t_reset      (transport only where the connectivity node moves qubits)
    #   t_react = published measurement→conditioned-operation loop, floor = t_meas + t_decode
    #   ops_per_coh = T2 / t_2Q ; idle exposure per round = t_round / T2 (compared with the measured idle error where published)
    HOST_ROUND={"code_erasure":"code_surface"}   # erasure codes reuse the host code's round
    RESET_AMORTISED={"ro_img","ro_imgfast"}      # atom reload is a reservoir cycle, not a per-round reset
    for p in PATHS:
        def first(L):
            ids=p["slots"].get(L,[]); return NODE[ids[0]] if ids else None
        car=first(1); g=first(3); c=first(4); ct=first(5); r=first(6); dec=first(8)
        notes=[]; parts={}; link_round=False
        t2q=_pow(g["b"]["t"]) if g and g["b"]["t"] is not None else None
        tmeas=_pow(r["c"]["t"]) if r and r["c"] and r["c"]["t"] is not None else None
        # the round is that of the first code on the architecture that has a published syndrome circuit (erasure codes → host code)
        code=None; codeid=None; d2r=d1r=None
        codes=[NODE[i] for i in p["slots"].get(7,[])]
        for cd in codes:
            host=HOST_ROUND.get(cd["id"],cd["id"]); rr=rec(host,"d2_layers")
            if rr: code=cd; codeid=host; d2r=rr; d1r=rec(host,"d1_layers"); break
        if codes and not code: code=codes[0]; codeid=codes[0]["id"]; notes.append("no published syndrome round for %s"%", ".join(x["id"] for x in codes))
        elif code and code["id"]!=codes[0]["id"]: notes.append("round of %s (%s has no published syndrome circuit)"%(codeid,codes[0]["id"]))
        elif code and code["id"] in HOST_ROUND: notes.append("round of the host code (%s)"%codeid)
        if c and c["d"]=="flying": code=None; d2r=None; notes.append("measurement-driven photonic architecture: no syndrome round; native clock in the measured column")
        # a network-node architecture (27 Sep 2026): the code's non-local checks run over an inter-node link, so the round is set by
        # the link rate, not by the local gates — no derived round (the physicist's review of the defect page: 127 µs was four
        # orders of magnitude off the 0.02–1 Hz link)
        if code:
            pn=set(i for ids in p["slots"].values() for i in ids)
            conn=[e["dst"] for e in EDGES if e["type"]=="requires" and e["src"]==code["id"] and e.get("group")=="connectivity" and e["dst"] in pn]
            if conn and all(NODE[x]["layer"]==9 for x in conn):
                notes.append("network-node architecture: the code's checks run over the %s link, whose rate (see its records) sets the round — no derived round"%conn[0]); code=None; d2r=None; link_round=True
        t1qr=(rec(car["id"],"t1q",unit="s") if car else None) or (rec(g["id"],"t1q",unit="s") if g else None)
        tmove_r=rec(c["id"],"t_move_layer",unit="s") if c and c["d"]=="transport" else None
        if c and c["d"]=="transport" and not tmove_r: notes.append("transport per layer unpublished for %s"%c["id"])
        treset_r=rec(r["id"],"t_reset",unit="s") if r and r["id"] not in RESET_AMORTISED else None
        if r and r["id"] in RESET_AMORTISED: notes.append("reset by optical pumping (unpublished); reload amortised")
        elif r and not treset_r: notes.append("reset time unpublished for %s"%r["id"])
        if code and d2r and t2q is not None and tmeas is not None:
            d2=d2r["num"]; d1=d1r["num"] if d1r else 0
            parts={"gates":d2*t2q,"transport":(d2*tmove_r["num"] if tmove_r else 0.0),"1q":(d1*t1qr["num"] if t1qr and d1 else 0.0),"readout":tmeas,"reset":(treset_r["num"] if treset_r else 0.0)}
            # a term the path needs but no record publishes enters as 0 and is named in `missing`: the total is then a partial sum,
            # a lower bound the tables print as "≥" (Codex review, 26 Sep 2026: no silent zero substitution)
            missing=[]
            if c and c["d"]=="transport" and not tmove_r: missing.append("transport")
            if c and c["id"]=="cx_bus": missing.append("serial gates"); notes.append("on one chain the gates of a layer run largely one at a time: d₂ layers assume parallel gates, so the total is a lower bound")
            if d1 and not t1qr: missing.append("1q")
            if r and r["id"] not in RESET_AMORTISED and not treset_r: missing.append("reset")
            total=sum(parts.values()); lim=max(parts,key=parts.get)
            p["round"]=dict(total=total,parts=parts,limiter=lim,d2=d2,d1=d1,code=HOST_ROUND.get(codeid,codeid),missing=missing,
                            sources=[x for x in (d2r,d1r,t1qr,tmove_r,treset_r) if x],notes=notes)
        else:
            p["round"]=dict(total=None,parts={},limiter=None,notes=notes+([] if (code or link_round) else ["no code on this architecture"]))
        # reaction time
        tff=rec(ct["id"],"t_ff",unit="s") if ct else None; tdec=rec(dec["id"],"t_decode",unit="s") if dec else None
        floor=(tmeas or 0)+(tdec["num"] if tdec else 0) if (tmeas is not None and tdec) else None
        p["react"]=dict(loop=(tff["num"] if tff else None),floor=floor,sources=[x for x in (tff,tdec) if x],
                        note=("published measurement→conditioned-operation loop" if tff else "no published feed-forward loop; floor = readout + decode"))
        # coherence
        enc2=(p["slots"].get(2) or [None])[0]
        t2r=(rec(enc2,"t2",unit="s") if enc2 else None) or (rec(car["id"],"t2",unit="s") if car else None); t1r=rec(car["id"],"t1",unit="s") if car else None
        idle_meas=rec(car["id"],"idle_err_round") if car else None
        ops=(t2r["num"]/t2q) if (t2r and t2q) else None
        expo=(p["round"]["total"]/t2r["num"]) if (t2r and p["round"]["total"]) else None
        p["coh"]=dict(t1=(t1r["num"] if t1r else None),t2=(t2r["num"] if t2r else None),t2_scope=(t2r["scope"] if t2r else None),ops_per_coh=ops,idle_exposure=expo,idle_measured=(idle_meas["num"] if idle_meas else None),
                      sources=[x for x in (t1r,t2r,idle_meas) if x])
        # legacy fields kept for the map (log10 seconds)
        p["clock_derived"]=(math.log10(p["round"]["total"]) if p["round"]["total"] else None)
        p["clock_parts"]={k:(math.log10(v) if v else None) for k,v in parts.items()}
        p["clock_limiter"]=p["round"]["limiter"]
    # defines edges flattened
    defines=[dict(type="defines",src=n["id"],dst=d["out"],metric=d["metric"],value=d["value"],date=d["date"],url=d["url"]) for n in NODES for d in n["defines"]]
    return dict(layers=[dict(n=l[0],id=l[1],en=l[2],ru=l[3]) for l in LAYERS],vocab=dict(AFF={('%g'%k):v for k,v in AFF.items()},DET=DET,MECH=MECH,MOB=MOB,MOD=MOD,PLACE=PLACE,ERR=ERR,FAB=FAB,STATUS=STATUS,OUT=OUT,OFFDIAG=OFFDIAG_RULES,CONSTAT=CONSTAT,RECKEYS=RECKEYS,EDGE_KIND=EDGE_KIND,GROUP_LABEL=GROUP_LABEL),
                nodes=NODES,paths=PATHS,edges=EDGES+defines,empty_status=empty,empty_slots=empty_slots)

if __name__=="__main__":
    G=compute()
    import os; json.dump(G,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("nodes",len(G["nodes"]),"edges",{t:sum(1 for e in G["edges"] if e["type"]==t) for t in ("requires","replaces","conflicts","defines")})
    print("\nOFF-DIAGONAL:")
    for n in G["nodes"]:
        if n["offdiag"]: print(f"  {n['id']:16s} {','.join(n['offdiag']):32s} via {n['offdiag_paths']}")
    print("\nEMPTY status:",G["empty_status"]); print("EMPTY slots:",[(e['path'],e['layer'],e.get('only')) for e in G['empty_slots']])
    print("\nCLOCK:")
    for p in G["paths"]: print(f"  {p['id']:10s} round={p['round']['total']} limiter={p['round']['limiter']} parts={ {k:('%.3g'%v) for k,v in p['round']['parts'].items()} } measured={p['cycle']} | react loop={p['react']['loop']} floor={p['react']['floor']} | T2={p['coh']['t2']} ops/coh={p['coh']['ops_per_coh']} idle_exp={p['coh']['idle_exposure']} idle_meas={p['coh']['idle_measured']} | {p['round']['notes']}")
