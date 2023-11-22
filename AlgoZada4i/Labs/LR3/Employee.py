class Employee:
    def __init__(self, emp_id, name, department, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position


def find_employee(employee_dict):
    emp_id = input("Введите идентификационный номер сотрудника: ")
    if emp_id in employee_dict:
        employee = employee_dict[emp_id]
        print("Найден сотрудник:")
        print("Идентификационный номер:", employee.get_emp_id())
        print("Имя:", employee.get_name())
        print("Отдел:", employee.get_department())
        print("Должность:", employee.get_position())
    else:
        print("Сотрудник с таким идентификационным номером не найден.")


def add_employee(employee_dict):
    emp_id = input("Введите идентификационный номер сотрудника: ")
    name = input("Введите имя сотрудника: ")
    department = input("Введите отдел сотрудника: ")
    position = input("Введите должность сотрудника: ")
    employee = Employee(emp_id, name, department, position)
    employee_dict[emp_id] = employee
    print("Сотрудник успешно добавлен.")


def update_employee(employee_dict):
    emp_id = input("Введите идентификационный номер сотрудника: ")
    if emp_id in employee_dict:
        employee = employee_dict[emp_id]
        print("Найден сотрудник:")
        print("Идентификационный номер:", employee.get_emp_id())
        print("Имя:", employee.get_name())
        print("Отдел:", employee.get_department())
        print("Должность:", employee.get_position())
        name = input("Введите новое имя сотрудника: ")
        department = input("Введите новый отдел сотрудника: ")
        position = input("Введите новую должность сотрудника: ")
        employee.name = name
        employee.department = department
        employee.position = position
        print("Сотрудник успешно обновлен.")
    else:
        print("Сотрудник с таким идентификационным номером не найден.")


def delete_employee(employee_dict):
    emp_id = input("Введите идентификационный номер сотрудника: ")
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("Сотрудник успешно удален.")
    else:
        print("Сотрудник с таким идентификационным номером не найден.")


def print_menu():
    print("Меню:")
    print("1. Найти сотрудника")
    print("2. Добавить нового сотрудника")
    print("3. Изменить данные сотрудника")
    print("4. Удалить сотрудника")
    print("5. Выйти из программы")


employee_dict = {}

while True:
    print_menu()
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        find_employee(employee_dict)
    elif choice == "2":
        add_employee(employee_dict)
    elif choice == "3":
        update_employee(employee_dict)
    elif choice == "4":
        delete_employee(employee_dict)
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

print("Программа завершена.")