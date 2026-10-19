from question.question import Question
from room.room import Room
from player.player import Player


class Game:
    """Holds game state. It builds nothing and prints nothing."""

    def __init__(self, player: Player, difficulty: int, rooms: dict[str, Room], questions, start_room: str):
        self._player = player
        self._difficulty = difficulty
        self._rooms = rooms
        self._questions = questions          # anything with load_question(room, difficulty, character)
        self._room = rooms[start_room]
        self._player.set_position(start_room)

    def get_room(self) -> Room:
        return self._room

    def get_all_rooms(self) -> dict[str, Room]:
        return self._rooms

    def get_player(self) -> Player:
        return self._player

    def get_difficulty(self) -> int:
        return self._difficulty

    def move_room(self, direction: str) -> str:
        self._room = self._rooms[self._room.get_exits()[direction]]
        self._player.set_position(self._room.get_name())
        return "Moved to " + self._room.get_name()

    def unlock_room(self, name: str) -> None:
        self._rooms[name].set_status(False)

    def collect(self, item: str) -> None:
        """Move an item from the current room into the player's inventory."""
        name = item.strip().lower()
        self._room.remove_item(name)
        self._player.add_item(name)

    def load_question(self) -> Question | None:
        return self._questions.load_question(self._room.get_name(), self._difficulty, self._player.get_name())

    def view(self) -> str:
        items = ", ".join(self._room.get_items()) or "nothing"
        exits = ", ".join(self._room.get_exits().keys())
        return (f"You are in {self._room.get_name()}. {self._room.get_description()}\n"
                f"You see: {items}\n"
                f"Exits: {exits}")

    def snapshot(self) -> dict:
        rooms = {}
        for room in self._rooms.values():
            rooms.update(room.to_dict())

        return {
            "character": self._player.get_name(),
            "charge": self._player.get_score(),
            "difficulty": self._difficulty,
            "items": self._player.get_items(),
            "position": self._room.get_name(),
            "rooms": rooms,
        }




