from database.database import Database
from room.room import Room
class RequestValidator:

    def __init__(self):
        self.answer = ''
        self.trial_items = ["Lens of Hope" , "Lens of Will" , "Void of Fear"]

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

    def check_item(self, item):
        if item in self.trial_items:
            return True
        else:
            return False
