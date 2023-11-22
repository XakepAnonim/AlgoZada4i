class CPerson:
    def __init__(self):
        self.name = ""
        self.date = ""
        self.gender = ""

    def set_info(self, name, date, gender):
        self.name = name
        self.date = date
        self.gender = gender

    def get_info(self):
        return {
            "ФИО": self.name,
            "Дата Рождения": self.date,
            "Пол": self.gender
        }

    def __del__(self):
        print("Объект CPerson был уничтожен.")


person = CPerson()
person.set_info("Иванов Иван", "1-1-2077", "Мужской")

info = person.get_info()
for key, value in info.items():
    print(key + ":", value)