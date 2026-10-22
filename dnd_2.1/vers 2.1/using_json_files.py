"""библиотека функций для манипуляции над данными"""
import json
import os


def save_character(character, save_place=None, way_to_file=None):
    """функция сохраненения данных в json файл"""
    if save_place is None:
        save_place = os.path.join("save_place", "saved_characters.json")
    if way_to_file is None:
        way_to_file = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(way_to_file, save_place)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(character)
    with open(file_path, "w", encoding="utf-8") as saved_inf:
        json.dump(data, saved_inf, ensure_ascii=False, indent=4)
    print(f"герой сохранент в {file_path}")


def read_info(json_storage, way_to_file=None):  # НЕ ТРОГАТЬ КОД РАБОТАЕТ
    """функция подгрузки и чтения
     документов json """
    if way_to_file is None:  # предохроняемся от сбоя параметров
        way_to_file = os.path.dirname(os.path.abspath(__file__))  # getway
    file_path = os.path.join(way_to_file, json_storage)  # объеднияем 2 пути в1
    try:
        with open(file_path, "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data  # при благоприятном условии загружаем данные в переменную
    except FileNotFoundError:
        print("такого файла нет")
        return None
    except json.JSONDecodeError:
        print("файл сломан")
        return None
