# Operatory logiczne:
# wzrost = 179
#
# if(wzrost > 180):
#     print('kobiety lubia to ;)')
# else:
#     print('smutna żaba')
# print('no i koniec...')

# wzrost=166
#
# if(wzrost>180):
#      print('kobiety lubią to ;)')
# elif(wzrost>170):
#      print('przeciętny wzrost')
# elif(wzrost>160):
#      print('do komandosów nie przyjmą')
# elif(wzrost>150):
#      print('wzrost nikczemny')
# else:
#      print('smutna żaba :( ')
# print('no i koniec...')

# Operatory logiczne w warunkach
# wzrost=185
# zarobki=1000000
# if(wzrost>180 and zarobki>10000):
#     print('gwiazda Tindera ;)')

# Pętla while

# x = 0
# while(x < 10):
#     print(x)
#     x+=1

        # Pętla for
# for x in range(1,11):
#     print(x)

# Pętla for z przeskokiem
# for x in range(1,20,3):
#     print(x)

# Pętla for z przeskokiem ujemnym
# for x in range(10,0,-1):
#  print(x)

        # Zagnieżdżanie pętli
# for y in range(1,11):
#     for x in range(1,11):
#         print('y={}, x={}'.format(y,x))


# y,x = 1,1
# while(y<10):
#     x = 1
#     while(x<=10):
#         print('y={}, x={}'.format(y,x))
#         x+=1
#     y+=1

#Break

for x in range(1,101):
 if(x%17.5==0):
     print("szukana liczba to {}".format(x))
     break

# Powyższy kod szuka pierwszej liczby z zakresu 1-100 podzielnej przez 17.5. Przeszukujemy zakres
# liczba po liczbie i sprawdzamy czy reszta z dzielenia tej liczby przez 17.5 wynosi 0. Jeśli tak, to jest
# to poszukiwana przez nas liczba i można przerwać dalsze poszukiwania z użyciem instrukcji break.

