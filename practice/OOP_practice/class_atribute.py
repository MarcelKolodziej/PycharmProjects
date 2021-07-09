# Function and method arguments:

# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.

class Person:
    number_of_people = 1

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())