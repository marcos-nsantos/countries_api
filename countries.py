import json
import sys

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


def count_countries():
    answer = web_request(URL_ALL)
    if answer:
        list_of_countries = parsing(answer)
        if list_of_countries:
            return len(list_of_countries)


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


def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("It's necessary to type country name")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("### WELCOME TO COUNTRY SYSTEM ###")
        print("How to use: python countries.py <action> <country_name>")
        print("Actions: count, currency, population")
    else:
        argument1 = sys.argv[1]

        if argument1 == "count":
            countries_number = count_countries()
            print(f"There are {countries_number} countries.")

        elif argument1 == "currency":
            country = read_country_name()
            if country:
                show_currency(country)

        elif argument1 == "population":
            country = read_country_name()
            if country:
                show_population(country)

        else:
            print("Invalid argument")
