from kivymd.app import MDApp
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from config import connect_to_database
from hashlib import sha256
from kivy.core.window import Window

from staff_dashboard import staff_dashboard

#connect to database
try:
    cursor,mydb=connect_to_database()
except:
    print("[!] Server is Down or some other error is there")



Builder.load_file("login_screen.kv")

class loginscreen(Screen):
    def __init__(self,**kwargs):
        super(loginscreen,self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.name="loginscreen"
    def validate_login(self,*args):
        if self.ids.username.text and self.ids.password.text:
            user=self.ids.username.text.replace(" ","")
            passwd=self.ids.password.text.replace(" ","")
            passwd=sha256(passwd.encode()).hexdigest()
    


            sql=f"Select * from users Where Username='{user}' and Password='{passwd}'"

            cursor.execute(sql)
            result=cursor.fetchall()
            if result:
                self.ids.username.text=""
                self.ids.password.text=''
                self.ids.login_error.text=""
                self.ids.username.focus=True
                self.parent.staff_dashboard.emp_id=result[0][8]
                self.parent.staff_dashboard.NameOfEmp=result[0][1]
                self.parent.staff_dashboard.ids.username.text=f"[b][size=22]{result[0][1]}[/size][/b]\n[color=#6ff542][size=15]          ID:{result[0][8]}[/size][/color]"
                self.parent.current="staff_dashboard"
            else:
                self.ids.username.text=""
                self.ids.password.text=''
                self.ids.username.focus=True
                self.ids.login_error.text="[*]Invalid Username Or Password"
                

        else:
            self.ids.username.text=""
            self.ids.password.text=''
            self.ids.username.focus=True
            self.ids.login_error.text="[*]Please Enter All The Details"
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        try:
            if keycode == 40:  # 40 - Enter key pressed
                if self.parent.current=="loginscreen":
                    self.validate_login()
        except:
            pass


class PMSApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Purple"
        self.sm=ScreenManager()
        self.sm.add_widget(loginscreen())
        self.sm.staff_dashboard=staff_dashboard()
        self.sm.add_widget(self.sm.staff_dashboard)
        
       

        self.sm.current="loginscreen"
        
        
        return self.sm

PMSApp().run()