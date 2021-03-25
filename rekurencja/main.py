import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select('#author')
print(type(elems)) # check what type is bs4 element

len(elems) # check length of bs4

type(elems[0])

elems[0].getText()