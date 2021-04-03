from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
import datetime
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import BoxLayout
from manage_slots import Manage_Slots
from admin_panel import Admin_Panel
from kivy.clock import Clock
from manage_vehicles import Manage_Vehicles
from manage_staff import Manage_Staff


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

    def __init__(self,**kwargs):
        super(AdminContentNavigationDrawer,self).__init__(**kwargs)
        Clock.schedule_once(self.provide_admin_privileges,0)
        

    def provide_admin_privileges(self,*args):
        try:
            if "admin_panel" not  in self.screen_manager._get_screen_names():
                self.screen_manager.add_widget(Admin_Panel(name='admin_panel'))
                self.screen_manager.current="admin_panel"
                
                
        except:
            pass

    def manage_vehicles(self,*args):
        try:
            self.screen_manager.remove_widget(self.manage_vehicles_screen)
        except:
            pass
        self.manage_vehicles_screen=Manage_Vehicles()
        self.screen_manager.add_widget(self.manage_vehicles_screen)
    
    def manage_staff(self,*args):
        try:
            self.screen_manager.remove_widget(self.manage_staff_screen)
        except:
            pass
        self.manage_staff_screen=Manage_Staff()
        self.screen_manager.add_widget(self.manage_staff_screen)

    def manage_slots(self,*args):
        try:
            self.screen_manager.remove_widget(self.manage_slots_screen)
            
        except:
            pass
        
        self.manage_slots_screen=Manage_Slots(name='manage_slots')
        self.screen_manager.add_widget(self.manage_slots_screen)

        

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Purple"
        return AdminDashboard()

#MainApp().run()