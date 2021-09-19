import spotipy
from spotipy import SpotifyClientCredentials
import os

prodigy_uri = 'spotify:artist:4k1ELeJKT1ISyDv8JivPpB'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_albums(prodigy_uri, album_type='album')

albums = results['items']


name = 'Led Zeppelin'
zep_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
results = spotify.artist(zep_uri)
res2 = spotify.artist_albums(zep_uri, album_type='album', limit=10)

artist_list = ['Deep Purple', 'Led Zeppelin', 'AC/DC', 'ZZ Top', 'The Beatles', "Guns 'N Roses", 'Metallica', 'Motorhead', 'Journey', 'Queen']

def search_artist_id(artist_list):
    a1 = []
    for artist in artist_list:
        rez = spotify.search(q='artist:' + artist, type='artist', limit=1)
        a1.append(rez)

    
def search_artist(art):
    a2 = []
    for artist in art:
        for i in artist.values():
            rez = spotify.artist(i['items'][0]['uri'].split(sep=':')[2])
            a2.append(rez)
    return a2
    