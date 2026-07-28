""" to create"""
import json
import os
import subprocess
from random import randint


class CharCreator:
    """Класс для создания персонажа и сохранения его в файл"""

    def __init__(self):
        self.character = {
            "name": "",
            "race": "",
            "background": "",
            "inventory": "",
            "stats": {
                "str": 0,
                "dex": 0,
                "const": 0,
                "int": 0,
                "wis": 0,
                "char": 0
            },
        }

        self.races_info = []
        self.bg_info = []
        self._load_data()

    def _load_data(self):
        """загрзка данных о расе и предистории"""
        base_dir = os.path.dirname(os.path.abspath(__file__))

        def load_json(filename):
            path = os.path.join(base_dir, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except FileNotFoundError:
                print("файл не найден")
            except json.JSONDecodeError:
                print("Файл поврежден или имеет не тот формат")
            return None

        self.races_info = load_json("races.json")
        self.bg_info = load_json("bgrounds.json")
        if self.races_info is None or self.bg_info is None:
            print("Не удалось загрузить данные для создания персонажа")
            exit(1)

    @staticmethod
    def termclean():
        """функция очистки экрана терминала"""
        if os.name == 'nt':
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)

    def generator_status(self):
        """функция генерации характеристик персонажа"""
        self.termclean()
        print('=' * 10 + "Генерация статов" + '=' * 10)
        stats = {'str': 0,
                 'dex': 0,
                 'const': 0,
                 'int': 0,
                 'wis': 0,
                 'char': 0}
        while True:
            for key in stats:
                dice = sorted(randint(1, 6) for _ in range(4))
                result = sum(dice[1:])
                stats[key] = result
                print(f"{key}:{result} (выпало {dice})")
                txt = "Введите 'прекратить генерацию' чтобы завершить  "
                txt += "или 'продолжить генерацию' чтобы продожить "
                while True:
                    answer = str(input(txt).lower())
                    match answer:
                        case "прекратить генерацию":
                            self.character["stats"] = stats
                            return
                        case "продолжить генерацию":
                            break
                        case _:
                            print("неверный ввод")

    def choose_name(self):
        """Выбор имени"""
        self.termclean()
        while True:
            confirmed = False
            name = input("Enter character's  name:").strip()
            print("Name your character: " + name + "?")
            while True:
                answer = input("Do you agree with the name?").lower()
                match answer:
                    case "no":
                        break
                    case "yes":
                        self.character["name"] = name
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                break

    def choose_race(self):
        """выбор расы"""
        race_by_number = {race["number"]: race for race in self.races_info}
        while True:
            self.termclean()
            for race in self.races_info:
                print(race["number"] + ". " + race["rname"])
            number = input("Enter number of character's race:").strip()
            if number not in race_by_number:
                print("нет такой расы повторите снова ввод")
                input("Нажмите Enter для продолжения...")
                continue
            chosen_race = race_by_number[number]
            print("Race your character: " + chosen_race["rname"] + "?")
            confirmed = False
            while True:
                answer = str(input("Do you agree with the race?").lower())
                match answer:
                    case "no":
                        break
                    case "yes":
                        self.character["race"] = chosen_race["rname"]
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                print("Раса персонажа: " + self.character["race"])
                break

    def choose_background(self):
        """выбор предистории из списка"""
        bg_by_number = {bg["number"]: bg for bg in self.bg_info}
        while True:
            self.termclean()
            for bg in self.bg_info:
                print(bg["number"] + ". " + bg["id"])
            number = input("Enter character's  bg:").strip()
            if number not in bg_by_number:
                print("нет такой предистории повторите выбор")
                input("Нажмите Enter для продолжения...")
                continue

            choosen_bg = bg_by_number[number]
            print("ПРЕДИСТОРИЯ your character: " + choosen_bg["id"] + "?")
            confirmed = False
            while True:
                answer = input("Do you agree with the bg?").lower()
                match answer:
                    case "no":
                        break
                    case "yes":
                        self.character["background"] = choosen_bg["id"]
                        confirmed = True
                        break
                    case _:
                        print("please confirm your choice. 'yes' or 'no'")
            if confirmed:
                print("ваша предисория: " + self.character["background"] + "?")
                break

    def save_character(self):
        """Сохранение персонажа"""
        filename = "character.json"
        try:
            with open(filename, "r", encoding="utf-8",) as f:
                character_list = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            character_list = []
        character_list.append(self.character)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(character_list, f, ensure_ascii=False, indent=4)
        print(f"Персонаж сохранен в {filename} (всего: {len(character_list)})")

    def run(self):
        """главное меню раздела"""
        actions = [("Выход", None),
                   ("Сгенерировать характеристики", self.generator_status),
                   ("Выбрать имя", self.choose_name),
                   ("Выбрать расу", self.choose_race),
                   ("Выбрать класс(пока нет)", lambda: print("Заглушка")),
                   ("Выбрать предисторию", self.choose_background),
                   ("Осмотреть инвентарь", lambda: print("Заглушка")),
                   ("Сохранить персонажа", self.save_character),]
        while True:
            self.termclean()
            print("="*10 + "Создание персонажа" + "="*10)
            for i, (desc, _) in enumerate(actions):
                print(f"{i}.{desc}")
            choice = input("Ваш выбор").strip()
            if not choice.isdigit() or int(choice) not in range(len(actions)):
                print("Неверный ввод. Повтрите ввод")
                input("нажмите enter")
                continue
            idx = int(choice)
            if idx == 0:
                print("выходим из меню создания")
                break
            func = actions[idx][1]
            if func:
                func()
            input("Нажмите enter для возврата в меню")
