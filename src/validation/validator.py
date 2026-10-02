class Validator:
    def __init__(self):
        self.valid_commands = ["go" , "look" , "take" , "use" , "inventory" , "charge" , "help" , "save" , "load" , "quit" , "exit"]
        self.valid_directions = ["north" , "south" , "west" , "east"]
        self.command = []


    def validate_command(self, command: str) -> str :

        command_list = command.split()
        self._clean(command_list)

        if self._validate(self.command):

            if len(self.command) is 1:
                return self.command[0]
            else:
                return self.command[1]
        else:
            return "Invalid Command!"

    def _clean(self,command_list: list[str]):
        for word in command_list:
            self.command.append(word.strip().lower())

    def _validate(self, command : list[str]) -> bool:
        if command[0] not in self.valid_commands:
            return False

        if len(command) > 1 :
            if command[1] not in self.valid_directions:
                return False

        return True






