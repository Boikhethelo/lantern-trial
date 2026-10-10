import display.display as display
from validation.input_validator import InputValidator
from player.player_dao import PlayerDAO
from validation.request_validator import RequestValidator
from requests.requests import Requests
from router.router import Router


class Play:

    def __init__(self):
        self.input_validator = InputValidator()
        self.player_loader = PlayerDAO()
        self.game = None
        self.validator = RequestValidator()
        self.requests = Requests(self.validator)
        self.router = Router()

    def main(self) -> None:
        display.start()
        game_choice = input("Type 'load' to continue a previous game? ")

        if game_choice.strip().lower() == "load":
            self.game = self.requests.load_game()
        else:
            self.game = self.requests.start()

        run = True

        while run:

            raw_command : str = input("What would you like to do next : ")

            if raw_command in ["exit" , "quit"]:
                run = False
            else:
                parsed_command = self.input_validator.validate_command(raw_command)


                if len(parsed_command)  > 0:
                    result = self.router.route(parsed_command, self.requests, self.game)
                    display.view(result)
                    display.view(self.requests.check_requirements(self.game))
                else:
                    print("Invalid command")

if __name__ == "__main__":
    play = Play()
    play.main()

