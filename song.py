# create your Song class in this file


class Song:

    def __init__(self, title, artist, year, require):
        self.title = title
        self.artist = artist
        self.year = year
        self.learn = False
        self.require = require

    def require_song(self):
        self.require = True

    def learned_song(self):
        self.learn = False

    def __str__(self):
        return "{},{},{},{},{}".format(self.title, self.artist, self.year, self.require)
