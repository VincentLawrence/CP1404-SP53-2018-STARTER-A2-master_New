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

    def build(self):
        self.title = "Song To learn 2.0"
        self.root = Builder.load_file('app.kv')
        song_list = self.load_songs()
        self.show_song(song_list)
        return self.root

    def load_songs(self):
        result_list = self.song_list.load_song('songs.csv')
        return result_list

    def show_song(self, display_order):
        for i in display_order:
            song_id = i.title
            display = '"{0}" by {1} ({2}) {3}'.format(i.title, i.artist, i.year, i.require)
            song_button = Button(id=song_id, text=display, color='')
            # self.all_widget.append(song_button)
            song_button.bind(on_release=self.select)
            self.root.ids.all_song.add_widget(song_button)

    def select(self, instance):
        song_title = instance.id
        self.root.ids.program_detail.color = (1,1,0,1)
        self.root.ids.program_detail.text = "{} is selected".format(song_title)

    def sorting(self, available_choice):
        if available_choice == 'Title':
            sort_song = self.song_list.sort(0)
        elif available_choice == 'Artist':
            sort_song = self.song_list.sort(1)
        elif available_choice == 'Year':
            sort_song = self.song_list.sort(2)
        else:
            sort_song = self.song_list.sort(3)
        self.show_song(sort_song)



SongsToLearnApp().run()
