from config import FILE_PATH

from utils import load_transactions, print_transactions, sort_transactions

if __name__ == "__main":
    raw_transactions = load_transactions(FILE_PATH)
    sorted_by_date = sort_transactions(raw_transactions)

    print_transactions(sorted_by_date)