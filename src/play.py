import display.display as display
from game.game import Game
from game.game_factory import GameFactory
from handlers.handlers import Handlers
from menu.start_menu import StartMenu
from persistence.save_load import SaveStore
from player.player_dao import PlayerDAO
from question.question_dao import QuestionDAO
from room.room_dao import RoomDAO
from router.router import Router
from rules.rules import Rules
from trial.trial_controller import TrialController
from validation.input_validator import InputValidator


class Play:
    def __init__(self, menu, router, handlers, input_validator, ask=input, show=display.view):
        self._menu = menu
        self._router = router
        self._handlers = handlers
        self._input_validator = input_validator
        self._ask = ask
        self._show = show
        self._game = None

    def main(self) -> None:
        display.show_title()
        display.opening_cinematic()
        self._game = self._menu.run()


        while True:
            charge = self._game.get_charge()

            if charge < 0:
                self._show("Game over your ring has run out of charge")
                break

            unlocked = self._handlers.unlock_rooms(self._game)
            if unlocked:
                self._show(unlocked)

            raw_command = self._ask("What would you like to do next : ").strip().lower()
            self._game.get_player().use_charge(1)
            if raw_command in ("exit", "quit"):
                break

            parts = self._input_validator.validate_command(raw_command)
            if not parts:
                self._show("Invalid command")
                continue

            result = self._router.route(parts, self._game)

            if isinstance(result, Game):
                self._game = result
                result = "Game loaded"

            self._show(result)

            if(result == "game over"):
                break

            elif(result == "Final Trial Complete"):
                display.won()
                break


def build() -> Play:
    """Composition root: the one place that creates and connects the pieces."""
    ask, show = input, display.view
    factory = GameFactory(PlayerDAO(), RoomDAO(), QuestionDAO())
    store = SaveStore()
    handlers = Handlers(Rules(), TrialController(ask, show), store, factory, ask)

    return Play(StartMenu(factory, store, ask, show), Router(handlers), handlers, InputValidator(), ask, show)


if __name__ == "__main__":
    build().main()