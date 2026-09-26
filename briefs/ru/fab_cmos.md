---
id: fab_cmos
name: CMOS-фабрика 300 mm (спины, cryo-CMOS, сверхпроводниковая разводка)
layer: 10 Производство
status: demonstrated
since: 2022
one_line: Промышленные CMOS-линии 300 mm, изготавливающие спиновые кубиты на квантовых точках, cryo-CMOS-контроллеры и сверхпроводниковую разводку; единственный маршрут производства кубитов со статистикой выхода годных в масштабе пластины.
verdict: Однородность доказана (96% выход годных приборов, субнанометровый CD); точность (fidelity) пока не является поставляемым фабрикой параметром. Понизить ранг, если к концу 2027 г. не появится прибор 300 mm с >20 кубитами и двухкубитной точностью по всем парам ≥ 99.5%.
updated: 2026-09-03
---

"Λ = коэффициент подавления ошибки на один шаг кодового расстояния; QBI = DARPA Quantum Benchmarking Initiative (этап A — концепция → B — план НИОКР → C — государственная верификация и валидация); G1–G7 = классы целей отчёта (см. «Акторы и экономика»)."

## Идентичность и происхождение

Этот узел — производственный режим, а не кубит: производственные линии CMOS 300 mm, изготавливающие массивы квантовых точек, задаваемых затворами (Si/SiGe, Si-MOS, Ge), их cryo-CMOS-ASIC, а также слои сверхпроводниковых кубитов и разводки. Квантовая точка — это транзистор в режиме обогащения при одноэлектронном заполнении; при шаге 45–100 nm фабрика (foundry) даёт однородность, качество границ раздела и изотопный контроль, а не разрешение, — и делает это на десятках тысяч приборов с пластины при криогенном тестировании на уровне пластины.

Маршрут открыла CEA-Leti в 2016 г. спиновым кубитом в маршруте 28 nm FD-SOI [D][584]. Intel и QuTech изготовили первые кубиты 300 mm, сформированные целиком оптической литографией, в марте 2022 г. [D][585], что и фиксирует *since 2022*; в 2024 г. Intel добавила EUV-массивы и статистику по пластине при 1.6 K [D][172], [586]. imec выпустила трансмоны 300 mm в 2024 г. [D][217], а вместе с Diraq — элементарные ячейки с показателями выше 99% в 2025 г. [D][162]. 22FDX от GlobalFoundries стал в 2025 г. коммерчески доступным (merchant) вариантом [D][587], ST запустила партии 28Si FD-SOI в декабре 2025 г. [P][588], а в мае 2026 г. последовали письма о намерениях по программе US CHIPS [G][224].

Атрибуты (граф технологий):
a, сродство к носителю: изготовление, 1.0; сам этот узел и есть изготовление.
b, характерное время: отсутствует; нет ни времени гейта, ни механизма запутывания.
c, считывание: отсутствует.
d, подвижность и связность: отсутствуют.
e, модальность управления: отсутствует.
f, структура ошибок: когерентная; разброс от прибора к прибору читается как ошибка калибровки.
g, производство: CMOS.

## Физика и пределы

Механизм. Фабрика фиксирует четыре наследуемые величины: геометрическую однородность — критический размер в пределах 0.5 nm при шаге 45–100 nm [D][172]; электростатический беспорядок — случайный разброс порогового напряжения 59 mV на Si/SiGe у Intel [D][586]; изотопную чистоту — 800 ppm остаточного 29Si у Intel [D][172] и 400 ppm у imec [D][162]; и качество границы раздела, задающее зарядовый шум, а в Si/SiGe — ещё и распределение долинного расщепления.

Масштабы. T2*/T2echo достигают 5/205 µs на 28Si Si/SiGe против 0.6/98 µs на природном кремнии [D][586]; T2 по Хану достигает 1.31 ms на SiMOS от imec [D][170].

Нижняя граница. Для спинов она материаловедческая: остаточный 29Si, зарядовый шум границы раздела и хвост распределения долинного расщепления в Si/SiGe, превращающий часть точек в стоки утечки (leakage). Для трансмонов это попадание переходов в номинал: разброс сопротивления 8% по пластине даёт разброс частоты 5–7% [D][217] — на порядок выше того, что нужно решётке без частотных коллизий; отжиг со знакопеременным смещением (попадание 97.4% [D][218]) выполняется после фабрики и свойством фабрики не является.

Как это видит код: когерентная, калибруемая ошибка (HRL относит около 80% ошибки CNOT на своём массиве из 54 точек к управлению и калибровке [D][163]) плюс утечка и медленный дрейф; ничто не конвертируется в стирание (erasure); градиенты по пластине [D][217] превращаются в пространственно коррелированную ошибку. Чтобы сдвинуть эту границу, нужны 28Si класса 10 ppm, инженерно заданное долинное расщепление (пока только моделирование [S][589]), дырки в Ge/SiGe или подгонка переходов внутри маршрута.

## Инженерное состояние (state of the art)

Лучшее продемонстрированное: четыре элементарные ячейки Diraq/imec, все операции выше 99% (1Q 99.97%, CZ 99.04–99.56%, SPAM 99.95% при 100 µs), томография набора гейтов, сентябрь 2025 г. [D][162][G:IMEC-300MM-2025]. Типичное на масштабе: 232 двенадцатиточечных прибора Intel на одной пластине дали 99.8% выхода годных точек и 96% выхода годных приборов целиком, май 2024 г. [D][586]; немодифицированный 22FDX дал 28–40% выхода «годных точек» на 1,024 точках, январь 2025 г. [D][587]; восьмикубитный массив imec подтвердил одну пару из четырёх, июль 2026 г. [D][170].

| Год | Показатель | Кто | Тег+ключ |
|---|---|---|---|
| 2016 | спиновый кубит в маршруте 28 nm FD-SOI на пластинах 300 mm | CEA-Leti | [D][584] |
| 2022-03 | >10,000 массивов точек на пластину; 1Q 99.0–99.1% | Intel/QuTech | [D][585] |
| 2024-09 | трансмоны 300 mm: медианное T1 75 µs, выход годных 98.25% | imec/KU Leuven | [D][217] |
| 2024-12 | >24,000 приборов на пластину, CD < 0.5 nm (EUV) | Intel | [D][172] |
| 2025-01 | 1,024 точки на 22FDX, cryo-CMOS-мультиплексор 1:1,024, < 10 min | Quantum Motion/GF | [D][587] |
| 2025-09 | CZ 99.04–99.56% на SiMOS 300 mm, 4 прибора из 4 выше 99% | Diraq/imec | [D][162] |
| 2026-07 | CMOS-контроллер на 4 K (366 ЦАП, ≤ 3.5 W) исполняет повторяющий код d=5, Λ = 4.7 | HRL | [D][163][G:HRL-2026] |

Доминирующий член ошибки: плато 2Q на уровне 99.0–99.6% — это зарядовый шум плюс калибровка обмена [D][162], [163]; считывание длительностью 100 µs ради SPAM класса 99.9% [D][162] задаёт цикл 100–300 µs; ни один прибор 300 mm с числом кубитов больше двенадцати не опубликовал 2Q по всем парам; для трансмонов ограничением служит разброс переходов, а не когерентность [D][217].

## Производство, материалы и цепочка поставок

Платформы. Intel D1: ямы Si/SiGe, иммерсионная и EUV-литография, отбраковка на криозонде [D][172], [586]. imec: SiMOS с перекрывающимися поликремниевыми затворами при шаге ниже 100 nm на 28Si с 400 ppm [D][162], плюс трансмонный маршрут с переходами внахлёст, формируемыми сухим травлением [D][217]. FD-SOI: GlobalFoundries 22FDX (Quantum Motion [D][587]; Equal1 [C][590]) и 28 nm у ST в Crolles на подложках 28Si от Soitec, первые партии — декабрь 2025 г. [P][588]. HRL и SkyWater работают на 200 mm [D][163][C][18].

Выход годных. 96% выхода годных приборов на маршруте, оптимизированном под квантовые задачи [D][586], против 28–40% на коммерческом маршруте [D][587] — центральное число этого узла.

Стоимость и энергия. Ни одна фабрика не публикует цену квантовой пластины; целевой ориентир Diraq < $1 на кубит [R][178] и заявления вендоров об уровне стойки [C][173], [286], [591] аудита не проходили.

Цепочка поставок. Линии: Intel (для собственных нужд); imec — координатор пилотной линии ЕС SPINS [G][592]; подразделение Quantum Technology Solutions в GlobalFoundries [C][284]; IBM Albany, превращающаяся в Anderon, — для сверхпроводниковой разводки, TSV и бампов [C][593]; SkyWater, 200 mm, с 2026-07-31 принадлежит IonQ [C][18]. Материалы: обогащённый 28Si, исторически российский; Silex в июне 2026 г. завершила строительство завода производительностью до 20 kg в год, ввод в эксплуатацию — конец 2026 г., в интересах SQC [C][594]. Оборудование: криогенные зондовые установки для пластин от Bluefors/Afore (< 2 K, 300 mm, 768 линий DC, 48 линий RF) [C][595] и FormFactor [C][596]. Единые точки отказа: EUV-точки только у Intel и imec; один завод 28Si; дуополия на зондовых установках.

Экспортный контроль. Правило BIS от 2024-09-06 контролирует криогенные CMOS-микросхемы для ≤ 4.5 K (ECCN 3A901), криогенные системы ≥ 600 µW при ≤ 0.1 K (3A904), криогенные зондовые установки для пластин (3B904) и квантовые компьютеры начиная с 34 кубитов (4A906), с исключением из лицензирования IEC для союзников [G][225][G:BIS-QUANTUM-2024]; списки ЕС и Великобритании совпадают.

## Управление, считывание и нагрузка на ввод-вывод

Мультиплексирование переезжает на кристалл или в корпус: cryo-CMOS-мультиплексор 1:1,024 на 13 линиях [D][587]; мультиплексор imec, разводящий трансмонные импульсы ниже 15 mK с сохранением 1Q > 99.9% [D][597]; кристалл 28 nm FD-SOI на 32 ячейки при 7 mK, ~20 nW/MHz на ячейку [D][419]; контроллер HRL на 4 K, 366 ЦАП при ≤ 3.5 W (~10 mW на канал), исполняющий повторяющий код [D][163]; контроллер IBM на 4 K с 23 mW на кубит [D][220]. Кроссбарное разделение требует T = 6√g − 1 линий для квадратного массива из g точек (23 для 16) [D][404].

Стены. 10³: индивидуальных линий на кубит достаточно; нагрузкой является время настройки. 10⁴: 10–23 mW на канал при 4 K означают 100–230 W — больше, чем способна принять ступень 4 K любого криостата, что вынуждает перейти к мультиплексированию ≥ 10:1 или к милликельвиновым ячейкам класса nW. 10⁶: закрывается только кроссбарным разделением (~6,000 линий [D][404]) плюс милликельвиновая CMOS или SFQ; удержит ли разделяемое управление когерентную ошибку ниже порога — открытый вопрос. Задержка: спиновые циклы ограничены считыванием, интегрирование 100 µs [D][162].

## Роль в стеке

Корень слоя 10: он не требует ничего и предоставляет массивы точек и криогенные ASIC, которые предполагает спиновый путь платформы. Он замещает изготовление доноров STM-литографией (регистры на 11 кубитов, последовательное изготовление, фабричного маршрута нет [D][165]); для ионных ловушек он — альтернатива MEMS-производствам ловушек, а ценой перехода становится переквалификация под CMOS, которую заплатила Oxford Ionics (с 2025-09-17 в составе IonQ), чья двухкубитная точность 99.99% на кристаллах со стандартной фабрики приведена в релизе IonQ [C][352][G:IONQ-OXIONICS-2025]. Внедиагональное прочтение: естественные носители (захваченные ионы), наследующие полупроводниковое производство. Производный такт = сумма раунда синдрома: слои гейтов + транспорт + считывание + сброс для пути платформы; этот узел своего члена не добавляет; производный раунд спинового пути — 8.5 µs, задан считыванием, против измеренного цикла 100–300 µs [D][162]. Конвейерный шаттлинг на 10 µm с точностью 99.5% [D][169], показанный на приборе делфтского изготовления, — именно то, что должны воспроизводить однородные затворы на 300 mm. Соседние пустые слоты: нет интерконнекта между спиновыми модулями (кандидат — фотоника на 300 mm, при милликельвиновых температурах не подтверждённая) и нет изготовленного криогенного декодера; проект cryo-CMOS-предекодера заявляет сокращение полосы синдромов в 3,780× при мощности ниже 0.56 mW [S][541].

## Верификация (QCVV)

Цифры выхода годных получены на криозондах при 1.6–1.7 K (автоматизированная настройка, критерии открытия/отсечки и зарядового считывания [D][172], [586]): это транзисторная статистика. Точности получены на считаных приборах в рефрижераторах растворения: томография набора гейтов (12,263 последовательности) для элементарных ячеек [D][162], рандомизированный бенчмаркинг на Tunnel Falls [D][172], карты T1/T2 по пластине для трансмонов [D][217].

Не охвачено: (1) зондирование при 1.6 K не видит ни долинного расщепления, ни обмена, ни когерентности, поэтому выход годных приборов ничего не говорит о выходе годных кубитов; (2) отбор: охарактеризованы 4 прибора imec из 20 [D][162], в 2022 г. охлаждены 6 массивов из > 10,000 [D][585]; (3) критерии: 28–40% и 96% по-разному определяют «работающий» [D][586], [587]; (4) ни на одном массиве 300 mm нет одновременного 2Q по всем парам [D][170]; (5) старение: дрейф переходов 3.7% за 146 дней [D][217] в заявлениях о точности отсутствует.

Воспроизводимость: числа imec по SiMOS воспроизводятся на четырёх приборах и в двух организациях [D][162]; у Intel они получены одним поставщиком. Отмечено особо: «первый полностековый кремниевый CMOS-квантовый компьютер» Quantum Motion без опубликованных точностей [C][173]; точки Equal1 на коммерческом процессе без кубитных метрик [C][590].

## Акторы и экономика

**Кто.**

| Организация | Роль | Страна | Что именно делает с технологией | Свидетельство |
|---|---|---|---|---|
| Intel | разработчик; поставщик для собственных нужд | США | EUV-массивы Si/SiGe; статистика по пластинам на криозонде; 12-кубитный кристалл в Argonne | [D][172], [586]; [G][175] |
| imec | исследования; поставщик | Бельгия | точки SiMOS 300 mm, трансмоны, милликельвиновый мультиплексор; координатор SPINS | [D][162], [217], [597]; [G][592] |
| GlobalFoundries | поставщик (коммерческая фабрика) | США | точки на 22FDX и cryo-CMOS; подразделение Quantum Technology Solutions; письмо о намерениях на $375 M | [C][284], [598]; [G][224] |
| IBM | разработчик; поставщик | США | Anderon: сверхпроводниковые пластины 300 mm, TSV, бампы; письмо о намерениях на $1 B | [C][10], [593]; [G][224] |
| Diraq | разработчик | Австралия | элементарные ячейки SiMOS на линии imec; QBI, этап B; письмо о намерениях CHIPS до $38 M | [D][162], [170]; [G][60], [224] |
| Quantum Motion | разработчик | Великобритания | массивы на 1,024 точки на 22FDX; система для NQCC; QBI, этап B | [D][587]; [C][173]; [G][60] |

**Деньги.**

| Дата | Актор | Событие | Сумма | Ведущий инвестор или программа | Накопленно | Статус |
|---|---|---|---|---|---|---|
| 2025-11-06 | Diraq; Quantum Motion; SQC | грант | до $15 M каждому | DARPA QBI, этап B | — | окончательно [G][60][G:QBI-STAGEB-2025-11] |
| 2026-01-15 | Equal1 | раунд | $60 M | ISIF | > $85 M | закрыт [C][591][G:EQUAL1-60M-2026-01] |
| 2026-04-03 | imec + 25 партнёров | грант | €50 M | пилотная линия SPINS, EU Chips JU | — | объявлено [G][592] |
| 2026-05-07 | Quantum Motion | раунд Series C | $160 M | DCVC, Kembara | — | закрыт [C][286][G:QM-160M-2026-05] |
| 2026-05-21 | GlobalFoundries | письмо о намерениях CHIPS | $375 M | Минторг США ($2.013 B по девяти письмам) | — | письмо о намерениях, необязывающее [G][224][C][284][G:CHIPS-LOI-2026-05] |
| 2026-05-21 | IBM (Anderon) | письмо о намерениях CHIPS | $1 B + $1 B собственных средств IBM | Минторг США | — | письмо о намерениях, необязывающее [G][224][C][593] |
| 2026-05-21 | Diraq | письмо о намерениях CHIPS | до $38 M | Минторг США | привлечено > $100 M [P][G:DIRAQ-FUNDING] | письмо о намерениях, средства не выделены [G][224] |
| 2026-06-03 | Quobly | раунд Series A | €115 M | Bpifrance, SEALSQ, STMicroelectronics | €134 M | закрыт [P][599][G:QUOBLY-115M-2026-06] |
| 2026-06 | Silex Systems | завершено строительство завода Q-Si | A$5.1 M + A$4.35 M | Defence Trailblazer; SQC | — | ввод в эксплуатацию в конце 2026 г. [C][594] |
| 2026-07-23 | IBM | M&A: HRL Laboratories | не раскрыта | — | — | объявлено, закрытие в Q3 2026; возможные планы по спиновым кубитам на Anderon [C][10][G:IBM-HRL-2026-07] |
| 2026-07-31 | IonQ | M&A: SkyWater | $15.00 + 0.4883 акции IonQ за акцию (~$1.8 B) | — | — | закрыто [C][18][G:IONQ-SKYWATER-2026] |

**Рынок и цепочка поставок.** Для выручки фабрик квантовая тематика несущественна. Концентрация: две линии точек с EUV, один коммерческий вариант FD-SOI (входит ST), дуополия на зондовых установках, один завод 28Si. Удельная экономика: не публикуется, кроме целевого ориентира Diraq [R][178]. Плательщики: G4 — за CMOS-плотность на 10⁶ кубитов; G7, по состоянию на 3 сентября 2026 г., — за спиновые системы уровня стойки; поставщики сверхпроводниковых систем покупают разводку Anderon/GF ради G2–G4; поставщики ионных систем покупают ловушки со стандартных фабрик ради G2, G3, G7.

**ИС и стандарты.** Портфели: Intel, HRL, Diraq/UNSW, Quantum Motion/UCL, Quobly (лицензии CEA/CNRS), Equal1; публичных судебных споров нет; датированного подсчёта патентных семейств по именованной базе данных не найдено. SPINS обещает квантовые PDK и доступ к мультипроектным пластинам [G][592]; GF продвигает криогенные модели FDX [C][284]; открытого стандарта на криогенные модели приборов не существует.

**Дорожные карты и послужной список.** Intel (обещано в 2022 г. · кубиты в масштабе пластины · выполнено в 2024 г., Argonne 2026-01-06 [G][175][G:INTEL-2026]; преемника или дорожной карты по состоянию на 2026-09-03 нет). Diraq (обещано 2026-07-09 · «тысячи» к 2029 г., переформулировано 2026-08-27 как 150,000 физических · показано восемь кубитов [D][170][R][178][G:DIRAQ-FUNDING]). Quantum Motion (обещано 2025-01 · система для NQCC · поставлена 2025-09-15, точность не опубликована [C][173], [598]). Quobly (обещано 2025-12 · метрики по партии ST в Q1 2026 [P][588] · по состоянию на 2026-09-03 ничего не найдено). GF, Anderon: сроков по пластинам не обещано [C][284], [593]. Достоверность: первыми идут imec/Diraq (рецензируемые публикации, воспроизведено); Intel производит, но без продуктового маршрута; Quantum Motion, Quobly, Equal1 поставляют системы без метрик; слайды дорожных карт — последними.

**Стратегическое прочтение.** Успех вознаграждает фабрики и поставщиков (GF, imec, ST/Soitec, Bluefors) и спиновых вендоров, у которых спецификация материалов сжимается до пластин плюс стоек; проигрывают штучные маршруты (STM-литография, университетский lift-off) и MEMS-производства ловушек. Переговорная сила поставщиков высока (линий мало, квантовая выручка несущественна), но три-четыре взаимозаменяемые линии и государственные деньги ограничивают то, что фабрики могут извлечь. Угрозы замещения: дырки в Ge/SiGe, фабрики фотонных интерконнектов, SFQ против cryo-CMOS.

*Открытая ниша:* Небольшая исследовательская компания в области QCVV/SFQ встраивается ровно в тот разрыв, в который эта справка упирается снова и снова: протоколы, отображающие статистику по пластине при 1.6 K на кубитные характеристики при милликельвиновых температурах; бенчмарки для массивов с разделяемым управлением, где стандартный рандомизированный бенчмаркинг предполагает индивидуальную адресацию; количественная оценка дрейфа на масштабе месяцев. Точка входа — канал мультипроектных пластин SPINS; CMOS-совместимый сверхпроводниковый стек imec подходит для тестового кристалла управления SFQ-на-CMOS.

## Прогноз и открытые вопросы

Вехи, 12–24 месяца: (1) прибор 300 mm с > 20 кубитами и опубликованной 2Q по всем парам ≥ 99.5% подтверждает узел; отсутствие такового к концу 2027 г. понижает ранг; (2) запуски мультипроектных пластин SPINS с публичным квантовым PDK; (3) перевод письма о намерениях GF в окончательное соглашение, названный квантовый продукт на 22FDX; (4) партия спиновых кубитов на Anderon после закрытия сделки IBM–HRL; (5) Intel называет преемника Tunnel Falls либо уходит.

Лучший сценарий на 2029 г.: две коммерческие линии 300 mm с квантовыми PDK, массивы на 10³ точек с мультиплексированием на кристалле, типичная 2Q ≥ 99.5%, подпороговая спиновая память. Худший: коммерческий выход годных в десятки процентов, 2Q на уровне 99–99.6%, дорожные карты снова урезаны, подразделение GF сведено к корпусированию для сверхпроводниковых и фотонных заказчиков.

Открытые вопросы: можно ли сделать долинное расщепление и зарядовый шум однородными по пластине — или каждый массив придётся отбирать постселекцией? Каков выход годных по кубитной точности у маршрута 300 mm? Удерживает ли разделяемое управление когерентную ошибку ниже порога? Может ли попадание переходов в номинал внутри маршрута выйти на субпроцентный уровень? Следить за первым числом выхода годных по точности, за первой мультипроектной пластиной SPINS, за окончательными решениями по CHIPS, за Intel.

## Источники

[10] IBM, “IBM to Acquire HRL Laboratories to Power the Future of Quantum,” Jul. 23, 2026. [Online]. Available: https://newsroom.ibm.com/2026-07-23-ibm-to-acquire-hrl-laboratories-to-power-the-future-of-quantum [C]
[18] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[60] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[162] P. Steinacker *et al.*, “Industry-compatible silicon spin-qubit unit cells exceeding 99% fidelity,” *Nature*, vol. 646, no. 8083, pp. 81–87, Sep. 2025, doi: [10.1038/s41586-025-09531-9](https://doi.org/10.1038/s41586-025-09531-9). [D]
[163] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[165] H. Edlbauer *et al.*, “An 11-qubit atom processor in silicon,” *Nature*, vol. 648, no. 8094, pp. 569–575, Dec. 2025, doi: [10.1038/s41586-025-09827-w](https://doi.org/10.1038/s41586-025-09827-w). [arXiv:2506.03567](https://arxiv.org/abs/2506.03567). [D]
[169] M. De Smet *et al.*, “High-fidelity single-spin shuttling in silicon,” *Nat. Nanotechnol.*, vol. 20, no. 7, pp. 866–872, Jun. 2025, doi: [10.1038/s41565-025-01920-5](https://doi.org/10.1038/s41565-025-01920-5). [D]
[170] A. Nickl *et al.*, “Eight-qubit operation of a 300 mm SiMOS foundry-fabricated device,” *Nat. Commun.*, vol. 17, no. 1, Art. no. 5878, Jul. 2026, doi: [10.1038/s41467-026-74597-6](https://doi.org/10.1038/s41467-026-74597-6). [D]
[172] H. C. George *et al.*, “12-spin-qubit arrays fabricated on a 300 mm semiconductor manufacturing line,” *Nano Lett.*, vol. 25, no. 2, pp. 793–799, Dec. 2024, doi: [10.1021/acs.nanolett.4c05205](https://doi.org/10.1021/acs.nanolett.4c05205). [arXiv:2410.16583](https://arxiv.org/abs/2410.16583). [D]
[173] Quantum Motion, “Quantum Motion Delivers the Industry's First Full-Stack Silicon CMOS Quantum Computer,” Sep. 15, 2025. [Online]. Available: https://quantummotion.com/quantum-motion-delivers-the-industrys-first-full-stack-silicon-cmos-quantum-computer/ [C]
[175] L. Hesla, “Argonne launches silicon quantum processor collaboration with Intel,” Argonne National Laboratory, Jan. 6, 2026. [Online]. Available: https://www.anl.gov/article/argonne-launches-silicon-quantum-processor-collaboration-with-intel [G]
[178] F. Elliott, “Diraq charts course to utility-scale quantum computing with millions of spin qubits on a single silicon chip,” Diraq, Aug. 27, 2026. [Online]. Available: https://www.diraq.com/newsdesk/diraq-sets-roadmap-for-utility-scale-quantum-computing-with-millions-of-qubits-on-a-single-silicon-chip [R]
[217] J. Van Damme *et al.*, “Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers,” *Nature*, vol. 634, no. 8032, pp. 74–79, Oct. 2024, doi: [10.1038/s41586-024-07941-9](https://doi.org/10.1038/s41586-024-07941-9). [D]
[218] D. P. Pappas *et al.*, “Alternating-bias assisted annealing of amorphous oxide tunnel junctions,” *Communications Materials*, vol. 5, no. 1, Art. no. 150, Aug. 2024, doi: [10.1038/s43246-024-00596-z](https://doi.org/10.1038/s43246-024-00596-z). [D]
[220] D. Underwood *et al.*, “Using Cryogenic CMOS Control Electronics to Enable a Two-Qubit Cross-Resonance Gate,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010326, Feb. 2024, doi: [10.1103/PRXQuantum.5.010326](https://doi.org/10.1103/PRXQuantum.5.010326). [D]
[224] National Institute of Standards and Technology, “Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing,” NIST News, May 21, 2026. [Online]. Available: https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion [G]
[225] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[284] GlobalFoundries, “GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing,” May 21, 2026. [Online]. Available: https://gf.com/gf-press-release/globalfoundries-launches-quantum-technology-solutions-to-scale-us-quantum-manufacturing/ Also https://investors.gf.com/news-releases/news-release-details/globalfoundries-launches-quantum-technology-solutions-scale-us. [C]
[286] Quantum Motion, “Quantum Motion Raises $160 Million Series C to Deliver Quantum Computing's "Transistor Moment,” May 7, 2026. [Online]. Available: https://quantummotion.com/quantum-motion-raises-160-million-series-c-to-deliver-quantum-computings-transistor-moment/ [C]
[352] IonQ, “IonQ Achieves Landmark Result, Setting New World Record in Quantum Computing Performance,” Oct. 21, 2025. [Online]. Available: https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing [C]
[404] F. Borsoi *et al.*, “Shared control of a 16 semiconductor quantum dot crossbar array,” *Nat. Nanotechnol.*, vol. 19, no. 1, pp. 21–27, Jan. 2024, doi: [10.1038/s41565-023-01491-3](https://doi.org/10.1038/s41565-023-01491-3). [D]
[419] S. K. Bartee *et al.*, “Spin-qubit control with a milli-kelvin CMOS chip,” *Nature*, vol. 643, no. 8071, pp. 382–387, Jul. 2025, doi: [10.1038/s41586-025-09157-x](https://doi.org/10.1038/s41586-025-09157-x). [D]
[541] A. Knapen *et al.*, “Pinball: A Cryogenic Predecoder for Surface Code Decoding Under Circuit-Level Noise,” [arXiv:2512.09807](https://arxiv.org/abs/2512.09807), Dec. 2025. [S]
[584] R. Maurand *et al.*, “A CMOS silicon spin qubit,” *Nat. Commun.*, vol. 7, Art. no. 13575, Nov. 2016, doi: [10.1038/ncomms13575](https://doi.org/10.1038/ncomms13575). [D]
[585] A.-M. Zwerver *et al.*, “Qubits made by advanced semiconductor manufacturing,” *Nat. Electron.*, vol. 5, no. 3, pp. 184–190, Mar. 2022, doi: [10.1038/s41928-022-00727-9](https://doi.org/10.1038/s41928-022-00727-9). [D]
[586] S. F. Neyens *et al.*, “Probing single electrons across 300-mm spin qubit wafers,” *Nature*, vol. 629, no. 8010, pp. 80–85, May 2024, doi: [10.1038/s41586-024-07275-6](https://doi.org/10.1038/s41586-024-07275-6). [D]
[587] E. J. Thomas *et al.*, “Rapid cryogenic characterization of 1,024 integrated silicon quantum dot devices,” *Nat. Electron.*, vol. 8, no. 1, pp. 75–83, Jan. 2025, doi: [10.1038/s41928-024-01304-y](https://doi.org/10.1038/s41928-024-01304-y). [D]
[588] C. Knowles, “Quobly runs silicon-28 quantum wafers through ST fab,” IT Brief Asia, Dec. 12, 2025. [Online]. Available: https://itbrief.asia/story/quobly-runs-silicon-28-quantum-wafers-through-st-fab [P]
[589] M. P. Losert *et al.*, “Practical strategies for enhancing the valley splitting in Si/SiGe quantum wells,” *Phys. Rev. B*, vol. 108, no. 12, Art. no. 125405, Sep. 2023, doi: [10.1103/PhysRevB.108.125405](https://doi.org/10.1103/PhysRevB.108.125405). [S]
[590] Equal1, “Equal1 advances scalable quantum computing with CMOS-compatible silicon spin qubit technology,” Apr. 16, 2025. [Online]. Available: https://www.equal1.com/post/commercial_cmos_process [C]
[591] University College Dublin, “Equal1 Announces $60 million in Funding to Accelerate Quantum Computing using Existing Semiconductor Manufacturing,” UCD Innovation, Jan. 15, 2026. [Online]. Available: https://www.ucd.ie/innovation/news-and-events/2026/equal1-announces-funding-round/ [C]
[592] imec, “Quantum pilot line 'SPINS' launched with EU support,” Apr. 3, 2026. [Online]. Available: https://www.imec-int.com/en/press/semiconductor-based-quantum-pilot-line-spins-launched-eu-support [G]
[593] IBM, “IBM and U.S. Department of Commerce Announce America's First Purpose-Built Quantum Foundry, Supported by Proposed $1 Billion CHIPS Award,” May 21, 2026. [Online]. Available: https://newsroom.ibm.com/ibm-and-u-s-department-of-commerce-announce-americas-first-purpose-built-quantum-foundry [C]
[594] Silex Systems, “SILEX Quantum Silicon (Q-Si) Production for Quantum Computing,” silex.com.au. [Online]. Available: https://www.silex.com.au/silex-technology/silex-zs-si-production-for-quantum-computing/ [C]
[595] Bluefors Oy, “Cryogenic Wafer Prober — Under 2 K with 300 mm Wafers,” bluefors.com, Jun. 10, 2026. [Online]. Available: https://bluefors.com/products/cryogenic-wafer-prober/ [C]
[596] FormFactor, Inc., “HPD IQ3000 - 4 K Cryogenic Probe Station,” Jun. 9, 2026. [Online]. Available: https://www.formfactor.com/product/quantum-cryo/quantum-wafer-multi-chip-cryogenic/iq3000/ [C]
[597] R. Acharya *et al.*, “Multiplexed superconducting qubit control at millikelvin temperatures with a low-power cryo-CMOS multiplexer,” *Nat. Electron.*, vol. 6, no. 11, pp. 900–909, Nov. 2023, doi: [10.1038/s41928-023-01033-8](https://doi.org/10.1038/s41928-023-01033-8). [D]
[598] H. Bennie, “Quantum Motion Announces Record Integration of Quantum Devices and Partnership with Semiconductor Manufacturer, GlobalFoundries,” quantummotion.com, Jan. 6, 2025. [Online]. Available: https://quantummotion.com/partnership-with-globalfoundries/ [C]
[599] Quobly, “Quobly Raises €115M Series A to Industrialize Silicon Quantum Computing,” HPCwire, Jun. 3, 2026. [Online]. Available: https://www.hpcwire.com/off-the-wire/quobly-raises-e115m-series-a-to-industrialize-silicon-quantum-computing/ [P]

## Открытые пункты верификации

- SPAM для элементарных ячеек imec/Diraq: 99.95% при 100 µs [162] (значение v1, сохранено) против 99.9%, зафиксированных для 300-мм линии imec (2025).
- Точность шаттлинга [169]: в v1 указано 99.54%; в аннотации сказано «99.5% в среднем»; используется значение из аннотации.
- Финансирование Silex (A$5.1 M от Defence Trailblazer, A$4.35 M от SQC): на странице Silex суммы не датированы [594]; строка учёта датирована по завершению строительства завода в июне 2026 г.
- [589] Losert et al.: библиографические данные приводятся по стандартной литературе и не подтверждены по странице издателя.
- Исключено из v1 как не подтверждённое здесь: «доля Минторга ~1% в капитале» в письме о намерениях GF по CHIPS (в v1 совместно цитировались [224], [284], [593]), заявление IBM о 30-кратном росте выпуска приборов на Anderon (только по отраслевой прессе) и показатель Intel 91% по считыванию одиночного электрона [586] против 96% настройки [172] (разные наборы приборов и разные критерии).
