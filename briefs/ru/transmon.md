---
id: transmon
name: Трансмон
layer: 1 Носитель
tier: 1
status: demonstrated
since: 2007
one_line: Джозефсоновский переход, шунтированный ёмкостью (Koch, 2007); носитель, стоящий за Willow, Heron/Nighthawk и Zuchongzhi, с самым быстрым детерминированным гейтом и самым быстрым циклом QEC среди всех продемонстрированных кубитов.
verdict: Наиболее финансируемый и самый быстрый носитель, ограниченный на масштабе двухкубитными ошибками ~10⁻³ и ошибками считывания ~10⁻², а также коррелированными всплесками раз в час. Подтвердить, если решётка из ≥100 кубитов покажет Λ ≥ 3 при медианной двухкубитной ошибке < 10⁻³ к 2028 г.; иначе понизить до статуса компонента.
updated: 2026-09-03
---

Λ = коэффициент подавления ошибок на шаг кодового расстояния; QBI = DARPA Quantum Benchmarking Initiative (Stage A — концепция → B — план НИОКР → C — государственная верификация и валидация); G1–G7 = классы целей отчёта (см. «Акторы и экономика»).

## Идентичность и происхождение

Трансмон — это джозефсоновский переход Al/AlOx/Al, шунтированный большой ёмкостью так, что E_J/E_C ≈ 50–100 [D][1]. Зарядовая дисперсия падает экспоненциально по √(8E_J/E_C), что снимает зарядовый шум 1/f ценой слабой ангармоничности α ≈ −E_C ≈ от −200 до −300 МГц; кубитом служат два нижних уровня осциллятора на 4–6 ГГц [D][1]. Koch et al. предложили его в 2007 г. [D][1]; трёхмерный трансмон (2011) [D][2] и Xmon от UCSB/Google (2014) [D][3] закрепили две линии, используемые до сих пор: с фиксированной частотой (IBM) и с перестройкой по потоку (Google, IQM, USTC).

Координаты (граф технологий):
- a: сродство 1.0, изготовленный (природного аналога нет).
- b: характерное время 10⁻⁸ с, детерминированное запутывание; ограничение на утечку (leakage) вида 1/α ставит нижнюю границу длительности импульса около 10 нс.
- c: считывание — дисперсионное СВЧ, 10⁻⁶·⁵ с (≈ 320 нс), неразрушающее, пригодное для внутрисхемного (mid-circuit) применения.
- d: подвижность — статичен, разводка на ближайших соседей.
- e: управление — СВЧ от электроники при комнатной температуре; варианты с холодной ступенью (cryo-CMOS, SFQ) — на ≤ 5 кубитах.
- f: структура ошибок — утечка + стохастические паулиевские + коррелированные всплески + когерентные/калибровочные.
- g: производство — сверхпроводниковая литография.

## Физика и пределы

Остаточная тепловая населённость (0.1% при 35 мК в трёхмерном трансмоне [D][54], ≈ 1% при 40–60 мК для кубита на 5 ГГц [S][54]) делает сброс и считывание нижней границей SPAM. Ангармоничность ограничивает однокубитные гейты 10–25 нс, а CZ на перестраиваемом каплере — 25–50 нс [D][4][7][P][5]; кросс-резонанс требует ≈ 200–500 нс [D][6].

Предел задаётся декогерентностью за время гейта: при среднем T1 = 68 мкс у Willow [D][7] CZ длительностью 40 нс несёт ≈ 6×10⁻⁴ некогерентной ошибки [S][7]; при рекордном T1 = 1.68 мс одиночного тестового трансмона Ta на Si [D][8] она падает ниже 5×10⁻⁵ [S][8]. В потерях доминируют двухуровневые системы (TLS) в аморфных оксидах на границах раздела [D][8], ниже них — квазичастицы, распад Парселла и шум магнитного потока.

Бо́льшая часть свёрнутого твёрлингом канала — стохастические паулиевские ошибки, поэтому Λ = 2.14 у Willow [D][7] согласуется с теорией. Утечка в |2⟩ накапливается под QEC, если не удалять её каждый цикл (полностью СВЧ-сброс у USTC снизил её в 72×, до 6.4×10⁻⁴, на 107 кубитах [D][9]). Когерентные ошибки (остаточное ZZ, дрейф TLS) вынудили применять перекалибровку с обучением с подкреплением прямо внутри прогона QEC у Google в 2026-07 [D][10]. Коррелированные всплески (ионизирующие частицы, наводняющие кристалл квазичастицами) поражают все кубиты разом — примерно один на 10 с на Sycamore в 2021 г. [D][11] и около одного в час на Willow после инженерии сверхпроводящей щели [D][7][12], — обрывая длинные прогоны памяти по всплескам, а не по расстоянию. Сдвинуть этот предел означает перейти к новым материалам (Ta, инкапсулированный Nb), к ангармоничности уровня флаксониума, к управлению радиационной обстановкой либо к конверсии в стирание (dual-rail).

## Инженерное состояние (state of the art)

Лучшие изолированные устройства: T1 1.68 мс, Q 2.5×10⁷, однокубитный гейт 99.994% [D][8]; CZ 99.93% и считывание за 280 нс с точностью (fidelity) 99.94% на двухкубитном кристалле IQM [D][13]; CZ на двойном трансмонном каплере Toshiba — 99.90% за 48 нс [D][4].

Типичное при ≥ 100 кубитах: Willow, 105 кубитов — средний T1 68 мкс, ошибка CZ 0.33%, считывание 99.5%, цикл QEC 1.1 мкс [D][7][C][14]; по парку IBM ошибка на слоёный гейт 3.7×10⁻³ типично, 1.9×10⁻³ на лучшем устройстве (2026-07) [C][15]; Zuchongzhi 3.0, 105 кубитов — двухкубитный гейт 99.62%, считывание 99.13% [D][16]; чиплеты Rigetti Cepheus-1-108Q — медианный двухкубитный 99.1% [C][G:RIGETTI-FIN-2026].

| Год | Показатель | Кто | Свидетельство |
|---|---|---|---|
| 2019 | Sycamore, 53 кубита, одновременная двухкубитная ошибка 0.62% | Google | [D][20] |
| 2023 | Condor, 1,121 кубит на одном кристалле | IBM | [C][21] |
| 2024 | Willow, 105 кубитов, Λ = 2.14 | Google | [D][7] |
| 2025 | Двумерный трансмон, T1 1.68 мс | Princeton | [D][8] |
| 2026 | Логическая ошибка при d=7 — 7.72×10⁻⁴ за цикл | Google | [D][10] |

На масштабе крупнейший член ошибки — двухкубитный гейт (~40% бюджета цветного кода у Google) [D][22], далее считывание (~10⁻² на парках машин [C][15]) и утечка; хвост распределения по решётке значит больше, чем медиана.

## Производство, материалы и цепочка поставок

Процесс: Nb или Ta на высокоомном Si либо на сапфире; переходы Al/AlOx/Al, напыляемые через теневую маску; трёхмерная интеграция методом flip-chip. На 300-мм КМОП-оборудовании imec/KU Leuven сообщили о 393 работающих трансмонах из 400 (98.25%) при медианном T1 ≈ 75 мкс (42–113 мкс) [D][23][G:IMEC-300MM-2025]: достижение по однородности, а не по когерентности. Решётки с фиксированной частотой обязаны, кроме того, попадать в целевые частоты (разброс переходов оборачивается коллизиями) — с помощью лазерного отжига (IBM), отжига со знакопеременным смещением (Rigetti, успех 97.4%) [D][24] или перестраиваемых каплеров.

Стоимость и энергия: ни один поставщик не публикует $/кубит; косвенные ориентиры — контракт IQM на LUMI стоимостью €33 M [P][26] и 14-нм криоконтроллер IBM с 23 мВт на кубит при 4 K [D][27] — десятки ватт на 10³ кубитах, отсюда и аргумент в пользу SFQ (заявляются нВт на кубит [C][58]).

Цепочка поставок: рефрижераторы растворения от Bluefors (Финляндия), Oxford Instruments (Великобритания), FormFactor и Maybell (США); ³He — из распада трития в государственных запасах (США: NNSA [G][55]), коммерческого производителя нет; 4-К HEMT-усилители фактически от одного поставщика (Low Noise Factory, Швеция); электроника управления — конкурентный рынок (Quantum Machines, Qblox, Zurich Instruments); коммерческие QPU от QuantWare (Нидерланды) [P][29]; фабрики (foundry) — Anderon (выделена из IBM Albany, 2026-05; письмо о намерениях CHIPS на $1 B, отдельно заявлен $1 B собственных средств IBM) [P][30][G][31] и GlobalFoundries (LOI на $375 M) [G][31].

Экспортный контроль: промежуточное окончательное правило BIS от 2024-09-06 охватывает квантовые вычислители от 34 кубитов (ECCN 4A906), рефрижераторы растворения с ≥ 600 мкВт при 0.1 K в течение 48 ч (3A904), криогенные зондовые станции для пластин (3B904) и параметрические усилители (3A901.b) [G][32][G:BIS-QUANTUM-2024]; поэтому китайские поставщики строят рефрижераторы на 10 мК собственными силами (2026-05-15) [P][19].

## Управление, считывание и нагрузка на ввод-вывод

Перестраиваемая решётка требует одной линии XY и одной линии Z на кубит плюс по одной на каплер (Sycamore: ≈ 3.6 управляющей линии на кубит без учёта считывания [D][20]); считывание мультиплексирует ≈ 6–10 кубитов на одну подводящую линию [D][7]; каждая линия — это канал ЦАП плюс коаксиал с аттенюаторами, так что и стоимость, и тепловыделение растут вместе с N.

Задержки: цикл QEC составляет 1.1 мкс; декодер Google, работающий в реальном времени, показал среднюю задержку 63 мкс при d=5 [D][7]; Relay-BP от IBM в моделировании нацелен на < 1 мкс на цикл [S][33] для gross-кода (qLDPC-код IBM типа bivariate bicycle [[144,12,12]], 12 логических кубитов на 288 физических [D][57]).

Стены: 10³ достигнуто (Condor, 1,121 кубит [C][21]); KIDE от Bluefors (> 4,000 ВЧ-линий, > 1,000 кубитов; страница продукта, 2026-06) [C][34] — потолок одного криостата. Для 10⁴ нужен cryo-CMOS при 4 K (HRL: код повторения d=5 от контроллера мощностью ≤ 3.5 Вт [D][35][G:HRL-2026]) либо SFQ на милликельвинах (SEEQC: однокубитные гейты до 99.9% на ≤ 5 кубитах [D][28][G:SEEQC-2026]) плюс модули из нескольких криостатов (IBM связала две ячейки, 2026-08 [C][36]). Для 10⁶ замкнутого проекта нет: ЦАП потока на кристалле, холодное декодирование и межкриостатные линии (ETH: 30 м при точности состояния Белла 80.4% [D][37]) не дотягивают по масштабу.

## Роль в стеке

Пути платформы: сверхпроводниковый путь и путь dual-rail-стирания (трансмон как анцилла или как один из «рельсов»); внедиагонального прочтения нет, хабом не является. Требует сверхпроводниковой литографии; поставляет носитель для гейтов на перестраиваемых каплерах и для кросс-резонансных гейтов, анциллу для гейтов на бозонных резонаторах, подпространство «голого» кубита, дисперсионный сдвиг для СВЧ-считывания и СВЧ-сторону оптического преобразователя. Замещается флаксониумом, который покупает ангармоничность и T1 ценой смещения по потоку на каждый кубит, управления в суб-ГГц-диапазоне и переработанного считывания. Конфликтует с управлением на SFQ: фотоны переключения отравляли кубиты квазичастицами в многокристальном модуле 2023 г. (0.96 из 1.2% ошибки на клиффорд) [D][39]; SEEQC утверждает, что устранила это конструктивно [C][58], так что конфликт остаётся в силе до независимой проверки на масштабе решётки. Производный такт сверхпроводникового пути ≈ 2.8×10⁻⁷ с (280 нс; производный такт = max(гейт, считывание, транспорт) для пути платформы), ограничен считыванием при гейтовом члене ≈ 40 нс, против измеренного цикла Willow в 1.1 мкс [D][7] — самый быстрый из продемонстрированных путей, за который платит G4 (крупномасштабная отказоустойчивость). Пограничные пустые слоты: СВЧ-оптический преобразователь (≈ на 3 порядка не дотягивающий до удалённых гейтов [S][40]) и криогенное декодирование.

## Верификация (QCVV)

Заголовочные цифры получают из клиффордовского RB/IRB, одновременного XEB (Google), метрик layer fidelity/EPLG у IBM и матриц отнесения при считывании; Λ — это аппроксимация зависимости логической ошибки от расстояния при одном фиксированном декодере. Здесь упускается: изолированная работа против одновременной (рекордные кристаллы измеряются изолированно); когерентные ошибки, усреднённые в одно деполяризующее число; утечка, невидимая для RB и часто удаляемая постселекцией; дрейф между калибровкой и использованием; а также различия в соглашениях (Rigetti приводит медианы, IBM — своё лучшее устройство, IQM — двухкубитный кристалл). «70 логических кубитов» у IBM в 2026-07 — это результат с обнаружением ошибок и постселекцией [D][41], а не отказоустойчивость.

Воспроизведение: подпороговое масштабирование воспроизведено USTC на 107 кубитах с Λ = 1.40 [D][9]. Споры: сэмплирование 2019 г., заявленное как квантовое превосходство, воспроизведено тензорными сетями [D][42]; эксперимент IBM 2023 г. о «полезности» был классически смоделирован в течение нескольких недель [D][43][44]; статья Google от 2026-07 не приводит Λ для прогона с d=7 [D][10]. Расхождение значений: T1 на 300-мм пластинах imec часто цитируют как «> 100 мкс»; медиана в статье равна ≈ 75 мкс [D][23][G:IMEC-300MM-2025] — она и используется здесь.

## Акторы и экономика

**Кто.**

| Организация | Роль | Страна | Деятельность | Свидетельство |
|---|---|---|---|---|
| Google Quantum AI | разработчик | США | Willow на 105 кубитов, Λ = 2.14; память при d=7 | [D][7][10] |
| IBM | разработчик | США | Парк Heron/Nighthawk; дорожная карта Starling; выделение Anderon | [C][15][59][P][30] |
| Rigetti | разработчик | США | Чиплеты Cepheus-1-108Q; собственная фабрика | [C][17] |
| IQM | разработчик | Финляндия | Продано 26 систем, установлено 17 | [C][46][G:IQM-LISTING-2026-07] |
| USTC | исследования | Китай | Zuchongzhi 3.x, 105 кубитов; Λ = 1.40 | [D][9][16] |
| SEEQC | поставщик | США | Управление на SFQ при милликельвинах; интеграция с IBM в рамках QBI | [D][28][G:SEEQC-2026] |

**Деньги.**
- 2025-11-06 · DARPA · QBI Stage B (до $15 M на каждую) · IBM — единственный поставщик трансмонных решёток из одиннадцати; Google и Rigetti остались на Stage A [G][50][G:QBI-STAGEB-2025-11][G:QBI-STAGEA-2025-04]
- 2026-01-20 · D-Wave · сделка M&A, Quantum Circuits (dual-rail-резонаторы на трансмонных анциллах) · $550 M (акции + деньги) · закрыта [C][48][G:DWAVE-QCI-2026-01][G:DUALRAIL-CZ-2026-08]
- 2026-05-05 · QuantWare (коммерческие QPU; дорожная карта VIO-40K [R][G:QUANTWARE-VIO]) · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners (новые инвесторы, ведущего нет) · суммарно > $210 M · закрыт [P][29]
- 2026-05-18 · Nord Quantique · финансирование роста через капитал · $30 M при оценке $1.4 B · закрыто [C][49][G:NQ-1.4B-2026-05]
- 2026-05-21 · US Dept of Commerce · письма о намерениях CHIPS ($2.013 B, девять компаний) · IBM/Anderon $1 B, GlobalFoundries $375 M, Rigetti ≤ $100 M, D-Wave $100 M · необязывающие LOI [G][31][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · обязательство · > $10 B за пять лет, $1 B собственных средств в Anderon заявлен отдельно · объявлено [C][45][G:IBM-10B-2026-06]
- 2026-06-03 · OQC (разработчик coaxmon [D][25]) · Series C · £260 M (~$350 M) · ведущий инвестор Bullhound · оценка не раскрыта · закрыт [C][47][G:OQC-SERIESC-2026-06]
- 2026-07-02 · IQM · листинг, Nasdaq и Хельсинки · денежные средства pro forma €337 M · закрыт [C][G:IQM-LISTING-2026-07]
- 2026-08-04 · IQM · результаты H1-2026 · выручка €8.9 M (+47%), денежные средства €309 M · отчёт [P][26]
- 2026-08-06 · Rigetti · результаты Q2-2026 · выручка $5.1 M, убыток по GAAP $52.6 M, денежные средства $541.3 M · отчёт [C][17]

**Рынок и цепочка поставок.** Обеспечивающее оборудование сконцентрировано сильнее, чем рынок самих QPU. Юнит-экономика не опубликована; контракт IQM на €33 M [P][26] и цена Quantum Circuits в $550 M [C][G:DWAVE-QCI-2026-01] — единственные точки, которые можно процитировать. Платящие цели: сегодня G7 (развёртываемые системы) и G2 (полезность с подавлением ошибок); G3 (ранняя отказоустойчивость) — через программы типа QBI начиная с 2027 г. [G:QBI-STAGEC-2026]; G4 (крупномасштабная отказоустойчивость) — после 2029 г. [R][G:IBM-ROADMAP]; G1 (аналоговое моделирование), G5 (оптимизация) и G6 (сети) не приносят выручки, специфичной для трансмонов.

**ИС и стандарты.** PatSnap (данные до 2026-06-30): IBM — 4,388 квантовых патентных семейств, Google — 2,385, Microsoft — 1,175; по сверхпроводниковым устройствам (H10N 60) IBM — 783, Google — 357 [P][52][G:PATSNAP-2026-06]. Судебных споров не найдено; семейство, специфичное именно для трансмона, подтвердить не удалось. Открытые стеки превращают вышележащий слой в общедоступный товар: Qiskit (IBM заявляет ≈ 70% разработчиков [C][45]), Cirq/Stim, OpenQASM 3, NVQLink [C][G:NVQLINK-2025].

**Дорожные карты и послужной список.**
- IBM Kookaburra (2022-05-10 · 2025 г., как многокристальный процессор на 1,386 кубитов [C][56]; переобещан 2025-06-10 · 2026 г., как первый qLDPC-модуль [R][59] · не поставлен по состоянию на 2026-09-03 [R][53][G:IBM-ROADMAP]).
- IBM Nighthawk (2025-06-10 · 2025 г. · поставлен 2025-12) и Starling (2025-06-10 · 2029 г., 200 логических кубитов / 10⁸ гейтов · открыт) [R][G:IBM-ROADMAP].
- Веха 3 у Google, логическая ошибка 10⁻⁶ (без даты · преемник Willow не опубликован; нейтрально-атомное направление открыто 2026-03-24) [R][10][G:GOOGLE-ATOMS-2026-03].
- Rigetti, 108 кубитов при 99.5% (обещано на конец 2025 г. · общая доступность 2026-04-07 при медиане 99.1%; 99.5% перенесены на «более поздний 2026 год») [C][G:RIGETTI-FIN-2026].
- Fujitsu/RIKEN, 1,000 кубитов (обещано 2025-04-22 · 2026 финансовый год · не запущены по состоянию на 2026-09-03) [R][18][G:FUJITSU-1000Q].
Достоверность: у IBM высокая по ритмичности поставок, слабая по первому qLDPC-модулю и по заявлениям о «преимуществе»; у Google высокая по физике, непрозрачная по срокам; у Rigetti — хронические срывы сроков; Fujitsu ничем не подтверждена.

**Стратегическое прочтение.** Если победят трансмоны, выиграют владельцы фабрик и поставщики криогеники — независимо от того, какой именно вендор победит; проиграют бесфабричные трансмонные стартапы, и консолидация уже видна (Atlantic Quantum → Google, 2025-10-03 [P][38][G:GOOGLE-ATLANTIC-2025-10]; Quantum Circuits → D-Wave). Угрозы замещения: флаксониум на той же фабрике, кодирования dual-rail и бозонные, низводящие трансмон до анциллы, атомы и спины — ради плотности. Переговорной силой обладают поставщики ³He, HEMT-усилителей и криостатов; поставщики платформ уходят от неё через вертикальную интеграцию.

*Открытая ниша:* разрыв в достоверности лежит в QCVV на масштабе — в бенчмарках с одновременной работой, учётом дрейфа и разрешением по утечке и всплескам, которых недостаёт покупателям (EuroHPC, C-DAC, аудиты в духе DARPA), — а конфликт трансмон–SFQ (отравление квазичастицами при холодном цифровом управлении) есть измерительная задача, которую компания уровня QCVV/SFQ может занять первой.

## Прогноз и открытые вопросы

Вехи на 12–24 месяца: (1) Kookaburra исполняет память на gross-коде ниже точки безубыточности — подтверждение; отсутствие результата к концу 2027 г. понижает в ранге дату IBM «2029» [R][G:IBM-ROADMAP]. (2) Google публикует Λ ≥ 3 либо логическую память с ошибкой 10⁻⁶ при d ≥ 9 — подтверждение; второй год без преемника Willow — понижение [D][10]. (3) QBI Stage C (ожидается около Q4 2026 [G:QBI-STAGEC-2026][P][51]) продвигает поставщика на трансмонах. (4) SFQ или cryo-CMOS управляет ≥ 50 трансмонами без потери точности [D][28][35]. Лучший сценарий на 2029 г.: машина класса Starling на 200 логических кубитов [R][G:IBM-ROADMAP] и память Google при d ≥ 11; худший: Λ около 2, считывание на уровне 10⁻², всплески ограничивают расстояние, трансмон выживает лишь в роли анциллы, а капитал перетекает к атомам и спинам. Открытые вопросы: переживает ли миллисекундная когерентность Ta/Si переход к 100-кубитному процессу с каплерами; является ли предел двухкубитной ошибки на масштабе когерентным (калибровочным) или некогерентным; способно ли считывание достичь 10⁻³ за < 300 нс по всей решётке. Следить за: следующей статьёй Google, Kookaburra, списком Stage C.

## Источники

[1] Koch et al. · Charge-insensitive qubit design derived from the Cooper pair box · Phys. Rev. A 76, 042319 · 2007-10 · https://arxiv.org/abs/cond-mat/0703002
[2] Paik et al. · Observation of high coherence in Josephson junction qubits measured in a three-dimensional circuit QED architecture · Phys. Rev. Lett. 107, 240501 · 2011-12 · https://arxiv.org/abs/1105.4652
[3] Barends et al. · Superconducting quantum circuits at the surface code threshold for fault tolerance · Nature 508, 500 · 2014-04 · https://arxiv.org/abs/1402.4848
[4] Toshiba (Kubo et al.) · Double-transmon coupler CZ 99.90% in 48 ns · Phys. Rev. X 14, 041050 · 2024-11 · https://journals.aps.org/prx/abstract/10.1103/PhysRevX.14.041050
[5] [P] The Quantum Insider · Oxford researchers demonstrate fast 99.8%-fidelity two-qubit gate (25 ns CZ) · trade press · 2025-03-26 · https://thequantuminsider.com/2025/03/26/oxford-researchers-demonstrate-fast-99-8-fidelity-two-qubit-gate-using-simplified-circuit-design/
[6] Kandala et al. (IBM) · Engineered-ZZ cross-resonance CNOT at 99.77% · Phys. Rev. Lett. 127, 130501 · 2021-09 · https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.130501
[7] Google Quantum AI · Quantum error correction below the surface code threshold · Nature · 2024-12 · https://www.nature.com/articles/s41586-024-08449-y
[8] Bland et al. (Princeton) · 2D transmons with lifetimes and coherence times exceeding 1 millisecond · arXiv:2503.14798; Nature · 2025-03-19 · https://arxiv.org/abs/2503.14798
[9] USTC · 107-qubit surface code below threshold with leakage reset · Phys. Rev. Lett. · 2025-12 · https://journals.aps.org/prl/abstract/10.1103/rqkg-dw31
[10] Google Quantum AI · RL-steered QEC, d=7 logical error 7.72×10⁻⁴ per cycle (arXiv:2511.08493) · Nature · 2026-07 · https://www.nature.com/articles/s41586-026-10759-2
[11] McEwen et al. · Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits · Nature Physics 18, 107 · 2022-01 · https://arxiv.org/abs/2104.05219
[12] McEwen et al. · Resisting high-energy impact events through gap engineering in superconducting qubit arrays · arXiv:2408.13687 · 2024-08 · https://arxiv.org/abs/2408.13687
[13] IQM · Above 99.9% fidelity single-qubit gates, two-qubit gates, and readout in a single superconducting quantum device · arXiv:2508.16437; PRX Quantum · 2025-08 · https://arxiv.org/abs/2508.16437
[14] [C] Google Quantum AI · Willow fidelities and "Quantum Echoes" verifiable advantage · Google blog · 2025-10 · https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/
[15] [C] IBM Quantum · What's new Q2 2026 (fleet EPLG) · IBM Quantum blog · 2026-07 · https://www.ibm.com/quantum/blog/whats-new-q2-2026
[16] Gao et al. (USTC) · Zuchongzhi 3.0, 105-qubit processor · Phys. Rev. Lett. 134, 090601 · 2025-03 · https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.090601
[17] [C] Rigetti · Second-quarter 2026 financial results · investor release · 2026-08-06 · https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2026-financial-results
[18] [C] Fujitsu · Quantum research page (1,000-qubit machine, fiscal 2026) · fujitsu.com · accessed 2026-09-03 · https://global.fujitsu/en-global/technology/research/quantum
[19] [P] The Quantum Insider · 10-plus companies leading the quantum technologies race in China · trade press · 2026-05-15 · https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/
[20] Arute et al. · Quantum supremacy using a programmable superconducting processor · Nature 574, 505 · 2019-10 · https://www.nature.com/articles/s41586-019-1666-5
[21] [C] IBM · Quantum roadmap to 2033 (Condor 1,121 qubits) · IBM Quantum blog · 2023-12 · https://www.ibm.com/quantum/blog/quantum-roadmap-2033
[22] Google Quantum AI · Scaling and logic in the colour code on a superconducting quantum processor · Nature · 2025-05 · https://www.nature.com/articles/s41586-025-09061-4
[23] Van Damme et al. (imec/KU Leuven) · Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers · Nature 634 · 2024-09-18 · https://www.nature.com/articles/s41586-024-07941-9
[24] Rigetti (Pappas et al.) · Alternating-bias assisted annealing of junctions · Communications Materials · 2024-08 · https://www.nature.com/articles/s43246-024-00596-z
[25] OQC · More than 500 qubits on one 3-inch die · arXiv:2602.12773 · 2026-02 · https://arxiv.org/abs/2602.12773
[26] [P] Investing.com · IQM Q2 2026 results slides: backlog up 52%, revenue up 47% in H1 · trade press · 2026-08 · https://www.investing.com/news/company-news/iqm-q2-2026-slides-backlog-surges-52-revenue-up-47-in-h1-93CH-4834587
[27] IBM · 14 nm cryo-CMOS qubit controller at 4 K · PRX Quantum 5, 010326 · 2024-02 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.5.010326
[28] SEEQC · SFQ qubit control at millikelvin · Nature Electronics · 2026-03-10 · https://www.nature.com/articles/s41928-026-01576-6
[29] [P] PostQuantum · QuantWare $178 M Series B (Intel Capital, In-Q-Tel, ETF Partners) · trade press · 2026-05-06 · https://postquantum.com/industry-news/quantware-178m-series-b-qoa/
[30] [P] Tom's Hardware · IBM spins off Anderon quantum chip foundry · trade press · 2026-05 · https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding
[31] US Department of Commerce / NIST · Letters of intent to 9 quantum companies, $2 billion · nist.gov · 2026-05-21 · https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion
[32] US BIS · Interim final rule: quantum ECCNs 4A906, 3A904, 3B904, 3A901.b · Federal Register (BIS-2024-0020) · 2024-09-06 · https://downloads.regulations.gov/BIS-2024-0020-0001/content.htm
[33] IBM · Relay-BP decoder for bivariate-bicycle codes on FPGA · arXiv:2510.21600 · 2025-10 · https://arxiv.org/abs/2510.21600
[34] [C] Bluefors · KIDE cryogenic platform (> 4,000 RF lines, > 1,000 qubits) · product page · revised 2026-06-16, accessed 2026-09-03 · https://bluefors.com/products/kide-cryogenic-platform/
[35] HRL Laboratories · Self-sequencing 4 K controller running a d=5 repetition code · arXiv:2604.16216; Nature · 2026-04-17 · https://arxiv.org/abs/2604.16216
[36] [C] IBM · Modular cryogenics: two coupled cells · IBM Quantum blog · 2026-08 · https://www.ibm.com/quantum/blog/modular-cryogenics
[37] Storz et al. (ETH Zürich) · Loophole-free Bell inequality violation with superconducting circuits (30 m cryogenic link, Bell-state fidelity 80.4%) · Nature 617, 265 · 2023-05 · https://www.nature.com/articles/s41586-023-05885-0
[38] [P] The Quantum Insider · Atlantic Quantum joins Google Quantum AI · trade press · 2025-10-03 · https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/
[39] Liu et al. · SFQ multi-chip module control limited by quasiparticle poisoning · PRX Quantum 4, 030310 · 2023-07 · https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.4.030310
[40] (authors not recorded) · Microwave–optical transduction gap analysis · arXiv:2503.10842 · 2025-03 · https://arxiv.org/abs/2503.10842
[41] Martiel, Chung, Seif, Ghosh, Hincks, Deshpande, Fefferman, Gambetta, Javadi-Abhari (IBM) · "Sampling hard circuits with verifiably high fidelity" — 70-qubit, depth-70 logical circuit with 468 T gates encoded in spacetime codes on 97 physical qubits, ~10× error suppression by syndrome post-selection · arXiv:2607.25941 · 2026-07-28 · https://arxiv.org/abs/2607.25941
[42] Pan, Chen, Zhang · Solving the sampling problem of the Sycamore quantum circuits · Phys. Rev. Lett. 129, 090502 · 2022-08 · https://arxiv.org/abs/2111.03011
[43] Kim et al. (IBM) · Evidence for the utility of quantum computing before fault tolerance · Nature 618, 500 · 2023-06 · https://www.nature.com/articles/s41586-023-06096-3
[44] Tindall et al. · Efficient tensor network simulation of IBM's Eagle kicked Ising experiment · PRX Quantum 5, 010308 · 2024-01 · https://arxiv.org/abs/2306.14887
[45] [C] IBM · IBM commits more than $10 billion to quantum computing · IBM newsroom · 2026-06-02 · https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers
[46] [C] IQM · IQM becomes first European quantum computing company listed on a major U.S. exchange · press release · 2026-07-02 · https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/
[47] [C] OQC · Series C, £260 M led by Bullhound · OQC newsroom · 2026-06-03 · https://oqc.tech/company/newsroom/series-c
[48] [C] D-Wave · D-Wave to acquire Quantum Circuits Inc. · press release · 2026-01-07 · https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/
[49] [C] Nord Quantique · Nord Quantique reaches $1.4 billion USD valuation · Business Wire · 2026-05-18 · https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment
[50] DARPA · QBI Stage B selection · darpa.mil · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
[51] [P] Quantum Ledger · DARPA QBI tracker (rosters, 2026-03 solicitation, Stage C timing) · secondary database · 2026-03 · https://quantumledger.report/darpa-qbi
[52] [P] PatSnap · Quantum computing patent landscape (data to 2026-06-30) · PatSnap blog · 2026-07 · https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape/
[53] [C] IBM · Quantum development and innovation roadmap (Kookaburra listed for 2026) · ibm.com · accessed 2026-09-03 · https://www.ibm.com/roadmaps/quantum/
[54] Jin et al. (MIT) · Thermal and residual excited-state population in a 3D transmon qubit · Phys. Rev. Lett. 114, 240501 · 2015-06 · https://arxiv.org/abs/1412.2772
[55] US GAO · Managing critical isotopes: weaknesses in DOE's management of helium-3 delayed the federal response to a critical supply shortage (GAO-11-472) · gao.gov · 2011-05-12 · https://www.gao.gov/products/gao-11-472
[56] [C] IBM · Expanding the IBM Quantum roadmap to anticipate the future of quantum-centric supercomputing (Kookaburra 1,386 q in 2025) · IBM Quantum blog · 2022-05-10 · https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025
[57] Bravyi et al. (IBM) · High-threshold and low-overhead fault-tolerant quantum memory · Nature 627, 778 · 2024-03 · https://arxiv.org/abs/2308.07915
[58] [P] Quantum Computing Report · SEEQC and IBM collaborate on SFQ control integration under DARPA's QBI · trade press · 2025-06-12 · https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/
[59] [C] IBM · IBM sets the course to build world's first large-scale, fault-tolerant quantum computer (Starling 2029, Blue Jay 2033) · IBM newsroom · 2025-06-10 · https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center

## Открытые пункты верификации

- Рыночная капитализация IQM ≈ $2.6 B (2026-08): первичного источника не найдено; показатель не приводится.
- Цель Rigetti «1,000 кубитов / 99.9%» и её дата: источник для них не установлен, обе величины опущены.
- Bluefors KIDE, «> 4,000 ВЧ-линий / > 1,000 кубитов»: страница продукта обновлена 2026-06-16; дата выпуска не установлена.
- IBM, «> $1.1 B клиентских контрактов с 2017 г.» [C][45]: независимо не подтверждено; показатель не приводится.
- Время кросс-резонансного гейта ≈ 200–500 нс: типичный для парка диапазон, выведенный из статьи по одному устройству [6]; источника по всему парку нет.
- Число чиплетов в Cepheus-1-108Q: подтверждённой цифры нет, поэтому она не приводится.
- Выход годных imec на 300 мм — 393 из 400 (98.25%): приводится со ссылкой на [23]; медианный T1 для этого запуска ≈ 75 мкс.
- Источник [40] (arXiv:2503.10842): список авторов не приводится; разрыв в преобразовании «≈ 3 порядка» приводится по литературе.
- «4-К HEMT-усилители фактически от одного поставщика (Low Noise Factory)»: рыночное наблюдение; источника в виде базы данных нет.
