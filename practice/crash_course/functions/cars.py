def make_car(manufacture, model, **info):
    """Stores info in dictionary about a car"""
    car_dict = {
        manufacture: "manufacture",
        model: "model"
    }
    for info, value in info.items():
        car_dict[info] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)