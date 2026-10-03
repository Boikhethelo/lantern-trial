import display.display
from validation.input_validator import InputValidator
from player.player_dao import PlayerDAO
from game.game import Game
from validation.request_validator import RequestValidator


class Play:

    def __init__(self):
        self.input_validator = InputValidator()
        self.validator = RequestValidator()
        self.player_loader = PlayerDAO()
        self.game = self._start()

    def _route(self ,commands: list[str]) -> bool:

        match commands[0]:
            case "go": self._move_request(commands[1])
            case "look" : self.game.view()
            case "take" : self._take_request(commands[1])
            case "use"  : print("""TODO""")
            case "charge" : print("""TODO""")
            case "help"  : display.show_help()
            case "save"  : self.game.save()
            case "load" : self.game.load()

        return True


    def _move_request(self, direction: str):

        if self.validator.validate_move(direction , self.game.get_room()):
            self.game.move_room(direction)
            print("Moved to " + self.game.get_room().get_name())
        else:
            print("Unable to move in that direction! ")

    def _take_request(self, chosen_item):

        if self.validator.check_item(chosen_item):
            self.game.load_trial()
            question = self.game.get_question()
            trial = True
            while trial:
                display.view_question(question)
                answer = input("Enter your answer: ")

                if self._check_answer(answer):
                    self.game.get_player().add_item(chosen_item)
                    trial = False
                else:
                    pass

        else:
            self.game.get_player().add_item(chosen_item)

    def _check_answer(self,answer):
        if answer == self.game.get_answer():
            return True
        else:
            return False


    def _start(self):
        display.start()

        choice = int(input("Select a character : "))
        character = self.validator.get_character(choice)


        player = self.player_loader.get_character(character)

        return Game(player, 1)


    def main(self) -> None:
        run = True

        while run:
            raw_command : str = input("What would you like to do next : ")

            if raw_command in ["exit" , "quit"]:
                run = False

            parsed_command = self.input_validator.validate_command(raw_command)

            if len(parsed_command)  > 0:
                run = self._route(parsed_command)
            else:
                print("Invalid command")

if __name__ == "__main__":
    play = Play()
    play.main()

