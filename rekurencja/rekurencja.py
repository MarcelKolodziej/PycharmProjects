# def ciag(n):
#     if (n == 0):
#         return 0
#     if (n == 1):
#         return 1
#
#     return ciag(n - 1) + 2 * ciag(n - 2)
#
# n = int(input("Podaj miejsce w ciagu:"))
# print("Numer w ciągu:", ciag(n))


#liczby 2,1,5,7,17,31,65,127,257,511
# def ciag_numerowany(n):
#     if (n == 1):
#         return 2
#     if (n == 2):
#         return 1
#
#     return ciag_numerowany(n - 2 ) *2 + ciag_numerowany(n-1)
#
# n = int(input("Podaj miejsce w ciagu:"))
# print("Twój numer to:", ciag_numerowany(n))




# liczby 1,1,1,2,2,3,5,7,9...
# solucja n = (n-3) + n(-2)

# def ciag_skoczek(n):
#     if (n == 1):
#         return 1
#     if (n == 2):
#         return 1
#     if (n == 3):
#         return 1
#
#     return ciag_skoczek(n - 3) + ciag_skoczek(n - 2)
#
# n = int(input("Podaj miejsce w ciagu:"))
# print("Numer:", ciag_skoczek(n))

# rekurencyjne szukanie danel liczb w liscie



def szukaj(lista,indeks):
    if indeks == -1:
        return 0
    if lista[indeks] == int(input("Podaj liczbe szukaną")):
        return szukaj(lista,indeks-1)+1
    else:
        return szukaj(lista,indeks-1)

lista = [4,4,5,6,3,5,6,4,5,64,4]
print(szukaj(lista,len(lista)-1))
