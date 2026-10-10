from room.room import Room
class RequestValidator:

    def __init__(self):
        self.answer = ''
        self.trial_items = ["lens of hope" , "lens of will" , "lens of resolve"]



    def get_character(self,choice: int) -> str:
        if choice == "":
            return "Hal Jordan"
        match choice:
            case 1 : return "Hal Jordan"
            case 2 : return "John Stewart"
            case 3 : return "Jessica Cruz"
            case 4 : return "Kilowog"


        return "Hal Jordan"

    def inventory_check(self, items:list[str], requested : str) -> bool:

        parsed_items = [item.strip().lower() for item in items]

        for item in parsed_items:
            if requested == item:
                return True
        return False



    def validate_move(self,direction: str , room: Room , locked: bool):
        exits = room.get_exits()
        if direction in exits.keys() and locked != True:
            return True
        else:
            return False

    def is_trial_item(self, item:str, room_items: list[str]):

        if item.strip().lower() in room_items and item in self.trial_items:
            return True
        else:
            return False

    def is_final_room(self,direction : str, room_exits : dict):

        return room_exits[direction]


    def check_item(self, item: str , room_items: list[str]):

        if item.strip().lower() in room_items:
            return True
        else:
            return False


    def central_power_battery_chamber_requirements(self,items) -> bool:

        required = 0
        for item in items:
            if item in self.trial_items:
                required += 1

        if required == 3:
            return True
        else:
            return False

    def will_forge_requirements(self,items) -> bool:

        required = "lens of hope"
        for item in items:
            if item == required:
                return True
        return False

