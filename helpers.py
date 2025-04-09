import os

from termcolor import cprint


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
