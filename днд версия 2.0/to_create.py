""" to create"""
import json
import os
import subprocess
# данный режим должен включать в себя
# 1. в качестве основной функции вносить новых персонажей в словарь/json файл
# 2. присваивать имя для персонажа  *добавить функциб в поведение "класса"
# 3. выбор класса персонажа.
# 4. выбор предистории. *добавить функциб в поведение "класса"
# 5. выбор расы.*добавить функциб в поведение "класса"
# а дальше в произвольном порядке будет избираться
# конкретная функция для пользователя.
# сперва наполним информациб которая будет доступна пользователю на выбор
# в ограниченном пуле т е будет небольшая часть предисторий небольшая часть рас
# и не большая часть классов. вся инфа будет храниться в json подобных файлах


def main():
    """работа раздела создания персонажа"""
    def generator_status():
        """функция генерации характеристик персонажа"""
    # посмотри основные моменты создания этой функции в первой версии программы
    def choose_race():
        """выбор расы"""
        race_by_number = {race["number"]: race for race in races_info}
        while True:
            termclean()
            show_race()
            number = input("Enter number of character's race:").strip()
            if number not in race_by_number:
                print("нет такой расы повторите снова ввод")
                input("Нажмите Enter для продолжения...")
                continue
            chosen_race = race_by_number[number]
            print("Race your character: " + chosen_race["rname"] + "?")
            while True:
                answer = input("Do you agree with the race?").lower()
                match answer:
                    case "no":
                        confirmed = False
                        break
                    case "yes":
                        character["CHrace"] = chosen_race["rname"]
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                print("Раса персонажа: " + character["CHrace"])
                break

    def termclean():
        """функция очистки экрана терминала"""
        if os.name == 'nt':
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)

    def show_race():
        """открывает список рас"""
        for race in races_info:  # проверка работы вывода доступных рас пока
            # что сделано две расы
            print(race["number"] + ". " + race["rname"])

    def show_bg():
        """открывает список предисторий"""
        for bg in bg_info:  # проверка работы вывода доступных рас пока что
            # сделано две предисторий
            print(bg["number"] + ". " + bg["id"])

    def choose_bg():
        """выбор предистории персонажа"""
        bg_by_number = {bg["number"]: bg for bg in bg_info}
        while True:
            termclean()
            show_bg()
            number = input("Enter character's  bg:").strip()
            if number not in bg_by_number:
                print("нет такой предистории повторите выбор")
                input("Нажмите Enter для продолжения...")
                continue
            choosen_bg = bg_by_number[number]
            print("ПРЕДИСТОРИЯ your character: " + choosen_bg["id"] + "?")
            while True:
                answer = input("Do you agree with the bg?").lower()
                match answer:
                    case "no":
                        confirmed = False
                        break
                    case "yes":
                        character["CHbg"] = choosen_bg["id"]
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                print("предисория персонажа " + character["CHbg"] + "выбрана")
                break

    def choose_name():
        """выбор имени персонажа"""
        while True:
            name = input("Enter character's  name:")
            print("Name your character: " + name + "?")
            while True:
                answer = input("Do you agree with the name?").lower()
                match answer:
                    case "no":
                        confirmed = False
                        break
                    case "yes":
                        character["CHname"] = name
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                break

    # в теории тут должен быть класс с описанными в нем действиями
    # данный блок отвечает за подгрузку json файлов
    way_to_races = os.path.dirname(os.path.abspath(__file__))
    races_info_path = os.path.join(way_to_races, "races.json")
    with open(races_info_path, "r", encoding="utf-8") as file0:
        races_info = json.load(file0)

    way_to_bgs = os.path.dirname(os.path.abspath(__file__))
    bgs_info_path = os.path.join(way_to_bgs, "bgrounds.json")
    with open(bgs_info_path, "r", encoding="utf-8") as file1:
        bg_info = json.load(file1)

    # way_to_bg = os.path.dirname(os.path.abspath(__file__))
    # bg_info_path = os.path.join(way_to_bg, "bgrounds.json")
    # with open(bg_info_path, "r", encoding="utf-8") as file1:
    #     bg_info = json.load(file1)    -- эта штука будет для
    # классов

    character = {"CHname": "",  # типа щаблон перса
                 "CHrace": "",
                 "CHbg": "",
                 "CHinv": "",
                 "CHstts": ""}
# основная работа программы через while
    print("вы в меню создания персонажа.\n пожалуйста выберите действие")
    action = ["выход", "сгенирировать характеристики", "выбрать имя",
              "выбрать расу и подрасу", "выбрать класс(реализовать в будущем)",
              "выбрать предисторию", "осмотреть инвентарь"]
    for index, item in enumerate(action):
        print(str(index) + ". " + str(item.title()))
    while True:
        termclean()
        choosen_act = input("yours chose:")
        match choosen_act:
            case "0":
                print("ВЫХОДИМ...")
                break
            case "1":
                print("ЗАГЛУШКА")
            case "2":
                choose_name()
            case "3":
                choose_race()
            case "4":
                print("ЗАГЛУШКА")
            case "5":
                choose_bg()
            case "6":
                print("ЗАГЛУШКА")
            case "7":
                print("ЗАГЛУШКА")
            case _:
                print("повторите ввод")


main()
