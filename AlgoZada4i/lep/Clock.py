class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Нужно ввести целове число')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{h}:{m}:{s}'

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Нужно ввести целове число')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('TypeError')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __le__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('TypeError')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Нельзя сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Нельзя сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds - sc)

    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Нельзя сложить')

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds * sc)


cl = Clock(86400)
cl2 = Clock(23785)
cl3 = Clock(-785)
print(cl.get_time())
cl *= cl2 * cl3
print(cl.get_time())