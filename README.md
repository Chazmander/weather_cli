# weather_cli

A small Python command-line app that shows the current weather and a short hourly forecast for a user-provided city.

It uses the free **Open-Meteo** APIs:
- Geocoding API (city name → latitude/longitude)
- Forecast API (hourly temperature + weather codes)

## Features
- Prompts for a city name
- Resolves the city to coordinates via Open-Meteo geocoding
- Fetches hourly weather for today and tomorrow
- Prints:
  - “Current” conditions (nearest hour at/after the current time)
  - A forecast for the next 5 hours
- Temperature shown in **Fahrenheit**

## Requirements
- Python 3.9+ (3.11+ recommended)
- `requests`

## Setup
Install dependencies:
- `pip install requests`

## Run
From the project folder:
- `python main.py`

Then enter a city name when prompted.

Example output (format):
- `The current weather in City, Region is 72.3°F with clear skies`
- Followed by the next 5 hourly lines.

## Notes / Limitations
- If the geocoding API returns no results, the program exits.
- “Current weather” is derived from the first hourly datapoint whose timestamp is **>=** your local system time.
- Weather descriptions come from Open-Meteo `weathercode` values mapped in `main.py`.

## APIs
- Geocoding: https://geocoding-api.open-meteo.com/v1/search
- Forecast: https://api.open-meteo.com/v1/forecast

## License
Add a license if you plan to distribute this project.