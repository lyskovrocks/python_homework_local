film = {}
film_list = []

for i in range(2):
    film['name'] = input('Введите название фильма: ')
    film['len'] = input('Введите длительность(мин) фильма: ')
    film['year'] = int(input('Введите год фильма: '))
    film['rate'] = float(input('Введите рэйтинг фильма: '))
    film_list.append(film.copy())
    # film.clear()
print('Ваши фильмы в очереди:\n', film_list)
