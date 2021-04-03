from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from config import connect_to_database
from kivy.clock import Clock

cursor,mydb=connect_to_database()



Builder.load_file("admin_panel.kv")

class Admin_Panel(Screen):

    def __init__(self,**kwargs):
        super(Admin_Panel,self).__init__(**kwargs)
        self.update_labels()
        Clock.schedule_interval(self.update_labels,5)
    
    def update_labels(self,*args):
        mydb.commit()
        
        sql="Select SUM(Total),SUM(Available) from slots"
        cursor.execute(sql)
        t_slots=cursor.fetchall()
        e_slots=t_slots[0][1]
        t_slots=t_slots[0][0]
        
        
        sql="Select Count(SNO) from users"
        cursor.execute(sql)
        t_users=cursor.fetchall()[0][0]

        t_parkings=t_slots-e_slots


        

        self.ids.total_slots.text=str(t_slots)
        self.ids.total_users.text=str(t_users)
        self.ids.total_parkings.text=str(t_parkings)
        self.ids.empty_slots.text=str(e_slots)

        

        


class MainApp(MDApp):
    def build(self):
        return Admin_Panel()

#MainApp().run()