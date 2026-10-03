import json


from player.player import Player

class PlayerDAO:
    def __init__(self):
        self._location = "resources/character.json"
        self._data = self._load_data()


    def _load_data(self):
        with open(self._location, "r" , encoding='utf-8') as player_data:
            return json.load(player_data)


    def get_character(self, name) -> Player:

        chosen_character = self._data.get(name)
        name = name
        sector = chosen_character.get("sector")
        strength = chosen_character.get("strength")
        weakness = chosen_character.get("weakness")

        return Player(name, sector, strength, weakness)



