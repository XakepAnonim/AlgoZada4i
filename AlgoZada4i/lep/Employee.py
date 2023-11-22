class Employee:

    def __init__(self, name, age, salary, bonus=0):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus


# создаем сотрудника с именем, возрастом и зарплатой
employee = Employee("Марина Арефьева", 30, 90000)

# устанавливаем бонус для сотрудника
employee.set_bonus(15000)

# выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
print("Имя:", employee.get_name())
print("Возраст:", employee.get_age())
print("Зарплата:", employee.get_salary())
print("Бонус:", employee.get_bonus())
print("Итого начислено:", employee.get_total_salary())
