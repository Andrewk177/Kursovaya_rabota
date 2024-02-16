import json


def get_json_file():
    """
    Считывает файл Json со списком производимых операций по карте или счету
    """
    with open("operations.json") as file:
        file = json.load(file)
        return file

def stars_in_card_number():
    pass

def stars_in_expence():
    pass

