from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
import datetime
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import BoxLayout
from manage_slots import Manage_Slots



Builder.load_file('admin.kv')

class AdminDashboard(Screen):
    def __init__(self,**kwargs):
        super(AdminDashboard,self).__init__(**kwargs)
        self.name="admin dashboard"
    
    def logout(self,*args):
        self.parent.current="loginscreen"
        self.parent.remove_widget(self)

class AdminContentNavigationDrawer(BoxLayout):
    screen_manager=ObjectProperty()

    nav_drawer=ObjectProperty()

    def manage_slots(self,*args):
        self.manage_slots_screen=Manage_Slots(name='manage_slots')
        self.screen_manager.add_widget(self.manage_slots_screen)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Purple"
        return AdminDashboard()

#MainApp().run()