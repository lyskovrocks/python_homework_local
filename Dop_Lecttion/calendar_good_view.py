"""
СЛОЖНЫЙ УРОВЕНЬ

Функция должна принимать неотсортированный список из 0-7 элементов.
Если список пуст, он просто возвращает пустой массив.
В противном случае он должен составить
отсортированное удобное для человека расписание
рабочего времени и вернуть его как string.

Формат вывода за один
день должен быть ВС: 11:00 - 23:00.

Если два или более дней недели подряд имеют
одинаковые рабочие часы, они должны быть объединены
и иметь следующий формат: ПН - СР: 11:00 - 23:00.
ИНФОРМАЦИЯ
Метод sort у списка переделывает в сортированный список
По стандарту - идёт сортировка от меньшего к большему,
в алфавите от a до z и тд.
Если мы сортируем список из элементов составных типов данных,
то нам нужно указать по какой логике будет идти сортировка
для этого есть аргумент key. Посмотрите файл list_sort в папке info.
"""


def reformat_date(date_list: list):
    week = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    date_list.sort(key=lambda x: x['day'])  # Сортировка по значнию ключа day
    list_interval = []
    # str_date_list = ''
    for d in date_list:
        d['day'] = week[d['day']]  # Замена чисел на дни недели
        d['interval'] = d['from'] + ' - ' + d['to'] # добавление интервалов в словарь

    list_interval.append(date_list[0]['day'] + ': ' + date_list[0]['interval'])
    list_interval += [(date_list[1]['day'] + ': ' + date_list[1]['interval'])]
    # в цикле использовать срез для поиска интервала предыдущего дня
    print(list_interval)
    for d1, d2 in zip(date_list, date_list[1:]):
        if d2['interval'] == d1['interval']:
            if d2['interval'] in dict_interval:
                dict_interval[d2['interval']] += d2['day']
            else:
                dict_interval[d2['interval']] = d2['day']
        else:
            dict_interval[d2['interval']] = d2['day']
    print(dict_interval)

    #     dict_interval[d1['from'] + d1['to']] = d1['day']
    #     # if d1['from'] == d2['from'] and d1['to'] == d2['to']:









    # str_date_list += d['day'] + ': ' + d['from'] + ' - ' + d['to'] + '\n'
    # print(str_date_list)

    return date_list


print(reformat_date([
    {
        "day": 6,
        "from": "10:00",
        "to": "23:00"
    },
    {
        "day": 0,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 1,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 2,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 3,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 4,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 5,
        "from": "11:00",
        "to": "23:00"
    }
]))

## На консоле должно быть
# ПН - СР: 11:00 - 23:00
# ЧТ - ПТ: 12:00 - 23:00
# СБ: 10:00 - 23:00
# ВС: 11:00 - 23:00
