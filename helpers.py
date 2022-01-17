import urllib.parse
import requests
import json


def cityfinder(cityname):
    """Accessing api key from file."""
    
   
    """Finds the city the user is looking for."""
    try:
        f = open('apikeys.json')
        findkey = json.load(f)
        apikey = str(findkey['API_Key'])
        f.close()
        url = f"http://api.weatherstack.com/current?access_key={apikey}&query={urllib.parse.quote_plus(cityname)}&units=m"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    try:
        data = response.json()
        return {
            "temp": data['current']['temperature'],
            "felltemp": data['current']['feelslike'],
            "wind": data['current']['wind_speed'],
            "description": data['current']['weather_descriptions'][0]
        }
    except (KeyError, TypeError, ValueError):
        return None