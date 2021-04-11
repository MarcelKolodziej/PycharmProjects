# Utwórz klasę reprezentującą prostokąt, musi posiadać atrybuty długość i szerokość. Klasa powinna posiadać metody obliczające pole, obwód i długość przekątnej.

import math
class MyNumber:
    def __init__(self,number):
        self.number = number

    def MyNumber_isOdd(self):
        if (self.number % 3) == 0:
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
    newNumber = MyNumber(6)
    print(newNumber.MyNumber_isOdd())
    print(newNumber.MyNumber_isEven())
    print(newNumber.MyNumber_sqrt())
    print(newNumber.MyNumber_pow(2))
    print(newNumber.MyNumber_add(3))
    print(newNumber.MyNumber_subtract(3))

if __name__ == '__main__':
    main()

