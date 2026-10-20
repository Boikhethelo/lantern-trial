import unittest

from question.question import Question


class QuestionTests(unittest.TestCase):

    def test_getters_return_what_was_passed_in(self):
        question = Question(7, "Will Forge", 2, "Color of will?", "green", "Look at your ring")

        self.assertEqual(question.get_id(), 7)
        self.assertEqual(question.get_question(), "Color of will?")
        self.assertEqual(question.get_answer(), "green")
        self.assertEqual(question.get_hint(), "Look at your ring")


if __name__ == "__main__":
    unittest.main()
