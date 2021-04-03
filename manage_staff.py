from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from config import connect_to_database
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDRaisedButton
from functools import partial
from hashlib import sha256

cursor,mydb=connect_to_database()

class Staff_Tab(MDFloatLayout,MDTabsBase):
    pass

Builder.load_file('manage_staff.kv')

class Manage_Staff(Screen):
    def __init__(self,**kwargs):
        super(Manage_Staff,self).__init__(**kwargs)
        self.name="manage_staff"
        self.show_staff()
        self.type_dropdown=DropDown()
        self.gender_dropdown=DropDown()
        self.username_dropdown=DropDown()
        self.passwd_username_dropdown=DropDown()
    
    def show_staff(self,*args):
        mydb.commit()
        
        sql="Select SNO,Name,Type,Gender,Mobile,Address,Username,Emp_Id from users"
        cursor.execute(sql)
        res=cursor.fetchall()

        try:
            self.ids.view_vehicles.remove_widget(self.table)
        except:
            pass

        self.table=MDDataTable(column_data=[('SNO',dp(30)),('Name',dp(30)),('Type',dp(30)),('Gender',dp(30)),('Mobile',dp(30)),('Address',dp(30)),('Username',dp(30)),('ID',dp(30))],row_data=res,rows_num=len(res),size_hint=(0.7,0.6),elevation=20,pos_hint={'center_x':0.5,'center_y':0.6})
        self.ids.view_staff.add_widget(self.table)
    
    def add_staff(self,*args):

        self.ids.add_name.text=""
        self.ids.add_type_btn.text="Type"
        self.ids.add_gender_btn.text="Gender"
        self.ids.add_mobile.text=""
        self.ids.add_address.text=""
        self.ids.add_username.text=""
        self.ids.add_password.text=""
        self.ids.add_id.text=""
        self.ids.add_staff_mess.text=""           

        mydb.commit()
        sqlt="Select Distinct Type from users"
        cursor.execute(sqlt)
        ty=cursor.fetchall()

        for i in ty:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i[0],self.type_dropdown))

            self.type_dropdown.add_widget(btn)

        self.ids.add_type_btn.bind(on_release=self.type_dropdown.open)

        self.type_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.add_type_btn, 'text', x))

        gender=['Male','Female','Other']

        for i in gender:
            btn=MDRaisedButton(text=i,size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i,self.gender_dropdown))

            self.gender_dropdown.add_widget(btn)
        
        self.ids.add_gender_btn.bind(on_release=self.gender_dropdown.open)

        self.gender_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.add_gender_btn, 'text', x))

    def save_added_staff(self,*args):

        if self.ids.add_name.text and self.ids.add_type_btn.text!="Type" and self.ids.add_gender_btn.text!="Gender" and self.ids.add_mobile.text and self.ids.add_address.text and self.ids.add_username.text and self.ids.add_id.text and self.ids.add_password.text:
            mydb.commit()
            sql=f"Select Username from users Where Username='{self.ids.add_username.text}'"
            cursor.execute(sql)
            if cursor.fetchall()==[]:

                sql=f"Select Emp_Id from users Where Emp_Id='{self.ids.add_id.text}'"
                cursor.execute(sql)

                if cursor.fetchall()==[]:
                    passwd=sha256(self.ids.add_password.text.encode()).hexdigest()

                    sql=f"Insert Into users (Name,Type,Gender,Mobile,Address,Username,Password,Emp_Id) Values ('{self.ids.add_name.text}','{self.ids.add_type_btn.text}','{self.ids.add_gender_btn.text[0]}','{self.ids.add_mobile.text}','{self.ids.add_address.text}','{self.ids.add_username.text}','{passwd}','{self.ids.add_id.text}')"
                    cursor.execute(sql)
                    mydb.commit()

                    self.ids.add_staff_mess.text=f"Staff '{self.ids.add_name.text}' Added Successfully"
                    self.ids.add_staff_mess.text_color=(0,1,0,1)

                    self.ids.add_name.text=""
                    self.ids.add_type_btn.text="Type"
                    self.ids.add_gender_btn.text="Gender"
                    self.ids.add_mobile.text=""
                    self.ids.add_address.text=""
                    self.ids.add_username.text=""
                    self.ids.add_password.text=""
                    self.ids.add_id.text=""
                
                else:
                    self.ids.add_staff_mess.text=f"This ID Is Already Taken, Please Type A Unique One"
                    self.ids.add_staff_mess.text_color=(1,1,1,1)

            else:
                self.ids.add_staff_mess.text=f"This Username Is Already Taken, Please Type A Unique One"
                self.ids.add_staff_mess.text_color=(1,1,1,1)
        
        else:
            self.ids.add_staff_mess.text=f"Please Enter All Details"
            self.ids.add_staff_mess.text_color=(1,1,1,1)
    
    def delete_staff(self,**kwargs):
        self.ids.delete_staff_mess.text=""
        mydb.commit()
        sql="Select Username from users"
        cursor.execute(sql)
        usernames=cursor.fetchall()

        self.username_dropdown.clear_widgets()

        for i in usernames:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i[0],self.username_dropdown))

            self.username_dropdown.add_widget(btn)

        self.ids.delete_username_btn.bind(on_release=self.username_dropdown.open)

        self.username_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.delete_username_btn, 'text', x))

        self.ids.delete_username_btn.text=usernames[0][0]
    
    def delete_particular_staff(self,*args):
        sql=f"Delete from users Where Username='{self.ids.delete_username_btn.text}'"
        cursor.execute(sql)
        mydb.commit()

        self.delete_staff()
        self.ids.delete_staff_mess.text=f"User '{self.ids.delete_username_btn.text}' Deleted Successfully"
        self.ids.delete_staff_mess.text_color=(0,1,0,1)

                  
    def select_dropdown(self,item,dropdown,*args):
        dropdown.select(item) 
        self.ids.new_passwd.disabled=True
        self.ids.new_passwd.text=""
        self.ids.save_passwd_mess.text=""
        self.ids.new_passwd.hint_text="New Password"

    def change_passwd(self,*args):
        self.ids.save_passwd_mess.text=""
        self.ids.new_passwd.disabled=True
        self.ids.new_passwd.text=""
        self.ids.new_passwd.hint_text="New Password"

        mydb.commit()
        sql="Select Username from users"
        cursor.execute(sql)
        usernames=cursor.fetchall()  

        self.passwd_username_dropdown.clear_widgets()

        for i in usernames:
            btn=MDRaisedButton(text=i[0],size_hint=(1,None ),font_size=20,md_bg_color=(0.2,0.23,0.93,0.5))
            btn.bind(on_release=partial(self.select_dropdown,i[0],self.passwd_username_dropdown))

            self.passwd_username_dropdown.add_widget(btn)

        self.ids.edit_passwd_btn.bind(on_release=self.passwd_username_dropdown.open)

        self.passwd_username_dropdown.bind(on_select=lambda instance, x: setattr(self.ids.edit_passwd_btn, 'text', x))

        self.ids.edit_passwd_btn.text=usernames[0][0]

    def edit_passwd(self,*args):
        self.ids.new_passwd.disabled=False
        self.ids.new_passwd.text=""
        self.ids.new_passwd.hint_text="********"
        self.ids.new_passwd.focus=True

    def save_new_passwd(self,*args):
        if self.ids.new_passwd.text:
            sql=f"Update users set Password ='{sha256(self.ids.new_passwd.text.encode()).hexdigest()}' Where Username='{self.ids.edit_passwd_btn.text}' "
            cursor.execute(sql)
            mydb.commit()

            self.ids.save_passwd_mess.text="Password Changed Successfully"
            self.ids.save_passwd_mess.text_color=(0,1,0,1)

            self.ids.new_passwd.hint_text="New Password"
            

        else:
            self.ids.save_passwd_mess.text="Please Enter New Password"
            self.ids.save_passwd_mess.text_color=(1,0,0,1)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        
        if instance_tab.title=="[b][size=30]View Staff[/size][/b]":
            
            self.show_staff()
        elif instance_tab.title=="[b][size=30]Add Staff[/size][/b]":
            
            self.add_staff()
        elif instance_tab.title=="[b][size=30]Delete Staff[/size][/b]":
            
            self.delete_staff()
        elif instance_tab.title=="[b][size=30]Change Password[/size][/b]":
            
            self.change_passwd()

class MainApp(MDApp):
    def build(self):
        return Manage_Staff()

#MainApp().run()