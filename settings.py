from colorama import init,Fore
from main import main
init()

setting = open('settings.txt', 'r')

settingses_1 = """
(1) Сменить цвет начального меню
(2) Убрать сообщения об покупке программы
(3) Добавить свое приветственное сообщение
(55) Обратно в меню
"""
print(Fore.RED + settingses_1)
settings_2 = input(Fore.RED + "Выберите пункт:")
if settings_2 == '55':
    main()