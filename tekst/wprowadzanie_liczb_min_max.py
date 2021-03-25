# Użytkownik ma wprowadzić cyfre X gdzie cyfra ta jest suma wszystkich liczb które wprowdzamy, potem wyciagamy minimalna i maksymalna.

liczba_ile_razy = int(input("Wprowadz ilosc liczb"))  #do petli ile razy ma sie wykonac

for i in range(liczba_ile_razy):
    new = int(input("Wpisz liczbe"))
    if i == 0:
        min = new
        max = new
    elif max < new:
        max = new
    if min > new:
        min = new
print("max = ", max, "\n min= ", min)