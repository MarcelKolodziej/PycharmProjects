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
     self.balans = float(input("Ile pieniedzy chcesz dodac do budzetu?"))
     self.wydatki = self.wydatki
     os.system('cls')
     self.main()

    def main(self):
     print('\nTwoj budzet to: $', '{:.2f}'.format(self.budget))
     main_option = int(input('\nWhat do you want to do?\n2) View Spending Budget\n3) Exit\n'))
     if main_option == 1:
         self.budget_plan()
     elif main_option == 2:
         self.spending_budget()
     else:
         quit


Budzet()