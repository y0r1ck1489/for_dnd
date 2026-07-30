"main"
import os
import subprocess
from character import CharCreator


def termclean():
    """функция очистки экрана терминала"""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


def main():
    """основная программа"""
    while True:
        termclean()
        text = '=' * 10 + 'CHARACTERMAKER' + '=' * 10
        print(text)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ: \n(введите номер действия)")
        placeholder = "\n1. Создать персонажа  \n2. Удалить персонажа\
             \n3. Изменить персонажа \n4. выйти\n"
        print(placeholder)
        choose = input("Ваш выбор:\n").strip()

        match choose:
            case "1":
                creator = CharCreator()
                creator.run()
            case "2":
                # """ЗАПУСК ФУНКЦИИ УДАЛЕНИЯ"""
                print("ЗАГЛУШКА ДЛЯ СТРАНИЦЫ УДАЛЕНИЯ")
            case "3":
                # """ЗАПУСК ФУНКЦИИ ОБНОВЛЕНИЯ"""
                print("ЗАГЛУШКА ДЛЯ СТРАНИЦЫ ОБНОВЛЕНИЯ")
            case "4":
                # """ЗАПУСК ФУНКЦИИ СОХРАНЕНИЯ И ВЫХОДА"""
                print("ПОШЕЛ НАХУЙ")
                break


if __name__ == "__main__":
    main()
