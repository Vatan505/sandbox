from pathlib import Path



class PathProvider:

    def __init__(self):
        self._root_dir = None
        self.filename: str = "pytest.ini"

    @property
    def root_dir(self) -> Path:
        current_path = Path(__file__).resolve()
        for parent in current_path.parents:
            if (parent / self.filename).exists():
                self.root_dir = parent
                return self._root_dir
        raise FileNotFoundError(f"Файл {self.filename} не найден в родительских директориях.")

    @root_dir.setter
    def root_dir(self, value):
        self._root_dir = value
        