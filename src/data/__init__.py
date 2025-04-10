# from . import db
from .db import initialize_data


movie_db: list[dict] = initialize_data()
