class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descreptive_name(self):
        """Return neatly formatted descriptive name."""
        long_name = f"{self.make=} {self.model} {self.year}"
        return long_name.title()

my_new_car = Car('Audi', 'a4', 2019)
print(my_new_car.get_descreptive_name())