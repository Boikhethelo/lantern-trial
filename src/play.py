import display.display
from validation.command_validator import CommandValidator
import validation.request_validator as validate
from player.player_dao import PlayerDAO
from room.room_dao import RoomDAO
from game.game import Game

class Play:
    def __int__(self):
        display.start()
        self.command_validator = CommandValidator
        self.player_loader = PlayerDAO()
        self.room_loader =RoomDAO



    def _route(self ,commands: list[str]) -> bool:


        match commands[0]:
            case "go": self._move_request(commands[1])

        return True


    def _move_request(self, direction: str) -> bool:

        if validate.validate_move(direction , self.game.get_room()):
            self.game.move_room(direction)
            print("Moved to " + self.game.get_room().get_name())

        return True




    def main(self) -> None:
        run = True

        display.start()

        choice = int(input("Select a character : "))
        character = validate.get_character(choice)


        player = self.player_loader.get_character(character)

        self.game = Game(player)


        while(run):
            raw_command : str = input("What would you like to do next : ")
            parsed_command = self.command_validator.validate_command(raw_command)

            if len(parsed_command)  > 0:
                run = self._route(parsed_command)
            else:
                print("Invalid command")
