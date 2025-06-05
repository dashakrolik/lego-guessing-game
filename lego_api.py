import os
import requests
from dotenv import load_dotenv
from model import LegoSet

load_dotenv()

API_KEY = os.getenv("REBRICKABLE_API_KEY")
BASE_URL = "https://rebrickable.com/api/v3/lego/sets/"
HEADERS = { "Authorization": f"key {API_KEY}" }


def get_random_set():
    response = requests.get(f"{BASE_URL}?page_size=1&ordering=random", headers=HEADERS)
    response.raise_for_status()
    results = response.json().get("results", [])
    if not results:
        return None

    raw_set = results[0]

    # Construct LegoSet object
    return LegoSet(
        name=raw_set['name'],
        year=raw_set['year'],
        piece_count=raw_set['num_parts'],
        theme=raw_set['theme_id']  # We'll improve this later
    )

