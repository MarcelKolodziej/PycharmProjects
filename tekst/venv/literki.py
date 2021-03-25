#Wpisz 5 imion i wypisz ile jest imion rzeńskich

lista_imion = ["Bartek" , "Arnold" ,"Emilka" , "Mieczysław" , "Beata"]
print("wypisz liste: ", lista_imion)
print("wypisz liste 1 slowo z listy: ", lista_imion[0])
print("wypisz ostatnia literke", lista_imion[0][len(lista_imion)])

imiona = 0
for x in range(len(lista_imion)):
    if lista_imion[x][len(lista_imion[x]) -1] == "a":

print("Suma rzenskich imion:",imiona)