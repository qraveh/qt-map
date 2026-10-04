# Russian terminology of the Quantum Technology Atlas — the binding list for every translation (4 Oct 2026)

The editor's order (4 Oct 2026): every Russian term checked for its correct use in the context of quantum mechanics — the most literate
academic usage, preferably in the context of the very device being described. Authority, in this order: (1) the Russian-language
literature of the device itself — ФИАН/РКЦ for ions (Колачевский, Заливако, Семериков), МИСиС/ВНИИА/ИФТТ/МФТИ for superconducting
circuits (Устинов, Беседин, Рязанов, Мажорин), ИФП СО РАН and МГУ for neutral atoms (Рябцев, Бетеров), МГУ/ИТМО for photonics (Кулик,
Страупе, Калачев), ФТИ им. Иоффе/НГУ for spins, ИТФ for topological; journals УФН, Письма в ЖЭТФ, ЖЭТФ, Квантовая электроника, Известия
вузов. Радиофизика, Фотоника; (2) the Russian QI texts — Нильсен, Чанг «Квантовые вычисления и квантовая информация» (Мир, 2006),
Прескилл, Китаев–Шень–Вялый, Валиев–Кокин, Килин (УФН 1999), university courses; (3) living usage only as an indicator (ru.wikipedia,
N+1, Элементы, Хабр). Checked 4 Oct 2026 by seven research passes (653 entries); the decisions and their evidence are in the
editor's working folder (DECISIONS_2026-10-04_russian-terms.md).

Rules. Formal written Russian, the register of a scientific review (УФН, not Хабр). Terms below are fixed: use them everywhere, in the
same form; a term that is not here is translated once, consistently, and reported for this list. Latin identifiers (`transmon`, `cx_nn`,
machine, product and organisation names, arXiv ids, DOIs, URLs), numbers, unit symbols (international in all three editions: K, mK, µs,
ns, ms, MHz, GHz, mm, nm, dB — never мкс, мК, МГц), citation marks ([D], [C], [R], [S], [P], [G:KEY], [S12], [1]), section marks (§7.3),
Markdown, `{{placeholders}}` and `{python expressions}` are kept exactly. A transliteration (гейт, каплер, интерконнект, линк, трансдьюсер,
геральдированный, фиделити, дизайн) is never the term of the Atlas; a Latin word stays only where the Russian literature itself keeps it
(time-bin, flip-chip, SNSPD, FBQC, QCCD, QEC, MWPM, qLDPC, GKP, TWPA, QFP, SLM, omg, IPO, SPAC, c-coupler/l-coupler, repetition-cat,
LDPC-cat, yoked), and then the first mention in a document carries the Russian expansion once (сверхпроводниковый однофотонный детектор
(SNSPD); ошибка приготовления и измерения (SPAM); неразрушающее измерение (QND); двухуровневые системы (TLS); код Готтесмана–Китаева–
Прескилла (GKP); динамическая развязка (DD)). Where a Russian term replaced a Latin one the reader may know in English, the first
mention carries the English once in parentheses: стирание (erasure), слияние (fusion), оповещение (heralding), паросочетание (matching),
безубыточность (break-even), квенч (quench), кросс-резонанс (cross-resonance).

| English | русский | gender / form | authority |
|---|---|---|---|
| gate (quantum logic gate) | вентиль; однокубитный / двухкубитный вентиль; CZ-вентиль; вентильная модель; устройство с вентилями; layer 3 «Механизм вентиля» | m. — вентиля, вентилем, вентили, вентилей; «операция» (однокубитные операции) is the ФИАН alternative and stays where written | Нильсен–Чанг (Мир 2006) «квантовые вентили»; Горбацевич, Шубин, УФН 188 (2018) «Квантовые логические вентили»; Мажорин…Рязанов, Изв. вузов. Радиофизика 66 (2023) «двухкубитный вентиль CZ»; ru.wikipedia «Квантовый вентиль» |
| gate (electrostatic, spin qubits) | затвор; квантовая точка, формируемая затворами; затворный стек | m. | Russian semiconductor physics (ФТИ, НГУ) |
| coupler, tunable coupler | элемент связи; перестраиваемый элемент связи; c-coupler / l-coupler (IBM's names) stay Latin | m. — элемента связи, элементами связи | Мажорин, дисс. МФТИ/РКЦ 2025 «соединительный элемент»; МИСиС/ODS course «элемент связи» |
| interconnect (layer 9) | межсоединение; межмодульные межсоединения | n. — agreement changes from the former m. интерконнект | the Russian microelectronics term (межсоединения ИС) |
| link (ion–photon, spin–photon) | интерфейс (ион-фотонный, спин-фотонный) | m. | Russian quantum-network literature |
| link (fibre, microwave, between modules/cryostats) | линия связи (волоконная, СВЧ-), канал связи | f. / m. | ВОЛС; Russian engineering |
| transducer (microwave–optical) | преобразователь; СВЧ-оптическое преобразование | m. | Russian engineering |
| heralded / heralding / herald | с оповещением (источник, фотон, состояние, запутывание — after the noun); оповещение; оповещающий фотон (сигнал) | — | Криштоп, Фотоника «однофотонные источники с оповещением», «фотон оповещения»; Чуприна, Латыпов, Изв. РАН сер. физ. 83 (2019) «оповещающего фотона» |
| erasure (error) | стирание; ошибка стирания; кубит со стиранием; преобразование ошибок в стирания; проверка на стирание; флаг стирания; частота стираний; коды, адаптированные к стираниям; декодирование с учётом стираний; естественные стирания; преобразуемая в стирание (error vocab) | n. | coding theory («стирающий канал», «ошибки стирания»); Russian QEC lecture notes |
| fusion (photonic) | слияние; вентиль слияния; сеть слияний; на основе слияний (FBQC stays) | n. | Russian photonic-QC reviews «операция слияния (fusion)» |
| dual-rail | двухрельсовый (кубит, кодирование) | adj. | Russian QI «двухрельсовое кодирование» |
| surface / colour / repetition code; rotated | поверхностный код; цветовой код; код с повторением; повёрнутый поверхностный код | m. | Russian QEC literature; ru.wikipedia; coding theory |
| concatenated codes, concatenation | каскадные коды; каскадирование | — | Russian coding theory (Форни) |
| bit-flip / phase-flip | переворот бита / переворот фазы; ошибка переворота бита; время переворота бита | m. | Нильсен–Чанг |
| matching (MWPM) | паросочетание; декодер на основе паросочетаний; коррелированное паросочетание; MWPM stays | n. | Russian graph theory «совершенное паросочетание минимального веса» |
| cavity (3D superconducting, optical) | резонатор; объёмный резонатор; резонаторная КЭД; литография → «механическая обработка объёмных резонаторов» | m. | Russian physics |
| cat qubit / cat code / cat state | кошачий кубит; кошачий код; кошачьи состояния (состояние кота Шрёдингера) | — | Russian quantum optics |
| quench (Hamiltonian; annealer) | квенч; когерентный квенч | m. (was закалка — hardening) | БРЭ «Глобальный квенч» |
| fidelity | точность; точность неразрушающего измерения (QND) | f. (never верность; достоверность = confidence) | ФИАН/РКЦ/ИФП theses «точность квантовых операций» |
| dephasing | дефазировка | f. (not расфазировка) | КФУ lecture text 2022 «релаксации, декогеренции и дефазировки»; ФУХА-2025 |
| decoherence | декогеренция | f. | УФН; Менский |
| entanglement, entangling | запутанность; запутанные состояния; запутывающий вентиль; запутывание | — (not перепутанность) | ru.wikipedia «Квантовая запутанность»; modern Russian QI |
| trapped ions | ионы в ловушках; ион в ловушке | — (not захваченные) | ФИАН «компьютер на ионах в ловушке» |
| Mølmer–Sørensen gate | вентиль Мёльмера–Соренсена | — | ФИАН/РКЦ papers |
| shuttling (ions, atoms, spins) | перемещение (ионов, атомов, спинов); transport stays транспорт (layer 4, MOB) | n. | Русских, Жаднов, Письма в ЖЭТФ 123 (2026) «перемещение ионов»; ФИАН 2026 |
| atom reload(ing) | дозагрузка атомов | f. (not перезагрузка, подгрузка) | technical Russian; ИФП «загрузка атомов в ловушку» |
| fluorescence detection / imaging | детектирование состояния по флуоресценции; регистрация флуоресценции (на камере); флуоресценция (ФЭУ/SNSPD) | f. | ФИАН; ИФП/МГУ atom arrays |
| clock-state qubit | кубит на часовом переходе; оптический кубит на узком переходе | m. | atomic-clock Russian «часовой переход» |
| defect spin | спин дефекта; спины дефектов; центр окраски | m. | Russian construction (as «спин электрона») |
| donor spin | донорный спин | m. — kept | Russian semiconductor physics |
| fermion parity | фермионная чётность | f. | Russian topological-SC literature |
| fabricated (carrier divide) | искусственный (носитель); естественный / искусственный; literal manufacturing keeps изготовленный | adj. | Астафьев (МФТИ) «сверхпроводниковым искусственным атомам» |
| superconducting (device) / (state) | сверхпроводниковый (кубит, процессор, схема, резонатор, детектор, электроника, литография) / сверхпроводящий (состояние, переход, щель, ток, плёнка, петля, контур) | adj. | МИСиС/ВНИИА/МПГУ «сверхпроводниковые кубиты», «сверхпроводниковый однофотонный детектор» |
| crosstalk | перекрёстные помехи | f. pl. (not наводки) | Russian QC literature |
| T1 relaxation / T2 coherence | T1-релаксация / когерентность T2 | — | Russian NMR/QI usage |
| randomized benchmarking; cycle benchmarking | рандомизированный бенчмаркинг; циклический бенчмаркинг (cycle benchmarking) | m. — kept | Russian QC literature |
| error mitigation; mitigated | смягчение ошибок; смягчён (gap ledger) | n. (one stem; снят = removed) | Russian QC usage |
| fault tolerance, fault-tolerant | отказоустойчивость, отказоустойчивый (never FT in Russian prose) | f. | Russian QC literature |
| ancilla | анцилла | f. — kept | Russian QI |
| magic-state cultivation | культивация (one form) | f. | Russian QEC usage |
| break-even | безубыточность; точка безубыточности (break-even) | f. | Russian QEC press and papers |
| sweet spot | оптимальная рабочая точка | f. | Russian SC-qubit literature |
| mid-circuit (measurement) | внутрисхемный (внутрисхемное измерение, внутрисхемная проверка стирания) | adj. | the Atlas's established rendering |
| real-time | в реальном времени; реального времени | — | Russian |
| on-chip | на чипе | — | Russian QC usage (чип is accepted technical Russian) |
| post-selected, post-selection | с постселекцией; постселекция | f. | Russian QI |
| bias-preserving; biased noise | сохраняющий смещение; смещённый шум | adj. | Russian cat-qubit texts |
| exchange-only | чисто обменное (кодирование) | adj. | Russian spin-qubit usage |
| baseband | в основной полосе частот | — | Russian radio engineering |
| feed-forward | прямая связь; электроника прямой связи | f. | Russian control theory |
| all-to-all | все со всеми | — | Russian |
| FPGA | ПЛИС; ПЛИС-декодер; декодер на ПЛИС | f. | Russian electronics |
| CMOS, cryo-CMOS | КМОП, крио-КМОП; КМОП-фабрика 300 mm | — | Russian microelectronics |
| SQUID, rf-SQUID, dc-SQUID | СКВИД, ВЧ-СКВИД, ПТ-СКВИД | m. | Russian superconducting electronics |
| SFQ (RSFQ) | БОК (быстрая одноквантовая логика); управление на БОК-логике | f. | Лихарев; Russian SC electronics |
| MEMS; surface-electrode trap | МЭМС; планарная ловушка | — | ФИАН «планарная ловушка Пауля» |
| STM (lithography) | СТМ; СТМ-литография | f. | Russian surface science |
| PIC (photonic integrated circuit) | ФИС (фотонная интегральная схема); фабрика ФИС; интегральная оптика / фотоника | f. | Russian photonics (ИТМО, МГУ) |
| MBE; III-V | МЛЭ; A3B5 (гетероструктуры A3B5) | — | Russian semiconductor physics |
| AOD / AOM | АОД (акустооптический дефлектор) / АОМ | m. | ИФП СО РАН (Бетеров, Автометрия 2020) |
| Purcell filter / effect | фильтр Парселла / эффект Парселла | m. | Russian circuit-QED literature |
| cross-resonance | кросс-резонанс; кросс-резонансный вентиль | m. | МИСиС |
| two-level systems (TLS) | двухуровневые системы (TLS) | f. pl. | Russian SC-qubit literature |
| continuous variables (CV) | непрерывные переменные; гауссовы вентили на непрерывных переменных | — | МГУ quantum optics |
| flying qubits | летающие кубиты | m. pl. (not летящие) | Russian QI |
| nearest neighbour (NN) | ближайшие соседи; разводка ближайших соседей; устройство со связностью ближайших соседей | — | Russian physics |
| 1Q / 2Q | однокубитный / двухкубитный (in prose; the bare column label stays) | adj. | Russian QC literature |
| rf (reflectometry, readout) | радиочастотная рефлектометрия; радиочастотное считывание; радиочастотное измерение квантовой ёмкости | adj. | Russian spin-qubit literature |
| spin-to-charge conversion | преобразование спина в заряд | n. | Russian |
| Loss–DiVincenzo | Лосса–ДиВинченцо | — | Russian spin-qubit texts |
| diamond growth | выращивание алмаза | n. | Russian CVD-diamond usage |
| crossbar | кроссбар | m. | Russian (the Atlas's own form) |
| foundry; merchant foundry | фабрика; контрактная фабрика | f. | Russian microelectronics |
| testbed | испытательный стенд | m. | Russian engineering |
| whitepaper | белая книга (white paper) | f. | Russian business press |
| undisclosed (amount) | не раскрыто; сумма не раскрыта | — | Russian |
| Series A/B/C; extension | раунд серии A/B/C; продление раунда серии B | m. | Russian business press |
| on-premise | на площадке заказчика | — | Russian IT |
| brief (technology brief) | обзор (обзор технологии) | m. (бриф is an agency assignment in Russian) | Russian: аналитический обзор |
| actors (Actors & economics; Actors & goals) | участники («Участники и экономика», «Участники и цели») | m. pl. | plain Russian |
| identity & lineage; engineering state of the art; outlook; IP & standards (brief headings) | «Сущность и происхождение»; «Достигнутый инженерный уровень»; «Перспективы и открытые вопросы»; «Интеллектуальная собственность и стандарты» (ИС reads as интегральная схема) | — | plain Russian |
| evidence grade | уровень доказательности | m. | the Russian term (клинические рекомендации) |
| crossing technology (the Atlas's concept) | сквозная технология | f. | «сквозные технологии» (cross-cutting; НТИ) |
| theory / design only; design (engineering) | только теория / проект; проект, проектирование (дизайн-центр stays) | — | Russian engineering |
| count with quality; carrier-agnostic; evaluator; standards body; headline figure; whole word (UI) | число кубитов с учётом качества; не зависящий от носителя; оценивающая сторона; орган по стандартизации; ключевые цифры; слово целиком | — | plain Russian |
| best / worst case (outlook labels) | «В лучшем случае к 2029 г.» / «В худшем случае» | — | plain Russian |
| kept after checking | анцилла, декодер, кубит, трансмон, флаксониум, потоковый кубит, отжигатель, квантовый отжиг, сверхтонкий кубит, ридберговский, оптический пинцет, магические состояния, высокоскоростные коды, накладные расходы, частота ошибок, цикл QEC, однократное считывание, динамическая развязка, Маха–Цендера, реестр, списан, по графику, ведущий инвестор, брутто, суммарно, финансирующая сторона, донорный спин, полупроводниковые спины, бамп (industry term), time-bin, flip-chip | — | the device literature uses them |
| resource-state generator (RSG) (the photonic FBQC term; the English pass of 4 Oct replaced "factory") | генератор ресурсных состояний (RSG) | m. | PsiQuantum (Bartolucci et al. 2023); «фабрика» stays for magic states |
| SiMOS; AlphaQubit 2; bivariate bicycle (English spellings fixed 4 Oct) | SiMOS; AlphaQubit 2; bivariate bicycle | — | Latin tokens as the English edition writes them |
