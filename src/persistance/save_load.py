import json
from pathlib import Path

SAVE_PATH = Path("resources/save_file.json")

def save_game(player, score, difficulty, items, room):
    data = {
        "character": player,
        "score": score,
        "difficulty": difficulty,
        "items": items,
        "room": room,
    }

    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SAVE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_game():
    with open(SAVE_PATH, "r") as file:
        return json.load(file)
