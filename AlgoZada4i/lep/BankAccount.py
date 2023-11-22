class BankAccount:

    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Депозит: +{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Вывод средств: -{amount}")
        else:
            print("Недостаточно средств!")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Добавление интереса: +{interest}")

    def history(self):
        print("История транзакций:")
        for transaction in self.__transactions:
            print(transaction)
        print(f"Текущий баланс: {self.__balance}")


# создаем объект счета с балансом 100000 и процентом по вкладу 0.05
account = BankAccount(100000, 0.05)

# вносим 15 тысяч на счет
account.deposit(15000)

# снимаем 7500 рублей
account.withdraw(7500)

# начисляем проценты по вкладу
account.add_interest()

# печатаем историю операций
account.history()