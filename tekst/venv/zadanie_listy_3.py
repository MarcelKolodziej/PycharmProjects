#Napisz program, który wylosuje 100 liczba z przedziału <1:200> i zapisze do listy. następnie program ma wypisać na ekran ilość liczb 3-cyfrowych
from random import randint

lista = []
liczba = 0
for i in range(100):
    a=randint(1,200)
    lista.append(a)
    print(lista[i], end=", ")
for i in range(len(lista)):
    if lista[i] > 99:
        liczba += 1
print("ilosc liczb 3 cyfrowych w liscie to:" , liczba)
