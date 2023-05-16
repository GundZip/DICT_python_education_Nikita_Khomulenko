import requests
import json
print("Product by Stell \n"
      "Hello")
print("--------------------------------------------------------------------------")

cache = {}

def get_exchange_rate(currency):
    if currency in cache:
        print("Checking the cache...")
        return cache[currency]
    else:
        print("Checking the website...")
        response = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
        data = json.loads(response.text)
        cache[currency] = data
        return data


def exchange_money():
    input_currency = input("Введіть код валюти, яку ви маєте (або натисни Enter для виходу ): ")
    while input_currency != "":
        exchange_currency = input("Введіть код валюти, на яку ви хочете обміняти: ")
        amount = float(input(f"Введіть суму {input_currency}, яку ви хочете обміняти: "))
        exchange_rate = get_exchange_rate(input_currency)[exchange_currency]
        result = round(amount * exchange_rate['rate'], 2)
        print("Checking the cache...")
        if exchange_currency in cache:
            print("It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
        print(f"You received {result} {exchange_currency}.")
        input_currency = input("Введіть код валюти, яку ви маєте (або натисни Enter для виходу ): ")

exchange_money()


print("--------------------------------------------------------------------------")
print("Have a nice day")
