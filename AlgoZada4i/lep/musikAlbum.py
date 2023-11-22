import random


class MusicAlbum:

    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def get_info(self):
        print(f'''
Название: {self.title}
Исполнитель: {self.artist}
Год выпуска: {self.release_year}
Жанр: {self.genre}
Списко треков: {self.tracklist}
''')

    def play_random_track(self):
        return random.choice(self.tracklist)


album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                     "Hallomann"])

album4.get_info()
album4.play_random_track()
