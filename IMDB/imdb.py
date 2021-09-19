import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"s":"Avengers Endgame","r":"json","page":"1"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
