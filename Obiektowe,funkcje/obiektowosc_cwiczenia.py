# class Osoba:
#     imie = "Andrzej"
#     nazwisko = "Klusiewicz"
#     wiek = 33
#     pustePole = None
#
# o = Osoba()
# print(o.imie, o.nazwisko, o.wiek, o.pustePole)
#
# o=Osoba()
# o.imie='Krzysztof'
# o.nazwisko='Jarzyna'
# print(o.imie,o.nazwisko)

class Osoba:
 imie=None
 nazwisko=None
 ksywka=None
o1=Osoba()
o1.imie='Jerzy'
o1.nazwisko='Kiler'
o1.ksywka='Killer'

o2=Osoba()
o2.imie='Stefan'
o2.nazwisko='Siarzewski'
o2.ksywka='Siara' #i wszystko jasne

Osoba.imie='zamienione...'

print(o1.imie,o2.imie)
o3=Osoba()
print('o3', o3.imie)