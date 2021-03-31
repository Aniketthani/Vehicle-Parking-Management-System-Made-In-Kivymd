from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
import datetime
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import BoxLayout


Builder.load_file('admin.kv')

class AdminDashboard(Screen):
    def __init__(self,**kwargs):
        super(AdminDashboard,self).__init__(**kwargs)

class ContentNavigationDrawer(BoxLayout):
    screen_manager=ObjectProperty()
    nav_drawer=ObjectProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Purple"
        return AdminDashboard()

MainApp().run()