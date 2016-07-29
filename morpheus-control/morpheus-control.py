# GUI for control over "Morpheus 1" vehicle

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MorpheusTouchWidget(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            print('speed: ', touch.y)
            print('angle: ', touch.x)

    def on_touch_move(self, touch):
        print('move: ', touch.x, touch.y)
        print('widget size:', self.size)
        # TODO: tell the size of entire root window and divide x,y by width and height to have a number in (0,255) for control of Morpheus robot motors


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

        self.touchController = MorpheusTouchWidget() # send human control input

        self.layout = GridLayout(cols = 3)
        self.layout.add_widget(self.controlModeBtn)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.empty13)
        self.layout.add_widget(self.empty21)
        self.layout.add_widget(self.touchController)
        return self.layout

if __name__ == '__main__':
    MorpheusApp().run()

