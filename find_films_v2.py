from films import film_list

high_rate = []
var_rating = 8.9
var_the = []
film_year = []
min_year = 2003
max_year = 2005
star_wars = []
year_list = []
max_rep = 0
max_rep_year = 0
year_dict = {}


for f in film_list:
    if f['rating'] > var_rating:
        high_rate.append(f['title'])

    if min_year <= f['year'] <= max_year:
        film_year.append(f['title'])

    year_list.append(f['year'])

    if f['title'].lower().find('the') != -1:
        var_the.append(f['title'])

    if 'Star Wars' in f['title']:
        star_wars.append(f'Позиция в топе: {f["top 250 rank"]}. Фильм: {f["title"]}')

print(f'Найдено {len(high_rate)} фильмов с рейтингом выше {var_rating}:')
for i, f in enumerate(high_rate):
    print(f'{i + 1}. {f}')

print(f'\nНайдено {len(film_year)} фильмов с {min_year} по {max_year} года:')
for i, f in enumerate(film_year):
    print(f'{i + 1}. {f}')

for y in year_list:
    if year_list.count(y) > max_rep:
        max_rep = year_list.count(y)
        max_rep_year = y
print(f'\nCамый часто встречающийся год: {max_rep_year}, ({max_rep} раз)')

print('\nФильмы с THE в названии:')
for t in var_the:
    print(t)

print("\nStar Wars:")
for f in star_wars:
    print(f)
