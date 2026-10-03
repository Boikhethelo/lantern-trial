from room.room import Room



def get_character(choice: int) -> str:
    match choice:
        case 1 : return "Hal Jordan"

    return "Hal Jordan"



def validate_move( direction: str , room: Room):
    exits = room.get_exits()
    if direction in exits.keys():
        return True
    else:
        return False
