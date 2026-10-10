from game.game import Game
from player.player_dao import PlayerDAO
from question.question import Question
from validation.request_validator import RequestValidator
import display.display as display
from persistence import save_load as storage


class Handlers:
    def __init__(self, validator: RequestValidator):
        self.validator = validator
        self.player_loader = PlayerDAO()


    def start(self):

            character_choice = int(input("Select a character : "))
            difficulty = int(input("Select a difficulty : "))
            character = self.validator.get_character(character_choice)
            player = self.player_loader.get_character(character)
            new_game = Game(player, difficulty)
            new_game.load_all_rooms()
            new_game.set_room("Guardian Citadel")
            return new_game

    def save(self,game):
        storage.save_game(game)
        return "Saved!"


    def load_game(self) -> Game:
            load_data = storage.load_game()
            player = self.player_loader.get_character(load_data.get("character"))
            player.set_items(load_data.get("items"))
            player.set_position(load_data.get("position"))
            difficulty = int(load_data.get("difficulty"))
            charge = int(load_data.get("charge"))
            loaded_game = Game(player, difficulty)

            rooms = load_data.get("rooms")
            room_dic = {}

            for room in rooms:
                room_obj = loaded_game.load_room(room, rooms[room])
                room_dic.update({room: room_obj})

            loaded_game.set_all_rooms(room_dic)
            loaded_game.set_room(load_data.get("position"))

            return loaded_game


    def check_requirements(self , game) -> str:

        output = ""
        if self.validator.will_forge_requirements(game.get_player().get_items()):
            game.unlock_room("Will Forge")
            output += " Will Forged has been unlocked"

        if self.validator.central_power_battery_chamber_requirements(game.get_player().get_items()):
            game.unlock_room("Central Power Battery Chamber")
            output += "Central Power Battery Chamber has been unlocked"

        return output

    def move(self, direction: str , game: Game) -> str:


        if self.validator.validate_move(direction , game.get_room().get_exits() , game.get_all_rooms()):

            return game.move_room(direction)

        elif game.get_room().get_name() == "Central Power Battery Chamber":
            display.final()
        else:
            return "Locked"

        return ''

    def run_trial(self, game: Game , chosen_item : str, question: Question  , user_input:str) -> str:



        if user_input  == question.get_answer():
            game.get_player().add_item(chosen_item)
            game.get_room().remove_item(chosen_item)

            return chosen_item
        elif user_input == "hint":
            return question.get_hint()
        else:
            return "Incorrect Answer"





    def take(self, chosen_item: str ,game:Game ):
        game.get_player().use_charge(10)

        if self.validator.inventory_check(game.get_player().get_items(), chosen_item):
            return "you already have " + chosen_item

        if self.validator.is_trial_item(chosen_item, game.get_room().get_items()):
            # question = game.load_question()

            # if question is None:
            #     game.get_player().add_item(chosen_item)
            #     game.get_room().remove_item(chosen_item)
            #
            #     return "Unable to load active question you have been gifted " + chosen_item
            # else:
                return "trial started"

        elif self.validator.check_item(chosen_item, game.get_room().get_items()):
            game.get_player().add_item(chosen_item)
            game.get_room().remove_item(chosen_item)

            return chosen_item + "Has been added to your inventory"

        else:
            return ""


    def use(self , command:str, game:Game) -> str:
        game.get_player().use_charge(10)

        final_trial = {
            "lens of will" : False,
            "lens of hope" : False,
            "lens of resolve" : False

        }

        if command not in final_trial.keys():
            return "used " + command
        else:

            for trial in final_trial.keys():

                order = input(
                    "For the final trial rebuild the lens in the create order by using 'use' command and items collected for the trial rooms ")

                if trial.lower().strip() == order.lower().strip():

                    if trial not in game.get_player().get_items():

                        return "You dont have this item"
                    else:
                        final_trial[trial] = True

                else:
                    return "Incorrect Order"


            return "Final Trial Complete"






















