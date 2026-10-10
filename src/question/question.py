class Question:
    def __init__(self , question_id:int , room:str, difficulty:int, question:str, answer:str, hint:str, character:str):
        self._id = question_id
        self._room = room
        self._difficulty = difficulty
        self._question = question
        self._answer = answer
        self._hint = hint
        self._character = character

    def get_id(self) -> int:
        return self._id
    def get_room(self) -> str:
        return self._room
    def get_difficulty(self) -> int:
        return self._difficulty
    def get_question(self) -> str:
        return self._question
    def get_answer(self) -> str:
        return self._answer
    def get_hint(self) -> str:
        return self._hint
    def get_character(self) -> str:
        return self._character

