from fastapi import FastAPI
from lego_api import get_random_set
from model import LegoSet
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware, # gives warning but is common, can ignore
    allow_origins=["*"],  # change this to Vue dev server later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuessRequest(BaseModel):
    guess: str
    answer: str
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

@app.post("/guess")
def check_guess(data: GuessRequest):
    is_correct = data.guess.lower().strip() in data.answer.lower().strip()
    return {"correct": is_correct}