# Utwórz klasę reprezentującą prostokąt, musi posiadać atrybuty długość i szerokość. Klasa powinna posiadać metody obliczające pole, obwód i długość przekątnej.

import math

class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def obliczPole(self):
        return self.dlugosc * self.szerokosc

    def ObwodProstokata(self):
        return 2*self.dlugosc + 2*self.szerokosc

    def PrzekatnaProstokata(self):
        return math.sqrt((self.dlugosc**2 + self.szerokosc**2))

nowyProstokat = Prostokat(4, 10)
print(nowyProstokat.obliczPole())
print(nowyProstokat.ObwodProstokata())
print(nowyProstokat.PrzekatnaProstokata())