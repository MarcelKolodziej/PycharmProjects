# Zad. Zamówienie
#
# 1. Napisać program do obsługi zamówień. Program powinien składać się z dwóch
#
# klas: Zamowienie oraz Pozycja , przy czym każde zamówienie zawierać może
#
# jedną lub więcej pozycji.
#

#
# Klasa Zamowienie powinna zawierać następujące pola:
#
# • pozycje (tablica obiektów kl. Pozycja) – pozycje składowe zamówienia,
#
# • ileDodanych (int) – liczba pozycji w zamówieniu,
#
# • maksRozmiar (int) – maksymalna liczba pozycji w zamówieniu
#
# oraz metody:
#
# • konstruktor bezparametrowy – maksRozmiar ustalany na wartość 10,
#
# • konstruktor z parametrem określającym maksymalną liczbę pozycji w zamówieniu,
#
# • metodę dodajPozycje(Pozycja p) , która dodaje podaną pozycję do
#
# zamówienia,
#
# • metodę double obliczWartosc() zwracającą wartość zamówienia,
#
# • metodę String toString() , która zwraca łańcuch zawierający spis pozycji
#
# zamówienia oraz łączną wartość zamówienia
#
# Przykładowy wynik:
#
# Chleb 3,50 zł 1 szt. 3,50 zł
#
# Cukier 4,00 zł 3 szt. 12,00 zł
#
# Zamówienie:
#
# Chleb 3,50 zł 1 szt. 3,50 zł
#
# Cukier 4,00 zł 3 szt. 12,00 zł
#
# Razem: 15,50 zł
#
# 2. W klasie Zamowienie :
#
# • zaimplementować metodę usunPozycje(int indeks) , która usuwa
#
# z zamówienia pozycję o podanym indeksie
#
# • zaimplementować metodę edytujPozycje(int indeks) , która umożliwi
#
# edycję wybranej pozycji zamówienia, tj. nazwy towaru, ceny oraz liczby
#
# sztuk
#
# • zmodyfikować metodę dodajPozycje(Pozycja p) , tak by w sytuacji,
#
# gdy dodawany jest ten sam towar nie dodawała kolejnej pozycji, lecz
#
# zwiększała liczbę sztuk w już istniejącej
#
# 3. W klasie Pozycja :
#
# • zaimplementować metodę double obliczWartoscZRabatem , która oblicza
#
# wartość pozycji zamówienia po uwzględnieniu rabatu zależnego od liczby
#
# sztuk:
#
# – 5–10 szt. rabat 5%,
#
# – 10–20 szt. rabat 10
#
# – powyżej 20 szt. rabat 15%.
#
# 4. Zmodyfikować metodę obliczWartosc w klasie Zamowienie, tak by również wyświetlała
#
# informacje o rabacie i łączny koszt zamówienia po jego uwzględnieniu.
#
# 5. zmodyfikować metodę toString , by wyświetlała również naliczony rabat i wartość
#
# z rabatem.

from random import randint

done = False

class listaZakupow:
    def __init__(self):
        self.produkty = []

    def dodajDoKoszyka(self, produkt):
        self.produkt.append(produkt)

    def usunZKoszyka(self, produkt_index):
        self.produkt.pop(produkt_index)

    def cenaKoszyka(self):
        cena = 0
        for x in self.produkty:
            cena = cena + x.cena
        return cena

    def listaProduktow(self):
        cid = 0
        print("Lista produktów:")
        for x in self.produkty:
            print(x.nazwa, x.cena.cid)
            cid = cid+1
        print("")

class Produkt:
    def __init__(self, cena, nazwa):
        self.cena = cena
        self.nazwa = nazwa


sklep = []
nazwaProduktow = ["Chleb" , "Cukier" , "Maka" , "Jaja"]

def stworzProdukty(amt):
    iloscProduktow = 0
    while iloscProduktow <= amt:
        nProdukt = Produkt(randint(1, 50), nazwaProduktow[randint(0, len(nazwaProduktow) - 1)])
        sklep.append(nProdukt)
        iloscProduktow = iloscProduktow + 1

def StworzSklep(dokument_tekstowy):
    try:
        fx = open(dokument_tekstowy, "r")
        str1 = ""
        str1 = dokument_tekstowy.read()
    except IOError:
        print("Brak sklepu,... tworzenie produktow")
        stworzProdukty(2)

def listaSklepu():
    iid = 0
    for x in sklep:
        print(iid, x.cena, x.nazwa)
        iid = iid + 1

def WypiszInstrukcje():
    print("C by zobaczyć Twój koszyk")
    print("R by usunac z koszyka")
    print("Wpisz liczbe by dodac produkt")
    print("Wpisz P by zobaczyc aktualna cene koszyka")
    print("X wyjscie <-----")

def usunProdukt(koszyk):
    input1 = input("Wpisz ID produktu by go usunac")
    koszyk.usunZKoszyka(input1)

def handleInput(in_var, koszyk):
	lista_klawiszy = ["C","R","P","X"]
	if(in_var == "C"):
		koszyk.listaProduktow()
	if(in_var == "R"):
		usunProdukt(koszyk)
	if(in_var == "P"):
		print("Obecna cena za koszyk")
		print(koszyk.cenaKoszyka())
	if(in_var == "X"): # wyjscie
		global done
		done = True
	if in_var not in lista_klawiszy:
		try:
			koszyk.dodajDoKoszyka(sklep[int(in_var)])
		except:
			print("Wybrales zla komende!")

koszyk1 = listaZakupow()
StworzSklep("koszyk1.listaZakupow")

while(done == False):
    listaSklepu()
    WypiszInstrukcje()
    input_var = input("Wybierz produkt do kupienia(Wpisz id)")
    handleInput(input_var, koszyk1)