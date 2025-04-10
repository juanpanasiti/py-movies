import os

from termcolor import cprint, colored


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux o Mac
        os.system('clear')


def show_menu():
    cprint('--- My Movies ---', 'red', attrs=['bold', 'blink'])
    cprint('1. Ver lista de Películas', 'blue')
    cprint('2. Agregar Película', 'blue')
    cprint('3. Ver info de una Película', 'blue')
    cprint('4. Editar Película', 'blue')
    cprint('5. Eliminar Película', 'blue')
    print()
    cprint('0. Salir', 'red', attrs=['bold'])

def print_movie(movie: dict):
    print(colored('\n=== MOVIE DETAILS ===', 'cyan', attrs=['bold', 'underline']))
    print(colored('Title:     ', 'yellow', attrs=['bold']) + colored(movie['title'], 'white'))
    print(colored('Director:  ', 'yellow', attrs=['bold']) + colored(movie['director'], 'white'))
    print(colored('Year:      ', 'yellow', attrs=['bold']) + colored(str(movie['year']), 'white'))
    print(colored('Viewed:    ', 'yellow', attrs=[
          'bold']) + colored('Yes' if movie['viewed'] else 'No', 'green' if movie['viewed'] else 'red'))
    print(colored('Synopsis:  ', 'yellow', attrs=['bold']))
    print(colored(movie['synopsis'], 'light_grey'))
    print(colored('=' * 24, 'cyan'))
