import json
from datetime import datetime


def load_transactions(file_path):
    """
    Открывает файл с операциями и сортирует по выполненным (EXECUTED)
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    operations = ([operations for operations in data
                   if operations.get("state") == "EXECUTED"])
    return operations

def hidden_number(card_or_account_number):
    """
    Функция подставляет в номер счета или карты звездочки
    """
    if card_or_account_number is None:
        return "Открыт новый счет"

    splited_number = card_or_account_number.split()

    if card_or_account_number.startswith("Счет"):
        number_for_masking = splited_number.pop()
        masked_number = f"**{number_for_masking[-4:]}"
        splited_number.append(masked_number)
    else:
        number_for_masking = splited_number.pop()
        masked_number = f"{number_for_masking[:4] + ' ** **** ' + number_for_masking[-4:]}"
        splited_number.append(masked_number)
    return " ".join(splited_number)


def sort_transactions(transactions):
    """
    Функция преобразует дату и отбирает 5 последних операций
    """
    formatted_date = []

    for transaction in transactions:
        transaction_date = datetime.strptime(transaction.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        transaction["date"] = transaction_date.strftime("%d.%m.%Y")

        transaction["from"] = hidden_number(transaction.get("from"))
        transaction["to"] = hidden_number(transaction.get("to"))

        formatted_date.append(transaction)

    sorted_operations = sorted(formatted_date, key=lambda x:
                                datetime.strptime(x["date"], "%d.%m.%Y"), reverse=True)
    latest_operations = sorted_operations[:5]

    return latest_operations

def print_transactions(transactions):
    """
    Выводит список последних 5 транзакций со скрытыми номерами счета и карты
    """
    for transaction in transactions:
        print(f"{transaction.get('date')} {transaction.get('description')}")
        print(f"{transaction.get('from')} -> {transaction.get('to')}")
        print(f"{transaction.get('operationAmount').get('amount')} {transaction.get('operationAmount').get('currency').get('name')}")
        print("\n")

