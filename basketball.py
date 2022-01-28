import requests

#No API key needed 

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
    #Grab full name of player 
    full_name = data["first_name"] + " " + data["last_name"]
    #Grab team the player plays for
    team = data["team"]["name"]
    print(f"{full_name} plays for {team}.")
else:
    print("Error retrieving data.")




