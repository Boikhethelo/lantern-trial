class Play:
    def __init__(self, menu, router, handlers, input_validator, ask=input, show=display.view): ...

    def main(self):
        display.start()
        self._game = self._menu.run()
        while True:
            unlocked = self._handlers.unlock_rooms(self._game)
            if unlocked:
                self._show(unlocked)

            raw = self._ask("What would you like to do next : ").strip().lower()
            if raw in ("exit", "quit"):
                break

            parts = self._input_validator.validate_command(raw)
            if not parts:
                self._show("Invalid command")
                continue

            result = self._router.route(parts, self._game)
            if isinstance(result, Game):      # the load command returns a whole game
                self._game = result
                result = "Game loaded"
            self._show(result)

def build():
    ask, show = input, display.view
    factory = GameFactory(PlayerDAO(), RoomDAO(), QuestionDAO())
    store = SaveStore()
    handlers = Handlers(Rules(), TrialController(ask, show), store, factory, ask)
    return Play(StartMenu(factory, store, ask, show), Router(handlers), handlers,
                InputValidator(), ask, show)

if __name__ == "__main__":
    build().main()
