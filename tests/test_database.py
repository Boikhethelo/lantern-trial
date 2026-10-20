import contextlib
import io
import sqlite3
import tempfile
import unittest
from pathlib import Path

from database.database import Database


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = str(Path(self.folder.name) / "questions.db")
        self.db = Database(self.path)
        with contextlib.redirect_stdout(io.StringIO()):      # read_schema prints a message
            self.db.read_schema()
        self._clear_table()

    def tearDown(self):
        self.folder.cleanup()

    def _clear_table(self):
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE FROM questions")
        conn.commit()
        conn.close()

    def test_character_only_hint_is_hidden_from_other_characters(self):
        self.db.insert_question("Void of Fear", 1, "Q?", "a", "secret hint", "Kilowog")

        for_kilowog = self.db.get_question("Void of Fear", 1, "Kilowog")
        for_hal = self.db.get_question("Void of Fear", 1, "Hal Jordan")

        self.assertEqual(for_kilowog["hint"], "secret hint")
        self.assertIsNone(for_hal["hint"])

    def test_falls_back_to_the_closest_difficulty(self):
        self.db.insert_question("Will Forge", 3, "Hard one?", "a", None, None)

        row = self.db.get_question("Will Forge", 1, "Hal Jordan")

        self.assertEqual(row["question"], "Hard one?")


if __name__ == "__main__":
    unittest.main()
