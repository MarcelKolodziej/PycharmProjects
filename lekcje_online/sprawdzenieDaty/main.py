""" Wypisanie prawidłowego formatu daty z pliku tekstowego """
import os
import re

filename = 
filesize = os.path.getsize("daty.txt")

if filesize == 0:
    print("The file is empty: " + str(filesize))
else:
    print("The file is not empty: " + str(filesize))

pattern = re.compile(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$')

for line in open("daty.txt"):
    for match in re.finditer(pattern, line):
        print(line)