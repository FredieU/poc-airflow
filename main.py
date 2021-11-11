import datetime
import requests
import pandas as pd

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
SPOTIFY_USER_ID = "fredieu"
API_TOKEN = ""
SPOTIFY_RECENTS_URL = "https://api.spotify.com/v1/me/player/recently-played"

if __name__ == "__main__":
    # Prepare request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }

    # Calculate timestamp to fetch data from the past 24 hours
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_timestamp_miliseconds = int(yesterday.timestamp()) * 1000
    request_url = f"{SPOTIFY_RECENTS_URL}?after{yesterday_timestamp_miliseconds}"

    request = requests.get(
        url=request_url, 
        headers=headers
    )

    data = request.json()

    data_columns = [
        "song_names",
        "artist_names",
        "played_at_times",
        "timestamps"
    ]

    song_names = []
    artist_names = []
    played_at_times = []
    timestamps = []

    # Pick out desired information
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_times.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    songs_dict = {}
    for column in data_columns:
        songs_dict[column] = eval(column)

    songs_df = pd.DataFrame(data=songs_dict, columns=data_columns)
    print(songs_df)