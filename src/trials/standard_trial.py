class TrialRunner:
    def __init__(self , hint: str , question: str , answer: str , hint_character: str , current_character: str):
        self._passed = False
        self._hint = hint
        self._question = question
        self._answer = answer
        self._hint_character = hint_character
        self._current_character = current_character

    def standard_trial(self , user_input):

        if user_input.lower().strip() == "hint":
            return self._get_hint()

        if user_input.lower().strip() in ["exit" , "leave"]:
            return "exit"

        if user_input == self._answer.lower().strip():
            self._passed = True
            return "Correct"
        else:
            return "Incorrect"

    def _get_hint(self) -> str:
        if self._hint_character == self._current_character:
            return self._hint
        else:
            return "Unavailable"

    def get_question(self):
        return self._question













