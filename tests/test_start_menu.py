import unittest

from menu.start_menu import StartMenu


class FakeFactory:
    def __init__(self):
        self.new_game_args = None

    def character_names(self):
        return ["A", "B", "C", "D"]

    def new_game(self, character, difficulty):
        self.new_game_args = (character, difficulty)
        return "NEW GAME"


class FakeStore:
    def load(self):
        return None


def run_menu(answers):
    replies, shown, factory = iter(answers), [], FakeFactory()
    menu = StartMenu(factory, FakeStore(), lambda prompt: next(replies), shown.append)
    return menu.run(), shown, factory


class StartMenuTests(unittest.TestCase):

    def test_bad_numbers_are_asked_again_until_valid(self):
        game, shown, factory = run_menu(["", "abc", "9", "2", "x", "3"])

        self.assertEqual(game, "NEW GAME")
        self.assertEqual(factory.new_game_args, (2, 3))
        self.assertEqual(sum("Please enter a number" in line for line in shown), 3)

    def test_load_with_no_save_falls_back_to_a_new_game(self):
        game, shown, _ = run_menu(["load", "1", "1"])

        self.assertEqual(game, "NEW GAME")
        self.assertIn("No saved game found, starting a new one.", shown)


if __name__ == "__main__":
    unittest.main()
