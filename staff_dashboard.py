from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty,StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from config import connect_to_database
from functools import partial
import datetime
from kivy.clock import Clock
from kivy.core.window import Window
from datatables import MDDataTable
from kivy.metrics import dp









cursor,mydb=connect_to_database()


Builder.load_file("staff_dashboard.kv")

global timenow,datenow



class CustomDropDown(DropDown):
    def __init__(self,**kwargs):
        super(CustomDropDown,self).__init__(**kwargs)
        


class Staff_Dashboard(Screen):
    def __init__(self,**kwargs):
        super(Staff_Dashboard,self).__init__(**kwargs)
        self.name="staff_dashboard"
        Window.bind(on_key_down=self._on_keyboard_down)

        #variables related to login details
        
        self.emp_id=StringProperty('')
        self.NameOfEmp=StringProperty('')

        self.dropdown_value=None
        self.dropdown=CustomDropDown()
        
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.dropbtn,'text',x))

        sql="Select V_Type from vehicles"
        cursor.execute(sql)
        res=cursor.fetchall()
        
        self.dropdown.select(res[0][0])
        self.dropdown_value=res[0][0]
        
        for i in res:
            self.dropdown.add_widget(MDRaisedButton(text=i[0],font_size=20,size_hint=(1,None),on_release= partial(self.select_dropdown,i[0]),theme_text_color="Custom",text_color=(1,0,0,1)))
        
        
        Clock.schedule_interval(self.live_clock,1)

        #edit btn
        self.edit_btn=Button(text="Edit",size_hint=(0.4,0.1 ),pos_hint={'center_x':0.5 },font_size=(0.4*self.ids.receipt_card.height/10 + 0.2*4*self.ids.receipt_card.width/10),on_release=self.edit_parking)
        self.edit_btn.font_size=3*self.edit_btn.height/10
        #current vehicle_number
        self.current_v_no=None
        #current SNO
        self.current_sno=None
        #want to edit
        self.want_to_edit=False
        #current v_type
        self.current_v_type=None

    def select_dropdown(self,item,*args):
        self.dropdown.select(item)
        self.dropdown_value=item
    def live_clock(self,*args):
        global timenow,datenow
        timenow=datetime.datetime.now().strftime("%I:%M:%S%p").lower()
        datenow=datetime.datetime.now().strftime("%Y-%m-%d")
        self.ids.live_clock.text=f"[size=25][color=#e6bf00]{datenow}    {timenow}[/color][/size]"
    
    def generate_receipt(self,*args):
        

        self.edit_btn.text="Edit"       
        receipt_text=""
        global timenow,datenow

        if self.want_to_edit:
            
            sqlslot=f"Select Available from slots Where Type='{self.current_v_type}'"
            cursor.execute(sqlslot)
            res=cursor.fetchall()
            res=res[0][0] + 1

            sqlslot=f"Update slots set Available='{res}' Where Type='{self.current_v_type}' "
            cursor.execute(sqlslot)
            mydb.commit()

            sqlslot2=f"Select Available from slots Where Type='{self.dropdown_value}'"
            cursor.execute(sqlslot2)
            res=cursor.fetchall()

            if res[0][0]<=0:
                sql=f"Delete From parking Where SNO='{self.current_sno}'"
                cursor.execute(sql)
                mydb.commit()
                self.ids.receipt_text.text=f"No Slot Of {self.dropdown_value} Is Available, Therefore Cancelling The Transaction "
                
                if self.edit_btn in self.ids.receipt_card.children:
                    self.ids.receipt_card.remove_widget(self.edit_btn)
                
                #clear the text fields
                self.ids.owner_name.text=""
                self.ids.mobile.text=""
                self.ids.v_no.text=""
        
                sql="Select V_Type from vehicles Where SNO='1'"
                cursor.execute(sql)
                res=cursor.fetchall()
                self.dropdown_value=res[0][0]
                self.dropdown.select(res[0][0])

                self.ids.owner_name.focus=True

                self.want_to_edit=False

                
                return
            else:
                res=res[0][0] - 1
                sqlslot=f"Update slots set Available='{res}' Where Type='{self.dropdown_value}'"
                cursor.execute(sqlslot)
                mydb.commit()




            sqlfare=f"Select Fare from vehicles Where V_Type='{self.dropdown_value}'"
            cursor.execute(sqlfare)
            fare=cursor.fetchall()
            fare=fare[0][0]

            sql=f"Update parking set Owner_Name='{self.ids.owner_name.text}',Mobile='{self.ids.mobile.text}',V_Type='{self.dropdown_value}',V_Number='{self.ids.v_no.text}',Check_In='{timenow}',Date='{datenow}',Fare='{fare}' where SNO='{self.current_sno}'"
            cursor.execute(sql)
            mydb.commit()

            #receipt_text
            receipt_text=f"""
                      Parking Receipt
            Date : {datenow} {timenow}
            Vehicle Owner : {self.ids.owner_name.text}
            Vehicle Type : {self.dropdown_value}
            Vehicle Number : {self.ids.v_no.text}
            Check In : {timenow}
            Fare : {fare} Rs
            ---------------Thank You----------------
            """

            self.ids.receipt_text.text=receipt_text
            if self.edit_btn in self.ids.receipt_card.children:
                    self.ids.receipt_card.remove_widget(self.edit_btn)

            self.current_v_type=self.dropdown_value
            

            #clear the text fields
            self.ids.owner_name.text=""
            self.ids.mobile.text=""
            self.ids.v_no.text=""
        
            sql="Select V_Type from vehicles Where SNO='1'"
            cursor.execute(sql)
            res=cursor.fetchall()
            self.dropdown_value=res[0][0]
            self.dropdown.select(res[0][0])

            self.ids.owner_name.focus=True

            self.want_to_edit=False

        elif self.ids.owner_name.text and self.ids.mobile.text  and self.ids.v_no.text:

            sqlslot=f"select Available from slots where Type='{self.dropdown_value}'"
            cursor.execute(sqlslot)
            res=cursor.fetchall()
            res=res[0][0]-1

            if res<0:
                self.ids.receipt_text.text=f"No Slot Of {self.dropdown_value} Is Available "
                self.ids.receipt_card.remove_widget(self.edit_btn)

                #clear the text fields
                self.ids.owner_name.text=""
                self.ids.mobile.text=""
                self.ids.v_no.text=""

                sql="Select V_Type from vehicles Where SNO='1'"
                cursor.execute(sql)
                res=cursor.fetchall()
                self.dropdown_value=res[0][0]
                self.dropdown.select(res[0][0])

                self.ids.owner_name.focus=True
                return

            sqlslot2=f"Update slots set Available='{res}' Where Type='{self.dropdown_value}'"

            cursor.execute(sqlslot2)
            mydb.commit()


            sqlfare=f"Select Fare from vehicles Where V_Type='{self.dropdown_value}'"
            cursor.execute(sqlfare)
            fare=cursor.fetchall()
            fare=fare[0][0]
            sql=f"Insert Into parking (Emp_Name,Emp_Id,Owner_Name,Mobile,V_Type,V_Number,Check_In,Check_Out,Date,Fare) VALUES ('{self.NameOfEmp}','{self.emp_id}','{self.ids.owner_name.text}','{self.ids.mobile.text}','{self.dropdown_value}','{self.ids.v_no.text}','{timenow}','0','{datenow}','{fare}')"
            cursor.execute(sql)
            mydb.commit()

            
            #receipt_text
            receipt_text=f"""
                      Parking Receipt
            Date : {datenow} {timenow}
            Vehicle Owner : {self.ids.owner_name.text}
            Vehicle Type : {self.dropdown_value}
            Vehicle Number : {self.ids.v_no.text}
            Check In : {timenow}
            Fare : {fare} Rs
            ---------------Thank You----------------
            """

            self.ids.receipt_text.text=receipt_text

            #adding edit btn in receipt card
            if self.edit_btn not in self.ids.receipt_card.children:
                self.ids.receipt_card.add_widget(self.edit_btn)
            
            #updating the current vehicle number
            self.current_v_no=self.ids.v_no.text
            self.current_v_type=self.dropdown_value

            

        else:
            if self.edit_btn in self.ids.receipt_card.children:
                self.ids.receipt_card.remove_widget(self.edit_btn)    

            
        
        #clear the text fields
        self.ids.owner_name.text=""
        self.ids.mobile.text=""
        self.ids.v_no.text=""
        
        sql="Select V_Type from vehicles Where SNO='1'"
        cursor.execute(sql)
        res=cursor.fetchall()
        self.dropdown_value=res[0][0]
        self.dropdown.select(res[0][0])

        self.ids.owner_name.focus=True

        if not receipt_text:
            self.ids.receipt_text.text="  Enter All Details To Generate The Receipt"

    

        

    def edit_parking(self,*args):
        if self.edit_btn.text=="Cancel Edit":
            self.edit_btn.text="Edit"
            self.ids.receipt_card.remove_widget(self.edit_btn)
            self.want_to_edit=False
            self.ids.owner_name.text=""
            self.ids.mobile.text=""
            self.ids.v_no.text=""

            sql="Select V_Type from vehicles Where SNO='1'"
            cursor.execute(sql)
            res=cursor.fetchall()
            self.dropdown_value=res[0][0]
            self.dropdown.select(res[0][0])

            self.ids.owner_name.focus=True
            return
        
        self.edit_btn.text="Cancel Edit"
        sql=f"select * from parking Where V_Number='{self.current_v_no}' Order By SNO Desc Limit 1"
        cursor.execute(sql)
        res=cursor.fetchall()

        if res:
            self.ids.owner_name.text=res[0][3]
            self.ids.mobile.text=res[0][4]
            self.ids.v_no.text=res[0][6]
            self.dropdown_value=res[0][5]
            self.dropdown.select(res[0][5])

            

            #updating the current SNO
            self.current_sno=res[0][0]
            self.want_to_edit=True

    


            
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        try:
            if keycode==40:
                if self.parent.current=="staff_dashboard":
                    self.generate_receipt()
        except:
            pass
    
    def generate_check_out_receipt(self,*args):
        self.ids.check_out_mess.text=""
        self.ids.check_out_receipt_box.text="                     Receipt Box"
        global timenow
        c_v_no=self.ids.check_out_v_no.text
        if c_v_no:
            sql=f"Select * from parking Where V_Number='{c_v_no}' and Check_Out='0' Order By SNO Desc Limit 1"
            cursor.execute(sql)
            res=cursor.fetchall()
            if res!=[]:
                vehicle_type=res[0][5]
                sql=f"Select Available from slots Where Type='{vehicle_type}'"
                cursor.execute(sql)
                available=cursor.fetchall()[0][0] + 1
                sql=f"Update slots set Available='{available}' Where Type='{vehicle_type}'"
                cursor.execute(sql)
                mydb.commit()

                sno=res[0][0]
                sql2=f"Update parking set Check_Out='{timenow}' Where SNO='{sno}'"
                cursor.execute(sql2)
                mydb.commit()
                self.ids.check_out_v_no.text=""
                
                self.ids.check_out_mess.text="Check Out Filled Successfully"
                self.ids.check_out_mess.text_color=(0,1,0,1)

                receipt_text=f"""
                            Parking Receipt
                    Date : {datenow} {timenow}
                    Vehicle Owner : {res[0][3]}
                    Vehicle Type : {res[0][5]}
                    Vehicle Number : {res[0][6]}
                    Check In : {res[0][7]}
                    Check Out : {timenow}
                    Fare : {res[0][10]} Rs
                    ---------------Thank You----------------
                    """
                self.ids.check_out_receipt_box.text=receipt_text
            else:
                self.ids.check_out_v_no.text=""
                
                self.ids.check_out_mess.text="This Vehicle is not parked"
                self.ids.check_out_mess.text_color=(1,0,0,1)
        else:
            self.ids.check_out_mess.text="Please Enter Vehicle Number"
            self.ids.check_out_mess.text_color=(1,0,0,1)
                
    def recent_entries(self,*args):
        sql="Select * from parking Order By SNO Desc Limit 20"
        cursor.execute(sql)
        res=cursor.fetchall()
        self.ids.recent_entries_screen.table=MDDataTable(column_data=[('SNO',dp(30)),('Emp Name',dp(30)),('Emp Id',dp(30)),('Owner Name',dp(30)),('Mobile',dp(30)),('V_Type',dp(30)),('V_Number',dp(30)),('Check In',dp(30)),('Check Out',dp(30)),('Date',dp(30)),('Fare',dp(30))],row_data=res,rows_num=20,size_hint=(0.9,0.8),pos_hint={'center_x':0.5,'center_y':0.5})
        self.ids.recent_entries_screen.add_widget(self.ids.recent_entries_screen.table)

    def logout(self,*args):
        self.parent.current="loginscreen"
        self.ids.owner_name.text=""
        self.ids.mobile.text=""
        self.ids.v_no.text=""
        self.ids.receipt_text.text="                     Receipt Box"
        self.ids.check_out_v_no.text=""
        self.ids.check_out_mess.text=""
        self.ids.check_out_receipt_box.text="                     Receipt Box"
        self.parent.remove_widget(self)


class ContentNavigationDrawer(BoxLayout):
    screen_manager=ObjectProperty()
    nav_drawer=ObjectProperty()
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Purple"
        
        return Staff_Dashboard()

#MainApp().run()