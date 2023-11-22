class Vector:
    '''qwerty'''
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x):
            self.x = x

        if Vector.validate(y):
            self.y = y

        print(Vector.norm2(self.x, self.y))
        print(self.norm2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD < arg < cls.MAX_COORD


v = Vector(1, 5)
# print(v.validate(6))
# print(v.__dict__)
# print(Vector.__dict__)