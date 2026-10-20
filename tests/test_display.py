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
