import sys

#Pokaz menu glowne
def mainMenu():
    while True:
        print()
        print('''### ZAMOWIENIE ###

        Wybierz co chcesz zrobic:

        1. Pokaz zamowienie
        2. Dodaj produkt do zamowienia
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        7. Exit
        ''')

        selection = input("Make your selection: ") # Ask the user to make a selection

        # Determine which action to perform based on the user's selection
        if selection == "1":
            pokazListe()
        # elif selection == "2":
        #     addItem()
        # elif selection == "3":
        #     removeItem()
        # elif selection == "4":
        #     checkItem()
        # elif selection == "5":
        #     listLength()
        # elif selection == "6":
        #     clearList()
        # elif selection == "7":
        #     sys.exit()
        else:
            print("You did not make a valid selection.")

lista_produktow = {'Chleb':  [3.50, 500], 'Cukier': [4.00,1000], }  # Add a few items to the shopping list

# Displays all items on the shopping list
def pokazListe():
    print()
    print("--- Zamowienie ---")
    for i in lista_produktow:
        print("* " + i )

class Pozycja():
    def __init__(self, nazwaTowaru, ileSztuk, cena):
        self.nazwaTowaru = nazwaTowaru
        self.ileSztuk = ileSztuk
        self.cena = cena

    def obliczWartosc(self):
        pass# return pozycjaZamowienia
    def toString(self):
        pass# return string nazwaTowaru

mainMenu()