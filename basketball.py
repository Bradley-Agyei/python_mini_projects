from urllib import response
import requests

#URL that request is being made to 
BASE_URL = "https://www.balldontlie.io/api/v1/players"

#request_url
request_url = f"{BASE_URL}"

#GET request to retrieve data
response1 = requests.get(request_url) 

#Check status code of request
if response1.status_code == 200:
    data = response1.json()
    print(data)
else:
    print("Error retrieving data.")




