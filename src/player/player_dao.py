import json


from player.player import Player

class PlayerDAO:
    def __init__(self, name:str):
        self._name = name

    def get_character(self) -> Player:
        with open("/resources/character.json", "r", encoding='utf-8') as characters:
            data = json.load(characters)

        chosen_character = data[self._name]
        name = chosen_character["name"]
        sector = chosen_character["sector"]
        strength = chosen_character["strength"]
        weakness = chosen_character["weakness"]

        return Player(name, sector, strength, weakness)



