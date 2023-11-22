class Point:
    MIN_COORD = 0
    MAX_COORD = 100
    z = 12345

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.__x = x
        if self.MIN_COORD < y < self.MAX_COORD:
            self.y = y

    @classmethod
    def set_bound(self, left):
        self.MIN_COORD = left

    def __getattribute__(self, item):
        if item == '_Point__x':
            raise ValueError
        return object.__getattribute__(self, item)

    def __str__(self):
        return f'x = {self.__x}, y = {self.y}'

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('getattr ' + item)


    def __delattr(self, item):
        object.__delattr__(self, item)

    def __del__(self):
        print('no object')


p = Point(1, 6)
# p.MAX_COORD = 7000
# p.set_bound(-100)
# p1 = Point(2, 7)
# print(p)
# print(p._Point__x)
# p.set_coord(2, 5)
# p.set_coord(-10, 15)
# print(p)
# print(Point.__dict__)
p.j = 15
Point.__setattr__(p, 'k', 154)
print(p.__dict__)
del p.j
print(p.__dict__)

