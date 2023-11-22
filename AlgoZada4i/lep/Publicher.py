class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print("Название:", self.name)
        print("Издание:", self.location)

    def publish(self, message):
        print("Издательство:", message)


class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, name, author):
        print("Издание:", name)
        print("Автор:", author)


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages


publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")
