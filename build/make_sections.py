# -*- coding: utf-8 -*-
import json, sys, re
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'data'))
import graph_data as gd
sys.path.insert(0,os.path.join(ROOT,'build'))
import machines_chapter as mc

SIGDIGITS=6
def determinize(x,sig=SIGDIGITS):
    """Round every float to `sig` significant digits so the build is byte-reproducible.

    The derived clocks (t_round and friends) are sums and products of doubles. Their last
    bit depends on summation order and on the platform's libm, so the same source data
    yields values one ULP apart on different machines — enough to make dist/ differ and
    the identity check before publication fail for no substantive reason.

    Six digits sits between the two scales that matter. It discards perturbations of
    order 1e-16 (the ULP noise) while itself perturbing a value by at most 5e-6 in
    relative terms, and the document never shows more than three significant digits
    (%.3g, %.2g, %.1e), i.e. a resolution of 5e-4. So nothing printed can move, and a
    rounded value can straddle its own boundary only if two platforms disagree at the
    sixth digit — eleven orders of magnitude beyond the noise they actually produce."""
    if isinstance(x,float): return x if x!=x or x in (float('inf'),float('-inf')) else float('%.*g'%(sig,x))
    if isinstance(x,dict): return {k:determinize(v,sig) for k,v in x.items()}
    if isinstance(x,list): return [determinize(v,sig) for v in x]
    return x

G=determinize(gd.compute())
NODE={n['id']:n for n in G['nodes']}
LAY={l['n']:l for l in G['layers']}
V=G['vocab']
def t(lang,pair): return pair[0] if lang=='en' else pair[1]
def mdcell(x):
    """Free text inside a markdown table cell: a bare `|` (e.g. `|0>,|1>`) would split the row, so escape it as `\\|`."""
    return str(x).replace('|','\\|') if x is not None else x
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
    ps=e['place'] if isinstance(e['place'],list) else [e['place']]   # list-valued since 17 Sep 2026: every stage, in the vocabulary's order (RT → 4 K → mK)
    ps=[p for p in V['PLACE'] if p in ps]+[p for p in ps if p not in V['PLACE']]
    return f"{t(lang,V['MOD'][e['mod']])} @ {' / '.join(t(lang,V['PLACE'][p]) for p in ps)}"
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
       "**Seven coordinates per node (design space, stable):** (a) carrier-nature affinity on the natural ↔ fabricated spectrum (photon = natural particle in engineered modes; donor/defect = intermediate; carrier-agnostic = neutral); (b) the characteristic time the node imposes (log-scale) with the entangling flag deterministic / probabilistic-heralded; (c) measurement mechanism with time bound, destructiveness and mid-circuit capability; (d) mobility/connectivity mechanism; (e) control modality and placement (temperature stage: room temperature / 4 K / millikelvin; a node may carry several, the first being primary); (f) dominant error structure *as the code sees it*; (g) manufacturing technology. A coordinate is a property that does not move as records improve; anything that moves with records (fidelity, Λ, counts, cycle times, QBI stage, funding) is an **evaluation-space attribute** — dated, sourced, attached to the node, never used for position. Actors and goals are **annotations** on paths.\n\n"
       "**Five edge types:** *requires/provides* (inter-layer dependency; either-or dependencies are flagged and only count where realised in a path), *alternatives* (two technologies that can fill the same slot of a layer; the relation is symmetric and does not mean exclusion — a platform may combine both across modules or hierarchy levels, e.g. surface-code processing with gross-code memory), *conflicts* (the two work together only with a mitigating element or a change in a third layer; every conflict edge carries the mechanism, the measured price, the mitigation, a status — open / mitigated / bypassed — and a dated source, see 8.10), *transfers* (the same node in several platform paths), *defines* (node → one of the four outputs, each carrying a source, a date and a number).\n\n"
       "**Clock is not a coordinate.** Per path it is derived as the length of one syndrome-extraction round, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, where d₂ and d₁ are the two- and one-qubit gate layers of the path's code (from the code node), t_2Q and t_meas come from the gate and readout coordinates, t_1Q, t_move (transport between gate layers, mobile platforms only) and t_reset from standard records; the measured QEC cycle is shown next to it as a check. Two further clocks are derived from the same records: the *reaction time* (measurement → conditioned operation; the published loop where one exists, else readout + decode latency as a floor) and *operations per coherence* T₂/t_2Q, with the idle exposure per round t_round/T₂ compared against the measured idle error.\n\n"
       "**Off-diagonal test** *(the map's own term; \"off-diagonal\" is borrowed from matrix language, not from the literature of the field)*. Along the natural–fabricated axis, coordinates correlate: natural carriers default to optical room-temperature control, transport connectivity, loss-type errors, slow fluorescence readout, optical/MEMS assembly; fabricated carriers default to microwave/electrical room-temperature control, static nearest-neighbour wiring, Pauli/leakage errors, fast dispersive/charge readout, lithography. A node is *off-diagonal* when, in the path that uses it, it breaks that correlation: natural carrier + microwave control; fabricated + far connectivity; fabricated + erasure; fabricated + cold-stage control or decoding; solid-state carrier + photonic interconnect; natural + sub-µs gate; natural + ≤ 30 µs readout; natural + semiconductor/photonic-chip fabrication. **Hubs** are nodes whose dependency reach (own paths plus paths of nodes that require them) spans ≥ 3 carrier families, or ≥ 2 families for a technology that reached hardware in 2023 or later. **Empty slots** are nodes with no demonstrated technology, or path slots with nothing in them.\n\n"
       "**Validity criterion.** The graph must *reproduce* the promising directions of §5 as the set S = off-diagonal ∪ hubs ∪ empty slots — it does not receive them as input. The test is only as independent as the off-diagonal patterns, which encode the natural/fabricated correlation; its real information is in the residuals: prose claims the graph does not support, and graph findings the prose missed (§9.8)."
       ) if en else (
       "### 9.1 Правила построения\n\n"
       "**Узлы — технологии, а не платформы.** Технология входит в граф, если она *самостоятельна* (её можно заменить, не трогая остальной стек) и *принципиальна* (замена сдвигает хотя бы один из четырёх выходов — канал ошибок, такт, счёт кубитов с качеством, путь масштабирования — на порядок). Платформа — это *путь*: по одному узлу на слой через десятислойный стек (носитель → кодирование → механизм гейта → связность/транспорт → управление → считывание → код → декодер → интерконнект → производство). Альтернативы внутри слота перечислены; первая — основная.\n\n"
       "**Семь координат узла (пространство проектирования, стабильно):** (a) сродство носителя на спектре естественный ↔ изготовленный (фотон = естественная частица в изготовленных модах; донор/дефект = промежуточный; независимые от носителя = нейтральные); (b) характерное время, которое узел навязывает (лог-шкала), с признаком перепутывания детерминированное / вероятностное-heralded; (c) механизм измерения с нижней границей времени, деструктивностью и возможностью mid-circuit; (d) механизм подвижности/связности; (e) модальность управления и его размещение (температурная ступень: комнатная / 4 K / милликельвины; узел может нести несколько, первая — основная); (f) структура доминирующей ошибки *как её видит код*; (g) технология производства. Координата — свойство, которое не сдвигается с ростом рекордов; всё, что сдвигается (fidelity, Λ, счёт, такт, стадия QBI, финансирование), — **атрибут пространства оценки**: датированный, с источником, прикреплён к узлу и никогда не используется для позиционирования. Акторы и цели — **аннотации** на путях.\n\n"
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
    # the diagonal on paper (brief E): rows = carrier class of the path (from the paths' `cls`), columns = trait side; the
    # flagged stations fill the off-diagonal cells by the side their flag names (NAT_* in the natural row, FAB_* in the fabricated row)
    # a family is fabricated when any of its paths is of class `fab` (spins: quantum dots are `fab`, donors `int`); otherwise natural (`nat`, `pho`, `int`)
    famcls={}
    for p in G['paths']:
        cl=p['cls'] if isinstance(p['cls'],str) else (p['cls'][0] if p['cls'] else 'fab')
        famcls[p['family']]=famcls.get(p['family'],False) or cl=='fab'
    order=[f for f in FAMS if f in famcls]
    natfams=[f for f in order if not famcls[f]]; fabfams=[f for f in order if famcls[f]]
    FLAGS_NAT=['NAT_MW','NAT_FAST_GATE','NAT_FAST_READ','NAT_FAB']; FLAGS_FAB=['FAB_FAR','FAB_ERASURE','FAB_COLD','FAB_PHOTONIC']
    def cell(flags):
        xs=[(n,[f for f in n['offdiag'] if f in flags]) for n in G['nodes']]; xs=[(n,fs) for n,fs in xs if fs]
        return '; '.join(f"{name(L,n)} `{n['id']}` ({', '.join(f'`{f}`' for f in fs)})" for n,fs in xs) or '—'
    nnat=sum(1 for n in G['nodes'] if any(f in FLAGS_NAT for f in n['offdiag'])); nfab=sum(1 for n in G['nodes'] if any(f in FLAGS_FAB for f in n['offdiag']))
    ndiag=len(G['nodes'])-sum(1 for n in G['nodes'] if n['offdiag'])
    o.append((f"**The diagonal on paper.** Rows are the carrier class of the path a station serves, columns the side its traits come from. Natural-side traits: optical control, µs–ms gates and readout, no semiconductor/photonic-chip fabrication, local connectivity. Fabricated-side traits: microwave control, sub-µs gates, ≤ 10 µs readout, cold electronics at 4 K/mK, transport/long-range connectivity, erasure conversion, photonic interconnect. The diagonal cells hold the stereotype — {ndiag} of {len(G['nodes'])} stations; the off-diagonal cells hold the {nnat + nfab} flagged stations ({nnat} natural-row, {nfab} fabricated-row; one station can carry a flag on each side) with their flags from the `OFFDIAG` vocabulary.\n" if en else
              f"**Диагональ на бумаге.** Строки — класс носителя пути, которому служит станция, столбцы — сторона, с которой взяты её свойства. Свойства естественной стороны: оптическое управление, гейты и считывание мкс–мс, без полупроводникового/фотонно-чипового производства, локальная связность. Свойства изготовленной стороны: СВЧ-управление, суб-мкс гейты, считывание ≤ 10 мкс, холодная электроника при 4 K/mK, транспортная/дальняя связность, конверсия в erasure, фотонный интерконнект. Диагональные ячейки — стереотип, {ndiag} из {len(G['nodes'])} станций; внедиагональные — {nnat + nfab} помеченных станций ({nnat} в естественной строке, {nfab} в изготовленной; одна станция может нести флаг с каждой стороны) с их флагами из словаря `OFFDIAG`.\n"))
    H(("| Carrier class of the path | Natural-side traits | Fabricated-side traits |" if en else "| Класс носителя пути | Свойства естественной стороны | Свойства изготовленной стороны |")+"\n|---|---|---|")
    H(f"| **{'natural' if en else 'естественный'}** ({fams(L,natfams)}) | {'the stereotype — most stations' if en else 'стереотип — большинство станций'} | {cell(FLAGS_NAT)} |")
    H(f"| **{'fabricated' if en else 'изготовленный'}** ({fams(L,fabfams)}) | {cell(FLAGS_FAB)} | {'the stereotype — most stations' if en else 'стереотип — большинство станций'} |")
    o.append("\n")
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
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {mdcell(e[L])} | {mdcell(e['price'][L])} | {mdcell(e['mitig'][L])} | {t(L,V['CONSTAT'][e['status']])} · [{e['date']}]({e['url']}) |\n")
        else:
            H(("| From | To | Note |" if en else "| От | К | Примечание |")+"\n|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {mdcell(e[L])}{' *(one-of)*' if e.get('any') else ''} |\n")
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
            o.append(f"| `{e['src']}` | {t(L,V['OUT'][e['dst']])} | {mdcell(e['metric'])} | {mdcell(e['value'])} | {e['date']} | {e['url']} |\n")
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
            o.append(f"| `{n['id']}` | {t(L,RK[r['key']])} | {mdcell(sv(r))} — {mdcell(r['text'])} | {mdcell(r['scope'])} | {r['date']} | {r['url']} · [{r['tag']}] |\n")
    o.append("\n")
    # 9.12 machines as measured paths (register join: data/machines.json)
    M=json.load(open(os.path.join(ROOT,'data','machines.json'),encoding='utf-8'))
    MS=sorted(M['machines'],key=lambda x:(x['family'],x['name']))
    FAMN={'SC':('superconducting','сверхпроводниковые'),'ION':('ions','ионы'),'ATOM':('atoms','атомы'),'PHOTON':('photonics','фотоника'),'SPIN':('spins','спины'),'DEFECT':('defects','дефекты'),'TOPO':('topological','топологические'),'ANNEAL':('annealing','отжиг')}
    H("### 9.12 " + ("Machines as measured paths" if en else "Машины как измеренные пути"))
    o.append((f"A machine is a *path instance* on the map: one station per layer, primary or alternate, taken from the stations the map already has, and a **gap** (`∅G-…`) wherever the map has no station for what the machine actually runs — no code, no decoder, no interconnect, an unpublished gate mechanism. The {len(MS)} machines of the Quantum Machines Register (edition {M['edition']}; [register](https://claude.ai/artifact/Bfj8NrxCsx8PMdxUCBMBhV), [Technology × Machine page](https://claude.ai/artifact/2EcsTbo9kjAHseEnBxzawp)) are joined to the graph by node id; every cell carries its evidence (verified or inferred) and the machine's own dated records sit beside the standard records of §9.11, never replacing them. Table A condenses the Technology × Machine matrix to one row per layer; Table B puts each machine's published clock numbers against the derived clock of its path (§9.4).\n\n"
              "On the map the **Machine selector** is one more term in the intersection isolate ∩ focus ∩ lens: choosing a machine keeps its stations along its family's path, dims the rest and marks the layers where the machine has a gap; with a lens the reader sees which coordinate the machine's choices share with the path, with focus which of its stations are interchanges. The register's numbers are evaluation-space attributes — dated, sourced, never used for position." if en else
              f"Машина — это *экземпляр пути* на карте: по одной станции на слой, основной или альтернативной, из тех станций, что на карте уже есть, и **пробел** (`∅G-…`) там, где у карты нет станции для того, что машина реально делает, — нет кода, нет декодера, нет интерконнекта, механизм гейта не опубликован. {len(MS)} машин Реестра квантовых машин (издание {M['edition']}; [реестр](https://claude.ai/artifact/Bfj8NrxCsx8PMdxUCBMBhV), [страница Технология × Машина](https://claude.ai/artifact/2EcsTbo9kjAHseEnBxzawp)) присоединены к графу по id узла; каждая ячейка несёт своё свидетельство (проверено или выведено), а собственные датированные рекорды машины стоят рядом со стандартными рекордами §9.11, не подменяя их. Таблица A сжимает матрицу Технология × Машина до одной строки на слой; таблица B ставит опубликованные машиной числа такта против выведенного такта её пути (§9.4).\n\n"
              "На карте **селектор машины** — ещё один член пересечения изоляция ∩ фокус ∩ линза: выбор машины оставляет её станции вдоль пути её семейства, гасит остальные и помечает слои, где у машины пробел; с линзой читатель видит, какую координату выбор машины разделяет с путём, с фокусом — какие из её станций пересадочные. Числа реестра — атрибуты пространства оценки: датированные, с источником, никогда не используемые для позиционирования.")+"\n\n")
    # Table A — the matrix condensed to one row per layer
    H("**"+("Table A — the Technology × Machine matrix by layer" if en else "Таблица A — матрица Технология × Машина по слоям")+"**\n")
    H(("| Layer | Stations used / on the map | Most-used stations (machines, primary) | Primary is a map gap: machines · gap ids |" if en else
       "| Слой | Станций занято / на карте | Самые занятые станции (машин, основные) | Основная — пробел карты: машин · id пробелов |")+"\n|---|---|---|---|")
    unknown=set()
    for l in G['layers']:
        ln=str(l['n']); used=set(); prim={}; gapm=0; gaps={}
        for x in MS:
            for c in x['layers'].get(ln,[]):
                if c['gap']:
                    if c['role']=='primary': gapm+=1; gaps[c['node']]=gaps.get(c['node'],0)+1
                    continue
                if c['node'] not in NODE: unknown.add(c['node']); continue
                used.add(c['node'])
                if c['role']=='primary': prim[c['node']]=prim.get(c['node'],0)+1
        onmap=sum(1 for n in G['nodes'] if n['layer']==l['n'])
        top=sorted(prim.items(),key=lambda kv:(-kv[1],kv[0]))[:3]
        tops='; '.join(f"{name(L,NODE[k])} `{k}` ({v})" for k,v in top) or '—'
        gs=', '.join(f"`{k}` ({v})" for k,v in sorted(gaps.items(),key=lambda kv:(-kv[1],kv[0]))) if gaps else '—'
        o.append(f"| {l['n']} {t(L,(l['en'],l['ru']))} | {len(used)} / {onmap} | {tops} | {gapm} · {gs} |\n")
    o.append("\n")
    # Table B — machine records vs the path's derived clock
    BK=('t1','t2','t1q','t2q','t_meas','t_ff','spam')
    def rec(x,k):
        rs=[r for r in x.get('records',[]) if r['key']==k and r['num'] is not None]
        return rs[0] if rs else None
    def part(p,k):  # path value the machine record is compared with; per gate layer for gates/1Q
        r=p['round']; pp=r.get('parts') or {}
        if k=='t2q': v=pp.get('gates'); d=r.get('d2') or 0; return (v/d if v and d else None)
        if k=='t1q': v=pp.get('1q'); d=r.get('d1') or 0; return (v/d if v and d else None)
        if k=='t_meas': return pp.get('readout') or None
        if k=='t_ff': return p['react']['loop'] or p['react']['floor']
        if k in ('t1','t2'): return p['coh'].get(k)
        return None
    CLOCKK=('t2q','t_meas','t1q','t_ff'); CLOCKN={'t2q':('2Q','2Q'),'t_meas':('readout','считывание'),'t1q':('1Q','1Q'),'t_ff':('reaction','реакция')}
    def verdict(q):
        if q is None: return '—'
        return t(L,('faster','быстрее')) if q<0.8 else (t(L,('slower','медленнее')) if q>1.25 else t(L,('on path','на пути')))
    def rat(q): return ('×%.1f'%q) if q is not None and 0.1<=q<1000 else (('×%.1e'%q) if q is not None else '—')
    def cell(x,k,p):
        r=rec(x,k)
        if not r: return '—'
        v=st(r['num']) if r['unit']=='s' else '%.2g'%r['num']
        if k in ('t1','t2'):
            pv=part(p,k); q=determinize(r['num']/pv) if pv else None
            return f"{v} ({r['date']}; {rat(q)})" if q is not None else f"{v} ({r['date']})"
        return f"{v} ({r['date']})"
    H("**"+("Table B — machines against the derived clock of their path" if en else "Таблица B — машины против выведенного такта их пути")+"**\n")
    H(("| Machine | Path | Path t_round | T1 (date; ×path) | T2 (date; ×path) | 1Q gate (date) | Feed-forward (date) | SPAM (date) | Clock term ×path | Verdict |" if en else
       "| Машина | Путь | t_round пути | T1 (дата; ×путь) | T2 (дата; ×путь) | 1Q-гейт (дата) | Feed-forward (дата) | SPAM (дата) | Член такта ×путь | Вердикт |")+"\n|---|---|---|---|---|---|---|---|---|---|")
    rows=0; none=0; VC={}; CC={}; ext=[]; cext=[]; joined=set(); unjoined=[]
    for x in MS:
        if not any(rec(x,k) for k in BK): none+=1; continue
        rows+=1; p=PATH[x['map_path']]; f=x['family']
        comp=[]; vd=None
        for k in CLOCKK:
            r=rec(x,k)
            if not r: continue
            pv=part(p,k)
            if pv is None: unjoined.append(f"{x['name']} ({t(L,CLOCKN[k])})"); continue
            q=determinize(r['num']/pv); joined.add(k); comp.append(f"{t(L,CLOCKN[k])} {rat(q)}")
            if vd is None: vd=q; ext.append((q,x['name']+' ('+x['org']+')',k,r['num'],pv))
        for k in ('t1','t2'):
            r=rec(x,k); pv=part(p,k) if r else None
            if r and pv: q=determinize(r['num']/pv); cext.append((q,x['name']+' ('+x['org']+')',k)); CC.setdefault(f,[0,0,0])[0 if q>1.25 else (2 if q<0.8 else 1)]+=1
            elif r: unjoined.append(f"{x['name']} ({k.upper()})")
        vw=verdict(vd); VC.setdefault(f,{})[vw]=VC.setdefault(f,{}).get(vw,0)+1
        o.append(f"| {x['name']} ({x['org']}) | {p[L]} | {st(p['round']['total'])} | {cell(x,'t1',p)} | {cell(x,'t2',p)} | {cell(x,'t1q',p)} | {cell(x,'t_ff',p)} | {cell(x,'spam',p)} | {'; '.join(comp) or '—'} | {vw} |\n")
    o.append("\n"+(f"{none} machines publish none of these numbers." if en else f"{none} машин не публикуют ни одного из этих чисел.")+"\n\n")
    # closing paragraph — computed
    fam_order=['SC','ION','ATOM','PHOTON','SPIN','DEFECT','TOPO','ANNEAL']
    def vline(f):
        d=VC.get(f,{}); return f"{t(L,FAMN[f])} {d.get(t(L,('faster','быстрее')),0)}/{d.get(t(L,('on path','на пути')),0)}/{d.get(t(L,('slower','медленнее')),0)}/{d.get('—',0)}"
    def cline(f):
        c=CC.get(f); return f"{t(L,FAMN[f])} {c[0]}/{c[1]}/{c[2]}" if c else None
    vs='; '.join(vline(f) for f in fam_order if f in VC); cs='; '.join(x for x in (cline(f) for f in fam_order) if x)
    hi=max(ext,key=lambda e:e[0]) if ext else None; lo=min(ext,key=lambda e:e[0]) if ext else None
    chi=max(cext,key=lambda e:e[0]) if cext else None; clo=min(cext,key=lambda e:e[0]) if cext else None
    nj=sum(1 for e in ext); nc=len(cext)
    uj=(f"published records that did not join: {len(unjoined)} — " if en else f"опубликованных рекордов не соединилось: {len(unjoined)} — ")+('; '.join(unjoined) or '—')
    ab=', '.join(f"`{k}`" for k in BK if not any(rec(x,k) for x in MS)) or '—'
    o.append((f"**What the comparison shows.** {rows} machines publish at least one of the seven numbers; only {nj} of them publish a *clock* term the path can be checked against (1Q gate time or feed-forward latency), and {nc} publish a coherence time. Verdicts per family, faster / on path / slower / no join: {vs}. Coherence against the path's T₁ or T₂ (above ×1.25 / within / below ×0.8): {cs}. The extremes are honest about what is being compared: the largest clock ratio is {hi[1]} ({t(L,CLOCKN[hi[2]])} {st(hi[3])} against {st(hi[4])} on its path, {rat(hi[0])}); the smallest is {lo[1]} ({t(L,CLOCKN[lo[2]])} {st(lo[3])} against {st(lo[4])}, {rat(lo[0])}); on coherence {chi[1]} sits at {rat(chi[0])} of its path's {chi[2].upper()} and {clo[1]} at {rat(clo[0])}. A ratio of ×1.0 is often the path's own record seen from the machine side (Willow's T₁/T₂ and 25 ns gate, Aurora's 1 µs loop), not an independent confirmation. Nulls: no machine in the register publishes {ab} — so the two largest terms of the superconducting and spin rounds, the 2Q gate and the readout, cannot be checked against any machine; {uj} — because their path has no derived round (photonic, defect, topological, annealing) or no 1Q layer in its code (cat); the ratios are per gate layer (parts ÷ d₂, d₁), so a machine's single-gate time is compared with a single gate of its path, not with the layer sum." if en else
              f"**Что показывает сравнение.** {rows} машин публикуют хотя бы одно из семи чисел; лишь {nj} из них публикуют член *такта*, проверяемый против пути (время 1Q-гейта или задержку feed-forward), и {nc} публикуют время когерентности. Вердикты по семействам, быстрее / на пути / медленнее / нет соединения: {vs}. Когерентность против T₁ или T₂ пути (выше ×1.25 / в пределах / ниже ×0.8): {cs}. Крайние случаи честны в том, что именно сравнивается: наибольшее отношение по такту — {hi[1]} ({t(L,CLOCKN[hi[2]])} {st(hi[3])} против {st(hi[4])} на его пути, {rat(hi[0])}); наименьшее — {lo[1]} ({t(L,CLOCKN[lo[2]])} {st(lo[3])} против {st(lo[4])}, {rat(lo[0])}); по когерентности {chi[1]} стоит на {rat(chi[0])} от {chi[2].upper()} своего пути, а {clo[1]} — на {rat(clo[0])}. Отношение ×1.0 — часто собственный рекорд пути, увиденный со стороны машины (T₁/T₂ и 25-нс гейт Willow, 1-мкс контур Aurora), а не независимое подтверждение. Пустые: ни одна машина реестра не публикует {ab} — поэтому два крупнейших члена сверхпроводникового и спинового раундов, 2Q-гейт и считывание, нельзя проверить ни по одной машине; {uj} — потому что у их пути нет выведенного раунда (фотоника, дефекты, топологические, отжиг) или нет слоя 1Q в его коде (кошки); отношения взяты на слой гейтов (части ÷ d₂, d₁), так что время одного гейта машины сравнивается с одним гейтом её пути, а не с суммой слоя.")+"\n\n")
    if unknown: o.append(("Register node ids not on the map: " if en else "Id узлов реестра, отсутствующие на карте: ")+', '.join(f"`{u}`" for u in sorted(unknown))+"\n\n")
    return ''.join(o)

json.dump(G,open(os.path.join(ROOT,'data','graph.json'),'w',encoding='utf-8',newline='\n'),ensure_ascii=False)
# splice the generated graph section (numbered 7 in the public edition) into the reports
def splice(lang,start,end):
    p=os.path.join(ROOT,'report','report_%s.md'%lang.upper()); s=open(p,encoding='utf-8').read()
    sec=sec9(lang); sec=re.sub(r'^(#+ )9(\.\d*)',r'\g<1>7\2',sec,flags=re.M).replace('## 9. ','## 7. ',1)
    sec=re.sub(r'(see|см\.) 8\.(\d+)',r'\1 7.\2',sec); sec=re.sub(r'§9(\.\d+)',r'§7\1',sec); sec=re.sub(r'§8(\.\d+)?',lambda m:'§7'+(m.group(1) or ''),sec)
    # §8 "Machines" (build/machines_chapter.py) follows the graph section; Sources is §9 in the public edition
    sec8=mc.sec_machines(lang)
    i=s.find(start); j=s.find(end); k=s.rfind('\n---\n',i,j)
    if i<0 or j<0: raise SystemExit('report %s: section markers not found'%lang)
    open(p,'w',encoding='utf-8',newline='\n').write(s[:i]+sec.rstrip()+'\n\n---\n\n'+sec8.rstrip()+'\n'+s[k:])
splice('en','## 7. The technology graph','## 9. Sources'); splice('ru','## 7. Граф технологий','## 9. Источники')
print('sec9 written', len(sec9('en').split()), len(sec9('ru').split()), '| sec8 (machines)', len(mc.sec_machines('en').split()), len(mc.sec_machines('ru').split()))
