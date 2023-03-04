from films import film_list
from year_count import create_or_update, year_dict

high_rate = []
var_rating = 8.9
var_the = []
film_year = []
star_wars = []
year_list = []
max_rep = 0
max_rep_year = 0


for f in film_list:
    if f['rating'] > var_rating:
        high_rate.append(f['title'])

    if 2001 <= f['year'] <= 2005:
        film_year.append(f['title'])

    create_or_update(f['year'], year_dict)

    if f['title'].lower().find('the') != -1:
        var_the.append(f['title'])

    if 'Star Wars' in f['title']:
        star_wars.append(f'Позиция в топе: {f["top 250 rank"]}. Фильм: {f["title"]}')

print(f'Найдено {len(high_rate)} фильмов с рейтингом выше {var_rating}:')
for i, f in enumerate(high_rate):
    print(f'{i + 1}. {f}')

print(f'\nНайдено {len(film_year)} фильмов с {2001} по {2005} года:')
for i, f in enumerate(film_year):
    print(f'{i + 1}. {f}')

print(f'\nCамый часто встречающийся год: {year_dict["max_year"]["year"]}, ({year_dict["max_year"]["count"]} раз)')

# print('\nФильмы с THE в названии:')
# for t in var_the:
#     print(t)
#
# print("\nStar Wars:")
# for f in star_wars:
#     print(f)

