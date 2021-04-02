from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from config import connect_to_database
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.uix.button import Button
from functools import partial

Builder.load_file('manage_slots.kv')

cursor,mydb=connect_to_database()

class Slot_Tab(MDFloatLayout,MDTabsBase):
    pass

class Manage_Slots(Screen):
    def __init__(self,**kwargs):
        super(Manage_Slots,self).__init__(**kwargs)
        
        self.show_slots()
        self.dropdown=DropDown() 
        

    def show_slots(self,*args):
        
        sql="Select * from slots"
        cursor.execute(sql)
        res=cursor.fetchall()
        
        
        try:
            
            self.ids.view_slots.remove_widget(self.table)
            
            
            
        except:
            pass

        self.table=MDDataTable(column_data=[('SNO',dp(50)),('Type',dp(50)),('Total',dp(50)),('Available',dp(50))],row_data=res,rows_num=len(res),size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5})
        self.ids.view_slots.add_widget(self.table)
            

        
        

    def edit_slots(self,*args):
        self.ids.edit_slot_mess.text=""
        self.ids.slot_total.disabled=True
        self.ids.slot_available.disabled=True
        self.ids.slot_total.text=""
        self.ids.slot_available.text=""
        
        sql="select Type,Total,Available from slots"
        cursor.execute(sql)
        res=cursor.fetchall()

        #create a dropdown with  buttons
        
        
        self.dropdown.clear_widgets()
        #dropdown.clear_widgets()
        for i in res:
            btn = MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))

            btn.bind(on_release=partial(self.select_dropdown,i[0],self.dropdown))

        # then add the button inside the dropdown
            self.dropdown.add_widget(btn)
        
        #bind mainbutton
        self.ids.mainbutton.text=res[0][0]
        self.ids.mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.mainbutton, 'text', x))

    def select_dropdown(self,item,dropdown,*args):
        dropdown.select(item)
        self.ids.slot_total.text=""
        self.ids.slot_available.text=""
        self.ids.slot_total.disabled=True
        self.ids.slot_available.disabled=True
        self.ids.edit_slot_mess.text=""

        
        
    def edit_particular_slot(self,slot,*args):
        self.ids.edit_slot_mess.text=""
        self.ids.slot_total.disabled=False
        self.ids.slot_available.disabled=False
        sql=f"Select Total,Available from slots Where Type='{slot}'"
        cursor.execute(sql)
        res=cursor.fetchall()

        self.ids.slot_total.text=str(res[0][0])
        self.ids.slot_available.text=str(res[0][1])

    def save_edit_slot(self,*args):
        
        if self.ids.slot_total.text and self.ids.slot_available.text:
            print()

            if not self.ids.slot_total.text.isnumeric() or not self.ids.slot_available.text.isnumeric():
                self.ids.edit_slot_mess.text="[!]Please Enter Numeric Values"
                self.ids.edit_slot_mess.text_color=(1,0,0,1)
                return
            
            if int(self.ids.slot_total.text) < int(self.ids.slot_available.text):
                self.ids.edit_slot_mess.text="[!]Available Slots should be less or equal to Total Slots"
                self.ids.edit_slot_mess.text_color=(1,0,0,1)
                return

            sql=f"Update slots set Total='{self.ids.slot_total.text}', Available='{self.ids.slot_available.text}' Where Type='{self.ids.mainbutton.text}'"
            cursor.execute(sql)
            mydb.commit()

            self.ids.slot_total.text=""
            self.ids.slot_available.text=""
            self.ids.slot_total.disabled=True
            self.ids.slot_available.disabled=True
            self.ids.edit_slot_mess.text_color=(0,1,0,1)
            self.ids.edit_slot_mess.text="Edited Successfully"





    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        
        if instance_tab.title=="[b][size=30]View Slots[/size][/b]":
            
            
            if self.table in self.ids.view_slots.children:
                self.ids.view_slots.remove_widget(self.table)
            self.show_slots()

        if instance_tab.title=="[b][size=30]Edit Slots[/size][/b]":
            
            self.edit_slots()
            
    
    

class MainApp(MDApp):
    def build(self):
        
        return Manage_Slots()

#MainApp().run()