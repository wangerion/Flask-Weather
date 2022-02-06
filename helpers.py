import urllib.parse
import requests
import json

class finder:
    """
    Accessing api key from JSON file.     
    """
    def __init__(self, path, apiname):
        self.path = path
        self.apiname = apiname
    #Loading apikey using the path specified and the key where the value we want is.
    def load(self):
        f = open(self.path)
        findkey = json.load(f)
        key = findkey[self.apiname]
        f.close()
        return key


def cityfinder(cityname):
    """Finds the city the user is looking for."""
    try:
        api1 = finder('apikey.json','API_Key' )
        apikey = api1.load()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote_plus(cityname)}&appid={apikey}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        data = response.json()
        return {
            "temp": round(data['main']['temp']),
            "feeltemp": round(data['main']['feels_like']),
            "wind": round(data['wind']['speed']),
            #"icons": "https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0027_light_snow_showers_night.png", #data['current']['weather_icons'],
            "description": data['weather'][0]['description']
        }
    except (KeyError, TypeError, ValueError):
        return None