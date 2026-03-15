import requests
#ask for city
city = input("Enter a City: ").strip()

#convert city to coords with api
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name" : city, "count" : 1}
geo_response = requests.get(geo_url, params=params)
geo_data = geo_response.json()
city_lat = geo_data["results"][0]["latitude"]
city_long = geo_data["results"][0]["longitude"]
#send coords to api
weather_url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": city_lat,"longitude": city_long, "current_weather" : True, "temperature_unit": "fahrenheit"}
weather_response = requests.get(weather_url, params=params)
weather_data = weather_response.json()
#pull wanted info from json
temp = weather_data["current_weather"]["temperature"]
#display to user
print(f"The current weather in {city} is {temp} degrees")