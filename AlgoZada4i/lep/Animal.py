class Animal:

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f"{self.name} подает голос.")

    def move(self):
        print(f"{self.name} двигается.")


class Dog(Animal):
    def __init__(self, name, species, legs, breed):
        super().__init__(name, species, legs)
        self.breed = breed

    def bark(self):
        print(f"{self.name} лает.")


class Bird(Animal):
    def __init__(self, name, species, legs, wingspan):
        super().__init__(name, species, legs)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} летит.")


dog = Dog("Геральт", "Собака", 4, "Доберман")
bird = Bird("Вася", "Птица", 2, "Попугай")
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()
