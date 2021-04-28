from random import choices
from collections import Counter
from pprint import pprint

d20 = tuple(range(1, 21))
width = 5
order = 1
n = 100_000

data = choices(d20, k = n + width - 1)
histogram = Counter(sorted(data[i: i+width])[order] for i in range(n))
pprint(dict(Counter(histogram)))
