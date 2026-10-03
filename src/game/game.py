from room import room
from room.room_dao import RoomDAO
from validation.input_validator import InputValidator
from player.player import Player
from room.room import Room
import display



class Game:
    def __init__(self, player:Player):
        self.room_loader = RoomDAO()

        self.player = player
        self.room = self.room_loader.load_room("Guardian Citadel")



    def move_room(self, direction:str):

        exits : dict[str,str] = self.get_room().get_exits()

        next_room : str = exits.get(direction)
        self.room = self.room_loader.load_room(next_room)



    def view_items_in_room(self):
        return self.room.get_items()


    def get_room(self):
        return self.room

    def view_player_items(self):
        return self.player.get_items()

    def save(self):
        """TODO"""

    def load(self):
        """TODO"""

    def exit(self):
        return False
























