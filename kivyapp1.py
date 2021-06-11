import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class RootWidget(BoxLayout):
    def __init__(self):
        super(RootWidget, self).__init__()
        
    def button_pressed(self):
        self.lbl.text = "Hello World!"

    
class HelloWorld(App):

    def build(self):
        return RootWidget()


helloWorld = HelloWorld()

helloWorld.run()