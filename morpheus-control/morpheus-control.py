# GUI for control over "Morpheus 1" vehicle

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MorpheusApp(App):
    connection = None

    def build(self):
        root = self.setup_gui()
        return root

    def setup_gui(self):
        self.label = Label(text='Morpheus 1 control panel')
        self.controlModeBtn = Button(text='Human/Autonomous')
        self.empty13 = Label(text='')
        self.empty21 = Label(text='')

        self.layout = GridLayout(cols = 3)
        self.layout.add_widget(self.controlModeBtn)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.empty13)
        self.layout.add_widget(self.empty21)
        return self.layout

if __name__ == '__main__':
    MorpheusApp().run()

