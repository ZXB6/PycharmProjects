##导入App，然后让TestApp这个类继承
from kivy.app import App
##导入一个Button,运维有这个button，当你点击的时候才会有所反应
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello,kivy')
TestApp().run()