# Utwórz klasę o nazwie MyNumber, której jedyny konstruktor przyjmuje liczbę. Klasa powinna mieć następujące metody
# MyNumber isOdd() – true jeśli atrybut jest nieparzysty,
# MyNumber isEven() – true jeśli atrybut jest parzysty,
# MyNumber sqrt() – pierwiastek z atrybutu,
# MyNumber pow(MyNumber x) – atrybut podniesiony do potęgi x (przydatnej metody poszukaj w javadoc do klasy Math),
# MyNumber add(MyNumber x) – zwraca sumę atrybutu i x opakowaną w klasę MyNumber,
# MyNumber subtract(MyNumber x) – zwraca różnicę atrybutu i x opakowaną w klasę MyNumber.

import math
class MyNumber:
    def __init__(self,number):
        self.number = number

    def MyNumber_isOdd(self):
        if (self.number % 2) == 1:
            return True
        else:
            return False

    def MyNumber_isEven(self):
        if (self.number % 2) == 0:
            return True
        else:
            return False

    def MyNumber_sqrt(self):
        return math.sqrt(self.number)

    def MyNumber_pow(self, potega):
        return self.number**potega

    def MyNumber_add(self, liczba):
        return self.number + liczba

    def MyNumber_subtract(self, liczbaOdejmowanie):
        return self.number - liczbaOdejmowanie

def main():
    newNumber = MyNumber(8)
    print(newNumber.MyNumber_isOdd())
    print(newNumber.MyNumber_isEven())
    print(newNumber.MyNumber_sqrt())
    print(newNumber.MyNumber_pow(2))
    print(newNumber.MyNumber_add(3))
    print(newNumber.MyNumber_subtract(3))

if __name__ == '__main__':
    main()
