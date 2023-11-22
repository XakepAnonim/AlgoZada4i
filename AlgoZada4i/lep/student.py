class Student:

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print(f'''
Имя: {self.name}
Возраст: {self.age}
Класс: {self.grade}
Оценки: {self.scores}
''')

    def average_score(self):
        return sum(self.scores) / len(self.scores)


student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
student2.info()
print('Средний балл:', student2.average_score())
