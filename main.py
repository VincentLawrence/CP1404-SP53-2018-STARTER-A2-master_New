"""
Name: Hav Kokfong
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from song import Song
from songlist import SongList

# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):

    def build(self):
        self.title = "Song To learn 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

    def sorting(self):


SongsToLearnApp().run()
