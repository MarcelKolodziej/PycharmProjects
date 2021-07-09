# inheritance using when two classes are similar
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I'm {self.age} years old.")

    def speak(self):
        print("I don't know what i say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # super inherit from __init__ class
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 12)
p.speak()
c = Cat("Bill", 34, "brown")
c.show()
d = Dog("Jill", 25)
d.show()
f = Fish("Bubbles", 20)
f.speak()
