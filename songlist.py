# create your SongList class in this file
import csv
from operator import attrgetter
from song import Song

class SongList:

    def __init__(self):
        self.song = []

    """ Loading the song from CSV file """
    def load_song(self, songs_csv):
        with open(songs_csv, 'r') as file:
            song_file = csv.reader(file)
            for i in song_file:
                if i[3] == 'y':
                    i[3] = True
                else:
                    i[3] = False
                complete_song = Song(i[0], i[1], i[2], i[3])
                self.song.append(complete_song)
        return self.song

    def sort(self, choice):
        if choice == 0:
            option = 'Title'
        elif choice == 1:
            option = 'Artist'
        elif choice == 2:
            option = 'Year'
        else:
            option = 'learn'
        self.song.sort(key=attrgetter(option))
        return self.song

    def add_song(self):

