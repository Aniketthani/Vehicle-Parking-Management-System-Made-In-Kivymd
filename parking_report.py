from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
from datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDRaisedButton
from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

Builder.load_file("parking_report.kv")

cursor,mydb=connect_to_database()

class Parking_Report(Screen):
    def __init__(self,**kwargs):
        super(Parking_Report,self).__init__(**kwargs)
        self.name="report"
        self.staff_dropdown=DropDown()
        self.v_type_dropdown=DropDown()
        
        self.fill_dropdown()
        
    
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
    
    def fill_dropdown(self,*args):
        self.ids.report_mess.text=""
        mydb.commit()

        self.staff_dropdown.clear_widgets()
        self.v_type_dropdown.clear_widgets()


        sql="Select Username from users Where Type='Staff'"
        cursor.execute(sql)
        usernames=cursor.fetchall()

        sql="Select V_Type from vehicles"
        cursor.execute(sql)
        v_types=cursor.fetchall()

        btn=MDRaisedButton(text="ALL",size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
        btn.bind(on_release=partial(self.select_dropdown,"ALL",self.staff_dropdown))
        self.staff_dropdown.add_widget(btn)

        for i in usernames:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i[0],self.staff_dropdown))

            self.staff_dropdown.add_widget(btn)
        

        self.ids.staff_btn.bind(on_release=self.staff_dropdown.open)

        self.staff_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.staff_btn, 'text', x))


        btn=MDRaisedButton(text="ALL",size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
        btn.bind(on_release=partial(self.select_dropdown,"ALL",self.v_type_dropdown))
        self.v_type_dropdown.add_widget(btn)


        for i in v_types:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i[0],self.v_type_dropdown))

            self.v_type_dropdown.add_widget(btn)
        
        self.ids.v_type_btn.bind(on_release=self.v_type_dropdown.open)

        self.v_type_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.v_type_btn, 'text', x))

    def select_dropdown(self,item,dropdown,*args):
        dropdown.select(item) 
    
    def generate_report(self,*args):
        self.ids.report_mess.text=""
        try:
            self.ids.report_container.remove_widget(self.main_table)
        except:
            pass
        try:
            self.ids.report_container.remove_widget(self.total_table)
        except:
            pass
        
        if self.ids.from_date.text!="From Date" and self.ids.to_date.text!="To Date" and self.ids.staff_btn.text!="Select Staff" and self.ids.v_type_btn.text!="Vehicle Type":
            
            sql=f"Select * from parking Where (Date Between '{self.ids.from_date.text}' and '{self.ids.to_date.text}')"
            sql2=f"Select Count(SNO),SUM(Fare) from parking Where (Date Between '{self.ids.from_date.text}' and '{self.ids.to_date.text}' )"
            sql3=f"Select Count(SNO),SUM(Fare) from parking Where (Date Between '{self.ids.from_date.text}' and '{self.ids.to_date.text}' )"
            if self.ids.v_type_btn.text!="ALL":
                sql=sql+f" and V_Type='{self.ids.v_type_btn.text}'"
                sql2=sql2+f" and V_Type='{self.ids.v_type_btn.text}'"
                sql3=sql3+f" and V_Type='{self.ids.v_type_btn.text}'"
            if self.ids.staff_btn.text!="ALL":
                mydb.commit()
                sqlid=f"Select Emp_Id from users Where Username='{self.ids.staff_btn.text}'"
                cursor.execute(sqlid) 
                Id=cursor.fetchall()[0][0]

                sql=sql+f" and Emp_Id='{Id}'"
                sql2=sql2+f" and Emp_Id='{Id}'"
                sql3=sql3+f" and Emp_Id='{Id}'"
            
            sql3=sql3+" and Check_Out!='0' "

            cursor.execute(sql2)
            restotal=cursor.fetchall()

            cursor.execute(sql3)
            rescheckout=cursor.fetchall()

            

            

            cursor.execute(sql)
            res=cursor.fetchall()

            if res!=[]:
            
                self.main_table=MDDataTable(column_data=[('SNO',dp(30)),('Emp Name',dp(30)),('ID',dp(30)),("Owner's Name",dp(30)),('Mobile',dp(30)),('V Type',dp(30)),('V Number',dp(30)),('Check In',dp(30)),('Check Out',dp(30)),('Date',dp(30)),('Fare',dp(30))],row_data=res,rows_num=len(res),size_hint=(0.9,0.35),pos_hint={'center_x':0.5})
                self.ids.report_container.add_widget(self.main_table)
            
                if restotal!=[] and rescheckout!=[]:

                    self.total_table=GridLayout(cols=4,size_hint=(0.7,0.12),pos_hint={'center_x':0.5})
                    self.total_table.add_widget(MDLabel(text="[b]Total Parkings[/b]",markup=True))
                    self.total_table.add_widget(MDLabel(text="[b]Total Fare[/b]",markup=True))
                    self.total_table.add_widget(MDLabel(text="[b]C.O Compltd Parkn's[/b]",markup=True))
                    self.total_table.add_widget(MDLabel(text="[b]Fare fr C.O Compltd Parkn's[/b]",markup=True))
        
                    self.total_table.add_widget(MDLabel(text=str(restotal[0][0])))
                    self.total_table.add_widget(MDLabel(text=str(restotal[0][1])))
                    self.total_table.add_widget(MDLabel(text=str(rescheckout[0][0])))
                    self.total_table.add_widget(MDLabel(text=str(rescheckout[0][1])))
        
                    self.ids.report_container.add_widget(self.total_table)
                    self.ids.report_container.add_widget(MDLabel(text="",size_hint=(1,0.02)))

        else:
            self.ids.report_mess.text="Please Select Values For All Fields"
            


            
        
            
            
            
        
        
class MainApp(MDApp):
    def build(self):
        return Parking_Report()

#MainApp().run()