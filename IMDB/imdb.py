import requests
import os
import json

headers = {
    'x-rapidapi-key': os.environ.get("RAPID_API_KEY"),
    'x-rapidapi-host': os.environ.get("IMDB_HOST")
    }

def top_5_us_actors():
    url_most_pop = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"
    par = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}
    celebs = requests.request("GET", url_most_pop, headers=headers, params=par, )
    unformated = celebs.json()
    top_5_long = unformated[:5]
    top_5 = [i[6:-1] for i in top_5_long]
    return top_5


def top_5_actors_filmography(top_actors):
    films = []
    for actor in top_actors:
        url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
        querystring = {"nconst":actor}
        movies = requests.request("GET", url, headers=headers, params=querystring)
        films.append(json.dumps(movies.json(), indent=2))
    
    return films

if __name__ == "__main__":
    top_5 = top_5_us_actors()
    film = top_5_actors_filmography(top_5)
    print(film)