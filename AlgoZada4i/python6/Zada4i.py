# 1
class Snow:

    def __init__(self, num):
        self.num = num

    def make_snow(self, el):
        for i in range(self.num // el):
            print('*' * el)
        print('*' * (self.num % el))

    def __add__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError

        # if isinstance(other, int):
        #     res = other
        # else:
        #     res = other.num
        res = other if isinstance(other, int) else other.num
        return Snow(self.num + res)

    def __sub__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        res = other if isinstance(other, int) else other.num
        return Snow(self.num - res)

    def __mul__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        return Snow(self.num * other)

    def __floordiv__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        return Snow(self.num // other)

    def __truediv__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        return Snow(self.num // other)


# ======================================================================================================================

# 2
class SnowFlake:

    def __init__(self, side_length):
        if side_length % 2 == 0:
            raise ValueError("Сторона квадрата должна быть нечетным числом.")
        self.side_length = side_length
        self.snowflake = self.create()

    def create(self):
        snowflake = [[" " for _ in range(self.side_length)] for _ in range(self.side_length)]
        mid = self.side_length // 2
        snowflake[mid][mid] = "*"
        for i in range(self.side_length):
            if i != mid:
                snowflake[i][mid] = "*"
                snowflake[mid][i] = "*"
        for i in range(1, mid):
            snowflake[i][i] = "*"
            snowflake[self.side_length - i - 1][self.side_length - i - 1] = "*"
            snowflake[i][self.side_length - i - 1] = "*"
            snowflake[self.side_length - i - 1][i] = "*"
        return snowflake

    def thaw(self, steps):
        for _ in range(steps):
            for i in range(self.side_length):
                if self.snowflake[i][0] == "*":
                    self.snowflake[i][0] = "-"
                if self.snowflake[i][-1] == "*":
                    self.snowflake[i][-1] = "-"
                if self.snowflake[0][i] == "*":
                    self.snowflake[0][i] = "-"
                if self.snowflake[-1][i] == "*":
                    self.snowflake[-1][i] = "-"

    def freeze(self, n):
        new_side_length = self.side_length + 2 * n
        new_snowflake = [["-" for _ in range(new_side_length)] for _ in range(new_side_length)]
        offset = n
        for i in range(self.side_length):
            for j in range(self.side_length):
                new_snowflake[i + offset][j + offset] = self.snowflake[i][j]
        self.side_length = new_side_length
        self.snowflake = new_snowflake

    def thicken(self):
        pass

    def show(self):
        for row in self.snowflake:
            print(" ".join(row))


# ======================================================================================================================

# 3
class Robot:

    def __init__(self, x, y):
        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise ValueError('Координаты долны быть заключены в переделах от 0 до 100')
        self.x = x
        self.y = y
        self.path_list = [(x, y)]

    def move(self, cmds):
        for cmd in cmds:
            if cmd == 'N':
                if self.y < 100:
                    self.y += 1
            elif cmd == 'S':
                if self.y > 0:
                    self.y -= 1
            elif cmd == 'E':
                if self.x < 100:
                    self.x += 1
            elif cmd == 'W':
                if self.x > 0:
                    self.x -= 1
        return self.get_position()

    def path(self):
        return self.path_list

    def get_position(self):
        return self.x, self.y


# ======================================================================================================================

# 4
class Talking:

    def __init__(self, name):
        self.no = 0
        self.yes = 0
        self.answer = True
        self.name = name

    def to_answer(self):
        if self.answer:
            self.yes += 1
            self.answer = False
            return 'moore-moore'
        else:
            self.no += 1
            self.answer = True
            return 'meow-meow'

    def number_yes(self):
        return self.yes

    def number_no(self):
        return self.no
