from termcolor import cprint, colored

from src.config.constants import VIEWED, NOT_VIEWED, MOVIES_JSON_FILE
from src.helpers.file_helpers import write_json_file
from src.data import movie_db, MovieModel


def show_menu():
    cprint('--- My Movies ---', 'red', attrs=['bold', 'blink'])
    cprint('1. Ver lista de Películas', 'blue')
    cprint('2. Agregar Película', 'blue')
    cprint('3. Ver info de una Película', 'blue')
    cprint('4. Editar Película', 'blue')
    cprint('5. Eliminar Película', 'blue')
    print()
    cprint('0. Salir', 'red', attrs=['bold'])


def print_movie(movie: MovieModel):
    view_status = VIEWED if movie.viewed else NOT_VIEWED
    year_str = '-' if not movie.year else str(movie.year)
    print(colored('\n===== PELICULA =====', 'cyan', attrs=['bold', 'underline']))
    print(colored('Título:     ', 'yellow', attrs=['bold']) + colored(movie.title, 'white'))
    print(colored('Director:   ', 'yellow', attrs=['bold']) + colored(movie.director, 'white'))
    print(colored('Año:        ', 'yellow', attrs=['bold']) + colored(year_str, 'white'))
    print(colored('Vista?      ', 'yellow', attrs=['bold']) + view_status)
    print(colored('Sinopsis:  ', 'yellow', attrs=['bold']))
    print(colored(movie.synopsis, 'light_grey'))
    print(colored('=' * 24, 'cyan'))


def save_movies() -> None:
    movies_list: list[dict] = [movie.to_json() for movie in movie_db]
    write_json_file(MOVIES_JSON_FILE, movies_list)
