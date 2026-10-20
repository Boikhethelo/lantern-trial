import unittest

from room.room import Room
from rules.rules import Rules


class RulesTests(unittest.TestCase):

    def test_can_enter_only_when_the_room_is_unlocked(self):
        rules = Rules()

        self.assertTrue(rules.can_enter(Room("A", "d", {}, [], False)))
        self.assertFalse(rules.can_enter(Room("B", "d", {}, [], True)))

    def test_a_room_unlocks_only_when_every_requirement_is_owned(self):
        rooms = {
            "Chamber": Room("Chamber", "d", {}, [], True, ["lens of will", "lens of hope"]),
            "Open": Room("Open", "d", {}, [], False),
        }
        rules = Rules()

        self.assertEqual(rules.rooms_to_unlock(rooms, ["lens of will"]), [])
        self.assertEqual(rules.rooms_to_unlock(rooms, ["Lens of Will", "lens of hope"]), ["Chamber"])


if __name__ == "__main__":
    unittest.main()
