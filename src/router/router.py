from game.game import Game
from handlers.handlers import Handlers


class Router:

    def route(self, commands: list[str] , handlers:Handlers , game:Game) -> str  :
        match commands[0]:
            case "go": return handlers.move(commands[1], game)
            case "look" : return game.view()
            case "take" : return handlers.take(" ".join(commands[1:]), game)
            case "use"  : return handlers.use(" ".join(commands[1:]), game)
            case "charge" : return "TODO"
            case "inventory" : return game.get_player().get_items()
            case "help"  : return "help"
            case "save"  : return handlers.save(game)
            case "load" : handlers.load_game()

        return ""