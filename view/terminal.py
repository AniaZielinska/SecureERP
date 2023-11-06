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
    column_widths = [max(len(str(cell)) for row in table for cell in row)]
    total_width = sum(column_widths) + 4 + len(table[0]) - 1
    print("/" + "-" * (total_width - 2) + "\\")
    header = table[0]
    # ToDo coś z indeksami z linijki 40 i 43, muszą być zależne od długości listy a nie na stałe 0, 1, 2
    print(f"| {header[0]:^{column_widths[0]}} | {header[1]:^{column_widths[1]}} | {header[2]:^{column_widths[2]}} |")
    print("|" + "-" * (total_width - 2) + "|")
    for row in table[1:]:
        print(f"| {row[0]:^{column_widths[0]}} | {row[1]:^{column_widths[1]}} | {row[2]:^{column_widths[2]}} |")
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
