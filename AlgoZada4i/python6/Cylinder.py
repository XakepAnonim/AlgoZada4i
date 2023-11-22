from math import pi


class Cylinder:

    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return circle * 2 + side

    def __init__(self, diam, high):
        self.diam = diam
        self.high = high
        self.area = self.make_area(self.diam, self.high)

    def __str__(self):
        return f'diam = {self.diam}, high = {self.high}, area = {self.area}'


c = Cylinder(2, 4)
print(c)
