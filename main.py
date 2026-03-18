import requests

#ask for city
city = input("Enter a City: ").strip().title()

#convert city to coords with api
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name" : city, "count" : 1}
geo_response = requests.get(geo_url, params=params)
geo_data = geo_response.json()
if "results" not in geo_data or len(geo_data["results"]) == 0:
    print(f"No results for {city}")
    exit()
city_lat = geo_data["results"][0]["latitude"]
city_long = geo_data["results"][0]["longitude"]

#send coords to api
weather_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": city_lat,
    "longitude": city_long,
    "current_weather": True,
    "temperature_unit": "fahrenheit",
    "hourly": "temperature_2m,weathercode"}

weather_response = requests.get(weather_url, params=params)
print(weather_response)
weather_data = weather_response.json()
#pull data from json
temp = weather_data["current_weather"]["temperature"]
weather_code = weather_data["current_weather"]["weathercode"]
#weathercode table
weather_codes = {
    0: "Clear sky ☀️",

    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",

    45: "Fog 🌫️",
    48: "Depositing rime fog 🌫️",

    51: "Light drizzle 🌦️",
    53: "Moderate drizzle 🌦️",
    55: "Dense drizzle 🌧️",

    56: "Light freezing drizzle 🧊🌧️",
    57: "Dense freezing drizzle 🧊🌧️",

    61: "Slight rain 🌧️",
    63: "Moderate rain 🌧️",
    65: "Heavy rain 🌧️",

    66: "Light freezing rain 🧊🌧️",
    67: "Heavy freezing rain 🧊🌧️",

    71: "Slight snow ❄️",
    73: "Moderate snow ❄️",
    75: "Heavy snow ❄️",

    77: "Snow grains ❄️",

    80: "Slight rain showers 🌦️",
    81: "Moderate rain showers 🌧️",
    82: "Violent rain showers ⛈️",

    85: "Slight snow showers ❄️",
    86: "Heavy snow showers ❄️",

    95: "Thunderstorm ⛈️",
    96: "Thunderstorm with slight hail ⛈️🧊",
    99: "Thunderstorm with heavy hail ⛈️🧊"
}
condition = weather_codes[weather_code]

#display to user
print(f"The current weather in {city} is {temp} degrees and {condition}")