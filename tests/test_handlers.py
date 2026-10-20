import unittest

from handlers.handlers import Handlers
from rules.rules import Rules
from tests.helpers import make_game


class FakeTrials:
    def __init__(self):
        self.ran_for = None

    def run(self, game, item):
        self.ran_for = item
        return "trial ran"


def make_handlers(trials=None):
    return Handlers(Rules(), trials or FakeTrials(), store=None, factory=None, ask=lambda prompt: "")


class HandlersTests(unittest.TestCase):

    def test_moving_into_a_locked_room_is_refused(self):
        game = make_game()

        message = make_handlers().move("east", game)

        self.assertEqual(message, "Vault is locked")
        self.assertEqual(game.get_room().get_name(), "Start")

    def test_taking_a_trial_item_hands_over_to_the_trial_controller(self):
        game, trials = make_game(), FakeTrials()

        message = make_handlers(trials).take("Lens of Will", game)

        self.assertEqual(message, "trial ran")
        self.assertEqual(trials.ran_for, "lens of will")
        self.assertFalse(game.get_player().has_item("lens of will"))


if __name__ == "__main__":
    unittest.main()
