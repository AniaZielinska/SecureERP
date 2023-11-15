from model.sales import sales
from view import terminal as view
from datetime import date


def list_transactions():
    transactions = sales.get_table_from_file()
    if transactions is None:
        view.print_error_message("File is empty.")
        return
    transactions.insert(0, sales.HEADERS)
    view.print_table(transactions)


def add_transaction():
    user_inputs = view.get_inputs(sales.HEADERS[1:])
    sales.adding_transaction(user_inputs)


def update_transaction():
    list_transactions()
    line_to_update = view.get_input("Which transaction you want to update? Insert ID")
    id_index = sales.get_id_index_in_file(line_to_update)
    if not id_index:
        view.print_error_message("No transaction with such ID.")
        return
    user_inputs = view.get_inputs(sales.HEADERS[1:])
    sales.update_transaction(id_index, user_inputs)


def delete_transaction():
    list_transactions()
    line_to_delete = view.get_input("What transaction would you like to delete? Insert ID")
    id_index = sales.get_id_index_in_file(line_to_delete)
    if not id_index:
        view.print_error_message("No transaction with such ID.")
        return
    sales.delete_transaction(id_index)


def get_biggest_revenue_transaction():
    transactions = sales.get_table_from_file()
    if transactions is None:
        view.print_error_message("File is empty.")
        return
    price_index = sales.HEADERS.index("Price")
    biggest_revenue_price = transactions[0][price_index]
    for row in transactions:
        if row[price_index] > biggest_revenue_price:
            biggest_revenue_price = row[price_index]
            biggest_revenue_transaction = row
    table = [sales.HEADERS, biggest_revenue_transaction]
    view.print_table(table)


def get_biggest_revenue_product():
    transactions = sales.get_table_from_file()
    if transactions is None:
        view.print_error_message("File is empty.")
        return
    product_id = sales.HEADERS.index("Product")
    price_id = sales.HEADERS.index("Price")
    product_price = []
    biggest_revenue_product = ["", 0]
    product_index = 0
    price_index = 1
    for row in transactions:
        if row[product_id] not in (item[product_index] for item in product_price):
            product_price.append([row[product_id], float(row[price_id])])
            if biggest_revenue_product[price_index] < float(row[price_id]):
                biggest_revenue_product = [row[product_id], float(row[price_id])]
        else:
            for item in product_price:
                if row[product_id] == item[product_index]:
                    item[price_index] = item[price_index] + float(row[price_id])
                    if biggest_revenue_product[price_index] < item[price_index]:
                        biggest_revenue_product = item
    view.print_general_results(biggest_revenue_product, "Biggest revenue product")


def count_transactions_between():
    transactions = sales.get_table_from_file()
    if transactions is None:
        view.print_error_message("File is empty.")
        return
    labels = ["\nFirst date:\nYear", "Month", "Day"]
    year1, month1, day1 = view.get_inputs(labels)
    date1 = date(int(year1), int(month1), int(day1))
    labels = ["\nSecond date:\nYear", "Month", "Day"]
    year2, month2, day2 = view.get_inputs(labels)
    date2 = date(int(year2), int(month2), int(day2))
    date_lower = min(date1, date2)
    date_higher = max(date1, date2)
    number_of_transactions = 0
    date_index = sales.HEADERS.index("Date")
    for row in transactions:
        date_row = row[date_index].split(sep="-")
        date_row = date(int(date_row[0]), int(date_row[1]), int(date_row[2]))
        if date_lower <= date_row <= date_higher:
            number_of_transactions += 1
    view.print_general_results(number_of_transactions, f"Number of transactions between {date_lower} and {date_higher}")


def sum_transactions_between():
    transactions = sales.get_table_from_file()
    if transactions is None:
        view.print_error_message("File is empty.")
        return
    labels = ["\nFirst date:\nYear", "Month", "Day"]
    year1, month1, day1 = view.get_inputs(labels)
    date1 = date(int(year1), int(month1), int(day1))
    labels = ["\nSecond date:\nYear", "Month", "Day"]
    year2, month2, day2 = view.get_inputs(labels)
    date2 = date(int(year2), int(month2), int(day2))
    date_lower = min(date1, date2)
    date_higher = max(date1, date2)
    sum_of_transactions = 0
    date_index = sales.HEADERS.index("Date")
    price_index = sales.HEADERS.index("Price")
    for row in transactions:
        date_row = row[date_index].split(sep="-")
        date_row = date(int(date_row[0]), int(date_row[1]), int(date_row[2]))
        if date_lower <= date_row <= date_higher:
            sum_of_transactions = sum_of_transactions + float(row[price_index])
    view.print_general_results(sum_of_transactions, f"Sum of transactions between {date_lower} and {date_higher}")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
