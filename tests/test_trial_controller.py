import unittest

from tests.helpers import make_game, make_question
from trial.trial_controller import TrialController


def run_trial(game, answers):
    replies = iter(answers)
    shown = []
    controller = TrialController(lambda prompt: next(replies), shown.append)
    result = controller.run(game, "lens of will")
    return result, shown


class TrialControllerTests(unittest.TestCase):

    def test_wrong_answer_then_hint_then_correct_answer_collects_the_item(self):
        game = make_game(make_question(answer="4", hint="Two plus two"))

        result, shown = run_trial(game, ["5", "hint", "4"])

        self.assertIn("Incorrect Answer", shown)
        self.assertIn("Two plus two", shown)
        self.assertIn("Correct", result)
        self.assertTrue(game.get_player().has_item("lens of will"))

    def test_leaving_the_trial_does_not_give_the_item(self):
        game = make_game(make_question())

        result, _ = run_trial(game, ["leave"])

        self.assertEqual(result, "You have left the trial")
        self.assertFalse(game.get_player().has_item("lens of will"))

    def test_item_is_gifted_when_no_question_can_be_loaded(self):
        game = make_game(question=None)

        result, _ = run_trial(game, [])

        self.assertIn("gifted", result)
        self.assertTrue(game.get_player().has_item("lens of will"))


if __name__ == "__main__":
    unittest.main()
