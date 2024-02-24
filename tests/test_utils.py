from utils import hidden_number
from utils import load_transactions
from utils import sort_transactions
from utils import print_transactions
import json


def test_load_transactions(tmp_path):
    test_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file)
    result = load_transactions(file_path)
    assert len(result) == 2
    assert all(operations.get("state") == "EXECUTED" for operations in result)


def test_hidden_number():
    assert hidden_number(None) == "Открыт новый счет"
    assert hidden_number("Счет 1234 5678 9012 3456") == "Счет 1234 5678 9012 **3456"


def test_sort_transactions():
    transactions = [
        {"date": "2022-01-15T08:00:00.000", "from": "1234 5678 9012 3456", "to": "9876 5432 1098 7654"},
        {"date": "2022-01-10T12:30:00.000", "from": "5678 1234 9012 3456", "to": "5432 9876 1098 7654"},
        {"date": "2022-01-20T15:45:00.000", "from": "9012 3456 1234 5678", "to": "1098 7654 5432 9876"}
    ]
    sorted_result = sort_transactions(transactions)
    assert sorted_result[0]["date"] == "20.01.2022"
    assert sorted_result[1]["date"] == "15.01.2022"


def test_print_transactions(capsys):
    transactions = [
        {
            "date": "2022-01-15",
            "description": "Payment",
            "from": "1234 5678 9012 3456",
            "to": "9876 5432 1098 7654",
            "operationAmount": {"amount": 100, "currency": {"name": "USD"}}
        },
        {
            "date": "2022-01-10",
            "description": "Transfer",
            "from": "5678 1234 9012 3456",
            "to": "5432 9876 1098 7654",
            "operationAmount": {"amount": 50, "currency": {"name": "EUR"}}
        }
    ]
    expected_output = [
        "2022-01-15 Payment",
        "1234 5678 9012 3456 -> 9876 5432 1098 7654",
        "100 USD",
        "/n",
        "2022-01-10 Transfer",
        "5678 1234 9012 3456 -> 5432 9876 1098 7654",
        "50 EUR",
        "/n"
    ]

    print_transactions(transactions)
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    assert output_lines == expected_output

