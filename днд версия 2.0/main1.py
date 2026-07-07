"""
черновая версия программы
реализация мемов
1. приветствие сделано.
2. переход к выбору действий сделано
3. прописать заглушки к режимам работы сделано
4. постаратсья вынести каждую из написанных функций/классов в отдельные файлики
согласно принципу ООП """


def main():
    """основная программа"""

    text = '=' * 10 + 'WELCOME TO CHARACTERMAKER' + '=' * 10
    print(text)
    print("SELECT YOURE ACTION:")
    print("(enter number)")
    placeholder = "\n1. Create Character \n2. Delete Character \n3. Updater"\
        "Character \n4. Exit\n"
    print(placeholder)

    while True:
        first_choose = int(input("yours chose:\n"))
        match first_choose:
            case 1:
                # ЗАПУСК ФУНКЦИИ СОЗДАНИЯ
                print("ЗАГЛУШКА ДЛЯ СТРАНИЦЫ СОЗДАНИЯ")
            case 2:
                # """ЗАПУСК ФУНКЦИИ УДАЛЕНИЯ"""
                print("ЗАГЛУШКА ДЛЯ СТРАНИЦЫ УДАЛЕНИЯ")
            case 3:
                # """ЗАПУСК ФУНКЦИИ ОБНОВЛЕНИЯ"""
                print("ЗАГЛУШКА ДЛЯ СТРАНИЦЫ ОБНОВЛЕНИЯ")
            case 4:
                # """ЗАПУСК ФУНКЦИИ СОХРАНЕНИЯ И ВЫХОДА"""
                print("ПОШЕЛ НАХУЙ(прописать штуку записи и сохранения инфы)")
                break


main()
