"""обработчик событий создания персонажа.
здесь располоджены функции для создания персонажа
при создании берет объект самого персонажа из
соответствущего файла.
ожидаемый результат - успещная сериализация данных в json файл

НАВОДИМ ПОРЯДОК В ЭТОЙ ПАРАШЕ"""

import create_fucntion as createFunc
import common_fucntion as commonFunc
from character_class import Character as Chara
import using_json_files as ujs


def run_character_maker():
    """запуск страницы создания персонажа"""
    any_hero = Chara()
    while True:
        commonFunc.clean_screen()
        commonFunc.header()
        actions = ["выход",  # 1
                   "сгенерировать характеристики",  # 2
                   "вписать имя игрока",  # 3
                   "выбрать имя персонажу",  # 4
                   "выбрать расу и подрасу",  # 5
                   "выбрать класс",  # 6
                   "выбрать подкласс",  # 7
                   "выбрать предисторию",  # 8
                   "осмотреть инвентарь",  # 9
                   "сохранить данные",  # 10
                   "сбросить"]  # 11
        commonFunc.user_chose(actions)
        user_choose = input("Ваш выбор: ").strip()
        match user_choose:
            case "1":
                break
            case "2":
                any_hero.stats = createFunc.generation_of_characteristics()
                # по идее правильно работает
            case "3":
                # имя игрока
                any_hero.player_name = createFunc.player_name_entry()
            case "4":
                # имя персонажа
                any_hero.character_name = createFunc.character_name_entry()
            case "5":
                createFunc.choose_race()  # выбор расы
            case "6":
                print("заглушка")
            case "7":
                print("заглушка")
            case "8":
                print("заглушка")
            case "9":
                print("заглушка")
            case "10":  # сохранение текущей информации в словарь
                ujs.save_character(any_hero.character_info())
            case "11":  # сброс данных к текущему словарю
                print("заглушка")
