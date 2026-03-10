"""Модуль для генерации характеристик персонажей для настольных игр."""
from random import randint
import math
import os
import subprocess

# создание имитации рабоыт программы в терминале
# для наглядности
# во время ращработки программы функции тестировать в отдельном файликах, чтобы
# не отвлекаться на работу основной программы
# добавить следующие функции: функции ввода имени и запоминания в
# словаре персонажn+1,
# добавть возможность добавления ключей словарей таких как раса класс и
# предистория в качестве значений в словарь персонаж
# примерный результат программы должен быть в виде списка словарей в
# которых отображена вся информация о герое/ях


def show_stats_all():
    """отображение информации о персонаже/жах"""
    termclean()
# прописать "процесс" пока список персонажей не равен 3
# программа должна работать и продолжать ввод
# персонажей если персонажей будет больше 3
# программа должна вывести сообщение о том что
# привышен лимит персонажей
    if characters is None or len(characters) == 0:
        print('Список данных персонажей пуст')
    else:
        print('список персонажей: ')
        for idx, char_data in enumerate(characters, 1):
            print('\nперсонаж ' + str(idx))
            print('=' * 29 + 'Stats' + '=' * 35)
            print(char_data)
            print('='*68)
            print('=' * 10 + 'mods' + '=' * 10)
            for stat, value in char_data.items():
                mod = math.floor((value - 10)/2)
                if mod >= 0:
                    mod = '+' + str(mod)
                    print(stat + ': ' + str(mod))
                else:
                    mod = str(mod)
                    print(stat + ': ' + mod)
            print('=' * 10 + 'end' + '=' * 11)


def saved_inf():
    """записывает созданные характеристики в список
        записывает как и характеристики так и модифакторы
        в список. т е создается список, элементы которого словари."""
    characters.append(character.copy())
# '''        elif characters > 3:
#                characters.append(character.copy())
#                del characters[-1]
#                print('превышено количество персонажей\n'
#                'последний ваш персонаж не сохранен')'''
# """for charact in character:
#                charact = input('введите имя персонажа:')"""


def mds():
    """функция для вычисления мод"""
    termclean()  # функция вычисления модификатора характеристики
    if any(value is None for value in character.values()):
        termclean()
        print('=' * 10 + 'data entry error' + '=' * 10)
        input("Press 'Enter' to continue")
        return
    print('=' * 10 + 'Mods' + '=' * 10)
    for stat, mod in character.items():
        mod = math.floor((character[stat] - 10)/2)
        if mod >= 0:
            mod = '+' + str(mod)
            print(stat + ': ' + str(mod))
        else:
            mod = str(mod)
            print(stat + ': ' + mod)


def stts():
    """генерация статов"""
    termclean()  # генерация случайных значений для характеристик
    print('=' * 10 + 'Stats' + '=' * 10)
    for stat in character:
        a_dice = sorted(randint(1, 6) for _ in range(4))
        character[stat] = sum(a_dice[1:])
        print(stat + ': ' + str(character[stat]))
    while True:
        USER_AGREE = input('Сохранить результат?\n').lower().strip() # исправить ошибку стиоя
        if USER_AGREE == "да" or USER_AGREE == 'yes':
            saved_inf()
            break
        elif USER_AGREE == 'нет' or USER_AGREE == 'no':
            print('повторите генерацию характеристик')
            break
        else:
            print('выполнен не корректный ввод данных.\n Повторите ввод')


def termclean():
    """функция очистки экрана терминала"""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


stats = ['str', 'dex', 'const', 'int', 'wisd', 'char']
"""modificator = dict.fromkeys(stats)"""
character = dict.fromkeys(stats)
INP = ''
USER_AGREE = ''
PROGRAM_WORK = True  # общая работа прогармы
characters: list[dict] = []  # работа подпрограмы со стстаи
MSG = '\nдля выхода из программы введите "выход"'
MSG += '\nдля генерации характеристик введите "характеристики"'
MSG += '\nдля вычисления модификатора введите "мод"'
MSG += '\nчтобы показать всех персонажей введите show"\n'


while PROGRAM_WORK:
    INP = input(MSG).strip().lower()
    if INP == 'характеристики':
        stts()
    elif INP == 'мод':
        mds()
    elif INP == 'show':
        show_stats_all()
    elif INP == 'выход':
        PROGRAM_WORK = False
    else:
        print("Выполнен некорректный ввод.\nПожалуйста повторите")
