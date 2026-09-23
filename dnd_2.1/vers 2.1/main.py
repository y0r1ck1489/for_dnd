"""ЗАПУСК ВСЕЙ ПРОГРАММЫ ЧЕРЕЗ ТЕРМИНАЛ"""


def run_program():
    """запуск программы"""
    while True:
        uzor = "=" * 10
        title = "CHARACTER MAKER"
        header = f"{uzor} {title} {uzor}"
        print(header)
        print("Выберите действие: \n(введите номер действия) ")
        items = ["создать персонажа",
                 "удалить персонажа",
                 "изменить персонажа",
                 "выйти из программы"]
        for i, choose in enumerate(items, start=1):
            print(f"{i}.{choose.capitalize()}")
        user_choose = input("Ваш выбор: ").strip()
        match user_choose:
            case "1":
                print("заглушка один")
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
