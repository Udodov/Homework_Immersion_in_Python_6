"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

from typing import List, Tuple


def queens_are_safe(queens: List[Tuple[int, int]]) -> bool:
    # Проверяем уникальность координат ферзей, чтобы убедиться, что они не находятся на одной вертикали или горизонтали.
    rows = set()
    cols = set()
    # Для проверки диагоналей используем разность и сумму индексов.
    diagonal_diffs = set()
    diagonal_sums = set()

    for queen in queens:
        row, col = queen

        # Проверяем горизонтали и вертикали
        if row in rows or col in cols:
            return False
        rows.add(row)
        cols.add(col)

        # Проверяем диагонали
        if (row - col) in diagonal_diffs or (row + col) in diagonal_sums:
            return False
        diagonal_diffs.add(row - col)
        diagonal_sums.add(row + col)

    # Если все проверки пройдены успешно, значит, ферзи расположены безопасно.
    return True


# Пример использования
queens_positions = [(1, 5), (2, 3), (3, 1), (4, 7), (5, 2), (6, 8), (7, 6), (8, 4)]
print(queens_are_safe(queens_positions))
