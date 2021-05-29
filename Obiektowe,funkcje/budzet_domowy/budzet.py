from getBudget import currentBudget, path
"""

Program do prowadzenia budżetu,
- Dodawanie przychodów i rozchodów
- rozchody podzielony na kategorie
- generowanie raportów przychodów i rozchodów


"""

def main():
    endProgram = 'no'
    totalBudget = currentBudget
    while endProgram == 'no':
        print("""
        1.Dodaj wydatek
        2.Dodaj przychod
        3.Pokaz Balans
        4.Zapisz balans
        5.Wyjdz bez zapisywania
        """)
        choice = int(input('enter your selection: '))
        if choice == 1:
            totalBudget = dodajWydatek(totalBudget)
        elif choice == 2:
            totalBudget = dodajPrzychod(totalBudget)
        elif choice == 3:
            print('Twój balans wynosi {0}'.format(totalBudget))
        elif choice == 4:
            zapiszBudzet(totalBudget)
            print('Dzięki za zapisanie ;-)')
        elif choice == 5:
            endProgram = 'yes'
            print('Do zobaczenia!')
        else:
            print('Nieprawidłowa komenda')

def dodajWydatek(totalBudget):
    wydatek = float(input("Podaj ile wynosi wydatek"))
    wydatekWMiesiacu = int(input("Ile razy miesiecznie"))
    calosciowy_wydatek = wydatek * wydatekWMiesiacu
    if totalBudget - calosciowy_wydatek >= 0:
        calosciowy_wydatek = totalBudget - calosciowy_wydatek
        print('Wydatek został zaakceptowany, twój pozostały budżet to: ${0}'.format(totalBudget))
        return totalBudget
    else:
        print('Wydatek został odrzucony ponieważ budżet tego nie udźwignie.')
        return totalBudget

def dodajPrzychod(totalBudget):
    przychod = float(input("Podaj nowy miesieczny przychod"))
    totalBudget = totalBudget + przychod
    print('Twój nowy budżet wynosi: {0}'.format(totalBudget))
    return totalBudget

def zapiszBudzet(totalBudget):
    with open(path, 'w') as f:
        f.write(str(totalBudget))
    f.close()

main()