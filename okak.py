from random import randint
import math
 #просто разработка имитации приложения
#сперва попорбую разрабатывать через терминал потом займусть графикой и всем таким.

#генерация 6 массивов с 4 случайными числами от 1 до 4
"""a =[randint(1,6) for i in range(4)]"""

stats = ['str','dex','const','int','wisd','char']
character = dict.fromkeys(stats)
programm_work= True
inputs = ''
help_inf= 'Для завершения рабоыт прогарммы напишите "выход"'
help_inf += '\nДля генерации случайных характеристик введите "характеристики"'



def stts():
        print( '='*10 + 'Stats' + '=' *10)
        for stat,data in character.items():
                a = sorted(randint(1,6) for i in range(4))
                data = sum(a[1:])
                character[stat] = data
                print(stat + ': ' + str(data))

def mods():
        print('='*10 + 'Mods' + '=' *10)
        modificator = dict.fromkeys(stats)
        for stat, mod in modificator.items():
                mod = math.floor((character[stat] - 10)/2)
                if mod >=  0:
                        mod = '+' + str(mod)
                modificator[stat] = mod
                print(stat + ': ' + str(mod))
