import requests
import json

print("Connecting to ISS satellite...")
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    print("Connection Successful!")
    data = json.loads(response.text)
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    print("Current Location:")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Failed to connect to the ISS API.")
