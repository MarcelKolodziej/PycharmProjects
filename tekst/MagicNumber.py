from random import randint

m_number = randint(0,10)
my_Number = int(input("Podaj liczbe:"))
counter = 1

while m_number != my_Number:
    my_Number = int(input("Podaj liczbe: "))
    counter += 1

if counter < 5:
    print("Gratulacje mr. Mastermind!",  )
elif counter > 5:
    print("Dobrze ale mogło być lepiej byczku udalo sie za", counter, "razem")
else:
    print("Niestety ale jasnowidzem nie zostaniesz...")