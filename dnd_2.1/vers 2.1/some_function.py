"""ряд функций всего приложения"""
import json
import os
import subprocess
from random import randint




def name_entry(default=" "):
    """функция которая принимает значение имени игрока
    персонаж может быть без владельца, иными словами черновик"""
    text_message = "Введите имя игрока:\n"
    players_name = input(text_message).strip()
    if players_name:
        return players_name
    else:
        return default 


def character_name_entry(default=""):
    """функция которая принимает имя персонажа
    может быть пустым, чтобы можно было придумать позже(хз как такое
    можно реализовать)"""
    text_message = "Введите имя персонажа\n"
    character_name = input(text_message).strip()
    if character_name:
        return character_name
    else:
        return default


def generation_of_characteristics():
    """функция "кидает кубики" и вычисляет
    модификаторы (вроде как хз пересмотреть потом)"""
    characteristics = {'str': '',
                       'dex': '',
                       'const': '',
                       'int': '',
                       'wisd': '',
                       'chrsm': ''}
    generation_process(characteristics)


def generation_process(characteristics):
    """рефакторная функция генерации характеристик"""
    while True:
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