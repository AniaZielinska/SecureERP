""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def is_valid_name(name):
    contains_non_space = any(char.isalpha() for char in name)
    return contains_non_space and (all(char.isalpha() or char.isspace() for char in name) or len(name) > 25)

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def is_valid_subscryption_status(subscription_status):
    return "1" in subscription_status or "0" in subscription_status

def get_customer_by_id(customer_id):
    customers = data_manager.read_table_from_file(DATAFILE)
    for customer in customers:
        if customer[0] == customer_id:
            return customer
    return None