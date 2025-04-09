from helpers import clear_console, show_menu
from movies import list_movies, add_movie, view_movie, update_movie, delete_movie

def run():
    clear_console()
    while True:
        show_menu()
        option = input('Elije una opción [0-5]: ')
        clear_console()
        match option:
            case '1':
                list_movies()
            case '2':
                add_movie()
            case '3':
                view_movie()
            case '4':
                update_movie()
            case '5':
                delete_movie()
            case '0':
                print('Hasta Luego!')
                break
            case _:
                print('Opcion no válida')


if __name__ == '__main__':
    run()
