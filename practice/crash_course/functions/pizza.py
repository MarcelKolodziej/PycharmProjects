# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pappers', 'extra cheese')

# def make_pizza(*toppings):
#     """Summarize the piza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
#
# make_pizza('pepperoni')
# make_pizza('mushrooms','green papers', 'extra cheese')

def make_pizza(size, *toppings):
    print(f"\nMaking pizza {size}-inch, with the following toppings")
    for topping in toppings:
        print(topping)

make_pizza(12,'cheese')
make_pizza(15,"cheese", 'mushrooms', 'extra cheese')