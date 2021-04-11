class auto:
    kolor = ""
    rok = 1993

class samochod(auto):
    przebieg=None

samochodzik = samochod()

samochodzik.kolor="zielony"
samochodzik.rok_produkcji = 2015
samochodzik.przebieg = 252121
print(samochodzik.przebieg)
print(samochodzik.kolor)
print(samochodzik.rok_produkcji)
samochodzik.wyswietl()
