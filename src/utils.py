import json
from datetime import datetime


def get_json_file():
    """
    Считывает файл Json со списком производимых операций по карте или
    счету и выбирает выполненные операции по ключу
    """
    with open("operations.json") as file:
        file = json.load(file)
        completed_operations = []
        for state in file :
            if state["state"] == "EXECUTED":
                completed_operations.append(state)
        return completed_operations


def date_format_sort_executed(list_: list[dict, ...]) -> list[dict, ...]:
    """
    Преобразует дату в привычный формат и выбирает 5 последних операций
    """
    datetime.fromisoformat('%d.%m.%Y')
    latest_transactions = sorted(list_, key=lambda date: date["date"], reverse=True)
    return latest_transactions[:5]


def stars_in_number(list_: list[dict, ...]) -> list[str, ...]:
    """
    Функция меняет часть номера карты/счета на звездочки
    """
    list_cards_number = [card.get("from") for card in list_]
    list_account_number = [number.split()[-1] for number in list_cards_number if number is not None]
    cards_number = [number[:6] + "*" * 6 + number[-4:] for number in list_account_number if len(number) < 20]
    hidden_numbers = ("".join([f"{cards_number[0][:4]} {cards_number[0][4:8]} {cards_number[0][8:12]} {cards_number[0][12:16]}," 
                               f"{cards_number[1][:4]} {cards_number[1][4:8]} {cards_number[1][8:12]} {cards_number[1][12:16]}"])
                                .split(","))
    hidden_numbers.append("**" + list_account_number[2][len(list_account_number[2]) - 4:])
    numbers_list = []
    for number in cards_number:
        if number is not None:
            for num in number:
                if num.isalpha():
                    numbers_list.append(num)
    return hidden_numbers

def get_operations_hidden_number():
    """
    Функция выводит результат
    """
    pass

