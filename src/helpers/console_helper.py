import os
from typing import Optional

from termcolor import colored, cprint


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux o Mac
        os.system('clear')


def get_string(message: str, accept_blank: bool = True) -> str:
    while True:
        value = input(colored(message, 'blue'))
        if not value and not accept_blank:
            cprint('Debe ingresar algo.', 'red')
            continue
        return value


def get_int(message: str, accept_blank: bool = True, min_value: Optional[int] = None, max_value: Optional[int] = None) -> Optional[int]:
    try:
        value = get_string(message, accept_blank)
        if not value and accept_blank:
            return None
        if not value.isnumeric():
            raise ValueError(colored('El valor ingresado no es un número.', 'red'))
        value = int(value)
        if min_value is not None and value < min_value:
            raise ValueError(colored(f'El número debe ser mayor o igual a {min_value}.', 'red'))
        if max_value is not None and value > max_value:
            raise ValueError(colored(f'El número debe ser menor o igual a {max_value}.', 'red'))
        return value
    except ValueError as ex:
        print(ex)
        return get_int(message, accept_blank, min_value, max_value)


def get_bool(message: str, accept_blank: bool = True) -> Optional[bool]:
    VALID_VALUES = ('S', 'N')
    try:
        value = get_string(message, accept_blank)
        if not value and accept_blank:
            None
        if value.upper() not in VALID_VALUES:
            raise ValueError(colored(f'Respuestas válidad: {VALID_VALUES}', 'red'))
        return value == VALID_VALUES[0]
    except ValueError as ex:
        print(ex)
        return get_bool(message, accept_blank)
