import requests
import config

response = requests.get(config.url)
result = response.json()["origin"]["url"]

print(result)