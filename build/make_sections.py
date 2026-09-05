# -*- coding: utf-8 -*-
import json, sys, re
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'data'))
import graph_data as gd
G=gd.compute()
NODE={n['id']:n for n in G['nodes']}
LAY={l['n']:l for l in G['layers']}
V=G['vocab']
def t(lang,pair): return pair[0] if lang=='en' else pair[1]
def aff(lang,x): return t(lang,V['AFF']['%g'%x])
def logt(x):
    if x is None: return '—'
    v=10**x
    if v>=1: return f"{v:.0f} s"
    if v>=1e-3: return f"{v*1e3:.3g} ms"
    if v>=1e-6: return f"{v*1e6:.3g} µs"
    return f"{v*1e9:.3g} ns"
def coordB(lang,n):
    b=n['b']; s=logt(b['t'])
    d=t(lang,V['DET'][b['det']])
    return f"{s}; {d}" if b['t'] is not None or b['det']!='na' else '—'
def coordC(lang,n):
    c=n['c']
    if not c: return '—'
    return f"{t(lang,V['MECH'][c['mech']])}; {logt(c['t'])}; {'destructive' if lang=='en' else 'разрушающее'}={('yes' if lang=='en' else 'да') if c['destr'] else ('no' if lang=='en' else 'нет')}; mid-circuit={('yes' if lang=='en' else 'да') if c['mid'] else ('no' if lang=='en' else 'нет')}"
def coordE(lang,n):
    e=n['e']
    if e['mod']=='none': return '—'
    return f"{t(lang,V['MOD'][e['mod']])} @ {t(lang,V['PLACE'][e['place']])}"
def coordF(lang,n): return ', '.join(t(lang,V['ERR'][x]) for x in n['f'])
def status(lang,n): return t(lang,V['STATUS'][n['status']])
def name(lang,n): return n[lang]
FAMS={'SC':('superconducting','сверхпроводники'),'ION':('ions','ионы'),'ATOM':('atoms','атомы'),'PHOTON':('photonics','фотоника'),'SPIN':('spins','спины'),'DEFECT':('defects','дефекты'),'TOPO':('topological','топологические'),'ANNEAL':('annealing','отжиг')}
def fams(lang,fs): return ', '.join(t(lang,FAMS[f]) for f in fs)
PATH={p['id']:p for p in G['paths']}

def sec9(lang):
    L=lang; en=(L=='en'); o=[]
    H=lambda s: o.append(s+"\n")
    H("## 9. " + ("The technology graph — nodes, coordinates, edges, and what the graph says on its own" if en else "Граф технологий — узлы, координаты, рёбра и что граф говорит сам"))
    H(("### 9.1 Construction rules\n\n"
       "**Nodes are technologies, not platforms.** A technology enters the graph if it is *self-contained* (replaceable without touching the rest of the stack) and *principled* (its replacement shifts at least one of the four outputs — error channel, clock, count-with-quality, scaling path — by an order of magnitude). A platform is a *path*: one node per layer through the ten-layer stack (carrier → encoding → gate mechanism → connectivity/transport → control → readout → code → decoder → interconnect → manufacturing). Alternates within a slot are listed; the first is the primary.\n\n"
       "**Seven coordinates per node (design space, stable):** (a) carrier-nature affinity on the natural ↔ fabricated spectrum (photon = natural particle in engineered modes; donor/defect = intermediate; carrier-agnostic = neutral); (b) the characteristic time the node imposes (log-scale) with the entangling flag deterministic / probabilistic-heralded; (c) measurement mechanism with time bound, destructiveness and mid-circuit capability; (d) mobility/connectivity mechanism; (e) control modality and placement (room temperature / 4 K / millikelvin / in-vacuum); (f) dominant error structure *as the code sees it*; (g) manufacturing technology. A coordinate is a property that does not move as records improve; anything that moves with records (fidelity, Λ, counts, cycle times, QBI stage, funding) is an **evaluation-space attribute** — dated, sourced, attached to the node, never used for position. Actors and goals are **annotations** on paths.\n\n"
       "**Five edge types:** *requires/provides* (inter-layer dependency; either-or dependencies are flagged and only count where realised in a path), *alternatives* (two technologies that can fill the same slot of a layer; the relation is symmetric and does not mean exclusion — a platform may combine both across modules or hierarchy levels, e.g. surface-code processing with gross-code memory), *conflicts* (the two work together only with a mitigating element or a change in a third layer; every conflict edge carries the mechanism, the measured price, the mitigation, a status — open / mitigated / bypassed — and a dated source, see 8.10), *transfers* (the same node in several platform paths), *defines* (node → one of the four outputs, each carrying a source, a date and a number).\n\n"
       "**Clock is not a coordinate.** Per path it is derived as the length of one syndrome-extraction round, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, where d₂ and d₁ are the two- and one-qubit gate layers of the path's code (from the code node), t_2Q and t_meas come from the gate and readout coordinates, t_1Q, t_move (transport between gate layers, mobile platforms only) and t_reset from standard records; the measured QEC cycle is shown next to it as a check. Two further clocks are derived from the same records: the *reaction time* (measurement → conditioned operation; the published loop where one exists, else readout + decode latency as a floor) and *operations per coherence* T₂/t_2Q, with the idle exposure per round t_round/T₂ compared against the measured idle error.\n\n"
       "**Off-diagonal test** *(the map's own term; \"off-diagonal\" is borrowed from matrix language, not from the literature of the field)*. Along the natural–fabricated axis, coordinates correlate: natural carriers default to optical room-temperature control, transport connectivity, loss-type errors, slow fluorescence readout, optical/MEMS assembly; fabricated carriers default to microwave/electrical room-temperature control, static nearest-neighbour wiring, Pauli/leakage errors, fast dispersive/charge readout, lithography. A node is *off-diagonal* when, in the path that uses it, it breaks that correlation: natural carrier + microwave control; fabricated + far connectivity; fabricated + erasure; fabricated + cold-stage control or decoding; solid-state carrier + photonic interconnect; natural + sub-µs gate; natural + ≤ 30 µs readout; natural + semiconductor/photonic-chip fabrication. **Hubs** are nodes whose dependency reach (own paths plus paths of nodes that require them) spans ≥ 3 carrier families, or ≥ 2 families for a technology that reached hardware in 2023 or later. **Empty slots** are nodes with no demonstrated technology, or path slots with nothing in them.\n\n"
       "**Validity criterion.** The graph must *reproduce* the promising directions of §5 as the set S = off-diagonal ∪ hubs ∪ empty slots — it does not receive them as input. The test is only as independent as the off-diagonal patterns, which encode the natural/fabricated correlation; its real information is in the residuals: prose claims the graph does not support, and graph findings the prose missed (§9.8)."
       ) if en else (
       "### 9.1 Правила построения\n\n"
       "**Узлы — технологии, а не платформы.** Технология входит в граф, если она *самостоятельна* (её можно заменить, не трогая остальной стек) и *принципиальна* (замена сдвигает хотя бы один из четырёх выходов — канал ошибок, такт, счёт кубитов с качеством, путь масштабирования — на порядок). Платформа — это *путь*: по одному узлу на слой через десятислойный стек (носитель → кодирование → механизм гейта → связность/транспорт → управление → считывание → код → декодер → интерконнект → производство). Альтернативы внутри слота перечислены; первая — основная.\n\n"
       "**Семь координат узла (пространство проектирования, стабильно):** (a) сродство носителя на спектре естественный ↔ изготовленный (фотон = естественная частица в изготовленных модах; донор/дефект = промежуточный; независимые от носителя = нейтральные); (b) характерное время, которое узел навязывает (лог-шкала), с признаком перепутывания детерминированное / вероятностное-heralded; (c) механизм измерения с нижней границей времени, деструктивностью и возможностью mid-circuit; (d) механизм подвижности/связности; (e) модальность управления и его размещение (комнатная / 4 K / милликельвины / в вакууме); (f) структура доминирующей ошибки *как её видит код*; (g) технология производства. Координата — свойство, которое не сдвигается с ростом рекордов; всё, что сдвигается (fidelity, Λ, счёт, такт, стадия QBI, финансирование), — **атрибут пространства оценки**: датированный, с источником, прикреплён к узлу и никогда не используется для позиционирования. Акторы и цели — **аннотации** на путях.\n\n"
       "**Пять типов рёбер:** *требует/обеспечивает* (межслойная зависимость; зависимости «одно из» помечены и учитываются только там, где реализованы в пути), *альтернативы* (две технологии, способные занять один и тот же слот слоя; отношение симметрично и не означает исключения — платформа может сочетать обе по модулям или уровням иерархии, например surface-код для обработки и gross-код для памяти), *конфликтует* (две технологии работают вместе только с элементом снятия или при изменении третьего слоя; каждое ребро конфликта несёт механизм, измеренную цену, способ снятия, статус — открыт / снят / обходится — и датированный источник, см. 8.10), *переносится* (один узел в нескольких платформенных путях), *определяет* (узел → один из четырёх выходов, с источником, датой и числом).\n\n"
       "**Такт — не координата.** Для каждого пути он выводится как длительность одного раунда извлечения синдрома, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, где d₂ и d₁ — число слоёв двух- и однокубитных гейтов в коде пути (из узла кода), t_2Q и t_meas — координаты гейта и считывания, а t_1Q, t_move (транспорт между слоями гейтов, только подвижные платформы) и t_reset — стандартные рекорды; измеренный цикл QEC показан рядом как проверка. Из тех же рекордов выводятся ещё два такта: *время реакции* (измерение → обусловленная операция; опубликованный контур, если есть, иначе считывание + задержка декодера как нижняя граница) и *операций на когерентность* T₂/t_2Q, а экспозиция простоя за раунд t_round/T₂ сравнивается с измеренной ошибкой простоя.\n\n"
       "**Тест на off-diagonal** *(собственный термин карты; «внедиагональный» заимствован из языка матриц, а не из литературы предмета)*. Вдоль оси естественный–изготовленный координаты коррелируют: у естественных носителей по умолчанию оптическое управление при комнатной температуре, транспортная связность, ошибки типа потерь, медленное флуоресцентное считывание, оптическая/MEMS-сборка; у изготовленных — СВЧ/электрическое управление при комнатной температуре, статическая NN-разводка, паулиевские ошибки и утечка, быстрое дисперсионное/зарядовое считывание, литография. Узел *off-diagonal*, если в использующем его пути он ломает эту корреляцию: естественный носитель + СВЧ-управление; изготовленный + дальняя связность; изготовленный + erasure; изготовленный + управление или декодирование в холодной ступени; твердотельный носитель + фотонный интерконнект; естественный + суб-мкс гейт; естественный + считывание ≤ 30 мкс; естественный + полупроводниковое/фотонно-чиповое производство. **Хабы** — узлы, чей охват зависимостей (собственные пути плюс пути узлов, которые их требуют) покрывает не менее трёх семейств носителей; для технологии, дошедшей до железа лишь в 2023 году или позже, порог — два семейства, потому что молодая технология ещё не успела распространиться. **Пустые слоты** — узлы без продемонстрированной технологии или слоты путей, в которых ничего нет.\n\n"
       "**Критерий валидности.** Граф должен *воспроизвести* перспективные направления §5 как множество S = off-diagonal ∪ хабы ∪ пустые слоты — он не получает их на вход. Тест независим ровно настолько, насколько независимы off-diagonal-паттерны, кодирующие корреляцию естественный/изготовленный; его реальная информация — в остатках: утверждения текста, которые граф не поддерживает, и находки графа, которые текст пропустил (§9.8)."))
    # 9.2 node table
    H("### 9.2 " + ("Node table (96 technologies × 7 coordinates)" if en else "Таблица узлов (96 технологий × 7 координат)"))
    H(("| # | Layer | Technology | (a) carrier affinity | (b) time · entangling | (c) readout | (d) mobility | (e) control · placement | (f) error structure | (g) manufacturing | status · since |" if en else
       "| # | Слой | Технология | (a) сродство носителя | (b) время · перепутывание | (c) считывание | (d) подвижность | (e) управление · размещение | (f) структура ошибки | (g) производство | статус · с года |")+"\n|---|---|---|---|---|---|---|---|---|---|---|")
    for i,n in enumerate(sorted(G['nodes'],key=lambda x:(x['layer'],-x['aff'],x['id'])),1):
        o.append(f"| {i} | {n['layer']} {t(L,(LAY[n['layer']]['en'],LAY[n['layer']]['ru']))} | **{name(L,n)}** `{n['id']}` | {aff(L,n['aff'])} | {coordB(L,n)} | {coordC(L,n)} | {t(L,V['MOB'][n['d']])} | {coordE(L,n)} | {coordF(L,n)} | {t(L,V['FAB'][n['g']])} | {status(L,n)} · {n['since'] if n['since']<2030 else '—'} |\n")
    o.append("\n")
    # 9.3 paths
    H("### 9.3 " + ("Platform paths through the stack (primary node per layer; alternates in brackets)" if en else "Пути платформ по слоям (основной узел на слой; альтернативы в скобках)"))
    hdr="| " + ("Path" if en else "Путь") + " | " + " | ".join(f"{l['n']} {t(L,(l['en'],l['ru']))}" for l in G['layers']) + " |"
    H(hdr+"\n|"+"---|"*(len(G['layers'])+1))
    for p in G['paths']:
        cells=[]
        for l in G['layers']:
            ids=p['slots'].get(l['n'],[])
            if not ids: cells.append("**∅**")
            else:
                pr=NODE[ids[0]]; s=f"{name(L,pr)}" + (" ✗" if pr['status']=='X' else "")
                if len(ids)>1: s+=" (" + "; ".join(name(L,NODE[i]) for i in ids[1:]) + ")"
                cells.append(s)
        o.append(f"| **{p[L]}** — {p['actors']} | " + " | ".join(cells) + " |\n")
    o.append("\n")
    # 9.4 derived clock
    def st(x,u="s"):
        if x is None: return "—"
        if u=="s":
            for k,f in (("s",1),("ms",1e-3),("µs",1e-6),("ns",1e-9)):
                if x>=f: return ("%.3g %s"%(x/f,k)).replace(".0 "," ")
            return "0"
        return "%.2g"%x
    H("### 9.4 " + ("Derived clocks per path — syndrome round, reaction time, operations per coherence" if en else "Выведенные такты по путям — раунд синдрома, время реакции, операций на когерентность"))
    H(("| Path | round of | d₂ | gates | transport | 1Q | readout | reset | **t_round** | limiter | measured cycle | reaction time (loop / floor) | T₂ | ops per coherence | idle exposure t_round/T₂ | idle measured |" if en else
       "| Путь | раунд кода | d₂ | гейты | транспорт | 1Q | считывание | сброс | **t_round** | ограничитель | измеренный цикл | время реакции (контур / граница) | T₂ | операций на когерентность | экспозиция простоя t_round/T₂ | простой измерен |")+"\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for p in G['paths']:
        r=p['round']; pp=r.get('parts',{}); c=p['coh']; rx=p['react']
        lim={'gates':('gates','гейты'),'transport':('transport','транспорт'),'1q':('1Q','1Q'),'readout':('readout','считывание'),'reset':('reset','сброс')}.get(r['limiter'])
        o.append(f"| {p[L]} | {r.get('code') or '—'} | {r.get('d2') or '—'} | {st(pp.get('gates'))} | {st(pp.get('transport'))} | {st(pp.get('1q'))} | {st(pp.get('readout'))} | {st(pp.get('reset'))} | **{st(r['total'])}** | {t(L,lim) if lim else '—'} | {p['cycle']} | {st(rx['loop'])} / {st(rx['floor'])} | {st(c['t2'])}{(' ('+c['t2_scope']+')') if c.get('t2_scope') and c['t2_scope']!='typical' else ''} | {('%.1e'%c['ops_per_coh']) if c['ops_per_coh'] else '—'} | {('%.1e'%c['idle_exposure']) if c['idle_exposure'] else '—'} | {('%.1e'%c['idle_measured']) if c['idle_measured'] else '—'} |\n")
    notes=[(p[L],"; ".join(p['round']['notes'])) for p in G['paths'] if p['round']['notes']]
    o.append("\n" + ("**Reading.** The round is a sum, not a maximum, so the limiter is the largest term, not the only one: on the superconducting path readout and reset together are two-thirds of the round, on the atom paths transport between gate layers is, on the QCCD ion path transport plus recooling is ~90%. Where the derived round sits below the measured cycle the difference is the gap between the *coordinate* (best published time for the mechanism) and the *device* (the cycle actually run) — on the superconducting path 0.65 µs against 1.1 µs, on the spin path the best 6 µs readout against the ~100 µs typically run. The idle exposure t_round/T₂ is a second check: on the superconducting path it predicts 0.7% per round against the 0.9% idle term in Google's measured error budget; on ions and atoms it is 10⁻⁴–10⁻⁷, which is why a millisecond clock costs those platforms time but not error. On the QCCD ion path the transport-plus-recooling primitives are the published H1 table (2020) — 9.7 ms derived against the 1–5 ms cycles reported for H2-class experiments, because the primitives have not been republished for H2/Helios and the derived value uses the colour code's eight layers. Reaction time is the quantity resource estimates assume (10 µs in the RSA-2048 estimate) and the one the map most often cannot fill: only the superconducting, atom and photonic paths have a published measurement-to-operation loop." if en else
       "**Чтение.** Раунд — сумма, а не максимум, поэтому ограничитель — наибольшее слагаемое, а не единственное: на сверхпроводниковом пути считывание и сброс вместе дают две трети раунда, на атомных — транспорт между слоями гейтов, на ионном QCCD-пути транспорт с повторным охлаждением — ~90%. Там, где выведенный раунд ниже измеренного цикла, разница — это зазор между *координатой* (лучшее опубликованное время механизма) и *устройством* (реально прогнанным циклом): на сверхпроводниковом пути 0.65 мкс против 1.1 мкс, на спиновом — лучшее считывание 6 мкс против типичных ~100 мкс. Экспозиция простоя t_round/T₂ — вторая проверка: на сверхпроводниковом пути она предсказывает 0.7% за раунд против 0.9% члена простоя в измеренном бюджете ошибок Google; у ионов и атомов она 10⁻⁴–10⁻⁷ — поэтому миллисекундный такт стоит этим платформам времени, но не ошибок. На ионном QCCD-пути примитивы транспорта и повторного охлаждения — опубликованная таблица H1 (2020): выведено 9.7 мс против 1–5 мс циклов, сообщённых для экспериментов класса H2, потому что примитивы для H2/Helios не переопубликованы, а выведенное значение берёт восемь слоёв цветового кода. Время реакции — величина, которую предполагают оценки ресурсов (10 мкс в оценке для RSA-2048), и та, которую карта чаще всего не может заполнить: опубликованный контур измерение → операция есть только у сверхпроводникового, атомного и фотонного путей.") + "\n\n")
    if notes:
        o.append(("Notes: " if en else "Примечания: ") + "; ".join(f"*{a}* — {b}" for a,b in notes) + ".\n\n")
    # 9.5 hubs
    H("### 9.5 " + ("Hubs — nodes with high cross-platform reach (the 'transfers' out-degree)" if en else "Хабы — узлы с высоким межплатформенным охватом (исходящая степень по «переносится»)"))
    H(("| Node | Layer | Families reached | Paths | Since | Reading |" if en else "| Узел | Слой | Охваченные семейства | Путей | С года | Прочтение |")+"\n|---|---|---|---|---|---|")
    READ={'cx_nn':("universal backbone (commodity)","универсальный каркас (commodity)"),'dec_mwpm':("universal backbone (commodity)","универсальный каркас (commodity)"),'ct_base':("shared by all solid-state spin-like carriers","общий для всех твердотельных спиновых носителей"),
          'fab_pic':("photonic-chip foundry pulled into ion traps, atom tweezers and transducers","PIC-фабрика втянута в ионные ловушки, атомные пинцеты и трансдьюсеры"),'ro_spd':("single-photon detection behind every photonic interconnect","детектирование одиночных фотонов за каждым фотонным интерконнектом"),
          'fab_cmos':("CMOS foundry: spins, cryo-CMOS, standard-fab ion traps, SC wiring","CMOS-фабрика: спины, cryo-CMOS, ионные ловушки со стандартных фабрик, SC-разводка"),'code_surface':("baseline code on three families","базовый код на трёх семействах"),
          'code_color':("transversal Cliffords + distillation on three families — a direction the prose under-weighted","трансверсальные Клиффорды + дистилляция на трёх семействах — направление, недооценённое текстом"),'code_magic':("non-Clifford resource on three families","не-клиффордов ресурс на трёх семействах"),
          'code_qldpc':("overhead reduction spreading from theory to ions/SC/photonics","снижение оверхеда, расходящееся из теории в ионы/SC/фотонику"),'dec_gpu':("platform-agnostic decoding layer (NVQLink)","платформенно-независимый слой декодирования (NVQLink)"),'dec_relaybp':("qLDPC decoder shared by SC, ions, photonics","qLDPC-декодер, общий для SC, ионов, фотоники"),
          'ro_erasure':("erasure detection transferring from atoms/photons into superconducting circuits","детекция erasure, переносимая из атомов/фотонов в сверхпроводниковые схемы"),'enc_dualrail':("erasure encoding shared by photonics and SC","erasure-кодирование, общее для фотоники и SC"),'enc_gkp':("grid encoding shared by microwave and optical modes","решёточное кодирование, общее для СВЧ и оптических мод"),
          'code_bosonic':("bosonic concatenation spanning SC and photonics","бозонная конкатенация, охватывающая SC и фотонику"),'code_erasure':("erasure-adapted codes on atoms and SC","erasure-адаптированные коды на атомах и SC"),'code_highrate':("high-rate transversal codes on atoms and ions","высокоскоростные трансверсальные коды на атомах и ионах"),
          'ct_cryocmos':("cold-stage control spreading from spins to SC (IBM/HRL)","управление в холодной ступени, расходящееся от спинов к SC (IBM/HRL)"),'cx_lr':("long-range couplers on SC and annealers","дальние couplers на SC и отжигателях"),'dec_nn':("neural decoders on SC and atoms","нейросетевые декодеры на SC и атомах"),'enc_omg':("metastable erasure encoding on atoms and ions","метастабильное erasure-кодирование на атомах и ионах")}
    for n in sorted([n for n in G['nodes'] if n['hub']],key=lambda x:(-x['reach_degree'],x['since'])):
        o.append(f"| **{name(L,n)}** `{n['id']}` | {n['layer']} | {fams(L,n['reach'])} | {len(n['paths'])} | {n['since'] if n['since']<2030 else '—'} | {t(L,READ.get(n['id'],('','')))} |\n")
    o.append("\n")
    # 9.6 off-diagonal
    H("### 9.6 " + ("Off-diagonal nodes — where the natural/fabricated correlation breaks" if en else "Off-diagonal узлы — где ломается корреляция естественный/изготовленный"))
    H(("| Node | Layer | Pattern | In paths | Why it matters |" if en else "| Узел | Слой | Паттерн | В путях | Почему важно |")+"\n|---|---|---|---|---|")
    WHY={'enc_dualrail':("erasure — a natural-world error class — engineered into a fabricated carrier; threshold ×4","erasure — класс ошибок естественного мира — инженерно внесён в изготовленный носитель; порог ×4"),
         'g_ryd':("a natural carrier with a 270 ns gate: the reason atoms compete at all","естественный носитель с гейтом 270 нс: причина, по которой атомы вообще конкурируют"),
         'g_elec':("removes lasers, the historic scaling blocker of ions; 8.4×10⁻⁵","убирает лазеры — исторический блокер масштабирования ионов; 8.4×10⁻⁵"),
         'cx_lr':("gives 2D lattices the degree-6 connectivity qLDPC needs","даёт 2D-решёткам связность степени 6, нужную qLDPC"),
         'cx_shuttle':("transport connectivity for a fabricated carrier — the spin route to non-local codes","транспортная связность для изготовленного носителя — спиновый путь к нелокальным кодам"),
         'ct_cryocmos':("control moves into the fridge: the I/O wall is the binding constraint at 10⁴ qubits","управление уходит в криостат: стена I/O — связывающее ограничение при 10⁴ кубитах"),
         'ct_sfq':("same, at millikelvin with nW/qubit; QP poisoning is the risk","то же при милликельвинах с нВт/кубит; риск — quasiparticle poisoning"),
         'ct_fluxdac':("annealer heritage: 10⁴ qubits on 200–300 lines (D-Wave's own figures disagree)","наследие отжигателей: 10⁴ кубитов на 200–300 линиях (собственные данные D-Wave расходятся)"),
         'ct_pic_trap':("optics of the fabricated world for a natural carrier; footprint ÷50 claimed","оптика изготовленного мира для естественного носителя; заявлено уменьшение габаритов в 50 раз"),
         'ct_ionlaser':("integrated photonics in the trap — the ion analogue of the same move","интегрированная фотоника в ловушке — ионный аналог того же хода"),
         'ct_ionmw':("~200 electronic sources for 1,000 ions instead of laser beams","~200 электронных источников на 1 000 ионов вместо лазерных лучей"),
         'ro_erasure':("the readout primitive behind every erasure code; 384 ns on transmons","примитив считывания за каждым erasure-кодом; 384 нс на трансмонах"),
         'code_erasure':("threshold 0.94% → 4.15%; the largest single lever on overhead","порог 0.94% → 4.15%; крупнейший одиночный рычаг для оверхеда"),
         'ic_mcm':("fabricated carriers reaching beyond one chip (chiplets, l-couplers)","изготовленные носители выходят за пределы одного чипа (чиплеты, l-couplers)"),
         'ic_cryolink':("30 m between fridges at 80% Bell — the microwave route to modularity","30 м между криостатами при 80% Bell — СВЧ-путь к модульности"),
         'ic_spinphoton':("solid-state spins reaching the network via photons","твердотельные спины выходят в сеть через фотоны"),
         'ic_transducer':("the missing link for optical modularity of superconducting machines — empty","недостающее звено оптической модульности сверхпроводниковых машин — пусто"),
         'fab_cmos':("ion traps from standard semiconductor fabs (Oxford Ionics, SkyWater)","ионные ловушки со стандартных полупроводниковых фабрик (Oxford Ionics, SkyWater)"),
         'ro_imgfast':("17.6 µs atom readout cuts the imaging term 30–50×, but the whole QEC round only ~2×","считывание атомов за 17.6 мкс сокращает вклад imaging в 30–50 раз, но весь раунд QEC — лишь примерно вдвое")}
    for n in [n for n in G['nodes'] if n['offdiag']]:
        pats='; '.join(t(L,V['OFFDIAG'][f]) for f in n['offdiag'])
        o.append(f"| **{name(L,n)}** `{n['id']}` | {n['layer']} | {pats} | {', '.join(PATH[p][L] for p in n['offdiag_paths'])} | {t(L,WHY.get(n['id'],('','')))} |\n")
    o.append("\n")
    # 9.7 empty slots
    H("### 9.7 " + ("Empty slots — where a technology does not exist yet" if en else "Пустые слоты — где технологии ещё нет"))
    H(("| Slot | Status | What would fill it | Best today vs needed |" if en else "| Слот | Статус | Что должно его заполнить | Лучшее сегодня vs необходимое |")+"\n|---|---|---|---|")
    GAPS=[('ic_transducer',("η_tot 15%, N_add 0.16 vs η > 1/2, N_add ≪ 1; ~3 orders of magnitude (IBM)","η_tot 15%, N_add 0.16 против η > 1/2, N_add ≪ 1; ~3 порядка (IBM)")),
          ('dec_cryo',("designs only (NISQ+ 20 ns, QECOOL 2.8 µW); no fabricated decoder chip","только дизайны (NISQ+ 20 нс, QECOOL 2.8 мкВт); ни одного изготовленного чипа"),),
          ('g_catcnot',("theory proposal Jul 2026; every cat resource estimate assumes it","теоретическое предложение июль 2026; каждая оценка ресурсов для кошек его предполагает")),
          ('src_resource',("8-photon states at < 1 Hz vs 24–168-photon encoded resource states at MHz","8-фотонные состояния при < 1 Гц против 24–168-фотонных кодированных ресурсных состояний на МГц")),
          ('g_mbq',("single-wire parity readout only; no X-lifetime ≈ Z, no two-qubit operation","только считывание чётности одной проволоки; нет времени жизни X ≈ Z, нет двухкубитной операции"))]
    for nid,gap in GAPS:
        n=NODE[nid]; o.append(f"| **{name(L,n)}** `{nid}` ({n['layer']}) | {status(L,n)} | {n['desc'][L]} | {t(L,gap)} |\n")
    SLOTGAP={('spin_qd',9):("an interconnect for quantum-dot spins (spin–photon in dots is lab-only)","интерконнект для спинов в квантовых точках (спин-фотон в точках — только лаборатория)"),('spin_donor',9):("interconnect for donor spins","интерконнект для донорных спинов"),
             ('defect',7):("a code for network nodes (memory/repeater codes are theory)","код для узлов сети (коды памяти/повторителей — теория)"),('defect',8):("—","—"),('topo',7):("Floquet / measurement-based codes on a demonstrated qubit","Floquet / measurement-based коды на продемонстрированном кубите"),('topo',8):("—","—"),('topo',9):("—","—"),
             ('anneal',2):("no encoding — analog Hamiltonian, not a qubit register","нет кодирования — аналоговый гамильтониан, не регистр кубитов"),('anneal',7):("no error correction in annealing","в отжиге нет коррекции ошибок"),('anneal',8):("—","—"),('anneal',9):("—","—")}
    for e in G['empty_slots']:
        if e.get('only'): continue
        k=(e['path'],e['layer']); o.append(f"| {PATH[e['path']][L]} — {t(L,(LAY[e['layer']]['en'],LAY[e['layer']]['ru']))} | ∅ | {t(L,SLOTGAP.get(k,('','')))} | — |\n")
    # additional numeric gaps (attributes on existing nodes)
    o.append("\n"+("Numeric gaps on existing nodes (attribute-level, not empty slots): ion–photon links at 10–250 s⁻¹ vs ≥ 10⁴ s⁻¹ needed; photonic switch loss 100–190 mdB vs ~7 mdB; optical GKP effective squeezing 0.62 dB vs 9.75 dB; cat phase-flip ~10⁻¹ per CX vs 10⁻³ assumed; spin readout 6 µs at 99.2% vs sub-µs at 99.9% for a µs-class cycle; atom imaging 0.5–1 ms typical vs 17.6 µs emerging." if en else
       "Числовые пробелы на существующих узлах (уровень атрибутов, не пустые слоты): ион-фотонные линки 10–250 с⁻¹ против ≥ 10⁴ с⁻¹; потери фотонных переключателей 100–190 мдБ против ~7 мдБ; эффективное оптическое сжатие GKP 0.62 дБ против 9.75 дБ; phase-flip кошек ~10⁻¹ на CX против заложенных 10⁻³; считывание спинов 6 мкс при 99.2% против суб-мкс при 99.9% для цикла класса мкс; imaging атомов 0.5–1 мс типично против формирующихся 17.6 мкс.")+"\n\n")
    # 9.8 validity
    H("### 9.8 " + ("Validity check — does the graph reproduce §5 on its own?" if en else "Проверка валидности — воспроизводит ли граф §5 самостоятельно?"))
    H(("| Direction (from §5) | Defining nodes | In S | Missing | Coverage |" if en else "| Направление (из §5) | Определяющие узлы | В S | Отсутствуют | Покрытие |")+"\n|---|---|---|---|---|")
    for k,v in G['validity']['directions'].items():
        o.append(f"| {k} | {len(v['hit'])+len(v['miss'])} | {', '.join('`'+x+'`' for x in v['hit'])} | {', '.join('`'+x+'`' for x in v['miss']) or '—'} | **{v['coverage']:.2f}** |\n")
    nov=[x for x in G['validity']['novel']]
    o.append("\n"+(f"S has {G['validity']['S_size']} nodes. All eleven directions are reproduced with coverage 1.00. **Residuals:** (i) the prose also called *diagonal* enablers promising — atom transport, algorithmic FT, correlated decoding, Yb/Sr atoms, QCCD, MEMS traps, ion–photon links (§9.1 lists them as `diagonal_enablers`); the graph classifies these as native strengths of a family, not cross-platform directions — a useful distinction the prose blurred. (ii) The graph flags nodes the prose did not name as directions: {', '.join('`'+x+'`' for x in nov)} — the colour code (transversal Cliffords + distillation on three families), the surface-code/NN-lattice/MWPM/baseband backbone (commodities every family shares; not a direction, but the graph's honest picture of where the stack is standardised), and two empty slots (Majorana measurement-based gate; multi-photon resource-state factory) that belong on the watch-list. (iii) The photonic-interconnect direction is reproduced through its *dependencies* (PIC foundry, single-photon detectors, transducer), not through photonic-link nodes themselves — i.e. the prose's claim 'photonics is the interconnect for everyone' is, in graph terms, 'every family now depends on the photonic supply chain'." if en else
       f"В S — {G['validity']['S_size']} узлов. Все одиннадцать направлений воспроизведены с покрытием 1.00. **Остатки:** (i) текст называл перспективными и *диагональные* энейблеры — транспорт атомов, алгоритмическую FT, коррелированное декодирование, атомы Yb/Sr, QCCD, MEMS-ловушки, ион-фотонные линки (§9.1 перечисляет их как `diagonal_enablers`); граф классифицирует их как нативные сильные стороны семейства, а не кросс-платформенные направления — полезное различение, которое текст размывал. (ii) Граф помечает узлы, которые текст не называл направлениями: {', '.join('`'+x+'`' for x in nov)} — colour code (трансверсальные Клиффорды + дистилляция на трёх семействах), каркас surface code/NN-решётка/MWPM/baseband (commodities, общие для всех семейств; не направление, но честная картина того, где стек стандартизирован) и два пустых слота (майорановский гейт через измерения; фабрика многофотонных ресурсных состояний), которым место в списке наблюдения. (iii) Направление «фотонный интерконнект» воспроизведено через *зависимости* (PIC-фабрика, детекторы одиночных фотонов, трансдьюсер), а не через сами узлы фотонных линков — т.е. утверждение текста «фотоника — интерконнект для всех» в терминах графа означает «каждое семейство теперь зависит от фотонной цепочки поставок».")+"\n\n")
    # 9.9 representation
    H("### 9.9 " + ("How a 7-coordinate, 5-edge-type graph is best shown — and why the map is dynamic" if en else "Как лучше показывать граф с 7 координатами и 5 типами рёбер — и почему карта динамическая"))
    o.append(("Options weighed: a force-directed layout (rejected — it destroys the layer semantics and makes the stack unreadable); an adjacency matrix (right for the dense *requires* relation but wrong for a narrative reader — kept as a table); a chord diagram (rejected — no layers); 3D (rejected — occlusion). The chosen form is a **layered map in the metro-map idiom**: the ten layers are columns; the vertical position inside a column is the node's carrier-nature affinity, so the natural/fabricated *diagonal* becomes literally visible and off-diagonal nodes sit where a warm path dips into the cool half or vice versa; platform paths are coloured lines through their stations; a station on several lines is an interchange — the *transfers* degree at a glance; empty slots are hollow dashed stations. Coordinates cannot all be painted at once (one hue channel is all a reader has), so the map carries a **lens** that recolours every station by one coordinate at a time, and a **parallel-coordinates strip** shows the full seven-vector of every node as a polyline; a **node inspector** keeps the three spaces physically apart — design coordinates, dated evaluation attributes, actors/goals. Edges of type *requires / alternatives / conflicts* are drawn only on focus (degree-of-interest), because 96 nodes × 160 edges is a hairball; *defines* edges live in the inspector as dated rows, not lines. **Dynamic is necessary, static is mandatory:** the resting frame is a complete readable map (all paths, all stations) that prints and thumbnails; the interaction adds lenses, focus and filters without which five edge types cannot be read. The equivalent static artefacts — the tables of §9.2–9.8 — are the print fallback." if en else
       "Взвешенные варианты: force-directed раскладка (отвергнута — уничтожает семантику слоёв и делает стек нечитаемым); матрица смежности (правильна для плотного отношения *требует*, но неверна для читателя-нарратива — оставлена как таблица); хордовая диаграмма (отвергнута — нет слоёв); 3D (отвергнуто — окклюзия). Выбранная форма — **слоистая карта в идиоме схемы метро**: десять слоёв — колонки; вертикальная позиция внутри колонки — сродство носителя, так что *диагональ* естественный/изготовленный становится буквально видимой, а off-diagonal узлы стоят там, где тёплая линия ныряет в холодную половину или наоборот; пути платформ — цветные линии через свои станции; станция на нескольких линиях — пересадочная — степень «переносится» с одного взгляда; пустые слоты — полые пунктирные станции. Все координаты нельзя закрасить одновременно (у читателя один канал оттенка), поэтому у карты есть **линза**, перекрашивающая станции по одной координате за раз, и **лента параллельных координат**, показывающая полный семимерный вектор каждого узла как ломаную; **инспектор узла** физически разводит три пространства — координаты проектирования, датированные атрибуты оценки, акторы/цели. Рёбра типов *требует / альтернативы / конфликтует* рисуются только в фокусе (degree-of-interest), потому что 96 узлов × 160 рёбер — это клубок; рёбра *определяет* живут в инспекторе датированными строками, а не линиями. **Динамика необходима, статика обязательна:** кадр покоя — полная читаемая карта (все пути, все станции), пригодная для печати и миниатюры; интерактив добавляет линзы, фокус и фильтры, без которых пять типов рёбер не прочесть. Эквивалентные статические артефакты — таблицы §9.2–9.8 — резерв для печати.")+"\n\n")
    # 9.10 edge list
    H("### 9.10 " + ("Edge list" if en else "Список рёбер"))
    for et,title in (("requires",("requires / provides","требует / обеспечивает")),("replaces",("alternatives (within layer)","альтернативы (внутри слоя)")),("conflicts",("conflicts","конфликтует"))):
        H("**"+t(L,title)+"**\n")
        if et=="conflicts":
            H(("| From | To | Mechanism | Measured price | Mitigation | Status · source |" if en else "| От | К | Механизм | Измеренная цена | Снятие | Статус · источник |")+"\n|---|---|---|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {e[L]} | {e['price'][L]} | {e['mitig'][L]} | {t(L,V['CONSTAT'][e['status']])} · [{e['date']}]({e['url']}) |\n")
        else:
            H(("| From | To | Note |" if en else "| От | К | Примечание |")+"\n|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {e[L]}{' *(one-of)*' if e.get('any') else ''} |\n")
        o.append("\n")
    H("**"+("transfers (node → additional platform paths)" if en else "переносится (узел → дополнительные платформенные пути)")+"**\n")
    H(("| Node | Paths |" if en else "| Узел | Пути |")+"\n|---|---|")
    for n in G['nodes']:
        if len(n['paths'])>1: o.append(f"| `{n['id']}` {name(L,n)} | {', '.join(PATH[p][L] for p in n['paths'])} |\n")
    o.append("\n")
    H("**"+("defines (node → output; every row carries a source, a date and a number)" if en else "определяет (узел → выход; каждая строка несёт источник, дату и число)")+"**\n")
    H(("| Node | Output | Metric | Value | Date | Source |" if en else "| Узел | Выход | Метрика | Значение | Дата | Источник |")+"\n|---|---|---|---|---|---|")
    for e in G['edges']:
        if e['type']=='defines':
            o.append(f"| `{e['src']}` | {t(L,V['OUT'][e['dst']])} | {e['metric']} | {e['value']} | {e['date']} | {e['url']} |\n")
    o.append("\n")
    # 9.11 standard records
    H("### 9.11 " + ("Standard records — the dated numbers behind the derived clocks (nulls are honest: not published)" if en else "Стандартные рекорды — датированные числа за выведенными тактами (пустые — честно: не опубликовано)"))
    RK=G['vocab']['RECKEYS']
    H(("| Node | Quantity | Value | Scope | Date | Source · tag |" if en else "| Узел | Величина | Значение | Охват | Дата | Источник · тег |")+"\n|---|---|---|---|---|---|")
    def sv(r):
        if r['num'] is None: return ("*not published*" if en else "*не опубликовано*") + (" — "+r['note'] if r.get('note') else "")
        u=r['unit']
        if u=='s': return st(r['num'])
        if u=='Hz': return "%.2g Hz"%r['num']
        if u=='count': return "%g"%r['num']
        return "%.3g"%r['num']
    for n in G['nodes']:
        for r in n.get('records',[]):
            o.append(f"| `{n['id']}` | {t(L,RK[r['key']])} | {sv(r)} — {r['text']} | {r['scope']} | {r['date']} | {r['url']} · [{r['tag']}] |\n")
    o.append("\n")
    return ''.join(o)

json.dump(G,open(os.path.join(ROOT,'data','graph.json'),'w',encoding='utf-8'),ensure_ascii=False)
# splice the generated graph section (numbered 7 in the public edition) into the reports
def splice(lang,start,end):
    p=os.path.join(ROOT,'report','report_%s.md'%lang.upper()); s=open(p,encoding='utf-8').read()
    sec=sec9(lang); sec=re.sub(r'^(#+ )9(\.\d*)',r'\g<1>7\2',sec,flags=re.M).replace('## 9. ','## 7. ',1)
    sec=re.sub(r'(see|см\.) 8\.(\d+)',r'\1 7.\2',sec); sec=re.sub(r'§9(\.\d+)',r'§7\1',sec); sec=re.sub(r'§8(\.\d+)?',lambda m:'§7'+(m.group(1) or ''),sec); sec=re.sub(r'§9(?!\.)','§8',sec)
    i=s.find(start); j=s.find(end); k=s.rfind('\n---\n',i,j)
    if i<0 or j<0: raise SystemExit('report %s: section markers not found'%lang)
    open(p,'w',encoding='utf-8').write(s[:i]+sec.rstrip()+'\n'+s[k:])
splice('en','## 7. The technology graph','## 8. Sources'); splice('ru','## 7. Граф технологий','## 8. Источники')
print('sec9 written', len(sec9('en').split()), len(sec9('ru').split()))
