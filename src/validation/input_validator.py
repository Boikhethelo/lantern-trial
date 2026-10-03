class InputValidator:
    def __init__(self):
        self._valid_commands = ["go" , "look" , "take" , "use" , "inventory" , "charge" , "help" , "save" , "load" , "quit" , "exit"]
        self._valid_directions = ["north" , "south" , "west" , "east"]
     



    def validate_command(self, command: str) -> list[str] :
        command_list = command.split()
        cleaned = [word.strip().lower() for word in command_list]

        if self._validate(cleaned):
            return cleaned
        else:
            return []

    def _validate(self, command : list[str]) -> bool:
        if command[0] not in self._valid_commands:
            return False

        if len(command) > 1 and command[0] in ["go" , "move"]:
            if command[1] not in self._valid_directions:
                return False

        return True








