class Room:
    def __init__(self, name : str , description : str , exits : dict[str,str] , items : list, locked : bool, requires=None, trial_items = None):
        self._name = name
        self._description = description
        self._exits = exits
        self._items = self._clean(items)
        self._locked = locked
        self._requires = self._clean(requires or [])
        self._trial_items = self._clean(trial_items or [])

    def has_item(self, item):
        return item.strip().lower() in self._items

    def is_trial_item(self, item):
        return self.has_item(item) and item.strip().lower() in self._trial_items

    def get_requires(self):
        return self._requires

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_exits (self) -> dict[str,str]:
        return self._exits

    def get_items(self) -> list:
        return self._items

    def remove_item(self, item):
        name = item.strip().lower()
        if name in self._items:
            self._items.remove(name)

    @staticmethod
    def _clean(items):
        return [item.strip().lower() for item in items]

    def get_status(self) -> bool:
        return self._locked

    def set_status(self, status: bool):
        self._locked = status


    def to_dict(self):
        return {
            self._name : {
                "description" : self._description,
                "exits" : self._exits,
                "items" : self._items,
                "locked" : self._locked,
                "requires" : self._requires,
                "trial_items" : self._trial_items
            }
        }




