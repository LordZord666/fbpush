import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="task"
)


def getData():
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM tables WHERE Availability IS 1")

  myresult = mycursor.fetchall()
  return myresult
