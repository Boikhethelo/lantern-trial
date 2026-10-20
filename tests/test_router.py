import unittest

from router.router import Router


class FakeHandlers:
    def __init__(self):
        self.moved = None

    def move(self, direction, game):
        self.moved = (direction, game)
        return "moved"


class RouterTests(unittest.TestCase):

    def test_go_is_sent_to_move_with_the_direction(self):
        handlers = FakeHandlers()

        result = Router(handlers).route(["go", "east"], "GAME")

        self.assertEqual(result, "moved")
        self.assertEqual(handlers.moved, ("east", "GAME"))

    def test_an_unknown_command_returns_an_empty_string(self):
        self.assertEqual(Router(FakeHandlers()).route(["dance"], "GAME"), "")


if __name__ == "__main__":
    unittest.main()
