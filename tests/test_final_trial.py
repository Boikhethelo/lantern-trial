
import unittest

from trial.final_trial import FinalTrial
from tests.helpers import make_game


class FinalTrialTests(unittest.TestCase):

    def setUp(self):
        self.game = make_game()
        self.trial = FinalTrial()

        # Move the test player to the final chamber.
        chamber = self.game.get_all_rooms()[
            "Central Power Battery Chamber"
        ]
        chamber.set_status(False)

        # Use the game's existing movement API to enter the chamber.
        self.game.get_room().get_exits()

        # For an isolated rule test, set the player's position and
        # current room consistently using the helper below instead.
        self.game._room = chamber
        self.game.get_player().set_position(
            "Central Power Battery Chamber"
        )

        self.game.get_player().set_items([
            "lens of hope",
            "lens of will",
            "lens of resolve",
        ])

    def test_player_must_be_in_final_chamber(self):
        self.game._room = self.game.get_all_rooms()["Start"]
        self.game.get_player().set_position("Start")

        result = self.trial.use_lens(
            self.game, "lens of hope"
        )

        self.assertIn("must be in", result)
        self.assertEqual(
            self.game.get_final_trial_progress(), []
        )

    def test_lenses_must_be_used_in_order(self):
        result = self.trial.use_lens(
            self.game, "lens of will"
        )

        self.assertIn("Incorrect order", result)
        self.assertEqual(
            self.game.get_final_trial_progress(), []
        )

    def test_correct_first_lens_advances_progress(self):
        result = self.trial.use_lens(
            self.game, "lens of hope"
        )

        self.assertIn("accepted", result)
        self.assertEqual(
            self.game.get_final_trial_progress(),
            ["lens of hope"],
        )

    def test_trial_completes_after_all_lenses(self):
        for lens in FinalTrial.LENS_ORDER:
            result = self.trial.use_lens(self.game, lens)

        self.assertEqual(result, "Final Trial Complete")
        self.assertTrue(self.game.has_won())


if __name__ == "__main__":
    unittest.main()
