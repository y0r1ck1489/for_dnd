from random import randint
import math
import os
import subprocess

#создание имитации рабоыт программы в терминале
#для наглядности

def show_stats_all():
        termclean()
        if characters is None or len(characters) == 0:
                print('Список данных персонажей пуст')
        else:
                print('Список данных персонажей: \n' +"Статы: " + str(characters) + "\nМодификатор" + str(modificator))

def saved_inf():
        """записывает созданные характеристики в список
        записывает как и характеристики так и модифакторы
        в список. т е создается список, элементы которого словари."""
        characters.append(character.copy())
        characters.append(modificator.copy())
        """for charact in character:
                charact = input('введите имя персонажа:')"""

def mds():
        termclean()
        #функция вычисления модификатора характеристики
        if any(value is None for value in character.values()):
                termclean()
                print('='*10 + 'data entry error' + '=' *10)
                input("Press 'Enter' to continue")
                return
                
        print('='*10 + 'Mods' + '=' *10)
        for stat, mod in modificator.items():
                mod = math.floor((character[stat] - 10)/2)
                if mod >=  0:
                        mod = '+' + str(mod)
                        modificator[stat] = mod
                        print(stat + ': ' + str(mod))
                else:
                        mod = str(mod)
                        modificator[stat] = mod
                        print(stat + ': ' + mod)
        while modif_work:
                user_agree = input('Вы хотите сохранить результат?\n').lower().strip()
                if user_agree == "да" or user_agree == 'yes':
                        saved_inf()
                        break
                elif user_agree =='нет' or user_agree == 'no':
                        print('повторите генерацию')
                        break
                else:
                        print('выполнен не корректный ввод данных.\n Повторите ввод')

def stts():
        termclean()
#генерация случайных значений для характеристик
        print( '='*10 + 'Stats' + '=' *10)
        for stat,data in character.items():
                a = sorted(randint(1,6) for _ in range(4))
                data = sum(a[1:])
                character[stat] = data
                print(stat + ': ' + str(data)) 

        while stts_work:
                user_agree = input('Вы хотите сохранить результат?\n').lower().strip()
                if user_agree == "да" or user_agree == 'yes':
                        saved_inf()
                        break
                elif user_agree =='нет' or user_agree == 'no':
                        print('повторите генерацию характеристик')
                        break
                else:
                        print('выполнен не корректный ввод данных.\n Повторите ввод')               

def termclean():
        """функция очистки экрана терминала"""
        if os.name=='nt':
                subprocess.call('cls', shell=True)
        else:
                subprocess.call('clear', shell = True)

stats = ['str','dex','const','int','wisd','char']
modificator = dict.fromkeys(stats)
character = dict.fromkeys(stats)
inp = ''
user_agree = ''
program_work = True #общая работа прогармы
characters = []
stts_work = True #работа подпрограмы со стстаи
modif_work = True #работа подпрограммы модификаторов


msg = '\nдля выхода из программы введите "выход"'
msg +='\nдля генерации характеристик введите "характеристики"'
msg +='\nдля вычисления модификатора введите "мод"'
msg +='\nчтобы показать всех персонажей введите show"\n'

while program_work:
        if inp == 'характеристики':
                stts()
        elif inp =='мод':
                mds()
        elif inp =='show':
                show_stats_all()
        elif inp == 'выход':
                program_work = False
                break
        """else:
                print("Выполнен некорректный ввод.\nПожалуйста повторите")"""
        inp = input(msg)   