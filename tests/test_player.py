import unittest

from tests.helpers import make_player


class PlayerTests(unittest.TestCase):

    def test_has_item_ignores_case_and_spaces(self):
        player = make_player()
        player.add_item("Lens of Will")

        self.assertTrue(player.has_item("  lens of will"))
        self.assertFalse(player.has_item("lens of hope"))

    def test_use_charge_reduces_charge(self):
        player = make_player()
        start = player.get_charge()

        player.use_charge(10)

        self.assertEqual(player.get_charge(), start - 10)


if __name__ == "__main__":
    unittest.main()
