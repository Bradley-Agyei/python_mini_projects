import requests

# API provided by openweathermap.org
API_KEY = "35646e041516daa06bc17d7cb2882bf7"

#URL for where request is being sent to 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Parameter used in request to obtain correct data
city = input("Enter a city name: ")

#passing api key to base_url and city as a query parameter
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#Sending GET request to retrieve data 
response = requests.get(request_url)

#Check status code of request 
if response.status_code == 200:
    data = response.json()
    #Obtain weather data description
    weather = data["weather"][0]["description"]
    #Obtain temp and convert to Fahrenheit rounded to 2 dec places
    temperature = round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)
    print(f"Weather in {city} is {weather}. The current temperature is {temperature} F.")
else:
    print("Error occurred.")