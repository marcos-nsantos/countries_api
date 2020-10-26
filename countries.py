import requests

URL_ALL = "https://restcountries.eu/rest/v2"
URL_NAME = "https://restcountries.eu/rest/v2/name/bra"
answer = requests.get(URL_NAME)

print(answer.text)
