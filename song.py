# create your Song class in this file


class Song:

    def __init__(self, title='', artist='', year='', require=''):
        """
            Insert attribute for Song class
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.require = require

    def require_song(self, require):        # Define check require method
        self.require = require

    def __str__(self):
        return "{},by {},{},{}".format(self.title, self.artist, self.year, self.require)
