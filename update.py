import mysql.connector
from main import *

mydb = mysql.connector.connect(
    host="localhost",
    user="laravel_user",
    passwd="Kraakmanisin",
    database="laravel"
)

mycursor = mydb.cursor()
ldrValue = rcv #from main.py
print(ldrValue)
sql = ("INSERT INTO ldr (value) VALUES (%s)")
mycursor.execute(sql, ldrValue)
mydb.commit()