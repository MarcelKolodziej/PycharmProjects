import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
Elems = exampleSoup.select('#author')
type(Elems)
print(len(Elems))
print(type(Elems[0]))
print(Elems[0].getText())
print(str(Elems[0]))
print(Elems[0].attrs)