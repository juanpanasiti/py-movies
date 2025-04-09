from typing import Optional

from data import movie_db
from constants import VIEWED, NOT_VIEWED
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
    title = input('Título: ')
    year = input('Año: ')
    director = input('Director: ')
    movie = {
        'title': title,
        'year': int(year) if year.isnumeric() else 0,
        'director': director,
        'synopsis': '',
        'viewed': False,
    }
    movie_db.append(movie)


def view_movie():
    if not __check_if_movies():
        return
    movie = __find_movie()
    if movie is None:
        return
    print(movie)


def update_movie():
    if not __check_if_movies():
        return
    movie = __find_movie()
    if movie is None:
        return
    new_title = input(f'Nuevo Título [{movie["title"]}]: ')
    new_year = input(f'Nuevo Año [{movie["year"]}]: ')
    new_director = input(f'Nuevo Director [{movie["director"]}]: ')
    new_viewed = input(f'Vista? S/N [{movie["viewed"]}]: ')
    if new_title:
        movie['title'] = new_title
    if new_year:
        movie['year'] = int(new_year)
    if new_director:
        movie['director'] = new_director
    if new_viewed:
        movie['viewed'] = True if new_viewed.upper() == 'S' else False


def delete_movie():
    if not __check_if_movies():
        return
    list_movies()
    option = int(input(f'Elije una pelicula para eliminar [1-{len(movie_db)}]: '))
    movie_db.pop(option - 1)


def __check_if_movies():
    if not movie_db:
        print('no hay peliculas cargadas')
        return False
    return True


def __find_movie() -> Optional[dict]:
    list_movies()
    option = int(input(f'Elije una película [1-{len(movie_db)}]: '))
    for index, movie in enumerate(movie_db, start=1):
        if option == index:
            return movie
    print('No se encontró la pelicula')
