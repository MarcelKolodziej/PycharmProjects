t=input("Podaj tekst")
nowy=""
kod= int(input("Podaj kod"))

for i in range(len(t)):
    if t[i]>='a' and t[i]<='z':
        if (ord(t[i]) + kod%26)>122:
            nowy += chr(ord(t[i]) + kod%26-26)
        else:
            nowy+=chr(ord(t[i])+kod%26)
    if t[i]>="A" and t[i]<='Z':
        if (ord(t[i]) + kod%26)>90:
            nowy+=chr(ord(t[i]) + kod%26-26)
    else:
            nowy+=chr(ord(t[i])+kod%26)
print(nowy)
