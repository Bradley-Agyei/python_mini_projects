import requests

#URL that request is being made to 
BASE_URL = "https://www.balldontlie.io/api/v1/players"

#requesting player id 
player_id = input("Enter a player id: ")

#request_url to get specific player based on ID
request_url = f"{BASE_URL}/{player_id}"

#GET request to retrieve data
response = requests.get(request_url) 

#Check status code of request
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error retrieving data.")




