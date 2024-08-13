import requests
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import os 

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)




playlist_URI = playlist_link.split("/")[-1].split("?")[0]

print(playlist_URI)

track_uris = [x["track"]["uri"]
              for x in sp.playlist_tracks(playlist_URI, limit = 100, offset = 0)["items"]]
# print(len(track_uris))
        
        
             