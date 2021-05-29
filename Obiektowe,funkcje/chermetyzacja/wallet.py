import os

"""

Program do prowadzenia budżetu,
- Dodawanie przychodów i rozchodów
- rozchody podzielony na kategorie
- generowanie raportów przychodów i rozchodów


"""

class Budzet(object):
    def __init__(self):
        os.system('cls')
        self.budzet = float(input('Ile wynosi twój budzet?\n'))
        self.wydatki = self.budzet * 0.5
        os.system('cls')
        self.main()

    def main(self):
        print('\nYour budzet: ', '{:.2f}'.format(self.budzet))
        main_option = int(input('\nCo chcesz zrobic??\n1) Pokaz plan\n2) Pokaz wydatki\n3) Wyjscie\n'))
        if main_option == 1:
            self.wydatki_budzet()
        elif main_option == 2:
            self.pokaz_wydatki()
        else
    quit

    def wydatki_budzet(self):
        os.system('cls')
        print('Spending Budzet: ', '{:.2f}'.format(self.wydatki))
        wynajem = float(input('\nIle wynosi wynajem?\n'))
        rachunki = float(input('\nIle wynoszą miesięczne rachunki?\n'))
        food = float(input('\nIle wydajesz miesięczne na jedzenie?\n'))
        print('\nWydatki:\nWynajem: ', '{:.2f}'.format(wynajem), '\nRachunki: ', '{:.2f}'.format(rachunki), '\nJedzenie: ',
              '{:.2f}'.format(food))
        os.system('pause')
        os.system('cls')
        self.main()


Budzet()