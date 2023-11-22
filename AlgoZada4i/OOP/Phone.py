class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receiveCall(self, name):
        print("Звонит", name)

    def getNumber(self):
        return self.number


phone1 = Phone("79999999999", "iPhone X", 150)
phone2 = Phone("78888888888", "Samsung Galaxy S21", 170)
phone3 = Phone("76666666666", "Note Book 5", 155)

print("Phone 1 - Number:", phone1.number, "Model:", phone1.model, "Weight:", phone1.weight)
print("Phone 2 - Number:", phone2.number, "Model:", phone2.model, "Weight:", phone2.weight)
print("Phone 3 - Number:", phone3.number, "Model:", phone3.model, "Weight:", phone3.weight)

phone1.receiveCall("Джон")
phone2.receiveCall("Лили")
phone3.receiveCall("Егор")

print("Phone 1 - Number:", phone1.getNumber())
print("Phone 2 - Number:", phone2.getNumber())
print("Phone 3 - Number:", phone3.getNumber())