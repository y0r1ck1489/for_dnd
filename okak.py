from random import randint
import math
import os
import subprocess
 #создание имитации рабоыт программы в терминале
#для наглядности
stats = ['str','dex','const','int','wisd','char']
character = dict.fromkeys(stats)
program_work = True
inp = ''
msg = '\nдля выхода из программы введите "выход"'
msg +='\nдля генерации характеристик введите "характеристики"'
msg +='\nдля вычисления модификатора введите "мод"\n'
def termclean():
        """функция очистки экрана терминала"""
        if os.name=='nt':
                subprocess.call('cls', shell=True)
        else:
                subprocess.call('clear', shell = True)    
def stts():
        termclean()
        #генерация случайных значений для характеристик
        print( '='*10 + 'Stats' + '=' *10)
        for stat,data in character.items():
                a = sorted(randint(1,6) for i in range(4))
                data = sum(a[1:])
                character[stat] = data
                print(stat + ': ' + str(data))
def mds():
        termclean()
        #функция вычисления модификатора характеристики
        print('='*10 + 'Mods' + '=' *10)
        modificator = dict.fromkeys(stats)
        for stat, mod in modificator.items():
                mod = math.floor((character[stat] - 10)/2)
                if mod >=  0:
                        mod = '+' + str(mod)
                modificator[stat] = mod
                print(stat + ': ' + str(mod))
while program_work:
        if inp == 'характеристики':
                stts()
        elif inp =='мод':
                mds()
        elif inp == 'выход':
                program_work = False
                break
        inp = input(msg)