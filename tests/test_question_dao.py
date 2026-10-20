import unittest

from question.question_dao import QuestionDAO


class FakeDatabase:
    def __init__(self, row):
        self.row = row

    def get_question(self, room, difficulty, character):
        return self.row


def dao_with(row):
    dao = QuestionDAO.__new__(QuestionDAO)     # skip __init__ so no real database is opened
    dao.sql_database = FakeDatabase(row)
    return dao


class QuestionDAOTests(unittest.TestCase):

    def test_builds_a_question_from_a_database_row(self):
        row = {"id": 3, "question": "Color of hope?", "answer": "blue", "hint": "Sky"}

        question = dao_with(row).load_question("Garden of Mogo", 1, "Hal Jordan")

        self.assertEqual(question.get_answer(), "blue")
        self.assertEqual(question.get_room(), "Garden of Mogo")

    def test_returns_none_when_the_database_has_no_row(self):
        self.assertIsNone(dao_with(None).load_question("Hall of Lanterns", 1, "Hal Jordan"))


if __name__ == "__main__":
    unittest.main()
