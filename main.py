
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ButtonTextApp(App):

    def build(self):

        #___INIT GRID___#

        self.box = BoxLayout()
        self.box.cols = 1

        self.gridLeft = GridLayout(rows=4, cols=1)
        self.gridRight = GridLayout(rows=4, cols=1)

        self.box.add_widget(self.gridLeft)
        self.box.add_widget(self.gridRight)

        #___INPUT == OUTPUT___#

        self.labelInput = TextInput(text="Enter some text here", background_color = "white", multiline=False)
        self.labelOut = Label(text="test")

        self.gridLeft.add_widget(self.labelInput)
        self.gridRight.add_widget(self.labelOut)

        self.labelInput.bind(text=self.labelOut.setter('text'))     #permet de changer en direct

        #___PLACE BUTTONS___#

        self.bouton4 = Button(text="yellow", background_color="yellow")
        self.bouton4.bind(on_press=self.buttonClicked)
        self.gridLeft.add_widget(self.bouton4)

        self.bouton5 = Button(text="pink", background_color="pink")
        self.bouton5.bind(on_press=self.buttonClicked)
        self.gridLeft.add_widget(self.bouton5)

        self.bouton6 = Button(text="brown", background_color="brown")
        self.bouton6.bind(on_press=self.buttonClicked)
        self.gridLeft.add_widget(self.bouton6)

        self.bouton1 = Button(text="red", background_color="red")
        self.bouton1.bind(on_press=self.buttonClicked)
        self.gridRight.add_widget(self.bouton1)

        self.bouton2 = Button(text="blue", background_color="blue")
        self.bouton2.bind(on_press=self.buttonClicked)
        self.gridRight.add_widget(self.bouton2)

        self.bouton3 = Button(text="green", background_color="green")
        self.bouton3.bind(on_press=self.buttonClicked)
        self.gridRight.add_widget(self.bouton3)

        return self.box

    def buttonClicked(self, button):
        self.labelOut.color = button.background_color           #permet de changer la couleur


if __name__ == "__main__":
    ButtonTextApp().run()
