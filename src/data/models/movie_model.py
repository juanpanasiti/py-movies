from typing import Optional

from .audiovisual_media_model import AudiovisualMediaModel


class MovieModel(AudiovisualMediaModel):
    def __init__(self, title: str, year: int, director: Optional[str], synopsis: Optional[str], viewed: Optional[bool] = False):
        # self.title: str = title.title()
        super().__init__(title, synopsis)
        self._year: str = year
        self.director: str = director or ''
        # self.synopsis: str = synopsis or ''
        self.viewed: bool = viewed

    @property
    def year(self) -> str:
        return self._year

    @year.setter
    def year(self, year: str) -> None:
        self._year = year

    def to_json(self):
        return self.__dict__
