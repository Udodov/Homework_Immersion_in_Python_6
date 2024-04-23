"""Напишите программу банкомат. Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счете
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег
- Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
- Необходимо:
1. Устранить дублирование кода.
2. Вынести проверку баланса на превышение WEALTH_TAX_THRESHOLD в отдельную функцию.
3. Выводить информацию о комиссии, в функции deposit() после добавления суммы на баланс."""

from decimal import Decimal

# Константы
WEALTH_TAX_THRESHOLD = Decimal('5000000')  # Порог для налога на богатство
WEALTH_TAX_RATE = Decimal('0.1')  # Ставка налога на богатство
DEPOSIT_WITHDRAW_MULTIPLE = Decimal('50')  # Кратность суммы для пополнения и снятия
MIN_COMMISSION = Decimal('30')  # Минимальная комиссия за снятие
MAX_COMMISSION = Decimal('600')  # Максимальная комиссия за снятие
COMMISSION_RATE = Decimal('0.015')  # Процент комиссии за снятие
BONUS_RATE = Decimal('0.03')  # Процент бонусов

# Хранилище операций
operations = []


def check_amount_multiple(amount: Decimal) -> bool:
    """Проверяет, кратна ли сумма заданному множителю."""
    return amount % DEPOSIT_WITHDRAW_MULTIPLE == 0


def apply_wealth_tax(balance: Decimal) -> Decimal:
    """Применяет налог на богатство, если это необходимо."""
    if balance > WEALTH_TAX_THRESHOLD:
        wealth_tax = balance * WEALTH_TAX_RATE
        balance -= wealth_tax
        print(f"Налог на богатство {WEALTH_TAX_RATE * 100}%: -{wealth_tax} у.е.")
    return balance


def deposit(balance: Decimal) -> Decimal:
    """Пополняет баланс."""
    amount = Decimal(input(f"Введите сумму кратную {DEPOSIT_WITHDRAW_MULTIPLE} у.е.: "))
    if not check_amount_multiple(amount):
        print(f"Сумма должна быть кратна {DEPOSIT_WITHDRAW_MULTIPLE} у.е.")
        return balance
    balance += amount
    operations.append(('Пополнение', amount))
    print(f"Пополнено: {amount} у.е.")
    return balance


def withdraw(balance: Decimal) -> Decimal:
    """Снимает деньги со счета с учетом комиссии."""
    amount = Decimal(input(f"Введите сумму кратную {DEPOSIT_WITHDRAW_MULTIPLE} у.е.: "))
    if not check_amount_multiple(amount):
        print(f"Сумма должна быть кратна {DEPOSIT_WITHDRAW_MULTIPLE} у.е.")
        return balance
    commission = max(min(amount * COMMISSION_RATE, MAX_COMMISSION), MIN_COMMISSION)
    total_amount = amount + commission
    if total_amount > balance:
        print("Недостаточно средств для снятия.")
        return balance
    balance -= total_amount
    operations.append(('Снятие', amount))
    print(f"Снято: {amount} у.е., комиссия: {commission} у.е.")
    return balance


def apply_bonus(balance: Decimal, operation_count: int) -> Decimal:
    """Начисляет бонусные проценты после каждой третьей операции."""
    if operation_count % 3 == 0:
        bonus = balance * BONUS_RATE
        balance += bonus
        print(f"Бонусные проценты: +{bonus} у.е.")
    return balance


def main() -> None:
    balance = Decimal('0')
    operation_count = 0

    while True:
        print(f"Текущий баланс: {balance} у.е.")

        print("\n Выберите действие:\n1. Пополнить\n2. Снять\n3. Выйти")
        action = input("Введите номер действия: ").strip()

        if action == "3":
            print("Спасибо за использование нашего банкомата!")
            print(f"Конечный баланс: {balance} у.е.")
            # Вывод списка всех операций перед выходом
            if operations:
                print("\nСписок всех операций:")
                for op_number, (op_type, amount) in enumerate(operations, start=1):
                    print(f"{op_number}. {op_type}: {amount} у.е.")
            else:
                print("Операций не было.")
            break
        elif action == "1":
            balance = deposit(balance)
            operation_count += 1
        elif action == "2":
            balance = withdraw(balance)
            operation_count += 1
        else:
            print("Неверный номер действия, попробуйте еще раз.")

        balance = apply_wealth_tax(balance)
        balance = apply_bonus(balance, operation_count)


if __name__ == "__main__":
    main()
