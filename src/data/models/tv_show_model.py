from typing import Optional

from .audiovisual_media_model import AudiovisualMediaModel

class TvShowModel(AudiovisualMediaModel):
    def __init__(self, title: str, start_year: int, end_year: Optional[int] = None, seasons: int = 1, status: str = 'en emisión', synopsis: Optional[str] = None):
        super().__init__(title, synopsis)
        self._start_year: int = start_year
        self._end_year: Optional[int] = end_year
        self._seasons: int = seasons
        self._status: str = status.lower()

    @property
    def start_year(self) -> int:
        return self._start_year

    @start_year.setter
    def start_year(self, year: int) -> None:
        if year > 1888:
            self._start_year = year
        else:
            raise ValueError('El año de inicio debe ser válido para una serie.')

    @property
    def end_year(self) -> Optional[int]:
        return self._end_year

    @end_year.setter
    def end_year(self, year: Optional[int]) -> None:
        if year is None or year >= self._start_year:
            self._end_year = year
        else:
            raise ValueError('El año de finalización no puede ser anterior al de inicio.')

    @property
    def seasons(self) -> int:
        return self._seasons

    @seasons.setter
    def seasons(self, new_season_count: int) -> None:
        if new_season_count > 0:
            self._seasons = new_season_count
        else:
            raise ValueError('El número de temporadas debe ser mayor a cero.')

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str) -> None:
        valid_status = ['en emisión', 'finalizada', 'cancelada']
        if new_status.lower() in valid_status:
            self._status = new_status.lower()
        else:
            raise ValueError(f'Estado inválido. Debe ser uno de: {valid_status}')