from game.game import Game
from room.room import Room


class GameFactory:
    START_ROOM = "Guardian Citadel"

    def __init__(self, player_dao, room_dao, question_source):
        self._players = player_dao
        self._rooms = room_dao
        self._questions = question_source

    def character_names(self) -> list[str]:
        return self._players.names()

    def new_game(self, character_choice: int, difficulty: int) -> Game:
        names = self.character_names()
        name = names[character_choice - 1] if 1 <= character_choice <= len(names) else names[0]
        player = self._players.get_character(name)
        rooms = self._build_rooms(self._rooms.load_data())
        return Game(player, difficulty, rooms, self._questions, self.START_ROOM)

    def from_save(self, data: dict) -> Game:
        player = self._players.get_character(data["character"])
        player.set_items(list(data["items"]))
        player.set_charge(int(data["charge"]))
        rooms = self._build_rooms(data["rooms"])
        return Game(player, int(data["difficulty"]), rooms, self._questions, data["position"] ,
                    final_trial_progress=data.get("final_trial_progress", []) , won=data.get("won", False),)

    @staticmethod
    def _build_rooms(room_data: dict) -> dict[str, Room]:
        return {
            name: Room(name, d["description"], d["exits"], d["items"], d["locked"],
                       d.get("requires"), d.get("trial_items"))
            for name, d in room_data.items()
        }