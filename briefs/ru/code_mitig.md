---
id: code_mitig
name: Смягчение ошибок в слоте кода (ZNE, PEC) — не код
layer: "7 Код"
status: demonstrated
since: 2017
one_line: "Классическая постобработка множества зашумлённых запусков — экстраполяция к нулевому шуму, вероятностная компенсация или усиление ошибок, твирлинг считывания, тензорно-сетевое обращение шума, — которая устраняет смещение средних значений (expectation values), не кодируя, не обнаруживая и не исправляя ни одной ошибки."
verdict: "Единственная обработка ошибок в большинстве сверхпроводниковых экспериментов масштаба полезности (utility-scale), включая два из трёх заявлений IBM о преимуществе (advantage) июля 2026 г.; оно покупает снижение смещения ценой числа запусков, экспоненциального по суммарной ошибке схемы, и не даёт ни одного логического кубита, так что по состоянию на 2026-09-26 это заменитель кода, а не шаг к нему."
updated: 2026-09-26
---

ZNE = экстраполяция к нулевому шуму (zero-noise extrapolation); PEC = вероятностная компенсация ошибок (probabilistic error cancellation); PEA = вероятностное усиление ошибок (probabilistic error amplification); TREX = подавление ошибок считывания твирлингом (twirled readout error extinction); TEM = тензорно-сетевое смягчение ошибок (tensor-network error mitigation); γ = норма знакопеременной смеси, обращающей шум; P = суммарная вероятность паулиевских ошибок в обратном световом конусе наблюдаемой (гейтах, которые могут на неё повлиять); CZ = контролируемый Z (controlled-Z); G1–G7 = классы целей отчёта (см. «Акторы и экономика»).

## Идентичность и происхождение
Смягчение ошибок (error mitigation) оценивает бесшумное среднее значение наблюдаемой по множеству зашумлённых запусков и классической постобработке; ничего не кодируется, ни один синдром не измеряется, ни одна ошибка не исправляется [G][693]. Temme, Bravyi и Gambetta в 2016 г. предложили экстраполяцию к нулевому шуму методом Ричардсона и компенсацию путём квазивероятностной перевыборки [D][694]; Li и Benjamin независимо экстраполировали усиленные ошибки к нулю [D][695]. Аппаратная ZNE последовала в 2019 г. [D][696]; затем появились PEA, усиливающее выученную модель шума внедрёнными паулиевскими ошибками [D][308], TREX для считывания [C][693] и TEM — тензорно-сетевое обращение глобального шума [S][697]. Атрибуты: не зависит от платформы, статическое, без транспорта и модальности управления; после твирлинга класс ошибки паулиевский.

## Физика и пределы
PEC записывает обратный шум каждого слоя как знакопеременную смесь реализуемых операций с нормой γ ≥ 1; оценка несмещённая, но число запусков растёт как γ², а γ — экспоненциально с глубиной [C][693]. Для паулиевского шума γ ≈ e^(2P), поэтому число запусков умножается на ≈ e^(4P) [S]. При медианной ошибке CZ у Heron r3 в 0.15% [D][698] 1,000 CZ в световом конусе дают P ≈ 1.5 и ≈ 400× запусков, 7,500 — ~10¹⁹× [S]; сегодняшние бюджеты 10²–10³× ограничивают P величиной около 1.2–1.7 [S]. ZNE делает выборки при усиленном шуме — по умолчанию с тремя коэффициентами, номинально ~3× [C][693], — и экстраполирует; она смещена своей аппроксимацией и должна различить сигнал, ослабленный вплоть до e^(−2P), поэтому её стоимость растёт сопоставимо [S]. TEM заявляет квадратный корень из накладных расходов PEC [S][697] — всё равно экспоненциально [S]. Предел общий: при локальном деполяризующем шуме накладные расходы любого протокола растут экспоненциально с глубиной [D][699], включая нелинейную постобработку [D][700], а оценка в худшем случае требует суперполиномиально многих выборок уже при малой глубине [D][701]. Сдвинуть показатель экспоненты может только меньшая физическая ошибка.

## Инженерное состояние (state of the art)
| Год | Показатель | Кто | Тег+ключ |
|---|---|---|---|
| 2019-03-27 | ZNE растяжением импульсов; вариационная химия и магнетизм | IBM, Kandala et al. | [D][696] |
| 2023-05-08 | PEC с выученной разреженной моделью Паули–Линдблада, включая перекрёстные помехи, 20 кубитов | IBM, van den Berg et al. | [D][702] |
| 2023-06-14 | 127 кубитов, до 60 слоёв, 2,880 CNOT; ZNE с PEA | IBM Eagle, Kim et al. | [D][308] |
| 2023-06/08 | Классические воспроизведения: тензорная сеть точнее аппаратуры; паулиевская динамика на одном ядре ноутбука; сходимость до <0.01 | Tindall et al.; Begušić, Chan; Begušić, Gray, Chan | [D][309][D][703][D][704] |
| 2025-11-12 | «samplomatic» сокращает выборочные накладные расходы PEC в 100× | IBM | [C][486] |
| 2026-07-27 | QESEM (на основе PEC и ZNE) на Heron r3, 51–74 кубита, до 30 циклов Флоке; тензорные сети не сходятся | Qedma, RIKEN, BlueQubit | [D][233] |
| 2026-07-28 | PEC на 56 кубитах, схемы до ~1,000 CZ: ~1.5 h и ~4 h времени QPU на двух глубинах | Algorithmiq et al., ibm_boston | [D][698] |
| 2026-08-31 | Оценка наблюдаемых с PEA на схемах из 7,500 гейтов | IBM Nighthawk r2 | [C][601] |

Заявление 2023 г. о точности «за пределами классических вычислений методом полного перебора» [D][308] было классически повторено в течение нескольких недель, а сошедшиеся значения выявили смещение в его экстраполяции [D][704]; заявления 2026 г. опираются на расхождение классических эвристик, а не на доказанную сложность [D][698]. Доминирующий член: P. Более быстрые запуски — 100,000 схем в секунду у Nighthawk r2, в 25× больше, чем у Heron, — сокращают реальное время выполнения, а не показатель экспоненты [C][601].

## Производство, материалы и цепочка поставок
Ничего не изготавливается; счёт выставляется временем QPU и классическими вычислениями — 3.2 млн запусков, ~45 min времени QPU на точку для перемасштабированной оценки Algorithmiq [D][698]. Поставка — это среда выполнения (runtime) поставщика [C][693], плюс QESEM от Qedma, который выучивает шум устройства, адаптирует схемы и выполняет постобработку [C][705], и TEM от Algorithmiq в Qiskit Functions Catalog от IBM [C][706].

## Управление, считывание и нагрузка на ввод-вывод
Требование — калиброванная стабильная модель шума: PEA и PEC выучивают разреженную модель Паули–Линдблада для каждого слоя перепутывающих гейтов при случайном паулиевском твирлинге [D][308][D][702]; каждая схема компилируется во множестве рандомизированных экземпляров [S]. TREX рандомизирует измерения гейтами X и классическими переворотами битов, диагонализуя матрицу считывания для её обращения [C][693]. Режим отказа — дрейф: модель, выученная перед четырёхчасовым запуском PEC, ошибочна ровно на то, что дрейфует во время него [S]. Прямой связи (feed-forward) нет, а на выходе — средние значения, а не выборки [G][693].

## Роль в стеке
Слот 7 архитектуры «Решётка трансмонов с перестраиваемыми каплерами», рядом с code_surface, code_color, code_qldpc, code_magic и code_detect. Технология **требует** ct_rt — ради калиброванных моделей шума; вниз по стеку она ничего не **обеспечивает** — ни логического кубита, ни синдрома для декодеров слота 8; её **заменяет** code_surface, а открытое ребро конфликта (2023-06) не указывает никакого средства против её экспоненциальных накладных расходов. code_detect отбрасывает помеченные запуски ценой множителя 1/acceptance (обратной доли принятых запусков), тоже экспоненциального по размеру схемы; смягчение ошибок сохраняет каждый запуск и перевзвешивает, устраняя смещение лишь в среднем [S]. Формулировка реестра пробелов «все три заявления IBM о преимуществе июля 2026 г.» на деле означает два из трёх — QESEM на Heron r3 [D][233] и PEC на ibm_boston [D][698]; заявление IBM–UChicago использует послеотбор на пространственно-временных кодах, это результат code_detect [C][45]. Предложенное в реестре пробелов размещение на ионах не принято, хотя Qedma повторила циклы на Quantinuum H2 и Helios [D][233]. Реестр: IBM Eagle r1–r3 (основная, выведены из эксплуатации); Heron r3 и Nighthawk r2 (альтернативная).

## Свидетельства — как измерены числа
PEC несмещённа и даёт планки погрешностей, если её модель шума верна, поэтому верификация сводится к валидации модели [C][45]. Из семи ячеек реестра верифицирована ✅ одна (Nighthawk r2, с локатором раздела); шесть — 🔎. Источник Eagle подтверждает его ячейку; Heron r1 и r3 ссылаются на статью в прессе об r3, которая не называет ни одного метода смягчения [P][707], а препринты по ibm_boston июля 2026 г. — недостающее первичное свидетельство для r3; Nighthawk r1 ссылается на блог об r2. Zuchongzhi 3.0 и Tianyan-287 выполняют выборку из случайных схем (random-circuit sampling), оцениваемую по сырой точности; их аннотации не упоминают ни смягчения, ни коррекции ошибок [D][35][D][708], так что по состоянию на 2026-09-26 их слот кода пуст, а не занят смягчением.

## Акторы и экономика
**Кто.**
| Организация | Роль | Страна | Что именно они делают с этой технологией | Свидетельства |
|---|---|---|---|---|
| IBM | разработчик | США | TREX, ZNE, PEA, PEC в Qiskit Runtime; эксперимент utility 2023 г.; PEA на 7,500 гейтах | [C][693][D][308][C][601] |
| Qedma | поставщик ПО | Израиль | QESEM: выучивание шума, оценщики на основе PEC и ZNE | [D][233] |
| Algorithmiq | поставщик ПО | Италия (ранее Финляндия) | TEM в каталоге IBM; PEC в заявлении на основе эха Лошмидта | [C][706][D][698] |
| Flatiron Institute | исследования | США | Участник открытого трекера преимущества | [C][486] |

**Деньги.**
- 2025-07-03 · Qedma · Series A во главе с Glilot Capital Partners при участии IBM · USD 26 M · объявлено [C][705]
- 2026-05-11 · Algorithmiq · раунд во главе с United Ventures, с участием CDP и Inventure · EUR 18 M (всего EUR 36 M) · объявлено [C][709]

**Рынок и цепочка поставок.** Продаётся как опции среды выполнения и функции третьих сторон в облаке поставщика аппаратуры, причём IBM владеет долей в Qedma: вертикально связанный рынок. Работает только на G2; G3–G4 нужен код.

**ИС и стандарты.** Ни один стандарт не определяет ни показателя качества для оценок со смягчением ошибок, ни формата раскрытия модели шума; датированного подсчёта патентов по названной базе данных нет по состоянию на 2026-09-26.

**Дорожные карты и послужной список.** IBM обещала ревизии Nighthawk на 5,000, 7,500, 10,000 и 15,000 гейтов [R][486]; шаг в 7,500 гейтов, её веха на 2026 г., поставлен 2026-08-31 с PEA [C][601].

**Стратегическое прочтение.** Смягчение ошибок делает продуктом модель шума и удерживает стоимость внутри стека поставщика аппаратуры. В отказоустойчивость переходит только выучивание шума; когда работает код, технология пустеет.

## Прогноз и открытые вопросы
Подтвердить, если к 2027-12-31 появится несмещённая оценка PEC на ≥5,000 гейтах с планками погрешностей или если одно из заявлений июля 2026 г. доживёт до 2027-07-31 без сошедшегося классического воспроизведения; понизить эти заявления до уровня utility, если с ними совпадут сошедшиеся значения тензорных сетей или распространения Паули (Pauli propagation), как в 2023 г.
Открытые вопросы. (1) Насколько стабильна выученная модель Паули–Линдблада на протяжении многочасового запуска при 10³–10⁴ гейтах? (2) Сохраняется ли квадратичная экономия TEM при ошибке модели на реальной аппаратуре? (3) С какого размера код обнаружения плюс смягчение ошибок выигрывает у одного смягчения по числу запусков? (4) Можно ли доказать классическую сложность задачи оценки среднего значения со смягчением ошибок? (5) Какой множитель числа запусков потратил 7,500-гейтовый запуск PEA на Nighthawk r2?

## Литература
[35] D. Gao *et al.*, “Establishing a New Benchmark in Quantum Computational Advantage with 105-qubit Zuchongzhi 3.0 Processor,” *Phys. Rev. Lett.*, vol. 134, Art. no. 090601, Mar. 2025, doi: [10.1103/PhysRevLett.134.090601](https://doi.org/10.1103/PhysRevLett.134.090601). [arXiv:2412.11924](https://arxiv.org/abs/2412.11924). [D]
[45] A. Kandala, A. Javadi-Abhari, and J. Gambetta, “Researchers demonstrate quantum advantage through trusted quantum computation,” IBM Quantum Computing Blog, Jul. 30, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/quantum-advantage [C]
[233] E. Leviatan *et al.*, “Resolving Structure in Prethermal Floquet Dynamics with Precision Quantum Computation,” [arXiv:2607.24937](https://arxiv.org/abs/2607.24937), Jul. 2026. [D]
[308] Y. Kim *et al.*, “Evidence for the utility of quantum computing before fault tolerance,” *Nature*, vol. 618, no. 7965, pp. 500–505, Jun. 2023, doi: [10.1038/s41586-023-06096-3](https://doi.org/10.1038/s41586-023-06096-3). [D]
[309] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, “Efficient Tensor Network Simulation of IBM's Eagle Kicked Ising Experiment,” *PRX Quantum*, vol. 5, no. 1, Art. no. 010308, Jan. 2024, doi: [10.1103/PRXQuantum.5.010308](https://doi.org/10.1103/PRXQuantum.5.010308). [arXiv:2306.14887](https://arxiv.org/abs/2306.14887). [D]
[486] R. Mandelbaum, “Scaling for quantum advantage and beyond,” IBM Quantum Computing Blog, Nov. 12, 2025. [Online]. Available: https://www.ibm.com/quantum/blog/qdc-2025 [C]
[601] H. Haas, D. McKay, and R. Davis, “IBM Quantum Nighthawk r2—more circuits, faster,” IBM Quantum Computing Blog, Aug. 31, 2026. [Online]. Available: https://www.ibm.com/quantum/blog/nighthawk-r2 [C]
[693] IBM, “Error mitigation and suppression techniques.” [Online]. Available: https://quantum.cloud.ibm.com/docs/en/guides/error-mitigation-and-suppression-techniques [C]
[694] K. Temme, S. Bravyi, and J. M. Gambetta, “Error mitigation for short-depth quantum circuits,” *Phys. Rev. Lett.*, vol. 119, Art. no. 180509, 2017, doi: [10.1103/PhysRevLett.119.180509](https://doi.org/10.1103/PhysRevLett.119.180509). [arXiv:1612.02058](https://arxiv.org/abs/1612.02058). [D]
[695] Y. Li and S. C. Benjamin, “Efficient Variational Quantum Simulator Incorporating Active Error Minimization,” *Phys. Rev. X*, vol. 7, no. 2, Art. no. 021050, Jun. 2017, doi: [10.1103/PhysRevX.7.021050](https://doi.org/10.1103/PhysRevX.7.021050). [arXiv:1611.09301](https://arxiv.org/abs/1611.09301). [D]
[696] A. Kandala *et al.*, “Error mitigation extends the computational reach of a noisy quantum processor,” *Nature*, vol. 567, pp. 491–495, Mar. 2019, doi: [10.1038/s41586-019-1040-7](https://doi.org/10.1038/s41586-019-1040-7). [arXiv:1805.04492](https://arxiv.org/abs/1805.04492). [D]
[697] S. Filippov, M. Leahy, M. A. C. Rossi, and G. García-Pérez, “Scalable tensor-network error mitigation for near-term quantum computing,” [arXiv:2307.11740](https://arxiv.org/abs/2307.11740), Jul. 2023. [S]
[698] S. V. Barron *et al.*, “Observable Estimation in the Absence of Classical Verification,” [arXiv:2607.25998](https://arxiv.org/abs/2607.25998), Jul. 2026. [D]
[699] R. Takagi, S. Endo, S. Minagawa, and M. Gu, “Fundamental limits of quantum error mitigation,” *npj Quantum Inf.*, vol. 8, Art. no. 114, 2022, doi: [10.1038/s41534-022-00618-z](https://doi.org/10.1038/s41534-022-00618-z). [arXiv:2109.04457](https://arxiv.org/abs/2109.04457). [D]
[700] R. Takagi, H. Tajima, and M. Gu, “Universal Sampling Lower Bounds for Quantum Error Mitigation,” *Phys. Rev. Lett.*, vol. 131, Art. no. 210602, 2023, doi: [10.1103/PhysRevLett.131.210602](https://doi.org/10.1103/PhysRevLett.131.210602). [arXiv:2208.09178](https://arxiv.org/abs/2208.09178). [D]
[701] Y. Quek, D. S. França, S. Khatri, J. J. Meyer, and J. Eisert, “Exponentially tighter bounds on limitations of quantum error mitigation,” *Nat. Phys.*, vol. 20, p. 1648, 2024, doi: [10.1038/s41567-024-02536-7](https://doi.org/10.1038/s41567-024-02536-7). [arXiv:2210.11505](https://arxiv.org/abs/2210.11505). [D]
[702] E. van den Berg, Z. K. Minev, A. Kandala, and K. Temme, “Probabilistic error cancellation with sparse Pauli–Lindblad models on noisy quantum processors,” *Nat. Phys.*, vol. 19, no. 8, pp. 1116–1121, May 2023, doi: [10.1038/s41567-023-02042-2](https://doi.org/10.1038/s41567-023-02042-2). [arXiv:2201.09866](https://arxiv.org/abs/2201.09866). [D]
[703] T. Begušić and G. K.-L. Chan, “Fast classical simulation of evidence for the utility of quantum computing before fault tolerance,” [arXiv:2306.16372](https://arxiv.org/abs/2306.16372), Jun. 2023. [D]
[704] T. Begušić, J. Gray, and G. K.-L. Chan, “Fast and converged classical simulations of evidence for the utility of quantum computing before fault tolerance,” *Sci. Adv.*, Art. no. eadk4321, 2024, doi: [10.1126/sciadv.adk4321](https://doi.org/10.1126/sciadv.adk4321). [arXiv:2308.05077](https://arxiv.org/abs/2308.05077). [D]
[705] QEDMA, “QEDMA raises $26M with participation from IBM to tackle quantum computing errors and accelerate pace to quantum advantage,” PR Newswire, Jul. 3, 2025. [Online]. Available: https://www.prnewswire.com/news-releases/qedma-raises-26m-with-participation-from-ibm-to-tackle-quantum-computing-errors-and-accelerate-pace-to-quantum-advantage-302497701.html [C]
[706] Algorithmiq, “Algorithmiq Launches High-Performing Error Mitigation Solution in IBM's Qiskit Functions Catalog,” Sep. 16, 2024. [Online]. Available: https://www.algorithmiq.fi/news/press-release-tem-ibm-qiskit-functions/ [C]
[707] M. Ivezic, “IBM Launches Heron R3 (ibm_pittsburgh): ~350 uS T2 and a Quality Upgrade for Its 156-Qubit Platform,” PostQuantum.com, Aug. 1, 2025. [Online]. Available: https://postquantum.com/industry-news/ibm-heron-r3-pittsburgh/ [P]
[708] T. Q. Group, “Tianyan: Cloud services with quantum advantage,” [arXiv:2512.10504](https://arxiv.org/abs/2512.10504), Dec. 2025. [D]
[709] Algorithmiq, “Algorithmiq Establishes Milan Headquarters and raises €18m to Position Europe as the Future of Quantum Software,” May 11, 2026. [Online]. Available: https://algorithmiq.fi/news/algorithmiq-establishes-milan-headquarters-and-raises-18m-to-position-europe-as-the-future-of-quantum-software/ [C]

## Открытые пункты верификации
- Заявленное IBM сокращение накладных расходов PEC в 100× с помощью samplomatic (2025-11-12) — утверждение из блога; статьи с указанием базового уровня или класса схем не найдено (попытка 2026-09-26).
- 7,500-гейтовый запуск PEA на Nighthawk r2: число запусков, время QPU и наблюдаемая в блоге не указаны (проверено 2026-09-26).
- Zuchongzhi 3.0 и Tianyan-287: прочитаны только аннотации на arXiv; полные тексты на наличие шага смягчения ошибок не проверялись (2026-09-26).
- Heron r1: не найдено первичного источника, показывающего, что названный метод смягчения ошибок выполнялся на самом r1 (2026-09-26).
- Том и выпуск Science Advances для Begušić, Gray и Chan не подтверждены (Crossref ограничил частоту запросов, PubMed Central закрыт капчей, 2026-09-26); заголовок статьи о TREX (arXiv:2012.09738) прочитать не удалось, поэтому TREX цитируется по документации IBM.
- Масштабирование числа запусков e^(4P) и значения P выведены здесь из конструкции PEC и опубликованных частот ошибок, а не процитированы из источника.
