
import kivy
from kivy.app import App
from kivy.lang import Builder
from translate import Translator

translator = Translator(
  from_lang='de', to_lang='en'
)

class MyApp(App):
    def build(self):
        return Builder.load_string(
'''
BoxLayout:
  orientation: 'vertical'
  display: entry
  Label:id entry
  font_size 24
TextInput:
  id: lang
  font_size: 24
Button:
  text: "Translate!"
  font_size: 28
  on_press: app.translate(lang.text)
'''
  )
  def translate(self, text):
    new = translator.translate(text)
    self.root.display.text = new
       
MyApp().run()