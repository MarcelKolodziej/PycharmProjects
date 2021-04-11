from math import sqrt

# Function return square value of a,b,c
# $ax^2$+bx+c
class square_fun:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        delta = (self.b)**2 - 4*(self.a) * (self.c)
        print(delta)

        if delta > 0:
            y1 = (-self.b - sqrt(delta))/(2*self.c)
            y2 = (-self.b + sqrt(delta))/(2*self.a)
            print("function has 2 zero places", "y1 = ", y1, "y2 = ", y2)

        if delta == 0:
            y = (-self.b)/(2*self.a)
            print("function has 1 zero places", "y0 = ", y)

        if delta < 0:
            print("no zero places")

        if self.a == 0:
            print("its not square function")

square_fun1 = square_fun(1,5,2)
print(square_fun1.delta())