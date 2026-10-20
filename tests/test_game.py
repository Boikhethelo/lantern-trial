import unittest

from tests.helpers import make_game


class GameTests(unittest.TestCase):

    def test_move_room_changes_room_and_player_position(self):
        game = make_game()

        message = game.move_room("east")

        self.assertEqual(message, "Moved to Vault")
        self.assertEqual(game.get_room().get_name(), "Vault")
        self.assertEqual(game.get_player().get_position(), "Vault")

    def test_collect_moves_an_item_from_the_room_to_the_player(self):
        game = make_game()

        game.collect("Spare Battery")

        self.assertTrue(game.get_player().has_item("spare battery"))
        self.assertFalse(game.get_room().has_item("spare battery"))


if __name__ == "__main__":
    unittest.main()
