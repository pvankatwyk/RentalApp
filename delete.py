####################

<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: 'Starred Properties'
                IconLeftWidget:
                    icon: 'star'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Starred Properties"

            OneLineIconListItem:
                text: 'All Properties'
                IconLeftWidget:
                    icon: 'home'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "All Properties"

            OneLineIconListItem:
                text: 'Settings'
                IconLeftWidget:
                    icon: 'tools'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Settings"
            OneLineIconListItem:
                text: 'Profile'
                IconLeftWidget:
                    icon: 'account'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Profile"

Screen:
    MDToolbar:
        id: toolbar
        title: "Rental App"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["dots-vertical", lambda x: app.callback()]]

    NavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "Starred Properties"
                MDLabel:
                    text: "Starred Properties"
            Screen:
                name: "All Properties"
                MDLabel:
                    text: "All Properties"
            Screen:
                name: "Settings"
                MDLabel:
                    text: "Settings"
            Screen:
                name: "Profile"
                MDLabel:
                    text: "Profile"



        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                Image:
                    id: profile_image
                    source: 'photo.png'
                    size_hint: None,None
                    size: "56dp", "56dp"
                MDLabel:
                    text: "Peter"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "pvankatwyk@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
            ContentNavigatorDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer



from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helpers import username_input, aprsl_price, arv, purchase_price, repair, address, num_units
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

# class ItemDrawer(OneLineIconListItem):
#     icon = StringProperty(None)
#

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )



class RentalApp(MDApp):
    def build(self):
        screen = Builder.load_file("Rental.kv")
        self.theme_cls.primary_palette="Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        return screen

RentalApp().run()





<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: 'Starred Properties'
                IconLeftWidget:
                    icon: 'star'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


Screen:
    MDToolbar:
        id: toolbar
        title: "Rental App"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["dots-vertical", lambda x: app.callback()]]

    NavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "Starred Properties"
                MDLabel:
                    text: "Starred Properties"
            Screen:
                name: "All Properties"
                MDLabel:
                    text: "All Properties"
            Screen:
                name: "Settings"
                MDLabel:
                    text: "Settings"
            Screen:
                name: "Profile"
                MDLabel:
                    text: "Profile"



        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                Image:
                    id: profile_image
                    source: 'photo.png'
                    size_hint: None,None
                    size: "56dp", "56dp"
                MDLabel:
                    text: "Peter"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "pvankatwyk@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
            ContentNavigatorDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer




