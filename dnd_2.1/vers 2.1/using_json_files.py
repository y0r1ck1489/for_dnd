"""библиотека функций подгрузки и сохранения данных"""
import json


# сохранение персонажа
def save_character(character):
    """сохранение персонажа"""
    filename = "saved_characters.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            characters = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        characters = []
    characters.append(character)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(character, file, ensure_ascii=False, indent=4)
        print(f"Герой сохранен в {filename}")


# чтение файла
def read_n_load_info(way_to_dir):
    """функция ищет путь для подгрузки всех данных"""
    try:
        with open(way_to_dir, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
        return None
    except json.JSONDecodeError:
        print("Файл поврежден")
        return None
