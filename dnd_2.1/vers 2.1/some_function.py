""" функции всего приложения"""
import json
from random import randint
import common_fucntion as cf


 # хз хуйня какаято


# функция ввода имени игрока
def name_entry(default=" "): # внести в бесконечный цикл
    """функция которая принимает значение имени игрока
    персонаж может быть без владельца, иными словами черновик"""
    text_message = "Введите имя игрока:\n"
    players_name = input(text_message).strip()  # добавить в цикл
    if players_name:
        return players_name
    else:
        return default


# функция ввода имени персонажа
def character_name_entry(default=""): # внести в бесконечный цикл
    """функция которая принимает имя персонажа
    может быть пустым, чтобы можно было придумать позже(хз как такое
    можно реализовать)""" 
    text_message = "Введите имя персонажа\n"
    character_name = input(text_message).strip()  # добавить в цикл
    if character_name:
        return character_name
    else:
        return default


# функция генерации характеристик1
def generation_of_characteristics(characteristics=None):
    """функция "кидает кубики" и вычисляет
    модификаторы (вроде как хз пересмотреть потом)"""
    while True:
        cf.clean_screen()
        cf.header()
        characteristics = {'str': 0,
                           'dex': 0,
                           'cons': 0,
                           'int': 0,
                           'wisd': 0,
                           'chrsm': 0}
        generation_process(characteristics)  # уточнить с нейронкой


def choose_race(races_inf):  # скорее всего функция будет принимать путь в качестве параметра
    """выбор расы"""
    race_by_number = {race["number"]: race for race in races_inf}
    # запихуливание функции


# функция генерации характеристик2
def generation_process(characteristics):
    """рефакторная функция генерации характеристик"""
    for key in characteristics:
        dice = sorted(randint(1, 6) for _ in range(4))
        result = sum(dice[1:])
        characteristics[key] = result
        print(f"{key}:{result} - {dice}")

    text = "чтобы прекратить генерацию введите 0\n чтобы продолжить"
    text += " введите 1 продолжить"
    answer = input(text).strip()
    match answer:
        case "1":
            pass  # continue
        case "0":
            return characteristics
        case _:
            print("неверный ввод")


def races_cycle(race_by_number):  # вернуться позже
    while True:
        clean_screen()
