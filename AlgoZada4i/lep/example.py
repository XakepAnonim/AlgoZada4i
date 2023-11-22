class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def __del__(self):
        print('Delete')
        DataBase.__init__(self)

    def connect(self):
        print(f'Соединение в БД: {self.user}, {self.password}, {self.port}, {self.user}, {self.password}, {self.port}')

    def close(self):
        print('Соединение разорвано')

    def read(self):
        print('Чтение данных')

    def write(self, data):
        print(f'Записываем данный {data}')


db = DataBase('user1', 'psw1', '8000')
db2 = DataBase('user1', 'psw1', '8000')
print(db)
print(db2)