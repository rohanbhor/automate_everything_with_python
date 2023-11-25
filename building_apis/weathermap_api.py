import requests
from pprint import pprint

url = "https://api.openweathermap.org/data/2.5/forecast"

query_params = {
    "q": "India",
    "APPID": "d68cfefa67ce489792b9278c63db9acd"
}

response = requests.get(url, params=query_params)

pprint(response.json())