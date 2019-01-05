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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_list = SongList()
        self.requireSong = 0
        self.learnedSong = 0

    def build(self):
        self.title = "Song To learn 2.0"    # Add the title of the program
        self.root = Builder.load_file('app.kv')     # Reference kivy file
        self.song_list.load_song()
        self.show_song()
        return self.root

    def show_song(self):  # Display Songs in GUI
        for i in self.song_list.song:
            if i.require == 'y':
                song_button = Button(text='' + '"' + i.title + '"' + " by " + i.artist + "(" + i.year + ")",
                                     id=i.title)
                song_button.background_color = [88, 89, 0, 0.3]
            else:
                song_button = Button(text='' + '"' + i.title + '"' + " by " + i.artist + "(" + i.year + ") (learned)",
                                     id=i.title)
                song_button.background_color = [0, 88, 88, 0.3]
            song_button.bind(on_release=self.select)
            self.root.ids.all_song.add_widget(song_button)
            # Display learned and to learn song
            self.root.ids.title_learned.text = "To learn: {}, Learned: {}".format(self.requireSong,
                                                                                  self.learnedSong)

    def select(self, button):     # Display selected song
        if self.song_list.get_song(button.id).require == 'y':
            self.song_list.get_song(button.id).require = 'n'
            self.root.ids.program_detail.text = "{} is learned.".format(button.id)
        else:
            self.song_list.get_song(button.id).require = 'y'
            self.root.ids.program_detail.text = "{} need to learn.".format(button.id)   # Display selected song format
        self.root.ids.program_detail.color = (1,1,0,1)
        self.root.ids.all_song.clear_widgets()
        self.show_song()

    def sorting(self, chosen):      # Sort song function
        available_choice = chosen
        if available_choice == 'Title':
            self.song_list.sort(0)
        elif available_choice == 'Artist':
            self.song_list.sort(1)
        elif available_choice == 'Year':
            self.song_list.sort(2)
        else:
            self.song_list.sort(3)
        self.root.ids.all_song.clear_widgets()
        self.show_song()

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
            song_input = Song(song_title, song_artist, song_year, 'y')
            self.song_list.add_song(song_input)
            self.root.ids.all_song.clear_widgets()
            self.show_song()

    def clear_all(self):    # Clear input in text input function
        self.root.ids.title_fill.text = ''
        self.root.ids.artist_fill.text = ''
        self.root.ids.year_fill.text = ''
        self.root.ids.program_detail.text = ''

    def stop(self):
        self.song_list.save_song()


SongsToLearnApp().run()
