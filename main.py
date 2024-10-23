from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random


class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.5, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.pfp = Image(source="da_rock.jpg")
        self.window.add_widget(self.pfp)
        

        # label widget
        self.greeting = Label(
                        text= "Hey you there! What's your name?",
                        font_size= 18,
                        color= '#FFFF00'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "enter",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=random.choice([self.build2, self.build3]))
        self.window.add_widget(self.button)

        return self.window

    def build2(self, x):
        # change label text and the main image"
        self.greeting.text = "Hi " + self.user.text + "! That's a cool name bro"
        self.pfp.source = "da_rock_pointing.jpg"
    
    def build3(self, x):
        # change label text and the main image"
        self.greeting.text = "HAHAHA,,, " + self.user.text + " is a real ugly name dude."
        self.pfp.source = "da_rock_laugh.jpg"

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()