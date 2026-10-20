import unittest

from room.room import Room


class RoomTests(unittest.TestCase):

    def test_items_are_lowercased_and_found_ignoring_case(self):
        room = Room("Armory", "desc", {}, ["Lens of Hope"], False)

        self.assertEqual(room.get_items(), ["lens of hope"])
        self.assertTrue(room.has_item("  LENS of hope "))

    def test_trial_item_stops_being_a_trial_item_once_taken(self):
        room = Room("Garden", "desc", {}, ["Lens of Hope"], False, None, ["lens of hope"])
        self.assertTrue(room.is_trial_item("lens of hope"))

        room.remove_item("Lens of Hope")

        self.assertFalse(room.is_trial_item("lens of hope"))


if __name__ == "__main__":
    unittest.main()
