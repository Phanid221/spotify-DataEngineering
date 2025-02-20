#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    playlist_URI = playlist_link.split('/')[-1].split('?')[0]
    data = sp.playlist_tracks(playlist_URI)
    print(data)
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket ="spotify-etl-project-phani",
        Key = "raw_data/to_be_processed/" + filename,
        Body = json.dumps(data)
        )

