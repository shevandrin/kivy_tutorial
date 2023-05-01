from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (450, 753)


def get_ingridients(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    sugars = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))
    return {'nitro': nitro,
            'salt': salt,
            'sugars': sugars,
            'starts': starts,
            'salting_time': salting_time}


class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0
        ingridients = get_ingridients(mass)
        print(ingridients)
        self.salt.text = ingridients.get('salt') + '+ 5'
        self.nitro.text = ingridients.get('nitro')
        self.starts.text = ingridients.get('starts')
        self.sugars.text = ingridients.get('sugars')
        self.time.text = ingridients.get('salting_time')




class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
