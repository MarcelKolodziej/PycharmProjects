#Napisz program, który sprawdzi i wypisze na ekran, które liczby powtarzają się na liście dokładnie 3 razy

from random import randint

lista=[]
for i in range(100):
    lista.append(randint(1,200))
    print(lista[i],end=", ")
lista.sort()

print("po sortowaniu")
for i in range(100):
   print(lista[i],end=", ")

print("3 takie same")
for i in range(1, len(lista)-1):
    if (list[i-1]==lista[i] and lista[i]==lista[i+1]):
        print(lista[i], end= " ")