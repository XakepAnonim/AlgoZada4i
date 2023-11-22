class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        return self.__rank

    def confirm_service_number(self, number):
        return self.__service_number == number

    def promote(self):
        if self.__rank == "рядовой":
            self.__rank = "сержант"
        elif self.__rank == "сержант":
            self.__rank = "лейтенант"
        elif self.__rank == "лейтенант":
            self.__rank = "капитан"
        else:
            print("Нельзя повысить звание")

    def demote(self):
        if self.__rank == "капитан":
            self.__rank = "лейтенант"
        elif self.__rank == "лейтенант":
            self.__rank = "сержант"
        elif self.__rank == "сержант":
            self.__rank = "рядовой"
        else:
            print("Нельзя понизить звание")


soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
print(soldier1.get_rank())
soldier1.promote()
print(soldier1.get_rank())
soldier1.demote()
print(soldier1.get_rank())