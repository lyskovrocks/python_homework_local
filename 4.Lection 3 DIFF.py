"""
Сделать функцию, которая считает разницу чисел,
добавить проверки в функции, вернуть результат.
Если результат меньше 0 - вернуть 0
"""


def subtraction(a, b):
    try:
        if a < b:
            return 0
        else:
            return a - b
    except BaseException as e:
        print("Ошибка ввода")
print(subtraction('К',8))
