import json

from room.room import Room

class RoomDAO:
    def __init__(self):
        self._location = "resources/game_data.json"


    def load_data(self):
        with open(self._location, "r" , encoding='utf-8') as game_data:
            return json.load(game_data)

 


