year_dict = {
    "max_year": {
        "year": '',
        "count": 0
    },
    "years": {}
}

def create_or_update(year, years):
    if year in years['years']:
        years['years'][year] += 1
        if years['years'][year] > years['max_year']['count']:
            years['max_year']['year'] = year
            years['max_year']['count'] = years['years'][year]
    else:
        years['years'].update({year: 1})