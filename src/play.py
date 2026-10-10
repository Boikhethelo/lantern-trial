import display.display as display
from trials.trial_runner import TrialRunner
from validation.input_validator import InputValidator
from player.player_dao import PlayerDAO
from validation.request_validator import RequestValidator
from handlers.handlers import Handlers
from router.router import Router


class Play:

    def __init__(self):
        self.input_validator = InputValidator()
        self.player_loader = PlayerDAO()
        self.game = None
        self.validator = RequestValidator()
        self.handlers = Handlers(self.validator)
        self.router = Router()

    def main(self) -> None:
        display.start()
        game_choice = input("Type 'load' to continue a previous game? ")

        if game_choice.strip().lower() == "load":
            self.game = self.handlers.load_game()
        else:
            self.game = self.handlers.start()

        run = True

        while run:

            raw_command : str = input("What would you like to do next : ")

            if raw_command in ["exit" , "quit"]:
                run = False
            else:
                parsed_command = self.input_validator.validate_command(raw_command)


                if len(parsed_command)  > 0:
                    result = self.router.route(parsed_command, self.handlers, self.game)
                    display.view(result)
                    if result == "trial started":

                        item = " ".join(parsed_command[1:])
                        active = True
                        question = self.game.load_question()
                        display.view(question.get_question())

                        while active:
                            answer = input("what is your answer? ").strip().lower()
                            if answer not in ["exit" , "leave"]:
                                result = self.handlers.run_trial(self.game , item , question , answer  )
                                display.view(result)
                            else:
                                display.view("You have left the trial")
                                active = False
                            if item == result:
                                active = False


                    display.view(self.handlers.check_requirements(self.game))
                else:
                    print("Invalid command")

if __name__ == "__main__":
    play = Play()
    play.main()

