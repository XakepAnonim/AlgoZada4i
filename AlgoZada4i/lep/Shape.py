class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print("Shape:", self.name)
        print("Color:", self.color)


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__("Circle", color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__("Rectangle", color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, color, base, height):
        super().__init__("Triangle", color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle("красный", 5)
rectangle = Rectangle("синий", 3, 4)
triangle = Triangle("фиолетовый", 6, 8)
circle.describe()
rectangle.describe()
triangle.describe()
print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")