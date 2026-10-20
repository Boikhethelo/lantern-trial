import unittest

from game.game_factory import GameFactory
from player.player import Player
from tests.helpers import FakeQuestions


class FakePlayers:
    def names(self):
        return ["Hal Jordan", "John Stewart"]

    def get_character(self, name):
        return Player(name, "2814", "strong", "weak")


class FakeRooms:
    def load_data(self):
        return {
            "Guardian Citadel": {"description": "Start", "exits": {"east": "Armory"},
                                 "items": [], "locked": False},
            "Armory": {"description": "Guns", "exits": {"west": "Guardian Citadel"},
                       "items": ["Spare Battery"], "locked": False},
        }


def make_factory():
    return GameFactory(FakePlayers(), FakeRooms(), FakeQuestions())


class GameFactoryTests(unittest.TestCase):

    def test_new_game_uses_the_chosen_character_and_starts_in_the_citadel(self):
        game = make_factory().new_game(2, 1)

        self.assertEqual(game.get_player().get_name(), "John Stewart")
        self.assertEqual(game.get_room().get_name(), "Guardian Citadel")

    def test_a_saved_game_restores_exactly_what_was_saved(self):
        factory = make_factory()
        game = factory.new_game(1, 2)
        game.move_room("east")
        game.collect("spare battery")
        game.get_player().use_charge(30)

        restored = factory.from_save(game.snapshot())

        self.assertEqual(restored.get_room().get_name(), "Armory")
        self.assertEqual(restored.get_player().get_items(), ["spare battery"])
        self.assertEqual(restored.get_player().get_score(), game.get_player().get_score())
        self.assertEqual(restored.get_difficulty(), 2)


if __name__ == "__main__":
    unittest.main()
