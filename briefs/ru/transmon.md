---
id: transmon
name: Трансмон
layer: 1 Носитель
status: demonstrated
since: 2007
one_line: Джозефсоновский переход, шунтированный ёмкостью (Koch, 2007); носитель, стоящий за Willow, Heron/Nighthawk и Zuchongzhi, с самым быстрым детерминированным гейтом и самым быстрым циклом QEC среди всех продемонстрированных кубитов.
verdict: Наиболее финансируемый и самый быстрый носитель, ограниченный на масштабе двухкубитными ошибками ~10⁻³ и ошибками считывания ~10⁻², а также коррелированными всплесками раз в час. Подтвердить, если решётка из ≥100 кубитов покажет Λ ≥ 3 при медианной двухкубитной ошибке < 10⁻³ к 2028 г.; иначе понизить до статуса компонента.
updated: 2026-09-03
---

Λ = коэффициент подавления ошибок на шаг кодового расстояния; QBI = DARPA Quantum Benchmarking Initiative (Stage A — концепция → B — план НИОКР → C — государственная верификация и валидация); G1–G7 = классы целей отчёта (см. «Акторы и экономика»).

## Идентичность и происхождение

Трансмон — это джозефсоновский переход Al/AlOx/Al, шунтированный большой ёмкостью так, что E_J/E_C ≈ 50–100 [D][206]. Зарядовая дисперсия падает экспоненциально по √(8E_J/E_C), что снимает зарядовый шум 1/f ценой слабой ангармоничности α ≈ −E_C ≈ от −200 до −300 МГц; кубитом служат два нижних уровня осциллятора на 4–6 ГГц [D][206]. Koch et al. предложили его в 2007 г. [D][206]; трёхмерный трансмон (2011) [D][207] и Xmon от UCSB/Google (2014) [D][208] закрепили две линии, используемые до сих пор: с фиксированной частотой (IBM) и с перестройкой по потоку (Google, IQM, USTC).

Атрибуты (граф технологий):
- a: сродство 1.0, изготовленный (природного аналога нет).
- b: характерное время 10⁻⁸ с, детерминированное запутывание; ограничение на утечку (leakage) вида 1/α ставит нижнюю границу длительности импульса около 10 нс.
- c: считывание — дисперсионное СВЧ, 10⁻⁶·⁵ с (≈ 320 нс), неразрушающее, пригодное для внутрисхемного (mid-circuit) применения.
- d: подвижность — статичен, разводка на ближайших соседей.
- e: управление — СВЧ от электроники при комнатной температуре; варианты с холодной ступенью (cryo-CMOS, SFQ) — на ≤ 5 кубитах.
- f: структура ошибок — утечка + стохастические паулиевские + коррелированные всплески + когерентные/калибровочные.
- g: производство — сверхпроводниковая литография.

## Физика и пределы

Остаточная тепловая населённость (0.1% при 35 мК в трёхмерном трансмоне [D][209], ≈ 1% при 40–60 мК для кубита на 5 ГГц [S][209]) делает сброс и считывание нижней границей SPAM. Ангармоничность ограничивает однокубитные гейты 10–25 нс, а CZ на перестраиваемом каплере — 25–50 нс [D][1], [36][P][210]; кросс-резонанс требует ≈ 200–500 нс [D][211].

Предел задаётся декогерентностью за время гейта: при среднем T1 = 68 мкс у Willow [D][1] CZ длительностью 40 нс несёт ≈ 6×10⁻⁴ некогерентной ошибки [S][1]; при рекордном T1 = 1.68 мс одиночного тестового трансмона Ta на Si [D][212] она падает ниже 5×10⁻⁵ [S][212]. В потерях доминируют двухуровневые системы (TLS) в аморфных оксидах на границах раздела [D][212], ниже них — квазичастицы, распад Парселла и шум магнитного потока.

Бо́льшая часть свёрнутого твёрлингом канала — стохастические паулиевские ошибки, поэтому Λ = 2.14 у Willow [D][1] согласуется с теорией. Утечка в |2⟩ накапливается под QEC, если не удалять её каждый цикл (полностью СВЧ-сброс у USTC снизил её в 72×, до 6.4×10⁻⁴, на 107 кубитах [D][3]). Когерентные ошибки (остаточное ZZ, дрейф TLS) вынудили применять перекалибровку с обучением с подкреплением прямо внутри прогона QEC у Google в 2026-07 [D][2]. Коррелированные всплески (ионизирующие частицы, наводняющие кристалл квазичастицами) поражают все кубиты разом — примерно один на 10 с на Sycamore в 2021 г. [D][213] и около одного в час на Willow после инженерии сверхпроводящей щели [D][1], [214], — обрывая длинные прогоны памяти по всплескам, а не по расстоянию. Сдвинуть этот предел означает перейти к новым материалам (Ta, инкапсулированный Nb), к ангармоничности уровня флаксониума, к управлению радиационной обстановкой либо к конверсии в стирание (dual-rail).

## Инженерное состояние (state of the art)

Лучшие изолированные устройства: T1 1.68 мс, Q 2.5×10⁷, однокубитный гейт 99.994% [D][212]; CZ 99.93% и считывание за 280 нс с точностью (fidelity) 99.94% на двухкубитном кристалле IQM [D][37]; CZ на двойном трансмонном каплере Toshiba — 99.90% за 48 нс [D][36].

Типичное при ≥ 100 кубитах: Willow, 105 кубитов — средний T1 68 мкс, ошибка CZ 0.33%, считывание 99.5%, цикл QEC 1.1 мкс [D][1][C][31]; по парку IBM ошибка на слоёный гейт 3.7×10⁻³ типично, 1.9×10⁻³ на лучшем устройстве (2026-07) [C][33]; Zuchongzhi 3.0, 105 кубитов — двухкубитный гейт 99.62%, считывание 99.13% [D][34]; чиплеты Rigetti Cepheus-1-108Q — медианный двухкубитный 99.1% [C][G:RIGETTI-FIN-2026].

| Год | Показатель | Кто | Свидетельство |
|---|---|---|---|
| 2019 | Sycamore, 53 кубита, одновременная двухкубитная ошибка 0.62% | Google | [D][215] |
| 2023 | Condor, 1,121 кубит на одном кристалле | IBM | [C][216] |
| 2024 | Willow, 105 кубитов, Λ = 2.14 | Google | [D][1] |
| 2025 | Двумерный трансмон, T1 1.68 мс | Princeton | [D][212] |
| 2026 | Логическая ошибка при d=7 — 7.72×10⁻⁴ за цикл | Google | [D][2] |

На масштабе крупнейший член ошибки — двухкубитный гейт (~40% бюджета цветного кода у Google) [D][40], далее считывание (~10⁻² на парках машин [C][33]) и утечка; хвост распределения по решётке значит больше, чем медиана.

## Производство, материалы и цепочка поставок

Процесс: Nb или Ta на высокоомном Si либо на сапфире; переходы Al/AlOx/Al, напыляемые через теневую маску; трёхмерная интеграция методом flip-chip. На 300-мм КМОП-оборудовании imec/KU Leuven сообщили о 393 работающих трансмонах из 400 (98.25%) при медианном T1 ≈ 75 мкс (42–113 мкс) [D][217][G:IMEC-300MM-2025]: достижение по однородности, а не по когерентности. Решётки с фиксированной частотой обязаны, кроме того, попадать в целевые частоты (разброс переходов оборачивается коллизиями) — с помощью лазерного отжига (IBM), отжига со знакопеременным смещением (Rigetti, успех 97.4%) [D][218] или перестраиваемых каплеров.

Стоимость и энергия: ни один поставщик не публикует $/кубит; косвенные ориентиры — контракт IQM на LUMI стоимостью €33 M [P][219] и 14-нм криоконтроллер IBM с 23 мВт на кубит при 4 K [D][220] — десятки ватт на 10³ кубитах, отсюда и аргумент в пользу SFQ (заявляются нВт на кубит [C][52]).

Цепочка поставок: рефрижераторы растворения от Bluefors (Финляндия), Oxford Instruments (Великобритания), FormFactor и Maybell (США); ³He — из распада трития в государственных запасах (США: NNSA [G][221]), коммерческого производителя нет; 4-К HEMT-усилители фактически от одного поставщика (Low Noise Factory, Швеция); электроника управления — конкурентный рынок (Quantum Machines, Qblox, Zurich Instruments); коммерческие QPU от QuantWare (Нидерланды) [P][222]; фабрики (foundry) — Anderon (выделена из IBM Albany, 2026-05; письмо о намерениях CHIPS на $1 B, отдельно заявлен $1 B собственных средств IBM) [P][223][G][224] и GlobalFoundries (LOI на $375 M) [G][224].

Экспортный контроль: промежуточное окончательное правило BIS от 2024-09-06 охватывает квантовые вычислители от 34 кубитов (ECCN 4A906), рефрижераторы растворения с ≥ 600 мкВт при 0.1 K в течение 48 ч (3A904), криогенные зондовые станции для пластин (3B904) и параметрические усилители (3A901.b) [G][225][G:BIS-QUANTUM-2024]; поэтому китайские поставщики строят рефрижераторы на 10 мК собственными силами (2026-05-15) [P][226].

## Управление, считывание и нагрузка на ввод-вывод

Перестраиваемая решётка требует одной линии XY и одной линии Z на кубит плюс по одной на каплер (Sycamore: ≈ 3.6 управляющей линии на кубит без учёта считывания [D][215]); считывание мультиплексирует ≈ 6–10 кубитов на одну подводящую линию [D][1]; каждая линия — это канал ЦАП плюс коаксиал с аттенюаторами, так что и стоимость, и тепловыделение растут вместе с N.

Задержки: цикл QEC составляет 1.1 мкс; декодер Google, работающий в реальном времени, показал среднюю задержку 63 мкс при d=5 [D][1]; Relay-BP от IBM в моделировании нацелен на < 1 мкс на цикл [S][46] для gross-кода (qLDPC-код IBM типа bivariate bicycle [[144,12,12]], 12 логических кубитов на 288 физических [D][227]).

Стены: 10³ достигнуто (Condor, 1,121 кубит [C][216]); KIDE от Bluefors (> 4,000 ВЧ-линий, > 1,000 кубитов; страница продукта, 2026-06) [C][228] — потолок одного криостата. Для 10⁴ нужен cryo-CMOS при 4 K (HRL: код повторения d=5 от контроллера мощностью ≤ 3.5 Вт [D][163][G:HRL-2026]) либо SFQ на милликельвинах (SEEQC: однокубитные гейты до 99.9% на ≤ 5 кубитах [D][229][G:SEEQC-2026]) плюс модули из нескольких криостатов (IBM связала две ячейки, 2026-08 [C][48]). Для 10⁶ замкнутого проекта нет: ЦАП потока на кристалле, холодное декодирование и межкриостатные линии (ETH: 30 м при точности состояния Белла 80.4% [D][230]) не дотягивают по масштабу.

## Роль в стеке

Пути платформы: сверхпроводниковый путь и путь dual-rail-стирания (трансмон как анцилла или как один из «рельсов»); внедиагонального прочтения нет, хабом не является. Требует сверхпроводниковой литографии; поставляет носитель для гейтов на перестраиваемых каплерах и для кросс-резонансных гейтов, анциллу для гейтов на бозонных резонаторах, подпространство «голого» кубита, дисперсионный сдвиг для СВЧ-считывания и СВЧ-сторону оптического преобразователя. Замещается флаксониумом, который покупает ангармоничность и T1 ценой смещения по потоку на каждый кубит, управления в суб-ГГц-диапазоне и переработанного считывания. Конфликтует с управлением на SFQ: фотоны переключения отравляли кубиты квазичастицами в многокристальном модуле 2023 г. (0.96 из 1.2% ошибки на клиффорд) [D][231]; SEEQC утверждает, что устранила это конструктивно [C][52], так что конфликт остаётся в силе до независимой проверки на масштабе решётки. Производный такт сверхпроводникового пути ≈ 6.5×10⁻⁷ с (651 нс; производный такт = сумма раунда синдрома: слои гейтов + транспорт + считывание + сброс для пути платформы), из них 282 нс — считывание, а считывание со сбросом дают две трети раунда, против измеренного цикла Willow в 1.1 мкс [D][1] — самый быстрый из продемонстрированных путей, за который платит G4 (крупномасштабная отказоустойчивость). Пограничные пустые слоты: СВЧ-оптический преобразователь (≈ на 3 порядка не дотягивающий до удалённых гейтов [S][232]) и криогенное декодирование.

## Верификация (QCVV)

Заголовочные цифры получают из клиффордовского RB/IRB, одновременного XEB (Google), метрик layer fidelity/EPLG у IBM и матриц отнесения при считывании; Λ — это аппроксимация зависимости логической ошибки от расстояния при одном фиксированном декодере. Здесь упускается: изолированная работа против одновременной (рекордные кристаллы измеряются изолированно); когерентные ошибки, усреднённые в одно деполяризующее число; утечка, невидимая для RB и часто удаляемая постселекцией; дрейф между калибровкой и использованием; а также различия в соглашениях (Rigetti приводит медианы, IBM — своё лучшее устройство, IQM — двухкубитный кристалл). «70 логических кубитов» у IBM в 2026-07 — это результат с обнаружением ошибок и постселекцией [D][45], а не отказоустойчивость.

Воспроизведение: подпороговое масштабирование воспроизведено USTC на 107 кубитах с Λ = 1.40 [D][3]. Споры: сэмплирование 2019 г., заявленное как квантовое превосходство, воспроизведено тензорными сетями [D][233]; эксперимент IBM 2023 г. о «полезности» был классически смоделирован в течение нескольких недель [D][234], [235]; статья Google от 2026-07 не приводит Λ для прогона с d=7 [D][2]. Расхождение значений: T1 на 300-мм пластинах imec часто цитируют как «> 100 мкс»; медиана в статье равна ≈ 75 мкс [D][217][G:IMEC-300MM-2025] — она и используется здесь.

## Акторы и экономика

**Кто.**

| Организация | Роль | Страна | Деятельность | Свидетельство |
|---|---|---|---|---|
| Google Quantum AI | разработчик | США | Willow на 105 кубитов, Λ = 2.14; память при d=7 | [D][1], [2] |
| IBM | разработчик | США | Парк Heron/Nighthawk; дорожная карта Starling; выделение Anderon | [C][33], [62][P][223] |
| Rigetti | разработчик | США | Чиплеты Cepheus-1-108Q; собственная фабрика | [C][236] |
| IQM | разработчик | Финляндия | Продано 26 систем, установлено 17 | [C][56][G:IQM-LISTING-2026-07] |
| USTC | исследования | Китай | Zuchongzhi 3.x, 105 кубитов; Λ = 1.40 | [D][3], [34] |
| SEEQC | поставщик | США | Управление на SFQ при милликельвинах; интеграция с IBM в рамках QBI | [D][229][G:SEEQC-2026] |

**Деньги.**
- 2025-11-06 · DARPA · QBI Stage B (до $15 M на каждую) · IBM — единственный поставщик трансмонных решёток из одиннадцати; Google и Rigetti остались на Stage A [G][60][G:QBI-STAGEB-2025-11][G:QBI-STAGEA-2025-04]
- 2026-01-20 · D-Wave · сделка M&A, Quantum Circuits (dual-rail-резонаторы на трансмонных анциллах) · $550 M (акции + деньги) · закрыта [C][14][G:DWAVE-QCI-2026-01][G:DUALRAIL-CZ-2026-08]
- 2026-05-05 · QuantWare (коммерческие QPU; дорожная карта VIO-40K [R][G:QUANTWARE-VIO]) · Series B · $178 M (€152 M) · Intel Capital, In-Q-Tel, ETF Partners (новые инвесторы, ведущего нет) · суммарно > $210 M · закрыт [P][222]
- 2026-05-18 · Nord Quantique · финансирование роста через капитал · $30 M при оценке $1.4 B · закрыто [C][84][G:NQ-1.4B-2026-05]
- 2026-05-21 · US Dept of Commerce · письма о намерениях CHIPS ($2.013 B, девять компаний) · IBM/Anderon $1 B, GlobalFoundries $375 M, Rigetti ≤ $100 M, D-Wave $100 M · необязывающие LOI [G][224][G:CHIPS-LOI-2026-05]
- 2026-06-02 · IBM · обязательство · > $10 B за пять лет, $1 B собственных средств в Anderon заявлен отдельно · объявлено [C][237][G:IBM-10B-2026-06]
- 2026-06-03 · OQC (разработчик coaxmon [D][238]) · Series C · £260 M (~$350 M) · ведущий инвестор Bullhound · оценка не раскрыта · закрыт [C][57][G:OQC-SERIESC-2026-06]
- 2026-07-02 · IQM · листинг, Nasdaq и Хельсинки · денежные средства pro forma €337 M · закрыт [C][G:IQM-LISTING-2026-07]
- 2026-08-04 · IQM · результаты H1-2026 · выручка €8.9 M (+47%), денежные средства €309 M · отчёт [P][219]
- 2026-08-06 · Rigetti · результаты Q2-2026 · выручка $5.1 M, убыток по GAAP $52.6 M, денежные средства $541.3 M · отчёт [C][236]

**Рынок и цепочка поставок.** Обеспечивающее оборудование сконцентрировано сильнее, чем рынок самих QPU. Юнит-экономика не опубликована; контракт IQM на €33 M [P][219] и цена Quantum Circuits в $550 M [C][G:DWAVE-QCI-2026-01] — единственные точки, которые можно процитировать. Платящие цели: сегодня G7 (развёртываемые системы) и G2 (полезность с подавлением ошибок); G3 (ранняя отказоустойчивость) — через программы типа QBI начиная с 2027 г. [G:QBI-STAGEC-2026]; G4 (крупномасштабная отказоустойчивость) — после 2029 г. [R][G:IBM-ROADMAP]; G1 (аналоговое моделирование), G5 (оптимизация) и G6 (сети) не приносят выручки, специфичной для трансмонов.

**ИС и стандарты.** PatSnap (данные до 2026-06-30): IBM — 4,388 квантовых патентных семейств, Google — 2,385, Microsoft — 1,175; по сверхпроводниковым устройствам (H10N 60) IBM — 783, Google — 357 [P][239][G:PATSNAP-2026-06]. Судебных споров не найдено; семейство, специфичное именно для трансмона, подтвердить не удалось. Открытые стеки превращают вышележащий слой в общедоступный товар: Qiskit (IBM заявляет ≈ 70% разработчиков [C][237]), Cirq/Stim, OpenQASM 3, NVQLink [C][G:NVQLINK-2025].

**Дорожные карты и послужной список.**
- IBM Kookaburra (2022-05-10 · 2025 г., как многокристальный процессор на 1,386 кубитов [C][240]; переобещан 2025-06-10 · 2026 г., как первый qLDPC-модуль [R][62] · не поставлен по состоянию на 2026-09-03 [R][67][G:IBM-ROADMAP]).
- IBM Nighthawk (2025-06-10 · 2025 г. · поставлен 2025-12) и Starling (2025-06-10 · 2029 г., 200 логических кубитов / 10⁸ гейтов · открыт) [R][G:IBM-ROADMAP].
- Веха 3 у Google, логическая ошибка 10⁻⁶ (без даты · преемник Willow не опубликован; нейтрально-атомное направление открыто 2026-03-24) [R][2][G:GOOGLE-ATOMS-2026-03].
- Rigetti, 108 кубитов при 99.5% (обещано на конец 2025 г. · общая доступность 2026-04-07 при медиане 99.1%; 99.5% перенесены на «более поздний 2026 год») [C][G:RIGETTI-FIN-2026].
- Fujitsu/RIKEN, 1,000 кубитов (обещано 2025-04-22 · 2026 финансовый год · не запущены по состоянию на 2026-09-03) [R][70][G:FUJITSU-1000Q].
Достоверность: у IBM высокая по ритмичности поставок, слабая по первому qLDPC-модулю и по заявлениям о «преимуществе»; у Google высокая по физике, непрозрачная по срокам; у Rigetti — хронические срывы сроков; Fujitsu ничем не подтверждена.

**Стратегическое прочтение.** Если победят трансмоны, выиграют владельцы фабрик и поставщики криогеники — независимо от того, какой именно вендор победит; проиграют бесфабричные трансмонные стартапы, и консолидация уже видна (Atlantic Quantum → Google, 2025-10-03 [P][53][G:GOOGLE-ATLANTIC-2025-10]; Quantum Circuits → D-Wave). Угрозы замещения: флаксониум на той же фабрике, кодирования dual-rail и бозонные, низводящие трансмон до анциллы, атомы и спины — ради плотности. Переговорной силой обладают поставщики ³He, HEMT-усилителей и криостатов; поставщики платформ уходят от неё через вертикальную интеграцию.

*Открытая ниша:* разрыв в достоверности лежит в QCVV на масштабе — в бенчмарках с одновременной работой, учётом дрейфа и разрешением по утечке и всплескам, которых недостаёт покупателям (EuroHPC, C-DAC, аудиты в духе DARPA), — а конфликт трансмон–SFQ (отравление квазичастицами при холодном цифровом управлении) есть измерительная задача, которую компания уровня QCVV/SFQ может занять первой.

## Прогноз и открытые вопросы

Вехи на 12–24 месяца: (1) Kookaburra исполняет память на gross-коде ниже точки безубыточности — подтверждение; отсутствие результата к концу 2027 г. понижает в ранге дату IBM «2029» [R][G:IBM-ROADMAP]. (2) Google публикует Λ ≥ 3 либо логическую память с ошибкой 10⁻⁶ при d ≥ 9 — подтверждение; второй год без преемника Willow — понижение [D][2]. (3) QBI Stage C (ожидается около Q4 2026 [G:QBI-STAGEC-2026][P][241]) продвигает поставщика на трансмонах. (4) SFQ или cryo-CMOS управляет ≥ 50 трансмонами без потери точности [D][163], [229]. Лучший сценарий на 2029 г.: машина класса Starling на 200 логических кубитов [R][G:IBM-ROADMAP] и память Google при d ≥ 11; худший: Λ около 2, считывание на уровне 10⁻², всплески ограничивают расстояние, трансмон выживает лишь в роли анциллы, а капитал перетекает к атомам и спинам. Открытые вопросы: переживает ли миллисекундная когерентность Ta/Si переход к 100-кубитному процессу с каплерами; является ли предел двухкубитной ошибки на масштабе когерентным (калибровочным) или некогерентным; способно ли считывание достичь 10⁻³ за < 300 нс по всей решётке. Следить за: следующей статьёй Google, Kookaburra, списком Stage C.

## Источники

[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[2] V. Sivak *et al.*, “Reinforcement learning control of quantum error correction,” *Nature*, vol. 655, no. 8124, pp. 879–884, Jul. 2026, doi: [10.1038/s41586-026-10759-2](https://doi.org/10.1038/s41586-026-10759-2). [D]
[3] T. He *et al.*, “Experimental Quantum Error Correction below the Surface Code Threshold via All-Microwave Leakage Suppression,” *Phys. Rev. Lett.*, vol. 135, no. 26, Art. no. 260601, Dec. 2025, doi: [10.1103/rqkg-dw31](https://doi.org/10.1103/rqkg-dw31). [D]
[14] D-Wave Quantum Inc., “D-Wave Announces Agreement to Acquire Quantum Circuits Inc., Establishing World's Leading Quantum Computing Company,” Jan. 7, 2026. [Online]. Available: https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits-inc-establishing-world-s-leading-quantum-computing-company/ [C]
[31] Y. Chen and M. Devoret, “Our quantum hardware: the engine for verifiable quantum advantage,” Google Blog, Oct. 22, 2025. [Online]. Available: https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/ [C]
[33] IBM Quantum, “What's new at IBM Quantum - Q2 2026.” [Online]. Available: https://www.ibm.com/quantum/blog/whats-new-q2-2026 [C]
[34] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[36] R. Li, K. Kubo, Y. Ho, Z. Yan, Y. Nakamura, and H. Goto, “Realization of High-Fidelity CZ Gate Based on a Double-Transmon Coupler,” *Phys. Rev. X*, vol. 14, no. 4, Art. no. 041050, Nov. 2024, doi: [10.1103/PhysRevX.14.041050](https://doi.org/10.1103/PhysRevX.14.041050). [arXiv:2402.18926](https://arxiv.org/abs/2402.18926). [D]
[37] F. Marxer *et al.*, “Above 99.9% Fidelity Single-Qubit Gates, Two-Qubit Gates, and Readout in a Single Superconducting Quantum Device,” *PRX Quantum*, vol. 7, Art. no. 020333, 2026, doi: [10.1103/n86s-2b88](https://doi.org/10.1103/n86s-2b88). [arXiv:2508.16437](https://arxiv.org/abs/2508.16437). [D]
[40] N. Lacroix *et al.*, “Scaling and logic in the color code on a superconducting quantum processor,” *Nature*, vol. 645, no. 8081, pp. 614–619, May 2025, doi: [10.1038/s41586-025-09061-4](https://doi.org/10.1038/s41586-025-09061-4). [arXiv:2412.14256](https://arxiv.org/abs/2412.14256). [D]
[45] S. Martiel *et al.*, “Sampling hard circuits with verifiably high fidelity,” [arXiv:2607.25941](https://arxiv.org/abs/2607.25941), Jul. 2026. [D]
[46] T. Maurer *et al.*, “Real-time decoding of the gross code memory with FPGAs,” [arXiv:2510.21600](https://arxiv.org/abs/2510.21600), Oct. 2025. [S]
[48] C. Dundon, S. Hall, M. Hollister, and A. Lindler, “IBM's new modular architecture for cryogenic systems,” IBM Quantum Computing Blog, Aug. 19, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/modular-cryogenics [C]
[52] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [C]
[53] M. Swayne, “Atlantic Quantum Joins Google Quantum AI,” The Quantum Insider, Oct. 3, 2025. [Online]. Available: https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/ [P]
[56] IQM Quantum Computers, “IQM Quantum Computers Becomes First European Quantum Computing Company Listed on a Major U.S. Exchange,” Jul. 2, 2026. [Online]. Available: https://iqm.tech/press-releases/iqm-quantum-computers-becomes-first-european-quantum-computing-company-listed-on-a-major-u-s-exchange/ [C]
[57] A. Curbison, “OQC raises £260m in Europe's largest ever private quantum computing funding round,” OQC, Jun. 2, 2026. [Online]. Available: https://oqc.tech/company/newsroom/series-c [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[62] IBM, “IBM Sets the Course to Build World's First Large-Scale, Fault-Tolerant Quantum Computer at New IBM Quantum Data Center,” Jun. 10, 2025. [Online]. Available: https://newsroom.ibm.com/2025-06-10-IBM-Sets-the-Course-to-Build-Worlds-First-Large-Scale,-Fault-Tolerant-Quantum-Computer-at-New-IBM-Quantum-Data-Center [C]
[67] IBM, “Quantum Roadmap.” [Online]. Available: https://www.ibm.com/roadmaps/quantum/ [R]
[70] Fujitsu, “Fujitsu Quantum.” [Online]. Available: https://global.fujitsu/en-global/technology/research/quantum [R]
[84] Nord Quantique, “Nord Quantique Reaches $1.4 Billion USD Valuation with Latest Investment,” Business Wire, May 18, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260518358351/en/Nord-Quantique-Reaches-$1.4-Billion-USD-Valuation-with-Latest-Investment [C]
[163] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[206] J. Koch *et al.*, “Charge-insensitive qubit design derived from the Cooper pair box,” *Phys. Rev. A*, vol. 76, no. 4, Art. no. 042319, Oct. 2007, doi: [10.1103/PhysRevA.76.042319](https://doi.org/10.1103/PhysRevA.76.042319). [arXiv:cond-mat/0703002](https://arxiv.org/abs/cond-mat/0703002). [D]
[207] H. Paik *et al.*, “Observation of High Coherence in Josephson Junction Qubits Measured in a Three-Dimensional Circuit QED Architecture,” *Phys. Rev. Lett.*, vol. 107, no. 24, Art. no. 240501, Dec. 2011, doi: [10.1103/PhysRevLett.107.240501](https://doi.org/10.1103/PhysRevLett.107.240501). [arXiv:1105.4652](https://arxiv.org/abs/1105.4652). [D]
[208] R. Barends *et al.*, “Superconducting quantum circuits at the surface code threshold for fault tolerance,” *Nature*, vol. 508, no. 7497, pp. 500–503, Apr. 2014, doi: [10.1038/nature13171](https://doi.org/10.1038/nature13171). [arXiv:1402.4848](https://arxiv.org/abs/1402.4848). [D]
[209] X. Y. Jin *et al.*, “Thermal and Residual Excited-State Population in a 3D Transmon Qubit,” *Phys. Rev. Lett.*, vol. 114, no. 24, Art. no. 240501, Jun. 2015, doi: [10.1103/PhysRevLett.114.240501](https://doi.org/10.1103/PhysRevLett.114.240501). [arXiv:1412.2772](https://arxiv.org/abs/1412.2772). [D]
[210] C. Choucair, “Oxford Researchers Demonstrate Fast, 99.8% Fidelity Two-Qubit Gate Using Simplified Circuit Design,” The Quantum Insider, Mar. 26, 2025. [Online]. Available: https://thequantuminsider.com/2025/03/26/oxford-researchers-demonstrate-fast-99-8-fidelity-two-qubit-gate-using-simplified-circuit-design/ [P]
[211] A. Kandala *et al.*, “Demonstration of a High-Fidelity CNOT Gate for Fixed-Frequency Transmons with Engineered ZZ Suppression,” *Phys. Rev. Lett.*, vol. 127, no. 13, Art. no. 130501, Sep. 2021, doi: [10.1103/PhysRevLett.127.130501](https://doi.org/10.1103/PhysRevLett.127.130501). [D]
[212] M. P. Bland *et al.*, “2D transmons with lifetimes and coherence times exceeding 1 millisecond,” [arXiv:2503.14798](https://arxiv.org/abs/2503.14798), Mar. 2025. [D]
[213] M. McEwen *et al.*, “Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits,” *Nat. Phys.*, vol. 18, no. 1, pp. 107–111, Dec. 2021, doi: [10.1038/s41567-021-01432-8](https://doi.org/10.1038/s41567-021-01432-8). [arXiv:2104.05219](https://arxiv.org/abs/2104.05219). [D]
[214] M. McEwen *et al.*, “Resisting High-Energy Impact Events through Gap Engineering in Superconducting Qubit Arrays,” *Phys. Rev. Lett.*, vol. 133, no. 24, Art. no. 240601, Dec. 2024, doi: [10.1103/PhysRevLett.133.240601](https://doi.org/10.1103/PhysRevLett.133.240601). [arXiv:2402.15644](https://arxiv.org/abs/2402.15644). [D]
[215] F. Arute *et al.*, “Quantum supremacy using a programmable superconducting processor,” *Nature*, vol. 574, no. 7779, pp. 505–510, Oct. 2019, doi: [10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5). [D]
[216] J. Gambetta, “The hardware and software for the era of quantum utility is here,” IBM Quantum Computing Blog, Dec. 4, 2023. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-roadmap-2033 [C]
[217] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[218] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[219] Investing.com, “IQM Q2 2026 slides: backlog surges 52%, revenue up 47% in H1,” Aug. 4, 2026. [Online]. Available: https://www.investing.com/news/company-news/iqm-q2-2026-slides-backlog-surges-52-revenue-up-47-in-h1-93CH-4834587 [P]
[220] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[221] U.S. Government Accountability Office, “Managing Critical Isotopes: Weaknesses in DOE's Management of Helium-3 Delayed the Federal Response to a Critical Supply Shortage,” U.S. Government Accountability Office, May 2011. [Online]. Available: https://www.gao.gov/products/gao-11-472 [G]
[222] M. Ivezic, “QuantWare Raises $178M Series B — What It Means for Quantum Open Architecture,” PostQuantum.com, May 6, 2026. [Online]. Available: https://postquantum.com/industry-news/quantware-178m-series-b-qoa/ [P]
[223] L. James, “IBM spins off America's first quantum chip foundry with $2 billion in federal and private funding — newly-minted 'Anderon' foundry to offer 300mm quantum wafer fab and manufacturing services,” Tom's Hardware, May 26, 2026. [Online]. Available: https://www.tomshardware.com/tech-industry/quantum-computing/ibm-spins-off-americas-first-quantum-chip-foundry-with-2-billion-in-federal-and-private-funding [P]
[224] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[226] M. U. Rehman, “Top Chinese Quantum Computing Companies in 2026,” The Quantum Insider, May 15, 2026. [Online]. Available: https://thequantuminsider.com/2026/05/15/10-plus-companies-leading-the-quantum-technologies-race-in-china/ [P]
[227] S. Bravyi *et al.*, “High-threshold and low-overhead fault-tolerant quantum memory,” *Nature*, vol. 627, no. 8005, pp. 778–782, Mar. 2024, doi: [10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7). [arXiv:2308.07915](https://arxiv.org/abs/2308.07915). [D]
[228] Bluefors, “KIDE Cryogenic Platform — For Large-Scale Quantum Computing,” Jun. 16, 2026. [Online]. Available: https://bluefors.com/products/kide-cryogenic-platform/ [C]
[229] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[230] S. Storz *et al.*, “Loophole-free Bell inequality violation with superconducting circuits,” *Nature*, vol. 617, no. 7960, pp. 265–270, May 2023, doi: [10.1038/s41586-023-05885-0](https://doi.org/10.1038/s41586-023-05885-0). [D]
[231] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[232] N. Dirnegger *et al.*, “Distilled remote entanglement between superconducting qubits across optical channels,” [arXiv:2503.10842](https://arxiv.org/abs/2503.10842), Mar. 2025. [S]
[233] F. Pan, K. Chen, and P. Zhang, “Solving the Sampling Problem of the Sycamore Quantum Circuits,” *Phys. Rev. Lett.*, vol. 129, no. 9, Art. no. 090502, Aug. 2022, doi: [10.1103/PhysRevLett.129.090502](https://doi.org/10.1103/PhysRevLett.129.090502). [arXiv:2111.03011](https://arxiv.org/abs/2111.03011). [D]
[234] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[235] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[236] Rigetti Computing, “Rigetti Computing Reports Second Quarter 2026 Financial Results,” Rigetti Investor Relations, Aug. 6, 2026. [Online]. Available: https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2026-financial-results [C]
[237] IBM, “IBM Commits More Than $10 Billion to Quantum Computing, Funding Its Roadmap from Today's Leading Systems to the World's First Fault-Tolerant Quantum Computers,” Jun. 2, 2026. [Online]. Available: https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers [C]
[238] O. W. Kennedy *et al.*, “Design and Operation of Wafer-Scale Packages Containing >500 Superconducting Qubits,” [arXiv:2602.12773](https://arxiv.org/abs/2602.12773), Feb. 2026. [D]
[239] PatSnap, “Quantum Computing Patent Landscape 2026,” Jun. 30, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/quantum-computing-patent-landscape/ [P]
[240] J. Gambetta, “Expanding the IBM Quantum roadmap to anticipate the future of quantum-centric supercomputing,” IBM Quantum Blog, May 10, 2022. [Online]. Available: https://www.ibm.com/quantum/blog/ibm-quantum-roadmap-2025 [C]
[241] Quantum Ledger, “DARPA QBI Tracker.” [Online]. Available: https://quantumledger.report/darpa-qbi [P]

## Открытые пункты верификации

- Рыночная капитализация IQM ≈ $2.6 B (2026-08): первичного источника не найдено; показатель не приводится.
- Цель Rigetti «1,000 кубитов / 99.9%» и её дата: источник для них не установлен, обе величины опущены.
- Bluefors KIDE, «> 4,000 ВЧ-линий / > 1,000 кубитов»: страница продукта обновлена 2026-06-16; дата выпуска не установлена.
- IBM, «> $1.1 B клиентских контрактов с 2017 г.» [C][237]: независимо не подтверждено; показатель не приводится.
- Время кросс-резонансного гейта ≈ 200–500 нс: типичный для парка диапазон, выведенный из статьи по одному устройству [211]; источника по всему парку нет.
- Число чиплетов в Cepheus-1-108Q: подтверждённой цифры нет, поэтому она не приводится.
- Выход годных imec на 300 мм — 393 из 400 (98.25%): приводится со ссылкой на [217]; медианный T1 для этого запуска ≈ 75 мкс.
- Источник [232] (arXiv:2503.10842): список авторов не приводится; разрыв в преобразовании «≈ 3 порядка» приводится по литературе.
- «4-К HEMT-усилители фактически от одного поставщика (Low Noise Factory)»: рыночное наблюдение; источника в виде базы данных нет.
