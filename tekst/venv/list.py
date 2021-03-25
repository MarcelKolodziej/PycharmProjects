#wylosuj do listy 10 elementów losowych z przedziału <1;100> i wyświetl z listy tylko elementu parzyste wraz z indeksami
import random
lista = []

for i in range(10):
    n = random.randint(1,100)
    lista.append(n)
    if lista[i]%2 == 0:
        print(lista[i], end="")