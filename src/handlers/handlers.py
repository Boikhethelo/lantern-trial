from game.game import Game


class Handlers:
    def __init__(self, rules, trials, store, factory, ask):
        self._rules = rules
        self._trials = trials
        self._store = store
        self._factory = factory
        self._ask = ask

    def move(self, direction: str, game: Game) -> str:
        target = game.get_room().get_exits().get(direction)
        if target is None:
            return "Nothing in that direction"
        if not self._rules.can_enter(game.get_all_rooms()[target]):
            return f"{target} is locked"
        return game.move_room(direction)

    def take(self, item: str, game: Game) -> str:
        game.get_player().use_charge(10)
        name = item.strip().lower()

        if game.get_player().has_item(name):
            return f"you already have {name}"
        if not game.get_room().has_item(name):
            return f"There is no {name} here"
        if game.get_room().is_trial_item(name):
            return self._trials.run(game, name)

        game.collect(name)
        return f"{name} has been added to your inventory"

    def unlock_rooms(self, game: Game) -> str:
        names = self._rules.rooms_to_unlock(game.get_all_rooms(), game.get_player().get_items())
        for name in names:
            game.unlock_room(name)
        return "\n".join(f"{name} has been unlocked" for name in names)

    def save(self, game: Game) -> str:
        self._store.save(game.snapshot())
        return "Saved!"

    def load(self) -> Game | str:
        data = self._store.load()
        if data is None:
            return "No saved game found"
        return self._factory.from_save(data)

    def use(self, command: str, game: Game) -> str:
        # Unchanged from your version apart from using the injected ask function.
        game.get_player().use_charge(5)

        final_trial = {"lens of will": False, "lens of hope": False, "lens of resolve": False}

        if command not in final_trial:
            return "used " + command

        for trial in final_trial:
            order = self._ask("For the final trial rebuild the lens in the create order by using 'use' command "
                              "and items collected for the trial rooms ")
            if trial == order.lower().strip():
                if not game.get_player().has_item(trial):
                    return "You dont have this item"
                final_trial[trial] = True
            else:
                return "Incorrect Order"

        return "Final Trial Complete"





















