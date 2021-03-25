#Podaj liczbe, zrob tabliczke mnozenia do 10
liczba = int(input("podaj liczbe"))

for i in range(1, liczba):
   for j in range(1,liczba):
      print(i * j, end='\t')
   print()
