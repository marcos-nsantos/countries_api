import json

import requests

URL_ALL = "https://restcountries.eu/rest/v2"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def web_request(url):
    try:
        answer = requests.get(url)
        if answer.status_code == 200:
            return answer.text
    except:
        print(f"There was an error making your request in: {url}")


def parsing(answer_text):
    try:
        return json.loads(answer_text)
    except:
        print("There was an error making your request in:")


def count_countries(countries_list):
    return len(countries_list)


def list_countries(countries):
    for country in countries:
        print(country['name'])


def show_population(country_name):
    answer = web_request(f"{URL_NAME}/{country_name}")
    if answer:
        list_of_countries = parsing(answer)
        if list_of_countries:
            for country in list_of_countries:
                print(f"{country['name']}: {country['population']}")
        else:
            print("Country was not found")


def show_currency(country_name):
    answer = web_request(f"{URL_NAME}/{country_name}")
    if answer:
        list_of_countries = parsing(answer)
        if list_of_countries:
            for country in list_of_countries:
                print(f"{country['name']} currencies:")
                currency = country['currencies']
                for currencies in currency:
                    print(f"{currencies['name']} - {currencies['code']}")
        else:
            print("Country was not found")
