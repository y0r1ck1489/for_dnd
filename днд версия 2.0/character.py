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
            "subrace": "",
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
            "mods": {
                "mstr": 0,
                "mdex": 0,
                "mconst": 0,
                "mint": 0,
                "mwis": 0,
                "mchar": 0

            }
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
            txt = "Введите '0' чтобы завершить генерацию "
            txt += "или '1' чтобы продожить "
            while True:
                answer = str(input(txt).lower())
                match answer:
                    case "0":
                        self.character["stats"] = stats
                        return
                    case "1":
                        break
                    case _:
                        print("неверный ввод")

    def choose_name(self):
        """Выбор имени"""
        self.termclean()
        while True:
            confirmed = False
            name = input("Введите имя персонажа\n").strip()
            print("Имя Вашего персонажа: " + name + "?")
            while True:
                answer = input("Вам нравится имя?\n").lower()
                match answer:
                    case "no" | "нет":
                        break
                    case "yes" | "да":
                        self.character["name"] = name
                        confirmed = True
                        break
                    case _:
                        print("Пожалуйста завершите выбор имени. \n Введите \
                    'yes/да' или 'no/нет'")
            if confirmed:
                break

    def choose_race(self):
        """выбор расы"""
        race_by_number = {race["number"]: race for race in self.races_info}
        while True:
            self.termclean()
            for race in self.races_info:
                print(race["number"] + ". " + race["rname"])
            number = input("Введите номер расы персонажа:\n").strip()
            if number not in race_by_number:
                print("нет такой расы повторите снова ввод")
                input("Нажмите Enter для продолжения...")
                continue
            chosen_race = race_by_number[number]
            print("Раса Вашего персонажа: " + chosen_race["rname"] + "?")
            confirmed = False
            while True:
                answer = str(input("Вы согласны с расой?\n").lower())
                match answer:
                    case "no" | "нет":
                        break
                    case "yes" | "да":
                        self.character["race"] = chosen_race["rname"]
                        self._choose_subrace(chosen_race)
                        confirmed = True
                        break
                    case _:
                        print("Пожалуйста завершите выбор расы. \n Введите \
                    'yes/да' или 'no/нет'")
            if confirmed:
                print("Раса персонажа: " + self.character["race"])
                break

    def _choose_subrace(self, race):
        """выбор подрасы"""
        if "subraces" not in race:
            self.character["subrace"] = ""
            return

        subraces = race["subraces"]
        subrace_keys = list(subraces.keys())
        while True:
            self.termclean()
            print(f"Выберите подрасу для расы {race['rname']}:")
            for i, key in enumerate(subrace_keys, 1):
                desc = subraces[key].get("description", "Нет описания")
                short_desc = (desc[: 80] + "...") if len(desc) > 80 else desc
                print(f"{i}. {key.replace('_', ' ').title()} - {short_desc}")
            print("0. Без подрасы")

            choice = input("Ваш выбор").strip()
            if not choice.isdigit() or int(choice) not in range(0, len(subrace_keys) + 1):
                print("Неверный ввод. Повторите ввод.")
                input("Введите enter")
                continue
            idx = int(choice)
            if idx == 0:
                self.character["subrace"] = ""
                break
            else:
                chosen_key = subrace_keys[idx - 1]
                print(f"Выбрана подраса: {chosen_key.replace('_', ' ').title()}")
                confirm = input("Вы согласны с подрасой?").lower()
                match confirm:
                    case "да" | "yes":
                        self.character["subrace"] = chosen_key
                        break
                    case "нет" | "no":
                        pass

    def choose_background(self):
        """выбор предистории из списка"""
        bg_by_number = {bg["number"]: bg for bg in self.bg_info}
        while True:
            self.termclean()
            for bg in self.bg_info:
                print(bg["number"] + ". " + bg["id"])
            number = input("Введите номер предистории:\n").strip()
            if number not in bg_by_number:
                print("нет такой предистории повторите выбор")
                input("Нажмите Enter для продолжения...")
                continue

            choosen_bg = bg_by_number[number]
            print("Предистория вашего персонажа: " + choosen_bg["id"] + "?")
            confirmed = False
            while True:
                answer = input("Вы согласны с выбором?\n").lower()
                match answer:
                    case "no" | "нет":
                        break
                    case "yes" | "да":
                        self.character["background"] = choosen_bg["id"]
                        confirmed = True
                        break
                    case _:
                        print("Пожалуйста завершите выбор предистории. \n \
                        Введите 'yes/да' или 'no/нет'")
            if confirmed:
                print("Ваша предисория: " + self.character["background"] + "?")
                break

    def save_character(self):
        """Сохранение персонажа"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(base_dir, "character.json")
        try:
            with open(filename, "r", encoding="utf-8",) as f:
                character_list = json.load(f)
                if not isinstance(character_list, list):
                    character_list =[]
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
                   ("Выбрать расу и подрасу(доделать)", self.choose_race),
                   ("Сложить расовые бонусы", lambda: print("Заглушка")),
                   ("Выбрать класс(пока нет)", lambda: print("Заглушка")),
                   ("Вычислить модификаторы", lambda: print("Заглушка")),
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
