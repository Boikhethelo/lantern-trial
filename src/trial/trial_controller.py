class TrialController:
    """Runs one question trial. Input and output are passed in, so it can be tested."""

    def __init__(self, ask, show):
        self._ask = ask
        self._show = show

    def run(self, game, item: str) -> str:
        question = game.load_question()

        if question is None:
            game.collect(item)
            return f"No question could be loaded, so {item} was gifted to you"

        self._show(question.get_question())

        while True:
            answer = self._ask("what is your answer? ").strip().lower()

            if answer in ("exit", "leave"):
                return "You have left the trial"
            if answer == "hint":
                self._show(question.get_hint() or "No hint for your Lantern on this one")
            elif answer == question.get_answer().strip().lower():
                game.collect(item)
                return f"Correct! {item} has been added to your inventory"
            else:
                self._show("Incorrect Answer")