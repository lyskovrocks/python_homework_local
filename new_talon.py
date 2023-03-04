from random import randint

first_name = input('Добрый день! Оформление записи к врачу:\nВведите ваше имя:')
last_name = input('Введите вашу фамилию:')
age = int(input('Введите ваш возраст:'))
wt = float(input('Введите ваш вес:'))
comment = input('Введите комментарий:')


print(f"{first_name} {last_name}, вы назначены к врачу.\nВаш номер талона № {randint(0,1000)}")