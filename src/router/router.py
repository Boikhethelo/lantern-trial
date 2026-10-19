
class Router:
    """Maps a command word to a function. To add a command, add one entry."""

    def __init__(self, handlers):
        self._commands = {
            "go":        lambda args, game: handlers.move(args[0], game),
            "look":      lambda args, game: game.view(),
            "take":      lambda args, game: handlers.take(" ".join(args), game),
            "use":       lambda args, game: handlers.use(" ".join(args), game),
            "inventory": lambda args, game: ", ".join(game.get_player().get_items()) or "nothing",
            "charge":    lambda args, game: f"Charge: {game.get_player().get_score()}",
            "help":      lambda args, game: "Commands: " + ", ".join(self._commands) + ", quit",
            "save":      lambda args, game: handlers.save(game),
            "load":      lambda args, game: handlers.load(),
        }

    def route(self, parts: list[str], game):
        handler = self._commands.get(parts[0])
        return handler(parts[1:], game) if handler else ""