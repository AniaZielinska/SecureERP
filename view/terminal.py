def print_menu(title, list_options):
    if len(list_options) > 1:
        print(f"\n{title}")
        for i in range(len(list_options)-1):
            print(f"({i+1}) {list_options[i+1]}")
        print(f"(0) {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table):
    # Calculate the maximum width for each column
    max_column_widths = []
    for row in table:
        column_widths = []
        for cell in row:
            column_widths.append(len(str(cell)))
        max_column_widths = column_widths if row == table[0] else max_column_widths
        for i in range(len(column_widths)):
            max_column_widths[i] = column_widths[i] if column_widths[i] > max_column_widths[i] else max_column_widths[i]

    # Calculate the total width of the table based on the widest column
    total_width = sum(max_column_widths) + len(table[0]) * 3  # 3 for padding and separator

    # Print the top border
    print("/" + "-" * (total_width - 2) + "\\")

    # Print the data rows
    for row in table:
        row_format = "| " + " | ".join(f"{row[i]:^{max_column_widths[i]}}" for i in range(len(row))) + " |"
        print(row_format)

    # Print the bottom border
    print("\\" + "-" * (total_width - 2) + "/")


def get_input(label):
    user_option = input(f"{label}: ")
    return user_option


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    print(f"\n{message}")
