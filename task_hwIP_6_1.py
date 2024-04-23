"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

import sys
from calendar import isleap
from datetime import datetime


def _isleap(year: int) -> str:
    """
    Возвращает строку, указывающую, является ли год високосным.

    :param year: Год для проверки.
    :return: Строка "Високосный" или "Не високосный".
    """
    return "Високосный" if isleap(year) else "Не високосный"


def is_valid_date(date_str: str) -> bool:
    """
    Проверяет, может ли существовать дата, представленная строкой в формате 'DD.MM.YYYY'.

    :param date_str: Строка с датой для проверки.
    :return: True, если дата может существовать, иначе False.
    """
    try:
        day, month, year = map(int, date_str.split('.'))
        if not (1 <= year <= 9999):
            return False
        datetime(year, month, day)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    # Проверяем, переданы ли аргументы командной строки
    if len(sys.argv) > 1:
        input_date = sys.argv[1]
    else:
        # Если аргументы не переданы, запрашиваем дату у пользователя
        input_date = input("Пожалуйста, введите дату в формате 'DD.MM.YYYY': ")

    if is_valid_date(input_date):
        _, _, year_check = map(int, input_date.split('.'))
        leap_status = _isleap(year_check)
        print(f"Дата {input_date} корректна, год {leap_status}.")
    else:
        print(f"Дата {input_date} некорректна.")
