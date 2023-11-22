class Figure:

    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')


class Line(Figure):

    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')

    def del_line(self):
        print('Линия удалена')


class Rect(Figure):

    def __init__(self, coors, width, color, right):
        super().__init__(coors, width, color)
        self.right = right

    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')


class Ellipse(Figure):

    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')


f = Figure([1, 2, 4, 5, 7, 8], 2, 'black')
f.draw()
l = Line([1, 1, 5, 6], 6, 'red')
l.draw()
e = Ellipse([5, 5, 2, 9], 4, 'yellow')
e.draw()
r = Rect([1, 8, 6, 2], 6, 'blue', 'not right')
r.draw()
