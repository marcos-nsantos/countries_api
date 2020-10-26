import json

import requests

URL_ALL = "https://restcountries.eu/rest/v2"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def web_request(url):
    try:
        answer = requests.get(URL_ALL)
        if answer.status_code == 200:
            return answer.text
    except:
        print(f"There was an error making your request in: {url}")


def parsing(answer_text):
    try:
        return json.loads(answer_text)
    except:
        print("There was an error making your request in:")


def count_countries(list_countries):
    return len(list_countries)


def list_countries(list_countries):
    for country in list_countries:
        print(country['name'])


def show_population(country_name):
    country_list = web_request(f"{URL_NAME}/ {country_name}")
    if country_list:
        pass

if __name__ == '__main__':
    answer_text = web_request(URL_ALL)
    if answer_text:
        list_of_countries = parsing(answer_text)
        if list_of_countries:
            list_countries(list_of_countries)
