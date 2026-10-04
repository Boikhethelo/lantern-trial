from player.player_dao import PlayerDAO
from question.question_dao import QuestionDAO
from persistence import save_load as storage
from room.room import Room
from room.room_dao import RoomDAO
from player.player import Player

import display.display as display

class Game:
    def __init__(self, player:Player , difficulty_setting):
        self._question = None
        self._room_data = RoomDAO().load_data()
        self._question_loader = QuestionDAO()

        self._player = player
        self._difficulty = difficulty_setting

        self._room = self._load_room("Guardian Citadel")

    def _load_room(self, name:str) -> Room:

        chosen_room = self._room_data.get(name)
        name = name
        description = chosen_room.get("description")
        exits = chosen_room.get("exits")
        items = chosen_room.get("items")
        status = chosen_room.get("locked")

        return Room(name, description, exits, items, status )


    def move_room(self, direction:str):


        exits : dict[str,str] = self.get_room().get_exits()

        next_room : str = exits.get(direction)


        if not self._room_data[next_room].get("locked"):
            self._room = self._load_room(next_room)
            self._player.set_position(self._room.get_name())
            return "Moved to " + self._room.get_name()

        else:
            return "Locked! "


    def view(self):
        display.view_room(self._room.get_name() , self.get_room().get_description())
        display.view_items(self._room.get_items())

    def load_trial(self):
        self._question = self._question_loader.load_question(self._room.get_name(), self._difficulty)


    def get_question(self):
        return self._question.get_question()

    def get_answer(self):
        return self._question.get_answer()


    def view_items_in_room(self):
        return self._room.get_items()


    def get_room(self):
        return self._room

    def get_player(self):
        return self._player

    def view_player_items(self):
        return self._player.get_items()


    def unlock_room(self, room):
            self._room_data[room]["locked"] = False


    def save(self):
        storage.save_game(self._player.get_name(), self._player.get_score() , self._difficulty , self._player.get_items() , self._room.get_name())

    def load(self):
        load_data = storage.load_game()
        character = load_data.get("character")
        room = load_data.get("room")
        score = int(load_data.get("score"))
        difficulty = int(load_data.get("difficulty"))
        items = load_data.get("items")

        self._player = PlayerDAO().get_character(character)
        self._room = self._load_room(room)

        self._player.set_position(room)
        self._player.set_score(score)
        self._player.set_items(items)
        self._difficulty = difficulty


