from typing import Any


class Player:
    def __init__(self , name:str, sector:str, strength:str, weakness:str):
        self._name = name
        self._sector = sector
        self._strength = strength
        self._weakness = weakness
        self._position = ""

        self._items = []
        self._score = 0

    def get_name(self ) -> str:
        return self._name

    def get_strength(self) -> str:
        return self._strength

    def get_weakness(self) -> str:
        return self._weakness

    def get_position(self) -> str:
        return self._position

    def set_position(self, position: str):
        self._position = position

    def set_items(self, items: list[str]):
        self._items = items

    def set_score(self, score: int):
        self._score = score

    def get_items(self) -> list[str]:
        return self._items

    def get_score(self) -> int:
        return self._score

    def add_item(self, item : str):
        self._items += item

    def add_score(self, score: int):
        self._score += score





