# -*- coding: utf-8 -*-
"""§8 "Machines" of the report — generated from data/machines.json (the machines register joined to the map)
and data/graph.json. Deterministic: same inputs give identical markdown. Called by make_sections.py (splice)
in both languages. Every number in the chapter is computed here; the prose states the claim, the test and the
verdict, so a reader can re-run the test on the register.

Classifiers (kept simple and visible, so a reviewer can disagree with a line, not with a model):
  status class   = first word of the register's status (DEPLOYED / DEMONSTRATED / ANNOUNCED / PLANNED / RETIRED / OTHER)
  cohort year    = first four-digit year in status_date
  device         = status class in {DEPLOYED, DEMONSTRATED, RETIRED} and no flag in {target-not-device, component-only}
  gate-capable   = device without a flag in {analog-only, no-entangling-gate, 1q-only, enabler-only, detection-only, not-a-qubit}
  control class  = integrated (on-chip microwave / cryo-CMOS / SFQ / flux DAC / 4 K), optics, room-temperature electronics, undisclosed
  decoding class = in-loop / offline / planned / none, from the register's `realtime` field
"""
import json, os, re, statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAM_ORDER = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']
FAMN = {'SC': ('superconducting circuits', 'сверхпроводниковые схемы'), 'ION': ('trapped ions', 'ионы в ловушках'), 'ATOM': ('neutral atoms', 'нейтральные атомы'), 'PHOTON': ('photonics', 'фотоника'), 'SPIN': ('semiconductor spins', 'полупроводниковые спины'), 'DEFECT': ('defect spins', 'дефектные спины'), 'TOPO': ('topological', 'топологические'), 'ANNEAL': ('quantum annealers', 'квантовый отжиг')}
STAT_ORDER = ['DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED', 'RETIRED', 'OTHER']
STATN = {'DEPLOYED': ('deployed', 'в эксплуатации'), 'DEMONSTRATED': ('demonstrated', 'продемонстрирована'),
         'ANNOUNCED': ('announced', 'анонсирована'), 'PLANNED': ('planned', 'запланирована'),
         'RETIRED': ('retired', 'выведена'), 'OTHER': ('other', 'прочее')}
NON_DEVICE_FLAGS = {'target-not-device', 'component-only'}
EXCL_ERR_FLAGS = {'hero-pair-number', 'target-not-device', 'component-only'}
NON_GATE_FLAGS = {'analog-only', 'no-entangling-gate', '1q-only', 'enabler-only', 'detection-only', 'not-a-qubit'}
LAYER_ORDER = ['carrier', 'encoding', 'gate', 'connect', 'control', 'readout', 'code', 'decoder', 'interconnect', 'fab']


def t(lang, pair): return pair[0] if lang == 'en' else pair[1]


def mdcell(x): return str(x).replace('|', '\\|') if x is not None else '—'


def status_class(s):
    u = (s or '').upper()
    for k in ('RETIRED', 'DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED'):
        if u.startswith(k): return k
    return 'OTHER'


def year_of(s):
    m = re.findall(r'(20\d\d)', s or '')
    return int(m[0]) if m else None


def control_class(s):
    u = (s or '').lower()
    if not u or 'undisclosed' in u or 'not disclosed' in u: return 'undisclosed'
    if any(k in u for k in ('cryo', 'sfq', 'flux dac', '4 k', 'on-chip')): return 'integrated'
    if 'optic' in u or 'laser' in u: return 'optics'
    if 'room' in u or 'baseband' in u: return 'room'
    return 'undisclosed'


def cryo_integrated(s):
    u = (s or '').lower()
    return any(k in u for k in ('cryo', 'sfq', 'flux dac', '4 k'))


def decoding_class(s):
    u = (s or '').lower().strip()
    if u.startswith('in-loop') or ('real-time' in u and not u.startswith(('planned', 'offline', 'none'))): return 'in-loop'
    if u.startswith('offline'): return 'offline'
    if u.startswith('planned') or u.startswith('intended'): return 'planned'
    return 'none'


SUP = str.maketrans('0123456789-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻')


def fmt_e(x):
    """4.0×10⁻³ — one decimal, Unicode superscript exponent (the report's style for error rates)."""
    if x is None: return '—'
    m, e = ('%.1e' % x).split('e')
    return '%s×10%s' % (m, str(int(e)).translate(SUP))


def median(xs): return statistics.median(xs) if xs else None


def fmt_n(x):
    if x is None: return '—'
    return '%g' % x if abs(x - round(x)) > 1e-9 else '{:,}'.format(int(round(x)))


def pct(a, b): return '%d %%' % round(100.0 * a / b) if b else '—'


def prep():
    M = json.load(open(os.path.join(ROOT, 'data', 'machines.json'), encoding='utf-8'))
    G = json.load(open(os.path.join(ROOT, 'data', 'graph.json'), encoding='utf-8'))
    node = {n['id']: n for n in G['nodes']}
    layers = {str(l['n']): l for l in G['layers']}
    paths = {p['id']: p for p in G['paths']}
    ms = []
    for m in M['machines']:
        p = m.get('profile', {})
        x = dict(m)
        x['sc'] = status_class(m['status']); x['year'] = year_of(m['status_date'])
        x['flags'] = set(p.get('flags', []))
        x['device'] = x['sc'] in ('DEPLOYED', 'DEMONSTRATED', 'RETIRED') and not (x['flags'] & NON_DEVICE_FLAGS)
        x['q'] = m.get('physical_qubits_num')
        x['cc'] = control_class(p.get('control_placement')); x['cryo'] = cryo_integrated(p.get('control_placement'))
        x['dc'] = decoding_class(p.get('realtime'))
        x['err'] = p.get('err_2q_median_num')
        x['has_code'] = bool(m.get('codes'))
        prim9 = [c for c in m['layers'].get('9', []) if c['role'] == 'primary']
        x['link'] = bool(prim9) and not prim9[0]['gap']
        x['cloud'] = 'cloud' in (m.get('access') or '').lower()
        x['gatedev'] = x['device'] and not (x['flags'] & NON_GATE_FLAGS)
        ms.append(x)
    return M, G, node, layers, paths, ms


def sec_machines(lang):
    L = lang; en = (lang == 'en')
    M, G, NODE, LAYERS, PATHS, MS = prep()
    o = []
    def H(s): o.append(s + "\n\n")
    def nm(n): return NODE[n][L] if n in NODE else n
    N = len(MS); dev = [m for m in MS if m['device']]
    byfam = {f: [m for m in MS if m['family'] == f] for f in FAM_ORDER}
    src = M.get('source', {})

    # ---------- 8.1 the population
    H("## 8. " + (f"Quantum machines — {N} attempts, {len(PATHS)} architectures, and where they are going" if en else f"Квантовые машины — {N} попыток, {len(PATHS)} архитектур, и куда они идут"))
    o.append((f"The map's stations are what *can* be built; the machines register says what *has been* built, announced or planned, one row per machine, each joined to the map as a path instance (§7.12). This chapter reads the register as a population: how large it is, which stations it is built from, what idea justifies each attempt, and what the population's trends say about where the architecture is heading. Every count below is computed by the build from `data/machines.json` ({src.get('register','')}; evidence {src.get('evidence','')}); a claim is tested against the register, not asserted, and its evidence grade is carried along — the share of the cells behind it that a document was seen to support (✅) rather than a press page or an inference (🔎).\n\n" if en else
              f"Станции карты — это то, что *может* быть построено; реестр машин говорит, что *построено*, анонсировано или запланировано: по строке на машину, каждая соединена с картой как экземпляр пути (§7.12). Эта глава читает реестр как популяцию: насколько она велика, из каких станций собрана, какая идея оправдывает каждую попытку и что тренды популяции говорят о том, куда движется архитектура. Каждое число ниже вычислено сборкой из `data/machines.json` ({src.get('register','')}; свидетельства {src.get('evidence','')}); утверждение проверяется по реестру, а не постулируется, и его класс свидетельств указан рядом — доля ячеек за ним, для которых видели подтверждающий документ (✅), а не пресс-релиз или вывод (🔎).\n\n"))
    ncells = sum(m['evidence_counts']['total'] for m in MS)
    o.append((f"**Terms used in this chapter.** A *machine* is one row of the register: a named system an organisation has built, announced or planned. Its *family* is its qubit platform ({', '.join(t(L, FAMN[f]) for f in FAM_ORDER)}); its *architecture* is the map path it instantiates — one of the {len(PATHS)} paths of §7.3, i.e. the family plus the choice of encoding, gate and control that defines it (cat qubits and dual-rail erasure are architectures of the superconducting family). A *station* is a technology on the map (a node of the graph); an *evidence cell* is one machine × one layer of the stack — the station the machine uses there, with the document that shows it — so a machine has about a dozen cells and the register holds {ncells:,}. A cell is *documented* (✅) when a paper, whitepaper or figure was seen to show that station in that machine, and *press-level* (🔎) when only a press page or an inference supports it; the *evidence grade* of a count is the documented share of the cells it rests on — it says how much of a claim would survive if press claims were struck. A *device* is a machine whose status is deployed, demonstrated or retired and that is not flagged as a target or a component; a *gate-capable* device additionally runs an entangling gate (analog simulators, tweezer arrays without a gate and single-qubit testbeds are devices but not processors). A *cohort* is the year of the register's status date. *Integrated control* means the qubits are driven by electronics on the chip or inside the cryostat (on-chip microwave electrodes, cryo-CMOS, SFQ, flux DACs) rather than by room-temperature racks or free-space optics; *closed-loop decoding* means the error-correction decoder acts within the cycle. A *link station* is a non-gap entry in the interconnect layer — a demonstrated way of joining modules. A *roadmap verdict* is the register's feasibility check of a published roadmap against its target algorithm (FEASIBLE, SHORT with a deficit, or NOT EVALUABLE).\n\n" if en else
              f"**Термины этой главы.** *Машина* — одна строка реестра: именованная система, которую организация построила, анонсировала или запланировала. Её *семейство* — кубитная платформа ({', '.join(t(L, FAMN[f]) for f in FAM_ORDER)}); её *архитектура* — путь карты, который она реализует: один из {len(PATHS)} путей §7.3, то есть семейство плюс выбор кодирования, гейта и управления, который его определяет (кошачьи кубиты и двухрельсовое стирание — архитектуры сверхпроводникового семейства). *Станция* — технология на карте (узел графа); *ячейка свидетельств* — одна машина × один слой стека: станция, которую машина там использует, вместе с документом, который это показывает; у машины около дюжины ячеек, в реестре их {ncells:,}. Ячейка *документирована* (✅), когда статья, whitepaper или рисунок были увидены показывающими эту станцию в этой машине, и *на уровне прессы* (🔎), когда её поддерживает только пресс-страница или вывод; *класс свидетельств* числа — документированная доля ячеек, на которых оно стоит: он говорит, какая часть утверждения уцелеет, если вычеркнуть заявления прессы. *Устройство* — машина со статусом «в эксплуатации», «продемонстрирована» или «выведена», не помеченная как цель или компонент; устройство *с гейтами* вдобавок выполняет перепутывающий гейт (аналоговые симуляторы, массивы пинцетов без гейта и однокубитные стенды — устройства, но не процессоры). *Когорта* — год даты статуса в реестре. *Интегрированное управление* — кубиты управляются электроникой на чипе или внутри криостата (микроволновые электроды на чипе, cryo-CMOS, SFQ, потоковые ЦАП), а не стойками при комнатной температуре или оптикой в свободном пространстве; *замкнутое декодирование* — декодер коррекции ошибок действует внутри такта. *Станция связи* — непустая запись в слое межсоединений: продемонстрированный способ соединить модули. *Вердикт дорожной карты* — проверка реестром опубликованной карты на осуществимость её целевого алгоритма (FEASIBLE, SHORT с дефицитом или NOT EVALUABLE).\n\n"))
    H("### 8.1 " + ("The population" if en else "Популяция"))
    nsc = {s: sum(1 for m in MS if m['sc'] == s) for s in STAT_ORDER}
    ncloud = sum(1 for m in MS if m['cloud']); nlab = sum(1 for m in MS if 'lab' in (m.get('access') or '').lower() or 'research' in (m.get('access') or '').lower())
    nprem = sum(1 for m in MS if 'on-prem' in (m.get('access') or '').lower() or 'sold' in (m.get('access') or '').lower())
    ctry = {}
    for m in MS: ctry[m['country']] = ctry.get(m['country'], 0) + 1
    topc = sorted(ctry.items(), key=lambda kv: (-kv[1], kv[0]))[:6]
    yrs = {}
    for m in MS:
        if m['year']: yrs[m['year']] = yrs.get(m['year'], 0) + 1
    o.append((f"**{N} machines, {len(FAM_ORDER)} families, {len(PATHS)} paths.** {len(dev)} are devices — {nsc['DEPLOYED']} deployed, {nsc['DEMONSTRATED']} demonstrated, {nsc['RETIRED']} retired, less the rows flagged as a target or a component — and {N-len(dev)} are announcements, plans or targets. Access: {ncloud} reachable through a cloud service, {nprem} sold on-premises, {nlab} laboratory-only. By country of the operating organisation: " + ', '.join(f"{c} {n}" for c, n in topc) + f". By cohort (the year of the status date): " + ', '.join(f"{y} — {n}" for y, n in sorted(yrs.items())) + ".\n\n" if en else
              f"**{N} машин, {len(FAM_ORDER)} семейств, {len(PATHS)} путей.** {len(dev)} — устройства ({nsc['DEPLOYED']} в эксплуатации, {nsc['DEMONSTRATED']} продемонстрированы, {nsc['RETIRED']} выведены, за вычетом строк, помеченных как цель или компонент), {N-len(dev)} — анонсы, планы или цели. Доступ: {ncloud} доступны через облачный сервис, {nprem} проданы на площадку заказчика, {nlab} только в лаборатории. По стране организации-оператора: " + ', '.join(f"{c} {n}" for c, n in topc) + f". По когортам (год даты статуса): " + ', '.join(f"{y} — {n}" for y, n in sorted(yrs.items())) + ".\n\n"))
    H("**" + ("Table 8.1 — families × status (machines); devices; cloud access; evidence cells and how many of them are documented" if en else "Таблица 8.1 — семейства × статус (машин); устройства; облачный доступ; ячейки свидетельств и сколько из них документировано") + "**")
    hdr = ("| Family | Machines | Deployed | Demonstrated | Announced | Planned | Retired | Other | Devices | Cloud access | Evidence cells | Documented cells (✅) | Documented, % |" if en else
           "| Семейство | Машин | В эксплуатации | Продемонстрированы | Анонсированы | Запланированы | Выведены | Прочее | Устройства | Облачный доступ | Ячеек свидетельств | Документировано (✅) | Документировано, % |")
    o.append(hdr + "\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    for f in FAM_ORDER:
        fm = byfam[f]
        if not fm: continue
        v = sum(m['evidence_counts']['verified'] for m in fm); a = sum(m['evidence_counts']['total'] for m in fm)
        c = {s: sum(1 for m in fm if m['sc'] == s) for s in STAT_ORDER}
        o.append(f"| {t(L, FAMN[f])} | {len(fm)} | {c['DEPLOYED']} | {c['DEMONSTRATED']} | {c['ANNOUNCED']} | {c['PLANNED']} | {c['RETIRED']} | {c['OTHER']} | {sum(1 for m in fm if m['device'])} | {sum(1 for m in fm if m['cloud'])} | {a} | {v} | {pct(v, a)} |\n")
    vt = sum(m['evidence_counts']['verified'] for m in MS); at = sum(m['evidence_counts']['total'] for m in MS)
    o.append(f"| **{'all' if en else 'все'}** | {N} | {nsc['DEPLOYED']} | {nsc['DEMONSTRATED']} | {nsc['ANNOUNCED']} | {nsc['PLANNED']} | {nsc['RETIRED']} | {nsc['OTHER']} | {len(dev)} | {ncloud} | {at} | {vt} | {pct(vt, at)} |\n\n")
    o.append((f"Reading the table: the superconducting family is the largest by far and also the only one with retirements; the photonic and spin families are small and mostly at the demonstration stage; the {nsc['OTHER']} rows in *other* are statuses the register could not reduce to one word (component testbeds, disputed reachability). The last three columns are the chapter's evidence grade: of the evidence cells behind a family's rows, how many a document was seen to support. It matters because every count in this chapter inherits it — a family at 30 % rests mostly on press claims and inferences, a family at 57 % mostly on papers — and it differs by family because the families publish differently: architecture papers with device figures are the norm for the academic superconducting, ion and atom machines and the exception for commercial photonic and spin announcements.\n\n" if en else
              f"Чтение таблицы: сверхпроводниковое семейство — самое большое и единственное с выведенными машинами; фотонное и спиновое семейства малы и в основном на стадии демонстрации; {nsc['OTHER']} строк *прочее* — статусы, которые реестр не свёл к одному слову (испытательные стенды компонентов, спорная достижимость). Последние три столбца — класс свидетельств главы: сколько из ячеек свидетельств за строками семейства подтверждены увиденным документом. Это важно, потому что каждое число главы его наследует — семейство на 30 % стоит в основном на заявлениях прессы и выводах, семейство на 57 % — в основном на статьях, — и он различается по семействам, потому что семейства публикуют по-разному: статьи об архитектуре с рисунками устройства — норма для академических сверхпроводниковых, ионных и атомных машин и исключение для коммерческих фотонных и спиновых анонсов.\n\n"))

    # ---------- 8.2 what they are built from
    H("### 8.2 " + ("What the machines are built from" if en else "Из чего собраны машины"))
    o.append(("Per layer of the map, the stations the machines actually occupy (primary role), the share of machines whose primary cell is a gap — the map has no station for what the machine runs, or the machine discloses nothing — and the families that share the most-used station. The gap share is the register's disclosure profile: near zero for the carrier, small for gates, connectivity and fabrication, and large for exactly the layers where the field's claims run ahead of its machines — code, decoder, interconnect.\n\n" if en else
              "По слоям карты: станции, которые машины реально занимают (основная роль), доля машин, у которых основная ячейка — пробел (на карте нет станции для того, что запускает машина, или машина ничего не раскрывает), и семейства, делящие самую занятую станцию. Доля пробелов — профиль раскрытия реестра: около нуля для носителя, мала для гейтов, связности и изготовления и велика ровно на тех слоях, где заявления отрасли опережают её машины: код, декодер, межсоединение.\n\n"))
    H("**" + ("Table 8.2 — layers: gap share and the most-used stations" if en else "Таблица 8.2 — слои: доля пробелов и самые занятые станции") + "**")
    o.append(("| Layer | Machines with a gap | Gap share | Most-used stations (machines) | Families on the first |" if en else
              "| Слой | Машин с пробелом | Доля пробелов | Самые занятые станции (машин) | Семейств на первой |") + "\n|---|---|---|---|---|\n")
    gapshare = {}
    for ln in sorted(LAYERS, key=int):
        l = LAYERS[ln]; prim = {}; gaps = 0; fam_of = {}
        for m in MS:
            for c in m['layers'].get(ln, []):
                if c['role'] != 'primary': continue
                if c['gap']: gaps += 1; continue
                prim[c['node']] = prim.get(c['node'], 0) + 1
                fam_of.setdefault(c['node'], set()).add(m['family'])
        top = sorted(prim.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
        gapshare[ln] = (gaps, N)
        first = top[0][0] if top else None
        fams = ', '.join(t(L, FAMN[f]) for f in FAM_ORDER if first and f in fam_of.get(first, ())) if first else '—'
        o.append(f"| {l['n']} {t(L, (l['en'], l['ru']))} | {gaps} | {pct(gaps, N)} | " + ('; '.join(f"{nm(k)} `{k}` ({v})" for k, v in top) or '—') + f" | {fams} |\n")
    o.append("\n")

    # ---------- 8.3 the idea behind each attempt
    H("### 8.3 " + ("The idea behind each architecture" if en else "Идея, стоящая за каждой архитектурой"))
    o.append(("A machine is an argument: *this* combination of stations will reach the goal before the others. The argument is made per architecture (a path of the map), not per machine, so the register is read here by path — the bet in one line, the count of machines and devices that make it, the largest gate-capable device the register holds for it (analog simulators, arrays without an entangling gate and single-qubit testbeds excluded), and the best two-qubit error among its devices (hero pairs, targets and component demonstrations excluded).\n\n" if en else
              "Машина — это аргумент: *эта* комбинация станций достигнет цели раньше других. Аргумент делается на уровне архитектуры (пути карты), а не машины, поэтому реестр читается здесь по путям: ставка в одну строку, число машин и устройств, её делающих, крупнейшее устройство с гейтами, которое реестр держит для неё (аналоговые симуляторы, массивы без перепутывающего гейта и однокубитные стенды исключены), и лучшая двухкубитная ошибка среди её устройств (рекордные пары, цели и демонстрации компонентов исключены).\n\n"))
    BET = {
        'sc': ("fast microwave gates on a lithographic lattice; scale by fabrication and, later, by links between chips", "быстрые микроволновые гейты на литографической решётке; масштаб за счёт изготовления и, позже, связей между чипами"),
        'cat': ("bias the noise so that one error type dominates, then correct only that type with a cheap code", "сместить шум так, чтобы доминировал один тип ошибок, и исправлять только его дешёвым кодом"),
        'dualrail': ("turn photon loss into a flagged erasure; erasures cost far fewer qubits to correct than Pauli errors", "превратить потерю фотона в помеченное стирание; стирания исправляются много дешевле паулиевских ошибок"),
        'ion_qccd': ("move the ions, not the information: transport gives all-to-all connectivity at the highest gate fidelities", "перемещать ионы, а не информацию: транспорт даёт связность «все со всеми» при наивысшей точности гейтов"),
        'ion_elec': ("static chains with electronic or integrated control; scale by photonic links between modules", "статические цепочки с электронным или интегрированным управлением; масштаб через фотонные связи между модулями"),
        'atom_rb': ("reconfigurable tweezers make the code geometry programmable and the qubit count cheap; the clock is slow", "перестраиваемые пинцеты делают геометрию кода программируемой, а число кубитов дешёвым; такт медленный"),
        'atom_ae': ("alkaline-earth atoms add erasure conversion and continuous reloading to the tweezer bet", "щёлочноземельные атомы добавляют к ставке на пинцеты преобразование в стирания и непрерывную перезагрузку"),
        'ph_fusion': ("make entanglement by measurement: room-temperature photonic fabrication and networking, loss is the enemy", "создавать перепутывание измерением: фотонное изготовление и сети при комнатной температуре; враг — потери"),
        'ph_cv': ("continuous-variable states and GKP encoding on the same photonic chips", "состояния непрерывных переменных и кодирование GKP на тех же фотонных чипах"),
        'spin_qd': ("the foundry: quantum dots in CMOS, density and cold electronics from the semiconductor industry", "фабрика: квантовые точки в CMOS, плотность и холодная электроника из полупроводниковой отрасли"),
        'spin_donor': ("donor spins in isotopically pure silicon: the longest coherence in a solid", "донорные спины в изотопно чистом кремнии: самая долгая когерентность в твёрдом теле"),
        'defect': ("defect spins that work at room temperature and network through photons", "дефектные спины, работающие при комнатной температуре и связанные через фотоны"),
        'topo': ("protection in the hardware: a topological gap instead of a code", "защита в самом устройстве: топологическая щель вместо кода"),
        'anneal': ("special-purpose scale now: thousands of analog qubits for optimisation and simulation", "специализированный масштаб сейчас: тысячи аналоговых кубитов для оптимизации и симуляции"),
    }
    H("**" + ("Table 8.3 — paths: the bet, the population, the best numbers" if en else "Таблица 8.3 — пути: ставка, популяция, лучшие числа") + "**")
    o.append(("| Architecture (map path) | Machines | Devices | Largest gate-capable device (physical qubits) | Best 2Q error among devices | The bet |" if en else
              "| Архитектура (путь карты) | Машин | Устройств | Крупнейшее устройство с гейтами (физ. кубитов) | Лучшая 2Q-ошибка среди устройств | Ставка |") + "\n|---|---|---|---|---|---|\n")
    for pid in [p['id'] for p in G['paths']]:
        pm = [m for m in MS if m['map_path'] == pid]
        if not pm: continue
        pd = [m for m in pm if m['device']]
        big = max([m for m in pd if m['q'] and m['gatedev']], key=lambda m: (m['q'], m['name']), default=None)
        errs = sorted([(m['err'], m['name']) for m in pd if m['err'] is not None and not (m['flags'] & EXCL_ERR_FLAGS)])
        o.append(f"| {PATHS[pid][L]} `{pid}` | {len(pm)} | {len(pd)} | " + (f"{mdcell(big['name'])} — {fmt_n(big['q'])}" if big else '—') + " | " + (f"{fmt_e(errs[0][0])} ({mdcell(errs[0][1])})" if errs else '—') + f" | {mdcell(t(L, BET.get(pid, ('—', '—'))))} |\n")
    o.append("\n")
    o.append(("Two readings. First, the bets are not symmetric in what they need to prove: the superconducting and tweezer bets are already made by dozens of devices and argue about *rates* (error per gate, qubits per year); the bosonic, topological and donor bets are made by one to seven machines and still argue about *existence* (does the protection hold at the second qubit, at the second module). Second, the best numbers sit on different paths for different quantities — the largest device is a tweezer array, the best two-qubit error is an ion trap, the fastest clock (§7.4) is a transmon lattice — which is the empirical form of the map's claim that no path dominates on all axes.\n\n" if en else
              "Два прочтения. Во-первых, ставки несимметричны в том, что им нужно доказать: сверхпроводниковая и пинцетная ставки уже сделаны десятками устройств и спорят о *темпах* (ошибка на гейт, кубиты в год); бозонные, топологическая и донорная сделаны одной–семью машинами и всё ещё спорят о *существовании* (держится ли защита на втором кубите, на втором модуле). Во-вторых, лучшие числа лежат на разных путях для разных величин — крупнейшее устройство это массив пинцетов, лучшая двухкубитная ошибка — ионная ловушка, самый быстрый такт (§7.4) — трансмонная решётка, — что есть эмпирическая форма утверждения карты: ни один путь не доминирует по всем осям.\n\n"))

    # ---------- 8.4 hypotheses
    H("### 8.4 " + ("Trends — eight hypotheses tested on the register" if en else "Тренды — восемь гипотез, проверенных по реестру"))
    o.append(("Each hypothesis is a falsifiable statement about the population; the test is the computation named with it, run by the build on the register's current rows; the verdict is *supported*, *partly supported* or *not supported*, with the sample size. What each verdict rests on, and what would overturn it, is in §8.7.\n\n" if en else
              "Каждая гипотеза — фальсифицируемое утверждение о популяции; проверка — вычисление, названное рядом с ней и выполняемое сборкой по текущим строкам реестра; вердикт — *подтверждена*, *подтверждена частично* или *не подтверждена*, с размером выборки. На чём стоит каждый вердикт и что его опрокинуло бы — в §8.7.\n\n"))
    VER = {'yes': ('**supported**', '**подтверждена**'), 'part': ('**partly supported**', '**подтверждена частично**'), 'no': ('**not supported**', '**не подтверждена**')}
    verdicts = {}

    # H1 — count moved to atoms (all devices vs gate-capable devices)
    gdev = [m for m in dev if m['gatedev']]
    devq = {f: sorted([m['q'] for m in gdev if m['family'] == f and m['q']]) for f in FAM_ORDER}
    allq = {f: sorted([m['q'] for m in dev if m['family'] == f and m['q']]) for f in FAM_ORDER}
    med = {f: median(v) for f, v in devq.items()}; meda = {f: median(v) for f, v in allq.items()}
    bigg = {f: max([m for m in gdev if m['family'] == f and m['q']], key=lambda m: (m['q'], m['name']), default=None) for f in FAM_ORDER}
    biga = {f: max([m for m in dev if m['family'] == f and m['q']], key=lambda m: (m['q'], m['name']), default=None) for f in FAM_ORDER}
    coh = {}
    for f in ('SC', 'ATOM'):
        by = {}
        for m in gdev:
            if m['family'] == f and m['q'] and m['year']:
                y = min(max(m['year'], 2021), 2026); by.setdefault(y, []).append(m['q'])
        coh[f] = {y: (median(v), len(v)) for y, v in sorted(by.items())}
    r_all = (meda['ATOM'] / meda['SC']) if meda.get('ATOM') and meda.get('SC') else None
    r_gate = (med['ATOM'] / med['SC']) if med.get('ATOM') and med.get('SC') else None
    atom_top_gate = bigg.get('ATOM') and all((bigg[f]['q'] if bigg.get(f) else 0) <= bigg['ATOM']['q'] for f in ('SC', 'ION', 'PHOTON', 'SPIN'))
    h1 = 'yes' if r_gate and r_gate > 1 and atom_top_gate else ('part' if (r_gate and r_gate > 1) or atom_top_gate else 'no')
    verdicts['H1'] = h1
    H("**H1 — " + ("Physical qubit count has moved to the atoms; superconducting machines no longer compete on count." if en else "Число физических кубитов ушло к атомам; сверхпроводниковые машины больше не соперничают числом.") + "**")
    o.append((f"*Test.* Median physical qubits per family over all devices and over gate-capable devices ({len(gdev)} of {len(dev)}; analog simulators, arrays without an entangling gate and single-qubit testbeds excluded); the largest gate-capable device per family; cohort medians for the two largest families.\n\n" if en else
              f"*Проверка.* Медиана физических кубитов по семействам для всех устройств и для устройств с гейтами ({len(gdev)} из {len(dev)}; аналоговые симуляторы, массивы без перепутывающего гейта и однокубитные стенды исключены); крупнейшее устройство с гейтами по семействам; медианы по когортам для двух крупнейших семейств.\n\n"))
    o.append(("| Family | Devices: median qubits (n) | Gate-capable: median qubits (n) | Largest gate-capable device | Largest device of any kind |" if en else
              "| Семейство | Устройства: медиана кубитов (n) | С гейтами: медиана кубитов (n) | Крупнейшее устройство с гейтами | Крупнейшее устройство любого рода |") + "\n|---|---|---|---|---|\n")
    for f in ('ATOM', 'SC', 'ION', 'PHOTON', 'SPIN'):
        if not allq[f]: continue
        o.append(f"| {t(L, FAMN[f])} | {fmt_n(meda[f])} ({len(allq[f])}) | {fmt_n(med[f])} ({len(devq[f])}) | " + (f"{mdcell(bigg[f]['name'])} — {fmt_n(bigg[f]['q'])}" if bigg.get(f) else '—') + " | " + (f"{mdcell(biga[f]['name'])} — {fmt_n(biga[f]['q'])}" if biga.get(f) else '—') + " |\n")
    o.append("\n")
    o.append(((f"*Result.* The atoms lead by ×{r_all:.1f} on all devices and ×{r_gate:.1f} on gate-capable ones. " if r_all and r_gate else "*Result.* ") + "Cohort medians (gate-capable; n in brackets) — " + '; '.join(f"{t(L, FAMN[f])}: " + ', '.join(f"{y} {fmt_n(v[0])} ({v[1]})" for y, v in coh[f].items()) for f in ('SC', 'ATOM')) + f". *Verdict:* {t(L, VER[h1])}. The atoms' lead in count is real among processors and much larger among trap arrays: the thousands-of-qubits machines are arrays that do not yet run an entangling gate, while the largest gate-capable tweezer processor and the largest transmon lattice are within a factor of a few of each other. The cohort medians move with who enters the register in a given year (small first chips from new entrants) more than with the leaders, and are too thin per cohort to carry a trend on their own.\n\n" if en else
              ((f"*Результат.* Атомы впереди в ×{r_all:.1f} по всем устройствам и в ×{r_gate:.1f} по устройствам с гейтами. " if r_all and r_gate else "*Результат.* ") + "Медианы по когортам (с гейтами; n в скобках) — " + '; '.join(f"{t(L, FAMN[f])}: " + ', '.join(f"{y} {fmt_n(v[0])} ({v[1]})" for y, v in coh[f].items()) for f in ('SC', 'ATOM')) + f". *Вердикт:* {t(L, VER[h1])}. Лидерство атомов по числу реально среди процессоров и много больше среди массивов ловушек: машины на тысячи кубитов — это массивы, которые пока не выполняют перепутывающий гейт, тогда как крупнейший пинцетный процессор с гейтами и крупнейшая трансмонная решётка отличаются в считанные разы. Медианы когорт движутся вместе с тем, кто входит в реестр в данном году (малые первые чипы новых участников), а не с лидерами, и слишком тонки по когортам, чтобы нести тренд сами по себе.\n\n")))

    # H2 — 2Q error converges at the median; the best stays with ions
    errs = {f: sorted([(m['err'], m['name']) for m in dev if m['family'] == f and m['err'] is not None and not (m['flags'] & EXCL_ERR_FLAGS)]) for f in FAM_ORDER}
    emed = {f: median([e for e, _ in v]) for f, v in errs.items() if v}
    ebest = {f: v[0] for f, v in errs.items() if v}
    big3 = [f for f in ('SC', 'ION', 'ATOM') if f in emed]
    spread = (max(emed[f] for f in big3) / min(emed[f] for f in big3)) if big3 else None
    bestfam = min(ebest.items(), key=lambda kv: kv[1][0])[0] if ebest else None
    h2 = 'yes' if spread is not None and spread <= 2 and bestfam == 'ION' else ('part' if spread is not None and spread <= 3 else 'no')
    verdicts['H2'] = h2
    H("**H2 — " + ("Two-qubit error is converging across the three large families at the median, while the best single number stays with the ions." if en else "Двухкубитная ошибка сходится у трёх больших семейств по медиане, а лучшее единичное число остаётся у ионов.") + "**")
    o.append((f"*Test.* Median and best `err_2q_median` over devices per family, excluding hero-pair numbers, targets and component demonstrations. *Result.* " + '; '.join(f"{t(L, FAMN[f])} median {fmt_e(emed[f])}, best {fmt_e(ebest[f][0])} ({mdcell(ebest[f][1])}), n = {len(errs[f])}" for f in FAM_ORDER if f in emed) + f". The spread of the three large medians is ×{spread:.1f}. *Verdict:* {t(L, VER[h2])}. A convergence of medians with a persistent gap at the best is what one expects when the median is set by the many second-tier machines and the best by a few labs that have run the same platform for a decade.\n\n" if en else
              f"*Проверка.* Медиана и лучшее значение `err_2q_median` по устройствам каждого семейства, исключая рекордные пары, цели и демонстрации компонентов. *Результат.* " + '; '.join(f"{t(L, FAMN[f])}: медиана {fmt_e(emed[f])}, лучшее {fmt_e(ebest[f][0])} ({mdcell(ebest[f][1])}), n = {len(errs[f])}" for f in FAM_ORDER if f in emed) + f". Разброс трёх больших медиан — ×{spread:.1f}. *Вердикт:* {t(L, VER[h2])}. Сходимость медиан при сохраняющемся разрыве в лучших значениях — то, чего ждёшь, когда медиану задают многочисленные машины второго ряда, а лучшее — несколько лабораторий, десятилетие работающих на одной платформе.\n\n"))

    # H3 — control stays external
    integ = [m for m in MS if m['cc'] == 'integrated']; cryo = [m for m in MS if m['cryo']]
    cc_f = {f: sum(1 for m in integ if m['family'] == f) for f in FAM_ORDER}
    big_sc_cryo = [m for m in dev if m['family'] == 'SC' and m['cryo'] and (m['q'] or 0) >= 100 and 'demo' not in (m['profile'].get('control_placement') or '').lower()]
    ext = sum(1 for m in MS if m['cc'] in ('room', 'optics'))
    h3 = 'yes' if len(integ) <= N * 0.2 and not big_sc_cryo else ('part' if len(integ) <= N * 0.3 else 'no')
    verdicts['H3'] = h3
    H("**H3 — " + ("Control stays external: integrated control is a minority confined to spins, annealers and a few traps; no superconducting device of 100 qubits or more is driven from inside the cryostat." if en else "Управление остаётся внешним: интегрированное управление — меньшинство, ограниченное спинами, отжигом и несколькими ловушками; ни одно сверхпроводниковое устройство от 100 кубитов не управляется изнутри криостата.") + "**")
    o.append((f"*Test.* The register's `control_placement` classified as room-temperature electronics, optics, integrated (on-chip microwave, cryo-CMOS, SFQ, flux DACs, 4 K) or undisclosed; the integrated class by family; superconducting devices ≥ 100 qubits with cryogenic control that is not a demo. *Result.* External {ext} of {N}; integrated {len(integ)} (" + ', '.join(f"{t(L, FAMN[f])} {cc_f[f]}" for f in FAM_ORDER if cc_f[f]) + f"), of which cryogenic {len(cryo)}; superconducting devices ≥ 100 qubits with non-demo cryogenic control: {len(big_sc_cryo)}. *Verdict:* {t(L, VER[h3])}. The station the map calls the slow trend (§7.4: control placement) is slow in the register too: the integrated class is where the physics forces it — flux DACs on annealers, CMOS next to CMOS spins, microwave electrodes in surface traps — and a plan elsewhere.\n\n" if en else
              f"*Проверка.* Поле реестра `control_placement`, классифицированное как электроника при комнатной температуре, оптика, интегрированное (микроволны на чипе, cryo-CMOS, SFQ, потоковые ЦАП, 4 K) или не раскрыто; интегрированный класс по семействам; сверхпроводниковые устройства ≥ 100 кубитов с криогенным управлением не в статусе демонстрации. *Результат.* Внешнее {ext} из {N}; интегрированное {len(integ)} (" + ', '.join(f"{t(L, FAMN[f])} {cc_f[f]}" for f in FAM_ORDER if cc_f[f]) + f"), из них криогенное {len(cryo)}; сверхпроводниковых устройств ≥ 100 кубитов с криогенным управлением не в статусе демонстрации: {len(big_sc_cryo)}. *Вердикт:* {t(L, VER[h3])}. Тренд, который карта называет медленным (§7.4: размещение управления), медленен и в реестре: интегрированный класс есть там, где его вынуждает физика — потоковые ЦАП у отжига, CMOS рядом с CMOS-спинами, микроволновые электроды в поверхностных ловушках, — а в остальном это план.\n\n"))

    # H4 — QEC on hardware becomes the entry ticket
    codem = [m for m in MS if m['has_code']]
    cohc = {}
    for m in MS:
        if m['year'] and 2023 <= m['year'] <= 2026:
            a = cohc.setdefault(m['year'], [0, 0]); a[1] += 1; a[0] += m['has_code']
    inloop = [m for m in MS if m['dc'] == 'in-loop']
    shares = [c[0] / c[1] for y, c in sorted(cohc.items())]
    h4 = 'yes' if shares and all(b >= a for a, b in zip(shares, shares[1:])) and len(inloop) >= 10 else 'part'
    verdicts['H4'] = h4
    H("**H4 — " + ("Running a code on the hardware is becoming the entry ticket: the share of new machines that have done so rises by cohort, and closed-loop decoding follows." if en else "Запуск кода на железе становится входным билетом: доля новых машин, которые это сделали, растёт по когортам, и замкнутое декодирование следует за ней.") + "**")
    o.append((f"*Test.* Machines with at least one code in the register's code table, by cohort 2023–2026; machines whose decoding is in the loop. *Result.* {len(codem)} of {N} machines have run a code (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in codem if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in codem)) + "); share by cohort " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohc.items())) + f"; decoding in the loop: {len(inloop)} (" + ', '.join(mdcell(m['name']) for m in sorted(inloop, key=lambda m: m['name'])) + f"). *Verdict:* {t(L, VER[h4])}. The share rises but not monotonically, and the loop is closed on a handful of machines: the entry ticket is a code *demonstration*, not yet a decoder in the cycle.\n\n" if en else
              f"*Проверка.* Машины хотя бы с одним кодом в таблице кодов реестра, по когортам 2023–2026; машины, у которых декодирование замкнуто в цикле. *Результат.* {len(codem)} из {N} машин запускали код (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in codem if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in codem)) + "); доля по когортам " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohc.items())) + f"; декодирование в цикле: {len(inloop)} (" + ', '.join(mdcell(m['name']) for m in sorted(inloop, key=lambda m: m['name'])) + f"). *Вердикт:* {t(L, VER[h4])}. Доля растёт, но не монотонно, и цикл замкнут на считанных машинах: входной билет — *демонстрация* кода, а не декодер в такте.\n\n"))

    # H5 — modularity is a roadmap, not a machine
    g9 = gapshare.get('9', (0, N)); linked = [m for m in MS if m['link']]
    worst = max(gapshare.items(), key=lambda kv: kv[1][0])[0]
    h5 = 'yes' if worst == '9' and g9[0] >= 0.75 * N else ('part' if g9[0] >= 0.5 * N else 'no')
    verdicts['H5'] = h5
    H("**H5 — " + ("Modularity is a roadmap, not a machine: the interconnect layer is the least populated layer of the register." if en else "Модульность — это дорожная карта, а не машина: слой межсоединений — наименее заполненный слой реестра.") + "**")
    o.append((f"*Test.* Gap share per layer (Table 8.2); machines whose primary interconnect cell is a map station. *Result.* Interconnect gap {g9[0]} of {N} ({pct(g9[0], N)}), the largest of the ten layers; {len(linked)} machines carry a link station (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in linked if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in linked)) + f"). *Verdict:* {t(L, VER[h5])}. Every roadmap that reaches thousands of qubits assumes a link between modules; the register holds a link on {len(linked)} machines, most of them ion or photonic testbeds. The layer where the architecture must go is the layer where it has least been.\n\n" if en else
              f"*Проверка.* Доля пробелов по слоям (таблица 8.2); машины, у которых основная ячейка межсоединения — станция карты. *Результат.* Пробел межсоединения у {g9[0]} из {N} ({pct(g9[0], N)}) — наибольший из десяти слоёв; станцию связи несут {len(linked)} машин (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in linked if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in linked)) + f"). *Вердикт:* {t(L, VER[h5])}. Каждая дорожная карта, доходящая до тысяч кубитов, предполагает связь между модулями; реестр держит связь на {len(linked)} машинах, в основном ионных и фотонных стендах. Слой, куда архитектура должна прийти, — слой, где её меньше всего было.\n\n"))

    # H6 — roadmaps fail on the error budget
    R = M.get('roadmaps', [])
    rv = {}
    for r in R: rv[r['verdict']] = rv.get(r['verdict'], 0) + 1
    short = [r for r in R if r['verdict'] == 'SHORT']
    errd = sum(1 for r in short if ('err' in r['deficit'] or 'gate' in r['deficit']))
    qonly = sum(1 for r in short if re.fullmatch(r'x[\d\.,e\-]+ q', r['deficit'].strip()))
    nroad = len({r['roadmap_id'] for r in R})
    h6 = 'yes' if short and errd >= 0.7 * len(short) else ('part' if short and errd >= 0.5 * len(short) else 'no')
    verdicts['H6'] = h6
    H("**H6 — " + ("Roadmaps fall short on the error budget, not on the qubit count." if en else "Дорожные карты не дотягивают по бюджету ошибок, а не по числу кубитов.") + "**")
    o.append((f"*Test.* The register's roadmap-feasibility table ({nroad} roadmaps × the target algorithms): verdicts, and among the SHORT verdicts the deficit's nature. *Result.* " + ', '.join(f"{k} {v}" for k, v in sorted(rv.items())) + f"; of the {len(short)} SHORT verdicts {errd} carry an error or gate-budget deficit and {qonly} a qubit-only deficit. *Verdict:* {t(L, VER[h6])}. Qubit counts are the roadmaps' own currency and they budget it generously; the logical error per operation and the gate count of the target algorithm are where the same roadmaps miss by one to six orders of magnitude.\n\n" if en else
              f"*Проверка.* Таблица осуществимости дорожных карт реестра ({nroad} карт × целевые алгоритмы): вердикты и, среди вердиктов SHORT, природа дефицита. *Результат.* " + ', '.join(f"{k} {v}" for k, v in sorted(rv.items())) + f"; из {len(short)} вердиктов SHORT {errd} несут дефицит по ошибке или бюджету гейтов и {qonly} — только по кубитам. *Вердикт:* {t(L, VER[h6])}. Число кубитов — собственная валюта дорожных карт, и её они закладывают щедро; логическая ошибка на операцию и число гейтов целевого алгоритма — то, где те же карты промахиваются на один–шесть порядков.\n\n"))

    # H7 — the announcement gap widens
    cohs = {}
    for m in MS:
        if m['year'] and 2023 <= m['year'] <= 2026:
            a = cohs.setdefault(m['year'], [0, 0]); a[1] += 1; a[0] += (m['sc'] in ('ANNOUNCED', 'PLANNED'))
    retf = {f: sum(1 for m in MS if m['sc'] == 'RETIRED' and m['family'] == f) for f in FAM_ORDER}
    sh = [c[0] / c[1] for y, c in sorted(cohs.items())]
    h7 = 'yes' if len(sh) >= 2 and sh[-1] > 2 * (sum(sh[:-1]) / len(sh[:-1])) else ('part' if len(sh) >= 2 and sh[-1] > sh[-2] else 'no')
    verdicts['H7'] = h7
    H("**H7 — " + ("The announcement gap widens: the newest cohort is increasingly announcements and plans rather than devices." if en else "Разрыв анонсов растёт: новейшая когорта всё больше состоит из анонсов и планов, а не устройств.") + "**")
    o.append((f"*Test.* Share of announced or planned rows per cohort 2023–2026; retirements by family. *Result.* " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohs.items())) + "; retired: " + ', '.join(f"{t(L, FAMN[f])} {retf[f]}" for f in FAM_ORDER if retf[f]) + f". *Verdict:* {t(L, VER[h7])} — with the caveat that the newest cohort is a partial year and some of its announcements will become devices; the shape to watch is whether the share falls back as the year closes.\n\n" if en else
              f"*Проверка.* Доля анонсированных или запланированных строк по когортам 2023–2026; выведенные машины по семействам. *Результат.* " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohs.items())) + "; выведены: " + ', '.join(f"{t(L, FAMN[f])} {retf[f]}" for f in FAM_ORDER if retf[f]) + f". *Вердикт:* {t(L, VER[h7])} — с оговоркой, что новейшая когорта — неполный год и часть её анонсов станет устройствами; следить надо за тем, упадёт ли доля к концу года.\n\n"))

    # H8 — ideas converge across families (station sharing)
    fam_by_node = {}
    for m in MS:
        for ln, cells in m['layers'].items():
            for c in cells:
                if c['gap'] or c['role'] != 'primary': continue
                fam_by_node.setdefault(c['node'], set()).add(m['family'])
    n_nodes = len(fam_by_node); n2 = sum(1 for v in fam_by_node.values() if len(v) >= 2); n3 = sum(1 for v in fam_by_node.values() if len(v) >= 3)
    shared3 = sorted([k for k, v in fam_by_node.items() if len(v) >= 3], key=lambda k: (-len(fam_by_node[k]), k))
    h8 = 'yes' if n2 >= 0.5 * n_nodes else ('part' if n2 >= 0.35 * n_nodes else 'no')
    verdicts['H8'] = h8
    H("**H8 — " + ("The families' ideas converge: a growing set of stations is shared across families." if en else "Идеи семейств сходятся: растущее множество станций делится между семействами.") + "**")
    o.append((f"*Test.* Stations occupied in the primary role, counted by the number of families that occupy them. *Result.* {n_nodes} stations occupied; {n2} by two families or more, {n3} by three or more (" + ', '.join(f"{nm(k)} `{k}` — {len(fam_by_node[k])}" for k in shared3) + f"). *Verdict:* {t(L, VER[h8])}. The families keep their own toolboxes; what they share is a *role* — mid-circuit readout, erasure conversion, a link between modules — filled by a different station on each path. Convergence, where it exists, is at the level of the map's coordinates (§7), not of its stations.\n\n" if en else
              f"*Проверка.* Станции, занятые в основной роли, посчитанные по числу занимающих их семейств. *Результат.* Занято {n_nodes} станций; {n2} — двумя семействами и более, {n3} — тремя и более (" + ', '.join(f"{nm(k)} `{k}` — {len(fam_by_node[k])}" for k in shared3) + f"). *Вердикт:* {t(L, VER[h8])}. Семейства держат собственные наборы инструментов; общей у них оказывается *роль* — считывание в середине схемы, преобразование в стирания, связь между модулями, — которую на каждом пути заполняет своя станция. Сходимость, где она есть, лежит на уровне координат карты (§7), а не её станций.\n\n"))

    # ---------- 8.5 forecasts (a ledger the next edition scores)
    H("### 8.5 " + ("Forecasts — what the register predicts, and how the next edition will score them" if en else "Прогнозы — что предсказывает реестр и как их оценит следующее издание"))
    def frontier(f, pool):
        fr = {}
        for m in pool:
            if m['family'] == f and m['q'] and m['year']: fr[m['year']] = max(fr.get(m['year'], 0), m['q'])
        run = 0; out = []
        for y in sorted(fr):
            run = max(run, fr[y]); out.append((y, run))
        return out
    def flat_since(series):
        if not series: return None
        top = series[-1][1]
        for y, v in series:
            if v == top: return y
        return None
    def rate(series):
        pts = [(y, v) for y, v in series]
        if len(pts) < 2 or pts[0][1] <= 0 or pts[-1][0] == pts[0][0]: return None
        return (pts[-1][1] / pts[0][1]) ** (1.0 / (pts[-1][0] - pts[0][0]))
    fr = {f: frontier(f, gdev) for f in ('SC', 'ION', 'ATOM')}
    ann = {f: sorted([(m['year'], m['q'], m['name']) for m in MS if m['family'] == f and not m['device'] and m['q'] and m['year'] and m['year'] <= 2028 and m['q'] > (fr[f][-1][1] if fr[f] else 0)]) for f in ('SC', 'ION', 'ATOM')}
    ion_rate = rate(fr['ION'])
    ion_2027 = fr['ION'][-1][1] * (ion_rate ** (2027 - fr['ION'][-1][0])) if ion_rate and fr['ION'] else None
    ion_lo = int(ion_2027 // 10 * 10) if ion_2027 else None; ion_hi = max([q for y, q, n in ann['ION']] + [ion_lo or 0])
    # error frontier and the median's lag behind it
    efr = {}
    for f in ('SC', 'ION', 'ATOM'):
        d = {}
        for m in dev:
            if m['family'] == f and m['err'] is not None and m['year'] and not (m['flags'] & EXCL_ERR_FLAGS): d[m['year']] = min(d.get(m['year'], 1.0), m['err'])
        run = 1.0; out = []
        for y in sorted(d):
            run = min(run, d[y]); out.append((y, run))
        efr[f] = out
    def erate(series):
        if len(series) < 2 or series[-1][0] == series[0][0]: return None
        return (series[0][1] / series[-1][1]) ** (1.0 / (series[-1][0] - series[0][0]))   # improvement factor per year
    def lag(f):
        med = emed.get(f)
        if med is None: return None
        for y, v in efr[f]:
            if v <= med: return 2026 - y
        return None
    # QEC adoption, closed-loop decoding, links, control
    cum = {}; c = 0
    for y in range(2019, 2027):
        c += sum(1 for m in MS if m['has_code'] and m['year'] == y); cum[y] = c
    planned_rt = [m for m in MS if m['dc'] == 'planned']
    link_dev = [m for m in MS if m['link'] and m['device']]; link_ann = sorted([m for m in MS if m['link'] and not m['device']], key=lambda m: (m['year'] or 9999, m['name']))
    ctl_cand = [m for m in MS if re.search(r'plan|claim|demo|intend', m['profile'].get('control_placement') or '', re.I)]
    due = sorted({(r['roadmap_id'], r['year']) for r in R if re.search(r'20(2[5-8])', r['year'] or '') and int(re.search(r'20(2[5-8])', r['year']).group(0)) <= 2028})
    yr = lambda f: fr[f][-1][0] if fr[f] else None
    o.append((f"A hypothesis says what the register shows; a forecast predicts what the next register will show. Each forecast below names its indicator, its value today, the value expected at the next two editions (2027.09 and 2028.09), the basis — the historical series, the register's own announcements, or both — and a confidence; the build writes the same rows to `data/forecast-ledger.json`, and the edition that reaches the date prints the outcome next to the forecast. Two limits govern the confidence: the series are short (five to eight yearly points) and dated by press releases, so the forecasts are directional with ranges rather than point estimates; and announcements are discounted — the register's three named rows that missed their date ({', '.join(mdcell(m['name']) for m in MS if re.search(r'never|not delivered', m['status'], re.I))}) are the reminder that an announced machine is a forecast, not a device.\n\n" if en else
              f"Гипотеза говорит, что показывает реестр; прогноз предсказывает, что покажет следующий реестр. Каждый прогноз ниже называет свой индикатор, его значение сегодня, ожидаемое значение к двум следующим изданиям (2027.09 и 2028.09), основание — историческую серию, собственные анонсы реестра или и то и другое — и уверенность; сборка записывает те же строки в `data/forecast-ledger.json`, и издание, дошедшее до даты, печатает итог рядом с прогнозом. Уверенность ограничивают две вещи: серии коротки (пять–восемь годовых точек) и датированы пресс-релизами, так что прогнозы направленные, с диапазонами, а не точечные; и анонсы дисконтированы — три именованные строки реестра, пропустившие свою дату ({', '.join(mdcell(m['name']) for m in MS if re.search(r'never|not delivered', m['status'], re.I))}), напоминают, что анонсированная машина — это прогноз, а не устройство.\n\n"))
    def fseries(f): return ', '.join(f"{y} {fmt_n(v)}" for y, v in fr[f])
    def aseries(f): return '; '.join(f"{mdcell(n)} — {fmt_n(q)} ({y})" for y, q, n in ann[f]) or '—'
    def eseries(f): return ', '.join(f"{y} {fmt_e(v)}" for y, v in efr[f])
    CONF = {'high': ('high', 'высокая'), 'medium': ('medium', 'средняя'), 'low': ('low', 'низкая')}
    ledger = []
    def F(fid, ind, now, f27, f28, basis, conf, falsif):
        ledger.append({'id': fid, 'indicator': ind, 'now': now, 'e2027': f27, 'e2028': f28, 'basis': basis, 'confidence': conf, 'falsified_if': falsif})
    # F1 — count frontiers
    sc_top = fr['SC'][-1][1] if fr['SC'] else None; at_top = fr['ATOM'][-1][1] if fr['ATOM'] else None; io_top = fr['ION'][-1][1] if fr['ION'] else None
    F('F1a', t(L, ('largest gate-capable superconducting device (physical qubits)', 'крупнейшее сверхпроводниковое устройство с гейтами (физ. кубитов)')),
      f"{fmt_n(sc_top)} ({t(L, ('flat since', 'без изменений с'))} {flat_since(fr['SC'])})",
      t(L, (f"≤ 1,121 (no gate-capable device above {fmt_n(sc_top)} delivered)", f"≤ 1 121 (устройство с гейтами крупнее {fmt_n(sc_top)} не поставлено)")),
      t(L, ("≤ 1,500; the first multi-module lattice (Kookaburra-class) is the only route above it", "≤ 1 500; единственный путь выше — первая многомодульная решётка класса Kookaburra")),
      t(L, (f"frontier series {fseries('SC')}; announced above the frontier: {aseries('SC')}", f"серия фронта {fseries('SC')}; анонсировано выше фронта: {aseries('SC')}")), 'high',
      t(L, ("a superconducting device with an entangling gate on more than 1,121 qubits in the 2027.09 register", "сверхпроводниковое устройство с перепутывающим гейтом более чем на 1 121 кубит в реестре 2027.09")))
    F('F1b', t(L, ('largest gate-capable neutral-atom device', 'крупнейшее нейтрально-атомное устройство с гейтами')),
      f"{fmt_n(at_top)} ({t(L, ('flat since', 'без изменений с'))} {flat_since(fr['ATOM'])})",
      t(L, (f"{fmt_n(at_top)}–1,300: one announced candidate above the frontier within the year (see basis); even odds it lands", f"{fmt_n(at_top)}–1 300: один анонсированный кандидат выше фронта в пределах года (см. основание); шансы примерно равные")),
      t(L, ("1,300–3,000: the 10,000-qubit plans sit at 2028 and are discounted to a third of their count on the register's delivery record", "1 300–3 000: планы на 10 000 кубитов датированы 2028 годом и дисконтированы до трети заявленного по истории поставок в реестре")),
      t(L, (f"frontier series {fseries('ATOM')}; announced above the frontier: {aseries('ATOM')}", f"серия фронта {fseries('ATOM')}; анонсировано выше фронта: {aseries('ATOM')}")), 'medium',
      t(L, ("a gate-capable tweezer processor above 3,000 qubits by 2028.09, or none above 1,180 by then", "пинцетный процессор с гейтами более чем на 3 000 кубитов к 2028.09 — или ни одного выше 1 180 к тому времени")))
    F('F1c', t(L, ('largest gate-capable trapped-ion device', 'крупнейшее ионное устройство с гейтами')),
      f"{fmt_n(io_top)} ({yr('ION')})",
      t(L, (f"{ion_lo}–{ion_hi}: the historical ×{ion_rate:.2f}/yr gives ≈{fmt_n(round(ion_2027))} by 2027; the largest announced system ({ion_hi}) caps the range" if ion_rate else "—", f"{ion_lo}–{ion_hi}: историческое ×{ion_rate:.2f}/год даёт ≈{fmt_n(round(ion_2027))} к 2027; крупнейшая анонсированная система ({ion_hi}) ограничивает диапазон сверху" if ion_rate else "—")),
      t(L, ("200–400", "200–400")),
      t(L, (f"frontier series {fseries('ION')} — the only family whose frontier still grows year on year; announced: {aseries('ION')}", f"серия фронта {fseries('ION')} — единственное семейство, чей фронт ещё растёт год от года; анонсировано: {aseries('ION')}")), 'medium',
      t(L, ("a trapped-ion device with entangling gates on more than 260 qubits by 2027.09, or the frontier still at 98", "ионное устройство с перепутывающими гейтами более чем на 260 кубитов к 2027.09 — или фронт всё ещё на 98")))
    # F2 — error frontier and the median's lag
    er = {f: erate(efr[f]) for f in ('SC', 'ION', 'ATOM')}; lg = {f: lag(f) for f in ('SC', 'ION', 'ATOM')}
    def proj(f, years):
        if not efr[f] or not er[f]: return None
        return efr[f][-1][1] / (er[f] ** (years))
    F('F2', t(L, ('best two-qubit error per family (devices; hero pairs excluded) and the family median', 'лучшая двухкубитная ошибка по семействам (устройства; рекордные пары исключены) и медиана семейства')),
      '; '.join(f"{t(L, FAMN[f])} {fmt_e(efr[f][-1][1])} / {t(L, ('median', 'медиана'))} {fmt_e(emed.get(f))}" for f in ('SC', 'ION', 'ATOM') if efr[f]),
      '; '.join(f"{t(L, FAMN[f])} ≈ {fmt_e(proj(f, 2027 - efr[f][-1][0]))}" for f in ('SC', 'ION', 'ATOM') if efr[f] and er[f]) + t(L, ("; medians ≈ 2–3×10⁻³ for the three large families", "; медианы ≈ 2–3×10⁻³ у трёх больших семейств")),
      '; '.join(f"{t(L, FAMN[f])} ≈ {fmt_e(proj(f, 2028 - efr[f][-1][0]))}" for f in ('SC', 'ION', 'ATOM') if efr[f] and er[f]) + t(L, ("; the first family median below 2×10⁻³", "; первая медиана семейства ниже 2×10⁻³")),
      t(L, ("frontier series " + '; '.join(f"{t(L, FAMN[f])}: {eseries(f)} (×{er[f]:.2f}/yr{', two points only' if len(efr[f]) <= 2 else ''})" for f in ('SC', 'ION', 'ATOM') if efr[f] and er[f]) + "; the median trails the frontier by " + ', '.join(f"{t(L, FAMN[f])} {lg[f]} yr" for f in ('SC', 'ION', 'ATOM') if lg.get(f) is not None) + " (the year the frontier first reached today's median)",
            "серии фронта " + '; '.join(f"{t(L, FAMN[f])}: {eseries(f)} (×{er[f]:.2f}/год{', всего две точки' if len(efr[f]) <= 2 else ''})" for f in ('SC', 'ION', 'ATOM') if efr[f] and er[f]) + "; медиана отстаёт от фронта на " + ', '.join(f"{t(L, FAMN[f])} {lg[f]} г." for f in ('SC', 'ION', 'ATOM') if lg.get(f) is not None) + " (год, когда фронт впервые достиг сегодняшней медианы)")), 'medium',
      t(L, ("a family frontier that fails to improve for two editions, or a median that improves faster than the frontier did three years earlier", "фронт семейства, не улучшившийся два издания подряд, или медиана, улучшающаяся быстрее, чем фронт тремя годами ранее")))
    # F3 — QEC on hardware
    F('F3', t(L, ('machines that have run a code; decoders in the loop', 'машины, запускавшие код; декодеры в цикле')),
      f"{len(codem)} / {len(inloop)}",
      t(L, (f"≥ 55 machines with a code (cumulative series {', '.join(f'{y} {v}' for y, v in cum.items() if y >= 2022)}); 6–8 in the loop", f"≥ 55 машин с кодом (накопленная серия {', '.join(f'{y} {v}' for y, v in cum.items() if y >= 2022)}); 6–8 в цикле")),
      t(L, (f"≥ 65 with a code; 8–12 in the loop ({len(planned_rt)} machines list real-time decoding as planned or intended: {', '.join(mdcell(m['name']) for m in sorted(planned_rt, key=lambda m: m['name']))}; half on time is the working assumption)", f"≥ 65 с кодом; 8–12 в цикле ({len(planned_rt)} машин заявляют декодирование в реальном времени как план: {', '.join(mdcell(m['name']) for m in sorted(planned_rt, key=lambda m: m['name']))}; рабочее допущение — половина в срок)")),
      t(L, ("cumulative count of code-running machines by cohort (a doubling every ~2 years since 2023) and the register's planned-decoding rows", "накопленное число машин с кодом по когортам (удвоение каждые ~2 года с 2023) и строки реестра с планируемым декодированием")), 'medium',
      t(L, ("fewer than 52 machines with a code, or fewer than 6 closed loops, in 2027.09", "менее 52 машин с кодом или менее 6 замкнутых циклов в 2027.09")))
    # F4 — links
    F('F4', t(L, ('devices with a demonstrated link station (interconnect layer)', 'устройства с продемонстрированной станцией связи (слой межсоединений)')),
      f"{len(link_dev)} ({', '.join(t(L, FAMN[f]) + ' ' + str(sum(1 for m in link_dev if m['family'] == f)) for f in FAM_ORDER if any(m['family'] == f for m in link_dev))})",
      t(L, (f"9–12: of the {len(link_ann)} announced machines that name a link ({', '.join(mdcell(m['name']) + ((' (%s)' % m['year']) if m['year'] else '') for m in link_ann)}), the ones dated 2025–2026 are the candidates", f"9–12: из {len(link_ann)} анонсированных машин, называющих связь ({', '.join(mdcell(m['name']) + ((' (%s)' % m['year']) if m['year'] else '') for m in link_ann)}), кандидаты — датированные 2025–2026")),
      t(L, ("12–18; the interconnect gap share falls below 85 % only if the multi-module superconducting lattices arrive", "12–18; доля пробелов межсоединения опустится ниже 85 % только с приходом многомодульных сверхпроводниковых решёток")),
      t(L, ("the register's announced-link rows discounted by the delivery record; the historical series is too short to extrapolate", "анонсированные строки реестра со связью, дисконтированные по истории поставок; историческая серия слишком коротка для экстраполяции")), 'low',
      t(L, ("fewer than 9 devices with a link in 2027.09, or more than 12", "менее 9 устройств со связью в 2027.09 — или более 12")))
    # F5 — control
    F('F5', t(L, ('machines with integrated control; superconducting devices ≥ 100 qubits driven cryogenically', 'машины с интегрированным управлением; сверхпроводниковые устройства ≥ 100 кубитов с криогенным управлением')),
      f"{len(integ)} / 0",
      t(L, (f"≤ 25 / 0: the candidates are demos and claims ({', '.join(mdcell(m['name']) for m in sorted(ctl_cand, key=lambda m: m['name']))}); IBM's cryo-CMOS is scheduled with Starling (2029)", f"≤ 25 / 0: кандидаты — демонстрации и заявления ({', '.join(mdcell(m['name']) for m in sorted(ctl_cand, key=lambda m: m['name']))}); cryo-CMOS IBM запланирован вместе со Starling (2029)")),
      t(L, ("≤ 30 / 0–1", "≤ 30 / 0–1")),
      t(L, ("H3's mechanism: integration happens where physics forces it (spins, annealers, surface traps) and is a plan elsewhere; the register's control-placement field lists the plans", "механизм H3: интеграция происходит там, где её вынуждает физика (спины, отжиг, поверхностные ловушки), и остаётся планом в остальном; поле размещения управления в реестре перечисляет планы")), 'high',
      t(L, ("a ≥ 100-qubit superconducting device with production cryogenic control before 2028.09", "сверхпроводниковое устройство ≥ 100 кубитов с серийным криогенным управлением до 2028.09")))
    # F6 — roadmap checkpoints
    F('F6', t(L, ('roadmap checkpoints the register can score by 2028', 'контрольные точки дорожных карт, которые реестр сможет оценить к 2028')),
      f"{len(due)} " + t(L, ('roadmaps dated 2025–2028', 'карт с датами 2025–2028')) + ': ' + ', '.join(f"{rid} ({y})" for rid, y in due),
      t(L, ("the checkpoints dated 2026–2027 are scored; on H6's distribution (56 of 65 SHORT verdicts on error or gates) the expectation is that they miss on the error budget, not on qubits", "точки, датированные 2026–2027, оцениваются; по распределению H6 (56 из 65 вердиктов SHORT — по ошибке или гейтам) ожидание таково, что они промахнутся по бюджету ошибок, а не по кубитам")),
      t(L, ("the 2028 checkpoints are scored; at least two of three miss on the logical error per operation", "оцениваются точки 2028 года; как минимум две из трёх промахиваются по логической ошибке на операцию")),
      t(L, ("the register's roadmap-feasibility verdicts and their dates", "вердикты реестра об осуществимости дорожных карт и их даты")), 'medium',
      t(L, ("a dated checkpoint met on qubits, error and gate budget together", "датированная точка, выполненная одновременно по кубитам, ошибке и бюджету гейтов")))
    H("**" + ("Table 8.5 — the forecast ledger (scored by the 2027.09 and 2028.09 editions)" if en else "Таблица 8.5 — реестр прогнозов (оценивается изданиями 2027.09 и 2028.09)") + "**")
    o.append(("| # | Indicator | Today (2026.09) | Expected at 2027.09 | Expected at 2028.09 | Basis | Confidence | Falsified if |" if en else
              "| # | Индикатор | Сегодня (2026.09) | Ожидание к 2027.09 | Ожидание к 2028.09 | Основание | Уверенность | Опровергнуто, если |") + "\n|---|---|---|---|---|---|---|---|\n")
    for r in ledger:
        o.append(f"| {r['id']} | {mdcell(r['indicator'])} | {mdcell(r['now'])} | {mdcell(r['e2027'])} | {mdcell(r['e2028'])} | {mdcell(r['basis'])} | {t(L, CONF[r['confidence']])} | {mdcell(r['falsified_if'])} |\n")
    o.append("\n")
    o.append(("Reading the ledger. The reliable part is the shape, not the digits: the count frontier of the two largest families has not moved for three and four years while the announced frontier runs a decade ahead of it (F1), the error frontier improves by a steady third to a half per year and the medians follow it with a lag of about three years (F2), and the adoption curves — codes on hardware, links, integrated control — are set by the delivery of the machines the register already lists as planned, discounted by how often such rows have slipped (F3–F5). What the ledger cannot do is time a single machine; what it can do is be wrong in public, one edition later.\n\n" if en else
              "Как читать реестр прогнозов. Надёжна форма, а не цифры: фронт числа кубитов у двух крупнейших семейств не двигался три и четыре года, тогда как анонсированный фронт убегает на десятилетие вперёд (F1); фронт ошибок улучшается на устойчивые треть–половину в год, а медианы следуют за ним с отставанием около трёх лет (F2); кривые принятия — коды на железе, связи, интегрированное управление — задаются поставкой машин, которые реестр уже числит запланированными, с дисконтом на то, как часто такие строки сползали (F3–F5). Чего реестр прогнозов не может — датировать отдельную машину; что может — оказаться неправым публично, одним изданием позже.\n\n"))
    if en:
        with open(os.path.join(ROOT, 'data', 'forecast-ledger.json'), 'w', encoding='utf-8', newline='\n') as fh:
            json.dump({'edition': M.get('edition'), 'written': 'by build/machines_chapter.py from the register of ' + str(src.get('register', '')), 'forecasts': ledger}, fh, ensure_ascii=False, indent=1); fh.write('\n')

    # ---------- 8.6 where the architecture goes
    H("### 8.6 " + ("Where the architecture is going" if en else "Куда идёт архитектура"))
    nsup = sum(1 for v in verdicts.values() if v == 'yes'); npart = sum(1 for v in verdicts.values() if v == 'part'); nno = sum(1 for v in verdicts.values() if v == 'no')
    o.append((f"Of the eight hypotheses, {nsup} are supported, {npart} partly and {nno} not. Read together they draw one direction rather than eight. **From count to encoded qubits and links.** The two least populated layers — code/decoder and interconnect — are exactly the two every roadmap depends on (H4, H5, H6): the next generation of machines will be judged by the logical error per cycle and by the link between modules, and the register already shows the count race losing its meaning (H1). **A division of roles between families rather than a winner.** The largest devices are tweezer arrays, the best gate is an ion trap, the fastest clock a transmon lattice and the room-temperature fabrication is photonic; the medians converge (H2) while the extremes stay apart, and the stations do not cross the family lines (H8) — the architecture that reaches the goals of §4 will more likely be a *composition* of paths joined by links than a single path grown large. **The slow variable is control.** Integrated control is a plan for the families that can afford room-temperature racks and a necessity only where the physics forces it (H3); the map's placement coordinate will move last. **The binding constraint is the error budget.** Roadmaps are short by orders of magnitude on error and gate count and rarely on qubits (H6), so the machines that matter next are the ones that move the logical error per operation, whatever their qubit count.\n\n" if en else
              f"Из восьми гипотез {nsup} подтверждены, {npart} — частично, {nno} — нет. Вместе они рисуют одно направление, а не восемь. **От числа кубитов — к закодированным кубитам и связям.** Два наименее заполненных слоя — код/декодер и межсоединение — ровно те, от которых зависит каждая дорожная карта (H4, H5, H6): следующее поколение машин будут судить по логической ошибке на цикл и по связи между модулями, и реестр уже показывает, как гонка за числом теряет смысл (H1). **Разделение ролей между семействами, а не победитель.** Крупнейшие устройства — массивы пинцетов, лучший гейт — ионная ловушка, самый быстрый такт — трансмонная решётка, а изготовление при комнатной температуре — фотонное; медианы сходятся (H2), крайние значения остаются врозь, а станции не пересекают границ семейств (H8) — архитектура, которая достигнет целей §4, скорее будет *композицией* путей, соединённых связями, чем одним разросшимся путём. **Медленная переменная — управление.** Интегрированное управление — план для семейств, которым по карману стойки при комнатной температуре, и необходимость только там, где его вынуждает физика (H3); координата размещения на карте сдвинется последней. **Связывающее ограничение — бюджет ошибок.** Дорожные карты не дотягивают на порядки по ошибке и числу гейтов и редко по кубитам (H6), поэтому машины, которые важны дальше, — те, что сдвигают логическую ошибку на операцию, каково бы ни было их число кубитов.\n\n"))

    # ---------- 8.7 verification and limits
    H("### 8.7 " + ("Verification and limits" if en else "Проверка и границы"))
    ev_layer = {}
    for m in MS:
        for ln, cells in m['layers'].items():
            for c in cells:
                if c['role'] != 'primary': continue
                a = ev_layer.setdefault(ln, [0, 0]); a[1] += 1; a[0] += bool(c['evidence'].get('verified'))
    def eg(ln): a = ev_layer.get(ln, [0, 0]); return f"{pct(a[0], a[1])} ✅ ({a[0]}/{a[1]})"
    pressonly = sorted(m['name'] for m in MS if m['evidence_counts']['verified'] == 0)
    H("**" + ("Table 8.7 — what each verdict rests on" if en else "Таблица 8.7 — на чём стоит каждый вердикт") + "**")
    o.append(("| Hypothesis | Verdict | Sample | Filters applied | Evidence grade of the inputs | What would overturn it |" if en else
              "| Гипотеза | Вердикт | Выборка | Применённые фильтры | Класс свидетельств входов | Что его опрокинуло бы |") + "\n|---|---|---|---|---|---|\n")
    rows = [
        ('H1', f"{len(gdev)} " + t(L, ('gate-capable devices', 'устройств с гейтами')), t(L, ('status ∈ {deployed, demonstrated, retired}; no target/component/analog/no-gate flag', 'статус ∈ {в эксплуатации, продемонстрирована, выведена}; без флагов цели/компонента/аналога/без гейта')), t(L, ('register field `physical_qubits_num` (press-level for most machines)', 'поле реестра `physical_qubits_num` (для большинства машин — уровень прессы)')), t(L, ('a superconducting device cohort whose median passes the atoms', 'сверхпроводниковая когорта устройств с медианой выше атомной'))),
        ('H2', ', '.join(f"{t(L, FAMN[f])} {len(errs[f])}" for f in FAM_ORDER if errs[f]), t(L, ('devices; hero-pair, target and component numbers excluded', 'устройства; исключены рекордные пары, цели и компоненты')), t(L, ('register field `err_2q_median` (paper-level where a figure is cited, else press)', 'поле реестра `err_2q_median` (уровень статьи, где цитируется рисунок, иначе пресса)')), t(L, ('a family median more than ×2 from the others, or a non-ion best', 'медиана семейства дальше ×2 от остальных или лучшее значение не у ионов'))),
        ('H3', f"{N}", t(L, ('none (all rows); the ≥ 100-qubit clause on devices', 'нет (все строки); условие ≥ 100 кубитов — по устройствам')), t(L, ('control layer cells: ', 'ячейки слоя управления: ')) + eg('5'), t(L, ('integrated control on more than 30 % of machines, or a ≥ 100-qubit superconducting device driven cryogenically', 'интегрированное управление более чем у 30 % машин или сверхпроводниковое устройство ≥ 100 кубитов с криогенным управлением'))),
        ('H4', f"{sum(c[1] for c in cohc.values())} " + t(L, ('machines in cohorts 2023–2026', 'машин в когортах 2023–2026')), t(L, ('cohort = year of the status date', 'когорта = год даты статуса')), t(L, ('code layer cells: ', 'ячейки слоя кода: ')) + eg('7'), t(L, ('a falling share across three cohorts, or ten machines with a decoder in the loop', 'падающая доля на трёх когортах или десять машин с декодером в цикле'))),
        ('H5', f"{N}", t(L, ('primary cells only', 'только основные ячейки')), t(L, ('interconnect layer cells: ', 'ячейки слоя межсоединений: ')) + eg('9'), t(L, ('another layer with a larger gap, or links on a quarter of the machines', 'другой слой с большим пробелом или связи у четверти машин'))),
        ('H6', f"{len(R)} " + t(L, ('roadmap × algorithm rows', 'строк карта × алгоритм')), t(L, ('verdict = SHORT', 'вердикт = SHORT')), t(L, ('register table `roadmap-feasibility` (targets as published by the vendors)', 'таблица реестра `roadmap-feasibility` (цели, как опубликованы вендорами)')), t(L, ('qubit-only deficits above half of the SHORT verdicts', 'дефициты только по кубитам более чем у половины вердиктов SHORT'))),
        ('H7', f"{sum(c[1] for c in cohs.values())} " + t(L, ('machines in cohorts 2023–2026', 'машин в когортах 2023–2026')), t(L, ('status ∈ {announced, planned}', 'статус ∈ {анонсирована, запланирована}')), t(L, ('register field `status` (press-level by nature)', 'поле реестра `status` (по природе — уровень прессы)')), t(L, ('the newest cohort’s share falling to the previous cohorts’ level', 'доля новейшей когорты, упавшая до уровня предыдущих'))),
        ('H8', f"{n_nodes} " + t(L, ('occupied stations', 'занятых станций')), t(L, ('primary role; gaps excluded', 'основная роль; пробелы исключены')), t(L, ('all primary cells: ', 'все основные ячейки: ')) + f"{pct(vt, at)} ✅", t(L, ('half of the occupied stations shared by two families or more', 'половина занятых станций, делимая двумя и более семействами'))),
    ]
    for h, n_, filt, evg, over in rows:
        o.append(f"| {h} | {t(L, VER[verdicts[h]])} | {n_} | {filt} | {evg} | {over} |\n")
    o.append("\n")
    o.append((f"Limits. The cohort is the year of the register's status date, which mixes first light, general availability and the latest milestone; the classifiers are string rules over free-text fields and are printed at the top of `build/machines_chapter.py` so that a reviewer can object to a rule rather than to a number; the population is the register's, which favours machines with an English-language document. {len(pressonly)} machines have no verified cell at all (press pages only) and enter the counts at press level: " + ', '.join(mdcell(x) for x in pressonly) + ". Every hypothesis is re-tested by each build; a verdict that flips between editions is itself a finding and will be reported in the changelog.\n\n" if en else
              f"Границы. Когорта — год даты статуса в реестре, смешивающий первый запуск, общую доступность и последнюю веху; классификаторы — строковые правила над свободным текстом, напечатанные в начале `build/machines_chapter.py`, чтобы рецензент мог возразить правилу, а не числу; популяция — реестровая, с перекосом к машинам, у которых есть документ на английском языке. {len(pressonly)} машин не имеют ни одной подтверждённой ячейки (только пресс-релизы) и входят в подсчёты на уровне прессы: " + ', '.join(mdcell(x) for x in pressonly) + ". Каждая гипотеза перепроверяется при каждой сборке; вердикт, изменившийся между изданиями, — сам по себе результат и будет отмечен в списке изменений.\n\n"))
    return ''.join(o)


if __name__ == '__main__':
    import sys
    lang = sys.argv[1] if len(sys.argv) > 1 else 'en'
    sys.stdout.write(sec_machines(lang))
