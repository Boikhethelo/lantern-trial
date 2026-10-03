from database.database import Database
from room.room import Room
class RequestValidator:

    def __init__(self):
        self.database = Database("questions.db")

    def get_character(self,choice: int) -> str:
        match choice:
            case 1 : return "Hal Jordan"

        return "Hal Jordan"



    def validate_move(self,direction: str , room: Room):
        exits = room.get_exits()
        if direction in exits.keys():
            return True
        else:
            return False
