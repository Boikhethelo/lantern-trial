import display.display
from validation.input_validator import InputValidator
import validation.request_validator as validate
from player.player_dao import PlayerDAO
from room.room_dao import RoomDAO
from game.game import Game
from validation.request_validator import RequestValidator


class Play:
    def __int__(self):
        self.input_validator = InputValidator()
        self.validator = RequestValidator()
        self.player_loader = PlayerDAO()
        self.room_loader =RoomDAO()




    def _route(self ,commands: list[str]) -> bool:


        match commands[0]:
            case "go": self._move_request(commands[1])

        return True


    def _move_request(self, direction: str) -> bool:

        if self.validator.validate_move(direction , self.game.get_room()):
            self.game.move_room(direction)
            print("Moved to " + self.game.get_room().get_name())
        else:
            print("Unable to move in that direction! ")

        return True




    def main(self) -> None:
        run = True

        display.start()

        choice = int(input("Select a character : "))
        character = self.validator.get_character(choice)


        player = self.player_loader.get_character(character)

        self.game = Game(player)


        while(run):
            raw_command : str = input("What would you like to do next : ")
            parsed_command = self.input_validator.validate_command(raw_command)

            if len(parsed_command)  > 0:
                run = self._route(parsed_command)
            else:
                print("Invalid command")
