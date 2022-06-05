port mysql.connector
import schedule
import time
import requests

#connection = pyodbc.connect(driver='{ODBC driver 17 for SQL Server}', host="")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="task"
)

def getData():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM table_product")
  myresult = mycursor.fetchall()
  print (myresult)
  schedule.every(4).seconds.do(getData)
  while True:
    schedule.run_pending()
    time.sleep(1)
  return myresult
