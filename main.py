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
    all_widget = []
    requiresong = 0
    learnedsong = 0

    def build(self):
        self.title = "Song To learn 2.0"
        self.root = Builder.load_file('app.kv')
        song_list = self.load_songs()
        self.show_song(song_list)
        self.learned_song(song_list)
        self.requiresong = 0
        self.learnedsong = 0
        return self.root

    def load_songs(self):
        result_list = self.song_list.load_song('songs.csv')
        return result_list

    def learned_song(self, song_list):
        for k in song_list:
            if k.require is True:
                self.requiresong += 1
            else:
                self.learnedsong += 1

    def show_song(self, display_order):
        self.clean()
        # requirement = self.learned_song()
        for i in display_order:
            song_id = i.title
            if i.require is True:
                to_learn = "(Learned)"
            else:
                to_learn = ''
            display = '"{0}" by {1} ({2}) {3}'.format(i.title, i.artist, i.year, to_learn)
            song_button = Button(id=song_id, text=display, color='')
            self.all_widget.append(song_button)
            song_button.bind(on_release=self.select)
            self.root.ids.all_song.add_widget(song_button)

    def select(self, instance):
        song_title = instance.id
        self.root.ids.program_detail.color = (1,1,0,1)
        self.root.ids.program_detail.text = "{} is selected".format(song_title)

    def sorting(self, chosen):
        self.clean()
        available_choice = chosen
        if available_choice == 'Title':
            sort_song = self.song_list.sort(0)
        elif available_choice == 'Artist':
            sort_song = self.song_list.sort(1)
        else:
            sort_song = self.song_list.sort(2)
        self.show_song(sort_song)

    def add_song(self):
        title = self.root.ids.title_fill.text
        artist = self.root.ids.artist_fill.text
        year = self.root.ids.year_fill.text
        if title == '' or artist == '' or year == '':
            self.root.ids.program_detail.color = (0,1,1,1)
            self.root.ids.program_detail.text = 'Please fill every box'
        else:
            song_title = self.root.ids.title_fill.text
            song_artist = self.root.ids.artist_fill.text
            song_year = self.root.ids.year_fill.text
            song_input = Song(song_title, song_artist, song_year, True)
            add_list = self.song_list.add_song(song_input)
            self.show_song(add_list)

    def clean(self):
        for j in self.all_widget:
            self.root.ids.all_song.remove_widget(j)

    def clear_all(self):
        self.root.ids.title_fill.text = ''
        self.root.ids.artist_fill.text = ''
        self.root.ids.year_fill.text = ''
        self.root.ids.program_detail.text = ''


SongsToLearnApp().run()
