# Object Orientated Programming in Python from youtube clip 'https://www.youtube.com/watch?v=JeznW_7DlB0'

class Dog:
    # special method
    def __init__(self, name):
        self.name = name
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Tim")
