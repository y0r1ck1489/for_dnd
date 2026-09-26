"""ЗАПУСК ВСЕЙ ПРОГРАММЫ ЧЕРЕЗ ТЕРМИНАЛ или главный обработчик"""
import creator_page
import common_fucntion as cf


def run_program():
    """запуск программы"""
    while True:
        cf.clean_screen()  # общая функция
        cf.header()  # общая функция
        print("Выберите действие: \n(введите номер действия) ")
        items = ["создать персонажа",
                 "удалить персонажа",
                 "изменить персонажа",
                 "выйти из программы"]
        cf.user_chose(items)  # обшая  функция
        user_choose = input("Ваш выбор: ").strip()
        match user_choose:
            case "1":
                print("заглушка один")
                creator_page.run_character_maker()  # вызов меню создания
            # персонажа
            case "2":
                print("заглушка два")
            case "3":
                print("заглушка три")
            case "4":
                print("Выходим...\n :)")
                break
            case _:
                print("Нет такого варианта")


if __name__ == "__main__":
    run_program()
