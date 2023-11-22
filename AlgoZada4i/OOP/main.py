class Person:
    kind = 'men'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('Объект уничтожен')

    def say(self, message):
        print(message)

    def say_hello(self):
        self.say(f'Hello, My name is {self.name}.\nI\'m {self.age} years old.')


tom = Person('Tom', 25)
bob = Person('Bob', 15)

# print(tom.age, tom.kind)x
# print(bob.kind)
# tom.say_hello('hi')
# tom.say('qwerty')
# print(tom.name)
# print(bob.name)
# tom.say_hello()
# bob.say_hello()
tom.height = 1.80
bob.weight = 50
print(tom.height)
del bob
print(bob.weight)