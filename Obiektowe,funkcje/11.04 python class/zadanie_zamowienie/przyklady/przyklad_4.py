class ShoppingCart(object):
    def __init__(self):
        self.item = None
        self.quantity = None
        self.price = None
        self.items = {}
        self._total_price = 0

    def add(self, item, price, quantity):
        if item in self.items:
            previous_quantity = self.items[item]['quantity']
            previous_price = self.items[item]['price']
            self.items[item] = {'quantity': previous_quantity + quantity,
                                'price': previous_price + price}
        else:
            self.items[item] = {'quantity':quantity, 'price':price}
        self._total_price += price * quantity

    @property
    def total_items_in_cart(self):
        return len(self.items) # better return a value instead of printing it

    @property
    def total_items_price_in_cart(self):
        return self._total_price

sc = ShoppingCart()
sc.add('book', 30, 1)
# sc.add('book', 132, 1)

sc.add('toothbrush', 4, 10)
# sc.add('toothbrush', 5, 20)

print(sc.total_items_in_cart)
print(sc.total_items_price_in_cart)