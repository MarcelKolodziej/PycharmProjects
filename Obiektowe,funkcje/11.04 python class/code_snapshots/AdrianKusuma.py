# get total price of a product
def get_price(product, quantity):
    subtotal = price_dict[product] * quantity
    print(product + ': $' + str(price_dict[product]) + ' x ' + str(quantity)\
          + ' = ' + str(subtotal))
    return subtotal
# get discount according to bill price
def get_discount(bill_price, membership):
    discount = 0
    if bill_price >= 25:
        if membership == 'gold':
            bill_price = bill_price * 0.75
            discount = 25
        elif membership == 'silver':
            bill_price = bill_price * 0.85
            discount = 15
        elif membership == 'bronze':
            bill_price = bill_price * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + \
              ' membership at total price no less than $25')
    return bill_price
price_dict = {'biscuit': 2, 'fish': 3, 'chicken': 5, 'cabbage': 2, 
              'potato': 0.5, 'tomato': 0.5, 'bread': 2, 'egg': 0.2, 'oil': 4, 
              'celery': 2}
buying_dict = {'biscuit':2, 'chicken': 3, 'egg': 20}
bill_price = 0
for key, value in buying_dict.items():
    bill_price += get_price(key, value)
membership = 'gold'
bill_price = get_discount(bill_price, membership)
print('The total price is $' + str(bill_price))