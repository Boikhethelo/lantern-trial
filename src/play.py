import display.display
from validation.command_validator import CommandValidator
from player.player_dao import PlayerDAO
from room.room_dao import RoomDAO
from game.game import Game

class Play:
    def __int__(self):
        display.start()
        self.validator = CommandValidator
        self.player_loader = PlayerDAO
        self.room_loader =RoomDAO

    def main(self) -> None:
        run = True

        character = input("Type who you would like to play as: ")

        while not self.validator.validate_character(character):
            character = input("Type who you would like to play as: ")

        player = self.player_loader.get_character(character)
        room = self.room_loader.load_room("Guardian Citadel")

        self.game = Game(player,room)

        while(run):
            raw_command = input("What would you like to do next : ")
            parsed_command = self.validator.validate_command(raw_command)

            if not "invalid" in parsed_command.lower():
                self.route(parsed_command)
            else:
                print("Enter a valid command")



    def route(self, command):
        match command:
            case "north" : self.game.move_room("north")
            case "south" : self.game.move_room("south")





















