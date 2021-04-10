class auto:
    kolor=""
    rok_produkcji=None
    def __init__(self,kolor,rok_produkcji):
        self.kolor = kolor
        self.rok_produkcji = rok_produkcji


samochod1 = auto("bialy",2011)
# samochod1.kolor = "czerwony"
# samochod1.rok_produkcji = 2010

samochod2 = auto("czarny", 1998)
# samochod2.kolor = "zielony"
# samochod2.rok_produkcji = 1999
print("kolor 1 samochodu: "+samochod1.kolor)
print("rok produkcji 1 samochodu: "+str(samochod1.rok_produkcji))

print("kolor 2 samochodu: "+samochod2.kolor)
print("rok produkcji 2 samochodu: "+str(samochod2.rok_produkcji))