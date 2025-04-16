from typing import Optional
# Movie
# - title: str
# - year: int
# - director: str
# - synopsis: str
# - viewed: bool


class MovieModel():
    def __init__(self, title: str, year: int, director: Optional[str], synopsis: Optional[str], viewed: Optional[bool] = False):
        self.title: str = title.title()
        self.year: str = year
        self.director: str = director or ''
        self.synopsis: str = synopsis or ''
        self.viewed: bool = viewed

    def to_json(self):
        return self.__dict__
