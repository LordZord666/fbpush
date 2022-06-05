from cgitb import text
import facebook
import config
import requests
from dbConnection import getData
import schedule
import time

page_access_token = "EAAF219B1ahEBAEPKtkgJVpnOBNVajj63uoi7kazXZBNBVHfuYVrd6J2CPpj3PGaWgq1SVe5ZCqDZB5EqW4sJGDMfFY4tberZAMy2rkSRppTgcMSMOseUF9zZBWeES7tXHT8d1SPwVO8K2JpZAzXDETnXXUTywPjfjUw0wsKz6xKGlkYqKqewri"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "113544291367455"
#graph.put_object(facebook_page_id, "feed", message='test message')


datas = schedule.every(3600).seconds.do(getData)
  
for data in datas:
    graph.put_object(facebook_page_id, "feed", message=data)
  #yha message ko satta data anusar tanera hal

while True:
  schedule.run_pending()
  time.sleep(1)
