from random import randint
import math
import os
import subprocess

###файл для создания функций
#задача функции: создать функцию которая сохраняет в себя 

#задаю словарь со значениями предисторий
predistor = {'предистория1' : 'описание 1',
             'предистория2' : 'описание 2',
             'предистория3' : 'описание 3',
             'предистория4' : 'описание 4',
             'предистория5' : 'описание 5',
             'предистория6' : 'описание 6',
             'предистория7' : 'описание 7', 
             'предистория8' : 'описание 8',
             'предистория9' : 'описание 9',
             'предистория10' : 'описание 10',
             'предистория11' : 'описание 11',
             'предистория12' : 'описание 12',
             'предистория13' : 'описание 13',}

warrior = {
    'описание' :'текст1',
    'умения': {'боевой стиль' : 'Описание1',
               'второе дыхание' : 'Описание2'}
}
klass = [warrior]
human = {'умения' :'описание'}
rase = [human]
character = {}
name = ''
def character_inf():

stats = ['str','dex','const','int','wisd','char']
char_stats= dict.fromkeys(stats)
characters = [] #работа подпрограмы со стстаи


def saved_inf():
        """записывает созданные характеристики в список
        записывает как и характеристики так и модифакторы
        в список. т е создается список, элементы которого словари."""
        for character in characters:
                character = {'имя' : name , #имя
                             'класс' : klass, #класс
                             'раса' : rase ,#раса
                             'характеристики' : stats, #характеристиики
                             'модификаторы' :  '''словарь модификаторов''', #дрьавленные модификаторы
                             'предистория' : predistor} 
                
        characters.append(stats.copy())
'''        elif characters > 3:
                characters.append(character.copy())
                del characters[-1]
                print('превышено количество персонажей\n' 
                'последний ваш персонаж не сохранен')'''
"""for charact in character:
                charact = input('введите имя персонажа:')"""

def input_name():
        while True:
                name = str(input("введите имя персонажа")).strip()
                user_agree = input('Вам нравится имя персонажа?\n').lower().strip()
                print(name)
                if user_agree == "да" or user_agree == 'yes':
                        
                        saved_inf()
                        break
                elif user_agree =='нет' or user_agree == 'no':
                        print('повторите генерацию характеристик')
                        break
                else:
                        print('выполнен не корректный ввод данных.\n Повторите ввод')  



def stts():
        termclean()
#генерация случайных значений для характеристик
        print( '='*10 + 'Stats' + '=' *10)
        for stat in stats:
                a = sorted(randint(1,6) for _ in range(4))
                stats[stat] = sum(a[1:])
                print(stat + ': ' + str(stats[stat])) 

        while True:
                user_agree = input('Вы хотите сохранить результат?\n').lower().strip()
                if user_agree == "да" or user_agree == 'yes':
                        saved_inf()
                        break
                elif user_agree =='нет' or user_agree == 'no':
                        print('повторите генерацию характеристик')
                        break
                else:
                        print('выполнен не корректный ввод данных.\n Повторите ввод')               


def mds():
        termclean()
        #функция вычисления модификатора характеристики
        if any(value is None for value in stats.values()):
                termclean()
                print('='*10 + 'data entry error' + '=' *10)
                input("Press 'Enter' to continue")
                return
                
        print('='*10 + 'Mods' + '=' *10)
        for stat, mod in stats.items():
                mod = math.floor((stats[stat] - 10)/2)
                if mod >=  0:
                        mod = '+' + str(mod)
                        print(stat + ': ' + str(mod))
                else:
                        mod = str(mod)
                        print(stat + ': ' + mod)

def termclean():
        """функция очистки экрана терминала"""
        if os.name=='nt':
                subprocess.call('cls', shell=True)
        else:
                subprocess.call('clear', shell = True)