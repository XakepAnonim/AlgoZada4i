class Soda:
    def __init__(self, добавка):
        self.добавка = добавка

    def show_my_drink(self):
        if self.добавка:
            print(f"Газировка и {self.добавка}")
        else:
            print("Обычная газировка")


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        elif not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (int, float)):
            return "Нужно вводить только числа!"
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

class Nikola:
    def __init__(self, имя, возраст):
        self.имя = self.process_name(имя)
        self.возраст = возраст

    def process_name(self, имя):
        if имя != "Николай":
            return f"Я не {имя}, а Николай"
        else:
            return имя

    def __str__(self):
        return f"Имя: {self.имя}, Возраст: {self.возраст}"

class RealString:
    def __init__(self, строка):
        self.строка = строка

    def __len__(self):
        return len(self.строка)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)
        elif isinstance(other, str):
            return len(self) == len(other)
        else:
            return False

    def __add__(self, other):
        if isinstance(other, RealString):
            return len(self) + len(other)
        elif isinstance(other, str):
            return len(self) + len(other)
        else:
            return False

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle

import pytest

@pytest.mark.parametrize("n, expected", [
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (3, [[1], [1, 1], [1, 2, 1]]),
    (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
])

def test_pascal_triangle(n, expected):
    assert pascal_triangle(n) == expected