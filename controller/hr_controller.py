from model.hr import hr
from model import util
from view import terminal as view
from datetime import datetime

def list_employees():
    employees=hr.data_manager.read_table_from_file(hr.DATAFILE)
    employees.insert(0, hr.HEADERS)
    view.print_table(employees)
def check_name(name):
        if not name.isalpha() or len(name)>25 or len(name)==0:
            view.print_message("The name cannot contain numbers and cannot be longer then 25 chars. Please provide a name.")
            return True
        else:
            return False

def add_employee():
    employees=hr.data_manager.read_table_from_file(hr.DATAFILE)
    name=""
    while not name:
        name = view.get_input("Name")
        if check_name(name):
            name=""
        
    birth_date = ""
    while not birth_date:
        birth_date = view.get_input("Birth date")
        try:
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            view.print_message("Please provide a valid birth date (YYYY-MM-DD).")
            birth_date = ""
    department=""
    while not department:
        department=view.get_input("Department")
        if 0==len(department)or len(department)>25:     
            view.print_message("Department name cannot be longer than 25 chars. Please provide a valid department name.")
            department=""
    clearance=""
    while not clearance:
        clearance = view.get_input("Clearance")
        if clearance in {"1","2","3","4","5","6","7"}:
            break
        else:
            view.print_message("Please provide a numeric clearance level (1-7).")
            clearance=""
    while True:
        new_employee = {
            "Id": util.generate_id(),
            "Name": name.capitalize(),
            "Date of birth": birth_date,
            "Department": department,
            "Clearance": clearance
        }
        if new_employee.values in employees:
            continue
        else:
            employees.append(new_employee.values())
            hr.data_manager.write_table_to_file(hr.DATAFILE, employees)
            break
    view.print_message("Employee added successfully.")
def update_employee_message(employees, id, i):
    hr.data_manager.write_table_to_file(hr.DATAFILE, employees)
    view.print_general_results(i, "Employee details")
    view.print_message(f"The employee {id} details have been successfully updated.")
def update_employee():
    employees=hr.data_manager.read_table_from_file(hr.DATAFILE)
    id=view.get_input("Enter ID of the employee to update")
    found = False
    for i in employees:
        if id == i[0]:
            found = True
            options = ["Back to HR menu","Name","Department","Clearance"]
            view.print_menu("Data to update:", options)
            user_option=""
            while user_option!="0":
                user_option=view.get_input("Select an operation")
                match user_option:
                    case "0":
                        return
                    case "1":
                        new_name=""
                        while not new_name:
                            new_name = view.get_input("New name")
                            if check_name(new_name):
                                new_name=""
                        i[1]=new_name
                        update_employee_message(employees, id, i)
                    case "2":
                        new_department=""
                        while not new_department:
                            new_department=view.get_input("New depertment")
                            if 0==len(new_department)or len(new_department)>25:     
                                view.print_message("Department name cannot be longer than 25 chars. Please provide a valid department name.")
                                new_department=""
                        i[3]=new_department
                        update_employee_message(employees, id, i)
                    case "3":
                        new_clearance=""
                        while not new_clearance:
                            new_clearance = view.get_input("New clearance")
                            if new_clearance in {"1","2","3","4","5","6","7"}:
                                break
                            else:
                                view.print_message("Please provide a numeric clearance level (1-7).")
                                new_clearance=""
                        i[4]=new_clearance
                        update_employee_message(employees, id, i)
                    case _:
                        view.print_error_message("There is no such option.")
            StopIteration
    if not found:
        view.print_error_message(f"No employee found with ID {id}.")

def delete_employee():
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    id_to_delete = view.get_input("Enter ID of the employee to delete")
    found=False
    for i in employees:
        if i[0] == id_to_delete:
            found=True
            user_option=view.get_input(f"Are you sure you want to delete the employee {id_to_delete}? Type \"Yes\" or \"No\"")
            if user_option.lower()=="yes":
                view.print_message(f"Employee with ID {id_to_delete} deleted successfully.")
                employees.remove(i)
                hr.data_manager.write_table_to_file(hr.DATAFILE, employees)
            else:
                break
        StopIteration
    if not found:
        view.print_message(f"No employee found with ID {id_to_delete}.")

def get_oldest_and_youngest():
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    table_of_dates=[]
    for i in employees:
        i[2] =str(i[2]).replace("-", "")
        i[2]=int(i[2])
        table_of_dates.append(i[2])
    earliest_birth_date = min(table_of_dates)
    latest_birth_date = max(table_of_dates)
    oldest_employees = [o[1] for o in employees if o[2] == earliest_birth_date]
    youngest_employees = [y[1] for y in employees if y[2] == latest_birth_date]
    earliest_birth_date=str(earliest_birth_date)
    latest_birth_date=str(latest_birth_date)
    view.print_general_results(oldest_employees, f"Oldest employees ({earliest_birth_date[:4]}-{earliest_birth_date[4:6]}-{earliest_birth_date[6:]})")
    view.print_general_results(youngest_employees, f"Youngest employees ({latest_birth_date[:4]}-{latest_birth_date[4:6]}-{latest_birth_date[6:]})")
    return tuple(oldest_employees), tuple(youngest_employees)

def get_average_age():
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    current_year = datetime.now().year
    total_age = 0
    for i in employees:
        i[2] = datetime.strptime(i[2], "%Y-%m-%d")
        age = current_year - i[2].year
        total_age += age
    average_age = total_age / len(employees)
    view.print_general_results(average_age, "Average age of employees")
    return average_age

def next_birthdays(days_left=14):
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    upcoming_birthdays = {}
    for i in employees:
        birth_date = datetime.strptime(i[2], "%Y-%m-%d")
        next_birthday = datetime(datetime.now().year, birth_date.month, birth_date.day)
        birthday_next_year = datetime(datetime.now().year+1, birth_date.month, birth_date.day)
        if 0 <= (next_birthday - datetime.now()).days <= days_left:
            upcoming_birthdays[i[0]] = next_birthday.strftime("%Y-%m-%d")
        elif 0 <= (birthday_next_year - datetime.now()).days <= days_left:
            upcoming_birthdays[i[0]] = birthday_next_year.strftime("%Y-%m-%d")
    if not upcoming_birthdays:
        view.print_message(f"There are no birthdays coming up for the next {days_left} days.")
    else:
        employees_birthday=[]
        names_to_return=[]
        for i in employees:
            if i[0] in upcoming_birthdays:
                employees_birthday.append([i[1],i[2]])
                names_to_return.append(i[1])
        view.print_message("Upcoming birthdays!")
        view.print_table(employees_birthday)
        return tuple(names_to_return)

def count_employees_with_clearance():
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    user_input=""
    while user_input!="0":
        user_input=view.get_input("Type clearance (1-7) or type \"0\" to come back to HR menu")
        match user_input:
            case "0":
                break
            case "1"|"2"|"3"|"4"|"5"|"6"|"7":
                count=0
                table_of_clearance=[]
                for i in employees:
                    if i[4]==user_input:
                        count+=1
                        table_of_clearance.append([count,i[0],i[1],i[4]])
                view.print_table(table_of_clearance)
                return count
            case _:
                view.print_error_message("Please provide a numeric clearance level (1-7).\n")
                continue

def count_employees_per_department():
    employees = hr.data_manager.read_table_from_file(hr.DATAFILE)
    dictionary_of_departments={}
    for i in employees:
        department = i[3]
        if department:
            if department in dictionary_of_departments:
                dictionary_of_departments[department] += 1
            else:
                dictionary_of_departments[department] = 1
    view.print_general_results(dictionary_of_departments, "Number of employees per department ")

    return dictionary_of_departments


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
