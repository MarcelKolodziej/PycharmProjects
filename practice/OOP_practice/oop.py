# Object Orientated Programming in Python from youtube clip 'https://www.youtube.com/watch?v=JeznW_7DlB0'

class Dog:
    # special method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

d = Dog("Tim", 43)
print(d.get_name())
d2 = Dog("Bill", 11)
print(d2.get_name())
