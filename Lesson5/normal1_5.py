import os
import easyLess5

exitos ='a'
while exitos != '0':
    print('Перейти в папку - нажмите 1')
    print('Содержимое текущей папки - нажмите 2')
    print('Удаление папки - нажмите 3')
    print('Создание папки - нажмите 4')
    print('Выход - нажмите 0')
    exitos = input('нажмите: ' )
    print(exitos)
    if exitos == '1':
        dir_name = input ('Введите полный путь папки: ')
        easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('Введите полный путь папки: ')
        easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('Введите полный путь папки: ')
        easy.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('неверный выбор')