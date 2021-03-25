#Oblicz sumę cyfr z wprowadzonej liczby
liczba = int(input("Wprowadz liczbe"))

suma = 0
for i in str(liczba):
    suma += int(i)

print(suma)

