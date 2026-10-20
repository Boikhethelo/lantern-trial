import unittest

from player.player_dao import PlayerDAO


class PlayerDAOTests(unittest.TestCase):

    def test_names_lists_every_character_in_the_json(self):
        names = PlayerDAO().names()

        self.assertIn("Hal Jordan", names)
        self.assertGreaterEqual(len(names), 4)

    def test_get_character_builds_a_player_from_the_json(self):
        player = PlayerDAO().get_character("Hal Jordan")

        self.assertEqual(player.get_name(), "Hal Jordan")
        self.assertEqual(player.get_strength(), "Fearless")


if __name__ == "__main__":
    unittest.main()
