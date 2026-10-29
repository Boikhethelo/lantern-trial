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
                ask=lambda prompt: next(replies), show=shown.append, intro=lambda: None,
                on_win=lambda: shown.append("WON"), on_lose=lambda: shown.append("LOST"))
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

class PlayEndingTests(unittest.TestCase):

    def test_game_over_when_the_ring_runs_out_of_charge(self):
        game = make_game()
        game.get_player().use_charge(101)          # 100 - 101 = -1
        play, shown = make_play(game, FakeRouter(), ["look"])

        play.main()

        self.assertIn("LOST", shown)


class PlayWinTests(unittest.TestCase):

    def test_completing_the_final_trial_ends_the_game_with_the_win_screen(self):
        class WinningRouter(FakeRouter):
            def route(self, parts, game):
                return "Final Trial Complete"

        play, shown = make_play(make_game(), WinningRouter(), ["use lens of will"])

        play.main()

        self.assertEqual(shown, ["Final Trial Complete", "WON"])


if __name__ == "__main__":
    unittest.main()