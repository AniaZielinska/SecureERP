from model.crm import crm
from model import util
from view import terminal as view


def list_customers():
    customers=crm.data_manager.read_table_from_file(crm.DATAFILE)
    customers.insert(0,crm.HEADERS)
    view.print_table(customers)


def add_customer():
    customers = crm.data_manager.read_table_from_file(crm.DATAFILE)
    new_customer_id = util.generate_id()
    name = view.get_input("Enter Name")
    while not crm.is_valid_name(name):
        view.print_error_message("Invalid name. The name can contain only letters and cannot be longer then 25 characters.\nPlease enter a valid name.")
        name = view.get_input("Enter Name")

    email = view.get_input("Enter Email")
    while not crm.is_valid_email(email):
        view.print_error_message("Invalid email format. Please enter a valid email.")
        email = view.get_input("Enter Email")

    subscription_status = view.get_input("Enter Subscription Status (1 for subscribed, 0 for not subscribed)")
    while not crm.is_valid_subscryption_status(subscription_status):
            view.print_error_message("Invalid subscription status. Please enter 0 or 1.")
            subscription_status = view.get_input("Enter Subscription Status (1 for subscribed, 0 for not subscribed)")
    new_customer = [new_customer_id, name, email, subscription_status]
    customers.append(new_customer)
    crm.data_manager.write_table_to_file(crm.DATAFILE, customers)
    view.print_message(f"\nUser added successfully with ID: {new_customer_id}\n")
    list_customers()


def update_customer():
    list_customers()
    customers = crm.data_manager.read_table_from_file(crm.DATAFILE)
    while True:
        customer_id_to_update = view.get_input("Enter the ID of the customer to update")
        customer_to_update = crm.get_customer_by_id(customer_id_to_update)
        if customer_to_update is not None:
            view.print_message("Current customer information:")
            view.print_table([customer_to_update])
            update_name = view.get_input("Enter new name or press Enter to skip")
            if update_name != "":
                while not crm.is_valid_name(update_name):
                    view.print_error_message("Invalid name. The name can contain only letters and cannot be longer then 25 characters.\nPlease enter a valid name.")
                    update_name = view.get_input("Enter new name or press Enter to skip")
            update_email = view.get_input("Enter the new email or press Enter to skip)")
            if update_email != "":
                while not crm.is_valid_email(update_email):
                    view.print_error_message("Invalid email format. Please enter a valid email.")
                    update_email = view.get_input("Enter the new email or press Enter to skip)")
            update_subscription = view.get_input("Enter the updated subscription status (1 for subscribed, 0 for not subscribed, or press Enter to skip)")
            if update_subscription != "":
                while not crm.is_valid_subscryption_status(update_subscription):
                    view.print_error_message("Invalid subscription status. Please enter 0 or 1.")
                    update_subscription = view.get_input("Enter the updated subscription status (1 for subscribed, 0 for not subscribed, or press Enter to skip)")
            if update_name:
                customer_to_update[1] = update_name
            if update_email:
                customer_to_update[2] = update_email
            if update_subscription:
                customer_to_update[3] = update_subscription
            for row in customers:
                if customer_id_to_update == row[0]:
                    customer_index = customers.index(row)
            customers[customer_index] = customer_to_update
            crm.data_manager.write_table_to_file(crm.DATAFILE, customers)
            view.print_message(f"Customer with ID {customer_id_to_update} updated successfully.")
            view.print_table([customer_to_update])
            break
        else:
            view.print_error_message(f"There's no customer with ID: {customer_id_to_update}")
            continue

def delete_customer():
    list_customers()
    customers = crm.data_manager.read_table_from_file(crm.DATAFILE)
    while True:
        customer_id_to_delete = view.get_input("Enter the ID of the customer to delete")
        customer_to_delete = crm.get_customer_by_id(customer_id_to_delete)
        if customer_to_delete is not None:
            customers.remove(customer_to_delete)
            crm.data_manager.write_table_to_file(crm.DATAFILE, customers)
            view.print_message(f"Customer with ID {customer_id_to_delete} deleted successfully.")
            list_customers()
            break
        else:
            view.print_error_message(f"There's no customer with ID: {customer_id_to_delete}")
            continue


def get_subscribed_emails():
    customers_list = crm.data_manager.read_table_from_file(crm.DATAFILE)
    customers = [(row[0], row[1], row[2], bool(int(row[3]))) for row in customers_list]
    subscribed_customers_emails = [customer[2] for customer in customers if customer[3]]
    view.print_message("\nEmails of customers with subscriptions:\n")
    subscription_list = [[email] for email in subscribed_customers_emails]
    view.print_table(subscription_list)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
