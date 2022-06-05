import facebook
import config
import requests
from dbConnection import getData
import schedule
import time

page_access_token = "EAAF219B1ahEBAEPKtkgJVpnOBNVajj63uoi7kazXZBNBVHfuYVrd6J2CPpj3PGaWgq1SVe5ZCqDZB5EqW4sJGDMfFY4tberZAMy2rkSRppTgcMSMOseUF9zZBWeES7tXHT8d1SPwVO8K2JpZAzXDETnXXUTywPjfjUw0wsKz6xKGlkYqKqewri"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "113544291367455"

def getDataandPush():
  datas = getData()
  for data in datas:
    graph.put_object(facebook_page_id, "feed", message=data)

schedule.every(120).seconds.do(getDataandPush)
while True:
  schedule.run_pending()
  time.sleep(1)
  
#image_url = 'https://graph.facebook.com/{page-id}/photos'.format(facebook_page_id)
#image_location = '/Users/User/Desktop/pic.jpg'
#image_playload = {
# 'url': image_location,
# 'access_token': config.page_access_token
#}
#r = requests.post(image_url, data=image_playload)
#print(r.text)
