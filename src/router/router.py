
class Router:
    def __init__(self, handlers):
        self._commands = {
            "go":   lambda args, game: handlers.move(args[0], game),
            "look": lambda args, game: game.view(),
            "take": lambda args, game: handlers.take(" ".join(args), game),
            "use":  lambda args, game: handlers.use(" ".join(args), game),
            "save": lambda args, game: handlers.save(game),
            "load": lambda args, game: handlers.load(),
            # inventory, charge, help follow the same pattern
        }

    def route(self, parts, game):
        handler = self._commands.get(parts[0])
        return handler(parts[1:], game) if handler else ""