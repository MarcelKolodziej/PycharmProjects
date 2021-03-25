from random import randint

def function(a):
    for i in range(a):
        lista = []
        x = randint(1, 300)
        lista.append(x)
    print(lista)

b = int(input("Podaj parametr b"))
c = int(input("Podaj parametr c"))

function(3)
function(b)
function(c)
