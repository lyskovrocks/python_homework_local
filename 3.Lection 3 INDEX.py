"""
В данной программе считается количество пробелов в строке str_var.
Задачи
1. Заменить пробел на букву 'o'
2. Добавить в программу ввод буквы для поиска
3. Добавить вывод списка индексов(где находится) буква для поиска  # enumerate

Дополнительно
# Завершение прошраммы exit('Какой нибудь текст перед концом')
4. Сделать проверку на то, чтобы для поиска использовался 1 символ
5. Вывести строку без символов, который ищется
6. Сделать программу которая будет спрашивать: Хотите найти ещё один символ?
"""

# str_var = "hello, how are you!?"
# char_count = 0
# var_index = []
# str_var = str_var.replace(' ','o')
# var_find_char = input('Введите символ для поиска:')
# for char in str_var:
#     if char == var_find_char:
#         char_count += 1
#         var_index.append(str_var.index(char))
#
# print(f"Количество = {char_count}")
# print(f'Индексы символа {var_find_char}: {var_index}')


str_var = "hello, how are you!?"
ask = 'y'
str_var = str_var.replace(' ', 'o')

while ask == 'y':
    char_count = 0
    var_index = []
    var_find_char = input('Введите символ для поиска:')
    if len(var_find_char) < 2:
        for index, char in enumerate(str_var):
            if char == var_find_char:
                char_count += 1
                var_index.append(index)
    else:
        exit('Необходимо ввести один символ')
    print(f"Количество = {char_count}")
    print(f'Индексы символа {var_find_char}: {var_index}')

    new_str_var = str_var.replace(var_find_char, '')
    print(new_str_var)

    ask = input('\nХотите ввести еще один символ? (y/n)')



exit('the end')
