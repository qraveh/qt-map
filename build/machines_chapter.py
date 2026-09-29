# -*- coding: utf-8 -*-
"""§8 "Machines" of the report — generated from data/machines.json (the machines register joined to the map)
and data/graph.json. Deterministic: same inputs give identical markdown. Called by make_sections.py (splice)
in both languages. Every number in the chapter is computed here; the prose states the claim, the test and the
verdict, so a reader can re-run the test on the register.

Classifiers (kept simple and visible, so a reviewer can disagree with a line, not with a model):
  status class   = first word of the register's status (DEPLOYED / DEMONSTRATED / ANNOUNCED / PLANNED / RETIRED / OTHER)
  cohort year    = first four-digit year in status_date
  device         = status class in {DEPLOYED, DEMONSTRATED, RETIRED} and no flag in {target-not-device, component-only}
  gate-capable   = device without a flag in {analog-only, no-entangling-gate, 1q-only, enabler-only, detection-only, not-a-qubit}, not on an architecture without an
                   entangling gate (annealer, Rydberg analog simulator, boson sampler), and whose primary gate cell is not `none`
  control class  = integrated (on-chip microwave / cryo-CMOS / SFQ / flux DAC / 4 K), optics, room-temperature electronics, undisclosed
  decoding class = in-loop / offline / planned / none, from the register's `realtime` field
"""
import json, os, re, statistics, sys
def _org_slug(m):
    """the slug of the machine's organisation page, or None (build/orgs.py; the organisations register)"""
    try:
        import orgs; return orgs.slug_for_machine(m.get('id') if isinstance(m, dict) else m)
    except Exception: return None
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAM_ORDER = ['SC', 'ION', 'ATOM', 'PHOTON', 'SPIN', 'DEFECT', 'TOPO', 'ANNEAL']
FAMN = {'SC': ('superconducting circuits', 'сверхпроводниковые схемы'), 'ION': ('trapped ions', 'ионы в ловушках'), 'ATOM': ('neutral atoms', 'нейтральные атомы'), 'PHOTON': ('photonics', 'фотоника'), 'SPIN': ('semiconductor spins', 'полупроводниковые спины'), 'DEFECT': ('defect spins', 'дефектные спины'), 'TOPO': ('topological', 'топологические'), 'ANNEAL': ('quantum annealers', 'квантовый отжиг')}
STAT_ORDER = ['DEPLOYED', 'DEMONSTRATED', 'ANNOUNCED', 'PLANNED', 'RETIRED', 'OTHER']
STATN = {'DEPLOYED': ('deployed', 'в эксплуатации'), 'DEMONSTRATED': ('demonstrated', 'продемонстрирована'),
         'ANNOUNCED': ('announced', 'анонсирована'), 'PLANNED': ('planned', 'запланирована'),
         'RETIRED': ('retired', 'выведена'), 'OTHER': ('other', 'прочее')}
NON_DEVICE_FLAGS = {'target-not-device', 'component-only'}
EXCL_ERR_FLAGS = {'hero-pair-number', 'target-not-device', 'component-only'}
CLAIM_FLAGS = {'vendor-claim', 'unverified-claim', 'unverifiable', 'unverifiable-vendor-claim', 'outlier-claim', 'not-peer-reviewed', 'press-only'}   # a 2Q figure from such a row is printed as a claim (27 Sep 2026: Table 8.3 mixed [C] and [D] numbers)


def claim_mark(m, L):
    """' (claimed)' after a two-qubit error that the register holds as a company claim rather than a measured, published figure"""
    txt = str((m.get('profile') or {}).get('err_2q_median') or '')
    return (' (claimed)' if L == 'en' else ' (заявлено)') if (m['flags'] & CLAIM_FLAGS) or 'claim' in txt.lower() else ''
NON_GATE_FLAGS = {'analog-only', 'no-entangling-gate', '1q-only', 'enabler-only', 'detection-only', 'not-a-qubit'}
NON_GATE_PATHS = {'anneal', 'atom_analog', 'ph_sampler'}   # architectures whose gate layer holds no entangling gate (analog evolution, linear optics, annealing)
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
        # a link technology joins modules (photonic, microwave or long-range coupler: mobility ≠ static); multi-die packaging and
        # cryogenic fan-out are interconnect technologies inside one module and do not count
        x['link'] = bool(prim9) and prim9[0].get('state', 'station') == 'station' and node.get(prim9[0]['node'], {}).get('d') != 'static'
        x['l9'] = prim9[0].get('state', 'station') if prim9 else 'none'
        x['cloud'] = 'cloud' in (m.get('access') or '').lower()
        # annealers, analog simulators and samplers run no entangling gate whatever their flags say; nor does a machine whose gate cell is `none`
        prim3 = [c for c in m['layers'].get('3', []) if c['role'] == 'primary']
        x['gatedev'] = x['device'] and not (x['flags'] & NON_GATE_FLAGS) and m.get('map_path') not in NON_GATE_PATHS and not (prim3 and prim3[0].get('state', 'station') != 'station')
        ms.append(x)
    return M, G, node, layers, paths, ms


FIG = {}   # the chapter's headline figures, filled while sec_machines runs; §0 of the hand-written report reads them through
           # build_html.report_numbers placeholders ({{N_CODE_RUN}} …) so that the summary can no longer drift from the chapter


def figures():
    """the headline figures of §8 (computed once; language-independent)"""
    if not FIG: sec_machines('en')
    return dict(FIG)


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
    o.append((f"The map's technologies are what *can* be built; the machines register says what *has been* built, announced or planned, one row per machine, each joined to the map as an architecture instance (§7.10). This chapter reads the register as a population: how large it is, which technologies it is built from, what idea justifies each attempt, and what the population's trends say about where the architecture is heading. Every count below is computed from the Quantum Machines Register as of 26 September 2026 (the register and its evidence file are published with the Atlas's data); a claim is tested against the register, not asserted, and its evidence grade is carried along — the share of the cells behind it whose cited source was opened and found to support them (✅) rather than left unverified or inferred (🔎).\n\n" if en else
              f"Технологии карты — это то, что *может* быть построено; реестр машин говорит, что *построено*, анонсировано или запланировано: по строке на машину, каждая соединена с картой как экземпляр архитектуры (§7.10). Эта глава читает реестр как популяцию: насколько она велика, из каких технологий собрана, какая идея оправдывает каждую попытку и что тренды популяции говорят о том, куда движется архитектура. Каждое число ниже вычислено по Реестру квантовых машин по состоянию на 26 сентября 2026 года (реестр и его файл свидетельств публикуются вместе с данными Атласа); утверждение проверяется по реестру, а не постулируется, и его класс свидетельств указан рядом — доля ячеек за ним, чей источник был открыт и подтвердил их (✅), а не оставлен непроверенным или выведен (🔎).\n\n"))
    ncells = sum(m['evidence_counts']['total'] for m in MS)
    o.append((f"**Terms used in this chapter.** A *quantum machine* — *machine* for short in this chapter — is one row of the register: a named system an organisation has built, announced or planned. Its *family* is its qubit platform ({', '.join(t(L, FAMN[f]) for f in FAM_ORDER)}); its *architecture* is the map architecture it instantiates — one of the {len(PATHS)} architectures of §7.3, i.e. the family plus the choice of encoding, gate and control that defines it (cat qubits and dual-rail erasure are architectures of the superconducting family). An *evidence cell* is one machine × one technology it uses in a layer of the stack, with the document that shows it (a layer may hold a primary technology and an alternate, so a machine has about a dozen cells, not ten) and the register holds {ncells:,}. A cell is *verified* (✅) when its cited source — a paper, a whitepaper, a product page or a technical press release; the card shows which by its glyph — was opened and seen to show that technology in that machine, and *unverified* (🔎) when the source was not re-opened or the cell is an inference; the *evidence grade* of a count is the verified share of the cells it rests on — it says how much of a claim rests on sources that were actually checked, not how many of them are papers. A *device* is a machine whose status is deployed, demonstrated or retired and that is not flagged as a target or a component; a *gate-capable* device additionally runs an entangling gate (analog simulators, tweezer arrays without a gate and single-qubit testbeds are devices but not processors). A *cohort* is the year of the register's status date. *Integrated control* means the qubits are driven by electronics on the chip or inside the cryostat (on-chip microwave electrodes, cryo-CMOS, SFQ, flux DACs) rather than by room-temperature racks or free-space optics; *closed-loop decoding* means the error-correction decoder acts within the cycle. A *link technology* is an interconnect-layer technology that joins modules — a photonic, microwave or long-range coupler link; multi-die packaging inside one module and cryogenic signal fan-out are interconnect technologies but not links. A layer in which a machine uses no technology holds one of three values: *none* (nothing in this layer — no code, no decoder, no interconnect; for analog and sampling machines no encoding layer or no entangling gate), *undisclosed* (something is there, nothing is published) or an *Atlas gap* (`∅G-…`: the machine runs what the map has no technology for; each is an entry of the register's gap ledger). A *roadmap verdict* is the register's feasibility check of a published roadmap against its target algorithm (FEASIBLE, SHORT with a deficit, or NOT EVALUABLE).\n\n" if en else
              f"**Термины этой главы.** *Квантовая машина* — в этой главе коротко *машина* — одна строка реестра: именованная система, которую организация построила, анонсировала или запланировала. Её *семейство* — кубитная платформа ({', '.join(t(L, FAMN[f]) for f in FAM_ORDER)}); её *архитектура* — линия карты, которую она реализует: одна из {len(PATHS)} архитектур §7.3, то есть семейство плюс выбор кодирования, гейта и управления, который её определяет (кошачьи кубиты и двухрельсовое стирание — архитектуры сверхпроводникового семейства). *Ячейка свидетельств* — одна машина × одна технология, которую она использует в слое стека, вместе с документом, который это показывает (в слое могут стоять основная технология и альтернатива, поэтому у машины около дюжины ячеек, в реестре их {ncells:,}. Ячейка *проверена* (✅), когда её источник — статья, whitepaper, страница продукта или технический пресс-релиз; какой именно, показывает значок в карточке — был открыт и в нём увидена эта технология в этой машине, и *не проверена* (🔎), когда источник не открывался заново или ячейка — вывод; *класс свидетельств* числа — доля проверенных ячеек, на которых оно стоит: он говорит, какая часть утверждения опирается на действительно проверенные источники, а не сколько из них — статьи. *Устройство* — машина со статусом «в эксплуатации», «продемонстрирована» или «выведена», не помеченная как цель или компонент; устройство *с гейтами* вдобавок выполняет перепутывающий гейт (аналоговые симуляторы, массивы пинцетов без гейта и однокубитные стенды — устройства, но не процессоры). *Когорта* — год даты статуса в реестре. *Интегрированное управление* — кубиты управляются электроникой на чипе или внутри криостата (микроволновые электроды на чипе, cryo-CMOS, SFQ, потоковые ЦАП), а не стойками при комнатной температуре или оптикой в свободном пространстве; *замкнутое декодирование* — декодер коррекции ошибок действует внутри такта. *Технология связи* — технология слоя межсоединений, соединяющая модули: фотонная, микроволновая или дальняя связь через каплер; многокристальная сборка внутри одного модуля и криогенная разводка сигналов — технологии межсоединения, но не связи. Слой, в котором машина не использует ни одной технологии, содержит одно из трёх значений: *none* (в этом слое ничего нет — нет кода, декодера, межсоединения; у аналоговых и сэмплирующих машин — нет слоя кодирования или перепутывающего гейта), *undisclosed* (что-то есть, но ничего не опубликовано) или *пробел Атласа* (`∅G-…`: машина запускает то, для чего у карты нет технологии; каждый — запись в реестре пробелов). *Вердикт дорожной карты* — проверка реестром опубликованной карты на осуществимость её целевого алгоритма (FEASIBLE, SHORT с дефицитом или NOT EVALUABLE).\n\n"))
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
    o.append((f"**{N} quantum machines, {len(FAM_ORDER)} families, {len(PATHS)} architectures.** {len(dev)} of them exist as hardware — *devices*, in this chapter's word: {nsc['DEPLOYED']} deployed, {nsc['DEMONSTRATED']} demonstrated, {nsc['RETIRED']} retired, not counting the rows flagged as a target or a component — and {N-len(dev)} are announcements, plans or targets. Every count in this chapter is computed from the register when the page is built; none is typed in. Access: {ncloud} reachable through a cloud service, {nprem} sold on-premises, {nlab} laboratory-only. By country of the operating organisation: " + ', '.join(f"{c} {n}" for c, n in topc) + f". By cohort (the year of the status date): " + ', '.join(f"{y} — {n}" for y, n in sorted(yrs.items())) + ".\n\n" if en else
              f"**{N} квантовых машин, {len(FAM_ORDER)} семейств, {len(PATHS)} архитектур.** {len(dev)} из них существуют в железе — *устройства*, словом этой главы: {nsc['DEPLOYED']} в эксплуатации, {nsc['DEMONSTRATED']} продемонстрированы, {nsc['RETIRED']} выведены, не считая строк, помеченных как цель или компонент, — а {N-len(dev)} — анонсы, планы или цели. Каждое число этой главы вычисляется из реестра при сборке страницы; ни одно не вписано вручную. Доступ: {ncloud} доступны через облачный сервис, {nprem} проданы на площадку заказчика, {nlab} только в лаборатории. По стране организации-оператора: " + ', '.join(f"{c} {n}" for c, n in topc) + f". По когортам (год даты статуса): " + ', '.join(f"{y} — {n}" for y, n in sorted(yrs.items())) + ".\n\n"))
    H("**" + ("Table 8.1 — families × status (machines); devices; cloud access; evidence cells and how many of them are documented" if en else "Таблица 8.1 — семейства × статус (машин); устройства; облачный доступ; ячейки свидетельств и сколько из них документировано") + "**")
    hdr = ("| Family | Machines | Deployed | Demonstrated | Announced | Planned | Retired | Other | Devices | Cloud access | Evidence cells | Verified cells (✅) | Verified, % |" if en else
           "| Семейство | Машин | В эксплуатации | Продемонстрированы | Анонсированы | Запланированы | Выведены | Прочее | Устройства | Облачный доступ | Ячеек свидетельств | Проверено (✅) | Проверено, % |")
    o.append(hdr + "\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    fshare = {}   # documented share per family, for the reading paragraph (the sentence quoted 30 % / 57 % from an earlier register until 27 Sep 2026)
    for f in FAM_ORDER:
        fm = byfam[f]
        if not fm: continue
        v = sum(m['evidence_counts']['verified'] for m in fm); a = sum(m['evidence_counts']['total'] for m in fm)
        fshare[f] = (v / a) if a else 0
        c = {s: sum(1 for m in fm if m['sc'] == s) for s in STAT_ORDER}
        o.append(f"| {t(L, FAMN[f])} | {len(fm)} | {c['DEPLOYED']} | {c['DEMONSTRATED']} | {c['ANNOUNCED']} | {c['PLANNED']} | {c['RETIRED']} | {c['OTHER']} | {sum(1 for m in fm if m['device'])} | {sum(1 for m in fm if m['cloud'])} | {a} | {v} | {pct(v, a)} |\n")
    vt = sum(m['evidence_counts']['verified'] for m in MS); at = sum(m['evidence_counts']['total'] for m in MS)
    o.append(f"| **{'all' if en else 'все'}** | {N} | {nsc['DEPLOYED']} | {nsc['DEMONSTRATED']} | {nsc['ANNOUNCED']} | {nsc['PLANNED']} | {nsc['RETIRED']} | {nsc['OTHER']} | {len(dev)} | {ncloud} | {at} | {vt} | {pct(vt, at)} |\n\n")
    o.append((f"Reading the table: the superconducting family is the largest by far and also the only one with retirements; the spin family is small and mostly at the demonstration stage, the photonic one small and split between deployed and demonstrated machines; the {nsc['OTHER']} rows in *other* are statuses the register could not reduce to one word (component testbeds, disputed reachability). The last three columns are the chapter's evidence grade: of the evidence cells behind a family's rows, how many the cited source was opened and found to support. It matters because every count in this chapter inherits it — the family at {round(100*min(fshare.values()))} % rests mostly on press claims and inferences, the family at {round(100*max(fshare.values()))} % mostly on papers — and it differs by family because the families publish differently: architecture papers with device figures are the norm for the academic superconducting, ion and atom machines and the exception for commercial photonic and spin announcements.\n\n" if en else
              f"Чтение таблицы: сверхпроводниковое семейство — самое большое и единственное с выведенными машинами; спиновое семейство мало и в основном на стадии демонстрации, фотонное — мало и поделено между развёрнутыми и продемонстрированными машинами; {nsc['OTHER']} строк *прочее* — статусы, которые реестр не свёл к одному слову (испытательные стенды компонентов, спорная достижимость). Последние три столбца — класс свидетельств главы: сколько из ячеек свидетельств за строками семейства проверены по открытому источнику. Это важно, потому что каждое число главы его наследует — семейство на {round(100*min(fshare.values()))} % стоит в основном на заявлениях прессы и выводах, семейство на {round(100*max(fshare.values()))} % — в основном на статьях, — и он различается по семействам, потому что семейства публикуют по-разному: статьи об архитектуре с рисунками устройства — норма для академических сверхпроводниковых, ионных и атомных машин и исключение для коммерческих фотонных и спиновых анонсов.\n\n"))

    # ---------- 8.2 what they are built from
    H("### 8.2 " + ("What the machines are built from" if en else "Из чего собраны машины"))
    o.append(("Per layer of the map, the technologies the machines actually occupy (primary role), the three ways a machine can occupy none — *none* (nothing in this layer), *undisclosed* (published nothing) and *Atlas gap* (the map has no technology for what it runs) — and the families that share the most-used technology. The `none` column is the register's maturity profile: near zero for the carrier, small for gates, connectivity and fabrication, and large for exactly the layers where the field's claims run ahead of its machines — code, decoder, interconnect. The `undisclosed` column is its disclosure profile, and the gap column is the map's own to-do list: what the machines run that the map does not yet name.\n\n" if en else
              "По слоям карты: технологии, которые машины реально занимают (основная роль), три способа не занимать ни одной — *none* (в этом слое ничего нет), *undisclosed* (ничего не опубликовано) и *пробел Атласа* (у карты нет технологии для того, что запускает машина), — и семейства, делящие самую занятую технологию. Столбец `none` — профиль зрелости реестра: около нуля для носителя, мал для гейтов, связности и изготовления и велик ровно на тех слоях, где заявления отрасли опережают её машины: код, декодер, межсоединение. Столбец `undisclosed` — его профиль раскрытия, а столбец пробелов — список дел самой карты: то, что машины запускают, а карта ещё не называет.\n\n"))
    H("**" + ("Table 8.2 — layers: none, undisclosed and gap cells, and the most-used technologies" if en else "Таблица 8.2 — слои: ячейки none, undisclosed и пробелы, и самые занятые технологии") + "**")
    o.append(("| Layer | none | undisclosed | Atlas gap | Most-used technologies (machines) | Families on the first |" if en else
              "| Слой | none | undisclosed | Пробел Атласа | Самые занятые технологии (машин) | Семейств на первой |") + "\n|---|---|---|---|---|---|\n")
    gapshare = {}; voidshare = {}; undshare = {}
    for ln in sorted(LAYERS, key=int):
        l = LAYERS[ln]; prim = {}; gaps = 0; void = 0; und = 0; fam_of = {}
        for m in MS:
            for c in m['layers'].get(ln, []):
                if c['role'] != 'primary': continue
                st = c.get('state', 'gap' if c['gap'] else 'station')
                if st == 'gap': gaps += 1; continue
                if st == 'none': void += 1; continue
                if st == 'undisclosed': und += 1; continue
                prim[c['node']] = prim.get(c['node'], 0) + 1
                fam_of.setdefault(c['node'], set()).add(m['family'])
        top = sorted(prim.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
        gapshare[ln] = (gaps, N); voidshare[ln] = (void, N); undshare[ln] = (und, N)
        first = top[0][0] if top else None
        fams = ', '.join(t(L, FAMN[f]) for f in FAM_ORDER if first and f in fam_of.get(first, ())) if first else '—'
        def cnt(k): return f"{k} ({pct(k, N)})" if k else "—"
        o.append(f"| {l['n']} {t(L, (l['en'], l['ru']))} | {cnt(void)} | {cnt(und)} | {cnt(gaps)} | " + ('; '.join(f"{nm(k)} `{k}` ({v})" for k, v in top) or '—') + f" | {fams} |\n")
    o.append("\n")

    # ---------- 8.3 the idea behind each attempt
    H("### 8.3 " + ("The idea behind each architecture" if en else "Идея, стоящая за каждой архитектурой"))
    o.append(("A machine is an argument: *this* combination of technologies will reach the goal before the others. The argument is made per architecture (an architecture of the map), not per machine, so the register is read here by architecture — the bet in one line, the count of machines and devices that make it, the largest gate-capable device the register holds for it (analog simulators, arrays without an entangling gate and single-qubit testbeds excluded), and the best two-qubit error among its devices (hero pairs, targets and component demonstrations excluded).\n\n" if en else
              "Машина — это аргумент: *эта* комбинация технологий достигнет цели раньше других. Аргумент делается на уровне архитектуры (линии карты), а не машины, поэтому реестр читается здесь по архитектурам: ставка в одну строку, число машин и устройств, её делающих, крупнейшее устройство с гейтами, которое реестр держит для неё (аналоговые симуляторы, массивы без перепутывающего гейта и однокубитные стенды исключены), и лучшая двухкубитная ошибка среди её устройств (рекордные пары, цели и демонстрации компонентов исключены).\n\n"))
    BET = {
        'sc': ("fast microwave gates on a lithographic lattice; scale by fabrication and, later, by links between chips", "быстрые микроволновые гейты на литографической решётке; масштаб за счёт изготовления и, позже, связей между чипами"),
        'cat': ("bias the noise so that one error type dominates, then correct only that type with a cheap code", "сместить шум так, чтобы доминировал один тип ошибок, и исправлять только его дешёвым кодом"),
        'dualrail': ("turn photon loss into a flagged erasure; erasures cost far fewer qubits to correct than Pauli errors", "превратить потерю фотона в помеченное стирание; стирания исправляются много дешевле паулиевских ошибок"),
        'ion_qccd': ("move the ions, not the information: transport between trap zones gives all-to-all connectivity at the highest gate fidelities", "перемещать ионы, а не информацию: транспорт между зонами ловушки даёт связность «все со всеми» при наивысшей точности гейтов"),
        'ion_chain': ("one static chain, every pair coupled through the shared motion, each ion addressed by its own laser beam; scale by more chains and photonic links", "одна статическая цепочка, каждая пара связана через общее движение, каждый ион адресуется своим лазерным лучом; масштаб — больше цепочек и фотонные связи"),
        'ion_elec': ("gates driven by microwaves and currents in the trap chip, no laser at the gate: control that scales like electronics", "гейты, управляемые микроволнами и токами в чипе ловушки, без лазера на гейте: управление, масштабируемое как электроника"),
        'atom_analog': ("no gates at all: programme the Hamiltonian of a Rydberg array or a lattice gas and let it evolve — simulation and optimisation now, at hundreds of atoms", "вовсе без гейтов: задать гамильтониан ридберговского массива или решёточного газа и дать ему эволюционировать — симуляция и оптимизация уже сейчас, на сотнях атомов"),
        'ph_sampler': ("sample from a linear-optical network of squeezed or single photons: a quantum-advantage experiment, not a programmable computer", "выбирать из линейно-оптической сети сжатых или одиночных фотонов: эксперимент квантового преимущества, а не программируемый компьютер"),
        'atom_rb': ("reconfigurable tweezers make the code geometry programmable and the qubit count cheap; the clock is slow", "перестраиваемые пинцеты делают геометрию кода программируемой, а число кубитов дешёвым; такт медленный"),
        'atom_ae': ("a two-electron atom whose metastable qubit flags its own decay as an erasure, paid for with a worse CZ; the clock qubit and continuous reloading come with the carrier", "двухэлектронный атом, чей метастабильный кубит сам помечает свой распад как стирание — ценой худшего CZ; часовой кубит и непрерывная перезагрузка идут вместе с носителем"),
        'ph_fusion': ("make entanglement by measurement: room-temperature photonic fabrication and networking, loss is the enemy", "создавать перепутывание измерением: фотонное изготовление и сети при комнатной температуре; враг — потери"),
        'ph_cv': ("continuous-variable states and GKP encoding on the same photonic chips", "состояния непрерывных переменных и кодирование GKP на тех же фотонных чипах"),
        'spin_qd': ("the foundry: quantum dots in CMOS, density and cold electronics from the semiconductor industry", "фабрика: квантовые точки в CMOS, плотность и холодная электроника из полупроводниковой отрасли"),
        'spin_donor': ("donor spins in isotopically pure silicon: the longest coherence in a solid", "донорные спины в изотопно чистом кремнии: самая долгая когерентность в твёрдом теле"),
        'defect': ("defect spins as network nodes: few-qubit registers joined by heralded photons", "дефектные спины как узлы сети: регистры из нескольких кубитов, соединённые heralded-фотонами"),
        'topo': ("protection in the hardware: a topological gap instead of a code", "защита в самом устройстве: топологическая щель вместо кода"),
        'anneal': ("special-purpose scale now: thousands of analog qubits for optimisation and simulation", "специализированный масштаб сейчас: тысячи аналоговых кубитов для оптимизации и симуляции"),
    }
    H("**" + ("Table 8.3 — architectures: the bet, the population, the best numbers" if en else "Таблица 8.3 — архитектуры: ставка, популяция, лучшие числа") + "**")
    o.append(("| Architecture (map architecture) | Machines | Devices | Largest gate-capable device (physical qubits) | Best 2Q error among devices | The bet |" if en else
              "| Архитектура (линия карты) | Машин | Устройств | Крупнейшее устройство с гейтами (физ. кубитов) | Лучшая 2Q-ошибка среди устройств | Ставка |") + "\n|---|---|---|---|---|---|\n")
    for pid in [p['id'] for p in G['paths']]:
        pm = [m for m in MS if m['map_path'] == pid]
        if not pm: continue
        pd = [m for m in pm if m['device']]
        big = max([m for m in pd if m['q'] and m['gatedev']], key=lambda m: (m['q'], m['name']), default=None)
        errs = sorted([(m['err'], m['name'], claim_mark(m, L)) for m in pd if m['err'] is not None and not (m['flags'] & EXCL_ERR_FLAGS)])
        o.append(f"| {PATHS[pid][L]} `{pid}` | {len(pm)} | {len(pd)} | " + (f"{mdcell(big['name'])} — {fmt_n(big['q'])}" if big else '—') + " | " + (f"{fmt_e(errs[0][0])} ({mdcell(errs[0][1])}){errs[0][2]}" if errs else '—') + f" | {mdcell(t(L, BET.get(pid, ('—', '—'))))} |\n")
    o.append("\n")
    o.append(("Two readings. First, the bets are not symmetric in what they need to prove: the superconducting and tweezer bets are already made by dozens of devices and argue about *rates* (error per gate, qubits per year); the bosonic, topological and donor bets are made by one to seven machines and still argue about *existence* (does the protection hold at the second qubit, at the second module). Second, the best numbers sit on different architectures for different quantities — the largest device is a tweezer array, the best two-qubit error is an ion trap, the fastest clock (§7.4) is a transmon lattice — which is the empirical form of the Atlas's claim that no architecture dominates on all axes.\n\n" if en else
              "Два прочтения. Во-первых, ставки несимметричны в том, что им нужно доказать: сверхпроводниковая и пинцетная ставки уже сделаны десятками устройств и спорят о *темпах* (ошибка на гейт, кубиты в год); бозонные, топологическая и донорная сделаны одной–семью машинами и всё ещё спорят о *существовании* (держится ли защита на втором кубите, на втором модуле). Во-вторых, лучшие числа лежат в разных архитектурах для разных величин — крупнейшее устройство это массив пинцетов, лучшая двухкубитная ошибка — ионная ловушка, самый быстрый такт (§7.4) — трансмонная решётка, — что есть эмпирическая форма утверждения Атласа: ни одна архитектура не доминирует по всем осям.\n\n"))

    # ---------- 8.3.k the seventeen architectures, one narrative each (report/paths/<pid>.<lang>.md, written 26 Sep 2026) + the register's block
    o.append(("**The seventeen architectures, one by one.** Each subsection below is the argument of one architecture in five parts — the idea, what it needs, where it stands in the register, its exceptions and borrowings, and the next test — followed by the register's own block: the machines on the architecture grouped by organisation, and every cell that falls outside the architecture's slots (an alternate borrowed from another architecture, an Atlas gap, or `undisclosed` where the architecture expects a technology). The short name in the heading is the nickname the map's chips use.\n\n" if en else
              "**Семнадцать архитектур, одна за другой.** Каждый подраздел ниже — аргумент одной архитектуры в пяти частях: идея, что ей нужно, где она стоит по реестру, её исключения и заимствования, следующая проверка — и за ним блок реестра: машины архитектуры по организациям и каждая ячейка вне слотов архитектуры (альтернатива, заимствованная у другой архитектуры, пробел Атласа или `undisclosed` там, где архитектура ожидает технологию). Короткое имя в заголовке — прозвище, которым пользуются чипы карты.\n\n"))
    LAYNAME = {str(l['n']): l for l in G['layers']}
    for k, p in enumerate(G['paths'], 1):
        pid = p['id']; pm = [m for m in MS if m['map_path'] == pid]
        short = (p.get('short') or {}).get(L) or p[L]
        H(f"#### 8.3.{k} {short} — {p[L]} (`{pid}`)")
        pf = os.path.join(ROOT, 'report', 'paths', f'{pid}.{L}.md')
        if not os.path.exists(pf) and not en: pf = os.path.join(ROOT, 'report', 'paths', f'{pid}.en.md')
        if os.path.exists(pf):
            prose = open(pf, encoding='utf-8').read().strip()
            if '[@' in prose: raise SystemExit(f'report/paths/{pid}: unresolved citation placeholder — run build/paths_import.py')
            o.append(prose + "\n\n")
        else:
            o.append(("*(narrative pending)*\n\n" if en else "*(текст готовится)*\n\n"))
        # the register's block
        slots = {str(kk): set(v) for kk, v in p['slots'].items()}
        byorg = {}
        for m in sorted(pm, key=lambda m: (m['org'], -(m['q'] or 0), m['name'])): byorg.setdefault(m['org'], []).append(m)
        def mtag(m):
            sc = t(L, STATN.get(m['sc'], (m['sc'].lower(), m['sc'].lower())))
            q = f", {fmt_n(m['q'])}" if m['q'] else ''
            return f"{mdcell(m['name'])} ({sc}{q})"
        def olink(org, ms_):
            sl = _org_slug(ms_[0]) if ms_ else None
            return f"[**{mdcell(org)}**](organisation/{sl}.html)" if sl else f"**{mdcell(org)}**"
        orgs = '; '.join(olink(org, ms_) + " — " + ', '.join(mtag(m) for m in ms_) for org, ms_ in sorted(byorg.items(), key=lambda kv: (-len(kv[1]), kv[0])))
        ndev = sum(1 for m in pm if m['device']); ngate = sum(1 for m in pm if m['gatedev'])
        o.append((f"**Machines of this architecture (register: {len(pm)}, of them {ndev} devices, {ngate} gate-capable).** {orgs}.\n\n" if en else
                  f"**Машины этой архитектуры (реестр: {len(pm)}, из них {ndev} устройств, {ngate} с гейтами).** {orgs}.\n\n"))
        exc = []
        for m in pm:
            for ln, cells in sorted(m['layers'].items(), key=lambda kv: int(kv[0])):
                for c in cells:
                    stt = c.get('state', 'station'); n = c['node']
                    if stt == 'station' and n not in slots.get(ln, set()):
                        exc.append(f"{mdcell(m['name'])}: L{ln} {nm(n)} (`{n}`, " + t(L, ('alternate borrowed from another architecture', 'альтернатива из другой архитектуры') if c['role'] != 'primary' else ('primary off the architecture\'s slots', 'основная вне слотов архитектуры')) + ")")
                    elif stt == 'gap':
                        exc.append(f"{mdcell(m['name'])}: L{ln} `{n}` (" + t(L, ('Atlas gap', 'пробел Атласа')) + (f" — {mdcell(c.get('summary', ''))[:90]}" if c.get('summary') else '') + ")")
                    elif stt == 'undisclosed' and slots.get(ln) and c['role'] == 'primary':
                        exc.append(f"{mdcell(m['name'])}: L{ln} " + t(L, ('undisclosed where the architecture expects a technology', 'undisclosed там, где архитектура ожидает технологию')))
        if exc:
            o.append((f"*Cells outside the architecture's slots ({len(exc)}).* " if en else f"*Ячейки вне слотов архитектуры ({len(exc)}).* ") + '; '.join(exc) + ".\n\n")
        else:
            o.append(("*Cells outside the architecture's slots:* none — every cell of every machine sits in a slot of the architecture.\n\n" if en else "*Ячеек вне слотов архитектуры нет* — каждая ячейка каждой машины сидит в слоте архитектуры.\n\n"))

    # ---------- 8.4 hypotheses
    H("### 8.4 " + ("Trends — eight hypotheses tested on the register" if en else "Тренды — восемь гипотез, проверенных по реестру"))
    o.append(("Each hypothesis is a falsifiable statement about the population; the test is the computation named with it, run by the build on the register's current rows, under a rule printed with the test; the verdict is *supported*, *partly supported* or *not supported*, with the sample size. What each verdict rests on, and what would overturn it, is in §8.7. A hypothesis's wording and rule freeze when the edition is stamped as released; a changed claim takes a new number, and an old one is retired, never reworded — so that the verdict history at the end of this section, one row per edition with the register's size beside it, shows how a verdict drifts as the register grows.\n\n" if en else
              "Каждая гипотеза — фальсифицируемое утверждение о популяции; проверка — вычисление, названное рядом с ней и выполняемое сборкой по текущим строкам реестра по правилу, напечатанному вместе с проверкой; вердикт — *подтверждена*, *подтверждена частично* или *не подтверждена*, с размером выборки. На чём стоит каждый вердикт и что его опрокинуло бы — в §8.7. Формулировка и правило гипотезы замораживаются, когда издание получает штамп выпуска; изменённое утверждение получает новый номер, а старое отзывается, но не переписывается, — чтобы история вердиктов в конце этого раздела, по строке на издание с размером реестра рядом, показывала, как вердикт дрейфует с ростом реестра.\n\n"))
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
    H("**H1 — " + ("Physical qubit count has moved to the atoms; superconducting quantum computers no longer compete on count." if en else "Число физических кубитов ушло к атомам; сверхпроводниковые квантовые компьютеры больше не соперничают числом.") + "**")
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
    errs = {f: sorted([(m['err'], m['name'], claim_mark(m, L)) for m in dev if m['family'] == f and m['err'] is not None and not (m['flags'] & EXCL_ERR_FLAGS)]) for f in FAM_ORDER}
    emed = {f: median([x[0] for x in v]) for f, v in errs.items() if v}
    ebest = {f: v[0] for f, v in errs.items() if v}
    big3 = [f for f in ('SC', 'ION', 'ATOM') if f in emed]
    spread = (max(emed[f] for f in big3) / min(emed[f] for f in big3)) if big3 else None
    bestfam = min(ebest.items(), key=lambda kv: kv[1][0])[0] if ebest else None
    h2 = 'yes' if spread is not None and spread <= 2 and bestfam == 'ION' else ('part' if spread is not None and spread <= 3 else 'no')
    verdicts['H2'] = h2
    H("**H2 — " + ("Two-qubit error is converging across the three large families at the median, while the best single number stays with the ions." if en else "Двухкубитная ошибка сходится у трёх больших семейств по медиане, а лучшее единичное число остаётся у ионов.") + "**")
    o.append((f"*Test.* Median and best `err_2q_median` over devices per family, excluding hero-pair numbers, targets and component demonstrations. *Result.* " + '; '.join(f"{t(L, FAMN[f])} median {fmt_e(emed[f])}, best {fmt_e(ebest[f][0])} ({mdcell(ebest[f][1])}){ebest[f][2]}, n = {len(errs[f])}" for f in FAM_ORDER if f in emed) + f". The spread of the three large medians is ×{spread:.1f}. *Verdict:* {t(L, VER[h2])}. A convergence of medians with a persistent gap at the best is what one expects when the median is set by the many second-tier machines and the best by a few labs that have run the same platform for a decade. The verdict describes one snapshot of the register; whether the medians keep converging is a question for the next edition's cohorts, not for this one.\n\n" if en else
              f"*Проверка.* Медиана и лучшее значение `err_2q_median` по устройствам каждого семейства, исключая рекордные пары, цели и демонстрации компонентов. *Результат.* " + '; '.join(f"{t(L, FAMN[f])}: медиана {fmt_e(emed[f])}, лучшее {fmt_e(ebest[f][0])} ({mdcell(ebest[f][1])}){ebest[f][2]}, n = {len(errs[f])}" for f in FAM_ORDER if f in emed) + f". Разброс трёх больших медиан — ×{spread:.1f}. *Вердикт:* {t(L, VER[h2])}. Сходимость медиан при сохраняющемся разрыве в лучших значениях — то, чего ждёшь, когда медиану задают многочисленные машины второго ряда, а лучшее — несколько лабораторий, десятилетие работающих на одной платформе. Вердикт описывает один снимок реестра; сходятся ли медианы дальше — вопрос к когортам следующего издания, а не к этому.\n\n"))

    # Figure 8.1 — count against error (build/fig81.py), placed after H1 and H2, which it illustrates
    try:
        import fig81
        o.append(fig81.build(L)[0] + "\n")
    except Exception as e:   # the figure is an illustration; a failure here must not take the chapter down
        o.append(("*(Figure 8.1 could not be generated: %s)*\n\n" % e))
    # H3 — control stays external
    integ = [m for m in MS if m['cc'] == 'integrated']; cryo = [m for m in MS if m['cryo']]
    cc_f = {f: sum(1 for m in integ if m['family'] == f) for f in FAM_ORDER}
    big_sc_cryo = [m for m in dev if m['family'] == 'SC' and m['cryo'] and (m['q'] or 0) >= 100 and 'demo' not in (m['profile'].get('control_placement') or '').lower()]
    CRYO_FAMS = ('SC', 'SPIN', 'TOPO', 'ANNEAL')   # families whose machines live in a cryostat: the only ones where 'control outside the cryostat' is a constraint (roundtable, 28 Sep 2026)
    cryo_ms = [m for m in MS if m['family'] in CRYO_FAMS]
    ext = sum(1 for m in cryo_ms if m['cc'] in ('room', 'optics'))
    FIG.update(N=N, CTRL_EXT=ext, CTRL_CRYO_N=len(cryo_ms), CTRL_INTEG=len(integ))
    h3 = 'yes' if len(integ) <= N * 0.2 and not big_sc_cryo else ('part' if len(integ) <= N * 0.3 else 'no')
    verdicts['H3'] = h3
    H("**H3 — " + ("Control stays external: integrated control is a minority confined to spins, annealers and a few traps; no superconducting device of 100 qubits or more generates its microwave drive inside the cryostat — 4-K cryo-CMOS flux bias has run in hybrid with room-temperature RF on 156 qubits (Heron r2, Mar 2026)." if en else "Управление остаётся внешним: интегрированное управление — меньшинство, ограниченное спинами, отжигом и несколькими ловушками; ни одно сверхпроводниковое устройство от 100 кубитов не формирует СВЧ-сигналы внутри криостата — cryo-CMOS смещение потока при 4 K работало в гибриде с комнатным СВЧ на 156 кубитах (Heron r2, март 2026).") + "**")
    o.append((f"*Test.* The register's `control_placement` classified as room-temperature electronics, optics, integrated (on-chip microwave, cryo-CMOS, SFQ, flux DACs, 4 K) or undisclosed; the integrated class by family; superconducting devices ≥ 100 qubits with cryogenic control that is not a demo. *Result.* External {ext} of the {len(cryo_ms)} machines of the cryogenic families (superconducting, spin, topological, annealing); integrated {len(integ)} (" + ', '.join(f"{t(L, FAMN[f])} {cc_f[f]}" for f in FAM_ORDER if cc_f[f]) + f"), of which cryogenic {len(cryo)}; superconducting devices ≥ 100 qubits with non-demo cryogenic control: {len(big_sc_cryo)}. *Verdict:* {t(L, VER[h3])}. The attribute the map treats as the slow-moving one (§7.2: control placement) moves slowly in the register too: the integrated class is where the physics forces it — flux DACs on annealers, CMOS next to CMOS spins, microwave electrodes in surface traps — and a plan elsewhere.\n\n" if en else
              f"*Проверка.* Поле реестра `control_placement`, классифицированное как электроника при комнатной температуре, оптика, интегрированное (микроволны на чипе, cryo-CMOS, SFQ, потоковые ЦАП, 4 K) или не раскрыто; интегрированный класс по семействам; сверхпроводниковые устройства ≥ 100 кубитов с криогенным управлением не в статусе демонстрации. *Результат.* Внешнее {ext} из {len(cryo_ms)} машин криогенных семейств (сверхпроводники, спины, топологические, отжиг); интегрированное {len(integ)} (" + ', '.join(f"{t(L, FAMN[f])} {cc_f[f]}" for f in FAM_ORDER if cc_f[f]) + f"), из них криогенное {len(cryo)}; сверхпроводниковых устройств ≥ 100 кубитов с криогенным управлением не в статусе демонстрации: {len(big_sc_cryo)}. *Вердикт:* {t(L, VER[h3])}. Атрибут, который карта считает медленно меняющимся (§7.2: размещение управления), медленно меняется и в реестре: интегрированный класс есть там, где его вынуждает физика — потоковые ЦАП у отжига, CMOS рядом с CMOS-спинами, микроволновые электроды в поверхностных ловушках, — а в остальном это план.\n\n"))

    # H4 — QEC on hardware becomes the entry ticket
    codem = [m for m in MS if m['has_code']]
    codem_dev = [m for m in codem if m['device']]   # the code was run, not only named in a roadmap
    cohc = {}
    for m in MS:
        if m['year'] and 2023 <= m['year'] <= 2026:
            a = cohc.setdefault(m['year'], [0, 0]); a[1] += 1; a[0] += m['has_code']
    inloop = [m for m in MS if m['dc'] == 'in-loop']
    shares = [c[0] / c[1] for y, c in sorted(cohc.items())]
    rises = bool(shares) and shares[-1] > shares[0]                    # the last cohort's share above the first
    mono = bool(shares) and all(b >= a for a, b in zip(shares, shares[1:]))
    h4 = 'yes' if mono and len(inloop) >= 10 else ('part' if rises or len(inloop) >= 5 else 'no')
    FIG.update(CODE_LIST=len(codem), CODE_RUN=len(codem_dev), CODE_ROADMAP=len(codem) - len(codem_dev), INLOOP=len(inloop))
    share_txt = (("The share rises but not monotonically" if rises else "The cohort shares do not rise — the last cohort's share is below the first"), ("Доля растёт, но не монотонно" if rises else "Доля по когортам не растёт — у последней когорты она ниже, чем у первой"))
    verdicts['H4'] = h4
    H("**H4 — " + ("Running a code on the hardware is becoming the entry ticket: the share of new machines that have done so rises by cohort, and closed-loop decoding follows." if en else "Запуск кода на железе становится входным билетом: доля новых машин, которые это сделали, растёт по когортам, и замкнутое декодирование следует за ней.") + "**")
    o.append((f"*Test.* Machines with at least one code in the register's code table, by cohort 2023–2026; machines whose decoding is in the loop. *Rule.* Supported if the cohort share rises monotonically and ten or more machines decode in the loop; partly if the last cohort's share is above the first's, or five or more machines decode in the loop. *Result.* {len(codem)} of {N} machines list a code — {len(codem_dev)} of them devices that have run it, the rest announced or planned machines whose roadmap names one (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in codem if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in codem)) + "); share by cohort " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohc.items())) + f"; decoding in the loop: {len(inloop)} (" + ', '.join(mdcell(m['name']) for m in sorted(inloop, key=lambda m: m['name'])) + f"). *Verdict:* {t(L, VER[h4])}. {share_txt[0]}, and the loop is closed on a handful of machines: the entry ticket is a code *demonstration*, not yet a decoder in the cycle.\n\n" if en else
              f"*Проверка.* Машины хотя бы с одним кодом в таблице кодов реестра, по когортам 2023–2026; машины, у которых декодирование замкнуто в цикле. *Правило.* Подтверждено, если доля по когортам растёт монотонно и не менее десяти машин декодируют в цикле; частично — если доля последней когорты выше первой или не менее пяти машин декодируют в цикле. *Результат.* {len(codem)} из {N} машин указывают код — {len(codem_dev)} из них устройства, которые его запускали, остальные анонсированные или планируемые машины, чья дорожная карта его называет (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in codem if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in codem)) + "); доля по когортам " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohc.items())) + f"; декодирование в цикле: {len(inloop)} (" + ', '.join(mdcell(m['name']) for m in sorted(inloop, key=lambda m: m['name'])) + f"). *Вердикт:* {t(L, VER[h4])}. {share_txt[1]}, и цикл замкнут на считанных машинах: входной билет — *демонстрация* кода, а не декодер в такте.\n\n"))

    # H5 — modularity is a roadmap, not a machine (register schema of 26 Sep 2026: `none` = no interconnect at all;
    # in-module packaging and fan-out are technologies but not links; `undisclosed` and Atlas gaps counted apart)
    v9 = voidshare.get('9', (0, N)); u9 = undshare.get('9', (0, N)); g9 = gapshare.get('9', (0, N)); linked = [m for m in MS if m['link']]
    packed = [m for m in MS if m['l9'] == 'station' and not m['link']]
    worst = max(voidshare.items(), key=lambda kv: (kv[1][0], kv[0]))[0]
    nolink = v9[0] + u9[0] + g9[0] + len(packed)   # machines with no link between modules, whatever the reason
    FIG.update(IC_NONE=v9[0], IC_UNDISC=u9[0], IC_NONE_OR_UNDISC=v9[0] + u9[0], IC_NOLINK=nolink, IC_LINKED=len(linked))
    h5 = 'yes' if nolink >= 0.75 * N and len(linked) <= 0.25 * N else ('part' if nolink >= 0.5 * N else 'no')
    verdicts['H5'] = h5
    H("**H5 — " + ("Modularity is a roadmap, not a machine: a link between modules is the rarest thing in the register." if en else "Модульность — это дорожная карта, а не машина: связь между модулями — самое редкое, что есть в реестре.") + "**")
    o.append((f"*Test.* Primary interconnect cells (Table 8.2): machines with no interconnect at all (`none`), with packaging or fan-out inside one module but no link, with an undisclosed link, with a link the map has no technology for, and with a link technology between modules. *Result.* No interconnect {v9[0]} of {N} ({pct(v9[0], N)}); in-module packaging or fan-out only, {len(packed)}; undisclosed, {u9[0]}; an Atlas gap, {g9[0]}; a link technology between modules on {len(linked)} machines (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in linked if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in linked)) + f") — {nolink} of {N} ({pct(nolink, N)}) have no link between modules. The layer with the most `none` cells is {t(L, (LAYERS[worst]['en'], LAYERS[worst]['ru']))} ({voidshare[worst][0]}). *Verdict:* {t(L, VER[h5])}. This is a snapshot of the register, not a trend: every roadmap that reaches thousands of qubits assumes a link between modules; the register holds one on {len(linked)} machines, {sum(1 for m in linked if m['device'])} of them devices — the rest announced or planned. The layer where the architecture must go is the layer where it has least been.\n\n" if en else
              f"*Проверка.* Основные ячейки слоя межсоединений (таблица 8.2): машины вовсе без межсоединения (`none`), со сборкой или разводкой внутри одного модуля без связи, с нераскрытой связью, со связью, для которой у карты нет технологии, и со технологией связи между модулями. *Результат.* Без межсоединения {v9[0]} из {N} ({pct(v9[0], N)}); только сборка или разводка внутри модуля — {len(packed)}; не раскрыто — {u9[0]}; пробел Атласа — {g9[0]}; технологию связи между модулями несут {len(linked)} машин (" + ', '.join(f"{t(L, FAMN[f])} {sum(1 for m in linked if m['family']==f)}" for f in FAM_ORDER if any(m['family']==f for m in linked)) + f") — у {nolink} из {N} ({pct(nolink, N)}) связи между модулями нет. Больше всего ячеек `none` в слое «{t(L, (LAYERS[worst]['en'], LAYERS[worst]['ru']))}» ({voidshare[worst][0]}). *Вердикт:* {t(L, VER[h5])}. Это снимок реестра, а не тренд: каждая дорожная карта, доходящая до тысяч кубитов, предполагает связь между модулями; реестр держит её на {len(linked)} машинах, из них {sum(1 for m in linked if m['device'])} — устройства, остальные анонсированы или планируются. Слой, куда архитектура должна прийти, — слой, где её меньше всего было.\n\n"))

    # H6 — roadmaps fall short on error more than on qubits (the panel of 29 Sep 2026: the old wording "not on the qubit count"
    # contradicted its own table — most SHORT verdicts carry a qubit deficit too; what separates the two is size)
    R = M.get('roadmaps', [])
    rv = {}
    for r in R: rv[r['verdict']] = rv.get(r['verdict'], 0) + 1
    short = [r for r in R if r['verdict'] == 'SHORT']
    def _fac(txt, unit):
        m_ = re.search(r'x([\d\.,]+(?:e[\-+]?\d+)?) ' + unit + r'\b', txt)
        return float(m_.group(1).replace(',', '')) if m_ else None
    qd = [_fac(r['deficit'], 'q') for r in short]; ed = [_fac(r['deficit'], 'err') for r in short]
    both = [(a, b) for a, b in zip(qd, ed) if a and b]
    err_gt = sum(1 for a, b in both if b > a)                      # error deficit larger than the qubit deficit
    err_only = sum(1 for a, b in zip(qd, ed) if b and not a)       # error deficit with no qubit deficit
    qonly = sum(1 for a, b in zip(qd, ed) if a and not b)          # qubit deficit with no error deficit
    med_q = median([a for a in qd if a]) or 0; med_e = median([b for b in ed if b]) or 0
    nroad = len({r['roadmap_id'] for r in R})
    h6 = 'yes' if short and (err_gt + err_only) >= 0.7 * len(short) else ('part' if short and (err_gt + err_only) >= 0.5 * len(short) else 'no')
    verdicts['H6'] = h6
    FIG.update(H6_SHORT=len(short), H6_BOTH=len(both), H6_ERRGT=err_gt, H6_ERRONLY=err_only, H6_QONLY=qonly, H6_NOTEVAL=rv.get('NOT EVALUABLE', 0), H6_MEDQ=round(med_q), H6_MEDE=round(med_e))
    H("**H6 — " + ("Where a roadmap falls short of a target algorithm, its logical-error deficit exceeds its qubit deficit." if en else "Где дорожная карта не дотягивает до целевого алгоритма, её дефицит по логической ошибке больше дефицита по кубитам.") + "**")
    o.append((f"*Test.* The register's roadmap-feasibility table ({nroad} roadmaps × the target algorithms): the verdicts, and for every SHORT verdict the size of its qubit deficit and of its error deficit (each a factor). *Rule.* Supported if in seven SHORT rows out of ten the error deficit is the larger one or the only one; partly at five out of ten. *Result.* " + ', '.join(f"{k} {v}" for k, v in sorted(rv.items())) + f"; of the {len(short)} SHORT verdicts {len(both)} quantify both deficits and in {err_gt} of them the error deficit is the larger, {err_only} carry an error deficit only and {qonly} a qubit deficit only; median qubit deficit ×{med_q:,.0f}, median error deficit ×{med_e:,.0f}. *Verdict:* {t(L, VER[h6])}. Qubit counts are the roadmaps' own currency and they budget it generously, so the qubit deficit is a small factor; the logical error per operation and the gate count of the target algorithm are where the same roadmaps miss by one to eight orders of magnitude.\n\n" if en else
              f"*Проверка.* Таблица осуществимости дорожных карт реестра ({nroad} карт × целевые алгоритмы): вердикты и для каждого вердикта SHORT — размер дефицита по кубитам и по ошибке (каждый — множитель). *Правило.* Подтверждено, если в семи строках SHORT из десяти дефицит по ошибке больше дефицита по кубитам или единственный; частично — при пяти из десяти. *Результат.* " + ', '.join(f"{k} {v}" for k, v in sorted(rv.items())) + f"; из {len(short)} вердиктов SHORT {len(both)} количественно дают оба дефицита, и в {err_gt} из них дефицит по ошибке больше, {err_only} несут только дефицит по ошибке и {qonly} — только по кубитам; медианный дефицит по кубитам ×{med_q:,.0f}, по ошибке ×{med_e:,.0f}. *Вердикт:* {t(L, VER[h6])}. Число кубитов — собственная валюта дорожных карт, и её они закладывают щедро, так что дефицит по кубитам — малый множитель; логическая ошибка на операцию и число гейтов целевого алгоритма — то, где те же карты промахиваются на один–восемь порядков.\n\n"))
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
    o.append((f"*Test.* Share of announced or planned rows per cohort 2023–2026; retirements by family. *Result.* " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohs.items())) + "; retired: " + ', '.join(f"{t(L, FAMN[f])} {retf[f]}" for f in FAM_ORDER if retf[f]) + f". *Verdict:* {t(L, VER[h7])} — with the caveat that the newest cohort is a partial year and some of its announcements will become devices; the shape to watch is whether the share falls back as the year closes. \"Widens\" is read off the cohorts of one register snapshot, not off successive editions; the trend claim is tested when the 2026 cohort closes.\n\n" if en else
              f"*Проверка.* Доля анонсированных или запланированных строк по когортам 2023–2026; выведенные машины по семействам. *Результат.* " + ', '.join(f"{y} {pct(c[0], c[1])} ({c[0]}/{c[1]})" for y, c in sorted(cohs.items())) + "; выведены: " + ', '.join(f"{t(L, FAMN[f])} {retf[f]}" for f in FAM_ORDER if retf[f]) + f". *Вердикт:* {t(L, VER[h7])} — с оговоркой, что новейшая когорта — неполный год и часть её анонсов станет устройствами; следить надо за тем, упадёт ли доля к концу года. «Растёт» прочитано по когортам одного снимка реестра, а не по последовательным изданиям; заявление о тренде проверяется, когда закроется когорта 2026 года.\n\n"))

    # H8 — ideas converge across families (technology sharing)
    fam_by_node = {}
    for m in MS:
        for ln, cells in m['layers'].items():
            for c in cells:
                if c.get('state', 'gap' if c['gap'] else 'station') != 'station' or c['role'] != 'primary': continue
                fam_by_node.setdefault(c['node'], set()).add(m['family'])
    n_nodes = len(fam_by_node); n2 = sum(1 for v in fam_by_node.values() if len(v) >= 2); n3 = sum(1 for v in fam_by_node.values() if len(v) >= 3)
    shared3 = sorted([k for k, v in fam_by_node.items() if len(v) >= 3], key=lambda k: (-len(fam_by_node[k]), k))
    occ_alt = set(fam_by_node)
    for m in MS:
        for ln, cells in m['layers'].items():
            for c in cells:
                if c.get('state', 'gap' if c['gap'] else 'station') == 'station': occ_alt.add(c['node'])
    FIG.update(OCC=n_nodes, OCC_ALT=len(occ_alt), SHARED2=n2, SHARED3=n3)
    h8 = 'yes' if n2 >= 0.5 * n_nodes else ('part' if n2 >= 0.35 * n_nodes else 'no')
    verdicts['H8'] = h8
    H("**H8 — " + ("The families' ideas converge: a growing set of technologies is shared across families." if en else "Идеи семейств сходятся: растущее множество технологий делится между семействами.") + "**")
    o.append((f"*Test.* Technologies occupied in the primary role, counted by the number of families that occupy them. *Result.* {n_nodes} technologies occupied; {n2} by two families or more, {n3} by three or more (" + ', '.join(f"{nm(k)} `{k}` — {len(fam_by_node[k])}" for k in shared3) + f"). *Verdict:* {t(L, VER[h8])}. The families keep their own toolboxes; what they share is a *role* — mid-circuit readout, erasure conversion, a link between modules — filled by a different technology on each architecture. Convergence, where it exists, is at the level of the map's attributes (§7), not of its technologies — and \"growing\" is a hypothesis about editions, not a measurement on this snapshot, which gives one count.\n\n" if en else
              f"*Проверка.* Технологии, занятые в основной роли, посчитанные по числу занимающих их семейств. *Результат.* Занято {n_nodes} технологий; {n2} — двумя семействами и более, {n3} — тремя и более (" + ', '.join(f"{nm(k)} `{k}` — {len(fam_by_node[k])}" for k in shared3) + f"). *Вердикт:* {t(L, VER[h8])}. Семейства держат собственные наборы инструментов; общей у них оказывается *роль* — считывание в середине схемы, преобразование в стирания, связь между модулями, — которую в каждой архитектуре заполняет своя технология. Сходимость, где она есть, лежит на уровне атрибутов карты (§7), а не её технологий — а «растущее» есть гипотеза об изданиях, а не измерение на этом снимке, который даёт одно число.\n\n"))

    # ---------- verdict history (the panel of 29 Sep 2026): one row per edition, the register's size beside the verdicts;
    # data/hypotheses-history.json keeps the rows — a row is rewritten by the builds of its own edition until the edition is
    # stamped as released (editions.STATUS == 'release' freezes it); older rows are never touched
    HIST = os.path.join(ROOT, 'data', 'hypotheses-history.json')
    try:
        hist = json.load(open(HIST, encoding='utf-8'))
    except Exception:
        hist = {'note': 'verdict history of the hypotheses of §8.4, one row per edition; written by build/machines_chapter.py; a frozen row is never rewritten', 'editions': []}
    ed = str(M.get('edition') or '')
    nver = sum(m['evidence_counts']['verified'] for m in MS); ncel = sum(m['evidence_counts']['total'] for m in MS)
    try:
        import editions as _ed; _frozen = (_ed.STATUS == 'release')
    except Exception:
        _frozen = False
    row = {'edition': ed, 'machines': N, 'devices': len(dev), 'cells': ncel, 'verified_share': round(nver / ncel, 3) if ncel else None, 'verdicts': dict(verdicts), 'frozen': _frozen}
    cur = next((r for r in hist['editions'] if r.get('edition') == ed), None)
    if cur is None: hist['editions'].append(row)
    elif not cur.get('frozen'): cur.update(row)
    if en:
        with open(HIST, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(hist, fh, ensure_ascii=False, indent=1); fh.write('\n')
    H("**" + ("Verdict history — one row per edition" if en else "История вердиктов — по строке на издание") + "**")
    o.append(("| Edition | Machines | Devices | Evidence cells (verified) | " if en else "| Издание | Машин | Устройств | Ячеек свидетельств (проверено) | ") + ' | '.join(f"H{k}" for k in range(1, 9)) + " |\n|---|---|---|---|" + "---|" * 8 + "\n")
    VS = {'yes': ('supported', 'подтверждена'), 'part': ('partly', 'частично'), 'no': ('not', 'нет')}
    for r in hist['editions']:
        vs = r.get('verified_share'); vtxt = f"{r.get('cells', 0):,} ({round(100 * vs)} %)" if vs is not None else str(r.get('cells', '—'))
        o.append(f"| {r['edition']}{'' if r.get('frozen') else t(L, (' (beta)', ' (бета)'))} | {r['machines']} | {r['devices']} | {vtxt} | " + ' | '.join(t(L, VS.get(r['verdicts'].get(f'H{k}'), ('—', '—'))) for k in range(1, 9)) + " |\n")
    o.append("\n")
    o.append(("A row is written by the builds of its edition and frozen when the edition is stamped as released; a verdict that flips between editions is re-run on the old and the new rows apart, and the row's note names the cause — new machines, re-graded cells or a re-cut map.\n\n" if en else
              "Строка пишется сборками своего издания и замораживается, когда издание получает штамп выпуска; вердикт, сменившийся между изданиями, перепроверяется отдельно на старых и на новых строках, и примечание строки называет причину — новые машины, переоценённые ячейки или перекроенная карта.\n\n"))

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
    ion_lo = int(ion_2027 // 10 * 10) if ion_2027 else None
    # the range's ceiling is the first announced system above the trend that is due within the year (Superion 256 → 260), so that the
    # range and the falsifier agree (until 27 Sep 2026 the ceiling was the largest announcement, 10,000, 25× the 2028 range)
    _above = sorted(q for y, q, n in ann['ION'] if q > (ion_lo or 0) and y <= 2027)
    ion_hi = (int(-(-_above[0] // 10) * 10) if _above else (ion_lo or 0))
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
    mname = {m['id']: m['name'] for m in MS}; rorg = {r['roadmap_id']: r.get('org') for r in R}
    def due_label(rid):   # a reader-facing name for a roadmap row: the machine's name when the row is a machine, else the organisation and the id
        return mname.get(rid) or (f"{rorg.get(rid)} — {rid}" if rorg.get(rid) else rid)
    yr = lambda f: fr[f][-1][0] if fr[f] else None
    o.append((f"A hypothesis says what the register shows; a forecast predicts what the next register will show. Each forecast below names its indicator, its value today, the value expected one year on (September 2027) and two years on (September 2028), the basis — the historical series, the register's own announcements, or both — and a confidence; the wording is frozen when this edition is stamped as released (`data/forecast-ledger.json`, kept under its edition), and the edition that reaches each date scores it against that frozen text; a new forecast takes a new number. Two limits govern the confidence: the series are short (five to eight yearly points) and dated by press releases, so the forecasts are directional with ranges rather than point estimates; and announcements are discounted — the register's rows marked as never or not (yet) delivered ({', '.join(mdcell(m['name']) for m in MS if re.search(r'never|not delivered', m['status'], re.I))}) are the reminder that an announced machine is a forecast, not a device.\n\n" if en else
              f"Гипотеза говорит, что показывает реестр; прогноз предсказывает, что покажет следующий реестр. Каждый прогноз ниже называет свой индикатор, его значение сегодня, ожидаемое значение через год (сентябрь 2027) и через два (сентябрь 2028), основание — историческую серию, собственные анонсы реестра или и то и другое — и уверенность; формулировка замораживается, когда это издание получает штамп выпуска (`data/forecast-ledger.json`, хранимый под своим изданием), и издание, дошедшее до даты, оценивает её по этому замороженному тексту; новый прогноз получает новый номер. Уверенность ограничивают две вещи: серии коротки (пять–восемь годовых точек) и датированы пресс-релизами, так что прогнозы направленные, с диапазонами, а не точечные; и анонсы дисконтированы — строки реестра с пометкой «не поставлена» или «так и не поставлена» ({', '.join(mdcell(m['name']) for m in MS if re.search(r'never|not delivered', m['status'], re.I))}), напоминают, что анонсированная машина — это прогноз, а не устройство.\n\n"))
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
      t(L, (f"{ion_lo}–{ion_hi}: the historical ×{ion_rate:.2f}/yr gives ≈{fmt_n(round(ion_2027))} by 2027; the first announced system above it caps the range at {ion_hi}" if ion_rate else "—", f"{ion_lo}–{ion_hi}: историческое ×{ion_rate:.2f}/год даёт ≈{fmt_n(round(ion_2027))} к 2027; первая анонсированная система выше него ограничивает диапазон значением {ion_hi}" if ion_rate else "—")),
      t(L, ("200–400", "200–400")),
      t(L, (f"frontier series {fseries('ION')} — the family whose frontier last grew (2023, 2025); announced: {aseries('ION')}", f"серия фронта {fseries('ION')} — семейство, чей фронт рос последним (2023, 2025); анонсировано: {aseries('ION')}")), 'medium',
      t(L, (f"a trapped-ion device with entangling gates on more than {ion_hi} qubits by 2027.09, or the frontier still at {fmt_n(io_top)}", f"ионное устройство с перепутывающими гейтами более чем на {ion_hi} кубитов к 2027.09 — или фронт всё ещё на {fmt_n(io_top)}")))
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
    F('F3', t(L, ('machines that list a code (run, or named in the roadmap); decoders in the loop', 'машины, указывающие код (запущенный или названный в дорожной карте); декодеры в цикле')),
      f"{len(codem)} / {len(inloop)}",
      t(L, (f"≥ 55 machines with a code (cumulative series by cohort year {', '.join(f'{y} {v}' for y, v in cum.items() if y >= 2022)}; {len(codem) - cum[2026]} planned machines dated after 2026 lie outside it); 6–8 in the loop", f"≥ 55 машин с кодом (накопленная серия по годам когорт {', '.join(f'{y} {v}' for y, v in cum.items() if y >= 2022)}; {len(codem) - cum[2026]} планируемых машин с датами после 2026 вне серии); 6–8 в цикле")),
      t(L, (f"≥ 65 with a code; 8–12 in the loop ({len(planned_rt)} machines list real-time decoding as planned or intended: {', '.join(mdcell(m['name']) for m in sorted(planned_rt, key=lambda m: m['name']))}; half on time is the working assumption)", f"≥ 65 с кодом; 8–12 в цикле ({len(planned_rt)} машин заявляют декодирование в реальном времени как план: {', '.join(mdcell(m['name']) for m in sorted(planned_rt, key=lambda m: m['name']))}; рабочее допущение — половина в срок)")),
      t(L, (f"cumulative count of code-running machines by cohort (×{(cum[2026] / cum[2023]) if cum.get(2023) else 0:.1f} from 2023 to 2026) and the register's planned-decoding rows", f"накопленное число машин с кодом по когортам (×{(cum[2026] / cum[2023]) if cum.get(2023) else 0:.1f} с 2023 по 2026) и строки реестра с планируемым декодированием")), 'medium',
      t(L, ("fewer than 52 machines with a code, or fewer than 6 closed loops, in 2027.09", "менее 52 машин с кодом или менее 6 замкнутых циклов в 2027.09")))
    # F4 — links
    F('F4', t(L, ('devices with a demonstrated link technology (interconnect layer)', 'устройства с продемонстрированной технологией связи (слой межсоединений)')),
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
      f"{len(due)} " + t(L, ('roadmaps dated 2025–2028', 'карт с датами 2025–2028')) + ': ' + ', '.join(f"{mdcell(due_label(rid))} ({y})" for rid, y in due),
      t(L, ("the checkpoints dated 2026–2027 are scored; on H6's distribution (56 of 65 SHORT verdicts on error or gates) the expectation is that they miss on the error budget, not on qubits", "точки, датированные 2026–2027, оцениваются; по распределению H6 (56 из 65 вердиктов SHORT — по ошибке или гейтам) ожидание таково, что они промахнутся по бюджету ошибок, а не по кубитам")),
      t(L, ("the 2028 checkpoints are scored; at least two of three miss on the logical error per operation", "оцениваются точки 2028 года; как минимум две из трёх промахиваются по логической ошибке на операцию")),
      t(L, ("the register's roadmap-feasibility verdicts and their dates", "вердикты реестра об осуществимости дорожных карт и их даты")), 'medium',
      t(L, ("a dated checkpoint met on qubits, error and gate budget together", "датированная точка, выполненная одновременно по кубитам, ошибке и бюджету гейтов")))
    H("**" + ("Table 8.5 — the forecast ledger (scored one and two years on)" if en else "Таблица 8.5 — реестр прогнозов (оценивается через год и через два)") + "**")
    o.append(("| # | Indicator | Today (2026.09) | Expected at 2027.09 | Expected at 2028.09 | Basis | Confidence | Falsified if |" if en else
              "| # | Индикатор | Сегодня (2026.09) | Ожидание к 2027.09 | Ожидание к 2028.09 | Основание | Уверенность | Опровергнуто, если |") + "\n|---|---|---|---|---|---|---|---|\n")
    for r in ledger:
        o.append(f"| {r['id']} | {mdcell(r['indicator'])} | {mdcell(r['now'])} | {mdcell(r['e2027'])} | {mdcell(r['e2028'])} | {mdcell(r['basis'])} | {t(L, CONF[r['confidence']])} | {mdcell(r['falsified_if'])} |\n")
    o.append("\n")
    def _rate_txt(en_):
        xs = [(f, er[f]) for f in ('SC', 'ION', 'ATOM') if efr.get(f) and er.get(f) and len(efr[f]) > 2]
        if not xs: return ''
        lo = min(xs, key=lambda x: x[1]); hi = max(xs, key=lambda x: x[1])
        return (f"×{lo[1]:.2f} ({t(L, FAMN[lo[0]])}) to ×{hi[1]:.2f} ({t(L, FAMN[hi[0]])}) a year" if en_ else f"в ×{lo[1]:.2f} ({t(L, FAMN[lo[0]])}) — ×{hi[1]:.2f} ({t(L, FAMN[hi[0]])}) в год")
    def _lag_txt(en_):
        xs = [(f, lg[f]) for f in ('SC', 'ION', 'ATOM') if lg.get(f) is not None]
        return ', '.join(f"{t(L, FAMN[f])} {v}" for f, v in xs)
    o.append((f"Reading the ledger. The reliable part is the shape, not the digits: the count frontier of the two largest families has not moved for years while the announced frontier lies an order of magnitude above it (F1); the error frontier improves by {_rate_txt(True)} where the series has more than two points, and the medians reach the frontier's value with a lag of years ({_lag_txt(True)}) (F2); and the adoption curves — codes on hardware, links, integrated control — are set by the delivery of the machines the register already lists as planned, discounted by how often such rows have slipped (F3–F5). What the ledger cannot do is time a single machine; what it can do is be wrong in public, one edition later.\n\n" if en else
              f"Как читать реестр прогнозов. Надёжна форма, а не цифры: фронт числа кубитов у двух крупнейших семейств не двигался годами, тогда как анонсированный фронт лежит на порядок выше (F1); фронт ошибок улучшается {_rate_txt(False)}, где в серии больше двух точек, а медианы доходят до значения фронта с отставанием в годы ({_lag_txt(False)}) (F2); кривые принятия — коды на железе, связи, интегрированное управление — задаются поставкой машин, которые реестр уже числит запланированными, с дисконтом на то, как часто такие строки сползали (F3–F5). Чего реестр прогнозов не может — датировать отдельную машину; что может — оказаться неправым публично, одним изданием позже.\n\n"))
    if en:
        with open(os.path.join(ROOT, 'data', 'forecast-ledger.json'), 'w', encoding='utf-8', newline='\n') as fh:
            json.dump({'edition': M.get('edition'), 'written': 'by build/machines_chapter.py from the register of ' + str(src.get('register', '')), 'forecasts': ledger}, fh, ensure_ascii=False, indent=1); fh.write('\n')

    # ---------- 8.6 where the architecture goes
    H("### 8.6 " + ("Where the architecture is going" if en else "Куда идёт архитектура"))
    nsup = sum(1 for v in verdicts.values() if v == 'yes'); npart = sum(1 for v in verdicts.values() if v == 'part'); nno = sum(1 for v in verdicts.values() if v == 'no')
    def _empty(ln):
        a = voidshare.get(ln, (0, N)); b = undshare.get(ln, (0, N)); return pct(a[0] + b[0], N)
    o.append((f"Of the eight hypotheses, {nsup} are supported, {npart} partly and {nno} not. **From count to encoded qubits and links.** The three layers most often empty on a machine — code, decoder and interconnect, with no technology or an undisclosed one on {_empty('7')}, {_empty('8')} and {_empty('9')} of the machines — are the layers every fault-tolerant roadmap must fill (H4, H5, H6): the next generation of quantum computers will be judged by the logical error per cycle and by the link between modules, not by the count (H1). **A division of roles between families rather than a winner.** The largest devices are tweezer arrays, the best gate is an ion trap and the fastest clock a transmon lattice; the medians converge (H2) while the extremes stay apart; hardware stays within its family while codes and decoders cross the family lines (H8) — and the roadmaps assume many modules joined by links rather than one module grown large (H5). **The slow variable is control.** Integrated control is a necessity where the physics forces it and a plan elsewhere (H3); the map's placement attribute will move last. **The binding constraint is the error budget.** Roadmaps are short on qubits too (a median ×{med_q:,.0f}) but far more on error (×{med_e:,.0f}) (H6), so the machines that matter next are the ones that move the logical error per operation, whatever their qubit count.\n\n" if en else
              f"Из восьми гипотез {nsup} подтверждены, {npart} — частично, {nno} — нет. **От числа кубитов — к закодированным кубитам и связям.** Три слоя, чаще всего пустые у машины, — код, декодер и межсоединение: без технологии или с нераскрытой у {_empty('7')}, {_empty('8')} и {_empty('9')} машин — это слои, которые должна заполнить каждая отказоустойчивая дорожная карта (H4, H5, H6): следующее поколение квантовых компьютеров будут судить по логической ошибке на цикл и по связи между модулями, а не по числу (H1). **Разделение ролей между семействами, а не победитель.** Крупнейшие устройства — массивы пинцетов, лучший гейт — ионная ловушка, самый быстрый такт — трансмонная решётка; медианы сходятся (H2), крайние значения остаются врозь; железо остаётся внутри своего семейства, а коды и декодеры пересекают границы семейств (H8) — и дорожные карты предполагают много модулей, соединённых связями, а не один разросшийся модуль (H5). **Медленная переменная — управление.** Интегрированное управление — необходимость там, где его вынуждает физика, и план в остальных местах (H3); атрибут размещения на карте сдвинется последним. **Связывающее ограничение — бюджет ошибок.** Дорожные карты не дотягивают и по кубитам (медиана ×{med_q:,.0f}), но куда сильнее по ошибке (×{med_e:,.0f}) (H6), поэтому машины, которые важны дальше, — те, что сдвигают логическую ошибку на операцию, каково бы ни было их число кубитов.\n\n"))

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
        ('H1', f"{len(gdev)} " + t(L, ('gate-capable devices', 'устройств с гейтами')), t(L, ('status ∈ {deployed, demonstrated, retired}; no target/component/analog/no-gate flag', 'статус ∈ {в эксплуатации, продемонстрирована, выведена}; без флагов цели/компонента/аналога/без гейта')), t(L, ('register field `physical_qubits_num` (press-level for most machines)', 'поле реестра `physical_qubits_num` (для большинства машин — уровень прессы)')), t(L, ('a gate-capable median of another family above the atoms’, or a larger gate-capable device outside the atoms', 'медиана другого семейства по устройствам с гейтами выше атомной или крупнейшее устройство с гейтами не у атомов'))),
        ('H2', ', '.join(f"{t(L, FAMN[f])} {len(errs[f])}" for f in FAM_ORDER if errs[f]), t(L, ('devices; hero-pair, target and component numbers excluded', 'устройства; исключены рекордные пары, цели и компоненты')), t(L, ('register field `err_2q_median` (paper-level where a figure is cited, else press)', 'поле реестра `err_2q_median` (уровень статьи, где цитируется рисунок, иначе пресса)')), t(L, ('a family median more than ×2 from the others, or a non-ion best', 'медиана семейства дальше ×2 от остальных или лучшее значение не у ионов'))),
        ('H3', f"{N}", t(L, ('none (all rows); the ≥ 100-qubit clause on devices', 'нет (все строки); условие ≥ 100 кубитов — по устройствам')), t(L, ('control layer cells: ', 'ячейки слоя управления: ')) + eg('5'), t(L, ('integrated control on more than 30 % of machines, or a ≥ 100-qubit superconducting device driven cryogenically', 'интегрированное управление более чем у 30 % машин или сверхпроводниковое устройство ≥ 100 кубитов с криогенным управлением'))),
        ('H4', f"{sum(c[1] for c in cohc.values())} " + t(L, ('machines in cohorts 2023–2026', 'машин в когортах 2023–2026')), t(L, ('cohort = year of the status date', 'когорта = год даты статуса')), t(L, ('code layer cells: ', 'ячейки слоя кода: ')) + eg('7'), t(L, ('a falling share across three cohorts, or ten machines with a decoder in the loop', 'падающая доля на трёх когортах или десять машин с декодером в цикле'))),
        ('H5', f"{N}", t(L, ('primary cells only; none, undisclosed, gap and in-module packaging counted as “no link”', 'только основные ячейки; none, undisclosed, пробел и сборка внутри модуля считаются «нет связи»')), t(L, ('interconnect layer cells: ', 'ячейки слоя межсоединений: ')) + eg('9'), t(L, ('links between modules on a quarter of the machines', 'связи между модулями у четверти машин'))),
        ('H6', f"{len(R)} " + t(L, ('roadmap × algorithm rows', 'строк карта × алгоритм')), t(L, ('verdict = SHORT', 'вердикт = SHORT')), t(L, ('register table `roadmap-feasibility` (targets as published by the vendors)', 'таблица реестра `roadmap-feasibility` (цели, как опубликованы вендорами)')), t(L, ('the error deficit larger than the qubit deficit in fewer than half of the SHORT rows', 'дефицит по ошибке больше дефицита по кубитам менее чем в половине строк SHORT'))),
        ('H7', f"{sum(c[1] for c in cohs.values())} " + t(L, ('machines in cohorts 2023–2026', 'машин в когортах 2023–2026')), t(L, ('status ∈ {announced, planned}', 'статус ∈ {анонсирована, запланирована}')), t(L, ('register field `status` (press-level by nature)', 'поле реестра `status` (по природе — уровень прессы)')), t(L, ('the newest cohort’s share falling to the previous cohorts’ level', 'доля новейшей когорты, упавшая до уровня предыдущих'))),
        ('H8', f"{n_nodes} " + t(L, ('occupied technologies', 'занятых технологий')), t(L, ('primary role; none, undisclosed and gap cells excluded', 'основная роль; ячейки none, undisclosed и пробелы исключены')), t(L, ('all primary cells: ', 'все основные ячейки: ')) + f"{pct(vt, at)} ✅", t(L, ('half of the occupied technologies shared by two families or more', 'половина занятых технологий, делимая двумя и более семействами'))),
    ]
    for h, n_, filt, evg, over in rows:
        o.append(f"| {h} | {t(L, VER[verdicts[h]])} | {n_} | {filt} | {evg} | {over} |\n")
    o.append("\n")
    o.append((f"Limits. The cohort is the year of the register's status date, which mixes first light, general availability and the latest milestone; the classifiers are string rules over free-text fields, printed at the top of the chapter's generator in the Atlas's repository (`build/machines_chapter.py`) so that a reviewer can object to a rule rather than to a number; the population is the register's, which favours machines with an English-language document. {len(pressonly)} machines have no verified cell at all (press pages only) and enter the counts at press level: " + ', '.join(mdcell(x) for x in pressonly) + ". Every hypothesis is re-tested by each build; a verdict that flips between editions is itself a finding and will be reported in the changelog.\n\n" if en else
              f"Границы. Когорта — год даты статуса в реестре, смешивающий первый запуск, общую доступность и последнюю веху; классификаторы — строковые правила над свободным текстом, напечатанные в начале `build/machines_chapter.py`, чтобы рецензент мог возразить правилу, а не числу; популяция — реестровая, с перекосом к машинам, у которых есть документ на английском языке. {len(pressonly)} машин не имеют ни одной подтверждённой ячейки (только пресс-релизы) и входят в подсчёты на уровне прессы: " + ', '.join(mdcell(x) for x in pressonly) + ". Каждая гипотеза перепроверяется при каждой сборке; вердикт, изменившийся между изданиями, — сам по себе результат и будет отмечен в списке изменений.\n\n"))
    return ''.join(o)


if __name__ == '__main__':
    import sys
    lang = sys.argv[1] if len(sys.argv) > 1 else 'en'
    sys.stdout.write(sec_machines(lang))
