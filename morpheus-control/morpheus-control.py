# GUI for control over "Morpheus 1" vehicle

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MorpheusApp(App):
    connection = None

    def build(self):
        root = self.setup_gui()
        return root

    def setup_gui(self):
        self.label = Label(text='Morpheus 1 control panel')
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.add_widget(self.label)
        return self.layout

if __name__ == '__main__':
    MorpheusApp().run()

