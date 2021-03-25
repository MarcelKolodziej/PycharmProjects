# max 5 znakow, wyswietla małe litery, duże litery i cyfry

a = input("Podaj tekst max 5 znakow")
cyfry= 0
m_litery = 0
d_litery = 0

#1 znak
if a[0]>= '0' and a[0]<= '9':
    cyfry+=1
if a[0]>= 'a' and a[0]<= 'z':
    m_litery+=1
if a[0]>= 'A' and a[0]<= 'Z':
    d_litery+=1

#2 znak
if a[1]>= '0' and a[1]<= '9':
    cyfry+=1
if a[1]>= 'a' and a[1]<= 'z':
    m_litery+=1
if a[1]>= 'A' and a[1]<= 'Z':
    d_litery+=1

#3 znak
if a[2]>= '0' and a[2]<= '9':
    cyfry+=1
if a[2]>= 'a' and a[2]<= 'z':
    m_litery+=1
if a[2]>= 'A' and a[2]<= 'Z':
    d_litery+=1

#4 znak
if a[3]>= '0' and a[3]<= '9':
    cyfry+=1
if a[3]>= 'a' and a[3]<= 'z':
    m_litery+=1
if a[3]>= 'A' and a[3]<= 'Z':
    d_litery+=1

#5 znak
if a[4]>= '0' and a[4]<= '9':
    cyfry+=1
if a[4]>= 'a' and a[4]<= 'z':
    m_litery+=1
if a[4]>= 'A' and a[4]<= 'Z':
    d_litery+=1

print("Tekst zawiera", cyfry, "cyfr", m_litery, "malych liter", d_litery, "duzych liter")