import json

from room.room import Room

class RoomDAO:
    def __init__(self, name:str):
        self._name = name

    def load_room(self) -> Room:
        with open("/resources/game_data.json") as game_data:
            data = json.load(game_data)

        chosen_room = data[self._name]
        name = self._name
        description = chosen_room.get("description")
        exits = chosen_room.get("exits")
        items = chosen_room.get("items")
        status = chosen_room.get("locked")

        return Room(name, description, exits, items, status )


