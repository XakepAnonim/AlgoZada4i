from Zada4i import Car, Book, Pet, Information, Employee, RetailItem, Patient, Procedure

# 1
print('#1\n')
my_car = Car
# my_car.go()

# ----------------------------------------------------------------------------------------------------------------------

# 2
print('\n#2')
book = Book('Name', 'Author', 'Description')

print(book)

# ----------------------------------------------------------------------------------------------------------------------

# 3
print('\n#3')
pet = Pet()

name = input('Введите имя питомца: ')
animal_type = input('Введите тип питомца: ')
age = int(input('Введите возраст питомца: '))

pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

print(f'''
Имя питомца: {pet.get_name()}
Тип питомца: {pet.get_animal_type()}
Возраст питомца: {pet.get_age()}
''')

# ----------------------------------------------------------------------------------------------------------------------

# 4
print('\n#4')
car = Car("2021", "Lada")

print("Ускорение:")
for _ in range(5):
    car.accelerate()
    print("Текущая скорость:", car.get_speed())

print("Торможение:")
for _ in range(5):
    car.brake()
    print("Текущая скорость:", car.get_speed())

# ----------------------------------------------------------------------------------------------------------------------

# 5
print('\n#5')
my_info = Information("Имя", "Адрес", 15, "Номер телефона")
f1_info = Information("Имя друга 1", "Адрес друга 1", 20, "Номер телефона друга 1")
f2_info = Information("Имя друга 2", "Адрес друга 2", 18, "Номер телефона друга 2")

print("Ваша информация:")
print("Имя:", my_info.get_name())
print("Адрес:", my_info.get_address())
print("Возраст:", my_info.get_age())
print("Телефонный номер:", my_info.get_phone_number())
print('\n')
print("Информация о ваших друзьях:")
print("Друг 1:")
print("Имя:", f1_info.get_name())
print("Адрес:", f1_info.get_address())
print("Возраст:", f1_info.get_age())
print("Телефонный номер:", f1_info.get_phone_number())
print("Друг 2:")
print("Имя:", f2_info.get_name())
print("Адрес:", f2_info.get_address())
print("Возраст:", f2_info.get_age())
print("Телефонный номер:", f2_info.get_phone_number())

# ----------------------------------------------------------------------------------------------------------------------

# 6
print('\n#6')
employee1 = Employee("Сьюзан Мейерс", 47899, "Бухгалтерия", "Вице-президент")
employee2 = Employee("Марк Джоунс", 39119, "ИТ", "Программист")
employee3 = Employee("Джой Роджерс", 81774, "Производственный", "Инженер")

print("Данные о сотрудниках:")
print("Сотрудник 1:")
print("Имя:", employee1.get_name())
print("Идентификационный номер:", employee1.get_id_number())
print("Отдел:", employee1.get_department())
print("Должность:", employee1.get_position())
print("\n")
print("Сотрудник 2:")
print("Имя:", employee2.get_name())
print("Идентификационный номер:", employee2.get_id_number())
print("Отдел:", employee2.get_department())
print("Должность:", employee2.get_position())
print('\n')
print("Сотрудник 3:")
print("Имя:", employee3.get_name())
print("Идентификационный номер:", employee3.get_id_number())
print("Отдел:", employee3.get_department())
print("Должность:", employee3.get_position())

# ----------------------------------------------------------------------------------------------------------------------

# 7
print("\n#7")
item1 = RetailItem("Товар №1", "Пиджак", 12, 59.95)
item2 = RetailItem("Товар №2", "Дизайнерские джинсы", 40, 34.95)
item3 = RetailItem("Товар №3", "Рубашка", 20, 24.95)

print("Данные о товарах:")
print("Товар 1:")
print("Имя товара:", item1.get_item_name())
print("Описание:", item1.get_description())
print("Количество на складе:", item1.get_quantity())
print("Цена:", item1.get_price())

print("Товар 2:")
print("Имя товара:", item2.get_item_name())
print("Описание:", item2.get_description())
print("Количество на складе:", item2.get_quantity())
print("Цена:", item2.get_price())

print("Товар 3:")
print("Имя товара:", item3.get_item_name())
print("Описание:", item3.get_description())
print("Количество на складе:", item3.get_quantity())
print("Цена:", item3.get_price())

# ----------------------------------------------------------------------------------------------------------------------


# 8
print('\n#8')
patient = Patient("Иван", "Иванович", "Иванов", "ул. Ленина, д. 10", "Москва",
                  "Московская область", "123456", "8-999-123-45-67",
                  "Мария", "8-999-765-43-21")

procedure1 = Procedure("врачебный осмотр", "сегодняшняя", "Ирвин", 250.00)
procedure2 = Procedure("рентгеноскопия", "сегодняшняя", "Джемисон", 500.00)
procedure3 = Procedure("анализ крови", "сегодняшняя", "Смит", 200.00)

procedures = [procedure1, procedure2, procedure3]

total_cost = sum(procedure.get_cost() for procedure in procedures)

print("Информация о пациенте:")
print("ФИО:", patient.get_full_name())
print("Адрес:", patient.get_address())
print("Телефон:", patient.get_phone_number())
print("Контактное лицо для экстренной связи:", patient.get_emergency_contact())
print()
print("Информация о процедурах:")
for i, procedure in enumerate(procedures):
    print(f"Процедура №{i+1}")
    print("Название процедуры:", procedure.get_name())
    print("Дата:", procedure.get_date())
    print("Врач:", procedure.get_doctor())
    print("Стоимость:", procedure.get_cost())
    print()
print("Общая стоимость всех процедур:", total_cost)

# ----------------------------------------------------------------------------------------------------------------------

# 9
print("\n#9")
print("Оно в 'Employee'")

# ----------------------------------------------------------------------------------------------------------------------

# 10
print("\n#10\n")

# ----------------------------------------------------------------------------------------------------------------------

# 11
print("\n#11")