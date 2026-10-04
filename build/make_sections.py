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
def t(lang,pair): idx={'en':0,'ru':1,'he':2}.get(lang,0); return pair[idx] if idx<len(pair) else pair[0]
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
    return f"{t(lang,V['MECH'][c['mech']])}; {logt(c['t'])}; {'destructive' if lang=='en' else ('разрушающее' if lang=='ru' else 'הרסנית')}={('yes' if lang=='en' else ('да' if lang=='ru' else 'כן')) if c['destr'] else ('no' if lang=='en' else ('нет' if lang=='ru' else 'לא'))}; {'mid-circuit' if lang=='en' else ('внутрисхемное' if lang=='ru' else 'mid-circuit')}={('yes' if lang=='en' else ('да' if lang=='ru' else 'כן')) if c['mid'] else ('no' if lang=='en' else ('нет' if lang=='ru' else 'לא'))}"
def coordE(lang,n):
    e=n['e']
    if e['mod']=='none': return '—'
    ps=e['place'] if isinstance(e['place'],list) else [e['place']]   # list-valued since 17 Sep 2026: every stage, in the vocabulary's order (RT → 4 K → mK)
    ps=[p for p in V['PLACE'] if p in ps]+[p for p in ps if p not in V['PLACE']]
    return f"{t(lang,V['MOD'][e['mod']])} @ {' / '.join(t(lang,V['PLACE'][p]) for p in ps)}"
def coordF(lang,n): return ', '.join(t(lang,V['ERR'][x]) for x in n['f'])
def status(lang,n): return t(lang,V['STATUS'][n['status']])
def name(lang,n): return n.get(lang,n['en'])
FAMS={'SC':('superconducting circuits','сверхпроводниковые схемы','מעגלים מוליכי-על'),'ION':('trapped ions','ионы в ловушках','יונים לכודים'),'ATOM':('neutral atoms','нейтральные атомы','אטומים ניטרליים'),'PHOTON':('photonics','фотоника','פוטוניקה'),'SPIN':('semiconductor spins','полупроводниковые спины','ספינים במוליכים למחצה'),'DEFECT':('defect spins','спины дефектов','ספיני פגם'),'TOPO':('topological','топологические','טופולוגי'),'ANNEAL':('quantum annealers','квантовый отжиг','מחשבי הרפיה קוונטית')}
def fams(lang,fs): return ', '.join(t(lang,FAMS[f]) for f in fs)
PATH={p['id']:p for p in G['paths']}

def sec9(lang):
    L=lang; en=(L=='en'); o=[]
    H=lambda s: o.append(s+"\n")
    H("## 9. " + ("The technology graph — nodes, attributes, edges, and what the graph says on its own" if en else ("Граф технологий — узлы, атрибуты, рёбра и что граф говорит сам" if L=='ru' else "גרף הטכנולוגיות — צמתים, תכונות, קשתות ומה שהגרף אומר בפני עצמו")))
    H(("### 9.1 Construction rules\n\n"
       "**Nodes are technologies, not platforms.** A technology enters the graph if it is *self-contained* (replaceable without touching the rest of the stack) and *principled* (its replacement shifts at least one of the four outputs — error channel, clock, count-with-quality, scaling path — by an order of magnitude). A platform is an *architecture*: one technology per layer through the ten layers — the *stack*, read from the qubit up: carrier → encoding → gate mechanism → connectivity/transport → control → readout → code → decoder → interconnect → manufacturing. Where an architecture uses more than one technology in a layer, the one it is defined by — its typical choice — is the *primary* and is drawn on its line; the others are its *alternates* (§7.3).\n\n"
       "**Seven attributes per node (design space, stable):**\n\n- (a) carrier-nature affinity on the natural ↔ fabricated spectrum (photon = natural particle in engineered modes; donor/defect = intermediate; carrier-agnostic = neutral);\n- (b) the characteristic time the node imposes (log-scale) with the entangling flag deterministic / probabilistic-heralded;\n- (c) measurement mechanism with time bound, destructiveness and mid-circuit capability;\n- (d) mobility/connectivity mechanism;\n- (e) control modality and placement (temperature stage: room temperature / 4 K / millikelvin; a node may carry several, the first being primary);\n- (f) dominant error structure *as the code sees it*;\n- (g) manufacturing technology.\n\nAn attribute is a property that does not move as records improve; anything that moves with records (fidelity, Λ, counts, cycle times, QBI stage, funding) is an **evaluation-space attribute** — dated, sourced, attached to the node, never used for position. Actors and goals are **annotations** on architectures.\n\n"
       "**Four edge types:** *requires/provides* (a dependency, read in the supply direction — *B is needed by A* — with the arrowhead at A, the technology that needs B; a dependency is *hard* (A cannot exist without B) or *soft* (B is the usual route), and B may be *one of* a group of technologies any of which would do; each dependency has a kind — acts on the carrier, fabrication route, signal delivery, readout apparatus, measurement or heralding, the code's connectivity need, decoder ↔ code, a particular encoding, built from other operations, part of or a refinement — see §7.8), *alternatives* (two technologies that can fill the same slot of a layer; the relation is symmetric and does not mean exclusion — a platform may combine both across modules or hierarchy levels, e.g. surface-code processing with gross-code memory), *conflicts* (the two work together only with a mitigating element or a change in a third layer; every conflict edge carries the mechanism, the measured price, the mitigation, a status — open / mitigated / bypassed — and a dated source, see §7.8), *defines* (node → one of the four outputs, each carrying a source, a date and a number).\n\n"
       "**Clock is not an attribute.** Per architecture it is derived as the length of one syndrome-extraction round, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, where d₂ and d₁ are the two- and one-qubit gate layers of the architecture's code (from the code node), t_2Q and t_meas come from the gate and readout attributes, t_1Q, t_move (transport between gate layers, mobile platforms only) and t_reset from standard records; the measured QEC cycle is shown next to it as a check. Two further clocks are derived from the same records: the *reaction time* (measurement → conditioned operation; the published loop where one exists, else readout + decode latency as a floor) and *operations per coherence* T₂/t_2Q, with the idle exposure per round t_round/T₂ compared against the measured idle error.\n\n"
       "**Crossing test** *(the map's own term)*. Along the natural–fabricated axis, attributes correlate: natural carriers default to optical room-temperature control, transport connectivity, loss-type errors, slow fluorescence readout, optical/MEMS assembly; fabricated carriers default to microwave/electrical room-temperature control, static nearest-neighbour wiring, Pauli/leakage errors, fast dispersive/charge readout, lithography. A technology is a *crossing technology* — hatched on the map — when, in the architecture that uses it, it breaks that correlation: natural carrier + microwave control; fabricated + far connectivity; fabricated + erasure; fabricated + cold-stage control or decoding; solid-state carrier + photonic interconnect; natural + sub-µs gate; natural + ≤ 30 µs readout; natural + semiconductor/photonic-chip fabrication. **Empty slots** are nodes with no demonstrated technology, or architecture slots with nothing in them.\n\n"
       ) if en else ((
       "### 9.1 Правила построения\n\n"
       "**Узлы — технологии, а не платформы.** Технология входит в граф, если она *самостоятельна* (её можно заменить, не трогая остальной стек) и *принципиальна* (замена сдвигает хотя бы один из четырёх выходов — канал ошибок, такт, число кубитов с учётом качества, путь масштабирования — на порядок). Платформа — это *архитектура*: по одной технологии на слой через десять слоёв — *стек*, читаемый от кубита вверх: носитель → кодирование → механизм вентиля → связность/транспорт → управление → считывание → код → декодер → межсоединение → производство. Где архитектура использует в слое больше одной технологии, та, которой она определена, — её типичный выбор — *основная* и нарисована на её линии; остальные — её *альтернативы* (§7.3).\n\n"
       "**Семь атрибутов узла (пространство проектирования, стабильно):**\n\n- (a) сродство носителя на спектре естественный ↔ искусственный (фотон = естественная частица в искусственно сформированных модах; донор/дефект = промежуточный; не зависящие от носителя = нейтральные);\n- (b) характерное время, которое узел навязывает (лог-шкала), с признаком запутывания детерминированное / вероятностное с оповещением;\n- (c) механизм измерения с нижней границей времени, деструктивностью и возможностью внутрисхемного измерения;\n- (d) механизм подвижности/связности;\n- (e) модальность управления и его размещение (температурная ступень: комнатная / 4 K / милликельвины; узел может нести несколько, первая — основная);\n- (f) структура доминирующей ошибки *как её видит код*;\n- (g) технология производства.\n\nАтрибут — свойство, которое не сдвигается с ростом рекордов; всё, что сдвигается (точность, Λ, число кубитов, такт, стадия QBI, финансирование), — **атрибут пространства оценки**: датированный, с источником, прикреплён к узлу и никогда не используется для позиционирования. Участники и цели — **аннотации** на архитектурах.\n\n"
       "**Четыре типа рёбер:** *требует/обеспечивает* (зависимость, читаемая в направлении поставки — *«B» требуется технологии «A»* — со стрелкой у A, технологии, которой нужно B; зависимость бывает *жёсткой* (без B технологии A не существует) или *мягкой* (B — обычный путь), а B может быть *одним из* группы технологий, любая из которых подошла бы; у каждой зависимости есть род — действует на носитель, маршрут изготовления, подача сигналов, система считывания, измерение или оповещение, связность, нужная коду, декодер ↔ код, определённое кодирование, строится из других операций, часть или уточнение — см. §7.8), *альтернативы* (две технологии, способные занять один и тот же слот слоя; отношение симметрично и не означает исключения — платформа может сочетать обе по модулям или уровням иерархии, например поверхностный код для обработки и gross-код для памяти), *конфликтует* (две технологии работают вместе только с элементом смягчения или при изменении третьего слоя; каждое ребро конфликта несёт механизм, измеренную цену, способ смягчения, статус — открыт / смягчён / обходится — и датированный источник, см. §7.8), *определяет* (узел → один из четырёх выходов, с источником, датой и числом).\n\n"
       "**Такт — не атрибут.** Для каждой архитектуры он выводится как длительность одного раунда извлечения синдрома, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, где d₂ и d₁ — число слоёв двух- и однокубитных вентилей в коде архитектуры (из узла кода), t_2Q и t_meas — атрибуты вентиля и считывания, а t_1Q, t_move (транспорт между слоями вентилей, только подвижные платформы) и t_reset — стандартные рекорды; измеренный цикл QEC показан рядом как проверка. Из тех же рекордов выводятся ещё два такта: *время реакции* (измерение → обусловленная операция; опубликованный контур, если есть, иначе считывание + задержка декодера как нижняя граница) и *операций на когерентность* T₂/t_2Q, а экспозиция простоя за раунд t_round/T₂ сравнивается с измеренной ошибкой простоя.\n\n"
       "**Тест на пересечение** *(собственный термин карты)*. Вдоль оси естественный–искусственный атрибуты коррелируют: у естественных носителей по умолчанию оптическое управление при комнатной температуре, транспортная связность, ошибки типа потерь, медленное флуоресцентное считывание, оптическая/МЭМС-сборка; у искусственных — СВЧ/электрическое управление при комнатной температуре, статическая разводка ближайших соседей, паулиевские ошибки и утечка, быстрое дисперсионное/зарядовое считывание, литография. Технология — *сквозная* (на карте заштрихована), если в использующей её архитектуре она ломает эту корреляцию: естественный носитель + СВЧ-управление; искусственный + дальняя связность; искусственный + стирания; искусственный + управление или декодирование в холодной ступени; твердотельный носитель + фотонное межсоединение; естественный + суб-µs вентиль; естественный + считывание ≤ 30 µs; естественный + полупроводниковое/фотонно-чиповое производство. **Пустые слоты** — узлы без продемонстрированной технологии или слоты архитектур, в которых ничего нет.\n\n") if L=='ru' else (
       "### 9.1 כללי הבנייה\n\n"
       "**הצמתים הם טכנולוגיות, לא פלטפורמות.** טכנולוגיה נכנסת לגרף אם היא *עצמאית* (אפשר להחליף אותה בלי לגעת בשאר המחסנית) וגם *עקרונית* (החלפתה מזיזה בסדר גודל לפחות אחד מארבעת הפלטים — ערוץ השגיאה, השעון, מספר הקיוביטים ואיכותם, נתיב ההגדלה). פלטפורמה היא *ארכיטקטורה*: טכנולוגיה אחת לכל שכבה לאורך עשר השכבות — *המחסנית*, הנקראת מהקיוביט כלפי מעלה: נושא ← קידוד ← מנגנון השער ← קישוריות/הובלה ← בקרה ← קריאה ← קוד ← מפענח ← חיבור בין-מודולי ← ייצור. כאשר ארכיטקטורה משתמשת ביותר מטכנולוגיה אחת בשכבה, זו שמגדירה אותה — הבחירה האופיינית לה — היא *הראשית*, והיא מצוירת על הקו שלה; האחרות הן *החלופיות* שלה (§7.3).\n\n"
       "**שבע תכונות לכל צומת (מרחב התכן; יציבות לאורך זמן):**\n\n- (a) זיקה לטבע הנושא על הרצף טבעי ↔ מיוצר (פוטון = חלקיק טבעי באופנים מהונדסים; אטום תורם/פגם = ביניים; בלתי תלוי בנושא = ניטרלי);\n- (b) הזמן האופייני שהצומת כופה (בסולם לוגריתמי), עם דגל השזירה: דטרמיניסטית / הסתברותית-מבושרת;\n- (c) מנגנון המדידה, עם חסם הזמן, ההרסנות והיכולת לקריאה באמצע המעגל;\n- (d) מנגנון הניידות/הקישוריות;\n- (e) אופן הבקרה ומיקומה (דרגת הטמפרטורה: טמפרטורת החדר / 4 K / מיליקלווין; צומת יכול לשאת כמה דרגות, והראשונה היא העיקרית);\n- (f) מבנה השגיאה השלטת *כפי שהקוד רואה אותה*;\n- (g) טכנולוגיית הייצור.\n\nתכונה היא מאפיין שאינו זז כשהשיאים משתפרים; כל מה שזז עם השיאים (נאמנות, Λ, מספרי קיוביטים, זמני מחזור, שלב QBI, מימון) הוא **תכונה של מרחב ההערכה** — מתוארכת, מלווה במקור, מוצמדת לצומת, ולעולם אינה משמשת לקביעת מיקום. שחקנים ויעדים הם **ביאורים** על ארכיטקטורות.\n\n"
       "**ארבעה סוגי קשתות:** *דורש/מספק* (תלות, הנקראת בכיוון האספקה — *B נחוצה ל-A* — וראש החץ ב-A, הטכנולוגיה הזקוקה ל-B; תלות היא *קשיחה* (A אינה יכולה להתקיים בלי B) או *רכה* (B היא הדרך המקובלת), ו-B יכולה להיות *אחת מתוך* קבוצת טכנולוגיות שכל אחת מהן תתאים; לכל תלות יש סוג — פועלת על הנושא, מסלול ייצור, הולכת אותות, מערך קריאה, מדידה או בישור, צורך הקישוריות של הקוד, מפענח ↔ קוד, קידוד מסוים, בנויה מפעולות אחרות, חלק או עידון — ראו §7.8), *חלופות* (שתי טכנולוגיות שיכולות למלא את אותה משבצת בשכבה; היחס סימטרי ואין פירושו מניעה הדדית — פלטפורמה יכולה לשלב את שתיהן במודולים שונים או ברמות היררכיה שונות, למשל עיבוד בקוד המשטח וזיכרון בקוד gross), *מתנגש* (שתי הטכנולוגיות פועלות יחד רק בעזרת רכיב מפחית או בשינוי בשכבה שלישית; כל קשת התנגשות נושאת את המנגנון, את המחיר הנמדד, את ההפחתה, מצב — פתוח / מופחת / נעקף — ומקור מתוארך, ראו §7.8), *מגדיר* (צומת ← אחד מארבעת הפלטים, כל אחד עם מקור, תאריך ומספר).\n\n"
       "**השעון אינו תכונה.** לכל ארכיטקטורה הוא נגזר כאורכו של סבב אחד של חילוץ הסינדרום, t_round = d₂·(t_2Q + t_move) + d₁·t_1Q + t_meas + t_reset, כאשר d₂ ו-d₁ הם מספרי שכבות השערים הדו-קיוביטיים והחד-קיוביטיים בקוד של הארכיטקטורה (מצומת הקוד), t_2Q ו-t_meas באים מתכונות השער והקריאה, ו-t_1Q, t_move (הובלה בין שכבות שערים, בפלטפורמות ניידות בלבד) ו-t_reset באים מרשומות התקן; מחזור תיקון השגיאות הנמדד מוצג לצדו כבדיקה. שני שעונים נוספים נגזרים מאותן רשומות: *זמן התגובה* (מדידה ← פעולה מותנית; הלולאה שפורסמה, אם קיימת, ואחרת קריאה + השהיית הפענוח כחסם תחתון), וכן *פעולות לזמן קוהרנטיות*, T₂/t_2Q; חשיפת הסרק לסבב, t_round/T₂, מושווית לשגיאת הסרק הנמדדת.\n\n"
       "**מבחן החצייה** *(מונח של המפה עצמה)*. לאורך הציר טבעי–מיוצר התכונות מתואמות: לנושאים טבעיים יש כברירת מחדל בקרה אופטית בטמפרטורת החדר, קישוריות באמצעות הובלה, שגיאות מסוג אובדן, קריאה איטית בפלואורסצנציה, הרכבה אופטית/MEMS; לנושאים מיוצרים יש כברירת מחדל בקרה במיקרוגל או בחשמל בטמפרטורת החדר, חיווט סטטי לשכנים הקרובים ביותר, שגיאות פאולי/דליפה, קריאה מהירה דיספרסיבית/מבוססת מטען, ליתוגרפיה. טכנולוגיה היא *טכנולוגיה חוצה* — מקווקוות במפה — כאשר בארכיטקטורה המשתמשת בה היא שוברת את המתאם הזה: נושא טבעי + בקרה במיקרוגל; מיוצר + קישוריות רחוקה; מיוצר + מחיקה; מיוצר + בקרה או פענוח בדרגה הקרה; נושא במצב מוצק + חיבור בין-מודולי פוטוני; טבעי + שער תת-µs; טבעי + קריאה של ≤ 30 µs; טבעי + ייצור מוליכים למחצה/שבבים פוטוניים. **משבצות ריקות** הן צמתים ללא טכנולוגיה מודגמת, או משבצות של ארכיטקטורה שאין בהן דבר.\n\n")))
    # 9.2 node table
    H("### 9.2 " + ((f"Node table ({len(G['nodes'])} technologies × 7 attributes)") if en else ((f"Таблица узлов ({len(G['nodes'])} технологий × 7 атрибутов)") if L=='ru' else (f"טבלת הצמתים ({len(G['nodes'])} טכנולוגיות × 7 תכונות)"))))
    H(("| # | Layer | Technology | (a) carrier affinity | (b) time · entangling | (c) readout | (d) mobility | (e) control · placement | (f) error structure | (g) manufacturing | status · since |" if en else
       ("| # | Слой | Технология | (a) сродство носителя | (b) время · запутывание | (c) считывание | (d) подвижность | (e) управление · размещение | (f) структура ошибки | (g) производство | статус · с года |" if L=='ru' else "| # | שכבה | טכנולוגיה | (a) זיקת הנושא | (b) זמן · שזירה | (c) קריאה | (d) ניידות | (e) בקרה · מיקום | (f) מבנה השגיאה | (g) ייצור | מצב · מאז |"))+"\n|---|---|---|---|---|---|---|---|---|---|---|")
    for i,n in enumerate(sorted(G['nodes'],key=lambda x:(x['layer'],-x['aff'],x['id'])),1):
        o.append(f"| {i} | {n['layer']} {t(L,(LAY[n['layer']]['en'],LAY[n['layer']]['ru'],LAY[n['layer']].get('he',LAY[n['layer']]['en'])))} | **{name(L,n)}** `{n['id']}` | {aff(L,n['aff'])} | {coordB(L,n)} | {coordC(L,n)} | {t(L,V['MOB'][n['d']])} | {coordE(L,n)} | {coordF(L,n)} | {t(L,V['FAB'][n['g']])} | {status(L,n)} · {n['since'] if n['since']<2030 else '—'} |\n")
    o.append("\n")
    # 9.3 architectures
    H("### 9.3 " + ("Architectures layer by layer — the technology each one uses in each of the ten layers (alternates in brackets)" if en else ("Архитектуры слой за слоем — технология каждой в каждом из десяти слоёв (альтернативы в скобках)" if L=='ru' else "הארכיטקטורות שכבה אחר שכבה — הטכנולוגיה שכל אחת מהן משתמשת בה בכל אחת מעשר השכבות (החלופיות בסוגריים)")))
    o.append(("Each row is an architecture, each column one of the ten layers of §7.1. The cell names the technology the architecture's line passes through on the map — its *primary* technology for that layer, the typical choice the architecture is defined by — and, in brackets, its *alternates*: technologies the same architecture also uses, or has used, in that layer (the half-tone squares of the map). **∅** is a layer the architecture has no technology for (§7.6 lists these empty slots); ✗ marks a technology that is itself an empty slot — a name for something no one has built yet." if en else
              ("Каждая строка — архитектура, каждый столбец — один из десяти слоёв §7.1. В ячейке — технология, через которую на карте проходит линия архитектуры: её *основная* технология в этом слое, типичный выбор, которым архитектура определена, — и в скобках *альтернативы*: технологии, которыми та же архитектура тоже пользуется или пользовалась в этом слое (полутоновые квадраты карты). **∅** — слой, для которого у архитектуры технологии нет (эти пустые слоты перечислены в §7.6); ✗ — технология, которая сама является пустым слотом: имя того, чего ещё никто не построил." if L=='ru' else "כל שורה היא ארכיטקטורה, וכל עמודה היא אחת מעשר השכבות של §7.1. התא נוקב בשם הטכנולוגיה שקו הארכיטקטורה עובר דרכה במפה — הטכנולוגיה *הראשית* שלה בשכבה זו, הבחירה האופיינית שמגדירה את הארכיטקטורה — ובסוגריים את הטכנולוגיות *החלופיות* שלה: טכנולוגיות שאותה ארכיטקטורה גם משתמשת בהן, או השתמשה בהן, באותה שכבה (הריבועים בחצי-גוון שבמפה). **∅** מסמן שכבה שאין לארכיטקטורה טכנולוגיה עבורה (§7.6 מונה את המשבצות הריקות האלה); ✗ מסמן טכנולוגיה שהיא עצמה משבצת ריקה — שם למשהו שאיש עוד לא בנה."))+"\n\n")
    hdr="| " + ("Architecture" if en else ("Архитектура" if L=='ru' else "ארכיטקטורה")) + " | " + " | ".join(f"{l['n']} {t(L,(l['en'],l['ru'],l.get('he',l['en'])))}" for l in G['layers']) + " |"
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
        o.append(f"| **{p.get(L,p['en'])}** — {p['actors']} | " + " | ".join(cells) + " |\n")
    o.append("\n")
    # 9.4 derived clock
    def st(x,u="s"):
        if x is None: return "—"
        if u=="s":
            for k,f in (("s",1),("ms",1e-3),("µs",1e-6),("ns",1e-9)):
                if x>=f: return ("%.3g %s"%(x/f,k)).replace(".0 "," ")
            return "0"
        return "%.2g"%x
    H("### 9.4 " + ("Derived clocks per architecture — syndrome round, reaction time, operations per coherence" if en else ("Выведенные такты по архитектурам — раунд синдрома, время реакции, операций на когерентность" if L=='ru' else "שעונים נגזרים לפי ארכיטקטורה — סבב סינדרום, זמן תגובה, פעולות לזמן קוהרנטיות")))
    H(("| Architecture | round of | d₂ | gates | transport | 1Q | readout | reset | **t_round** | limiter | measured cycle | reaction time (loop / floor) | T₂ | ops per coherence | idle exposure t_round/T₂ | idle measured |" if en else
       ("| Архитектура | раунд кода | d₂ | вентили | транспорт | 1Q | считывание | сброс | **t_round** | ограничитель | измеренный цикл | время реакции (контур / граница) | T₂ | операций на когерентность | экспозиция простоя t_round/T₂ | простой измерен |" if L=='ru' else "| ארכיטקטורה | קוד הסבב | d₂ | שערים | הובלה | 1Q | קריאה | איפוס | **t_round** | גורם מגביל | מחזור נמדד | זמן תגובה (לולאה / חסם תחתון) | T₂ | פעולות לזמן קוהרנטיות | חשיפת סרק t_round/T₂ | סרק נמדד |"))+"\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for p in G['paths']:
        r=p['round']; pp=r.get('parts',{}); c=p['coh']; rx=p['react']
        lim={'gates':('gates','вентили','שערים'),'transport':('transport','транспорт','הובלה'),'1q':('1Q','1Q','1Q'),'readout':('readout','считывание','קריאה'),'reset':('reset','сброс','איפוס')}.get(r['limiter'])
        def mt(k): return (t(L,('unpublished','не опубл.','לא פורסם')) if k in (r.get('missing') or []) else st(pp.get(k)))   # a term the architecture needs but nothing publishes: named, not a silent 0
        o.append(f"| {p.get(L,p['en'])} | {r.get('code') or '—'} | {r.get('d2') or '—'} | {st(pp.get('gates'))} | {mt('transport')} | {mt('1q')} | {st(pp.get('readout'))} | {mt('reset')} | **{('≥ ' if r.get('missing') else '')+st(r['total'])}** | {t(L,lim) if lim else '—'} | {p['cycle']} | {st(rx['loop'])} / {st(rx['floor'])} | {st(c['t2'])}{(' ('+c['t2_scope']+')') if c.get('t2_scope') and c['t2_scope']!='typical' else ''} | {('%.1e'%c['ops_per_coh']) if c['ops_per_coh'] else '—'} | {('%.1e'%c['idle_exposure']) if c['idle_exposure'] else '—'} | {('%.1e'%c['idle_measured']) if c['idle_measured'] else '—'} |\n")
    notes=[(p.get(L,p['en']),"; ".join(p['round']['notes'])) for p in G['paths'] if p['round']['notes']]
    o.append("\n" + ("**Reading.** The round is a sum, not a maximum, so the limiter is the largest term, not the only one: on the superconducting architecture readout and reset together are two-thirds of the round, on the atom architectures transport between gate layers is, on the QCCD ion architecture transport plus recooling is ~90%. Where the derived round sits below the measured cycle the difference is the gap between the *attribute* (best published time for the mechanism) and the *device* (the cycle actually run) — on the superconducting architecture 0.65 µs against 1.1 µs, on the spin architecture the best 6 µs readout against the ~100 µs typically run. The idle exposure t_round/T₂ is a second check: on the superconducting architecture it predicts 0.7% per round against the 0.9% idle term in Google's measured error budget; on ions and atoms it is 10⁻⁴–10⁻⁷, so a millisecond clock costs those platforms mostly time — idle error is small per round, though the terms the idle exposure omits (heating during transport, loss during imaging, drift between calibrations) are exactly the ones those platforms report. A total printed with ≥ is a partial sum: a term the architecture needs (transport, 1Q, reset) that no record publishes enters as zero and is named in the column, so the round is a lower bound, not an estimate. On the QCCD ion architecture the transport-plus-recooling primitives are the published H1 table (2020) — 9.7 ms derived against the 1–5 ms cycles reported for H2-class experiments, because the primitives have not been republished for H2/Helios and the derived value uses the colour code's eight layers. Reaction time is the quantity resource estimates assume (10 µs in the RSA-2048 estimate) and the one the map most often cannot fill: only the superconducting, atom and photonic architectures have a published measurement-to-operation loop." if en else
       ("**Чтение.** Раунд — сумма, а не максимум, поэтому ограничитель — наибольшее слагаемое, а не единственное: в сверхпроводниковой архитектуре считывание и сброс вместе дают две трети раунда, в атомных — транспорт между слоями вентилей, в ионной QCCD-архитектуре транспорт с повторным охлаждением — ~90%. Там, где выведенный раунд ниже измеренного цикла, разница — это зазор между *атрибутом* (лучшее опубликованное время механизма) и *устройством* (реально прогнанным циклом): в сверхпроводниковой архитектуре 0.65 µs против 1.1 µs, в спиновой — лучшее считывание 6 µs против типичных ~100 µs. Экспозиция простоя t_round/T₂ — вторая проверка: в сверхпроводниковой архитектуре она предсказывает 0.7% за раунд против 0.9% члена простоя в измеренном бюджете ошибок Google; у ионов и атомов она 10⁻⁴–10⁻⁷ — поэтому миллисекундный такт стоит этим платформам главным образом времени: ошибка простоя за раунд мала, хотя члены, которых экспозиция простоя не учитывает (нагрев при транспорте, потери при съёмке, дрейф между калибровками), — ровно те, о которых эти платформы сообщают. Итог, напечатанный с ≥, — частичная сумма: слагаемое, нужное архитектуре (транспорт, однокубитные вентили, сброс), которого не публикует ни один рекорд, входит нулём и названо в столбце, так что раунд — нижняя граница, а не оценка. В ионной QCCD-архитектуре примитивы транспорта и повторного охлаждения — опубликованная таблица H1 (2020): выведено 9.7 ms против 1–5 ms циклов, сообщённых для экспериментов класса H2, потому что примитивы для H2/Helios не переопубликованы, а выведенное значение берёт восемь слоёв цветового кода. Время реакции — величина, которую предполагают оценки ресурсов (10 µs в оценке для RSA-2048), и та, которую карта чаще всего не может заполнить: опубликованный контур измерение → операция есть только у сверхпроводниковой, атомной и фотонной архитектур." if L=='ru' else "**פרשנות.** הסבב הוא סכום, לא מקסימום, ולכן הגורם המגביל הוא האיבר הגדול ביותר, לא היחיד: בארכיטקטורת המוליכים-על הקריאה והאיפוס יחד הם שני שלישים מהסבב, בארכיטקטורות האטומים — ההובלה בין שכבות השערים, ובארכיטקטורת היונים QCCD — ההובלה והקירור החוזר, ~90%. כאשר הסבב הנגזר נמוך מהמחזור הנמדד, ההפרש הוא הפער בין *התכונה* (הזמן הטוב ביותר שפורסם עבור המנגנון) לבין *ההתקן* (המחזור שהורץ בפועל) — בארכיטקטורת המוליכים-על 0.65 µs לעומת 1.1 µs, בארכיטקטורת הספינים קריאה מיטבית של 6 µs לעומת ~100 µs שמורצים בדרך כלל. חשיפת הסרק t_round/T₂ היא בדיקה שנייה: בארכיטקטורת המוליכים-על היא חוזה 0.7% לסבב, לעומת איבר הסרק של 0.9% בתקציב השגיאות הנמדד של Google; ביונים ובאטומים היא 10⁻⁴–10⁻⁷, ולכן שעון של מילישניות עולה לפלטפורמות האלה בעיקר בזמן — שגיאת הסרק לסבב קטנה, אף שהאיברים שחשיפת הסרק משמיטה (חימום בזמן הובלה, אובדן בזמן דימות, סחיפה בין כיולים) הם בדיוק אלה שהפלטפורמות האלה מדווחות עליהם. סך כולל שמודפס עם ≥ הוא סכום חלקי: איבר שהארכיטקטורה זקוקה לו (הובלה, 1Q, איפוס) ושאף רשומה אינה מפרסמת נכנס כאפס ונקוב בשמו בעמודה, ולכן הסבב הוא חסם תחתון, לא אומדן. בארכיטקטורת היונים QCCD, הפרימיטיבים של הובלה וקירור חוזר הם טבלת H1 שפורסמה (2020) — 9.7 ms נגזרים לעומת מחזורים של 1–5 ms שדווחו בניסויים מדרגת H2 משום שהפרימיטיבים לא פורסמו מחדש עבור H2/Helios, והערך הנגזר משתמש בשמונה השכבות של קוד הצבע. זמן התגובה הוא הגודל שאומדני משאבים מניחים (10 µs באומדן עבור RSA-2048), והוא הגודל שהמפה לרוב אינה יכולה למלא: רק לארכיטקטורות המוליכים-על, האטומים והפוטוניקה יש לולאת מדידה-לפעולה שפורסמה.")) + "\n\n")
    if notes:
        o.append(("Notes: " if en else ("Примечания: " if L=='ru' else "הערות: ")) + "; ".join(f"*{a}* — {b}" for a,b in notes) + ".\n\n")
    # 9.5 crossing technologies (the map's hatch)
    H("### 9.5 " + ("Crossing technologies — where a technology takes a trait from across the natural/fabricated divide" if en else ("Сквозные технологии — где технология берёт свойство с другой стороны раздела естественное/искусственное" if L=='ru' else "טכנולוגיות חוצות — היכן שטכנולוגיה נוטלת מאפיין מעברה השני של החלוקה טבעי/מיוצר")))
    # the diagonal on paper (brief E): rows = carrier class of the architecture (from the architectures' `cls`), columns = trait side; the
    # flagged technologies fill the off-diagonal cells by the side their flag names (NAT_* in the natural row, FAB_* in the fabricated row)
    # a family is fabricated when any of its architectures is of class `fab` (spins: quantum dots are `fab`, donors `int`); otherwise natural (`nat`, `pho`, `int`)
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
    nod=sum(1 for n in G['nodes'] if n['offdiag']); ndiag=len(G['nodes'])-nod; nboth=nnat+nfab-nod
    o.append((f"**The divide on paper.** Rows are the carrier class of the architecture a technology serves, columns the side its traits come from. Natural-side traits: optical control, µs–ms gates and readout, no semiconductor/photonic-chip fabrication, local connectivity. Fabricated-side traits: microwave control, sub-µs gates, ≤ 10 µs readout, cold electronics at 4 K/mK, transport/long-range connectivity, erasure conversion, photonic interconnect. The two cells where the row and the column agree hold the stereotype — {ndiag} of {len(G['nodes'])} technologies; the two crossing cells hold the {nod} hatched technologies ({nnat} in the natural row, {nfab} in the fabricated row; {nboth} of them carries a flag on each side and appears in both rows) with their flags from the `OFFDIAG` vocabulary.\n" if en else
              (f"**Раздел на бумаге.** Строки — класс носителя архитектуры, которой служит технология, столбцы — сторона, с которой взяты её свойства. Свойства естественной стороны: оптическое управление, вентили и считывание µs–ms, без полупроводникового/фотонно-чипового производства, локальная связность. Свойства искусственной стороны: СВЧ-управление, суб-µs вентили, считывание ≤ 10 µs, холодная электроника при 4 K/mK, транспортная/дальняя связность, преобразование в стирания, фотонное межсоединение. Две ячейки, где строка и столбец согласны, — стереотип, {ndiag} из {len(G['nodes'])} технологий; две перекрёстные ячейки — {nod} заштрихованных технологий ({nnat} в естественной строке, {nfab} в искусственной; {nboth} из них несёт флаг с каждой стороны и стоит в обеих строках) с их флагами из словаря `OFFDIAG`.\n" if L=='ru' else f"**החלוקה על הנייר.** השורות הן מחלקת הנושא של הארכיטקטורה שהטכנולוגיה משרתת, והעמודות — הצד שממנו באים מאפייניה. מאפייני הצד הטבעי: בקרה אופטית, שערים וקריאה בטווח µs–ms, ללא ייצור מוליכים למחצה/שבבים פוטוניים, קישוריות מקומית. מאפייני הצד המיוצר: בקרה במיקרוגל, שערים תת-µs, קריאה של ≤ 10 µs, אלקטרוניקה קרה ב-4 K/mK, קישוריות באמצעות הובלה/לטווח ארוך, המרה למחיקה, חיבור בין-מודולי פוטוני. שני התאים שבהם השורה והעמודה מסכימות מכילים את הסטריאוטיפ — {ndiag} מתוך {len(G['nodes'])} טכנולוגיות; שני התאים החוצים מכילים את {nod} הטכנולוגיות המקווקוות ({nnat} בשורה הטבעית, {nfab} בשורה המיוצרת; {nboth} מהן נושאת דגל בכל צד ומופיעה בשתי השורות), עם הדגלים שלהן מאוצר המונחים `OFFDIAG`.\n")))
    o.append("\n\n"+"\n".join([("| Carrier class of the architecture | Natural-side traits | Fabricated-side traits |" if en else ("| Класс носителя архитектуры | Свойства естественной стороны | Свойства искусственной стороны |" if L=='ru' else "| מחלקת הנושא של הארכיטקטורה | מאפייני הצד הטבעי | מאפייני הצד המיוצר |"))+"\n|---|---|---|", f"| **{'natural' if en else ('естественный' if L=='ru' else 'טבעי')}** ({fams(L,natfams)}) | {'the stereotype — most technologies' if en else ('стереотип — большинство технологий' if L=='ru' else 'הסטריאוטיפ — רוב הטכנולוגיות')} | {cell(FLAGS_NAT)} |", f"| **{'fabricated' if en else ('искусственный' if L=='ru' else 'מיוצר')}** ({fams(L,fabfams)}) | {cell(FLAGS_FAB)} | {'the stereotype — most technologies' if en else ('стереотип — большинство технологий' if L=='ru' else 'הסטריאוטיפ — רוב הטכנולוגיות')} |"])+"\n\n")   # one markdown block: a blank line before, no blank lines between the rows (they were emitted through H(), which broke the table into paragraphs — found by the editor on 17 Sep)
    o.append("\n")
    H(("| Node | Layer | Pattern | In architectures | Why it matters |" if en else ("| Узел | Слой | Паттерн | В архитектурах | Почему важно |" if L=='ru' else "| צומת | שכבה | דפוס | בארכיטקטורות | מדוע זה חשוב |"))+"\n|---|---|---|---|---|")
    WHY={'enc_dualrail':("erasure — a natural-world error class — engineered into a fabricated carrier; threshold ×4","стирание — класс ошибок естественного мира — инженерно внесено в искусственный носитель; порог ×4","מחיקה — מחלקת שגיאות של העולם הטבעי — מהונדסת לתוך נושא מיוצר; סף ×4"),
         'g_ryd':("a natural carrier with a 270 ns gate: the reason atoms compete at all","естественный носитель с вентилем 270 ns: причина, по которой атомы вообще конкурируют","נושא טבעי עם שער של 270 ns: הסיבה שאטומים מתחרים בכלל"),
         'g_elec':("removes lasers, the historic scaling blocker of ions; 8.4×10⁻⁵","убирает лазеры — исторический блокер масштабирования ионов; 8.4×10⁻⁵","סילוק הלייזרים, החסם ההיסטורי בפני הגדלת מערכות יונים; 8.4×10⁻⁵"),
         'cx_lr':("gives 2D lattices the degree-6 connectivity qLDPC needs","даёт 2D-решёткам связность степени 6, нужную qLDPC","מעניקה לסריגי 2D את הקישוריות מדרגה 6 ש-qLDPC זקוק לה"),
         'cx_shuttle':("transport connectivity for a fabricated carrier — the spin route to non-local codes","транспортная связность для искусственного носителя — спиновый путь к нелокальным кодам","קישוריות באמצעות הובלה לנושא מיוצר — דרכם של הספינים אל קודים לא-מקומיים"),
         'ct_cryocmos':("control moves into the fridge: wiring and heat are one of the four limits on the count","управление уходит в криостат: проводка и тепло — одно из четырёх ограничений на число кубитов","הבקרה עוברת אל תוך המקרר: חיווט וחום הם אחת מארבע המגבלות על מספר הקיוביטים"),
         'ct_sfq':("the second cold route: nW per qubit at millikelvin; quasiparticle poisoning is the open risk","второй холодный маршрут: нВт на кубит при милликельвинах; открытый риск — quasiparticle poisoning","הדרך הקרה השנייה: nW לקיוביט במיליקלווין; הרעלת קוואזי-חלקיקים היא הסיכון הפתוח"),
         'ct_fluxdac':("annealer heritage: 10⁴ qubits on 200–300 lines (D-Wave's own figures disagree)","наследие отжигателей: 10⁴ кубитов на 200–300 линиях (собственные данные D-Wave расходятся)","מורשת מחשבי ההרפיה: 10⁴ קיוביטים על 200–300 קווים (הנתונים של D-Wave עצמה אינם מתיישבים זה עם זה)"),
         'ct_pic_trap':("optics of the fabricated world for a natural carrier; footprint ÷50 claimed","оптика искусственного мира для естественного носителя; заявлено уменьшение габаритов в 50 раз","אופטיקה של העולם המיוצר עבור נושא טבעי; נטענת הקטנת שטח ÷50"),
         'ct_ionlaser':("integrated photonics in the trap — the ion analogue of the same move","интегральная фотоника в ловушке — ионный аналог того же хода","פוטוניקה משולבת במלכודת — המקבילה היונית של אותו מהלך"),
         'ct_ionmw':("~200 electronic sources for 1,000 ions instead of laser beams","~200 электронных источников на 1 000 ионов вместо лазерных лучей","~200 מקורות אלקטרוניים ל-1,000 יונים במקום קרני לייזר"),
         'ro_erasure':("the readout primitive behind every erasure code; 384 ns on transmons","примитив считывания за каждым кодом со стираниями; 384 ns на трансмонах","פרימיטיב הקריאה שמאחורי כל קוד מחיקה; 384 ns על טרנסמונים"),
         'code_erasure':("threshold 0.94% → 4.15%; the largest single lever on overhead","порог 0.94% → 4.15%; крупнейший одиночный рычаг для оверхеда","סף 0.94% ← 4.15%; המנוף הבודד הגדול ביותר להפחתת התקורה"),
         'ic_mcm':("fabricated carriers reaching beyond one chip (chiplets, l-couplers)","искусственные носители выходят за пределы одного чипа (чиплеты, l-couplers)","נושאים מיוצרים החורגים אל מעבר לשבב יחיד (צ'יפלטים, l-couplers)"),
         'ic_cryolink':("30 m between fridges at 80% Bell — the microwave route to modularity","30 m между криостатами при 80% Bell — СВЧ-путь к модульности","30 m בין מקררים ב-80% Bell — דרך המיקרוגל למודולריות"),
         'ic_spinphoton':("solid-state spins reaching the network via photons","твердотельные спины выходят в сеть через фотоны","ספינים במצב מוצק המגיעים לרשת באמצעות פוטונים"),
         'ic_transducer':("the missing link for optical modularity of superconducting machines — empty","недостающее звено оптической модульности сверхпроводниковых машин — пусто","החוליה החסרה למודולריות אופטית של מכונות מוליכות-על — ריקה"),
         'fab_cmos':("ion traps from standard semiconductor fabs (Oxford Ionics, SkyWater)","ионные ловушки со стандартных полупроводниковых фабрик (Oxford Ionics, SkyWater)","מלכודות יונים ממפעלי מוליכים למחצה סטנדרטיים (Oxford Ionics, SkyWater)"),
         'ro_imgfast':("17.6 µs atom readout cuts the imaging term 30–50×, but the whole QEC round only ~2×","считывание атомов за 17.6 µs сокращает вклад регистрации флуоресценции в 30–50 раз, но весь раунд QEC — лишь примерно вдвое","קריאת אטומים ב-17.6 µs מקצרת את איבר הדימות 30–50×, אך את סבב תיקון השגיאות כולו רק ~2×")}
    for n in [n for n in G['nodes'] if n['offdiag']]:
        pats='; '.join(t(L,V['OFFDIAG'][f]) for f in n['offdiag'])
        o.append(f"| **{name(L,n)}** `{n['id']}` | {n['layer']} | {pats} | {', '.join(PATH[p].get(L,PATH[p]['en']) for p in n['offdiag_paths'])} | {t(L,WHY.get(n['id'],('','','')))} |\n")
    o.append("\n")
    # 9.6 empty slots
    H("### 9.6 " + ("Empty slots — where a technology does not exist yet" if en else ("Пустые слоты — где технологии ещё нет" if L=='ru' else "משבצות ריקות — היכן שטכנולוגיה עדיין אינה קיימת")))
    H(("| Slot | Status | What would fill it | Best today vs needed |" if en else ("| Слот | Статус | Что должно его заполнить | Лучшее сегодня vs необходимое |" if L=='ru' else "| משבצת | מצב | מה ימלא אותה | הטוב ביותר כיום לעומת הנדרש |"))+"\n|---|---|---|---|")
    GAPS=[('ic_transducer',("η_tot 15%, N_add 0.16 vs η > 1/2, N_add ≪ 1; ~3 orders of magnitude (IBM)","η_tot 15%, N_add 0.16 против η > 1/2, N_add ≪ 1; ~3 порядка (IBM)","η_tot 15%, N_add 0.16 לעומת η > 1/2, N_add ≪ 1; ~3 סדרי גודל (IBM)")),
          ('dec_cryo',("designs only (NISQ+ 20 ns, QECOOL 2.8 µW); no fabricated decoder chip","только проекты (NISQ+ 20 ns, QECOOL 2.8 µW); ни одного изготовленного чипа","תכנונים בלבד (NISQ+ 20 ns, QECOOL 2.8 µW); אין שבב מפענח מיוצר"),),
          ('g_catcnot',("theory proposal Jul 2026; every cat resource estimate assumes it","теоретическое предложение июль 2026; каждая оценка ресурсов для кошачьих кубитов его предполагает","הצעה תאורטית, יולי 2026; כל אומדן משאבים לקיוביטי חתול מניח את קיומה")),
          ('src_resource',("8-photon states at < 1 Hz vs 24–168-photon encoded resource states at MHz","8-фотонные состояния при < 1 Hz против 24–168-фотонных кодированных ресурсных состояний на МГц","מצבים של 8 פוטונים בקצב של < 1 Hz לעומת מצבי משאב מקודדים של 24–168 פוטונים בקצב MHz")),
          ('g_mbq',("single-wire parity readout only; no X-lifetime ≈ Z, no two-qubit operation","только считывание чётности одной проволоки; нет времени жизни X ≈ Z, нет двухкубитной операции","קריאת זוגיות של תיל יחיד בלבד; אין זמן חיים של X ≈ Z, אין פעולה דו-קיוביטית"))]
    for nid,gap in GAPS:
        n=NODE[nid]; o.append(f"| **{name(L,n)}** `{nid}` ({n['layer']}) | {status(L,n)} | {n['desc'].get(L,n['desc']['en'])} | {t(L,gap)} |\n")
    SLOTGAP={('spin_qd',9):("an interconnect for quantum-dot spins (spin–photon in dots is lab-only)","межсоединение для спинов в квантовых точках (спин-фотон в точках — только лаборатория)","חיבור בין-מודולי לספינים בנקודות קוונטיות (ספין–פוטון בנקודות קיים רק במעבדה)"),('spin_donor',9):("interconnect for donor spins","межсоединение для донорных спинов","חיבור בין-מודולי לספיני תורמים"),
             ('defect',7):("a code for network nodes (memory/repeater codes are theory)","код для узлов сети (коды памяти/повторителей — теория)","קוד לצומתי רשת (קודי זיכרון/ממסר הם תאוריה בלבד)"),('defect',8):("—","—","—"),('topo',7):("Floquet / measurement-based codes on a demonstrated qubit","Floquet / measurement-based коды на продемонстрированном кубите","קודי Floquet / קודים מבוססי מדידה על קיוביט שהודגם"),('topo',8):("—","—","—"),('topo',9):("—","—","—"),
             ('anneal',2):("no encoding — analog Hamiltonian, not a qubit register","нет кодирования — аналоговый гамильтониан, не регистр кубитов","אין קידוד — המילטוניאן אנלוגי, לא אוגר קיוביטים"),('anneal',7):("no error correction in annealing","в отжиге нет коррекции ошибок","אין תיקון שגיאות בהרפיה"),('anneal',8):("—","—","—"),('anneal',9):("—","—","—")}
    for e in G['empty_slots']:
        if e.get('only'): continue
        k=(e['path'],e['layer']); o.append(f"| {PATH[e['path']].get(L,PATH[e['path']]['en'])} — {t(L,(LAY[e['layer']]['en'],LAY[e['layer']]['ru'],LAY[e['layer']].get('he',LAY[e['layer']]['en'])))} | ∅ | {t(L,SLOTGAP.get(k,('','','')))} | — |\n")
    # additional numeric gaps (attributes on existing nodes)
    o.append("\n"+("Numeric gaps on existing nodes (attribute-level, not empty slots): ion–photon links at 10–250 s⁻¹ vs ≥ 10⁴ s⁻¹ needed; photonic switch loss 100–190 mdB vs ~7 mdB; optical GKP effective squeezing 0.62 dB vs 9.75 dB; cat phase-flip ~10⁻¹ per CX vs 10⁻³ assumed; spin readout 6 µs at 99.2% vs sub-µs at 99.9% for a µs-class cycle; atom imaging 0.5–1 ms typical vs 17.6 µs emerging." if en else
       ("Числовые пробелы на существующих узлах (уровень атрибутов, не пустые слоты): ион-фотонные интерфейсы 10–250 s⁻¹ против ≥ 10⁴ s⁻¹; потери фотонных переключателей 100–190 mdB против ~7 mdB; эффективное оптическое сжатие GKP 0.62 dB против 9.75 dB; переворот фазы кошачьих кубитов ~10⁻¹ на CX против заложенных 10⁻³; считывание спинов 6 µs при 99.2% против суб-µs при 99.9% для цикла класса µs; регистрация флуоресценции атомов 0.5–1 ms типично против формирующихся 17.6 µs." if L=='ru' else "פערים מספריים בצמתים קיימים (ברמת התכונות, לא משבצות ריקות): קישורי יון–פוטון בקצב 10–250 s⁻¹ לעומת ≥ 10⁴ s⁻¹ הנדרשים; אובדן במתגים פוטוניים 100–190 mdB לעומת ~7 mdB; סחיטה אפקטיבית של GKP אופטי 0.62 dB לעומת 9.75 dB; היפוך פאזה בקיוביטי חתול ~10⁻¹ לכל CX לעומת 10⁻³ שהונחו; קריאת ספין ב-6 µs ובנאמנות 99.2% לעומת תת-µs ו-99.9% הנדרשים למחזור בסדר גודל של µs; דימות אטומים 0.5–1 ms באופן טיפוסי לעומת 17.6 µs המתהווים."))+"\n\n")
    # 9.7 representation
    H("### 9.7 " + ("How the map shows a graph of 7 attributes and 4 edge types — and why it is dynamic" if en else ("Как карта показывает граф с 7 атрибутами и 4 типами рёбер — и почему она динамическая" if L=='ru' else "כיצד המפה מציגה גרף של 7 תכונות ו-4 סוגי קשתות — ומדוע היא דינמית")))
    o.append(("The map is a **layered map**: the ten layers of §7.1 are its columns, left to right from the carrier to the application; inside a column a technology's vertical position is its carrier-nature affinity, so the natural half sits above and the fabricated half below, and a *crossing technology* (§7.5) is the one drawn in the other half, hatched. Each architecture is a coloured line through its primary technology in every layer it has one for; its alternates are half-tone squares of the same colour beside the line; a layer the architecture skips shows a dotted circle where the line jumps the column; an empty slot (§7.6) is a hollow dashed technology. Seven attributes cannot all be painted at once — a reader has one hue channel — so the map carries a **lens** that recolours every technology by one attribute at a time, a **parallel-coordinates strip** that draws the full seven-vector of every technology as a polyline, and a **card** that keeps the three spaces apart: design attributes, dated evaluation attributes, actors and goals. Edges of type *requires / alternatives / conflicts* are drawn only for the focused technology, because " + str(len(G['nodes'])) + " technologies × " + str(sum(1 for e in G['edges'] if e['type'] in ('requires','replaces','conflicts'))) + " edges of those three types drawn together are a hairball; *defines* edges live in the card as dated rows, not lines. **Dynamic is necessary, static is mandatory:** the resting frame is a complete readable map (all architectures, all technologies) that prints and thumbnails; the interaction adds lenses, focus, the machine selector and Find, without which four edge types and " + str(len(G['nodes'])) + " technologies cannot be read. The tables of §7.2–7.9 are the same graph on paper." if en else
       ("Карта — **слоистая карта**: десять слоёв §7.1 — её столбцы, слева направо от носителя к приложению; внутри столбца вертикальная позиция технологии — её сродство к природе носителя, так что естественная половина сверху, искусственная снизу, а *сквозная технология* (§7.5) — та, что нарисована в чужой половине, со штриховкой. Каждая архитектура — цветная линия через её основную технологию в каждом слое, где такая есть; её альтернативы — полутоновые квадраты того же цвета рядом с линией; слой, который архитектура пропускает, отмечен пунктирным кружком там, где линия перескакивает столбец; пустой слот (§7.6) — полая пунктирная технология. Семь атрибутов нельзя закрасить одновременно — у читателя один канал оттенка, — поэтому у карты есть **линза**, перекрашивающая технологии по одному атрибуту за раз, **лента параллельных координат**, рисующая полный семимерный вектор каждой технологии ломаной, и **карточка**, разводящая три пространства: атрибуты проектирования, датированные атрибуты оценки, участники и цели. Рёбра типов *требует / альтернативы / конфликтует* рисуются только для технологии в фокусе, потому что " + str(len(G['nodes'])) + " технологий × " + str(sum(1 for e in G['edges'] if e['type'] in ('requires','replaces','conflicts'))) + " рёбер этих трёх типов, нарисованные разом, — клубок; рёбра *определяет* живут в карточке датированными строками, а не линиями. **Динамика необходима, статика обязательна:** кадр покоя — полная читаемая карта (все архитектуры, все технологии), пригодная для печати и миниатюры; интерактив добавляет линзы, фокус, селектор машины и поиск, без которых четыре типа рёбер и " + str(len(G['nodes'])) + " технологий не прочесть. Таблицы §7.2–7.9 — тот же граф на бумаге." if L=='ru' else "המפה היא **מפה בשכבות**: עשר השכבות של §7.1 הן עמודותיה, משמאל לימין, מהנושא ועד היישום; בתוך עמודה, המיקום האנכי של טכנולוגיה הוא זיקתה לטבע הנושא, כך שהמחצית הטבעית נמצאת למעלה והמחצית המיוצרת למטה, ואילו *טכנולוגיה חוצה* (§7.5) היא זו שמצוירת במחצית האחרת, מקווקוות. כל ארכיטקטורה היא קו צבעוני העובר דרך הטכנולוגיה הראשית שלה בכל שכבה שיש לה בה טכנולוגיה; החלופיות שלה הן ריבועים בחצי-גוון באותו צבע לצד הקו; שכבה שהארכיטקטורה מדלגת עליה מסומנת בעיגול מנוקד במקום שבו הקו מדלג על העמודה; משבצת ריקה (§7.6) היא טכנולוגיה חלולה בעלת מתאר מקווקו. את שבע התכונות אי אפשר לצבוע בבת אחת — לקורא יש ערוץ גוון אחד — ולכן יש במפה **עדשה** הצובעת מחדש כל טכנולוגיה לפי תכונה אחת בכל פעם, **רצועת קואורדינטות מקבילות** המציירת את הווקטור המלא בן שבעת הרכיבים של כל טכנולוגיה כקו שבור, וכן **כרטיס** המפריד בין שלושת המרחבים: תכונות התכן, תכונות הערכה מתוארכות, שחקנים ויעדים. קשתות מהסוגים *דורש / חלופות / מתנגש* מצוירות רק עבור הטכנולוגיה שבמיקוד, משום ש-" + str(len(G['nodes'])) + " טכנולוגיות × " + str(sum(1 for e in G['edges'] if e['type'] in ('requires','replaces','conflicts'))) + " קשתות משלושת הסוגים האלה, כשהן מצוירות יחד, הן סבך; קשתות *מגדיר* חיות בכרטיס כשורות מתוארכות, לא כקווים. **הדינמיות נחוצה, והסטטיות חובה:** התמונה הנייחת היא מפה שלמה וקריאה (כל הארכיטקטורות, כל הטכנולוגיות) שאפשר להדפיס ולהציג כתמונה ממוזערת; האינטראקציה מוסיפה עדשות, מיקוד, את בורר המכונה ואת החיפוש, שבלעדיהם אי אפשר לקרוא ארבעה סוגי קשתות ו-" + str(len(G['nodes'])) + " טכנולוגיות. הטבלאות של §7.2–7.9 הן אותו גרף על הנייר."))+"\n\n")
    # 9.8 edge list
    H("### 9.8 " + ("Edge list" if en else ("Список рёбер" if L=='ru' else "רשימת הקשתות")))
    for et,title in (("requires",("dependencies — B is needed by A (the table lists A, then B)","зависимости — «B» требуется технологии «A» (в таблице сначала A, затем B)","תלויות — B נחוצה ל-A (בטבלה מופיעה A תחילה, ואחריה B)")),("replaces",("alternatives (within layer)","альтернативы (внутри слоя)","חלופות (בתוך שכבה)")),("conflicts",("conflicts","конфликтует","מתנגש"))):
        H("**"+t(L,title)+"**\n")
        if et=="conflicts":
            H(("| From | To | Mechanism | Measured price | Mitigation | Status · source |" if en else ("| От | К | Механизм | Измеренная цена | Смягчение | Статус · источник |" if L=='ru' else "| מצומת | לצומת | מנגנון | מחיר נמדד | הפחתה | מצב · מקור |"))+"\n|---|---|---|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {mdcell(e.get(L,e['en']))} | {mdcell(e['price'].get(L,e['price']['en']))} | {mdcell(e['mitig'].get(L,e['mitig']['en']))} | {t(L,V['CONSTAT'][e['status']])} · [{e['date']}]({e['url']}) |\n")
        elif et=="requires":
            KIND=V.get('EDGE_KIND',{})
            H(("| Technology | Needs | Kind | Strength | Note |" if en else ("| Технология | Нужно | Род | Сила | Примечание |" if L=='ru' else "| טכנולוגיה | דורשת | סוג | חוזק | הערה |"))+"\n|---|---|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    kind=t(L,KIND[e['kind']]) if e.get('kind') in KIND else ''
                    strength=(t(L,tuple(G['vocab']['GROUP_LABEL'].get(e['group'],('one of ('+e['group']+')',)*2+('אחת מתוך ('+e['group']+')',))))) if e.get('any') else (('soft' if en else ('мягкая' if L=='ru' else 'רכה')) if e.get('strength')=='soft' else ('hard' if en else ('жёсткая' if L=='ru' else 'קשיחה')))
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {kind} | {strength} | {mdcell(e.get(L,e['en']))} |\n")
        else:
            H(("| From | To | Note |" if en else ("| От | К | Примечание |" if L=='ru' else "| מצומת | לצומת | הערה |"))+"\n|---|---|---|")
            for e in G['edges']:
                if e['type']==et:
                    o.append(f"| `{e['src']}` {name(L,NODE[e['src']])} | `{e['dst']}` {name(L,NODE[e['dst']])} | {mdcell(e.get(L,e['en']))} |\n")
        o.append("\n")
    H("**"+("defines (node → output; every row carries a source, a date and a number)" if en else ("определяет (узел → выход; каждая строка несёт источник, дату и число)" if L=='ru' else "מגדיר (צומת ← פלט; כל שורה נושאת מקור, תאריך ומספר)"))+"**\n")
    H(("| Node | Output | Metric | Value | Date | Source |" if en else ("| Узел | Выход | Метрика | Значение | Дата | Источник |" if L=='ru' else "| צומת | פלט | מדד | ערך | תאריך | מקור |"))+"\n|---|---|---|---|---|---|")
    for e in G['edges']:
        if e['type']=='defines':
            o.append(f"| `{e['src']}` | {t(L,V['OUT'][e['dst']])} | {mdcell(e['metric'])} | {mdcell(e['value'])} | {e['date']} | {e['url']} |\n")
    o.append("\n")
    # 9.9 standard records
    H("### 9.9 " + ("Standard records — the dated numbers behind the derived clocks (nulls are honest: not published)" if en else ("Стандартные рекорды — датированные числа за выведенными тактами (пустые — честно: не опубликовано)" if L=='ru' else "רשומות התקן — המספרים המתוארכים שמאחורי השעונים הנגזרים (ערכים ריקים הם כנים: לא פורסמו)")))
    RK=G['vocab']['RECKEYS']; SCOPE_T={'typical':('typical','типичное','טיפוסי'),'best':('best','лучшее','מיטבי')}
    H(("| Node | Quantity | Value | Scope | Date | Source · tag |" if en else ("| Узел | Величина | Значение | Охват | Дата | Источник · тег |" if L=='ru' else "| צומת | גודל | ערך | היקף | תאריך | מקור · תג |"))+"\n|---|---|---|---|---|---|")
    def sv(r):
        if r['num'] is None: return ("*not published*" if en else ("*не опубликовано*" if L=='ru' else "*לא פורסם*")) + (" — "+r['note'] if r.get('note') else "")
        u=r['unit']
        if u=='s': return st(r['num'])
        if u=='Hz': return "%.2g Hz"%r['num']
        if u=='count': return "%g"%r['num']
        return "%.3g"%r['num']
    for n in G['nodes']:
        for r in n.get('records',[]):
            o.append(f"| `{n['id']}` | {t(L,RK[r['key']])} | {' — '.join(x for x in (mdcell(sv(r)),mdcell(r['text'])) if x)} | {mdcell(t(L,SCOPE_T.get(r['scope'],(r['scope'],r['scope'],r['scope']))))} | {r['date']} | {r['url']} · [{r['tag']}] |\n")
    o.append("\n")
    # 9.10 machines as measured architectures (register join: data/machines.json)
    M=json.load(open(os.path.join(ROOT,'data','machines.json'),encoding='utf-8'))
    MS=sorted(M['machines'],key=lambda x:(x['family'],x['name']))
    FAMN=FAMS
    H("### 9.10 " + ("Machines as instances of the architectures — the register joined to the map" if en else ("Машины как экземпляры архитектур — реестр, соединённый с картой" if L=='ru' else "מכונות כמופעים של הארכיטקטורות — המרשם מצורף למפה")))
    o.append((f"A machine is an *instance* of its architecture on the map: one technology per layer, primary or alternate, taken from the technologies the map already has — and its measured numbers (§8) are what the architecture, on paper, could only promise. A layer without a technology holds one of three values, which the register keeps apart: **none** — the machine has nothing in this layer (no code, no decoder, no interconnect; for analog and sampling machines no encoding layer or no entangling gate); **undisclosed** — something is there and nothing is published (a gate mechanism, a control stack, an inter-core link); a **gap** (`∅G-…`) — the machine runs what the map has no technology for, each an entry in the register's gap ledger and a candidate technology for a later edition. The {len(MS)} machines of the Quantum Machines Register (edition {M['edition']}; its input files are in the repository, [data/register](https://github.com/qraveh/qt-map/tree/main/data/register), and every machine has its own page, [machine/](machine/index.html)) are joined to the graph by node id; every cell carries its evidence (verified or inferred) and the machine's own dated records sit beside the standard records of §7.9, never replacing them. Table A condenses the Technology × Machine matrix to one row per layer; Table B puts each machine's published clock numbers against the derived clock of its architecture (§7.4).\n\n"
              "On the map the **Machine selector** is one more term in the intersection isolate ∩ focus ∩ lens: choosing a machine keeps its technologies along its family's architecture, dims the rest and marks the layers where the machine has no technology (none, undisclosed or a gap); with a lens the reader sees which attribute the machine's choices share with the architecture, with focus which of its technologies other architectures share. The register's numbers are evaluation-space attributes — dated, sourced, never used for position." if en else
              (f"Машина — *экземпляр* своей архитектуры на карте: по одной технологии на слой, основной или альтернативной, из тех технологий, что на карте уже есть, — а её измеренные числа (§8) — то, что архитектура на бумаге могла лишь обещать. Слой без технологии содержит одно из трёх значений, которые реестр различает: **none** — в этом слое у машины ничего нет (нет кода, декодера, межсоединения; у аналоговых и сэмплирующих машин — нет слоя кодирования или запутывающего вентиля); **undisclosed** — что-то есть, но ничего не опубликовано (механизм вентиля, стек управления, связь между ядрами); **пробел** (`∅G-…`) — машина запускает то, для чего у карты нет технологии; каждый — запись в реестре пробелов и кандидат в технологии следующего издания. {len(MS)} машин Реестра квантовых машин (издание {M['edition']}; его входные файлы — в репозитории, [data/register](https://github.com/qraveh/qt-map/tree/main/data/register), а у каждой машины есть своя страница, [machine/](machine/index.html)) присоединены к графу по id узла; каждая ячейка несёт своё свидетельство (проверено или выведено), а собственные датированные рекорды машины стоят рядом со стандартными рекордами §7.9, не подменяя их. Таблица A сжимает матрицу Технология × Машина до одной строки на слой; таблица B ставит опубликованные машиной числа такта против выведенного такта её архитектуры (§7.4).\n\n"
              "На карте **селектор машины** — ещё один член пересечения изоляция ∩ фокус ∩ линза: выбор машины оставляет её технологии вдоль линии её семейства, гасит остальные и помечает слои, где у машины нет технологии (none, undisclosed или пробел); с линзой читатель видит, какой атрибут выбор машины разделяет с архитектурой, с фокусом — какие из её технологий разделяют другие архитектуры. Числа реестра — атрибуты пространства оценки: датированные, с источником, никогда не используемые для позиционирования." if L=='ru' else
              f"מכונה היא *מופע* של הארכיטקטורה שלה על המפה: טכנולוגיה אחת לכל שכבה, ראשית או חלופית, מתוך הטכנולוגיות שכבר קיימות במפה — והמספרים הנמדדים שלה (§8) הם מה שהארכיטקטורה, על הנייר, יכלה רק להבטיח. שכבה ללא טכנולוגיה מחזיקה אחד משלושה ערכים, שהמרשם מבחין ביניהם: **none** — אין למכונה דבר בשכבה זו (אין קוד, אין מפענח, אין חיבור בין-מודולי; במכונות אנלוגיות ובמכונות דגימה — אין שכבת קידוד או אין שער שזירה); **undisclosed** — יש שם משהו, אך דבר לא פורסם (מנגנון שער, מערך בקרה, קישור בין ליבות); **פער** (`∅G-…`) — המכונה מפעילה משהו שאין לו טכנולוגיה במפה; כל פער הוא רשומה בפנקס הפערים של המרשם ומועמד לטכנולוגיה במהדורה מאוחרת יותר. {len(MS)} המכונות של מרשם המכונות הקוונטיות (מהדורה {M['edition']}; קובצי הקלט שלו נמצאים במאגר, [data/register](https://github.com/qraveh/qt-map/tree/main/data/register), ולכל מכונה יש דף משלה, [machine/](machine/index.html)) מצורפות לגרף לפי מזהה הצומת; כל תא נושא את הראיות שלו (מאומתות או מוסקות), והרשומות המתוארכות של המכונה עצמה עומדות לצד רשומות התקן של §7.9, ואינן מחליפות אותן. טבלה A מצמצמת את מטריצת טכנולוגיה × מכונה לשורה אחת לכל שכבה; טבלה B מעמידה את מספרי השעון שכל מכונה פרסמה מול השעון הנגזר של הארכיטקטורה שלה (§7.4).\n\n"
              "במפה, **בורר המכונה** הוא איבר נוסף בחיתוך בידוד ∩ מיקוד ∩ עדשה: בחירת מכונה משאירה את הטכנולוגיות שלה לאורך הארכיטקטורה של משפחתה, מעמעמת את השאר ומסמנת את השכבות שבהן אין למכונה טכנולוגיה (none, undisclosed או פער); עם עדשה, הקורא רואה איזו תכונה משותפת לבחירות המכונה ולארכיטקטורה, ועם מיקוד — אילו מהטכנולוגיות שלה משותפות גם לארכיטקטורות אחרות. המספרים של המרשם הם תכונות של מרחב ההערכה — מתוארכים, מלווים במקור, ולעולם אינם משמשים לקביעת מיקום."))+"\n\n")
    # Table A — the matrix condensed to one row per layer
    H("**"+("Table A — the Technology × Machine matrix by layer" if en else ("Таблица A — матрица Технология × Машина по слоям" if L=='ru' else "טבלה A — מטריצת טכנולוגיה × מכונה לפי שכבה"))+"**\n")
    H(("| Layer | Technologies used / on the map | Most-used technologies (machines, primary) | Primary none · undisclosed | Primary is an Atlas gap: machines · gap ids |" if en else
       ("| Слой | Технологий занято / на карте | Самые занятые технологии (машин, основные) | Основная none · undisclosed | Основная — пробел Атласа: машин · id пробелов |" if L=='ru' else "| שכבה | טכנולוגיות בשימוש / במפה | הטכנולוגיות הנפוצות ביותר (מכונות, ראשית) | ראשית none · undisclosed | הראשית היא פער של האטלס: מכונות · מזהי פערים |"))+"\n|---|---|---|---|---|")
    unknown=set()
    for l in G['layers']:
        ln=str(l['n']); used=set(); prim={}; gapm=0; gaps={}; void=0; und=0
        for x in MS:
            for c in x['layers'].get(ln,[]):
                cs=c.get('state','gap' if c['gap'] else 'station')
                if cs=='gap':
                    if c['role']=='primary': gapm+=1; gaps[c['node']]=gaps.get(c['node'],0)+1
                    continue
                if cs in ('none','undisclosed'):
                    if c['role']=='primary': void+=(cs=='none'); und+=(cs=='undisclosed')
                    continue
                if c['node'] not in NODE: unknown.add(c['node']); continue
                used.add(c['node'])
                if c['role']=='primary': prim[c['node']]=prim.get(c['node'],0)+1
        onmap=sum(1 for n in G['nodes'] if n['layer']==l['n'])
        top=sorted(prim.items(),key=lambda kv:(-kv[1],kv[0]))[:3]
        tops='; '.join(f"{name(L,NODE[k])} `{k}` ({v})" for k,v in top) or '—'
        gs=', '.join(f"`{k}` ({v})" for k,v in sorted(gaps.items(),key=lambda kv:(-kv[1],kv[0]))) if gaps else '—'
        o.append(f"| {l['n']} {t(L,(l['en'],l['ru'],l.get('he',l['en'])))} | {len(used)} / {onmap} | {tops} | {void} · {und} | {gapm} · {gs} |\n")
    o.append("\n")
    # Table B — machine records vs the architecture's derived clock
    BK=('t1','t2','t1q','t2q','t_meas','t_ff','spam')
    def rec(x,k):
        rs=[r for r in x.get('records',[]) if r['key']==k and r['num'] is not None]
        return rs[0] if rs else None
    def part(p,k):  # architecture value the machine record is compared with; per gate layer for gates/1Q
        r=p['round']; pp=r.get('parts') or {}
        if k=='t2q': v=pp.get('gates'); d=r.get('d2') or 0; return (v/d if v and d else None)
        if k=='t1q': v=pp.get('1q'); d=r.get('d1') or 0; return (v/d if v and d else None)
        if k=='t_meas': return pp.get('readout') or None
        if k=='t_ff': return p['react']['loop'] or p['react']['floor']
        if k in ('t1','t2'): return p['coh'].get(k)
        return None
    CLOCKK=('t2q','t_meas','t1q','t_ff'); CLOCKN={'t2q':('2Q','2Q','2Q'),'t_meas':('readout','считывание','קריאה'),'t1q':('1Q','1Q','1Q'),'t_ff':('reaction','реакция','תגובה')}
    def verdict(q):
        if q is None: return '—'
        return t(L,('faster','быстрее','מהירה יותר')) if q<0.8 else (t(L,('slower','медленнее','איטית יותר')) if q>1.25 else t(L,('on its clock','по архитектуре','תואמת לארכיטקטורה')))
    def rat(q): return ('×%.1f'%q) if q is not None and 0.1<=q<1000 else (('×%.1e'%q) if q is not None else '—')
    def cell(x,k,p):
        r=rec(x,k)
        if not r: return '—'
        v=st(r['num']) if r['unit']=='s' else '%.2g'%r['num']
        if k in ('t1','t2'):
            pv=part(p,k); q=determinize(r['num']/pv) if pv else None
            return f"{v} ({r['date']}; {rat(q)})" if q is not None else f"{v} ({r['date']})"
        return f"{v} ({r['date']})"
    H("**"+("Table B — machines against the derived clock of their architecture" if en else ("Таблица B — машины против выведенного такта их архитектуры" if L=='ru' else "טבלה B — מכונות מול השעון הנגזר של הארכיטקטורה שלהן"))+"**\n")
    H(("| Machine | Architecture | Architecture t_round | T1 (date; ×architecture) | T2 (date; ×architecture) | 1Q gate (date) | Feed-forward (date) | SPAM (date) | Clock term ×architecture | Verdict |" if en else
       ("| Машина | Архитектура | t_round архитектуры | T1 (дата; ×архитектура) | T2 (дата; ×архитектура) | Однокубитный вентиль (дата) | Прямая связь (дата) | SPAM (дата) | Член такта ×архитектура | Вердикт |" if L=='ru' else "| מכונה | ארכיטקטורה | t_round של הארכיטקטורה | T1 (תאריך; ×ארכיטקטורה) | T2 (תאריך; ×ארכיטקטורה) | שער 1Q (תאריך) | הזנה קדימה (תאריך) | SPAM (תאריך) | איבר השעון ×ארכיטקטורה | פסק |"))+"\n|---|---|---|---|---|---|---|---|---|---|")
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
        o.append(f"| {x['name']} ({x['org']}) | {p.get(L,p['en'])} | {('≥ ' if p['round'].get('missing') else '')+st(p['round']['total'])} | {cell(x,'t1',p)} | {cell(x,'t2',p)} | {cell(x,'t1q',p)} | {cell(x,'t_ff',p)} | {cell(x,'spam',p)} | {'; '.join(comp) or '—'} | {vw} |\n")
    o.append("\n"+(f"{none} machines publish none of these numbers." if en else (f"{none} машин не публикуют ни одного из этих чисел." if L=='ru' else f"{none} מכונות אינן מפרסמות אף אחד מהמספרים האלה."))+"\n\n")
    # closing paragraph — computed
    fam_order=['SC','ION','ATOM','PHOTON','SPIN','DEFECT','TOPO','ANNEAL']
    def vline(f):
        d=VC.get(f,{}); return f"{t(L,FAMN[f])} {d.get(t(L,('faster','быстрее','מהירה יותר')),0)}/{d.get(t(L,('on its clock','по архитектуре','תואמת לארכיטקטורה')),0)}/{d.get(t(L,('slower','медленнее','איטית יותר')),0)}/{d.get('—',0)}"
    def cline(f):
        c=CC.get(f); return f"{t(L,FAMN[f])} {c[0]}/{c[1]}/{c[2]}" if c else None
    vs='; '.join(vline(f) for f in fam_order if f in VC); cs='; '.join(x for x in (cline(f) for f in fam_order) if x)
    hi=max(ext,key=lambda e:e[0]) if ext else None; lo=min(ext,key=lambda e:e[0]) if ext else None
    chi=max(cext,key=lambda e:e[0]) if cext else None; clo=min(cext,key=lambda e:e[0]) if cext else None
    nj=sum(1 for e in ext); nc=len(cext)
    uj=(f"published records that did not join: {len(unjoined)} — " if en else (f"опубликованных рекордов не соединилось: {len(unjoined)} — " if L=='ru' else f"רשומות שפורסמו ולא צורפו: {len(unjoined)} — "))+('; '.join(unjoined) or '—')
    ab=', '.join(f"`{k}`" for k in BK if not any(rec(x,k) for x in MS)) or '—'
    o.append((f"**What the comparison shows.** {rows} machines publish at least one of the seven numbers; only {nj} of them publish a *clock* term the architecture can be checked against (1Q gate time or feed-forward latency), and {nc} publish a coherence time. Verdicts per family, faster / on its clock / slower / no join: {vs}. Coherence against the architecture's T₁ or T₂ (above ×1.25 / within / below ×0.8): {cs}. The extremes are honest about what is being compared: the largest clock ratio is {hi[1]} ({t(L,CLOCKN[hi[2]])} {st(hi[3])} against {st(hi[4])} on its architecture, {rat(hi[0])}); the smallest is {lo[1]} ({t(L,CLOCKN[lo[2]])} {st(lo[3])} against {st(lo[4])}, {rat(lo[0])}); on coherence {chi[1]} sits at {rat(chi[0])} of its architecture's {chi[2].upper()} and {clo[1]} at {rat(clo[0])}. A ratio of ×1.0 is often the architecture's own record seen from the machine side (Willow's T₁/T₂ and 25 ns gate, Aurora's 1 µs loop), not an independent confirmation. Nulls: no machine in the register publishes {ab} — so the two largest terms of the superconducting and spin rounds, the 2Q gate and the readout, cannot be checked against any machine; {uj} — because their architecture has no derived round (photonic, defect, topological, annealing) or no 1Q layer in its code (cat); the ratios are per gate layer (parts ÷ d₂, d₁), so a machine's single-gate time is compared with a single gate of its architecture, not with the layer sum." if en else
              (f"**Что показывает сравнение.** {rows} машин публикуют хотя бы одно из семи чисел; лишь {nj} из них публикуют член *такта*, проверяемый против архитектуры (время однокубитного вентиля или задержку прямой связи), и {nc} публикуют время когерентности. Вердикты по семействам, быстрее / по архитектуре / медленнее / нет соединения: {vs}. Когерентность против T₁ или T₂ архитектуры (выше ×1.25 / в пределах / ниже ×0.8): {cs}. Крайние случаи честны в том, что именно сравнивается: наибольшее отношение по такту — {hi[1]} ({t(L,CLOCKN[hi[2]])} {st(hi[3])} против {st(hi[4])} в его архитектуре, {rat(hi[0])}); наименьшее — {lo[1]} ({t(L,CLOCKN[lo[2]])} {st(lo[3])} против {st(lo[4])}, {rat(lo[0])}); по когерентности {chi[1]} стоит на {rat(chi[0])} от {chi[2].upper()} своей архитектуры, а {clo[1]} — на {rat(clo[0])}. Отношение ×1.0 — часто собственный рекорд архитектуры, увиденный со стороны машины (T₁/T₂ и 25-ns вентиль Willow, 1-µs контур Aurora), а не независимое подтверждение. Пустые: ни одна машина реестра не публикует {ab} — поэтому два крупнейших члена сверхпроводникового и спинового раундов, двухкубитный вентиль и считывание, нельзя проверить ни по одной машине; {uj} — потому что у их архитектуры нет выведенного раунда (фотоника, дефекты, топологические, отжиг) или нет слоя однокубитных вентилей в её коде (кошачьи кубиты); отношения взяты на слой вентилей (части ÷ d₂, d₁), так что время одного вентиля машины сравнивается с одним вентилем её архитектуры, а не с суммой слоя." if L=='ru' else f"**מה ההשוואה מראה.** {rows} מכונות מפרסמות לפחות אחד משבעת המספרים; רק {nj} מהן מפרסמות איבר *שעון* שאפשר לבדוק מול הארכיטקטורה (זמן שער 1Q או השהיית הזנה קדימה), ו-{nc} מפרסמות זמן קוהרנטיות. פסקים לפי משפחה, מהירה יותר / תואמת לארכיטקטורה / איטית יותר / ללא צירוף: {vs}. קוהרנטיות מול T₁ או T₂ של הארכיטקטורה (מעל ×1.25 / בתחום / מתחת ל-×0.8): {cs}. הקצוות כנים לגבי מה שמושווה: יחס השעון הגדול ביותר הוא של {hi[1]} ({t(L,CLOCKN[hi[2]])} {st(hi[3])} לעומת {st(hi[4])} בארכיטקטורה שלה, {rat(hi[0])}); הקטן ביותר — של {lo[1]} ({t(L,CLOCKN[lo[2]])} {st(lo[3])} לעומת {st(lo[4])}, {rat(lo[0])}); בקוהרנטיות, {chi[1]} עומדת על {rat(chi[0])} מה-{chi[2].upper()} של הארכיטקטורה שלה, ו-{clo[1]} על {rat(clo[0])}. יחס של ×1.0 הוא לעתים קרובות רשומת הארכיטקטורה עצמה במבט מצד המכונה (T₁/T₂ ושער ה-25 ns של Willow, לולאת ה-1 µs של Aurora), ולא אישור בלתי תלוי. ערכים ריקים: אף מכונה במרשם אינה מפרסמת {ab} — ולכן את שני האיברים הגדולים ביותר בסבבי המוליכים-על והספינים, שער ה-2Q והקריאה, אי אפשר לבדוק מול אף מכונה; {uj} — משום שלארכיטקטורה שלהן אין סבב נגזר (פוטוניקה, ספיני פגם, טופולוגי, הרפיה) או שאין שכבת 1Q בקוד שלה (קיוביטי חתול); היחסים מחושבים לכל שכבת שערים (חלקים ÷ d₂, d₁), כך שזמן שער בודד של מכונה מושווה לשער בודד של הארכיטקטורה שלה, ולא לסכום השכבה."))+"\n\n")
    if unknown: o.append(("Register node ids not on the map: " if en else ("Id узлов реестра, отсутствующие на карте: " if L=='ru' else "מזהי צמתים במרשם שאינם במפה: "))+', '.join(f"`{u}`" for u in sorted(unknown))+"\n\n")
    return ''.join(o)

# ---- BEGIN Hebrew overlay (29 Sep 2026, the language framework — build/langs.py) ------------------------------------------------------
# data/i18n/graph_he.json, when it exists, adds the Hebrew names and texts of the graph beside the English and Russian ones:
#   {"layers": {id or n: he}, "vocab": {KEY: {k: he}}, "nodes": {id: {"he": name, "desc": he, "attrs": he}},
#    "paths": {id: {"he": name, "short": he, "na": {layer: [he]}}}, "edges": [{"type", "src", "dst", "he", "price", "mitig"}]}
# → layer['he'], vocab[KEY][k][2], node['he'], node['desc']['he'], node['attrs']['he'], path['he'], path['short']['he'], path['na'][layer][2],
# edge['he'], edge['price']['he'], edge['mitig']['he']. What the file lacks stays absent: the pages read English there.
def _he_overlay(G, path=os.path.join(ROOT, 'data', 'i18n', 'graph_he.json')):
    if not os.path.exists(path): return 0
    O = json.load(open(path, encoding='utf-8')); n = 0
    def third(seq, v):   # a vocabulary pair (en, ru) → (en, ru, he)
        seq = list(seq); seq += [seq[0]] * max(0, 2 - len(seq)); return seq[:2] + [v]
    for l in G.get('layers', []):
        v = (O.get('layers') or {}).get(str(l.get('id'))) or (O.get('layers') or {}).get(str(l.get('n')))   # by the layer's id ('carrier') or its number
        if v: l['he'] = v; n += 1
    for key, items in (O.get('vocab') or {}).items():
        for k, v in (items or {}).items():
            if v and k in (G.get('vocab') or {}).get(key, {}): G['vocab'][key][k] = third(G['vocab'][key][k], v); n += 1
    for node in G.get('nodes', []):
        o = (O.get('nodes') or {}).get(node['id']) or {}
        if o.get('he'): node['he'] = o['he']; n += 1
        for f in ('desc', 'attrs'):
            if o.get(f) and isinstance(node.get(f), dict): node[f]['he'] = o[f]; n += 1
    for p in G.get('paths', []):
        o = (O.get('paths') or {}).get(p['id']) or {}
        if o.get('he'): p['he'] = o['he']; n += 1
        if o.get('short') and isinstance(p.get('short'), dict): p['short']['he'] = o['short']; n += 1
        for lay, v in (o.get('na') or {}).items():
            v = v[0] if isinstance(v, (list, tuple)) and v else v
            if v and lay in (p.get('na') or {}): p['na'][lay] = third(p['na'][lay], v); n += 1
    E = {(e.get('type'), e.get('src'), e.get('dst')): e for e in G.get('edges', [])}
    for o in O.get('edges') or []:
        e = E.get((o.get('type'), o.get('src'), o.get('dst')))
        if not e: continue
        if o.get('he'): e['he'] = o['he']; n += 1
        for f in ('price', 'mitig'):
            if o.get(f) and isinstance(e.get(f), dict): e[f]['he'] = o[f]; n += 1
    return n
_nhe = _he_overlay(G)
if _nhe: print('graph_he.json: %d Hebrew entries merged' % _nhe)
# ---- END Hebrew overlay -------------------------------------------------------------------------------------------------------------------
# the descriptions name the register's counts through placeholders ({{N_T_CT_IONAOD_MACHINES_W}} — build/counts.py, 29 Sep 2026)
import counts as _cn
_M = json.load(open(os.path.join(ROOT, 'data', 'machines.json'), encoding='utf-8'))
_nf = 0
for _L in ('en', 'ru', 'he'):
    _vals = _cn.tech_placeholders(_L, _M, G); _vals['MACHINES'] = str(len(_M['machines']))
    for _n in G['nodes']:
        for _f in ('desc', 'attrs'):
            if isinstance(_n.get(_f), dict) and '{{' in (_n[_f].get(_L) or ''): _n[_f][_L] = _cn.fill(_n[_f][_L], _L, _vals); _nf += 1
if _nf: print('graph descriptions: %d placeholder text(s) filled from the register' % _nf)
json.dump(G,open(os.path.join(ROOT,'data','graph.json'),'w',encoding='utf-8',newline='\n'),ensure_ascii=False)
# the architectures must satisfy their technologies' hard dependencies (build/audit/edges_check.py, 27 Sep 2026): an unmet need of a primary
# technology stops the build; an alternate's is printed as a warning
sys.path.insert(0,os.path.join(ROOT,'build','audit')); import edges_check as _ec
_errs,_warns=_ec.check(G)
for _w in _warns: print('edges_check WARN',_w)
if _errs: raise SystemExit('edges_check: '+'; '.join(_errs))
_SUP=str.maketrans('0123456789-','⁰¹²³⁴⁵⁶⁷⁸⁹⁻')
def tidy(text,lang):
    """Reader-facing polish of the generated chapters — applied to the rendered text, never to the data.
    e-notation from the record texts and the formatters becomes m×10ⁿ (the report's style); the ASCII 'us' of
    the record texts becomes µs; the cataloguer's label 'Honest null' is dropped from the notes (the cell already
    reads 'not published'); first-person wording in the notes is neutralised; the Russian edition gets the
    space as the thousands separator instead of the English comma."""
    def sci(m):
        e=int(m.group(2)); return m.group(1)+'×10'+str(e).translate(_SUP)
    def prose(t):
        t=re.sub(r'(?<![\w/.\-])(\d+(?:\.\d+)?)e([-+]?\d+)(?![\w/])',sci,t)
        t=re.sub(r'(?<=\d) us\b',' µs',t)
        t=re.sub(r'Honest null(?: \[[A-Z]\])? (?:\()?by construction(?:\))?(?=[.:;,]| [-–—]|$)',('by construction' if lang=='en' else ('по построению' if lang=='ru' else 'מעצם הבנייה')),t)   # "Honest null (by construction)" → the reason itself
        t=re.sub(r'Honest null(?: \[[A-Z]\])?[.:;]\s*','',t)
        t=re.sub(r' — (?:\s*— )+',' — ',t); t=re.sub(r'(?<=[^\s|]) —(?= ?\|)','',t)      # an empty segment between separators ("x —  — y", "x — |")
        t=t.replace('the sources I opened','the sources consulted')
        if lang=='ru': t=re.sub(r'(?<=\d),(?=\d{3}\b)','\u00a0',t)
        return t
    # embedded SVG (Figure 8.1 and the like) is markup, not prose: its numbers and separators stay as they are
    parts=re.split(r'(<svg\b.*?</svg>)',text,flags=re.S)
    return ''.join(x if x.startswith('<svg') else prose(x) for x in parts)

# splice the generated graph section (numbered 7 in the public edition) into the reports
def splice(lang,start,end):
    p=os.path.join(ROOT,'report','report_%s.md'%lang.upper()); s=open(p,encoding='utf-8').read()
    sec=sec9(lang); sec=re.sub(r'^(#+ )9(\.\d*)',r'\g<1>7\2',sec,flags=re.M).replace('## 9. ','## 7. ',1)
    sec=re.sub(r'(see|см\.) 8\.(\d+)',r'\1 7.\2',sec); sec=re.sub(r'§9(\.\d+)',r'§7\1',sec); sec=re.sub(r'§8(\.\d+)?',lambda m:'§7'+(m.group(1) or ''),sec)
    sec=tidy(sec,lang)
    # §8 "Machines" (build/machines_chapter.py) follows the graph section; Sources is §9 in the public edition
    sec8=tidy(mc.sec_machines(lang),lang)
    i=s.find(start); j=s.find(end); k=s.rfind('\n---\n',i,j)
    if i<0 or j<0: raise SystemExit('report %s: section markers not found'%lang)
    open(p,'w',encoding='utf-8',newline='\n').write(s[:i]+sec.rstrip()+'\n\n---\n\n'+sec8.rstrip()+'\n'+s[k:])
splice('en','## 7. The technology graph','## 9. References'); splice('ru','## 7. Граф технологий','## 9. Литература')
if os.path.exists(os.path.join(ROOT,'report','report_HE.md')): splice('he','## 7. ','## 9. מקורות')   # markers without the newline — a marker that starts with one loses it at every run   # the Hebrew report (29 Sep 2026): its §7/§8 are regenerated like the others
print('sec9 written', len(sec9('en').split()), len(sec9('ru').split()), '| sec8 (machines)', len(mc.sec_machines('en').split()), len(mc.sec_machines('ru').split()))
