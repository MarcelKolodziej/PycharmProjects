from random import randint

lista=[]
for i in range(200):
    lista.append(randint(1,50))

for i in range(200):
    suma=0
    for j in range(200):
        if lista[i]==lista[j]:
            suma+=1
    print(lista[i]," = ",suma)