from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class propAnalyzer(MDApp):
    def build(self):
        screen = Builder.load_file("rental.kv")
        return screen

propAnalyzer().run()