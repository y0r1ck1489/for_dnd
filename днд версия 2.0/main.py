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
        text = '=' * 10 + 'WELCOME TO CHARACTERMAKER' + '=' * 10
        print(text)
        print("SELECT YOURE ACTION:")
        print("(enter number)")
        placeholder = "\n1. Create Character \n2. Delete Character\
             \n3. Updater"\
            "Character \n4. Exit\n"
        print(placeholder)
        choose = input("yours chose:\n").strip()

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
                print("ПОШЕЛ НАХУЙ(прописать штуку записи и сохранения инфы)")
                break


if __name__ == "__main__":
    main()
