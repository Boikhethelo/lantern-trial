from room.room import Room


class Rules:
    """Game rules, driven by the data in game_data.json."""

    def can_enter(self, room: Room) -> bool:
        return not room.get_status()

    def rooms_to_unlock(self, rooms: dict[str, Room], items: list[str]) -> list[str]:
        owned = [item.strip().lower() for item in items]
        return [
            name for name, room in rooms.items()
            if room.get_status()
            and room.get_requires()
            and all(required in owned for required in room.get_requires())
        ]