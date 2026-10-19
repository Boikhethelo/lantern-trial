class StartMenu:
    def __init__(self, factory, store, ask, show):
        self._factory = factory
        self._store = store
        self._ask = ask
        self._show = show

    def run(self):
        if self._ask("Type 'load' to continue a previous game, or press Enter to start: ").strip().lower() == "load":
            data = self._store.load()
            if data:
                return self._factory.from_save(data)
            self._show("No saved game found, starting a new one.")
        return self._new_game()

    def _new_game(self):
        names = self._factory.character_names()
        for number, name in enumerate(names, 1):
            self._show(f"{number}. {name}")

        character = self._ask_number("Select a character : ", 1, len(names))
        difficulty = self._ask_number("Select a difficulty (1-3) : ", 1, 3)
        return self._factory.new_game(character, difficulty)

    def _ask_number(self, prompt: str, low: int, high: int) -> int:
        while True:
            answer = self._ask(prompt).strip()
            if answer.isdigit() and low <= int(answer) <= high:
                return int(answer)
            self._show(f"Please enter a number from {low} to {high}.")