import spotipy
from spotipy import SpotifyClientCredentials
import os

prodigy_uri = 'spotify:artist:4k1ELeJKT1ISyDv8JivPpB'
spotify = spotipy.Spotify()
results = spotify.artist_albums(prodigy_uri, album_type='album')

albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

print(albums)

