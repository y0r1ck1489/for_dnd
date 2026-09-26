"""модуль общих функций"""
import os
import subprocess


# функция для отображения списков
def user_chose(items):
    """функция корретного отображения списка"""
    for i, choose in enumerate(items, start=1):
        print(f"{i}.{choose.capitalize()}")


# функция генерации шапочки
def header():
    """делает просто красивую шапочку"""
    uzor = "=" * 10
    title = "CHARACTER MAKER"
    head = f"{uzor} {title} {uzor}"
    print(head)


# функция очистки экрана
def clean_screen():
    """функция очищающая терминал"""
    if os.name == "nt":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)
