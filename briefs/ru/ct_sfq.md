---
id: ct_sfq
name: Цифровое управление на SFQ (милликельвины)
layer: "5 Управление"
status: emerging
since: 2026
one_line: "Квантованные импульсы магнитного потока с ниобиевого цифрового кристалла, смонтированного flip-chip на кубитную пластину, выполняют гейты при милликельвинах, заменяя микроволновый коаксиал на каждый кубит."
verdict: "Реально: один пятикубитный модуль с однокубитной точностью > 99%. Не доказано: двухкубитные гейты, считывание, потоковое смещение, устойчивость к квазичастицам за пределами пяти кубитов. Понизить, если к 2028 г. не появится SFQ-модуль более чем на 20 кубитов."
updated: 2026-09-03
---

Λ = коэффициент подавления ошибки на шаг расстояния кода; QBI = DARPA Quantum Benchmarking Initiative (Stage A — концепция → B — план НИОКР → C — государственная V&V); G1–G7 = классы целей, принятые в отчёте (см. «Акторы и экономика»).

## Идентичность и происхождение

Логика на одиночных квантах магнитного потока (SFQ) хранит бит как один квант потока Φ₀ = h/2e в сверхпроводящем контуре; переключающийся переход излучает импульс площадью Φ₀ — около 1 mV в течение 2 ps. Её быстрый вариант (RSFQ; Likharev & Semenov, 1991) создавался для классических вычислений при 4 K. Для управления кубитом последовательность импульсов, привязанная к периоду кубита, когерентно складывается в раби-поворот [S][565]. В реализации 2026 года контроллер соединён с кубитами по технологии flip-chip при 10 mK [D][304]. Более широкая область сверхпроводниковой электроники отслеживается в Superconductor Electronics Monitor [P][56].

Атрибуты. **Сродство к носителю:** полностью изготавливаемый управляющий слой. **Время / запутывание:** неприменимо. **Считывание:** не продемонстрировано [C][53]. **Подвижность:** отсутствует, посадка на бампы. **Модальность управления @ размещение:** микроволновый привод, синтезируемый цифровым способом *при милликельвинах*. **Структура ошибки, как её видит код:** паулиевская плюс коррелированные всплески отравления [D][249]. **Производство:** многослойная ниобиевая литография.

## Физика и пределы

Каждый импульс Φ₀ даёт кубиту фиксированный фазовый толчок, поэтому угол гейта задаётся *числом* импульсов, а не аналоговой амплитудой. Переключение стоит всего ~I_cΦ₀ ≈ 10⁻¹⁹ J на событие; в бюджете камеры смешения — десятки µW при 20 mK — первыми ограничивают статическая мощность смещения RSFQ и распределение смещения.

Нижний предел — разрушение куперовских пар: переключающиеся переходы излучают фотоны выше щели алюминия (2Δ ≈ 90 GHz), которые разрывают куперовские пары в плёнке кубита — это отравление квазичастицами, — вызывая спад T₁ и коррелированные всплески. По прогнозу, ограничение полосы импульсов драйвера устраняет этот механизм и приближает ошибку гейта к 0.1% для резонансных последовательностей [D][249]. Другие рычаги: ловушки квазичастиц, инженерия щели, поглотители миллиметрового диапазона.

## Инженерное состояние (state of the art)

Лучшее продемонстрированное (3 сентября 2026 г.): пятикубитный модуль SEEQC при 10 mK, однокубитная точность выше 99%, один цифровой вход, демультиплексируемый на несколько кубитов [D][304][C][53]. Ни один SFQ-результат не выходит за пределы пяти кубитов и не включает ни двухкубитного гейта, ни цикла QEC.

| Год | Показатель | Кто | Тег+ключ |
|---|---|---|---|
| 2014 | 4,544 потоковых ЦАП на кристалле для 512 кубитов через 56 проводов | D-Wave | [D][430] |
| 2019 | Первый SFQ-гейт на трансмоне, ≈ 95% | Wisconsin / Syracuse | [D][566] |
| 2023 | Драйвер на отдельном кристалле: 1.2(1)% ошибки на клиффорд, из них 0.96(2)% от отравления | Wisconsin, Syracuse, NIST | [D][249] |
| 2026-03 | Пять кубитов, SFQ-управление при 10 mK; 1Q > 99%, пик 99.9% | SEEQC | [D][304] |
| 2026-03 | Считывание по времени задержки флюксона, точность не сообщается | препринт | [S][568] |

Доминирующий член ошибки: отравление квазичастицами в модуле 2023 года [D][249]; для модуля SEEQC не раскрыт.

## Производство, материалы и цепочка поставок

Управляющий кристалл — многослойная структура Nb/AlOx/Nb: восемь и более планаризованных ниобиевых слоёв, 10⁴–10⁶ переходов, — в отличие от алюминиевого кубитного процесса [D][569]. Фабрик мало: MIT Lincoln Laboratory (линия SFQ5ee, кубитная фабрика SQUILL) [C][570], ниобиевый процесс AIST с библиотеками ячеек [D][571] и коммерческая фабрика SEEQC в Elmsford, штат New York [C][572]. Выход годных требует разброса критического тока в единицы процентов на тысячах переходов. Экспортная уязвимость (правило BIS от 2024-09-06): ECCN 3A904, 3B904 и 4A906; позиция 3A901.a при буквальном прочтении охватывает только криогенные CMOS-схемы [G][301]. Единые точки отказа: рефрижераторы растворения, посадка на индиевые бампы, установки напыления ниобия и CMP.

## Управление, считывание и нагрузка на ввод-вывод

Комнатнотемпературному управлению нужен примерно один коаксиал привода и одна потоковая линия на трансмон, так что предел ему задают сечение криостата и тепловая нагрузка; платформа класса KIDE предлагает > 4,000 ВЧ-линий для «более 1000 кубитов» [C][G:BLUEFORS-KIDE]. SFQ-управлению нужен тактовый сигнал плюс низкоскоростной поток инструкций [D][304]. Считывание на SFQ существует лишь как схема в препринте [S][568]; потоковое смещение SEEQC относит к будущим работам [C][53].

## Роль в стеке

Архитектура: решётка сверхпроводящих трансмонов. Узлу требуются литография сверхпроводящих кубитов и flip-chip модули; он даёт холодную цифровую логику для криогенного декодера и потоковых ЦАП D-Wave [D][430]. Холодные маршруты управления — cryo-CMOS или SFQ: cryo-CMOS переиспользует коммерческие фабрики и средства проектирования; SFQ нужна ниобиевая экосистема, чьи коммерческие инструменты заканчиваются на физической верификации. Конфликт с трансмоном — фотоны переключения, отравляющие кубит, — открыт: его подавление пока лишь прогнозируется [D][249], а сообщение SEEQC 2026 года об отсутствии детектируемого отравления известно только из прессы [C][53]. Вклад в производный такт: нейтральный — раунд синдрома остаётся **0.65 µs** против измеренного цикла QEC **1.1 µs** [D][1]. Соседние пустые слоты: потоковое смещение на SFQ, считывание на SFQ.

## Свидетельства — как измерены числа

Каждая заглавная цифра — это среднее по клиффордам из рандомизированного бенчмаркинга (RB) [D][566][D][249][D][304]. RB предполагает марковские, не зависящие от гейта ошибки, поэтому редкие коррелированные всплески усредняются в слегка ухудшенное среднее, и модуль может пройти проверку на 99.9%, порождая при этом коррелированные ошибки, которых декодеры не моделируют. Заявление SEEQC об «отсутствии детектируемого отравления квазичастицами» приводится только в прессе [C][53]. Не сообщались: зарядовая чётность при непрерывном тактировании, T₁ при включённом и выключенном такте. Независимого воспроизведения нет: все авторы работы 2026 года — из SEEQC [D][304]. Противоречия: «выше 99%» в аннотации [D][304] против «выше 99.5%» в прессе [C][53]; «нановатты на кубит» [C][53] против ~1.6 µW на кубит в оценке 2026 года [S][550][G:CRYOCMOS-POWER-CONFLICT].

## Акторы и экономика

**Кто.**

| Организация | Роль | Страна | Что именно делает с технологией | Свидетельство |
|---|---|---|---|---|
| SEEQC | разработчик / фабрика | США | Модуль SFQ-управления при mK; коммерческая Nb-фабрика | [D][304][C][572] |
| IBM | интегратор | США | Интеграция SFQ с SEEQC (QBI); собственное cryo-CMOS-управление | [P][54][C][527] |
| Wisconsin–Madison, Syracuse, NIST Boulder | исследования | США | Резонансное SFQ-управление; исследование отравления | [S][565][D][249] |
| MIT Lincoln Laboratory | фабрика | США | Процесс SFQ5ee; кубитная фабрика SQUILL | [C][570] |
| D-Wave | разработчик (смежный) | Канада | Потоковые SFQ-ЦАП на кристалле в отжигателях | [D][430] |
| AIST, NEC | исследования / фабрика | Япония | Библиотеки ячеек на Nb; мультиплексированный контроллер при 4.2 K | [D][571][C][567] |

**Деньги.**
- 2020-09-16 · SEEQC · раунд серии A · $22.4 M · EQT Ventures (лид) · закрыт [C][572]
- 2025-01-16 · SEEQC · раунд роста · $30 M · SIP Global и другие · закрыт [P][573]
- 2025-06-12 · SEEQC + IBM · интеграция SFQ в рамках DARPA QBI, исполнитель — IBM [G][65] · сумма не раскрыта · объявлено [P][54][G:SEEQC-2026]
- 2026-06-29 · SEEQC · форма S-1 для IPO на Nasdaq, параллельно соглашению о SPAC-слиянии с Allegro Merger Corp (оценка предприятия $1 B) · подана [P][556][G:SEEQC-S1-2026-07]
- 2026-08-25 · SEEQC / Allegro · SPAC-слияние прекращено по соглашению об урегулировании: Allegro получает $6 M акциями по pre-money оценке $1.3 B при будущем IPO, продаже или привлечении ≥ $100 M · расторгнуто [G][574]

**Рынок и цепочка поставок.** Рынка SFQ-управления пока нет: один вендор, одна демонстрация. SkyWater — контрактная фабрика, упомянутая в отчётах D-Wave по форме 10-K [G][492], — с июля 2026 г. принадлежит IonQ [C][19]. Платят за это G3 и G4; G7 — во вторую очередь.

**ИС и стандарты.** SEEQC владеет патентами Hypres на схемотехнику RSFQ и ниобиевый процесс, переданными при её выделении в 2019 г. [C][572]. Стандартов на SFQ-управление нет; общие проектные базы — библиотека ячеек AIST [D][571] и наборы проектных данных MIT-LL [C][570].

**Дорожные карты и послужной список.** SEEQC: милликельвиновое SFQ-управление (обещано на 2021–22 · поставлено 2026-03 на пяти кубитах) [D][304]; потоковое управление и считывание на кристалле (объявлено 2026-03 · без даты) [C][53].

**Стратегическое прочтение.** Ниобиевые технологические мощности сосредоточены у SEEQC и, через Lincoln Laboratory, у правительства США. Из холодных маршрутов, cryo-CMOS или SFQ, более весомые результаты у cryo-CMOS: демонстрация QEC под управлением cryo-CMOS-контроллера при 4 K [D][190] и паритет с тёплой электроникой на процессоре IBM [C][527]; у SFQ — однокубитные гейты на пяти кубитах от одной группы [D][304].

## Прогноз и открытые вопросы

Подтверждают, если до конца 2027 г. какая-либо группа опубликует двухкубитный гейт с приводом от SFQ и ошибкой ниже 1%, управляемое SFQ устройство более чем на десять кубитов или многочасовые данные по зарядовой чётности без коррелированных с тактом всплесков. Понижают, если к концу 2028 г. ни один SFQ-модуль не превысит двадцати кубитов либо разложение ошибки покажет отравление выше 0.1% на клиффорд. Открытые вопросы: переживёт ли «отсутствие детектируемого отравления» непрерывное тактирование при скважностях, характерных для QEC? Способно ли потоковое смещение на SFQ обеспечить стабильность по постоянному току, необходимую трансмонам?

## Литература
[1] Google Quantum AI and Collaborators, “Quantum error correction below the surface code threshold,” *Nature*, vol. 638, no. 8052, pp. 920–926, Dec. 2024, doi: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y). [D]
[19] IonQ, “IonQ Completes Acquisition of SkyWater Technology,” Jul. 31, 2026. [Online]. Available: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology [C]
[53] M. Abdel-Kareem, “SEEQC Reports Integrated Qubit Control Logic Operating at Millikelvin Temperatures,” Quantum Computing Report, Mar. 21, 2026. [Online]. Available: https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/ [C]
[54] M. Abdel-Kareem, “SEEQC and IBM Collaborate on SFQ Control Integration Under DARPA's Quantum Benchmarking Initiative,” Quantum Computing Report, Jun. 12, 2025. [Online]. Available: https://quantumcomputingreport.com/seeqc-and-ibm-collaborate-on-sfq-control-integration-under-darpas-quantum-benchmarking-initiative/ [P]
[56] R. Neeman, “Superconductor Electronics Monitor,” Qodeh, 2026, doi: [10.5281/zenodo.21860767](https://doi.org/10.5281/zenodo.21860767). [Online]. Available: https://qodeh.com/publications/superconductor-electronics-monitor-2026/ [P]
[65] DARPA, “Stage B selection,” Nov. 6, 2025. [Online]. Available: https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection [G]
[190] Members of the HRL Quantum Team and Collaborators, “A digitally controlled silicon quantum processing unit,” [arXiv:2604.16216](https://arxiv.org/abs/2604.16216), Apr. 2026. [D]
[249] C. Liu *et al.*, “Single Flux Quantum-Based Digital Control of Superconducting Qubits in a Multichip Module,” *PRX Quantum*, vol. 4, no. 3, Art. no. 030310, Jul. 2023, doi: [10.1103/PRXQuantum.4.030310](https://doi.org/10.1103/PRXQuantum.4.030310). [D]
[301] US Department of Commerce, Bureau of Industry and Security, “Commerce Control List Additions and Revisions; Implementation of Controls on Advanced Technologies Consistent With Controls Implemented by International Partners,” *Federal Register*, vol. 89, p. 72926, Sep. 6, 2024. [Online]. Available: https://www.federalregister.gov/documents/2024/09/06/2024-19633/commerce-control-list-additions-and-revisions-implementation-of-controls-on-advanced-technologies [G]
[304] C. Jordan *et al.*, “A quantum computer controlled by superconducting digital electronics at millikelvin temperature,” *Nat. Electron.*, vol. 9, no. 3, pp. 287–294, Mar. 2026, doi: [10.1038/s41928-026-01576-6](https://doi.org/10.1038/s41928-026-01576-6). [D]
[430] P. I. Bunyk *et al.*, “Architectural considerations in the design of a superconducting quantum annealing processor,” [arXiv:1401.5504](https://arxiv.org/abs/1401.5504), Jan. 2014. [D]
[492] U.S. Securities and Exchange Commission, “EDGAR full-text search: ‘SkyWater’ in D-Wave Quantum Inc. 10-K filings,” SEC EDGAR Full-Text Search, Feb. 26, 2026. [Online]. Available: https://efts.sec.gov/LATEST/search-index?q=%22SkyWater%22&forms=10-K&ciks=0001907982 [G]
[527] A. Noori *et al.*, “A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing: Part 2,” IBM Research, Mar. 16, 2026. [Online]. Available: https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-2 [C]
[550] S. Kawabata, “Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers,” [arXiv:2601.03922](https://arxiv.org/abs/2601.03922), Jan. 2026. [S]
[556] SEEQC, “SEEQC Files Registration Statement for Proposed Initial Public Offering,” Business Wire, Jun. 29, 2026. [Online]. Available: https://www.businesswire.com/news/home/20260629077919/en/SEEQC-Files-Registration-Statement-for-Proposed-Initial-Public-Offering [P]
[565] R. McDermott and M. G. Vavilov, “Accurate Qubit Control with Single Flux Quantum Pulses,” *Phys. Rev. Appl.*, vol. 2, no. 1, Art. no. 014007, Jul. 2014, doi: [10.1103/PhysRevApplied.2.014007](https://doi.org/10.1103/PhysRevApplied.2.014007). [S]
[566] E. Leonard *et al.*, “Digital Coherent Control of a Superconducting Qubit,” *Phys. Rev. Appl.*, vol. 11, no. 1, Art. no. 014009, Jan. 2019, doi: [10.1103/PhysRevApplied.11.014009](https://doi.org/10.1103/PhysRevApplied.11.014009). [arXiv:1806.07930](https://arxiv.org/abs/1806.07930). [D]
[567] AIST; Yokohama National University; Tohoku University; NEC, “Successful demonstration of a superconducting circuit for qubit control within large-scale quantum computer systems,” NEC Press Releases, Jun. 3, 2024. [Online]. Available: https://www.nec.com/en/press/202406/global_20240603_02.html [C]
[568] S. Kamimura, A. Taguchi, M. Tanaka, and T. Yamamoto, “Fluxon Time-Delay Readout of a Superconducting Qubit Protected by a Spectral Gap in a Josephson Transmission Line,” [arXiv:2603.13175](https://arxiv.org/abs/2603.13175), Mar. 2026. [S]
[569] S. K. Tolpygo, “Superconductor Digital Electronics: Scalability and Energy Efficiency Issues,” [arXiv:1602.03546](https://arxiv.org/abs/1602.03546), Feb. 2016. [D]
[570] MIT Lincoln Laboratory, “SQUILL Foundry.” [Online]. Available: https://www.ll.mit.edu/r-d/projects/squill-foundry [C]
[571] T. Yamae *et al.*, “Rapid single-flux-quantum and adiabatic quantum-flux-parametron cell libraries using a 1 kA/cm2 niobium fabrication process,” *Scientific Reports*, vol. 15, Art. no. 41429, Nov. 2025, doi: [10.1038/s41598-025-20666-7](https://doi.org/10.1038/s41598-025-20666-7). [D]
[572] SEEQC, “SEEQC Secures $22.4 Million In Series A Round; Strategic Investment Led By EQT Ventures,” Sep. 16, 2020. [Online]. Available: https://seeqc.com/resources/seeqc-secures-22.4-million-in-series-a-round-strategic-investment-led-by-eqt-ventures [C]
[573] SIP Global Partners, “SIP Global Partners Participates in $30M Round for SEEQC, Developer of the World's First Full-Stack Processor for Quantum Computers,” PRWeb, Jan. 16, 2025. [Online]. Available: https://www.prweb.com/releases/sip-global-partners-participates-in-30m-round-for-seeqc-developer-of-the-worlds-first-full-stack-processor-for-quantum-computers-302352970.html [P]
[574] Allegro Merger Corp.; SeeQC, Inc., “Settlement, Termination and Release Agreement,” U.S. Securities and Exchange Commission (EDGAR), Aug. 2026. [Online]. Available: https://www.sec.gov/Archives/edgar/data/1779977/000121390026095175/ea028847004ex2-2.htm [G]

## Открытые пункты верификации

- Основной текст [304] за платным доступом: пять кубитов, 10 mK и «нановатты на кубит» взяты из прессы [53], а не из аннотации.
- Параметры процесса SFQ5ee MIT-LL получить не удалось; [570] описывает только кубитную фабрику.
- Датированного китайского результата 2025–26 гг. по SFQ-управлению кубитами не найдено; счёта патентных семейств нет.
- Выручка, денежные средства и объём размещения SEEQC не раскрыты [556]; оценка предприятия взята из отраслевой прессы.
- Сверхпроводниковые возможности SkyWater выведены из упоминаний в отчётах D-Wave по форме 10-K [492].
