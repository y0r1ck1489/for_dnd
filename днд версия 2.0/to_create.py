""" to create"""
import json
import os
# данный режим должен включать в себя
# 1. в качестве основной функции вносить новых персонажей в словарь/json файл
# 2. присваивать имя для персонажа
# 3. выбор класса.
# 4. выбор предистории.
# 5. выбор расы.
# в теории такую функциб нужно реализовать через класс
# а дальше в произвольном порядке будет избираться
# конкретная функция для пользователя.
# сперва наполним информациб которая будет доступна пользователю на выбор
# в ограниченном пуле т е будет небольшая часть предисторий небольшая часть рас
# и не большая часть классов. вся инфа будет храниться в json подобных файлах
# для проведения соответсвующих операциях
#  """print(type(race_info))
#  print(race_info)"""  мусор

# данный блок отвечает за подгрузку json файла рас
way_to_race = os.path.dirname(os.path.abspath(__file__))
races_info_path = os.path.join(way_to_race, "races.json")
with open(races_info_path, "r", encoding="utf-8") as file0:
    race_info = json.load(file0)

# данный блок отвечает за подгрузку json файла предимторий
way_to_bg = os.path.dirname(os.path.abspath(__file__))
bg_info_path = os.path.join(way_to_bg, "bgrounds.json")
with open(bg_info_path, "r", encoding="utf-8") as file1:
    bg_info = json.load(file1)


def show_race():
    """открывает список рас"""
    for race in race_info:  # проверка работы вывода доступных рас пока что
        # сделано две расы
        print(race["number"] + ". " + race["name"])


def show_bg():
    """открывает список предисторий"""
    for bg in bg_info:  # проверка работы вывода доступных рас пока что
        # сделано две предисторий
        print(bg["number"] + ". " + bg["id"])


def choose_name():
    """ввод имени персонажа"""
    while True:
        name = input("Enter character's  name:")
        print("Name your character: " + name)
        while True:
            answer = input("Do you agree with the name?").lower()
            match answer:
                case "no":
                    confirmed = False
                    break
                case "yes":
                    confirmed = True
                    break
                case _:
                    print("please confirm your choice. 'yes' or 'no'")
        if confirmed:
            break

show_race()

show_bg()