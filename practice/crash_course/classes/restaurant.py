class Restaurant:
    def __init__(self, name, type ):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"Name of restaurant {self.name}, type of restaurant {self.type}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open!")


italy_rastaurant = Restaurant("PizzaBoy", "Italy")
poland_restaurant = Restaurant("Karkowka i Kaszanka", "Polish")
Japanese_restaurant = Restaurant("Ramen&Sake", "Japanese")

italy_rastaurant.describe_restaurant()
italy_rastaurant.open_restaurant()

poland_restaurant.describe_restaurant()
poland_restaurant.open_restaurant()

Japanese_restaurant.describe_restaurant()
Japanese_restaurant.open_restaurant()

