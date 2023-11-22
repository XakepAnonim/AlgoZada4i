from Zada4i import Snow, Robot, Talking, SnowFlake

# 1
print('#1\n')
s = Snow(100)
s1 = Snow(5)
s2 = s * 1
s2.make_snow(10)

print('---------------------------------------------------------------------------------------------------------------')

# 2
print('#2\n')
snowflake = SnowFlake(7)
print('Снежинка (snow)')
snowflake.show()

snowflake.thaw(2)
print('\nСнежинка после таяния (thaw)')
snowflake.show()

snowflake.freeze(2)
print('\nСнежинка с увеличением квадрата на 2 (freeze)')
snowflake.show()

snowflake.thicken()
print('\n(thicken)')
print('Я не понял как это делать :c')

print('---------------------------------------------------------------------------------------------------------------')

# 3
print('#3\n')
robot = Robot(50, 50)

robot.move("NEESWN")

path = robot.path()
print("Список координат точек перемещения робота:", path)

position = robot.get_position()
print("Текущая позиция робота:", position)

print('---------------------------------------------------------------------------------------------------------------')

# 4
print('#4')

print('Первый пример\n')
tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')

print('\n')

print('Второй пример\n')
tk = Talking('Pussy')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')
