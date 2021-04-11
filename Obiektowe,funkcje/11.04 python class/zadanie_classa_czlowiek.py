# Utwórz klasę Human reprezentującą człowieka, musi posiadać atrybuty takie jak
# wiek, waga, wzrost, imię i płeć. Klasa powinna także zawierać metody getAge, getWeight, getHeight, getName, isMale.

class Human:
    def __init__(self, wiek, waga, wzrost, imie, płeć):
        self.imie = imie
        self.waga = waga
        self.wzrost = wzrost
        self.wiek = wiek
        self.płeć = płeć

    def getAge(self):
        return self.wiek

    def getWeight(self):
        return self.waga

    def getHeight(self):
        return self.wzrost

    def getName(self):
        return self.imie

    def isMale(self):
        return self.płeć