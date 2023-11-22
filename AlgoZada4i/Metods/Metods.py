import random
from random import randint
import math


class Passport:

    def __init__(self, first_name, last_name, country, date_ot_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_ot_birth = date_ot_birth
        self.num_of_passport = num_of_passport

    def Info(self):
        print(f'''
\nFullname: {self.first_name} {self.last_name}
Date of Birth: {self.date_ot_birth}
Country: {self.country}
Passport number: {self.num_of_passport}''')

    def __repr__(self):
        return f'Name: {self.first_name} {self.last_name}, Passport: {self.num_of_passport}'


class ForeignPassport(Passport):

    def __init__(self, first_name, last_name, country, date_ot_birth, num_of_passport, visa):
        super().__init__(first_name, last_name, country, date_ot_birth, num_of_passport)
        self.visa = visa

    def Info(self):
        super().Info()
        print('Visa:', self.visa)


# =================================================================================================


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name} {self.make} {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series  # серия

    def __str__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


# =================================================================================================


class Soldier:
    def __init__(self, name='Noname', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))


class Battle:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было"

    def battle(self):  # метод моделирующий сражение
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.u1.make_kick(self.u2)
            else:
                self.u2.make_kick(self.u1)
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)


# =================================================================================================


class Card():
    NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10',
                "Валет", "Дама", "Король", "Туз"]
    MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, i, j):
        self.Mastb = self.MastList[i - 1]
        self.Num = self.NumsList[j - 1]


class DeckOfCards():
    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self, i):
        if 0 <= i <= 55:
            answer = self.deck[i].Num
            answer += " "
            answer += self.deck[i].Mastb
        else:
            answer = "В колоде только 56 карт"
        return answer


# =================================================================================================


class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def add(self, other):
        result = Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def sub(self, other):
        result = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return result

    def mul(self, other):
        if isinstance(other, Vector3D):
            result = self.x * other.x + self.y * other.y + self.z * other.z
        else:
            result = Vector3D(self.x * other, self.y * other, self.z * other)
        return result

    def __mul__(self, other):
        return self.mul(other)

    def __rmul__(self, other):
        return self.mul(other)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __matmul__(self, other):
        result = Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
        return result

    def read(self):
        self.x = int(input("Введите значение x: "))
        self.y = int(input("Введите значение y: "))
        self.z = int(input("Введите значение z: "))


# =================================================================================================


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def increase_side(self, percent):
        self.a *= (1 + percent / 100)
        self.a *= (1 + percent / 100)

    def decrease_side(self, percent):
        self.a *= (1 - percent / 100)
        self.b *= (1 - percent / 100)

    def radius(self):
        r = (self.a * self.b) / math.sqrt((self.a ** 2) + (self.b ** 2))
        return r

    def perimeter(self):
        p = self.a + self.b + math.sqrt((self.a ** 2) + (self.b ** 2))
        return p

    def angles(self):
        a1 = math.degrees(math.atan(self.a / self.b))
        a2 = math.degrees(math.atan(self.b / self.a))
        a3 = 90
        return a1, a2, a3

# =================================================================================================


class Bus:

    def __init__(self, speed, capacity, maxSpeed):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.passengers = []
        self.hasEmprySeats = True
        self.seats = {}

    def planting(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            self.seats[name] = True
            self.hasEmptySeats = True if len(self.passengers) < self.capacity else False
            print(f"{name} сел в автобус.")
        else:
            print("Автобус полон. Куда ты лезешь?")

    def landing(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            del self.seats[name]
            self.hasEmptySeats = True if len(self.passengers) < self.capacity else False
            print(f"{name} вышел из автобуса.")
        else:
            print(f"{name} не найден в автобусе.")

    def augmentation(self, value):
        self.speed += value
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

    def reduction(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.planting(name)
        return self

    def __isub__(self, name):
        self.landing(name)
        return self
