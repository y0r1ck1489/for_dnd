#функция добавления имени я словарь
name = input('введите имя персонажа')
agree = input('вам нравится имя?').lower().strip()
while True:
    if agree == 'да' or agree == 'yes':
        saved_inf()
        break
    elif agree == 'нет' or agree =='no':
        print('введите имя снова')
        break
    else:
        print('выполнен не корректный ввод данных.\n Повторите ввод')               # хз что это