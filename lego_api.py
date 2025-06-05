import os
import requests
from dotenv import load_dotenv
from model import LegoSet
import random

load_dotenv()

API_KEY = os.getenv("REBRICKABLE_API_KEY")
BASE_URL = "https://rebrickable.com/api/v3/lego/sets/"
HEADERS = { "Authorization": f"key {API_KEY}" }
_theme_cache: dict[int, str] = {}

def get_theme_name(theme_id: int) -> str:
    if theme_id in _theme_cache:
        return _theme_cache[theme_id]

    theme_url = f"https://rebrickable.com/api/v3/lego/themes/{theme_id}/"
    response = requests.get(theme_url, headers=HEADERS, verify=False)
    if response.status_code != 200:
        theme_name = f"Unknown Theme ({theme_id})"
    else:
        data = response.json()
        theme_name = data.get("name", f"Theme {theme_id}")

    _theme_cache[theme_id] = theme_name
    return theme_name

def get_random_set():
    # Step 1: get total number of sets
    meta_response = requests.get(f"{BASE_URL}?page_size=1", headers=HEADERS, verify=False)
    meta_response.raise_for_status()
    total = meta_response.json().get("count", 0)

    if total == 0:
        return None

    # Step 2: pick random index
    rand_index = random.randint(0, total - 1)
    page_size = 100  # max page size allowed
    page = rand_index // page_size
    index_on_page = rand_index % page_size

    # Step 3: fetch that page
    page_response = requests.get(
        f"{BASE_URL}?page_size={page_size}&page={page + 1}",  # pages are 1-indexed
        headers=HEADERS,
        verify=False
    )
    page_response.raise_for_status()
    results = page_response.json().get("results", [])

    if not results or index_on_page >= len(results):
        return None

    raw_set = results[index_on_page]
    theme_name = get_theme_name(raw_set['theme_id'])

    return LegoSet(
        name=raw_set['name'],
        year=raw_set['year'],
        piece_count=raw_set['num_parts'],
        theme=theme_name,
        image_url=raw_set.get('set_img_url')
    )