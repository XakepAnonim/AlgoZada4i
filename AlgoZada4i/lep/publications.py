class Publication:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print('Название:', self.title)
        print(f'Автор: {self.author}')
        print(f'Год издания: {self.year}')


class Book(Publication):

    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')


class Magazine(Publication):

    def __init__(self, title, author, year, isbn_number):
        super().__init__(title, author, year)
        self.isbn_number = isbn_number

    def display(self):
        super().display()
        print(f'Номер журнала: {self.isbn_number}')


p = Publication('Название1', 'Автор1', 2015)
p.display()
print()
b = Book('Название2', 'Автор2', 20221, 124657845)
b.display()
print()
b = Magazine('Название3', 'Автор3', 20221, 5)
b.display()