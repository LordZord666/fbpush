import mysql.connector
import requests
import schedule
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="task"
)


def getData():
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM table_product WHERE Availability ='1' ")

  myresult = mycursor.fetchall()
  return myresult

schedule.every().day.at("16:41").do(getData)
while True:
  schedule.run_pending()
  time.sleep(1)
