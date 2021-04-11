class Uczen:
    imie = ""
    nazwisko = ""
    pesel = None

    def __init__(a, imie, nazwisko, pesel):
        a.imie = imie
        a.nazwisko = nazwisko
        a.pesel = pesel

    def przedstawienie_ucznia(a):
        print("-----")
        print("Imie" + " : " + a.imie)
        print("Nazwisko" + " : " + a.nazwisko)
        print("Pesel" + " : " + str(a.pesel))

def zapytaj_o_dane(message=''):
    user_input = ''
    while not user_input:
        user_input = input(message)
    return user_input

def wypelnienie_danych(values, placement, length):
    placement = []
    while len(placement) < length:
        imie = zapytaj_o_dane("Podaj Imie: ")
        nazwisko =  zapytaj_o_dane("Podaj Nazwisko: ")
        pesel = zapytaj_o_dane("Podaj pesel: ")
        values = Uczen(imie, nazwisko, pesel)
        placement.append(values)
    return placement

class UczenSzkoly(Uczen):

    nazwaSzkoly = ""

    def UstawSzkole(self, nazwaSzkoly):
        self.nazwaSzkoly = nazwaSzkoly


class UczenKlasy(UczenSzkoly):
    nazwaKlasy = ""

    def UstawKlase(self, nazwaKlasy):
        self.nazwaKlasy = nazwaKlasy

    def __init__(self, imie, nazwisko, pesel, nazwaSzkoly, nazwaKlasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.nazwaSzkoly = nazwaSzkoly
        self.nazwaKlasy = nazwaKlasy

def main():
    # users = wypelnienie_danych('user', 'users', 1)
    # for a in range(len(users)):
    #     users[a].przedstawienie_ucznia()
    # dopisac imputy, "nie na sztywno"
    u1 = UczenKlasy("Marcel", "Kolod", 399138983, "Sienkiewicz", "1C")
    u1.przedstawienie_ucznia()

if __name__ == '__main__':
    main()




