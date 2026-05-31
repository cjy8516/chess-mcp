import requests

CHESS_API_URL = "https://api.chess.com/pub/"

headers = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/3.10 requests/2.31.0"
}   

def get_player_profile(username):
    """Fetches the profile of a chess player by their username."""
    url = f"{CHESS_API_URL}player/{username}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    
    return response.json()

def get_player_stats(username):
    """Fetches the statistics of a chess player by their username."""
    url = f"{CHESS_API_URL}player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()