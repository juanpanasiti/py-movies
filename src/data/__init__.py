from typing import List

# from . import db
from .db import initialize_data
from .models.movie_model import MovieModel


movie_db: List[MovieModel] = initialize_data()
