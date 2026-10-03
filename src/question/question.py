class Question:
    def __init__(self , question_id:int , room:str, difficulty:int, question:str, answer:str, hint:str, character:str):
        self._id = question_id
        self._room = room
        self._difficulty = difficulty
        self._question = question
        self._answer = answer
        self._hint = hint
        self._character = character

    def get_id(self):
        return self._id
    def get_room(self):
        return self._room
    def get_difficulty(self):
        return self._difficulty
    def get_question(self):
        return self._question
    def get_answer(self):
        return self._answer
    def get_hint(self):
        return self._hint
    def get_character(self):
        return self._character

