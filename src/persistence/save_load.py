import json
from pathlib import Path

from game.game import Game

SAVE_PATH = Path("resources/save_file.json")

def save_game(game: Game):

    rooms = {}
    for room in game.get_all_rooms().values():
        rooms.update(room.to_dict())


    data = {
        "character": game.get_player().get_name(),
        "charge": game.get_player().get_score(),
        "difficulty": game.get_difficulty(),
        "items": game.get_player().get_items(),
        "position": game.get_room().get_name(),
        "rooms" : rooms,
    }

    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SAVE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_game():
    with open(SAVE_PATH, "r") as file:
        return json.load(file)
