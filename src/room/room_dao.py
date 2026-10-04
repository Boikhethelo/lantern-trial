import json

from room.room import Room

class RoomDAO:
    def __init__(self):
        self._location = "resources/game_data.json"


    def load_data(self):
        with open(self._location, "r" , encoding='utf-8') as game_data:
            return json.load(game_data)

    # def load_room(self, name:str) -> Room:
    #
    #     chosen_room = self._data[name]
    #     name = name
    #     description = chosen_room.get("description")
    #     exits = chosen_room.get("exits")
    #     items = chosen_room.get("items")
    #     status = chosen_room.get("locked")
    #
    #     return Room(name, description, exits, items, status )


