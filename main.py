from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen, ScreenManager
from special import MyTextInput, MyBODHText
from settings import *


# App
class Program(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Screen 1
        self.wid_input = MyTextInput(font_size=100, background_color=YELLOW, size_hint=(3.8, 1), trans=self.transforming)
        self.wid_text = Label(text='...', font_size=50, color=YELLOW)
        self.wid_from = Spinner(text='Choose', values=bits, font_size=100, color=RED, background_color=GREEN, background_normal='')
        self.wid_to = Spinner(text='Choose', values=bits, font_size=100, color=GREEN, background_color=RED, background_normal='')

        # Screen 3
        self.wid3_label = Label(color=YELLOW, font_size=55)
        self.wid3_to = Spinner(text='Choose', values=number_system, font_size=110, background_color=RED, color=GREEN, background_normal='')
        self.wid3_from = Spinner(text='Choose', values=number_system, font_size=110, background_color=GREEN, color=RED, background_normal='')
        self.wid3_input = MyBODHText(font_size=100, background_color=YELLOW, size_hint=(3.9, 1), trans=self.appTransform)

        self.sm = ScreenManager()  # Creating ScreenManager

    def build(self):
        # Window Settings

        self.title = name
        self.icon = icon

        # xScreens
        sc1 = Screen(name='project')
        sc2 = Screen(name='info')
        sc3 = Screen(name='numsys')
        sc4 = Screen(name='info2')

        # Screen 1
        box = BoxLayout(orientation='vertical')
        box1 = BoxLayout(orientation='horizontal')
        self.wid_from.bind(text=self.transforming)
        self.wid_to.bind(text=self.transforming)
        wid_info = Button(background_normal=img_info, background_down=img_info, on_press=self.go_to_info)
        wid_numsys = Button(text='Number\nSystems', color=YELLOW, background_color=BLUE, background_normal="", font_size=33, on_press=self.go_to_NumSys)

        # Screen 2
        ibox = BoxLayout(orientation='vertical')
        ibox1 = BoxLayout(orientation='horizontal')
        wid2_go_back = Button(background_normal=img_go_back, background_down=img_go_back, on_press=self.go_to_project)
        wid2_infotext = Label(text=infotext, font_size=17, size_hint=(1.75, 1), color=YELLOW)
        wid2_infotext2 = Label(text=infotext2, font_size=17, color=YELLOW)

        # Screen 3
        jbox = BoxLayout(orientation='vertical')
        jbox1 = BoxLayout(orientation='horizontal')
        self.wid3_from.bind(text=self.appTransform)
        self.wid3_to.bind(text=self.appTransform)
        wid3_back = Button(text='Memory\nUnit\nSystem', color=YELLOW, background_color=BLUE, background_normal="", font_size=32, on_press=self.go_to_project)
        wid3_info = Button(background_normal=img_info2, background_down=img_info2, on_press=self.go_to_info2)

        # Screen 4
        xbox = BoxLayout(orientation='vertical')
        xbox1 = BoxLayout(orientation='horizontal')
        wid4_go_back = Button(background_normal=img_go_back, background_down=img_go_back, on_press=self.go_to_NumSys)
        wid4_infotext = Label(text=infotext, font_size=17, size_hint=(1.75, 1), color=YELLOW)
        wid4_infotext2 = Label(text=infotext2, font_size=17, color=YELLOW)

        # Add Screen 1 To Screen Manager
        box1.add_widget(self.wid_input)
        box1.add_widget(wid_numsys)
        box1.add_widget(wid_info)

        box.add_widget(box1)
        box.add_widget(self.wid_from)
        box.add_widget(self.wid_to)
        box.add_widget(self.wid_text)

        # Add Screen 2 To Screen Manager
        ibox1.add_widget(wid2_go_back)
        ibox1.add_widget(wid2_infotext)

        ibox.add_widget(ibox1)
        ibox.add_widget(wid2_infotext2)

        # Add Screen 3 To Screen Manager
        jbox1.add_widget(self.wid3_input)
        jbox1.add_widget(wid3_back)
        jbox1.add_widget(wid3_info)

        jbox.add_widget(jbox1)
        jbox.add_widget(self.wid3_from)
        jbox.add_widget(self.wid3_to)
        jbox.add_widget(self.wid3_label)

        # Add Screen 4 To Screen Manager
        xbox1.add_widget(wid4_go_back)
        xbox1.add_widget(wid4_infotext)

        xbox.add_widget(xbox1)
        xbox.add_widget(wid4_infotext2)

        # Add Screens To ScreenManager
        sc1.add_widget(box)
        sc2.add_widget(ibox)
        sc3.add_widget(jbox)
        sc4.add_widget(xbox)

        self.sm.add_widget(sc1)
        self.sm.add_widget(sc2)
        self.sm.add_widget(sc3)
        self.sm.add_widget(sc4)

        return self.sm

    # Switch Screens
    def go_to_info(self, *event):
        self.sm.current = 'info'

    def go_to_info2(self, *event):
        self.sm.current = 'info2'

    def go_to_project(self, *event):
        self.sm.current = 'project'

    def go_to_NumSys(self, *event):
        self.sm.current = 'numsys'

    # Transforming Memory Unit System
    def transforming(self, *event):
        spin_from = self.wid_from
        spin_to = self.wid_to
        label = self.wid_text
        __input__ = self.wid_input
        try:
            number = float(__input__.text)
            if spin_from.text == 'Choose' or spin_to.text == 'Choose':
                label.text = '...'
            else:
                label.text = str(transform(number, spin_from.text, spin_to.text))
        except:
            label.text = '...'

    # Transforming Number Systems
    def appTransform(self, *event):
        spin_from = self.wid3_from
        spin_to = self.wid3_to
        label = self.wid3_label
        __input__ = self.wid3_input
        try:
            number = __input__.text
            if spin_from.text == 'Choose' or spin_to.text == 'Choose':
                label.text = '...'
            else:
                label.text = str(transformBinOctDecHex(number, spin_from.text, spin_to.text))
        except:
            label.text = '...'

# Run
if __name__ == '__main__':
    app = Program()
    app.run()
