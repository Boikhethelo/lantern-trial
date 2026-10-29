
class FinalTrial:
    """Validates and applies the rules for the final lens trial."""

    ROOM_NAME = "Central Power Battery Chamber"

    LENS_ORDER = (
        "lens of hope",
        "lens of will",
        "lens of resolve",
    )

    def use_lens(self, game, lens: str) -> str:
        lens = lens.strip().lower()
        player = game.get_player()

        # Rule 1: The player must be in the correct room.
        if game.get_room().get_name() != self.ROOM_NAME:
            return "You must be in the Central Power Battery Chamber."

        # Rule 2: Only the three trial lenses are accepted.
        if lens not in self.LENS_ORDER:
            return f"{lens} is not part of the final trial."

        # Rule 3: The player must own the lens.
        if not player.has_item(lens):
            return f"You do not have {lens}."

        # Rule 4: Do not allow the same step twice.
        progress = game.get_final_trial_progress()

        if lens in progress:
            return f"{lens} has already been accepted."

        # Rule 5: The next lens must be used in order.
        expected_index = len(progress)
        expected_lens = self.LENS_ORDER[expected_index]

        if lens != expected_lens:
            return f"Incorrect order. Use {expected_lens} next."

        # Rule 6: Record a valid step.
        game.record_final_trial_lens(lens)

        if game.is_final_trial_complete():
            game.mark_won()
            return "Final Trial Complete"

        next_lens = self.LENS_ORDER[len(progress)]
        return f"{lens} accepted. Next: {next_lens}."
