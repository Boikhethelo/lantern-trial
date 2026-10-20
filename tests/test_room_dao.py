import unittest

from room.room_dao import RoomDAO


class RoomDAOTests(unittest.TestCase):

    def setUp(self):
        self.data = RoomDAO().load_data()

    def test_every_room_has_the_keys_the_game_reads(self):
        for name, room in self.data.items():
            for key in ("description", "exits", "items", "locked"):
                self.assertIn(key, room, f"{name} is missing '{key}'")

    def test_every_exit_leads_to_a_room_that_exists(self):
        for name, room in self.data.items():
            for direction, target in room["exits"].items():
                self.assertIn(target, self.data, f"{name} -> {direction} -> {target}")


if __name__ == "__main__":
    unittest.main()
