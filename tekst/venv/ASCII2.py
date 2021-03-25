text = input("Podaj tekst")
k = int(input("Podaj kod"))
new = ""
kod = k
for i in range(len(t)):
    if t[i]>='a' and t[i]<='z':
        if (ord(t[i]) - kod%26)<97:
            nowy += chr(ord(t[i])