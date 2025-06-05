import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REBRICKABLE_API_KEY")
BASE_URL = "https://rebrickable.com/api/v3/lego/sets/"
HEADERS = { "Authorization": f"key {API_KEY}" }

def get_random_set():
    response = requests.get(f"{BASE_URL}?page_size=1&ordering=random", headers=HEADERS)
    response.raise_for_status()
    results = response.json().get("results", [])
    return results[0] if results else None
