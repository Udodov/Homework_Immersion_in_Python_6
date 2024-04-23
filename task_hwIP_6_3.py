"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
* отрисовка расстановки"""

import random
from typing import List

BOARD_SIZE = 8  # Размер шахматной доски


def is_safe(row: int, col: int, board: List[int]) -> bool:
    """
    Проверка, безопасно ли разместить ферзя в данной позиции.
    """
    for prev_col in range(col):
        if board[prev_col] == row or \
                board[prev_col] - prev_col == row - col or \
                board[prev_col] + prev_col == row + col:
            return False
    return True


def print_board(board: List[int]) -> None:
    """
    Печать шахматной доски с ферзями.
    """
    for r in range(BOARD_SIZE):
        line = ""
        for c in range(BOARD_SIZE):
            if board[c] == r:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")


def find_queens_solutions() -> List[List[int]]:
    """
    Генерация 4 успешных расстановок ферзей.
    """
    unique_solutions = []
    while len(unique_solutions) < 4:
        board = [-1] * BOARD_SIZE
        for col in range(BOARD_SIZE):
            safe_positions = [r for r in range(BOARD_SIZE) if is_safe(r, col, board)]
            if not safe_positions:
                break
            board[col] = random.choice(safe_positions)
        if all(is_safe(r, col, board) for col, r in enumerate(board)):
            if board not in unique_solutions:
                unique_solutions.append(board.copy())
    return unique_solutions


if __name__ == "__main__":
    random.seed()  # Инициализация генератора случайных чисел
    found_solutions = find_queens_solutions()
    for idx, solution in enumerate(found_solutions, 1):
        print(f"Расстановка #{idx}:")
        print_board(solution)
