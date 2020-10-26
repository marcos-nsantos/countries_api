import json

import requests

URL_ALL = "https://restcountries.eu/rest/v2"
URL_NAME = "https://restcountries.eu/rest/v2/name/bra"
answer = requests.get(URL_ALL)

countries = json.loads(answer.text)  # JSON parsing to python object

for country in countries:
    print(country["name"], country["currencies"])
