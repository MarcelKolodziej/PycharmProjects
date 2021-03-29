
# sum_integers_list.py
##def my_sum(my_integers):
##    result = 0
##    for x in my_integers:
##        result += x
##    return result
##
##list_of_integers = [1, 2, 3]
##print(my_sum(list_of_integers))

# sum_integers_args.py
##def my_sum(*args):
##    result = 0
##    # Iterating over the Python args tuple
##    for x in args:
##        result += x
##    return result
##
##print(my_sum(1, 2, 3))

# We can pass multiple arguments
# sum_integers_args_2.py
##def my_sum(*integers):
##    result = 0
##    for x in integers:
##        result += x
##    return result
##
##print(my_sum(1, 2, 3,4,5,7,33))

##operator * is not a list but a tuple.
##my_list = [1, 2, 3]
##my_list[0] = 9
##print(my_list)
##
##my_tuple = (1,2,3)
##my_tuple = (3,2,3,4,6)
##print(my_tuple)

# change_tuple.py
##my_tuple = (1, 2, 3)
##my_tuple[0] = 9
##print(my_tuple)

## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered and unindexed. No duplicate members.
## Dictionary is a collection which is unordered and changeable. No duplicate members.

#____________________________________
# concatenate.py
##def concatenate(**kwargs):
##    result = ""
##    # Iterating over the Python kwargs dictionary
##    for arg in kwargs.values():
##        result += arg
##    return result

##print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

##def concatenate(**words):
##    result = ""
##    for arg in words.values():
##        result += arg
##    return result
##    
##print(concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!"))

# concatenate_keys.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
