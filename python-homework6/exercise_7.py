cart_1 = {'bread':1, 'eggs': 5}
cart_2 = {'milk':2, 'ham': 8}

def total_price(cart):
    total = 0
    for price in cart.values():
        total += price
    return total

print(total_price(cart_2))
print(total_price(cart_1))