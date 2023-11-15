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
    return table


def adding_transaction(user_input):
    transactions = data_manager.read_table_from_file(DATAFILE)
    user_input.insert(0, util.generate_id())
    transactions.append(user_input)
    data_manager.write_table_to_file(DATAFILE, transactions)


def get_id_index_in_file(given_id):
    data = get_table_from_file()
    for row in data:
        if given_id == row[0]:
            return data.index(row)
    return None


def update_transaction(id_index, user_input):
    transactions = data_manager.read_table_from_file(DATAFILE)
    for i in range(len(user_input)):
        transactions[id_index][i+1] = user_input[i]
    print(transactions)
    data_manager.write_table_to_file(DATAFILE, transactions)


def delete_transaction(id_index):
    transactions = data_manager.read_table_from_file(DATAFILE)
    transactions.pop(id_index)
    data_manager.write_table_to_file(DATAFILE, transactions)



