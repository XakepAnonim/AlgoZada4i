from random import randint

from Zada4i import ThingData, VectorData, Vector3D, Goods, Book, CarData, Thing, AirCastle, GoodIfrit, Wizard

th = Thing('name', 15, 1500)
# print(th)
td = ThingData('qwerty', 12, 2.5)
th.dims.append(10)
print(td)
td2 = ThingData('qwerty', 12, 2.5)
print(td2)


# td = ThingData('name2', 12, 2.5)
# td2 = ThingData('name2', 12, 2.5)
# print(td == td2)
# pprint(ThingData.__dict__)

# ----------------------------------------------------------------------------------------------------------------------

v = Vector3D(1, 2, 3, False)
# print(v.__dict__)
vd = VectorData(1, 4)
vd2 = VectorData(1, 2)
print(vd == vd2)
print(vd)
# print(vd2)

# ----------------------------------------------------------------------------------------------------------------------

g = Goods(1200, 2.5)
print(g)

g1 = Goods(1200, 2.5)
print(g1)

b = Book(2000, 2.5, 'eqwrqwrwq', 'eqwrqwrqwerty')
for i in range(len(b.meassure)):
    b.meassure[1] = randint(10, 20)

print(b)

# ----------------------------------------------------------------------------------------------------------------------

cd = CarData('Lada Granra', 120, 72378432)
print(cd.get_max_speed())
print(cd.get_price())
print(cd)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print('\n#1')
cl = AirCastle(100, 5, "Blue")
cl2 = AirCastle(80, 8, "Red")
print(cl)

cl.change_height(50)
print(cl)

cl + 3
print(cl)

visibility = cl(10)
print(visibility)

print(cl > cl2)
print(cl >= cl2)
print(cl < cl2)
print(cl <= cl2)
print(cl != cl2)
print(cl == cl2)

# ----------------------------------------------------------------------------------------------------------------------

print('\n#2')
gi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness(4)
print(gi)

gi1 = gi + 15
print(gi1)

print(gi(31))

gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)

gi1.change_goodness(2)
print(gi > gi1)
print(gi, gi1, sep='\n')

# ----------------------------------------------------------------------------------------------------------------------

print('\n#3')
gi = Wizard("Gandalf", 90, 60)
gi.change_rating(10)
print(gi)

gi += "The Grey"
print(gi)

print(gi(50))

gi1 = Wizard("Merlin", 80, 35)
gi2 = Wizard("Dumbledore", 95, 70)
print(gi1 < gi2)

gi1.change_rating(-20)
print(gi1 > gi2)

print(gi1, gi2, sep='\n')
