# Dla wprowadzonego tekstu policz ile jest małych liter, wielkich liter oraz liczb.
#Silne hasło zawiera minimum 8 znaków, małe i duże litery oraz cyfry.

cyfry= 0
m_litery = 0
d_litery = 0

text = input("Wprowadz tekst")
for x in range(0,len(text)): # możemy wprowadzić tylko jedną zmienną.
    if text[x] >= '0' and text[x] <= '9':
        cyfry += 1
    elif text[x] >= 'a' and text[x] <= 'z':
        m_litery += 1
    elif text[x] >= 'A' and text[x] <= 'Z':
        d_litery += 1
if cyfry >= 0 and m_litery > 0 and d_litery > 0 and 8 and len(text) > 8:
    print("Twoje hasło jest silne")
else:
    print("Twoje haslo za silne to nie jest")
print("Tekst zawiera cyfry ", cyfry,"\n",  "małe litery", m_litery, "duze litery\n", d_litery)
