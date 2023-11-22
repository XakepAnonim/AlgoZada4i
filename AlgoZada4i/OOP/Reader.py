class Reader:
    def __init__(self, full_name, library_card_number, faculty, date_of_birth, phone_number):
        self.full_name = full_name
        self.library_card_number = library_card_number
        self.faculty = faculty
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    def takeBook(self, num_books):
        print(f"{self.full_name} взял {num_books} книги.")

    def returnBook(self, num_books):
        print(f"{self.full_name} вернул {num_books} книги.")


reader = Reader("Петров В. В.", "678123", "Факультет читателей", "02.01.2077", "78005553535")

reader.takeBook(3)
reader.returnBook(3)