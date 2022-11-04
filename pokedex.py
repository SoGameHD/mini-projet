import requests

api_url = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"
data = requests.get(api_url).json()

print(len(data["results"]))