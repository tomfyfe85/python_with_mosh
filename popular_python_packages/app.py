import requests
url = "https://rickandmortyapi.com/api/character/822"
response = requests.get(url)
result = response.json()["origin"]["url"]

print(result)