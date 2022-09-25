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
        streetmapurl = f"https://nominatim.openstreetmap.org/search?city={urllib.parse.quote_plus(cityname)}&format=json&addressdetails=1&limit=1"
        r = requests.get(streetmapurl)
        r.raise_for_status()
        coord = r.json()
        if coord:
            lat = coord[0]['lat']
            lon = coord[0]['lon']
            #url = f"http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote_plus(cityname)}&appid={apikey}&units=metric"
            url = f"https://api.openweathermap.org/data/2.5/onecall?lat={urllib.parse.quote_plus(lat)}&lon={urllib.parse.quote_plus(lon)}&appid={apikey}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
        else:
            return None
    except requests.RequestException:
        return None
    try:
        data = response.json()

        with open("weathermap.json", "w") as write_file:
            json.dump(data, write_file, indent=4)

        return {
            "temp": round(data['current']['temp']),
            "feeltemp": round(data['current']['feels_like']),
            "wind": round(data['current']['wind_speed']),
            "icons": data['current']['weather'][0]['icon'],
            "description": data['current']['weather'][0]['description'],
            "humidity": data['current']['humidity'],
            "dewpoint": round(data['current']['dew_point']),
            "uvi": data['current']['uvi'],
            "pressure": data['current']['pressure'],
            "vis": data['current']['visibility']
        }
    except (KeyError, TypeError, ValueError):
        return None