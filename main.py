import mysql.connector
import time
import matplotlib
matplotlib.use("Pdf")
from matplotlib import pyplot as plt
import serial

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)
prevDigits = '404'

mydb = mysql.connector.connect(
    host="localhost",
    user="laravel_user",
    passwd="Kraakmanisin",
    database="laravel"
)

mycursor = mydb.cursor()

deleteLDR = """truncate table ldr """
mycursor.execute(deleteLDR)
mydb.commit()
while True:
    mycursor.execute("SELECT * FROM display;")
    for x in mycursor:
        digits = x[1]
        if digits != prevDigits:
            print(digits)
            port.write(digits.encode())
            prevDigits = digits

    if port.readline() != "":
        ldrValue = port.readline()
        print(ldrValue)
        sql = """INSERT INTO ldr (value) VALUES (%s)"""
        mycursor.execute(sql, (ldrValue,))

    # omzetten naar graph
    mycursor.execute("SELECT * FROM ldr;")
    ids = []
    values = []
    for x in mycursor:
        ids.append(x[0])
        values.append(x[1])
    plt.plot(ids, values)
    plt.xlabel('time (s)')
    plt.ylabel('LDR value')
    plt.title('LDR')
    plt.savefig('public/img/ldrgraph.png', bbox_inches='tight')
    time.sleep(1)
    mydb.commit()
mydb.close()