class Pozycja:

    def __init__(self, nazwaTowaru, ileSztuk, cena):
        self.nazwaTowaru = nazwaTowaru
        self.ileSztuk = ileSztuk
        self.cena = round(float(cena), 2)

    def obliczWartosc(self):
        return self.ileSztuk * self.cena

    def wartoscZrabatem(self):
        if self.ileSztuk >= 5 and self.ileSztuk < 10:
            return self.ileSztuk * self.cena * 0.95
        elif self.ileSztuk >= 10 and self.ileSztuk < 20:
            return self.ileSztuk * self.cena * 0.90
        elif self.ileSztuk >= 20:
            return self.ileSztuk * self.cena * 0.85
    def toString(self):
        lancuch = ''
        if len(self.nazwaTowaru) > 20:
            lancuch += self.nazwaTowaru[:20:]
        else:
            lancuch += self.nazwaTowaru
        lancuch = lancuch + ' ' + str(self.ileSztuk) + ' szt. ' + str(self.cena) + ' zl ' + str(self.obliczWartosc()) + ' zl ' + str(self.wartoscZrabatem()) + ' zl'
        return lancuch

class Zamowienie:

    def __init__(self):
        self.pozycje = []
        self.ileDodanych = len(self.pozycje)
        self.maksRozmiar = None
    def maks(self):
        self.maksRozmiar = 10
    def makspos(self, x):
        self.maksRozmiar = x

    def dodajPozycje(self, pozycja):
        for i in self.pozycje:
            if i.nazwaTowaru == pozycja.nazwaTowaru:
                i.ileSztuk += pozycja.ileSztuk
                return
        if len(self.pozycje) < self.maksRozmiar:
            self.pozycje.append(pozycja)

    def obliczWartosc(self):
        k = 0
        s = 0
        for i in self.pozycje:
            k += i.obliczWartosc()
            s += i.wartoscZrabatem()
        return k,s

    def toString(self):
        for i in self.pozycje:
            print(i.toString())
        s = 'wartosc ' + str(self.obliczWartosc()[0]) + '\n' + 'wartosc z rabatem ' + str(self.obliczWartosc()[1])
        return s

    def usunPozycje(self, x):
        self.pozycje.pop(x)

    def edytujPozycje(self, x):
        nazwaTowaru = input('podaj nazwe ')
        cena = int(input('podaj cene '))
        liczba = int(input('podaj liczbe '))
        self.pozycje[x].nazwaTowaru = nazwaTowaru
        self.pozycje[x].cena = cena
        self.pozycje[x].ileSztuk = liczba

Pozycja('nazwa', 14.14, 15)
