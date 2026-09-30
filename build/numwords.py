# -*- coding: utf-8 -*-
"""Number words and counted phrases in the three languages (29 Sep 2026).

The hand-written narratives of §8.3 name the register's counts through placeholders — {{N_A_ATOM_RB_MACH_CAP}} prints
"Fifteen machines" / «Пятнадцать машин» / «חמש-עשרה מכונות» — so a re-cut of the register can no longer leave "Thirteen machines"
standing in front of fifteen (the editor, 29 Sep 2026: "check completeness of propagation … design this process for effectiveness").
Words up to twenty where the language writes them, digits above; Russian declines the noun by the number, Hebrew agrees the
number with the noun's gender (מכונה feminine, התקן masculine)."""

EN = {0: 'no', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
      12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
RU_M = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
        11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
        18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать'}
RU_F = {**RU_M, 1: 'одна', 2: 'две'}
RU_N = {**RU_M, 1: 'одно', 2: 'два'}
HE_M = {1: 'אחד', 2: 'שני', 3: 'שלושה', 4: 'ארבעה', 5: 'חמישה', 6: 'שישה', 7: 'שבעה', 8: 'שמונה', 9: 'תשעה', 10: 'עשרה', 11: 'אחד-עשר',
        12: 'שנים-עשר', 13: 'שלושה-עשר', 14: 'ארבעה-עשר', 15: 'חמישה-עשר', 16: 'שישה-עשר', 17: 'שבעה-עשר', 18: 'שמונה-עשר', 19: 'תשעה-עשר', 20: 'עשרים'}
HE_F = {1: 'אחת', 2: 'שתי', 3: 'שלוש', 4: 'ארבע', 5: 'חמש', 6: 'שש', 7: 'שבע', 8: 'שמונה', 9: 'תשע', 10: 'עשר', 11: 'אחת-עשרה',
        12: 'שתים-עשרה', 13: 'שלוש-עשרה', 14: 'ארבע-עשרה', 15: 'חמש-עשרה', 16: 'שש-עשרה', 17: 'שבע-עשרה', 18: 'שמונה-עשרה', 19: 'תשע-עשרה', 20: 'עשרים'}

# noun forms: en (one, many); ru (one, few, many, gender); he (one, many, gender)
NOUNS = {'machine': {'en': ('machine', 'machines'), 'ru': ('машина', 'машины', 'машин', 'f'), 'he': ('מכונה', 'מכונות', 'f')},
         'device': {'en': ('device', 'devices'), 'ru': ('устройство', 'устройства', 'устройств', 'n'), 'he': ('התקן', 'התקנים', 'm')},
         'row': {'en': ('row', 'rows'), 'ru': ('строка', 'строки', 'строк', 'f'), 'he': ('שורה', 'שורות', 'f')},
         'cell': {'en': ('cell', 'cells'), 'ru': ('ячейка', 'ячейки', 'ячеек', 'f'), 'he': ('תא', 'תאים', 'm')}}


def digits(lang, n):
    s = f'{n:,}'
    return s.replace(',', ' ') if lang == 'ru' else s   # Russian groups thousands with a space


def ru_form(n, forms):
    """the noun after a numeral written in digits: 21 машина, 22 машины, 25 машин"""
    if n % 10 == 1 and n % 100 != 11: return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return forms[1]
    return forms[2]


def word(lang, n, gender='m'):
    """the bare number: a word up to twenty (Hebrew: in the noun's gender), digits above; 'no'/'ноль'/'0' for zero"""
    if lang == 'en': return EN.get(n, digits(lang, n))
    if lang == 'ru': return {'m': RU_M, 'f': RU_F, 'n': RU_N}.get(gender, RU_M).get(n, digits(lang, n))
    if lang == 'he': return (HE_F if gender == 'f' else HE_M).get(n, digits(lang, n)) if n else '0'
    return str(n)


def phrase(lang, n, noun):
    """the counted noun: 'seven devices' / «семь устройств» / «שבעה התקנים»; 'no device' / «ни одного устройства» / «אף לא התקן אחד»"""
    N = NOUNS[noun][lang]
    if lang == 'en':
        return ('no ' + N[0]) if n == 0 else word('en', n) + ' ' + (N[0] if n == 1 else N[1])
    if lang == 'ru':
        g = N[3]
        if n == 0: return ('ни одной ' if g == 'f' else 'ни одного ') + N[1]   # genitive singular = the 'few' form for these nouns
        if n <= 20: return word('ru', n, g) + ' ' + ru_form(n, N)
        return digits('ru', n) + ' ' + ru_form(n, N)
    if lang == 'he':
        g = N[2]; one = ' אחת' if g == 'f' else ' אחד'
        if n == 0: return 'אף לא ' + N[0] + one
        if n == 1: return N[0] + one
        if n <= 20: return word('he', n, g) + ' ' + N[1]
        return digits('he', n) + ' ' + N[1]
    return f'{n} {noun}'


def cap(s):
    return s[:1].upper() + s[1:] if s else s


if __name__ == '__main__':
    for L in ('en', 'ru', 'he'):
        print(L, ' | '.join(phrase(L, n, 'machine') for n in (0, 1, 2, 3, 5, 13, 21, 22, 75)), '||', ' | '.join(phrase(L, n, 'device') for n in (0, 1, 2, 4, 7, 11, 58)))
