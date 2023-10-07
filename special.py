from kivy.uix.textinput import TextInput


# Memory Unit
class MyTextInput(TextInput):
    def __init__(self, font_size, background_color, size_hint, trans):
        super().__init__(font_size=font_size, background_color=background_color, size_hint=size_hint)
        self.trans = trans

    def keyboard_on_key_up(self, window, keycode):
        self.trans()

# Number Systems
class MyBODHText(TextInput):
    def __init__(self, size_hint, font_size, background_color, trans):
        super().__init__(font_size=font_size, size_hint=size_hint, background_color=background_color)
        self.trans = trans

    def keyboard_on_key_up(self, window, keycode):
        self.trans()
