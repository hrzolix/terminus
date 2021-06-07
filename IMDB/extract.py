import requests
import os

url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

headers = {
    'x-rapidapi-key': os.environ.get("RAPID_API_KEY"),
    'x-rapidapi-host': os.environ.get("IMDB_HOST")
    }

response = requests.request("GET", url, headers=headers, params=querystring)

ls = response.json()
ls_5 = ls[:5]
l_cel = [i[6:-1] for i in ls_5]

ls1 = []

for i in l_cel:
    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    querystring = {"nconst":i}
    response = requests.request("GET", url, headers=headers, params=querystring)
    ls1.append(response.text)