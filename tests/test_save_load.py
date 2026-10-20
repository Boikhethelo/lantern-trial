import json
import tempfile
import unittest
from pathlib import Path

from persistence.save_load import SaveStore


class SaveStoreTests(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = Path(self.folder.name) / "saves" / "save_file.json"
        self.store = SaveStore(self.path)

    def tearDown(self):
        self.folder.cleanup()

    def test_what_is_saved_is_what_is_loaded(self):
        data = {"character": "Hal Jordan", "charge": 80, "items": ["lens of hope"]}

        self.store.save(data)

        self.assertEqual(self.store.load(), data)

    def test_missing_file_or_empty_save_loads_as_none(self):
        self.assertIsNone(self.store.load())

        self.path.parent.mkdir(parents=True)
        self.path.write_text(json.dumps({"character": "", "charge": 0}))

        self.assertIsNone(self.store.load())


if __name__ == "__main__":
    unittest.main()
