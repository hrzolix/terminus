import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"s":"Avengers Endgame","r":"json","page":"1"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "b2ad99815bmshabdd84715b31552p194ccdjsnf1751e22dfbe"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)