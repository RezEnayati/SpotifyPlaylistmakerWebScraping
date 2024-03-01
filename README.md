## Project README: Billboard Top 100 Playlist Creator

This project involves creating a Spotify playlist based on the Billboard Top 100 songs from a specified date. It utilizes web scraping with BeautifulSoup to extract song titles from the Billboard website and interacts with the Spotify API using Spotipy to search for the songs and create a playlist.

### Components:

1. **Web Scraping with BeautifulSoup:**
   - The `requests` library is used to fetch the HTML content of the Billboard website for a specified date.
   - BeautifulSoup is employed to parse the HTML and extract the song titles listed on the Billboard Top 100 chart.
   - The extracted song titles are stored in a list named `title_list`.

2. **Spotify Authentication with Spotipy:**
   - Spotify OAuth2 authentication is implemented using Spotipy to gain access to the Spotify API.
   - The Spotify client ID, client secret, and redirect URI are provided for authentication.
   - The necessary scopes are defined to allow modifications to private playlists.
   - A cache file named `token.txt` is used to store the authentication token.
   - The username of the Spotify account is specified to link the script to the correct user.

3. **Searching for Songs on Spotify:**
   - For each song title extracted from Billboard, a search query is performed on Spotify using Spotipy.
   - The search query includes the song title and the year to narrow down the search results.
   - If a matching track is found on Spotify, its URI (Uniform Resource Identifier) is extracted and added to the `uri_list`.

4. **Creating and Populating a Spotify Playlist:**
   - A new private playlist is created on the user's Spotify account using the `user_playlist_create` method from Spotipy.
   - The playlist name is based on the specified date for the Billboard chart.
   - The list of Spotify track URIs (`uri_list`) is added to the newly created playlist using the `playlist_add_items` method.

### Usage:

1. **Input Date for Billboard Chart:**
   - When running the script, the user is prompted to input a date in the format `YYYY-MM-DD` for the Billboard chart they want to create a playlist for.

2. **Web Scraping:**
   - The script scrapes the Billboard website for the specified date to extract the song titles from the Top 100 chart.

3. **Spotify Authentication:**
   - OAuth2 authentication with Spotify is initiated using Spotipy, requiring the user to log in and authorize access.

4. **Searching and Creating Playlist:**
   - The script searches for each song title on Spotify, retrieves the track URI if found, and stores it in a list.
   - A new private playlist is created on the user's Spotify account with the name based on the input date.
   - The list of Spotify track URIs is added to the newly created playlist.

### Dependencies:

- **BeautifulSoup**: Used for web scraping to parse HTML content and extract relevant information.
- **Requests**: Required to fetch HTML content from web pages.
- **Spotipy**: A lightweight Python library for the Spotify Web API, used for authentication and interacting with Spotify.

### Spotify Account:

To use this script, you need a Spotify account. Ensure that you have created a Spotify Developer account to obtain the client ID and client secret required for authentication.

### Notes:

- If a song title from Billboard cannot be found on Spotify, the script prints a message indicating that the song was skipped.

- Make sure to replace placeholders such as "Spotify Client ID", "Spotify Client Secret", "http://example.com", and "spotify username" with your actual Spotify credentials and username.

### Contributors:

- This project was created by [Reza Enayati].

Feel free to modify and improve this script according to your needs! If you encounter any issues or have suggestions, please don't hesitate to reach out. Happy playlist creation!
