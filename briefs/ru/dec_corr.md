---
id: dec_corr
name: Коррелированное декодирование / декодирование с учётом потерь (трансверсальное, потеря атомов)
layer: "8 Декодер"
tier: 3
status: demonstrated
since: 2025
one_line: Декодеры, которые принимают геральды потери атома как локализованные стирания и декодируют сразу по трансверсальным слоям гейтов, а не раунд за раундом.
verdict: Реально на одном наборе данных (1.73(13)× против декодера, слепого к потерям, 448 атомов, четыре раунда); не подтверждено ни при дозагрузке, ни на глубине, ни во второй лаборатории.
updated: 2026-09-03
---

Λ = коэффициент подавления ошибки на шаг кодового расстояния; QBI = DARPA Quantum Benchmarking Initiative (стадия A — концепция → B — план НИОКР → C — государственная верификация и валидация); G1–G7 = классы целей настоящего отчёта (см. «Акторы и экономика»).

## Идентичность и происхождение
Не железо, а дисциплина декодирования. Декодирование с учётом потерь потребляет геральд (herald): отсутствующий атом — это стирание (erasure) в известной позиции, поэтому стабилизаторы, задевающие вакансию, перемножаются в операторы *суперпроверки* большего веса, по-прежнему коммутирующие с уцелевшим кодом [1]. Коррелированное декодирование решает совместную историю синдромов сразу по трансверсальным (блок-в-блок) слоям, а не поблочно; Cain et al. (Harvard, 2024-03-05) показали, что число раундов между клиффордовыми гейтами падает как O(d)→O(1) [2], что затем обобщено как алгоритмическая отказоустойчивость (Nature 2025) [3].
f = потери + стирание; a/c/d/e/g = отсутствуют — классические вычисления, ни производства, ни размещения [запись графа].

## Физика и пределы
Активом здесь является сам геральд: >80% утечки (leakage) в ридберговских массивах приходится на потерю атома, и визуализация её находит [1]. Локализованное стирание стоит декодеру только паулевского фрейма, но не позиции — именно поэтому конверсия в стирание поднимает пороги схемного уровня в 3–4× при неизменной физике гейта [4]. Платой служит расстояние: каждая суперпроверка есть произведение двух стабилизаторов, так что всякая вакансия локально прореживает код. Коррелированное декодирование платит иначе: трансверсальные CNOT переносят ошибки между блоками, поэтому граф растёт с глубиной схемы, а не с d. Нижнюю границу не сдвигает ничто — негеральдированный остаток остаётся нетронутым: утечка по m_F составляет 0.008(1)% на атом на гейт против 0.087(5)% потери атома [G:HARVARD-CZ-2026-04].
## Инженерное состояние (state of the art)
| Дата | Показатель | Кто | Тег+ключ |
|---|---|---|---|
| 2025-11-10 | Выигрыш 1.73(13)× от флагов потерь + ML относительно обычного декодирования, те же данные на 448 атомов | Harvard/MIT/QuEra | [D][1][G:HARVARD-LOSS-QEC-2025] |
| 2026-03 | Декодер коррелированных потерь: порог 4% против 3.2% в предположении независимых потерь; 144 µs на раунд; моделирование | QPerfect | [S][5][G:QPERFECT-CORRLOSS-2026-03] |
| 2026-06-12 | [[4,2,2]] на ¹⁷¹Yb: безусловный распад в 1.9(4)× медленнее при использовании информации о стираниях (3.6(1)× — это пост-селектированное удержание) | Princeton | [D][6][G:PRINCETON-ERASURE-RESOLVED-2026-09] |

Та же схема: 2.14(13)×, d=3→5, четыре раунда. Доминирующий член: потеря атома, а не ошибка Паули.

## Производство, материалы и цепочка поставок
Никакой фабрики: классические вычислители уже куплены под паросочетание. Область применения задаёт задержка: 144 µs на раунд укладываются в атомный цикл 1–4.5 ms с запасом 7–30× [5], но превышают сверхпроводниковый цикл 1.1 µs в ~130× — вот почему это остаётся специфичным для атомов. Полоса под флаги потерь составляет один бит на узел за раунд, поэтому стеной на 10³–10⁴ атомов оказываются визуализация в ~0.5–1 ms и окно декодирования, растущее с логической глубиной, а вовсе не канал связи. Унаследованные единые точки отказа: визуализация на qCMOS от Hamamatsu [G:HAMAMATSU-CAMERA-CONC-2026] и два поставщика AOD [G:AOD-VENDORS-2026].

## Роль в стеке
Требует высокоскоростных конкатенированных кодов с трансверсальными гейтами; предоставляет декодирующую половину алгоритмической отказоустойчивости, чьё утверждение о постоянном числе раундов иначе ничем на железе не подкреплено. Производный такт = max(гейт 270 ns, считывание ~1 ms, транспорт ~100 µs) ≈ 1 ms, ~1.0 kHz; декодер обязан уложиться внутрь него, а не задавать его. Верификация: 1.73× — это отношение декодера к декодеру на данных одной лаборатории, невоспроизведённое; 4% — моделирование [5].  Четыре раунда не проверяют ни дрейф, ни дозагрузку; контролем служит тороидальный код Atom Computing, где подавление при дозагрузке исчезает (0.63% против 0.64% за цикл) [7]. Расхождение 1.9(4)×/3.6(1)× у Princeton разрешено: одна работа, две разные величины [G:PRINCETON-ERASURE-RESOLVED-2026-09].

## Акторы и экономика
**Кто.**

| Организация | Роль | Страна | Что именно | Свидетельство |
|---|---|---|---|---|
| Harvard/MIT | исследования | США | Коррелированное декодирование, суперпроверки, 1.73(13)× | [D][1][2] |
| QuEra | разработчик | США | Соавтор; Libra 2028 на это рассчитывает | [D][1][C][8] |
| QPerfect (BTQ) | поставщик | Франция | Декодер коррелированных потерь; цифровой двойник aQCess | [S][5][C][10] |
| Atom Computing | пользователь | США | Yb с нативным стиранием; контрпример с дозагрузкой | [D][7][C][11] |

**Деньги.**
2025-04-09 · BTQ Technologies · €2 M в QPerfect при оценке €10 M pre-money (16.67%) · term sheet [P][9]
2026-07-22 · QPerfect · цифровой двойник aQCess, Equipex+ ANR-21-ESRE-0032 · объявлено [C][10]
2026-06-16 · Atom Computing · $100 M раунда Series C (Third Point) + LOI по CHIPS на $100 M · закрыт + LOI [C][11][G:ATOM-300M-2026-06]
2025-11-06 · DARPA QBI Stage B · Atom Computing, QuEra среди одиннадцати · ≤$15 M каждому [G:QBI-STAGEB-2025-11]

**Рынок и цепочка поставок.** Рынка компонентов нет: такты GPU/FPGA уже куплены под паросочетание; риск концентрации лежит выше по цепочке — в визуализации и AOD. Платит только по G3/G4.

**ИС и стандарты.** Ни одно датированное патентное семейство не называет декодирование с учётом потерь или коррелированное декодирование по состоянию на 4 сентября 2026 г.; методы открыты, код академический.

**Дорожные карты и послужной список.** Раунды O(d)→O(1) (2024-03): в Nature 2025 показаны только в схеме из четырёх раундов. QuEra, 100 логических (2024-01, на 2026 год): теперь Libra 2028 [G:QUERA-LIBRA-2026]. Физика в срок, продукты с опозданием.

**Стратегическое прочтение.** Если это устоит, атомы превращают свой худший недостаток в дешёвый учитываемый канал, а трансверсальные архитектуры обыгрывают решёточную хирургию по пространственно-временной стоимости: выигрывают QuEra, Atom Computing, Pasqal и Infleqtion, а сверхпроводниковые вендоры теряют задержку декодера как отличительное преимущество. Угроза замещения: ридберговский CZ выше 99.95% сжимает член потерь. Неконкурентное благо: сдать его в аренду не может ни один поставщик.

*Открытая ниша:* оба заголовочных числа суть отношения к базовой линии, выбранной той же самой командой; QCVV-коллектив без собственного атомного железа может заново вывести 1.73× относительно оптимального слепого к потерям декодера на опубликованных данных синдромов и проверить порог 4% на прочность при дозагрузке.

## Прогноз и открытые вопросы
Подтвердить, если декодер QPerfect отработает на реальных синдромах либо второй вендор опубликует собственный выигрыш от учёта потерь; понизить в статусе, если выигрыш умрёт при дозагрузке или за пределами четырёх раундов. Лучший случай к 2029 году: значение по умолчанию во всех отказоустойчивых стеках на нейтральных атомах; худший — архитектура одной группы, никогда не выходящая за 10³ атомов. Открыто: держится ли 1.73× на 10⁴ атомах, на глубинах, где коррелированный граф перерастает память, и на ионах [12]?

## Источники
[1] Bluvstein et al. (Harvard/MIT/QuEra), "Architectural mechanisms of a universal fault-tolerant quantum computer", Nature 649, 39, 2025-11-10 (arXiv:2506.20661) — https://www.nature.com/articles/s41586-025-09848-5
[2] Cain, Zhao, Zhou, Meister, Bonilla Ataides, Jaffe, Bluvstein, Lukin, "Correlated decoding of logical algorithms with transversal gates", arXiv:2403.03272, 2024-03-05 (rev. 2025-04-07) — https://arxiv.org/abs/2403.03272
[3] Zhou, Zhao, Cain, Bluvstein, Maskara, Duckering, Hu, Wang, Kubica, Lukin, "Low-overhead transversal fault tolerance for universal quantum computation", Nature, 2025, doi 10.1038/s41586-025-09543-5 (arXiv:2406.17653) — https://arxiv.org/abs/2406.17653
[4] Wu, Kolkowitz, Puri, Thompson, "Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays", arXiv:2201.03540, 2022-01 — https://arxiv.org/abs/2201.03540
[5] Perrin, Roger, Pupillo (Univ. Strasbourg/CNRS, QPerfect SAS), "Correlated atom loss as a resource for quantum error correction", arXiv:2603.24237, 2026-03 — https://arxiv.org/html/2603.24237
[6] Princeton, [[4,2,2]] metastable ¹⁷¹Yb erasure conversion, Nature Physics 22, 910, 2026-06-12 (arXiv:2506.13724v2) — https://arxiv.org/html/2506.13724v2
[7] Atom Computing/Microsoft, toric code with continuous reloading, arXiv:2606.04079, 2026-06 — https://arxiv.org/abs/2606.04079
[8] QuEra, $230 M financing round, press release [C] — https://www.quera.com/press-releases/quera-expands-230-million-financing-round-advancing-quantum-accelerated-supercomputing
[9] The Quantum Insider, "BTQ Technologies to invest over $2 million in QPerfect", 2025-04-09 [P] — https://thequantuminsider.com/2025/04/09/btq-technologies-to-invest-over-2-million-in-qperfect-to-advance-neutral-atom-quantum-computing/
[10] BTQ Technologies / QPerfect and University of Strasbourg, aQCess partnership, PR Newswire, 2026-07-22 [C] — https://www.prnewswire.com/news-releases/btq-technologies-qperfect-subsidiary-and-the-university-of-strasbourg-partner-to-support-frances-first-public-neutral-atom-quantum-computing-platform-302831874.html
[11] Atom Computing, raise of more than $300 M including a $100 M DoC letter of intent, 2026-06-16 [C] — https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[12] Microsoft Quantum + Quantinuum, [[16,6,4]] tesseract code, Nature 654, 2026-06-10 — https://www.nature.com/articles/s41586-026-10628-y
[G] Bluvstein et al. (Harvard/MIT/QuEra), Nature 649, 39 (online 2025-11-10; arXiv:2506.20661, 2025-06-25): surface code on up to 448 atoms, 2.14(13)× below threshold in a four-round c… · 2025-11-10 · https://www.nature.com/articles/s41586-025-09848-5
[G] Evered, Xu, Li, Geim, Bonilla Ataides, Kalinowski, Bluvstein, Maskara, Kokail, Greiner, Vuletic, Lukin (Harvard/MIT), "High-fidelity entangling gates and nonlocal circuits with neu… · 2026-04-28 · https://arxiv.org/abs/2604.25987
[G] Perrin, Roger, Pupillo (Univ. Strasbourg/CNRS, QPERFECT SAS), "Correlated Atom Loss as a Resource for Quantum Error Correction", arXiv:2603.24237 (2026-03): fast correlated-loss de… · 2026-03 · https://arxiv.org/html/2603.24237
[G] CONFLICT RESOLVED: the 1.9(4)x and 3.6x figures both appear in arXiv:2506.13724v2 (Princeton [[4,2,2]] metastable 171-Yb) and describe different quantities — the logical decay rate… · 2026-09-04 · https://arxiv.org/html/2506.13724v2
[G] Hamamatsu Photonics ORCA-Quest qCMOS is the named single-photon-sensitivity camera in the Harvard/QuEra 448-atom fluorescence-imaging line and in MIT, NIST/UMD and Osaka neutral-at… · 2026-09 · https://www.hamamatsu.com/us/en/news/events/2026/APS-DAMOP-2026.html
[G] Only two acousto-optic deflector suppliers are named across the sourced neutral-atom literature: AA Opto-Electronic (France; DTSX-400 crossed AODs in the Harvard 448-atom system, a… · 2026-09-04 · https://gandh.com/news-and-resources/g-and-h-acousto-optic-deflectors-in-nature-papers
[G] QuEra: Libra fault-tolerant system 2028 (>256 logical, 10⁻⁶, on Braket) and gigaquop system 2028–29 — its Jan-2024 roadmap had promised 100 logical qubits in 2026 · 2026-06-15 · https://www.quera.com/press-releases/quera-announces-2028-fault-tolerant-quantum-computer-and-expanded-multi-year-strategic-collaboration-with-aws
[G] Atom Computing: $100 M Series C (Third Point) plus $100 M DoC CHIPS LOI, total > $300 M, 2026-06-16 · 2026-06-16 · https://www.prnewswire.com/news-releases/atom-computing-raises-more-than-300-million-to-accelerate-deployment-of-fault-tolerant-neutral-atom-quantum-computers-302800832.html
[G] DARPA QBI Stage B (announced 2025-11-06, ~12 months, up to $15 M each): Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon… · 2025-11-06 · https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
## Открытые пункты верификации
- Выигрыш 1.73(13)× не воспроизведён за пределами набора данных Harvard/MIT/QuEra на 448 атомов, а базовый декодер для сравнения выбирала та же команда.
- Порог 4% против 3.2% у QPerfect получен исключительно моделированием; проверки на аппаратных синдромах по состоянию на 4 сентября 2026 г. не найдено.
- Опцион BTQ на полное приобретение QPerfect был исполнен между 2025-04 и 2026-07 (более поздний релиз называет QPerfect полностью принадлежащей компанией); датированного закрытия сделки или цены не найдено.
- Датированного патентного семейства по декодированию с учётом потерь или коррелированному декодированию не найдено.
