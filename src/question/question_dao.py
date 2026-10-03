from database.database import Database
from question.question import Question


class QuestionDAO:
    def __int__(self):
        self.sql_database = Database("questions.db")

    def load_question(self, room_name:str , difficulty: int) -> Question:
        question_data = self.sql_database.get_question(room_name,difficulty)

        q_id = question_data.get("id")
        question = question_data.get("question")
        answer = question_data.get("answer")
        hint = question_data.get("hint")
        character = question_data.get("character")

        return Question(q_id, room_name, difficulty, question, answer, hint, character)






