lista=["Samanta","Elvis","BożydarrrrrAAA"]

m_literki = 0
d_literki = 0

for x in range(len(lista)):
    for i in range(len(lista[x])):
        if lista[x][i] >= 'a' and lista[x][i] <= 'z':
            m_literki += 1
        if lista[x][i] >= 'A' and lista[x][i] <= 'Z':
            d_literki += 1
print("Liczba malych literek =", m_literki, "Liczba duzych literek", d_literki)