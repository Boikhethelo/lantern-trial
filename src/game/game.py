from question.question_dao import QuestionDAO
from room.room import Room
from room.room_dao import RoomDAO
from player.player import Player

import display.display as display

class Game:
    def __init__(self, player:Player , difficulty_setting):
        self._question = None
        self._room_data = RoomDAO().load_data()
        self._rooms = {}
        self._question_loader = QuestionDAO()
        self._player = player
        self._difficulty = difficulty_setting


    def load_all_rooms(self) -> dict[str,Room]:
        output = {}

        for room_name in self._room_data:
            current = self.load_room(room_name)
            output.update({current.get_name() : current})

        return output

    def set_all_rooms(self, rooms:dict[str,Room]):
        self._rooms = rooms



    def load_room(self, name:str) -> Room:

        chosen_room = self._room_data.get(name)
        name = name
        description = chosen_room.get("description")
        exits = chosen_room.get("exits")
        items = chosen_room.get("items")
        status = chosen_room.get("locked")

        return Room(name, description, exits, items, status )

    def load_saved_rooms(self, rooms):
        self._rooms = rooms


    def move_room(self, direction:str):

        exits : dict[str,str] = self.get_room().get_exits()

        name : str | None = exits.get(direction)

        next_room = self._rooms.get(name)


        if not next_room.get_status():
            self._room = next_room
            self._player.set_position(self._room.get_name())
            return "Moved to " + self._room.get_name()

        else:
            return "Locked! "


    def view(self):
        display.view_room(self._room.get_name() , self.get_room().get_description())
        display.view_items(self._room.get_items())

    def load_trial(self) -> bool:

        self._question = self._question_loader.load_question(self._room.get_name(), self._difficulty, self._player.get_name())
        if self._question:
            return True
        else:
            return False


    def get_question(self):
        return self._question.get_question()

    def get_answer(self):
        return self._question.get_answer()


    def view_items_in_room(self):
        return self._room.get_items()


    def get_room(self):
        return self._room

    def get_all_rooms(self):
        return self._rooms

    def set_room(self, room_name:str):
        self._room = self._rooms[room_name]

    def get_player(self):
        return self._player

    def get_difficulty(self):
        return self._difficulty

    def view_player_items(self):
        return self._player.get_items()


    def unlock_room(self, room:str):
            self._rooms[room].set_status(False)




