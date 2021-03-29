## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered and unindexed. No duplicate members.
## Dictionary is a collection which is unordered and changeable. No duplicate members.

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
##def concatenate(**kwargs):
##    result = ""
##    # Iterating over the keys of the Python kwargs dictionary
##    for arg in kwargs:
##        result += arg
##    return result
##
##print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

### print my_list.py
##my_list = [1, 2, 3]
##print(my_list)
##print(*my_list) # In this case, the output is no longer the list itself, but rather the content of the list

# unpacking_call.py
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
