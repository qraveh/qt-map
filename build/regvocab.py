# -*- coding: utf-8 -*-
"""The register's enumerations as the Russian page prints them (a table per language since 29 Sep 2026; English is the register's own) — one table for both renderers (build/cards.py in Python, the map's
JavaScript through window.__MACH.t), so that a word is translated once (27 Sep 2026: the Russian cards printed DEPLOYED, typical,
lab-only and "32 физических кубитов").

The register's status is a free-text field whose head word(s) are canonical (DEPLOYED, DEMONSTRATED / DEPLOYED, ANNOUNCED (never GA));
the head words are translated, the parenthetical qualifier stays as the register wrote it. Access values that are not in the table
print as written.
"""

STATUS = {   # the register's status word → Russian (the machine is feminine: «машина развёрнута»)
    'DEPLOYED': 'РАЗВЁРНУТА', 'DEPLOYING': 'РАЗВЁРТЫВАЕТСЯ', 'DEMONSTRATED': 'ПРОДЕМОНСТРИРОВАНА', 'ANNOUNCED': 'АНОНСИРОВАНА',
    'PLANNED': 'ЗАПЛАНИРОВАНА', 'RETIRED': 'ВЫВЕДЕНА', 'CONTESTED': 'ОСПАРИВАЕТСЯ', 'DISTRIBUTED': 'РАСПРЕДЕЛЁННАЯ',
    'DEMONSTRATED-in-validation': 'ПРОДЕМОНСТРИРОВАНА (валидация идёт)',
}
ACCESS = {   # the register's access value → Russian
    'lab-only': 'только в лаборатории', 'lab': 'лаборатория', 'n/a': 'н/д', 'not disclosed': 'не раскрыт',
    'cloud service': 'облачный сервис', 'free open-access cloud': 'бесплатное открытое облако', 'was cloud service': 'был облачным сервисом',
    'on-prem sold': 'продаётся для установки у заказчика', 'on-prem sold + cloud': 'продаётся заказчику + облако',
    'cloud service + export sales': 'облачный сервис + экспортные продажи', 'research use': 'исследовательское использование',
    'sold as components': 'продаётся как компоненты', 'on-prem at a national testbed': 'на площадке национального испытательного центра',
    'domestic academic access': 'доступ для отечественных академических групп', 'partners only': 'только партнёры',
    'internal': 'внутреннее использование', 'on-prem': 'у заказчика', 'cloud': 'облако',
}
SCOPE = {'typical': ('typical', 'типичное', 'טיפוסי'), 'best': ('best', 'лучшее', 'הטוב ביותר')}   # the scope of a standard record
FLAGS = {   # the register's caveat slugs on a machine → words (27 Sep 2026: 61 machine pages printed the slugs)
    'no-published-error-rates': ('no published error rates', 'ошибки гейтов не опубликованы', 'לא פורסמו שיעורי שגיאה'), 'source-not-confirmed': ('source not confirmed', 'источник не подтверждён', 'המקור לא אושר'),
    'target-not-device': ('a target, not a device', 'цель, не устройство', 'מטרה, לא התקן'), 'spec-absent': ('specification absent', 'спецификация отсутствует', 'אין מפרט'),
    'cryo-gap': ('cryogenic details missing', 'нет данных о криогенике', 'חסרים פרטי הקריוגניקה'), 'conflicting-claim': ('conflicting claims', 'противоречивые заявления', 'טענות סותרות'),
    'schedule-risk': ('schedule risk', 'риск сроков', 'סיכון בלוח הזמנים'), 'estimated-baseline': ('estimated baseline', 'оценочная база', 'בסיס משוער'),
    'post-selection-dominated': ('post-selection dominates the result', 'результат определяется постселекцией', 'התוצאה נקבעת בסינון בדיעבד (post-selection)'), 'component-only': ('a component, not a machine', 'компонент, не машина', 'רכיב, לא מכונה'),
    'press-only': ('press sources only', 'только пресса', 'מקורות עיתונאיים בלבד'), 'no-code-named': ('no code named', 'код не назван', 'לא צוין קוד'), 'no-device': ('no device yet', 'устройства ещё нет', 'עדיין אין התקן'),
    'conflicting-count': ('conflicting qubit counts', 'противоречивые числа кубитов', 'מספרי קיוביטים סותרים'), 'vendor-claim': ('company claim', 'заявление компании', 'טענת החברה'),
    'eroded-claim': ('claim later eroded', 'заявление позже ослаблено', 'הטענה נשחקה בהמשך'), 'code-id-missing': ('code id missing in the register', 'нет идентификатора кода в реестре', 'חסר מזהה קוד במרשם'),
    'analog-only': ('analog operation only', 'только аналоговый режим', 'פעולה אנלוגית בלבד'), 'unverified-claim': ('unverified claim', 'непроверенное заявление', 'טענה לא מאומתת'),
    'annealer-reference-only': ('annealer reference only', 'только ссылка на отжигатель', 'הפניה למחשב חישול בלבד'), 'phase-flip-unpublished': ('phase-flip time unpublished', 'время фазового переворота не опубликовано', 'זמן היפוך הפאזה לא פורסם'),
    'rebutted-claim': ('claim rebutted', 'заявление опровергнуто', 'הטענה הופרכה'), 'roadmap-missed': ('roadmap date missed', 'срок дорожной карты пропущен', 'מועד מפת הדרכים הוחמץ'),
    'snippet-only': ('source seen as a snippet only', 'источник виден только фрагментом', 'המקור נראה כקטע בלבד'), 'code-node-mismatch': ('code and technology disagree', 'код и технология не согласуются', 'הקוד והטכנולוגיה אינם מתיישבים'),
    'no-numbers-published': ('no numbers published', 'числа не опубликованы', 'לא פורסמו מספרים'), 'no-entangling-gate': ('no entangling gate', 'нет перепутывающего гейта', 'אין שער שזירה'),
    'outlier-claim': ('outlier claim', 'выпадающее заявление', 'טענה חריגה'), 'assumption-gap': ('rests on an assumption', 'опирается на допущение', 'נשען על הנחה'),
    'no-logical-error-rate': ('no logical error rate', 'нет логической ошибки', 'אין שיעור שגיאה לוגית'), 'not-peer-reviewed': ('not peer-reviewed', 'без рецензирования', 'לא עבר ביקורת עמיתים'),
    'no-distance-scaling': ('no distance scaling shown', 'масштабирование по расстоянию не показано', 'לא הוצגה הגדלה עם מרחק הקוד'), 'name-not-qubit-count': ('the name is not a qubit count', 'название — не число кубитов', 'השם אינו מספר הקיוביטים'),
    'access-disputed': ('access disputed', 'доступ оспаривается', 'הגישה שנויה במחלוקת'), 'estimate-only': ('estimate only', 'только оценка', 'הערכה בלבד'), 'acquisition-unconfirmed': ('acquisition unconfirmed', 'поглощение не подтверждено', 'הרכישה לא אושרה'),
    'never-user-accessible': ('never accessible to users', 'никогда не была доступна пользователям', 'מעולם לא הייתה נגישה למשתמשים'), 'test-chip-vs-system': ('test chip, not a system', 'тестовый чип, не система', 'שבב ניסוי, לא מערכת'),
    'unverifiable-vendor-claim': ('unverifiable company claim', 'непроверяемое заявление компании', 'טענת חברה שאי אפשר לאמת'), 'aggressive-roadmap': ('aggressive roadmap', 'агрессивная дорожная карта', 'מפת דרכים אגרסיבית'),
    'unverifiable': ('unverifiable', 'непроверяемо', 'אי אפשר לאמת'), 'contested': ('contested', 'оспаривается', 'שנוי במחלוקת'), 'not-a-qubit': ('not a qubit', 'не кубит', 'אינו קיוביט'), 'hero-pair-number': ('hero-pair number', 'число для лучшей пары', 'ערך של זוג שיא'),
}


def flag_words(slug, L):
    """a caveat slug as words in the page's language (English where the language has none); an unknown slug prints as itself with
    hyphens as spaces"""
    return _pick(L, FLAGS.get(slug, (slug.replace('-', ' '),)))
PLURAL = {   # Russian plural forms: one, few (2–4), many
    'qubits': ('физический кубит', 'физических кубита', 'физических кубитов'),
    'stations': ('технология', 'технологии', 'технологий'),
    'machines': ('машина', 'машины', 'машин'),
}
PLURAL_HE = {   # Hebrew: one form for 1 — the whole phrase, the number word inside it — and one for every other number
    'qubits': ('קיוביט פיזי אחד', 'קיוביטים פיזיים'),
    'stations': ('טכנולוגיה אחת', 'טכנולוגיות'),
    'machines': ('מכונה אחת', 'מכונות'),
}


def ru_plural(n, forms):
    """the Russian form of a noun after the number n: (one, few, many)"""
    try: n = abs(int(n))
    except (TypeError, ValueError): return forms[2]
    if n % 10 == 1 and n % 100 != 11: return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return forms[1]
    return forms[2]


def he_count(n, forms):
    """the Hebrew count phrase of n: forms[0] for 1 («טכנולוגיה אחת»), otherwise 'n forms[1]' («12 טכנולוגיות»)"""
    try: k = abs(int(n))
    except (TypeError, ValueError): k = None
    return forms[0] if k == 1 else '%s %s' % (n, forms[1])


def status_ru(s):
    """DEMONSTRATED / DEPLOYED (open testbed) → ПРОДЕМОНСТРИРОВАНА / РАЗВЁРНУТА (open testbed)"""
    s = s or ''
    head, sep, tail = s.partition('(')
    words = [STATUS.get(w.strip(), w.strip()) for w in head.split('/')]
    return ' / '.join(w for w in words if w) + ((' ' + sep + tail) if sep else '')


def access_ru(a): return ACCESS.get((a or '').strip(), a or '')


# ---------- any language (29 Sep 2026): the register's words have a table per language; a language without one prints the register's
# English (status_l / access_l for the cards in Python, TABLES for the map's JavaScript through window.__MACH.t = {lang: table})
def _pick(L, x):
    from langs import pick
    return pick(L, x)


STATUS_HE = {   # the register's status word → Hebrew (the status words of data/i18n/he-terms.md, masculine as there: the device, התקן)
    'DEPLOYED': 'בהפעלה', 'DEPLOYING': 'בפריסה', 'DEMONSTRATED': 'הודגם', 'ANNOUNCED': 'הוכרז',
    'PLANNED': 'מתוכנן', 'RETIRED': 'הוצא משימוש', 'CONTESTED': 'שנוי במחלוקת', 'DISTRIBUTED': 'מבוזר',
    'DEMONSTRATED-in-validation': 'הודגם (האימות נמשך)',
}
ACCESS_HE = {   # the register's access value → Hebrew
    'lab-only': 'במעבדה בלבד', 'lab': 'מעבדה', 'n/a': 'לא ישים', 'not disclosed': 'לא נמסר',
    'cloud service': 'שירות ענן', 'free open-access cloud': 'ענן פתוח ללא תשלום', 'was cloud service': 'היה שירות ענן',
    'on-prem sold': 'נמכר להתקנה באתר הלקוח', 'on-prem sold + cloud': 'נמכר להתקנה באתר הלקוח + ענן',
    'cloud service + export sales': 'שירות ענן + מכירות לייצוא', 'research use': 'שימוש מחקרי',
    'sold as components': 'נמכר כרכיבים', 'on-prem at a national testbed': 'באתר של מתקן ניסוי לאומי',
    'domestic academic access': 'גישה לקבוצות אקדמיות מקומיות', 'partners only': 'שותפים בלבד',
    'internal': 'שימוש פנימי', 'on-prem': 'באתר הלקוח', 'cloud': 'ענן',
}
STATUS_T = {'ru': STATUS, 'he': STATUS_HE}   # the register's status word → the language's word
ACCESS_T = {'ru': ACCESS, 'he': ACCESS_HE}


def status_l(s, L):
    """the register's status in language L: its head words translated where the language has a table (the parenthetical stays)"""
    t = STATUS_T.get(L)
    if not t: return s or ''
    head, sep, tail = (s or '').partition('(')
    words = [t.get(w.strip(), w.strip()) for w in head.split('/')]
    return ' / '.join(w for w in words if w) + ((' ' + sep + tail) if sep else '')


def access_l(a, L):
    t = ACCESS_T.get(L); return t.get((a or '').strip(), a or '') if t else (a or '')


TABLE = {'status': STATUS, 'access': ACCESS, 'scope': {k: v[1] for k, v in SCOPE.items()}, 'plural': PLURAL}   # the Russian table (the old name)
TABLE_HE = {'status': STATUS_HE, 'access': ACCESS_HE, 'scope': {k: v[2] for k, v in SCOPE.items()}, 'plural': PLURAL_HE}   # plural: (one, other), see he_count
TABLES = {'ru': TABLE, 'he': TABLE_HE}   # for window.__MACH.t: {lang: {status, access, scope, plural}}; a language without a table reads the register's English
