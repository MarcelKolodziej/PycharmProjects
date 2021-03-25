from random import randint

lista=[]
for i in range(10):
    a=randint(1,100)
    lista.append(a)
    print(lista[i], end=", ")
a=int(input("podaj a"))
b=int(input("podaj b"))
ile=0
for i in range(10):
    if lista[i]>=a and lista[i]<=b:
        ile+=1
print("liczb z przedzialu a i b jest = ",ile)