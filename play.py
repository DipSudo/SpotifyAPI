import requests
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

from info import *


client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)




playlist_URI = playlist_link.split("/")[-1].split("?")[0]

print(playlist_URI)

track_uris = [x["track"]["uri"]
              for x in sp.playlist_tracks(playlist_URI, limit = 100, offset = 0)["items"]]
# print(len(track_uris))
        
        
             