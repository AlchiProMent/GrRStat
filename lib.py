# вспомогательные функции и константы
def msg(text=''):
    # вывод простого сообщения
    print(f'\n{text}')

# код выхода из меню
EXIT_CODE = '0'

def run(menu_items:dict):
    # главная функция
    # в справочнике пунктов ключ каждого элемента выводится в виде кода пункта меню,
    # значения для ключа представляет из себя кортеж из двух элементов:
    # название пункта и имя функции, которая должна выполниться после выбора пункта
    # пункт меню вводится с клавиатуры и подтверждается нажатием ENTER

    def view_menu(items_menu):
        # вывод меню на экран
        print()
        for key, item in items_menu.items():
            print(f'[{key}] - {items_menu[key][0]}')

    menu_keys_lst = []
    # получить ключи всех пунктов меню
    for key in menu_items:
        menu_keys_lst.append(key)

    # стартовый вывод меню на экран
    view_menu(menu_items)
    # Большой цикл по пунктам меню, пока пользователь не введёт EXIT_CODE
    while (menu_key := input('Введите код меню: ')) != EXIT_CODE:

        # если пользователь ввёл верный пункт меню и не EXIT_CODE
        if menu_key in menu_keys_lst and menu_key != EXIT_CODE:
            # получить имя функции
            func_name = menu_items[menu_key][1]
            # оформить вызов функции
            func_name()
        elif (menu_key != EXIT_CODE):
            msg('Неверная команда!')

        # снова вывести меню на экран
        view_menu(menu_items)

    # сообщение в конце работы программы
    msg('Программа закончила работу.')

