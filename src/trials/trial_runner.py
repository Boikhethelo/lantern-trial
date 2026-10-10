class TrialRunner:

    def standard_trial(self , user_input , hint):



        if user_input.lower().strip() in ["exit" , "leave"]:
            return "exit"

        if user_input.lower().strip() == self._answer.lower().strip():
            self._passed = True
            return "correct"
        else:
            return "incorrect"

    def _get_hint(self) -> str:
        if not self._hint:
            return self._hint
        else:
            return "No hint for this character available"


    def get_question(self):
        return self._question













