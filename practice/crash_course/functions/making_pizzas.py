import pizza

pizza.make_pizza(16, 'peperoni')
pizza.make_pizza(16, 'peperoni', 'green papers', 'extra cheese')

# import function from module
from pizza import make_pizza

make_pizza(16, 'peperroni')
make_pizza(16, 'peperroni', 'green pepers', 'extra cheese')

# import module with a alias
from pizza import make_pizza as mp

mp(16, 'peperroni')
mp(16, 'peperroni', 'green pepers', 'extra cheese')


#alias for module
import pizza as p

p(16, 'pepperoni')
p(16, 'peperroni', 'green pepers', 'extra cheese')

#import everything from module using *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza((16, 'peperroni', 'green pepers', 'extra cheese'))