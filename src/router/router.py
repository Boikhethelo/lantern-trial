from game.game import Game
from requests.requests import Requests


class Router:

    def route(self, commands: list[str] , requests:Requests , game:Game) -> str  :
        match commands[0]:
            case "go": return requests.move(commands[1]  , game)
            case "look" : return game.view()
            case "take" : return requests.take(" ".join(commands[1:]), game)
            case "use"  : return requests.use(" ".join(commands[1:]), game)
            case "charge" : return "TODO"
            case "inventory" : return game.get_player().get_items()
            case "help"  : return "help"
            case "save"  : return requests.save(game)
            case "load" : requests.load_game()

        return ""