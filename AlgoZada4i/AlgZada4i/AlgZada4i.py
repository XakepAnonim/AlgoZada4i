import math


class Student:

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print(f'''
Имя: {self.name}
Возраст: {self.age}
Класс: {self.grade}
Оценки: {self.scores}
''')

    def average_score(self):
        return sum(self.scores) / len(self.scores)


# =================================================================================================

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


# =================================================================================================

class Car:

    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def modify_brand(self, new_brand):
        self.brand = new_brand

    def modify_model(self, new_model):
        self.model = new_model

    def modify_year(self, new_year):
        self.year = new_year

    def modify_mileage(self, new_mileage):
        self.mileage = new_mileage

    def info(self):
        print(f'''
Марка: {self.brand}
Модель: {self.model}
Год выпуска: {self.year}
Пробег: {self.mileage}
        ''')


# =================================================================================================

class BankAccount:
    def __init__(self, client, balance=0):
        self.client = client
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Депозировано {amount} рублей. Новый баланс: {self.balance} рублей.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Выведено {amount} рублей. Новый баланс: {self.balance} рублей.")
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(f"Клиент: {self.client}")
        print(f"Баланс: {self.balance} рублей")


# =================================================================================================

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_triangle(self):
        if self.a == self.b == self.c:
            return "Равносторонний треугольник"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
