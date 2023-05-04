import requests
import json

url = input("Enter the URL: ")

response = requests.get(url)

if response.status_code != 200 or '"' not in response.text:
    print("Invalid quote resource!")
else:
    quote = json.loads(response.text)["content"]
    print("Quote: ", quote)
