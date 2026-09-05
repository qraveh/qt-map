# -*- coding: utf-8 -*-
"""Technology graph — single source of truth.
Nodes = technologies (not platforms). Layers 1..10. Seven coordinates (a..g).
Three spaces kept apart: design (coords), evaluation (dated attrs/defines), actors&goals (annotations).
"""
LAYERS = [
 (1,"carrier","Carrier","Носитель"),
 (2,"encoding","Encoding","Кодирование"),
 (3,"gate","Gate mechanism","Механизм гейта"),
 (4,"connect","Connectivity / transport","Связность / транспорт"),
 (5,"control","Control","Управление"),
 (6,"readout","Readout","Считывание"),
 (7,"code","Code","Код"),
 (8,"decoder","Decoder","Декодер"),
 (9,"interconnect","Interconnect","Интерконнект"),
 (10,"fab","Manufacturing","Производство"),
]
# coordinate vocabularies (design space) -----------------------------------------
AFF = {0.0:("natural","естественный"),0.25:("photon (natural particle, engineered modes)","фотон (естественная частица, изготовленные моды)"),
       0.5:("intermediate / carrier-agnostic","промежуточный / независим от носителя"),0.75:("hybrid (fabricated host)","гибридный (изготовленная матрица)"),1.0:("fabricated","изготовленный")}
DET = {"det":("deterministic","детерминированное"),"her":("probabilistic / heralded","вероятностное / heralded"),"na":("n/a","н/п")}
MECH = {"disp":("dispersive microwave","дисперсионное СВЧ"),"fluor":("fluorescence (PMT/SNSPD)","рассеяние фотонов (ФЭУ/SNSPD)"),"img":("fluorescence imaging (camera)","флуоресцентный imaging (камера)"),
        "s2c":("spin-to-charge + rf reflectometry","спин-в-заряд + rf-рефлектометрия"),"spd":("single-photon detection","детектирование одиночных фотонов"),"qcap":("rf quantum capacitance (parity)","rf квантовая ёмкость (чётность)"),
        "erasure":("ancilla erasure check","проверка erasure через анциллу"),"none":("—","—")}
MOB = {"static":("static NN wiring","статическая NN-разводка"),"longrange":("long-range static couplers","дальние статические связи"),"transport":("physical transport","физический транспорт"),
       "bus":("shared bus (motional / cavity)","общая шина (моды движения / резонатор)"),"flying":("flying qubits (photons)","летящие кубиты (фотоны)"),"shared":("shared-line crossbar","crossbar с общими линиями"),"none":("—","—")}
MOD = {"opt":("optical","оптическое"),"mw":("microwave","СВЧ"),"lf":("low-frequency electrical","низкочастотное электрическое"),"eo":("electro-optic","электрооптическое"),"none":("—","—")}
PLACE = {"RT":("room temperature","комнатная"),"4K":("4 K stage","ступень 4 K"),"mK":("millikelvin stage","милликельвиновая ступень"),"vac":("in-vacuum integrated","интегрировано в вакууме"),"none":("—","—")}
ERR = {"erasure":("erasure-convertible","erasure-конвертируемая"),"bias":("biased","смещённая"),"pauli":("stochastic Pauli","стохастическая паулиевская"),"coherent":("coherent / calibration","когерентная / калибровочная"),
       "leak":("leakage","утечка"),"burst":("correlated bursts","коррелированные всплески"),"loss":("loss (erasure)","потеря (erasure)"),"gauss":("Gaussian (small-shift)","гауссова (малые сдвиги)"),"unknown":("unknown / contested","неизвестна / оспаривается"),"none":("—","—")}
FAB = {"cmos":("CMOS foundry 300 mm","CMOS-фабрика 300 мм"),"sclitho":("superconducting lithography","сверхпроводящая литография"),"3d":("3D machined cavities","3D-обработка полостей"),"mems":("MEMS / surface-electrode traps","MEMS / поверхностные ловушки"),
       "pic":("photonic IC foundry","PIC-фабрика"),"optics":("optical / mechanical assembly","оптическая / механическая сборка"),"mbe":("III-V MBE heterostructures","III-V MBE гетероструктуры"),"stm":("STM hydrogen lithography","STM-литография"),"diamond":("diamond growth / implantation","рост / имплантация алмаза"),"none":("—","—")}
STATUS = {"D":("demonstrated","продемонстрировано"),"E":("emerging","формируется"),"T":("theory / design only","только теория / дизайн"),"X":("empty slot — no technology yet","пустой слот — технологии ещё нет")}
OUT = {"channel":("error channel","канал ошибок"),"clock":("clock (cycle time)","такт (время цикла)"),"count":("count with quality","счёт кубитов с качеством"),"path":("scaling path","путь масштабирования")}

def N(id,layer,en,ru,aff,cls,b_t,det,c,mob,mod,place,f,g,status,den,dru,defines=(),attrs_en="",attrs_ru=""):
    return dict(id=id,layer=layer,en=en,ru=ru,aff=aff,cls=cls,b=dict(t=b_t,det=det),c=c,d=mob,e=dict(mod=mod,place=place),f=f,g=g,status=status,
                desc=dict(en=den,ru=dru),defines=[dict(out=o,metric=m,value=v,date=d,url=u) for (o,m,v,d,u) in defines],attrs=dict(en=attrs_en,ru=attrs_ru))
def C(mech,t,destr,mid): return dict(mech=mech,t=t,destr=destr,mid=mid)

NODES=[]
# ---------------------------------------------------------------- L1 CARRIER
NODES += [
N("transmon",1,"Transmon","Трансмон",1.0,["fab"],-8.0,"det",C("disp",-6.5,False,True),"static","mw","RT",["leak","pauli","burst","coherent"],"sclitho","D",
  "Anharmonic LC oscillator; ~200–300 MHz anharmonicity bounds gates at ~10 ns; T1 ~70–100 µs.","Ангармонический LC-осциллятор; ангармонизм ~200–300 МГц ограничивает гейт снизу ~10 нс; T1 ~70–100 мкс.",
  [("channel","Willow mean T1 / 2Q error","68 µs / 0.33% CZ (QEC chip)","2024-12","https://www.nature.com/articles/s41586-024-08449-y"),
   ("channel","correlated burst rate","~1 per hour on 101-qubit Willow","2024-12","https://arxiv.org/abs/2408.13687")],
  "Willow 105 q; IBM Heron/Nighthawk 156/120 q; Zuchongzhi 3.x 105–107 q.","Willow 105 q; IBM Heron/Nighthawk 156/120 q; Zuchongzhi 3.x 105–107 q."),
N("fluxonium",1,"Fluxonium","Флаксониум",1.0,["fab"],-7.3,"det",C("disp",-6.5,False,True),"static","lf","RT",["pauli","coherent"],"sclitho","D",
  "Low-frequency (0.2–1 GHz) superconducting qubit with large anharmonicity; longer T1, flux-biased.","Низкочастотный (0.2–1 ГГц) сверхпроводниковый кубит с большим ангармонизмом; больший T1, смещение потоком.",
  [("channel","record 2Q (CNOT, Manucharyan group)","99.94% in 60 ns, > 99.9% over 24 days","2024-07","https://arxiv.org/abs/2407.15783"),
   ("channel","MIT FTF CZ (RL-optimised mean)","99.922%","2023-09","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.031035")],
  "Atlantic Quantum absorbed by Google (Oct 2025); D-Wave on-chip flux-DAC control on fluxonium (Jan 2026); D-Wave's DR17/DR49/DR181 are dual-rail cavity qubits, not fluxonium.","Atlantic Quantum поглощена Google (окт. 2025); D-Wave — on-chip flux-DAC управление флаксониумом (янв. 2026); DR17/DR49/DR181 у D-Wave — dual-rail полостные кубиты, а не флаксониум."),
N("cavity",1,"Bosonic cavity mode","Бозонная мода резонатора",1.0,["fab"],-6.5,"det",C("disp",-6.0,False,True),"bus","mw","RT",["loss","bias"],"3d","D",
  "Harmonic mode of a 3D/planar superconducting resonator; single-photon T1 10 ms (Al, Yale 2013), cavity-qubit T2 34 ms (Weizmann 2023); errors = photon loss (structured).","Гармоническая мода 3D/планарного сверхпроводящего резонатора; T1 фотона 10 мс (Al, Yale 2013), T2 полостного кубита 34 мс (Weizmann 2023); ошибки — потеря фотона (структурированная).",
  [("channel","cavity single-photon lifetime (Al, Yale)","10 ms","2013","https://arxiv.org/abs/1302.4408"),
   ("channel","cavity-qubit coherence (Weizmann)","T1 25.6 ms / T2 34 ms","2023-09","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030336")],
  "The 25.6 ms / 34 ms figures are Weizmann (Milul/Rosenblum, PRX Quantum 4, 030336), not a Yale-lineage result; the cavity material is not stated, so 'Nb-coated' is unsupported.","Значения 25.6 мс / 34 мс — Weizmann (Milul/Rosenblum, PRX Quantum 4, 030336), а не результат линии Yale; материал полости не указан, поэтому «покрытие Nb» не подтверждено."),
N("ion",1,"Trapped atomic ion","Ион в ловушке",0.0,["nat"],-4.2,"det",C("fluor",-5.0,False,True),"transport","opt","RT",["coherent","leak","pauli"],"mems","D",
  "Yb⁺/Ba⁺/Ca⁺ ions in RF traps; motional coupling (MHz) bounds gates at µs; hour-scale memory.","Ионы Yb⁺/Ba⁺/Ca⁺ в РЧ-ловушках; связь через моды движения (МГц) ограничивает гейт снизу микросекундами; память часового масштаба.",
  [("channel","Helios (98 q) 2Q / SPAM","7.9×10⁻⁴ / 4.8×10⁻⁴","2025-11","https://arxiv.org/abs/2511.05465"),
   ("channel","memory","> 1 hour single-qubit coherence","2021","https://arxiv.org/abs/2008.00251")],
  "Quantinuum Helios 98 q; IonQ Tempo 100 q chain.","Quantinuum Helios 98 q; IonQ Tempo — цепочка 100 q."),
N("alkali",1,"Alkali atom (Rb/Cs) in tweezer","Щелочной атом (Rb/Cs) в пинцете",0.0,["nat"],-6.6,"det",C("img",-3.3,False,True),"transport","opt","RT",["loss","leak","coherent"],"optics","D",
  "Hyperfine qubit; Rydberg interaction (MHz–GHz) allows sub-µs gates; T2 ~1–13 s; dominant error is atom loss.","Сверхтонкий кубит; ридберговское взаимодействие (МГц–ГГц) допускает суб-мкс гейты; T2 ~1–13 с; доминирующая ошибка — потеря атома.",
  [("count","atoms with coherence","6,100 Cs atoms, T2 12.6 s (Caltech)","2025-09","https://arxiv.org/abs/2403.12021"),
   ("count","continuous operation","> 3,000 qubits held > 2 h; 300,000 atoms/s reloaded into tweezers, 30,000 initialised qubits/s","2025-09","https://www.nature.com/articles/s41586-025-09596-6"),
   ("count","trapped (no gates)","11,022 Rb atoms in 18,225 metasurface tweezers","2026-06","https://arxiv.org/abs/2606.02715")],
  "Harvard/QuEra 448-atom FT processor; Gemini 260 q.","Процессор Harvard/QuEra на 448 атомах; Gemini 260 q."),
N("ae_atom",1,"Alkaline-earth atom (Yb/Sr) — erasure-native","Щёлочноземельный атом (Yb/Sr) — erasure-нативный",0.0,["nat"],-6.6,"det",C("img",-3.3,False,True),"transport","opt","RT",["erasure","loss"],"optics","D",
  "Nuclear-spin / clock-state qubits with metastable levels; decays are detectable → erasures (98% theory, 56% shown).","Кубиты на ядерном спине / часовых состояниях с метастабильными уровнями; распады детектируемы → erasure (98% теория, 56% показано).",
  [("channel","erasure conversion demonstrated","56% of 1Q errors → erasures (Yb-171)","2023-05","https://arxiv.org/abs/2305.05493"),
   ("channel","Yb CZ","99.72% post-selected / 99.40% raw","2024-11","https://arxiv.org/abs/2411.11708")],
  "Atom Computing (Yb), Princeton, Caltech (Sr), Pasqal (Rb→?)","Atom Computing (Yb), Princeton, Caltech (Sr)."),
N("photon",1,"Single photon (discrete variable)","Одиночный фотон (дискретные переменные)",0.25,["pho"],-7.0,"her",C("spd",-8.0,True,False),"flying","eo","RT",["loss"],"pic","D",
  "Heralded (SFWM) or quantum-dot photons; entangling is probabilistic (fusion); the error is loss = erasure.","Heralded (SFWM) или квантово-точечные фотоны; перепутывание вероятностное (fusion); ошибка — потеря = erasure.",
  [("channel","source purity / HOM (Omega)","99.5% / 99.5%","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","QD source system efficiency","71.2% (first above 2/3 loss threshold)","2023-11","https://arxiv.org/abs/2311.08347")],
  "", ""),
N("squeezed",1,"Squeezed light mode (CV)","Сжатая световая мода (CV)",0.25,["pho"],-6.0,"her",C("spd",-8.0,True,False),"flying","eo","RT",["gauss","loss"],"pic","D",
  "Continuous-variable modes for GKP/cluster states; needs ~10 dB *effective* squeezing for FT (0.62 dB on chip today); raw on-chip squeezing is a different quantity (1.4 dB measured on TFLN).","Моды непрерывных переменных для GKP/кластерных состояний; для FT нужно ~10 дБ *эффективного* сжатия (сегодня 0.62 дБ на чипе); сырое сжатие на чипе — другая величина (1.4 дБ измерено на TFLN).",
  [("channel","on-chip GKP effective squeezing (Xanadu)","0.62 dB vs ~9.75 dB required","2025-06","https://www.nature.com/articles/s41586-025-09044-5"),
   ("channel","on-chip raw squeezing (poled TFLN)","1.4 dB measured (> 10 dB loss-corrected)","2025-08","https://arxiv.org/abs/2508.08599")],
  "Xanadu's 0.62 dB is GKP *effective* squeezing, not raw quadrature squeezing — the two are not comparable. The readout coordinate is kept as single-photon detection, but CV practice is homodyne detection.","0.62 дБ у Xanadu — *эффективное* сжатие GKP, а не сырое квадратурное; величины несопоставимы. Координата считывания оставлена как детектирование одиночных фотонов, хотя практика CV — гомодинное детектирование."),
N("qd_spin",1,"Gate-defined quantum-dot spin (Si/SiGe, Si-MOS, Ge)","Спин в затворной квантовой точке (Si/SiGe, Si-MOS, Ge)",1.0,["fab"],-7.3,"det",C("s2c",-5.2,False,True),"static","lf","RT",["coherent","pauli","leak"],"cmos","D",
  "Electron/hole spin in a CMOS-fabricated dot; exchange (10–100 MHz) gives ns–100 ns gates; readout via charge sensor.","Спин электрона/дырки в CMOS-квантовой точке; обмен (10–100 МГц) даёт гейты нс–100 нс; считывание через зарядовый сенсор.",
  [("channel","2Q on 300 mm foundry wafer","99.04–99.56% (Diraq/imec)","2025-09","https://www.nature.com/articles/s41586-025-09531-9"),
   ("count","largest arrays","18 qubits (Groove/QuTech Ge; HRL EO)","2026-04","https://arxiv.org/abs/2604.01063")],
  "Intel, Diraq, Quantum Motion, HRL→IBM, QuTech, Quobly, Equal1.","Intel, Diraq, Quantum Motion, HRL→IBM, QuTech, Quobly, Equal1."),
N("donor",1,"Donor spin (P in ²⁸Si)","Донорный спин (P в ²⁸Si)",0.5,["int"],-6.0,"det",C("s2c",-5.0,False,True),"static","lf","RT",["pauli"],"stm","D",
  "STM-placed phosphorus atoms; nuclear qubits gated through a shared electron's hyperfine coupling; no foundry path.","Атомы фосфора, размещённые STM; ядерные кубиты управляются через сверхтонкую связь с общим электроном; нет фабричного пути.",
  [("channel","nuclear-spin gates (range reported)","99.5–99.99%; Bell > 99% (single 99.90(4)% CZ not isolable in the abstract)","2025-12","https://www.nature.com/articles/s41586-025-09827-w")],
  "SQC (Australia), founded 2017; the first deterministically placed single-donor device is UNSW/Simmons (2012). ²⁸Si feedstock from ASP Isotopes and DOE/ORNL.","SQC (Австралия), основана в 2017; первое устройство с детерминированно размещённым одиночным донором — UNSW/Simmons (2012). Сырьё ²⁸Si — ASP Isotopes и DOE/ORNL."),
N("defect",1,"Colour-centre / defect spin (NV, SiV, SnV, T)","Центр окраски / дефектный спин (NV, SiV, SnV, T)",0.5,["int"],-6.0,"det",C("fluor",-4.0,False,True),"flying","opt","RT",["pauli","loss"],"diamond","D",
  "Optically addressable spin in a solid host; network node with spin–photon interface rather than a processor qubit.","Оптически адресуемый спин в твердотельной матрице; узел сети со спин-фотонным интерфейсом, а не процессорный кубит.",
  [("channel","NV gate errors (GST)","< 0.1% [P] — press release only, no primary paper","2025-03","https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/")],
  "QuTech/Fujitsu, Harvard, Photonic Inc (T-centres), Quantum Brilliance. Element Six's DNV-B1 is an NV-*ensemble* sensing grade, not a single-defect node substrate.","QuTech/Fujitsu, Harvard, Photonic Inc (T-центры), Quantum Brilliance. DNV-B1 от Element Six — сенсорный сорт для *ансамблей* NV, а не подложка для узлов на одиночных дефектах."),
N("majorana",1,"Majorana parity (InAs–Pb tetron)","Майорановская чётность (тетрон InAs–Pb)",1.0,["fab"],-6.0,"det",C("qcap",-4.0,False,True),"static","lf","RT",["unknown"],"mbe","E",
  "Gate-defined nanowire device; only single-wire parity readout demonstrated; topological protection contested.","Затворная нанопроволока; продемонстрировано только считывание чётности одной проволоки; топологическая защита оспаривается.",
  [("channel","single-nanowire parity switching time","~20 s in one wire of one tetron (not a qubit lifetime), Z only; X loop 14.5 µs (2025)","2026-06","https://arxiv.org/abs/2606.03884")],
  "Microsoft; no two-qubit operation, no Bell test. DARPA US2QC: final Validation & Co-Design stage since 2025-02-06 (not QBI Stage B).","Microsoft; нет двухкубитной операции, нет теста Белла. DARPA US2QC: финальная стадия Validation & Co-Design с 2025-02-06 (не QBI Stage B)."),
N("fluxq",1,"rf-SQUID flux qubit (annealer)","rf-SQUID потоковый кубит (отжигатель)",1.0,["fab"],-8.5,"na",C("disp",-6.0,False,False),"longrange","lf","mK",["pauli","coherent"],"sclitho","D",
  "Analog-Hamiltonian carrier; 4,400+ qubits with 20-way Zephyr coupling; not a gate-model qubit.","Носитель аналогового гамильтониана; 4 400+ кубитов со связностью Zephyr 20; не гейтовый кубит.",
  [("count","Advantage2","4,400+ qubits, degree 20","2025-05","https://thequantuminsider.com/2025/05/20/d-wave-announces-general-availability-of-advantage2-quantum-computer/")],"D-Wave.","D-Wave."),
]
# ---------------------------------------------------------------- L2 ENCODING
NODES += [
N("enc_bare",2,"Bare two-level subspace","«Голое» двухуровневое подпространство",1.0,["fab"],None,"na",None,"none","none","none",["leak"],"none","D",
  "Computational subspace of an anharmonic oscillator; leakage to |2⟩ is the price.","Вычислительное подпространство ангармонического осциллятора; цена — утечка в |2⟩.",
  [("channel","leakage suppression","72× (all-microwave reset), residual 6.4×10⁻⁴ after 40 cycles","2025-12","https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31")],
  "USTC leakage suppression = PRL 135, 260601 (2025-12-22), Λ = 1.40(6) at d=7; the paper does not name the processor 'Zuchongzhi 3.2'.","Подавление утечки USTC — PRL 135, 260601 (2025-12-22), Λ = 1.40(6) при d=7; в статье процессор «Zuchongzhi 3.2» не назван."),
N("enc_hf",2,"Hyperfine / clock-state qubit","Сверхтонкий / часовой кубит",0.0,["nat"],None,"na",None,"none","none","none",["pauli","leak"],"none","D",
  "Ground-state hyperfine (or nuclear-spin) levels of atoms and ions; second-to-hour coherence.","Сверхтонкие (или ядерно-спиновые) уровни основного состояния атомов и ионов; когерентность от секунд до часов.",
  [("channel","leakage per 1Q Clifford (Helios)","1.1×10⁻⁵","2025-11","https://arxiv.org/abs/2511.05465")],"",""),
N("enc_omg",2,"Metastable ('omg') erasure encoding","Метастабильное («omg») erasure-кодирование",0.0,["nat"],None,"na",None,"none","none","none",["erasure"],"none","E",
  "Qubit in metastable manifold so that decay leaves the subspace detectably; ions (proposal) and Yb atoms (shown).","Кубит в метастабильном многообразии: распад выводит из подпространства детектируемо; ионы (предложение) и атомы Yb (показано).",
  [("channel","erasure fraction (theory)","98% of errors convertible (Yb-171)","2022-01","https://arxiv.org/abs/2201.03540"),
   ("channel","[[4,2,2]] with erasure info","logical decay 1.9(4)× slower (unconditional decoding)","2026-06","https://arxiv.org/abs/2506.13724")],
  "The 3.6(1)× often quoted is the post-selected hold; the architecturally relevant figure is the unconditional 1.9(4)× (arXiv:2506.13724 v1 and v2).","Часто цитируемое 3.6(1)× относится к постселектированному удержанию; архитектурно значимо безусловное 1.9(4)× (arXiv:2506.13724 v1 и v2)."),
N("enc_dualrail",2,"Dual-rail (erasure) encoding","Dual-rail (erasure) кодирование",0.25,["fab","pho"],None,"na",None,"none","none","none",["erasure"],"none","D",
  "One excitation in two modes/transmons/cavities; loss leaves the codespace → detected as erasure (80–90% of gate errors).","Одно возбуждение в двух модах/трансмонах/полостях; потеря выводит из кодового пространства → детектируется как erasure (80–90% ошибок гейта).",
  [("channel","cavity dual-rail CZ","erasure 0.53%/gate, residual Pauli < 0.1%, 500 ns","2026-08","https://www.nature.com/articles/s41586-026-10822-y"),
   ("channel","transmon dual-rail","erasure 2.5×10⁻²/check, residual 6×10⁻⁴, bias 42","2026-04","https://arxiv.org/abs/2604.16292")],
  "D-Wave/QCI (Aqumen), AWS, SUSTech (four transmons, not cavities); photonic dual-rail is native.","D-Wave/QCI (Aqumen), AWS, SUSTech (четыре трансмона, не полости); фотонный dual-rail нативен."),
N("enc_cat",2,"Cat-code encoding (biased noise)","Кошачье кодирование (смещённый шум)",1.0,["fab"],None,"na",None,"none","none","none",["bias"],"none","D",
  "Two-photon-dissipation-stabilised coherent states; bit-flips exponentially suppressed, phase-flips grow ∝ n̄.","Когерентные состояния, стабилизированные двухфотонной диссипацией; bit-flip подавлен экспоненциально, phase-flip растёт ∝ n̄.",
  [("channel","bit-flip time","44 min mean (12-cat chip, preliminary); 22 s squeezed cat","2025-09","https://alice-bob.com/newsroom/alice-bob-surpasses-bit-flip-stability-record"),
   ("channel","phase-flip per CX (Ocelot)","9.6(4)×10⁻² at n̄=2 (bit-flip 3.5(4)×10⁻³); bias > 25 under the gate, > 30 idle","2025-02","https://www.nature.com/articles/s41586-025-08642-7")],
  "Alice & Bob (DARPA QBI Stage A only), AWS. The '27–33' figures quoted elsewhere are phase-flip *times* in µs, not bias values.","Alice & Bob (DARPA QBI только Stage A), AWS. Числа «27–33», встречающиеся в других местах, — это *времена* phase-flip в мкс, а не значения bias."),
N("enc_gkp",2,"GKP grid encoding","GKP-кодирование (решётка)",0.75,["fab","pho"],None,"na",None,"none","none","none",["gauss"],"none","E",
  "Grid states in a bosonic (microwave cavity) or optical mode; corrects small shifts; needs ~10 dB squeezing.","Решёточные состояния в бозонной (СВЧ-полость) или оптической моде; исправляет малые сдвиги; нужно ~10 дБ сжатия.",
  [("channel","single-mode GKP logical error","8.1×10⁻³/round (survival 0.24×0.39)","2026-07","https://arxiv.org/abs/2607.06718"),
   ("channel","GKP qudit gain beyond break-even (UCSB + Google)","1.82–1.87","2025-05","https://www.nature.com/articles/s41586-025-08899-y"),
   ("channel","best bosonic memory gain (GKP, Yale)","2.27(7)","2023-03","https://www.nature.com/articles/s41586-023-05782-6")],
  "Nord Quantique (microwave), Xanadu (optical). The GKP-qudit work is Brock et al. (UC Santa Barbara + Google, Nature 641, 612), not Yale; Nord Quantique's magic-state SPAM is 8(5)×10⁻³ (7(7)×10⁻⁴ on cardinal states).","Nord Quantique (СВЧ), Xanadu (оптика). Работа по GKP-кудитам — Brock et al. (UC Santa Barbara + Google, Nature 641, 612), а не Yale; SPAM магических состояний у Nord Quantique — 8(5)×10⁻³ (7(7)×10⁻⁴ на кардинальных состояниях)."),
N("enc_eo",2,"Exchange-only / singlet-triplet spin encoding","Exchange-only / синглет-триплетное спиновое кодирование",1.0,["fab"],None,"na",None,"none","none","none",["leak","coherent"],"none","D",
  "Encoded spin qubits controlled purely by baseband exchange pulses; leakage 0.015%/Clifford (AEON).","Кодированные спиновые кубиты, управляемые только baseband-импульсами обмена; утечка 0.015%/Клиффорд (AEON).",
  [("channel","EO 1Q error (18 qubits)","2×10⁻⁴ mean","2026-07","https://arxiv.org/abs/2604.16216")],"HRL → IBM.","HRL → IBM."),
N("enc_timebin",2,"Time-bin / path photonic encoding","Time-bin / путевое фотонное кодирование",0.25,["pho"],None,"na",None,"none","none","none",["loss"],"none","D",
  "Photonic dual-rail in time or path; loss is the error and it is heralded.","Фотонный dual-rail во времени или пути; ошибка — потеря, и она heralded.",[],
  "Origin: Brendel, Gisin, Tittel and Zbinden, Phys. Rev. Lett. 82, 2594 (1999). No mobility of its own — the coordinate is 'none', inherited from the host carrier.","Происхождение: Brendel, Gisin, Tittel, Zbinden, Phys. Rev. Lett. 82, 2594 (1999). Собственной подвижности нет — координата «—», наследуется от носителя."),
N("enc_parity",2,"Fermion-parity encoding (tetron)","Кодирование в чётности фермионов (тетрон)",1.0,["fab"],None,"na",None,"none","none","none",["unknown"],"none","T",
  "Qubit in joint parity of two Majorana wires; X-measurement lifetime 1000× shorter than Z in 2025 data.","Кубит в совместной чётности двух майорановских проволок; время жизни X-измерения в 1000 раз короче Z (данные 2025).",
  [("channel","Z / X parity lifetimes","12.4 ms / 14.5 µs in the quoted tuning (~9.3 ms / ~4 µs in others; the ~10³ ratio is robust, the point values are not)","2025-07","https://arxiv.org/abs/2507.08795")],
  "The gap is attributed to the larger quasiparticle-capture cross-section of the two-wire X loop — flux noise is not the stated cause. DARPA US2QC: final Validation & Co-Design stage since 2025-02-06, not QBI Stage B.","Разрыв объясняется большим сечением захвата квазичастиц у двухпроволочной X-петли — потоковый шум как причина в статье не назван. DARPA US2QC: финальная стадия Validation & Co-Design с 2025-02-06, не QBI Stage B."),
]
# ---------------------------------------------------------------- L3 GATE MECHANISM
NODES += [
N("g_tc",3,"Tunable-coupler CZ / iSWAP","CZ / iSWAP через перестраиваемый coupler",1.0,["fab"],-7.4,"det",None,"static","mw","RT",["coherent","leak","pauli"],"sclitho","D",
  "Flux-tunable coupler switches ZZ/exchange on and off; 30–70 ns gates.","Перестраиваемый потоком coupler включает/выключает ZZ/обмен; гейты 30–70 нс.",
  [("channel","record CZ (tunable coupler, IQM)","99.93% over 40 h","2025-08","https://arxiv.org/abs/2508.16437"),
   ("channel","record CZ (double-transmon coupler)","99.90% in 48 ns","2024-11","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050"),
   ("clock","gate time (Willow)","~30 ns CZ","2024-12","https://www.nature.com/articles/s41586-024-08449-y"),
   ("channel","fleet EPLG (full width)","best 0.19% (ibm_boston), typical 0.37%","2026-07","https://www.ibm.com/quantum/blog/whats-new-q2-2026")],
  "The often-quoted Oxford '25 ns at 99.8%' is a fixed-coupling coaxmon pair with no tunable coupler and does not belong to this node.","Часто цитируемое оксфордское «25 нс при 99.8%» — пара coaxmon с фиксированной связью, без перестраиваемого coupler; к этому узлу не относится."),
N("g_cr",3,"Cross-resonance (fixed-frequency, all-microwave)","Cross-resonance (фиксированная частота, только СВЧ)",1.0,["fab"],-6.5,"det",None,"static","mw","RT",["coherent","pauli"],"sclitho","D",
  "Microwave-only entangling gate on fixed-frequency transmons; 180–500 ns; superseded by tunable couplers in IBM Heron.","Чисто СВЧ гейт на трансмонах фиксированной частоты; 180–500 нс; вытеснен перестраиваемыми couplers в IBM Heron.",
  [("channel","CR CNOT with intrinsic static-ZZ suppression (Kandala)","99.77(2)% in a single 180 ns pulse","2021","https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501")],
  "Kandala 2021 suppresses the static ZZ intrinsically (two fixed coupling elements retuning the dressed levels), not by an active cancellation drive; the pulse is 180 ns, not 320 ns. CR stayed IBM's native gate through Condor; Heron introduced the tunable-coupler CZ.","Kandala 2021 подавляет статический ZZ внутренне (два фиксированных элемента связи перестраивают одетые уровни), а не активным компенсирующим драйвом; импульс 180 нс, не 320 нс. CR оставался нативным гейтом IBM вплоть до Condor; CZ на перестраиваемом coupler появился в Heron."),
N("g_ryd",3,"Rydberg-blockade CZ","CZ через ридберговскую блокаду",0.0,["nat"],-6.6,"det",None,"transport","opt","RT",["loss","leak","coherent"],"optics","D",
  "Global Rydberg pulses entangle neighbouring atoms; 270 ns; fast for a natural carrier.","Глобальные ридберговские импульсы перепутывают соседние атомы; 270 нс; быстро для естественного носителя.",
  [("channel","record CZ","99.854% raw / 99.941% loss-post-selected","2026-04","https://arxiv.org/abs/2604.25987"),
   ("clock","gate time","270 ns","2025-06","https://arxiv.org/abs/2506.20661")],"",""),
N("g_ms",3,"Mølmer–Sørensen / light-shift laser gate","Гейт Мёльмера–Сёренсена / light-shift (лазерный)",0.0,["nat"],-4.2,"det",None,"bus","opt","RT",["coherent","leak","pauli"],"optics","D",
  "Laser-driven spin-motion coupling; 70 µs (Helios) to 550–880 µs (IonQ Forte chains); 1.6 µs record.","Лазерная связь спин–движение; 70 мкс (Helios) — 550–880 мкс (цепочки IonQ Forte); рекорд 1.6 мкс.",
  [("channel","Helios 2Q","7.9×10⁻⁴ in ~70 µs","2025-11","https://arxiv.org/abs/2511.05465"),
   ("clock","IonQ Forte MS duration (30-ion chain, all 435 pairs)","550–883 µs (median 672 µs)","2023-08","https://arxiv.org/abs/2308.05071"),
   ("clock","fastest laser gate (Schäfer et al., Oxford)","99.8% at 1.6 µs","2018","https://arxiv.org/abs/1709.06952")],
  "The 1.6 µs record is Schäfer et al. (Oxford, Nature 555, 2018), not Ballance. The Forte figure is one 30-ion chain benchmarked over all 435 pairs.","Рекорд 1.6 мкс — Schäfer et al. (Oxford, Nature 555, 2018), а не Ballance. Данные Forte — одна цепочка из 30 ионов, промерены все 435 пар."),
N("g_elec",3,"Electronic near-field microwave gate (ions, laser-free)","Электронный near-field СВЧ гейт (ионы, без лазера)",1.0,["nat"],-3.7,"det",None,"bus","mw","RT",["pauli","coherent"],"mems","D",
  "Chip currents create microwave gradients; no lasers for gates, no ground-state cooling; 120–226 µs.","Токи на чипе создают СВЧ-градиенты; без лазеров для гейтов, без охлаждения в основное состояние; 120–226 мкс.",
  [("channel","record 2Q","8.4×10⁻⁵ without ground-state cooling","2025-10","https://arxiv.org/abs/2510.17286"),
   ("clock","gate duration","225.8 µs (2025); ≈120 µs in 2024 (two 60 µs pulses, arXiv:2407.07694)","2025-10","https://arxiv.org/html/2510.17286")],"Oxford Ionics → IonQ.","Oxford Ionics → IonQ."),
N("g_exch",3,"Exchange gate (spins; incl. shuttled-spin CZ)","Обменный гейт (спины; вкл. CZ на переносимых спинах)",1.0,["fab"],-7.0,"det",None,"static","lf","RT",["coherent","pauli","leak"],"cmos","D",
  "Voltage-pulsed exchange J (10–90 MHz); 58–500 ns; ~80% of error is calibration/control (HRL).","Обмен J (10–90 МГц) под импульсами напряжения; 58–500 нс; ~80% ошибки — калибровка/управление (HRL).",
  [("channel","foundry CZ","99.04–99.56% (300 mm)","2025-09","https://www.nature.com/articles/s41586-025-09531-9"),
   ("channel","EO CNOT best / mean","9×10⁻⁴ / 3×10⁻³","2026-07","https://arxiv.org/abs/2604.16216"),
   ("clock","mobile-spin CZ","98.86% in 58 ns","2026-05","https://www.nature.com/articles/s41586-026-10423-9")],
  "Best exchange gate is HRL's exchange-only CNOT at 9×10⁻⁴; SQC's '99.90% donor nuclear CZ' is not isolable from its abstract, which gives a 99.5–99.99% range and Bell > 99%.","Лучший обменный гейт — exchange-only CNOT у HRL, 9×10⁻⁴; «99.90% ядерный CZ на донорах» у SQC не выделяется из аннотации, где дан диапазон 99.5–99.99% и Bell > 99%."),
N("g_fusion",3,"Linear-optical fusion (heralded)","Линейно-оптический fusion (heralded)",0.25,["pho"],-7.0,"her",None,"flying","eo","RT",["loss"],"pic","D",
  "Probabilistic Bell measurement on photons (50%, 75% boosted); failure is heralded → erasure.","Вероятностное измерение Белла на фотонах (50%, 75% с усилением); неудача heralded → erasure.",
  [("channel","fusion Bell fidelity","99.22%","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],"",""),
N("g_bos",3,"Ancilla-mediated bosonic gates (cat CX, dual-rail CZ, beam-splitter)","Бозонные гейты через анциллу (cat CX, dual-rail CZ, beam-splitter)",1.0,["fab"],-6.3,"det",None,"bus","mw","RT",["erasure","bias","pauli"],"3d","D",
  "Transmon ancilla, or a differentially driven DC-SQUID beam-splitter coupler between modes; ~500 ns.","Анцилла-трансмон либо beam-splitter-coupler на дифференциально управляемом DC-SQUID между модами; ~500 нс.",
  [("channel","dual-rail cavity CZ","post-selected infidelity 0.029% (bound 0.12%), 500 ns","2026-08","https://www.nature.com/articles/s41586-026-10822-y"),
   ("channel","cavity beam-splitter (DC-SQUID coupler)","> 99.98%, ~100 ns swaps","2023-03","https://arxiv.org/abs/2303.00959")],
  "The beam-splitter coupler of arXiv:2303.00959 is a differentially driven DC-SQUID, not a SNAIL. Quantum Circuits was never in DARPA QBI; Alice & Bob reached Stage A only.","Beam-splitter-coupler в arXiv:2303.00959 — дифференциально управляемый DC-SQUID, а не SNAIL. Quantum Circuits никогда не входила в DARPA QBI; Alice & Bob дошла только до Stage A."),
N("g_mbq",3,"Measurement-based Majorana gate","Майорановский гейт через измерения",1.0,["fab"],None,"det",None,"static","lf","RT",["unknown"],"mbe","X",
  "Braiding by sequences of parity measurements — nothing demonstrated; single-wire readout only.","Плетение последовательностями измерений чётности — ничего не продемонстрировано; только считывание одной проволоки.",
  [("channel","status","no two-qubit operation, no entanglement","2026-06","https://arxiv.org/abs/2606.03884")],"",""),
N("g_anneal",3,"Analog annealing evolution","Аналоговая эволюция (отжиг)",1.0,["fab"],-8.4,"na",None,"longrange","lf","mK",["coherent","pauli"],"sclitho","D",
  "Coherent quenches 3.6–27 ns on 1,222–5,627 qubits; not a gate.","Когерентные квенчи 3.6–27 нс на 1 222–5 627 кубитах; не гейт.",
  [("clock","coherent quench","3.6–27 ns","2025-03","https://arxiv.org/abs/2403.00910")],
  "Pasqal's 10,000 physical qubits slipped from 2026 to 2028 (100 logical in 2029); QuEra's Series B expansion closed 2025-09-09 (Google, SoftBank Vision Fund 2, NVentures); Quantinuum's magnetism result is Trotterised *digital* simulation, not analog evolution.","10 000 физических кубитов Pasqal сдвинуты с 2026 на 2028 (100 логических — 2029); расширение Series B у QuEra закрыто 2025-09-09 (Google, SoftBank Vision Fund 2, NVentures); результат Quantinuum по магнетизму — троттеризованная *цифровая* симуляция, а не аналоговая эволюция."),
]
# ---------------------------------------------------------------- L4 CONNECTIVITY / TRANSPORT
NODES += [
N("cx_nn",4,"Static nearest-neighbour lattice","Статическая решётка ближайших соседей",1.0,["fab"],None,"na",None,"static","none","none",["coherent"],"sclitho","D",
  "Heavy-hex (degree 2.3) or square lattice (degree 3.5–3.6) with on-chip couplers; ZZ crosstalk is the tax.","Heavy-hex (степень 2.3) или квадратная решётка (степень 3.5–3.6) с couplers на чипе; налог — ZZ-crosstalk.",
  [("count","Nighthawk","120 q, 218 couplers, 5,000 2Q gates/circuit","2025-11","https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance"),
   ("channel","CZ crosstalk (fitted budget term, Willow d=7)","5.5×10⁻⁴","2024-08","https://arxiv.org/abs/2408.13687")],
  "The 5.5×10⁻⁴ is a fitted component of the Willow error budget, not a directly measured crosstalk figure. EUV is a single point of failure for the spin branch only — no fielded transmon lattice uses it. Rigetti: median 2Q 99.5% at 36 q falls to 99.1% at 108 q (12 chiplets).","5.5×10⁻⁴ — подобранная компонента бюджета ошибок Willow, а не напрямую измеренный crosstalk. EUV — единая точка отказа только для спиновой ветви: ни одна работающая трансмонная решётка её не использует. Rigetti: медиана 2Q 99.5% при 36 q падает до 99.1% при 108 q (12 чиплетов)."),
N("cx_lr",4,"Long-range on-chip couplers (c-couplers, mm-scale)","Дальние couplers на чипе (c-couplers, мм-масштаб)",1.0,["fab"],None,"na",None,"longrange","none","none",["coherent"],"sclitho","E",
  "Resonator/coupler links beyond NN; enables degree-6 qLDPC layouts; 2 mm CZ 99.81% (IQM); IBM Loon components without numbers.","Резонаторные/coupler-связи дальше NN; открывает qLDPC-разводки степени 6; CZ на 2 мм 99.81% (IQM); компоненты IBM Loon без чисел.",
  [("path","long-range CZ","99.81% over ≥ 2 mm","2023","https://arxiv.org/abs/2208.09460"),
   ("path","IBM Loon","c-couplers + multilayer routing shown, no performance numbers","2025-11","https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance")],"",""),
N("cx_qccd",4,"Ion shuttling (QCCD, junctions, grid traps)","Транспорт ионов (QCCD, перекрёстки, решётчатые ловушки)",0.0,["nat"],-1.3,"na",None,"transport","none","none",["coherent"],"mems","D",
  "Ions moved between zones at m/s with sub-quantum heating; transport + cooling dominate runtime (55 ms per full layer on Helios).","Ионы перемещаются между зонами со скоростью м/с при нагреве меньше кванта; транспорт + охлаждение доминируют во времени (55 мс на полный слой Helios).",
  [("clock","time per full-width layer (Helios)","~55 ms","2025-11","https://arxiv.org/html/2511.05465v1"),
   ("path","junction transport","4 m/s, 0.013–0.03 quanta/round trip","2022","https://arxiv.org/abs/2206.11888"),
   ("path","grid-trap ion exchange","2.5 kHz","2024-03","https://arxiv.org/abs/2403.00756"),
   ("path","two-module matter link (Universal Quantum)","2,424 transfers/s, loss infidelity < 7×10⁻⁸","2023-02","https://www.nature.com/articles/s41467-022-35285-3")],
  "A chip-to-chip matter link between two ion-trap modules exists (Universal Quantum, Nat. Commun. 14, 531, 2023); the empty slot here is a link across more than two modules, not chip-to-chip itself.","Межчиповый материальный линк между двумя модулями ионных ловушек существует (Universal Quantum, Nat. Commun. 14, 531, 2023); пустой слот здесь — связь более чем двух модулей, а не сама стыковка чип-чип."),
N("cx_bus",4,"Ion-chain motional bus (all-to-all in chain)","Шина мод движения ионной цепочки (all-to-all в цепочке)",0.0,["nat"],-3.2,"na",None,"bus","none","none",["coherent"],"mems","D",
  "Shared motional modes give all-to-all within one chain; gates slow with chain length (median 672 µs on Forte's 30-ion chain).","Общие моды движения дают all-to-all внутри одной цепочки; гейты замедляются с её длиной (медиана 672 мкс на 30-ионной цепочке Forte).",
  [("count","independently benchmarked chain (Forte)","30 ions, all 435 pairs","2023-08","https://arxiv.org/abs/2308.05071"),
   ("count","largest claimed chain (Tempo)","100 ions, #AQ 64 [C] — a company claim, no per-pair data","2025-10","https://ionq.com/quantum-systems/tempo")],
  "IonQ Forte is a 30-ion chain (435 pairs), not 36; the 100-ion all-to-all Tempo chain is a company claim with no published gate time or per-pair fidelity.","IonQ Forte — цепочка из 30 ионов (435 пар), а не 36; 100-ионная цепочка Tempo с all-to-all — заявление компании без опубликованного времени гейта и попарных fidelity."),
N("cx_aod",4,"Atom transport by AOD tweezers (zoned architecture)","Транспорт атомов AOD-пинцетами (зонная архитектура)",0.0,["nat"],-3.0,"na",None,"transport","none","none",["loss"],"optics","D",
  "Coherence-preserving moves of 100s µm in 0.4–1.6 ms at ~99.95%; storage/entangling/readout zones.","Сохраняющие когерентность перемещения на сотни мкм за 0.4–1.6 мс при ~99.95%; зоны хранения/перепутывания/считывания.",
  [("clock","move time","610 µm in 1.6 ms at 99.95%; 270 µm in 400 µs at 99.8%","2025-09","https://arxiv.org/abs/2403.12021"),
   ("count","zoned FT processor","448 atoms, 256 in entangling zone","2025-11","https://www.nature.com/articles/s41586-025-09848-5")],
  "Harvard's continuously reloaded 3,000-atom system moves atoms ~0.5 m on optical-lattice conveyor belts, using AOD tweezers only for local rearrangement. TU/e's 3D acousto-optic lensing (arXiv:2510.09398) is a design study [S] with no atoms.","Непрерывно перезагружаемая система Harvard на 3 000 атомов перемещает атомы на ~0.5 м оптическими решёточными конвейерами, а AOD-пинцеты использует только для локальной перестановки. 3D acousto-optic lensing из TU/e (arXiv:2510.09398) — расчётная работа [S], без атомов."),
N("cx_shuttle",4,"Spin shuttling (conveyor mode)","Перенос спинов (конвейерный режим)",1.0,["fab"],-6.7,"na",None,"transport","none","none",["coherent"],"cmos","E",
  "Spins carried 10 µm in < 200 ns at 99.5%; gates between moving spins 98.86%; gives fabricated carriers transport connectivity.","Спины переносятся на 10 мкм за < 200 нс при 99.5%; гейты между движущимися спинами 98.86%; даёт изготовленным носителям транспортную связность.",
  [("path","conveyor shuttling","10 µm, 99.54%, up to 64 m/s","2025-06","https://www.nature.com/articles/s41565-025-01920-5"),
   ("path","weight-4 parity via shuttled ancilla","97.7% per shuttle","2026-07","https://www.nature.com/articles/s41586-026-10766-3")],"",""),
N("cx_switch",4,"Photonic switching / routing (EO, feed-forward)","Фотонная коммутация / маршрутизация (EO, feed-forward)",0.25,["pho"],-6.0,"na",None,"flying","eo","RT",["loss"],"pic","D",
  "Every switch costs loss: 0.19 dB/MZI at system scale (Aurora), 100 mdB for the best in-line element (PsiQuantum BTO); FT needs ~7 mdB.","Каждый переключатель стоит потерь: 0.19 дБ/MZI в масштабе системы (Aurora), 100 мдБ у лучшего элемента в линии (BTO у PsiQuantum); для FT нужно ~7 мдБ.",
  [("channel","best in-line switch (PsiQuantum BTO)","100 mdB insertion; 52(12) mdB fibre-to-chip","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","system-scale switch loss (Aurora)","0.19 dB/MZI; requirement ≈ 7 mdB","2025-01","https://www.nature.com/articles/s41586-024-08406-9"),
   ("channel","BTO phase shifter","0.33 dB·V","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "A '30 mdB' switch figure sometimes quoted is untraceable to any source. Omega's single-mode SiN loss is 1.8(2) dB/m against the 0.5 dB/m multimode figure — unreconciled.","Иногда цитируемые «30 мдБ» для переключателя не прослеживаются ни к одному источнику. Потери одномодового SiN в Omega — 1.8(2) дБ/м против многомодовых 0.5 дБ/м; расхождение не устранено."),
N("cx_crossbar",4,"Crossbar shared-line control (spins)","Crossbar с общими линиями (спины)",1.0,["fab"],None,"na",None,"shared","lf","RT",["coherent"],"cmos","E",
  "Shared plunger/barrier lines: 23 lines for 16 dots, T = 6√g − 1 scaling; no coherent qubit operation shown.","Общие plunger/barrier-линии: 23 линии на 16 точек, масштабирование T = 6√g − 1; когерентных операций с кубитами не показано.",
  [("path","control lines vs dots (no coherent qubit operation)","23 lines for 16 dots","2024-01","https://www.nature.com/articles/s41565-023-01491-3")],
  "The 2024 crossbar (16 dots, 23 lines; founding paper online 2023-08-28) showed no coherent qubit operation. The 'one of four pairs gated' result belongs to imec/Diraq's individually wired 8-qubit 300 mm device (Nat. Commun. 17, 5878, 2026-07), not to a crossbar.","Crossbar 2024 года (16 точек, 23 линии; основополагающая статья онлайн 2023-08-28) не показал когерентных операций с кубитами. Результат «сработала одна пара из четырёх» относится к индивидуально разведённому 8-кубитному 300-мм устройству imec/Diraq (Nat. Commun. 17, 5878, 2026-07), а не к crossbar."),
]
# ---------------------------------------------------------------- L5 CONTROL
NODES += [
N("ct_rt",5,"Room-temperature electronics + per-qubit coax/flex","Комнатная электроника + коаксиал/флекс на кубит",1.0,["fab"],None,"na",None,"none","mw","RT",["coherent"],"sclitho","D",
  "One RF line per qubit through the fridge; the I/O wall: > 4,000 RF lines (KIDE), 1,121 qubits (Condor).","Одна РЧ-линия на кубит через криостат; стена I/O: > 4 000 РЧ-линий (KIDE), 1 121 кубит (Condor).",
  [("path","I/O wall","> 4,000 high-density RF lines per fridge","2026","https://bluefors.com/"),
   ("count","largest single-fridge chip","1,121 qubits (Condor)","2023-12","https://www.ibm.com/quantum/blog/quantum-roadmap-2033")],"",""),
N("ct_cryocmos",5,"Cryo-CMOS controller (4 K / mK)","Cryo-CMOS контроллер (4 K / мК)",1.0,["fab"],None,"na",None,"none","mw","4K",["coherent"],"cmos","D",
  "CMOS ASICs at 4 K (or 7 mK) generating pulses next to the qubits; 2–23 mW/qubit at 4 K; 20 nW/MHz per cell at mK.","CMOS ASIC при 4 K (или 7 мК), формирующие импульсы рядом с кубитами; 2–23 мВт/кубит при 4 K; 20 нВт/МГц на ячейку при мК.",
  [("path","HRL 4 K controller sequencing QEC","≤ 3.5 W, 366 DACs; d=5 *bit-flip-only* repetition code Λ=4.7 without room-temperature real-time electronics (arXiv Apr–May 2026, Nature Jul 2026)","2026-07","https://arxiv.org/abs/2604.16216"),
   ("path","IBM 14 nm at 4 K","23 mW/qubit; 1Q 8×10⁻⁴","2024-02","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326"),
   ("path","mK CMOS next to spin qubits","~20 nW/MHz per cell; fidelity impact 0.07%","2025-06","https://www.nature.com/articles/s41586-025-09157-x")],"",""),
N("ct_sfq",5,"SFQ digital control (millikelvin)","Цифровое SFQ-управление (милликельвины)",1.0,["fab"],None,"na",None,"none","mw","mK",["pauli"],"sclitho","E",
  "Single-flux-quantum digital circuits at the mK stage: pulse trains drive qubits from a flip-chip (1Q > 99%, 99.9% peak; nW/qubit claimed), and the same circuit family loads D-Wave's on-chip flux DACs. SFQ logic at 4 K (pulse sequencing, decoding) is the empty cold-decoder slot, not a control node.","Одноквантовые цифровые схемы на мК-ступени: цепочки импульсов управляют кубитами с flip-chip (1Q > 99%, пик 99.9%; заявлено нВт/кубит), и та же схемотехника загружает on-chip flux-DAC D-Wave. SFQ-логика при 4 K (секвенсирование импульсов, декодирование) — пустой слот холодного декодера, а не узел управления.",
  [("path","SEEQC mK SFQ control","1Q > 99%, up to 99.9% (Nature Electronics)","2026-03","https://www.nature.com/articles/s41928-026-01576-6"),
   ("path","QP-poisoning-limited SFQ MCM","1.2% error/Clifford, 0.96% from photon-mediated QP","2023-07","https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310")],
  "SEEQC–IBM integration under DARPA QBI (since Jun 2025).","Интеграция SEEQC–IBM в рамках DARPA QBI (с июня 2025)."),
N("ct_fluxdac",5,"On-chip flux-DAC multiplexing","On-chip мультиплексирование flux-DAC",1.0,["fab"],None,"na",None,"none","lf","mK",["coherent"],"sclitho","D",
  "Annealer-heritage SFQ flux DACs: ~200–300 bias lines for 10⁴ qubits; applied to fluxonium (bump-bonded MCM).","Flux-DAC на SFQ из наследия отжигателей: ~200–300 линий смещения на 10⁴ кубитов; применено к флаксониуму (bump-bonded MCM).",
  [("path","bias lines per qubits","200 bias wires (press release 2026-01-06) vs ~300 bias lines (whitepaper 2026-01-23) for the same annealer scheme — unreconciled; fluxonium MCM at 10 mK","2026-01","https://www.dwavequantum.com/media/41upubz2/14-1090a-a_fluxonium-dac-control.pdf")],
  "D-Wave's own figures disagree: 200 bias wires in the 2026-01-06 release against ~300 in the 2026-01-23 whitepaper. NASA JPL fabricated key components of the module.","Собственные данные D-Wave расходятся: 200 линий смещения в релизе 2026-01-06 против ~300 в whitepaper 2026-01-23. Ключевые компоненты модуля изготовлены в NASA JPL."),
N("ct_laser",5,"Laser + AOD/SLM optical control (atoms)","Лазер + AOD/SLM оптическое управление (атомы)",0.0,["nat"],None,"na",None,"none","opt","RT",["coherent"],"optics","D",
  "SLM-generated tweezer arrays (12,000 sites), AOD moves, Rydberg lasers; 33 W for 18,225 tweezers; the binding constraint above 10⁴ sites is the AOD time–bandwidth product, not an SLM refresh rate.","Массивы пинцетов от SLM (12 000 сайтов), перемещения AOD, ридберговские лазеры; 33 Вт на 18 225 пинцетов; выше 10⁴ сайтов ограничивает произведение время–полоса у AOD, а не частота обновления SLM.",
  [("count","SLM array","~12,000 sites, 6,100 atoms","2025-09","https://arxiv.org/abs/2403.12021"),
   ("path","metasurface tweezers","18,225 traps from 33 W","2026-06","https://arxiv.org/abs/2606.02715")],
  "The '~10 MHz SLM refresh' sometimes quoted is unsourced: LCOS panels frame at tens of hertz, and deflector reconfiguration is bounded by acoustic transit. The only end-to-end vendor loop figure is QuEra Gemini: one shot per second at 260 qubits.","Иногда цитируемое «обновление SLM ~10 МГц» не подкреплено источником: панели LCOS обновляются с частотой десятков герц, а перестройка дефлектора ограничена акустическим пробегом. Единственная сквозная вендорская цифра — QuEra Gemini: один выстрел в секунду на 260 кубитах."),
N("ct_pic_trap",5,"PIC-generated tweezers / integrated optics for atoms","Пинцеты от PIC / интегрированная оптика для атомов",0.25,["nat"],None,"na",None,"none","opt","RT",["coherent"],"pic","E",
  "Trap generation moved onto a photonic chip (4 atoms, 27.5 s lifetimes); fabricated-world optics for a natural carrier.","Генерация ловушек перенесена на фотонный чип (4 атома, время жизни 27.5 с); оптика изготовленного мира для естественного носителя.",
  [("path","on-chip traps","4 Rb atoms, 27.5 s lifetime","2026-08","https://www.pasqal.com/newsroom/pasqal-brings-qubit-control-on-chip/")],
  "Pasqal. Two functions hide here and only the first is trap generation: UChicago's 2024 tweezers are free-space traps over nanophotonic cavities, and USTC's 2026 glass-waveguide chip addresses trapped atoms rather than generating the traps.","Pasqal. Здесь скрыты две функции, и только первая — генерация ловушек: пинцеты UChicago 2024 года — ловушки в свободном пространстве над нанофотонными резонаторами, а стеклянно-волноводный чип USTC 2026 года адресует уже захваченные атомы, а не создаёт ловушки."),
N("ct_ionlaser",5,"Laser control with integrated photonics (ions)","Лазерное управление с интегрированной фотоникой (ионы)",0.0,["nat"],None,"na",None,"none","opt","vac",["coherent"],"pic","D",
  "Waveguides in the trap deliver all wavelengths; > 99.3% 2Q (ETH); ≥ 7 wavelengths on Helios.","Волноводы в ловушке доставляют все длины волн; > 99.3% 2Q (ETH); ≥ 7 длин волн на Helios.",
  [("path","waveguide-delivered 2Q gate","> 99.3%","2020-10","https://www.nature.com/articles/s41586-020-2823-6")],"",""),
N("ct_ionmw",5,"Chip-integrated microwave control (ions)","СВЧ-управление, интегрированное в чип (ионы)",1.0,["nat"],None,"na",None,"none","mw","RT",["pauli"],"mems","D",
  "Electronic signal sources replace gate lasers: ~200 sources for 1,000 ions (WISE); 1Q 1.5×10⁻⁷ without shielding.","Электронные источники сигнала заменяют лазеры гейтов: ~200 источников на 1 000 ионов (WISE); 1Q 1.5×10⁻⁷ без экранирования.",
  [("channel","chip-integrated microwave 1Q","1.5×10⁻⁷ error per Clifford","2024-12","https://arxiv.org/abs/2412.04421"),
   ("path","WISE architecture","1,000 ions with ~200 signal sources (design)","2023","https://arxiv.org/abs/2305.12773")],"Oxford Ionics/IonQ, eleQtron (MAGIC).","Oxford Ionics/IonQ, eleQtron (MAGIC)."),
N("ct_base",5,"Baseband electrical control (spins, Majorana)","Baseband электрическое управление (спины, майораны)",1.0,["fab"],None,"na",None,"none","lf","RT",["coherent"],"cmos","D",
  "Voltage pulses on gates; digital, dense; the calibration burden shows up as coherent error.","Импульсы напряжения на затворах; цифровое, плотное; бремя калибровки проявляется как когерентная ошибка.",
  [("channel","extrinsic control share of CNOT error","~80% (HRL)","2026-07","https://arxiv.org/abs/2604.16216")],
  "QuTech's baseband hopping-gate figure of 99.50(6)% is a lower bound, not a point estimate. HRL's Λ = 4.7 is a bit-flip-only repetition code, and its [[4,2,2]] fidelity of 0.95 is post-selected.","99.50(6)% для baseband hopping-гейта у QuTech — нижняя граница, а не точечная оценка. Λ = 4.7 у HRL — repetition-код только по bit-flip, а его [[4,2,2]] с fidelity 0.95 — постселектированный."),
]
# ---------------------------------------------------------------- L6 READOUT
NODES += [
N("ro_disp",6,"Dispersive microwave readout (+TWPA, Purcell)","Дисперсионное СВЧ-считывание (+TWPA, Purcell)",1.0,["fab"],None,"na",C("disp",-6.55,False,True),"none","mw","RT",["leak"],"sclitho","D",
  "Resonator shift read through a parametric amplifier; 240 ns pulse at 99.94% (IQM); readout-induced leakage is the hidden cost.","Сдвиг резонатора, читаемый через параметрический усилитель; импульс 240 нс при 99.94% (IQM); скрытая цена — утечка, наведённая считыванием.",
  [("clock","readout pulse / fidelity (IQM)","240 ns pulse (≈280 ns full window) / 99.94% simultaneous assignment; QNDness 99.3%","2025-09","https://arxiv.org/abs/2508.16437"),
   ("channel","at-scale readout error","~1×10⁻² (fleet)","2025-08","https://www.ibm.com/quantum/hardware")],"",""),
N("ro_fluor",6,"Fluorescence state detection (ions)","Флуоресцентное определение состояния (ионы)",0.0,["nat"],None,"na",C("fluor",-4.0,False,True),"none","opt","RT",["pauli"],"optics","D",
  "State-dependent scattering counted by PMT/SNSPD; 11 µs at 99.93% record; SPAM 4.8×10⁻⁴ on Helios.","Зависимое от состояния рассеяние, считаемое ФЭУ/SNSPD; рекорд 11 мкс при 99.93%; SPAM 4.8×10⁻⁴ на Helios.",
  [("clock","fastest ion readout","11 µs at 99.931% (¹⁷¹Yb⁺, MoSi SNSPD)","2019","https://www.nature.com/articles/s42005-019-0195-8"),
   ("channel","Helios SPAM","4.8×10⁻⁴","2025-11","https://arxiv.org/abs/2511.05465")],
  "The Kyoto/Yaqumo 17.6 µs result (arXiv:2605.24175) is neutral ¹⁷⁴Yb *imaging* — spinless, not qubit-state-resolved — and is not an ion-readout record.","Результат Kyoto/Yaqumo 17.6 мкс (arXiv:2605.24175) — *imaging* нейтрального ¹⁷⁴Yb, бесспиновый и не разрешающий состояние кубита; это не рекорд считывания ионов."),
N("ro_img",6,"Fluorescence imaging of atom arrays","Флуоресцентный imaging массивов атомов",0.0,["nat"],None,"na",C("img",-3.3,False,True),"none","opt","RT",["loss"],"optics","D",
  "Camera imaging, 0.5–1 ms typical; non-destructive with 0.24% loss; fast neutral-Yb imaging emerging (17.6 µs, 99.89%).","Imaging камерой, типично 0.5–1 мс; неразрушающее с потерей 0.24%; формируется быстрый imaging нейтрального Yb (17.6 мкс, 99.89%).",
  [("clock","typical mid-circuit readout","~0.5–1 ms; 0.46% bit-flip, 0.24% loss","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("clock","fast imaging (emerging)","17.6 µs, 99.89% discrimination, 98.8% survival — neutral ¹⁷⁴Yb, spinless (not qubit-state-resolved)","2026-08","https://arxiv.org/html/2605.24175")],"",""),
N("ro_s2c",6,"Spin-to-charge conversion + rf reflectometry","Спин-в-заряд + rf-рефлектометрия",1.0,["fab"],None,"na",C("s2c",-5.2,False,True),"none","lf","RT",["coherent"],"cmos","D",
  "Pauli/energy-selective tunnelling sensed by a gate-based single-electron box (SEB) or an SET; 99.2% in < 6 µs; 99.9% at 100 µs.","Туннелирование по Паули/энергии, регистрируемое затворным одноэлектронным боксом (SEB) или SET; 99.2% за < 6 мкс; 99.9% за 100 мкс.",
  [("clock","fast readout (Oakes et al., Quantum Motion; rf single-electron box)","99.2% in < 6 µs","2023-02","https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.011023"),
   ("channel","best SPAM","99.9% (100 µs integration)","2025-09","https://www.nature.com/articles/s41586-025-09531-9")],
  "The 99.2% in < 6 µs is Oakes et al., PRX 13, 011023 (2023), Quantum Motion — an rf single-electron box, not an SET.","99.2% за < 6 мкс — Oakes et al., PRX 13, 011023 (2023), Quantum Motion: rf-одноэлектронный бокс, а не SET."),
N("ro_spd",6,"Single-photon detection (SNSPD / TES)","Детектирование одиночных фотонов (SNSPD / TES)",0.25,["pho"],None,"na",C("spd",-8.0,True,False),"none","eo","4K",["loss"],"pic","D",
  "Destructive by nature; 93.4% wafer-scale median to 99.73% on a hero device, 3 ps jitter, 1–4 K; thousands of channels needed.","Разрушающее по природе; от 93.4% медианы в масштабе пластины до 99.73% на рекордном устройстве, джиттер 3 пс, 1–4 K; нужны тысячи каналов.",
  [("channel","wafer-scale median on-chip efficiency (PsiQuantum Omega, 300 mm)","93.4% at ~2 K","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","best on-chip efficiency (laboratory device)","99.73%","2025-10","https://www.nature.com/articles/s41377-025-02031-5")],
  "The '98.9% median (PsiQuantum)' sometimes quoted is superseded: the Omega paper gives 93.4% median on-chip efficiency — 0.30 dB per detection rather than 0.05 dB.","Иногда цитируемая «98.9% медиана (PsiQuantum)» вытеснена: статья по Omega даёт 93.4% медианной эффективности на чипе — 0.30 дБ на детектирование вместо 0.05 дБ."),
N("ro_qcap",6,"rf quantum-capacitance parity readout","rf-считывание чётности по квантовой ёмкости",1.0,["fab"],None,"na",C("qcap",-4.0,False,True),"none","lf","RT",["unknown"],"mbe","E",
  "Interferometric parity readout of a Majorana wire; 1% assignment error, SNR 1 in 3.6 µs.","Интерферометрическое считывание чётности майорановской проволоки; 1% ошибка присвоения, SNR 1 за 3.6 мкс.",
  [("clock","readout","1% error; SNR 1 in 3.6 µs","2025-02","https://www.nature.com/articles/s41586-024-08445-2"),
   ("clock","independent replication (QuTech, InSb Kitaev chain)","~1.85 ms dwell, SNR ~1.93","2026-02","https://www.nature.com/articles/s41586-025-09927-7")],
  "The independent replication is van Loo et al., Nature 650 (2026-02-11), on an InSb minimal Kitaev chain; arXiv:2607.09511 is the follow-on coherent parity qubit, a different result.","Независимая репликация — van Loo et al., Nature 650 (2026-02-11), на минимальной цепочке Китаева в InSb; arXiv:2607.09511 — последующий когерентный кубит чётности, другой результат."),
N("ro_erasure",6,"Mid-circuit erasure check","Проверка erasure в середине схемы",0.5,["fab","nat","pho"],None,"na",C("erasure",-6.4,False,True),"none","mw","RT",["erasure"],"none","D",
  "Ancilla-based detection of leakage/loss without disturbing the code: 384 ns (transmon), 1.8 µs (cavity), 20 µs (Yb atoms).","Детекция утечки/потери через анциллу без возмущения кода: 384 нс (трансмон), 1.8 мкс (полость), 20 мкс (атомы Yb).",
  [("clock","transmon dual-rail check","384 ns, false-negative ~0.8%","2026-04","https://arxiv.org/abs/2604.16292"),
   ("clock","cavity dual-rail check","1.8 µs, FP 0.51% / FN 3.7%","2025-01","https://www.nature.com/articles/s41534-024-00944-4"),
   ("clock","Yb erasure detection","20 µs (1Q) / 420 µs (2Q)","2023-05","https://arxiv.org/abs/2305.05493")],"",""),
]
# ---------------------------------------------------------------- L7 CODE
NODES += [
N("code_surface",7,"Rotated surface code (+ yoked variants)","Ротированный surface code (+ yoked-варианты)",0.5,["fab","nat"],None,"na",None,"static","none","none",["pauli"],"none","D",
  "2D nearest-neighbour code; threshold 0.94%; ~650–1,500 physical per logical at 10⁻¹² (yokes cut ~1,500 to 600–800).","2D-код ближайших соседей; порог 0.94%; ~650–1 500 физических на логический при 10⁻¹² (yokes снижают ~1 500 до 600–800).",
  [("channel","Λ (Willow, d=3→7)","2.14 ± 0.02; d=7 record 7.72×10⁻⁴/cycle (Jul 2026)","2026-07","https://www.nature.com/articles/s41586-026-10759-2"),
   ("channel","Λ (USTC 107 q, d=7)","1.40(6)","2025-12","https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31"),
   ("channel","neutral-atom d=3→5","2.14(13)× in 4-round circuit","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("count","teraquop footprint, plain patches (p=10⁻³)","~1,500 physical/logical (800 with 1D yokes, 600 with 2D yokes)","2023-12","https://arxiv.org/abs/2312.04522"),
   ("count","teraquop footprint with correlated matching (p=10⁻³)","~650 physical/logical","2023-12","https://arxiv.org/abs/2312.08813")],"",""),
N("code_color",7,"Colour code (transversal Cliffords)","Colour code (трансверсальные Клиффорды)",0.5,["fab","nat"],None,"na",None,"static","none","none",["pauli"],"none","D",
  "Triangular 2D code with transversal H/S/CNOT; ~1.9× the surface-code footprint; hosts distillation and injection.","Треугольный 2D-код с трансверсальными H/S/CNOT; ~1.9× площадь surface code; несёт дистилляцию и инъекцию.",
  [("channel","Λ₃/₅ (Google)","1.56(4); logical Clifford 0.0027","2025-05","https://www.nature.com/articles/s41586-025-09061-4"),
   ("channel","5-to-1 distillation on logical qubits","d=3: 95.1%→99.4%; d=5: 92.5%→98.6%","2025-07","https://www.nature.com/articles/s41586-025-09367-3")],"",""),
N("code_qldpc",7,"Non-local qLDPC codes (bivariate-bicycle, 'gross')","Нелокальные qLDPC-коды (bivariate-bicycle, «gross»)",0.5,["fab","nat"],None,"na",None,"longrange","none","none",["pauli"],"none","E",
  "The surface code is itself a qLDPC code with 2D-local checks and vanishing rate; this node is the non-local, constant-rate family. 'Gross' = IBM's [[144,12,12]] bivariate-bicycle code (144 = a gross, 12 dozen; 'two-gross' = [[288,12,18]]): 12 logical in 288 qubits incl. checks, threshold 0.8%, needs degree-6 connectivity. Hardware: IonQ 4 logical in 18 ions (reported as [[18,4,3]]) at break-even, Zhejiang [[18,4,4]] not.","Поверхностный код сам является qLDPC-кодом с 2D-локальными проверками и исчезающей скоростью; этот узел — нелокальное семейство с постоянной скоростью. «Gross» = код IBM [[144,12,12]] (144 = гросс, 12 дюжин; «two-gross» = [[288,12,18]]): 12 логических в 288 кубитах с проверками, порог 0.8%, нужна связность степени 6. На железе: IonQ — 4 логических в 18 ионах (сообщается как [[18,4,3]]) на break-even, Zhejiang [[18,4,4]] — нет.",
  [("count","gross code overhead","288 physical for 12 logical (~24/logical) vs ~3,000 surface","2024-03","https://arxiv.org/abs/2308.07915"),
   ("channel","IonQ memory: 4 logical in 18 ions (reported as [[18,4,3]])","3.95 ± 0.68 s vs 3.3 ± 0.9 s physical (leakage post-selected)","2026-06","https://arxiv.org/abs/2606.06455"),
   ("channel","Zhejiang [[18,4,4]] on 32 SC qubits","8.91%/logical/cycle (not break-even)","2025-05","https://arxiv.org/html/2505.09684"),
   ("count","RSA-2048 with qLDPC (Pinnacle)","< 100,000 physical qubits at 10⁻³, 1 µs cycle","2026-02","https://arxiv.org/abs/2602.11457")],
  "IBM Kookaburra (2026, not yet delivered). The IonQ abstract states '4 logical into 18 physical' without code notation; [[18,4,3]] is inferred, not reported.","IBM Kookaburra (2026, ещё не поставлен). В аннотации IonQ сказано «4 логических в 18 физических» без нотации кода; [[18,4,3]] — вывод, а не заявленное значение."),
N("code_highrate",7,"High-rate concatenated codes with transversal gates","Высокоскоростные конкатенированные коды с трансверсальными гейтами",0.0,["nat"],None,"na",None,"transport","none","none",["pauli"],"none","D",
  "Iceberg [[k+2,k,2]], [[80,48,4]], tesseract colour code [[16,6,4]] (subsystem variant [[16,4,2,4]] at Quantinuum): many logical qubits per physical block; needs all-to-all.","Iceberg [[k+2,k,2]], [[80,48,4]], тессерактный colour code [[16,6,4]] (подсистемный вариант [[16,4,2,4]] у Quantinuum): много логических кубитов на физический блок; нужен all-to-all.",
  [("count","Helios [[80,48,4]]","48 corrected logical qubits; logical gate error 1.0–1.2×10⁻⁴","2026-02","https://arxiv.org/abs/2602.22211"),
   ("count","Harvard tesseract [[16,6,4]]","up to 96 d=4 logical qubits active","2025-11","https://www.nature.com/articles/s41586-025-09848-5"),
   ("count","Quantinuum tesseract [[16,6,4]] on ions","transversal logical Clifford group in depth-one circuits, 12 addressable logical CZ pairs","2026-06","https://www.nature.com/articles/s41586-026-10628-y")],
  "The tesseract is [[16,6,4]], a doubly-even self-dual 4D CSS code; the [[16,4,4]] sometimes quoted is wrong. Quantinuum uses its subsystem variant [[16,4,2,4]].","Тессеракт — [[16,6,4]], дважды-чётный самодуальный 4D CSS-код; иногда встречающееся [[16,4,4]] неверно. Quantinuum использует его подсистемный вариант [[16,4,2,4]]."),
N("code_erasure",7,"Erasure-adapted codes","Коды, адаптированные к erasure",0.5,["fab","nat","pho"],None,"na",None,"static","none","none",["erasure"],"none","E",
  "Surface/loss-tolerant codes fed with erasure flags: threshold 0.94% → 4.15%; dual-rail simulation Λ≈27 (idealised).","Surface/loss-tolerant коды с флагами erasure: порог 0.94% → 4.15%; симуляция dual-rail Λ≈27 (идеализировано).",
  [("channel","threshold with 98% erasure","4.15% vs 0.937%","2022-01","https://arxiv.org/abs/2201.03540"),
   ("channel","[[4,2,2]] erasure teleportation (atoms)","logical decay 1.9(4)× slower with erasure info in unconditional decoding","2026-06","https://arxiv.org/abs/2506.13724")],
  "Use 1.9(4)× architecturally: it is the unconditional decoding gain. The 3.6(1)× often quoted is the post-selected hold.","Архитектурно использовать 1.9(4)×: это выигрыш безусловного декодирования. часто цитируемое 3.6(1)× — постселектированное удержание."),
N("code_bosonic",7,"Bosonic concatenation (repetition-cat, LDPC-cat, GKP+qLDPC)","Бозонная конкатенация (repetition-cat, LDPC-cat, GKP+qLDPC)",0.75,["fab","pho"],None,"na",None,"static","none","none",["bias","gauss"],"none","E",
  "Outer code exploits inner bias/shift correction; Ocelot's two points are not a distance scan; LDPC-cat assumes 0.1% phase-flip (measured ~10%).","Внешний код использует внутренний bias/коррекцию сдвигов; две точки Ocelot — не скан по расстоянию; LDPC-cat предполагает 0.1% phase-flip (измерено ~10%).",
  [("channel","repetition-cat (Ocelot)","d=3 1.75% at |α|²=1 → d=5 1.65% at |α|²=1.5 per 2.8 µs cycle — different n̄, not a distance scan","2025-02","https://www.nature.com/articles/s41586-025-08642-7"),
   ("count","LDPC-cat estimate","758 cats → 100 logical at 10⁻⁸ (assumes 0.1% phase-flip)","2024-01","https://arxiv.org/abs/2401.09541"),
   ("count","repetition-cat estimate (Gouzien et al.)","126,133 cats for a 256-bit elliptic-curve logarithm in 9 h","2023-02","https://arxiv.org/abs/2302.06639")],
  "Ocelot's 'd=3→5 nearly flat' is not a distance scan: the two points sit at different mean photon numbers. Gouzien et al. size ECC-256, not RSA-2048.","«Почти плоско от d=3 к d=5» у Ocelot — не скан по расстоянию: точки взяты при разных средних числах фотонов. Gouzien et al. оценивают ECC-256, а не RSA-2048."),
N("code_fusion",7,"Fusion-based fault tolerance","Fusion-based отказоустойчивость",0.25,["pho"],None,"na",None,"flying","none","none",["loss"],"none","T",
  "Resource states + fusions; loss threshold 2.7%/photon (boosted 6-ring), 17.4% only for a {7,4}-encoded resource state of ~168 photons; no demonstration.","Ресурсные состояния + fusions; порог потерь 2.7%/фотон (усиленный 6-ring), 17.4% — только для {7,4}-кодированного ресурсного состояния из ~168 фотонов; демонстраций нет.",
  [("channel","loss threshold","2.7% per photon (boosted 6-ring); 17.4% ({7,4}-encoded resource state)","2025-06","https://arxiv.org/abs/2506.11975")],
  "FBQC framework = Bartolucci et al., Nat. Commun. 14, 912 (2023-02). The 2.7% (boosted 6-ring) and Sparrow's 0.38–0.82% (unencoded 6-ring, arXiv:2606.28490, 2026) assume different boosting, bias models and decoders and remain unreconciled.","Каркас FBQC — Bartolucci et al., Nat. Commun. 14, 912 (2023-02). 2.7% (усиленный 6-ring) и 0.38–0.82% у Sparrow (некодированный 6-ring, arXiv:2606.28490, 2026) исходят из разных допущений об усилении, модели bias и декодере и не сведены."),
N("code_aft",7,"Algorithmic FT / transversal architectures","Алгоритмическая FT / трансверсальные архитектуры",0.0,["nat"],None,"na",None,"transport","none","none",["pauli"],"none","E",
  "Constant syndrome rounds per logical gate via transversal gates + correlated decoding; amortises slow cycles (> 10× space-time).","Постоянное число синдромных раундов на логический гейт через трансверсальные гейты + коррелированное декодирование; амортизирует медленные циклы (> 10× пространство-время).",
  [("clock","rounds per logical gate","O(d) → O(1)","2024-06","https://arxiv.org/abs/2406.17653"),
   ("count","Shor / P-256 on reconfigurable atoms","10,000 atoms minimum (26,000 time-efficient); P-256 in days, RSA-2048 one to two orders longer","2026-03","https://arxiv.org/abs/2603.28627"),
   ("count","RSA-2048 on reconfigurable atoms (ISCA 2025)","5.6 days on 19 M qubits at a 1 ms cycle","2025-05","https://arxiv.org/abs/2505.15907")],
  "'RSA-2048 with ~10⁴ atoms' is what neither paper says: arXiv:2603.28627 is Shor/P-256, and the RSA-2048 point on the same trade curve is 19 M qubits for 5.6 days (ISCA 2025). Transversal architectures are not atoms-only — Quantinuum ran the tesseract [[16,6,4]] on trapped ions (Nature 654, 2026-06).","«RSA-2048 на ~10⁴ атомах» не утверждает ни одна из статей: arXiv:2603.28627 — это Shor/P-256, а точка RSA-2048 на той же кривой компромисса — 19 млн кубитов за 5.6 суток (ISCA 2025). Трансверсальные архитектуры не привязаны к атомам — Quantinuum выполнила тессерактный [[16,6,4]] на ионах (Nature 654, 2026-06)."),
N("code_magic",7,"Magic-state factory (cultivation / distillation / code switching)","Фабрика магических состояний (культивация / дистилляция / переключение кодов)",0.5,["fab","nat"],None,"na",None,"static","none","none",["pauli"],"none","D",
  "Non-Clifford resource; cultivation reaches 10⁻⁹ T-error at ~cost of a CNOT (theory), 0.9999 shown at 8% acceptance.","Ресурс для не-клиффордовых гейтов; культивация даёт 10⁻⁹ T-ошибки за ~цену CNOT (теория), показано 0.9999 при 8% принятых.",
  [("channel","cultivation (Google)","0.9999(1), 8% acceptance, 40× error reduction","2025-12","https://arxiv.org/abs/2512.13908"),
   ("channel","code switching (Quantinuum)","≤ 5.1×10⁻⁴ at 82.6% acceptance","2025-06","https://arxiv.org/abs/2506.14169")],"",""),
]
# ---------------------------------------------------------------- L8 DECODER
NODES += [
N("dec_mwpm",8,"MWPM / Sparse Blossom (+correlated matching)","MWPM / Sparse Blossom (+коррелированный matching)",0.5,["fab","nat"],None,"na",None,"none","none","none",["pauli"],"none","D",
  "Matching decoder; < 1 µs/round at d=17 on one core (throughput), 0.8 µs FPGA latency at d=13 (Micro Blossom); Λ=2.04 on Willow vs 2.14 neural.","Matching-декодер; < 1 мкс/раунд при d=17 на одном ядре (пропускная способность), 0.8 мкс задержки на FPGA при d=13 (Micro Blossom); Λ=2.04 на Willow против 2.14 у нейросетевого.",
  [("clock","PyMatching v2 throughput","< 1 µs/round at d=17, p=0.1%","2023-03","https://arxiv.org/abs/2303.15933"),
   ("clock","Micro Blossom FPGA (ASPLOS 2025)","0.8 µs average latency at d=13, p=0.1%","2025-02","https://arxiv.org/abs/2502.14787")],
  "Micro Blossom's published figure is 0.8 µs at d=13 (ASPLOS 2025, arXiv:2502.14787); the repository's 367 ns appears in no paper. Willow's real-time decoder is a parallelised Sparse Blossom variant built by Google, not stock PyMatching.","Опубликованный результат Micro Blossom — 0.8 мкс при d=13 (ASPLOS 2025, arXiv:2502.14787); 367 нс из репозитория не встречаются ни в одной статье. Декодер реального времени Willow — параллелизованный вариант Sparse Blossom, сделанный Google, а не стандартный PyMatching."),
N("dec_nn",8,"Neural decoders (AlphaQubit2, CNN, transformers)","Нейросетевые декодеры (AlphaQubit2, CNN, трансформеры)",0.5,["fab","nat"],None,"na",None,"none","none","none",["pauli"],"none","D",
  "Learned decoders beat matching by 5–25%; FPGA NN decode 124 ns at d=3; throughput at d≥11 still short of 1 µs.","Обучаемые декодеры лучше matching на 5–25%; NN на FPGA — 124 нс при d=3; пропускная способность при d≥11 ещё меньше 1 мкс.",
  [("channel","Willow d=7 with AlphaQubit2","7.72×10⁻⁴/cycle","2026-07","https://www.nature.com/articles/s41586-026-10759-2"),
   ("clock","FPGA NN decoder","124 ns decode, 550 ns closed loop (d=3)","2026-05","https://arxiv.org/abs/2605.04892")],"",""),
N("dec_relaybp",8,"Relay-BP for qLDPC (FPGA)","Relay-BP для qLDPC (FPGA)",0.5,["fab","nat"],None,"na",None,"none","none","none",["pauli"],"none","D",
  "Belief propagation with relays: 24 ns/iteration, average < 1 µs per cycle, ~100× lower LER than BP-OSD.","Belief propagation с реле: 24 нс/итерация, в среднем < 1 мкс на цикл, ~100× ниже LER, чем BP-OSD.",
  [("clock","FPGA Relay-BP","average < 1 µs per cycle at p < 3×10⁻³ (simulated syndromes)","2025-10","https://arxiv.org/abs/2510.21600")],
  "A '480 ns per 12-cycle window' figure sometimes quoted is ~25× off the paper's average of under 1 µs per cycle. Relay-BP originates with Müller et al., arXiv:2506.01779 (2025-06-02); arXiv:2510.21600 is the FPGA implementation.","Иногда цитируемые «480 нс на окно из 12 циклов» расходятся примерно в 25 раз со средним значением статьи — менее 1 мкс на цикл. Relay-BP берёт начало от Müller et al., arXiv:2506.01779 (2025-06-02); arXiv:2510.21600 — это FPGA-реализация."),
N("dec_fpga",8,"FPGA real-time decoders (LCD, Deltaflow)","FPGA-декодеры реального времени (LCD, Deltaflow)",0.5,["fab","nat"],None,"na",None,"none","none","none",["pauli"],"none","D",
  "Local-clustering < 1 µs/round to d=17; Deltaflow 2 16 µs mean latency at d=5 on QPU data (vs Google 63 µs).","Local-clustering < 1 мкс/раунд до d=17; Deltaflow 2 — 16 мкс средней задержки при d=5 на данных QPU (против 63 мкс у Google).",
  [("clock","Riverlane LCD","< 1 µs/round to d=17","2025-12","https://www.nature.com/articles/s41467-025-66773-x"),
   ("clock","Google real-time at d=5","63 µs latency, Λ=2.0","2024-08","https://arxiv.org/abs/2408.13687")],"",""),
N("dec_gpu",8,"GPU decoding via NVQLink","GPU-декодирование через NVQLink",0.5,["fab","nat"],None,"na",None,"none","none","none",["pauli"],"none","D",
  "3.84 µs round trip; Helios+GH200 BP-OSD median 67 µs (5.4× LER gain); platform-agnostic layer.","Круговая задержка 3.84 мкс; Helios+GH200 BP-OSD медиана 67 мкс (выигрыш LER 5.4×); платформенно-независимый слой.",
  [("clock","NVQLink RoCE round trip","3.84 µs mean","2025-10","https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/")],
  "NVQLink was announced on 2025-10-28.","NVQLink анонсирован 2025-10-28."),
N("dec_corr",8,"Correlated / loss-aware decoding (transversal, atom loss)","Коррелированное / loss-aware декодирование (трансверсальные гейты, потеря атомов)",0.0,["nat"],None,"na",None,"none","none","none",["loss","erasure"],"none","D",
  "Decodes across transversal gates and uses loss flags; 1.73× QEC gain on 448-atom processor.","Декодирует сквозь трансверсальные гейты и использует флаги потерь; выигрыш QEC 1.73× на процессоре из 448 атомов.",
  [("channel","loss-aware ML decoding gain","1.73(13)×","2025-11","https://www.nature.com/articles/s41586-025-09848-5")],"",""),
N("dec_rl",8,"In-loop RL calibration / decoder steering","RL-калибровка в контуре / управление декодером",1.0,["fab"],None,"na",None,"none","none","none",["coherent"],"none","D",
  "Reinforcement learning tunes > 1,000 control parameters during QEC: ~20% extra suppression, 3.5× drift robustness.","Обучение с подкреплением подстраивает > 1 000 параметров управления во время QEC: ~20% дополнительного подавления, 3.5× устойчивость к дрейфу.",
  [("channel","RL-steered QEC","20% LER cut, 3.5× stability vs drift","2026-07","https://arxiv.org/abs/2511.08493")],"",""),
N("dec_cryo",8,"Cryogenic / on-chip decoder (SFQ, cryo-CMOS)","Криогенный / on-chip декодер (SFQ, cryo-CMOS)",1.0,["fab"],None,"na",None,"none","mw","mK",["pauli"],"sclitho","X",
  "Designs only: NISQ+ (≤ 20 ns, SFQ), QECOOL (2.8 µW), Pinball/CryoZip (4 K predecoders) — no fabricated decoder chip.","Только дизайны: NISQ+ (≤ 20 нс, SFQ), QECOOL (2.8 мкВт), Pinball/CryoZip (предекодеры при 4 K) — ни одного изготовленного чипа-декодера.",
  [("clock","QECOOL on-line SFQ decoder (simulation)","2.78 µW at 2 GHz","2021-03","https://arxiv.org/abs/2103.14209"),
   ("clock","NISQ+ approximate SFQ decoder (design)","≤ 20 ns latency","2020-04","https://arxiv.org/abs/2004.04794"),
   ("path","cryo-CMOS predecoder (design)","3,780× syndrome-bandwidth reduction at < 0.56 mW","2025-12","https://arxiv.org/abs/2512.09807")],
  "arXiv:2103.14209 is QECOOL — an SFQ decoder, not cryo-CMOS; the ≤ 20 ns latency belongs to NISQ+ (arXiv:2004.04794).","arXiv:2103.14209 — это QECOOL, SFQ-декодер, а не cryo-CMOS; задержка ≤ 20 нс относится к NISQ+ (arXiv:2004.04794)."),
]
# ---------------------------------------------------------------- L9 INTERCONNECT
NODES += [
N("ic_mcm",9,"Multi-chip modules / l-couplers (same cryostat)","Многочиповые модули / l-couplers (один криостат)",1.0,["fab"],None,"na",None,"longrange","mw","mK",["coherent"],"sclitho","E",
  "Chiplet tiling (Rigetti 12×9 q, 99.1%) and metre-scale l-couplers between modules (IBM Cockatoo 2027 [R]).","Плитка чиплетов (Rigetti 12×9 q, 99.1%) и метровые l-couplers между модулями (IBM Cockatoo 2027 [R]).",
  [("count","chiplet tiling","108 q from 12 chiplets, median 2Q 99.1% (vs 99.5% at 36 q)","2026-04","https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system"),
   ("path","coupled cryogenic cells","two cells coupled; 0.53 m² wiring area each","2026-08","https://www.ibm.com/quantum/blog/modular-cryogenics")],"",""),
N("ic_cryolink",9,"Cryogenic microwave link between refrigerators","Криогенный СВЧ-линк между криостатами",1.0,["fab"],None,"na",None,"longrange","mw","mK",["loss","coherent"],"sclitho","E",
  "30 m superconducting waveguide at < 50 mK; Bell fidelity 80.4% at 12.5 kHz; 0.55–0.65 dB total loss.","30-м сверхпроводящий волновод при < 50 мК; fidelity Bell 80.4% при 12.5 кГц; суммарные потери 0.55–0.65 дБ.",
  [("channel","30 m link Bell fidelity / rate","80.4% / 12.5 kHz","2023-05","https://www.nature.com/articles/s41586-023-05885-0"),
   ("path","2026 modular link","waveguide loss < 0.03 dB/30 m; end-to-end transfer loss 0.55–0.65 dB, i.e. 86–88% transmission","2026-04","https://arxiv.org/html/2604.15971v1")],
  "ETH Zürich. A '75–79% transfer efficiency' sometimes quoted is not implied by 0.55–0.65 dB, which is 86–88% transmission; the ETH paper attributes the loss to the 26 demountable module joints, and any residue would be node emission/absorption efficiency.","ETH Zürich. Иногда цитируемая «эффективность передачи 75–79%» не следует из 0.55–0.65 дБ, что соответствует пропусканию 86–88%; статья ETH относит потери к 26 разъёмным стыкам модулей, а остаток пришёлся бы на эффективность излучения/поглощения в узлах."),
N("ic_ionphoton",9,"Ion–photon photonic link","Ион-фотонный фотонный линк",0.0,["nat"],None,"na",None,"flying","opt","RT",["loss"],"optics","D",
  "Remote Bell pairs at 9.7–250 s⁻¹ with 94–97% fidelity; teleported CZ 86%; needs ≥ 10⁴ s⁻¹.","Удалённые пары Белла при 9.7–250 с⁻¹ с fidelity 94–97%; телепортированный CZ 86%; нужно ≥ 10⁴ с⁻¹.",
  [("channel","distributed CZ (Oxford)","remote Bell 96.9% at 9.7 s⁻¹; teleported CZ 86.2%","2025-02","https://www.nature.com/articles/s41586-024-08404-x"),
   ("clock","entanglement rate record","250 s⁻¹ at F > 94%","2024","https://arxiv.org/abs/2404.16167")],
  "The 2007 first remote ion–ion entanglement is Monroe's group (Michigan, later Maryland/Duke) — the lineage holding today's rate record — not the Wineland/NIST line. IonQ's 2026-04 interconnect milestone discloses no rate, fidelity or distance and asserts no measured Bell state.","Первая удалённая запутанность ион–ион 2007 года — группа Monroe (Michigan, позже Maryland/Duke), та же линия, что держит нынешний рекорд скорости, а не линия Wineland/NIST. В сообщении IonQ от 2026-04 не раскрыты ни скорость, ни fidelity, ни расстояние и не заявлено измеренное состояние Белла."),
N("ic_atomcavity",9,"Atom–photon cavity interface","Атом-фотонный интерфейс через резонатор",0.0,["nat"],None,"na",None,"flying","opt","RT",["loss"],"optics","E",
  "Tweezer atoms coupled to cavities: ~90% generation-to-detection atom–photon efficiency (MPQ); no inter-module rates yet.","Атомы в пинцетах, связанные с резонаторами: ~90% эффективность атом–фотон от генерации до детектирования (MPQ); межмодульных скоростей пока нет.",
  [("channel","atom–photon efficiency (MPQ, Science 385, 179)","~90% generation-to-detection","2024-07","https://arxiv.org/abs/2407.09109")],
  "Atom Computing–Nu Quantum/Cisco (MoUs, no numbers). A 'cavity-carved Bell fidelity 91%' sometimes quoted is not in the source abstract. Nu Quantum's $60 M Series A closed 2025-12-10, led by National Grid Partners.","Atom Computing–Nu Quantum/Cisco (меморандумы, без чисел). Иногда цитируемая «fidelity Bell 91% через cavity-carving» отсутствует в аннотации источника. Series A Nu Quantum на $60 млн закрыт 2025-12-10 во главе с National Grid Partners."),
N("ic_spinphoton",9,"Spin–photon solid-state link (SiV, NV, T-centre)","Спин-фотонный твердотельный линк (SiV, NV, T-центр)",0.5,["int"],None,"na",None,"flying","opt","RT",["loss"],"diamond","D",
  "Entanglement over 25–35 km deployed fibre at 0.02–1 Hz with F 0.53–0.86; two distinct inter-cryostat teleported-CNOT results — post-selected on T centres (Photonic Inc.) and unconditional on NV (QuTech).","Запутанность на 25–35 км проложенного волокна при 0.02–1 Гц с F 0.53–0.86; два разных результата по телепортированному CNOT между криостатами — постселектированный на T-центрах (Photonic Inc.) и безусловный на NV (QuTech).",
  [("channel","SiV over 35 km","F = 0.69, ≤ 1 Hz","2024-05","https://www.nature.com/articles/s41586-024-07252-z"),
   ("channel","NV Delft–The Hague 25 km","F = 0.534, 0.022 s⁻¹","2024-04","https://arxiv.org/html/2404.03723"),
   ("channel","T-centre inter-cryostat link (Photonic Inc.)","Bell F = 0.60(8) at 7.5 mHz; teleported-CNOT sequence post-selected, no gate fidelity","2024-06","https://arxiv.org/html/2406.01704v1"),
   ("channel","NV unconditional teleported CNOT (QuTech)","63(4)% (4-qubit GHZ 64(4)%), real-time feed-forward, no post-selection","2026-05","https://www.nature.com/articles/s41467-026-72818-6")],
  "Both results exist and differ in kind: Photonic Inc.'s 2024 T-centre demonstration is a post-selected preprint with a truth table rather than a gate fidelity; QuTech's 2026 NV result is unconditional. Quoting them together without that distinction overstates the T-centre platform.","Оба результата существуют и различаются по природе: демонстрация Photonic Inc. на T-центрах (2024) — постселектированный препринт с таблицей истинности вместо fidelity гейта; результат QuTech на NV (2026) — безусловный. Совместное цитирование без этого различия завышает оценку платформы на T-центрах."),
N("ic_transducer",9,"Microwave–optical transducer (useful efficiency)","СВЧ-оптический трансдьюсер (полезной эффективности)",1.0,["fab"],None,"na",None,"flying","eo","mK",["loss"],"pic","X",
  "Best: η_tot 15%, N_add 0.16 (EO); useful regime needs η > 1/2 and N_add ≪ 1; ~3 orders of magnitude short (IBM analysis).","Лучшее: η_tot 15%, N_add 0.16 (EO); полезный режим требует η > 1/2 и N_add ≪ 1; ~3 порядка не хватает (анализ IBM).",
  [("channel","state of the art (review)","η_int 99.5%, η_tot 15%, N_add 0.16 (EO, 60 mK)","2026-05","https://arxiv.org/html/2605.26976"),
   ("path","gap to useful","3 orders of magnitude (noise, η, rate) for 99.7% remote gates at MHz","2025-03","https://arxiv.org/abs/2503.10842")],"",""),
N("ic_fibre",9,"Fibre links between photonic modules","Волоконные линки между фотонными модулями",0.25,["pho"],None,"na",None,"flying","eo","RT",["loss"],"pic","D",
  "Chip-to-chip Bell 99.72% over 42 m (loss excluded); Aurora inter-rack fibre.","Межчиповые пары Белла 99.72% на 42 м (без учёта потерь); межстоечное волокно Aurora.",
  [("channel","chip-to-chip Bell fidelity","99.72% over 42 m, conditional on heralded events (channel loss excluded)","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "Facet coupling is quoted on two different bases: Xanadu 0.085 dB/facet [C] against PsiQuantum's published 52(12) mdB [D] for the same interface.","Стыковка на торце приводится на двух разных основаниях: 0.085 дБ/торец у Xanadu [C] против опубликованных 52(12) мдБ у PsiQuantum [D] для того же интерфейса."),
]
# ---------------------------------------------------------------- L10 MANUFACTURING
NODES += [
N("fab_cmos",10,"300 mm CMOS foundry (spins, cryo-CMOS, SC wiring)","CMOS-фабрика 300 мм (спины, cryo-CMOS, SC-разводка)",1.0,["fab"],None,"na",None,"none","none","none",["coherent"],"cmos","D",
  "Intel D1 EUV (24k devices/wafer, 96% tune-up), imec (2Q > 99%), GF 22FDX (1,024 dots), ST FD-SOI; GF now a multi-modality foundry ($375 M LOI).","Intel D1 EUV (24 тыс. устройств/пластина, 96% выход), imec (2Q > 99%), GF 22FDX (1 024 точки), ST FD-SOI; GF — многомодальная фабрика ($375 млн LOI).",
  [("path","wafer-scale statistics","> 24,000 devices/wafer, 96% single-electron tune-up, CD < 0.5 nm","2024-10","https://arxiv.org/abs/2410.16583"),
   ("path","multi-modality foundry LOI","GlobalFoundries $375 M (SC, ion, photonic, topological, spin)","2026-05","https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion")],"",""),
N("fab_sc",10,"Superconducting-qubit lithography (Nb/Al JJ, 300 mm)","Литография сверхпроводниковых кубитов (Nb/Al JJ, 300 мм)",1.0,["fab"],None,"na",None,"none","none","none",["coherent"],"sclitho","D",
  "IBM Albany 300 mm / Anderon foundry; Google Santa Barbara; Rigetti ABAA trimming (97.4% frequency-targeting success); OQC 500-qubit wafer-scale package.","IBM Albany 300 мм / фабрика Anderon; Google Santa Barbara; Rigetti ABAA-подстройка (97.4% попаданий в частоту); OQC — 500-кубитная пластинная упаковка.",
  [("path","junction frequency targeting (ABAA)","97.4% success, 0.9 ± 2.4% of prediction","2024-08","https://www.nature.com/articles/s43246-024-00596-z"),
   ("count","wafer-scale package (OQC)","> 500 qubits on one 3-inch sapphire die; T1 ~97 µs, T2e ~129 µs; no per-qubit control lines in the measured configuration","2026-02","https://arxiv.org/abs/2602.12773"),
   ("path","Anderon foundry","$1 B CHIPS + $1 B IBM; SC wiring/TSV/bump; 30× device output vs 200 mm","2026-05","https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding")],
  "The OQC package is on 3-inch sapphire and its coherence is reported as T1 ~97 µs and T2e ~129 µs separately, not as a '~100 µs median' for both; it is a packaging result, not a processor.","Сборка OQC выполнена на 3-дюймовом сапфире, а когерентность приводится раздельно как T1 ~97 мкс и T2e ~129 мкс, а не как «медиана ~100 мкс» для обеих величин; это результат по упаковке, а не по процессору."),
N("fab_3d",10,"3D machined superconducting cavities","3D-обработанные сверхпроводящие полости",1.0,["fab"],None,"na",None,"none","none","none",["loss"],"3d","D",
  "Aluminium/niobium cavities with Q > 10⁹; cm-scale footprint per qubit — the scaling liability of cavity-based bosonic codes.","Алюминиевые/ниобиевые полости с Q > 10⁹; сантиметровая площадь на кубит — масштабная обуза полостных бозонных кодов.",
  [("channel","cavity Q (Al, Yale)","> 0.5×10⁹, single-photon lifetime 10 ms","2013","https://arxiv.org/abs/1302.4408")],
  "The 25.6 ms / 34 ms coherence figures are Weizmann (PRX Quantum 4, 030336), and neither the abstract nor the journal summary states the cavity material — 'Nb-coated' is unsupported.","Значения когерентности 25.6 мс / 34 мс — Weizmann (PRX Quantum 4, 030336); ни аннотация, ни резюме журнала не указывают материал полости — «покрытие Nb» не подтверждено."),
N("fab_trap",10,"Surface-electrode ion-trap microfabrication","Микроизготовление поверхностных ионных ловушек",0.0,["nat"],None,"na",None,"none","none","none",["coherent"],"mems","D",
  "MEMS/CMOS-fab traps: Helios 1,228 electrodes / 273 signals; Oxford Ionics chips from standard semiconductor fabs; SkyWater in-house at IonQ.","MEMS/CMOS-ловушки: Helios 1 228 электродов / 273 сигнала; чипы Oxford Ionics с обычных полупроводниковых фабрик; SkyWater внутри IonQ.",
  [("path","Helios trap","1,228 electrodes, 273 independent signals (2.8 per qubit)","2025-11","https://arxiv.org/html/2511.05465"),
   ("path","standard-fab traps","99.99% 2Q on chips from standard semiconductor fabs","2025-10","https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing")],"",""),
N("fab_pic",10,"Photonic IC foundry (SiN, BTO, TFLN, SNSPD on 300 mm)","PIC-фабрика (SiN, BTO, TFLN, SNSPD на 300 мм)",0.25,["pho"],None,"na",None,"none","none","none",["loss"],"pic","D",
  "GlobalFoundries Fab 8 for PsiQuantum (SiN 0.5 dB/m multimode but 1.8(2) dB/m single-mode, BTO switches, on-chip SNSPD at 93.4% median); TFLN/SiN for Xanadu; also ion integrated photonics and atom PIC traps.","GlobalFoundries Fab 8 для PsiQuantum (SiN 0.5 дБ/м многомодовый, но 1.8(2) дБ/м одномодовый, BTO-переключатели, SNSPD на чипе с медианой 93.4%); TFLN/SiN для Xanadu; также интегрированная фотоника ионов и PIC-ловушки атомов.",
  [("channel","SiN waveguide loss (multimode)","0.5 dB/m","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","SiN waveguide loss (single-mode)","1.8(2) dB/m","2025-02","https://www.nature.com/articles/s41586-025-08820-7"),
   ("channel","wafer-scale median on-chip SNSPD efficiency","93.4% at ~2 K, 300 mm","2025-02","https://www.nature.com/articles/s41586-025-08820-7")],
  "The 0.5 dB/m figure is multimode; the single-mode Omega number is 1.8(2) dB/m and the two are unreconciled. The 98.9% median SNSPD efficiency sometimes quoted is superseded by 93.4%.","0.5 дБ/м — многомодовое значение; одномодовое значение Omega — 1.8(2) дБ/м, расхождение не устранено. Иногда цитируемая медианная эффективность SNSPD 98.9% вытеснена значением 93.4%."),
N("fab_optics",10,"Optical / mechanical assembly (lasers, vacuum, objectives)","Оптическая / механическая сборка (лазеры, вакуум, объективы)",0.0,["nat"],None,"na",None,"none","none","none",["coherent"],"optics","D",
  "Room-temperature systems: Pasqal Orion 3 kW / 2,500 kg; continuous reload hardware (2 optical-lattice conveyors, 300,000 atoms/s into tweezers → 30,000 initialised qubits/s).","Системы при комнатной температуре: Pasqal Orion 3 кВт / 2 500 кг; аппаратура непрерывной перезагрузки (2 оптических решёточных конвейера, 300 000 атомов/с в пинцеты → 30 000 инициализированных кубитов/с).",
  [("path","system power / mass","3 kW avg, 2,500 kg (Orion Gamma)","2025-11","https://www.pasqal.com/wp-content/uploads/2025/11/2509_Pasqal_Quantum-Computing-Processor_Brochure-RVB-V8.pdf"),
   ("path","continuous reload hardware","300,000 atoms/s reloaded into tweezers; 30,000 initialised qubits/s","2025-09","https://www.nature.com/articles/s41586-025-09596-6")],
  "The two rates are different quantities and both are correct: 300,000 atoms/s is the reload rate into tweezers, 30,000/s the rate of initialised qubits. Long-range transport in that system is by optical-lattice conveyor belts.","Две скорости — разные величины, и обе верны: 300 000 атомов/с — темп перезагрузки в пинцеты, 30 000/с — темп инициализированных кубитов. Дальний транспорт в этой системе выполняют оптические решёточные конвейеры."),
N("fab_mbe",10,"III-V MBE heterostructures (InAs–Pb wires, QD sources)","III-V MBE гетероструктуры (проволоки InAs–Pb, КТ-источники)",0.75,["fab","pho"],None,"na",None,"none","none","none",["unknown"],"mbe","D",
  "In-house Microsoft growth for tetrons (no external replication); GaAs quantum-dot photon sources (Quandela).","Собственный рост Microsoft для тетронов (без внешней репликации); GaAs квантово-точечные источники фотонов (Quandela).",
  [("path","replication","no independent replication of the InAs–Pb stack","2026-06","https://www.nature.com/articles/s41586-026-10567-8")],
  "The 'sevenfold larger gap' claimed for Pb over Al is unsourced. The lineage's founding result — quantized Majorana conductance in InAs–Al, Nature 556 (2018) — was retracted on 2021-03-08. ECCN 3C907 covers epitaxial materials; no ECCN names MBE reactors. QuTech's InSb wires are grown at TU Eindhoven (Bakkers).","Заявленный «в семь раз больший гэп» у Pb по сравнению с Al не подкреплён источником. Основополагающий результат линии — квантованная майорановская проводимость в InAs–Al, Nature 556 (2018) — отозван 2021-03-08. ECCN 3C907 покрывает эпитаксиальные материалы; ни один ECCN не называет MBE-реакторы. Проволоки InSb для QuTech выращивают в TU Eindhoven (группа Bakkers)."),
N("fab_stm",10,"STM hydrogen lithography (donors)","STM-литография (доноры)",0.5,["int"],None,"na",None,"none","none","none",["pauli"],"stm","D",
  "Atom-precise placement of P donors (~3 nm); bespoke, serial, no foundry route.","Атомно-точное размещение доноров P (~3 нм); штучно, последовательно, без фабричного пути.",
  [("count","register size","11 qubits","2025-12","https://www.nature.com/articles/s41586-025-09827-w")],
  "The ~3 nm figure is the incorporated donor's positional uncertainty from segregation and diffusion during encapsulation — the limiting step is thermal, not lithographic; ~1 nm is not supported.","~3 нм — неопределённость положения встроенного донора из-за сегрегации и диффузии при заращивании: ограничивающая стадия термическая, а не литографическая; ~1 нм не подтверждается."),
N("fab_diamond",10,"Diamond growth / implantation (NV, SiV, SnV)","Рост / имплантация алмаза (NV, SiV, SnV)",0.5,["int"],None,"na",None,"none","none","none",["pauli"],"diamond","D",
  "Nanocavity yield: 327 SnV devices with cooperativity > 1 on two chips (QuTech); Quantum Brilliance diamond foundry.","Выход нанорезонаторов: 327 SnV-устройств с кооперативностью > 1 на двух чипах (QuTech); алмазная фабрика Quantum Brilliance.",
  [("path","device yield","327 devices, cooperativity > 1","2026-06","https://qutech.nl/2026/06/25/a-step-toward-faster-quantum-networks/")],
  "Element Six's DNV-B1 (2020) is an NV-*ensemble* sensing grade, not a substrate for single-defect network nodes, which need electronic-grade plates.","DNV-B1 от Element Six (2020) — сенсорный сорт для *ансамблей* NV, а не подложка для сетевых узлов на одиночных дефектах, где нужны пластины электронного качества."),
]
# ---------------------------------------------------------------- extra nodes (added while assembling paths)
NODES += [
N("enc_spin_ld",2,"Single-spin (Loss–DiVincenzo) / nuclear-spin encoding","Кодирование на одиночном спине (Loss–DiVincenzo) / ядерном спине",0.75,["fab","int"],None,"na",None,"none","none","none",["coherent","pauli"],"none","D",
  "Bare spin-1/2 of an electron, hole or nucleus; needs microwave/EDSR for 1Q.","«Голый» спин-1/2 электрона, дырки или ядра; для 1Q нужны СВЧ/EDSR.",[],"",""),
N("g_cv",3,"CV Gaussian gates + GKP-assisted non-Gaussian ops","CV гауссовы гейты + негауссовы операции с помощью GKP",0.25,["pho"],-6.0,"det",None,"flying","eo","RT",["gauss","loss"],"pic","D",
  "Beam-splitters, squeezers and homodyne feed-forward on optical modes at 1 MHz clock (Aurora).","Beam-splitters, сжиматели и гомодинный feed-forward на оптических модах при такте 1 МГц (Aurora).",
  [("clock","Aurora clock","1 MHz, 12 modes per cycle","2025-01","https://www.nature.com/articles/s41586-024-08406-9")],
  "Time-domain-multiplexed CV cluster states originate with Yokoyama et al. (University of Tokyo, 2013, > 10,000 modes); Xanadu's Aurora is the first modular chip-based networked version, not the first such state.","Кластерные CV-состояния с временным мультиплексированием восходят к Yokoyama et al. (University of Tokyo, 2013, > 10 000 мод); Aurora у Xanadu — первая модульная сетевая версия на чипах, а не первое такое состояние."),
N("g_mwspin",3,"Microwave / optical spin gates (defect centres, 1Q spins)","СВЧ / оптические спиновые гейты (центры окраски, 1Q спины)",0.5,["int","fab"],-6.0,"det",None,"static","mw","RT",["pauli","coherent"],"diamond","D",
  "ESR/EDSR-driven rotations and hyperfine-conditional gates; < 0.1% error on NV electron+nuclear registers.","Вращения на ESR/EDSR и сверхтонко-условные гейты; ошибка < 0.1% на регистрах NV электрон+ядро.",
  [("channel","NV 1Q/2Q (GST)","< 0.1% [P] — press release only, no primary paper","2025-03","https://thequantuminsider.com/2025/03/28/fujitsu-and-qutech-realize-high-precision-quantum-gates/")],
  "The Fujitsu/QuTech '< 0.1%' figure exists only as a press release [P]; no primary paper has been located.","Значение «< 0.1%» от Fujitsu/QuTech существует только в виде пресс-релиза [P]; первичная статья не найдена."),
N("g_catcnot",3,"Bias-preserving cat–cat CNOT","Bias-сохраняющий CNOT кошка–кошка",1.0,["fab"],None,"det",None,"bus","mw","RT",["bias"],"sclitho","X",
  "Required by every cat-qubit resource estimate; only a July-2026 theory proposal exists.","Требуется каждой оценкой ресурсов для кошачьих кубитов; существует только теоретическое предложение июля 2026.",
  [("channel","status","no experimental bias-preserving cat–cat CNOT","2026-07","https://arxiv.org/abs/2607.22852")],"",""),
N("src_resource",3,"Multi-photon resource-state factory (6-ring etc.)","Фабрика многофотонных ресурсных состояний (6-ring и т.п.)",0.25,["pho"],None,"her",None,"flying","eo","RT",["loss"],"pic","X",
  "Fusion-based FT needs 24–168-photon encoded resource states at high rate; largest fused deterministic-emitter graph states are 8 photons at < 1 Hz.","Fusion-based FT нужны кодированные ресурсные состояния из 24–168 фотонов с высокой скоростью; крупнейшие слитые графовые состояния — 8 фотонов при < 1 Гц.",
  [("count","largest emitter-fused graph state","8 qubits, 0.4–2.3 coincidences/min","2024-05","https://www.nature.com/articles/s41586-024-07357-5"),
   ("count","independent emitter graph states (C2N Paris-Saclay)","reconfigurable 4-photon graph states from one quantum dot, ~0.5 Hz","2025-05","https://www.nature.com/articles/s41467-025-59693-3")],
  "Quandela's Lucy was delivered to CEA in 2025-10 and launched on the Joliot-Curie HPC system on 2026-04-14 — delivery and integration, two dates for two events.","Lucy у Quandela поставлена в CEA в 2025-10 и запущена на HPC-системе Joliot-Curie 2026-04-14 — поставка и интеграция, две даты для двух событий."),
N("ct_eo",5,"Electro-optic drive + feed-forward electronics (RT)","Электрооптическое управление + feed-forward электроника (комн. т.)",0.25,["pho"],None,"na",None,"none","eo","RT",["loss"],"pic","D",
  "MHz–GHz switching of BTO/TFLN modulators conditioned on detector outcomes within one clock cycle.","МГц–ГГц переключение BTO/TFLN-модуляторов по результатам детекторов в пределах одного такта.",
  [("clock","single-clock-cycle feed-forward","1 MHz (Aurora)","2025-01","https://www.nature.com/articles/s41586-024-08406-9")],"",""),
N("ro_imgfast",6,"Fast (≤ 20 µs) atom-array readout","Быстрое (≤ 20 мкс) считывание массивов атомов",0.0,["nat"],None,"na",C("img",-4.75,False,True),"none","opt","RT",["loss"],"optics","E",
  "Neutral-Yb imaging in 17.6 µs at 99.89% discrimination / 98.8% survival (Kyoto); cuts the imaging term 30–50×, but the whole QEC round improves only ~2× — transport and the camera link remain.","Imaging нейтрального Yb за 17.6 мкс при 99.89% различения / 98.8% выживания (Kyoto); сокращает вклад imaging в 30–50 раз, но весь раунд QEC улучшается лишь ~в 2 раза — остаются транспорт и канал камеры.",
  [("clock","fast imaging","17.6 µs, 99.89%, survival 98.8% — neutral ¹⁷⁴Yb, spinless","2026-08","https://arxiv.org/html/2605.24175")],
  "The 30–50× applies to the imaging term alone (Amdahl): a 1–4.5 ms round is imaging plus transport plus a 442 µs camera-to-server transfer, so the round improves ~2×. The 'suppression vanished once reloading was included' result belongs to Atom Computing's toric code (arXiv:2606.04079), not to the Harvard 448-atom processor.","Множитель 30–50 относится только к вкладу imaging (закон Амдала): раунд в 1–4.5 мс складывается из imaging, транспорта и передачи кадра камера-сервер за 442 мкс, поэтому раунд улучшается ~в 2 раза. Результат «подавление исчезло, как только включили перезагрузку» относится к торическому коду Atom Computing (arXiv:2606.04079), а не к 448-атомному процессору Harvard."),
]
SINCE={'transmon': 2007, 'fluxonium': 2009, 'cavity': 2013, 'ion': 1995, 'alkali': 2016, 'ae_atom': 2019, 'photon': 2001, 'squeezed': 2012, 'qd_spin': 2012, 'donor': 2012, 'defect': 2004, 'majorana': 2025, 'fluxq': 2011, 'enc_bare': 2007, 'enc_hf': 1995, 'enc_omg': 2023, 'enc_dualrail': 2023, 'enc_cat': 2020, 'enc_gkp': 2020, 'enc_eo': 2013, 'enc_timebin': 1999, 'enc_parity': 2025, 'enc_spin_ld': 1998, 'g_tc': 2014, 'g_cr': 2011, 'g_ryd': 2010, 'g_ms': 2003, 'g_elec': 2024, 'g_exch': 2018, 'g_fusion': 2005, 'g_bos': 2018, 'g_mbq': 2030, 'g_anneal': 2011, 'g_cv': 2020, 'g_mwspin': 2004, 'g_catcnot': 2030, 'src_resource': 2030, 'cx_nn': 2014, 'cx_lr': 2023, 'cx_qccd': 2002, 'cx_bus': 2003, 'cx_aod': 2022, 'cx_shuttle': 2025, 'cx_switch': 2015, 'cx_crossbar': 2023, 'ct_rt': 2007, 'ct_cryocmos': 2024, 'ct_sfq': 2026, 'ct_fluxdac': 2026, 'ct_laser': 2016, 'ct_pic_trap': 2026, 'ct_ionlaser': 2020, 'ct_ionmw': 2024, 'ct_base': 2012, 'ct_eo': 2020, 'ro_disp': 2005, 'ro_fluor': 1995, 'ro_img': 2016, 'ro_s2c': 2004, 'ro_spd': 2001, 'ro_qcap': 2025, 'ro_erasure': 2023, 'ro_imgfast': 2026, 'code_surface': 2023, 'code_color': 2024, 'code_qldpc': 2025, 'code_highrate': 2024, 'code_erasure': 2025, 'code_bosonic': 2024, 'code_fusion': 2030, 'code_aft': 2025, 'code_magic': 2025, 'dec_mwpm': 2015, 'dec_nn': 2024, 'dec_relaybp': 2025, 'dec_fpga': 2025, 'dec_gpu': 2025, 'dec_corr': 2025, 'dec_rl': 2026, 'dec_cryo': 2030, 'ic_mcm': 2025, 'ic_cryolink': 2020, 'ic_ionphoton': 2007, 'ic_atomcavity': 2024, 'ic_spinphoton': 2013, 'ic_transducer': 2030, 'ic_fibre': 2025, 'fab_cmos': 2022, 'fab_sc': 2007, 'fab_3d': 2013, 'fab_trap': 2006, 'fab_pic': 2015, 'fab_optics': 2016, 'fab_mbe': 2018, 'fab_stm': 2012, 'fab_diamond': 2010}
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
P("sc","Superconducting transmon","Сверхпроводниковый трансмон","SC","fab",
  {1:["transmon","fluxonium"],2:["enc_bare"],3:["g_tc","g_cr"],4:["cx_nn","cx_lr"],5:["ct_rt","ct_cryocmos","ct_sfq"],6:["ro_disp"],7:["code_surface","code_color","code_qldpc","code_magic"],8:["dec_nn","dec_mwpm","dec_fpga","dec_relaybp","dec_rl","dec_gpu"],9:["ic_mcm","ic_cryolink","ic_transducer"],10:["fab_sc","fab_cmos"]},
  "Google, IBM, Rigetti, IQM, OQC, USTC/Zhejiang, Fujitsu","1.1 µs (Willow QEC cycle)","G2 G3 G4"),
P("cat","Superconducting bosonic (cat / GKP)","Сверхпроводниковые бозонные (кошки / GKP)","SC","fab",
  {1:["cavity"],2:["enc_cat","enc_gkp"],3:["g_bos","g_catcnot"],4:["cx_nn"],5:["ct_rt"],6:["ro_disp"],7:["code_bosonic"],8:["dec_mwpm"],9:["ic_mcm"],10:["fab_sc","fab_3d"]},
  "Alice & Bob, AWS, Nord Quantique","2.8 µs (Ocelot cycle)","G3 G4"),
P("dualrail","Superconducting dual-rail erasure","Сверхпроводниковые dual-rail erasure","SC","fab",
  {1:["cavity","transmon"],2:["enc_dualrail"],3:["g_bos"],4:["cx_nn"],5:["ct_rt"],6:["ro_erasure","ro_disp"],7:["code_erasure"],8:["dec_mwpm"],9:["ic_mcm"],10:["fab_3d","fab_sc"]},
  "D-Wave/QCI, AWS, SUSTech","~2 µs (CZ 500 ns + 384 ns check)","G3 G4"),
P("ion_qccd","Trapped ions — QCCD, laser gates","Ионы — QCCD, лазерные гейты","ION","nat",
  {1:["ion"],2:["enc_hf"],3:["g_ms"],4:["cx_qccd"],5:["ct_ionlaser"],6:["ro_fluor"],7:["code_highrate","code_color","code_magic"],8:["dec_gpu","dec_mwpm"],9:["ic_ionphoton"],10:["fab_trap","fab_optics"]},
  "Quantinuum, AQT","~1–5 ms syndrome cycle; 55 ms per full layer (Helios)","G2 G3 G6 G7"),
P("ion_elec","Trapped ions — electronic gates, chip control","Ионы — электронные гейты, управление с чипа","ION","nat",
  {1:["ion"],2:["enc_hf","enc_omg"],3:["g_elec","g_ms"],4:["cx_bus","cx_qccd"],5:["ct_ionmw"],6:["ro_fluor"],7:["code_qldpc","code_highrate"],8:["dec_relaybp","dec_mwpm"],9:["ic_ionphoton"],10:["fab_trap","fab_cmos"]},
  "IonQ / Oxford Ionics, eleQtron, Quantum Art","~1–5 ms (IonQ decoder assumption)","G2 G3 G6 G7"),
P("atom_rb","Neutral atoms — alkali (Rb/Cs)","Нейтральные атомы — щелочные (Rb/Cs)","ATOM","nat",
  {1:["alkali"],2:["enc_hf"],3:["g_ryd"],4:["cx_aod"],5:["ct_laser","ct_pic_trap"],6:["ro_img","ro_imgfast"],7:["code_highrate","code_surface","code_color","code_aft","code_magic"],8:["dec_corr","dec_nn","dec_gpu"],9:["ic_atomcavity"],10:["fab_optics"]},
  "Harvard/MIT, QuEra, Pasqal, Infleqtion, Google (2026)","~1–4.5 ms per QEC round","G1 G3 G7"),
P("atom_ae","Neutral atoms — alkaline-earth (Yb/Sr), erasure-native","Нейтральные атомы — щёлочноземельные (Yb/Sr), erasure-нативные","ATOM","nat",
  {1:["ae_atom"],2:["enc_omg","enc_hf"],3:["g_ryd"],4:["cx_aod"],5:["ct_laser"],6:["ro_img","ro_erasure","ro_imgfast"],7:["code_erasure","code_surface"],8:["dec_corr"],9:["ic_atomcavity"],10:["fab_optics"]},
  "Atom Computing/Microsoft, Princeton, Caltech","~1–4 ms","G1 G3 G7"),
P("ph_fusion","Photonic — fusion-based (DV)","Фотоника — fusion-based (DV)","PHOTON","pho",
  {1:["photon"],2:["enc_timebin","enc_dualrail"],3:["g_fusion","src_resource"],4:["cx_switch"],5:["ct_eo"],6:["ro_spd"],7:["code_fusion"],8:["dec_mwpm"],9:["ic_fibre"],10:["fab_pic"]},
  "PsiQuantum, Quandela, QuiX","MHz–GHz by design; no logical cycle","G4 G6"),
P("ph_cv","Photonic — continuous-variable / GKP","Фотоника — непрерывные переменные / GKP","PHOTON","pho",
  {1:["squeezed"],2:["enc_gkp"],3:["g_cv","g_fusion"],4:["cx_switch"],5:["ct_eo"],6:["ro_spd"],7:["code_bosonic"],8:["dec_relaybp","dec_mwpm"],9:["ic_fibre"],10:["fab_pic"]},
  "Xanadu","1 MHz clock (Aurora); no logical cycle","G4 G6"),
P("spin_qd","Silicon / germanium quantum-dot spins","Кремниевые / германиевые спины в квантовых точках","SPIN","fab",
  {1:["qd_spin"],2:["enc_eo","enc_spin_ld"],3:["g_exch"],4:["cx_nn","cx_shuttle","cx_crossbar"],5:["ct_base","ct_cryocmos"],6:["ro_s2c"],7:["code_surface"],8:["dec_mwpm"],9:[],10:["fab_cmos"]},
  "Intel, Diraq, Quantum Motion, HRL→IBM, QuTech/Groove, Quobly, Equal1","~100 µs – 300 µs (readout-limited)","G4 G7"),
P("spin_donor","Donor spins in silicon","Донорные спины в кремнии","SPIN","int",
  {1:["donor"],2:["enc_spin_ld"],3:["g_exch"],4:["cx_nn"],5:["ct_base"],6:["ro_s2c"],7:["code_surface"],8:["dec_mwpm"],9:[],10:["fab_stm"]},
  "SQC","~ms (nuclear-spin gates µs, readout 100 µs)","G7"),
P("defect","Defect-spin network nodes (NV/SiV/T)","Узлы сети на дефектных спинах (NV/SiV/T)","DEFECT","int",
  {1:["defect"],2:["enc_spin_ld"],3:["g_mwspin"],4:["cx_nn"],5:["ct_base"],6:["ro_fluor"],7:[],8:[],9:["ic_spinphoton"],10:["fab_diamond"]},
  "QuTech/Fujitsu, Harvard, Photonic Inc, Quantum Brilliance","n/a (network node)","G6"),
P("topo","Topological (Majorana)","Топологические (майорановские)","TOPO","fab",
  {1:["majorana"],2:["enc_parity"],3:["g_mbq"],4:["cx_nn"],5:["ct_base"],6:["ro_qcap"],7:[],8:[],9:[],10:["fab_mbe"]},
  "Microsoft","n/a (no qubit)","—"),
P("anneal","Quantum annealing","Квантовый отжиг","ANNEAL","fab",
  {1:["fluxq"],2:[],3:["g_anneal"],4:["cx_lr"],5:["ct_fluxdac"],6:["ro_disp"],7:[],8:[],9:[],10:["fab_sc"]},
  "D-Wave","µs–ms anneal; 3.6–27 ns quenches","G1 G5"),
]
# ---------------------------------------------------------------- EDGES
def E(t,a,b,en,ru): return dict(type=t,src=a,dst=b,en=en,ru=ru)
EDGES=[]
REQ=[
("g_tc","transmon","flux-tunable coupler between transmons","перестраиваемый coupler между трансмонами"),
("g_cr","transmon","fixed-frequency transmons","трансмоны фиксированной частоты"),
("g_ryd","alkali","Rydberg excitation of the atom","ридберговское возбуждение атома"),("g_ryd","ae_atom","Rydberg excitation of the atom","ридберговское возбуждение атома"),
("g_ryd","ct_laser","Rydberg lasers, global pulses","ридберговские лазеры, глобальные импульсы"),
("g_ms","ion","spin–motion coupling","связь спин–движение"),("g_ms","ct_ionlaser","laser fields","лазерные поля"),
("g_elec","ion","chip currents act on the ion","токи чипа действуют на ион"),("g_elec","ct_ionmw","electronic signal sources","электронные источники сигнала"),
("g_exch","qd_spin","exchange between dots","обмен между точками"),("g_exch","donor","exchange between donors","обмен между донорами"),("g_exch","ct_base","voltage pulses on gates","импульсы напряжения на затворах"),
("g_fusion","photon","photons to fuse","фотоны для fusion"),("g_fusion","ro_spd","heralding detection","heralded детекция"),("g_fusion","cx_switch","feed-forward routing","маршрутизация feed-forward"),
("g_cv","squeezed","squeezed modes","сжатые моды"),("g_cv","ct_eo","homodyne feed-forward","гомодинный feed-forward"),
("g_bos","cavity","bosonic modes","бозонные моды"),("g_bos","transmon","ancilla transmon","анцилла-трансмон"),
("g_catcnot","enc_cat","two cat qubits","два кошачьих кубита"),
("g_mbq","majorana","Majorana wires","майорановские проволоки"),("g_mbq","ro_qcap","measurement-based","через измерения"),
("g_mwspin","defect","spin register","спиновый регистр"),
("src_resource","g_fusion","fusions build the resource state","fusions строят ресурсное состояние"),("src_resource","photon","deterministic or multiplexed photons","детерминированные или мультиплексированные фотоны"),
("enc_cat","cavity","two-photon dissipation on a mode","двухфотонная диссипация на моде"),("enc_gkp","cavity","microwave GKP","СВЧ GKP"),("enc_gkp","squeezed","optical GKP needs ~10 dB squeezing","оптический GKP требует ~10 дБ сжатия"),
("enc_dualrail","ro_erasure","erasure check","проверка erasure"),("enc_omg","ae_atom","metastable manifold","метастабильное многообразие"),("enc_omg","ion","metastable ion levels","метастабильные уровни иона"),
("enc_eo","qd_spin","three-dot encoded qubit","кубит на трёх точках"),("enc_timebin","photon","photonic modes","фотонные моды"),("enc_parity","majorana","two wires per tetron","две проволоки на тетрон"),("enc_bare","transmon","anharmonic subspace","ангармоническое подпространство"),
("cx_qccd","ion","ions to move","перемещаемые ионы"),("cx_qccd","fab_trap","junction / grid traps","ловушки с перекрёстками / решётчатые"),
("cx_aod","ct_laser","AOD deflectors","AOD-дефлекторы"),("cx_shuttle","qd_spin","spins to move","переносимые спины"),("cx_shuttle","fab_cmos","uniform conveyor gates","однородные конвейерные затворы"),
("cx_lr","fab_sc","multilayer routing","многослойная разводка"),("cx_switch","fab_pic","low-loss switches","переключатели с малыми потерями"),("cx_crossbar","qd_spin","dot array","массив точек"),
("ct_sfq","fab_sc","flip-chip SFQ MCM","flip-chip SFQ MCM"),("ct_cryocmos","fab_cmos","cryo ASIC","крио-ASIC"),("ct_fluxdac","fab_sc","on-chip SFQ DACs","on-chip SFQ DAC"),
("ct_pic_trap","fab_pic","photonic chip","фотонный чип"),("ct_ionlaser","fab_pic","integrated waveguides","интегрированные волноводы"),("ct_ionmw","fab_trap","current traces in the trap","токовые дорожки в ловушке"),("ct_eo","fab_pic","modulators","модуляторы"),
("ro_disp","transmon","dispersive shift","дисперсионный сдвиг"),("ro_disp","cavity","ancilla-mediated readout","считывание через анциллу"),
("ro_fluor","ion","cycling transition","циклический переход"),("ro_fluor","defect","optical readout of the spin","оптическое считывание спина"),
("ro_img","alkali","imaging transition","переход для imaging"),("ro_img","ae_atom","imaging transition","переход для imaging"),("ro_imgfast","ae_atom","Yb fast imaging","быстрый imaging Yb"),
("ro_s2c","qd_spin","charge sensor","зарядовый сенсор"),("ro_s2c","donor","charge sensor","зарядовый сенсор"),("ro_spd","photon","detection","детекция"),("ro_qcap","majorana","quantum capacitance","квантовая ёмкость"),
("ro_erasure","enc_dualrail","erasure-detectable encoding","erasure-детектируемое кодирование"),("ro_erasure","enc_omg","erasure-detectable encoding","erasure-детектируемое кодирование"),
("code_surface","cx_nn","2D nearest-neighbour checks","2D-проверки ближайших соседей"),("code_color","cx_nn","2D checks","2D-проверки"),
("code_qldpc","cx_lr","degree-6 long-range checks","дальние проверки степени 6"),("code_qldpc","cx_qccd","long-range via transport","дальние связи через транспорт"),("code_qldpc","cx_bus","all-to-all in chain","all-to-all в цепочке"),("code_qldpc","cx_aod","long-range via transport","дальние связи через транспорт"),
("code_highrate","cx_aod","transversal blocks by transport","трансверсальные блоки через транспорт"),("code_highrate","cx_qccd","all-to-all via QCCD","all-to-all через QCCD"),("code_highrate","cx_bus","all-to-all in chain","all-to-all в цепочке"),
("code_erasure","ro_erasure","erasure flags","флаги erasure"),("code_erasure","dec_corr","erasure-/loss-aware decoding (flags are useless to a plain matcher)","декодирование с учётом стирания/потерь (плоскому matching флаги бесполезны)"),("code_bosonic","enc_cat","biased inner qubit","смещённый внутренний кубит"),("code_bosonic","enc_gkp","GKP inner qubit","внутренний GKP-кубит"),
("code_fusion","g_fusion","fusion measurements","fusion-измерения"),("code_fusion","src_resource","resource states","ресурсные состояния"),
("code_aft","cx_aod","transversal gates by transport","трансверсальные гейты через транспорт"),("code_aft","cx_qccd","transversal gates by ion shuttling (Quantinuum tesseract on ions)","трансверсальные гейты через транспорт ионов (тессеракт Quantinuum на ионах)"),("code_aft","dec_corr","correlated decoding","коррелированное декодирование"),
("code_magic","code_surface","host code","код-носитель"),("code_magic","code_color","host code","код-носитель"),
("dec_relaybp","code_qldpc","qLDPC syndromes","синдромы qLDPC"),("dec_corr","code_highrate","transversal circuits","трансверсальные схемы"),("dec_rl","dec_nn","decoder in the loop","декодер в контуре"),
("dec_cryo","ct_sfq","cold digital logic","холодная цифровая логика"),("dec_cryo","ct_cryocmos","cold digital logic","холодная цифровая логика"),
("ct_fluxdac","ct_sfq","the flux DAC is an SFQ circuit: flux-storage loops loaded one flux quantum at a time by SFQ pulses (D-Wave, since 2010)","flux-DAC — это SFQ-схема: петли хранения потока, заполняемые по одному кванту SFQ-импульсами (D-Wave, с 2010)"),("dec_fpga","code_surface","matching/clustering on surface syndromes","matching/кластеризация на синдромах surface"),("dec_nn","code_surface","trained on surface-code syndromes","обучен на синдромах surface code"),
("ic_mcm","fab_sc","chiplets, couplers","чиплеты, couplers"),("ic_cryolink","fab_sc","superconducting waveguide","сверхпроводящий волновод"),
("ic_ionphoton","ion","ion–photon entanglement","запутанность ион–фотон"),("ic_ionphoton","ro_spd","photon detection","детекция фотонов"),
("ic_atomcavity","alkali","cavity-coupled atoms","атомы в резонаторе"),("ic_atomcavity","ae_atom","cavity-coupled atoms","атомы в резонаторе"),("ic_atomcavity","fab_optics","cavities","резонаторы"),
("ic_spinphoton","defect","spin–photon interface","спин-фотонный интерфейс"),("ic_spinphoton","ro_spd","photon detection","детекция фотонов"),
("ic_transducer","fab_pic","electro-optic / optomechanical chip","электрооптический / оптомеханический чип"),("ic_transducer","ro_spd","heralded entanglement through the transducer needs single-photon detection","геральдированная запутанность через трансдьюсер невозможна без детектора одиночных фотонов"),("ic_transducer","transmon","microwave qubit","СВЧ-кубит"),("ic_fibre","fab_pic","chip-to-fibre coupling","стыковка чип–волокно"),
("transmon","fab_sc","JJ lithography","литография JJ"),("fluxonium","fab_sc","JJ arrays","массивы JJ"),("cavity","fab_3d","machined cavities","обработанные полости"),("fluxq","fab_sc","annealer fab","производство отжигателей"),
("ion","fab_trap","surface-electrode trap","поверхностная ловушка"),("ion","fab_optics","lasers, vacuum","лазеры, вакуум"),("alkali","fab_optics","tweezers, vacuum","пинцеты, вакуум"),("ae_atom","fab_optics","tweezers, clock lasers","пинцеты, часовые лазеры"),
("photon","fab_pic","sources, waveguides","источники, волноводы"),("squeezed","fab_pic","squeezers","сжиматели"),("qd_spin","fab_cmos","300 mm dots","точки на 300 мм"),("donor","fab_stm","STM placement","размещение STM"),("defect","fab_diamond","host crystal","кристалл-матрица"),("majorana","fab_mbe","InAs–Pb stack","стек InAs–Pb"),
]
ANY={("g_ryd","alkali"),("g_ryd","ae_atom"),("g_exch","qd_spin"),("g_exch","donor"),("enc_gkp","cavity"),("enc_gkp","squeezed"),("enc_omg","ae_atom"),("enc_omg","ion"),
     ("ro_disp","transmon"),("ro_disp","cavity"),("ro_fluor","ion"),("ro_fluor","defect"),("ro_img","alkali"),("ro_img","ae_atom"),("ro_s2c","qd_spin"),("ro_s2c","donor"),("ro_erasure","enc_dualrail"),("ro_erasure","enc_omg"),
     ("code_qldpc","cx_lr"),("code_qldpc","cx_qccd"),("code_qldpc","cx_bus"),("code_qldpc","cx_aod"),("code_highrate","cx_aod"),("code_highrate","cx_qccd"),("code_highrate","cx_bus"),("code_aft","cx_aod"),("code_aft","cx_qccd"),("code_bosonic","enc_cat"),("code_bosonic","enc_gkp"),
     ("code_magic","code_surface"),("code_magic","code_color"),("dec_cryo","ct_sfq"),("dec_cryo","ct_cryocmos"),("ic_atomcavity","alkali"),("ic_atomcavity","ae_atom"),("g_bos","transmon"),("cavity","fab_3d"),("dec_fpga","code_surface"),("dec_nn","code_surface")}
EDGES += [dict(type="requires",src=a,dst=b,en=en,ru=ru,any=((a,b) in ANY)) for (a,b,en,ru) in REQ]
REP=[
("transmon","fluxonium","alternative superconducting carriers","альтернативные сверхпроводниковые носители"),("alkali","ae_atom","alternative atomic species","альтернативные виды атомов"),("photon","squeezed","DV vs CV photonics","DV vs CV фотоника"),("qd_spin","donor","dot vs donor spins","спины точек vs доноров"),
("enc_bare","enc_dualrail","bare vs erasure encoding","голое vs erasure кодирование"),("enc_bare","enc_cat","bare vs cat","голое vs кошка"),("enc_cat","enc_gkp","cat vs GKP","кошка vs GKP"),("enc_hf","enc_omg","ground vs metastable manifold","основное vs метастабильное многообразие"),("enc_eo","enc_spin_ld","encoded vs bare spin","кодированный vs голый спин"),
("g_tc","g_cr","tunable vs fixed-frequency","перестраиваемый vs фиксированная частота"),("g_ms","g_elec","laser vs electronic gates","лазерные vs электронные гейты"),("g_fusion","g_cv","DV fusion vs CV Gaussian","DV fusion vs CV гауссовы"),("g_bos","g_catcnot","ancilla-mediated vs direct cat CNOT","через анциллу vs прямой cat-CNOT"),
("cx_nn","cx_lr","NN vs long-range couplers","NN vs дальние couplers"),("cx_qccd","cx_bus","shuttling vs chain bus","транспорт vs шина цепочки"),("cx_nn","cx_shuttle","static vs shuttled spins","статические vs переносимые спины"),("cx_nn","cx_crossbar","individual vs shared lines","индивидуальные vs общие линии"),
("ct_rt","ct_cryocmos","RT vs 4 K control","комнатное vs 4 K управление"),("ct_rt","ct_sfq","RT vs mK SFQ","комнатное vs мК SFQ"),("ct_cryocmos","ct_sfq","cryo-CMOS vs SFQ","cryo-CMOS vs SFQ"),("ct_rt","ct_fluxdac","RT lines vs on-chip DACs","комнатные линии vs on-chip DAC"),("ct_laser","ct_pic_trap","free-space vs PIC optics","свободное пространство vs PIC-оптика"),("ct_ionlaser","ct_ionmw","laser vs microwave ion control","лазерное vs СВЧ управление ионами"),
("ro_img","ro_imgfast","ms vs µs imaging","мс vs мкс imaging"),
("code_surface","code_color","surface vs colour","surface vs colour"),("code_surface","code_qldpc","local (surface) vs non-local constant-rate qLDPC — alternatives for the same slot, combinable hierarchically (surface/LPU processing + gross memory)","локальный (surface) vs нелокальный qLDPC постоянной скорости — альтернативы для того же слота, совместимы иерархически (surface/LPU-обработка + gross-память)"),("code_qldpc","code_highrate","non-local BB memory (gross) vs high-rate transversal blocks ([[16,6,4]] tesseract, [[16,4,2,4]])","нелокальная BB-память (gross) vs высокоскоростные трансверсальные блоки ([[16,6,4]] tesseract, [[16,4,2,4]])"),("code_surface","code_highrate","2D vs high-rate transversal","2D vs high-rate трансверсальные"),("code_surface","code_erasure","Pauli vs erasure-adapted","паулиевский vs erasure-адаптированный"),("code_fusion","code_bosonic","DV fusion FT vs GKP concatenation","DV fusion FT vs конкатенация GKP"),
("dec_mwpm","dec_nn","matching vs neural","matching vs нейросетевой"),("dec_mwpm","dec_relaybp","matching vs BP","matching vs BP"),("dec_fpga","dec_gpu","FPGA vs GPU","FPGA vs GPU"),("dec_fpga","dec_cryo","RT FPGA vs cryo decoder","FPGA при комн. т. vs крио-декодер"),
("ic_mcm","ic_cryolink","same-fridge vs inter-fridge","один криостат vs между криостатами"),("ic_cryolink","ic_transducer","microwave link vs optical link","СВЧ-линк vs оптический линк"),
("fab_sc","fab_3d","planar vs 3D","планарное vs 3D"),("fab_cmos","fab_stm","foundry vs STM","фабрика vs STM"),("fab_trap","fab_cmos","MEMS vs standard CMOS fab for traps","MEMS vs стандартная CMOS-фабрика для ловушек"),
]
EDGES += [E("replaces",a,b,en,ru) for (a,b,en,ru) in REP]
CON=[
("code_highrate","cx_nn","needs all-to-all connectivity","нужна связность all-to-all"),
("code_qldpc","cx_nn","needs degree ≥ 6; heavy-hex insufficient without c-couplers","нужна степень ≥ 6; heavy-hex недостаточно без c-couplers"),
("code_aft","cx_nn","transversal permutations need transport","трансверсальные перестановки требуют транспорта"),
("enc_cat","code_surface","unbiased code wastes the bias — needs repetition/XZZX/elevator codes","несмещённый код теряет bias — нужны repetition/XZZX/elevator"),
("enc_dualrail","code_surface","plain surface code discards erasure flags","обычный surface code игнорирует флаги erasure"),
("ro_spd","code_surface","destructive detection precludes repeated syndrome extraction on the same photon","разрушающая детекция исключает повторное извлечение синдрома с того же фотона"),
("g_ms","cx_bus","gate time grows with chain length (median 672 µs on Forte's 30-ion chain)","время гейта растёт с длиной цепочки (медиана 672 мкс на 30-ионной цепочке Forte)"),
("fab_3d","cx_nn","cm-scale cavities cannot tile dense 2D lattices","сантиметровые полости не укладываются в плотные 2D-решётки"),
("cx_crossbar","g_exch","shared lines vs per-pair exchange calibration","общие линии vs попарная калибровка обмена"),
("ct_sfq","transmon","SFQ switching photons cause quasiparticle poisoning unless shielded (0.96% error source in 2023 MCM)","фотоны SFQ-переключений вызывают quasiparticle poisoning без экранирования (0.96% источник ошибки в MCM 2023)"),
("code_color","dec_mwpm","colour-code syndromes contain three-body (hyperedge) events that pairwise matching cannot decode","синдромы цветного кода содержат трёхчастичные (гиперрёберные) события, которые попарное паросочетание не декодирует"),
("dec_gpu","transmon","GPU decoding over NVQLink adds a ~4 µs round trip to a ~1 µs surface-code cycle","GPU-декодирование через NVQLink добавляет ~4 мкс кругового пути к циклу поверхностного кода ~1 мкс"),
]
EDGES += [E("conflicts",a,b,en,ru) for (a,b,en,ru) in CON]
# Conflict semantics: "conflicts" = the two technologies work together only with a mitigating element or a change of
# a third layer; every conflict edge carries the mechanism (en/ru above), the measured price, the mitigation, a status and a source.
# status: open = no demonstrated mitigation at scale · mitigated = mitigation demonstrated at small scale · bypass = resolved by choosing another node in a third layer
CONX={
("code_highrate","cx_nn"):dict(
  price=("no nearest-neighbour device has run a high-rate code; on a static lattice the non-local checks need SWAP networks whose depth grows with the check span, and errors accumulate with it","ни одно NN-устройство не запускало код высокой скорости; на статической решётке нелокальные проверки требуют SWAP-сетей, глубина которых растёт с размахом проверки, и ошибки накапливаются вместе с ней"),
  mitig=("long-range on-chip couplers (IBM c-couplers, Loon 2025-11) or physical transport (atoms, ions)","дальние on-chip каплеры (IBM c-couplers, Loon 2025-11) или физический транспорт (атомы, ионы)"),
  status="open",date="2025-06",url="https://arxiv.org/abs/2506.03094"),
("code_qldpc","cx_nn"):dict(
  price=("bivariate-bicycle codes need a degree-6 Tanner graph — two long-range connections per qubit — which heavy-hex (degree 2–3) cannot provide; without c-couplers no gross code runs","бивариантные bicycle-коды требуют графа Таннера степени 6 — две дальние связи на кубит, — чего heavy-hex (степень 2–3) не даёт; без c-couplers gross-код не запускается"),
  mitig=("c-couplers (Loon), then Kookaburra module; measured coupler fidelity and length not yet published","c-couplers (Loon), затем модуль Kookaburra; измеренные точность и длина каплера пока не опубликованы"),
  status="open",date="2024-03",url="https://www.nature.com/articles/s41586-024-07107-7"),
("code_aft","cx_nn"):dict(
  price=("transversal gates between logical blocks need block-to-block qubit permutations; on a static lattice that is O(d) SWAP depth per logical gate, which erases the constant-depth advantage","трансверсальные гейты между логическими блоками требуют перестановок кубитов между блоками; на статической решётке это SWAP-глубина O(d) на логический гейт, что уничтожает преимущество постоянной глубины"),
  mitig=("physical transport (AOD tweezers, ion shuttling) — the reason the architecture is atom/ion-native","физический транспорт (AOD-пинцеты, шаттлинг ионов) — поэтому архитектура нативна для атомов/ионов"),
  status="bypass",date="2025-09",url="https://www.nature.com/articles/s41586-025-09543-5"),
("enc_cat","code_surface"):dict(
  price=("a CSS surface code corrects X and Z symmetrically, so a bias > 25 (Ocelot, 2025) buys nothing; the ~10× qubit saving of cat architectures exists only with bias-tailored codes","CSS-поверхностный код исправляет X и Z симметрично, поэтому bias > 25 (Ocelot, 2025) ничего не даёт; ~10-кратная экономия кубитов кот-архитектур существует только с кодами под смещённый шум"),
  mitig=("repetition (Ocelot), XZZX, elevator or LDPC-cat codes instead of the plain surface code","repetition (Ocelot), XZZX, elevator или LDPC-cat вместо обычного поверхностного кода"),
  status="bypass",date="2025-02",url="https://www.nature.com/articles/s41586-025-08642-7"),
("enc_dualrail","code_surface"):dict(
  price=("a matching decoder that ignores erasure flags sees a threshold of 0.937% instead of 4.15% — the erasure advantage is lost entirely","декодер паросочетания, игнорирующий флаги стирания, видит порог 0.937% вместо 4.15% — преимущество стирания теряется полностью"),
  mitig=("erasure-aware decoding (heralded-loss matching) — a decoder change, not a hardware change","декодирование с учётом стирания (matching с геральдированными потерями) — замена декодера, не железа"),
  status="mitigated",date="2022-01",url="https://arxiv.org/abs/2201.03540"),
("ro_spd","code_surface"):dict(
  price=("a detected photon is gone: no repeated syndrome extraction on the same carrier, so a surface-code memory cycle cannot be run on flying qubits","обнаруженный фотон исчезает: повторное извлечение синдрома с того же носителя невозможно, поэтому цикл памяти поверхностного кода на летящих кубитах не запускается"),
  mitig=("fusion-based / measurement-based fault tolerance, where every photon is measured exactly once by design","fusion-based / measurement-based отказоустойчивость, где каждый фотон по построению измеряется ровно один раз"),
  status="bypass",date="2023-02",url="https://www.nature.com/articles/s41467-023-36493-1"),
("g_ms","cx_bus"):dict(
  price=("spectral crowding of the motional modes makes the gate slower and less faithful as the chain grows: median 672 µs on Forte's 30-ion chain vs ~10–30 µs on short chains","спектральная теснота мод движения делает гейт медленнее и менее точным с ростом цепочки: медиана 672 мкс на 30-ионной цепочке Forte против ~10–30 мкс на коротких цепочках"),
  mitig=("short chains in zoned QCCD traps (Quantinuum), amplitude/phase-modulated gates, or electronic gates on ≤ 4-ion segments","короткие цепочки в зонированных QCCD-ловушках (Quantinuum), амплитудно/фазово-модулированные гейты или электронные гейты на сегментах ≤ 4 ионов"),
  status="open",date="2025",url="https://www.ionq.com/quantum-systems/forte"),
("fab_3d","cx_nn"):dict(
  price=("cm-scale machined cavities give ~1 mode per cm²; a dense 2D lattice of them is impossible, so 3D bosonic qubits stop at a few tens of modes per module","сантиметровые фрезерованные полости дают ~1 моду на см²; плотная 2D-решётка из них невозможна, поэтому 3D-бозонные кубиты останавливаются на десятках мод на модуль"),
  mitig=("mm-scale coaxial λ/4 and double-post cavities, or planar bosonic modes; density still an order below transmon lattices","миллиметровые коаксиальные λ/4 и двухштыревые полости или планарные бозонные моды; плотность всё ещё на порядок ниже решёток трансмонов"),
  status="open",date="2026-07",url="https://arxiv.org/abs/2607.06718"),
("cx_crossbar","g_exch"):dict(
  price=("one shared line drives many exchange gates at once, but J varies dot-to-dot with disorder; the 2024 16-dot crossbar showed no coherent qubit operation","одна общая линия управляет многими обменными гейтами сразу, но J меняется от точки к точке из-за беспорядка; 16-точечный crossbar 2024 г. не показал когерентной работы кубитов"),
  mitig=("300 mm uniformity (~1% device-to-device), local floating-gate trims, or a semi-shared scheme with per-qubit correction lines","однородность 300 мм (~1% от прибора к прибору), локальные подстроечные плавающие затворы или полуобщая схема с корректирующими линиями на кубит"),
  status="open",date="2024-07",url="https://www.nature.com/articles/s41467-024-50355-4"),
("code_color","dec_mwpm"):dict(
  price=("weight-6 checks produce detection events that fire in triples; a plain matcher is not applicable, and the decoders that are (restriction, Möbius, Chromobius) lose accuracy — Google's d=5 colour memory reached 8.19(14)×10⁻³ per cycle with the search-based Tesseract decoder, worse than its d=5 surface code","проверки веса 6 дают события детекции тройками; плоское паросочетание неприменимо, а применимые декодеры (restriction, Möbius, Chromobius) теряют точность — цветная память d=5 у Google достигла 8.19(14)×10⁻³ за цикл с поисковым декодером Tesseract, хуже её же surface code d=5"),
  mitig=("hyperedge-capable decoders: Chromobius / restriction decoders, Tesseract (search), neural decoders; hook-free one-ancilla circuits (2026) reduce the hyperedge burden","декодеры с гиперрёбрами: Chromobius / restriction, Tesseract (поиск), нейросетевые; схемы без hook-ошибок с одной анциллой (2026) снижают нагрузку гиперрёбер"),
  status="mitigated",date="2026-07",url="https://www.nature.com/articles/s41586-026-10759-2"),
("dec_gpu","transmon"):dict(
  price=("NVQLink's measured round trip is 3.84 µs mean / 3.96 µs max, i.e. 3–4 surface-code cycles of a Willow-class transmon (~1.1 µs): syndromes queue faster than any single-cycle reaction, so real-time feed-forward (non-Clifford, teleportation) must wait","измеренный круговой путь NVQLink 3.84 мкс в среднем / 3.96 мкс максимум — 3–4 цикла поверхностного кода трансмона класса Willow (~1.1 мкс): синдромы накапливаются быстрее любой реакции за один цикл, и обратная связь в реальном времени (не-Клиффорд, телепортация) вынуждена ждать"),
  mitig=("windowed / streaming decoding with an FPGA pre-decoder at the fridge, deferring only the reaction-critical decisions; slower carriers (atoms, ions: ms cycles) do not see the conflict","оконное / потоковое декодирование с FPGA-предекодером у криостата, откладывающее только критичные к реакции решения; медленные носители (атомы, ионы: мс-циклы) конфликта не видят"),
  status="open",date="2025-11",url="https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/"),
("ct_sfq","transmon"):dict(
  price=("photons emitted by switching junctions lie above the aluminium gap (2Δ ≈ 90 GHz) and break Cooper pairs in the qubit film: T₁ decay plus correlated, non-Pauli bursts; 0.96(2)% of the 1.2(1)% error per Clifford in the 2023 multi-chip module","фотоны переключающихся переходов лежат выше щели алюминия (2Δ ≈ 90 ГГц) и разрывают куперовские пары в плёнке кубита: распад T₁ плюс коррелированные не-паулиевские всплески; 0.96(2)% из 1.2(1)% ошибки на Клиффорд в многочиповом модуле 2023 г."),
  mitig=("driver on a separate die, pulse-bandwidth limiting (projected 0.1%), quasiparticle traps / gap engineering, mm-wave shielding; SEEQC 2026 reports no detectable poisoning at 5 qubits","драйвер на отдельном кристалле, ограничение полосы импульсов (прогноз 0.1%), ловушки квазичастиц / инженерия щели, мм-волновое экранирование; SEEQC 2026 сообщает об отсутствии детектируемого отравления на 5 кубитах"),
  status="mitigated",date="2023-09",url="https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310"),
}
CONSTAT={"open":("open — no mitigation shown at scale","открыт — снятие в масштабе не показано"),"mitigated":("mitigated at small scale","снят в малом масштабе"),"bypass":("bypassed by a different node in a third layer","обходится выбором другого узла в третьем слое")}
for e in EDGES:
    if e["type"]=="conflicts":
        x=CONX.get((e["src"],e["dst"]))
        if x: e.update(price=dict(en=x["price"][0],ru=x["price"][1]),mitig=dict(en=x["mitig"][0],ru=x["mitig"][1]),status=x["status"],date=x["date"],url=x["url"])
assert all(e.get("status") for e in EDGES if e["type"]=="conflicts"), "every conflict edge needs CONX detail"
# ---------------------------------------------------------------- DERIVATIONS (transfers, off-diagonal, empty slots, clock, validity)
import json, math
NODE={n["id"]:n for n in NODES}
LAYER_BY_ID={l[0]:l for l in LAYERS}
FAMILY_OF={p["id"]:p["family"] for p in PATHS}

OFFDIAG_RULES = {
 "NAT_MW":  ("natural carrier + microwave/electronic control","естественный носитель + СВЧ/электронное управление"),
 "FAB_FAR": ("fabricated carrier + far connectivity (transport / long-range)","изготовленный носитель + дальняя связность (транспорт / long-range)"),
 "FAB_ERASURE": ("fabricated carrier + erasure error structure","изготовленный носитель + структура ошибок erasure"),
 "FAB_COLD": ("fabricated carrier + control/decoding in the cold stage","изготовленный носитель + управление/декодирование в холодной ступени"),
 "FAB_PHOTONIC": ("fabricated/solid-state carrier + photonic interconnect","изготовленный/твердотельный носитель + фотонный интерконнект"),
 "NAT_FAST_GATE": ("natural carrier + sub-microsecond gate","естественный носитель + суб-микросекундный гейт"),
 "NAT_FAST_READ": ("natural carrier + ≤ 10 µs readout","естественный носитель + считывание ≤ 10 мкс"),
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
        if node["e"]["place"] in ("4K","mK") and L in (5,8): f.add("FAB_COLD")
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
                if e.get("any") and e["dst"] not in path_nodes[pid]: continue   # either-or dependency counts only where realised
                NODE[e["dst"]]["reach"].add(FAMILY_OF[pid])
    for n in NODES:
        n["reach"]=sorted(n["reach"]|set(n["families"])); n["reach_degree"]=max(0,len(n["reach"])-1)
        recent=(n["since"]>=2023 or n["status"] in ("E","X"))
        n["hub"]= n["reach_degree"]>=2 or (n["reach_degree"]>=1 and recent)
        n["hub_recent"]= n["hub"]
    # empty slots
    empty=[n["id"] for n in NODES if n["status"]=="X"]
    empty_slots=[]
    for p in PATHS:
        for L in range(1,11):
            ids=p["slots"].get(L,[])
            if not ids: empty_slots.append(dict(path=p["id"],layer=L))
            elif all(NODE[i]["status"]=="X" for i in ids): empty_slots.append(dict(path=p["id"],layer=L,only=ids))
    # derived clock per path = max(gate, readout, transport)
    for p in PATHS:
        def first(L):
            ids=p["slots"].get(L,[]); return NODE[ids[0]] if ids else None
        g=first(3); r=first(6); c=first(4)
        tg=g["b"]["t"] if g and g["b"]["t"] is not None else None
        tr=r["c"]["t"] if r and r["c"] and r["c"]["t"] is not None else None
        tc=c["b"]["t"] if c and c["b"]["t"] is not None and c["d"] in ("transport",) else None
        parts={"gate":tg,"readout":tr,"transport":tc}
        vals=[v for v in parts.values() if v is not None]
        p["clock_derived"]=max(vals) if vals else None
        p["clock_parts"]=parts
        p["clock_limiter"]=max(parts,key=lambda k:(parts[k] if parts[k] is not None else -99)) if vals else None
    # defines edges flattened
    defines=[dict(type="defines",src=n["id"],dst=d["out"],metric=d["metric"],value=d["value"],date=d["date"],url=d["url"]) for n in NODES for d in n["defines"]]
    # validity check against prose directions
    DIRECTIONS={
     "D1 superconducting + engineered error structure + qLDPC + cold-stage control":["enc_dualrail","ro_erasure","code_erasure","code_qldpc","cx_lr","ct_cryocmos","ct_sfq","ct_fluxdac","ic_mcm","ic_cryolink","dec_relaybp","dec_nn"],
     "D2 neutral atoms + zoned + transversal/algorithmic FT + erasure conversion":["g_ryd","enc_omg","ro_erasure","code_erasure","code_highrate","ro_imgfast","ct_pic_trap"],
     "D3 trapped ions + electronic gates + chip traps":["g_elec","ct_ionmw","fab_cmos","ct_ionlaser"],
     "D4 silicon spins + CMOS manufacturability":["fab_cmos","ct_cryocmos","cx_shuttle"],
     "D5 photonics as interconnect":["fab_pic","ro_spd","ic_transducer","ic_spinphoton"],
     "D6 bosonic codes as a direction":["enc_dualrail","enc_gkp","code_bosonic","g_catcnot"],
     "X1 erasure engineering (cross-cutting)":["enc_dualrail","enc_omg","ro_erasure","code_erasure"],
     "X2 real-time decoding (cross-cutting)":["dec_nn","dec_relaybp","dec_gpu","dec_cryo"],
     "X3 qLDPC / transversal FT (cross-cutting)":["code_qldpc","code_highrate","code_magic"],
     "X4 cold-stage control (cross-cutting)":["ct_sfq","ct_cryocmos","ct_fluxdac"],
     "X5 photonic interconnect (cross-cutting)":["fab_pic","ro_spd","ic_transducer"],
    }
    DIAGONAL_ENABLERS={"D2":["cx_aod","code_aft","dec_corr","ae_atom"],"D3":["cx_qccd","fab_trap","ic_ionphoton"],"D5":["ic_fibre","ic_ionphoton","ic_atomcavity"]}
    S=set(offd)|set(n["id"] for n in NODES if n["hub_recent"])|set(empty)
    report={}
    for k,ids in DIRECTIONS.items():
        hit=[i for i in ids if i in S]; miss=[i for i in ids if i not in S]
        report[k]=dict(hit=hit,miss=miss,coverage=round(len(hit)/len(ids),2))
    covered=set(i for ids in DIRECTIONS.values() for i in ids)
    novel=sorted(S-covered)
    validity=dict(directions=report,S_size=len(S),S=sorted(S),novel=novel,diagonal_enablers=DIAGONAL_ENABLERS)
    return dict(layers=[dict(n=l[0],id=l[1],en=l[2],ru=l[3]) for l in LAYERS],vocab=dict(AFF={('%g'%k):v for k,v in AFF.items()},DET=DET,MECH=MECH,MOB=MOB,MOD=MOD,PLACE=PLACE,ERR=ERR,FAB=FAB,STATUS=STATUS,OUT=OUT,OFFDIAG=OFFDIAG_RULES,CONSTAT=CONSTAT),
                nodes=NODES,paths=PATHS,edges=EDGES+transfers+defines,empty_status=empty,empty_slots=empty_slots,validity=validity)

if __name__=="__main__":
    G=compute()
    import os; json.dump(G,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("nodes",len(G["nodes"]),"edges",{t:sum(1 for e in G["edges"] if e["type"]==t) for t in ("requires","replaces","conflicts","transfers","defines")})
    print("\nOFF-DIAGONAL:")
    for n in G["nodes"]:
        if n["offdiag"]: print(f"  {n['id']:16s} {','.join(n['offdiag']):32s} via {n['offdiag_paths']}")
    print("\nHUBS (reach>=2 families):")
    for n in sorted(G["nodes"],key=lambda x:(-x["reach_degree"],x["id"])):
        if n["hub"]: print(f"  {n['id']:16s} {'RECENT' if n['hub_recent'] else 'commodity':9s} reach={n['reach']} paths={len(n['paths'])}")
    print("\nEMPTY status:",G["empty_status"]); print("EMPTY slots:",[(e['path'],e['layer'],e.get('only')) for e in G['empty_slots']])
    print("\nCLOCK:")
    for p in G["paths"]: print(f"  {p['id']:10s} derived=10^{p['clock_derived']} s limiter={p['clock_limiter']} parts={p['clock_parts']} measured={p['cycle']}")
    print("\nVALIDITY:"); 
    for k,v in G["validity"]["directions"].items(): print(f"  {v['coverage']:.2f} {k}  miss={v['miss']}")
    print("  novel (in S, not in prose):",G["validity"]["novel"])
