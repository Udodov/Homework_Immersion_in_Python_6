"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
* расстановка в кортеже"""

import random
from typing import List, Tuple

from task_hwIP_6_3 import BOARD_SIZE


def is_safe(row: int, col: int, queens: List[int]) -> bool:
    """
    Проверка, безопасно ли разместить ферзя в данной позиции.
    """
    for prev_col in range(col):
        if queens[prev_col] == row or \
                queens[prev_col] - prev_col == row - col or \
                queens[prev_col] + prev_col == row + col:
            return False
    return True


def find_queens_solutions() -> List[List[Tuple[int, int]]]:
    """
    Генерация 4 успешных расстановок ферзей в виде кортежей координат.
    """
    unique_solutions = []
    while len(unique_solutions) < 4:
        queens = [-1] * BOARD_SIZE
        for col in range(BOARD_SIZE):
            safe_positions = [r for r in range(BOARD_SIZE) if is_safe(r, col, queens)]
            if not safe_positions:
                break
            queens[col] = random.choice(safe_positions)
        if all(is_safe(r, col, queens) for col, r in enumerate(queens)):
            solution_as_tuples = [(col, queens[col]) for col in range(BOARD_SIZE)]
            if solution_as_tuples not in unique_solutions:
                unique_solutions.append(solution_as_tuples)
    return unique_solutions


if __name__ == "__main__":
    random.seed()  # Инициализация генератора случайных чисел
    found_solutions = find_queens_solutions()
    for idx, solution in enumerate(found_solutions, 1):
        print(f"Расстановка #{idx}: {solution}")
