class Kvadrat:

    def __init__(self, length):
        self.length = length

    def sum_area(self):
        area = self.length ** 2
        return area

    def sum_perimeter(self):
        perimeter = self.length * 4
        return perimeter


kvadrat = Kvadrat(10)

area = kvadrat.sum_area()
print(f'Площадь квадрата: {area}')

perimetr = kvadrat.sum_perimeter()
print(f'Площадь квадрата: {perimetr}')