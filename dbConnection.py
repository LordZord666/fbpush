from multiprocessing import connection
from sqlite3 import Cursor
import mysql.connector
import cv2

def convertToBinary (filename):
  with open(filename,'rb') as file:
    binarydata= file.read()
  return binarydata

def convertBinaryToFile(binarydata, filename):
  with open(filename,'wb') as file:
    file.write(binarydata)

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
  
  insertQuery = """ INSERT into table_product (id, title, description, price, image, Availabitity) value(%s,%s,%s,%s,%s,%s)"""
  img=cv2.imread('pic.jpg')
  gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  print(gray_img)
  value = ('3,ball,basketball,500,convertPic,1')
  Cursor.execute(insertQuery,value)
  connection.commit
  
  return myresult


