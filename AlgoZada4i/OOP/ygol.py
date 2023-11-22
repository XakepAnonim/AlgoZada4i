class Treygolnik:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_area(self):
        return 0.5 * self.a * self.b

    def calc_perimeter(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return self.a + self.b + c


triangle = Treygolnik(3, 5)

area = triangle.calc_area()
perimeter = triangle.calc_perimeter()

print("Площадь треугольника:", area)
print("Периметр треугольника:", perimeter)