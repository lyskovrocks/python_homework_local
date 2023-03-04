from films import film_list

#---------------------------------------Поиск фильмов по рэйтингу------------------------------------------------------
# high_rate = []
# var_rating = 8.9
# for f in film_list:
#     if f['rating'] > var_rating:
#         high_rate.append(f['title'])
# print(f'Найдено {len(high_rate)} фильмов с рейтингом выше {var_rating}:')
# for i,f in enumerate(high_rate):
#     print(f'{i+1}. {f}')

#-----------------------------------------Поиск фильма по годам--------------------------------------------------------
film_year = []
min_year = 2003
max_year = 2005
for f in film_list:
    if f['year'] >= min_year and f['year'] <= max_year:
        film_year.append(f['title'])
print(f'Найдено {len(film_year)} фильмов с {min_year} по {max_year} года:')
for i,f in enumerate(film_year):
    print(f'{i+1}. {f}')

#--------------------------------------Cамый часто встречающийся год---------------------------------------------------
year_list = []
max_rep = 0
max_rep_year = 0
for f in film_list:
    year_list.append(f['year'])
for y in year_list:
    if year_list.count(y) > max_rep:
        max_rep = year_list.count(y)
        max_rep_year = y
print(f'Cамый часто встречающийся год: {max_rep_year}, ({max_rep} раз)')

#--------------------------------------------------------THE----------------------------------------------------------

for f in film_list:
    if 'the' in f['title'][:3] or 'The' in f['title'][:3]:      # Если нужно найти любое 'the', даже в середине слова,
        print(f['title'])                                       # нужно убрать срез


#--------------------------------------------------------Star Wars-----------------------------------------------------

for f in film_list:
    if 'Star Wars' in f['title']:
        print(f'Позиция в топе: {f["top 250 rank"]}. Фильм: {f["title"]}')



