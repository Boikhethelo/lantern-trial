from question.question import Question
from question.question_dao import QuestionDAO
from room.room import Room
from room.room_dao import RoomDAO
from player.player import Player

import display.display as display

class Game:
    def __init__(self, player:Player , difficulty_setting):
        self._question = None
        self._questions = []
        self._rooms = {}
        self._question_loader = QuestionDAO()
        self._player = player
        self._difficulty = difficulty_setting




    def load_all_rooms(self):

        room_data = RoomDAO().load_data()

        for room_name in room_data:
            current = self.load_room(room_name, room_data[room_name])
            self._rooms.update({current.get_name() : current})


    def set_all_rooms(self, rooms:dict[str,Room]):
        self._rooms = rooms

    def load_room(self, name:str , room:dict) -> Room:

        name = name
        description = room.get("description")
        exits = room.get("exits")
        items = room.get("items")
        status = room.get("locked")

        return Room(name, description, exits, items, status )



    def move_room(self, direction:str):

        exits : dict[str,str] = self.get_room().get_exits()
        name : str | None = exits.get(direction)
        next_room = self._rooms.get(name)
        self._room = next_room
        self._player.set_position(self._room.get_name())
        return "Moved to " + self._room.get_name()



    def view(self):
        display.view_room(self._room.get_name() , self.get_room().get_description())
        display.view_items(self._room.get_items())

    def load_question(self) -> Question | None:

        self._question = self._question_loader.load_question(self._room.get_name(), self._difficulty, self._player.get_name())
        if self._question:
            self._questions.append(self._question)
            return self._question
        else:
            return None


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




