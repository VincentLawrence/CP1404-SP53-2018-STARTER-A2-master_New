"""
Name: Hav Kokfong
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from song import Song
from songlist import SongList

# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):
    song_list = SongList()
    requireSong = 0
    learnedSong = 0

    def build(self):
        self.title = "Song To learn 2.0"    # Add the title of the program
        self.root = Builder.load_file('app.kv')     # Reference kivy file
        song_list = self.load_songs()
        self.show_song(song_list)   # Loading song using class
        return self.root

    def load_songs(self):  # Loading songs
        result_list = self.song_list.load_song('songs.csv')
        return result_list

    def show_song(self, display_order):  # Display Songs in GUI
        self.requireSong = 0    # For counting require song
        self.learnedSong = 0
        require_colour = (0,1,0,1)
        for i in display_order:
            song_id = i.title
            if i.require is True:   # For counting require song
                to_learn = ''
                self.requireSong += 1
                display = '"{0}" by {1} ({2}){3}'.format(i.title, i.artist, i.year, to_learn)  # Display format
                song_button = Button(id=song_id, text=display, color='')  # Add song to clickable button
                Button.background_color = (0,1,0,1)
                song_button.bind(on_release=self.select)
            else:                           # For counting Learned song
                to_learn = "(Learned)"
                self.learnedSong += 1
                display = '"{0}" by {1} ({2}){3}'.format(i.title, i.artist, i.year, to_learn)   # Display format
                song_button = Button(id=song_id, text=display, color='')    # Add song to clickable button
                song_button.bind(on_release=self.select)
            self.root.ids.all_song.add_widget(song_button)
            # Display learned and to learn song
            self.root.ids.title_learned.text = "To learn: {}, Learned: {}".format(self.requireSong,
                                                                                  self.learnedSong)

    def select(self, instance):     # Display selected song
        song_title = instance.id
        self.root.ids.program_detail.color = (1,1,0,1)
        self.root.ids.program_detail.text = "{} is learned".format(song_title)    # Display selected song format

    def sorting(self, chosen):      # Sort song function
        available_choice = chosen
        if available_choice == 'Title':
            sort_song = self.song_list.sort(0)
        elif available_choice == 'Artist':
            sort_song = self.song_list.sort(1)
        else:
            sort_song = self.song_list.sort(2)
        self.root.ids.all_song.clear_widgets()
        self.show_song(sort_song)

    def add_song(self):     # Add new song to the list
        title = self.root.ids.title_fill.text
        artist = self.root.ids.artist_fill.text
        year = self.root.ids.year_fill.text
        if title == '' or artist == '' or year == '':       # No input validation
            self.root.ids.program_detail.color = (0, 1, 1, 1)
            self.root.ids.program_detail.text = 'Please fill every box'
        elif len(year) != 4:    # Length of year validation
            self.root.ids.program_detail.color = (0, 1, 1, 1)
            self.root.ids.program_detail.text = 'Year must have at least 4 digits'
            try:       # Variable type validation
                year = int(year)
            except ValueError:
                self.root.ids.program_detail.color = (0, 1, 1, 1)
                self.root.ids.program_detail.text = 'Year must be an integer'
        else:
                song_title = self.root.ids.title_fill.text
                song_artist = self.root.ids.artist_fill.text
                song_year = self.root.ids.year_fill.text
                song_input = Song(song_title, song_artist, song_year, True)
                add_list = self.song_list.add_song(song_input)
                self.show_song(add_list)

    def clear_all(self):    # Clear input in text input function
        self.root.ids.title_fill.text = ''
        self.root.ids.artist_fill.text = ''
        self.root.ids.year_fill.text = ''
        self.root.ids.program_detail.text = ''

    def saving(self):
        self.song_list.save_song()


SongsToLearnApp().run()
