from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Web Scraping for the songs on Billboard (Works):
playlist_date = input("Which year do you want to travel to? Format: YYYY-MM-DD ")
year = playlist_date.split("-")[0]
URL = "https://www.billboard.com/charts/hot-100/" + "2001-11-12"
response = requests.get(URL)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")
song_titles = soup.select("li ul li h3")
title_list = [title.text.strip() for title in song_titles]

# Spotify Authentication (works):
CLIENT_ID = "Spotify Client ID"
CLIENT_SECRET = "Spotify Client Secret"
redirect_uri = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=redirect_uri,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="spotify username "
    )
)
user_id = sp.current_user()["id"]

# Get a list of the song uris and check to see if it exists in spotify or not:
uri_list = []
for title in title_list:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{title} doesn't exsit in spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=sp.current_user()['id'],
    name=f"{playlist_date} Top Billboard 100",
    public=False,
)
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=uri_list
)
