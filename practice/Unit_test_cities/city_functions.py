def get_formatted_city(city, country, population=''):
    if population:
        full_name = city + ' ' + country + "Population - " + population
    else:
        full_name = city + ' ' + country

    return full_name.title()
