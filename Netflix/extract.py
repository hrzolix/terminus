import requests
import os
url = "https://unogsng.p.rapidapi.com/genres"

headers = {
    'x-rapidapi-key': os.environ.get("NETFLIX_KEY"),
    'x-rapidapi-host': os.environ.get("NETFLIX_HOST")
    }

response = requests.request("GET", url, headers=headers)

print(response.text)