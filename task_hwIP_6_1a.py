"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
* в 'одну строку'"""

import sys
from calendar import isleap
from datetime import datetime


def _isleap(year: int) -> str:
    return "Високосный" if isleap(year) else "Не високосный"


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    input_date = sys.argv[1] if len(sys.argv) > 1 else input("Пожалуйста, введите дату в формате 'DD.MM.YYYY': ")
    year_check = int(input_date.split('.')[-1])
    print(
        f"Дата {input_date} {'корректна, год ' + _isleap(year_check) if is_valid_date(input_date) else 'некорректна.'}")
