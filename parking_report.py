from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
from datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.picker import MDDatePicker

Builder.load_file("parking_report.kv")

cursor,mydb=connect_to_database()

class Parking_Report(Screen):
    def __init__(self,**kwargs):
        super(Parking_Report,self).__init__(**kwargs)
        self.name="report"
    
    def from_date(self,*args):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.save_from_date)
        date_dialog.open()
    
    def to_date(self,*args):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.save_to_date)
        date_dialog.open()

    def save_from_date(self, instance, value, date_range):
        self.ids.from_date.text=str(value)
    def save_to_date(self, instance, value, date_range):
        self.ids.to_date.text=str(value)

class MainApp(MDApp):
    def build(self):
        return Parking_Report()

MainApp().run()