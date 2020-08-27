from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helpers import username_input, aprsl_price, arv, purchase_price, repair, address, num_units
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout

class RentalApp(MDApp):
    def build(self):
        screen = Builder.load_file("Rental.kv")
        self.theme_cls.primary_palette="Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        #screen = Screen()

        Title = MDLabel(text = "Rental Property Analysis", theme_text_color = "Primary", pos_hint = {'x': 0.05, 'y': 0.425}, font_style = 'H6')
        Home_Info_Title = MDLabel(text = "Property Information", theme_text_color = "Secondary", pos_hint = {'x': 0.05, 'y': 0.375},
                                  font_style = 'Subtitle2')
        #username = Builder.load_string(username_input)
        #button = MDRectangleFlatButton(text = 'Enter', pos_hint = {'center_x': 0.5, 'center_y': 0.4})

        # address_field = Builder.load_file("Rental.kv")
        # screen.add_widget(address_field)
        #
        # number_units = Builder.load_string(num_units)
        # screen.add_widget(number_units)
        #
        # appraisal = Builder.load_string(aprsl_price)
        # screen.add_widget(appraisal)
        #
        # after_repair_value = Builder.load_string(arv)
        # screen.add_widget(after_repair_value)
        #
        # purchase = Builder.load_string(purchase_price)
        # screen.add_widget(purchase)
        #
        # rehab = Builder.load_string(repair)
        # screen.add_widget(rehab)
        #
        # screen.add_widget(Title)
        # screen.add_widget(Home_Info_Title)
        #screen.add_widget(username)
        #screen.add_widget(button)


        return screen

RentalApp().run()