class Room:
    def __init__(self, name : str , description : str , exits : dict[str,str] , items : list, status : bool):
        self._name = name
        self._description = description
        self._exits = exits
        self._items = items
        self._status = status

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_exits (self) -> dict[str,str]:
        return self._exits

    def get_items(self) -> list:
        return self._items

    def remove_item(self, item):
        self._items.remove(item)

    def get_status(self) -> bool:
        return self._status

    def set_status(self, status: bool):
        self._status = status



