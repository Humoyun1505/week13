import requests
import json

country = input("Enter a country to search: ")
url = "http://universities.hipolabs.com/search"
params = {
    "country": country
}
response = requests.get(url, params=params)
data = json.loads(response.text)
if len(data) == 0:
    print(f"No universities found for {country}.")
else:
    print(f"Found {len(data)} universities in {country}.")
    print("Here are the first 5:")

    for i, university in enumerate(data[:5], start=1):
        print(f"{i}. {university['name']}")

