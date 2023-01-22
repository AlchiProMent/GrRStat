# Дипломный проект "Получение данных с вебсайта Р-Стат"
#
from lib import *

TITLE_PROG = '"Получение данных с вебсайта Р-Стат" ver 1.0'

def block_one():
    msg('Выполнен блок 1...')

def block_two():
    msg('Выполнен блок 2...')

def block_three():
    msg('Выполнен блок 3...')

if __name__ == '__main__':
    # стартовая точка программы

    print(f'{TITLE_PROG}')

    # описание пунктов меню
    menu = {'1': ('Блок 1', block_one),
            '2': ('Блок 2', block_two),
            '3': ('Блок 3', block_three),
            EXIT_CODE: ('Выход', None)}

    # запуск меню
    run(menu_items=menu)
