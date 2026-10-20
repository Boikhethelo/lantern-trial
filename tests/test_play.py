import unittest

from play import Play
from tests.helpers import make_game


class FakeMenu:
    def __init__(self, game):
        self.game = game

    def run(self):
        return self.game


class FakeHandlers:
    def unlock_rooms(self, game):
        return ""


class FakeRouter:
    def __init__(self, load_returns=None):
        self.games_seen = []
        self.load_returns = load_returns

    def route(self, parts, game):
        self.games_seen.append(game)
        return self.load_returns if parts[0] == "load" else "routed " + parts[0]


class FakeValidator:
    def validate_command(self, raw):
        return raw.split()


def make_play(game, router, commands):
    replies, shown = iter(commands), []
    play = Play(FakeMenu(game), router, FakeHandlers(), FakeValidator(),
                ask=lambda prompt: next(replies), show=shown.append)
    return play, shown


class PlayTests(unittest.TestCase):

    def test_commands_are_routed_and_quit_ends_the_loop(self):
        play, shown = make_play(make_game(), FakeRouter(), ["look", "quit"])

        play.main()

        self.assertEqual(shown, ["routed look"])

    def test_a_loaded_game_replaces_the_current_one(self):
        original, loaded = make_game(), make_game()
        router = FakeRouter(load_returns=loaded)
        play, shown = make_play(original, router, ["load", "look", "quit"])

        play.main()

        self.assertIs(router.games_seen[0], original)
        self.assertIs(router.games_seen[1], loaded)
        self.assertEqual(shown[0], "Game loaded")


if __name__ == "__main__":
    unittest.main()
