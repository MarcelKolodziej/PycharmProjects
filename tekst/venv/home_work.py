# Dla podanego n i m, gdzie n < m, wyświetl wszystkie liczby całkowite zawierające się w przedziale [n, m], spełniające warunek:
#
# - są nieparzyste lub podzielne przez 5
#
# - w dzieleniu przez 3 dają resztę 2 i cyfrą jedności jest 3 lub 4
#
# - dzielą się przez 5, ale nie dzielą się przez 3.

# n = 5
# m = 33
# for i in range(n,m):
#     if i%3 == 2 or i%5 == 0:
#         print(i)
#         continue


# 4
# liczba = int(input("Podaj liczbe calkowita: "))
# cyfry = 0
# for i in range (liczba):
#     if(liczba%3 == 0):
#         cyfry+=cyfry
# print("Liczba cyfr podzielnych przez 3 podanej liczby to:", cyfry)

# Napisz program, który pobierze od użytkownika liczbę całkowitą n i wyświetla wartość sumę
# liczb nieparzystych z przedziału domkniętego < n. 2n >. Przykład: We: 5 Wy: 21 (czyli suma 5-1-7+9).



# number1 = int(input("Podaj liczbe całkowitą: "))
# number2 = number1 * 2
#
# for i in range(number1, number2):
#     print(i)

# n = int(input("Podaj liczbe n: "))
# suma = 0

# Zadanie 5
# Napisz program, który pobierze od użytkownika liczbę całkowitą n i wyświetla wartość sumę
# liczb nieparzystych z przedziału domkniętego < n. 2n >. Przykład: We: 5 Wy: 21 (czyli suma 5-1-7+9).

# for i in range(n, 2*n+1):
#     if i%2!=0:
#         suma +=i
# print("suma = ", suma)

#Zadanie 6
#Napisz program, który pobierze od użytkownika trzy liczby całkowite a,b,n i wyświetla
# na standardowym wyjściu wszystkie liczby całkowite z przedziału domkniętego < a.b >,
# które są podzielne przez n. Przykład: a = 5, b = 25, n = 5, Wynik: 5.10,15,20,25

# a = int(input("podaj a = "))
# b = int(input("podaj b = "))
# c = int(input("podaj c = "))
# for i in range(a,b+1):
#     if i%n==0:
#         print(i)


#Zadanie #4 solucja 1.0
# x = input("podaj x = ")
# ile = 0
# for i in range (len(x)):
#     if int(x[i]%3==0:
#         ile += 1
# print("cyfr podzielnych przez 3 jest ", ile)


# zadanie #4 solucja 2.0
# x = int(input("podaj x = "))
# ile = 0
# while x!=0:
#     if (x%10)%3==0:
#         ile += 1
#     x=x//10
# print("cyfr podzielnych przez 3 jest ", ile)

# n=25   #int(input("podaj liczbe gwiazdek"))
# for a in range(n):
#     for i in range(a):
#         print("*", end="")
#     print()

# 1
# n=40   #int(input("podaj liczbe gwiazdek"))
# for a in range(n):
#     for n in range(n-1):
#         print("*",)
#     print()

# n=10   #int(input("podaj liczbe gwiazdek"))
# for a in range(n):
#     for n in range(a*2):
#         print("", "*", end="")
#     print()


#a)
# n = 10
# for a in range(n):
#     for a in range(n-a):
#        print("*", end="")
#     print()


#b)
# n = 25
# for a in range(n):
#     for x in range(1, n-a):
#         print(" ", end="")
#     for x in range(1+a):
#         print("*", end="")
#     print()

#c)
# n = 25
# for a in range(n):
#     for i in range(0, a):
#         print(" ", end="")
#     for i in range(a, n-1):
#         print("*", end="")
#     print()


#d)
# a = 25
# for p in range (a):
#     for p in range(a-p):
#         print(" ", end="")
#     for i in range (p*2):
#         print('*', end="")
#     print()

# n = int(input("Podaj ilosc liczb"))
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()