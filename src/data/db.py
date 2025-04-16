from typing import List

from src.helpers.file_helpers import read_json_file
from src.config.constants import MOVIES_JSON_FILE
from .models.movie_model import MovieModel


def initialize_data() -> List[MovieModel]:
    movies_list: list[dict] = read_json_file(MOVIES_JSON_FILE)
    # return [MovieModel(title=movie_dict['title'], ....) for movie_dict in movies_list]
    return [MovieModel(**movie_dict) for movie_dict in movies_list]

    