import contextlib
import io
import unittest

import display.display as display


class DisplayTests(unittest.TestCase):

    def test_view_prints_the_text(self):
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            display.view("Moved to Corps Armory")

        self.assertEqual(output.getvalue().strip(), "Moved to Corps Armory")


if __name__ == "__main__":
    unittest.main()


class ScreenTests(unittest.TestCase):
    """The story screens, with delays switched off."""

    def setUp(self):
        display.FAST = True

    def tearDown(self):
        display.FAST = False

    def _output_of(self, screen):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            screen()
        return output.getvalue()

    def test_help_lists_the_commands_with_their_arguments(self):
        text = self._output_of(display.view_help)

        self.assertIn("go [direction]", text)      # would vanish if [..] were read as markup
        self.assertIn("take [item]", text)
        self.assertIn("hint", text)

    def test_winning_screen_shows_the_oath_and_the_restored_battery(self):
        text = self._output_of(display.won)

        self.assertIn(display.OATH[0], text)
        self.assertIn("CENTRAL BATTERY: RESTORED", text)

    def test_losing_screen_says_game_over(self):
        self.assertIn("GAME OVER", self._output_of(display.lost))