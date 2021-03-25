#Mapisz program który wylosuje do listy 200 liczb z przedziału <100,500>
# program ma policzyć średnią liczb parzystych i nieparzystych.
from random import randint

lista=[]
for i in range(200):
    lista.append(randint(100,500))

a= 0
y= 0
b= 0
x= 0

for i in range(200):
    if lista[i]%2==0:
        a += lista[i]
        y += 1
srednia=(a/y)
print("srednia liczb parzystych: ", srednia )

for i in range(200):
    if lista[i]%2==0:
        b += lista[i]
        x += 1
srednia2=(b/x)
print("srednia liczb nieparzystych: ", srednia2 )