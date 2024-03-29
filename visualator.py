from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)

Builder.load_file('visu.kv')

class MyLayout(Widget):
    pass

class VisualatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    VisualatorApp().run()