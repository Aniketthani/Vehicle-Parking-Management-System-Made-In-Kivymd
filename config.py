import mysql.connector

def connect_to_database():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="aniket",
    database="pms"
)
    cursor=mydb.cursor()

    return cursor,mydb 

