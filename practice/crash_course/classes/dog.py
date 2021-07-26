class Dog:
    """A simple atemp to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting in response to command."""
        print(f'{self.name} is now sitting')

    def roll_over(self):
        """Simulate dog roll over command"""
        print(f'{self.name} is rolling over')

# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
my_dog = Dog('Willie', 4)
my_dog.roll_over()