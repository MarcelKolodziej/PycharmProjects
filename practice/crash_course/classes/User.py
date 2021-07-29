class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, age, gender, height, weight):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


    def describe_user(self):
        """Display summary of user's information"""
        print(f"First Name:{self.first_name},\n last Name:{self.last_name},\n Age:{self.age},\n Gender:{self.gender},\n"
              f"Height:{self.height}cm, Weight:{self.weight}kg")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}!")


user_Jacob = User('Jacob', 'Dyrda', 28, 'Male', 180, 80)
user_Jacob.describe_user()
user_Jacob.greet_user()

user_Kamil = User('Kamil', "Papała", 14, "Male", 150, 40)
user_Kamil.describe_user()
user_Kamil.greet_user()