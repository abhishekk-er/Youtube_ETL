import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try:
        url = (
            "https://youtube.googleapis.com/youtube/v3/channels"
            f"?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        )

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if not data.get("items"):
            raise ValueError("Channel not found")

        channel_items = data["items"][0]
        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        return channel_playlist_id

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")

if __name__ == "__main__":
    print(get_playlist_id())