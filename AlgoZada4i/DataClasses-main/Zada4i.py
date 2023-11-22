from dataclasses import dataclass, field, InitVar, make_dataclass
from pprint import pprint
from typing import Any


class Thing:

    def __init__(self, name, weight, price=0, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f'{self.__dict__}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.price == other.price


# ======================================================================================================================

class Vector3D:

    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0


@dataclass()
class VectorData:
    x: int
    y: int = field(compare=False)
    z: int = field(default=0)
    calc_len: InitVar[bool] = True
    length: float = field(init=False)
    pi: float = field(init=False)

    def __post_init__(self, calc_len):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        self.pi = 3.14


# ======================================================================================================================

@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


class GoodMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0, 0, 0]


@dataclass
class Book(Goods):
    title: str
    author: str
    price: int
    weight: float
    meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)

    def __post_init__(self):
        super().__post_init__()
        print('Book')


# ======================================================================================================================

class Car:

    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


@dataclass
class CarD:
    model: str
    max_speed: int | float
    price: int = field(default=0)

    def get_max_speed(self):
        return self.max_speed

    def get_price(self):
        return self.price


CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', int, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed,
                                    'get_price': lambda self: self.price})


# ======================================================================================================================
# ======================================================================================================================

@dataclass(order=True)
class AirCastle:
    height: int
    cloud_count: int
    color: str

    def change_height(self, value):
        self.height = value if value > -1 else 0

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('Fail')
        self.cloud_count += other
        self.height += other // 5

    def __call__(self, visibly):
        visibility = self.height // visibly * self.cloud_count
        return f'Видимость замка: {visibility}'

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.cloud_count} clouds"


# ======================================================================================================================

@dataclass(order=True)
class GoodIfrit:
    height: int
    name: str
    goodness: int = field(compare=False, default=0)

    def change_goodness(self, value):
        self.goodness = max(0, self.goodness + value)

    def __add__(self, number):
        new_height = self.height + number
        return GoodIfrit(new_height, self.name, self.goodness)

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"


# ======================================================================================================================

@dataclass(order=True)
class Wizard:
    name: str
    rating: int
    age: int

    def change_rating(self, value):
        if value > 0:
            self.rating = min(100, self.rating + value)
            self.age = max(18, self.age - abs(value) // 10)
        else:
            self.rating = max(1, self.rating + value)
            self.age += abs(value) // 10

    def __iadd__(self, other):
        self.rating += len(other)
        self.age = max(18, self.age + len(other) // 10)
        return self

    def __call__(self, args):
        return (args - self.age) * self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age} years old'