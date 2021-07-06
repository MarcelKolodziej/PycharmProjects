from city_functions import get_formatted_city
""" Program should return single
formatted string from Inputs City and Country """

print("Enter q for quit")
while True:
    city = input("Enter city name: ")
    if city == 'q':
        break
    country = input("Enter country name: ")
    if country == 'q':
        break
    population = input("Enter population: ")
    if population == 'q':
        break

    formatted_country = get_formatted_city(city, country, population)
    print("\tNeatly formatted country: " + formatted_country + ".")