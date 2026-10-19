class GameFactory:
    START_ROOM = "Guardian Citadel"

    def __init__(self, player_dao, room_dao, question_source): ...

    def character_names(self):
        return self._players.names()

    def new_game(self, character_choice, difficulty):
        names = self.character_names()
        name = names[character_choice - 1] if 1 <= character_choice <= len(names) else names[0]
        rooms = self._build_rooms(self._rooms.load_data())
        return Game(self._players.get_character(name), difficulty, rooms, self._questions, self.START_ROOM)

    def from_save(self, data):
        player = self._players.get_character(data["character"])
        player.set_items(list(data["items"]))
        player.set_score(int(data["charge"]))
        rooms = self._build_rooms(data["rooms"])
        return Game(player, int(data["difficulty"]), rooms, self._questions, data["position"])

    @staticmethod
    def _build_rooms(room_data):
        return {name: Room(name, d["description"], d["exits"], d["items"], d["locked"],
                           d.get("requires"), d.get("trial_items"))
                for name, d in room_data.items()}