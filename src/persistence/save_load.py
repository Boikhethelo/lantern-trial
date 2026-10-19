
class SaveStore:
    def __init__(self, path=Path("resources/save_file.json")):
        self._path = path

    def save(self, data: dict) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self) -> dict | None:
        if not self._path.exists():
            return None
        try:
            with open(self._path) as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        return data if data.get("character") else None
