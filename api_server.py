from fastapi import FastAPI
from lego_api import get_random_set
from model import LegoSet

app = FastAPI()

@app.get("/random-set")
def random_set():
    lego_set = get_random_set()
    if not lego_set:
        return {"error": "Could not fetch LEGO set."}
    return {
        "name": lego_set.name,
        "year": lego_set.year,
        "pieces": lego_set.piece_count,
        "theme": lego_set.theme,
        "image_url": lego_set.image_url,
    }
