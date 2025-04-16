from src.helpers.console_helper import clear_console  # * Recomendado
from src.helpers.movie_helpers import show_menu
# from helpers import *  # ! No recomendado
# from movies import list_movies, add_movie, view_movie, update_movie, delete_movie
# from controllers import movies_controller as movies
# from src.controllers import movies_controller as movies
from src.controllers import movies


def run():
    clear_console()

    while True:
        show_menu()
        option = input('Elije una opción [0-5]: ')
        clear_console()
        match option:
            case '1':
                movies.list_movies()
            case '2':
                movies.add_movie()
            case '3':
                movies.view_movie()
            case '4':
                movies.update_movie()
            case '5':
                movies.delete_movie()
            case '0':
                print('Hasta Luego!')

                break
            case _:
                print('Opcion no válida')