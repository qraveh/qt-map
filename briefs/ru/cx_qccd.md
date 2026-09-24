---
id: cx_qccd
name: Транспортировка ионов (QCCD, переходы, сеточные ловушки)
layer: "4 Связность / транспорт"
status: demonstrated
since: 2002
one_line: Перемещение захваченных ионов между зонами через переходы или сеточные ловушки, благодаря чему небольшой пригодный для гейтов кристалл получает связность «все со всеми».
verdict: Такт ионной машины задают сортировка, разделение кристаллов и повторное охлаждение — не перелёт и не гейт (~55 мс на слой полной ширины в Helios). Без 10-кратного сокращения к 2028 г. ионный QCCD останется высокоточным и низкопроизводительным.
updated: 2026-09-04
---

Λ = коэффициент подавления ошибок на шаг кодового расстояния; QBI = DARPA Quantum Benchmarking Initiative (этап A — концепция → B — план НИОКР → C — государственная V&V); G1–G7 = классы целей отчёта (см. «Акторы и экономика»).

## Идентичность и происхождение
QCCD, предложенная Kielpinski, Monroe и Wineland в 2002 г. [D][1], разбивает регистр на зоны и с помощью меняющихся во времени напряжений на электродах перемещает ионы между зонами памяти и зонами взаимодействия, так что ни одной цепочке не нужно быть одновременно длинной и пригодной для гейтов — маршрутизация покупается площадью ловушки. Переходы делают её двумерной; сеточные ловушки переставляют ионы, как костяшки в игре в пятнашки.

Подвижность и время: движется сам носитель, измеренная скорость 1.7–4 м/с [D][2], [3], поэтому связность — это расписание, а не карта элементов связи (каплеров); перемещение вместе с повторным охлаждением ~2 мс, детерминизм запутывания неприменим. Ошибки и изготовление: когерентное возбуждение движения плюс потеря ионов, проявляющиеся как повышенная двухкубитная неточность (infidelity) и утечка (leakage); MEMS-чипы с поверхностными электродами, управляемые формами DC-напряжений.

## Физика и пределы
Плавное изменение напряжений на соседних сегментах тянет потенциальную яму, а вместе с ней и ион, вдоль оси — причём перемещение вовсе не обязано быть медленным: в NIST ⁹Be⁺ переместили на 370 мкм за 8 мкс, при этом возбуждение достигало пика в 1.6 кванта и возвращалось к 0.2 за счёт подбора формы сигнала [D][4]. Миллисекундная цена приходится, таким образом, не на перелёт, а на разделение и повторное объединение кристаллов (два иона, разделённые за 55 мкс, сохранили примерно по 2 кванта каждый [D][4]) и на сайдбэнд-охлаждение, восстанавливающее моды, на которых работает гейт.

В области перехода ВЧ-нуль терпит разрыв: ион пересекает горб псевдопотенциала с избыточным микродвижением, и именно это задаёт скорость прохождения и нагрев. Под этим лежит аномальный нагрев от шума поверхности электродов, круто растущий по мере приближения иона к поверхности, так что более жёстким удержанием адиабатичности не купить. Пол сдвигает гейт, терпимый к тёплому кристаллу: электронный гейт достиг ошибки 8.4×10⁻⁵ без охлаждения до основного состояния [D][5], то есть не уменьшил слагаемое повторного охлаждения, а убрал его вовсе.

## Инженерное состояние (state of the art)
| Год | Показатель | Кто | Тег |
|---|---|---|---|
| 2022-06 | Круговой проход через X-переход, средняя скорость 4 м/с, 0.013(1)–0.030(2) кванта | Quantinuum | [D][2] |
| 2023-02 | Межчиповая материальная связь, 2,424 переноса/с, неточность из-за потерь < 7×10⁻⁸ | Universal Quantum | [D][3] |
| 2024-03 | Обмен ионами в сеточной ловушке с частотой 2.5 кГц | Quantinuum | [D][6] |
| 2025-11 | 55 мс на слой полной ширины, 98 ионов, 8 зон | Quantinuum | [D][7] |

Главная находка — разрыв между примитивом и продуктом: двухкубитный гейт в Helios занимает ~70 мкс против ~55 мс на слой, а в H2 транспорт составлял ~60% времени исполнения [D][7], [8]. Доминирующее слагаемое — расписание: сортировка, разделение/слияние, повторное охлаждение, сериализация по восьми зонам.

## Производство, материалы и цепочка поставок
Ловушки — это чипы с сегментированными электродами. Honeywell выступает кэптивной фабрикой Quantinuum и изготовила чип двумерной сетки для Sol, который по состоянию на второй квартал 2026 г. проходит валидацию [C][9]. Infineon Villach — коммерческая (merchant) линия: пластины 6–12 дюймов, электроды третьего поколения с выходом из плоскости, для которых заявлено усиление удержания примерно в 10×; она обслуживает одновременно Oxford Ionics, eleQtron, Innsbruck и ETH [C][10]. IonQ сломала эту дуополию, купив SkyWater примерно за $1.8 B; сделка закрыта 2026-07-31 — первый ионный вендор, владеющий собственным производством [G][11]. MESA в Sandia остаётся сугубо исследовательской [G][12]. Данных о выходе годных нет в открытом доступе; единственная известная цена — 20-кубитная система AQT «под ключ» за EUR 9.8 M, т. е. ≈ EUR 0.5 M на кубит [C][13]. Единые точки отказа: единственная линия Infineon и УФ-лазеры, где доминирует TOPTICA, а длина волны 369 нм для Yb⁺ дефицитна [P][14]. Ни один ECCN не называет ионные ловушки прямо, но готовая машина подпадает под 4A906, действующий с 2024-09-06 [G][15].

## Управление, считывание и нагрузка на ввод-вывод
Перемещение — это синхронизированная форма DC-напряжений на десятках электродов с обновлением на масштабе микросекунд, затем охлаждение и, для лазерных гейтов, переадресация пучков. В Helios на 98 ионов приходится 1,228 электродов [D][7]: масштабируется именно число электродов, а обновления укладываются в 55-мс слой с запасом в три порядка, так что электроника — не стена. При 10³ ионах это ~10⁴ фильтрованных DC-каналов; Oxford Ionics предлагает сократить их до ~200 внешних источников, разместив коммутирующую электронику на чипе, — это проектное исследование, чип не изготовлен [S][16]. При 10⁴–10⁶ ограничением становится разводка охлаждающего и гейтового света сразу во множество зон (Helios требует ≥7 длин волн): ни одна система не обслуживает одновременно больше нескольких десятков.

## Роль в стеке
Транспортировка обслуживает оба ионных пути платформы — QCCD с лазерными гейтами (Quantinuum, AQT) и электронные гейты с управлением на чипе (IonQ/Oxford Ionics, eleQtron), — обеспечивая связность произвольных пар, которую предполагают qLDPC-памяти на двумерных велосипедных кодах (bivariate bicycle) и трансверсальные коды высокой скорости: и демонстрация [[80,48,4]] у Quantinuum, и выход qLDPC на точку безубыточности у IonQ оплачены транспортом. Она заменяет статическую длинную цепочку, спектр мод которой уплотняется по мере добавления ионов; плата за это — связность превращается в планирование, а такт переходит от гейта к перемещению: производный такт = сумма раунда синдрома: слои гейтов + транспорт + считывание + сброс ≈ 9.7 мс, из них 9.0 мс — транспорт, против измеренного слоя полной ширины ~55 мс [D][7]. Соседний пустой слот: более двух связанных модулей — связь двух модулей существует [D][3], большего нет.

## Верификация (QCVV)
Самостоятельного бенчмарка для транспорта нет. О нём судят косвенно — по сайдбэнд-термометрии до и после перемещения (те самые 0.013(1)–0.030(2) кванта [D][2]) и по двухкубитной точности (fidelity) после транспортной последовательности, что сворачивает транспорт в ошибку гейта. Ни то, ни другое не схватывает накопленный нагрев на глубокой схеме, потери в переходах при масштабировании и перекрёстные помехи между зонами. Значения 55 мс на слой и 2.5 кГц обмена сообщены самим вендором и по состоянию на 2026-09-04 независимо не воспроизведены; квантовый объём 32,768 у AQT — не измерение транспорта и не раскрывает никаких временных характеристик [C][17].

## Акторы и экономика
**Кто.**
| Организация | Роль | Страна | Что именно делает с технологией | Свидетельство |
|---|---|---|---|---|
| Quantinuum | разработчик | США/Великобритания | QCCD с кольцом и переходом, сеточная ловушка для Sol | [D][7] |
| Honeywell | поставщик | США | Кэптивная фабрика, изготовила чип для Sol | [C][9] |
| IonQ | разработчик | США | Ловушки с переходами, владеет SkyWater | [G][11] |
| Infineon | поставщик | Австрия | Коммерческая фабрика (foundry) ловушек, Gen-3 | [C][10] |
| Universal Quantum | разработчик | Великобритания | Единственная межчиповая материальная связь | [D][3] |
| AQT | разработчик | Австрия | Модуль LYNX, поставки в 4-м квартале 2026 г. | [C][17] |
| Quantum Art | разработчик | Израиль | Оптическая реконфигурация ионных массивов | [P][18] |

**Деньги.** 2022-11-02 · Universal Quantum · контракт DLR · EUR 67 M · не исполнен [P][19]. 2025-09-04 · Quantinuum · раунд · $600 M при оценке $10 B pre-money · NVentures, Quanta, QED, JPMorgan · закрыт [G][20]. 2025-11-06 · Quantinuum и IonQ · QBI, этап B · ≤$15 M каждому · действует [G:QBI-STAGEB-2025-11]. 2026-05-05 · eleQtron · раунд Series A · EUR 57 M [G][21]. 2026-06-03 · Quantinuum · IPO · $1.68 B валовых поступлений, Nasdaq QNT, денежные средства $2.1 B [G][9]. 2026-07-31 · IonQ · сделка M&A по SkyWater · ~$1.8 B, после Oxford Ionics за $1.075 B [G][11], [22].

**Рынок и цепочка поставок.** Изготовление ловушек держалось на одной кэптивной и одной коммерческой линии; SkyWater добавляет третью, вертикально интегрированную, — самое значимое событие года в цепочке поставок [C][10][G][11]. УФ-лазеры остаются более жёстким узким местом [P][14]. Транспортировку оплачивает G2, и она является предпосылкой для G3 и G4.

**ИС и стандарты.** Число патентных семейств именно по транспортировке не публиковалось. Ближайшие датированные данные: IonQ подала 9+ семейств по ионным ловушкам в юрисдикциях JP/EP/IL в 2025–26 гг.; у Quantum Art есть две находящиеся на рассмотрении заявки IL/KR на оптическую реконфигурацию ионных массивов [P][23]. Открытого стека для транспортировки не существует.

**Дорожные карты и послужной список.** Quantinuum: Helios (обещан 2024-09-10, выпущен 2025-11-05 — выполнено); Sol (2027, чип на валидации во втором квартале 2026 г. — идёт по графику); Apollo (2029 — без оценки) [R][24][C][9]; заслуживает доверия. IonQ: 10,000 физических кубитов на одном чипе к 2027 г., 2 M к 2030 г., при этом не опубликовано ни данных по нагреву в двумерных ловушках, ни данных по транспорту, а дорожная карта 2020 года промахнулась мимо 4,000 кубитов примерно в 40 раз — это намерение, а не план [R][25]. Universal Quantum с 2022 г. не поставила ничего [P][26].

**Стратегическое прочтение.** Сократите время слоя в 10 раз — и ионы конвертируют преимущество по точности в отказоустойчивость, конкурентоспособную по пропускной способности; не сократите — и они будут выигрывать заголовки про логические кубиты, проигрывая по числу измерений (shots) в секунду. В любом случае выигрывают Infineon и Honeywell, продающие дефицитный объект. Угроза замещения: оптические пинцеты нейтральных атомов и сверхпроводниковые каплеры дальнего действия — связность без транспорта.

*Открытая ниша:* Общепринятого QCVV-протокола для отдельного перехода или отдельного перемещения нет. Небольшая команда могла бы выпустить такой протокол с открытым исходным кодом — кванты на одно прохождение перехода, потери на 10⁶ прохождений, перекрёстные помехи между зонами, рандомизированный бенчмаркинг с чередованием транспорта и гейта, — то, чего не публикует ни один вендор и что сделало бы цифру 55 мс проверяемой.

## Прогноз и открытые вопросы
Подтвердить/понизить в течение 12–24 месяцев: Sol выходит в 2027 г. с опубликованным временем на слой; любой вендор публикует слой полной ширины быстрее 10 мс; Universal Quantum связывает более двух модулей. Лучший случай к 2029 г.: слои быстрее 10 мс приближают логический такт ионов к сверхпроводниковому с разрывом ~10×. Худший случай: время слоя остаётся в пределах двукратного от 55 мс, и ионы остаются платформой, которая демонстрирует коды, а не исполняет алгоритмы. Открытые вопросы: вынуждает ли аномальный нагрев переходить к криогенным ловушкам при 10⁴ ионов; можно ли сделать разделение/слияние свободным от возбуждения квантов средствами оптимального управления; действительно ли гейты на тёплом кристалле устраняют повторное охлаждение; появится ли вторая коммерческая фабрика. Следить за: валидацией Sol, мощностями Infineon, первой ловушкой IonQ производства SkyWater.

## Источники
[1] D. Kielpinski, C. Monroe, and D. J. Wineland, “Architecture for a large-scale ion-trap quantum computer,” *Nature*, vol. 417, no. 6890, pp. 709–711, Jun. 2002, doi: [10.1038/nature00784](https://doi.org/10.1038/nature00784).
[2] W. C. Burton, B. Estey, I. M. Hoffman, A. R. Perry, C. Volin, and G. Price, “Transport of multispecies ion crystals through a junction in an RF Paul trap,” *Phys. Rev. Lett.*, vol. 130, Art. no. 173202, Apr. 2023, doi: [10.1103/PhysRevLett.130.173202](https://doi.org/10.1103/PhysRevLett.130.173202). [arXiv:2206.11888](https://arxiv.org/abs/2206.11888).
[3] M. Akhtar *et al.*, “A high-fidelity quantum matter-link between ion-trap microchip modules,” *Nat. Commun.*, vol. 14, no. 1, Art. no. 531, Feb. 2023, doi: [10.1038/s41467-022-35285-3](https://doi.org/10.1038/s41467-022-35285-3).
[4] R. Bowler *et al.*, “Coherent Diabatic Ion Transport and Separation in a Multi-Zone Trap Array,” *Phys. Rev. Lett.*, vol. 109, no. 8, Art. no. 080502, 2012, doi: [10.1103/PhysRevLett.109.080502](https://doi.org/10.1103/PhysRevLett.109.080502). [arXiv:1206.0780](https://arxiv.org/abs/1206.0780).
[5] A. C. Hughes *et al.*, “Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling,” [arXiv:2510.17286](https://arxiv.org/abs/2510.17286), Oct. 2025.
[6] R. D. Delaney *et al.*, “Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap,” *Phys. Rev. X*, vol. 14, Art. no. 041028, Nov. 2024, doi: [10.1103/PhysRevX.14.041028](https://doi.org/10.1103/PhysRevX.14.041028). [arXiv:2403.00756](https://arxiv.org/abs/2403.00756).
[7] A. Ransford *et al.*, “A 98-qubit trapped-ion quantum computer with all-to-all connectivity,” *Nature*, vol. 655, no. 8121, pp. 81–86, Jun. 2026, doi: [10.1038/s41586-026-10676-4](https://doi.org/10.1038/s41586-026-10676-4). [arXiv:2511.05465](https://arxiv.org/abs/2511.05465).
[8] S. A. Moses *et al.*, “A Race Track Trapped-Ion Quantum Processor,” *Phys. Rev. X*, vol. 13, Art. no. 041052, Dec. 2023, doi: [10.1103/PhysRevX.13.041052](https://doi.org/10.1103/PhysRevX.13.041052). [arXiv:2305.03828](https://arxiv.org/abs/2305.03828).
[9] Quantinuum, “Quantinuum Reports Second Quarter 2026 Results,” Aug. 11, 2026. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-reports-second-quarter-2026-results [C]
[10] “Infineon Technologies, trapped-ion QPU platform (Villach), company page accessed 2026-09-03,” infineon.com, Sep. 4, 2026. [Online]. Available: https://www.infineon.com/promo/trapped-ions [C]
[11] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[12] T. Rummler, “In the Mountain West, a quantum computing collaboration announces major results,” Sandia Lab News, Aug. 27, 2026. [Online]. Available: https://www.sandia.gov/labnews/2026/08/27/in-the-mountain-west-a-quantum-computing-collaboration-announces-major-results/
[13] AQT, “AQT lands million euro contract,” Dec. 5, 2023. [Online]. Available: https://www.aqt.eu/aqt-lands-million-euro-contract/ [C]
[14] M. Ivezic, “The Optical Table's Hidden Supply Chain: Who Really Wins If Trapped-Ion Quantum Computing Wins,” PostQuantum.com, Apr. 10, 2026. [Online]. Available: https://postquantum.com/quantum-ecosystem/trapped-ion-quantum-ecosystem/ [P]
[15] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies
[16] M. Malinowski, D. Allcock, and C. Ballance, “How to Wire a 1000-Qubit Trapped-Ion Quantum Computer,” *PRX Quantum*, vol. 4, no. 4, Art. no. 040313, Oct. 2023, doi: [10.1103/PRXQuantum.4.040313](https://doi.org/10.1103/PRXQuantum.4.040313). [arXiv:2305.12773](https://arxiv.org/abs/2305.12773).
[17] Alpine Quantum Technologies GmbH, “AQT Sets New European Industry Standard: Introducing the ‘LYNX’ Series with Record-Breaking Quantum Volume,” AQT, May 5, 2026. [Online]. Available: https://www.aqt.eu/lynx-quantum-volume-record/ [C]
[18] M. Abdel-Kareem, “Quantum Art Extends Series A to $140M to Scale Trapped-Ion Architecture,” Quantum Computing Report, Apr. 27, 2026. [Online]. Available: https://quantumcomputingreport.com/quantum-art-extends-series-a-to-140m-to-scale-trapped-ion-architecture/ [P]
[19] A. Ingall, “German government tasks Sussex spin-out with building a powerful quantum computer in €67M contract,” University of Sussex Broadcast, Nov. 2, 2022. [Online]. Available: https://www.sussex.ac.uk/broadcast/read/59206 [P]
[20] Honeywell, “Honeywell Announces $600 Million Capital Raise for Quantinuum at $10B Pre-Money Equity Valuation to Advance Quantum Computing at Scale,” Sep. 4, 2025. [Online]. Available: https://www.honeywell.com/us/en/news/press-releases/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale
[21] A. Cordes, “Quantum computing scale-up eleQtron secures €57 million in one of the largest Series A funding rounds worldwide,” eleQtron, May 5, 2026. [Online]. Available: https://eleqtron.com/en/quantum-computing-scale-up-eleqtron-secures-57-million-in-one-of-the-largest-series-a-funding-rounds-worldwide/
[22] IonQ, “IonQ Completes Acquisition of Oxford Ionics, Rapidly Accelerating Its Quantum Computing Roadmap,” Sep. 17, 2025. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-oxford-ionics-rapidly-accelerating-its-quantum [C]
[23] PatSnap, “Trapped Ion Quantum Computing: Technology Landscape 2026,” Apr. 23, 2026. [Online]. Available: https://www.patsnap.com/resources/blog/rd-blog/trapped-ion-quantum-computing-2026-patsnap-eureka/ [P]
[24] Quantinuum, “Quantinuum Unveils Accelerated Roadmap to Achieve Universal, Fully Fault-Tolerant Quantum Computing by 2030,” Sep. 10, 2024. [Online]. Available: https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030
[25] IonQ, “IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality,” Jun. 13, 2025. [Online]. Available: https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality [C]
[26] M. Abdel-Kareem, “Universal Quantum and Atlas Copco Partner to Industrialize Vacuum Systems for Scalable Quantum Computers,” Quantum Computing Report, Dec. 18, 2025. [Online]. Available: https://quantumcomputingreport.com/universal-quantum-and-atlas-copco-partner-to-industrialize-vacuum-systems-for-scalable-quantum-computers/ [P]

## Открытые пункты верификации
- Список авторов и точное название статьи о сеточной ловушке [6] не удалось получить со страницы аннотации arXiv; атрибуция к Quantinuum взята из фактчекинга основного отчёта, а число узлов сетки в аннотации не приводится.
- Независимого (невендорского) воспроизведения ни времени 55 мс на слой полной ширины, ни частоты обмена 2.5 кГц в сеточной ловушке не существует.
- Архитектура LYNX у AQT (с переходами или только линейная), а также её времена транспорта и гейтов не раскрыты.
- Ни по одной линии производства ионных ловушек не опубликованы выход годных, однородность или стоимость кристалла; цифра EUR 0.5 M на кубит — это цена системы «под ключ» 2023 года, а не стоимость чипа.
- Охватывают ли пороги ECCN 4A906 по числу кубитов и уровню ошибок нынешние коммерческие ионные системы — с числовыми значениями в тексте правила не сверялось.
