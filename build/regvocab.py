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
SCOPE = {'typical': ('typical', 'типичное'), 'best': ('best', 'лучшее')}   # the scope of a standard record
FLAGS = {   # the register's caveat slugs on a machine → words (27 Sep 2026: 61 machine pages printed the slugs)
    'no-published-error-rates': ('no published error rates', 'ошибки гейтов не опубликованы'), 'source-not-confirmed': ('source not confirmed', 'источник не подтверждён'),
    'target-not-device': ('a target, not a device', 'цель, не устройство'), 'spec-absent': ('specification absent', 'спецификация отсутствует'),
    'cryo-gap': ('cryogenic details missing', 'нет данных о криогенике'), 'conflicting-claim': ('conflicting claims', 'противоречивые заявления'),
    'schedule-risk': ('schedule risk', 'риск сроков'), 'estimated-baseline': ('estimated baseline', 'оценочная база'),
    'post-selection-dominated': ('post-selection dominates the result', 'результат определяется постселекцией'), 'component-only': ('a component, not a machine', 'компонент, не машина'),
    'press-only': ('press sources only', 'только пресса'), 'no-code-named': ('no code named', 'код не назван'), 'no-device': ('no device yet', 'устройства ещё нет'),
    'conflicting-count': ('conflicting qubit counts', 'противоречивые числа кубитов'), 'vendor-claim': ('company claim', 'заявление компании'),
    'eroded-claim': ('claim later eroded', 'заявление позже ослаблено'), 'code-id-missing': ('code id missing in the register', 'нет идентификатора кода в реестре'),
    'analog-only': ('analog operation only', 'только аналоговый режим'), 'unverified-claim': ('unverified claim', 'непроверенное заявление'),
    'annealer-reference-only': ('annealer reference only', 'только ссылка на отжигатель'), 'phase-flip-unpublished': ('phase-flip time unpublished', 'время фазового переворота не опубликовано'),
    'rebutted-claim': ('claim rebutted', 'заявление опровергнуто'), 'roadmap-missed': ('roadmap date missed', 'срок дорожной карты пропущен'),
    'snippet-only': ('source seen as a snippet only', 'источник виден только фрагментом'), 'code-node-mismatch': ('code and technology disagree', 'код и технология не согласуются'),
    'no-numbers-published': ('no numbers published', 'числа не опубликованы'), 'no-entangling-gate': ('no entangling gate', 'нет перепутывающего гейта'),
    'outlier-claim': ('outlier claim', 'выпадающее заявление'), 'assumption-gap': ('rests on an assumption', 'опирается на допущение'),
    'no-logical-error-rate': ('no logical error rate', 'нет логической ошибки'), 'not-peer-reviewed': ('not peer-reviewed', 'без рецензирования'),
    'no-distance-scaling': ('no distance scaling shown', 'масштабирование по расстоянию не показано'), 'name-not-qubit-count': ('the name is not a qubit count', 'название — не число кубитов'),
    'access-disputed': ('access disputed', 'доступ оспаривается'), 'estimate-only': ('estimate only', 'только оценка'), 'acquisition-unconfirmed': ('acquisition unconfirmed', 'поглощение не подтверждено'),
    'never-user-accessible': ('never accessible to users', 'никогда не была доступна пользователям'), 'test-chip-vs-system': ('test chip, not a system', 'тестовый чип, не система'),
    'unverifiable-vendor-claim': ('unverifiable company claim', 'непроверяемое заявление компании'), 'aggressive-roadmap': ('aggressive roadmap', 'агрессивная дорожная карта'),
    'unverifiable': ('unverifiable', 'непроверяемо'), 'contested': ('contested', 'оспаривается'), 'not-a-qubit': ('not a qubit', 'не кубит'), 'hero-pair-number': ('hero-pair number', 'число для лучшей пары'),
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


def ru_plural(n, forms):
    """the Russian form of a noun after the number n: (one, few, many)"""
    try: n = abs(int(n))
    except (TypeError, ValueError): return forms[2]
    if n % 10 == 1 and n % 100 != 11: return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return forms[1]
    return forms[2]


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


STATUS_T = {'ru': STATUS}   # the register's status word → the language's word ('he': {...} when written)
ACCESS_T = {'ru': ACCESS}


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
TABLES = {'ru': TABLE}   # for window.__MACH.t: {lang: {status, access, scope, plural}}; a language without a table reads the register's English
