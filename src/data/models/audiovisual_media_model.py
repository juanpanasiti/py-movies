from typing import Optional


class AudiovisualMediaModel():
    def __init__(self, title: str, synopsis: Optional[str] = ''):
        self._title = title
        self._synopsis = synopsis

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def synopsis(self) -> str:
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        self._synopsis = synopsis
