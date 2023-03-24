import requests
import json
print("Product by Stell \n"
      "Hello")
print("--------------------------------------------------------------------------")
money = input("Please enter currency code (USD, EUR): ")
url = f"http://www.floatrates.com/daily/{money}.json"
response = requests.get(url)
data = json.loads(response.text)
if "usd" in data:
      usd = data['usd']['rate']
      print(f"Exchange rate for USD: {usd} EUR")
if "eur" in data:
      eur = data ['eur']['rate']
      print(f"Exchange rate for eur: {eur} USD")


print("--------------------------------------------------------------------------")
print("Have a nice day")
