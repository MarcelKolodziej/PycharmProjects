from random import randint

lista=[]
for i in range(100):
    lista.append(randint(1,200))
    print(lista[i],end=", ")
lista.sort()
print("po sortowaniu")
for i in range(100):
   print(lista[i],end=", ")
print("unikaty")
for i in range(len(lista)):
    if i==0:
        if (lista[i] != lista[i + 1]):
            print(lista[i],end=", ")
    elif i==len(lista)-1:
        if (lista[i - 1] != lista[i]):
            print(lista[i],end=", ")
    else:
        if (lista[i-1]!=lista[i] and lista[i]!=lista[i+1]):
            print(lista[i],end=", ")