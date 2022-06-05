import mysql.connector
import time
import requests

#connection = pyodbc.connect(driver='{ODBC driver 17 for SQL Server}', host="")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

def getData():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM Tab")
  myresult = mycursor.fetchall()
  return myresult
