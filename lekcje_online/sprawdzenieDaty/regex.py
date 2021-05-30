import re

pattern = re.compile(r'\d\d\d\d[-.]\d\d[-.]\d\d')
#pattern = re.compile(r'^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$')

with open('daty1.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)