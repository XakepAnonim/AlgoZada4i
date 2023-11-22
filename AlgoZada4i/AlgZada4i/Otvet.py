from AlgZada4i import Student, Rectangle, Car, BankAccount, Triangle

# 1
student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
print('#1')
student2.info()
print('Средний балл:', student2.average_score())

print('----------------------------------------------------------------')

# 2
rectangle = Rectangle(5, 10)
area = rectangle.area()
perimeter = rectangle.perimeter()

print('\n#2')
print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)

print('----------------------------------------------------------------')

# 3
car = Car("Toyota", "Camry", 2019, 50000)
print('\n#3')
car.info()

car.modify_brand('Honda')
car.modify_mileage(60000)
car.info()

print('----------------------------------------------------------------')

# 4
print('\n#4')
account = BankAccount("Вася Пупкин")
account.display_info()

account.deposit(5000)
account.withdraw(2000)
account.display_info()

print('----------------------------------------------------------------')

# 5
print('\n#5')
triangle = Triangle(5, 5, 5)
print(triangle.get_triangle())
print(triangle.area())

triangle = Triangle(4, 4, 6)
print(triangle.get_triangle())
print(triangle.area())

triangle = Triangle(3, 4, 5)
print(triangle.get_triangle())
print(triangle.area())
