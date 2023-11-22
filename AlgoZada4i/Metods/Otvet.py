from Metods import Passport, ForeignPassport, Scaner, Xerox, Printer, Soldier, Battle, DeckOfCards, Vector3D, Triangle, \
    Bus

MFC = []
p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 457896')
MFC.append(p)
fp = ForeignPassport('Petr', 'Petrov', 'Russia', '25.03.1999', '4785 124356', 'China')
MFC.append(fp)
print(MFC)
for item in MFC:
    item.Info()

# ----------------------------------------------------------------


sklad = []
scaner = Scaner('Mustek', 'BearPow 1200CU', 2010)
sklad.append(scaner)
xerox = Xerox('Xerox', 'Phaser 3120', 2019)
sklad.append(xerox)
printer = Printer("1200", 'hp', 'Laser Jet', 2018)
sklad.append(printer)
print("На складе имеются:")

for x in sklad:
    print(x, end=' ')
    print(x.action())
for x in sklad:
    if isinstance(x, Printer):
        sklad.remove(x)

print("\nНа складе осталось:")
for x in sklad:
    print(x, end=' ')
    print(x.action())

print(scaner <= xerox)

# ----------------------------------------------------------------


first = Soldier('Mr. First',140)
second = Soldier()
second.set_name('Mr. Second')
b = Battle(first,second)
b.battle()
b.who_win()


# ----------------------------------------------------------------


deck = DeckOfCards()
deck.shuffle()
print('Выберите карту из колоды в 56 карт:')
n = int(input())
if n <= 56:
    card = deck.get(n - 1)
    print('Вы взяли карту: ', card, end='.\n')
else:
    print("В колоде только 56 карт")


# ----------------------------------------------------------------


v1 = Vector3D(4, 1, 2)
v1.display()
v2 = Vector3D()
v2.read()
v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()
a = v4 * v3
print(a)
v4 = v1 * 10
v4.display()
v4 = v1 @ v3
v4.display()


# ----------------------------------------------------------------


triangle = Triangle(3, 4)
triangle.increase_side(10)
triangle.decrease_side(5)

circle_radius = triangle.radius()
perimeter = triangle.perimeter()
angles = triangle.angles()

print("Радиус описанной окружности:", circle_radius)
print("Периметр треугольника:", perimeter)
print("Значения углов:", angles)


# ----------------------------------------------------------------


bus = Bus(50, 30, 80)

bus += "Иван"
bus += "Петров"

print("Список пассажиров:", bus.passengers)
print("Места в автобусе:", bus.seats)

bus -= "Петров"

print("Список пассажиров:", bus.passengers)
print("Места в автобусе:", bus.seats)

bus.augmentation(20)
print("Скорость автобуса:", bus.speed)
bus.reduction(10)
print("Скорость автобуса после уменьшения:", bus.speed)
