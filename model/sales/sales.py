""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_table_from_file():
    table = data_manager.read_table_from_file(DATAFILE)
    if not table:
        return None
    table.insert(0, HEADERS)
    return table


def give_headers():
    return HEADERS


def adding_transaction(user_input):
    transactions = data_manager.read_table_from_file(DATAFILE)
    transactions.append(user_input)
    data_manager.write_table_to_file(DATAFILE, transactions)
