# Napisz program w którym, w zależności od wyboru
# użytkownika, przeliczysz podaną wartość Mil na kilometry, stopni
# Celcjusza na Fahrenheita, kilogramów na funty, litrów na galony, km/h na m/s.
wybor = int(input("Wybor: \n 1. Mile i kilometry, \n 2. Celcjusze i Fahrenheity \n 3. Kilogramy i funty \n 4. Litry i galony 5. Km/h i m/s "))

if wybor == 1:
    wybor2 = int(input("1. Mile na Kilometry \n 2. Kilometry na Mile "))
    if wybor2 == 1:
        zmienna1 = float(input("Podaj ilosc mil"))
        print(zmienna1 * 0.62137, "mil")

    if wybor2 == 2:
        zmienna1 = float(input("Podaj ilosc kilometrow"))
        print(zmienna1 * 1,609344, "kilometrow")

if wybor == 2:
    wybor2 = int(input("1. Celcjusz na Fahrenheity \n 2.  Fahrenheity na Celcjusz "))
    if wybor2 == 1:
        zmienna1 = float(input("Podaj ilosc Celcjuszy"))
        print(zmienna1 - 32 / 1.8000 ,"Fahrenheita")

    if wybor2 == 2:
        zmienna1 = float(input("Podaj ilosc Fahrenheita "))
        print(zmienna1 * 33.8, "Celcjusza")

if wybor == 3:
    zmienna1 = float(input("Podaj ilosc Kilogramów"))
    print(zmienna1 * 2.20462262, "Funta")

if wybor == 4:
    zmienna1 = float(input("Podaj ilosc Litrów"))
    print(zmienna1 * 0,264172052, "Galona" )
if wybor == 5:
    zmianna1 = float(input("Podaj ilość kilometrów"))
    print(zmianna1 * 1000, "m/s" )