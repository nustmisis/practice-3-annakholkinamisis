# -*- coding: utf-8 -*-
"""
Напишите функцию, которая получает на вход на вход строку с госномером
автомобиля и выводит тип данного госномера или "Fail!", если это не госномер.

Рассматриваемые типы госномеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

В госномерах могут использоваться только цифры и буквы кириллицы, имеющие
графические аналоги в латинском алфавите - А, В, Е, К, М, Н, О, Р, С, Т, У и Х.

В контексте данной задачи корректными считаются номера, записанные в нижнем
регистре без перевода строки, в которых код региона (последние 2 или 3 цифры)
отделен от остальных символов одним знаком пробела. Корректность номера региона
проверять не требуется.

Подробнее о форматах госномеров:
https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5_%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D1%8B%D1%85_%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""

import re
def get_plate_type(plate):
    # ваше решение:
    reg_1A = r"[а,в,е,к,м,н,о,р,с,т,у,х]{1}\d{3}[а,в,е,к,м,н,о,р,с,т,у,х]{2}\s\d{2}"
    reg_1B = r"[а,в,е,к,м,н,о,р,с,т,у,х]{2}\d{3}\s\d{2}"
    reg_2 = r"[а,в,е,к,м,н,о,р,с,т,у,х]{2}\d{4}\s\d{2}"
    reg_3 = r"\d{4}[а,в,е,к,м,н,о,р,с,т,у,х]{2}\s\d{2}"

    if re.match(reg_1A, plate):
        return "1А"
    elif re.match(reg_1B, plate):
        return "1Б"
    elif re.match(reg_2, plate):
        return "2"
    elif re.match(reg_3, plate):
        return "3"
    else:
        return "Fail!"
