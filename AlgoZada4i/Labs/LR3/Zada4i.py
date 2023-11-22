# 1
class Car:
    def go(self):
        print('Go')


# ======================================================================================================================

# 2

class Book:

    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    def __str__(self):
        return f'Book: {self.name}\nAuthor: {self.author}\nPublisher: {self.publisher}'


# ======================================================================================================================

# 3
class Pet:

    def __init__(self):
        self._name = ''
        self._animal_type = ''
        self._age = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_animal_type(self):
        return self._animal_type

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


# ======================================================================================================================

# 4
class Car:
    def __init__(self, year_model, make):
        self._year_model = year_model
        self._make = make
        self._speed = 0

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed


# ======================================================================================================================

# 5
class Information:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


# ======================================================================================================================

# 6
class Employee:
    def __init__(self, name, id_number, department, position):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.position = position

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position


# ======================================================================================================================

# 7
class RetailItem:
    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def get_item_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

# ======================================================================================================================

# 8
class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, region, postal_code, phone_number,
                 emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.region}, {self.postal_code}"

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact(self):
        return f"{self.emergency_contact_name}: {self.emergency_contact_phone}"


class Procedure:
    def __init__(self, name, date, doctor, cost):
        self.name = name
        self.date = date
        self.doctor = doctor
        self.cost = cost

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_doctor(self):
        return self.doctor

    def get_cost(self):
        return self.cost


# ======================================================================================================================

# 9
# Оно в 'Employee'

# ======================================================================================================================

# 10

# ======================================================================================================================

# 11
