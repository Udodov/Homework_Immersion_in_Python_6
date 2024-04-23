"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
1)Добавить возможность сортировки предметов по различным критериям (например, вес, ценность, категория).
2)Добавить возможность фильтрации предметов по заданным критериям
   (например, исключить предметы, которые не подходят для определенного сезона)."""

from typing import List, Dict, Callable, Optional

Item = Dict[str, any]
Items = List[Item]
PackingList = List[str]


def sort_by_weight(item: Item) -> float:
    return item['weight']


def sort_by_value(item: Item) -> float:
    return item['value']


def filter_by_category(category: str) -> Callable[[Item], bool]:
    def inner(item: Item) -> bool:
        return item['category'] == category

    return inner


def find_combinations(
        items_list: Items, max_weight_limit: float,
        filter_function: Optional[Callable[[Item], bool]] = None,
        sorting_key: Optional[Callable[[Item], any]] = None
) -> List[PackingList]:
    if sorting_key:
        items_list = sorted(items_list, key=sorting_key)
    if filter_function:
        items_list = list(filter(filter_function, items_list))

    all_combinations = []
    current_combination = []

    def backtrack(remaining_items: Items, current_weight: float) -> None:
        if current_weight <= max_weight_limit:
            all_combinations.append([item['name'] for item in current_combination])
        for index in range(len(remaining_items)):
            next_item = remaining_items[index]
            weight = next_item['weight']
            if current_weight + weight <= max_weight_limit:
                current_combination.append(next_item)
                backtrack(remaining_items[index + 1:], current_weight + weight)
                current_combination.pop()

    backtrack(items_list, 0)
    return all_combinations


def user_input_for_sorting_and_filtering() -> (Optional[Callable[[Item], bool]], Optional[Callable[[Item], any]]):
    print("Выберите критерий сортировки:")
    print("1. Вес")
    print("2. Ценность")
    sort_choice = input("Ваш выбор (1-2): ")

    sorting_key = None
    if sort_choice == '1':
        sorting_key = sort_by_weight
    elif sort_choice == '2':
        sorting_key = sort_by_value

    print("\n Выберите категорию для фильтрации (оставьте пустым для выбора всех):")
    print("Примеры: Оборудование, Кухня, Электроника, Питание, Навигация, Медицина")
    category_choice = input("Категория: ").strip()

    filter_function = None
    if category_choice:
        filter_function = filter_by_category(category_choice)

    return filter_function, sorting_key


# Пример списка предметов
items_example = [
    {"name": "Палатка", "weight": 2.5, "value": 10, "category": "Оборудование", "season": "Любой"},
    {"name": "Спальник", "weight": 1.5, "value": 8, "category": "Оборудование", "season": "Зима"},
    {"name": "Котелок", "weight": 0.5, "value": 5, "category": "Кухня", "season": "Любой"},
    {"name": "Фонарик", "weight": 0.2, "value": 7, "category": "Электроника", "season": "Любой"},
    {"name": "Еда", "weight": 2.0, "value": 9, "category": "Питание", "season": "Любой"},
    {"name": "Вода", "weight": 3.0, "value": 1, "category": "Питание", "season": "Любой"},
    {"name": "Карта", "weight": 0.2, "value": 3, "category": "Навигация", "season": "Любой"},
    {"name": "Аптечка", "weight": 0.5, "value": 2, "category": "Медицина", "season": "Любой"},
    # Добавьте больше предметов по желанию
]

max_weight_input = float(input("Введите максимальный вес рюкзака: "))
filter_function_input, sorting_key_input = user_input_for_sorting_and_filtering()

combinations = find_combinations(
    items_example, max_weight_input,
    filter_function=filter_function_input,
    sorting_key=sorting_key_input
)

print("\n Возможные комбинации предметов:")
for combination_index, combination in enumerate(combinations, start=1):
    print(f"Комбинация {combination_index}: {combination}")
