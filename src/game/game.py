from room.room_dao import RoomDAO
from validation.command_validator import CommandValidator
from player.player import Player
from room.room import Room
import display


class Game:
    def __init__(self, player:Player, room:Room):
        self.validator = CommandValidator
        self.player = player
        self.room = room
        self.room_loader = RoomDAO

    def move_room(self, direction:str):
        """TODO"""


    def view_items_in_room(self):
        return self.room.get_items()

    def get_rooms_description(self):
        return self.room.get_description()

    def view_player_items(self):
        return self.player.get_items()

    def save(self):
        """TODO"""

    def load(self):
        """TODO"""

    def exit(self):
        return False
























