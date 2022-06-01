import facebook
import time
from dbConnection import getData
page_access_token = "EAAF219B1ahEBAEYJB0h82ZAcEbrJAkXrLrZCSNu6KYUgP4I7H6NZAe6YZAvoa4EtJm6zKfUqzPSz05ZCnZBwKd9rP0MnDQwNF37fhjOsw95r2BoIw3agQZA3MotAueTEYmMLhNlFXb74lYSryqWrgoAzPoZAqi0N218LKVpbpwl71A34gG5OcCgAsAGibImGo0ZACLRiJDAoMagZDZD"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "113544291367455"
graph.put_object(facebook_page_id, "feed", message='test message')
data= getData()
print(data)