""" функции всего приложения"""
from random import randint
import common_fucntion as cf
#  import using_json_files as ujs

# ипипупуп добавить чтение данных в соответствующие функции


def choose_race():  # хз но по идее тут уже надо указать путь к файлам
    """выбор расы"""


# функция ввода имени игрока
def player_name_entry(default=""):
    """функция которая принимает значение имени игрока
    персонаж может быть без владельца, иными словами черновик"""
    text_message = "Введите имя игрока:\n"
    players_name = input(text_message).strip()  # добавить в цикл
    if players_name:
        return players_name
    else:
        return default


# функция ввода имени персонажа
def character_name_entry(default=""):
    """функция которая принимает имя персонажа
    может быть пустым, чтобы можно было придумать позже(хз как такое
    можно реализовать)"""
    text_message = "Введите имя персонажа\n"
    character_name = input(text_message).strip()  # добавить в цикл
    if character_name:
        return character_name
    else:
        return default


# функция генерации характеристик
def generation_of_characteristics():
    """функция "кидает кубики" и вычисляет
    модификаторы (вроде как хз пересмотреть потом)"""
    while True:
        cf.clean_screen()
        cf.header()

        text = "чтобы прекратить генерацию введите 0\n чтобы продолжить"
        text += " введите 1 продолжить"

        characteristics = generation_process()  # уточнить с нейронкой
        for k, v in characteristics.items():
            print(f"{k}: {v}")
        answer = input(text).strip()
        match answer:
            case "1":
                pass  # continue
            case "0":
                return characteristics
            case _:
                print("неверный ввод")


# функция генерации характеристик рефакторная часть
def generation_process():
    """рефакторная функция генерации характеристик"""
    stats = {}
    characteristics = ["strt", "dext", "cons", "intgl", "wisd", "charm"]
    for key in characteristics:
        dice = sorted(randint(1, 6) for _ in range(4))
        result = sum(dice[1:])
        stats[key] = result
        print(f"{key}:{result} - {dice}")
    return stats
