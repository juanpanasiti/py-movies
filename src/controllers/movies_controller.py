from typing import Optional

from src.config.constants import VIEWED, NOT_VIEWED
from src.data import movie_db
from src.helpers.movie_helpers import print_movie, save_movies
from src.helpers.console_helper import get_string, get_int, get_bool
# Movie
# - title: str
# - year: int
# - director: str
# - synopsis: str
# - viewed: bool


def list_movies():
    if not __check_if_movies():
        return

    for index, movie in enumerate(movie_db, start=1):
        view_status = VIEWED if movie['viewed'] else NOT_VIEWED
        print(f'{index}. {movie['title']} - {view_status}')  # 1. Star Wars - ⬜


def add_movie():
    title = get_string('Título: ', accept_blank=False)
    year = get_int('Año: ', accept_blank=False, min_value=1900)
    director = get_string('Director: ')
    movie = {
        'title': title,
        'year': year,
        'director': director,
        'synopsis': '',
        'viewed': False,
    }
    movie_db.append(movie)
    save_movies()


def view_movie():
    if not __check_if_movies():
        return
    movie = __find_movie()
    if movie is None:
        return
    print_movie(movie)


def update_movie():
    if not __check_if_movies():
        return
    movie = __find_movie()
    if movie is None:
        return
    view_status = VIEWED if movie['viewed'] else NOT_VIEWED
    movie['title'] = get_string(f'Nuevo Título [{movie["title"]}]: ') or movie['title']
    movie['year'] = get_int(f'Nuevo Año [{movie["year"]}]: ') or movie['year']
    movie['director'] = get_string(f'Nuevo Director [{movie["director"]}]: ') or movie['director']
    viewed = get_bool(f'Vista? S/N [{view_status}]: ')
    movie['viewed'] = movie['viewed'] if viewed is None else viewed
    save_movies()


def delete_movie():
    if not __check_if_movies():
        return
    list_movies()
    option = get_int(
        message=f'Elije una pelicula para eliminar [1-{len(movie_db)}]: ',
        min_value=1,
        max_value=len(movie_db),
        accept_blank=True,
    )
    if not option:
        return
    movie_db.pop(option - 1)
    save_movies()


def __check_if_movies():
    if not movie_db:
        print('no hay peliculas cargadas')
        return False
    return True


def __find_movie() -> Optional[dict]:
    list_movies()
    option = get_int(
        message=f'Elije una película [1-{len(movie_db)}]: ',
        min_value=1,
        max_value=len(movie_db),
        accept_blank=False,
    )
    for index, movie in enumerate(movie_db, start=1):
        if option == index:
            return movie
    print('No se encontró la pelicula')
