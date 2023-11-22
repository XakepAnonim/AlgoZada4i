import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance


a = Point(2, 4)
b = Point(6, 9)
c = Point(6, 0)

ab = a.calc_distance(b)
bc = b.calc_distance(c)
ca = c.calc_distance(a)

perimeter = ab + bc + ca

print("Периметр треугольника:", perimeter)


