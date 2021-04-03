from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDRaisedButton
from functools import partial

Builder.load_file("manage_vehicles.kv")

cursor,mydb=connect_to_database()

class Vehicle_Tab(MDFloatLayout,MDTabsBase):
    pass

class Manage_Vehicles(Screen):
    def __init__(self,**kwargs):
        super(Manage_Vehicles,self).__init__(**kwargs)
        self.name="manage_vehicles"
        self.show_vehicles()
        self.drop_down=DropDown()
        self.delete_dropdown=DropDown()
        
        

    def show_vehicles(self,*args):
        mydb.commit()
        
        sql="Select * from vehicles"
        cursor.execute(sql)
        res=cursor.fetchall()

        try:
            self.ids.view_vehicles.remove_widget(self.table)
        except:
            pass

        self.table=MDDataTable(column_data=[('SNO',dp(50)),('Vehicle Type',dp(50)),('Fare',dp(50))],row_data=res,rows_num=len(res),size_hint=(0.45,0.5),pos_hint={'center_x':0.5,'center_y':0.6})
        self.ids.view_vehicles.add_widget(self.table)

    def add_new_vehicle(self,*args):
        self.ids.add_vehicle_mess.text=""
        if self.ids.new_v_type.text and self.ids.new_v_fare.text and self.ids.new_v_slots.text:
                
            if not self.ids.new_v_fare.text.isnumeric() or not self.ids.new_v_slots.text.isnumeric():
                self.ids.add_vehicle_mess.text=f"Only Numeric Data Allowed For Fare and Total Slots "
                self.ids.add_vehicle_mess.text_color=(1,0,0,1)
                self.ids.new_v_type.focus=True

                self.ids.new_v_type.text=""
                self.ids.new_v_fare.text=""
                self.ids.new_v_slots.text=""
                return

            sql=f"Insert Into vehicles (V_Type,Fare) VALUES ('{self.ids.new_v_type.text}','{self.ids.new_v_fare.text}')" 
            cursor.execute(sql)
            mydb.commit()

            sql=f"Insert Into slots (Type,Total,Available) VALUES ('{self.ids.new_v_type.text}','{self.ids.new_v_slots.text}','{self.ids.new_v_slots.text}')"
            cursor.execute(sql)
            mydb.commit()

            self.ids.add_vehicle_mess.text=f"Vehicle {self.ids.new_v_type.text} Added Successfully"
            self.ids.add_vehicle_mess.text_color=(0,1,0,1)

            self.ids.new_v_type.focus=True

            self.ids.new_v_type.text=""
            self.ids.new_v_fare.text=""
            self.ids.new_v_slots.text=""
        else:
            self.ids.add_vehicle_mess.text=f"Please Fill All The Details"
            self.ids.add_vehicle_mess.text_color=(1,0,0,1)
            self.ids.new_v_type.focus=True
            self.ids.new_v_type.text=""
            self.ids.new_v_fare.text=""
            self.ids.new_v_slots.text=""
        
    def edit_vehicle(self,*args):
        
        self.ids.edited_fare.text=""
        self.ids.edited_fare.disabled=True
        self.ids.edit_vehicle_mess.text=""

        mydb.commit()
        sql="Select V_Type from vehicles"
        cursor.execute(sql)    
        res=cursor.fetchall()

        self.drop_down.clear_widgets()

        for i in res:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_drop_down,i[0],self.drop_down))

            self.drop_down.add_widget(btn)
        
        #bind edit_v_type_btn
        self.ids.edit_v_type_btn.text=res[0][0]
        self.ids.edit_v_type_btn.bind(on_release=self.drop_down.open)

        self.drop_down.bind(on_select=lambda instance, x: setattr(self.ids.edit_v_type_btn, 'text', x))

    def select_drop_down(self,item,dropdown,*args):
        dropdown.select(item)
        self.ids.edited_fare.text=""
        
        self.ids.edited_fare.disabled=True
        
        self.ids.edit_vehicle_mess.text=""

    def edit_vehicle_fare(self,*args):

        mydb.commit()
        sql=f"Select Fare from vehicles Where V_Type='{self.ids.edit_v_type_btn.text}'"
        cursor.execute(sql)
        res=cursor.fetchall()[0][0]

        self.ids.edited_fare.disabled=False
        self.ids.edited_fare.text=str(res)


    def save_edited_vehicle(self,*args):
        if self.ids.edited_fare.text.isnumeric():
            sql=f"Update vehicles set Fare='{self.ids.edited_fare.text}' Where V_Type='{self.ids.edit_v_type_btn.text}'"
            cursor.execute(sql)
            mydb.commit()

            self.ids.edited_fare.disabled=True
            self.ids.edited_fare.text=""

            self.ids.edit_vehicle_mess.text="Vehicle Edited Successfully"
            self.ids.edit_vehicle_mess.text_color=(0,1,0,1)
        else:
            self.ids.edit_vehicle_mess.text="Please Enter Valid Details"
            self.ids.edit_vehicle_mess.text_color=(1,0,0,1)


    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        
        if instance_tab.title=="[b][size=30]View Vehicles[/size][/b]":
            
            self.show_vehicles()
        if instance_tab.title=="[b][size=30]Add Vehicle[/size][/b]":
            
            self.ids.add_vehicle_mess.text=""
            self.ids.new_v_type.text=""
            self.ids.new_v_fare.text=""
            self.ids.new_v_slots.text=""
        
        if instance_tab.title=="[b][size=30]Edit Vehicle[/size][/b]":
            
            self.edit_vehicle()
        
        if instance_tab.title=="[b][size=30]Delete Vehicle[/size][/b]":
            
            self.delete_vehicle()

    def delete_vehicle(self,*args):
        
        self.ids.delete_vehicle_mess.text=""
        

        mydb.commit()
        sql="Select V_Type from vehicles"
        cursor.execute(sql)    
        res=cursor.fetchall()

        self.delete_dropdown.clear_widgets()

        for i in res:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_delete_dropdown,i[0],self.delete_dropdown))

            self.delete_dropdown.add_widget(btn)
        
        #bind edit_v_type_btn
        self.ids.delete_v_type_btn.text=res[0][0]
        self.ids.delete_v_type_btn.bind(on_release=self.delete_dropdown.open)

        self.delete_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.delete_v_type_btn, 'text', x))
    
    def select_delete_dropdown(self,item,dropdown,*args):
        dropdown.select(item)
        self.ids.delete_vehicle_mess.text=""
        

    def delete_particular_vehicle(self,*args):
        sql=f"Delete from vehicles Where V_Type='{self.ids.delete_v_type_btn.text}'"
        cursor.execute(sql)
        mydb.commit()

        sql=f"Delete from slots Where Type='{self.ids.delete_v_type_btn.text}'"
        cursor.execute(sql)
        mydb.commit()

        

        self.delete_vehicle()
        self.ids.delete_vehicle_mess.text=f"[b]Vehicle Deleted Successfully[/b]"
        self.ids.delete_vehicle_mess.color=(0,1,0,1)
class MainApp(MDApp):
    def build(self):
        return Manage_Vehicles()

#MainApp().run()