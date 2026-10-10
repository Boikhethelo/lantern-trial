from database.database import Database
from question.question import Question


class QuestionDAO:
    def __init__(self):
        self.sql_database = Database("resources/questions.db")

    def load_question(self, room_name:str , difficulty: int , character:str) -> Question | None:

        question_data : dict = self.sql_database.get_question(room_name,difficulty, character)
        if not question_data:
            return None

        q_id : int = question_data.get("id")
        question : str = question_data.get("question")
        answer : str = question_data.get("answer")
        hint : str = question_data.get("hint")

        return Question(q_id, room_name, difficulty, question, answer, hint)






